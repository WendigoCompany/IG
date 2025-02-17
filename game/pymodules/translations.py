import renpy.exports as renpy

TEXTS = {}


def get_lang():
    if not renpy.game.preferences.language:
        set_lang("en")
        return "en"
    return renpy.game.preferences.language


def set_lang(lang):
    renpy.change_language(lang)
    renpy.game.persistent.disclaimed = True
    # disclaimed("w", True)
    renpy.save_persistent()
    renpy.reload_script()
    # renpy.game.persistent.disclaimed = False


# ITERACIONES MULTIPLES => db = ["user"] , index=["k1","k2"]
def get_txt_db(db, index):
    try:
        lang = get_lang()
     
        holder = TEXTS.get(db)
        if not holder:
            return "EMPTY"
        if type(index) == tuple or type(index) == list:
            try:
                for i in index:
                    holder = holder[i]

                try:
                    return holder[lang]
                except Exception:
                    return "ERROR LANG"

            except Exception as err:
                print("********************************************")
                print("Error in get_text: FUERA DE LUGAR")
                print(err)
                print("********************************************")
                return "ERR"

        else:
            try:
                return holder[index][lang]
            except Exception:
                return "ERROR LANG2"

    except Exception:
        return "ERROR MAIN"