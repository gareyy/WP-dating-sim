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
image rocq = Image("images/side_characters/rocq.png")

transform threeleft:
    xalign 0.10
    yalign 1.0

transform threeright:
    xalign 0.9
    yalign 1.0

transform threemid:
    xalign 0.5
    yalign 1.0

transform closeleft:
    xalign 0.4
    yalign 1.0
transform closeright:
    xalign 0.6
    yalign 1.0

label spa:

    scene bg spa
    with fade
    show dafny at left
    show basil at right

    dafny "Cmon! Lets enjoy the spa together!"
    dafny "Oh, this place is so nice and relaxing! I love it here!"
    dafny "I like how you chose this place!"

    rocq "Welcome to the Monadic Mind Spa and Wellness Center!"
    rocq "We have a variety of services available, including massages, cold plunges, and hot tubs!"

    hide dafny
    show rocq at left

    basil "Hey I know you!"
    rocq "Me?"
    basil "You're Coq, right?"
    rocq "Me? No."
    basil "I swear when I always come here, its Coq that is working here."
    rocq "Yeah, um, how do I say this."
    rocq "Actually, I don't think I should be stating anything, its private."

label .spa_menu:

    hide basil
    hide rocq
    show rocq
    rocq "Um anyway..."
    rocq "Which one would you like to try out today?"

    play sound "sfx/choice.ogg"
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
            basil "I agree with the special massage."
            dafny "I think I would like to go through with the special massage!"

        "Don't do the special massage":
            dafny "I think I might just pass on the special massage for now..."
            basil "Umm, me too."
            rocq "Oh, that's too bad! Maybe next time!"
            jump .spa_menu

    # Dafny hurts their neck during the massage and has to be rushed to the emergency room.
    jump .massage_badend

label .cold_plunge:
    # Dafny says they want to do the cold plunge, but they aren't prepared for how cold it is and end up getting hypothermia.
    # TODO: dafny says they want basil to stare at their body lovingly.
    basil "We can do the cold plunge."
    dafny "Yes please!"
    scene bg black with fade
    scene bg spa
    with fade
    show dafny swimwear at left
    show basil swimwear at right
    dafny "You know, I have never done a cold plunge before!"
    "Dafny and Basil walk into the cold plunge pool."
    dafny "Oooh! Brrr!"
    basil "Yeeesh!"
    "They both settle down in the tub."
    dafny "Wo- wow, c-c-c-cold..."
    dafny "Can I hug you for some w-warmth?"
    show basil swimwear blushing
    basil "Sure..."
    dafny "Th-th thanks..."
    # TODO: add some transition thing that moves them closer?
    show dafny swimwear at closeleft with move
    show basil swimwear at closeright with move

    dafny "You kn-kn-know, we are pretty close now..."
    dafny "I ha-ha-have to con-confess, {b}I like it when you stare at me{\b} like a deer in the he-he-headlights."
    $ pool_info = True
    $ lemmas_list.add("Dafny is attracted to Basil's stare")
    dafny "Especially in a swimsuit like this..."
    basil "..."
    basil "Y- ha, ha."
    basil "Yeah..."
    dafny "You know Basil, you are pretty cu-cu-"
    "Dafny collapses into the water"
    hide dafny
    basil "Oh shit!"
    "Basil rushes out of the cold water and tries to drag Dafny's body out."
    basil "Rocq! Please help!"

    show bg black with fade
    basil "Unfortunately, Dafny succumbed to hypothermia."
    basil "I felt completely alone and guilty after that, I believed I killed her..."

    jump generalbadend

label .spa_badend:
    jump badend_a

