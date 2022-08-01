import requests
import pandas as pd
import io
import zipfile
import xml.etree.ElementTree as et
import json

crtfc_key = '3c9b2c6ae4cc077d7c4162e2c143a80fe2143ca4'

def get_corpcode(crtfc_key):
    params = {'crtfc_key' : crtfc_key}
    items = ["corp_code", "corp_name", "stock_code", "modify_date"]
    item_names = ["고유번호", "회사명", "종목코드", "수정일"]
    url = "https://opendart.fss.or.kr/api/corpCode.xml"
    res = requests.get(url, params = params)
    zfile = zipfile.ZipFile(io.BytesIO(res.content))
    fin = zfile.open(zfile.namelist()[0])
    root = et.fromstring(fin.read().decode('utf-8'))
    data = []
    for child in root:
        if len(child.find('stock_code').text.strip())>1:
            data.append([])
            for item in items:
                data[-1].append(child.find(item).text)
    df = pd.DataFrame(data, columns=item_names)
    return df

if __name__ == "__main__":
    stock_comp = get_corpcode(crtfc_key)
    print(stock_comp)