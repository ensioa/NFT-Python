# -*- coding: utf-8 -*-

"""

外部功能测试
"""

foods = [{
  "_id": {
    "$oid": "645f41d56fd3f673b4c665e3"
  },
  "name": "�����¸�ɶ�緹��",
  "imgUrl": "http://127.0.0.1:8803/upload\\20230513\\1683964369964.png",
  "classification": {
    "$oid": "645e7c0d81f3a427028d1e34"
  },
  "stratPrice": 3245,
  "introduce": "��ʿ������ط�",
  "nowPrice": [
    4745,
    5045,
    5345,
    5645,
    5345,
    5645,
    5345,
    5645,
    5945,
    6245,
    6545,
    6845,
    7145,
    6845,
    7145,
    6845,
    6545,
    6845,
    6545,
    6245,
    5945,
    5645,
    5345,
    5645,
    5945,
    6245,
    5945,
    5645,
    5945,
    5645
  ],
  "config": {
    "starts": 3245,
    "end": 8245,
    "space": 300,
    "add": 0
  },
  "isShow": True,
  "userSell": [],
  "date": "2023-05-13 15:51:48",
  "SWl": True,
  "__v": 0
},
{
  "_id": {
    "$oid": "645f41dc665e3222222"
  },
  "name": "2222",
  "imgUrl": "http://127.0.0.1:8803/upload\\20230513\\1683964369964.png",
  "classification": {
    "$oid": "645e7c0d81f3a427028d1e34"
  },
  "stratPrice": 3245,
  "introduce": "��ʿ������ط�",
  "nowPrice": [
    47445,
    50445,
    54345,
    56445,
    53545,
    56455,
    53455,
    5645,
    5945,
    6245,
    6545,
    6845,
    7145,
    6845,
    7145,
    6845,
    6545,
    6845,
    6545,
    6245,
    5945,
    5645,
    5345,
    5645,
    5945,
    6245,
    5945,
    5645,
    5945,
    5645
  ],
  "config": {
    "starts": 3245,
    "end": 8245,
    "space": 300,
    "add": 0
  },
  "isShow": True,
  "userSell": [],
  "date": "2023-05-13 15:51:48",
  "SWl": True,
  "__v": 0
},
{
  "_id": {
    "$oid": "3333333333"
  },
  "name": "33333333333333",
  "imgUrl": "http://127.0.0.1:8803/upload\\20230513\\1683964369964.png",
  "classification": {
    "$oid": "222222222222"
  },
  "stratPrice": 3245,
  "introduce": "��ʿ������ط�",
  "nowPrice": [
    4745,
    5045,
    5345,
    5645,
    5345,
    5645,
    5345,
    5645,
    5945,
    6245,
    6545,
    6845,
    7145,
    6845,
    7145,
    6845,
    6545,
    6845,
    6545,
    6245,
    5945,
    5645,
    5345,
    5645,
    5945,
    6245,
    5945,
    5645,
    5945,
    5645
  ],
  "config": {
    "starts": 3245,
    "end": 8245,
    "space": 300,
    "add": 0
  },
  "isShow": True,
  "userSell": [],
  "date": "2023-05-13 15:51:48",
  "SWl": True,
  "__v": 0
},
{
  "_id": {
    "$oid": "44444444444444"
  },
  "name": "4444444444444",
  "imgUrl": "http://127.0.0.1:8803/upload\\20230513\\1683964369964.png",
  "classification": {
    "$oid": "222222222222222"
  },
  "stratPrice": 3245,
  "introduce": "��ʿ������ط�",
  "nowPrice": [
    4745,
    5045,
    5345,
    5645,
    5345,
    5645,
    5345,
    5645,
    5945,
    6245,
    6545,
    6845,
    7145,
    6845,
    7145,
    6845,
    6545,
    6845,
    6545,
    6245,
    5945,
    5645,
    5345,
    5645,
    5945,
    6245,
    5945,
    5645,
    5945,
    5645
  ],
  "config": {
    "starts": 3245,
    "end": 8245,
    "space": 300,
    "add": 0
  },
  "isShow": True,
  "userSell": [],
  "date": "2023-05-13 15:51:48",
  "SWl": True,
  "__v": 0
}]


def getUniqueItems(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# 分类ID
classification = []
for food in foods:
    classification.append(food['classification']['$oid'])
classification = getUniqueItems(classification)
classification_resualt = []
print()
print(classification)

classification_resualt = []
for c in classification:
    price_temp = []
    for food in foods:
        if c == food['classification']['$oid']:
            price_temp.append(food['nowPrice'])
    price_temp1 = []

    for i in range(0, len(price_temp[0])):
        t = 0
        for price in price_temp:
            t += price[i]
        price_temp1.append(t)
    classification_resualt.append({'classification':c, 'prices': price_temp1})
print(classification_resualt)