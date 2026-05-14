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
    isabelle "And I say you are closer to it than you think."
    show basil surprised
    basil "What?"
    isabelle "I think you'll figure it out..."
    isabelle "But first, a hint."
    play sound "sfx/discovery.ogg"
    $ lemmas_list.add("Dafny's favourite food is tofu")
    isabelle "You know she would have wanted to have the tofu, right?"
    basil "Yeah I guess? I might've ordered it if I knew it was on the menu."
    basil "Maybe for next time we eat together."
    show basil sad
    basil "Which will be never, we drifted apart."
    isabelle "Oh really?"
    isabelle "Look around..."
    "Basil takes a look around, then looks at the date and time."
    basil "Uh oh!"
    isabelle "You should take a sledgehammer approach to these next few first dates."
    basil "I don't get what you're saying."

    isabelle "Actually, let's try it right now!"
    isabelle "One thing I know about Dafny – sometimes she just needs a bit of guidance."
    isabelle "Some additional facts might help her figure things out. Even if those facts seems trivial to you."


    hide isabelle
    hide basil

    show isabelle
    show screen lemmabutton with dissolve

    isabelle "For new choices to appear, you must apply what you've learned on the way."
    isabelle "If you click that button on the top left, it'll show you some useful information."
    isabelle "Useful information is {b}marked in bold.{\b} as they appear in dialog."
    isabelle "You can apply those information when you need to make a choice."

    call add_lemma(TUTORIAL_INFO)

label tutorial_loop:
    if tutorial_loop_no > 42:
        if renpy.random.randint(1, 10) == 1:
            isabelle "Actually, you know what? This has been going on for long enough."
            "Isabelle sledges her sledgehammer towards you."
            show bg black with fade
            isabelle "Here's your good ending."
            call goodend
            $ MainMenu(confirm=False, save=True)()
        elif renpy.random.randint(1, 5) == 1:
            isabelle "Okay, that's enough. Just... come back another time."
            $ tutorial_loop_no = 0
            $ MainMenu(confirm=False, save=True)()
    if tutorial_loop_no > 15:
        pass
    if tutorial_loop_no > 0:
        isabelle "You need to apply what you've learned."
        isabelle "Check out that button on top left."
    $ tutorial_loop_no += 1
    menu:
        "Go back":
            call tutorial_loop
        "Go back":
            call tutorial_loop
        "Leave" if tutorial_info:
            python:
                lemmas_list.remove(TUTORIAL_INFO)

    scene bg restaurant with fade
    jump restaurant
