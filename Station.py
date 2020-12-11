class station():
    def __init__(self,name,line_info,next_dis = 0.00):
        self.name = name
        self.next_dis = next_dis
        self.line_info = line_info
    #获取站名
    def get_name(self):
        return self.name
    #获取本站到下一站到距离
    def get_dis(self):
        return self.next_dis
    #获取本站所在到地铁线路
    def get_line_info(self):
        return self.line_info
