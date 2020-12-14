#coding: utf-8
import tkinter as tk
from Dijkstra import dijkstra
from Dijkstra import serach_path
from Dijkstra import cal_ticket
from ReadFile import road
from draw_picture import draw_pic_final
import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def gui():
    window = tk.Tk()
    window.title('线路查询中心')
    window.geometry("700x700")

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

    # 一组输入email的界面
    tk.Label(window, text='输入邮箱获取行程: ', font=('Arial', 17)).place(x=8, y=600, anchor='nw')
    email = tk.StringVar()
    get_email = tk.Entry(window, textvariable=email)
    get_email.place(x=165, y=598, anchor='nw')

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
        with open('Route.txt','r+') as f:
            f.seek(0)
            f.truncate()
            for station in final_path:
                f.write(station+'\n')
    def show_graph():
        os.system('python openHTML.py')
    def inital_graph():
        lon_s = []
        lat_s = []
        stations = []
        with open('location.txt', 'r') as f:
            for i in f:
                hang = i.split(' ')
                x = hang[0].split(',')
                stations.append(x)
                y = hang[1].split(',')
                lon_s.append(float(y[0]))
                lat_s.append(float(str(y[1])))
        path = list()
        final_path = list()
        start = start_station.get()
        destination = get_des.get()
        parent_dict, distance_dict = dijkstra(start)
        path.append(destination)
        final_path = serach_path(start, parent_dict, destination, path)
        final_lon_s = []
        final_lat_s = []
        point = []
        for item in final_path:
            i = 0
            for a in stations:
                if a[0] == item:
                    final_lon_s.append(lon_s[i])
                    final_lat_s.append(lat_s[i])
                    point.append(i)
                    i = 0
                    break
                else:
                    i = i + 1
        draw_pic_final(lon_s, lat_s, final_lon_s, final_lat_s, point)
    def get_email():
        email_receiver  = email.get()

        my_sender = '1473992538@qq.com'  # 发件人邮箱账号
        my_pass = 'zhecwfvjdievgice'  # 发件人邮箱密码

        ret = True
        try:
            with open('Route.txt', 'r') as f:
                list = f.readlines()
                final_path = []
                content = '您的地铁路线：'
                for i in list:
                    final_path.append(i[0:len(i) - 1])
            for i in final_path:
                content += i
                if i != final_path[len(final_path)-1]:
                    content += '->'
            msg = MIMEText(content, 'plain', 'utf-8')
            msg['From'] = formataddr(["From冯兄化吉", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["YZW", email_receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "您的地铁路线"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [email_receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
                ret = False

        if ret:
            print("邮件发送成功")
        else:
            print("邮件发送失败")
        tk.Button(window,text = "确认",font = ('Arial',18),command = cal).place(x = 350,y = 105,anchor = 'nw')
    tk.Button(window, text="百度地图显示路线", font=('Arial', 18), ).place(x=300, y=535, anchor='nw')
    tk.Button(window, text="动态查询路线轨迹", font=('Arial', 18), command=inital_graph).place(x=100, y=535, anchor='nw')
    tk.Button(window, text="确认", font=('Arial', 18), command=get_email).place(x=360, y=600,anchor='nw')
    window.mainloop()
