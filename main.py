import re
import sys
import time
from datetime import datetime

import cv2
import numpy as np
import requests
from geopy.geocoders import Nominatim
from PIL import ImageGrab

import Ai

start_time = time.time()

FORMAT = '%Y-%m-%d %H-%M-%S'
file_name = f'image/{datetime.now().strftime(FORMAT)}.png'
geolocation = Nominatim(user_agent='geotest')

x, y = 0, 0
im = ImageGrab.grab(bbox=(x, y, x+1250, y+900), all_screens=True)
img_np = np.array(im)
frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
cv2.imwrite(file_name, frame)
txt = Ai.convert(file_name)
list = re.findall('[0-9.]+', txt)
for i in list:
    if '.' in i:
        index = list.index(i)
        break
location = str(geolocation.reverse(f'{list[index]},{list[index + 1]}')).split(', ')

# channel = [997371332796895312]
channel = [997371332796895312, 944193820503994408, 1031438474651381791]

level = sys.argv[1].replace('+', '強').replace('-', '弱')
sec = int(sys.argv[2])

try:
    msg = '\n- 慎防強烈搖晃，就近避難「趴下、掩護、穩住」' if int(level) >= 3 else ''
except:
    msg = '\n- 慎防強烈搖晃，就近避難「趴下、掩護、穩住」'

header = {
    'authorization': 'NDEzMjcxOTc1Nzc1OTYxMDk5.GI3eNz.iApStbvLfKyqdp1ly5QKSELc0RCSlj2Rtt1rGw'
}

end_time = time.time()

data = {
    'content': f"""```diff
- {list[index - 5]}/{list[index - 4]} {list[index - 3]}:{list[index - 2]}:{list[index - 1]} 左右發生顯著有感地震{msg}

新北市預估震度: {level} 級
預估抵達時間: {int(list[index + 6]) - int(end_time - start_time)} 秒
預估震央: 北緯 {list[index]} 度, 東經 {list[index + 1]} 度 ({''.join(location[::-1][2:])})
預估深度: {list[index + 2]} 公里
預估規模: {list[index + 3]}
預估最大震度: {list[index + 4]} 級

+ 資料來源: 地牛 Wake Up!
+ 使用技術: Tesseract OCR 影像辨識
```"""
}

# files = {
#     'file': (f'./{file_name}', open(f'./{file_name}', 'rb')),
# }

for i in channel:
    try:
        res = requests.post(f'https://discord.com/api/v9/channels/{i}/messages', headers=header, data=data)
    except: ...
# input()