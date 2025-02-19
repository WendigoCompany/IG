init python:
    from game.pymodules.moduleClasses import SimpleVars
    from game.girls.girls import girls_db
    
    max_per_page= 9
    max_per_col= 3
    actual_page= SimpleVars()


    def compare_girls_unlocked():
        g_filtrated = []
        for g in girls_db:
            if not g["id"] in (get_store("g_unlocked")):
                g_filtrated.append(g)
        return g_filtrated

    def filtrate_recl_girls():
        arr = []
        for  i,g in enumerate(compare_girls_unlocked()):
            if i // max_per_page == actual_page.v: 
                arr.append(g)
        return arr

    def reclut_shop_next_page():
        # Show("girl_prev")
        newval = actual_page.v + 1
        to_dism = 0
        compared = len(compare_girls_unlocked())
        if compared % max_per_page == 0.0:
            to_dism = 1
        if (compared // max_per_page) - to_dism  >= newval: 
            actual_page.setload(newval)
            Show("reclut_shop")

    def reclut_shop_prev_page():
        newval = actual_page.v - 1
        if 0  <= newval: 
            actual_page.setload(newval)
            Show("reclut_shop")


    def recl_show_girl_info(index):
        print("LA WAFLE SELECCIONADA ES: ", index)
        # Show("girl_prev")
    
    def recl_positon(i, pos):
        if pos == "y":
            base = -(i * 200)
            y = base + 31 + 100
            y += (i // max_per_col) * 215 
            return y
        elif pos == "x":
            base = 0 + 300
            x = base + 44
            x += ((i) % 3) *215
            return x


style tx_button:
    color "#131212"
    size 10
    # font "KGSorryNotSorryChub.ttf"


screen girl_prev(index):
    vbox:
        text girls_db[index]["s_pre_desc"][lang]

screen reclut_shop:
    add "/assets/reclutamiento_final3.png" xpos 300 ypos 100
    # add "/assets/reclutamiento.png" xpos 300 ypos 100
    $ g_visible = filtrate_recl_girls()
    vbox:
        for i,g  in enumerate(g_visible):
            $ image = im.Scale("images/profiles/" + g["reclut"]["s_pre_img"][0], 200, 200)
            $ image_hov = im.Scale("images/profiles/" + g["reclut"]["s_pre_img"][1], 200, 200)
            vbox:
                box_wrap True
                imagebutton:
                    idle image
                    action Function(recl_show_girl_info, g["id"])
                    ypos recl_positon(i, "y")
                    xpos recl_positon(i, "x")
                    hover image_hov

    vbox:
        $ btn = im.Scale("images/assets/flecha_next2.png" , 200, 50)
        $ btn_hov = im.Scale("images/assets/flecha_next_hover2.png" , 200, 50)
        imagebutton:
            idle btn
            hover btn_hov
            ypos 697 + 100
            xpos 474 + 300
            action Function(reclut_shop_next_page)


    vbox:
        $ btn = im.Scale("images/assets/menu2.png" , 200, 50)
        $ btn_hov = im.Scale("images/assets/menu_hover2.png" , 200, 50)
        imagebutton:
            idle btn
            hover btn_hov
            ypos 697 + 100
            xpos 259 + 300
            action Function(reclut_shop_prev_page)

    vbox:
        $ btn = im.Scale("images/assets/flecha_prev2.png" , 200, 50)
        $ btn_hov = im.Scale("images/assets/flecha_prev_hover2.png" , 200, 50)
        imagebutton:
            idle btn
            hover btn_hov
            ypos 697 + 100
            xpos 44 + 300
            action Function(reclut_shop_prev_page)
            

            
            

label reclut:
    $ actual_page.setload(0)
    call screen reclut_shop