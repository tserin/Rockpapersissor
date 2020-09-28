# ✊🏻 ✋🏻 ✌🏻 🧔 💻 🎉 💀 🏆 ⛔ 🗑
import random
player_count=0
computer_counter=0
while player_count < 3 or computer_counter < 3:
    player_hand = input("🧔 : ")
    computer = random.randrange(3)  #0,1,2

    if(player_hand != "✊🏻"
    and player_hand != "✋🏻"
    and player_hand != "✌🏻"):
        print("⛔")
        print("")
        continue

    if computer == 0:
        computer ="✊🏻"
    elif computer == 1:
        computer= "✋🏻"
    else:
        computer = "✌🏻"
    print("💻 : " + computer)

    # 0. Draw - Skip round
    # 1. ✊🏻 beats ✌🏻
    # 2. ✋🏻 beats ✊🏻
    # 3. ✌🏻 beats ✋🏻

    if computer==player_hand:
        print("🗑")
    elif player_hand == "✊🏻":
        if computer =="✋🏻":
            print("You Lost ! ! ! 💀")
            computer_counter+=1
        else:
            print("You Won  🎉🎉🎉")
            player_count+=1
    elif player_hand == "✋🏻":
        if computer =="✌🏻":
            print("You Lost ! ! ! 💀")
            computer_counter+=1
        else:
            print("You Won  🎉🎉🎉")
            player_count+=1
    elif player_hand == "✌🏻":
        if computer =="✊🏻":
            print("You Lost ! ! ! 💀")
            computer_counter+=1
        else:
            print("You Won  🎉🎉🎉")
            player_count+=1
        pass
    print ("Player : "+ player_count * "🏆" +"Computer" + computer_counter * "🏆" )
    if player_count > computer_counter:
        print ("You Won the Game")
    else:
        print ("You Lose the Game")

