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
        basil "(Wait... I thought I had already been here before...)"
        basil "Uh umm... no, I don't think so. I just got here."
        dafny "Alright, well, I hope you got us a seat!"
        basil "Um actually..."
        hide dafny
        jump tutorial

    elif loop_no == 2:
        basil "(This is getting weird...)"

    elif loop_no == 3:
        basil "(Looks like I'm stuck in some kind of loop.)"

    elif loop_no <= 6:
        basil "(I'll keep trying until I get it right!)"

    elif loop_no % 2 == 1:
        basil "(I don't know how many times I've been here, but I won't give up!)"

    else:
        basil "(I need to try something different this time!)"


    if 2 <= loop_no <= 3:
        basil "Uh umm... no, I don't think so. I just got here."

    elif loop_no >= 4:
        basil "No, I just got here. I was waiting for you."

    dafny "Ah! Here we go, a nice place to sit."

# The tutorial meets the restaurant scene here
label restaurant:

    show dafny

    dafny "Hey uh, you said you were ordering us stuff right?"
    basil "Oh yeah!"
    dafny "Ummm lets see here."
    "You two open the menu together"

    if loop_no >= 3:
        basil "(Do these things ever change?)"

    basil "Okay ummm entries... Lets see."

    menu:
        "Breadsticks":
            call .breadsticks

        "Crackers":
            call .crackers
    
    dafny "I'm pretty thirsty, what should we drink?"
    basil "I think I would like something shared."
    dafny "Oh yeah! Great idea!"
    dafny "One jug of...."

    menu:
        "Lemonade":
            call .lemonade
        "Water":
            call .water

    dafny "And for the main course, hmmm what to eat..."
    dafny "Oh you choose!"
    basil "Me?"
    dafny "You promised to choose for me!"
    basil "Alright, I choose..."
    
    menu:
        "Curry":
            jump .curry

        "Chicken":
            jump .chicken

        "Tofu" if restaurant_info == True:
            jump .tofu

label .breadsticks:
    dafny "Oh, breadsticks! I love those!"
    basil "Oh you do?"
    return

label .crackers:
    dafny "Crackers? I don't really like those..."
    dafny "ass"
    return

label .lemonade:
    dafny "Lemonade is my favorite! Great choice!"
    return

label .water:
    dafny "Water is good, but I was hoping for something a little sweeter..."
    return

label .curry:
    dafny "YUCK! That's way too spicy for me!"
    dafny "Sorry, I don't think I can eat that..."
    basil "Um, yeah, sorry..."
    jump .restaurant_badend

label .chicken:
    dafny "Umm..."
    dafny "I don't eat meat. I'm vegan."
    dafny "I thought you knew that..."
    basil "Sorry..."
    jump .restaurant_badend

label .restaurant_badend:
    python:
        restaurant_info = True
    jump badend_a

label .tofu:
    dafny "TOFU!!"
    jump .success

label .success:
    dafny "LETS GO SOMEWHERE ELSE TONITE"
    # GO TO LOCATION CHOICE
    jump museum
    return
