import time
import datetime
class analyzerTask:
    """Класс задачи для диспетчера задач"""

    def __init__(self,description,pos):
        self.position=pos
        self.status = "Ожидание"
        self.description = description
        self.creationDate = datetime.datetime.now()
        self.startDate =""
        self.stopDate=""
        self.totalTime=""

if __name__ == "__main__":
    task1 = analyzerTask("testTask",2)
    print(task1.creationDate)