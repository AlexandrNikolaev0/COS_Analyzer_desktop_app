import time
import datetime
from analyzerTask import analyzerTask

class sampleTask(analyzerTask):
    """Класс задачи экспермента"""
    def __init__(self,groupName,pos, expType, sampleName, value, valueRazm, razmConcentr, operator, comment,
                 autosamplerEnable=str(False), sampleNum=str(1), repeatSampleNum=str(1), posTray=str("Tray 1"), posTube=str(1), razbav=str(1), plotn=str(1)):
        super().__init__(groupName,pos)
        self.expType = expType
        self.sampleName = sampleName
        self.value = value
        self.valueRazm = valueRazm
        self.razmConcentr = razmConcentr
        self.operator = operator
        self.comment = comment
        self.autosamplerEnable = autosamplerEnable
        self.sampleNum = sampleNum
        self.repeatSampleNum = repeatSampleNum
        self.posTray = posTray
        self.posTube = posTube
        self.razbav = razbav
        self.plotn = plotn
if __name__ == "__main__":
    task1 = sampleTask("sampleN",2,"standart", "Sample 1", 20, "мкл", "ммоль", "оператор 1", "коммент 1")
    print(task1.expType)
    print(task1.sampleName)
    print(task1.value)
    print(task1.valueRazm)
    print(task1.razmConcentr)
    print(task1.operator)
    print(task1.comment)
    print(task1.autosamplerEnable)
    print(task1.sampleNum)
    print(task1.repeatSampleNum)
    print(task1.posTray)
    print(task1.posTube)
    print(task1.razbav)
    print(task1.plotn)