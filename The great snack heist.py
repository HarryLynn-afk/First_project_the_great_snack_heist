print(r'''  ___________,_____
      |     |  #  |=====|
      |     | (_) |=====|
      |> _  |_____|=====|
      | [_] |     |     |
      |     |_____|=====|
      |     |     |_____|
      |   ] |_____|     |
      |     |_____|=====|
      |     | ___ |_____|
      |>    |[___]|     |
      |     |[___]|=====|
      |_____|=====|_____|
''')
print("The Great Snacks Heist")
print("______________________")
print("It’s midnight.\n"
      "The house is silent, and your stomach growls louder than your conscience. \n"
      "The mission is clear – steal snacks without waking anyone… or the cat.")
print("______________________")
print("You tiptoe into the kitchen, avoiding every creaky floorboard like a ninja.\n"
      "But how will you pull off the heist?")
print("______________________")

print("Options:(Enter Only Number!)")
option_1 = (input("1.Open the fridge quietly.\n"
                  "2.Check the pantry instead.\n"
                  "3.Snatch leftovers from the table.\n"))

if option_1 == "1":
    print("You carefully pull the fridge door open.\n"
          "The light blazes like a spotlight at a crime scene.\n"
          "The cat's eyes reflect the light, glowing like two tiny headlights.\n"
          "It blinks slowly, watching your every move.\n"
          "What happens next?(Enter only number!)\n"
          "------------------------------------")
    option_1_1 = (input("1.Close the fridge and try again.\n"
                        "2.Grab snacks quickly and close the door\n"))
    if option_1_1 == "1":
        print("You gently close the fridge, hoping the cat forgets what it saw.\n"
              "It does not. The cat tilts its head, eyes narrowing.\n"
              "Suddenly, it lets out a long, dramatic meow that echoes through the house.\n"
              "--------------------------\n"
              "Grandma's voice drifts down the hallway. Who’s in the kitchen?\n"
              "You freeze. The cat wins.\n"
              "-------------------------\n"
              "       GAME OVER         ")
    elif option_1_1 == "2":
        print("In one swift move, you grab whatever your hand touches –\n"
              " cheese slices, leftover cake, a questionable yogurt.\n"
              "You slam the door shut, narrowly escaping the cat’s judgment.\n"
              "You disappear into the night, snacks in hand.\n"
              "--------------------------\n"
              "          VICTORY           ")
    else:
        print("Invalid!Pleaser Enter 1 or 2.")

elif option_1 == "2":
    print("You tiptoe toward the pantry, carefully turning the knob.\n"
          "CREEEEEEAK. The sound is deafening in the silence.\n"
          "You hold your breath, glancing nervously toward the cat.\n"
          "What happens next?(Enter only number!)")
    option_1_2 = (input("1.Tiptoe away quietly.\n"
                        "2.Slam the door and run.\n"))
    if option_1_2 == "1":
        print("You freeze for a moment, then silently back away like you were never there.\n"
              "The cat blinks, seemingly unimpressed by your escape.\n"
              "You live to snack another day.\n"
              "-----------------------------\n"
              "         GAME OVER           ")
    elif option_1_2 == "2":
        print("Panic takes over.\n"
              "You slam the pantry shut and sprint down the hall.\n"
              "Unfortunately, you forgot about the laundry basket in your path.\n"
              "You trip and crash to the floor, making more noise than a marching band\n"
              "Lights flick on upstairs!"
              "-----------------------------"
              "        GAME OVER            ")
    else:
        print("Invalid!Please Enter 1 or 2.")

elif option_1 == "3":
    print("You spot a plate of food left on the table.\n"
          "Desperate and starving, you grab it and take a bite.\n"
          "It’s chewy. Too chewy.\n"
          "---------------------------------\n"
          "You glance down in horror – it’s the dog’s food.\n"
          "What happens next?(Enter only number!\n")
    option_1_3 = input("1.Keep eating and pretend nothing’s wrong.\n"
                       "2.Spit it out and abandon the mission.\n")
    if option_1_3 == "1":
        print("You continue chewing slowly, locking eyes with the cat as if daring it to challenge you.\n"
              "The dog appears in the doorway, staring in disbelief at the betrayal.\n"
              "In the end, the dog lets you live – but trust is forever broken.\n"
              "----------------------------\n"
              "        GAME OVER            \n")
    elif option_1_3 == "2":
        print("ou gag and spit the food back onto the plate, leaving the evidence for someone else to find.\n"
              "The cat watches in silence, quietly judging your life choices.\n"
              "No snacks tonight, but at least your pride is intact.\n"
              "----------------------------\n"
              "       GAME OVER             \n")
else:
    print("Invalid!Pleaser Enter 1 or 2 or 3.")

