define FMG = Character('Akira', color="#FF9900")
define Chibuki = Character('Chibuki', color="#CC33FF")
define Takamura = Character('Takamura-Sensei', color="#FF9900")
define Cashier = Character('Cashier', color="#FF9900")
define Chie = Character('Chie', color="#FF9900")
define Fujimoto = Character('Fujimoto', color="#FF9900")

image FMG neutral = DynamicImage("Graphics/FMG/[globalsize]/neutral.png")
image FMG happy = DynamicImage("Graphics/FMG/[globalsize]/happy.png")
image FMG sad = DynamicImage("Graphics/FMG/[globalsize]/sad.png")
image FMG surprised = DynamicImage("Graphics/FMG/[globalsize]/surprised.png")
image FMG angry = DynamicImage("Graphics/FMG/[globalsize]/angry.png")
image FMG aroused = DynamicImage("Graphics/FMG/[globalsize]/aroused.png")
image FMG flex = DynamicImage("Graphics/FMG/[globalsize]/flex.png")

image Chibuki neutral = "Graphics/minor/chibuki-neutral.png"

init 2 python:
    #go over order again after implementing new scenes
    #go over order again after implementing new scenes
    #go over order again after implementing new scenes
    #Core
    eventlibrary['FMG001'] = {"name": "Tower of Athletics", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",              "priority": PrioEnum.NONE, "next": "FMG002", "obsflags": ["testday"],   "conditions": []}
    eventlibrary['FMG002'] = {"name": "An Off Day", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                               "location": "gym",              "priority": PrioEnum.NONE, "next": "FMG003", "obsflags": [],            "conditions": []}
    eventlibrary['FMG003'] = {"name": "Hallway Opportunity", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "hallway",          "priority": PrioEnum.NONE, "next": "FMG007", "obsflags": [],            "conditions": []}
    eventlibrary['FMG007'] = {"name": "Lunch and Hobbies", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "FMG008", "obsflags": [],            "conditions": []}
    eventlibrary['FMG008'] = {"name": "The Pencil OF DOOM!", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "dormexterior",     "priority": PrioEnum.NONE, "next": "FMG009", "obsflags": [],            "conditions": []}
    eventlibrary['FMG009'] = {"name": "Junk Food Junkie", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                         "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "FMG014", "obsflags": [],            "conditions": []}
    eventlibrary['FMG014'] = {"name": "A Problem Solver", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                         "location": "schoolplanter",    "priority": PrioEnum.NONE, "next": "FMG015", "obsflags": [],            "conditions": []}
    eventlibrary['FMG015'] = {"name": "", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                         "location": "town",             "priority": PrioEnum.NONE, "next": "FMG017", "obsflags": [],            "conditions": []}
    eventlibrary['FMG017'] = {"name": "Beware... The Curse", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "campuscenter",     "priority": PrioEnum.NONE, "next": "FMG018", "obsflags": [],            "conditions": []}
    eventlibrary['FMG018'] = {"name": "IT'S RAW!!!", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "cookingclassroom", "priority": PrioEnum.NONE, "next": "FMG019", "obsflags": [],            "conditions": []}
    eventlibrary['FMG019'] = {"name": "You Shine Like the Sun", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                   "location": "roof",             "priority": PrioEnum.NONE, "next": "FMG021", "obsflags": [],            "conditions": []}
    eventlibrary['FMG021'] = {"name": "EMUS!", "girls": ["FMG", "AE"], "type": EventTypeEnum.CORE,                                                    "location": "library",          "priority": PrioEnum.NONE, "next": "FMG022", "obsflags": [],            "conditions": []}
    eventlibrary['FMG022'] = {"name": "Akira end", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                "location": "library",          "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}
    
    #Optional
    eventlibrary['FMG004'] = {"name": "Journey of 1000 Miles", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                "location": "track",            "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG006'] = {"name": "Crying Over Spilled Milk", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                             "location": "gym",              "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG011'] = {"name": "Press A to Start", "girls": ["FMG", "BBW"], "type": EventTypeEnum.OPTIONAL,                              "location": "dormexterior",     "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}
    eventlibrary['FMG012'] = {"name": "Rubbing One Out", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                      "location": "gym",              "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG016'] = {"name": "Fate at the Café", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                         "location": "schoolplanter",    "priority": PrioEnum.NONE, "next": "", "obsflags": [],            "conditions": []}
    eventlibrary['FMGBBW001'] = {"name": "Conspiracies with a Side of Cupcakes", "girls": ["FMG", "BBW"], "type": EventTypeEnum.OPTIONAL,       "location": "town",             "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}
    
    eventlibrary['FMG005'] = {"name": "Despair in the Hallway", "girls": ["FMG"], "type": EventTypeEnum.OPTIONALCORE,                           "location": "hallway",          "priority": PrioEnum.GIRL, "next": "", "obsflags": ["aftertest"],       "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['FMG010'] = {"name": "The Bigger They Are...", "girls": ["FMG"], "type": EventTypeEnum.OPTIONALCORE,                            "location": "dormexterior",     "priority": PrioEnum.GIRL, "next": "", "obsflags": ["aftersize2"],      "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    
label FMG001:
    $setProgress("FMG", "FMG002")
    scene Track with fade #track might not be the right background?
    play music Schoolday
    "After thinking of what to do after class, I decided to check out the Athletics Area, so when I have P.E. I would know where it is."
    "Compared to the rest of the academy, the building itself was not only taller, but almost as wide as the rest of the school."
    "From how tall the windows were made the building looked least two or three stories tall."
    scene Gym with fade
    "I walked inside to see if it really was as big as it looked."
    "The inside was not what I thought it would look like, what I imagined to be a normal three story building turned out to be just one room that was three stories high."
    "The exercise equipment was unique, to say the least; while some did look normal, most of them came in extreme shapes and sizes."
    "One thing I also noticed was that the building was so empty that there was a lone echo coming from the far end of the building and once again curiosity drove me to follow where the source of the echo was coming from."
    "As I got closer to the source, I began to hear someone counting."
    UNKNOWN "...87...88..."
    "It sounded like a woman, but I couldn't make out who it was just yet."
    UNKNOWN "...92...93..."
    "After a minute of looking, I found that the source of noise was coming from a bench-pressing Akira."
    "From what I could guess, she was too focused on her workout to notice me walking towards her, or that she assumed it was just someone who was working out as well."
    show FMG angry with dissolve
    FMG "98...99...100!"
    "Akira then proceeded to put the weights back on the bar and moved off the bench press; it was only when she looked up she saw me watching her."
    show FMG neutral
    FMG "Well hey there..."
    extend "Um, your name was Keisuke, right?"
    MC "Indeed it is."
    FMG "All right, Keisuke, got it...So as I was saying...what brings you to these parts?"
    MC "Curiosity mostly, I wanted to checked out the Athletics Area to get a better layout of the school and when I got here I heard an echo that lead me to you."
    show FMG happy
    FMG "And here I was thinking you were here to check me out."
    "The way she said that sounded she was joking, but I just found it kinda awkward, still it would be a bit rude not to give some sort of reply."
    "My only response was a light chuckle and then silence. We stood there for about 30 seconds till I spoke up."
    MC "So Akira...how are you holding up?"
    show FMG neutral
    FMG "Huh, what do you mean?"
    MC "Well, I mean that we're going have these 'growths' affect the rest of our lives, so what I'm asking is how you're taking this?"
    show FMG happy
    FMG "Oh, in that case, I'm fine with it."
    MC "Huh, really?"
    show FMG neutral
    FMG "Yeah, I don't know if I will grow or not but if I do, I accept it with open arms."
    MC "You don't know you're going to grow?"
    FMG "Well I mean compared to people like your boob friend or Shiori Buttsumoto, I'd think I look normal enough."
    MC "Well, you are a bit muscular."
    FMG "Yeah. But not overly."
    "She proceed to put her hand under her chin and push her head to left side, causing a series of loud cracking from her neck. She repeated this process with the right before continuing."
    show FMG happy with dissolve
    FMG "I may work out almost every day, but it's not my entire life, just 80%%."
    show FMG neutral with dissolve
    FMG "So yeah, just call it a hunch. What about you?"
    MC "Well, I don't feel any different but I am kinda worried about my sis-"
    "I didn't get to finish my sentence when Akira looked at a nearby clock and interrupted me."
    show FMG sad
    FMG "Ah crap! It's 5:35! I'm five minutes late for my routine!"
    hide FMG with dissolve
    "She said while running past me to the door."
    MC "Wait, huh?"
    "Was all I could say in flustered state. Akira then turned around, jogging in one spot for a brief moment."
    show FMG sad with dissolve
    FMG "Sorry! I have to go now, if you want to talk you can find me here whenever there's no classes or at the local gym, later!"
    hide FMG with dissolve
    "And in a flash, Akira proceeded to sprint out the door, leaving me in the same spot, still a bit confused."
    MC "Well that happened."
    "With that I left the building."
    jump daymenu
    
label FMG002:
    $setProgress("FMG", "FMG003")
    scene Gym with fade
    play music Busy
    "With class over I decided to take a shortcut through the Athletics Area."
    "I'd expected to see Akira coming out of the building, what I didn't expect to see was her looking very tired."
    "I figured she must need some cheering up so went to go talk to her."
    MC "Hey Akira, what's up?"
    "Her facial response was of that of slight confusion and following that annoyance."
    show FMG angry with dissolve
    FMG "Ugh, what do you want Keisuke?!"
    "I was honestly taken aback by Akira's response, but in hindsight with how tired she looked, I probably should have expected this."
    "Her face slowly softened from a face of annoyance to one of regret."
    show FMG sad
    FMG "*Sigh*...Look, I'm sorry, I just get frustrated sometimes."
    "She apologized, for the most part she did look apologetic but she still looked physically tired, if not mentally."
    MC "Um, is everything all right?"
    "She took a deep breath before answering."
    FMG "Not really, I went too hard on the treadmill and now I'm too tired to do the rest of my routine."
    MC "Really, how?"
    FMG "I thought if I did twice the speed I normally go I'd get it done in half the time."
    "She paused before continuing."
    FMG "For the most part it worked, but I forgot about the side effect of going past your limit."
    MC "I mean, isn't that the goal to push yourself?"
    FMG "Yeah, but the point of it is to PUSH your limit, not fricking PASS it to the point of exhaustion."
    FMG "Trust me, it's not healthy to do that, the body can only take so much exercise before needing to repair muscle. If you keep doing it with no breaks, you're doing more harm than good."
    MC "Well that sucks, what are you going to do now?"
    FMG "I'm going to bed, I need to let my muscles heal. So if it's all the same, I'll be leaving."
    MC "Ok then, bye."
    FMG "...yeah, later."
    hide FMG with dissolve
    "I was about to make my leave, when I heard Akira call out my name."
    show FMG neutral with dissolve
    FMG "Um...thanks for caring enough to ask."
    MC "You're welcome Akira."
    "With that we went our separate ways."
    jump daymenu
    
label FMG003:
    $setProgress("FMG", "FMG007")
    $setTimeFlag("testday")
    scene Hallway with fade
    "Finally finished with my morning class, I went to get a quick snack from the vending machines before I had to repeat the process with my next class."
    "At least for the most part it was business as usual..."
    FMG "HEY KEISUKE!!!"
    play music FMG
    "...That is until I saw Akira sprinting down the hall."
    show FMG neutral at Transform(xzoom=-1):
        linear 0 xpos -0.5
        ease 0.5 xpos 0.2
    "I braced for impact, but Akira came to a screeching halt just before colliding into me."
    show FMG neutral at Transform(xzoom=1) 
    show FMG neutral at Position(xpos=0.2)
    FMG "Yo, how're you?"
    "Akira asked that almost too casually for someone who just came sprinting down a hallway at 32 kph."
    MC "Um...fine?"
    show FMG sad
    FMG "Great, hey look about the other day..."
    MC "Oh you don't have to apologize, you were just having a bad day is all."
    show FMG neutral
    FMG "Yeah I know, but I feel like I should make it up to you. I thought about it and, well, do you want to join me in my work out sessions?"
    MC "Wait, what?"
    FMG "Well I figured I could make it up to you by becoming like your personal trainer."
    MC "My personal trainer? Why?"
    FMG "Well I know that you're not chubby like 'Princess' Alice Whatever-her-last-name-is, but that doesn't mean you're not out of shape either."
    FMG "Plus, it could help having some muscle when in the middle of a fight, or just wanting to look good."
    FMG "But if you don't want to, that's fine, I'm not gonna force you to do something you don't want to do."
    FMG "So, you game?"
    menu:
        "Eagerly agree":
            jump FMG003_c1
        "Agree but at your own pace":
            jump FMG003_c2
        "Refuse":
            jump FMG003_c3

label FMG003_c1:
    $setAffection("FMG", 2)
    $setFlag("FMG_workout")
    MC "Sure, why not? Let's do it!"
    "I honestly have no idea why I came off so excited, maybe some of Akira's energy had rubbed off on me."
    show FMG happy
    FMG "Heck yeah! That's the spirit, Keisuke. I expect you at your top fitness..."
    show FMG sad
    FMG "...Wait is it top fitness?"
    show FMG happy
    FMG "Ah screw it, just be ready okay?"
    MC "All right, when do get started?"
    show FMG neutral
    FMG "When the time comes, you'll know..."
    MC "Um... no I don't, t-that's why I-"
    FMG "Oh Crap the bell's gonna to ring in 30 seconds! LATER!"
    show FMG neutral at Transform(xzoom=-1)
    show FMG neutral:
        ease 0.75 xpos 0.9
    "She yelled out before sprinting down the hall... leaving me bewildered."
    hide FMG
    MC "...Asked...Wait, 30 seconds!?"
    jump daymenu

label FMG003_c2:
    $setAffection("FMG", 1)
    $setFlag("FMG_workout")
    MC "...All right, I guess..."
    FMG "Yes! We ca-"
    MC "BUT!"
    "I spoke up, catching her off guard."
    MC "I will only do it at my own pace, I don't want to feel like I'm dying after the first session."
    show FMG sad
    FMG "...Oh well...yeah that makes sense."
    show FMG neutral
    FMG "I'll admit I'm a little disappointed, but I'm more glad you're willing to give it a shot."
    MC "Well I am willing as long as-"
    FMG "Oh Crap the bell's gonna to ring in 10 seconds! LATER!"
    show FMG neutral at Transform(xzoom=-1)
    show FMG neutral:
        ease 0.75 xpos 0.9
    "She yelled out before sprinting down the hall... leaving me bewildered."
    hide FMG
    MC "...You don't go overboard...Wait, 10 seconds!?"
    jump daymenu

label FMG003_c3:
    $setAffection("FMG", -1)
    MC "Um look it's nice of you to offer but I got too much to worry about with school and everything else."
    "Upon me saying this her facial expressions turned from hopeful to disappointed."
    stop music
    show FMG sad
    FMG "Oh...ok."
    MC "I'm sorry about this, but thanks for the offer."
    FMG "No it's fine, I'm not made of glass. If you change your mind you know where to find me..."
    MC "...So see you later?"
    FMG "Yeah Later."
    show FMG neutral at Transform(xzoom=-1)
    show FMG neutral:
        ease 0.75 xpos 0.9
    "I honestly felt kinda bad for her but I got too much on my plate to worry about exercise."
    hide FMG
    "..Like the fact I'm going to be late for class if I don't move!"
    jump daymenu
    
label FMG004:
    scene Hallway with fade
    play music Schoolday
    "Another day, another class over...and for once I have nothing to do..."
    "...That is, until a paper ball (that Akira threw before running out of class) hit me on the head."
    MC "Ow."
    "I said more out of reflex than pain, and decided to uncrumple the piece of paper out of boredom."
    "\n{i}The time has come! Meet me at the school's track in 5\n~Akira{/i}"
    "I guess she must have been excited, as she hadn't even put a period at the end of her note."
    "Well, I promised I'd join her, so might as well see what she's up to."
    scene Track with fade
    play music Busy
    "By the time I arrived, Akira was already there as expected, doing stretches as I approached."
    "As I got closer she stopped doing her stretches and walked up to me."
    show FMG happy with dissolve
    FMG "Welcome partner, to the beginning of your training!"
    MC "Well I'm ready for whatever, what will we be doing today?"
    show FMG neutral
    FMG "Today we shall do something simple and easy."
    "She's going to make me run, isn't she..."
    FMG "Running this whole track."
    "I hate being right sometimes."
    show FMG sad
    FMG "*sigh*... But we have to do something, first..."
    "She reached for her bag, pulling out two cups with lids on it."
    FMG "...We have to drink...*gag*... these protein shakes."
    MC "Oh that's it, you made it sound like something bad."
    FMG "Well the thing is, I HATE protein shakes. Like a lot."
    MC "Really? I thought protein shakes were important for exercise."
    FMG "Well it is, doesn't mean I have to like them though. Now as much as I want to delay drinking this sludge, it has to be done."
    "She took it in one go, eyes shut tight the entire time. When she finished it she looked like she was about to vomit."
    "I knew I had to drink it as well, but I figured Akira might just be over exaggerating , I mean can't be that-"
    MC "*GAG*"
    "Oh god, why didn't she add fruit or something..."
    "Well I've already agreed to this, might as well finish it."
    FMG "Ugh... God, I feel like I'm gonna die every time I drink those things."
    MC "Yeah I don't blame you...just what was is in that?"
    show FMG neutral
    FMG "It's just water and protein powder, why?"
    MC "Ever thought of using a liquid that has flavor, like milk or Berry tea?"
    "She just looked at me with no expression, but I swear I could hear her screaming internally."
    FMG "..."
    extend " Oh well, there's always next time."
    show FMG happy
    FMG "Now that the hard part is over, now we get to the actual exercise! Don't worry, I'm not asking for you to run a mile, just a quarter of one!"
    FMG "Today we're going to just make one lap around this track."
    "I followed her to the starting point."
    show FMG neutral
    FMG "All right, ready..."
    FMG "GO!"
    hide FMG with dissolve
    if getSkill("Athletics") >= 5:
        jump FMG004_testpass
    elif getSkill("Athletics") >= 2:
        jump FMG004_testsemipass
    else:
        jump FMG004_testfail

label FMG004_testfail:
    $setAffection("FMG", -1)
    MCT "Ok, Akira's got the lead, but if I can keep a good pace I can do this!"
    MCT "I can do this!"
    MCT "...I can do this..."
    MCT "...I...can...do...this..."
    "I realized Akira had already finished, and she was walking towards me... and I wasn't even near halfway done."
    show FMG sad with dissolve
    FMG "Um...are you okay?"
    "Her concern was clearly shown."
    MC "I... can't *wheeze* do this..."
    FMG "But... dude you're not even half way."
    "Her concern turned to slight annoyance."
    MC "Don't...care *heavy breathing* must... rest..."
    show FMG angry
    FMG "Dude, you're really not making a good first impression, you're worse off than I thought."
    "Now she looked REALLY annoyed."
    MC "...Tell... Daichi...I took his last chocolate...b-bar..."
    FMG "You're not even dying you big baby!"
    hide FMG
    "The last thing I saw before my world was swallowed in darkness was an angry Akira."
    "When I woke up it was an hour later, Akira was nowhere to be found, but there was a piece of paper on my chest."
    "\n{i}Dear Kei, WORK ON GETTING IN FRICKING SHAPE!\n~Akira{/i}"
    "...Yeah I get the feeling Akira is not going to let me live this down..."
    jump daymenu

label FMG004_testsemipass:
    FMG "GO!"
    hide FMG with dissolve
    MCT "Alright, there's no way I'll be able to beat her at the rate she's going. If I can just keep a good pace I'll be able to make at least the lap...Assuming I don't die from exhaustion..."
    FMG "Come on you can do it!"
    "She yelled out ahead, already close to finishing. By the time I finished, The world was getting blurry..."
    show FMG happy with dissolve
    $setAffection("FMG", 1)
    FMG "WOO! Great job there dude, you sure got..."
    show FMG surprised
    FMG " potential? Dude are you okay!?"
    "That was the last thing I heard before passing out."
    scene black with fade
    "One hour later."
    scene Dorm Interior with fade
    "By the time I woke up I was in my room. Confused, I turned to find Daichi who was looking through old newspaper articles."
    show RM neutral with dissolve
    RM "Oh hey, you're up. That Mizutani girl came here carrying you on her back. She said to give this note to you."
    "He handed me the note, to which I began to read."
    "{i}Dear Kai, you did good today, sorry I couldn't do much else to help. Word of advice though you might want to get in better shape. ~Akira{/i}"
    MCT "Well, at least she was kind enough to help me to my room."
    RM "By the way..."
    extend " did you eat my last chocolate bar?!"
    MCT "...Oh crap."
    jump daymenu

label FMG004_testpass:
    $setAffection("FMG", 2)
    "Despite Akira being already in the lead, I managed to keep a good pace."
    "I started to feel a bit winded half way but I pushed myself to go farther."
    "It was about to the end when I was starting to get too tired, luckily I've managed to run the whole lap before stopping completely."
    show FMG happy with dissolve
    FMG "WOO!"
    "Akira fist pumped before walking towards me."
    FMG "Great job there dude, you sure got potential!"
    MC "But I lost, you won by a landslide."
    FMG "It's not about competing, it's about giving all you got and you stuck with it all the way to the end!"
    FMG "Stay right there, need to go get something from the vending machines."
    hide FMG
    "She run to where the vending machines were. When she came back, in each of her hands was ice cream, one cherry blossom and one vanilla."
    show FMG happy
    FMG "Here, A congratulation prize, didn't know what flavor you liked so I got you vanilla."
    MC "Ice cream? But isn't that like the worst thing you could have during a workout?"
    show FMG neutral
    FMG "True, but I'd probably burned half the calories of this ice cream pop in this run, and that's not including the rest of my workout today."
    "I don't think that's how it works..."
    FMG "Besides, I'll take eating an ice cream pop and workout the entire day then drink a fricking protein shake and workout just for only an hour any day of the week."
    MC "At least you got your priorities straight."
    show FMG happy
    FMG "Hell yeah I do!"
    "We stayed there for a while till both ice creams were finished. Akira tossed her popsicle in the trash before turning to me."
    show FMG neutral
    FMG "Well this has been fun, let's call it a day, shall we?"
    MC "Sure, but I got a question."
    FMG "Shoot."
    MC "Why vanilla?"
    FMG "I don't know, you seem like a vanilla kinda guy."
    "I don't know why but I got a chuckle out of that."
    "I waved good bye before heading back to my room."
    jump daymenu

label FMG005:
    $setTimeFlag("aftertest")
    scene Hallway with fade
    play music Rain
    "As much as I didn't like the shot, I am glad this is all over. Well I have nothing better to-"
    UNKNOWN "*sniff*"
    "That's odd, it sounds like there's someone crying near the corner."
    UNKNOWN "*sob*...Why did I have to get a shot...*sob*"
    "As I walked closer to the corner, I saw the one person I did not expect to be crying ...Akira Mizutani."
    show FMG sad
    FMG "...Hey..."
    "She looked slightly annoyed and she had her left hand on the crook of her elbow...but I could tell there was some moisture still under her eyes."
    menu:
        "Are you okay?":
            jump FMG005_c1
        "Man shots suck.":
            jump FMG005_c2

label FMG005_c1:
    $setAffection("FMG", -1)
    MC "Are you okay?"
    FMG "No, I just had a stupid needle jammed into my arm, which by the way was a waste of time."
    MC "Okay...Well what's your factor?"
    stop music
    "I did my best to try and act dumb for her sake but instead she took it the wrong way."
    show FMG angry
    FMG "MY MUSCLES!"
    "I was taken back from her outburst, to which she grudgingly looked away."
    FMG "Look, I'm not in the best of moods so just leave me alone for now, ok?"
    "She proceeded to walk away from me. I figured it was best to leave her alone."
    jump daymenu

label FMG005_c2:
    $setAffection("FMG", 1)
    MC "Man, shots suck, am I right?"
    "I felt that it was best to try to lighten her up, and it seems I was rewarded."
    show FMG neutral
    FMG "Heh, yeah they do, I'm guessing you heard all of that?"
    MC "Um..."
    FMG "It's fine, just don't go spreading what just happened, I kinda don't want to get a rep as a weakling."
    MC "Fair enough."
    MC "...So, will you be all right?"
    show FMG sad
    FMG "Well, it's not the growth that's affected me the most... It's the needles."
    MC "Um, if I may, why do you hate needles so much?"
    FMG "Well, I guess it's because when I was 3, I was playing in the backyard when a rabid raccoon bit me on my leg... hard."
    "She pulled down her right sock, revealing a scar in the shape of a bite on her calf."
    FMG "If you were wondering why I wear my socks so high, that's why."
    MC "Oh god, looks like it was painful."
    FMG "Yeah I guess it did, luckily I don't remember it happening... but I guess my body goes."
    "She pulled her sock back up before continuing."
    FMG "My parents rushed me to the hospital, where they injected me with all kinds of needles."
    MC "Ah, so that's why you don't like needles. Sorry to hear."
    FMG "Yeah, I think it's a combination of the bite and the needles that kinda F'd me up."
    show FMG neutral
    FMG "Just the sight alone makes me hyperventilate... but when it goes in is when I start getting pissed."
    MC "Wow... I don't know what to say."
    FMG "Don't worry about it, I mean it's not something I care for, but I usually feel better after talking about it... Well, once I calm down at least..."
    show FMG sad
    FMG "Otherwise I'd just get mad for no good reason."
    MC "Well, at least it's over. Did you find out your factor?"
    show FMG neutral
    FMG "Oh, my factor is my muscles, kinda obvious in retrospect."
    MC "Well yeah, you are kinda muscular."
    show FMG happy
    FMG "Well yeah, guess it's true that hindsight is twenty twenty then, huh?"
    show FMG flex
    FMG "Well, at least I get to see these bad boys get bigger, huh? I don't know about you, but I'm looking forward to it."
    show FMG neutral
    FMG "What about you Kei, what's your factor?"
    MC "Yeah well, it's my hair."
    show FMG happy
    FMG "Ha, should have guessed. I'm amazed you can see as of now."
    MC "H-Hey, it's not {i}that{/i} long!"
    FMG "Nah, you're right, it'll get longer!"
    "Akira burst into laughter, already forgetting the despair that entrapped her only minutes ago. Once she finished she looked back at me."
    show FMG neutral
    FMG "All right, if it's all the same to you I'd rather be alone right now."
    show FMG happy
    FMG "But for what it's worth, thanks for the talk... I REALLY needed it."
    hide FMG
    "With that she left, leaving me alone in the hallway."
    jump daymenu
    
label FMG006:
    scene Classroom with fade
    play music Busy
    "And so another day of classes ended, and for once I actually felt like working out today. I walked over to Akira's desk just as she got up, putting a paper ball behind her back once she saw me walking towards her... like I hadn't noticed."
    show FMG neutral with dissolve
    FMG "Um, hey Kei, I was about to head your way, got anything planned for the next hour?"
    MC "Not really, did you want to exercise more? Because I feel like it today."
    show FMG happy
    FMG "Oh! Yeah, I got time for you today. I got to get my workout stuff, so meet me in the athletics area in five, OK?"
    MC "All right, sounds good."
    "She walked out the door... But not before not before throwing that ball at my head."
    hide FMG with dissolve
    FMG "Sorry, can't waste a good paper ball!"
    MC "...Why does she keep doing that..."
    scene Gym with fade
    "By the time I got to the athletics area, Akira was already doing her warm-up stretches by the weight sets."
    show FMG neutral with dissolve
    FMG "Hey there! You know, I'm kinda surprised you came to me today instead of the other way around. But anyways, first order of business is the shakes."
    MC "You look more happy about that than last time."
    FMG "Thing is, you know I hate protein shakes, right?"
    MC "Right."
    show FMG happy
    FMG "Well, I've been experimenting with different drinks, and I found one that doesn't make me want to vomit to death."
    "She pulled out her shake cup from her bag in triumph."
    FMG "Behold, and be amazed!"
    MC "Isn't that the same thing?"
    show FMG angry
    FMG "Shut up and let me have this moment."
    show FMG happy
    FMG "Milk protein coffee ice cream shake!"
    show FMG neutral
    FMG "Basically I mixed coffee flavored ice cream with a bit of milk with the protein powder and the final result was this."
    MC "Huh, you really like ice cream don't you?"
    FMG "Yep, it's my third or fourth favorite thing ever!"
    "She drank it in one go, with a little still inside."
    show FMG happy
    FMG "Ahh, that tasted almost drinkable!"
    show FMG flex
    FMG "Hell yeah, let's do this!"
    stop music
    "Akira slammed the drink on a nearby table; however, she didn't realize until it was too late that she slammed it on the edge, causing it to fall down on the carpet and leave a stain."
    show FMG angry
    FMG "...Oh come on!"
    FMG "Great, now we gotta clean this before it stains..."
    MC "Oh, well, all right."
    scene black with fade
    "Much to Akira's dismay, we spent about the next hour cleaning the carpet. By the time we finished, Akira looked...upset?"
    scene Gym with fade
    play music Peaceful
    show FMG angry with dissolve
    FMG "Man this blows... cleaning that carpet took over an hour, we don't even have time to work out."
    MCT "I don't think I've seen her like this, the question is why though."
    MC "Don't worry, we can exercise some other time."
    show FMG sad
    FMG "{i}Sigh{/i} Kei, that's not what I'm mostly bummed about, I wasted your time by helping me clean a mess I made when you could have done something more fun..."
    MCT "Oh, she feels guilty for making me help her out..."
    menu:
        "Buy her ice cream":
            jump FMG006_c1
        "Tell her it doesn't bother you":
            jump FMG006_c2
        "Make your leave":
            jump FMG006_c3
            
label FMG006_c1:
    $setAffection("FMG", 1)
    MCT "Geez, I don't want her to feel bad just because I helped her, there's gotta be something I could... That's it!"
    MC "You know what? Wait right there for a minute, okay?"
    FMG "Huh, what are you doing?"
    MC "Just a minute!"
    scene black with fade
    "It took a bit to get to the vending machines, but I got what I needed for Akira."
    scene Gym with fade
    show FMG sad with dissolve
    MC "Here, I know you feel bad but I figured I could cheer you up with -"
    show FMG happy
    FMG "{i}GASP{/i} FREE ICE CREAM!? SWEET!"
    "In a flash, Akira grabbed the ice cream and proceeded to consume it as quick as a five-year-old who just discovered ice cream."
    MCT "It only took her thirty seconds to eat the entire ice cream bar...how did she not get a brain fre- ECK!"
    "And she has wrapped me in a VERY tight hug."
    FMG "Thank you so much! "
    MC "Yo-u're... wel-come... bu-t c-can't breathe."
    show FMG surprised
    FMG "Oh!"
    "She let go before she crushed my body to pieces."
    show FMG neutral
    FMG "Sorry about that, I just felt like I should show you my appreciation."
    MC "It's fine, I just wanted to let you know I'm not upset about it at all."
    FMG "Well again, thanks for that, I really appreciate it."
    "I looked at the time - it was almost 5 pm."
    MC "I think it's time we head out."
    FMG "Yeah, it's getting late, thanks again for everything."
    jump daymenu
    
label FMG006_c2:
    MC "Um... Hey, don't worry about it, it had to be cleaned up, so..."
    MCT "...Yeah, I have no idea what I'm doing, but at least she stopped looking sad."
    show FMG sad
    FMG "Yeah I know, I'll find a way to make it up to you."
    MC "Um...you don-"
    show FMG angry
    FMG "I swear, I will make up for my mistake and wasting your time!"
    MC "Please-"
    FMG "THIS I SWEAR!!!"
    hide FMG with dissolve
    MCT "...Aaannnd she is out of here..."
    MC "Well it's out of my hands now, might as well go back to the dorms."
    jump daymenu

label FMG006_c3:
    $setAffection("FMG", -1)
    MCT "Um, this is awkward, so..."
    MC "Look it's late, how about we do this later?"
    FMG "{i}Sigh{/i} Fine, whatever..."
    MC "Is everything okay? Are...are we good?"
    FMG "Sure, whatever."
    MCT "I think it's best just to leave her alone for now..."
    jump daymenu
    
label FMG007:
    $setProgress("FMG", "FMG008")
    scene Cafeteria with fade
    play music Sunset
    "Lunch hour. The cafeteria was bustling with the sounds of conversations, student voices blending together, making it hard to differentiate one from another."
    "I walked past table after table of students eating, talking, even one student was asleep, but nothing out of the norm."
    "At the far end, near the windows, sat an all-too-familiar bodybuilder. Akira was resting her head in her hand, taking slow but big bites from what was left of her stir-fried beef and rice. She was staring into space, though she didn't look tired; it was more of a listless catatonia."
    show FMG neutral with dissolve
    MC "Hey, is it all right if I eat with you?"
    FMG "Hm? Oh, sure, I'm almost done but take a seat."
    MC "Hey, do you want to work out after class?"
    show FMG sad
    FMG "Yeah, sorry, but I'm not feeling it today. I got a knot the size of a baseball in my Quadriceps and it's a pain to walk, let alone work out. All I want to do is eat my lunch."
    MC "Oh, sorry."
    show FMG neutral
    FMG "Don't worry about it."
    "For the next few minutes we ate in silence, but given her head start Akira was finished well before me. With nothing else to do, at least that she had the energy or inclination for, she decided to start a conversation."
    FMG "So... What do you do in your spare time?"
    MC "Nothing specific, really, just whatever I feel like at the time. Don't really have any specific hobbies or anything. What about you, besides exercising?"
    FMG "I enjoy playing arcade games."
    MC "..."
    extend "Wait, really?"
    show FMG sad
    FMG "Oh come on, don't look so surprised. Just because I work out doesn't mean I don't have other hobbies."
    menu:
        "Encourage":
            jump FMG007_c1
        "Apologize":
            jump FMG007_c2
        "Rationalize":
            jump FMG007_c3

label FMG007_c1:
    $setAffection("FMG", 1)
    MC "So... What's your favorite arcade game?"
    show FMG neutral
    FMG "...Rage of the Waste."
    MC "Isn't that the rail shooter set in a 80's vision of the future?"
    FMG "No, you're thinking of Electric Rage: Crimson Beam. Which, by the way, is my second favorite."
    FMG "RotW is a fighting game that takes place in a post-apocalyptic Los Angeles, after an angry defense engineer single-handedly caused armageddon by launching nukes at Russia."
    MC "Sounds interesting. How did you start playing video games?"
    FMG "Well, my dad worked at this electronic company called Shun Electronics for most of my life, so he would often bring the games he was working on, and often times would let me play test them."
    MC "Wait... Your dad works at Shun Electronics!?"
    show FMG happy
    FMG "Yep, thanks to him I found my love for video games."
    show FMG flex
    FMG "Even a bodybuilder like me has got to have a hobby, dude!"
    show FMG happy
    FMG "Hey, if we ever get the chance, let's play some time, okay?"
    MC "Sure, love to."
    "The smile Akira got at the prospect seemed to break her from her torpor, and she finally got up to take her leave."
    jump daymenu
    
label FMG007_c2:
    MC "Sorry, it's just I never pictured you as the gamer type."
    show FMG neutral
    FMG "Blame my dad, his work rubbed off on me."
    FMG "Look, I got things to do. Later."
    MC "Uh, well, bye?"
    jump daymenu

label FMG007_c3:
    MC "I mean, the only times I remember seeing strong people around the arcade, they were usually bullies who'd take the smaller kids' yen..."
    show FMG angry
    extend " Wait, I didn't mean it like that!"
    FMG "Wow dude, way to judge a book by its cover!"
    MC "Wait, I'm-"
    FMG "Ugh, why do I even try..."
    hide FMG dissolve
    "She left before I could explain... Though to be fair, I didn't think I could have salvaged that."
    jump daymenu

label FMG008:
    $setProgress("FMG", "FMG009")
    scene Dorm Exterior with fade
    play music Schoolday
    "I wasn't really going anywhere today, just felt like going for a walk and taking in the sights."
    "Days're a bit hotter, students are hanging out, Mizutani-san is trying to get something under a vending machine, wind's a bit- ...wait, what?!"
    "My mind wasn't playing tricks; Akira Mizutani was on her knees trying to get something from under the machine."
    show FMG angry
    FMG "Oh come on, you stupid pencil!"
    "She groaned in frustration before getting up, once she did she saw me watching her."
    show FMG sad
    FMG "*Sigh* Hey."
    MC "Um... What's wrong?"
    FMG "Ugh. My only pencil fell behind the vending machine and my arm's too big to fit. I'd move the stupid machine if I wasn't afraid I might break something!"
    "She went to grab a fallen stick from one of the trees, and went back down to the vending machine to try to poke the pencil out. Alas, the stick only pushed the pencil further back."
    show FMG angry
    FMG "A-Are you for real!? Ugh!"
    MC "Sorry to hear that, do you want to borrow a pencil?"
    "She calmed down before answering."
    show FMG neutral
    FMG "Nah. I'd feel like I owed you a new one, and I barely got enough cash for myself."
    MC "Well, is there anything else I could do?"
    FMG "Actually... Hey, you got smaller hands than I do, think you could grab it for me?"
    MC "Oh, sure, I'll try."
    MCT "Wait, what did she say about my hands? Nevermind..."
    "It was hard to reach, but I got it."
    show FMG happy
    FMG "All right, thanks dude!"
    FMG "..."
    show FMG sad
    FMG "Huh... You know something... That's one thing I'm not looking forward to..."
    MC "Excuse me?"
    FMG "My muscles. Well, the whole growth thing in general. With how things are going, I'm gonna grow so big, it's going to be hard to fit in small places."
    show FMG neutral
    FMG "Don't get me wrong, I'm looking forward to see how big I might get, I just hope I'm not sacrificing my mobility in the process."
    FMG "It's worrying, but like I said before; whatever happens, I accept it with open arms."
    show FMG happy
    FMG "Anywho, it's been fun but I gotta jet! Thanks again!"
    "Huh. now I'm beginning to wonder if I got lucky or not with my growth..."
    jump daymenu

label FMG009:
    $setTimeFlag("size2")
    $setProgress("FMG", "FMG014")
    scene Dorm Exterior with fade
    play music Rain
    "The sun was setting, people were talking and hanging out, and I found myself craving a Rocco-Choco Bar from the vending machines. To my surprise, Akira was waiting near the machines; she seemed calm for the most part, if a little annoyed."
    show FMG neutral with dissolve
    FMG "Hey Kei, what's up?"
    MC "Nothing much, just getting something from the vending machine. What's up with you?"
    show FMG sad
    FMG "*Sigh* I'm waiting for someone because I need to talk to her. Speak of the devil..."
    show FMG sad at Position(xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    show Chibuki neutral at Position(xpos=0.75) with dissolve
    "Just like she said, there really was someone walking towards us. A girl with dark red hair, a small scar on her right eyebrow, wearing what I could describe as an punkish version of the school uniform, which gave her this aura of disobedience and defiance."
    "There were two big things that immediately made her stand out. One, her eyes were as blue if not bluer than Alice's, which would mean she was a foreign student. And two..."
    "...Her nipples were easily seen bulging out of the fabric of her shirt."
    UNKNOWN "Yo Akira, I'm here, so what did you... wait, are you trying to hook me up with this guy?!"
    show FMG surprised
    FMG "What?! No! God Chibuki, he's here for something else."
    UNKNOWN "Well sorry, but then who and why is he here?"
    show FMG neutral
    FMG "Well since you asked, this is Keisuke. He was just saying hi before you got here."
    UNKNOWN "Oh, this is that Keisuke kid you've been spending your time exercising with? Well then, allow me to introduce myself."
    Chibuki "The name's Chibuki Blackburne; weird last name in these parts, I know, but I was born and raised in Manchester, England after me mum moved from Japan."
    MC "Nice to meet you. So, how do you know Akira?"
    play music Tension
    show FMG angry
    FMG "She's my roommate, who by the way STILL has yet to get her dirty clothes off the bathroom floor!"
    Chibuki "*sigh* Really Mizutani, that's why I'm here? Would it kill you not to bring it up every day?"
    FMG "Let's not forget that you leave half-empty bags of potato chips all over the floor. I wouldn't care if our room didn't smell like sour cream and onions! I swear, you are such a slob!"
    Chibuki "In my defense, that Butts-in-moto brat has been watching me like an ex-girlfriend after I accidentally broke a school rule, plus I'm the president of the art club! I gotta be there or else it will come crashing down!"
    FMG "Ugh! Why do you feel the need to push the blame on others?! Admit it, You're just lazy Chibuki!"
    Chibuki "Akira, just because you're my roommate and stronger than me, doesn't mean I won't knock ya bloody teeth in if ya don't knock it off!"
    "It looked like the both of them were going to fight it out right there..."
    MC "Um, hey can-"
    FMG "Ugh! I'm not dealing with this now!"
    "Akira lashed out before walking away, all the while angry."
    hide FMG
    play music Rain
    extend " Chibuki, for her part, just looked back at me defeated."
    show Chibuki neutral at Position(xpos=0.5)
    Chibuki "*sigh* Sorry you had to be part of that, she can be a little hot-headed."
    "She apologized, before walking to the vending machine to buy chips, it's only when she grabbed the first chip she said more."
    Chibuki "Heh, she is right about one thing, I really am lazy."
    "I honestly didn't really know how to take that, so maybe an apology was in order."
    MC "Well, sorry if I made you uncomfortable in any way."
    Chibuki "Oh no, far's I can tell, you did nothing wrong. Akira's just having some issues of her own."
    Chibuki "In any case, if you really want to get along better with her, try to take her boisterous attitude with a grain of salt."
    MC "What do you mean by that?"
    Chibuki "My gut is telling me that she's hiding something, but I ain't gotta clue as to what."
    Chibuki "As for me, I suppose I'll still help her when you're not around. Later Kei."
    jump daymenu
    
label FMG010:
    $setSize(2)
    $setTimeFlag("aftersize2")
    scene Classroom with fade
    play music Schoolday
    "The class started as normal with roll call, until Mizutani's name was called out and I realized she didn't answer."
    MCT "Weird, I don't think I've ever seen her miss class. Sleeping in sure, but never missing."
    scene black with fade
    pause 1
    scene Classroom with fade
    "Class ended with no sign of Akira. I turned to ask Matsumoto if she'd seen Akira today."
    MC "Hey Matsumoto, sorry to bother you but have seen Akira today?"
    show AE neutral with dissolve
    AE "Hm? You're looking for her too?"
    MC "So you noticed she was gone as well? It's not like her to miss class."
    AE "Indeed. Despite her more lenient mannerisms, she at least has the decency to show up to class eventually."
    MC "Do you remember the last time you saw her?"
    AE "I'm afraid the last time I had seen her was right after class ended yesterday."
    MC "All right, I guess. If you do see her, let me know, okay?"
    AE "Indeed, I certainly will."
    MC "Thanks for the help, I'll see you later."
    AE "Goodbye, Hotsure-san."
    scene Hallway with fade
    "I left Shiori alone and exited the room. With no help from Shiori, I figured it was probably best just to leave it be for now..."
    if getAffection("FMG") >= 3:
        jump FMG010_testpass
    else:
        jump FMG010_testfail
        
label FMG010_testpass:
    "...At least, that was the plan before I was called out to from behind. I turned around to find Mizutani's roommate running towards me; Blackbourne-san, Akira said her name was."
    show Chibuki neutral with dissolve
    Chibuki "Sorry, but you're Mizutani's workout partner, right?"
    MC "Yes that's me, did you need something Bla-"
    Chibuki "Let me just stop you real quick, just call me Chibuki; I never did fully cotton to the weird ways my mum referred to people, all last name first."
    MC "Understandable, so what did you need Chibuki?"
    Chibuki "I'll be blunt. Akira had a growth spurt and asked me to get her new clothes she ordered from the tailor. Her old outfit got ripped pretty bad, so she was forced to stay in our room."
    Chibuki "However, little miss Buttsumoto, in her infinite wisdom, wants me to go over the decorations for the upcoming school festival because of my duty as art club president... For the third time. Damn, I wish she'd get that stick out of her fat arse."
    Chibuki "But anyways, I gotta be at the council room in five or I get the third degree. I figured since you both have been hanging out together, you could bring it to her. Do this, and I'll owe ya a favor you can cash in later."
    "This was interesting. It would explain why she was absent today. Without any clothes that fit her muscular body, she wouldn't be able to go out in public. She could probably use any help she could get."
    MC "All right, I'll help Akira out."
    Chibuki "Great. So, because Akira's got nothing but her birthday suit on, you'll have to throw a pebble or something at our window to get her attention. It's on the second floor, look for the slightly opened window covered with a black poster. "
    MC "How do you know the window will be open?"
    Chibuki "I sleep near the window- love the fresh air, but hate the sunlight."
    Chibuki "Once you get her attention, have her tie our laundry basket with spare sheets, and she'll do the rest. Her clothes are at the tailor's. Now I gotta leave, later dude!"
    Chibuki "Oh, and don't be a perv, even if she's got a rockin bod!"
    MC "Wait wh-"
    "But alas, she left before I could finish asking what she meant by that."
    MCT "...Ugh, why is it when someone says something interesting, they leave it off without an explanation..."
    "I went to the student tailor to begin my mission of importance. The clothes were on a counter by the time I got there, I could tell it was hers because of the bright red undershirt packed in... and the fact it had a note saying ‘Akira Mizutani'."
    stop music
    scene Dorm Exterior with fade
    play music FMG
    "I got the clothes and made my way to the dorms, picking up a few small pebbles I noticed along the way. I followed Chibuki's instructions and found the exact window she'd described. I threw a pebble at the window to get Akira's attention and sure enough Akira stuck her head out, looking like she was wrapped in some kind of blanket toga."
    FMG "Keisuke!? Why are you throwing rocks at my window? Where's Chibuki? She was supposed to be here by now with- hey, my clothes! Is that my uniform!?"
    MC "That's why I'm here, Chibuki had a meeting with Shiori and asked me to give you your new outfit."
    FMG "Well, how are you going to do that?! I wouldn't let you up here even if I wanted to!"
    MC "Just get some sheets and tie them to your laundry basket, lower it down out the window, and I'll put the clothes in."
    FMG "All right, but you better not try anything!"
    "After a few minutes she lowered the basket, allowing me to put the clothes in. Once she pulled it back up, she once again stuck her head out the window."
    FMG "Hey, meet me outside of my door, we can talk there!"
    "She pulled her head in after that, and I headed for Mizutani's room. Once there, I knocked on the door."
    MC "Mizutani-san, are you dressed?"
    FMG "Almost, you came just in time, I was going nuts!"
    MC "Oh? Tell me about it."
    FMG "For the past two days, I've been stuck in my room. I forgot to get food, so all we had was Chibuki's junk food and soda. Worst part of it was that the soda was some cheap knock-off of Cane Cola called Kool Kola."
    FMG "Okay, I'm ready."
    "She opened the door and walked out. It was only then I truly saw how big she'd gotten, to have burst through her previous uniform..."
    show FMG happy
    FMG "Oh god, it feels nice to be outside!"
    "Her arms were thicker than the last time I saw her, her chest more toned, abs starting to be more noticeable though the shirt. Her legs were more muscular, and I could swear she was even a bit taller, though it could just have been my mind playing tricks on me, given how big the rest of her was."
    show FMG neutral
    FMG "Thanks again, man! I was really in a pickle there..."
    FMG "..."
    show FMG flex
    FMG "Why are you looking at me like that, as if I don't already know?"
    MC "Sorry, you're just... really buff."
    show FMG neutral
    FMG "Thanks, I kinda knew I was getting big for a while, but it didn't really hit me till my outfit ripped to shreds during morning cardio."
    MC "I have to ask, do you think-"
    FMG "-That working out is accelerating my growth factor?"
    FMG "Yes."
    FMG "Did the nurse warn me about that?"
    FMG "Of course she did."
    FMG "Am I gonna stop?"
    show FMG happy
    FMG "Hell no!"
    show FMG neutral
    FMG "Look, I know that it's probably going to affect my life, but I've come too far to give up now. It's part of who I am, and there's nothing that can change that."
    "Huh, even when against her own growth, Mizutani-san was pushing toward her goals. Be that as it may, I still had to know..."
    MC "Why do you want to become strong so bad?"
    FMG "..."
    show FMG sad
    FMG "..."
    show FMG flex
    FMG "Everyone has a life goal, mine's just that simple, I guess!"
    "I couldn't help shake the feeling that she was only giving me half of the truth, if not a quarter-truth truth. It made me wonder if Chibuki was right about Akira hiding something. Still, I didn't want to force it out of her, if she wanted to tell me then I'd let it be of her own volition."
    show FMG neutral
    FMG "By the way, I gotta know, dude..."
    show FMG angry
    FMG "Why did you come all this way to my dorm, anyways? Were you trying to get a quick peek or something?"
    MCT "...huh, I was so caught up in getting these clothes, I had never even thought about anything like that."
    MC "Er, to be honest, no. The thought never occurred to me. Chibuki said you needed help, and that was enough for me."
    show FMG neutral
    FMG "Wow...I'm shocked. If I was a guy in your place, I totally would have tried something."
    show FMG flex
    FMG "Especially with a body this hot!"
    show FMG neutral
    FMG "I'm..."
    show FMG happy
    FMG "I'm glad to know you care like that, Kei!"
    FMG "Have a big hug for your troubles!"
    "She swept me up in a big hug, and I held my breath. I'd expected a tight, bone-creaking hug from a bear but instead the hug felt nice, gentle even. I wouldn't have minded staying like that for-"
    show Chibuki neutral at Position(xpos=0.8)
    Chibuki "So are you guys gonna shag here or what?"
    $setVar("RinFavor", getVar("RinFavor") + 1)
    MC "AHH!!"
    show FMG surprised at Position(xpos=0.2, yalign=1.0), Transform(xzoom=-1)
    "Both Akira and I yelled out in surprise, breaking the hug in the process."
    FMG "What?! Chibuki?! I thought you had a meeting with Shiori!"
    "Akira yelled out in both frustration and confusion, though this had little to no effect on Chibuki as she answered Akira's question."
    Chibuki "Yeah, turns out one of the schedulers double-booked my meeting with another, so Buttsumoto let me off the hook. Anyways, now that I see you out in the open, {i}man{/i} you look big, Akira."
    show FMG neutral
    FMG "Oh, I'm big? You're not so small yourself, torpedo-nips."
    "I couldn't tell if Akira was annoyed because of the scare, or from having to break the hug. Wait, what had she said about Chibuki's 'nips'...?"
    MC "Does that mean Chibuki's...?"
    Chibuki "Yeah, my growth thingy is my nipples; I don't mind though, I plan to use 'em to my advantage! Anyways, sorry I was earwigging on your conversation; If you need me, I'll be in our room venting my frustrations into a sketchbook. Later."
    Chibuki "Oh, and I didn't forget about that favor!"
    hide Chibuki with dissolve
    "..."
    show FMG neutral at Position(xpos=0.5, yalign=1.0), Transform(xzoom=1) with dissolve
    MC "Um...what did she mean by using them to-"
    FMG "Man I don't even know, and I don't think I {i}want{/i} to know. That girl is something else."
    MC "You know, she seems like a good friend, even if she's a bit weird."
    FMG "I guess. Listen, these past two days have been irritating..."
    FMG "I'm going to go up to my room and yell at Chibuki to get the brand name soda from now on and not leave me stuck with crappy off-brand. See you on the flip side, man."
    MC "See you."
    hide FMG with dissolve
    FMG "Chibuki! You better get Cane Cola from now on or I swear..."
    Chibuki "Who cares about soda, you ruined my Nyte Lyte poster!"
    FMG "What did you expect!? I had to get to the window somehow!"
    MCT "...It's probably best if I leave those two alone..."
    "Once I gave it more thought, I realized the more I hung out with Akira, the more I became aware she was hiding something. I guessed the only thing I could do at the time was wait, but there was something else still bugging me..."
    MC "...What the hell is 'earwigging'?"
    jump daymenu

label FMG010_testfail:
    "...it didn't make me any less worried though."
    scene black with fade
    pause 1
    scene Hallway with fade
    play music Sunset
    "The day went by as normal, and around sunset I decided to get a quick snack from the common area."
    "As I made my way down the ramp nearest to the vending machines, I saw Akira...but she was bigger than I remembered."
    show FMG sad with dissolve
    FMG "*sigh* Hey Keisuke."
    "Her arms were thicker than the last time I saw her, her chest more toned, abs starting to be more noticeable though the shirt. Her legs were more muscular, and I could swear she was even a bit taller, though it could just have been my mind playing tricks on me, given how big the rest of her was."
    FMG "Yes, I know I'm big but can you please not stare at me? I've had a long day!"
    MC "Um, are you all right?"
    show FMG angry 
    FMG "I've been stuck in my room for the past two fricking days! I had to live off of Chibuki's junk food and soda! It wasn't even the name brand, it was some cheap knock-off of Cane Cola called Kool Kola!"
    MC "Wait, why were you stuck in your room?"
    FMG "Because I had a growth spurt! I couldn't fit into my clothes without ripping them. Chibuki was supposed to get my replacement uniform from the tailor's but got detention, leaving me all alone in my room till she got back an hour ago!"
    show FMG sad
    FMG "I mean, I'm glad I got bigger muscles, but the day has been so awful that I couldn't really enjoy them."
    MC "Sorry, I would have helped if I'd known."
    show FMG angry
    FMG "That's nice of you to say, but I think I've had enough 'help' for one afternoon... goodnight."
    hide FMG with dissolve
    "She left before I could say anything. Given her situation, I thought it best to leave her be and talk to her another time..."
    jump daymenu

label FMG011:
    scene School Planter with fade
    "It was a cloudy day that day, but I figured it would be nice to just walk around the school despite that."
    "...At least, until it started raining."
    "Luckily, I found a room of some kind that was attached to the school , and entered without questioning its purpose. As I entered, I realized it was a recreation room of some kind, like something from an 80's arcade or something."
    scene Recreation with fade
    play music Busy
    MC "How old is this place, anyway?"
    "A few fellow students had the same idea I had, taking shelter from the downpour, but I realized there was someone who had already been in here before the rain started."
    "To my surprise, Akira was playing on one of the machines..."
    if isEventCleared("BBW009"):
        "... And she looked focused. I walked up to get a better view of the game."
        show FMG neutral at Position (xpos=0.75, yalign=1.0), Transform(xzoom=-1) with dissolve
        FMG "Hey. Can't talk now. Killing."
        "She was in the middle of a boss fight with a strange mutated creature. Given the size of its health bar, I thought it might be the final boss."
        show FMG angry
        FMG "Come on you stupid bat-cat-zombie-thing. Just die already."
        "Despite being annoyed, she was able to keep focused. About 5 minutes later she killed the boss, keeping a cool head the entire time."
        show FMG happy at Transform(xzoom=1)
        FMG "Woo!"
        "...For the most part, at least."
        MC "Wow, you're good."
        show FMG neutral
        FMG "Yeah, practice makes perfect and all, I've been playing this thing whenever I get spare time since losing that swim bet."
        MCT "...Ah, balls. I forgot about that."
        MC "Er... you okay?"
        FMG "Don't worry, I ain't mad at you, if that's what you're wondering. I just want to give that smug jerk a taste of her own medicine."
        show FMG angry at Position(yalign=1.0), Transform(xzoom=-1)
        FMG "Heh. She thinks all I do is work out, well she's not the only one with a hidden talent."
        MC "Well, you never know. She could be good at this kinda stuff."
        FMG "Any overweight, smug overachiever can play and be good, but it takes skill and practice to be great at something."
        "Oh great, history was repeating itself. This time, the one behind her was-"
        show BBW neutral at Position (xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
        FMG "You don't just sit around to be great at something, you gotta go out there and do it yourself."
        "Alice, and she looked angry. I'd say I was surprised this was happening again...but I wasn't."
        FMG "But no, people want to do it the easy way, by sitting down, getting fat, and having everything given to them. Not all of us were born with a silver spoon in our mouths."
        MC "Ak-"
        FMG "And by the way, I know you're behind me, Alice, I can hear you breathing."
        MCT "At least your hearing's better than Alice's, I guess..." 
        show BBW angry
        BBW "Well at least you have some skills of perception."
        show BBW haughty
        BBW "I'm just curious how it is someone who 'sits around all day' trounced you so thoroughly at the pool."
        show FMG angry at Transform(xzoom=1)
        FMG "What the heck does 'trounced' mean?"
        BBW "Beaten. Clobbered."
        FMG "T-Then why didn't you- you know what, I want a rematch- and I pick this time."
        BBW "Certainly, assuming you have any interests besides athletics?"
        FMG "...Do you not see that I'm standing next to an arcade game?"
        BBW "Oh! I didn't know you were actually playing."
        BBW "I thought you were just waving a toy gun around, going ‘Pew pew!'"
        MCT "Oh no, Alice... now you've done it."
        FMG "... You... grab the gun and put your cash in so we can start."
        "Akira was visibly shaking with rage while Alice got into position. All I could do was watch this happen while Akira grabbed the second player gun."
        show FMG angry at Position(yalign=1.0), Transform(xzoom=-1)
        show BBW haughty at Position (xpos=0.55) with dissolve
        FMG "I'm going to take a wild guess and say you want to be player one. Doesn't matter in the long run, though."
        BBW "{i}Au contraire{/i}, you can be whichever you want. I wouldn't want you handicapped." 
        show FMG neutral
        FMG "Quit speaking... whatever language that is and let's do this."
        show BBW neutral
        "Thus began a duel for honor, pride, and some other third thing. About ten minutes into it Akira was already ahead of Alice by ten thousand points, mostly because Alice was shooting normal civilians before realizing she lost points for doing that."
        "Both were too focused on the game to say anything to the other, but I could tell that Akira was feeling smug about her lead, while Alice was both confused and annoyed."
        "An hour later, and a lot of both their coins, they managed to get to the final boss, and once it was dead, the scoreboard tallied up the results, with Alice's score first."
        show BBW neutral at Position (xpos=0.40) with dissolve
        "Player One Score: 21521"
        show FMG neutral
        FMG "Huh. Not bad..."
        BBW "Why of course I would do great, only someone like me can reach a score lik-"
        "Player Two Score: 74681 !NEW RECORD!"
        show BBW angry
        BBW "-What!?"
        show FMG happy at Transform(xzoom=1)
        FMG "... For a beginner, that is!"
        "Alice looked at her gun for a moment before putting it back, her face stony."
        show BBW neutral
        BBW "It should be expected that I would not master this the first time."
        BBW "So congratulations. You have defeated a newcomer."
        show FMG sad
        FMG "... I'm just trying to show how I felt at the swim dare and you can't even let me have that..."
        BBW "..."
        BBW "That wasn't your first time swimming, though, was it?"
        FMG "No, and that's why it hurt when you acted all high and mighty, especially when you didn't realize I was behind you."
        BBW "..."
        "Alice didn't reply for a moment, and I thought she was about to say something vicious or snide. Instead she exhaled slowly, pinching the bridge of her nose."
        BBW "I was unaware it would hurt you. I apologize if you were offended."
        MCT "That's not really an apology..."
        FMG "Whatever, just promise me one thing..."
        "As if a burning passion was ignited, Akira stared down Alice with fire in her eyes..."
        FMG "Don't you ever insult me and my father's work of arcade games ever again!"
        "Akira looked down on Alice before going to normal. To this day I'll never forget the look of shock Alice had on her face."
        show FMG happy
        FMG "I hope we have a understanding. Let's play again sometime."
        hide FMG happy with dissolve
        "That was all Akira said before leaving me, Alice, and the machine in the room..."
        MC "Alice, are you okay?"
        "She took a second to clear her throat before responding."
        BBW "S-strange girl..."
        BBW "She's upset about losing at swimming, but she's more concerned about her gaming skills?"
        MC "To be fair, you did say something about waving the gun around, going ‘Pew pew'. She takes her hobby seriously, I guess."
        BBW "Apparently..."
        MC "Well, thanks for kinda apologizing. I'm heading back to my room. See you at class."
        show BBW happy
        BBW "Indeed. Good day, Hotsure-san."
    else:
        "...Though she looked rather casual, like she was really just playing it for fun, not trying to beat it or anything. I walked up to get a better look of the game."
        show FMG neutral at Position (xpos=0.75) with dissolve
        FMG "Yo, what's up?"
        MC "It's raining, so I came in here. Shouldn't you be focusing on the game?"
        show FMG happy
        FMG "Nah, I don't care if I lose or not. Besides, it's going to enter a cutscene in a sec."
        FMG "Can you believe this school has a recreation room, let alone three arcade games!"
        MC "Yeah, so what's that you're playing?"
        FMG "Dead Awakening: Fubar, it's just a first person rail shooter about killing zombies in a made up place called Fallon City, I think it's a play on words of ‘Fallen City'. I'm just about to fight the final boss once this cutscene finishes."
        show FMG happy at Position(yalign=1.0), Transform(xzoom=-1.0)
        "Just then, a bat-cat-zombie-thing showed up. Akira took about 3 minutes to beat it, and once she did a leaderboard showed up, displaying her score."
        show FMG neutral at Transform(xzoom=1)
        FMG "Man, that was fun. Third place too, not bad."
        MC "Yeah, thinking of going for first place?"
        FMG "Nah, unless I've got a VERY good reason, I'm not that competitive. Speaking of competitiveness, look who just came in..."
        "By the doorway was a slightly soaked Alice, looking annoyed."
        FMG "Hey Alice! How's it going?"
        show BBW angry at Position(xpos=0.25) with dissolve
        BBW "Irritatingly. The weather report said nothing of showers, and... Look at me."
        FMG "Oh yeah, Kei said something about rain but I wasn't paying attention. At least you found shelter before it really got bad."
        show BBW neutral
        BBW "(Sigh) Any damage to my hair or clothing is bad enough, but I won't bemoan a fair sprinkling."
        "Akira turned to Alice and  pointed her thumb at the arcade game behind her."
        FMG "Well, wanna take your anger out on these zombies?"
        "Alice's expression remained like she was smelling something slightly unpleasant, but she walked up to Akira and took the proffered gun."
        BBW "Let me guess, I point and shoot anything that moves?"
        FMG "Well, yeah, if you wanna lose points by killing innocent people. It's to keep the game balanced. Focus on the things that look like they shouldn't be alive. Oh and watch your ammo, you're a sitting duck if you can't shoot. To reloa-"
        "She didn't have a chance to explain how to reload as Alice had already started, once Alice had emptied her clip she continued firing to no avail, with increasing irritation."
        "Eventually the zombies got to her, the screen turning red with blood splotches until the words ‘Game Over' came up."
        show FMG sad 
        FMG "..Um, you shoot off the screen...to reload. I'm sorry."
        BBW "I see now."
        "She put in another 100 yen coin. Her game didn't improve by much, but she did manage to avoid getting mobbed again. Come the boss, though..."
        BBW "And this is what people do for fun?"
        FMG "Eh, it's not for everyone, I know. I've been playing arcade games most of my life. But yeah, if this isn't doing anything for you, you can stop playing."
        BBW "Not so fast. I'm not going to let some cheap toy beat me." #had suggestion
        FMG "Um actually, they cost a lot of cash to produce, you gotta program, animate the people, it's basically like a movie..."
        "This cycle went on for about an hour, Alice making incrementally more progress with each bit of cash, but eventually I realized the rain stopped."
        MC "Hey, the rain stopped, I should head back to my room."
        FMG "Yeah, Hey...  Alice, the rain stopped, are you going to stop?"
        show BBW angry
        BBW "Not just yet. One more go at that cyber-brain and I should have it beat."
        show FMG sad at Position(yalign=1.0), Transform(xzoom=-1.0)
        FMG "{i}(Yeah I don't think she realizes that's the third boss and there's three more to go...){/i}"
        FMG "Well, see you at class tomorrow, don't play for too long."
        BBW "I'll be fine."
        "We left Alice there, playing that game for who knows how long. As for Akira and I, we exchanged goodbyes and went our separate ways."
    jump daymenu

label FMG012:
    scene Gym with fade
    show FMG neutral with dissolve
    FMG "Come on, harder!"
    MC "Gah!"
    "For the past two hours, with Akira's help, I learned some boxing moves thanks to a punching bag. Once we were done, I could feel myself stronger already."
    $setSkill("Athletics", 1)
    show FMG happy
    FMG "All right Kei-kun, you're definitely improving!"
    MC "Thanks, I guess I have, I'm- wait, did you just call me Kei-kun?"
    if getAffection("FMG") >= 10:
        show FMG sad
        FMG "W-well, I thought it would be alright to call you that since we've been hanging out a lot, if you're not okay about it I can-"
        MC "Oh no, it's fine, I was just a bit surprised is all."
        show FMG happy
        FMG "Oh, glad you like it!"
    else:
        show FMG neutral
        FMG "Eh, I figured if we're working out together it wouldn't hurt to give you a nickname."
        MC "Makes sense."
    show FMG neutral
    FMG "Anyways, I'm glad you're improving; definitely getting the hang of it."
    MC "Yep, I thin- Geh."
    "Perhaps it was the constant punching, but both my neck and back, mostly my neck, felt some uncomfortable pressure. I tried rubbing my neck to relieve some of the pressure, this action did not go unnoticed by Akira."
    show FMG sad
    FMG "Hey, are you okay?"
    MC "My neck... it's feels like there's a vice grip on it. "
    show FMG neutral
    FMG "Do you need my help?"
    MCT "Help? How could she help with my neck? ... Wait a minute..."
    MC "Oh. You mean cracking my neck? Like how you did the first time I meet you here?"
    FMG "Kinda, I've done it a lot so I know the limits of it, but it I'll only do it if you're alright with it."
    "Normally I'd think of what to do next..."
    "..."
    "But I really didn't want to deal with that pain for who knows how long."
    MC "Alright, I'll leave the fate of my neck in your hands."
    "..."
    MC "Pun not intended."
    show FMG happy
    FMG "Ha. Okay, let's do this. Just lie down on this weight bench face up. After that follow my instructions."
    "I followed suit and lied down on the bench, Akira took one hand under my jaw and the other on top of my head."
    show FMG neutral
    FMG "Okay, relax your head. Breathe in..."
    #<breathes in>
    FMG "...And out."
    hide FMG with dissolve
    #<breathes out>
    "*CRACK* *CRACK* *POP*"
    "*POP* *CRACK* *POP*"
    "Surprisingly, what I thought I would feel would be pain, was actually a wave of relief. After this, Akira had me turn on my back, allowing her to rub my neck as well as my back."
    MCT "Huh, who would have thought such a muscular person would be great at massages."
    "This lasted for about twenty more minutes before she finished. Any pain I've felt was gone thanks to Akira."
    show FMG neutral with dissolve
    FMG "Alrighty, feel any better?"
    MC "Y-yeah! Where did you learn to do that?"
    FMG "With how much workouts I do, I have to learn some sort of massage techniques whenever you get sore from working out. Course it's better when someone else does it, but that how it goes."
    show FMG happy
    FMG "... Well, that and the occasional online video of neck and back cracking."
    MC "Ha, well, thanks for that."
    show FMG neutral
    FMG "No prob, it's not often I get to try my skills at being a masseuse."
    MC "Very much so. I think this has been a successful session, wanna get some ice cream?"
    show FMG happy
    FMG "I'd be insulted if we didn't."
    jump daymenu
    
label FMG013:
    #Scene Afternoon
    $setProgress("FMG", "FMG014")
    scene Gym with fade
    play music Schoolday
    "After a long day, I headed back to my dorm and grabbed my gym clothes. Since Akira invited me to watch how she works out, I figured I might end up getting some exercise in myself."
    "Walking over to where she was sitting, I waved and greeted her."
    MC "Yo, Akira!"
    show FMG neutral with dissolve
    FMG "Ahaaay! Yo! Look who's all ready for a nice workout!"
    MC "Yeah, I'm probably gonna do some reps too. I will say, I'm a bit more excited to watch a pro do her thing."
    FMG "Aww, c'mon, I wouldn't say {i}pro{/i}."
    MC "I mean, you-"
    FMG "Now, ready to get a closer look at perfection?"
    MCT "Eheheh... yep, I should have expected that."
    FMG "C'mon, c'mon, c'mon, let's start!"
    MC "Alright, well, you get ready and I'll-"
    FMG "Nah, nah, nah, you're gonna spot me!"
    MC "I... huh?"
    FMG "Yep!"
    "Akira laid down on the bench and brought the bar, loaded with weights bigger than my head, to her chest."
    FMG "Here, try it out."
    MCT "There is... no way in hell I'm going to be able to lift that."
    "Succumbing to Akira's innocent gaze, I put both of my hands on the bar."
    FMG "Nyaah~"
    "With little to no effort, Akira pushed on the bar, making it look as though I lifted her weights for her."
    FMG "See? You're a lifesaver, my dude!"
    MC "Eheh, I mean... thanks?"
    FMG "Yep!"
    FMG "Now, let's do this!"
    FMG "Woo!"
    FMG "C'mon, Kei, do it with me; Woo!"
    MC "W-Woo."
    FMG "Wooo! Let's get it!"
    "Akira clapped her hands and laid prone on the cushioned bench."
    FMG "Aight, well, get some weights and start then."
    stop music
    "Without warning, Akira's normally bright and cheery face suddenly became *far* less inviting. In a look of sheer contempt and dissonance, she began her routine, treating me as though I were a non-entity."
    MC "Woah, you alright there?"
    FMG "..."
    MC "..."
    MC "Um..."
    FMG "..."
    MC "Okay, I guess I can just sit over here, then?"
    FMG "Mm."
    MC "..."
    FMG "*Khm*..."
    MC "..."
    MCT "It feels like I'm in a cage with a lion, like at any second I'm gonna get torn apart if I make even one wrong move."
    FMG "..."
    "She lifted those massive blocks of iron for what felt like a good forty minutes, never once responding to my comments or meeting my gaze."
    "Afterwards, she sat up and began lifting the dumbbells one at a time. Once more, same treatment."
    FMG "..."
    MC "... Is everything alright-?"
    "Akira didn't say anything. She did, however, lower the bar a bit too quick into her chest. Her face went determined and scowly for a moment before she snapped herself out of it and continued."
    FMG "Mm."
    MC "Ah... got it."
    "After a few more reps with the dumbbells, she reached into her bag and rustled around."
    MCT "A... Juice box?"
    "No doubt about it, right on the label; Grape Juice Explosion. A popular brand of kid's juice."
    MCT "Ehhh?!"
    MCT "N-No way. Is she gonna drink that in public?! I remember drinking that as a kid!"
    "Angrily, she forced the straw in and began to sip."
    FMG "... *Sssspp*"
    MC "..."
    MC "Y'know, despite the fact that I just watched you lift twice my bodyweight, it's kinda cute watching you drink juice out of a box like a kid."
    $setAffection("FMG", 4)
    FMG "...Heh..."
    "With only the most subtle of smirks, she went back to drinking from her juice box."
    play music Schoolday
    FMG "WOO!"
    MC "Hoh, shit-!"
    "Nearly making my heart burst, Akira returned to her usual goofy self with a room quaking shout. Pumping her fist, she gave a big, toothy grin."
    FMG "I am feelin' nice!"
    FMG "So, how'd I do? Was it cool?"
    MC "U-Uh..."
    FMG "Speechless, eh? Yep, these puppies tend to do that, hehe!"
    MC "Uh, yeah, you looked... kinda pissed, though."
    "What I imagined what was going to happen was either she was going to laugh it off or get actually angry at me... but what happened was she looked surprised and then sad."
    FMG "Pissed? O-oh shit, sorry dude.  I guess when I get too focused on my workout I can come off as a jerk. I never noticed cuz nobody wants to work out with me..."
    MC "Hey don't worry about it okay?"
    FMG "Umm, you sure? I don't want you to get used to that type of attitude. I'm surprised you actually showed up, most people I invite to work out with me don't."
    MC "Hey, we all have our bad days. This is probably just one of those days for you. I know you're not like that, okay? Besides, those people probably don't have to motivation to work out in the first place."
    FMG "Yeah okay; I guess I can't focus JUST on the weights when I have someone with me. The only things a girl needs in life to make her happy is someone to spot her, a goal to work towards, and a whole ton of protein!"
    MC "*pfft*"
    FMG "Eh?"
    MC "S-Sorry, that was immature."
    FMG "..."
    FMG "PFFF GYAHAHAHAAA~"
    FMG "Oh damn, nice one, dude. You got me on that."
    MC "Eheheh."
    "I couldn't help but chuckle with Akira. It wasn't even my dumb joke that got me, it was the fact that my dumb joke got her."
    FMG "Man, I oughta hang out with you more."
    FMG "So... how's about we do just that!"
    MC "Eh?"
    FMG "Same time tomorrow, you'll spot for me, let's do it!"
    MC "I- uh,"
    FMG "Yeees, yes, say it, *yeees*."
    MC "Y-Yes."
    FMG "Woo!"
    "Jumping up in joy, I could feel the impact of her landing all the way up to my knees."
    FMG "You won't regret it, dude. Same time tomorrow!"
    MC "Same time tomorrow."
    "As Akira grabbed her bag and walked out the door, I couldn't help but think about everything that just transpired... and I couldn't stop myself from smiling at the prospect of being a part of it again. I picked up some weights myself, and began training for next time."
    $setSkill("Athletics", 3)
    jump daymenu

label FMG014:
    $setProgress("FMG", "FMG015")
    scene School Planter with fade
    play music Schoolday
    "You know, sometimes you gotta just walk around campus and see the sights. The gardens looked beautiful that time of year, it's great to enjoy yourself without a care in the-"
    FMG "KEISUKE!!!"
    MCT "Oh god she's running straight at me again!"
    "..."
    MCT "And she's bigger this time!"
    "Once again I prepared for my immediate demise, but alas, Mizutani-San stopped just before I could be reunited with my Great Uncle Lee."
    show FMG neutral with dissolve
    FMG "Hey dude, you got a sec?"
    MC "...Y-yes?"
    MCT "This girl is going to be the death of me."
    show FMG sad
    FMG "I need your help with something. I'm sucking at algebra and I need your help with the quiz next week."
    MC "Oh, you need me to help you study?"
    show FMG neutral
    FMG "Hell no. I need you to convince your roommate to get the answer sheet for me."
    ". . ."
    MCT "I have several questions!"
    MC "Okay first off, why my roommate? Second of all what makes you think he can even get the sheet in the first place!?"
    FMG "Because a few days after the nurse appointment thing, I was getting a bottle of water from the vending machines when I saw that he was using his 'Special Tactics', i.e. he was hiding in a tree. I snuck up on him and he just jumped off and ran like hell."
    "Honestly, I should have asked more questions to that...but I was getting a headache at the idea of my roommate and Akira in one room."
    MC "If you know of him, why don't you ask him yourself?"
    show FMG sad
    FMG "I would if he was easy to get into contact. I've tried to find him, but given his... “Tactics” he's not the kind of guy that wants to be found."
    show FMG neutral
    FMG "So yeah, can you get him?"
    jump FMG014_c1

label FMG014_c1:
    menu:
        "Agree":
            jump FMG014_c1_1
        "Teach her yourself" if not getFlag("FMG014_testfail"):
            jump FMG014_c1_2
        "Teach her yourself (disabled)" if getFlag("FMG014_testfail"):
            pass
        "Don't do it":
            jump FMG014_c1_3

label FMG014_c1_1:
    MC "*sigh* Fine. I'll go find him."
    show FMG happy
    FMG "Yes! Thanks dude, I'll be waiting behind the bookstore."
    MCT "We have a bookstore?!"
    scene Dorm Interior with fade
    MC "Hey Daichi, Can I talk to you about something?"
    show RM neutral with dissolve
    RM "Depends are you bugged?"
    MC "H-How should I know?!"
    show RM smug
    RM "Good answer. You're learning."
    MCT "Come on, you can do this...probably."
    show RM neutral
    RM "So what do you need?"
    MC "You know Mizutani right?"
    RM "Big girl, muscle growth factor, brown hair and eyes. Has an unhealthy - and given her lifestyle, ironic - obsession with arcade games and ice cream?"
    MC "Yeah."
    RM "What about her?"
    MC "She wants you to steal the answer sheet for algebra class."
    RM "She does realize the teacher would give everyone F's if that were to happen, right?"
    MC "...Why aren't you denying that you can't steal it?"
    show RM happy
    RM "Because I can. You've known me long enough to know that."
    MCT "What gave you that idea!?"
    show RM neutral
    RM "Alright, I'll meet with her, where is she?"
    MC "At the bookstore... hey did you know-"
    show RM angry
    RM "Oh my god, look out the window! What's Inoue-san doing? Is she taking off her shirt?"
    hide RM with dissolve
    if getAffection("BE") > 5:
        MC "Oh great, what has she gotten herself into now..."
        "Thankfully, when I looked out of the window, there was no exposed Honoka."
        MC "Well that's a relief, but Daichi why-"
        "As I turned around, there was nothing there but an open door and the faint. sound of Daichi running."
    else:
        MC "Wait, really!?"
        "I ran towards the window, alas there was no topless Honoka... And I heard Daichi running out the door..."
    MC "..."
    "I looked up to the heavens, as if they could answer my prayer for answers."
    scene Town with fade
    "By the time I got to the back of the bookstore, Akira...was all alone. I have no idea why I thought Daichi would be here."
    show FMG neutral with dissolve
    FMG "Hey dude, how'd it go?"
    MC "He told me he'd be here, but where is he?"
    FMG "Oh he's behind you."
    MCT "What."
    show RM neutral at Position (xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    show FMG neutral at Position (xpos=0.75) with dissolve
    RM "Hello."
    MC "AHHH!"
    MC "Dude! How?!"
    FMG "Meh, does it matter?"
    MC "Yes! And how come you're so calm about this?!"
    FMG "Because I'm looking at the bigger picture."
    MC "Can you at least tell me how you know each other?"
    RM "No time, Matsumoto-san may show up and give us a lecture, which is why I agreed to this meeting."
    MC "That just raises more questions! Why would Shiori giving us a lecture make you agree to this meeting?!"
    show RM angry
    "He simply gave me an annoyed look."
    MCT "These guys are going to be the death of me!"
    FMG "So can you get that sheet?"
    show RM neutral
    RM "I can, but I have one condition."
    show FMG angry
    FMG "Ugh, you're lucky I'm desperate. What are your terms?"
    RM "I need a bodyguard. My investigations have gotten some powerful people angry at me; so I need the biggest, strongest person at this school. That's where you come in."
    RM "Since this is a long term commitment to short term requirement, I'm willing to pay you for your services as well; let's say 1500 a day?"
    show FMG neutral
    FMG "Fine, that works."
    show RM happy
    RM "Thank you for your cooperation. Is that everything?"
    FMG "Ya, later and thanks."
    RM "So long!"
    hide RM with dissolve
    "Upon saying that, he throw something on the ground... it was a rock. When I looked up, Daichi was gone..."
    show FMG happy at Position(xpos=0.5)
    FMG "Well, glad to get that done. Thanks for your help, Kei. See ya!"
    hide FMG with dissolve
    MC ".  .  ."
    MC "God, I need some ibuprofen now."
    jump daymenu

label FMG014_c1_2:
    MC "You know, I can help you with your homework."
    FMG "Oh really, then?"
    "She pulled out a piece of paper from her bag, I assume that it was her homework, and my assumption was correct."
    FMG "What is 7x+5=2(x+10)?"
    if getSkill("Academics") < 5:
        MC "... Umm ... can I have a piece of paper?"
        $setAffection("FMG", -1)
        show FMG angry
        FMG "Ugh, I'm not wasting all this time dude."
        show FMG sad
        FMG "Can you stop messing around and go get your weird roomie, please?"
        $setFlag("FMG014_testfail")
        jump FMG014_c1
    else:
        MC "If you give me a piece of paper, I can show you."
        FMG "Ah all right, you seem to know what you're doing."
        "Reluctantly, Akira handed me a piece of paper. It took me a bit but in the end..."
        MC "And there you have it, 3."
        $setAffection("FMG", 2)
        show FMG surprised
        FMG "... Wow, really? Looks like you showed me, huh?"
        show FMG neutral
        FMG "I guess I don't need that sheet after, if you help me, that is."
        MC "I would love to help you."
        show FMG aroused
        FMG "T-Thank you, I appreciate it."
        scene black with fade
        pause 1
        scene School Planter with fade
        "I spend the rest of the day helping Akira with her homework. By the time we were done, the sun was starting to set."
        MC "Well, that's everything then."
        show FMG happy with dissolve
        FMG "Yep! Hey, it's getting late; we should call it a day. Thanks again!"
        hide FMG with dissolve
        MCT "You know, I can't help shake the feeling like I really helped her. I wonder what is in store for us."
        jump daymenu

label FMG014_c1_3:
    MC "*sigh* Look, I'm sorry, but I got such a headache right now that I'm just going..."
    $setAffection("FMG", -2)
    show FMG sad
    FMG "Wow... Dick move."
    MC "Look I-"
    FMG "Nope. Glad to know your headache is more important than my grades. If you need me, I'll be staying up all night trying to figure out the test..."
    show FMG angry
    FMG "Again."
    hide FMG with dissolve
    MC "... God I hope she doesn't take this personally..."
    jump daymenu

label FMG015:
    $setProgress("FMG", "FMG016")
    scene Town with fade
    play music Sunset
    "The day began with a rain shower that followed suit till the afternoon, giving the air a more clean sensation. With it being the weekend, I felt like going out on the town with some spending money."
    "The streets were full of bustling people given the time and day, everyone was either working or buying things from the many open stores. Seeing so many going shopping made me feel like buying something too."
    "As I was taking in the sites as well as wondering what store I should go to, a thought came to me."
    "Akira had been going out of her way to help me work on my muscles; while I did believe that just working out was payment enough for her, I felt like I should at least give her something."
    "While lost in thought, I came across a store called ‘ Pop Culture’, the front of the building was made of bricks and concrete, with anime figures and cardboard cutouts in the window frames. I figured this was as good a spot as any, so I went inside."
    "The store seemed to, as the name implied, caters to pop culture of this generation, the inside also had brick walls as well as posters of various media. The stores goods for sale consisted of toys, games, and of course, clothing. Now because of my only knowledge of what I went to the hoodie section to find a few that popped out to me."
    "On the right was a gray hoodie, the hoodie was a weightlifting stick figure sweating profusely, with the words ‘No Pain no Muscle Gain.’ on the bottom. Considering her lifestyle, Akira might love this one."
    "In the middle was a crimson hoodie and this one was a detective looking man holding a gun, and the words ‘Sun’s out Guns out!’ were displayed in a word bubble. I think I recognize the guy from that one arcade game Akira likes, Cyber Rage."
    "Last but not least was … a mint green hoodie that has a picture of a cute anime cat girl with white stripes on the left chest area... on the back was the words ‘ Nya’dorable’ above four anime cat-girls."
    "…"
    MCT "I’m tempted to get it just as a joke."
    menu:
        "No Pain no Muscle Gain.": #+1
            $setFlag("FMG015_c1_1")
            MCT "Well, she does work out a lot, I’ll get her this one, I’m sure she’ll like it."
        "Sun's out Guns out!": #+2
            $setFlag("FMG015_c1_2")
            MCT "Well, she sure does love arcade games, I think she’ll like this one a lot."
        "Nya’dorable.": #+5
            $setFlag("FMG015_c1_3")
            MCT "... Yeah I don’t know if she’ll like this… but it might be funny to give this to her."
    "With the sweat shirt in hand, I paid for it, and set my sights on finding Akira."
    "I figured that given I was already in town, I would start my search for her at the local gym."
    "The gym itself was about what you expected,  white walls, dark blue carpet flooring, buzzing lights, and workout equipment. The number of occupants was low given the time of day, however over in the far back I could see Akira on, something that she called a “Rowing Machine”, pulling the rope thing in a similar manner of rowing a boat."
    "It did not take long for her to see me, she smiled and gave me a wave to come over."
    show FMG happy with dissolve
    FMG "Sup Kei-kun! What brings you to this side of the island?"
    MC "Well, I wanted to thank you for going out of your way to help me workout. So I got you something?"
    show FMG neutral
    FMG "Hmm? You got me something? What is it?"
    "I handed her the bag with the hoodie in it. She pulled it out to get a good look at it..."
    if getFlag("FMG015_c1_1"):
        "… Only to look a mix between confused and disappointed."
        show FMG sad
        FMG "…Oh...umm."
        MC "Something wrong?"
        FMG "Well, don't get me wrong, I appreciate the hoodie and I am probably going to wear it...but don't you think it's kinda generic and unoriginal?"
        MCT "... In hindsight, Akira was never one to cater to the cliche of being a muscular tomboy..."
        MC "Oh...I'm sorry, it's just that I when I saw it I thought of you."
        show FMG surprised
        FMG "...You...thought of…"
        "It appeared that my words had swayed her in someway. Her slight disdain turned into surprised and then joy."
        $setAffection("FMG", 1)
        show FMG happy
        FMG "You know what, I really appreciate it that you got me this."
    elif getFlag("FMG015_c1_2"):
        "… and upon seeing it, looked happy."
        show FMG happy
        $setAffection("FMG", 2)
        "Aww sweet! It's Matthew Ryberg from Cyber Rage:CB saying his famous catchphrase!"
        MC "Oh, you like it?"
        FMG "Yeah I do! Thanks dude!"
    else:
        "… And her reaction was not confusion like I had predicted, but pure joy and excitement… and that was an understatement."
        show FMG surprised
        FMG "Is that..."
        show FMG happy
        FMG "*GASP* OH MY GOD! I LOVE NYA’DORABLE!"
        "She was squealing like a child."
        MCT "...Huh?"
        MC "Wait, really?"
        FMG "Yeah! I was in grade School when the manga came out and I’ve been a huge fan of Nya’dorable ever since! I've even plan to watch the anime when it comes out this summer!"
        FMG "I mean, sure I’ll have to cut the sleeves and a bit of the gut area, but I absolutely love it! How did you know?!"
        MC "I… had a hunch."
        show FMG neutral
        FMG "Guess you got lucky then. After all, love it!"
        "She pauses for a moment."
        FMG "Though..."
        show FMG happy
        FMG "...I’m glad you didn’t get something that has a bodybuilder on it or something."
        MCT "!!!"
        MC "Yeah...right..."
    show FMG happy
    FMG "Hey look, as much as we workout, why don’t we just hang out?"
    MC "Sure,we already in town, let’s go exploring."
    FMG "Alright! Just wait right here while I make the appropriate trimmings on this in the locker room, I’ll be right back."
    "It didn’t take her long to trim the hoodie, roughly ten minutes or so. By the time she came out, she was wearing the hoodie with pride."
    FMG "Okay! I'm dressed to not impress and hyped!"
    MC "So what's the game plan?"
    FMG "Funny you should say. We're going to the one place I go when I'm bored and don't feel like exercising."
    FMG "The arcade!"

    scene Arcade with fade
    "After about a 15 minute walk, we made it to Akira’s favorite arcade, Grand Blaze Arcade."
    "Inside was filled with the sounds of a hundred arcade games being played mixed with the sounds of enjoyment from People of various ages playing. Beyond that there wasn’t much in the way of decoration beyond the arcade cabinets."
    "There was a man behind the front counter. Late 20’s black hair covered with a baseball hat, glasses, beard and wearing a gray long sleeve shirt."
    show FMG happy with dissolve
    FMG "Yo Fujimoto!"
    Fujimoto "Hey Mizutani, not everyday you come here before six pm, let alone bring someone with you. What's the occasion?"
    FMG "Wanted to hang out with this guy for getting me this hoodie!"
    Fujimoto "Nice, have fun you two."
    FMG "We will."
    FMG "Alright, I got a bunch of coins in cases like this. Let's do this!"
    "For the next hour and a half, I played various arcade games with Akira. Spending time with her, either exercising or just hanging out, has been enjoyable and exhilarating."
    jump daymenu

label FMG016:
    scene School Planter with fade
    play music Sunset
    "It was such a beautiful day; the sun is shining, the birds were  flying, the wind was blowing..."
    "...And I was so bored!"
    "Seriously, normally I'd have something to do, but for the life of me I can't think of anything to do besides lay down on the grass, stare at the blue sky, and sulk in my boredom!"
    "My vision of the sunlight was then blocked by Akira standing over me."
    show FMG neutral with dissolve
    FMG "Hey Kei-kun, how's it going?"
    MCT "Finally! Something not boring! Thank you my savior! Wait, she's expecting a response. Quick you fool! Say something!"
    menu:
        "I'm bored.":
            MC "...Bored..."
        "I'm SUPER bored.":
            MC "...Super...Bored..."
        "I'm so bored I fear the onset of rigor mortis.":
            MC "...too bored.. for big words..."
    show FMG happy
    FMG "*Giggle*"
    MCT "...Smooth move, genius... well, at least Akira got a giggle out of my suffering."
    FMG "Well then, how about you take that offer of mine, and let's head into town?"
    MC "Yes! ...I mean. sure."
    "..."
    MCT "Okay well, I'm just going to ignore my small outburst and follow Akira to town."
    FMG "Man, you're nuts, dude. Well, come on, let's see what the town has to offer."
    scene Town with fade
    "While walking down a street, we came across what appeared to be a shopping district dedicated to technology and electronics. Despite the fact we could pick literally any electronic store, retro shop, or even the otaku store to check out..."
    show FMG neutral with dissolve
    FMG "You know what, what the hell, let's check out this café!"
    "...She picks the only maid café in this district, if not the entire town."
    MC "...Um, that looks like a maid café."
    FMG "Yeah so? I want to see what the fuss is about with these places. Guess you never thought I'd be up for something like this?"
    MC "A little, I'm more surprised there's even one on this island."
    FMG "Meh, I think the town's main income comes from the school, so they probably want to get every niche of school life for extra income."
    MCT "Huh, that actually makes sense."
    MC "Well, you've convinced me."
    show FMG happy
    FMG "All right!"
    scene Cafe with fade
    play music Schoolday
    "As we entered the café, we were greeted with a flurry of pink and white decorum. The room itself felt inviting, if not a bit too... pastel, for my tastes. Still, effeminate style or not, it gave of a naturally comfortable aura enough to beckon us to stay."
    show FMG neutral with dissolve
    FMG "Huh, this place is cute."
    MCT "I find it more cloying than cute."
    "Once we were done ‘admiring' the scenery, we took our seats and waited for the waitress."
    MC "You know, never thought we'd be in a café like this."
    FMG "Well, I don't know about you, but I'll try anything once."
    "About two minutes later, our waitress came by, but I couldn't shake the feeling I knew her."
    show Chibuki neutral at Position(xpos=0.75) with dissolve
    show FMG neutral at Position(xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    Chibuki "Hi, welcome mast- oh, crap."
    show FMG surprised
    FMG "Wait a minute, CHIBUKI?!"
    MC "Wait is that rea-"
    Chibuki "*ahem* Why masters, I would love to have a conversation once my break starts, until then what would you like?"
    MC "Um... the Sunshine Sundae with extra nuts."
    FMG "...Milk tea."
    Chibuki "Fantastic choices! I'll have them right away!"
    hide Chibuki with dissolve
    MC "...Well this is happening, I guess."
    "I didn't get a single response. Akira was silent the entire time, staring at the spot Chibuki was. Though to be fair, it must have been quite the shock, seeing your roommate acting the exact opposite way you'd always seen her... while dressed as a maid."
    show Chibuki neutral at Position(xpos=0.75) with dissolve
    Chibuki "Here you go, and I'll see you in 10. Till then masters, I bid you adieu!"
    hide Chibuki with dissolve
    "We did nothing but consume our orders in silence while we waited for Chibuki's break to happen."
    scene Town with fade
    play music Sunset
    "Once we finished and it was time, we went out to the front of the store with no sign of Chibuki. I heard a ‘hey' from the alleyway, and followed it to find Chibuki down there waiting for us. Both Akira and I walked down the alleyway to meet up with Chibuki."
    show Chibuki neutral at Position(xpos=0.75) with dissolve
    show FMG neutral at Position(xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    Chibuki "God, out of all the people in the world to come to this one maid café, it had to be my roommate and her boyfriend!"
    "Chibuki vented out her frustrations, though in our defense this island wasn't exactly Tokyo."
    if getAffection("FMG") > 10:
        show FMG aroused
        FMG "B-boyfriend?"
        show FMG surprised
        FMG "I-I mean um..."
        show FMG neutral
        FMG "Uh hey Chibuki, I almost didn't recognize you without your bulging nips."
    elif getAffection("FMG") > 5:
        FMG "Ha, boyfriend; He's just a friend Chibuki. But back to you, I didn't recognize you without your bulging nips!"
    else:
        show FMG angry
        FMG "Geez, Chibuki. You think I can't talk to a guy without it meaning something? "
        show FMG neutral
        FMG "Getting back on track, you look different without your bulging nips!"
    Chibuki "Yeah well, My growth is still concealable so I don't have to worry too much for now. Besides, all the padding over them to smooth out the bulge makes me look bustier, which usually means more tips."
    MC "I never would have thought you would work here."
    Chibuki "I think I got the job because I'm half-British, guys love the British maid type. Plus I guess they wanted some variety."
    show FMG surprised
    FMG "But why are you even working here in the first place?!"
    Chibuki "I want money, the job pays well."
    show FMG neutral
    FMG "Chibuki, I know you too well. If that was the case, than why didn't you get a job at a mini market or something less... degrading."
    Chibuki "... Fine! I really like acting like a maid, ok! It's one of my biggest fantasies ever! The maid falling in love with her master, willingly mind you... I find it romantic, THERE, HAPPY?!"
    MCT "Huh...never picked Chibuki as the hopeless romantic type."
    Chibuki "Look, if any of the students, god forbid Shiori, finds out about this, then I'm so boned. Gossip spreads fast. Akira, if you keep quiet about this... I'll clean my half of the room. And Kei..."
    $setVar("RinFavor", getVar("RinFavor") + 1)
    if getVar("RinFavor") >= 1:
        Chibuki "I know I already owe you a favor Kei, but I'll give you another for your word."
    else:
        Chibuki "I'll give you a favor for later, deal?"
    FMG "On one condition Chibuki. You gotta clean the room, while dressed as a maid!"
    MCT "I can't tell if she's serious or not, maybe I should-"
    Chibuki "I'll do it."
    show FMG surprised
    FMG "..."
    FMG "WHAT?!"
    Chibuki "If that's what it takes to buy your loyalty, then so be it...  master."
    FMG "...Nope. Nope I'm not dealing with this! Nope! I'm nope'ing back to the dorms and then I'm going to nope myself to bed... nope... nope..."
    hide FMG with dissolve
    "Akira just left, repeating ‘nope' to herself till she was out of earshot. I turned to Chibuki to say something, but to my confusion and surprise, she was grinning like she'd won something."
    show Chibuki neutral at Position(xpos=0.5)
    Chibuki "And that, my dear Keisuke, is how you win a battle against your roommate."
    MC "...Huh?"
    Chibuki "That whole romantic BS was just to fluster Akira; an act, if you will. Dad always did say I had the makings of a great method actor."
    MC "Then, why are you working here?"
    Chibuki "For the money of course. I thought we established that. Now then, my break is almost over. Oh and don't worry, the favor's still there so long as ya keep this on the down low."
    "Before anything was said, She... did that weird peace symbol pose and winked..."
    Chibuki "Come again, master! <3"
    hide Chibuki with dissolve
    "Once she was finished with that, Chibuki went back into the café."
    MC "Well, at least I'm not bored anymore... "
    MC "..."
    MC "....."
    MC "...Aaannnd I'm bored again. What am I going to do now?"
    jump daymenu
    
label FMG017:
    $setProgress("FMG", "FMG018")
    scene Campus Center with fade
    play music Busy
    show FMG neutral with dissolve
    MC "So, how’s life been?"
    FMG "Eh, nothing much has changed really, my mom send some cookies from home, so that was nice of her."
    MC "Oh, your mom bakes?"
    FMG "Oh yeah, she likes to bake, something about it being relaxing for her."
    MC "How long did it take to get your care package?"
    FMG "Well, about a day or so because it takes a plane to get from here to Okinawa."
    MC "Oh, you’re from Okinawa, explains your accent."
    show FMG happy
    FMG "Yep, born and raised. Might not hold the same excitement Tokyo has, but it’s home and I love it. I’m a fourth-generation Mizutani that’s lived there."
    MC "Huh that’s cool. Hey, speaking of moms, mines been sending mail. Not packages or anything but just normal mail."
    show FMG neutral
    FMG "What does she not use email?"
    MC "She does, the thing is that she doesn’t want to clutter my inbox."
    show FMG sad #confused
    FMG "… So she thinks it’s better to clutter your dorm room with real mail?"
    MC "I didn’t say it made sense."
    show FMG neutral
    FMG "Ignoring that, what kind of massage has she been sending?"
    MC "Well, it’s mostly just “how are you doing?” and such. in the latest one, she was asking about how why my sis-"
    show FMG surprised
    FMG "O-Oh no!"
    "Alas, I was not able to complete my sentence about how my sister has not been replying to mother’s mail thanks to Akira. My confusion as to why Akira interrupted me was answered to what was in front of us."
    "A raggedy old stuffed bear on the ground; there wasn’t anything odd about it, but it was kinda an eyesore. I went up to it to gra-"
    stop music
    FMG "Woah Woah Woah, do NOT touch that bear!"
    MC "What?"
    show FMG sad
    play music Tension
    FMG "Don’t you know that picking up abandoned scruffy dolls on the ground will bring you bad luck!?"
    MCT "I legit have never heard that before."
    show FMG neutral
    FMG "Trust me, I’ve seen it happen to another kid when I was in kindergarten."
    MC "… Okay, you have to explain this one."
    "Akira had taken a breath in before explaining what kind of oddity she had as a child… one of several now that I look back on it."
    FMG "Well, what happened was this girl, she found an old-looking stuffed rabbit on top of the slide. She wanted to ride the slide, so she grabbed it and tossed it; the moment she slid down, she went faster then she should and crashed into the sand ass up. Ever since then, word got around town and thus, a curse was born."
    "Her story explained why I never heard of it since it was only local. Though in all likelihood, that girl crashing seems to be more out of bad luck than a curse from a stuffed rabbit. Despite this, it did not call much of my confusion on the subject matter."
    MC "Okay, well, even so, it shouldn’t matter because we’re nowhere near Okinawa."
    show FMG sad
    FMG "Be that as it may, I don’t think it’s a great idea to mess with that bear. Look, just don’t pick it up okay?"
    menu:
        "Pick it up.": #-1
            jump FMG017_c1_1
        "Don’t pick it up.": #+1
            jump FMG017_c1_2

label FMG017_c1_1:
    MCT "Yeah, that thing looks as harmful as a… thing that’s less harmful than a teddy bear… whatever, I’m picking it up."
    MC "See, no harm do-"
    MCT "QUACK!"
    MC "Wha- GAH!"
    stop music
    show FMG surprised
    "Somehow out of nowhere a duck came in and started to attack me. It got so bad I dropped the bear."
    MC "AHHH! DUCK! GET IT OFF OF ME!"
    MC "HELP!"
    MC "AKIRA!"
    "For five minutes the stupid duck kept attacking me, all the while Akira was just watching me being assaulted by a duck. It didn’t stop until I laid down and pretended to be dead."
    "By the time the duck left, I was beaten and my clothes were a mess. Akira on the other hand just looked at me in disappointment."
    show FMG sad
    $setAffection("FMG", -1)
    FMG "Yep, I was right. Can’t say I warned you. Maybe if I leave you there you’ll learn to believe in curses."
    hide FMG with dissolve
    MCT "Yep, she left me on the ground…"
    MC "I hate ducks now."
    jump daymenu

label FMG017_c1_2:
    stop music
    MC "Alright, I won’t pick it up."
    "As much as I wanted to, I wasn’t going to lose sleep if I didn’t pick it up."
    show FMG happy
    $setAffection("FMG", 1)
    FMG "Phew, thanks Kei-Kun. No telling what would have happened if you picked up that plushie."
    "With my decision made, I left the bear on the ground where it sat, however just when we thought it was over, we heard someone and…"
    hide FMG with dissolve
    show BE sad with dissolve
    BE "Aww poor thing, why would anyone abandon you..."
    show BE happy
    BE "Don’t worry, I’ll give you a new home little gu-"
    "Inoue-san was about to bend over to pick up the doll, we didn’t have a chance to say anything before she grabbed it and-"
    "{i}POP! POP! POP!{/i}"
    "Every single one of her shirt buttons popped off, leaving absolutely nothing left but her bra for the world to see."
    show BE neutral
    BE "A-ah…"
    show BE sad
    BE "I…I..."
    show BE angry
    BE "Awww not again… I just got this top!"
    hide BE with dissolve
    "All Honoka could do was run towards the dorm rooms. She was so focused on her lack of ability to button her shirt that she left the bear in its place."
    play music Schoolday
    show FMG surprised with dissolve
    FMG "Yep, I was right, that thing is cursed…"
    MCT "WOW. Am I glad I didn’t touch it."
    jump daymenu

label FMG018:
    $setProgress("FMG", "FMG019")
    scene Classroom with fade
    play music Schoolday
    "Morning class... Some would argue that no one would be awake enough to learn anything so early, but luckily this time, the teacher planned something different for that day."
    show HR neutral with dissolve
    HR "All right class, today is the planned cooking class. For those who don't remember, to better prepare yourselves for your self-sufficient futures, you will have the next three hours to test your cooking skills."
    HR "The food you choose to make will not lower your grade, but how well you make it. Now get your books and bags together because you're not coming back and Takamura-san and I will explain more there."
    hide HR with dissolve
    "Once he was done explaining, we all prepared to leave..."
    "..."
    "Except Akira... who was sleeping on her desk... again."
    MC "Akira wake up, we gotta go."
    FMG "Ugh... Get your hands off my pizza Reginald... I'm the pizza queen..."
    MCT "Geez What kind of dreams does she have? Wait, I'm getting distracted."
    MC "Akira, wake up!"
    show FMG neutral with dissolve
    FMG "Wha... Oh, good morning, Kei-Kun. I had this dream where I was the queen of Italy and there was..."
    show FMG sad
    FMG "...Uh, where's the rest of the class? Don't tell me it's Sunday and I walked to class without checking again."
    MC "No, the class is going to the cooking classroom to do test our culinary skills."
    show FMG neutral
    FMG "Oh, that's cool..."
    show FMG surprised
    FMG "Wait, what?!"
    MC "Um yeah, we're going to cook."
    show FMG sad
    FMG "But Kei-Kun, I can't cook! Every time I do it catches on fire!"
    MCT "Well... Honestly I am not that surprised by this discovery..."
    if isEventCleared("FMG004"):
        MCT "Especially when she couldn't even make a simple protein shake."
    MC "Well, we don't know what exactly is happening. For now let's get with the rest of the class, before they notice we're not there."
    show FMG neutral
    FMG "Okay... but I'm warning you, it will not come out edible."
    scene Cooking Classroom with fade
    "We managed to catch up with the rest of the class before anyone (especially Shiori) figured out we were behind."
    "Once we were at the cooking class, we waited till the cooking teacher began explaining."
    Takamura "So, here's what we have planned, you will team up in groups of three to create any dish you can find a recipe for, be it from the cookbooks here or online."
    "As the teachers were explaining, Akira pulled me aside."
    show FMG neutral with dissolve
    FMG "Okay Kei-Kun, there is no way I'm going to be able to make anything without help, so can you please help me?"
    MC "Oh. Sure, I'll be happy to."
    FMG "Thanks, but what are we going to do about a third person?"
    "That was the question most, if not all, students were asking as they started to partner up. The thought of Aida being a suitable partner popped up, however she was taken almost right away by Alice, so that was out of the question."
    MC "Looks like the only ones who don't have a partner are Shiori, Naomi, Honoka, and that guy who always eats seaweed in the back of class."
    FMG "Well we gotta pick a third person, so who should it be?"
    
    menu:
        "Choose Shiori":
            jump FMG018_c1_1
        "Choose Naomi":
            jump FMG018_c1_2
        "Choose Honoka":
            jump FMG018_c1_3

label FMG018_c1_1:
    MC "Well, let's ask Matsumoto, maybe she can help."
    FMG "If you say so... I have my doubts, though."
    "Ignoring Akira's doubts, I followed suit and walked towards Shiori. For her part, she was still by herself, looking deep in thought."
    show FMG neutral at Position(xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    show AE neutral at Position(xpos=0.75) with dissolve
    MC "Hey Matsumoto-san, what's on your mind? Akira and I are teaming up, do you need a partner?"
    AE "Hmm... It appears that I do, very well."
    AE "I can't say most of these recipes are to my tastes. Perhaps something I can recall from memory, then?"
    MC "Sure. Whatever works. Though I figured you would want to cook by the exact recipe-"
    show AE neutral-smug
    MC "You remember the exact recipe."
    AE "Of course."
    show FMG happy
    FMG "Wow, that's awesome of you!"
    AE "What say you to a plate of 'Himmel und Erde', hm?"
    show FMG neutral
    FMG "Eh? H-Hey, was that French? Are we gonna make French food, because I can't even cook cereal right."
    AE "No, that was German. It means 'Heaven and Ea-'"
    show AE surprised
    AE "Did you just say you can't make cereal?"
    FMG "Yeah, my mom never taught me how to cook it."
    show AE neutral
    AE "Make."
    FMG "Cook, right."
    show AE neutral-eyebrow
    AE "..."
    show AE neutral
    AE "T-The recipe, um... the recipe we'll make calls for black pudding, mashed potatoes, applesauce, and cooked onions. Fairly straightforward, no unnecessary bells and whistles."
    MC "Wait, what's black pudding?"
    FMG "You can cook onions? I thought they were just a hamburger topping."
    AE "Yes. Yes you can."
    AE "Black pudding is a type of pudding made from oatmeal-"
    MC "Okay."
    AE "A bit of salt-"
    FMG "Okay."
    AE "Pork fat, pork blood, and mixed in with some oat groats."
    MC "W-Wait, did you say *blood*?!"
    FMG "I'm cool with that, but what's a groat?"
    MC "I don't even know where we'd get pork blood!"
    AE "Well, I *believe* that it should be among the pork products. Check with the teacher, if you will. As for the other ingredients, we have those right here."
    FMG "All right, guess I'll go grab the ingredients then. Kei-kun, maybe do whatever Shiori tells you."
    scene black with fade
    "After a discussion with a confused teacher, I later found that the fat, blood, and other rendered parts of the animals could be found in the school kitchen."
    "At the very least, I know the food here's fresh."
    scene Cooking Classroom with fade
    show FMG neutral at Position(xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    show AE neutral at Position(xpos=0.75) with dissolve
    MC "Yo! I'm back with the blood."
    AE "Ah, splendid. We've been working on the mashed potatoes."
    FMG "Yeah! Check *this* out."
    "In her excitement to help, Akira picked up an unpeeled potato and placed the potato between her forearm and upper arm and mashes it with a bicep flex, with such great force that the chunky remains splattered into a bowl."
    if getAffection("FMG") > 12:
        MCT "Huh... that's... oddly interesting."
    AE "Aha...Well, if you'd like to contribute more, then how about coring the apples for the applesauce? There should be a device for it under the kitchenware."
    MC "Yeesh, this place has everything."
    AE "I'm honestly surprised. I've yet to find anything we need that isn't here. I'm glad the increase to the culinary budget is going to good use."
    FMG "Yet somehow we still can't get decent coffee in the cafeteria. Anyways, where are those apples?"
    AE "Over near the other fruits on the counter. I'll get the cinnamon for the apples."
    "After some gruesome time cooking, we finally completed the dish Shiori assigned to us. Each turned out well... about as well as we could hope, at least."
    AE "All right, I believe that should be all. Now all we need is to wait for our grades after a quick test of quality."
    FMG "Woo!"
    MC "Eheheh..."
    show FMG happy
    FMG "A+ baby, let's go!"
    show FMG neutral
    "After a moment, Mrs. Takamura came over to test our individual plates, starting with Shiori-san."
    Takamura ".... Mm... very nice! What did you say this was?"
    AE "Himmel Und Erde, ma'am."
    Takamura "Splendid!"
    AE "... Indeed."
    Takamura " Keisuke, good work as well. A bit heavy on the cinnamon, but that's okay."
    MCT "Yes!"
    Takamura "And... Mizutani-san..."
    FMG "Nehehe~ It'll be fine!"
    Takamura "Y-You're right, it can't be that bad..."
    Takamura "..."
    Takamura " ... Passable!"
    $setAffection("FMG", 2)
    show FMG happy
    FMG "YES! YEAH! WOO!"
    Takamura "Hmm, a bit heavy on the cinnamon- *urch*... but passable!"
    "Shiori let out a sigh, whether out of disappointment or relief, I wasn't sure."
    FMG "Finally! I cooked something that didn't taste like ash!"
    show FMG neutral
    FMG "Shiori, thank you for helping us, I ain't exactly the best cook!"
    FMG "I mean, ask me to help hook up a CPU board to a switching power supply for an arcade cabinet any time, but for the life of me I can't cook."
    AE "Think nothing of it, Mizutani-san. Please, if you need help on group projects in the future, don't hesitate to-"
    show FMG happy
    show AE sad
    AE "I've made a terrible mistake, haven't I?"
    FMG "Oh, you worry too much, how bad could helping me be?"
    AE "Nuugh..."
    jump daymenu

label FMG018_c1_2:
    MC "Let's ask Naomi, she might be a good cook."
    FMG "How would you know that?"
    if getAffection("GTS") > 4:
        MC "Well, from what I've seen, she's pretty domestic, and knows how to grow food... "
        FMG "Domestic doesn't exactly mean she's a good cook."
    else:
        MC "I don't know, She has a green thumb, so she might be good at cooking, I guess."
        FMG "I would prefer not to have this be based on some basic knowledge, Kei-kun."
    MC "Look, let's just ask her, okay?"
    FMG "Fine, not like we have a lot of options. "
    "With that discussion out of the way, we headed towards Naomi."
    show FMG neutral at Position(xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    show GTS neutral at Position(xpos=0.75) with dissolve
    MC "Hey Yamazaki-san, how's it going?"
    GTS "Oh, hello there Hotsure-san, Mizutani-san. I'm doing well, though I'm currently in need of partners."
    MC "Well, we need a third person, would you like to join us?"
    GTS "Thank you, I'd be glad to. Is there anything you two have in mind to cook?"
    MC "Not... really. We were more looking for help in the actual cooking because..."
    FMG "I can't cook. Just plain can't. I can't even cook cereal right, I'm that bad."
    GTS "I... see."
    show GTS sad
    GTS "As for me, I am sorry to say but I am not very good either."
    MC "...Oh."
    $setAffection("FMG", -2)
    show FMG angry
    FMG "So much your 'feeling', dude. Now what, genius?"
    MC "Ummm... Do you guys think we can make ramen?"
    show GTS neutral
    GTS "Well, I suppose it would not hurt to try."
    show FMG neutral
    FMG "Yeah, I'll try, hopefully I don't burn it."
    scene black with fade
    "We took our positions after that, Naomi took care of the noodles, Akira was in charge of the broth, and I was handling the extra bits..."
    "... and somehow we messed up. The noodles were undercooked, the extra toppings like mushrooms and green onions were less than the recommended amount because others had the same ramen idea, and the broth was low and tasted burnt somehow."
    scene Cooking Classroom with fade
    show FMG neutral at Position(xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    show GTS neutral at Position(xpos=0.75) with dissolve
    FMG "... Well, this turned out better than I thought."
    show GTS sad
    GTS "Again, I am sorry for my lack of experience cooking. I... never had to cook at home."
    show FMG angry
    FMG "... Don't worry about this, I don't blame *you*."
    MCT "I get the feeling Akira is upset with me... though I guess I did made a decision based on a feeling."
    jump daymenu

label FMG018_c1_3:
    MC "Hmm, I wonder if Honoka cooks?"
    FMG "How would I know? For all I know she could eat and drink nothing but milk products."
    MC "Still, it can't hurt to ask her."
    FMG "I guess, she doesn't really look like a chef to me, though."
    "We walked towards Honoka, who was staring at a block of cheese."
    show FMG neutral at Position(xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    show BE neutral at Position(xpos=0.75) with dissolve
    MC "Hey Honoka, Akira and I need a third partner, are you open?"
    BE "Oh yeah! I could join up with ya, Kei-chan."
    FMG "Sweet, but do you have any cooking experience?"
    BE "Ah, I've made instant ramen before. Oh, and those 'make your own candy' kits you can find sometimes."
    FMG "That's better than what I can do, I can't even cook cereal right."
    BE "Uh. But you don't... cook... okay!"
    MC "Okay, do you guys have any ideas on what we can make?"
    FMG "Nope."
    BE "Something neat, but simple maybe. What about a pie?"
    FMG "I don't got any issue with it, pie sounds good."
    MC "Alright, we should have enough ingredients for apple pie. I'll take care of the crust, Honoka can make the filling, and Akira can get the ingredients in order."
    FMG "Fine by me! Be back in five minutes."
    scene black with fade
    "After she got what we needed, we put together a pie and cooked it for 45 minutes..."
    "...But the end result left much to be desired."
    scene Cooking Classroom with fade
    show FMG sad at Position(xpos=0.25, yalign=1.0), Transform(xzoom=-1) with dissolve
    show BE sad at Position(xpos=0.75) with dissolve
    FMG "... Uh, I don't think it's supposed to look so... undercooked, I get the feeling we didn't use the right centigrade."
    MC "Maybe you're right, Honoka what recipe were you following anyways?"
    show BE happy
    BE "..."
    MC "... You were following a recipe... right?"
    show BE neutral
    BE "Sure. I mean. Technically it's a recipe. I found it online and looked good. It's just the instructions weren't in Japanese."
    show FMG surprised
    FMG "T-Then what language was it?!"
    show BE happy
    BE "I think French? It looked the yummiest!"
    MC "... French? You can read French?"
    BE "Yeah, I had it as an elective!"
    MC "Did you pass?"
    show BE neutral
    BE "...Well, no, but..."
    BE "Look. It had all the measurements for the ingredients, easy to read. Maybe we just didn't add them in the right order."
    $setAffection("FMG", 1)
    show FMG neutral
    FMG "You know what, at least we actually made something. It could have come out worse than this."
    MC "You have a point, Akira. Honoka, thank you for planning things out."
    FMG "Yeah, you've been a big help."
    BE "Hey, well, thanks for letting me help. Okay, so who else wants a slice?"
    FMG "... Uh... I guess?"
    "Akira grabbed a slice, she took a bite and..."
    show FMG sad
    FMG "... I don't know how, but it tastes like two day old apple slice pancakes..."
    show BE sad
    BE "Where are you getting that from? I think it's like cold mac and cheese, even though it's only been out of the oven for a little bit..."
    MC "It tastes more like ramen noodles boiled in orange soda."
    "And yet somehow, we got a C+ for our strange pie... at least Akira was happy about it."
    jump daymenu

label FMG019:
    $setProgress("FMG", "FMG021")
    scene Dorm Exterior with fade
    play music Rain
    "After a long day of classes, I realized that during that day I couldn’t find any sign of Akira. My first thought was that she was locked in her room again, so I went to check it out."
    play sound Knock
    pause 1
    MC "Hello?"
    "The response was what I could only describe as swearing in another language. Judging from the language, I could at least tell Chibuki was home. A minute later, the door opened with a tired-looking Chibuki wearing a shirt that looked three sizes too large standing in front of me."
    show Chibuki neutral with dissolve
    Chibuki "Oh… hey Keisuke."
    MC "Umm, hey. Did I wake you up?"
    Chibuki "Yeah… I was napping… something up?"
    MC "Is Akira here? I thought she was stuck in the room."
    "Chibuki gave me a look of a mix between confusion and irritation before sighing. She took a moment to leaned her head out of the door to look around the room."
    Chibuki "Yo! Akira! You stuck?"
    "No response. She turned her attention back at me."
    Chibuki "Yep, nah, pretty sure she's not stuck. If she’s not here she’s probably at her thinking spot."
    MC "Thinking spot?"
    Chibuki "Yeah, it’s the rooftop on the athletics building, normally you’ll find her there if she’s not working out."
    MC "Got it. Thanks for letting me know."
    Chibuki "No problem… later, I guess."
    "As Chibuki closed the door, I turned around and set off towards the Athletics Building… which in hindsight I should have checked anyways."
    
    scene Gym with fade
    "I made my way to the back and looked around to find a door that would lead to the rooftop. After finding an easy entrance, I entered without issue, regardless of signs nearby letting me know that I was entering a restricted area, and climbed up to the roof."

    scene Roof with fade
    "As I opened the doorway, A warm wind pushed my hair aside as I sputtered to keep the strands out of my mouth. It only took me a second to find my target."
    "Laying on the ground with a popsicle stick sticking out of her mouth. Akira turned her head to see who was walking towards her. She held up an errant peace sign, her large biceps bulging slightly as she did."
    show FMG neutral with dissolve
    FMG "Yo, Kei-Kun."
    MC "Hey, I was wondering where you been, and here I find you catching some rays."
    FMG "Heh. Yeah, been here since after class."
    MC "So, what are you doing up here?"
    FMG "Thinking."
    MC "Oh yeah? What are you thinking about?"
    FMG "Stuff."
    MC "…What kind of stuff?"
    FMG "Meh, life stuff, I guess. Right now I just want to get school life behind me."
    MC "Why is that?"
    FMG "I guess I’m just a little tired mentality. What with not only classes but how there’s gonna be like, a lot of big and tall students,"
    FMG "Myself included, hopefully."
    MC "Heh, for what it’s worth I think you’re pretty big, or at least have a big personality."
    MC "Speaking of, classes been good?"
    FMG "Well, as good as they could be. To be honest I never liked school, besides P.E. that is."
    FMG "I get why it’s important, it’s to help build up the path to our future and what we are going to be..."
    FMG "...But for the life of me, I can’t think about what I want to do after I graduate."
    MC "You mean job-wise? Have you thought about going to a university afterward?"
    FMG "I mean, yeah, but that’s not the problem."
    FMG "The problem is... well, can I be completely honest with you?"
    MC "Sure, go right ahead."
    FMG "As much as I enjoy becoming strong and muscular… it limits what I can and can’t do."
    MC "What you don’t want to become a bodybuilder or an athlete?"
    FMG "Maybe, but…"
    "Akira had sat up, cracking her back in the process. The series of pops and cracks were lauder then one would think. Once done she rested her head on her hand, looking out in the setting sun."
    FMG "I dunno, I guess I just want more options in my life. That's not the only thing I’ve been thinking about, though."
    FMG "I’ve been wondering if destiny actually exists."
    MC "Huh, any reason?"
    FMG "I mean, look at me, I’ve always wanted to become strong, but what were the chances that my growth factor is becoming stronger."
    "Honestly, quite slim looking back on it."
    FMG "If destiny has been leading me on a path… then it’s sure has been a crappy path."
    MC "Huh?"
    FMG "I- I mean that I should decide on what I should do. Not some mystical force."
    MC "Well, I don't know about stuff like destiny, what I do know is that only you can choose to follow the path life has given you, or you can make your own."
    FMG "True that. Thanks, Kei-Kun."
    "Akira smiled, she turned her head back into the direction of the sunset, in all its glory."
    FMG "I love this spot, it has such a great view of the sunset."
    FMG "But I think it’s better with friends."
    $setAffection("FMG", 1)
    "I only smiled as I sat down next to Akira, we spend the next 20 minutes in silence as the sunset on that beautiful day."
    jump daymenu

label FMG021:
    $setProgress("FMG", "FMG022")
    play music Busy
    scene Library with fade
    "Well, I should probably get to that report before it’s due. What I didn't expect at the library was a bored Akira and An angry Shiori...at the same table."
    show FMG sad at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show AE neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    FMG "Ugh...Matsumoto-san...I’m SO bored…"
    AE "If I'm not mistaken, it was YOU who decided on this topic, and I already spent valuable time researching this for your sake."
    show AE angry
    AE "So pay attention!"
    FMG "Awww ... what are we doing again I forgot…"
    AE "You-gch-you asked me to be here so you-!"
    show AE embarrassed
    AE "Ghn...you know what? Never mind. We’ll go over the first portion AGAIN."
    show FMG neutral
    FMG "Alright, I’ll start so it’s fair. The great emu war…"
    show FMG sad #flustered
    FMG "Wait...this actually happened? I thought it was a movie."
    show AE neutral
    AE "I...I’ll admit, I had to double-check the legitimacy of this event as well."
    FMG "According to this book, it happened in the ’30s in the down under, so they had bombs and Light Machine Guns...so how hard is it to kill a bunch of stupid emus?! And why does the library even have this book, to begin with?!"
    AE "It was less about their equipment, and more about the failure of their tactics when faced with the natural defenses of the birds. Meanwhile, the book was donated by an Australian philanthropist around the time the library was built."
    AE "As for why THIS particular topic...let’s just say, serendipity. It’s quite a coincidence that you have the exact book for this extremely specific event…"
    AE "...When did you decide on the topic, again?"
    FMG "...I thought it was based on that movie starring Jack Belinski where he fights zombie emus at a gas station..."
    show AE embarrassed
    AE "I don’t...I don’t know who that is. Is-is he…? Is that a real thing?"
    FMG "B-blame my roommate! She watches cult classic movies when she’s not painting or something!"
    show AE neutral
    AE "Hm...I sincerely hope she isn’t disturbing your studies."
    "Jeez...this might be the most non-hostile conversation these two have ever had… Well, I got nothing better to do, so I might as well join in on this."
    MC "Hey guys, what are you working on?"
    show FMG neutral
    FMG "Oh hey… yeah about that...Shiori will answer that."
    AE "Well, I’ve noticed that out of all of the class, Mizutani-san was holding back the most about her topic for next week's World History report. I’d offered to help, and she obliged with...whatever topic this is."
    FMG "… Wait this is for world history? When did that happen?"
    show AE embarrassed
    AE "Clearly, It’s not going well."
    MC "Oh, well I’m not really doing anything, I can help if you want."
    show FMG happy
    FMG "Aww sweet, thanks, man! Now read this book, fair warning someone-who was totally not me out of boredom-drew weiners on page 13. "
    MC "Umm...Thanks?"
    show AE angry
    AE "WHAT?!"
    FMG "You can’t check if my handwriting matches the drawings, so you can’t prove it!"
    AE "The only proof I need in this instance your own confession of guilt!"
    MCT "This is less than good. If this continues, Matsumoto-san might figure out I was the one who drew dicks on page 20."
    MC "U-um, hey, so you need help, eh? I actually read that book a while ago on...Daichi’s behalf."
    AE "-and furthermore-!"
    show AE neutral
    AE "Wait, Utagashi-san? For...what reason?"
    MC "Because the school is being controlled by Emus, apparently… though in hindsight he might have just wanted to distract me."
    AE "..."
    show FMG neutral
    FMG "Huh, guess that explains who drew dicks in page 20 and 25 before, Daichi must have done that."
    MCT "25 TO?! Wait, no, that one wasn’t me!"
    MC "A-anyways, what do you want to know about-"
    show AE sad
    AE "That book was a relic from the beginning of the library."
    MC "ABOUT THE EMU WARS?"
    FMG "… Wait, Shiori when is this due exactly?"
    show AE angry
    AE "TOMORROW."
    MCT "Shit, tomorrow?! I’m only halfway done."
    show FMG sad #flustered
    FMG "...Then why did you say next week!?"
    show AE happy
    AE "I indeed did say next week!"
    show AE angry
    AE "LAST WEEK!"
    show FMG angry
    FMG "THAT’S JUST CONFUSING!"
    "The two bickered a bit about scheduling and the confounding nature of time for a good while before I spoke up to break the madness."
    MC "Hey, girls, um, you know that every minute you’re not working is a minute Akira will lose, right?"
    show AE neutral
    AE "...Haan, you’re right Hotsure-san. Mizutani-san, if we lament the time lost we will lose more to lament."
    show FMG neutral
    FMG "I don’t know how a lamp has to do with my report, but maybe we should just shut up and get back to the report."
    show AE embarrassed
    AE "L-lamp? I...That’s fine too."

    scene black with fade
    stop music
    "The next day..."

    scene Classroom with fade
    play music Schoolday
    show FMG happy with dissolve
    FMG "...And then! As the Americans ran across the great desert in their 1969 Brimstone muscle cars, they shot down the great emu mech robot thing piloted by sergeant general lieutenant Emmet Mel and he died in the explosion! Killing all the emus in the process! And so, the city of New Zealand, Australia was renamed to Melbourne! And then everyone ate emu burgers!"
    FMG "And that’s how the great emu war happened!"
    hide FMG with dissolve
    show AE neutral with dissolve
    AE "..."
    MC "..."
    MCT "........."
    AE "Hotsure-san?"
    MC "Y-yeah?"
    AE "Not only did yesterday did not happen, but the whole report never happened as well."
    MC "A-ah."
    hide AE with dissolve
    show HR neutral with dissolve
    HR "Alright, thank you, Mizutani-san for your...enlightening report."
    
    scene Classroom with fade
    show FMG happy at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show AE neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    FMG "Guys guess what! I got an A+ on my report!"
    AE "What report? I never-wait, what?!"
    FMG "Oh don’t worry Shiori, I told Tashi all about how you and Kei helped me-"
    MCT "Please for the love of god keep my name out of that trainwreck."
    FMG "I even took this picture to remember it by and gave him a copy!"
    MCT "Still though, I can’t believe what just happened."
    
    scene Classroom with fade
    show HR neutral with dissolve
    HR "Hotsure-san, did you actually help Mizutani-san?"
    MC "You know what, there was not only nothing I could do, but I felt like impeding the trainwreck would have just made me a casualty."
    HR "Well, regardless, I’d think she’d have SOME knowledge on her own topic."
    HR "The emu war was in 1932 by Major G.P.W. Meredith, not 'Emmet Mel'."
    MCT "...Huh?"
    HR "I figured Matsumoto-chan gave up at some point, but I’d think you’d know better to just find facts on the internet."
    MC "We, uh, used the book in the library."
    MCT "'Used' being in massive quotations."
    HR "Oh, yeah. The old one? Christ, I don’t think anyone picked that up since I was a student."
    MC "..."
    MC "You drew dicks on page 25, didn’t you?"
    HR "..."
    MC "..."
    HR "...So, I think that with all the work she’s put in, Mizutani-san earned an A, wouldn’t you agree?"
    MC "O-OY, OY! What was that?!"
    HR "Okay, look, my old librarian forgave, Matsumoto-chan, however will NOT; and quite frankly I haven’t had my coffee this morning. Dealing with her will give me an aneurysm, so I’m willing to give Mizutani-san any grade she wants."
    "And that’s how Shiori-san and Mizutani-san got the same grade in our world history report."
    jump daymenu

label FMGBBW001:
    scene black with fade
    "..."
    RM "Hey, wake up!"
    MC "Wah?" 
    scene Library with fade
    show RM angry with dissolve
    play music RM
    MC "...Oh right... library archives. Why am I here again?"
    RM "For the fifth time, I need you to keep watch while I'm going over these documents, and you can't when you keep falling asleep!"
    MC "What did you expect, you made me get up at three in the morning; I only got like six hours of sleep, what time is it anyways?"
    RM "Around six in the morning."
    MC "Oh I'm sorry, six hours and 36 minutes, in between the times you keep waking me up."
    show RM neutral
    RM "Sarcasm is the lowest form of wit."
    MC "Oh, thank you for that piece of information, I'll be sure to put it in the file cabinet I keep under my bed next to those papers of yours."
    RM "Look, is it too much to- Ah!"
    "Daichi stopped himself as he grabbed an old but intact file."
    MC "Alright I'll bite, what is it?"
    show RM happy
    RM "Something that maybe lead to a breakthrough. Give me a minute to read it."
    show RM neutral
    RM "Alright, so most of these articles are dead ends, but this particular article is about the first record of growth. Apparently it was a female around her teens. Name: Chie Kazomazumi."
    RM "She was about as average as average can be. However around her sixteen birthday her breasts started to enlarge to an extreme size around in the 1970's."
    MCT "Huh, he might actually have found something worth a damn, assuming it's legit."
    show RM smug
    RM "This is a great lead. I need to follow up on it."
    MC "Hey, congrats man..."
    MC "...So can I go back to bed now?"
    show RM neutral
    RM "Fine, fine, I guess we earned a rest."
    "With that, we started to walk out, Daichi wanted to make sure we could see anyone come in, so we left the door a crack open."
    MCT "Wait... is the library open at this time? If not how did he... ah screw it, I'm too tired for this."
    "However, due to the door already slightly opened, we saw though the crack that there was someone facing away from the door and looking at the stairwell. Before I could check who it was, Daichi grabbed me, forcing me to crouch down with him."
    show RM angry
    RM "Keep it down, who is that?!"
    MC "How should I know!?"
    RM "Well go check, I made you watch, else what am I paying you for?!"
    MC "I'm not being paid jack!"
    show RM smug
    RM "Not with that attitude you aren't. Now go check!"
    MC "Ugh, fine."
    "Reluctantly, I sneaked towards the door, to my surprise..."
    scene Hallway with fade
    show FMG neutral with dissolve
    MC "It's Akira Mizutani, she's in the hallway near the stairway."
    hide FMG with dissolve
    show RM angry with dissolve
    RM "Why is she here?! It's around 6, and I've never seen her awake earlier than five minutes before class starts at the most."
    MC "How should I know, I wouldn't be here if- wait... I think I see someone coming down the stairs."
    RM "Oh god, move over!"
    hide RM with dissolve
    "Daichi moved to the side to get a look for himself. To both of our surprise the person who was coming down the stairs..."
    show FMG neutral at Position(xpos=0.20), Transform(xzoom=-1) with dissolve
    show BBW neutral at Position(xpos=0.75) with dissolve
    RM "Alice Nikumaru? She's without the assistance of miss Kodama. That alone raises more red flags."
    MC "Be quiet, I think they're about to talk..."
    BBW "Alright Mizutani, what was so important that you had me wake up so early?"
    FMG "Hey Alice, the reason I wanted to talk to you..."
    show FMG sad
    FMG "I wanna get to know you better!"
    show BBW surprised
    BBW "Um...sorry?"
    FMG "I know we don't really see eye to eye, but I generally want to get along with you."
    show BBW neutral
    BBW "Well, I appreciate the desire. However, I fail to see much common ground between us."
    FMG "That's the thing, you don't know. I really wanna give this a chance."
    show BBW sad
    BBW "...I'm still not seeing-"
    show FMG neutral
    FMG "Tell you what, do you know Kazomazumi Bakery on Genki street?"
    show BBW neutral
    BBW "I do. Why?"
    FMG "If you're willing to get to know each other, I'll treat you to some cupcakes there."
    show BBW happy
    BBW "This does sound like it could be beneficial. I accept your invitation."
    show FMG happy
    FMG "Great! How does twelve sound?"
    show BBW haughty
    BBW "Well, they're rather small, I'd want a half-dozen at least, so that would-"
    show FMG surprised
    FMG "Wha? No, I mean twelve o'clock."
    show BBW surprised
    BBW "O-Oh um... *ahem*."
    show BBW neutral
    BBW "T-That is customarily during my study time, but I can fit you into my schedule. Until then, I bid you adieu."
    show FMG happy
    FMG "Sweet, see you then."
    hide FMG with dissolve
    hide BBW with dissolve
    "Once both of them were done, they went their own ways."
    MC "Huh, that‘s something."
    show RM neutral with dissolve
    RM "I'm sure you noticed something wrong with that conversation right?"
    MC "... Kazomazumi Bakery."
    show RM angry
    RM "EXACTLY! Why would those two meet up at that specific bakery, that shares the same name in the article of the first record growth I found on the same day!?"
    MC "... I-it might be a coincidence that they share the same name?"
    show RM neutral
    RM "... Well, how many Kazomazumi's do you know?"
    MC "..."
    MC "Alright fine! It sounds kinda weird."
    show RM angry
    RM "See! There's something going on, I think we should go to this meeting spot and witness what might be a breakthrough!"
    "Normally, I would have thought about this... but it was a too big of a coincidence to pass up."
    MC "Alright, let's go."
    show RM neutral
    RM "Alright, but first take this."
    "He handed me a baseball hat before putting one on himself."
    RM "We don't want those two to catch us spying on them."
    MC "W-Why do you even have these in the first place?"
    RM "You can never be too careful. Now then..."
    show RM smug
    RM "Operation 'stakeout at the bakeout' starts now!"
    scene Town with fade
    play music Sunset
    "A few hours later, we arrived at the town with five minutes till the meeting. We peeked around to see the bakery in question."
    MC "Is that the place?"
    show RM neutral with dissolve
    RM "This is the only bakery on Genki street, and the next closest bakery is nine blocks away on Enoshima Ave."
    MC "Hey, why are we hiding behind a pole?"
    "...I forgot to mention we were peeking around a telephone pole."
    RM "Do you see an open alley with a good view of the front?"
    MC "...Fair point."
    RM "All right, we got five minutes before the meeting time, let's head in!"
    scene Cafe with fade
    show RM neutral with dissolve
    "We entered the bakery, a small but cozy establishment with a caramel-brown and cream-white decorative theme. It only had five tables and a counter with stools for seating. The store was mostly empty, given the time; The only person I could see was the counter girl."
    "The girl looked to be in her late twenties, mid-cut curly dark hazel hair, bright brown eyes, and slightly chubby with big breasts, maybe an E-cup. She wore a caramel-brown and cream-white patterned baker outfit, with an name tag that said “Haruko” pinned to the front."
    Cashier "Hi, welcome to Kazomazumi Bakery! What can I get you two?"
    MC "Yeah hi, this is our first time here, what do you recommend?"
    Cashier "Well, today we have a special on pies, or the cupcakes."
    MC "We'll have the cherry pie please."
    Cashier "Sure, give me a second. So I'm guessing you two are students? The outfit gives it away."
    Cashier "Yeah my mom had a growth thing as well, but I'm not sure if the school was built when she was a teen. Best I know is that it was there when I went there, ten years ago."
    MCT "Huh, didn't know the school was that old."
    Cashier "Anyways, here you guys go."
    "We paid the cashier in advance before we leave, we took the pie, thanked her, and planned our next move."
    MC "So where should we sit?"
    RM "Hmm, we cannot risk them walking past us, that will give away our position."
    RM "We'll sit at the edge of the counter on the stools. The lights are dim enough so at a distance they can't tell us apart from any other students, plus it's in the middle of the building."
    "Once we finished talking about it, we took our seats on the middle stools and waited for the girls to come. I tucked my hair into my collar so as to not give myself away, though I left my bangs out to hide my face."
    MC "Hey, maybe you can ask the owners about this place?"
    show RM angry
    RM "Are you nuts!? I'm not going to show my hand right away! I'll keep coming as a regular, and calmly ask one or two questions, at the most, by the third visit."
    MC "Well, I'm just saying it wouldn't hu-"
    #*Door chime*
    RM "Zip it."
    hide RM with dissolve
    show FMG neutral at Position(xpos=0.20), Transform(xzoom=-1) with dissolve
    show BBW neutral at Position(xpos=0.75) with dissolve
    "Both Akira and Alice entered the building. They were a few feet away from us but enough to not recognize us."
    Cashier "Oh hi, is it just you two?"
    FMG "Yes ma'am, just me and my friend."
    Cashier "Well, what would you two students like?"
    FMG "Let's see, we'll have a box of cupcakes, please."
    BBW "I'll have coffee. Cream and sugar."
    FMG "Yeah, me too."
    BBW "Oh? You take your coffee sweet as well?"
    FMG "Sure, so long as it's not that water downed sludge the school cafeteria serves that is."
    show BBW happy
    BBW "I couldn't have said it better. Is it too much to ask for a nice cup of coffee to start the day off? With the budget the school has, you would think they could put some aside for an espresso machine."
    FMG "Wouldn't be surprised, their chefs aren't exactly winning any awards for niceness."
    BBW "That is the truth. It's nice to meet someone who gets it, Mizutani-san."
    FMG "Yeah, but you can just call me Akira, no need for formalities."
    show BBW neutral
    BBW "Very well, now shall we take a seat?"
    "They got their food and sat at the table behind us. Once there, Daichi did a zipping motion around his lips and slumped farther into the table; I followed suit and we listened in while pretending to read the menus."
    BBW "All right Akira, how are we doing this?"
    FMG "I ask a question, and you ask a question."
    BBW "Seems almost like a game. Very well. You brought me here, you may begin."
    FMG "First, what's your last name?"
    BBW "Nikumaru. For my question: how long have you not remembered my last name?"
    FMG "Um... since the beginning of school. I'm sorry it's just for the life of me I couldn't remember your last name."
    BBW "It's fine. I prefer going by my first name anyway."
    FMG "Right, my next question is, have you ever gone to America?"
    BBW "Yes. My mother is from there and I did most of my schooling there."
    FMG "That's cool!"
    BBW "Indeed. Where do you see yourself in five years?"
    FMG "I dunno."
    show BBW surprised
    BBW "..."
    BBW "T-that's it? You don't know?"
    FMG "Well, how can any of us expect how the future will turn out? I like, think about the future as much as the next girl, but you gotta put in some room for the unknown."
    show BBW neutral
    BBW "I can understand that rationale, but leaving so much to chance..."
    "Alice shook her head, flummoxed."
    FMG "Now for this next question, I want you to be honest."
    FMG "Is it true that Americans deep fry soda and junk food?"
    BBW "Wha-? Where did you hear that?"
    FMG "The Internet."
    show BBW sad
    BBW "...Just to be clear, I do not partake of that kind of food. But yes, some places deep fry soda, Tronkos, chocolate bars..."
    FMG "Huh. No offense, but Americans seem kinda weird."
    show BBW neutral
    BBW "It is a large country and there are many... eccentrics on the fringes."
    "I heard Akira sipping her coffee as she processed the idea of deep-fried candy."
    FMG "Man, the coffee is a hell a lot better here than the school."
    BBW "Mmm, yes. Not my preferred choice, but it's one of the more palatable substitute brands I've had since coming here."
    BBW "Now, why did you pick cupcakes?"
    "Akira put downed the cupcake she was eating and looked down at it before answering."
    FMG "Whenever I was really down, my mom would always bake cupcakes. She would always do it all by hand, and it made it that much more tasty."
    FMG "Even now, I always go eat a cupcake when I'm sad; I do it to remind myself that whenever something bad happens, there will always be something to make life a little bit sweet."
    BBW "I had you pegged as the brash tomboy who didn't have a care."
    BBW "What do you have to be sad about, if it is not too personal?"
    FMG "Sorry, I couldn't tell you, besides it's my turn."
    FMG "Why did you agree to come join me?"
    show BBW sad
    BBW "I came to see..."
    show BBW happy
    extend " If you were a fellow connoisseur of cupcakes."
    "It seemed like she wanted to say something else at first, but Akira didn't seem to notice."
    FMG "Heh, yeah I am."
    FMG "Oh, it's almost 12:30, we should probably get going."
    show BBW neutral
    BBW "You go on ahead. I'll handle the check."
    show FMG surprised
    FMG "What? But I-"
    show BBW happy
    BBW "Please, this is nothing to me. Consider it a show of my enjoyment of this get-together."
    show FMG happy
    FMG "All right, I hope we can do this again. Later."
    BBW "As do I. Pleasant travels, Mizutani-san."
    hide FMG with dissolve
    show BBW sad
    BBW "*Sigh* You had a potential sale there Nikumaru, until that personal matter cropped up."
    show BBW neutral
    BBW "No way to foresee that, though. Next time, keep the mood light."
    "After talking to herself, she paid the bill and left."
    hide BBW with dissolve
    show RM angry at center with dissolve
    RM "Wait... that's it? We been here for 20 minutes listening to girl talk, and they didn't say a single thing about the article, let alone this stupid bakery!?"
    MC "Huh, maybe it really was just a coincidence."
    show RM sad
    RM "B-but the timing was too perfect! How could-"
    UNKNOWN "Excuse me, but are you students at that academy?"
    MC "Um yes ma'am, we-"
    MCT "HOLY MILK JUGS!"
    "She looked like she was in her 30s, but her aura felt like she was much older. Chestnut hair formed in a bun, dark brown eyes, very voluptuous with a bit of a belly, and her boobs... if I had to guess a bra size, I'd say a big triple M at LEAST!"
    "She was dressed about the same as the cashier, but her name tag read Chie."
    Cashier "Mom! Quit bugging the customers!"
    Chie "Oh hush dear, I just wanted to see how fellow growers were handling things."
    MCT "Fellow growers? Does that mean..."
    MC "You must be miss Chie Kazomazumi."
    Chie "Why yes I am, an can I say you two look so cute, especially you mister shaggy hair. I saw all that hair stuffed down your shirt. Is that your factor? You don't need to be ashamed of it."
    show RM neutral:
        ease 2 xpos 0.01
    "While I was talking to her, Daichi was trying to stealthily leave out the front door... too bad everyone could see him. I felt like it was better just to ask and get it over with."
    MC "Look, my roommate is too shy to ask, but are you really the first person to have a growth factor?"
    show RM angry at Transform(xzoom=-1):
        ease 0.5 xpos 0.3
    "Upon hearing me speak, he spun around as if to try and stop me, unfortunately for him he was cut off by Chie."
    Chie "Well, I am the first person to actually be recognized as having tested positive for a growth factor..."
    Chie "...But I'm sure there were others that had growth factors long before I came around. Sorry, but I can't really tell you how it started."
    show RM sad
    Chie "The school wasn't even finished when I got here, the only place that was totally furnished was some of the giant dorms."
    "... If I had to describe Daichi's reaction... it would be pure despair."
    Chie "But hey, it's not like everyone knows about that! Thanks for asking."
    MC "Well, thanks for the pie, we'll be sure to come back."
    Chie "Thanks for coming! You'll always be welcome here!"
    "She gave me a wink before going to the back, her daughter looking like a mix between embarrassed and annoyed for the most part."
    Cashier "Thanks for coming, and I'm sorry about my mom... please come again!"
    scene Town with fade
    show RM neutral with dissolve
    "With that we left the store, and once we were out of sight of the windows I turned to see Daichi looking like he's trying to take things in stride."
    RM "Well, I am disappointed this wasn't the big break I've been searching for, but it gives me an idea of how far this may actually go. Not to mention that last comment she made, about the giant dorms..."
    show RM happy
    RM "Plus, I got some pretty great pie out of it."
    MC "Yeah, I'll see you later."
    hide RM happy with dissolve
    MCT "Well, this was an interesting day..."
    "..."
    MC "Wait... was that lady hitting on me?"
    "..." 
    MC "Nah..."
    jump daymenu

label FMG022:
    "This marks the current end of Akira's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance
