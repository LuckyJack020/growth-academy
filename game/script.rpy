#define config.interpolate_exprs = "fallback" #Add back in if interpolation ever fails again
default persistent.enable_notifications=2
default persistent.enable_nsfw=True
default AEOutfit = OutfitEnum.DEFAULT
default BEOutfit = OutfitEnum.DEFAULT
default FMGOutfit = OutfitEnum.DEFAULT
default GTSOutfit = OutfitEnum.DEFAULT
default PRGOutfit = OutfitEnum.DEFAULT
default WGOutfit = OutfitEnum.DEFAULT
default MCOutfit = OutfitEnum.DEFAULT
default TakoOutfit = OutfitEnum.DEFAULT
default TomoOutfit = OutfitEnum.DEFAULT
default MinoriOutfit = OutfitEnum.DEFAULT
default NatsOutfit = OutfitEnum.DEFAULT
default OkishoOutfit = OutfitEnum.DEFAULT
default SakuraOutfit = OutfitEnum.DEFAULT
default RyokoOutfit = OutfitEnum.DEFAULT
default JinekoOutfit = OutfitEnum.DEFAULT
default DaitaroOutfit = OutfitEnum.DEFAULT
default TakamuraOutfit = OutfitEnum.DEFAULT
default KanamiOutfit = OutfitEnum.DEFAULT
default AENsfw = False
default BENsfw = False
default FMGNsfw = False
default GTSNsfw = False
default PRGNsfw = False
default WGNsfw = False
default MCNsfw = False
default TakoNsfw = False
default AEPrevOutfit = OutfitEnum.DEFAULT
default AENsfwOutfit = OutfitEnum.DEFAULT
default BEPrevOutfit = OutfitEnum.DEFAULT
default BENsfwOutfit = OutfitEnum.DEFAULT
default FMGPrevOutfit = OutfitEnum.DEFAULT
default FMGNsfwOutfit = OutfitEnum.DEFAULT
default GTSPrevOutfit = OutfitEnum.DEFAULT
default GTSNsfwOutfit = OutfitEnum.DEFAULT
default PRGPrevOutfit = OutfitEnum.DEFAULT
default PRGNsfwOutfit = OutfitEnum.DEFAULT
default WGPrevOutfit = OutfitEnum.DEFAULT
default WGNsfwOutfit = OutfitEnum.DEFAULT
default MCPrevOutfit = OutfitEnum.DEFAULT
default MCNsfwOutfit = OutfitEnum.DEFAULT
default NatsPrevOutfit = OutfitEnum.DEFAULT
default NatsNsfwOutfit = OutfitEnum.DEFAULT
default TakoPrevOutfit = OutfitEnum.DEFAULT
default TakoNsfwOutfit = OutfitEnum.DEFAULT
define dis1 = { "master" : Dissolve(1.0) }
define mov1 = { "master" : MoveTransition(1.0)}
define mov3 = { "master" : MoveTransition(3.0)}

#Custom ATL-based move transition for character sprites. Allows for movement WHILE dialogue is shown.
#xcenter value (basically the same as what value between 0.00 and 1.00 along the x-axis) is passed as variable.
#if combining with "Transform(xzoom=+-1)", separate into two different "show ______ at" statements
#error happens whenever xzoom is set to +1 only, but for consistency's sake; we'll separate them regardless.

transform altMove (xSp, xCen):
    linear xSp xcenter xCen

transform altFall(ySp):
    easeout ySp yoffset 720

transform altRise(ySp):
    easein ySp yoffset 0

transform wiggle_loop(xSP):
    easein xSP xoffset 20
    easeout xSP xoffset 0
    easein xSP xoffset -15
    easeout xSP xoffset 0
    easein xSP xoffset 10
    easeout xSP xoffset 0
    easein xSP xoffset -5
    ease xSP xoffset 0
    repeat

transform shake2(rate=.090, rpt=1):
    linear rate xoffset 2 yoffset 0
    linear rate xoffset -2.8 yoffset 2
    linear rate xoffset 2.8 yoffset 0
    linear rate xoffset -2 yoffset 2
    linear rate xoffset +0 yoffset +0
    repeat rpt

transform slowease(start, end, time):
    subpixel True
    start
    easein time end

transform pacing(xSP):
    easein xSP xoffset -200
    xzoom -1.0
    easein xSP xoffset 200
    xzoom 1.0
    easein xSP xoffset -100
    xzoom -1.0
    easein xSP xoffset 50
    xzoom 1.0
    easein xSP xoffset -100
    xzoom -1.0
    easein xSP xoffset 50
    xzoom 1.0
    repeat

