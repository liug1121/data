class Datas:
    ID_A0M05 = 'A0M05'
    NAME_A0M05 = '各级各类学校数'
    
    def __init__(self, dataType, dataName):
        self.dataType = dataType
        self.dataName = dataName

    def setDatas(self, datas):
        self.datas = datas

class Index:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Page:
    def __init__(self, startPage = 0, size = 10, totalPage = 0):
        self.__startPage = startPage
        self.__size = size
        self.__totalPage = totalPage
    def getSize(self):
        return self.__size
    def getStartPage(self):
        return self.__startPage



