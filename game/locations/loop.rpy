# set of badendings and stage choices
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

    basil "It can't end like this."
    basil "It shouldn't."

    python:
        loop_no = loop_no + 1

    jump loophead
