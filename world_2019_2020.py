import csv
from plotly.graph_objs import *
import plotly.graph_objects as go
import plotly as py

import plotly.offline

file_name1='./data_3/世界大学排名.csv'
file_name2='./data_3/中国大学排名500强.csv'

#散点图/折线图 大学在世界分布柱状图，2019和2020排名对比，柱状

with open(file_name1, 'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    rank2020= []
    rank2019=[]
    country_region = []
    college=[]
    point=[]
    #定义地方和学校的字典
    place_dict=[]
    i=-1
    for line in csv_reader:
        rank2020.append(line[0].strip('\n'))
        rank2019.append(line[1].strip('\n'))
        country_region.append(line[2].strip('\n'))
        college.append(line[3].strip('\n'))
        point.append(line[4].strip('\n'))
trace1 = go.Bar(
    x=country_region[1:-1],
    y=rank2019[1:-1],
    name="2019年世界大学排名"
)

trace2 = go.Bar(
    x=country_region[1:-1],
    y=rank2020[1:-1],
    name="2020年世界大学排名"
)

fig = go.Figure(data=[trace1, trace2])
pyplt = py.offline.plot
pyplt(fig, filename='./produced_data/2019和2020年世界大学排名.html', auto_open=False)
print("2019和2020年世界大学排名.hmtl输出成功")