import datetime
staffdict = {
    "Gbenga":"P8107",
    "Chukwudi":"S5401",
    "Chinwe":"P1088",
}


class timestaff:
    name = input("Name:  ")
    hr = eval(input("HH"))
    min = eval(input("MM"))
    cut_hr=eval("7")
    cut_min=eval("30")
    cut_timein = datetime.time(cut_hr,cut_min)
    timein = datetime.time(hr,min)

    def __init__(self,name, timein,cut_timein):
        self.__name = name
        self.__timein = timein
        self.__cut_timein = cut_timein

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_timein(self, timein):
        self.timein = timein
    def get_timein(self):
        return self.timein

    def get_detail(self):
        if self.name in staffdict.keys() and self.timein <= self.cut_timein:
            return "{} with staffid {}, you came at {}. That's early.".format(self.name,staffdict[self.name],self.timein)
        elif self.name not in staffdict.keys():
            return "You don't work here."
        else:
            return "{}, you can't be doing this every time. You came late at {} today.".format(self.name,self.timein)

print("Cut off time: 07:30:00")
staff1 = timestaff("name","timein","cut_timein")
staff1.get_detail()
print(staff1.get_detail())
