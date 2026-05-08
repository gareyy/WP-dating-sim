# A tutorial section for the game.


# ?
# Meet Dafny
# Choose meals
# Dafny's reaction
# Dafny is vegan
# Loss

label loophead:
    scene bg restaurant
    with fade

    dafny "Hey, have you been waiting long?"

    if loop_no == 0:
        basil "No, I just got here. I was waiting for you."

    elif loop_no == 1:
        
        basil "Huh?"
        "Wait... I thought I had already been here before..."
        basil "Uh umm... no, I don't think so. I just got here."
        dafny "Alright, well it's nice to see you!"
        dafny "I'm going to sit down, do you want to join me?"
        hide dafny
        jump tutorial

    elif loop_no == 2:
        "This is getting weird..."

    elif loop_no == 3:
        "Looks like I'm stuck in some kind of loop."

    elif loop_no <= 6:
        "I'll keep trying until I get it right!"

    elif loop_no % 2 == 1:
        "I don't know how many times I've been here, but I won't give up!"

    else:
        "I need to try something different this time!"


    if 2 <= loop_no <= 3:
        basil "Uh umm... no, I don't think so. I just got here."

    elif loop_no >= 4:
        basil "No, I just got here. I was waiting for you."

    dafny "Alright, well it's nice to see you!"

# The tutorial meets the restaurant scene here
label restaurant:

    show dafny

    dafny "Would you like to order something to eat?"

    menu:

        "Breadsticks":
            call .breadsticks

        "Crackers":
            call .crackers
    
    dafny "I'm pretty thirsty, what would you like to drink?"

    menu:
        "Lemonade":
            call .lemonade
        "Water":
            call .water

    dafny "And for the main course, what would you like to eat?"

    menu:
        "Curry":
            call .curry

        "Chicken":
            call .chicken

label .breadsticks:
    dafny "Oh, breadsticks! I love those!"
    return

label .crackers:
    dafny "Crackers? I don't really like those..."
    return

label .lemonade:
    dafny "Lemonade is my favorite! Great choice!"
    return

label .water:
    dafny "Water is good, but I was hoping for something a little sweeter..."
    return

label .curry:
    dafny "GWAHHH! That's way too spicy for me!"
    dafny "Sorry, I don't think I can eat that..."
    jump badend

label .chicken:
    dafny "Umm..."
    dafny "I don't eat meat. I'm vegan."
    dafny "I thought you knew that..."
    jump badend