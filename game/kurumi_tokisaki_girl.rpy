init python:
    import game.girls.kurumitokisaki

#IMAGES

default sk = 0
default po = 0

image bg kurumi_t_bg = "/images/menu_backgrounds/bg_doorms_1.png"

image kurumi_t SK0_PO = "/images/sprays/kurumi_dorm_sk[sk]_po[po].png"
# image kurumi_t SK0_PO1 = "/images/sprays/kurumi_dorm_sk0_po0.png"
# image kurumi_t SK0_PO2 = "/images/sprays/kurumi_dorm_sk0_po1.png"


# image kurumi_t SK4_PO1 = "/images/sprays/kurumi_dorm_sk4_po0.png"
# image kurumi_t SK4_PO2 = "/images/sprays/kurumi_dorm_sk4_po1.png"


# image kurumi_t SK5_PO1 = "/images/sprays/kurumi_dorm_sk5_po0.png"
# image kurumi_t SK5_PO2 = "/images/sprays/kurumi_dorm_sk5_po1.png"



#IMAGES


label dorm_w_kurumi_tokisaki:
    pl "¿Buenos dias, Kurumi?"
    kurumi_t "['Buenos dias Sr '] [get_store('plname')] ['¿que necesita?']"
    pl "Queria hablar contigo, ¿Estas libre en tu habitacion?"
    kurumi_t "Si, puede venir cuando quiera."
    pl "Bien, voy para alla."
    jump dorm_inside_kurumi_tokisaki
    return ""

label cosa3:
    $ dorms_loop = True
    call screen cosa1
    return ""



screen dorm_menu_1_kurumi_tokisaki:
    vbox:
        textbutton "Entrenar" action Function(Jump_To, "cosa3") style_prefix "dorm_menu_"
        textbutton "Cambiar Ropa" action Function(Jump_To, "dorm_menu_changeClothes_kurumi_tokisaki") style_prefix "dorm_menu_"
        textbutton "Volver a mi habitacion" action Function(Jump_To, "dorm_inside_gb_kurumi_tokisaki") style_prefix "dorm_menu_"

    # vbox:
    #     textbutton "asd" action Function(Jump_To, "cosa3") style_prefix "button2_"
    #     if dorms_loop:
    #         textbutton "asd2" action Function(Jump_To, "cosa3") style_prefix "button2_"



label dorm_menu_changeClothes_kurumi_tokisaki:
    $ shared_doorm_wid = 1
    call screen shared_doorm_inside_change_clothes
    return ""



label dorm_inside_changing_kurumi_tokisaki:
    pass

label dorm_inside_kurumi_tokisaki:
    $ shared_dorm_skin_jumper = "dorm_inside_changing_kurumi_tokisaki"
    scene bg kurumi_t_bg with dissolve
    $ sk = get_actual_skin(1)
    $ po = 1
    show kurumi_t SK0_PO:
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
        kurumi_t "Buenos dias. ¿En que puedo ayudarlo?"
        $ sk = get_actual_skin(1)
        $ po = 0
        show kurumi_t SK0_PO:
            xpos 1400
        with dissolve
        $ dorms_loop = True
        call screen dorm_menu_1_kurumi_tokisaki with dissolve

    else:
        $ sk = get_actual_skin(1)
        $ po = 1
        show kurumi_t SK0_PO:
            xpos 1400
        with dissolve
        kurumi_t "Kiki. ¿Necesita algo mas?~"
        $ sk = get_actual_skin(1)
        $ po = 0
        show kurumi_t SK0_PO:
            xpos 1400
        with dissolve
        call screen dorm_menu_1_kurumi_tokisaki with dissolve


label dorm_inside_gb_kurumi_tokisaki:
    $ dorms_loop = False
    $ shared_dorm_skin_jumper = False
    $ shared_dorm_actual_skin = -1
    $ sk = get_actual_skin(1)
    $ po = 1
    show kurumi_t SK0_PO:    
        xpos 1400
    with dissolve
    kurumi_t "Espero que haiga pasado un buen rato."
    kurumi_t "Lo espero la proxima, Sr [get_store('plname')]." 
    hide kurumi_t with dissolve
    jump dorms
    return ""


# im.Scale("bg/house.jpg", config.screen_width, config.screen_height),




# "Entrenar"

# "Cambiar Ropa"

# "Volver al menu"