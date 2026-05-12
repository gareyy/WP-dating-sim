# tutorial
label tutorial:
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
    
    show isabelle at left
    show basil surprised at right

    basil "Wait wh- who are you?"

    isabelle "Let's just say..."
    isabelle "An observant bystander."

    show basil hesitant at right
    basil "Ok and why are you so interested?"
    isabelle "Oh I just don't like seeing people fumble on dates."

    basil "Oh- Wh-"
    show basil angry
    basil "That was not a date!"
    isabelle "I know what you want..."
    isabelle "And I say you are you closer to it than you think."
    show basil surprised
    basil "What?"
    isabelle "I think you'll figure it out..."
    isabelle "But first a hint."
    play sound "sfx/discovery.ogg"
    $ lemmas_list.add("Dafny's favourite food is tofu")
    isabelle "You know she would have wanted the tofu right?"
    basil "Yeah I guess?"
    basil "Maybe for next time we eat together."
    basil "Which will be never, we drifted apart."
    isabelle "Oh really?"
    isabelle "Look around..."
    "Basil takes a look around, then looks at the date and time."
    basil "Uh oh!"
    isabelle "Let's just say, you should take a sledgehammer approach to these next few first dates.."
    basil "I don't get what you're saying."
    isabelle "You'll understand in time."

    hide isabelle
    hide basil

    show isabelle
    show screen lemmabutton with dissolve
    isabelle "Oh by the way, if you click that button on the top left, it'll show you some useful information."
    isabelle "Useful information is {b}marked in bold.{\b}"

    scene bg restaurant with fade
    jump restaurant
