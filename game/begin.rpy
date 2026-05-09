# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define basil = Character("Basil", color="#c8ffc8")
define dafny = Character("Dafny", color="#ffffc8")
define isabelle = Character("Isabelle", color="#715bff")

image bg black = "#000"
image bg lab = Image("images/backgrounds/lab_resized.png")
image bg restaurant = Image("images/backgrounds/restaurant.png")
image bg museum = Image("images/backgrounds/museum.png")
image bg pool = Image("images/backgrounds/pool_resized.png")
image bg alleyway = Image("images/backgrounds/alleyway.png")
image bg karaoke = Image("images/backgrounds/karaoke_bg.png")
image bg spa = Image("images/backgrounds/spa.png")
image bg arcade = Image("images/backgrounds/arcade.png")
image bg uqlakes = Image("images/backgrounds/lake.png")

image verifying:
    "images/backgrounds/verify.png"
    0.35 # Wait for 0.5 seconds
    "images/backgrounds/verify2.png"
    0.35 # Wait for 0.5 seconds
    repeat # Loop forever

# oversample = 6 if TODO sprite
image basil = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=3))
image basil happy = Crop((0, 0, 925, 925), Image("images/basil/Happy.png", oversample=3))
image basil laughing = Crop((0, 0, 925, 925), Image("images/basil/Laughing.png", oversample=3))
image basil normal = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=3))
image basil surprised    = Crop((0, 0, 925, 925), Image("images/basil/Surprise.png", oversample=3))
image basil thinking = Crop((0, 0, 925, 925), Image("images/basil/Thinking.png", oversample=3))

image basil blushing = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=6))
image basil angry = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=6))
image basil sad = Crop((0, 0, 925, 925), Image("images/basil/Surprise.png", oversample=6))
image basil swimwear = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=6))
image basil swimwear blushing = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=6))
image basil swimwear happy = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=6))
image basil swimwear lovestruck = Crop((0, 0, 925, 925), Image("images/basil/Normal.png", oversample=6))

image dafny = Crop((0, 0, 925, 925), Image("images/dafny/Neutral.png", oversample=3))
image dafny happy = Crop((0, 0, 925, 925), Image("images/dafny/Happy 2.png", oversample=3))
image dafny blushing = Crop((0, 0, 925, 925), Image("images/dafny/Flustered.png", oversample=3))
image dafny excited = Crop((0, 0, 925, 925), Image("images/dafny/Flustered_Excited.png", oversample=3))
image dafny lovestruck = Crop((0, 0, 925, 925), Image("images/dafny/Flustered_Excited.png", oversample=3))
image dafny sad = Crop((0, 0, 925, 925), Image("images/dafny/Disappointed.png", oversample=3))
image dafny laughing = Crop((0, 0, 925, 925), Image("images/dafny/Flustered_Excited.png", oversample=3))

image dafny surprised = Crop((0, 0, 925, 925), Image("images/dafny/Flustered.png", oversample=6))
image dafny angry = Crop((0, 0, 925, 925), Image("images/dafny/Neutral.png", oversample=6))
image dafny scared = Crop((0, 0, 925, 925), Image("images/dafny/Neutral.png", oversample=6))
image dafny swimwear = Crop((0, 0, 925, 925), Image("images/dafny/Neutral.png", oversample=6))
image dafny swimwear angry = Crop((0, 0, 925, 925), Image("images/dafny/Neutral.png", oversample=6))
image dafny swimwear happy = Crop((0, 0, 925, 925), Image("images/dafny/Neutral.png", oversample=6))
image dafny swimwear blushing = Crop((0, 0, 925, 925), Image("images/dafny/Neutral.png", oversample=6))


define whitefade = Fade(1.0, 1.0, 0.5, color='#fff')

transform left:
    xalign 0.25
    yalign 1.0

transform right:
    xalign 0.75
    yalign 1.0

# The game starts here.

label start:

    python:
        import random

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

    default preferences.volume.music = 0.5

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # can end the game at any time with "return"
    
    basil "Do you ever think about what would have happened if you knew one thing beforehand, or knew how to react in the right way?"
    basil "Sometimes I think about what would have been the right thing to say, or the right thing to do."
    basil "..."
    basil "Theres this girl where I work at... She is the prettiest thing in the world."
    show dafny
    basil "She's the main reason why i'm still doing this program verification stuff."
    basil "I feel like I could reach new heights with her."
    basil "I can show her the world and she can show me the stars."
    basil "I feel like she is a piece of me that I am missing and need filled."
    basil "Its a precondition for me to be with her if I want my life to feel full."
    basil "But you know what? She is just a coworker."
    hide dafny 
    basil "I don't know if she loves me. And I am too scared to find out."
    basil "I fear that if I confess, it may jeopardise my professional relationship with her."
    basil "And maybe my own happiness..."
    basil "A million fish in the sea and I will release them back into the oceans if they are not her.."
    basil "Oh heavens above! May you help me in my quest!"
    basil "I would do anything! Even if it meant living the same day over and over again until I get it right!"

    show bg lab with fade
    queue music "main/vara.ogg" volume 0.5 fadein 5.0
    
    show basil at right
    basil "Nice! all my work for today is done!"
    basil "I finally implemented that big stupid compoment that was bogging me and Dafny."
    show dafny at left
    basil "Hey Dafny! I finally got that stupid thing implemented!"
    dafny "Yeah, uh, which one?"
    basil "You know, the one I made a PR for in the repository."
    dafny "Gimme 2 seconds..."
    dafny "The indirect call resolution stuff?"
    basil "Yeah that one."
    dafny "Well congratulations buddy!"
    dafny "You want a reward for that?"
    show basil blushing
    basil "Y-yeah..."
    dafny "You know, you've been getting better at this stuff."
    basil "hahah okay..."
    basil "What did you get done today?"
    dafny "I've been doing some optimisations,"
    dafny "-mostly on your code."
    show basil
    basil "Wait wh-"
    dafny "Well when I said you were improving, I can definitely advocate for it."
    basil "Oh really?"
    dafny "Good little puppy."
    show basil blushing
    basil "Wh- wh-"
    show dafny laughing
    dafny "Pffftt- hahahhaha"
    show basil
    basil "Toying with me is your favourite thing huh?"

    show basil
    show dafny
    basil "Oh shit, did we remember to have some lunch?"
    "Dafny looks around with an unsure face"
    dafny "Yeah uh, fuck."
    dafny "I think we forgot."
    dafny "You know what? How about we go out for dinner together?"
    dafny "Just a little reward for how far you've gone."
    "Basil gives it some thought."
    basil "I think it would be cheaper if I ate with you today."
    basil "Are you covering me?"
    show dafny blushing
    dafny "Can you pay for me please?"
    basil "You sure you want me to pay?"
    dafny "Y-yeah?"
    basil "Pfft."
    dafny "Is a compliment to you not enough?"
    dafny "You like my compliments right?"
    basil "I somewhat live off them."
    dafny "Great! I take that as you paying for my meal?"
    basil "Only if I get to choose."
    dafny "Fine then, your pick."
    dafny "I hope you pick something good."
    dafny "Anyway, where should we go to to eat?"
    basil "Eughhhh...."
    show basil thinking
    basil "Someplace cheap I hop-"
    dafny "The fancy place at the uni here!"
    basil "Oh you mean the pub? I hear they have great student discou-"
    dafny "Oh no I mean the really fancy one."
    show basil angry
    basil "Ah."
    dafny "Oh, I still have a small bit to do, mind if you go ahead to the place without me?"
    basil "Yeah sure."

    jump loophead
