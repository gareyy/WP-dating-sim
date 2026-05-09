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
    basil "(Wow she is so hot.)"
    show basil swimwear blushing
    dafny "You okay?"
    basil "..."
    basil "(I gotta say something!)"

    menu:
        "Thanks!":
            basil "Thanks!"

        "I know 🫦":
            basil "I know 🫦"
            dafny "Um, okay..."
            basil "..."
            dafny "..."
            call .pool_badend_A

    # BUNCH OF BS OR WHATEVER
    dafny "Aww you love my compliments!"
    basil "Th-thank you..."
    dafny "Do you want to hop in the water now?"
    show basil swimwear at right
    basil "Oh right!"
    basil "Lets hop in!"
    "SPLASH!"
    "The two hopped in the pool."
    basil "Wahooo!"
    dafny "Yippee!"
    show basil swimwear happy
    show dafny swimwear happy
    dafny "Hahaha!"
    basil "Hah, this is great..."
    dafny "I'm glad you picked this place."
    dafny "But still, I feel like a hot tub would be better."
    show dafny swimwear blushing
    dafny "..."
    basil "(I should say something.)"
    
    menu:
        "Your one piece also looks great!":
            call .first_choice

        "Your hair looks really nice!":
            call .second_choice
        
        "(Just keep staring.)" if pool_info:
            call .good_choice


label .first_choice:
    dafny "Oh, thanks..."
    jump pool_badend_B

label .second_choice:
    dafny "Oh, thanks..."
    jump pool_badend_B

label .good_choice:
    basil "(Yeah my eyes are completely frozen on her.)"
    show basil swimsuit lovestruck
    basil "..."
    basil "...."
    basil "....."
    dafny "You staring at me?"
    basil "..."
    "Basil dips their head into the water out of embarassment."
    hide basil swimsuit
    basil "(AHHH!)"
    basil "(Wow I am really in the thick of it now.)"
    dafny "You okay?"
    # TODO possibly change the positioning of basil?
    show basil swimsuit blushing
    basil "Yeah yeah I am."
    dafny "Were you staring at me?"
    dafny "You know what, forget about that, you look cute when you're flustered."
    basil "!!!!"
    dafny "Its all fine, I hope something isn't bothering you."
    basil "Okay, alright alright."
    dafny "You know what? Lets go swim for a few laps."
    show basil swimsuit
    hide dafny swimuit
    "Dafny drops into the water and starts swimming."
    basil "(I gotta admit, I don't swim that much.)"
    basil "(I'll just wade around.)"
    show bg black with fade

    scene bg pool
    with fade
    show dafny at left
    show basil at right
    dafny "Oh that was so fun!"
    basil "Yeah."
    basil "I don't think I've been to the pool since childhood."
    dafny "Ah, thats fine."
    dafny "Two computer scientists going to a body of water? What a rarity these days!"
    basil "Ha."
    dafny "You know what? I don't want this night to end, where should we go to?"
    jump choice2

label .pool_banend_B:
    dafny "Do you really mean that?"
    jump badend_a

label .pool_badend_A:
    # barely dipped toes in water
    dafny "Let's just dip our toes in the water."
    scene bg pool with fade # to show passage of time
    show dafny swimwear at left
    show basil swimwear at right
    basil "(We have literally done nothing but only dip our toes in the water.)"
    basil "(She hasn't said a single word since, for 10 minutes.)"
    dafny "I think we're done here..."
    hide dafny
    "Dafny leaves the water to go change."
    basil "..."
    basil "Damn."
    basil "(I sat in the water for another hour, just over thinking what happened there.)"
    jump badend_a

