# Choice:
# Dafny compliments you and you have to select the right response
# (multi-stage response) (thank you/(compliment them back)/”i know 🫦”)
# Information: (Before choice)
# Dafny says they want to get closer in a hot tub some time soon (Spa)
# Bad Ending: Dafny has clearly shown some skin for Basil but the lack of compliment indicates that Basil isn’t into them.


label pool:

    scene bg pool
    with fade

    show dafny

    dafny "A chance to get wet together! I love swimming and relaxing in the pool."

    dafny "I hope we can go swimming together sometime soon, maybe even in a hot tub!"

    dafny "That would be so nice and intimate, don't you think?"

    basil "Yeah, that sounds really nice."

    python:
        spa_info = True
    
    basil "Now, let's go change into our swimwear and have some fun in the pool!"

    show dafny swimwear at left
    show basil swimwear at right
    with whitefade

    dafny "Your outfit looks great on you!"

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

        "Tofu" if pool_info:
            call .good_choice

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
