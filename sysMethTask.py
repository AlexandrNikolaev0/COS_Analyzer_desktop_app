import time
import datetime
from analyzerTask import analyzerTask

class sysMethTask(analyzerTask):
    """Класс задачи режима"""
    def __init__(self,mode,pos, innerTemp, outerTemp, shakerTemp, injectionSpeed, transpLineTemp):
        super().__init__(mode,pos)
        self.innerTemp = innerTemp
        self.outerTemp = outerTemp
        self.shakerTemp = shakerTemp
        self.injectionSpeed = injectionSpeed
        self.transpLineTemp = transpLineTemp
if __name__ == "__main__":
    task1 = sysMethTask("startup",2,300, 400, 20, 5,200)
    print(task1.creationDate)
    print(task1.description)
    print(task1.shakerTemp)