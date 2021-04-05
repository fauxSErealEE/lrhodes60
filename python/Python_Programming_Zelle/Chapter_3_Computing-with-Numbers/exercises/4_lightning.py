#lightning.py

def main():
    time = eval(input("Enter time elapsed between seen and heard: "))

    vel_sound = 1100
    mile_ft = 5280

    dist = float(time * vel_sound) / float(mile_ft)

    print("The lightning strike is {:0.2f} miles away".format(dist))

main()