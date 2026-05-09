define house = Character("The House")

label casino:
  
    scene bg casino
    show dafny at left
    show basil at right
    with fade
    stop music fadeout 3.0
    queue music "main/vara.ogg"

    basil "Let's go gambling!"
    "Basil pulls the lever"
    "⊥"
    "⊥ ⊥"
    "⊥ ⊥ ⊥"

    dafny "What does that mean?"
    basil "I think I lost..."
    basil "Guess it can't hurt to try again."
    "Basil pulls the lever"
    "⊥"
    "⊥ ⊥"
    "⊥ ⊥ ⊥"

    show basil angry
    basil "WHY IS THERE ONLY ⊥!"
    show basil
    dafny "Maybe we should quit while we are ahead..."
    basil "Just one more pull."
    "Basil pulls the lever with force and vigor"
    "The lever snaps"

    house "Hey! What do you think you're doing?"
    show basil surprised
    basil "Uhhh... Sorry"
    basil "I didn't mean to.."
    house "You broke my machine!"
    house "That's it! I'm taking your kidneys as punishment."
    dafny "You can't just.."

    "Basil's kidneys are ripped from their body."
    house "I always win."

    jump generalbadend
