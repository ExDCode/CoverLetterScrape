# from asyncore import read
from bs4 import BeautifulSoup
import pandas as pd

htmlFile = open("index.html", 'r')

index = htmlFile.read()

soup = BeautifulSoup(index, 'lxml')

Datalist = []
dataDict = {}

for index, tr in enumerate(soup.findAll('tr')):
    data = tr.find_all('td')
    val1 = data[0].find('strong').text.rstrip().lstrip()
    val2 = data[1].text.rstrip().lstrip()
    dataDict[val1] = val2
    # Datalist.append(dataDict)
    # print(f'Index value is {index} and {val1}')
    # print(val1, val2)
print(dataDict)
finalDataFrame = pd.DataFrame.from_dict(dataDict)
display(finalDataFrame)
# print(soup.findAll(id))