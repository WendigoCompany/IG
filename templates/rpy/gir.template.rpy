init python:
    import game.girls.{module}


###################################################################################################[DORMS]##########################################################################################################################################################################################

#IMAGES

#IMAGES
# ENTRANDO A LA HABITACION
label dorm_w_{girl}:
# ENTRANDO A LA HABITACION

# MENU PRINCIPAL
screen dorm_menu_1_{girl}:
    vbox:
        textbutton get_txt_db(dorm_txt["dorm_menu"]["ui"] , "train", False) action Function(Jump_To, "cosa3") style_prefix "dorm_menu_"
        textbutton get_txt_db(dorm_txt["dorm_menu"]["ui"] , "change_clothes", False) action Function(Jump_To, "dorm_menu_changeClothes_{girl}") style_prefix "dorm_menu_"
        textbutton get_txt_db(dorm_txt["dorm_menu"]["ui"] , "back_room", False) action Function(Jump_To, "dorm_inside_gb_{girl}") style_prefix "dorm_menu_"
# MENU PRINCIPAL


# MENU CAMBIAR ROPA
label dorm_menu_changeClothes_{girl}:
    $ shared_doorm_wid = {id}
# MENU CAMBIAR ROPA


#ACTUALIZANDO LA SKIN
label dorm_inside_changing_{girl}:
#ACTUALIZANDO LA SKIN

#LLAMANDO AL MENU PRINCIPAL
label dorm_inside_{girl}:
    $ shared_dorm_skin_jumper = "dorm_inside_changing_{girl}"
    $ shared_dorm_skin_cb = "dorm_inside_{girl}"
#LLAMANDO AL MENU PRINCIPAL

#SALIDA DEL DORM
label dorm_inside_gb_{girl}:
#SALIDA DEL DORM

###################################################################################################[DORMS]##########################################################################################################################################################################################
