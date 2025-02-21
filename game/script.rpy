# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    from game.girls.girls import girls_db
    from game.pymodules.store_data import get_store , new_game
    from game.pymodules.moduleClasses import SimpleVars

    def Jump_To(lab):
        renpy.jump(lab)
        # jump_to.setload(lab)
        # return ""

define e = Character("Eileen")

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
        

label start:
    $ new_game()
    
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
