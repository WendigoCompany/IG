# import renpy.exports as renpy
# from game.pymodules.test import see_module
# from game.pymodules.translations import get_txt_db

# import copy


# game_store = {}

# ############################################################################################################

# try:
#     if renpy.game.persistent.game_store is None:
#         renpy.game.persistent.game_store = {}
#         print("Persistent creado!")
# except Exception as pererror:
#     print("ERROR CARGANDO PERMANENT")
#     print(pererror)

# ############################################################################################################

# old_save = copy.deepcopy(renpy.save)


# def new_save(*args, **kwargs):
#     game_store = {"NAM" : "asd"}
#     if renpy.game.persistent.game_store.get("saves") is None:
#         # print(1)

#         renpy.game.persistent.game_store["saves"] = {
#             args[0]: game_store
#             }
#         # renpy.save_persistent()
#         old_save(args[0], **kwargs)

#     else:
#         renpy.game.persistent.game_store["saves"].update({args[0]: game_store})
#         old_save(args[0], **kwargs)
#     renpy.save_persistent()
#     return ""
#     # old_save(args[0], **kwargs)
#     # regis_save_entry(args[0])


# # auto
# renpy.save = new_save


# ############################################################################################################


# old_load = copy.deepcopy(renpy.load)


# def new_load(*args, **kwargs):
#     global game_store
#     game_store = renpy.game.persistent.game_store["saves"].get(args[0])
#     old_load(args[0])
#     return ""


# renpy.load = new_load


############################################################################################################
import renpy.exports as renpy
from  game.pymodules.test  import see_module
from  game.pymodules.moduleClasses  import SimpleVars
import copy



base_game ={
    "g_unlocked" : [0],
    "girls_data": [
        {
            "id" : 0,
            "skins": [],
            "s_params" : {},
        }
    ]
}

cache_game = SimpleVars()
cache_game.v = base_game

try:
    if renpy.game.persistent.game_store is None:
        renpy.game.persistent.game_store = {}
        print("Persistent creado!")
        
    # renpy.game.persistent.game_cache = base_game
    print("Cache creado!")
except Exception as pererror:
    print("ERROR CARGANDO PERMANENT")
    print(pererror)

############################################################################################################
def get_store(key):
    # if renpy.game.persistent.game_cache.get(key):
    #     if not key:
    #         renpy.game.persistent.game_cache
    #     return renpy.game.persistent.game_cache.get(key)
    # else:
    #     return None
    if cache_game.v.get(key):
        if not key:
            cache_game.v
        return cache_game.v.get(key)
    else:
        return None
############################################################################################################

old_save = copy.deepcopy(renpy.save)


def new_save(*args, **kwargs):
    if renpy.game.persistent.game_store.get("saves") is None:
        renpy.game.persistent.game_store["saves"] = {
            # args[0]: renpy.game.persistent.game_cache
            args[0]: cache_game.v
            }
        
        old_save(args[0], **kwargs)

    else:
        # renpy.game.persistent.game_store["saves"].update({args[0]: renpy.game.persistent.game_cache})
        renpy.game.persistent.game_store["saves"].update({args[0]: cache_game.v})
        old_save(args[0], **kwargs)
    renpy.save_persistent()
    return ""


# auto
renpy.save = new_save


############################################################################################################



loaded = SimpleVars()


old_load = copy.deepcopy(renpy.load)

def new_load(*args, **kwargs):  
    loaded.setload(True)
    # renpy.game.persistent.game_cache = renpy.game.persistent.game_store["saves"].get(args[0])
    cache_game.setload(renpy.game.persistent.game_store["saves"].get(args[0]))
    old_load(args[0])
    return ""


renpy.load = new_load


############################################################################################################

def new_game():
    if not loaded.v:
        # renpy.game.persistent.game_cache = base_game
        cache_game.setload(base_game)
    loaded.setload(False)