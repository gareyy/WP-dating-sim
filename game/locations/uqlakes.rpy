# Story - UQ Lakes: 
# Choice: Which animal/thing to look at and see and talk about.
# Information: (Before choice) You two are listening to music together on the walk, they put on their favourite song (Karaoke)
# Animals: Raven, Ibis, Pukeko, Water Dragon, Possum (3 neutral, 1 ideal, 1 bad (on second run))
# Animals should be the only voice acted characters and use real images.
# Bad ending: Animal can steal your girl

# Dafny’s favourite song, duet, some romantic song about loving and missing each other



label uqlakes:

    scene bg uqlakes
    show dafny at left
    show basil at right
    with fade

    # Walking to the lakes
    dafny "This is such a nice place to go for a walk together!"
    basil "Yeah, I love coming here. It's so peaceful and beautiful."
    dafny "I always love listening to music together while we walk."
    basil "Yeah, I love sharing music with you. It feels like we're connecting on a deeper level when we do that."
    dafny "Oh, I have a song I want to play for you! It's one of my favorites!"
    basil "Sure, I'd love to hear it!"
    play music "audio/duet.ogg"

    ""
    dafny "I hope you like it! It's a really romantic song that I think is perfect for a walk by the lake."
    basil "I love it!"

    python:
        karaoke_info = True

    dafny "It's really nice to have such a beautiful place to relax so close to our workplace!"
    basil "Yeah, it's really great. I love coming here during my breaks to clear my head."

    
    basil "Look at those animals over there! They look so cute and peaceful."


    if not uqlakes_info:
        menu:
            "Ibis":
                call .ibis_choice

            "Water Dragon":
                call .water_dragon_choice
            
            "Possum":
                call .possum_choice
    
    if uqlakes_info:
        menu:
            "Raven":
                call .raven_choice

            "Possum":
                call .possum_choice
            
            "Pukeko":
                call .pukeko_choice

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

label .raven_choice:
    basil "Oh look! A sick ass raven!"
    dafny "Wow that is a sick ass raven! I love ravens, they are so epic and wise!"
    return

label .pukeko_choice:
    basil "Oh look! A pukeko!"
    dafny "A pukeko! Those are interesting!"
    jump .uqlakes_badend

label .uqlakes_badend:
    jump badend_a

