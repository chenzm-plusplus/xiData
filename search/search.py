
def searchintext(searchText):
    f=open('fenci.txt','r')
    for line in f.readlines():
        result = line.startswith(searchText)
        if result==True:
            print(line)
            ret=line.split()
            ret.pop(0)
            return ret
    return ['NoFound']