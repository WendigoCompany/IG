screen reclut_shop:
    vbox:
        for g in girls_db:
            textbutton g.name action "ASD"


label reclut:
    call screen reclut_shop