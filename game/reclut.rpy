init python:
    def girl_hovered(index):
        Show("girl_prev")
    
    def recl_positon(i, pos):
        if pos == "y":
            return [[0,-200,-200]][i // 3][i]

# image bg frame = "/assets/frame.png"
style tx_button:
# define girl_hovered =
    color "#131212"
    size 10
    # font "KGSorryNotSorryChub.ttf"

screen girl_prev(index):
    vbox:
        text girls_db[index]["s_pre_desc"][lang]

screen reclut_shop:

    add "/assets/reclutamiento.png"
    vbox:
        for i,g  in enumerate(girls_db):

            $ image = im.Scale("images/profiles/" + g["s_pre_img"][0], 200, 200)
            $ image_hov = im.Scale("images/profiles/" + g["s_pre_img"][1], 200, 200)
            vbox:
                box_wrap True
                imagebutton:
                    idle image
                    action "sad"
                    xpos 0
                    ypos recl_positon(i, "y") 
                    hover image_hov
                    # hovered Function(girl_hovered, i)
                # imagebutton auto "images/profiles/" + g["s_pre_img"] action "ASD"


label reclut:
    call screen reclut_shop