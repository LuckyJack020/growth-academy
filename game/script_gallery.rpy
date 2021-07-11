init python:
    activegal = ""
    hovergal = ""
    convertGal = {"BE": "Honoka", "AE": "Shiori", "GTS": "Naomi", "FMG": "Akira", "WG": "Alice", "PRG": "Aida"}
    galleries = {"BE": Gallery(), "AE": Gallery(), "GTS": Gallery(), "FMG": Gallery(), "WG": Gallery(), "PRG": Gallery(), "RM": Gallery()}
    galImgList = {}
    galImgList["BE"] = ["BE000", "BE000b", "BE001", "BE010", "BE028", "BE028_fem", "BE031", "BE031b", "BE031c", "BE032"]
    galImgList["AE"] = ["AE000", "AE015", "AE024", "AE024b", "AE024c", "AE024d", "AE024e", "AE025", "AE050_behind1", "AE050_behind2", "AE050_behind3", "AE050_behind4", "AE050_behind5", "AE050_behind6", "AE050_bj1", "AE050_bj2", "AE050_bj3", "AE050_bj4", "AE050_sit1", "AE050_sit2", "AE050_spank1", "AE050_spank2", "AE050_spank3", "AE050_spank4", "AE074_snow1", "AE074_snow2", "AE074_snow3"]
    galImgList["GTS"] = ["GTS000", "GTS024", "GTS025", "GTS035"]
    galImgList["FMG"] = ["FMG016", "FMG041"]
    galImgList["WG"] = ["WG000", "WG009", "WG010", "WG046", "WG047"]
    galImgList["PRG"] = ["PRG020", "PRG020b", "PRG025", "PRG038"]
    galImgList["RM"] = ["RM000"]

    for g in girllist:
        galleries[g].locked_button = im.Scale("Graphics/ui/gallery/gallery-lock.png", 200, 150, bilinear=True)
        galleries[g].transition = dissolve
        for i in galImgList[g]:
            galleries[g].button("cg " + i)
            galleries[g].unlock_image("cg " + i)

screen galleryselect():
    tag menu
    add "Graphics/ui/bg/artroom_eve.png"
    add "gui/overlay/confirm.png"
    grid 3 3:
        xfill True
        yfill True
        for g in girllist:
            imagebutton:
                xalign 0.5
                yalign 0.5
                idle "Graphics/ui/gallery/gallery-" + g + ".png"
                action [SetVariable("activegal", g), ShowMenu("gallery")]
                hovered SetVariable("hovergal", g)
                unhovered SetVariable("hovergal", "")
        null
        textbutton "Return" action ShowMenu("extras") xalign 0.5 yalign 0.5
        null
    if hovergal != "":
        frame:
            xalign 0.9
            yalign 0.9
            xanchor 1.0
            background Solid(Color((0, 0, 0, 100)))
            text(convertGal[hovergal] + "'s Gallery")

screen gallery():
    tag menu
    add "Graphics/ui/bg/artroom_eve.png"
    add "gui/overlay/confirm.png"
    default page = 0
    grid 3 3:
        xfill True
        yfill True

        for i in range(page * 6, (page * 6) + 6):
            if i < len(galImgList[activegal]):
                add galleries[activegal].make_button("cg " + galImgList[activegal][i], im.Scale("Graphics/ui/gallery/" + galImgList[activegal][i] + ".png", 200, 150, bilinear=True), xalign=0.5, yalign=0.5)
            else:
                null

        if page > 0:
            textbutton "Last" action SetScreenVariable("page", page - 1) xalign 0.5 yalign 0.5
        else:
            null
        textbutton "Return" action ShowMenu("galleryselect") xalign 0.5 yalign 0.5
        if page < (math.ceil(len(galImgList[activegal]) / 6)):
            textbutton "Next" action SetScreenVariable("page", page + 1) xalign 0.5 yalign 0.5
        else:
            null
