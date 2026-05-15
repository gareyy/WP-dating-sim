
init python:

    g = Gallery()

    g.button("dafny")
    g.image(Image("images/dafny/Neutral.png", oversample=6))
    g.unlock("dafny")
    g.image(Image("images/dafny/Lovestruck.png", oversample=6))
    g.unlock("dafny lovestruck")
    g.image(Image("images/dafny/Flustered.png", oversample=6))
    g.unlock("dafny flustered")
    g.image(Image("images/dafny/Swimwear.png", oversample=6))
    g.unlock("dafny swimwear")

    g.button("basil")
    g.image(Image("images/basil/Normal.png", oversample=6))
    g.unlock("basil")
    g.image(Image("images/basil/Laughing.png", oversample=6))
    g.unlock("basil laughing")
    g.image(Image("images/basil/Swimwear.png", oversample=6))
    g.unlock("basil swimwear")
    g.image(Image("images/basil/Lovestruck.png", oversample=6))
    g.unlock("basil lovestruck")
    g.image(Image("images/basil/Pooped.png", oversample=6))
    g.unlock("basil pooped")

    g.button("animals")
    g.image(Image("images/animals/ibis.png", oversample=0.5))
    g.unlock("ibis")
    g.image(Image("images/animals/possum.png", oversample=0.3))
    g.unlock("possum")
    g.image(Image("images/animals/possum_fork.png", oversample=0.5))
    g.unlock("possum fork")
    g.image(Image("images/animals/pukeko.png", oversample=1.2))
    g.unlock("pukeko")
    g.image(Image("images/animals/raven.png", oversample=1))
    g.unlock("raven")

    g.button("boogie")
    g.image(Image("images/boogie/Boogie.png", oversample=6.5))
    g.unlock("boogie")
    
    g.button("isabelle")
    g.image(Image("images/isabelle/Neutral.png", oversample=6))
    g.unlock("isabelle")
    g.image(Image("images/isabelle/Sledging.png", oversample=6.5))
    g.unlock("isabelle sledging")

    g.button("rocq")
    g.image(Image("images/side_characters/rocq.png", oversample=1))
    g.unlock("rocq")
    g.image(Image("images/side_characters/coq.png", oversample=1))
    g.condition("persistent.hundoPercent")

    g.button("cutscenes")
    g.image("taiko")
    g.unlock("cutscene taiko")
    g.image("housealwayswins")
    g.unlock("cutscene housealwayswins")
    g.image("shot")
    g.unlock("cutscene shot")
    g.image(Image("images/cutscene/pukeko.png"))
    g.unlock("cutscene pukeko")
    g.image("kiss")
    g.unlock("cutscene kiss")

    g.button("artifacts")
    g.image(Image("artifacts/ligature.png", oversample=0.7))
    g.unlock("artifact left")
    g.image(Image("artifacts/crab.png", oversample=0.7))
    g.unlock("artifact middle")
    g.image(Image("artifacts/foxgirl_new.png", oversample=0.7))
    g.unlock("artifact right")
    g.image(Image("artifacts/wpp.png", oversample=0.7))
    g.unlock("artifact enter")
    
    g.button("backgrounds")
    g.unlock_image("bg lab")
    g.unlock_image("bg restaurant")
    g.unlock_image("bg uqlakes")
    g.unlock_image("bg museum")
    g.unlock_image("bg pool")
    g.unlock_image("bg hartley")
    g.unlock_image("bg alleyway")
    g.unlock_image("bg karaoke")
    g.unlock_image("bg arcade")
    g.unlock_image("bg spa")
    g.unlock_image("bg casino")
    g.unlock_image("bg house")

    g.button("concept_art")     # Finished game + below
    g.condition("persistent.goodEnding")
    g.image(Image("gallery/dafny.jpg", oversample=2))   # Always
    g.image(Image("gallery/isabelle0.jpg", oversample=2))   # Always
    g.image(Image("gallery/isabelle1.jpg", oversample=3.4))   # Always
    g.image(Image("gallery/prototype.jpg", oversample=2))   # Always
    g.image(Image("gallery/sketch_yuri.png"))   # Always
    g.image(Image("gallery/sketch_housealwayswins.png"))   # Housealwayswins
    g.unlock("cutscene housealwayswins")
    g.image(Image("gallery/sketch_shot.png"))   # Shot
    g.unlock("cutscene shot")
    g.image(Image("gallery/sketch_taiko.png"))   # Taiko
    g.unlock("cutscene taiko")
    g.image(Image("gallery/possum.png", oversample=0.35))   # Possum
    g.unlock("possum")
    g.image(Image("gallery/boogie1.png", oversample=2))   # Boogie
    g.unlock("boogie")
    g.image(Image("gallery/boogie0.png", oversample=0.6))   # 100%
    g.condition("persistent.hundoPercent")
    g.image(Image("gallery/sketch_sidecharacters.png", oversample=6))   # 100%
    g.condition("persistent.hundoPercent")
    g.image(Image("gallery/yuri0.jpg", oversample=2.5))   # 100%
    g.condition("persistent.hundoPercent")
    g.image(Image("gallery/alt_ergo.jpg", oversample=3.3))  # ?
    g.condition("persistent.hundoPercent")
    g.image(Image("gallery/coq_and_rocq.jpg", oversample=2))   # ?
    g.condition("persistent.hundoPercent")
    g.image(Image("gallery/lean0.jpg", oversample=3))   # ?
    g.condition("persistent.hundoPercent")
    g.image(Image("gallery/lean1.png", oversample=3))   # ?
    g.condition("persistent.hundoPercent")
    g.image(Image("side_characters/phantom.png", oversample=1))   # ?
    g.condition("persistent.hundoPercent")

    g.transition = dissolve


screen gallery:

    # Ensure this replaces the main menu.
    tag menu

    imagemap:
        idle "images/backgrounds/restaurant.png"
        hover "images/backgrounds/restaurant.png"
        xsize 1920
        ysize 1080
        at transparency()

    grid 5 2:

        ysize 970
        xfill True
        yfill True

        add g.make_button("basil", "#00ff00", xalign=0.5, yalign=0.5, style="button")
        add g.make_button("dafny", "#ffff00", xalign=0.5, yalign=0.5, style="button")
        add g.make_button("animals", "#ff0000", xalign=0.5, yalign=0.5, style="button")

        add g.make_button("boogie", "#ff0000", xalign=0.5, yalign=0.5, style="button")
        add g.make_button("isabelle", "#ff0000", xalign=0.5, yalign=0.5, style="button")
        add g.make_button("rocq", "#ff0000", xalign=0.5, yalign=0.5, style="button")

        add g.make_button("cutscenes", "#ff0000", xalign=0.5, yalign=0.5, style="button")
        add g.make_button("artifacts", "#ff0000", xalign=0.5, yalign=0.5, style="button")
        add g.make_button("backgrounds", "#ff0000", xalign=0.5, yalign=0.5, style="button")
        add g.make_button("concept_art", "#ff0000", xalign=0.5, yalign=0.5, style="button")

    null height 60
    
    # TODO: Make this look better
    textbutton "Return" action Return() xalign 0.5 yalign 0.95