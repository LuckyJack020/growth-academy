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
        name = "Peaks and Valleys",
        path = "Audio/BGM/scene_BE.ogg",
        priority = 1,
        author = "Post-Bop",
        description = "Honoka's Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_BE.ogg")
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
        name = "Dokkoi!",
        path = "Audio/BGM/scene_festival.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Festival Theme",
        cover_art = False,
        unlocked = renpy.seen_audio("Audio/BGM/scene_festival.ogg")
    )
    ost.manualDefineList.append(Festival)

    Higheredu = ost.soundtrack(
        name = "Higher Education",
        path = "Audio/BGM/scene_higheredu.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Hallway Music",
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

    TremWhis = ost.soundtrack(
        name = "Trembling Whispers",
        path = "Audio/BGM/tremblingWhispers.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Horror Movie Night Track 1",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(TremWhis)

    CrePres = ost.soundtrack(
        name = "Creeping Presence",
        path = "Audio/BGM/CreepingPresence.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Horror Movie Night Track 2",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(CrePres)

    Cha = ost.soundtrack(
        name = "The Chase",
        path = "Audio/BGM/Chase.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Horror Movie Night Track 3",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(Cha)

    BriLi = ost.soundtrack(
        name = "Bright Lights",
        path = "Audio/BGM/BrightLights.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Town Theme",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(BriLi)

    SomSun = ost.soundtrack(
        name = "Somber Sunset",
        path = "Audio/BGM/general4.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Emotional Rest",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(SomSun)

    PRGMB = ost.soundtrack(
        name = "Quiet Wandering (Music Box)",
        path = "Audio/BGM/scene_PRGMusicBox.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Alt Cover of Aida's Theme",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(PRGMB)

    BgCh = ost.soundtrack(
        name = "Big Changes",
        path = "Audio/BGM/scene_uncategorized2.mp3",
        priority = 2,
        author = "Pocket Sound",
        description = "Serious Developments",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(BgCh)

    RiV = ost.soundtrack(
        name = "Show Stopper",
        path = "Audio/BGM/rivalry.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Tense Rivalry",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(RiV)

    ElA = ost.soundtrack(
        name = "Elegant Antics",
        path = "Audio/BGM/scene_WG2.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Alice's Good Mood",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(ElA)

    PsO = ost.soundtrack(
        name = "Press On",
        path = "Audio/BGM/scene_PRG2.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Aida's Elegance",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(PsO)

    theme_ToM = ost.soundtrack(
        name = "Finding Purpose",
        path = "Audio/BGM/scene_tomoko.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Tomoko's Theme",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_ToM)

    theme_SeB = ost.soundtrack(
        name = "Sea Breeze",
        path = "Audio/BGM/scene_beach.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Beach Theme",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_SeB)

    theme_LaB = ost.soundtrack(
        name = "Last Bell",
        path = "Audio/BGM/general4.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Now or Never",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_LaB)

    theme_TwiDus = ost.soundtrack(
        name = "Dusk",
        path = "Audio/BGM/twilightDusk.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Twilight (Dark)",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_TwiDus)

    theme_WiBr = ost.soundtrack(
        name = "Wild Blur",
        path = "Audio/BGM/scene_uncategorized1.mp3",
        priority = 3,
        author = "Pocket Sound",
        description = "Energetic and Fast",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_WiBr)

    theme_HoL = ost.soundtrack(
        name = "Winter Wonderland",
        path = "Audio/BGM/scene_holiday.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Snowy Holiday Theme",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_HoL)

    theme_WiN = ost.soundtrack(
        name = "Solstice Night",
        path = "Audio/BGM/scene_winter.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Wintry Theme",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_WiN)

    theme_WiV = ost.soundtrack(
        name = "Solstice Night (Vocal Mix)",
        path = "Audio/BGM/scene_wintervocal.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Wintry Theme Vocals",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_WiV)

    theme_HmT = ost.soundtrack(
        name = "Hidden Meadow (Taishogoto Ver.)",
        path = "Audio/BGM/scene_GTS2.ogg",
        priority = 1,
        author = "Post-Bop",
        description = "Alternate Naomi Theme",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_HmT)

    theme_OvO = ost.soundtrack(
        name = "Hatred",
        path = "Audio/BGM/theme_natsuko.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Natsuko's Theme",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_OvO)

    theme_ClS = ost.soundtrack(
        name = "Clear Skies",
        path = "Audio/BGM/theme_clearskies.ogg",
        priority = 2,
        author = "Post-Bop",
        description = "Uplifting Theme",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_ClS)

    theme_NbS = ost.soundtrack(
        name = "Nembutsu",
        path = "Audio/BGM/scene_nembutsu.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Morning Mist",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_NbS)

    theme_PoF = ost.soundtrack(
        name = "Overflow",
        path = "Audio/BGM/scene_PRGOverflow.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Overflow",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_PoF)

    theme_RlY = ost.soundtrack(
        name = "Reality",
        path = "Audio/BGM/reality.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Distant Questioning",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_RlY)

    theme_DfP = ost.soundtrack(
        name = "Different Paths",
        path = "Audio/BGM/differentpaths.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Branching Fates",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_DfP)

    theme_MtV = ost.soundtrack(
        name = "Motivation",
        path = "Audio/BGM/motivation.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Rekindled Determination",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_MtV)

    theme_StD = ost.soundtrack(
        name = "Stardust",
        path = "Audio/BGM/stardust.ogg",
        priority = 3,
        author = "Post-Bop",
        description = "Evening Serenity",
        cover_art = False,
        unlocked = True
    )
    ost.manualDefineList.append(theme_StD)

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
