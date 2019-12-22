define AE = Character('Shiori', color="#FF3300")
define FemStudent1 = Character('Female Student 1', color="#ce6950") #New color maybe?
define FemStudent2 = Character('Female Student 2', color="#ce9b50") #New color maybe?
define CMM = Character('Male Council Member', color="#ffa18a") #Lighter Orange
define CMF = Character('Female Council Member', color="#ffa18a") #Lighter Orange
define Ama = Character('Amatsu-san', color="#ffc3b5")
define All = Character('Everyone', color="#ffffff")
define Tako = Character('Tako', color="#ce9b50")

image AE neutral = DynamicImage("Graphics/AE/[globalsize]/neutral.png")
image AE neutral-annoyed = DynamicImage("Graphics/AE/[globalsize]/neutral-annoyed.png")
image AE neutral-eyebrow = DynamicImage("Graphics/AE/[globalsize]/neutral-eyebrow.png")
image AE neutral-noglasses = DynamicImage("Graphics/AE/[globalsize]/neutral-noglasses.png")
image AE neutral-smug = DynamicImage("Graphics/AE/[globalsize]/neutral-smug.png")
image AE happy = DynamicImage("Graphics/AE/[globalsize]/happy.png")
image AE smile = DynamicImage("Graphics/AE/[globalsize]/happy.png")
image AE sad = DynamicImage("Graphics/AE/[globalsize]/sad.png")
image AE sad-2 = DynamicImage("Graphics/AE/[globalsize]/sad-2.png")
image AE frown = DynamicImage("Graphics/AE/[globalsize]/sad.png")
image AE surprised = DynamicImage("Graphics/AE/[globalsize]/surprised.png")
image AE angry = DynamicImage("Graphics/AE/[globalsize]/angry.png")
image AE angry-2 = DynamicImage("Graphics/AE/[globalsize]/angry-2.png")
image AE angry-3 = DynamicImage("Graphics/AE/[globalsize]/angry-3.png")
image AE aroused = DynamicImage("Graphics/AE/[globalsize]/aroused.png")
image AE embarrassed = DynamicImage("Graphics/AE/[globalsize]/embarrassed.png")
image AE aroused-3 = DynamicImage("Graphics/AE/[globalsize]/aroused-3.png")
image AE aroused-4 = DynamicImage("Graphics/AE/[globalsize]/aroused-4.png")
image AE glasses = DynamicImage("Graphics/AE/[globalsize]/unique.png")
image AE glasses-2 = DynamicImage("Graphics/AE/[globalsize]/unique-2.png")

image AE nude-neutral = DynamicImage("Graphics/AE/[globalsize]n/neutral.png")
image AE nude-neutral-annoyed = DynamicImage("Graphics/AE/[globalsize]/neutral-annoyed.png")
image AE nude-neutral-eyebrow = DynamicImage("Graphics/AE/[globalsize]/neutral-eyebrow.png")
image AE nude-neutral-noglasses = DynamicImage("Graphics/AE/[globalsize]/neutral-noglasses.png")
image AE nude-neutral-smug = DynamicImage("Graphics/AE/[globalsize]/neutral-smug.png")
image AE nude-happy = DynamicImage("Graphics/AE/[globalsize]n/happy.png")
image AE nude-smile = DynamicImage("Graphics/AE/[globalsize]/happy.png")
image AE nude-sad = DynamicImage("Graphics/AE/[globalsize]/sad.png")
image AE nude-sad-2 = DynamicImage("Graphics/AE/[globalsize]/sad-2.png")
image AE nude-surprised = DynamicImage("Graphics/AE/[globalsize]/surprised.png")
image AE nude-angry = DynamicImage("Graphics/AE/[globalsize]/angry.png")
image AE nude-angry-2 = DynamicImage("Graphics/AE/[globalsize]/angry-2.png")
image AE nude-angry-3 = DynamicImage("Graphics/AE/[globalsize]/angry-3.png")
image AE nude-aroused = DynamicImage("Graphics/AE/[globalsize]/aroused.png")
image AE nude-embarrassed = DynamicImage("Graphics/AE/[globalsize]n/embarrassed.png")
image AE nude-aroused-3 = DynamicImage("Graphics/AE/[globalsize]/aroused-3.png")
image AE nude-aroused-4 = DynamicImage("Graphics/AE/[globalsize]/aroused-4.png")
image AE nude-glasses = DynamicImage("Graphics/AE/[globalsize]/unique.png")
image AE nude-glasses-2 = DynamicImage("Graphics/AE/[globalsize]/unique-2.png")

image AE dress-neutral = DynamicImage("Graphics/AE/[globalsize]/neutral.png")
image AE dress-neutral-annoyed = DynamicImage("Graphics/AE/[globalsize]/neutral-annoyed.png")
image AE dress-neutral-eyebrow = DynamicImage("Graphics/AE/[globalsize]/neutral-eyebrow.png")
image AE dress-neutral-noglasses = DynamicImage("Graphics/AE/[globalsize]/neutral-noglasses.png")
image AE dress-neutral-smug = DynamicImage("Graphics/AE/[globalsize]/neutral-smug.png")
image AE dress-happy = DynamicImage("Graphics/AE/[globalsize]/happy.png")
image AE dress-smile = DynamicImage("Graphics/AE/[globalsize]/happy.png")
image AE dress-sad = DynamicImage("Graphics/AE/[globalsize]/sad.png")
image AE dress-sad-2 = DynamicImage("Graphics/AE/[globalsize]/sad-2.png")
image AE dress-surprised = DynamicImage("Graphics/AE/[globalsize]/surprised.png")
image AE dress-angry = DynamicImage("Graphics/AE/[globalsize]/angry.png")
image AE dress-angry-2 = DynamicImage("Graphics/AE/[globalsize]/angry-2.png")
image AE dress-angry-3 = DynamicImage("Graphics/AE/[globalsize]/angry-3.png")
image AE dress-aroused = DynamicImage("Graphics/AE/[globalsize]/aroused.png")
image AE dress-embarrassed = DynamicImage("Graphics/AE/[globalsize]/aroused-2.png")
image AE dress-aroused-3 = DynamicImage("Graphics/AE/[globalsize]/aroused-3.png")
image AE dress-aroused-4 = DynamicImage("Graphics/AE/[globalsize]/aroused-4.png")
image AE dress-glasses = DynamicImage("Graphics/AE/[globalsize]/unique.png")
image AE dress-glasses-2 = DynamicImage("Graphics/AE/[globalsize]/unique-2.png")

image Tako neutral = "Graphics/minor/tako-neutral.png"
image Tako surprised = "Graphics/minor/tako-neutral.png"

#image Dorm AE = "Graphics/ui/bg/AEdorm_day.png"
image Dorm AE = "Graphics/ui/bg/NYI.png"
image Student Government = "Graphics/ui/bg/NYI.png"

#MISSING: size1: sad-2, aroused-4
#MISSING: size2: angry-2, angry-3

init 2 python:
    
    #Core
    eventlibrary['AE001'] = {"name": "Hush", "girls": ["AE"], "type": EventTypeEnum.CORE,                                       "location": "library",          "priority": PrioEnum.NONE, "sp": 0,     "next": "AE002", "obsflags": ["size2"],         "conditions": []}
    eventlibrary['AE002'] = {"name": "A Hard Read", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "office",           "priority": PrioEnum.NONE, "sp": 0,     "next": "AE003", "obsflags": ["size2"],         "conditions": []}
    eventlibrary['AE003'] = {"name": "The Lord High Executioner", "girls": ["AE"], "type": EventTypeEnum.CORE,                  "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 0,     "next": "AE004", "obsflags": [],                "conditions": []}
    eventlibrary['AE004'] = {"name": "A Statistically Probable Meeting", "girls": ["AE"], "type": EventTypeEnum.CORE,           "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 0,     "next": "AE006", "obsflags": [],                "conditions": []}
    eventlibrary['AE006'] = {"name": "Opportunity and Networking", "girls": ["AE"], "type": EventTypeEnum.CORE,                 "location": "office",           "priority": PrioEnum.NONE, "sp": 1,     "next": "AE007", "obsflags": [],                "conditions": []}
    eventlibrary['AE007'] = {"name": "The Value of a Minute or Two", "girls": ["AE"], "type": EventTypeEnum.CORE,               "location": "office",           "priority": PrioEnum.NONE, "sp": 1,     "next": "AE008", "obsflags": [],                "conditions": []}
    eventlibrary['AE008'] = {"name": "Striking Up a One Sided Conversation", "girls": ["AE"], "type": EventTypeEnum.CORE,       "location": "office",           "priority": PrioEnum.NONE, "sp": 1,     "next": "AE009", "obsflags": [],                "conditions": []}
    eventlibrary['AE009'] = {"name": "On Your Mind", "girls": ["AE"], "type": EventTypeEnum.CORE,                               "location": "office",           "priority": PrioEnum.NONE, "sp": 1,     "next": "AE011",    "obsflags": [],                "conditions": []}
    eventlibrary['AE011'] = {"name": "Raising the Question", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE012",    "obsflags": [],                "conditions": []}
    eventlibrary['AE012'] = {"name": "Inquiry and Response", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE013", "obsflags": [],                "conditions": []}
    eventlibrary['AE013'] = {"name": "Stickers on Caskets", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE014", "obsflags": [],                "conditions": []}
    eventlibrary['AE014'] = {"name": "The Daily Grind", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE015", "obsflags": [],                "conditions": []}
    eventlibrary['AE015'] = {"name": "Hostage Situation", "girls": ["AE"], "type": EventTypeEnum.CORE,                          "location": "office",           "priority": PrioEnum.NONE, "sp": 3,     "next": "AE016", "obsflags": [],                "conditions": []}
    eventlibrary['AE016'] = {"name": "A Little List", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "library",          "priority": PrioEnum.NONE, "sp": 3,     "next": "AE017", "obsflags": [],                "conditions": []}
    eventlibrary['AE017'] = {"name": "Chopsticks", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "AE018", "obsflags": [],                "conditions": []}
    eventlibrary['AE018'] = {"name": "Miseri Mei", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "AE019", "obsflags": [],                "conditions": []}
    eventlibrary['AE019'] = {"name": "Rondo Alla Turca", "girls": ["AE"], "type": EventTypeEnum.CORE,                           "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 3,     "next": "AE020", "obsflags": [],                "conditions": []}
    eventlibrary['AE020'] = {"name": "Pascha Nostrum", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "classroom",        "priority": PrioEnum.NONE, "sp": 4,     "next": "AE021", "obsflags": [],                "conditions": []}
    eventlibrary['AE021'] = {"name": "Prelude for Choir", "girls": ["AE", "BBW", "PRG"], "type": EventTypeEnum.CORE,            "location": "classroom",        "priority": PrioEnum.NONE, "sp": 4,     "next": "AE022", "obsflags": [],                "conditions": []}
    eventlibrary['AE022'] = {"name": "Casta Diva", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "hallway",          "priority": PrioEnum.NONE, "sp": 4,     "next": "AE023", "obsflags": [],                "conditions": []}
    eventlibrary['AE023'] = {"name": "Sarabande", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "hallway",          "priority": PrioEnum.NONE, "sp": 4,     "next": "AE024", "obsflags": [],                "conditions": []}
    eventlibrary['AE024'] = {"name": "Carmen", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "roof",             "priority": PrioEnum.NONE, "sp": 4,     "next": "AE025", "obsflags": [],                "conditions": []}
    eventlibrary['AE025'] = {"name": "Seasons", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 5,     "next": "AE026", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE026'] = {"name": "The Most Wondrous Dream", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 5,     "next": "AE027", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE027'] = {"name": "Through Thicc or Thin", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "AE028", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE028'] = {"name": "Bolero", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "roof",             "priority": PrioEnum.NONE, "sp": 5,     "next": "AE029", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE029'] = {"name": "Moon in June", "girls": ["AE"], "type": EventTypeEnum.CORE,                               "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 5,     "next": "AE030", "obsflags": [],                "conditions": []}
    eventlibrary['AE030'] = {"name": "Exposure", "girls": ["AE", "BE"], "type": EventTypeEnum.CORE,                             "location": "classroom",        "priority": PrioEnum.NONE, "sp": 6,     "next": "AE031", "obsflags": [],                "conditions": []}
    eventlibrary['AE031'] = {"name": "The Keys to her Heart", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 6,     "next": "AE032", "obsflags": [],                "conditions": []}
    eventlibrary['AE032'] = {"name": "Standardized High Standards", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 6,     "next": "AE033", "obsflags": [],                "conditions": []}
    eventlibrary['AE033'] = {"name": "Your Secret Told on You", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "hallway",          "priority": PrioEnum.NONE, "sp": 6,     "next": "AE034", "obsflags": [],                "conditions": []}
    eventlibrary['AE034'] = {"name": "O Mio Babbino Caro", "girls": ["AE"], "type": EventTypeEnum.CORE,                         "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 6,     "next": "AE035", "obsflags": [],                "conditions": []}
    eventlibrary['AE035'] = {"name": "The Black Box", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 7,     "next": "AE036", "obsflags": [],                "conditions": []}
    eventlibrary['AE036'] = {"name": "Out There", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "schoolfront",      "priority": PrioEnum.NONE, "sp": 7,     "next": "AE037", "obsflags": [],                "conditions": []}
    eventlibrary['AE037'] = {"name": "A Walk Through Town", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "town",             "priority": PrioEnum.NONE, "sp": 7,     "next": "AE038", "obsflags": [],                "conditions": []}
    eventlibrary['AE038'] = {"name": "A Simple Meal", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "town",             "priority": PrioEnum.NONE, "sp": 7,     "next": "AE039", "obsflags": [],                "conditions": []}
    eventlibrary['AE039'] = {"name": "Dawn of Warblade", "girls": ["AE"], "type": EventTypeEnum.CORE,                           "location": "town",             "priority": PrioEnum.NONE, "sp": 7,     "next": "AE040", "obsflags": [],                "conditions": []}
    eventlibrary['AE040'] = {"name": "A Game of Oversized Thrones", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE041", "obsflags": [],                "conditions": []}
    eventlibrary['AE041'] = {"name": "Ambush", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE042", "obsflags": [],                "conditions": []}
    eventlibrary['AE042'] = {"name": "Chaos Reigns", "girls": ["AE"], "type": EventTypeEnum.CORE,                               "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE043", "obsflags": [],                "conditions": []}
    eventlibrary['AE043'] = {"name": "Rainy Skies, Hot Coffee", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE044", "obsflags": [],                "conditions": []}
    eventlibrary['AE044'] = {"name": "From Which The Angel Falls", "girls": ["AE"], "type": EventTypeEnum.CORE,                 "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE045", "obsflags": [],                "conditions": []}
    eventlibrary['AE045'] = {"name": "Let My Prayers Arise", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "clocktower",       "priority": PrioEnum.GIRL, "sp": 9,     "next": "AE046", "obsflags": [],                "conditions": []}
    eventlibrary['AE046'] = {"name": "Perfection in Normality", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "dormAE",           "priority": PrioEnum.NONE, "sp": 9,     "next": "AE047", "obsflags": [],                "conditions": []}
    eventlibrary['AE047'] = {"name": "So Many", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "dormAE",           "priority": PrioEnum.NONE, "sp": 9,     "next": "AE048", "obsflags": [],                "conditions": []}
    eventlibrary['AE048'] = {"name": "Taking it Seriously", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 9,     "next": "AE049", "obsflags": [],                "conditions": []}
    eventlibrary['AE049'] = {"name": "The Wise Thief", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 9,     "next": "AE050", "obsflags": [],                "conditions": []}
    eventlibrary['AE050'] = {"name": "Nights in White Satin", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "dormAE",           "priority": PrioEnum.ALL, "sp": 10,     "next": "AE051", "obsflags": [],                "conditions": []}
    eventlibrary['AE051'] = {"name": "Never Reaching the End", "girls": ["AE"], "type": EventTypeEnum.CORE,                     "location": "dormAE",           "priority": PrioEnum.ALL, "sp": 10,     "next": "AE052", "obsflags": [],                "conditions": []}
    eventlibrary['AE052'] = {"name": "Tristesse", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "library",          "priority": PrioEnum.NONE, "sp": 10,    "next": "AE053", "obsflags": [],                "conditions": []}
    eventlibrary['AE053'] = {"name": "Dressed to Impress", "girls": ["AE", "BBW"], "type": EventTypeEnum.CORE,                  "location": "town",             "priority": PrioEnum.NONE, "sp": 10,    "next": "AE054", "obsflags": [],                "conditions": []}
    eventlibrary['AE054'] = {"name": "Molto Allegro", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 10,    "next": "AE055", "obsflags": [],                "conditions": []}
    eventlibrary['AE055'] = {"name": "Ruhe Sanft", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "hillroad",         "priority": PrioEnum.NONE, "sp": 11,    "next": "AE056", "obsflags": [],                "conditions": []}
    eventlibrary['AE056'] = {"name": "Hymn of the Cherubim", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "classroom",        "priority": PrioEnum.NONE, "sp": 11,    "next": "AE057", "obsflags": [],                "conditions": []}
    eventlibrary['AE057'] = {"name": "Norwegian Dance", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 11,    "next": "AE058", "obsflags": [],                "conditions": []}
    eventlibrary['AE058'] = {"name": "Waltz of the Flowers", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "library",          "priority": PrioEnum.NONE, "sp": 11,    "next": "AE059", "obsflags": [],                "conditions": []}
    eventlibrary['AE059'] = {"name": "Eye to Eye, Face to Face, Heart to Heart", "girls": ["AE"], "type": EventTypeEnum.CORE,   "location": "hallway",          "priority": PrioEnum.NONE, "sp": 11,    "next": "AE060", "obsflags": [],                "conditions": []}
    eventlibrary['AE060'] = {"name": "Csárdás", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "library",          "priority": PrioEnum.NONE, "sp": 12,    "next": "AE061", "obsflags": [],                "conditions": []}
    eventlibrary['AE061'] = {"name": "Shiori End", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 12,    "next": "", "obsflags": [],                     "conditions": []}
    
    #Optional
    eventlibrary['AE005'] = {"name": "Confirmation", "girls": ["AE"], "type": EventTypeEnum.OPTIONALCORE,                       "location": "hallway",          "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],                      "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
     #fixme: it's an office scene, make sure that's handled in split
    eventlibrary['AE010'] = {"name": "Blue Danube", "girls": ["AE"], "type": EventTypeEnum.OPTIONALCORE,                        "location": "office",           "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": ["aftersize2"],                     "conditions": [[ConditionEnum.TIMEFLAG, "size2"], [ConditionEnum.FLAG, "AE006_helpinginoffice"]]}
    
label AE001:
    $setProgress("AE", "AE002")
    scene Library with fade
    "After a long day, I figured that some time in the library would do well for me. I could use somewhere quiet to wind down."
    "Even though a few hours had passed, what Tashi-sensei said was still ringing in my head. I wasn't completely sure how to process what had been going on, but I was worried to say the least."
    "I grabbed a chair, sat down at the table and, resting my head on my hands, I let out a long sigh."
    MC "Well, I never got anywhere by just moping... right?"
    AE "*Ahem*"
    MC "Eh?"
    "I looked over to the table adjacent, where I saw Shiori-san flipping through the pages of a large book."
    play music AE
    show AE angry at center with dissolve
    MC "A-ah! Shiori-san, how are y-"
    AE "Hotsure-san, adjust your volume in the library, please."
    MCT "Oh... right."
    MC "Sorry, Shiori-san."
    show AE neutral
    AE "Hm."
    hide AE with dissolve
    "Shiori looked back down to her book, eyes fixated on the page in front of her. She adjusted her slowly slipping glasses and turned to the next page."
    MCT "Okay, I guess I'll just... sit here."
    "The silence in the room was palpable."
    "It's weird when you think you're alone, but then learn another person is there, and your body just tenses up a bit. Though it may very well have just been Shiori's presence."
    "She was someone who just emanated a strict and commanding aura... but still I felt as though I should at least try to socialize."
    MCT "Should I just move over to her table? Would that be intrusive?"
    "I moved over and sat a seat away from where she was, better to be near and speak softly than far and shout I supposed."
    MC "So... Hey."
    "Shiori looked up from her book, glancing at me with an apathetic gaze."
    show AE neutral at center with dissolve
    AE "...Hello, Hotsure-san."
    MC "How, uh, w-what are you doing?"
    MCT "Uaaah, she's absolutely chilling me to the bone!"
    AE "Researching questions I had that Tashi-Sensei was unable to answer."
    MC "Ah, what about?"
    AE "The nature of the Academy."
    extend " What is going on,"
    extend " how long has this been happening,"
    extend " what preventative measures there are,"
    extend " what school records exist."
    AE "There are so many questions I have, and I plan to make sure they are all answered."
    MC "I see... That book has all that?"
    AE "Clearly not, why would a single book have all of the answers? I'm merely researching the questions that are the most relevant to me at this moment."
    MC "Ah, okay."
    "Shiori looked back down at her book, steadily writing down notes with her other hand."
    "We sat in silence for a few moments, Shiori-san dutifully writing down line after line of notes while I stared up towards the ceiling."
    MCT "I think... there is still a question I have on my mind..."
    menu:
        "How are you taking all this?":
            jump AE001_c1
        "I don't think I have anything left to say.":
            MCT "I... don't really think I do, actually. She's busy. I shouldn't bother her."
            jump AE001_after
        "You're worried, aren't you?":
            jump AE001_c3
            
label AE001_c1:
    MC "So... Shiori-san. How are you handling this?"
    AE "..."
    extend "I suppose... I just need to further my understanding of the situation. That's all. It's unlikely that my situation is anything to worry about, anyway."
    MCT "That... didn't really answer my question."
    jump AE001_after
    
label AE001_c3:
    $setAffection("AE", -1)
    MC "The reason you're in here... you're worried about this whole thing, right?"
    show AE angry
    "Shiori-san stopped writing for a moment and looked up towards me again, with an annoyed look on her face."
    AE "How astute of you to presume my emotions after only a day of meeting me. No. I'm not worried about this, and I think it would be best if you didn't say asinine things so bluntly."
    MC "A-ah! I meant no... I'm sorry."
    "Shiori looked back down at her book, and I felt a chill run down my spine after the talking she gave me."
    MCT "What the hell was I thinking?!"
    show AE neutral
    jump AE001_after
    
label AE001_after:
    "We sat in silence a bit more, until I noticed something... I couldn't hear Shiori writing anymore."
    MCT "Eh? Is she done taking notes already?"
    "I looked over at Shiori, who had stopped writing mid-sentence. Her eyes seemed focused on a particular line, and her mouth opened slightly as she read."
    show AE sad
    AE "What? But... no... That can't be true..."
    MC "S-Shiori-san... Are you okay?"
    AE "Yes, I... I just... I have to go. Pardon me, Hotsure-san."
    "I could do little but stammer as Shiori quickly stood up, her rear tilting the chair back on its hind legs before she turned and walked away."
    "The clack of the front legs against the floor as the chair dropped level made Shiori flinch, but she had regained her composure in an instant and kept on walking."
    hide AE with dissolve
    stop music
    MC "Shiori-san... Hm?"
    "I looked over to where Shiori was sitting, and found that she had forgotten to take her book with her."
    MC "Ah! Her book!"
    MCT "What... Do I do? Should I just take it and bring it back to her?"
    MCT "..."
    MCT "I guess it wouldn't hurt... if I checked it out and brought it back to her tomorrow."
    "I picked up the book and read the title, 'An examination of Cellular Reproduction'."
    MCT "But why would she... I guess it's not too important. I'll just make sure she gets it next time I see her."
    MCT "Well, so much for a relaxing time in the library, eh?"
    jump daymenu

label AE002:
    $setProgress("AE", "AE003")
    scene Hallway with fade
    play music Hallway
    "I walked around the hallways after class looking for Shiori-san, so far having no luck."
    "In class, she wouldn't acknowledge me when I whispered to her, and every time I tried to get close to her, she just got pulled aside by another student."
    Student "-merging the committees into student council. I don't get it either man."
    MC "Yo! Excuse me?"
    Student "Huh? Oh, um, what's up?"
    MC "Are you a member of the student council?"
    "He looked at me with a bit of suspicion before looking down at his jacket and holding his hands up."
    Student "Uh... I mean, I- Yeah?"
    MC "Have you seen the president?"
    Student "Just got out from the first meeting, actually. She's in there."
    "He pointed over candidly at the library door as the last few student council members slipped out."
    MC "Library. Perfect, thanks man."
    Student "Mm."
    "Walking over and opening the large ornate door, I held the book close under my arm."

    scene Library with fade
    "As the wooden door closed behind me, it's loud knock echoed throughout the empty room. The sheer size of the room, as well as the contrasting silence once the echo faded, was a stark reminder of just how large the school was."
    MCT "If I know Shiori-san like I think I do, she'd get mad and tell me to keep quiet if I make too much noise."
    MC "Yo! Anyone in here?!"
    MC "..."
    MCT "No response. She really isn't here."
    MC "Well damn. I guess-"
    MC "Oh!"
    "It was only now that I noticed the door with the sign 'Student Organizations' directly on top of the door frame on the opposite side of the room."
    MC "Yeah, that'd explain it."
    "I saw her through the large window in the wall separating the Library from the room, sitting alone, working on a stack of papers. I walked up to the window and lightly tapped, unsure if I should go in."
    MC "Hey, Shiori-san."
    "Shiori looked up from the paperwork with a bit of confusion. She placed her forms down and walked over to the window."
    MC "Am I interrupting anything?"
    show AE neutral at center with dissolve
    AE "Not at the moment, no. Come in, it would be best for you to not have to raise your voice."
    MCT "In the... empty library?"
    MC "Sure."

    scene Office with fade
    show AE neutral at center with dissolve
    "The inside of the room was larger than it first looked. There were filing cabinets that lined the walls, and a long table in the middle with different chairs for the representatives and student body to discuss the agenda of the day."
    AE "There. Now, what do you need?"
    MC "Oh, uh, yeah. Yesterday in the library, you forgot this."
    show AE neutral-eyebrow
    "I took the book from my bag and put it on the table next to Shiori-san. She looked at it for a moment, and inhaled before looking to me."
    MC "I was wondering if you were wanting it back?"
    show AE neutral
    AE "Thank you, however I have no more need or it."
    MC "Huh?"
    show AE glasses
    AE "I had read all the parts that pertained to what I was looking for, so I figured that there was no point in bringing it back to my dorm."
    MC "Oh, okay... I just kind of figured that you would put it back..."
    AE "Had I put it back or not, it would have inevitably ended up in its original spot when the library closed, yes? It is a common courtesy, however it's not officially required."
    play music AE
    if getSkill("Academics") < 1:
        MC "True... and I checked it out anyway, so no harm no foul!"
        jump AE002_c1_after
    else:
        menu:
            "She's lying, call her out.":
                jump AE002_c1_1
            "She's telling the truth.":
                MC "True... and I checked it out anyway, so no harm no foul!"
                jump AE002_c1_after

label AE002_c1_1:
    $setFlag("AE002_c1_1")
    MC "...Can I level with you on something?"
    show AE neutral
    AE "Go ahead."
    MC "I don't think you're being completely honest with me."
    show AE angry
    AE "That's a bit presumptuous of you to..."
    show AE neutral-annoyed
    AE "..."
    show AE sad
    AE "My apologies. You're right."
    $setAffection("AE", 2)
    show AE aroused-3
    AE "Haah... Well, I saw some upsetting things in there in relation to my own growth. I was admittedly a bit shocked and in my heightened worry I left the book behind."
    MC "Oh, you-... Wow, I didn't expect you to just come out and tell me all of that."
    show AE neutral-annoyed
    AE "You implored honesty, and I gave it to you."
    MC "Well, thank you. That actually means a lot."
    show AE happy
    AE "And it means a lot for you to keep me honest. Thank you."
    jump AE002_c1_after

label AE002_c1_after:
    show AE neutral
    AE "In any case, thank you for being considerate. It's that mindset that helps a school run."
    show AE neutral-smug
    AE "Well, that and capable leadership."
    "Shiori's attitude had definitely gotten better, from what I could tell, but the way she was acting the other day kept nagging at me."
    show AE neutral
    AE "Is there anything else you need?"
    MC "Uh..."
    menu:
        "Are you okay?":
            jump AE002_c2_1
        "I'm fine":
            jump AE002_c2_2

label AE002_c2_1:
    if getFlag("AE002_c1_1"):
        MC "Well, you said that you were upset by what you saw... Are you doing better?"
    else:
        MC "Yeah... Yesterday you seemed really out of it. Are you okay?"
    AE "Of course I am."
    MC "Yeah, I-"
    MCT "Wait, what?"
    MC "Really?"
    show AE neutral-annoyed
    AE "I wouldn't answer that I am if I wasn't. I already had at least somewhat of an inkling of what the school was for, even before the announcement."
    MCT "She did?"
    MC "I kind of thought that-"
    if not getFlag("AE002_c1_1"):
        show AE angry-3
        AE "Well, let's look at your claim. You said I was 'out of it', what do you mean by that?"
        MC "Well... You were more silent than usual. It seemed like you were really distraught."
        show AE neutral-eyebrow
        AE "Than usual? We've only known each other for a small amount of time."
        MC "Ah... Well... True. But I still felt kind of unsure as to why you seemed to act differently than the first time we met."
        AE "Simple. First, I had questions that went unanswered, and as such immersed myself in my studies. I found the answers, and as such I feel alleviated."
        MCT "Well, she did kind of keep to her book..."
        show AE glasses-2
        AE "Second, I was indeed shocked by the initial reveal, however I don't have reason to believe that it should be too much to bear. After all, if this school is indeed for people with unique... growing situations, then I should be able to adapt in well, yes?"
        MC "True... but it doesn't bother you at all?"
        show AE glasses
        AE "Hotsure-san, fate is inescapable. If I will grow, as per what Tashi-sensei says, then it will happen inevitably. Why worry about that which will happen no matter what?"
        MCT "Wait, what? Something... irks me about that statement."
        MC "I guess... you have a point."
    show AE neutral-annoyed
    AE "As class representative, my responsibility is to the school. I don't have the luxury of worrying about these sorts of things when there are more pressing matters at hand."
    MC "...You're right. I was being silly."
    AE "Certainly not. You had a legitimate concern for a fellow student, and you acted accordingly."
    MC "Well... as long as you're doing okay."
    AE "I assure you, Hotsure-san, I am more than capable of handling myself."
    MC "I believe you, Shiori-san."
    AE "Good."
    show AE neutral-eyebrow
    AE "Well then, is that all you need?"
    MC "Yeah, I think that I should be alright."
    AE "Then I will see you in class. Remember, our homework is Chapter 1 section 3. I expect good results."
    MC "Yeah... See you then."
    stop music
    
    scene Library with fade
    "As Shiori got back to her work, I walked out of the door and back through the library. While her talk was meant to calm me down, it only ended up raising more questions."
    jump daymenu

label AE002_c2_2:
    MC "No, I should be alright."
    MCT "It really doesn't matter I guess, she seems alright now."
    AE "Alright then, have a good day."
    MC "Alright, see you later, I guess."
    show AE neutral-eyebrow
    AE "Oh yes, and Hotsure-san?"
    MC "Yeah?"
    show AE neutral-annoyed
    AE "Tuck in your shirt, it doesn't comply with the current dress code."
    MC "Uh... Yeah... I will."
    "Shiori turned back to her paperwork, and I turned out of the door to leave the library, content that I had been able to get the book situation sorted. But that still left the question of what else I could do today."
    jump daymenu
    
label AE003:
    $setProgress("AE", "AE004")
    scene Campus Center with fade
    play music Schoolday
    MCT "C'mon, just a bit farther!"
    "I had spent a good amount of time after class making paper airplanes and throwing them around in the central courtyard, attempting to beat my earlier record by a few precious inches."
    MCT "Almost... there!"
    "The plane soared through the air and made a smooth crisp landing at about four or so feet in front of me."
    MCT "I seriously need to work on my plane making... or at least do something productive instead."
    MC "Hmm?"
    "I heard a bit of squabbling as I got up from the bench I was sitting on and decided to take a tiny peek... Just for studying purposes of course."
    Student1 "Come on! It's just a wrapper!"
    show AE angry at center with dissolve
    AE "I don't care if it's a scrap of paper, it says clearly in your student handbook that there is to be no littering on campus. Period. Do I need to talk to administration about this?"
    Student1 "D-Don't be unreasonable!"
    AE "There is a garbage can right over there. Pick it up and throw it away."
    hide AE with dissolve
    MCT "Wow... I don't want to be on the end of THAT scolding... Wait."
    "I looked behind me to see the legions of failed craft lying on the ground, and I could swear I broke out in a cold sweat."
    MC "Hoooo boy... I need to pick these up quick, lest Shiori-san comes this way."
    "After a short while, I picked up my tiny, oblong aircraft and put them in my bag, ready to head back to my room. The sense of confusion and surprise left in favor for a general feeling of what I can only describe as uneasy acceptance."
    "Shiori's words resonated with me for a small while the more I thought about it, what will happen will happen, all I can really do is accept it."
    MCT "Can she really rebound from the news that quickly? I figured she'd be-"
    show AE neutral-eyebrow at center with dissolve
    AE "Everything all right, Hotsure-san?"
    MC "GAH!"
    "In my shock, I nearly dropped my bag with the planes in tow."
    MC "Oh! Hey, Shiori-san. You scared me. Uh, yeah, I'm all good."
    show AE neutral
    AE "Yes, well, I apologize for frightening you. You seemed distressed about something."
    MC "Oh, no, I'm fine. Thanks though."
    show AE neutral-annoyed
    "There was an air of apprehension as Shiori-san looked on at me in an inquisitive manner; almost judging my every move."
    show AE angry
    AE "Yes, well, if there IS anything you need, don't hesitate to ask."
    MC "Yeah, then... What was our homework again?"
    show AE neutral
    AE "Chapter one, section three, page 16. Read it and answer the questions on the following page."
    MC "Okay, thanks, Shiori-san!"
    AE "Hm."
    hide AE with dissolve
    "I strode off in the opposite direction; breathing a sigh of relief knowing that my paper airplanes didn't win me a thrashing."
    stop music
    scene Hallway with fade
    MCT "Okay, so if Tashi-sensei wants us to do section three by tomorrow, then I can probably finish in about two or so at home, meaning that I can... Eh?"
    "As I reached the corner, I found an unexpected sight. The student from earlier, and his two friends talking somewhat loudly about something."
    "As I got closer, I was able to listen in on just what it was."
    play music Tension
    Student3 "In front of Haruno-chan?"
    Student1 "She wasn't even a few feet away when she did it."
    Student2 "Shit, man, that's embarrassing."
    Student1 "You're telling me! It was just a wrapper, she didn't need to be so uptight about it."
    Student2 "What a bitch."
    Student1 "Right?"
    Student3 "Gonna do anything about it?"
    Student1 "What am I supposed to do?"
    Student2 "Tell her off, let her know that she can't look down on you like that."
    Student1 "To hell with that! Have you seen her? She's small, but goddamn if she isn't scary."
    MCT "Damn, I mean... He's not wrong, but chill."
    Student3 "She needs someone to tell her not to be so anal."
    Student1 "She *needs* to get laid."
    Student2 "Ain't that the truth."
    MC "If you guys are gonna-"
    Student1 "Huh?"
    menu:
        "Stand up for Shiori.":
            jump AE003_c1_1
        "Bail.":
            jump AE003_c1_2

label AE003_c1_1:
    $setFlag("AE003_c1_1")
    MC "If you guys are gonna talk shit about a girl, at least leave their sex life out of it, I mean c'mon."
    Student1 "Eh? The hell's your problem?"
    MC "It ain't cool, is all. I mean, I get it, you're pissed, but you don't gotta bring up banging her. Just cause she can't get any doesn't mean you get to be salty cause you aren't getting any either."
    if getSkill("Athletics") > getSkill("Academics") and getSkill("Athletics") > getSkill("Art"):
        "The biggest of the three seemed to take exception to this, as he walked up to me with his chest puffed up."
        Student3 "What was that, punk?"
        MC "Try it and get laid out."
        Student3 "..."
        "I'm not exactly the strongest, but apparently neither is he, as he felt intimidated enough to back down quickly."
    elif getSkill("Academics") > getSkill("Art"):
        "One of his friends decided to get up and hold the line for him."
        Student2 "Now hold on, what does how much we get laid have to do with anything?!"
        MC "If it doesn't, then why'd he bring it up in the first place?"
        Student2 "A..."
        "Unable to come up with a rebuttal, he shrunk back."
    else:
        Student1 "He called me out in front of my girl, man. That's going too far."
        MC "Look, I get where you're coming from, I really do, but are you really a guy who'd litter right in front of your girlfriend? Wouldn't you think she'd like it more if you had more class?"
        Student1 "Gch..."
        "Apparently, I hit a sore spot, as he visibly seemed uncomfortable looking at just how well I maintained my uniform even under stress. Simply put, I outclassed him."
    Student1 "Yeah, well... Maybe you're just jealous at the thought of anyone else porkin' her?"
    MC "...What?"
    Student2 "Yeah, what's the matter, you gotta thing for her gross ass or something?"
    MC "I'd kick yours if I didn't care about keeping my shoes shining."
    Student3 "Man, to hell with this guy."
    Student2 "Yeah, I don't got time for this."
    "As the first students friends left, he suddenly found himself with less confidence."
    Student1 "..."
    MC "...You just gonna stare at me? Are you gonna swing? What's happening here?"
    Student1 "...I'll remember this."
    "He finally followed suit after his friends, leaving me victorious, but no less pissed."
    MC "Tch."
    stop music
    jump AE003_c1_after

label AE003_c1_2:
    MCT "Shit, what am I doing? This is not the hill I wanna die on socially."
    stop music
    MC "Hang out in the halls, can you tell me where the bathrooms are?"
    Student1 "Uhh... Like, straight down the hall to the left."
    MC "Thanks man."
    Student1 "No worries."
    jump AE003_c1_after

label AE003_c1_after:
    "Hands in my pockets, I walked down the hall, considering everything they were saying."
    MCT "Needs to get laid? What kind of douche just openly says that in public? I mean... probably wouldn't hurt-"
    MCT "Goddamnit, focus! That's a messed up thing to say about a girl, even if she told you off in front of your lady."
    if not getFlag("AE003_c1_1"):
        Student1 "Yo! I said left!"
    "Continuing right, I exhaled through my nose, just frustrating myself more thinking about it until I got to my room."
    
    scene Dorm Exterior with fade
    play sound Knock
    "*KNOCK* *KNOCK*"
    play music Hallway
    MC "Daichi! C'mon man, open the door."
    RM "Who is it?"
    MC "It's the colonel, I got some recipes to share. Open up."
    RM "You're not the colonel! He would never share his recipes openly!"
    MC "What the fu- Just open the door!"
    MCT "The door opened up, this time more readily than the first few times I entered."
    show RM happy at center with dissolve
    RM "Relax! Relax! Just a joke. C'mon in."
    
    scene black with fade
    pause .5
    scene Dorm Interior with fade
    "I sat at my desk, head resting on my hand as I looked out the window."
    MCT "Shiori-san... Is she really as harsh as that guy was making her out to be? ...No, no she was justified in what she did, he just can't handle getting called out."
    "Sitting up to stretch, I shook off some of the frustration and grabbed my pencil."
    MCT "Well, no point in just dwelling on it, might as well get started on my homework."
    "I pulled out all my materials, pencil, book, empty notebook, eraser..."
    MCT "...Wait... What the?"
    "I looked in my notebook and found nothing. Only a few measly papers sticking out... Airplanes are expensive."
    MCT "Damnit! Now I have to go and get a new one. Guess I'm headed out then."
    jump daymenu
    
label AE004:
    $setProgress("AE", "AE006")
    $setTimeFlag("testday")
    scene Dorm Interior with fade
    play music Rain
    "I slipped my shoes on as my mind began to mull over the incident in the hall the other day, it was strange, but honestly I just felt a bit ticked off about the whole thing." #Splitted the line up in 2 -Auctus
    "Was it because they were bad mouthing someone I knew, was it because it was just blatant disrespect towards someone who seems like they work hard? Either way, I was annoyed enough by the whole thing that I now had a big problem on my hands."
    MCT "I can't believe I forgot to get a new notebook!"
    "The notebook that I had been mulling around with yesterday lay in the bin next to my bed. It was old and used up in the first place, but it didn't help that I used it as a factory for miniature planes."
    MC "Okay, so if I rush, I can get to the store in time to get a new one, get back, and start writing my homework down."
    scene Dorm Exterior with fade
    "I opened the door quickly, and began to head out. If it weren't for my reflexes, I would have ran head first into Shiori-san, hand prepped to knock on the door. I jumped a bit, and took a step back."
    show AE surprised at center with dissolve
    MC "Uwa! S-sorry, Shiori-san! I was just heading out, I didn't mean to startle you."
    "She appeared a bit surprised for a moment, but quickly regained her original posture as she cleared her throat. She slowly put her hand on a large file she was carrying in her other arm."
    show AE neutral-eyebrow
    AE "Yes, well, just be a bit more careful."
    MC "Can do. So, uh, is there anything that you need? Is something wrong?"
    show AE angry
    AE "Very much so. I need to see Utagashi-san. Is he here?"
    MC "Oh, sorry. He left earlier and hasn't come back yet, I have no idea where he went."
    show AE neutral-annoyed
    AE "I see. Well, when you do see him, tell him I would like a word with him. Thank you, that is all."
    "Shiori-san had begun to walk away, but my interest had been piqued. At this point I just had to know."
    MC "Hey, Shiori-san?"
    show AE neutral-eyebrow
    AE "Hm?"
    MC "What exactly... did Daichi do?"
    if getAffection("AE") <= 1:
        show AE neutral-annoyed
        AE "It's a matter between myself and him. There's no need to pry any further."
        menu:
            "C'mon please!":
                $setAffection("AE", -1)
                MC "Really? I mean, I promise I won't tell anyone else, please?"
                show AE angry
                AE "Begging, Hotsure-san? Over something so minor? Pitiful."
                MCT "Yikes! She did NOT find that cute."
                jump AE004_aftertest
            "Ah, okay.":
                MC "Ah! Sorry, I shouldn't pry."
                show AE neutral-annoyed
                AE "Indeed. If you wish to know, ask him later."
                jump AE004_aftertest
            "I feel like it's my right to know.":
                $setAffection("AE", 1)
                MC "Well, with all due respect, I feel as if it's my right to know."
                show AE neutral-eyebrow
                AE "Is that so?"
                MC "Well, I want to make sure that Daichi-san isn't up to no good. I feel like it would benefit the both of us if I knew, right? That way, I could feel safe about this, and be able to keep him in check. He is my roommate after all."
                AE "Hmm."
                "Shiori-san pondered what I said and, after a short moment, spoke with her answer."
                show AE neutral
                AE "...Very well. Here."
                jump AE004_testpass
    else:
        "Shiori-san paused for a moment, before turning to me and holding the file out in her hands."
        AE "I suppose if anyone should know, it should be you. Take a look."
        jump AE004_testpass
        
label AE004_testpass:
    "Shiori handed me the file with both hands and then crossed them across her chest, fingers tapping at her forearms as she awaited my response. What I saw was..."
    MC "Daichi's... student file?"
    show AE neutral-annoyed
    AE "A printed copy, yes, I had planned to transcribe it onto paper for filing; however do you perhaps notice anything strange about it?"
    "I didn't need to look long to see the problems. His height, weight, and appearance seemed to all be described wrong, his record looked like a cheesy spy movie script, and he even put down that he was from a country that seemed nonexistent!"
    MC "Where the hell is Cobrastan?!"
    show AE angry
    AE "Nowhere, clearly."
    MC "Who wrote this?"
    show AE neutral-annoyed
    AE "The student registrar is in charge of obtaining all the information on the students, and everyone I asked seemed to say there were no problems with his profile. I came to... question him."
    MC "Couldn't it be a problem with the registrar then?"
    show AE neutral
    AE "Unlikely. They have a 96%% accuracy rating. A bit lenient, yes, but still effective."
    MCT "So then why... Wait... Did he change what was in his profile last minute?!"
    show AE neutral-eyebrow
    AE "Something wrong?"
    MC "N-no. Just some stupid thoughts."
    show AE angry
    AE "I wouldn't be so sure they were."
    MCT "She thinks so too? ...Wait, how did she-?!"
    show AE neutral-annoyed
    AE "Well then, next time you see him, tell him my concerns and that I wish to see him immediately."
    MC "Can do."
    "Shiori-san took the file back and nestled it between her arm and her hip."
    jump AE004_aftertest

label AE004_aftertest:
    AE "In any case, unless you have any issues to bring up, I have other things to do today."
    MCT "Is there anything I want to bring up to Shiori-san?"
    menu:
        "Nothing I can think of.":
            MC "I should be all right, thank you."
            AE "Very well. Have a good day."
            jump daymenu
        "Bring up yesterday's events.":
            jump AE004_prechoice

label AE004_prechoice:
    MC "Actually... Yeah. I do have something that's been on my mind."
    show AE neutral-eyebrow
    AE "Do tell?"
    MCT "That wasn't right for those guys to just start badmouthing Shiori-san like that after she left. I gotta tell her."
    MC "Yesterday, after you left, I caught a conversation between the group of guys that you had talked to."
    AE "The littering incident? It's been taken care of."
    MC "W-well, yeah, but that's not what I mean."
    MC "Those guys... They said some pretty hurtful things about you."
    AE "..."
    MC "And I was kind of thinking that it wasn't right."
    show AE glasses-2
    AE "...And what did you do about it?"
    MC "Eh? Oh."
    menu:
        "I told them off.":
            jump AE004_c1
        "I didn't say anything.":
            jump AE004_c2
        "I was gonna say something, but didn't.":
            jump AE004_c3

label AE004_c1:
    $setAffection("AE", -2)
    MC "I wasn't just gonna let them get away with it! I stood up for you, and told them off."
    show AE angry
    AE "Nngh."
    "Shiori-san put her hand under her glasses and lightly shook her head."
    show AE glasses-2
    AE "Why would you do that?"
    MC "Eh?"
    AE "You really have no reason to get involved in my personal affairs. I can handle myself. Did you even think about what could have happened?"
    MC "I'm sorry... I was just trying to look out for you."
    show AE neutral-annoyed
    AE "Look out for yourself. The less you meddle, the less work I have to do."
    MCT "Ow... That actually hurt a bit."
    jump AE004_afterchoice

label AE004_c2:
    $setAffection("AE", 2)
    MC "Well, I didn't really say anything. I figured it wouldn't help to complicate things, so I just held my tongue and waited to tell you directly instead of starting unneeded drama. It wouldn't have been professional."
    show AE happy
    AE "...I'm impressed, Hotsure-san. You keep your emotions under check and think things through. That will serve you well. Let's hope you continue this behavior in the future."
    jump AE004_afterchoice

label AE004_c3:
    $setAffection("AE", 1)
    MC "Well... I'm sorry, Shiori-san. I was going to say something, but I... kinda got cold feet and backed off."
    AE "I see. That's okay Hotsure-san. Moments of weakness can be common. Next time, don't even say anything, and things will turn out better."
    MC "I know, I-"
    MCT "Wait... What?"
    AE "I can tell your heart was in the right place, but perhaps leave things to your better judgement, hm?"
    MC "U-uh."
    show AE glasses-2
    AE "The only thing I am worried about is that lack of resolve. If you do something, commit to it. That is all."
    MCT "That turned out... O?!"
    jump AE004_afterchoice

label AE004_afterchoice:
    MC "So...what do you plan to do?"
    show AE neutral
    AE "Nothing."
    MC "?!"
    MC "B-uh."
    show AE glasses
    AE "I'm not going to actively feud with delinquents. Their opinion of me is theirs, nothing more. Unless it turns to harassment among students, I have no plans to take up things such as this with administration."
    MC "I..."
    MCT "It can't be helped. If Shiori-san thinks that's best..."
    MC "Yes, Shiori-san. I understand."
    AE "Have a good day, Hotsure-san."
    MC "You too, Shiori-san."
    AE "Oh, and Hotsure-san?"
    MC "Y-yeah?"
    show AE neutral-annoyed
    AE "If the wind blew your planes would have been everywhere... Keep that in mind next time, and stay near a bin."
    MC "Ngh!"
    MCT "How did she-?!"
    MC "Y-Yes, Shiori-san. I will."
    hide AE
    "I watched Shiori-san as she walked away. She was an interesting one. The way she carried herself was astounding... if not slightly baffling."
    jump daymenu

label AE005:
    $setTimeFlag("aftertest")
    scene Hallway with fade
    "I let out a sigh and rubbed the back of my neck. I don't know why, but I still felt a bit of anxiety after the fact. The raw emotion in the area was overwhelming, there was so much tension from everywhere at once."
    MCT "My hair...? My hair. I mean, it's so..."
    "I looked down at my knuckles. Since puberty, I've had a bit of hair on them. I remember how all the other kids would jeer me for it; being hairy here isn't exactly that common, especially as a teen."
    "*Click*"
    MCT "Hm?"
    "I stopped for a moment, caught off guard by the sound of the door in front of me slowly creaking open. I stood there, silently watching as a girl walked out."
    show AE sad at center with dissolve
    play music AE
    "It was Shiori-san, finally done with her results."
    MC "Shiori-san?"
    AE "N-ng! Hah... *ahem* hello, Hotsure-san."
    MCT "H-her face!"
    "Shiori-san held her head high, but her face and body betrayed her. Her eyes seemed more apprehensive than before. Her face showed a certain embarrassment I'd never seen on her before; her cheeks were puffy, and her face was a slight tinge of crimson."
    "Though her posture was fairly uniform, all the posture the human body can muster couldn't hide her trembling."
    MC "Shiori-san, is everything all right? How did it go?"
    AE "Yes. I... should be all right. I was taken slightly aback by my results..."
    "She gave a deep breath, and though her face still showed a tinge of pink, she appeared to instantly regain her composure."
    show AE neutral
    AE "It's nothing that I hadn't expected, of course. I had a theory on what my situation was, it was just that... having it said to me was a bit more jarring than I would have liked."
    MC "A theory on your type of growth?"
    show AE embarrassed
    AE "Essentially, yes."
    MC "How did you know?"
    AE "...I'd already been experiencing some of the effects before I came here. I realized that they weren't attributed to my lifestyle beforehand, though I had been assuming so for a while, so I began to research what it could possibly be. Once I got the transfer notice from the school, it was all but confirmed."
    MC "I see... I can expect that from someone like you, Shiori-san. But if you had an idea of what was going on, then why was being told jarring?"
    show AE neutral
    AE "Well, having a theory is different from getting a confirmation, and when you're told something like that outright..."
    MC "It's like going to the doctor thinking you have a disease, only to be told that you do."
    AE "Yes, precisely. It's strange, it's as though I had some futile hope in the back of my head that my particular case was less that I was making it out to be, even though it was obvious what it was from the start."
    MCT "I think I know what it was."
    menu:
        "Try and play it off.":
            jump AE005_c1
        "Tell her what you think it is.":
            jump AE005_c2

label AE005_c1:
    MC "Well, uh, ya know, it could be anything. I mean, it's not like-"
    show AE aroused-3
    AE "You're a horrible liar."
    MC "...Eh?"
    AE "It's obvious to anyone what my growth is..."
    MC "Shiori-san... I'm sorry."
    show AE sad
    AE "It's fine. At least you were kind enough to make an attempt... and it's always useful to know your tells when being dishonest. It makes it easier."
    jump AE005_after

label AE005_c2:
    $setAffection("AE", -1)
    MC "It's your butt, isn't it?"
    show AE surprised
    "Shiori-san looked at me with shock. I could tell she didn't expect me to just come out and say it."
    MCT "Why did I say that out loud?! She just told you hearing it was jarring for her."
    show AE aroused-3
    MC "Shiori-san! I didn't mean to just blurt that out, I'm sorry."
    show AE angry-2
    AE "Y-you!"
    show AE aroused-3
    AE "..."
    if getAffection("AE") >= 3:
        show AE sad
        AE "It's all right Hotsure-san, I realize that this is a stressful time for us all... Yes, you're correct. The growth I came to this school for is my... rear."
        "I looked down at Shiori-sans hips. They were already flared out as it was. I've seen butts like hers from American media and stuff like that, but seeing it on a Japanese girl was still so surreal to me."
        MC "I'm sorry. I didn't mean to be so thoughtless."
        show AE neutral-annoyed
        AE "I've already accepted your apology, Hotsure-san."
    else:
        "Shiori-san peeked behind her back at her derriere. Almost sheepishly, she grabbed the bottom of her skirt and pulled it down."
        show AE angry-2
        AE "T-that is on a need to know basis, and I see absolutely no reason why you would need to know."
        MC "Ah! Sorry, Shiori-san."
        AE "Hopefully you have more tact in the future... I'll be keeping an eye on you."
    jump AE005_after

label AE005_after:
    show AE glasses
    AE "However, as you know my growth, I think it only fair for information to be exchanged for research purposes. What is your diagnosis."
    MC "O-oh, um. My hair."
    show AE surprised
    "Shiori-san's eyes lit up for a moment. She looked down at the ground for a second and then back at me, bewilderment strewn across her face."
    show AE angry
    AE "Hair? But why did..."
    MC "S-shiori-san?"
    show AE angry-3
    "Shiori-san bit her knuckle for a moment in contemplation before returning to her regular demeanor."
    show AE neutral
    AE "It's nothing Hotsure-san. Merely thoughts to myself. As we'll both be growing, I assume there will be a level of..."
    show AE neutral-eyebrow
    extend " mutual learning at some level between us."
    MC "Mutual... Huh?"
    show AE neutral
    AE "In any case, I can tell that tonight will be fairly arduous. I'll be filling out forms for the health committee."
    MC "Okay... Yeah, you do that."
    AE "Have a good evening."
    hide AE with dissolve
    stop music
    "Shiori-san walked away toward the library, holding her skirt with one hand from behind her. As I watched her walk away, I started to contemplate what she said."
    MCT "Mutual learning..."
    if getAffection("AE") >= 3:
        MCT "I... look forward to it."
    else:
        MCT "Yeesh, could she get any creepier?"
    jump daymenu

label AE006:
    scene Hallway with fade
    play music Rain
    "The soles of my shoes made a loud, squeaky, and wet patter as I walked down the hall, drenched with the torrential downpour from outside."
    MC "Ugh, why does it always have to rain on days that look sunny in the morning? I'm soaked!"
    "In an attempt to shield myself from the heavy rain, I used the notebook in my right hand. Not exactly my brightest idea."
    MC "Man, the whole thing looks trashed, I just bought this!"
    MCT "I can't believe that it's soaked already. Only a few days with this thing and I've only used it once... Oh god, no."
    "As I opened up the notebook, a mix of shock and utter despair began to sink in, as I realized my Calculus homework was reduced to what could only be described as a Jackson Pollock wet dream."
    MC "Are you kidding me?! I spent hours trying to figure this out!"
    MCT "Dammit! This is bad. This needs to be done by tomorrow! This is the only notebook I have... uh, had, and the store is on the other side of campus. If I run over I-"
    show AE neutral-eyebrow at center with dissolve
    AE "Hotsure-san?"
    MC "AGuaH!"
    MCT "Sh-Shiori-san?"
    "Shiori-san stood with a dark brown umbrella carefully tucked away in a sheath under her arm, her glasses fogged by the moisture."
    MC "A-ah, yeah, hey, hi, Shiori-san. How are you holding up?"
    show AE neutral
    AE "Fine."
    show AE neutral-annoyed
    AE "You, on the other hand, are drenched, and dripping water all over the halls."
    MC "Huh?"
    "I looked down to see the fair-sized puddle forming around my feet. Before looking back up at Shiori-san's piercing gaze."
    MC "Oh! Uh-"
    show AE neutral
    AE "Quite the unfortunate predicament for you, Hotsure-san. But, you're in company with many of your peers, it seems."
    MC "What do you mean?"
    show AE neutral-annoyed
    AE "Well, you aren't the only one to forget your umbrella, I've seen six students with the same problem; Though I will say you're the first to sacrifice your notebook in the process."
    MCT "She... noticed?"
    show AE neutral
    AE "Hopefully you don't treat that hair of yours with more respect than your homework all the time, lest you fall behind in your studies."
    show AE neutral-noglasses
    "Shiori-san took her glasses off and began to rub them with a handkerchief. She slowly walked past me as she did and came to a stop in front of the library, she turned her head and looked at me."
    AE "Though this advice comes late, perhaps you should look at the weather reports a day in advance and plan accordingly."
    MCT "I haven't really got a good look at her eyes before. I'd never really noticed but... they are kinda beautiful."
    MC "Yeah... Well, there are some things that are hard for anyone to plan for."
    AE "How so? I'd easily looked at the local forecast and prepared accordingly for all variables."
    MC "Wind direction and umbrella coverage don't count, then?"
    AE "What?"
    MC "Your skirt."
    show AE surprised
    "Shiori-san looked down at her skirt and saw what I noticed. The back of her skirt was wet. Though she held her umbrella in a way to guard herself from the rain, her rear stuck out far enough for it to get rained on."
    "The damp fabric of her skirt clung to her cheeks, showing the faint outline of her panties. Shiori-san bristled up for a moment before putting on her glasses and adjusting her skirt."
    show AE embarrassed
    AE "I... hadn't taken into account my... changing dimensions."
    show AE aroused-3
    AE "Besides, I would prefer if you kept your wandering eyes to yourself."
    MC "Oh, sorry, Shiori-san!"
    MCT "Now I remember. When we got our reports back, was shown that her butt was getting bigger, right? Man, talk about the short end of the stick... I mean, it was big before, but to think that already freakishly huge butt of hers is only gonna swell..."
    show AE neutral-annoyed
    AE "It's fine, Hotsure-san. Now, if you will, I have paperwork to do."
    MC "Okay. I'm gonna run down to the store."
    AE "Wait, run?"
    show AE angry-2
    MC "Yeah, I mean, I don't wanna get more wet than I'm about to, right?"
    show AE angry-3
    AE "Absolutely not."
    MC "Right, so I'll put this over my head and go get another one, put it under my shirt and-"
    AE "No, I mean you aren't running outside in this rain. You could slip outside and hurt yourself, plus you got lucky by not getting mud all over your shoes, don't test that."
    MC "I don't know what else to do, my notebook is ruined and I need paper to do my homework."
    show AE neutral-eyebrow
    AE "Hmm... Very well. Come with me."
    MC "Huh? Why?"
    show AE neutral
    AE "There is paper in the office room, you can use some of it."
    MC "Really? Awesome, thanks."
    show AE neutral-annoyed
    AE "Just don't make too much of a ruckus."
    "Shiori-san and I walked into the library and over to the door of the office. She pulled out a key from her pack and unlocked the door, flicking on the lights as she entered the room."
    scene Office with fade
    show AE neutral at center with dissolve
    AE "One moment. I'll get the papers with some of the work I need done out first."
    hide AE with dissolve
    "I leaned up against the wall as Shiori-san began to look through the filing cabinets for papers, I looked at her desk and noticed the obscene stacks of paper piled up."
    MCT "Is she really going through all of that?! It could take months!"
    "My eyes wandered over to where Shiori-san was, and I thought admirably on her hard working nature... and then my eyes began to wander a bit lower. As she hopped on her toes to grab some files on the top of the cabinet, I watched as her big bum began to jiggle ever so slightly."
    "She lifted one leg up, unknowingly accentuating her slightly chubby thighs. My thinking went blank for a moment, before immediately snapping back."
    MCT "Sh-shit! If she saw me staring at her like some kind of perv, she would hate me forever. I gotta keep my cool."
    "Shiori-san turned around as I exhaled a deep breath, holding papers in her hands."
    show AE neutral at center with dissolve
    AE "I apologize. One of my subordinates has been rearranging my files. Here."
    MC "Thanks, Shiori-san."
    AE "Now, if you need me, I will be here."
    MC "Okay."
    play music AE
    "I began to leave, but I had an idea in my head that I couldn't really get out. So I turned back to Shiori-san to say what I needed."
    MC "Hey, uh..."
    AE "Yes?"
    MC "You've really got a lot of papers to work on, yeah?"
    show AE glasses-2
    AE "Yes. While usually delegated to multiple members of the student organizations, I've taken the liberty of filling out the forms myself. I've often noticed it's less trouble that way."
    MC "Well, I've been thinking. Maybe I could help."
    show AE neutral-annoyed
    AE "What?"
    "Shiori-san seemed to be taken aback from my statement for a moment."
    if getAffection("AE") < -3:
        AE "I apologize, however I think you misunderstood my gesture by giving these papers to you. I didn't want you to run around outside because the school would be liable. I have no intention of spending any more time with you than I need to."
        MC "Oh... I mean, I just wanted to help."
        AE "I'll take my chances with one of the other members should the need come. Good day."
        MCT "Ouch... Well, I guess that's that."
        jump AE006_routeend #TO BE REMOVED LATER
    elif getAffection("AE") > 2:
        show AE neutral
        AE "Perhaps... it would be better if I had someone with me. From what I gather, you seem competent and responsible."
        MC "Thank you. And if anything, it will make your work be done more efficiently."
        show AE happy
        AE "I see. I must admit, Keisuke-san, in the short time I've known you, you've proven to be quite a driven person."
        show AE neutral
        AE "Very well. I will see to it that you will begin to work under me after class ends. Do your best to not miss a day, will you?"
        MC "You have my word, Shiori-san. See you tomorrow."
    else:
        show AE neutral-eyebrow
        AE "I... No. I can manage this by myself."
        MC "Oh. Um, I didn't mean to say that you needed my help. Just that I think, y'know, it would get done more efficiently."
        show AE neutral
        AE "..."
        "Shiori-san sat in contemplation for a moment. She brought her thumb up and lightly bit on the end of her fingernail."
        show AE angry-3
        AE "...Very well. If anything, I'll be doing a service to the school by helping you prepare for the outside world."
        MC "Thank you, Shiori-san! I promise, you won't regret this."
        AE "I certainly hope not."
    show AE neutral
    AE "Hotsure-san?"
    MC "Hm? Yeah, what's up?"
    show AE glasses-2
    AE "I hope you know what working with me unofficially would entail. We would be spending the next few weeks to a month mostly isolated after classes."
    AE "Spending such amount of time in an office can often be dull for those who aren't interested in the work."
    MC "Right..."
    show AE glasses
    AE "If you feel you don't have a stable enough attention span, then you'll only do more harm than good. With that in mind, are you absolutely certain you wish to work alongside me?"
    menu:
        "Of course":
            MC "Of course. Like I said, I'd love to work with you."
            show AE neutral
            AE "Hmm... Interesting."
            AE "Very well. See you tomorrow."
            $setFlag("AE006_helpinginoffice")
        "On second thought...":
            MC "On second thought... You're probably right. It seems like you really bust your- uh, your... You put a lot of work into the council. I don't think I'd be able to keep up."
            show AE neutral
            AE "No worries. As I said, it's not for everyone."
            show AE happy
            AE "However... I will say, I appreciate your interest in our work."
            AE "Please, have a good day, Hotsure-san."
    scene Hallway with fade
    stop music
    "As I left the library, I gazed out the window. The rain had passed into to a soft drizzle on the horizon as the sun's golden rays began to peek through the clouds. As I walked outside into to fresh air, the smell of petrichor hit my nose as I began to ponder how I would spend the rest of the day."
    if not getFlag("AE006_helpinginoffice"): #TO BE REMOVED LATER
        jump AE006_routeend
    $setProgress("AE", "AE007")
    jump daymenu

label AE006_routeend:
    scene black with fade
    $disableRoute("AE")
    "Refusing to work with Shiori will initiate an alternate route that is currently in development."
    "However, because it's incomplete, Shiori's route will end here. Stay tuned for the alternate route!"
    jump daymenu

label AE007:
    $setProgress("AE", "AE008")
    scene Hallway with fade
    play music Schoolday
    "I briskly strode towards the Library, backpack slung across my shoulder as I prepped for a day to do some extra work. Today was the day I promised Shiori-san I would help her with her paperwork, at least, the day she would introduce me to it."
    "As I turned the corner to the Library entrance hallway, the punctual girl came into view, waiting outside the door."
    show AE neutral at center with dissolve
    MC "Hey, Shiori-san!"
    AE "Hotsure-san, good afternoon."
    MC "So, ready to get to work?"
    show AE neutral-eyebrow
    AE "Are you?"
    MCT "That... felt more like a challenge than a little small talk from her."
    MC "Yeah. Definitely."
    show AE neutral
    AE "Good. I've made ample preparations for today's work, and I estimate that I would be able to finish before sunset."
    MCT "Sunset?! That stack the other day looked like it would last waaaay past sunset."
    MC "Ample preparations? Aren't we just filling out forms?"
    show AE neutral-annoyed
    AE "There is more to my job than filling out forms, Hotsure-san. You, however, will be working on filing the forms."
    MC "Sounds easy enough!"
    show AE neutral
    AE "Well then, let's head in."
    scene Office with fade
    show AE neutral at center with dissolve
    "We walked into the library and headed to the student council office. Shiori-san unlocked it with a key and flipped the switch on; filling the room with the soft whir of the fluorescent lights. Shiori-san sat down at the table and began to pull assorted items from her bag, stamp, pens, pencils, and a menagerie of different folders."
    MCT "I have to make a good impression. I don't want her to think I'm just some lazy bum who can't hold my own!"
    MC "So, I'm ready to get started! Got anything for me to start off with?"
    AE "Yes. If you would please, sign this."
    "Shiori-san handed over a thick packet of papers to me. Just by looking at the front page, I saw a pool of legal jargon and terminology."
    MC "Um... Shiori-san... What is this?"
    show AE glasses-2
    AE "A form that states that you are here assisting me on your free will and accord, as well as a contract stating that you intend to follow the standard rules and procedures set up by the school constitution while working under me."
    MC "Wow... The school administration has a contract like this just to help with the forms?"
    show AE neutral
    AE "No. I wrote it myself last night with the approval of the administration. It also contains the terms of our cooperation, so that there is no confusion on the nature of this agreement."
    MC "...Shiori-san."
    menu:
        "Okay, I'll sign it.":
            jump AE007_c1
        "No way!":
            jump AE007_c2

label AE007_c1:
    $setAffection("AE", 2)
    MC "Well... Sure."
    show AE neutral-annoyed
    AE "You don't plan on reading through it first?"
    MCT "THIS beast?!"
    MC "I trust your judgement. If you made it, I'm sure everything in the contract is agreeable. If I ever get confused I can just refer back to it."
    AE "...Well then, thank you for placing your faith in me."
    "I signed my name on the line provided and handed it back to Shiori-san, who put it in one of her folders for safe keeping."
    jump AE007_after

label AE007_c2:
    $setAffection("AE", -3)
    AE "...Well?"
    MC "I'm not signing this."
    show AE neutral-annoyed
    AE "...Mind explaining?"
    MC "I mean, I promised to help, shouldn't that be enough?"
    show AE angry
    AE "The contract is a simple agreement stating that-"
    MC "Right, but it's not truly official. I shouldn't be signing things that the school hasn't explicitly made necessary."
    show AE neutral-annoyed
    AE "...Very well. I suppose it is unnecessary, then. However, know that I have the clout to terminate your help at any time."
    jump AE007_after

label AE007_after:
    show AE neutral-eyebrow
    AE "Well, in any case, as you can see there is a lot of work to be done. If you work efficiently, we may be able to return to our dorms before sundown."
    MC "Right. I'll get to work on filling these out."
    show AE neutral-annoyed
    AE "Absolutely not."
    MCT "Ehhhh?"
    MC "But you said-"
    AE "I told you that you could file the forms, not fill them out. These deal with sensitive student information. Your job is to put the forms I finish into their respective filing cabinets."
    MC "Then... will I really be helping at all? If all I'm doing is filing the files, then it would still take months to finish all of that, let alone by sundown! All I'd really be doing is shaving a minute or two off of your workload."
    AE "Keisuke-san, there are two things you're underestimating; my ability to sort documents, and the value of a minute or two."
    MC "...Okay, I guess."
    scene black with fade
    "We got to work, and Shiori-san began filling out forms at neck cracking speeds. Every other minute was the sound of scribbling, stamping, and then sliding a paper to me. I nearly choked for a second, before taking the files in hand and bringing them to the cabinet."
    "The names went on and off the desk like lightning, and it honestly felt like for every paper I would take off the desk and file, two more would take its place. A document hydra."
    "By the time the stream stopped, I was nearly panting from the quick, bustling motion of it all. The scribbling and stamping had stopped now, and as I grabbed the last few files, I looked back on the pile of files and I realized..."
    scene Office with fade
    show AE neutral at center with dissolve
    MC "They're...gone?"
    AE "Yes, Hotsure-san. I filled them all out."
    MC "B-wha-I-"
    show AE neutral-smug
    AE "As I said, removing the time to sort the files increased my productivity drastically. I thank you for that."
    MC "Huh... oh... OH! Yeah! It really did!"
    show AE neutral-annoyed
    AE "Enough so that we aren't even close to sunset..."
    "Shiori-san let out a sigh, and with a sullen look walked over to the filing cabinets."
    MC "Shiori-san? Is everything okay?"
    show AE angry
    AE "My estimate was wrong for the time needed, which can only mean one thing; you worked faster than my estimate."
    MC "Oh! Thanks, Shio-"
    show AE neutral
    AE "It's my fault, I asked you to sort the files without teaching you a proper method."
    MC "Eh?"
    "I looked down at my 'handiwork' and a feeling of absolute despair washed over me."
    MC "EEEEEHHHH?!"
    "Files were strewn about and placed incorrectly in their folders, there were crumpled messes of paper smashed into the areas between folders."
    MC "Oh man... Shiori-san, it was my responsibility, and my fault. I should have been paying attention."
    AE "It's fine, Hotsure-san, I can fix this easily. It will take a bit after sundown to do so, but I can."
    MC "I... I should go."
    AE "If you did you wouldn't learn anything."
    MC "O-Oh."
    show AE angry-3
    AE "Hmm..."
    AE "Pacing." 
    MC "Huh?"
    show AE neutral
    AE "Your problem is pacing. I plan on rectifying that. I will have plenty of files tomorrow to work on as well, I hope you will be there."
    MC "Shiori-san... Thank you. I will."
    AE "Hm."
    scene Hallway with fade
    "I walked out of the library, my hope restored with plans for the next time. Until then, I gotta figure out the rest of the day."
    jump daymenu

label AE008:
    $setProgress("AE", "AE009")
    scene Office with fade
    show AE neutral at center with dissolve
    play music Hallway
    "Today was the second day I went to the office with Shiori-san. I kind of felt like I was missing out on a bright, sunny day, but at least I could redeem myself for the other days failure."
    AE "Remember, steady breathing. No matter how quickly you receive files, double check to make sure that everything is in order."
    MC "Got it."
    hide AE with dissolve
    "Today started off much the same as yesterday, but as promised, she was intent on teaching me 'proper filing methods'. It started off with me looking on uninterested, but over time, surprisingly, I actually got invested."
    show AE neutral-eyebrow at center with dissolve
    AE "And here, unless it's the only available cabinet, avoid the ones at the very top and bottom. If you take the middle rows to be the most often used, you won't need to spend extra time and effort bending over or standing on your toes."
    MC "Yeah, I can see how that would help. It looks like you've already moved the paper from the other day."
    show AE neutral
    AE "Indeed."
    MC "So, how long did all of that take? Putting the files back in the right places?"
    show AE neutral-annoyed
    AE "Twenty minutes or so. However, that also involved re copying papers that you crinkled."
    MCT "Oh... right. Man, first day and I actually ADDED work instead of helping. Shiori-san must either feel sorry for me, or really care about me to keep me around..."
    MC "Sorry again. I know it must be a pain having me here."
    show AE neutral
    AE "Not at all, it's somewhat reaffirming to have someone here of their own volition. It shows you care about the inner workings of the school."
    MCT "That's a VERY generous depiction of me."
    AE "So, all in all, I believe I've given you what you need to be able to sort the files correctly. Use the new method I showed you to sort these files on the desk."
    MC "Got it..."
    MCT "Wait."
    MC "Shiori-san, did you have these pre-prepared for me to work on?"
    show AE happy
    AE "Ah, observant of you, Hotsure-san. Yes. I came in early this morning and filled out some forms in anticipation for your training."
    MCT "Early this morning? How did she get all of these done before class?"
    MC "Oh, uh, thanks Shiori-san, but... How early did you wake up?"
    show AE neutral
    AE "Around five thirty."
    MCT "Five thirty?! Is she insane?!"
    MC "Wow... um, that's... dedication?"
    show AE neutral-eyebrow
    AE "Thank you. Now, if you will."
    "Shiori-san made a hand motion over to the papers. I could tell that the lack of productivity was making her antsy."
    MC "Okay, what will you do?"
    show AE neutral
    AE "I have to stamp these documents with the school seal. Feel free to ask for help if you need it."
    MC "Will do."
    hide AE with dissolve
    "I got to work on the filing, this time taking things in stride. Every few seconds, I could hear the click of a stamp pushing down on paper."
    "*K-chk*"
    "It started off as just background noise, but as time went on it felt more like a rhythm, reminding me to keep pace. It worked pretty well... for a bit. Shortly after the student's bane began to set in, the dreaded foe of all academics... boredom."
    MCT "Seriously, how does she just do this day in and day out?! It's killing me."
    show AE neutral at center with dissolve
    AE "You're stalling. What's wrong?"
    MCT "Ah, I guess she noticed. Well, maybe a bit of conversation will help."
    MC "Hey, Shiori-san, not to seem like I don't like being here, don't get me wrong, it's just... is this it?"
    show AE neutral-annoyed
    AE "It? Yes. But 'It' is an important task that must be dealt with care."
    MC "I know, but like... Do you do anything while you work or is that, I dunno, distracting?"
    AE "Well, I usually just sit in silence. The office is often empty, so I suppose it gives me some time to myself."
    MC "Doesn't that get lonely?"
    "Shiori-san took a bit to answer, thinking to herself as she stamped away."
    AE "I must admit, it can get somewhat... desolate, for lack of a better term."
    MC "Well, would you like to talk a bit then, or?"
    show AE angry-3
    "Shiori-san stopped for a moment, and began gently nibbling on the end of her thumb nail."
    AE "That depends... It seems as though the monotony is affecting your output, but do you think that you can keep working if we do?"
    MCT "Anything that can stop myself from falling asleep would be a godsend."
    MC "Definitely."
    show AE neutral
    AE "Very well then. Talk to me if you wish."
    MC "Cool."
    "I continued back on my regular filing patterns, feeling slightly renewed with the new prospect of interactivity."
    MC "So, how are classes going?"
    AE "..."
    MCT "..."
    MC "U-um, are they going well or?"
    AE "..."
    MC "Uh, Shiori-san?"
    show AE neutral-eyebrow
    AE "Yes?"
    MC "Didn't you want to talk?"
    show AE neutral
    AE "Oh? You wanted me to talk with you?"
    MCT "What's the point of a one sided conversation?!"
    MC "I mean, having a conversation together is what I was hoping for, yeah."
    show AE angry-3
    AE "Hmm... All right. I suppose it wouldn't affect my work one way or another. You asked me about classes, yes?"
    MC "Yeah, how are they?"
    show AE neutral
    AE "Perfectly fine. The subject matters are interesting, but there are some things that are a bit... unnerving about the room."
    MC "Like what?"
    AE "The size of the room, as well as distance between chairs, for example. That much free room is somewhat strange."
    MC "Well, I mean, it makes sense. After all it's our homeroom, and they will need to be tailored for, y'know, different conditions and stuff."
    show AE neutral-annoyed
    AE "And stuff? Such as?"
    MCT "Eh? Why the intensity all of a sudden?"
    MC "Well, I dunno. I mean, we'll all be growing, so the class seating has to be shifted around a bit just in case, right?"
    show AE sad
    AE "...Yes... I'm well aware."
    MC "I don't think I'll be needing to shift around that much, but I mean, you sit right in front of me."
    show AE neutral
    AE "Ye-"
    show AE surprised
    MCT "...Huh?"
    "Shiori-san stopped for a moment, moving her hand a bit closer to her mouth before hesitating. It was faint, but she was lightly blushing."
    show AE embarrassed
    AE "Behind me..."
    MC "Shiori-san? Did you forget?"
    show AE aroused-3
    AE "N-no. I merely thought of some things that I... hadn't previously taken into account."
    MC "Uh... okay?"
    AE "I can trust you to..."
    MC "Huh?"
    MCT "Tooo...?"
    show AE neutral
    AE "Never mind. It's of no importance at the moment."
    MCT "Shiori-san doesn't seem like one to leave a thought unfinished... Is everything okay?"
    MC "Hey, Shio-"
    show AE neutral-eyebrow
    AE "You've stopped filing, Hotsure-san."
    MC "Hm? Oh! Sorry, I forgot."
    show AE neutral
    AE "It's fine, it seems as though you're nearly done anyway."
    MC "Eh?"
    "The stack of papers I had been filing had been thinned down without me noticing. It seems as though her 'training' paid off."
    MC "Ah! H-Hey! Yeah, I did it! And I think... Yep, all placed correctly!"
    AE "I've finished as well, so I suppose we can call it a day."
    MC "All right. Ready to head out?"
    show AE neutral-eyebrow
    AE "Mm, you go on ahead. I'm going to double check your work and make note of a few things in the office."
    MC "Oh, okay. See you later, Shiori-san!"
    AE "Indeed."
    scene Hallway with fade
    "I walked out of the office door and into the library, ready to finally get some fresh air and sunlight... Well, until something hit me. I was at the door of the library when I was hit with a wave of curiosity."
    scene Library with fade
    "Call it a compulsion, a random stroke of unease, whatever, but for some reason I had a suspicion about Shiori-san after I left. I realize that most would consider it crazy, even a bit creepy, but I felt the need to take a quick look back at Shiori-san before I left. Walking up to the office window, I peeked in."
    MCT "Shiori-san? What is she...?"
    "Shiori-san wasn't working. She was standing up. Her hands reached down to the sides of her hips as she looked back at her rear. She was staring at the far wall when I heard her speak."
    AE "Stand... Bow."
    "Shiori-san bent over, bowing to the invisible teacher... When she looked back. Her back was arched, and it was impossible not to see her twin mounds, covered by her blue skirt, sticking straight out to see. She looked back, put her hands on her butt and squeezed as the color drained from her face."
    "I dared not look any more, for fear of being seen, and quickly left the library prepared to face a the rest of the day, admittedly, with a new level of concern for my classmate."
    jump daymenu
    
label AE009:
    $setTimeFlag("size2")
    $setProgress("AE", "AE011")
    scene Hallway with fade
    "The sound of rubber squeaking against the laminated floors echoed as I ran down the hall. I briskly rounded the hallway corner, just barely missing another student."
    MCT "Damnit, Daichi! You just had to play that homemade documentary, didn't you?!"
    "I hadn't been keeping an eye on the time. I went back to my dorm to grab a bite to eat before I went to the office, but as soon as I got in Daichi decided it was a good idea to sit me down to show me a video he made about the how the School profits are being diverted to some shady Biotech company that I'd never heard of."
    "I slowed down as I neared the library door, composing myself before entering. I made my way through and entered the office, where Shiori-san was writing a report of some kind."
    
    scene Office with fade
    play music Peaceful
    show AE sad at center with dissolve
    AE "There you are, Hotsure-san. I wanted to-"
    show AE surprised
    MC "Hi! Really sorry I'm late."
    "Shiori-san winced for a moment, and then replied after a few seconds."
    show AE neutral
    AE "...It's fine Hotsure-san, just try to be more punctual in the future."
    MC "I hurried to head over here as soon as I-"
    MCT "GAK! DON'T SAY HURRY!"
    show AE neutral-annoyed
    AE "...You didn't run to get here, did you?"
    MCT "Eeeeeehhhhh."
    MC "Kind of?"
    show AE angry
    AE "You-w-nghh."
    show AE neutral-annoyed
    AE "Nevermind. I had something I wanted to ask you about first."
    MC "Already? You don't want me to start working to catch up?"
    AE "It can wait. I need you to answer this."
    MCT "Woah... Shiori-san is being really serious with this. It must be important."
    MC "Oh. Okay, sure."
    show AE sad
    AE "When we do the morning introductions, is my... growth a problem?"
    MC "Um... What do you mean by problem?"
    show AE aroused-3
    AE "Is it distracting to you? Unsightly? If you find the situation unsettling I will take precautions to stop it."
    menu:
        "Absolutely not.":
            jump AE009_c1
        "Yes, but it's fine":
            jump AE009_c2
            
label AE009_c1:
    MC "Not at all. I mean, I usually close my eyes whenever I bow, so it's no big deal."
    show AE angry-3
    AE "Hm... I suppose that if we all bowed at the same time it wouldn't be too much of a problem."
    MC "Exactly. You can rest assured that I'm not..."
    extend " You know, gawking."
    show AE neutral
    AE "Good. I didn't want to have to file a request for seat transfer. However, since it seems as though it won't be affecting you no action will need to be taken."
    jump AE009_after

label AE009_c2:
    MC "Well, I guess in a way it is kind of distracting, yeah. But, I wouldn't say it's that big of a deal."
    if getAffection("AE") >= 4:
        $setAffection("AE", 1)
        show AE angry
        AE "Getting distracted isn't a big deal? Hotsure-san, your academic standing is one of my top priorities, if for any reason you feel distracted I would not hesitate-"
        MC "Shiori-san, it's fine! Really. I should be apologizing for not paying attention."
        show AE neutral-annoyed
        AE "Hotsure-san, you don't need to say things like that. It's my duty as class president to make sure that you are given an efficient learning environment."
        MC "But it's mine as an individual to adapt to situations. You don't need to take any precautions for me. Besides, I can learn responsibility by reminding myself to keep focused, right?"
        "Shiori-san seemed conflicted for a moment, if not slightly agitated. She let out a sigh and nodded."
        show AE neutral
        AE "Right. Well, that's that then."
    else:
        $setAffection("AE", -1)
        show AE neutral-annoyed
        AE "How so?"
        MC "Huh? Oh, well, I notice it a lot, but it's not like, that big of a deal. I mean, it's normal to stare a bit."
        show AE angry-2
        "Shiori-san looked at me with concerned eyes, her brow furrowed in a mix of confusion and what felt like a hint of contempt."
        show AE aroused-3
        AE "Well, if you would please, cease that behavior. If you get distracted it makes the class look bad. Furthermore, I would appreciate that you didn't... gaze at me in the manner that you're implying."
        MC "O-oh! No, no, no, I didn't mean it in that way. I meant more like, it's abnormal to see someone with a body like yours and... I..."
        MCT "Rest in peace Hotsure, you blithering idiot."
        show AE angry-3
        AE "..."
        show AE neutral-annoyed
        AE "Just... Just make sure that you correct yourself, good?"
        MC "Yeah."
        show AE neutral-eyebrow
        AE "Well, I suppose I won't be needing this then."
    jump AE009_after

label AE009_after:
    "Shiori-san took the piece of paper she had until recently been filling out and folded it twice before carefully placing it in the waste bin."
    show AE neutral
    AE "So, shall we get to work?"
    MC "Yeah."
    hide AE with dissolve
    "Like before, Shiori-san wrote away while I took the files she filled and put them in the correct cabinets."
    "I was just about to get done with my first stack when I head Shiori-san speak up from behind me."
    show AE neutral at center with dissolve
    AE "So... Is there anything on your mind?"
    MCT "Any... huh?"
    "I was taken aback for a moment, before realizing what had happened. Shiori-san wanted to start a conversation."
    MC "Sh-Shiori-san?"
    show AE neutral-eyebrow
    AE "Well, you said that having a conversation helped you work efficiently, yes? Then let's begin."
    show AE neutral
    "I couldn't help but smile a bit, I hadn't expected this, so I scrambled for a conversation topic really quick."
    MC "So, the academy itself, what do you think?"
    show AE neutral-eyebrow
    AE "Can you be specific?"
    MC "Well, how does it compare to your old school?"
    show AE neutral
    AE "Seichou is far better. So far I've only had to deal with minor infractions every now and then."
    MC "Barring the whole, you know, thing with those guys a while ago?"
    AE "Including. It was supposedly nothing but childish comments, I'm used to dealing with that."
    MCT "I guess she's right, getting flak for being the class president should be kind of expected... but wait."
    MC "Used to it? So, you've been in a position like this before?"
    show AE glasses-2
    AE "Of course. If I hadn't, and hadn't been good at it, I wouldn't have been chosen to be the class president by the school board."
    MC "Oh yeah. I heard that it was an abnormal election, for the most part. No one wanted to step up aside from you."
    show AE neutral
    AE "Indeed."
    show AE neutral-annoyed
    AE "Actually, if we can go back to the topic of infractions, I would like to know why you were late."
    show AE neutral
    MCT "Oh boy, here we go."
    MC "Daichi. Enough said?"
    show AE neutral-annoyed
    AE "No."
    MC "Oh. Well, uh, Daichi-san kinda forced me down and had me watch a video he made about a conspiracy he thought up."
    show AE neutral
    AE "...I truly do not envy you."
    MC "Right?"
    show AE angry
    AE "What he needs is strict discipline, and I swear I will bring it right to him once I have justification."
    MCT "Yikes. This is getting kind of intense. I think I should dial it back a bit."
    MC "Yeah, uh, you like this school better than your last? That's good."
    MC "And, you know, I think the reason why the students here have less rules broken and stuff is because everyone is here under... You know, the same circumstances."
    show AE angry-2
    stop music
    AE "I don't believe that for a second."
    MC "..."
    "The silence hung there in the room, coming out of left field, along with the drastic change in tone from Shiori-san. The way she said that... just didn't feel right."
    "I opened my mouth to say something, when Shiori-san spoke up."
    show AE neutral
    AE "Well now, Hotsure-san, it seems like you're nearly finished with the stack."
    play music Peaceful
    MC "O-Oh, yeah! Just a few more left after this."
    "Shiori-san laid down a few more pages which I picked up readily, preparing to place them in the final slots."
    MC "Two aaaand, done."
    show AE happy
    AE "I must say, Hotsure-san, you're getting very good at this."
    MC "Actually, yeah, I'm really feeling like I'm getting my stride here."
    show AE neutral-smug
    AE "Glad to hear, because I have these."
    "Shiori-san plopped down a second pile on the desk in front of me, around twice the size as the last."
    MC "Shiori-san... What are these?"
    show AE neutral
    AE "These are the second batch that I also had done before you came."
    MC "U-um, Shiori-san? How am I supposed to file all of these?"
    show AE neutral-smug
    AE "Consider it your punishment for your tardiness."
    MCT "EEEEHHHHHH?!"
    MC "A-are you sure? I mean, it could take all day! You wanna go home too, right?"
    AE "I can wait."
    
    scene black with fade
    "After facing a hellscape of papers, I finally got to leave... once Shiori-san had enough pity for me to let me go."
    jump daymenu
    
label AE010:
    $setSize(2)
    $setTimeFlag("aftersize2")
    scene Hallway with fade
    play music Peaceful
    "I walked down the hallway, getting ready to meet Shiori-san at the office. I heard that shipping and processing had been getting a lot of orders recently, so I figured that today would be a busy one."
    "I assumed, however, that was the reason for Shiori-san's absence from class, something I would have never expected."
    MCT "Hmm? Wait... Shiori-san?"
    "Shiori-san stood by the entrance to the library, holding a stack of yellow sheets in both arms. The spectacled girl had her back against the hallway wall, looking at me from the side."
    MC "Hey, Shiori-san! Have you been waiting out here for me?"
    show AE neutral at Position(xpos=.99, xanchor=0.5, yalign=1.0) with dissolve
    AE "Good day, Hotsure-san, I had to get these papers from inventory, so I figured we would meet here around the same time."
    MC "Need me to get those?"
    show AE embarrassed
    "Shiori-san stepped back a bit when I put my hands out."
    AE "N-no, it's fine."
    MC "Okay, then. Here, let me get the door."
    "I held the door for a bit before Shiori-san looked at me with determined eyes."
    show AE aroused-3
    AE "You go first."
    MC "Um... All right then."
    
    scene Library with fade
    "We walked through the library, Shiori-san following closely behind me, until we reached the office door."
    MC "Want me to take those, so you can unlock it?"
    show AE neutral at Position(xpos=.99, xanchor=0.5, yalign=1.0) with dissolve
    AE "Here. The key is on the stack. Take it."
    MC "Okay...? Thanks."
    MCT "That's a bit convenient, isn't it?"
    "Taking the key in hand, I inserted it and turned the knob."
    
    scene Office with fade
    "The lights were flicked on and I went to my station."
    MC "So, Shiori-san, what's with the stack of papers?"
    show AE neutral at Position(xpos=.99, xanchor=0.5, yalign=1.0) with dissolve
    AE "These forms are going to processing after they're filled out, don't worry about them."
    MC "Okay."
    MCT "Doesn't really tell me anything, but whatever."
    AE "Right, well, turn around and get to work."
    MC "..."
    AE "..."
    MC "Um... Are you gonna start filling some out so I can... you know?"
    AE "There's still some stacks you've yet to file from last time. I can start approving these forms here while you work."
    MC "Oh, okay. I'll just get those then."
    show AE embarrassed
    "I moved to go pick up a stack next to Shiori-san, when she sidestepped away. I took it as just a courtesy, but it got strange once she turned to ensure that she was facing me."
    MCT "Okaaaay. That's weird. It's almost like..."
    "I would move and Shiori-san would reciprocate by maneuvering opposite to me. She tried to make her moves subtle, I could tell, but once I started to catch on, it was impossible not to notice."
    MCT "Is she... avoiding me?"
    show AE aroused-3
    "Just as a way to test my suspicion, I made an extra effort to walk over to the far cabinet towards Shiori-san rather than just reaching over. Much to my suspicion, Shiori-san backed away slightly."
    MCT "Okay, something is definitely wrong."
    MC "Shiori-san, is everything all right?"
    AE "Yes, Hotsure-san. Keep working."
    MC "It's just that you seem a bit different this morning."
    MCT "Shiori-san stiffened up a bit, turning further a bit. She brought her thumbnail up to her mouth."
    show AE angry
    AE "Oh... really? How so?"
    MCT "Why is she so apprehensive? Well, more than usual at least."
    MC "I dunno, it's just that you aren't the same as the last time we talked, is all."
    show AE sad
    AE "Yes, well... I suppose that we're the same in that regard."
    "Shiori-san pointed at my head in the same way one would when trying to tell someone there was something on their face."
    MCT "Huh? What is she...?"
    "I looked off the side to catch a glimpse when I saw it."
    "Completely going unnoticed by me until now, my hair was definitely longer. Feeling around the back of my neck, I noticed that it went past my nape at this point, and flowed to bottom of my neck."
    MC "Wait... How did this? When did it get this long?"
    show AE angry
    AE "You never noticed?"
    MC "No, I..."
    show AE aroused-3
    "I sat in confusion for a moment, trying to get a full grasp of just how my hair had grown this long without my knowledge, when I noticed Shiori-san quietly sit down and face her back to the wall. That's when it hit me."
    MC "Shiori-san... Are you also?"
    AE "...Also what?"
    MC "Well, if my hair has grown like this for the relatively short time I've been here, then... have you also?"
    "Shiori-san shrunk back a bit, eyes intently glaring at me."
    MCT "I'll take that as a yes."
    show AE sad
    AE "Well..."
    MC "And that's why you've been hiding your back."
    MCT "Now that I'm saying it out loud, I'm starting to realize how dumb I was for not noticing it earlier."
    if getAffection("AE") >= 4:
        "Shiori-san winced a bit when she realized that her gambit had been called, then, finally resigned to the inevitable."
        show AE sad
        AE "...Yes. Yes it is."
        "Shiori-san let out as sigh. Of relief or frustration, I couldn't really tell."
        AE "Well, if I keep trying to hide myself then it seems neither of us will be able to get our work done."
        AE "So I want you to... get it out of your system now." 
    else:
        "Shiori-san looked at me fiercely, an angry scowl spread across her face in return for what she took as grave disrespect."
        show AE aroused-3
        AE "N-now hold on! I would recommend you keep your comments to yourself."
        MC "Shiori-san?"
        AE "My personal affairs are my own, and if I choose to... evade your gaze, I have every right to."
        MC "Sorry, I didn't mean anything by it."
        show AE angry
        AE "Look. Just get it out of your system now so we can continue our day."
    "Shiori-san took her back away from the wall and finally did it."
    MC "Out of my system? Shiori-san, I'm not going to insult y-"
    "Shiori-san finally turned around."
    stop music
    show AE neutral at Position(xalign=0.5, ypos=1.0, yanchor=0.95), Transform(zoom=2.0)
    play sound Boing
    MC "W-HOA MY GOD!"
    "I took the full force of the sight at once. Shiori-san's skirt did little to hide her gigantic behind, tears appearing along the seams showed small glimpses of pale and taut skin as the fabric squeezed her rear, only leaving a scarce inch between the bottom of her butt and the fabrics end."
    "Both cheeks were blown up to the size of full balloons and stuck out a foot from her back, creating noticeable creases along the top of their curvature. Shiori's shelf-like hips stuck out from her sides to match her astounding ass, taking her poor skirt to its limits in order to cover her shame."
    "Her legs, though, didn't receive any such mercy. Her thunder thighs were in full view, as the girl could do nothing but show off her fat, chubby legs in embarrassment, her knee being the only respite until reaching her calves, which had seemed to have swelled a bit too."
    MC "Shiori-san! You're huge!"
    show AE neutral at center, Transform(zoom=1.0)
    "Shiori-san turned around, blushing furiously as she brought a hand to the side of her face to avoid eye contact."
    show AE sad
    play music AE
    AE "..."
    MC "I mean... oh my god!"
    if getAffection("AE") >= 4:
        AE "I get it, Hotsure-san."
    else:
        show AE angry
        AE "I get it."
    "Her response served as a reminder of the situation was in, as well as the inappropriate nature of my words."
    MC "Oh! No, I mean, well... sorry."
    show AE sad
    AE "..."
    show AE embarrassed
    AE "It's fine, Hotsure-san. I realize that it's... off putting, but now that that's over, we can continue work uninterrupted."
    MC "Y-yeah."
    "I got to work on the stack of last time's papers. An awkward silence permeated the room as we both tried to get over what had just happened. I kept trying to focus on my job, but my mind kept racing back to the image of Shiori-sans rear."
    MCT "Damnit, how was that supposed put my mind at ease again?!"
    MCT "I gotta at least try to start off a conversation, if I don't, I'll be standing here all day."
    MC "Did..."
    show AE neutral
    AE "Hmm?"
    MC "Did that happen overnight?"
    show AE sad
    AE "...I don't believe so. It's just that I need a larger uniform and I've yet to get one, is all."
    MC "I would have figured that you would ordered early."
    AE "I did. As it so happens there was a backlog."
    "Shiori-san took another stack of yellow papers and placed them on her desk."
    show AE neutral
    AE "This is the backlog."
    MC "So, that's what those were."
    show AE angry
    AE "Yes, and the sooner it's done the sooner I can get out of this embarrassing situation."
    MC "So, what, then students just have to wait until their clothes get too small?"
    show AE neutral
    AE "Well, yes, however the School has a partnership with a local tailor. If you pay a premium then you can get your clothes fixed at any time."
    MC "Oh, really? I didn't know that."
    AE "Most students don't, to be honest. That's why the student council is thinking of ways to get the message out."
    MC "Why don't you do that? Get your clothes fitted?"
    show AE sad
    AE "..."
    "Shiori-san sat in silence for a moment, but spoke up again after a brief period."
    show AE glasses
    AE "I would have to fill out more forms then. My clothes aren't as high a priority as my work."
    MC "They seemed pretty high priority..."
    MCT "I shouldn't get into it."
    AE "What?"
    MC "Nothing."
    show AE neutral
    AE "Hm."
    hide AE with dissolve
    "We kept working for a bit, until Shiori-san put her pencil down and stacked the papers."
    show AE neutral at center with dissolve
    AE "There. Forms filled."
    MC "Oh, cool. Should I keep working?"
    AE "No, actually, I think that should be it for today. I need to get these back to processing."
    MC "Okay. I'll head out too then."
    "I closed the file cabinet, and prepared to head out, backpack in tow, when Shiori-san stopped me in the middle of the room."
    show AE aroused-3
    AE "Wait, Hotsure-san, before you go..."
    MC "Hm? What's up?"
    show AE embarrassed
    AE "I think it goes without saying, but... could you not bring up earlier to anyone? I showed you... why I was worried in order to ease your mind, nothing else."
    MC "Oh, don't worry about it. It's okay, I mean, as long as you don't go around talking about my rat's-nest hair."
    show AE neutral-smug
    AE "I won't."
    MC "Cool."
    scene Library with fade
    "As we walked out, I couldn't help but catch a glimpse of Shiori-san's butt. It wobbled as she shuffled along, swishing side to side as the bottom of her skirt fabric swayed with her movements."
    MCT "H-hey, c'mon man, don't."
    "My eyes snapped back up to attention, thankfully keeping me from running into the library door frame. I walked out, and headed into the hall to continue my day."
    jump daymenu

label AE011:
    $setProgress("AE", "AE012")
    scene Hallway with fade
    play music Peaceful
    MC "Oy! Shiori-san. How's it going?"
    show AE neutral at center with dissolve
    AE "Perfectly fine, Hotsure-san. Just getting some papers for the printer."
    MC "O-oh, yeah! Cool."
    MCT "Cool? Really?"
    if isEventCleared("AE010"):
        jump AE011_010followup
    else:
        jump AE011_no010

label AE011_010followup:
    "I was trying my best to conceal my awkwardness, but by looking at Shiori-san, the mental image of her big behind kept lingering in my mind."
    MCT "C'mon man, get a grip. You saw a girls clothed ass. Big deal. If you make it awkward then-"
    "My thought was cut short by the sound of Shiori-san clearing her throat."
    MC "Huh?"
    AE "I hope I wasn't interrupting any important thoughts, however we should be heading in if we're to get our work done on time."
    MC "O-oh, yeah. Sounds good."
    scene Library with fade
    "Shiori-san opened the doors of the Library, holding it for me to enter. As we walked, Shiori-san muttered something under her breath. It was low enough for me to not hear, but I know something was said."
    show AE neutral at center with dissolve
    MC "U-um... Shiori-san?"
    AE "Hm?"
    MC "What was that, just now?"
    show AE neutral-annoyed
    AE "..."
    AE "I assume... you kept your end of the bargain?"
    MC "The...?"
    show AE neutral
    AE "From the other day."
    MC "I don't... know what you're talking about."
    if getAffection("AE") >= 4:
        show AE neutral-smug
        "Shiori-san turned around with a slight smirk on her face."
        AE "Ah, I see. Very astute of you, Hotsure-san. You're diligent."
        "I responded with a smile and nod of my own."
        MC "Always."
        "As soon as Shiori-san turned around my smile immediately dropped into a look of confusion."
        MCT "What was that abo-"
        MCT "Oooohhh. The promise, not to talk about... yeah."
    else:
        "Shiori-san let out a sigh, and stopped in place."
        show AE neutral-annoyed
        AE "You forgot, right?"
        MC "The... uh..."
        show AE angry
        AE "You said you weren't going to dwell on the events of yesterday or tell anyone."
        if getSkill("Academics") > 3:
            $ setAffection("AE", 2)
            MC "I realize, Shiori-san. That's why I've been pretending like I didn't know."
            show AE neutral
            AE "W-"
            show AE neutral-smug
            "Shiori-san looked on confused for a moment, before slowly giving a small smirk."
            MCT "I did it."
            AE "A-Ah, I see. Very astute of you, Hotsure-san. I'm sorry for doubting you."
            "I responded with a smile and nod of my own."
            MC "Always."
            MCT "I'm unstoppable."
        else:
            MC "I... uh..."
            AE "Ngh... I suppose it's my fault."
            MCT "Ugh... that hurts."
    jump AE011_aftertest

label AE011_no010:
    "My mind was blanking. For some reason, my eyes kept getting drawn to Shiori-san, but I couldn't tell why."
    AE "Well... let's continue. You go first."
    MC "It's all right. You can."
    show AE embarrassed
    AE "..."
    "Shiori-san let out a sigh."
    show AE aroused-3
    AE "Hmph. I have a new skirt anyway, so... fine."
    MC "Um... Shiori-san? What does that have to do with anything?"
    show AE neutral-annoyed
    AE "...Nothing."
    MC "Okaaaay~."
    scene Library with fade
    "We headed into the library, and it was only a short matter of time before I noticed what had changed."
    MCT "I... is her... butt bigger?!"
    show AE angry
    AE "AHEM."
    "Shiori-san cleared her voice loud enough to startle the librarian at the front."
    show AE neutral-annoyed
    AE "Khm... I apologize. Throat soreness."
    MC "A-ah..."
    MCT "And with that my eyes are front and center..."
    jump AE011_aftertest

label AE011_aftertest:
    scene Office with fade
    "We entered the room together. The all too familiar whirr of electric lights sounded as fluorescence filled the room."
    MC "Welp. Let's get to work."
    show AE neutral at center with dissolve
    AE "Let's."
    hide AE with dissolve
    "The workday carried out today like previous days. Shiori-san and I gave sparing comments here and there as we worked with little actually happening. That's when it hit me."
    "I was bored."
    "It took me a bit of meandering about my work before I realized what today was lacking; human interaction. Sure, Shiori-san and I were talking here and there, but what the words felt empty. I wanted something with substance."
    show AE neutral at center with dissolve
    MC "Hey, Shiori-san, what've you been up to?"
    "Shiori-san slowed from her lightning speed writing in order to acknowledge my question."
    AE "Up to? Do you think I've been planning something?"
    MCT "It wouldn't be a first."
    MC "Well, no, not like that. I mean what all have you been doing?"
    AE "Hm, well, I've been performing the duties of my office."
    MC "...Filling out papers?"
    play music Tension
    show AE neutral-annoyed
    AE "...Is that all you think I do?"
    MCT "Yes."
    MC "Not to say that you're job isn't rough or anything, it's just that when I see you work it's usually here filling out forms."
    show AE neutral
    AE "That's for good reason. Much of my work deals with things not open to the public. Student government tends to be a fairly involved undertaking, both inside of meetings and out."
    MC "Really?"
    AE "Of course. Between meetings, monitoring, management, setting up for events, amending and enforcing laws and the ubiquitous peacekeeping duties in the school, filing forms is one of the few moments of quiet I have in the day."
    MCT "It's really sad when your only down time is filling out paperwork. At that point I'd rather just become a NEET."
    MC "And you still have some of the top grades in class? I'm surprised you haven't asked me to stay around more often."
    AE "Trust me. If you were a full time assistant, you wouldn't have been so keen to offer your help."
    MC "I dunno about that. It's been fun spending time with you."
    show AE happy
    AE "Well... I appreciate the sentiment, in that case."
    MC "So... what else do you do?"
    show AE neutral
    AE "Hm?"
    MC "You know, outside of class and work."
    AE "There isn't really that much else for me to do. I study different topics that might help me further my knowledge, I suppose."
    MC "Is... is that it?"
    show AE neutral-annoyed
    AE "Does there need to be anything more?"
    menu:
        "There is more to life than classes.":
            jump AE011_c1
        "I guess not.":
            jump AE011_c2
            
label AE011_c1:
    $setAffection("AE", -1)
    MC "There is more to life than just going to class, you know."
    show AE neutral
    AE "Such as?"
    MC "Well... you know, having hobbies, doing something fun, doing something... anything at all?"
    show AE neutral-annoyed
    AE "I live by what I must do to ensure my future, Hotsure-san. My duties are to the school, as is my loyalty. To me that's enough to sustain my lifestyle."
    MC "Well, right, but can't you say something that you have done or do that seems interesting at all?"
    show AE neutral
    AE "..."
    show AE angry
    AE "What are you insinuating, Hotsure-san?"
    MC "Wait, wait, I didn't mean anything by that. I meant, like, what all is there to look forward to at the end of the day?"
    show AE neutral-annoyed
    AE "I believe I've already answered that."
    MC "A-ah, right, sorry."
    show AE neutral
    AE "Hm."
    jump AE011_afterchoice

label AE011_c2:
    $setAffection("AE", 1)
    MC "Well, I guess not, really. You live the way you think is best."
    AE "Exactly. I'm glad you understand."
    MCT "Still, I can't imagine that would be any type of life I'd want to live."
    MC "Well... what keeps you going?"
    AE "My obligation."
    MC "Your... obligation?"
    AE "Well, I suppose we all have one. I simply do everything I can to ensure that I'm doing right by the position of my office."
    MC "Hmm... yeah."
    jump AE011_afterchoice

label AE011_afterchoice:
    MC "Still though, I want to know what your interests are."
    AE "My interests?"
    MC "Yes."
    show AE neutral-annoyed
    AE "And why are you concerned about those?"
    "I shrugged, not knowing the best way to respond."
    MC "Dch-I guess I just wanted to know more about you."
    "Shiori-san went from my gaze to looking back down at her papers."
    show AE neutral
    AE "I don't see why. As you can tell I'm not a person with very exciting life stories."
    MC "Well, You don't need to be. I just wanna know what you like and dislike."
    "Shiori-san began to look around a bit, before facing me again."
    AE "I see... and you would like to know?"
    MC "Of course."
    play music Peaceful
    AE "Hmm... okay."
    MC "Great! So first, wha-"
    AE "Next time we work."
    MC "...Eh?"
    AE "I need to prepare some answers to possible questions. Next time, when we are working, you may ask as many questions about me as you like."
    MCT "Eeeehhhh?"
    MC "Why do you... need to prepare for questions about yourself?"
    AE "Well first of all, I want to ensure completely accurate answers."
    MC "...About yourself."
    AE "Yes."
    MCT "Whatever. I can deal."
    MC "Okay."
    AE "Second, you wish to ask multiple questions, yes?"
    MC "Yes."
    show AE angry
    AE "Well I suppose if you did so now you would need to do so quickly."
    MC "Why's that?"
    show AE neutral
    AE "I have a Student Government meeting soon, and from the looks of it... Yes, I'm done with this stack for today."
    MC "Eh...? Already?"
    AE "Indeed."
    "Shiori-san stood up, and pushed her chair in."
    AE "If you don't mind, close up after you've finished filing."
    MC "Oh, okay, sure."
    AE "That should be all, then. Have a good day."
    "Shiori-san walked away from the desk, nearly knocking over a pile of printer paper with her huge rump before firmly walking out the door. I felt bad for it, but I couldn't help but ogle at her new round bubble butt the entire time."
    MCT "If this is how it's gonna be the rest of the year with her, I'm gonna be in for a mind-numbing time."
    "I finished up filing, and left through the library in order to prep for the rest of the day."
    jump daymenu
    
label AE012:
    $setProgress("AE", "AE013")
    scene Hallway with fade
    play music Rain
    "I strode through the halls, excited and ready to begin my day with Shiori-san, questions running through my head as I wondered what all I would get to learn."
    MC "Good day, Shiori-san!"
    show AE neutral-annoyed at center with dissolve
    AE "Hotsure-san? What's with that look? Your goofy smile is somewhat troubling."
    MC "Hah, it's nice to see you waiting for me; as usual."
    show AE neutral
    AE "...Of course."
    MC "Wanna head in?"
    AE "Mhm, you first."
    scene Office with fade
    MC "All right. Ready for another day."
    MCT "Yup, another day, another stack of papers."
    show AE neutral at center with dissolve
    AE "..."
    "However, today had a different air about it than the day before. There was a bit of anticipation, to be honest, because I could just feel as though I was going to learn something exciting."
    MC "So, how's about it? You promised you would answer any questions I have."
    AE "I certainly will."
    AE "Later. Until then, let's get to work."
    MC "Eh?"
    "I was so excited to start actually getting to know Shiori-san as a person that I forgot about work."
    hide AE with dissolve
    MCT "Okay. I'm ready. I just need to remember what I'm gonna ask so I don't look dumb. The big ones were sports, music, food. Okay."
    MCT "So, sports, music-ah, food club form, that goes in the left cabinet."
    MCT "Okay, got it. Just need to remember what all I want to ask, and then I'll know her better."
    "We worked, as usual, for minutes on end, throwing the occasional topic to one another. By the time we finished, we were already deep into a conversation once more."
    show AE happy at center with dissolve
    MC "-and the sight of it is just... Ngh..."
    AE "Really?"
    MC "H-hooo yeah. That's exactly why I hate peanut butter."
    AE "I must say, I have some eccentric tastes but... Hm..."
    "We had gotten done far earlier than expected. Surprisingly enough, it felt like Shiori-san had finished hers even earlier."
    MC "So, Shiori-san, you actually seemed to finish up quicker than usual."
    show AE neutral
    AE "Observant of you, Hotsure-san. It certainly seems that way."
    MC "You need to work on your pacing, young lady!"
    AE "Indeed. Which means that we can begin. You had questions, yes?"
    MCT "Ah, so that's the sound of a joke getting eviscerated."
    MC "Oh, yeah definitely... So, do you have everything... prepared, I guess?"
    AE "Yes. I have everything prepared."
    MC "Okay..."
    play music AE
    jump AE012_menu

label AE012_menu:
    menu:
        "Favorite activity?" if not getFlag("AE012_activity"):
            $setFlag ("AE012_activity")
            jump AE012_activity
        "Favorite activity? (disabled)" if getFlag("AE012_activity"):
            pass
        "Life goals?" if not getFlag("AE012_goals"):
            $setFlag ("AE012_goals")
            jump AE012_goals
        "Life goals? (disabled)" if getFlag("AE012_goals"):
            pass
        "Food?" if not getFlag("AE012_food"):
            $setFlag ("AE012_food")
            jump AE012_food
        "Food? (disabled)" if getFlag("AE012_food"):
            pass
        "Favorite music?" if not getFlag("AE012_music"):
            $setFlag ("AE012_music")
            jump AE012_music
        "Favorite music? (disabled)" if getFlag("AE012_music"):
            pass
        "Favorite sport?" if not getFlag("AE012_sports"):
            $setFlag ("AE012_sports")
            jump AE012_sports
        "Favorite sport? (disabled)" if getFlag("AE012_sports"):
            pass
        "That's everything...":
            jump AE012_after
            
label AE012_activity:
    MC "What is your favorite activity?"
    show AE neutral
    AE "Outside of class?"
    MC "T-That's a given, yes."
    show AE glasses-2
    AE "Things that let me test my knowledge, I suppose. I tend to read when I can."
    AE "A hobby of mine is to study the laws of different nations around the world."
    MC "Ah, sounds... fun."
    MC "That's it?"
    show AE neutral
    AE "I suppose so."
    jump AE012_menu
    
label AE012_goals:
    MC "Let's talk about goals. What do you want to do after school?"
    show AE neutral-annoyed
    AE "..."
    show AE sad
    "Shiori-san looked down for a moment to ponder my question."
    show AE neutral
    AE "I want to be a lawyer."
    MCT "Knew it."
    MC "Figures, yeah."
    show AE neutral-annoyed
    AE "Hmph."
    show AE neutral
    MC "I'm guessing prosecution? I mean, you could do defense if you want, but-"
    show AE angry
    "Before I could finish, Shiori-sans eyes turned to me like ice cold daggers."
    AE "I'm sorry to interrupt, but can we change the subject please?"
    MC "O-Oh. Okay."
    MCT "Yeesh. Did I hit a sore spot?"
    jump AE012_menu
    
label AE012_food:
    MC "T-The food club form goes in the left cabinet."
    show AE neutral
    AE "..."
    MC "..."
    AE "W-"
    MC "What is your favorite food?"
    "We sat there in silence for a moment. Shiori-san looked at me with confusion and concern, before finally resolving to just answer the question."
    AE "I like German food."
    MC "Really? Now that's interesting!"
    AE "Is it?"
    MCT "I... I think so?"
    jump AE012_menu
    
label AE012_music:
    MC "What is your favorite genre of music?"
    AE "I tend to listen to liturgical music."
    MC "Um... L-Literu...?"
    show AE neutral-annoyed
    AE "...Classical. Just go with classical."
    MC "Ah, there we go."
    MCT "Why didn't she just say that first?"
    MC "Is that the only genre you'll listen to, or...?"
    show AE neutral
    AE "No, I also like piano music, as well as organ works."
    MC "Never would've figured you had a taste in western music."
    AE "Mhm."
    MCT "Yes! That's something."
    jump AE012_menu
    
label AE012_sports:
    MC "How about sports?"
    show AE neutral
    AE "None."
    MCT "And my hopes of wooing her with my few actual skills has been dashed."
    MC "O-Oh, really?"
    AE "Hmm... Kendo I suppose."
    MC "Oh, Kendo? Nice."
    AE "Mhm, it's one of the few sports I enjoy watching for long periods of time."
    jump AE012_menu

label AE012_after:
    MCT "Well, I think I got everything I wanted to ask about her."
    "While I'd been somewhat excited for the day where I could learn more about Shiori-san, that excitement had been dashed when I learned something somewhat disheartening."
    MCT "She's not really that boring or anything it's just... nothing abnormal. She has her eccentricities, but all in all she's just kind of what I would have expected. A typical busybody in every sense of the word."
    show AE neutral
    AE "I'm sensing some disappointment."
    show AE neutral-smug
    AE "Looking for something you couldn't find?"
    MC "Huh? N-no, I'm not... disappointed."
    show AE neutral
    AE "Good. So, now that you know about me, I have some questions for you."
    MC "Eh?"
    "Shiori-san pulled out notecards from her breast pocket, and tapped them on the desk."
    AE "Shall we begin?"
    MC "H-hold on, begin?"
    AE "I have some questions for you as well."
    MCT "So that's why she took so long to prepare!"
    AE "Now, shall we?"
    MC "Uh..."
    "I was caught off guard. I wasn't sure how to respond outside of some small stammers of protest."
    AE "First. Why do you want to spend time with me? Hasn't this been getting boring to you?"
    "Sitting in the chair, there was little I could do aside from just shrug and purse my lips."
    MC "Because I like hanging out with you, I guess. You're cool."
    show AE neutral-annoyed
    AE "How so? As far as I know there's never been that much considered 'cool' about me."
    MCT "Your presence maybe."
    MC "I don't know what to tell you. I just consider you an interesting person to spend time with."
    show AE neutral
    AE "Hmm... And the work? Does it seem repetitive?"
    MC "Well, I guess, yeah. But I figure it's nice spending time here. It's helping me grow as a person."
    show AE glasses-2
    AE "Yes... I know you said that, it's just... I suppose your responsibility is something I didn't expect."
    "Shiori-san took her notecard and flipped it to the back, bringing forth the next one in the row."
    show AE neutral
    AE "All right then. When you refer to me, you use -san, yet instead of calling me Matsumoto-san, you use first name basis. Why is that?"
    MC "Eh?"
    MCT "Actually, to be honest I hadn't thought of that."
    MC "Well, um, I guess it's because I consider you to be close enough to me to use first names, but since you're... y'know, the president and all that, it's polite to use -san."
    AE "I see..."
    MC "Do you not like it? I can start calling you Matsumoto-san if-"
    show AE embarrassed
    AE "N-No, no, it's fine."
    "Shiori-san was about to move to the next card when she hesitated. She then, out of the blue, decided to put them down. Taking a deep breath."
    show AE neutral-annoyed
    AE "Let's just get to the point. My main question for you is 'why are you so curious about my interests?'"
    MC "It's good to know about your friends right?"
    MCT "Ah."
    MCT "I think I let that one slip."
    show AE surprised
    AE "...Friends?"
    MC "Well... yeah."
    show AE aroused
    AE "I'm... your friend?"
    MC "I mean... we spend a lot of time together and stuff so... Yeah."
    if getAffection("AE") >= 5:
        AE "Friend... Hm."
        "Shiori-san adjusted her glasses, clearly not wholly sure how to take what I just said."
        AE "Well..."
        show AE happy
        AE "Thank you, Hotsure-san. I..."
        show AE embarrassed
        AE "Hm. Friends..."
        "Something seemed to brighten up in the room. Shiori-sans usually imposing presence felt less severe; it felt like a weight lifting off my shoulders."
    else:
        show AE surprised
        AE "Hotsure-san..."
        "Shiori-san seemed somewhat confused by the statement, taking it upon herself to avoid eye contact for a moment while adjusting her glasses."
        show AE glasses
        AE "I appreciate the sentiment, Hotsure-san. Hopefully I can further assist you as a co-worker."
        "Though nothing that she said seemed malicious on the surface, it was the way she said it that formed a deep pit in my stomach."
        MCT "Did I just get coworker-zoned?!"
    MC "So... is that it?"
    show AE neutral
    AE "I suppose so, yes. Thank you."
    MC "All right, well, in any case, I'll see you tomorrow!"
    "I began to grab my bags and walk out the door when I heard Shiori-san speak up."
    show AE aroused-3
    AE "If... If you are becoming bored with our meetings-"
    MC "O-oh, no, it's okay! I'm perfectly fine just working files."
    show AE neutral
    AE "Well... in any case, I... Hmm... Meet me outside the office next time. Okay?"
    MC "Huh? What for?"
    AE "Well... I suppose you deserve a bit of variety. Plus, it will be helpful for you to see some of the other functions of the student government."
    MC "Other functions?"
    show AE glasses-2
    AE "Yes. Simply wait for me by the door."
    MC "Oh, okay. Cool. Well, I'll see you then."
    show AE neutral
    AE "Yes, 'see you then'."
    "I walked out of the office without a clue of what Shiori-san was talking about, but in my mind, any change of pace was a good one. Admittedly though, I came in with plenty of questions and left with plenty more."
    jump daymenu
    
label AE013:
    $setProgress("AE", "AE014")
    #FIXME character positioning probably needs work?
    scene Hallway with fade
    play music Busy
    "I walked down the halls to my destination, still anticipating what exactly it was Shiori-san had in mind from the other day."
    "As I walked, I saw posters of a smiling anthropomorphic seed, holding out it's fingers in a peace sign. The picture was accompanied with a message in bright, bubbly hiragana."
    "*Don't wait! Apply for refitting today!*"
    MC "Huh, well it looks like they finally got around to putting up the posters."
    AE "N-Not quite."
    MC "Eh?"
    "As I looked up to the source of the voice, I saw Shiori-san, standing on her toes while reaching up to apply a poster to an empty wall."
    show AE neutral-annoyed at center with dissolve
    MC "S-shiori-san? What's going on up there?"
    AE "Well as you can see, I, nghf... am setting up posters for the refitting, as was discussed earlier."
    show AE neutral
    MC "Oh! So you all finally... yeah, you got a design."
    AE "Mhm, though it was more of the design accepted by the entire council."
    MC "So you're just setting up for today?"
    AE "Yes. Although, it's more so that {i}we're{/i} setting up for today."
    MC "Ahhh, okay, I see. So this is what was planned for today."
    AE "Mhm, now, if you please, could you grab those stacks over there and move the ladder when I get down."
    MC "Alight, sure."
    hide AE with dissolve
    "Taking the stacks in my hands, I lifted them up as Shiori-san plastered the posters across the walls. This continued for a few minutes, with small talk breaking up the monotony every once in a while."
    show AE neutral at center with dissolve
    MC "Well, hey, you were right. Being the president of the student government, really does have a lot to do, eh? Files and posters."
    show AE neutral-annoyed
    AE "Hmpf, well, I'm sure you'll get to appreciate it full hand when you get into a management job at some point."
    MC "Nahh, management isn't really what I'm shooting for."
    show AE neutral
    AE "Really? Well then what are you planning? After school, that is."
    MC "Architect."
    show AE surprised
    AE "I... honestly didn't expect that response."
    MC "Why's that?"
    show AE neutral
    AE "It's just... that's far more certain than I'd expected from you."
    MC "I can be unambiguous sometimes. I like architecture, not much to it."
    AE "Hmm... I see. Never figured you as an architect."
    MC "Ehhh, well, it's not exactly a given... You though, phew, I can see you going places."
    show AE sad-2
    AE "..."
    "Shiori-san quieted up a bit more. At that moment, I started to get a bit of a feeling that Shiori-san is uncomfortable with discussing occupations."
    show AE neutral-annoyed
    AE "If I can admit something to you, Hotsure-san, this is my least favorite part of my position."
    MC "Um... Putting up signs? I mean, you're a bit short so..."
    show AE angry
    AE "That's not what I meant."
    MCT "Eep. Point taken."
    show AE neutral-annoyed
    AE "I mean... I mean putting a faux happy spin on things such as this."
    MCT "A faux..."
    MC "Oh, you mean with the posters?"
    show AE neutral
    AE "Well, yes, however the... gaudy design is merely a symptom of a greater problem with the general mentality about these sort of things."
    MC "Greater mentality? I'm sorry, you kinda lost me there. I mean, I kinda like the posters."
    AE "Hmm... It's hard to put in the most accurate terms..."
    show AE neutral-annoyed
    AE "In essence, I think it's unfortunate that people need to digest information with a spectacle. The idea that something needs to be 'cute' or have some sort of friendly overtone in order to get people to do things."
    MC "Oh."
    show AE neutral
    AE "Yes, and... and I feel like in this setting it's more concerning than anywhere else."
    MC "Here? How so?"
    AE "Well, I suppose that this sort of place is a bit more serious than the school wants to let on. By all accords this place is for people with clinical conditions, and as such the school body needs to treat this all in a, well, clinical manner."
    MC "Well... I get what you're saying but... I don't think I agree."
    AE "Oh? What do you think?"
    MC "I agree, yeah, it is a clinical situation that needs to be taken seriously; but it's because it's such a serious matter that we need to put a bright spin on things to keep people's spirits up. I mean, even you'd agree that people who are happier are more efficient, right?"
    show AE neutral-annoyed
    AE "In this particular situation, it's not about efficiency, it's about common decency."
    MC "Either way, we all just gotta do what we can to keep people's hopes up."
    show AE angry
    AE "I apologize, Hotsure-san, however I don't find value in stamping happy face stickers on caskets."
    MC "Isn't that analogy a bit much?"
    show AE neutral
    AE "Mmm, perhaps, but I got my point across. I prefer a harsh reality to a comforting fantasy. It makes things easier to assess and easier to fix."
    if getSkill("Academics") > 5:
        MC "So long as you're not building a harsh fantasy in its stead."
        AE "...Fair."
    "We continued to work after that somewhat strange discussion, until we ran into a particularly high area."
    MC "Woah... Looks like we'll need more than a stepladder for this. Or, y'know, I could get on and we could swap positions."
    show AE neutral-annoyed
    AE "Hmm... No. Putting you on top of this ladder would put you at risk."
    MC "Eh? Well, putting you on top would put you at risk, AND make it so you can't reach."
    show AE sad
    "Shiori-san bit her thumbnail once more, and began to contemplate a possible solution while closing her eyes."
    AE "If we get Yamasaki-san... No... No, she's in the garden. I wouldn't want to use her condition for my gain."
    MCT "Wouldn't want to...? Really? I would have never..."
    AE "Hmm... equilibrium. If the ladder has mass on the bottom to counteract the weight on top, then the ladder will keep stable."
    "Shiori-san took her thumb away and opened her eyes."
    show AE neutral
    AE "Hotsure-san. I have a proposition for you."
    MC "Huh? Yeah?"
    AE "Stand on the ladder while I get on the top."
    MC "U-um... Shiori-san? It's not that I want to rebel against your plans or anything but... wouldn't that mean I was..."
    AE "...Yes?"
    MC "Right beneath your skirt?"
    show AE embarrassed
    AE "..."
    "Shiori-san bristled a bit, bashfully moving one leg to keep her mind off of it."
    show AE aroused-3
    AE "I... I can trust you won't look at my... posterior as I'm working."
    MC "No, I definitely won't."
    show AE neutral
    AE "Okay... Good. Well... Get on."
    "As Shiori-san climbed the ladder, my eyes went directly to her posterior. Because of course they did."
    "Could I really help myself though? No. Shiori-san's butt was tantalizingly close to my face. And her beautiful legs..."
    show AE embarrassed
    AE "Eep! Hotsure-san?!"
    MC "Don't worry, I'm just grabbing your waist for support."
    show AE aroused
    AE "O-oh. Smart idea."
    MCT "W-what?! That was an actual concern!"
    hide AE with dissolve
    "All was going well. I was holding Shiori-san up as she reached for the wall space. But that's when it happened."
    MC "Shiori-san, w-wait, I-"
    show AE aroused-3 with vpunch
    stop music
    AE "W-woah!"
    MC "A-I got you!"
    "From my point of view, all I saw was Shiori-san's pillowy mounds push out towards my face, seemingly swelling out as the back of her head faded from my view as she bent over; the fabric of her skirt being the last thing I see as her butt collided with my face. I fell flat on my back on the tile floor below, head missing the floor by about... not at all."
    show AE surprised
    AE "Oh dear god."
    MC "Ahk-ahw, dammit, ugh..."
    show AE sad
    AE "Hotsure-san, I am so sorry! A-are you all right?!"
    "Shiori-san walked her way down the stepladder to get to me, it wasn't that big of a fall, but it was more of landing directly on my back that knocked the wind out of me."
    show AE neutral-annoyed
    AE "Nggh, why did I do that-why did I think that was a good idea."
    MC "It's okay, Shiori-san, I'm all right! I was the one who offered to hold your-"
    AE "But I shouldn't have accepted."
    MC "N-no. It's okay."
    MCT "The view was fine till I hit the floor."
    show AE sad-2
    AE "Here, let me help you up."
    "Shiori-san worriedly reached her hand out to me, grasping my own as I hopped to my feet."
    AE "Are you sure you aren't hurt? I can refer you to the nurse."
    MC "I'm telling you, I'm fine! It's all right."
    AE "A-all right. If you say so. Ach, here, you have... dirt all over..."
    "Shiori-san swiftly began to brush the back of my back before, unknowingly I'm sure, began to pat the rear of my pants."
    MC "U-um, hey!"
    show AE embarrassed
    AE "O-oh! Right, sorry, just let me..."
    MCT "Pat, pat, pat."
    AE "There."
    MC "All right... Well, that was embarrassing."
    "I scratched the back of my head, chuckling to myself as Shiori-san continued her concerned gaze."
    MC "Welp, now that that's over, let's get back to work."
    show AE neutral-annoyed
    AE "Oh no, you are staying on the ground and carrying the papers."
    MC "I'm telling you Shiori-san, it's okay."
    "I turned around and grabbed the stepladder, getting ready to move on to the next empty space. Not noticing as Shiori-sans face went from a look of worry to a look of shock and anger. That's when she did something I didn't expect."
    show AE angry
    MC "W-woah, hey!"
    "Shiori-san buried a hand in my hair and felt the back of my head."
    MC "Woah, woah, what was that about...?"
    MCT "What is she looking at?"
    "Shiori-san looked at her hand, a quick look of alarm shooting across her face."
    show AE neutral-annoyed
    play music Tension
    AE "Like hell you're okay!"
    MC "Huh, what?"
    "She held her finger out to me when I noticed..."
    MCT "...Blood?"
    AE "P-put the papers down and go to the nurse, now!"
    MC "Ehh?! But, I didn't even hit my head that ha-"
    AE "No excuses!"
    "Shiori-san grabbed my hand, and I felt each tiny tremble ripple throughout her shaky arms."
    scene Nurse Office with fade
    show AE sad-2 at center with dissolve
    "I sat on the small, cushioned bench, paper crinkling beneath my pants as I shifted position. Shiori-san had spent a good five minutes washing and sanitizing her hands as we waited; eventually sitting down next to me and holding my hand, despite my protests that I was fine."
    "After a brief intermission, the nurse walked back in, a woman with long painted fingernails which clacked with every errant movement on her clipboard."
    Nurse "Okay, Hotsure-san, I did a double check on your medical history and the likelihood you have a concussion is minor."
    AE "Nurse, I would like to inform you that I was the one who-"
    MC "Decided to bring me straight here."
    show AE surprised
    AE "...W-Hotsure-san you-"
    play music Hallway
    Nurse "Well, it was a kind gesture, Matsumoto-san, however it seems as though it wasn't necessary."
    show AE neutral-annoyed
    AE "N-not necessary? He was bleeding from the impact point."
    Nurse "Hotsure-san, I actually have the perfect solution for you."
    "The nurse reached into her bag and grabbed a bottle of shampoo. The bottle had the school logo on it with a man in a shower."
    MC "Um... ma'am?"
    Nurse "I'm guessing you scratch your head a lot, son?"
    MC "Well... Yeah."
    "The nurse gave a soft wink."
    Nurse "It's scalp treatment shampoo. It doesn't flake up, so you don't have to worry about scabs."
    show AE sad-2
    AE "S-scabs?"
    Nurse "Mhm, it seems as though he scratched the back of his head, opening up a scab from showering."
    MC "E-eh?"
    Nurse "Look, see my nails? Whenever I wash, I make sure the edges are rounded so I don't cut my head up. From the looks of it, you've got some sharp nails yourself."
    MC "O-Oh."
    "I darted a look over to Shiori-san, who was looking on incredulously."
    MC "Okay ma'am, thank you, I will."
    Nurse "All right, have a good day. Oh, and tell your girlfriend that she's very loving."
    show AE surprised
    AE "Wha-"
    MC "Gnk-"
    Nurse "Mhnhnhn, have a good day."
    "The door creaked closed, the fogged glass blocking view to the inside."
    show AE embarrassed
    AE "H-hold on, I-I believe you've made an error in assessment!"
    MC "..."
    AE "U-um..."
    "Shiori-san straightened up a bit more before adjusting her glasses."
    show AE glasses-2
    AE "In the diagnosis, that is. You-you're still not in the clear yet. I want you to go to your dorm and take a rest. Then... Then I'll see you again tomorrow. When you're healed."
    MC "Shio-"
    "Before I could say anything more, Shiori-san walked away bashfully, rear swinging as she walked. I blew air out of my mouth and rested my back against the wall."
    hide AE with dissolve
    MC "Mhn... Girlfriend..."
    MCT "Welp, I oughta get heading back, Daichi is probably going to interrogate me about why I was at the nurse's office."
    "I cracked my neck and walked to my dorm, rubbing my neck the way back."
    jump daymenu

label AE014:
    $setProgress("AE", "AE015")
    scene Hallway with fade
    play music Hallway
    "I walked over to the library doors to begin another day of work with Shiori. Newly printed posters adorned the halls, as well as the doors themselves."
    MCT "Yeesh, she really got to work after yesterday, didn't she?"
    "I opened the library door, but this time I noticed something strange. It only opened part of the way before jamming."
    MCT "Eh? What's..."
    "A slight push. Nothing. A greater push. Once more, nothing."
    MC "Okay. You know what, I think I'm good for today."
    "I turned around and began to walk back to my dorm. Mind swimming with what all I was going to do today."
    stop music
    scene black with fade
    pause 1
    scene Hallway
    play music Busy
    MC "RAGH!!"
    "With all the swiftness of the wind kami at my back, I ran forward and punted the door with my knee. The door swung open with a loud creak."
    MC "*Pant* *Pant* Hah! I win..."
    "I looked down in time to notice the dolly with a cabinet on it sitting in front of the door."
    MC "Oh! ...Oh."
    MCT "And the door..."
    "The door had a two inch scratch in the wood finish near the base."
    MC "Mch... M'kay. Yep. I'll just..."
    MCT "I'll just wipe this off aaaan- okay, I made it bigger. I'll just... just... yeah."
    "I left it alone for the moment, wanting to flee the scene. I fled said scene by entering the office; a move similar to entering the police station to escape a bank heist."
    scene Office with fade
    MC "H-Hey, Shiori-san, did you see that someone-ohp, woah."
    "I nearly ran face first into a wall of drawers."
    MC "Eh?"
    MCT "Is... Is this punishment for what I did to your kin?"
    "I gave a deep bow."
    MCT "I'm sorry."
    AE "Hotsure-san? I assume that's you, yes?"
    MC "Um... Yeah, Shiori-san."
    MCT "D-Did she not hear the cabinet fall?!"
    AE "Good, good, I'm over here, behind the cabinets."
    MCT "You're gonna need to be a lil bit more specific there."
    MC "Oh, I don't really see you, um..."
    AE "No? Okay, over by the window, near the far end of the wall."
    MC "Ah! There you are! Finally."
    show AE embarrassed at center with dissolve
    "I was greeted with the usually upright and taut Shiori-san now appearing cramped and mousy between a cavalry of black metal drawers."
    MC "Hey, Shiori-san."
    AE "Hotsure-san, good evening. I'd get up to bow, but as you can see, I'm not exactly in a suitable position."
    "I looked around to admire the sheer magnitude of the junk in the room. It's surprisingly fun to have a room you're so used to change like that."
    MC "I guess. What's with all of the tables and cabinets and stuff?"
    show AE neutral-annoyed
    AE "Despite my protests, administration is temporarily utilizing the office for storage."
    play sound Thud
    "*THUNK*"
    MC "Ach-Couldn't they find anywhere else?! I can barely move in here."
    AE "Be thankful you're not in my position at least. I can't move without getting, ngh, stuck every few steps."
    "Shiori-san went to walk forward, but found that doing so sandwiched her vast hips between two cabinets. She let out a sigh of exasperation before beginning to scoot her way out."
    MC "Oh! Here, if you want, I can-"
    show AE embarrassed
    AE "No, no, I can do it."
    "With hands on both cabinets, she pressed on, trying to free herself from the tight squeeze."
    show AE aroused-3
    AE "Hggggn-UH!"
    "With a ungraceful tug, she freed herself, sending her bulbous derriere into a wobbling fit before a quick movement of her hips subsided it."
    show AE angry
    AE "Confounded-! Nggh..."
    MC "Do you want to move up front?"
    show AE neutral-annoyed
    AE "That would be a pleasure, if it weren't for the fact that my table hadn't been moved to accommodate the space. The one time I {i}do{/i} want Mizutani-san to lift tables about..."
    MC "Well... Let's get to work, I guess."
    AE "Simply unacceptable... Yes. That will get my mind off of this."
    "We worked together like usual, with the caveat being the metallic labyrinth that I needed to navigate just to get to the correct folders. Shiori-san went to move her arm, and winced in pain as her funny bone was jolted by the edge of a cabinet."
    show AE neutral
    AE "Hotsure-san, can you get that stray file? It should be on top of the third shelf."
    MCT "Oh, the one at the very top?! Where I've hit my head 4 times?!"
    MC "Sure."
    "I stretched up to reach it, yet it eluded my grasp slightly."
    show AE neutral-annoyed
    AE "Ugh, no. The drama club budget sheet needs to be on the lower shelf."
    "Shiori-san got up and walked over to my general location. Seems as though she needed the lower cabinet."
    MC "H-hey, Shiori-san, yo-"
    "I moved my hips back."
    show AE aroused-3
    AE "Wait, I just have to..."
    "She, however, misjudged. And while trying to squeeze out..."
    show AE surprised
    stop music
    AE "A-ah!"
    MC "Woah!"
    "Squeezed her backside right up against my crotch."
    MC "Wooooah, okay. Um."
    show AE embarrassed
    play music Steamy
    AE "..."
    MCT "Oh god, oh man, oh god, oh man, oh god, oh man."
    MC "I-it's okay, um, s-should I scooch out of the way or?"
    AE "No, no, let me, I-"
    "Shiori-san tried to perk up and squish her way out, but it only drove her cheeks deeper into my groin."
    MC "Okay, that's not really-"
    show AE aroused-3
    AE "Helping-"
    MC "Yeah, no, um..."
    MCT "Damn, this is bad. I gotta get out of this or else... Ahnnn, I can feel her through my... C'mon, c'mon c'mon!"
    "I could feel my heart begin to race. My palms began to sweat as I started blushing deeply."
    MCT "Oh man, if I keep this up I'm gonna-"
    show AE embarrassed
    AE "H-hold on, let me try..."
    MC "A-ah!"
    MCT "OKAY, OKAY, NOW IT HURTS. I WANNA GET OFF THIS WILD RIDE."
    MC "NNNNNGGHGH."
    "With what little room I had, I slid my hips out from the side, finally escaping the awkward and intense butt-squish heaven and hell."
    MC "Okay! All right... I, uh, g-got it."
    "Shiori-san's face was in a deep shock, before slowly turning to a solemn sadness."
    show AE sad
    AE "I'm sorry."
    MC "Oh, no! I'm sorry, I shouldn't have been... I-it's really inappropriate of me."
    show AE sad-2
    AE "I take full responsibility for this."
    MC "W-well... it's fine. I'll make sure it won't happen again."
    AE "Yes. I'm sorry."
    MCT "Wow... She's really beat up about this."
    MC "Don't worry too much about it..."
    "I turned around and continued to work, attempting to alleviate the tension in the room without success."
    MC "Um... I hope I didn't make that super awkward or anything."
    show AE sad
    AE "No, no, it's quite all right. I apologize for pressing my bottom against your handbook."
    MC "It's oka-"
    MCT "Huh?"
    MC "Handbook? My student handbook?"
    show AE sad-2
    AE "Yes. I'm sorry."
    MCT "Eh? I left my handbook at the do-"
    MCT "..."
    MC "Yeah, it's okay. Don't worry about my handbook."
    MCT "If I tell her it wasn't my handbook she'll flip."
    show AE sad
    AE "How could I not? The student handbook is a symbol of rights and school diction, and I besmirched it by... rubbing it against my unmentionables!"
    MCT "On second thought. It'd probably be best if I told her it wasn't."
    show AE sad-2
    AE "Sincerely. Accept my apology to both you and to your symbol of the school!"
    MCT "She gave me an equivalent to a standing lap dance without desire or warning and the first thing she thinks about is apologizing to the school?!"
    MC "Hey, hey! I said it was okay."
    AE "V-very well then."
    "We continued to work a bit longer, but not a word was said between us. We worked in silence for another 30 or so minutes before Shiori-san spoke up."
    show AE embarrassed
    AE "Well, um, I suppose that should be enough for today. Hopefully by tomorrow this... mess will all be cleared up."
    MCT "I can only hope."
    MC "Okay, well, see you next time."
    show AE sad-2
    AE "Next time, then... I'm sorry."
    MCT "Oh brother."
    hide AE with dissolve
    "Shiori-san quickly strode out of the office, muttering to herself along the way. I let out a sigh of relief. The scene replaying in my mind as-"
    show AE angry at center with dissolve
    AE "Who scratched the library door?!"
    MCT "..."
    jump daymenu

label AE015:
    $setProgress("AE", "AE016")
    scene Hallway with fade
    "As I walked down the halls, my mind kept flashing back to yesterday's incident. Specifically, my mind travelled more towards the worry that Shiori-san may have realized by now that it wasn't my pocketbook she was rubbing up against."
    MCT "I am NOT looking forward to having to work in such a cramped environment again."
    "I tried to convince myself pathetically, with a smile on my face and less than innocent thoughts running through my head. I headed towards the old wood door, wary of any possible obstructions."
    MC "I hope they got the door scratch fixed."
    "I looked at a blue post-it note on the side of the handle."
    "{i}Please open door GENTLY.{/i}"
    MC "Oh good."
    "I pushed the door open without problem this time, and made my way through the empty library."
    scene Office with fade
    play music Busy
    "As I walked into the office, I was greeted with an unbroken wall of black-iron filing cabinets, sitting there menacingly. And in the middle of two cabinets..."
    MC "..."
    MCT "S-Shiori-san?!"
    "More specifically, the poor girl's rear and two legs stuck between the cabinets. She was lifted slightly off of the ground by the table, her thick thighs pitifully kicking in resistance."
    MCT "O-Oh no! Shiori-san's been captured!"
    AE "Oh god... Mnf..."
    MCT "W-What's gonna happen to her? Is she gonna be eaten and turned into paper? Is she going to become one of the cabinets?!"
    "It took every ounce of my mental fortitude not to start cackling like a hyena."
    AE "*Nngh* *Nnnnff*"
    $setVar("AE015_watch", 0)
    jump AE015_menu

label AE015_menu:
    menu:
        "Watch her a little longer." if getVar("AE015_watch") < 10:
            $setVar("AE015_watch", getVar("AE015_watch") + 1)
            jump AE015_watch
        "Watch her a little longer. (disabled)" if getVar("AE015_watch") >= 10:
            pass
        "Help her out.":
            jump AE015_aftermenu

label AE015_watch:
    if getVar("AE015_watch") == 3:
        "I couldn't help but stare on at Shiori-san as she began to try and wiggle out, eyes fixed on her round rear as her hips shook more frequently."
        AE "Hoooah... W-wait... Nggggnn~!"
        "I pulled up a chair and sat down, with pursed lips and hands resting lightly on my abdomen as I watched on."
        AE "Ach-H-hold on... nhg."
        jump AE015_menu
    if getVar("AE015_watch") == 6:
        "I rested my feet up on the table, watching with intent as Shiori-san continued her struggle."
        MCT "It's like watching an adorable trainwreck."
        AE "Are you-ach- k-kidding me?!"
        jump AE015_menu
    if getVar("AE015_watch") == 9:
        "I continuously watched as sweat began to form along the seat of Shiori-san's skirt."
        AE "*Pant*... *Pant*... Hng... Hnnnnn~."
        "I opened up my backpack and pulled out a bag of shrimp flavored popcorn chips. I slowly began to much on the treat as sadistically and smugly as I possibly could."
        AE "H-huh? Hello? Is that shrimp? What's happening?!"
        MC "...*Munch*"
        MCT "Y'know, I should probably help her... or just wait for some students to walk by for end of the day cleaning."
        jump AE015_menu
    if getVar("AE015_watch") == 10:
        MCT "She's stopped kicking now. It's w-oh, no, there she goes again."
        "I watched on, bag of popcorn now empty, as a twinge of sympathy began to set in."
        MCT "All right, now I'm getting bored, plus I'm starting to feel bad."
        jump AE015_menu
    else:
        MCT "I... I'm gonna see how this plays out. I'm sure she'll get out eventually."
        "I watched a little longer as Shiori-san kicked her massive legs up and down, her thighs wobbling like mad and her skirt swishing from side to side as she struggled in vain."
        AE "*Pant* *Pant* Hggnnn."
        jump AE015_menu

label AE015_aftermenu:
    if getVar("AE015_watch") >= 9 and getSkill("Academics") > 3:
        $setAffection("AE", 2)
        MCT "Oh, wait, hang on."
        "For subtleties sake, I snuck out of the room, then out of the library before making a show of entering again and making loud footsteps as I entered the office."
        MC "Huuh? What's going on here!?"
        AE "Oh... *pant*... Oh thank heavens."
        MCT "Nice."
    MC "U-um, Shiori-san?"
    AE "H-Hotsure-san? Is that you?"
    MC "Y-yeah, Shiori-san, I just got here. Are you stuck?"
    AE "Um... Y-yes."
    MC "Here, let me help."
    "I walked behind Shiori-san and put both hands on her hips as I began to tug."
    AE "W-Wait, Hotsure-san, isn't there a better way?"
    MC "One, two..."
    "I positioned my own legs in a way that would allow for greater force."
    MC "Three!"
    "With a quick tug, I pulled Shiori-san free from the cabinets. Once free, the two of us both collapsed to the floor, the force from dislodging her pushing us back."
    show AE aroused-3 at center with dissolve
    play music Schoolday
    AE "Nhg..."
    MC "Ayah... Y-you all right?"
    "I looked at Shiori-san, her raven hair spread out on the ground, and gave a slight chuckle. Shiori-san opened her eyes, and looked at my face before sitting up and rubbing the side of her head."
    show AE embarrassed
    AE "Y-yes. Thank you."
    MC "No problem."
    "Shiori-san's face was cherry red, and there was a light moisture around her eyes."
    MC "You look like you were a couple of seconds away from screaming your head off!"
    show AE neutral-annoyed
    AE "Come now, Hotsure-san, I have more composure than that."
    "I sprung up and stood straight, stretching my back until I heard a pop from my spine. Shiori-san sat cross legged, before grabbing onto the side of a table and slowly lifting herself up."
    show AE embarrassed
    AE "M-mnph."
    MC "Oh, do you ne-"
    show AE neutral
    AE "No, no, I can get up."
    "Her arms wobbled as she pulled the weight of her large behind from the ground; before finally standing up straight in the doorway."
    show AE sad-2
    AE "Hooo, okay. Wow."
    MC "So... What happened?"
    AE "I, uh, whoo... *ahem*"
    "Shiori-san straightened up, regaining her posture as she positioned her glasses."
    MCT "Her and those loose glasses."
    show AE glasses-2
    AE "I was making an attempt to retrieve some supplies from the room... As it turns out my reach is nowhere near what I would hope for."
    MC "I'd say..."
    "I looked around the inside of the room. It was full of black metal filing cabinets from the door to the back wall."
    MC "So..."
    "I looked to Shiori-san with a slight grin."
    MC "Wanna get to work now?"
    show AE aroused-3
    AE "I'm not looking to have a repeat of the... incident from the other day."
    MC "P-Please don't bring it up."
    show AE neutral
    AE "I already have. I gave administration a full account when trying to convince them to remove the extra cabinets."
    MCT "Th-this unbelievable girl is going to get me suspended! Can we please change topics!?"
    MC "Wait, you talked to administration?"
    show AE neutral
    AE "Yes."
    "Shiori-san rested one hand on her hip, letting the other hand stay at the side of her body as she shifted her weight."
    show AE neutral
    AE "I'm not usually one to go against the decisions of the administration, however I made an effort recently to have these removed from the office."
    "I took one last exaggerated look around the office room from the doorway."
    MC "Oh... I can see it turned out well."
    show AE neutral-annoyed
    AE "No, actually. In fact the administration said that they were planning on keeping the supplies here..."
    show AE angry
    extend " For the next few days..."
    show AE sad
    extend " In which time I won't be able to access the cabinets."
    show AE sad
    "Shiori-san took her thumb nail between her teeth as she stared at the mess of iron filling the room."
    MC "So then, what are you planning on doing?"
    show AE neutral
    AE "I would usually spend any spare time monitoring the halls, so I suppose that's a good place to start."
    "Shiori-san, grabbed her books, which had been lying on a drawer adjacent."
    AE "We'll pick up work within a few days. Until then, I'll be seeing you in class. Have a good day."
    "She walked past me and began to head towards the library door."
    MC "Hey, Shiori-san, wait."
    AE "Hm? Is everything all right?"
    MC "W-well, yeah, but..."
    "I scratched the back of my head, causing Shiori-san to let out a sigh in exasperation."
    show AE neutral-annoyed
    AE "Have you been shampooing correctly?"
    "She pointed an accusatory finger at me while placing a balled hand on her hip."
    show AE angry
    AE "I don't want you getting any more cuts on the head. Proper scalp health is vital to-"
    MCT "My mind began to wander a bit as she talked, looking directly into her eyes and nodding every few seconds. My memory was pulled back to a specific statement that the nurse said... and I gave a light smile."
    MC "Do you wanna spend some time together?"
    show AE neutral-annoyed
    AE "Further mo-"
    show AE neutral
    extend " ...hm?"
    "Shiori-san let her hand slip from her hip, her finger no longer straightened as she absorbed what I had said."
    MC "We may not be working, but I think we should spend some time together outside of class."
    "We stood there in silence for a moment."
    show AE neutral-annoyed
    AE "W-Well, um, I don't see any reason why, it's not beneficial to your development..."
    MC "Well, no, but I think it would be nice to hang out together outside of work. We could relax a bit together."
    show AE neutral
    AE "Relax?"
    "Shiori-san thought to herself a moment, glancing between her feet and myself."
    AE "That... It won't be necessary. We don't really..."
    MC "It'll be fun."
    menu:
        "We can make it your choice what we do.":
            jump AE015_c1
        "It'd be nice to let you loosen up a bit.":
            jump AE015_c2

label AE015_c1:
    $setAffection("AE", 2)
    MC "If you want, we can do whatever you want to do."
    AE "Whatever I want?"
    "Shiori-san stood there, eyes twitching as she contemplated what we could possibly do together."
    AE "Hmm... I see. I'll... keep the possibility in mind. Do you truly trust me to pick something enjoyable?"
    MC "W-well, yeah."
    AE "Hm. Well, thank you."
    jump AE015_afterchoice

label AE015_c2:
    $setAffection("AE", -2)
    MC "I think it would be nice to help you get out of this stuffy office for a bit. It would help you loosen up."
    show AE surprised
    "Shiori-san seemed a bit taken aback by the words 'loosen up'. She thought to herself a moment before looking to me through severe eyes."
    show AE neutral-annoyed
    AE "Well, I so happen to like my 'stuffy' office. It's an environment that lets me achieve peak performance."
    MC "Really? I mean, can anybody really like-?"
    show AE angry
    AE "I certainly do. Or is that not 'loose' enough for you?"
    MCT "Yikes. Wrong call."
    jump AE015_afterchoice

label AE015_afterchoice:
    show AE neutral
    AE "...Still, though. It would be nice to do something outside of office work with you... It could allow me to see how you behave in a... non-formal setting."
    AE "Very well then, Hotsure-san, we will spend time together. Free time."
    MC "All right! It's a date."
    show AE surprised
    AE "...W-what?"
    MC "Oh! Uh, a hangout date. I-It's an expression."
    show AE aroused-3
    AE "Ah, yes. Expressions! And... hm. S-See you then."
    MC "See you."
    "Shiori-san was halfway out of the door before stopping and poking her head in to speak to me again."
    show AE neutral
    AE "Oh, um, about where we'll go."
    MC "Y-yeah?"
    AE "Follow me after class. I will lead us."
    MC "Okay."
    hide AE
    "With that, Shiori-san left. I stood around in the library for a moment before speaking up to myself."
    MC "It's a date... tch, c'mon, man."
    "I let out a sigh of audible exasperation before opening up the door myself and heading out to the dorms, ready to continue the rest of my day."
    jump daymenu

label AE016:
    $setProgress("AE", "AE017")
    scene Hallway with fade
    show AE neutral at center with dissolve
    play music Rain
    "Today was the day I said I would meet Shiori-san outside of the office. I was somewhat excited for a bit, this was the first day we would actually be able to spend time one on one without working."
    "I got up and followed Shiori-san once class ended. Where, as promised, she lead me to where we would spend time today."
    AE "Well, here we are."
    "We came to a stop in front of an old wooden door."
    "A familiar old wooden door."
    MC "...Eh?"
    MCT "This is..."
    scene Library with fade
    show AE neutral at center with dissolve
    MCT "The library? Really?"
    MC "U-um... the library?"
    AE "Yes. It's a good place to spend time, no?"
    "Shiori-san looked at me expectantly, confusion clearly plastered on my face."
    MC "W-well, I mean... weren't we gonna go out and talk or...?"
    AE "Oh. Well, I assumed that you would've wanted to go somewhere like the library. It's quiet, no-one is around, and we can talk uninterrupted. Is there somewhere else?"
    MCT "..."
    MCT "Oooohh, I think I see. She's shy about just going out with me in public. She doesn't want people to get the wrong idea. Okay, I understand now."
    MC "Oh, uh, no this is fine."
    AE "Good."
    AE "Then, please, take a seat."
    "I grabbed one of the large chairs and pulled it across the floor to the table."
    show AE neutral-annoyed
    AE "Please don't drag the chairs."
    MC "Eh? Oh."
    "I picked up a chair and put it beside the table."
    show AE neutral
    AE "There. Best not to scratch the floors. I'll be right back."
    MC "Huh? Okay, but what are-"
    hide AE
    "Shiori san walked away and headed over to a small box near the door of the office; one which had until now escaped my notice. With papers in her hand, she walked over to the table and sat across from me."
    show AE neutral at center with dissolve
    AE "All right. That should do it."
    MC "W-Huh? Shiori-san what-"
    MCT "Oh. Oh I get it."
    MCT "She wasn't shy about going outside with me, she just wanted to get some work done in the library."
    MC "Um... Shiori-san?"
    AE "Hm?"
    MC "What's with the papers?"
    AE "Oh, just some things to pass the time. I hoped we could look over these to knock some things off of my to do list, seeing as how today is a day we aren't in the office."
    MCT "As expected. She can't help herself."
    MCT "I gotta try and tear her away from work for even a second."
    menu:
        "Give her a random topic":
            jump AE016_c1
        "Ask her to stop":
            jump AE016_c2
        "Offer to help":
            jump AE016_after

label AE016_c1:
    MCT "I should try and give her an interesting topic. That way she will get immersed in the discussion."
    MC "Well, uhh, did you know that a student slipped on the saliva from Tashi-sensei's tongue?"
    AE "Yes. I had to do the paperwork involved in the incident."
    MC "Heh, I figured."
    AE "..."
    MC "..."
    "The silence was like agony as I desperately wanted at least some form of acknowledgement."
    MCT "Of course. Think of something else"
    MC "D-um... I went over to... Uh..."
    AE "Please. Don't mind me, continue."
    MCT "I'd be more than happy to. AS SOON AS YOU PUT DOWN THE PAPERS!"
    MCT "Okay, this isn't working. Well, I guess she is, but that's the problem. She's a workaholic. Maybe if I... Hmm."
    jump AE016_after

label AE016_c2:
    MC "Um, hey, Shiori-san?"
    show AE sad-2
    "Shiori-san looked up to me, clearly sensing something in my tone I didn't mean to convey."
    MC "Do you wanna talk or am I just... you know, bothering you?"
    "Shiori-san looked at her papers a second before quickly looking back at me."
    show AE sad
    AE "Oh. Is this... is this rude, Hotsure-san? I'm sorry, I didn't mean to..."
    MCT "Aw man, the look in those eyes seem really disheartening. I can't just make her stop like that."
    MC "N-no, no, it's fine! I mean... you can keep working."
    show AE neutral
    AE "Well, good then."
    "Shiori-san looked back to the papers, leaving me to just sit there, running my hand across the back of my neck."
    MCT "Okay, this isn't working. Well, I guess she is, but that's the problem. She's a workaholic. Maybe if I... hmm."
    jump AE016_after

label AE016_after:
    MC "Sooo..."
    show AE neutral
    AE "Hm? Yes?"
    MC "What are those?"
    play music Schoolday
    AE "These are all request forms submitted by students who have concerns for the Student Government."
    MC "Oh."
    MCT "Student Government here has request forms? Huh..."
    MC "I'm gonna be honest with you, I didn't know we had a request form."
    AE "Of course. The school values feedback from the students, thankfully. These forms are a way to get things done that the students believe need to be handled."
    MC "So, how often do you get those?"
    AE "Hm?"
    MC "You know, the forms, how many do you get?"
    AE "It depends, but so far around twenty or so a week, they're submitted to a box outside of the office and Student Government reads them at the end of every school week."
    MCT "Twenty or so a week?! Jeez, I didn't realize people here were so needy."
    MC "Well, let's take a look!"
    AE "...You want to help?"
    MC "Well, sure. Unless it's against the rules..."
    MCT "Nice wording."
    AE "Hmm... It's not. All right, have a look."
    MCT "All right! That's a step in the right direction."
    "Shiori-san got up and walked over to my side of the table, papers under her arms. She sat down beside me, splaying the papers out in a row. She picked one up and read it aloud."
    AE "'Install sound devices in the girls restroom.'"
    AE "Hm. I like this one. Water expenditures here are abysmal as is, so installing sound devices should help."
    MC "Eh? How would a sound device cut on water?"
    show AE embarrassed
    AE "Clearly you know nothing of female toilet etiquette."
    MCT "...What?!"
    show AE neutral
    AE "What's this one?"
    show AE neutral-annoyed
    AE "'Matsuro-san's breath is bad, please expel him.'"
    "We sat in silence for a moment, a blank expression being the only accompaniment to my seething confusion."
    MC "O-oy! That one isn't a real request is it?!"
    show AE angry
    AE "For the sake of my sanity, I assume not."
    "Lightly, she took the paper and creased the paper in the middle, placing it gently to the side. She picked up another."
    show AE neutral
    AE "'Stop making me button up my shirt.'"
    "Another crease."
    AE "No."
    MCT "I'm 70%% sure that's Mizutani-san's handwriting."
    show AE angry
    AE "'Satoru-sensei is-' nggh."
    "And another."
    MC "Jeez what's with these dumb requests?!"
    show AE neutral-annoyed
    AE "It's par for the course. It was the same as in my previous school."
    MC "Well, is there any way to... I guess cull the requests so there are only serious ones?"
    show AE neutral
    AE "That's what we're doing right now."
    "For a moment, I forgot I wasn't a member of the student government; what with all the work I'd been doing. It hadn't dawned on me that I wasn't approving anything, just looking over it."
    MC "Well, no, I mean like to even be able to submit one."
    AE "Ah, I see. No, there shouldn't be."
    "I recoiled a bit. That was one of the more unexpected things I've heard from Shiori-san in a while."
    MC "Huh, bu-"
    AE "Everyone deserves the right to have their voice heard, no matter how puerile it may be."
    MCT "Huh... Who would've thought."
    MC "I didn't take you as such an advocate for free speech."
    show AE neutral-annoyed
    AE "I'm an advocate for whatever rights the school allows its students."
    MCT "Thaaat's more what I expected."
    show AE neutral
    AE "The simple answer is just to take the serious requests into mind and discard the ones that aren't."
    MC "Huh... All right."
    AE "Mhm. Come on. Let's look through these."
    hide AE with dissolve
    "Within a few minutes, we went through all twenty two requests. In the end, we only came up with seven legitimate concerns. But my mind wasn't on that for the moment, because the air in the room had changed."
    show AE happy at center with dissolve
    MC "And my sister, my sister, she would always flush the toilet all the time too, and you're saying it's because... pffft-ehehehe."
    "My chuckle was seemingly contagious, as even Shiori-san gave a little smile of amusement."
    AE "Precisely. And that must have drone your father up a wall for water bills."
    MC "Mm- No, actually, my mom."
    show AE neutral
    AE "Really?"
    MC "Yep, mom was the breadwinner of the house. Dad was just a manager at a convenience store."
    AE "Ah, really? "
    MC "Yep... So, uh... What about you? Do you ever flush the toilet constantly?"
    show AE aroused-3
    AE "H-hey now! That's not a question to ask the class president!"
    MC "HAH! Ahaha!"
    show AE angry-2
    AE "D-w-mhn..."
    MC "Ah, man. Hey, you know I'm just playing. Wouldn't want to drive your old man up the walls with bills, eh?"
    show AE glasses
    AE "...No. No, I certainly wouldn't."
    MC "..."
    show AE embarrassed
    AE "I didn't waste water at my house. I was a very conscientious girl."
    MC "Oh! Yeah, true, I can see that."
    "We sat in silence for a short moment before I spoke up."
    MC "Uh, heh heh, uh... Man, I've been really loud the past few minutes haven't I."
    show AE neutral-smug
    AE "Yes, yes, I know. You've managed to cause enough ruckus in the library."
    MC "Well, you're the one who chose it! There's no one around."
    show AE neutral
    AE "Well yes... However, if you've noticed, I've been keeping my voice at a respectable level."
    MC "Eh, true, true."
    "I leaned back in my chair and put my hands over my abdomen. Letting out a sigh of relief."
    MC "Haaahn... Boy, I'm tired."
    AE "Indeed."
    "Shiori-san stood up and put the papers, both full and creased under her arm."
    AE "Well, I suppose we've spent a good amount of time together today. We certainly should... do this again. The outside of work aspect."
    MC "Oh! Yeah, yeah, any time."
    show AE happy
    AE "Good. Well, I'll see you tomorrow then."
    "Shiori-san bowed, and turned around. As she began to walk away, almost as a compulsion, I asked her straight."
    MC "Do you wanna eat lunch with me?"
    show AE neutral
    AE "...Hm?"
    MC "Mw-Well, like... maybe we could get lunch together."
    "Shiori-san stood there for a moment. Looking off to the side with pursed lips. There was an audible inhale as she began to speak."
    AE "Um... Yes. Yes, I'd like that."
    "My only response was a goofy grin and a small scoff."
    MC "Okay, cool. Later?"
    AE "Later, yes. See you later."
    MC "Yeah, later."
    "Shiori-san walked out of the room, her rear bouncing with a light wobble with every step. Strangely enough, I hadn't noticed her ass the entire time we were together, when before I at least took sort glances. I adjusted myself in the chair, before closing my eyes and exhaling a deep breath; an indication of my planning for the rest of the day."
    jump daymenu

label AE017:
    $setProgress("AE", "AE018")
    scene Cafeteria with fade
    play music Busy
    "After lessons had ended, I walked out of the room. I was going to walk out with Shiori-san, like with yesterday, but a student came up addressing her as \"ma'am\" so I assumed she had further business. I got up and walked over to the cafeteria to get in line and grab some food."
    MCT "I hope everything is all right. I should grab us a table just in case, that way she'll know I was waiting for her."
    "Looking at the selections, it seemed as though the school had a wide variety of different foods and drinks available, definitely more than I'd seen before."
    MC "Uaaah, look at all this stuff."
    MCT "Hmm... I think I'll just go with the Rice and Chicken."
    "I grabbed a bowl and began to fill it up in the self-serve area; taking a few small strawberries as a little dessert. After grabbing some chopsticks, I went to look for a place to sit."
    MCT "Hmm... Let's see... Where can I sit where Shiori-san and I-"
    "Almost to answer my own question, I caught a glimpse of the spectacled girl looking at me over a small partition."
    MCT "Oh! Oh, she's here already."
    "I went to walk over to where Shiori-san sat, and when I turned the corner I saw her talking to a short girl with large pouty lips."
    show AE neutral-annoyed at center with dissolve
    AE "-and after that, I want you to tell her to get her forms in on time if she cares so much. Good? All right, good."
    show AE angry
    "The girl walked in the other direction as I continued to walk over to where Shiori-san sat, her hands massaging the sides of her temples."
    MC "Hey, you came!"
    show AE neutral
    "Shiori-san looked up from her hands, quietly putting them back down to her sides."
    AE "Well, I said I would, didn't I?"
    MC "Yeah, I just didn't see you in line."
    AE "I got here fairly early."
    MCT "How did she get here so fast though?!"
    MC "Ah, should have figured."
    "I sat down at the bench and immediately began to sink in the plush cushions."
    MC "Huh, the cushions on these benches are really soft."
    MC "In fact, these benches are pretty wide too."
    AE "Well, I'd suppose they'd have to be."
    MC "Oh, yeah, because... Yeah."
    "Shiori-san looked at me softly while I mulled around. Patting the sides of the bench, I decided to ask about what happened."
    MC "So what was that about? With the girl?"
    show AE glasses-2
    AE "The art club head has been late with her forms again, I simply told Yuki-san to deliver a message."
    MC "A-ah, okay."
    "I twiddled my fingers a bit before reaching over and grabbing my chopsticks."
    MC "Welp, let's eat!"
    show AE neutral
    AE "Hm."
    "Shiori-san took hers as well and we began to dig in. Her tray seemed fairly tame; rice, noodles, carrots, and a single piece of strange desert, already half eaten."
    MC "What's that?"
    AE "It's a dough pastry with Hakuto jelly. It's strange, I tried it a while back and I can't get enough of it."
    MC "Well, can I try a bite?"
    "Shiori-san looked at me for a moment, before taking the plate the pastry was on and passing it over to me."
    AE "Go ahead."
    MC "Thanks."
    "I bit into it, and was greeted with a tangy and sweet gush of peach flavored jelly."
    MC "Mmmn~  That's great!"
    AE "It seems like we have common tastes then. Good."
    MC "Yeah, I love peach stuff."
    "As I took a few more bites of the pastry, I figured it would be a good idea to share some of my food with her."
    MC "Oh!"
    "I picked up a strawberry, nearly dropping it for a moment."
    MC "I got some strawberries. Want some?"
    AE "Oh, well I-"
    MC "Here."
    "I reached over the table and put it in front of her expectantly waiting. She stared at the small red thing as she slowly began to turn the same shade."
    show AE aroused-3
    AE "U-um... I'm not sure it's appropriate to..."
    MC "Eh?"
    "I looked over at a pair of girls snickering adjacent, when I finally realized what I was doing."
    MC "Oh! Oh, yeah, sorry. Don't wanna give people the wrong... Yeah."
    "I placed it on her tray gently, sitting back down as I stared at her. It was interesting watching her. The soft and subtle movements of her body when she changes emotions is cute."
    MC "Sooo..."
    show AE neutral
    AE "Hm?"
    MC "Isn't it kind of strange for there to be a full cafeteria here?"
    AE "What do you mean?"
    MC "I mean, it's a bit of an abnormality at this level of schooling."
    AE "Well, I suppose the board figured that it would be better to provide lunches for the students, rather than leaving it to them to bring their own."
    MC "Yeah, it kinda feels like middle school again."
    AE "Do you feel like that's a bad thing?"
    MC "Hmmm..."
    MC "Well, no, to be honest. I'm glad we have a cafeteria."
    extend " Why? Do you?"
    show AE neutral-annoyed
    AE "There are some things I feel the school needs to change for the sake of maturity."
    MC "Ehhh, I dunno. Seeking maturity for the sake of just 'being mature' can often get in the way of stuff getting done."
    show AE neutral
    AE "True. And I suppose it is necessary for students with more... voracious tendencies."
    MC "Hm? Oh, do you mean the, uh, students who're gaining weight or...?"
    AE "Strictly speaking, yes. They tend to consume far more than it's believed they can bring, so it's for the best that the school provides for them."
    "My mind flashed to Nikumaru-san, as I began to doubt the part about 'far more than they can bring'."
    AE "Besides, if we're going to bring up 'non-conventional' methods, have you noticed something about the shoe lockers?"
    MC "Shoe lockers...?"
    MCT "Shoe lockers... I haven't really used them... Wait."
    MC "Oh! We don't have any."
    show AE glasses-2
    AE "Precisely. I'm not the only one who noticed either, I found Yamazaki-san walking around in her socks first day looking for a place to put her shoes."
    MC "I mean... I didn't think it was as big of a deal."
    show AE neutral-annoyed
    AE "Because you haven't had to clean the floors when they're covered in mud yet; a problem which you almost contributed to a while back."
    MC "Oh yeah... Man, that must be a whole lot of extra work."
    AE "Undoubtedly."
    show AE angry
    AE "I tell you, it may work fine for now, but when the rainy days really start, that's when administration will regret not installing them."
    MC "Hmn..."
    extend " Y-know i-"
    stop music
    "As I began to speak, I moved my hand over my tray, accidentally putting my hand on some of the peach-filling from the pastry."
    MC "Ohp..."
    show AE neutral
    AE "Oh, I-"
    MC "It's all right, I can get a napkin..."
    "I reached over to the dispenser on the end of the table, but I ended up putting my hand in an empty slot."
    MC "Napkin... eh... There are no napkins."
    MCT "Shiori-san would kill me if I just wiped it off on my school uniform, let alone the bench."
    MC "A-Ah well. I can get it later."
    AE "..."
    MC "So, like I was saying, I actually used to forget my shoes at the door of my house all the time."
    "Shiori-san seemed only tangentially focused on me, her eyes changing focus from my own to the mess on my hand."
    show AE neutral-annoyed
    AE "..."
    MC "My mom got so mad at me, she made me deep wash the carpet whenever I... Um..."
    show AE angry
    AE "..."
    MC "Hey S-"
    "Without warning, Shiori-san grabbed a handkerchief from her shirt and grabbed my hand. She began to rub the spot with the jelly clean, looking intently at my hands as she did. I couldn't really do anything aside from look on in confusion; same with the group of friends next to us who watched on."
    "She finished wiping my hand, gently moving it about with her own soft and delicate hands before she was satisfied."
    play music Busy
    show AE happy
    AE "There. Clean."
    MC "..."
    AE "I apologize for the intrusion. Please, go on."
    MC "U-uh... Yeah."
    MCT "What the hell was that?!"
    MC "Uhh... W-well I, aha... Um... Is everything all right?"
    show AE neutral
    AE "It's fine."
    MC "...Okay."
    MCT "I shouldn't question it. If I do I'll probably get an aneurysm."
    MC "But, uh... mom! Yeah, yeah, she would often have me deep wash the carpet until I learned to put my shoes in the cubby. Needless to say, I washed the carpet until I left."
    AE "As a soccer player?"
    MC "E-he-yup."
    show AE neutral-annoyed
    AE "Your poor mother."
    MC "Oy, oy! It sucked, I spent a solid forty minutes a day just cleaning the floors!"
    show AE neutral-smug
    AE "And that, Hotsure-san..."
    "Shiori-san grabbed the strawberry from her tray and put it to her mouth."
    show AE happy
    AE "Is good parenting."
    "She popped it in, satisfied smirk on her face as she began to chuckle in amusement. I rolled my eyes and scoffed at the ridiculous girl in front of me."
    show AE neutral
    AE "Mmhn. I suppose we need to get heading back, the cafeteria is emptying."
    "We stood up as Shiori-san dabbed her mouth with her handkerchief; the jelly from my hand on the other side."
    "I looked back at the bench where Shiori-san sat. She told me she was there a while, but from the looks of it she'd been waiting for me the entire time. There was a massive indent where she sat, creating a crater that could fit about two people."
    AE "Hotsure-san, are you coming?"
    MC "Y-yeah! I'll be right there."
    jump daymenu
    
label AE018:
    $setProgress("AE", "AE019")
    scene Hallway with fade
    play music Hallway
    "I sat at the windowsill waiting. My feet dangling just slightly off of the floor as I kicked them back and forth. Looking down at them, I was given a slight tunnel vision from my own black locks dangling down a few inches from my face. I looked up to the ceiling, inhaling and letting out a low gust of air from my lips. As I looked back forward, I saw a familiar face slowly heading up the stairs."
    MC "Oy, Shiori-san."
    show AE happy at center with dissolve
    AE "Oh, good, Hotsure-san y-"
    "Shiori-san's face swiftly changed to one of concern."
    show AE angry
    AE "H-hey, off the window sill. Off it now."
    MC "Hm?"
    MC "Um... okay?"
    "I hopped down in time to catch Shiori-san walking over swiftly to look out the window."
    show AE neutral-annoyed
    AE "Be careful. That's a long drop from here."
    MC "Long drop? Shiori-san the window's-"
    show AE neutral
    "Before I could continue, Shiori-san looked at me with an expressionless face as she lightly pushed the window, causing it to swing open at the side. She raised a single eyebrow."
    MC "...Latched."
    AE "And you just so happened to find the one window that isn't."
    "Shiori-san let out a light sigh, and put her hands on her hips."
    show AE neutral-smug
    AE "Such a helpless young man. I'm glad I've been supervising you."
    MC "O-oy, oy!"
    AE "Hm?"
    MCT "..."
    MC "Th-thank you, Shiori-san."
    "Shiori-san stood up a little taller, a light blush crossing her face as she looked away and brushed her hair to the side."
    show AE embarrassed
    AE "Y-you don't need to thank me, Hotsure-san... Looking out for your wellbeing is what's expected of me."
    MCT "Eheh, she gets so cute when she's bashful."
    MC "So, Shiori-san, why did you want me to wait for you up here?"
    show AE neutral
    AE "Mm, well, I was making my rounds for monitoring the halls when I decided that we could maybe spend a little time somewhere else."
    MC "Okay, cool. Where at?"
    AE "Follow me."
    "I did as Shiori-san said and followed behind as we climbed the stairs. Though it was subconsciously, I followed a bit closer than was necessary."
    "I looked up the whole time at Shiori-san's tush as we climbed, eyes fixated on the side to side movements of her skirt with every wobble and bounce of her derriere."
    "We climbed for a bit more until we reached our destination."
    MC "Oh, you wanted to go to the roof?"
    AE "Mhm. It's nice up here. Not a lot of people, nice, cool air, and a great view."
    MC "All right, cool."
    scene Roof with fade
    "Shiori-san opened the doors, and a nice gust of air swept into the doorway. It was fairly strong, and almost instantly as the wind picked up, Shiori-san's skirt was lifted a few inches as well; giving me a brief view of her behind, squeezed tightly by white panties, before she pulled her skirt back down. Shiori-san cleared her throat."
    show AE embarrassed at center with dissolve
    AE "Ah, I apologize."
    MC "Oh, no, it's okay."
    MCT "Nose, I swear, if you bleed on me now..."
    "As we walked out onto the gravelly roofing, the sun brightly gleamed in my eyes as I heard the birds around us chirp while they fluttered away to a nearby ledge."
    MC "Oh, wow, it's really nice out today."
    show AE happy
    AE "I agree. It's a bit warm, but the wind is soothing."
    "We looked around for a place to sit, before coming across a lone metal bench."
    MC "Ah, there we go."
    show AE embarrassed
    AE "..."
    MCT "Hm?"
    MC "What's up?"
    show AE aroused
    AE "I-it's nothing."
    "Shiori-san sat down on the double wide bench, with me sitting beside her. We sat in contemplation for a moment, taking in the surroundings."
    MC "Haaaahn~"
    show AE neutral
    AE "..."
    extend "Hotsure-san, do you hear that?"
    play sound Bird
    MC "Hm?"
    AE "That bird."
    play sound Bird
    MC "Oh, yeah, it sounds nice."
    show AE happy
    AE "Mhm... It's a Siberian Rubythroat. They're native to the area."
    MC "Hm? Really?"
    AE "Yes. Many northern birds find their way over here."
    MC "Huh, that's nice... How did you know that?"
    AE "Ah, well, I heard it a while ago and looked up the native bird species. I referenced the bird with the image and found an article about them."
    MC "Ahh."
    AE "Mhm..."
    "We sat there in silence for a bit longer. We looked out towards the distant horizon, a few grassy mountains rising over the landscape, slowly fading to blue as it gave way to the far ocean, and the ocean to the sky."
    MC "I wonder... I wonder how far the horizon really is."
    show AE neutral
    AE "..."
    show AE sad-2
    AE "I've never thought to ask that..."
    MCT "How far the horizon is..."
    MC "Hey, Shiori-san, I have a question for you?"
    show AE neutral
    AE "Hm?"
    MC "How often do you dream?"
    show AE sad-2
    AE "...That's a strange question to ask."
    MC "Ehe, I figured, but I wanted to know... Do you ever have any recurring dreams?"
    AE "..."
    "Shiori-san's face crinkled up a bit as she thought, hands tapping her thighs as she put the tongue on the inside of her cheek and looked away."
    show AE embarrassed
    AE "I... suppose. Why?"
    MC "I've been having this weird dream lately... and I've been wondering what it means."
    show AE neutral
    AE "What it means...?"
    MC "W-what?"
    show AE neutral-annoyed
    AE "Well... Why does it need to 'mean' anything?"
    MC "I mean... I dunno. I guess it's just that our dreams are like a look into our minds is all."
    show AE sad-2
    AE "W- ...a look into...?"
    "Shiori-san looked at me with a look of confusion."
    AE "I don't mean to be... off-putting... but how can you prove that?"
    MC "Well... I don't know. There are some things that you just can't prove, right?"
    show AE embarrassed
    AE "With enough proper research I-I assume we can know everything there is to know... However, yes, some things naturally can't really be proven or disproven."
    MC "Exactly. It's a matter of faith in the idea."
    show AE neutral-annoyed
    AE "Tch-it has nothing to do with faith, it's about an unproven field of psychoanalysis."
    show AE angry
    AE "Don't conflagrate faith with pseudoscience."
    MC "..."
    MCT "I struggled to bring back the entire memory of my dream, but only one piece of it sprang forth."
    show AE sad-2
    MC "I... I remember standing on a concrete island. There was a blue sky... and blue waves."
    AE "..."
    MC "I was standing in front of a concrete pillar with a red number on it... four, I think... I dunno."
    show AE neutral
    AE "Oh... well... Is that all?"
    MC "Yeah, I think so."
    AE "How very... insightful?"
    "I looked over at Shiori-san expectantly."
    MC "Well?"
    AE "Hm?"
    MC "What do you think it means."
    show AE neutral-annoyed
    AE "Oh, come on now."
    MC "I think it's about my desire for strength and support in an unknown situation."
    show AE neutral-smug
    AE "I think it's about someone who needs more sleep and less caffeine."
    MCT "Hmm, she's not really getting it."
    MC "All right... Tell me yours."
    show AE neutral-annoyed
    AE "Come now, Hotsure-san, don't be foolish."
    MC "Hey, I told you mine."
    AE "Without my consent or desire."
    "I put on a cute face and spoke in a slow tone."
    MC "Come on, Shiori-san, pleeease~?"
    show AE aroused-3
    AE "Begging... Really?"
    "Shiori-san let out a sigh of defeat. She put her hand on her chin and rested it against her knee."
    show AE neutral
    AE "Well... In my dreams, I often see myself climbing a set of white stairs in an old concrete stairway of some kind. I get to the top, and I find myself atop of what I assume to be a tall building."
    MC "..."
    AE "There isn't any light... only fog. The only thing I can see is a blinking red light in the distance."
    AE "Is that what you wanted to hear?"
    MC "You want to know what I think?"
    show AE neutral-annoyed
    AE "You're going to tell me anyway, go ahead."

    if getSkill("Academics") < 2:
        MC "I think... it represents your fear of heights."
        show AE neutral-smug
        AE "Hmm... Do you know what I see?"
        MC "What?"
        show AE angry
        AE "I see a young man, struggling in vain to find answers from a futile source."
        MCT "Oookay, welp, I walked right into that one."
        MC "I mean... am I a little close?"
        show AE neutral
        AE "...Hotsure-san, where are we right now?"
        MC "Um... Seichou?"
        AE "No, no, currently."
        MC "The roof?"
        AE "Why?"
        MC "You wanted us to me--"
        MCT "Oh."
        show AE neutral-smug
        AE "And the roof is...?"
        MC "Okay, okay, I get it, yeesh."
        AE "You're the Sigmund Freud of dream analysis, Hotsure-san."
    elif getSkill("Academics") > 2 and getSkill("Academics") < 4:
        MC "I think... you subconsciously believe that you're lonely."
        show AE neutral
        AE "..."
        MC "You stand alone. At the top, but alone. It's signifying a deeper fear of alienation."
        show AE neutral-annoyed
        AE "Oh, w-, enough of this nonsense, Hotsure-san."
        MC "Huh?"
        AE "I'll have you know that I don't feel lonely. I've plenty of company, includi--"
        MC "Student council doesn't count."
        show AE sad-2
        AE "..."
        AE "Including you."
        MC "..."
        play sound Bird
        "We stood there, the sounds of the wind carrying with it the chirping of the birds."
        MC "W-... Thank you, Shiori-san."
    elif getSkill("Academics") >= 4:
        MC "I think... that you're worried about your future."
        show AE neutral-annoyed
        AE "...What?"
        MC "Your vision of the horizon, of the top, is completely clouded by fog."        
        MC "You let your fears of isolation completely stop you from being able to visualize a good future for yourself."
        show AE sad-2
        AE "...I... I feel we should stop."
        MC "O-oh, I'm sorry I didn't mean to-"
        AE "No, no, I... That was just a little off-putting, is all."
        MCT "I must have hit too hard with that."
    show AE neutral
    AE "Well... Now we at least know each other's dreams, whatever good that does."
    MCT "Eh, I can see I'm not gonna get through to her with the idea."
    MC "Mmm, well, it's nice to know what you think about."
    AE "Presumptively."
    "Shiori-san let out a grunt as she began to pick her body up. I sprung to my feet and offered a hand to help, but she waved her hand down signifying that she wished to do it on her own."
    show AE aroused-3
    AE "M-hrgn... Ahn... Got it."
    MC "All good?"
    show AE neutral
    AE "Yes, I..."
    "Shiori-san felt the back of her skirt, before shakily feeling under it."
    show AE neutral-annoyed
    AE "Oh lord."
    "While I couldn't see it all, I'm guessing by the red lines across her thighs that her butt had a bench-shaped pattern etched into the skin."
    show AE angry
    AE "Ugh, this is going to tingle for minutes on end."
    MC "A-ah."
    show AE neutral
    AE "Hmm... Well, it's been fun, Hotsure-san, however I must get going."
    MC "O-oh, yeah, okay."
    "Shiori-san turned around and walked towards the door, before turning around to talk to me."
    show AE aroused-4
    AE "If... If you ever want to come up here with me again... just flag me down."
    MC "Okay... can do."
    hide AE with dissolve
    "Shiori-san opened the door to the stairs and walked down, slowly disappearing from view."
    "I looked up at the blue sky above, and thought about all I learned from Shiori-san's dream. I closed my eyes, and thought about how to spend the rest of the day."
    jump daymenu

label AE019:
    $setProgress("AE", "AE020")
    scene Hallway with fade
    play music Peaceful
    "As I walked towards the library, basket under my arm, I was greeted by Shiori-san waiting patiently for me by the door. Standing straight, her glasses reflected the sun as she looked out the window towards the campus."
    MC "Shiori-san, hey!"
    "She turned to me and nodded with respect."
    show AE neutral at center with dissolve
    AE "Good day, Hotsure-san."
    MC "So, ready to hang out again?"
    AE "Yes. Where is it you wish to talk today?"
    MC "Mmm... I'm thinking by the sakura. You in?"
    show AE happy
    AE "Certainly."
    "We walked side by side, Shiori-san's hips creating a natural distance between the two of us as they swayed back and forth with every step."
    show AE neutral
    AE "Have your studies been progressing well?"
    MC "Huh? Oh, uh, yeah."
    AE "Mm."
    "Shiori-san looked down to the wicker basket in my arms, before looking up to me."
    AE "And the basket, are those books?"
    MC "Oh, ehe, no, no. I can show you when we get there."
    AE "...Very well."
    scene Campus Center with fade
    "We walked further until we opened the door to the school, a gust of wind breaking the stagnant air of the school's interior. We continued further, with few other people anywhere around at the time, walking along the pathway until we reached the old tree at the center of the campus."
    show AE neutral at center with dissolve
    AE "Is this the place?"
    MC "Yeah, nice and shaded. This seems like a good spot."
    show AE glasses-2
    AE "You've yet to explain for what, Hotsure-san."
    "I took the blanket from the basket and placed it down, and sat in a squat against the tree. Try as she might, Shiori-san couldn't help herself from making an audible *POMPH* as she sat down, not yet used to the magnitude of her swelling behind, and how much less distance she needed to cover when sitting on the ground."
    "Placing her own bag on the ground, she let out a contented sigh and began to wipe her glasses."
    show AE neutral
    AE "Hotsure-san, I hope you don't mind, but could you get my notebook from my bag? I was hoping to take some quick notes."
    MC "Sure thing."
    "The bag was a fairly simple one. It looked to be an older, worn out, leather, but it suited her well enough. Rooting around, I found an assortment of things; a collection of pencils, pens, a beaded necklace, some notecards, erasers, and finally, a small black notebook."
    MC "Here you go."
    AE "Many thanks."
    AE "So. The basket?"
    MC "Well, you're in a in a rush today."
    AE "Well, no more in a rush than anyone else kept in anticipation over a secret."
    MC "All right, all right."
    "I opened up the old wicker basket I brought from home and handed some of the food over to Shiori-san."
    MC "Here."
    AE "Hm?"
    MC "Onigiri."
    show AE aroused-4
    AE "Oh! Well... thank you."
    MC "You're... looking at it like you've never had onigiri before."
    "I was about to laugh to myself a bit before..."
    show AE neutral
    AE "No. Never."
    MC "Eh? W-what, you can't be serious, right?"
    AE "I assure you, Hotsure-san, I've never had it."
    MC "O-oh. Well, okay. First time for everything, right?"
    MCT "Seriously?! Who's never had Onigiri before?"
    "I watched as Shiori-san took a small bite of hers."
    show AE happy
    AE "Mmmph.~"
    MC "Good?"
    show AE neutral
    AE "Hm?"
    "Shiori-san quickly swallowed and dabbed her mouth with a napkin."
    show AE embarrassed
    AE "Y-yes. Thank you. I'm sorry for being so audible."
    MC "Ahhh, it's all right."
    MCT "Better pull one out myself, it's my mom's old recipe."
    MC "Ah, I never really like the nori. Lemme just-"
    show AE glasses
    "Shiori-san looked at me, and without a word I realized that flicking the seaweed away without care would have been a grave error."
    MC "Ooor not."
    show AE neutral
    "We sat, eating in silence a bit longer before I decided to lighten up the mood with a bit of small talk."
    MC "You look really nice today."
    show AE surprised
    AE "Begging your pardon?"
    MCT "Biiiit too strong with that one."
    MC "Oh. Uh, you look good."
    show AE aroused
    AE "O-oh..."
    "Shiori-san brushed her hair to the side with the back of her wrist."
    show AE happy
    AE "Well, um, thank you for that."
    "We sat for a bit longer, eating and staring out into the campus; the occasional meeting of the eye here and there. I looked at Shiori-san every once in a while, when she looked away. Her skirt was starting to ride up again, which meant that she was growing even larger. Fabric was pulled tightly over her hips, making it so she sat in a somewhat compact pose as she looked out at the view."
    MC "I really don't envy you, y'know."
    show AE neutral
    AE "Hm? What?"
    MC "Having your... y'know. Condition."
    show AE aroused-3
    AE "Oh."
    MC "Yeah. I mean, if I had your growth, I'm not sure how I'd handle it. You're really strong for being able to take it so well."
    show AE sad
    AE "...Hm."
    MC "O-oh, um, I didn't mean any offense."
    show AE neutral
    AE "Oh-no, no, none taken. I was merely thinking to myself."
    MC "About what?"
    if getAffection("AE") >= 6:
        AE "Well, admittedly..."
        "Shiori-san looked to me, a light smirk forming on the sides of her lips."
        show AE neutral-smug
        AE "How strange you'd look with my condition."
        MC "E-eeehhh?"
        "Shiori-san went back to nibbling at her onigiri, purposefully avoiding my eyes."
        MC "C'mon now, no need to give me the mental image!"
    else:
        AE "...Nothing in particular."
        MCT "Yeesh. That felt a bit cold."
    show AE neutral
    AE "Well, you're not growing out. That's a good thing."
    MC "I feel like it."
    show AE glasses
    "I couldn't tell if Shiori-san took exception to that; all she did was look over at me, glasses slipping as she re-adjusted them on her face."
    MC "Even with how big the school is I can't help but feel..."
    show AE neutral
    AE "Cramped?"
    MC "Yeah, Yeah! It's like a feeling of being too big for where you're at."
    AE "Well, I suppose we all have that then."
    MC "Heh. Yeah."
    "I looked at the pure white rice ball in my hand. It reminded me of home. My mind raced with memories of my previous life. The days of lazing about the house reading manga, the times when I would just walk around the city bored, the days with my friends all spending time together; playing soccer in the warm summer sun. My days of normality, dashed with a mere note."
    AE "Is something the matter?"
    "With only a few words, Shiori-san reminded me of my company; as well as the surroundings."
    MC "Hm?"
    AE "You're looking forlornly at the ground."
    MC "Oh. Uh."
    "I took a moment to speak, the words lingering on my lips with a fear of possible wording-error."
    MC "It's just... I've been feeling a bit of stress recently."
    AE "Stress? Do tell."
    MC "N-nah. It's nothing."
    AE "Mm-well, hardly sounds like 'nothing'."
    MCT "She doesn't relent, does she?"
    MCT "Nevermind. I might as well tell her."
    MC "I just feel like I have some nagging worries on my mind. I feel like... I have a bit of anxiety being here."
    AE "And why do you feel that way?"
    MC "Well, it's hard. I mean, I had friends and family back home. I miss them. I understand that it's for the best that I'm here but like..."
    MC "I sometimes think that maybe my condition isn't severe enough to warrant being here. I imagine what life would have been like if I wasn't REQUIRED to be here."
    AE "Mhm."
    MC "And it's like... you don't really know how to feel about that."
    "Shiori-san looked at me through squinted eyes, her chin resting lightly on the back of her hand. She nodded, and leaned in slightly, making an audible inhale as she started to speak."
    play music AE
    AE "Hotsure-san, your main concern is about what might have been, right?"
    MC "Well... Yeah, I guess so."
    AE "Mm. I want you to think of a road."
    MCT "A... road?"
    MC "Um... okay."
    AE "It splits into four paths. You go down one, not knowing precisely the location. You end up at the end and reach your destination, but what of the other paths?"
    MC "Well... I guess I would try to visit them again someday, to know for sure."
    show AE happy
    AE "Ah, the path of certainty. Admittedly I would do the same. But think of the metaphor itself for a moment. What we are talking about is time. We can go forward as far as we want, but we will never be able to truly go back."
    MC "That's for sure."
    show AE neutral
    AE "Time is like a series of spirals. It starts from a single instance of our birth and from there spirals into one event to another, leaving behind a tangent of what could have been."
    "I listened as Shiori-san spoke, and  noticed a softness in her eyes which I had never seen before."
    show AE happy
    AE "If we always worry about those tangents, or those things which might have been, then we cannot look into the reality in front of us. That which could have happened never did, and if it had you may still be there worrying about 'what might have been'; if you are still there at all."
    "The bell rang in the tower, indicating that break was over."
    show AE neutral
    AE "Ah, well, I suppose that class is about to begin. We will have to continue this talk later."
    "Shiori-san grabbed her notebook and tucked it lightly under her shoulder. Standing straight up to get ready to leave. In that moment, I had something I wanted to get off my chest. Something I wanted her to know."
    MC "Hey, Shiori-san. The path I took... I don't regret it."
    AE "..."
    show AE happy
    AE "That's good to hear, Keisuke san."
    menu:
        "Because it lead me to you.":
            jump AE019_c1_1
        "Because I have nothing to fear.":
            jump AE019_c1_2

label AE019_c1_1:
    MC "Because... Because it lead me to you."
    show AE aroused-4
    $setAffection("AE", 3)
    "Shiori-san perked up a bit, a slight blush overtaking her face. She took one hand and swept her hair to the side."
    show AE happy
    AE "Well... Your candor is very welcome... I suppose I am glad to be travelling with you, Hotsure-san. Come on now, let's not be late."
    jump daymenu

label AE019_c1_2:
    MC "Because you helped me realize I have nothing to fear."
    show AE sad-2
    $setAffection("AE", -1)
    "Shiori-san bristled ever so slightly. Appearing to swallow something, before giving me a light smile."
    show AE happy
    AE "Yes, Hotsure-san... You indeed have nothing to fear."
    jump daymenu

label AE020:
    scene Office with fade
    play music Hallway
    "As I walked into the office, I was greeted with Shiori-san, kneeling over in order to place some files in a cabinet, butt positioned directly in my line of sight. I looked to the side a moment, before moving over to her. She looked over towards me and gave a small smile."
    show AE happy at center with dissolve
    AE "Nice to see you, Hotsure-san."
    MC "Oy, Shiori-san!"
    MCT "That's weird... Isn't she usually in the desk?"
    MC "Oh... um, why are you just, uhh?"
    show AE neutral 
    AE "Care to elaborate?"
    MC "Well, you're usually sitting down while I file, don't you have any more documents or?"
    AE "Actually no, everything is filled out for today. We'll be filing together."
    MC "Oh! Aight, well then, let's get to work."
    "I took my place next to her, as she handed me half of her stack and I began the daily grind."
    MC "So, what compelled you to file today? Am I not pacing myself again?"
    AE "No, not precisely. It's just that I've run out of forms."
    MCT "A-already!?"
    MC "Woah... that's a first."
    show AE neutral-smug
    AE "Funny."
    show AE neutral
    AE "But in all seriousness, this means that after today, we will no longer be meeting for work."
    MC "...Oh."
    MCT "We won't... be meeting?"
    "I stood there in silence a bit, trying to figure out how to respond to what she said."
    MC "Well, what about the other jobs? Do you need help with those?"
    AE "Like I said a while ago, Hotsure-san, much of my work isn't open to the public. I was barely able to convince administration to let you to help me in the first place."
    MC "I thought you said it was easy."
    AE "..."
    "Shiori-san pushed up her glasses with her off hand."
    show AE glasses-2
    AE "Well, I suppose many things are easy on a relative scale."
    MC "I'll... I'll kind of miss doing this with you."
    show AE happy
    AE "You really do defy expectations, Hotsure-san."
    MC "How so?"
    AE "Let's be honest. How many students would actually want to help here, hm? Based on what I know about your personality, you certainly didn't seem like the type to want to work behind the scenes, but you certainly stepped up to the occasion."
    show AE neutral
    AE "As for why, I've still yet to truly figure out."
    MC "Shiori-chan, I thought I told you, it's because I want to be a responsible adult."
    show AE neutral-annoyed
    AE "...-chan?"
    MCT "!!!"
    MC "S-san. Sorry, slip of the tongue."
    show AE neutral
    AE "Hm."
    AE "Well, whatever the reason, you've certainly found a way to keep me on my toes. In fact, I've achieved so much progress in my work that I've been able to finish it all within my relatively short time here, including with our few days of laxity."
    MC "Wait... Speaking of which, the days before we started going for lunch and the like, you started finishing filling out forms way quicker."
    AE "Ah, so you did notice."
    MC "Yeah. It makes me wonder... how did you do that?"
    AE "I simply allotted more time to office work by doing what I need to do early in the morning. This means that I can spend more time to match your pace when filing."
    MC "Really... You've been doing all that?"
    AE "Yes. I've actually been working early on papers as well in order to make it so that you have something to do. In a way, you certainly have helped my increase work productivity."
    MC "Wow. Sorry for that. I didn't know me being here was causing stress."
    show AE happy
    AE "Sorry? Hotsure-san, I've been doing so of my own volition. In fact I enjoy your company."
    MC "Right, but you do a lot of work! Don't you spend time with anyone else?"
    show AE sad-2
    AE "...No, actually. Admittedly... I don't really have anyone else. Work and all that, not to mention my position and duties don't exactly endear me to anyone. It can get a bit lonely, for lack of a better term."
    MCT "No one? Like... at all?"
    MC "Well, you have me then! I guess. But, if you really wanted, you can try ways to get yourself out there."
    show AE neutral-smug
    AE "Oh? And how would you propose that?"
    MC "Well, I dunno, have you considered... maybe dating?"
    show AE neutral-annoyed
    AE "Not at all."
    MCT "Ouch... that was fast."
    MC "Really? Not even once?"
    AE "Why consider the unlikely? I acknowledge the fact I have an unattractive body, as well as an unlikeable personality, therefore it's unreasonable to assume I would try and find a partner."
    MC "Ahh, now c'mon."
    show AE neutral
    AE "Well, it's not like I'm missing out on anything, dating is frivolous endeavor."
    MC "Well, I say don't knock it till you've tried it!"
    "Shiori-san made a somewhat sly face towards me."
    show AE neutral-smug
    AE "Oh, so then you assume I haven't?"
    MC "Oh. Uh, well, have you?"
    show AE neutral
    AE "..."
    "Her slyness quickly subsided to her usual coldness."
    AE "Well, no, but it's not nice to assume."
    MCT "Pfft. Oh lord."
    AE "What I said still stands though. Our concepts of love at this age are pointless, and based on hormonal reaction rather than calculated thought. I am simply not fit for 'dating' because I'm not fit for any person's desire."
    MC "Again with that! Geez, don't be so hard on yourself!"
    MC "I'd love to date you."
    stop music fadeout 0
    show AE surprised
    AE "..."
    MC "..."
    MCT "..."
    "Silence hung in the air. Shiori-san looked at me for what felt like eternity as I felt my stomach become 5 pounds lighter."
    show AE neutral-annoyed
    AE "What did you just say?"
    MCT "Uhn..."
    MC "Ach, wa- a- I, uh."
    show AE sad-2
    AE "Hotsure... san?"
    MC "I... I..."
    MCT "This is it... Moment of truth... Why now?!"
    "I don't know why people say that there are 'butterflies in their stomach', it felt like a swarm of angry moths. My fingertips became cold as I finally resolved to make my choice. It was now or never."
    menu:
        "I didn't mean it like that.":
            jump AE020_c1_1
        "I think we should be together":
            jump AE020_c1_2

label AE020_c1_1:
    play music Bittersweet
    MC "Well, I didn't really mean it like THAT, you know, it's just that you seem like a cool person."
    MCT "I... I can't. I just can't."
    show AE sad
    AE "O-oh."
    MC "Yeah, uh, I hope it didn't come across as, like-"
    show AE sad-2
    AE "Yeah... I get what you mean. It just seemed kind of-"
    MC "No, no, it's like, you know how it is. Like you said, dating is frivolous."
    show AE neutral
    AE "Mhm, yes. I completely agree."
    MC "I just meant that if you WANTED to find anyone, y'know, it wouldn't be that hard for you."
    show AE sad-2
    AE "Well..."
    show AE happy
    AE "Thank you, Hotsure-san. I'll take what you said to heart"
    MC "Right... The 'anyone you want thing' not the, um-"
    show AE neutral
    AE "Oh! Yes, yes, right."
    "We stood there in silence for a bit, neither one of us truly knowing how to continue the conversation."
    MC "One... and... there we go. That's it."
    AE "Yes. The last processing forms for the year."
    MC "So, then after today... I guess I won't really need to be around here."
    show AE sad-2
    AE "No... I suppose not."
    show AE neutral
    AE "U-um, well, the office is probably going to close early today then. Neither of us have any business so..."
    MC "Huh? Oh, yeah."
    AE "Alright."
    AE "Well, it was nice working with you. I hope you carry with you... whatever it is you learned here."
    MC "Yeah. It was nice talking with you."
    show AE sad
    AE "..."
    show AE neutral
    AE "Alright. Well, have a good year."
    MC "Yep... yep."
    hide AE with dissolve
    "I walked out of the office for the final time. My chest was somewhat heavy, but I feel like I made the decision that was in my heart."
    if getAffection("AE") >= 8:
        show AE sad-2 at center with dissolve
        AE "Um, w-wait, Hotsure-san."
        "Shiori-san came bounding from behind me, and put a hand on my shoulder."
        MC "...Yeah?"
        show AE neutral
        AE "If you, um, if you ever need anything, the office is always open to you... and admittedly, I wouldn't mind if we perhaps got lunch every now and again."
        MC "W-well, yeah! I mean, that's what friends do, right?"
        AE "Friends... yes... Yes, I'm thankful for that. Well then."
        "Shiori-san squared her shoulders and bowed."
        show AE happy
        AE "Thank you. For being my friend."
    $disableRoute("AE")
    jump daymenu

label AE020_c1_2:
    MC "Shiori-san..."    
    "I stood straight, though my knees felt like they were betraying me, and I bowed with the ferocity of a hammer coming down on an iron nail."
    play music Romance
    MC "P-Please be my girlfriend!"
    show AE aroused-4
    AE "...I..."
    "Shiori-san looked on my display with distress and confusion. She brought her hand up to her mouth."
    show AE sad
    AE "Hotsure-san..."
    MCT "She... She's going to say no, isn't she."
    show AE angry
    AE "W-What the hell kind of trick are you trying to play on me?!"
    MC "Huh?"
    AE "I swear to you, Hotsure-san, i-if this is some kind of sick joke, then I'll show you just how humorous I can be!"
    MC "I-it's no joke, Shiori-san, I really like you!"
    show AE sad-2
    AE "You... You..."
    AE "..."
    show AE neutral
    AE "You really... mean that?"
    MC "Yes! I'm serious when I'm telling you that I want to be your boyfriend."
    "I made another light bow for emphasis."
    show AE sad-2
    AE "W-well... now I know why you've been here so often."
    MC " I... yes. I'm sorry for deceiving you. I didn't come to work for you to better myself as a student... but because I wanted to... b-be near you."
    show AE sad
    AE "Wha- ...b-but... why?"
    show AE angry
    AE "Why are you... How could you possibly be attracted to... me?!"
    MCT "She's mad... This was a bad idea."
    MC "That's easy Shiori-san. I-it's because you're you."
    AE "Don't give me that. There has to be some reason why."
    MC "Shiori-san, I can't keep my feelings for you locked in my heart any more. Since the day we met I... I've been interested in you."
    show AE sad
    AE "..."
    MC "N-now I know you think relationships are frivolous, but please, at least give me a chance?"
    AE "Hotsure-san... I'll consider it."
    MC "Eh?"
    show AE sad-2
    AE "G-give me..."
    show AE neutral
    AE "Give me a few days' time. By then I will give you a definite answer."
    MC "A few days? F-for what?"
    AE "..."
    AE "I want to learn."
    MC "Learn... what?"
    show AE neutral-annoyed
    AE "I-if you're serious about what you said, then accept my terms."
    MC "Shiori-san..."
    MC "Okay. A few days. A few months. Whatever time you need. I'm sure you will find what you are looking for."
    show AE neutral
    AE "A few days' time will be enough. Until then..."
    AE "This is our final day here. No matter what, this is the last day of our working relationship. And simultaneously, time to leave the office for now."
    MC "Well... where can I see you again? Outside of class?"
    AE "We won't meet here... but under the Sakura after class. That's where I will tell you."
    "Shiori-san placed the last three of her files in the proper folders, and began to leave the office."
    AE "Good day, Hotsure-san."
    "I took out my final file, and placed in in the cabinet."
    MC "Then here's to the next few days..."
    MCT "Whatever may come."
    $lockRoute("AE")
    $setProgress("AE", "AE021")
    jump daymenu

label AE021:
    $setProgress("AE", "AE022")
    scene Classroom with fade
    "When I walked into class today, Shiori-san was the first in the room. Admittedly I was a bit awkward around her, seeing as how a day before I told her I wanted her to be my girlfriend. I nodded and smiled to her and she turned a shade of pink before doing the same. She pulled out her notebook and began to write."
    show AE neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve #not sure if aroused, surprised or sad/shy
    MC "U-um... Shiori-cha-"
    "As I was about to speak, Alice walked into the room with Aida in tow."
    show PRG neutral at Position(xpos=0.90, xanchor=0.5, yalign=1.0) with dissolve
    show BBW happy at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Ohoho, now what's going on here?~"
    MC "E-eh? Oh, Nikumaru-san, good morning."
    if getAffection("BBW") < 0:
        BBW "My my, Hotsure-san, mind telling what's going on here with our dear president?"
        MC "E-eh?"
        BBW "From the sounds of it, that was a '-chan' forming in your mouth. You and miss assiduous are getting a bit close I see."
        show AE neutral-annoyed
        AE "Our business is between ourselves."
        BBW "Of course it is. Don't let me interrupt."
        "Alice gave a little wink before walking to her chair. Before sitting down, she motioned to me to come over to where she was."
        hide AE with dissolve
        hide PRG with dissolve
        MC "U-um... yeah?"
        show BBW neutral
        BBW "Bit of advice... you'll catch pneumonia if you stay to close to the ice queen. I'd recommend keeping your distance a bit for fear of frostbite."
        MC "...I'll keep that in mind."
        if getAffection("PRG") > 0:
            show PRG neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
            PRG "H-hi, Hotsure-san."
            MC "Hey, Kodama-san."
            "Aida gave a little smile. It felt nice to know the whole school wasn't against me."
            hide PRG with dissolve
            hide BBW with dissolve
    else:
        show BBW neutral
        BBW "G-good morning, Hotsure-san."
        "Aida shrunk back a bit and gave a tiny smile. I reciprocated with a nod and a smile as well."
        MC "Good morning, Kodama-san."
        BBW "I see you're a bit busy. I don't want to interrupt."
        MC "Ah, no, it's fine."
        show BBW happy
        BBW "Hmm... well now... the student council president, eh?"
        show AE neutral
        AE "Is there something you need, Nikumaru-san?"
        BBW "Oh, no, no, no not at all, dear... mhm~"
        "Alice walked over to her seat, but not before leaning in and whispering to me."
        BBW "Good luck, dear. Don't catch a cold, now~."
        MC "E-eh? Oh. Thanks, Nikumaru-san."
        hide AE with dissolve
        hide BBW with dissolve
        hide PRG with dissolve
    show HR neutral at center with dissolve
    "Tashi-sensei walked in the room, and after standing and bowing; as well as opening the door for Honoka, we began our lessons... however there was a problem. I couldn't help it, but I felt like I was being watched."
    "My attention was drawn to the picture of the second president of Japan on the wall when I noticed something... bright beaming glasses staring at me on the reflective glass. I looked down to my desk."
    MCT "What the..."
    hide HR neutral
    show AE glasses at Position(xpos=0.575, ypos=0.0, yanchor=0.12), Transform(zoom=8.0)
    "I looked up once more, and once more, on top of the president's eyes, the bright gleam of Shiori's glasses dove daggers into my own. She looked down, but only for a moment before looking back up through a side glance; her eyes piercing their way into my mind. I straightened up, and attempted to ignore her."
    hide AE
    show HR neutral
    HR "-of 1973. Okay. That should be all for today. Your homework is chapter five page eight."
    "Tashi-sensei nodded, and walked over to stand by the door."
    hide HR with dissolve
    show AE neutral at center with dissolve
    AE "Stand."
    "The class stood up. Honoka taking a little bit longer than the rest."
    AE "...Bow."
    MCT "The picture!"
    "While I would usually take in a nice view, I instead stared intently at the picture as I bowed. Sure enough, Shiori-san's eyes gazed right at mine all while we bowed."
    MCT "That was a close one."
    hide AE with dissolve
    show HR neutral at center with dissolve
    HR "Aright, all done? Good. See you all tomorrow."
    hide HR with dissolve
    "Everyone began to pick up their bags and Shiori placed her notebook under her arm. She began to leave, but I caught up with her just in time."
    show AE neutral at center with dissolve
    MC "U-um, Shiori-san?"
    AE "Hm? Yes?"
    MC "E-earlier... in class, I noticed you staring really intently at the picture on the wall."
    AE "The one of the second president? Indeed. It's very strange isn't it."
    MC "Oh? How so?"
    show AE neutral-annoyed
    AE "..."
    show AE neutral
    AE "I'm wondering what the significance of it is. I can't see why he in parti-"
    MC "Why were you watching me?"
    AE "..."
    show AE neutral-annoyed
    AE "Hotsure-san, it's very impolite to interrupt someone mid-sentence."
    if getSkill("Academics") < 4:
        MC "A-ah. Yes. Sorry, Shiori-san."
        show AE neutral
        AE "No worries. As long as you keep that in mind."
        MC "S-so, um..."
        AE "Yes?"
        MC "I can't... um..."
        AE "Hmm... well, I suppose I should get going. I'll see you around."
        MC "Huh? Oh. S-sure."
    else:
        MC "And it's very impolite to stare."
        show AE aroused-3
        AE "...W-well... I suppose so."
        MC "You usually aren't one to care that much about what's polite or not either. What's the deal? Is something wrong?"
        show AE embarrassed
        AE "A-I..."
        MC "...Have you thought about my request?"
        AE "...I have to go."
        MC "Huh? W-wait."
    hide AE with dissolve
    "Shiori-san walked away briskly, her now further distended rear bumping into a desk knocking it out of line. She turned, and straightened it before turning around and leaving."
    MC "Huh..."
    MCT "What was that about?!"
    "I stood up from my desk and popped my back. I grabbed my bag when I noticed something... a single boy had stayed behind. He was staring at me from behind his book. As soon as I turned to face him he kneeled his head down to avoid me."
    MC "W...?"
    "I stared at him for a minute, but he didn't pop his head back up. I gave up and just left."
    scene Campus Center with fade
    "My day continued along much of the same way. Every time I went to drink water, talk to students, or get something from a machine I would see someone out of the corner of my eye. Just staring at me and writing."
    scene Hallway with fade
    MC "Raw wheat, raw rice waw- no wait. Rwa- no. Raw wheat, raw rice... raw..."
    "I turned around and noticed, just around the corner, as Yuki-chan stared at me. She jumped for a moment before darting behind the wall."
    MC "...egg."
    MCT "H-oooookay. Now I'm starting to get fed up with this."
    "I walked over to the wall to see the girl with the rosy pink lips scribble on a notepad, squatting behind the wall. I watched on as she kept writing, only catching a few words here and there. She pulled out some chapstick and began applying it before continuing to write."
    "*Scribble scribble scribble*"
    MC "Yuki-chan?"
    show Yuki neutral at center with dissolve
    Yuki "Eep!"
    MC "What are you doing? Why are you hiding?"
    show Yuki sad
    Yuki "U-ummm..."
    "The thick lipped girl stood up straight and saluted."
    show Yuki neutral
    Yuki "S-student council business ma-sir!"
    MC "Okay... what I-"
    Yuki "Goodbye!"
    MC "Wait, no you di-"
    hide Yuki with dissolve
    "Yuki-chan turned around and began to shuffle away before I could catch up and ask what was going on."
    MC "No, wait you..."
    RM "Psssst. Pssssst."
    MC "Eh?"
    RM "Psssst."
    MC "What...?"
    "I turned to see Daichi hiding behind a plant."
    MCT "Ah. I see."
    "I pursed my lips and turned back around slowly, pretending I didn't see him."
    show RM neutral at center with dissolve
    RM  "O-oy, oy! I said 'pssst' which makes you socially obligated to acknowledge me!"
    MC "What do you wan-"
    RM "They're after you."
    MC "A-after me- ow, hey, hey!"
    "Daichi grabbed me by the hair and walked quickly across the corner, causing me to stomp awkwardly in his direction."
    RM "Here, into the men's bathroom. They won't follow us here."
    scene Bathroom with fade
    show RM neutral at center with dissolve
    MC "Ach-g-get your hands off ma-!"
    RM "Sh! Sh-sh-sh-sh... aight we're clear."
    MC "What the hell was that about?! Why is your sister following me?! What did you do?!"
    "Daichi shook his hand feverishly, a few strands of my hair falling to the ground as he did."
    MC "Oy, wait, wait, wait-is that my ha-"
    RM "No time."
    RM "Listen. You're being watched by student council. I don't know why, I don't know the situation, all I know is that if you lead them back to OUR room I'm screwed."
    MC "...I think student council knows where our rooms are."
    show RM sad
    RM "Then we're already too late."
    show RM angry
    RM "Listen, there are three student council members nearby, all women, but there's a male member who can just walk in here no problem and listen in. You're being followed. We both want to know why. Help me by letting me help you."
    MC "Wha-no!"
    show RM sad
    RM "Pleeeease... don't you wanna know?"
    "My mind flashed back to earlier, when Shiori-san was staring at me though the picture frame. Her intense eyes burning into my mind. I let out a sigh of exasperation."
    MC "Okay, okay, fine."
    "I let out a small sigh and began to walk out before feeling a tight grip grab me by the wrist."
    show RM angry
    RM "O-ho, no, no, no. If we exit there then they will definitely keep tailing you."
    MC "W-wait, then how am I-"
    "I turned to face Daichi when I heard the sound of metal creaking. It took me a second to register the sight of Daichi holding a metal grate to a ventilation shaft open."
    show RM neutral
    RM "Get in."
    MCT "..."
    MC "NO. WAY."
    show RM sad
    RM "H-hey, hey-sh-sh-sh. Okay, listen-"
    MC "I'm NOT crawling around in a vent."
    RM "Listen. Okay? These vents connect to the whole facility. I can get you right outside the door to our dorm room and from there I can open the passcode."
    MC "Why do you know th-"
    MCT "!!!"
    MC "Wait, is that how you found a way to creep around the building undetected?!"
    show RM smug
    RM "Exactly. I'm in the vents, yes."
    MC "When did y-"
    RM "Remember when I was missing from orientation?"
    MC "...Oh my god."
    RM "Vents dude. They never check 'em."
    MC "W-well either way I'm not-"
    show RM neutral
    RM "If you want my help you have to."
    MC "..."
    "Possibly for emphasis, Daichi began wiggling the grate up and down to make it squeak. Looking at me expectantly."
    MC "Okay. Fine."
    show RM smug
    RM "Yusss. Okay. Follow me."
    scene black with fade
    "I followed Daichi quietly through the vents of Seichou. With the exception of the occasional light source from the adjacent room and some quiet murmurs of people going about their day unaware, there was nothing but blackness as we twisted and turned throughout the massive system. We continued on, until we came across a light directly in front."
    RM "We're here."
    MC "Oh..oh thank god."
    "The grate opened, and from it slunk Daichi and I. He stood up composed wiping off his shirt as I lay on the ground gasping for fresh air."
    scene School Inner with fade #Used the same background as the time he first met Daichi
    MC "Pah... ahc... ngh..."
    show RM neutral
    RM "Tch, c'mon get up."
    MC "Okay... Okay... Phew."
    RM "Oy. You got something in your hair."
    MC "Eh?"
    "I ran my fingers through my hair and started to scratch."
    MC "Better?"
    RM "...Yeah. Oh, wait, actually, no. No, that did absolutely nothing."
    MC "Oh. Lemme-"
    RM "Dude just-"
    MC "Okay, yeah, inside, right."
    "We entered into the room as Daichi ran over to his bed to grab a book bag to which he began to stuff with various trinkets. I looked at my reflection in the bathroom mirror; my hair turned gray from the dust and cobwebs."
    "I took a shower and spent the rest of my time drawing up plans with Daichi."
    jump daymenu

label AE022:
    $setProgress("AE", "AE023")
    scene Dorm Exterior with fade
    "As I exited my room, I took a breath of fresh air as I stretched my back. Daichi walked out next and nodded to me, purpose in his eyes. One of my own still shut mid yawn, I nodded as Daichi opened the grate to the vents and climbed in, heading towards his planned destination."
    MCT "Alright. So far so good, I guess. Now I just head to class."
    "I put on the pair of sunglasses and headed out towards class."
    scene Hallway with fade
    "I walked with confidence through the halls, enough so that I had a slight smirk on my face."
    "*Tap tap*"
    "I passed by a pillar in the hall, and without stopping or turning around, I took two fingers up to my head and made an aloof salute."
    "Yooo, Amatsu-san, good morning."
    Ama "E-eh?!"
    "I turned a corner, and sure enough..."
    "*Tap Tap*"
    "I did a quick spin around a waiting Yuki-chan."
    show Yuki sad at center with dissolve
    Yuki "Eek!"
    MC "Paaardon me~"
    "As I began to walk away, Yuki-chan decided to follow in suit silently."
    MC "Something you need?"
    Yuki "Gh!"
    "The girl tensed up a bit and opened her mouth before speaking up."
    show Yuki neutral
    Yuki "U-um, it's rude to nearly run into people without at least bowing in apology!"
    MC "Mh, you're right. Sorry. I'm just really nervous for the swim meet after class."
    Yuki "S-swim meet!?"
    MC "Yep."
    "The girl put a finger up to her large, pouty lips in thought before pulling out a notepad and writing."
    show Yuki gossip
    Yuki "I... I didn't know, you were a swimmer Hotsu-"
    MC "Mhm. See you around."
    show Yuki neutral
    Yuki "E-eh? But-"
    "I began whistling to myself as I walked towards my class."
    Yuki "A-ah! Hey! That's disrespectful!"
    "Yuki-chan caught up with me and began to walk alongside me."
    Yuki "Heeey, what gives! You're acting all weird this morning."
    MC "You know how I usually act?"
    show Yuki sad
    Yuki "Ah! Um... Well... D-oh, just tell me what you want with the president!"
    MCT "Huh?"
    Yuki "Eep!"
    MC "...What?"
    show Yuki neutral
    Yuki "M-me and my big fat mouth..."
    MC "What are you-?"
    Yuki "L-listen! Forget what I said, okay! Erase, erase, eraaase~"
    MC "...D-umm..."
    Yuki "A-anyway, why are you acting so weird? What's with the glasses? What's up with you?"
    "While caught off guard for a moment, I smirked to myself before turning to her and setting the record straight."
    MC "Don't worry too much, just know that in this moment, I'm damn near untouchable."
    Yuki "Eh... W-wha-"
    MC "Class is about to begin. Isn't yours the other way?"
    Yuki "Ah! I-I can't be late, Matsumoto-san would kill me!"
    hide Yuki with dissolve
    "Kuchibiru-chan quickly strode in the opposite direction before turning the corner once more."
    MC "...Tch. Nice try, kid."
    "As soon as I felt nice and smug, I turned around and face planted right into the door to my own room."
    MC "Ach... I deserved that..."
    MC "No. No I didn't."
    scene Classroom with fade
    show AE embarrassed at center with dissolve
    "I walked into the room to see Shiori-san, who straightened up and looked straight ahead to the board."
    MCT "Ah... Just like yesterday then?"
    hide AE with dissolve
    BE "Pfft, ehehe..."
    MC "Hm?"
    "I turned to see Honoka, giggling into her hand."
    show BE happy at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    MC "Good morning, Honoka!"
    show BE neutral
    BE "Hey, Hotsure-san... Sooo, what's with the shades?"
    MC "Huh, oh, these? They-"
    show AE neutral-annoyed at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    AE "Are against dress code, as well as disallowed in class."
    show FMG happy at center with dissolve
    FMG "Ooooo."
    MC "Ah... Yeah. Right."
    show AE sad
    AE "...Sorry, Hotsure-san."
    FMG "OOOOOOO!"
    show AE neutral-annoyed
    AE "Is there a problem, Mizutani-san?"
    show FMG neutral
    FMG "Nobody said nothin..."
    AE "...Hmph."
    hide BE with dissolve
    hide FMG with dissolve
    hide AE with dissolve
    show HR neutral at center with dissolve
    HR "All right, all right, sit down."
    AE "Stand."
    HR "Or, yeah, that."
    AE "Bow."
    "The entire class bowed along with Shiori-san."
    HR "Everyone all good? Yeah? Okay. Now we can start."
    "The class went by as I-"
    HR "Oh, uh, Hotsure, take off the glasses."
    MCT "Oh, right."
    hide HR with dissolve
    "The class went by as I simply sat there and listened, the seeds of what I had sown being put into action all the meanwhile."
    scene black with fade
    "Last night."
    scene Dorm Interior with fade
    show RM neutral at center with dissolve
    RM "-and knock with Tokyo Ondo."
    MC "Eh? Really? Why that song?"
    RM "It works. Trust me."
    MC "A- ...okay, whatever."
    show RM happy
    RM "Mhm! Here, take these."
    MC "Eh?"
    "Daichi held his hands out and along with them a pair of black sunglasses."
    MC "Sun...glasses?"
    show RM neutral
    RM "Put them on."
    MCT "Okay... I don't see-woah!"
    show RM smug
    RM "Cool right? They have mirrors on the sides so you can see behind you."
    MC "Where did you get these?!"
    show RM neutral
    RM "Tengu Trader. Same place I get all my stuff."
    MC "...Dude, you gotta show me that site sometime, these things are wicked."
    show RM happy
    RM "Yep! Put them on when you are just walking in the halls."
    MC "Ehm... but my bangs..."
    show RM neutral
    RM "Pull your hair back."
    MC "Ach-bu-but I'd look dumb if I-"
    RM "I know! But look, look, as a reminder, when you head to class today, I'll follow you. When there's a creep hiding from you, I'll knock on the grate."
    MC "Okay. Where are you going to go, by the way?"
    RM "Student council room. I'm gonna take some of their files and see how many members they might have."
    MC "Isn't that..."
    show RM angry
    RM "Illegal, yes, very."
    MC "Please don't."
    show RM smug
    RM "Okay, I will."
    MCT "I SAID DON'T, DUMBASS!"
    show RM neutral
    RM "Once I know who all there is, I'll leave you a note in the window sill of death."
    MC "Window sill... of death?"
    RM "Mhm. It's a windowsill with a super loose window. I heard Shiori-san saved a dude from falling recently."
    MC "...Oh really... is that so?"
    RM "Yep."
    MC "Oh... So, uh... What will you do if people know you aren't in class?"
    RM "Don't worry. Nobody will notice."
    show RM happy
    RM "Good luck man. Night!"
    hide RM with dissolve
    "Daichi flopped over into his blanket and started to sleep. I sat up in bed, wondering to myself if this would really work."
    MCT "Do I really have a choice? ...Better yet, do I have anything better to do?"
    scene black with fade
    pause 1
    scene Hallway with fade
    "It had been a while since class ended, and I waited by the window sill of death for a good amount of time."
    MC "...What's taking him so lo-"
    "It was then that I saw it. Stuffed in the shape of a poorly crafted origami crane was a piece of paper on the windowsill."
    MC "Oh."
    MCT "The note?"
    "I looked around a moment before grabbing the paper from the windowsill and read it."
    "{i}Keisuke, President following. Writing in notebook. Contents unknown.{/i}"
    "I looked around a bit more before doing as instructed and folding the paper up and putting it in my pocket. I put my glasses on so that nothing would go wrong while I scanned the area for Daichi to reveal himself."
    "I scanned around and, with one hand, knocked the tune of the Tokyo Ondo on a metal grate. After waiting a few minutes, out came Daichi from the grate on the opposite side of the corner my back was leaning against."
    show RM angry at center with dissolve
    RM "Virtually untouchable? Really? Dude, c'mon."
    MC "I was trying to show my bravery in the face of-"
    "Daichi peered around the side of the corner and looked at me the same way I look at him whenever he tells me about the schools various conspiracies."
    MC "I... um... I wanted to sound cool."
    RM "You're completely unforgivable."
    MC "A-anyway, give me a status update."
    show RM neutral
    RM "Yuki is searching for you at the pool, the girl with the denim jacket went out to the town and most of the other people who were following either lost track of you or gave up looking."
    MCT "Girl with a denim jacket? I never..."
    MC "And how about Shiori-san?"
    RM "I have no idea. She was just sitting down and writing in a book last time I saw her. I think she's become aware of me, though."
    "Daichi began looking around, peering over the corner he was trying to obscure himself behind."
    show RM angry
    RM "I tell you man, she may be mousy in stature, but she's like a hawk... with an elephant's rear end."
    MC "Y-yeah, I get it."
    show RM neutral
    RM "I mean, for real, what would that even look like? A weird hawk-mouse-elephant combo. That doesn't even sound feasible, yet that's what Shiori i-"
    show RM sad 
    RM "She's right behind me isn't she?"
    MC "Um..."
    MC "No?"
    "Daichi slowly turned around as he came face to face with..."
    "Nothing. There actually was no-one behind him."
    show RM neutral
    RM "Oh... Huh... Usually this a thing where... Whatever."
    MCT "If there was ever an inkling of sanity in this man, it has long since passed into the ether."
    MC "Well, she's a really level headed person, and if she's trying to be sneaky then I doubt she would reveal herself because of some taunts."
    "I did a quick scan of the area with my eyes."
    MCT "Still though, I can't help but get that feeling... It's the same as yesterday... Wait."
    "I was hit with a sudden realization. I stood there baffled as how I didn't notice before."
    "Behind a pillar in the hall I saw it."
    "Wide hips constrained by a blue skirt, standing directly behind a pillar in an attempt at stealth."
    MC "..."
    AE "..."
    "I reached my hands out for a moment. The desire to push my hands against the exposed sides of her rear and fluff her butt like a pillow was strong... but I managed instead to just say what was on my mind instead."
    MC "Shiori-san, what are you doing?"
    AE "..."
    MC "..."
    AE "..."
    AE "Ngh."
    show AE aroused-3 at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    AE "Hmph."
    show RM angry
    RM "She was stalking us?!"
    MCT "Seriously, how did you not notice?!"
    show AE neutral-annoyed
    AE "I was not 'stalking' you. I was merely studying Hotsure-san."
    RM "Studying?! Keisuke, this chick is bad news-"
    show AE neutral-smug
    AE "So then you're Daichi Utagashi? I believe it's our first time meeting face to face."
    show RM neutral
    RM "Uh..."
    show AE glasses
    AE "Mhm. Well. I'll be taking note of this encounter."
    MC "W-we can iron out the details later."
    "Despite how crazy he is, I can't help but feel bad for the guy."
    MC "For now, why is the student council following me?"
    show AE neutral
    AE "Hotsure-san, you know that I detest utilizing student body resources for personal matters... However I figured this was a justifiable expenditure."
    "As she talked, Shiori-san began rubbing her arm and turning away, purposefully avoiding eye contact."
    MC "Expenditure for what though?"
    show AE aroused-3
    AE "Well, I was... I had a few things on my mind... concerning a few days from now."
    MC "...Oh. Oh?"
    show AE neutral
    AE "The things that were cluttering my mind... were inhibiting my performance during meetings. Surely clearing my concerns was worth the efforts I put forth."
    MC "Then perhaps you can put forth effort in clearing MY concerns?"
    show AE sad-2
    AE "Mph..."
    if getAffection("AE") <= 8:
        "Shiori-san straightened up before exhaling."
        show AE neutral
        AE "Put quite frankly... I don't trust you."
        "Shiori-sans words hit like a metal baseball bat to the temple, sinking my beating heart in my chest."
        MC "...Oh."
        show AE sad-2
        AE "N-now, I don't instantly assume that you have alternative intentions... It's simply that, well... Hm... I'm struggling to find the correct phrasing."
        MC "..."
    else:
        show AE embarrassed
        AE "I was simply... I want to know why."
        MC "...Why what?"
        "Shiori-san put one foot behind the other as she rubbed her arm. One of the few examples of poor posture she's ever displayed."
        AE "Why... Why someone like you wanted to be with... with me."
        MC "O-oh!"
        "I was admittedly a bit relieved. Shiori-san was just nervous about me asking her out due to her self-esteem."
        MC "Shiori-san, you have nothing to worry about! I'm being honest with my feelings."
        show AE neutral
        AE "..."
        MCT "Huh? I'm sensing... a bit of hesitation from her when I said that."
    show AE neutral-annoyed
    AE "I-in any case. I need to have a bit of a talk with your roommate. Sneaking about in the vents?! That's absolutely absurd!"
    MC "U-um... at least it isn't against school rules?"
    AE "Ach-wha-Who would think it would need to be a rule?! In any case, let me speak to him."
    show AE surprised
    MC "Daichi, Shiori-san wa-"
    hide RM with dissolve
    "I turned around in time to witness a mop dressed in a school uniform flop over onto the ground. I stared at the thing for a while, marveling in the insane speed that must have been required to set that up."
    MC "How... when did he?"
    AE "Dch-I was looking at him the entire time and I have no idea when it happened."
    "I looked around the general area for a little while before snapping to my senses."
    MC "O-oh, yeah, right."
    MC "In any case. You don't need to worry about me! Honest. I'm not trying to hurt you, or whatever."
    show AE sad-2
    AE "O-oh! No, I never..."
    MC "So please, Shiori-san."
    "I bowed deeply as a sign of respect."
    MC "Stop having your goons follow me around!"
    CMM "G-goons?!"
    show AE angry
    AE "Not now!"
    CMM "Ah!"
    "As soon as he appeared, he ducked behind the hall corner."
    show AE sad-2
    AE "I...I'm sorry, Hotsure-san. I didn't know what I was thinking. I-I never meant to harass you."
    MC "O-oh, no! It wasn't harassment! In fact... I thought it was kinda fun! Haha... but seriously though, stop."
    show AE neutral
    AE "Very well."
    "Shiori-san put her arms at her side and stood up straight."
    AE "Once more, I apologize for the inconvenience!"
    "Shiori-san bowed, causing her large rear end to hike up her skirt a bit before she quickly pulled it down. She stood back up and pushed her glasses up."
    AE "Now, if you'll excuse me."
    "Shiori-san turned quickly and walked away with confidence..."
    hide AE with dissolve
    play sound Boing
    "Causing her massive rump to wobble as she walked. Though she tried to keep her composure, she put her arms tightly to the side and put her hands on the sides of her donk in an admittedly sad attempt to stop the wiggling."
    MC "...Pheeww..."
    RM "Is she gone yet?"
    MC "H-Ach!"
    show RM neutral at center with dissolve
    RM "Wooo, man. And I thought I had trust problems."
    MC "Where were you?!"
    show RM angry
    RM "...Don't ask questions you don't need answers to."
    MC "N-...ugn..."
    show RM happy
    RM "In any case, I'm free from the tyranny that is the student council!"
    "Daichi crawled back into his vent."
    RM "I'll see you back at home base, okay?"
    hide RM with dissolve
    "Daichi crawled through the vents, making bumps and bangs along the way."
    MC "...Ugn... yep... see you there."
    jump daymenu

label AE023:
    $setProgress("AE", "AE024")
    scene Classroom with fade
    show HR neutral at center with dissolve
    HR "-and essentially, you end up with an absolute mess called the Treaty of Versailles."
    "Class had been going by fairly normally. My eyes had begun to flutter as fatigue began to set in. I looked up towards Shiori-san, who was sitting with her usual composed demeanor."
    GTS "U-um."
    HR "Yeah? What is it, Yamazaki-san?"
    GTS "I apologize greatly for interrupting the lesson, however... you have some red bean paste on your cheek."
    HR "Hm?"
    "Tashi-san looked off to the side of his face, noticing the spot instantly. With one quick, nearly sickening swoop of his cow like tongue he licked the spot clean in an instant, causing Alice to almost audibly gag."
    HR "Eh... Should be good for today. Matsumoto-san, do-"
    hide HR with dissolve
    show AE neutral-annoyed at center with dissolve
    AE "Stand."
    HR "Okay, well, there we go then."
    "The class stood up with the sound of metal scraping against tile."
    AE "Bow."
    hide AE with dissolve
    show HR neutral at center with dissolve
    "The class bowed down in respect as Tashi-sensei merely nodded and put his hands in his pockets. As I bent, however, my eyes were fixed elsewhere."
    MCT "I see someone will be getting a new skirt soon."
    HR "Alright, see you all tomorrow."
    hide HR with dissolve
    "As we grabbed our bags to leave, I listened around for what everybody was saying. Aside from the usual banter, not much had seemed to shift that much since the day before."
    show BE neutral at center with dissolve
    BE "Yo, Kei-kun!"
    MC "Oy, what's up, Honoka?"
    show BE happy
    BE "Thanks for the specs, these things are cool!"
    "I noticed that Daichi had completely forgotten to ask for his glasses back, so naturally I assumed he just gave them to me."
    "By the time I realized I was mistaken, I had already given them to Honoka."
    "After weighing my options, I figured I'd rather face secret agent man's wrath than disappoint her by asking for them back."
    MC "Hey, no problem. Have fun."
    BE "Hey, hey! Yamazaki-chan, put these on for a sec!"
    hide BE with dissolve
    "As I turned around to leave, I came face to face with Shiori-san, waiting expectantly."
    show AE embarrassed at center with dissolve
    AE "U-um... Hello, Hotsure-san."
    MC "Hey, Shiori-san, what's up?"
    AE "Would you care to walk with me? To the dorms, at least?"
    "I looked down at the girls expectant eyes, the frames of her glasses reflecting my own eyes back at me."
    MC "Oh! Well, uh... Yeah, sure! Come on, I'll walk you to your room."
    scene Hallway with fade
    "As we walked, we had gotten into a conversation about our best attributes to each other. It started off, ironically enough, after Shiori-san got quiet once she realized her massive behind was bumping into me after walking so close."
    show AE happy at center with dissolve
    AE "-and furthermore, you have a very nice sense of humor."
    MC "So then... What is this, by the way?"
    show AE neutral
    AE "Hm?"
    MC "I mean... I'm, y'know, walking you to your room, you're giving me compliments... What's going on here? Did you, y'know, come to a conclusion about me?"
    AE "..."
    "Shiori-san stalled for a moment, before simply adjusting her glasses, a pink hue overtaking her face."
    show AE embarrassed
    MC "Hm?"
    "After saying that, Shiori-san cast a cold aura around us, as though a level of personal tension was targeted directly at me."
    MC "Whatever it is, don't worry about it. Go ahead."
    show AE aroused-3
    AE "What is your relationship with Inoue-san?"
    MC "My relationship with her?"
    show AE neutral
    AE "Yes. When we first met, she walked into the school with you."
    MC "Oh... Well, yeah."
    AE "You seem to have very close interactions. I assume you've known each other for a long time?"
    "I stopped to think back about the good times Honoka and I shared in our days back in Tokyo. As my memories called deep back to my days of childhood in order to gauge just how long it was I actually HAD known her for."
    MC "Uh... Yeah, yeah I guess you could say that."
    show AE sad-2
    AE "As friends or...? "
    MCT "Oh geez, here we go."
    show AE embarrassed
    AE "I-I apologize for my intrusiveness."
    MC "N-not at all."
    MCT "I NEVER would have taken Shiori-san for a jealous type, though I may have been misreading the situation."
    MC "Ehh..."
    menu:
        "We're just childhood friends": #+1
            jump AE023_c1_1
        "I had a crush on her": #-1
            jump AE023_c1_2
        "I think she had a crush on me":
            jump AE023_c1_3

label AE023_c1_1:
    MC "Well, we've been friends since elementary school, I suppose. But that's just it. We've always been really good friends."
    $setAffection("AE", 1)
    "Shiori-san seemed to lighten up a bit at that, as the atmosphere became less tense."
    show AE neutral
    AE "Ah, I see."
    MC "Yeah, I mean, you probably have had some old friends you like to meet up with, right?"
    AE "Hmm... No, not exactly."
    MC "...Really?"
    AE "No. Er, well, I suppose Utagashi-san."
    MC "DAICHI?!"
    AE "Yuki."
    MC "Why does he talk like he never knew you?"
    AE "I'd never met him."
    MC "So... Wait, you were friends with his sister, who went to the same school as you?"
    AE "Yes. Yes to the, eh... Being from the same school. We'd only been acquaintances, however."
    MC "Huh. How bout that."
    AE "..."
    MC "..."
    jump AE023_c1_after

label AE023_c1_2:
    MC "Hmm... Honoka. Yeah, uh... We kinda had a thing going-er, well I had a thing going for her. I was too chicken to say anything though."
    $setAffection("AE", -1)
    show AE sad-2
    AE "Ah..."
    "I felt Shiori-san began to tense up a bit, meaning that admitting that was probably not the best idea I've ever had."
    MC "...What's wrong?"
    show AE neutral
    AE "N-nothing, Hotsure-san. Everything's fine."
    MC "...Is it because of Honoka?"
    AE "W-I don't believe I have any reason to worry. I mean, that's in the past after all."
    "A coy smile sprung up on my face as Shiori-san spoke my own defense for me."
    MC "Worry? So then you're thinking of me as a love interest then?"
    show AE embarrassed
    AE "Mmmn..."
    "Shiori-san brushed her hair to the side as she began to look away."
    AE "I... I'm entertaining the thought."
    MCT "Yes!"
    show AE neutral-annoyed
    AE "Maybe I should pad my chest to be more suitable to your tastes, however."
    MCT "Aaaand she hasn't let it go."
    MCT "Okay, change topic, change topic."
    jump AE023_c1_after

label AE023_c1_3:
    MC "If I can be honest... I think she had a crush on me."
    show AE neutral
    AE "Oh?"
    MC "Mhm. She'd get kinda awkward around me, always try to act really boy-ish in front of me, I think it was to get my attention."
    AE "Ah. That makes sense."
    MC "Yeah. And I gotta say, she's really sweet, but as far as a relationship goes, I'm not sure I would have felt the same way."
    AE "Hm... I'll keep that in mind."
    MCT "I-Is that a good thing? A bad thing?"
    MCT "Nevermind. What can I say to ease up the mood."
    jump AE023_c1_after

label AE023_c1_after:
    MC "It's nice to walk around freely without feeling like I'm being watched though, heh."
    show AE sad-2
    AE "..."
    "Shiori-san appeared to take my comment with a level of seriousness, as she looked down at the ground for a moment and brought her thumb up to her mouth."
    show AE sad
    AE "Once, again, I would like to apologize for yesterday."
    MC "Oh, no, like I said, it's okay."
    MCT "I wonder... Would it be impolite to ask about the nail biting thing?"
    MC "It's just... You're way more passionate than I first expected from you."
    show AE neutral
    AE "...Oh?"
    MC "Yeah."
    AE "Well, what makes you say that?"
    MC "Aha, well most girls don't send people to spy on others who tell them they like them."
    show AE aroused-3
    AE "T-that was merely an attempt to gauge your intentions, was all."
    MC "I never would have pinned you to be as opinionated either."
    show AE neutral
    AE "Now what makes you think I'm opinionated?"
    MC "Ehh, I dunno. The way you talk, the way you go about enforcing things, it really makes it seem as though you have some pretty strong opinions is all."
    MC "I mean, not that that's a bad thing. I guess that's one of the reasons why I've taken such a liking to you!"
    AE "..." 
    MC "Hm?"
    "I looked back, and saw Shiori-san staring down at the floor."
    MC "You stopped. What's up?"
    show AE neutral-annoyed
    AE "There's a wad of... chewing gum on the floor."
    "I looked down where Shiori-san was looking, and sure enough, a small pink disk with indentions lay plopped down right where I had walked."
    MC "Ick. Did it get on my shoe?"
    "I pulled up my foot for Shiori-san to see."
    AE "N-no. However if you HAD stepped in it, it would have streaked across the floor."
    MC "Oh. Well you should probably just leave it. It will probably be cleaned up by some of the students later."
    AE "Hotsure-san, never expect someone to do their job right. If I don't get it now, it will be on my mind all day."
    MCT "I think you may need to make major life adjustments if a piece of gum on the floor is at the forefront of your mind."
    "Shiori-san pulled out a small protractor from her bag and began to scrape off the gum."
    MC "U-um... Shiori-san?"
    show AE neutral
    AE "Yes?"
    MC "Why do you have that?"
    AE "To measure angles. Unfortunately, I have no choice but to use it for unintended purposes."
    MCT "Okay, but why do you need to measure angles though?!"
    "Shiori-san bent down and began to scrape at the wad with the plastic triangle, trying to get it off the floor. As she did, I just stood watching bashfully."
    "I began to wonder what people would think if they just saw Shiori-san bending over scraping gum off the floor. However, my worries were replaced by something else. I noticed something peculiar."
    show AE angry
    AE "Ngf, how long has this been here?"
    MCT "Wait... is that..."
    "I hadn't noticed before, but from here it was all but too obvious that you can see her ass from the front. Her hips bulged out far enough to create a wall of flesh and stretch the fabric atop two massive legs."
    MC "..."
    "I walked silently behind Shiori-san to get a better view. Though my head was turned, my eyes were focused right on her. Her growth was becoming more obvious, as her skirt was beginning to ride up even further."
    show AE neutral at Position(xalign=0.5, ypos=1.0, yanchor=0.95), Transform(zoom=2.0)
    play sound Boing
    "Her already thick thighs were plumping up quite nicely, pairing themselves with some wide, supple hips as well."
    "However, her bootyus maximus was, as always, the greatest sight to behold, the bottom of each cheek protruding through the bottom of her soon to be ruined skirt, the very bottom of her panties eliciting lewd thoughts from me. I lightly bit my bottom lip as every failed attempt to scrape the gum from the floor caused her backside to wobble gently."
    show AE angry at center, Transform(zoom=1.0)
    AE "Ugh, this damnable-"
    show AE neutral-annoyed
    AE "Hotsure-san, can you-"
    show AE neutral
    AE "..."
    MC "Hm?"
    "I realized a bit too late what had just occurred. I was able to break my gaze from Shiori-san's ass as I felt my chest tense up once I saw that she was looking back at me."
    MC "Oh... oh, wait, no."
    show AE sad-2
    "She stared back at me with a distressed look of betrayal and confusion, her lips parted as though to say something."
    MC "S-Shiori-san! I'm... I'm so sorry!"
    "My words were lost on her as she slowly stood back up, the gum still on the floor. She turned around to look me in the eyes, as I fruitlessly struggled to explain myself."
    MC "I was looking out the window and I saw tha-"
    MC "Huh?"
    "To my surprise, Shiori-san wasn't angry... she was smiling."
    show AE happy
    AE "Ahaa... so that's it."
    MC "Um... what's it?"
    show AE neutral-smug
    AE "Hotsure-san, see me on the roof tomorrow. I'll be able to settle this."
    MC "O-okay... wait, what time? I-"
    show AE neutral
    AE "Directly after class."
    hide AE with dissolve
    "Shiori-san answered extremely quickly, and left even quicker. I couldn't fully register what I was feeling more of at the moment, worry, confusion, or the lingering arousal from the image of Shiori-san's ass stuck up in the air."
    MC "After class, then..."
    MCT "Why was she smiling? I mean, I expected her to hit me..."
    "I let out a sigh and started rubbing the back of my neck."
    MCT "Still though, if she says she has an answer so quickly after catching me staring at her... I might be in trouble."
    "I felt my heart begin to sink deeper as those words went through my head; 'I might be in trouble'. I started to walk back to my dorm as anxiety began to kick in."
    MCT "I mean, it was a shitty thing to do, yeah, but can you blame me? It's just been a while since..."
    "It had definitely been a while since the last time I jacked off. Having a roommate, let alone who could be anywhere and everywhere, kind of put a strain on that."
    MC "Ahh man... what have I gotten myself into?"
    scene Dorm Interior with fade
    "As I got to my door, I began thinking of possible excuses, however I had no doubts she'd see right through me. I was just ready to get some rest. I entered the room, and collapsed on the bed, laying in silence as I contemplated my possible next moves."
    jump daymenu

label AE024:
    $setProgress("AE", "AE025")
    scene black with fade
    "{i}Creeeeak{/i}"
    scene Roof with fade
    play music Hallway
    "The light from the roof was blinding. I brought my arm up and looked down to shield my eyes as I stepped out from the stairwell."
    MC "U-um, Shiori-san? Are you there?"
    "After feeling my eyes had adjusted enough, I looked up to find..."
    MC "Shiori-sa-oh."
    MCT "Oh, she's not here."
    MCT "Hm."
    "I looked around a bit, but she was nowhere to be seen."
    MCT "I know she said she wanted to meet after class, but I guess I was wrong in assuming... she meant right after..."
    "After standing around a bit more, I walked over to the bench and sat down; awaiting whatever fate was going to befall me. As the minutes passed, I couldn't help but be reminded of the time Shiori-san and I sat up here together."
    "The more my memories lingered on the moment, the more my stomach began to feel light, as the fear of a possible inevitable rejection set in."
    MCT "This is bad. If th-"
    "{i}Creeeak{/i}"
    "I watched wide eyed as the metal door creaked open. I hopped up from the bench, and patted down the front of my pants. As Shiori-san emerged from the staircase, she stepped forward and slowly closed the door behind her."
    show AE neutral at center with dissolve
    MCT "There she is."
    MC "U-um... hey."
    AE "...Hi."
    MC "So... I wanted to apologize."
    AE "..."
    MC "Yesterday, I-I was just..."
    "I rubbed the back of my neck with my free hand, and looked off to the bench where I sat previously."
    MC "I don't know what came over me. I... I'm sorry."
    AE "Let's get to the point. Yesterday... I saw you staring at me while I was bending over."
    show AE aroused
    "Shiori-san began to clutch the sides of her skirt, as she began to blush in embarrassment."
    MC "A-ah... yeah. Look, Shiori-san, I-"
    show AE embarrassed
    AE "I'm not mad... in fact I-I have a proposition for you."
    MCT "She's not mad...? I mean, she was acting strangely yesterday, but she's being really gung ho about this."
    "As I looked at Shiori-sans glasses, past the light of the blistering sun glimmering off their metal frames, I saw something beyond... something I hadn't expected."
    show AE aroused
    play music Steamy
    AE "P-p-please grab my ass!"
    "A fiery lewdness I could have never predicted."
    MC "E-EEEHHHH!?!?"
    MCT "No way... this has to be a joke! How is this-?!"
    MC "O-oy. Sh-Shiori-san, you can't be serious!"
    show AE aroused-3
    AE "No, no, listen. I... I know I'm not popular with the boys. I never have been. The lack of attention all these years... I don't know if I can take it any longer."
    "Shiori-san began rubbing her legs together for emphasis, her voice making tiny squeaks with every wobble of her meaty thighs."
    show AE aroused-4
    AE "Since I've been growing though, my thighs have been rubbing together... down there."
    show AE aroused
    AE "S-sometimes, I even go jogging because the vibrations... mmmnff~"
    "Shiori-san made a small waddle to turn around in place, hoisted the sides of her skirt up, and bent over. Her asscheeks were on full display in front of me, a pair of massive and supple pale spheres of flesh shielded only by a pair of white panties."
    AE "I know why you've been spending time with me. This moment right here. So please... give me a good squeeze and I'll be yours forever~"
    "Shiori-san's mouth changed from biting her lip to her signature smirk, her lewd eyes obscured behind the glare from her glasses."
    show AE glasses
    AE "Come on... let me feel the pleasure I've been craving for so long."
    
    menu:
        "Do it.": # -33%
            jump AE024_c1_1
        "Don't do it.": # +5
            jump AE024_c1_2
        "I can't decide.":
            jump AE024_c1_3

label AE024_c1_1:
    MCT "I... I can't help myself. It's a golden opportunity."
    MCT "Shiori-san is beckoning to me like a cat in heat. It's impossible for me to resist!"
    MC "Shiori-chan..."
    "I stood up and stepped forward. My own legs trembling as well, not even attempting to hide my raging erection."
    MC "Well...I wouldn't want to keep a lady wanting."
    "I reached out my hands and grabbed it."
    show AE aroused
    AE "Ahnn~."
    "Shiori-chan tensed up as I grabbed a handful of her bare bottom. It was like ecstasy. It felt better than I could have imagined. I laid my palms flat on both cheeks, taking in every inch of soft supple flesh, every inch of dimple as my mind began to go blank."
    AE "Hotsure-san~."
    "Shiori-san lifted up her leg. I responded by sliding my hand down her chubby thigh. I gave her a light spank with the other, and watched as her ass began to undulate."
    MC "Mhm. Does that feel good?"
    "It was time to go for the kill. I slid my hand under her panties, lightly teasing her as my open palm began to slowly travel down her crack."
    AE "Oh, yes, Hotsure-san."
    "Shiori-san took her own hand and removed mine from her panties. I stood there, letting her take the lead. She placed her foot at the bottom of my abdomen."
    show AE aroused-4
    AE "It feels."
    show AE embarrassed
    AE "So."
    show AE aroused-3
    stop music
    $affectionDamage = int(math.ceil(getAffection("AE") * 0.3))
    $setAffection("AE", -1 * affectionDamage)
    $setFlag("AE024_grabbedass")
    AE "Good."
    "With what felt like lightning speed and the strength of a baseball bat, Shiori-san kicked backwards, sending me flying a few feet back and causing me to land on my ass."
    MC "Gah!"
    "I coughed and sputtered a bit before opening one eye. Shiori-san stood over me with an imposing presence I'd never before experienced."
    show AE neutral-smug
    play music Bittersweet
    AE "Ahh, it feels so good to have a question answered, doesn't it? 'Why does Keisuke want to date me?' Another problem solved."
    MC "...Ah... B-I..."
    show AE neutral-annoyed
    AE "Sexual conduct in a public area is prohibited. I will let you off with a warning for now, however I will not hesitate to report you to administration should it become a problem in the future"
    MC "Shiori-san."
    show AE sad-2
    AE "I... I wanted to trust you, Hotsure-san... goodbye."
    hide AE with dissolve
    if getAffection("AE") > 10:
        MC "Shiori-san... Shiori-san, wait!"
        AE "..."
        "She stopped on the first step of the stairwell, not looking back."
        show AE neutral at center with dissolve
        AE "...Yes, Hotsure-san?"
    else:
        MC "But... Shiori-san."
        show AE neutral at center with dissolve
        AE "Mm, Matsumoto-san, please."
    MC "I... I don't understand. What happened..."
    show AE sad-2
    AE "This whole time... it was my body this whole time."
    show AE neutral-annoyed
    AE "I should have known that the only person who would actually have wanted to spend time with me was... just a pervert who only cared about my body."
    MC "Shiori-san... I'm sorry. I didn't mean to betray you."
    "Shiori-san took one of her fists and slightly protruded a knuckle, which she began to bite with intensity."
    show AE angry
    AE "Your words mean nothing to me anymore, degenerate."
    "At that moment, a sharp pain like a dagger drove itself into my chest. I could barely speak."
    MC "I..."
    MC "Listen... I... I messed up. There's no two ways about it."
    MC "I need you to absolutely *know* that I didn't mean to hurt you in any way."
    MC "I just thought... I don't know-"
    MC "I thought you knew how I felt about you. Not only as a person, but how I felt when I looked at you."
    MC "I thought that we just got to a point where we could trust each other with our feelings."
    "By this point, my face had gotten a bit red and a lump had formed in my throat."
    MC "It's not about your body, I just thought we were closer than that. I figured I could trust you to be honest."
    AE "..."
    show AE sad-2
    AE "...I..."
    "Shiori-san slowly walked over to where I was, my own frustration and remorse visibly starting to show in my body language."
    show AE sad
    AE "I... I realize that I may have come on too strong... the kick was unwarranted... I just..."
    MC "..."
    show AE sad-2
    AE "Please... please don't betray me... don't let your feelings for me have been only lust."
    MC "I would never... I would never let that come between us."
    show AE sad-2
    AE "I don't know WHY you have the... desires you do. I don't think I'll ever be able to understand it... but... I know that at the very least, the feelings you had for me at lunch, underneath the tree, on the roof... they were all very real."
    AE "I can sense it. Through the perversion... there is purity in your feelings."
    MC "...I..."
    "I stood there dumbfounded as Shiori-san talked. Unable to fully follow her."
    show AE neutral
    AE "Please... please meet me underneath the tree. I'm sure... all my questions have been answered."
    "As quick as she came up, she left back down in a hurry. My eyes were heavy, but my heart was filled with hope."
    MC "...Thank you. Thank you, Shiori-san."
    jump daymenu

label AE024_c1_2:
    MCT "This... no. Something's wrong... I think I know what's going on here."
    MCT "Yesterday, after Shiori-san caught me staring... she was acting way too weird."
    MCT "If I'm wrong, then I could lose out completely though..."
    stop music
    MC "Shiori-san... no."
    show AE embarrassed
    AE "...Begging your pardon?"
    MC "I... I want something more from you than just pleasure."
    show AE neutral
    AE "..."
    MC "Yes, you did catch me looking at you inappropriately, and I will admit I find your body attractive, but to me your body isn't what I'm attracted to, it's you."
    AE "..."
    MC "I don't want a sex toy. I want you... I want you for who you are."
    "I sat there in silence for a moment, hands over my crotch as a show of restraint. Shiori-san looked at me incredulously, even with her ass on display right in front of me, I knew she saw that I was looking directly in her eyes."
    show AE neutral-annoyed
    AE "...Why must you make everything so difficult?"
    "Shiori-san straightened her back once more, dropping her skirt, and turned around to face me again."
    play music AE
    AE "Even after I went through all of that trouble to say and do such... humiliating things."
    MC "I'm sorry you had to humiliate yourself to find the truth, but you could've just done so by talking to me instead."
    AE "That wouldn't have yielded a definite answer."
    MC "Do you not trust me?"
    show AE embarrassed
    AE "I... i-it's not that, it's just..."
    "Shiori-san brought her thumb up to her lip in contemplation."
    show AE sad
    AE "I haven't found my answer..."
    MC "I can wait for as long as you need."
    show AE sad-2
    AE "N-not that... the other question."
    MCT "Other... question?"
    show AE neutral
    AE "Hotsure-san, I came here... assuming that you were just a pervert. ...I don't know WHY you think my body is attractive, but... I won't judge you for it. But I still don't have the answer I'm looking for..."
    show AE sad
    AE "Until then, however..."
    "Shiori-san gave a deep bow."
    $setAffection("AE", 5)
    show AE embarrassed
    AE "Th-thank you, for showing me respect."
    MC "..."
    "I looked down for a moment, and I took a deep breath in. Shiori-san, however, picked up on this and was quick to respond."
    AE "N-now I realize that you've been patiently waiting but..."
    "I looked up to her with same downtrodden look on my face, and Shiori-san realized that wasn't the issue."
    show AE surprised
    AE "O-oh... is there...?"
    MC "Well, I mean... It's just that I thought you had more respect for me."
    show AE sad-2
    AE "I... I'm sorry. I just..."
    MC "H-hey, it's alright. Look, I know you haven't been in a relationship before... a-and I know you don't have a very high opinion of yourself, but you need to trust me when I say I really want to be with you."
    show AE sad
    AE "..."
    "Shiori-san looked down and brought her thumb once more to her lip. Clearly distressed, she began to nibble as she held her elbow with her other arm."
    AE "It's just... I do trust you. You've proven to be kind, respectful, loyal... I just don't know why you..."
    MC "...Why what?"
    AE "..."
    show AE neutral
    AE "You'll have your answer soon. Please, it's all I ask... just please let me think until then."
    hide AE with dissolve
    "Before I could even open my mouth to speak, Shiori-san had already turned around and headed down the stairs in a hurry."
    MC "W-wait!"
    MCT "..."
    "I drew in a breath of air and exhaled. My previous worries calmed, but now replaced with confusion and a feeling of impatience."
    MCT "What is she looking for? Is it because of me? What...?"
    "I leaned up against the stairway wall, my hands resting in my pockets as I began to slump down and think about what all I could do to truly show her the severity of my feelings."
    jump daymenu

label AE024_c1_3:
    MCT "Is this the real life? Is this just fantasy?!"
    MCT "Have I died?!"
    MCT "I can't... I..."
    MC "B-w-ch... I-ah... um..."
    show AE aroused
    AE "S-such cute mouth movements!~ I wonder how that mouth would feel if I rubbed it against my-"
    MCT "!!!"
    MC "Ah! W-w-w-wah, bwha?!"
    show AE aroused-3
    AE "M-my..."
    MC "..."
    "I could do nothing but make a hoarse groaning. My chest tightening up as I exhaled, but failed to inhale."
    show AE neutral
    AE "...Hotsure-san?"
    "Shiori-san began snapping her fingers at me as I merely sat there dazed and confused."
    show AE neutral-annoyed
    $setFlag("AE024_confusion")
    AE "Ugh, I can see this is going nowhere."
    "Shiori-san stood up straight and turned around."
    show AE angry
    AE "I should have figured this would happen. I went too far. And to have put myself through such degradation..."
    MC "..."
    show AE neutral-annoyed
    AE "Here, Hotsure-san, let me..."
    "Shiori-san was distracted for a moment by noticing the prominent bulge in my pants."
    show AE embarrassed
    AE "L-let me help you up."
    MC "Shiori-san, I-I-I..."
    show AE neutral-annoyed
    AE "Mm, don't worry about it, Hotsure-san. I was too forward... I don't quite know what I expected, but I put too much out at once and my gambit failed."
    MCT "Eh? Gambit? What?"
    show AE neutral
    AE "Please, accept my sincerest apologies."
    hide AE with dissolve
    "Shiori-san bowed deeply before turning around and walking down the stairs, her hand covering the side of her face."
    MC "A... Wha-"
    MCT "..."
    MC "WHAT THE HELL JUST HAPPENED?!?!"
    jump daymenu

label AE025:
    $setProgress("AE", "AE026")
    scene Dorm Interior with fade
    play music Rain
    MC "Pheeww... okay... it's all going to turn out alright."
    show RM neutral at center with dissolve
    RM "Are you ready to go?"
    MC "Yeah... yeah, I'm ready."
    MCT "Today's the day."
    "The day Shiori-san would tell me truly how she felt about me. The day that we would either just stay friends or be official."
    show RM angry
    RM "I gotta say dude, fraternizing with the enemy? Rough."
    MC "Sh-she's not 'the enemy'!"
    show RM happy
    RM "Yo, yo, ey... I'm happy for you dude."
    MC "Ah, tha-"
    show RM neutral
    RM "Or sad for you. Depends on how it turns out."
    MC "...Thanks."
    if getFlag("AE024_grabbedass"):
        "I have to admit, yesterday filled me with fear. I'd never felt more pathetic in my life. But what Shiori-san said at the end filled me with hope."
        MC "Daichi... yesterday, I really messed up man."
        show RM angry
        RM "Oh? Wait, what?! How?"
        MC "U-um, on the roof... I don't wanna talk about it. All I know is that convincing her is gonna be rough."
        RM "Rough? What? How did I not know what happened on the roof?! I have precautions to-"
        show RM neutral
        RM "..."
        MC "...What?"
        show RM happy
        RM "N-nothing. Go get er."
        MC "...Again. Thanks."
        "I walked out the door and headed over to the sakura tree."
    elif getFlag("AE024_confusion"):
        MC "I-I mean... I don't know."
        RM "Oh?"
        MC "Daichi... is it... is it normal for an uptight girl to... lift up her skirt and ask you to grab her ass?"
        RM "..."
        show RM angry
        RM "What?"
        MC "N-nothing forget I-"
        RM "That shit doesn't work on me. What are you talking about?"
        MC "I-it's a hypothetical!"
        MCT "If Shiori-san thinks I told anyone, she'd eviscerate me."
        MC "Like... what would it mean?"
        show RM neutral
        RM "...I suppose that girls who are really strict have a lot of pent up feelings. Girls like that are probably really kinky."
        MC "Ach! Wa-"
        show RM neutral
        RM "That's actually a super weird thing to ask, even by my standards."
        MC "Well, I, uh... I saw it in a porn."
        RM "...A porn?"
        MC "Yeah, I wanted to see if it was realistic or not."
        RM "Oh. Well, no it's not. At least not in my experience."
        MC "O-okay."
        RM "Aight. Go get your girl, dude..."
        RM "Weirdo."
        MC "Eh?!"
        "Daichi closed the door behind me and left me in shock at what he said."
        MC "Hey! Hey, no, you just implied something really unforgivable!"
        MCT "Tch... well, whatever. I gotta psych myself up."
        MCT "I'm... I'm ready!"
    else:
        MC "I... I have to admit. I'm feeling pretty good about this. A-a bit nervous, but good."
        RM "Yeah?"
        MC "Yeah, I let Shiori-san know my intentions are pure."
        RM "I have to admit... I really don't see it. Why her?"
        MC "Why her?"
        MCT "Initially? Hmm..."
        MC "I guess... I dunno. There are a lot of reasons to be honest. But I guess... you just can't really explain it with words."
        show RM angry
        RM "Uggh. You people are the worst. The guys who are just like 'Oh, words can't express my feelings.'. Grab a dictionary or something!"
        MC "U-um... yeah. Will do."
        RM "But in all seriousness dude, hope everything turns out well. Now, if you don't mind, I'm going to Matsumoto-proof my half of the room."
        MC "Ahah, well, thanks."
        "I turned around and exited the room, a feeling of serenity only slightly beating out my queasy stomach."
        "I'm usually not like this, but to be honest, it had been a long time since I last felt this strongly about a girl, and if she says yes, and feels the same... it just felt nice knowing someone cared that much about me as well. IF she says yes."
    stop music
    show Campus Center with fade
    "I opened the door to the courtyard, wind whipping about me as I looked towards the trees pink petals, falling gently to the earth."
    MCT "Okay... there she is."
    show AE neutral at center with dissolve
    play music AE
    "Shiori-san was waiting there, bag under her arm, looking around for me. The moment she met my eye, she straightened up while putting her fist up to her mouth to clear her throat."
    AE "H-Hotsure-san."
    MC "Hey..."
    show AE embarrassed
    "We stood there awkwardly, Shiori-san looking on expectantly for an opportunity for the conversation to begin."
    MCT "I'm guessing she wants me to start it off."
    "I opened my mouth to talk, but without any prior planning nothing could come up except for thoughtless, typical, small talk."
    MC "It's really nice out."
    show AE neutral
    AE "Truly."
    MC "Hm..."
    AE "..."
    MC "A-and you look beautiful."
    show AE aroused-4
    AE "O-oh... um..."
    show AE neutral-annoyed
    AE "Alright, I hope you don't mind if I just get straight to the point."
    if getFlag("AE024_grabbedass"):
        AE "Well, I know your intentions, but..."
        "Shiori-san looked behind her to her ever growing backside. Call me crazy, but it looked like it had grown even larger than before. I shifted in place a little bit and moved my hips back; a side effect of remembering what happened yesterday."
        show AE sad-2
        AE "I just don't understand why-"
        MC "Can I interject for, like-"
        show AE sad-2
        AE "A-ah, yes. Go ahead."
        MC "Um. Okay. So... yes. It's true. I've had an attraction to you for... uh..."
        AE "Sexual."
        MC "Y-N-no, no that's not just it. It... ugh."
        "I felt my heart sink further into my chest."
        menu:
            "It was because of your body":
                MC "Yes. Yes it's true. It started off that... I wanted to get to know you because of your body."
                AE "..."
                "Shiori-san visibly swallowed her own sadness."
                AE "So then what?"
                show AE sad
                AE "What was the point of any of what we did? This whole time... was I just-"
                MC "No! It wasn't like that at all! Once I got to know you, I knew... I knew you for who you were."
                show AE sad-2
                AE "And then... who am I to you?"
                "Thoughts rushed through my head as I tried to think of something that had been said in a million ways by millions of people before me. I wanted to speak out with my heart."
                MC "You're Shiori Matsumoto."
                show AE surprised
                AE "..."
                "Everything was silent. Shiori-san looked at me in a way I had never seen anyone look at me before. I could tell by her gaze that without a doubt, simply telling her that let her understand the depth of my feelings for her."
                show AE sad
                AE "Hagn... A- ...Hotsure-san... I never..."
                MC "Do you... understand?"
                show AE aroused-4
                AE "...So that's how it is."
            "It was heat of the moment":
                MC "It was a moment of weakness. I-I mean, it was just so sudden and... I was just so..."
                show AE sad-2
                AE "Hotsure-san..."        
                "Shiori-san seemed more conflicted now than I had ever been in her entire life."
                AE "I... I expected you to be stronger. I realize my methods were crass, but..."
                MC "I know. I needed to hold myself up to a higher standard. I needed to contain myself, but I just..."
                "In a show of remorse, I knelt down to my knees, put my hands on the ground, and placed my forehead against the cold soil."
                MC "From the bottom of my heart... I apologize."
                show AE sad
                AE "A-ah..."
                "Shiori-san seemed worried for a moment, and looked around to see if anyone was looking."
                show AE surprised
                AE "H-Hotsure-san, I appreciate the gesture, b-but this is a bit much! You don't need to degrade yourself, please, please stand."
                "I stood up and nodded, heart heavy with shame for my own weakness."
                show AE embarrassed
                AE "You're not weak, Hotsure-san. You did what anyone else with your... tastes would have done."
                MC "..."
                show AE aroused-4
                AE "Mmm, here."
                "Shiori-san took out her handkerchief and rubbed some dirt off my head. Our eyes met in that moment, and in her eyes I could see remorse for her actions as well."
                show AE neutral
                AE "Hotsure-san... do you remember what I said to you on the roof?"
                MC "Hm?"
                show AE happy
                AE "You have purity within you. I can sense it. It was a time of weakness... that is all."
                "Shiori-san brought her hands in close to her breast."
                show AE embarrassed
                AE "I don't... I don't presume to understand your oddities. But... It was a bit too far for me to call you a degenerate. I realize that."
                show AE aroused-4
                AE "Hotsure-san... Alright... I want to give this a chance..."
                AE "I'm willing to give... us a chance."
                MC "S-Shiori-san."
    else:
        show AE neutral-annoyed
        AE "Why are you attempting to court me?"
        MC "Eh?"
        show AE angry
        AE "You know what I mean. What is your end goal? Humiliation? My own behind is doing that enough. Money? Trust me, I'm painfully bereft-"
        MC "It's not about anything like that... I really care about you."
        show AE sad-2
        AE "But that's just the thing. I ruled out every possible explanation, but still I-"
        MC "Shiori-san... please just listen."
        show AE neutral
        AE "..."
        show AE sad
        AE "You're right. I'm not hearing what you have to say. I'm sorry."
        MC "No, it's okay... but..."
        MC "I know you've never really... HAD anyone show any interest in you. This all must be really confusing."
        MC "But you have to understand, you're one of the best girls I've ever met. You're interesting to me, as well as insanely beautiful."
        show AE surprised
        "Shiori-san began to blush, her face matching the blossoms falling around us."
        show AE embarrassed
        AE "N-now I'm even MORE convinced you're not being honest."
        MC "It's true."
        show AE sad-2
        AE "...I just... I want to understand."
        show AE embarrassed
        AE "I want to understand why... what this feeling is."
        "Shiori-san clutched at her breast as she bit her thumbnail with the other hand."
        show AE sad
        AE "You're so... you're like no man I've ever met. I just... I'm so used to being alone."
        MC "You don't have to be. I want to be with you."
        MC "Shiori-san... once more..."
        MC "Will you be my girlfriend?"
        "I bowed a deep bow, heart racing as I let my heart pour out."
        show AE sad-2
        AE "Hotsure-san..."
        show AE aroused-4
        AE "Yes. I... I know now without a doubt... yes."
        MC "Hah... Ah..."
        "I stood straight up and looked her in the eyes. She walked up towards me to meet my gaze further; to get closer to me."
        show AE happy
        AE "I can't believe... this is what it feels like."
    "I took Shiori-sans hands in my own. Her cold, smooth hands, considered by so many to be that of a heartless woman began to warm in my own."
    MC "I promise. I will do everything to show just how much I care about you."
    MC "Even now I'm doing what I can to hide your trembling from anyone watching."
    show AE neutral-annoyed
    AE "Ach-wha-y-you!"
    MC "Ehehe..."
    "Shiori-san broke my grasp before twiddling her fingers together."
    show AE embarrassed
    AE "U-um, I'm not really sure how to put this... but... I've been working on something."
    MC "Hm?"
    "Shiori-san rustled about her bag for a moment before taking out a stack of papers."
    show AE aroused-4
    AE "While I waited for this day, I spent some time reworking our relationship contract. I hope you find everything agreeable."
    MC "Eh?!"
    MCT "Y-you're kidding, right?!"
    show AE happy
    AE "...Pfft... eheh."
    MC "..."
    "Shiori-san smiled a tiny smile a bit before putting her hand up to her face to cover it."
    AE "Only kidding, of course."
    "She put the papers back in the bag and brushed away some stray locks."
    MC "Ah... ah, phew, heh."
    show AE aroused
    AE "S-Sorry, my sense of humor is-"
    MC "O-Oh, no it was funny, just uhh... I thought you were serious."
    show AE happy
    AE "No, no, ehe..."
    "Shiori-san and I stood there awkwardly for a moment. Though the awkwardness, however, there was a lightness that I hadn't felt in a long time, and while her joke wasn't the best, it sure as hell was nice to see her joking around with me."
    MC "Hmm... so, uh, g-got any other plans for today?"
    show AE aroused-4
    AE "Not at the moment, no. I finished all my work before I got here."
    MC "Ah... Heh."
    "Hearing those words from her was the best gift I could have gotten. My heart was fluttering, and her eyes showed that she felt the same."
    MC "Well, uh..."
    "I put my hands in my pockets and hung my head down, hiding the blush creeping over my face."
    MC "What do you wanna do now?"
    show AE embarrassed
    AE "U-um... I'm not sure. What are my duties? A-as a newly-instated girlfriend."
    MC "Your...? I guess... we can take it slow. You're new to the whole-"
    AE "D-dating scene."
    MC "-girlfriend thi-yes, yeah, right, exactly, dating scene. Dating scene." 
    AE "Mm."
    MC "And uhh..."
    show AE happy
    "I scratched the back of my neck a bit, and Shiori-san tilted her head slightly."
    MC "Yeah. Yeah, till then... I guess... see you tomorrow?"
    show AE sad-2
    AE "O-Oh!"
    MC "Unless, you-"
    show AE neutral
    AE "No, no, I hadn't uhh... I don't have any prominent ideas."
    show AE happy
    AE "Ehe..."
    MC "...Well then... see you tomorrow."
    AE "See you tomorrow."
    "I bowed shyly before starting to turn around. That's when Shiori-san piped up out of the blue."
    show AE aroused-4
    AE "...A-actually, um..."
    MC "Hm?"
    show AE embarrassed
    AE "The dorms are only a little bit a ways from each other..."
    MC "Wanna walk together?"
    show AE aroused
    AE "...Mhm."
    MC "Oh, ehe... okay."
    "As Shiori-san began to walk off with myself in tow, a cool breeze set in, blowing Shiori-san's skirt up slightly before she caught it with her off hand."
    MC "Eheh... haaaah..."
    scene black with fade
    "I closed my eyes and let out a deep breath."
    "I'm still not quite sure how the day was supposed to end. Was I supposed to kiss her then and there? Hold hands? All I know is that once I got back to my room, I collapsed on my bed and let out a nice, big sigh."
    "Shiori-san and I were now official."
    jump daymenu

label AE026:
    $setProgress("AE", "AE027")
    scene black
    play sound AlarmClock
    scene Dorm Interior with fade
    "I awoke to the sound of my alarm clock buzzing it's shrill beeps as my eyes fluttered slowly open."
    MC "Mngh... urh... shut up, you damn thing."
    play sound Thud
    "I closed my eyes for what felt like a few seconds more, when..."
    show RM angry
    RM "Dude, dude, wake up."
    MC "Huh-wa?"
    show RM neutral
    RM "Get up, we got class."   
    MC "Mm... what time is it?"
    show RM angry
    RM "Like, six thirty. C'mon."
    MC "Aagn, damnit. Do you think I have time for-"
    RM "I get to class via air duct and I'm still gonna cut it close; you don't have time for nothin'."
    MCT "Ech, hair's gonna get all matted. Whatever, I'll deal with it later."
    "I rubbed my eyes with my thumb and middle finger before sluggishly pulling myself off of bed and pulling on my uniform, laid out as I usually have it at the end of the bed."
    "I pulled the pants on first and then the button up came next. A warm smile came to my face as I recounted my wonderful sleep."
    MC "I had this... amazing dream last night."
    show RM neutral
    RM "Huh? What about?"
    MC "I had a dream that Shiori and I... we were just under the tree and she, she said she wanted to be with me. It was nice."
    "Daichi eyed me for a moment, before himself putting on a bright smile and scoffing."
    RM "Uhh, earth to Keisuke. That wasn't a dream."
    MC "Eh?"
    #show RM happy
    RM "Aha, dude, you were so excited I had to postpone my presentation on what I found in the principal's office to listen to you gush."
    "My heart began to flutter, as the reality of yesterday's events became distinguished from my dreams. This is likely because my dreams were, at this point, naught compared to the happiness and joy I felt than I had before returning to my dorm."
    MC "O-oh yeah."
    MCT "Then yeah, it's a real thing now. Shiori-san's my girlfriend."
    show RM neutral
    RM "Mhm. Now c'mon."
    "Daichi opened up the door and motioned me out, which I begrudgingly took him up on."
    #show RM happy
    RM "Ahh, the vent over the teacher's lounge is always so nice in the morning. Fresh smell of coffee."
    MC "Do you ever fear getting caught? Y'know, like, at all?"
    show RM neutral
    RM "Nope. Because I'll never get caught."
    MC "Ah..."
    MCT "That is an absolutely psychopathic level of confidence."
    "Daichi crawled into the vent systems, carefully shutting the grate behind him. As for myself, I walked briskly to class, a renewed sense of self flowing through my body, as though a great weight had been lifted from my shoulders."
    scene Classroom with fade
    "It appeared as though I was one of the last ones to class, as everyone was already in their seats and talking. Of course, the first one on my mind in the room was Shiori-san, who looked up towards me and nodded before bashfully looking back down at her desk. I walked over to her desk, a faint flutter in my heart as I went to talk."
    MC "Um... g-good morning, Shiori-san."
    "She looked up back at me, a light blush covering her face as she rubbed her arm with her other hand."
    show AE embarrassed
    AE "Good morning, Hotsure-san."
    show FMG angry at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    FMG "O-oy! You chewed me out for almost being late, why does he get a pass?!"
    show AE neutral
    AE "O-oh! Yes. Hotsure-san, you were almost late. It's b-best you not make a habit of this."
    MC "Ah. Sorry, won't happen again."
    AE "I sincerely hope so..."
    show FMG happy
    FMG "Haaa, you got in trouble."
    show AE angry
    AE "Hush!"
    FMG "Heeeh~"
    "As I went to sit down at my desk, I heard a faint murmur as I passed Shiori-san."
    hide FMG happy
    show AE embarrassed
    AE "S-sorry."
    MC "Hm?"
    show AE neutral
    BBW "...Hm?"
    "I responded in a light whispery voice as well."
    MC "It's all right. Don't worry about it."
    "Shiori-san nodded as I sat down in my seat. As soon as I sat, however, Tashi sensei walked into class, suit jacket slung over his right shoulder with a mug of coffee in his left hand."
    #show TS
    AE "Stand."
    MCT "Ohp, hey, here we go."
    AE "Bow."
    "The class bowed and then sat back down to continue the lessons for the day."
    hide AE neutral
    #hide TS
    scene black with fade
    scene Classroom with fade
    TS "-Okay. Any questions? I'm leaving either way. See you tomorrow."
    "With a stand and a bow, we all began to talk amongst ourselves as we left the room, however I waited to leave. I wanted to talk to Shiori-san a little bit between classes. Within a minute or two, almost everyone had piled out."
    show PRG sad at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    PRG "N-N-Nikumaru-san, are you sure you don't need me? I don't mind, really-"
    show BBW neutral at Position(xpos=0.25) with dissolve
    BBW "Yes, yes, Kodama-chan. Everything is perfectly fine. Simply wait for me by our usual spot, okay dear?"
    PRG "O-okay."
    hide PRG sad with dissolve
    "The tiny Kodama-chan, usually seen with Nikumaru-san, left the room alone, and somewhat morose."
    MC "U-um, hey, Nikumaru-san? Why did you make Kodama-chan leave?"
    show BBW happy
    BBW "Ohoho, don't worry about that now. I simply wanted a bit of space is all. Oh! Matsumoto-san is looking this way now, dear. Don't let the poor girl get the wrong idea now."
    MC "O-oh?"
    MCT "How did she... know I was waiting for Shiori-san?"
    MC "Well... thank you, Nikumaru-san."
    BBW "Mhm~."
    hide BBW happy with dissolve
    "I turned around to see Shiori-san waiting patiently, her bag slung over her shoulder, with her generous frame almost the width of the window she was standing in front of."
    show AE neutral
    MC "Hey."
    AE "Hotsure-san."
    MC "So, wanna go hang out? Somewhere?"
    AE "Ah, yes. How about the courtyard?"
    MC "Sounds good."
    "I looked her in the eyes, and she looked back with a deep, yet calm and serene gaze. The two of us walked into the hallway together, us standing side to side as we walked."
    "Or, at least as side to side as her massive rear would allow."
    scene School Inner with fade
    show AE sad
    AE "Hotsure-san, I'd like to start off by apologizing for this morning."
    MC "Hm?"
    MCT "This morning...? Oh!"
    MC "You don't need to worry about that."
    AE "I'm sorry. I would have corrected your behavior sooner, however I'm still a bit thrown off by my new... position in your life."
    MCT "Ah. So that's what she was sorry about..."
    MC " Ehe... sorry, I'll be more on time. A-actually, I had to smack my alarm clock because it was so loud, and I kind of... fell back asleep."
    show AE angry
    AE "T-that's school property!"
    MC "Eh? W-wait, I can explain."
    show AE happy
    AE "Eheh, don't worry about it. Those things are nearly indestructible, anyways."
    MC "Ah... y-yeah."
    MCT "I know, because I tried to destroy the damn thing!"
    show AE neutral
    AE "Still though. There must be a certain tragedy to being an alarm clock."
    MC "Hm? What makes you say that?"
    AE "Well, we create them to do what we ask, and then hate them for doing what we ask."
    MC "Huh... that's, uh... hm."
    MCT "I guess that's one way to see it... Hmm. This girl."
    "I looked over towards Shiori-san and walked a little bit closer to her, causing her hip to gently brush against my leg."
    scene School Planter with fade
    "We reached our destination a few minutes later. The courtyard was mostly empty, save for two friends playing frisbee a far enough distance away."
    MC "All right. We're here."
    show AE neutral
    AE "Mhm..."
    MC "..."
    AE "..."
    MC "So... ehe..."
    show AE happy
    AE "B-boyfriend and girlfriend."
    MC "Boyfriend and girlfriend, yep!"
    AE "Ehe..."
    MC "Hoo... *khm*"
    AE "..."
    MC "..."
    show AE neutral
    AE "...What now?"
    "I sat in silence for a moment, before looking down at the ground."
    MCT "I... I dunno?!"
    MC "So... um..."
    AE "Is this normal for couples, Hotsure-san?"
    MC "...Yep. About par for the course."
    AE "Hm..."
    MC "Hey, uh, by the way, you don't need to call me Hotsure-san anymore."
    AE "Hm?"
    MC "W-well... We're dating now. So, I'm fine with 'Keisuke-kun' or whatever."
    show AE embarrassed
    AE "Oh! Oh, I know, I know, it's just... i-it's what I'm used to. It's just crazy to think that just a few days ago it was all so... hm..."
    MC "I know. It's crazy for me too."
    MC "Shiori-chan."
    AE "E-eh?"
    "Shiori-chan looked confused for a moment, batting her eyes before adjusting her glasses a bit."
    AE "C-chan?"
    MC "Mhm. Er, well, you're my girlfriend now so I figured... it'd be appropriate."
    AE "Oh! Um... yes. Yes, I am."
    show AE happy
    AE "I'm... Shiori-chan."
    AE "'chan'... hm... I haven't been okay with being called that in... God knows how long."
    MC "Aha... really?"
    AE "Mhm. I'd suppose not since middle school."
    MC "Not even your parents?"
    show AE neutral
    AE "No."
    "Shiori once more answered bluntly and quickly when the topic of her parents were brought up, just like last time."
    MCT "Hmm... sore topic, I'm guessing. I won't go after it right now."
    MC "A-ah."
    AE "..."
    MC "Do, uh, do you have anything you want to do?"
    AE "Hmm... well, I can't think of anything."
    MC "Well, then, do you want to maybe... just sit here for a while?"
    show AE happy
    AE "...Absolutely."
    "I sat down, and Shiori-san did the same, the air causing her colossal skirt to flutter lightly as the warm flesh of her bulging behind spread out slightly across the grass."
    "I rested my head in my arms and laid back, looking up at the sky as the birds chirped around us."
    AE "Mhm... ehehe..."
    MC "Hm?"
    MCT "Shiori-chan... is she laughing?"
    MC "You all right?"
    AE "This... this feeling."
    AE "This lightness."
    AE "It feels so... unlike anything, Hotsure-san."
    MC "I know. It does, doesn't it? Let it... let it stay with you for a moment."
    AE "Hmm..."
    "Shiori-san scooted in closer to me, and began to fidget around for a bit."
    "We sat there contently looking up at the sky, sharing some small topics here and there."
    scene black with fade
    scene School Planter with fade
    "Before we knew it, our entire break had passed. Shiori-san rested her hands politely on her lap the entire time, and I just laid back and gave short glances between her face and the daytime sky."
    show AE happy
    AE "Haaahh, this really is nice."
    MC "Yeah..."
    "I nestled my head further into my own hands and let out a sigh as I closed my eyes. I turned my head and opened them once more, only to notice a figure of the corner of my eye. I sat up a bit to see clearer, but the figure disappeared into the door."
    MC "Hey, Shiori-chan?"
    show AE neutral
    AE "Hm?"
    MC "...Did you feel like we're being watched?"
    "Shiori-san looked around for a short moment, before returning her gaze to me."
    AE "I highly doubt it."
    show AE angry
    AE "Besides, if someone HAD been spying, I'd need to teach them a lesson about personal privacy."
    MC "Heh. Straight to that, eh?"
    play sound ClockTower
    show AE neutral
    AE "Ah. That's the bell for class."
    MC "Oh? Oh! Yep."
    MC "Haaah."
    "I sat up and lifted myself off the ground. Shiori-chan began to push herself off the ground with a heavy strain."
    show AE embarrassed
    AE "H-grh... mhn."
    MC "Here."
    AE "N-no, I should be able... to..."
    MC "Shiori-chan."
    AE "Hm?"
    MC "I... I'm your boyfriend. Allow me."
    "I held my hand out for her. She looked at it, and then looked up at me; a bright glimmer quickly gleaming across her glasses."
    AE "Oh.. well... in that case."
    if getSkill("Athletics") >= 3:
        $setAffection("AE", 2)
        MC "Alight, hrg..."
        "I grabbed her arm and pulled upwards. Shiori-chan let out a little yelp as she quickly was lifted from her sitting position. She got her balance on her feet, giant ass wobbling like mad in response to my pull."
        show AE embarrassed
        AE "Ahn! Mmn... hoo, ah... Hotsure-san, you're... much stronger than you seem. I'll need to take note of that. Aha..."
        MC "Heh... thanks."
    else:
        MC "HHRGN..."
        "I pulled as hard as I could but Shiori-chan refused to budge. Her big fat ass weighed her down to the ground like a flesh-anchor."
        show AE embarrassed
        AE "A-ah. Don't strain yourself too much."
        show AE neutral
        AE "..."
        show AE embarrassed
        AE "Here, let me... hmpf!"
        "Shiori-chan, without any help from me, grabbed onto the nearby tree and hoisted herself up. She put her arms out for balance, and I supported her back to keep her stable so she didn't fall."
        show AE neutral
        AE "Hoo, ah... *khm*, I should be fine..."
        MC "Ah... y-yeah, cool, cool."
        MCT "First day as a couple and I'm already embarrassing myself in front of her."

    "I cracked my back and stood straight as thoughts of what all to do went through my head."
    MC "So, uh, got any plans for tonight?"
    show AE neutral
    AE "Oh, um... well, I have a meeting at six, and the rest of the time from three will be mostly hall monitoring."
    MC "Ah, it's okay then, you don't need to worry about it."
    show AE embarrassed
    AE "...B-but, I don't have anything to do after that, and tomorrow is free too. If you want to do something, that is."
    "Shiori-chan put her hands behind her back and began to move lightly from side to side. Without her knowing, this caused her thick thighs to wobble that much more noticeably."
    MC "D-uh... sure! Yeah, we can definitely do something tomorrow."
    show AE neutral
    AE "Like what?"
    MC "Oh, um, I dunno? Maybe just, like, take a walk around campus together?"
    AE "Around campus?"
    "Shiori-chan seemed a bit hesitant at the idea. But after a small bit of silence she piped up."
    show AE happy
    AE "I'd... I'd like that."
    MC "Cool. Tomorrow then?"
    show AE neutral
    AE "Of course."
    MC "All right! See you in class."
    "I went to turn around before Shiori-chan grabbed the sleeve of my shirt delicately."
    AE "H-hotsure-san?"
    MC "Hm?"
    show AE embarrassed
    AE "Will... will you, um..."
    AE "W-walk me to class?"
    "I smiled at her softly, and waited for her to walk by my side."
    MC "Absolutely."
    jump daymenu

label AE027:
    $setProgress("AE", "AE028")
    scene Hallway with fade
    MC "Mgn... {i}Haaahn~{/i}"
    "This morning was eventful to say the least. At five in the morning my clock sounded off and scared me senseless, clearly taking exception to its poor treatment the other day. Without thinking, I shot out of bed and hurriedly put on my clothes before running out the door."
    "It wasn't until I saw no one else out that I realized my mistake."
    "I decided to walk the campus till class was open, but as people began to pop up here and there I noticed some strange things."
    MCT "What's everybody whispering about?"
    "At first it felt like my mind playing tricks on me due to sleep deprivation, but after a few times I started to get suspicious."
    MCT "Did something happen? Is it about me? Is my shirt on backwards, or...?"
    "After a quick inspection of myself I found..."
    MCT "Oh... Oh no, it's-it's actually inside out."
    MCT "Crap."
    "Accompanied by the giggles of some girls with chipmunk-esque cheeks, I ducked behind some lockers and oriented my shirt, watching carefully that no one was looking."
    MCT "Okay, got it. I hope I didn-"
    FemStudent1 "Was that the president's boyfriend?"
    MCT "...Huh?"
    FemStudent2 "I think so."
    FemStudent1 "I can't believe it. Like, I would have never guessed."
    MCT "What are they...?"
    "I exited my hiding spot in the corner and walked out in the open towards the girls."
    FemStudent1 "Y'know, she once had me clean all the windows because I put gum on the-"
    MC "U-um, hey, ladies. What's going o-?"
    "Deliberately, the girls turned away and began to look about anxiously without talking."
    MC "-n with...?"
    FemStudent1 "Oh, hey there! I love your hair."
    MC "Oh, uh, thanks?"
    FemStudent2 "Mhm! Y'know, I think Matsumoto-san is such a cute-"
    "The first girl jabbed the other girl hard with her elbow, which elicited a tiny peep."
    FemStudent1 "Welp, we should get heading to class!"
    MC "Wait, I actually wanted to ask-"
    "Before I could continue, the girls ran off and left me in a state of utter confusion."
    MCT "Ooookay? That was... no, you know what, that was more than weird. What the hell?"
    "I took another look around, yet nothing. No answers or even any more people in sight."
    MCT "Hmn... something weird is going on... eh, I should just get to class. Hopefully I can get away from this weirdness."
    scene black with fade
    scene Classroom with fade
    MC "Oooor not."
    "When I entered the classroom, my fellow classmates were already there despite it being so early. They were talking amongst each other until the very moment I walked in the room; heralded by 'Shh, here he comes!'"
    show GTS happy at Position(xpos=0.05)
    show FMG surprised at Position(xpos=0.20)
    show BE surprised at Position(xpos=0.35)
    show PRG happy at Position(xpos=0.95)
    show BBW neutral at Position(xpos=0.75)
    MC "..."
    All "..."
    GTS "Good morning, Hotsure-sa-"
    FMG "Is it true?! Are you and Shio-"
    BE "Kei-chan for real?! The president?!"
    MC "Wait, hold on-"
    BBW "Perhaps you can be a humanizing influence on our dear president."
    PRG "I'm... really ha-"
    FMG "No way in hell that'd happen!"
    MC "Um, girls?"
    show GTS sad 
    GTS "Oh dear. I apologize for all the noise, Hotsure-sa-"
    BE "I can't even remember the last time you dated anybody!"
    MC "OY!"
    All "..."
    MC "What is going on here?!"
    "The girls all looked to the side aside from Yamazaki-chan, who tilted her head and spoke plainly."
    show GTS neutral
    GTS "Well, it appears that there is a... rumor going around."
    show FMG happy
    FMG "Did the two of you bang yet?!"
    MC "Eh?! What even-"
    "As I talked, Shiori-chan walked into the room with a look of surprise and confusion on her face."
    show AE angry at Position(xpos=0.55, xanchor=0.5, yalign=1.0) with dissolve
    AE "What is going-?!"
    show AE neutral
    show BE neutral
    show PRG neutral
    AE "...Oh. You're all here early..."
    "She took something that was sticking out of her bag and stuffed it further in before adjusting her glasses."
    MC "G-Good morning."
    show GTS happy
    GTS "Good morning, Matsumoto-san."
    AE "Good morning Hotsure-san, Yamazaki-san."
    BE "Ah, see, Hotsure-SAN. Nothing after all."
    show BBW angry
    BBW "You don't know yet!"
    MCT "What is even happening?!"
    "I beckoned to Shiori-chan and she begrudgingly leaned forward, her wide hips accidentally pushing away her own desk."
    MC "So, something really weird is going on today and I have no idea what's happening. Do you know anything?"
    AE "You don't need to whisper. Just act normally, and go about your business. This foolishness will end on its own. For now try not to... try not to let anyone know."
    MCT "Hm? Try not to let anyone know...?"
    MC "Okay, yeah, but-"
    "Before I could finish, Shiori-chan leaned back forward to her own desk."
    show BE neutral
    BE "Kei-chan, what was that about?"
    MC "N-nothing. Just, y'know, forgot my homework."
    AE "You did?"
    MC "Wait, no, I-"
    show AE angry
    AE "Hotsure-san, I'm disappointed. Today's assignment was very interesting."
    MCT "Save me from this hell."
    MC "O-oh, no, wait. It's right here! Ha ha. Guess I was worried about nothing."
    show AE neutral
    AE "Oh... I see."
    show BBW neutral
    BBW "Wait, then what were you two-"
    MC "{i}HAAAAAHN~{/i} Man I woke up early! I spent my whole night working on homework, I barely got any sleep."
    show AE happy
    AE "Mmm, I appreciate the hard work, but you need rest, Hotsure-san. I don't want you to fall behind."
    MC "Ah, Thank you, Shiori-chan."
    show BE surprised
    show FMG surprised
    BE "-chan?!" #Honoka and Akira say it, merge it somehow?
    MC "E-erm..."
    show AE neutral
    AE "..."
    FMG "Yooo! What?!"
    PRG "S-so then the rumor is true?"
    MC "Wait- What do you mean?"
    show BBW neutral
    BBW "I brought us all here because I heard you'd woken up early. I had some acquaintances of mine wake up the class because I wanted to have you confirm with-"
    show BE angry
    BE "That's not what happened at all! I just woke up early."
    show FMG neutral
    FMG "Yeah, I was up early lifting."
    show GTS neutral
    GTS "I as well was tending to the garden."
    BE "In fact, it was one of the other girls who woke YOU up to tell you."
    BBW "..."
    PRG "Y-you woke me up early, Nikumaru-san."
    show BBW happy
    BBW "As I said, I woke our class up early to meet you here."
    MCT "Uhuh..."
    MC "How did you know I'd get here before Shiori-chan?!"
    FMG "She always gets here at the same time... every day... since school started."
    show AE sad
    AE "Well... I like to have a punctual schedule."
    MC "A-anyways, go on, Kodama-chan." #chan?
    PRG "W-we um, h-h-heard that you were really close to Shiori-san the other day."
    MC "So then someone was spying?"
    show AE angry
    AE "Is that so?"
    "Shiori-chan stood from her seat and looked around the room."
    AE "Who was it, hm?"
    "Almost instantaneously, all eyes in the class were on Nikumaru-san, filing her nails in her seat."
    show BBW angry
    BBW "Wh-ah-tch- I did not!"
    MC "Erm... I kind of doubt Nikumaru-san was sneaking around. She isn't exactly..."
    BBW "Isn't exactly what?"
    MC "N-nothing! Sor-"
    BBW "PAH!"
    AE "..."
    show BBW neutral
    BBW "Well... I was simply shocked, was all. It'd be absolutely horrid of me to ignore the well-being of my fellow students, right?"
    AE "A-I will have you know that invasion of privacy is a very serious-!"
    MC "Um, Shiori-chan."
    AE "-offense and I-"
    show AE neutral
    AE "...Hm?"
    MC "It's okay. I got this."
    MC "Uh, yeah, it's true. Shiori-chan and I are going steady."
    AE "..."
    FMG "Huh, didn't know you liked 'em like that-"
    show BE angry
    BE "Mizutani-chan, that's rude!"
    show AE embarrassed
    AE "N-now hold on, everyone sit down and-"
    TS "Hey, what's going on in here?"
    show AE neutral
    AE "Stand."
    TS "Oookay, yep."
    AE "Bow."
    TS "Alright, you all done? What's the issue?"
    AE "Well... it would appear word is out that Hotsure-san and I are dating, sir."
    TS "Wha..."
    TS "O-oh... well, listen, if you all can get this middle school garbage out of the way we can begin."
    AE "Yes, sir, I apologize."
    TS "All right then. So, today's lesson-"
    scene black with fade
    scene Classroom with fade
    "Class went by fairly regularly. I felt a bit strange; as though all eyes of the class were on me."
    TS "And that's what he meant by 'Cut his head off with a daikon.'"
    TS "Any questions? No? Good."
    "After standing and bowing, I was going to talk to Shiori-chan until I was beckoned over by someone..."
    $secondHighest = getSecondHighest("AE")
    if secondHighest == "BE": 
        jump AE027_BE
    elif secondHighest == "BBW": 
        jump AE027_BBW
    elif secondHighest == "FMG": 
        jump AE027_FMG
    elif secondHighest == "PRG": 
        jump AE027_PRG
    elif secondHighest == "GTS": 
        jump AE027_GTS
    else:
        jump AE027_BE #If for some reason noone is the second highest, it'll default to Honoka.

label AE027_BE:
    show BE neutral
    BE "Hey, Kei-chan, got a sec?"
    MC "Oh, hey, Honoka! What's up?"
    BE "Mm, not much. Hangin out."
    BE "..."
    MC "..."
    BE "Um..."
    MC "Yeah?"
    BE "I'm super happy for you!"
    MC "Oh! Thanks, Honoka."
    show BE neutral
    BE "It's just... why her, again?"
    MC "Um... why-?"
    show BE surprised
    BE "D-don't get me wrong, I mean, she's cute! I just... wow, I didn't expect that."
    MC "Oh. Is that... do you have a problem with-?"
    BE "No, no, not at all. She's just, like... REALLY serious and stuff."
    MC "Well, yeah. But she's an amazing person. You really should try to get to know her. I think you'd make great friends."
    show BE sad 
    BE "Mmm, I dunno. She got me in trouble just for talking too loud. I don't talk loud though!"
    MC "Well, I think the two of you will get along eventually."
    show BE neutral
    BE "Hmm, I'll try! Any friend of Kei-chan's is a friend of mine!"
    hide BE neutral with fade
    jump AE027_after


label AE027_BBW:
    show BBW neutral
    MC "Hey Nikumaru-sa-"
    show BBW happy
    BBW "I knew it! I knew it all along!~"
    BBW "I'll have to admit, I was thrown for a bit of a loop by the 'Hotsure-san' title, however I just knew the two of you were an item!"
    MC "Y-yeah, about that. Why did you spy on us the other day?"
    BBW "While I realize it was a bit crass of me... this is a major opportunity!"
    MC "Opportunity-?"
    BBW "To think, you have the entire student council in your pocket, which by extension means I do as well! Do put in a good word for me, will you, dear?"
    MC "W-wait, I'm not going to-"
    show BBW neutral
    BBW "Mhmhmhm~ Don't worry, it's just a little joke. I was simply curious about a friend's life is all. You understand that."
    MC "Oh. Well, yeah, I guess so."
    BBW "Wonderful. I may have my... reservations about your taste in women, but I'm quite glad for you."
    MC "Thank you, Nikumaru-san."
    BBW "Mhm~ Oh, and by the way, remember my advice, will you?"
    hide BBW neutral with fade
    jump AE027_after    

label AE027_FMG:
    show FMG neutral
    FMG "Oy, Oy, c'mere. I got some stuff I wanted to talk about." #uhhhh
    FMG "Hotsure-san."
    MC "Hey Mizutani-san, how are you-"
    FMG "'Mere."
    MC "Eh?"
    MC "Oh, okay..."
    "I walked over to a straight faced Mizutani-san, her muscular arms propping her up against her desk..."
    MC "Gak-!?"
    "And was greeted with a swift and thunderous pat on the back, popping it in what felt like nine different places..."
    show FMG happy
    FMG "Hah! So you got yourself a girl, eh?!"
    MC "Pah... ahn... yeah, uh... Shiori-san is, um... {i}khm{/i} she's great."
    show FMG neutral
    FMG "I'm telling you, I would have NEVER expected you to go for her. Not in a million billion years."
    MC "Huh? What makes you say that?"
    FMG "Well, don't mean to be THAT girl, but... have you SEEN her ass? Like, do your bangs blind you that much?"
    MC "Y-Yeah, I know she has a big... {i}khm{/i}..."
    show FMG surprised
    FMG "...Oh no way. Do you... do you think that's hot?!"
    MC "U-um..."
    show FMG neutral
    FMG "Are you for real right now? Wow! I mean... that's so weird! I mean... really?!"
    MC "Hey I hope you don't mind but... that's a little rude."
    show FMG sad
    FMG "Ohp, sorry, didn't mean it like that. No offense to you. Shiori though... hmph."
    MC "Do you have a problem with her?"
    FMG "Eh... I dunno. We don't see eye to eye a lot of the time."
    show FMG happy
    FMG "Still though, you're my friend. There's no way in hell I'd let past grudges affect that."
    MC "Well... thank you, Mizutani-san. That means a lot."
    show FMG neutral
    FMG "It's just... I'd think you'd want a girl that's a bit less flabby, is all. It just goes against my expectations."
    FMG "Ehh, anyways, I've talked long enough. Good luck with the gal pal!"
    hide FMG neutral with fade
    jump AE027_after

label AE027_PRG:
    show PRG neutral
    PRG "U-um, Hotsure-san? Can we talk, please?" #Changed to we
    MC "Ah, hello, Kodama-chan."
    PRG "So, um, Shiori-san is really cute."
    MC "Eheh, glad you think so."
    PRG "Um..."
    PRG "So, I was wondering... how o-open is Matsumoto-san?"
    MC "Um... I'm sorry?"
    show PRG sad
    PRG "N-nothing!"
    PRG "She's just... r-really lucky to have someone like you, is all."
    MC "Ehe, thanks, Kodama-chan. If anything, I'm the lucky one."
    show PRG neutral
    PRG "You're really brave, too. I-It's hard for me to look her in the eyes..."
    MC "You think she's scary?"
    show PRG sad
    PRG "Eep! I'm sorry!"
    MC "Oh, no! I wasn't offended!"
    show PRG neutral
    PRG "Um... not really scary. Just v-very assertive."
    MC "Heh, that I can see."
    show PRG happy
    PRG "W-well, I hope you are happy with Shiori-san. I hope the two of you make really cute babies together. I'll look over them for you whenever."
    MC "Eh? W-wait, I think that may be a bit too far, right?!"
    hide PRG happy with fade
    jump AE027_after

label AE027_GTS:
    show GTS neutral
    GTS " I apologize for the intrusion, Hotsure-san, but I would like to speak with you."
    MC "It's nice to see you, Yamazaki-san."
    show GTS happy
    GTS "It is nice to see you as well."
    show GTS neutral
    GTS "Congratulations, Hotsure-san. While surprising, this is rather lovely news."
    MC "Oh! Well, thank you, Yamazaki-san."
    GTS "..."
    MC "Um, Yamazaki-san?"
    GTS "Hm?"
    MC "Did you, uh... have anything you wanted to say?"
    GTS "Not that I could think of, no. Simply that I hope the best for you."
    "Yamazaki-san closed her eyes and bowed, smiling gently."
    show GTS happy
    GTS "My friend and my classmate are both happy, and that's all I could ever hope for."
    MC "Yamazaki-san... thank you. That really means a lot."
    show GTS neutral
    GTS "Hm~"
    GTS "The two of you are welcome in the garden any time, of course. I'm thinking of planting some yellow roses. I hope you both enjoy them."
    MC "Oh, okay, cool!"
    hide GTS neutral with fade
    jump AE027_after

label AE027_after:
    "After she walked away, I went out to go speak with Shiori-chan, who was waiting for me right outside the door."
    jump daymenu

label AE028:
    scene Classroom with fade
    play music Peaceful
    $setProgress("AE", "AE029")
    "Students piled out of class, ready for their afternoon meal. The day went by fairly regularly, though today Tashi-sensei walked in with a big pink stain on his shirt; snickering ensued, shushes were issued. By the end, we were all ready to head out."
    MCT "Ah, there she is."
    MC "Oy, Shiori-chan!"
    show AE neutral with dissolve
    AE "Good afternoon, Hotsure-san. Nice weather today."
    MC "A good day to go to the roof then, eh?"
    show AE happy
    AE "My thoughts exactly."
    "I smiled at her warmly. It was nice to see her so friendly and relaxed... at least as far as relaxed can be for her."
    scene black with fade
    "We walked together towards the staircase. As we walked, we discussed many different topics. How our days went, how we're doing in class, and of course, the different tasks Shiori-chan had to carry out as class president."
    "I followed her lead up the stairs; taking the admitted glance every once in a while. Her skirt had recently begun to ride up even further, signifying that she'd been growing a lot recently. I looked to my own hair and began to lightly pet it. Shiori-chan opened the door and we stepped out into the light."
    scene Roof with fade
    show AE happy with dissolve
    MCT "Last time we were up here was... less than reputable. I hope it doesn't mar the vibe of the area."
    MC "Same place as before?"
    "I motioned to the metal bench, and Shiori-chan nodded her head and placed a small pillow from her bag on the iron grate before sitting down."
    MC "Ah, nice thinking."
    show AE embarrassed
    AE "Mhm. I wouldn't want to mark myself again. I couldn't feel anything... back there for a good while last time."
    MC "Heh."
    "I sat down next to her. To my expectations, her behind took up much more space than before. My hand, tactically placed at my side, brushed past her exposed flesh as I sat, causing her to bristle slightly."
    MC "O-oops. Sorry, Shiori-chan."
    if getAffection("AE") > 10: #half
        AE "N-no need to apologize, Hotsure-san. I don't... I don't mind that much."
        "I blushed slightly and rubbed the back of my neck."
    else:
        AE "Y-yes, well... ensure it doesn't happen too often."
        MC "Ah..."
        show AE neutral
        AE "If you please, that is. I'd prefer it so that-"
        MC "R-right, yeah-"
        show AE embarrassed
        AE "Ah-Mhm... *khm*..."
    "The clouds overhead cast a large shadow on the roof as it blocked the sun at its zenith, giving respite from the warm rays of the bright sun."
    MC "Mm, clouds coming in."
    show AE neutral
    AE "Oh? The forecast didn't call for rain, thankfully."
    MC "As long as we don't get hit, it'll be fine. You don't need to worry anyways."
    AE "Oh?"
    MC "I'd guard you from the rain if it starts."
    show AE embarrassed
    AE "Ah."
    "Shiori-chan sheepishly smiled and brushed her hair to the side with her hand."
    show AE happy
    AE "Mhm~ Well... I'll hold you to that."
    MC "Hmm..."
    AE "J-Just don't sacrifice your notebook in the process."
    MC "Ahaha~ It's turned out well for me so far."
    AE "Ehehe."
    MC "Heheh..."
    "We looked out towards the grassy green hills. I closed my eyes and took a deep breath of the fresh air."
    MC "Haaaan~"
    AE "The wind is so soothing."
    MC "Mhm..."
    "Opening my eyes, I grinned happily; thankful to the days of peace I'd been blessed with recently."
    show AE neutral
    AE "...You know..."
    show AE embarrassed
    AE "Um..."
    AE "...3.57 times the square root of your height."
    MC "Eh?"
    "Shiori-chan fidgeted a bit in her seat and looked up at me."
    AE "That's... that's how far away the horizon is."
    MC "..."
    $setSkill("Academics", 1)
    MC "Ehe... you remembered."
    show AE happy
    AE "Mhm. I-I looked it up recently."
    MC "What compelled you to do that?"
    show AE neutral
    AE "Hm? Oh..."
    show AE embarrassed
    AE "I just figured it's what a good g-girlfriend would do."
    MC "Ah..."
    MC "It most certainly is."
    show AE happy
    AE "Don't take that as me spoonfeeding you information all the time though. Look things up for yourself every once in a while!"
    MC "I know, I know!"
    "We smiled at each other and looked back out to the horizon."
    MC "3.57 and the square root of my height, eh?"
    MC "Wow... not that far, I guess."
    "The wind kicked up a bit around us. The sky was a nice mixture of azure beauty and silvery clouds, yet I hadn't felt a drop on me."
    "Still though, being up there had kicked up some memories from a while back."
    MCT "Should I... should I bring up how I've felt... about the last time we were up here?"
    menu:
        "Keep it to yourself":
            MCT "No... no I don't want to spoil the mood. We can stay like this for a while."
            MCT "I feel weird about what she did, but..."
            MCT "I'm fine with just letting it go."
            "I slumped back further in my bench as I put my hands on my stomach, letting out a sigh of content."
            jump AE028_c1_after
        "Say something":
            jump AE028_c1_2

label AE028_c1_2:
    MCT "It just... it feels too weird."
    MCT "I have to at least talk to her about it."
    MC "Um, Shiori-chan?"
    show AE neutral
    AE "Hm?"
    MC "I wanted to talk. About... last time we were here."
    show AE embarrassed
    AE "...Oh."
    AE "Did you... tell anyone?"
    MC "N-no, no, I haven't."
    MC "It's just..."
    menu:
        "That was messed up.": #-1
            jump AE028_c2_1
        "Couldn't there have been a better way?": #+0
            jump AE028_c2_2
        "I didn't expect that.": #+1
            jump AE028_c2_3

label AE028_c2_1:
    MC "That was messed up. What you did."
    AE "..."
    MC "I mean, you came up here and just... showed me... your behind and tempted me."
    MC "That's messed up."
    $setAffection("AE", -1)
    AE "I... I'm sorry, Hotsure-san. I just figured..."
    "Shiori-chan shifted around a bit and moved her thumb in a circular motion on her skirt."
    AE "I figured it would have given me the answer I wanted."
    MC "But you outright tempted me though, without even asking me how I felt."
    MC "If I was anyone else, who knows what would have happened."
    show AE sad
    AE "..."
    AE "I'm sorry. I'd... I'd made a horrible mistake that could have ruined our relationship. It's just, I didn't know what kind of relationship we had that I'd ruin."
    if getFlag("AE024_grabbedass"):
        MC "Right, but then you went on to both kick me and then turn around to say I broke the rules."
        MC "I'm sorry, but that just makes you look manipulative. Were you trying to look cool? "
        show AE sad
        AE "..."
        AE "I... I..."
        show AE embarrassed
        AE "I cannot apologize enough. I'm sorry. If someday I can make it up to you, anything... I'll do it. I just... I had to know."
        MC "Shiori-chan..."
    jump AE028_c2_after

label AE028_c2_2:
    MC "Couldn't there have been a better way to gauge my intentions?"
    AE "I... *ahem*... I perhaps was a bit too forceful."
    show AE sad
    AE "T-to be honest, I was unsure and willing to risk a lot by doing so."
    MC "You could have just asked me. I would have understood."
    AE "Yes, b-but I just didn't..."
    show AE embarrassed
    AE "I was worried about our relationship. It clouded my judgement."
    MC "Our relationship?"
    AE "I was... admittedly interested in you, too. As you can guess, I'm not very good at dealing with romantic situations."
    MC "...Shiori-chan."
    jump AE028_c2_after

label AE028_c2_3:
    MC "I have to admit, I really didn't expect that of you."
    AE "Hm?"
    MC "You took some very provocative risks, and you were way more... forward than I'd expected."
    AE "...Indeed."
    MC "I kind of... I suppose I expected more from you."
    show AE neutral
    AE "What do you mean?"
    MC "Well, you're usually extremely well-composed and levelheaded, but what you did seemed kind of foolish."
    $setAffection("AE", 1)
    show AE sad
    AE "...Ah."
    MC "But don't worry, I guess it's just that, well, since I expect the best from you. So it caught me off-guard."
    show AE neutral
    AE "...You really expect the best from me?"
    MC "Shiori-chan..."
    jump AE028_c2_after

label AE028_c2_after:
    MC "It was foolish, yeah... but I wanted to say I forgive you. I know you're new to relationships and, while unexpected, it gave me a glance of how much you care."
    show AE happy
    AE "...Thank you, Hotsure-san... that means a lot."
    jump AE028_c1_after

label AE028_c1_after:
    "I lightly sniffed at the air as a curious scent piqued my nose."
    MC "Hm... smells like rain."
    show AE neutral
    AE "Really? But I checked the forecasts..."
    MC "Well, they're not right 100%% of the time, it seems."
    show AE embarrassed
    AE "I suppose not..."
    show AE neutral
    AE "Still though."
    "Shiori-chan took a deep breath and smiled."
    show AE happy
    AE "I love the smell of petrichor."
    MC "Petrichor?"
    show AE neutral
    AE "Mhm. It's the smell from aerosols in the ground during rain. It's a soothing scent."
    MC "Oh yeah... I think I've heard that word before."
    MC "Hm... fancy that."
    "The faint smell permeated the air as I sat upright and turned my head to the side."
    MC "Welp, we better head inside before it starts to rain."
    MC "Ready to-"
    play music Rain
    show AE sad
    AE "Hotsure-san, wait."
    MC "Hm?"
    "Shiori-chan looked at me in a somber yet somewhat distressed way."
    AE "There's something I wanted to tell you..."
    "The wind picked up slightly, breezing past my ears."
    MC "Yeah? What's up?"
    AE "If I... If I start to change... as a person, I want you to know I won't be hurt if you leave."
    MC "...What?"
    AE "If I... If I lose who I am... feel free to abandon me. I don't want to take you down with me."
    AE "If I'm to die in shame, I would want to die alone."
    "A spike of adrenaline rushed through my mind at the shocking words Shiori-chan just spoke."
    MC "Die?! What-what-what are you talking about?"
    AE "Not a literal death, of course, but... a death of who I am."
    MC "Who you...?"
    show AE neutral
    AE "Put quite simply, people like me are always treated like the villain. The one who comes along and ruins the fun of others, who enforces rules at the most inopportune time. The one who needs to be humiliated and ridiculed, to be brought down to earth."
    show AE embarrassed
    AE "...Hmn..."
    show AE sad
    AE "I guess... simply put, I don't know why I'm the one who is expected to change. To have some sort of 'moment of enlightenment' where I suddenly change my entire personality."
    AE "I don't want to become docile. I want to stay who I am. I'd rather face the inevitability of my fall as me."
    MCT "There it is... the talk of fate, once again."
    MC "..."
    AE "...Don't get me wrong, Hotsure-san, I understand the necessity to adapt or die, and I understand the need to adhere to certain social standards, it's just that I don't understand why I can't just be me. My love for efficiency, order, law... I don't want that to disappear."
    MC "And I don't want that either! It's just... I don't see why you think..."
    MC "I dunno."
    MCT "This is such an absurd topic. I don't understand what she means."
    AE "Hm... well, in any case, I suppose I'll simply have to wait..."
    AE "Wait for the death of my personality."
    play sound ClockTower
    MC "..."
    show AE neutral
    AE "Until then... I'm more than happy spending every moment with you."
    MC "Shiori-chan... I-"
    play sound Thunder
    AE "Hm?"
    MC "C-come on, let's get off the roof, before we experience an actual death."
    AE "M-Mm."
    "We stood up together and Shiori-chan grabbed her pillow to put back in her bag. We rushed inside in order to get out of the rain, and back to class."
    play sound Stomach
    MC "U-um, Shiori-chan?"
    AE "...Hm?"
    MC "Next time, let's bring lunch with us."
    show AE happy
    AE "...Eheh..."
    AE "Sure thing, Hotsure-san."
    scene Classroom with fade
    "As we walked back to class, I thought more and more about the ominous words Shiori-chan said."
    MCT "Death of her personality? I don't get it. What does she mean? Is it some cliché I'm not in on?"
    show AE sad with dissolve
    AE "So... tomorrow I have to head back to my room after class to pick up some things, then I have a meeting. We won't have that much time to spend together."
    MC "O-oh."
    MC "Well... maybe I can... go with you to your room?"
    show AE neutral
    AE "Oh?"
    show AE embarrassed
    AE "A... A boy in my room?"
    "Shiori-chan looked off to the side a bit, before seemingly remembering something."
    AE "My room is a disaster. You wouldn't want to-"
    MC "N-No, it's fine. I still want to at least check it out..."
    show AE neutral
    AE "Oh."
    show AE embarrassed
    AE "Well... all right. I'll make sure there's nothing against it in the rulebook."
    show AE neutral
    AE "Until then, let's head into class."
    MC "Mm, good suggestion."
    "We headed back in, and after a seemingly long lesson with rain hitting the window panes, we all left. We walked back to class silently, her words still resonating in my head."
    jump daymenu

label AE029:
    $setProgress("AE", "AE030")
    scene Dorm Exterior with fade
    play music Peaceful
    "After class, Shiori-chan and I got up together and made our way to her room. After yesterday's events, I figured it would be nice to see what Shiori-chan's room was like, get a closer look at how she's living."
    show AE neutral with dissolve
    MC "So, you got the okay?"
    AE "Mhm. I double checked. You can be in my room to visit any time before nighttime."
    MC "So, I gotta say, I'm a bit excited."
    AE "I'm not entirely sure why, it's only my room."
    MC "Well, yeah, but I dunno, I just kinda want to see what you call home."
    AE "Hm..."
    AE "It's in a bit of a state. I hope you don't mind, but... she's very particular about her side of the room."
    MC "...She?"
    AE "My roommate."
    MCT "Shiori's roommate? Oh yeah, she never said anything about her."
    MC "So... what's she like?"
    "We got to her door, and she input her key code. After a high beep and a green light from the pad, a click sounded out as Shiori-chan grabbed the handle."
    AE "See for yourself."
    "Shiori-san pushed the door open and we stepped in together."
    scene Dorm AE with fade
    "My eyes were immediately drawn to the left side of the room. It was hard for them not to be. The room smelled fresh, with a nice apple-cinnamon scent. The window had white curtains which created a bright glow from the sunlight, gently bouncing off the pristine, spotless carpet onto the mirrors of a white wardrobe."
    "Along the wall, bookshelves held a good many books and folders, a desk in between with stacks of paper in two neatly kept bins. Next to the window, a white nightstand, and next to the nightstand, a massive white bed, of which the sheets, blankets, and coverings had not a single crease or wrinkle."
    MC "W-wow, Shiori-chan! Your room looks... really good! It must take a lot of work to get it to look like this."
    show AE happy with dissolve
    AE "Thank you for the compliment. I indeed put a lot of work into the room's upkeep."
    show AE angry
    AE "...MY side, that is."
    MC "Eh?"
    MC "Hrgk-!"
    "I turned my head to the right and immediately got assaulted by the stench of sweaty sock, onion, and what I assumed was the olfactory equivalent of parental regret."
    "In strict opposition to the haven of cleanliness to the left, the right side of the room was absolutely atrocious. An empty pizza box lay abandoned and forgotten on the far side of the room, and next to it rested a mini-screen TV, hooked up to an old 90's-era video game console with black wires tangled in a mess."
    "The floor was littered with junk listlessly tossed about. An acoustic guitar covered from neck to base with various stickers and Kanji written in marker lay on the bed, along with sheets and blankets piled up in random mounds."
    "The only respite from the mess was the kitchen, which in itself had been kept clean; no doubt by Shiori-chan. Between the trash, the stench and the clothes thrown about, I'd say the disaster was fit more for a pig than a girl."
    MC "Urg..."
    AE "Aha! It's horrid to you too then. If even a few more people attest to its atrocious state, she'll have no choice but to let me clean it!"
    "I looked on the ground near my feet and saw a ragged and crumpled piece of cloth."
    AE "Article three of the Dorm Room Health and Safety Protocol clearly states that-"
    MC "U-um, Shiori-chan, what's-"
    "I unraveled the cloth and realized bit too late that what I had in my hands was a huge pair of black panties with broken red hearts covering the design."
    MC "E-ech!"
    show AE embarrassed
    AE "Oh! Oh-dear God, Hotsure-san-"
    MC "Okay, yep, where should I-"
    AE "On the ground, I-I'll get it later."
    MC "Maybe I should just place them on her floor."
    UNKNOWN "Pfft, ehe~"
    MCT "Hm?"
    "Shiori-san and I were silent for a moment upon hearing the snicker. While I looked on in confusion, Shiori-sans eyes flamed with anger and contempt."
    show AE angry
    AE "Do not step on her side of the room."
    MC "Eh?"
    MCT "Is... everything alright?"
    MC "I mean... there's a lot of junk everywhere, but..."
    show AE neutral
    AE "I-Listen, anywhere on my side is fine. I'm telling you now: if you go on her side, you'll regret it."
    MC "..."
    MCT "I'm gonna do it."
    show AE angry
    AE "Ahp! A-mn-okay, I warned you."
    hide AE with dissolve
    stop music
    "I stepped forward and placed the panties on the bed as not to be rude by throwing them, and then, just then..."
    MC "...Oh look nothing happened."
    show AE neutral
    AE "Five, four..."
    MC "U-um, Shiori-chan, why-"
    AE "Three, two..."
    MC "Have I made a mista-"
    AE "One."
    "I turned around just in time to catch a spring loaded pad covered in baby powder... to the face."
    MC "MGHPH!?"
    play music Busy
    UNKNOWN "A-HAHAHAHA! Ohhh my god, that was bad~!"
    "Out from the bathroom door came a girl, clutching at her stomach and cackling loudly like a hyena."
    show AE angry at Position (xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show Tako neutral at Position (xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    AE "Ngh, Yureno-san!"
    Tako "Oy, oy, Shio-rear, what, didn't hear me in the bathroom?"
    AE "I thought I told you not to call me that!"
    MC "H-hey! What's going on?!"
    Tako "Ehehehe."
    "I took off the pad from my face, and sputtered as I tried to get the powder out of my mouth."
    Tako "Sorry about that dude, she warned you though, right?"
    "As I wiped my eyes, the girl came into plain view. She was a somewhat taller girl, around my height actually, with a toothy grin plastered across a soft and feminine face. Her hair was a light brown color with a golden blonde tips."
    "Her hair was mostly covered, however, by a grey beanie with a pin on it. Her tattered denim jacket sported more pins with various anime characters and bands, but was left opened to reveal her untucked school shirt."
    "I could tell she wasn't exactly the type to take things seriously; from her weird hat to her unkempt jacket, she seemed like one of those carefree types."
    "From demeanor, to dress, and even their sides of the rooms; the two were polar opposites in every way."
    "Aside from one glaring similarity."
    #show Tako zoomin
    #Boing sound effect
    #pause 2
    #reset
    Tako "Hey, you must be Keisuke-san, right?"
    MC "Y-yeah."
    show AE neutral
    AE "You don't need to answer that, Hotsure-san."
    Tako "Daaaww, shy? Isn't that Kodama-chan's thing?"
    show AE angry
    AE "How many times have I told you to clean up your side of the room?!"
    "Shiori-chan reached for an empty two-liter when she was stopped by the girl."
    Tako "Woah, woah, ey, don't touch that! I might use it."
    AE "Ach-For what?!"
    Tako "Like... uh..."
    AE "And the rest of this-this trash, hm?"
    Tako "I'll get to it, geez!"
    "Shiori-chan, I could tell, was uncomfortable with the girl's mere presence. She let out a sigh and rubbed her eyes under her glasses."
    show AE neutral
    AE "Don't you have friends to go spend time with?"
    #if romance
    Tako "Mm... well, I did, but I wanted to see your catch!"
    MC "Um, c-catch?"
    Tako "Her fling? Lover? Boyfriend, dummy."
    #else
    #Tako "When I told 'em ya finally made a friend, a guy nonetheless, they all thought I was lying my ass off! And trust me, it's a lot to lie off!"
    #MC "Eheheh"
    "Yureno-san put her face right up to my own, hands on her massive hips. As she looked me in the eyes, a pungent wave of wet dog odor hit my nose all at once. I stifled back a cough; I didn't want to be rude."
    Tako "Huh, he actually looks normal... what's his deal, Shiori?"
    show AE angry
    AE "His 'deal' is that he's clearly uncomfor-"
    Tako "Ohp! I got it, it's the hair, right?"
    MC "Oh... um... yeah."
    Tako "Hah! Knew it."
    "The girl took a seat on the floor, using her ass as a cushion, and pulled out a small game device to start playing."
    show AE angry
    AE "Yureno-san, how many times have I told you-"
    Tako "Stop using my ass as a couch, I know."
    MC "She probably doesn't want you to get your skirt dirty."
    "The girl looked up at me and squinted, pursing her lips."
    Tako "Ah, so that's how it is. You've been whipped into submission."
    MCT "I-I'm not whipped!"
    Tako "Anyways, names Tako. I like building stuff, I guess."
    "She followed up with a snap of her fingers into a peace sign."
    MC "Y'know... I'm honestly shocked. I never expected two people with such different... tastes to be roommates."
    show AE embarrassed
    AE "The school found it appropriate to room us together. It would mean there would be more efficient... lodging."
    Tako "It's cause we both have big fat asses."
    show AE angry
    AE "Ach-excuse me?!"
    "Yureno-san clapped her game device closed and stood up, before pacing behind Shiori-chan."
    Tako "Hey, Shio-rear, I know I'm gettin' big, but you're REALLY gettin' XXL on me. I don't stand a chance."
    AE "Enough, Yureno-san."
    Tako "Don't take it so personal-like, you make it work, girl!"
    MC "Pftt... ehehe."
    show AE neutral
    AE "Hotsure-san?"
    MC "You two... it's just funny to me."
    Tako "Hm?"
    MC "Tako-san, it's nice to meet you."
    "I stood up straight, and bowed in respect. She looked at me in confusion for a second, before straightening her back and wiping her forehead."
    #if romance
    Tako "...Wow, Shiori-chan, you really got yourself a man, huh."
    "Yureno-san put her hands in her pocket and went to lay on her bed."
    Tako "Ahh, I knew it was gonna happen some day! The baby bird always flies from the nest, the student always has to leave the teacher at some point! I'm an expert on boys, after all, so it's only natural-"
    show AE embarrassed
    AE "T-to call yourself a teacher is absolutely-"
    Tako "Haaaannn~ What to do now?  Soon my dear Shiori-chan is going to be going to town on her new fling; having picnics, getting married, having babies- Oh! Shiori-chan, you'd be super adorbs pregnant!"
    show AE angry
    AE "Enough! Now see here, I-"
    "Hopping up from the bed, she grabbed her keys from off the floor and walked over towards the door."
    Tako "Well, I'm headed to town. Shiori-chan, glad my advice worked out for ya."
    #else
    #Tako "Jeez, no need to be such a stiff man."
    #"She grinned widely at me as she turned around and pushed her butt into me, causing me to stumble back a bit onto the bed."
    #Tako "Lighten up a little, I won't bite!"
    #MC "W-Uh..."
    #Tako "Soft ain't it..."
    #MC "U-Um-"
    #Tako "I'm talkin about the bed, perv! GYAHAHAHAH~!"
    #show AE angry
    #AE "Uch, you're such a child! If I had-!"
    #Tako "Man, I'm bored. Boredboredboredboredbored!"
    #"Yureno-san bent over to pick up her keys, looking back to see if I was staring before chuckling to herself."
    #Tako "I'mma head out. Peace!"
    show AE neutral
    AE "Wait, let me fi-"
    Tako "Nice to meet you, dude."
    MC "Oh, um, nice to meet you, too."
    show AE angry
    AE "Ach... Hm... just, be home before curfew?"
    Tako "You got it, babe."
    AE "Don-"
    Tako "Oh! By the way, I left some cookies in the cupboard for y'all. Later~"
    "Yureno-san walked behind Shiori-chan and lightly bumped their two gigantic tushes together, leading to noticeable jiggling from the two of them."
    AE "Ah! Y-you!"
    Tako "Bubble Booty Babes~"
    hide Tako with dissolve
    stop music
    "As Yureno-san left the room, Shiori-chan's face was filled with a blush like none other I've seen; whether out of frustration or embarrassment, I couldn't tell."
    show AE angry at center with dissolve
    play music Peaceful
    AE "That girl..."
    MC "Heh, she's fun."
    show AE aroused
    AE "Define 'fun'."
    "I looked over to Shiori-san, who was observing the cupboard on the wall intently."
    show AE neutral
    AE "Hmm..."
    "She opened it up, away from herself, and as soon as she did a small spoon catapult launched a wad of gum straight out."
    show AE angry
    AE "Of course."
    MC "Does she do that a lot?"
    AE "Act unruly? Yes. Constantly."
    MC "I meant more of set up traps and things."
    show AE neutral
    AE "Yes... loathe as I am to admit, she's extremely talented."
    show AE angry
    AE "Talent, however, does not equate to aptitude. Her studies are atrocious."
    MC "Hm."
    MC "So... bubble booty babes?"
    AE "Not a word. Ever."
    MC "G-got it!"
    AE "I swear, the girl's obsessed with my rear. She says that's going to be our 'show names'; absolutely uncouth."
    MC "Well, she has a unique sense of humor, I guess."
    AE "Humor?! Ha! I've heard fax machines funnier than her."
    MCT "I'm going to take that literally."
    show AE embarrassed
    AE "I... I hope you don't mind but could you not mention the nickname to anyone? I don't want..."
    MC "Bubble Bo-"
    show AE angry
    AE "THAT nickname to follow me anywhere."
    MC "Oh, um, sure."
    show AE neutral
    AE "Good. Now..."
    "Shiori-chan walked over to her side of the room and thumbed through the files on her desk, grabbing a few and placing them in her bag."
    AE "I hope you don't mind, but I have a meeting and I can't have you in here after sundown."
    MC "Okay, then I guess... tomorrow, then."
    "We walked to the door, and I opened it for Shiori-chan. After exiting, we walked side by side towards the office."
    scene Hallway with fade
    show AE neutral with dissolve
    MC "All right, we're here."
    AE "Okay. I'll see you tomorrow."
    MC "Yep, see you then."
    AE "Oh, and Hotsure-san?"
    MC "Yeah?"
    show AE embarrassed
    AE "Would you like to walk with me to class tomorrow?"
    MC "Yeah, definitely!"
    "Shiori-san gave a weak smile and nodded before entering the library, a loud clack from the door heralding my exit towards my room. As I walked, I thought about the new connection I had made with someone in Shiori-chan's life, and got ready for the next time we met."
    jump daymenu

label AE030:
    $setProgress("AE", "AE031")
    $setSize(3)
    $setTimeFlag("size3")
    scene Classroom with fade
    play music Rain
    "Sitting silently in my seat as the clock ticked by. That would sum up the past few minutes. Shiori-chan hadn't come in yet, and that was strange, because it was well past the usual time she came in."
    MCT "She didn't answer when I knocked... I thought we were gonna walk together today."
    "The morning, however, progressed much in the way I'd expected. Looking in the mirror, I'd noticed that my hair had grown even longer. After brushing it and getting dressed, I walked my usual way to class. I'd honestly hoped I would enter to see her sitting in her chair; her calm demeanor starting off my day."
    "But Shiori-chan was nowhere to be found. I rested my head on my hand, each tick from the clock building onto my heightened feeling of worry."
    MCT "She's usually here by now... what's holding her up?"
    "I started to get antsy, and wondered if I should head to her room to see if she's all right."
    MCT "It's okay. She's responsible, I'm sure she just has to deal with some school work."
    MCT "Yeah, that's it."
    MCT "..."
    MCT "But what if she's hurt?"
    MCT "Gah! I haven't been worried about anyone like this in a long time. What's gotten into me?"
    if getSkill("Academics") > 6:
        MCT "Okay, I need to think logically."
        MCT "...Hmm... It was a while ago, but I do remember her being absent before."
        MCT "I didn't think much of it at the time, but looking back on it was a big deal."
        MCT "Because that day... that was the day her skirt was ripped."
        MCT "Ah!"
        MCT "That must be it. Her skirt's been destroyed by her growth again!"
        "I let out a sigh of relief, successfully rationalizing, or from some points of view fooling myself into believing, that to be the reason for her absence."
        MCT "Okay. Good. She's probably alright."
        show BE neutral with dissolve
        BE "Hey, Kei-chan."
        MC "Hm?"
        "Honoka patted me on the shoulder. I turned to see that she looked somewhat worried, but kept a warm smile up."
        MC "Hey, Honoka. What's up?"
        show BE sad
        BE "You seem a bit out of it today. Is everything alright?"
        MC "Oh, uh, yeah. Shiori-chan is just a bit late, is all."
        show BE neutral
        BE "Hm?"
        BE "That's why you're worried?"
        MC "Yeah, it's not normal for her."
        "Honoka craned her neck to look past her massive mammaries towards Shiori-chan's seat."
        BE "Oh yeah, I hadn't noticed. She's usually super quiet."
        BE "Where's she at?"
        MC "Well, it's just a hunch but... I think she had a wardrobe malfunction."
        show BE surprised
        BE "Ehh? For real?"
        MC "Mhm. The last time it happened was the only time she was out of class, although I'm a bit shaky on the idea that it's the only reason."
        show BE neutral
        BE "Mmm, well, it makes sense. She has a lot of pride in herself, I think. She would go out of the way not to embarrass herself, right?"
        MC "True... she just doesn't seem like the type to value her pride over her responsibilities."
        BE "Me either, but what other explanation do you have that makes sense?"
        MC "None that I'd like to contemplate."
        hide BE with dissolve
    else:
        MC "Um, hey, I hope you guys don't mind, but..."
        show BE neutral with dissolve
        show FMG neutral at Position(xpos=0.2, xanchor=0.5, yalign=1.0) with dissolve
        show BBW neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
        "When I turned around, much of the class looked up towards me. We were a fairly small class, but it still felt weird to be the center of attention in the room."
        MC "Have any of you seen Shiori-chan?"
        "Honoka rested her elbow on one of her enormous breasts and put a finger to her lips."
        BE "Hmm? Uhhh... no, I actually haven't."
        "Mizutani-san, however, continued eying her phone as she rested her head on her arm; legs crossed with one bouncing listlessly."
        FMG "I haven't seen her for a while, man."
        BBW "*Ahem* Pardon, however I think I know why."
        MC "Hm? Nikumaru-chan?"
        "Nikumaru-chan flipped her hair on being acknowledged, something I felt was intentional on the grounds that she waited till both Honoka and I were looking at her."
        BBW "Simply put, Matsumoto-chan's skirts gradually become a bit... worse for the wear over time. I'm sure you've noticed, right?"
        MC "U-um-"
        show BBW happy
        BBW "I'll take your usual stutterings as a confession of guilt, then."
        MCT "Ga-ch!"
        BE "Wait, t-then why do you notice?"
        show BBW neutral
        BBW "Mmm, darling, not a single student passes my eye without thorough wardrobe examination."
        MCT "I... could believe that. Though whether she was looking for potential customers for her business or simply making sure she looked the best in the room, I had no idea."
        BBW "Anyways, though it may as of yet be coincidental, the only times Matsumoto-chan is missing from class is when she's awaiting a new wardrobe."
        BBW "In fact, I believe that last time she *ahem* 'outgrew her apparel', she only left her room to work with lover boy over there-"
        MC "Lover boy?!"
        show FMG happy
        FMG "*Pfft* Heh."
        BBW "-and when she came back to class the next day she had her new skirt."
        MCT "Oh yeah... I remember her being missing from class a while back."
        MC "That... makes a lot of sense, actually."
        BBW "Precisely. As to why she doesn't simply buy a new one beforehand is beyond me. You'd think for as many schedules as she keeps she'd have a bit more forward planning, hm~?"
        MC "But Shiori-chan isn't the type to value her pride over her responsibilities. I couldn't imagine her skipping class over her skirt not fitting."
        BBW "Perhaps not normally, however, I'd suppose that current situations may have changed that."
        MC "How so?"
        BBW "Well? Think about it, where do you sit?"
        MC "Um... A-ah... I see."
        BBW "I doubt she'd willingly skip class unless it could lead to something that would cause a more... indecent infraction."
        show BE surprised
        BE "Woah, Nikumaru-chan, you're way smarter than you look!"
        BBW "Mhm, thank you da-"
        show BBW angry
        BBW "Wait, what do you mean by that?!"
        BE "Eh? W-woah, woah, woah, I didn't mean it like that-!"
        MCT "I do not envy Honoka right now."
        hide BE with dissolve
        hide FMG with dissolve
        hide BBW with dissolve
    MC "Still though, it's hard to think she'd just miss a day every time she outgrows her skirt."
    AE "Which is exactly why I plan for that NOT to be the case."
    MC "Eh?"
    stop music
    show AE neutral at Position(xpos=0.5, xanchor=0.5, ypos=1.0, yanchor=0.5) with dissolve
    "I looked at the doorway, and sure enough, Shiori-chan poked her head out from behind the wall. I smiled at her, my fears dashed and my worry alleviated."
    MC "Shiori-chan! I'm glad you're okay."
    show AE angry
    AE "I'll have you know that my previous absence was for school business and was annulled by the administration. I even went to Tashi-sensei later on to catch up on my work, so I will not tolerate rumors about truancy from me going-"
    MCT "Ah... there's the Shiori-chan I expected this morning."
    MC "Shiori-chan? I hate to cut you short, but Tashi-sensei will be in at any minute. You better head inside or else you really WILL be late."
    show AE neutral
    AE "...Um..."
    "Shiori-chan shrunk back a bit, putting her thumb up to her mouth."
    show AE sad
    AE "*Khm* Yes, well... please take note that my wardrobe is a bit... worse for the wear."
    MCT "So then the theory was correct. Shiori-chan's skirt..."
    AE "Out of respect, I'd like you all to act appropriately and... and..."
    "Shiori-chan's voice gave out a bit, and she spoke in a tone of defeat."
    AE "Avert your gazes."
    play music AE
    show AE sad:
        linear 2.0 yanchor 1.0
    "As Shiori-san entered the room, it was to the mixed reactions of the class."
    "Some, like Honoka and Akira-chan starred with their mouths agape. Alice starred, yet placed her thick fingers over her mouth for politeness. Aida and Naomi, however, did as instructed and looked off in different directions."
    "I on the other hand, began to blush and could not keep my eyes off of my girlfriend's fairly bare figure."
    "Her legs had grown even more; each smooth swollen thigh lightly jiggling with each step. Her hips were now even larger as well, reaching past the length of her shoulders by a good few inches."
    "She got to her desk and started to sit down. In that moment, I could feel my heartbeat in my toes. Her booty had blown up immensely; a fact now made more evident by the pathetic scraps around her waist that were once a skirt. Each pale cheek jutted out a good foot or so from her body, and her panties, now visible to all, were stretched and had dug into her skin tightly."
    "She sat down with a grunt, and the whole room was silent and still. Shiori-chan was blushing bright red and trembling in her seat, which was a trait the two of us currently shared together."
    HR "*Tchaaah~* Okay, class time."
    show AE neutral
    AE "..."
    HR "...Are you gonna do the-?"
    show AE embarrassed
    AE "Oh! Yes, I apologize, sir."
    show AE neutral
    AE "S-stand."
    "I got up from my seat and took a breath in. It was obvious Shiori-chan was uncomfortable with bowing in her current situation."
    MCT "I should close my eyes. It'd save her from further humiliation."
    scene black with fade
    AE "Bow."
    #*Brush*#
    MC "A-"
    MC "..."
    AE "..."
    MCT "What was that...?"
    scene Classroom with fade
    show AE embarrassed with dissolve
    "I looked up to see what my head brushed against, knowing damn well what just happened."
    MC "Ah..."
    AE "..."
    "The two of us, realizing what happened, were stunned. I opened my mouth to talk, but only stammers left my lips. Shiori-chan looked back at me with a face of shock and embarrassment."
    "We shot back up from bowing and Shiori-chan swiftly sat back in her seat. I took a minute to let my legs wobble a bit as I sat down slowly; rubbing the back of my neck as I blew air out of my mouth."
    MCT "It's not like I subconsciously bowed deeper than normal..."
    HR "Hm? What? What happened? I wasn't paying attention."
    AE "Merely a problem with Hotsure-san's bowing posture, sir."
    HR "Aha... Well, then let's begin."
    scene black with fade
    pause 1
    scene Classroom with fade
    "Class had continued on normally, but I couldn't shake the pinkness from my face."
    "Upon Tashi-sensei ending the class, I got up and talked to Shiori-chan as everyone started to leave."
    show AE neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    MC "Shiori-chan, I'm so-"
    show HR neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    HR "Matsumoto-chan, can I talk to you for a moment?"
    "She looked towards me, and then towards him, then back to me."
    AE "This may be important. Wait for me outside of class, Hotsure-san."
    "Not knowing what to say, or what even could be said, I simply nodded."
    MC "Okay."
    "I exited the room, but not entirely, because just as Shiori-chan had earlier, I clung to the doorframe and watched in silence."
    HR "Listen, Matsumoto-chan, the school is somewhat lax with a bit of skin showing every once in a while, but I can tell you're not. I know you can't really do anything about the skirt situation so..."
    HR "If or when the time comes that you can't wear it to class, feel free to just skip out."
    AE "I couldn't do that, sir. As class president I'm expected to be here."
    HR "I get that, and trust me, I value my sleep, so I'm not big on the idea of catching you up all the time. But I realize that you were really uncomfortable today. I can't have that."
    show AE embarrassed
    AE "..."
    HR "You're an amazing student, Matsumoto-san, but you need to look after yourself more."
    show AE neutral
    AE "...I understand, sir."
    HR "All right, well, have a good day then."
    hide HR with dissolve
    hide AE with dissolve
    "Shiori-chan bowed and walked out of the class. Once she got to the door, she instantly turned to where I was."
    MC "Hey, Shiori-chan."
    show AE neutral with dissolve
    AE "I'd like to apologize for that spectacle today, Hotsure-san."
    MC "No, no, I'm sorry! I bowed too low. I'm just glad you're alright."
    show AE angry
    AE "No, while I DO need to update you on the proper bowing form..."
    show AE sad
    AE "I mean my appearance today."
    MC "Your... huh?"
    AE "It's unbecoming of me to just walk about with ruined clothes."
    AE "I don't want my appearance to reflect poorly on you."
    MC "Shiori-chan, don't you remember what I told you? I don't care about my reputation. The way I see it, if you can't get new clothes that's no-one else's business."
    AE "But I'm causing a public disturbance by-"
    MCT "Not opening that can of worms."
    MC "Actually, that's something I wanted to ask."
    show AE neutral
    AE "Hm?"
    MC "Why can't you just get new clothes again? Most students seem like they can just get adjustments whenever. In fact, it seems like most of the girls do."
    show AE embarrassed
    AE "It's because... well..."
    "Shiori-chan seemed really uncomfortable. Her hands became fidgety as she spoke."
    show AE neutral
    AE "It's no business of mine... that is, I have full faith in the efficiency of the school to get students their clothes when necessary."
    MC "Do you not have the money to buy new ones?"
    show AE embarrassed
    AE "...No. Not at the moment."
    menu:
        "I can buy you some": #-1
            jump AE030_c1_1
        "I'm sure you'll find a way": #+1
            jump AE030_c1_2
        "That sucks, lol": #+0
            jump AE030_c1_3

label AE030_c1_1:
    MC "Well then let me give you some money to-"
    $setAffection("AE", -1)
    show AE neutral
    AE "Absolutely not. I don't take handouts. It would be improper of me as president."
    MCT "More improper than running around almost half-naked?"
    MC "Are you sure?"
    AE "Without a doubt. If I want more fitting clothes, I'd find work to get them. Until then, I'm content with waiting as the school's uniform office intends."
    MC "Hmm."
    MCT "There's no getting through to her. I can tell this is something she's ironclad about."
    MC "Okay, if you're sure."
    AE "Good. I'm glad you see things my way."
    jump AE030_c1_after

label AE030_c1_2:
    MC "I'm sorry to hear that..."
    MC "I'm sure that you can find a way to get a nice pair yourself though. I have full faith in you that you can work at it, and hopefully make the school's uniform policy better for everyone."
    show AE neutral
    AE "Yes... yes that's exactly right!"
    show AE happy
    $setAffection("AE", 1)
    AE "I knew you'd understand, Hotsure-san. You usually do."
    AE "If even a single student has to go without fitting clothes, then why is it appropriate for me to have when others here don't?"
    AE "No, that won't do. I'll simply work my hardest to ensure that every student always has clothes that fit!"
    AE "I understand that I'm a representative for the school, but if the fact I keep outgrowing my clothes is evidence that there is a problem with the current uniform policy, then by god I can make a difference!"
    show AE embarrassed
    AE "Ah..*ahem*, I'm sorry, Hotsure-san... I got carried away."
    MCT "You can say that again."
    MC "I have complete faith that you can work to change the school's policy on uniforms."
    jump AE030_c1_after

label AE030_c1_3:
    MC "Yeesh, y'know, that really sucks. It does."
    MCT "A kinder man would offer money but..."
    MCT "Only a dumbass would pass on a chance to catch a glimpse of that fat ass every few weeks!"
    MCT "...I think I have a problem."
    MC "I mean, it is what it is."
    show AE neutral
    AE "You're indeed right... crude, but right."
    AE "I'll simply work hard to ensure that I have the proper clothing."
    MC "I know you can do it!"
    MCT "Meanwhile, I want to see if I can make you even bigger..."
    MCT "I know I have a problem."
    jump AE030_c1_after

label AE030_c1_after:
    MC "Until then, want to go get lunch?"
    show AE embarrassed
    AE "Oh..."
    AE "I hope you don't mind, but I was thinking I'd sit in class and wait until it begins again."
    MC "Oh... then, can I join you?"
    "Shiori-chan tilted her head, looking at me through the thick lenses of her glasses with a look of pity."
    show AE sad
    AE "Are you sure? I'm sure you have friends who might want to talk to you. I don't want to be a burden."
    MC "You aren't a burden. I just like sitting and talking with you."
    "She smiled at that, and blushed a bit as she held her arm with her left hand."
    show AE embarrassed
    AE "T-thank you, Hotsure-san... that means a lot."
    scene black with fade
    "We went back into the room and discussed our lives as students came in once more for class. Afterwards, I walked her back to her room, though I walked behind her to keep some of her backside out of sight... and to catch a glimpse at her engorged back-end."
    jump daymenu

label AE031:
    $setProgress("AE", "AE032")
    scene Hallway with fade
    "Once class ended, I spent some time with Shiori-chan. We talked for a while, and generally had a good time. However, after an hour or two, we parted ways and, with little to do, I decided to explore a bit."
    "I stood up straight and popped my back. My exploration had led me do a fairly empty part of the school, and in front of the music room."
    MCT "If a seasoned soccer player loses his breath just walking around the first floor, how the hell is anyone else supposed to-?!"
    #WALTZ OP 64 NO 2
    MC "Hm?"
    MCT "Is there... someone in the music room?"
    "I listened from beyond the door as beautiful melodic tones hit my ears."
    "After standing outside and listening for a few minutes, I opened the door and entered the room."
    scene Music Classroom with fade
    "Entering the spacious room, I was hit by the strong acoustics. The piano at the centers notes echoing through the room in a cascade of sound."
    "I walked towards the piano, my footsteps going unheard as I approached."
    "And there, on the bench..."
    MC "Shiori-chan?"
    show AE neutral with dissolve
    pause 1
    show AE embarrassed
    #pause music
    #Piano Clang SFX
    "Shiori-chan jumped, and turned her head; eyes wide with shock."
    show AE surprised
    AE "H-Hotsure-san!"
    MC "Woah!"
    AE "Oh! Hoah... *Khm*, ah... y-you startled me."
    show AE neutral
    MC "S-sorry. I didn't... I, uh..."
    "I looked around the room before looking to Shiori-chan. Her gargantuan rear took up a large amount of the bench as her skirt, tucked under her butt, packed her ass in tightly. Noticing this, she pulled her skirt out to loosen it."
    MC "Do you, um..."
    MC "I-I had no idea you played piano."
    show AE embarrassed
    AE "Well, I..."
    "Shiori-chan fidgeted about a bit and avoided eye contact. For some reason, she was seemingly bashful about this revelation."
    show AE neutral
    AE "I dabble."
    AE "I've never done any SERIOUS work, mind you. I just... it's a way to relieve stress, is all."
    "I pointed to the book she was reading from, which seemed to be a handmade compilation of songs; a massive behemoth of paper and ink."
    MC "Where did you get that?"
    show AE embarrassed
    AE "I, um... I made it."
    MCT "W-WHAT?!"
    MC "You made those songs?!"
    show AE surprised
    AE "N-no! No, no, no, heavens no. These are all just piano arrangements or sheet notes for different songs from different musicians."
    MC "Th-That thing is huge! How long did it take to compile all of that?"
    show AE neutral
    AE "I'd say... since the beginning of high school. It's not that important of a book, it just has songs I like, is all."
    "I picked it up, and began to flip through the pages."
    MC "Shiori-chan, this is amazing! W-when were you going to show me this?!"
    AE "Actually, if I'm to be honest, I'd planned to show you after class."
    MC "Huh? Really?"
    AE "Mhm."
    MC "When?"
    show AE embarrassed
    AE "The day that, well, our relationship was made public."
    AE "Seeing the situation was hectic, I suppose I simply decided to put it off. However after some thought... I decided against showing you altogether."
    MC "Why altogether?"
    AE "Well..."
    show AE sad
    AE "Out of the belief you wouldn't care."
    MC "Whaaat?"
    MC "Shiori-chan, this is a big thing!"
    show AE neutral
    AE "How so?"
    MC "I-I mean, I've never... that's kind of a big deal! You're an amazing piano player!"
    show AE angry
    AE "Please. I've only five or so years of experience."
    MC "Which makes it that much more amazing!"
    show AE sad
    "Shiori-chan looked away from me once more, and back to her book. She pursed her lips and then looked up to me with soft and honest eyes."
    AE "You truly believe that?"
    MC "Without a doubt!"
    "I pulled up a chair. It's loud screech across the tile, along with a glare from Shiori-chan, reminded me to pick it up off the ground."
    MC "Here, play!"
    show AE surprised
    AE "O-oh?"
    MC "Yeah! Keep playing."
    "She looked to the song on her notes and placed her hands on the keys where she left off."
    show AE neutral
    AE "Very well then..."
    MC "..."
    show AE embarrassed
    AE "..."
    MC "Something wrong?"
    AE "No, no, I just wasn't expecting... company, is all. I haven't played for anyone in... a long time."
    MCT "Ah... I see. I'm distracting."
    MC "Oh, do you want me to-"
    show AE surprised
    AE "No, please, stay. This is nice..."
    show AE happy
    AE "Relaxing, even."
    "She flipped through her book a bit and looked back at me."
    AE "Just going to... find a new song, is all."
    "Placing her hands on the pristine white keys, she straightened her posture."
    "She took a deep breath and closed her eyes. After opening them, she began."
    #PLAY DIE FORELLE
    if getSkill("Art") < 4:
        "She played a song unfamiliar to me, and yet so relaxing. I leaned back in my chair and just watched her play."
    else:
        MC "Ah! Schubert."
        AE "You're familiar?"
        $setAffection("AE", 3)
        MC "Yeah, I learned about him recently, fantastic composer."
        show AE aroused
        AE "Yes... yes he is."
    scene black with fade
    "The song went on for a little while longer, all while I watched her gently and gracefully tapping away."
    scene Music Classroom with fade
    #SONG END
    show AE happy with dissolve
    AE "...Well, there. How was it?"
    MC "That was... amazing."
    AE "O-oh?"
    "Her face began to blush lightly as she gleefully took my compliment, brushing her hair off to the side."
    MC "How many songs can you play?"
    show AE surprised
    AE "Hm?"
    MC "You know, like, just by ear."
    show AE neutral
    AE "Oh. Hmm... give me a song."
    MC "How about 'Kusatsu-bushi'?"
    show AE happy
    AE "Ah. A traditional one, very well."
    #PLAY KUSATSU BUSHI
    scene black with fade
    "..."
    scene Music Classroom with fade
    #SONG END
    show AE neutral with dissolve
    AE "How was that?"
    MC "Amazing! You didn't even look at your notes."
    show AE happy
    AE "Mm, well, like I said, I can play by ear as well."
    #START PLAYING MO LI HUA
    MC "Hmm..."
    MC "Hey, where did you learn to play anyway?"
    "Shiori-san smiled and perked up a bit, still melodiously tapping away."
    show AE neutral
    AE "Ah, well, that would be Mr. Schultz."
    MC "Schultz?"
    AE "Mhm. Hans Schultz. Music teacher at my old high school."
    MC "Sounds foreign."
    AE "German, in fact. A former organist and administrator of a diocese in southern Munich. He was a true connoisseur of music; cultured beyond any man or woman I'd ever met."
    show AE happy
    if getSkill("Arts") > 5:
        AE "You remind me a bit of him, actually."
        MC "Really?"
        AE "Mhm..."
    AE "He was like a father to me."
    MC "Really?"
    AE "Mm."
    MC "What about your old man? Was he okay with you hanging out with foreigners?"
    show AE neutral
    AE "..."
    AE "He didn't care much."
    MC "Ah."
    MC "Yeah, yeah, I got ya."
    scene black with fade
    "..."
    scene Music Classroom with fade
    #SONG STOP
    show AE happy with dissolve
    AE "...Well, that was nice."
    MC "Yeah."
    "Standing up, her legs pushing back the bench, she closed the lid on the piano and stepped to the side."
    MC "Did you play a lot? Before coming here?"
    show AE neutral
    AE "Whenever I could. I never got the chance to outside of school after junior year."
    MC "Oh? What happened junior year?"
    AE "..."
    "Shiori-chan's hand rested on her book. She looked at it solemnly for a moment before grabbing it and putting it in her bag."
    show AE angry
    AE "Unforeseen complications."
    MC "W-"
    show AE neutral
    AE "Walk with me to my dorm? It's a bit late, and it's always nice to have you as company while I walk."
    MC "Oh, really? Thanks."
    "I stood up from my chair and moved it back to its original position."
    MC "Sure, I'll walk you there."
    show AE happy
    AE "After you."
    "We walked up the tiled stairs built into the floor. As we did, our footsteps echoed out of the room together, and after shutting off the lights Shiori-chan and I discussed her background in music  as we walked back to her dorm."
    jump daymenu

label AE032:
    $setProgress("AE", "AE033")
    scene Campus Center with fade
    "I sat on the bench under the shade of a dogwood tree, watching the blue, cloud-laden sky as I awaited Shiori-chan."
    "I tossed a peach up and down as I waited; blowing stray locks of hair up before they fell back down onto my face. I sat forward and looked around. Even though we only agreed on meeting here after class, it was never specified when."
    MCT "I hope she's oka-"
    "As I thought to myself, out from the door came Shiori-chan. I sat up with a smile, before it faded when seeing she was followed closely by another girl."
    play music Tension
    show AE angry with dissolve
    AE "And if I had my way we wouldn't be in this predicament in the first place, yet here we are."
    CMF "I'm sorry ma'am, if I knew, I would have backed you!"
    MCT "Huh? What's going on?"
    AE "Unfortunately it's a bit late for that. He's made far too many concessions as is and it's made costs to the fund that were ultimately unnecessary."
    CMF "I-I understand ma'am. Can we schedule him for five o'clock?"
    show AE neutral-annoyed
    AE "No. I'm meeting with the disciplinary committee head then to discuss the new policy. He reports directly to me as of yesterday."
    CMF "Then what time-?"
    AE "Six thirty. Exactly. He'll do so after I file the report for the art club."
    CMF "Okay, got it."
    AE "Good. I'll regroup with the other members in about ten minutes."
    CMF "Yes, ma'am!"
    "The girl walked off in the other direction, leaving Shiori-chan and I alone."
    "I looked up towards her. Her eyes were weary, with dark circles forming under them. She sat down next to me; her butt pillowing out over onto my leg slightly, forcing me to scoot away to net her more room."
    play music Hallway
    AE "Ngf..."
    MC "Long day?"
    AE "Longer still, considering I'd stayed up most of the night working on filling out the forms for the new legislation brought up by Amigawa-san, to actually do something about the surplus food."
    MC "Oof. Sounds rough."
    AE "That's not even the end of it. I still have meetings with three separate club members in a few hours, as well as organizing the outgoing forms."
    MC "Well, maybe cut back a bit on the work you have to do, then. You can miss a meeting or two, and if you turn in a few forms late, it's just a few out of, what, thousands?"
    MC "I'm sure it will be fine."
    show AE angry
    AE "It most certainly will *not* be fine. When I begin to jeopardize my work ethic, I begin to jeopardize my very being."
    "I looked at her as she trailed off in her thoughts, and placed a hand on her shoulder."
    MC "Shiori-chan, you have to realize that this isn't healthy. You're doing way too much for one person."
    show AE neutral-annoyed
    AE "If I don't do it, it won't be done."
    MC "That's what the other members are for, right? They joined the club, you'd figure they'd want to work hard as well?"
    show AE neutral
    AE "It's dangerous to assume that someone will do their share at all, let alone do it correctly. It's downright foolish to assume someone would WANT to do their share."
    MC "You don't really seem to have faith in your classmates..."
    show AE glasses
    "She pushed up her glasses, and spoke plainly as the light bounced from one side of her frames to the other."
    AE "I don't mean it to come off that way at all. I have complete faith in my classmates. I just want to be realistic. If I don't check and make sure everything is held up to the proper standards, then who will?"
    MC "By proper standards do you mean... well, your standards?"
    AE "Of course."
    show AE neutral
    AE "Besides, if the school expects things to be done the way they want it, then I have to abide by it, as per my position."
    MC "Well, what do you think the school wants?"
    "She sat with her hands at her lap in contemplation, then opened her mouth and spoke with absolute sincerity in her voice."
    AE "Nothing less than absolute perfection."
    MC "Oh, tch, come on, now."
    show AE neutral-annoyed
    AE "I'm serious."
    MC "You and I both know that's not possible, though."
    AE "Who are you to decide that?"
    AE "If we never *try* for perfection, we cannot strive to be the best we can be. 'Good enough' is the most surefire way to ensure future failure."
    AE "If the ceiling you set for yourself is infinite, you will never be stopped by it."
    MC "Shiori-chan, you shouldn't hold yourself up to such a high standard. It's not healthy."
    show AE neutral
    AE "That's my job, Hotsure-san. As Student Council President, I'm expected to hold myself to a high standard. That way any high expectations of me are well-founded."
    MC "But the stress you can cause yourself-"
    show AE neutral-annoyed
    AE "A worthy sacrifice. High expectations are like fuel for the diligent. I crave it above any platitudes or comments of 'Good Enough'."
    MC "..."
    MCT "She seems dead set on her philosophy. I doubt there's much else I can say."
    "Shiori-chan sat up, grunting as she lifted her body up with the side of the bench. I sat up with speed and put my hand out to help her. She shook her head and dismissively waved her hand to signify she could handle it."
    "As she stood up straight, her ass stuck straight out, and from a side view appeared as a big bubble wiggling gently with her motions. She signaled for me to follow her."
    show AE neutral
    AE "Come, come."
    "I obliged, and followed her closely behind as we walked through the courtyard slowly."
    MC "It's a beautiful day out."
    show AE happy
    AE "Hm, yes it is."
    MC "Good enough to go to the rooftop?"
    show AE neutral
    AE "Ah, as much as I'd love to do so, I'm actually short on time."
    MC "Oh..."
    show AE sad
    AE "I-I hear you sound disappointed... however, if there's anything you want to do later, I can certainly find time."
    MC "It's cool. You've got a lot to do. I'll think of something for later."
    show AE neutral
    AE "Yes, um... cool. Good."
    MC "Eheh."
    AE "Hm?"
    MC "It's cute when you try to speak informally."
    show AE surprised
    AE "Oh?"
    show AE sad-2
    AE "I mean... I'd assumed I had been."
    MC "Not by most standards, no."
    AE "I see."
    AE "..."
    AE "Is that an issue?"
    MC "No, no, it's fine. Totally fine."
    "Shiori-chan looked down to the ground for a moment before looking to me."
    show AE neutral
    AE "I'm not so sure it is."
    MC "Hm?"
    MC "What do you mean?"
    AE "Well, you'd agree that I'm not the most comfortable girl to be around, yes?"
    MC "Uhh..."
    menu:
        "You are.": #-1
            jump AE032_c1_1
        "You aren't.": #0
            MC "That's... true, unfortunately. You're not a very comfortable person."
            jump AE032_c1_after
        "You are to me. (disabled)" if getSkill("Arts") < 3:
            pass
        "You are to me." if getSkill("Art") >= 3: #+2
            jump AE032_c1_3

label AE032_c1_1:
    MC "I-I don't know what you mean! You're plenty comfortable to talk to."
    show AE neutral-annoyed
    AE "Hotsure-san, let's not talk falsely. I'd more appreciate that you look at things realistically."
    MC "I am! I..."
    $setAffection("AE", -1)
    AE "..."
    MC "S-sorry."
    jump AE032_c1_after

label AE032_c1_3:
    MC "Well, you're plenty comfortable to me. In fact, I'd say you put me at ease when you are around."
    show AE aroused-3
    AE "..."
    "Shiori-chan blushed a simple and quiet blush of appreciation."
    $setAffection("AE", 2)
    AE "O-oh. Well, thank you."
    show AE neutral
    AE "But the fact of the matter still remains. To most, I'm not very comfortable to be around."
    jump AE032_c1_after

label AE032_c1_after:
    show AE neutral
    AE "And that's fine. It does me well enough to be austere. However... some things could be resolved more easily if I were more readily capable of talking in ways that better facilitated emotional conveyance."
    "Shiori-chan opened the door from the courtyard to the hall and stepped in, me in tow."
    scene Hallway with fade
    show AE neutral with dissolve
    if getSkill("Academics") > 4:
        MC "And because you feel like you're not someone people can confide their feelings in, you feel like a less effective leader."
        AE "Exactly."
    else:
        MC "...Yoouu lost me at that last part."
        AE "How do... well, think of it this way:"
    AE "If a girl came up to you crying that she felt alone, I would bet you'd be far better equipped to deal with the situation than I, and yet as a representative for the school, I need to be able to help with any of the students' needs on a moment's notice."
    show AE sad-2
    AE "How do you handle problems like that with such ease?"
    MC "How do *I*?"
    show AE neutral-annoyed
    AE "Yes."
    MC "Hmm..."
    MC "Well... I like to think about my words carefully and visualize my possible responses."
    show AE neutral
    AE "Visualize...? I'm not sure what you mean."
    MC "Well, think of it like 'You've laid out separate possible choices and considered who you're talking to.' Then modify your choice based on who it is for the most effective response."
    AE "That's... hmm."
    MC "What?"
    AE "Is that common for you? To visualize your choices?"
    "I shrugged and looked around."
    MC "I guess, yeah."
    AE "I see... you're kind of like a social chameleon in that aspect then."
    MC "Chameleon?"
    AE "Mhm. You adapt well to your surroundings, at least."
    MCT "I'm not sure if that's a compliment or an insult."
    MC "Well, um... thank you?"
    show AE happy
    AE "Mhmhm, the vagueness of my statement WAS enough to get a cute reaction out of you. Your confused face is surprisingly cute."
    "Shiori-chan stepped closer to me and looked me in the eyes."
    show AE embarrassed
    AE "Although, most of your faces are."
    MC "O-Oh yeah?"
    AE "Maybe I'm not so bad at this after all?"
    "We walked further for a few moments before stopping at a door."
    MC "No you certainly are not..."
    AE "Hotsure-san..."
    MC "Hm?"
    show AE aroused
    AE "As a boyfriend... you exceed my standards."
    MC "..."
    MC "Ehe... thanks."
    MC "You know, I-"
    show AE neutral
    AE "Um, Hotsure-san?"
    MC "Hm? Yeah?"
    AE "I hope you don't mind but... I'm afraid we'll have to cut our conversation short today."
    MC "Why's that?"
    AE "No time. We'll talk later on."
    MC "Wait, why-?"
    AE "I'll talk to you later, after my meeting in five, four, three, two-"
    "With that, Shiori-chan turned around; her voluptuous rear nearly smacking me in the side as she opened the door wide and walked in."
    hide AE with dissolve
    AE "Everyone, let's skip the formalities and get directly to the matter at hand-"
    "A student near the door on the inside closed it shut before my raised hand could start to wave or my opened mouth could wish her good luck."
    MC "...Eheh... as expected."
    jump daymenu

label AE033:
    $setProgress("AE", "AE034")
    scene Library with fade
    play music Peaceful
    "I sat quietly, book in hand, at the table outside of the student organizations office. Shiori-chan had recently seen an uptick in work, and it seemed as though her meetings had been becoming even longer. I was worried, but right after class she'd told me to wait for her in the library."
    "Gazing up at the door, I exhaled and looked up at the clock. It'd been around an hour or so at this point. Just as I was becoming worried she'd not be out at all tonight, the door opened. One after another, students walked out and after they all left Shiori-chan exited and locked the door."
    MCT "There she is."
    MC "Hey, Shiori-chan!"
    show AE neutral with dissolve
    AE "Hm?"
    "After looking around a bit, I finally caught her eye and she walked over. I stood, brushing off my pants and bowing."
    AE "Ah, yes, sorry for keeping you so long. That was... more of an ordeal than it needed to be."
    MC "Ich, rough time with the... rules-stuff?"
    show AE neutral-annoyed
    AE "Rules-stuff? I don't- can you explain what you mean by...?"
    MC "Oh, um, I dunno. Whatever it is you talk about in those meetings."
    show AE neutral
    AE "Mm, I doubt you'd be that interested if I went into the semantics of it, so... yes, *khm* rules-stuff."
    MC "Well don't just assume I won't get it, I want to know too!"
    show AE neutral-annoyed
    AE "Hotsure-san, I never said you wouldn't get it, I said you wouldn't be interested."
    MC "..."
    MC "You know, I'm starting to think that you don't WANT me to know."
    show AE angry
    AE "Don't be ridiculous."
    MC "Tch, uwaah, Shiori-chan is so cruel! You're giving me these weird vibes and then shutting me down? So cruel..."
    show AE neutral-annoyed
    AE "D-don't go acting so foolishly. When I say you wouldn't be interested, that's all I mean."
    MCT "Hmm..."
    
    menu:
        "I trust you, don't you trust me?": #+1
            jump AE033_c1_1
        "It's my right to know.": #-1
            jump AE033_c1_2
        "I'll tickle it out of you.": #+0
            jump AE033_c1_3

label AE033_c1_1:
    MC "Shiori-chan, I know you well enough to know that you mean what you say. But you have to understand that I trust you with anything I bring to you because I know you'll respect what I confide in you. I want you to know that... you can feel the same way about me too."
    show AE sad
    AE "...You... really trust me that much?"
    MC "Of course! All I ask is that you show me that same respect."
    "Shiori-chan closed her eyes and sighed, signifying she agreed with me to some capacity."
    show AE neutral-annoyed
    $setAffection("AE", 1)
    AE "...Such an underhanded guilt trip. You must really be desperate to know... fine."
    MCT "YES! SUCCESS!"
    show AE embarrassed
    AE "...Even if that was a ploy, thank you for at least saying you trust me."
    jump AE033_c1_after

label AE033_c1_2:
    MC "Shiori-chan, as a student of this academy-"
    $setAffection("AE", -1)
    show AE angry
    AE "Don't. You. Dare."
    MC "I- Eh?"
    show AE neutral-annoyed
    AE "I know what you're going to say."
    MC "If you do, you know you already agree with me in some capacity."
    show AE neutral
    AE "...Fine. You're right. You do have a right to know what's happening with your Student Council."
    MC "Glad you understand."
    show AE neutral-annoyed
    AE "I need to stop falling for that."
    jump AE033_c1_after

label AE033_c1_3:
    $setFlag("AE033_c1_3")
    MC "...Tell me or I'll tickle it out of you."
    show AE neutral
    AE "You'll... what?"
    "I held my hands up and wiggled my fingers excitedly."
    MC "Kehehehehe~ Hey, Shiori-chan, how about it? How strong is your resolve to not tell me?"
    show AE neutral-annoyed
    AE "H-how dare you even-! We're in the library!"
    MC "And it'd be such a shame if it was filled with the squeals and giggles of our Student Council President, riiight?~"
    AE "You-!"
    AE "Ngf-Fine. I can tell by your lewd eyes you mean business."
    jump AE033_c1_after

label AE033_c1_after:
    show AE neutral
    AE "Let's not discuss it here though. Come. Walk with me to the dorms."
    if getFlag("AE033_c1_3") and getSkill("Academics") > 3:
        MC "O-ho-hoo, no. If I let you leave I lose some leverage. I see the game you're playing."
        show AE neutral-annoyed
        AE "Gch-now look here-"
        MC "Fine."
        show AE neutral
        AE "I mean to- Hm? Fine?"
        MC "Yep, because if we leave and you don't tell me I'll pinch your cheek and make you yelp."
        show AE embarrassed
        AE "Stop saying such absurd things!"
        MC "Oh it's not absurd at all. There's a LOT of cheek to pinch.~"
        show AE neutral
        AE "...Wait..."
        "Shiori-chan looked behind her at her massive swollen 'cheeks' and put her hands on her hips. She looked back to me with a gaze that could murder a demon."
        show AE angry
        MCT "TOO FAR, TOO FAR."
        MC "Y-you have such a cute rosy face after all!"
        AE "...Are you saying my face looks fat?"
        MCT "KILL ME."
        MC "HAHA, LET'S GET GOING TO THE DORMS NOW."
        show AE neutral-annoyed
        AE "..."
        show AE happy
        AE "Too easy."
        MC "Huh?"
        show AE neutral
        AE "No shouting in the library. Let's head to the dorms... you deserve to hear at least a bit after that spot of teasing."
        MCT "T-teasing?"
    else:
        MC "Oh. Okay then... why the dorms?"
        AE "I want to put some things in my desk before I monitor the halls for a bit. It will only take a minute."
        MC "Sounds good."
    "I began to walk away from the table, but something caught Shiori-chan's eye."
    AE "Ahp- The book."
    MC "Hm?"
    AE "Please put the book back where you found it."
    MC "Where I..."
    MC "Are you sure the librarian won't just put it back at the end of the day? No harm, no-"
    show AE neutral-annoyed
    AE "No. Put it back, please. It'd be the least you could do."
    MC "...All right."
    "I put the book back, and when I turned around Shiori-chan was waiting by the door for me. We walked out together, talking along as we went."
    scene Hallway with fade
    show AE neutral with dissolve
    MC "Sooo, wanna fill me in?"
    AE "Well... please don't say a word to anyone about this, though I assume it's already public knowledge to some degree."
    MC "Not a word."
    AE "...One of the members broke down crying after being insulted about their nose. It was a fairly embarrassing situation."
    MC "Oh."
    MCT "That's... it?!"
    MC "Is that all?"
    AE "That was the most pressing issue, yes."
    MC "How was it an issue? Did you, I dunno, discipline the student who did it?"
    AE "Oh indeed. But that was only one part of the discussion."
    MC "What about the guy they insulted?"
    AE "I let him know her reaction wasn't befitting of a member of student council."
    MC "That's... kind of messed up."
    AE "Hm?"
    MC "I mean, that's kind of messed up don't you think? It's not his fault, he just felt hurt."
    AE "Indeed, and I empathized with his pain. The fact of the matter, however, is that you can't let the other students SEE you get too emotional."
    show AE neutral-annoyed
    AE "We're representatives. We're meant to seem logical and upright at all times, not being slaves to petty feelings."
    MC "I've seen you get angry before, many times."
    show AE neutral
    AE "Well, we have a more intimate relationship than I do with anyone else."
    MC "Right, but even BEFORE we were a couple, I've seen you raise your voice and-"
    show AE neutral-annoyed
    AE "Trust me, Hotsure-san, while I may need to seem angry at times in order to motivate and correct, I'm in control of myself at all times."
    MC "...Hmn..."
    MCT "I mean... she has a point. Every time she's shown a fairly strong emotion it's always been to sway things in her direction. She never seems to 'lose it'..."
    show AE neutral
    AE "I mean no disrespect, of course. You, on the other hand, seem to be fairly easy to read based on how you act."
    MC "How I... act?"
    AE "Indeed. For example, your neck. You rub it when bashful, yes?"
    MC "Wuh-I..."
    AE "Furthermore, it's rare, but I've seen you stroke your hair from time to time. I assume that means you're deeper in thought."
    MC "I-"
    AE "When you put your cupped hands on your stomach, you feel content, and when you purse your lips you feel mild confusion."
    MC "I-I do not!"
    MCT "She's right on all accounts!"
    AE "There's no shame in it, though. As a spry and active young adult it would make sense for you to telegraph your more obvious feelings."
    MC "I see... and as student council president, I suppose you'd naturally want to seem the most emotionally stable."
    AE "I've often been told that I'm hard to read."
    "We walked silently for a bit longer, our conversation cutting off a bit awkwardly. When I spoke up, I'd given good thought into what I wanted to say."
    MC "Actually, I think it's just the opposite."
    AE "Hm?"
    MC "From an outsider's point of view, yeah, but I feel I've gotten to know you well enough to point out how you feel based on your small movements."
    AE "How so?"
    MC "Well, let's start with an easy one."
    MC "I've noticed that when you're feeling proud you cross your arms."
    AE "...Oh?"
    MC "You brush your hair to the side when YOU feel bashful."
    AE "Hm... a minor one, but intentional."
    MCT "Intentional? Is that true or is she trying to brush it off?"
    MC "You... for some reason you bite your thumbnail when you are worried."
    show AE glasses
    AE "..."
    MC "When you're REALLY mad I think I've seen you bite your knu-"
    AE "Anything more?"
    MC "Hm?"
    AE "Any other tells I should keep in mind?"
    "Shiori-chan pushed up her glasses as the light from the windows bounced across the frames."
    MC "...As a matter of fact, yes."
    MC "When you... you, uh... I don't know what it is you feel, but for some reason you like to push up your glasses at specific moments."
    show AE neutral
    AE "...Oh?"
    MC "No offense, but it's so weird."
    MC "Why not just buy new glasses if they slip off easily?"
    AE "...These glasses are prescription, it's not as easy to simply go out and buy a new pair."
    MC "Then why not get them refitted?"
    AE "..."
    AE "I-..."
    AE "I feel as though there's no point. They haven't broken yet, and I don't mind adjusting them from time to time."
    "Shiori-chan took off her glasses from her face and looked at the lenses. Squinting, she manipulated the spectacles about her fingers before placing them back on."
    AE "If that's all, there's not much to say. I have tells, yes, but I'm quite mindful of all my actions. If I do something, I do it with purpose."
    MCT "...I feel like she doesn't WANT to be easy to read... on a deeper level than she's letting on."
    MC "Shiori-chan?"
    AE "Yes?"
    MC "I feel as though you don't want to express yourself."
    AE "I believe we've come full circle. Yes, Hotsure-san, as I said-"
    MC "No, I mean that you don't want to let your feelings known because you don't want to... um..."
    show AE neutral-annoyed
    AE "...Yes?"
    MCT "That's... way too much to bring into this today. I don't even know myself if I believe she wants to stunt her feelings."
    MC "N-nevermind, I'm just being weird."
    MC "Eheh."
    "I semi-consciously rubbed the back of my neck. Shiori-chan, however, seemed to pick up on the difference."
    AE "I see... then we'll leave it at that, if you want."
    AE "Until then, my room is fairly close by."
    MC "Ah... so it is."
    AE "Mhm. If you need, I'll be here."
    MC "Okay, then... I guess... see you later?"
    AE "Yes. See you later."
    "I turned around as she began to close the door, only before opening it and sticking her head out."
    show AE embarrassed
    AE "U-um, Hotsure-san?"
    MC "Hm?"
    show AE neutral
    AE "..."
    "Shiori-chan brushed her hair back behind her shoulder."
    show AE embarrassed
    AE "Even if it's on strange topics like today... I thoroughly enjoy spending time with you."
    MC "...Eheh... same."
    AE "..."
    AE "Would you like to spend some more time with me in the halls today? I'm sure by doing so we can... *khm* perhaps talk about some softer subjects."
    MCT "Haah, there we go."
    MC "Of course! "
    "I waited as Shiori-chan put her things in her room. Once she did, we walked the halls together. I've still yet to figure out what it means when her bell-like hips sway when we walk together, but I can tell that it must be good, since she only does it when we delight in each other's company."
    jump daymenu

label AE034:
    $setProgress("AE", "AE035")
    scene Dorm Interior with fade
    play music Schoolday
    "I bounced a rubber ball from the wall back to my hand as I lazed about. My homework was all done, and I didn't have much else to do. I went to talk to Shiori-chan after class, but she walked away talking to another student before I could catch up."
    "'Keep an eye on her. I have a feeling I know what's going on.'"
    "It was ominous, but I figured that I'd best keep my nose out of it. However as I put the ball in my pocket, a knock came to the door and when I went to open it..."
    show AE neutral with dissolve
    MC "Oh! Shiori-chan, hey. I haven't seen you all day, what's been going on?"
    "Shiori-chan bowed, and placed a hand on her hip as she spoke in a plain and dry tone. I could tell she wasn't here to say hi and ask to spend time together."
    AE "It's good to see you, Hotsure-san. I'm investigati-"
    MC "Daichi literally left out the window a couple of minutes ago."
    show AE angry
    AE "Gch! Tell him to stop doing that!"
    show AE neutral
    AE "...But that has nothing to do with what I was going to say."
    MC "O-oh?"
    AE "Mhm. Please, come with me."
    MC "O...kay?"
    scene Hallway with fade
    show AE neutral with dissolve
    "We walked through the halls together, and I glanced at her every once in a while, trying to figure out what was going on."
    MC "So, Shiori-chan, wha-"
    stop music
    UNKNOWN "*Huff* *Puff* *Haah*"
    MCT "Huh?"
    play music Busy
    "Around the corner, we heard huffing and puffing from a girl, along with the pater of shoes hitting the flooring."
    AE "Hm?"
    hide AE with dissolve
    show Ryoko neutral with dissolve
    if isEventCleared("GTS011") or isEventCleared("GTS011b"):
        "Ryoko-san rounded the corner, running at Mach speed with a determined look in her eyes."
    else:
        "A girl rounded the corner, running at Mach speed with a determined look in her eyes."
    Ryoko "I'm gonna be late-I'm gonna be late-I'm-"
    hide Ryoko with dissolve
    show AE neutral-annoyed with dissolve
    AE "You there! No running in the halls!"
    "Upon noticing Shiori-chan, she picked up speed and covered her face with her hand."
    hide AE with dissolve
    show Ryoko neutral with dissolve
    Ryoko "Oh crap! Gonnabelategonna-"
    "Then, in that moment, she tripped herself up on the edge of her shoe."
    hide Ryoko with dissolve #animate?
    Ryoko "Eek!"
    "She hit the ground with a loud thud, her books flying a few feet in front of her; papers everywhere."
    show AE angry with dissolve
    AE "I said no run-!"
    "Shiori-chan stopped herself, and put her hands up to her mouth to gasp."
    show AE surprised
    AE "Oh dear lord."
    "Shiori-chan jogged over to where she was, with me following closely by."
    show Ryoko neutral at Position (xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    show AE sad at Position (xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    AE "Are you alright? "
    Ryoko "Egch. I think I bit my tongue."
    "She opened her mouth, and from it flopped out a lengthy pink tongue; a small spot of red on the very end."
    AE "I can see. I'd suggest getting it checked with the nurse."
    Ryoko "N-no, no, I'll be alright."
    AE "Are you sure?"
    Ryoko "Y-yeah, I think. Ach, my books!"
    "She scrambled to her knees to pick up her misplaced papers."
    AE "Let me help."
    "In turn, Shiori-chan carefully went to her knees and grabbed some; her rump resting heavily on the backs of her heels as she did so. I joined in, and within seconds the papers were all neatly stacked once again."
    show AE neutral
    AE "Ah. One moment. Your face."
    "She pulled out her handkerchief, and went to dab her face before pulling back."
    AE "Do you mind?"
    Ryoko "Um, n-no. Go ahead."
    "She began wiping the side of her face with the cloth, and after checking for now cuts or bruises, put her handkerchief back in her shirt."
    AE "There. Now, slow down and talk with me."
    "Rather than doing so, she sprang up with great swiftness."
    Ryoko "I'm gonna be la-"
    AE "I understand that. We can walk and talk. No need to run."
    "Shiori-chan supported her weight on an adjacent wall and lifted herself up off the ground. As she got up they briskly walked side by side down the hall."
    AE "Where are you headed?"
    Ryoko "U-um, the library. I need to meet with the club!"
    AE "Okay, you're going the wrong way. You see the dogwood, over there?"
    Ryoko "Mhm."
    AE "Go to the door left of that and take a right. Go down the hall. And DON'T run."
    Ryoko "It's the first day I'm in the club, I don't want to-"
    AE "If you're late, I can talk to the club organizer about your accident. Ryoko Tanaka, right?"
    Ryoko "Y-yeah. How did you-?"
    AE "This school isn't so large that I can't remember it's students. You're one of only a few with a tongue growth."
    AE "Now get going."
    "Ryoko-san bowed and then hurried off in the other direction."
    Ryoko "T-thank you!"
    hide Ryoko with dissolve
    show AE neutral-annoyed
    stop music
    AE "And don-! Ach-Oh, nevermind."
    "Shiori-chan turned around and sighed before adjusting her slipping glasses."
    show AE neutral at Position(xpos=0.5, xanchor=0.5, yalign=1.0) with dissolve
    AE "Now that that's out of the way, come."
    "We continued, however I finally had the opportunity to speak up."
    MC "So where are you going?"
    AE "I need to talk with a student. I figured you'd be helpful."
    MC "How so?"
    AE "I figured you'd be able to get through to her more easily."
    MC "Her? I don't know...?"
    play music Rain
    AE "Your sister."
    MC "Eh?! What's she done? What's going on? Is she okay?!"
    AE "Relax, Hotsure-san. It's going to be fine. I just need you to talk to her."
    MC "Dch-well can you tell me what about?"
    AE "I have reason to believe... she may be privy to private information on students."
    MC "Private...?"
    MCT "She knows I've been getting advice from her."
    "Tomoko, my sister, has always been there to give me advice when I wanted to know how things were. Always open to give me advice. I always wondered how she was so knowledgeable, even while just using video game facts."
    AE "Please. Follow me."

    scene Dorm Exterior with fade
    show AE neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    "We reached her room, and I walked up to knock on the door."
    play sound Knock
    MC "Tomoko, it's me, Keisuke. Can we talk?"
    Tomoko "Mmhn... can we talk later? I'm almost at the second boss."
    MC "T-Tomoko, please open up."
    Tomoko "Auuuu~"
    "I heard the sound of footsteps and then the click of the door unlocking as she opened the door a crack."
    show Tomoko neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    Tomoko "Hm? Big bro?"
    "Tomoko's hair reached down to her calves at this point, her silken ebony locks swaying with even the gentlest touch of the wind. Her bangs covered but one eye."
    MCT "Her depth perception must be terrible. I can't understand how anyone sees so easily with their hair in the way..."
    MC "Hi, Tomoko. Me and my... friend wanted to talk."
    AE "May we come in, please?"
    Tomoko "...Okay."
    
    scene Dorm Tomoko with fade
    "She opened the door fully, and squinted as the light shone down into her room. This was hardly surprising, as a black blanket covered the window. The lights in her room were off, barring the bright intense light of the shmup's pause screen on her television."
    "As we entered the room, she crawled up onto her bed, took her comforter and covered herself in it leaving only her hands, face, and long flowing bangs exposed. Shiori-chan and I stood, as I began."
    show AE neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show Tomoko neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    MC "Tomoko, do you know who this is?"
    Tomoko "...Not really. Sorry."
    show AE neutral
    AE "No offense taken."
    MC "T-this is Matsumoto Shiori. She's the school's Student Council President-"
    Tomoko "Your girlfriend?"
    "I looked to Shiori-chan, who did nothing but nod to her."
    show AE neutral
    AE "Yes. I'm very close to your brother."
    "Stepping forward, Shiori-chan gently sat on the bed after asking Tomoko if it was okay."
    show AE happy
    AE "You were quick to point out my status as his girlfriend. Has he told you?"
    "Tomoko shrugged, and looked up to me."
    Tomoko "I mean... I know a lot of stuff that happens."
    show AE neutral
    AE "Indeed. However, I find it strange that you know as much as you do about the social happenings about the school when you often stay indoors outside of class."
    Tomoko "I'm in a club, you know."
    AE "Which one?"
    Tomoko "...U-um..."
    show AE happy
    AE "It's all right if you're in the 'Go Home' club, I'm not mad. There are many students who are."
    Tomoko "Oh..."
    AE "You don't need to worry, you're not in trouble for anything, however I've heard a rumor that concerns me."
    Tomoko "I-I didn't sell my panties to Kurosaki-san! That was a dumb rumor started by Izumi-chan!"
    MC "Wait, what?!"
    "Before I could say anything more, Shiori-chan put a hand up to stop me from going any further."
    show AE neutral-annoyed
    AE "No, it's nothing egregious, though I do intend to look into that rumor later."
    show AE neutral
    AE "I've been hearing that you've been getting private information about the other students."
    Tomoko "..."
    "Tomoko looked up at me in an accusatory manner. I tried to convey as best I could without words that I didn't tell her anything, and to not point out that I've been a benefactor of her knowledge."
    AE "And I just wanted to know if that's true."
    "Tomoko began to sink deeper into her comforter, and started to avoid eye contact."
    AE "Is everything all right? You don't need to feel uncomfortable around me."
    MCT "To be fair, it's kind of a natural impulse."
    Tomoko "I guess I'm just thinking about stuff."
    AE "About what?"
    Tomoko "You have a really big butt."
    MCT "GAK-T-TOMOKO!!!"
    show AE surprised
    AE "O-Oh."
    Tomoko "Did you get gum stuck on it too?"
    MC "Aha! Ahaha! Tomoko, how's about you-"
    show AE neutral
    AE "I'm not quite sure what you're trying to say..."
    Tomoko "Well, when Keisuke and I were really little we got in trouble because our hair got caught up together in a big wad of chewing gum."
    Tomoko "Now, our hair is growing. If you have a really big butt, then you must have sat on a really big wad of gum."
    "The room was silent. I looked at Tomoko the same way I always had when I found out she cleared my save files in games to fit her playthroughs. However, the silence was broken by a somewhat unexpected sound."
    show AE happy
    AE "Pfft... eheh..."
    MC "S-Shiori-chan?"
    AE "Yes, well, *khm* that's a bit of Post hoc ergo propter hoc, however I'd suppose If I had it would be quite the interesting cause."
    show AE neutral
    Tomoko "Eheh, it must have been the extra big bubble kind."
    AE "..."
    MCT "O-OY, BRAT, ARE YOU TRYING TO GET US BOTH KILLED?!"
    AE "B-Back to the issue at hand. Is it true you've been getting students personal information?"
    Tomoko "...Yes."
    show AE neutral-annoyed
    AE "I see, then she's the one who's been leaking information."
    MC "S-Shiori-chan, I doubt Tomoko meant to cause any harm. She's a good-"
    AE "I'm not talking about her."
    MC "E-eh?"
    "Almost instantaneously, Yuki-chan came bursting through the doors and began talking up a storm."
    hide AE
    hide Tomoko
    show Yuki neutral
    Yuki "OH MY GOD GIRL, YOU WILL NOT BELIEVE THIS!"
    show Yuki neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show AE neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    AE "..."
    Yuki "Did you know that Yureno-chan got in trouble for-... erm..."
    show AE neutral-smug
    AE "No, please continue, Utagashi-san. Do go on."
    "Yuki-chan began sweating as she licked her fat lips and smiled a nervous smile."
    Yuki "Shio-M-Ma'am!"
    show AE angry
    AE "Then I was right. A student council member releasing private information makes all too much sense. Natural it was you."
    Yuki "F-... Fo-..."
    "Yuki-chan got on her hands and knees and put her head to the ground."
    Yuki "FORGIVE ME MA'AM!"
    scene black with fade
    pause 1
    scene Dorm Tomoko with fade
    "After a strict talking by Shiori-chan, Yuki-chan was able to keep her seat on the student council, but was no longer allowed anywhere near student files."
    show AE neutral at Position(xpos=0.5, xanchor=0.5, yalign=1.0) with dissolve
    MC "Well, I guess that settles that."
    AE "Mm. Hopefully I won't be hearing any more personal information of students being shared."
    show AE neutral-annoyed
    AE "Isn't that right, Yuki-chan?"
    show Yuki neutral at Position(xpos=0.2, xanchor=0.5, yalign=1.0) with dissolve
    Yuki "Eep! Y-yes ma'am!"
    AE "Good. Then, I hope you both have a good day."
    MC "Oh, real quick, before I go."
    AE "Hm?"
    MC "Hey, Yuki-chan? What's Kurosaki-san's room number?"
    show AE angry
    AE "Hotsure-san, out, now."
    MC "Ghgn!"
    show Tomoko neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    Tomoko "Eek!"
    "At the same time, Tomoko and I sprung up and ran out of the room to Shiori-chan. She looked at the two of us, before clearing her throat and bowing to Tomoko."
    AE "N-not you."
    Tomoko "Oh. S-sorry."
    scene Dorm Exterior with fade
    show AE neutral with dissolve
    "The door closed behind Tomoko, and almost immediately I heard Yuki-chan begin chattering away about her day."
    MC "Phew. That's settled."
    AE "Indeed."
    MC "Got anything else you need?"
    AE "Need?"
    show AE embarrassed
    MC "Well, no, but... would you like to go to the library with me? I found an interesting book I think you might like."
    AE "Oh? In that case, sure!"
    "Shiori-chan and I walked over to the library and spent a good amount of time reading together; showing passages or lines we liked as we delighted in one another's company."
    jump daymenu

label AE035:
    $setProgress("AE", "AE036")
    scene Campus Center with fade
    play music Peaceful
    "The bells chimed, signifying that it was time for students to begin lunch. Shiori-chan was rushed out of the room by a student council member who burst in as soon as class ended, though I caught a glimpse of her, or rather her gigantic badonk, as I entered the courtyard."
    MC "Oy, Shiori-chan, got a sec?"
    show AE surprised with dissolve
    AE "Oh, Hotsure-san, it's good to see you. I'm sorry but I have a meeting after class and-"
    show AE sad
    MC "N-no, it's fine, I understand, I just wanted to see if you were free now."
    AE "You know I'd like to, but I need to get these forms submitted by... um..."
    "Shiori-chan looked at the overlapping plastic bags in my hands."
    show AE neutral
    AE "I hope you don't mind my asking, but... care to explain the bag?"
    MC "Yeah, uhh..."
    "Unwrapping the bags revealed a black box. I handed it to Shiori-chan with both hands and bowed."
    MC "Here, I made this for you."
    AE "Hm?"
    MC "It's a bento."
    show AE surprised
    AE "A..."
    MC "I figured that since, well, you're busy more often now, I could make you something you could sit down and eat whenever you have the time."
    "The small black box was unassuming, and was made from a smooth plastic. I'd brought it with me when I came here on my mother's request, but I never thought I would need it."
    "Opening the lid, I showed Shiori-chan the contents; slices of pink salmon, hotdog slices, rice, red bean paste, and cheese cubes. Everything that I could scavenge from the fridge that Daichi had been storing was here."
    AE "Hotsure-san, you made this for me?"
    AE "...I..."
    "Shiori-chan smiled a warm and loving smile, one which I'd been hoping to see for a while now."
    show AE happy
    AE "W-well, um, ahah... thank you."
    AE "Wow..."
    MC "A-anyways, I'm sure you have a lot to do before you head back to class, so I guess I'll just head out a-"
    show AE neutral
    AE "W-wait."
    MC "Hm?"
    "Shiori-chan looked over the contents carefully."
    AE "This was made in your dorm?"
    MC "Yeah, I made it myself."
    show AE neutral-annoyed
    AE "Absolutely unacceptable."
    MC "Eh?!"
    MC "Don't tell me there's a rule about making bentos in the dorms?!"
    AE "No, but think logically for a moment. You made this in your dorm with Utagashi-san unattended."
    MC "W-wait, what does Daichi-"
    show AE angry
    AE "He could have put laxatives or some sort of poison in this!"
    MC "No, I made sure he didn't-"
    AE "No excuses, Hotsure-san. I will not have you possibly poisoning me!"
    MC "I-"
    show AE neutral-smug
    AE "As punishment for your recklessness, you're going to have to sit here and eat with me to ensure my safety."
    MC "...Ah..."
    "Shiori-chan walked over to the shade of a tree and placed the box down before, with a grunt, planting her bubble butt down. She patted at the ground next to her."
    show AE happy
    AE "I'm sure you find that agreeable?"
    MC "Hoo, well, what can I say, you're the boss."
    MC "Ah, but, your forms-"
    AE "I can make time. Come. Sit."
    if getSkill("Academics") < 6:
        MC "Oh, but I don't have-"
        show AE neutral
        AE "Chopsticks, right."
        AE "No matter, I can go and get some from the cafeteria. Just a moment."
        hide AE with dissolve
        "As she sat up, her sizeable derriere wiggled gently. She walked off with a small skip, her skirt swishing from side to side as her bulbous behind began to slow its movements. I watched tantalized all the while, a tinge of pink overtaking my cheeks as I focused on hers."
        MC "Haahn..."
        MCT "Pfft, did Daichi poison the food. That was clever of her..."
        "I waited in the shade for a short moment before-"
        MCT "...DID Daichi do anything to it?!"
        "I looked around the box, however it seemed as though it had no signs of tampering. Growing suspicious of the box itself, I lifted it, yet not a single aberration was found. Still on guard, I placed it down as Shiori-chan came out of the door with the utensils in hand."
        show AE happy with dissolve
        AE "Here we are."
        MC "Thank you."
        MCT "I swear to god, if he did anything..."
    else:
        "I pulled out a pair of chopsticks out of my pocket as Shiori-chan sat down on the ground."
        show AE neutral
        AE "Oh, right, you need-"
        show AE surprised
        AE "..."
        AE "Chopsticks."
        MC "Hm?"
        show AE happy
        AE "..."
        AE "As expected of Hotsure Keisuke. How much of your plan worked out to the letter?"
        MC "I'm not quite sure what you mean?"
        show AE surprised
        AE "You expected to leave me here with the food, and yet you have spare chopsticks?"
        AE "You figured I'd be guilt tripped into eating with you?"
        AE "Dear lord, if it were anyone else, I'd be frustrated to be manipulated so easily, but frankly I'm impressed!"
        MC "...And yet I couldn't get it past you."
        MC "Heh, I swear, that would have worked against most in a heartbeat."
        show AE happy
        AE "Mhm. Well, come, sit down. Enjoy the fruits of your mental labor."
    MC "Let's dig in!"
    AE "Mm."
    "We pointed our sticks to the food, she moved hers around from piece to piece as I waited patiently for her."
    show AE neutral
    AE "So, can you tell me what these are?"
    MC "Eh?"
    AE "...The, um, brownish pink strip."
    MC "...Salmon?"
    show AE happy
    AE "Yes! Yes, that's it, I'll try this."
    MCT "She's never had salmon?"
    AE "Mmhm... it's really good."
    MC "Yeah! Ohp, here, try some with rice."
    show AE neutral
    AE "Oh, s-sure."
    show AE happy
    AE "Mmhm, it complements the taste well."
    MC "Yep!"
    show AE neutral
    AE "And what's that there, in the center?"
    MC "Oh, that, that's red bean paste."
    AE "Ah. And the yellow squares?"
    MC "Cheese cubes."
    show AE surprised
    AE "Oph, hm-mm, can't eat that. Lactose intolerant."
    MC "Really?"
    show AE embarrassed
    AE "Unfortunately so... Embarrassingly so, actually. Diary of any kind makes me... *khm* Well, nevermind. I simply don't eat dairy."
    MCT "I never knew that... and here I thought she might be a big ice-cream fan."
    MC "Well, I can eat those then."
    MC "That's a shame they go really well with-"
    show AE happy
    AE "Ah! Hotdog squids."
    MC "Hm?"
    "She pointed to the tiny hot dogs cut up into squid shapes."
    MC "Oh, you know those?"
    AE "Mhm. They were a childhood favorite."
    MC "Then help yourself!"
    AE "T-thank you."
    "As we dug in, we talked about our day as the birds chirped in the sky. I'd gotten through half of the cheese by the time Shiori-chan had finished the salmon, and minute by minute the contents of the tray slowly disappeared."
    "I stopped for a moment, and looked at her as the breeze gently blew her hair, as well as her skirt, exposing pale thigh flesh before she inevitably readjusted it. I chuckled to myself and looked out towards the campus."
    MC "So... about Tomoko."
    show AE neutral
    AE "Hm?"
    "She gulped and then responded, looking at me solemnly."
    show AE neutral-annoyed
    AE "As I said, Hotsure-san, she wasn't complicit in anything egregious-"
    MC "No, no, I just... I wanted to thank you for how you handled it."
    MC "She's a really shy girl, and yet she opened up to you readily."
    show AE surprised
    AE "O-oh..."
    "Readjusting her glasses, Shiori-chan cleared her throat and placed her hands on her vast lap."
    show AE neutral
    AE "Someone in my position needs to know how to handle all types of people. I did nothing more than what my office required of me."
    MC "Right, but you went the extra mile to seek me out so she'd be comfortable. That's the mark of someone who cares deeply for the well-being of others."
    AE "I merely took an action that ensured optimal results."
    AE "..."
    show AE embarrassed
    AE "But... thank you for your compliment."
    MC "No problem."
    MC "Did you ever get back to Ryoko-chan?"
    show AE neutral
    AE "Yes, actually. After reprimanding her further for running, she informed me that she was okay."
    MC "Oh, well that's go-"
    show AE neutral-annoyed
    AE "Then she said I would make a great actress for her project 'Attack of the Bubble Butt Space Vixens'."
    MC "...I'm guessing you took exception to that?"
    AE "I took exception to that."
    MC "Of course."
    show AE neutral
    AE "However, apparently, Yureno-san was far too happy to fill the role, apparently."
    MCT "Wait, it's a real thing planned?!"
    MCT "...Is it in 3D?"
    MC "You know... I'm really glad you're working so hard to look out for all of us."
    AE "Well, Hotsure-san, that's my obligation and desire."
    "She separated her hands and put one on each of her thick legs, both sinking in lightly."
    AE "I wish for nothing but to see everyone have the chance and tools to let them obtain their happiness."
    MC "..."
    AE "..."
    "*pat*"
    show AE surprised
    AE "Hm?"
    "With little hesitation, I reached over to her lap and put her hand in mine. Her cold palms warmed up once they felt the embrace of my own. She looked up at me, and I smiled, letting her know that I was here. That I was delighting in her touch."
    show AE happy
    AE "A-ah..."
    "She shrunk back a moment, before giving a tiny smile. It was now obvious to me that she was delighting my touch as well. She fiddled about, and I gently stroked her ring finger with my pointer. She wouldn't be outdone, however, and with her middle began to caress my palm."
    MC "Ehehe, that tickles a bit."
    AE "Mhmhm..."
    "Her face was pink as the salmon she'd eaten just moments before, with her free hand she brushed her hair to the side and looked to me with eyes that promised to hold this sensation close to her for as long as she could remember."
    "We stayed like that for a while, and only broke once the bell tower beckoned us back to class. As I stood up, however, I'd found that Shiori-chan hadn't let go. Propping herself up, she grabbed the box and put it under her arm, and we walked hand in hand back to the classroom."
    jump daymenu

label AE036:
    scene Hallway with fade
    $setProgress("AE", "AE037")
    #SCENE IN AFTERNOON
    play music Busy
    "As the day came and went, I had found time to talk with Shiori-chan when I could, and as usual, she was whisked away into a meeting after class. Thankfully, according to her, her schedule had been clearing up and soon we'd be able to spend more time together."
    "That didn't mean, however, I could wait patiently. I bent down behind a potted plant, waiting at the library door. Peeking every few seconds at the door, I'd been-"
    Student "Um, what are you doing?"
    MC "..."
    Student "..."
    "I crouched down further to hide myself from the girl who was staring intently at me. After a few seconds, she backed away and left me to continue. I'd been waiting here for a good amount of time for Shiori-chan to get out, and just as I felt that I was acting silly..."
    #Creeeak
    show AE neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    AE "Until then, I can't see that being an issue."
    MCT "THERE SHE IS."
    "I got out from behind the plant. I slowly snuck up behind Shiori-chan, whose massive rear end seemed to have grown even more since the last time we spoke."
    show Yuki neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    Yuki "Okay. I'll inform Ryoko-chan about the-"
    #show Yuki surprised
    Yuki "...Um. Ma'am?"
    show AE neutral-annoyed
    AE "Hm?"
    show AE surprised
    AE "W-woah!"
    "I rushed up and grabbed Shiori-chan's hand trying to pull her away. It was strange, but since we held hands I felt as though she was more open to hold on to, and in turn I felt more tactile."
    MC "Sorry Kuchibiru-chan, I'm gonna need to borrow her for a little bit!"
    if getSkill("Athletics") > 3:
        "Shiori-chan was pulled swiftly and effortlessly, and soon the two of us were going towards my planned destination."
    else:
        "I barely made it a few inches before I felt a short tug from Shiori-chan's arm which stopped me dead in my place."
        AE "Oof! H-Hotsure-san, what was that?"
        MC "Pah... ah... s-sorry, I was just... trying to be cute."
        MCT "She's so heavy!"
        AE "W-well, you don't need to pull on me. What's-"
        "I looked up, a pathetic grin forming on my face as I tried to pull her again."
        MC "C-come on! I wanna... ech..."
        show AE neutral
        AE "I'll... I'll speak with you later, Kuchibiru-san."
        Yuki "Y-Yes ma'am."
        "Looking at me as though I was the most useless man on earth, Kuchibiru-chan shook her head and walked off."
    hide Yuki with dissolve
    show AE surprised at center with dissolve
    AE "Hotsure-san? What's wrong?"
    MC "No time! Come on!"
    AE "Wha-hey!"
    "I walked around her and began to push Shiori-chan's back, being careful not to touch her sensitive 'assets' for fear of a swift kick."
    AE "Ohp, what are you-?"
    MC "No words! Just come on!"
    scene School Front with fade
    show AE surprised with dissolve
    AE "Hold on, hold on, one moment!"
    MC "Agn-!"
    "Shiori-chan came to a halt, causing me to crash into her butt chest-first. I bounced off and fell onto my own."
    show AE sad
    AE "Pah... ah... just... just let me catch my breath."
    "She took in deep breaths and turned around to give me an annoyed frown."
    MC "Ach... s-sorry, Shiori-chan."
    show AE neutral-annoyed
    AE "You should know by now... I'll... hah... not tolerate running on school grounds."
    MCT "She's not mad about the airbag test?!"
    show AE surprised
    AE "N-now, what's going on?"
    MC "Well, you said your schedule would be clearing up soon, right?"
    "She looked at me apprehensively, adjusting her glasses and clearing her throat, the signs that her exhaustion had faded by now."
    show AE neutral-annoyed
    AE "Well, yes, but what does that have to do with rushing me out to the gate?"
    MC "I was thinking... we should go out and do something fun!"
    show AE neutral
    AE "Fun?"
    "She looked out past the gate and took a step back with a concerned look, putting her hands up."
    show AE neutral-annoyed
    AE "What exactly do you have in mind?"
    MC "Well... I mean, we haven't really been off campus before."
    stop music
    "As I spoke, her look of concern faded slowly into her usual deadpan judgmental look, her hands going back down to her sides as she let out an exasperated sigh."
    play music Bittersweet
    AE "...Come now, Hotsure-san."
    MC "Ahah, I'm serious."
    AE "I've not a single reason to leave the campus."
    MCT "She doesn't... want to go?"
    AE "Why openly invite their calumny and consternation? I can sustain my life here perfectly well on the premises. I'd rather not be a public disturbance, anyways."
    "There was a bit of silence. To say I was a bit annoyed was an understatement, after waiting all day and taking her out here; that much was evident in my tone."
    MC "Shiori-chan, this school isn't meant to be a prison. It's meant to allow students to adapt into new lives."
    show AE neutral
    AE "Prison? No. I'd scarcely call our school a prison. It's meant to be a sanctuary from the prying eyes of the public."
    MCT "I can't believe her!"
    MC "And what about when we graduate? Will our homes be our sanctuaries? We can't just shelter ourselves from the outside forever."
    show AE angry
    AE "I-I have no intention of 'sheltering' myself!"
    show AE embarrassed
    AE "I'd just prefer... not to be seen in my current circumstances. Not a thing more."
    MCT "...Is that why she doesn't want to go out?"
    MC "Ach-The town is full of people like us, or at least who understand us! They have buildings and stuff made for people in our conditions."
    "Shiori-chan looked out past the gate once more and opened her mouth to speak."
    show AE sad
    AE "You... you have a point, Hotsure-san."
    "A point which she refuted by taking another step back."
    show AE neutral-annoyed
    AE "However, my point still stands that I have no desire to go walking about in such a public place."
    MC "Well, can't we at least-?"
    show AE angry
    AE "My answer is no, Hotsure-san."
    "Silence. I wasn't sure what to say, or how to vent my frustration to her."
    MC "Oh."
    show AE sad
    AE "I appreciate your dedication to our relationship, and I understand that you feel a bit... underwhelmed by our interactions at times."
    MC "I-I don't! I just..."
    MC "I dunno. I wanted to go out and be a couple... out there, you know?"
    AE "I..."
    AE "I don't know why that's such an important aspect of a relationship to you, but..."
    AE "N-no. I'm sorry. I have no intent to leave the campus."
    MC "O-okay. I just figured... you'd want a bit of freedom, is all."
    show AE neutral
    AE "..."
    "Shiori-chan turned around, her wide rear carrying the inertia and jiggling a little bit as she turned from me."
    show AE sad
    AE "You've a very strange definition of freedom."
    "She began to walk away, but I could tell that she felt at least somewhat bad about denying me an opportunity to spend some time with her."
    stop music
    AE "If you want... I'll be on the roof. Meet me there at around five, please?"
    MC "...Sure."
    AE "I just need to catch up a bit with Kuchibiru-san. Honest."
    scene black with fade
    "She walked off, and I waited by the gate for a moment. Disappointed, I walked towards the school and waited in the courtyard. Three minutes from when we'd meet, I went up to the roof and awaited her, watching the sun wane in the sky as I sat on the bench."
    scene Roof with fade
    #CREEAK
    play music Hallway
    MCT "Ah, there she is."
    "Shiori-chan came up from the stairway, her black hair blowing softly with the wind as she walked over to me."
    show AE neutral with dissolve
    AE "Good evening, Hotsure-san."
    MC "Hi."
    show AE sad
    AE "..."
    MC "...Um..."
    AE "I've many things to apologi-"
    MC "I want to apologize to-"
    MC "Oh."
    AE "I... I suppose I'll go first so we don't argue about who should start."
    MCT "Heh... barely any time since we became official and she knows me too well."
    AE "I was a bit too heartless by denying you so quickly and fervently. I didn't take how you felt into consideration."
    AE "I'm just... you can see why I'd be a bit uncomfortable out in public, yes?"
    MC "Well, yeah, of course! And that's why I wanted to apologize. I as well didn't think about if it made you uncomfortable, and that's messed up."
    AE "Oh, come now, Hotsure-san, you don't need to do that for me."
    MC "You're willing to do it for me, why can't I for you?"
    show AE neutral
    AE "Well, I'm... as the student council president I have to take things as they come, regardless of how I feel."
    MC "Well what about as my girlfriend? You shouldn't be subjected to that from me."
    show AE happy
    AE "...You've a very good nature, Keisuke Hotsure."
    AE "Very good indeed..."
    show AE sad
    AE "I can't say I understand your more socialite natures, however."
    MC "What can I say, I just want... people to know about our love."
    show AE neutral-annoyed
    AE "For what? How could people knowing about us matter?"
    MC "...I thought you'd be more proud of our relationship."
    show AE sad
    AE "...And I believed that the feelings we shared together would be enough."
    MC "I-it is! I don't mean to say... I mean..."
    MC "I'm sorry. I didn't mean to imply-"
    AE "I felt like that was manipulative."
    MC "Huh?"
    AE "I... I shouldn't have said that. It's such an underhanded comeback."
    MC "Well, no, it's how you feel."
    AE "Haah... I'm sorry, Hotsure-san. You're right. I'm... I'm being foolish in my reasoning."
    AE "...Hmph..."
    "Holding on tightly to the metal balustrades, Shiori-chan looked out towards the town. She squinted her eyes and inhaled, a brisk air of contemplation overtaking her as the slowly appearing lights of the town flickered across the lenses of her glasses. Exhaling, she turned to me and nodded."
    AE "I must admit, Hotsure-san, it's truly a wondrous view."
    MC "Yeah, there's a whole town out there."
    AE "..."
    show AE neutral
    AE "Very well, Hotsure-san."
    MC "Hm?"
    AE "I'll... indulge a bit in your strange freedom."
    MC "Shiori-chan?"
    show AE sad
    AE "I...I don't have many logical reasons to say no given your arguments. I was being overly emotional, and I apologize for that."
    MC "No, don't! I understand why you'd feel uncomfortable."
    AE "I'm not sure why going out and being a 'public' couple is important to you. I don't foresee myself ever understanding that mentality."
    show AE happy
    AE "But the fact that it is something important to you... I suppose that gives me enough reason to give it a try."
    MC "Hah, Shi-"
    show AE neutral-annoyed
    AE "School rules still apply out there, however. I expect you to act and behave as an upright member of society and I wish for you to keep curfew in mind."
    MC "...Of course."
    "I walked up behind her, and placed my hand upon hers. Our hands rested there together on the cold metal, but we couldn't be warmer. We watched the sun sink in the sky until curfew hit, and by then we'd walked to our dorms as I anticipated our adventure outside the gates."
    jump daymenu

label AE037:
    $setProgress("AE", "AE038")
    scene School Front with fade
    #SCENE AFTERNOON
    #BIRD CHIRPING SFX
    play music Peaceful
    "The day had come for Shiori-chan and I to go to town. Thankfully, the forecast was sunny and cool for the rest of the day, and the birds chirped happily in the branches of the tree near the gate I was resting my back against."
    "I took a breath and looked around for a bit; Shiori-chan hadn't come yet."
    MC "Hm... I'm sure she's just getting ready."
    "I took a bit after class myself to get prepared. I sported a pair of jeans, a brown leather jacket, and a beige shirt. The jacket itself was my dad's, but it fit me like a glove."
    "I ran my fingers through my hair, now well at lower-back length, as I picked apart a few stray mats. I usually made sure to brush when I could, but at this point it'd become too much of a chore."
    "Still, hair was the least of my worries. Did I forget to mention a time? Did she want to back out?"
    "However, thankfully my worries were assuaged once I saw her unmistakable form around the corner."
    MC "Hey-! Uhh..."
    "My eyes widened as I took a glance at what she was wearing."
    MCT "S-she..."
    show AE neutral with dissolve
    MCT "Hasn't changed at all since class..."
    "I gave a weak smile, and she tilted her head."
    AE "Hm? Is something the matter?"
    MC "No, no, I just... didn't expect you to be in uniform, is all."
    AE "Is that a problem?"
    MC "N-no, it's fine."
    "Admittedly, I was a bit disappointed. I'd at least hoped she would have dressed up in something more casual to shake things up."
    AE "..."
    show AE aroused-3
    AE "I... *khm* I wasn't expecting the, uh... the elaborate wardrobe, either."
    MC "It's not really elaborate. Just something I put together."
    show AE happy
    AE "You didn't have to do that."
    MC "You don't like it?"
    show AE surprised
    AE "Well, no, I never said I didn't like it. I just think it was unnecessary to dress up, is all."
    menu:
        "I just like to look good.": #+0
            jump AE037_c1_1
        "I thought you'd like it.": #+1
            jump AE037_c1_2
        "I wanted to put effort into our date.": #-1
            jump AE037_c1_3

label AE037_c1_1:
    MC "I guess I just like to look good, is all."
    show AE neutral
    AE "Indeed. I suppose it makes sense. After all, ones outwards appearance is often indicative of their personality."
    MC "And what kind of guy do I look like to you?"
    show AE sad
    AE "...Not one who I'd think would want to be seen with me."
    MC "Well, it's hard to imagine, but I guess you're not always right."
    show AE happy
    AE "..."
    AE "Hm, I guess that's a blessing, then."
    jump AE037_c1_after

label AE037_c1_2:
    MC "I just figured you'd like it, is all."
    show AE sad
    AE "You don't have to think about what I'd like."
    MC "I feel like it's my responsibility as your boyfriend. I wanted to make you comfortable, after all."
    $setAffection("AE", 1)
    show AE surprised
    AE "I-Indeed."
    show AE embarrassed
    AE "Then..."
    AE "Y-you look nice."
    MC "Eheh, thanks."
    jump AE037_c1_after

label AE037_c1_3:
    $setFlag("AE037_c1_3")
    MC "I just thought it would be nice to put a little effort into this date, is all."
    show AE sad
    AE "..."
    AE "I see. I..."
    $setAffection("AE", -1)
    AE "Well, I apologize for not having a proper dress for the occasion."
    MC "O-oh! I didn't mean it like-"
    show AE neutral
    AE "It's fine, Hotsure-san."
    MC "..."
    jump AE037_c1_after

label AE037_c1_after:
    show AE neutral
    AE "Well, shall we head off?"
    MC "Sure."
    #GATE SFX
    "I opened the metal gate and ushered her though, admittedly taking a peek at her behind as we exited the school grounds and walked along the road through the hills."
    #BIRD SFX END
    
    scene Hill Road with fade
    show AE neutral with dissolve
    "We walked along the side of the gravelly road from the school. The town was far in the distance, and seemed nestled among the green hills. After a few minutes, we'd walked past the two mountains in the front of the school into the windswept valley."
    if getSkill("Athletics") < 5:
        "After a while, I began to slow down and walk behind Shiori-chan, though not on purpose, as my shins began to ache. She slowed to match my speed and eventually we came to a stop as I sat along the hillside in the grass."
        MC "Phew~ Hah, it's quite a walk, uh- S-sorry."
        show AE happy
        AE "It's perfectly alright, Hotsure-san. Rest until you feel ready."
    else:
        "I looked to Shiori-chan, and to my surprise, after this fairly long trek hauling her wide load she still hadn't broken a sweat."
    MC "Hey, Shiori-chan."
    show AE neutral
    AE "Hm?"
    MC "Are you feeling winded or sore at all?"
    AE "I can't say I do, no."
    MC "Even with your-"
    MC "Gch!"
    MCT "D-don't talk about-!"
    show AE happy
    AE "It's perfectly fine, Hotsure-san."
    show AE embarrassed
    AE "No, no even with my... extra baggage, I'm doing just fine. In fact, I'd even say I have a much greater walking endurance now..."
    show AE neutral
    AE "Hmm... I'll need to make note of that."
    "With her words, a gust of wind blew once more through the valley. I took a deep breath in, reveling in the cool relief until I heard a peculiar sound."
    AE "*Snff.*"
    MC "Huh?"
    "I looked over worriedly at my partner, expecting to see tears in her eyes over perceived imminent public humiliation but when I looked over, she had a calm and serene face on."
    AE "*Snff*."
    MC "Everything alright?"
    AE "'Just put something together', hm?"
    MC "Umm, what does that mean?"
    show AE happy
    AE "Nothing... that's a nice cologne."
    MC "Oh, eheh."
    MC "Yeah, I brought some with me from home. Haven't really gotten a use for it until today."
    AE "I see... well, regardless, you smell nice."
    MC "Thanks."
    "We continued on, and after walking for a little bit more, we'd reached the town."
    
    scene Town with fade
    show AE neutral with dissolve
    "The afternoon brought with it plenty of students, free from their scholarly duties and willing to spend whatever money they had either earned or been sent in order to gather food, luxuries, and experiences. As the two of us walked through town, we also gathered the occasional murmur from the odd student here or there."
    "She started off strong as we walked through the streets, however, as person after person passed us I noticed her stand less and less tall. Once we got near the center of town, she'd mostly resolved to shrink back from public eye; at least as much as her gigantic ass would allow."
    "Walking closer to me, I felt her fleshy hips rhythmically rub against my leg every step she took. I forced a smile, and looked to her with hope."
    MC "See? It's not so hard to get used to just walking around with me in public."
    "I drew a breath of the fresh air in my nose and exhaled, looking down towards Shiori-chan."
    MC "It's even comforting, right?"
    "Shiori-chan, however, didn't seem to take in the environment quite as well as I was."
    show AE sad
    AE "I wouldn't exactly say I feel comfortable."
    show AE neutral
    AE "But admittedly, it's... been quite a while since I last walked about freely."
    "Looking up to the building tops, her face seemed to soften, and her worry had apparently been loosened a bit."
    show AE happy
    AE "Quite a while indeed."
    "Our trip to town had been going smoothly, and we took notice of different shops and businesses in the area, but even though I offered to pay, she herself seemed a bit hesitant to walk in anywhere."
    "We made our way to the center of town, and rested on a bench beside a fountain. We stopped at a gyoza vendor and ordered two sticks, which we munched on as we talked."
    AE "I must say, Hotsure-san, it is rather refreshing to be out and about."
    MC "I'll say."
    "Though she kept her posture, upright, I slouched a bit in the bench. Surprisingly, and to my relief, she said nothing about it."
    MC "Hey, look at that building, right there."
    show AE neutral
    AE "Hm?"
    MC "Do you see that dome at the top?"
    AE "The... dome?"
    MC "Yeah, the one with the green top."
    AE "Yes, I see it."
    MC "It's called a cupola. It's a western design."
    show AE happy
    AE "I see, interesting."
    "I gave a self-proud smirk at Shiori-chan."
    MC "Hmph, I'm glad I know something you don't~."
    show AE neutral-annoyed
    AE "Ach- Alright, then sir acumen, why is it green?"
    MC "Eh?"
    MC "Oh, uh..."
    show AE happy
    AE "Mmmhm, quite embarrassing, no?"
    AE "It's oxidized copper, verdigris."
    MC "Oh, pssh, who'll know that?"
    show AE neutral-smug
    AE "Oh, I don't know, anyone who would have paid attention in the chemistry lesson last week, perhaps?"
    MC "Gak-!!"
    AE "Well, it seems I've found a point we should study together, no?"
    MC "...Heh, I wouldn't mind."
    show AE happy
    AE "Hmm~."
    "We sat in silence and listened as the people walked by. Eventually, however, Shiori-chan noticed something out of the side of her eye..."
    "A child passing by had begun to stare at her thighs, which had taken up a fair amount of space on the already spacious bench. Their mother scolded them, but looked back at Shiori-chan, causing her to cross her legs."
    show AE sad
    AE "..."
    MC "Are you actually uncomfortable right now?"
    "I asked a question with an obvious answer, however I felt as though I wanted to clear the air between us. As I spoke, a grown man passed, and turned around to catch a glimpse at Shiori-chan's 'unique growth'."
    AE "A bit."
    MC "The people here have seen all types of students from the school. It's just like our hallways, just that the students here aren't wearing uniforms."
    show AE neutral-annoyed
    AE "I-I can handle regular people, Hotsure-san. You don't need to put sugar in the medicine for me."
    show AE neutral
    AE "But..."
    show AE happy
    AE "Thank you for trying to help, I suppose."
    "Shiori-chan propped herself on the benches arm to lift herself. I offered to help her up, but she looked around and refused."
    show AE neutral
    AE "So, *umph*, is it often that you like to take walks?"
    MC "Yeah, back in Tokyo I'd usually take long walks from time to time, but... I dunno, this time it's a lot more serene, I guess."
    "We began to walk together along the sidewalk, her backside bouncing up and down rhythmically with her steps."
    MC "Not as many people around here as there are back home."
    AE "Yes, well, that's quite the blessing, at least."
    MC "..."
    MC "...Do you wanna go back?"
    show AE surprised
    AE "Wha-?"
    MC "Because if you really wanna go back that badly, then we can-"
    show AE sad
    AE "No, no. You're right. I'm being obtuse."
    AE "I... I'm sorry."
    "Shiori-chan looked down and pursed her lips. Though it was true I said what I did out of annoyance, I quickly changed my tone."
    MC "Oh! I mean, well, I didn't mean in, like, an annoyed way, I meant if you felt uncomfortable we could always... you know, go back and watch a movie."
    show AE neutral
    AE "No. I want this. It's good for me to get used to having a public presence like... this."
    menu:
        "I wanted to help you feel normal.": #-3
            jump AE037_c2_1
        "I thought it'd be nice to share experiences with you.": #+2 
            jump AE037_c2_2

label AE037_c2_1:
    $setFlag("AE037_c2_1")
    MC "I'm sorry. I just wanted to help you feel normal."
    stop music
    AE "..."
    AE "Normal?"
    MC "Shiori-chan?"
    "Her body tensed up, and she brought her knuckle up to her teeth and bit down gently."
    $setAffection("AE", -3)
    show AE angry
    AE "You wanted to help me feel NORMAL by parading me-!"
    show AE neutral-annoyed
    AE "..."
    "She stopped and looked around, though it seemed most were ignoring her small outburst, she took a breath and brought her hand down."
    show AE sad
    play music Peaceful
    AE "N-no. Your intentions were good. I... I'm sorry, Hotsure-san."
    MC "Shiori-chan... I didn't mean it like-"
    show AE neutral-annoyed
    AE "Your intentions are good, Hotsure-san. I think we should leave it at that."
    MC "...Okay."
    jump AE037_c2_after

label AE037_c2_2:
    $setFlag("AE037_c2_2")
    MC "I just wanted to let today be a day we can share experiences together."
    show AE happy
    AE "It... it was, Hotsure-san. It still is."
    "Shiori-chan took me by the hand, and wrapped her fingers tight around my own."
    $setAffection("AE", 2)
    AE "We can... we should make today an experience."
    MC "...Yeah. Make it one worth remembering. Our first day in town together."
    "We walked around town a bit more, admiring the sights and happily talking about a menagerie of different topics."
    jump AE037_c2_after

label AE037_c2_after:
    scene Hill Road with fade
    show AE neutral with dissolve
    "As the sun began to wane, the two of us headed back up the hillside to the school in order to make it back by curfew."
    MC "So, what'd you think?"
    if getFlag("AE037_c2_1"):
        show AE neutral
        AE "...It went as expected."
        MC "Oh?"
        AE "...If... if you're happy, that's what matters to me."
        show AE happy
        AE "So, in that regard... thank you for taking me out."
        MC "...Uh, n-no problem."
    if getFlag("AE037_c2_2"):
        show AE happy
        AE "Hmm... there were a few hiccups, but being with you made the experience..."
        AE "I'm glad you were there with me."
        MC "The pleasure was mine."
    if getFlag("AE037_c1_3"):
        show AE sad
        AE "..."
        AE "Do you... not think I look appealing?"
        MC "Hm?"
        AE "It's just that you're all dressed up and I'm not and that could make you look-"
        show AE embarrassed
        AE "I mean, even if I HAD dressed up, I couldn't hide my... um..."
        AE "I apologize, Hotsure-san, for making you look bad."
        MC "Huh? N-no! You looked great. I just... I meant like, you didn't need to stay in your uniform if it was uncomfortable."
        show AE neutral
        AE "Comfortable...?"
        show AE sad
        AE "..."
        AE "Yes, Hotsure-san. I'd... I'd actually say that this IS my most comforting wardrobe."
    "We walked together through the windy valley towards the school, and entered the gate."
    scene School Front with fade
    MC "I had a really good time."
    show AE happy
    AE "I'm glad for that."
    MC "Well, uh... I'm not quite sure how to end our day, eheh..."
    if getFlag("AE037_c2_1"):
        show AE sad
        AE "..."
        AE "I realize today didn't quite go as you wanted."
        MC "Hm?"
        show AE embarrassed
        AE "...I'm... willing to give it another try. If it would make you feel better."
        MC "O-oh... um... if you're uncomfortable with-"
        show AE neutral
        AE "No. It's good practice, and... despite some of the more unfavorable moments, I felt as though we had some good times there."
        MC "If that's what you want, sure."
        AE "No, if that's what YOU want."
        MC "...Eheh, sure, why not."
        show AE happy
        AE "Very well then. Here's hoping for a better try the second time. Definition of insanity be damned."
    if getFlag("AE037_c2_2"):
        show AE embarrassed
        AE "...Would you like to go again?"
        MC "Hm?"
        "Shiori-chan looked down to her feet as she brushed stray locks of hair to the side."
        AE "I mean, we didn't see ALL of the town... perhaps we can share the experience again sometime?"
        MC "...I'd love that."
    "We went our separate ways, the memory of our times in town still fresh in my head as I thought of what all we could do together the next time we go."
    jump daymenu

label AE038:
    $setProgress("AE", "AE039")
    #Scene Afternoon 
    scene Hill Road with fade
    play music Schoolday
    show AE neutral with dissolve
    "The wind blew softly through the valley as Shiori-chan and I walked to town, causing the grass of the green valley to sway gently in the breeze, along with her skirt, which fluttered gently as she walked."
    "Shiori-chan seemed to be lost in a bit of contemplation, and hadn't been talking much throughout the walk. I was worried it was about last time we went to town."
    MC "Hey."
    AE "Hm?"
    "She looked up towards me. Her eyes met my own, and thankfully I saw no worry in them."
    MC "Are you feeling all right?"
    AE "Yes, Hotsure-san. Thank you for asking."
    MC "I've noticed that you've been going to meetings less. Everything all right there?"
    show AE neutral-annoyed
    AE "Not of my own volition. We've been hitting a bit of a wall with productivity, and our meetings seem to be getting shorter."
    AE "It's natural for work to slow over time. So long as it doesn't halt altogether, then I'll be fine with it. For now."
    MC "Yeah?"
    show AE happy
    AE "Mhm. It means I get to spend more time with you."
    "I grinned, and let out a little scoff. Shiori-chan smiled softly in response."
    MC "That line was so cheesy I can't help but think I'm rubbing off on you a bit."
    AE "..."
    "Her smile slowly faded, and her contemplative look soon returned. She pushed her glasses up with her fingers, as she was oft to do."
    AE "Yes, well, I suppose that too is natural."
    MC "...Hm... yeah."
    scene black with fade
    "We continued to walk, and eventually we reached the town."
    scene Town with fade
    show AE neutral with dissolve
    "The town was much more calm today. We walked around for a bit, taking in the layout of the different shops, and we soon found ourselves in a part of the town neither of us had ventured to yet."
    MC "Oh cool, there's the convenience store! It's the same chain as the one my dad ran."
    show AE surprised
    AE "..."
    "Shiori-chan, however, appeared to be distracted by something. It wasn't the same as on the walk here, but it was a definite change."
    MC "Are you feeling alright?"
    show AE neutral
    AE "...Indeed."
    MC "Hmm... C'mon, you can tell me anything. What is it?"
    AE "No, no, I don't want you to-"
    "I stopped her by walking out in front of her, causing her to stop before collision."
    MC "Shiori-chan, I'm worried. You've really been acting weird today, and I want to know what's up."
    show AE sad
    AE "...If you must know... I haven't eaten yet."
    MCT "O-oh."
    "I let out a sigh of relief, knowing her odd behavior was more due to hunger than anything I did."
    MC "Ahaaaah, I knew skipping lunch would have come back for ya."
    MC "When was the last time you ate?"
    show AE embarrassed
    AE "Well, I've been busy, and..."
    AE "...Yesterday morning."
    MC "What?! Aren't you hungry?"
    show AE neutral-annoyed
    AE "I'm perfectly fine, Hotsure-san. I'm not-"
    #*STOMACH GRUMBLE SFX*
    MC "..."
    show AE neutral
    AE "..."
    "Shiori-chan crossed her arms over her chest and looked away, attempting to ignore the situation altogether."
    #*GRUMBLE SFX*
    "Her body betrayed her."
    MC "Here, c'mon, there's a restaurant over here."
    AE "That won't be necessary, I don't have-"
    "I took Shiori-chan by the hand and lead her over."
    show AE surprised
    AE "O-oh?"
    MC "Let's check it out. It looks like a Youshoku place."
    "With Shiori-chan's hand still in mine, we entered the restaurant."
    scene Restaurant with fade
    show AE neutral with dissolve
    "The bell above the door dinged, and a kindly looking woman at the front bowed."
    Waitress "Welcome! Just two?"
    MC "Yes, ma'am."
    "The waitress looked at the two of us holding hands and gave a little smile. After nodding, however, she took a closer look at Shiori-chan and noticed her 'assets'. She drew in some breath and looked away for a moment."
    Waitress "O-oh, students. Um, is this your friend?"
    MC "Girlfriend, yes."
    Waitress "O-oh.~"
    "She still kept her professional smile, and yet she seemed to have a bit more apprehension."
    AE "..."
    Waitress "R-right this way."
    "Walking through the restaurant, there seemed to be a few patrons here and there. Some in Seichou uniforms, others in regular clothes. Most of them were couples, it seemed."
    Waitress "Table or booth?"
    AE "Booth would be preferable."
    Waitress "Oh! Y-yes, of course. My apologies."
    "I ushered Shiori-chan into her seat near the window. It was a bit of a tight squeeze between the booth, her rump, and the table, but she managed. I then took my own."
    show AE neutral-annoyed
    AE "Mph."
    Waitress "Does this work ma'am?"
    show AE neutral
    AE "Yes."
    Waitress "Good to hear."
    show AE sad
    AE "You don't-"
    Waitress "Hm?"
    show AE neutral
    AE "You don't get many students with... *khm*, my type of growth here, do you?"
    "The waitress appeared to be taken aback for a moment, but responded softly."
    Waitress "N-not often, no."
    show AE embarrassed
    AE "A-ah. I apologize ma'am. I didn't mean to, trouble you."
    Waitress "No, no trouble at all."
    "She pulled out a pair of menus, as well as a small piece of paper on a leather pad. I looked over the menu as she did, and noticed an array of different western style foods."
    Waitress "Can I get you anything to drink?"
    show AE neutral
    AE "I'd like tea, please. Pu'er, if you have it."
    Waitress "I'm sorry, we don't ma'am."
    AE "Green would do well then."
    Waitress "Okay, and you sir?"
    MC "Hm?"
    "I caught myself thinking about the exchange that happened with Shiori-chan and the waitress that I wasn't paying attention."
    Waitress "Your drink, sir?"
    MC "I'd just like a cola, thank you."
    Waitress "Okay, I'll be back."
    "She walked off, leaving the two of us to talk. As I was about to talk, Shiori-chan piped up with a comment."
    AE "Cola?"
    MC "Hm?"
    AE "I'd never really taken you for much of a soda person, to be honest."
    MCT "Soda... person?"
    MC "Ehh... yeah, from time to time."
    AE "Mm, well, I hope you brush your teeth often."
    MC "Eh?"
    show AE neutral-annoyed
    AE "You do, right?"
    MC "Well, I mean... every now and again."
    AE "Come now, Hotsure-san. If I can find the time to brush my teeth in the mornings surely you can."
    MC "H-hey! My breath is fine!"
    AE "It's about more than smell, it's oral health."
    MC "All right, all right, I'll brush more. Happy, mom?"
    show AE angry
    AE "...Don-"
    Waitress "Thank you for waiting!"
    show AE neutral
    "The waitress placed our drinks out in front of us, and went back to her pad."
    Waitress "What would you like to order, sir?"
    MC "Oh, uhh, I'll have the curry rice, please."
    "I looked over to Shiori-chan, who oddly didn't have her menu open at all."
    MC "You know what you want?"
    AE "N-no, I'm not getting anything."
    MC "Huh?"
    show AE sad
    AE "I... didn't bring much money with me."
    MC "Oh, don't worry, I'll pay."
    show AE surprised
    AE "You don't need to-"
    MC "No, no, I want to. You're my girlfriend, it's normal."
    "Admittedly, I would have been more than happy to go Dutch with the bill, but I wanted to leave a good impression."
    AE "Are you sure? I mean, I-"
    MC "D-don't worry about paying me back, it's fine! Now tell me, anything you like?"
    "Shiori-chan's looked at me silently for a moment, hand over her chest as she stared. However, not to waste time, she looked over the menu."
    show AE neutral
    AE "T-the, um, Beefsteak, please."
    Waitress "All right! I'll be right out with those!"
    "As she walked away, Shiori-chan looked at me with the same awe she did earlier. I took a sip of my drink, and my eye caught hers."
    MC "Something the matter?"
    show AE embarrassed
    AE "You're... you're very generous, Hotsure-san."
    MC "Huh?"
    AE "B-buying lunch for the two of us."
    MC "Don't worry! I'm the boyfriend, right? I pay for that kind of stuff on dates."
    AE "..."
    "Shiori-chan blushed a little, and twiddled her hair in her fingers, avoiding eye contact by looking out the window."
    MCT "Is... is everything okay?"
    show AE neutral
    AE "How is your drink?"
    MC "Hm? The soda?"
    AE "Yes."
    MC "I-It's good, yeah."
    AE "Hm."
    MC "..."
    AE "..."
    MC "...Have you never drank soda before?"
    AE "I never got around to... the sugar alone is..."
    AE "No, I suppose I haven't."
    MC "Here."
    AE "Hm?"
    MC "Try a sip!"
    AE "O-oh, I couldn't-"
    MC "C'moon.~"
    AE "It's your drink, I-"
    MC "Try iiittt.~"
    AE "..."
    "Shiori-chan took the straw in her mouth and sucked on it lightly. The moment the saccharine drink went from the straw to her mouth, her eyes widened and she pulled away."
    show AE surprised
    AE "Mmph."
    MC "Don't like it?"
    AE "A... A-"
    AE "*Urp*"
    "Shiori-chan's face turned bright red as she let out a tiny burp. She covered her face with her hands and looked away."
    MC "Pff, eheh."
    AE "H-Hotsure-san, I apologize. That was very unladylike of me."
    show AE sad
    AE "Ugh, I must look like a pig."
    MC "D-don't worry, it's all right!"
    show AE surprised
    AE "Is it supposed to be that fizzy? I mean, I know the effects of carbonation and all, but-"
    "As Shiori-chan frantically explained on, the waitress walked over with our food."
    Waitress "And heeeere's your order!"
    MC "O-oh? That fast?"
    Waitress "Mhm! Tell me if there's anything you need, lovebirds.~"
    show AE embarrassed
    AE "L-lovebirds?"
    "The waitress walked away, leaving us with our piping hot meals. I took a bite of the curry; the warm soft meat mixing well with the rice. However, Shiori-chan's beefsteak must have been made in heaven, based on the look on her face as she ate."
    MCT "Does she... always get like this when she eats?"
    MC "Hey, Shiori-chan?"
    show AE neutral
    AE "Hm?"
    MC "What's the best meal you've ever had?"
    if getAffection("AE") > 15: #IF POINTS ABOVE 2/3 OF TOTAL
        show AE happy
        AE "Well, I'd... I'd say the bento you made me."
        MC "Ach, c'mon. You don't gotta try and be cute-"
        show AE surprised
        AE "I'm serious, Hotsure-san."
        "Holding her chopsticks off to the side, a gentle complacent smile overcame her face."
        show AE happy
        AE "I'd never really tasted food like yours before. It just... When I eat, it's for nutritional reasons, you'd understand, but... the way you make your food makes me feel warm inside."
        "Shiori-chan took another bite of her food."
        MC "Because I made it for you?"
        "Shiori-chan smiled a bit, and covered her mouth with her hand as she chewed, looking away from me."
        AE "I suppose so, yes."
    else:
        show AE happy
        AE "Hmm...You know, when I was in High School, I once shared lunch with my piano teacher. And he had this dish that, to this day, I've yet to find anything more appetizing."
        MC "What was it?"
        AE "I believe it was liver and onions."
        "The mere mention of the name made me nearly gag at the thought of what it must smell like, let alone taste like."
        MC "R-really?!"
        AE "What? It's pungent, but extremely flavorful. You should try it some time."
        MCT "Hard pass."
    "We had a nice meal together, and by the time we finished, it was nearing curfew. I paid the bill, to Shiori-chan's obvious admiration, and the two of us left in time to make it back before sundown, holding hands the whole way."
    jump daymenu

label AE039:
    #SCENE AFTERNOON
    $setProgress("AE", "AE040")
    scene Town with fade
    play music Schoolday
    show AE neutral with dissolve
    "As Shiori-chan and I walked through town, the murmur of bustling crowds and the gentle rumble of vehicles permeated the air, giving me a distinct feeling of nostalgia for home."
    #%If the area hasn't been seen before%
    "We explored the town like usual, however today we found ourselves in a new area; one with tall apartment complexes, brand name stores, and plenty of motorbikes and cars going to and fro."
    #%If the area has been seen before%
    ##Today, I decided to take Shiori-chan to a new part of town for her; the commercial area. I was worried at first, but she actually seemed to not mind all the people.#
    "Despite the crowds, Shiori-chan seemed calm and composed, staying as close as her behind would allow to me while taking in the sights and sounds around her."
    #%If this area hasn't been seen before%
    MC "Look at this place! I'd never expect something like this from the island."
    #%If this area has been seen before%
    #K: What do ya think? Not expecting all this from our little island, huh?
    AE "Well, it makes sense. If there's a sustained community here, there has to be somewhere for the people to stay."
    MC "Yeah, I guess so. Still feels nice to have somewhere that feels like home, though."
    "Rounding a street corner, we made it to the main strip of the commercial area. Brand name shops with vibrant street signs filled both sides of the bustling street, people young and old conversing over coffee, and students handing out pocket tissues every few feet."
    MCT "Yep, definitely feels like home."
    show AE happy
    AE "So, got any ideas for where you want to go?"
    MC "Eh, I dunno. I'm thinking I may just walk around for a bit, get a lay of the land."
    show AE neutral
    AE "Sounds good to me."
    "We walked forward, window shopping as we did, thinking of what would look good on each other, talking about posters for upcoming movies, but then I noticed something. A few feet away from the end of the street, Shiori-chan stopped, and looked away to a building on the other side of the road."
    MC "Hm? Yo, Shiori-chan, everything okay?"
    show AE surprised
    AE "That store... across the street."
    "Craning my neck to see further, I noticed a store with a purple and yellow awning, the characters for 'Amatsu Game Store' on the window pane. Shiori-chan turned around after addressing it to me."
    MC "Amatsu? Never heard of it."
    show AE happy
    AE "Aha, that's... it's an old store from my childhood."
    MC "Huh? Wait, really?"
    AE "Mhm."
    MC "You played video games?"
    show AE neutral
    AE "Board games. It was hard finding other players, but when I did, it was a lot of fun. The one by my house closed down, so I never really found anywhere else to play."
    MC "Board games? Like chess?"
    AE "Well, I actually don't know much about chess... but there is *one* game in particular."
    "Shiori-chan turned back to the store, and let out a reminiscent sigh."
    show AE happy
    AE "Haah, it's just been so many years."
    MC "...Shiori-chan."
    show AE neutral
    AE "Hm?"
    MC "Do you want to go in?"
    "Although at first I thought she may have been guilt-tripping me into wanting to check it out, her surprised reaction showed she hadn't expected me to say that."
    show AE surprised
    AE "...M-may we?"
    MC "Eheh, sure."
    "Taking her hand, we waited at the stop light to cross before getting to the front of the store. I held it open and motioned for her to go in first."
    
    scene Game Store with fade
    "As we entered the building, a strange smell of cheap cinnamon-apple air freshener and dust permeated the air. Behind glass displays, miniature soldiers and creatures were painted a variety of vibrant colors with precise detail."
    "Along the walls, wooden shelves contained a plethora of shrink wrapped books and board games, some in Japanese, but a majority having logos in what appeared to be English. While I was taking in the sights, Shiori-chan looked around, the nostalgia creeping in."
    show AE happy with dissolve
    AE "Wow... It's just like the one back home."
    MC "Are there a lot of these stores?"
    show AE surprised
    AE "No, that's why I was so surprised to see one here of all places."
    MC "Well, hey, guess today's a day full of surprises."
    Owner "Welcome! Is there anything I can help you with?"
    show AE happy
    AE "Yes, sir. I was wondering if you-"
    "As Shiori-chan spoke with the shopkeep, I looked around a bit more. In a glass case, small, plastic die had been cut into strange shapes, some even getting to thirty sides. Looking around, I noticed the posters on the walls of different fantasy creatures, and wondered just what kind of games Shiori-chan was into."
    AE "Hotsure-san?"
    MC "Hm? Yeah?"
    AE "Come. I've something to show you."
    MCT "Wait, her face... is she trying to contain happiness?"
    MCT "That's... wow. I don't think I've ever seen her do that before."
    MC "A-alright, sure."
    "Taking my hand, she lead me to the back of the store, where there was a single table. The table was covered in miniature buildings and grass, like what you'd see in one of those miniature train collections, and on the sides of the room, inside glass cases, were hundreds of plastic miniature soldiers. And the sign above the table said..."
    MC "Warblade 4000?"
    AE "Mhm, it's... my favorite strategy game."
    AE "I didn't play it often, but when I did it was the highlight of my week other than homework."
    MCT "Homework... shouldn't be the highlight of anyone's week."
    MC "Why'd you stop playing?"
    show AE neutral
    AE "Ah, well, a multitude of reasons. Primarily, as I grew older, I had less time for games. It also didn't help that not many people I knew played it."
    AE "But still, even playing on a board with complete strangers, the game was just always so fun to me."
    show AE sad
    AE "...Um... the regular pieces can be kind of expensive. I had to work for weeks to afford my only box of soldiers... but they have demo versions for first time players..."
    AE "Do you... um..."
    AE "Nevermind."
    MCT "I can tell this is something that she's passionate about. If that's the case, then..."
    MC "I'd love to play it with you, Shiori-chan."
    show AE happy
    "For the first time since I've known her, Shiori-chan's eyes lit up with childlike wonder and excitement; a concept I once thought lost on her entirely."
    AE "A-ah, yes well..."
    "She tried to act calm, but she couldn't hide her adorable smile from me in her current state. She nodded, and motioned to the glass displays."
    AE "Alright, first things first, pick your army."
    show AE neutral
    AE "I will be playing as 'The Order'."
    MC "Okay. Umm..."
    "There were a multitude of different armies to choose from, strange alien creatures, spikey elves, and robot skeletons. After a bit of deliberation, I just picked one at absolute random."
    MC "I'll go Space Military. They have cool looking tanks."
    show AE happy
    AE "Good choice!"
    MCT "Is it really though?"
    show AE neutral
    AE "So, next, the rules."
    AE "The conditions for victory are simple. Destroy the enemy's army, control all points on the map, or have the most points by turn 20."
    MC "Sounds easy enough."
    show AE happy
    AE "Definitely. This game is the epitome of simplicity and hands on gameplay."
    AE "So, here are the dice."
    "Within a breath of her previous statement, she pulled out two buckets of dice from the bottom of the table."
    AE "We roll them to take an action."
    MC "Wow... that's a lot of dice."
    show AE neutral
    AE "Indeed."
    MC "So... just pick which ones we use?"
    AE "Hm... I estimate there's around twenty six dice in each sooo..."
    "She looked into the bucket and jostled the dice around before looking back up at me."
    AE "No, we will probably need to use every one each turn."
    MC "..."
    MC "Shiori-chan?"
    AE "Hm?"
    MC "Is there a lot of math in this game?"
    "But she had already pulled out a clean notepad and pencil from her pocket."
    AE "Pardon?"
    MC "...Never mind."
    MCT "What have I gotten myself into?"
    AE "Now, moving your soldiers. You use a... hm... let's see. Ruler, ruler, Hotsure-san, is there a ruler on your side?"
    MC "Wait, a ruler?"
    AE "Yes."
    MC "What do you need a ruler for?"
    AE "You roll to see how many inches your squads can move."
    MC "Um, Shiori-chan?"
    AE "Hm?"
    MC "Is there anything you... {i}don't{/i} roll for?"
    AE "No."
    MC "Oookay."
    "After I pulled out the ruler from the side compartment Shiori-chan pointed out, she pulled out a deck of cards from the side wall."
    MC "Okay, wait, no, cards too?"
    AE "These are spell cards."
    MC "Wait, spells?"
    AE "Yes. Each team can have a psychic character, and they can cast spells."
    MC "I thought this was sci-fi?!"
    AE "They can be stacked with leader abilities, a-"
    MC "Do you have to roll for them?"
    AE "You have to roll for them."
    MC "Of course."
    AE "When you roll an attack spell, for example, you then roll to see the area in which it can attack."
    MC "Area?"
    show AE happy
    AE "Yes, which is why we use this."
    MCT "Aaaand out comes the protractor."
    AE "You roll nine twenty sided die to determine how much of the protractors radius is covered by the spell, which as well accounts for the direction, and for the reach of its effect, you can use the tape measurer to-"
    MCT "CHANGE THE SUBJECT NOW."
    MC "I gotta say, I like the little details on the building ruins."
    AE "This, Hotsure-san, is cover. Your squad can hide behind it in order to evade fire, but you have to be completely obscured."
    show AE neutral
    AE "Now, back to attack spells."
    MCT "NO"
    MC "Mhm, go on."
    MCT "Is there anything about this game that isn't a complete headache?!"
    show AE surprised
    AE "Ohp, one moment, I left the ruler on the other side."
    "As Shiori-chan reached over the table, her ass was put on full display in front of me; revealing her blue panties as they tightly squeezed her pale flesh."
    MCT "By the emperor... I think I can give this game a shot."
    scene black with fade
    pause 1
    scene Game Store with fade
    show AE neutral with dissolve
    "Shiori-chan spent the next thirty minutes explaining the intricacies of how each model has its own power level based on their equipment, my mind focused on her ample display enough to keep me looking intrigued."
    AE "-And this is a flame-wurfer. It is able to fire out through the entirety of the protractors radius at the cost of switching to a six sided die to see it's range."
    MC "Yep."
    AE "This, however is a laser cannon. It can burn the souls of-"
    "In the middle of Shiori-chan's sentence, the shopkeep, who somehow didn't pass out while listening to her talk, chimed in."
    Owner "Actually, the laser cannon no longer applies soul burn."
    show AE surprised
    AE "What? Since when?"
    Owner "Fourth edition."
    AE "Fourth? Last I knew the game still ran on second edition!"
    Owner "No, the chi were nerfed, but the plagued warriors have their own rulebook now."
    MCT "WHAT IS EVEN GOING ON?!"
    show AE sad
    AE "Hotsure-san, I apologize, but we'll have to belay the game for now. It's all too obvious that I'm not up to date."
    MC "U-uh... no problem."
    show AE neutral
    AE "Okay. Well, the full rulebook is online, thankfully."
    MC "The rulebook? Well, makes sense there's an entire book for it."
    AE "Mhm. It's not as in depth as the for sale ones, but it works for new players."
    MC "Well, then I guess that means it's it for today."
    AE "Mm. Once you feel you're covered, come see me about it, and we can get you into your first game."
    MC "R-right."
    scene black with fade
    "After thanking the shopkeep for having us, Shiori-chan and I left for the school. By the time I'd gotten back, the sun was starting to set."
    scene Dorm Interior with fade
    "Finishing my homework earlier, I went straight to the website with the rules, and was put into despair, but not surprised, to find that it was five hundred and ninety seven pages long."
    MCT "How the hell did she even get into this game?! There are so many rules that I can-"
    MCT "I just answered my own question."
    "I continued to read on, but it just seemed like a jumbled mess of lore vomit and war jargon. My mind quickly found itself indulging in other thoughts."
    MCT "This sucks. I can't remember all of this..."
    "Sighing to myself, I clicked off of the webpage and leaned back in my chair, looking up to the ceiling."
    MCT "I might just have to tell her I can't play, next time the subject comes up."
    MCT "Still, though, it was so nice to see her happy today."
    "I got off the computer and laid in the bed, cracking my neck before resting my hands behind it and thinking about how I would spend tomorrow."
    jump daymenu

label AE040:
    #SCENE AFTERNOON
    #SCENE OUTSIDE GIRLS DORM
    $setProgress("AE", "AE041")
    scene Dorm Exterior with fade
    play music Schoolday
    "As I exited the room, my eyes adjusted to the bright light of the adjacent window. I'd spent some of the afternoon with Tomoko, waiting for Shiori-chan to get done with her meeting so we could have one of our usual excursions to town."
    show Yuki neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve #happy
    show Tomoko neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    Yuki "IT WAS CRAZY! And then, and then, Shiori-chan almost knocked over the cup with her butt, but caught it and was all like 'Who brought a drink to the meeting?' and I was all like-"
    "Of course, the indication her meeting had ended came when Kuchibiru-san came in babbling about the new topic of the second."
    MC "O-okay, Okay, Kuchibiru-san, I think I'm good for now."
    "Giving a coy chuckle, I nodded to Tomoko, still perched on the edge of her bed."
    MC "I'll call mom and tell her you said hi, okay?"
    Tomoko "Okay."
    MC "Okay, and hey, you really should go out and socialize more."
    #show Yuki neutral
    Yuki "Uhuh, uhuh! I actually heard that there are some really cute boys who took a liking to you, and-"
    Tomoko "Are you sure I don't have enough in my ear for a lifetime?"
    MC "Faaaair enough."
    hide Yuki with dissolve
    hide Tomoko with dissolve
    "I waved goodbye to my sister and her gabby friend and was going to wait outside Shiori-chan's room when-"
    show Tako neutral with dissolve #happy
    Tako "Keisuke! What's good?"
    "I ran into Yureno-san, looking as hip as ever in every sense of the word."
    MC "Afternoon, Yur-"
    Tako "Soooo, a lil bird told me you and Shiori-chan walked into an Amatsu game store. That true?"
    MCT "She... didn't even try to pretend to care about how I was."
    MCT "For that matter, why does she care where we went?"
    MC "Y-yeah, Shiori-chan showed me a game, but it looked really difficult. I actually came to tell her-"
    #show Tako neutral
    Tako "Aww you don't wanna play? That's too bad."
    #show Tako happy
    Tako "Ah well. Your loss."
    MC "My... loss?"
    "She pouted her lips, putting one finger to the side of her mouth."
    #show Tako sad
    Tako "Nooo, I shouldn't. Shiori-chan would be pissed if I-"
    stop music
    #show Tako happy
    Tako "If you win, she'll give you her panties."
    MC "!?!"
    play music Busy
    MC "D-don't say such an unbelievable thing like that! Aren't you being too obvious with your lies?!"
    #show Tako smug
    Tako "Whaaat, it's true. I even-"
    #show Tako neutral
    Tako "Here, she'll tell ya."
    #show Tako happy
    Tako "OOOOOOI! Shiorear-saaan!~"
    #show Tako happy at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    show Tako neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    show AE neutral-annoyed at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    "I turned around with the speed of a cheetah, Shiori-chan quick to take note of the urgency in my eyes appeared surprised, but then quelled it with annoyance."
    AE "I don't know why you think you can just give me an asinine name such as-"
    #show Tako smug
    Tako "Hey, remember the thing you said about your panties? I told Keisuke."
    show AE embarrassed
    AE "W-w-what?!"
    MC "Shiori-chan?! Did you really say that?"
    AE "I... erm..."
    Tako "Hmmm?~"
    show AE sad
    AE "Yes. I did."
    MC "EEEHHH?!"
    #show Tako happy
    Tako "HAH! As expected, no way she'd lie!"
    show AE angry
    AE "Quiet! It's your fault I'm IN this embarrassing situation."
    MC "Are you serious?! Like, for real?!"
    show AE embarrassed
    AE "W-well, I-"
    "I placed a hand on her shoulder, and looked down to the ground. My body as stiff and still as a statue."
    show AE surprised
    AE "Huh?"
    MC "Let's go. You and me, we're playing, right now."
    AE "H-hold on. This is very sudden, we shouldn't just-"
    "Just then, I grabbed her hand, and sprinted towards the courtyard."
    AE "W-woah!"
    hide AE with dissolve
    #show Tako happy
    Tako "Woo! Give it to her, Keisuke! Make 'er squeal! Kyahahaha!"
    #show Tako neutral
    Tako "...In the meantime, I gotta go make a call..."

    scene Campus Center with fade
    show AE surprised with dissolve
    AE "H-Hotsure-san, I still have other duties to attend to today!"
    MC "Huh-uh, playin' the Warblade."

    scene School Front with fade
    show AE surprised with dissolve
    AE "I-If you'd please!"
    MC "We're doing the Warblade, let's go."

    #CHANGE SCENE VALLEY
    scene Hill Road with fade
    show AE surprised with dissolve
    if getSkill("Athletics") >= 5:
        show AE embarrassed
        AE "Pah... Ah... Hotsure-sah... agh..."
        "It would have been a cute view. An exhausted, sweaty Shiori-chan, panting for breath, massive bum in my face as she bent over to catch her breath..."
        MC "No time. Warblade."
    else:
        MC "Pah... ach... W-Warbla... hah..."
        AE "D-don't strain yourself now."
        MC "NAH, Nahg. It's fahn... I'm... ah..."
        MCT "Those panties... are mine..."

    #SCENE STORE FRONT/STREET
    scene Town with fade
    show AE sad with dissolve
    "I traveled through the mountains high and the valleys green, through the streets paved with cobble and stone. Indeed, there have been many men who have done so for the sake of booty, yay. But nary a man to do so for the promise of panties. This is my creed."
    MC "Okay. Hah... hah... here we are."
    AE "N-no... pah.. r-running in... ugh..."
    "We stopped to catch our breath, the amount of time it likely would have taken us just to walk spent resting my arm on Shiori-chan's hip as she panted away. We composed ourselves, and after a verbal thrashing to me, Shiori-chan calmed down."
    show AE surprised
    AE "H-Hotsure-san, what's gotten into you?!"
    MC "The lore is so deep. I'm just so enticed by the plot."
    MC "We have to play now."
    AE "Are you sure? Yesterday you didn't seem like you knew-"
    MC "You know what those words sound like?"
    show AE neutral
    AE "...What?"
    MC "The words of a heretic."
    show AE neutral-annoyed
    AE "Let's go."
    MCT "S-so easily?!"
    "Passion in her heart, Shiori-chan took me hand first into the store."

    scene Game Store with fade
    show AE neutral with dissolve
    "*RING RING*"
    Owner "Welcome, welcome! Is there-"
    "Before he could continue, the shopkeeper's jumped a bit in surprise."
    Owner "Oh! It's you!"
    AE "Good afternoon, sir. My friend and I were hoping that we-"
    Owner "Of course you can use the demos, ma'am! Whenever you please!"
    AE "Oh? Last I remembered, you only get one play on the demo, and then you need to know someone with a membership ca-"
    Owner "Policy changed!"
    show AE surprised
    AE "...When?"
    Owner "Ten minutes ago!"
    MCT "Ten minutes ago? That's when we left the school."
    show AE neutral-annoyed
    AE "I find it hard to believe that-"
    Owner "Come, come! Play to your heart's content!"
    "The man guided us over to a table, pre-prepared with an 'Order' and 'Space Military' army set, a dice bin, and all the accoutrements needed to play."
    Owner "Everything to your liking, ma'am?"
    show AE neutral
    AE "..."
    MC "Shiori-chan?"
    AE "Y-yes. Thank you."
    Owner "Mhmhm~"
    "The man bowed, and made his way back to the front desk, leaving the two of us confused."
    MC "What... was that?"
    AE "I'm not sure... but I will get to the bottom of it."
    "She looked over the table. Cards neatly stacked, armies placed in symmetric and orderly formations."
    show AE happy
    AE "L-later. For now, though, let's play."
    "The game began, and we soon began moving our soldiers to and fro."
    
    scene black with fade
    pause 1
    scene Game Store with fade
    show AE neutral with dissolve
    play music Tension
    MCT "Okay, my soldiers are in position around the middle of the field... and my psychic has his mouth basically wrapped around the nozzle of one of Shiori-chan's soldier's flame throwers. He can probably pop off one last spell..."
    "I looked over my cards, knowing the next one would be my last."
    "In order to use Lightning War, you must have a squad next to a tank. That squad will be able to travel at the same distance as the tank, but only if you roll above a 10 on a d20."
    MCT "d20?"
    MCT "I... should have probably read the rulebook more."
    MCT "Buuut..."
    "I glanced over to the empty plastic disk on the right side of the table."
    MCT "Point C is free for the taking. Using the Lightning War ability, I can have my soldiers rush over and take it instantly."
    MC "Moving squad with tank using 'Lightning War'."
    MCT "I gave a smirk, and reached over to the dice, hand hovering over them."
    MC "Wiiith a d20.~"
    MCT "I gauged Shiori-chan's eyes as I hovered my hand over the dice, seeing if she would react to the right one. Her eyebrows raised as I picked one up."
    MC "Ro-"
    AE "That's a d6."
    MC "...Good catch."
    "My smirk widened, as I tried to play my mistake off as psychological warfare."
    "It wasn't working."
    MC "So now I'll grab... a d20... from the-"
    AE "It means twenty sided die."
    MC "YES! Yes, yes, everyone and their mother knows that."
    "I grabbed my tank, and moved it over to-"
    AE "What are you doing?"
    MC "Huh? Oh. Moving my soldi-"
    "Shiori-chan walked over in a huff and pulled a tape measure from the side of the table."
    AE "You have to {i}roll{/i} in order to see how many you move. You need up to t5 to move fifteen inches and grab the point."
    AE "There you go. Sixteen."
    MC "..."
    MC "Aaand boom."
    "I emphatically placed a point marker on point C for my team."
    MC "With that, I now have fifteen points to your te-"
    AE "Casting 'Deep Terrain Strike.' Sending marines into point B, and rolling to see distance from the intended drop site."
    AE "Rolled one."
    MC "Eh?"
    "Shiori-chan, whether intended or not, bumped me out of the way with her rump and used a tape measure to find one inch from the center of my base."
    AE "Being unguarded, I now control point B."
    AE "I now have twenty points to your five."
    MC "A-ah..."
    AE "Why would you leave point B unguarded if you knew The Order could send troops anywhere onto the field using the 'Deep Strike' ability?"
    MC "I... was testing yo-!"
    AE "No."
    MC "Eheheh... ehhh..."
    MC "Is... is it my turn yet?"
    AE "No."
    MCT "Damnnit! Well... that's fine. After her turn, I'll use my commander unit to... um..."
    MC "Juuust to make sure you know, what is my commander's ability again?"
    AE "Commander Dogma can hide any and all units on your side."
    MCT "YEAH! I'll use that to... um... hide my soldiers! I think if I do that, I can move them anywhere I want on the-"
    AE "I use my psychic character's ability to charm any soldier on your side to mine."
    MC "Wuh..."
    show AE neutral-smug
    AE "Oh, would you look at that."
    show AE neutral
    AE "I rolled high enough to take your commander."
    MC "B-buh..."
    "Shiori-chan reached over and grabbed Commander Dogma."
    show AE neutral-smug
    AE "I'll be taking that from you."
    MC "B-but, n-no, my comma-"
    AE "Oh, trust me, he'll be much happier on the winning side."
    scene black with fade
    pause 1
    scene Game Store with fade
    MCT "This is it... last turn. Shiori-chan's destroyed most of my soldiers, and unless I can get the upper hand, she'll win by running down the clock... buut..."
    "I looked over to her point A... which she completely left unguarded!"
    MCT "She was so busy reinforcing point B to stop me from taking it back that she must have forgot!"
    menu:
        "Take Point A":
            jump AE040_c1_1
        "Attack Point B":
            jump AE040_c1_2

label AE040_c1_1:
    show AE neutral
    AE "Uncloaking unit, rolling for initiative."
    "Then, from nowhere, she placed a massive tank right on top of the point."
    MC "Wait, a tank?! How did you cloak a tank?!"
    AE "Commander ability."
    MC "But-!"
    AE "Commander Dogma has the ability to cloak any and all units."
    MC "O-oh..."
    MCT "DOGMAAAAAA."
    stop music
    "In a loud and thunderous din, my soldiers were blown away by a cavalcade of Order tanks."
    "I lost."
    jump AE040_c1_after

label AE040_c1_2:
    MCT "I... no... no, this is definitely a trap."
    "I looked over the board. With only my measly five points, I was caught between dying in a trap, and dying head on in a confrontation to retake point B..."
    show AE neutral
    AE "Well, Hotsure-san? Your move?"
    MC "...I'm not goin down... like a punk."
    "I turned my soldiers around, and charged toward point B, a fire ignited in my heart as I felt the Empresses strength."
    MC "Rolling a d6 to throw plasma grenade!"
    MCT "AAAAAAAAHHHHH"
    AE "..."
    MC "..."
    stop music
    AE "One. You cooked it too long and it exploded in your hand."
    "I placed my elbows on the table and rested my head in my hands."
    AE "Roll for collateral."
    "I limply picked up the dice and let it drop from my hand."
    show AE happy
    AE "One... t-total squad annihilation."
    "Shiori-chan was nearly on the verge of laughing her bulbous ass off."
    MC "Can I roll to reclaim some dignity?"
    AE "Pffft... *khm*, s-sure..."
    "One."
    AE "O-oh God!"
    "Shiori-chan hid her face with a hand and did her best to restrain her laughter. My head slipped from my hands as I let it bump against the table."
    jump AE040_c1_after

label AE040_c1_after:
    play music Hallway
    show AE neutral
    AE "Well, Hotsure-san, that's that."
    MC "I... I put up a good fight though. Right to the-"
    AE "No, it was pretty pathetic. Half of your squad even retreated off of the board when you lost the other half of your unit."
    MC "Yeah, yeah, I get it... but next time, though!"
    MCT "Will probably end up like this time, to be honest."
    AE "Hmph... I look forward to our next game then."
    show AE happy
    AE "Until then, come. I still have other appointments at the school."
    "The day was lost... but I made a vow. For my sense of pride, and my desires as a man."
    "I WILL win a game of Warblade against Shiori-chan. Those panties are MINE."
    jump daymenu

label AE041:
    $setProgress("AE", "AE042")
    scene Classroom with fade
    #SCENE AFTERNOON
    play sound ClockTower
    "As the bell rang out Shiori-chan concluded the class with a respectful bow to the teacher, however, I didn't take the leisure of looking up, as my mind was focused elsewhere."
    MCT "Today's the day... It's almost time."
    play music Rain
    if getAffection("FMG") > 0:
        show AE neutral at Position(xpos=.25, xanchor=0.5, yalign=1.0) with dissolve
        AE "..."
        show FMG happy at Position(xpos=.75, xanchor=0.5, yalign=1.0) with dissolve
        FMG "Woah, someone's pumped up! Catch me in the gym later. We can hit a few reps, 'kay?"
    else:
        show AE neutral with dissolve
        AE "..."
    "I grabbed my things and began to walk out of the room, planning on waiting for Shiori-chan to leave after me."
    scene Hallway with fade
    "I got halfway out of the door when..."
    show AE neutral with dissolve
    AE "Hotsure-san, I need to talk to you for a moment."
    "From behind, Shiori-chan gently put her hand on my shoulder and took me off to the side once I left the room."
    AE "You seemed distracted in class today. Is my skirt riding up again? Is everything alright?"
    MC "Wanna go again?"
    "She seemed slightly taken aback at first, but then gave a cautious look."
    AE "Again? You'll need to give reference to... what is it you're talking about?"
    MC "Warblade. You and me. Let's go."
    show AE surprised
    AE "Oh! Ooohhh, um... are you sure?"
    MC "Y-Yeah. I want a round two."
    AE "...You remember last time, corre-?"
    MC "I remember last time! But *this* time is what's important!"
    MC "So... what do you say?"
    show AE neutral
    AE "Hmm..."
    MCT "Come oooonnn. Come oooonnn!"
    AE "Very well. I don't have a meeting until much later, so I suppose I can play a quick game with you."
    MC "Yes!"
    AE "But Hotsure-san, I can see that you have a heightened resolve for victory."
    show AE neutral-annoyed
    AE "I plan on testing that resolve."
    MC "Understood."
    stop music
    
    scene Town with fade
    "We exited the school, went through the valley, and made our way to the commercial district. The closer I got, the more amped I became."
    "After spending all night reading up on the rules and watching games online, I'd become more motivated than ever to win. My soul felt like it was on fire as I experienced a surge of energy like I never had before."

    scene Game Store with fade
    #RING SFX
    show AE neutral with dissolve
    Owner "Welcome!"
    MCT "This may have started because I wanted to get a hold of Shiori-chan's panties, but now it's about pride."
    MCT "I can't just let her see me as a failure, and I refuse to let myself put all the work I put into learning how to play well go to waste."
    "We made our way to the back, and Shiori-chan began to put all the gamepieces in place."
    AE "So, are you ready to play?"
    MC "Yeah, let's do this!"
    "I began to plan out my first moves, and looked down at the spell cards I had on hand."
    MCT "This time..."
    MC "I WILL WIN!!"
    play music Tension
    scene black with fade
    #DICEROLL SFX
    pause 2
    scene Game Store with fade
    show AE neutral with dissolve
    "The game had been well under way for around fifteen or so minutes, and soldiers began to pile up on the side of the table; the dead zone."
    "However, something had changed."
    "Last time around this point, I was doing extremely poorly."
    "But this time..."
    AE "Psychic Field Implosion passes. Your tank is destroyed."
    "This time, I'm getting absolutely decimated."
    MC "Ghk-nngh!"
    "I took my plastic tank, and flipped it upside down."
    MC "Y-Yeah, well, your soldiers are still out in the open!"
    AE "No they're not."
    #DICE ROLL SFX
    "She then took her miniatures and had them huddle behind the tank, obscuring their view completely."
    AE "Destroyed vehicles and giant units count as cover."
    MC "P-Page twenty four, rule three hundred and eighty nine, right."
    MCT "Damnit! Another amazing play."
    MCT "This is bad. Her tank is aimed right at my captain."
    MCT "It's my turn, but there's nothing I can do. My plan was to bombard her units before they got too close, but she has a tank active and her knights hiding behind my ruined tank. After this turn, she'll attack my footsoldiers."
    AE "Hotsure-san, as a friendly gesture, your best move is to hide behind cove-"
    MC "I-I know! Way ahead of you."
    show AE neutral-annoyed
    AE "...Make sure you're obscured, hm?"
    MCT "It's best to retreat when I have the chance."
    "Rolling for movement, I took my commander and his bodyguard and moved them behind a grey painted brick wall, windows broken out and rocks covering the sides to prevent flanking."
    MC "Your turn."
    "Shiori-chan let out a disappointed sigh and picked up her dice."
    MCT "Okay, as long as I'm behind cover-"
    show AE neutral
    AE "Attacking the commander with a tank, rolling for-"
    MC "W-wait, what?"
    AE "I'm attacking your commander, I have to roll for damage."
    MC "Wha-But I thought you said I could hide behind cover!"
    AE "I said you need to be completely obscured for cover to work. There's a window I can see your commander through, so you're not in cover."
    MC "Wait, wait, okay, how can a tank accurately shoot through a window?!"
    #DICE ROLL SFX
    show AE neutral-smug
    AE "By rolling a five."
    MC "...This is gonna be a long afternoon, isn't it."
    show AE neutral
    AE "Probably not, no."
    "The next 30 minutes were spent getting completely destroyed by Order tanks."
    scene black with fade
    #DICE SFX
    pause 2
    scene Game Store with fade
    show AE neutral with dissolve
    "Finally."
    "Finally after a hellish time of pure decimation, I got my chance."
    "She moved her soldiers to retreat between the plastic trees and rocks. As she did, she walked through a painted brown patch, mud, which slows your troops as they walk through it."
    MCT "This is just the opportunity I needed. My force is large enough to be able to take her scouts down and take point A. Should I go in?"
    menu:
        "Push forward":
            jump AE041_c1_1
        "Fall back":
            jump AE041_c1_2

label AE041_c1_1:
    MCT "Without a doubt. If I just fall back like a coward over and over, then there'd never be any progress."
    MCT "No, even if I backed down, that's probably what she's gambling on."
    MC "Rolling to move in on enemy units."
    #DICE ROLL SFX
    MC "Pass."
    AE "Sending reserve reinforcements, rolling to pass."
    AE "Pass."
    MCT "Yes! She's panicking and sending out her spare soldiers already! I have her right where I-"
    "Just then, she placed two squads of soldiers on the left and right flank of my army in the valley. She turned her retreating army around, guns pointed directly at me."
    MC "..."
    AE "Rolling to attack."
    #DICE ROLL SFX
    stop music
    AE "...I think we can safely call it game here."
    MCT "Everyone... every single one of my soldiers were destroyed."
    jump AE041_c1_after

label AE041_c1_2:
    MCT "No... No, she has something planned. This is the hidden tank tactic all over again. I know how she plays, she loves to trap people. Both her General and her Hero character are on low health."
    "I turned my army around, and returned to my point B."
    MCT "I'll kill them, and scatter her armies."
    MC "Rolling to attack Commander."
    AE "..."
    MCT "YES! A Six!"
    MC "Hit. Applying 'Poison of the Void' for extra damage."
    MCT "Yeah, that should be enough. That stacks up to three hits, more than enou-"
    AE "'Be Careful my Good Man'. Four or more."
    MC "..."
    MCT "Damnit. I forgot. The rule that lets a nearby soldier protect a leader."
    AE "Rolling three. Casting 'Boon of the Empire' to add one. It passes."
    MC "Oka-"
    AE "Character affect active. Upon dying, allows secondary reserves to be played on the right side of the field."
    MCT "Secondary... reserves?"
    "Suddenly, a cavalcade of armored knights on motorcycles came from the void and charged towards point C, my only territory, from out of nowhere."
    MC "Wait... wait, wait, wait, wait!"
    "She took her motorcade and slowly moved them onto point C, capturing it by having more units on the point than my defending force could attack."
    stop music
    MC "Wait, wait please! Please wait! Oh god!"
    AE "Aaand that's game."
    jump AE041_c1_after

label AE041_c1_after:
    play music Hallway
    "I hung my head in defeat. The fire I went in with had been blown away by the icy chill of her calculating tactics."
    show AE sad
    AE "Um... good game."
    MC "..."
    show AE neutral
    AE "Um, sir? We'll be cleaning up now!"
    "I slowly helped her put everything away, and after giving a nod to the shopkeep, the two of us walked back towards the school."
    
    scene Hill Road with fade
    show AE neutral with dissolve
    AE "H-Hey, don't worry about it. Tell you what, when we get back, we can go and read together before I go to my meeting. I found a really good book about-"
    "I'd been completely tuning her out. The sheer feeling of despair washed over me and wouldn't set me free."
    MCT "What's even the point? She outclasses me in this game in every respect."
    MCT "When she doesn't have an amazing tactic up her sleeve, she uses sheer luck from the dice rolls to lead her to victory! And when her dice rolls aren't enough, she uses Boon of the Empire to add one to her dice."
    MCT "I should just give up..."
    MCT "..."
    MCT "I should... give up?"
    "I almost stopped in place as we walked."
    AE "Hm? Everything alright Hotsure-san?"
    MC "I want to play again."
    show AE surprised
    AE "Eh?!"
    MCT "I've done it."
    MCT "I've won."
    jump daymenu

label AE042:
    $setProgress("AE", "AE043")
    #SCENE AFTERNOON
    scene Game Store with fade
    #STORE BELL SFX
    play music Tension
    "We entered the store to complete silence, a testament to the momentus game we were abo-"
    Owner "Welcome!~"
    "..."
    "We entered the store to a warm welcome from the shopkeep, whom Shiori-chan nodded to and asked about the news on the newest campaign box set coming out."
    "After a few minutes of standing in silence as they talked, doing little other than looking around and hopping on my toes, Shiori-chan led me back to the table so that we could begin another game."
    show AE sad with dissolve #worried
    AE "Hotsure-san, I must say, you're pretty antsy today."
    MC "Yep."
    show AE neutral
    AE "..."
    MC "..."
    AE "Any particular reason why?"
    MC "Cause I'm gonna win."
    AE "..."
    AE "Well then, I suppose if you were to do it, now would be the time. Meetings are going to start earlier in two days so-"
    "While I usually try to absorb whatever it is she says into memory, now I was completely tuning her out. Adrenaline was coursing through my veins as victory wafted to my nose, close enough to almost smell it."
    show AE surprised
    AE "Oh, um, Shopkeep?"
    Owner "Hm?"
    show AE happy
    AE "Is that a new brand of air freshener? I think I use the same one at home."
    MCT "Huh... I was wondering why victory smells like apples."
    show AE neutral
    "I placed my soldiers at my end of the table, and after a coinflip, I was decided to roll first."
    MC "Rolling to move scouts."
    #Dice roll sfx
    MC "Two threes, one five. Moving 12 inches."
    "I moved all my scouts along the edge of the left side of the table into the mud, effectively creating a mud trap, keeping them in place."
    MC "Okay, your turn."
    AE "..."
    AE "Are you sure that's where you want to move your scouts?"
    MC "Yeah."
    AE "Further into your own territory?"
    MC "Yep."
    show AE neutral-annoyed
    AE "..."
    show AE neutral
    AE "Rolling to move motorcade."
    "I watched in silence as Shiori-chan systematically began to send out waves of units from both two directions, cutting off access to her side of the board early."
    AE "Well. This should be fairly quick."

    scene black with fade
    pause 1
    scene Game Store with fade
    show AE neutral with dissolve
    AE "Your turn."
    "She'd already moved in towards C, but had yet to attack any of my soldiers."
    MC "Got it."
    "Nodding, I rolled a single dice and sent forward my leader. Once he was behind cover, I turned him around and-"
    MC "Uncloaking unit."
    show AE surprised
    AE "...Wuh..."
    show AE neutral-annoyed
    AE "Hotsure-san, I'd like to remind you that you can only use a character ability once per game."
    MC "I know."
    show AE neutral
    AE "..."
    MC "..."
    "Though subtle, I could tell that she was trying to hide the fact that she was taken off guard by my actions and response. Shaking her head, she rolled to attack the lone soldier, who was gunned down effortlessly."
    AE "..."
    AE "Not quite sure what you expected..."
    scene black with fade
    pause 1
    scene Game Store with fade
    show AE neutral with dissolve
    "Shiori-chan advanced forward, her army making quick work of some of my smaller units. She had her General-Commander combo following the lead, but they were right in the line of sight of one of my snipers."
    MC "Attacking general."
    AE "'Be Careful, My Good Man.' Four or more."
    #DICE SFX
    AE "Roll passes. Character effect active, deploying reserves from..."
    AE "Hm?"
    show AE neutral-annoyed
    AE "...I see. Well, you're clever, I'll give you that. Taking advantage of spacing rules to stop my deployment."
    MC "Oh, wait, is that what I did?"
    show AE neutral
    AE "..."
    AE "Yes. Yes you did."
    MC "Alright, cool."
    show AE neutral-annoyed
    AE "..."

    scene black with fade
    pause 1
    scene Game Store with fade
    show AE neutral with dissolve
    "One hour in. Neither of us had made substantial progress, and the lack of total domination was getting to Shiori-chan."
    "In what appeared to be a tactically complex strategy, she had amassed a massive force around point B. With point A being guarded sparsely."
    AE "Alright, Hotsure-san. You've so far blocked my soldiers, attempted to trip me up by sacrificing your leader ability, sending your own helicopter into play and then subsequently taking it out."
    show AE neutral-annoyed
    AE "But your bluffs are mostly nothing more than an annoyance. As it stands, I've finally built up enough power to cast 'Psychic Field Implosion'."
    show AE neutral
    AE "This attack will allow me to create a strike of pure magic at any part on the board, and will-"
    MC "You don't gotta explain it. I've read the rules."
    show AE neutral-annoyed
    AE "...May the void take you."
    "She picked up her dice, ten in both hands..."
    show AE neutral
    AE "Casting 'Psychic Field Implosion'."
    "And cast them."
    #Dice roll sfx
    AE "One-two-three-four-five-six..."
    show AE surprised
    AE "..."
    show AE neutral-annoyed
    AE "Critical backfire."
    show AE angry
    AE "R-Rolling for damage."
    #Dice roll sfx
    show AE surprised
    AE "...Max damage."
    "Her eyes darted from miniature to miniature, and then slowly, she started taking them off the board."
    MC "Hey, Shiori-chan?"
    show AE neutral-annoyed
    AE "...Hm?"
    MC "Why did you place all of your units in one spot?"
    show AE angry
    AE "Because that's how you're supposed to play the game."
    MC "Naturally."

    scene black with fade
    pause 1
    scene Game Store with fade
    show AE neutral-annoyed with dissolve
    stop music
    AE "Haaahn..."
    AE "Alright. It looks like we only have a few turns until the game ends."
    MC "Looks like it."
    show AE neutral
    AE "Hmm..."
    show AE happy
    AE "I think I'm gonna call it."
    AE "I concede, you win."
    MC "Eh, whatever."
    play music Schoolday
    MC "W-Wait, what?"
    show AE neutral
    AE "I concede. It's improbable that I'll be able to make a comeback with the troops I have left."
    show AE happy
    AE "You win."
    MC "A... Ah..."
    MC "WOO-!"
    show AE angry
    AE "There are customers in the front."
    MC "...."
    MC "{i}woooo{/i}"
    show AE neutral
    AE "Good."
    show AE happy
    AE "I must say, Hotsure-san, I admire your prudence. You had your mind on the game the whole time, and-"
    MC "Eh? Oh. Not really. In fact, I felt kind of tired, so I kept blacking out every few minutes or so."
    show AE surprised
    AE "...Huh?"
    MC "Yeah, I wasn't really trying."
    show AE neutral-annoyed
    AE "Pride is the bane of many, Hotsure-san. Just because you won-"
    MC "No, really, I didn't try."
    show AE surprised
    AE "Eh?"
    MC "You planned for everything. Read my every action, every single step of the way. How could I stop that?"
    MC "Not planning at all. Every move was random, every outcome based on sheer luck from the dice rolls. Really, I only won because your general destroyed himself."
    AE "But... what about that ingenious play stopping my reserve-?"
    MC "Not planned at all. I'm being honest, I put zero effort or strategy into the game."
    MC "You can never fail if you never try."
    "Shiori-chan put a finger up and knitted her brow as if to lecture me, her mouth agape, but no words came out. She pursed her lips, and brought her finger back down, exhaling through her nose."
    AE "I'm... not sure if I should be disgusted by your philosophy, or impressed by your unorthodox thinking."
    MC "Impressed by my thinking, you say?"
    show AE neutral-annoyed
    AE "No... No, I think I'll settle with being disgusted at both."
    show AE happy
    AE "But you won, and that's not something I can't take from you."
    MC "So, ready to head back?"
    AE "...Yeah. Let's head back to the dorms."
    
    scene black with fade
    "We walked back to the school, and as we did, Shiori-chan made sure to keep me close. Call it a hunch, but I feel as if that victory may have made us closer... somehow?"
    scene Dorm Exterior with fade
    "We got to the dorms just in time, the sun nearly sunk into the horizon, orange light shining through the windows in the hall. We stopped just short of Shiori-chan's door, and the anticipation finally kicked in."
    MC "Sooo, Shiori-chan?"
    show AE neutral with dissolve
    AE "Hm?"
    MC "Seeing as how I woooon~"
    show AE surprised
    AE "Nngh!"
    "Her reaction actually made me feel kind of bad. She was the one that offered, and yet here I was, feeling as though I was taking advantage of her."
    MCT "Man... this isn't right. I oughta just play it off as a joke."
    MC "Hey, don't wo-"
    show AE neutral-annoyed
    AE "Very well... you deserve it."
    MC "Eh?"
    "Shiori-chan let out a sigh as her hands traveled down towards her hips, her skirt crinkling as her hands sunk into her flesh. The sight made me lose all sense of decency that was there previously, and I found myself in vitriolic anticipation once more."
    MCT "Wait, she's doing it here?! In public?! What if someone comes an-"
    show AE neutral
    AE "Hotsure-san..."
    "Her hands stopped, and rather than pulling her skirt down, she merely rested her hands on her sides. At least as well as her hips would allow."
    show AE sad
    AE "I... was wrong. You're a great Warblade player."
    MC "...Eh?"
    "To compound to my confusion, Yureno-chan bounded out of the room and between the two of us, grappling me in a bear hug."
    show AE sad at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show Tako neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    #show Tako happy at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    Tako "YOU WON?!"
    Tako "AHAHAHAH! NO WAY!"
    show AE neutral-annoyed
    AE "Y-Yureno-san, keep your voice down! We're in the halls and-"
    Tako "She was soooo confident you'd lose too! Bragged about how there was no way you'd win!"
    Tako "What was it you said again?"
    "Mockingly, Yureno-san placed a hand on her hip and pushed up a pair of invisible glasses."
    Tako "'If I were a betting woman, I wouldn't fear betting my own panties against Hotsure-san in Warblade!'"
    Tako "KYAHAHAHAHA!"
    show AE angry
    AE "Tch!"
    MC "A-aa..."
    show AE sad
    AE "I'm so sorry. I should have never spoken ill of your skills, no matter how much Yureno-san prodded me."
    "A pit slowly began to form in my stomach. I wasn't even concerned about a 'prize' or anything, I just felt cheated. I got played by Yureno-chan in a real life strategy game."
    Tako "Oy, oy! Let's not forget the big factor here!"
    Tako "Fork over those panties, girl! "
    show AE neutral-annoyed
    AE "..."
    show AE neutral
    AE "Yureno-san..."
    AE "The key words were 'IF I were a betting woman.'."
    show AE happy
    AE "I'm not. There was neither a spoken or written agreement that I would give you anything."
    #show Tako neutral
    Tako "...Eh?"
    show AE angry
    AE "And just to let you know... soliciting a student representative for their undergarments is a serious violation of school policy."
    #show Tako sad
    Tako "H-hey, hey, take it easy! I... I was just gonna... um... sell 'em! Turn a buck! It wasn't anything sexual-"
    AE "You were going to SELL my panties?"
    Tako "A-ah..."
    "Shiori-chan turned to me in a huff, and gave a sincere and honest look."
    show AE sad
    AE "I... want to apologize. I was playing so aggressively because of my own pride. It was foolish and careless."
    show AE happy
    AE "Hotsure-san... playing games with you was really fun. I really hope we can do it again sometime."
    "I let out a sigh, and gave a thumbs up with a smile."
    MC "Yeah. I'd like that."
    MCT "Despite the circumstances of our game, I'd be lying if I said it wasn't fun. And hey, now that I know how to be good at Warblade, maybe we can play again sometime."
    show AE angry
    AE "If you don't mind, I have school business to attend to."
    MC "I understand completely."
    Tako "H-hey. K-Kei, my dude, my m-man, help me out here."
    MC "Sorry. You rolled all ones here."
    Tako "W-wait!"
    hide AE with dissolve
    hide Tako with dissolve
    "The door slowly shut as Shiori-chan pulled the girl into the room. I walked away from the door, faintly listening to the sounds of bickering as a smile crossed my face."
    MCT "Good game."
    jump daymenu

label AE043:
    $setProgress("AE", "AE044")
    #SCENE AFTERNOON
    scene Town with fade
    play music Rain
    "As we walked through town, the bright afternoon sun shone only in short rays as silver clouds rolled in and filled the air with the rain's fragrance."
    #RAIN SFX
    show AE neutral with dissolve
    "Shiori-chan, ever vigilant of the weather, had brought her umbrella along in anticipation, a large school-regulated tent of a thing. A side effect of her giant umbrella being able to cover her front to back, however, was that it could me alongside her, as I'd forgotten mine."
    "I didn't mind, however. It simply meant I needed to huddle close to her... although her swinging hips made it a bit hard."
    MC "Well, so much for a walk in the park, eh?"
    AE "Unfortunately."
    MC "Tch, just our luck for it to start raining the minute we hit the town."
    AE "No luck involved. After all, wasn't it you who said it would 'be fine'?"
    MC "Gch!"
    MC "A-And I'm right! So what if we have a light drizzle, let's go for that walk anyway!"
    "Giving a confident smile, I grabbed onto Shiori-chan's umbrella, and then her hand."
    show AE surprised
    AE "Now hold on, I don't think it's a good idea for you to-"
    MC "Come on, let's go-!"
    #THUNDER SFX
    "I took only three steps forward before a gust of wind caught the underside of the umbrella, lifting it up into the air, and me for what felt for a split second."
    MC "Nngh!"
    show AE neutral
    AE "I think the storm's starting to pick up. Here, hand me the umbrella so you don't-"
    "Before she could finish, another gust pulled me back a bit, completely turning and bending the umbrella inside out."
    MC "Eh!?"
    show AE sad
    AE "Y-Yeah, that's what I was worried about."
    "The rain began to fall down with greater intensity, winds whipping droplets against our clothes as we huddled closer together."
    MC "Come on, let's go in here!"
    "I opened the door to the nearest building, holding it for Shiori-chan before entering."

    scene Diner with fade
    MC "Ugch, drenched."
    "Though my jacket saved much of my shirt, my hair had gotten dripping wet in the rain. As Shiori-chan patted her soggy buns to check the moisture, I fought the urge to shake my head out like a dog."
    show AE happy with dissolve
    AE "Well, we're out of the rain for now, at least."
    MC "Man, do you think the w-"
    Waitress "Good afternoon, sir! Table for two?"
    MC "Oh, wh-ummm."
    show AE neutral
    AE "Oh, n-no, ma'am, we're just-"
    MC "Yeah, yeah, booth for two please."
    show AE surprised
    AE "Eh?"
    "Shiori-chan looked to me in confusion, and I responded with a simple shrug."
    MC "Eh, I'm hungry anyway. Let's grab a bite, kill some time."
    show AE embarrassed
    AE "A-Ah... okay."
    "We followed the waitress, who led us to an extra-large booth. She began placing menus down on the two sides as Shiori-chan sat down, heralded by a loud squeak from the booth's leather."
    Waitress "What would you like, sir?"
    MC "Tea'd be nice."
    Waitress "And you, ma'am?"
    show AE neutral
    AE "Coffee, please. Black."
    Waitress "Can do!"
    MC "Huh. Didn't take you for a black coffee kind of girl."
    show AE happy
    AE "Oh? What makes a black coffee girl, then?"
    MC "Um... well, I guess most girls don't seem like the black coffee type. Usually black coffee is enjoyed by office workers and really serious people..."
    MC "Actually, never mind, you fit a black coffee drinker exactly."
    show AE embarrassed
    AE "I mean... I'd debate you, but seeing as how I ordered the coffee..."
    MC "Exactly."
    show AE neutral
    AE "Did you...?"
    MC "Hm?"
    show AE surprised
    AE "Did you plan this? The fact that we ended up here?"
    MC "..."
    "A coy smile crossed my face, and I held my hands up in defeat."
    MC "Ya got me. What can I say, I-"
    show AE neutral
    AE "Ah, so it {i}was{/i} just by chance after all."
    MCT "S-She called my bluff that quick?!"
    show AE happy
    AE "Haaah, what to do with you?"
    #THUNDER SFX
    MC "Geez, it's really coming down out there."
    show AE neutral
    AE "Mhm. Forecast said it was coming in from the east. Should clear up by morning."
    "Shiori-chan fiddled around with the metal arms of the umbrella as she spoke, but apparently the damage was too great, and she relented. Letting out a sigh, she placed it underneath the table."
    show AE sad
    AE "Scrapped. Haaah, well, recycling bin it is."
    MC "If you knew it was gonna be bad, why not just tell me, eh?"
    show AE embarrassed
    AE "W-Well, um..."
    show AE sad
    AE "I suppose I didn't want to ruin the evening. I figured we'd be able to take a stroll and head back before it got too bad."
    MC "Ah... that explains why you seemed antsy when I took a while to get my hair presentable."
    AE "Sorry."
    MC "Aaaah, no big deal. Although if you wanted we could have stayed behind and hung out in my dorm or something."
    show AE neutral-annoyed
    AE "A-Absolutely not!"
    MC "Whaaaat? Why not?"
    show AE embarrassed
    AE "I mean... it's inappropriate, is all."
    MC "Why's that? I've been in yours before."
    show AE neutral
    AE "Well, yes, but only to look around for a moment."
    AE "Although... there is a bit of lenience in the rules for situations where you can be in the girls dorms. Visitation rights and all that, and as long as you're not loitering in the halls..."
    AE "Hm..."
    "Our waitress placed our drinks out in front of us, Shiori-chan's cup giving a pungent, yet pleasant aroma. After nodding to the woman, however, Shiori-chan merely looked out at the rain in silent contemplation."
    Waitress "Anything to eat, sir?"
    MC "Just a pudding and some toast, please."
    Waitress "Mhm, and you ma'am?"
    AE "Oh, nothing for me, thanks."
    Waitress "Okay, I'll be right back!"
    "The droplets made small, low pitter-patters as they hit the windowpane before falling down in clear streaks. Shiori-chan rested her elbow on the table and her head in her hand; looking out at the rain as the steam from her untouched coffee made wisps in the air."
    "Her other hand laid flat on the table, I smiled, and placed my hand on hers. She looked at it, and then to me, and smiled back, her face giving off a warm and gentle radiance."
    show AE happy
    AE "Hmm~"
    "I began to caress the back of her hand with my thumb down to her finger, softly rubbing past her..."
    MCT "Scar?"
    "Though I only recently noticed, on Shiori-chan's right knuckle, was a pale scar running from one side of the finger to the other."
    MC "..."
    show AE neutral
    AE "Something wrong?"
    MC "No, nothing, just didn't know you had a scar there."
    "She looked down at it, and pulled her hand away with an unexpected urgency. She placed her hand into her lap, and covered it with her other."
    AE "Y-Yes. It's a just a childhood scar, is all."
    MC "Looks kinda deep. How'd you get it?"
    AE "It's honestly hard to remember."
    MC "Right, because childhood injury-"
    AE "Precisely."
    MC "Yeah, I get that."
    MCT "Maybe it's because she's always biting her knuckle when she's mad?"
    "Though her initial reaction worried me a bit, she didn't seem worried or upset, so I just left it at that."
    "My plate came shortly after, the pudding wiggling as she placed it down before coming to a stop."
    MC "Thank you!"
    "Taking my spoon, I took a small scoop off the top, and put it into my mouth."
    MC "Mmm~"
    "Strangely enough, I noticed Shiori-chan eyeing my pudding, almost transfixed. She tilted her head to the side, analyzing it."
    "Taking another scoop, I held it out to her."
    MC "Here."
    AE "Hm?"
    MC "Aaa~. Go like this. Aaa~"
    "She stared at it for a moment, before opening her mouth."
    show AE happy
    AE "Aaa~"
    "I fed her the pudding as she blushed, and her eyes lit up."
    AE "Mmm!"
    MC "Good, right?"
    AE "Yeah!"
    MC "Well get one, then!"
    show AE neutral
    AE "Mm, I couldn't, it'd go straight to my thighs."
    MC "Well, doesn't it already?"
    show AE neutral-annoyed
    AE "W-what was that just now?!"
    MC "N-Not like that! I mean, well, who's gonna notice an extra pound, right?"
    "Fully expecting to get my neck snapped, Shiori-chan instead pondered what I said."
    show AE embarrassed
    AE "You have a point, but... I really shouldn't."
    MC "Ah, excuse me, ma'am?"
    Waitress "Hm?"
    MC "One of these for her too?"
    show AE surprised
    AE "Wa-"
    Waitress "Coming right up!"
    show AE embarrassed
    AE "Wah-ach-you!"
    MC "Ehehe~"
    show AE neutral-annoyed
    AE "Hmmhp~!"
    "Shiori-chan blushed and puffed out her cheeks a bit, causing me to audibly giggle at her trying to look cute, which she picked up on and started doing so too, even if it sounded a bit awkward."
    Waitress "Heeeere you go!"
    show AE neutral
    AE "Thank you, ma'am."
    "Going for her spoon in the napkin, she paused noticing the napkin was tilted at an angle. Correcting it, she then unfolded it and took the spoon."
    MCT "Still not used to that. So weird."
    "She looked at the pudding before poking it. As she did, it undulated with a silly grace."
    "Looking at her own leg, then, she looked around a bit before lightly tapping her own thigh with the spoon, responding to the pudding in kind; with silly and graceful wobbling."
    MC "Did you just... compare your leg to the pudding?"
    show AE surprised
    AE "N-no! Don't be foolish."
    MC "Pffff! Ahaha~!"
    AE "H-Hey!"
    show AE neutral-annoyed
    AE "Hrmph."
    "She took a nice spoonful and took a bite. A small smile crossed her face as she savored the flavor, looking out the window... and pausing."
    "Her smile faded, and she took the spoon from her mouth. Her eyes were transfixed on something."
    MC "..."
    "I didn't know what she was looking at at first, but by tracing where her eyes were looking, I saw..."
    "A completely innocuous billboard. Nothing extreme or out of the ordinary. Just a billboard for laundry detergent, a picture of a mother and daughter smiling happily at a dove above some Kanji."
    "{i}Cleans and whitens clothes 60%% better than any other brand!{/i}"
    show AE sad
    AE "..."
    AE "{i}Sssp{/i} Khm."
    "After taking a drink and clearing her throat, her eyes finally broke contact with the sign, and she seemed to relax a bit more."
    MCT "Shiori-chan..."
    show AE neutral
    AE "You know the wea-"
    MC "Is everything o-"
    AE "Oh."
    MC "Oh, uh..."
    MC "Y-You first."
    AE "No, just a comment on the weather patterns here. What were you going to say?"
    MC "Um..."
    MCT "I'm not sure if I should ask her if everything is alright all at once. I better ease into the conversation."
    MC "Is everything okay school wise? Like, how are classes going?"
    AE "Perfectly fine, Hotsure-san. I haven't been wrong on any of my work yet."
    MC "Yeah? How about around the office?"
    AE "I find the sign odd, if that's what you want to talk about."
    MC "Huh?"
    MCT "Straight to business. I guess I should expect that from her."
    MC "Uh... no, no, I don't think so?"
    AE "Why a dove? Why only the mother and daughter? It's..."
    AE "Just a weird sign, is all."
    MC "I think it's cute."
    AE "I suppose... but why's the mother have so much bearing over the daughter in the picture."
    show AE neutral-annoyed
    AE "Look, look, she's practically looming over her. Should she be that close?"
    MC "Well, yeah, that's what parents do, right? They kinda just shadow over their kids."
    show AE sad
    AE "..."
    MC "I mean, I guess."
    show AE neutral
    AE "...Mm. {i}Sssp{/i}"
    "We spent some more time at the diner, and thankfully the mood started to lighten up. By the time we were both done, drinks and all, we were nearly two hours from sundown."
    Waitress "Aaall right! Here's your check, sir."
    MC "Ah, thank you."
    "I pulled out my wallet, and began to flip through the bills I had on hand as Shiori-chan looked on."
    show AE sad
    AE "...Are you truly sure that you don't want me to help pay?"
    MC "Yeah, it's all good."
    AE "I do feel awful about you paying for our dates, Hotsure-san. If there is anything at all I could do, I wouldn't hesitate."
    MC "Hey, hey, like I said, it's all good. You don't need to, like... worry about money stuff, all right?"
    AE "See, you say that but..."
    show AE happy
    AE "Haaah, never mind. Thank you very much."
    MCT "Hm... I don't know why having people pay for stuff for her gets to her... still, though, it would suck of me to stick her with the bill."
    "We paid, and Shiori-chan grabbed the broken umbrella. As we headed for the door, I pulled her in a bit closer to me. Wrapping my arm around her, she smiled warmly and moved a bit closer in."
    show AE neutral
    AE "Hey, Hotsure-san?"
    MC "Hm?"
    AE "You realize the closest bus stop to the school is at the end of the block, yes?"
    MC "..."
    "I let out an exasperated sigh, and pulled her even closer."
    MC "Hey, how well do you think your skirt would make for an umbrella?"
    show AE happy
    AE "Let's not test that."
    jump daymenu

label AE044:
    $setProgress("AE", "AE045")
#SCENE AFTERNOON
    scene Campus Center with fade
    #BIRD SFX
    "Entering the courtyard, I took a look around for Shiori-chan, who I'd promised to meet with for another afternoon out on the town."
    "There she sat on a stone bench underneath a magnolia blossom, midday light shining from the bright sun in the sky; her burgeoning thighs taking up most of the cold stone seat."
    "Approaching her, she looked up and smiled, tucking her journal into her pocket as she straightened her posture."
    show AE neutral with dissolve
    AE "Hotsure-san, I see you're dressed and ready."
    MC "Of course. Wouldn't want to show up unprepared, right?"
    "She went to sit up, however it seemed as though her legs were a bit weak, and she seemed to have a bit of trouble getting the momentum to lift her behind from the seat."
    show AE angry
    AE "Hmph... rrg-"
    MC "Please, allow me."
    "Holding out my hand, she looked at it with a hint of conflict. Closing her eyes, she nodded and smiled warmly, taking it and allowing me to pull her up."
    show AE happy
    AE "Thank you."
    MC "Getting a bit harder to pick yourself up?"
    show AE sad
    AE "No, no, this happens at the tail end of every cycle."
    MC "Cycle?"
    AE "Mhm. I've noticed that as I've grown, my body slowly adapts to my growing derriere. My leg muscles grow stronger to support it, but it sometimes lags behind."
    MC "Right, yeah."
    MCT "Man, at times I can't believe how complex her growth is. Sometimes she's outpacing me easily in a jog, other times she's struggling to lift her ass from where she sits."
    MC "Anyways, you don't look to bad yourself."
    show AE neutral
    AE "Feh. I'm no different than I am any other day."
    MC "No, it's more than just your outfit, you just seem a bit more... radiant than usual, I guess."
    show AE embarrassed
    AE "R-Radiant, you say?"
    "Her pink blush elicited a chuckle from me as I walked over and grabbed her hand."
    MC "C'mon, let's head out. We can go for that walk, okay?"
    show AE neutral
    AE "Mm."
    
    scene black with fade
    "Once more through the windy valley, we made our way to the town."
    scene Park with fade
    MC "Hmm... chapter five."
    show AE neutral with dissolve
    AE "'There are three courses in which to hold a principality which lived under their own laws: ruin them, reside there in person, or permit them to live under their laws with tribute.'"
    MC "Geez, Shiori-chan, that's seven random chapters you were able to remember off of the top of your head. Do you just remember every book you've read?"
    show AE happy
    AE "Many of them, yes. Although I really just try and gather the most important bits."
    MC "Yeah, that and you seem to fancy a lot of western books, huh?"
    AE "I suppose that's one way to put it, yes. Though you surprised me with how well you knew The Prince. I never took you as a Machiavelli type of man."
    if getSkill("Academics") > 7 and getSkill("Art") > 7:
        MC "Mhm, I used to research him a lot. Thought his stuff was pretty interesting, though it was hard to find a translated copy."
        $setAffection("AE", 4)
        AE "Hmm~ It's been so long since I've had anyone to talk to about things like this. Honestly, you make me feel just so... open when I'm around you."
        "I smiled and pulled her in close to me. Though her soft, plush derriere rubbed against my leg, she didn't show a single bit of hesitation to my advance."
    else:
        MC "Never heard of the guy. I don't even think I know how to pronounce that."
        show AE surprised
        AE "Hm? Then how were you able to tell me if I was correct for each chapter."
        MC "I just assumed you were."
        AE "Wha-You!"
        MC "Eheheh"
        "Shiori-chan smiled playfully as she hip-checked me off to the side a bit. Though I had to pause to catch my footing, I didn't mind the view as I caught up to her."
        "Whether it was because of her smiling face or the exposed flesh popping out of a small rip in her skirt, I couldn't tell."

    scene Town with fade
    "As we made our way out of the park, we had just the right sight awaiting us."
    MC "Ah, there we go! I knew I smelled something good."
    show AE happy with dissolve
    MC "Oi, Shiori-chan! Want some Takoyaki?"
    AE "Oh, are you getting some? If so, then I'll have some too, if you wouldn't mind."
    MC "Alright then, two orders, sir."
    Vendor "Just made a fresh batch."
    "Placing the money on the counter, I looked over at Shiori-chan and smiled, and she did so in kind. Her eyes glimmered brighter than the lenses of her glasses as she rubbed one arm and shrunk back bashfully."
    Vendor "Here you go! One for you and the lady."
    MC "Ah, thanks."
    "I handed Shiori-chan hers and grabbed mine as we walked away. Grabbing the chopsticks, I bit in-"
    MC "Ach! Still hot! Still hot!"
    "Batter dripped down my chin as I breathed cool air and fanned my mouth. Not wanting to spit out food in front of my company, I swallowed the whole thing."
    MC "Ahp, ah, S-Shorry. *Gulp*"
    show AE happy
    AE "Oh, I don't mind at all. I like watching you eat. It's cute."
    MC "Me eating is cute?"
    AE "Yeah."
    AE "Although."
    "Taking her napkin, she lightly dabbed my mouth and chin."
    AE "You're much more cute when I can see your face."
    MC "Eheh, sorry."
    "We walked along the sidewalk with takoyaki in hand, Shiori-chan looking over at my face and smiling rather than eating herself."
    show AE neutral
    AE "..."
    show AE sad
    AE "..."
    "Her smile dropped slowly and her brow furrowed  as she looked past me, clearly disheartened by something."
    MCT "Huh?"
    "{i}Cleans and whitens clothes 60%% better than any other brand!{/i}"
    MCT "Ah, that billboard again."
    MC "Hey, Shiori-chan?"
    AE "Hm?"
    MC "Billboard again?"
    AE "..."
    "She only looked down and shook her head."
    AE "No, it's nothing, I-"
    MC "Well, I doubt it's nothing when you react like that."
    "Letting go of her hand, I walked over to a nearby bench and patted the seat next to me."
    MC "C'mon. Let doc Keisuke help you out."
    AE "N-No, that's fine, I wouldn't want to burden-"
    MC "No burden at all. I wanna be open with you, and part of that is learning what's up with that sign."
    AE "...Alright."
    "She walked over and turned around, her butt making an audible *flumph* sound as she squeezed in."
    MC "So, the billboard. What's the deal?"
    AE "I'm just... I'm just thinking about how to interpret it."
    MC "How to interpret...? Well, I mean, I interpret that it whitens clothes 60%% better than any other brand."
    show AE neutral
    AE "Well, directly, yes. But... I just get this weird feeling that it represents something... important to me personally. At least I feel that it does."
    show AE sad
    AE "Ugh, I sound like a psychopath."
    MC "No, no, it's fine. It's just... what {i}does{/i} it represent to you?"
    show AE neutral
    AE "Purity, I suppose."
    MC "Purity?"
    AE "Mm."
    MC "Huh... why purity?"
    AE "Well, I think it's pretty obvious from the product sold. The white dove represents purity as it's meant to be spotless."
    MC "Well yeah, but the dove could also be, like, peace."
    AE "Peace?"
    MC "Yeah, at least that's what the rest of the billboard signals. The dove means peace and all that."
    AE "I think the billboard portrays the idea of purity perfectly. A mother and daughter, happy together, looking at a symbol of something pure while advertising detergent."
    AE "It's a state of natural purity."
    MC "I mean, if you wanna look at it like that... but that kind of implies perfection right?"
    AE "Well, no, that wouldn't-"
    MC "I get it, it's nice imagery and all, but at the end of the day you can't really expect perfection like that."
    "As I spoke, I failed to notice Shiori-chan seeming to get more and more riled up and aggravated."
    MC "It's just not realistic."
    show AE neutral-annoyed
    AE "How so?"
    MC "I dunno. I guess it's just that 'purity' doesn't exist."
    show AE angry
    AE "Of course it does."
    AE "If there were no purity, how could there be stains? If there's a fallen angel, there must be a heaven from which the angel fell."
    AE "And there {i}is{/i} a hell for the angel that falls. I've seen it."
    MC "..."
    AE "..."
    MC "What... what was that, just now?"
    show AE neutral-annoyed
    AE "..."
    MC "Shiori-chan... what are you saying?"
    show AE neutral
    AE "..."
    show AE sad
    AE "Oh... Oh my god, I didn't-"
    MC "That was-"
    AE "Creepy, yeah."
    MC "No, I mean, it wasn't creepy, just... I dunno what to say."
    AE "..."
    MC "..."
    MC "Hey, uh, are you okay? You haven't touched your octopus balls."
    show AE neutral
    AE "Oh, um... I'm not particularly hungry."
    MC "Oh."
    show AE sad
    AE "..."
    MC "..."
    "Wanting to save them for later, Shiori-chan silently placed her napkin over her box."
    AE "I hope you don't mind, Hotsure-san, but can we go back to the school after you're finished?"
    MC "You want to go home? Did I-"
    AE "I-It's nothing you did, I'm just not feeling..."
    AE "*Khm*"
    MC "O-okay."
    
    scene black with fade
    "Helping her up, the two of us walked out of town and back to the school. Not a single word spoken between the two of us."
    scene Dorm Exterior with fade
    show AE neutral with dissolve
    AE "..."
    MC "..."
    MCT "Shiori-chan..."
    MC "Is everything okay?"
    AE "Hm?"
    MC "Like... with us?"
    show AE surprised
    AE "Of course it is!"
    show AE sad
    AE "Hotsure-san, I-I hope I'm not making you feel as though-"
    MC "Don't blame yourself, I'm just... It's just me worrying."
    AE "..."
    AE "Is it about how I've been acting today? With the angel question?"
    MC "No, not at all! You just..."
    MC "...Well... yeah, a little bit. But it's that, and... well, a couple of other things. Like, from time to time you seem a little..."
    AE "Well, Hotsure-san, I'm sorry I'm worrying you. I've just been reminiscing a lot about life experiences."
    MC "Like... what?"
    show AE neutral
    AE "Nothing I wish to talk on now."
    AE "You see I'm not exactly in a position to..."
    AE "A-as you can tell..."
    show AE sad
    AE "A-As, um..."
    "I waited for her to finish what she was saying, but she just stared at the ground. Then, she took in a deep breath and balled up her fists."
    show AE neutral-annoyed
    AE "..."
    show AE angry
    AE "No."
    show AE sad
    AE "No, I don't want this. I don't want to be cryptic and withhold my thoughts from you. I-..."
    AE "I don't want the petty emotional struggles of the past have a stranglehold on what I have with you now."
    MC "The past?"
    show AE angry
    AE "I'm just sick of it. Sick of worrying you. Sick of not being open with you."
    MC "Shiori-chan..."
    show AE sad
    AE "Tomorrow when classes have ended, I want to meet you in the belltower."
    MC "The belltower?"
    show AE neutral
    AE "Yes. It's completely segregated from anyone without clearance to enter. I can give you access."
    show AE sad
    AE "Please, it's important."
    MC "Okay."
    "We walked down the hall to Shiori-chan's room, where she turned around at the door."
    show AE happy
    AE "Thanks again, by the way, for convincing me to go to town with you."
    MC "Eheh, don't mention it."
    show AE neutral
    AE "And Hotsure-san?"
    MC "Hm?"
    show AE sad
    AE "You can be pure without being perfect."
    MC "..."
    show AE embarrassed
    AE "I just... I want you to know that."
    MC "...Yeah. I guess so."
    hide AE with dissolve
    "As she slowly closed the door behind her, I couldn't help but ponder just what was going to happen tomorrow."
    jump daymenu

label AE045:
    $setProgress("AE", "AE046")
    #SCENE AFTERNOON
    scene Campus Center with fade
    "The wind howled and whipped about as I walked through the campus. Classes had ended, none of the student organization members had appeared outside of class, and yet Shiori-chan had yet to talk with me at all today. She avoided eye contact, refused to speak, the whole shebang."
    "To say I was worried was an understatement."
    #CREEEAK
    scene black with fade
    "I opened the ornate door and was greeted with the smell of dust and wood. I looked to the stairs, which seemed to climb up to the heavens. Not wanting to waste any time I began to climb."
    #CLOCK SFX
    "The higher I climbed, the closer the sound of the clock on the tower became. I continued, my steps seemingly blending in with the sound as I climbed. I became a bit shaky after a certain height, almost tripping on a loose wooden stair, but it wasn't long until I reached the belfry."
    #FADE IN BELL TOWER
    scene Clock Tower with fade
    "The room had no lighting apart from the small windows at near the high ceiling, and the light passing through the inverted clock. The light reflected particles of dust, which bounced about softly in the air to the sound of ticking machinery."
    "There, in the center of the room, stood Shiori-chan, who turned around to greet me."
    play music AE
    show AE surprised with dissolve
    AE "Hotsure-san! There you are, I was worried you... come in, come, come."
    MC "Hey, Shiori-chan."
    "My voice sounded distant. Shiori-chan picked up on this and appeared to struggle to hold an uncharacteristically chipper demeanor."
    show AE happy
    AE "Haaah, such a nice day is it not? Perfect temperature, smell of moisture in the air."
    MC "..."
    AE "Mhm~"
    MC "..."
    show AE neutral
    AE "..."
    show AE happy
    AE "I must say, Hotsure-san, this has to be one of my favorite places on campus, a-and the administration gave me access to it whenever I wish as well! Merely ask and I'll bring you here whenever you wish."
    MC "Yeah. Yeah it's, uh... it's nice."
    AE "Mhm~"
    AE "I'm glad I picked it out after classes though, otherwise we'd come out of here deaf!"
    MC "Heh, yeah."
    AE "..."
    AE "Y-you know, I'm quite the avid fan of bells. It's such a breathtaking sound."
    AE "And the machinery! So complex and-and..."
    AE "..."
    "Her smile dropped. Her eyes, dark and soft, spoke volumes about the struggle in her heart."
    show AE sad
    AE "*Khm* ...I suppose pleasantries are out of place here."
    AE "There's no point in trying to ease into the conversation. Let us get right into it, shall we?"
    "Shiori-chan motioned to the ornate wooden bench at the side of the room. I sat down and stared attentively as she let out a sigh."
    AE "Where to begin... well, um... my name is Shiori Matsumoto. I-"
    AE "Ach, no, you know that. This isn't a speech I-"
    MC "I-it's okay, Shiori-chan. I understand you're nervous, just... speak from the heart."
    AE "...Of course. My apologies."
    AE "Hah... well, I was born in a hospital in Chūō. My parents were visiting relatives and, well, I suppose the inclement weather was the second biggest disappointment for my parents that day, heh."
    MC "D-don't say that about yourself."
    AE "Well, perhaps disappointment is too strong a word. I was... you see, my parents conceived me at a very inopportune time in their lives."
    MC "Inopportune?"
    AE "Yes. You see, my mother and father weren't married and were fairly young parents."
    MC "How young?"
    "Shiori-chan froze, as though she hadn't expected a question for that."
    AE "..."
    AE "...My mother was sixteen."
    MC "WHAT?!"
    show AE surprised
    AE "N-now I realize that's rather shocking to hear-"
    MC "How old was your dad?!"
    show AE sad
    AE "...Seventeen."
    MC "Wuh... t-that's insane! That's so young, I mean-"
    AE "My father and grandmother thought so to. There was a bit of a push from father to give me up for adoption after birth, from what my mother said. And my grandmother... wanted to see me off a bit earlier."
    MC "..."
    "Silence. What she implied was a bit too hard for me to respond to, I was at a complete loss for words."
    MC "Your grandmother wanted you..."
    show AE neutral
    AE "Push came to shove and my mother decided against it. Even if it meant her dreams of being an idol were to be put off to the side."
    MC "Idol?"
    show AE happy
    AE "Yes. She was quite the singer. Beautiful, too... anyways, she pushed to see I was kept and raised. My father at the time was jobless, and within a few years got hired as a police officer to look after us."
    MC "...Huh..."
    MCT "An officer? I can see why she'd be driven to legal stuff, then."
    show AE sad
    AE "My mother tried to stay at home for a while, but necessity changed that and she became a convenience store worker."
    MC "She was?"
    show AE neutral
    AE "Mhm. She lacked a proper higher level education, but she made due with what she had."
    show AE sad
    AE "It was around that time, however, that father was fired from the police force."
    MC "Fired?"
    AE "I'm not sure about the full circumstances of it, but... it hit our family hard."
    show AE neutral-annoyed
    AE "And rather than get back on his feet and do something with his life, he decided he wanted to drink his problems away."
    MC "..."
    show AE angry
    AE "Can you believe it? A wife and a child, barely enough money to eat, and he goes out and spends whatever he has on alcohol."
    MC "I guess he had a lot of problems... losing a job can do that to a man when he's down."
    show AE neutral-annoyed
    AE "Ha! If it weren't for the fact that his hair was black, I'd assume he was more shōjō than man."
    MC "That's..."
    show AE angry
    AE "Disrespectful? Good. He doesn't deserve any of my-!"
    show AE neutral-annoyed
    AE "..."
    show AE neutral
    AE "We made a fair enough living up until that point, I suppose. But with father's refusal to work, it all landed on mother."
    show AE sad
    AE "She started working more and more often and I got to see her less and... the effect on me was evident."
    MC "Evident?"
    AE "...I wasn't the best child. I was ratty, scruffy and... well, unruly. I'd often cause incidents at school."
    AE "I tried to fit in with anyone, but... my economic situation was fairly public knowledge."
    AE "It didn't quite endear me with the others."
    MC "I gotta say, I can't see you as a delinquent."
    AE "..."
    AE "A-anyways... it was around fourth grade that... mother broke her spine on the job."
    MC "Her spine!?"
    AE "Yes. First time she went to the doctor since I was born and... well, you can guess where I'm going with this?"
    MC "Did... did she die?"
    AE "...In a way."
    AE "The pain was so severe that she'd... often times lie awake groaning. The doctor prescribed her oxycodone and..."
    "She paused. Looking to the ground, she choked on her own words as they struggled to come out."
    AE "I guess that was that."
    MC "...How was your father in all this?"
    show AE angry
    AE "Drunk. Of course he was. Every time I wanted to spend time with him, he was either drunk or telling me to leave him alone."
    MC "But what about your mother? After the... you know..."
    show AE sad
    AE "I... before the accident she was always so loving and caring. Even with our situation, she'd always find a reason to smile."
    AE "She was always there."
    AE "..."
    AE "She lost her job after the accident... and by that point she'd decided to 'experiment' with new experiences. Painkillers weren't enough anymore."
    MC "W-wait, Shiori-chan, if neither of your parents were working, how did she get the money to-"
    show AE angry
    AE "By surviving the only way a woman in her position {i}CAN{/i}!"
    #CLOCK SFX
    pause 2
    MC "...Oh."
    show AE neutral-annoyed
    AE "..."
    show AE sad
    AE "...I didn't mean to raise my voice."
    MC "N-no, it's okay."
    AE "..."
    AE "And the scary thing is... it could be me in her place. Easily. Anything could be a catalyst for a downward spiral."
    AE "If I let myself become even a bit like her, I'd be trading an office for a brothel."
    MC "H-hey, come on, Shiori-chan, don't be like that. There aren't any brothels in-"
    show AE angry
    AE "Because prostitution is illegal? Against the rules? You know, running in the halls is against the rules too."
    MC "..."
    show AE neutral
    AE "...In any case, as this trend continued, I became more and more self-reliant. I cooked, cleaned, did everything. The only respite for me was... the school."
    show AE happy
    AE "My sanctuary."
    MC "Your old high school?"
    show AE neutral
    AE "Indeed. No-one aside from the teachers liked me. Yet I managed to attain the place of student council president there, too."
    MC "You told me a while ago you didn't really have friends."
    AE "I indeed didn't."
    AE "...Well, at least not of my peers."
    MC "Hm?"
    "Shiori-chan put her hands behind her back and turned from me."
    show AE happy
    AE "My piano teacher... if I ever had a father, I'd say he was the closest."
    "She took off her glasses and held them up in the light."
    AE "He opened my eyes to the truth of the world. Helped me see when I was blind."
    AE "These are his glasses, you know. Rather, he got them for me..."
    AE "I was so thankful. I didn't have much, but I promised I'd pay him back. Told me I'd do it by practicing. When I told him I didn't have the money for a piano... hah..."
    "Slipping them back on and pushing them up, she turned once more to me."
    show AE neutral
    AE "*Khm* I'm uh... I'm getting off track. Where was I?"
    MC "Your school."
    AE "Yes, thank you."
    AE "The students were my burden and my drive. I wanted to make sure... the ones worth working for were given the perfect school they deserved. Even if they along with others would still hate me."
    "She looked up to the metal bells, hanging in the darkness."
    show AE happy
    AE "Like the bells above, their melodious tunes working as a reminder to keep upright and dutiful; I too would be a reminder to do the same. Through my example, others would know when to rest and when to work."
    show AE neutral
    AE "As I went through school, I started noticing that I sat a bit higher. Perhaps due to pride?"
    show AE sad
    AE "Then a bit higher... and a bit higher..."
    AE "Then I got the letter."
    MC "How did your parents feel?"
    show AE angry
    AE "Couldn't give a-!"
    show AE surprised
    AE "..."
    show AE sad
    AE "...*Khm* M-me the time of day. As I left, my mother sitting at the table was the last vision of my home that etched itself into my mind."
    MCT "Mom... before I left, I made sure to give her the tightest hug I could. Promised her I'd do good and look out for sis."
    MC "You didn't say goodbye?"
    show AE angry
    AE "...Not a peep."
    MC "..."
    #CLOCK SFX
    pause 2
    show AE sad
    AE "My mother... I often wonder what the catalyst was. What it was that drove her to her life of debauchery."
    AE "Maybe it was me."
    MC "..."
    "The silence in the room couldn't possibly be described as deafening. Deafening means there's a sensation there in the first place. It was more of that the essence of the room itself was numb."
    "It was hard to find the words to describe my feelings in this moment. I wanted to apologize. With every fiber of my being I did. But what do I say sorry for? I guess I just wanted to portray some level of understanding and empathy; even if through an abstract and unfitting 'sorry'."
    MC "I... I'm sorry, Shiori-chan. If I'd known all this, maybe I would have been more careful about talki-"
    AE "Enough, enough, Hotsure-san. I didn't tell you my upbringing for sympathy's sake."
    AE "I did so... so that you could make your own determinations about me. That you can understand me better. Why I do the things I do."
    AE "I'm sorry... I'm sorry I haven't been forthcoming about myself to you before."
    MC "...I suppose you believe I think less of you? For living in poverty?"
    AE "...It would make sense. I'm just... I wanted to air everything out between us. And knowing me means knowing my shame."
    AE "Hotsure-san..."
    show AE neutral-annoyed
    AE "I am the way I am. Not because of my parents or my upbringing, but because it's my personality. But maybe... maybe you know more about me because of this. Maybe it's an explanation of sorts."
    #CLOCK SFX
    MC "Shiori-chan."
    show AE neutral
    AE "Hm?"
    "Walking over, I wrapped my arms around her and held her as close as I could, holding on to her head with my hand as I pulled her in tight."
    MC "It's okay. I know."
    MC "You're you. And that's all that matters."
    show AE sad
    AE "Hotsure-san... Keisuke-kun..."
    "Shiori-chan put her hands on her heart and smiled the most heartfelt smile I've ever seen her give. There was no cold, no ice, no severity... just her."
    show AE happy
    AE "I feel so blessed... to have you in my life."
    "She walked over to where I was, light beaming past her from the window of the grand tower. She knelt down to where I was on the bench, resting her gargantuan behind softly on her thick calves, and wrapped her arms around me. I did the same, and brought her head close to mine with my hand."
    "We stayed like this for a time, the ticking of the clock passing the seconds by in our embrace. Though the bells had since become silent for the night, I could still hear them. Both in my mind at the moment, and with every swing of Shiori-chan's hips as she walked down the stairs."
    jump daymenu

label AE046:
    $setProgress("AE", "AE047")
    #MUST HAVE SEEN AE 045
    #SCENE AFTERNOON
    scene Dorm Exterior with fade #girl's dorm
    play music Rain
    play sound Knock
    "I knocked on Shiori-chan's door, and then waited with my hands in my pockets. The hallways were silent, most students having returned to their dorms earlier, and as I waited, I couldn't help but wonder why it was Shiori-chan asked me earlier during lunch to meet her here."
    "The door creaked open, as Shiori-chan stepped out, her massive behind taking up much of the doorframe."
    show AE sad with dissolve
    MC "Hey."
    AE "Hi."
    MC "You wanted to see me?"
    AE "Yes, well, I'm free right now, so..."
    "The air around us was awkward, as though every word we spoke was marred and jumbled by apprehension."
    MC "Yeah, usually you're at a meeting around this time."
    show AE neutral
    AE "There wasn't enough going on to warrant one today. Please, come in."
    "Quick to answer, she ushered me into her room."
    scene Dorm AE with fade
    MC "Ah, Yureno-san's not here?"
    show AE neutral with dissolve
    AE "No, she went out to town earlier."
    MC "And you planned around it so we could talk alone?"
    show AE sad
    AE "..."
    MCT "Sounds like I hit the nail on the head."
    "Shiori-chan sat on her bed, and I took the chair at her desk. As she sat, her bed gave off a noticeable creak, accompanying a short grunt from her as her massive ass took up a large portion of the already extra-wide California king."
    AE "Yes. I've thought it over and..."
    AE "I apologize."
    "Her ebon locks swooped down as she bowed."
    MC "You... apologize?"
    show AE embarrassed
    AE "F-for being so forward in the tower. A-and, of course, the events leading up to it. It was unwarranted of me."
    MC "Unwarranted?"
    show AE sad
    AE "I... I was emotionally compromised, and I put more on your mind than you needed."
    AE "I sincerely regret that. So please, forgive me."
    "With another bow, she expressed her heartfelt apology. I, meanwhile, looked at her directly, and answered in a plain and honest manner."
    MC "I don't think you should regret it at all. In fact, now that everything's out in the open, I feel like I can better understand you."
    AE "You truly believe that?"
    MC "I do. If there's anything more that you want me to know about you, tell me. Anything at all."
    "Though she looked to be in disbelief for a moment, she let out a sigh and smiled gently."
    show AE happy
    AE "I thank you for your candor, Keisuke-kun, but..."
    show AE neutral
    AE "I think... I've told you enough about myself."
    show AE happy
    AE "I want to talk about you."
    MC "Huh?"
    MCT "About myself...?"
    MC "What do you mean? How I feel about what you said, or-?"
    show AE neutral
    AE "No, that's not it at all. I've left everything about myself out in the open for you."
    show AE happy
    AE "I want to hear about {i}you{/i}."
    "I sat dumbfounded. Never in a million years would I have thought she'd care that deeply about my own past."
    MC "Eheh, I don't know why you want to hear more about me, I'm just an average guy."
    show AE neutral
    AE "..."
    MC "My life is probably so painfully bland that-"
    show AE neutral-annoyed
    AE "Stop it."
    MC "Huh?"
    show AE sad
    AE "Don't... call yourself average all the time. Don't treat that like it's a badge of shame."
    show AE happy
    AE "Even if your life is like everyone else's... I still want to know what it's like."
    MC "..."
    MC "Okay then... what do you want to know?"
    "Shiori-chan was nearly beaming when I accepted, as though I'd given her a gift. She put her hands in her lap and prepared to listen attentively."
    show AE happy
    AE "What was your childhood like?"
    MC "W-uh... It was... fine, I guess?"
    AE "What about it was fine? How did you spend it?"
    MC "Uhh..."
    "I sat silent for a moment, thinking back on what experiences popped out to me; hoping not to disappoint."
    MC "Eheh, s-sorry, it's just... I'm not really... used to being asked that kind of stuff."
    MC "Ehh..."
    MC "Well, y'know, when I was living out in Tokyo... there'd be this sand hill near this old construction site-"
    show AE neutral
    AE "Sand hill?"
    MC "Yeah. Yeah, it was, uh... just a couple of meters tall. My friends and I, though, we always used to go to the little sand hill and just mess around."
    AE "Mess around how?"
    MC "Ehh... tsh, y'know what, I remember something we always used to do was that... we'd all scramble to the top of the hill, and when we got there we'd toss little pebbles at anyone trying to get to the top."
    show AE surprised
    AE "You threw pebbles?"
    MC "Yeah, yeah, well- I mean, they didn't hurt."
    MC "But, uh... whenever I walked home I'd have a bunch of sand and stuff in my pockets, so... you can tell my mom got pissed at that often."
    show AE neutral-annoyed
    AE "As she has every right to be! Playing around in the sand, chucking pebbles, ugh! It would be a mess!"
    MC "Hey, I cleaned it! No harm, no foul!"
    show AE happy
    AE "Mhmhm~"
    show AE neutral
    AE "...Speaking of, I remember you talking about how you would track mud in the house often."
    MC "N-not often!"
    AE "Did your mother make you clean it every time?"
    MC "Well... yeah, I guess. I mean, she wasn't strict, but she knew how she wanted her house."
    show AE happy
    AE "She sounds like a lovely woman."
    "Speaking to Shiori-chan, I remembered the emotion and sorrow in her voice when she spoke about her own. It reminded me that there was something I wanted to do later."
    MC "Yeah, yeah, she is."
    AE "You said she was an author, yes? Tell me about that."
    MC "I hope you don't mind my asking, but you seem really interested in some kind of minor things."
    show AE surprised
    AE "Minor? I never said I considered them minor at all."
    show AE happy
    AE "Much of the beauty of life is found within small details. Getting to know just those small things about you speaks measures to me about who you are."
    MC "Small things, eh?"
    MCT "This will be cool. She's gonna flip."
    MC "Here, watch this."
    "Reaching into my bag, I grabbed two sharpened pencils and a notebook. I placed the book on her desk, and began to tap the pencils against it with force."
    show AE surprised
    AE "I hope you don't mind my asking, Hotsure-san, but... why are you flattening the points of those pencils?"
    MC "Just watch."
    "I placed the first pencil on it's eraser and let go. Rather than falling, it stood straight up."
    MC "Looking at a possible tilt of the room... maybe slant the second slightly..."
    show AE neutral
    AE "Hm?"
    "Shiori-chan looked on bewildered as I made a rectangle with my thumbs and pointer fingers. I looked through them at the pencil and then, without hesitation, placed the point of one pencil onto the point of the other."
    show AE surprised
    AE "Wuh-...?"
    MC "Done."
    AE "Bu-How is it...?"
    "Shiori-chan eyed the lead and wood tower for a moment, kneeling next to the desk to look at it."
    MC "Old party trick I used to impress friends back in my high school. Cool, right?"
    AE "I don't understand how it hasn't fallen."
    MC "Eh. In general I'm good at keeping things stable."
    MC "I'd guess it's a good trait for an architect to have, yeah?"
    show AE happy
    AE "Mhm, I'd suppose so."
    AE "Wow."
    MC "Now you do something."
    show AE neutral
    AE "Hm?"
    MC "I showed you a little thing I can do, now you do something."
    AE "Wuh... and why are you so certain that I have anything I can do?"
    MC "Ohooo, is that reluctance I hear in your voice?"
    AE "Well, no, but..."
    MC "The beauty of life is found in the small things, yeah?"
    AE "..."
    show AE neutral-annoyed
    AE "Very well, but don't expect me to do this for you on command."
    "Shiori-chan adjusted her posture, bending forward a bit to look me in the eyes, and began to blush slightly as..."
    "*Twitch* *Twitch*"
    MC "Eh?"
    "*Twitch Twitch* *Twitch Twitch*"
    "She began to twitch her nose. Her face hardly moved, but her nose wiggled from side to side."
    MC "Aaaww."
    show AE embarrassed
    AE "S-stop it."
    MC "You look like a lil' bunny!"
    AE "Mmmph."
    "Shiori-chan did her best to turn her face from me, puffing out her cheeks as her blush intensified."
    MC "Don't be shy! That's super adorable."
    AE "Representatives aren't meant to be 'adorable'."
    MC "There's that opinionated side coming out again."
    show AE neutral-annoyed
    AE "And there are your accusations of me being opinionated again. I still don't understand why you think that."
    MC "Well, like I said last time, you just come off that way. Even if I don't..."
    MC "Hmm..."
    show AE neutral
    AE "Something the matter?"
    MC "You know, even though I say you are opinionated, I just realized... I don't even know what your opinions are most of the time."
    AE "..."
    MC "Y'know, I remember you said something a while ago."
    AE "Hm? About what?"
    MC "Something about your beliefs being complex?"
    AE "..."
    AE "I never said they were complex, merely that they would be a bit hard to explain..."
    MC "No worries, then. If you don't feel like explaining, you don't gotta."
    MC "But... I'm just gonna tell you now, there's nothing you should ever feel the need to hold back saying, or even questioning, when it comes to me."
    show AE neutral
    AE "...Very well, then... I'll keep that in mind."
    scene black with fade
    "We spent the rest of the time talking about small things. Pleasantries, annoyances, the whole gambit of minor details about each other. By the time we started to wrap up, a fair amount of time had passed."
    scene Dorm AE with fade
    show AE happy with dissolve
    MC "Well, I better get goin'."
    "Shiori-chan looked surprised for a moment, but looked out of her window to watch the sun sink slowly on the horizon."
    AE "Ah! I hadn't noticed I've... been talking this long, aha."
    AE "Wouldn't want you out when you shouldn't be."
    MC "Right, right."
    MC "Well, I'll see you in class. Tell Yureno-san I said hi when she gets back."
    "I got up, and headed for the door. I turned around and wanted to ask Shiori about her plans tomorrow when..."
    show AE embarrassed
    AE "S-see me again here? Same time?"
    "I gave a soft, warm smile at her question. Knowing she felt the same way elicited at least a sense of contentment in my heart."
    MC "...Yeah. Of course."
    "I walked out the door, and headed to my room to get a bit of rest before tomorrow."
    scene black with fade
    "At least, after talking to a certain someone."
    scene Dorm Interior with fade
    MC "..."
    #*PHONE BEEP SFX*
    Mom "{i}Keisuke?{/i}"
    MC "Hey mom... I'm just calling to say hi."
    jump daymenu

label AE047:
    $setProgress("AE", "AE048")
    scene Dorm AE with fade
    play music Hallway
    #SCENE AFTERNOON
    "A brisk wind blew through the open bedroom window, the curtains fluttering lightly at it's passing. Shiori-chan and I had spent much of the afternoon talking together, and before we knew it, we'd reached into the early hours of sundown."
    "As it so happened, the two of us had gotten onto the topic of music. Her piano teacher apparently playing a more prominent role in her life than I'd thought, it turned out she was a pretty big connoisseur on the topic."
    show AE happy with dissolve
    AE "Now, you see, a Wurlitzer band organ has a fairly unique sound, and is useful for more jaunty playful tunes like you'd find in theatres, though perhaps a carnival organ would have a somewhat comparable sound to-"
    "If not a bit obsessive."
    "I didn't mind, though. Listening to her talk about things she's passionate about strangely makes me feel content knowing that she's comfortable around me."
    AE "I however vastly prefer a nice, traditional cathedral organ. Of course, I wouldn't turn down a portative if offered."
    MC "Ever been offered?"
    show AE embarrassed
    AE "N-No... but I wouldn't turn it down if I was."
    MC "Not a lot of people offering up portable organs, eh?"
    AE "Oh lord, now I sound idiotic."
    MC "Pfff- Keheheh~"
    show AE happy
    AE "Haaaah, dear... still, though, what a treat it would be to hear a nice rendition of Bach live."
    MC "You listen to music often?"
    show AE neutral
    AE "Not really, no. After I transferred to Seichou, I didn't really have the means to do so."
    MC "Really? You don't go and listen to music on your phone or anything?"
    AE "Music on a... phone?"
    MC "...Um..."
    MC "Do you have a phone?"
    AE "I do."
    MC "And you can't play music on it?"
    AE "Well, I mean..."
    "Shiori-chan sat up, her skirt clearly becoming increasingly ill-fitting, as her attempts to pull it further down were in vain. Ceding, she walked over to her drawer and pulled out a phone... an outdated one from nearly ten years ago."
    AE "It's not much, but it can send messages and make calls. Not really much point other than that."
    MC "Ah... I suppose that makes sense. No need for the extra bells and whistles of... well, modern technology."
    show AE neutral-annoyed
    AE "Hey! I'm very well versed in modern technology! I'll have you know that the office printer is a t-847."
    MC "Wow! A t-847!?"
    MC "Here. Take a look at this."
    "As she sat down, I pulled my own phone from my pocket, and went to a music site. Pulling some headphones from my pocket, I plugged it in and placed one in my ear, offering up the other one to Shiori-chan."
    show AE embarrassed
    AE "I'm usually only used to telling people to take them out, so bear with me."
    "Fiddling with it, and after it falling out of her ear a few times, she seemed to get the hang of it."
    show AE neutral
    AE "Okay. So, where are the buttons?"
    MC "Um... the screen... you touch it and the pictures work as buttons."
    "Shiori-chan watched as I tapped the screen and found the app. I typed in a song by one of my favorite pop bands, AR4Q and pressed play."
    MC "This is one of my favorites."
    show AE surprised
    AE "O-oh! It's a bit loud... but it's interesting."
    MC "Eheh, yeah, I know you said you like older music, but I figured I'd show you some of mine."
    show AE happy
    AE "Hmm... well, it certainly is very upbeat."
    "We listened to the rest of the song, and I handed the phone off to Shiori-chan."
    MC "Here. Now you pick something."
    show AE surprised
    AE "Me?"
    MC "Yeah, just type the name into the search bar."
    show AE neutral
    AE "Hmm..."
    "After a few seconds of fidgeting and changing words, she finally pressed a song."
    "Orchestral music softly faded into the bud. From the first few seconds, I could hear what Shiori-chan was talking about when she was mentioning her western influences."
    MC "Huh... I'd heard classical music before, but this style is new to me."
    AE "Mhm. It's a coronation anthem."
    MC "It makes me wonder wh-"
    $renpy.music.set_pause(True)
    "{i}ZAAAAAADOOOOK THE PRIEEEEEST{/i}"
    MC "ACHG-!!"
    "{i}AND NAAAAAATHAN THE PRO-{/i}"
    $renpy.music.set_pause(False)
    "Panicking, I quickly grabbed the phone and turned the volume to mute."
    AE "Hm? What's wrong?"
    MC "That... ah..."
    MC "W-Wow, Shiori-chan, I had no idea the music you listened to was that... um... loud."
    AE "You consider that loud? Perhaps 'boisterous' is a better term."
    MCT "YOU THINK POP IS LOUD COMPARED TO THAT?!"
    MCT "I gotta change this to a different song, my ears are gonna start bleeding if I don't."
    MC "So, um, a while back you said your favorite song was... Ech-Echi-?"
    AE "Ecce Sacerdos Magnus. Bruckner."
    MC "Okay, right, I'll play that next."
    "A few types and a tap later, and music slowly started up again."
    $renpy.music.set_pause(True)
    "{i}ECC-{/i}"
    $renpy.music.set_pause(False)
    MC "Turning it down a bit, if you don't mind."
    show AE happy
    AE "Perfectly fine."
    "After turning it down severely, the complexity of the music became more clear. A choir of different voices sang in a foreign language I didn't understand, yet I picked up on the tone and beauty of the song quickly."
    #IF YOU'VE SEEN 013-B, Skip Dialogue
    #K: Mmm, sounds nice, but I don't know what they're saying.
    #S: It means 'Behold the Great Priest'.
    #K: Really? What language is that?
    #S: That's latin.
    #K: You speak latin?!
    #S: A bit, yes.
    #K: Where did you learn that?
    #S: I learned it from Professor Schultz initially, but as I learned more English, I met with people who had more experience speaking it, and I learned it in depth.
    #K: Ah, I see.
    #*That professor again. Just how much of her life does he influence?*

    scene black with fade
    "We listened to the music for a bit longer, and eventually, we got to talking a bit more."

    scene Dorm AE with fade
    show AE neutral with dissolve
    MC "Really? With the eel? That's crazy!"
    AE "I... never said anything about an eel."
    "I may have been fading in and out of conversation to take glances at her legs."
    show AE happy
    AE "In any case, I'm very glad we've become so close."
    MC "Definitely! I feel I could share anything with you."
    "She smiled lightly, but it slowly faded. She took a glance up at my hair and then asked..."
    show AE embarrassed
    AE "Does your hair get matted?"
    MC "Huh?"
    AE "It's just... something I'm curious about."
    "Amused by her curiosity, I grinned as I sunk back into the bed, shaking my hair before stroking it at the side."
    MC "Umm, yeah, if I don't brush it."
    AE "Ah, I see. Thank you."
    MC "No problem."
    show AE neutral
    AE "..."
    MC "Anything else?"
    show AE embarrassed
    AE "..."
    AE "How can you see? With the bangs, and all that?"
    MC "Uhh... y'know, I actually have no idea. I've had this style since I was little, but I've never really thought about it."
    show AE neutral
    AE "Have you ever tried to shave it bald completely?"
    MC "N-no way!"
    AE "I only ask because I know that your particular case makes your hair grow more rapidly over time."
    MC "But what if it stops altogether if I shave it!?"
    show AE happy
    AE "Well then, I'd have one adorable melon, wouldn't I?"
    MC "O-Oy!"
    AE "Mhmhm~"
    MC "I don't wanna take any chances. My hair is sensitive as is."
    show AE neutral
    AE "Ah, So it does hurt if it's pulled?"
    "Reaching over, she took to fingers and slowly yanked down."
    MC "O-Ow! Yeah! It's just like normal hair, you know?"
    show AE embarrassed
    AE "I-I figured, I just wanted to know if your growth was anything like mine."
    AE "I apologize."
    MC "Ahaha, it's fine. It didn't hurt that much."
    show AE neutral
    AE "Anything you want to know about me?"
    MC "About you?"
    AE "Yeah."
    MC "Hmm."
    "If I had any questions for her, what should I ask..."
    menu:
        "How are you with children?": # +2
            jump AE047_c1_1
        "Can you lie on your back?":
            jump AE047_c1_2
        "How does it feel?": #+1
            jump AE047_c1_3
        "Anything positive?":
            jump AE047_c1_4
        "Ever skip leg day?": #-1
            jump AE047_c1_5
        "I can't think of anything in particular.": #+2
            MC "Can't think of anything."
            show AE surprised
            AE "Really?"
            MC "Yep. You're you, and that's all I need to know."
            $setAffection("AE", 2)
            show AE happy
            AE "..."
            "Though most would feel offended about a seeming lack of interest in their personal affairs, Shiori-chan seemed to like that last line especially."
            jump AE047_c1_after

label AE047_c1_menu:
    menu:
        "How are you with children?" if not getFlag("AE047_c1_1"): # +2
            jump AE047_c1_1
        "How are you with children? (disabled)" if getFlag("AE047_c1_1"):
            pass
        "Can you lie on your back?" if not getFlag("AE047_c1_2"):
            jump AE047_c1_2
        "Can you lie on your back? (disabled)" if getFlag("AE047_c1_2"):
            pass
        "How does it feel?" if not getFlag("AE047_c1_3"): # +1
            jump AE047_c1_3
        "How does it feel? (disabled)" if getFlag("AE047_c1_3"):
            pass
        "Anything positive?" if not getFlag("AE047_c1_4"):
            jump AE047_c1_4
        "Anything positive? (disabled)" if getFlag("AE047_c1_4"):
            pass
        "Ever skip leg day?" if not getFlag("AE047_c1_5"): # -1
            jump AE047_c1_5
        "Ever skip leg day? (disabled)" if getFlag("AE047_c1_5"):
            pass
        "Nothing else.":
            MC "I think that should be it. Everything I feel would be polite to ask, anyways."
            "Nodding, Shiori-chan leaned back into the weight of her own puffy ass, acting as a sort of natural cushion."
            show AE happy
            AE "Right. Tell me if you think of anything else, okay?"
            jump AE047_c1_after

label AE047_c1_1:
    $setFlag("AE047_c1_1")
    MC "How are you with kids, Shiori-chan?"
    AE "W-what?!"
    MC "Ah, strictly from an experience point of view."
    AE "Y-yes, yes, of course."
    AE "I... don't have much experience with children but... I'd really like to..."
    AE "S-strictly from an experience point of view, that is. I have an occupation to think about."
    $setAffection("AE", 2)
    AE "It is still... quite the touching thought, it is. Children of my own..."
    AE "*Khm* Well, enough of that. I've thoroughly embarrassed myself, so if you'd please, stick with questions that are a bit less up for interpretation."
    jump AE047_c1_menu

label AE047_c1_2:
    $setFlag("AE047_c1_2")
    MC "Can you lie on your back?"
    AE "Unfortunately not. When I try, I usually end up having to arch my back."
    MC "Oof, that sounds like it has to hurt after a while, right?"
    AE "Surprisingly, no. My back muscles are particularly strong, I've noticed."
    MC "Think it has to do with your posture?"
    AE "Of course."
    MC "Huh... well, I guess you were right about the importance of sitting up straight, then."
    AE "...Hm, I suppose so."
    MC "Hey, no need to get smug!"
    AE "Mhmhm~."
    MC "That does raise the question, though, how do you lay in bed? On your side?"
    AE "No, my hips prevent me from doing that. Same problem with the back, but less support."
    MC "Then... on your stomach?"
    AE "Unfortunately, yes. I understand the health risks, but I don't have much other choice."
    MC "What's keeping you from getting trapped under the weight of your own butt after a while?"
    AE "I was worried about that too, but it appears my leg muscles are becoming stronger as well."
    MC "Huh... well, that makes sense, I guess."
    jump AE047_c1_menu

label AE047_c1_3:
    $setFlag("AE047_c1_3")
    MC "So... how does it feel?"
    AE "It?"
    MC "As in, you know, having your body grow."
    AE "Oh... hm..."
    AE "I... don't know. It just feels strange. For the past few months, my life has just been a constant feeling of skin and... parts of me just stretching, squishing, swelling; things getting re-positioned on my body I never thought were possible."
    AE "First it feels like I'm made of jello, and then I feel stretchy until everything just feels so tight... and then it feels like I'm made of jello again."
    AE "The constant shifting of the fat in my body makes me feel nauseous, but... sometimes it just feels... good? Does that make any sense?"
    AE "No? No, I suppose it wouldn't."
    MC "Shiori-chan... I don't think I can ever fully understand the feeling, but I think what you're describing makes sense."
    $setAffection("AE", 1)
    AE "Thank you, Keisuke-kun."
    jump AE047_c1_menu

label AE047_c1_4:
    $setFlag("AE047_c1_4")
    MC "Are there any upsides to having a... butt like yours?"
    show AE sad
    AE "That's a question I've been asking myself since I first learned I was growing."
    MC "Have you found any answers?"
    AE "...No."
    MC "Ah."
    AE "..."
    MC "..."
    "Silence. I could tell there was a bit of pain in her voice, echoed in the awkwardness in the stagnant air."
    show AE embarrassed
    AE "Well, I suppose that my leg muscles make it so that I have more endurance and strength in my legs. I've also found that the skin in my entire lower body is extremely resistant to cuts and damage."
    MC "Wait, really?!"
    show AE neutral
    AE "Mhm. If you remember, I didn't scrape my legs when you tripped me up during the sporting festival. I'm sure there's a threshold, but I don't dare try and experiment further than I already have."
    MC "T-that's amazing! That's like a superpower!"
    show AE sad
    AE "It's... not much of a consolation."
    MC "Well, maybe not, but it's nice to think on the positive side of things every now and then, yeah?"
    show AE neutral
    AE "...True."
    jump AE047_c1_menu

label AE047_c1_5:
    $setFlag("AE047_c1_5")
    MC "So, do you ever skip leg day?"
    show AE neutral
    AE "..."
    $setAffection("AE", -1)
    "Thought her face betrayed it, I could feel nothing but seething anger emanating from Shiori-chan."
    "Enough so that I quickly began to reevaluate my life choices, as well as what I should ask."
    jump AE047_c1_menu

label AE047_c1_after:
    MC "I honestly gotta say, I feel like I've learned more about you over our time here than I've ever got to know anyone in my life."
    show AE happy
    AE "I completely agree."
    "Shiori-chan brushed her hair to the side and smiled, a light blush slowly forming on her cheeks."
    AE "You know, I'll always be thankful for that day in the rain. The day I invited you in for those papers."
    MC "Oh yeah! That was how it started, huh?"
    show AE neutral
    AE "Mhm, and since then you've opened my eyes to... so many new things."
    AE "So many..."
    MC "..."
    stop music
    show AE sad
    AE "..."
    MC "..."
    "Not a word needed to be said. The tension in the air said it all for me. I could feel it strongly as I stared Shiori-chan in the eyes, the same numbness I felt the day I asked her out. I opened my mouth slightly to speak the words of my heart, but they never came."
    AE "..."
    MC "..."
    
    scene black with fade
    "And then, almost on instinct..."
    MC "..."
    AE "...Mmph~"
    #Fade back in, Kissing CG
    "All I did was lean my head forward slightly, and before long our lips were sealed in a passionate kiss. My heart felt like it was on fire; a flame sparked by the warm touch of her soft lips."
    MC "M-Mmhm~"
    AE "Hmn, mph..."
    "She pulled away for a second, but moved my head further towards the warmth again. The tips of our tongues began a soft and gentle dance as my hand wrapped around the back of her neck, her long silky locks caressing my hand, as mine caressed hers as she placed her own on my shoulder."
    "Neither of us wanted to let go. We didn't know when to let go. We kissed for a minute which felt like eternity. When we finally did, she opened her beautiful silvery eyes, her glasses having slipped down to the tip of her nose in our embrace."
    scene Dorm AE with fade
    show AE happy with dissolve
    play music Hallway
    AE "...Wow..."
    MC "Mhm, yeah... wow."
    "The bell chimed in the tower as golden sunlight bathed the room in its radiance. There it was. Our first kiss."
    AE "Hah... I've finally done it... I've kissed a man... for the first time in my life."
    "I smiled and took her hand in mine, her palms warm and soothing to the touch with traces of her heartbeat."
    MC "How was it?"
    AE "I..."
    "She shrunk back and smiled, her face burning a vibrant pink."
    AE "Is this...?"
    MCT "Is this...?"
    MC "Oh! T-the bell, right. Um... I guess curfew is starting. I outta head back to..."
    MC "Uh..."
    "Shiori-chan's eyes were still, her breathing heavy as she rested her hands in her lap."
    show AE sad
    AE "Am I truly willing to...?"
    MC "To... what?"
    AE "..."
    "Shiori-chan looked out of the window towards the setting sun, mind clearly swimming with thoughts."
    AE "You... you should probably go... curfew."
    MC "Ah. Y-yeah."
    MC "So, can I see you...?"
    AE "..."
    MC "R-Right. Curfew."
    MC "That was great, by the way. It really was."
    AE "..."
    "The romantic mood had completely changed into emptiness. Shiori-chan didn't respond, only looked out the window and nodded."
    MC "Alright... well, see you later."
    "I stood up and exited the room, half expecting an invitation for the next day, but never getting one."
    scene black with fade
    "The minute I left, the feeling returned, and my heart began racing once more. Try as hard as I might to contain it, a deep, heartfelt smile crossed my face, and I began to laugh slightly."
    "Leaning up against the wall, I put my hand on my beating chest, and began to wonder where all our relationship would take us."
    jump daymenu

label AE048:
    $setProgress("AE", "AE049")
    scene Hallway with fade
    #SCENE AFTERNOON
    "I paced the halls worriedly, and the longer I looked, the stronger my anxiety became. Just the other day, I felt like I was on the top of the world; I'd finally kissed Shiori-chan. But just when I get excited to spend my afternoon with her and talk it over."
    "She vanished."
    "When I tried to talk to her after class, she nearly darted out, leaving me behind. I could swear that I saw her cover her face with her hand too. After checking the office, her room, and the roof, I'd nearly given up until I noticed something strange when looking out the window."
    "Yuki-chan was standing in the courtyard next to the clocktower entrance. Arms crossed, looking side to side every few seconds as if on the lookout."
    MCT "Hell's going on out there?"
    MC "Hm..."
    "Part of my worry replaced by a heightened sense of curiosity, I exited the hallway and entered the courtyard."
    
    scene Campus Center with fade
    play music Hallway
    MC "Oy! Yuki-chan, got a sec?"
    show Yuki neutral with dissolve
    Yuki "Huh? Keithuke-than?"
    MC "Yeah, hey! I was wondering if-"
    "Quickly, as I approached, she pouted and put her arms out to block the door."
    MC "Woah, geez, why so defensive?"
    Yuki "I cannawt wet anywun in. Mathumoto-than is tawkin wif Yuweno-than."
    MCT "Can't let anyone in? Isn't this place already off limits to regular students? Why the extra security?"
    MC "What about?"
    Yuki "Nuhn uv yow beethwaxf."
    MCT "Yuki-chan's growth is getting pretty bad... I think I may have gotten two words out of that."
    MC "Do you know?"
    Yuki "Ah..."
    MCT "Why would she and Yureno-san meet here? What's going on?"
    MC "Yuki-chan... I'm worried about Shiori-chan. I just wanna talk- look, can you just let me in?"
    Yuki "N-Nuh!"
    "She says no, but her giant lips can't possibly hide the sorrow on her face as I spoke. I step a bit closer."
    MC "Yuki-chan, please. I'm her boyfriend. I'm worried about her, she hasn't even wanted to acknowledge me recently! You're the closest thing to a friend she has, don't you feel the same?"
    Yuki "Nuugh..."
    Yuki "O'tay, o'tay, 'ou gawt me. Yeth, I am wowwied abowt huw. She'th been aktin weawwy stwange wecentwy. I'm wowwied."
    Yuki "...Hmm..."
    Yuki "Wook. Aww webbuw wiff 'ou. If ah tuwn awound, ah didun thee nuthin."
    MC "Um... I'm sorry, you kind of lost me..."
    Yuki "Ugh, wissen. Aww wet 'ou in, buh if 'ou get cawt, 'ou snuck pasth me, o'tay?"
    MC "My lips are sealed."
    MCT "I... probably should have watched the wording."
    Yuki "Smawt-ath. Get in dewe, an' wet me kno wha'th goin awn."
    MC "Ota- Okay."
    "Yuki-chan stepped out of the way, and I nodded humbly. I entered the clocktower once again, and began my ascent."

    scene Clock Tower with fade
    "I silently climbed up the wooden stairwell, each step causing a minor creak which I did my best to minimize. As I ascended I heard the two bickering about something."
    UNKNOWN "-room isn't private enough."
    UNKNOWN "Fine, but why don't-...-makes absolutely no sense."
    "The closer I got, the more clear they became, until I finally poked my head into the main chamber."
    #show Tako angry at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show Tako neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show AE sad at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    Tako "Look, are you gonna get 'em or not?"
    AE "I... I am. I can't risk-"
    Tako "Then go get 'em. I said I'll do it, but not if you just sit around being indecisive about it."
    show AE embarrassed
    AE "N-Never. I've never been indecisive in my whole life!"
    Tako "Then we wouldn't even be talking it over right now!"
    "Shiori-chan and Yureno-san were acting like I'd never seen before. Yureno-san was annoyed, upset even, as she stood up straight and talked Shiori-chan down. Shiori-chan shunk back, her knees buckled, and her flabby thighs pressed tightly together."
    Tako "Why are you even hesitating anyway? Don't you have a future to think about?"
    AE "I do! It's just... It's just against my principles is all."
    Tako "Against your pri- Do you even have any idea what you're doing?!"
    AE "I know, I know! I just... I have to do this. I feel it. I'm being called to do this with every inch of my being."
    Tako "Here we go again. Look, why don't I just get em' eh? You can look after him instead."
    AE "No. I can't be anywhere near him. Whenever I am, I feel like I'm going to-"
    "*CRRK*"
    "I looked down to see that my foot had been placed on the loose board."
    show AE surprised
    AE "Eh?"
    Tako "What in the..."
    MC "Gch!"
    "I quickly ducked behind the stairway to hide."
    Tako "Yo, isn't puffy lips supposed to be guarding the door?"
    show AE embarrassed
    AE "Sh-Show yourself! I'll have you know this area is off l-l-limits!"
    MCT "Damnit. If I run out of the tower, Yuki-chan will for sure have to give me away..."
    "Realizing I'd been completely caught, I stood up and walked into the belfry proper."
    show AE surprised
    AE "K-Keisuke-kun? What are you-? Y-you're not supposed to be here!"
    MC "I-I know, but... what's going on? What are you two talking about?"
    Tako "Shiori-chan has a clown fetish."
    MC "EH?!"
    AE "EEEEHH?!"
    Tako "Yep. Cats out of the bag now ain't it."
    AE "N-No I do not!"
    Tako "She wants me to get her clown shoes and helium. Seriously, do you even know where to get that stuff?"
    "Shiori-chan swung around to face me directly, her fleshy ass wobbling like mad as she did."
    show AE angry
    AE "K-Keisuke-kun! Don't listen to her! She's j-just being facetious. Isn't that right? Tell him I'm right!"
    "Yureno-chan broke her stony facade and began to giggle to herself, ending with a sneer as she rested a hand on her oversized hip."
    Tako "Tch, wastin' a good distraction."
    AE "That was NOT a good distraction!"
    AE "I'll have you know I have no distasteful... eccentricities whatsoever!"
    Tako "Come on, don't be such a prude. There's gotta be something that gets you goin'!"
    Tako "Who knows, maybe you're one of those people that loves wearing giant animal costumes or something!"
    show AE embarrassed
    "She bagan maniacally cackling to herself before bringing a firm hand on her roommate's extra-jiggly, sensitive rump. Shiori-chan's back immediately straightened further than I'd ever seen it, even with her sharp attention to good posture."
    "Her eyes went wide, pupils dilating beneath the frames of her glasses, as her mouth drops open. The softest, barely-audible moan escaped her lips. A low, guttural groan of pleasure surfacing from the deepest recesses of her brain."
    "The jiggling in her rump continues unabated for several seconds, only ceasing when she finally recovers from the unexpected thrill of her buttocks being spanked."
    Tako "Shiori? Yoohoo?"
    "No idea how to respond, her throat has become too dry to say a single word. All her brain power being used to focus on whatever it was she was feeling in that moment."
    MC "I... I think you broke her."
    Tako "Damn, I guess she really is sensitive now."
    MC "Sensitive?"
    AE "U-Uuuooahgh...."
    Tako "Oop, there we go. She's comin out of it."
    AE "What... what was..."
    "Shiori-chan blinked a few times and readjusted her glasses, her face as read as a cherry."
    show AE angry
    AE "Y-Yureno-!"
    Tako "Weeelp, I'm bored. See ya back at the dorms Shiorear."
    show AE embarrassed
    AE "W-Wait, no, don't leave me to-"
    hide Tako with dissolve
    "Before finishing her sentence, Yureno-san was already descending the staircase with a peace sign displayed proudly from one hand. Shiori-chan looked to her mouth agape, then back to me as she blushed."
    show AE sad at center with dissolve
    AE "K-Keisuke-kun..."
    MC "What's been going on with you?"
    show AE embarrassed
    AE "M-Me?"
    MC "Why are you avoiding me? What was with the face hiding? Why are you sneaking arou-"
    show AE surprised
    AE "Your space!"
    MC "Eh?"
    "Shiori-chan's quick response left me speechless as she looked around."
    show AE sad #nervous
    AE "You're a... m-man who-"
    show AE embarrassed
    AE "Who, uh..."
    show AE sad #nervous
    AE "Needs his privacy, is all."
    show AE happy
    AE "Yes, yes that's right. I wish to respect your space."
    MC "Shiori-chan... what happened to being open and honest?"
    show AE embarrassed
    AE "Ah..."
    AE "..."
    AE "I'm just..."
    show AE sad
    AE "I'm sorry. I just need some time alone is all."
    MC "But why?"
    AE "...Please. Just... a lot has been on my mind."
    MC "..."
    "While her resistance did hurt a bit, I took a good look into her eyes. Not a trace of sorrow, nor malice... in fact, I strangely felt like I saw love in those eyes."
    MC "...Eheh, you're right. I've been damn near smothering you lately. If you want some space to think for a while I'll let you have it."
    show AE sad #nervous
    AE "Y-Yes?"
    show AE happy
    AE "Keisuke-kun... Thank you."
    MC "The minute you want to hang out again, though, you know where to find me."
    "I flashed her a smile, and she smiled back... then her eyes widened and her smile faded. Her knees buckling once more, she began to blush like mad."
    show AE embarrassed
    AE "Y-Yes, well, I'll k-keep that in mind."
    "A bit taken aback from her reaction, I nodded and turned around, descending the stairway."

    scene Campus Center with fade
    show Yuki neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    Yuki "Ah'm tewwin 'ou, 'ou cannawt go in dewe!"
    show RM neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    RM "C'mon! He's my roomate! He could be in trouble!"
    Yuki "Yea wite! Daichi yow mai bwudder, 'ou can't twick me wiff dat!"
    RM "I'm telling you, Keisuke's been looking forlorn and hurt since class ended! If he's hurting, it's my responsibility as a friend to help."
    Yuki "...Uuu Daichi~ Fine, if 'ou teww me what's gowin own, aww wet 'ou-"
    MC "Um, guys?"
    RM "Keisuke! Have you seen Matsumoto-san?"
    MC "Wait, wa- I thought you were looking for me?"
    RM "I lied."
    Yuki "Wuh- 'Ou jewk!"
    MC "And my hubris sinks even further. Why are you looking for my girlfriend?"
    RM "Because she disappeared! I tried looking everywhere but she vanished!"
    MC "Rewording: Why are you {b}actively{/b} looking for my girlfriend..."
    RM "Because she's the class president. Someone like that doesn't just go off the radar."
    Yuki "Yeah! Speakin uv which, wha happuh? Yuweno-than wawked owt uweuw."
    MC "Ahh..."
    RM "'Speaking of which, what happened? Yureno-san walked out earlier.'"
    MC "Oh, right."
    MC "Uh..."
    MCT "What even did happen? I'm so confused."
    MCT "But... even so. At least I know that she isn't mad at me."
    MC "She just needs some time alone. She'll get better soon."
    Yuki "Eh? Weawwy?"
    MC "Weawwy-"
    MC "Ach- R-Really."
    show AE neutral at center with dissolve
    "As we spoke, Shiori-chan walked out of the bell tower. She looked to Yuki-chan and pursed her lips."
    Yuki "Eheh... no gawwd duty fwum nao awn?"
    hide RM
    AE "Correct."
    "She turned to me, and opened her mouth to talk, yet no words escaped her thin lips. She instead blushed and stammered out a simple-"
    show AE embarrassed
    AE "B-Be seeing you."
    "I looked to Daichi, who had disappeared, leaving a mop in a uniform to flop over onto the ground."
    MC "Okay seriously, how does he keep doing that shit?!"
    AE "Language."
    "After the most unenthusiastic scolding from Shiori-chan I think anyone's ever gotten, she walked away, stopping briefly at the door. Looking back, she blushed, covered her massive behind with her hands as best she could, and stepped through the door."
    hide AE with dissolve
    Yuki "Uuu~ Daichi, duh bwoom twick won't wuwk awn me!"
    RM "..."
    show RM neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    RM "...I never could get it to work with you."
    MC "OH FU- Dude, how do you do that?!"
    RM "You jokin me? I learned that from a magic trick book for kids."
    Yuki "Yah, aww 'ou bwind?"
    MC "..."
    MCT "If I were, I'd probably be at a better school."
    RM "Well?! Back you never answered my question? Why's she actin all crazy eh?"
    MC "Look, it's none of your..."
    MC "..."
    MC "Actually..."
    MC "Yeah, sure, I'll tell you."
    RM "Are you fu-!"
    RM "Wait, you will?"
    MC "Yeah, you doin' anything right now?"
    Yuki "Wait, wait, wuh bowt me!? I wunnuh know too!"
    RM "Ehh, Yuki-chan, I think this is something Keisuke wants to talk about privately. You're not exactly a private girl."
    Yuki "Ah-!... Eh... faiw point."
    MCT "He will without a doubt tell her everything later."
    
    scene Diner with fade
    show RM neutral with dissolve
    RM "You kissed her?!"
    "Going to my usual restaurant, I filled Daichi in on everything that's happened so far. Whether I did it out of pity, morbid curiosity, or hope for some kind of solid advice, I'll never know."
    MC "Y-yeah. It felt like... it just felt like the right time."
    RM "You may as well have proposed to her! Dammit, what were you thinking?!"
    MC "Wait, what?!"
    "The notion was absolutely absurd. I know Shiori-chan would take it seriously, but not {i}that{/i} seriously."
    MC "I-It was just a kiss, I don-"
    RM "A girl like Shiori ain't just gonna look at it like 'Just a kiss', she's the type of girl who thinks holding hands in public is lewd!"
    RM "Look, look, what was she saying after the kiss, eh?"
    MC "Um... 'Wow'?"
    RM "Anything else?"
    MC "She was telling me... it was her first kiss."
    RM "PFFF, REALLY?! Oh my god what a los-!"
    MC "Yo."
    RM "Pure and innocent girl."
    RM "So pure. So innocent... it makes me suspicious."
    MC "Oh geeze. Man, I get it, you're paranoid about her-"
    RM "Of you."
    MC "Eh? Me?!"
    "Taking another sip of his coffee, he looked up to me and raised an eyebrow."
    RM "So... did you two kiss or did you steal one?"
    MC "Oh no, don't you put that on me! We both leaned in for the kiss together!"
    RM "Did you, or is that how you remember it in the moment?"
    MC "That is how it happened! I think... I mean, she looked happy right after..."
    MC "..."
    "I sat in silence for a moment, recalling everything that happened."
    MCT "We kissed, I smiled, she smiled... I felt proud... she felt..."
    MCT "Shame? Wait... was she feeling shame?"
    MC "..."
    MC "Hey, man, um... here's some cash, can you pay for the both of us? I'm gonna head out."
    RM "Yeah, yeah, stick me with half the bill why don't you, not like you said you'd pay or anything."
    "I placed some cash on the table and walked out, back towards the school, a new source of worry on my mind."
    
    scene black with fade
    RM "*Sssp*"
    RM "Mm, this is some damn good coffee."
    jump daymenu

label AE049:
    $setProgress("AE", "AE050")
    scene Dorm Exterior with fade
    #SCENE AFTERNOON
    play sound Knock
    MC "Shiori-chan, it's me. Can you open up?"
    "Shiori-chan had been acting strange recently, and it left me worried and confused. Up until the other day, I'd felt we'd been getting closer. But after that kiss..."
    MC "Shiori-chan... if it's about the kiss. I wanted to say I'm sorry. I was too forward and-"
    "*Click*"
    "The door was opened swiftly, and I was greeted by a girl with elephantine hips... just not Shiori-chan."
    play music Schoolday
    show Tako neutral with dissolve
    MC "Oh."
    Tako "'Oh', yourself."
    MC "Hey, Yureno-san. What's up?"
    Tako "Not much. Eating pizza, playing guitar, the punk queen life."
    "I tried to be polite by smiling and nodding, but I would actively look past her to Shiori's bed."
    Tako "Really, there's not much to do outside of class today."
    MC "Uh-huh. I get you there. Hey, by the way-"
    Tako "She's out right now."
    MC "A-ah."
    MCT "Is it really that obvious."
    MC "Well, uh... guess I'll look for her then. I wanted to-"
    Tako "Mm! Hm-mm, no can do. Just remembered I'm supposed to look after you."
    MC "Look after me?"
    Tako "Yeah, Shiori had stuff to do, and asked me to keep track of you."
    MCT "What am I, a dog?!"
    MC "Wuh- That doesn't... but why?"
    Tako "Can't say. Although..."
    "Yureno-san grinned heartily, and placed a hand on on of her wide, child bearing hips as the other stroked her chin."
    MC "Well... I think I'm fine on my own. Eh, tell her I'll-"
    Tako "You free?"
    MC "Huh?"
    Tako "Are. You. Free?"
    MC "I heard you, but-"
    Tako "Then quit with the 'huh?' and 'wha?' all the time. It's annoying."
    MCT "I don't say it that much!"
    MC "Well, classes are over so-"
    Tako "Let's get a coffee together."
    MC "Uhh... no thanks, I was just thinking that Shiori-chan and I-"
    Tako "We'll be back before her, now come on, let's go."
    MC "W-wait, hold on, I barely know you and-"
    Tako "Come oooonnn~"
    MCT "I guess there's no point trying to argue. She seems really enthusiastic about it..."
    MCT "Whatever, I was just going to wait for Shiori-chan anyways."
    MC "Sure. There's this diner in town that-"
    Tako "Yep-yep! I know the one. I'm ready."
    MCT "Ready?! You look like you just got out of bed!"
    "Before I could say anything more, Yureno-san already was leaving her room, and leaving me behind as she walked briskly out of the dorms."
    stop music
    
    scene black with fade
    "I eventually caught up with her at the gate, and we walked out to the diner."
    
    scene Restaurant with fade
    play music Busy
    "Today seemed busier than usual. As we walked in, we were greeted with the murmurs of the patrons and the smell of freshly ground coffee. Yureno-san walked up to the counter and greeted the waitress with... extra enthusiasm."
    show Tako neutral with dissolve
    Tako "Hey-hey, there, cutie. Got any seats open for shaggy and me?"
    "Yureno-san bent over and rested her arms on the counter, making her skirt ride up and revealing a pair of lacy black panties. Rather than try to pull her skirt down, she scratched her gargantuan behind, lacking any sense of social grace or tact."
    MCT "I... I shouldn't stare at her like that. It just feels like I'm being unfaithful."
    Waitress "Yes ma'am! Please follow me."
    "She smiled, and lead us to our seats. The same seats Shiori-chan and I would usually sit in."
    Waitress "Can I start you off with anything to drink?"
    Tako "We're both just gonna have coffees. Ain't that right, Keisuke?"
    MCT "She's... really keen on just talking to me on a first name basis."
    MC "Y-yes, ma'am. Just some coffees, please."
    Waitress "Okay, and what type would you like?"
    Tako "Ehhhh. Hmmmm."
    MC "Try it just black."
    Tako "Hm?"
    MC "It's pretty good like that."
    Tako "...A'ight, yeah, hardcore."
    "We ordered two black coffees, and then just waited in silence. I looked around, and tapped my hands on the table. Every few seconds, I would glance over at Yureno-san, who simply stared at me. I spoke up, if only to break the ice."
    MC "So, uh... how's school goin'?"
    Tako "Actually, to be honest, I don't know if I'm gonna continue with school. I'm thinking about playing the guitar and joining a band."
    MC "Really? I guess it makes sense tha-"
    Tako "Nah, I'm just messin with ya. I'm going for an engineering degree."
    Tako "I mean, I'm a sick guitar player too, I just {i}really{/i} like building stuff."
    MC "Yeah, that's... cool."
    Tako "..."
    MC "Um, hey do you-"
    Tako "You're so damn lucky."
    MC "Huh?"
    Tako "..."
    "Though she seemed severe at first, she smiled and then gave a little peace sign."
    Tako "Naah, ain't no luck involved. Your fortune is aaalll me, babe."
    Tako "If you knew what was comin', you'd be worshiping me right now for hooking you up."
    MCT "What is she talking about?"
    MC "Hooking me up?"
    Tako "Yeaaah, a lil' bit of heaven. It's why I'm stayin' at a friend's tomorrow."
    MC "You are?"
    Tako "Yep! I mean, it ain't as comfortable as my room, but hey, if it's for Shiori-chan, I'm cool with it."
    "She shrugged and leaned back in the bench, resting her hands behind her head. A bit later, the waitress walked over with our cups, and placed them in front of us."
    Tako "I've done a lot for that girl, the love advice, the distraction, the list, all kinds o-"
    MC "The list?"
    Tako "..."
    Tako "She was, uh... a bit down in the dumps, to be honest. Back when she had an eye for you, hoo boy, she wouldn't shut the hell up about how she 'Wasn't the ideal beauty an upright man deserved.'"
    Tako "Sooo... I maybe kinda sorta helped a couple of dudes write a list of the hottest girls in school."
    MC "...It was you?"
    Tako "Tch, no! I just like... maybe stirred the pot in her favor a bit. Told a couple of guys... maybe she'd put out a bit more if we let her know she's hot."
    Tako "I mean, would I be in the top five otherwise? Kehehehe."
    Tako "*Sssp*"
    MC "That's... kind of manipulative."
    Tako "But you agree with it, don'tcha?"
    MC "I mean..."
    Tako "See? I'm a good friend. The result matters, not what you do to get it."
    MC "..."
    Tako "*Sssp*"
    Tako "Mm, goddamn. This is some good coffee, my dude."
    MC "O-oh, uh, yeah, that one's Shiori-chan's favorite."
    Tako "And here I thought she had shit taste in everything, am I right?"
    MCT "That's... not a nice thing to say."
    MC "..."
    Tako "..."
    Tako "Did y'all bang yet?"
    MC "...What?"
    Tako "What do you mean 'what'? I wanna know if you two got it on. If you hit that dank tush, my boy."
    MC "I-I don't-"
    Tako "Ay, ay, dude... I'm just playin. I know you didn't."
    "Her usually playful and goofy grin resurfaced, but in my current state of mind it seemed less like a gesture of friendliness and more like an open insult."
    Tako "Nah, with that weak stutter and unreliable personality, I doubt you've even had sex yet."
    MC "That's none of your business!"
    Tako "None of my business? I'm Shiori-chan's roommate, it's my job she doesn't end up with some spineless wimp."
    MC "Well, Shiori-chan doesn't think I am, so that's good enough for me."
    Tako "..."
    Tako "C'mon. I know what you want, dude."
    MC "What I... want?"
    "Yureno-san was gone. Whoever I was talking with was a far cry from the carefree and laid back girl who I walked in with."
    stop music
    Tako "Don't play dumb. Shiori-chan says she knows people, but I know people in a way she could never understand."
    Tako "I know you're actually a huge liar."
    MC "Liar?"
    Tako "You act all humble and afraid to step on anyone's toes, but in reality you're just a massive perv."
    if getSkill("Academics") > 10:
        MC "Oh yeah?"
        Tako "Yeah. I don't know many 'nice guys' who'd tag along with a girl who's so cold to them."
        MC "Well... I don't know any 'punk queens' who wear seventy thousand yen designer underwear either."
        Tako "..."
        "Any emotion had completely faded from Yureno-san's face. She stared at me in a way I'd seen a thousand times by now. She was analyzing me. Studying me. It was unnerving coming from her, to say the least. Like the girl I've known till now-"
        Tako "Oi, were you staring at my ass earlier?"
        MC "Gch!"
        MC "U-um..."
        Tako "HAHAHAHAHAHA! Oh man, for reals!?"
        Tako "Hey, what can I say, I can't help myself; I just reel ALL the boys in!"
        Tako "But y'know... it {i}does{/i} kind of prove my point~"
    Tako "You just wanna get with her because of her huge ass."
    MC "T-that's not-"
    Tako "Well, y'know... I have a huge ass too. Weeell... not as big, but..."
    Tako "If you wanted, you could leave her alone, and start gawking at *my* ass instead."
    MC "Stop it."
    Tako "Hm?"
    MC "It's not about her body. It's about her. Yeah, her ass is nice, but there's more to her than that."
    MC "I... {i}believe{/i} in her, I guess."
    Tako "...Are you deadass? That's the kind of shit that won her over?"
    MC "Call it what you want, but you're not changing my mind."
    Tako "Tsh..."
    Tako "Man... what a pain."
    Tako "Alright, well, I guess I got no other choice."
    "She slunk back in her booth, and exhaled audibly through her nose, for some reason forlorn."
    "Suddenly, her forlorn gaze turned into a wiley grin as she held her cup up and nodded with a wink."
    Tako "I'm with you all the way, my dude. I can't think of anyone better for Shiori."
    Tako "Take good care of her, aight?"
    "Taking another drink of her coffee, she looked over to the Kazoku-mart across the street and..."
    play music Busy
    Tako "MM!"
    "Suddenly, and excitedly, she put down her cup and stood up from the table."
    Tako "Yo! Let's bounce. It was really good and all, but I think we should head back."
    MC "Huh?"
    MCT "S-so suddenly?"
    MC "Um... okay, but we should probably pay for-"
    Tako "I'll pay."
    "Yureno-san began waving her hand in the air, and motioned to our waitress."
    Tako "Oy, we're ready! How much is it?"
    Waitress "O-oh. Um, it should be about-"
    Tako "Here you go. Keep the change."
    "She looked at the money slapped on the table. The waitress's eyes widened in shock."
    Waitress "...Ah! M-m-ma'am, this is-!"
    Tako "Yeah, yeah, whatever. Keisuke, let's head out."
    MC "Huh? W-wait!"
    Tako "This is going to be hilarious."

    scene Town with fade
    MC "D-did we just dine and dash?! What was that? Why did that waitress-?!"
    "I didn't continue my question, because I could tell it would fall on deaf ears. Yureno-san was grinning ear to ear, enveloped in whatever situation she's seeing unfold."
    "We stopped in front of the Kazoku-mart, and just waited until out from the door came..."
    show Tako neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show AE embarrassed at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    MC "S-Shi-"
    Tako "Oy! Shiorear!"
    show AE neutral
    AE "Hm?"
    show AE surprised
    AE "H-Huh?!"
    "Upon seeing the two of us, Shiori-chan nearly dropped her bag in shock. Yureno-chan merely waved, and smiled a wide, toothy grin."
    AE "K-Keisuke-kun?! What is... what on earth is-?!"
    show AE angry
    AE "Y-Yureno-san! I told you-!"
    Tako "Whaaat? I looked after him, didn't I?"
    show AE neutral
    AE "Ngh-!"
    Tako "We just stopped and got some coffee, no big deal."
    show AE angry
    AE "Y-you were SUPPOSED to keep him-"
    MC "Shiori-chan? What's going on?!"
    show AE embarrassed
    AE "O-oh, um..."
    Tako "Keheheheheh, *that's* a secret, lover-boy."
    "She darted towards Shiori-chan quickly and grabbed the bag in her hands, causing Shiori-chan to recoil."
    Tako "So is this bag."
    show AE angry
    AE "Y-Yureno-!"
    Tako "Relaaax, I'm takin it back home. I just wanted you two to walk home together as a couple.~"
    AE "..."
    Tako "See ya there!"
    "She walked towards me, but leaned in and whispered softly."
    Tako "Oi, Keisuke. Good luck!"
    hide Tako with dissolve
    "Yuren-san skipped off towards the valley home, leaving Shiori-chan fuming. We stood there for a while, speechless until I finally spoke up."
    MC "Shiori-chan, what was that about?! What's going on?"
    show AE embarrassed at center with dissolve
    AE "I... I can't tell you right now."
    MC "Why? Don't you trust me to-?"
    AE "I'm sorry. I just can't. L-let's head back to the school."
    "Shiori-chan's face was bright red, and she was fiercely shaking. I could tell that now was not the time to try and push her any further."
    MC "...Okay."
    stop music
    
    scene black with fade
    "We walked out of town together, and through the valley back to the school. I pulled her in close, and yet she still seemed somewhat distant."
    
    scene Dorm Exterior with fade
    play music Rain
    "We made it back in time for curfew. Yureno-san made it back by quite a bit, as it sounded like she was playing music loudly behind the doors."
    MC "Ah, she's home. Causing a racket as usual, eheh."
    show AE embarrassed with dissolve #nervous
    AE "..."
    MC "..."
    AE "Um..."
    MC "Hm?"
    AE "Tomorrow night... meet me in my room tomorrow night."
    MC "Like... after classes?"
    AE "N-no. After curfew, at midnight. You have my express permission!"
    MC "What?! *You* want me to break curfew?!"
    AE "Shhh, shhh... I'm not happy about it, but it can't be helped."
    AE "Please."
    "There was a desperation in Shiori-chan's eyes. I could tell that this was something serious. Something that weighed on her very soul."
    MC "...Okay. Okay, yeah, sure."
    show AE sad
    AE "O-okay... tomorrow, then."
    MC "Tomorrow."
    "She nodded, and then slowly entered her room, and closed the door behind her."
    hide AE with dissolve
    AE "HOW DARE YOU!?"
    Tako "Whaaat?~"
    "I heard the two bicker as I walked away. In retrospect, I got the opposite of what I came to her room for. I was just more confused and worried."
    "The fact of the matter is, though, that nothing could prepare me for what would happen tomorrow."
    jump daymenu

label AE050:
    $setProgress("AE", "AE051")
    $setSize(4)
    #SCENE NIGHTTIME
    scene Dorm Interior with fade
    play music Rain
    "The room was completely silent, save for Daichi's soft breathing as he slept. The only source of light in the room was the bedside alarm clock, the faded glow illuminating the far side of the room."
    "I stared at the red numbers as my eyes adjusted from the darkness. 11:45. Almost midnight."
    "Unclear of my motive, I slowly pulled the covers away and, as meticulously as I could, got out of my bed without a sound. Not wanting to waste time to change, I'd gone to bed with my clothes on."
    "Silently, I crept through the room as to not wake Daichi. I reached the door, slowly unlocking and opening it to the darkness of the empty hall. I turned around once more to ensure that Daichi wasn't watching."
    MCT "If whatever is going on is important enough to warrant Shiori-chan asking me to break the rules, then I think this should be private."
    
    scene Dorm Exterior with fade
    "I stepped out of the room and closed the door behind me. With no hallway monitor out and about, all I needed to do was make sure that I didn't wake any of the other students or on site faculty."
    #FOOTSTEP SFX
    "Though it was dark, the moonlight from the windows was able to guide me well enough through the hallways. It took some time, but eventually I made my way to the girls dorm."

    scene Dorm Exterior with fade #girl's dorms
    "As I entered the main hallway of the dorms, I began to tread even more lightly. Getting caught here after hours would be disastrous."
    "Finally, I managed to climb the stairs and reach the top floor. I made my way over to her door at the end of the hall. With the back of my knuckles, I made the lightest knock I could muster."
    MC "Shiori-chan, you awake?"
    "I spoke lightly as to not alert anyone, but after a minute or so of no response, I was worried she hadn't heard me."
    "Then the door creaked open."
    MC "Hey-"
    show AE sad with dissolve
    AE "Come in."
    MC "Oh, yeah, yeah."
    "I entered briskly as Shiori-chan slowly closed the door."

    scene Dorm AE with fade
    "As I entered, I noticed that the room was not immediately dark, but that the lighting had been dimmed down. Yureno-san's side of the room had been made completely spotless... and she was nowhere to be found."
    MC "Hey, what's going on? Is everything-?"
    show AE sad with dissolve
    AE "No need to whisper. The walls are thick, no-one will hear us."
    "I looked back at her and looked her up and down, just as she has been for the past few days, her knees seemed weak, her demeanor less severe, her posture no longer upright... and of course, it was impossible not to notice her gargantuan ass, which had almost completely stretched out and ripped her skirt."
    AE "Any problems getting here?"
    MCT "She's not looking me in the eyes... something's wrong."
    "She was right. The walls must have been thicker than stone, because the inside of the room made the empty halls of the school seem like a concert in comparison. Everything was neat, the sheets were pressed, and the air freshener in the room secreted a fragrant, sweet smell."
    MC "Nah. I didn't tell Daichi about any of this, and the hallways were emptied out."
    AE "That's good, that's good..."
    "She continued to avoid my gaze as she solemnly walked over to her bedside and sat down, eliciting a heavy groan from the boxspring. She looked over to me finally and, reaching as far as she could over her thighs, patted the spot next to her."
    show AE neutral
    AE "Please, sit down."
    "As I did, my hand brushed against her thigh flesh, causing her to inhale a bit. I pulled my hand away and put it in my lap... only for her to grab hold of it and put it back in its original position."
    MC "Shiori-chan, you never even told me what's going on."
    AE "Keisuke-kun..."
    AE "There comes a time in every woman's life..."
    show AE sad
    AE "No, no, that's not..."
    AE "Ehm..."
    "Her hands were clammy, and quivered as they grasped on tightly to my own."
    show AE neutral
    AE "A-As you can surmise from our recent interactions, I've been... um..."
    "She released my hand and stood up, looking down."
    show AE sad
    AE "..."
    MC "..."
    AE "I don't know how to say this to you. I don't know what to say. It's like my brain is f-filling up with fog, and I... I just don't want to mess this up."
    AE "Because... I want to make it clear to you... as clear as I possibly can..."
    stop music
    "Shiori-chan slowly placed her hand on my thigh."
    AE "I truly care about you."
    MC "..."
    AE "..."
    "We stared in each other's eyes. As I looked on at her pink, panting visage, I could feel my heart skip a beat. I didn't know what to say, nor what I could have said. All I knew in that moment, was that now was the time."
    "I leaned in, and she followed suit..."
    play music Steamy
    MC "Mmm..."
    show AE embarrassed
    AE "Mmn.~"
    "As we kissed, I felt the warmth of her hand gently caress my face. I grabbed her waist and pulled her in even tighter as we started to rock back and forth together."
    "Now realizing the true reason why I'd been called to her room so late in the night, I decided to take a chance, as I grabbed two handfuls of that plump ass."
    AE "MMMM!"
    MCT "Ah! W-Was I wrong to-?"
    AE "Mmm~"
    MCT "...No... No, tonight is the night."
    "My hands squeezed and massaged her fat behind, each squeeze feeling like my hands were sinking deeper into her warm, jiggly flesh. Travelling down, my hands explored her ass all around, leading to small, muffled yelps from Shiori-chan."
    "I finally broke our kiss, and placed my hands on the inside of her skirt rim. I started to kneel, as I slowly pulled down her skirt. Once they were on the ground, I looked up at her..."
    MC "W-Woah!"
    "As she lightly pushed me onto my ass with her foot. I recollected myself as she stood over me next to the bed frame. She crossed her arms and stood with her legs spread, a look of disdain showing clearly on her face."
    if getFlag("AE024_grabbedass"):
        MCT "Shit! Did I mess up again?!"
    else:
        MC "H-Huh?"
    AE "H-... H-Heel dog!"
    MC "Huh? Dog?"
    AE "T-That's r-r-right. I'm going to show you w-what a real woman l-looks like!"
    MC "What a real woman- huh?"
    AE "Y-Yeah! And who knows... if you stop being a... a, um... s-sniveling pile of garbage, maybe you'll get this!"
    "Shiori-chan reached into her shirt pocket, and held up a small package into the air."
    "A condom."
    MC "Ah!"
    MCT "So that's what she was buying at the store!"
    AE "Tako helped me... When I asked her to distract you, she was reluctant, but... she m-made this all possible."
    AE "W-Well? What do you have to say, vermin?"
    if getFlag("AE003_c1_1"):
        jump AE050_assertive
    else:
        jump AE050_passive

label AE050_assertive:
    "A sly smirk crept across my face, and I looked up at her with a loving smile."
    MCT "Alright. If you want to show me, then show me."
    MC "Yes, mistress. What must this lowly dog do to please you?"
    AE "U-Um..."
    "Shiori-chan looked around the room, clearly she hadn't planning for this part."
    AE "How's about... um..."
    AE "K-Kiss my feet, cur!"
    MC "As you wish, mistress. Please, have a seat."
    "I got on my knees and did as she asked. Pulling off her sock gently, I noticed her leg was trembling and her toes were curled. Looking up, I caught her nervous gaze, and watched as she quickly tried to put on a domineering face."
    AE "W-What's the matter, scum? Are you going to... u-um... e-ejaculate from my feet alone?!"
    MCT "Ejaculate? Is that the best she can come up with? Furthermore, what kind of kinky shit does she think I'm into?!"
    AE "Go on, grovel at my feet, and I'll reward you."
    "Following her command, I lightly pecked the very top of her ankle."
    AE "Eep!"
    MC "Hmm~"
    "My lips travelling further, I watched her quiver as I slowly, methodically planted a kiss to her inner thigh. I moved my head even closer, feeling the heat emanating from behind her dark blue panties, I could hear her begin to pant."
    MC "May I go further, mistress?"
    AE "A-Ah!"
    AE "You... You may."
    "A confident grin forming on my face, I spread my arms out across her wide hips to grab the sides of her panties; which had dug in deep to her pillowy leg flesh. Nibbling the top of her panties with my teeth, I reared my head and hands back as I slowly peeled away the blue cloth."
    "There it was. Her pussy was in full sight. Her labia was puffy, and even now looked dripping wet. Though I'd dreamt of plowing her many times, this was the first time I'd ever gotten to see her exposed like this."
    MCT "Keep it together. Don't mess this up for her OR you."
    MC "Aha, I-I see you take good care of yourself."
    AE "I've n-never been touched down there..."
    MCT "...What?"
    MC "Not even by yourself?"
    AE "N-No. I mean, I clean myself, but... d-does that count?"
    MC "You've never masturbated {i}in your entire life{/i}."
    AE "Never."
    MCT "Holy shit, that... explains a lot."
    MC "Alright then..."
    MC "Let me teach you how, mistress."
    "Her legs began to quiver even more as my fingers slowly reached her slit; until finally..."
    AE "A-AAAHHN~!"
    "Penetration."
    MC "You see, mistress, I know you're smart enough to know the anatomy of the female genitalia, but it's truly a marvel how much it can feel."
    AE "Haaahn- Aaaghn!"
    MC "For example, you know this part, right?"
    AE "Ahn! Uhgg-!~"
    MC "This is the labia. It's the soft lips that work as the entrance."
    MC "And thiiss-"
    AE "Mngaaah!"
    MC "Would be the clitoris."
    MC "And when I push my fingers in and out-"
    AE "Uu-Uu-Uuuu~"
    MC "It simulates penetration, see?"
    MC "Aren't you learning so much mistress?"
    AE "Nng! A-Ah~"
    MC "And if you do it right..."
    "I pulled my fingers out of her box, and brought my mouth closer."
    MC "It should feel something like this."
    jump AE050_after1
    
label AE050_passive:
    MC "U-Um, Shiori-chan?"
    AE "That's m-mistress to you!"
    MC "Er, right, mistress."
    MC "Are... you doing this because it's what you think *I* want, or because it's what *you* want?"
    AE "..."
    AE "W-Why do you ask?"
    MC "I, uh... I can tell that being dominant in bed doesn't come naturally for you."
    AE "Oh."
    AE "Well, then..."
    AE "What is it you want?"
    "I stood up and looked in her eyes softly, my hand gently caressing her face as my other wrapped around her waist."
    MC "I just want you, in this moment. Just you."
    AE "..."
    AE "*Mmph~*"
    "I pulled her in for a kiss, and then we finally began properly. No masters, no mistresses, no expectations; just us."
    "We stayed in that kiss for a moment, however. Her soft lips and warm tongue sent waves of warmth throughout my body as we swayed together."
    "I pulled away and looked her once more in the eyes, pale moonlight from the window bouncing off the lenses of her glasses."
    AE "S-So, um... that was my plan... um... how do we begin."
    MC "How do we begin?"
    AE "Y-Yeah."
    MC "Um..."
    MC "I don't know. I'm a virgin."
    AE "Y-You too?!"
    MC "Yeah. I mean, I got close one time but... yeah."
    "The silence of the room left us stirring in our thoughts and anticipation. Shiori-chan rubbed her thighs together as she shuffled about in place, for the first time since I'd known her appearing antsy, uncollected, and uncertain."
    AE "Is-Is that okay?! Can I really take your virginity?!"
    MC "Yeah. If anyone should, it should be you."
    AE "...Alright."
    MC "So, um... how's about this-"
    AE "Hm."
    MC "Here... let me get these."
    "Slowly, I positioned myself between her legs. She let out a gasp as I grabbed her panties. I looked up to her, and she nodded. I pulled them down, my confidence steeled by my desire to please her."
    "There it was. Her pussy was in full sight. Her labia was puffy, and even now looked dripping wet. Though I'd dreamt of plowing her many times, this was the first time I'd ever gotten to see her exposed like this."
    MCT "Keep it together. Don't mess this up for her OR you."
    MC "Aha, I-I see you take good care of yourself."
    AE "I've n-never been touched down there..."
    MCT "...What?"
    MC "Not even by yourself?"
    AE "N-No. I mean, I clean myself, but... d-does that count?"
    MC "You've never masturbated {i}in your entire life{/i}."
    AE "Never."
    MCT "Holy shit, that... explains a lot."
    MC "Alright then..."
    MC "Okay... Ready?"
    AE "Y-Yeah. What, um... what are you gonna do?"
    MC "...This."
    jump AE050_after1
    
label AE050_after1:
    "Ready to begin, I began to lap away greedily at her warm pussy."
    AE "AHN! Mmm~!"
    "I slowly ran my tongue along her folds as she began to lightly buck her hips a bit."
    MC "Mmph~"
    "With one hand resting and sinking into her thigh, and another lightly toying with her labia, I then went for the kill, and lightly teased her clit with the tip of my tongue; moving it in circles."
    AE "OOOOH~!"
    "At the sudden surge of pleasure, she brought her legs together; trapping my head between her fluffy, warm legs. Arching her back, she grabbed my hair and drove it further in."
    "Her knees quivering as my tongue works its magic on her, the long locks of hair in front of my face tickling her most sensitive regions."
    AE "Ah, A-ah~! MMmm~!"
    MC "Mmm, mmm~"
    "As I lap greedily away, Shiori-chan, no longer mindful of where she is, or even who she was for that matter, grabbed a handful of my hair, driving me deeper into her, and her deeper into lust."
    if getFlag("AE003_c1_1"):
        jump AE050_assertive2
    else:
        jump AE050_passive2

label AE050_assertive2:
    MC "Mmm... Mm? Mm!"
    "Finding my nose covered by her fat thighs, I found myself struggling to breathe. I tapped her leg, and as her vagina began to moisten even more she finally released my head from between her legs."
    AE "Ahn... Ahn!"
    MC "*Pant* *Pant* Hah, couldn't breath for a second there."
    AE "W-wait! I haven't-! I-I was almost about to-!"
    AE "Keisuke-kun... I need... I need more. I was just about to..."
    AE "Please... you can-"
    MC "Don't... hah... get ahead of yourself."
    AE "H-huh?"
    MC "Remember what you said? If I do a good job, you'd reward me, right?"
    "I climbed onto the commodious bed next to her and took my shirt off, and watched as Shiori-chan ogled my bare chest. I beckoned her closer, and further onto the bed."
    MC "Well, mistress? May I receive a reward?"
    AE "W-What would you, um... l-like?"
    MC "Suck my dick."
    AE "Huh?!"
    "She reacted with shock at my language, but I watched her eyes widen and her mouth water at the prospect of it."
    "She got closer to me on the bed, and nestled between my legs; kneeling."
    AE "I-I supposed you've earned it."
    AE "Okay, haah... please pull it-"
    AE "A-Ah! No, I c-command you to pull it out!"
    MC "Yes, mistress."
    jump AE050_after2

label AE050_passive2:
    MC "Mmph, Mmph~"
    AE "Hahn! K-Keisuke-kun... ugh!~"
    "Finally, and abruptly, she began to cum as she released a steady moan. I pulled myself away, panting and out of breath."
    MC "Wow... Hah..."
    AE "Haahh..."
    MC "So... me next?"  
    AE "Huh?"
    MC "Do you wanna... do me next?"
    AE "Ah! Keisuke-kun, you don't have a... you know."
    MC "H-Huh? Oh! No, I meant, like... a blowjob?"
    AE "O-Oh! Um... okay, so... I guess that means I get to see your..."
    MC "Yeah."
    AE "Yeah."
    AE "Alright... Unzip them."
    MC "Right. Got it."
    jump AE050_after2
    
label AE050_after2:
    "She looked on in anticipation as I slowly, methodically, unbuttoned my pants and pulled down my zipper; my boxers only slightly hiding my raging erection. My heart beat heavily in my chest as I did. Though it had been this whole time, I could feel it now more than ever."
    "Shiori-chan jumped back a bit and gasped, her eyes widening as my cock sprung out of the hole in my boxers."
    AE "H-Haaah~"
    AE "K-Keisuke-kun's p-p-penis... it's-"
    if getFlag("AE003_c1_1"):
        MC "All yours, mistress."
    else:
        "My face began to blush a deep red as she stammered. I put on a weak smile and tried to avoid her gaze."
        MC "Y-Yeah."
    AE "Hah..."
    AE "I-I didn't think it would be t-t-this big."
    MCT "Thanks for the vote of confidence, Shiori-chan."
    "After a moment of staring at it, she gave it a little poke with her finger. After another, she wrapped her hand around my dick and began to lightly stroke."
    AE "How do I, um..."
    MC "Just like that."
    AE "Oh, okay."
    MC "Mmn..."
    AE "R-Right, um... felatio. I um... I r-r-read up a bit on it."
    AE "Hoookay, you can do this..."
    "She took a deep breath in, and then after planting a few tiny kisses to the tip of my dick-"
    AE "HHRGK!"
    MC "Ahn!"
    "Shoved the whole thing down her throat."
    "Eyes darting open in shock, she pulled away and began to cough her lungs out and gag."
    AE "*Kaff* Pagh- *Kaff*"
    MC "You alright?"
    AE "Y-Yeah. Let me just try something."
    if getFlag("AE003_c1_1"):
        jump AE050_assertive3
    else:
        jump AE050_passive3

label AE050_assertive3:
    "She balled up her fist around her thumb and took a few breaths to calm herself. With her other hand, she gently wrapped her hand around my shaft and placed the head in her mouth; slowly sliding down further and further as she bobbed her head."
    AE "*Mmph* Mmmh~"
    MC "Oh fuck... ahn..."
    "Grasping her hair, I guided her head on instinct, and pulled her in further."
    AE "Gch!"
    "Her mouth engulfed my shaft as a small gasp escaped me. It was warm and inviting, I couldn't stop my muscles from twitching as the tip of her tongue flicked the helm of my rod."
    "The crown of my cock was assaulted by her twirling tongue; her lips making a perfect suction as it gripped my length. Each pull moving the skin while her tongue kneaded the underside."
    AE "Mmph, mmph, mmph."
    "She increased her speed as best as she could, her head bobbing back and forth; rocking her whole body with her movements. Looking past her head, I noticed her immense booty as it quaked with every rhythmic movement of her head."
    MC "H-Haaahn~"
    "This flipped the switch in me as I grunted and my muscles contracted. My balls seized up and tensed as a flood of my seed sprayed her mouth. I saw her eyes widen as she her cheeks puffed up with my load. She pulled her head away from my cock, and covered her lips with her hand."
    AE "Mmph!"
    jump AE050_after3

label AE050_passive3:
    "She then took a surprising turn when she ended up moving my body down a bit on the bed till I was laying down, she then hovered her gargantuan, jiggling ham-hocks over my face. Given how big it was, both cheeks brushed my own as I began to turn bright red."
    AE "I-I hope you don't mind, I just think t-this might be more comfortable... are you okay with this?"
    MCT "S-She wants to sit on my face? Huh..."
    MC "W-Well  it's, unexpected  but, just as long as it makes you comfortable."
    "She saw my warm smile and felt my warm words put her at ease as she wiggled her gargantuan hips and was about to sit on my face."
    AE "D-Dont worry, I'll try to be gentle."
    "She slowly lowered herself down, her soft warm flesh engulfing my face with her two massive cheeks smushing it in-between. She lowered a bit more and more until her whole weight of her ass was comfortablely on my face, my warmth of my face seeming to make her shiver a bit."
    AE "A-ahn.. you feel... really nice down there..."
    MC "Mmm~"
    "Preparing for a second try at my cock, she balled up her fist around her thumb and took a few breaths to calm herself. With her other hand, she gently wrapped her hand around my shaft and placed the head in her mouth; slowly sliding down further and further as she bobbed her head."
    AE "*Mmph* Mmmh~"
    MC "Mmph!"
    "Gasping for air, I buried my face further between her cheeks, my hands squeezing her ass tightly,"
    AE "Gch!"
    "Her mouth engulfed my shaft as a small gasp escaped me. It was warm and inviting, I couldn't stop my muscles from twitching as the tip of her tongue flicked the helm of my rod."
    "The crown of my cock was assaulted by her twirling tongue; her lips making a perfect suction as it gripped my length. Each pull moving the skin while her tongue kneaded the underside."
    AE "Mmph, mmph, mmph."
    "She increased her speed as best as she could, her head bobbing back and forth; rocking her whole body with her movements, including her ass which wobbled like mad. In the heat of the moment, she pressed her hips harder into my face, clearly getting a sense of enjoyment from the sensations it brought."
    MC "H-Haaahn~"
    "This flipped the switch in me as I grunted and my muscles contracted. My balls seized up and tensed as a flood of my seed sprayed her mouth. Her eyes widened as her cheeks puffed up with my load. She pulled her head away from my cock, and covered her lips with her hand."
    AE "Mmph!"
    "She then lifted up her massively plump rear carefully and slowly, so that I was able to pull myself out from underneath her. I was a bit stunned, but afterwards I got a good look at her face and chuckled a bit."
    jump AE050_after3

label AE050_after3:
    MC "Hah... Sorry, I guess it's been a while."
    AE "Mmmgn..."
    "She seemed to cringe a bit at the bitterness of my cum, her cheeks making her seem reminiscent of a chipmunk. But as I was about to make a joking comment on it... that's when I heard her do it."
    AE "*GULP*"
    "I looked on in shock as Shiori-chan not only swallowed her first blowjob rather than spit, but as she did so to the biggest nut I'd busted in a long time. Cum dribbled down her chin as she did her best to gulp down the bitter fluid. After two gulps, she opened her mouth and gasped."
    AE "Pah-*urp*-ahgn..."
    MC "Holy shit."
    AE "I... ah... d-didn't want to get anything on my bed."
    MC "Wow..."
    MC "Say... I think that shirt looks a bit restrictive."
    AE "Y-Yeah?"
    MC "Mhm..."
    MC "Here. Let me help."
    "Slowly, I reached over and began to undo the buttons of her shirt. First at the bottom, then the second, then the third up. Slowly but surely, her shirt, jacket, everything came off; until she was left in only her bra."
    MC "Hmm~."
    "I pulled her in closer, and embraced her with a hug and a kiss. My hands rubbing her back, I leaned in and whispered in her ear as I reached her bra."
    MC "May I do the honors?"
    AE "M... Mhm."
    "I grabbed the metal hooks that attach to the blue fabric and I unhooked them, one by one."
    "The first."
    "The second."
    "And the third."
    "Shiori-chan put her arms out as my heart pounded in my chest. I pulled her bra away and got a look at her cute tits."
    "They weren't big, but they were sure as hell beautiful. I watched her chest as she began to breath deep."
    MC "Wow."
    if getFlag("AE003_c1_1"):
        AE "S-Sorry. They're nothing to call home ove-"
        "Before she could finish, I lunged forward and pushed her down onto the bed as I began to lick her nipple."
        AE "-ER! HAAHN~!"
    else:
        AE "S-Sorry. They're nothing to call home over."
        "I sauntered over to her and pulled her in, her naked chest pressing against mine; soft flesh and skin titillating every nerve in my body."
        MC "They're perfect."
        "I placed my hands on her shoulders and kissed her once more. As we kissed, I took the time to let my hands explore her naked body. Each inch of smooth, pale skin caressed my hands as I ran them across her slender waist."
        "My hands were stopped, though, by her ginormous hips, into which her waist flowed seamlessly. I ran my hands along the curvature of her hips and found my hand resting on her naked asscheek. A grabbed a handful and began to walk forward towards the bed. My throbbing manhood pressing against the crux of her waist, she followed suit."
        "I gently guided her body down onto the bed as I began to lick her nipple."
    "She placed one hand on my head, another biting the finger as she released tiny moans. I traced her small, pink nipples with the tip of my tongue and then looked up at her."
    AE "Ng-Ahh!~"
    MC "Pah, ah... nonsense. They're wonderful."
    AE "Mmm~"
    "As Shiori-chan lay naked on the bed, I hopped off and picked the condom off the ground. My cock fully erect and exposed, I pulled it out of the package and began to roll it over the head."
    "As confident as I tried to sound, I only ended up stuttering as I thought over the prospect of finally losing my virginity."
    MC "R-Ready?"
    AE "Y-Yeah..."
    MC "Okay!"
    "I rolled the condom down to the base. A snug fit, but it worked. I began breathing heavily as I pressed my cock right on Shiori-chan's slit. She bit her lip as her eyes widened... and then she whimpered."
    MC "Fuck... your pussy's so warm."
    AE "..."
    AE "W-wait."
    MC "Huh?"
    AE "Don't... don't put on the condom."
    MC "W-What?"
    AE "I..."
    AE "N-nevermind. Forget I said anything."
    "My mind clearing up for the first time in this dance of love we were doing, my heart skipped a beat as I could see the sorrow in her face."
    MC "Wait, no, that's not really a 'nevermind' kind of thing. You don't want me to put a condom on?"
    AE "...N-No. I don't."
    MC "I mean... what if you get pregnant?"
    AE "I know, it's just... what if there's a chance it will fail?"
    MC "Well, the risk's always there, I guess."
    "She sat silently and pondered, as she is often to do. She brought her thumbnail up to the teeth and bit down, a telltale sign of her internal struggle."
    MC "What now? It's your call."
    AE "..."
    AE "F-Fuck me in the ass!"
    MC "EH?!"
    MC "W-Wait, wait, you wanna go for that already?"
    AE "After weighing all the options, I... I just feel like I'm ready for that before... um... vaginal."
    "I wasn't sure what to say. Generally, anal is usually reserved for more experienced couples. But still, I could tell by the look on Shiori-chan's face that she was absolutely sure of this."
    MC "Sure thing. Let's start with that and see how everything works out."
    AE "Y-Yeah..."
    if getFlag("AE003_c1_1"):
        MC "That makes me wonder, though... you said your ass was getting sensitive?"
        AE "Mhm."
        MC "Maybe you planned it out so that you could have an excuse for us to do anal, then?"
        AE "N-Not at all!"
        MC "I wonder... is your ass more or less sensitive than your pussy?"
        "The sight of her beautiful, jiggling butt cheeks begging for my touch caused my face to go hot and my hands to sweat."
        MC "You said it yourself. You've been feeling *extra* sensitive back there, right?"
        MC "Maybe it's high time we test that out.~"
        "I playfully gave her tush a little smack with my hand-"
        AE "HAAAH!"
        "And Shiori-chan's eyes widened as she let out a gasp."
        MC "...Huh?"
        MC "Wait... you reacted the same way in the clocktower..."
        AE "Ahn... U-Um..."
        "A wily smirk slowly spread across my face as I crawled over to her on the bed."
        MC "I think we've found your fetish."
        AE "H-HUH?!"
        MC "Well, I mean, you can deny it... but how about we try {i}juuust{/i} to make sure."
        MC "Here."
        "I kneeled on the bed, and patted my knee."
        MC "If you wanna try it, just bend over my knee. If not, we can skip right to the main course."
        AE "I..."
        "Just as I predicted, her usual steadfast resolve couldn't keep hold. She gave into temptation, and submitted; kneeling over my knee."
        AE "Please s-s-spank me!"
        MC "Oooh? So forceful. What a naughty girl.~"
        AE "Y-Yes! I've been naughty, please, I deserve it!"
        "While what part of me that was still in conscious thought questioned if she should see someone about what she just said, the fact that the tip of my dick was rubbing against her plump rump superseded that."
        MC "Mhmm~"
        "I took my middle finger and ran it gently, slowly, through the crack of her ass, sending signals of pleasure to her brain."
        AE "Ho yes, yes-"
        "I reached the top of her ass and then raised my hand up."
        AE "-yes, YES, YES, YES, YES!!"
        "And brought it down."
        "*SMACK*"
        AE "HAAAAHN!!!"
        "*Smack*"
        extend " *Smack*"
        extend " *Smack*"
        "Between each few spanks, I gently rubbed her jiggling backside, soothing the area to make it more sensitive for the next hit."
        "*Smack*"
        AE "Uu-uu-uu-UU-UU-UU~!!"
        "Her eyes became pinned as I continued, and her breathing was ragged and erratic. Her vocalisations rose it pitch as her situational awareness dropped to zero."
        AE "HARDER, HARDER, PLEASE-PLEASE-PLEASE!! OOOHH!!"
        "*SMACK*"
        AE "HAAAHN~"
        "I continued to pummel her mind with senseless pleasure as her moans echoed through the room. She nearly went cross eyed as my hand made constant, rhythmic contact with her asscheeks."
        "Soon, she began to cum as my spanks turned into a gentle massage."
        MC "Well, I guess that settles it. We found your fetish."
        "She didn't respond. Her whole body was shaking as her booty continued to wobble well after my barrage. Eventually, she began to settle down and cleared her throat."
        MC "Alright. I think that's about enough foreplay, eh?"
        AE "M-Mhm."
        MC "Alright, how's about you get on your knees, yeah?"
        AE "Y-Yeah."
    "We positioned ourselves on the bed. She kneeled down as I fully took my pants off; leaving the both of us now totally naked. I got a good look at her fat cheeks stuck in the air and put my hand on one, stroking my cock with my other hand."
    MC "Such a beautiful ass. Mmn~"
    "As each pale cheek eclipsed my view of the rest of her, I lowered myself and buried my head inside of her clenched thighs before feeling the soft, yielding flesh part for me. I began to run my tongue along her eager slit while feeling her legs quake around my head."
    MC "Mmph~"
    "After pulling back and gasping for air, I gripped the upper slopes of her curvaceous ass and began guiding myself toward her."
    MC "So... what do you say? Should I?"
    AE "Yes! P-Please!"
    "She bowed down into the bed, sticking her giant fleshy ass up and burying her head into the white sheets."
    AE "P-Please fuck me in the ass!"
    "I moved and positioned myself behind her, my dick harder than diamonds as the realization of my virginity being lost soon began to set in. I stayed as calm as I could as readied myself."
    MC "Ready?"
    "I slapped my cock on the inner curves of her buttcheeks as she shuddered."
    AE "Mhm..."
    "I felt myself press against the outer slopes of her gargantuan ass and nearly came right then from the sensation of being enveloped in such a warm embrace. Taking an extra moment to steel my nerves, Shiori-chan clearly felt the hesitation in my progress and decided to push back into my waist, burying myself even deeper within her."
    "Caught off-guard by her sudden forwardness, I pushed against her and felt my rigid cock press against her hole. Then, all at once, it entered."
    AE "Hooo-OOOOOOH!!!"
    "She began cumming as soon as I'd stuck my dick in, her tongue lolling out as a rich red took up most of her cheeks. Both the ones on her face, and the gigantic ones on her backside."
    AE "OOOOOOOHHHH~!"
    "Her hands scratched at the sheets to try and keep herself upright, but soon the strength in her arms gave way as well. She was left face-down, her butt wobbling all over like a broken bowl of pudding as I pounded into her, my entire body tensed up with strength I never knew I had."
    MC "Pah-Ngh!"
    AE "HAAAH, HAAH, AAAAGN!!!"
    "Settling into a slow rhythm of bouncing away and into her fleshy cushioning I could feel her tempo begin to increase as her body began to shudder from both the motion and her own skyrocketing arousal."
    "It was like she was caught in an endless ejaculation, each thrust forcing her to an even greater state of climax."
    "I started moving on instinct, stretching my arms around both cheeks as my tempo increased. The bed began to creak with every thrust as the movements of her massive body rocked the entire bed."
    "Her glasses fogged up, her mind in a foggy, pleasant haze, feeling my throbbing manhood thrust into her meaty backside over and over again."
    MC "Haah! Ngh! S-Shiori-chan... I'm gonna c-c.. Ah!"
    "I wasn't even sure she could hear or understand what I was saying, as she only responded with a few garbled moans. One last smack to her ass, and finally..."
    MC "Ha-Ha-Haah!"
    "The dam broke. I grabbed her arms and pulled her back, pushing my cock as deep as I could into her ass as I thrusted my hips a few more times."
    "My chest against her back, our hearts beating like mad together, I began to hyperventilate as I grabbed her waist with one hand, the other grabbing her chest and pulling her in as I bounced our bodys up and down together."
    MC "Hahn-*gch*-ahn!"
    AE "Ah... Ah... Ah..."
    "She twitched at every new pulse of cum that filled her cavity, her mind completely wracked by my dick as she stayed kneeled over silently. At the very least, her vice-like bum meant she didn't have to worry about any of my semen leaking out. Not that she'd have any chance of keeping the bed clean, however; everything under her was completely soaked."
    MC "Haaahn... ahhh..."
    "My energy completely spent, I slumped forward, grabbing her tight as I pulled her down with me."
    "Falling to the side, I could feel her panting as I pulled my member from her cheeks. She did her best to maneuver herself over her own ass to look me in the eyes."
    AE "Ahhn... Aaaahn~"
    AE "K-Keisuke-kun..."
    show AE happy
    AE "I'm so happy... you were my first..."
    "I smiled and gently caressed her face with my hand, wiping away her tear."
    "The last thing I saw as I slowly drifted off to sleep was Shiori-chan's smiling face; an image that burned into my mind, and would stay there forever. The last words echoing through my mind, but never escaping my lips:"
    "I love you."
    jump daymenu

label AE051:
    $setProgress("AE", "AE052")
    #SCENE MORNING
    scene black with fade
    AE "Mmn."
    #*Creak SFX*
    "The next morning, the deep creak of the mattress roused me from my sleep, my eyes opened slowly to the white ceiling above, and the calling of birds outside the window echoed through my head as a cool breeze rolled in from the newly opened window..."
    
    scene Dorm AE with fade
    play music Hallway
    MC "M-Mmmn."
    "I yawned as I wiped the sleep from my eyes, memories of last night still replaying fondly in my head. I almost began to wonder if it was a dream, until I looked over to my lover."
    MC "Haah, morning."
    "Clutching a book in her hand mere inches from her face, her other holding her bedsheet to cover her lower body, the light of the window through the white curtains shone down on her as though it were a natural aura of sheer radiant light that graced her skin."
    "She was extremely cute, she seemed down to earth and honest, she was someone..."
    "...Someone I'd never seen in my entire life."
    "The woman pulled the covers up to her breasts and shrunk back, looking at me as though she was at a loss for words. She had raven dark hair that obscured well over half of her visage, what I could see revealed a silver eye that conveyed a look of uncertainty."
    MCT "Who... who is this?"
    MC "U-um..."
    show AE nude-surprised with dissolve
    UNKNOWN "..."
    MC "Hi?"
    show AE nude-embarrassed
    AE "...Hey."
    "I raised my eyebrows as her familiar voice rocked me back to consciousness. It was Shiori-chan alright. I would've never expected her to look so different with her hair down, though morning haze may have played a part as well."
    MC "Hah, u-um, good morning."
    AE "Good morning, Keisuke-kun."
    MC "So..."
    MCT "What do I even say? 'That felt great'? 'Let's do that again some time'?"
    MC "How are you doing?"
    "Catching a glance at her book, it looked thick and somewhat old, bound with brown leather. The words, at first glance, looked like a foreign language, and the pages were marked here and there with yellow highlighting. Breathing through her nose, she closed her book and looked down."
    show AE nude-happy
    AE "I feel... I don't know how to describe it. I feel lighter than air."
    MC "Sleep well?"
    "I reached over to pat her leg under the covers, as my hands sunk into her smooth flesh, all doubt was removed, and replaced with a sense of content and a small amount of personal pride."
    show AE nude-neutral
    AE "I, um... I didn't get much sleep last night."
    MC "Eheh, yeah, me either."
    show AE nude-embarrassed
    AE "..."
    "She brought her knees up as far as her giant asscheeks would allow, her hands reaching out and sinking into her meaty calves."
    AE "Did I... do a good job?"
    menu:
        "You're a natural.": #-1
            jump AE051_c1_1
        "You were perfect.": #+2
            jump AE051_c1_2
        "I don't know.": #+0
            jump AE051_c1_3

label AE051_c1_1:
    MC "You were great!"
    show AE nude-happy
    AE "R-Really? I made you feel good?"
    MC "Without a doubt! I don't know why you're worried, you're a natural!"
    AE "Mhmhm~"
    show AE nude-neutral
    AE "..."
    $setAffection("AE", -1)
    "Shiori-chan's smile faded, she broke eye contact with me and just stared straight forward. After giving a slow gulp, she blinked and reared her head back a bit."
    show AE nude-embarrassed
    AE "A natural, huh..."
    MCT "...Oh my god I'm such an idiot."
    MC "Well, I mean, I wouldn't say {i}that{/i}. You were uh... you were special, to me, and... you know, it was like we were naturally meant to be."
    AE "Yeah. Naturally. This was bound to happen. Naturally."
    jump AE051_c1_after

label AE051_c1_2:
    "Scooting up next to her until our hips were touching, I wrapped my arms around her and buried my face in her hair, nuzzling her gently."
    show AE nude-surprised
    AE "Eh?"
    MC "You were perfect in every way."
    "She put her hand on my arm and looked up to my face, we stared each other in the eyes for a moment before she leaned in with a kiss."
    show AE nude-happy
    AE "Mm~"
    $setAffection("AE", 2)
    AE "Thank you, Keisuke-kun. I'm happy I was able to please you."
    jump AE051_c1_after

label AE051_c1_3:
    MC "I... I dunno. It was my first time, remember?"
    show AE nude-embarrassed
    AE "Ah, y-yes. Mine too."
    show AE nude-sad
    AE "I'm sorry, I don't know why I'm concerned with such things."
    MC "Don't worry about it... you felt... really nice though."
    show AE nude-happy
    AE "...Thank you."
    jump AE051_c1_after

label AE051_c1_after:
    MC "So, you really put a lot of work into all of this. I can tell this was planned to a T."
    show AE nude-neutral
    AE "Yeah. I mean, I had a lot of help. Yureno-san was meant to act as a watchdog as I bought the condoms and-"
    MC "Why not have her get them?"
    AE "Huh?"
    MC "Why couldn't you spend time with me and have her get them?"
    show AE nude-embarrassed
    AE "...I couldn't control myself around you."
    MC "Couldn't control yourself?"
    show AE nude-embarrassed
    AE "Over the past few days... I've... I've NEEDED you inside me. I couldn't help it, it was like I was in heat."
    AE "As my growth progressed, my... feminine parts began to rub against my thighs constantly, and my behind started to feel so sensitive... if I tried to spend time with you as we usually do, I don't know if I would have been able to control myself."
    MCT "Wow. It was that serious, huh?"
    show AE nude-neutral
    AE "Of course, I feel much better now. At least enough to focus on classes."
    MC "Yureno-chan must have been driven up the wall with your... um..."
    "I looked over to Yureno-san's side of the room, completely cleaned, and noticed two neat squares on the side of the bed."
    show AE nude-embarrassed
    AE "W-Well, I requested for her to stay with a friend, but she was very hesitant. She said she didn't mind being in the roo-"
    MC "Are... those my clothes?"
    show AE nude-neutral
    AE "Hm? Oh."
    show AE nude-happy
    AE "Yeah, I made sure to prepare them for you when you woke up."
    show AE nude-embarrassed
    AE "I'd also tried to set up to prepare something for breakfast, but... well, I'm admittedly still a bit weak in the knees after last night."
    AE "Although... I have to confess something."
    AE "After getting you under the covers, I um... I began to cuddle you."
    MC "Oh?"
    show AE nude-neutral
    AE "You can attribute it to post-coital giddiness, I suppose. I apologize for intruding on your personal space."
    MC "Hm. Darn. Wish I'd been awake for that."
    show AE nude-happy
    AE "Mhn."
    "Shiori-chan began to blush as she placed her hand on her hip... and she went wide eyed."
    show AE nude-surprised
    AE "What... what on earth?"
    "Dropping her sheet and leaving her breasts out in the open, she became overcome with shock as she began grasping at her lower body."
    MC "What, what's wrong?"
    AE "No. No-no-no-no-no-no."
    "As she lifted herself out of bed, I got a good glimpse of her full enormity. I could tell without her even needing the measuring tape, the same thing I noticed last night as well, her buttcheeks are definitely bigger."
    "I sat silently, struggling for things to say as she pulled out the measure and wrapped it around each leg, then from front to the back, and-"
    AE "Gch, I can barely see. Numbers are too faded."
    show AE nude-sad
    AE "Hotsure-san, can you come here for a moment? I need your hands and eyes."
    "As I got up naked from the bed, a cold breeze hit my groin as Shiori-chan looked back at me. Her face turning red, she quickly looked away and back to her front."
    "Taking the measure in both hands, I ran my hands across the material until they were at width with her behind."
    MCT "Oh man... She's not gonna be happy about this."
    AE "How large is my... rump from end to end?"
    MC "From the looks of it... here. Take a look."
    "Shiori took the tape and nearly pressed it against her face as close as possible."
    show AE nude-surprised
    AE "W-What?!"
    AE "Is-Is that number exact?!"
    show AE nude-sad
    AE "H-How am I getting so big?! This stage of growth is only found in the top 30th percentile of students with lower body growth!"
    "She let out a sigh and put the tape measure down. Taking this as my cue, I walked up behind her and placed my back against hers. I had to bend my back a bit, as her ass pressed against my crotch."
    show AE nude-surprised
    AE "Eep!"
    AE "O-Oh."
    MC "Hey, it's gonna be okay, alright? You're strong."
    "As she looked back, I did little to hesitate as I pulled her in for another kiss."
    show AE nude-happy
    AE "Mmm~"
    "As we kissed, the tension in the room rose. Feeling her heat, I reached down slowly towards her slit as I felt my manhood get stiff, forcing it's way between her buttcheeks."
    show AE nude-surprised
    AE "Mmph!"
    "At the feeling, she pushed my hand away, and pulled her rear away from my groin. She looked at me with shock and what seemed to be some fear."
    MC "Huh?"
    show AE nude-embarrassed
    AE "Ah-U-Um..."
    MC "I'm sorry, was I-... you okay?"
    AE "Yes! Um... ah! The clock! Look at the time! We shouldn't dawdle longer."
    AE "*Khm* Yes. Indeed. We should prepare for class."
    "She rushed over to her cabinet, where she pulled out a pre-pressed uniform."
    AE "I foolishly left my headband and glasses on Yureno-san's side. If you please?"
    MCT "What was that? We were having an intimate moment and then..."
    MC "Right, yeah, you're right. Do you need to take a shower, or-?"
    AE "No! I took one last night and... um... practiced what you taught me. You, however, probably should."
    MC "What, do I smell?"
    AE "No, no, it's just... you worked up a sweat last night and you just have some... masculine musk."
    MC "So I smell?"
    AE "Not at all!"
    MC "Alright, if you say so."
    AE "If I... so you're not?"
    MC "Nah."
    AE "Ah perhaps I... *Khm*, nevermind."
    "I chuckled a bit at her attempt to cover for her awkwardness. I probably wouldn't have been able to get a shower in anyways, as I usually take a long time. I brushed through my hair with my hand-"
    MCT "Gch! Ow. Ugh, matted... whatever, I already said I wouldn't."
    hide AE with dissolve
    "As I went to the other side of the bed, I looked back to Shiori-chan, who had put on her shirt and was hiking up her panties as best she could, her ass engulfing it to make a triangle shaped thong."
    "I handed her the accessories as I put my own uniform on as she squeezed as best she could into an ill-fitting skirt."
    #$Ripping sfx$
    show AE sad with dissolve
    AE "Haah. Of course. Let me guess-"
    MC "It's... right over the crack."
    AE "As expected. Are my panties visible?"
    MC "Not... past your flesh."
    show AE angry
    AE "Grrr... Haahn, whatever. I'll be getting a new uniform soon anyways. I'll need to bear with the humiliation."
    show AE sad
    AE "It feels like my life has been nothing *BUT* humiliation after humiliation recently."
    MC "..."
    MC "I won't tell anyone."
    show AE neutral
    AE "Hm?"
    MC "I won't tell a single person we fucked. If anyone asks about where I was, I'll tell them I went to town at night."
    show AE sad
    AE "Keisuke-kun... No."
    AE "I don't want any dishonesty. If someone asks you directly... tell them. I'd do the same. If I'm adult enough to invite you over at night for sex, I'm adult enough to accept the consequences of breaking the rules."
    MC "I..."
    MC "Understood."
    show AE happy
    AE "I appreciate the gesture, though. I truly do. You understand the importance of a woman's honor..."
    MC "Of-"
    show AE angry
    AE "Also, please watch your language."
    MC "Of course."
    "I looked over at the clock. Only a few minutes before class started."
    MC "Should I try to sneak back to my room? Daichi is probably wondering where I've been."
    show AE embarrassed
    AE "I think it may be a bit too late for that. The others are sure to be getting out of their dorms to get to class."
    MC "Hmm... I guess that means that we'll just have to walk back to class together."
    "Extending a hand out to me, I got ready to open the door."
    MC "You mind?"
    show AE happy
    AE "...Not at all."
    "She took my hand, and we opened the door. Out into the hall, and out towards a new chapter in our relationship."
    jump daymenu

label AE052:
    $setProgress("AE", "AE053")
    #AFTERNOON
    scene Library with fade
    play music Peaceful
    "As I walked into the library, I was surprised to not only find it occupied, but occupied by a familiar face."
    show Tomoko neutral with dissolve
    MC "Hey, Tomo!"
    Tomoko "Oh. Hi, big brother."
    "Tomo sat on a chair at a table, holding her hair (or as much as she could fit) in her arms. It was obvious that she hadn't even been making any attempts to cut it."
    MC "Look who got herself out of her room!"
    show Tomoko surprised
    Tomoko "Ehh! I come out of my room! Just, like, for classes and junk."
    MC "Why are you out here now?"
    show Tomoko neutral
    Tomoko "I'm waiting out here for Yuki-chan."
    MC "Yeah? Good-!"
    Tomoko "Yeah."
    MC "Good, good, ah, man, that's good."
    MC "God, I'm so glad you're getting out and making friends."
    Tomoko "I-I'm not getting out at all, she's my roommate."
    MC "Well, yeah, but-"
    MC "Ah, whatever, you get what I mean."
    show Tomoko happy
    Tomoko "Hmm~"
    "Sitting next to Tomo felt refreshing in a way. Though we'd both changed drastically, I felt as though she was kind of like an anchor to me from my time before coming to Seichou. In a way, I liked to think she felt the same."
    show Tomoko neutral
    Tomoko "Haaaahn-Mm!~"
    MC "Tired?"
    Tomoko "Lil bit."
    MC "Up studying?"
    Tomoko "Nyeeeh... Monster Quest."
    MC "Tomooo."
    show Tomoko surprised
    Tomoko "Hey! I'm doing good right now!"
    MC "Uhuh. Hey, how's chemistry going?"
    show Tomoko sad
    Tomoko "...It's going fine."
    MC "Tomo, you know my girlfriend has access to every student's record, right?"
    MCT "I had no idea if that was true, and I knew for a fact that if she did there's no way she'd show me, but what was important was that my bluff worked on my gullible little sister."
    Tomoko "Mweeeeh~"
    MC "Tomooo, c'mon!"
    show Tomoko neutral
    Tomoko "Chemistry is haaard!"
    MC "If you needed to-"
    "*Creak*"
    "I stopped mid sentence to look to the door, saving Tomo from a a verbal lashing. As students piled out from the office, Shiori made her way out before turning back to the office."
    show Tomoko neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show AE neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    AE "-and be sure to lock up when you're done."
    MC "Long day at work, eh?"
    AE "Hm?"
    "She did a small waddle to turn around, craning her head to meet my gaze."
    show AE surprised
    AE "O-Oh, Hotsure-... Keisuke."
    "As we made eye contact, I couldn't help but feel a lightness in my chest."
    "I wouldn't say it was awkward, but... it just felt so surreal. I couldn't look at her in the same way that I had before we had sex."
    "I can remember when being near her made me feel on edge, but now I just get this feeling of comfort when she's near."
    show AE smile
    AE "A bit. What all have you been up to today?"
    MC "Not much. I went back to my dorm for a bit, caught up with Tomo."
    AE "Ah, yes, hello Tomo-Chan."
    Tomoko "H-Hi."
    MCT "Oy, oy! How come it took me weeks to be called -chan, but she gets it within only meeting her twice?!"
    "Tomo sheepishly stepped back a bit, but with a small smile. Knowing her, I'm glad she's at least taken to Shiori a bit, even if she hasn't fully let her guard down."
    MC "I'm guessing today's mostly just been meetings for you?"
    show AE neutral
    AE "Right. I've mostly been making up for the time lost when I was... emotionally indisposed."
    MC "Mm, I see."
    MC "So then... it helped?"
    show AE embarrassed
    AE "..."
    Tomoko "Hm? What did?"
    "Biting her bottom lip, Shiori seemed to have a bit of insecurity as a mentioned that. Realizing the implications of what I said only after saying what I did, I was about to slap together a false clarification, when Shiori spoke up."
    AE "Do you, um..."
    show AE smile
    AE "Do you want to go to the roof?"
    MC "Oh, uh, sure."
    Tomoko "W-Wait, hold up. Where's Y-Yuki-chan?"
    show AE neutral
    AE "She's still organizing in the room. Feel free to enter, simply be careful around the documents."
    Tomoko "Got it, m-m-ma'am."
    show AE smile
    AE "No need for the ma'am, business, Tomo-chan."
    MC "O-Oh yeah? Well, I think you *should* call her ma'am! Be respectful to your seniors, Tomo!"
    AE "Keisuke? The roof?"
    MC "Oh, yeah, um..."
    MC "I'll catch up with you later. Love you."
    Tomoko "Love you too, Keisuke."
    hide AE with dissolve
    "Shiori took the lead as we exited the library and made our way through the halls."
    Tomoko "You guys are weird."

    scene Roof with fade
    "As we reached the roof, the sun had created a light orange patine on the clouds above, and the air had a markedly chilled breeze as it wisped about my locks. Shiori went first, and made her way to the metal bench. She patted the seat next to hers, beckoning me to join."
    show AE smile with dissolve
    MC "So."
    AE "Mm."
    MC "Lovers."
    show AE happy
    AE "...I suppose, yes."
    MC "Sorry, about the question when Tomo was in the room."
    show AE neutral
    AE "Oh, no, no worries."
    MC "Mm, cool, cool."
    AE "..."
    MC "..."
    "Though I didn't know what to say, the two of us, I could tell, both felt as though we were in a whole new world together."
    MC "How's it been since, well, we... did it?"
    show AE embarrassed
    AE "Admittedly, it's been a bit hard to walk straight today."
    MC "Eheh, um... sorry. I probably should have been more gentle."
    show AE neutral
    AE "..."
    show AE embarrassed
    AE "A-ah! No, no, no, it has nothing to do with, t-that."
    show AE neutral
    AE "My legs have just been adjusting to the weight of, um-"
    MC "Oh! Oh, right, the new size. Right."
    show AE smile
    AE "N-no, you were perfect."
    show AE embarrassed
    AE "Oh god, I really shouldn't be saying that out loud."
    "As a blush overcame her face, she sheepishly turned away and covered the side of her face with her hand."
    MC "Ehehe, good to know."
    MC "So... what now?"
    show AE neutral
    AE "What now?"
    MC "Well, what I mean is..."
    MC "Where do we go from here?"
    AE "Ah, I see."
    show AE smile
    AE "Um... I don't know about you, but... I suppose now I feel a bit more open with... being with you."
    MC "Yeah?"
    AE "Yeah."
    show AE neutral
    AE "Recently, I've been thinking about..."
    show AE sad
    AE "Well..."
    show AE neutral
    AE "...How often do you think about your future?"
    MC "Um..."
    "I was unsure of why she was asking me that, but it seems as though, with the emphasis put on the question, that was the main reason we were up here."
    MC "Why do you ask?"
    AE "Well, I was... *khm*"
    show AE sad
    AE "I... nevermind."
    "It was obvious that there was something she was holding back, unsure of whether or not she should say. I could see it creating a lump in her throat that she simply swallowed. I decided instead to spare her the anxiety with a question of my own."
    MC "Any plans once we get out of here?"
    show AE neutral
    AE "When we get out of here? You mean, once we graduate?"
    MC "Yes."
    AE "Hmm..."
    MC "I can think of a few things."
    AE "...Like what?"
    "I lightly pet Shiori-san's head as I began to go through all I wanted to do."
    MC "If I recall, you grew up in Tokyo, yeah?"
    AE "Somewhat."
    MC "Somewhat?"
    MC "That's not usually a question that has 'Somewhat' as an answer."
    AE "It's a bit complicated, to be honest. I wouldn't want to bore you."
    MC "Classes are done, so I got all day. Shoot."
    AE "Ah. Very well... um, I was born in Chuo at St. Lukes, but my parents were only visiting my uncle at the time. For a good portion of my life, I was actually raised in Asahikawa."
    MC "Eh? Hokkaido?"
    AE "Mhm. My grandparents owned a home a distance out from the city and into the mountains, but they ran a small restaurant. Up until... What was it... age six I believe, I was living in the upstairs room at the building."
    MC "Huh... Hokkaido... I don't really hear it in your voice. You don't really have much of an accent."
    show AE sad
    AE "My father had one, but not my mother and... well... she was the one who would talk to me more often."
    MC "I see."
    AE "After a while, the housing market crisis took a toll on my grandparents, and we had to move out of the shop and into Kabukicho. My uncle set us up in a building, but..."
    MC "I'm guessing there was a catch?"
    AE "...It was originally a den in a back alley that was supposed to catch fire in an insurance fraud scam. There was only one room left standing. Little better than a hovel, really, but it was home."
    AE "Shortly after moving to Tokyo, my mother took up a job, broke her neck, and... well, I suppose you know the rest from there."
    AE "Living in Kabukicho... was one of the darkest times of my life. But it was also where I developed the most into who I am today."
    "Getting up, she walked over to the railing and began to pace as close to it as her hips would allow."
    show AE smile
    AE "Still, though. Going back to Hokkaido at some point, getting a view of the mountains, relaxing in the snow... haaah, it would be nice."
    "Shiori exhaled and looked out to the blinking lights of the city past the hills, arms resting on the metal railing as she arched her back."
    AE "It indeed would be."
    MC "..."
    MC "Alright then."
    show AE neutral
    AE "'Alright'?"
    MC "Let's do it."
    AE "I... beg pardon?"
    MC "After we graduate, you and I are going to take a little trip on the mainland. We can go up to the mountains in Hokkaido for a few days, maybe rent a cabin, go to a hot spring. It'll be fun!"
    show AE surprised
    AE "A hot spring?"
    "Though somewhat confused, I sensed a hint of excitement at the idea in her voice."
    show AE neutral
    AE "I've... never been to one."
    MC "Well, then, now we definitely gotta do it!"
    "The apprehension on her face turned to a smile as she began to chuckle to herself."
    show AE happy
    AE "I suppose we do."
    MC "Hmm~"
    "Coming up from behind, I pressed up against her rear, feeling her soft ass squish against me as I arched forward to give her a peck on the top of her head."
    MC "Hey, Shiori-chan."
    show AE neutral
    AE "Hm?"
    MC "Think your snow angel will have a bigger dress, or just a more elaborate one with your butt?"
    show AE surprised
    AE "Ach!"
    MC "Kahahaha!"
    show AE angry
    AE "Mmmph!~"
    show AE smile
    AE "...Tshh, you're such a pain."
    MC "Nehehe~"
    "Smiling up at me, she leaned in as we embraced with a kiss for a few moments before I pulled away with a question of my own."
    MC "Soo, I have a question."
    show AE neutral
    AE "Mm?"
    MC "What do you usually wear out?"
    AE "What I wear out?"
    MC "Yeah. Last time we went out together, you just wore your uniform."
    MC "That can't *really* be your only clothes, yeah?"
    AE "...I feel like you're going somewhere with this."
    MC "Humor me."
    show AE sad
    AE "Haahn... yes, they are. I came into Seichou with an old tank top and a pair of shorts."
    AE "The shorts did not fare well."
    show AE neutral
    AE "At the moment, this uniform, as ill fitting as it can be, is all I have."
    MC "Hmm..."
    MC "Alright, that settles it."
    show AE angry
    AE "If that reaction indicates what I suspect-"
    MC "Tomorrow, we're going into town and getting you a pair of clothes to wear."
    AE "Knew it."
    MC "Yeah, you said you didn't have any, so let's go get you some."
    show AE neutral
    AE "That's completely unnecessary."
    MC "I'd say it's very much so necessary."
    show AE angry
    AE "I'm still growing, Keisuke. Buying clothes now would be a waste."
    MC "Plenty of places do adjustments!"
    show AE neutral
    AE "True as that may be..."
    show AE angry
    AE "Clothes are very expensive, and it would be improper of me to scrounge off you."
    MC "They're expensive for a reason, though. More than just for how you look, it's about being professional."
    AE "I look plenty professional wearing what I am now."
    MC "You're going to wear your school uniform to college?"
    "Shiori opened her mouth, yet hesitated. She thought over what I said, and simply sighed."
    show AE sad
    AE "I..."
    show AE neutral
    AE "I figured if I were to get clothes, I'd do so with my own money."
    MC "Right but... what money?"
    show AE sad
    AE "..."
    MC "No offense."
    AE "No, no, none taken. You're... you're right."
    show AE neutral
    AE "Fine. Tomorrow we can go out and get some clothes together."
    MC "Alright!"
    show AE sad
    AE "I promise I won't overload you with anything expensive."
    MC "Don't worry about it!"
    MC "C'mon, lets head back down. Sun's going down."
    show AE neutral
    AE "Right."
    "Taking the lead, I held the door open for Shiori to enter. Giving her a kindly smile, she reciprocated, and headed down into the stairway."
    AE "For the record, Keisuke?"
    MC "Hm? Yeah?"
    show AE smile
    AE "It really did help."
    MC "...Good to hear."
    "I closed the door behind myself, and we returned to our dorms for the night."
    jump daymenu

label AE053:
    $setProgress("AE", "AE054")
    #SCENE AFTERNOON
    scene Town with fade
    play music Busy
    AE "Are you sure you know where it is?"
    show AE neutral with dissolve
    "For the past half of an hour or so, I'd been exploring the city with Shiori after class; looking for a clothing store for the lady on the grow."
    MC "Yeah, I saw it last time we were in town."
    "I may have lied and told her I already knew of one to further convince her. This may or may not have lead to us standing on the sidewalk corner as I tried to think over where we've been."
    "On the plus side, I've now racked up a nice collection of free pocket tissues."
    AE "And that appliance store we went into?"
    MC "I've been looking for a microwave recently."
    MCT "I'd admit that I don't know what I'm doing, but my pride won't allow it."
    AE "Like the ones we have in dorm?"
    show AE happy
    AE "Mhmhm, I'm glad you're terrible at lying. It makes life easier."
    MCT "Ow, my pride."
    MC "Eheh, eh... sorry bout that. I'll, put 'clothing stores' into my phone."
    MC "Let's see here..."
    MC "Ah, here we go!"
    MC "'Radiant Raiment (Placeholder name), clothing for ladies and gentlemen of all sizes', cool. I'll put this into the map-"
    MC "Aaand it's right around this corner."
    show AE surprised
    AE "W-Wait, really?"
    "I walked only a few feet forward around the bend and the gigantic mannequins of different proportions were the first thing I saw."
    MC "It... looks like it."
    show AE smile
    AE "Saves us a walk, at least. Less people staring."
    MC "Yeah, let's head in."
    "We walked over to the glass door, as I pulled it open for Shiori to go first."
    show AE smile
    MC "I told you I knew where it was."
    show AE angry
    AE "Opf-! You- Mmn!"
    MC "Heheheh."

    scene Clothes Store with fade
    "As we walked inside, the cool air and smell of perfume became immediately noticeable, and the clothing distribution made it immediately obvious that the store more than often catered to a specific clientele: people who can afford luxuries while dealing with their growth."
    MC "Okay, so, you look around while I... look for somewhere to sit."
    show AE neutral with dissolve
    AE "Understood."
    AE "..."
    AE "..."
    show AE embarrassed
    AE "Where do I start?"
    MC "Where do- I think you just look around for clothes you like."
    AE "Right, but... how do I know if they'll look good or not?"
    MC "Eh, I'd just get something you feel comfortable in."
    AE "W-Well, indeed, but I should find something that would make me {i}look{/i} good. That should at least help justify the expense-"
    UNKNOWN "Oh? What's this now?"
    "As Shiori voiced her concerns, a familiar face made her way over to us."
    show AE neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    show BBW neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    MC "Ah, Nikumaru-san!"
    BBW "Good afternoon, Keisuke. I wouldn't expect to see you here."
    AE "Good afternoon, Nikumaru-san."
    show BBW surprised
    BBW "Hm? Ah! I {i}certainly{/i} didn't expect to see {i}you{/i} here. No offense."
    AE "None taken. It's not often I leave the campus."
    show BBW neutral
    BBW "Indeed. It must be something dramatic to call you away from the campus."
    show BBW haughty
    BBW "And to a clothing store of all places. That is a surprise."
    MC "Yeah, it's actually Shiori's first time going clothes shopping."
    show AE embarrassed
    AE "K-Keisuke, don't-"
    show BBW surprised
    BBW "Truly? Your first time, ever?"
    show AE sad
    AE "I... yes. That's true."
    BBW "That is..."
    "She coughed into her hand, looking embarrassed."
    show BBW happy
    BBW "Well, I hope your first time leads to something memorable. Find something that will {i}wow{/i} those around you."
    AE "I doubt it."
    AE "Admittedly, I... don't know much about fashion or design-"
    "As Shiori continued, I could see Nikumaru-san's eyes light up as a small grin slowly formed across her face."
    show AE neutral
    AE "-and really, I've never had the luxury of-"
    BBW "Of course! I completely understand."
    show BBW haughty
    BBW "You're a hard working woman; things like shopping or accessorizing can take a backseat. Here. You go get a basket and we'll start immediately."
    show AE surprised
    AE "Start...?"
    show BBW neutral
    BBW "Since you need someone to be a fair and experienced judge, I will help you put together a wardrobe."
    AE "Y-You'll help?"
    show BBW haughty
    BBW "Of course! There are a few ways to flatter your body and a million ways to not, and my sense of style won't abide someone pulling just anything off the rack."
    BBW "Now, chop, chop. We both can appreciate things being done efficiently and quickly, hm?"
    show AE neutral
    AE "Right. Thank you."
    show BBW neutral
    BBW "Mhm, no worries."
    hide AE with dissolve
    if True: #If you haven't gone through crossover scenes (TBI)
        if getAffection("BBW") < 10:
            MC "Alright, Nikumaru-san, what's the end goal?"
            show BBW angry
            BBW "Moi? I don't have any sort of..."
            BBW "..."
            "Nikumaru-san craned her puffy neck to look over in Shiori's direction, using her thick, pillowy arm to bring her fingers up to her chin as she smirked."
            show BBW happy
            BBW "Just making sure she's out of earshot."
            BBW "It's simple diplomacy, Keisuke. The Student Council president is seen wearing something fashionable, she's asked who assembled her wardrobe, she tells them it was yours truly, and I get publicity for my business."
            MC "So... manipulating, basically?"
            show BBW haughty
            BBW "No, no. Just seizing an opportunity that presented itself."
            MC "Well, whatever, just please don't mess with her too much."
            BBW "Ohohoo, Hotsure-san, I would never.~"
        else:
            MC "Thanks a lot for this, Nikumaru-san. I know you don't exactly get along with Shiori."
            BBW "Oh, she's definitely a thorn in my side from time to time, but don't be fooled. I intend to help her to the best of my ability."
            show BBW happy
            BBW "After all, she has a good taste in suitors."
            MC "Eheh, well, thanks."
    else: #If you have gone through crossover scenes
        MC "Thanks for helping out Shiori, Alice."
        show BBW neutral
        BBW "Not at all. She and I share an understanding. It's only right that I lend her a hand in my area of expertise."
        MC "I'm glad the two of you became closer. I really am."
        show BBW happy
        BBW "...I am too."
    show AE neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve 
    AE "Okay, I got a basket."
    show BBW happy
    BBW "Splendid. Why don't you go find some articles that appeal to you, and we can start from there? It is important that you retain your own style."
    show BBW neutral
    BBW "And, mhm, I appreciate the look, but I think your hair would look much better with a more fashionable headband on. How about we try-"
    "As Nikumaru-san reached out her hand, Shiori reacted quicker than I'd ever seen before, and quickly jumped out of the way and next to me."
    show AE surprised
    AE "W-Wait!"
    show BBW surprised
    BBW "Oh, wuh-?"
    show AE sad
    AE "I- um... I'd like to keep the headband on."
    show BBW neutral
    BBW "Hm?"
    AE "Y-You're an expert on fashion, right? You can integrate it into an outfit, can't you?"
    show BBW surprised
    BBW "Erm... I suppose..."
    "Nikumaru-san turned to me with a puzzled look. I mouthed 'It's complicated' and she nodded in understanding."
    show BBW neutral
    BBW "Of course I can, dear! I make it work for myself, why not you too?"
    show AE smile
    AE "Thank you."
    BBW "Now, I want you to find an outfit and bring it to me. {i}I'll{/i} judge whether or not you should wear it."
    show AE neutral
    AE "Understood."
    "As the minutes passed, Shiori walked around the store, collecting up clothes. Finally, she brought her basket of clothes, folded neatly, over to Nikumaru-san."
    BBW "Let's take a look here."
    "She went through the first set."
    show BBW angry
    BBW "Ugh! Gaudy."
    "Second."
    show BBW neutral
    BBW "Mmm. These pants could work, but this shirt is too much to pair with anything."
    "Third."
    show BBW angry
    BBW "...A tweed pantsuit? A bowtie? Dear, are you actively trying to sabotage your public image?"
    show AE sad
    AE "I... I was hoping you'd say yes to the pantsuit."
    BBW "You're not going to work at a retirement home, are you?"
    "I looked at Shiori, and it seemed obvious that her last statement really irked her."
    MC "Well, I mean, I think it looks good."
    BBW "What you think looks good and what the public thinks are two different things, then."
    show BBW neutral
    BBW "But! I digress. I assume that even Matsumoto-san would agree that being presentable is one of society's most important expectations. That's part of the reason why we wear uniforms, right, Matsumoto-san?"
    show AE neutral
    AE "Well, I suppose looking {i}respectable{/i} is a key aspect of-"
    show BBW happy
    BBW "Exactly. Now, on to the next one."
    show BBW angry
    BBW "Oh my god. PLEASE tell me you're not going to try to wear a beige dress shirt."
    show AE angry
    AE "I-I'm sorry, but I don't see what's wrong with any of what I brought."
    BBW "Well, for starters most of what you bought is suited more for an old man than for a young woman."
    show AE neutral
    AE "Well... is that a problem?"
    BBW "My dear, 'professional' does not simply mean 'office appropriate.' You need to take into consideration your femininity, your physique. Dressing like a senior male partner at a law firm won't work for you, no matter how spiritually in sync you may be with that sort."
    show BBW neutral
    BBW "Well, it's fine. I suppose I'll put in a bit of leg work myself and find something {i}for{/i} you. No use standing around all day."
    BBW "But this is for you, after all. What would you like? Generally, I mean."
    AE "W-"
    BBW "Think {i}feminine{/i}."
    show AE embarrassed
    AE "U-Um... well... I suppose if I were to go for more... feminine clothing, I would want..."
    "Shiori leaned in and whispered to Nikumaru-san, whose eyes widened in surprise."
    show BBW surprised
    BBW "What? Really?"
    MC "Wait, what?"
    BBW "I see... I mean, I could see the look working for you, but... are you sure?"
    AE "M-Mm."
    MC "Huh? What? What was that whisper about?"
    show BBW happy
    BBW "It appears that little miss stern and stone faced wants to try something a bit unexpected."
    AE "Mm. Hopefully it will be something that will 'wow' all of us."
    BBW "..."
    show BBW haughty
    BBW "Ohoho, very well dear. I'll find you something that will make you absolutely shine."
    hide BBW with dissolve
    "As Nikumaru-san waddled away and over towards the ladies clothes, I leaned over to Shiori."
    MC "I... don't think she liked your tone."
    show AE neutral
    AE "Perhaps but... I thought all the outfits I chose were respectable and fine. I saw no issue with any of them."
    MC "Don't worry, Alice knows what she's doing, alright?"
    show AE embarrassed
    AE "..."
    show AE sad
    AE "You're right. I wouldn't have took her help if I didn't trust her judgement."
    "After a few more moments, she returned."
    show BBW neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    BBW "And here we are. Your outfit and undergarments."
    show AE surprised
    AE "U-Undergarments?!"
    BBW "An outfit needs to match even what isn't seen, dear. I'm sure you understand."
    show AE angry
    AE "W-Buh-tch-ah!"
    show BBW haughty
    BBW "Come now, dear. Try it on."
    show BBW neutral
    BBW "I believe this could be what you're looking for."
    AE "...Fine, I'll-"
    BBW "Oh, and by the way?"
    show AE neutral
    AE "Hm?"
    BBW "I think it would go best without your headband."
    AE "Wait, what?"
    BBW "It simply wouldn't look as good with it."
    AE "Well, that's fine, I'm not taking off my headband."
    show BBW angry
    BBW "Tsk! Listen, I don't know {i}why{/i} you can't just take it off for a moment, but I'm being honest with you when I tell you this outfit {i}needs{/i} you to try it on without the accessories."
    MCT "Damn, these two are at a pretty rough impasse."
    menu:
        "Take it off": #+1 alice
            jump AE053_c1_1
        "Keep it on": #+1 shiori
            jump AE053_c1_2

label AE053_c1_1:
    MC "Shiori, I don't know much about fashion, but... she might have a point."
    show BBW happy
    $setAffection("BBW", 1)
    BBW "Thank you. Your boyfriend has a good eye for this sort of thing as well, I see."
    show AE sad
    AE "B-But..."
    MC "I mean... I know it means a lot to you, but it's only for a little bit. You don't have to wear it 24/7."
    AE "..."
    AE "Haah, you're right. It's childish of me to cling to it."
    show AE angry
    AE "Still, though... it'll only be while I'm trying it on. After, I want it back."
    show BBW neutral
    BBW "Of course."
    jump AE053_c1_after

label AE053_c1_2:
    MC "Shiori, you don't have to take it off if you don't want to."
    $setAffection("AE", 1)
    show AE sad
    AE "Y-Yeah, I know. Thanks for understanding."
    BBW "Very well, stepping {i}away{/i} from the {i}boyfriend bias{/i}, you need to understand that even the smallest detail can make or break a look. You get that, right?"
    AE "Well, I... I suppose."
    show BBW neutral
    BBW "If a student walked in with a school uniform with a gold tie, you would tell him to take it off. Fashion's the same way."
    jump AE053_c1_after

label AE053_c1_after:
    AE "..."
    BBW "Come now, don't be so bashful. You {i}did{/i} ask me to find you something."
    AE "I... you're right. I trust your judgement."
    BBW "Well, then, off to the dressing room with you!"
    "Shiori nodded, as she handed me her prized headband, letting her hair down and walked into the dressing room."

    scene black with fade
    pause 1
    scene Clothes Store with fade
    show BBW neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    "I sat next to Nikumaru-san for a few minutes as she filed her nails. Waiting in anticipation to see Shiori. Just then, she stepped out.."
    show BBW haughty
    BBW "Well, dear? How is-"
    show BBW surprised
    BBW "..."
    MC "Hm? What?"
    MC "A-"
    MC "..."
    show AE dress-neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    "I couldn't believe my eyes. It was as though the girl I saw once before in Shiori's bed had returned. She was dressed in a tight pink bodycon dress, a magenta sash tied around her waist."
    "The outfit being made for her body type, it clung to her body, leaving a definite outline of her enormous tush."
    "For the first time since I'd seen her, Shiori didn't just look like 'The Student Council President', when I saw her... I saw a girl."
    BBW "Oh. My. God."
    show BBW happy
    BBW "I... I wasn't sure it would be the case, but pink really DOES work well for you!"
    show AE dress-surprised
    AE "It does?"
    "Hearing her voice gave me whiplash. I was still in shock from just how different she looked."
    MC "Shiori, you... *asked* Alice to find you a tube dress?"
    BBW "She simply asked for something pink. It's a bit revealing, but she *does* look rather nice, hm?"
    AE "I... I look beautiful?"
    MC "Well, yeah!"
    "Shiori turned around, her humongous rump facing us as she did her best to pat it, she then ran her hands along her sides as she looked at herself in shock, blushing pink enough to make her dress look pale."
    AE "I look..."
    show AE dress-happy
    AE "Ehe..ehehehe~"
    MC "A-Ah."
    "Nikumaru-san and I both looked at her with wide eyes and open mouths."
    MCT "Did Shiori just... giggle?!"
    "Now I was without a doubt convinced; this woman was not my girlfriend."
    MC "U-Um... you... you just giggled."
    show AE dress-surprised
    AE "I... did I? I'm sorry, I just..."
    show AE dress-happy
    AE "Haah! I look pretty! For the first time in my life, I-!"
    MC "Well, Nikumaru-san, you definitely 'wowed' me."
    show BBW happy
    BBW "I... I actually picked it out for a bit of a laugh, but... you're right!"
    BBW "She looks like the belle of the ball!"
    show AE dress-surprised
    AE "Really?"
    show BBW haughty
    BBW "Of course, dear! Why if you weren't dating Keisuke, the boys would be coming for miles!"
    show AE dress-neutral
    AE "..."
    MC "You got that right. You look like the kind of girl that men would line up just to see."
    show AE dress-glasses
    stop music
    AE "..."
    "In hindsight, I damn my obliviousness."
    MC "Kehehe, tell me, do I gotta keep a better eye on ya or wha-!"
    AE "I hate it."
    MC "Eh?"
    AE "I... Get this off of me. I hate it."
    show BBW surprised
    BBW "Oh? But... I thought you, um-"
    hide AE with dissolve
    "Without a word, Shiori walked into the changing room and shut the door. A few moments later, she carefully slid the folded outfit under the door."
    MC "U-Um... Sorry."
    show BBW sad
    BBW "..."
    BBW "I'll... go find her something a bit more conservative."
    MC "Yeah... Yeah, I'll help."
    scene black with fade
    pause 1
    scene Clothes Store with fade
    play music Rain
    "Eventually, we settled on something completely different. A grey turtleneck with a black long-skirt. Shiori looked great when she tried it on, and it even matched with her headband, as Alice pointed out."
    Cashier "Alright, with the student discount, your total comes up to 18,197 yen, sir."
    "Shiori seemed to tense up a bit, looking at me for a moment for confirmation. She lowered her voice to a whisper."
    show AE sad at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    AE "{i}Keisuke, are you sure? I don't have many means to-{/i}"
    MC "No worries, I can swing it."
    AE "I had no idea clothes cost that much."
    show BBW neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    BBW "That much? Honey, that was a steal."
    "Pulling out my card, I handed it to the cashier who swiped it and then input the numbers onto her pad. Printing out a receipt, she gave it, and the card, to me with both hands and a smile."
    Cashier "Have a good day, sir."
    MC "Have a good day, ma'am."
    BBW "Enjoy, you two!"
    BBW "Now, I'd also like to make a purchase-"
    "As we walked out of the door, I looked at Nikumaru-san to see her put a red basket on the counter."

    scene Town with fade
    show AE sad with dissolve
    AE "So... about my... panic attack."
    MC "No need to explain. I think I understand."
    AE "..."
    show AE smile
    AE "Thanks."

    scene Dorm Exterior with fade
    MC "So, can you do lunch tomorrow?"
    show AE smile with dissolve
    AE "Definitely. Schedule's free."
    MC "Okay, cool! Well... enjoy the new clothes."
    show AE happy
    AE "Mm, yes. One moment."
    "She put down her bag in her dorm and then turned back around to plant a me a kiss."
    AE "Mmmph~"
    Tako "Woo!"
    AE "Thanks for today."
    MC "...You're welcome."
    hide AE with dissolve
    "As she shut the door, I could hear Tako's hearty cackle as I rounded the corner and headed down the stairs to the main floor of the girls dorm."
    show BBW neutral with dissolve
    BBW "Get home oka-"
    MC "WOAH, JE-"
    show BBW surprised
    BBW "Ah!"
    MC "Fff, oh, woah, eh- Ah... S-sorry, you startled me."
    show BBW neutral
    BBW "Mm."
    BBW "Admittedly, I may have brought her that tube-dress for my own amusement, but... despite her proportions, she truly is quite stunning."
    "Hearing Nikumaru-san say that made me chuckle a bit. It wasn't often she was very open with compliments, let alone for Shiori."
    MC "Eheh, yeah, she really is-"
    show BBW haughty
    BBW "Not quite on *my* level, but she certainly has something going for her."
    MCT "There we go. Wouldn't want to think I slipped into the wrong timeline."
    show BBW sad
    BBW "...Satisfy my curiosity... why is she so attached to her headpiece?"
    if getSkill("Academics") < 10:
        MC "Honestly? I'm not completely sure, but... I know it's important to her. That should be all that matters."
        show BBW neutral
        BBW "Hm... I understand."
    else:
        MC "I think... I think that it means something deeper to her about *who* she is. Like... she attaches it to her identity."
        MC "Does that make sense?"
        show BBW sad
        BBW "I see."
    show BBW happy
    BBW "Clothes have strong powers, Keisuke. They determine how someone is seen by a simple glance. It gives people insight into who they are, even if they don't want to let it be known."
    MC "Heh, I get you. I mean, I love this old jacket too."
    show BBW neutral
    BBW "Yes... Well, have a good night."
    MC "Yeah, you too."
    BBW "Oh, Keisuke?"
    MC "Yeah?"
    show BBW haughty
    BBW "That jacket is ratty. It doesn't suit you at all."
    MC "..."
    show BBW happy
    BBW "You somehow make it work well, though. You should keep it."
    "Handing me a brown bag, she turned around and headed back further into the dorms."
    MCT "A bag?"
    BBW "She'll appreciate it one day."
    MC "..."
    MC "...Thanks, Nikumaru-san. Really. {i}I{/i} appreciate it."
    show BBW neutral
    BBW "Have a good night."
    "I left the girls dorm, and headed out to the dimming courtyard as the lights flickered on, satisfied by a good day."
    jump daymenu

label AE054:
    $setProgress("AE", "AE055")
    #Scene Morning
    scene Dorm Interior with fade
    play music Schoolday
    "I'd woken up a bit earlier than usual, getting a pretty good amount of sleep. I made myself some breakfast as Daichi got up threw on his clothes."
    show RM neutral with dissolve
    RM "Hey man, did you see the game last night?"
    MC "Erm, which... one?"
    show RM smug
    RM "I don't know, I was just trying to think of something to say to distract you while I steal your toast."
    MC "Ah, I see. That's a pretty solid tactic, but personally, I'd go for a topic with-"
    MC "OY!"
    RM "Ha-Haah~"
    MC "Son of- Ngggh..."
    show RM neutral
    RM "Mmph, so I hear you're spending a bit on girl's clothes, eh?"
    MC "...Where did you hear that?"
    show RM happy
    RM "My special informant-"
    MC "I told Tomo who told Yuki who told you."
    show RM neutral
    RM "My special informant let me know that you and Shiori were out at the clothing store together, and Alice went too!"
    RM "Don't have more than one waifu, dude. That's messed up."
    MC "Nah- Tssh, I wasn't doing anything like that. I just went to go get a new outfit for Shiori."
    show RM angry
    RM "What, so she can disguise herself better?! Are you nuts?!"
    "As I got up from the table, grabbed my bag, and headed towards the door, I shook my head and raised an eyebrow at Daichi."
    MC "Nah. She doesn't need disguises when she can hide in plain sight."
    "I opened the door to see my loving girlfriend taking up most of the frame."
    show RM angry at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show AE happy at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    AE "Keisuke."
    MC "Hey Shiori."
    "At this point, I'd gotten used to Shiori showing up unannounced at my door. To a point, it was even endear-"
    show RM sad
    RM "Oh shi-!"
    hide RM with dissolve
    "At the sight of her at the door, Daichi scrambled out of the window with his bag."
    show AE surprised at center with dissolve
    AE "H-Hey! Don't go out the window, please!"
    MC "He's long gone."
    show AE smile
    AE "One day he'll get used to me."
    MC "Just not today."
    MC "So, what's up!"
    show AE neutral
    AE "Can you come back to my dorm with me for a bit?"
    MC "Hm?"
    MC "Any particular reason why?"
    show AE embarrassed
    AE "I have something for you."
    MC "Oh? For me?"
    "Shiori seemed a bit nervous, but she nodded and came closer."
    AE "Yeah, come with me."
    "Taking me by the hand, we walked to the girl's dorms as everyone was getting out of their dorms for the morning."

    scene Dorm AE with fade
    "Entering into her room, I noticed a missing Yureno-san; a fact that instantly brought another time to my mind."
    MCT "Wait... what's going on?"
    MC "So, you got me here, what's up?"
    show AE neutral with dissolve
    "Without saying a word, Shiori walked over to the side of the bed and bent over."
    MCT "GCH! It was a joke! Is this really happening right now?!"
    MCT "Shit, won't we be late for class if we do it here? I'd think she'd care."
    MCT "W-Whatever, don't look a gift horse in the mouth."
    "As my hands got closer to her voluptuous behind, she spoke up causing me to freeze."
    AE "Keisuke."
    MC "Eh?"
    AE "What you did for me when you bought me my new attire was extremely generous."
    MC "Ahh, it was nothing."
    show AE angry
    AE "It most certainly wasn't nothing."
    show AE neutral
    AE "I can't thank you enough. Truly."
    play music Hallway
    "Taking a rectangular metal box from under her bed, she lifted a hatch on the side and pulled it up to open the top."
    MCT "Ah. I see... down, boy."
    AE "However, be that as it may, I have no intention of letting your kindness go unrewarded."
    "Reaching her hands in and picking something up from the inside, she turned around and presented it to me with both hands."
    show AE embarrassed
    AE "Please, take it!"
    "A small stack of bills, held in the middle with a clip."
    MC "What?"
    show AE neutral
    AE "It's enough to cover a portion of what you paid to get me new clothes. I can get the rest to you after taking up a part time job."
    MC "..."
    MC "I'm not taking that money."
    show AE surprised
    AE "Eh?"
    "Shiori looked up from her bow as I looked on to her stern-faced."
    MC "You're already dealing with enough as it is; what with the student council and all."
    MC "If you get a part time job, how will I ever get to see you?"
    show AE neutral
    AE "W-Well, how am I supposed to pay you back?"
    MC "You don't. That's the point of a gift."
    show AE sad
    AE "I..."
    MC "Come on, you don't need to be so stingy with money."
    show AE angry
    AE "I-I'm not!"
    show AE neutral
    AE "..."
    show AE sad
    AE "Sorry."
    MC "Like I said, nothing to worry about. It was just a gift, you don't need to pay me back by getting a part time job."
    AE "I-I suppose you're right."
    MC "Do you really think you could balance a job too?"
    AE "...I mean, I could try."
    show AE neutral
    AE "I've worked part time jobs before."
    MC "That so? What, tutoring? Internships?"
    AE "Sometimes tutoring. But otherwise, no."
    AE "Nothing too impressive, I started off with handing out pocket tissues on a street corner, cleaning around my teacher's house, minor things. I made pocket change, but it was enough to get myself an occasional book or snack."
    show AE sad
    AE "Of course, when I could keep it, that is."
    MC "Keep it?"
    AE "Whatever money I made would go straight to my parents. I suppose that gave me {i}some{/i} use."
    MCT "No way..."
    MC "So, what, you're parents just up and stole shit from you?"
    AE "Whatever was valuable."
    MC "How did you get it back?"
    AE "That implies I got it back."
    AE "My parents would usually take a good amount of whatever I made, but I would usually have some left which I would keep hidden."
    MC "Do you ever have any {i}good{/i} stories about your parents? Because every time you talk about them..."
    show AE neutral
    AE "Well, of course. My mother wasn't always an addict, and my father... I can tell he {i}did{/i} feel something for me."
    show AE smile
    AE "In the summer months in Hokkaido, mother would always take a blanket up to the hills with me, and we'd always just sit out and read books together."
    show AE happy
    AE "She'd also love to just sit out with me in the winter, and we'd just lay down and catch snowflakes with our tongues."
    show AE smile
    AE "Father may have been loud but... when he was happy, it was a good loud. I didn't like sports much, but usually after the Tokyo Birds would win, he would be so happy. I'd always cheer too, and he'd hug me really tight."
    AE "The best, though, was when Uncle Oishi would come to town. When they got together and played a game of Mahjong, even just looking at dad's smile when he'd get ron would make everything feel... better. He was a competitive person like that; he loved winning."
    "Shiori closed her eyes, smiling as she exhaled, remembering the days of her early childhood. Though her reminiscences soothed me for the moment, her smile slowly faded as she opened her eyes."
    show AE sad
    AE "Their moments of past affection don't redeem their later actions, however. They would steal from me to fulfil their frivolous wants."
    show AE neutral
    AE "When my mentor taught me about money, he taught me not to covet it. To use it wisely, and save for important needs, but not to let it consume me."
    show AE sad
    AE "So... On that end, I suppose you have a point when you tell me about not being so... worrisome about funds."
    MC "See? What did I say, don't worry about it!"
    MC "Your mentor sounds like a smart guy."
    show AE smile
    AE "Mm. That's true."
    show AE neutral
    AE "..."
    AE "That's very true."
    show AE sad
    AE "..."
    if getAffection("AE") > 50: #80%
        AE "..."
        AE "I never told you how I met my mentor, did I?"
        MC "Um..."
        MCT "She looks hesitant, but... it kind of feels like this is something she would really like to get off of her chest."
        MC "Nah, I don't think you did. What was your whole deal?"
        AE "When I was far too young to have a job, just entering middle school, and my family was struggling... I... at the time I thought I did what I had to."
        MC "What you had to do?"
        AE "..."
        MC "What did you have to do?"
        AE "..."
        AE "Kabukichou was just {i}full{/i} of foreigners. College students, businessmen looking for a soapland; so many people in expensive clothes, with expensive jewelry, indulging in so much pleasure... wasting so much money..."
        MC "...No way."
        MCT "Theft. She's straight up confessing theft to me."
        MC "If you don't want to-"
        AE "I... I only tried it once. At night... when the town was at its busiest... an older man walked by with a cane. I thought he must have been rich... and he wouldn't be able to chase me."
        AE "I ran towards him... I grabbed his wallet from his hand as he went to buy food from a stall..."
        AE "And I ran face first into a car mirror not but two seconds later."
        MC "A-Ah."
        "While my face was definitely stoic and sympathetic, I couldn't help but laugh internally at the mental image. Turns out, though, Shiori saw right through me."
        show AE angry
        AE "My family couldn't afford glasses and it was dark. It didn't help that I... that I looked back."
        show AE sad
        AE "I must have blacked out for a second, because before I knew it, the man had knelt down next to me... He was concerned about me... he cared. He asked me why I did what I did and... he told me that no child should have to go hungry."
        AE "He gave me the money in his wallet and... told me where to find him if I wanted to have a chat. I cried the rest of the night when I got home."
        AE "For the first time in my life, I felt sick of myself. Sick of my existence. I knew I was meant for something better."
        AE "So I made the resolve to seek him out. His ways were foreign, but... they spoke to me more than I could have ever predicted."
        MC "Shiori..."
        "Walking over to her, I wrapped my arms around her in a big hug as she perked up a bit in surprise."
        "I pecked her lightly on the head and chuckled."
        MC "You didn't have to tell me all that, you know. But I'm glad you did."
        MC "Thank you for trusting me."
        show AE smile
        AE "A-Ah, it's nothing. Thank you for listening."
        MC "Oh! That reminds me."
    MC "Heheh, you know, it's weird; you brought me here to give me something, but..."
    show AE surprised
    AE "What?"
    "The minute I took the brown bag out of my backpack, Shiori was able to instantly recognize it."
    AE "No."
    AE "C-Come now, that's not-"
    "With a gasp Shiori looked at the pink bodycon dress from earlier. Not just the dress, as it turned out, but the undergarments and the other accoutrements too."
    MC "Ah, damn, it's a bit wrinkled from the bag."
    MC "Sorry about that."
    show AE sad
    AE "N-No, no, it's okay."
    show AE angry
    AE "N-No, wait, it's *not* okay!"
    AE "Why would you get that?!"
    AE "I told you, I don't want it."
    MC "I know, but-"
    AE "Why would I want to walk around looking like a base, tactless-"
    MC "You just looked so happy when you first wore it."
    MC "Besides, Nikumaru-san is the one who bought it for you. From what the slip said, you can get it refitted for free, too."
    show AE sad
    AE "Why would Nikumaru-san want to give that as a gift to me? It was obvious she was trying to humiliate me when she first had me wear it."
    MC "Well... I dunno, maybe she just thought you looked beautiful in it."
    MC "I know I did."
    AE "..."
    show AE smile
    AE "I... I thought so too."
    show AE sad
    AE "But that's exactly {i}why{/i} I had to put it back!"
    MC "Right, but..."
    MCT "Ah, right, her whole {i}plainness as a virtue{/i} thing. I didn't know it ran {i}that{/i} deep."
    "I couldn't think of much of a retort, but from the way Shiori looked at the dress, it seemed like I didn't have to."
    AE "..."
    show AE surprised
    AE "It... {i}does{/i} look quite pretty, doesn't it?"
    MC "Y-Yeah."
    AE "..."
    show AE sad
    AE "It's a gift from Nikumaru-san, hm?"
    AE "Well..."
    show AE smile
    AE "A gift is a gift, I suppose."
    show AE happy
    AE "Tell her... tell her I said thank you."
    "I smiled as she took it in her hands. Though her brow furrowed, she gave the most subtle of smiles with her jaw slacked. She exhaled sharply as she began to speak."
    show AE sad
    AE "Keisuke... I-I don't know what to say..."
    AE "I mean, you {i}know{/i} I can't wear this in public."
    MC "Well, I mean, you don't have to."
    MC "Just... wear it when you're alone and you want to... um... dress up?"
    show AE embarrassed
    AE "M-Mm."
    show AE sad
    AE "Keisuke..."
    show AE happy
    AE "Thank you."
    MC "Ah, don't thank me; thank Nikumaru-san. She bought it for you."
    show AE smile
    AE "I-I will, but, thank {i}you{/i} as well."
    show AE happy
    AE "For everything."
    MC "Eheh, no worries. It was my privilege."
    AE "Ehe~"
    show AE smile
    AE "By the way."
    MC "Hm?"
    show AE glasses
    AE "You totally could have grabbed my butt."
    MC "NGH!?"
    MCT "D-Damn it."
    MCT "...Nehehe"
    "I briskly sauntered over, and grabbed a handful anyway."
    show AE embarrassed
    AE "Meep!"
    MC "Is now good, then?"
    AE "N-Now's good too."
    "I smiled, and with a kiss, Shiori placed the dress on the bed and we headed out together through the halls."
    "I was so glad to have made her happy, so glad to see her smile."
    "I had the feeling that this was the beginning of something new in our relationship."
    jump daymenu

label AE055:
    #SCENE AFTERNOON
    $setProgress("AE", "AE056")
    scene Hill Road with fade
    show AE happy with dissolve
    "The cold, autumnal wind echoed through the hills as we descended down into the glen. Holding Shiori by the hand, we crossed a narrow stream together as we made our way around the bend. She stopped for a moment and looked around with a gentle smile."
    MC "What's wrong?  Tired already?"
    "I chuckled through my own huffing and puffing, knowing fully well that Shiori's legs wouldn't be exhausted from just this. Instead, she merely looked around and smiled to herself."
    show AE smile
    AE "No, no, just admiring the view."
    MC "Yeah?"
    show AE happy
    AE "Mm, I don't travel far from the road. It's refreshing."
    MC "Heh, yeah. Every time I come out to these hills I always manage to find something new."
    show AE smile
    AE "You come out here a lot, then?"
    MC "Eh, on occasion."
    MC "C'mon. It's just up this hill."
    if getAffection("AE") > 50:
        "As I stepped forward into a less step part of the incline, Shiori gently grabbed me by the shoulder."
        show AE happy
        AE "Ah-ah... I think {i}I'll{/i} go first."
        "With a sly grin and rosey cheeks, she ascended first, leaving me with a nice view in a somewhat uncharacteristic fashion."
        MC "Ke-heh-heh, sure thing."
        "As we made our way up-"
        "*Slk*"
        show AE surprised
        AE "Ohf!"
        MC "Woah, you alright?"
        show AE embarrassed
        AE "Y-Yeah, almost slipped. Center of mass and all... h-hey-"
        MC "Should I get in front?"
        show AE neutral
        AE "That would be for the best."
    "As I made my way up, with Shiori in tow, I began to feel a twinge of wanderlust as I continue to ascend, thankful to have Shiori by my side."
    
    scene Woods with fade
    #CICADA SFX
    "As the afternoon cicadas made their soothing, yet eerie chirps throughout the forest, I brought Shiori to the forest's entrance by the hand. As we stepped into the trees, I let out a sigh of contentment."
    MC "Good place as any for a picnic, yeah?"
    show AE surprised with dissolve
    AE "It's breathtaking."
    MC "Eheh, I figured you'd like the trees."
    "The forest itself, other than being a stunning canaphony of red and orange, had an intriguing layout. Each tree seemed to be placed as though they were equal distance from each other like a chess board; rows upon rows of poplar trees stretching on and on, light shining through each wooden path."
    AE "I... don't think I've seen this grove on any of the school maps."
    MC "Really? I mean... we're pretty far out, maybe the school doesn't own it."
    show AE sad
    AE "If that's the case... should we be here? What if it's private property?"
    MC "Eh, I wouldn't worry about it. I don't see any signs."
    show AE neutral
    AE "I suppose..."
    "Taking her by the hand and further inwards to the forest, I found a nice spacious intersection of trees and placed down the spare seat I brought from my dorm."
    MC "Did you bring a book?"
    show AE smile
    AE "Mhm! Wouldn't be much of a reading picnic if I didn't."
    MC "Eheh, yeah, sorry for forgetting to make any food. I know you didn't eat lunch today."
    AE "Oh, that's alright. I have a small stomach, I can go a while without eating."
    "As she lay down on the sheet, belly side down, her large rump stuck up a good distance from her body as it softly jiggled, her skirt only sparsely covering up half of her cheeks. I myself sat down a few feet away, resting my back on on a tree as my hair scattered out on the ground beneath me."
    MC "What's it you're reading?"
    if getSkill("Art") >= getSkill("Athletics") and getSkill("Art") >= getSkill("Academics"):
        AE "Mm, it's {i}Journey to the West.{/i}"
    elif getSkill("Athletics") >= getSkill("Academics"):
        AE "Mm, it's {i}A Book of Five Rings.{/i}"
    else:
        AE "Mm, it's {i}Mathematical Principles of Natural Philosophy.{/i}"
    MC "Ooohh, nice!"
    AE "Mm, I figured I'd start to read more about things that interest you."
    MC "Cool! I mean, I haven't read that, but it does sound pretty cool."
    AE "Mm. And how about you?"
    MC "Just an old manga from home. Figured I'd read it a bit in my free time."
    AE "Ah, I see."
    MC "You read any?"
    show AE neutral
    AE "No, I could never get much into manga or anime. Other than the lack of availability, I'm just not really used to a lot of the cartoonish style."
    MC "Ah, that makes sense."
    show AE smile
    AE "I'm willing to try and read some, however."
    MC "Yeah?"
    AE "Later, though. For now, I'll finish this first."
    MC "Alright."
    "Silently taking in the surroundings, the two of us sat with our books in hand for a good while. I didn't get much reading done, however, as every few moments I would look up to gaze at her behind."
    MC "..."
    show AE neutral
    AE "..."
    show AE smile
    AE "Mhmhmhm~"
    "Even with her nose in a book, she could still catch me."
    MC "Ehehe, sorry. I got a bit-"
    show AE neutral
    AE "Does that tree hurt your back?"
    MC "Hm?"
    "I looked back to the black and white aspen and looked back to Shiori. While it wasn't particularly uncomfortable, I picked up by the look in her eye what she was getting at."
    MC "Oof, yeah, it's giving me a real crick in my neck! Got anywhere else I could lay down?"
    show AE smile
    AE "Hmm, let me think~"
    AE "Mhmhm, alright, since it's a matter of your personal health..."
    show AE happy
    AE "Climb aboard."
    MC "Ehehe, don't mind if I do."
    "I closed my manga and walked over to my wide, beautiful girlfriend with a smirk. As I lay on the soft, plush groves of her pillowy legs, I leaned back and rested my head on her giant behind."
    MC "Mmhn... Haaah..."
    show AE smile
    AE "Am... am I comfortable?"
    MC "I feel like I'm in heaven."
    show AE surprised
    AE "O-Oh!"
    "I patted her round bottom like a pillow and closed my eyes as I rested on her legs. Shiori, undoubtedly, was a bit flustered by the situation, and yet she didn't object. Perhaps she too got a bit of enjoyment out of it as well."
    MC "How you doin back there?"
    show AE embarrassed
    AE "Um... Perhaps you can lay on my lap instead?"
    MC "Huh? Is it uncomfortable?"
    AE "N-No, it's just a bit... {i}too{/i} stimulating."
    "I only now noticed that she was slightly trembling as I nuzzled the back of my head into her curvaceous cheeks. I lifted my head up and looked back to her."
    MC "Oh! Haha, s-sorry, I forgot about your uh... sensitivity."
    show AE neutral
    AE "No worries."
    MC "Here how's about we switch the position a bit. Sit up for a sec?"
    AE "Oh? Sure. Hgn!"
    "As Shiori flipped herself over and sat up, I gently rested my head on her lap."
    MC "Haaah~"
    show AE surprised
    AE "O-Oh!"
    AE "..."
    show AE smile
    AE "Mhmhm~"
    "The warmth of her lap enveloped me as I rested my head on her plush thighs; blue fabric nuzzling my face as the back of my head rubbed against her belly."
    "I felt every gentle motion of her body. The sound of her slow and calmed breathing accompanied by the smallest of motions from her chest, reverberating as miniscule tremors on her puffy legs."
    "I closed my eyes in response to the comfort when, carefully, she took her soft, slender hand and began to pet my head. Fingers rustling through my silken hair as a smile crossed my face."
    "In the moment, I felt truly at peace."
    show AE happy
    AE "...Hmmm, hm-hm-hm-hmmm~"
    MC "Are you humming?"
    show AE sad
    AE "Sorry, is it annoying?"
    MC "No, no, it's soothing. What is it?"
    show AE happy
    AE "It's just a little tune by Mozart. I hope... I'll be able to hum it to my own child one day."
    MC "Yeah?"
    "Shiori-chan set her book to the side. As the sun broke through the leafy trees, it's light paling in comparison to the light radiating from her smile, she looked down at my face. For once, it was her locks draping downwards to my eyes, as the light revealed the blue hue of her dark hair."
    show AE smile
    AE "Yeah."
    "She began to playfully pet my head as we gazed in each other's eyes. I tilted my head to the side and she did the same. The chirping birds above were the only break from the serene silence between us."
    AE "Keisuke-kun I want you to know that I-"
    "As she spoke, her glasses fell from her face, bonking me on the head as I gave a hearty chuckle."
    show AE surprised
    AE "Opf!"
    MC "Keheheheh~"
    show AE smile
    AE "S-Sorry about that."
    MC "No worries."
    MC "Hm-Ahn!"
    "As I sat up from her lap, I stretched my arms and sighed a deep breath of relief."
    MC "Haaah, that was nice. I get you don't like how... erm, puffy, your legs are, but they damn sure are comfortable."
    show AE surprised
    AE "O-Oh? You really think so?"
    MC "Yeah."
    "I put my hand just beneath her skirt, and began to rub the soft, silky skin of her pillowy thigh."
    MC "I know so."
    "She began to squirm a bit as her face became bright red as I touched her leg. I knew she was sensitive, but the extent of it seemed a bit odd."
    MC "Hm... He-"
    "Before I could continue to talk, she slowly tried to sit up."
    "Her arms began to shake as she tried to lift herself from the ground."
    show AE angry
    AE "H-Ggn!"
    menu:
        "Need help?": #+2
            MC "Need help?"
            show AE embarrassed
            AE "Ahg, y-yes please."
            MC "Okay, ready?"
            AE "Mhm."
            MC "Hup!"
            "Grabbing her hands, I braced myself and lifted her up with an ample amount of strength. After a moment or two of lifting, she stumbled onto her two feet, massive bum jiggling from the inertia of her sudden movement. I pulled her close and wrapped my hand around her rear for support."
            AE "Oof."
            MC "Hah, there you go."
            $setAffection("AE", 2)
            show AE aroused
            AE "Thanks... handsy."
            MC "Ehehe."
        "Just watch":
            "I watched as Shiori struggled to get herself up from her sitting position, adjusting her body to allow her leg muscles to carry the work lifting her fat ass from the ground."
    show AE happy
    AE "Haaah, well, that was nice. We should head back before-"
    MC "Oh, yeah, one sec."
    show AE surprised
    AE "Hm? Mmph-!"
    "As Shiori turns around, I plant her with a deep kiss, pulling her in with my arm. As we embraced, I gently caressed her back as she closed her eyes as the leaves slowly fell around us."
    show AE smile
    AE "Mmmn~"
    MC "Mm-Maah~"
    MC "Okay, now we can go back."
    show AE happy
    AE "Ehehe~ Sure."
    "We followed the path of trees out towards the pastel purple sky ahead; returning to the dorms to await another day."
    jump daymenu

label AE056:
    $setProgress("AE", "AE057")
    #SCENE AFTERNOON
    scene Classroom with fade
    play music Peaceful
    "It was nearly time for homeroom to end, and I could barely keep my head focused toward the front of the class. I found myself nodding and fading for a few seconds before catching myself again."
    "I could tell that boredom and exhaustion were starting to set in for the other students as well, Mizutani-san having long since fallen asleep behind her book, Yamazaki-san quietly sitting with her eyes closed, and Kodama-chan humming her kicking little ones a lullaby as their mother started to doze off herself."
    "Even from behind, it was clear to me that Shiori was starting to slacken in posture, though she remained focused as she steadily wrote down her notes."
    HR "-should make decorous behaviour their leading principle, for the leading principle of the government of the people consists in decorous behaviour."
    "The ringing of the bell cut through the idle chatter of the other students as everyone began packing up and gathering by the door."
    HR "Aaaand there we go. Now you can leave."
    show AE neutral with dissolve
    AE "Hm? Ah, yes. Stand."
    hide AE with dissolve
    "The classroom sluggishly stood at attention and bowed."
    FMG "HHHHHHKN... chuuu~"
    "All except Mizutani-san, who continued to snooze in class."
    "I stood up quickly, trying to wake myself up and get ready to throw myself back into the whirlpool of other students making their way down the halls."
    MCT "Geeze, did he have to go over the meaning of {i}every{/i} word in the constitution?! I felt like I was gonna start bleeding out of my eye sockets."
    show AE neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    AE "Mizutani-san... Mizutani-san."
    FMG "HHHNK- Hm?! Woah, yeah?"
    show AE neutral-annoyed
    AE "Please don't sleep in class. It's disrespectful to your peers."
    show FMG surprised at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    FMG "Eh? Oh! Yeah, yeah, totally. I get it. I totally get it..."
    hide FMG with dissolve
    FMG "..."
    FMG "..."
    FMG "Hhhhhnk... chuuu~"
    AE "..."
    "Shiori simply turned around quietly and walked towards me. I started to reach out to Mizutani-san before-"
    AE "No, no, leave her be."
    MC "I- uh... I mean, sure."
    FMG "Hhhhhnk... chuuu~"
    "As I began to leave the room with Shiori in tow, a whistle came unexpectedly back from the room."
    HR "Hey. Shaggy. 'Mere."
    AE "Hm?"
    show BE surprised at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    BE "Huh? What'd I do?"
    HR "Nooot talking to you, Inoue-san. Keisuke. 'Mere."
    hide BE with dissolve
    MC "Huh? Oh, uh, sure."
    show AE sad-2
    AE "Keisuke? What's going on?"
    MC "Eh, it's probably nothing, I'll catch up with you later, I promise."
    show AE sad
    AE "...M-Mm. Right..."
    show AE smile
    AE "Right. see you in a bit, I'll be waiting in the office."
    show AE happy
    AE "Don't keep me too long."
    hide AE with dissolve
    "I stepped over to Tashi's desk by the front of the class and I couldn't help but feel a building sense of anxiety forming in the pit of my stomach."
    MCT "I wonder what he wants to talk about, he usually doesn't request people to stay after class."
    show HR neutral with dissolve
    "Tashi-sensei sighed, resting himself on the edge of the desk, his posture far more relaxed than I would have expected for wanting to talk in moderate privacy after class. His hand was resting on the table, it looked like he was resting it on top of some old assignments."
    MC "Was there something you wanted to talk to me about?"
    show HR annoyed
    HR "This isn't an interrogation. How've classes been goin'?"
    MCT "Shouldn't... you know that?"
    MC "They've been going okay, why do you ask?"
    show HR neutral
    HR "Well, I wanted to talk to you a bit about Matsumoto-san."
    MC "Oh! Um, okay, sure."
    HR "Everything going all right between you two?"
    MC "Um... sir?"
    HR "Hm?"
    MC "Why do, um..."
    show HR annoyed
    HR "Humor me."
    MC "...Pretty good, I guess."
    show HR neutral
    HR "Yeah? Good. Good. That's good to hear."
    "Tashi-sensei took a swig of coffee from his mug as he retracted his tongue, exhaling after wiping his lips with his sleeve."
    HR "Good to hear."
    MC "Aaany reason why you ask?"
    HR "...Sit down."
    MC "M-Mm."
    "As I sat down at the edge of the desk in front of him, Tashi-sensei only shrugged and held his mug with both hands as he gazed into it."
    HR "...See, we teachers, we talk after classes. We let each other know what we hear from other classrooms. Rumors, news, how students are doing, the grapevine."
    MC "Okay."
    HR "And from what I hear, words getting around that Shiori's being pretty relaxed nowadays."
    MC "Actually, sir... how is {i}she{/i} doing in classes?"
    show HR annoyed
    HR "Tch, do you really need to ask? I've honestly considered not even looking at her papers any more."
    MC "If you stopped-"
    HR "She'd gut me, I know."
    show HR neutral
    HR "But you get my point. She's an exemplary student."
    MC "Well, good."
    show HR annoyed
    HR "Not good."
    MC "...N-Not-?"
    show HR neutral
    HR "Well, no, it's good, but that's not what I mean."
    show HR annoyed
    HR "I mean, how's she doing as a {i}girl{/i}? Not a student, Hotsure-san. As a person?"
    show HR neutral
    HR "You think she's getting a bit {i}too{/i} soft?"
    MC "What? No, no, not at all-"
    HR "And that's why you asked how she's doing in class, yeah? You're worried?"
    MC "..."
    HR "Well... I gotta admit, I think this is good for her. Even if her grades {i}did{/i} take a hit, she needs to get out into the world and experience youth. Living the way she did, she'd crack for sure."
    MC "...Yeah, you're right."
    show HR annoyed
    HR "I know I'm right, kid."
    show HR neutral
    HR "Keep doing what you're doing. Let her live a little, just don't let her get carried away."
    HR "A girl like that... has lots of potential in this world."
    "With that, Tashi-sensei pushed up off the desk and started making his way over to collect his bag on the far side of the desk."
    show HR annoyed
    HR "I hate seeing potential go to waste. Seen it far too much over these years; but it's the good ones that make the job worth it."
    MC "I'll do my best sir, thank you for telling me."
    show HR neutral
    HR "Any questions?"
    MC "Um..."
    menu:
        "Are you worried about her for a reason?":
            jump AE056_c1_1
        "None, sir.":
            MC "None, sir."
            HR "All right, well... see you around, Hotsure-san."
            jump AE056_c1_after
        "How do you talk with your tongue like that?":
            jump AE056_c1_3

label AE056_c1_1:
    MC "Is there a reason you're worried, sir?"
    HR "Why do you think I'm worried about her?"
    MC "I mean... you wouldn't ask otherwise."
    show HR annoyed
    HR "...Haah... Look, kid. I've been a teacher for years. The amount of kids I've seen let their growths get to their heads... damn, I don't think I could count on both hands."
    show HR neutral
    HR "A trend I notice is that when students with the growth that Shiori has starts to get sensitive, they tend to, uh... branch out and get popular with the students, despite their looks."
    HR "Do you know what I'm saying?"
    MC "...You think that will happen to Shiori?"
    show HR annoyed
    HR "It's not unthinkable."
    MC "Yes it is."
    show HR neutral
    HR "..."
    show HR annoyed
    HR "It's hard to think of, I admit, but trust me when I say I'm not just saying this due to cynicism."
    HR "I've seen plenty of students with that growth experience it. Shiori's one of a kind, but I don't for a second think she's {i}wholly{/i} above it."
    MC "...Mm."
    show HR neutral
    HR "You all right?"
    MCT "Shiori's mentioned to me before, her fear of changing as a person... is this what she was talking about?"
    MCT "Is that what Tashi-sensei is talking about?"
    MC "Yeah, yeah, I just... You gave me a lot to think about."
    HR "...All right then, I think that's that."
    HR "Now get out of here. I got papers to grade."
    HR "Ssp."
    jump AE056_c1_after

label AE056_c1_3:
    MC "All right then... I gotta level with you. How can you talk so well with your tongue like that?"
    show HR annoyed
    HR "...Tch, smartass."
    show HR neutral
    HR "Ehh, well, I said I'd answer any questions, eh?"
    HR "Practice."
    MC "...That's it?"
    HR "What, do you think I'd have some big secret? Nah, I'm a grown man, I've had this growth since I was 19."
    MC "I... guess that makes sense."
    MCT "It... doesn't. It really doesn't."
    HR "Now get the hell out, I got papers to not grade."
    jump AE056_c1_after

label AE056_c1_after:
    "With that, I bowed and made my way out of the classroom towards the library."
    
    scene Student Government with fade
    "Pushing open the door to the student government meeting room, I could see Shiori facing the far wall. She seemed to be focused on organizing and filing away a stack of papers that had been left out earlier."
    MC "Knock knock~"
    "The noise was enough to disrupt whatever train of thought was currently racing through Shiori's mind as she seemed to refocus and look back toward the doorway. Placing her pen down with a smile, she shuffled her papers a bit and bashfully moved a stray hair out of her face."
    MC "I'd like to schedule an appointment with the president, if she's free, that is."
    show AE smile with dissolve
    AE "Did you schedule an appointment?"
    MC "Mhmm~"
    MCT "I walked over and gave Shiori a tiny peck on the cheek, who in return tilted her head to the side for another as she began to pack up her things."
    MC "How's it going?"
    AE "Mmm, pretty good. Just had to quickly jot down a few things for work. Everything all right with Tashi-sensei?"
    MC "Oh... Eh, it was nothing important really, he just wanted to check in and see if everything was going okay. My last couple assignments weren't really up to par so he wanted to make sure nothing was wrong."
    show AE aroused
    AE "Well, if you ever need help I'd be more than happy to give you a {i}private{/i} lesson."
    "Her warm, flirtatious smile was enough to push aside my current fears about her performance. She seemed practically giddy as she bounded over from the far wall to my side, her prodigious rear taking a few extra moments to settle as she wrapped herself around my arm."
    MC "You seem to be in a particularly good mood, eh?"
    show AE happy
    AE "I'm just happy to have you back by my side again, it gets particularly quiet in here when everyone else is out for the day."
    MC "Yeah?"
    show AE smile
    AE "Mhm."
    MCT "I leaned in for a proper kiss, but she put a finger to my lips and moved away a bit."
    AE "Ututut, not here. How's about we go somewhere more... private?"
    MC "All right, lead the way~"

    scene Dorm AE with fade
    "We made our way back over to her dorm room without much interruption. Shiori managed to let a giggle slip between her lips before her hand shot up to try and silence her laughter."
    "Stepping inside, we made our way over to Shiori's bed. It was uncharacteristically cluttered, with several books spread out across the sheets. Without much hesitation I reached over and slid the books to the floor, clearing enough room for Shiori and I to sit side by side."
    show AE sad with dissolve
    AE "Ngh..."
    MC "Something wrong?"
    show AE smile
    AE "N-No. It's nothing."
    AE "Here, let me get a bit more comfortable as well."
    play music Steamy
    "As we sat together on the edge of her bed, her demeanor seemed to change, she pushed into me more forcefully as we sat down, her hips spilling over the top of mine and pushing into my side."
    "As we kissed, I took of her headband and placed it amongst her books, causing her raven black hair to fall loosely in front of her glasses before she sweeped one side of her locks behind her ear."
    "As my hands rode gingerly up her skirt, I reared my hands back and gave a hearty slap to her sizable rear."
    "*SMACK*"
    show AE surprised
    AE "Kyaah!~"
    MC "Mhmm~"
    show AE embarrassed
    AE "K-Keisuke, please, I-I'm starting to feel increasingly more sensitive."
    MC "Oh yeah?"
    "I buried my nose in the side of her neck and continued to kiss her passionately as I gently rubbed the one of her engorged cheeks with my hand; the other gingerly petting her thick, pillowy leg as my fingers sunk deep into the soft skin."
    show AE happy
    AE "Nye-he~"
    stop music
    ##Door open SFX#
    Tako "H-WOAH MY GOD-!"
    show AE surprised at Position(xpos=0.75, xanchor=0.5, yanchor=1.0)
    AE "Eek!"
    "The sudden loud shout from Tako as she walked through the door and threw her bag onto her bed caused my heart to relocate itself comfortably in my throat as Shiori's panicked yelp was accompanied by her rolling of me hurriedly."
    MC "Woah, shit!"
    "Tako turned her head and covered her face with her hand."
    show Tako surprised at Position(xpos=0.5, xanchor=0.5, yanchor=1.0)
    Tako "S-Sorry! Sorry!"
    AE "I thought you were out for the night-!"
    Tako "Holy shit, can you give a girl some warning if you're gonna bring Keisuke in here?!"
    show AE embarrassed
    AE "A- I- Um-!"
    "Shiori stammered as she shakily adjusted her skirt and bent over to pick up her headband off of the ground."
    show Tako neutral
    Tako "Yo, like, you can continue if you need, but I got an exam goin' on tomorrow, man."
    AE "No, no, K-Keisuke and I were just about to leave."
    "I nodded wordlessly and stroked my long, brown locks in embarrassment. Shiori grabbed my hand and led me out of the room past Tako as she pursed her lips, held open the door for Shiori, and closed the door behind herself."

    scene Dorm Exterior with fade
    play music Hallway
    MC "Well... damn."
    show AE sad with dissolve
    AE "I am... {i}SO{/i} sorry for that."
    MC "Oh- nah, nah, no worries, I got homework due tomorrow anyways. I wouldn't want to catch an earful from... well, you."
    show AE smile
    AE "Tsh, don't worry too much about it. It's all... g-good."
    MC "Mm."
    AE "..."
    MCT "Is it just me or... did that seem a bit too... disingenuous of her?"
    MC "You feeling all right?"
    show AE neutral
    AE "Huh? Yeah. Yeah, I'm... doing fine."
    if getSkill("Academics") > 10:
        MC "Ah."
        show AE smile
        AE "Yes."
        MC "..."
        AE "..."
        MC "Ok, so, I couldn't help but notice that you seemed a bit uncomfortable when I moved the stuff off of your bed."
        show AE neutral
        AE "What... do you mean?"
        MC "Well, I dunno, you just seemed to be a bit-"
        "Shiori shook her head and smiled at me warmly."
        show AE smile
        AE "It's nothing. Really."
        MC "I... Yeah, you're right. Sorry, I'm just kind of a bit worried. Wanna make sure you're doing all right, and all."
        show AE neutral
        AE "Yes- I, um, *khm*, y-yeah, I'm fine."
    AE "So, in any case, we *probably* should continue this some other time. Maybe spend some time together after class?"
    MC "Totally."
    show AE smile
    AE "Well, then, how's about we spend some time in the music room?"
    MC "Sounds good!"
    AE "Ok! I'll bring my music sheets, so..."
    show AE happy
    AE "Yeah! I'll be seeing you, um... later!"
    MC "Yep, later!"
    "With a bow, Shiori turned around and walked back into the room. As the door clicked shut, I let out a breath of air through my nose as I consider everything that Tashi-sensei said to me. Still, though, I felt confident that I knew Shiori well enough to know she's got control of herself."
    MC "So... what to do with my day..."
    "As I began to walk down the halls, I wondered if it was just by sheer chance, or by some string of fate that the two of us could end up like this; happy with ourselves."
    jump daymenu

label AE057:
    $setProgress("AE", "AE058")
    #SCENE AFTERNOON
    scene Music Classroom with fade
    #PLAY SONG: Kinderszenen
    "Entering the music lab, the soft, gentle tones from the piano graced my ears as I slowly shut the door. I descended the stairs, and was greeted with Shiori's bench-bending behind; her skirt slightly lifted up to show a bit of exposed undergarment."
    "I walked slowly as to try to sneak up on her, adjusting my weight to the front of my feet as I slowly crept up behind her."
    show AE happy with dissolve
    AE "I've been waiting, Keisuke~"
    "Clearly, it was for naught."
    "Deciding instead to go all in, I wrapped my arms around her shoulders and gave the back of her head a warm kiss."
    MC "Looks like you've put the time to good use, eh?"
    "She glanced up at her notesheet and then back up to me, a coy smile plastered on her bespectacled face."
    AE "Might as well practice while I wait."
    MC "Practice well served. You play like an angel."
    show AE smile
    AE "Aha, no, no."
    "As she continued to play her tune, I pulled up a chair and sat next to the old piano; slouching in the seat as I crossed one leg over the other."
    MC "Hmm..."
    AE "Is that contentment, or curiosity?"
    MC "Lemme ask you this."
    MC "If you were to go anywhere in the world, where would you go?"
    AE "Hmmm..."
    AE "Well, there are a lot of places I'd like to visit: Russia, Switzerland, France-"
    MC "Top of your head. Pick one. Go."
    show AE surprised
    AE "Oh! Um-"
    show AE happy
    AE "Italy would be nice, I think."
    MC "Italy?"
    show AE smile
    AE "Mm."
    if getSkill("Academics") < 2:
        MC "I mean, I'd at least want to go somewhere warm."
        show AE neutral
        AE "...Keisuke, Italy is moderately warm."
        MC "No it's not! It's over in Europe."
        AE "..."
        show AE smile
        AE "Tsh, you're pulling my leg, right?"
        MC "Wuh- Am I wrong?"
        AE "Yes!"
        MC "So it's {i}not{/i} in Europe?"
        AE "No, it's in Europe, but on average it's a fairly warm country."
        MC "So there {i}aren't{/i} mountains or-?"
        AE "The Alps!"
        MC "Oh for-"
        show AE surprised
        AE "Dch- Are you serious?!"
        MC "Tsshh, {i}c'moooon{/i}."
        show AE happy
        AE "OH! My god!"
        MC "Geography is my worst topic-!"
        show AE smile
        AE "Keisuke!"
        MC "What!?"
        show AE happy
        AE "Are you being honest right now?!"
        MC "Oh, fu-"
        AE "Pfffff-!"
        #pause music?
        "Shiori took her hands off the keys and rested her face in them as her body began to convulse, causing her thick legs to wobble with each stifled laugh."
        MC "Eheheheh!"
        "She looked over to me, her face a light pink and tears in her eyes as she took off her glasses and covered her eyes with one hand."
        "Biting her lip, she positioned her glasses onto her face as she cleared her throat and began to play again."
        #resume music?
    else:
        MC "Nice! Nice. Anywhere in particular you wanna check out?"
        show AE happy
        AE "Hmm... St. Peter's Basilica would be nice. Cathedral of Milan, the Alps; there's just a lot of places to visit in general."
        MC "Yeah. I think Venice would be cool."
        show AE smile
        AE "Mm."
    "As she continued to play quietly, I walked over and rested my hand on the wooden frame of the piano."
    MC "Can I try?"
    show AE surprised
    AE "...You can play?"
    MC "How hard can it be? We can do a duet, even."
    AE "How hard- Okay, sure."
    MC "What, don't think I can do it?"
    show AE neutral
    AE "You are welcome to try."
    if getSkill("Art") < 20:
        show AE smile
        AE "A-ha! How's about this one then, hm?"
        MC "A-Apa..."
        AE "Appassionata."
        MC "Euch, no. Too many notes."
        show AE angry
        AE "Ach- too many notes indeed."
        show AE smile
        AE "Shall I slow it down for you, mein kaiser?"
        MC "Eh?"
        AE "Ah. B-Because, um... the emperor of Austria and..."
        show AE embarrassed
        AE "*Khm*, never mind."
        MC "Oh my God, you and your awkward jokes."
        show AE smile
        AE "Ehehe, s-sorry."
        MC "Here. I'll flip through and see if there's anything I can figure out."
        "I looked through three pages-"
        MC "Oookay! That's about enough on my end."
        AE "Figured."
        MC "Don't look so proud of yourself!"
    else:
        "I pointed to the song on the next page."
        MC "There we go. Norwegian Dance. Greig."
        show AE neutral
        AE "...Wait. Are you serious?"
        MC "What, do you think I'm not?"
        AE "I... shouldn't, but for some reason I do think you are."
        MC "Question is..."
        "I popped my knuckles as I placed my hands on my end of the keyboard."
        MC "Are you?"
        AE "..."
        show AE smile
        AE "Psssh. I used to play this song with my mentor all the time."
        #Play: Norwegian dance.
        "As we played together, Shiori's eyes flared up in amazement as I hit my notes spot on."
        show AE surprised
        AE "I-I don't..."
        AE "K-Keisuke! When did you-?!"
        MC "Shh. You'll interrupt my flow."
        show AE neutral
        AE "..."
        show AE angry
        AE "...Hmph!"
        "Proudly sticking her chin up, she matched my tune to a T. However, taking one hand off of the keyboard, I reached down."
        MC "Pinchi~"
        show AE surprised
        AE "EEK!"
        "And pinched her right cheek."
        "She brought her hands down from the keyboard and to her skirt but a moment before I did to block a potential hit."
        MC "I win!"
        show AE angry
        AE "Ghn-! I-It wasn't a competition!"
        MC "Then how did I win?"
        AE "A... hmph. Cheeky."
        MC "No, you."
        AE "Ach-!"
        MC "Nehehe~"
        $setAffection("AE", 4)
        show AE smile
        AE "...Mhmhmhm~"
        "Shiori gently flipped back to the previous page and started playing once more."
        #return to previous music
    MC "Hm~"
    show AE surprised
    AE "A-ah!~"
    "Shiori's hands went up from the keys as I made my way in front of her. First sitting on one of her gargantuan thighs, I scooted back a bit as I wrapped my arms around her and pecked her on the cheek."
    AE "Keisuke-kun, w-wha-?"
    MC "Keep playing."
    show AE neutral
    AE "With you sitting in my lap like this?"
    "I closed my eyes and nodded, nuzzling my head on her shoulder."
    show AE embarrassed
    AE "Oh, um... alright."
    "As she gently tapped away, I felt her heart daintily beating in her chest. After a while, I pecked her on the cheek and looked her in the eye."
    MC "Wanna switch positions?"
    show AE neutral
    #stop music?
    AE "I'm... not quite sure that's a good idea."
    MC "Whaaat? It should be fine~"
    show AE angry
    AE "Well, that's not exactly what I'm concerned about."
    MC "C'mooon, just try it."
    show AE neutral
    AE "Alright, fine."
    "I hopped off and scooted into the seat as Shiori then scooted in between myself and the keys. Try as she might, she couldn't help but plop her massive booty down on the keys as she straddled me."
    "*CLANG*"
    "Shiori's massive buttcheeks beared down onto the ivory keys with a loud clang as she sat on my lap. Her face turned a light pink as she heard just how much of the piano her ass covered."
    MC "E-ehh?"
    "What's more, even if her ass wasn't covering the keys, I couldn't reach past her large expanse enough to even get to them."
    MC "My hands can't..."
    show AE smile
    AE "There, see?"
    MCT "Hmm, that didn't exactly go as planned."
    MCT "..."
    show AE embarrassed
    AE "A-ahn~!"
    "Quickly, I brought my hands to rest on Shiori's ass and began to tickle her gently. Her whole body convulsed as she erupted into a sea of giggles, her arms flailing behind her, trying to swat me away."
    MC "Ahh, even without touching the keys I can make such beautiful sounds!"
    "Tracing my fingers along her tremendous behind, I brought my fingers lower to avoid her arms, and went to town. Shiori tried arching her back to reach my hands to no avail."
    show AE happy
    AE "K-Keisuke! Stop, th-that *Pft* t-t-t-tickles!"
    "Then, with one huge leap, she pulled herself very close to me and kissed me on the lips, grabbing the back of my head to pull me in even closer to her. I was so shocked that my hands took to fondling her ass instead, my fingers exploring every inch of her booty. After a short time, I pulled back to catch my breath."
    MC "Just... just as planned."
    show AE smile
    AE "Hm. Sure. However, I don't believe I told you to stop."
    "Shiori grabbed me by the shirt and pulled me in close again. As we kissed, I felt her tongue bump into my lips, as if asking for admittance. I parted my lips a bit to allow her tongue through, where our two tongues met. We sat there, our tongues doing a slow dance on the insides of each other's cheeks, locked in a warm embrace."
    "It felt like heaven. It was enough to help me forget that I was losing feeling in my legs. After what seemed like hours, my legs began to turn to jelly and slowly crumpled under Shiori. Thankfully, she caught herself on the piano."
    show AE surprised
    AE "A-Are you alright?"
    MC "Yeah, you know how you make me weak in the knees."
    MCT "I... maaay need to check and see how long my legs were without circulation."
    MC "You alright?"
    show AE embarrassed
    AE "Mm. I'm fine."
    MC "Good, could you play me another song?"
    "I stood up, albeit rather shakily, and offered her the bench. She sat down and slid it forward towards the piano and suddenly jumped back, a pained look on her face."
    MC "Everything okay?"
    AE "Yes. It's just... my thighs are a bit... in the way."
    "Shiori raised her hands from her legs, revealing a bright red line running across each one."
    show AE sad
    AE "They put a bit more distance between me and the keys than I'm used to."
    MC "I see... here. Let me help."
    show AE embarrassed
    AE "N-Ngh."
    "Shiori winced as I gently rubbed the tender skin on her thighs. Soon though, her grunts of pain turned to sighs of relief."
    show AE smile
    AE "Thank you, Keisuke."
    "Shiori sat there in silence for a while, looking at the spot where her legs had previously been slightly sore as her face went from contentment to a sudden, deep melancholy."
    show AE sad
    AE "...Haaaah..."
    MC "Hm? Everything alright?"
    AE "Y-Yeah, just... just thinking about things..."
    "Suddenly, she picked herself up from her bench, one of her bloated cheeks almost knocking my head off before I dodged out of the way."
    show AE surprised
    AE "The office!"
    "Shiori quickly grabbed her bag and her music sheet book and hurriedly placed them in her bag."
    AE "Keisuke, I must apologize, I've just remembered that I've forgotten to lock the office for the night."
    MC "Oh! Really?"
    show AE sad
    AE "Yes, yes, I know, it's careless, but-"
    MC "Nah, nah, go ahead. Go do your thing."
    show AE happy
    AE "Thank you."
    "Shiori stood and gave me a peck on the cheek before hurrying for the door. Her massive cheeks audibly clapping with every bounce as she rushed up the stairs."
    show AE smile
    AE "I'll see you tomorrow?"
    MC "You know you will."
    show AE happy
    AE "Then indeed I will."
    hide AE with dissolve
    "She made her way to the top as I walked to the door and shut it behind me. Leaving me alone in the empty music room."
    MC "Yeesh. Not like her to forget something like that..."
    "With a sigh, I pulled out my phone and clicked the on button to look at the time."
    MCT "Damn. When'd it get so late? I better head out myself."
    "I slung my bag over my shoulder and slowly made my way up the stairs, sure to click off the light on my way out."
    jump daymenu

label AE058:
    $setProgress("AE", "AE059")
    scene Library with fade
    play music Schoolday
    show AE happy with dissolve
    if getSkill("Academics") < 10:
        jump AE058_c1_fail
    else:
        jump AE058_c1_pass

label AE058_c1_fail:
    MC "Uhh..."
    MC "Let's see..."
    AE "Come now, highschool wasn't {i}that{/i} long ago. Surely you remember some things."
    MC "Ahh, cut me some slack, I've always been more of a math guy."
    "After a long day of studying and note taking, Shiori and I took some time to ourselves for..."
    "More studying and note taking."
    "Thankfully, though, it was in a topic I'd been interested in learning more about for quite some time: english."
    "And thankfully, it felt as though my labors may have been paying off."
    AE "Here. What does this say?"
    MC "Hmm..."
    MC "'Dissu... is... a pehn.'"
    AE "Good."
    "I liked to think they were at least."
    AE "Next one?"
    MC "'A catto... zea is.'"
    show AE smile
    AE "Ah, no no, in English, it goes Subject, Verb, Object."
    MC "Oh yeah?"
    AE "Mm."
    MC "Maaaan, that's just confusing."
    AE "You can do it. Just think about the {i}structure{/i} of the sentence you're trying to say."
    MC "Hrrrmm..."
    MC "'Zea... is a catto.'"
    show AE happy
    AE "Right!"
    MC "Alright! 'Veruy guud!'"
    AE "... *Snrk*... Ehehe~"
    MC "Eh?"
    show AE surprised
    AE "O-Oh! Sorry, sorry."
    MC "Whaaaat? It was good wasn't it?"
    "Shiori cleared her throat and looked up to me with a bashful smile."
    show AE embarrassed
    AE "Um, It's nothing. I just think your accent is cute, is all."
    "I tried to stifle a laugh myself, but ended up with a big, goofy grin."
    MC "Oh yeah?"
    show AE smile
    AE "Yeah! It's pretty cute. I can tell you've never really spoken to a native speaker, though."
    MC "Eheh, eh, never got much opportunity."
    MC "Still, though, I guess it's more of the fluency I care about anyways."
    MC "How am I doing on that end?"
    "Shiori looked down at my writing for a moment, as she furrowed her brow a bit."
    show AE frown
    AE "Hmm..."
    show AE smile
    AE "Well, I'd be easier if we had some supplementary materials."
    AE "Wait here. I'll fetch some books."
    "She stood up from her extra wide chair, causing it to nearly tip over as her rotund ass pushed it well out of it's way. Shiori jumped a bit as the loud clack echoed through the hall."
    show AE sad
    AE "Ech. I don't think I'll ever get used to that."
    "Placing her book on the table, she took a few steps away before I spoke up."
    MC "What about what you're reading?"
    show AE neutral
    AE "Hm?"
    MC "It looks like it has English on the front. Read some of it so I know how it's supposed to sound!"
    show AE surprised
    AE "Oh! Uhhh... Sure."
    "Sitting her giant rump back down, she opened up her book once more and looked up to me."
    show AE neutral
    AE "Admittedly, I don't think I've outright *spoken* english in a bit of time."
    MC "Naaah, I should be good! Just try it out. Start off from where you're reading."
    AE "Right..."
    AE "So, just read to you the English?"
    MC "Yeah, I wanna get a hold on how English is supposed to sound."
    AE "I see... Very well."
    AE "'Accordingly a practical philosophy not basing itself on nature, but the freedom of the will, will presuppose and require a subsequent  metaphysic pertaining to morality. It is even a duty to have such a metaphysic; and every man does, in fact, possess it in himself, although in an obscure-'"
    MCT "I completely blanked out after the first few syllables."
    MC "E-Eeeehhh..."
    AE "I'm guessing..."
    MC "Yeah. I thiiink you lost me."
    show AE smile
    AE "No worries, as long as you think you have a good grip on how it sounds like."
    show AE happy
    AE "Just try to replicate words you heard. I can practice it with you, if you want."
    MCT "T-The pronunciation doesn't help much if I have no idea what it's saying!"
    MC "Hmm ehh, let's take a break for a sec and just talk."
    show AE surprised
    AE "Oh! Okay, sure."
    jump AE058_c1_after

label AE058_c1_pass:
    "After a long day, I decided to settle down with Shiori in the library and spend some time relaxing with a nice book."
    "I leaned back in my chair a bit, one hand on my lap as the other held the book well in front of my face."
    "A warm smile crawled across that same face as I felt a warm hand glide across my own. Looking over, Shiori herself was doing the same."
    MC "Well now, you feel warmer than usual."
    show AE smile
    AE "Ahh, is that so? Maybe it's because I'm turning the pages faster than you, eh?"
    MC "Tssh, don't kid yourself. You're gonna be here all night if you keep lingering on every page."
    show AE happy
    AE "Eheheh. Fair enough."
    show AE smile
    AE "That's a fair stack of books you have yourself. Plan on a long night of studying?"
    MC "Feh, I'm just browsing at what all we have in the library. Admittedly, I think I'm starting to run out of stuff relevant to my interests, I guess."
    AE "That's just as much a blessing as it is a curse. The library is {i}very{/i} extensive, after all."
    MC "Ehh, true, true."
    MC "How about you?"
    show AE happy
    AE "Ah! I'm reading Kant's 'Metaphysics of Morals'."
    show AE smile
    AE "Have you ever read any of his works?"
    MC "Hmm... Nah, I don't think I have. But I know who he is."
    show AE neutral
    AE "'Accordingly a practical philosophy not basing itself on nature, but the freedom of the will, will presuppose and require a subsequent  metaphysic pertaining to morality. It is even a duty to have such a metaphysic; and every man does, in fact, possess it in himself, although in an obscure-'"
    MC "Ahhh, interesting."
    MC "That sure is a lot to unpack, though. 'Moral Metaphysics'? I don't think I've seen those words put together like... well, that."
    show AE smile
    AE "Mm. It's a somewhat abstract idea, buuuut I like it. It's a pretty interesting theory."
    MC "Do you read a lot of stuff like this?"
    show AE neutral
    AE "From time to time. Actually, if I'm to be honest, I don't read many books in Japanese unless I can't find an English version."
    MC "Oh, really? Why's that?"
    AE "Well, it's always good to keep my skills sharpened. If you don't stay vigilant with your skills, they'll be gone before you know it. That's why I always like to read in English when I can."
    jump AE058_c1_after

label AE058_c1_after:
    MC "Who's your favorite writer of all time?"
    show AE smile
    AE "Ah, that'd be Erasmus of Rotterdam."
    if getSkill("Academics") < 30:
        MC "Hmm... Gotta admit, I don't think I've ever heard of him."
    else:
        MC "Erasmus of Rotterdam? Hmm..."
        MC "Yeah, I think I know who that is. Dutch philosopher, right?"
        AE "Y-Yeah! Exactly right!"
        MC "I'm always surprised at just how much you know."
    MC "Why him?"
    AE "Ah! Well, other than personal reasons, I suppose that it'd be because I like his idea of 'Docta Pietas' or 'Learned Piety'."
    MC "Learned piety?"
    show AE happy
    AE "Mm. I believe it was that 'studies culminate manners'. I don't think I could put it better myself."
    MC "Studies culminate manners? Hmm..."
    menu:
        "I agree.":
            jump AE058_c2_1
        "I disagree.":
            jump AE058_c2_2

label AE058_c2_1:
    MC "Yeah, I can see that. The more you learn, the better a person you can be, right?"
    show AE smile
    AE "Right! I mean, Docta Pietas was used in a different context, but the same can be said for any field of study."
    AE "What better way to learn right and wrong thaen culminating the skill sets for mindfulness through study?"
    MC "Yeah, though to be honest, there {i}is{/i} such a thing as overdoing it."
    show AE neutral
    AE "Hm? What do you mean?"
    MC "Weeell, I've just been thinking..."
    jump AE058_c2_after

label AE058_c2_2:
    MC "Nah, I can't say that sounds right to me."
    show AE neutral
    AE "Oh? Why do you say that?"
    MC "Eh. There are plenty of scummy politicians and lawyers and the like, and they all seem to have good educations, yeah? Surely there must be more to morals than cultivating them through studies?"
    AE "W-Well of course, but looking at the converse of that, learing what's {i}legal{/i} is different from being aware of what's right. It's a matter of properly learning from your studies rather than just using them as tools."
    MC "Hmm... I dunno. I still can't say I see it."
    show AE sad
    AE "Ah... That's alright, then."
    MC "And what about you?"
    show AE neutral
    AE "Hm?"
    jump AE058_c2_after

label AE058_c2_after:
    MC "You want to study law, right?"
    show AE smile
    AE "Of course."
    MC "If that's the case; why study all this other stuff?"
    "Shiori took a moment to think, her finger tapping against her book, as she then nodded and answered."
    show AE happy
    AE "Well, you know, philosophy and history are two of the most popular fields for pre-law. I think it's natural for me to-"
    MC "Well, nah, yeah, I get that, but there's lots of other stuff too."
    MC "Most people have subjects they're good at, and some stuff they're just bad at. No shame in it, it's just how things are."
    MC "But you, I mean, math, history, science, you really are a jack of all trades with all sorts of random topics."
    MC "Why is that?"
    show AE neutral
    AE "I mean, I wanna pass, right? Everyone {i}wants{/i} to pass their classes. If you're asking why I try with such vigor, well, I suppose it's just in my nature. Being studious is part of who I am."
    MC "Yeah, but usually people just forget that kinda stuff when they pass the class. You just seem to absorb every little detail. That seems like more than just 'being studious' to me."
    show AE happy
    AE "Well, aren't you Mr. inquisitive."
    show AE neutral
    AE "Well... I simply did everything I could to make sure my teacher's efforts never went to waste."
    show AE happy
    AE "And I like learning! It's fun."
    show AE smile
    AE "Besides, think about it, wouldn't you want a lawyer, judge, what have you, to know as much about the world as they could? That way, you get the best rulings you can get."
    MC "Yeah, I can get that... but is there something more to it? Is there anything more than just your goals to be a lawyer?"
    show AE neutral
    AE "I suppose... one of the reasons I admire studying is because, well... 'studies culminate manners', right?"
    MC "Heh, alright, alright, I get it. Though I can't imagine you ever needing to learn about being well behaved."
    "Shiori stared at her book for a moment before nodding with a weak smile."
    show AE smile
    AE "...Well, eheh, we all have to start somewhere, right?"
    show AE neutral
    "Her smile faded as she bit her lower lip. After a quick shake of the head, her smile returned and she closed her book."
    show AE smile
    AE "And we never stop learning. I'll always be thankful for that."
    AE "And I'll always be thankful for my teachers along the way."
    show AE happy
    AE "Especially one of my greatest."
    MC "Oh yeah? Your piano teacher?"
    show AE smile
    AE "Well, yes, but..."
    show AE happy
    AE "You, Keisuke. You've been one of my greatest teachers."
    MC "Ahh, come here."
    "I pulled her in close and gave her a peck on the cheek. As a pink blush swept across her face, she giggled for a moment before turning to kiss me as well."
    AE "Hmm~"
    show AE smile
    AE "Well, I suppose that should be it for today. Shall we head back?"
    MC "Sure, sure. Just let me put these back."
    AE "Right!"
    MC "..."
    show AE neutral
    AE "..."
    MC "おい, 栞?"
    show AE neutral
    AE "ええ? はい?"
    MC "ありがとうございました."
    show AE happy
    AE "...You're welcome."
    MC "えへへ~"
    AE "Ehehe~"
    "After our little multilingual encounter, we decided to walk back to the dorms for today. Though we'd only known each other for a moderately short time, I'd been slowly realizing that there has never been anyone in my life who I'd been closer to."
    "No matter what the language, I wished to tell her that in any way I could."
    jump daymenu

label AE059:
    $setProgress("AE", "AE060")
    scene Hallway with fade
    play music Peaceful
    "Shiori-chan and I walked down the halls hand in hand once more. We made note of everything that had happened in our day; from Daichi's antics to Tako's wildness. It felt like only yesterday that we took our relationship to the next level, and yet today everything seemed calm, simple."
    show AE happy with dissolve
    AE "Hmm~"
    MCT "Hah... It's nice seeing her like this."
    MC "Class interesting to you today?"
    show AE smile
    AE "Ah, yes, however that's not why I'm so... contented."
    MC "Oh? Care to share?"
    AE "Mmm, well... It's a beautiful day out, and I figured..."
    MC "Yeah?"
    AE "Would you like to go and sit by the fountain?"
    MC "Oh?"
    "Her proposition seemed to come out of nowhere. We'd never been to the fountain before."
    show AE happy
    AE "It's soothing. I sat there the other day after work. Would you like to come?"
    MC "Oh, absolutely."
    "We turned the corner and exited out of the doors to the right, leaving to the courtyard."
    
    scene Campus Center with fade
    #Scene change fountain (Just courtyard for now)
    "She led me to the fountain by hand, however I was the one to usher her down. She sat on the stone edge, her humongous butt piling out on the surface. I sat close to her, and she put her hands on her thighs after patting the fountain for good measure."
    MC "Haaa, you're right. It is nice out today."
    show AE smile with dissolve
    AE "Yeah. Breezy, nice scenery."
    MC "Hm..."
    show AE neutral
    AE "..."
    AE "Keisuke-kun?"
    MC "Hm?"
    show AE sad
    AE "Be honest with me, will you please?"
    MC "Hm?"
    AE "How do I look?"
    "Shiori-san looked at me softly, yet in a straightforward manner."
    MC "Completely honest?"
    AE "Y-yes."
    MC "You're one of the most beautiful women I've ever seen."
    show AE embarrassed
    AE "Oh, come now."
    MC "I'm serious. I mean, you don't wear makeup, and yet every time I look at you I can't help but be reminded of how beautiful you are."
    show AE surprised
    AE "O-oh."
    "Shiori-san wiped her hair off to the side and looked at me through the sides of her eyes, a bright smile shining across her face."
    show AE happy
    AE "Thank you, Keisuke-kun. I'll... take that to heart."
    MC "Ehe..."
    "I scooted closer to Shiori-chan, placing my hand on hers."
    MC "All right, then... How do I look?"
    show AE neutral
    AE "Hm?"
    MC "What do you say? Am I handsome?"
    show AE smile
    AE "Mmmm."
    "Shiori-chan smiled and bit her bottom lip, her blush becoming more and more prominent across her cheeks."
    AE "I believe so."
    MC "Atch- Believe so?!"
    show AE happy
    AE "Haha~"
    MC "What's that supposed to mean?!"
    MC "I knew you were honest, but cut me some slack!"
    show AE embarrassed
    AE "Well, it's a bit hard to judge. Your face is obscured and all, heh."
    MC "Oh?"
    MC "Hmm."
    "I thought to myself a bit before responding."
    MC "Here, lemme try this."
    "Dipping my hand into the pristine water in the fountain, I swirled my hand around a bit to make sure it was nice and wet. Pulling it out, I brought it to my face and quickly slicked my hair back; my head tilting a bit as I did. Shiori's mouth opened agape when I looked in her direction."
    MC "So, how is it?"
    show AE surprised
    AE "..."
    "She began to blush bashfully as she twiddled her fingers."
    AE "Y-You're... You look like a different man altogether!"
    MC "Awww c'mon now."
    show AE embarrassed
    AE "I think... um..."
    MC "What?"
    show AE surprised
    AE "I think this is the first time I've seen your eyes..."
    "I let out a small laugh and hung my head, before looking back up at her coyly."
    MC "Yeah?"
    show AE smile
    AE "Y-yeah."
    MC "Y'know... I actually remember the first time I saw you without glasses."
    AE "Really?"
    MC "Yeah. You were cleaning your glasses after the rain."
    AE "Hmm~"
    "Shiori-san took of her glasses. It was the first time I think we ever truly got a glimpse at each other's full faces."
    MC "Yep. Just as beautiful as you've always been."
    show AE happy
    AE "Ehehe~"
    "I leaned in, and she reciprocated with her lips. We stayed like that for a few minutes, only daring to let go once we realized the passage of time."
    MC "Mmn~"
    show AE surprised
    AE "Mmm-Ah, the bell."
    if getSkill("Art") < 6:
        MC "R-really? So soon?"
        show AE happy
        AE "Hmm, don't worry, Hotsure-san. My meeting will only be an hour or so. Until then~"
        "Shiori-chan pecked me once more quickly on the cheek."
        show AE smile
        AE "Let that tide you over."
        if getSkill("Art") >= 4:
            MC "Mhm, you know it won't."
            show AE happy
            AE "Hmm~"
    else:
        MC "Gods forsake it. Every second with you is timeless."
        show AE happy
        AE "O-oh!"
        "I pulled Shiori-san in for another kiss, and without hesitation she wrapped her arms around me once more. After a final long embrace, I let her go."
        show AE smile
        AE "Hahn~ Now I'm really going to be late."
        MC "Mhm... You can make it."
    "Shiori-chan looked back at me with a smile as her hand slowly slipped from mine. I watched her now-massive rear bounce and wobble up and down as she hurried along, bag under her arm."
    "I let out a sigh as I leaned back onto the cold concrete of the fountain, my hand rubbing the warm spot where my lover's bountiful body had just been as my thoughts raced with passion."
    "I looked down into the water. Honestly, it'd been awhile since I'd seen my own face, either. I looked at my reflection for a moment."
    MC "Hmm..."
    "I stared at myself a bit longer, before stroking my hair gently. At this point, it must have at least reached to my mid back. I lifted my head, and took a look at my straight black locks in my hand before letting them fall."
    MCT "It won't do to wait here until she's back. I should head in and wait by the door."
    if getSkill("Art") > getSkill("Academics") and getSkill("Art") > getSkill("Athletics") :
        "I stood up and pulled out my fine arts book to read and pass the time. Putting it under my arm, I began to walk inside towards the office. I only got a few feet away from the fountain before turning back. I stared at the pool one last time before solemnly heading inside."
        $setSkill("Art", 1)
    elif getSkill("Academics") > getSkill("Athletics"):
        "I stood up and pulled out my science book to read and pass the time. Putting it under my arm, I began to walk inside towards the office. I only got a few feet away from the fountain before turning back. I stared at the pool one last time before solemnly heading inside."
        $setSkill("Academics", 1)
    else:
        "I stood up and pulled out my fitness book to read and pass the time. Putting it under my arm, I began to walk inside towards the office. I only got a few feet away from the fountain before turning back. I stared at the pool one last time before solemnly heading inside."
        $setSkill("Athletics", 1)
    jump daymenu

label AE060:
    $setProgress("AE", "AE061")
    #AFTERNOON
    scene Library with fade
    play music Hallway
    "Entering the library, I once again found myself greeted with a mostly empty room, save for a few members of student council having a chat at one of the free tables."
    "Meetings had thankfully been getting much shorter for her, and I could tell. She seemed way less high strung, and the council itself began to relax a bit more in her presence."
    MC "Yo! Is Shiori in the office?"
    Student "Yep, head on in."
    MC "Thanks."
    Student "Oh! By the way, Keisuke?"
    MC "Hm? Yeah?"
    "The girl motioned for me to come in closer, and spoke with a whisper as she covered the side of her face with her hand."
    Student "I don't know what you did, but for a good while, the president has been {i}really{/i} happy."
    Student "Thanks for finally getting her to calm down a bit!"
    MC "Eheh, weeell, no worries. I'm just glad I can make her happy."
    "With a smile on my face, I turned around and opened the door to the office."

    scene Office with fade
    MC "Hey!"
    "Shiori sat at her end of the table, elbow on the table, her head resting gently on her hand as she tapped at a paper in front of her with her pen."
    show AE happy with dissolve
    AE "Ah, Keisuke! I was waiting for you."
    MC "Oh, sorry, were you working on something?"
    show AE smile
    AE "No, no, don't worry about it. It can wait until later."
    "She put her pen down by some of the blank papers, and looked to me with a smile."
    show AE happy
    AE "So! How are you today?"
    MC "Good, good, just been thinking about you a lot."
    show AE smile
    AE "Good things, I hope."
    MC "Always."
    "Walking over, I knelt down and gave her a kiss on the cheek."
    AE "Hmm~"
    MC "Wanna come up to the roof with me? It's a pretty clear day out."
    AE "I'd love to."
    "Standing up from her seat, she braced herself with the table before catching her balance and sauntering over; her wide hips making minor dips with her every step."
    "I followed her closely behind as we left the office and headed up the stairs."

    scene Roof with fade
    #Quail Sfx
    "We sat under the blue sky on the metal bench as we talked about our day. Usually wide enough to fit us both, I found that Shiori's ass was slowly starting to take up more and more space over the span of our time together, and causing her thick thighs to rub up gently next to my own legs."
    MC "With winter on the way, I'm glad we're spending more time outside before it gets freezing."
    show AE happy with dissolve
    AE "Got your snow clothes ready?"
    MC "Yep."
    show AE smile
    AE "Good. I don't want you coming down sick."
    MC "...Well what about you?"
    show AE neutral
    AE "No need. I'm used to cold winters."
    MC "Ahh, c'mon, we gotta get you a coat."
    AE "I'm serious. I used to live in Hokkaido in a house without heating, I can handle a bit of cold weather."
    MC "Naah, I won't let you go out in the cold like that, you'll freeze your ass off in that skirt."
    show AE sad
    AE "Eugh, gladly. My body is absolutely grotesque."
    "Shiori grimaced as she looked back at her own posterior. Hanging her head down, she rubbed her meaty thighs in front of her as her soft, pale flesh squished around her hands."
    AE "Nngh..."
    MC "Trust me, hon, it's not too big."
    AE "It's {i}beyond{/i} too big."
    if getSkill("Arts") > 17:
        MC "Is the sky too blue? Is the sun too bright?"
        MC "You're a sight to behold; a wonder. You're not {i}too{/i} anything."
        show AE smile
        AE "Pssh..."
        show AE happy
        AE "You're certainly {i}too{/i} sweet."
        MC "Eheh, I try my best."
    MC "I mean... I think you're plenty beautiful."
    show AE smile
    AE "Hm... Well, I'm glad you like my body still."
    show AE happy
    AE "...Hon."
    MC "Caught that, did you?"
    show AE smile
    AE "It's the first time you called me that."
    MC "Heh, I guess it is."
    MC "I guess it is."
    show AE happy
    AE "Ehehe~"
    MC "..."
    show AE smile
    AE "..."
    "We sat in silence together as I reclined back on the bench, my hands holding the back of my head as I let out a breathy sigh."
    MC "Hey, Shiori?"
    AE "Hm?"
    MC "Am I... y'know, a good boyfriend?"
    show AE happy
    AE "Best I've ever had."
    show AE neutral
    AE "Why?"
    MC "Baah, I'm just worrying too much. Just some whispers here and there from others."
    show AE sad
    AE "...It was when I cleaned your cheek after lunch, wasn't it?"
    MC "Huh? No, I-"
    AE "Uch, I'm sorry, I really can't help myself sometimes. You had every right to tell me to knock it off."
    MC "N-No, no, I thought it was cute! I was just a bit embarrassed at the time."
    MC "It's just... haah..."
    MC "I dunno... I just worry I'm not man enough for you."
    show AE neutral
    AE "Man enough?"
    show AE sad
    AE "Where's this coming from all of a sudden?"
    MC "...Baaah, it's nothing. Don't worry about it."
    show AE neutral
    AE "..."
    if not getFlag("AE003_c1_1"):
        MC "Those assholes..."
        show AE surprised
        AE "Huh? What was that?"
        MC "Neeh... It's nothing."
        show AE neutral
        AE "What happened?"
        MC "...I'm sorry. I overheard a couple of guys saying some messed up stuff about you again."
        AE "Ah. I see."
        MC "I just... sat back and didn't say anything."
        MC "I know you told me a while ago that's the best thing to do, but... I just felt like such a damn coward. I let them dishonor you, and I couldn't even say a word."
        show AE sad
        AE "Keisuke, do you know how often I hear people talking about me being an... {i}uppity{/i} woman?"
        show AE neutral
        AE "It's perfectly fine, I'm used to it."
        MC "It's not fine! You're my girlfriend now, I can't just let people trample all over you like that."
        show AE sad
        AE "It... unfortunately comes with the position."
        MC "Ngh..."
    show AE smile
    AE "Aww, come now, there's no need to be so dour."
    "Placing her hand on my chest, she stood close and looked up to meet my eyes."
    show AE happy
    AE "You're all the man I could ever need."
    "Pulling me in, she pecked me lightly on the cheek and whispered in my ear."
    show AE smile
    AE "And the only man who I've ever let inside me~"
    MC "Hmm~"
    "Wrapping my arms around her waist, we began to sway side to side together."
    MC "Gotta say, the hair at least has the bonus of letting me come here to meet you, eh?"
    AE "Ehehe, I suppose that's one way to look at it."
    MC "It's the only way to look at it."
    show AE happy
    AE "Of course, with that yeti hair of yours it was only a matter of time before you decided to climb my mountains~"
    MC "O-Oy!"
    show AE smile
    AE "Ehehe~"
    MC "If you're not careful..."
    "With a single hand, I put my thumb and fingers on Shiori's soft cheeks and squished her face, making her normally thin lips puff out as she unintentionally made a silly face."
    MC "Those pretty lips of yours will get you in trouble!"
    show AE surprised
    AE "Eehp! Keethuke! Schtop!"
    MC "Squish, squish~"
    show AE embarrassed
    AE "Mmph! Pah, y-you scoundrel! My cheeks are sensitive!"
    MC "Oh, trust me, I know."
    show AE angry
    AE "...Opf! Why you-!"
    MC "Ahahaha!"
    "*Twack*"
    MC "Ha-Ow! Heeey, that hurt!"
    AE "Hmph! Serves you right."
    MC "Nehehe, sorry about that."
    show AE smile
    AE "Hmm~"
    show AE happy
    AE "You're lucky you're so cute."
    MC "Speaking of sensitivity, has it gotten any better?"
    show AE neutral
    AE "..."
    show AE sad
    AE "Worse."
    MC "Eh? Really?"
    show AE embarrassed
    AE "Y-Yeah."
    AE "It's led to some... humiliating situations."
    MC "Naah, hell, who knows, this may even only be a temporary thing."
    MC "With how much you work your ass off, you can probably lose it in a day!"
    "I gave a hearty chuckle as I pulled back and smacked her ass with an open hand, causing her entire puffy lower body to ripple."
    show AE surprised
    AE "N-NYAAAGH~!!"
    "Shiori's eyes shot open as her mouth went agape. Her knees went weak, causing her to collapse onto the floor with a thud, stopping herself with her hands."
    MC "Woah! Shit, that was loud."
    show AE angry
    AE "K-Keisuke, p-p-please, don't do that in public-nnf!"
    "Trembling on her knees, her ass completely engulfing her feet, I walked in front of her and outheld my hand to help her up."
    MC "Sorry! Sorry, I didn't think about it before I... Sorry."
    show AE embarrassed
    AE "Haah... Pah..."
    AE "Nngh... Now I'm... kind of hot..."
    MC "Oh?"
    show AE angry
    AE "Hahhn~ You devil..."
    show AE smile
    AE "How're you gonna fix this?"
    MC "Hmm... I dunno. I think I may just head back for the night. See you-"
    show AE sad
    AE "W-What? No, don't leave me like-!"
    MC "Nehehe, c'mon, did you really think I was gonna leave you high and wet- I mean, dry, like that?"
    MC "C'mon. Let's hit up your room. I wanna try something."
    "I grabbed on to Shiori's shaky hand as I opened the door. Heading back down the stairs, we went over to the dorms and made our way to Shiori's room."

    scene Dorm AE with fade
    show AE happy with dissolve
    AE "Ohh, heavens above, this is {i}so{/i} humiliating~"
    MCT "She says that... but it sounds like that's exactly why she's letting me do it."
    "Shiori put both hands on her desk as she bent over, massive legs fully exposed as her panties were pulled down just enough to expose her mighty cheeks."
    MC "Let's start. Just tell me the word after I write it."
    show AE embarrassed
    AE "Uhuh..."
    "With the tip of my finger, I pressed on her left cheek, causing Shiori to squeak audibly."
    MCT "Something she couldn't just guess..."
    MC "Mhmm... and..."
    AE "O-Orange."
    MC "Yeah! Exactly right! One point, Shiori!"
    MC "Now..."
    MC "Leeet's see here."
    "Taking the tip of my finger I traced my name across her bare cheeks as Shiori once more bristled."
    AE "'K-Keisuke Hotsure.'"
    MC "Yeah! That's right too!"
    AE "Haaah... Keisuke, this feels... so-ho... mmmn!~"
    MC "Yeah?"
    AE "Nngh~"
    MC "How's about this then?"
    "I traced the characters along my fleshy canvas with a smirk on my face."
    show AE aroused
    AE "Ohoo~"
    MC "Bet you're regretting teaching me more complex Kanji now, eh?"
    MCT "How's about I {i}really{/i} leave her blushing?"
    MCT "I lov-"
    "*CREAK*"
    stop music
    show Tako surprised
    Tako "WOAH, SHIT!"
    show AE surprised at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show Tako surprised at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    AE "EEK!"
    MC "Woah, whoa- Uh-!!"
    Tako "Seriously?! Again?"
    MC "Yureno-san, I-uh!"
    "Shiori panickedly pulled up her panties and hiked down her skirt, causing a minor rip to form near the top as she inspected the damage."
    Tako "I swear, I'mma change the lock one of these days."
    show AE embarrassed
    AE "I-I-I-I-"
    Tako "Didn't know it was date night, damn."
    Tako "I mean, I can head out for a bit if you wanna finish, or-?"
    show AE surprised
    AE "N-No, I think we, um-"
    MC "Yeah, I was gonna head out in a bit."
    show AE neutral
    AE "Yes-"
    show Tako neutral
    Tako "Ah, alright, cool-"
    AE "That's probably a good idea."
    Tako "Cool."
    show AE happy
    AE "I'll escort you out, Hotsure-sa-, Keisuke."
    MC "Yep, yep."
    "We made our way past Yureno-san, who's massive hips proved to be a bit of trouble to get past at first; eventually leading us to the outside as we shut the door."
    
    scene Dorm Exterior with fade
    play music Hallway
    show AE angry with dissolve
    AE "{i}Why{/i} did I forget to lock the door? Uch..."
    "Sighing, Shiori took off her glasses and massaged her eyes; her face still pink from our session."
    show AE sad
    AE "I'm sorry, Keisuke, I-"
    MC "No, no, it's my bad."
    show AE neutral
    AE "Haah... Well, uh... I suppose... I'll see you around?"
    MC "Yep! Thanks for the-"
    AE "Yeah, yeah."
    MC "Mm."
    AE "..."
    show AE happy
    AE "By the way, Keisuke?"
    MC "Hm? What's up?"
    show AE embarrassed
    AE "I hope you don't mind, but could you come to the office tomorrow? I could use a hand."
    MC "Oh! I mean... Sure. Sounds good."
    AE "Okay."
    MC "'Kay."
    AE "S-See you tomorrow."
    MC "Tomorrow, then."
    hide AE with dissolve
    "As Shiori was closing the door, I was able to catch a bit of the oncoming conversation on the other side."
    Tako "Did you do it for him?!"
    AE "N-Not yet! I thought you were supposed to be a-"
    #*Door Close SFX*
    jump daymenu
    
label AE101:
    scene Gym with fade
    show FMG neutral
    MC "Twelve..."
    FMG "COME ON HOTSURE, GO AT IT LIKE YOU HAVE A PAIR!"
    "Akira-san jeered me on as I lay on the mat... I never even asked her to come over, she just saw what I was doing and started shouting."
    MCT "NNggggh, if I do any more I might end up vomiting. Just. ONE. MORE!!!"
    MC "AGH!"
    "As I reached thirteen, I felt my body give way as I collapsed onto the mat with a loud thud. Akira-san stood over me smiling."
    FMG "So... How do ya feel?"
    MC "Like I'm gonna die."
    FMG "I'm impressed, dude. I've never seen a near fatality from thirteen sit ups before."
    "Despite my protests, Akira-san picked me up by the shirt with one hand and plopped me down on a bench."
    FMG "Y'know Hotsure-chi, if you wanna build up muscle right, you gotta start off a bit slow, hell, someday you may be able to do more than a seven year old!"
    "Akira-sans boisterous laugh echoed through the gym, as I turned a shade of crimson. I covered my face with a hand and looked to the side to hide my shame when I came across someone who I would have never expected to see here. Akira-san, however, appeared to notice first."
    show FMG neutral at Position (xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    FMG "OOOOOI, Matsumoto-chi, what's up!"
    show AE neutral at Position (xpos=0.75) with dissolve
    "Shiori-san looked over towards our direction and, in acknowledgement to Akira-san's waving, nodded before going back to her clipboard."
    FMG "Awwww, what's with that crap?! Come on over dude!"
    AE "I'm fine, thank you."
    FMG "Aww, come on now, I'm chillin with Hotsure-chi; don't you wanna come over? I can save you a seat on the bench... though you'll probably need two! BAHA!"
    MCT "Ow. I mean, I get it was with good intentions, but that was harsh."
    "Shiori-san closed her eyes and gave a deep inhale, before going back to her examination of... whatever that machine is."
    AE "And have you sweating all over me? No. That won't be happening."
    FMG "Hmmm... A'ight."
    "Akira-san stood up and out of nowhere..."
    MC "Eh? A-AH!"
    "Lifted up the bench with one arm. My body lying prone on the bench as Akira-san walked the bench and I over to where Shiori-san stood. Obviously disdainful of the display she was seeing, Shiori-san looked Akira-san directly in her eyes with a scowl on her face."
    AE "Mizutani-san, that is school property! Put that down this instant!"
    MC "W-what about me?!"
    AE "I was talking about you."
    MCT "It hurts just a little."
    FMG "Haha, all right all right."
    "Akira-san placed the bench down with me in tow, still shaking from the experience."
    AE "Back where it belongs."
    FMG "You just said put it down though."
    AE "Nggh... Just make sure you put it back before you leave."
    FMG "Can do!"
    "Shiori-san went back to her paperwork unamused as Akira-san started humming to herself."
    FMG "Sooooo, whatcha doin?"
    AE "Taking inventory of the exercise equipment."
    FMG "Bitchin."
    AE "Language!"
    FMG "Ehehe, sorry."
    "Shiori-san was about to go back to her work before she turned around and faced Akira-san, something on her mind as it appeared."
    AE "Actually... why are you here?"
    FMG "Uh, duh! Working out! And I thought you were the braniac."
    AE "You know that's not what I meant. Why would you work out?"
    FMG "Uhh... to gain muscle?"
    AE "But... what? I thought your file stated that you have muscular growth... Why would you accelerate it?!"
    FMG "Because it's fun, dude!"
    "Shiori-san seemed somewhat unnerved by this answer."
    AE "Fun? Is that a joke?"
    FMG "Nah... It's who I am. I'm strong, it's kinda my thing."
    AE "I would understand why you would see it as inevitable, but to accentuate it... insulting. Unforgivable."
    FMG "Hey man, I do me and you do you, but I think you might wanna work out too!"
    MCT "Ehhh?!"
    AE "Now you're just saying ridiculous things to cover for yourself. Why would I want to get sweaty and further exhausted then my work is already making me?!"
    FMG "Well, I like gettin big and from the way you talk, it sounds like you don't wanna be big. Maybe a bit of exercise would do something for those ham-hocks of yours."
    MCT "GAH! AKIRA-SAN WHY?!"
    AE "W-why you!"
    "Angered at first, Shiori-san looked like she was about to go off on Akira-san... but her anger gave way to something else. She looked down for a minute and then behind her to her... assets."
    "There was no denying it. Shiori-san had more than just junk in the trunk, she had a full on garbage barge. She slowly moved her hands down to her rear and ran them across the sides of her blooming cheeks. It looked like she had shoved two fleshy globes into her skirt."
    "Despite her best efforts, her undergarments had a noticeable outline on her clothes, leaving little to the imagination as her big bubbly booty jiggled and swayed from side to side with every step. She hated it."
    AE "Is... is that so?"
    FMG "Well, have you tried it?"
    AE "No... I never considered it as an option... All my research indicated that..."
    FMG "Dude, ya can't knock it until you try it!"
    AE "...Very well. Consider this an experiment, I will exercise with you-"
    FMG "Woohoo!"
    "Akira-san snatched the clipboard from Shiori-sans hands, making her jump in shock."
    FMG "You won't be needing this!"
    "Akira snapped the board with a slight movement of her hands."
    AE "...After I am done working... I was using that."
    FMG "O-oh... whoops... sorry."
    "Akira-san tried to jam the pieces back together as Shiori-san rubbed her eyes with her fingers."
    MCT "Why do I feel like... this isn't the last time I'll see these two go at it?"
    jump daymenu
    
label AE102:
    scene Hallway with fade
    "And so, we have reached the end of school for the day. I was going to just head back to my dorm room, however I saw Shiori whispered something to Akira before both of them left the room. I was just going to leave it alone, but unfortunately there still outside the classroom for all to hear."
    FMG "For that last time, I ain't buttoning my shirt no matter what the stupid dress code says!"
    AE "It is indeed the last time, Mizutani-san, because you WILL be wearing your uniform properly. If you would have listened to me the first time, this wouldn't have been an issue."
    FMG "If you listened the first time, you know I'm not going to button it, not for you or anyone! What is the big deal, it's not like I'm wearing something that shows anything I'm not supposed too!"
    MCT "Ohhh boy, this looks like trouble. If I don't intervene soon these two are going to be going at it for hours."
    show FMG angry at Position (xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show AE angry at Position (xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    AE "It's not about what you're wearing, it's about what you're NOT wearing. The student handbook page 45-"
    MC "H-hey girls, what's going on?"
    FMG "Little miss honor role here is bugging me about how my shirt isn't buttoned. Oh and by the way, I've been using that handbook to keep the table in my dorm room balanced!"
    AE "Oh so you do know it exists. Good."
    MC "Oookay, yep, that-uh-"
    MCT "Think of something, Hotsure, quick!"
    menu:
        "Defend Shiori":
            jump AE102_c1
        "Defend Akira":
            jump AE102_c2

label AE102_c1:
    MC "Hey, Akira-san, it doesn't seem like that big of a deal. I mean, rules are rules, right?"
    show FMG sad
    FMG "Rules!? Rules!? I thought the whole point of this school was to be comfortable with our bodies, but instead you guys are ganging up on me! *shiff* I would have thought you'd understand Kei!  And Shiori, you're a heartless bitch!"
    "Without so much as a word, Akira ran off down the hallway with fresh tears falling behind."
    hide FMG
    show AE sad
    AE "N-now Mizutani-san, hold on!"
    "Shiori-san let out a sigh once she realized that Akira-san was long gone."
    show AE angry at Position (xpos=0.5)
    AE "Hotsure-san, why did you have to intervene? I had the situation under control."
    MC "Because if I hadn't that argument could have gotten out of hand, not to mention how it would have gone on forever."
    AE "And a student running off crying isn't out of hand?"
    "Shiori-san took a seat nearby and rested her hand on her head."
    show AE neutral
    AE "I... I'm sorry Hotsure-san. You're right. Mizutani-san made her own decisions, you merely tried to keep the peace."
    MC "And I'm sorry for just running in thoughtlessly."
    AE "Hmm."
    "Shiori-san got up and began to pace, twiddling her fingers behind her back."
    AE "Still, however, Mizutani-san's reactions were a bit more severe than I anticipated. I didn't expect her to start crying and run off. Definitely not a normal reaction to a simple reprimand."
    MCT "She screamed that you were a bitch and you think that's 'a bit' more severe?"
    MC "Well. I mean, she felt cornered and angered."
    AE "That's more than just feeling cornered. I saw it in her eyes. There's more to this, and it has something to do with her shirt. It's only a matter of time until I find out what."
    MCT "..."
    MC "You know, Shiori-san, she did have a point. Why were you so adamant about her shirt?"
    AE "Because it's a rule."
    MCT "Uhhh, okay? That's not what I-"
    AE "Because I must be. I have to."
    show AE sad
    "Shiori-san began nibbling at the end of her thumbnail."
    AE "If I don't, then..."
    MC "...What?"
    AE "..."
    show AE neutral
    AE "Nevermind. It's not a topic for now. If you see Akira-san after this, apologize to her."
    MC "For you?"
    AE "For yourself. My apology will mean nothing to her."
    MC "So... then you're okay with her considering you a 'heartless bitch'."
    AE "Language."
    MCT "Hey, her words!"
    AE "And... yes. That's probably for the best. For now."
    MC "W-what? How c-"
    AE "Good day, Hotsure-san."
    jump daymenu

label AE102_c2:
    MC "Look Shiori, I don't know the whole story but did you ever ask why Akira never has her shirt buttoned?"
    show AE neutral
    AE "What possible explanation could she have for repeatedly breaking the school's mandate? All I know for now is that Mizutani-san is outright defying school legislation, and I refuse to let that happen."
    FMG "Well guess what! I can't wear it buttoned because I don't feel comfortable!"
    AE "It doesn't matter if it is comfortable or not, it's the rules and-"
    show AE angry
    AE "You know what? I've harped on this point enough. This is already enough of a time-vampire as is. Next time, I want to see you conform to the dress code; and Hotsure-san? I would have never expected this level of disregard from you."
    FMG "Leave him out of this, and I hope the door hits your fat ass on the way out!"
    MCT "Oh..."
    show AE surprised
    "Shiori-san gasped in shock. It was obvious that she didn't know how to handle what Mizutani-san just said. She looked at her, then to me, and then, swiftly exiting without a word muttered, began biting her thumbnail."
    hide AE
    show FMG sad at Position (xpos=0.5)
    FMG "*sigh* I swear, that girl better lighten up or she's never going to find a guy, assuming he could get past her extra junk in her trunk."
    MC "Well, it coulda gone better I guess, she could have at least hear you out."
    show FMG neutral
    FMG "Maybe... I also could have handled that better. I only wish she'd see it from my point of view."
    MC "what do you mean by that?"
    "Akira for her part, just exhaled before turning back to me."
    show FMG sad
    FMG "Sorry Kei, but I don't feel comfortable talking about it, maybe another day, maybe not, who knows... Who cares..."
    show FMG neutral
    FMG "Anyways, it's probably best if you say sorry to her..."
    MC "In your absence?"
    FMG "Not for me, for you. I get the feeling she's not going to forget the whole 'let the door hit your ass on the way out' comment I made."
    MC "Yeah, probably for the best."
    show FMG sad
    FMG "*sigh* We're only human after all... See you."
    MC "Goodbye Akira."
    jump daymenu

label AE061:
    "This marks the current end of Shiori's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance
