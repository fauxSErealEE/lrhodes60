#to_numbers.py

def toNumbers(strList):
    numList = []
    for i in range(len(strList)):
        k = len(strList[i]) - 1
        tempNum = 0
        for ch in strList[i]:
            tempNum += (ord(ch) - ord("0")) * 10**k
            k -= 1
        numList.append(tempNum)
    return numList

def test():
    strNumList = ["9","120","43","69","420"]
    numList = []

    print("begin test")
    print(strNumList)
    numList = toNumbers(strNumList)
    print(numList)
    print("end test")

test()