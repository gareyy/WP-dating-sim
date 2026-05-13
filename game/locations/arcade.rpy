# Story - Arcade: 
# Choice: Choose an arcade game to play against Dafny.
#  Dafny has a game they are really really good at, which is Trimonis (based on the 3400 assignment).
#  Other games include Floyd-ger, Hoare Racing and Taiko.
# Information: (After choice) Dafny feels defeated by you at whatever game you picked,
#  but looks longingly at the game they are good at, Basil notices this (Arcade)
# Bad Ending: Breaks wrist during Taiko and has to be rushed to the emergency room

image cutscene taiko = Image("images/cutscene/taiko.png")

label arcade:

    scene bg arcade
    with fade
    show dafny at left
    show basil at right
    queue music "main/vara.ogg"
    
    dafny "Wow! This place is so bright!"
    basil "It's an arcade after all."
    dafny "Ooh! What should we play?"
    dafny "Ummm, lets see..."
    show dafny surprised
    dafny "Ooh! Floydger! Thats an oldie, how do they have a machine for a 40 year old game?"
    show dafny at left
    basil "Apparently this arcade loves to have their oldie games."
    dafny "It's about Robert W. Floyd trying to cross a whole acyclic graph."
    basil "You do know your games, huh?"
    show dafny surprised
    dafny "Wow! Is that Hoare Racing?"
    "You two look at the giant hard to miss cabinet."
    show dafny at left
    dafny "So this one is all about sorting a bunch of numbered blocks before the guy on screen sorts them first!"
    basil "Who's the guy?"
    dafny "Tony Hoare."
    basil "Huh."
    dafny "Oh, look, there's taiko too."
    basil "Oh hell yeah! That's my favourite!"
    basil "So that's the one where you bang a drum and stuff."
    basil "I'm nearly a pro at it."
    dafny "If you pick that one, I'm gonna try and outdo you!"
    basil "You sure? Have you ever played the game?"
    dafny "Eh, we'll see."
    
    "Dafny darts her eyes to to the Trimonis game."
    #"Basil notices how Dafny is staring at the Trimonis game, and then looks back at her."

    dafny "So which game do you wanna play? My treat."
    basil "Your treat? Is it because its only $3 a game?"
    dafny "..."
    dafny "Possibly."

    python:
        games = ["floydger", "hoareracing", "taiko"]

        if not arcade_info:
            choices = ["floydger", "hoareracing", "taiko"]
        else:
            choices = renpy.random.sample(games, 2)

    play sound "sfx/choice.ogg"

    menu:
        "Which game should the two play?"
        "Floydger" if "floydger" in choices:
            call .floydger from _call_arcade_floydger

        "Hoare Racing" if "hoareracing" in choices:
            call .hoareracing from _call_arcade_hoareracing

        "Taiko" if "taiko" in choices:
            call .taiko from _call_arcade_taiko

        "Trimonis" if arcade_info:
            jump .trimonis

    dafny "That was so much fun! I love playing games with you!"
    dafny "We should do this more often!"

    jump location_choice

label .floydger:
    #dafny "Fun game where Robert W. Floyd is trying to cross an acyclic graph."
    basil "Ok! Floydger!"
    dafny "The old one?"
    basil "Yeah.."
    dafny "Wow, this cabinet is old!"
    basil "How come you know this game?"
    dafny "Oh, my dad had this game on his old computer."
    dafny "Like old old."
    show basil surprised
    basil "..."
    show basil at right
    basil "Alright, uh, lets get this game started!"
    dafny "I hope I can remember how to play this..."
    scene bg black with fade
    scene bg arcade
    with fade
    show dafny sad at left
    show basil sad at right

    dafny "..."
    basil "..."
    "The cabinet's screen is flashing weird colours."
    dafny "Did we break the game?"
    basil "Yeah."
    dafny "It was because we were able to go back on the acyclic graph, right?"
    basil "Yep."
    show dafny at left
    show basil at right
    dafny "Let's leave before someone suspects us of breaking this thing."
    basil "Oh yep, definitely."
    call .arcadelearn from _call_arcade_arcadelearn
    jump .arcade_badend

