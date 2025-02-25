# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    from game.girls.girls import girls_db
    from game.pymodules.store_data import get_store , new_game , girl_exist
    from game.girls.functions import get_skins , get_actual_skin
    from game.pymodules.moduleClasses import SimpleVars
    

    get_skins(1)

    # girl_exist()
    def Jump_To(lab):
        renpy.jump(lab)
        # jump_to.setload(lab)
        # return ""


define dorms_loop = False
define jump_to = SimpleVars()

# The game starts here.



# label jumper:
#     $ renpy.jump(jump_to.v)
    # if jump_to.v == "reclut":
    #     jump reclut
    # elif jump_to.v == "mm_lab":
    #     jump mm_lab
    # elif jump_to.v == "dorms":
    #     $ renpy.jump("dorms")
        

style dorm_menu_button:
    background "#006"
    insensitive_background "#444"
    hover_background "#00a"

style dorm_menu_text:
    color "#fff"
    hover_color "#c3d"

label start:
    $ new_game()
    # $ girl_exist()
    # # Show a background. This uses a placeholder by default, but you can
    # # add a file (named either "bg room.png" or "bg room.jpg") to the
    # # images directory to show it.

    # scene bg room

    # # This shows a character sprite. A placeholder is used, but you can
    # # replace it by adding a file named "eileen happy.png" to the images
    # # directory.

    # show eileen happy

    # # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"
    

    jump mm_lab
    # jump reclut

    # This ends the game.

    return
