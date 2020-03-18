def getDic() :
    f = open('Osterspaziergang.txt','r')
    dic = {}
    list = []
    length = 0
    for line in f:
        for word in line.split():
            list.append(word)
            length +=1
    dic.update({length : list})
    return dic

def printDic(mydic) :
    for i in mydic :
        print(i,mydic[i])

printDic(getDic())