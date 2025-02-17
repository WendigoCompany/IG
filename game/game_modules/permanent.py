import renpy.exports as renpy


try:
    if renpy.game.persistent.game_params is None:
        renpy.game.persistent.game_params = {
            "prev": False
        }
        print("Params creado!")
except Exception as pererror:
    print("ERROR CARGANDO PERMANENT")
    print(pererror)

def update_permanent(data, perdb  , save=False):
    if perdb == 'game_params':
        renpy.game.persistent.game_params.update(data)

    if save:
         renpy.save_persistent()

    