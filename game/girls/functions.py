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



        

    # for file in py_files:
    #     if not os.path.isdir(route_py + file):
    #         print(file)

    # for file in rpy_files:
    #     if not os.path.isdir(route_rpy + file):
    #         print(file)
        
   

