# This RPY is a base template on defining songs manually that aren't located in
# the track folder. Use the commented sample below as a base to manually
# add songs from your projects to here. (MP3/OGG only ATM)

init python:
    # imports the OST library. Leave this as-is.
    import ost

    theme_AE = ost.soundtrack(
        name = "A Secret Place",
        path = "Audio/BGM/scene_AE.ogg",
        priority = 1,
        author = "Post-Bop",
        description = "Shiori's Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_AE.ogg")
    )
    ost.manualDefineList.append(theme_AE)

    theme_BE = ost.soundtrack(
        name = "I'm Just Motivated",
        path = "Audio/BGM/scene_BE.mp3",
        priority = 1,
        author = "Yoshiki ARA",
        description = "Honoka's Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_BE.mp3")
    )
    ost.manualDefineList.append(theme_BE)

    theme_GTS = ost.soundtrack(
        name = "Hidden Meadow",
        path = "Audio/BGM/scene_GTS.ogg",
        priority = 1,
        author = "Post-Bop",
        description = "Naomi's Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_GTS.ogg")
    )
    ost.manualDefineList.append(theme_GTS)

    theme_FMG = ost.soundtrack(
        name = "Pump It",
        path = "Audio/BGM/scene_FMG.ogg",
        priority = 1,
        author = "Post-Bop",
        description = "Akira's Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_FMG.ogg")
    )
    ost.manualDefineList.append(theme_FMG)

    theme_PRG = ost.soundtrack(
        name = "Quiet Wandering",
        path = "Audio/BGM/scene_PRG.ogg",
        priority = 1,
        author = "Post-Bop",
        description = "Aida's Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_PRG.ogg")
    )
    ost.manualDefineList.append(theme_PRG)

    theme_WG = ost.soundtrack(
        name = "Aristocratic Opulence",
        path = "Audio/BGM/scene_WG.ogg",
        priority = 1,
        author = "Post-Bop",
        description = "Alice's Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_WG.ogg")
    )
    ost.manualDefineList.append(theme_WG)

    theme_MC = ost.soundtrack(
        name = "Our Protagonist",
        path = "Audio/BGM/scene_MC.ogg",
        priority = 1,
        author = "Post-Bop",
        description = "Keisuke's Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_MC.ogg")
    )
    ost.manualDefineList.append(theme_MC)

    daymenu = ost.soundtrack(
        name = "Choose Your Story",
        path = "Audio/BGM/menu_daymenu.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Map Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/menu_daymenu.ogg")
    )
    ost.manualDefineList.append(daymenu)

    theme_RM = ost.soundtrack(
        name = "Roommate",
        path = "Audio/BGM/scene_RM.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Daichi's Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_RM.ogg")
    )
    ost.manualDefineList.append(theme_RM)

    PRGDrama = ost.soundtrack(
        name = "Small Moments",
        path = "Audio/BGM/scene_PRGdrama.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Aida's Drama Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_PRGdrama.ogg")
    )
    ost.manualDefineList.append(PRGDrama)

    PRGChallenge = ost.soundtrack(
        name = "The Challenge",
        path = "Audio/BGM/scene_PRGchallenge.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Aida's Challenge Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_PRGchallenge.ogg")
    )
    ost.manualDefineList.append(PRGChallenge)

    Bittersweet = ost.soundtrack(
        name = "Bittersweet",
        path = "Audio/BGM/scene_bittersweet.mp3",
        priority = 2,
        author = "Post-Bop",
        description = "Bitter Mood Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_bittersweet.mp3")
    )
    ost.manualDefineList.append(Bittersweet)

    Busy = ost.soundtrack(
        name = "Busy",
        path = "Audio/BGM/scene_busy.mp3",
        priority = 2,
        author = "Post-Bop",
        description = "Bustlin' Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_busy.mp3")
    )
    ost.manualDefineList.append(Busy)

    Festival = ost.soundtrack(
        name = "Festival",
        path = "Audio/BGM/scene_festival.mp3",
        priority = 3,
        author = "Post-Bop",
        description = "Town Festival Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_festival.mp3")
    )
    ost.manualDefineList.append(Festival)

    Higheredu = ost.soundtrack(
        name = "Higher Education",
        path = "Audio/BGM/scene_higheredu.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Scholarly Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_higheredu.ogg")
    )
    ost.manualDefineList.append(Higheredu)

    Memory = ost.soundtrack(
        name = "Memories",
        path = "Audio/BGM/memories.mp3",
        priority = 2,
        author = "Post-Bop",
        description = "Reminiscing Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/memories.mp3")
    )
    ost.manualDefineList.append(Memory)

    Rainy = ost.soundtrack(
        name = "Rain",
        path = "Audio/BGM/scene_rain.mp3",
        priority = 2,
        author = "Post-Bop",
        description = "Somber Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_rain.mp3")
    )
    ost.manualDefineList.append(Rainy)

    Requi = ost.soundtrack(
        name = "Requiem",
        path = "Audio/BGM/requiem.mp3",
        priority = 2,
        author = "Post-Bop",
        description = "Resolved Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/requiem.mp3")
    )
    ost.manualDefineList.append(Requi)

    HallowHall = ost.soundtrack(
        name = "Hallowed Halls",
        path = "Audio/BGM/hallowedhalls.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Main Menu Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/hallowedhalls.ogg")
    )
    ost.manualDefineList.append(HallowHall)

    DayBy = ost.soundtrack(
        name = "Day By Day",
        path = "Audio/BGM/scene_daybyday.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Casual Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_daybyday.ogg")
    )
    ost.manualDefineList.append(DayBy)

    SunSet = ost.soundtrack(
        name = "Sunset",
        path = "Audio/BGM/scene_sunset.mp3",
        priority = 3,
        author = "Post-Bop",
        description = "Soothing Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_sunset.mp3")
    )
    ost.manualDefineList.append(SunSet)

    SchoolDay = ost.soundtrack(
        name = "Schoolday",
        path = "Audio/BGM/scene_schoolday.mp3",
        priority = 2,
        author = "Post-Bop",
        description = "Classroom Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_schoolday.mp3")
    )
    ost.manualDefineList.append(SchoolDay)

    SunSet = ost.soundtrack(
        name = "Sunset",
        path = "Audio/BGM/scene_sunset.mp3",
        priority = 3,
        author = "Post-Bop",
        description = "Soothing Music",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_sunset.mp3")
    )
    ost.manualDefineList.append(SunSet)

    HallWay = ost.soundtrack(
        name = "Hallway",
        path = "Audio/BGM/scene_hallway.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Academy Campus Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_hallway.ogg")
    )
    ost.manualDefineList.append(HallWay)

    Tense = ost.soundtrack(
        name = "Tension",
        path = "Audio/BGM/tension.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Conflicted Music",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(Tense)

    TwiBright = ost.soundtrack(
        name = "Bright Twilight",
        path = "Audio/BGM/twilightBright.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Twilight (Happy)",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/twilightBright.ogg")
    )
    ost.manualDefineList.append(TwiBright)

    TwiAmb = ost.soundtrack(
        name = "Ambient Twilight",
        path = "Audio/BGM/twilightAmbient.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Twilight (Moody)",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(TwiAmb)

    ## Base Template
    ######################################

    # easy_like_summer = ost.soundtrack(
    #     name = "Easy",
    #     path = "bgm/09 Easy.mp3",
    #     priority = 1,
    #     author = "Lionel Richie",
    #     description = "Easy like sunday morning.",
    #     cover_art = False,
    #     unlocked = renpy.seen_audio("bgm/09 Easy.mp3")
    # )
    # ost.manualDefineList.append(easy_like_summer)
