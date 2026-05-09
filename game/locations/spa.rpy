# Story - Spa:
# Choice: Dafny says they want to do something physical (implied to be a bit intimate).
#  Dafny wants to do the hot and steamy hot tub.
#  The other choices result in death
# Information: (After choice) when doing the something physical Dafny whispers
#  some sweet nothings into Basil’s ear, and directly says they would like Basil say to them
#  “THE CORRECT CHOICE FOR POOL” (Pool) 
# Bad Ending: Hypothermia, accidentally neck snapped by Dafny during massage
# Monadic Mind



label spa:

    scene bg spa
    with fade

    show dafny at left
    show basil at right
    
    dafny "Oh, this place is so nice and relaxing! I love it here!"
    dafny "I can't wait to spend some time here with you!"

    python:
        games = ["floydger", "hoareracing", "taiko", "trimonis"]

        if not spa_info:
            choices = ["floydger", "hoareracing", "taiko"]
        else:
            choices = random.sample(games, 2)

    menu:
        
        "Floydger" if "floydger" in choices:
            call .floydger

        "Hoare's Racing" if "hoareracing" in choices:
            call .hoareracing

        "Taiko" if "taiko" in choices:
            call .taiko

        "Trimonis" if spa_info:
            jump .trimonis

    dafny "That was fun but I think I would rather something involving more triangles..."
    
    dafny "That was so much fun! I love playing games with you!"
    dafny "We should do this more often!"

    jump choice2

label .floydger:
    dafny "Fun game where Robert W. Floyd is trying to cross an acyclic graph."
    return

label .hoareracing:
    dafny "Fun game where Tony Hoare is racing against you to sort a list."
    return

label .taiko:
    dafny "Fun game where you play drums!"
    "BANG BANG BANG"
    dafny "Ouch, I think I might have hurt my wrist..."
    jump .taiko_badend

label .trimonis:
    dafny "Fun game where you stack blocks composed of three equilateral triangles."
    return

label .spa_badend:
    jump badend_a

label .taiko_badend:
    # Dafny's wrist is broken and they have to be rushed to the emergency room.
    jump generalbadend