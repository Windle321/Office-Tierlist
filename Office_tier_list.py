
global favorite3
global e1
global e2
global e3
global e4
global e5
global e6
global episode_totals 

episode_totals = [] 

favorite3 = []

  
def pick_3():
    global favorite3
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global episode_totals 
    print("to select a character, input the number of that character on the list")
    print("pick your 3 favroite characters") 
    
    selection = int(input("enter your FAVORITE The Office! character -> "))
    favorite3.append(selection)
    
    selection = int(input("enter your SECOND FAVORITE The Office! character -> "))
    favorite3.append(selection)

    selection = int(input("enter your THIRD FAVORITE The Office! character -> "))
    favorite3.append(selection)





def character_select(): 
    print("[1] Michael Scott")
    print("[2] Pam Beesly")
    print("[3] Jim Halpert")
    print("[4] Dwight Schrute")
    print("[5] Ryan Howard")
    print("[6] Phyllis vance")
    print("[7] Angela Martin")
    print("[8] Kevin Malone")
    print("[9] Toby Flenderson")
    print("[10] Meredith Palmer")
    print("[11] Stanley Hudson")
    print("[12] Oscar Martinez")
    print("[13] Creed Bratton")
    print("[14] Darryl Phlibin")
    print("[15] Roy Anderson")

def episodes():    
    global favorite3
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global episode_totals 

    e1 = [8, 6, 10, 6, 4, 2, 1, 1, 0, 2, 4, 3, 0, 0, 3]
    e2 = [9, 4, 6, 7, 3, 1, 2, 3, 2, 1, 5, 4, 0, 0, 0]
    e3 = [9, 6, 9, 9, 0, 0, 2, 4, 0, 0, 2, 1, 0, 0, 0]
    e4 = [10, 8, 9, 8, 1, 5, 6, 1, 3, 4, 4, 7, 0, 0, 0]
    e5 = [9, 8, 8, 8, 5, 3, 0, 4, 0, 0, 0, 4, 0, 6, 7]
    e6 = [10, 7, 8, 8, 3, 0, 3, 0, 2, 0, 4, 0, 0, 0, 5]


def point_assignment(): 

    global favorite3
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global episode_totals 

    firstpick = favorite3[0]
    secondpick = favorite3[1]
    thirdpick = favorite3[2]


    a = firstpick - 1 
    b = secondpick - 1
    c = thirdpick - 1 

    e1[a] = e1[a] * 4 
    e1[b] = e1[b] * 3 
    e1[c] = e1[c] * 2 

    e2[a] = e2[a] * 4 
    e2[b] = e2[b] * 3
    e2[c] = e2[c] * 2

    e3[a] = e3[a] * 4 
    e3[b] = e3[b] * 3
    e3[c] = e3[c] * 2

    e4[a] = e4[a] * 4 
    e4[b] = e4[b] * 3
    e4[c] = e4[c] * 2

    e5[a] = e5[a] * 4 
    e5[b] = e5[b] * 3
    e5[c] = e5[c] * 2

    e6[a] = e6[a] * 4 
    e6[b] = e6[b] * 3
    e6[c] = e6[c] * 2



def episode_ranks(): 

    global favorite3
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global episode_totals 

    e1sum = sum(e1)
    e2sum = sum(e2)
    e3sum = sum(e3)
    e4sum = sum(e4)
    e5sum = sum(e5)
    e6sum = sum(e6)

    episode_totals.append(e1sum)
    episode_totals.append(e2sum)
    episode_totals.append(e3sum)
    episode_totals.append(e4sum)
    episode_totals.append(e5sum)
    episode_totals.append(e6sum)

    winner = max(episode_totals)
    first = episode_totals.index(winner)
    episode_totals[first] = 0 
    print("Best episode:", (first + 1))

    winner = max(episode_totals)
    second = episode_totals.index(winner)
    episode_totals[second] = 0
    print("Second best episode:", second + 1)

    winner = max(episode_totals)
    third = episode_totals.index(winner)
    episode_totals[third] = 0 
    print("Third best episode:", (third + 1))

    winner = max(episode_totals)
    fourth = episode_totals.index(winner)
    episode_totals[fourth] = 0 
    print("Fourth best episode:", (fourth + 1))

    winner = max(episode_totals)
    fifth = episode_totals.index(winner)
    episode_totals[fifth] = 0 
    print("Fifth best episode:", (fifth + 1))

    winner = max(episode_totals)
    last = episode_totals.index(winner)
    episode_totals[last] = 0 
    print("Worst episode:", (last + 1))

    
    
    
    

def main(): 
    character_select()
    pick_3()
    episodes()
    point_assignment()
    print(e1)
    print(e2)
    print(e3)
    print(e4)
    print(e5)
    print(e6)
    episode_ranks()
    print(episode_totals)

main()






