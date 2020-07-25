import json
t=[]
with open('json.json', 'r') as f:
    data = json.load(f)




class Calculate:
    def __init__(self, list):
        self.list = list
        self.total = 0

    def cal_frame(self):
        if self.list[0] == 'Aluminum':
            self.total = 1000
        elif self.list[0] == 'Iron':
            self.total = 800
        elif self.list[0] == 'Steel':
            self.total = 800
        return self.total

    def cal_handbreak(self):
        if self.list[1] == 'type1':
            self.total = 1000
        elif self.list[1] == 'type2':
            self.total = 800
        elif self.list[1] == 'type3':
            self.total = 800
        return self.total
    def cal_tyres(self):
        if self.list[2] == 'tube':
            self.total = 1000
        elif self.list[2] == 'tubless':
            self.total = 2000
        elif self.list[2] == 'light':
            self.total = 8000
        return self.total

    def cal_chanAsam(self):
        if self.list[3] == 'type1':
            self.total = 1000
        elif self.list[3] == 'type2':
            self.total = 800
        elif self.list[3] == 'type3':
            self.total = 800
        return self.total


def total():
    for i in range(5):
        l = list(data[i].values())
        obj = Calculate(l)
        sum = obj.cal_frame() + obj.cal_handbreak() + obj.cal_chanAsam() + obj.cal_tyres()
        print("Calculated cost of cycle",sum)

total()
