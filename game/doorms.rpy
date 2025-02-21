init 1 python:
    from game.girls.functions import compare_girls_locked
    from game.pymodules.moduleClasses import SimpleVars

    doorms_max_per_col= 4
    doorms_max_per_page= doorms_max_per_col * 3
    doorms_actual_page= SimpleVars()
    
    def filtrate_dorms_girls():
        arr = []
        for  i,g in enumerate(compare_girls_locked(True)):
            if i // doorms_max_per_page == doorms_actual_page.v: 
                arr.append(g)
        return arr

    def dorms_shop_next_page():
        newval = doorms_actual_page.v + 1
        to_dism = 0
        compared = len(compare_girls_locked(True))
        if compared % doorms_max_per_page == 0.0:
            to_dism = 1
        if (compared // doorms_max_per_page) - to_dism  >= newval: 
            doorms_actual_page.setload(newval)
            Show("dorm_init_screen")

    def dorms_shop_prev_page():
        newval = doorms_actual_page.v - 1
        if 0  <= newval: 
            doorms_actual_page.setload(newval)
            Show("dorm_init_screen")

    def dorms_positon(i, pos):
        if pos == "y":
            base = -(i * 200)
            y = base + 31 + 100
            y += (i // doorms_max_per_col) * 215 
            return y
        elif pos == "x":
            base = 0 + 300
            x = base + 44
            x += ((i) % 3) *215
            return x


screen dorm_init_screen():
    add "/assets/reclutamiento4.png" xpos 300 ypos 100
    $ g_visible = filtrate_dorms_girls()
    $ print(g_visible)
    vbox:
        for i,g  in enumerate(g_visible):
            $ image = im.Scale("images/profiles/" + g["reclut"]["s_pre_img"][0], 200, 200)
            $ image_hov = im.Scale("images/profiles/" + g["reclut"]["s_pre_img"][1], 200, 200)
            vbox:
                box_wrap True
                imagebutton:
                    idle image
                    action "sad"
                    ypos dorms_positon(i, "y")
                    xpos dorms_positon(i, "x")
                    hover image_hov

    vbox:
        $ btn = im.Scale("images/assets/flecha_next3.png" , 200, 50)
        $ btn_hov = im.Scale("images/assets/flecha_next_hover3.png" , 200, 50)
        imagebutton:
            idle btn
            hover btn_hov
            ypos 697 + 100
            xpos 474 + 300
            action Function(dorms_shop_next_page)


    vbox:
        $ btn = im.Scale("images/assets/menu3.png" , 200, 50)
        $ btn_hov = im.Scale("images/assets/menu_hover3.png" , 200, 50)
        imagebutton:
            idle btn
            hover btn_hov
            ypos 697 + 100
            xpos 259 + 300
            action Function(Jump_To, "mm_lab")

    vbox:
        $ btn = im.Scale("images/assets/flecha_prev3.png" , 200, 50)
        $ btn_hov = im.Scale("images/assets/flecha_prev_hover3.png" , 200, 50)
        imagebutton:
            idle btn
            hover btn_hov
            ypos 697 + 100
            xpos 44 + 300
            action Function(dorms_shop_prev_page)
label dorms:
    $ doorms_actual_page.setload(0)
    image bg doorms_bg_init = "/menu_backgrounds/bg_dorms_init.png"
    show bg doorms_bg_init with dissolve
    show image "/menu_backgrounds/obcs_50.png" with dissolve
    call screen dorm_init_screen with dissolve