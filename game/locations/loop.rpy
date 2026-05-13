# pooo
image red = Image("images/verification/barfadeRed.png")
image green = Image("images/verification/barfadeGreen.png")

transform barspotoffscreen:
    xalign 0.033
    yalign 5.0

transform barspot:
    xalign 0.033

define moveintopslow = MoveTransition(1.0, enter=barspotoffscreen)

# set of badendings and stage choices
label generalbadend:
    hide screen lemmabutton
    show verifying
    stop music fadeout 3.0
    ""
    show red at barspot
    with moveintopslow
    if loop_no >= 5 and renpy.random.randint(1, 100) == 99:
        "ensures false"
    elif loop_no % 3 == 0:
        basil "It can't end like this."
        basil "It shouldn't."
    elif loop_no % 3 == 1:
        basil "No! This isn't how it ends!"
    elif loop_no % 3 == 1:
        basil "No! This isn't how it ends!"
    else:
        basil "It can't end like this."
        basil "I refuse to accept this."

    play sound "sfx/loopreset.ogg"

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


