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

image ibis = Image("images/animals/ibis.png", oversample=1)
image pukeko = Image("images/animals/pukeko.png", oversample=2)
image dragon = Image("images/animals/water_dragon.png", oversample=2)
image possum = Image("images/animals/possum.png", oversample=0.5)
image raven = Crop((0, 0, 768, 700), Image("images/animals/raven.png", oversample=1))

label uqlakes:

    scene bg uqlakes
    show dafny at left
    show basil at right
    with fade
    stop music fadeout 3.0
    queue music "audio/main/vara.ogg" volume 0.5 fadein 10.0

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
    # play music "audio/duet.ogg"

    "..."
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

    play sound "audio/sfx/choice.ogg"
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
    voice "voice/ibis/line00.ogg"
    ibis "What did you just call me?"
    basil "Oh I am so sorry!"
    voice "voice/ibis/line01.ogg"
    ibis "What did you call me???"
    show dafny scared
    basil "Please calm down."
    basil "My name is Basil and I am so truly sorry."
    voice "voice/ibis/line02.ogg"
    ibis "Grr."
    dafny "You are not gonna do anything to my friend!"
    voice "voice/ibis/line03.ogg"
    ibis "How would you feel if your friend called you a bin chicken?"
    show dafny happy
    dafny "I'd laugh at it."
    voice "voice/ibis/line04.ogg"
    ibis "Go on Basil, call your friend a \"bin chicken\""
    basil "Um..."
    basil "Hey Dafny, you are a uh, um, bin chicken."
    dafny "Wow."
    dafny "I am so honoured..."
    ibis "..."
    voice "voice/ibis/line05.ogg"
    ibis "You have a point Basil."
    voice "voice/ibis/line06.ogg"
    ibis "But I am still offended by you."
    basil "What?"
    "The ibis flies away"
    hide ibis
    show basil at right
    basil "Wow. what a spoil sport of a bird."
    basil "I always see those things picking in bins anyway, thats why they are called bin chickens."
    voice "voice/ibis/line07.ogg"
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
    voice "voice/dragon/grunt0.ogg"
    dragon "..." # add dragon noise where elipsis is, just make something up hayden
    basil "Um, hello?"
    voice "voice/dragon/grunt1.ogg"
    dragon "..."
    dafny "Hello little guy! My name is Dafny, and this is Basil."
    voice "voice/dragon/grunt2.ogg"
    dragon "..."
    basil "Um? Do you talk little guy?"
    voice "voice/dragon/grunt3.ogg"
    dragon "..."
    dafny "I've heard mystical things about the animals of this lake."
    dafny "Like they talk and give you wise advice."
    basil "Is that so?"
    dafny "Supposedly."
    dafny "Like if an animal from here started talking to me I wouldn't be surprised."
    voice "voice/dragon/grunt1.ogg"
    dragon "..."
    basil "..."
    basil "I thought that thing was gonna talk."
    dafny "Anyway, I heard some of these animals could give you advice or fortune."
    dafny "Or possibly have impeccable charisma."
    basil "Really?"
    dafny "I haven't given much thought to it."
    voice "voice/dragon/grunt4.ogg"
    dragon "..."
    hide dragon
    show basil at right

    jump .uqlakes_badend

