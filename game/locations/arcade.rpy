# Story - Arcade: 
# Choice: Choose an arcade game to play against Dafny.
#  Dafny has a game they are really really good at, which is Trimonis (based on the 3400 assignment).
#  Other games include Floyd-ger, Hoare-s Racing and Taiko.
# Information: (After choice) Dafny feels defeated by you at whatever game you picked,
#  but looks longingly at the game they are good at, Basil notices this (Arcade)
# Bad Ending: Breaks wrist during Taiko and has to be rushed to the emergency room


label arcade:

    scene bg arcade
    with fade

    show dafny at left
    show basil at right
    
    dafny "Wow, this arcade is so cool! I love playing games!"
    dafny "I can't wait to play some games with you!"
    dafny "What game should we play first? I have a few in mind, but I'm open to suggestions too!"

    python:
        games = ["floydger", "hoareracing", "taiko", "trimonis"]

        if not arcade_info:
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

        "Trimonis" if arcade_info:
            jump .trimonis

    dafny "That was fun but I think I would rather something involving more triangles..."
    
    dafny "That was so much fun! I love playing games with you!"
    dafny "We should do this more often!"

    jump choice2

label .floydger:
    dafny "Fun game where Robert W. Floyd is trying to cross an acyclic graph."
    call .arcadelearn
    return

label .hoareracing:
    dafny "Fun game where Tony Hoare is racing against you to sort a list."
    call .arcadelearn
    return

label .taiko:
    dafny "Fun game where you play drums!"
    "BANG BANG BANG"
    dafny "Ouch, I think I might have hurt my wrist..."
    jump .taiko_badend

label .trimonis:
    dafny "Fun game where you stack blocks composed of three equilateral triangles."
    # good ending
    return

label .arcade_badend:
    jump badend_a

label .taiko_badend:
    # Dafny's wrist is broken and they have to be rushed to the emergency room.
    call .arcadelearn
    jump generalbadend

label .arcadelearn:
    scene bg black with fade
    basil "(I just remembered now, she was looking at that {b}trimonis{\b} game)"
    python:
        arcade_info = True
    basil "(She didn't tell me, I felt like I should have chosen that one too.)"
    return
