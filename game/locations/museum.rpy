
# Museum location and events
# Gives Lake info
# Info comes from karaoke

image artifact enter = Image("images/artifacts/wpp.png")
image artifact left = Image("images/artifacts/ligature.png")
image artifact middle = Image("images/artifacts/crab.png")
image artifact right = Image("images/artifacts/foxgirl.png")

label museum:

    scene bg museum
    with fade
    queue music "main/vara.ogg"

    show dafny

    dafny "I always wanted to come here! I'm so glad you brought me here!"

    dafny "I love art and history, and this place has so many cool exhibits to check out!"
    dafny "Oooh look at those ones over there! They look so interesting!"
    basil "Oh yeah, that one is Odin."
    dafny "Haha I just liked it because it had ravens on it."
    basil "Oh, do you like black birds?"
    call add_lemma("Dafny's favourite animal is a raven")
    $ lake_info = True
    dafny "Only {b}ravens{\b} really. They are epic and wise."

    hide dafny
    show artifact enter at truecenter 
    "As you enter the art gallery, your eyes are drawn to a large yellow canvas emblaisoned with the words:"
    "\"This program was verified by real weakest precondition patriots\""
    hide artifact enter

    show dafny
    dafny "Look at these ones over here!"
    hide dafny
    "Before you are three glorious works of art."
    # Alt-Ergo
    show artifact left at truecenter
    "On the left is a ligature of an 'a' and an 'e' between two double-struck horizontal lines."
    # C++
    hide artifact left
    show artifact middle at truecenter
    "In the middle is an abstract representation of a crab claw on a blue hexagon pinching the concat operation."
    hide artifact middle
    show artifact right at truecenter
    "On the right is an oil painting of fox girl, looking gorgeous and regal."
    hide artifact right

    show dafny
    dafny "Which one do you like the most?"
    play sound "sfx/choice.ogg"
    
    menu:
        "The one on the left":
            call .first_choice from _call_museum_first_choice

        "The one in the middle":
            call .second_choice from _call_museum_second_choice

        "The one on the right":
            call .third_choice from _call_museum_third_choice
        
        "The one by the entrance" if museum_info:
            call .good_choice from _call_museum_good_choice
    
    jump choice2

label .first_choice:
    show dafny sad
    dafny "Oh, I don't really like that one..."
    dafny "It's just kind of bland."
    basil "What about the ligature?"
    basil "That looks cool!"
    dafny "..."

    jump .museum_badend

label .second_choice:
    show dafny sad
    dafny "Umm, I'm not sure how I feel about that one..."
    basil "How so?"
    dafny "Something about just feels very undefined."
    dafny "It makes me feel unsafe."

    jump .museum_badend

label .third_choice:
    dafny "Hmm, that's a bit much..."
    basil "What do you mean!?"
    basil "You can see every brush stroke the artist made!"
    basil "And oil painting is the objectively best medium!"
    dafny "Sure..."
    jump .museum_badend

label .good_choice:
    dafny "I know it's so cool!"
    dafny "Yellow, bold, unafraid of speaking truth to power!"
    dafny "You have good taste."
    basil "Thank you!"
    $ good_museum = True
    return

label .museum_badend:
    jump badend_a
