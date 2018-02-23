init python:
    config.use_cpickle = False
    style.menu_choice_button.background = Frame("choice_bg_idle.jpg",28,9) #These two commands set the background of all in-game choice-buttons.
    style.menu_choice_button.hover_background = Frame("choice_bg_hover.jpg",28,9)
    style.menu_choice.color = "#fff" #These two commands set the color of the font in the in-game choice buttons.
    
    style.menu_choice_button_disabled.background = Frame("choice_bg_disabled.jpg",28,9)
    
    import datetime
    
    eventlibrary = {}
    presetdays = {}
    datelibrary = {}
    girllist = ['BE', 'GTS', 'AE', 'FMG', 'BBW', 'PRG']
    girlsizes = {'BE': 1, 'GTS': 1, 'AE': 1, 'FMG': 1, 'BBW': 1, 'PRG': 1}
    locationlist = ['auditorium', 'cafeteria', 'campuscenter', 'classroom', 'cookingclassroom', 'dormexterior', 'dorminterior', 'festival', 'gym', 'hallway', 'library', 'office', 'pool', 'roof', 'schoolfront', 'schoolplanter', 'track', 'musicclassroom']
    debuginfo = False
    debugenabled = False
    debugscene = ""
    debugsceneinput = ""
    debugpriorities = ""
    gametime = datetime.date(2005, 4, 4)
    
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
    
    class WeightedChoicePicker(object): #Class for weighted selection (used for favored girl selection)
            def __init__(self, dict):
                #"dict" is a dict of {"value": chance, "value": chance...}
                self.dict = dict
                self.sum = sum([ val for key, val in dict.iteritems()])
           
            def pick(self):
                rand = renpy.random.uniform(0, self.sum)
                sum = 0.0
                ret = None
                for key, val in self.dict.iteritems():
                    sum += val
                    if rand < sum:
                        ret = key
                        break
                if ret == None:
                    ret = key
               
                self.sum -= val
                del self.dict[key]
                return ret
               
            def hasKeysLeft(self):
                return len(self.dict) != 0
    #Condition enums/stuff
    class ConditionEnum:
        EVENT, NOEVENT, FLAG, NOFLAG, GAMETIME, ISDAYTIME, ISNIGHTTIME, AFFECTION, SKILL, PRESET, OR = range(11)
    
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
            elif c[0] == ConditionEnum.NOFLAG:
                if c[1] not in flags:
                    continue
                else:
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.GAMETIME:
                if c[1] == ConditionEqualityEnum.LESSTHAN:
                    if gametime >= c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.GREATERTHAN:
                    if gametime <= c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.LESSTHANEQUALS:
                    if gametime > c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.GREATERTHANEQUALS:
                    if gametime < c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.EQUALS:
                    if gametime != c[2]:
                        criteriavalid = False
                        break
                    else:
                        continue
                else:
                    renpy.log("Invalid criteria equality enum ID: %s" % str(c[1]))
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.ISDAYTIME:
                if gametime_eve:
                  criteriavalid = False
                  break
                else:
                    continue
            elif c[0] == ConditionEnum.ISNIGHTTIME:
                if not gametime_eve:
                    criteriavalid = False
                    break
                else:
                    continue
            elif c[0] == ConditionEnum.AFFECTION:
                if c[2] == ConditionEqualityEnum.LESSTHAN:
                    if getAffection(c[1]) >= int(c[3]):
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
                else:
                    renpy.log("Invalid criteria equality enum ID: %s" % str(c[2]))
                    criteriavalid = False
                    break
            elif c[0] == ConditionEnum.PRESET:
                if gametime in presetdays.keys():
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
            else:
                renpy.log("Invalid criteria enum ID: %s" % str(c[0]))
                criteriavalid = False
                break
        return criteriavalid    
                
    #Other misc functions
    def setAffection(girl, val):
        if not girl in girllist and not girl == "RM":
            renpy.log("ERROR: Could not change affection: Girl %s does not exist" % girl)
            return
        affection[girl] += val
        
    def getAffection(girl):
        if not girl in girllist and not girl == "RM":
            renpy.log("ERROR: Could not fetch affection: Girl %s does not exist" % girl)
            return 0
        return affection[girl]
        
    def isEventCleared(event):
        return event in clearedevents
        
    def setScenecount(girl, val):
        if not girl in girllist:
            renpy.log("ERROR: Could not change affection: Girl %s does not exist" % girl)
            return
        scenecounter[girl] += val
        
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
            return None
    
    def getSize(g):
        if g in girllist:
            return girlsizes[g]
        else:
            return -1
    
    def updateSizes():
        for g in girllist:
            for i in range(6, 1, -1):
                if i == 1:
                    girlsizes[g] = i
                    break
                s = g + '_size_' + str(i)
                if gametime > datelibrary[s]:
                    girlsizes[g] = i
                    break
        
    def setSkill(s, val):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
            return -1
        else:
            skills[s] += val
            return skills[s]
            
    def getSkill(s):
        if s not in skills.keys():
            renpy.log("Unknown skill ID: %s" % s)
            return -1
        else:
            return skills[s]
    
    def getTimeString():
        s = gametime.strftime("%a %B %d, 20XX")
        if gametime_eve:
            s += " (Evening)"
        else:
            s += " (Morning)"
        return s
        
    def getTimeCode():
        s = str(gametime.month) + "-" + str(gametime.day)
        if gametime_eve:
            s += "-T"
        else:
            s += "-F"
        return s
            
    def pickPreferredGirl():
        sc = scenecounter.copy()
        scsort = sorted(sc.iteritems(), key=lambda x: x[1], reverse=True)
        # Finally, we pick out the heaviest items by picking off the heaviest side of the array.
        topweight = scsort[0][1]
        weightlist = {}
        weightlist[scsort[0][0]] = 3
        i = 1
        while i < len(scsort) and scsort[i][1] + 2 >= topweight:
            if scsort[i][1] == topweight:
                weightlist[scsort[i][0]] = 3
            elif scsort[i][1] + 1 == topweight:
                weightlist[scsort[i][0]] = 2
            else:
                weightlist[scsort[i][0]] = 1
            i += 1
        picker = WeightedChoicePicker(weightlist)
        return picker.pick()

