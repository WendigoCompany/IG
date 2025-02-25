init python:
    import game.girls.kurumitokisaki



###################################################################################################[DORMS]##########################################################################################################################################################################################
#IMAGES

default kurumi_dorm_sk = 0
default kurumi_dorm_po = 0

image bg kurumi_t_bg = "/images/menu_backgrounds/bg_doorms_1.png"

image kurumi_t SK0_PO = "/images/sprays/kurumi_dorm_sk[kurumi_dorm_sk]_po[kurumi_dorm_po].png"

#IMAGES

# ENTRANDO A LA HABITACION
label dorm_w_kurumi_tokisaki:
    pl "[get_txt_db(dorm_txt['girls']['1']['intro'] , 0, False)]"
    kurumi_t "[get_txt_db(dorm_txt['girls']['1']['intro'] , 1, False)] [get_store('plname')] [get_txt_db(dorm_txt['girls']['1']['intro'] , 2, False)]"
    pl "[get_txt_db(dorm_txt['girls']['1']['intro'] , 3, False)]"
    kurumi_t "[get_txt_db(dorm_txt['girls']['1']['intro'] , 4, False)]"
    pl "[get_txt_db(dorm_txt['girls']['1']['intro'] , 5, False)]"
    jump dorm_inside_kurumi_tokisaki
    return ""
# ENTRANDO A LA HABITACION

# MENU PRINCIPAL
screen dorm_menu_1_kurumi_tokisaki:
    vbox:
        textbutton get_txt_db(dorm_txt["dorm_menu"]["ui"] , "train", False) action Function(Jump_To, "cosa3") style_prefix "dorm_menu_"
        textbutton get_txt_db(dorm_txt["dorm_menu"]["ui"] , "change_clothes", False) action Function(Jump_To, "dorm_menu_changeClothes_kurumi_tokisaki") style_prefix "dorm_menu_"
        textbutton get_txt_db(dorm_txt["dorm_menu"]["ui"] , "back_room", False) action Function(Jump_To, "dorm_inside_gb_kurumi_tokisaki") style_prefix "dorm_menu_"

    # vbox:
    #     textbutton "asd" action Function(Jump_To, "cosa3") style_prefix "button2_"
    #     if dorms_loop:
    #         textbutton "asd2" action Function(Jump_To, "cosa3") style_prefix "button2_"
# MENU PRINCIPAL



# MENU CAMBIAR ROPA
label dorm_menu_changeClothes_kurumi_tokisaki:
    $ shared_doorm_wid = 1
    call screen shared_doorm_inside_change_clothes
    return ""
# MENU CAMBIAR ROPA


#ACTUALIZANDO LA SKIN
label dorm_inside_changing_kurumi_tokisaki:
    show kurumi_t SK0_PO:
        xpos 2000
    with moveinright
    $ kurumi_dorm_sk = get_actual_skin(1)
    $ kurumi_dorm_po = 0
    show kurumi_t SK0_PO:
        xpos 1400
    with moveinright
    call screen shared_doorm_inside_change_clothes
    return ""
#ACTUALIZANDO LA SKIN

#LLAMANDO AL MENU PRINCIPAL
label dorm_inside_kurumi_tokisaki:
    $ shared_dorm_skin_jumper = "dorm_inside_changing_kurumi_tokisaki"
    $ shared_dorm_skin_cb = "dorm_inside_kurumi_tokisaki"
    scene bg kurumi_t_bg with dissolve
    $ kurumi_dorm_sk = get_actual_skin(1)
    $ kurumi_dorm_po = 1
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
        kurumi_t "[get_txt_db(dorm_txt['girls']['1']['inside'] , 0, False)]"
        $ kurumi_dorm_sk = get_actual_skin(1)
        $ kurumi_dorm_po = 0
        show kurumi_t SK0_PO:
            xpos 1400
        with dissolve
        $ dorms_loop = True
        call screen dorm_menu_1_kurumi_tokisaki with dissolve

    else:
        $ kurumi_dorm_sk = get_actual_skin(1)
        $ kurumi_dorm_po = 1
        show kurumi_t SK0_PO:
            xpos 1400
        with dissolve
        kurumi_t "[get_txt_db(dorm_txt['girls']['1']['inside'] , 1, False)]"
        $ kurumi_dorm_sk = get_actual_skin(1)
        $ kurumi_dorm_po = 0
        show kurumi_t SK0_PO:
            xpos 1400
        with dissolve
        call screen dorm_menu_1_kurumi_tokisaki with dissolve
    return ""
#LLAMANDO AL MENU PRINCIPAL

#SALIDA DEL DORM
label dorm_inside_gb_kurumi_tokisaki:
    $ dorms_loop = False
    $ shared_dorm_skin_jumper = False
    $ shared_dorm_actual_skin = -1
    $ kurumi_dorm_sk = get_actual_skin(1)
    $ kurumi_dorm_po = 1
    show kurumi_t SK0_PO:    
        xpos 1400
    with dissolve
    kurumi_t "[get_txt_db(dorm_txt['girls']['1']['cb'] ,0, False)]"
    kurumi_t "[get_txt_db(dorm_txt['girls']['1']['cb'] , 1, False)] [get_store('plname')]." 
    hide kurumi_t with dissolve
    jump dorms
    return ""
#SALIDA DEL DORM

###################################################################################################[DORMS]##########################################################################################################################################################################################

# im.Scale("bg/house.jpg", config.screen_width, config.screen_height),




# "Entrenar"

# "Cambiar Ropa"

# "Volver al menu"