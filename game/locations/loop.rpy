image red = Image("images/backgrounds/barfadeRed.png")
image green = Image("images/backgrounds/barfadeGreen.png")

transform barspotoffscreen:
    xalign 0.033
    yalign 5.0

transform barspot:
    xalign 0.033

define moveintopslow = MoveTransition(1.0, enter=barspotoffscreen)

# set of badendings and stage choices
label generalbadend:
    show verifying
    stop music fadeout 3.0
    show red at barspot
    with moveintopslow
    basil "It can't end like this."
    basil "It shouldn't."

    play sound "sfx/loopreset.ogg"

    python:
        loop_no = loop_no + 1

    jump loophead


label badend_a:

    show verifying with fade
    stop music fadeout 5.0
    play sound "sfx/fail.ogg"

    hide screen lemmabutton
    hide screen lemmas

    basil "It all fizzled out in the end..."
    basil "Shortly after, she left me alone."
    basil "The day after at work was a little awkward, we barely talked."
    basil "We really only talked about work stuff in our conversations."
    basil "I didn't really get to know her better..."
    basil "We remained as friends somewhat, but I never got the chance to tell her how I felt about her."
    basil "Over time, we drifted apart, and eventually lost contact with each other."
    basil "My heart started to beat less for love..."

    "..."
    jump generalbadend


label goodend:
    show verifying
    # wait 0.5
    show green at barspot
    with moveintopslow
    # wait 2.0
    return

label choice1:
    basil "(Where should we go next?)"
    python:
        stage1locations = ["pool", "lake", "museum", "hartley"]

        if not seen_choice1:
            choices = ["pool", "lake", "museum"]
        else:
            choices = random.sample(stage1locations, 3)

        seen_choice1 = True

    play sound "sfx/choice.ogg"
    menu:
        "Where should we go?"

        "The Pool" if "pool" in choices:
            dafny "Ooh, I love going to the pool! That sounds like so much fun!"
            jump pool
        "The Lake" if "lake" in choices:
            dafny "The lake sounds like a nice place to spend time!"
            jump uqlakes
        "The Museum" if "museum" in choices:
            dafny "I love visiting museums! That sounds like a great idea!"
            jump museum
        "Hartley Teakle" if "hartley" in choices:
            dafny "Ew, that place looks really creepy and scary. I don't think I want to go there..."
            basil "You sure? Could be fun though!"
            jump hartley
    return

label choice2:
    basil "(Where should we go next?)"
    python:
        stage2locations = ["spa", "casino", "arcade", "karaoke"]

        if not seen_choice2:
            choices = ["spa", "arcade", "karaoke"]
        else:
            choices = random.sample(stage2locations, 3)
        
        seen_choice2 = True
    
    play sound "sfx/choice.ogg"
    menu:
        "Where should we go?"

        "The Karaoke" if "karaoke" in choices:
            dafny "Ooh, I love karaoke! That sounds like so much fun!"
            jump karaoke
        "The Spa" if "spa" in choices:
            dafny "A spa day sounds so relaxing and fun! I would love to go to the spa with you!"
            jump spa
        "The Arcade" if "arcade" in choices:
            dafny "Let's go to the arcade! I love playing games!"
            jump arcade
        "The Casino" if "casino" in choices:
            dafny "Hmm, neither of us like gambling, or have much money to gamble with."
            basil "This could be life-changing money."
            basil "Let's go."
            jump casino
    return
