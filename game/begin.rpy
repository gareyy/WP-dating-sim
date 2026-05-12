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

label start:

    python:
        loop_no = 0
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
        good_museum = False
        good_lake = False
        good_spa = False
        good_pool = False
        good_arcade = False
        good_karaoke = False

    default preferences.volume.music = 0.5

    jump prologue
