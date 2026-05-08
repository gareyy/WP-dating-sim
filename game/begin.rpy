# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define basil = Character("Basil", color="#c8ffc8")
define dafny = Character("Dafny", color="#ffffc8")
define isabelle = Character("Isabelle", color="#715bff")


# The game starts here.

label start:

    python:
        loop_no = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # can end the game at any time with "return"
    
    basil "Do you ever think about what would have happened if you knew one thing beforehand, or knew how to react in the right way?"
    basil "Sometimes I think about what would have been the right thing to say, or the right thing to do."
    basil "..."
    basil "Theres this girl where I work at... She is the prettiest thing in the world."
    show dafny
    basil "She's the main reason why i'm still doing this program verification stuff."
    basil "I feel like I could reach new heights with her."
    basil "I can show her the world and she can show me the stars."
    basil "I feel like she is a piece of me that I am missing and need filled."
    basil "Its a precondition for me to be with her if I want my life to feel full."
    basil "But you know what? She is just a coworker."
    hide dafny
    basil "I don't know if she loves me. And I am too scared to find out."
    basil "I fear that if I confess, it may jeopardise my professional relationship with her."
    basil "And maybe my own happiness..."
    basil "A million fish in the sea and I will release them back into the oceans if they are not her.."
    basil "Oh heavens above! May you help me in my quest!"
    basil "I would do anything! Even if it meant living the same day over and over again until I get it right!"

    show bg lab with fade
    
    show basil
    basil "Nice! all my work for today is done!"
    basil "I finally implemented that big stupid compoment that was bogging me and Dafny."
    show dafny
    basil "Hey Dafny! I finally got that stupid thing implemented!"
    dafny "Yeah, uh, which one?"
    basil "You know, the one I made a PR for in the repository."
    dafny "Gimme 2 seconds..."
    dafny "The indirect call resolution stuff?"
    basil "Yeah that one."
    dafny "Well congratulations buddy!"
    dafny "You want a reward for that?"
    show basil blushing
    basil "Y-yeah..."
    dafny "You know, you've been getting better at this stuff."
    basil "Oh I have?"
    dafny "Better than an AI I guess."
    show basil
    basil "Im not sure if thats a compliment or not."
    dafny "*cackling* "
    
    jump loophead