#coding: utf-8
import tkinter as tk
from Dijkstra import dijkstra
from Dijkstra import init_distance
from ReadFile import manage_station
from Dijkstra import serach_path
from Dijkstra import cal_ticket
from PIL import ImageTk, Image
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ReadFile import road
def gui():
    window = tk.Tk()
    window.title('线路查询中心')
    window.geometry("600x600")
    # # # 画布
    # canvas = tk.Canvas(window,height = 600,width = 400)
    # imgpath = 'pic.gif'
    # img = Image.open(imgpath)
    # photo = ImageTk.PhotoImage(img)
    # canvas.create_image(0,0,anchor = 'nw',image = photo)
    # canvas.place(x= 0,y = 0,anchor = 'nw')


    l = tk.Label(window,text='欢迎前来查询地铁线路',bg = 'white',font = ('Arial',18),width = 70,height = 5)
    l.pack()


    # 显示具体经过的站
    tk.Label(window, text='本次的具体行程为:', font=('Arial', 17)).place(x=8, y=179, anchor='nw')
    route = tk.Text(window, height=3)
    route.place(x=8, y=210, anchor='nw')

    # 显示距离
    how_long = tk.StringVar()
    tk.Label(window, text='本次行程的距离为: ', font=('Arial', 17)).place(x=8, y=130, anchor='nw')
    tk.Entry(window, textvariable=how_long).place(x=153, y=130, anchor='nw')


    # 显示票价
    ticket_price = tk.StringVar()
    tk.Label(window, text='本次行程的票价: ', font=('Arial', 17)).place(x=8, y=155, anchor='nw')
    tk.Entry(window, textvariable=ticket_price).place(x=153, y=155, anchor='nw')

    #一组输入起始站点的界面
    tk.Label(window, text='请输入您的起始站: ',font = ('Arial',17)).place(x=8, y=83,anchor = 'nw')
    start_station = tk.StringVar()
    get_start = tk.Entry(window,textvariable=start_station)
    get_start.place(x = 153,y = 81,anchor = 'nw')
    start = start_station.get()


    #一组输入终点的界面
    tk.Label(window, text='请输入您的终点站: ',font = ('Arial',17)).place(x=8, y=107,anchor = 'nw')
    destination_station = tk.StringVar()
    get_des = tk.Entry(window,textvariable=destination_station)
    get_des.place(x = 153,y = 105,anchor = 'nw')

    #票价列表
    #price_list = tk.StringVar()
    tk.Label(window,text = '起始站到各个站的票价:',font =  ('Arial',17)).place(x = 8,y = 265,anchor = 'nw')
    ticket_price_list = tk.Listbox(window,width = 60)
    ticket_price_list.place(x=13,y = 290,anchor = 'nw')
    #查询线路按钮
    tk.Label(window,text = '点击下面按钮查询行程路线图:',font = ('Arial',17)).place(x = 8,y = 480,anchor = 'nw')
    def cal():
        path = list()
        final_path = list()
        start = start_station.get()
        #print(type(start))
        destination = get_des.get()
        #print(type(destination))
        parent_dict,distance_dict = dijkstra(start)
        path.append(destination)
        flag = True
        #防止出现错误
        try:
            final_path = serach_path(start,parent_dict,destination,path)
        except KeyError:
            start, destination = destination, start
            parent_dict, distance_dict = dijkstra(start)
            final_path.clear()
            final_path = serach_path(start, parent_dict, destination, path)
            final_path[len(final_path)-1] = destination
            price_list = []
            for i in road:
                for k in road[i]:
                    price_list.append(k.get_name() + " " + str(cal_ticket(distance_dict[k.get_name()])) + "元")
            for item in price_list:
                ticket_price_list.insert('end', item)
            dis = distance_dict[destination]
            price = cal_ticket(dis)
            ticket_price.set(str(price) + '元')
            how_long.set(str(dis) + '公里')
            if str(route).strip() == '':
                route.insert('insert', final_path)
            else:
                route.delete('1.0', tk.END)
                route.insert('insert', final_path)
            flag = False

        if flag == True:
            final_path.reverse()
            price_list = []
            for i in road:
                for k in road[i]:
                    price_list.append(k.get_name()+" "+str(cal_ticket(distance_dict[k.get_name()]))+"元")
            for item in price_list:
                ticket_price_list.insert('end',item)
            dis = distance_dict[destination]
            price = cal_ticket(dis)
            ticket_price.set(str(price)+'元')
            how_long.set(str(dis)+'公里')
            if str(route).strip()=='':
                route.insert('insert',final_path)
            else:
                route.delete('1.0',tk.END)
                route.insert('insert', final_path)

    def initial_graph():
        fig = plt.figure(figsize=(7, 7))
        lon_s = []
        lat_s = []
        with open('location.txt', 'r') as f:
            for i in f:
                hang = i.split(' ')
                x = hang[0].split(',')
                y = hang[1].split(',')
                lon_s.append(float(y[0]))
                lat_s.append(float(str(y[1])))
        # 线路1
        line_1_s = lon_s[0:23]
        line_1_d = lat_s[0:23]
        # 线路2
        line_2_s = lon_s[24:43]
        line_2_d = lat_s[24:43]
        # 线路4
        line_4_s = lon_s[44:67]
        line_4_d = lat_s[44:67]
        # 线路5
        line_5_s = lon_s[68:90]
        line_5_d = lat_s[68:90]
        # 线路6
        line_6_s = lon_s[97:123]
        line_6_d = lat_s[97:123]
        # 线路7
        line_7_s = lon_s[124:144]
        line_7_d = lat_s[124:144]
        # 线路8
        line_8_s = lon_s[145:162]
        line_8_d = lat_s[145:162]
        # 线路9
        line_9_s = lon_s[177:189]
        line_9_d = lat_s[177:189]
        # 线路10
        line_10_s = lon_s[190:236]
        line_10_d = lat_s[190:236]
        # 线路13
        line_13_s = lon_s[237:252]
        line_13_d = lat_s[237:252]
        # 线路14
        line_14_s = lon_s[253:279]
        line_14_d = lat_s[253:279]
        # 线路15
        line_15_s = lon_s[280:299]
        line_15_d = lat_s[280:299]
        # 线路16
        line_16_s = lon_s[300:309]
        line_16_d = lat_s[300:309]
        # 线路八通线
        line_8t_s = lon_s[310:322]
        line_8t_d = lat_s[310:322]
        # 线路cp
        line_cp_s = lon_s[323:334]
        line_cp_d = lat_s[323:334]
        # 线路yz
        line_yz_s = lon_s[335:348]
        line_yz_d = lat_s[335:348]
        # 线路fs
        line_fs_s = lon_s[349:359]
        line_fs_d = lat_s[349:359]
        # 线路airplane
        line_ap_s = lon_s[360:363]
        line_ap_d = lat_s[360:363]
        # 线路dx
        line_dx_s = lon_s[364:375]
        line_dx_d = lat_s[364:375]
        # 线路S1
        line_S1_s = lon_s[376:382]
        line_S1_d = lat_s[376:382]
        plt.scatter(lon_s, lat_s, label=None, c='k', alpha=0.75, s=1)
        plt.plot(line_1_s, line_1_d, '-', color='r', linewidth=2, alpha=0.7, )
        plt.plot(line_2_s, line_2_d, '-', color='dodgerblue', linewidth=2, alpha=0.7, )
        plt.plot(line_4_s, line_4_d, '-', color='darkcyan', linewidth=2, alpha=0.7, )
        plt.plot(line_5_s, line_5_d, '-', color='violet', linewidth=2, alpha=0.7, )
        plt.plot(line_6_s, line_6_d, '-', color='chocolate', linewidth=2, alpha=0.7, )
        plt.plot(line_7_s, line_7_d, '-', color='sandybrown', linewidth=2, alpha=0.7, )
        plt.plot(line_8_s, line_8_d, '-', color='chartreuse', linewidth=2, alpha=0.7, )
        plt.plot(line_9_s, line_9_d, '-', color='yellowgreen', linewidth=2, alpha=0.7, )
        plt.plot(line_10_s, line_10_d, '-', color='deepskyblue', linewidth=2, alpha=0.7, )
        plt.plot(line_13_s, line_13_d, '-', color='yellow', linewidth=2, alpha=0.7, )
        plt.plot(line_14_s, line_14_d, '-', color='pink', linewidth=2, alpha=0.7, )
        plt.plot(line_15_s, line_15_d, '-', color='orchid', linewidth=2, alpha=0.7, )
        plt.plot(line_16_s, line_16_d, '-', color='green', linewidth=2, alpha=0.7, )
        plt.plot(line_8t_s, line_8t_d, '-', color='darkred', linewidth=2, alpha=0.7, )
        plt.plot(line_cp_s, line_cp_d, '-', color='fuchsia', linewidth=2, alpha=0.7, )
        plt.plot(line_yz_s, line_yz_d, '-', color='hotpink', linewidth=2, alpha=0.7, )
        plt.plot(line_fs_s, line_fs_d, '-', color='darkorange', linewidth=2, alpha=0.7, )
        plt.plot(line_ap_s, line_ap_d, '-', color='grey', linewidth=2, alpha=0.7, )
        plt.plot(line_dx_s, line_dx_d, '-', color='aquamarine', linewidth=2, alpha=0.7, )
        plt.plot(line_S1_s, line_S1_d, '-', color='darkgoldenrod', linewidth=2, alpha=0.7, )
        plt.show()

    confirm_2 = tk.Button(window,text = "确认",font = ('Arial',18),command = cal).place(x = 350,y = 105,anchor = 'nw')
    query = tk.Button(window, text="查询路线", font=('Arial', 18), command=initial_graph).place(x=220, y=515, anchor='nw')
    window.mainloop()