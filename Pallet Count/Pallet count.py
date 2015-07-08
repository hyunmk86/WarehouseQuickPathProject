
class pallets(object):

    def __init__(self,list):
        self.list = list


    def add(self,quantityDate):
        self.list.extend(quantityDate)
        return self.list

    def subtract(self):
        self.list.pop(0)
        return self.list




