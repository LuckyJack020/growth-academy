default persistent.enable_notifications=2
default persistent.enable_nsfw=True
default AEOutfit = OutfitEnum.DEFAULT
default BEOutfit = OutfitEnum.DEFAULT
default FMGOutfit = OutfitEnum.DEFAULT
default GTSOutfit = OutfitEnum.DEFAULT
default PRGOutfit = OutfitEnum.DEFAULT
default WGOutfit = OutfitEnum.DEFAULT
default TakoOutfit = OutfitEnum.DEFAULT
default TomoOutfit = OutfitEnum.DEFAULT
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

#Custom ATL-based move transition for character sprites. Allows for movement WHILE dialogue is shown.
#xcenter value (basically the same as what value between 0.00 and 1.00 along the x-axis) is passed as variable.
#if combining with "Transform(xzoom=+-1)", separate into two different "show ______ at" statements
#error happens whenever xzoom is set to +1 only, but for consistency's sake; we'll separate them regardless.

transform altMove (xSp, xCen):
    linear xSp xcenter xCen

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

init python:
    preferences.set_volume("music", 0.65)
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
        'arcade': ("town", (1100,650)),
        'auditorium': ("school", (470,560)),
        'bakery': ("town", (1100,650)),
        'ballroom': ("town", (1100,650)),
        'businterior': ("town", (1100,650)),
        'cafeteria': ("school", (655,570)),
        'campuscenter': ("school", (570,390)),
        'classroom': ("school", (750,280)),
        'clocktower': ("school", (570,500)),
        'cookingclassroom': ("school", (740,490)),
        'dock': ("school", (1100,650)),
        'dormAE': ("school", (870,300)),
        'dormWG': ("school", (870,280)),
        'dormBE': ("school", (870,260)),
        'dormPRG': ("school", (870,280)),
        'dormFMG': ("school", (870,300)),
        'dormexterior': ("school", (860,375)),
        'dormhallway': ("school", (870,250)),
        'dorminterior': ("school", (880,380)),
        'facultyroom': ("school", (880,380)),
        'festival': ("town", (1100,650)),
        'field': ("town", (1100,650)),
        'frozenbeach': ("town", (1100,650)),
        'giantdorminterior': ("town", (950,100)),
        'gym': ("school", (730,220)),
        'hallway': ("school", (745,375)),
        'hillroad': ("town", (1100,650)),
        'infodesk': ("school", (590,590)),
        'lakeroad': ("school", (460,120)),
        'library': ("school", (490,560)),
        'lockers': ("school", (730,220)),
        'musicclassroom': ("school", (740,490)),
        'nurseoffice': ("school", (590,590)),
        'okinawa': ("town", (1100,650)),
        'office': ("school", (590,590)),
        'park': ("town", (1100,650)),
        'pool': ("school", (440,165)),
        'roof': ("school", (750,375)),
        'schoolfront': ("school", (570,620)),
        'schoolplanter': ("school", (570,265)),
        'schoolexterior': ("school", (715,650)),
        'summer-beach': ("town", (570,620)),
        'summer-guestbedroom': ("town", (570,620)),
        'supermarket': ("town", (1100,650)),
        'town': ("town", (1100,650)),
        'tokyo': ("town", (1100,650)),
        'track': ("school", (570,165)),
        'unknown': ("school", (550, 550)),
        'waterpark': ("town", (1100,650)),
        'woods': ("school", (460,120))
    }
    debugenabled = True
    debuginput = ""

    import math





    class Shaker(object):       #This is Python code to implement a feature to shake the screen around at random, not just in one direction like with the punch commands

        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child

        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)

        return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

    Shake = renpy.curry(_Shake)

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
        TRADITIONAL = "traditional"
        WORK = "work"
        NOHAT = "nohat"

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
            img = "Graphics/ui/notification/" + girl + "-up.png"
        elif val < 0:
            img = "Graphics/ui/notification/" + girl + "-down.png"
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
                img = "Graphics/ui/notification/" + girl + "-win.png"
                showNotification(img)
                return True
            else:
                img = "Graphics/ui/notification/" + girl + "-fail.png"
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
                img = "Graphics/ui/notification/" + s + "-up.png"
            else:
                img = "Graphics/ui/notification/" + s + "-down.png"
            showNotification(img)
            return skills[s]

    def setSkillDebug(s, val):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
        else:
            skills[s] += val
            if val >= 0:
                img = "Graphics/ui/notification/" + s + "-up.png"
            else:
                img = "Graphics/ui/notification/" + s + "-down.png"
            showNotification(img)

    def setSizeDebug(mod):
        global globalsize, prgsize
        globalsize += mod
        if globalsize < 1:
            globalsize = 1
        if globalsize > 6:
            globalsize = 6
        prgsize = globalsize
        #updateMinorSizes() #change after backwards compatibility is broken

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
                img = "Graphics/ui/notification/" + s + "-win.png"
                showNotification(img)
                return True
            else:
                img = "Graphics/ui/notification/" + s + "-fail.png"
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
        if (AEOutfit == OutfitEnum.NUDE or AEOutfit == OutfitEnum.EPILOGUEBAD) and not isNSFW():
            AEOutfit = AEPrevOutfit
        elif AENsfw and isNSFW():
            AEOutfit = AENsfwOutfit

        if BEOutfit == OutfitEnum.NUDE and not isNSFW():
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
        #updateMinorSizes(newsize) #change after backwards compatibility is broken

    def updateMinorSizes(newsize):
        global minorsizes, legalsizes
        legalsizes = {
            "Yuki": [1, 2, 3, 4, 5, 6],
            "Jineko": [1, 2, 3, 4, 5, 6],
            "Natsuko": [1, 2, 3, 4, 5, 6],
            "Okisho": [1, 2, 3, 4, 5, 6],
            "Kanami": [1, 2, 3, 4, 5, 6],
            "Tako": [1, 2, 3, 4, 5, 6],
            "Tomoko": [1, 2, 3, 4, 5, 6],
            "Sakura": [1, 2, 3, 4, 5, 6]
        }

        try: #backwards compatibility, remove later
            if instanceof(minorsizes, int):
                minorsizes = {}
        except NameError:
            minorsizes = {}
        for k in legalsizes.keys():
            if k not in minorsizes: #backwards compatibility, remove much later (when we stop adding minor characters)
                minorsizes[k] = legalsizes[k][-1]
            if newsize in legalsizes[k]:
                minorsizes[k] = newsize

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
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.BEND or o == OutfitEnum.EPILOGUEGOOD or o == OutfitEnum.DRESS or o == OutfitEnum.TIRED or o == OutfitEnum.CASUAL:
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
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.CASUAL or o == OutfitEnum.CASUAL2 or o == OutfitEnum.DRESS or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMSUIT:
            BENsfw = False
            BEOutfit = o
        elif o == OutfitEnum.NUDE:
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
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.CASUAL or o == OutfitEnum.DRESS or o == OutfitEnum.GYM or o == OutfitEnum.RIPPED or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMSUIT:
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
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.DRESS or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMSUIT or o == OutfitEnum.COW or o == OutfitEnum.PAJAMAS:
            PRGNsfw = False
            PRGOutfit = o
        elif o == OutfitEnum.NUDE:
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
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.DRESS or o == OutfitEnum.CASUAL or o == OutfitEnum.CASUAL2 or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMCAP or o == OutfitEnum.SWIMSUIT or o == OutfitEnum.SUMINT or o == OutfitEnum.SUMEXT or o == OutfitEnum.SUMINTSG or o == OutfitEnum.SUMEXTSG:
            WGNsfw = False
            WGOutfit = o
        elif o == OutfitEnum.NUDE:
            WGNsfw = True
            WGNsfwOutfit = o
            if isNSFW():
                WGPrevOutfit = WGOutfit
                WGOutfit = o

    def setTakoOutfit(o):
        global TakoOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.CASUAL or o == OutfitEnum.NOHAT:
            TakoOutfit = o

    def setTomoOutfit(o):
        global TomoOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.CASUAL:
            TomoOutfit = o

    def setNatsOutfit(o):
        global NatsOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.ATHLETIC or o == OutfitEnum.GYM or o == OutfitEnum.SWIM or o == OutfitEnum.SWIMSUIT:
            NatsOutfit = o

    def setKanamiOutfit(o):
        global KanamiOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.SWIMSUIT:
            KanamiOutfit = o

    def setOkishoOutfit(o):
        global OkishoOutfit
        if o == OutfitEnum.DEFAULT or o == OutfitEnum.CASUAL:
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
            #    img = im.FactorScale("Graphics/ui/icons/minor-icon.png", .25)
            #else:
            #    img = im.FactorScale("Graphics/ui/icons/%s-icon.png" % eventlibrary[highlitevent]["girls"][0], .25)
            #child_render = renpy.render(img, 25, 25, st, at)
            #iconend = (end[0] - 12, end[1] - 12)
            #render.blit(child_render, iconend)

            #draw line
            canvas = render.canvas()
            canvas.line("#000", (260, starty), (360, starty), 2) #horizontal, first point should be based on choice selected, second point should be horizontal some distance out
            canvas.line("#000", (360, starty), end, 2) #diagonal, first point here should be second point horizontal, second point should be the map point

            return render

