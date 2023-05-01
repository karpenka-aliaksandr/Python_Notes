from datetime import datetime
class Note:
    def __init__(self,id:int,date_time:datetime,header:str,body:str):
        self.id = id
        self.date_time = date_time
        self.header = header
        self.body = body
    
    def __str__(self) -> str:
        return str(self.id) + ' ' + str(self.date_time.date()) + ' ' + self.header + ' ' + self.body