init python:
    activegal = ""
    hovergal = ""
    convertGal = {"BE": "Honoka", "AE": "Shiori", "GTS": "Naomi", "FMG": "Akira", "WG": "Alice", "PRG": "Aida", "OTHER": "Other Character"}
    galleries = {"BE": Gallery(), "AE": Gallery(), "GTS": Gallery(), "FMG": Gallery(), "WG": Gallery(), "PRG": Gallery(), "OTHER": Gallery()}
    galImgList = {}
    galImgList["BE"] = [["BE000b", "GoodNotGreat", 995], ["BE010_pov1", "GoodNotGreat", 995], ["BE010_pov2", "GoodNotGreat", 995], ["BE010_pov3", "GoodNotGreat", 995], ["BE010_pov4", "GoodNotGreat", 995], ["BE010_pov5", "GoodNotGreat", 995], ["BE028", "GoodNotGreat", 995], ["BE028_fem", "GoodNotGreat", 995], ["BE031", "GoodNotGreat", 995], ["BE031b", "GoodNotGreat", 995], ["BE031c", "GoodNotGreat", 995], ["BE043_movie1", "GoodNotGreat", 995], ["BE043_movie2", "GoodNotGreat", 995], ["BE043_movie1_fem", "GoodNotGreat", 995], ["BE043_movie2_fem", "GoodNotGreat", 995]]
    galImgList["AE"] = [["AE000", "GoodNotGreat", 995], ["AE015", "GoodNotGreat", 995], ["AE024", "GoodNotGreat", 995], ["AE024b", "GoodNotGreat", 995], ["AE024c", "GoodNotGreat", 995], ["AE024d", "GoodNotGreat", 995], ["AE024e", "GoodNotGreat", 995], ["AE025", "GoodNotGreat", 995], ["AE050_behind1", "GoodNotGreat", 995], ["AE050_behind2", "GoodNotGreat", 995], ["AE050_behind3", "GoodNotGreat", 995], ["AE050_behind4", "GoodNotGreat", 995], ["AE050_behind5", "GoodNotGreat", 995], ["AE050_behind6", "GoodNotGreat", 995], ["AE050_bj1", "GoodNotGreat", 995], ["AE050_bj2", "GoodNotGreat", 995], ["AE050_bj3", "GoodNotGreat", 995], ["AE050_bj4", "GoodNotGreat", 995], ["AE050_sit1", "GoodNotGreat", 995], ["AE050_sit2", "GoodNotGreat", 995], ["AE050_spank1", "GoodNotGreat", 995], ["AE050_spank2", "GoodNotGreat", 995], ["AE050_spank3", "GoodNotGreat", 995], ["AE050_spank4", "GoodNotGreat", 995], ["AE053_mirror1", "GoodNotGreat", 995], ["AE053_mirror2", "GoodNotGreat", 995], ["AE074_snow1", "GoodNotGreat", 995], ["AE074_snow2", "GoodNotGreat", 995], ["AE074_snow3", "GoodNotGreat", 995], ["AE092_tv1", "GoodNotGreat", 995], ["AE092_tv2", "GoodNotGreat", 995], ["AE092_tv3", "GoodNotGreat", 995], ["AE098D_musicvideo1", "GoodNotGreat", 995], ["AE098D_musicvideo2", "GoodNotGreat", 995], ["AE098D_musicvideo3", "GoodNotGreat", 995], ["AE098D_musicvideo4", "GoodNotGreat", 995], ["AE098D_musicvideo5", "GoodNotGreat", 995]]
    galImgList["GTS"] = [["GTS000", "GoodNotGreat", 995], ["GTS024", "Ekkonshon", 1040], ["GTS025", "GoodNotGreat", 995], ["GTS035", "GoodNotGreat", 995], ["GTS044_stars1", "Ekkonshon", 1040], ["GTS044_stars2", "Ekkonshon", 1040], ["GTS046_upskirt", "GoodNotGreat", 995],  ["GTS046_hold1", "GoodNotGreat", 995], ["GTS046_hold2", "GoodNotGreat", 995], ["GTS046_hold3", "GoodNotGreat", 995]]
    galImgList["FMG"] = [["FMG016", "Sheepapp", 1050], ["FMG041", "Sheepapp", 1050], ["FMG050", "Sheepapp", 1050], ["FMG055", "Sheepapp", 1050], ["FMG056", "Sheepapp", 1050], ["FMG058", "Sheepapp", 1050], ["FMG061", "Sheepapp", 1050], ["FMG067", "Sheepapp", 1050]]
    galImgList["WG"] = [["WG000", "GoodNotGreat", 995], ["WG009", "GoodNotGreat", 995], ["WG039", "Radoon & Sparkcadia", 905], ["WG042", "MOLOT.CO", 1050], ["WG046", "GoodNotGreat", 995], ["WG047", "GoodNotGreat", 995], ["WG060S", "MOLOT.CO", 1050]]
    galImgList["PRG"] = [["PRG020", "Marrazan", 1055], ["PRG025", "Marrazan", 1055], ["PRG038", "Marrazan", 1055]]
    galImgList["OTHER"] = [["MC000", "GoodNotGreat", 995], ["RM000", "GoodNotGreat", 995], ["RM000_escape1", "GoodNotGreat", 995], ["RM000_escape2", "GoodNotGreat", 995], ["RM000_escape3", "GoodNotGreat", 995], ["MC003", "GoodNotGreat", 995]]

    for g in girllist:
        galleries[g].locked_button = im.Scale("Graphics/ui/gallery/gallery-lock.png", 266.67, 150, bilinear=True)
        galleries[g].transition = dissolve
        for i in galImgList[g]:
            galleries[g].button("cg " + i[0])
            galleries[g].unlock("cg " + i[0])
            galleries[g].image(Composite(
                (1280,720),
                (0,0), "Graphics/ui/gallery/" + i[0] + ".png",
                (i[2],690), Text("Art by: " + i[1], bold=True, color="#000000", style='outlined_text')))
            galleries[g].image("cg " + i[0])

    galleries["OTHER"].locked_button = im.Scale("Graphics/ui/gallery/gallery-lock.png", 266.67, 150, bilinear=True)
    galleries["OTHER"].transition = dissolve
    for i in galImgList["OTHER"]:
        galleries["OTHER"].button("cg " + i[0])
        galleries["OTHER"].unlock("cg " + i[0])
        galleries["OTHER"].image(Composite(
            (1280,720),
            (0,0), "Graphics/ui/gallery/" + i[0] + ".png",
            (i[2],690), Text("Art by: " + i[1], bold=True, color="#000000", style='outlined_text')))
        galleries["OTHER"].image("cg " + i[0])


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
        imagebutton:
            xalign 0.5
            yalign 0.5
            idle "Graphics/ui/gallery/gallery-OTHER.png"
            action [SetVariable("activegal", "OTHER"), ShowMenu("gallery")]
            hovered SetVariable("hovergal", "OTHER")
            unhovered SetVariable("hovergal", "")
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
                add galleries[activegal].make_button("cg " + galImgList[activegal][i][0], im.Scale("Graphics/ui/gallery/" + galImgList[activegal][i][0] + ".png", 266.67, 150, bilinear=True), xalign=0.5, yalign=0.5)
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
