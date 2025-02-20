init python:
    from game.pymodules.moduleClasses import SimpleVars, l_filter
    from game.girls.girls import girls_db
    
    max_per_page= 9
    max_per_col= 3
    actual_page= SimpleVars()
    previewed_girl =SimpleVars()
    previewed_girl.v =[-1]
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


    def recl_update_preview(ind):
        previewed_girl.setload([previewed_girl.v[0],ind])
        Show("reclut_shop", True)

    def recl_show_girl_info(index):
        previewed_girl.setload([index,0])
        Show("reclut_shop", True)
    
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

define g_visible =[]
screen reclut_shop(preview=False):
    add "/assets/reclutamiento_final3.png" xpos 300 ypos 100
    # add "/assets/reclutamiento.png" xpos 300 ypos 100
    if not preview:
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
        
    $ marco = im.Scale("/assets/marco_preview.png", 460, 460)
    add marco xpos 1046 ypos 214
    if not previewed_girl.v[0] == -1:
        
        $ girl_preview = im.Scale("/profiles/" + (l_filter(girls_db,previewed_girl.v[0] , "id", i))["v"]["reclut"]["preview"][previewed_girl.v[1]], 440, 440)
        add girl_preview xpos 1056 ypos 230

        vbox:
            $ btn = im.Scale("images/assets/cloth.png" , 77*2, 60)
            $ btn_hov = im.Scale("images/assets/cloth_hover.png" , 77*2, 60)
            imagebutton:
                idle btn
                hover btn_hov
                xpos 1045 
                ypos 129 + 10
                action Function(recl_update_preview,0)
        vbox:
            $ btn = im.Scale("images/assets/under.png" , 77*2, 60)
            $ btn_hov = im.Scale("images/assets/under_hover.png" , 77*2, 60)
            imagebutton:
                idle btn
                hover btn_hov   
                xpos 1045 +77*2
                ypos 129 + 10
                action Function(recl_update_preview,1)
        vbox:
            $ btn = im.Scale("images/assets/nude.png" , 77*2, 60)
            $ btn_hov = im.Scale("images/assets/nude_hover.png" , 77*2, 60)
            imagebutton:
                idle btn
                hover btn_hov
                xpos 1045 +77*2+77*2
                ypos 129 + 10
                action Function(recl_update_preview,2)
          
image bg reclutamiento_bg1 = "/menu_backgrounds/bg_reclutamiento.png"
image bg reclutamiento_bg2 = "/menu_backgrounds/bg_reclutamiento_2.png"

label reclut:
    show bg reclutamiento_bg1 with dissolve
    $ renpy.pause(.2)
    show bg reclutamiento_bg2 with dissolve
    $ renpy.pause(.2)
    $ actual_page.setload(0)
    call screen reclut_shop with dissolve
