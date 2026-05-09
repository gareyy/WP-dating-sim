# Story - UQ Lakes: 
# Choice: Which animal/thing to look at and see and talk about.
# Information: (Before choice) You two are listening to music together on the walk, they put on their favourite song (Karaoke)
# Animals: Raven, Ibis, Pukeko, Water Dragon, Possum (3 neutral, 1 ideal, 1 bad (on second run))
# Animals should be the only voice acted characters and use real images.
# Bad ending: Animal can steal your girl

# Dafny’s favourite song, duet, some romantic song about loving and missing each other

define possum = Character("Possum")
define pukeko = Character("Pukeko")
define ibis = Character("Ibis")
define dragon = Character("Water Dragon") # kinda looks like a dragon???
define raven = Character("Raven")

label uqlakes:

    scene bg uqlakes
    show dafny at left
    show basil at right
    with fade

    # Walking to the lakes
    dafny "This is such a nice place to go for a walk together!"
    dafny "So serene, so peaceful."
    basil "Yeah, I love coming here. It's so peaceful and beautiful."
    basil "I like the sounds of the birds and the fountain."
    dafny "Yeah.."
    dafny "But when im walking through nature, I do prefer to listen to my own music."
    basil "Ooh! What kind of songs?"
    dafny "I have this favourite one, wanna listen?"
    basil "Oh! Yes sure!"
    "Dafny offers an earbud to Basil, and they put it in."
    "Dafny then pushes play on her phone..."
    play music "audio/duet.ogg"

    ""
    show dafny happy
    show basil happy
    dafny "I hope you like it! It's a really {b}romantic song{\b} that I think is perfect for a walk by the lake."
    basil "I love it!"
    basil "(Wait, romantic song?)"
    basil "(Is this really a date now?)"

    python:
        karaoke_info = True

    dafny "It's really nice to have such a beautiful place to relax so close to our workplace!"
    basil "Yeah, its beautiful out here. I love the green out here."
    dafny "Not as serene as you beautiful"
    show basil blushing
    basil "Wh-"
    dafny "Ppffft I'm just joking buddy."
    show basil at right
    basil ".... ok ok"
    basil "..."
    basil "Ummm.."
    basil "Look at those animals over there! They look so cute and peaceful."
    dafny "I want to get close to one of them!"
    basil "Oh, which one?"
    dafny "Which one look the most interesting to you Basil?"

    if not lake_info:
        menu:
            "Ibis":
                call .ibis_choice

            "Water Dragon":
                call .water_dragon_choice
            
            "Possum":
                call .possum_choice
    
    else:
        menu:
            "Raven":
                call .raven_choice

            "Possum":
                call .possum_choice
            
            "Pukeko":
                call .pukeko_choice

    
    jump choice2

label .ibis_choice:
    basil "Oh look! an ibis!"
    dafny "Those are quite ordinary birds, but they are pretty cute..."
    jump .uqlakes_badend

label .water_dragon_choice:
    basil "Oh look! A water dragon!"
    dafny "They are pretty cool, but they are a bit scary..."
    jump .uqlakes_badend

label .possum_choice:
    basil "Oh look! A possum!"
    dafny "Oh, I sort of like those ones, but they are a bit scary..."
    jump .uqlakes_badend

