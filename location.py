import math
import re

import requests
from bs4 import BeautifulSoup


class Location():

    def __init__(self, latitude: float, longitude: float) -> None:
        """
        latitude 緯度

        longitude 經度
        """
        self.latitude = latitude
        self.longitude = longitude

    def getDistanceTo(self, target) -> float:
        """
        KM
        """
        dLat = (target.latitude - self.latitude) * math.pi / 180.0
        dLon = (target.longitude - self.longitude) * math.pi / 180.0

        lat1 = self.latitude * math.pi / 180.0
        lat2 = target.latitude * math.pi / 180.0

        a = math.sin(dLat / 2) ** 2 + math.sin(dLon / 2) ** 2 * math.cos(lat1) * math.cos(lat2)

        return 12742 * math.asin(a ** 0.5)
    
    def getAddress(self) -> str:
        sea = {'台灣海峽', '東海', 'Bashi Channel', '菲律賓海', '南海'}
        res = requests.get(f'https://www.google.com/maps/place/{self.latitude},{self.longitude}')
        soup = BeautifulSoup(res.text, "html.parser")
        address = soup.find("meta", itemprop= 'description').get('content')
        
        return '外海' if address in sea else re.sub(r'^\d+|\d+[號]', '', address)

class City():

    Taipei = Location(25.0331574, 121.5668777)    # 台北 信義
    NewTaipei = Location(24.9899673, 121.4246321) # 新北 樹林
    Taoyuan = Location(24.9939190, 121.3016657)   # 桃園 桃園
    Taichung = Location(24.1658213, 120.6336717)  # 台中 西屯
    Chiayi = Location(23.4786578, 120.4534596)    # 嘉義 東區
    Tainan = Location(22.9945789, 120.1688523)    # 台南 安平
    Kaohsiung = Location(22.6270750, 120.3625250) # 高雄 鳳山
    Yilan = Location(24.7520373, 121.7531493)     # 宜蘭 宜蘭

    Keelung = Location(25.1407924, 121.7592534)   # 基隆 中正
    Hsinchu = Location(24.8163726, 120.9703141)   # 新竹 北區
    Miaoli = Location(24.5616772, 120.8190175)    # 苗栗 苗栗
    Changhua = Location(24.0809056, 120.5422565)  # 彰化 彰化
    Nantou = Location(23.9116414, 120.6874199)    # 南投 南投
    Yunlin = Location(23.6971143, 120.5269987)    # 雲林 斗六
    Pingtung = Location(22.6624980, 120.4914295)  # 屏東 屏東
    Taitung = Location(22.7548208, 121.1465131)   # 台東 台東
    Hualien = Location(23.9820651, 121.6067705)   # 花蓮 花蓮
    Penghu = Location(23.5661590, 119.5786920)    # 澎湖 馬公
    Kinmen = Location(24.4328240, 118.3206970)    # 金門 金城
    Lianjiang = Location(26.1529312, 119.9387995) # 連江 南竿
