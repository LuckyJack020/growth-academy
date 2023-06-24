init python:
    activegal = ""
    hovergal = ""
    convertGal = {"BE": "Honoka", "AE": "Shiori", "GTS": "Naomi", "FMG": "Akira", "WG": "Alice", "PRG": "Aida", "OTHER": "Other Character"}
    galleries = {"BE": Gallery(), "AE": Gallery(), "GTS": Gallery(), "FMG": Gallery(), "WG": Gallery(), "PRG": Gallery(), "OTHER": Gallery()}
    galImgList = {}
    galImgList["BE"] = [["BE000b", "GoodNotGreat", 995, "sfw"], ["BE010_pov1", "GoodNotGreat", 995, "sfw"], ["BE010_pov2", "GoodNotGreat", 995, "sfw"], ["BE010_pov3", "GoodNotGreat", 995, "sfw"], ["BE010_pov4", "GoodNotGreat", 995, "sfw"], ["BE010_pov5", "GoodNotGreat", 995, "sfw"], ["BE020_date1", "Vespa", 1100, "sfw"], ["BE020_date2", "Vespa", 1100, "sfw"], ["BE020_date3", "Vespa", 1100, "sfw"], ["BE020_date4", "Vespa", 1100, "sfw"], ["BE020_date5", "Vespa", 1100, "sfw"], ["BE020_date6", "Vespa", 1100, "sfw"], ["BE020_date7", "Vespa", 1100, "sfw"], ["BE028", "GoodNotGreat", 995, "sfw"], ["BE028_fem", "GoodNotGreat", 995, "sfw"], ["BE031", "GoodNotGreat", 995, "nsfw"], ["BE031b", "GoodNotGreat", 995, "nsfw"], ["BE031c", "GoodNotGreat", 995, "sfw"], ["BE043_movie1", "GoodNotGreat", 995, "sfw"], ["BE043_movie2", "GoodNotGreat", 995, "sfw"], ["BE043_movie1_fem", "GoodNotGreat", 995, "sfw"], ["BE043_movie2_fem", "GoodNotGreat", 995, "sfw"], ["BE049", "Oct-Oppai", 1045, "sfw"]]
    galImgList["AE"] = [["AE_Icon", "Sheepapp", 1050, "icon"], ["AE000", "GoodNotGreat", 995, "sfw"], ["AE015", "GoodNotGreat", 995, "nsfw"], ["AE024", "GoodNotGreat", 995, "nsfw"], ["AE024b", "GoodNotGreat", 995, "nsfw"], ["AE024c", "GoodNotGreat", 995, "nsfw"], ["AE024d", "GoodNotGreat", 995, "nsfw"], ["AE024e", "GoodNotGreat", 995, "sfw"], ["AE025", "GoodNotGreat", 995, "sfw"], ["AE050_behind1", "GoodNotGreat", 995, "nsfw"], ["AE050_behind2", "GoodNotGreat", 995, "nsfw"], ["AE050_behind3", "GoodNotGreat", 995, "nsfw"], ["AE050_behind4", "GoodNotGreat", 995, "nsfw"], ["AE050_behind5", "GoodNotGreat", 995, "nsfw"], ["AE050_behind6", "GoodNotGreat", 995, "nsfw"], ["AE050_bj1", "GoodNotGreat", 995, "nsfw"], ["AE050_bj2", "GoodNotGreat", 995, "nsfw"], ["AE050_bj3", "GoodNotGreat", 995, "nsfw"], ["AE050_bj4", "GoodNotGreat", 995, "nsfw"], ["AE050_sit1", "GoodNotGreat", 995, "nsfw"], ["AE050_sit2", "GoodNotGreat", 995, "nsfw"], ["AE050_spank1", "GoodNotGreat", 995, "nsfw"], ["AE050_spank2", "GoodNotGreat", 995, "nsfw"], ["AE050_spank3", "GoodNotGreat", 995, "nsfw"], ["AE050_spank4", "GoodNotGreat", 995, "nsfw"], ["AE053_mirror1", "GoodNotGreat", 995, "sfw"], ["AE053_mirror2", "GoodNotGreat", 995, "sfw"], ["AE074_snow1", "GoodNotGreat", 995, "sfw"], ["AE074_snow2", "GoodNotGreat", 995, "nsfw"], ["AE074_snow3", "GoodNotGreat", 995, "sfw"], ["AE092_tv1", "GoodNotGreat", 995, "sfw"], ["AE092_tv2", "GoodNotGreat", 995, "sfw"], ["AE092_tv3", "GoodNotGreat", 995, "sfw"], ["AE098D_musicvideo1", "GoodNotGreat", 995, "nsfw"], ["AE098D_musicvideo2", "GoodNotGreat", 995, "nsfw"], ["AE098D_musicvideo3", "GoodNotGreat", 995, "nsfw"], ["AE098D_musicvideo4", "GoodNotGreat", 995, "nsfw"], ["AE098D_musicvideo5", "GoodNotGreat", 995, "sfw"]]
    galImgList["GTS"] = [["GTS_Icon", "Sheepapp", 1050, "icon"], ["GTS000", "GoodNotGreat", 995, "sfw"], ["GTS024", "Ekkonshon", 1040, "sfw"], ["GTS025", "GoodNotGreat", 995, "sfw"], ["GTS035", "GoodNotGreat", 995, "sfw"], ["GTS043_planks1", "Vespa", 1100, "sfw"], ["GTS044_stars1", "Ekkonshon", 1040, "sfw"], ["GTS044_stars2", "Ekkonshon", 1040, "sfw"], ["GTS046_upskirt", "GoodNotGreat", 995, "nsfw"],  ["GTS046_hold1", "GoodNotGreat", 995, "sfw"], ["GTS046_hold2", "GoodNotGreat", 995, "nsfw"], ["GTS046_hold3", "GoodNotGreat", 995, "nsfw"], ["GTS050_nightmare1", "Ekkonshon", 1040, "nsfw"]]
    galImgList["FMG"] = [["FMG_Icon", "Sheepapp", 1050, "icon"], ["FMG016", "Sheepapp", 1050, "sfw"], ["FMG041", "Sheepapp", 1050, "sfw"], ["FMG050", "Sheepapp", 1050, "nsfw"], ["FMG055", "Sheepapp", 1050, "sfw"], ["FMG056", "Sheepapp", 1050, "sfw"], ["FMG058", "Sheepapp", 1050, "sfw"], ["FMG058_pose1", "Sheepapp", 1050, "sfw"], ["FMG058_pose2", "Sheepapp", 1050, "sfw"], ["FMG058_pose3", "Sheepapp", 1050, "sfw"], ["FMG061", "Sheepapp", 1050, "sfw"], ["FMG067", "Sheepapp", 1050, "sfw"], ["FMG077", "Sheepapp", 1050, "nsfw"], ["FMG082", "Sheepapp", 1050, "sfw"]]
    galImgList["WG"] = [["WG_Icon", "Sheepapp", 1050, "icon"], ["WG000", "GoodNotGreat", 995, "sfw"], ["WG009", "GoodNotGreat", 995, "sfw"], ["WG039", "Radoon & Sparkcadia", 905, "sfw"], ["WG042", "MOLOT.CO", 1050, "sfw"], ["WG046", "GoodNotGreat", 995, "sfw"], ["WG047", "GoodNotGreat", 995, "sfw"], ["WG060S", "MOLOT.CO", 1050, "sfw"], ["WG070", "MochiiStar", 1035, "sfw"], ["WG071", "MochiiStar", 1035, "nsfw"], ["WG079_drawing1", "Oct-Oppai", 1045, "sfw"], ["WG079_drawing2", "Oct-Oppai", 1045, "sfw"]]
    galImgList["PRG"] = [["PRG_Icon", "Sheepapp", 1050, "icon"], ["PRG020", "Marrazan", 1055, "sfw"], ["PRG025", "Marrazan", 1055, "nsfw"], ["PRG028a", "Marrazan & Diant707", 905, "custom"], ["PRG028b", "Marrazan & Diant707", 905, "custom"], ["PRG028c", "Marrazan & Diant707", 905, "custom"], ["PRG028d", "Marrazan & Diant707", 905, "custom"], ["PRG038", "Marrazan", 1055, "sfw"], ["PRG038_poster", "GoodNotGreat", 995, "sfw"]]
    galImgList["OTHER"] = [["MC000", "GoodNotGreat", 995, "sfw"], ["RM000", "GoodNotGreat", 995, "sfw"], ["RM000_escape1", "GoodNotGreat", 995, "sfw"], ["RM000_escape2", "GoodNotGreat", 995, "sfw"], ["RM000_escape3", "GoodNotGreat", 995, "sfw"], ["MC003", "GoodNotGreat", 995, "sfw"]]

    for g in girllist:
        galleries[g].locked_button = im.Scale("Graphics/ui/gallery/gallery-lock.png", 266.67, 150, bilinear=True)
        galleries[g].transition = dissolve
        for i in galImgList[g]:
            if i[3] == "icon":
                galleries[g].button("cg " + i[0])
                galleries[g].image(Composite(
                    (1280,720),
                    (0,0), "Graphics/ui/gallery/" + i[0] + ".png",
                    (i[2],690), Text("Art by: " + i[1], bold=True, color="#000000", style='outlined_text')))
                galleries[g].image("Graphics/ui/gallery/" + i[0] + ".png")
            elif i[3] == "sfw":
                galleries[g].button("cg " + i[0])
                galleries[g].unlock("cg " + i[0])
                galleries[g].image(Composite(
                    (1280,720),
                    (0,0), "Graphics/ui/gallery/" + i[0] + ".png",
                    (i[2],690), Text("Art by: " + i[1], bold=True, color="#000000", style='outlined_text')))
                galleries[g].image("cg " + i[0])
            elif i[3] == "custom":
                galleries[g].button("cg " + i[0])
                galleries[g].condition("persistent.unlock_cg" + i[0])
                galleries[g].image(Composite(
                    (1280,720),
                    (0,0), "Graphics/ui/gallery/" + i[0] + ".png",
                    (i[2],690), Text("Art by: " + i[1], bold=True, color="#000000", style='outlined_text')))
                galleries[g].image("cg " + i[0])
            elif i[3] == "nsfw":
                galleries[g].button("cg " + i[0])
                galleries[g].condition("persistent.unlock_cg" + i[0])
                galleries[g].image(Composite(
                    (1280,720),
                    (0,0), "Graphics/ui/gallery/" + i[0] + ".png",
                    (i[2],690), Text("Art by: " + i[1], bold=True, color="#000000", style='outlined_text')))
                galleries[g].image("cg " + i[0])

    galleries["OTHER"].locked_button = im.Scale("Graphics/ui/gallery/gallery-lock.png", 266.67, 150, bilinear=True)
    galleries["OTHER"].transition = dissolve
    for i in galImgList["OTHER"]:
        if i[3] == "sfw":
            galleries["OTHER"].button("cg " + i[0])
            galleries["OTHER"].unlock("cg " + i[0])
            galleries["OTHER"].image(Composite(
                (1280,720),
                (0,0), "Graphics/ui/gallery/" + i[0] + ".png",
                (i[2],690), Text("Art by: " + i[1], bold=True, color="#000000", style='outlined_text')))
            galleries["OTHER"].image("cg " + i[0])
        elif i[3] == "nsfw":
            galleries["OTHER"].button("cg " + i[0])
            galleries["OTHER"].condition("persistent.unlock_cg" + i[0])
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
        textbutton "Return" action ShowMenu("extras") xalign 0.5 yalign 0.5 text_outlines [ (2, "#000000", 0, 0) ] text_size 30 text_color "#FFFFFF" text_hover_color "#b1b1b1"
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
            if i < len(galImgList[activegal]) and (galImgList[activegal][i][3] == "sfw" or galImgList[activegal][i][3] == "icon" or galImgList[activegal][i][3] == "custom"):
                add galleries[activegal].make_button("cg " + galImgList[activegal][i][0], im.Scale("Graphics/ui/gallery/" + galImgList[activegal][i][0] + ".png", 266.67, 150, bilinear=True), xalign=0.5, yalign=0.5)
            elif i < len(galImgList[activegal]) and isNSFW():
                add galleries[activegal].make_button("cg " + galImgList[activegal][i][0], im.Scale("Graphics/ui/gallery/" + galImgList[activegal][i][0] + ".png", 266.67, 150, bilinear=True), xalign=0.5, yalign=0.5)
            elif i < len(galImgList[activegal]) and not isNSFW():
                add im.Scale("Graphics/ui/gallery/gallery-nsfw.png", 266.67, 150, xalign=0.5, yalign=0.5, bilinear=True)
            else:
                null

        if page > 0:
            textbutton "Last" action SetScreenVariable("page", page - 1) xalign 0.5 yalign 0.5 text_outlines [ (2, "#000000", 0, 0) ] text_size 30 text_color "#FFFFFF" text_hover_color "#b1b1b1"
        else:
            null
        textbutton "Return" action ShowMenu("galleryselect") xalign 0.5 yalign 0.5 text_outlines [ (2, "#000000", 0, 0) ] text_size 30 text_color "#FFFFFF" text_hover_color "#b1b1b1"
        if page < (math.ceil(len(galImgList[activegal]) / 6)) - 1:
            textbutton "Next" action SetScreenVariable("page", page + 1) xalign 0.5 yalign 0.5 text_outlines [ (2, "#000000", 0, 0) ] text_size 30 text_color "#FFFFFF" text_hover_color "#b1b1b1"
        else:
            null
