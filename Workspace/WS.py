list = ["WS1", ['kali', '1', '1'], ['ubuntu', '1', '2'], ['unix', '1', '3']]
addlist = ["centos", '1', '4']
class WorkspaceManager():
    def __init__(self, id, list):
        self.worklist = list
        self.id = id
        #self.worklist.append(self.id)

    # 전체 WorkSpace리스트 보여주기
    def showList(self):
        print(self.worklist)

    # WorkSpace리스트에 구성요소 추가
    def addComp(self, addlist):
        self.worklist.append(addlist)

    # WorSpace리스트에 구성요소 삭제
    def selectDelete(self, comp):
        #print(len(self.worklist))

        for count in range(1, len(self.worklist)):
            if comp == self.worklist[count][0]:
                del self.worklist[count]
                break

    # WorkSpace리스트 전체 삭제
    def allDelete(self):
        self.worklist = []

if __name__=="__main__":
    cmc = WorkspaceManager("hi", list)
    cmc.selectDelete("kali")
    cmc.showList()
    cmc.selectDelete('unix')
    cmc.showList()
    cmc.selectDelete('hi')
    cmc.showList()
    cmc.allDelete()
    cmc.showList()
