define BBW = Character('Alice', color="#CC33FF")
define Lunch = Character('Lunchlady', color="#CC33FF")
define Francois = Character('Francois', color="#CC33FF")
define BBWCell = Character('Alice', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Waitress = Character('Lunchlady', color="#CC33FF")

image BBW neutral = DynamicImage("Graphics/BBW/[globalsize]/neutral.png")
image BBW happy = DynamicImage("Graphics/BBW/[globalsize]/happy.png")
image BBW sad = DynamicImage("Graphics/BBW/[globalsize]/sad.png")
image BBW surprised = DynamicImage("Graphics/BBW/[globalsize]/surprised.png")
image BBW angry = DynamicImage("Graphics/BBW/[globalsize]/angry.png")
image BBW aroused = DynamicImage("Graphics/BBW/[globalsize]/aroused.png")
image BBW haughty = DynamicImage("Graphics/BBW/[globalsize]/unique.png")

image BBW swimneutral = DynamicImage("Graphics/BBW/[globalsize]/neutral.png")
image BBW swimhappy = DynamicImage("Graphics/BBW/[globalsize]/happy.png")
image BBW swimsad = DynamicImage("Graphics/BBW/[globalsize]/sad.png")
image BBW swimsurprised = DynamicImage("Graphics/BBW/[globalsize]/surprised.png")
image BBW swimangry = DynamicImage("Graphics/BBW/[globalsize]/angry.png")
image BBW swimaroused = DynamicImage("Graphics/BBW/[globalsize]/aroused.png")
image BBW swimhaughty = DynamicImage("Graphics/BBW/[globalsize]/unique.png")

image cg BBW001 = "Graphics/ui/gallery/BBW-001.png"

image Dorm BBW = "Graphics/ui/bg/BBWDorm.png"
image Dorm BBW Flip = im.Flip("Graphics/ui/bg/BBWDorm.png", horizontal=True)

init 2 python:
    #Core
    eventlibrary['BBW001'] = {"name": "Human Resources", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                          "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "BBW002", "obsflags": [],            "conditions": []}
    eventlibrary['BBW002'] = {"name": "Concerning a Missing Right Arm", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                           "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "BBW003", "obsflags": [],            "conditions": []}
    eventlibrary['BBW003'] = {"name": "Necessity is the Mother of Employment", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                             "location": "cookingclassroom", "priority": PrioEnum.NONE, "next": "BBW006", "obsflags": [],            "conditions": []}
    eventlibrary['BBW006'] = {"name": "A Proud Patron of the Arts", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                               "location": "hallway",          "priority": PrioEnum.NONE, "next": "BBW007", "obsflags": [],            "conditions": []}
    eventlibrary['BBW007'] = {"name": "Her Other Fluent Language", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                         "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "BBW008", "obsflags": [],            "conditions": []}
    eventlibrary['BBW008'] = {"name": "How to Train Your Diva", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                            "location": "musicclassroom",   "priority": PrioEnum.NONE, "next": "BBW012", "obsflags": [],            "conditions": []}
    eventlibrary['BBW008A'] = {"name": "The Fat Lady Won't Sing", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                 "location": "cafeteria",        "priority": PrioEnum.GIRL, "next": "BBW012", "obsflags": [],            "conditions": []}
    eventlibrary['BBW012'] = {"name": "Business Business Business Numbers", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                       "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "BBW015", "obsflags": ["BBWnowork"], "conditions": []}
    eventlibrary['BBW015'] = {"name": "This is the Stealth Section", "girls": ["BBW", "AE"], "type": EventTypeEnum.CORE,                                        "location": "dormexterior",     "priority": PrioEnum.NONE, "next": "BBW016", "obsflags": ["BBWnowork"], "conditions": []}
    eventlibrary['BBW016'] = {"name": "Game Time Interrupted", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                    "location": "dormexterior",     "priority": PrioEnum.NONE, "next": "BBW017", "obsflags": [],            "conditions": []}
    eventlibrary['BBW017'] = {"name": "What's She Got That I Haven't Got More Of?", "girls": ["BBW"], "type": EventTypeEnum.CORE,                               "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "BBW020", "obsflags": [],            "conditions": []}    
    eventlibrary['BBW020'] = {"name": "I Like Big...?", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                                    "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "BBW021", "obsflags": [],            "conditions": []}
    eventlibrary['BBW021'] = {"name": "The Lady in the Pool", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                     "location": "pool",             "priority": PrioEnum.NONE, "next": "BBW022", "obsflags": ["BBWnowork"], "conditions": []}
    eventlibrary['BBW022'] = {"name": "Helpful Muscle", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                                    "location": "dorminterior",     "priority": PrioEnum.NONE, "next": "BBW023", "obsflags": [],            "conditions": []}
    eventlibrary['BBW023'] = {"name": "It Can Be Found Anywhere", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                 "location": "classroom",        "priority": PrioEnum.NONE, "next": "BBW025", "obsflags": ["BBWnowork"], "conditions": []} #\/ disabled due to affection not being very grindable right now
    eventlibrary['BBW025'] = {"name": "Interoffice Romance", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                      "location": "hallway",          "priority": PrioEnum.NONE, "next": "BBW026", "obsflags": [],            "conditions": []} #"conditions": [[ConditionEnum.AFFECTION, "BBW", ConditionEqualityEnum.GREATERTHANEQUALS, 6]]}
    eventlibrary['BBW026'] = {"name": "The Trial of Smarts", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                      "location": "classroom",        "priority": PrioEnum.NONE, "next": "BBW027", "obsflags": [],            "conditions": []}
    eventlibrary['BBW028'] = {"name": "No 'Big Day' Puns, Please", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                "location": "classroom",        "priority": PrioEnum.NONE, "next": "BBW029", "obsflags": [], "conditions": [[ConditionEnum.FLAG, "BBW_dating"]]}
    eventlibrary['BBW029'] = {"name": "Who Are the Ad Wizards...", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "BBW030", "obsflags": [],            "conditions": []}
    eventlibrary['BBW030'] = {"name": "Alice end", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                                "location": "library",          "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}

    #Optional
    eventlibrary['BBW004'] = {"name": "As Long as the Job Gets Done, Right?", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONAL,                          "location": "classroom",        "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}
    eventlibrary['BBW005'] = {"name": "What to Expect When You're Growing", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONAL,                            "location": "cafeteria",        "priority": PrioEnum.GIRL, "next": "", "obsflags": ["aftertest"],       "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['BBW005A'] = {"name": "You Ate, You Drank, and You Were Merry, For Today You Diet", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONAL,   "location": "cafeteria",        "priority": PrioEnum.GIRL, "next": "", "obsflags": [],                  "conditions": [[ConditionEnum.FLAG, "BBW005_ondiet"]]}
    eventlibrary['BBW005B'] = {"name": "Pump You Up, Not Plump You Up", "girls": ["BBW", "PRG", "FMG"], "type": EventTypeEnum.OPTIONAL,                         "location": "gym",              "priority": PrioEnum.GIRL, "next": "", "obsflags": [],                  "conditions": [[ConditionEnum.FLAG, "BBW005_workout"]]}
    eventlibrary['BBW009'] = {"name": "Between a Soft and a Hard Place", "girls": ["BBW", "PRG", "FMG"], "type": EventTypeEnum.OPTIONAL,                        "location": "pool",             "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}
    eventlibrary['BBW010'] = {"name": "ABC: Always Be Clothing", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                              "location": "cafeteria",        "priority": PrioEnum.GIRL, "next": "", "obsflags": [],                   "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['BBW011'] = {"name": "True Romance", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONAL,                                                  "location": "hallway",          "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}
    eventlibrary['BBW013'] = {"name": "The Elephant In The Room", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                             "location": "hallway",          "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}
    eventlibrary['BBW014'] = {"name": "Silence Can Be Heavy", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                 "location": "gym",              "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}
    eventlibrary['BBW018'] = {"name": "All the Tycoons", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONAL,                                               "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": [[ConditionEnum.FLAG, "BBW016_testpass"]]}
    eventlibrary['BBW019'] = {"name": "Time Management", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                      "location": "hallway",          "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}
    eventlibrary['BBW024'] = {"name": "Mental Defragmentation", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                               "location": "hallway",          "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []} 
    eventlibrary['BBW025A'] = {"name": "Second Chance", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                           "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "BBW026", "obsflags": [],            "conditions": [[ConditionEnum.AFFECTION, "BBW", ConditionEqualityEnum.GREATERTHANEQUALS, 10]]}
    eventlibrary['BBW027'] = {"name": "Have it All?", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                         "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": [[ConditionEnum.FLAG, "BBW_working"]]}

label BBW001:
    $setProgress("BBW", "BBW002")
    scene Cafeteria with fade
    play music Busy
    MC "Well! That was... a first day. I didn't expect the school to be exactly like my old one, but on a list of unexpected surprises I didn't think..."
    MC "OK, I guess I couldn't have expected it for it to be a surprise."
    extend " But still, if the teacher had ripped off his face to reveal an alien underneath I wouldn't have been more surprised."
    MC "At least food is familiar enough. A nice snack after class is normal, right?"
    UNKNOWN "I'm sorry, you must not realize who you're talking to."
    MC "I wonder who that is."
    "Standing near the doors leading to the kitchen itself was the heavyset girl from my class. There was a man in a chef's outfit standing behind her, and she was arguing with an old woman in an apron and hairnet."
    show BBW angry at center with dissolve
    BBW "The name is Alice Nikumaru."
    BBW "I am sure there was some kind of memorandum circulated among the staff announcing my arrival at this school."
    extend " A missive to let you all know that I am here and that special accommodations to satisfy me would be instituted."
    Lunch "If you have an allergy or other dietary need, I would have been told."
    show BBW angry at Position(xpos=0.4) with dissolve
    BBW "You there. Tell... Madame Hairnet here who I am."
    MC "She's a student. She's in my class."
    show BBW haughty at center with dissolve
    BBW "I am THE student, as far as you are concerned. You may see hundreds of others passing down your line as you ladle warmed over spaghetti sauce onto rubber pasta, but I am not just another stomach to fill."
    MCT "You didn't hear the part about me being in your class, did you?"
    BBW "The meals you mass-produce for the student body may be satisfactory given the level of culinary talent you possess, but I have greater needs."
    BBW "Francois here studied at the finest institutes in France, Italy and Japan, all for the sake of honing his skills to a level suitable for me."
    Lunch "We make enough food for even the fat kids. Don't worry, you'll get your share."
    show BBW angry
    BBW "I am NOT some 'fat kid'. I am not even obese."
    show BBW neutral at Position(xpos=0.6) with dissolve
    BBW "And it is not a matter of quantity, but quality. My palate is a delicate instrument that needs to be handled with care. I have certain expectations that you – as qualified for this job as you may be – can not meet."
    show BBW neutral at Position(xpos=0.25) with dissolve
    BBW "Now, I've already gone to the trouble of ordering the equipment you probably don't have – wood-fire pizza oven, rotisserie, espresso machine, meat smoker; just a few odds and ends..."
    show BBW neutral at Position(xpos=0.4) with dissolve
    BBW "But he will need, say, 20%% of your workspace emptied out and handed over to him."
    Francois "And deliveries."
    show BBW happy at center
    BBW "Of course. And he needs to have deliveries made every day, so if you could give him the address and directions to this building, that would be wonderful."
    MCT "Oh, is that all? Your own private chef and special deliveries every day? Just how loaded is this girl?"
    Lunch "Students don't get to bring private chefs with them, princess. Non-faculty don't get access to our kitchen or any other facilities on campus. Either you can take what we offer you, or you can make your own meals in the Home Ec classes."
    show BBW angry
    BBW "What? Francois can not perform at his best in a classroom kitchen. He needs a full assemblage of utensils and appliances-"
    Lunch "I said you can make your meals."
    extend " Yourself."
    show BBW haughty
    BBW "Do you really expect me to subject my dainty hands and creamy skin to the raw ingredients that come with making a three-star meal?"
    BBW "Do you have any idea how much this manicure costs? What would handling an ox tongue or a raw Cornish game hen do to it?"
    Lunch "If you don't get out of my kitchen in the next five seconds, you'll be dunking that expensive manicure in cold, greasy dishwater as I have you scrubbing every pot and pan we have."
    show BBW angry
    stop music
    BBW "You... You wouldn't."
    Lunch "You wouldn't be the first student punished with kitchen duty."
    BBW "Very well, but this is not the end. A Nikumaru does not give up."
    show BBW neutral at Position(xpos=0.4) with dissolve
    play music BBW
    BBW "Did you see that?"
    MCT "Did you forget that you talked to me not two minutes ago?"
    menu:
        "Yeah. Typical hard-ass school employee, being cruel for the sake of it.":
            jump BBW001_c1_1
        "That was kind of harsh. She could at least have tried to work something out with you.":
            jump BBW001_c1_2
        "I've heard of spoiled little girls, but your own private chef? That's a whole new level.":
            MC "I've heard of spoiled little girls, but your own private chef? That's a whole new level."
            BBW "Is it 'spoiled' to have the best that money can buy? I am Alice Nikumaru."
            jump BBW001_c1_after

label BBW001_c1_1:
    MC "Yeah. Typical hard-ass school employee, being cruel for the sake of it."
    show BBW haughty
    BBW "Maybe this is how they do it at lesser institutions, but in my experience schools exist for the betterment of the students."
    extend " If this is a taste of how this place operates, perhaps transferring is the sensible thing. There must be other schools that can handle my needs."
    MC "I guess if you can have a private chef, you can also have a private tutor."
    jump daymenu

label BBW001_c1_2:
    MC "That was kind of harsh. She could at least have tried to work something out with you."
    BBW "Absolutely. Life is filled with give and take, and she wouldn't even come to the negotiating table. How is it that so many people can not understand the basics of business deals?"
    MC "Fancy yourself something of a business-woman, eh?"
    show BBW happy
    BBW "I know a lot about how the world works. It's an inherited trait."
    jump BBW001_c1_after

label BBW001_c1_after:
    show BBW neutral
    BBW "Perhaps you've heard of my father, Daitaro Nikumaru?"
    menu:
        "Daitaro... Isn't he some sort of businessman?":
            jump BBW001_c2_1
        "Oh, yeah! He's the guy who plays in that traveling jug band, isn't he?":
            jump BBW001_c2_2

label BBW001_c2_1:
    MC "Daitaro... Isn't he some sort of businessman?"
    show BBW happy
    BBW "Not just 'some sort' of businessman. He is the leader of the heavy manufacturing and seafood industries in Japan. He is ranked on the list of the richest people in the world."
    MC "Consider me impressed. But if he's so rich, couldn't he just buy this school and install Francois as head chef?"
    show BBW neutral with dissolve
    BBW "Such a simple thought. Just because you {i}can{/i} buy something, my dear boy, does not mean you should. Not all investments are worth the trouble."
    hide BBW
    MC "D-Did she actually take my joke seriously?"
    jump daymenu
    
label BBW001_c2_2:
    MC "Oh, yeah! He's the guy who plays in that traveling jug band, isn't he?"
    show BBW angry
    BBW "* scoff * Is there not a single ounce of class or breeding in this place?"
    hide BBW
    MC "I'd settle for an ounce of humor."
    jump daymenu
    
label BBW002:
    $setProgress("BBW", "BBW003")
    scene Cafeteria with fade
    play music Schoolday
    MCT "This place seems kind of quiet for a high school cafeteria. Everyone's so subdued, it's like someone died. Guess I'm not the only one who was thrown for a loop by yesterday's news."
    MCT "We're all probably wondering the same thing: what's going to happen to me? How... big am I going to get? Am I going to end up like one of those people who can't live in normal society?"
    MCT "Ugh, this is too heavy for first thing in the morning. Let's just get something to eat and take the day as it goes."
    MCT "..."
    MCT "Now to find a table. Oh! There's Alice, eating by herself. I don't think she'd mind if I joined her."
    "I found Alice sitting at a table, a few plates and bowls of food in front of her. She looked unimpressed by the spread."
    show BBW neutral at center with dissolve
    MC "Mind if I join you?"
    BBW "Be my guest. Perhaps you could help me with something."
    MC "Uh, sure! What's on your mind?"
    "Alice held up a fork with a piece of fish on it."
    BBW "This fish. There's something familiar about it."
    MC "It's mackerel. Fish is a common part of Japanese breakfasts."
    show BBW haughty
    BBW "I know that. I've lived here for most of my life. And 'common' may be the best word for what I am eating. I would never have known what this uninspired morsel was if you hadn't told me."
    "She ate the forkful of fish, her face displaying bland disgust."
    BBW "So tell me this: why, when there are literally hundreds of ways of turning even as pedestrian a choice as mackerel into an appetizing entree, did the staff in this kitchen decide to approach their job like they were vulcanizing a piece of rubber?"
    BBW "Is it because they are just that incompetent? What sort of 'cook' treats their ingredients so disdainfully?"
    MC "I don't know. Grilled mackerel's pretty good."
    BBW "I wouldn't mind having mackerel if it was properly prepared. Poach it, bake it in a honey chipotle glaze, something. But I guess that's too much to ask. Just slap it on a grill, turn it after a minute, job's done, right?"
    show BBW neutral
    BBW "Perhaps I should find out who is supplying seafood to this school and have Father undercut them. We could get some decent food in here without profits being too razor thin."
    MCT "Please don't talk about your father influencing the school with his wealth. I don't know if you're joking or if you actually will try it."
    jump BBW002_prechoice
    
label BBW002_prechoice:
    menu:
        "What do you normally have, if not mackerel?" if not getFlag("BBW002_c1_1"):
            jump BBW002_c1_1
        "What do you normally have, if not mackerel? (disabled)" if getFlag("BBW002_c1_1"):
            pass
        "Well, they have to make food for a few hundred people, you know? There's only so much you can do when you're preparing so much at once.":
            jump BBW002_c1_2
        "(Change the subject) So, how about that news about why we're here? How are you taking that?":
            jump BBW002_c2_1

label BBW002_c1_1:
    $setFlag("BBW002_c1_1")
    MC "What do you normally have, if not mackerel?"
    BBW "Tuna, usually. Though for breakfast I prefer something more like a French menu with coffee, berries in cream, and a croissant. Maybe a poached egg. I'm very particular about my breakfast; a heavy meal to start the day can leave me feeling lethargic for hours."
    "She picked up her mug and drank from it, showing the same mild disgust."
    show BBW angry
    BBW "And this is not coffee. I'll have to call Mother later, have her send my French press here."
    BBW "I suppose it was foolish of me to think this place would have proper coffee, but I was told this was an exclusive institution. So far the only thing 'exclusive' is the most uninspired menu I have ever encountered. Is this what you eat every day?"
    jump BBW002_prechoice

label BBW002_c1_2:
    MC "Well, they have to make food for a few hundred people, you know? There's only so much you can do when you're preparing so much at once."
    show BBW neutral
    BBW "All the more reason to let me have Francois on hand. It's unnecessary to force every student here to subsist on this food, and to have someone like me – someone accustomed to a certain standard – suffer this becomes downright cruel."
    MC "It's not that bad. I've had better, but I've definitely had worse."
    MCT "Besides, you managed to clear your plates."
    show BBW haughty
    BBW "You must not have had much better than this, but trust me when I say that offering this to my refined palate is like substituting Mascagni with... I don't know, some vulgar pop diva."
    MCT "I don't know who Mascagni is."
    menu:
        "(Change the subject) So, how about that news about why we're here? How are you taking that?":
            jump BBW002_c2_1
        "Other than the food, what do you think of this place?":
            jump BBW002_c2_2

label BBW002_c2_1:
    MC "So, how about that news about why we're here? How are you taking that?"
    show BBW neutral
    BBW "I have never encountered a problem I could not deal with. Whatever sort of... mutation I am about to experience, I will handle it with grace and composure. You will not see me sobbing or wailing my misfortune."
    MC "Hmm-mmm. You have any idea what it might be? Or if they even know?"
    BBW "I haven't the slightest."
    show BBW neutral at Position(xpos=0.5, ypos=0.0, yanchor=0.3), Transform(zoom=2.0)
    MC "Yeah, it's a puzzle. Anyway..."
    show BBW neutral at center, Transform(zoom=1.0)
    jump BBW002_c2_2

label BBW002_c2_2:
    MC "Other than the food, what do you think of this place?"
    show BBW neutral
    BBW "I haven't formed an opinion yet, but my expectations are dropping rapidly. First the unwelcome surprise of this school's true purpose, then the matter of the food. And, of course, being denied the privilege of my servants."
    show BBW angry
    BBW "The term has begun with me being hobbled, almost as if they want me to flounder."
    menu:
        "Do you really need someone to carry your books? Is that beneath you?":
            jump BBW002_c3_1
        "I'm sure you can get by without a butler or whatever.":
            jump BBW002_c3_2

label BBW002_c3_1:
    MC "Do you really need someone to carry your books? Is that beneath you?"
    show BBW haughty
    $setAffection("BBW", -1)
    BBW "Your jealousy is so transparent. Go ahead and mock my situation, as children always make light of what they don't understand. If you had even the basic conception of culture and breeding you would understand how this all degrades me."
    hide BBW
    MCT "I was just teasing..."
    jump daymenu

label BBW002_c3_2:
    $setFlag("BBW002_c3_2")
    MC "I'm sure you can get by without a butler or whatever. I get that you're used to having... help. I'm going to guess that you've gone to private academies, right? Elite places that take care of fewer students."
    show BBW haughty
    BBW "I have attended only the best schools in America and Japan. Yes, this place is... different from them. There are a lot more people, for one."
    MC "But you're not the only one adjusting. I mean, we've all been thrown into it without warning, and none of us know what the future holds."
    MC "Maybe you should reach out to some of the other students. Someone in our class might help you deal with this upheaval. Listen to your problems, help you navigate the school culture. You don't have to deal with this on your own."
    show BBW neutral
    BBW "You do have a point. The uncertainty we are all experiencing is a common ground I can exploit."
    MCT "Exploit?"
    BBW "Thank you, Hotsure-san. You've given me something to think about."
    hide BBW
    MC "Well that ended abruptly. Maybe if I'd been more direct..."
    MC "Wait, did she actually remember my name?"
    jump daymenu
    
label BBW003:
    $setTimeFlag("testday")
    $setProgress("BBW", "BBW006")
    scene Hallway with fade
    MC "I think the library is this way? Maybe? Wait, that bulletin board doesn't look familiar..."
    MC "Ah! I was supposed to turn left back there."
    UNKNOWN "Amazing!"
    MC "Oh? I know that voice."
    scene Cooking Classroom with fade
    play music Busy
    show BBW happy at Position (xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Simply superb. Where did you study?"
    show PRG neutral at Position (xpos=0.75, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    PRG "I didn't. I just sort of... taught myself."
    BBW "So modest. These are fantastic."
    show PRG happy
    PRG "Oh! K-Keisuke!"
    show BBW neutral
    BBW "Hmm? Hotsure-san, what brings you here?"
    MC "I was walking by and overheard you two. What's supposed to be so awesome?"
    show BBW happy
    show PRG neutral
    BBW "This souffle Kodama-san has prepared. I've seen enough of Japan's attempts to mimic French cuisine to know to lower my expectations, but this is surprising."
    menu:
        "Oh, is it really that good?":
            jump BBW003_c1_1
        "Can I try some?":
            jump BBW003_c1_2
        "Aida, I didn't know you were a cook.":
            MC "Aida, I didn't know you were a cook."
            jump BBW003_c1_3

label BBW003_c1_1:
    MC "Oh, is it really that good?"
    show BBW neutral
    BBW "It's all relative. I wouldn't tell her to open up a bakery, but for a high school student working with the ingredients and facilities on hand, this is almost revelatory. I can see my judgment was sound as ever to invite her into service."
    MC "Invite who?"
    BBW "Kodama-san, of course. It almost seems destined that my roommate would turn out to be perfectly suited to act as my right-hand woman during my time at this school."
    MC "I think I missed something."
    if getFlag("BBW002_c3_2"):
        BBW "What do you mean? It was your own idea that I should seek help among our classmates. And Kodama-san is all too eager to fill the role of my servants while I'm left to fend for myself here."
        MC "I wasn't really suggesting you find a maid..."
    else:
        BBW "I've decided not to let the loss of my servants hold me back. Just because I can not have trained professionals on hand to help me does not mean I need to flail around on my own. And Kodoma-san is all too eager to fill the role of my servants while I'm left to fend for myself here."
        MC "Seems like you're asking a bit much of your roommate."
    show BBW happy at center with dissolve
    BBW "Nonsense, Kodama-san is more than qualified to act as my chef, secretary, personal trainer, accountant, media relations manager, bodyguard, chauffeur and interpreter. And she's eager to start right away. Aren't you, Kodama-san?"
    PRG "Y-yes, ma'am."
    menu:
        "Is she? I guess that's fortunate for you.":
            jump BBW003_c2_1
        "So are you paying her, or... ?":
            jump BBW003_c2_2
        "Aida, do you really just want to be her maid?":
            jump BBW003_c2_3

label BBW003_c2_1:
    MC "Is she? I guess that's fortunate for you."
    show BBW haughty
    BBW "It is. I would have survived just fine had I been left to my own devices, but people like me – those of us who are always looking at the big picture and have so many things to worry about – we benefit from having dedicated subordinates. Having someone to cook for me frees up time and energy I can devote to other things."
    MC "Like what?"
    BBW "Anything. My studies, my hobbies, being the glamorous trendsetter that I am."
    MC "I guess if she's OK helping you, there's nothing wrong with that."
    BBW "Why wouldn't she be okay? I'm giving her focus and direction, at a time when she needs it most. All of us have been blindsided by the news of this school, and I think the best way to deal with it is to carry on as always. It's what I'm doing."
    MC "I can't say you're letting all this get to you. Maybe you have something there."
    show BBW neutral
    BBW "Of course, I could use more help. It's a full-time job being me, and I'm always looking for people I can count on to help me. Would you be interested in such a position?"
    MC "I'll... get back to you on that. I need to be somewhere else right now."
    BBW "Very well, but don't complain if I find someone else in the meanwhile."
    MCT "I think I'll get by."
    MCT "There's a big difference between making friends and becoming someone's butler."
    jump daymenu

label BBW003_c2_2:
    MC "So are you paying her, or... ?"
    show BBW haughty
    BBW "It's not polite to talk about money so plainly. But to answer your question, I have offered Kodama-san compensation for her services. And let us leave it at that."
    MC "Didn't mean to offend."
    show BBW neutral
    BBW "I'm sure you didn't, but do be careful in the future. Now, Kodama-san and I have more to discuss, so is there something you need or...?"
    MC "Don't mind me. I have somewhere else to be right now."
    jump daymenu

label BBW003_c2_3:
    show BBW neutral
    MC "Aida, do you really just want to be her maid?"
    PRG "O-Oh no, it's not like that. Alice- M-Madame Nikumaru is very nice, and I enjoy helping others. I'm just happy to have found a f-friend!"
    MC "Okay... I guess that's one way of looking at it."
    BBW "Kodama-san is happy with her position, as you can see."
    MC "Yeah. Sure. Happy. Well, I need to get going..."
    jump daymenu

label BBW003_c1_2:
    MC "Can I try some?"
    BBW "I suppose. There is more than enough here. Try some, and tell me my assessment was wrong."
    menu:
        "Hey, you're right. This is pretty good.":
            jump BBW003_c3_1
        "Aida, this is pretty good.":
            MC "Aida, these are pretty good."
            jump BBW003_c1_3

label BBW003_c3_1:
    MC "Hey, you're right. These are pretty good."
    show BBW haughty
    $setAffection("BBW", 1)
    BBW "Did you think I was being hyperbolic? I don't hand out praise unless it's earned, and even then I'm careful with my words."
    BBW "I have found in Kodama-san a rare talent, waiting to be nurtured and cultivated. And who better to guide her than someone with a palette as refined as mine? No one else at this school can help her like I can."
    MC "That's pretty generous of you."
    BBW "I know, but it's the least I can do. It's one of the burdens of the wealthy seldom talked about: the need to foster talent wherever it is found. With my help Kodama-san will become an excellent chef, someone capable of pleasing even my tastes."
    MCT "And now I'm wondering just how altruistic you are. Still, Aida seems happy with herself, so who am I to butt in?"
    jump daymenu

label BBW003_c1_3:
    $setAffection("PRG", 1)
    PRG "Ohnoit'snothingspecial. I-I-I just like to make treats and share them with people."
    MCT "Cripes. Is she not used to getting compliments?"
    BBW "Kodama-san had mentioned that she was thinking of making treats for our classmates, though I think directing her energy to one person, such as myself, is better than any scattershot approach."
    MCT "Better for who?"
    BBW "I'm afraid we can't stop and chat. Kodama-san has more training to do if I'm to bring her on as my assistant."
    MC "Your assistant?"
    BBW "Naturally I'll need to find someone to help me now that my personal retinue has been barred from the school. And Kodama-san practically begged me for the position."
    MCT "Why do I believe things played out a little differently outside your head?"
    MCT "I'm not up for an argument, though. I should get get going."
    MC "Well, I don't want to interrupt you two…"
    hide BBW with dissolve
    hide PRG with dissolve
    "As I left I heard Alice giving Aida notes about the texture of the souffle."
    jump daymenu
    
label BBW004:
    scene Classroom with fade
    play music Schoolday
    show BBW neutral at center with dissolve
    MCT "After class clean-up. That's normal. Mind-numbingly boring, but right now I'll take dull over surprising."
    MCT "..."
    MCT "?"
    MC "Um, are you planning to help out?"
    BBW "I have Aida taking care of my share of the work."
    MC "Aida? Where is she- Why are you down there?"
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, ypos=1.0, yanchor=0.3) behind BBW with dissolve
    PRG "Oh! H-hello Hotsure-san. I'm just doing what Nikumaru-san said."
    MC "Did she say to scrub the floor? I'm pretty sure we just need to sweep it."
    show PRG neutral:
        linear 0.75 yalign 1.0
    PRG "I- I know. I just wanted to do a good job."
    MC "But it's not your job. Alice's name was on the roster."
    show BBW haughty
    BBW "And I got Aida to do it for me. It's called delegating. As long as the work gets done, nothing else matters."
    menu:
        "I... guess I can't argue with that.":
            jump BBW004_c1
        "It's not just about getting the work done.":
            jump BBW004_c2
        "Do I have to tell on you? Because that seems like a really childish thing for all of us.":
            jump BBW004_c3

label BBW004_c1:
    MC "I... guess I can't argue with that."
    show BBW neutral
    BBW "Of course not. Aida isn't complaining, so there should be no issue here."
    MC "I'm not saying I agree. I just can't think of a counterargument."
    jump daymenu

label BBW004_c2:
    MC "It's not just about getting the work done. It's about being part of a team."
    show BBW neutral
    BBW "I am part of the team. I'm supplying leadership and direction to Aida. If she's not complaining, is it really any of your business?"
    MC "...You might not want to make a habit of this. That's all I'm saying."
    jump daymenu

label BBW004_c3:
    MC "Do I have to tell on you? Because that seems like a really childish thing for all of us."
    show BBW angry
    $setAffection("BBW", -1)
    BBW "You're threatening to report me? At what point did any of this become your concern, anyway?"
    MC "When I saw someone not doing their share. This is a collective assignment, we all have to carry our weight. You don't get to sit back and take it easy just because you managed to rope someone else in."
    BBW "Are you a figure of authority in this class? No? Then you do not get to tell me that I do not get to do something."
    show BBW haughty
    BBW "As for alerting someone with actual power, go ahead. Play the sniffling toddler, tattle on me. My conscience is clear."
    MC "Guess that's what I'll be doing..."
    jump daymenu

label BBW005:
    $setTimeFlag("aftertest")
    scene Cafeteria with fade
    play music Sunset
    MC "Hair? What kind of mutation is hair growth? This almost seems like a joke."
    MC "Hmm, no open tables. Oh! There's a spot."
    show BBW sad at center with dissolve
    show PRG sad at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    BBW "..."
    PRG "I-Is something wrong, Nikumaru-sama? Did I use too much coriander, or..."
    show BBW neutral
    BBW "No. The dish is exemplary. It's just..."
    MC "Stewing over the test results? Is it something bad?"
    hide PRG with dissolve
    BBW "A Nikumaru does not 'stew.' We take action, we confront problems. Destiny does not come to us, we make things happen."
    MC "So what was it? Or is it too personal to tell?"
    show BBW angry
    BBW "(You might have thought of that before you asked.) To answer your question, yes, I am thinking about the test results. I am questioning what can be done to curtail my... expansion."
    MC "If anything can be done."
    show BBW haughty
    BBW "There is always a way, even if it might be extreme. But the lengths you are willing to go to achieve something demonstrate how much you deserve it. Right, Kodama-san?"
    show PRG neutral at Position (xpos=0.8, xanchor=0.5, yalign=1.0)
    PRG "Ah! Y-yes, Nikumaru-sama!"
    MC "So what is your 'factor?'"
    hide PRG with dissolve
    show BBW neutral
    BBW "They say, and you might have trouble believing this just as I did, that I am inclined to grow... stout."
    MC "Stout?"
    BBW "..."
    extend " Obese."
    extend " Fat."
    MC "Oh. Yeah, that's, um, hard to swallow. But maybe it won't be too bad. They can't tell how 'stout' you'll end up being, right?"
    show BBW angry
    BBW "No, they can not predict that. But any excessive weight is unbecoming, which brings me to my quandary. Do I restrict my diet even further than the modest regiment I already have, or do I allow the growth to happen and fix things later?"
    MC "You think you can lose the weight after you're done growing? Isn't this supposed to be permanent?"
    show BBW neutral
    BBW "Failure only comes when you give up. Liposuction and similar weight loss treatments have helped others, so why not me?"
    BBW "But I am interested in your thoughts. Which sounds like a better approach, tackling the growth now or dealing with it at a later date?"
    menu:
        "I don't know anything about liposuction, so I'd say try to work at it now. Eat less, eat healthier.":
            jump BBW005_c1
        "Modern medicine is pretty extraordinary. If you ended up getting really fat there's probably some surgery you can get.":
            jump BBW005_c2
        "What if you worked out? Burn those calories before they turn into fat.":
            jump BBW005_c3


label BBW005_c1:
    $setFlag("BBW005_ondiet")
    $setAffection("BBW", -1)
    MC "I don't know anything about liposuction, so I'd say try to work at it now. Eat less, eat healthier."
    BBW "That does seem the best tactic. If I don't give my body the means to get fat..."
    MC "Just don't starve yourself or anything."
    BBW "Of course not. I know exactly what my body needs. Kodama-san!"
    show PRG neutral at Position (xpos=0.8, xanchor=0.5, yalign=1.0)
    PRG "Yes, Nikumarua-sama!"
    BBW "Going forward I want my meals to have a maximum of 650 calories. Adjust my menu accordingly, but be sure to include an appetizer, entree, side dish and dessert."
    hide PRG with dissolve
    MC "So now she's your dietician?"
    BBW "All part of her job description. Did you get all that?"
    show PRG neutral at Position (xpos=0.8)
    PRG "Yes, Nikumaru-sama."
    MCT "Seems a bit much to ask of anyone, even if they're as eager to please as Aida is. But what do I know about cooking?"
    jump daymenu

label BBW005_c2:
    MC "Modern medicine is pretty extraordinary. If you ended up getting really fat there's probably some surgery you can get."
    BBW "I agree, this is the idea most likely to succeed. I don't know enough right now, so how am I supposed to proceed? What if my growth is miniscule? Would I end up starving myself for nothing? Or what if it is extreme, and denying myself a proper diet is for naught?"
    show PRG neutral at Position (xpos=0.8)
    PRG "N-Nikumaru-sama? The quail is ready."
    show BBW happy
    BBW "Then bring it out! And excellent choice to include the spicy mustard greens in this salad. It was exactly what it needed."
    show PRG happy
    PRG "T-thank you!" 
    MCT "Whether this will work or not, it is the path of least resistance. Maybe that's why she's eager to go along with it."
    jump daymenu

label BBW005_c3:
    $setFlag("BBW005_workout")
    $setAffection("BBW", 1)
    MC "What if you worked out? Burn those calories before they turn into fat."
    BBW "Now that is sensible. I admit, the thought of denying myself proper meals is distressing, more so after discovering Kodama-san's talents."
    show BBW haughty
    BBW "I mean, who else at this school is prepared to give her ability the recognition it deserves? And if I can support her while taking care of myself at the same time, so much the better."
    MC "Have your cake and eat it too, you mean?"
    show BBW neutral
    BBW "Quite. You do have a good mind, Hotsure-san, but perhaps humor is outside your reach."
    MCT "I wasn't trying to make a joke."
    jump daymenu

label BBW005A:
    scene Cafeteria with fade
    play music Peaceful
    MCT "Why do I always have trouble finding an open seat? I wonder how much harder this will be once some of the people start growing..."
    MC "Mind if I sit here?"
    show BBW sad at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Oh! G-Good morning, Hotsure-san."
    BBW "... By all means."
    MC "Thanks. Say, did you two get the Lit reading done? I kind of spaced out last night."
    show PRG happy
    PRG "I did it. How far along did you get?"
    MC "About... two pages in."
    BBW "Kodama-san."
    PRG "Yes, Nikumaru-san?"
    BBW "Can you get the other half of the grapefruit? The first half was not adequate alone."
    PRG "Certainly, ma'am. And would you like some more toast?"
    BBW "... Two slices."
    PRG "With jam or butter?"
    BBW "No. Plain."
    PRG "All right. I'll be right back."
    hide PRG with dissolve
    show BBW sad at center with dissolve
    MCT "Someone's in a bad mood. I wonder if I should say something or not."
    stop music
    MC "Light breakfast today?"
    MCT "Mouth, you're not helping."
    BBW "Light breakfast today, and every day. Light lunch every day. Light dinner every day."
    MC "Oh? ... Oh! Yeah. Your factor. I guess you're doing the diet thing, huh?"
    play music Tension
    BBW "If I am to maintain authority over my own body and not be controlled by the whims of fate, then yes, I am doing 'the diet thing.' Every day, at every meal, I will be watching my intake, limiting the calories, sugars, and fats I take in. I will limit it all to what I need and no more."
    MC "You don't seem too happy about it."
    show BBW angry
    BBW "Is there something here I should be happy about? I have a palate more refined than people twice my age. My appreciation of the arts – culinary or otherwise – exceeds that of professional critics."
    BBW "And now I must cut out my tongue, surviving on simple fruits and steamed vegetables and whatever other staples a Neanderthal wandering the plains of famine would call a meal."
    MCT "That's a bit melodramatic. Better think of some positive way to look at this."
    MC "At least it will help in the long run! That'll be good, right?"
    show BBW neutral
    BBW "I am already beginning to question that. I can endure an existence marked by suffering and lacking. I am strong enough to bear up in the face of abject want, unlike many others."
    show BBW angry
    BBW "But is that a life worth living? Is the path of self-denial, of self-inflicted misery, beneficial to anyone? How can one grow as a person if they have committed their life to depriving themselves of opportunity and experience? Every bowl of plain rice, every plate of salad, is another act of self-flagellation. Shall my days be marked by anguish, my life's story a tale of torment? Who would live such a life by choice? Who would be inspired by that?"
    MC "But... you just started the diet. This is your first meal."
    BBW "Is my suffering any less brutal for being so brief? Shall I remain silent until I have carried my burden for a certain number of days? No! Pain is pain. It is not to be dismissed for failing to meet some arbitrary metric."
    BBW "You were the one to suggest this trial of deprivation, and now you mock me for not embracing my torture?"
    show BBW angry at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Miss Nikumaru? I brought you your food."
    show BBW neutral
    BBW "Thank you, Aida, but now I want you to go prepare me a real breakfast. Crepes Florentine and smoked salmon to start, along with some coffee and fresh-squeezed orange juice."
    show PRG happy
    PRG "Y-Yes, ma'am. ... I'll just leave the toast and grapefruit."
    hide PRG with dissolve
    show BBW angry at center with dissolve
    BBW "Or does this not meet your approval, Hotsure-san?"
    MC "Whoa! I'm not judging you. I'm just..."
    BBW "You're just... what?"
    MC "I'm just saying a diet might not be easy, but in the end you might be glad you did it."
    BBW "Is my mood a concern of yours? Is it your business to tell me how I deal with my factor? I assume you have your own condition to deal with, no?"
    MC "Yeah. My hair grows really fast."
    BBW "... That is your condition? That is why you're here?"
    MC "Yep. That's it."
    show BBW neutral
    BBW "I would suggest you withhold any attempts to guide others through their own crises until you have experience with actual problems yourself. Some people seem to just float through life without a care in the world, never understanding how hard and unyielding life can be."
    MC "Uh huh... Consider me properly scolded."
    MCT "I was just trying to help."
    jump daymenu
    
label BBW005B:
    scene Classroom with fade
    play music Busy
    "The last bell of the day rang and everyone got ready to get up and go. I had nothing in particular I wanted to do this afternoon, but like most everyone else I wanted to get out as quickly as I could."
    "I made it halfway to the door before I was stopped by a hand on my shoulder. Turning around, I saw Alice standing there with Aida hovering behind."
    show BBW happy at center with dissolve
    show PRG neutral at Position (xpos=0.4, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    BBW "It's time we begin our journey."
    MC "Journey?"
    BBW "Our journey towards health and well-being for myself. In order to stave off the effects of my growth factor I will be taking up an exercise routine. An intense calorie-burning regimen to keep myself fit and sleek."
    MC "Where do I come in?"
    show BBW neutral
    BBW "It was your idea, after all. And I can't tackle such a daunting task myself. I remember reading that new habits undertaken with others have a better success rate, and let's be frank, some exercise wouldn't do you much harm."
    MC "I'd be insulted, but... Yeah. What about Kodama-san, though? I thought you said she would be your personal fitness trainer."
    BBW "And she is, but she can't be both working out and coaching me. Plus, she wouldn't do as a spotter. Too frail."
    MC "I think she should be insulted, but..."
    show PRG sad at Position(xpos=0.75) with dissolve
    PRG "..."
    MC "Yeah. Well, I have nothing better to do right now, so why not? Let's hit the gym."
    show BBW happy
    BBW "That's the spirit. Go change, and we'll meet you at the weight room."
    
    scene Gym with fade
    show BBW neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "OK! Where do we start?"
    MC "Um..."
    BBW "I was asking Kodama-san. She's the official expert here."
    PRG "Uh... Maybe if we did some stretches?"
    show BBW happy
    BBW "Excellent. We'll ease into the workout."
    "We went to a set of mats set up in a corner, away from the weights and machines, and Kodama-san led us in some light stretches and calisthenics that took me back to grade school. I can't say it did anything to burn calories, but it did loosen me up."
    "Eventually she stopped (or she ran out of exercises)."
    PRG "Now how about we... do push-ups?"
    show BBW neutral
    BBW "You're the boss. Come on, Keisuke."
    hide BBW with dissolve
    "Alice and I got down on the mat and started doing push-ups. That is, we tried. I knocked out a couple before I was struggling to keep my form, but Alice was having trouble doing just one."
    show BBW angry:
        xpos 0.25 xanchor 0.5
        ypos 1.0 yanchor 0.0
        linear 1.0 ypos 0.8
    pause 1
    BBW "Nnnnnhg... Gggggrrrr... One!"
    show BBW angry:
        linear 1.0 ypos 1.0
    pause 1
    BBW "Aaaaannnn..."
    show BBW angry:
        linear 1.0 ypos 0.8
    pause 1
    BBW "Two!"
    show BBW angry:
        linear 1.0 ypos 1.0
    pause 1
    show PRG happy
    PRG "Come on, Nikumaru-san! Push it! Unleash the beast! Own your power!"
    "Kodama-san tried encouraging Alice with some slogans I'm sure she got off fitness clothing commercials, and ever so slowly she managed to do a full set."
    show BBW angry:
        linear 1.0 ypos 0.8
    pause 1
    BBW "Ggggggggnnnnnnnn... Ten!"
    PRG "You did it, ma'am! Well done!"
    show BBW happy at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Thank you, thank you. If you'll excuse me, I need to take a quick water break. Hydration is important, after all."
    hide BBW with dissolve
    show PRG neutral
    PRG "OK. We'll wait for you."
    "I wasn't going to say anything; after all, it's not like I'm effortlessly knocking out the push-ups one-handed or anything. And Alice was sweating by the end, so she was putting in some effort."
    "She came back five minutes later, no longer sweating and looking like she had straightened up her hair in the bathroom."
    show BBW neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    BBW "What shall we do next?"
    "Kodama-san looked around, a little bit lost among the machines she clearly had no experience with."
    PRG "Maybe we can start here? And then work our way around?"
    "She was looking at a pulldown bar, the kind where you stay standing and pull the bar in front of your chest."
    BBW "Very well. Keisuke, you go first."
    MC "Why me- No, never mind. I'll go."
    hide PRG with dissolve
    "As I was looking at the weights in increments of ten pounds, trying to guess what my limit was, another person came over and joined us."
    show FMG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    FMG "Hey sorry to bother but how much longer are you...Oh hey guys. What brings you here?"
    MC "Hi, Akira. We're just working out, trying to help Alice lose weight."
    show BBW angry
    BBW "I don't need to lose weight. I just need to keep myself from getting fat. There is a world of difference there."
    MC "Right. Anyway, we'll try not to take too long."
    FMG "Nah it's cool, I could use the breather anyways."
    show BBW neutral
    "She stayed standing a bit to the side, watching as I decided how to adjust the weight and making me self-conscious. If it was just me and Alice I could get away with something easy, but with Akira looking over my shoulder I was afraid she would say something if I wasn't going all out."
    "In the end I decided to add 50%% more what I was originally going to lift. To my surprise it weighed more than what I expected. Before I could lift it up, Akira came and grabbed the bar."
    FMG "Sorry but I have a quick question, just how much did you put on the bar?"
    MC "About 150 pounds. Why?"
    show FMG sad
    FMG "Because it looked like it was too much for you. You gotta know your limits and take it one step at a time."
    BBW "You look like you know what you're talking about. Maybe you have some tips you can share."
    show FMG neutral
    FMG "Sure. First off, did you take a protein shake before exercising?"
    BBW "Uh, no? Is that necessary?"
    FMG "Not really but it helps. Here, I have an extra."
    MC "I don't think we need it. We're not trying to build up muscle, are we?"
    FMG "Fair enough I guess."
    "Akira puts the shake away before whispering to me."
    show FMG happy
    FMG "{i}(Between you and me, I just wanted to see Alice's reaction to drinking this sludge.){/i}"
    FMG "All right, tips. The first thing you want to do is, like I said, know your limits and pace yourself. Take short breaks when you need it. Keep consistent and follow a routine. And the most importantly, be patient, don't expect results overnight. As long as you keep it up and actively enjoy it, you won't have any problems."
    show BBW happy
    BBW "Sounds good. Let's get to it."
    show BBW neutral
    BBW "..."
    MC "..."
    BBW "You were about to begin."
    MC "Right."
    "I reset the weight to what I thought was a manageable amount. Akira was still standing by, watching, but I put her out of my mind as I did ten reps with what felt like too little weight in her eyes."
    "When I was done I stepped aside for Alice."
    BBW "My turn."
    "She left the weight where it was, but turned out to be too much for her."
    show BBW angry
    BBW "Nnnnggg! Grrrrr!"
    "She reduced the weight and tried again, then reduced it a third time."
    BBW "Gggnnnn!"
    "She probably would have reduced it again if she wasn't already at the bare minimum. I looked over at Akira as Alice struggled to get to ten reps."
    show FMG sad
    FMG "...Um, you ok Alice? Need anything?"
    BBW "Ggnnnooo, thank you. Just doing what you said and taking it slow."
    FMG "...I didn't mean to the point where you're not even pulling the damn bar. For god's sake, you have it at the lowest level!"
    BBW "Did you not just tell us to know our limits? Are you now reversing yourself and telling me to risk injury by going beyond my limitations? What is it you want me to do?"
    show FMG angry
    FMG "No I... Gar!"
    FMG "Ugh, screw it. I'm getting ice cream before I really get mad!"
    hide FMG with dissolve
    "And she stormed off. For a second I thought about going after her, trying to cool things off so at least she wouldn't leave mad, but then I decided it'd be better this way."
    "Plus, turning back to Alice I another opportunity to play mediator."
    show BBW neutral
    BBW "Well that was uncalled for. It was certainly arrogant of her."
    MC "Arrogant?"
    BBW "Not everyone is gifted with physical prowess, and for her to carry on as if anyone should be able to do what she can... That's arrogant."
    MC "I'm not sure that was her problem, but I agree she could have been a bit more patient... How about I talk to her later, once she's cooled off? She probably could help you with this better than I or Aida could."
    show BBW happy
    BBW "That's thoughtful, but you don't need to put yourself out. This was a worthwhile experiment, but I've reached the conclusion that I'm not cut out to be a gym rat."
    BBW "I don't think this stress of trying to constantly outdo myself would be good for my temperament, if Mizutani-san is any indication. Still, thank you for your assistance."
    MC "You're welcome. (I guess.)"
    BBW "Now, Aida, let's go back to the dorms. I feel a hot bath and massage is the best way to unwind after a workout like this."
    show PRG happy at Position(xpos=0.75)
    PRG "Y-Yes, ma'am! I'll get the oils."
    jump daymenu

label BBW006:
    $setProgress("BBW", "BBW007")
    scene Hallway with fade
    play music Peaceful
    MCT "Classes are done, so what now? Don't want to go back to my room, I've got enough weirdness going on without someone trying to find more lurking around every corner. Maybe I can see if any of the clubs are recruiting yet."
    "..."
    MCT "Sounds like the music club is rehearsing. Not my thing... Oh!"
    show BBW neutral at center with dissolve
    MC "Niku- Alice. Thinking of joining the music club?"
    show BBW haughty
    BBW "Offering my services to the ensemble is one reason I'm here, though I'm disheartened to find out freshmen are not considered for seated positions. Waiting a year just to take my rightful place on the stage..."
    show BBW neutral
    BBW "I'm more sorry for the club, having to endure without my contribution."
    MC "How thoughtful. So what instrument do you play?"
    BBW "I have my own natural instrument: my voice."
    MC "You're a singer?"
    BBW "A soprano. And a gifted one, I should say. I've been coached since I was five."
    MC "I didn't know the music club did operas."
    show BBW neutral
    BBW "According to the club adviser, they do not. Put more accurately, they never have."
    show BBW haughty
    BBW "But the higher arts are not more difficult by nature. With sufficient commitment and practice I'm sure they could put on a fair performance. And with me as the star..."
    show BBW neutral
    BBW "But I'd also hoped to find a talent or two I could nurture during my time here."
    MC "Nurture?"
    BBW "The Nikumarus have a long history of patronage of the arts, one I hope to continue. I hope to get a start on it by finding a budding talent to encourage. Pushing them to refine their art and attain what greatness they were born for."
    BBW "Privilege, after all, comes with the responsibility of helping others."
    MCT "You sound both selfless and selfish as you say that."
    BBW "On that note, do you play any instruments, Hotsure-san?"
    MC "Me? Uh..."
    menu:
        "No, I don't.":
            jump BBW006_c1
        "I've practiced a little, but I'm not really talented.":        #FIXME maybe these should be skill checks?
            jump BBW006_c2
        "I don't mean to brag, but I'm a pretty skilled musician.":     #maybe these should be skill checks?
            jump BBW006_c3


label BBW006_c1:
    MC "No, I don't."
    BBW "Hmm. An honest answer, but a shame."
    MC "Does anybody here catch your eye? Or ear, I should say?"
    BBW "It's too soon to say. None of them are masters, so finding the seed of potential requires a deeper look. I'll need to sit in on a few more meetings."
    MC "I take it you'll be the joining the club, even as a benchwarmer?"
    BBW "...I am unfamiliar with that term. But yes. With my gift it would only be appropriate that I join. And I cannot convince the club president of their folly in keeping me in reserve if I am not here."
    MC "You don't take 'No' for an answer, do you?"
    show BBW haughty
    BBW "I'm a Nikumaru. A 'No' to me is just another obstacle to overcome."
    jump daymenu

label BBW006_c2:
    MC "I've practiced a little, but I'm not really talented."
    BBW "Oh? What instrument?"
    MCT "Immediate regret setting in. What's an impressive instrument?"
    MC "Uh... Violin. I've had a few lessons, but I'm no, you know, virtuoso."
    stop music
    BBW "None of the students here are, if the music club is any indicator. But talent can blossom anywhere when given a guiding hand. Show me what you can do."
    MC "Here? Now? Are you sure it's OK to use the club's instruments?"
    BBW "Of course. The instruments belong to the school, and we're students."
    MC "All right."
    "I squeaked out a few sharp chords that sounded like someone stroking a balloon. Alice's thoughts were too easy to read as she grimaced in pain."
    show BBW angry
    BBW "Enough!"
    MC "Sorry. It's been a while since I've practiced."
    show BBW neutral
    $setAffection("BBW", -1)
    BBW "Maybe I shouldn't have expected much. You... You might have some skill. Some day."
    hide BBW with dissolve
    "She wasn't disappointed, but as she turned away I could tell she was let down."
    jump daymenu

label BBW006_c3:
    MC "I don't mean to brag, but I'm a pretty skilled musician."
    MCT "Oh dear god, why did I say that? I can't even play the triangle."
    BBW "Really? Which instruments do you favor?"
    MCT "Instruments? Plural? Oh, jeez..."
    MC "I mostly play... violin. But I also toy with the oboe."
    MCT "Sure, let's keep lying."
    BBW "The violin? It wouldn't take much to outshine the other students here, but how experienced are you? Have you had many public performances?"
    MCT "Fix this, you dolt. Now!"
    MC "I've never performed in front of an audience. I don't have the nerves for it. Just a lot of practice in private."
    BBW "All that practice must have been worth something. Show me what you can do."
    stop music
    "And before I could say anything she was thrusting one of the club's violins into my hands. This was too fast for me to deal with, I couldn't think of anything to say to get out of it. So, nervously, I put the violin under my chin like I had seen people do in movies and I tried stroking the bow back and forth."
    "The disgust on Alice's face was immediate, and I couldn't blame her. If the violin was a living being I would have been arrested for animal cruelty. But I still thought I could fake it if I could, I don't know, figure out how to stroke the chords right."
    show BBW angry
    BBW "Stop! Stop!"
    MC "Sorry. It's been a while since I-"
    $setAffection("BBW", -3)
    BBW "Learned how to tune it properly? I don't know what kind of goofing off you think constitutes 'practice,' but you should keep this musical torture private."
    hide BBW with dissolve
    "And she stormed off. Which, considering her mood, may have been preferred."
    jump daymenu

label BBW007:
    $setProgress("BBW", "BBW008")
    scene Cafeteria with fade
    MCT "First time I haven't had trouble finding a spot. I guess other people are spending lunch up on the roof or in their classrooms, like at a normal school. Looking around, it does seem like a lot of people are drifting into cliques or avoiding certain people."
    MCT "And I'm off by myself, which is par for the course."
    "No sooner had I thought that than someone sat down across from me."
    show BBW neutral at center with dissolve
    MC "Oh, Alice. Didn't know you'd be having lunch here."
    BBW "Why wouldn't I? It is a pleasant day outside, but it seems improper to eat in some random place. Or maybe it is simply proper to eat where the food is served. Structure is an oft-overlooked virtue, in life and in business."
    MC "If you say so."
    "It took me a second to realize Alice wasn't alone. Right behind her was Aida, holding a few packages."
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    MC "Hi, Aida. How did you get so much mail already? It's still the first week of the year."
    PRG "Oh, it's not mine. I was carrying it for Nikumaru-sama. We just came from the mail room."
    show PRG sad
    extend " ... There was nothing for me."
    MCT "She seems a bit sad. Is there something about mail that bothers her? Better change the conversation."
    BBW "Interested in what I got?"
    MC "Uh..."
    hide PRG with dissolve
    BBW "A lot of it is the usual care package stuff. Hand lotion, chewable candies, perfume, a new phone -"
    MCT "That left 'usual' territory pretty quickly."
    BBW "But I also ordered myself some things. White knee-high stockings seem to be 'in' among the other students, and I was not aware how cold winters in this part of the country can get, so I needed a new coat."
    BBW "And Aida confided in me that she only has one pair of shoes and barely any clothing besides her school uniforms. So I ordered some stuff for her."
    MC "That was considerate."
    BBW "Well, she doesn't have a credit card or bank account of her own, so ordering things online are beyond her means. But it was the least I could do to facilitate her shopping."
    MC "Facilitate... You mean she still paid for the stuff herself?"
    BBW "But of course. I'm not running a charity. And I would like to point out that with my connections I was able to buy directly from the manufacturer, saving her money."
    MC "What do you mean by connections?"
    show BBW haughty
    BBW "I know the sons and daughters of many business owners and CEOs. We always turn up at the same hotels in Monaco or ski lodges in Switzerland. You don't think the owner of a factory that makes dresses or suits has to buy off the rack, do you?"
    MC "I guess not. So if I needed to buy a new laptop could you get me one at a discount?"
    show BBW neutral
    BBW "I suppose I could. Hitomi and I – that's Hitomi Ogawa, daughter of the president of Ogawa Electronics – aren't on the closest of terms, but she could get me one for... 90,000 yen. Plus 10%% commission for myself would be 99,000."
    MC "An Ogawa laptop for under a hundred thousand yen? That's pretty steep for some old model being unloaded-"
    BBW "That's for an Ogawa D2300. 22” monitor, if I remember correctly."
    MC "... For 99,000?! Are you serious?"
    BBW "Completely."
    MCT "Unbelievable. That's a 170,000-yen machine, and she says she can get one for under 100K?"
    BBW "Don't be surprised. I'd be buying direct from the company, so there's no middle-man mark-up. Except for my commission, of course."
    MC "O-Of course."
    BBW "Or would you prefer the Essence 4K? I could probably get that for, let me see..."
    "And she checked her smartphone. Was she checking the manufacturing cost online, or did she know what the mark-up from retailers was?"
    BBW "How does 115,000 yen sound?"
    MC "I think I might faint."
    BBW "Shall I order one? You don't have to pay me now, you can take care of that when it gets here."
    MC "No, no. I don't need a new laptop. I mean, I could use one, but I don't have that kind of money."
    BBW "Well you should have said so."
    extend " ... Idea. Aida, take a note: I am going to start a business here at school. Direct retail, goods offered at a discount."
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    MC "There's already a store on campus, you know."
    BBW "I know, I've seen it. But it lacks many of the essentials of modern living, and the mark-up is scandalous. 300 yen for a soda? I can beat those prices and still make a worthwhile profit."
    PRG "What do you need me to do, Nikumaru-sama?"
    BBW "Our first step will be to get the word out. We'll need some sort of ad campaign, make the people aware of my service. Then we'll need a system of taking orders and fulfilling them. Dorm-room delivery would be an enticing service; convenient for the customer."
    BBW "But the guys' dorm... Keisuke! How would you like a job?"
    if getSkill("Academics") < 3:
        MC "Me? Doing what?"
        BBW "Haven't you been listening? I'll need runners, people to deliver packages as they come in. I can offer you 1,000 yen an hour."
    else:
        MC "Let me guess: you need a deliveryman."
        show BBW happy
        BBW "Got it in one. I'm offering 1,000 yen an hour."
        show BBW neutral
    MC "I... will think about it."
    MCT "She's actually serious about this. I wouldn't have guessed she was this sort of vigorous go-getter. I guess business runs in her blood."
    "The conversation died as Alice started giving instructions to Aida."
    "The idea had just come to her, but she was immediately rattling off ideas about what products to offer, how to acquire, pricing and advertising."
    "I'd thought she was more a spoiled rich girl than anything, but it seemed she wasn't content to spend her daddy's money. She had a mind for business herself."
    "Made me feel a little lazy. I was just trying to keep up with my coursework. Never mind building a business from scratch."
    jump daymenu
    
label BBW008:
    scene Hallway with fade
    "After another day of classes I found myself not in my dorm and not in my classroom. I wasn't heading anywhere special, I was just wandering around."
    "I eventually found myself passing by the music room."
    scene Music Classroom with fade
    MCT "Maybe I can listen in on them practicing."
    "But the club wasn't meeting right now. There were just two people, Aida and another student. It's not like I wanted to spy on them, but I was curious and they were talking loud enough to overhear them."
    play music Bittersweet
    Student "-alented or not, I have no patience for someone trying to undermine my authority."
    show PRG sad at Position(xpos=0.8, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    PRG "Y-yes, ma'am. But I don't think she means to be-"
    Student "You seem to be the closest thing she has to a friend, so maybe she'll listen to you. Tell her she can either be happy in the chorus or she can look for another club to join."
    PRG "Y-yes, ma'am."
    "The other girl (is she the music club president?) turned away, the conversation over. Head bowed, Aida made for the door. I stepped back, but not fast enough to not get caught."
    show PRG surprised at center, Transform(xzoom=1)
    PRG "Oh! H-Hotsure-san."
    MC "Hey, Aida."
    MCT "Should I ask what that was about? Aida looks pretty bummed."
    MC "Is something wrong? It looked like you were being given the third degree."
    show PRG neutral
    PRG "N-no. I wasn't in trouble. It's Nikumaru-san. She doesn't like being in the chorus, but Mizawa-san won't make her lead vocalist."
    MC "Is that the club president? Is Alice butting heads with her or something?"
    PRG "Yes. They keep getting into arguments, and now Mizawa-san is threatening to kick Nikumaru-san out if she doesn't behave."
    MC "I haven't known her too long, but Alice doesn't seem like much of a team player. Guess I'm not surprised she's already getting into trouble like this."
    show PRG sad
    PRG "I-I'm supposed to t-tell her to mind herself, b-but I don't think Nikumaru will listen to me. She's kind of head strong."
    MCT "And you're kind of a pushover."
    MCT "Oh, that's mean. But it's not wrong."
    menu:
        "Well, good luck with that.":
            $setTimeFlag("size2")
            $setProgress("BBW", "BBW012")
            stop music fadeout 0
            "Well, good luck with that."
            show PRG surprised
            $setAffection("PRG", -1)
            PRG "..."
            MCT "I could go for a soda now."
            jump daymenu
        "Maybe I could help.":
            jump BBW008_prechoice

label BBW008_prechoice:
    MC "Maybe I could help."
    MC "I wouldn't say Alice listens to me so much as she hears what I say. I can pass the word along for you."
    show PRG happy
    PRG "C-could you?"
    show PRG sad
    $setAffection("PRG", 1)
    PRG "I-I don't want to trouble you, but it would be so sad if she got kicked out of the club. She's a stranger here, you know. She doesn't fit in."
    MC "We're all strangers, but I get what you mean. She kind of fits that whole 'pushy American' stereotype, doesn't she?"
    show PRG angry
    PRG "Oh, no! Nikumaru-san is just very determined."
    MCT "Determined. Sure."
    MC "Do you know where Alice is now?"
    show PRG neutral
    if isEventCleared("BBW007"):
        PRG "She should be in the cafeteria. I made some snacks for her to sample while she works on setting up her business."
    else:
        PRG "She should be in the cafeteria. I made some snacks for her to sample."
        MC "Might as well deliver the news now, then."
    stop music

    scene Cafeteria with fade
    play music Sunset
    "We found Alice sitting at her usual table, one hand typing on a laptop and the other picking up high tea pastries from a tray next to her."
    show BBW happy at center with dissolve
    BBW "Hotsure-san, good afternoon. Thank you for bringing Aida back. I've been waiting for her for... five and a half minutes now."
    MC "Actually she brought me here. There's something I need... Something you should know."
    show BBW neutral
    BBW "Oh?"
    MC "Yeah, um... How's the music club? You're still doing that, right?"
    BBW "Despite my feelings on how it is being managed, yes, I am still a member."
    MC "Right, right. So I was told- That is, Aida was told..."
    show BBW angry
    BBW "..."
    "I stammered a few words, and Alice became irritated quickly."
    MC "We were told to tell you to, you know... Maybe ease up on the prima donna thing."
    BBW "Excuse me?"
    MC "It's not that you're... You can be a little... "
    MC "You're going to get kicked out if you don't stop fighting with the president."
    BBW "Oh, really? Aida, is this true?"
    show PRG sad at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Y-yes, Nikumaru-san."
    BBW "I should find her at once and tell her..."
    hide PRG with dissolve
    MCT "She didn't understand anything I just said, did she?"
    menu:
        "Say nothing. Let Alice do what she wants.":
            jump BBW008_c1
        "Suggest Alice not make things worse.":
            jump BBW008_c2
        "Tell Alice she's in the wrong.":
            jump BBW008_c3

label BBW008_c1:
    $setProgress("BBW", "BBW008A")
    MCT "Well, if she wants to pick a fight, let her. Whatever happens is on her head."
    show BBW haughty
    BBW "Thank you for bringing this to my attention, Hotsure-san. My esteem for Mizawa-san was already low, but to use an intermediary like this is pathetic."
    MC "No problem."
    "I decided to excuse myself then. Didn't want to get caught up in this drama."
    jump daymenu

label BBW008_c2:
    $setProgress("BBW", "BBW012")
    MCT "Oh man, this is going to get out of hand quickly if I don't do something."
    MC "Maybe you shouldn't push back right away."
    show BBW angry
    BBW "What do you mean? Should I let this stand-?"
    MC "Some people just don't get the message right away, do they? Clearly the club president - this Mizawa girl - hasn't recognized your talent yet."
    show BBW haughty
    BBW "No, she hasn't-"
    MC "So getting in her face again won't do any good. This seems like one of those times where the person needs to realize their failure on their own."
    BBW "And what do I do in the meanwhile? Resign myself to the chorus until Mizawa-san decides to admit she was wrong?"
    MC "I don't think there's much you can do at the moment."
    BBW "Are you not familiar with the phrase 'The squeaky wheel gets the grease'? If I'm supposed to wait for that tone-deaf girl to realize my talent, I will be stuck in the chorus all year."
    MC "And have you ever heard the phrase 'The upturned nail gets hammered down'? If you keep fighting her you won't even be on the chorus."
    show BBW angry
    BBW "..."
    BBW "Hmm..."
    show BBW neutral
    $setAffection("BBW", 1)
    BBW "Is it just me, or are Japanese people excessively non-confrontational?"
    BBW "Very well. Aida, forget my last order. I'll toe the line, for now."
    BBW "But not forever, Hotsure-san. I don't intend to let my genius go ignored indefinitely."
    MC "Wait, why are you making it sound like it's my job to get you out of the chorus?"
    jump daymenu

label BBW008_c3:
    $setTimeFlag("size2")
    $setProgress("BBW", "BBW012")
    MC "Can't you just admit that you're in the wrong here?"
    show BBW angry
    BBW "I beg your pardon?"
    MC "You're not the leader of the music club, are you?"
    BBW "I'm the best singer-"
    MC "That's a 'No,' then. Well, the actual leader has made a decision, and it doesn't matter if you like it or not."
    MC "Maybe you are the best singer, but there's more to an ensemble than any one person getting what they want."
    MC "You're going to have a hard time getting along here if you don't understand that. We're all dealing with some pretty major stuff right now, not just you."
    $setAffection("BBW", -1)
    BBW "How dare you..."
    "She didn't have to say anything, I knew what she was thinking. All the better, as I wasn't looking for a fight or anything."
    MC "Just something to think about."
    "And I turned and walked away. Maybe a bit quicker than I intended, but I didn't want to stay and get chewed out or anything."
    jump daymenu

label BBW008A:
    $setTimeFlag("size2")
    $setProgress("BBW", "BBW012")
    scene Cafeteria with fade
    show BBW angry at center with hpunch
    play sound Crash
    BBW "That impudent egotist!"
    play music Tension
    "I was sitting in the cafeteria, not so much enjoying my lunch as eating it without gagging-"
    show BBW angry at Position(xpos=0.8)
    play sound Crash
    BBW "How could such a woman be put in a position of authority? Bribery? Blackmail? Nepotism?"
    "-when Alice came up to my table and started complaining to me about someone."
    "There was no way to know how long she had already been ranting before reaching me..."
    show BBW angry at Position(xpos=0.2)
    play sound Crash
    BBW "A leader who thinks their job is to simply dictate to others does not understand leadership. A captain who does not know her destination might as well run the boat aground."
    MC "Problem with authority? Is this about the music club thing?"
    show BBW angry at center with dissolve
    BBW "What does it say about a club leader who is more concerned with maintaining a cordial environment where mediocrity can rule than challenging everyone to deliver their best?"
    MC "That... this is more about having some fun than anything else?"
    show BBW neutral
    BBW "And how is it 'fun' to rehearse the same pieces of music without striving for improvement?"
    show BBW angry
    BBW "This Mizawa-san is only wasting everyone's time if she refuses to demand anything of her members."
    MC "It's only the start of the year. I'm sure there must be some period of adjustment for a musical group to come together."
    MC "Maybe if you tell her - politely - that you think she can ask a little more of everyone she'll agree. Maybe she already wants more of them, but she doesn't want to be overbearing."
    show BBW haughty
    BBW "I have already addressed my concerns with Mizawa-san. Just now, when she suspended me from the club."
    MC "What?! She kicked you out?"
    show BBW neutral
    BBW "Not permanently, but I am on forced sabbatical until I have 'adjusted to the upheaval in my life,' as she put it."
    show BBW haughty at Position(xpos=0.2) with dissolve
    BBW "She thinks I am, what were her words, 'behaving out of turn' because I am in an unfamiliar environment, with the news of my condition hanging over me."
    show BBW angry at Position(xpos=0.8) with dissolve
    BBW "Projection. That's what it is. Mizawa-san is uncomfortable being here, and so she is pretending I am the one with the problem."
    show BBW neutral
    BBW "Perhaps that is easier to believe than acknowledging I am in the right."
    MC "So... This isn't about the other students in the club? This is just about you still butting heads with her?"
    show BBW haughty at center with dissolve
    BBW "This is only about the club, and how I know what is best for it."
    show BBW angry
    BBW "Mizawa-san may try to pull rank, but shoving me aside does not win her the argument. I am still of half a mind to press the issue."
    menu:
        "I don't see what good that would do. If she's as headstrong as you say, arguing will only make her dig her heels in.":
            jump BBW008A_c1
        "If you feel this strongly, go for it. You're the one talking about squeaky wheels, right?":
            jump BBW008A_c2
        "Arguing with Mizawa-san obviously isn't doing any good. Maybe try a different tack.":
            jump BBW008A_c3

label BBW008A_c1:
    play music Sunset
    MC "I don't see what good that would do. If she's as headstrong as you say, arguing will only make her dig her heels in."
    show BBW angry
    BBW "Mmmf!"
    BBW "..."
    show BBW neutral
    BBW "She probably would, wouldn't she?"
    BBW "I suppose this is a situation that calls for patience rather than the firm hand of guidance."
    BBW "Very well. I shall endure my sabbatical with my natural grace, and when I return to the music club even Mizawa-san will not be able to deny what a difference my presence makes."
    hide BBW with dissolve
    "And she trotted off. I don't think she was any less angry, but at least things hadn't gotten worse."
    jump daymenu

label BBW008A_c2:
    MC "If you feel this strongly, go for it. You're the one talking about squeaky wheels, right?"
    show BBW neutral
    BBW "You are not wrong. There may still be time to find Mizawa-san before lunch ends, and we can settle this matter before the club meeting this afternoon."
    hide BBW with dissolve
    "And she walked off."
    scene black with fade
    stop music
    "Ten minutes later, she came back."
    scene Cafeteria with fade
    show BBW angry
    play sound Crash
    $setAffection("BBW", -2)
    BBW "There is no word for 'foolishness' in your language that is strong enough for that girl."
    play music Sunset
    MC "She didn't listen to you-"
    BBW "She says that I am a hair's breadth from being cut entirely, and she makes it sound as if she is being reasonable by giving me a 'second chance.'"
    BBW "That my talent, which I have clearly demonstrated by this point, could be dismissed so flippantly..."
    BBW "Argh!"
    BBW "I almost want to leave of my own accord. Being hobbled by this enabler of mediocrity may not be worth it."
    MC "I-"
    hide BBW with dissolve
    "But she was already storming away, as if she wanted to get away from the entire school."
    jump daymenu

label BBW008A_c3:
    $setFlag("BBW008A_fail")
    stop music
    MC "Arguing with Mizawa-san obviously isn't doing any good. Maybe try a different tack."
    MC "Instead of taking up this fight yourself, why don't you get some others on your side?"
    MC "Talk to the other members of the music club, see if they'll back you up. Then you can all go up to the club prez and try to reason with her."
    show BBW happy
    BBW "That is not a bad idea, Hotsure-san. Strength in numbers."
    show BBW haughty
    BBW "Or if I can convince enough members to see it my way, I could simply try to oust Mizawa-san as president."
    MCT "OK, that is not what I'm suggesting."
    show BBW neutral
    BBW "There's still time before lunch ends. I need to speak with some of the other members."
    hide BBW
    "And she walked off, holding her chin up as if she had already won a victory."
    scene Hallway with fade
    "As I left the cafeteria and started to make my way back to class, I ran into Alice coming in the opposite direction."
    show BBW angry
    play sound Crash
    $setAffection("BBW", -10)
    BBW "Hotsure-san! How could you possibly suggest such a terrible idea?"
    MC "Me? What did-"
    MCT "Oh, this must be about the music club thing."
    play music Bittersweet
    BBW "I've been kicked out of the music club! Mizawa-san claims I was attempting to mutiny-"
    MCT "Well, you did suggest-"
    BBW "And now I have been expelled entirely."
    "By her expression I had no doubt who she blamed for this, and while there were a number of ways I could have responded, I ultimately decided on staying silent and not making things worse."
    "Alice continued glowering at me, perhaps waiting for me to answer, but after a while she huffed and muttered"
    BBW "What is wrong with this place?"
    "And then she walked away."
    "Which was awkward, because we were headed in the same direction, so I had to hang back a couple feet and try to look anywhere besides directly at her."
    scene Classroom with fade
    "And when we got to class and took our seats she adamantly refused to look in my direction."
    show BBW angry
    BBW "Harumph!"
    hide BBW with dissolve
    "At least I knew where I stood at the moment."
    jump daymenu
    
label BBW009:
    scene Hallway with fade
    play music Busy
    "It was only the second week of the year and I was already getting cabin fever being stuck at the school 24/7."
    "There was a town not far from the gates, but I hadn't gotten a chance to check it out yet. Hadn't even checked out much of the school, for that matter."
    "That's probably why I found myself at the locker rooms after class. Going back to my dorm room didn't appeal to me; just two weeks in and I was getting tired of that place."
    "And I still didn't belong to a club, so I had no specific place to be..."
    "I was thinking of maybe changing into my gym clothes and doing a little cardio when I was surprised to see Nikumaru-san, of all people, coming out of the women's locker room."
    show BBW happy at center with dissolve
    MC "Oh, Ni- Alice! How's it going?"
    show PRG sad at Position(xpos=0.8, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    PRG "..."
    MC "A-and you, Kodama-san! What were you two up to?"
    BBW "I was doing a light workout."
    MC "I thought you weren't going to try to lose weight just yet."
    hide PRG with dissolve
    show BBW neutral
    BBW "I'm not, but exercise has other benefits besides weight loss."
    show BBW haughty
    BBW "A strong mind in a strong body, as they say."
    BBW "So I was making use of the school's swimming pool. 20 laps, back and forth. A fair workout to get my heartrate up."
    MC "20 laps!? That's... That's actually impressive."
    BBW "I understand how it can seem like that to most people, but I have a natural affinity for the water. I've been an accomplished swimmer since I was a young girl."
    if isEventCleared("BBW008"):
        MC "Maybe you should have joined the swim team instead of the music club."
        BBW "I did consider it, actually, but the school would allow me to join only one club at a time. I find the limitation frustrating but bearable."
        show BBW angry
        BBW "And who knows. If the matter between me and the music club president is not resolved satisfactorily I may take my talents to more appreciative grounds."
    MC "How fast can you swim? Have you ever timed yourself?"
    show BBW neutral
    BBW "Quite fast, actually. I should have had Kodama-san timing me, upon reflection. An accurate chart of my ability would help measure my fitness levels."
    show PRG neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    PRG "I'm sorry, Alice. I'll remember next time, I promise!"
    hide PRG with dissolve
    show BBW haughty
    BBW "I don't have a specific number, but I feel confident that I am the best swimmer in our class. Probably in the top percentile of the school."
    MC "Even better than Mizutani-san? She's pretty athletic, you know."
    BBW "There's more to it than just physical strength. Stamina, hydrodynamics, breathing control."
    stop music
    MC "!"
    "Alice didn't see her, but standing behind her was-"
    BBW "Sheer muscle may be good for lugging heavy weights around, but swimming is a much more graceful art than being a simple packmule."
    show FMG angry behind BBW at Position(xpos=0.7, xanchor=0.5, yalign=1.0) with dissolve
    play music Tension
    "-was Akira. And judging by her expression she didn't like what she was hearing."
    BBW "It's the difference between composing poetry and punching a sack of meat. Elegance versus brute force."
    "I was just about to interrupt Alice - even though she already seemed to be wrapping up - when Akira beat me to it."
    FMG "Hello Alice What's-your-last-name! Interesting theory you have there!"
    show BBW haughty at Position(xpos=0.6) with dissolve
    show FMG angry at Position(xpos=0.25), Transform(xzoom=-1) with dissolve
    "Alice blanched at the sound of Akira's voice, but she recovered swiftly."
    show BBW happy
    BBW "It's not so much a theory as good common sense."
    BBW "One isn't pushing against the water but rather propelling oneself through it. It's a complete different act, an interplay of body and water rather than a conflict between muscle and weight."
    FMG "Oh yeah! Well how about we test your little 'act of pushing water by being something something BS' by seeing who's the fastest swimmer! Or are you too full of yourself to do it!?"
    "Alice let out a single 'Ha' while brushing one of her curls over her shoulder."
    show BBW haughty
    BBW "Ha!"
    BBW "I would never make a claim I could not back up. If you wish to see the truth of my words in action, then certainly. Let us race."
    FMG "God, are all Americans as snobby as you? Let's do this!"
    "Alice turned to me, her self-satisfied look still there."
    show BBW happy
    BBW "Any objections to Hotsure-san acting as judge? I'm sure he'll be impartial."
    show PRG neutral at Position(xpos=0.45, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    PRG "I... I could, maybe..."
    show FMG neutral
    FMG "Yeah, sure. But Keisuke, don't you think this is a forgone conclusion?"
    MC "Well..."
    hide PRG with dissolve
    menu:
        "You do seem the obvious choice, Mizutani-san.":
            $setAffection("FMG", 1)
            FMG "Heh, well whatever happens, happens I guess!"
            show BBW neutral
            BBW "Indeed..."
        "Alice seems pretty confident. I think this might be an upset.":
            $setAffection("BBW", 2)
            show BBW haughty
            BBW "Not an upset. As Mizutani-san said, it's a foregone conclusion."
            show FMG angry
            FMG "Whatever, 'princess'!"
        "I really don't know.":
            show BBW neutral
            BBW "Well, you shall know soon enough."
    scene Pool with fade
    "I went out to the pool as the two ladies got changed. Aida came out and stood next to me, and then the swimmers showed up."
    show FMG angry at Position(xpos=0.25, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    show BBW happy at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Three full laps should be adequate, I think. Any objections?"
    FMG "Just don't forget your pool cap thingy! Don't want to get your expensive mullet to get ruined by chlorine!"
    "They took their positions, I counted down from three, and they were off."
    stop music
    hide FMG with dissolve
    hide BBW with dissolve
    "It was neck and neck for most of the first lap, but when the two reached the far end and pushed off the wall to return Alice began to pull ahead."
    "By the time she completed her first lap Alice was a full length ahead of Akira, and that lead grew for the rest of the race."
    "When she completed her third lap Alice almost leapt out of the pool, springing to her feet and looking down to watch Akira reach the end."
    show FMG sad at Position(xpos=0.25, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    show BBW happy at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    play music Busy
    FMG "...Son of a bitch... Good job I guess... I'm going to bed. Later."
    hide FMG with dissolve
    show BBW happy at center with dissolve
    BBW "At least she's magnanimous in defeat."
    MC "Nice job. That was quite the blowout."
    show BBW haughty
    BBW "Was there ever a doubt? But as much as I enjoyed this contest, I have to get going."
    show BBW neutral
    BBW "Aida, what's next on my agenda?"
    hide BBW with dissolve
    "She was already walking away as Aida answered. Something about 'contacting her distributor.'"
    jump daymenu
    
label BBW010:
    $setSize(2)
    $setTimeFlag("aftersize2")
    scene Cafeteria with fade
    play music BBW
    "It was a quiet morning. Reminded me of the first day, after we all learned why we were here."
    "Looking around at the faces in the cafeteria when I arrived, I got the same vibe as before. The embarrassment everyone was probably feeling because of their 'second puberty' issue."
    "Standing out in the mildly dark gloom of the other students, one face was unexpectedly shining."
    show BBW happy at center with dissolve
    MC "Good morning, Alice."
    BBW "It {i}is{/i} a good morning, isn't it?"
    "I took another quick scan of the room, at the subdued expressions and lack of light-hearted chatting you would normally find."
    MC "It's subjective, I guess."
    MC "Is there a particular reason you're happy? Did Aida make some really nice treats or something?"
    BBW "Business, my dear Hotsure-san. Business is doing well, and it's set to do even better soon."
    MC "Oh, your, what would you call it... Your..."
    show BBW neutral
    BBW "My requisition agency."
    MC "Yeah... That. Are people coming to you for stuff?"
    show BBW happy
    BBW "Word is beginning to spread of my services, with strong customer satisfaction driving an increase of my market share."
    show BBW haughty
    BBW "And I have set my flag on a particular shore with tremendous growth potential, based on both necessity and a consistent need for replacements."
    MC "What... Cell phones?"
    show BBW happy
    BBW "Clothing, my dear boy."
    show BBW haughty
    BBW "It may have escaped your notice, being a guy and all - one apparently not particularly concerned with your own appearance, at that - but the changes we are experiencing are already making the clothing and other accessories we arrived with obsolete."
    show BBW happy at Position(xpos=0.3), Transform(xzoom=-1) with dissolve
    BBW "The school {i}does{/i} supply new uniforms in larger sizes as we need them, but their system does not have the motivating factor of free market capitalism to push their productivity."
    show BBW happy at Position(xpos=0.7), Transform(xzoom=1) with dissolve
    BBW "And such aid only extends to the clothing we need as students. Personal expression and comfort is left to the individual to provide, a tiresome chore when the only stores are outside the school, all the way in town."
    show BBW angry at Position(xpos=0.3), Transform(xzoom=-1) with dissolve
    BBW "And are we supposed to make that trip while wearing ill-fitting, potentially scandalous clothing?"
    MC "Hey..."
    show BBW happy at center, Transform(xzoom=1) with dissolve
    BBW "Now there's a better choice. I, through my personal contacts with the biggest and best names in clothing retail, can offer you-"
    MC "Hey!"
    show BBW surprised
    BBW "!"
    MC "I don't need a sales pitch. I know what you're doing. You offered to get a computer for me, remember?"
    show BBW neutral
    BBW "Yes, yes. Got carried away there for a second."
    show BBW happy
    BBW "But the fact that you're familiar with this is perfect, because I have a proposition for you."
    BBW "I have more potential customers than I have time and energy to corral myself. I need subordinates out there spreading the word and taking orders."
    BBW "How'd you like the job?"
    MC "What, like a salesman?"
    show BBW neutral
    BBW "Not 'like' a salesman. Actually be one."
    show BBW happy
    BBW "It's child's play. All you have to do is distribute these catalogues I've made-"
    "She handed me a box of tri-folded papers - more like brochures than catalogues - that she must have made on her computer."
    "While they lacked the polish an experienced graphic designer would bring, they did get right to the point, emphasizing the low prices and breadth of available sizes for every body type."
    BBW "-and talk up what a bargain this is. Be sure to emphasize the more prestigious name brands, and that other designer labels will be available in the future."
    show BBW neutral
    BBW "Still have a few more deals to finalize. This school is so remote, bulk shipping out here is a logistical nightmare."
    show BBW happy
    BBW "But we already have most of our selection here at the school, ready to distribute to any interested buyer."
    BBW "And if anyone wants to see our products in real life, you can tell them that I'm already wearing my first new set of clothing."
    BBW "The school told me it would take as much as a week to get me a larger set of uniforms, but I - going directly to the company that has the contract with this school - was able to get this comfortable and properly-fitting outfit before my old set became restrictive."
    "She did a quick modeling job, turning around to show how her top didn't pinch or roll up on her now-wider torso and rounder belly."
    show BBW happy at Position(xpos=0.5, ypos=0.0, yanchor=0.3), Transform(zoom=2.0)
    "I actually hadn't noticed that she had gotten plumper. It hadn't been two weeks yet, and I wasn't expecting to see such changes so quickly."
    "But apparently she had, because unless she had told me I wouldn't have noticed that this was a larger outfit, and it fit her as well as her old set. I could see how she thought this would be a good advertisement for her business."
    show BBW haughty at center, Transform(zoom=1.0)
    BBW "No muffin top, no pinching in the sleeves."
    "I was still looking over her plump middle, my eyes lingering on the soft curves of her belly, when she snapped me out of my reverie."
    show BBW happy
    BBW "Sound good?"
    menu:
        "I could use a little spending money.":
            MC "I could use a little spending money."
            BBW "Can't we all?"
            MCT "I don't think you're hurting..."
            jump BBW010_accept
        "(Might as well agree. I don't think she'd take 'No' for an answer.)":
            MC "Sure, I can do it."
            show BBW neutral
            BBW "I was hoping you'd be a little more fired up, but..."
            BBW "As long as you bring the thunder when you're engaging the customers, it's fine."
            MCT "Bring the thunder?"
            jump BBW010_accept
        "You can count on me!":
            MC "You can count on me!"
            BBW "Excellent! That enthusiasm is exactly what I'm looking for."
            jump BBW010_accept
        "No. I... I don't want to work for you.":
            jump BBW010_decline

label BBW010_accept:
    $setFlag("BBW_working")
    show BBW happy
    BBW "We can discuss your salary and bonuses later. Right now I want you to take advantage of the period before classes."
    BBW "Get out there and distribute those catalogues. I want to see that box at least half-empty before the bell for first period rings."
    "Caught up in her energy and enthusiasm, I sped away to start hawking her services."
    "I tried to think of who would need new clothes. Like Alice, I hadn't noticed any real growth in anybody yet."
    "But maybe necessity wasn't the best avenue to take yet. Maybe there was someone who just wanted something nice and flattering for after school."
    menu:
        "Shiori. She tends to dress conservatively, but doesn't every woman want to look nice?":
            jump BBW010_c1
        "Aida. Alice had mentioned she doesn't have an extensive wardrobe.":
            jump BBW010_c2
        "Honoka. Even if she hasn't grown, her needs already stretch most clothing shops.":
            jump BBW010_c3

label BBW010_c1:
    $setFlag("BBW010_shiori")
    scene Hallway with fade
    show AE angry at center with dissolve
    "I found Shiori prowling the halls, eyes jumping around from student to student, as if she was looking for violations of the school dress code or something."
    "For a second I thought this would be a good lean-in to my sales pitch, but when I saw her expression I scratched that idea."
    "Something a little more subtle would be needed."
    MC "Hey, Matsumoto-san. You sleep well?"
    show AE neutral
    AE "Hotsure-san. Well, I'd say about four hours at this point, however that's neither here nor there. Anything you need?"
    MCT "I could respond with 'Actually, it's about what you need.' Except she looks more serious than usual."
    MC "Just making conversation. We are classmates, after all. We should be friendly with one another."
    AE "Ah, I see. Yes, well, while I'm all for interaction, I'm preoccupied at the moment. Begging your pardon."
    "She started to turn away, but I at least had to give her a 'catalogue' to say I did my job."
    "Gracelessly, I almost shoved one of them at her arm."
    MC " Here. Something to check out at your leisure, when you have some free time."
    show AE surprised
    AE "Hm? What is...The Nikumaru Outlet Direct? Keisuke...is this what I think it is?"
    "Something in her tone told me to tread carefully. But I, not exactly a cat burglar, couldn't do much except flail around."
    MC "Well, it's... I'm not sure what you think it is. What do you..."
    show AE angry
    "She's glaring at me, and I see that playing coy wouldn't work even if I could do so properly."
    MC "Alice... Nikumaru-san has created a direct-market business. She orders stuff from manufacturers and can sell them at a discount. Clothes, school supplies, stuff like that."
    show AE angry
    AE "Hotsure-san...you can't just...ngh...where is Nikumaru-san? I swear if she thinks she can just undermine the administration with this-this tripe!"
    MC "She should be in the cafeteria..."
    "Only now did I realize what a blunder this was. Of course the school would have some rule about not running a business out of your dorm or something like that, and of course Shiori would memorize it and expect it to be followed to the letter."
    hide AE with dissolve
    "Shiori was already brushing past me, making a direct line for the cafeteria."
    $setAffection("BBW", -1)    
    "I looked down at the box of 'catalogues' I was holding, wondering if I should keep handing them out or consider myself fired."
    jump daymenu

label BBW010_c2:
    scene Cooking Classroom with fade
    "My first guess was that Aida would be at the cooking classroom, preparing Alice's breakfast. I wasn't wrong."
    show PRG neutral at center with dissolve
    "When I saw the baggy state of her clothes I thought this was probably a dead end. But then I wondered if she had any casual clothing that fit her and pushed on."
    MC "Good morning, Kodama-san. Making breakfast?"
    show PRG happy
    PRG "Oh!  Uh, hello Hotsure-san. Is Nikumaru-sama ready for her food?  I-I can hurry it up..."
    MC "Oh no, it's not that. I was just walking by and thought I'd say hi."
    MC "Is that a new uniform? It looks a bit baggier than your old one."
    show PRG sad
    PRG "Um, d-do you not like it?"
    "For a split-second I thought about suggesting she buy something in her own size, but her doe-eyed expression made her look like she was on the brink of tears and I shot that idea down."
    MC "No, it's... it's cute."
    MC "But when you're cooking you don't really want anything that can get stained or burnt, right?"
    "I took out one of the 'catalogues' and held it out."
    MC "If you're interested in something a bit more form-fitting - for safety purposes - there's..."
    show PRG sad
    "I trailed off, because her expression had turned ashamed, lip bit and eyes downcast."
    MC "What?"
    PRG "I, I'm sorry Hotsure-san, but... W-well, I already got these from Nikumaru-sama. I was her first customer."
    "I suppressed a groan as I realized that of course Aida would already be in on Alice's plans. It was her need for more clothing that had first put the idea of doing this in Alice's head."
    MC "Right, right. Forgot. Well, sorry to bother you."
    show PRG neutral
    PRG "No, no! I'm sorry for, um, wasting your time...  I'll, uh, still take one of the pamphlets, if you like..."
    "Hesitantly, I handed her one. I think not doing so would have made her more embarrassed."
    MC "If you'd like to place an order... Well, you know where to find me."
    if getAffection("PRG") >= 3:
        show PRG happy
        PRG "Yes, th-thank you, Hotsure-san... I-I'll see you later."
    else:
        show PRG neutral
        PRG "Yes, th-thank you, Hotsure-san..."
    "As I walked away I wondered who was more embarrassed, me or her. She was doing a better job of putting a happy face on it, at least."
    "My first stab at a sale and I whiffed it. But I still had time before class started, so the morning wasn't a complete waste. Yet."
    jump daymenu

label BBW010_c3:
    scene Hallway with fade
    "I was trying to think of where I could find Honoka when I was tackled from behind, collapsing to the ground."
    play sound Thud
    "A heavy, squishy weight on my back told me my search was over."
    show BE happy at center with dissolve
    BE "Hey, Kei-chan. You're looking a bit more spaced out than usual. You hit your head on something? I mean, besides me, of course."
    "Climbing to my feet, the sales pitch I had been rehearsing in my mind was pushed aside as I tried to think of something sarcastic and/or witty to say in response."
    MC "You ask me that after you run into me? Project much?"
    MC "At least help me clean these up."
    BE "What're these?"
    "I didn't process the question as I found myself distracted by Honoka's chest. After Alice's modeling routine I had curves on the brain, and Honoka was looking particularly big today."
    show BE zoomin at Position(xpos=0.65, ypos=0.0, yanchor=0.25), Transform(zoom=0.8)
    BE "Hey, Earth to Keisuke? You look like you took a hit to the noggin, considering you can't lift your neck above chest level."
    MC "I was just... Um..."
    show BE neutral at center, Transform(zoom=1.0)
    "And then, as if struck by inspiration, I realized this was actually perfect."
    MC "I was just noticing that your shirt looks a bit tight. That can't be comfortable, can it?"
    show BE neutral
    BE "Oh yeah! Definitely tighter. Been noticing it get tighter every day recently. Was pretty fun at first, definitely proof that I'm growing where they said I would."
    BE "But, heh, yeah, it's not exactly comfortable. You have no idea how much bras pinch when they aren't made to fit you right."
    MC "Bras... Yeah. Those things."
    "Black lace bras with the cups almost transparent, frilly edges rising from her cleavage like dolphins jumping out of the sea. White cotton cups pulled taut by two great mounds of flesh, the straps digging into her shoulders..."
    BE "..."
    MC "Ah!"
    "I snapped my head downward to escape eye contact with her. Only then did I remember the box I was again holding in my hands. I took out one of the 'catalogues.'"
    MC "If you're looking for new clothing, there's a new service that just opened up. Really affordable clothes, some custom-made, direct from the manufacturer."
    "Quizzical, she looked the 'catalogue' over."
    BE "Huh. Wow, there's a lot of stuff in here. Pretty neat, actually. Most of the time once you get past a certain size, you can only get bras in boring colors or things without patterns. It really takes the fun out of it."
    BE "But, they're saying here they can do more custom patterns? Prices seem okay too, all things considered. How'd you get your hands on this?"
    MC "Ali- Nikumaru-san hired me. She knows people in high places at all these companies, so she has an 'in,' so to speak."
    MC "She's also selling school supplies and other stuff, but I guess she's focusing on clothing right now because... Well."
    "I gestured at her chest, wrapped up in a too-tight shirt and bra."
    show BE happy
    BE "Because it's like starting up an ice cream stand in the middle of a heat wave. She'll make a killing here if she can get everything authorized! You better be getting a cut of all of this if you're going to be helping her out. Don't let her take advantage of you."
    show BE surprised
    BE "Unless you're into that kind of thing. A big girl like Alice? Yeah,  I could definitely see that. Was there a dominatrix getup in this catalogue? That'd be something to see on her..."
    "Man, my imagination was getting a workout today."
    "I shook my head to clear my mind."
    MC "I am being compensated (though the specifics haven't been hammered out yet). I believe she even mentioned something about a commission."
    MC "So can I put you down for a sale? I can run your order back to her before class starts, but I'm not sure how long it will be until everything arrives. She did say she already has a lot of stuff here..."
    show BE happy
    BE "Oh absolutely! Here, let me take a look again real quick. ... Yeah, I think I can spring for three bras and, maybe two shirts. No I'll just stick with this one for now. Luckily I've been looking up how to properly measure busts so I can figure out my own size. Well, as long as I'm capable of getting my arms around them that is!"
    MC "Even if you have trouble measuring yourself, we can find clothing big enough..."
    "My voice trailed off as I was hit with the mental image of Honoka carrying a pair of breasts bigger than she was, carting them around in a wheelbarrow..."
    "...and running me over with them."
    "Like I said, my imagination was running on all cylinders today. Salesman-mode had delayed the image conjured by her blithe comments about her growth, but the idea that she would grow so big she couldn't wrap her arms around herself... That was impossible to ignore."
    "I cleared my throat, blushing as I saw her smile mischievously at me, and sputtered."
    MC "I'll get back to you on how soon we can deliver these. Do you just want the plain model for the bras?"
    show BE surprised
    BE "Oh god no. I want one with the heart design, one with the joystick design, and, hm, I dunno, probably one with just some nice color. What do you think would be best; blue, pink, or black?"
    MCT "Black! Black!"
    MC "I think... black might be best. Bold, but not garish."
    show BE neutral
    BE "Sounds good to me. We'll go with the black then. And I circled the shirt I wanted too. Thanks Kei-chan. This is pretty cool, I appreciate it."
    MC "Well, I am being paid. But you're welcome, all the same."
    "She winked playfully and then spun around, jogging away."
    "Even from the back I could see the extra bounce... in her step. I admired it for a moment, and then turned back to the matter at hand."
    $setAffection("BBW", 1)
    "Landing a sale five minutes into my job was great, but I suspected Alice wouldn't ignore a still-full box of 'catalogues' because of it."
    jump daymenu

label BBW010_decline:
    stop music
    MC "No. I... I don't want to work for you."
    show BBW neutral
    "She was quiet for a second, as if she wasn't expecting that answer."
    BBW "I'm sorry? Could you say that again?"
    MC "I'm not interested."
    BBW "Do you understand what an opportunity this is?"
    BBW "Are you worried about balancing a job and your school work? Because I can understand your trepidation."
    menu:
        "It's not a question of time. I just don't want to work for you.":
            play music Bittersweet
            $setTimeFlag("BBWnowork")
            MC "It's not a question of time. I just don't want to work for you."
            $setAffection("BBW", -10)
            show BBW angry
            BBW "So be it."
            BBW "I hope you learn not to dismiss future opportunities so casually."
            BBW "The world can get quite competitive. If you expect things to be handed to you..."
            BBW "I don't have time for this. Good day."
            hide BBW with dissolve
            MCT "That was actually less volatile than I was expecting."
            jump daymenu
        "Well... I guess I can try it out.":
            play music BBW
            MC "Well... I guess I can try it out."
            MCT "It's not like I'm eager to work for her, but a little extra green wouldn't be too bad."
            jump BBW010_accept
    
label BBW011:
    scene Hallway with fade
    play music Schoolday
    "Another day done, and I find myself with no idea of what I want to do."
    "The afternoon's a blank page, but when you can start in a million different ways it's impossible to pick just one."
    MCT "It's not like I'm hoping to find something to do if I wander around the school long enough, but... Maybe I will?"
    scene Gym with fade
    "Half an hour passed. I walked from the classrooms to the gym to the pool to behind the campus. Nothing."
    scene School Planter with fade
    "Another half hour. I went to the rooftop, the garden. Nothing."
    "At one point I thought I saw a person sneaking behind the cafeteria, but they were gone when I got there."
    scene Dorm Exterior with fade
    "Another fifteen minutes of walking, and I started to think maybe I should have gone to the gym and gotten a real workout in."
    "I had finally decided to go back to my dorm and take care of my homework when I was saved from my boredom by almost running into Aida."
    show PRG surprised at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    MC "Whoops. Pardon me."
    show PRG neutral
    PRG "O-oh! I'm sorry."
    "Coming right behind her, albeit not running headlong, was Alice."
    show BBW neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Don't mind her. She's too excited for her own good."
    BBW "Watch where you're going, Kodama-san."
    PRG "Y-yes, ma'am."
    MC "What's going on that has you in such a rush?"
    BBW "Kodama-san wants to join the film club meeting today. Apparently they're screening one of her favorite movies."
    show PRG happy
    PRG "It's called Waiting for the Wrong Bus. It's a romantic-comedy from a couple years ago."
    MC "Yeah, I've heard of that. Typical chick flick, right?"
    PRG "Oh, it's more than that. It's a beautiful and tender tale of two destined souls overcoming circumstances working to keep them apart-"
    MC "Isn't it because they don't like each other at first, but then they do?"
    show PRG angry
    PRG "No! It's not just that. Come watch the movie with us and you'll see."
    BBW "It does sound like every other rom-com I've seen."
    PRG "You're both wrong."
    menu:
        "Sorry, but I've got homework to do. And chick flicks aren't my thing, you know?":
            jump BBW011_fail
        "OK, OK. I'll come with and see for myself.":
            jump BBW011_prechoice
            
label BBW011_fail:
    MC "Sorry, but I've got homework to do. And chick flicks aren't my thing, you know?"
    show PRG sad
    PRG "Oh... All right."
    show PRG happy
    PRG "Maybe some other time?"
    MC "Uh, maybe."
    jump daymenu

label BBW011_prechoice:
    MC "OK, OK. I'll come with and see for myself."
    show PRG happy
    PRG "!"
    "Aida's face lit up, clearly happy to have another person accompanying her."
    stop music
    scene Hallway with fade
    "The three of us went to the club meeting. There were about a dozen members, the upperclassmen and women showing fully developed factors like muscles or extra-large hands."
    "But the screening room was much bigger than our classroom, which left plenty of seats for guests."
    "100 minutes later we were back out in the hallway."
    show PRG happy at Position(xpos=0.25)
    show BBW neutral at Position(xpos=0.75)
    play music Rain
    PRG "What did you think? Wasn't it beautiful?"
    "Aida had her hands clasped in front of her heart, her cheeks rosy and her eyes closed. She looked like she might swoon at a moment's notice."
    BBW "..."
    "Alice, meanwhile, looked like she was listening to elevator music playing at one-half speed."
    menu:
        "It was... sweet?":
            jump BBW011_c1
        "They didn't like each other at first, and then they did. I called it.":
            jump BBW011_c2
        "Well... Alice? What did you think?":
            $setSkill("Art", 1)
            jump BBW011_c3

label BBW011_c1:
    MC "It was... sweet?"
    PRG "Wasn't it? When Kenji ran into the burning building to get her teddy bear it was so touching."
    PRG "What was your favorite part?"
    MCT "Guess I've got to make a bluff check."
    MC "When Kenji... was complaining about Ayami and then suddenly he was talking about how much he loved her?"
    "That actually had to have been my least favorite scene, but that's why it was the only one I could think off."
    "And the way Alice fought back a snort, it didn't look like the movie had worked on her, either."
    "But this was an opportunity to free myself from the conversation."
    jump BBW011_c3

label BBW011_c2:
    MC "They didn't like each other at first, and then they did. I called it."
    show PRG angry
    $setAffection("PRG", -1)
    PRG "But it's more than that. It's about them realizing what the other means to them, and how happy they are together."
    MC "I have to say, I didn't see that. They spent, like, 75%% of the movie sniping at each other, and then suddenly they want to be together?"
    PRG "It's not sudden. Don't you remember the scene where Kenji warns Ayami not to eat the shrimp that made everyone else sick?"
    PRG "It's because deep down he cared about her."
    MC "That only makes sense if you can believe that neither would come out and say what they were feeling."
    MC "But that seems to be every movie like this. All their problems would be solved if they were just honest for five seconds."
    show PRG happy
    PRG "But then they wouldn't get to show their love. What about when Kenji ran into the burning building to get Ayami's teddy bear? Wasn't that dashing?"
    MC "And then he realizes he could have gone around the building to get to Ayami's room, because the fire hadn't touched that place yet. And then he trips and knocks himself out. It was amusing."
    MC "But running into the building in the first place? I'm really not a fan of the big, showy demonstrations of love. They always come across as manufactured."
    show PRG angry
    MC "That climax in particular... Probably the only realistic thing in the movie was the firefighters berating him for that stupid stunt."
    PRG "But he got the bear!"
    MC "The bear was never in danger."
    PRG "That's not the point!"
    "I could see how quickly this was falling apart, and I didn't want to keep digging myself deeper."
    "Fortunately, I had an out."
    jump BBW011_c3

label BBW011_c3:
    show PRG neutral
    MC "Well... Alice? What did you think?"
    "Alice looked down at Aida, still blushing deeply."
    BBW "I think it was exactly like every other rom-com I've seen."
    MC "Is that a good thing?"
    BBW "If it's what you're looking for, yes. The familiar has its own appeal."
    show PRG sad
    PRG "But you didn't like it?"
    "Alice hesitated again before responding. Despite her bored expression, her quick glances at Aida told me she was being careful with her words."
    "Concern for Aida's feelings, I would assume."
    BBW "The genre is well-established, and as such it has too many ideas that have become cliched through overuse."
    BBW "And all too often that leads to an attempt to outdo the cliches, rather than to break fresh ground."
    BBW "The once-novel idea of having two people not express their feelings gets turned into an obstinate game, each character overexaggerated to the point of cartoonishness."
    show PRG neutral
    PRG "Games?"
    BBW "If there is something you want and you do not make every effort to claim it, what are you doing? You are playing around, wasting time and effort."
    MC "That's a pretty harsh view of romance, don't you think? You make it sound like a guy going after a girl sees her as nothing but a prize."
    BBW "Her heart is the prize."
    BBW "Courtship is a challenge, the man is tested and tries to prove himself. And, if he is successful, he is rewarded with her love."
    MC "But the woman doesn't have to do anything? Doesn't have to prove herself?"
    BBW "Women have their own trials in any relationship, but how often are we the pursuer?"
    MC "Not big on women's lib, I take it."
    show BBW haughty
    BBW "Au contraire. I've never met a woman in our generation more dedicated to conquering the world of business and smashing the glass ceiling than I am."
    BBW "I'm simply a realist. Even with advances in women's equality it's considered custom for the man to initiate, to pursue, to 'win.'"
    BBW "But this set-up gives us ladies our own power, as long as we recognize it and use it."
    MC "So you don't mind being considered an object, a trophy?"
    MC "You wouldn't be insulted if, say, I asked you out, dated you, and then 'won' you? Made you my wife?"
    "She chuckled, brushing one of her locks behind her shoulder."
    BBW "Hotsure-san... Do you know what a woman wants?"
    MC "Eh?"
    MC "You mean like flowers and chocolates?"
    show PRG happy
    PRG "Or stuffed animals!"
    show BBW neutral
    BBW "No, I'm not talking about simple gifts."
    BBW "I'm talking about romance. Do you know how to woo a lady?"
    MC "Yeah! I mean... I've dated before. I understand romantic... stuff."
    MCT "I just lost the argument when I called it 'stuff,' didn't I?"
    show BBW haughty
    BBW "Romantic 'stuff.' Heh."
    BBW "I don't think I need to worry about becoming merely your wife."
    BBW "Thinking it is your job to win means you are destined to lose."
    show BBW neutral
    BBW "Fun talk, though. We should do this again."
    BBW "Hopefully with a better movie."
    show PRG sad
    PRG "But *I* liked it."
    jump daymenu
    
label BBW012:
    if getFlag("BBW_working"):
        $setProgress("BBW", "BBW015")
    else:
        $setProgress("BBW", "BBW016")
    scene Classroom with fade
    play music Schoolday
    "When the classes ended for the day, I was more than ready to shut my brain off."
    "The whammy of the news of our condition didn't mean we got to stop learning. Tashi-sensei ran the class like a herd of pack mules, just instead of piling loads of goods onto our backs we were packing our brains full of facts and figures."
    "I had several chapters of reading to get through later that day, but first I needed to decompress before my grey matter started to overheat."
    "But as I gathered up my things and made to leave, I felt a hand on my shoulder."
    show BBW neutral at center with dissolve
    BBW "Keisuke, do you have a moment?"
    MC "Uh... Yes?"
    show BBW happy
    BBW "Excellent. We need to have a meeting to discuss the future of The Nikumaru Outlet Direct."
    BBW "I'm calling all employees in, so come along."
    scene Cafeteria with fade
    "I followed Alice to the cafeteria, where Aida had already laid out tea and crumpets at Alice's usual table."
    show BBW happy at center with dissolve
    BBW "Good. We're all here."
    MC "All three of us?"
    show PRG neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    show BBW neutral
    BBW "Both of us. Kodama-san is still operating in her capacity as my personal assistant, so for now this is still a two-person operation."
    show BBW happy
    BBW "There's me in the CEO/CFO/President chair, and you pounding the pavement to get orders and make deliveries."
    hide PRG with dissolve
    BBW "It's exactly the type of humble beginnings that all great corporate empires are born from."
    show BBW angry
    BBW "But we're in the midst of a crisis right now. Our very existence as this school's premiere clothing retailer is under attack."
    show BBW neutral
    BBW "Hence this meeting. We need to address this attack on free enterprise: Matsumoto-san asserts that it violates the school's rules and regulations for a student to run a business on campus."
    if not getFlag("BBW010_shiori"):
        MC "Wait, we're not allowed to be doing this? Then why are we having this meeting?"
        show BBW haughty
        BBW "Don't be so hasty to accept defeat, Keisuke. As in any competition, to win in business is not just to strive for success, but to reject failure."
        BBW "If you allow others to set the terms you're handicapping yourself. It is only when you seize control of the playing field and the rules of the game that ultimate victory becomes possible."
    MC "So you think there's some sort of loophole to exploit?"
    show BBW haughty
    BBW "Over, under or through. There's always a way to get past a mountain."
    BBW "The Nikumaru Outlet Direct will not shutter its doors just because one nosey bureaucrat seeks to hobble us. I've already found a way forward."
    jump BBW012_c1
    
label BBW012_c1:
    menu:
        "About that name..." if not getFlag("BBW012_c1_1"):
            jump BBW012_c1_1
        "About that name... (disabled)" if getFlag("BBW012_c1_1"):
            pass
        "Maybe we should just stop before we get into real trouble." if not getFlag("BBW012_c1_2"):
            jump BBW012_c1_2
        "Maybe we should just stop before we get into real trouble. (disabled)" if getFlag("BBW012_c1_2"):
            pass
        "I'm all ears.":
            jump BBW012_c1_3

label BBW012_c1_1:
    $setFlag("BBW012_c1_1")
    MC "About that name... It's a bit long, isn't it? And kind of bland."
    show BBW neutral
    BBW "That is one thing addressed in my plans. I admit, marketing is not my strongest suit."
    BBW "But if you have a suggestion, by all means. Share."
    MC "How about... Niku-Knacks!"
    show BBW angry
    BBW "..."
    show BBW neutral
    BBW "OK. Marketing is a weak point for both of us."
    BBW "I'll keep that in mind."
    jump BBW012_c1

label BBW012_c1_2:
    $setFlag("BBW012_c1_2")
    MC "Maybe we should just stop before we get into real trouble."
    show BBW angry
    "Alice scoffed-"
    BBW "Scoff."
    "-and gave me a withering look, but I pushed on."
    MC "Maybe Matsumoto-san's a bit strict, but she's not being a hard-ass-"
    MC "Um, she's not some sort of killjoy that has it out for you personally."
    MC "The school has rules for a reason, even if we don't always like them. It's lame, but true."
    MC "And with everything on our plates right now anyway, with school work and dealing with our conditions, do you really want more drama in your life by starting something with the class president?"
    MC "Or maybe the teachers and administrators?"
    "She didn't respond immediately, but I simply waited. She looked irritated enough already and I knew better than to poke her."
    "After a moment she exhaled."
    show BBW neutral
    BBW "This is how I'm dealing with it."
    MC "I'm... sorry?"
    BBW "The schoolwork isn't too much for me. If anything it's a bit easier than at my old school."
    BBW "But the news about our condition? I've already tried to stop it by dieting and working out. It wasn't successful, and I've come to accept that - for now, at least - my weight gain will run its inevitable course."
    show BBW angry
    BBW "But that doesn't mean I will allow it to change my life."
    BBW "I was already on the path to a life of success and prestige in the world of business before I came here. My size will not be a roadblock, or even an obstacle."
    show BBW haughty
    BBW "I will proceed as I was before, as if nothing has changed."
    BBW "I am not ignoring what is happening, but neither will I allow it to control me or my actions. That is not the Nikumaru way."
    menu:
        "Oh... I think I understand.":
            jump BBW012_c2_1
        "I still think you're making trouble for yourself down the line.":
            jump BBW012_c2_2

label BBW012_c2_1:
    MC "Oh... I think I understand. You're pretty serious about this, huh?"
    $setAffection("BBW", 1)
    BBW "I am always serious about business, Hotsure-san."
    MC "I can respect that, even if I'm not entirely convinced it won't come back to bite you."
    MC "But if you're sure you want to do this, I can help."
    jump BBW012_c1

label BBW012_c2_2:
    $setFlag("BBW012_c1_1")
    MC "I still think you're making trouble for yourself down the line."
    MC "And I've gotta be blunt, I don't fancy getting Matsumoto-san or any of the teachers getting on my case because you're trying to make a few extra dollars."
    show BBW angry
    $setAffection("BBW", -1)
    BBW "If you're that concerned, don't be."
    BBW "You're simply a hired hand. If any hammer is dropped it will be on my head."
    MC "I'm not asking you to take all the blame-"
    show BBW haughty
    BBW "Whatever your objections, you'll be protected. This is my business, after all."
    BBW "You worry about making your deliveries, and I'll handle everything else."
    jump BBW012_c1

label BBW012_c1_3:
    show BBW happy
    BBW "Earlier today I contacted a clerk at a law firm that does occasional out-of-house work for my father's business."
    BBW "As we speak she's filing the paperwork to create the Alice's Wishes Granted LLC."
    BBW "Its official address will be a PO box I've secured in town, with all correspondence coming or going through it. Legally speaking, no business will be conducted on school grounds."
    MC "That's your solution? Won't that be inconvenient for people who want to place orders, having to mail a letter to a PO box?"
    MC "And who's going to collect the mail? I don't think-"
    "Alice held up a hand to stop me."
    show BBW neutral
    BBW "We won't be taking orders through snail mail. That's far too inefficient."
    BBW "If you hadn't interrupted, I would have explained that I also have a software engineer developing a website and business email account."
    BBW "Everything involved in placing the order and paying for it will be handled online. The PO box is merely a formality."
    BBW "Understand?"
    MC "I guess. Is it really necessary?"
    BBW "Yes. As I said, by establishing a storefront off school grounds I am no longer in violation of any rules."
    MC "And what about filling the orders? Will the packages be delivered to you here?"
    show BBW happy
    BBW "Got it in one. While there are prohibitions on what items can be mailed to students here, our selection of products does not include weapons, drugs, or other such items."
    BBW "Everything to be mailed to me is in keeping with permissible personal effects."
    MC "You're still exchanging goods for money."
    BBW "No, I am accepting gifts purchased by my fellow students and then graciously returning them when it turns out they do not suit my needs."
    MC "You're... what?"
    "She grinned deviously, like a smug cat meme."
    show BBW haughty
    BBW "Once the website is up and running you'll see. Or perhaps I should tell you now."
    BBW "The website and order form will be constructed so as to appear as if our customers are buying items on my personal wish list."
    BBW "All orders will be mailed to me, with the customer's information included as a special message so I know who the thoughtful party is."
    MC "And once you have a new skirt or set of underwear you'll say 'Oh, this doesn't fit me' or 'Oh, it's not my style' and you 'give it back' to the person who bought it."
    "Her smile didn't grow wider, but it somehow grew more smug."
    MC "One question: What's the difference between bending the rules and breaking them?"
    BBW "Breaking gets you punished. Bending increases your profit margin."
    jump daymenu

label BBW013:
    scene Hallway with fade
    "My name had come up on the class clean-up schedule again, so when I got out for the day the hallways were mostly empty. Everyone else was back at their dorm or enjoying the pleasant afternoon."
    "It made it easy to recognize the two figures over by the stairs, even if one wasn't the only blonde woman on campus and the other wasn't..."
    show BBW angry at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    MCT "Oh no..."
    "If the other wasn't my roommate."
    play music RM
    show RM angry at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    "I couldn't hear what they were talking about, but I could see Alice standing rigid, her expression stony cold as Daichi held up one of those measuring device clamp things."
    "What were they called? Shiori would probably know..."
    "Anyway, I started walking slower, not wanting to eavesdrop on the two but also fearing I had some idea of what they were talking about."
    RM "Taking these measurements now is vital if we're going to chart your future expansion. We need to know how much you weigh and where your body distributes your fat-"
    BBW "Grrrr!"
    RM "-to compare with how big you - and specific parts of you - will become later."
    show RM neutral
    RM "I also need you to answer some questions about your eating habits, your exercise routine. If you have one."
    RM "Are you eating more than you did before you came here? More often? Are you hungrier than before?"
    RM "Do you find it harder to carry your weight? Do you get tired more quickly?"
    RM "This will all tell us what 'they' are doing to you, which will give us a clue as to their ultimate plans."
    MCT "Yeah, this is exactly what I feared."
    BBW "'They?' 'They' who?"
    show RM angry
    RM "The govern-"
    BBW "Clearly I was being facetious. I don't actually want to know what paranoid fantasy you're harboring."
    MCT "I should probably step in and get Daichi out of there before she really tears into him."
    MCT "Then again, I don't want to bring her wrath upon myself..."
    menu:
        "Stay back. Daichi got himself into this.":
            jump BBW013_c1
        "Rescue Daichi.":
            jump BBW013_c2

label BBW013_c1:
    play music Tension
    "I backed away slowly, not drawing either's attention, and hid inside a classroom door."
    BBW "Do you think I have nothing better to do than be accosted by some conspiracy theorist?"
    BBW "What are you, a 'growth truther?' Do you think they're slipping us hormones in our food?"
    show RM neutral
    RM "That might actually be-"
    show BBW angry with hpunch
    BBW "I DON'T HAVE TIME FOR YOUR GAMES, BOY!"
    BBW "I am stuck here on an isolated rock, shoved away with a bunch of other... people with conditions like mine, dealing with the news that my own body is going to blimp out of its own accord."
    BBW "And you want to get in my face about some secret cabal making me fat?"
    RM "To be honest, I don't know who exactly is doing this."
    show BBW angry with hpunch
    BBW "SHUT! IT!"
    BBW "And answer me this: if there was an insidious conspiracy bent on performing experiments on random people, do you really think that I, Alice Nikumaru, daughter of Daitaro Nikumaru, would be one of those guinea pigs?"
    BBW "My father has connections reaching through every corner of the world's industrial and political. No one would dare subject me to something like this without invoking his wrath."
    RM "There might have been-"
    show BBW angry with hpunch
    BBW "I TOLD YOU TO SHUT IT!"
    BBW "And get out of my sight. Don't ever even think of planting your grimy little paws on me, and don't ever talk to me about my body again."
    show RM sad
    RM "OK. OK."
    hide RM with dissolve
    show BBW angry at center with dissolve
    "Daichi didn't quite run from her, but he didn't drag his feet."
    "Alice stayed standing there and watched him leave. After a while she exhaled, but she didn't look any less tense."
    "I didn't want to take the long way back to the dorms, so I'd have to walk past her. Hopefully she wouldn't-"
    BBW "Hotsure-san."
    MCT "Uh-oh."
    MC "Ali- Nikumaru-san. You look... tense."
    BBW "Did you hear any of that buffon's rambling?"
    MC "Uh, yeah. I got the gist."
    MC "Daichi's kind of like that-"
    BBW "Daichi? Is that his name?"
    MC "Yep. He's my roommate..."
    "The next words shriveled in my mouth as Alice turned the full intensity of her glare upon me. Too late, I realized my mistake."
    BBW "Your roommate?"
    $setAffection("BBW", -1)
    BBW "So is it a coincidence that out of all the students on campus, he came to me, your classmate, to harass?"
    BBW "Who put it in his mind to come to Alice, the soon-to-be portly girl?"
    MC "Actually he's in our class-"
    MC "Never mind that. I didn't tell him to bother you. I want nothing to do with his ramblings, and I would never put him up to coming after you."
    BBW "(tsk)"
    BBW "You didn't stop him, either."
    MC "No, but... What was I supposed to do?"
    "Alice held up a dismissive hand and turned away."
    BBW "Teach him to have more class. He's in the same boat we all are, isn't he?"
    MC "Actually, he's here because his sister has a growth factor."
    BBW "Either way, he should have some empathy, if not basic social graces."
    hide BBW with dissolve
    "She walked off in a huff, and I wasn't too eager to chase her and explain my uninvolvement."
    "Better to take the hit and let her be angry with me for a while."
    jump daymenu

label BBW013_c2:
    "Daichi was opening his mouth to retort. I couldn't predict his exact words, but I knew they would be some form of doubling down, trying harder to get her to listen to him."
    "I couldn't let that happen. Alice didn't deserve to listen to his ramblings, and Daichi needed to be pulled out of the hole he was digging for himself."
    MC "Daichi! There you are."
    show RM neutral
    RM "Huh? Keisuke?"
    MC "Shiori is looking for you. She said something about a sample the nurse needs to get from you?"
    show RM sad
    RM "Crap! Where was she?"
    MC "Back that way."
    "I hooked a thumb over my shoulder, and Daichi immediately pelted in the opposite direction. He was gone before I even finished walking up to Alice."
    hide RM with dissolve
    show BBW angry at center with dissolve
    play music Rain
    BBW "..."
    BBW "Matsumoto-san wasn't in the classroom, was she?"
    MC "No."
    "Alice let out a gust of air, relaxing in body, but not quite spirit. A feeling of tension hung around her, like an aura."
    show BBW neutral
    BBW "No. At this time she should be in the library, taking care of her paperwork."
    MC "Probably. She is predictable, if nothing else."
    show BBW happy
    $setAffection("BBW", 1)
    BBW "I owe you my thanks, Hotsure-san. If that fool had continued, I'm not sure I could have been held responsible for my actions."
    MC "I wouldn't be surprised. At least you don't have to share a room with him."
    show BBW neutral
    BBW "He's your roommate? Then you must know if he's always like that."
    MC "Yes and no. He's got no shortage of ideas about what's 'really happening' here, but this is the first time I've seen him going that far."
    BBW "Trying to put his hands on someone else?"
    MC "I really don't think he was trying to be grabby or anything. He just... forgot about personal boundaries."
    MC "He is very serious about all this."
    BBW "I suppose some of us are having a harder time dealing with this than others."
    BBW "Assigning blame for this may be more accommodating than accepting it's pure chance. It's easier when you can be angry at someone."
    BBW "What is his growth factor? It must be severe to set him off like that."
    MC "He... It's rather personal."
    "What? It's not like I could tell her Daichi doesn't really belong here."
    "It's not my place to talk about his sister."
    BBW "I understand."
    BBW "Still, one would think that someone in his position would have more empathy for the rest of us. We have all been blindsided by this. None of us should be making it harder for anyone else when it comes to our conditions."
    MC "Yeah. I'll tell him to ease up when I see him later."
    MC "Say, Alice..."
    "I hesitated a moment, but she looked at me, waiting."
    MC "Don't take this the wrong way, but I'm curious. Are you upset about your weight?"
    BBW "No."
    "She answered pretty quickly, in that way that makes it hard to believe someone. But I didn't say anything."
    BBW "I accepted what was happening once I learned the news, and I know I can address my weight gain once it fully happens."
    BBW "In the meantime, I am still Alice Nikumaru. I am not defined by my size or my appetite."
    BBW "Character is revealed in how one deals with tribulation, not what form those trials take."
    MC "You sound like you're dealing with it pretty OK."
    "I was about to walk away, but then I decided..."
    MC "Hey, Alice. I was about to get a snack at the cafeteria. You hungry?"
    BBW "... Hmm..."
    show BBW happy
    BBW "I could go for some cake."
    jump daymenu

label BBW014:
    scene Gym with fade
    play music Peaceful
    "Gym today was a free day, everyone finding something quasi-athletic to do. Afterwards I ended up being one of those called on to clean up the equipment lying around."
    "I wasn't alone, per se, but with a handful of us spread across the entire gym it was dead quiet."
    "After a while I noticed I was drifting over to where Alice was bending down to gather up some croquet mallets."
    show BBW neutral at center with dissolve
    MC "Hey, Alice."
    BBW "Hotsure-san."
    BBW "Can you give me a hand with the mats? Somebody must have been practicing wrestling, or maybe judo."
    MC "I think it was sumo."
    "I inhaled sharply. The idea of sumos made me think of Alice's plump frame destined to grow fatter, and it probably brought the same image to her mind."
    "As we folded up the mats and carried them to the equipment room I scrambled to think of a way to change the subject."
    MC "I don't think I've asked this, but you're from America, right?"
    show BBW neutral at Position(xpos=0.3) with dissolve
    BBW "My mother is. I've lived both there and here in Japan, going to school in both countries."
    MC "What part? Of America, I mean."
    BBW "The east coast. My mom's side of the family has been involved in banking and investing for generations."
    MC "Oh... Are there beaches? Where you lived, I mean."
    "She chortled quietly, her lip turning up in a tiny grin."
    BBW "There are a lot of beaches up and down the east coast. And the west coast. And Hawaii is full of them."
    BBW "But they're not all sun and warm water. Up in New England... You're not doing much surfing or sunning."
    "We finished stacking the mats up, but continued chatting as we cleaned up."
    BBW "Did you grow up near the water?"
    show BBW neutral at Position(xpos=0.8) with dissolve
    MC "No. I just... When I think of America I think of beaches."
    MC "Either that or burgers and fries."
    MC "!"
    "I almost bit my tongue clamping my mouth shut."
    "First the reference to sumo, then greasy American fast food."
    "Did Alice think I was trying to bring up her weight?"
    "She didn't say anything, and I looked around desperately for something else to talk about."
    show BBW neutral at Position(xpos=0.65) with dissolve
    MC "Why are there hockey sticks here?"
    BBW "For the winter, I assume."
    MC "No, out here. Who was trying to play hockey?"
    MC "And dumbbells! This isn't the weight room."
    BBW "I believe I saw Mizutani-san working with those. They may be her personal effects."
    MC "That makes sense. Think we should put them off to the side?"
    "I carried the weights to the bleachers, where I found a large round thing on the floor."
    MC "I don't even know what that is."
    show BBW neutral at Position(xpos=0.2) with dissolve
    BBW "It's used in curling. It's the thing you push across the ice."
    MC "Didn't even know we had stuff like that here. What it's called?"
    BBW "A curling... rock?"
    MC "Rock?"
    BBW "Errrr..."
    show BBW angry
    BBW "Nobody curls in America! That's a Canadian thing."
    "She huffed as she kicked the curling 'rock' across the floor and to the equipment room."
    show BBW neutral:
        linear 1.0 xpos 0.35
    BBW "Grr."
    show BBW neutral:
        linear 1.0 xpos 0.5
    BBW "Bah!"
    show BBW neutral:
        linear 1.0 xpos 0.65
    BBW "Huff."
    show BBW neutral:
        linear 1.0 xpos 0.8
    BBW "Gar."
    "I found a couple skis propped up against the wall and followed her."
    MC "Somebody was messing with the skis as well. Did I sleep through the summer and fall?"
    show BBW neutral
    BBW "Put them over there with the cap gun."
    MC "Why is there a rifle here?!"
    BBW "It's fake, Hotsure-san. I assume it's used for biathlon practice."
    MC "Biath-wha now?"
    BBW "Cross-country skiing and rifle shooting. It's an Olympic sport."
    show BBW neutral at center with dissolve
    MC "Seriously?"
    pause 1
    MC "You're not joking."
    MC "Who thought to put those two things together?"
    BBW "I don't know. I do know it's as ridiculous as it sounds."
    BBW "I saw it at the Winter Games a few years ago. Completely nonsensical."
    MC "You've been to the Olympics?"
    BBW "As a spectator."
    MC "Wow, that's pretty cool."
    "She shrugged."
    show BBW neutral at Position(xpos=0.2) with dissolve
    BBW "Far too many crowds, security checkpoints every twenty feet, and if you wanted to see two different competitions in one day you had to hope they were in the same arena."
    BBW "Too much of a headache to be worth the trouble, if I'm being honest."
    MC "But to travel to another country, meet people from other nations..."
    BBW "Traveling to other countries can actually be tedious. Everywhere you go it's the same franchises, the same highly polished tourist spots where the poverty or unrest is kept at bay to present a picture perfect image of the country."
    BBW "You don't really get a taste for the culture that way."
    show BBW neutral at Position(xpos=0.65) with dissolve
    BBW "As for meeting other people... Only if you speak the same language."
    MC "Oh... hadn't thought of it that way."
    "I didn't have much to say to that, so as Alice and I picked up some kendo sticks I let things get quiet."
    "But things felt even more awkward being next to someone in complete silence."
    "I've never thought small talk was something essential, but as I saw the time needed to finish this stretching out before me I realized I needed to fill it somehow."
    MC "So... have you traveled a lot?"
    "She looked down at a pair of luchador masks she had picked up before answering."
    BBW "I've 'been' to several countries in Europe and Asia, in that I've flown to them while Father conducted business."
    BBW "And we've vacationed in places like Geneva and Tuscany and Monte Carlo. Though we spent almost all our time at exclusive hotels and resorts."
    show BBW sad
    BBW "Tiny little islands within the larger nations, almost isolated from the culture less than a mile away."
    MC "Huh?"
    show BBW neutral
    BBW "The places that cater to the rich tend to have the same trappings, the same luxuries. Sometimes there's an effort to bring a taste of the local cuisine, music and whatnot in, but the separation can become palpable."
    show BBW neutral at Position(xpos=0.8) with dissolve
    BBW "I've always found more amusement and insight in those times when we left the carefully constructed pockets of luxury."
    MC "You like rubbing elbows with the commonfolk, eh?"
    BBW "Nnnnnn- Sort of."
    BBW "Don't get me wrong, I don't want to sleep on a straw mat or wash myself in an outdoor shower."
    show BBW neutral at Position(xpos=0.2) with dissolve
    BBW "But if I'm going to spend several hours flying just to have the same spa services, the same massages, the same Swiss chocolates and mineral water, why even travel?"
    BBW "When I leave home I want to leave my comfort zone. I want to experience something new."
    MC "So when you were in Geneva did you ever go hiking up the alps?"
    BBW "Oh, no! I'm much too sensitive for so much physical strain."
    show BBW happy at Position(xpos=0.65) with dissolve
    BBW "But I did ride the cable-car up to the top of one of the mountains. A splendid view."
    BBW "And the brisk wind made the hot tub extra luxurious that evening."
    MC "So you want to leave your comfort zone, but you don't want to be uncomfortable while you do it?"
    show BBW neutral
    BBW "Mmmm..."
    show BBW happy
    BBW "Yes!"
    MC "And you don't find that odd?"
    show BBW neutral
    BBW "Why should I?"
    "I had no answer to that, so I distracted myself with gathering up a set of bowling pins."
    "After enough time had passed I shifted the conversation."
    MC "Have you been in touch with any friends from your old school?"
    show BBW neutral at Position(xpos=0.2) with dissolve
    BBW "Not lately."
    BBW "There were several people from my old academy I was friendly with, but we've all gone to different places for our higher education."
    MC "Oh."
    MC "I was just thinking..."
    BBW "..."
    MC "It's been a couple weeks since we all got here. It's starting to feel like I'm used to this place."
    MC "At first I didn't try to get in touch with my friends from back home, because none of them probably know about this place or the whole 'factor' thing. But now that I've come to grips with it I can't think of a reason not to tell them."
    "Too late I realized what I had just done: opened the door to bringing up Alice's factor. Again."
    BBW "Your factor concerns your hair, yes?"
    BBW "It doesn't seem to be that significant a dilemma."
    MC "I didn't mean-"
    show BBW neutral at Position(xpos=0.8) with dissolve
    "She looked at me sideways, not grinning but not frowning. Almost like she was trying to do both at once."
    BBW "You're pretty easy to read, Hotsure-san."
    MC "Uh..."
    BBW "You're thinking of my weight, and you're worried about mentioning it."
    BBW "After the incident with your roommate the other day I can understand your trepidation."
    MC "Sorry."
    show BBW neutral at Position(xpos=0.35) with dissolve
    BBW "You don't have to apologize for making me aware of my condition."
    BBW "Though if you want to apologize for thinking that I am so frail as to need to be shielded from reality, I will accept it."
    MC "What?"
    BBW "(Sigh.)"
    BBW "I don't need to be reassured or comforted. My condition is not a death sentence."
    BBW "Having everyone here walk on eggshells around one another would be antithetical to this institution's reason for being, would it not?"
    BBW "We're supposed to address our inevitable growth and learn to live with it, aren't we? A direct confrontation is the only way to do so."
    show BBW neutral at center with dissolve
    BBW "I've already done that, thinking of dieting or exercise and deciding not to make myself miserable."
    BBW "And if I can turn that page, what makes you think you need to shoulder my burden?"
    MC "I wasn't... I mean, not everyone is as fine with this as you."
    MC "I can think of a couple girls in our class having more trouble coming to terms with all this."
    BBW "And I hope they can find peace with it. I sincerely do."
    BBW "But I have other things in my future more important than the number on my scale."
    show BBW happy
    BBW "For instance, it looks like we're almost done with this."
    BBW "I need to take care of my studies, and then it's back to work getting our little business venture going."
    show BBW happy at Position(xpos=0.2) with dissolve
    BBW "Pick up the pace, Hotsure-san! We're almost out of here."
    hide BBW with dissolve
    "We stuffed the last pieces of equipment in the closet, closed it, and went our separate ways."
    "An uneventful conclusion to an uneventful day."
    "Getting a chance to have a real, non-business-related conversation with Alice was pretty eventful. Even if it had been out of desperation to kill time."
    jump daymenu

label BBW015:
    $setProgress("BBW", "BBW016")
    scene Hallway with fade
    show BBW happy at center with dissolve
    play music BBW
    BBW "Keisuke! A mission!"
    "I was headed to... breakfast..."
    show BBW neutral
    MCT "There goes my train of thought. How am I supposed to manage if I can't supply a running commentary of my day?"
    BBW "Keisuke."
    MC "Yes? Good morning."
    show BBW happy
    BBW "Good morning. Are you ready to work?"
    MC "I'm ready for breakfast. It's not work, but it's-"
    show BBW neutral
    BBW "Breakfast is important, but so is fulfilling one's obligations."
    BBW "The wheels of business never stop turning, and thus we ourselves can never cease."
    MC "It's a little early to go looking for sales."
    BBW "That's not what I need you for. Do you remember the restructuring of our company?"
    MC "Hmm? Oh! Right."
    MC "That wish list thing."
    "Only now did I notice the thick mailing envelope in Alice's hand."
    MC "Did we already get an order?"
    show BBW happy
    BBW "First of the company's new era."
    BBW "And you have the singular privilege of making this first delivery. The first delivery of any kind for the company."
    "She handed me the brown, bubble interior envelope, already open."
    "Inside was a folded sheet of paper and a small green and white garment wrapped in plastic."
    "The paper was an order form. Turned out the garment was a pair of panties, ordered by one Moriko Fukushi."
    MC "Where can I find this woman?"
    BBW "She's in room 306 of the women's dorm. You'll find it on the sales slip. If you hurry you can probably find her there now."
    show BBW angry
    BBW "But exercise caution."
    BBW "Mastumoto-san is already keeping one eye on me, and I suspect her myopic adherence to the concept of rules blinds her to the actual letter of the law."
    BBW "Which I am fully in line with, as you know."
    BBW "It's a 'forest for the trees' situation. She has her own idea of what the spirit of the law is, and she's unflappable in following that."
    show BBW neutral
    BBW "The most efficient solution is to avoid contact with her. I have no quarrel with her personally, after all."
    MCT "It would only be antagonistic to point out the simplest solution is to drop this whole venture."
    MCT "And hypocritical. It's not as if I'm turning down the promise of money."
    MC "I got it. Stealth."
    "Alice nodded and let me go."
    hide BBW with dissolve
    stop music
    "The question now was, how to get to the dorm? Guys weren't forbidden from going into the women's dorm building, but it stood to reason it was the place I'd most likely run into Shiori."
    menu:
        "Take the direct approach. Get in, get out.":
            jump BBW015_c1_1
        "Go around and come in from the rear. Less chance of getting caught.":
            jump BBW015_c1_2
        "Think outside the box. Go through the vents.":
            jump BBW015_c1_3

label BBW015_c1_1:
    scene Dorm Exterior with fade #FIXME this may need new graphics
    "I tucked the mailing envelope into my backpack and headed for the women's dorm with deliberate speed."
    show AE neutral at Position(xpos=0.65, ypos=0.0), Transform(rotate=-20) with dissolve
    "I ignored the ladies I passed in increasing numbers the closer I got to the building. If anyone asked I had an excuse at the ready-"
    UNKNOWN "Hotsure-san."
    MCT "Eep!"
    hide AE with dissolve
    show AE neutral at center with dissolve
    play music AE
    AE "What are you doing here?"
    "I had made it to the lobby of the women's dorm, mere feet from the elevator and relative safety."
    "Of course I would get stopped here."
    "Worse, I had the sales slip in my hand as I was double-checking the room number."
    menu:
        "Answer.":
            jump BBW015_c2_1
        "Hide the sales slip.":
            jump BBW015_c2_2

label BBW015_c2_1:
    "Folding the slip one-handed, I casually tucked it into my pocket while answering."
    MC "I was trying to find Mizutani-san. I had a manga I had borrowed from her, and I wanted to give it back."
    AE "And you couldn't wait until class?"
    MC "I suppose I could have, but I wanted to do it before I forgot."
    MC "I'm sure you can appreciate the importance of promptness."
    show AE neutral at Transform(xzoom=-1)
    AE "I do..."
    "Her eyes narrowed. I could feel beads of sweat start to appear at the top of my forehead."
    show AE neutral at Transform(xzoom=1)
    AE "Very well. Go return the book."
    AE "But don't dawdle. Access to the women's dorm is a privilege, not a right."
    MC "Yes, ma'am."
    stop music
    scene black with fade
    "After that brief scare the rest of the delivery went off without a hitch."
    "I found the right room, found Fukushi still there, and gave her the package."
    "Later..."
    scene Classroom with fade
    show BBW happy
    play music BBW
    $setAffection("BBW", 1)
    BBW "Excellent work!"
    BBW "Dependable and resourceful. Keisuke, you have the makings of a great Nikumaru delivery agent."
    "Alice seemed more impressed with my job than I felt I deserved, but it wasn't that odd for her to overreact."
    BBW "Be on standby for the next delivery. Business will start slow, but before you know it be flooded with orders."
    MCT "Just so long as they're not all a close call like this one..."
    jump daymenu

label BBW015_c2_2:
    "Before I said anything I needed to hide that sales slip."
    MC "Well..."
    "I folded the slip in two, and then again, and was just about to put the telltale paper into my pocket when Shiori noticed my fumbling."
    AE "What is that?"
    "Her tone made me shiver. It wasn't an idle question, something I could pass off as 'just a piece of paper.'"
    stop music
    $ timer_count = 2
    $ timer_jump = "BBW015_c2_2_menu2"
    show screen choicetimer
    menu:
        "EAT THE SLIP!":
            hide screen choicetimer
            jump BBW015_c3_1

label BBW015_c2_2_menu2:
    menu:
        "Lie.":
            jump BBW015_c3_2
        "Hand the note over.":
            jump BBW015_c3_3
        "EAT THE SLIP!":
            jump BBW015_c3_1

label BBW015_c3_1:
    "I did the first thing that came to mind."
    show AE surprised
    AE "Ah-"
    "I shoved the paper into my mouth and began chewing."
    "It was hard to chew at first, because the paper was folded twice over. I had to work up some spit to get it soft, first."
    show AE angry
    play music Tension
    AE "Hotsure-san..."
    MC "Yesh?"
    $setAffection("AE", -1)
    AE "Did... did you just destroy evidence in front of me? What was that?"
    "I forced myself to swallow. My throat ached as I struggled to get the wet mass of paper down."
    MC "Gasp!"
    MC "It was... nothing. It was private."
    show AE angry at Transform(xzoom=-1)
    AE "..."
    show AE angry at Transform(xzoom=1)
    MC "There was no mistaking her mood, but the exact thoughts running through her head were harder to figure."
    AE "You are in the women's dorm, with a 'private' note you clearly do not want others to see. Any chance you had of clearing your name of suspicion went down your gullet with the paper."
    AE "But since the note is gone, you no longer have any reason to be here, correct?"
    MC "I-"
    show AE neutral
    AE "Rhetorical question."
    AE "I'm afraid I must ask you to leave, and I will keep note of this."
    scene black with fade
    play music BBW
    "I turned around and left, not wanting to give her a chance to change her mind."
    "Alice was surprisingly chill about the news of my failure."
    scene Classroom with fade
    show BBW neutral
    BBW "This is not the desired outcome, Hotsure-san, but you did mitigate any potentially worse results."
    BBW "I compliment you on your unorthodox solution."
    show BBW happy
    BBW "You still have the package, yes?"
    MC "It's in my backpack."
    BBW "Then all is not lost. After classes today you can try again."
    show BBW neutral
    BBW "I don't know if Fukushi-san belongs to any teams or clubs, but I would suggest waiting until after the dinner hour."
    BBW "You are more likely to find her in her dorm then."
    scene black with fade
    "She wasn't wrong. After dinner I went back to the women's dorm and found Fukushi there."
    "The delivery was made, and I apologized for the less-than-prompt service."
    "Not the smoothest operation, but I avoided complete disaster."
    "Still, it was an instructive taste of what I could expect going forward."
    jump daymenu

label BBW015_c3_2:
    "I couldn't hide the slip, but I didn't have to just hand it over."
    play music AE
    MC "This is a private note, meant for one particular individual."
    AE "Which individual? Perhaps I can pass it on for you?"
    MC "Sorry, but that's private."
    AE "..."
    "I could sense she wanted to ask more questions. Maybe some sixth sense was telling her I was up to no good."
    "But as nosy as she was, there was no rule (as far as I knew) granting the student council search and seizure rights."
    "That is what I was gambling on, and sure enough..."
    AE "Very well. But keep your visit here brief."
    AE "I wouldn't to hear of any infractions on your behalf... understand?"
    MC "Yes, ma'am."
    scene black with fade
    stop music
    "I found Fukushi's room, with her still in it. I gave her the package, thanked her for using our service, and left."
    "Alice was more than pleased with how I handled myself."
    scene Classroom with fade
    show BBW happy
    play music BBW
    $setAffection("BBW", 1)
    BBW "Brilliantly done, Keisuke."
    "Maybe more pleased than was justified, but I wasn't going to complain. It felt good to have done a job well."
    show BBW neutral
    BBW "You will have to be more cautious going forward, though. Spending too much time at the women's dorm will draw attention."
    BBW "That's a problem to consider before our business grows too much. But we can deal with it tomorrow."
    show BBW happy
    BBW "In the meantime, you've earned yourself a snack."
    BBW "Go enjoy the rest of your day."
    "I hung around for a moment, wondering if she was going to give me a couple yen to get myself a treat."
    "But no. She just kept smiling, then jerked her head to dismiss me."
    jump daymenu

label BBW015_c3_3:
    "I couldn't think of a lie that Shiori wouldn't see right through, so I pulled the slip back out of my pocket and held it out."
    play music AE
    MC "Here."
    MC "It's a sales slip. I have a delivery to make for Alice..."
    AE "...Well, I'd like to commend you for your honesty. I'm glad you have the sense for basic decency."
    MC "O-oh?"
    show AE angry
    AE "Unfortunately, the fact that you went behind my back to do this makes that wholly irrelevant!"
    "Of course."
    stop music
    scene black with fade
    "I mostly tuned out Shiori's mini-tirade, already fearing what Alice was going to say."
    "At least Shiori could direct her anger elsewhere. Alice..."
    scene Hallway with fade
    show BBW angry at center with dissolve
    play music BBW
    BBW "Hotsure-san! Explain yourself!"
    MC "I got caught."
    BBW "You laid down and died! You didn't even try to avoid discovery."
    MC "I'm not a natural liar. I'm sorry."
    BBW "Who said anything about lying?"
    BBW "Don't you know how to massage the truth? When she asked what the slip was, you should have said 'It is a private matter between me and someone else.'"
    BBW "Being student council president does not entitle her to intrude on our private affairs."
    MC "It's still lying by omission, isn't it?"
    BBW "Grrrrrrr!"
    BBW "Do you even want this job?"
    "I thought about it for a few seconds, weighing the promise of spending money against the idea of getting in trouble."
    MC "I'm not sure."
    BBW "You think on it. And I'll be thinking of whether you deserve this opportunity."
    hide BBW with dissolve
    "She didn't so much as look in my direction for the rest of the day."
    jump daymenu

label BBW015_c1_2:
    scene Dorm Exterior with fade
    "It would mean taking more time, but this seemed like a good time for the less obvious path."
    "After all, everyone leaving the dorms was heading to the cafeteria, going out the front entrance. Nobody would notice me coming in from the back door and heading right for the stairs."
    "I took the stairs two at a time, doublechecking the room number."
    "When I got to the third floor I peeked through the door. The coast looked clear."
    "It wasn't."
    show AE neutral at center with dissolve
    play music AE
    AE "Hotsure-san? What are you doing here?"
    "Her eyes flicked down to the mailing envelope. I had to think of something, quick."
    if getAffection("AE") >= 10:
        jump BBW015_test_pass 
    if getAffection("AE") >= 4:
        jump BBW015_test_semipass
    jump BBW015_test_fail

label BBW015_test_pass:
    MC "There was a mailing mix-up. Somebody's order got sent to my room."
    MC "They must have put 'Men's dorm' on the address, not 'Women's.'"
    AE "A mailing mix-up?"
    "Shiori-san looked back at the envelope, but then back at me; her eyes showing confusion and possible disappointment. Closing her eyes and exhaling deeply, she looked back to me."
    AE "I understand. I'll have to rectify that from happening again. I...won't keep you."
    show AE happy
    AE "But be sure to be quick. You need to make sure to get breakfast before class."
    hide AE with dissolve
    stop music
    scene black with fade
    "I nodded and walked past her, only mildly guilty about lying like that."
    "Later, Alice complimented me about the job."
    scene Classroom with fade
    show BBW happy at center with dissolve
    play music BBW
    BBW "A satisfying first mission. And you even managed to give Matsumoto-san the slip."
    BBW "Well done. Just be sure to stay on your toes next time as well."
    "The quiet reservations I still had about this entire technically illicit affair were further quieted when Alice smiled at me and gave that encouraging note."
    "I knew this was strictly a business arrangement, but there was still something nice about having her approval."
    jump daymenu

label BBW015_test_semipass:
    MC "There was a mailing mix-up. Somebody's order got sent to my room."
    MC "They must have put 'Men's dorm' on the address, not 'Women's.'"
    AE "That makes no sense. There's not a single female student with the name “Keisuke Hotsure”."
    MC "Y-yeah, well..."
    "Busted."
    "Shiori-san crossed her arms expectantly, showing deep frustration."
    show AE angry
    AE "Look, I'm willing to trust that you're doing as you say."
    show AE angry at Transform(xzoom=-1)
    AE "Do *not* make that trust ill-founded."
    show AE neutral at Transform(xzoom=1)
    AE "Go ahead and take the item to the rightful owner. And then please leave."
    AE "The residents here need to prepare for the day, and I don't want your presence to be distracting."
    MC "Got it."
    stop music
    scene black with fade
    "I nodded and walked past her, not really feeling guilty about lying like that."
    "Later, Alice complimented me about the job."
    scene Classroom with fade
    show BBW happy at center with dissolve
    play music BBW
    BBW "A satisfying first mission. And you even managed to give Matsumoto-san the slip."
    BBW "Well done. Just be sure to stay on your toes next time as well."
    "The quiet reservations I still had about this entire technically illicit affair were further quieted when Alice smiled at me and gave that encouraging note."
    "Her approval was nice, but at the same time I had Shiori's disapproving expression stuck in the back of my mind."
    "I couldn't see a way to keep both ladies happy, but maybe there was a way to not let one down?"
    jump daymenu

label BBW015_test_fail:
    "I tried to think of a plausible lie, but Shiori's gaze was practically stabbing me. So intense, I almost wanted to confess right then and there."
    MC "I... was coming to return a manga I borrowed from Mizutani-san."
    AE "I see. And what is in that envelope?"
    MC "It's just..."
    "She held out a hand."
    AE "Let me see it."
    "I did as instructed. She pulled the panties out, an eyebrow arching as she realized what they were."
    "Fortunately I had the sales slip in my hand, and she didn't look at the label on the envelope. Either of those could have given up the game."
    show AE neutral-smug
    AE "Let me guess. Yours?"
    MC "Don't judge."
    show AE surprised
    AE "!"
    show AE aroused-2
    AE "O-Oh god, I..."
    MCT "Alice, you owe me."
    "She stared at me for a bit, then silently put the panties back in the envelope and handed it back."
    AE "Mizutani-san does not live on this floor. She's one floor down."
    AE "Return her manga and please leave the dorm. The ladies here need to get ready for the day."
    MC "Roger."
    stop music
    scene black with fade
    "I went to the staircase and went down one flight, but I stayed in the stairwell."
    "After a few minutes I went back up to the third and checked the hall again. Shiori was gone."
    "And I hadn't missed Fukushi. I made the delivery and got out of the building."
    "Alice was amused at my cover story, but she was more taken with my commitment to getting the job done."
    scene Classroom with fade
    show BBW happy at center with dissolve
    play music BBW
    $setAffection("BBW", 1)
    BBW "It's not the most airtight story you could have come up with, but you did good, Keisuke."
    MC "Yeah, I've already thought of how I could have handled that in a much less embarrassing way."
    MC "At least I can trust Matsumoto-san to be one of the most tight-lipped people here. Anyone else..."
    "I had a sudden flash of Honoka seeing me with a pair of women's underwear. My blood ran icy."
    BBW "Don't be too hard on yourself. Most others would have crumbled under her stare."
    BBW "Just be more careful next time. Better to not find yourself in that position at all."
    jump daymenu

label BBW015_c1_3:
    scene Nurse Office with fade
    play music Tension
    "It took all of five seconds to realize this was the wrong decision."
    "To avoid detection I had gone into the men's room, waited until it was empty, and then tried to crawl into the ventilation system."
    "Thus when I got stuck nobody was around to see me, or hear me."
    "Almost an hour passed, me half in and half out of the vent, before someone came in to pee. Another twenty minutes were gone before I pulled out."
    "I got banged up and scraped. My clothes took most of the damage, but I still had plenty of scratches to get treated."
    show AE angry at center with dissolve
    $setAffection("AE", -1)
    "And of course the student council president had heard of my little escapade. In trying to avoid running into her I had ended up alone in the nurse's office as she chewed me out."
    "As she chewed me out and I 'Uh-huh'ed every now and then I thought to myself 'I have to learn how Daichi does this.'"
    hide AE with dissolve
    stop music
    "Surprisingly, things got a little better when Alice showed up."
    play music BBW
    show BBW neutral at center with dissolve
    BBW "Were you hurt too bad?"
    MC "I'll live."
    BBW "Good."
    show BBW angry with hpunch
    play sound Thud
    BBW "Idiot! What kind of stunt was that?"
    MC "I thought it would be the easiest way to avoid detection."
    show BBW neutral
    BBW "You might as well have climbed to the roof and rappelled down to her room."
    BBW "Do you still have the package?"
    MC "It's in my backpack still."
    BBW "Very well. When you are able you can still finish the job."
    BBW "This is not an auspicious start to your career, but I suppose I cannot fault you for your enthusiasm."
    BBW "Just learn to balance it with some common sense."
    jump daymenu
    
label BBW016:
    $setProgress("BBW", "BBW017")
    scene Dorm Interior with fade
    play music Sunset
    "Classes were done, my homework was done, and even though I had wandered around the school for over an hour, I hadn't found anything to do."
    "No one to talk to, nobody that needed help with anything. I was left to myself."
    "So I came back to the dorm. Daichi was out - fortunately - so I had a nice quiet room to relax in."
    "I had broken out my laptop and was refamiliarizing myself with Titans of Eververse when my phone buzzed."
    MC "?"
    "It wasn't a call, though. It was a text."
    "I couldn't remember the last time someone had ever texted me, much less the last time I had sent one."
    BBWCell "<Hello, Keisuke. This is Alice. How are you?>"
    "I spent a few seconds staring at the message, confused. What did she want? Why was she texting me?"
    "Then I realized she might not want anything. Didn't Americans text each other all the time?"
    "But was Alice the sort to make small talk just because? She usually had something on her mind."
    "And here I had gotten comfortable and was having fun with my game."
    menu:
        "Text back you're up to nothing special.":
            jump BBW016_c1_1
        "Text back asking if she wants something.":
            jump BBW016_c1_2
        "Text back you're in the middle of something and can't talk.":
            jump BBW016_c1_3

label BBW016_c1_1:
    Cell "<I'm good. Just having a quiet afternoon to myself.>"
    "I unpaused the game - good thing I was between fights - when I heard another beep from my phone."
    MCT "That was fast."
    MCT "Or direct, I should say. Fitting."
    BBWCell "<I am currently idle as well. Kodama-san is working on a new recipe for me to try, and at my insistence she is taking her time to make sure it is perfect. Thus, I am waiting later than usual for my afternoon tea and as I have completed my homework and studies I am looking for something else to occupy my time.>"
    if getFlag("BBW_working"):
        "I wasn't sure how to feel that she was hoping I could keep her entertained, but this did imply she wasn't contacting me with a new delivery assignment."
        "Right?"
    else:
        "I wasn't sure how to feel that she was hoping I could keep her entertained."
    jump BBW016_c1_after

label BBW016_c1_2:
    Cell "<Was there something specific you wanted to talk to me about?>"
    "Her response was immediate."
    BBWCell "<No, no. This is just friendly small talk.>"
    BBWCell "<I find myself idle as I wait for Kodama-san to finish working on a new recipe.>"
    jump BBW016_c1_after

label BBW016_c1_after:
    if getFlag("BBW_working"):
        Cell "<Oh. I thought you had another delivery for me to make or something.>"
        "Again, she responded right away."
        "Looked like I wasn't going to make it to the next dungeon anytime soon..."
        BBWCell "<Again, no. Our company is still in its infancy, building a customer base and waiting for word of mouth and customer satisfaction to rise.>"
    BBWCell "<I am not interrupting anything, am I?>"
    menu:
        "Not really.":
            jump BBW016_c2_1
        "Well, actually...":
            jump BBW016_c1_3

label BBW016_c2_1:
    Cell "<Not really. I was just doing some level-grinding.>"
    "I turned my player character back around and headed back to the village."
    "When my phone beeped again I kept one hand on my mouse and used the other read her response."
    play music Schoolday
    BBWCell "<I am not familiar with that term. What does it mean?>"
    Cell "<Video game speak. I'm trying to make my character more powerful.>"
    BBWCell "<That explains my ignorance. I have never been one for frivolities such as that.>"
    Cell "<There's nothing wrong with video games.>"
    BBWCell "<Perhaps not, but there are always better uses of your time.>"
    Cell "<That's subjective. If I'm having fun, if it helps me relax, that's good enough for me.>"
    Cell "<I'm thinking of maybe joining the computer club. I hear they spend most of their time playing MMORPGs.>"
    BBWCell "<Tsk.-"
    "Yes, she actually wrote out 'Tsk' in a text."
    BBWCell "<Tsk. When there are other, more enriching art forms available to you, you choose to wallow in crude power fantasies.>"
    "I didn't want to get into an argument over the merits of video games, but when I saw a flaw in her argument I felt I had to press."
    Cell "<If you've never played video games, then you can't really criticize them, can you?>"
    "That bought me all of a couple seconds. Maybe I had stunned her."
    BBWCell "<I have seen what those games are like.>"
    BBWCell "<Either a cartoonish mascot jumping from one cliff to another, hopping onto creatures that get in his way.>"
    BBWCell "<Or an orgy of ultraviolence that allows the disturbed to play out their grotesque fantasies.>"
    "Now I was getting a little peeved."
    Cell "<I wouldn't have pegged you as a moral prude, Alice.>"
    Cell "<Not that I want to start an argument, but there are far more types of videos than just platformers and shoot 'em ups.>"
    jump BBW016_c3
    
label BBW016_c3:
    menu:
        "Like fighting games." if not getFlag("BBW016_c3_1"):
            jump BBW016_c3_1
        "Like fighting games. (disabled)" if getFlag("BBW016_c3_1"):
            pass
        "Like dating sims." if not getFlag("BBW016_c3_2"):
            jump BBW016_c3_2
        "Like dating sims. (disabled)" if getFlag("BBW016_c3_2"):
            pass
        "Like simulator games.": #(opens up BBW018)
            jump BBW016_c3_3

label BBW016_c3_1:
    $setFlag("BBW016_c3_1")
    "I started to write 'Like fighting games,' before realizing I wasn't doing myself any favors with that."
    if getFlag("BBW016_c3_2"):
        BBWCell "<Such as...?>"
        "I gritted my teeth, trying to think of an example that would blow away her contempt in one move."
    jump BBW016_c3

label BBW016_c3_2:
    $setFlag("BBW016_c3_2")
    "I started to write 'Like dating sims,' and stopped right before I sent it off."
    "If she didn't know what dating sims are, I'd have to explain it. And if she did know, I'd have to explain why that was the genre I went to."
    "I didn't relish the thought of having to defend dating sims to a female classmate."
    if getFlag("BBW016_c3_1"):
        BBWCell "<Such as...?>"
        "I gritted my teeth, trying to think of an example that would blow away her contempt in one move."
    jump BBW016_c3

label BBW016_c3_3:
    $setFlag("BBW016_testpass")
    Cell "<Like simulator games.>"
    "Another pause of a couple seconds followed."
    BBWCell "<Explain. Please.>"
    Cell "<It's right there in the name. They're games that simulate something, like farming or flying an airplane.>"
    Cell "<A lot of them are simple by design, a way to unwind by doing something repetitive.>"
    "I started typing 'I'm not really into them,' but then inspiration hit."
    "My lips curling up in a smile, I deleted what I had typed and then wrote"
    Cell "<The more complex ones have you running a city or a business.>"
    "I hit send, and waited."
    "This time it took almost ten seconds for her to respond. I had enough time to enter the inn and save my game."
    BBWCell "<There are business video games?>"
    Cell "<Yep.>"
    Cell "<Though not like regular businesses where you create a product and sell it.>"
    Cell "<The bigger titles revolve around more exciting things like amusement parks or zoos.>"
    BBWCell "<How do they work?>"
    "Cue victory fanfare."
    $renpy.music.set_pause(True)
    play sound Victory
    pause 3
    $renpy.music.set_pause(False)
    Cell "<You're put in charge of a business that's starting out or is struggling, and your job is to make it profitable.>"
    Cell "<You create rides or buy animals, set ticket prices, add concession stands or whatever.>"
    "Another pause."
    BBWCell "<Do you have any of those types of games?>"
    Cell "<I don't, but I can find one or two.>"
    Cell "<Interested in trying them?>"
    BBWCell "<I suppose I owe it to myself to sample all forms of art, so that I may make a more discerning judgement.>"
    BBWCell "<It is more impressive to appreciate the interplay of light and shadow in a Raphael than to master some violent spectacle.>"
    BBWCell "<But you were right: I cannot judge unless I have experienced it for myself.>"
    Cell "<I'll look into finding some business management simulators.>"
    BBWCell "<Money is no object. I can reimburse you.>"
    BBWCell "<It looks like Kodama-san is ready to serve the dish, so I will take my leave.>"
    "I sent a final message - Enjoy - and put my phone down."
    "I was free to return to Titans of Eververse, but the thought of getting Alice into gaming, even if it was the 'Zoo Manager' variety I'm not interested in."
    "So I went to my usual PC gaming storepage and started looking through the business management titles."
    jump daymenu

label BBW016_c1_3:
    Cell "<Well actually, I was in the middle of a dungeon crawl. Can I talk to you later?>"
    "This time she actually took a moment to respond."
    stop music
    $setAffection("BBW", -1)
    BBWCell "<Oh. Well I would not want to interrupt whatever childish game you're engaged in.>"
    BBWCell "<Your time is too precious to spend engaged in actual human interaction, I see.>"
    "And that was the last text she sent me."
    "For my part I tried to diplomatically explain I could talk later, but all I got was silence in return."
    "I had a pretty good feeling she wouldn't hide her irritation the next time we met. I just hoped she didn't carry it too long."
    jump daymenu
    
label BBW017:
    $setProgress("BBW", "BBW020")
    scene Cafeteria with fade
    "I was feeling peckish after class, so I went to the cafeteria looking for something a bit more filling than a candy bar."
    "A bowl of ice cream called out to me, but it did mean I had to stay in the cafeteria as I ate it."
    play music Tension
    "No sooner had I gotten comfortable than Alice huffed her way into the dining area."
    show BBW angry at center with dissolve
    "Her anger was almost palpable. Not in her expression so much as this aura emanating off her."
    "Not a hornet's nest I would want to smack, but the cafeteria was mostly empty and so she noticed me almost instantly."
    BBW "Hotsure-san! What do you know of this?"
    "She thrust a piece of paper at me. It was a list of some sort. I took it and read it over."
    MC "It looks like all the girls in our year."
    BBW "Ranked by preference."
    BBW "Some boy or boys have judged all the women in our class and ranked them according to order of attractiveness."
    MC "Is that what this is?"
    MCT "(That's pretty skeevy, but I can't say I'm surprised. Stuff like that happened at my old school, too.)"
    MCT "(I can see why she's upset. We're all here because of some physical abnormality, and now here's some jerk objectifying all the girls-)"
    BBW "Why am I number 13?"
    MC "Th-That's what you're angry about?"
    BBW "Of course."
    show BBW neutral
    BBW "I have no reason to fear being judged for my beauty, but I have not decided if placing me so low is malicious or ignorant."
    MC "Wait, how are you at 13? There's less than 10 girls in our class."
    BBW "By 'class' I mean 'year'."
    show BBW angry
    BBW "But that is not the worst part. Look at the top of the list."
    MC "Matsumoto... Shiori's number one?"
    BBW "Madame President herself is at the top of the rankings. I want you to explain that to me."
    MC "You think I had something to do with this? Because I didn't."
    show BBW neutral
    BBW "But you are a man, yes? You should have some insight into the thought process."
    BBW "Do you think Matsumoto-san is more attractive than me?"
    MCT "So I'm being put on the spot. Because I'm the one who was here? This is not the first time you've betrayed me, ice cream."
    menu:
        "Yes.":
            jump BBW017_c1
        "No.":
            jump BBW017_c2
        "Square the circle.":
            jump BBW017_c3

label BBW017_c1:
    MC "If you must ask... Yes."
    show BBW angry
    BBW "..."
    MC "It's all subjective, right?"
    $setAffection("BBW", -2)
    BBW "You're honest, at least."
    BBW "That will serve you well. Stupidity and deception are a terrible combination."
    hide BBW with dissolve
    "And that was her final word."
    jump daymenu

label BBW017_c2:
    if getAffection("BBW") >= getAffection("AE"):
        $setFlag("BBW017_testpass")
        MC "If you must ask... No."
        BBW "Go on..."
        MC "Go on? It's all subjective, isn't it?"
        BBW "Yes and no. Any culture has an established ideal of beauty. You're right to say I'm more attractive than Matsumoto-san, but this list indicates you're the exception."
        BBW "Why is that?"
        "I considered sweet-talking her, but something told me she wasn't going to have any of that."
        MC "Well, it might not be physical."
        MC "Personality-wise, you are kind of abrasive."
        "She didn't say anything for a moment, but I could see her thinking over what I just said."
        BBW "Let's say you're right (though I'm not admitting to being unduly proud). How does that explain Matsumoto's popularity?"
        BBW "She goes out of her way to push people away. It's as if she wants to be despised."
        MC "I think you might be overstating it, but you're not entirely wrong. She has the 'tsun' part of the tsundere type going for her."
        MC "It's a paradox. The more you can't have something, the more you want it."
        MC "And with someone like Matsumoto-san there's the fantasy that if you can pierce her icy exterior you can find the sweet center and she'll reciprocate your feelings."
        MC "You... You're seen more as a stuck-up rich girl. People aren't going to be interested in getting to know you if they think that's all there is."
        "She stayed silent a while, her irritated mood melting."
        play music Peaceful
        BBW "And do you think that's all I am? A stuck-up rich girl?"
        MC "I think there's more to you than your money. You have an interest in music, right?"
        show BBW haughty
        BBW "I am cultured, yes."
        MC "Right. Just don't be so elitist about it and you can probably find some other people with the same interest."
        show BBW neutral
        BBW "Elitist? Whatever do you mean?"
        MC "You were butting heads with the music club president after just a couple days, remember?"
        show BBW haughty
        BBW "Is it elitist to let others know when their standards are below acceptable?"
        MC "Yes! Yes, that's the very definition of 'elitist!'"
        show BBW angry
        BBW "!"
        "She looked like she was about to snap, but then quickly relaxed, exhaling slowly."
        show BBW neutral
        BBW "Boys like it when someone like Matsumoto-san orders them around, because they harbor this fantasy that they can win her over. But they don't like it when someone like me chastises them for their shortcomings."
        BBW "It's all about having this illusion of control, isn't it? Some people just can't accept not being in charge of everything."
        BBW "Boys like to play pretend, after all."
        MC "Not all guys are like that, you know."
        show BBW happy
        BBW "Oh, I know. I'm not lumping you in with the children who concocted this list."
        BBW "You are man enough to admit your own feelings, and reasonable in your tastes."
        show BBW neutral
        BBW "I'm not sure if you're mature enough to follow your own path, but we shall see..."
        show BBW happy
        BBW "Enjoy your ice cream."
        hide BBW with dissolve
        "She walked off in a much better mood than when she had shown up, but I didn't think it was so simple as her being complimented by my saying I found her more attractive than Shiori."
        "Something else was on her mind, but I didn't stop to consider what it might have been."
        "You can say she was right about me not being mature enough, if you want, but when the conversation was over my impulse was to get on with my life as if nothing had happened."
        jump daymenu
    else:
        MC "If you must ask... No."
        BBW "..."
        show BBW angry
        BBW "You're a terrible liar."
        MC "I- Wha?"
        show BBW neutral
        BBW "I've seen you and Matsumoto-san. You're rather close, the two of you."
        MC "No, we're... We're friendly, but it's not like we're dating."
        show BBW haughty
        BBW "I understand human behavior, Hotsure-san. It's a necessary trait for anyone looking to enter the jungle of free enterprise."
        BBW "You can't hide what you're feeling whenever you're chatting with the Ice Queen. Maybe she can't figure it out, maybe you're too timid to take the leap, but I know."
        show BBW angry
        BBW "So don't EVER try to sweet talk me like that again."
        MC "Okay. Okay. I guess I do find Shi- Matsumoto-san a bit more attractive than you. A bit."
        MC "But it's not like I would put you at 13 or anything that low."
        "Alice's expression softened a bit, her stony exterior melting into something a little less severe."
        show BBW neutral
        BBW "Of course you wouldn't. Nobody with sense would."
        show BBW angry
        BBW "But I still need to find whatever cretin made this list."
        show BBW neutral
        BBW "Hotsure-san."
        hide BBW with dissolve
        "And she walked off."
        jump daymenu

label BBW017_c3:
    MC "Well... it's all relative. Beauty is in the eye of the beholder and all that."
    MC "I mean, when you say 'attractive' are you talking about pure physical beauty, and do we then go off of classical standards of what a given culture considered ideal?"
    MC "For that matter, how do you compare two different objects that are both, in their own ways, beautiful? A landscape and a portrait differ in their subject matter, but they each have their own criteria for what is beautiful or not."
    show BBW angry
    MC "So while you have your own unique air and... gravitas, someone like Shiori has an equally distinct but undeniably different bearing. Who is to say which is 'right' or 'more attractive?'"
    "As I rambled I could see Alice's expression darkening. This wasn't working."
    $setAffection("BBW", -1)
    BBW "Stop. Just stop."
    MC "..."
    BBW "I don't know what's going on inside your head, but I have no tolerance for weakness."
    BBW "And however I may feel about Madame President, I don't think she's the sort to take pity on a wishy-washy... toad."
    BBW "Figure out what you want and grow the requisite spine to go after it. Playing the middle isn't going to get you anywhere."
    hide BBW with dissolve
    "And our conversation ended there."
    jump daymenu

label BBW018:
    scene Cafeteria with fade
    play music Busy
    "So Alice wanted to try a tycoon game, and since I was the one to suggest them to her it fell on me to hold her hand."
    "Not that I minded. I really had no experience with those games, but playing with someone else or just watching them could be fun in its own way."
    "And when I stopped to think about it, I was having trouble thinking of times I had seen Alice hanging out with anyone besides me. Or Kodoma-san, of course."
    "I knew she was in the music club, but from what I'd heard she wasn't exactly endearing herself to anyone there."
    "Was I her only friend at the school? Nah, it couldn't be."
    "Either way, as brusque as she could be, I didn't mind the thought of getting closer to her."
    show BBW happy at center with dissolve
    show PRG neutral at Position (xpos=0.45, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    BBW "Ah, Keisuke. Over here."
    "I found Alice and Aida sitting at her usual table, but instead of tea and cakes there was a full computer set-up. Monitor, tower, keyboard, mouse."
    "And jeez, this wasn't cheap. I wasn't up on the latest gaming hardware, but it looked like a Hayashi ZX-5000. Fresh out of the box, even."
    MC "Is this new?"
    BBW "Indeed. It arrived just this morning."
    BBW "I don't know anything about video game hardware, but the reviews for this model were uniformly good."
    MC "You bought an entirely new computer just to play games?"
    show BBW neutral
    BBW "Well, yes. If I am to give this endeavor the best opportunity I need to have the finest equipment possible, wouldn't you agree?"
    hide PRG with dissolve
    MCT "Not really. Graphics and sound aren't as important as gameplay, and we aren't going to be looking at the latest AAA titles or anything."
    MC "Did you find any games you were interested in? I know the names of some of the more popular titles, though I'm not as familiar with them."
    BBW "I just finished our reading for Literature a few minutes ago, so I haven't had much chance to find anything yet."
    BBW "You have taken care of your homework, yes? I wouldn't want to impose on your time with something as frivolous as this."
    if getSkill("Academics") >= 4:
        MC "Huh? Oh, yeah. I've taken care of everything."
        show BBW happy
        BBW "Excellent."
        jump BBW018_c1_after
    else:
        MCT "Gah! The reading."
        MCT "I haven't even started it yet."
        menu:
            "Sure, I'm all caught up.":
                $setFlag("BBW018_c1_lie")
                MC "Yeah, I'm on top of everything."
                "A blatant lie, but Alice didn't even blink."
                show BBW happy
                BBW "Excellent."
                jump BBW018_c1_after
            "Actually...":
                jump BBW018_c1_2

label BBW018_c1_2:
    MC "No, I still have some stuff to take care of."
    BBW "Hmm."
    BBW "Well, business before pleasure. By which I mean your studies come before games."
    BBW "I will wait here while you go take care of your obligations first. There is still much I can do to familiarize myself with this machine."
    MC "OK..."
    $setAffection("BBW", -1)
    "She wasn't angry as she said that, but she was clearly disappointed."
    "She sounded almost like Shiori in that moment, though I guess with Alice it was less about adhering to the rules and more about striving for excellence or whatever."
    scene black with fade
    "I went back to my dorm and hit the books, doublechecking my math homework and trying not to take any shortcuts with the reading."
    "It took almost two hours, but I finished it all and headed back to the cafeteria on the off-chance that Alice was still waiting for me."
    scene Cafeteria with fade
    show BBW neutral at Position (xpos=0.25)
    show PRG neutral at Position (xpos=0.75)
    "I expected her to have started a game already, figuring it out on her own, but nope. She was having tea, not even looking at her computer."
    show BBW happy
    BBW "Finished your work?"
    MC "Yep. All caught up now."
    BBW "Good. I would advise keeping on top going forward."
    jump BBW018_c1_after

label BBW018_c1_after:
    BBW "Have a seat."
    "I sat down next to her and she opened an online game store."
    show BBW neutral
    BBW "Now, what game would you recommend? I am a novice, but I am hoping for something engaging nonetheless."
    MC "Well, the most popular titles are..."
    $setVar("BBW018_gamesplayed", 0)
    menu:
        "Rollercoaster Tycoon":
            jump BBW018_c2_1
        "Railroad Tycoon":
            jump BBW018_c2_2
        "Professional Wrestler Tycoon":
            jump BBW018_c2_3

label BBW018_c2_menu:
    menu:
        "Rollercoaster Tycoon" if not getFlag("BBW018_rollercoaster"):
            jump BBW018_c2_1
        "Rollercoaster Tycoon (disabled)" if getFlag("BBW018_rollercoaster"):
            pass
        "Railroad Tycoon" if not getFlag("BBW018_railroad"):
            jump BBW018_c2_2
        "Railroad Tycoon (disabled)" if getFlag("BBW018_railroad"):
            pass
        "Professional Wrestler Tycoon" if not getFlag("BBW018_wrestler"):
            jump BBW018_c2_3
        "Professional Wrestler Tycoon (disabled)" if getFlag("BBW018_wrestler"):
            pass
        "Imperialis" if getVar("BBW018_gamesplayed") >= 2:
            jump BBW018_c2_4

label BBW018_c2_1:
    MC "It's kind of the standard for these types of games. You're put in charge of an amusement park and you need to make money by putting in rides and concessions, adjusting the ticket prices, stuff like that."
    BBW "Sounds straightforward enough, and running a business - even a simulacrum of one - is perfect for me."
    if not getFlag("BBW018_railroad"):
        "Even though there was an older version of the game discounted 75%% off, Alice went with the latest one."
        BBW "I want to experience the best possible version of the game."
        "Never mind that 'latest' didn't necessarily mean 'best.' But all right, Alice is new to gaming and I didn't feel up to opening that can of worms."
        "I was more bothered by the fact that even the latest version was two years old, and she was using a ZX-5000 to play it. So much processing power called up in service of so little."
        "The game started with a tutorial; how to place or destroy attractions, change ticket prices, read the interface."
        "It took almost 15 minutes, and I could see Alice losing interest. But finally it was done and she got to start her own game."
        "She played in silence for a while, getting the hang of the basics and, as far as I could tell, doing OK."
        "She was making money, expanding her operations and improving the existing ones."
    else:
        "So she bought the game, again going with the latest version, and sat through another tutorial."
        "Once she got into the game proper she seemed to do OK."
    "Her rollercoaster designs were kind of basic, but serviceable. And I think she was overcharging on the pictures you had taken on the rides."
    "Eventually, though, she started to look annoyed."
    "The monthly status report that gauge her park's finances, growth and expenses was on the screen, and something on it was irritating her."
    "She went through the drop-down menus and other screens, searching for something."
    show BBW angry
    BBW "Grrrr..."
    MC "What's up?"
    BBW "Look at that."
    "She pointed to the screen, the tip of her finger on 'Taxes.' It was a deduction taken out of her monthly earning based on how much her park was making."
    MC "What about it?"
    BBW "There's no way to contest this."
    BBW "It's completely unbelievable."
    MC "No... Businesses pay taxes."
    BBW "Not a flat rate like that."
    BBW "If this was real I would be able to make a deal with the local municipality for tax credits in exchange for the revenue my park would bring to the local economy."
    BBW "Hiring local labor to build and expand the park, the extra business people would bring to the surrounding restaurants and shops."
    BBW "I'm constructing a keystone of the local economy, and yet the city or state won't incentivize my work? It's absurd."
    MC "These games aren't supposed to be 100%% realistic."
    MC "I can see how a 'Lobby the mayor' side-mission would be kind of distracting."
    BBW "Whatever. I was losing interest in this game anyway."
    show BBW neutral
    BBW "It's too casual in how it depicts things like pricing and expanding the grounds."
    BBW "You can't even set wages for your workers, or handle advertising!"
    BBW "What other games are there?"
    $setFlag("BBW018_rollercoaster")
    $setVar("BBW018_gamesplayed", getVar("BBW018_gamesplayed") + 1)
    jump BBW018_c2_menu

label BBW018_c2_2:
    MC "Railroad Tycoon is a pretty well-known title. I've never played it, but it must have its fans."
    BBW "'Build your own railroad empire across Europe as you construct routes, upgrade your trains and handle both commercial and passenger business.'"
    BBW "So it's like operating a business, but more concerned with the ground-level operations instead of dealing with shareholders or building a brand."
    show BBW happy
    BBW "I can see how this would be fun."
    if not getFlag("BBW018_rollercoaster"):    
        "Even though there was an older version of the game discounted 75%% off, Alice went with the latest one."
        show BBW neutral
        BBW "I want to experience the best possible version of the game."
        "Never mind that 'latest' didn't necessarily mean 'best.' But all right, Alice is new to gaming and I didn't feel up to opening that can of worms."
        "I was more bothered by the fact that even the latest version was two years old, and she was using a ZX-5000 to play it. So much processing power called up in service of so little."
        "The game started with a tutorial; how to place or destroy train tracks, change ticket prices, read the interface."
        "It took almost 15 minutes, and I could see Alice losing interest. But finally it was done and she got to start her own game."
        "She played in silence for a while, getting the hang of the basics and, as far as I could tell, doing OK."
        "She was making money, expanding her operations and improving the existing ones."
    else:
        "So she bought the game, again going with the latest version, and sat through another tutorial."
        "Once she got into the game proper she seemed to do OK."
    "She was more interested in commercial fare than catering to passengers, probably because that brought in more money."
    show BBW neutral
    "After a while, a bored expression crept onto her face."
    MC "Having fun?"
    BBW "No, I cannot say that I am."
    BBW "This isn't exactly the most realistic depiction of the railroad enterprise, is it?"
    MC "No, of course not. It's just a game."
    BBW "I understand that, but to have each country charge the same tax rate? To have the same cost of building and maintaining the tracks no matter where in Europe I go?"
    BBW "And how is it I cannot undercut my competitors when I clearly have the most advanced trains and access to the most routes?"
    MC "Uh, anti-monopoly policies?"
    BBW "I should then be able to lobby the various governments and secure special exemptions."
    BBW "For that matter, why aren't government contracts an option? There's so much revenue unaccounted for!"
    show BBW angry
    BBW "Argh!"
    "She closed her eyes. Inhaled, exhaled."
    show BBW neutral
    BBW "No, I don't think this game is for me."
    BBW "What else is there?"
    $setFlag("BBW018_railroad")
    $setVar("BBW018_gamesplayed", getVar("BBW018_gamesplayed") + 1)
    jump BBW018_c2_menu

label BBW018_c2_3:
    MC "This one is a little off-beat, but it falls under the 'business simulator' banner."
    BBW "Professional Wrestler Tycoon?"
    BBW "I know even less of pro-wrestling than I do video games. Why would I play this?"
    MC "Just give a try. Who knows, maybe you'll get into it."
    "Alice shrugged and bought the game. That it was full-price didn't seem to bother her (though I made a note to myself to point out she could get a refund if she didn't care for the game)."
    "The game downloaded and the instant she opened it the cafeteria was filled with a primal roar."
    show BBW neutral with hpunch
    play sound Crash
    Computer "<RWAAAARRRR!>"
    show BBW angry
    BBW "Ah!"
    show BBW angry with hpunch
    Computer "<DO YOU HAVE WHAT IT TAKES TO BUILD THE GREATEST WRESTLING FRANCHISE THE WORLD HAS EVER KNOWN?!>"
    "I lunged forward and hit the mute button on Alice's keyboard, then looked around the cafeteria."
    "The place was mostly empty, but everyone around had heard the full volume outburst. More than a couple heads turned in our direction, their expressions irritated at best."
    "Nobody was as upset as Alice, though."
    BBW "Oh! What was that assault? Is this game trying to punish you for playing it?"
    MC "It was surprisingly aggressive."
    "I turned the volume down to a reasonable amount, which for this game turned out to be 5 out of 100."
    MC "Still, might as well see how the game plays."
    "I could tell it was futile. From the moment she started the tutorial, directed by a wrestler called 'White Jaguar,' she was put off by everything."
    BBW "..."
    "That the game had almost nothing to do with actual wrestling and was instead built around managing a wrestling federation."
    "You started with a small roster of performers divided into heavyweights, cruiserweights and tag teams, and you made choices about which ones to push, which ones feed to other stars, and which to give championship belts to."
    "The objective was to build up stars that would bring in audiences, but not have them win all the time lest the fans get bored. Having a stable of villains the audience cared about was integral too."
    "So it was more like a resource management game with the twist that you needed both good and bad elements, faces and heels."
    "It wasn't the worst idea for a game, but the mechanics meant nothing to Alice."
    "The surface aesthetics were not doing it for her, and whatever enjoyment she would find in building a business was buried under her disinterest in the spandex-clad beefcakes going through exaggerated poses whenever you selected one."
    show BBW neutral
    BBW "I'm done with this. Surely there must be less off-putting displays than this."
    $setFlag("BBW018_wrestler")
    $setVar("BBW018_gamesplayed", getVar("BBW018_gamesplayed") + 1)
    jump BBW018_c2_menu

label BBW018_c2_4:
    MC "Maybe the regular business simulators aren't for you. They kind of are straightforward."
    MC "How about something like Imperialis? A 4X game might be more your thing."
    BBW "4X?"
    MC "Explore, expand, exploit and exterminate."
    MC "The goal is to build an empire and either conquer the world or achieve some sort of technological achievement before anyone else."
    BBW "An empire? Like ancient Rome or China?"
    MC "Yeah. There actually are games that use ancient civilizations-"
    show BBW happy
    BBW "And I'd be empress?"
    "As I said 'Yes' I could see her eyes taking on a dreamy expression, like she was losing herself to some beautiful vision."
    play sound Cheer
    BBW "Let's play that one!"
    show BBW neutral
    "She bought and downloaded the second-to-latest version of Imperialis, ignoring the space-based game that had come out last year, a giddy smile on her face."
    "It didn't even fade when she had to sit through yet another tutorial, the longest one by far."
    "I probably should have told her how much micromanaging there was in these sorts of games, but she wasn't bothered at all. She drank it all in."
    "When she started the game proper she selected the Roman-esque option, and was midly put out that she couldn't change her avatar to a female. A fair criticism."
    "Other than that, she was clearly having a ball."
    "She didn't master it right away - there was just too much going on to get a feel for everything all at once - but even when she started to get outclassed by the other empires, and when she engaged in an ill-fated war against one of her neighbors, she was still beaming."
    "It took almost six hours for her to get through her first game. For a while she had the lead, until another continent was discovered and three other empires joined the picture."
    "She ended up in second place after managing to conquer a neighbor, but the game ranked her performance right at the bottom of the charts. 'Andrew Johnson.'"
    "I'd have to look him later to see just how dismal that was."
    "But Alice was unfazed, even if she knew who he was."
    show BBW happy
    BBW "I admit, Keisuke, I may have been wrong. That was a wonderful game."
    BBW "Obviously there is much room for improvement, so much to learn and master, but I am undaunted."
    BBW "If you have any tips, though, I'm open to them."
    MC "Actually, I don't really play these games."
    if getSkill("Academics") >= 4:
        MC "But I think I noticed a couple things you could have done better. You didn't have to restrict your defenses in each city like you did, for one."
        $setAffection("BBW", 1)
        BBW "Yes, I saw that. And maybe if I had stuck to one path with the technological developments..."
    else:
        MC "But it definitely was interesting. I think you're getting the knack for it."
    BBW "Would you be interested in meeting again over the weekend? I'm practically aching to start another game, but it's getting too late as it is."
    MC "Oh, wow, it's already eight o'clock."
    $setAffection("BBW", 1)
    MC "No, yeah. Let's do this again."
    MC "Do you need help taking your computer back to your room?"
    BBW "Oh, don't worry. Kodoma-san will handle that."
    "I was hesitant to leave it for Aida until I saw she had a wheeled cart waiting by the side."
    scene black with fade
    if getFlag("BBW018_c1_lie"):
        "I hurried back to my dorm to take care of my homework."
        "I wasn't too concerned about Alice realizing I had lied to her, but making a habit of it wasn't going to lead to anything good."
        "It looked like I had a long night ahead of me."
    else:
        "So I said my goodbyes and headed back to my dorm."
        MCT "Maybe I could look up some Let's Plays for Imperialis, learn a few tips for Alice."
    jump daymenu

label BBW019:
    scene Dorm Interior with fade
    "It was afternoon and I was bored. I was so bored I can't think of any way more exciting than that to put it."
    "I didn't have any immediate homework to work on, just essays and projects due later in the term."
    "And none of my usual hobbies could even hold my attention long enough to not grab it. As soon as I thought of something to do I'd think 'Nah' and forget it."
    "But it was too nice a day outside to stay cooped up in my room. I could almost hear my parents getting on my case, that if I was so bored I should go out and find some entertainment of my own."
    
    scene Town with fade
    "I was kind of tired of the school grounds, so I walked to the nearby town. Still nothing caught my eye. It became more a question of, what was the least unexciting thing?"
    menu:
        "The arcade":
            jump BBW019_arcade
        "A cafe":
            jump BBW019_cafe
        "The movie theater":
            jump BBW019_theater

label BBW019_arcade:
    scene Arcade with fade
    play music Busy
    "The arcade was probably the best shot at ending my boredom. With all those bright lights and electronic chimes I at least couldn't zone out."
    "I got some change and walked around the floor once, seeing if maybe something caught my eye. When that failed, I went for one of the racing games."
    "Oddly, driving around in circles turned out to not be the key to shaking off my lethargy. I won a couple races, the changing scenery of each track more interesting than the races themselves, but after the difficulty stepped up I quickly lost."
    "I left to look for another game, and a pattern had been established. I would start a game, play a little, lose because my heart wasn't in it and move on."
    "After a few rounds of this I started thinking of going somewhere else, but then I ran into a familiar face."
    show BBW neutral at center with dissolve
    BBW "Oh, Keisuke. Good afternoon."
    MC "Afternoon. I didn't take you for a gamer, Alice."
    BBW "I'm not, really. I came to town to run some errands, and Kodoma-san noticed a plush doll in one of those crane games."
    BBW "So I am waiting as she tries to win it."
    BBW "I cannot say I approve of how she is spending her money, but it is hers to spend."
    BBW "Do you spend much time at these sorts of places? Is she even likely to win, or is this a fool's errand?"
    MC "I actually don't come here all that often, but as I understand it those types of games aren't too easy to win."
    MC "Some people are skilled, though. Or maybe there's a trick."
    if getAffection("BBW") >= 4 and getFlag("BBW_working"):
        MC "Hey, you don't have any delivery jobs for me, do you?"
        $setAffection("BBW", 1)
        show BBW happy
        BBW "Not at the moment. Why so eager, though?"
    MC "I'm just here because I'm bored. Don't have any homework to worry about, got nothing else going on."
    show BBW neutral
    BBW "Hmm..."
    BBW "So with your free time you decided to while away an afternoon playing video games?"
    if getSkill("Athletics") >= 5:
        MC "You make it sound worse than it is."
        MC "I've done my homework, I did a good workout the other day, I've got no other obligations to take care of."
        MC "What's wrong with spending an afternoon playing games and having frivolous fun?"
        "Her expression, slightly judgmental, softened."
        BBW "You do have a point."
        BBW "I personally have little interest in games, particularly ones where you have to keep pumping money in just to play, but it is your time, your money."
        BBW "As long as your priorities are in order an afternoon or evening of, as you say, frivolous fun is defensible."
        BBW "Enjoy yourself, Keisuke."
        hide BBW with dissolve
        "And she wandered off, probably to find Aida."
        "For my part I spent another hour-plus playing different games, never truly getting into them but having enough fun I didn't feel the afternoon was a waste."
        jump daymenu
    else:
        MC "More like I just found myself here. Looking for something to do."
        BBW "'Looking' for something to do."
        BBW "*sigh*"
        BBW "You make it sound as if your only goal is to kill time, to speed through the prime of your life distracted and complacent."
        MC "What do you mean?"
        BBW "Your passive tone, my dear boy. You say you are looking for something to do, rather than going out and doing it."
        BBW "Life either happens to you or you make it happen, but it never comes to you. Understand?"
        MC "Ye-... No."
        "She closed her eyes and breathed in and out slowly."
        BBW "If there is something you want, be it mastering a skill or acquiring an object or achieving something, you must work for it. You have to make it happen."
        BBW "You can't sit back and just wait for it to drop in your lap."
        BBW "For instance, do you get any exercise outside of gym? Staying motionless in front of these flashing screens isn't good for your health in the long run."
        MC "I... Get in workouts now and then."
        "She closed her eyes again and shook her head."
        BBW "You don't sound too confident, Keisuke."
        BBW "Remember, habits you develop now can last a lifetime. If you don't take care of yourself today you can't just make up for it when you're 40 or 50."
        MC "I'm not that lazy."
        "She gave me a look that was one part 'Uh huh' and one part 'Really?'"
        "Then we heard Aida squealing with joy. Apparently she had gotten her plushie."
        BBW "Sounds like our business is done here."
        BBW "Keisuke, have a good afternoon. I hope you put it to good use."
        hide BBW with dissolve
        "She headed to the exit, and I was left to decide if I wanted to play some more games or do something a little more active."
        menu:
            "Keep playing games.":
                "Going back to the school, changing my clothes and hitting the gym sounded like too much work."
                "I found a fighting game to dump a few yen into, doing OK at first but never making it to the boss."
                "I was entertained, at least."
                jump daymenu
            "Hit the gym.":
                scene Gym with fade
                "I went back to my dorm and changed into some workout clothes. Faded shorts, an old shirt."
                "The gym wasn't too crowded, so I had my pick of the machines. Just like the arcade nothing really appealed to me, but going around the weight machines and jogging for half an hour on the treadmill was a better use of my time, I will admit."
                "I saw Akira at one of the other machines, pulling a monstrous amount of weight with her legs. But that area was seeing heavy use and crowds, so I didn't want to bother her."
                $setSkill("Athletics", 1)
                "When I left I felt mildly better. Not as listless, at any rate."
                jump daymenu

label BBW019_cafe:
    scene Cafe with fade
    play music Rain
    "I bought a coffee and a muffin and took a seat by the window, watching the townsfolk walking by."
    "I wondered how much they knew about the school. Surely they had to know about why it existed, but did they keep abreast of the school's operations, or did they avoid even thinking about it?"
    "I wasn't there long before in came Alice and Aida. The latter meekly waved when she saw me, but Alice was bolder, walking up to my table."
    show BBW happy at center with dissolve
    BBW "Keisuke. Are you meeting someone here? A date, perhaps?"
    MC "Wha-? N-no! No, I'm just having a coffee."
    BBW "Relax. I'm just saying 'Hi.'"
    show BBW neutral
    BBW "Aida and I were running errands and we stopped in for refreshments."
    BBW "But are you really just having coffee by yourself on an afternoon like this?"
    if getAffection("BBW") >= 4 and getFlag("BBW_working"):
        MC "Why? You don't have any delivery jobs for me, do you?"
        show BBW happy
        $setAffection("BBW", 1)
        BBW "Not at the moment. You sound eager for work though. Good to hear."
    MC "Well, I don't have anything else going on today. I came to town and found myself here. Drinking my coffee, watching the people go by, having a leisurely afternoon."
    show BBW neutral
    BBW "You don't even have a book with you? Nothing goes better with a cup of coffee than a good book."
    if getSkill("Academics") >= 5:
        MC "Didn't think to bring one with me. I've done plenty of studying lately, I can use a day without sticking my nose in a book."
        show BBW happy
        BBW "I can understand that."
        BBW "Sometimes you need to take a day off and give your brain a chance to rest up."
        if getFlag("BBW_working"):
            BBW "I won't interrupt your day off. But keep your phone handy. If a new order comes in I'll be messaging you."
        else:
            BBW "I won't interrupt your day off."
        hide BBW with dissolve
        "She went back to the counter, where Aida had already placed their order. When they got their drinks they walked out, and I was by myself again."
        "I took my time enjoying the coffee, even though it wasn't particularly great. After I was done I strolled around the town some more, then went back to the school to grab dinner from the cafeteria."
        "An unexciting day, but a restful one."
        jump daymenu
    else:
        MC "No. Wouldn't care to."
        MC "Honestly, the reading we've had to do for class has been kicking my butt. I needed a break."
        "I could see in her expression I had said something wrong."
        BBW "I see."
        BBW "I don't think the courseload has been overly burdensome, but this may be subjective."
        BBW "Though I would think that if you are having trouble right now, so early in the term, that you would want to spend more time studying and developing better habits, not less."
        MC "Everyone deserves some time off now and then."
        "I sounded more defensive than I had intended. Alice's expression didn't change that much, but something in her eyes told me I had lost some standing in her mind."
        BBW "Hmm, yes. Leisure time is important, but I find it can be too easy to mistake the necessity of downtime for an entitlement."
        BBW "An important part of success is making sure you earn your downtime by driving yourself in your work."
        BBW "You don't stop running halfway through a race, you reach the finish line first."
        MC "Yeah, but if you get a cramp or something-"
        BBW "It means you should have done more work conditioning yourself beforehand. Preparation is another component of success."
        "She looked back to the counter, where Aida was holding two drinks and hanging back."
        BBW "But how you spend your time is up to you, Hotsure-san."
        hide BBW with dissolve
        "And she went back to Aida, and the two left the cafe."
        menu:
            "Stay at the cafe.":
                "I couldn't find fault in Alice's argument, but that didn't mean a fire had been lit under my seat."
                "I was already off campus, enjoying a change in scenery and general break from the school."
                "I could start studying regularly tomorrow."
                jump daymenu
            "Go back to the dorms and study.":
                MC "*sigh*"
                MC "She's right, of course. I didn't need her to point it out, but sometimes reinforcement of what you know helps make it clearer."
                MC "Or at least harder to ignore."
                "I finished my coffee and trudged back to the school, back to my dorm."
                scene Dorm Interior with fade
                "I had to push myself to ignore possible distractions like the internet or rereading my manga or (and this should tell you how susceptible I was) cleaning my half of the room."
                $setSkill("Academics", 1)
                "But I managed. I spent a couple hours going over the past week's history and literature lessons, refreshing what I already knew and getting a better handle on what had been giving me trouble."
                "Not what I would call an exciting afternoon, but a productive one."
                jump daymenu
                
label BBW019_theater:
    scene Theater with fade
    play music Sunset
    "I found myself walking by the town's movie theater, looking over the posters."
    "There were a couple blockbuster-type movies showing, but also a historical drama, a romantic comedy and an indie melodrama."
    "I had enough money in my wallet that I could buy a movie ticket, and I could think of worse ways to while away a couple hours."
    "After I had decided to catch a flick, but before I had decided what to see, I heard someone call my name."
    UNKNOWN "Keisuke!"
    show BBW happy at center with dissolve
    MC "Alice. Good afternoon."
    BBW "Good afternoon."
    show PRG neutral at Position (xpos=0.75, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    MC "And Aida."
    PRG "H-Hello."
    hide PRG with dissolve
    BBW "Taking in a show?"
    MC "I was thinking about it."
    if getAffection("BBW") >= 4 and getFlag("BBW_working"):
        MC "Why? You don't have any delivery jobs for me, do you?"
        $setAffection("BBW", 1)
        BBW "Not at the moment. Why so eager, though?"
        MC "No particular reason."
    MC "None of these speak to me, but I've got nothing else going on right now."
    if getSkill("Art") >= 5:
        MC "I might check out this one. The Chrysanthemum Shadow."
        BBW "Ah. A fan of historical dramas?"
        MC "Not exactly, but it's supposed to have gotten good reviews. And the director's well-regarded."
        BBW "I've heard of Hagiwara, but I'm unfamiliar with his work."
        BBW "It's too bad I have other errands to attend to. This looks to be a promising film."
        BBW "Let me know how it is. I might go see it later."
        hide BBW with dissolve
        "She and Aida walked off, and I went to buy a ticket."
        scene Black with fade
        pause 2
        scene Town with fade
        "The movie wasn't bad. A bit dry in the second half, and the battle scenes seemed almost perfunctory, but overall it was a solid flick."
        MCT "Need to remember to tell Alice about this one later."
        jump daymenu
    else:
        MC "I was thinking of seeing Iron Fan 5. The last couple ones weren't that great, but the original director is back so maybe this one is good?"
        "Alice looked the over the poster, with its white-suited gangsters, stern-faced police and bloodied asphalt in 'artistic' red, white and black."
        show BBW neutral
        "It wasn't hard to see she wasn't impressed."
        BBW "I wouldn't know how the movie is. I don't have much taste for crime stories."
        BBW "Particularly not ones as... lurid as this series' reputation suggests."
        MC "Nah, it's just silly, over-the-top violence. It's not even trying to be realistic."
        show BBW haughty
        BBW "That's not much of a distinction."
        show BBW neutral
        BBW "But it is your money, after all. Far be it from me to tell you how to spend it."
        "She turned and started to walk away, but then something caught her eye."
        BBW "Oh! The Chrysanthemum Shadow. I've heard good things about this."
        BBW "And Hagiwara-san is rather acclaimed, is he not?"
        MC "Who?"
        "She gave a brief but stinging look, then quietly suppressed a sigh."
        BBW "Never mind. Enjoy your popcorn flick."
        hide BBW with dissolve
        "As she walked off the quasi-dismissive tone in her voice gave me second thoughts."
        "I had only come here to find a way to kill the afternoon, but now I was thinking that Iron Fan might be a little too trashy."
        menu:
            "Iron Fan 5":
                scene Black with fade
                "I decided to see Iron Fan."
                scene Town with fade
                "Yes, it was trashy. Yes, it just repeated a lot of stuff from the earlier movies."
                "But it let me shut my brain off for a couple hours, so it wasn't all bad."
                "Maybe not the best use of my free time, but I made my choice."
                jump daymenu
            "The Chrysanthemum Shadow":
                scene Black with fade
                "I decided to see Chrysanthemum Shadow."
                scene Town with fade
                $setSkill("Art", 1)
                "It was actually pretty good."
                "The subject matter was a bit dry - too much talk about what might happen if the characters do this or don’t do that - but I found the camerawork interesting. The director has an eye for balancing epic sweep with personal experience."
                "Yeah. A good movie."
                jump daymenu

label BBW020:
    $setProgress("BBW", "BBW021")
    play music BBW
    scene Cafeteria with fade
    "I had gotten to the cafeteria earlier than most of the other students, but after the rush had come and gone I was still there."
    "See, I'd brought a book with me to read while I ate, and it turned out to be more engrossing than I expected. 'I'll just finish this chapter,' I told myself, even after my plate was clean."
    "When I found a good place to stop I looked up to find most of the cafeteria empty. Just a few stragglers or members of sports teams coming off practice."
    UNKNOWN "Hotsure-san."
    "I was initially annoyed to have the quiet of the place broken, but when I realized who it was I relaxed a little."
    show BBW happy at center with dissolve
    BBW "Enjoying your dinner? Or it looks like you've already finished."
    MC "Yeah. I was just reading."
    BBW "That's good. Feed the mind as well as the body."
    "As Aida arrived, pushing a cart with a covered tray on top, Alice took the seat opposite me. She let Aida set her place for her, eager to see what she would be having."
    BBW "Stir-fried vegetables and beef, with mushroom soup. It looks delicious, Kodama-san."
    show PRG happy at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Th-Thank you."
    BBW "We should see about going into town this weekend, pick up some seasonal fruits. Summer will be here soon, and I do so enjoy watermelon and strawberries."
    "She was surprisingly happy, considering the recent issue with that list."
    MC "You're in a good mood. Did something happen?"
    BBW "My probation with the music club has come to an end."
    show BBW neutral
    BBW "I am still not satisfied with the club's guiding hand, but I recognize that further instigation will only take me further from my desires."
    BBW "So I will hold my tongue and restrict myself to the role given to me."
    BBW "It is to the club's detriment, but sometimes a flawed leader needs to be given the rope to hang themselves."
    MC "That's a bit heavy."
    MCT "Wrong choice of words, man."
    "But Alice didn't seem to care, she was already enjoying her meal."
    MC "Is that why you're having a late dinner? Club meeting?"
    show BBW happy
    BBW "That, and I found resolution to the... matter we were talking about the other day."
    MC "The list? Did you find out who it was?"
    show BBW neutral
    BBW "Found and confronted them."
    MC "What... What did you do?"
    "She shrugged, as if the entire matter was behind her."
    BBW "I didn't have to do much of anything. The child behind the list is even more pathetic than I expected."
    BBW "So pathetic I didn't have it in me to bring my full wrath down on him."
    BBW "I will simply say that his presence at this school is possibly more tragic than anyone else's. To tear him down more than he must already be would be cruel."
    show BBW angry
    BBW "However, he does understand - in no uncertain terms - that if he continues with this behavior I will identify him to every other woman on the list."
    BBW "Let those less forgiving than me punish him."
    MCT "Yikes. It says something she thinks threatening to out someone is 'forgiving.'"
    MCT "Can't blame her for being angry, though."
    MC "Did he explain why he ranked you so low, or did you not ask?"
    show BBW neutral
    BBW "He said I am too 'plump' for his tastes."
    BBW "He specifically cited my belly fat, after I asked him about Matsumoto-san's 'plump' rear."
    BBW "I understand that certain body parts are more appealing to men than others, but this did confirm my assumption that this was a purely superficial exercise."
    BBW "Were I in Matsumoto-san's place I would be deeply offended if I was seen as a rear with a woman attached."
    MC "I'm not surprised it was about looks, but he didn't say anything about her 'strong' bearing?"
    BBW "By 'strong' do you mean 'stiff?'"
    BBW "No, he didn't say anything about personality. I got no sense he has looked past any of our bodies."
    MC "So he just doesn't like 'plump' women."
    menu:
        "His loss. Beauty can come in all sizes.":
            jump BBW020_c1
        "To each his own, I guess.":
            jump BBW020_c2

label BBW020_c1:
    $setFlag("BBW020_c1")
    MC "His loss. Beauty can come in all sizes."
    "Alice smiled wryly, almost rolling her eyes."
    BBW "That's a bit platitudinal for my tastes, Hotsure-san."
    BBW "And while I appreciate the gesture, I do not need the affirmation."
    MC "I'm just saying there is no single definition of attractiveness. Different people look good in different ways."
    BBW "That is all subjective. 'Beauty' is a label given by the observer, not claimed by the subject."
    BBW "Some men may find a stout woman pleasing to the eye and the touch, but it is a niche taste."
    MC "So you're worried about your weight. You think you won't look good anymore if you get fatter?"
    show BBW angry
    BBW "!"
    show BBW neutral
    BBW "(Sigh)"
    BBW "I have already accepted my condition, and I'm prepared to deal with it if it becomes a genuine issue."
    BBW "Whatever fears may have been planted by my diagnosis will not be acknowledged. We don't deal with what might be wrong, but what can go wrong or is going wrong."
    BBW "I am not worried about my weight."
    "I didn't really believe her."
    "Maybe she wasn't concerned about her weight in a vacuous 'Oh no, I gained a couple pounds' sense, but there was something bothering her."
    BBW "Question."
    MC "Yes?"
    BBW "You said 'anymore.' That I 'won't look good anymore' if I get fat."
    MC "Yeah... You are pretty."
    show BBW haughty
    BBW "I know I am."
    MCT "That was fast."
    show BBW neutral
    BBW "But would I still be pretty if I was fat?"
    MC "You want to know if I like fat women?"
    BBW "I just want to know what your agenda is."
    show BBW haughty
    BBW "Obviously our current relationship as employer/employee would make dating problematic, but I am curious."
    "There was something confrontational about how she asked this. But also something... vulnerable? Like she was a little too eager."
    "I don't know why I felt like I had to hide anything here. Maybe it was just how Alice was so bold that I had to go in the opposite direction."
    MC "You said you are not bothered by your weight. So I take it that you're not looking for a compliment."
    show BBW neutral
    BBW "It's not about me. It's all about you, and your preferences."
    MC "Yes."
    MC "So speaking of what I like in general terms, with no comments about certain individuals, I will say that..."
    MC "I do, in fact, find something... enticing about larger women."
    BBW "Go on..."
    MC "Soft things are inviting. Pillows, sofas, plush jackets. They feel nice, they're relaxing."
    show BBW happy
    BBW "You want to lie down on a fat woman?"
    "I coughed, my mind going straight to the lewdest possible vision, and the way Alice chuckled after a beat I could tell she had surprised herself."
    BBW "That tells me more than you just said, actually."
    "It was more than I wanted to say, definitely."
    "But it was also more than I expected. I've never thought about being with a... a fat woman, but thinking about it now I could see the attraction."
    "I quickly got things back on track."
    MC "There are beautiful women who are larger than normal, to answer your original question."
    MC "As for physical desire..."
    show BBW neutral
    BBW "You do not need to paint any pictures."
    show BBW happy
    BBW "I could simply invoke the stereotype that men are never discerning about where they... Ahem ..."
    MC "Hang the bird feeder in the garden?"
    show BBW neutral
    BBW "... What?"
    MC "I don't know. I couldn't think of a euphemism that didn't sound dirty."
    show BBW happy
    BBW "I think they're supposed to. Just not too dirty."
    "She ate the last bit of stir fry, daintily wiped her mouth, and pushed her chair back from the table."
    BBW "That was an excellent meal, and the conversation was... interesting."
    BBW "Hotsure-san, I'll leave you to your book."
    BBW "See you in class tomorrow."
    MC "Yeah. See you."
    hide BBW with dissolve
    "Even after she was gone and Aida had cleaned up the dishes and silverware, my thoughts kept coming back to Alice."
    "I had been invited to consider her body, so it's not like I was a pervert or anything. But now that the idea of being with a large woman was in my mind, I didn't find myself trying to get it out."
    jump daymenu

label BBW020_c2:
    MC "To each his own, I guess."
    "Alice chewed a mouthful of stir fry, thinking."
    show BBW neutral
    BBW "Overweight women aren't that common in Japan, in my experience."
    BBW "America is different. Too much bad junk food, restaurants giving bigger and bigger portions for better value."
    BBW "It's not that being overweight is seen as attractive, but it is unremarkable to see a heavyset man or woman in a relationship."
    MC "I suppose. I've never been outside the country."
    BBW "..."
    stop music
    "Something was on her mind, and I thought I knew what it was, but I didn't want to press things."
    "After the business with the list she must have been sensitive about her appearance, and I wasn't the one who could build her up without sounding like a bad self-help guru."
    "The longer the silence went on the more pressure I felt. Alice was eating, so she had an excuse not to say anything. And besides, it just felt like she was waiting for me to break through whatever wall was being set up."
    MC "Well... I should probably get back to my room. I've still got that history reading to do."
    "Alice nodded, not looking up at me, and I felt tense every step of the way out of the cafeteria."
    scene black with fade
    "Something was supposed to have happened there. I could feel it."
    "And I'd blown it."
    jump daymenu

label BBW021:
    scene Pool with fade
    "I had a creative writing assignment I needed to work on, and I just couldn't think of any ideas. Thus I found myself at the pool."
    "I had read somewhere that physical activity could get the mind working, get those creative juices flowing, so I thought I'd do a little exercising."
    "I came out of the men's locker room to find the pool rather empty."
    "I'd complain it was a waste to let such fancy facilities go unused, but it's not like I was coming here regularly. Who was I to talk?"
    "Among the students in or around the water two caught my eye."
    show BBW swimneutral at center with dissolve
    "Alice was climbing out of the pool, Aida ready to hand her a towel."
    MC "Hey, Alice."
    BBW "Keisuke."
    "She began drying herself off, and I knew I should just go and get started myself."
    "But at the same time our conversation about 'is big beautiful' had been on my mind since the other day."
    "I had been sneaking glances at Alice now and then, really taking in her figure."
    show BBW swimneutral at Position(xpos=0.5, ypos=0.0, yanchor=0.3), Transform(zoom=2.0)
    "And I'd come to the decision that there wasn't anything wrong with some extra curves."
    show BBW swimneutral at center, Transform(zoom=1.0)
    "Especially now, with the bathing suit clinging to her body, her hair wet (yet still keeping its spirals somehow). Stuff like that could make most any woman appealing."
    if getFlag("BBW020_c1"):
        jump BBW021_flagpass
    else:
        jump BBW021_fail2
        
label BBW021_flagpass:
    "But I hadn't really come out and said that, had I? What I thought about big women was left hanging."
    "This might be a good chance to be clear... Except bringing it up when she's in a bathing suit might make me seem perverted."
    menu:
        "Say something.":
            jump BBW021_beforechoice
        "Wait for a better opportunity.":
            jump BBW021_fail1
            

label BBW021_beforechoice:
    MC "Hey, you know the conversation we were having before?"
    BBW "?"
    BBW "Was this about the hours you could work making deliveries?"
    MC "No. It was about the list you found, and you had asked me how I felt about 'bigger' women?"
    MCT "Why did I say 'bigger' like it was a euphemism?"
    BBW "Oh, yes. That."
    MC "I just wanted to be clear. I do think bigger women are attractive, and not just in an 'I'll sleep with whoever' way."
    "Standing off to the side, Aida was turning bright red. I angled away from her and acted as if she wasn't there. This was potentially embarrassing for me as it was."
    MC "It's not like I have a type. Maybe more like a spectrum."
    $setAffection("BBW", 1)
    "She nodded agreeably."
    show BBW swimhappy
    BBW "Most people do, I think. Though with such a focus on superficial trappings in our society many may not recognize it."
    if getAffection("BBW") <= 7:
        MC "True. But hey, that's one of the things we're supposed to get out of this school, right? Not being so focused on the superficial."
        show BBW swimneutral
        BBW "That's not quite what I was thinking. You are correct, but I was going for the fact that there's nothing wrong with having a type."
        BBW "So long as you do not develop myopia, blind to the other options around you."
        MC "Oh, right."
        MC "But like I said, bigger women are attractive. Not automatically more than skinny women, but not less so, definitely."
        show BBW swimhappy
        BBW "I'm glad you got the chance to clear that up, Keisuke."
        BBW "I know you're not trying to soothe my wounded pride..."
        BBW "... but if you're explaining this as part of some larger scheme, I'm afraid I have to cut you off."
        BBW "The music club is meeting soon and I have to change."
        BBW "We can resume this conversation later. If there is anything more you want to say."
        hide BBW with dissolve
        "She said that last part as if there was deeper meaning to it. And no, she wasn't exactly wrong that there was more I would like to say."
        "But I was glad, all the same, that we had to cut this short, because I didn't think I would have been able to seize the moment right now."
        "Still, I felt energized as I dove into the pool and started doing my laps. Today was turning out to be a good day."
        $setProgress("BBW", "BBW022")
        jump daymenu
    else:
        BBW "And you did say I was pretty, of course."
        MC "W-Well, yes."
        "She looked at me like a cat with a bowl of cream just set down in front of it. I wasn't sure I knew what she was thinking until she spoke."
        show BBW swimaroused
        BBW "Keisuke..."
        MC "Yes?"
        BBW "What I am about to suggest violates every ethical rule about the relationship between an employer and her employee..."
        BBW "But that makes it even more appealing."
        MC "Um... Are you...?"
        BBW "How would you like to go out some time? Just you and me?"
        "I didn't think I had any right to be surprised she would be so forthright, and yet..."
        "It did feel like it had come out of nowhere. I guess Alice isn't the sort to play around."
        menu:
            "I'd love to.":
                $setFlag("BBW_dating")
                MC "Sure. I'd love to, as long as it wouldn't make things weird over on the 'business' end."
                show BBW swimhappy
                BBW "I don't think it has to. I am mature enough to separate my private life from my business ventures, and I trust that you can learn to do the same."
                MC "Um, OK."
                MCT "I was being a little tongue-in-cheek there..."
                MC "What do you have in mind? Dinner? A movie?"
                BBW "I will leave that up to you."
                BBW "I know that our options are limited here at the school, but I am interested in seeing how you express your romantic side."
                MC "Leave it to me, then."
                "She smiled warmly, and despite how fast everything was going I felt more elated by the thought of success than worried about failure."
                show BBW swimneutral
                BBW "I'm sorry, but I have to run. The music club is meeting soon."
                BBW "A demain."
                hide BBW with dissolve
                "She waved goodbye and went back to the women's locker room."
                "I almost went back to change myself, until I remembered why I had come there in the first place."
                $setProgress("BBW", "BBW026")
                jump daymenu
            "That's moving a bit fast.":
                $setFlag("BBW021_c2")
                MC "Sorry, but I think that's a bit fast."
                show BBW swimsad
                $setAffection("BBW", -1)
                BBW "Oh."
                MC "It's not that-"
                show BBW swimneutral
                BBW "No, I understand."
                BBW "This is a trying time in our lives, there are bigger things on our minds."
                MC "I'm not saying 'No' outright. Just... maybe later?"
                show BBW swimneutral at Position(xpos=0.8), Transform(xzoom=-1) with dissolve
                BBW "Hmm. Yes, perhaps."
                BBW "I have to go. The music club is meeting soon."
                BBW "I'll see you in class tomorrow."
                MC "Yeah. See you."
                hide BBW with dissolve
                "She went back to the women's locker room."
                "Not storming off, though. It was a plus that she didn't seem legitimately angry."
                "I'd have to be careful, but I thought I could keep things at least civil between us, if not friendly."
                $setProgress("BBW", "BBW022")
                jump daymenu
            "I... don't think that would work.":
                $setFlag("BBW021_c3")
                MC "I... don't think that would work out."
                MC "It's a bit fast. I mean, we're in unfamiliar territory with this school and everything else, and like you said I'm working for you-"
                show BBW swimangry with hpunch
                $setAffection("BBW", -5)
                BBW "I understand!"
                BBW "..."
                pause 1
                show BBW swimsad
                BBW "I do tend to be direct, don't I?"
                MC "That's not always a bad thing, but sometimes it can be overbearing."
                BBW "Yes, I know."
                show BBW swimneutral
                BBW "Forget I said anything, Hotsure-san."
                MC "No, it's-"
                show BBW swimneutral at Position(xpos=0.8), Transform(xzoom=-1) with dissolve
                BBW "I need to go. The music club is meeting soon and I have to get dressed."
                hide BBW with dissolve
                "She didn't storm off angrily, but it was obvious to anyone watching that she was hurrying to get out of there."
                "I watched her leave, then went into the pool and began to mechanically swim several laps."
                "Instead of thinking about the writing assignment, I was now trying to figure out how to patch things up with Alice."
                jump daymenu

label BBW021_fail1:
    MC "Well, I'm going to get some laps in. I'll see you two later."
    show BBW swimneutral
    BBW "Work hard, Keisuke, but don't overdo it."
    hide BBW with dissolve
    "I tried to banish the impression of squandering the opportunity by assuring myself I would be on the lookout for a more appropriate time and place."
    "Not that this the end of the world or anything. I just wanted to say that I found women like Alice potentially attractive."
    "It's not as if I'm trying to woo her or anything."
    "Right?"
    $setProgress("BBW", "BBW022")
    jump daymenu

label BBW021_fail2:
    MC "You know..."
    "She turned to look at me, and I felt a little tongue-tied."
    MCT "Just say she looks nice even at her size, don't make it sound perverted, and then move on."
    MC "I just wanted to say, after that whole 'list' thing and the guy saying he doesn't like plump women..."
    MC "Not all guys are turned off by a few extra pounds. Some even prefer it."
    show BBW swimneutral
    BBW "Indeed."
    BBW "I know you wouldn't just be saying that to soothe my wounded pride."
    MC "No. It's the truth."
    MC "I've seen larger women I found attractive. Never dated one, but that was because of circumstances."
    BBW "It's all right, Keisuke. You don't have to try so hard."
    show BBW swimneutral at Position(xpos=0.65), Transform(xzoom=-1) with dissolve
    MC "I just want you to know... That guy doesn't speak for all men."
    BBW "I know."
    BBW "I just think that it is on each man to speak for himself."
    show BBW swimneutral at Position(xpos=0.8), Transform(xzoom=-1) with dissolve
    BBW "To say something more than just 'He doesn't speak for me.'"
    BBW "Now I have to run. The music club is meeting soon."
    BBW "So if there is anything else you would like to say to me about this, we can talk later."
    hide BBW with dissolve
    "And she went back to the locker room to change."
    "The way she sounded at the end, I had no doubt she wanted me to say more. And I know what she wanted me to say."
    "Maybe next time I could stop skirting around the issue. You never got anywhere by going halfway."
    $setProgress("BBW", "BBW022")
    jump daymenu

label BBW022:
    $setProgress("BBW", "BBW023")
    scene Dorm Interior with fade
    "I was back in my room relaxing after another day of studies when my phone buzzed."
    "It was Alice."
    BBWCell "<Can you come to my room? I need help with something.>"
    "I wasn't doing anything important right now, but I was leery that she was up to something of questionable permissibility."
    menu:
        "Text back 'Absolutely.'":
            "I texted back an emphatic 'Yes' and headed over."
        "Text back 'I can, but I can't spend the whole afternoon.'":
            $setAffection("BBW", 1)
            "I wrote back saying I still had homework and studying to take care of, but I could swing by and lend a hand."
        "Ehhhh, I don't want to deal with Alice right now.":
            jump BBW022_c1_3
    scene Dorm PRG with fade
    "Aida answered the door."
    show PRG neutral at center with dissolve
    PRG "H-Hello... Thank you for coming. Nikumaru-san needs help-"
    if getAffection("BBW") >= 8:
        BBW "Is that Keisuke?"
    else:
        BBW "Is that Hotsure-san?"
    MC "It's me. You needed help with something?"
    "Aida stepped back to let me into the room. This was first time I was seeing their living space."
    "Aida kept hers almost impossibly clean and neat. It looked like something you would see on a magazine cover."
    "It was hard to believe anyone actually lived here."
    MC "Whoa."
    "But then I saw Alice's half of the room."
    scene Dorm BBW with fade
    MC "None of this came from the school, did it?"
    show BBW happy at center with dissolve
    BBW "No. It's just a few odds and ends I brought from home."
    BBW "I like to be comfortable."
    MCT "This isn't comfort, this is a five-star hotel."
    MC "Why does your half of the room look bigger?"
    BBW "I know how to use space efficiently."
    BBW "Which brings us to why I called you here."
    BBW "I've gotten a bit tired of how my half of the room is decorated. It's time for a change."
    MC "It hasn't even been two months."
    show BBW neutral
    BBW "Yes. And?"
    BBW "I'm not a flighty fashionista, changing styles whenever something new comes along, but I do like to keep things fresh."
    MC "A stale environment leads to a stale mind?"
    BBW "'Familiarity breeds contempt,' is how I would put it. But the conclusion is the same."
    MC "Hey, it's your space. But I don't know much about interior decorating."
    show BBW happy
    BBW "Don't worry yourself about that. I've already planned out how I want to rejuvenate the space."
    show BBW neutral at Position(xpos=0.2)
    show PRG neutral at Position(xpos=0.15) behind BBW
    BBW "I need your help moving the furniture around. Kodoma-san and I aren't strong enough to move the bed."
    MC "Oh. Well, all right."
    MC "Let me limber up here..."
    "I did a few stretches to get warmed up."
    MC "What are we moving first?"
    show BBW happy
    BBW "The bed is the centerpiece, so I want to adjust that first. Everything else will follow from there."
    if getSkill("Athletics") < 3:
        "I went to the head of the bed and bent my knees, while Alice and Aida went to the other side."
        MC "On three."
        MC "1... 2... 3-"
        "The plan was to rise and lift the bed in one fluid motion, but when the legs of the bed left the floor and I was now supporting its weight I felt a fire erupt in my back."
        MC "Ah!"
        "I let go of the bed, causing the ladies to drop their end, both crying out as well. Just not in pain."
        if getAffection("BBW") >= 8:
            show BBW sad
            BBW "Keisuke?"
        else:
            show BBW neutral
            BBW "Hotsure-san?"
        show PRG sad
        PRG "Ho-Hotsure-san?"
        scene black with fade
        "I hadn't thrown my back out, but I had pulled a muscle."
        "I couldn't move for a while, but by the time I was able to walk to the nurse's station I felt more embarrassed than in pain."
        "Alice sent me a text later that evening, making sure I was OK."
        "I played it off as no big deal, but I was sore for a couple days after that."
        "I found out later Alice paid one of the musclebound students to help move her furniture instead."
        "She didn't look at me any less after that, but I could feel I had lost a little standing in her eyes."
        jump daymenu
    else:
        "I went to the head of the bed and bent my knees, while Alice and Aida went to the other side."
        MC "On three."
        MC "1... 2... 3!"
        "We all stood up at the same time, lifting as we did."
        "As big as the bed was, it wasn't particularly heavy. I did have to bear more of the weight than they did, but it wasn't taxing or anything."
        "Alice directed us as we moved the bed, and with a little nudging this way and that we had it positioned just right."
        
        "After that it was considerably easier. The table, chairs, dresser and TV stand weren't nearly as heavy."
        "But since I was already there I got conscripted into doing most of the gruntwork, moving everything heavier than a pillow and adjusting it to Alice's eyeballing whims."
        "She said she had everything planned out, but it ended up taking an hour to get everything just right."
        scene Dorm BBW Flip with fade
        "I couldn't tell you if the room looked better when it was done. It was fancier than anything I was used to, but I guess for Alice this was a step down from whatever mansion she had grown up in."
        "I was thinking of a way to politely excuse myself as Alice set out pictures and knick-knacks on her bookshelf, when suddenly I was blindsided by Aida."
        show PRG neutral at center with dissolve
        PRG "W-would you like a snack?"
        "She was holding up a plate of cheese and cracker concoctions, with... some sort of thinly sliced meat on top."
        MC "Uh, thank you."
        "I couldn't just up and leave now, so I took a closer look at the various affects Alice had around her side of the room."
        hide PRG with dissolve
        "The books on her shelf (a number of biographies, plus a few bodice-ripper romance novels)."
        "The dolls and trinkets (sort of standard 'girly' stuff)."
        "And pictures of her parents and what I took to be friends."
        MC "!"
        "One caught my eye. It was Alice and a man roughly our age, but they weren't standing next to each other as just friends."
        "Their bodies were turned toward each other, though they were looking at the camera, hands clasped and cheeks almost touching."
        "Way beyond familiar with each other."
        "And Alice looked genuinely happier than I could recall her being... ever."
        "(Though I had only known her for a few weeks...)"
        MC "Who's that?"
        show BBW happy at center with dissolve
        "She looked at the picture I was looking at, and her expression turned kind of dreamy."
        BBW "Oh. Forgot I still had that one."
        BBW "He's an old flame. Someone I knew back in Tokyo."
        "She took the picture out of the frame and slid it into a binder at the bottom of her bookshelf."
        "I wasn't surprised or intimidated to know Alice had dated before. We're not children."
        "But that guy in the photo was damningly handsome, and dressed so slick. He was probably rich and worldly too."
        "Did Alice still carry a torch for him?"
        MC "Are you guys... still friends?"
        show BBW neutral
        "She shrugged, her posture and expression pokerface blank."
        show BBW happy
        BBW "We were closer once, but after graduating our paths went in different directions."
        show BBW neutral
        BBW "I wasn't interested in a long-distance relationship, and he has his own ambitions for university and beyond, so we called it quits."
        BBW "For now, at least."
        "For now..."
        "So Alice's affections aren't claimed, but I do have a... should I call him a rival?"
        MC "Do you still keep in touch?"
        BBW "A little. We have mutual friends, so we get cc'd emails now and then."
        BBW "But I haven't been too close with anyone from my old school since coming here."
        "I would be surprised if she hasn't told anyone about her condition."
        "I wonder how that other guy would react if he found out."
        "Maybe he's not actually a rival..."
        MC "Well, I need to get back and take care of my homework."
        MC "I'll see you in class tomorrow."
        BBW "Yes, thank you for your help."
        if getAffection("BBW") >= 8:
            show BBW happy
            BBW "Oh, you're perspiring. Here."
            "She handed me a handkerchief, silk with lace around the edges."
            "I almost felt bad wiping my sweat on it, but would it have been impolite to refuse it?"
            MC "Thank you. I'll return it after I wash it."
            "She smiled at me and thanked me again."
        scene Dorm Exterior with fade
        "As I walked back to my dorm I felt amped up."
        "I was simultaneously worried that Alice was still pining for her old boyfriend, while also cheering myself on with the fact that I was here and he wasn't."
        "Maybe there was a chance for me here, if I wanted it."
        jump daymenu

label BBW022_c1_3:
    "I wasn't really in the mood for whatever Alice has in mind right now. Probably some chore she wanted me to do for her, but hopefully not something violating the rules."
    "I texted back that I was in the middle of something, and could I take a rain check?"
    if getAffection("BBW") >= 8:
        $setAffection("BBW", -1)
    "Her response was quick, and kind of curt."
    BBWCell "<If you're busy, you're busy. I shall find someone else to assist me.>"
    "So I was off the hook, but part me wondered if she was going to take this personally..."
    jump daymenu

label BBW023:
    $setProgress("BBW", "BBW025")
    scene Classroom with fade
    show BBW neutral at center with dissolve
    show PRG neutral at Position(xpos=0.6, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    "After classes, Alice called Aida and I together for a business meeting."
    "She played it all straight-laced, going through a list of topics like an actual agenda."
    hide PRG with dissolve
    "The fact that there were only two employees, myself and her, didn't lead her to treat this any less properly."
    "She wasn't playing, and when she looked at me and said"
    BBW "Hotsure-san, could you please give a rundown of your work in deliveries?"
    "She looked as no-nonsense as a teacher calling on a student."
    MC "Uh... I didn't prepare anything."
    if getAffection("BBW") >= 7:
        BBW "I know, I'm dropping this on you out of the blue. This meeting itself was a last-minute change of plans."
    BBW "Just tell us how things have been going with the deliveries. You haven't had any issues, correct?"
    MC "No, no problems so far."
    MC "I do have to avoid Matsumoto-san when I'm carrying a package too big for my bag, I don't think the other members of the student council really care."
    BBW "The deliveries aren't interfering with your studies, are they?"
    MC "No. I've gotten in the groove."
    MC "Waiting until right before or after the dinner hour seems to be the key to catching the students in their dorms."
    BBW "Splendid."
    BBW "Business has been pretty stable across the board. I'm satisfied with our sales so far, they're within range of my projections when we started."
    BBW "But as word of mouth spreads the number of orders will increase, and you'll be working harder than before."
    MC "I think I can handle it."
    BBW "That's what I like to hear."
    BBW "On that note, next on our agenda is the coming sales period."
    BBW "This will cover the next month and a half, with our primary focus being summer clothing and accessories."
    BBW " The weather is warming up, so expect a rise in demand for tank tops, sundresses, and sunglasses."
    BBW "With an emphasis on style."
    BBW "My reconnaissance to the nearby town tells me that the students here won't be hurting for seasonal clothing in even the largest sizes."
    BBW "But so many of the larger-sized pieces sacrifice fashion for function, creating an opening for our enterprise to seize upon."
    BBW "Believe me, no woman at this school is going to keep potential body image issues at bay when they're dressed like a Quaker."
    MC "I don't get it... Quaker...?"
    BBW "Just... Be ready in a day or two to start pushing bikinis and sun hats."
    BBW "I'm working on a revised catalog with our summer line at the forefront, with only the most stylish or boldest designs on offer."
    if getSkill("Academics") >= 4:
        MC "Women want to feel beautiful. Even here."
        BBW "Especially here."
        MC "Yeah, I've noticed a lot of orders have been for things like bath salts and oils."
        MC "There's been some for make-up, but the... I guess you'd call them 'body works'?"
        MC "Those seem to be really popular."
        MC "Maybe we could have a sale for those as well."
        $setAffection("BBW", 1)
        show BBW happy
        BBW "That's an excellent observation, Keisuke. And not a bad suggestion."
    else:
        BBW "In addition, there has been a steady market in our health and beauty section."
        BBW "The more luxurious items like bath oils and perfumes have done especially well."
        BBW "I wasn't expecting there to be too much demand for such indulgences, but I believe that in times such as these people want to pamper themselves."
        BBW "It offsets the blow being here delivers."
    show BBW happy
    BBW "So I'm going to make plans for a sale on bath salts, perfume and assorted beauty products soon as well."
    show BBW neutral
    BBW "Kodama-san. Is there a dance or some form of soiree planned for next month?"
    show PRG neutral at Position(xpos=0.6, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Um... I don't know. I'll check."
    BBW "Thank you."
    hide PRG with dissolve
    show BBW happy
    BBW "Timing is everything in business. If we do this right we can net at least 2,500 yen above our current weekly sales."
    MC "That sounds smart."
    MC "I have seen some of our classmates... you know, getting close."
    MC "You almost wouldn't know there's anything 'off' about this place."
    BBW "People handle change in their own ways. Moving forward as if nothing is different is one way."
    MC "You mean ignoring bad news?"
    show BBW neutral
    BBW "Or accepting that which you can't change. It's a matter of perspective."
    BBW "Ending up here doesn't change the fact that we're young only once. Dating, partying, making mistakes we'll regret when we're older..."
    show BBW happy
    BBW "If you don't do it here, then when?"
    MC "True."
    if getFlag("BBW021_c3"):
        jump BBW023_fail
    elif getFlag("BBW021_c2"):
        menu:
            "I've been thinking about it myself lately. Dating.":
                jump BBW023_c1_1
            "I can understand why others would want to. It might not be for me, though.":
                jump BBW023_cx_2
    else:
        show BBW happy
        BBW "As busy as I've been with everything else - my studies, the music club, starting this enterprise - I've been thinking about my own social life."
        BBW "Not all interaction has to be about networking. My father has always taught me about the value of personal time."
        MC "He's right. A social life is kind of necessary. Part of the human experience and all."
        "She looked me in the eyes, and I could guess what was about to come."
        BBW "Are you talking about hanging out with your classmates, or have you thought about more intimate possibilities?"
        MCT "She's not asking out of idle curiosity. Better tread lightly."
        menu:
            "If the right girl came along.":
                jump BBW023_c2_1
            "That's a bit more serious than I've thought about.":
                jump BBW023_cx_2

label BBW023_fail:
    "She looked back at her agenda, then declared"
    show BBW neutral
    BBW "I think that covers everything for today."
    BBW "We might have another meeting next week, but only if there's anything of importance to discuss."
    BBW "If not, just keep up the good work."
    MC "Thanks. I will."
    scene Dorm Exterior with fade
    "With the meeting adjourned I went back to my dorm to take care of my homework."
    "Just another day. Nothing significant happening."
    jump daymenu

label BBW023_c1_1:
    show BBW happy
    BBW "Oh?"
    MC "Yeah. I mean, you're right. This is the only youth we get."
    MC "And not to be callous, but my condition is pretty easy to deal with."
    MC "I can sympathize with those who have something more extreme, but that's no reason I can't make the best of my time here."
    BBW "Exactly."
    show BBW aroused
    BBW "Has anyone in particular caught your eye?"
    "It was impossible to miss what was going on in her mind, the way she was practically batting her eyes, and how she brushed her hair behind her ear."
    "But my tongue chose this moment to get tongue-tied."
    "All I could think to say was"
    MC "There are one or two girls in our class. And around the school."
    "I started blushing like I was 13. She could see what I was thinking, and that just made me nervous."
    MC "I just want to be sure they're interested, first."
    $setAffection("BBW", 1)
    "It looked like she was holding back a chuckle, but there wasn't anything malicious in her expression."
    "She was probably just bemused. Maybe she was used to being around more decisive people."
    show BBW happy
    BBW "Well, the only real way to be sure they're interested is to ask them, yes?"
    MC "Right. Yeah."
    MC "Just a matter of finding the opportunity."
    BBW "Or creating the opportunity. You can't just wait for things to fall in your lap."
    MC "I guess not."
    "She looked back at her agenda, then declared"
    BBW "I think that covers everything for today."
    BBW "We might have another meeting next week, but only if there's anything of importance to discuss."
    BBW "If not, just keep up the good work."
    MC "Thanks. I will."
    scene Dorm Exterior with fade
    "With the meeting adjourned I went back to my dorm to take care of my homework."
    "But I couldn't stop thinking of Alice, how close I came to asking her out."
    "She was waiting for me to, that much was obvious."
    "But the moment didn't seem right."
    "And now that I was alone, I started thinking about how little we had in common."
    "She's rich and worldly, I'm... not."
    "But going down that rabbit hole would only make me more miserable. If she's interested, what did I have to lose?"
    "Who knows? This could turn out to be something real, whatever our differences."
    "I ended up forgetting about my homework until the next morning, when I did it all in a frantic rush."
    jump daymenu

label BBW023_c2_1:
    MC "I don't want to say 'No' outright, but I've never been the sort to see dating as something to do just for the sake of doing it."
    MC "Maybe I'm kind of square like that, or you could say I'm more discerning."
    show BBW neutral
    BBW "No, that's understandable."
    BBW "If you don't know what you're looking for, you're unlikely to find it."
    BBW "Rushing in blind is more likely to waste a lot of energy than anything."
    BBW "I just hope you don't miss the 'right woman' when she comes along."
    "She looked back at her agenda, then declared"
    BBW "I think that covers everything for today."
    BBW "We might have another meeting next week, but only if there's anything of importance to discuss."
    BBW "If not, just keep up the good work."
    MC "Thanks. I will."
    scene Dorm Exterior with fade
    "With the meeting adjourned I went back to my dorm to take care of my homework."
    "But I was distracted with Alice's rather heavyhanded hinting."
    "Whether she was the 'right girl' or not I couldn't say, but I could see that I was at a fork in the road, and I had to make a decision one way or the other soon."
    "Maybe asking her out would turn out to be a good thing. We might have more in common than I know."
    "Or if I'm this undecided I should just back off, and let her know. She didn't deserve to be left hanging, did she?"
    "Either way, this would have to wait to be settled for another day."
    jump daymenu

label BBW023_cx_2:
    MC "I guess I would say 'Not right now.'"
    MC "I've got plenty on my plate, what with school and this job."
    MC "Once I find my groove, in a month or two, I might have a different answer."
    show BBW neutral
    BBW "I suppose I can understand that."
    BBW "Dating isn't like a passive hobby. If your heart isn't in it, you're better off not doing it."
    MC "It wouldn't be fair to the other person, you know?"
    MC "What if they're more invested in it but I'm just 'Whatever'?"
    BBW "No, I know."
    "She looked back at her agenda, then declared"
    BBW "I think that covers everything for today."
    BBW "We might have another meeting next week, but only if there's anything of importance to discuss."
    BBW "If not, just keep up the good work."
    MC "Thanks. I will."
    scene Dorm Exterior with fade
    "With the meeting adjourned I went back to my dorm to take care of my homework."
    "I hoped she got the message. She's intelligent enough."
    "I just didn't want to come out and say 'I'm not interested in you like that.'"
    "Maybe she could handle it, but no reason to risk being too harsh."
    jump daymenu

label BBW024:
    scene Hallway with fade
    "My turn to clean the classroom had come up again, so I ended up walking through empty halls alone."
    "I thought about going back to my dorm, but I wasn't really 'feeling' it."
    "Maybe if I took the long way around I would find something more interesting than those now familiar four walls."
    show BBW angry at center with dissolve
    MC "Oh, Alice. Good afternoon."
    MC "Something bothering you?"
    BBW "No. Just a minor perturbance."
    MCT "You look a little upset for something you say is minor."
    MC "So what's up?"
    BBW "The library board is having a meeting, so the place is closed for the afternoon."
    MC "Looking for a book?"
    BBW "No, I need a quiet place to meditate."
    MC "Huh. Wouldn't have figured you for that sort of thing."
    show BBW neutral
    BBW "It's quite common among CEOs. Running a business demands a lot, and it's important to, as a former classmate called it, defrag your mental hard drive regularly."
    MC "Do you always do it in the library?"
    BBW "Yes. Not so much because of the quiet - I have noise-canceling headphones for when I use my mindfulness app - but because I want someplace where I don't have to worry about people intruding on my space."
    BBW "It can get distracting to have people walking back and forth, the more obnoxious ones asking me what I'm doing."
    "Then she added, under her breath:"
    BBW "(That I would have my plans upset on today of all days...)"
    menu:
        "What's special about today?": # (If affection < 5, +1)
            jump BBW024_c1_1
        "Recommend a place to meditate.":
            MC "There have to be other places where you can find solitude."
            jump BBW024_c1_2

label BBW024_c1_1:
    MC "What's special about today?"
    if getAffection("BBW") < 5:
        $setAffection("BBW", 1)
    BBW "It's not 'special.' Not in a positive sense."
    BBW "I have a dental appointment coming up this weekend. Those are never pleasant, so I'm on edge."
    BBW "That I would have this trouble now, when I need serenity..."
    MC "There have to be other places where you can find solitude."
    jump BBW024_c1_2

label BBW024_c1_2:
    menu:
        "How about the gardens?": # (+1 affection)
            jump BBW024_c2_1
        "How about the rooftop?":
            jump BBW024_c2_2
        "What about your dorm? (disabled)" if getSkill("Academics") >= 4 or getFlag("BBW024_c2_3"):
            pass
        "What about your dorm?" if getSkill("Academics") < 4 and not getFlag("BBW024_c2_3"):
            jump BBW024_c2_3

label BBW024_c2_1:
    MC "How about the gardens?"
    "She thought about that for a second."
    show BBW neutral
    BBW "Is there a lot of foot traffic there? I've never been to that part of the school."
    if getAffection("GTS") <= 5:
        MC "I don't think so."
    else:
        MC "No. It's an isolated island in the school."
    BBW "That sounds perfect."
    scene School Planter with fade
    "I had to help her find her way to the gardens. Sure enough, the place was empty at first glance."
    "Alice found a seat under a shady tree and put her headphones on."
    "When she closed her eyes I was torn between hanging around until she was done or leaving her. I decided it would seem rude if she finished, opened her eyes and found me gone."
    "Not that I knew how long she would take..."
    "I occupied myself by looking at the flowers. This place really was quiet."
    "At one point I saw Naomi walk by."
    show GTS neutral at center with dissolve
    "I waved, but when she saw Alice she seemed to stiffen."
    "She nodded slightly, then continued on."
    hide GTS with dissolve
    "After ten minutes Alice opened her eyes and took her headphones off."
    show BBW happy at center with dissolve
    MC "Feel better?"
    BBW "Calmer, yes."
    $setAffection("BBW", 1)
    BBW "This place was a good suggestion."
    "She looked at her watch and tsk'd."
    show BBW neutral
    BBW "Tsk."
    BBW "No time to savor the feeling, though. I have too much else to do."
    show BBW happy
    BBW "Keisuke. I'll see you in class."
    hide BBW with dissolve
    "And she was off."
    "Me, I didn't have anywhere to be. Back to my original problem."
    jump daymenu

label BBW024_c2_2:
    MC "How about the rooftop?"
    show BBW neutral
    BBW "The roof? Are we allowed up there?"
    MC "We're not not allowed, I don't think."
    scene Roof with fade
    "I led her to the roof, Alice grumbling about the stairs after the second story."
    show BBW neutral at center with dissolve
    BBW "Such an inconvenient place."
    MC "Sure to be secluded, right?"
    BBW "You're not wrong."
    BBW "Let me find a place to get comfortable."
    hide BBW with dissolve
    "It would have felt odd to just leave her there on the roof, so I hung back and let her get on with it."
    "Unfortunately the place turned out to not be as empty as I was expecting."
    show BE happy at center with dissolve
    BE "Hey, Keisuke, what's up?"
    MC "Alice is here to meditate. This seemed the most quiet place."
    show BE neutral
    BE "Ooooh?"
    BE "Wouldn't have taken her for the spiritual sort."
    MC "I think she just likes to clear her head."
    show BE happy at Position(xpos=0.8), Transform(xzoom=-1) with dissolve
    "As I was talking Honoka walked up to Alice."
    "Not right in her face. She hung back a bit. But it was close enough to disturb Alice."
    show BE happy at Position(xpos=0.65), Transform(xzoom=-1) with dissolve
    show BBW angry at Position (xpos=0.8, xanchor=0.5, yalign=1.0) behind BE with dissolve
    BBW "..."
    "She opened one eye, frowning."
    if getAffection("BBW") >= 8:
        MC "Here, why don't we give her some space?"
        "I went up and pulled Honoka back, but she resisted."
        show BE angry
        BE "Leggo!"
    BBW "Do you mind?"
    "She slipped her headphones down, clearly irritated."
    show BE neutral
    BE "Why are you meditating?"
    show BBW neutral
    BBW "To calm my mind. To find my center."
    show BE angry
    BE "... Sounds boring."
    BE "I could never sit still for so long."
    BBW "Actually, you could do just five minutes a day and derive some benefit from it."
    show BE neutral
    BE "No, still too long."
    show BE happy at Position(xpos=0.65, yalign=1.0), Transform(xzoom=1)
    BE "Hey, Keisuke. Race you to the vending machine! Loser buys!"
    hide BE with dissolve
    show BBW angry
    "And then she was racing to the stairwell before I could even respond."
    "I looked back at Alice, still annoyed."
    MC "She... gets like that."
    MC "Actually, I probably should have expected to find her here. She comes up here now and then."
    show BBW angry at center with dissolve
    BBW "So I see."
    show BBW neutral
    BBW "Well, the place is quiet now."
    BBW "I don't have much time to spare, but maybe I can still salvage a moment's peace."
    MC "Yeah, I'll... I'll go make sure she doesn't fall down the stairs."
    "It didn't seem like she was angry at me personally, but even still, I could read her mood."
    "I quietly retreated, giving her solitude."
    jump daymenu

label BBW024_c2_3:
    MC "How about your dorm?"
    "She gave me a look that mixed irritation with exasperation and pity."
    show BBW angry
    BBW "Tsk."
    $setAffection("BBW", -1)
    BBW "That was my first choice, but Kodama-san has trouble sitting still when she studies."
    BBW "She paces around. It gets distracting."
    MC "Oh... Yeah, I guess there's a reason you're not there already."
    jump BBW024_c1_2

label BBW025:
    $setProgress("BBW", "BBW026")
    scene Cafeteria with fade
    "The music club was meeting today, which meant Alice wouldn't have her dinner until later."
    "I had to pass along a payment for a delivery to her. That was the reason I gave myself for waiting to get my own dinner."
    "I could have rushed to meet her before the meeting started, get in and out of the music room, but..."
    "Anyway, I found her at her usual table."
    "I wouldn't say this outloud, but it was hard to miss her."
    show BBW neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    "I had noticed it in class this morning. While her clothes still fit her perfectly, she was unmistakably heavier."
    "I assume she had been gaining steadily, but today was the point when I took a good look at her and realized that she was bigger."
    "It didn't seem to bother her. She had been most pleasant all day, and right now she looked to be enjoying her dinner."
    "Maybe-"
    pause 1
    show BBW happy at center with dissolve
    BBW "Ah! Keisuke! Good evening."
    MC "Good evening."
    MC "I just wanted to make a quick drop-off. Yamaguchi-san apologizes for the late payment."
    BBW "Oh. Thanks."
    BBW "I appreciate your promptness."
    MC "I'll leave you to your meal."
    BBW "Oh, you don't have to rush off. Have a seat."
    BBW "Aida made a bit too much flatbread. Help yourself."
    MC "Thank you."
    MCT "It does look like there's more food than usual. Is her appetite growing with her body?"
    "I meant to sneak a quick peek at Alice's belly, round enough that it filled most of her lap when she sat down."
    show BBW neutral at Position(xpos=0.5, ypos=0.0, yanchor=0.3), Transform(zoom=2.0)
    "I must have been staring, because when I looked up I found her watching me."
    show BBW neutral at center, Transform(zoom=1.0)
    MCT "Crap. Say something before she does."
    MC "I hope I'm not overstepping any boundaries, but I like how you're carrying your new weight."
    "It sounded a bit more suave in my head, and when she didn't respond at first I was worried she had taken it the wrong way."
    "But then she fluttered her eyes and laughed."
    BBW "That is rather bold, Keisuke. But I like your directness."
    BBW "And thank you, by the way."
    BBW "I believe I've said before one of the side goals of my business is to help our classmates weather these changes."
    BBW "My own continued self-assurance is integral to that. I am the face of the company, after all."
    BBW "Still, it is good to know that others have picked up on that."
    MC "Judging by how the perfumes and cosmetics are selling, I'm not sure if the other ladies are trying to cover up their own growth or if they're like you."
    MC "Determined to keep their chin up regardless of what life is throwing at them."
    BBW "I think it's more the latter."
    BBW "There were a lot of people, men and women, initially despondent when the term started."
    BBW "But the general mood of this place has risen. Most people are more confident, or at least lighter of spirit."
    MC "It is the season for romance, after all."
    BBW "A little late. We're almost in summer."
    BBW "But still, the perfect time to be out enjoying the fresh air and sunshine. Which is always nicer with someone close to you."
    MCT "Can't misread that sign..."
    menu:
        "You're not interested in dating her.":
            jump BBW025_c1_1
        "Ask her out.":
            jump BBW025_c1_2

label BBW025_c1_1:
    MC "Or just having fun with friends."
    MC "Like you, Alice. You're a good friend."
    pause .25
    show BBW neutral
    pause .25
    show BBW angry
    $setAffection("BBW", -10)
    BBW "..."
    MCT "Uh-oh..."
    show BBW neutral
    BBW "(sigh)"
    BBW "Thank you, Hotsure-san. I consider you a friend, too."
    "Her tone was remarkably even, her face stone-like, but there was hellfire in her eyes."
    "Maybe spending so much time with her lately has put me in tune with her emotions..."
    "Or maybe she's just really easy to read."
    "Either way, I knew how to read a room. Looking at my phone, I said"
    MC "Oh, shoot. My mom's been trying to call me."
    MC "I gotta go. I'll see you later."
    hide BBW with dissolve
    "And I made for the exit, not running and certainly not looking back."
    MC "Probably best if I don't run into her for a couple days. Or weeks."
    $disableRoute("BBW")
    jump daymenu

label BBW025_c1_2:
    MCT "Deep breath. Here we go."
    MC "Alice. Would you like to go out some time?"
    if getAffection("BBW") < 9:
        $setFlag("BBW025A_unlock")
        show BBW neutral
        BBW "'Go out' as in 'go out,' I take it."
        show BBW happy
        BBW "I have to compliment you on your taste..."
        show BBW neutral
        BBW "But I don't think this is the right time."
        MC "Oh..."
        MC "I guess you do have a lot to deal with right now, what with your business and all."
        BBW "Hmm?"
        BBW "No, that's not taking up too much of my time."
        MC "Wait. Are you... not doing the 'It's not you, it's me' thing?"
        BBW "Oh, no."
        BBW "The issue isn't me."
        BBW "Not that it's you, per se."
        BBW "It's us, rather."
        BBW "Compatibility-wise, I'm not convinced there's something there."
        MC "What do you mean?"
        BBW "There is a physical connection. You have a certain charm, and just now you mentioned my own glamor."
        show BBW haughty
        BBW "Not in a passive or even placating way, but with a genuine eye for beauty."
        BBW "But you're not the first gentleman I've had swoon over me, mistaking physical attraction for emotional resonance."
        show BBW neutral
        BBW "And I've found those who can't look past the flesh often have nothing under the surface themselves."
        BBW "Convince me this is not an idle fancy of yours, and I might change my answer."
        BBW "I'm not saying you have to sweep me off my feet. Love is not a spontaneous combustion, but a bonfire that must be built and tended."
        BBW "But I know not to go flitting around like a moth drawn to any bright light, and I want to make sure you understand that as well."
        BBW "Do you understand?"
        MC "I think I do."
        show BBW happy
        BBW "Glad to hear."
        BBW "Now if you'll excuse me, I see Aida approaching with my second course."
        hide BBW with dissolve
        "I excused myself, leaving Alice to her dinner."
        "I did understand what she was getting at, though I'm not sure I agreed."
        "If this was purely physical, I could have just asked her out back at the start of the term."
        "Didn't my working for her count for anything?"
        "Well, no. She probably saw that as an employer-employee relationship. I guess I should be happy she didn't outright say 'No' based on that."
        "So, OK. I just have to prove myself more serious."
        "Not impossible."
        jump daymenu
    else:
        $setFlag("BBW_dating")
        show BBW happy
        BBW "Yes, I would."
        MC "Really?"
        MC "I mean, wonderful. Splendid."
        MC "Say... Saturday night?"
        MC "Dinner and a movie?"
        BBW "That sounds nice."
        MC "OK. I'll meet you at 6."
        "I might have stammered for a few minutes more if Aida hadn't turned up just then, wheeling in Alice's second course."
        "It was the perfect out, so I excused myself and walked out of the cafeteria."
        hide BBW with dissolve
        "It was hard to fight the urge to skip or whoop, until I reached the hall and suddenly realized I had no idea where I was going to take her."
        "I was so focused on just getting the question out I didn't think about what came next."
        jump daymenu

label BBW025A:
    scene Cafeteria with fade
    "I was having trouble paying attention to the week's company meeting."
    show BBW neutral at center with dissolve
    BBW "Moving on to new business, the recent tariff battle between America and China has me concerned blah blah blah..."
    "After building up the courage to ask Alice out it was hard not to treat her 'Ask me later' response as a loss."
    "A straight up 'No' would have been like ripping the band-aid off, the pain strong but gone quickly."
    show BBW happy
    "And I could have written it off as her just not being into me. Not what anyone wants to hear, but it would have been easier to move on from."
    "But her actual response left the door open, and that just made things worse. Neither 'Yes' nor 'No,' I was left wondering what exactly she was looking for."
    show BBW angry
    "Do I act more manly? More independent? More subservient?"
    "I at least knew that just asking her wouldn't cut it. That would be too desperate, even for someone who enjoyed attention like she did."
    show BBW neutral
    "So I came to the decision to just be myself - as much as that sounded like pablum - and see if her opinion of me wouldn't change."
    "She seemed happy enough lately, but how to tell that was a reflection of her attitude towards me and not just how she felt with her place in life right now?"
    BBW "Thoughts?"
    MCT "Crud. I missed 90% of that."
    MCT "Something about tariffs?"
    MC "I... have not been paying attention to the news."
    MC "If you have some articles I could read I could catch up, but right now... I can't weigh in."
    "Alice nodded her head."
    BBW "I understand. This probably didn't seem too important as a ground-level salesman. (Even though this does trickle down to what products we'll have for sale and possible price increases...)"
    show BBW happy
    BBW "But the potential for upward mobility is always there for workers who display motivation, drive and initiative."
    BBW "You don't have to be just a salesman forever, Keisuke. Opportunities don't always come flashing neon signs."
    BBW "Next on our agenda blah blah blah."
    show BBW neutral
    "Despite my best efforts, I got lost in my own thoughts again."
    "Was Alice just being encouraging, or was she hinting that there was an opportunity for me right now?"
    "When the meeting broke - coinciding with Aida rolling up the first course of Alice's dinner - I leapt."
    MC "One last thing, Alice. It's not business related."
    show BBW happy
    "Her expectant look perked up, which seemed like a good sign but which also made me nervous."
    "But after going through this once already, I couldn't back down now."
    "Especially since I had what I was sure was a killer offer."
    MC "There's a special showing of The Lace of Heaven this Saturday. Would you be interested in seeing it?"
    "Lace of Heaven wasn't what I would call a 'Keisuke movie,' but the time period arthouse title seemed like the sort of thing Alice would be interested in."
    show BBW happy
    "And it looked like I had chosen well, judging by her reaction."
    $setFlag("BBW_dating")
    BBW "That sounds delightful."
    BBW "I'll trust you to get the tickets, and perhaps we should have dinner before the show?"
    MC "Yeah. Leave it all to me."
    MC "I'll let you know what time to be ready once I have everything sorted out."
    BBW "It's a date."
    "The fact that she was the one to say that made me even giddier, but I managed to keep myself restrained as I left the cafeteria."
    scene Hallway with fade
    "I held out until I made it to the hallway before I pumped fist."
    MC "Mission accomplished!"
    MC "Of course, now I have to work to keep her happy."
    MC "So it's more like 'Level one complete.'"
    MC "But one thing at a time. I've got the day set, I have things planned. Let's get through that first and worry about what comes next later."
    jump daymenu

label BBW026:
    scene Classroom with fade
    $setProgress("BBW", "BBW028")
    if not getFlag("BBW_dating"):
        "After Alice turned down my invitation to a date - not an actual 'No,' but more like 'Try again later' - I'd been racking my brains trying to think of what else I could do to clear that last hurdle."
        "Not that I was sure what the hurdle was. Alice had said she wanted something more than physical attraction, so complimenting her on her fashion wasn't going to cut it."
        "I'd have to dig deeper, but when you aren't even in a relationship what can you do to woo someone?"
        "All my ideas came from movies or TV shows, the big romantic gestures that I had a feeling Alice would dismiss as superficial."
    else:
        "Getting Alice to say 'Yes' to a date had been a minor victory, but it also opened up a new level of challenges."
        "I had already put a lot of thought into what we would do come Saturday night. I had the movie and restaurant picked out, and I had even tried to set a reservation."
        "Turned out they didn't take reservations, but I was able to get the movie tickets in advance."
        "But Saturday wasn't here yet. I'd still be sitting in classes with her, working with (or for, technically) her. There'd be chances to embarrass myself, to turn her off even unintentionally."
    "I wasn't stressed out so terrible I couldn't sleep, but I couldn't keep such thoughts out of my mind as I sat through class."
    MCT "At least I don't have anything else to worry about right now."
    show HR neutral with dissolve
    HR "And yes, that will be on the test."
    MCT "!"
    MCT "Test?! Oh... crud."
    MCT "The test I haven't made time to study for yet."
    MCT "Looks like my evening's been planned."
    hide HR with dissolve
    "But as I was getting ready to leave Alice put a hand on my shoulder."
    show BBW neutral with dissolve
    BBW "May I have a moment?"
    MC "Uh, sure."
    "Her tone of voice almost made my stomach drop. This wasn't good news, whatever it was."
    
    scene Hallway with fade
    show BBW neutral
    BBW "I have a problem. I need some help."
    MCT "OK, so it's not about me. That's good."
    BBW "I need to mail off some paperwork related to the requisitions company, tax filings and whatnot."
    BBW "It needs to get to my family’s accountant within a couple days, and I don’t trust regular mail going out of the school."
    MC "Think it’ll take too long?"
    BBW "Exactly."
    BBW "But I can’t make the trip to the post office to send it express, because I have music club. And Aida is busy with other tasks."
    BBW "Would you be willing to make the trip for me? It would save me the hassle tomorrow, which is already looking to be an ordeal."
    MCT "Great. I have a chance to court Alice’s good graces, but only if I shirk my studies."
    menu:
        "Sorry, but I don't have the time.": #(+1 affection)
            jump BBW026_c1_1
        "Sure, I can do it.": #(-1 affection)
            jump BBW026_c1_2
        "(I think I can pull off both the errand and the studying)": #(+2 affection, if Academics score is > / = 12; -1 affection if Academics score is < 12)
            jump BBW026_c1_3

label BBW026_c1_1:
    MC "Sorry, but I don't have the time."
    MC "I need to study for the test tomorrow."
    BBW "I see."
    show BBW happy
    BBW "That is the greater priority, though."
    BBW "I'll see if I can find someone else to help out."
    BBW "Study hard."
    "Now that I had thrown away the chance to score points with Alice, I really had to buckle down and make the most of my time."
    scene Classroom with fade
    "It was worth it, though. I scored higher on the test than I expected."
    "And Alice did notice how well I did."
    show BBW happy with dissolve
    $setAffection("BBW", 1)
    BBW "Well done, Keisuke."
    BBW "You even got question six right. I found that one rather... tricky."
    MC "Yeah, it almost tripped me up."
    MCT "That must be worth something in her eyes, right?"
    jump daymenu

label BBW026_c1_2:
    MC "Sure, I can do it. Just give me the address."
    show BBW happy
    BBW "Really? Excellent."
    BBW "Just bring it back to my room tonight."
    BBW "You're a lifesaver, Keisuke."
    "I felt pretty cocky as I dropped my stuff off in my room and then headed into town."
    scene Town with fade
    "I had hoped it would be a quick jaunt. If I rushed to and from the post office I could get back in time to get some studying done."
    "Unfortunately the post office was pretty busy. I didn’t think this town was that active, but there was a line almost to the door of people sending stuff off or picking stuff up."
    "I didn’t have any chance to study that night, but as I dressed for bed I made a promise to myself to cram the next morning."
    scene Classroom with fade
    "It did me no good."
    "I wasn't too far off from a passing score. I could see a handful of questions where I was almost right..."
    "And there were several others where I was almost on the right track..."
    "And the ones where I had guessed... Well, if I had guessed differently..."
    "No, I had failed."
    show BBW neutral with dissolve
    BBW "So how did you do, Keisuke?"
    BBW "I thought question six was a bit tricky."
    MC "I... didn't get that one."
    BBW "Did you pick 'D' as well?"
    "Before I could stop her Alice took the sheet from my hand."
    "Her expression was even more crushing than the test score itself."
    show BBW sad
    BBW "Oh... What happened, Keisuke? Didn't you study for this?"
    MC "I didn't get a chance."
    MC "I meant to last night, but I went into town for you and that turned into a whole thing."
    BBW "Why didn't you tell me you needed to study? I could have gotten someone else."
    MC "I just... I thought... I don't know what I was thinking."
    $setAffection("BBW", -1)
    BBW "You're going to have to really work to keep your grades up after this, Keisuke."
    BBW "If you need time to study, just tell me. I can find other people to help me out."
    MC "No, it's-"
    "I wanted to say 'It's fine,' but I realized I'd just be digging myself in deeper."
    MC "I'll keep that in mind."
    MCT "So now Alice thinks I'm sliding towards flunking. Not the best foot forward."
    jump daymenu

label BBW026_c1_3:
    MCT "I think I can pull off both the errand and the studying."
    if getSkill("Academics") < 12:
        jump BBW026_c1_2
    else:
        MC "Sure, I can do it. Just give me the address."
        show BBW happy
        BBW "Really? Excellent."
        BBW "Just bring it back to my room tonight."
        BBW "You're a lifesaver, Keisuke."
        "Alice said it wouldn't take long, but you never knew."
        "I left for town right away, wanting to get the job done quick. And I brought my books with me."
        "I could almost sense there would be some delays, and if that was the case I wanted to get some quick studying in while I waited."
        scene Town with fade
        "It turned out to be the right call."
        "I had hoped it would be a quick jaunt. If I rushed to and from the post office I could get back in time to get some studying done."
        "Unfortunately the post office was pretty busy. I didn’t think this town was that active, but there was a line almost to the door of people sending stuff off or picking stuff up."
        "At least I was able to use my time waiting efficiently. Got a lot of studying in."
        scene Classroom with fade
        "And it was worth it. I scored higher on the test than I expected."
        "Alice noticed how well I did, which on top of running the errand had to have raised my standing in her eyes."
        show BBW happy with dissolve
        $setAffection("BBW", 2)
        BBW "Well done, Keisuke."
        BBW "You even got question six right. I found that one rather... tricky."
        MC "Yeah, it almost tripped me up."
        "As casual as I thought I sounded, I was really about to crumble."
        "I had almost bitten off more than I could chew, but I had managed to come out ahead."
        "I just hoped I wouldn't have to juggle so much at once anytime soon again."
        "Maybe Alice wouldn't turn out to be so high-maintenance? Hopefully?"
    jump daymenu

label BBW027:
    scene Hallway with fade
    "Getting out of class didn't free me for the day. It meant my day had just started."
    "When we were dismissed from class I made a beeline for the library to take care of some research for a project I'd been putting off."
    "Then I spent an hour zipping around the girls' dorm delivering orders for Alice's business."
    "Then to the boys' for the same. Then back to the girls' to try again with those who weren't in their room the first time."
    "I wanted to get it all done quickly, because I had to get tomorrow's homework done and I had some long-term assignments weighing on my mind."
    "Eventually I only had one last package to deliver, but after the third time visiting the lady-in-question's dorm I decided to call it a day on that front."
    "I had too much homework to tackle to spend all afternoon on this one thing."

    scene Cafeteria with fade
    "The cafeteria was opening for dinner at this point, and I needed fuel."
    "It felt good to get off my feet, but once I had my food and a seat I pulled out a textbook."
    "I had too much to do right now to relax."
    "I was in the middle of my meal and a description of eukaryotes when Alice appeared."
    show BBW happy with dissolve
    BBW "Hello, Keisuke."
    BBW "Studying while eating? I applaud your efficiency."
    MC "Thanks..."
    "I rubbed my eyes and sighed."
    show BBW neutral
    BBW "Something wrong?"
    MC "Just feeling overwhelmed right now."
    BBW "Hmm... Yes. Our courseload is picking up."
    show BBW happy
    BBW "No special treatment because of our condition, right?"
    MC "I'm not asking for things to be easier, I just..."
    MC "You ever feel like you're going as fast as you can just to keep up?"
    show BBW neutral
    BBW "The Red Queen race."
    MC "What?"
    BBW "Literary reference that made its way into scientific terminology. It's an esoteric term for what you just described."
    BBW "Everyone feels it now and then."
    show BBW happy
    BBW "Trust me. I grew up in circles of the most driven and harried people in the world."
    BBW "You're either struggling to get to the top or you're struggling to keep your place. Or both."
    MC "Yeah, that sounds super-stressful."
    show BBW sad
    BBW "It is. I've seen people unable to keep up. They didn't just drop out of the game, they... crashed."
    MC "Cripes. Why do you sound so happy?"
    show BBW happy
    BBW "Because I love the stress."
    BBW "To a point, of course. Everyone has their limits."
    show BBW haughty
    BBW "But when my workload is just right - not too light, not too heavy - I feel invincible."
    BBW "The thought of having so much being hurled at me at once and I remain unbowed... I am a woman on fire."
    MC "I... see."
    MC "But you still need a break now and then."
    show BBW neutral
    BBW "Oh, not just 'now and then.'"
    BBW "Recreation and relaxation have to be part of your schedule. You need time to recover, mentally and physically."
    BBW "Just make sure your downtime is not time wasted. Slowing down doesn't mean being idle."
    BBW "Time is like nothing else. What you lose is gone forever."
    BBW "You can make more money. You can replace worn out or damaged goods. Usually. But when the day is done you don't get it back."
    MC "So even when you're taking it easy you don't actually relax?"
    BBW "Oh, no. I do relax."
    show BBW haughty
    BBW "I wouldn't bother paying for massages if I was still tense afterward, would I?"
    show BBW neutral
    BBW "I just never do nothing. Even when I'm relaxing my decisions about what to do are made with an eye towards replenishing my energy or rejuvenating my mental prowess."
    MC "That still sounds stressful. To have a free afternoon and try to figure out the best way to unwind?"
    MC "I don't know. When I have free time I'm intentionally not thinking about what the most efficient thing to do with my time is."
    BBW "It's not hard, if you plan ahead and know what you want."
    BBW "Like I said before, you have to make your downtime part of your schedule."
    MC "OK, I guess I get that."
    MC "But real life doesn't always accommodate, you know?"
    MC "Things happen. Unexpected problems turn up, or it takes longer to do something than you expect."
    "Alice shook her head, as if I didn't understand her."
    BBW "Of course 'things happen.' Where would the challenge be if you knew exactly what to expect all the time?"
    BBW "But to the well-organized mind even the unexpected can be anticipated."
    show BBW haughty
    BBW "And, if you're good enough, the unexpected won't be a problem."
    show BBW happy
    BBW "But my point stands. You need to slow down now and then."
    BBW "Set aside a chunk of time each day where you don't think about school or work or anything."
    BBW "No matter what you have yet to do, you recharge your batteries at the appointed time. And when you get back to work you'll be ready for come what may."
    show BBW neutral
    BBW "The important thing is that you practice self-care."
    MC "But do you think your life can be so finely planned that you can say 'Now is the time when I will relax'?"
    BBW "I believe in structure, just as a general principle."
    BBW "As you said, life doesn't try to accommodate our plans, so it's on us to make our plans work."
    MC "And you don't think that gets too rigid?"
    BBW "Not at all. I've lived by this for years, and it's served me well."
    show BBW haughty
    BBW "Then again, I do have the benefit of knowing where I'm going in life. It makes it easier to think long-term and, working backwards, in the short term."
    show BBW happy
    BBW "But anyone can be determined and focused if they put a little effort in."
    BBW "Just visualize what you want, divide the path between 'here' and 'there' into manageable tasks, and go after it bit by bit."
    MC "Heh. You sound like a self-help guru."
    show BBW neutral
    BBW "Do I? I suppose I've listened to enough of those kinds of presentations."
    BBW "Life coaches and motivational speakers get a lot of business among the upper echelons of the corporate world."
    BBW "I guess I've picked up some of that that stuff here and there. It's all crept into my brain."
    "I took another bite of my food to give myself a moment to think."
    "I wanted to say that what worked for Alice wouldn't work for everyone, but I couldn't pin down the fault in her argument."
    menu:
        "I can see the logic behind it.":
            jump BBW027_c1_1
        "Do you actually buy it?":
            jump BBW027_c1_2

label BBW027_c1_1:
    MC "I can see the logic behind it."
    MC "The need to take things slow now and then, the importance of focusing."
    MC "I guess I just need to get serious about all this."
    MC "I should have expected the courses to get harder now, and I knew working for you was going to require time and energy."
    BBW "It's not all unmanageable, though."
    BBW "You just have to step it up."
    BBW "Though if your workload gets to be too much, let me know. I can try to hire someone else to help out."
    MC "Oh, no. It's not too much. It's just... a lot."
    show BBW happy
    BBW "If you say so."
    "She looked at her watch."
    BBW "I need to go. The swim team should be done with the pool now, so I'm going to get my workout in."
    BBW "Good luck with everything, Keisuke."
    MC "Yeah, thanks."
    "When she was gone I turned back to my textbook."
    "None of the information seemed to be getting through, so I closed it and turned my attention to my dinner."
    "And for a while after I was done I just sat there, thinking."
    "Next thing I knew, half an hour had passed."
    MCT "Crap! That's exactly what she said not to do. I got nothing done."
    jump daymenu

label BBW027_c1_2:
    MC "Do you actually buy it?"
    "Alice blinked."
    BBW "What do you mean 'buy it?'"
    MC "That it's as easy as... how do I put it? Partitioning everything."
    MC "This is when I work, this is when I play, this is when I get romantic."
    BBW "If you know what you want-"
    MC "Yeah, yeah. You said that."
    MC "'If you know what you want' you can work towards it."
    MC "But that's obvious, isn't it? And it's not always as simple as looking off in the distance and then walking there."
    MC "You'll hit roadblocks, you'll have to take detours."
    MC "Or maybe something more important turns up."
    MC "How do you plan for something like love, for instance?"
    "Alice's expression sort of set. I had given her pause."
    MC "You can't schedule the moment you fall in love. You can't really plan for a major fight-"
    MC "Well, you can try to plan how you would react. Tell yourself not to get heated or say anything out of bounds."
    MC "But when the moment arrives? That'll be when emotion takes over, not logic."
    MC "And if we look at the long term, something like marriage or parenthood could really disrupt your life plans."
    "I stopped at that point, because I could see Alice trying to grapple with what I had said."
    "I guess she didn't have an answer at the ready for this."
    "After a moment she responded."
    BBW "The question of children isn't that hard to deal with. Contraceptives and other things can prevent an unwanted pregnancy."
    BBW "And even if you plan for a child, that is a potential Pandora's Box of issues."
    "She closed her eyes and sighed."
    BBW "But I already said that if you're prepared, you can handle the unexpected."
    BBW "I accept the unexpected will happen. I just don't accept that I have to lay out the welcome mat for it."
    "She looked at her watch."
    BBW "I need to go. The swim team should be done with the pool now, so I'm going to get my workout in."
    BBW "We can continue the conversation later, if you want."
    show BBW happy
    BBW "In the meantime, good luck handling your homework and everything."
    MC "Yeah. Have fun."
    "As she walked off I finished my dinner."
    "I tried to also continue with the science reading, but I saw right away it wasn't going to stick."
    "Alice had been right about the need to slow down at times."
    "I still didn't know about how much one could plan ahead for themselves, but I wasn't about to solve the problem anytime soon."
    "After I was done eating I stayed there for a moment, letting my mind unwind."
    "Then, before too long, I bussed my table and left. Back to the grindstone."
    jump daymenu

label BBW028:
    scene Dorm Interior with fade
    "Whether I was ready or not, my first date with Alice had come."
    "It was easy - terrifyingly easy - to be intimidated by her. She was rich, she was used to the finer things, she was a bit... forceful in personality."
    "When I was trying to get to sleep last night, my stomach fluttering like I was in junior high or something, I reassured myself that she must be at least a little open to this."
    "I can't imagine she's ever had trouble saying 'No,' so I wouldn't be here if there wasn't at least a chance."
    MCT "Too late for second-guessing, my man. Let's get this going."
    scene Gate Front with fade
    MC "Alice! Hey!"
    show BBW surprised with dissolve
    "She cocked an eyebrow at my informal 'Hey.'"
    MCT "Right. Gotta be a bit more polished."
    MC "I mean, it's lovely to see you."
    show BBW happy
    BBW "Thank you. You look handsome yourself."
    MC "Uh, thanks."
    MCT "Just a clean shirt and ironed pants. I guess changing out of my uniform made more of an impact that I expected."
    MCT "Or is she just being polite?"
    MCT "Damn it, don't overthink everything."
    MC "Shall we be off?"
    BBW "We shall. What do you have planned?"
    "Such an easy question, but I had spent the past few days agonizing over it."
    "Alice has expensive tastes, but I'm not the guy to meet them."
    "Going over my meager savings, plus what I had scraped together working for her, I had enough for a nice meal out at what the town had in the way of an upscale restaurant."
    "It would make a good first date, but I couldn't take her back anytime soon."
    "On the other hand, if I was more economic I could stretch my money further and take her out more often. Just not to the costlier places."
    MC "I thought about it, and I figured why not..."
    menu:
        "Some place cozy? Stop at a cafe and then a stroll around the town.":
            $setFlag("BBW028_cafe")
        "Something special? Reservations at the restaurant in town.":
            $setFlag("BBW028_restaurant")
    BBW "Sounds delightful."

    scene Hill Road with fade
    show BBW happy
    "We decided to walk to town instead of waiting for the bus. The weather was accommodating and this would give us a chance to talk."
    "Only at first we couldn't think of anything to talk about except classes and papers coming due."
    BBW "I wanted to say, you've been really great with your deliveries."
    BBW "Repeat business is currently 16% above the rate of equivalent companies, and that might be due to our monopoly-"
    MC "Alice?"
    BBW "?"
    MC "Let's not talk about work today."
    MC "We're not out here as employer/employee, right?"
    show BBW neutral
    "She grimaced a bit, but recovered quickly."
    BBW "You're right. Sorry."
    MC "It's all right."
    MC "..."
    MCT "Damn it, man. Think of something else to talk about."
    MCT "Something to impress her. Maybe talk about the arts, or current events."
    menu:
        "Ask if she's seen the new art film that's playing.":
            MC "Have you heard anything about Autumn Tide? I'm not the biggest fan of costume dramas, but this one looks pretty... intense."
            show BBW happy
            BBW "No, I don't get to the movies that much. What's it about?"
        "Ask what she thinks about the upcoming election.":
            MC "Did you see that analysis about the upcoming election? There's growing expectations that the domestic economy is going to be more of an issue than was first thought."
            show BBW happy
            BBW "I must have missed that. To be frank I don't pay too close attention to Japan's politics."
            MC "It doesn't seem like there're any drastic changes in store for the make-up of parliament, but the LDP might lose a bigger chunk of their majority than first thought..."
    "Having found something not related to school or work to talk about, the rest of the walk to town went by quickly."
    
    scene Town with fade
    show BBW neutral
    "When we got to the town I felt a brief resurgence of dread."
    "Like I needed to make an excuse for how my plans for today couldn't possibly measure up to her normal expectations."
    MC "There's not a lot to do in this town, have you noticed? Not too many places to eat, not much in the way of entertainment."
    BBW "I've noticed."
    BBW "It makes sense, I suppose. Businesses are like plants; they need the right environment to grow and thrive."
    BBW "A niche biome like this island - dedicated to the school and its student body - can only support so much in the way of capital."
    show BBW happy
    BBW "Still, there's something pleasant in the quaintness of it all."
    MC "Yeah..."
    "We walked through the town, the streets not too crowded, and came to..."

    if getFlag("BBW028_cafe"):
        jump BBW028_cafe
    else:
        jump BBW028_rest

label BBW028_cafe:
    scene Cafe with fade
    "The cafe."
    "I had worried the place would be too busy when we got there - having to stand in line for too long or talking over a dozen other conversations would ruin the mood - but the place was mostly empty."
    "We went up to the counter, and as I scanned the menu Alice asked"
    show BBW happy with dissolve
    BBW "What selection of blends do you have?"
    Waitress "I'm sorry, but we only have one kind of coffee."
    Waitress "It's a French roast. It's very good."
    Waitress "And we do have an espresso machine."
    show BBW neutral
    BBW "Coffee is fine."
    MC "I'll have a coffee as well. Do you want a pastry or anything?"
    BBW "Sure. I'll have..."
    "She looked over the display case, her expression souring slightly."
    BBW "I'll have a cheese danish."
    MC "I'll have a chocolate croissant."
    "When the cashier rang us up I reached for my wallet, and at the same time I saw Alice opening her purse."
    "Time slowed down. Should I pay for her order, as is tradition, or should I let her cover her half? She has the money, after all."
    menu:
        "Pay for Alice.":
            MC "It's all right. I got it."
            "To cut her off, I jerked my wallet out and snatched a couple bills. I had to stop and doublecheck them to make sure they were the right amount."
            show BBW happy
            BBW "Nice to see chivalry isn't dead."
        "Let Alice pay for her order.":
            "I moved a little slower as I took my wallet out, giving Alice a chance to open her purse."
            "She stopped before she withdrew her own money, turning to me."
            BBW "Shall we each pay for ourselves?"
            MC "I'm a modern guy, but if you want to do it the old-fashioned way..."
            BBW "No, it's fine."
            BBW "I don't mind paying my own way."
    hide BBW with dissolve
    "We took our coffees and pastries to a corner table in the back."
    "At the last second I remembered to pull her chair out for her."
    show BBW happy with dissolve
    BBW "Oh! Thank you."
    "I'd never done that before on a date, but I didn't think the informal approach would fly with Alice."
    "I wondered if I had scored points for that move, or if she expected something like that."
    show BBW neutral
    BBW "Mmmm. The coffee's not terrible."
    "I took a sip before agreeing."
    "Truth be told, I didn't have a particular taste for coffee, but it was alright."
    BBW "Still, you would expect a cafe to have some variety of choice."
    MC "Do you have a favorite type of coffee?"
    show BBW happy
    BBW "I'm rather fond of Sumatran blends. And I do enjoy some Guatemalans."
    BBW "Oh! There's an idea."
    BBW "We can start selling exotic coffee blends through our company."
    MC "Alice..."
    "I put as much 'stern' into my voice as I could manage."
    show BBW neutral
    BBW "Sorry. No business."
    "She took another sip of her coffee, and I did likewise."
    "I tried to think of something else to talk about. Something neutral."
    "Dates are supposed to be the time to get to know the other person, right? Anything should be on the table."
    "I eventually settled on the most mundane thing."
    MC "How's your danish?"
    BBW "It's also not bad."
    MC "But not what you're used to?"
    BBW "I wouldn't put it that way."
    BBW "I am accustomed to more enticing fare, but I don't lack the stomach for the simple."
    BBW "It doesn't speak well for the owners of this place, though. Having the market cornered is no excuse for mediocre offerings."
    BBW "I've seen other examples of this, monopolization leading to a drop in quality."
    MC "Sounds like you don't approve."
    MC "I guess because you enjoy the finer things you want other people to experience them to?"
    show BBW happy
    BBW "Exactly!"
    BBW "I mean, there are some things where scarcity is unavoidable, in which case only those who appreciate it should enjoy it."
    BBW "But fine food isn't the same as an unspoiled beach."
    MC "But isn't the talent or knowledge to make a high-class dish scarce? There are only so many people who go to cooking schools."
    "Our conversation went on from there."
    "Alice argued that if people demanded better cuisine there would be more of a market for real restaurants, not fast food places. And I brought up things like the need for quick-service food that was affordable."
    
    scene Town with fade
    #time = dusk
    show BBW neutral
    "The conversation ran off on its own tangents from there. Even when we were done with our food we were still chatting as we left the cafe and started walking around the town."
    "I don't know about Alice, but I didn't realize how late it was getting until the streetlamps turned on."
    jump BBW028_afterdate
                          
label BBW028_rest:
    scene Restaurant with fade
    "The restaurant."
    "I had worried the place would be too busy when we got there - even though it was still early, I didn't want to have to compete with a dozen other conversations - but the place was mostly empty."
    "There was a podium just inside the entrance, though not a full-time hostess."
    "A waitress greeted us, I gave her my name, and she showed us to a table."
    "At the last second I remembered to pull Alice's chair out for her."
    show BBW happy
    BBW "Oh! Thank you."
    "I'd never done that before on a date, but I didn't think the informal approach would fly with Alice."
    "I wondered if I had scored points for that move, or if she expected something like that."
    "As we looked over our menus Alice chuckled quietly."
    MC "What?"
    BBW "Oh, it's just..."
    BBW "I haven't seen many Italian restaurants in Japan, and when I first noticed this place I was surprised."
    BBW "But then I guessed it was only the decor, everything designed to give it an Italian flavor."
    BBW "And indeed, the menu is pan-European, with what looks like the American version of group-sized pizzas."
    MC "Oh."
    BBW "I can see why they do it this way."
    BBW "A uniform motif for the restaurant itself is more professional than something more... schizophrenic."
    BBW "You wouldn't believe how chaotically some of the restaurants in America are decorated."
    MC "I guess with the menu their thinking is 'There aren't that many choices in town.' Variety only helps there."
    BBW "Perhaps."
    MC "Not that many people would be upset that an Italian restaurant has..."
    "I struggled to think of something from French cuisine."
    MC "... French bread."
    BBW "No. Though under any other circumstances I would have very high expectations for their alfredo sauce."
    BBW "As simple as it is, it's a favorite of mine."
    BBW "There was one time, a few years ago, when we were in Tuscany..."
    "I thought she was about to go into an anecdote, but as she gazed off into the distance her eyes suddenly went wide."
    BBW "Oh! I just thought of something perfect."
    BBW "Have you ever heard of DeLuca candies?"
    MC "No. What are they?"
    BBW "They're these hard candies made in Italy, with a gooey center. They come in different fruit flavors."
    BBW "They're really good, and they're really popular over there, but I've never seen them outside of Italy."
    BBW "What if we started selling them here?"
    "I did my best to silently scold her, trying to recreate the same look my mother would give my sister or me whenever we were skating on thin ice."
    "She got the hint."
    show BBW neutral
    BBW "Right. Sorry. No work today."
    "Before either of us could help the conversation recover from that moment of awkwardness, our waitress arrived."
    "We took a moment to decide on our orders, and then we were left alone again."
    MC "So you've been to Italy."
    show BBW happy
    BBW "My father's business took him there, so he brought Mom and me and turned it into a vacation."
    "She didn't need much prodding to keep going, and until our food arrived she told me about hiking through Tuscany and the canals of Venice."
    "I found my paella to be pretty good. I didn't have any frame of reference to compare it to."
    "But Alice wasn't that impressed with her linguine in alfredo sauce."
    MC "Is your food okay?"
    show BBW neutral
    BBW "It's fine. Exactly what I was expecting, if that doesn't sound too critical."
    MC "Just not what you're used to?"
    BBW "I wouldn't put it that way."
    BBW "I am accustomed to more enticing fare, but I don't lack the stomach for the simple."
    BBW "It doesn't speak well for the owners of this place, though. Having the market cornered is no excuse for mediocre offerings."
    BBW "I've seen other examples of this, monopolization leading to a drop in quality."
    MC "Sounds like you don't approve."
    MC "I guess because you enjoy the finer things you want other people to experience them to?"
    show BBW happy
    BBW "Exactly!"
    BBW "I mean, there are some things where scarcity is unavoidable, in which case only those who appreciate it should enjoy it."
    BBW "But fine food isn't the same as an unspoiled beach."
    MC "But isn't the talent or knowledge to make a high-class dish scarce? There are only so many people who go to cooking schools."
    "Our conversation went on from there."
    "Alice argued that if people demanded better cuisine there would be more of a market for real restaurants, not fast food places. And I brought up things like the need for quick-service food that was affordable."
    
    scene Town with fade
    #time = dusk
    show BBW neutral
    "The conversation ran off on its own tangents from there. We were still chatting as we left the restaurant, and I would have enjoyed just walking around the town and talking."
    "But I hadn't realized how late it was. Right as we stepped into the fresh air the streetlamps all turned on."
    jump BBW028_afterdate

label BBW028_afterdate:
    MC "Oh, wow. It's almost night."
    MC "We should probably get back to campus, huh?"
    show BBW angry
    BBW "Yes. We wouldn't want the day spoiled being chewed out by Madame Presidente."
    menu:
        "Agree with Alice":
            MC "Yeah. Sticklers like her have a tendency to squash other people's fun, even if they don't mean to."
        "Defend Shiori":
            MC "Shiori's not the worst stickler I've ever met. I'd say she's reasonable most of the time."
    show BBW neutral
    BBW "Quite."
    show BBW happy
    BBW "Still, if not her then one of the teachers might come down on us. Let's not give them the excuse."
    "We headed back to campus, our conversation dying down as we took in the twilight."
    MC "The island isn't that developed, other than the school and town."
    BBW "No."
    MC "I haven't seen this much nature in one place in... Don't know how long."
    MC "Probably when I went camping as a kid."
    BBW "There's a forest in southern-"
    "And suddenly Alice was falling towards me."
    "I caught her... Or rather, when she fell against me I braced myself and kept us from both sprawling on the ground."
    show BBW angry
    BBW "Sorry. There was a rock..."
    MC "Are you hurt?"
    BBW "No, just..."
    "I helped her stand back up, suddenly aware of my arm reaching around her back."
    "She felt soft, like I expected, but also a little bit firm."
    MCT "I wonder what she'll say if I don't move my arm."
    menu:
        "Leave the arm there.":
            MC "Can you stand? You didn't sprain your ankle or anything, did you?"
            show BBW neutral
            BBW "No, I'm not hurt."
            "Tentatively, she put her weight on both legs. She seemed fine."
            show BBW happy
            BBW "I think I'll be fine on my own."
            "The way she smiled I could see she wasn't bothered by my being so close. But I guess she didn't want to get too familiar on the first date."
            "So I stepped back, returning the smile and (hopefully) not coming across as a creep."
        "Give her space.":
            "I stepped back slowly, making sure she wasn't about to fall again."
            MC "Can you stand? You didn't sprain your ankle or anything, did you?"
            show BBW neutral
            BBW "No, I'm not hurt."
            "Tentatively, she put her weight on both legs. She seemed fine."
    show BBW happy
    BBW "Sorry about that."
    MC "No worries."
    BBW "Now and then I feel a little out of sync with my own body."
    show BBW neutral
    BBW "There's a bit more of me than I'm used to."
    MC "Right."
    menu:
        "Compliment her body.":
            "Even if she wasn't fishing for a compliment, there was no better opening to talk boldly about her weight."
            "It was one of the biggest worries on my mind leading up to tonight, and I have put more than a little thought into how I would seize the opportunity."
            MC "I have to say, you're carrying it well."
            MC "You're still undeniably elegant, no matter your size."
            "Admittedly, it came across as more suave in my own mind."
            "But when she rolled her eyes she also smirked a little, so I hadn't flubbed it too bad."
            show BBW happy
            BBW "Flatterer."
            BBW "But is that what you really think? You're not just feeding me a line?"
            MC "No, I mean it."
            BBW "Uh-huh. And how elegant was I when I was falling onto you?"
            MC "Well... OK, you were clumsy just then."
            MC "But I'm not about to complain about feeling you pressed against me like that."
            show BBW surprised
            BBW "!"
            "That was bolder than I was planning, but it was worth it to see Alice stunned like that."
            "She recovered quickly, though. No surprise."
            show BBW happy
            BBW "That's more than flattery."
            BBW "But it's also the right thing to say."
        "Ask how she's managing with her extra weight.":
            MC "Are you... gaining weight faster than you can manage?"
            BBW "Not quite."
            BBW "I've been told my body will acquire muscle a bit easier than most people, if only from carrying around all this weight."
            BBW "I simply need to stay dedicated to my workout routine."
            MC "That's good."
            MC "I do have to say, I think you look quite nice with your extra curves."
            MCT "D'oh."
            "This had been one of my biggest concerns for today, the subject of Alice's body."
            "I had tried to think of just the right thing to say to get across that I find her attractive - sexy, even - at her current size."
            "This wasn't how I had planned it, though. 'Quite nice'?"
            "Maybe I should have gone with stunning, like I had thought of first."
            
    scene Dorm with fade
    show BBW neutral
    "We finished the return trip in relative silence."
    "I walked Alice to the girl's dorm, and would have offered to walk her to her room if Shiori wasn't in sight."
    MC "Guess this is where we call it a night."
    show BBW happy
    BBW "Looks like."
    BBW "I had a good time, Keisuke. Aside from the near-tumble."
    BBW "I'd love to do this again. Soon."
    MC "Sure!"
    "For the last time that night I told myself to calm down."
    MC "Yeah. I'd like that."
    "I watched her go into the girls' dorm, then casually made my way back to my room."
    "Well past midnight I was lying in bed, replaying the date in my head."
    "Had I done the right things, said the right things? Had her view of me changed in any dramatic way?"
    "What should I do differently next time? Be more bold? Play it cool?"
    "Eventually I told myself I could figure it out later. For now I needed sleep."
    jump daymenu

label BBW029:
    $setProgress("BBW", "BBW029")
    scene Cafeteria with fade
    play music Schoolday
    "I timed my dinner for when I expected Alice would be here, but her usual spot was empty."
    MCT "Oh, right. Music club practice."
    MCT "Well, I’m already here. Guess I’ll grab some grub for myself."
    "I had a nice meal - nice as far as the cafeteria food went - and as I was finishing up Alice appeared on the scene."
    MC "Hey, Alice. How’s the music club treating you?"
    show BBW neutral with dissolve
    BBW "It’s fine. Just fine. It meets my expectations."
    MC "Uh-oh. You’re not fighting with the president again, are you?"
    BBW "No. She and I have an accord. My previous criticisms, while still on the record, notwithstanding."
    BBW "But it is a struggle to keep my peace when she seems committed to watering down our collective effort so thoroughly."
    BBW "Just look at these fliers she’s produced for our first concert."
    "She handed me a small stack of blue pages announcing a performance the following weekend."
    "I couldn’t see Alice’s complaint at first, until I tried to look at it from her perspective."
    MC "They’re kind of plain."
    show BBW angry
    BBW "They are practically designed to be ignored!"
    show BBW neutral
    BBW "I’m supposed to post these around the campus, next to all the other bills for every other club or gathering."
    BBW "If the auditorium is even a quarter full with this as our advertising campaign it would be astounding."
    BBW "It’s a waste of my time to put them up in the first place."
    MC "Maybe you could redo these. Make them better."
    BBW "If I had the time…"
    if getSkill("Art") >= 7:
        MC "I could do it for you."
        BBW "Could you?"
        MC "It wouldn’t be anything too fancy, but give me an hour in the computer lab and I can make something a little more eye-catching."
        show BBW happy
        BBW "That would be nice."
        BBW "Could you do it now? I said I would put them up tonight."
        MC "Sure. I’ll bring the finished ones to your room."
        BBW "This is a big help, Keisuke. Here, take these with you so you have the info."
        "She handed me the stack of original fliers."
        scene Hallway with fade
        "The computer lab was busy, but I found an open station and got to work."
        "I didn’t spend too long on it, just copying the info from the original fliers and changing the fonts to make them pop."
        "Add a few flourishing patterns in the corners and bold the showtime to have it stand out, and it was a marked improvement over the original."
        "I printed out 50 copies and took them to Alice’s dorm."
        show BBW happy with dissolve
        $setAffection("BBW", 1)
        BBW "Oh, these are much better."
        BBW "I still have time to hang them up tonight. Care to join me?"
        MC "Sure. It’s a nice night."
        "We walked all over the campus, Alice taping up the fliers as we chatted."
        "It wasn’t what I would call ‘romantic,’ but in its own simple way it was nicer than some dates I’d had."
        jump daymenu
    BBW "As it is, I already have too much on my plate."
    "She looked at her watch and sighed."
    BBW "Could I ask a favor of you? Could you do this for me?"
    BBW "Just post them at all the regular announcement boards and in the halls."
    menu:
        "I guess I can do it.":
            jump BBW029_c1_1
        "I have my own work to do.":
            jump BBW029_c1_2
        "I can’t do it for you, but I can help." if getAffection("BBW") >= 14: #(If affection score is > / = 14; +1 affection)
            jump BBW029_c1_3
        "I can’t do it for you, but I can help. (disabled)" if getAffection("BBW") < 14:
            pass

label BBW029_c1_1:
    MC "I guess I can do it. It won’t take long, will it?"
    BBW "Not if you work fast."
    BBW "Thanks. Here you go."
    "And she unceremoniously dropped the stack on the table in front of me, then walked away."
    scene Hallway with fade
    "As I walked around the campus I couldn’t fight the feeling that I had given in too easily."
    "She had said ‘Thanks,’ but her tone…"
    "Maybe I was imagining it, but she had sounded like my saying ‘Yes’ was a given. Like she was entitled to my help."
    "It didn’t stop me from doing the job, but I made myself a promise that next time I wouldn’t roll over right away."
    jump daymenu

label BBW029_c1_2:
    MC "Sorry, but I have my own work to do."
    MC "Not club stuff, but homework, essays, you know."
    BBW "I understand."
    BBW "And the job was given to me, after all."
    MC "On another day I could help."
    BBW "I get it."
    BBW "I guess I need to start on this now, if I’m going to have time to look over our sales figures tonight."
    if getAffection("BBW") >= 10:
        BBW "I’ll see you around."
    else:
        BBW "I'll see you in class, Hotsure-san."
    "And she left."
    hide BBW
    "She didn’t sound angry, at any rate. That was good."
    jump daymenu

label BBW029_c1_3:
    MC "I can’t do it for you, but I can help."
    "She considered it for a second, then nodded."
    show BBW happy
    BBW "That would be appreciated."
    BBW "It won’t take as long this way."
    scene Hallway with fade
    "We walked all over the campus, Alice taping up the fliers as we chatted."
    "It wasn’t what I would call ‘romantic,’ but in its own simple way it was nicer than some dates I’d had."
    jump daymenu

label BBW030:
    "This marks the current end of Alice's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance
