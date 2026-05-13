define child = Character("Child")

image cutscene shot = Image("images/cutscene/shot.png")

label hartley:
    stop music fadeout 3.0
    scene bg hartley

    show basil thinking at left
    basil "Why is it so in dark here?"
    show dafny laughing at right
    dafny "Awww~ Are you scared?"
    dafny "Can't handle your own haunt?"
    show basil
    basil "I'm not scared..."

    "CLANG!"
    
    show dafny scared
    dafny "What was that?"
    basil "Not so confident yourself huh."

    "The sound of a screaming child rings out through the halls"
    child "Six seven six seven!"
    dafny "Basil, this isn't funny any more."
    dafny "Please make it stop!"
    show basil hesitant
    basil "Uh um uhh..."

    child "Six seven! I’m such a fat fucking chud."
    play sound "sfx/fail.ogg"
    "The sound of gun fire fills the corridors as Dafny and Basil are shot in the head."
    show cutscene shot with fade
    ""

    jump generalbadend
