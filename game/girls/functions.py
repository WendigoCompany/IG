from game.pymodules.store_data import get_store, cache_game
from game.girls.girls import girls_db
from game.girls.girlsDict import girls_dict
from game.pymodules.moduleClasses import l_filter
import os
import inspect





def compare_girls_locked(rever=False):
        g_filtrated = []
        for g in girls_db:
            if (g["id"] in (get_store("g_unlocked"))) == rever:
                g_filtrated.append(g)
        return g_filtrated


def get_skins(wid):
    myskins = get_store("girls_data")
    skins = l_filter(girls_db, wid, 'id')["v"]["skins"]
    
    found = l_filter(myskins, wid , 'id')
    

        

    # for file in py_files:
    #     if not os.path.isdir(route_py + file):
    #         print(file)

    # for file in rpy_files:
    #     if not os.path.isdir(route_rpy + file):
    #         print(file)
        
   

