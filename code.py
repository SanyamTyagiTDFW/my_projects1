import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/Apple-AirPods-Wireless-Charging-Case/dp/B07QDRYVCZ/ref=sr_1_2?keywords=airpods&qid=1572433404&s=shoes&sr=8-2"

headers = {
    "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle")
    title = title.get_text()
    price = soup.find(id="priceblock_ourprice")
    price = price.get_text()
    converted_price = float(price[2:4]+price[5:8])
    print(converted_price)
    print(title.strip())
    if (converted_price) <= 14000.0:
        send_mail()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("tyagisanyam01@gmail.com", "gqaxuhzgkwwdwhgx")

    subject = "hey!! price fell down"
    body = "check the amazon link https://www.amazon.in/Apple-AirPods-Wireless-Charging-Case/dp/B07QDRYVCZ/ref=sr_1_2?keywords=airpods&qid=1572433404&s=shoes&sr=8-2 "

    msg = f"subject:{subject}\n\n{body}"

    server.sendmail(
        "tyagisanyam01@gmail.com",
        "vksingh943@gmail.com",
        msg
    )
    print("hey email has been sent!!")
    server.quit()

while(True):
    check_price()
    time.sleep(60*60*12)

