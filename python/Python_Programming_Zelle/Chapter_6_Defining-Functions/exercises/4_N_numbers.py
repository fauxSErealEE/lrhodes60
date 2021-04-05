# N_numbers.py

def sumN(N):
    total = 0
    for i in range(N+1):
        total += i
    return total

def sumNCubes(N):
    total = 0
    for i in range(N+1):
        total += i**3
    return total

def main():
    n = eval(input("Enter n: "))
    
    total_sumN = sumN(n)
    total_sumNCubes = sumNCubes(n)

    print("The sum of the first {0} natural numbers is {1}.".format(n,total_sumN))
    print("The sum of the cubes of the first {0} natural numbers is {1}.".format(n,total_sumNCubes))

main()