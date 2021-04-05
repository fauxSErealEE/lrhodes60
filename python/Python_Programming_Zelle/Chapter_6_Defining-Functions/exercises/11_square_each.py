#square_each.py

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    return nums

def test():
    numList = [1,3,5,2,4,6]

    print("start test")
    print("\tbefore squaring")
    print(numList)
    print("\tafter squaring")
    numList = squareEach(numList)
    print(numList)
    print("end test")

test()