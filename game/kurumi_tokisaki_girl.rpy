init python:
    import game.girls.kurumitokisaki

#IMAGES
image bg kurumi_t_bg = "/images/menu_backgrounds/bg_doorms_1.png"
image kurumi_t SK0_PO1 = "/images/sprays/kurumi_dorm_sk0_po0.png"
image kurumi_t SK0_PO2 = "/images/sprays/kurumi_dorm_sk0_po1.png"
#IMAGES


label dorm_w_kurumi_tokisaki:
    $ plname = "{color=#ffffff}[pl.name]{/color}"
    pl "¿Buenos dias, Kurumi?"
    kurumi_t "['Buenos dias Sr '] [get_store('plname')] ['¿que necesita?']"
    pl "Queria hablar contigo, ¿Estas libre en tu habitacion?"
    kurumi_t "Si, puede venir cuando quiera."
    pl "Bien, voy para alla."


# label a2a21:
#     menu:
#         "Say Statement"
#         "Choice 1":
#             pass
#             #block of code to run
#         "Choice 2":
#                 pass
#             #block of code to run

# label aa21:
#     menu:
#         "Say Statement"
#         "Choice 3":
#             pass
#             #block of code to run
#         "Choice 4":
#                 pass
#             #block of code to run

screen cosa1 :
    vbox:
        textbutton "asd" action Function(Jump_To, "cosa3")
        if dorms_loop:
            textbutton "asd2" action Function(Jump_To, "cosa3")



label dorm_inside_kurumi_tokisaki:
    scene bg kurumi_t_bg with dissolve
    show kurumi_t SK0_PO2:
        xpos 1400
    with moveinright
    # fade, dissolve, pixellate, move,
    # moveinright (Also: moveinleft, moveintop, moveinbottom),
    # moveoutright (Also: moveoutleft, moveouttop, moveoutbottom),
    # ease (Also: easeinright, easeinleft, easeintop, easeinbottom, easeoutright, easeoutleft, easeouttop, easeoutbottom),
    # zoomin, zoomout, zoominout, vpunch, hpunch, blinds, squares,
    # wipeleft (Also: wiperight, wipeup, wipedown),
    # slideleft (Also:  slideright, slideup, slidedown),
    # slideawayleft (Also: slideawayright, slideawayup, slideawaydown),
    # irisin, irisout.



    if not dorms_loop:
        # $ dorms_loop = True
        show kurumi_t SK0_PO1:
            xpos 1400
        with dissolve
        kurumi_t "Buenos dias. ¿En que puedo ayudarlo?"
        call screen cosa1

    else:
        kurumi_t "Kiki. ¿Necesita algo mas?~"
        call screen cosa1


# im.Scale("bg/house.jpg", config.screen_width, config.screen_height),

label cosa3:
    $ dorms_loop = True
    call screen cosa1
