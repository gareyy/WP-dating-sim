# set of badendings and stage choices
label generalbadend:
    basil "It can't end like this."
    basil "It shouldn't."

    python:
        loop_no = loop_no + 1

    jump loophead

label badend_a:

    scene bg black with fade

    basil "It all fizzled out in the end..."
    basil "Shortly after, she left me alone."
    basil "The day after at work was a little awkward, we barely talked."
    basil "We really only talked about work stuff in our conversations."
    basil "I didn't really get to know her better..."
    basil "We remained as friends somewhat, but I never got the chance to tell her how I felt about her."
    basil "Over time, we drifted apart, and eventually lost contact with each other."
    basil "My heart started to beat less for love..."

    ""
    jump generalbadend


label choice1:
    basil "(Where should we go next?)"
    python:
        stage1locations = ["pool", "lake", "museum", "hartley"]

        if not seen_choice1:
            choices = ["pool", "lake", "museum"]
        else:
            choices = random.sample(stage1locations, 3)

        seen_choice1 = True

    menu:
        "Where should we go?"

        "The Pool" if "pool" in choices:
            dafny "Ooh, I love going to the pool! That sounds like so much fun!"
            jump pool
        "The Lake" if "lake" in choices:
            dafny "The lake sounds like a nice place to spend time!"
            jump lake
        "The Museum" if "museum" in choices:
            dafny "I love visiting museums! That sounds like a great idea!"
            jump museum
        "Hartley Teakle" if "hartley" in choices:
            dafny "Ew, that place looks really creepy and scary. I don't think I want to go there..."
            jump badend_a
    return

label choice2:
    basil "(Where should we go next?)"
    python:
        import random
        stage2locations = ["spa", "casino", "arcade", "karaoke"]

        if not seen_choice2:
            choices = ["spa", "arcade", "karaoke"]
        else:
            choices = random.sample(stage2locations, 3)
        
        seen_choice2 = True
    
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
            dafny "Hmm, neither of us like gambling, or have any money to gamble with."
            dafny "I think I might just stay home instead..."
            jump badend_a
    return
