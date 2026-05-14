# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define basil = Character("Basil", color="#c8ffc8")
define dafny = Character("Dafny", color="#ffffc8")
define isabelle = Character("Isabelle", color="#715bff")

image bg black = "#000"
image bg white = "#FFF"
image bg lab = Image("images/backgrounds/lab_resized.png")
image bg restaurant = Image("images/backgrounds/restaurant.png")
image bg museum = Image("images/backgrounds/museum.png")
image bg pool = Image("images/backgrounds/pool_resized.png")
image bg alleyway = Image("images/backgrounds/alleyway.png")
image bg karaoke = Image("images/backgrounds/karaoke_bg.png")
image bg spa = Image("images/backgrounds/spa.png")
image bg arcade = Image("images/backgrounds/arcade.png")
image bg uqlakes = Image("images/backgrounds/lake.png")
image bg hartley = Image("images/backgrounds/hartley.png")
image bg casino = Image("images/backgrounds/casino.png")
image bg house = Image("images/backgrounds/bedroom.png")

image verifying:
    "images/verification/verify.png"
    0.35 # Wait for 0.35 seconds
    "images/verification/verify2.png"
    0.35 # Wait for 0.35 seconds
    repeat # Loop forever

image verifying_light:
    "images/verification/verify_light.png"
    0.4 # Wait for 0.4 seconds
    "images/verification/verify_light2.png"
    0.4 # Wait for 0.4 seconds
    repeat # Loop forever

# oversample = 6 if TODO sprite
image basil = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=3))
image basil happy = Crop((0, 0, 925, 925), Image("images/basil/Happy.png", oversample=3))
image basil laughing = Crop((0, 0, 925, 925), Image("images/basil/Laughing.png", oversample=3))
image basil normal = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=3))
image basil surprised    = Crop((0, 0, 925, 925), Image("images/basil/Surprise.png", oversample=3))
image basil thinking = Crop((0, 0, 925, 925), Image("images/basil/Thinking.png", oversample=3))
image basil hesitant = Crop((0, 0, 925, 925), Image("images/basil/Hesitant.png", oversample=3))
image basil blushing = Crop((0, 0, 925, 925), Image("images/basil/Blushing.png", oversample=3))
image basil angry = Crop((0, 0, 925, 925), Image("images/basil/Angry.png", oversample=3))
image basil sad = Crop((0, 0, 925, 925), Image("images/basil/Sad.png", oversample=3))
image basil pooped = Crop((0, 0, 925, 925), Image("images/basil/Pooped.png", oversample=3))
image basil swimwear = Crop((0, 0, 925, 925), Image("images/basil/Swimwear.png", oversample=3))
image basil swimwear blushing = Crop((0, 0, 925, 925), Image("images/basil/Swimwear_Blush.png", oversample=3))
image basil swimwear happy = Crop((0, 0, 925, 925), Image("images/basil/Swimwear_Happy.png", oversample=3))
image basil swimwear lovestruck = Crop((0, 0, 925, 925), Image("images/basil/Swimwear_Lovestruck.png", oversample=3))
image basil swimwear sad = Crop((0, 0, 925, 925), Image("images/basil/Swimwear_Sad.png", oversample=3))

image dafny = Crop((0, 0, 925, 925), Image("images/dafny/Neutral.png", oversample=3))
image dafny happy = Crop((0, 0, 925, 925), Image("images/dafny/Happy.png", oversample=3))
image dafny blushing = Crop((0, 0, 925, 925), Image("images/dafny/Blushing.png", oversample=3))
image dafny excited = Crop((0, 0, 925, 925), Image("images/dafny/Flustered_Excited.png", oversample=3))
image dafny lovestruck = Crop((0, 0, 925, 925), Image("images/dafny/Lovestruck.png", oversample=3))
image dafny sad = Crop((0, 0, 925, 925), Image("images/dafny/Disappointed.png", oversample=3))
image dafny laughing = Crop((0, 0, 925, 925), Image("images/dafny/Flustered_Excited.png", oversample=3))

image dafny surprised = Crop((0, 0, 925, 925), Image("images/dafny/Flustered.png", oversample=3))
image dafny angry = Crop((0, 0, 925, 925), Image("images/dafny/Angry.png", oversample=3))
image dafny scared = Crop((0, 0, 925, 925), Image("images/dafny/Scared.png", oversample=3))
image dafny swimwear = Crop((0, 0, 925, 925), Image("images/dafny/Swimwear.png", oversample=3))
image dafny swimwear angry = Crop((0, 0, 925, 925), Image("images/dafny/Swimwear_Angry.png", oversample=3))
image dafny swimwear happy = Crop((0, 0, 925, 925), Image("images/dafny/Swimwear_Happy.png", oversample=3))
image dafny swimwear blushing = Crop((0, 0, 925, 925), Image("images/dafny/Swimwear_Blush.png", oversample=3))