label start:
    python:
        #Global Variables
        affection = {'BE': 0, 'GTS': 0, 'AE': 0, 'FMG': 0, 'WG': 0, 'PRG': 0, 'RM': 0, 'TM': 0}
        prefgirl = ""
        skills = {"Athletics": 0, "Art": 0, "Academics": 0}
        globalsize = 1
        prgsize = 1
        minorsizes = {'Yuki': 1, 'Jineko': 1, 'Natsuko': 1, 'Okisho': 1, 'Kanami': 1, 'Tako': 1, 'Tomoko': 1, 'Sakura': 1}
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
        AENsfw = False
        BENsfw = False
        FMGNsfw = False
        GTSNsfw = False
        PRGNsfw = False
        WGNsfw = False
        AEOutfit = OutfitEnum.DEFAULT
        BEOutfit = OutfitEnum.DEFAULT
        FMGOutfit = OutfitEnum.DEFAULT
        GTSOutfit = OutfitEnum.DEFAULT
        PRGOutfit = OutfitEnum.DEFAULT
        WGOutfit = OutfitEnum.DEFAULT
        TakoOutfit = OutfitEnum.DEFAULT
        TomoOutfit = OutfitEnum.DEFAULT
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
        AENsfw = False
        BENsfw = False
        FMGNsfw = False
        GTSNsfw = False
        PRGNsfw = False
        WGNsfw = False
        AEOutfit = OutfitEnum.DEFAULT
        BEOutfit = OutfitEnum.DEFAULT
        FMGOutfit = OutfitEnum.DEFAULT
        GTSOutfit = OutfitEnum.DEFAULT
        PRGOutfit = OutfitEnum.DEFAULT
        WGOutfit = OutfitEnum.DEFAULT
        TakoOutfit = OutfitEnum.DEFAULT
        TomoOutfit = OutfitEnum.DEFAULT
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
    add "Graphics/ui/map/map_school.png"

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
                        imagebutton idle Crop((0, 0, 250, 40), "Graphics/ui/icons/bgicon-%s.png" % eventlibrary[c]["location"]) action [SetVariable("activeevent", c), SetVariable("eventname", eventlibrary[c]["name"]), Jump("startevent")] hovered [SetVariable("highlitevent", c), SetVariable("highlitmenuchoice", i)] unhovered [SetVariable("highlitevent", ""), SetVariable("highlitmenuchoice", -1)]
                    else:
                        imagebutton idle Crop((0, 0, 250, 40), "Graphics/ui/icons/bgicon-missing.png") action [SetVariable("activeevent", c), SetVariable("eventname", eventlibrary[c]["name"]), Jump("startevent")] hovered [SetVariable("highlitevent", c), SetVariable("highlitmenuchoice", i)] unhovered [SetVariable("highlitevent", ""), SetVariable("highlitmenuchoice", -1)]
                    hbox:
                        spacing -140
                        order_reverse True
                        if len(eventlibrary[c]["girls"]) == 0:
                            add Crop((0, 0, 184, 40), "Graphics/ui/icons/charicon-missing.png")
                        else:
                            for g in eventlibrary[c]["girls"]:
                                add Crop((0, 0, 184, 40), "Graphics/ui/icons/charicon-%s.png" % g)
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
        text "Free Periods: " + str(spmax - spspent) xalign 0.05 yalign 0.845 color Color((0, 0, 0))
        if spmax > spspent:
            imagebutton idle "Graphics/ui/map/athletics.png" xalign 0.05 yalign 0.95 action [SetVariable("activeevent", "Athletics"), Jump("train")]
            imagebutton idle "Graphics/ui/map/art.png" xalign 0.15 yalign 0.95 action [SetVariable("activeevent", "Art"), Jump("train")]
            imagebutton idle "Graphics/ui/map/academics.png" xalign 0.25 yalign 0.95 action [SetVariable("activeevent", "Academics"), Jump("train")]

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
        text getProgress("BE")

        text "GTS"
        hbox:
            textbutton "-" action Function(setAffection, "GTS", -1)
            text str(affection["GTS"])
            textbutton "+" action Function(setAffection, "GTS", 1)
        text getProgress("GTS")

        text "AE"
        hbox:
            textbutton "-" action Function(setAffection, "AE", -1)
            text str(affection["AE"])
            textbutton "+" action Function(setAffection, "AE", 1)
        text getProgress("AE")

        text "FMG"
        hbox:
            textbutton "-" action Function(setAffection, "FMG", -1)
            text str(affection["FMG"])
            textbutton "+" action Function(setAffection, "FMG", 1)
        text getProgress("FMG")

        text "WG"
        hbox:
            textbutton "-" action Function(setAffection, "WG", -1)
            text str(affection["WG"])
            textbutton "+" action Function(setAffection, "WG", 1)
        text getProgress("WG")

        text "PRG"
        hbox:
            textbutton "-" action Function(setAffection, "PRG", -1)
            text str(affection["PRG"])
            textbutton "+" action Function(setAffection, "PRG", 1)
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
        updateMinorSizes(globalsize)
        highlitevent = ""
        gametime = TimeEnum.DAY
        AEOutfit = OutfitEnum.DEFAULT
        BEOutfit = OutfitEnum.DEFAULT
        FMGOutfit = OutfitEnum.DEFAULT
        GTSOutfit = OutfitEnum.DEFAULT
        PRGOutfit = OutfitEnum.DEFAULT
        WGOutfit = OutfitEnum.DEFAULT
        TakoOutfit = OutfitEnum.DEFAULT
        TomoOutfit = OutfitEnum.DEFAULT
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
    scene Library with fade
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