label .hoareracing:
    #dafny "Fun game where Tony Hoare is racing against you to sort a list."
    basil "Here we go! Hoare Racing!"
    dafny "Kinda sounds like horse racing."
    basil "Ehhh, maybe."
    basil "This giant thing doesn't have any horses in it though."
    "Dafny scans the arcade card."
    dafny "Ok Tony Hoare, time to get sorted!"
    basil "Alright!"

    "The game starts, a bunch of blocks drop in front of the two, and a video of Tony Hoare sorting blocks appears."

    basil "Let's race Hoare!"

    scene bg black with fade
    scene bg arcade
    with fade
    show dafny sad at left
    show basil sad at right

    dafny "..."
    basil "..."
    "The arcade screen shows a video of Tony Hoare dancing"
    dafny "We lost."
    basil "Yeah."
    dafny "What a bummer to end the night."
    basil "You want to split ways now?"
    dafny "Sure..."

    call .arcadelearn from _call_arcade_arcadelearn_1
    jump .arcade_badend

label .arcade_badend:
    jump badend_a

label .taiko:
    #dafny "Fun game where you play drums!"
    basil "Let's play taiko!"
    "The two rush over to the taiko machine."
    basil "Alright let's see here, I want to warm up with a good and easy song."
    basil "Ah here! Idol by YOASOBI."
    "The taiko machine plays Idol, but it is the English version nobody likes."
    basil "..."
    basil "Fine enough."
    dafny "So how do you play this game again?"
    basil "Oh so when you see those blue things, you hit the edge of the drum, and when you see those red things, you hit the center of the drum!"
    dafny "Oh!"
    dafny "Sounds easy."
    "Dafny picks the hardest difficulty for the song."
    basil "Wait Dafny! Please no!"
    dafny "Trust me, I know what I'm doing."
    scene bg black with fade
    "One song later..."
    "BANG BANG BANG"
    dafny "Ouch, I think I might have hurt my wrist..."
    scene bg arcade
    with fade
    show dafny sad at left
    show basil at right
    dafny "Owwww owww."
    basil "Are you okay?"
    dafny "Oh yeah, it's just..."
    "Dafny sits on the floor."
    dafny "AHHHH!"
    basil "Okay, breathe in, breathe out,"
    basil "(I gotta call the ambulance.)"
    dafny "Ouch..."
    basil "I should have warned you not to pick that difficulty."
    show cutscene taiko with fade
    play sound "sfx/fail.ogg"
    basil "I followed her on the ambulance to the hospital."
    basil "They were able to stabilise her."
    basil "Unfortunately, she wasn't able to work for the next few months."
    basil "Crap, I feel so bad for letting her down like this..."
    call .arcadelearn from _call_arcade_arcadelearn_2
    jump generalbadend

label .trimonis:
    #dafny "Fun game where you stack blocks composed of three equilateral triangles."
    dafny "I didn't expect you to pick this game."
    basil "Why's that?"
    dafny "Because I'd destroy you in it of course!"
    dafny "Do you even know how this game works?"
    basil "Um, no."
    dafny "Ok so you gotta basically stack these triangle things on top of each other, and yeah that's it!"
    basil "Ok you know what, sounds fun."
    basil "Let's go!"
    scene bg black with fade
    scene bg arcade with fade
    show dafny at left
    show basil at right
    dafny "Yeah! I win!"
    basil "Aww, I lost..."
    dafny "You know what? As a consolation prize."
    "Dafny gives Basil a peck on the cheek."
    show basil blushing
    basil "!!!"
    dafny "You like that huh?"
    basil "Y-yeah.."
    dafny "Enjoy your prize."
    basil "..."

    $ good_arcade = True
    jump location_choice


label .arcadelearn:
    scene bg black with fade
    call add_lemma("Dafny's favourite game is Trimonis")
    $ arcade_info = True
    basil "(I just remembered now, she was looking at that {b}Trimonis{\b} game)"

    basil "(She didn't tell me, I felt like I should have chosen that one too.)"

    return
