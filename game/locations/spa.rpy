# Story - Spa:
# Choice: Dafny says they want to do something physical (implied to be a bit intimate).
#  Dafny wants to do the hot and steamy hot tub.
#  The other choices result in death
# Information: (After choice) when doing the something physical Dafny whispers
#  some sweet nothings into Basil’s ear, and directly says they would like Basil say to them
#  “THE CORRECT CHOICE FOR POOL” (Pool) 
# Bad Ending: Hypothermia, accidentally neck snapped by Dafny during massage
# Monadic Mind

define rocq = Character("Rocq", color="#ffb68c")

label spa:

    scene bg spa
    with fade

    show dafny at left
    show basil at right
    
    dafny "Oh, this place is so nice and relaxing! I love it here!"
    dafny "I can't wait to spend some time here with you!"

    rocq "Welcome to the Monadic Mind Spa and Wellness Center!"
    rocq "We have a variety of services available, including massages, cold plunges, and hot tubs!"

label .spa_menu:

    rocq "Which one would you like to try out today?"

    menu:
        
        "Massage":
            call .massage

        "Cold Plunge":
            call .cold_plunge

        "Hot Tub" if spa_info:
            jump .hot_tub

    jump ending

label .massage:
    # Rocq says the usual massage isn't available and gives the option of a "special massage" that is more intimate and physical.
    dafny "Ooh, I would love to get a massage! That sounds so nice and relaxing!"
    rocq "Great! We have a variety of massages available, including Swedish, deep tissue, and our special massage!"
    dafny "Ooh, the special massage sounds so intriguing! I want to try that one!"
    rocq "Oh, the usual massage therapist isn't uhh, isn't available right now, but I can do it myself."
    rocq "Though I warn you, it's a bit more physical and intimate than our usual massages, and I can't guarantee that it will be a pleasant experience for everyone..."
    menu:
        "Go through with the special massage":
            dafny "I think I would like to go through with the special massage!"

        "Don't do the special massage":
            dafny "I think I might just pass on the special massage for now..."
            rocq "Oh, that's too bad! Maybe next time!"
            jump .spa_menu

    # Dafny hurts their neck during the massage and has to be rushed to the emergency room.
    jump .massage_badend

label .cold_plunge:
    # Dafny says they want to do the cold plunge, but they aren't prepared for how cold it is and end up getting hypothermia.

    dafny "Wow, that was colder than I expected! I think I might have gotten hypothermia..."
    jump .spa_badend

label .hot_tub:
    # Dafny and Basil have an intimate time in the hot tub
    # Until Rocq interrupts them and tells them that they have to leave because the spa is closing.
    return

label .spa_badend:
    jump badend_a

label .massage_badend:
    # Dafny's wrist is broken and they have to be rushed to the emergency room.

    dafny "Ouch my neck! What the hell did you do to me?!"

    jump generalbadend