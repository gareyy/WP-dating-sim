
# Museum location and events
# Gives Lake info
# Info comes from karaoke

label museum:

    scene bg museum
    with fade
    queue music "audio/main/vara.ogg"

    show dafny

    dafny "I always wanted to come here! I'm so glad you brought me here!"

    dafny "I love art and history, and this place has so many cool exhibits to check out!"
    dafny "Oooh look at those ones over there! They look so interesting!"
    basil "Oh yeah, that one is Odin."
    dafny "Haha I just liked it because it had ravens on it :3"
    basil "Oh, do you like black birds?"
    dafny "Only ravens really. They are epic and wise."

    python:
        lake_info = True

    dafny "Look at these ones over here!"

    dafny "Which one do you like the most?"

    if not museum_info:
        menu:
            "The one on the left":
                call .first_choice

            "The one in the middle":
                call .second_choice

            "The one on the right":
                call .third_choice

    menu:
        "The one on the left":
            call .second_choice

        "The one in the middle":
            call .third_choice

        "Tofu":
            call .good_choice


    
    jump choice2

label .first_choice:
    dafny "Oh, I don't really like that one..."
    jump museum_badend

label .second_choice:
    dafny "Umm, I don't really like that one..."
    jump museum_badend

label .third_choice:
    dafny "Hmm, that's a bit much..."
    jump .museum_badend

label .good_choice:
    dafny "Oh, this looks great! Thank you!"
    return

label .museum_badend:
    jump badend_a