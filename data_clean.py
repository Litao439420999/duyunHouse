import re
import csv

filename = "anjuke1015.csv"
with open(filename,'r', encoding='utf-8') as f:    #
    reader = csv.reader(f)
    context = [line for line in reader]

with open("anjuke-m1015.csv", "w", encoding="utf-8", newline="")as f:
    writer = csv.writer(f)
    for line in context:
        line = [x.strip() for x in line]  # 去除每个数据项的空白符和换行符
        house_name = line[0]
        house_type = line[1]
        houseaddress = line[5].split('\n')
        house_zone = houseaddress[0].strip()
        house_zhuzhi = line[5].split('\n')[-1].split(' ')[-1].strip()
        house_address = line[5]
        price = line[2].split('元')[0]
        house_area = line[3].split('平')[0]
        house_location = line[4]
        writer.writerow([house_name, house_type, house_zone, house_zhuzhi, price, house_area, house_location])
print("数据项转换成功！")
