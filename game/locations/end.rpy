# ending

label ending:
    scene bg black with fade
    play music "sad/intro.ogg"
    queue music "sad/maina.ogg"
    dafny "Oh! Actually, before we split, do you want to come over to my place?"
    basil "(!!!)"
    basil "Uhm..."
    dafny "I would love to have you over."
    dafny "Like please, Basil."
    dafny "I think tonight has been great."
    dafny "I just want to talk about a few things..."
    # show da house
    # singular ending... basil tells truth of the thing to dafny being a time looop
    scene bg house with fade
    show basil at left
    show dafny at right
    # this is the bedroom
    basil "Wow, so uh, this is your bedroom?"
    basil "Nice place."
    dafny "Yeah, um, thanks."
    dafny "Ever since I moved out, I don't think anyone else has been in my bedroom with me."
    show basil blushing
    basil "Y-yeah."
    "They both sit on the bed."
    dafny "Hey um.."
    dafny "..."
    basil "..."
    show dafny blushing
    dafny "...."
    basil "...."
    dafny "....."
    basil "....."
    dafny "U-um.."
    dafny "Do you think we went out on a date tonight?"
    "Basil lets out a slight gasp."
    basil ".."
    basil "I- I-"
    basil "I think so..."
    basil "Like romantic I guess..."
    dafny "Y-yeah, I agree."
    dafny "You know, despite us going to the restaurant and two places tonight, I feel like we may have gone to more places than I remember..."
    dafny "Like it's an amnesiac thing."
    dafny "Or deja vu, or whatever its called."

    show basil at left
    show dafny at right

    queue music "sad/mainb.ogg"

    dafny "Of course, we went to the restaurant, and you ordered the tofu for me, the same thing I was thinking..."
    dafny "You know, sometimes it feels like you were reading my mind."
    dafny "Anyway, what else do I remember?"

    if good_lake:
        dafny "We went to the lake near our work."
        dafny "And there was this raven."
        dafny "And it told us that we are something like soulmates."
        dafny "..."
    if good_museum:
        dafny "We went to the art museum."
        dafny "And there was this painting that really spoke to me."
        dafny "It reminded me of myself."
        dafny "And somehow, you said you liked it the most."
        dafny "..."
    if good_karaoke:
        dafny "I had this favourite song."
        dafny "And somehow you knew what it was."
        dafny "Like I swear I showed you it today."
        dafny "But at the same time my memory is a bit fuzzy on it."
        dafny "And then we went to karaoke, and you chose it as the song to sing."
        dafny "I felt like as when we were singing it, that I was bonded to you in some way."
        dafny "..."
    if good_arcade:
        dafny "When we went to the arcade, there was this one arcade machine I forgot to tell you about."
        dafny "And then you suggested we play that one."
        dafny "The Trimonis one."
        dafny "But like, I didn't ever tell you explicitly."
        dafny "We had a fun time on it, and I won."
        dafny "..."
    if good_pool:
        dafny "Now, I remember that we went to the pool."
        dafny "We were in our swimsuits, and you were like, awestruck at how I looked."
        dafny "It made me feel a little good about myself for the first time in a while."
        dafny "..."
    if good_spa:
        dafny "Later in the night, we went to the spa."
        dafny "And we decided to go to the hot tub together."
        dafny "And um..."
        dafny "I think we were interrupted."
        dafny "..."
    
    show dafny sad
    dafny "Be honest with me Basil, what is truly going on?"
    dafny "How do I remember these things?"

    basil "..."
    basil "I think I was in a time loop."

    dafny "..!"
    dafny "I felt like I was in one too."
    dafny "And there were like, multiple endings to our day that didn't leave me happy in a way."
    dafny "Even if it lead to me going out with someone else..."

    basil "Im glad you trust me on that."
    basil "There was this strange being, with a sledgehammer, that forced me into this time loop."
    basil "And I'm so happy they made me go through this over and over again."
    basil "Because I am such a failure of a human being, and sometimes I feel like you were unapproachable."

    dafny "..."
    dafny "I guess this really was a date tonight, huh?"

    dafny "..."
    basil "Uhm-"
    dafny "..."
    show dafny blushing
    dafny "...."
    
    basil "Um, Earth to Dafny?"

    dafny "Basil."
    dafny "Do you love me?"

    basil "..."
    basil "...."
    show basil blushing
    basil "Y-yes."

    dafny "Basil, I love you too."
    basil "..."
    basil "Yep, yeah, yeah."
    basil "I want to do everything with you."
    basil "I want to spend my whole life with you, Dafny."

    dafny "I agree."
    dafny "I agree so so much."

    basil "Um."
    basil "Do you want to kiss?"

    dafny "Yes please."

    show basil blushing at closeright with move
    show dafny blushing at closeleft with move
    "Their lips collide."
    "Magic is created."
    "The proof of love has been verified."
    basil "(I think I have reached a new high.)"
    basil "*sniff*"
    show basil sad
    basil "*sniff*"
    basil "Dafny, this is my first time kissing."
    dafny "I think you have kissed me better than anyone else."
    dafny "You're a natural at this."
    basil "You sure?"
    dafny "I am."
    basil "I just- have never experienced anything else like this before."
    "Basil begins to cry tears of happiness."
    basil "Oh my god I'm so sorry."
    dafny "It's fine, it's fine Basil."
    dafny "You're with me now."
    show basil blushing at closeright
    basil "I want to do more tonight."
    dafny "M-me too."
    basil "I love you Dafny."
    dafny "I love you Basil."

    scene bg white with fade
    ""
    show isabelle with fade
    queue music "sad/outro.ogg" noloop
    isabelle "And then they had hot steamy verification!"
    isabelle "The end!"

    scene bg black with fade
    "Wekissed Preconditon"
    "A GameJam 2026 game."
    " - "
    " - "
    " - "
    " - "
    " - "

    $ MainMenu(confirm=False)()
