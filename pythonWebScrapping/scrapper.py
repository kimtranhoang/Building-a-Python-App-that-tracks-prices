import requests
from bs4 import BeautifulSoup
import smtplib
import time
from urllib.parse import urlparse
URL = 'https://www.amazon.com/Apple-iPhone-XR-Fully-Unlocked/dp/B07P6Y7954/ref=sr_1_2?dchild=1&keywords=iphone&qid=1588429075&sr=8-2'
# headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

def check_price():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    # products = soup.find_all('div')
    print(soup)
    # for product in products:
    #     # if 'data-price' in product.keys():
    #     if product.has_attr('_341bF0'):
    #         if int(product['_341bF0']) > 500000:
    #             print(product['shopee-search-item-result__item'], product['_341bF0'])
    # print(title[0])

    # for data in title:
    #     print(data['data-title'], data['data-price'])
    # print(title[0]['data-title'])


    

    # print(title)


check_price()
    # print(soup.find_all('span'))
    # for data in soup.find_all('span', id_="priceblock_ourprice"):
    #     price = data.get_text()
    #     print(float(price.strip()[1:6]))


    # converted_price = float(price[0:3])

    # if(converted_price < 150.00):
    #     send_mail()

  
    # print(converted_price)

# def send_mail():
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()

#     server.login('hoangkim.9296@gmail.com', 'vmvwolvlotwcurjl')

#     subject = 'Price fell down'
#     body = 'Check the amazon link https://www.amazon.de/dp/B07KD8R6MJ?ref_=nav_em_0_2_9_4__k_mvk'

#     msg = f"Subject: {subject}\n\n{body}"

#     server.sendmail(
#         'hoangkim.9296@gmail.com',
#         'kimtranhoang92@gmail.com',
#         msg
#     )
#     print("Email has been sent")
#     server.quit

# while(True):
#     check_price()
#     print("done")
#     time.sleep(60)