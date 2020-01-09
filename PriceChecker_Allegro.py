import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://allegro.pl/oferta/antena-tv-pokojowa-dvb-t-dab-fm-wewnetrzna-100dbuv-7892924025?bi_c=swieta2019&bi_m=mpage&' #for another website check title and price

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'} # your user-agent


def check_price():
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_='_1sjrk').get_text()
    price = soup.find(class_='_1t4ky').get_text()
    converted_price = int(price[0:2])

    if(converted_price < 70):
        send_mail()

    print(title.strip())
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email', 'password') # i used gmail, so for me there will be my email and my app password

    subject = 'Price fell down!'
    body = 'Check the allegro link! https' #you can put here full link

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'myemail', #my email
        'outputemail', #output email
        msg
    )
    print('email has been sent!')
    server.quit()

    
while(True):

    check_price()
    time.sleep(60 * 60)