label start:
    python:
        #Global Variables
        affection = {'BE': 0, 'GTS': 0, 'AE': 0, 'FMG': 0, 'BBW': 0, 'PRG': 0, 'RM': 0}
        skills = {"Athletics": 0, "Art": 0, "Academics": 0}
        scenecounter = {'BE': 5, 'GTS': 5, 'AE': 5, 'FMG': 5, 'BBW': 5, 'PRG': 5}
        globalsize = 1
        flags = []
        vars = {}
        scenecountmax = 10
        eventchoices = []
        activeevent = ""
        gametime = datetime.date(2005, 4, 4)
        gametime_eve = False
        eventpool = []
        preferredpool = []
        clearedevents = []
        prefgirl = ""
        freeday = True
        prefscene = True
    jump global000

label splashscreen:
    scene black
    with Pause(1)
    
    show splash with dissolve
    with Pause(2)
    
    scene black with dissolve
    with Pause(1)
    
    return

screen choicetimer:
    timer 0.01 repeat True action If(timer_count > 0, true=SetVariable('timer_count', timer_count - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

screen daymenu:
    if gametime_eve:
        add "Graphics/ui/menubg-evening.png"
    else:
        add "Graphics/ui/menubg-day.png"
    
    if debuginfo:
        vbox:
            xalign 0
            yalign 0
            text ("Debug info:")
            text ("Prefgirl: %s" % prefgirl)
            text ("Preferred scenes exist? %s" % prefscene)
            text ("Girls w/ Priority: %s" % debugpriorities)
            text ("Scene limit: %d" % scenecountmax)
            text ("Girl/Aff/Scenes")
            text ("BE %(aff)d %(scene)d" % {"aff": affection["BE"], "scene": scenecounter["BE"]})
            text ("GTS %(aff)d %(scene)d" % {"aff": affection["GTS"], "scene": scenecounter["GTS"]})
            text ("AE %(aff)d %(scene)d" % {"aff": affection["AE"], "scene": scenecounter["AE"]})
            text ("FMG %(aff)d %(scene)d" % {"aff": affection["FMG"], "scene": scenecounter["FMG"]})
            text ("BBW %(aff)d %(scene)d" % {"aff": affection["BBW"], "scene": scenecounter["BBW"]})
            text ("PRG %(aff)d %(scene)d" % {"aff": affection["PRG"], "scene": scenecounter["PRG"]})
            text ("Athletics: %d" % skills["Athletics"])
            text ("Art: %d" % skills["Art"])
            text ("Academics: %d" % skills["Academics"])
            text ("Scenes:")
            for e in eventchoices:
                text ("%s" % e)
    
    text(getTimeString()):
        xalign 0.1
        yalign 0.1
        
    #event choices (3-choice day)
    if len(eventchoices) <= 3:
        vbox:
            xalign 0.5
            ypos 120
            spacing 60
            for c in eventchoices:
                fixed:
                    xmaximum 600
                    ymaximum 60
                    if eventlibrary[c]["location"] in locationlist:
                        imagebutton idle "Graphics/ui/bgicon-%s.png" % eventlibrary[c]["location"] action [SetVariable("activeevent", c), Jump("startevent")]
                    else:
                        add "Graphics/ui/bgicon-missing.png"
                    hbox:
                        spacing -120
                        order_reverse True
                        if len(eventlibrary[c]["girls"]) == 0:
                            add "Graphics/ui/charicon-missing.png"
                        else:
                            for g in eventlibrary[c]["girls"]:
                                add "Graphics/ui/charicon-%s.png" % g
                
    #event choices (6-choice day)
    if len(eventchoices) > 3:
        grid 2 3:
            xalign 0.5
            ypos 120
            spacing 60
            for c in eventchoices:
                button:
                    xmaximum 250
                    ymaximum 60
                    action [SetVariable("activeevent", c), Jump("startevent")]
                    if eventlibrary[c]["location"] in locationlist:
                        add "Graphics/ui/bgicon-%s.png" % eventlibrary[c]["location"] crop(0, 0, 250, 60)
                    else:
                        add "Graphics/ui/bgicon-missing.png"
                    hbox:
                        spacing -120
                        order_reverse True
                        if len(eventlibrary[c]["girls"]) == 0:
                            add "Graphics/ui/charicon-missing.png"
                        else:
                            for g in eventlibrary[c]["girls"]:
                                add "Graphics/ui/charicon-%s.png" % g
    
    #studying activities (non-special day)
    if freeday:
        textbutton "Train Athletics" xalign 0.1 yalign 0.8 action [SetVariable("activeevent", "Athletics"), Jump("train")]
        textbutton "Train Art" xalign 0.5 yalign 0.8 action [SetVariable("activeevent", "Art"), Jump("train")]
        textbutton "Train Academics" xalign 0.9 yalign 0.8 action [SetVariable("activeevent", "Academics"), Jump("train")]
            
    #debug menu toggle (if debug is enabled)
    if debugenabled:
        textbutton "Toggle Debug" xalign 0.9 yalign 0.9 action SetVariable("debuginfo", not debuginfo)
        textbutton "Enter Debug Menu" xalign 0.9 yalign 0.95 action Jump("debugmenu")
        
screen debugmenu:
    $debugscene = ""
    $debugsceneinput = ""
    grid 3 9:
        xalign 0.5
        yalign 0.5
        
        text "Show Scene:"
        input value VariableInputValue("debugsceneinput")
        textbutton "Go!" action Jump("debugscene")
        
        text "Girl"
        text "Affection"
        text "Scenes"

        text "BE"
        hbox:
            textbutton "-" action Function(setAffection, "BE", -1)
            text str(affection["BE"])
            textbutton "+" action Function(setAffection, "BE", 1)
            
        hbox:
            textbutton "-" action Function(setScenecount, "BE", -1)
            text str(scenecounter["BE"])
            textbutton "+" action Function(setScenecount, "BE", 1)
            
        text "GTS"
        hbox:
            textbutton "-" action Function(setAffection, "GTS", -1)
            text str(affection["GTS"])
            textbutton "+" action Function(setAffection, "GTS", 1)
            
        hbox:
            textbutton "-" action Function(setScenecount, "GTS", -1)
            text str(scenecounter["GTS"])
            textbutton "+" action Function(setScenecount, "GTS", 1)
            
        text "AE"
        hbox:
            textbutton "-" action Function(setAffection, "AE", -1)
            text str(affection["AE"])
            textbutton "+" action Function(setAffection, "AE", 1)
            
        hbox:
            textbutton "-" action Function(setScenecount, "AE", -1)
            text str(scenecounter["AE"])
            textbutton "+" action Function(setScenecount, "AE", 1)
            
        text "FMG"
        hbox:
            textbutton "-" action Function(setAffection, "FMG", -1)
            text str(affection["FMG"])
            textbutton "+" action Function(setAffection, "FMG", 1)
            
        hbox:
            textbutton "-" action Function(setScenecount, "FMG", -1)
            text str(scenecounter["FMG"])
            textbutton "+" action Function(setScenecount, "FMG", 1)

        text "BBW"
        hbox:
            textbutton "-" action Function(setAffection, "BBW", -1)
            text str(affection["BBW"])
            textbutton "+" action Function(setAffection, "BBW", 1)
            
        hbox:
            textbutton "-" action Function(setScenecount, "BBW", -1)
            text str(scenecounter["BBW"])
            textbutton "+" action Function(setScenecount, "BBW", 1)
            
        text "PRG"
        hbox:
            textbutton "-" action Function(setAffection, "PRG", -1)
            text str(affection["PRG"])
            textbutton "+" action Function(setAffection, "PRG", 1)
            
        hbox:
            textbutton "-" action Function(setScenecount, "PRG", -1)
            text str(scenecounter["PRG"])
            textbutton "+" action Function(setScenecount, "PRG", 1)
        
        #hbox:
        #    text "Athletics:"
        #    textbutton "-" action Function(setSkill, "Athletics", -1)
        #    text str(skills["Athletics"])
        #    textbutton "+" action Function(setSkill, "Athletics", 1)
            
        #hbox:
        #    text "Art:"
        #    textbutton "-" action Function(setSkill, "Art", -1)
        #    text str(skills["Art"])
        #    textbutton "+" action Function(setSkill, "Art", 1)
            
        #hbox:
        #    text "Academics:"
        #    textbutton "-" action Function(setSkill, "Academics", -1)
        #    text str(skills["Academics"])
        #    textbutton "+" action Function(setSkill, "Academics", 1)
        
        textbutton "Return to game" action Jump("daymenu_noadvance")
        text ""
        text ""
        
        
label debugscene:
    if debugsceneinput in eventlibrary:
        $activeevent = debugsceneinput
        jump startevent
    "I couldn't call that scene. Check the spelling and case (it's case sensitive, for example 'BE001')"
    jump debugmenu

label daymenu:
    $updateSizes()
    $renpy.choice_for_skipping()
    #Roll random events
    python:
        if gametime_eve:
            gametime_eve = False
            gametime += datetime.timedelta(days=1)
        else:
            gametime_eve = True
        
        eventchoices = []
        eventcount = 3
        prefpool = []
        allpool = []
        priorities = []
        prefscene = False
        #It's a preset day, don't worry about pools, just use whatever the preset says
        if getTimeCode() in presetdays.keys():
            eventchoices = presetdays[getTimeCode()]
            eventcount = min([5, len(allpool)])
            freeday = False
        #It's not a preset day, randomly select 3 events
        else:
            freeday = True
            #Determine preferred girl
            prefmax = 0
            prefgirl = pickPreferredGirl()
            
            #While we've figured out the preferred girl, update the weight limit, which is floor(average of all non-preferred girls) + 5
            tmpscenemax = 0
            for g in girllist:
                if g == prefgirl:
                    continue
                tmpscenemax += scenecounter[g]
            scenecountmax = math.floor(tmpscenemax / 5) + 5
            
            #Fill allpool (and prefpool, if applicable)
            for k, v in eventlibrary.iteritems():
                if k in clearedevents:
                    continue
                criteriavalid = checkCriteria(v["conditions"])
                if not criteriavalid:
                    continue
                if "priority" in v.keys() and v["priority"]:
                    for priogirl in v["girls"]: #If event is priority, add all girls to the priority list (if they aren't already)
                        if priogirl in priorities:
                            continue
                        priorities.append(priogirl)
                if prefgirl in v["girls"]:
                    prefscene = True
                    prefpool.append(k)
                allpool.append(k)

            #Scan for priorities and purge non-priorities
            if len(priorities) != 0:
                for e in allpool[:]: #use a copy of the list, python gets cranky if you modify a list you're iterating over
                    event = eventlibrary[e]
                    for g in event["girls"]:
                        if g in priorities:
                            if not "priority" in event.keys() or not event["priority"]:
                                allpool.remove(e)
                
                if prefgirl in priorities:
                    for e in prefpool[:]: #use a copy of the list, python gets cranky if you modify a list you're iterating over
                        event = eventlibrary[e]
                        if not "priority" in event.keys() or not event["priority"]:
                            prefpool.remove(e)
            
            #Select from preferred pool
            if len(prefpool) != 0:
                tmp = renpy.random.choice(prefpool)
                eventchoices.append(tmp)
                allpool.remove(tmp)
            elif len(allpool) != 0: #...or the allpool, if the preferred pool is empty
                tmp = renpy.random.choice(allpool)
                eventchoices.append(tmp)
                allpool.remove(tmp)
            
            #Pick 2 more "allpool" events
            if (len(allpool) >= 2):
                eventchoices += renpy.random.sample(allpool, 2)
            else:
                eventchoices += allpool
        debugpriorities = "".join(priorities)
    scene black
    window hide None
    call screen daymenu
    window show None
    
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

label startevent:
    python:
        if activeevent[0:10] != "specialday":
            for g in eventlibrary[activeevent]["girls"]:
                scenecounter[g] += 1
                if scenecounter[g] >= scenecountmax:
                    scenecounter[g] = scenecountmax

        clearedevents.append(activeevent)
        
    $renpy.block_rollback()
    $renpy.jump(activeevent)
    
label train:
    if activeevent == "Athletics":
        jump trainathletics
    elif activeevent == "Art":
        jump trainart
    elif activeevent == "Academics":
        jump trainacademics
    else:
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