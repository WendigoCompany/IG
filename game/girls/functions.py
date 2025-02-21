from game.pymodules.store_data import get_store
from game.girls.girls import girls_db 

def compare_girls_unlocked():
        g_filtrated = []
        for g in girls_db:
            if not g["id"] in (get_store("g_unlocked")):
                g_filtrated.append(g)
        return g_filtrated