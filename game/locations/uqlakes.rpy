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

    $ import random
    $ coinflip = random.choice([0, 1, 2])
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
            "Ibis" if coinflip == 0:
                call .ibis_choice

            "Water Dragon" if coinflip == 1:
                call .water_dragon_choice

            "Possum" if coinflip == 2:
                call .possum_choice
            
            "Raven":
                call .raven_choice

            
            "Pukeko":
                call .pukeko_choice

    
    jump choice2

label .ibis_choice:
    basil "Oh look! an ibis!"
    dafny "Those are quite ordinary birds, but they are pretty cute..."
    basil "They're also called bin chickens."
    "An ibis swoops in and lands in front of them, blocking their path."
    hide basil
    show ibis at right
    ibis "What did you just call me?"
    basil "Oh I am so sorry!"
    ibis "What did you call me???"
    show dafny scared
    basil "Please calm down."
    basil "My name is Basil and I am so truly sorry."
    ibis "Grr."
    dafny "You are not gonna do anything to my friend!"
    ibis "How would you feel if your friend called you a bin chicken?"
    show dafny happy
    dafny "I'd laugh at it."
    ibis "Go on Basil, call your friend a \"bin chicken\""
    basil "Um..."
    basil "Hey Dafny, you are a uh, um, bin chicken."
    dafny "Wow."
    dafny "I am so honoured..."
    ibis "..."
    ibis "You have a point Basil."
    ibis "But I am still offended by you."
    basil "What?"
    "The ibis flies away"
    hide ibis
    show basil at right
    basil "Wow. what a spoil sport of a bird."
    basil "I always see those things picking in bins anyway, thats why they are called bin chickens."
    ibis "Bombs away!"
    "Bird poop falls from the sky and lands on Basil."
    show basil pooped
    basil "..."
    dafny "..."
    show dafny laughing
    dafny "BAWHAHHAHAHAHAHAHHAHA!!!-"
    basil "Hey!"
    dafny "Oh my, everyone is gonna lose it when I tell them about this tomorrow."
    scene bg black with fade
    basil "After that, me and Dafny split ways."
    basil "The next day, Dafny told everyone about what happened."
    basil "All the in jokes at the lab are now about me being pooped on."
    basil "Still, I didn't end up with Dafny, probably for unrelated reasons I hope."
    basil "..."
    jump generalbadend

label .water_dragon_choice:
    basil "Oh look! A water dragon!"
    dafny "They are pretty cool, but they are a bit scary..."
    basil "Why are they called water dragons anyway?"
    dafny "Maybe because they look,"
    dafny "Like a dragon."
    show basil angry
    basil "..."
    basil "...."
    basil "....."
    dafny "You know, like the game?"
    show basil at right
    basil "Ok, alright, um."
    "They both stare intensly at the water dragon"
    hide basil
    show dragon at right
    dragon "..." # add dragon noise where elipsis is, just make something up hayden
    basil "Um, hello?"
    dragon "..."
    dafny "Hello little guy! My name is Dafny, and this is Basil."
    dragon "..."
    basil "Um? Do you talk little guy?"
    dragon "..."
    dafny "I've heard mystical things about the animals of this lake."
    dafny "Like they talk and give you wise advice."
    basil "Is that so?"
    dafny "Supposedly."
    dafny "Like if an animal from here started talking to me I wouldn't be surprised."
    dragon "..."
    basil "..."
    basil "I thought that thing was gonna talk."
    dafny "Anyway, I heard some of these animals could give you advice or fortune."
    dafny "Or possibly have impeccable charisma."
    basil "Really?"
    dafny "I haven't given much thought to it."
    dragon "..."
    hide dragon
    show basil at right

    jump .uqlakes_badend

label .possum_choice:
    basil "Oh look! A possum!"
    dafny "Oh, I sort of like those ones, but they are a bit scary..."

    hide basil 
    show possum at right
    possum "Oh hey you two!"
    basil "Oh, us?"
    possum "Yes you two!"
    show possum fork
    possum "Give me both of your wallets."
    possum "NOW!"
    show dafny scared
    basil "AAAH!"
    dafny "AAAH!"
    possum "NOW!"
    dafny "Please please please! We are both broke program verification researchers!"
    basil "I promise you, all my money is gone and I spent it on food!"
    possum "Is that so?"
    basil "Spare my life please!"
    "Basil drops every card and thingiemabob from their wallet on the ground."
    "The mischievous possum takes what Basil dropped."
    basil "*GASP!*"
    dafny "What did you do that for?"
    possum "I can sell these cards on the internet for a few pretty pennies."
    possum "I can sell this loyalty card for 20 dollars."
    basil "NO PLEASE! NOT THE LOYALTY CARD!"
    basil "Please spare the loyalty card, please please please.."
    dafny "You give them back the loyalty card right now!"
    basil "I can give you my drivers licence, please!"
    basil "I don't even drive anymore!"
    "The possum takes a closer look at the drivers licence."
    possum "Expired."
    possum "I can sell this to some kids to make fake ones from."
    basil "Please do, just not the loyalty card."
    possum "You have a deal."
    "The possum quickly disappears."
    hide possum
    show basil sad at right
    basil "..."
    dafny "..."

    basil "Lets leave."
    dafny "Yeah."
    basil "Wait, it took my go card."
    dafny "What?"
    scene bg black with fade
    basil "After a stupid long walk, I was able to reach home."
    basil "From that point on, Dafny knew me only as the person who got their drivers licence stolen by a possum."
    basil "..."
    jump generalbadend

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
    dafny "So, um, nice lake day I suppose?"
    dafny "Did you like that song I shared to you?"
    basil "Yeah."
    basil "So you like romantic songs I guess?"
    dafny "Oh yeah, absolutely."
    dafny "But I think I should leave now."
    basil "Oh, um yeah, me too.."
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
