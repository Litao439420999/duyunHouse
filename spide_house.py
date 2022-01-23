from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import time
import re
import string

csv_file = open("anjuke1015.csv", "w+", encoding='utf-8', newline='')  # encoding='utf-8'
csv_writer = csv.writer(csv_file, delimiter=',')

def getdata():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87."
    }
    url_list = []
    for i in range(20):
        if i == 0:
            url = 'https://qn.zu.anjuke.com/fangyuan/duyun/px3'
            url_list.append(url)
        else:
            url = 'https://qn.zu.anjuke.com/fangyuan/duyun/px3-p'+str(i + 2) + '/'
            url_list.append(url)

    for i in range(len(url_list)):
        response = requests.get(url_list[i], headers=headers)  #
        # response = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'lxml')  # lxml

        totaldivlist = soup.find_all("div", attrs={"class", "zu-itemmod"})  # 每页中房源信息列表
        lenth = len(totaldivlist)  # 每页房源的数目
        for j in range(lenth):
            # 房源名
            house_info = totaldivlist[j].find("div", attrs={"class", "zu-info"})
            house_a = house_info.find(name="a")
            house_b = house_a.find_all(name="b")
            house_name = house_b[0].text
            # 房源的链接link
            house_u = house_info.find(name="a")
            house_url = house_u['href']
            # 户型
            house_t = totaldivlist[j].find("p", attrs={"class", "details-item tag"})
            house_ty = house_t.find_all(name="b")
            house_area = ''
            house_type = ''
            for k in range(len(house_ty)):
                if k == 0:
                    house_type += house_ty[k].text + '室'
                elif k == 1:
                    house_type += house_ty[k].text + '厅'
                else:  # 房源面积
                    house_area = house_ty[k].text + '平米'
            # 户型朝向
            location = totaldivlist[j].find("span", attrs={"class", "cls-2"})
            house_location = location.text
            # 房源地址
            addresp = totaldivlist[j].find("address", attrs={"class", "details-item"})
            address = addresp.text
            #address = address_a.text
            # 房价
            price_span = totaldivlist[j].find("div", attrs={"class", "zu-side"})
            price = price_span.find('b').text + '元/月'

            csv_writer.writerow([house_name, house_type, price, house_area, house_location, address, house_url])
            baibai_x = (i + 1) * (101 * 100)
            baifen_y = 101 * (101 * 40)
            print("爬取进度" + str(baibai_x / baifen_y))
        print("下一页页开始。。。\n")
    print("数据下载结束！")


if __name__ == '__main__':
    csv_writer.writerow(["房源名称", "户型", "价格", "面积", "朝向", "地址","链接"])
    getdata()

