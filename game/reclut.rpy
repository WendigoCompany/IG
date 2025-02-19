init python:
    from game.pymodules.moduleClasses import SimpleVars
    from game.girls.girls import girls_db
    
    max_per_page= 9
    max_per_col= 3
    actual_page= SimpleVars()


    def reclut_shop_next_page():
        # Show("girl_prev")
        newval = actual_page.v + 1
        if (len(girls_db) // max_per_page)  >= newval: 
            actual_page.setload(newval)
            Show("reclut_shop")

    def reclut_shop_prev_page():
        newval = actual_page.v - 1
        if 0  <= newval: 
            actual_page.setload(newval)
            Show("reclut_shop")


    def girl_hovered(index):
        Show("girl_prev")
    
    def recl_positon(i, pos):
        if pos == "y":
            base = -(i * 200)
            y = base + 31
            y += (i // max_per_col) * 215 
            return y


style tx_button:
    color "#131212"
    size 10
    # font "KGSorryNotSorryChub.ttf"


screen girl_prev(index):
    vbox:
        text girls_db[index]["s_pre_desc"][lang]

screen reclut_shop:
    add "/assets/reclutamiento.png"
    $ g_visible = []
    for i,g in enumerate(girls_db):
        $ print(get_store("g_unlocked"))
        if not g["id"] in (get_store("g_unlocked")) and i // max_per_page == actual_page.v: 
            $ g_visible.append(g)
    vbox:
        for i,g  in enumerate(g_visible):

            $ image = im.Scale("images/profiles/" + g["reclut"]["s_pre_img"][0], 200, 200)
            $ image_hov = im.Scale("images/profiles/" + g["reclut"]["s_pre_img"][1], 200, 200)
            vbox:
                box_wrap True
                imagebutton:
                    idle image
                    action Function(reclut_shop_prev_page)
                    ypos recl_positon(i, "y")
                    xpos 0
                    hover image_hov
                    # hovered Function(girl_hovered, i)
                # imagebutton auto "images/profiles/" + g["s_pre_img"] action "ASD"


    vbox:
        $ btn = im.Scale("images/assets/flecha_next.png" , 200, 50)
        $ btn_hov = im.Scale("images/assets/flecha_next_hover.png" , 200, 50)
        imagebutton:
            idle btn
            hover btn_hov
            ypos 697
            xpos 474
            action Function(reclut_shop_next_page)


    vbox:
        $ btn = im.Scale("images/assets/menu.png" , 200, 50)
        $ btn_hov = im.Scale("images/assets/menu_hover.png" , 200, 50)
        imagebutton:
            idle btn
            hover btn_hov
            ypos 697
            xpos 259
            action Function(reclut_shop_prev_page)

    vbox:
        $ btn = im.Scale("images/assets/flecha_prev.png" , 200, 50)
        $ btn_hov = im.Scale("images/assets/flecha_prev_hover.png" , 200, 50)
        imagebutton:
            idle btn
            hover btn_hov
            ypos 697
            xpos 44
            action Function(reclut_shop_prev_page)
            

            
            

label reclut:
    $ actual_page.setload(0)
    call screen reclut_shop