#coding: utf-8
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
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
import time
def draw_pic_final(lon_s,lat_s,final_lon_s,final_lat_s,point):
    window_2 = tk.Tk()
    window_2.title("路线轨迹")
    fig = plt.figure(figsize=(8, 8))
    a = fig.add_subplot(111)
    window_2.geometry("800x800")
    a.scatter(lon_s, lat_s, label=None, c='k', alpha=0.75, s=1)
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
    a.scatter(lon_s, lat_s, label=None, c='k', alpha=0.75, s=1)
    a.plot(line_1_s, line_1_d, '-', color='r', linewidth=2, alpha=0.7, )
    a.plot(line_2_s, line_2_d, '-', color='dodgerblue', linewidth=2, alpha=0.7, )
    a.plot(line_4_s, line_4_d, '-', color='darkcyan', linewidth=2, alpha=0.7, )
    a.plot(line_5_s, line_5_d, '-', color='violet', linewidth=2, alpha=0.7, )
    a.plot(line_6_s, line_6_d, '-', color='chocolate', linewidth=2, alpha=0.7, )
    a.plot(line_7_s, line_7_d, '-', color='sandybrown', linewidth=2, alpha=0.7, )
    a.plot(line_8_s, line_8_d, '-', color='chartreuse', linewidth=2, alpha=0.7, )
    a.plot(line_9_s, line_9_d, '-', color='yellowgreen', linewidth=2, alpha=0.7, )
    a.plot(line_10_s, line_10_d, '-', color='deepskyblue', linewidth=2, alpha=0.7, )
    a.plot(line_13_s, line_13_d, '-', color='yellow', linewidth=2, alpha=0.7, )
    a.plot(line_14_s, line_14_d, '-', color='pink', linewidth=2, alpha=0.7, )
    a.plot(line_15_s, line_15_d, '-', color='orchid', linewidth=2, alpha=0.7, )
    a.plot(line_16_s, line_16_d, '-', color='green', linewidth=2, alpha=0.7, )
    a.plot(line_8t_s, line_8t_d, '-', color='darkred', linewidth=2, alpha=0.7, )
    a.plot(line_cp_s, line_cp_d, '-', color='fuchsia', linewidth=2, alpha=0.7, )
    a.plot(line_yz_s, line_yz_d, '-', color='hotpink', linewidth=2, alpha=0.7, )
    a.plot(line_fs_s, line_fs_d, '-', color='darkorange', linewidth=2, alpha=0.7, )
    a.plot(line_ap_s, line_ap_d, '-', color='grey', linewidth=2, alpha=0.7, )
    a.plot(line_dx_s, line_dx_d, '-', color='aquamarine', linewidth=2, alpha=0.7, )
    a.plot(line_S1_s, line_S1_d, '-', color='darkgoldenrod', linewidth=2, alpha=0.7, )
    flag = 0
    point.reverse()
    for i in point:
        a.scatter(lon_s[i], lat_s[i], label=None, c='r', marker='*')
        plt.ion()
        plt.pause(1)
        flag+=1
        if flag == len(point):
            a.scatter(lon_s[i], lat_s[i], label=None, c='r', marker='*')
            plt.ion()
            plt.close()
    canvas = FigureCanvasTkAgg(fig, master=window_2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, window_2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    def back():
        window_2.destroy()
    button_back = tk.Button(master=window_2, text="Back", font=('Comic Sans MS', 30), command= back)
    button_back.place(x = 250,y = 750)
    def quit():
        window_2.quit()
        window_2.destroy()
    button_quit = tk.Button(master=window_2, text="Quit", font=('Comic Sans MS', 30), command=quit)
    button_quit.place(x = 430,y = 750)
# def draw_pic_final(lon_s,lat_s,final_lon_s,final_lat_s):
#     fig = plt.figure(figsize=(8, 8))
#     plt.scatter(lon_s, lat_s, label=None, c='k', alpha=1, s=1)
#     # 线路1
#     line_1_s = lon_s[0:23]
#     line_1_d = lat_s[0:23]
#     # 线路2
#     line_2_s = lon_s[24:43]
#     line_2_d = lat_s[24:43]
#     # 线路4
#     line_4_s = lon_s[44:67]
#     line_4_d = lat_s[44:67]
#     # 线路5
#     line_5_s = lon_s[68:90]
#     line_5_d = lat_s[68:90]
#     # 线路6
#     line_6_s = lon_s[97:123]
#     line_6_d = lat_s[97:123]
#     # 线路7
#     line_7_s = lon_s[124:144]
#     line_7_d = lat_s[124:144]
#     # 线路8
#     line_8_s = lon_s[145:162]
#     line_8_d = lat_s[145:162]
#     # 线路9
#     line_9_s = lon_s[177:189]
#     line_9_d = lat_s[177:189]
#     # 线路10
#     line_10_s = lon_s[190:236]
#     line_10_d = lat_s[190:236]
#     # 线路13
#     line_13_s = lon_s[237:252]
#     line_13_d = lat_s[237:252]
#     # 线路14
#     line_14_s = lon_s[253:279]
#     line_14_d = lat_s[253:279]
#     # 线路15
#     line_15_s = lon_s[280:299]
#     line_15_d = lat_s[280:299]
#     # 线路16
#     line_16_s = lon_s[300:309]
#     line_16_d = lat_s[300:309]
#     # 线路八通线
#     line_8t_s = lon_s[310:322]
#     line_8t_d = lat_s[310:322]
#     # 线路cp
#     line_cp_s = lon_s[323:334]
#     line_cp_d = lat_s[323:334]
#     # 线路yz
#     line_yz_s = lon_s[335:348]
#     line_yz_d = lat_s[335:348]
#     # 线路fs
#     line_fs_s = lon_s[349:359]
#     line_fs_d = lat_s[349:359]
#     # 线路airplane
#     line_ap_s = lon_s[360:363]
#     line_ap_d = lat_s[360:363]
#     # 线路dx
#     line_dx_s = lon_s[364:375]
#     line_dx_d = lat_s[364:375]
#     # 线路S1
#     line_S1_s = lon_s[376:382]
#     line_S1_d = lat_s[376:382]
#     plt.scatter(lon_s, lat_s, label=None, c='k', alpha=0.75, s=1)
#     plt.plot(line_1_s, line_1_d, '-', color='r', linewidth=2, alpha=0.7, )
#     plt.plot(line_2_s, line_2_d, '-', color='dodgerblue', linewidth=2, alpha=0.7, )
#     plt.plot(line_4_s, line_4_d, '-', color='darkcyan', linewidth=2, alpha=0.7, )
#     plt.plot(line_5_s, line_5_d, '-', color='violet', linewidth=2, alpha=0.7, )
#     plt.plot(line_6_s, line_6_d, '-', color='chocolate', linewidth=2, alpha=0.7, )
#     plt.plot(line_7_s, line_7_d, '-', color='sandybrown', linewidth=2, alpha=0.7, )
#     plt.plot(line_8_s, line_8_d, '-', color='chartreuse', linewidth=2, alpha=0.7, )
#     plt.plot(line_9_s, line_9_d, '-', color='yellowgreen', linewidth=2, alpha=0.7, )
#     plt.plot(line_10_s, line_10_d, '-', color='deepskyblue', linewidth=2, alpha=0.7, )
#     plt.plot(line_13_s, line_13_d, '-', color='yellow', linewidth=2, alpha=0.7, )
#     plt.plot(line_14_s, line_14_d, '-', color='pink', linewidth=2, alpha=0.7, )
#     plt.plot(line_15_s, line_15_d, '-', color='orchid', linewidth=2, alpha=0.7, )
#     plt.plot(line_16_s, line_16_d, '-', color='green', linewidth=2, alpha=0.7, )
#     plt.plot(line_8t_s, line_8t_d, '-', color='darkred', linewidth=2, alpha=0.7, )
#     plt.plot(line_cp_s, line_cp_d, '-', color='fuchsia', linewidth=2, alpha=0.7, )
#     plt.plot(line_yz_s, line_yz_d, '-', color='hotpink', linewidth=2, alpha=0.7, )
#     plt.plot(line_fs_s, line_fs_d, '-', color='darkorange', linewidth=2, alpha=0.7, )
#     plt.plot(line_ap_s, line_ap_d, '-', color='grey', linewidth=2, alpha=0.7, )
#     plt.plot(line_dx_s, line_dx_d, '-', color='aquamarine', linewidth=2, alpha=0.7, )
#     plt.plot(line_S1_s, line_S1_d, '-', color='darkgoldenrod', linewidth=2, alpha=0.7, )
#     plt.scatter(final_lon_s, final_lat_s, label=None, c='r', marker='*')
#     plt.show()
