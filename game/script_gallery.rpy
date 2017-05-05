init python:
    activegal = ""
    galleries = {"BE": Gallery(), "AE": Gallery(), "GTS": Gallery(), "FMG": Gallery(), "BBW": Gallery(), "PRG": Gallery()}
    galImgList = {}
    galImgList["BE"] = ["BE001"]
    galImgList["AE"] = []
    galImgList["GTS"] = []
    galImgList["FMG"] = []
    galImgList["BBW"] = ["BBW001"]
    galImgList["PRG"] = []
    
    for g in girllist:
        galleries[g].locked_button = im.Scale("Graphics/ui/galleryicon-imglocked.png", 200, 150, bilinear=True)
        for i in galImgList[g]:
            galleries[g].button("cg " + i)
            galleries[g].unlock_image("cg " + i)

screen galleryselect:
    tag menu

    grid 3 3:
        xfill True
        yfill True
        for g in girllist:
            imagebutton:
                xalign 0.5
                yalign 0.5
                idle "Graphics/ui/galleryicon-" + g + ".png"
                action [SetVariable("activegal", g), ShowMenu("gallery")]
        
        null
        textbutton "Return" action Return() xalign 0.5 yalign 0.5
        null

screen gallery:
    tag menu
    default page = 0
    grid 3 3:
        xfill True
        yfill True
        
        for i in range(page * 6, (page * 6) + 6):
            if i < len(galImgList[activegal]):
                add galleries[activegal].make_button("cg " + galImgList[activegal][i], im.Scale("Graphics/cg-" + galImgList[activegal][i] + ".png", 200, 150, bilinear=True), xalign=0.5, yalign=0.5)
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