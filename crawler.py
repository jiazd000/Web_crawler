# -*- coding: utf-8 -*-
# import MySQLdb
import requests
from bs4 import BeautifulSoup
# import json
from database import get_database,get_tables,insert_data

def get_links(url):
    response = requests.get(url)
    # print response.text
    # response=con.decode('utf-8','ignore')
    # response.encoding='utf-8'
    # print response.encoding

    soup = BeautifulSoup(response.text, 'html.parser')
    links_div = soup.find_all('div', class_="pic-panel")
    links = [div.a.get('href') for div in links_div]
    # print links_div
    return links


def get_info(url):
    house_response = requests.get(url)
    house_soup = BeautifulSoup(house_response.text, 'html.parser')

    price = house_soup.find('span', class_="total").text
    unit = house_soup.find('span', class_="unit").text.strip()
    house_info = house_soup.find_all('p')

    houseNum = house_soup.find('span', class_="houseNum").text[5:]

    area = house_info[0].text[3:].strip()
    layout = house_info[1].text[5:]
    floor = house_info[2].text[3:]
    direction = house_info[3].text[5:].strip()

    subway = house_info[4].text[4:]
    village = house_info[5].text[3:9]
    place = house_info[6].text[3:].strip()
    time = house_info[7].text[4:]
    # print subway

    house = {

        '链家编号': houseNum,
        '价格': price,
        '单位': unit,
        '面积': area,
        '户型': layout,
        '楼层': floor,
        '朝向': direction,
        '发布时间': time,
        '地铁': subway,
        '小区': village,
        '位置': place
    }

    return house


if __name__ == '__main__':

    db=get_database()
    get_tables(db)

    link_url = 'https://bj.lianjia.com/zufang/haidian/'
    house_url = get_links(link_url)
    for i in range(len(house_url)):
        house1 = get_info(house_url[i])
        h = house1['位置']
        print(h)
        insert_data(db,house1)
