init python:
    config.use_cpickle = False
    style.menu_choice_button.background = Frame("choice_bg_idle.jpg",28,9) #These two commands set the background of all in-game choice-buttons.
    style.menu_choice_button.hover_background = Frame("choice_bg_hover.jpg",28,9)
    style.menu_choice.color = "#fff" #These two commands set the color of the font in the in-game choice buttons.
    
    eventlibrary = {}
    girllist = ['BE', 'GTS', 'AE', 'FMG', 'BBW', 'PRG']
    
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
        EVENT, FLAG, GAMETIME, AFFECTION, SKILL = range(5)
    
    class ConditionEqualityEnum:
        EQUALS, NOTEQUALS, GREATERTHAN, LESSTHAN = range(4)
        
    def checkCriteria(clist):
        criteriavalid = True
        for c in clist:
            if c[0] == ConditionEnum.EVENT:
                if c[1] not in clearedevents:
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
            elif c[0] == ConditionEnum.GAMETIME:
                if c[1] == ConditionEqualityEnum.LESSTHAN:
                    if gametime >= int(c[2]):
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.GREATERTHAN:
                    if gametime <= int(c[2]):
                        criteriavalid = False
                        break
                    else:
                        continue
                elif c[1] == ConditionEqualityEnum.EQUALS:
                    if gametime != int(c[2]):
                        criteriavalid = False
                        break
                    else:
                        continue
                else:
                    renpy.log("Invalid criteria equality enum ID: %s" % str(c[1]))
                    criteriavalid = False
                    break
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
        
    def getSize():
        if gametime > 10:
            return 2
        else:
            return 1
            
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
        scenecounter = {'BE': 5, 'GTS': 5, 'AE': 5, 'FMG': 5, 'BBW': 5, 'PRG': 5}
        globalsize = 1
        flags = []
        scenecountmax = 10
        eventchoices = ["", "", ""]
        activeevent = ""
        gametime = 0
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
    
screen daymenu:    
    vbox:
        xalign 0
        yalign 0
        text ("Debug info:")
        text ("Girl/Aff/Scenes")
        text ("BE %(aff)d %(scene)d" % {"aff": affection["BE"], "scene": scenecounter["BE"]})
        text ("GTS %(aff)d %(scene)d" % {"aff": affection["GTS"], "scene": scenecounter["GTS"]})
        text ("AE %(aff)d %(scene)d" % {"aff": affection["AE"], "scene": scenecounter["AE"]})
        text ("FMG %(aff)d %(scene)d" % {"aff": affection["FMG"], "scene": scenecounter["FMG"]})
        text ("BBW %(aff)d %(scene)d" % {"aff": affection["BBW"], "scene": scenecounter["BBW"]})
        text ("PRG %(aff)d %(scene)d" % {"aff": affection["PRG"], "scene": scenecounter["PRG"]})
        text ("Prefgirl: %s" % prefgirl)
        text ("Scene limit: %d" % scenecountmax)
        text ("Preferred scenes exist? %s" % prefscene)
    
    vbox:
        xalign 0.5
        yalign 0.5
        
        text ("Day %d" % gametime)
        textbutton eventtext[0] action If(eventtext[0] != "", [SetVariable("activeevent", eventchoices[0]), Jump("startevent")])
        textbutton eventtext[1] action If(eventtext[1] != "", [SetVariable("activeevent", eventchoices[1]), Jump("startevent")])
        textbutton eventtext[2] action If(eventtext[2] != "", [SetVariable("activeevent", eventchoices[2]), Jump("startevent")])
    
    #fixed:
        #textbutton "Train A" xalign 0.3 yalign 0.7 action If(freeday, Jump("train"))
        #textbutton "Train B" xalign 0.5 yalign 0.7 action If(freeday, Jump("train"))
        #textbutton "Train C" xalign 0.7 yalign 0.7 action If(freeday, Jump("train"))

label daymenu:
    $globalsize = getSize()
    #Roll random events
    $gametime += 1
    python:        
        eventchoices = []
        eventtext = ["", "", ""]
        
        freeday = True
        #determine preferred girl
        prefmax = 0
        prefgirl = pickPreferredGirl()
        
        #while we've figured out the preferred girl, update the weight limit, which is floor(average of all non-preferred girls) + 5
        tmpscenemax = 0
        for g in girllist:
            if g == prefgirl:
                continue
            tmpscenemax += scenecounter[g]
        scenecountmax = math.floor(tmpscenemax / 5) + 5
        
        #fill the pools
        prefpool = []
        allpool = []
        priority = 0
        prefscene = False
        for k, v in eventlibrary.iteritems():
            if k in clearedevents:
                continue
            criteriavalid = checkCriteria(v["conditions"])
            if not criteriavalid:
                continue
            if "priority" in eventlibrary[k].keys():
                p = eventlibrary[k]["priority"]
            else:
                p = 0
            if p > priority: #if event has a higher priority, clear all pools and don't use prefgirl system
                freeday = False
                prefscene = False
                prefpool = []
                allpool = []
                priority = p
            if p == priority:
                if prefgirl in v["girls"] and priority == 0:
                    prefscene = True
                    prefpool.append(k)
                allpool.append(k)

        #select from the pools
        if len(prefpool) != 0:
            tmp = renpy.random.choice(prefpool)
            eventchoices.append(tmp)
            allpool.remove(tmp)
        elif len(allpool) != 0:
            tmp = renpy.random.choice(allpool)
            eventchoices.append(tmp)
            allpool.remove(tmp)
        else:
            eventchoices.append("")
        
        if (len(allpool) >= 2):
            eventchoices += renpy.random.sample(allpool, 2)
        else:
            eventchoices += allpool
                
        for i in [0, 1, 2]:
            if i >= len(eventchoices):
                break
            if eventchoices[i] == "":
                eventtext[i] = ""
                continue
            eventtext[i] = eventlibrary[eventchoices[i]]["name"] + ' ' + ' '.join(eventlibrary[eventchoices[i]]["girls"])
        if len(eventchoices) == 1:
            eventchoices.append("")
            eventchoices.append("")
        if len(eventchoices) == 2:
            eventchoices.append("")
        
    scene black
    window hide None
    call screen daymenu
    window show None

label startevent:
    python:
        if activeevent[0:10] != "specialday":
            for g in eventlibrary[activeevent]["girls"]:
                scenecounter[g] += 1
                if scenecounter[g] >= scenecountmax:
                    scenecounter[g] = scenecountmax

        clearedevents.append(activeevent)
        
    $renpy.jump(activeevent)