style tx_button:
    color "#131212"
    size 10
    # font "KGSorryNotSorryChub.ttf"
screen reclut_shop:
    vbox:
        for g in girls_db:

            $ image = im.Scale("images/profiles/" + g["s_pre_img"], 200, 200)
            vbox:
                imagebutton:
                    idle image
                    action "sad"
                # imagebutton auto "images/profiles/" + g["s_pre_img"] action "ASD"
                textbutton g["name"] :
                    text_style "tx_button"
                    action "ASD"


label reclut:
    call screen reclut_shop