
def wanttriplets (Box, ElementCount):
    found = True
    for first in range(0, ElementCount - 2):
        for second in range(first+1, ElementCount - 1):
            for third in range(second+1, ElementCount):
                if(Box [first] + Box [second] + Box [third] == 0):
                    print(Box[first], Box[second], Box[third])
                    found = True
                else:
                    print("no")

Box=[]
ElementsCount=int(input('Enter  number of elements you want to check:---'))
for i in range(0, ElementsCount):
    Element=int(input())
    Box.append(Element)


wanttriplets(Box, ElementsCount)