label .massage_badend:
    # Dafny's wrist is broken and they have to be rushed to the emergency room.
    scene spa with fade
    rocq "Alright, the special massage is a couple's massage!"
    show dafny blushing at left
    show basil blushing at right
    dafny "..."
    basil "..."
    rocq "Basil, I feel like a couple's massage would be perfect for you two!"
    basil "This is the kind of thing you normally do only in towels, right?"
    basil "Um, can we get swimsuits only?"
    rocq "If that's fine by you..."

    scene bg black with fade
    scene bg spa
    with fade
    show dafny swimwear at threeleft
    show basil swimwear at threemid

    basil "..."
    basil "...."
    basil "....."
    dafny "..."
    dafny "{b}I like it when you stare{\b}, you know?"
    $ pool_info = True
    $ lemmas_list.add("Dafny is attracted to Basil's stare")
    basil "Oh, um, I wasn't staring."
    dafny "Hmph, yeah right."

    show rocq at threeright
    rocq "Okay first, we will have Dafny lie down on the massage table please."
    "Dafny lies on the table."
    hide dafny
    hide basil
    hide rocq
    show rocq at left
    show basil at right
    dafny "Time to get hands on Basil!"

    scene bg black with fade
    scene bg spa
    with fade
    show dafny swimwear angry at left
    show basil swimwear at right

    dafny "Ouch my neck! What the hell did you do to me?!"
    basil "!!!"
    rocq "Um sorry, I think you misheard me Basil."
    basil "Crap, crap, crap, I am so sorry!"
    rocq "Okay, hands off her."
    rocq "Miss are you okay?"
    hide basil
    show rocq at right
    dafny "Y- Owww."

    scene bg black with fade
    basil "I think she hated me after that incident."
    basil "She came back to work the next day and didn't talk to me for a whole week."
    basil "We never even had the chance to become friends."

    jump generalbadend

label .hot_tub:
    # Dafny and Basil have an intimate time in the hot tub
    # Until Rocq interrupts them and tells them that they have to leave because the spa is closing.
    basil "Um, hot tub please..."
    dafny "Oh yes! I've always wanted to do one of these!"
    dafny "Especially with you Basil."
    show basil blushing
    basil "!!!"
    "..."
    scene bg black with fade
    scene bg spa
    with fade
    show dafny swimwear at left
    show basil swimwear at right    

    dafny "..."
    dafny "What's with the look Basil?"
    basil "..."
    show basil swimwear blushing
    dafny "You stunlocked by my beautiful looks?"
    basil "!!!"
    dafny "Come on in the tub Basil."
    "Dafny and Basil walk into the tub and sit down."
    dafny "Look at us, two program verification researchers, in a hot tub together."
    dafny "Five feet apart, but are we gay?"
    basil "Um..."
    show dafny swimwear at closeleft with move
    dafny "Come closer Basil."
    dafny "I want to tell you something..."
    basil "(Holy cow I am going insane!)"
    basil "(Is my crush really gonna do this to me?)"
    basil "Um, okay.."
    show basil swimwear at closeright with move
    dafny "You seem a little shy, love~."
    basil "(She called me love???)"
    dafny "Two program verification researchers, in a hot tub, together."
    dafny "Mind if I pat your head love~?"
    basil "Uh uhm, yes please."
    dafny "Alright then."
    "Dafny takes Basil's head and begins to pat it"
    show dafny swimwear blushing
    "Dafny begins to whisper something in Basil's ear."
    dafny "You know, {b}I like it when you stare at me{\b} lovingly~..."
    $ pool_info = True
    $ lemmas_list.add("Dafny is attracted to Basil's stare")
    basil "L-lovingly?"
    dafny "I always notice you staring at me~."
    basil "aksljdhgfjhawqjhfajsh-"
    basil "Uh ummmm.."
    basil "Can we be like-like-"
    basil "Like this for a few moments?"
    dafny "Yea-"
    
    show basil swimwear at threeright with move
    show dafny swimwear at threemid with move

    show rocq at threeleft with fade

    rocq "Hey sorry!"
    rocq "We are closing up soon."
    rocq "You know, cleaning and such."
    basil "..."

    $ good_spa = True

    jump ending