init python:
    preferences.set_volume("music", 0.125)
    preferences.set_volume("sound", 0.75)
    config.use_cpickle = False
    #style.menu_choice_button.background = Frame("Graphics/ui/choice_bg_idle.jpg",28,9) #These two commands set the background of all in-game choice-buttons.
    #style.menu_choice_button.hover_background = Frame("Graphics/ui/choice_bg_hover.jpg",28,9)
    #style.menu_choice.color = "#fff" #These two commands set the color of the font in the in-game choice buttons.

    #style.menu_choice_button_disabled.background = Frame("Graphics/ui/choice_bg_disabled.jpg",28,9)
    activeevent = ""
    eventname = ""
    eventlibrary = {}
    datelibrary = {}
    showQuickMenu = False
    charlist = ['BE', 'GTS', 'AE', 'FMG', 'WG', 'PRG', 'MC', 'RM', 'TM', 'faculty']
    girllist = ['BE', 'GTS', 'AE', 'FMG', 'WG', 'PRG']
    locationlist = {
        #name of place: (map used, x/y pixel position)
        'arcade': ("town", (500,700)),
        'auditorium': ("school", (385,200)),
        'bakery': ("town", (500,700)),
        'ballroom': ("town", (500,700)),
        'businterior': ("town", (500,700)),
        'cafeteria': ("school", (750,215)),
        'campuscenter': ("school", (570,390)),
        'chukanpoint': ("school", (975,50)),
        'classroom': ("school", (750,280)),
        'classroom_2': ("school", (750,280)),
        'classroom_3': ("school", (750,280)),
        'clocktower': ("school", (625,555)),
        'cookingclassroom': ("school", (745,290)),
        'dock': ("school", (500,700)),
        'dormAE': ("school", (870,300)),
        'dormWG': ("school", (870,280)),
        'dormBE': ("school", (870,260)),
        'dormPRG': ("school", (870,280)),
        'dormFMG': ("school", (870,300)),
        'dormexterior': ("school", (820,375)),
        'dormhallway': ("school", (870,250)),
        'dorminterior': ("school", (890,390)),
        'dormtomoko': ("school", (870, 260)),
        'facultyroom': ("school", (590,590)),
        'festival': ("town", (500,700)),
        'field': ("town", (500,700)),
        'frozenbeach': ("town", (500,700)),
        'gamestore': ("town", (500,700)),
        'gatefront': ("school", (570,390)),
        'giantdorminterior': ("town", (975,50)),
        'gym': ("school", (385,400)),
        'hallway': ("school", (745,375)),
        'hallwaystairs': ("school", (745, 375)),
        'hillroad': ("town", (500,700)),
        'infodesk': ("school", (590,590)),
        'lakeroad': ("school", (460,120)),
        'library': ("school", (570,275)),
        'lockers': ("school", (385,400)),
        'musicclassroom': ("school", (745,290)),
        'nurseoffice': ("school", (590,590)),
        'okinawa': ("town", (500,700)),
        'office': ("school", (590,590)),
        'park': ("town", (500,700)),
        'pool': ("school", (385,400)),
        'roof': ("school", (750,375)),
        'schoolfront': ("school", (570,620)),
        'schoolplanter': ("school", (570,150)),
        'schoolexterior': ("school", (715,650)),
        'summer-beach': ("town", (500,700)),
        'summer-guestbedroom': ("town", (500,700)),
        'supermarket': ("town", (500,700)),
        'town': ("town", (500,700)),
        'tokyo': ("town", (500,700)),
        'track': ("school", (570,165)),
        'unknown': ("school", (550, 550)),
        'waterpark': ("town", (500,700)),
        'woods': ("school", (825,65))
    }
    debugenabled = True
    debuginput = ""

    import math

    #Condition enums/stuff
    class TimeEnum:
        DAY = "day"
        NIGHT = "night"
        EVE = "eve"
        NIGHTLIGHTS = "night_lights"
        RAIN = "rain"

    class OutfitEnum:
        DEFAULT = "default"
        DRESS = "dress"
        NUDE = "nude"
        ATHLETIC = "athletic"
        ALTERNATE = "alternate"
        BEND = "bend"
        CASUAL = "casual"
        CASUAL2 = "casual-2"
        COOKING = "cooking"
        COSTUME = "costume"
        EPILOGUE = "epilogue"
        EPILOGUEBAD = "epilogue-bad"
        EPILOGUEGOOD = "epilogue-good"
        FORMAL = "formal"
        GYM = "gym"
        SWIM = "swim"
        SWIMCAP = "swimcap"
        SWIMSUIT = "swimsuit"
        COW = "cow"
        PAJAMAS = "pajamas"
        RIPPED = "ripped"
        SUMEXT = "summer-exterior"
        SUMEXTSG = "summer-exterior-sunglasses"
        SUMINT = "summer-interior"
        SUMINTSG = "summer-interior-sunglasses"
        TIRED = "tired"
        TOPLESS = "topless"
        TRADITIONAL = "traditional"
        UNDERWEAR = "underwear"
        WORK = "work"

    class ConditionEnum:
        EVENT, NOEVENT, FLAG, NOFLAG, AFFECTION, SKILL, TIMEFLAG, AND, OR, ROUTELOCK, NOROUTELOCK, VAR = range(12)

    #EVENT: arg1 = (string) event code, true if event has been seen
    #NOEVENT: arg1 = (string) event code, true if event has NOT been seen
    #FLAG: arg1 = (string) flag name, true if flag has been raised
    #NOFLAG: arg1 = (string) flag name, true if flag has NOT been raised
    #AFFECTION: arg1 = (string, in girls list) girl, arg2 = ConditionEqualityEnum, arg3 = (int) affection score, true if the comparison is true (between girl specified in arg1's affection score and arg3)
    #SKILL: arg1 = (string, in skills list) skill, arg2 = ConditionEqualityEnum, arg3 = (int) skill score, true if the comparison is true (between skill specified in arg1 and arg3)
    #OR: arg1 = condition, arg2 = condition, returns true if either arg1 or arg2 are true
    #ROUTELOCK: arg1 = (string) character code, true if you're on that route (or, if empty string, true if not on any route)
    #NOROUTELOCK: arg1 = (string) character code, true if you're NOT on that route (or, if empty string, true if on any route)
    #VAR: arg1 = (string) variable name, arg2 = (string) variable value, true if value matches the current value of the variable name

    class EventTypeEnum:
        CORE, OPTIONAL, OPTIONALCORE = range(3)

    #CORE: Event is in someone's core route. Cannot be selected randomly.
    #OPTIONAL: Event is an optional event. Can be selected randomly.
    #OPTIONALCORE: Event is selected like an optional event, but is displayed like a core event in the UI.

    class PrioEnum:
        NONE, GIRL, ALL = range(3)

    #NONE: Not a priority. Other events available.
    #GIRL: Priority. Other events featuring the first girls in the charlist are not available.
    #ALL: Priority. Other events not available, no matter who's in them.

    class ConditionEqualityEnum:
        EQUALS, NOTEQUALS, GREATERTHAN, LESSTHAN, GREATERTHANEQUALS, LESSTHANEQUALS = range(6)

    def checkCriteria(clist):
        criteriavalid = True
        for c in clist:
            if c[0] == ConditionEnum.EVENT:
                if c[1] not in clearedevents:
                    criteriavalid = False
                    break
                else:
                    continue
            elif c[0] == ConditionEnum.NOEVENT:
                if c[1] in clearedevents:
                    criteriavalid = False
                    break
                else:
                    continue
            elif c[0] == ConditionEnum.FLAG:
                if c[1] not in flags:
                    criteriavalid = False
                    break
                else:
                    continue
            elif c[0] == ConditionEnum.TIMEFLAG:
                if c[1] not in timeflags:
                    criteriavalid = False
                    break
                else:
                    continue
            elif c[0] == ConditionEnum.NOFLAG:
                if c[1] not in flags:
                    continue
                else:
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.AFFECTION:
                if c[2] == ConditionEqualityEnum.LESSTHAN:
                    if getAffection(c[1]) >= int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[2] == ConditionEqualityEnum.LESSTHANEQUALS:
                    if getAffection(c[1]) > int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[2] == ConditionEqualityEnum.GREATERTHAN:
                    if getAffection(c[1]) <= int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[2] == ConditionEqualityEnum.GREATERTHANEQUALS:
                    if getAffection(c[1]) < int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                else:
                    renpy.log("Invalid criteria equality enum ID: %s" % str(c[2]))
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.SKILL:
                if c[2] == ConditionEqualityEnum.LESSTHAN:
                    if getSkill(c[1]) >= int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[2] == ConditionEqualityEnum.LESSTHANEQUALS:
                    if getSkill(c[1]) > int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[2] == ConditionEqualityEnum.GREATERTHAN:
                    if getSkill(c[1]) <= int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[2] == ConditionEqualityEnum.GREATERTHANEQUALS:
                    if getSkill(c[1]) < int(c[3]):
                        criteriavalid = False
                        break
                    else:
                        continue
                else:
                    renpy.log("Invalid criteria equality enum ID: %s" % str(c[2]))
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.AND:
                if checkCriteria([c[1]]) and checkCriteria([c[2]]):
                    continue
                else:
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.OR:
                if checkCriteria([c[1]]) or checkCriteria([c[2]]):
                    continue
                else:
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.ROUTELOCK:
                if routelock == c[1]:
                    continue
                else:
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.NOROUTELOCK:
                if routelock != c[1]:
                    continue
                else:
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.VAR:
                if getVar(c[1]) == c[2]:
                    continue
                else:
                    criteriavalid = False
                    break
            else:
                renpy.log("Invalid criteria enum ID: %s" % str(c[0]))
                criteriavalid = False
                break
        return criteriavalid

    def getEventForGirl(girl):
        #rewrite to return selected core event and list of optional events
        pool = []
        priority = False #true = girl priority

        #Populate optional event pool (to find priority stuff)
        for k, v in eventlibrary.iteritems():
            badFlag = False
            if v["type"] == EventTypeEnum.CORE:
                continue
            if len(v["girls"]) == 0 or v["girls"][0] != girl:
                continue
            if girl in girllist and not isRouteEnabled(girl):
                continue
            if k in clearedevents:
                continue
            criteriavalid = checkCriteria(v["conditions"])
            if not criteriavalid:
                continue
            for f in timeflags:
                if f in v["obsflags"]:
                    badFlag = True
                    break
            if badFlag:
                continue
            if v["priority"] != PrioEnum.GIRL and priority:
                continue
            if v["priority"] == PrioEnum.GIRL and not priority:
                priority = True
                pool = []
            pool.append(k)

        #Find core event, if available
        if girl in girllist:
            if isRouteEnabled(girl):
                #check for stale core event
                rid = routeprogress[girl]
                s = eventlibrary[rid]
                for f in s["obsflags"]:
                    if f in timeflags:
                        setProgress(girl, s["next"])
                        return getEventForGirl(girl)

                #check for validity of next event (if not stale)
                criteriavalid = checkCriteria(s["conditions"])
                if s["priority"] == PrioEnum.GIRL or not priority:
                    if criteriavalid:
                        return routeprogress[girl], pool

        #if we found a priority optional event, and the core event isn't priority, always offer that optional event (and no other optional events)
        if priority:
            return renpy.random.choice(pool), []

        #If there's no core event available (either due to conditions or because it's not a main girl), just return the pool
        return None, pool

    def getAllPriorityEvents():
        pool = []
        for k, v in eventlibrary.iteritems():
            if v["priority"] != PrioEnum.ALL:
                continue
            if k in clearedevents:
                continue
            #Only care about all-priority core events if it's the current one
            if v["type"] == EventTypeEnum.CORE and routeprogress[v["girls"][0]] != k:
                continue
            badFlag = False
            for f in timeflags:
                if f in v["obsflags"]:
                    badFlag = True
                    break
            if badFlag:
                continue
            criteriavalid = checkCriteria(v["conditions"])
            if not criteriavalid:
                continue
            pool.append(k)
        if len(pool) > 6:
            return renpy.random.sample(pool, 6)
        else:
            return pool

    def rollEvents():
        prefgirl = getHighestAffection()

        eventchoices = []
        opteventpool = []
        allPriority = getAllPriorityEvents()
        if not allPriority:
            for g in charlist:
                event, opt = getEventForGirl(g) #returns an event and a list of available optional events
                if event != None:
                    eventchoices.append(event)
                opteventpool = opteventpool + opt

            #Pull 2 random optional events
            #add minor character optional events to pool
            if minorEventsEnabled():
                event, opt = getEventForGirl("minor")
                opteventpool = opteventpool + opt

            if len(opteventpool) == 1:
                eventchoices.append(opteventpool[0])
            if len(opteventpool) >= 2:
                tmp = renpy.random.sample(opteventpool, 2)
                eventchoices.append(tmp[0])
                eventchoices.append(tmp[1])
            return eventchoices
        else: #AllPriority event(s) exist, use the returned list
            return allPriority

        #to implement:
        #route lock

    def minorEventsEnabled():
        for t in minorDisableTimes:
            if t[0] in timeflags and not t[1] in timeflags:
                return False
        return True

    #Other misc functions
    def setAffection(girl, val):
        if not girl in charlist:
            renpy.log("ERROR: Could not change affection: Girl %s does not exist" % girl)
            return
        affection[girl] += val
        #if affection[girl] < 0:
        #    affection[girl] = 0
        if val > 0:
            img = "Graphics/ui/notification/" + girl + "-up.webp"
        elif val < 0:
            img = "Graphics/ui/notification/" + girl + "-down.webp"
        else:
            return
        showNotification(img)

    def getAffection(girl):
        if not girl in charlist:
            renpy.log("ERROR: Could not fetch affection: Girl %s does not exist" % girl)
            return 0
        return affection[girl]

    def checkAffection(girl, exp, checkVal):
        if not girl in charlist:
            renpy.log("ERROR: Could not change affection: Girl %s does not exist" % girl)
            return
        if exp == ">":
            if affection[girl] > checkVal:
                checkResult = True
            else:
                checkResult = False
        elif exp == "<":
            if affection[girl] < checkVal:
                checkResult = True
            else:
                checkResult = False
        elif exp == ">=":
            if affection[girl] >= checkVal:
                checkResult = True
            else:
                checkResult = False
        elif exp == "<=":
            if affection[girl] <= checkVal:
                checkResult = True
            else:
                checkResult = False
        elif exp == "==":
            if affection[girl] == checkVal:
                checkResult = True
            else:
                checkResult = False
        else:
            renpy.log("ERROR: Expression used in code is not a valid operator.")
            return
        if persistent.enable_notifications < 2:
            if checkResult:
                return True
            else:
                return False
        else:
            if checkResult:
                img = "Graphics/ui/notification/" + girl + "-win.webp"
                showNotification(img)
                return True
            else:
                img = "Graphics/ui/notification/" + girl + "-fail.webp"
                showNotification(img)
                return False

    #Returns girl with highest affection. In the event of a tie, returns a random girl among those tieing.
    def getHighestAffection():
        tmplist = girllist[:]
        renpy.random.shuffle(tmplist)
        highestgirl = ""
        highestscore = -999
        for g in tmplist:
            if getAffection(g) > highestscore:
                highestscore = getAffection(g)
                highestgirl = g
        return highestgirl

    #Checks which of the girls has the highest affection, excluding any girl(s) given in the argument. Ties go to earliest girl in girllist.
    #Function is expecting a list argument, even if there's only one girl
    def getSecondHighest(ignorelist):
        highestAffection = 0
        secondGirl = ""
        for girl in girllist:
            if girl in ignorelist:
                continue

            affection = getAffection(girl)
            if affection > highestAffection:
                highestAffection = affection
                secondGirl = girl
        return secondGirl

    def isHighestSkill(s):
        if getSkill(s) >= getSkill("Art") and getSkill(s) >= getSkill("Academics") and getSkill(s) >= getSkill("Athletics"):
            checkSkill(s, "==", getSkill(s))
            return True
        else:
            checkSkill(s, ">", getSkill(s))
            return False

    def isEventCleared(event):
        return event in clearedevents

    def setFlag(flag, state=True):
        if state:
            if flag in flags:
                return
            else:
                flags.append(flag)
        else:
            if flag in flags:
                flags.remove(flag)
            else:
                return

    def getFlag(flag):
        return flag in flags

    def setVar(id, val):
        vars[id] = val

    def getVar(id):
        if id in vars.keys():
            return vars[id]
        else:
            return 0

    def debugListVars():
        l = ""
        for k, v in vars.items():
            l += k + ": " + str(v) + ", "
        return l

    def debugListFlags():
        l = ""
        for f in flags:
            l += f + ", "
        return l

    def debugListTimeFlags():
        l = ""
        for f in timeflags:
            l += f + ", "
        return l

    def debugListClearedEvents():
        l = ""
        for s in clearedevents:
            l += s + ", "
        return l

    def setSkill(s, val):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
            return -1
        else:
            skills[s] += val
            if val >= 0:
                img = "Graphics/ui/notification/" + s + "-up.webp"
            else:
                img = "Graphics/ui/notification/" + s + "-down.webp"
            showNotification(img)
            return skills[s]

    def setSkillDebug(s, val):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
        else:
            skills[s] += val
            if val >= 0:
                img = "Graphics/ui/notification/" + s + "-up.webp"
            else:
                img = "Graphics/ui/notification/" + s + "-down.webp"
            showNotification(img)

    def setSizeDebug(mod):
        global globalsize, prgsize
        globalsize += mod
        if globalsize < 1:
            globalsize = 1
        if globalsize > 6:
            globalsize = 6
        prgsize = globalsize

    def getSkill(s):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
            return -1
        else:
            return skills[s]

    def checkSkill(s, exp, checkVal):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
            return -1
        if exp == ">":
            if skills[s] > checkVal:
                checkResult = True
            else:
                checkResult = False
        elif exp == "<":
            if skills[s] < checkVal:
                checkResult = True
            else:
                checkResult = False
        elif exp == ">=":
            if skills[s] >= checkVal:
                checkResult = True
            else:
                checkResult = False
        elif exp == "<=":
            if skills[s] <= checkVal:
                checkResult = True
            else:
                checkResult = False
        elif exp == "==":
            if skills[s] == checkVal:
                checkResult = True
            else:
                checkResult = False
        else:
            renpy.log("ERROR: Expression used in code is not a valid operator.")
            return
        if persistent.enable_notifications < 2:
            if checkResult:
                return True
            else:
                return False
        else:
            if checkResult:
                img = "Graphics/ui/notification/" + s + "-win.webp"
                showNotification(img)
                return True
            else:
                img = "Graphics/ui/notification/" + s + "-fail.webp"
                showNotification(img)
                return False

    def showNotification(img):
        global activenotifications
        if persistent.enable_notifications == 0:
            return
        try:
            activenotifications
        except NameError:
            activenotifications = 0
        if activenotifications < 0:
            activenotifications = 0
        if activenotifications <= 4:
            activenotifications += 1
            renpy.show_screen("notification" + str(activenotifications), img)

    def setProgress(girl, event):
        routeprogress[girl] = event

    def getProgress(girl):
        return routeprogress[girl]

    def disableRoute(girl):
        if girl in routeenabled:
            routeenabled[girl] = False

    def enableRoute(girl):
        if girl in routeenabled:
            routeenabled[girl] = True

    def lockRoute(girl):
        global routelock
        if girl in girllist:
            routelock = girl

    def isRouteEnabled(girl):
        return routeenabled[girl] and (routelock == girl or routelock == "")

    def getRoutelock():
        return routelock

    def isNSFW():
        return persistent.enable_nsfw

    def adjustNSFW():
        global AEOutfit
        global BEOutfit
        global FMGOutfit
        global GTSOutfit
        global PRGOutfit
        global WGOutfit
        global MCOutfit
        global NatsOutfit
        global TakoOutfit
        if (AEOutfit == OutfitEnum.NUDE or AEOutfit == OutfitEnum.EPILOGUEBAD) and not isNSFW():
            AEOutfit = AEPrevOutfit
        elif AENsfw and isNSFW():
            AEOutfit = AENsfwOutfit

        if (BEOutfit == OutfitEnum.NUDE or BEOutfit == OutfitEnum.TOPLESS) and not isNSFW():
            BEOutfit = BEPrevOutfit
        elif BENsfw and isNSFW():
            BEOutfit = BENsfwOutfit

        if FMGOutfit == OutfitEnum.NUDE and not isNSFW():
            FMGOutfit = FMGPrevOutfit
        elif FMGNsfw and isNSFW():
            FMGOutfit = FMGNsfwOutfit

        if GTSOutfit == OutfitEnum.NUDE and not isNSFW():
            GTSOutfit = GTSPrevOutfit
        elif GTSNsfw and isNSFW():
            GTSOutfit = GTSNsfwOutfit

        if PRGOutfit == OutfitEnum.NUDE and not isNSFW():
            PRGOutfit = PRGPrevOutfit
        elif PRGNsfw and isNSFW():
            PRGOutfit = PRGNsfwOutfit

        if WGOutfit == OutfitEnum.NUDE and not isNSFW():
            WGOutfit = WGPrevOutfit
        elif WGNsfw and isNSFW():
            WGOutfit = WGNsfwOutfit

        if MCOutfit == OutfitEnum.NUDE and not isNSFW():
            MCOutfit = MCPrevOutfit
        elif MCNsfw and isNSFW():
            MCOutfit = MCNsfwOutfit
        
        if NatsOutfit == OutfitEnum.NUDE and not isNSFW():
            NatsOutfit = NatsPrevOutfit
        elif NatsNsfw and isNSFW():
            NatsOutfit = NatsNsfwOutfit

        if TakoOutfit == OutfitEnum.NUDE and not isNSFW():
            TakoOutfit = TakoPrevOutfit
        elif TakoNsfw and isNSFW():
            TakoOutfit = TakoNsfwOutfit

    def setTimeFlag(flag):
        if flag not in timeflags:
            timeflags.append(flag)

    def debugSetTimeFlag(flag, state):
        if state:
            if flag in timeflags:
                return
            else:
                timeflags.append(flag)
        else:
            if flag in timeflags:
                timeflags.remove(flag)
            else:
                return

    def getSize():
        global globalsize
        return globalsize

    def setSize(size):
        global globalsize, prgsize
        if size > globalsize:
            globalsize = size
            if size != 3: #Aida's initial pregnancy doesn't follow globalsize schedule
                prgsize = size

    def getTime():
        global gametime
        return gametime

    def setTime(t):
        global gametime
        if t == TimeEnum.DAY or t == TimeEnum.EVE or t == TimeEnum.NIGHT or t == TimeEnum.NIGHTLIGHTS or t == TimeEnum.RAIN:
            gametime = t

    def setAEOutfit(o):
        global AEOutfit
        global AEPrevOutfit
        global AENsfwOutfit
        global AENsfw
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.BEND or o == OutfitEnum.EPILOGUEGOOD or o == OutfitEnum.DRESS or o == OutfitEnum.TIRED or o == OutfitEnum.TRADITIONAL or o == OutfitEnum.CASUAL or o == OutfitEnum.UNDERWEAR:
            AENsfw = False
            AEOutfit = o
        elif o == OutfitEnum.NUDE or o == OutfitEnum.EPILOGUEBAD:
            AENsfw = True
            AENsfwOutfit = o
            if isNSFW():
                AEPrevOutfit = AEOutfit
                AEOutfit = o

    def setBEOutfit(o):
        global BEOutfit
        global BEPrevOutfit
        global BENsfwOutfit
        global BENsfw
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.CASUAL or o == OutfitEnum.CASUAL2 or o == OutfitEnum.DRESS or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMSUIT or o == OutfitEnum.TRADITIONAL:
            BENsfw = False
            BEOutfit = o
        elif o == OutfitEnum.NUDE or o == OutfitEnum.TOPLESS:
            BENsfw = True
            BENsfwOutfit = o
            if isNSFW():
                BEPrevOutfit = BEOutfit
                BEOutfit = o

    def setFMGOutfit(o):
        global FMGOutfit
        global FMGPrevOutfit
        global FMGNsfwOutfit
        global FMGNsfw
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.CASUAL or o == OutfitEnum.COSTUME or o == OutfitEnum.DRESS or o == OutfitEnum.GYM or o == OutfitEnum.RIPPED or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMSUIT or o == OutfitEnum.TRADITIONAL or o == OutfitEnum.CASUAL2 or o == OutfitEnum.UNDERWEAR:
            FMGNsfw = False
            FMGOutfit = o
        elif o == OutfitEnum.NUDE:
            FMGNsfw = True
            FMGNsfwOutfit = o
            if isNSFW():
                FMGPrevOutfit = FMGOutfit
                FMGOutfit = o

    def setGTSOutfit(o):
        global GTSOutfit
        global GTSPrevOutfit
        global GTSNsfwOutfit
        global GTSNsfw
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.CASUAL or o == OutfitEnum.SWIMSUIT or o == OutfitEnum.TRADITIONAL or o == OutfitEnum.WORK:
            GTSNsfw = False
            GTSOutfit = o
        elif o == OutfitEnum.NUDE:
            GTSNsfw = True
            GTSNsfwOutfit = o
            if isNSFW():
                GTSPrevOutfit = GTSOutfit
                GTSOutfit = o

    def setPRGOutfit(o):
        global PRGOutfit
        global PRGPrevOutfit
        global PRGNsfwOutfit
        global PRGNsfw
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.ALTERNATE or o == OutfitEnum.CASUAL or o == OutfitEnum.DRESS or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMSUIT or o == OutfitEnum.TRADITIONAL or o == OutfitEnum.COW or o == OutfitEnum.PAJAMAS:
            PRGNsfw = False
            PRGOutfit = o
        elif o == OutfitEnum.NUDE or o == OutfitEnum.TOPLESS:
            PRGNsfw = True
            PRGNsfwOutfit = o
            if isNSFW():
                PRGPrevOutfit = PRGOutfit
                PRGOutfit = o

    def setWGOutfit(o):
        global WGOutfit
        global WGPrevOutfit
        global WGNsfwOutfit
        global WGNsfw
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.ALTERNATE or o == OutfitEnum.DRESS or o == OutfitEnum.CASUAL or o == OutfitEnum.CASUAL2 or o == OutfitEnum.FORMAL or o == OutfitEnum.PAJAMAS or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMCAP or o == OutfitEnum.SWIMSUIT or o == OutfitEnum.SUMINT or o == OutfitEnum.SUMEXT or o == OutfitEnum.SUMINTSG or o == OutfitEnum.SUMEXTSG or o == OutfitEnum.TRADITIONAL:
            WGNsfw = False
            WGOutfit = o
        elif o == OutfitEnum.NUDE:
            WGNsfw = True
            WGNsfwOutfit = o
            if isNSFW():
                WGPrevOutfit = WGOutfit
                WGOutfit = o

    def setMCOutfit(o):
        global MCOutfit
        global MCPrevOutfit
        global MCNsfwOutfit
        global MCNsfw
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.ALTERNATE or o == OutfitEnum.CASUAL or o == OutfitEnum.CASUAL2 or o == OutfitEnum.FORMAL or o == OutfitEnum.PAJAMAS or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMSUIT or o == OutfitEnum.TRADITIONAL or o == OutfitEnum.UNDERWEAR:
            MCNsfw = False
            MCOutfit = o
        elif o == OutfitEnum.NUDE:
            MCNsfw = True
            MCNsfwOutfit = o
            if isNSFW():
                MCPrevOutfit = MCOutfit
                MCOutfit = o

    def setTakoOutfit(o):
        global TakoOutfit
        global TakoPrevOutfit
        global TakoNsfwOutfit
        global TakoNsfw
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.CASUAL or o == OutfitEnum.ALTERNATE or o == OutfitEnum.TRADITIONAL:
            TakoOutfit = o
        elif o == OutfitEnum.NUDE:
            TakoNsfw = True
            TakoNsfwOutfit = o
            if isNSFW():
                TakoPrevOutfit = TakoOutfit
                TakoOutfit = o

    def setTomoOutfit(o):
        global TomoOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.CASUAL or o == OutfitEnum.TRADITIONAL:
            TomoOutfit = o

    def setNatsOutfit(o):
        global NatsOutfit
        global NatsPrevOutfit
        global NatsNsfwOutfit
        global NatsOutfit
        global NatsNsfw
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.UNDERWEAR or o == OutfitEnum.GYM or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMSUIT or o == OutfitEnum.CASUAL:
            NatsOutfit = o
        elif o == OutfitEnum.NUDE:
            NatsNsfw = True
            NatsNsfwOutfit = o
            if isNSFW():
                NatsPrevOutfit = NatsOutfit
                NatsOutfit = o

    def setKanamiOutfit(o):
        global KanamiOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.SWIMSUIT:
            KanamiOutfit = o

    def setOkishoOutfit(o):
        global OkishoOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.CASUAL or o == OutfitEnum.TRADITIONAL:
            OkishoOutfit = o

    def setSakuraOutfit(o):
        global SakuraOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ALTERNATE or o == OutfitEnum.CASUAL:
            SakuraOutfit = o

    def setDaitaroOutfit(o):
        global DaitaroOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.FORMAL:
            DaitaroOutfit = o

    def setJinekoOutfit(o):
        global JinekoOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.CASUAL:
            JinekoOutfit = o

    def setRyokoOutfit(o):
        global RyokoOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.CASUAL:
            RyokoOutfit = o

    def setTakamuraOutfit(o):
        global TakamuraOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.COOKING:
            TakamuraOutfit = o
    
    def setMinoriOutfit(o):
        global MinoriOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ALTERNATE:
            MinoriOutfit = o

    #Edge case handler for Aida's initial pregnancy
    def setPregnant():
        global prgsize
        if 3 > prgsize:
            prgsize = 3

    def cleanupCostumes():
        #BE
        if getVar('BEMode') == 0:
            setVar('BEMode', 'Tomboy') #Initialize Honoka, if not initialized already
        if getVar('BEMode') == 'Tomboy':
            if getVar('BEFeminine') >= getVar('BETomboy') + 1: #temporarily 1, to show outfit changes at all
                setVar('BEMode', 'Feminine')
        else:
            if getVar('BETomboy') >= getVar('BEFeminine') + 1: #temporarily 1, to show outfit changes at all
                setVar('BEMode', 'Tomboy')

    def updateSP():
        global eCounter
        global spmax
        global spspent
        if not "eCounter" in globals():
            spmax = 0
            spspent = 0
            eCounter = 0
        if eCounter >= 4:
            spmax += 1
            eCounter = 0
        else:
            eCounter += 1

    class MapLine(renpy.Displayable):
        def __init__(self, **kwargs):
            super(MapLine, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            render = renpy.Render(1280, 720)
            if highlitevent == "" or highlitmenuchoice == -1:
                return render
            starty = 40 + (highlitmenuchoice * 60) #highlitmenuchoice
            if eventlibrary[highlitevent]["location"] in locationlist:
                end = locationlist[eventlibrary[highlitevent]["location"]][1]
            else:
                end = (260, starty)

            #blit icon image on end
            #if len(eventlibrary[highlitevent]["girls"]) == 0:
            #    img = im.FactorScale("Graphics/ui/icons/minor-icon.webp", .25)
            #else:
            #    img = im.FactorScale("Graphics/ui/icons/%s-icon.webp" % eventlibrary[highlitevent]["girls"][0], .25)
            #child_render = renpy.render(img, 25, 25, st, at)
            #iconend = (end[0] - 12, end[1] - 12)
            #render.blit(child_render, iconend)

            #draw line
            canvas = render.canvas()
            canvas.line("#000", (260, starty), (360, starty), 2) #horizontal, first point should be based on choice selected, second point should be horizontal some distance out
            canvas.line("#000", (360, starty), end, 2) #diagonal, first point here should be second point horizontal, second point should be the map point

            return render

    class Flashlight(renpy.Displayable):
        def __init__(self):
            super(Flashlight, self).__init__()
            
            # This image should be twice the width and twice the height
            # of the screen.
            self.child = Image("Graphics/ui/notification/flashlight.webp")

            # (-1, -1) is the way the event system represents
            # "outside the game window".
            self.pos = (-1, -1)

        def render(self, width, height, st, at):
            render = renpy.Render(config.screen_width, config.screen_height)
            
            if self.pos == (-1, -1):
                # If we don't know where the cursor is, render pure black.
                render.canvas().rect("#000", (0, 0, config.screen_width, config.screen_height))
                return render

            # Render the flashlight image.
            child_render = renpy.render(self.child, width, height, st, at)

            # Draw the image centered on the cursor.
            flashlight_width, flashlight_height = child_render.get_size()
            x, y = self.pos
            x -= flashlight_width / 2
            y -= flashlight_height / 2
            render.blit(child_render, (x, y))
            return render

        def event(self, ev, x, y, st):
            # Re-render if the position changed.
            if self.pos != (x, y):
                renpy.redraw(self, 0)

            # Update stored position
            self.pos = (x, y)

        def visit(self):
            return [ self.child ]

label start:
    python:
        #Global Variables
        affection = {'BE': 0, 'GTS': 0, 'AE': 0, 'FMG': 0, 'WG': 0, 'PRG': 0, 'RM': 0, 'TM': 0}
        prefgirl = ""
        skills = {"Athletics": 0, "Art": 0, "Academics": 0}
        globalsize = 1
        prgsize = 1
        gametime = TimeEnum.DAY
        AEPrevOutfit = OutfitEnum.DEFAULT
        AENsfwOutfit = OutfitEnum.DEFAULT
        BEPrevOutfit = OutfitEnum.DEFAULT
        BENsfwOutfit = OutfitEnum.DEFAULT
        FMGPrevOutfit = OutfitEnum.DEFAULT
        FMGNsfwOutfit = OutfitEnum.DEFAULT
        GTSPrevOutfit = OutfitEnum.DEFAULT
        GTSNsfwOutfit = OutfitEnum.DEFAULT
        PRGPrevOutfit = OutfitEnum.DEFAULT
        PRGNsfwOutfit = OutfitEnum.DEFAULT
        WGPrevOutfit = OutfitEnum.DEFAULT
        WGNsfwOutfit = OutfitEnum.DEFAULT
        MCPrevOutfit = OutfitEnum.DEFAULT
        MCNsfwOutfit = OutfitEnum.DEFAULT
        NatsPrevOutfit = OutfitEnum.DEFAULT
        NatsNsfwOutfit = OutfitEnum.DEFAULT
        TakoPrevOutfit = OutfitEnum.DEFAULT
        TakoNsfwOutfit = OutfitEnum.DEFAULT
        AENsfw = False
        BENsfw = False
        FMGNsfw = False
        GTSNsfw = False
        PRGNsfw = False
        WGNsfw = False
        MCNsfw = False
        NatsNsfw = False
        TakoNsfw = False
        AEOutfit = OutfitEnum.DEFAULT
        BEOutfit = OutfitEnum.DEFAULT
        FMGOutfit = OutfitEnum.DEFAULT
        GTSOutfit = OutfitEnum.DEFAULT
        PRGOutfit = OutfitEnum.DEFAULT
        WGOutfit = OutfitEnum.DEFAULT
        MCOutfit = OutfitEnum.DEFAULT
        TakoOutfit = OutfitEnum.DEFAULT
        TomoOutfit = OutfitEnum.DEFAULT
        MinoriOutfit = OutfitEnum.DEFAULT
        NatsOutfit = OutfitEnum.DEFAULT
        OkishoOutfit = OutfitEnum.DEFAULT
        SakuraOutfit = OutfitEnum.DEFAULT
        RyokoOutfit = OutfitEnum.DEFAULT
        JinekoOutfit = OutfitEnum.DEFAULT
        DaitaroOutfit = OutfitEnum.DEFAULT
        TakamuraOutfit = OutfitEnum.DEFAULT
        KanamiOutfit = OutfitEnum.DEFAULT
        flags = []
        vars = {}
        eventchoices = []
        activeevent = ""
        timeflags = []
        clearedevents = []
        routeprogress = {}
        for g in girllist:
            routeprogress[g] = g + "001"
        highlitevent = ""
        hightlitmenuchoice = -1
        routeenabled = {'BE': True, 'GTS': True, 'AE': True, 'FMG': True, 'WG': True, 'PRG': True}
        routelock = ""
        eCounter = 0
        spmax = 0
        spspent = 0

        activenotifications = 0
        debugmapname = ""
    jump global000

label splashscreen:
    python:
        AEPrevOutfit = OutfitEnum.DEFAULT
        AENsfwOutfit = OutfitEnum.DEFAULT
        BEPrevOutfit = OutfitEnum.DEFAULT
        BENsfwOutfit = OutfitEnum.DEFAULT
        FMGPrevOutfit = OutfitEnum.DEFAULT
        FMGNsfwOutfit = OutfitEnum.DEFAULT
        GTSPrevOutfit = OutfitEnum.DEFAULT
        GTSNsfwOutfit = OutfitEnum.DEFAULT
        PRGPrevOutfit = OutfitEnum.DEFAULT
        PRGNsfwOutfit = OutfitEnum.DEFAULT
        WGPrevOutfit = OutfitEnum.DEFAULT
        WGNsfwOutfit = OutfitEnum.DEFAULT
        MCPrevOutfit = OutfitEnum.DEFAULT
        MCNsfwOutfit = OutfitEnum.DEFAULT
        NatsPrevOutfit = OutfitEnum.DEFAULT
        NatsNsfwOutfit = OutfitEnum.DEFAULT
        TakoPrevOutfit = OutfitEnum.DEFAULT
        TakoNsfwOutfit = OutfitEnum.DEFAULT
        AENsfw = False
        BENsfw = False
        FMGNsfw = False
        GTSNsfw = False
        PRGNsfw = False
        WGNsfw = False
        MCNsfw = False
        NatsNsfw = False
        TakoNsfw = False
        AEOutfit = OutfitEnum.DEFAULT
        BEOutfit = OutfitEnum.DEFAULT
        FMGOutfit = OutfitEnum.DEFAULT
        GTSOutfit = OutfitEnum.DEFAULT
        PRGOutfit = OutfitEnum.DEFAULT
        WGOutfit = OutfitEnum.DEFAULT
        MCOutfit = OutfitEnum.DEFAULT
        TakoOutfit = OutfitEnum.DEFAULT
        TomoOutfit = OutfitEnum.DEFAULT
        MinoriOutfit = OutfitEnum.DEFAULT
        NatsOutfit = OutfitEnum.DEFAULT
        OkishoOutfit = OutfitEnum.DEFAULT
        SakuraOutfit = OutfitEnum.DEFAULT
        RyokoOutfit = OutfitEnum.DEFAULT
        JinekoOutfit = OutfitEnum.DEFAULT
        DaitaroOutfit = OutfitEnum.DEFAULT
        TakamuraOutfit = OutfitEnum.DEFAULT
        KanamiOutfit = OutfitEnum.DEFAULT
    scene black
    with Pause(1)
    centered "The following represents a work in progress."
    centered "Art assets are placeholders or otherwise unfinished and all general content has yet to be finalized."
    centered "This is a work of fiction. Any resemblance to actual events or locales or persons, living or dead, is entirely coincidental."
    centered "For more information, visit\n https://discord.gg/Hs6ggpp"
    centered "Enjoy."
    play movie "Graphics/ui/intro.webm"
    pause 96
    return

#Remember to hide choicetimer for each choice made before the timer finishes.
screen choicetimer():
    timer 0.01 repeat True action If(timer_count > 0, true=SetVariable('timer_count', timer_count - 0.01), false=[Hide('choicetimer'), Jump(timer_jump)])

screen daymenu():
    add "Graphics/ui/map/map_school.webp"
    add "Graphics/ui/map/border.webp"

    #event choice sidebar
    grid 1 8:
        #xalign 0.1
        xpos 10
        ypos 20
        spacing 20
        for i in range(8): #c in eventchoices:
            if i >= len(eventchoices):
                null
            else:
                $c = eventchoices[i]
                fixed:
                    xmaximum 250
                    ymaximum 40
                    if eventlibrary[c]["location"] in locationlist:
                        imagebutton idle Crop((0, 0, 250, 40), "Graphics/ui/icons/bgicon-%s.webp" % eventlibrary[c]["location"]) action [SetVariable("activeevent", c), SetVariable("eventname", eventlibrary[c]["name"]), Jump("startevent")] hovered [SetVariable("highlitevent", c), SetVariable("highlitmenuchoice", i)] unhovered [SetVariable("highlitevent", ""), SetVariable("highlitmenuchoice", -1)]
                    else:
                        imagebutton idle Crop((0, 0, 250, 40), "Graphics/ui/icons/bgicon-missing.webp") action [SetVariable("activeevent", c), SetVariable("eventname", eventlibrary[c]["name"]), Jump("startevent")] hovered [SetVariable("highlitevent", c), SetVariable("highlitmenuchoice", i)] unhovered [SetVariable("highlitevent", ""), SetVariable("highlitmenuchoice", -1)]
                    hbox:
                        spacing -140
                        order_reverse True
                        if len(eventlibrary[c]["girls"]) == 0:
                            add Crop((0, 0, 184, 40), "Graphics/ui/icons/charicon-missing.webp")
                        else:
                            for g in eventlibrary[c]["girls"]:
                                add Crop((0, 0, 184, 40), "Graphics/ui/icons/charicon-%s.webp" % g)
                        #FIXME this looks awful and breaks tables, needs harder adjustments
                        #fixed:
                        #    frame:
                        #        xalign 0.5
                        #        yalign 0.5
                        #        background Solid(Color((0, 0, 0, 100)))
                        #        text eventlibrary[c]["name"]

    add MapLine()

    #studying activities (costs skill point)
    if "spmax" in globals():
        text "Free Periods: " + str(spmax - spspent) xalign 0.05 yalign 0.765 color Color((0, 0, 0))
        if getSkill("Athletics") > 9:
            text str(getSkill("Athletics")) xalign 0.0646 yalign 0.83 color Color((0, 0, 0)) textalign 0.5
        else:
            text str(getSkill("Athletics")) xalign 0.068 yalign 0.83 color Color((0, 0, 0)) textalign 0.5
        if getSkill("Art") > 9:
            text str(getSkill("Art")) xalign 0.161 yalign 0.83 color Color((0, 0, 0)) textalign 0.5
        else:
            text str(getSkill("Art")) xalign 0.165 yalign 0.83 color Color((0, 0, 0)) textalign 0.5
        if getSkill("Academics") > 9:
            text str(getSkill("Academics")) xalign 0.258 yalign 0.83 color Color((0, 0, 0)) textalign 0.5
        else:
            text str(getSkill("Academics")) xalign 0.26 yalign 0.83 color Color((0, 0, 0)) textalign 0.5
        if spmax > spspent:
            imagebutton idle "Graphics/ui/map/setathletics.webp" hover "Graphics/ui/map/newathletics.webp" xalign 0.05 yalign 0.92 action [SetVariable("activeevent", "Athletics"), Jump("train")]
            imagebutton idle "Graphics/ui/map/setart.webp" hover "Graphics/ui/map/newart.webp" xalign 0.15 yalign 0.92 action [SetVariable("activeevent", "Art"), Jump("train")]
            imagebutton idle "Graphics/ui/map/setacademics.webp" hover "Graphics/ui/map/newacademics.webp" xalign 0.25 yalign 0.92 action [SetVariable("activeevent", "Academics"), Jump("train")]
        else:
            add "Graphics/ui/map/athletics.webp" xalign 0.05 yalign 0.92
            add "Graphics/ui/map/art.webp" xalign 0.15 yalign 0.92
            add "Graphics/ui/map/academics.webp" xalign 0.25 yalign 0.92

    #scene title
    if highlitevent != "":
        frame:
            xalign 0.9
            yalign 0.9
            xanchor 1.0
            background Solid(Color((0, 0, 0, 100)))
            if debugenabled:
                text("(" + highlitevent + ") " + eventlibrary[highlitevent]["name"])
            else:
                text(eventlibrary[highlitevent]["name"])
        frame:
            xalign 0.9
            yalign 0.975
            xanchor 1.0
            background Solid(Color((0, 0, 0, 100)))
            if eventlibrary[highlitevent]["type"] == EventTypeEnum.CORE or eventlibrary[highlitevent]["type"] == EventTypeEnum.OPTIONALCORE:
                text("Core Event")
            else:
                text("Optional Event")

    #debug menu toggle (if debug is enabled)
    if debugenabled and highlitevent == "":
        #textbutton "Profiles" xalign 0.1 yalign 0.9 action Jump("profileselect")
        textbutton "Enter Debug Menu" xalign 0.9 yalign 0.95 action Jump("debugmenu")

screen notification1(img):
    frame:
        xalign .9
        background None
        add img
        at notif_transform
    timer 4.0 action [Hide("notification1"), SetVariable("activenotifications", activenotifications - 1)]

screen notification2(img):
    frame:
        xalign .8
        background None
        add img
        at notif_transform
    timer 4.2 action [Hide("notification2"), SetVariable("activenotifications", activenotifications - 1)]

screen notification3(img):
    frame:
        xalign .7
        background None
        add img
        at notif_transform
    timer 4.4 action [Hide("notification3"), SetVariable("activenotifications", activenotifications - 1)]

screen notification4(img):
    frame:
        xalign .6
        background None
        add img
        at notif_transform
    timer 4.6 action [Hide("notification4"), SetVariable("activenotifications", activenotifications - 1)]

screen notification5(img):
    frame:
        xalign .5
        background None
        add img
        at notif_transform
    timer 4.8 action [Hide("notification5"), SetVariable("activenotifications", 0)]

transform notif_transform:
    yalign -0.2
    linear 1.0 yalign 0.009
    pause 2
    linear 1.0 yalign -0.2

screen debugmenu():
    $debuginput = ""
    grid 3 16:
        xalign 0.5
        yalign 0.5

        text "Input:"
        input value VariableInputValue("debuginput")
        text ""

        textbutton "Start Event" action Jump("debugevent")
        textbutton "List Cleared Events" action Jump("debugclearedeventlist")
        textbutton "List Variables" action Jump("debugvarlist")

        textbutton "List Flags" action Jump("debugflaglist")
        textbutton "Set Flag" action Jump("setflag")
        textbutton "Unset Flag" action Jump("unsetflag")

        textbutton "List Timeflags" action Jump("debugtimeflaglist")
        textbutton "Set Timeflag" action Jump("settimeflag")
        textbutton "Unset Timeflag" action Jump("unsettimeflag")

        text "Girl"
        text "Affection"
        text "Core Progress"

        text "BE"
        hbox:
            textbutton "-" action Function(setAffection, "BE", -1)
            text str(affection["BE"])
            textbutton "+" action Function(setAffection, "BE", 1)
            textbutton "{u}Lock Route{/u}" action Function(lockRoute, "BE")
        text getProgress("BE")

        text "GTS"
        hbox:
            textbutton "-" action Function(setAffection, "GTS", -1)
            text str(affection["GTS"])
            textbutton "+" action Function(setAffection, "GTS", 1)
            textbutton "{u}Lock Route{/u}" action Function(lockRoute, "GTS")
        text getProgress("GTS")

        text "AE"
        hbox:
            textbutton "-" action Function(setAffection, "AE", -1)
            text str(affection["AE"])
            textbutton "+" action Function(setAffection, "AE", 1)
            textbutton "{u}Lock Route{/u}" action Function(lockRoute, "AE")
        text getProgress("AE")

        text "FMG"
        hbox:
            textbutton "-" action Function(setAffection, "FMG", -1)
            text str(affection["FMG"])
            textbutton "+" action Function(setAffection, "FMG", 1)
            textbutton "{u}Lock Route{/u}" action Function(lockRoute, "FMG")
        text getProgress("FMG")

        text "WG"
        hbox:
            textbutton "-" action Function(setAffection, "WG", -1)
            text str(affection["WG"])
            textbutton "+" action Function(setAffection, "WG", 1)
            textbutton "{u}Lock Route{/u}" action Function(lockRoute, "WG")
        text getProgress("WG")

        text "PRG"
        hbox:
            textbutton "-" action Function(setAffection, "PRG", -1)
            text str(affection["PRG"])
            textbutton "+" action Function(setAffection, "PRG", 1)
            textbutton "{u}Lock Route{/u}" action Function(lockRoute, "PRG")
        text getProgress("PRG")

        text "RM"
        hbox:
            textbutton "-" action Function(setAffection, "RM", -1)
            text str(affection["RM"])
            textbutton "+" action Function(setAffection, "RM", 1)
        text ""

        text "TM"
        hbox:
            textbutton "-" action Function(setAffection, "TM", -1)
            text str(affection["TM"])
            textbutton "+" action Function(setAffection, "TM", 1)
        text ""

        hbox:
            text "Athletics"
            textbutton "-" action Function(setSkillDebug, "Athletics", -1)
            text str(skills["Athletics"])
            textbutton "+" action Function(setSkillDebug, "Athletics", 1)

        hbox:
            text "Art"
            textbutton "-" action Function(setSkillDebug, "Art", -1)
            text str(skills["Art"])
            textbutton "+" action Function(setSkillDebug, "Art", 1)

        hbox:
            text "Academics"
            textbutton "-" action Function(setSkillDebug, "Academics", -1)
            text str(skills["Academics"])
            textbutton "+" action Function(setSkillDebug, "Academics", 1)

        textbutton "Return to game" action Jump("daymenu_noadvance")
        text ""
        text ""

        text "Size: " + str(globalsize)
        textbutton "+" action Function(setSizeDebug, 1)
        textbutton "-" action Function(setSizeDebug, -1)

screen debugvarlist():
    vbox:
        text debugListVars()
        textbutton "Return" action Jump("debugmenu")

screen debugflaglist():
    vbox:
        text debugListFlags()
        textbutton "Return" action Jump("debugmenu")

screen debugtimeflaglist():
    vbox:
        text debugListTimeFlags()
        textbutton "Return" action Jump("debugmenu")

screen debugclearedeventlist():
    vbox:
        text debugListClearedEvents()
        textbutton "Return" action Jump("debugmenu")

screen flashlight:
    add Flashlight()

label debugevent:
    $renpy.block_rollback()
    if debuginput in eventlibrary:
        $activeevent = debuginput
        $eventname = eventlibrary[debuginput]["name"]
        jump startevent
    "I couldn't call that event. Check the spelling and case (it's case sensitive, for example 'BE001')"
    jump debugmenu

label setflag:
    $setFlag(debuginput, True)
    jump debugmenu

label unsetflag:
    $setFlag(debuginput, False)
    jump debugmenu

label settimeflag:
    $debugSetTimeFlag(debuginput, True)
    jump debugmenu

label unsettimeflag:
    $debugSetTimeFlag(debuginput, False)
    jump debugmenu

label daymenu:
    scene black with fade
    python:
        renpy.choice_for_skipping()
        showQuickMenu = False
        activeevent = ""
        eventname = ""
        eventchoices = rollEvents()
        cleanupCostumes()
    stop sound
    play music Daymenu
    window hide None
    call screen daymenu with fade
    window show None

#Don't change day or events
label daymenu_noadvance:
    scene black
    window hide None
    call screen daymenu
    window show None

label debugmenu:
    scene black
    window hide None
    call screen debugmenu
    window show None

label debugvarlist:
    scene black
    window hide None
    call screen debugvarlist
    window show None

label debugflaglist:
    scene black
    window hide None
    call screen debugflaglist
    window show None

label debugclearedeventlist:
    scene black
    window hide None
    call screen debugclearedeventlist
    window show None

label debugtimeflaglist:
    scene black
    window hide None
    call screen debugtimeflaglist
    window show None

label startevent:
    stop music
    play sound EventStart
    scene black with dissolve
    pause .5
    python:
        highlitevent = ""
        gametime = TimeEnum.DAY
        AEOutfit = OutfitEnum.DEFAULT
        BEOutfit = OutfitEnum.DEFAULT
        FMGOutfit = OutfitEnum.DEFAULT
        GTSOutfit = OutfitEnum.DEFAULT
        PRGOutfit = OutfitEnum.DEFAULT
        WGOutfit = OutfitEnum.DEFAULT
        MCOutfit = OutfitEnum.DEFAULT
        TakoOutfit = OutfitEnum.DEFAULT
        TomoOutfit = OutfitEnum.DEFAULT
        MinoriOutfit = OutfitEnum.DEFAULT
        NatsOutfit = OutfitEnum.DEFAULT
        OkishoOutfit = OutfitEnum.DEFAULT
        SakuraOutfit = OutfitEnum.DEFAULT
        RyokoOutfit = OutfitEnum.DEFAULT
        JinekoOutfit = OutfitEnum.DEFAULT
        DaitaroOutfit = OutfitEnum.DEFAULT
        TakamuraOutfit = OutfitEnum.DEFAULT
        KanamiOutfit = OutfitEnum.DEFAULT
        clearedevents.append(activeevent)
        updateSP()
        showQuickMenu = True
        renpy.block_rollback()
        save_name = eventlibrary[activeevent]["name"]
        renpy.jump(activeevent)

label train:
    stop music
    $gametime = TimeEnum.DAY
    $renpy.block_rollback()
    $spspent += 1
    $showQuickMenu = True
    if activeevent == "Athletics":
        jump trainathletics
    elif activeevent == "Art":
        jump trainart
    elif activeevent == "Academics":
        jump trainacademics
    else:
        $spspent -= 1
        "Error: Unknown skill selected. ID selected was [activeevent]. Please report to your local coder."
        jump daymenu

label trainathletics:
    scene Track with fade
    $tmp = renpy.random.randint(1, 2)
    if tmp == 1:
        "I ran around for a while."
    elif tmp == 2:
        "I lifted weights for a while."
    if getSkill("Athletics") < 5:
        "I'm pretty out of shape, so it was exhausting, but it was a good workout."
    else:
        "It wasn't too tough, but it was a good workout."
    $tmp = setSkill("Athletics", 1)
    "(Your athletics skill has increased to [tmp])"
    jump daymenu

label trainart:
    scene Dorm Interior with fade
    $tmp = renpy.random.randint(1, 2)
    if tmp == 1:
        "I spent some time doodling."
    elif tmp == 2:
        "I spent some time playing guitar."
    if getSkill("Art") < 5:
        "It didn't really turn out great, but I think I'm learning from my mistakes. It was pretty good practice."
    else:
        "It turned out alright. It was pretty good practice."
    $tmp = setSkill("Art", 1)
    "(Your art skill has increased to [tmp])"
    jump daymenu

label trainacademics:
    scene Library with fade
    $tmp = renpy.random.randint(1, 2)
    if tmp == 1:
        "I studied the next chapter in my math book."
    elif tmp == 2:
        "I studied the next chapter in my history book."
    if getSkill("Academics") < 5:
        "I'm having trouble remembering everything, but I did learn a few things. I hope I get a good score on the next test."
    else:
        "I feel like I'm starting to master this material. I hope I get a good score on the next test."
    $tmp = setSkill("Academics", 1)
    "(Your academics skill has increased to [tmp])"
    jump daymenu
