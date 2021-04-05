# create the game fizzbuzz and print the output from 1-100
# multiples of 3 print 'fizz'
# multiples of 5 print 'buzz'
# multiples of 3 and 5 print 'fizzbuzz'

def main():

    print("Printing the output of the game FizzBuzz from 1-100")

    
    for i in range(101):
        output = ""
        if ((i % 3) == 0):
            output += "Fizz"
        if ((i % 5) == 0):
            output += "Buzz"
        if ((i %3) !=0) and ((i % 5) != 0):
            output += str(i)

        print(output)


main()