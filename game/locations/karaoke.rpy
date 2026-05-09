# Story - Karaoke:
# Choice: Song to choose and sing. Dafny has a favourite song. Song choices include: 
# Disco style song (original composition)
# Dafny's favourite song, duet, some romantic song about loving and missing each other
# Song about drinking heavily and being heartbroken, i.e like baka mitai
# Information: (Before Choice) you two are appreciating the graffiti on the walls walking to the karaoke place, Dafny mentions they would like to be an artist's muse one day (Museum)
# Bad Ending: Boogie steals your girl if you select the disco song


label karaoke:

    scene bg karaoke
    show dafny at left
    show basil at right
    with fade

    # See graffiti on the way to karaoke
    dafny "Wow, look at all this graffiti! It's so cool and artistic!"
    basil "Yeah, it's really impressive."
    dafny "I wish I could be an artist's muse one day and inspire them to create amazing art like this!"
    basil "That would be really cool. You would make a great muse!"
    python:
        karaoke_info = True


    dafny "I can't wait to sing some songs together! This is going to be so much fun!"
    
    dafny "What song should we sing first? I have a few in mind, but I'm open to suggestions too!"

    menu:
        "Disco Song":
            call .disco_choice

        "Heartbreak Song":
            call .heartbreak_choice
        
        "Romantic Duet" if karaoke_info:
            call .duet_choice
    
    dafny "That was so much fun! I love singing with you!"
    dafny "We should do this more often!"

label .disco_choice:
    basil "Oh, a disco song! That sounds like fun!"
    dafny "I'm not sure if that's really my style, but I'm down to give it a try!"
    if karaoke_info:
        jump .steal_your_girl
    jump .karaoke_badend

label .heartbreak_choice:
    basil "Oh, a heartbreak song! That sounds really emotional!"
    dafny "Kinda makes me sad just thinking about it..."
    jump .karaoke_badend

label .duet_choice:
    basil "Oh, a romantic duet! That sounds perfect for us!"
    dafny "Aww, this is one of my favourite songs! I'm so glad you want to sing it with me!"
    return

label .steal_your_girl:
    dafny "Aaa, I've been got"

label .karaoke_badend:
    jump badend_a