label .pukeko_choice:
    basil "Oh look! A pukeko!"
    dafny "A pukeko! Those are interesting!"
    dafny "You know the \"DAMNNN\" meme with that fucked up little pukeko with one leg?"
    basil "Yeah?"
    dafny "Yeah that stuff still makes me laugh."
    "You two approach the pukeko"
    dafny "Oh hey little pukeko!"
    hide basil
    show pukeko at right
    pukeko "Oh hey baby girl."
    show dafny blushing
    dafny "Who, me?"
    pukeko "Yes you, fine little thing."
    basil "(Oh fuck.)"
    basil "Hey uh, pukeko, you talk?"
    pukeko "Oh yes I do beautiful."
    pukeko "You two on a date?"
    basil "Oh um-"
    show dafny surprised
    dafny "Oh uhhh"
    pukeko "I take that as a no beautiful?"
    dafny "I don't think we are."
    basil "(Ruh roh...)"
    basil "I think we did just eat at a fancy restaurant tho."
    "The pukeko looks at Dafny"
    show dafny blushing
    pukeko "What's your name honeypumps?"
    dafny "Um, Dafny."
    "She twiddles with her hair, pulling it back to show her ear."
    basil "Oh and my name is Basil."
    pukeko "Ah, nice to meet you two."
    pukeko "But especially you more,"
    pukeko "Dafny"
    "The pukeko says her name in a way that sounds like the most beautiful music to Dafny's ears"
    show dafny lovestruck
    dafny "W- wow..."
    dafny "Basil, I think I love this pukeko..."
    basil "Are you kidding me???"
    pukeko "I can show you the world, babygirl."
    dafny "I am convinced."
    dafny "You know what little pukeko? I love you."
    dafny "Can we go out today?"
    pukeko "Oh absolutely yes! That was what I was thinking!"
    dafny "Oh we think the same, its like fate!"
    hide pukeko
    show basil sad at right
    dafny "Well Basil, sorry for the abrupt end, but see you tomorrow?"
    basil "Yeah I gues..."

    scene bg black with fade
    basil "I got Dafny stolen by a bird???"
    basil "Grr- AHH!!!"
    basil "And now, fast forward a few years later, Dafny asked me to be the officiant at their wedding."
    basil "The night after the wedding, I cried and cried at how the eye of my apple got stolen by a bird!"
    basil "A BIRD!!"
    basil "I do admit, that pukeko does have some \'w rizz\'."

    jump generalbadend

label .uqlakes_badend:
    "Dafny and Basil walk away from what they were looking at"
    jump badend_a

label .raven_choice:
    basil "Oh look! A sick ass raven!"
    dafny "Wow that is a sick ass raven! I love ravens, they are so epic and wise!"
    hide basil
    show raven at right
    raven "Hello."
    raven "What are your names you two?"
    dafny "Dafny"
    basil "Basil"
    raven "I see..."
    raven "You say I am wise?"
    dafny "Oh yes! I do."
    raven "The wisest do not say they are wise, but they have others prove it."
    dafny "So you're saying you're wise?"
    raven "..."
    basil "You got any wise sayings or whatever it is?"
    basil "That stuff Sun Tzu says?"
    raven "That guy is a warlord, I am a bird of peace."
    raven "I am also hungry."
    dafny "Ooh I got something!"
    dafny "I got the entree from the restaurant!"
    basil "Oh yeah!"
    "Dafny and Basil split the food, and give it to the raven."
    "The raven chews it up and spits it out in a wise way."
    raven "Yummers."
    raven "For your offering of the physical world, I shall return to you some knowledge of the spiritual world."
    "The raven looks introspective."
    raven "Oh, I am starting to see."
    raven "..."
    raven "You two are two halves that need to come together at some part in the world."
    raven "Thats when you will achieve true happiness."
    show dafny blushing
    dafny "Woah."
    basil "W-"
    raven "I see a long life of love and happiness."
    dafny "..."
    basil "..."
    raven "Oh I just realised what I said was a prediction, not knowledge of the spiritual world."
    raven "I'm sorry about that."
    "Dafny and Basil are blushing purple."
    dafny "..."
    basil "..."
    basil "(Woah.)"
    raven "But uh yeah, thats it."
    raven "Thank you for your time, Dafny and Basil."
    "The raven flies away."

    hide raven
    show basil blushing at right

    dafny "..."
    basil "..."
    basil "(This really is a date, huh?)"
    dafny "..."
    dafny "Y-you, um, want to go anywhere else?"
    basil "Oh- yeah, of course."

    basil "(This could get more intense now.)"

    jump choice2
