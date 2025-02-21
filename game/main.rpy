

init python:
    def calltext():
        Show("mm_screen_help",txt="hola")

screen mm_screen():
    $ pp_rcl_on = im.Scale("/assets/mm_map_point_recl_on.png", 100, 160);
    $ pp_rcl_off = im.Scale("/assets/mm_map_point_recl_off.png", 100, 160);
    add "/menu_backgrounds/mm_mañana.png"
    imagebutton:
        ypos 450
        idle pp_rcl_off
        hover pp_rcl_on
        xpos 900
        action Function(calltext)
        hovered Function(calltext)

screen mm_screen_help(txt="2"):
    text txt


screen mm_screen_alpha:
    textbutton "RECLUTAMIENTO" action Function(Jump_To, "reclut") ypos 0
    textbutton "DORMS" action Function(Jump_To, "dorms") ypos 100

image bg mm_lab = "/menu_backgrounds/mm_dia.png"

label mm_lab:
    # call screen mm_screen
    hide image "/menu_backgrounds/obcs_50.png"
    show bg mm_lab with dissolve
    call screen mm_screen_alpha
    # jump jumper
    # jump reclut
    # "HOLA"