label .possum_choice:
    basil "Oh look! A possum!"
    dafny "Oh, I sort of like those ones, but they are a bit scary..."

    hide basil 
    show possum at right
    voice "voice/possum/line00.ogg"
    possum "Oh hey you two!"
    basil "Oh, us?"
    voice "voice/possum/line01.ogg"
    possum "Yes you two!"
    show possum fork
    voice "voice/possum/line02.ogg"
    possum "Give me both of your wallets."
    voice "voice/possum/line03.ogg"
    possum "NOW!"
    show dafny scared
    basil "AAAH!"
    dafny "AAAH!"
    voice "voice/possum/line04.ogg"
    possum "NOW!"
    dafny "Please please please! We are both broke program verification researchers!"
    basil "I promise you, all my money is gone and I spent it on food!"
    voice "voice/possum/line05.ogg"
    possum "Is that so?"
    basil "Spare my life please!"
    "Basil drops every card and thingiemabob from their wallet on the ground."
    "The mischievous possum takes what Basil dropped."
    basil "*GASP!*"
    dafny "What did you do that for?"
    voice "voice/possum/line06.ogg"
    possum "I can sell these cards on the internet for a few pretty pennies."
    voice "voice/possum/line07.ogg"
    possum "I can sell this loyalty card for 20 dollars."
    basil "NO PLEASE! NOT THE LOYALTY CARD!"
    basil "Please spare the loyalty card, please please please.."
    dafny "You give them back the loyalty card right now!"
    basil "I can give you my drivers licence, please!"
    basil "I don't even drive anymore!"
    "The possum takes a closer look at the drivers licence."
    voice "voice/possum/line08.ogg"
    possum "Expired."
    voice "voice/possum/line09.ogg"
    possum "I can sell this to some kids to make fake ones from."
    basil "Please do, just not the loyalty card."
    voice "voice/possum/line10.ogg"
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
    voice "voice/pukeko/line00.ogg"
    pukeko "Oh hey baby girl."
    show dafny blushing
    dafny "Who, me?"
    voice "voice/pukeko/line01.ogg"
    pukeko "Yes you, fine little thing."
    basil "(Oh fuck.)"
    basil "Hey uh, pukeko, you talk?"
    voice "voice/pukeko/line02.ogg"
    pukeko "Oh yes I do beautiful."
    voice "voice/pukeko/line03.ogg"
    pukeko "You two on a date?"
    basil "Oh um-"
    show dafny surprised
    dafny "Oh uhhh"
    voice "voice/pukeko/line04.ogg"
    pukeko "I take that as a no beautiful?"
    dafny "I don't think we are."
    basil "(Ruh roh...)"
    basil "I think we did just eat at a fancy restaurant tho."
    "The pukeko looks at Dafny"
    show dafny blushing
    voice "voice/pukeko/line05.ogg"
    pukeko "What's your name honeypumps?"
    dafny "Um, Dafny."
    "She twiddles with her hair, pulling it back to show her ear."
    basil "Oh and my name is Basil."
    voice "voice/pukeko/line06.ogg"
    pukeko "Ah, nice to meet you two."
    voice "voice/pukeko/line07.ogg"
    pukeko "But especially you more,"
    voice "voice/pukeko/line08.ogg"
    pukeko "Dafny"
    "The pukeko says her name in a way that sounds like the most beautiful music to Dafny's ears"
    show dafny lovestruck
    dafny "W- wow..."
    dafny "Basil, I think I love this pukeko..."
    basil "Are you kidding me???"
    voice "voice/pukeko/line09.ogg"
    pukeko "I can show you the world, babygirl."
    dafny "I am convinced."
    dafny "You know what little pukeko? I love you."
    dafny "Can we go out today?"
    voice "voice/pukeko/line10.ogg"
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
    voice "voice/raven/line00.ogg"
    raven "Hello."
    voice "voice/raven/line01.ogg"
    raven "What are your names you two?"
    dafny "Dafny"
    basil "Basil"
    voice "voice/raven/line02.ogg"
    raven "I see..."
    voice "voice/raven/line03.ogg"
    raven "You say I am wise?"
    dafny "Oh yes! I do."
    voice "voice/raven/line04.ogg"
    raven "The wisest do not say they are wise, but they have others prove it."
    dafny "So you're saying you're wise?"
    raven "..."
    basil "You got any wise sayings or whatever it is?"
    basil "That stuff Sun Tzu says?"
    voice "voice/raven/line05.ogg"
    raven "That guy is a warlord, I am a bird of peace."
    voice "voice/raven/line06.ogg"
    raven "I am also hungry."
    dafny "Ooh I got something!"
    dafny "I got the entree from the restaurant!"
    basil "Oh yeah!"
    "Dafny and Basil split the food, and give it to the raven."
    "The raven chews it up and spits it out in a wise way."
    voice "voice/raven/line07.ogg"
    raven "Yummers."
    voice "voice/raven/line08.ogg"
    raven "For your offering of the physical world, I shall return to you some knowledge of the spiritual world."
    "The raven looks introspective."
    voice "voice/raven/line09.ogg"
    raven "Oh, I am starting to see."
    raven "..."
    voice "voice/raven/line10.ogg"
    raven "You two are two halves that need to come together at some part in the world."
    voice "voice/raven/line11.ogg"
    raven "Thats when you will achieve true happiness."
    show dafny blushing
    dafny "Woah."
    basil "W-"
    voice "voice/raven/line12.ogg"
    raven "I see a long life of love and happiness."
    dafny "..."
    basil "..."
    voice "voice/raven/line13.ogg"
    raven "Oh I just realised what I said was a prediction, not knowledge of the spiritual world."
    voice "voice/raven/line14.ogg"
    raven "I'm sorry about that."
    "Dafny and Basil are blushing purple."
    dafny "..."
    basil "..."
    basil "(Woah.)"
    voice "voice/raven/line15.ogg"
    raven "But uh yeah, thats it."
    voice "voice/raven/line16.ogg"
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
