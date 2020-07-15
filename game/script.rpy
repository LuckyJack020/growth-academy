default persistent.enable_notifications = True

init python:
    config.use_cpickle = False
    #style.menu_choice_button.background = Frame("Graphics/ui/choice_bg_idle.jpg",28,9) #These two commands set the background of all in-game choice-buttons.
    #style.menu_choice_button.hover_background = Frame("Graphics/ui/choice_bg_hover.jpg",28,9)
    #style.menu_choice.color = "#fff" #These two commands set the color of the font in the in-game choice buttons.

    #style.menu_choice_button_disabled.background = Frame("Graphics/ui/choice_bg_disabled.jpg",28,9)

    eventlibrary = {}
    datelibrary = {}
    showQuickMenu = False
    girllist = ['BE', 'GTS', 'AE', 'FMG', 'BBW', 'PRG']
    locationlist = {
        #name of place: (map used, x/y pixel position)
        'arcade': ("town", (600,230)),
        'auditorium': ("school", (710,490)),
        'cafeteria': ("school", (770,490)),
        'campuscenter': ("school", (720,390)),
        'classroom': ("school", (810,390)),
        'clocktower': ("school", (715,430)),
        'cookingclassroom': ("school", (810,335)),
        'dormAE': ("school", (880,330)),
        'dormBBW': ("school", (880,330)),
        'dormBE': ("school", (880,330)),
        'dormPRG': ("school", (880,330)),
        'dormexterior': ("school", (850,375)),
        'dorminterior': ("school", (885,400)),
        'festival': ("town", (600,230)),
        'field': ("town", (600,230)),
        'gym': ("school", (630,325)),
        'hallway': ("school", (810,390)),
        'hillroad': ("town", (600,230)),
        'library': ("school", (810,370)),
        'musicclassroom': ("school", (810,400)),
        'office': ("school", (660,485)),
        'pool': ("school", (800,295)),
        'roof': ("school", (810,400)),
        'schoolfront': ("school", (715,520)),
        'schoolplanter': ("school", (720,325)),
        'schoolexterior': ("school", (715,520)),
        'supermarket': ("town", (600,230)),
        'town': ("town", (600,230)),
        'track': ("school", (715,270)),
        'woods': ("school", (600,230))
    }
    debugenabled = True
    debuginput = ""
    debugmappoint = False

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
    class ConditionEnum:
        EVENT, NOEVENT, FLAG, NOFLAG, AFFECTION, SKILL, TIMEFLAG, OR, ROUTELOCK, NOROUTELOCK = range(10)

    #EVENT: arg1 = (string) event code, true if event has been seen
    #NOEVENT: arg1 = (string) event code, true if event has NOT been seen
    #FLAG: arg1 = (string) flag name, true if flag has been raised
    #NOFLAG: arg1 = (string) flag name, true if flag has NOT been raised
    #AFFECTION: arg1 = (string, in girls list) girl, arg2 = ConditionEqualityEnum, arg3 = (int) affection score, true if the comparison is true (between girl specified in arg1's affection score and arg3)
    #SKILL: arg1 = (string, in skills list) skill, arg2 = ConditionEqualityEnum, arg3 = (int) skill score, true if the comparison is true (between skill specified in arg1 and arg3)
    #OR: arg1 = condition, arg2 = condition, returns true if either arg1 or arg2 are true
    #ROUTELOCK: arg1 = (string) character code, true if you're on that route (or, if empty string, true if not on any route)
    #NOROUTELOCK: arg1 = (string) character code, true if you're NOT on that route (or, if empty string, true if on any route)

    class EventTypeEnum:
        CORE, OPTIONAL, OPTIONALCORE = range(3)

    #CORE: Event is in someone's core route. Cannot be selected randomly.
    #OPTIONAL: Event is an optional event. Can be selected randomly.
    #OPTIONALCORE: Event is selected like an optional event, but is displayed like a core event in the UI.

    class PrioEnum:
        NONE, GIRL, ALL = range(3)

    #NONE: Not a priority. Other events available.
    #GIRL: Priority. Other events featuring the first girls in the girllist are not available.
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
            for g in girllist:
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
        if not girl in girllist and not girl == "RM":
            renpy.log("ERROR: Could not change affection: Girl %s does not exist" % girl)
            return
        affection[girl] += val
        if val > 0:
            img = "Graphics/ui/notification/" + girl + "-up.png"
        elif val < 0:
            img = "Graphics/ui/notification/" + girl + "-down.png"
        else:
            return
        showNotification(img)

    def getAffection(girl):
        if not girl in girllist and not girl == "RM":
            renpy.log("ERROR: Could not fetch affection: Girl %s does not exist" % girl)
            return 0
        return affection[girl]

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

    def setSizeDebug(mod):
        global globalsize, prgsize, minorsize
        globalsize += mod
        if globalsize < 1:
            globalsize = 1
        if globalsize > 6:
            globalsize = 6
        prgsize = globalsize
        minorsize = int(math.floor(globalsize/2))

    def getSkill(s):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
            return -1
        else:
            return skills[s]

    def showNotification(img):
        global activenotifications
        if not persistent.enable_notifications:
            return
        try:
            activenotifications
        except NameError:
            activenotifications = 0
        if activenotifications <= 2:
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
        if girl in girllist:
            routelock = girl

    def isRouteEnabled(girl):
        return routeenabled[girl] and (routelock == girl or routelock == "")

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

    def setSize(size):
        global globalsize, prgsize, minorsize
        if size > globalsize:
            globalsize = size
            if size != 3: #Aida's initial pregnancy doesn't follow globalsize schedule
                prgsize = size
            minorsize = int(math.floor(globalsize/2))

    #Edge case handler for Aida's initial pregnancy
    def setPregnant():
        global prgsize
        if 3 > prgsize:
            prgsize = 3

    def updateSP(event):
        global spmax
        global spspent
        if not "spmax" in globals():
            spmax = 0
            spspent = 0
        if not "sp" in eventlibrary[event]:
            return
        if eventlibrary[event]["sp"] <= spmax:
            return
        spmax = eventlibrary[event]["sp"]

    class MapLine(renpy.Displayable):
        def __init__(self, **kwargs):
            super(MapLine, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            render = renpy.Render(800, 600)
            if highlitevent == "" or highlitmenuchoice == -1:
                return render
            starty = 40 + (highlitmenuchoice * 60) #highlitmenuchoice
            end = locationlist[eventlibrary[highlitevent]["location"]][1]

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
            canvas.line("#000", (260, starty), (460, starty), 2) #horizontal, first point should be based on choice selected, second point should be horizontal some distance out
            canvas.line("#000", (460, starty), end, 2) #diagonal, first point here should be second point horizontal, second point should be the map point

            return render

label start:
    python:
        #Global Variables
        affection = {'BE': 0, 'GTS': 0, 'AE': 0, 'FMG': 0, 'BBW': 0, 'PRG': 0, 'RM': 0}
        prefgirl = ""
        skills = {"Athletics": 0, "Art": 0, "Academics": 0}
        globalsize = 1
        prgsize = 1
        minorsize = 1
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
        routeenabled = {'BE': True, 'GTS': True, 'AE': True, 'FMG': True, 'BBW': True, 'PRG': True}
        routelock = ""
        spmax = 0
        spspent = 0

        activenotifications = 0
        debugmapname = ""
    jump global000

label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return

#Remember to hide choicetimer for each choice made before the timer finishes.
screen choicetimer:
    timer 0.01 repeat True action If(timer_count > 0, true=SetVariable('timer_count', timer_count - 0.01), false=[Hide('choicetimer'), Jump(timer_jump)])

screen daymenu:
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
                        imagebutton idle im.Crop("Graphics/ui/icons/bgicon-%s.png" % eventlibrary[c]["location"], (0, 0, 250, 40)) action [SetVariable("activeevent", c), Jump("startevent")] hovered [SetVariable("highlitevent", c), SetVariable("highlitmenuchoice", i)] unhovered [SetVariable("highlitevent", ""), SetVariable("highlitmenuchoice", -1)]
                    else:
                        imagebutton idle im.Crop("Graphics/ui/icons/bgicon-missing.png" % eventlibrary[c]["location"], (0, 0, 250, 40)) action [SetVariable("activeevent", c), Jump("startevent")] hovered [SetVariable("highlitevent", c), SetVariable("highlitmenuchoice", i)] unhovered [SetVariable("highlitevent", ""), SetVariable("highlitmenuchoice", -1)]
                    hbox:
                        spacing -120
                        order_reverse True
                        if len(eventlibrary[c]["girls"]) == 0:
                            add im.Crop("Graphics/ui/icons/charicon-missing.png", (0, 0, 184, 40))
                        else:
                            for g in eventlibrary[c]["girls"]:
                                add im.Crop("Graphics/ui/icons/charicon-%s.png" % g, (0, 0, 184, 40))
                        #FIXME this looks awful and breaks tables, needs harder adjustments
                        #fixed:
                        #    frame:
                        #        xalign 0.5
                        #        yalign 0.5
                        #        background Solid(Color((0, 0, 0, 100)))
                        #        text eventlibrary[c]["name"]
    #map icons (for debug test)
    if debugmappoint:
        for loc in locationlist:
            fixed:
                xpos (locationlist[loc][1][0] - 12)
                ypos (locationlist[loc][1][1] - 12)
                imagebutton idle im.FactorScale("Graphics/ui/icons/BE-icon.png", .25) action [SetVariable("debugmapname", loc)]

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

    if debugmappoint:
        frame:
            xalign 0.5
            yalign 0.9
            background Solid(Color((0, 0, 0, 100)))
            text(debugmapname)

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
    timer 5.0 action [Hide("notification1"), SetVariable("activenotifications", activenotifications - 1)]

screen notification2(img):
    frame:
        xalign .8
        background None
        add img
        at notif_transform
    timer 5.0 action [Hide("notification2"), SetVariable("activenotifications", activenotifications - 1)]

screen notification3(img):
    frame:
        xalign .7
        background None
        add img
        at notif_transform
    timer 5.0 action [Hide("notification3"), SetVariable("activenotifications", activenotifications - 1)]

transform notif_transform:
    yalign -0.2
    linear 1.0 yalign 0.009
    pause 3
    linear 1.0 yalign -0.2

screen debugmenu:
    $debuginput = ""
    grid 3 15:
        xalign 0.5
        yalign 0.5

        text "Input:"
        input value VariableInputValue("debuginput")
        text ""

        textbutton "Start Event" action Jump("debugevent")
        textbutton "List Cleared Events" action Jump("debugclearedeventlist")
        textbutton "Map Points Toggle" action SetVariable("debugmappoint", not debugmappoint)

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

        text "BBW"
        hbox:
            textbutton "-" action Function(setAffection, "BBW", -1)
            text str(affection["BBW"])
            textbutton "+" action Function(setAffection, "BBW", 1)
        text getProgress("BBW")

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

screen debugflaglist:
    vbox:
        text debugListFlags()
        textbutton "Return" action Jump("debugmenu")

screen debugtimeflaglist:
    vbox:
        text debugListTimeFlags()
        textbutton "Return" action Jump("debugmenu")

screen debugclearedeventlist:
    vbox:
        text debugListClearedEvents()
        textbutton "Return" action Jump("debugmenu")

label debugevent:
    $renpy.block_rollback()
    if debuginput in eventlibrary:
        $activeevent = debuginput
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
    python:
        renpy.choice_for_skipping()
        showQuickMenu = False
        activeevent = ""
        eventchoices = rollEvents()
    scene black with fade
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
        minorsize = int(math.floor(globalsize/2)) #backwards compatibility
        clearedevents.append(activeevent)
        updateSP(activeevent)
        showQuickMenu = True
        renpy.block_rollback()
        renpy.jump(activeevent)

label train:
    stop music
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
