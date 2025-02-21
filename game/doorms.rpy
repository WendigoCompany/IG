init 1 python:
    from game.girls.functions import compare_girls_unlocked



screen dorm_screen():
    $ girls_aval = compare_girls_unlocked()
    add "/assets/reclutamiento4.png" xpos 300 ypos 100

label dorms:
    
    # show bg reclutamiento_bg1 with dissolve
    # $ renpy.pause(.2)
    # show bg reclutamiento_bg2 with dissolve
    # $ renpy.pause(.2)
    # $ previewed_girl.setload([-1])
    # $ actual_page.setload(0)
    # call screen reclut_shop with dissolve
    # jump jumper
    # show bg reclutamiento_bg1 with dissolve
    # shjoew

    image bg doorms_bg_init = "/menu_backgrounds/bg_dorms_init.png"
    show bg doorms_bg_init with dissolve
    show image "/menu_backgrounds/obcs_50.png" with dissolve
    call screen dorm_screen with dissolve