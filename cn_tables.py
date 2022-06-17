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
    # 表格
    fig = go.Figure(data=[go.Table(header=dict(values=['名次', '学校名称', '综合得分', '星级排名', '办学层次']),
                                   cells=dict(
                                       values=[rank_cn[1:11], college[1:11], point[1:11], rank_star[1:11],
                                               education_layer[1:11]]))
                          ])
    # 保存照片用pio这条
    # pio.write_image(fig, './produced_data/2010年世界各国GDP排名前十名.jpg')
    # 保存html用plotly这条
    plotly.offline.plot(fig, filename="./produced_data/中国大学排名前十名.html", auto_open=False)
    print("中国大学排名前十名.hmtl输出成功")