import csv
from plotly.graph_objs import *
import plotly.graph_objects as go
import plotly as py

import plotly.offline

file_name1='./data_3/世界大学排名.csv'
file_name2='./data_3/中国大学排名500强.csv'

with open(file_name1, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    rank2020 = []
    rank2019 = []
    country_region = []
    college = []
    point = []
    # 定义地方和学校的字典
    place_dict = []
    i = -1
    for line in csv_reader:
        rank2020.append(line[0].strip('\n'))
        rank2019.append(line[1].strip('\n'))
        country_region.append(line[2].strip('\n'))
        college.append(line[3].strip('\n'))
        point.append(line[4].strip('\n'))

    print("打印")

    college1 = list(reversed(college[2:12]))

    point1 = list(reversed(point[2:12]))
    trace0 = Scatter(
        x=college1,
        y=point1,
        mode="markers",
        name='世界排名前十大学得分'
    )

    # plotly.offline.plot(trace0)
    fig = go.Figure(data=trace0)
    pyplt = py.offline.plot
    pyplt(fig, filename='./produced_data/世界各大学得分.html', auto_open=False)
    # 可改变一下点的形状
    print("输出世界各大学得分.html成功")