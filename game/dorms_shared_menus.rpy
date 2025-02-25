define shared_dorm_skin_jumper = ""
define shared_doorm_wid = -1
define shared_dorm_skin_cb = "ads"

init python:
    def change_clothes(cid, wid):
        if shared_doorm_wid == 0:
            pass
        elif shared_doorm_wid == 1:
            kurumi_dorm_sk = cid
        
        found = l_filter(get_store("girls_data"), wid, 'id', True)["i"]
        cache_game.v["girls_data"][found]["actual_skin"] = cid
        Jump_To(shared_dorm_skin_jumper)


    def get_skins(wid):
        myskins = get_store("girls_data")
        skins = l_filter(girls_db, wid, 'id')["v"]["skins"]
        myskins = l_filter(myskins, wid , 'id')["v"]["skins"]
        skindata =[]
        
        for skin in myskins:
            skindata.append(l_filter(skins, skin , 'id')["v"])
        return skindata



screen  shared_doorm_inside_change_clothes:
    $ skins = get_skins(shared_doorm_wid)
    for i,skin in enumerate(skins):
        textbutton skin["name"][get_lang()] action Function(change_clothes, skin["id"],shared_doorm_wid) style_prefix "dorm_menu_":
            ypos 10+ (i * 50)
        if i == len(skins) - 1: 
            textbutton get_txt_db(dorm_txt["dorm_menu"]["ui"] , "back", False) action Function(Jump_To,shared_dorm_skin_cb) style_prefix "dorm_menu_":
                ypos 10+ ((i + 1) * 50)