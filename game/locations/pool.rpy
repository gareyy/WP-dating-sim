# Choice:
# Dafny compliments you and you have to select the right response
# (multi-stage response) (thank you/(compliment them back)/”i know 🫦”)
# Information: (Before choice)
# Dafny says they want to get closer in a hot tub some time soon (Spa)
# Bad Ending: Dafny has clearly shown some skin for Basil but the lack of compliment indicates that Basil isn’t into them.

# basil has rashie and shorts
# dafny has one piece

label pool:

    scene bg pool
    with fade

    show dafny at left
    show basil at right
    dafny "I did not even know they sold togs around here, isn't that awesome?"
    show basil blushing
    basil "Y-yeah."
    dafny "Perfect! I would love to see you in your swimmers soon..."
    basil "..."
    basil "(My mind just shortcircuited.)"
    dafny "Ooh! Maybe in the future, we can go swimming together again sometime soon, maybe even in a {b}hot tub!{\b}"
    python:
        spa_info = True

    dafny "That would be so nice and intimate, don't you think?"

    basil "Y-yeah.."
    basil "Alright, uhh, yeah."
    dafny "Yep! See you after changing."

    "The two go to different change stalls to change..."

    scene bg pool with fade

    show dafny swimwear at left
    show basil swimwear at right
    with whitefade

    dafny "Hey hey!"
    basil "Y-yeah.."
    dafny "Your swimmies looks great on you!"
    basil "(Wow she is so hot)"

    menu:
        "Thanks!":
            basil "Thanks!"

        "I know 🫦":
            basil "I know 🫦"
            dafny "Uh okay..."
            call .pool_badend

    
    menu:
        "Your outfit also looks great!":
            call .first_choice

        "Your hair looks really nice!":
            call .second_choice
        
        # THAT BODY OF YOURS IS ABSURD
        "" if pool_info:
            call .good_choice



    jump choice2

label .first_choice:
    dafny "Oh, thanks..."
    jump pool_badend

label .second_choice:
    dafny "Oh, thanks..."
    jump pool_badend

label .good_choice:
    dafny "Aw, thank you!"
    return

label .pool_badend:
    jump badend_a
