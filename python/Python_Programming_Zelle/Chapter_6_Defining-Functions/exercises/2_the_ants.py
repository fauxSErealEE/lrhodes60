#the_ants.py
def marchingAnts(numAnts):
    return "The ants go marching " + numAnts +" by " + numAnts

def hurrah():
    return "hurrah, hurrah!"

def stanza(numAnts):
    ants = marchingAnts(numAnts)
    hurr = hurrah()
    stnz = ants + ", " + hurr
    print(stnz)

def littleOne(littleAction):
    print("The little one stops to " + littleAction + ",")

def tag():
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")

def verse(numAnts,littleAction):
    print()
    stanza(numAnts)
    stanza(numAnts)
    print(marchingAnts(numAnts)+",")
    littleOne(littleAction)
    tag()

def lastVerse(numAnts,littleAction):
    print()
    stanza(numAnts)
    stanza(numAnts)
    print(marchingAnts(numAnts)+",")
    littleOne(littleAction)

def main():
    verse("one","suck his thumb")
    verse("two","tie his shoe")
    verse("three","climb a tree")
    verse("four","shut the door")
    verse("five","take a dive")
    verse("six","pick up sticks")
    verse("seven","pray to heaven")
    verse("eight","check the gate")
    verse("nine","check the time")
    lastVerse("ten","say \"The End!\"")
main()