image isabelle = Crop((0, 0, 925, 925), Image("images/isabelle/Neutral.png", oversample=6))


define whitefade = Fade(1.0, 1.0, 0.5, color='#fff')

transform left:
    xalign 0.25
    yalign 1.0

transform right:
    xalign 0.75
    yalign 1.0

# The game starts here.

label add_lemma(lemma, notify=True):

    $ lemmas_list.add(lemma)

    if notify:
        show screen lemmabutton()
        play sound "sfx/discovery.ogg"
    
    return

# TODO: Make sure this works
label untoggle_lemma(lemma):
    "lemma = False"
    return

label choice(label, lemma):
    $ store.last_label = label
    if infos_map[lemmas_map[lemma]] == label:
        $ setattr(store, lemmas_map.get(lemma), True)
    else:
        basil "(I don't think that would work here...)"
    
    if label == "give_location_choice":
        call give_location_choice(last_location_choices)
        return
    jump expression label

init python:
    def label_callback(name, abnormal):
        if name == "add_lemma":
            return
        store.last_label = name
        return

    config.label_callback = label_callback

label start:

    python:
        loop_no = -1
        restaurant_info = False
        karaoke_info = False
        spa_info = False
        pool_info = False
        arcade_info = False
        museum_info = False
        lake_info = False
        seen_choice1 = False
        seen_choice2 = False
        lemmas_list = set()
        lemmas_map = {
            "Dafny's favourite game is Trimonis": "arcade_info",
            "Dafny would like to see art of themself one day": "museum_info",
            "Dafny's favourite animal is a raven": "lake_info",
            "Dafny would like to go in a hot tub with Basil sometime": "spa_info",
            "Dafny is attracted to Basil's stare": "pool_info",
            "Dafny likes romantic songs": "karaoke_info",
            "Dafny's favourite food is tofu": "restaurant_info"
        }
        infos_map = {
            "arcade_info": "arcade_choice",
            "museum_info": "museum_choice",
            "lake_info": "uqlakes_choice",
            "spa_info": "spa_choice",
            "pool_info": "pool_choice2",
            "karaoke_info": "karaoke_choice",
            "restaurant_info": "restaurant_choice"
        }
        good_museum = False
        good_lake = False
        good_spa = False
        good_pool = False
        good_arcade = False
        good_karaoke = False
        seen_hartley = False
        seen_casino = False
        # Done choices track whether the player has made the location choice
        #     *in this loop*
        done_choice1 = False
        done_choice2 = False
        last_location_choices = []

    default preferences.volume.music = 0.5

    jump prologue

label loophead:

    python:
        loop_no = loop_no + 1
        done_choice1 = False
        done_choice2 = False

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

    elif loop_no >= 10 and renpy.random.randint(1, 100) == 69:
        basil "(I'M BACK IN THIS FUCKING BUILDING AGAIN!)"

    elif loop_no % 3 == 0:
        basil "(I don't know how many times I've been here, but I won't give up!)"
    elif loop_no % 3 == 1:
        basil "(I need to remember what I know about Dafny!)"
        show screen lemmabutton
    else:
        basil "(I need to try something different this time!)"

    if loop_no >= 5:
        menu:
            "Would you like to skip ahead to the location choice?"

            "Yes":
                show screen lemmabutton()
                jump location_choice

            "No":
                pass

    if 2 <= loop_no <= 3:
        basil "Uh umm... no, I don't think so. I just got here."

    elif loop_no >= 4:
        basil "No, I just got here. I was waiting for you."

    dafny "Ah! Here we go, a nice place to sit."

    jump restaurant

# Determine where to send the player next.
# Callback for all locations.
label location_choice:
    if not done_choice1:
        jump choice1
    elif not done_choice2:
        jump choice2
    else:
        jump choice3


label choice1:
    basil "(Where should we go next?)"
    python:
        stage1locations = ["pool", "lake", "museum", "hartley"]

        if not seen_choice1:
            choices = ["pool", "lake", "museum"]
        else:
            choices = renpy.random.sample(stage1locations, 3)

        seen_choice1 = True
        done_choice1 = True
    
    call give_location_choice(choices)



label choice2:
    basil "(Where should we go next?)"

    python:
        stage2locations = ["spa", "casino", "arcade", "karaoke"]

        if not seen_choice2:
            choices = ["spa", "arcade", "karaoke"]
        else:
            choices = renpy.random.sample(stage2locations, 3)
        
        seen_choice2 = True
        done_choice2 = True

    call give_location_choice(choices)


