# A tutorial section for the game.
# Meet Dafny
# Choose meals
# Dafny's reaction
# Dafny is vegan
# Loss

label loophead:
    hide dafny
    hide basil
    scene bg restaurant with fade

    show dafny

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
        basil "(Did that weirdo put me in a time loop?)"

    elif loop_no == 3:
        basil "(Looks like I'm stuck in some kind of loop.)"

    elif loop_no <= 6:
        basil "(I'll keep trying until I get it right!)"

    elif loop_no % 2 == 1:
        basil "(I don't know how many times I've been here, but I won't give up!)"

    elif loop_no >= 10 and renpy.random.randint(1, 100) == 69:
        basil "(I'M BACK IN THIS FUCKING BUILDING AGAIN!)"

    else:
        basil "(I need to try something different this time!)"

    if loop_no >= 5:
        menu:
            "Would you like to skip ahead to the location choice?"

            "Yes":
                jump choice1

            "No":
                jump .sitting

label .sitting:

    if 2 <= loop_no <= 3:
        basil "Uh umm... no, I don't think so. I just got here."

    elif loop_no >= 4:
        basil "No, I just got here. I was waiting for you."

    dafny "Ah! Here we go, a nice place to sit."

# The tutorial meets the restaurant scene here
label restaurant:

    show dafny at left
    show basil at right

    if loop_no != 0:
        show screen lemmabutton()
        queue music "main/vara.ogg" fadein 3.0
    dafny "Hey uh, you said you were ordering us stuff right?"
    basil "Oh yeah!"
    dafny "Ummm, let's see here."
    "You two open the menu together."

    if loop_no >= 3:
        basil "(Do these things ever change?)"

    basil "Okay, ummm... entrées... let's see."

    menu:
        "Breadsticks":
            call .breadsticks from _call_restaurant_breadsticks

        "Crackers":
            call .crackers from _call_restaurant_crackers

    show dafny at left
    show basil at right

    dafny "I'm pretty thirsty. What should we drink?"
    basil "I think I'd like something shared."
    dafny "Oh yeah! Great idea!"
    dafny "One jug of...."

    menu:
        "Lemonade":
            call .lemonade from _call_restaurant_lemonade
        "Water":
            call .water from _call_restaurant_water

    show dafny at left
    show basil at right

    dafny "And for the main course, hmmm what to eat..."
    dafny "Oh you choose!"
    basil "Me?"
    dafny "You promised to choose for me!"
    basil "Alright, I choose..."
    
    play sound "sfx/choice.ogg"
    menu:
        "Curry":
            jump .curry

        "Chicken":
            jump .chicken

        "Tofu" if restaurant_info == True:
            jump .tofu

label .breadsticks:
    dafny "Oh, breadsticks! I love those!"
    basil "Oh, you do?"
    dafny "Great choice, Basil!"
    $ entree = "breadsticks"
    return

label .crackers:
    dafny "Crackers? I don't really like those..."
    show dafny sad 
    dafny "Too salty..."
    $ entree = "crackers"
    return

label .lemonade:
    show dafny happy
    dafny "Lemonade is my favourite! Great choice!"
    dafny "I can't wait!"
    $ drink = "lemonade"
    return

label .water:
    show dafny sad
    dafny "Water is good, but I was hoping for something a little sweeter..."
    basil "Like, um?"
    show basil sad
    dafny "I think everything that isn't water is sweeter."
    $ drink = "water"
    return

label .curry:
    show dafny angry
    dafny "YUCK! That's way too spicy for me!"
    dafny "Sorry, I don't think I can eat that..."
    show basil sad
    basil "Um, yeah, sorry..."
    jump .restaurant_badend

label .chicken:
    dafny "Umm..."
    show dafny angry
    dafny "I don't eat meat. I'm vegan."
    dafny "I thought you knew that..."
    show basil sad
    basil "Sorry..."
    basil "(Crap!)"
    jump .restaurant_badend

label .restaurant_badend:
    stop music fadeout 10.0
    show dafny at left
    show basil at right

    dafny "I don't think I'm gonna eat tonight."
    basil "Okay, um... fine... sorry."
    dafny "It's okay. I can buy my own food later."
    dafny "You know, that {b}tofu{/b} on the menu looked nice..."

    python:
        restaurant_info = True

    basil "You fine with just me eating tonight?"
    dafny "Yeah, I'm fine with just [entree] and [drink] tonight..."
    basil "Alright, y-yeah..."
    show basil sad
    show dafny sad
    dafny "..."
    basil "..."

    "Shortly after, Dafny left her seat and went home..."

    jump badend_a

label .tofu:
    queue music "main/varb.ogg"
    show dafny happy
    dafny "Oh hell yeah! Tofu! My favourite!"
    dafny "Thank you so much Basil! You read my mind!"
    basil "Y-yeah..."
    jump .success

label .success:
    scene bg restaurant with fade
    show dafny happy at left
    show basil at right
    dafny "Mmm!"
    dafny "I never knew this tofu was so good!"
    basil "It is?"
    basil "It's something I've never tried before, but yeah, it's pretty good."

    "..."
    dafny "Hey, you got any plans for tonight?"
    basil "Usually I go home and play solitaire..."
    dafny "Ooh! Let's do something fun tonight!"
    basil "Like what?"
    dafny "You know, I've always wanted to walk by that lake nearby."
    dafny "Ooh! Maybe that pool nearby too!" 
    basil "Pool?"
    dafny "How about the art museum!"
    dafny "Or maybe that weird-ass abandoned building. Hartley Teakle, right?"
    dafny "How about you?"
    basil "Me?"
    show basil thinking
    basil "How about the arcade?"
    dafny "Ooh I love the arcade!"
    basil "Or maybe karaoke?"
    basil "The casino?"
    basil "How about a spa?"
    dafny "Hm, nice ideas..."

    basil "(Maybe this is a date after all...)"
    basil "(It could end in something more...)"
    jump choice1
    return
