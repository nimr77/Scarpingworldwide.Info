import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/country/morocco/"
resp = requests.get(url)
data = resp.text
soup = BeautifulSoup(data, features="html.parser")
rects = soup.find_all('script')

# 'Highcharts.chart'
yx_points = []
for rect in rects:
    if rect.has_attr("type") and rect['type'] == "text/javascript":
        val = str(rect)
        if("Highcharts.chart" in val):

            try:           
                title = val.split("title:")[1].split('text:')[1].split('\n')[0]
                xAxis = val.split("xAxis:")[1].split("categories:")[1].split('\n')[0]
                data = val.split('series:')[1].split('data:')[1].split('\n')[0]
            
            except:
                title = val.split("title:")[1].split('text:')[1].split('\n')[0]
                xAxis = val.split("xAxis:")[1].split("categories:")[1].split('\n')[0]
                data = val.split('series:')[2].split('data:')[1].split('\n')[0]
            print({
                'title':title,
                'xAxis':xAxis,
                'data':data
                })