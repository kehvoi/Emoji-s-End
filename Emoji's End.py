print("Emojis are living happily in a building, \n"
      "but on of them is a terrorist\n"
      "who do you think is the bad emoji?")


floor3 = ["🤩","🥴","🤭"]
floor2 = ["🤮","🥵","🥰"]
floor1 = ["🥺","🤮","🥴"]
building = [floor1, floor2, floor3]
print(f"{floor3}\n{floor2}\n{floor1}")
mapinput = input("Which emoji is your target?\n "
                 "type the first digit for the floor \n"
                 "and the second digit for the window\n"
                 "double digits only from 1 to 3")
atkfloor = int(mapinput[0])
atkwindow = int(mapinput[1])

selectedEmoji = building[atkfloor - 1][atkwindow - 1]
print(selectedEmoji)

print("This emoji will die \n ")
building[atkfloor - 1][atkwindow - 1] = "💀"
print(f"{floor3}\n{floor2}\n{floor1}")
print("you saved the other emojis from the terrorist\n"
      "congratulations"
      "\nnow all the emojis will be able to sleep in peace\n"
      "knowing that an unknown force is eliminating them by assumption")
print("Yay!")