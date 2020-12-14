from Station import station
import linecache
from collections import defaultdict
file_path = r'BaseSubWayInfo.txt'
file = open("BaseSubWayInfo.txt")
linenums = len(file.readlines())
road=defaultdict(list)
linenum = linecache.getline(file_path,1)
#以下是吧txt里面的所有栈都读到一个list里面了，list的每一个元素是一个station类
for i in range(2,int(linenum)+2):
    line_info = linecache.getline(file_path,i).split("，")[1]
    j = linecache.getline(file_path,i).split("，")[2]
    for k in range(3,int(j)*2+1,2):
        temp_name = linecache.getline(file_path,i).split("，")[k]
        k = k+1
        temp_dis = (linecache.getline(file_path, i).split("，")[k])
        temp = station(temp_name,line_info,temp_dis)
        road[line_info].append(temp)
    else:
        temp_name = linecache.getline(file_path,i).split("，")[int(j)*2+1]
        temp_name = temp_name[0:len(temp_name)-1]
        temp = station(temp_name,line_info)
        road[line_info].append(temp)
#构建临接表 road_graph_list 就是一个临接表
road_graph = defaultdict(set)
road_graph_prev = defaultdict(set)
road_graph_next = defaultdict(set)
manage_station = {}
temp_dict = {}
for i in road:
    for j, k in enumerate(road[i]):
        if j == 0:
            #temp = road_graph[k.get_name()].add(road[i][j + 1])
            temp = road[i][j + 1]
            # road_graph[k.get_name()].add(temp)
            # road_graph_next[k.get_name()].add(temp)
            temp_dict[temp.get_name()] = k.get_dis()#后面那站到该站到距离
            if k.get_name in manage_station:
                manage_station[k.get_name()].update(temp_dict)
            else:
                manage_station[k.get_name()] = temp_dict
            temp_dict ={}
        elif j == len(road[i]) - 1:
            temp_name = road[i][j-1].get_name()
            temp = road[i][j - 1]
            # road_graph[temp_name].add(temp)
            # road_graph_prev[temp_name].add(temp)
            temp_dict[temp.get_name()] = temp.get_dis()#上一站到现在这站到距离
            if k.get_name in manage_station:
                manage_station[k.get_name()].update(temp_dict)
            else:
                manage_station[k.get_name()] = temp_dict
            temp_dict ={}
            #print(road_graph[k.get_name()])
        else:
            # road_graph[temp_name].add(road[i][j + 1])
            # road_graph[temp_name].add(road[i][j - 1])
            # road_graph_prev[temp_name].add(road[i][j - 1])
            # road_graph_next[temp_name].add(road[i][j + 1])
            temp = road[i][j-1]
            temp_dict[temp.get_name()] = temp.get_dis()
            temp = road[i][j+1]
            temp_dict[temp.get_name()] = k.get_dis()
            if k.get_name() in manage_station:
                manage_station[k.get_name()].update(temp_dict)
            else:
                manage_station[k.get_name()] = temp_dict
            temp_dict ={}




