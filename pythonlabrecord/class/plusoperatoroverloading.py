class time:
    def __init__(self,hours,minuts,second):
        self.__hr=hours
        self.__mi=minuts
        self.__sec=second
    def __add__(self, other):
        add_hr=self.__hr+other.__hr
        add_mi=self.__mi+other.__mi
        add_se=self.__sec+other.__sec
        if add_se>60:
            add_mi=add_mi+add_se//60
            add_se=add_se%60
        if add_mi>60:
            add_hr=add_hr+add_mi//60
            add_mi=add_mi%60
        print("total hr={},total min{},total sec{}".format(add_hr,add_mi,add_se))



hr1=time(3,28,45)
hr2=time(5,56,57)
hr1+hr2