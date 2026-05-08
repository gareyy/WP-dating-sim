# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define basil = Character("Basil")
define dafny = Character("Dafny")


# The game starts here.

label start:

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

