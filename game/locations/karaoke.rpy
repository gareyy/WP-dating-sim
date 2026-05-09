# Story - Karaoke:
# Choice: Song to choose and sing. Dafny has a favourite song. Song choices include: 
# Disco style song (original composition)
# Dafny's favourite song, duet, some romantic song about loving and missing each other
# Song about drinking heavily and being heartbroken, i.e like baka mitai
# Information: (Before Choice) you two are appreciating the graffiti on the walls walking to the karaoke place, Dafny mentions they would like to be an artist's muse one day (Museum)
# Bad Ending: Boogie steals your girl if you select the disco song

define boogie = Character("Boogie", color="#ffffff")

label karaoke:

    scene bg alleyway
    show dafny at left
    show basil at right
    with fade

    # See graffiti on the way to karaoke
    dafny "Wow, look at all this graffiti! It's so cool and artistic!"
    basil "Yeah, it's really impressive."
    dafny "I wish I could be an artist's muse one day and inspire them to create amazing art like this!"
    basil "That would be really cool. You would make a great muse!"
    python:
        museum_info = True

    scene bg karaoke
    show dafny at left
    show basil at right
    with fade

    dafny "I can't wait to sing some songs together! This is going to be so much fun!"
    
    dafny "What song should we sing first? I have a few in mind, but I'm open to suggestions too!"

    menu:
        "Club Song":
            call .club_choice

        "Heartbreak Song":
            call .heartbreak_choice
        
        "Romantic Duet" if karaoke_info:
            call .duet_choice
    
    dafny "That was so much fun! I love singing with you!"
    dafny "We should do this more often!"

    jump ending

label .club_choice:
    basil "Oh, a club song! That sounds like fun!"
    dafny "I'm not sure if that's really my style, but I'm down to give it a try!"
    if karaoke_info:
        jump .steal_your_girl
    jump .karaoke_badend

label .heartbreak_choice:
    basil "Oh, a heartbreak song! That sounds really emotional!"
    dafny "Kinda makes me sad just thinking about it..."

    "Basil begins to sing the song about heartbreak."
    basil "Oh..."
    basil "You make my heart bleed."
    basil "You were key to my heart, the key to my soul."
    basil "My love was too much, it went out of bounds."
    basil "And now my heart bleeds..."
    basil "It runs wild for you unchecked."
    basil "And that's thats how I lost you..."
    basil "And now my heart is left vulnerable."
    basil "..."
    "The music ends"

    show dafny sad
    basil "Are you alright?"
    dafny "Yeah, I'm okay."
    dafny "I don't always deal well with songs like that..."
    basil "Sorry, I..."
    dafny "It's okay, I know you didn't mean to."
    "The karaoke score says \"78\""
    dafny "On the bright side, you got a score of 78."

    jump .karaoke_badend

label .duet_choice:
    basil "Oh, a romantic duet! That sounds perfect for us!"
    dafny "Aww, this is one of my favourite songs! I'm so glad you want to sing it with me!"

    "Basil and Dafny sing the duet together."

    basil "You asserted yourself into my life."
    basil "And now you're part of my scope."
    dafny "And as I reasoned about you more."
    dafny "You became invariant to myself."
    dafny "As time, goes by."
    dafny "I find more reason to make you an invariant in my life."
    basil "It's true from the start, it's true in the end."
    basil "Instead of what's been done,"
    basil "Think about whats to come."
    dafny "You proved our lemma to me and now it's crystal clear."
    dafny "You fit my specification perfectly, you're the correct one for me."
    
    "The song ends."

    show dafny laughing
    dafny "Thank you for doing that!"
    basil "You have a very nice singing voice."
    dafny "You aren't too bad yourself, even though you were a bit pitchy!"
    "The karaoke score reads \"100\""
    basil "Yeah!"
    dafny "Yeah!"

    return

label .steal_your_girl:
        # Start playing the sick bop
    "As the song begins playing, the door is thrown open"

    show basil at left
    basil "What in the..."
    
    show boogie at right
    boogie "Now that's a funky music I hear in here!"
    basil "Who are y..."
    boogie "With fine vibes like thine it would be a crime not to swing by!"
    basil "Who are you!?"
    boogie "Name is Boogie and I'm here to take you on the fast track to funky town!"

    "Boogie proceeds to spin around in a groovy fashion"

    hide basil
    boogie "Speakin' of funky, who's the groovy young lady over here?"
    show dafny blushing at left
    dafny "Groovy?..."
    boogie "Why do you doubt yourself? Your vibe is evident for all to see."
    dafny "Are you sure?"
    boogie "You're the vibiest girl I've seen all night!"

    hide dafny
    show basil angry at left
    basil "What about my vibe?"
    boogie "You're... okay."
    boogie "Anyways, young lady, shall we hit the dance floor?"
    basil "You don't even know her name!"

    hide basil
    show dafny blushing at left
    dafny "Dafny, my name is Dafny."
    boogie "Well that settles things, to the dance floor!"
    
    hide boogie
    show dafny at right
    show basil at left
    basil "Wait what about our..."
    dafny "Don't worry I'll see you after the song is over."
    basil "Are you sure?"
    hide dafny
    "Dafny was whisked away by Boogie's charisma and charm"

    "The karaoke score was \"99\""

    scene bg black with fade
    show basil sad
    basil "It's been four hours, I don't think she is coming back."
    basil "I can see why..."
    basil "He was simply too groovy for me to handle."


    jump generalbadend

label .karaoke_badend:
    jump badend_a

