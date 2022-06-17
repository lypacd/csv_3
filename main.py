import csv
from plotly.graph_objs import *
import plotly.graph_objects as go
import plotly as py

import plotly.offline

file_name1='./data_3/世界大学排名.csv'
file_name2='./data_3/中国大学排名500强.csv'

#散点图/折线图 大学在世界分布柱状图，2019和2020排名对比，柱状
def f1():
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


        print("打印")

        college1=list(reversed(college[2:12]))

        point1=list(reversed(point[2:12]))
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
        #可改变一下点的形状
        print("输出世界各大学得分.html成功")

        #2019和2020
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

    #绘制大学和地方分布的关系
        place_dict=list(zip(college[2:-1],country_region[2:-1]))
        country_region1=list(set(country_region))
        print("打印")
        place_index=dict()
        for i in range(len(country_region1)):
            place_index[country_region1[i]]=i
        #每个地点所对应的大学数
        num_colleges=[]
        for j in range(len(country_region1)):
            num_colleges.append(0)
        for item in place_dict:
            index_temp=place_index[item[1]]
            num_colleges[index_temp]+=1
        trace3 = go.Bar(
            x=country_region1,
            y=num_colleges,
            name="世界各地区大学分布"
        )

        fig = go.Figure(data=[trace3])
        pyplt = py.offline.plot
        pyplt(fig, filename='./produced_data/世界各地区大学分布.html', auto_open=False)
        # 可改变一下点的形状
        print("输出世界各地区大学分布.html成功")


#散点图，中国大学排名，表格
def f2():
    with open(file_name2, 'r',encoding='utf8') as f:
        csv_reader = csv.reader(f)
        rank_cn= []
        college=[]
        point=[]
        rank_star=[]
        education_layer=[]
        i=-1
        for line in csv_reader:
            # print(line)
            rank_cn.append(line[0])
            college.append(line[1])
            point.append(line[2])
            rank_star.append(line[3])
            education_layer.append(line[4])
        # print("打印")
        #散点图
        trace4= Scatter(
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
        #可改变一下点的形状
        print("输出中国各大学得分.html成功")

        #表格
        fig = go.Figure(data=[go.Table(header=dict(values=['名次', '学校名称', '综合得分', '星级排名','办学层次']),
                                       cells=dict(
                                           values=[rank_cn[1:11],college[1:11], point[1:11], rank_star[1:11],education_layer[1:11]]))
                              ])
        # 保存照片用pio这条
        # pio.write_image(fig, './produced_data/2010年世界各国GDP排名前十名.jpg')
        # 保存html用plotly这条
        plotly.offline.plot(fig, filename="./produced_data/中国大学排名前十名.html", auto_open=False)
        print("中国大学排名前十名.hmtl输出成功")


# f1()
f2()
