from game.pymodules.store_data import get_store
from game.girls.girls import girls_db 

def compare_girls_locked(rever=False):
        g_filtrated = []
        for g in girls_db:
            if (g["id"] in (get_store("g_unlocked"))) == rever:
                g_filtrated.append(g)
        return g_filtrated


