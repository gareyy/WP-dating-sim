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


label choice2:
    basil "(Where should we go next?)"
    $ stage1locations = ["spa", "casino", "arcade", "karaoke"]
    $ import random
    $ choices = random.sample(stage1locations, 2)
    menu:
        "Where should we go?"

        "Karaoke" if "karaoke" in choices:
            ""
        "The Casino" if "casino" in choices:
            ""
        "The Spa" if "spa" in choices:
            ""
        "The Arcade" if "arcade" in choices:
            ""
    return
