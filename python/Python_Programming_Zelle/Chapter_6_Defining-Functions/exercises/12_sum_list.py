#sum_list.py

def sumList(nums):
    sumTotal = 0
    for i in range(len(nums)):
        sumTotal += nums[i]
    return sumTotal

def test():
    numList = [1,3,5,2,4,6]

    print("start test")
    sumTotal = sumList(numList)
    print(sumTotal)
    print("end test")

test()