label choice3:
    dafny "Tonight has been so much fun! I don't want it to end yet!"
    dafny "Where should we go next? Or do you want to come back to my place?"

    menu:
        "Let's go to your place":
            jump ending

        "Let's go somewhere else":
            jump choice_all


# Allows the player to choose from locations they haven't finished,
# or locations they might want to revisit if they have already finished multiple
label choice_all:

    python:
        good_choices = [
            "pool" if not good_pool else None,
            "lake" if not good_lake else None,
            "museum" if not good_museum else None,
            "karaoke" if not good_karaoke else None,
            "spa" if not good_spa else None,
            "arcade" if not good_arcade else None,
            "hartley" if not seen_hartley else None,
            "casino" if not seen_casino else None
        ]
        good_choices = [x for x in good_choices if x is not None]

        bad_choices = [
            "pool" if good_pool else None,
            "lake" if good_lake else None,
            "museum" if good_museum else None,
            "karaoke" if good_karaoke else None,
            "spa" if good_spa else None,
            "arcade" if good_arcade else None,
            "hartley" if seen_hartley else None,
            "casino" if seen_casino else None
        ]
        bad_choices = [x for x in bad_choices if x is not None]

        choices = renpy.random.sample(good_choices, min(4, len(good_choices)))
        if len(choices) < 4:
            choices += renpy.random.sample(bad_choices, 4-len(choices))
        choices = ["house"] + choices
    
    call give_location_choice(choices)


label give_location_choice(choices):

    $ last_location_choices = choices

    play sound "sfx/choice.ogg"

    menu:
        "Where should we go?"

        "Dafny's House" if "house" in choices:
            jump choice3

        # Location choice 1
        "The Pool" if "pool" in choices and not good_pool:
            dafny "Ooh, I love going to the pool! That sounds like so much fun!"
            jump pool
        "The Pool ⭐" if "pool" in choices and good_pool:
            dafny "Ooh, I love going to the pool! That sounds like so much fun!"
            jump pool
        "The Lake" if "lake" in choices and not good_lake:
            dafny "The lake sounds like a nice place to spend time!"
            jump uqlakes
        "The Lake ⭐" if "lake" in choices and good_lake:
            dafny "The lake sounds like a nice place to spend time!"
            jump uqlakes
        "The Museum" if "museum" in choices and not good_museum:
            dafny "I love visiting museums! That sounds like a great idea!"
            jump museum
        "The Museum ⭐" if "museum" in choices and good_museum:
            dafny "I love visiting museums! That sounds like a great idea!"
            jump museum
        "Hartley Teakle" if "hartley" in choices and not seen_hartley:
            show dafny sad
            dafny "Ew, that place looks really creepy and scary. I don't think I want to go there..."
            basil "You sure? Could be fun though!"
            jump hartley
        "Hartley Teakle ⭐" if "hartley" in choices and seen_hartley:
            show dafny sad
            dafny "Ew, that place looks really creepy and scary. I don't think I want to go there..."
            basil "You sure? Could be fun though!"
            jump hartley

        # Location choice 2
        "The Karaoke" if "karaoke" in choices and not good_karaoke:
            dafny "Ooh, I love karaoke! That sounds like so much fun!"
            jump karaoke
        "The Karaoke ⭐" if "karaoke" in choices and good_karaoke:
            dafny "Ooh, I love karaoke! That sounds like so much fun!"
            jump karaoke
        "The Spa" if "spa" in choices and not good_spa:
            dafny "A spa day sounds so relaxing and fun! I would love to go to the spa with you!"
            jump spa
        "The Spa ⭐" if "spa" in choices and good_spa:
            dafny "A spa day sounds so relaxing and fun! I would love to go to the spa with you!"
            jump spa
        "The Arcade" if "arcade" in choices and not good_arcade:
            dafny "Let's go to the arcade! I love playing games!"
            jump arcade
        "The Arcade ⭐" if "arcade" in choices and good_arcade:
            dafny "Let's go to the arcade! I love playing games!"
            jump arcade
        "The Casino" if "casino" in choices and not seen_casino:
            dafny "Hmm, neither of us like gambling, or have much money to gamble with."
            basil "This could be life-changing money."
            basil "Let's go."
            jump casino
        "The Casino ⭐" if "casino" in choices and seen_casino:
            dafny "Hmm, neither of us like gambling, or have much money to gamble with."
            basil "This could be life-changing money."
            basil "Let's go."
            jump casino

    return

