init python:
    def girl_hovered(index):
        Show("girl_prev")


# define girl_hovered = -1 
image bg frame = "/assets/frame.png"
style tx_button:
    color "#131212"
    size 10
    # font "KGSorryNotSorryChub.ttf"

screen girl_prev(index):
    vbox:
        text girls_db[index]["s_pre_desc"][lang]

screen reclut_shop:
    
    vbox:
        for i,g  in enumerate(girls_db):

            $ image = im.Scale("images/profiles/" + g["s_pre_img"][0], 200, 200)
            $ image_hov = im.Scale("images/profiles/" + g["s_pre_img"][1], 200, 200)
            vbox:
                
                imagebutton:
                    idle image
                    action "sad"
                    xpos 175 + (i * 30)
                    ypos 175 + (i * 30)
                    hover image_hov
                    # hovered Function(girl_hovered, i)
                    hovered Show("girl_prev", index = i )
                # imagebutton auto "images/profiles/" + g["s_pre_img"] action "ASD"


label reclut:
    call screen reclut_shop