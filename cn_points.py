import csv
from plotly.graph_objs import *
import plotly.graph_objects as go
import plotly as py

import plotly.offline

file_name1='./data_3/世界大学排名.csv'
file_name2='./data_3/中国大学排名500强.csv'

with open(file_name2, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    rank_cn = []
    college = []
    point = []
    rank_star = []
    education_layer = []
    i = -1
    for line in csv_reader:
        # print(line)
        rank_cn.append(line[0])
        college.append(line[1])
        point.append(line[2])
        rank_star.append(line[3])
        education_layer.append(line[4])
    # print("打印")
    # 散点图
    trace4 = Scatter(
        x=college,
        y=point,
        mode="markers",
        name='中国各大学得分',
        marker={
            "size": 16,  # 点的大小
            "color": "rgba(102, 198, 147, 0.7)",  # 点的颜色
        }
    )

    # plotly.offline.plot(trace0)
    fig = go.Figure(data=trace4)
    pyplt = py.offline.plot
    pyplt(fig, filename='./produced_data/中国各大学得分.html', auto_open=False)
    # 可改变一下点的形状
    print("输出中国各大学得分.html成功")