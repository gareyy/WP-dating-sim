label tutorial:

    # Start by playing some music.
    play music "audio/tutorial.ogg"

    scene bg restaurant

    show isabelle
    
    ""

    isabelle "Hey, you look familiar..."

    menu:

        isabelle "Do I remember seeing you before?"

        "I don't think so":

            isabelle "No, I'm pretty sure you've been here before, not that long ago."

        "I feel like I've been here before":

            isabelle "Oh, I do remember you! You were here not that long ago!"
    
    isabelle "Looks like your date didn't go so well that time, huh?"

    isabelle "You have another chance to do it right this time!"

    isabelle "Remember to make a good impression on your date! You only get one chance!"

    hide isabelle

    show dafny

    jump restaurant
