define PRG = Character('Kodama', color="#FF3399", what_prefix='{size=-6}', what_suffix='{/size}')
define Sakura = Character('Sakura', color="#FF3399")
define Announcer = Character('Announcer', color="#C0C0C0")
define PRGCell = Character('Kodama', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define fade = Fade(0.5, 0.0, 0.5)

image PRG neutral = DynamicImage("Graphics/PRG/[prgsize]/neutral.png")
image PRG happy = DynamicImage("Graphics/PRG/[prgsize]/happy.png")
image PRG sad = DynamicImage("Graphics/PRG/[prgsize]/sad.png")
image PRG surprised = DynamicImage("Graphics/PRG/[prgsize]/surprised.png")
image PRG angry = DynamicImage("Graphics/PRG/[prgsize]/angry.png")
image PRG aroused = DynamicImage("Graphics/PRG/[prgsize]/aroused.png")
image PRG unique = DynamicImage("Graphics/PRG/[prgsize]/unique.png")

image Dorm PRG Day = "Graphics/ui/bg/PRGdorm_day.png"
image Dorm PRG Eve = "Graphics/ui/bg/PRGdorm_eve.png"
image Supermarket = "Graphics/ui/bg/NYI.png"

init 2 python:    
    #Core
    eventlibrary['PRG001'] = {"name": "A Bun Tasting", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,            "location": "cafeteria",       "priority": PrioEnum.NONE, "next": "PRG003", "obsflags": [],           "conditions": []}
    eventlibrary['PRG003'] = {"name": "An Inviting Aroma", "girls": ["PRG"], "type": EventTypeEnum.CORE,               "location": "classroom",       "priority": PrioEnum.NONE, "next": "PRG008", "obsflags": [],           "conditions": []}
    eventlibrary['PRG008'] = {"name": "Cups and Measurements", "girls": ["PRG"], "type": EventTypeEnum.CORE,           "location": "classroom",       "priority": PrioEnum.NONE, "next": "PRG009", "obsflags": [],           "conditions": []}
    eventlibrary['PRG009'] = {"name": "Handling with Change", "girls": ["PRG"], "type": EventTypeEnum.CORE,            "location": "campuscenter",    "priority": PrioEnum.NONE, "next": "PRG012", "obsflags": [],           "conditions": []}
    eventlibrary['PRG012'] = {"name": "Archetypes", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                "location": "classroom",       "priority": PrioEnum.NONE, "next": "PRG013", "obsflags": [],           "conditions": []}
    eventlibrary['PRG013'] = {"name": "Competitive Spirit", "girls": ["PRG"],"type": EventTypeEnum.CORE,               "location": "classroom",       "priority": PrioEnum.NONE, "next": "PRG014", "obsflags": [],           "conditions": []}
    eventlibrary['PRG014'] = {"name": "Cozy Lunch Time", "girls": ["PRG"], "type": EventTypeEnum.CORE,                 "location": "cafeteria",       "priority": PrioEnum.NONE, "next": "PRG015", "obsflags": [],           "conditions": []}
    eventlibrary['PRG015'] = {"name": "Nurturing", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "dormBBW",         "priority": PrioEnum.NONE, "next": "PRG016", "obsflags": [],           "conditions": []}
    eventlibrary['PRG016'] = {"name": "The First Step", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "classroom",       "priority": PrioEnum.NONE, "next": "PRG017", "obsflags": [],           "conditions": []}
    eventlibrary['PRG017'] = {"name": "Slowly Blooming", "girls": ["PRG"], "type": EventTypeEnum.CORE,                 "location": "schoolplanter",   "priority": PrioEnum.NONE, "next": "PRG019", "obsflags": [],           "conditions": []}
    eventlibrary['PRG019'] = {"name": "Seconds Please", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,           "location": "classroom",       "priority": PrioEnum.NONE, "next": "PRG020", "obsflags": [],           "conditions": []}
    eventlibrary['PRG020'] = {"name": "Scheduling Conflict", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,      "location": "dorminterior",    "priority": PrioEnum.NONE, "next": "PRG021", "obsflags": [],           "conditions": []}
    eventlibrary['PRG021'] = {"name": "Practice Makes Perfect", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,   "location": "cafeteria",       "priority": PrioEnum.NONE, "next": "PRG022", "obsflags": [],           "conditions": []}
    eventlibrary['PRG022'] = {"name": "Grocery Run", "girls": ["PRG"], "type": EventTypeEnum.CORE,                     "location": "supermarket",     "priority": PrioEnum.NONE, "next": "PRG023", "obsflags": [],           "conditions": []}
    eventlibrary['PRG023'] = {"name": "Invaluable Research", "girls": ["PRG"], "type": EventTypeEnum.CORE,             "location": "library",         "priority": PrioEnum.NONE, "next": "PRG024", "obsflags": [],           "conditions": []}
    eventlibrary['PRG024'] = {"name": "Flicker", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "dorminterior",    "priority": PrioEnum.NONE, "next": "PRG025", "obsflags": [],           "conditions": []}
    eventlibrary['PRG025'] = {"name": "House Call", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "dorminterior",    "priority": PrioEnum.NONE, "next": "PRG026", "obsflags": [],           "conditions": []}
    eventlibrary['PRG026'] = {"name": "Here Nor There", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dormPRG",         "priority": PrioEnum.ALL, "next": "PRG027", "obsflags": [],            "conditions": []}
    eventlibrary['PRG027'] = {"name": "The Morning Routine", "girls": ["PRG"], "type": EventTypeEnum.CORE,             "location": "dormPRG",         "priority": PrioEnum.NONE, "next": "PRG028", "obsflags": [],           "conditions": []}
    eventlibrary['PRG028'] = {"name": "Flipping Lids", "girls": ["PRG"], "type": EventTypeEnum.CORE,                   "location": "cookingclassroom", "priority": PrioEnum.NONE, "next": "PRG029", "obsflags": [],          "conditions": []}
    eventlibrary['PRG029'] = {"name": "Aida end", "girls": ["PRG"], "type": EventTypeEnum.CORE,                        "location": "library",         "priority": PrioEnum.NONE, "next": "", "obsflags": [],                 "conditions": []}
    eventlibrary['PRGend_nofather'] = {"name": "Aida end", "girls": ["PRG"], "type": EventTypeEnum.CORE,               "location": "library",         "priority": PrioEnum.NONE, "next": "", "obsflags": [],                 "conditions": []}

    #Optional
    eventlibrary['PRG001b'] = {"name": "Tongue Twister", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                 "location": "schoolexterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["testday"],    "conditions": []}
    eventlibrary['PRG004'] = {"name": "Mother Nature", "girls": ["PRG", "FMG"], "type": EventTypeEnum.OPTIONAL,            "location": "track",           "priority": PrioEnum.NONE, "next": "", "obsflags": [],             "conditions": []}
    eventlibrary['PRG006'] = {"name": "Double Stacked", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                  "location": "campuscenter",    "priority": PrioEnum.NONE, "next": "", "obsflags": [],             "conditions": []}
    eventlibrary['PRG007'] = {"name": "A (Soft) Wall to Hide Behind", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,    "location": "cafeteria",       "priority": PrioEnum.NONE, "next": "", "obsflags": [],             "conditions": []}
    eventlibrary['PRG011'] = {"name": "Homerun!", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                        "location": "classroom",       "priority": PrioEnum.NONE, "next": "", "obsflags": [],             "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['PRG018'] = {"name": "A Small Touchup", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                 "location": "campuscenter",    "priority": PrioEnum.NONE, "next": "", "obsflags": [],             "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['PRG026b'] = {"name": "", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                               "location": "classroom",       "priority": PrioEnum.ALL, "next": "", "obsflags": [],              "conditions": [[ConditionEnum.TIMEFLAG, "size3"], [ConditionEnum.NOROUTELOCK, "PRG"], [ConditionEnum.NOROUTELOCK, ""]]}
    
    eventlibrary['PRG005'] = {"name": "Hold on Tight", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,               "location": "auditorium",      "priority": PrioEnum.GIRL, "obsflags": ["aftertest"],              "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}    
    eventlibrary['PRG010'] = {"name": "Rapidly Curvy", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,               "location": "cookingclassroom", "priority": PrioEnum.GIRL, "obsflags": ["aftersize2"],            "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}

label PRG001b:
    scene School Exterior with fade
    play music Sunset
    "On my way to the vending machines for a drink, I spied Aida-san from my class, frowning down at a can of tea."
    show PRG sad with dissolve
    "Her worried look made me think back to that first morning with Tashi-Sensei, and how she'd reacted to his tongue."
    "While most students had been shocked, disgusted, or morbidly interested in the meter-long appendage, Aida had covered her face in her hands and slunk down in her seat like she was trying to hide from it."
    "Maybe she was still trying to work through it? I decided to go talk to her."
    MC "Hey, Aida?"
    show PRG surprised
    PRG "Ah! Oh, sorry, do you need me to move?"
    MC "No, I just wanted to see how you were doing."
    PRG "M-Me?"
    MC "After that first speech in class...you didn't seem to take it very well."
    show PRG aroused
    PRG "Oh... I hoped no one had noticed. Please, don't concern yourself over it."
    menu:
        "Are you sure?":
            jump PRG001_a
        "You should talk about stuff if it bothers you.":
            jump PRG001_b
        "You can tell me, I promise I won't tell anyone.":
            jump PRG001_c

label PRG001_a:
    MC "Are you sure? You seemed pretty upset."
    show PRG neutral
    PRG "I, it's fine, really. Don't concern yourself over it, please."
    MC "Well... Okay, if you're sure..."
    "Aida nodded stiffly and turned away, cradling her tea even closer to herself as she stared at the floor. Being private was one thing, but she looked like a snail trying to tuck itself inside its shell..."
    jump daymenu
   
label PRG001_b:
    MC "You should talk about stuff if it bothers you, Aida..."
    PRG "I...It's fine, really."
    MC "No one makes a face like you made if they're fine. It's okay, everyone was put off by Tashi-sensei's tongue that first time."
    show PRG neutral
    "Aida twiddled her thumbs on the front of her can, looking back down at the ground to one side of me and then the other, before finally looking at me. Well, looking at my stomach, at least, seemingly unwilling or able to look at my face."
    PRG "But... You didn't go to everyone, did you?"
    MC "Well... no. But you seemed to be the most affected."
    show PRG sad
    PRG "Sigh... Well, I'm sorry. I'll try not to make you worry like that in the future."
    MC "Aida, it's not like that..."
    PRG "Thank you for your concern, Hotsure-san."
    hide PRG with dissolve
    "Aida quickly turned and walked away at a brisk pace, tucking her head down towards her chest."
    MCT "Sometimes I just don't understand women..."
    jump daymenu
    
label PRG001_c:
    MC "You can tell me, I promise I won't tell anyone."
    PRG "You...you promise?"
    MC "Absolutely."
    PRG "Well..."
    show PRG neutral
    PRG "I didn't think... I mean, I was wondering why they'd offer me a place here, because I'm nothing special, but I didn't think it would be anything like this."
    PRG "I-I'm an only child, so that means...Tashi-sensei said I was going to change."
    MC "Scared, huh?"
    "Aida nodded, her hands tightening around her tea can enough to make it crinkle a bit."
    MC "Right. I guess it's like he said. They can help us, but they can't give us resolve."
    PRG "...That's what I'm afraid of."
    MC "I guess we're in the same boat, then."
    show PRG surprised
    PRG "Oh, no! I didn't mean you! Just...I'm so sorry! Please don't be mad I said that!"
    PRG "I'm sure whatever it is that's different about you won't be bad at all..."
    MC "Well, it could even be good, you know? Think about it this way. Is there anything about yourself you'd want to change?"
    show PRG neutral
    PRG "..."
    PRG "..."
    show PRG angry
    PRG "..."
    show PRG sad
    PRG "..."
    PRG "..."
    PRG "...Lots of things."
    MC "So that means change doesn't have to be bad, right? What if it's something you wanted to have happen?"
    PRG "..."
    show PRG neutral
    PRG "...You know... well, my luck is pretty bad..."
    MC "Maybe, but someone has to get the lucky fortunes at the shrine, right?"
    PRG "But... Well..."
    show PRG happy
    PRG "You know, you're right. Maybe... Maybe this won't be so bad after all."
    "Aida finally looked up at me, and though I could still see the worry plastered across her face, there was at least a hint of hope in her eyes."
    PRG "Thank you, Keisuke!"
    MC "Glad I could help!"
    hide PRG with dissolve
    "And with that she was on her way again, though I thought about the conversation for a few minutes afterwards. What {i}was{/i} going to change about me?"
    $ setAffection("PRG", 2)
    jump daymenu
    
label PRG001:
    $setProgress("PRG", "PRG003")
    scene Cafeteria with fade
    play music Schoolday
    "I felt hungrier than usual today, so I stopped by the cafeteria for an extra snack. I had just finished my red bean bun when I spied Aida coming in the door near where I was sitting."
    show PRG neutral at Position(xpos=0.65) with dissolve
    MC "Hi there, Kodama-san!"
    PRG "Oh! Ah, h-hello Hotsure-san."
    MC "How are you today?"
    PRG "Oh, I'm fine. Just getting Alice-san's between-meal snack."
    MC "I thought you were cooking for her?"
    PRG "Meals, yes, but for snacks she usually prefers something sweet and pre-made. I'm supposed to get a bunch of sweets so she can figure out what she likes..."
    "I used a tissue to wipe up any residual crumbs and threw my trash in the can."
    MC "Well, I'll wait in line with you, how about? Help it go quicker."
    show PRG happy
    PRG "Oh, really? W-well sure, that'd be wonderful!"
    show PRG neutral
    "We spent a few minutes in line, making small talk and getting to know each other better."
    "When we finally got up to the counter, Aida ordered several bean paste buns and a few jelly rolls. Her large bag of pastries in hand, we set out into the cafeteria seating, looking for Alice."
    BBW "Here, Kodama-san."
    PRG "Ah! C-coming!"
    show BBW neutral at Position(xpos=0.25) with dissolve
    "I followed Aida over to the table Alice was sitting at, a small picnic cloth spread over the table and actual silverware set in front of her. Aida quickly set to work opening each of the packaged sweets and setting them out on the picnic cloth in front of Alice."
    BBW "It looks like you did your job satisfactorily. Is this a full selection of the snacks available or did you prioritize some over others?"
    PRG "O-oh, well, um, this was as many as I could a-afford..."
    BBW "Hmm. Keep a record of which ones I am sampling right now. We can repeat this process at a future time, to ensure I am making the most educated decision."
    BBW "Now, which flavor is this?"
    PRG "Uhm, that's the red bean bun."
    MC "I just had one of those, they're good."
    "Alice arched a brow at my comment, but didn't say anything as she cut a generous slice from the middle and popped it in her mouth. I still couldn't believe she was using fancy silverware to eat a bun."
    "After she swallowed she took a sip of water, swishing it around in her mouth."
    BBW "Initial thoughts: strong immediate taste. The texture of the paste was a bit like glue. It stuck to my tongue a bit, but was not troublesome. The pastry was not fluffy in the slightest. Almost mashed down. The aftertaste diminishes quickly."
    BBW "Final verdict: Fair, but not exemplary in any way."
    "I looked over and saw Aida studiously taking notes on a notepad."
    PRG "O-okay, well, the next one here is melon bread..."
    "Again with cutting a piece, tasting, then cleansing her palate."
    BBW "Sweet taste that almost overpowers the fruitiness, perhaps due to whatever preservatives or flavor enhancers are included in this. The bread has the same problem as the red bean sample, thin but dense. Perhaps unavoidable in a mass-produced and distributed product like this. The aftertaste is strong enough to be noted, but not unpleasant."
    BBW "Final verdict: Above average quality."
    "Again Aida took notes, and I just sort of stood there observing as Alice worked her way through the pastries, until I couldn't take the curiosity any longer."
    MC "So... what is this, exactly?"
    BBW "I am familiarizing myself with the different types of snacks available. Like a wine tasting, but appropriate for the school."
    menu:
        "Ask about the food":
            MC "You're not actually going to eat them all?"
            BBW "What, all of this at once?"
            "She indicated the spread of snacks in front of her, which was as much food as a normal meal."
            MC "I see your point. But why go through several at once? Why not buy one, try it, and then buy another later on?"
            BBW "Too time-intensive, plus I do not care to consume an entire snack that is subpar or ill-suited for my sense of taste."
            MC "So what do you do with the rest of it?"
            BBW "Rest of what?"
            MC "Well, you've got most of each bun left, do you give the rest to Aida or something?"
            show BBW happy
            BBW "Why Hotsure-san, what a wonderful idea! That way I won't have to reimburse Aida for the full price."
            MC "..."
            PRG "..."
            BBW "Good thinking, Hotsure-san. Whether it's component manufacturing or one's lunch, excess inventory just wastes money."
            MC "...Glad to help...?"
            $setAffection("BBW", 1)
        "Ask about Aida":
            MC "No, I mean, with Aida. Taking notes and everything."
            show PRG sad
            PRG "Um..."
            MC "I can understand favors, but is... I mean, is she working for you or something? Are you paying her?"
            BBW "Yes, she is being compensated for her time and effort. Why do you ask?"
            MC "Just don't want to see anyone being taken advantage of..."
            MCT "Especially someone as timid as Aida seems to be..."
            BBW "Business is not about taking advantage. Not always, at least. This is a fair and equitable exchange, my money for her labor."
            PRG "P-please, it's okay, I don't mind..."
            MC "..."
            BBW "..."
            BBW "Anyways, on to the next one..."
            show PRG neutral
            MC "I, uh, I should get on my homework. I'll see you around, okay Kodama-san? Alice-san, nice to see you too."
            "Alice simply nodded, her mouth full of food at the moment, and Aida gave me a small but terse smile."
            $setAffection("PRG", 1)
    jump daymenu

label PRG003:
    $setTimeFlag("testday")
    $setProgress("PRG", "PRG008")
    scene F1 Hallway with fade
    play music Busy
    "None of the clubs I was interested in were meeting after class today, so I just wandered the halls after class, watching the other students as they filed out of the building."
    "It was amazing to see all the different sizes and shapes and exaggerations of anatomy leaving out the big double doors, but most of the upperclassmen seemed to have adjusted fairly well."
    MC "...sniff, sniff..."
    MC "Wow, something smells good..."
    "I followed the scent to the end of the hallway, a small room in the corner opposite the stairs beckoning me with its open door. I peeked inside, and who should I find at the home ec stations but mousy, unassuming Aida."
    scene Classroom with fade
    show PRG happy with dissolve
    MC "Hi there, Kodama-san!"
    "I had tried to sound friendly, but she jumped like I'd shouted her name at the top of my lungs."
    show PRG surprised
    PRG "Ah! I'm sorry!"
    show PRG neutral at Position(xpos=0.75)
    PRG "I-is there a club meeting? Am-Am I in the way?"
    menu:
        "No, no one's coming that I know of.":
            jump PRG003_1
        "So you fancy yourself a chef?":
            jump PRG003_2
        "Actually, I was looking for you.":
            jump PRG003_3

label PRG003_1:
    MC "No, no one's coming that I know of..."
    PRG "Oh... Okay..."
    show PRG neutral at center with dissolve
    "Aida turned back to her cooking and I pondered how to work through the ensuing awkward silence."
    MC "So, ah, what's cookin'?"
    PRG "Oh, th-this is for Nikum- I mean, Alice-san. She prefers to be addressed as Alice."
    MC "So she's got you cooking for her, huh? How'd that happen?"
    PRG "W-well, Ni- she- she asked me to."
    MC "...Just out of the blue?"
    PRG "W-well, she said I did a good job cleaning for her, it didn't make sense to have another person just for cooking. A-and I already know how to cook, a little..."
    MC "Cooking {i}and{/i} cleaning? What, does she have you carry her books, too?"
    show PRG sad
    "The way Aida bit her lip and looked down at her saucepan, she didn't even need to say the answer."
    MC "Good grief..."
    menu:
        "...I sure hope she's paying you what you're worth...":
            jump PRG003_1_a
        "...What's she doing that she needs all that help?":
            jump PRG003_1_b
            
label PRG003_2:
    MC "So, you fancy yourself a chef, Kodama-san?"
    show PRG aroused
    "I smiled at her reassuringly, but Aida nevertheless blushed hotly."
    PRG "Oh, I don't know a-about that... I just know, um, how to cook."
    MC "People who just 'know how to cook' don't make smells that can lure people in from halfway down the hall..."
    PRG "Oh, n-no, it's really nothing special..."
    menu:
        "Don't be so modest. You're great.":
            jump PRG003_2_a
        "Well {i}I{/i} think it's something special.":
            jump PRG003_2_b
        "Nothing special? ...Well, I suppose everyone needs a hobby.":
            jump PRG003_2_c

label PRG003_3:
    MC "Actually, I was looking for you, Kodama-san."
    show PRG surprised
    show PRG surprised at center, Transform(xzoom=-1)
    show PRG surprised at Transform(xzoom=1)
    show PRG surprised at center, Transform(xzoom=-1)
    "I don't think Aida could have looked more surprised if I'd told her aliens had just landed."
    show PRG aroused
    PRG "M-me? Why? Did I d-do something wrong?"
    MC "No, I just thought I'd drop by and visit with you for a bit. I like hanging around you."
    "Aida's blush deepened, and she stared intently at her saucepan as she stirred it."
    PRG "B-but all I'm doing is cooking some things..."
    menu:
        "I've always wanted to know more about cooking.":
            jump PRG003_3_a
        "You think you could teach me?":
            jump PRG003_3_b
        "'All you're doing'? That's such an important skill to have!":
            jump PRG003_3_c

label PRG003_1_a:
    MC "...I sure hope she's paying you what you're worth."
    PRG "I... what?"
    MC "Alice. She's paying you, right? She better be."
    PRG "Hotsure-san..."
    MC "I just don't want her taking advantage of you, is all."
    PRG "no, it... it's not like that. She's paying me..."
    MC "How much? Is it even minimum wage?"
    show PRG angry
    PRG "Hotsure-san!"
    "The sharpness of her tone was unfamiliar from the shy, mousey girl, and I halted in my verbal tracks."
    PRG "I-I'm not helpless, Hotsure-san! I-I know... I can m-make decisions for myself, you know..."
    MC "W-well, that's, I'm just-"
    "I didn't even get to finish pulling together a defense before Aida wiped her eyes with the back of one hand and shakily asked me to leave."
    $ setAffection("PRG", -1)
    jump daymenu

label PRG003_1_b:
    MC "...What's she doing that she needs all that help?"
    show PRG neutral
    PRG "Hm?"
    MC "Well, she's got you cooking for her, cleaning for her, doing her errands... what's she doing with all that free time?"
    show PRG happy
    PRG "Oh, so much! After she's done with her schoolwork, she's always reading something, or on the phone, or filling out these complicated-looking forms... Whatever it is, it's big and important and I, I couldn't possibly do any of it."
    "I blinked, expecting the answer to be more along the lines of television and expensive sweets. I guess even busybodies could get fat..."
    MC "Wow, it sounds like she really {i}does{/i} need you."
    PRG "I know! And she's so appreciative! She even pays me!"
    MCT "She should be doing that regardless...?"
    MC "Er, well, good! I'm sure you're worth every penny, if not more."
    show PRG aroused
    "Aida just nodded, embarrassed but happy with the affirmation. We continued to chat as she finished her cooking, before parting as she took it back to the girls' dorms."
    $ setAffection("PRG", 1)
    jump daymenu

label PRG003_2_a:
    MC "Don't be so modest. You're great."
    show PRG sad
    PRG "You... you're just saying that."
    MC "No, I mean it."
    show PRG neutral
    PRG "B-but, when did you ever eat any of my cooking?"
    MC "Er... well, I mean... I haven't, but..."
    show PRG sad
    PRG "...I see."
    MC "Well, hey, something that smells this good can't possibly taste bad, right?"
    PRG "...You don't need to try to make me feel better. It's okay."
    MC "W-well, um... it really {i}does{/i} smell good..."
    PRG "Mm."
    "The way Aida's head hung, I realized I was neck deep in this conversation with no shore in sight. I quickly excused myself and had a long think about how to walk the tightrope of giving Aida Kodama a compliment."
    $ setAffection("PRG", -1)
    jump daymenu

label PRG003_2_b:
    MC "Well, {i}I{/i} think it's something special."
    show PRG surprised
    PRG "R-really?"
    show PRG neutral
    PRG "But... but you've never even tried any of it."
    MC "Well, I don't need it. Look at you, fresh ingredients, staying after school, cooking for a roommate you just met... It almost doesn't matter what it tastes like, if it has so much care put into it."
    pause 1.5
    show PRG happy
    MC "Plus, given that it's what lured me in here, I refuse to believe anything that {i}smells{/i} that good could possibly {i}taste{/i} bad..."
    PRG "Y-you think so?"
    #show PRG aroused
    PRG "Th-thank you, Hotsure-san, that's... y-yes, thank you, thank you very much."
    $ setAffection("PRG", 2)
    jump daymenu

label PRG003_2_c:
    MC "Nothing special? ...Well, I suppose everyone needs a hobby."
    PRG "R-right, a hobby, just, just some things I picked up from home... no need to make a fuss over it..."
    MC "Still, it does smell nice."
    PRG "Well, thank you, Ho-Hotsure-san."
    jump daymenu
    
label PRG003_3_a:
    MC "I've always wanted to know more about cooking..."
    show PRG neutral
    PRG "What... what do you mean?"
    MC "I can boil an egg and make rice and noodles, but I don't know anything about real {i}cooking{/i}, like you're making there."
    PRG "Oh, well... I-I mean, I can tell you some of the stuff I know while I work on Nik- ooooh, darn it!- Alice-san's meal here, i-if you want..."
    MC "I would love that!"
    show PRG aroused
    PRG "Oh, okay, w-well, this odd-looking spoon, that's called a pasta fork, actually. A-and this, this is a ravioli stamp. Alice says she enjoys Italian food, but uhm, a lot of 'Italian' food, like modern pizza, was actually invented in America... Maybe, uhm, inspired by original Italian dishes like Focaccia, but..."
    scene black with fade
    scene Classroom with fade
    show PRG happy at Position(xpos=0.75) with dissolve
    PRG "...And now that it's drained in the, uh, in the strainer, I just need to put some of the alfredo sauce- named after an Italian restaurant owner in Rome- over it and it's ready for Alice."
    MC "Wow, you sure do know a lot, Kodama-san."
    show PRG aroused at center with dissolve
    PRG "I-it's really nothing special..."
    MC "Well, if you say so, but I sure learned a lot. Thanks for letting me hang out with you, hope Alice's happy with her food!"
    show PRG happy
    PRG "R-right! Y-you too, Hotsure-san!"
    hide PRG with dissolve
    "Aida hurried off to her dorm, and I snuck a ravioli from the strainer before she returned."
    MCT "Wow, she really {i}is{/i} good..."
    $ setSkill("Art", 1)
    $ setAffection("PRG", 1)
    jump daymenu
    
label PRG003_3_b:
    MC "You think you could teach me?"
    show PRG neutral
    PRG "Teach... you? Teach you what?"
    MC "How to cook! I can barely boil an egg or make noodles, would be nice to be able to make better dishes."
    PRG "M-me? Teach you?"
    show PRG sad
    PRG "But I, I'm not, uhm..."
    MC "Well, you obviously know more than me, given the spread in front of you..."
    show PRG neutral
    PRG "W-well, I, I'm not... not much of a teacher, really..."
    MC "Come on, it's just us. Just a few of your tips and secrets?"
    show PRG sad
    PRG "N-no, I, I, I'm s-sorry, but I'm just not comfortable. I-I could lend you some of my cookbooks, m-maybe?"
    "I groaned inwardly. It was obvious she was skilled at cooking. Why did she have to be afraid of showing it?"
    "But the way she huddled up against herself as she worked now, unwilling to raise her eyes up from her cooking, let me know there was no chance. If I pressed any more she'd probably start crying..."
    jump daymenu

label PRG003_3_c:
    MC "'All you're doing'? That's such an important skill to have!"
    show PRG surprised
    PRG "It-it is?"
    MC "Well, of course! Everyone has to eat. Being able to take what's available and make something delicious out of it..."
    show PRG neutral
    PRG "W-well, I guess it's useful..."
    MC "It's more than just useful. There's something about a lovingly home-cooked meal, especially shared with others. It shows our better natures to each other in such an important way."
    PRG "You... you really think so?"
    MC "Absolutely. It's one of the purest forms of showing care and love for another, to give up what's yours to make sure they're healthy and happy. It's practically the basis of civilization, preparing and sharing food."
    show PRG aroused
    PRG "I... never thought of it like that."
    show PRG happy
    PRG "Do... do you really think all that, Hotsure-san?"
    "I nodded, smiling. I'd kind of gone off on a tangent, but hey, if I could give Aida something to lift her mood, I wanted to do it, and the way she was beaming it was pretty obvious I'd succeeded..."
    $ setAffection("PRG", 2)
    jump daymenu
    
label PRG004:
    scene Track with fade
    play music Peaceful
    "Aida had finished making Alice's lunch early, so she and I decided to go for a walk around campus. The weather was nice, the sea breeze was cool... it almost felt like a date. I took a deep breath as we passed in front of the athletics building, and smiled."
    MC "This is nice, isn't it?"
    show PRG neutral with dissolve
    PRG "Hm? What is?"
    MC "This, just, us, the sky, the sun, the breeze... It's nice to just be out with a friend on peaceful days like this."
    PRG "..."
    show PRG aroused
    PRG "..."
    PRG "You... y-you think I'm a-"
    stop music fadeout 0.0
    "{b}{i}SLAM!{/i}{/b}"
    $ renpy.with_statement(vpunch, always=True)
    show FMG angry at Position (xpos=0.75) with dissolve
    show PRG surprised:
        linear 0.25 xpos 0.25
    "We were interrupted by Akira flying through the front doors of the athletics center at dangerous speeds, sprinting full tilt down the side of the building. We watched with wonder as she made it to the end of the long building in seconds."
    hide FMG angry with dissolve
    show PRG neutral at Transform(xzoom=-1) with dissolve
    PRG "...Was that... That was Mizutani-san, right? From our class?"
    MC "Yeah, and she... That didn't look like an exercise run..."
    PRG "We should go see what's wrong."
    "I nodded, and we hurried around the corner of the building to see if there was any sign of Akira."
    
    scene School Planter with fade
    "To our surprise she was only a handful of paces past the corner, kneeling in the grass and looking at something."
    show FMG sad at Position (xpos=0.75) with dissolve
    FMG "Oh no, oh no, c'mon little guy..."
    play music Bittersweet
    "When we got close to Akira, we saw what she was so concerned about. Lying motionless in the grass in an unnatural, awkward heap was a small bird, no bigger than Akira's hands cupped together."
    show PRG sad at Position (xpos=0.25) with dissolve
    FMG "I was just inside on the butterfly machine, kinda spacing out, when WHAM! This little guy slams into the window and drops like a rock!"
    PRG "Oh no!"
    MC "That's terrible..."
    show FMG neutral
    FMG "So, we need to get it to a vet or something, right? Anyone have anything to carry it with?"
    show PRG neutral
    PRG "Uhm..."
    MC "Gosh, let me look... don't have my gym bag..."
    PRG "Ah..."
    FMG "Oh, that's right, let me go get my gym bag and-"
    show PRG aroused
    PRG "I- uh- I {size=-5}think that might not be the best idea...{/size}"
    MC "Wait, hold up, Mizutani-san. What was that, Kodama-san?"
    PRG "W-well, I just remem-em-ember hearing that touching little b-birds will make their mothers not like them a-anymore. Like, they d-don't smell like birds anymore..."
    MC "Oh yeah, I remember hearing that too..."
    show FMG angry
    FMG "What! No way! We've gotta do something!"
    PRG "B-but, their m-moth-mothers..."
    FMG "We can worry about that later! If we leave it here it'll get gobbled up by the next stray cat or fox before nightfall."
    show PRG sad
    PRG "Ah! I'm sorry!"
    show FMG sad
    FMG "Okay, okay, okay, right, yeah..."
    "Akira seemed unsure of what to do, fidgeting side to side, hands above the fallen bird."
    FMG "W-well? What should we do?"
    menu:
        "You're right. We need to get it somewhere safe.":
            jump PRG004_1
        "I think Aida's right- we shouldn't touch it.":
            jump PRG004_2
            
label PRG004_1:
    MC "You're right. We need to get it somewhere safe."
    show FMG happy
    FMG "Right! Okay little guy, let's get you some help."
    show FMG neutral
    FMG "..."
    FMG "..."
    "Akira kept moving her hands oddly around the little bird without touching it, almost like she was trying to cast a spell or something."
    show FMG aroused
    FMG "...Umm, can- would you mind getting it, Hotsure-san? I... I'm a little worried I might hurt it, too in the zone of holding hard metal right now..."
    MC "Oh, uh, sure thing, yeah."
    "I kneeled down next to the bird, taking off my jacket and bunching it up into a kind of horseshoe around it. Slowly, gently, I closed it around and under the bird, lifting it up off the ground in the makeshift fabric bird's nest."
    MC "Okay... Okay, let's go find someone who can help."
    show FMG neutral
    show PRG neutral
    FMG "Right."
    PRG "..."
    
    scene School Exterior with fade
    play music Rain
    MC "Excuse me, do you know anything about birds? This one's injured, and- oh, you don't? Thanks anyways."
    show FMG angry with dissolve
    FMG "Hey! Hey you! We've got an injured animal here, and- hey! Where are you- stop running!"
    FMG "Sheesh, why does no one want to help?"
    MC "Well, uh... you might be coming on a little too strong."
    FMG "Harumph. Oh hey, you there, lady with the long hair!"
    show FMG neutral at Position (xpos=0.25) with dissolve
    show GTS neutral at Position (xpos=0.75) with dissolve
    GTS "Hm?"
    FMG "Hey, you're in our class, right? Do you know anything about birds?"
    show GTS sad
    GTS "Well, not much, I- oh, what happened there?"
    "Naomi looked at the bird as I caught up with Akira, her long bangs hovering just above."
    show FMG sad
    FMG "It ran into a window at the gym and I was worried about it."
    show GTS neutral
    GTS "I see. Yes, I had that happen several times at our greenhouse. Thankfully, it only appears to be stunned."
    show FMG neutral
    FMG "So you know what to do?"
    "Naomi nodded once, looking remarkably serene and level-headed next to the panicky amazon next to her."
    GTS "Just get a small box of some kind, put something soft in the bottom- I'd suggest a towel instead of your uniform, Hotsure-san- then just lay the bird in it gently and close the box up."
    GTS "Keep it somewhere dark and quiet for a few hours, then take the box outside and open it up. It doesn't look like anything's broken, so it should be able to just fly away."
    show FMG happy
    FMG "Oh, awesome! Thank you, Yare... um... Yamazu... uh..."
    GTS "Yamazaki."
    FMG "Yamazaki! Thank you, Yamazaki-san!"
    hide FMG happy with dissolve
    hide GTS neutral with dissolve
    "Akira ran off to find what she needed, yelling for me to follow. I turned to Aida with an apologetic look."
    show PRG neutral with dissolve
    MC "So much for 'peaceful days like this', I suppose. Sorry you got wrapped up in all this excitement."
    PRG "N-no, don't worry about it. It's... I'm okay."
    MC "Okay, thanks!"
    PRG "..."
    show PRG sad
    PRG "..."
    $ setAffection("FMG", 1)
    jump daymenu
    
label PRG004_2:
    MC "I think Kodama-san's right- we shouldn't touch it."
    show PRG happy
    pause 1.5
    show FMG angry
    FMG "What?!"
    show PRG aroused
    MC "Well, I mean-"
    FMG "We're not just leaving it here!"
    MC "Well hey, do you know what's wrong with it?"
    show FMG aroused
    FMG "W-well, no..."
    MC "So for all you know, touching it or trying to move it could make it worse."
    FMG "But- I mean..."
    "Akira slumped her shoulders and frowned down at the bird, obviously caught between wanting to do something immediately and wanting to do the right thing."
    MC "Look, we'll stand guard. You go find someone who knows what to do."
    show FMG sad
    FMG "I... all right."
    show FMG angry
    FMG "Sit tight little guy, I'll be right back!"
    hide FMG angry with dissolve
    play music Rain
    "Akira was off like a shot, her muscular legs propelling her towards the classrooms with surprising speed."
    show PRG neutral at center with dissolve
    PRG "..."
    MC "Phew... that was a thing. I hope the bird pulls through..."
    PRG "Hotsure-san..."
    MC "Yeah?"
    PRG "Thank..."
    show PRG happy
    PRG "Thank you for believing in me..."
    MC "Oh, it's no problem. Yours sounded like the best idea, after all."
    show PRG neutral
    PRG "(Not like anyone else does...)"
    $ setAffection("FMG", -1)
    $ setAffection("PRG", 1)
    jump daymenu
    
label PRG005:
    $setTimeFlag("aftertest")
    scene Auditorium with fade
    play music Peaceful
    "I spied Aida milling about in a corner of the auditorium, frowning at a piece of paper in her hands. It must have been her results, as the paper was the same odd size and shape as mine had been."
    MC "Hi Aida, how are-"
    "Aida's hands reflexively jerked to her chest, crumpling the paper inside them as she looked up, wide-eyed."
    show PRG surprised
    PRG "...Oh! oh, hello Keisuke. You, um, you startled me."
    MC "I'm sorry, Aida, just saw you over here and thought I'd say hello."
    show PRG happy
    "Aida's expression visibly brightened, but she still kept her results clasped tight to her bosom."
    PRG "Oh, well, um, hello!"
    PRG "..."
    MC "..."
    show PRG neutral
    PRG "..."
    MC "Soooo, are those your results there?"
    "Aida's eyes flicked down towards her chest, but she said nothing. After a few tense, awkward moments, I pulled my paper out of my pocket and unfolded it."
    MC "See? I got the same one."
    PRG "Uhm... w-well..."
    "She slowly took the paper off of her chest, and I could see Aida looking from me to her paper over and over, frowning at it with fluctuating degrees of intensity."
    MC "Er... Would you like it if I went first?"
    PRG "Yeah! I mean, um... if that's okay."
    MC "Not at all. *ahem* 'Student has hyper-productive keratin in scalp and face, leading to accelerated hair growth. No indications of accelerated hair growth in other areas.'"
    PRG "So... your hair's going to grow really fast?"
    MC "That's what they think, anyways."
    PRG "..."
    "Aida looked at her sheet again, then down at the floor."
    show PRG sad
    PRG "I-I'm sorry, I don't..."
    "She looked away, and I knew she didn't want to tell me. Maybe she was upset that I had something so relatively benign while she had something disfiguring. In any case I wasn't going to press it, but as I turned to leave I heard her whisper something under her breath."
    MC "What was that?"
    show PRG surprised
    PRG "Eeep."
    MC "It's okay, Aida, really. I promise I won't tell anyone."
    show PRG sad
    PRG "Th-thanks, Hotsure-san, but, ah... I- I should probably get back to the dorms..."
    hide PRG with dissolve
    "Aida gave a quick, deep bow, and scurried off, leaving me wondering what was so terrible on that sheet she couldn't tell me..."
    jump daymenu

label PRG006:
    $setVar("PRG006_walking", 0)
    scene School Front with fade
    play music Schoolday
    "With a light homework schedule for the day, I decided to walk around campus a bit, get more familiarized with the layout. I was up near the front gates of the school when I saw Aida come out of one of the administration buildings, arms piled high with boxes."
    "Seeing her slow, plodding steps under the wobbling stack of boxes, I headed over to help."
    show PRG neutral with dissolve
    MC "Hi Kodama-san, how are you?"
    PRG "Who...? Oh! H-hello, Hotsure-san."
    MC "Hello. Those boxes seem pretty heavy, would you like me to take some?"
    PRG "Oh, n-no thanks, I've... I've got it."
    MC "Are you sure? I don't mind."
    PRG "I-I'm okay. Don't, um, trouble yourself over it."
    jump PRG006_menu

label PRG006_menu:
    menu:
        "Let me help, I insist.":
            jump PRG006_a
        "You're sure I can't help?":
            $setVar("PRG006_walking", getVar("PRG006_walking") + 1)
            jump PRG006_b

label PRG006_a:
    MC "Let me help, I insist."
    show PRG unique
    PRG "No really, I-I-I-"
    MC "Come on, Kodama-san. I can see your legs shaking when you walk."
    PRG "W-well..."
    "I reached up and grabbed the top half of the pile from her. She didn't say anything to stop me, and the embarrassed smile let me know he wasn't against it."
    scene Campus Center with fade
    show PRG neutral
    MC "So what is all this stuff for?"
    PRG "These are supplies for Alice-san's new business."
    MC "Business?"
    PRG "It's, um, basically a mail-order catalogue. Alice can get things custom-made for students as they, uh, grow."
    MC "...Doesn't the school already do that?"
    show PRG unique
    PRG "I- I think so? But, well, Alice-san, she..."
    show PRG neutral
    PRG "Well, I suppose I shouldn't second-guess her..."
    jump PRG006_end

label PRG006_end:
    scene Dorm Exterior with fade
    show PRG neutral
    "We finally arrived at the women's dorms, Aida slightly red in the face from the exertion. I knocked on the door for her, and Alice answered after not to long of wait."
    show BBW neutral at Position(xpos=0.75) with dissolve
    BBW "Hm?"
    show BBW happy
    BBW "Oh! Wonderful, they've arrived!"
    "Alice started taking the boxes from Aida, the two of them setting boxes on a large kitchen table in the middle of the room. Having not been invited, I waited patiently outside the open door."
    "After they had gotten all the boxes, Alice started in on opening them, using a box cutter to slit the tape with fluid, well-practiced motions."
    "Aida wandered over to the door as Alice began casting packing paper and bubble wrap to the floor, looking behind her at the growing mess she'd undoubtedly have to clean up. She looked up at me, leaning against the half-closed door."
    hide BBW happy with dissolve
    PRG "...Good-bye, Hotsure san. And..."
    PRG "..."
    PRG "...thanks."
    "She gave me a small smile and closed the door, Alice's eager and authoritative voice already rambling out orders."
    if getVar("PRG006_walking") == 0:
            $setAffection("PRG", 1)
    elif getVar("PRG006_walking") == 3:
            $setAffection("PRG", 2)
    jump daymenu

label PRG006_b:
    if getVar("PRG006_walking") <= 3:
        MC "You're sure I can't help?"
        PRG "I-it's fine, don't worry about it."
        MC "Well, let's just keep walking together?"
        PRG "S-sure."
        "We slowly made our way through campus, one cautious step at a time. I tried to keep a conversation up with her, but the focus and exertion it took her to keep the boxes aloft and balanced took up all her attention."
        "Finally, she set the pile of boxes down to rest her hands."
        jump PRG006_menu
    else:
        MC "Are you sure?"
        show PRG angry
        PRG "Yes, Hotsure-san!"
        show PRG neutral
        PRG "..."
        show PRG sad
        PRG "We're almost there, anyhow..."
        "A little shocked at her outburst, I walked the rest of the way with her in silence."
        MCT "Why is she being so stubborn...?"
        jump PRG006_end

label PRG007:
    scene Cafeteria with fade
    play music Busy
    "After our morning classes, I headed over to the cafeteria for lunch. However, the queue was surprisingly long. It seemed I joined in at the peak hour."
    "I took a moment to glance around, looking for potential tables to sit at. A good portion of them were already taken. But then I spotted Aida, sitting alone at one of the big tables, hunched over her food."
    MCT "Huh, she's not with Alice? I'll drop by once I've got my lunch."
    "Once I had the plastic tray with my lunch, I walked over to the spot where Aida had been sitting before."
    "However, a large group of students now occupied the table alongside her, the only seat available right between her and the group. I made my way to her side of the table."
    show PRG neutral with dissolve
    MC "Hey Kodama-san!"
    show PRG surprised
    PRG "Ah! H-hi, Hotsure-san."
    MC "Mind if I sit next to you? You seem like you could use the company."
    show PRG sad
    PRG "O-oh, really? Hrm..."
    "She looked back down at her boxed lunch for a moment,"
    show PRG neutral
    extend " then nodded gently."
    "I took that as my cue to sit down in the chair next to her, between the group and Aida. We both dug into our food, but after a minute or so, my curiosity got the better of me."
    MC "So, uh... no Alice today?"
    PRG "Well... She's taking care of something personally, but she wants me on call in case she needs me."
    MC "On call, huh..."
    MCT "That does sound like something she would say."
    PRG "Y-yes."
    MC "Well... let's make the best of it then, hm?"
    stop music
    "Before she could get a word out, the environment got a lot louder."
    hide PRG with dissolve
    play music Tension
    "I looked around the room, already sensing a shift in atmosphere from where I was. Up ahead were two students who seemed like they were having an argument, though the already loud environment prevented me from hearing what about."
    "It turned out to be more than a regular disagreement, however. Things became physical, and each push in the already-busy cafeteria made the air more and more tense, and I was starting to get worried."
    MCT "I should do something before anyone gets hurt over there..."
    "Fortunately, a nearby teacher made her way through the crowd and dispersed the fighting students, and it dialed down relatively quickly."
    MC "I let out a sigh and turned back to the table, only to notice Aida had been holding onto my shoulder with both hands, her tiny fingers wrapped around the cuff of my shirt."
    show PRG unique with dissolve
    MCT "Huh?"
    "The conflict took only about a minute, but I neither recalled nor noticed Aida touching me. Once she realized that {i}I{/i} noticed, she quickly let go and returned to eating position at the table, intensely focused on her lunch."
    menu:
        "Are you alright?":
            $setAffection("PRG", 1)
            show PRG sad
            PRG "Y-yes, I'm fine."
            MC "You sure? I mean... I think it's normal to be concerned when a conflict occurs. Everyone responds differently. I was about to try to stop them, but thankfully there was no need for that."
            "Aida turned and looked at my face, before diverting her eyes again. But she nodded and gave a slight smile."
            show PRG neutral
            PRG "Yeah... Thank you, Hotsure-san."
            MC "No problem."
            stop music
            MC "Anyway, glad that's over. Let's enjoy that free time, shall we?"
            show PRG happy
            PRG "Sure!"
            "Her voice had a sudden cheer to it. She dug her chopsticks into her lunch with more energy than before."
        "Were you scared?":
            $setAffection("PRG", -1)
            show PRG sad
            PRG "Ye-... I mean... sorry."
            MC "Hm? There's no need to be. I got a bit scared too. It could've easily gotten ugly, but fortunately the teacher got between them before that happened."
            stop music
            "Aida sat there in silence, not even eating her food. I felt I should probably switch topics..."
            MC "Anyway, glad that's over. Let's enjoy that free time, shall we?"
            "Aida gave a slight nod... I took that as a sign to continue eating. That's what we're here for."
        "Good thing the teacher intervened...":
            show PRG sad
            PRG "Y-yes, I don't like to think about what would've happened if..."
            stop music
            MC "But it didn't, fortunately. Even if they would have fought, the students around them would've probably stopped them before either of them got seriously injured. That's what I like to think, anyway."
            show PRG happy
            PRG "Yeah, you're probably right."
            MC "Anyway, glad that's over. Let's enjoy that free time, shall we?"
            show PRG neutral
            PRG "All r-right. Sounds good to me."
    "The remainder of the lunch went smooth. We both enjoyed our lunch, talked about things that happened in class, general small talk. Once we were done, we walked back to our homeroom for the next class."
    jump daymenu

label PRG008:
    $setProgress("PRG", "PRG009")
    scene School Inner with fade
    "The day had gone by quickly, classwork barely slowing me down. With little else to do before dinner, I went to find Aida, probably in the cooking classroom again."
    MCT "And maybe get a free sample, heh..."
    
    scene Classroom with fade
    play music Schoolday
    show PRG neutral at Position (xpos=0.25) with dissolve
    PRG "Oohh..."
    hide PRG neutral with dissolve
    show PRG neutral at Position (xpos=0.75) with dissolve
    PRG "Not here either..."
    hide PRG neutral with dissolve
    show PRG neutral at center with dissolve
    PRG "Isn't there one anywhere?"
    "Instead of the usual soft, quiet, unobtrusive girl in the corner, Aida was shuffling from one side of the classroom to the other, every cupboard not already locked up opened as she searched for something."
    MC "Uh... Ko-Kodama-san?"
    show PRG surprised
    "Aida jumped in place, turning to me and blushing."
    show PRG aroused
    PRG "Ho-hotsure-san! I'm sorry, I- I didn't see you come in."
    MC "It's okay... What seems to be the problem?"
    PRG "Oh, it's awful, Hotsure-san! Alice, she gave me these fancy dishes for when I was cooking for her, but, but... well, look!"
    "Aida handed me a measuring cup, and I looked at the lines along the side."
    MC "...what's 'oz' stand for?"
    show PRG angry
    PRG "I don't know! It's some kind of American measurement, and my cookbook is all in milliliters! Now I'm running behind, and Alice is going to yell at me..."
    show PRG sad
    PRG "...and I don't know what to do!"
    MC "Oh! Ounces, right!..."
    menu:
        "I'll go find out the answer, be right back!":
            jump PRG008_1
        "I think I remember seeing it somewhere...":
            jump PRG008_2
        "Don't worry, I know the conversion rate. Show me the recipe." if getSkill("Academics") >= 3:
            jump PRG008_3
        "Don't worry, I know the conversion rate. Show me the recipe. (disabled)" if getSkill("Academics") < 3:
            pass

label PRG008_1:
    MC "I'll go find out the answer, be right back!"
    show PRG surprised
    PRG "O-okay!"
    
    scene Hallway with dissolve
    "I took off at a jog down the hall, looking around for anything that might help me. Stopping to ask every student would take too much time, and probably wouldn't get me anywhere besides. I could look for any transfer students, but..."
    "Well, the only one I'd seen was Alice, and I couldn't exactly ask her or she'd know something was wrong."
    "Then I spied one of the teachers turning down the stairs."
    MC "Tsubasa-sensei!"
    "I was so loud Tsubasa nearly dropped the big folder he was carrying, turning as he stood on the first step down."
    TS "Goodness, not so loud. What is it?"
    MC "Do you know how to convert Metric into American?"
    TS "American? Oh, you mean, like measurements?"
    MC "Yes, sensei."
    TS "Well, sure, it's actually in the back of the math book here. And it's called 'Imperial', not 'American'."
    "Tsubasa-sensei hadn't even finished opening the book to the right page before I snatched it up and started running back to the cooking classroom."
    MC "Thanks, I'll bring it right back!"
    TS "H-hey! That's the teacher's edition!"
    MC "Promise I won't peek!"
    
    scene Classroom with fade
    show PRG sad with dissolve
    MC "I got it!"
    show PRG happy
    PRG "You did! Oh, thank you!"
    MC "Okay, let's see here, measurements, measurements... Ah, okay, so eight ounces in a 'cup'... and now, over here... twenty-nine-point-five... thirty milliliters in an ounce. What's the recipe say?"
    show PRG neutral
    "Ah, ah, um... A hundred and fifty milliliters."
    MC "Okay, so, five ounces, about, and eight to a cup... You want to fill it to right there."
    "I pointed to the space between the '1/2 cup' and '3/4 cup' notches on the measuring cup. Aida nodded and we moved to the next ingredient, and then the next, until she had all the measurements down in the more familiar milliliters."
    "Later..."
    PRG "Well, Alice's not going to be happy it's late, but at least it's right... I hope she's not mad at me."
    MC "I'm sure she'll understand."
    PRG "Right... well, thank you again, Hotsure-san."
    hide PRG with dissolve
    "Aida finished plating Alice's meal and left, leaving me alone in the room. It had been a bit hectic, but it was still nice to have spent time with her."
    jump daymenu
    
label PRG008_2:
    MC "I think I remember seeing it somewhere..."
    show PRG happy
    PRG "You do?! Oh, thank goodness!"
    MC "Yeah, lemme just... Hmm... How much did you need?"
    show PRG neutral
    PRG "Oh, um, a- a hundred and fifty milliliters."
    MC "Right, so, one-fifty... and there's... eight to an ounce? No, wait... it was something like..."
    PRG "...?"
    MC "Okay, I think that's about right, there. It looks right. I think."
    if (renpy.random.random() * 100) >= 30:
        jump PRG008_2_a
    else:
        jump PRG008_3_a

label PRG008_2_a:
    "Aida worked quickly, but the worried look on her face never lifted, instead deepening as the minutes ticked by."
    show PRG neutral
    PRG "This isn't... it's not setting up..."
    show PRG sad
    PRG "What did I do wrong?"
    show PRG neutral
    PRG "Hotsure-san, are you sure you got the measurements right?"
    MC "Um... Sort... of..."
    show PRG sad
    PRG "Oh, Hotusre-saaaaan! I- what am I going to do now?"
    MC "I'm sorry! I thought I remembered!"
    PRG "Now I have to start over! Alice is going to be so mad!"
    MC "I- I'm sorry! I should have looked it up somewhere..."
    "Aida's pouting made my heart sink, but she refused any more 'help' from me. Dejected, I headed back to my dorm, trying to think of some way to make things up to Aida..."
    $ setAffection("PRG", -1)
    jump daymenu

label PRG008_3:
    MC "Don't worry, I know the conversion rate. Show me the recipe."
    show PRG surprised
    PRG "R-really?!"
    MC "Yeah, it's about thirty milliliters to the ounce."
    show PRG aroused
    PRG "Um, 'about'?"
    MC "Twenty-nine and a bit. Not enough to make a difference."
    show PRG neutral
    PRG "Oh... oh, okay."
    $ setAffection("PRG", 1)
    MC "So what's the first measurement you need?"
    PRG "Ah, ah, um... A hundred and fifty milliliters."
    MC "Okay, so, five ounces, about, and eight to a cup... You want to fill it to right there."
    "I pointed to the space between the '1/2 cup' and '3/4 cup' notches on the measuring cup. Aida nodded and we moved to the next ingredient, and then the next, until she had all the measurements down in the more familiar milliliters."
    jump PRG008_3_a

label PRG008_3_a:
    MC "...Okay, I think you're good to go!"
    show PRG happy
    PRG "Thank you, Hotsure-san! I was afraid I was going to be late with dinner!"
    MC "Anytime, Kodama-san."
    "I stayed around and talked with Aida while she finished up her cooking, swearing to ask Alice for either a metric set of measuring dishes or a cookbook written in Imperial measurements..."
    $ setAffection("PRG", 1)
    jump daymenu
    
label PRG009:
    $setTimeFlag("size2")
    $setProgress("PRG", "PRG012")
    scene School Exterior with fade
    play music Sunset
    "After finishing my homework for the day, I decided to take a walk around, get some fresh air. As I passed by the vending machines, I saw Aida sitting at one of the picnic tables, looking at something in her hands."
    show PRG neutral at Position (xpos=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    PRG "..."
    "I approached Aida from the side, not trying to be sneaky, just that's how my path wound up intersecting her. As I got close, I recognized the paper she was staring at by the distinct shape and size."
    MC "Looking at your results, huh?"
    show PRG surprised
    PRG "Eep!"
    show PRG neutral at Position(yalign=1.0), Transform(xzoom=1)
    PRG "O-oh, Hotsure-San! I, uh, y-you... Um..."
    "Aida whipped the paper behind her in the least convincing attempt at hiding something I think I'd ever seen."
    MC "..."
    PRG "..."
    MC "...Soo, checking out your results again?"
    show PRG sad
    pause 1.5
    show PRG neutral with dissolve:
        linear 0.5 xpos 0.4
    PRG "...Yes."
    show PRG neutral at Position(xpos=0.4)
    MC "...Is something the matter? I mean, I understand if you don't want to tell me, but it seems like it's causing you distress."
    "Aida clutched the paper to her chest, and I could tell from the bits that were sticking out that it had been completely crumpled up and smoothed out numerous times."
    MC "It's okay! Really! I just... I hate to see someone as nice as you upset, I couldn't not at least ask..."
    show PRG happy 
    PRG "Hotsure-san..."
    show PRG neutral
    PRG "..."
    MC "Is it okay if I sit?"
    PRG "Oh, ah... s-sure, I guess."
    "Aida scooted over for me, even though there was plenty of room on the bench. I sat down and looked out towards the sunset-lit clouds."
    MC "You know, I was so worried when I first found out what mine was. The hair, that is."
    PRG "..."
    MC "I was worried I was going to be growing it everywhere- on my arms, on my chest, my back..."
    PRG "..."
    MC "Even on my butt! Can you imagine, having hair growing out of your butt long enough to style?!"
    show PRG aroused
    PRG "{i}*Snrghk!*{/i}"
    "Aida tried to hold it back, but the absurdity of the image was too much for her and she laughed."
    MC "Ah, there we go, that broke the ice."
    show PRG neutral
    PRG "Hotsure-san..."
    MC "Well hey, it got you to stop thinking about whatever you were worried about for a second, didn't it?"
    show PRG happy
    PRG "..."
    show PRG neutral
    PRG "..."
    MCT "Hm, this doesn't seem to be working... Maybe I should just go..."
    "I waited for a little while longer, then decided to leave. But right as I put my hands on my knees to push myself up off the bench..."
    PRG "What... What do you really think about it?"
    MC "Excuse me?"
    "Aida unfolded her results and looked at it again, then looked over to me."
    PRG "Y-your change. How do... how do you feel? How do you make it through the day?"
    menu:
        "Well, I'm worried.":
            MC "Well, I'm worried, of course."
            PRG "You... You are?"
            MC "Absolutely. We're dealing with such major uncharted territory. I mean, sure, it's 'only' hair, but how fast is it going to grow? Is it going to suck all the color out of me early, leaving my with white old man hair before I'm 30?"
            MC "Where's all the hair coming from, is it going to, I don't know, leech the hard stuff out of my skull to fuel it?"
            PRG "..."
            MC "I don't think anyone here is completely carefree about being here."
            PRG "Mizutani-san seems pretty okay with hers. She tells just about everyone she meets, it seems."
            MC "Hahaha, well, Mizutani-san might be a special case... She seems excited about everything."
            PRG "Heh..."
            MC "But, so, are you worried about yours? Do you need... I don't know, someone to confide in? Rant to? If I can help, I'd like to."
            PRG "That's..."
            show PRG happy
            PRG "That's very nice of you, Hotsure-san..."
            show PRG neutral
            PRG "But I... don't want to talk about it."
            show PRG sad
            PRG "I think... I should go now. I'm sorry for bothering you."
            MC "Are you sure? It's not a bother, really."
            show PRG neutral at center with dissolve
            PRG "..."
            show PRG sad
            PRG "No, I-I should get going..."
        "Actually, I'm kind of excited.":
            MC "Actually, I'm kind of excited for it."
            show PRG surprised
            PRG "R-Really? Why? How?"
            MC "Well, really, how interesting is one's hair, normally? I mean, there can be fun styles, but how interesting is hair by itself?"
            show PRG neutral
            PRG "Not... really, I guess?"
            MC "Exactly. But now, what's my hair going to be like? Are the strands going to be super thick? Are they going to split into smaller hairs as they grow out? Scientists are going to be testing and examining my hair in a laboratory, how neat is that?"
            PRG "But... but what about... what if something goes wrong?"
            MC "So what if it does? It's hair, it'll grow back. And apparently quickly, at that."
            PRG "No, I mean, like, like... I, what if it hurts, or if it goes out of control, or makes you look weird?"
            "I snorted, looking over to Aida and smiling when she met my eyes for a moment, before she quickly glanced back down."
            MC "Well, I mean, I guess I'll deal with it. It's not like I'm not in the best place in the world to deal with it, right?"
            PRG "I suppose..."
            MC "Come on, we're in probably the most accepting place for these kind of special attributes. Whatever happens to any of us here... well, it will be an adventure, right? Sure, it'll have its ups and downs, but nothing terrible's going to happen to us, not here of all places."
            PRG "..."
            show PRG unique
            PRG "W-would... I mean, u-um... is it okay, uh, t-to..."
            "I could hear the paper crinkling in her hands as she fidgeted, staring at her knees."
            PRG "W-would you help me, if it's not any t-trouble? I'm n-n-not much good at adventures..."
            MC "Sure, absolutely. What do you need?"
            show PRG surprised
            PRG "Oh! N-nothing right now, I- I wouldn't put you on the sp-p-spot like that."
            MC "Well, you just let me know, okay? I hate to see someone as nice as you upset if I can help it."
            show PRG neutral
            PRG "..."
            show PRG happy
            PRG "...!"
            show PRG neutral
            PRG "*Ahem*, y-yes, I will, i-if, if it's not a bother."
            PRG "...Thank you, Hotsure san. I, I think, um, I'll be going now..."
            MC "Sure, no problem!"
            "Both of us got off the bench and said our goodbyes, but something occurred to me before she turned away."
            if isEventCleared("PRG005"):
                MC "...Still don't wanna tell me what yours is?"
                show PRG neutral
                PRG "I..."
                show PRG neutral at Transform(xzoom=-1)
                pause .75
                show PRG sad at Transform(xzoom=1)
                pause .75
                show PRG sad at Transform(xzoom=-1)
                pause .75
                show PRG sad at Transform(xzoom=1)
                PRG "..."
                PRG "I'm s-sorry, no."
                MC "*sigh*"
                MC "All right, well... I suppose sooner or later the answer's gonna be obvious one way or another."
                PRG "I... I'm s-sorry, really..."
                PRG "..."
            else:
                MC "So... mind if I ask what yours is? I've told you mine.."
                PRG "...!"
                PRG "I... I..."
                show PRG sad
                PRG "..."
                MC "Hey, hey, it's okay. I just, a burden shared is a burden halved, you know?"
                PRG "...I'm... I'm sorry, Hotsure-san. I'm not..."
                show PRG sad at Transform(xzoom=-1)
                MC "Oh, well, um... Okay, Kodama-san. See you in class..."
                hide PRG sad
                MCT "I wonder what she's got that's got her so upset...?"
        "I try not to think about it.":
            MC "Honestly? I try not to think about it."
            show PRG surprised
            PRG "R-really?"
            MC "Yeah. Just kinda file it away and leave it there."
            PRG "But how... h-how do you do it?"
            MC "...Do what?"
            PRG "Just- just ignore it! Ignore whatever's changing with you??"
            show PRG angry
            PRG "Th-they said it was permanent! That we'll, we'll, we're never going to get back to the way we were!"
            MC "That's {i}exactly{/i} why it's easy to ignore."
            show PRG neutral
            PRG "...?"
            MC "Let me ask you this: If I told you it was going to rain tomorrow, what would you do?"
            PRG "Eh? B-but I didn't hear anything about-"
            MC "Hypothetically. Hypothetically, you know 100%% that it was going to rain tomorrow. What would you do?"
            PRG "W-well, I don't know. Uh, I, well I'd get my umbrella.. Maybe a raincoat if it was bad... I think I have some galoshes if it was really raining..."
            MC "But what would you do tonight?"
            PRG "Tonight?"
            MC "Yeah. It's raining tomorrow, what do you do different tonight?"
            PRG "I- I don't know, do I have laundry out, is my house in a flood zone...?"
            MC "No, nothing like that. Your home is fine, but it's raining tomorrow. What do you do?"
            show PRG unique
            PRG "I- I don't know. Nothing, I guess? I mean, it's not raining yet, right?"
            MC "No, it's not. You don't bother doing anything about it because it hasn't happened yet."
            "Aida nodded a few times, brow furrowed, until she closed her eyes and her features fell."
            show PRG neutral
            PRG "Oh... I see."
            MC "Exactly. You can't do anything about the rain before it happens, you can't stop it when it does happen, but you can take care of yourself and protect yourself from the worst of it."
            MC "If everything the nurses, Tashi-Sensei, and the older students have said is true, whatever's going to happen is {i}going{/i} to happen. So why worry about it now? I might as well worry if the sun is going to come up."
            MC "When whatever changes we have start actually changing us, I'll see what I need to do. Do I just need the umbrella? Do I need a coat, too? Is it so bad I need galoshes?"
            MC "Whatever the case, I'll deal with it when it happens. Worrying now is like going outside in coat, galoshes, and umbrella every day just in case it rains really badly. So, like I said, I just don't think about it. Does no one any good."
            PRG "..."
            "Aida just kind of looked at the ground for a few moments, nodding slowly, then nodding a little faster before looking at me."
            PRG "I... well... you've given me a lot to think about, Hotsure-san. I-I'm sorry, but I need to go now..."
            hide PRG neutral with dissolve
            "She picked up her things and left, leaving me to watch and wonder if she was even capable of not caring about something, or if she was stuck feeling like all the world's a stage and there are always critics in the audience, even down to her innermost feelings..."
    jump daymenu

label PRG010:
    $setSize(2)
    $setTimeFlag("aftersize2")
    scene Classroom with fade
    play music Peaceful
    "I wandered into the cooking clubhouse, knowing it was about the time that Aida started cooking for Alice, but before she got too involved in the meal to socialize."
    show PRG happy with dissolve
    "Aida looked at the sound of someone approaching, her expression momentarily brightening before her usual worried look crossed back over her features."
    PRG "Oh! U-um, hi Keisuke. What brings you here?"
    MC "Nothing much, was just around and thought I'd come visit for a bit, maybe help you with your cooking, if you'd like."
    show PRG aroused
    "As I walked closer, Aida seemed to get more uncomfortable, hunching her shoulders forward oddly and turning red."
    MC "Is something the matter? Do you need a fan for the heat or anything?"
    PRG "No! No, I-I'm fine, just fine."
    "I'd known Aida long enough that her 'Just fine' was anything but, so I came around to her counter. When I did, her posture shifted again, her apron hanging off her oddly."
    MC "Here, let me help. I can do the dishes, or cut veggies, or something."
    PRG "N-no, that's okay, I-I've got it. Why don't you have a seat, I'll make you a portion too, if you want?"
    "Aida reached for a new cherry tomato to slice up, but the oblong red sphere spat out from under her knife, rolling off the cutting board."
    show PRG surprised
    PRG "Oops!"
    MC "I got it!"
    "We both bent down to try and catch the falling fruit, and..."
    "{i}Bomf{/i}"
    "I bolted upright and took a step back, cheeks burning. I knew that feeling. Soft, resilient, a bit of bounceback."
    MC "I-I'm sorry! I just bent down on instinct, and..."
    show PRG aroused
    PRG "..."
    "I used the awkward silence to confirm what I'd felt. It was subtle, given how loosely she was wearing her clothes, but under the apron it was clear that Aida's bust had gotten larger. Not as big as Honoka, of course, but definitely bigger than that first meeting."
    "My eye wandered down from her chest, and I saw her hips were bigger, too, wider, more thick-looking. Definitely more padding than could be explained by a 'freshman 15'."
    MC "So..."
    PRG "..."
    MC "I guess this is your growth?"
    "Aida bit her lip and nodded, looking away and blushing."
    menu:
        "Don't worry, lots of guys like girls with curves.":
            jump PRG010_a
        "It's okay, you'll be fine.":
            jump PRG010_b
        "I think it really suits you.":
            jump PRG010_c

label PRG010_a:
    MC "Don't worry, lots of guys like girls with curves."
    show PRG surprised
    PRG "Wh- so you didn't like me before?"
    MC "Huh? No, of course not! I mean, I did!"
    show PRG angry
    PRG "But not now?!"
    MC "No, no! I like you just as you are!"
    show PRG sad
    PRG "But- but then if I get bigger you won't like me...?"
    MC "No! I mean, yes! I mean, uh, I..."
    $ renpy.with_statement(Shake((0, 0, 0, 0), 0.75, dist=20))
    PRG "Uwaaa~!"
    hide PRG with dissolve
    "Aida ran from the room crying. Dumbstruck, I turned the stove off and put the food away."
    MC "Boy, I really stepped into that one, huh?"
    $ setAffection("PRG", -2)
    jump daymenu
    
label PRG010_b:
    MC "It's okay, you'll be fine."
    "Aida looked up at me, frowning. Obviously she didn't share my confidence."
    MC "I mean it! There's a whole school set up here to make sure everything's okay with us."
    PRG "But that's easy for... easy for you to say. You fix your change with a barber..."
    MC "And you can fix yours with some new clothes. Come on, you almost had it already, if I hadn't- If we hadn't bumped into each other, I never would have noticed."
    PRG "...Really? You're not just saying that?"
    MC "Really. You'll see. Everything's going to be okay."
    PRG "Well... okay."
    "She didn't seem that convinced, but at least she wasn't going to run out of the room crying or anything..."
    jump daymenu
    
label PRG010_c:
    MC "I think it really suits you, actually."
    PRG "I- what?"
    "Aida looked down at herself, pressing the apron flat against her stomach. It had the effect of accentuating her growth, a clear difference in both size and heft. She looked down at herself, then up at me."
    PRG "You... you really think so?"
    MC "Of course! You already had that kind of body before, this just... accentuates it, somewhat."
    show PRG happy
    "Aida looked happy for a moment, putting her hands on her hips and pulling the apron tight across them."
    PRG "And... and if I get... bigger?"
    MC "I think you're pretty at any size."
    "Again, happiness flitted over Aida's features before the nervous frown overtook them, like someone trying to hold up a too-heavy blanket."
    show PRG neutral
    PRG "So... so you like curvy girls?"
    MC "I don't know about all curvy girls, but I certainly think you're beautiful..."
    show PRG happy
    "This time, the smile stayed up, and she and I talked pleasantly while she finished her cooking."
    $ setAffection("PRG", 2)
    jump daymenu
    
label PRG011:
    scene F1 Hallway with fade
    play music Busy
    "My footsteps echoed down the long hallway on campus. The other students were mingling outside, but I felt like simply taking a small stroll."
    "I could hear the faint noise of activity outside but what caught my attention was some light commotion coming from further down the hall."
    "Curious, I moved closer to the source of the disturbance and could make out the noise of what may have been an announcer."
    "The door to the cooking club was slightly opened so I decided to peek inside."
    scene Classroom with fade
    show PRG unique with dissolve
    "I quickly spotted Aida standing in front of a radio. Her hands were clenched as she looked intensely at the audio book."
    "The next noise from the radio was unmistakable as it was the clack of a bat hitting a baseball. The announcer's voice cheering through to declare the player taking first base."
    show PRG happy
    PRG "Yes! Woo!"
    MC "Who's playing?"
    "The moment my voice rang out, Aida jumped and quickly lowered the radio's volume."
    show PRG surprised
    PRG "AH! H-h-h-h-hotsure-san!"
    extend " I'm sorry! Was it t-too loud!?"
    PRG "It wasn't disturbing you was it!? Oh of course it was!"
    extend " I'm so sorry! I'll shut it off right away!"
    MC "Whoa whoa, calm down Kodama-san. Breathe...calm down. It's fine, it wasn't bothering me."
    show PRG unique
    PRG "Oh...sorry."
    MC "Heh, I already said it was fine. I wasn't aware you were into baseball."
    PRG "I-I am a little bit."
    "I walked over as she took a few steps back and left the radio on the desk."
    "Turning the volume back up, I looked over at her as she immediately looked away from me and towards the floor."
    MC "I can leave if I'm making you uncomfortable."
    show PRG surprised
    PRG "No no no no! I-I'm sorry, you're not bothering me."
    extend " I-I'm just not used to having others listen with me."
    PRG "Ah! I should make some treats or something!"
    "She quickly hurried off to grab some supplies from the club fridge before rushing over to the stove."
    show PRG unique
    "I was surprised by how quick she could be as she was already preparing what I imagined were cookies."
    MC "How long have you been into baseball?"
    PRG "U-Uh...a few years...give or take a few more."
    MC "Seems you have more than a light interest in it then."
    show PRG sad
    PRG "S-s-sorry..."
    MC "What are you apologizing for?"
    PRG "T-that I lied..."
    MC "You didn't lie, so don't worry. Which teams are playing by the way?"
    show PRG unique
    PRG "U-um, the Dragons versus the Lions."
    menu:
        "The Dragons must be getting destroyed.":
            jump PRG011_a
        "I hope the Dragons pull through.":
            jump PRG011_b
            
label PRG011_a:
    MC "Oh man, talk about a rough matchup. The Dragons must be getting destroyed."
    show PRG sad
    "Aida stopped stirring the batter she had been working on until now, making me look over towards her."
    PRG "..."
    MC "Hm?"
    PRG "..."
    MC "Y-you're a Dragon's fan, aren't you?"
    PRG "Y-y-yes..."
    MC "Oh! I'm sorry, I didn't mean that in like a bad way."
    MC "Um okay...maybe there's no other way to mean that. Sorry though, seriously I didn't mean to insult the team you like."
    PRG "I-it's okay. I'm used to people picking on the team I like..."
    "She went back to stirring as my heart sank a little, scratching the back of my head. I walked over in hopes of cheering her back up."
    MC "What type of cookies are you making?"
    "She flinched as she must have not noticed me move closer to her."
    show PRG neutral
    PRG "J-just some butter cookies. I h-hope that's okay."
    MC "Yeah, sounds great to me. I could use one of your tasty snacks."
    "She blushed lightly as she stirred with a bit more energy to her."
    $setAffection("PRG", -1)
    jump PRG011_outro
    
label PRG011_b:
    MC "Well...they might be at a disadvantage, but I hope the Dragons pull through."
    "Aida suddenly stopped stirring the batter she had been working on and turned to look over at me."
    show PRG unique
    PRG "Y-y-you like t-the D-dragons too!?"
    MC "U-uh yeah..."
    "She moved over towards me, the batter swaying about in the bowl as she smiled."
    show PRG happy
    PRG "M-me too! I-it's nice to meet someone else who does."
    MC "Heh, they've had a rough career, but I feel that makes them more endearing."
    PRG "Y-y-yeah! I feel the same way. They have a lot of heart and they never give up."
    "We shared a smile as I looked down at the batter she had."
    MC "What type of cookies are you making?"
    show PRG neutral
    PRG "J-just some butter cookies. I hope that's okay with you."
    MC "Heh, sounds like the perfect treat. I could use one of your tasty snacks."
    "She blushed lightly, but smiled as she resumed her stirring before walking back to the stove."
    $setAffection("PRG", 5)
    $setFlag("PRG011_b")
    jump PRG011_outro
    
label PRG011_outro:
    MC "So what got you into watching baseball?"
    show PRG neutral
    PRG "I saw a lot of it on television and I guess grew more attached to it as time went on."
    PRG "W-what about you?"
    MC "My father likes it. He doesn't really have a favorite though."
    MC "For him, he'll just pick a team at the start of the game and bet to see if he picked correctly."
    MC "So I just learned to appreciate it from him, I suppose. Granted, I don't bet on any of the teams."
    "Our conversation was cut off as there was another loud clack from the bat's impact."
    "The announcer mentioning how far it was going as the Dragons were taking all the bases back home."
    "Aida quickly hurried over as we listened to how the ball was soaring, soaring, soaring,"
    extend " and it was out of there!"
    show PRG happy
    if getFlag("PRG011_b"):
        "Both" "Yeah!"
    else:
        PRG "Yay!"
        MC "Wow, look at that."
    "Aida hopped a little in her excitement."
    "However, this caused the batter she had been working on to suddenly lurch out from the bowl and splatter all over the floor!"
    show PRG surprised
    PRG "AH! Oh no!"
    "She immediately ran off to gather cleaning supplies as once she came back, she went straight to cleaning."
    "Taking some of the supplies, I knelt down and helped her clean."
    show PRG sad
    PRG "I'm sorry! So sorry!"
    extend " I ruin everything..."
    MC "Hey, it's okay. Don't worry about it."
    PRG "But I ruined it."
    MC "Then we'll just make more. Here, I'll help you out."
    show PRG surprised
    PRG "H-h-huh?"
    MC "It shouldn't be that hard, right? I'll help you make the next batch. You'll just have to show me how."
    show PRG unique
    PRG "U-u-u-u-u-uh okay..."
    "I helped her back up, her face a deep red constantly looking down at her feet."
    "I couldn't resist chuckling as I gave her a small pat on the shoulder, having her guide me in our escapades of baking."
    "All while the Dragons had managed to win the first game of the new season."
    jump daymenu
    
label PRG012:
    $setProgress("PRG", "PRG013")
    scene Classroom with fade
    "The rest of the day went by relatively quickly."
    "Fairly straightforward classes, some homework that would have to be finished next week."
    "Nothing out of the ordinary."
    "Matsumoto led the usual outro, followed by the class dispersing and going about their own business."
    "I glanced over to see Aida being kidnapped by Alice again."
    extend " -Figuratively, of course."
    extend " She waved at me before disappearing beyond the door frame."
    "I started packing my books in my bag, however by the time I was done, I noticed someone standing right next to my desk."
    show BE happy with dissolve
    play music BE
    BE "Heey Kei-chan! How's it going?"
    MC "Yo. Not much, deciding what to do today. What about you?"
    BE "Doing pretty good. So..."
    "She took a moment to grab a vacant chair to sit on. However she sat on it in reverse, practically putting her bust on display."
    if isEventCleared("BE001") or isEventCleared("BE010"):
        "They seemed relatively bigger than before, so that hunch she had a while back turned out to be right."
        "Though that would've been what most people would have guessed."
    else:
        "If I hadn't known better, I would've figured my eyes were playing tricks on me. But it definitely seemed Honoka's growth factor was her breasts."
    BE "You're getting pretty cozy with Kodama-san, huh?"
    MC "I mean...cozy sounds kinda extreme. We're becoming pretty good friends, I'd put it like that."
    show BE neutral
    BE "Fair point, fair point. There's something I've been wondering about, now that we've all been here for several weeks."
    MC "What's that?"
    BE "Do you...happen to know Kodama's growth factor? It's pretty obvious what everyone else's is by this point, but I haven't really noticed anything about her."
    BE "With that said though...if sharing is too personal or uncomfortable, that's totally cool too."
    "I took a moment to consider. Aida hasn't told me explicitly what her growth factor is, but there was definitely {i}that{/i} moment where I bumped into her."
    "If that's going to keep growing as it is, Honoka and basically everyone will eventually find out anyway. Doesn't seem to be any harm in telling her."
    MC "Well, she has grown a bit bust and hip-wise. Not as much as you though."
    show BE aroused
    BE "My my, Kei-chan! You're quite perceptive, aren't you?"
    MC "O-oh. Uhm...sorry, I just blurted that out."
    show BE neutral
    BE "Hehe, no worries. Wait... are you sure it's both? I haven't heard of anyone who has two separate growths."
    MC "Hrm...there could be something that effectively combines the two?"
    BE "..."
    MC "..."
    show BE surprised
    BE "OH! I know!"
    MC "Oh?"
    show BE aroused
    BE "Hey Kei-chan...are you, by any chance, familiar with the MILF archetype?"
    if getAffection("PRG") >= 7:
        MC "W-W-WHA? I mean...Y-yeah but...you really think that she'd grow that way?"
        BE "Ooh my, you're turning all red!"
        MC "Ah c-come on, Honoka, gimme a break..."
        show BE happy
        BE "Just teasing ya. And well...maybe? Only time will tell."
        extend " But I already know you two are a couple waiting to happen."
        menu:
            "Maybe...":
                MC "Maybe...we'll see how things go. Like you said, time will tell."
                BE "Totally."
            "That seems like a stretch.":
                MC "That seems like a stretch, Honoka. I mean, she's sweet and all, but..."
                show BE neutral
                BE "Oh, don't take it too literally. All I'm saying is that I can picture you two together, that's all."
                if getSecondHighest("PRG")=="BE":
                    show BE unique
                    BE "Or...you and me."
                    "To make her hint even {i}less{/i} obvious, she winked."
                elif getSecondHighest("PRG")=="BBW":
                    BE "Or you and Nikumaru-san."
                elif getSecondHighest("PRG")=="FMG":
                    BE "Or you and Mizutani-san."
                elif getSecondHighest("PRG")=="GTS":
                    BE "Or you and Yamazaki-san."
                elif getSecondHighest("PRG")=="AE":
                    BE "Or you and Matsumoto-san."
    else:
        MC "Honoka...I don't really think that classifies as a growth factor."
        show BE neutral
        BE "Why not? It isn't like there's an encyclopedia on growth factors."
        MC "True, but an archetype like that isn't even anything specific; not to mention, it's highly subjective."
        MC "Especially the first word of that abbreviation."
        show BE angry
        BE "Boo... but I guess you're probably right."
    "Honoka glances over at the clock, quickly getting up from her seated position. With plenty of after-bounce to admire."
    show BE neutral
    BE "Oh, how time flies! I better get going. A club I wanna join is having tryouts in a few minutes."
    BE "Catch ya later Kei-chan, was nice talking to you!"
    MC "Likewise Honoka, was nice to chat a bit."
    "I waved her goodbye as she nearly sprinted out of the classroom."
    hide BE with dissolve
    BE "Ah, hello Kodama-san!"
    "But she seemed to run into Aida right away."
    PRG "A-ah, h-hello Inoue-san..."
    BE "Kei-chan's still in the classroom, if you're looking for him."
    PRG "Ah...Y-yes...thank you."
    stop music
    show PRG neutral with dissolve
    "Moments later, Aida peeked her head inside the classroom. I chuckled and smiled."
    MC "Hey Kodama-san. What's up?"
    PRG "Uhm...nothing much. I was...wondering if you would like to spectate another match with me?"
    MC "Oh? The Dragons are playing again? Their matches are pretty tightly scheduled this season..."
    PRG "Y-yes. This week they definitely are."
    MC "Well, sure thing. In the cooking room again, I presume?"
    PRG "Yes, I'll be making some sweets for Alice. She gave me a recipe to follow."
    MC "Sounds good! Let's see if I can't help you out with that, then."
    show PRG happy
    PRG "Yay!"
    "I packed my stuff and left the classroom with Aida. Together we walked towards the clubroom and went about our business."
    jump daymenu
    
label PRG013:
    $setProgress("PRG", "PRG014")
    scene F1 Hallway with fade
    play music Schoolday
    "I strolled past the classrooms, into the clubroom hallway."
    "Naturally, I found myself gravitating towards the lovely aroma of what I assumed to be lovely food."
    "As I got closer, I realized the smell wasn't the usual sweet. Rather savory instead."
    "I peeked inside the cooking clubroom."
    scene Classroom with fade
    show PRG sad at Transform(xzoom=-1), Position(xpos=0.65) with dissolve
    "For a change, Aida wasn't the only one inside. On the other side of the room, a trio of girls seemed to be working together."
    "Judging from the high amounts of steam present, the aroma was caused by the dishes they were making."
    "Aida, however, was still making some kind of batter in her own little corner."
    "She didn't seem to be stirring with as much excitement as she usually did."
    "I waited a moment before finally stepping into the clubroom. The sound of my shoe hitting the tiled floor made enough sound for Aida to turn around."
    "She smiled instantly at the sight of me approaching."
    show PRG happy at Position(xzoom=1)
    "She released the spoon to wave, keeping quiet as the girls beside her chatted about. I moved closer before greeting her."
    MC "Good afternoon, Kodama-san."
    PRG "Hello Hotsure-san! What brought you here?"
    MC "Hm? You, of course. I wanted to see how you're holding up."
    show PRG unique
    PRG "O-oh...W-well...as you can see, the club president is back."
    "I glanced over, trying to figure out which of the three was the president."
    "Her distance from the workstations and confident posture were enough to give it away. The style of her long, brown hair reminded me of Alice, but nowhere near as refined."
    "The president turned around, our eyes meeting but hers immediately turned back to continue talking to the other club members."
    MC "Huh. For some reason, the thought of there being more members in this club never occurred to me."
    show PRG neutral
    PRG "I heard the president had family matters that suddenly came up. Fortunately, nothing b-bad happened."
    PRG "The others...well, it was just me during that time."
    "The club president made her way over to Aida's workstation; no doubt, to welcome me."
    show PRG sad
    UNKNOWN "Hello there. You a friend of Kodama-chan?"
    menu:
        "Yes, a good friend.":
            MC "A good friend, yes."
            if getAffection("PRG") < 7:
                $ setAffection("PRG", 3)
                $ setFlag("PRG013_goodfriendslie")
            "Aida inhaled sharply, staring at me with wide eyes. The president didn't seem to notice it, as she continued to talk."
            UNKNOWN "Neat! Maybe you can help us convince her to join the competition!"
        "Yeah, we're friends.":
            MC "Yeah, we're friends."
            UNKNOWN "Neat! Maybe you can help us convince her to join the competition!"
        "We're just classmates.":
            $ setAffection("PRG", -1)
            MC "We're just classmates."
            show PRG sad
            PRG "J-just...classmates?"
            if getFlag("global1000_aidasit"):
                PRG "I...I thought we were friends?"
                MC "Oh! Yeah, of course. I kind of forgot about that, sorry Kodama-san."
            else:
                MC "Yeah...well, I mean...I wouldn't want to overstep my boundary by suddenly declaring us as friends."
                PRG "A-ah... Yes, of course..."
            UNKNOWN "Well... maybe you can help us convince her to join the competition."
    MC "Like a cooking competition?"
    UNKNOWN "Exactly that. Though we're trying to keep it friendly in nature. I figured it'd be fun to do with the club!"
    MC "It does sound fun."
    "I look over at Aida who wasn't thrilled at all, judging by her expression."
    PRG "I don't know... I-I'm sorry..."
    MC "Why not? You're great at cooking! This is a great way to put it to the test."
    PRG "I could... but I'm not that competitive... I just like to cook for my friends and family."
    UNKNOWN "Oh well. Was worth a try with you on our side. Was nice talking to you...?"
    MC "Hotsure."
    UNKNOWN "--Hotsure-san. I'm Michiko, by the way."
    MC "Ah! Likewise, Michiko-san."
    "Michiko rejoined the two, who seemed to be nearly finished with their dish."
    show PRG unique
    PRG "Sorry..."
    MC "Hm? Don't worry about it. You might be looking at it the wrong way though."
    PRG "O-oh?"
    MC "This competition won't be like... say, baseball. A lot is on stake for each of the teams there."
    MC "This sounds to be way more laid back than that. I've witnessed one back in high school, it's totally different from that."
    MC "It's not about beating the other team, it's just about creating the best taste you can. Everybody wins, in a way, because at the end of it there's a bunch of delicious food other people get to enjoy."
    show PRG neutral
    MC "It'll also be a great opportunity to learn from the others! Tips and tricks, new recipes and maybe even some friends."
    MC "On top of it all, I'll be here to cheer you on."
    show PRG aroused
    PRG "Y-you'd do that for me?"
    MC "Of course, I'd love to."
    PRG "Hehe... That does sound quite nice..."
    MC "Cool. I'll bring some banners and a giant finger to cheer you on!"
    show PRG surprised
    PRG "W-whaa!? N-no... that's way too much!"
    MC "Hahah, you know I'm only joking right?"
    show PRG unique
    PRG "Oh..."
    MCT "Guess I wasn't obvious enough with that one."
    MC "Well, what do you say?"
    show PRG happy
    PRG "Well... if you're there... alright. I'll try my best."
    MC "There you go! I'm sure you'll do a great job at it."
    PRG "T-thank you. I hope so."
    jump daymenu
    
label PRG014:
    $setProgress("PRG", "PRG015")
    play music Schoolday
    scene Classroom with fade
    "After the usual History classes, lunch break arrived. I particularly felt like hanging out with Aida again, possibly getting to know her better. I glanced around the classroom to find Aida nearly hopping to my desk with her hands behind her back. In all of her bouncing glory."
    MCT "Jeez, someone's excited."
    show PRG happy with dissolve
    PRG "Hello, Hotsure-san!"
    MC "Good mor-... er, afternoon, Kodama-san. Having a good day, huh?"
    show PRG neutral
    PRG "A-ah! Well... I... I have made something for y-you!"
    "With that, she revealed the mystery object behind her, a small box, wrapped in a brightly-colored napkin. Aida held it out with both of her hands."
    "I held it by the knot and carefully lowered it on the table. My curiosity as to what's inside grew by the second. Before I could open my mouth to ask her about it..."
    show PRG unique
    PRG "L-lunch! It's... uhm... It is a lunchbox. I m-made it for you."
    MC "Ooh! How nice of you, Kodama-san. I can't wait to start eating it."
    show PRG happy
    PRG "Hehe... I'm glad..."
    MC "Well, let's get to the cafeteria and try it out. Unless you have any plans, of course."
    "She shook her head. We grabbed our stuff and headed for the cafeteria."
    play music Peaceful
    scene Hallway with fade
    "Aida held onto my shirt from behind me, as we maneuvered amidst the crowd of students with the same destination. I wanted to ask about her practice for the cooking competition, but that will have to wait until we get there."

    scene Cafeteria with fade
    "The two of us had the privilege of carrying our lunch. Instead of waiting in line, we sat down right away, next to each other."
    show PRG neutral with dissolve
    "I rubbed my hands before carefully untying the knot and opening the lunch box that she had prepared for me. I wasn't sure what kind of expectations I had, but they were surpassed by a long shot."
    "As usual with bento, the box was divided up into sections, each with its own food type. Rice, fruits, meat and vegetables. It was all there. The vibrant colors were a sight to behold."
    if getAffection("PRG") > 8:
        extend " Not to mention the sauce in the shape of an heart."
    MC "Wooow. If... if this tastes as good as it looks, I totally have to marry you."
    show PRG surprised
    PRG "W-w-w-wha?!"
    show PRG aroused
    extend " R-really? You'd..."
    MC "Huh? I meant it as a joke obviously, it would be way too soon and rude to even consider that."
    "Aida was clearly flabbergasted by my comment, as she was blushing red while playing with her fingers."
    PRG "A-ah... Of course..."
    MCT "Well... time to break the ice again."
    show PRG neutral
    "I took out my chopsticks, picked up some of the rice and ate it."
    "Before I could commend Aida on her cooking skills, my eyes jumped to Aida's lunch. Or rather, the lack thereof. She had been watching me eat this without getting anything herself?"
    "I took a glance in the opposite direction, the queue for the cafeteria lunch was still quite long. So going out to grab one would probably take a good chunk of time."
    MC "Uhm... did you not make enough for yourself?"
    PRG "N-no... I had to redo some of it, so I ended up only enough to overstuff your box instead."
    MC "Well, we can totally share if you want. You made it after all."
    PRG "Nah... there's no need. It's all yours."
    MC "Hrmm... okay, if you say so..."
    "With hesitation, I continue to eat the lunchbox. Wasn't expecting her to be so selfless."
    MC "So, how's the competition going?"
    PRG "O-oh! W-well... There will be practice for a few days before the first match, which is actually in teams of two..."
    MC "Huh, that's nice. Have you met your partner then?"
    PRG "Y-yes. During the training we also kinda got to know each other... She... she seems nice."
    MC "Awesome. Who knows, you might make a friend while you're at it."
    show PRG unique
    PRG "Heh... I don't know... I'm not sure if I could, with the competition and all."
    MC "Oh yeah. Just uhm... just focus on the competition then. Kinda feel it out, you know?"
    show PRG neutral
    PRG "Right. I'll do that."
    "Hearing her having issues with focusing on the competition made me feel extra guilty. I glanced down at the overstuffed lunchbox. I basically forced her to enter it. And now she threw herself in the deep end, with no lunch to enjoy. I should..."
    menu:
        "Slide the lunchbox to her":
            jump PRG014_c1_1
        "Feed a piece to her" if getAffection("PRG") > 8:
            jump PRG014_c1_2
        "Feed a piece to her (disabled)" if getAffection("PRG") <= 8:
            pass
        "Take her word for it and finish it":
            "I continued eating lunch. I already asked her earlier and she refused. I wouldn't want to pressure her again."
            jump PRG014_c1_after

label PRG014_c1_1:
    "I placed the chopsticks on the lunchbox and shoved it to in front of Aida. Even if she made it for me, I wouldn't want her to starve because of it."
    MC "Please, have some yourself. I really don't mind if you do."
    show PRG sad
    "Aida reluctantly stared at the box, clearly contemplating her options. She took a deep breath before picking up the chopsticks."
    show PRG neutral
    PRG "Okay... if that's what you want."
    "She initially took a nib out of the piece of meat, licking her lips. Her face lit up, probably realizing how tasty her own food is. Her second and third bite were way more generous as a smile escaped her lips. One that quickly disappeared once she realized I was watching."
    show PRG happy
    MC "It's good right?"
    $setAffection("PRG", 1)
    PRG "Mhm-hmm!"
    jump PRG014_c1_after

label PRG014_c1_2:
    $setFlag("PRG014_c1_2")
    "I punctured a piece of meat with the chopsticks, holding it up with my other hand covering for any bits that might fall off."
    MC "Here, say 'aaah'."
    show PRG surprised
    PRG "H-Huh?!"
    MC "You really have to taste this, it is really good. Plus, I wouldn't want you to starve."
    show PRG unique
    PRG "Uhm... okay..."
    "I brought my hands closer to her. She repositioned to face me properly and hesitantly closed her eyes."
    "..."
    "That's all she did."
    MC "Uhm... you still have to open your mouth, Kodama-san."
    PRG "Oh! R-right. Sorry..."
    show PRG neutral
    "After apologizing, she opened her mouth but barely moved her jaw. There wasn't much room for me to easily drop in the food."
    "Once the piece was right in front of Aida, I gently pushed it against her lips. With some force, I maneuvered the piece inside of her mouth."
    "I took a brief moment to bask in on the cuteness of Aida as she started to chew on the piece. With her eyes still closed. Her face lit up as soon as she acquired the taste."
    show PRG happy
    $setAffection("PRG", 2)
    PRG "Mhmm! I tasted bits of it when I was making it but... you are totally right!"
    MC "Yup! And you made that!"
    MC "But uhm..."
    extend " You can open your eyes again."
    show PRG neutral
    PRG "Oh! R-right."
    jump PRG014_c1_after

label PRG014_c1_after:
    show PRG neutral
    UNKNOWN "Heey Kodama-san!"
    show PRG surprised
    "She visibly jumped in her seat. I turned around with her to see a girl approaching us, with a platter of food. At first glance, I didn't notice anything peculiar about her body."
    if getFlag("PRG014_c1_2"):
        UNKNOWN "Just passing by to say hi, didn't want to interrupt you two on your moment here."
        show PRG unique
        PRG "A-ah, Sakura-sama! It's... n-not what you t-think!"
        Sakura "Hey no worries. Must be nice to have someone close to you in a place like this, with all these changes."
        show PRG aroused
        PRG "Hehe..."
        extend " Y-yeah..."
    else:
        UNKNOWN "Just passing by to say hi. Good job on those cinnamon rolls yesterday!"
        show PRG happy
        PRG "Oh! T-thank you!"
        UNKNOWN "It'd be nice if you could show me how to make them. I was kinda busy with my own dish back then. If you'd like to, of course."
        PRG "S-sure. I'd... I would love to."
        UNKNOWN "Nice!"
    Sakura "Oh right. I'm the cooking partner of Kodama-san for the competition. Name's Sakura. Nice to meet you, Hotsure-san."
    MCT "Wait... I don't think I told her my name."
    MC "Ah! Likewise, Sakura-san. You seem like a great partner for Aida."
    show PRG surprised
    extend " Honestly, I'm rather relieved because I put her thr-... what?"
    "The two had an equally surprised expression on their faces. I looked at the box, then my body, but nothing that stood out."
    Sakura "A-anyway, I'll go join my friends over there. Looking forward to working with you Kodama-chan!"
    show PRG happy
    PRG "L-Likewise!"
    MC "You were right on that one."
    show PRG neutral
    PRG "Hm?"
    MC "She does seem nice."
    jump daymenu

label PRG015:
    $setProgress("PRG", "PRG016")
    scene Dorm BBW with fade
    show PRG sad with dissolve
    play music Sunset
    PRG "I'm sorry to lend your time like this..."
    MC "Don't worry about it! Getting you up to speed is also a way for me to refine my studies, making sure I didn't forget bits."
    show PRG neutral
    "I looked over behind her, the orange sky was slowly transitioning into a dark night. Truthfully I had hoped to spend my evening differently, the day ended up pretty tiring. But when Aida asked me for her help, with those eyes... My heart faltered."
    "Nevertheless, it was intriguing to see how Alice and Aida arranged their dorm room. The divide was eerily similar to mine and Daichi's. Rather than Daichi's cluttered half, Alice's looked more like a fancy five-star hotel. The bed, chairs, table, just about everything appeared incredibly luxury. How much did she bring from her home..."
    scene Dorm PRG Day with dissolve
    show PRG neutral
    "And Aida's side was quite simple, but looked cleaner than any of ours did. Like it was straight out of a magazine cover."
    PRG "S-so... Where did you want to begin?"
    MC "Hrm... let's do a quick refresher of what you already know."
    scene black with fade
    "We spent the next half hour making sure she was caught up, as most of the theory that she has problems with will presumably be in the test tomorrow."
    "After that we took a quick break, where Aida seemingly went all out on studying snacks. I pointed it out, but as expected, she said it wasn't any trouble at all. We continued on studying and snacking away."
    "As I continued... I started to notice Aida's gaze being on me, rather than the book in front of her. I tried to not let it hinder me, but time only made her staring stand out more."
    scene Dorm PRG Eve with fade
    MC "What's wrong? You having trouble focusing?"
    if getAffection("PRG") <= 2:
        show PRG sad
        PRG "S-sorry! Could you repeat the question please?"
        MC "Sure thing."
        "And so I did. We continued for another hour until curfew approached."
        jump PRG015_after
    else:
        show PRG unique
        PRG "Eep! N-no... It's just... there's something on your face."
        MC "Oh. Where?"
        PRG "The left corner of your mouth."
        "I proceed to lightly wipe it with my finger, checking if some residue showed up. But no luck."
        PRG "A... A bit lower. No... more to the righ- Ah! Too far... Okay, hold on."
        "I paused as Aida looked around her on the ground. After not being able to find what she was looking for, she got up from her sitting position and kneeled over the low table, her left hand resting on the table."
        "I instinctively looked away as she made her way closer to me. But then I realized I had to be facing her. My head turned back, my eyes darted to her impressive bust which nearly seemed to be touching the table. I prevent myself from staring and quickly looked up."
        "Even from the corner of my eye, I could see her face light up red as her hand reached my left cheek. Her soft thumb delicately wiped off the filling off of my face. She made doubly sure it was clean, then made her way back to her initial position."
        show PRG aroused
        PRG "There, all clean."
        MCT "Huh... how sweet of her."
        MC "T-thank you, Kodama-san."
        MCT "Crap, I can feel my cheeks warm up. Quick."
        MC "Anyway! Where were we? Ah right... Nobunaga."
        MC "What uhm-... Which two clans are the presumed ancestors of the Oda clan?"
        if getAffection("PRG") <= 8:
            show PRG sad
            PRG "The Fujiwara and... uhm... Taira clan?"
            MC "Yup! That's totally right. See? You'll do just fine!"
            show PRG happy
            PRG "Hehe..."
            "We continued for another hour, where Aida ended up feeling pretty confident in her knowledge. Which was quite interesting to observe."
            jump PRG015_after
        else:
            MC "Hm? Kodama-san?"
            "I looked up from the book. She was staring at a corner of the table, seemingly in a trance while sucking on her right thumb."
            stop music
            MCT "...Wait."
            MCT "Which thumb did she use to clean my face? Was it... no... She wiped my left cheek, so she'd use her right hand if-..."
            extend " Oh no."
            "I was unsure of what to do. Aida's eyes had a dreamy look, and her cheeks blushed like when she wiped my cheek. Her jaw moved slightly as she swirled it around her mouth before swallowing it. She closed her eyes before licking her lips."
            "When she opened her eyes, and noticed me staring at her for... however long, they jumped wide open."
            show PRG surprised
            PRG "A-... I..."
            show PRG unique
            PRG "..."
            show PRG unique:
                ease 1 yanchor 0.9
            "Aida lowered her posture, seemingly trying to hide under the low table. Which was probably impossible with her figure. Her gaze was fixed downwards. She remained in complete silence."
            play music Sunset
            MC "Let's... uh... *ahem* let's continue... There's only a bit more to learn. After that I think you'll be fine."
            PRG "O-okay."
            "And so we continued. Both me and Aida had trouble focusing on the task at hand. I tried to ignore it but it kept nagging my mind."
            "Eventually we put a stop to the studying session, about an half hour before curfew."
            jump PRG015_after

label PRG015_after:
    play music Schoolday
    scene black with fade
    pause 1
    scene Hallway with fade
    show PRG neutral with dissolve
    PRG "Thank you so much for helping out, Hotsure-san."
    MC "No problem. You'll do just fine tomorrow!"
    show PRG happy
    PRG "I hope so!"
    MC "Don't be afraid to ask me for help! But.. maybe do it a bit earlier than the day before. Anyway, have a good night and see ya tomorrow, Kodama-san."
    PRG "B-bye!"
    "We waved at each other before she closed the door, and I made my way back to my room."
    scene Dorm Interior with fade
    "I shoved the door behind me hard enough for it to close. I let out a deep sigh. My mind's totally maxed out. Lots of theory to digest and helping out Aida on top of that?"
    if getAffection("PRG") <= 8:
        "I threw myself on my bed, mentally exhausted from all the studying. Daichi was still reading a book on his bed, but I had little energy left to strike up a conversation."
        scene black with fade
        "I closed my eyes, letting out a deep sigh. It didn't take long before my subconscious slipped into a deep slumber."
        jump daymenu
    else:
        "I noticed Daichi still was reading a book on his bed. We greeted each other, and I decided to inquire for a second opinion. I explained what had happened during our study session."
        scene Dorm Interior with fade
        show RM neutral with dissolve
        MC "And I'm pretty sure she put it in her mouth. It looked like she was really enjoying it."
        RM "Sounds like she wants something from you, man. And this was during studying?"
        MC "Yeah... I just... It just doesn't make any sense coming from her."
        RM "You never know, Keisuke. Or she was really hungry."
        RM "Who were you studying with again?"
        MC "Huh?! Aida Kodama. Small, meek girl. Twin tails? She has-... nevermind. You wouldn't recognize her. Maybe if you'd show up to class more than once a week."
        RM "Doesn't mean I don't know a thing or two about the students. I know exactly of whom you speak. Her growth factor however... I haven't been able to determine exactly what it is. Maybe..."
        if isEventCleared("PRG012"):
            MC "Why is everyone so interested in knowing her growth factor? You don't even know her!"
            extend " ...right?"
            RM "I can only speak for myself, but I need to explore every mysterious avenue to truly find out what's going on here."
        else:
            MC "Please don't do anything illegal."
            show RM smug
            RM "Oh don't worry. I won't be caught."
        MC "I... I guess. In any case. I really can't see her doing something like that. It doesn't..."
        show RM neutral
        RM "Fit her nature? Maybe. Maybe you're right. Or... it's purely for her own gain."
        show RM sad
        RM "...Okay no... That is actually worse. Forget I said that."
        MCT "Great. That definitely didn't help."
        MC "Well... Nevermind. Thanks anyway. I'm just gonna head to bed. Hopefully get some sleep in before the test tomorrow."
        show RM neutral
        RM "Alright, I'll dim the lights then. Good night."
        MC "Good night."
        scene black with fade
        RM "...."
        RM "Wait. Hold on..."
        extend " There's a test tomorrow?"
        jump daymenu

label PRG016:
    $setProgress("PRG", "PRG017")
    scene Classroom with fade #[SCENE CLASSROOM_DAY]
    play music Busy
    show AE happy with dissolve
    AE "Thank you for your assistance, Hotsure-san."
    MC "Not a problem. That didn't take much time at all."
    "I gazed back into the classroom. All of the desks and chairs were rearranged for a more “optimal” setup. In the end, I didn't notice much difference, but I had no intention of doubting Matsumoto."
    AE "True."
    show AE neutral
    AE "Now if only everyone else wasn't so eager to leave the very moment I turned to get their attention..."
    MC "Yeah... I'd imagine they felt that something was coming, and didn't want to stick around to find out what it could be."
    AE "Hrm... I'll have to bring it up to the class tomorrow. It worked out fine today, but imagine if the issue was significantly more serious."
    MC "Yeah, I'd mention it tomorrow just to get your point across. But, for now, I have to run. Have a good afternoon, Matsumoto-san."
    show AE happy
    AE "Same to you, Hotsure-san."
    
    scene Hallway with fade
    "I left the room and hurried off down the hall, making sure that my footfalls weren't too heavy, lest Matsumoto hear me running."
    "I rounded the corner and closed in on the clubroom hallway, smelling the sweet aroma of the competition before I even could see the room."
    "The competition was already underway, with two teams of two at their own designated cooking set. The other side of the room had a bunch of chairs neatly arranged, presumably for the audience."
    
    scene Classroom with fade #[SCENE CHANGE CLASSROOM_DAY]
    "I quietly made my way over to the spectator chairs. Aida, who must've already spotted me entering, smiled and tapped the empty chair next to her. I happily accepted, sitting down next to her."
    show PRG happy with dissolve
    PRG "H-Hotsure-san! I'm glad you could make it."
    MC "Of course! I practically dragged you into this, seems only fair that I join you today."
    PRG "Hehe... true."
    Sakura "Oh! Hello, Hotsure-san. Lovely of you to join us."
    "I turned to see Sakura approaching us, bouncing up and down like a kid with one hell of a sugar high."
    MC "Heh, lovely to see you as well, Sakura-san."
    jump PRG016_c1
    
label PRG016_c1:
    menu:
        "Already know what you guys are going to make?" if not getFlag("PRG016_c1_1"):
            jump PRG016_c1_1
        "Already know what you guys are going to make? (disabled)" if getFlag("PRG016_c1_1"):
            pass
        "Are you excited?" if not getFlag("PRG016_c1_2"):
            jump PRG016_c1_2
        "Are you excited? (disabled)" if getFlag("PRG016_c1_2"):
            pass
        "When are you guys up?" if not getFlag("PRG016_c1_3"):
            jump PRG016_c1_3
        "When are you guys up? (disabled)" if getFlag("PRG016_c1_3"):
            pass
        "Stay silent and observe the round":
            jump PRG016_c1_after

label PRG016_c1_1:
    $setFlag("PRG016_c1_1")
    MC "What are you guys planning to make?"
    Sakura "Cinnamon rolls!"
    show PRG neutral
    PRG "Hehe, yeah... Since the first round is bakery and we've already made together once before. We figured it would be our best shot."
    MC "Alright, nice. Sakura seems pretty keen on making them again, huh?"
    Sakura "You betcha! She's totally underselling herself. The way she makes them... It's the perfect balance of sweet and taste. They're the best I've ever had."
    show PRG unique
    PRG "Sakura-san... It's really too much..."
    MC "Well, if she really enjoys them that much, It'll be perfect for this round, yeah? They'll definitely impress the judges."
    PRG "Y-Yeah. I hope you're right."
    jump PRG016_c1

label PRG016_c1_2:
    $setFlag("PRG016_c1_2")
    MC "Are you excited?"
    show PRG unique
    PRG "Y-Yeah. But... I'm a little nervous too."
    MC "Don't worry too much, just try to relax. Take a few deep breaths."
    "Before I even finished my thought, Aida already had her eyes shut and gave a slow exhale."
    "Sakura looked over, first to Aida, then to me, and smiled. I returned the smile before glancing back at the current competing teams."
    "Several minutes passed as they put the finishing touches on their dishes."
    jump PRG016_c1

label PRG016_c1_3:
    $setFlag("PRG016_c1_3")
    MC "When are you guys up?"
    show PRG neutral
    PRG "Right after they're finished."
    if not getFlag("PRG016_c1_2"):
        PRG "It sure makes me nervous... waiting for our turn."
        MC "Yeah, I can totally understand that. Waiting for your turn to present, it's a feeling like none other..."
        MC "B-but! I'm sure you two will do just fine."
        PRG "Thanks! I hope so too..."
    else:
        MC "Oh nice! I really did join just in time."
        PRG "Yup! I'd say that's one of your best qualities."
        MC "Ha-... Eh?"
        MCT "If it were from any other girl I'd shrug it off, but it coming from her... Seems she's actually gotten more relaxed."
        MC "Well, I'd prefer that over always arriving late."
    "We both continued watching the contestants."
    jump PRG016_c1

label PRG016_c1_after:
    hide PRG with dissolve
    "I watched the two competing teams, carefully observing their technique. The minutes flew by quickly until it was Aida and Sakura's turn."
    "Suddenly a loud bell rang from the Announcer's stand."
    Announcer "TIME!"
    "Both teams gingerly grabbed their completed dishes and brought them to the judges table to await their results."
    Announcer "NEXT ROUND!"
    "Aida and Sakura both nodded to the announcer and rose from their chairs. It was finally their time to shine."
    show PRG neutral with dissolve
    Sakura "Well, wish us luck!"
    menu:
        "You've got this!":
            pass
        "I believe in you!":
            pass
        "You guys can do this!":
            pass
    PRG "T-Thanks!"
    stop music
    "Both of them made their way through the field of chairs and onto their kitchen set, and waited for the announcer to start the round."
    "Across from them, their opponents took their stations and stared down Aida and Sakura."
    Announcer "BOW!"
    "Both teams bowed respectfully to the other pair, as a show of good sportsmanship."
    play music Tension
    Announcer "AND BEGIN!"
    "The bell rang out again and the two teams began. Sakura flew to the fridge and grabbed out a gallon of milk, a carton of eggs and a large stick of butter, while Aida began combining sugar, salt, and flour into a large bowl."
    "Sakura quickly measured the milk and butter before slowly heating them on the stove. As they heated, she grabbed two eggs out of the carton and passed them to Aida. Taking the egg in one hand, Aida deftly cracked and emptied it into the bowl."
    show PRG unique
    "As she passed the other egg into her cracking hand, her hand slipped and the egg fell to the countertop, scattering shell pieces and yolk across their workstation."
    MCT "No. Not now."
    "Sakura wasted no time in getting another egg, as Aida quickly wiped the counter clean. This time, she held the egg more firmly and cracked it into the bowl."
    "Meanwhile, Sakura armed herself with two spoons and slowly stirred the milk and butter, while Aida reached her free hand across the counter and pulled a large hand mixer toward her."
    "However, when she pressed the power button on the top, her finger nudged the eject button for the whisks and they came loose, clattering down onto the counter next to the bowl. Aida hurriedly jammed them back into their slots and glanced over to me, her face reddened in frustration. I shot her a quick thumbs up and mimicked the motion of a deep breath."
    "She momentarily shut her eyes and deeply inhaled. It was just then that Aida seemed to find her magic touch."
    show PRG angry
    "She opened her eyes and pressed the mixer into the bowl, turning it to medium speed. As Aida blended, Sakura went to work activating the yeast and joined Aida by the blender, slowly adding the butter to Aida's concoction."
    "The two of them were simply incredible to watch, working together like gears in a clock. Since Sakura knew this was one of Aida's specialties, she let Aida handle the main parts while she supplemented as needed."
    "Finally, Sakura carried her now activated yeast and emptied it into the bowl. Aida turned her mixer onto a higher speed as the dough began to thicken, while Sakura hurried to the other side of the counter and began to work on mixing the filling and frosting."
    "Soon, Aida had her dough on the counter and began kneading it until it smoothed out and became almost stretchy. Sakura grabbed an extra bowl from her side of the counter and covered it with oil. Taking the bowl from her, Aida took her doughy blob and pressed it into the bowl, covered it in plastic wrap, and set a timer next to the bowl for the sake of precision."
    show PRG neutral
    "Letting her dough rise on the counter, Aida came to Sakura's side of the counter and helped her prepare the filling and frosting. As they worked, my gaze wandered to the other team's side. It looked as though they were making a pie of some sort, but I had no way of telling how far along they were, or even what kind of pie they were making."
    "In no time at all, Aida had the cinnamon rolls baked and filled, while Sakura applied a light layer of filling to the top. Just as Sakura drizzled the last spoonful on top, the announcer's bell rang out loud and clear once more."
    stop music
    Announcer "TIME!"
    "Aida breathed a sigh of relief and looked over to Sakura, who gave her a reassuring nod."
    "Aida picked up her pan of cinnamon rolls and awkwardly carried them over to the judges table, setting them down gently in front of them. Sakura joined Aida and put a comforting arm around her shoulders."
    "Minutes passed. Each of the three judges tasted the cinnamon rolls, then tasted the other team's pie. Since spectators weren't allowed at the judges table, all I could do was sit there and hope that I could read lips well enough to figure out what they were saying."
    "The three judges whispered amongst themselves for a few moments before one of them wrote something on a sheet of paper and passed it to the announcer."
    Announcer "And the winner is..."
    play music Busy
    Announcer "... Kodama-san and Sakura-san!!"
    show PRG happy
    "The room erupted in applause. Aida bounced happily, a smile spread wide across her face, and embraced Sakura, who looked like she was near tears."
    "Breaking apart from Sakura, Aida hurried across the room towards me, her face lit up like a Christmas tree."
    PRG "Hotsure-san! We won! We won!"
    MC "Congratulations, Kodama-san! You guys did amazing!"
    show PRG unique
    PRG "I have to thank you though... I-I started to panic and my hands wouldn't stop s-shaking."
    PRG "Then, I looked over to you and you reminded me just to take a breath. I... I guess what I mean is, I couldn't have made it through this without you, Hotsure-san."
    "I was about to speak when, in a flash, Aida had her arms wrapped around me in a tight embrace."
    show PRG happy
    PRG "T-T-Thank you!"
    MC "Erm... Of course! Anytime!"
    "Aida pulled away from me and rubbed her head sheepishly, before promptly taking the seat next to my own."
    "As the day wore on, more competitors came and went. Out of respect, Aida and I stayed seated and watched the remaining rounds go by, until the final round had ended and the spectators began to file out of the room."
    show PRG neutral
    PRG "I-I think I'd better help pick up the room a bit, Hotsure-san."
    MC "Good idea, what can I do to help?"
    PRG "I didn't say you had to help too..."
    MC "No you didn't, but I'm volunteering. Now you'd better tell me where everything goes before I start piling the dirty dishes inside the oven."
    "Aida shook her head and for the next hour or so, I helped her rearrange everything back to its usual state. Dishes were washed, leftover ingredients were sorted and stored, and load after load of trash was taken out."
    MC "Whew! All done?"
    PRG "We should be."
    MC "Great. That wasn't overly difficult."
    PRG "Not at all. As they say, many hands make light work."
    scene Hallway with fade
    stop music
    "Aida flicked the lights off and led the way out the door, closing it softly behind us. By now, night had fallen, giving the school's hallways a dark and almost haunting feel as the pale moonlight crept in through the windows."
    MC "So... I'll see you tomorrow then?"
    show PRG unique
    play music Sunset
    PRG "H-Hotsure-san? Could I ask a favor of you?"
    MC "Sure, whatever you need."
    PRG "C-Could you w-walk me back to my dorm?"
    "I glanced down the hallways, which almost looked as if they led off to nowhere but more darkness. Even I had to admit, it was a little spooky."
    MC "Absolutely."
    "I set off down the hallway with Aida directly by my side. Soon, we found our way to the schoolyard and began the walk across to the dorms."
    
    scene Campus Center with fade #[SCENE CHANGE CAMPUSCENTER_EVE]
    show PRG neutral with dissolve
    PRG "Thank you again for coming today, Hotsure-san. It was nice to have someone I knew watch me."
    MC "It was my pleasure. You guys are a lot of fun to watch."
    PRG "Hehe... Thanks. But I couldn't have done it without Sakura. She's the real reason we won."
    MC "You two are becoming pretty close friends now, aren't you?"
    PRG "Y-Yeah. I guess you could say that."
    MC "Well, that's what being in a club is all about. Meeting new friends and enjoying doing something you love together."
    "Aida nodded slightly, her shoulder length hair shimmering in the clear moonlight."
    PRG "I wouldn't have met her if it wasn't for you, Hotsure-san. You're the one who... encouraged me to join."
    MC "Oh, I'm sure you two would've met up sooner or later. You both love cooking so you would've already had common ground."
    PRG "Still..."
    "I noticed then that as we had been walking, Aida had been drifting closer and closer to me until her newly widened hips brushed against me. Rather than pulling away and souring the experience, I let her hips continue to bump into me."
    MCT "They're... unusually soft."
    
    scene Dorm Exterior with fade
    "It wasn't long until we were walking down the hall toward her dorm room, and Aida produced her key from her pocket."
    show PRG neutral with dissolve
    PRG "T-Thank you again for coming today, Hotsure-san. It meant a lot."
    MC "Think nothing of it. It was my pleasure."
    PRG "Oh, and I wanted to thank you as well, for pushing me to join cooking club. All of this wouldn't be happening if you hadn't encouraged me into it."
    PRG "Just... Thank you so much."
    MC "You're welcome. I could tell from the get-go that you had a knack for cooking. All you needed was a little extra push to let your talents shine."
    PRG "Well, I'm... I'm lucky you were there."
    "Aida inserted her key and twisted, her door opening quietly into her dimly lit and quiet room."
    PRG "Goodnight, Hotsure-san."
    MC "Goodnight, Kodama-san. And congratulations again."
    "She smiled at me one last time before shutting her door, leaving me alone in the girl's dorm hallway."

    scene black with fade
    "It was a long walk to the boy's dorms alone in the dark..."
    jump daymenu
    
label PRG017:
    $setProgress("PRG", "PRG019")
    scene School Planter with fade
    play music Sunset
    "After classes had ended for the day, I was left with not only a cramped wrist from the usual excessive note taking, but also a pounding tension headache that felt as though someone was hammering a nail deep into my forehead."
    "Rather than going back to my dorm and allowing it get any worse, I decided to go au naturel and take in a little fresh air. Seeing as how the roof would no doubt be packed with students at this time of day, I found my way to the gardens."
    "The garden was quiet and peaceful, as always. Beams of warm, afternoon sun shone down and warmed the courtyard, as I wandered around for a moment, looking for a place to rest my head."
    "I sauntered over to a nearby tree in the middle of the garden and sat underneath it, feeling the cool bark behind me. I sighed softly and closed my eyes."
    
    scene black with fade
    "I listened to the sound of my own breathing, and heard the faint tweeting of birds nearby, along with a gust of wind blowing the tree's leaves this way and whistling as it blew past Seichou's buildings."
    "I could feel myself just beginning to doze off when I heard a sort of... tapping and scratching?"

    scene School Planter with fade
    "I lazily opened my eyes and looked off toward the source of the unusual sound. At first, all I saw was the bright green bushes and the wide variety of trees that littered the landscape. I let my gaze follow the line of bushes until I came to a small cluster of flowers surrounding a large, willow tree."
    show PRG neutral with dissolve
    "Aida sat amongst them, observing one of the luminous, pink flowers. As I looked on, I noticed a tiny sketchbook and a pencil in her hands. From time to time, she'd tap the pencil on the sketchbook page, as if pondering how to go about drawing the flower."
    "Gently, she reached over and adjusted a petal on the flower ever so slightly, before taking up her pencil and sketchbook once more, and slowly beginning to draw the flower."
    "Using the tree trunk as a support beam, I heaved myself shakily to my feet before haphazardly throwing my backpack over my shoulder and walking over to where she sat, brushing the long willow branches out of my face as I went."
    show PRG surprised
    PRG "Oh! G-Good afternoon, Hotsure-san!"
    MC "Good afternoon, Kodama-san. I hope I didn't startle you."
    show PRG neutral
    PRG "N-No. Not at all."

    menu:
        "I never knew that you could draw.": #PRG +1
            jump PRG017_c1_1
        "That's an Azalea, right?" if isEventCleared("GTS002"): #PRG +2
            jump PRG017_c1_2
        "That's an Azalea, right? (disabled)" if not isEventCleared("GTS002"):
            pass

label PRG017_c1_1:
    MC "Wow, I never knew that you could draw."
    show PRG unique
    PRG "Yeah. I-It's not something I do very often."
    MC "Maybe you should try drawing more often, you're really good!"
    show PRG aroused
    $setAffection("PRG", 1)
    PRG "Thanks. B-But... It's only a flower. It's not like I'm drawing something complex like a face or anything."
    MC "Flowers are complex! Look at the way the petals shift when a strong breeze blows them, or the way that the entire shape of the flower shifts when the wind hits it. It's far from just a simple shape!"
    PRG "I-I guess so..."
    if getSkill("Art") < 4:
        jump PRG017_test_1
    else:
        jump PRG017_test_2

label PRG017_test_1:
    MC "Well, I definitely couldn't draw it."
    "Aida leaned over into her bag and produced another small sketchbook and pencil, then turned to hand it to me."
    show PRG neutral
    PRG "Try it. I-I want to see how you do."
    MC "Alright, but I'm warning you, your average kindergartener could draw better than me."
    "I took the pencil and gave it an artistic flourish."
    MC "Behold... The artistic stylings of... Hotsure Keisuke."
    "Aida giggled softly as I began to draw. My first attempt at drawing the stem left me with a curvy, floppy looking stick of a stem, so I scrubbed it out with my eraser and redrew it a few more times, until I had what looked like more like a tiny tree stump than a stem of a flower."
    "Then I worked my way into the petals, but whereas Aida's looked like flowing curtains elegantly curving this way and that, mine were jagged and looked as though they had been cut out with a scissors."
    "As I drew, Aida peeked her head over my shoulder to watch me work. I exhaled suddenly as I felt her breasts brush lightly against my back, sending chills of excitement down my spine."
    "I purposely took a bit longer drawing the center of the flower, not wanting the unintentional back rub to end."
    MC "And... Done!"
    show PRG aroused
    "I held up my artwork for Aida to see and her face instantly went bright scarlet as she stared at my drawing, her eyes darting this way and that across the page, as if she wasn't quite sure what she was looking at. She threw her hands over her mouth quickly to keep herself from laughing."
    MC "It's alright, you can laugh!"
    "Aida put her hands down and burst into more giggles, her whole body practically convulsing in hysterics."
    show PRG unique
    PRG "I-I'm sorry. I don't mean to laugh."
    MC "It's fine! I told you that I'm not exactly Michelangelo when it comes to this sort of thing."
    PRG "I-I know. But still, I shouldn't be so rude..."
    MC "Laughing with me and laughing at me are two entirely different things, Kodama-san. Besides, I know for a fact that you don't have a mean bone anywhere in your body."
    show PRG surprised
    PRG "R-Really? Y-You aren't just saying that, are you?"
    MC "Of course not! You're always extremely courteous and kind. From the first day I spoke to you, you've been nothing but genuine."
    show PRG neutral
    PRG "I-I... T-Thank you, Hotsure-san."
    MC "And look, now you've learned something today!"
    PRG "I-I did? What did I learn?"
    MC "You learned that I am an atrocious artist."
    show PRG happy
    "Aida didn't bother to cover her mouth this time and laughed sincerely."
    jump PRG017_test_after

label PRG017_test_2:
    MC "Would you mind if I tried drawing it?"
    show PRG neutral
    "Aida nodded before handing me a blank sketchbook and a pencil from her bag."
    "I put the pencil to the paper and began to slowly mark the paper with tiny guidelines. As Aida looked on, I drew the long, thin stem and the dark leaves branching from it before moving up to the petals."
    "Following the flow of them in the breeze, I let the pencil drift a bit on the paper to give the petals a slightly more wispy and ethereal look before feathering on the inside of the petal to give it a bit of shading. With each petal I drew, I took care to watch how the wind would blow the petal and drew it accordingly."
    show PRG surprised
    $setAffection("PRG", 1)
    PRG "Wow..."
    "After a bit more touching up, I laid the sketchbook down and set the pencil on top."
    PRG "Y-You're really good, Hotsure-san!"
    MC "Thank you, Kodama-san."
    PRG "H-How did you learn how to draw?"
    MC "I'm not sure exactly. I mean, when I was little, I'd always doodle in my notebooks during school, but I only started actually practicing drawing recently."
    show PRG sad
    PRG "It really shows. I-I think yours is better than mine."
    "She held the two sketchbooks next to each other to compare the two flowers, before handing them to me, a slightly dejected look creeping onto her face."
    MC "I don't think one is necessarily better than the other. I think it's more the difference of perspective that makes them slightly different from each other."
    PRG "Perspective? How do you mean?"
    MC "Take this for example: In your drawing, you drew the petals of the flower with a bit of a ripple at the top to indicate the petal's movement. In mine, I had the petals bending off to the side a bit, to indicate the same movement."
    MC "Both of the ways the petals were drawn show the petals movement, it's just that I chose to draw mine slightly differently. Neither of them are right, but neither of them are wrong either. It's all about artistic expression."
    show PRG neutral
    PRG "That makes a lot of sense, Hotsure-san."
    MC "That's the beauty of art. You're never really right, but you're never wrong either. It's just about drawing something the way that you see it."
    PRG "T-That's a really good way to put it."
    MC "Heh, thanks."
    PRG "T-Thanks for making me feel better."
    MC "Of course. But I really did mean what I said."
    PRG "I-I know. I believe you."
    MC "Good. How did you learn to draw by the way?"
    show PRG sad
    PRG "I just kind of picked it up here and there..."
    MC "Interesting! They always say that teaching yourself a craft is one of the most rewarding things you can do in life."
    PRG "Y-Y-Yeah..."
    "I smiled at Aida before she quickly turned her gaze away from me, staring off into the distance as if lost in her own thoughts. Her once clear gray eyes now exuded a certain heaviness."
    jump PRG017_test_after

label PRG017_test_after:
    "Aida got up from where she sat and gathered her sketchbook and pencil. I quickly scribbled my signature onto my flower before handing my sketchbook back to her."
    MC "Now that it's signed, you can sell that and make a fortune. I'm sure that there's a museum or a gallery nearby that would love to get their hands on that fine work of art!"
    show PRG neutral
    PRG "I-I'll keep an eye out for one. Until then... would you mind if I held onto it?"
    MC "Pshhh, go ahead! It's your sketchbook after all!"
    PRG "T-Thank you, Hotsure-san. I'd better get going, I need to go practice for the next round of the competition." 
    MC "Alright, Kodama-san. Have a good time."
    PRG "I-I will."
    "She smiled at me before turning toward the cooking clubroom. Rather than putting the other sketchbook into her bag with her personal one, she held it against her chest as she hurried across the garden."
    MCT "Huh, weird."
    jump daymenu

label PRG017_c1_2:
    MC "Isn't that an Azalea?"
    PRG "Y-Yes it is. It's my favorite flower."
    MC "Really? What makes them your favorite?"
    PRG "Well, I love all of their different colors. Their colors give them a certain type of uniqueness. Each Azalea is unique from the next, k-kind of like a snowflake."
    MC "I never knew that there are different colors of Azaleas. I guess I always thought they could only be pink, like the ones here."
    PRG "T-They come in lots of colors! T-There is pink, of course. But, there's also white, purple, and red. There's even bi-colored ones."
    MC "You mean like a flower with two different colors at the same time?"
    show PRG happy
    PRG "Yeah! Those ones are my favorites."
    MC "I don't know if I've ever even had a favorite flower. I mean, I've taken note of them in passing, but never have really delved deep into them."
    show PRG neutral
    PRG "R-Really? I've always loved Azaleas."
    "I watched Aida bring her pencil to the paper once more as she rounded off the edge of a petal."
    MC "Now that I look at them more closely, they kind of remind me of you."
    "Aida whipped her head in my direction, her iron-colored eyes suddenly wide and full of expectation."
    show PRG surprised
    PRG "R-R-Really? H-How so?"
    MC "Well, I know that Azaleas symbolize patience and modesty, two very important virtues that I'd say you surely possess. As for their physical presence, they're delicate and stunning to the eye, even though they prefer being out of direct sunlight."
    PRG "I-I'm s-stunning to the eye?!"
    MC "I'd definitely say so."
    "Aida's smile shone brightly as a flash of indecent pink dusted her cheeks."
    show PRG neutral
    $setAffection("PRG", 2)
    PRG "T-Thank you, H-Hotsure-san. Although I'm not sure I'd call myself that..."
    MC "Well, I'm here to tell you that you are definitely something special. No one is really 100% in love with their own appearance. Sometimes, it just takes an outsider's point of view to see your own finer points."
    show PRG aroused
    "Aida became even redder still, wringing her hands nervously as she looked up at me and flashed her brilliant smile once more."
    PRG "T-Thank you so much, Hotsure-san. I'm glad I have your point of view. I-I was thinking about going to practice for the second round tournament. W-Would you like to come help?"
    MC "I'd love to. Lead the way!"
    "Aida nodded before stowing her sketchbook in her bag and hauling herself to her feet. She stalled to brush the dirt from her skirt before coming to stand next to me."
    show PRG happy
    PRG "R-Ready!"
    "I nodded to her in confirmation before we turned and crossed the garden, heading for the cooking clubroom and talking all the way."
    jump daymenu

label PRG018:
    scene Classroom with fade
    play music Schoolday
    "Morning classes went by in no time at all, as usual. As the day wore on, I found myself glancing across the room at Aida from time to time. On occasion, I'd catch her looking at me as well, but she'd turn her head away at the last minute, trying to look inconspicuous. When we were finally dismissed from our classes, Aida popped up from her desk and walked over to mine."
    show PRG unique with dissolve
    PRG "Hello, Keisuke-kun."
    MC "Hi, Aida-san."
    "I smiled at her. It was unusual for her to be so relaxed, but her body language told a different story. She was wringing her hands, clearly trying to keep her composure."
    PRG "I couldn't help but notice that your hair must've grown again recently."
    MC "Really? I didn't notice."
    "I reached a hand up and ran it through my hair. It did feel longer, and when I pulled my hand back, it all flopped down into my eyes."
    MC "I see what you mean."
    show PRG happy
    "This made Aida bust out laughing. Aida was usually so worried or nervous about something, that when she did laugh, it seemed to brighten the whole room."
    PRG "D-do you have an appointment made to see a barber?"
    MC "No, and on such short notice, I won't be able to get in for at least a couple of days."
    PRG "Well... Maybe... I could cut your hair for you? S-so you wouldn't have to wait!"
    MC "I couldn't ask you to do something like that, Aida. You already have so much going on, I'd hate to take up more of your time."
    show PRG aroused
    PRG "I guess what I'm asking is... can I please cut your hair?"
    "I was shocked to hear her being so forward, but it would be nice to have her cut my hair for a change. Plus, I wouldn't have to wait."
    MC "Are you sure it's no trouble?"
    show PRG happy
    PRG "None at all! I love cutting hair!"
    MC "It's a deal then! So where would you like to do this?"
    PRG "Hmm... let's go out by the picnic tables after our afternoon classes. It's nice out today, and any mess we make will be easier to clean out there."
    MC "Good thinking. Let's head to the cafeteria for now, I'm starving!"
    PRG "O-Okay!"
    "We both left the classroom and hurried down to the cafeteria together."
    scene Hallway with fade
    show PRG neutral with dissolve
    PRG "If it's not too much trouble, would you mind if I brought my radio when I cut your hair? The dragons are playing again tonight and if they win, they'll be in the Japan Series!"
    MC "Of course not! Bring it, and I'll cheer them on with you!" 
    show PRG happy
    "Aida's face lit up when I said that."
    PRG "Yay! With the two of us cheering together, they can't lose!"
    scene black with fade
    "We made our way into the cafeteria together. I joined Aida at her table, once again, and we spent what was left of lunch period talking about baseball, classes, and really anything else we could think of."
    scene Campus Center with fade
    "The air was warm as I stepped out into the schoolyard. Immediately, a strong blast of wind hit me and blew my hair around like some bishounen anime. Through my blowing tufts of hair, I saw something moving in front of me. I pulled my hair apart and looked up. Aida was waving at me from the picnic tables. I ran up to meet her, trying to not be blinded by my own hair in the process."
    show PRG neutral with dissolve
    PRG "H-Hey Keisuke-kun. Are you ready for your haircut?" 
    MC "Yep, all set!" 
    "I gave Aida a reassuring smile, one of those that hopefully said 'I trust you,' and not 'please, dear god, don't screw up my hair.'"
    "I sat down at the bench, and I felt something drape over my shoulders. I took a look down to see that Aida had laid a towel down over them."
    MC "Thank you."
    PRG "You're welcome. It's how I was taught, after all."  
    MC "Have you been doing this long, then?" 
    PRG "Not for a while. My mom taught me how to cut hair when I was little."  
    MC "My mom used to cut my hair all the time when I was little. She always used to tell me 'It may not be the most glamourous haircut, but it's free.'" 
    show PRG happy
    "Aida laughed out loud at that."
    PRG "What's your family like?" 
    MC "They're not bad. It's just my mom, my dad, my sister, and I. We would always do a lot together, and we always enjoyed the time we had, but my dad worked a lot, so we were used to him going away quite often for trips and such."
    PRG "That's so nice. What's your sister like?" 
    MC "We've always been really close. She actually goes here too, but I haven't seen her much since we got here. She has a hair growth factor just like I do." 
    PRG "Really? I-I'd like to meet her sometime. What's her name?" 
    MC "It's Tomoko. She's into the Dragons too, so you two would have a lot of fun together. Oh! Did you want to turn the game on?" 
    show PRG surprised
    PRG "Oh, yes! I completely forgot!"
    "Aida spun around and slid her radio out of her bag. She messed with the channels until we heard the announcer's voice, albeit with a bit of static."
    show PRG neutral
    PRG "I'd hate to miss this." 
    "Aida turned back to my head and leaned over to reach my bangs. As she leaned over, one of her breasts pressed against my back, feeling soft like a pillow, yet surprisingly firm."
    PRG "Your hair is so thick." 
    "She ran a hand through my hair as she backed up."
    MC "It's always been that way, thick hair runs in my family."
    "Just then, the announcer's voice rang out loud and clear."
    Announcer "And it's gone! A home run for the Dragons! The score is now 3-1! If the Dragons can keep this lead, the World Series may have a new contender on their hands!" 
    show PRG happy
    PRG "YES!!!!!!!" 
    "Aida was bouncing up and down happily. Thankfully, she had set down the scissors when she had heard the announcer, so I wasn't at risk of a potentially dangerous new piercing. Suddenly, Aida looked worried."
    show PRG unique
    PRG "I... I hope they can go all the way. They really deserve it." 
    menu:
        "They'll make it for sure!":
            jump PRG018_c1_1
        "Let's hope they can keep their cool.": #-2
            jump PRG018_c1_2

label PRG018_c1_1:
    $setAffection("PRG", 2)
    show PRG happy
    "Aida smiled at me."
    PRG "You're right! It's best to stay optimistic."
    MC "This is their best season in a long time. If anyone can win, I'd put my money on them any day!" 
    PRG "I'm glad you think so. It's nice to have someone else to cheer them on with."
    jump PRG018_c1_after
    
label PRG018_c1_2:
    show PRG neutral
    PRG "W-what do you mean?"
    MC "I mean that any team can get nervous and screw up. It happens to the best of them. It's good to be hopeful for them, but don't be upset if they don't make it." 
    show PRG sad
    $setAffection("PRG", -2)
    PRG "Yeah, that makes sense I guess."
    jump PRG018_c1_after

label PRG018_c1_after:
    "Aida went back to cutting my hair, while I sat and listened to the rhythmic snips of her scissors. Each cut so precise, with no movement wasted."
    show PRG neutral
    PRG "Can I ask you something, Keisuke?" 
    MC "Sure, what's on your mind?" 
    PRG "Um..."
    "She stopped cutting for a moment. I looked back and she was looking around nervously, like someone was about to attack her or something."
    show PRG unique
    PRG  "I... I know you mentioned your feelings about your growth before, but how are you feeling now? Are you doing okay?"
    MC "I'm doing pretty well with it, at least I'd say so. I realized that with regular haircuts, I can keep mine in check, whereas most people won't have that luxury. By the way, thanks again for doing this, I could never cut it myself and not look like a disaster."
    show PRG neutral
    PRG "It's no trouble: like I said before, it's kinda fun."
    "I closed my eyes as Aida moved to my bangs once more, and just like before, her breasts brushed against me. All the while, the sound of the radio droned on in the background."
    MC "How have you been dealing with your growth?" 
    show PRG unique
    PRG "...All right, I guess."
    "There it was again. That uneasiness as soon as her growth was brought up. Whatever her growth was, she wasn't too keen on revealing it."
    MC "I'm sorry, I didn't mean to bring up a touchy subject."
    show PRG neutral
    if getAffection("PRG") > 9:
        PRG "It's alright, Keisuke. It wouldn't be hard to explain anyway, especially to a man."
        MC "Hey! Just because I'm a guy doesn't mean I don't understand things."
        PRG "I'm not saying you aren't smart. This is just... different." 
        "I decided not to press the issue any further. If she wanted to tell me, she'd tell me when she was ready, and it wasn't my place to push her."
    else:
        PRG "It's okay. Let's just talk about something else. I'm almost done here." 
    "Aida cleaned off her scissors and picked up her towel. I stood up and shook my head, sending little hairs flying in the breeze. I turned to Aida."
    MC "Thanks so much, Aida!" 
    show PRG happy
    PRG "You're welcome. I'm glad I could help you. You were starting to look a little shaggy."  
    "I looked in the hand mirror Aida had brought along and threw my head this way and that, examining every angle."
    MC "It looks really good. Maybe you should look for a career as a personal stylist."
    show PRG aroused
    PRG "I...I could never do that."
    MC "Of course you could! I couldn't pay someone to give me a cut like this. You have some serious talent."  
    PRG "You're sweet, Keisuke. Maybe I'll have to think about it a bit."
    "Just then, the radio crackled to life as the announcer's voice rang out loud and clear."
    Announcer "THE DRAGONS WIN IT! THEY'RE ON THEIR WAY TO THE WORLD SERIES!!"
    "Aida dropped her towel in shock, then a huge grin crossed her face."
    show PRG happy
    PRG "YES! FINALLY!! THEY'RE IN!!"
    "She was practically shaking with excitement, jumping up and down like a kid in a candy store."
    "I stood there staring at Aida, dumbfounded. I'd never seen her so excited, but there she was, cheering for her favorite team. It was pretty cool to see actually."
    "Aida ran over to me and hugged me, almost surprising me more than the Dragon's victory."
    PRG "Thanks for listening to this with me. You must've been my good luck charm!" 
    MC "I'd be happy to listen to more games with you if that's the case!" 
    PRG "Would you? I'd love that!" 
    MC "Count on it!" 
    PRG "Yay!!"
    "Aida looked down at her watch."
    show PRG surprised
    PRG "O-Oh no! It's that late already?! I'd better get back for cooking club, I'd hate to be late."
    MC "No problem! Thanks again!"
    show PRG happy
    "Aida gave a me a small, sweet wave, and set out across the courtyard. The way the wind was blowing pressed her skirt against her hips, accentuating them even further. A thought crossed my mind as I headed back to the boys dorms."
    MCT "She's definitely gained a little weight, probably from the cooking club. But thankfully, it looks good on her."
    jump daymenu

label PRG019:
    $setProgress("PRG", "PRG020")
    scene black with fade
    pause 2
    play sound AlarmClock
    
    scene Dorm Interior with fade
    play music Peaceful
    "I jolted out of bed and grunted as if I was coming out of an exorcism. Looking to my nightstand, I glanced down at my cursed alarm clock."
    MC "You're going to find yourself flying out of my window one of these days."
    "I let loose a yawn as I shut off the alarm and gazed sleepily at the clock face."
    MCT "Damn. 9:45 already?"
    "Being that it was a weekend, I didn't have much on my plate today, besides putting in a bit of study time for the latest exam that Tashi-sensei had dumped onto the classes lap."
    menu:
        "Study hard": #PRG +2
            jump PRG019_c1_1
        "Start the day with a shower": #PRG -4
            jump PRG019_c1_2

label PRG019_c1_1:
    "Grabbing my bag from the floor, I tossed it onto my bed and pulled out my expanse of books, with the occasional notepad strewn about here and there."
    "I had flopped down onto the bed and was about to hit the books, when I heard my phone quietly buzz on my nightstand."
    PRGCell "Hey. Are you coming today?"
    "I thought for a moment about what I could possibly be going to, before the realization hit me hard."
    MCT "Wait. Is the 2nd round of the competition today?!"
    "Flicking through my apps, I opened up my calendar and swiped to today's date, where it clearly said: 'Aida 2nd competition 10 AM.'"
    MC "Yep! On my way!"
    "I launched myself off of my bed, sending my textbooks flying, and quickly grabbed the nearest uniform from my closet. After a quick comb through my hair and a spray of deodorant, I was jogging out the door toward the cooking classroom."
    
    scene Classroom with fade
    play music Schoolday
    #[SCENE CHANGE- CLASSROOM_DAY]
    "Miraculously, I made it to the clubroom hallway without getting caught sprinting across the school courtyard. I breathed a sigh of relief and pure exhaustion as I saw a large crowd formed outside of the doorway, slowly pouring into the cooking classroom."
    "I joined the crowd and nudged my way into the classroom. From across the room, Aida waved to me and pointed next to her, where once again, a lone chair sat awaiting my arrival."
    show PRG neutral with dissolve
    PRG "G-Good morning, Hotsure-san!"
    MC "G... Good... Morning, Kodama-san."
    PRG "You ran all the way here, didn't you?"
    MC "Not all the way! I-I at least slowed down in the hallway."
    "Aida chuckled before her gaze went to the top of my head and froze there."
    show PRG surprised
    PRG "Hold on."
    "I sat, motionless, as Aida reached up and gently tugged a piece of my hair back into place. She ran her hand down my head once more before withdrawing her hand."
    show PRG happy
    PRG "There... Much better!"
    "The familiar piercing tone of the announcement bell rang loud and clear as the announcer came to stand in the middle of the room."
    Announcer "Round one will be getting underway now. Will the two competing teams please take their stations?"
    "Across the room, Sakura rose from her chair and gave Aida a thumbs up."
    show PRG neutral
    PRG "W-Wish me luck?"
    MC "You two are gonna clean up!"
    hide PRG with dissolve
    stop music
    "Aida smiled at me before standing to join Sakura at their workstation."
    Announcer "Both teams ready?"
    "Aida and Sakura both nodded, as did their opponents."
    Announcer "Then bow!"
    "Both teams bowed deeply to the others."
    Announcer "And begin!"
    play music Tension
    "As the bell rang loudly once again, Aida reached below her and pulled out an enormous steel mixing bowl, while Sakura retrieved cabbage and green onions from the fridge and began chopping furiously."
    "As their round wore on, shrimp and vegetable oil was added to their bowl, as well as a handful of other spices and herbs."
    BBW "How is she doing?"
    show BBW neutral with dissolve
    "I jumped out of my blank stare as Alice sat down daintily next to me."
    MC "Oh! Good morning, Alice. She's doing really well, so far."
    BBW "As expected. Kodama-san is far from a slouch when it comes to the culinary arts. Let's just hope that this Sakura character won't hold her back."
    MC "I doubt she will. Those two are like a well-oiled machine. They play off of each other's strengths in ways that leave little room for error."
    "Alice nodded thoughtfully before turning her attention to Aida, who was now wrapping her nearly finished dumplings in a wonton wrapper. As she wrapped, Sakura took each dumpling and added it to a large steamer."
    BBW "Ah, shrimp dumplings. If those two can prepare them correctly, it'll be an easy win."
    MC "How do you mean?"
    show BBW haughty
    BBW "You see, since dumplings are so popular, everyone knows what to expect when they eat one. If Kodama-san and Sakura-san can make theirs taste more unique than anything the judges have had before, it could easily give them the victory."
    "I looked on as Aida wrapped her last dumpling and set it in the steamer. Sakura shut the lid and set the timer nearby. Both of them sighed happily as they give each other a high five."
    "After a short while, the timer dinged and the steamer lid was opened. A savory smell of freshly cooked shrimp with a hint of garlic wafted over the crowd, with the occasional “ooh” and “ahh” being murmured here and there."
    "Aida reached into the steamer with a pair of tongs and gently pulled out each dumpling, setting them on a large plate. She handed them off to Sakura who added a touch of garnish before bringing them to the awaiting judge's table."
    stop music
    "Their opponents handed the judges their offering of Sukiyaki. Tasting was done and the judges faces remained blank and ambiguous."
    "Just as at the last competition, one of the judges wrote something onto a small sheet of paper and that was passed on to the announcer."
    Announcer "And the winner is..."
    play music Busy
    Announcer "Kodama-san and Sakura-san!"
    "As the crowd applauded furiously, Aida celebrated with her now seemingly trademark bounce."
    MC "YES! GO TEAM KODAMA!!"
    "Aida hurried from the judges table back to where Alice and I stood."
    show BBW neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show PRG surprised at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    PRG "O-Oh! Good Morning Nikumaru-sama!"
    BBW "No need for such formalities today, Kodama-san. That was a very well executed round. I expected no less from you."
    show PRG neutral
    PRG "A-And what did you think, Hotsure-san?"
    MC "Everything she said, and more! You guys did incredible!"
    Sakura "All thanks to the master chef, here!"
    "Sakura came up behind Aida and hugged her tightly."
    show PRG unique
    PRG "I-It wasn't all me. Sakura-san, you did a lot more of the work than I did."
    Sakura "Sure, I may do a bit more of the grunt work, but I don't have your finesse, your skill, your flourish, whatever you want to call it! You know exactly how every ingredient will work best and you utilize it to its fullest potential!"
    Sakura "That's a skill that isn't easily taught, Kodama-san."
    show BBW happy
    BBW "Well said, Sakura-san. Now then, I must be off. The music club has a performance coming up and I intend to sing a solo."
    hide BBW with dissolve
    show PRG unique at center with dissolve
    "Alice started toward the door, working her way through the crowds of spectators until she was out of sight."
    MC "Did you want to go do something, Kodama-san? It's still early."
    show PRG neutral
    PRG "Thank you, Hotsure-san, but I should stay and help get the room back in order once the competition is finished."
    Sakura "You handled that at the last competition, Kodama-san. Let me take care of it this time."
    PRG "A-Are you certain... ?"
    Sakura "One hundred percent! You kids go off and have fun!"
    show PRG happy
    PRG "O-Okay! Thank you, Sakura-san."
    
    scene Hallway with fade
    play music Sunset
    "Aida led the way through the crowd, with me in tow, until we were finally out in the hallway."
    MC "Well, I'm glad I'm not claustrophobic. That room was a bit cramped."
    show PRG neutral with dissolve
    PRG "Yeah, there was quite a few more spectators for this round, and there will most likely be more next week."
    MC "I don't doubt it. Anything you'd like to do?"
    PRG "C-Could we go into the city? I haven't had a chance to go see it yet."
    MC "Then today is the day for it! Let's go catch the bus."
    hide PRG with dissolve
    "Aida and I hurried toward the bus stop, catching it just in time, and rode into town, passing by the lush springtime trees as we went."

    scene Town with fade
    "Soon the bus screeched to a halt in the middle of the main street."
    MC "Here we are!"
    show PRG surprised with dissolve
    PRG "Wow... I didn't expect such a built-up city on a small island like this."
    MC "There's a lot to see, but no rush. Let's just walk a bit and see what we find."
    "Walking down a handful of blocks, we passed restaurant after restaurant, and more tourist shops than I cared to count. I never realized that, apart from the academy, the island apparently had considerable tourism."
    "Reaching the end of the block, we turned and immediately spotted a tiny ice cream parlor tucked between two shops."
    show PRG neutral
    PRG "A-Are you in the mood for some ice cream?"
    MC "I was about to ask you the same thing. I think some celebratory ice cream is in order."
    PRG "Okay!"
    "After a short wait in line, we emerged from the parlor victorious, two large ice cream cones in hand."
    MC "Let's find a place to sit down, I've never been a fan of walking and eating."
    PRG "Me either... It's harder to enjoy the food."
    "We crossed the street where a small, stone bench sat pressed against the side of a building. Being that the bench wasn't winning any awards for its size, the two of us had to sit rather close."
    PRG "I haven't had ice cream in so long."
    MC "It's been a while for me, too. Is ice cream not popular where you're from?"
    show PRG sad
    PRG "No, it is. I-I just never really had it much when I was little."
    MC "My sister was an ice cream fiend when we were younger. There was always some laying around somewhere."
    MC "I remember she once caught me trying to steal some of her stash."
    show PRG neutral
    PRG "I'm sure she taught you a lesson after that."
    MC "I did learn one thing after that:  My sister has a hell of a backhand!"
    PRG "There's something else you probably learned too..."
    MC "What's that?"
    show PRG happy
    PRG "NEVER steal a girl's ice cream!"
    "She laughed warmly, her chest gently shaking with every movement. I slowly leaned over and reached for her ice cream cone, doing my best impression of a claw machine at an arcade."
    show PRG angry
    PRG "No! Mine!"
    show PRG happy
    "She held her ice cream close to her and slapped my hand away, laughing playfully once more."
    hide PRG with dissolve
    $setAffection("PRG", 2)
    "We finished our ice cream and walked down main street for a while longer, until the sun dropped behind the steep buildings that surrounded us."
    MC "It's probably about time for us to head back."
    show PRG neutral
    PRG "Oh... Alright, good idea. I don't really want to leave though, there's so much more I want to see."
    MC "It's always a bus ride away. You can visit anytime you'd like!"
    if getAffection("PRG") > 7:
        PRG "I'd love to. But... would you come with me?"
        MC "Be delighted to!"
        PRG "G-Good."
    else:
        show PRG unique
        PRG "Y-Yeah. I suppose I can."
    hide PRG with dissolve
    "Once we reached the bus stop, we spent the time going on and on about the next round of the competition. Aida brainstormed ideas and I reviewed them as she spoke, giving what little cooking knowledge I had to offer."
    "Soon the bus picked us up and whisked us back to Seichou. Even on the bus ride, Aida kept giving more and more ideas. I had to admit, the girl had a future as a gourmet chef."
    
    scene Hill Road with fade
    "As we pulled up to Seichou's gates, I felt myself begin to come down from the high of the day's events to the relaxation of a calm night. The school was peaceful and serene at night time, the moonbeams lighting the ground and making everything have an almost hazy glow."
    "In the moonlight, Aida herself even seemed to glow, the evening light hitting her white top in a way that made her whole body seem to shimmer."
    MC "Man, I'm exhausted. My bed is calling my name."
    show PRG neutral with dissolve
    PRG "I-I'm sleepy too."
    MC "I suppose you don't normally go explore a town after winning a contest, eh?"
    PRG "N-No, I can't say that I have, but I had a really good time."
    MC "So did I, it was a great change of pace."
    
    scene Campus Center with fade
    #[SCENE CHANGE - CAMPUS CENTER EVE]
    "The two of us walked through the silent campus, the only signs of life being the hum of crickets and the occasional light in a dorm room window."
    show PRG unique with dissolve
    PRG "M-May I ask you something, Hotsure-san?"
    MC "Shoot."
    PRG "So... You and I... hanging out and going to the city together after the competition. Was this a... a date?"
    MCT "O-Oy?!"
    MC "Well... a date is two people going out and doing something, isn't it? So... yes, I guess you could call this a date."
    PRG "Wow... I'm on a date."
    MC "Yep, you are! Feels good, doesn't it?"
    show PRG happy
    PRG "Yeah!"
    "Aida was practically shaking with excitement. I half expected her to pass out."
    MC "Would you like me to make this an official date?"
    show PRG aroused
    PRG "What... What do you mean?"
    show PRG surprised
    "To her surprise, I brought my arm down and took her hand in my own, holding it firmly. She stood there for a moment, gazing at our intertwined hands, as if they were about to detach themselves from our wrists and fly away."
    MC "They aren't going anywhere, you know."
    show PRG aroused
    PRG "I-I know. It's just..."
    PRG "I-I've never been on a... d-date before."
    MC "And how would you say your first date was? Everything you ever hoped for and more? "
    PRG "Y-Yeah! It was wonderful!"
    hide PRG with dissolve
    "The moonlight seemed a little brighter as we continued our walk, hands clasped tightly between the two of us. Tired as I had been before, I felt more awake than ever now, more alive."
    "Our time together came to an end as we stood in the dark shadow of the dorms."
    show PRG neutral with dissolve
    MC "I guess... this is goodnight then."
    PRG "I-I guess so."
    PRG "I... I want to thank you, Hotsure-san. For everything."
    MC "Eh? I didn't do anything special."
    PRG "Y-You've come to every competition I've had. You've helped me train, and you pushed me to do something I love."
    MC "You have a skill in cooking, Kodama-san. It would've been a crime if I let it go unnoticed."
    PRG "Still... it means a lot. T-Thank you."
    "Rather than the quick embraces I'd come to expect from her, Aida wrapped her arms around me and pulled herself closer. After a brief moment of contemplation, I let my arms fall around Aida, holding her against me."
    "Time seemed to halt for a brief moment. Aida and I stood there in each other's arms. Not only was the world around us silent, but neither of us spoke."
    PRG "W-We'd better get to bed. I-I don't want to get you in trouble."
    hide PRG with dissolve
    "The two of us pulled apart, albeit unwillingly. Walking toward my dorm, I let the image of Aida smiling up at me sink into my mind's eye, hoping that I wouldn't forget it."
    "I didn't forget it. I never forgot."
    jump daymenu

label PRG019_c1_2:
    "Arising from my bed, I picked out clothes for the day and took a long, relaxing shower. I shut my eyes and let the warm water flow over me."
    "After my stint in the shower, I got dressed and found my way back to my bed. Opening my book as I would a long lost tome, I found the new material easy to understand and simple to remember. After about an hour, I shut the book and rubbed my eyes."
    "Glancing at my phone screen, I noticed the time was nearing 12:00."
    MCT "Lunch time. Finally."
    "I threw my shoes on and strolled out of my dorm. The sun shone brightly, and the wind was strong, whipping my hair this way and that as I walked."
    
    scene School Planter with fade
    stop music
    "Cutting through the garden was the quickest way to the cafeteria, so I made a beeline through. As I passed by the freshly trimmed shrubbery and newly grown flowers, I spotted Aida seated on a bench nearby the door to the cafeteria hallway."
    show PRG sad with dissolve
    MC "Morning Kodama-san!"
    "I bowed to her slightly as I slowed to a stop before her."
    PRG "H-Hello, Hotsure-san."
    MC "I'm heading to the cafeteria to grab a bite to eat. Care to join me?"
    PRG "N-No thanks. I already ate."
    MC "Oh? I thought the cafeteria didn't start serving lunch until 12:00?"
    PRG "I... ate at my competition."
    play music Bittersweet
    MC "O-Oy?!"
    MCT "Shit! Her competition was this morning?!"
    MC "K-Kodama-san! I-I'm sorry! I completely forgot!"
    show PRG angry
    PRG "I-I thought you liked coming to watch me cook..."
    MC "I do, Kodama-san!"
    PRG "..."
    show PRG sad
    $setAffection("PRG", -4)
    "Tears slowly began to roll down her cheeks. Standing up, she turned away from me and began to walk toward the dorms."
    MC "Kodama-san... please."
    PRG "I... I'll t-talk to you another t-t-time, Hotsure-san."
    "I looked on helplessly as she broke into a run and hurried out of the gardens, leaving me completely alone."
    jump daymenu

label PRG020:
    scene Dorm Interior with fade
    $setProgress("PRG", "PRG021")
    play music Rain
    MCT "The feeling of cleanliness, how I adore thee."
    "I trudged into my dorm room, towel around my waist, and began rummaging through my dirty clothes hamper, searching for the least odorous uniform."
    MCT "Laundry, on the other hand, how I despise thee."
    "Daichi wasn't around. He had run off before the sun was even up, some kind of weird, tinfoil contraption tucked under his arm. So I had the place to myself until morning classes began."
    "I had finally decided on a uniform, when a light, almost inaudible knock came from my door. I hastily threw on my uniform and opened the door."
    show BBW neutral with dissolve
    "There stood Alice, fist raised again to knock. Usually, she had a persistent aura of confidence surrounding her, but today, her eyes looked riddled with worry."
    BBW "Good morning, Hotsure-san. May I speak with you?"
    MC "Oh- uh, good morning, Alice. What's going on?"
    MCT "It must be important if she couldn't even wait for class to begin first."
    BBW "Would you mind if we spoke somewhere that's a bit more private? I'd rather not have our conversation picked up by wandering ears."
    MC "Understandable. Will my room work?"
    "I gestured back into my dorm. Thankfully, a bit of motivation had struck me to clean recently, so it now was more reminiscent of a clothing store after a large sale than the usual disaster pit that it had been."
    "Alice nodded and slowly shuffled into my room. She took one look at my room before deciding that the bed was the safest bet, and sat down elegantly."
    MC "Alright, so what's on your mind?"
    show BBW sad
    "Alice's expression immediately soured."
    BBW "Well... It's concerning Kodama-san."
    MC "Kodama-san? Is everything alright? She isn't in some sort of trouble or anything, is she?"
    BBW "Kodama-san in trouble? Nothing so dramatic. She was late with my breakfast this morning, which is quite unusual for her. She is usually so prompt and always seems ready for the day, but today, she looked exhausted and worn-out."
    BBW "I realize that she had another cooking competition yesterday, so she is most likely a bit overtired from that whole affair, however, I must confess that I'm a bit worried about her."
    MC "How do you mean worried?"
    "I sat down on the bed next to Alice and studied her face. Alice always carried herself with such poise and grace, and could seemingly shake off any and all inconvenience. For her to be coming to speak with me privately, let alone her being this upset, must mean that she was truly concerned."
    BBW "She used to offer to help me before I'd even think to ask. And what's more, she always seemed content and happy with her work. But, as of late, her mind seems to be less and less in the moment, like she's in an eternal daydream of sorts."
    BBW "In fact, just the other day, she completely forgot my midday snack. And when I mentioned it to her, it was as if I had just snapped her back to reality for just a moment."
    BBW "I don't want to let her go, Hotsure-san, but I feel as if she isn't happy. And if Kodama-san isn't happy working for me anymore, then why keep her as my assistant? Why force her to continue working for me if it's something she truly doesn't want to do?"
    menu:
        "Tell her to lighten up on Aida.": #PRG +2, BBW +1
            jump PRG020_c1_1
        "Convince her to let Aida go.": #PRG -2, BBW -1
            jump PRG020_c1_2

label PRG020_c1_1:
    $setFlag("PRG020_c1_1")
    MC "So, you said that Kodama-san has been acting distant for a little while, yeah? As in, it didn't just begin this morning?"
    show BBW neutral
    BBW "Precisely. It seemed to begin just over a week ago. I tried to think of what could've possibly triggered such a drastic change, but I came up with nothing."
    MC "Well, I know that she had first begun to train for her competition just a bit over a week ago, then she had her first round shortly thereafter."
    MC "In addition to that, she has her studies and her work with you. Not to mention her growth factor weighing on her shoulders as well."
    BBW "I see. So you believe that she could be tired from dealing with all of these commitments?"
    MC "Not just tired, Alice. I think that she's feeling overworked and stressed out."
    BBW "I beg your pardon?"
    MC "Think about this: How often does she work for you?"
    BBW "Every day mostly, with an occasional day off here and there."
    MC "Alright, and how often does she have classwork?"
    BBW "Every weekday, with additional homework on the weekends, usually."
    MC "Yes. And finally, how often does she put in practice for her competition?"
    BBW "I suppose I've never taken much notice, but I'd have to wager that she practices every day."
    MC "Okay. Final question:  Have you ever seen Kodama-san relax?"
    "Alice's gaze drifted to the floor as she thought hard."
    BBW "Ah... I think she... Well..."
    BBW "When she does relax, it's usually not for much longer than a few minutes, at best."
    MC "Alright, how about this? Try giving her a short amount of time off. Let her rest a bit so she can get herself back in order."
    "For a moment, I thought Alice would go off on me, but to my surprise, she kept her composure."
    BBW "Alright. I'll give her 5 days off. Do you feel that will be sufficient for her to prepare for her next contest, and to rest a bit?"
    MC "I think so. I plan to help her prepare too, so I'll make sure she takes it easy."
    BBW "See to it that she does."
    "Alice stood and made her way to my door, opening it with a creak before turning back to me."
    BBW "Thank you for your insight, Hotsure-san."
    MC "Of course, Alice. Until class then?"
    "Alice nodded and turned down the hall, shutting the door behind her. I finished getting ready for class and found myself sitting back on my bed, my head swimming with what Alice had been talking about."
    jump PRG020_c1_after

label PRG020_c1_2:
    $setFlag("PRG020_c1_2")
    MC "Alice, I hate to say it, but maybe letting Kodama-san go isn't the worst idea."
    show BBW surprised
    "Alice looked at me in stunned silence."
    BBW "I-I'm sorry...?"
    MC "Maybe what's best for her is for you to let her go."
    BBW "But are you certain that letting her go and potentially finding someone else to fulfil her duties is entirely necessary? Maybe just letting her take a few more days off here and there would be better."
    MC "Alice, I'm sorry, but I think that what Kodama-san needs is more time for herself."
    show BBW sad
    "Alice breathed a soft sigh and hung her head, clearly distraught."
    BBW "Perhaps you're right, Hotsure-san. I suppose I'll have to let her go."
    show BBW neutral
    BBW "She will be quite difficult to replace, however."
    MC "I'm sure in due time, you'll find someone to fill the mold that you're looking for."
    BBW "I will. A Nikumaru does not settle for just anyone, you know."
    "Alice stood promptly and opened my door."
    BBW "Even though it wasn't quite what I anticipated coming from you, I'll take your words to heart and make my decision."
    "I nodded politely as she closed the door behind her. Now exasperated, I fell back into my bed and breathed a sigh of relief."
    "Soon, I'd have Aida out from under Alice's iron fist."
    jump PRG020_c1_after

label PRG020_c1_after:
    scene Classroom with fade
    "Morning classes came and went as usual. As Tashi-Sensei droned on at the front of the room, I couldn't help but let my eyes wander to Aida's side of the room. Even if Alice wouldn't have brought it up, I could tell she was exhausted. Her usually bright and cheerful eyes were now clouded and blank, the bags under her eyes making it all the more apparent."
    "Plus, her letting out a yawn every minute or so wasn't helping her case."
    scene Classroom with fade
    #[SCENE CHANGE- CLASSROOM-EVE]
    "By some force which I could only describe as a mix of black magic and sheer willpower, Aida made it through the full day of classes without falling asleep."
    play sound Bell
    "As the bell rang throughout the classroom, Aida gathered her books hastily, and hurried out the door."
    MCT "She seems like she's already in a hurry, best not to overwhelm her."
    "I slung my bag over my shoulder and sauntered off down the hallway. It was Friday, which meant no classes tomorrow. I'd have some free time to practice that new combo I'd been working on lately in Hyper Alley Brawlers IV."
    
    scene Hallway with fade
    stop music
    "Rather than going straight back to the dorm, I took a brief stroll around the school. Daichi was usually at the dorm about now, and I wasn't really in the mood to talk about his latest radical theory."
    
    scene Roof with fade
    #SCENE CHANGE- ROOF_EVE
    play music Sunset
    "Eventually, my stroll took me up to the roof. Since it was a Friday night, and most students had better things to do than wander aimlessly, the roof was deserted."
    "I went to the chain-link fence that surrounded the roof and gazed out over the campus, now bathed in the warmth of the setting sun. Taking a seat on a nearby metal bench, I pulled out the handheld system that I carried with me specifically for times like this."
    "After only a few minutes, I heard the metal door to the roof open with a loud, groaning creak, and slam shut again momentarily."
    if getFlag("PRG020_c1_1"):
        jump PRG020_c2_1
    else:
        jump PRG020_c2_2

label PRG020_c2_1:
    "Of course, curiosity got the best of me and I turned around to see Aida walking towards me, appearing slightly more put together than before, but still looking like she could use a coffee."
    show PRG neutral with dissolve
    PRG "G-Good afternoon, Hotsure-san."
    MC "Good afternoon, Kodama-san. I didn't expect to find you up here."
    PRG "I-I don't come to the roof often. It's just nice because it's usually calm and peaceful."
    MC "It is. It's a good place to come and think."
    show PRG surprised
    PRG "Oh. W-Were you thinking about something? I can leave you alone if you'd prefer some privacy."
    MC "Oh, no. Not at all. I just came up here to relax a bit."
    show PRG unique
    PRG "Oh..."
    "Aida went silent and fidgeted a bit, kicking at a pebble with her shoe."
    MC "Did YOU come up here to think, as well?"
    PRG "I-I suppose."
    MC "Ah. I'll let you be then."
    "I stood and stowed my handheld and was about to head out, when Aida put a hand on my back."
    PRG "Could you... stay here, please?"
    MC "If you'd like. Is anything the matter?"
    PRG "No... not really. I-I just have some things on my mind."
    MC "If you'd prefer to talk to someone about it, I'm here if you need me. My sister tells me I'm a good therapist."
    show PRG neutral
    PRG "T-Thanks, Hotsure-san, but I wouldn't want to be a bother."
    MC "No bother at all! I'm all ears!"
    "Aida thought for a moment before nodding and joining me on the bench, flattening her skirt with her hands as she sat."
    show PRG unique
    PRG "Well... I went to see Alice after classes finished today as I normally do. B-But when I got there, she didn't have any of her usual tasks for me today."
    PRG "I-I was worried that she was going to reprimand me, because I was late with her breakfast this morning, but instead, she gave me some time off. A 'Work Vacation' is what she called it."
    PRG "She told me to take the time to relax, and also brainstorm some ideas for my contest. And maybe once my break is over, I could make the meals I made for the contest for her."
    PRG "But, when I asked her where this idea came from, she told me about her going to see you this morning, and the advice you gave her."
    PRG "I guess... I-I was wondering why you told her what you told her."
    "I ran my hand through my hair and took a breath. Saying I was a bit taken aback was a complete understatement. I wasn't used to Aida being so forward, let alone speaking so much all at once."
    MC "Well... She mentioned to me how tired you've been lately, which is understandable, given how much you've had on your plate lately. But then, I started breaking down how much you actually do on a daily basis, and I realized how little time that leaves you for yourself."
    show PRG neutral
    $setAffection("PRG", 2)
    $setAffection("BBW", 1)
    PRG "T-That's very nice of you, Hotsure-san."
    MC "I hope I didn't overstep my boundaries at all. I just didn't want to watch you run yourself into the ground."
    PRG "You didn't overstep anything."
    MC "Good. I'm glad you'll have some time to just relax now, anything special you plan to do?"
    show PRG happy
    PRG "I-I don't know. Maybe practice for the contest a little. Could you be my taste tester again?"
    MC "I'd be happy to."
    show PRG neutral
    PRG "Good, and thank you, Hotsure-san."
    MC "Oh, it's no problem! Especially for some really tasty free food!"
    PRG "N-No. Not about that. I meant for getting me some time off."
    MC "Oh, that! Duh! You're welcome. I've seen how much you've been doing lately, and that's enough to drive even the strongest people down."
    PRG "I-It's not so bad."
    MC "Not so bad? You should've seen yourself this morning! If someone had slid a pillow onto your desk, you would've been snoring within minutes!"
    PRG "... Yeah, you're right."
    "She started chuckling to herself, putting a delicate hand over her mouth to hide her soft giggles."
    MC "See? You just have to see yourself the way I see you."
    show PRG aroused
    PRG "T-The way y-y-you see me? How exactly do you see me, Hotsure-san?"
    "As those words left her mouth, she inched ever so slightly closer to me."
    MC "Well... I see you as a good friend who needs to try taking naps more!"
    PRG "R-Really? Am I that good of a friend?"
    MC "Of course you are! More than that, I'd call you a very close friend of mine!"
    PRG "Wow..."
    "I let my gaze drift off toward the setting sun, which was slowly fading behind the lush tree line. As I watched the sunset, I failed to notice Aida sliding herself even closer to me, until her wide hips brushed against me."
    MC "You're just such a welcoming person, Kodama-san. Always so pleasant to be around."
    "Her face went bright red, as if it were the first complement she'd ever received."
    PRG "I-I'm not sure if I'd call myself welcoming. I'm not the most social girl."
    MC "You don't have to be a chatterbox to be welcoming. Just a smile or a wave is all you need."
    PRG "H-Hotsure-san?"
    MC "Yeah?"
    PRG "I-I'm glad that... I'm glad that I got to know you."
    MC "And I'm glad that I've gotten to know you too."
    stop music fadeout 1.0
    PRG "I... "
    "Slowly, Aida began to lean herself closer to me. I found myself leaning in closer, as if being pulled in by her. Our faces met in the middle, staying only a scant few inches from one another."
    "Now we were both just sitting there, incredibly close to each other, staring into each other's eyes. It felt like we were standing by an extremely calm, tranquil lake. No movement at all: Just stillness and complete lucidity."
    "Then, the stillness was shattered. I closed the distance and kissed her. Right on the lips."
    play music Sunset fadein 1.0
    "Aida's arms instantly wrapped around me, and mine around her. We embraced tightly as we kissed, Aida leaning even more into me, her huge chest sandwiched between myself and her."
    "I jumped a bit as I felt her tongue brush tentatively against my lips. Taking the hint, I opened my mouth ever so slightly, inviting her in."
    "Our tongues touched and did a sort of dance together, twisting and turning this way and that, kind of like a tongue's interpretation of a flamenco. She began to work her hands through my hair, giving it gentle, little tugs as she went."
    "Although I could've let the moment go on for much longer, eventually, Aida pulled back a bit, breaking apart from me. We both sat there, panting slightly for a moment."
    PRG "W-Wow..."
    MC "What?"
    MCT "Nice going, Captain Obvious."
    PRG "M-My f-first kiss."
    MC "I'm... I'm glad I could be your first."
    "Aida smiled at me sweetly, before looking up and noticing one thing: the sun had now set, and sky was fading from the bright orange of sunset, to the dark blue of dusk."
    show PRG surprised
    PRG "Oh! It's already getting dark?! W-We shouldn't be out past curfew!"
    "She stood up suddenly, haphazardly brushing her skirt flat and adjusting her top hurriedly."
    PRG "W-We should go, Hotsure-san!"
    MC "Oh, okay! Can I see you tomorrow?"
    show PRG neutral
    PRG "I-I'd really like that."
    MC "Well, I'll make it happen then."
    "Aida smiled at me happily, her eyes practically shining in the waning light."
    PRG "T-Thank you, Keisuke-san."
    "She give me a quick peck on the cheek before hurrying towards the stairs, the clicking of her shoes on the concrete steps fading into the distance of the stairwell. I flopped back down onto the bench and breathed a sigh, staring up at the scarce few stars that had appeared in the sky."
    MCT "I shall never forget this bench."
    jump daymenu

label PRG020_c2_2:
    show PRG sad
    "Of course, natural curiosity got the best of me and I turned to see Aida walking towards me, a troubled look plastered onto her face."
    MC "Good afternoon, Kodama-san!"
    PRG "H-Hello, Hotsure-san."
    MC "I didn't expect to see you up here. Do you usually come up to the roof?"
    PRG "N-No. Just when I need a calm place to think."
    "She sat on the bench next to me and gazed off towards the setting sun, her eyes practically glowing in the low sunlight."
    MC "Oh, if you came here to think, I can leave if you'd like. I wouldn't want to intrude."
    PRG "N-No. Can... can I talk to you?"
    "I quickly put away my handheld and gave her my full attention. Whatever it was must've been serious, because Aida just wasn't acting like Aida."
    MC "Of course. What's on your mind?"
    "Aida let her gaze fall to the floor, her stormy gray eyes looked almost lost in themselves, like she was trying to think of how to say something, but couldn't quite put her thoughts together."
    PRG "N-Nikumaru-san told me that m-my services were no longer required."
    MC "Oh, really?"
    "I did my best to act concerned and sincere, despite me already knowing about it."
    MC "Did she give you any reason?"
    PRG "S-S-She told me that I haven't been acting like m-myself. She said that I seem almost... too p-preoccupied with my own thoughts."
    "As I looked on, tears began to stream down Aida's face, falling to the cold concrete below."
    PRG "S-S-She also told me that... that she talked to you this morning... and that you a-advised her to let me go."
    PRG "W-Why Hotsure-san? W-Why would you tell her that?"
    MC "I... I saw how tired you've been lately. You've had so much on your plate lately, and I noticed you never seem to let yourself rest. Then, when Alice told me about how you've seemed distant lately, I thought that maybe if she let you go, you'd have more time to catch up on other things, like the competition."
    $setAffection("PRG", -2)
    $setAffection("BBW", -1)
    PRG "But... I-I LIKED working for Alice, Hotsure-san."
    "I went slack jawed. It had never occurred to me that Aida may actually enjoy her time working with Alice."
    MC "K-Kodama-san. I don't know what to say. I guess I just thought that you needed more time for yourself..."
    "I put my head into my hands and ran my hands through my hair, staring at the floor, enveloped in my own frustration. I had tried to make things easier on Aida and I had totally blown it."
    show PRG neutral
    "I felt a light tap on my shoulder and turned to Aida, who smiled at me weakly, and to my surprise, offered me her hand. I sat there momentarily, staring at it as if it were a sacred treasure, before taking it in my own hand."
    PRG "I-I appreciate you trying to help, H-Hotsure-san. But really, I-I'm fine."
    MC "If you say so. Are you going to try talking to Alice and see if she'll take you back?"
    "Aida looked off in the distance, a wistful haze coming over her."
    PRG "S-She seemed as though her mind was made up. I think I'll take it a little easier, just for now, and maybe ask her later."
    MC "Okay... I-I'm sorry that I intruded on your personal matters."
    PRG "I-It's fine, Hotsure-san."
    "I smiled at her and turned to look back to the sunset, which had now faded past the crest of the tall trees in the distance. As I stared at the rays of light giving way to dusk, I felt something soft against my shoulder and turned my head."
    "Aida was laying her head against my shoulder. After a brief moment of consideration, I released my hand from her grasp and brought it up behind her, putting my arm around her shoulders."
    "Neither of us said a word as we quietly watched the rays of sunlight finally fade away."
    PRG "W-We should probably get back to the dorms. It's getting close to curfew."
    "I blinked myself out of my dream-like haze and rubbed my eyes."
    MC "Y-Yeah. Good idea."
    "Aida stood and offered her hand to me again. I took it eagerly, and she helped pull me to my feet."
    MC "Can I see you soon?"
    PRG "Y-Yes. If you want to."
    MC "Alright, sounds like a plan."
    PRG "O-Okay. Goodnight, Hotsure-san."
    MC "Goodnight, Kodama-san."
    "She gave me a small hug before turning and hurrying down the stairs, her footfalls fading off into the distance. I waited just a moment before following her down the steps and making my way across the courtyard to the dorms."
    "As I made my way through the lush grass of the campus courtyard, I thought deeply about Aida, and the bits of guilt that clung to my conscience."
    jump daymenu

label PRG021:
    $setProgress("PRG", "PRG022")
    scene Classroom with fade
    #SCENE - CLASSROOM DAY
    show AE neutral with dissolve
    play music Schoolday
    AE "And bow!"
    "The class bowed to start the day, as usual. As hard as I tried to stay focused on Tashi-sensei's lesson, my thoughts kept drifting to my latest encounter with Aida."
    hide AE with dissolve
    if getFlag("PRG020_c1_1"):
        "Her kiss had been perfect, despite it being her first. When our lips first touched, she was delicate and unsure, but as the moment continued, she became more steady and firm, pressing into my body more and more. "
    else:
        "From the moment she laid her head on my shoulder, I had been feeling more at ease. Such a simple gesture meant more than most words could, especially from someone who wasn't the most social to begin with."
    "The walk home afterwards had seemed like torture. Although we had said our goodbyes, my mind still lingered on her, and with every step I took, the butterflies that came with the feeling of longing took hold."
    "And when I got back to my-"
    show HR neutral with dissolve #angry
    HR "Hotsure-san!"
    MC "Ehh?!"
    "Tashi-sensei stared at me, his icy gaze seemingly piercing into my soul itself."
    HR "If you have time to day dream, you have time to listen, so eyes front!"
    MC "Y-Yes Sensei."
    "I paid closer attention to Tashi-sensei for the rest of the lesson, save for the occasional glances in Aida's direction. At one point, our eyes met and Aida whipped her head back to the front."
    #SHOW TASHI NEUTRAL
    HR "And at that point, the-"
    play sound Bell
    HR "Bell rang..."
    "Aida hopped up from her desk and gathered her books quickly, rushing out the door before any other student could even rise from their desks."
    
    scene Cafeteria with fade
    "Walking into the cafeteria, I grabbed a tray and worked my way through the line, staring at the back of the person in front of me as my mind drifted off again."
    show BE happy with dissolve
    BE "Kei-chan!!"
    MC "H-Ach!?"
    "My heart nearly pounded through my chest as I swung around to find Honoka standing behind me."
    show BE neutral
    BE "Ahem."
    "She pointed down towards the blunt edge of my tray that I had unknowingly slammed into her left breast."
    MC "Eheh... sorry."
    BE "It's no biggie. I am here as an official secretary for the office of Kodama-san!"
    "She passed me an off-yellow sticky note."
    MC "You, a secretary? That's a sight I'd pay to see."
    show BE happy
    BE "Hell, I'd be a great secretary. As long as I don't have to wear those librarian glasses with the chain on the ends."
    BE "Those are gross."
    MC "Well, keep your vision working the right way, and you won't need those!"
    BE "Easy for you to say! I don't see you sitting at a desk all day, staring down a mound of paperwork!"
    MC "Then hire an assistant to stare at the paper for you."
    show BE angry
    BE "Oh! You know what I mean!"
    MC "So, did Kodama-san say what this was for?"
    show BE neutral
    BE "That's what reading the note is for. Use your eyes, now."
    Note "Meet me in the kitchen after class."
    BE "Sounds like you two lovebirds have a fun day ahead of you. Well, I'll be off then! More papers to deliver, more invoices to shred, never a dull day, in the life of Honoka the secretary, you know!"
    hide BE with dissolve
    "I waved to Honoka as I reached the end of the line."
    "Aida was nowhere to be seen, most likely she was in the kitchen preparing something for our meeting later."

    scene Hallway with fade
    "After slogging through a few more hours of classes, I found myself walking down the hallway toward the kitchen. From time to time, I'd catch the slightest smell of something baking nearby, with a hint of... fruit?"

    scene Cooking Classroom with fade
    #SCENE CHANGE - KITCHEN
    "Walking into the kitchen, I saw no sign of Aida, save for her bag tossed on the nearby table. Scanning around carefully, I finally spotted Aida."
    "She was bent over, reaching deep into the depths of the oven. From this angle, her skirt lay taut against her well rounded hips and impressively thick thighs, riding up just a bit higher than usual."
    MC "K-Kodama-san?"
    show PRG neutral
    "Aida rose from the oven, holding a large pan covered in baking paper."
    PRG "O-Oh! Hello, Hotsure-san! I-I'm sure you got my note?"
    "I held the note up with a grin."
    MC "I came as I was told. You have a very unique secretary running your errands for you!"
    show PRG unique
    PRG "B-But... Inoue-san doesn't work for me..."
    MC "I'm only teasing. So what's the occasion?"
    show PRG neutral
    PRG "I-I'm trying to make a new type of dessert. They're kind of hard to get right, but if I can get them perfect, I can make these again for a competition round."
    MC "Well, I'll help wherever I can. What can I do?"
    "She pointed at the table and smiled."
    PRG "Sit down there. They're all done baking, they just need a bit of time to cool down."
    MC "I see, how long?"
    show PRG unique
    PRG "Maybe... 20 minutes? They usually should be chilled after they're baked though..."
    MC "I've got it! We can put them in the fridge now and go do something while they chill, then come back and enjoy them later!"
    show PRG neutral
    PRG "T-That's a good idea, Hotsure-san, but they're supposed to cool to room temperature first, and then be chilled from there."
    MC "Alright, well then we can wait here for 20 minutes."
    PRG "O-Okay! I'm really excited for you to try these. I-I hope you like them."
    MC "This may come as a shock, but I've loved almost everything you've asked me to taste so far, so I don't doubt that they will be another success!"
    PRG "T-That's very sweet of you, Hotsure-san."
    MC "I could say the same to you. You keep on making me all of this delicious food, and don't ask for anything in return."
    PRG "I do ask for something. Your honest opinion."
    MC "You want my honest opinion? Your food rocks."
    show PRG surprised
    PRG "W-Well... I, uh... T-Thank you, Hotsure-san."
    "After a few more minutes of us going back and forth, Aida went to the counter and reached her hand under the baking sheet."
    show PRG neutral
    PRG "Perfect. Finally room temperature."
    "She took the tray in both hands and guided it into the fridge, being very careful not to bump the edges of the fridge."
    PRG "A-Alright, now we just have to wait. W-What did you want to do?"
    MC "Care to go for a little walk?"
    PRG "Where to?"
    MC "There's a really beautiful path that follows the lake nearby. We could try that?"
    PRG "S-Sounds wonderful. Lead on."

    scene Lake Road with fade
    "I heard Aida let loose a sigh of wonder as we came to a stop at the start of the lake path."
    show PRG surprised with dissolve
    PRG "Wow..."
    MC "Amazing, no?"
    PRG "T-The water is so clear here. It's gorgeous, Hotsure-san!"
    MC "It is. It makes me a little nostalgic just being here."
    show PRG neutral
    PRG "Did you grow up near a lake?"
    MC "Oh no, nothing quite that deep. It's just... this was the path I took when I first came to Seichou. I was so nervous."
    PRG "I was nervous too. I didn't know anyone or even what to expect from a school like this."
    MC "I'm sure we all were a bit nervous coming here. But, all things considered, I'm glad I came here."
    PRG "S-So am I..."
    "As we began to follow the lake path along the coast, the wind picked up, whipping mine  and Kodama-san's hair around as we walked."
    PRG "Can I... tell you something, Hotsure-san?"
    "I glanced over at Aida and studied her face. I couldn't tell whether what was about to come out of her mouth was going to be good or bad, but there was only one way to find out."
    MC "Sure, what's on your mind?"
    show PRG aroused
    PRG "I-I just wanted to thank you... for the other day."
    MC "You... you mean for the Alice thing?"
    PRG "N-No! For the... other thing."
    if getFlag("PRG020_c1_1"):
        "Her face flushed pink as she smiled sweetly. I relaxed a bit as we stopped walking."
        MC "O-Oh! Y-You're welcome. I-I feel like I should be thanking you for that too."
        PRG "No need to thank me. I-It's not like I didn't enjoy it too..."
        MC "It was special, wasn't it?"
        PRG "Y-Yes it was."
    else:
        MC "Well, I-I felt like it fit the mood. I had overstepped my boundaries a bit with everything else that day."
        PRG "Y-You don't have to justify your actions to me, Hotsure-san. I will admit, the extra time off has been nice."
        MC "Then, as long as you're happy, then I'll be happy too."
        PRG "I-I am happy..."
    hide PRG with dissolve
    "We continued walking, listening to the birds and watching the lake lap at the shoreline."
    "Soon, we had turned around and were heading back to the school. We had been walking for nearly an hour, so Aida's dessert should be chilled by now."

    scene Cooking Classroom with fade
    "As soon as we got to the kitchen, Aida went straight to the fridge."
    show PRG neutral with dissolve
    PRG "Sit back at the table, Hotsure-san. And shut your eyes!"
    scene black with fade
    "I did as I was told, and listened as a plate was set in front of me. One by one, I heard multiple hard things being set down on the plate."
    PRG "And finished! You can open your eyes now."
    scene Cooking Classroom with fade
    show PRG neutral with dissolve
    "I opened my eyes and looked down. On the plate was 6 small cookies, each one a different color."
    if getSkill("Art") > 8:
        MC "These are french macarons, right?"
        show PRG surprised
        PRG "Y-Yes! How did you know?!"
        MC "I read about them once. You weren't kidding about the difficulty in making these, though. Macarons are supposed to be a nightmare to make."
        show PRG neutral
        PRG "I-It wasn't too hard. Just really time consuming."
    else:
        MC "What are these?"
        PRG "They're called french macarons. Alice told me about them."
        MC "They look classy. What are they made of?"
        PRG "Mainly sugar, almond flour, and eggs. But each one here has a unique flavor. Try the orange one!"
    "I lifted the orange macaron to my nose and inhaled deeply."
    MC "Oh, God. I've smelled heaven, and it smells amazing."
    "I took a small bite of the macaron and chewed thoughtfully. The flavor was not overwhelming whatsoever, yet it still shone through brightly. The texture was light, and slightly chewy, but not overly soft either."
    PRG "W-What do you think?"
    MC "They're amazing! The texture is perfect and I love the flavor. What do you call the flavor, exactly?"
    PRG "I was going for a blood orange flavor..."
    MC "Well, you nailed that too! This may be one of the best desserts I've ever had!"
    show PRG happy
    PRG "R-Really?!"
    MC "Yes! What other flavors did you make?"
    PRG "T-There's lemon, chocolate, blueberry, strawberry, and red velvet."
    MC "You need to try one of these!"
    show PRG neutral
    "I lifted the blueberry macaron from the plate, and set it in her hand gently. Aida smelled it quickly before popping it into her mouth."
    PRG "..."
    show PRG surprised
    PRG "Oh! Oh my!"
    MC "And? The verdict is?"
    PRG "T-They're unreal!"
    MC "I told you! If you make these for the competition, you'll dominate!"
    show PRG happy
    PRG "I may just have to! I have something planned for the next round already, b-but for the round after, I'll make these."
    PRG "D-Do you think I should make multiple flavors?"
    MC "I'd do chocolate, blood orange, blueberry, and red velvet for sure."
    PRG "Is red velvet really that popular?"
    MC "I'm not sure, but it looks classy, so maybe you can use it to score some bonus points?"
    "Aida and I laughed heartily as we finished most of the macarons, until there were only two left."
    show PRG neutral
    PRG "W-Would you care if I took these last two with me, Hotsure-san? I want to give them to Nikumaru-san so she can try them too."
    MC "Go ahead, they're your creations after all."
    "Aida gently set them inside of a plastic container and covered it."
    PRG "Thank you, Hotsure-san. And thanks again for being my taste tester."
    MC "As I've said before, it's no problem!"
    PRG "D-Don't you ever get sick of trying my food all of the time?"
    MC "Kodama-san, I'm a guy. We never turn down free food, especially if this free food happens to be five star meal quality."
    show PRG unique
    PRG "M-My food isn't quite at that caliber..."
    MC "Well it's pretty damn close!"
    show PRG neutral
    PRG "Eheh... I'd better get these to Nikumaru-san. I don't want them to get too warm."
    MC "Alright. I'll catch you in class tomorrow then?"
    PRG "Y-Yeah. Have a good rest of your day, Hotsure-san."
    MC "Same to you!"
    "Even as I said my goodbyes and left the kitchen, I still had the lingering flavor of blood orange in my mouth."
    jump daymenu

label PRG022:
    $setProgress("PRG", "PRG023")
    scene Classroom with fade
    show HR neutral with dissolve
    play music Rain
    HR "-and that's why you never mix Bleach and Vinegar."
    hide HR with dissolve
    "I leaned back in my chair and sighed. Classes had been getting more and more boring lately. Tashi-Sensei was a knowledgeable man, no question about that. However, watching paint dry on a house was more interesting than listening to his lectures. Just then, the reassuring *DING* of the bell sounded throughout the school, signaling the end of classes for the day."
    "As everyone began gathering their books, I couldn't help but smile to myself. It was Friday, meaning that I had two days of freedom. I could sense a nap and some video games in my future."
    "A light tap on my shoulder snapped my out of my daydream, making me jump."
    MC "Oy?!"
    "I spun around and glanced down to see a very shaken Aida standing behind me."
    show PRG surprised with dissolve
    PRG "I-I didn't mean to startle you, Hotsure-san! Please forgive me!"
    "Aida bowed politely before me, clearly trying to hide her slowly reddening face."
    MC "It's fine, Kodama-san. What's up?"
    "Aida looked up at me again, brushing her hair out of her face sheepishly."
    show PRG unique
    PRG "I-I was just wondering. With the next round of the competition coming up, I have a handful of recipes I'd like to try. I...I was wondering if you would be my taste tester once more?"
    "A loud growl filled the air between us. I put an arm over my growling stomach, making Aida giggle."
    MC "How could I ever say no to an offer like that?"
    "Aida smiled at me sweetly, looking at me expectantly."
    show PRG happy
    PRG "Yay! Also...would you like to go grocery shopping with me? I need some supplies to make these recipes perfect."
    MC "Sounds great! I've been meaning to check out the grocery store anyway."
    PRG "Great! Let's leave our books at our rooms and meet by the school's entrance."
    MC "Alright! I'll be there before you know it!"
    "Aida smiled at me and waved as she hurried out of the room."
    hide PRG with dissolve
    MCT "This will be so awesome. Getting to hang out with Aida AND have some amazing food, it's a win-win!"

    scene School Front with fade
    "A light breeze blew across the school grounds as I passed by the main buildings of Seichou Academy, nearing the entrance. As I got closer, I spotted Aida seated on a nearby bench, scribbling on a piece of paper with a pencil. I quickly closed the distance between us, slowing to a stop beside her."
    show PRG neutral with dissolve
    PRG "H-hey Hotsure-san. Ready to go?"
    MC "I'm ready when you are!"
    PRG "Good, let's get going then. The supermarket isn't far from here so we can walk it."
    MC "Alright. Lead the way then."
    hide PRG with dissolve
    "We passed through the school's gates and turned left, heading south, towards the supermarket."

    scene Town with fade
    play music Sunset
    show PRG neutral with dissolve
    PRG "I wrote down a few recipes here along with the items I'll need to make them. Pick three of them, and we'll get the items we need to make those."
    "She passed me the wrinkled piece of paper so I could read it."
    MC "Hmm, let's do teriyaki chicken wings, the pork ramen, and some strawberry mochi. I think those will be a hit at the competition."
    "Aida looked surprised for a moment."
    show PRG surprised
    PRG "R-really? You like pork ramen too?"
    "I nodded, handing her the list."
    show PRG unique
    PRG "I used to make it all the time, my mother taught me. But with how popular ramen is, I always thought that everyone at the school would be sick of it, so I haven't made it since I came here."
    "Aida stopped walking for a moment."
    show PRG sad
    PRG "Do you think the judges will think my ramen is too...ordinary?"
    MC "The way I see it, pretty much everyone has tasted ramen before, right?"
    "Aida nodded, looking at me intently."
    MC "Well, since everyone thinks that ramen is almost the same every time, all you have to do is make a ramen that's better than any other ramen they've ever tried!"
    MCT "Thanks for the idea, Alice."
    "Aida looked away."
    PRG "But do you think I can really do that? I don't know if I'm that good of a chef..."
    MC "That's why I'm here! My family used to have ramen all the time too, plus I've tasted both good and bad ramen. You can make a few different batches, with subtle variations to each one. Then, I'll taste them, and we can determine which one will be the best one to present at the competition!"
    "Aida began to blush, as she had a tendency to do."
    show PRG aroused
    PRG "Would you really do that for me?"
    MC "As the official taste tester, I insist!"
    "Aida's face lit up like I'd never seen before."
    show PRG happy
    PRG "Thank you Hotsure-san! Thank you so much!"
    MC "Of course! I'm your friend! It's what friends do for each other. Now, let's get going before it gets too late."
    show PRG surprised
    PRG "O-Oh! Yes, let's go!"
    "Aida led the rest of the way until we arrived at the supermarket."

    scene Supermarket with fade
    "The two of us entered the store, grabbed a cart, and made our way deeper into the store."
    MC "What kind of spices will we need for everything?"
    show PRG neutral with dissolve
    PRG "I-I think the cooking club should have everything we need as far as spices go. Let's start with vegetables, then go for oils, and finally, meat at the end. The meat will stay cooler if we grab it last. If it's frozen, it should thaw a bit by the time we get back to the school."
    MC "Ah, good point."
    hide PRG with dissolve
    "It still amazed me sometimes how much Aida knew about cooking. I knew how to cook the basics, of course, but she was a force of nature in the kitchen."
    "Coming upon the produce department, we split up, grabbing everything from mushrooms to leeks, and enough garlic to make Dracula scream."
    show PRG neutral with dissolve
    MC "That all of the veggies?"
    PRG "I think so. I'm going to go get the oils. Could you go find the ramen noodles? Get a few bags if they have them."
    MC "On it!"
    hide PRG with dissolve
    "Ducking down the noodle aisle, I spotted the ramen right away. I loaded myself with 4 big bags and hobbled back down the aisle, turning right towards where Aida had gone."
    PRG "I see you found the ramen."
    "I peeked around my stack of noodles to see Aida standing in front of me, pushing the cart up so I could unload."
    show PRG neutral with dissolve
    MC "Heh, yeah I did. How was the hunt for oil?"
    PRG "Um...Oily?"
    "Aida gestured down at a handful of bottles littering the bottom of the cart."
    PRG "I grabbed some sesame oil and soy sauce for the ramen. I think they'll add some flavor. Also, how do you feel about spicy food?"
    MC "Eh, I'm okay with it. I mean, I'm not gonna go out and eat ghost peppers for kicks or anything, but I can handle my spice fairly well."
    PRG "Good. I found some chili powder which could be good sprinkled on top."
    MC "Awesome, can't wait! So, onto meat then?"
    "Aida nodded and pointed down by the cash registers, where the giant meat freezers stood."
    MC "Oh, good. We can get the meat and then check out right away."
    hide PRG with dissolve
    "I led the way to the freezers. I had to admit, it was fun going shopping with Aida. Even if it was just going out and buying groceries, it still had a special feeling to it."
    "Once we pulled up to the freezers, we loaded up the cart with chicken and pork, plus a carton of eggs for good measure."
    show PRG neutral with dissolve
    PRG "All done! Let's head to the registers."
    MC "Yeah, good idea. All of this food is making me hungry."
    show PRG happy
    PRG "I-I'm pretty sure you're always hungry."
    MC "Eh, it's a guy thing, comes with the title."
    PRG "Well, I can't argue. Good food is one of life's biggest gifts."
    MC "That's seriously deep."
    PRG "What can I say? I'm a poet and chef."
    "We both laughed as we started loading our food onto the conveyor belt for the tired looking cashier to scan."
    show PRG unique
    PRG "This... This is gonna be a pretty crazy bill..."
    menu:
        "Offer to help pay":
            jump PRG022_c1_1
        "Do nothing":
            jump PRG022_c1_2
        "Pull out wallet":
            jump PRG022_c1_3

label PRG022_c1_1:
    MC "We can split it, if you'd like."
    show PRG surprised
    PRG "No! No, no. I invited you along, I'll pay."
    MC "I'm going to be eating quite a bit of this, I should at least help."
    Cashier "That'll be 13061 yen, please."
    "Aida pulled out her wallet, which had the dragon's logo on it, and slid her credit card onto the counter."
    MC "Put half on that card, and half on this one, please."
    "I slid my own card next to Aida's."
    show PRG unique
    PRG "No...Hotsure-san..."
    MC "Shhh."
    "The cashier punched some numbers into the register and swiped our cards."
    Cashier "You two are all set, have a good rest of your day!"
    PRG "You too."
    hide PRG with dissolve
    "We bagged our groceries. Thankfully, the store has having an event that day and was giving away free tote shopping bags, so rather than risking having a plastic bag tear open, we took full advantage of the tote bags. And since the bags were fairly large, we managed to fit all of our groceries into two bags, each of us taking one to help balance out the load."

    scene Hill Road with fade
    "By the time we left the store, the sun was beginning to set, bathing the trees and buildings with a warm, orange hue."
    show PRG sad with dissolve
    PRG "You didn't have to do that."
    MC "Do what?"
    PRG "You know... help me pay."
    MC "It was only fair, you're already going to be cooking for me. It's the least I could do. Plus, you've baked and cooked for me so much in the past, I felt like I had to repay you somehow."
    "Aida was silent for a short while. As we walked, I looked over and saw she was smiling."
    $setAffection("PRG", 1)
    show PRG neutral
    PRG "It's fun for me too. I love cooking for others and seeing the smiles on their faces. It's nice to feel wanted, you know?"
    MC "Yeah, I understand."
    jump PRG022_c1_after

label PRG022_c1_2:
    MC "Yeah, I didn't even think about that until now."
    Cashier "That'll be 13061 yen, please."
    MCT "Ouch."
    "Aida sighed and slid her credit card across the counter. The cashier took it and swiped it, punched some numbers into her computer, and handed Aida's card back to her."
    Cashier "You're all set hun, have a good one!"
    PRG "Oh, thank you! You too!"
    hide PRG with dissolve
    "We bagged our groceries. Thankfully, the store has having an event that day and was giving away free tote shopping bags, so rather than risking having a plastic bag tear open, we took full advantage of the tote bags. And since the bags were fairly large, we managed to fit all of our groceries into two bags, each of us taking one to help balance out the load."
    
    scene Hill Road with fade
    "We began walking back to the school. I was feeling guilty about Aida having to cover the entire bill herself."
    show PRG sad with dissolve
    MC "Hey... Sorry I didn't help you pay."
    PRG "Oh... It's no trouble, Hotsure-san. It's all for my competition, anyway."
    MC "Yeah, but still. I'll give you some yen when we get back."
    $setAffection("PRG", -1)
    PRG "No. It's fine. Just helping me put all of this away will be enough."
    MC "O-okay."
    jump PRG022_c1_after

label PRG022_c1_3:
    $setFlag("PRG022_c1_3")
    "I pulled out my wallet and slid my credit card to the cashier."
    MC "Put it all on this, please."
    show PRG surprised
    PRG "B-b-but! Hotsure-san!"
    Cashier "That'll be 13061 yen, please."
    "The cashier grabbed my card and swiped it, passing it back to me, along with my receipt."
    Cashier "You're all set! You two have a great rest of your day!"
    MC "You too!"
    hide PRG with dissolve
    "We bagged our groceries. Thankfully, the store has having an event that day and was giving away free tote shopping bags, so rather than risking having a plastic bag tear open, we took full advantage of the tote bags. And since the bags were fairly large, we managed to fit all of our groceries into two bags, each of us taking one to help balance out the load."

    scene Hill Road with fade
    "By the time we left the store, the sun was setting, giving the buildings and trees and rich, deep red color."
    show PRG unique with dissolve
    PRG "Hotsure-san, you didn't have to do that."
    MC "What?"
    show PRG angry
    PRG "You know what!"
    if getAffection("PRG") > 6:
        MC "It's habit, I guess."
        show PRG neutral
        PRG "What do you mean?"
        MC "From little on, my dad always taught me that, when I'm out with a girl, I should always pay."
        PRG "R-really?"
        MC "Yep. Plus, I couldn't just let you pay for that whole bill yourself. I'm going to be eating a good portion of it, so I should help pay."
        show PRG surprised
        PRG "But, helping to pay and covering the entire bill are two totally different things, Hotsure-san!"
        MC "Well, like my dad always would say: 'It's proper date etiquette.'"
        "Next to me, Aida's face turned bright red."
    else:
        MC "My dad always told me that paying a bill was the polite thing to do. I guess it's just habit now."
        show PRG neutral
        PRG "But still, thank you all the same."
    $setAffection("PRG", 2)
    jump PRG022_c1_after

label PRG022_c1_after:
    hide PRG with dissolve
    "The two of us walked all the way back to school, talking about the recipes and the competition. It was funny, the longer I was around Aida, the more she opened up to me. She never would give a lot away at one time, but every so often, I'd get little glimpses."
    "It was kinda cute, honestly."

    scene Cooking Classroom with fade
    "The two of us entered the cooking classroom and set our bags down on the counter. Right away, Aida got to work putting everything away. I would help where I could, but I still had no idea where everything went, so all I could really do was hand her things."
    show PRG neutral with dissolve
    PRG "Thanks again for coming today, Hotsure-san. Shopping is a lot more fun with someone else."
    MC "Thank you for inviting me! I never thought going grocery shopping could be that much fun."
    PRG "You and me both."
    "In no time at all, we had finished putting everything away. By now, it was dark out, and we had about half an hour until curfew."
    MC "Well, I'd better head back to the dorms. It's getting late."
    PRG "Yeah, you're right. When would you to do our taste test?"
    MC "Whenever you'd like. I have a fairly open schedule."
    PRG "A-Alright, I'll let you know."
    if getFlag("PRG022_c1_3") and getAffection("PRG") > 8:
        "Aida looked down at the floor for a moment, before letting her gaze meet my eyes again."
        show PRG aroused
        PRG "So... how do people usually end a date?"
        MCT "Oh, the things I could say."
        MC "Well, there are a number of ways, but let's start off with the most simple way first."
        PRG "Okay...What's that?"
        MC "This."
        "I opened my arms wide and pulled Aida into a hug. As she got closer, I felt her arms wrap around my abdomen. We both squeezed a bit tighter, and as we did so, I felt her soft breasts press up against me, being squeezed between the two of us. Aida turned her head sideways to lay her head against my chest, turning the hug into an all-out embrace. We stayed that way for a little while until we heard the low bell that signaled that we were getting close to curfew."
        MC "We'd better get going. Don't wanna get in trouble."
        PRG "Oh... of course."
        MCT "I don't really want to leave, though."
    PRG "Thanks again for coming with me. I'll see you in class then?"
    MC "For sure. And who knows? Maybe we'll bump into each other before then."
    PRG "Quite possibly. Goodnight, Hotsure-san!"
    MC "Goodnight, Kodama-san. Sleep well!"
    hide PRG with dissolve
    "I left the classroom and walked all the way back to the dorms. But, the entire time I walked, I couldn't get my mind off of Aida. I was thankful that she was beginning to open up a bit to me, because I had a feeling she wouldn't open up to just anyone."
    jump daymenu

label PRG023:
    $setProgress("PRG", "PRG024")
    scene Classroom with fade
    #SCENE: CLASSROOM DAY
    play music Busy
    "As per usual, I didn't pay much attention in class, choosing instead to stare at the wall in front of me. Tashi-sensei was engrossed in his typical long running lectures, and didn't seem to care whether the class paid any notice."
    show HR neutral with dissolve
    HR "And to wrap up today, I'm assigning you guys a 15 page research paper, due in one month exactly. You may choose a partner to work with you, if you wish. However, both of you will be sharing a grade, so make sure you aren't slacking. "
    MCT "W-Wait... what are we researching?!"
    "Turns out, I wouldn't be waiting long to find out."
    
    scene Hallway with fade
    "The minute I stepped into the hallway, I noticed the telltale bounce of Aida as she came to stand in front of me."
    show PRG happy with dissolve
    PRG "Good morning, Hotsure-san!"
    MC "Hello, Kodama-san. What brings you here today?"
    show PRG unique
    "Aida looked more than a little confused."
    PRG "Um... I go to school here, Hotsure-san. Same as you."
    MC "Heh. Only kidding, what's up?"
    show PRG neutral
    PRG "I-I was curious if you wanted to partner up for that paper? I-I've never been much good when it comes to brainstorming ideas, so I figured, maybe two heads are better than one?"
    MC "Well, thanks for thinking so highly of my creativity. I'd love to be your partner, but I do have one question first."
    PRG "Y-Yes... ?"
    MC "What exactly are we supposed to be researching?"
    show PRG surprised
    "Aida had a look on her face that was half pity and half confusion."
    PRG "D... Did you not hear Tashi-sensei? It can be on anything we'd like, as long as it reaches 15 pages."
    MC "Oh! That'll be easy then!"
    PRG "I-It will?"
    MC "Yeah, we can research anything we'd like! It'll be a cinch to come up with something!"
    scene Library with fade
    "It most definitely was not a cinch."
    show PRG unique with dissolve
    MC "Ahhh... Maybe we could research plants?"
    PRG "I think Yamazaki-san is already doing that. It'd probably be best not to be redundant."
    MC "You've a point there. Maybe... the history of Japan?"
    PRG "T-That may be a little too broad. Let's try to come up with something more defined."
    MC "Alright..."
    "We both sat for a moment before Aida jumped up from her chair, excitedly knocking it over."
    show PRG happy
    PRG "I've got it! We can do a 15 page paper on the history of the Dragon's baseball team!"
    if getFlag("PRG011_b"):
        MC "Yes! That's an awesome idea, Kodama-san!"
        show PRG neutral
        PRG "T-Thanks. Since we're both fans, this should be both an easy and fun topic."
        MC "And a perfect topic. So how should we get started?"
        show PRG surprised
        PRG "Y-You want me to make the plan?"
        MC "Go ahead! It was your idea, and I trust your knowledge base on them way more than mine."
        show PRG neutral
        PRG "Alright! First... we should construct an outline to follow, then start compiling the facts that we already know together. We can check the facts online to make sure they're true afterwards."
        MC "Then we can start the actual researching of new information from there. Since we have a month to work at this, we don't have to rush, but we shouldn't slack either."
        PRG "Y-Yeah..."
    else:
        MC "Uhm... Alright. That could work."
        show PRG sad
        PRG "I-I know you aren't the biggest fan of the dragons, but since I've been following them for years, I think I know their history really well, so maybe I can help guide us through the research."
        MC "Sure. All the same though, we should fact check our work to make sure we're on the mark with everything."
        PRG "Y-Yes... Good idea."
        MC "N-Not saying that your information isn't accurate!"
        show PRG neutral
        PRG "I didn't take it that way. Don't worry."
    MC "So, when would you like to start?"
    PRG "Right now works for me."
    MC "Oh! Uh- sure! That's fine!"
    show PRG surprised
    PRG "U-Unless you have plans! We don't have to start now! I-I shouldn't have assumed you had the time right now! I-I'm sorry!"
    MC "Woah, it's alright. Just take a deep breath. I just wasn't quite expecting such a quick turnaround time. I don't have any plans today, so yeah, let's get going now!"
    show PRG neutral
    PRG "O-Okay!"
    "Aida leaned over and reached into her backpack, withdrawing a thick notebook from it's depths."
    PRG "We can use this to pool all of our ideas together."
    show PRG surprised
    PRG "Oh! I just remembered I have a book that my grandparents got for me about the Dragons in my dorm!"
    MC "That would be awesome to use! And since it's an officially printed book, it'll have some of the most accurate information available."
    show PRG neutral
    PRG "Right. I'll go get it quick."
    hide PRG with dissolve
    "Aida got up and dashed out of the room, leaving me in the library."
    "I grabbed her notebook and a pencil, and rifled through the pages, searching for a clean sheet. The notebook had seen its fair share of use, and was in danger of losing some of its pages. Something with bold, dark colors caught my eye and I stopped mid page turn."
    "On the page was a drawing of two people, a man and a woman by the looks of it, and they were... kissing? Their arms were wrapped around each other in a romance novel style hug, and the man had the woman leaned back slightly into his arms."
    "Scanning over the drawing, my eyes landed on a surprisingly detailed crest emblazoned on the woman's shirt. Something about it struck me as familiar. Quickly dismissing the thought, I turned my focus back to the rest of the drawing."
    "The woman was shorter than the man, at least by a handful of inches, and she had absolutely enormous breasts. Looking over the rest of her showed that she was a shapely woman everywhere else as well, with thick thighs and a generously proportioned rear end. "
    "Turning my focus to the man, he looked oddly simple, with formal pants and a white button down dress shirt. What struck me as odd was his long, flowing hair, which stopped mid-back, and he had the same crest featured on his shirt as the woman did... wait."
    "I looked down at my shirt and stared. There was the crest: the Seichou Academy crest. "
    "Reaching behind me, I felt for my hair. While not quite to my mid back, it was surely on its way. Even my dress pants matched the image almost to a tee. "
    "Looking over to the girl again revealed little more than what I had previously noticed, until I glanced at her hair and noticed a rather miniscule detail. Tiny purple beads were in her hair, forming the ends into two distinct ponytails, which hung over the shoulder. "
    "My heart began to race as the pieces suddenly fit together. This was supposed to be Aida and I kissing. "
    "The sound of rapid footsteps from the hallway snapped me back as I began shuffling through the notebook again, until I reached a blank page and quickly scribbled a heading and date on the top. "
    show PRG neutral with dissolve
    "Aida appeared in the door, a heavy looking book tucked under her arm. She looked out of breath, her cheeks reddened from the effort. "
    PRG "G-G-Got it! This... should tell us everything we need to know."
    MC "You didn't have to run back! Like I said, we have all day to work! "
    PRG "I-I-I know... I just... wanted to make the most of our time. "
    "As Aida sat back down across from me, I glanced up at her hair, and my heart rate picked up once again. The purple beads were present, as they always were. "
    MC "So, where's the best place to begin? The beginning of their career, I assume?"
    PRG "Yeah, we can use any facts we have memorized already, but let's start off by using the book first, and if we think of anything else down the line, we can add onto that later. "
    if getFlag("PRG011_b"):
        MC "Alright. I know the Dragons became an established team in 1948, right?"
        PRG "1946, actually. They competed in their first league in 1948."
        MC "Ah, should've known that."
        PRG "I-It's a common mistake. Not a lot of people remember that. A lot of people throw out so many random dates for when they actually became a team, that it's become a little hard to remember when they actually started. But I know for a fact that it's 1946."
        "She grabbed her book and opened it to one of the first pages, which showed a small timeline. All the way at the start of the timeline was the year 1946, with “The Beginning” written underneath it."
        MC "That's... to the point."
        "We spent the remainder of our time in the library bouncing facts off of one another. Even though I was no slouch when it came to the Dragons, Aida was on a completely different level of expertise. Every question I asked her was answered without so much of a second thought."
    else:
        "We flipped through the book to the first section, titled “The Early Years.”"
        MC "Let's see... they started in 1946 according to this."
        PRG "I had that written already, I-I knew that."
        MC "Wow, guess I underestimated how much you actually know about the Dragons."
        show PRG angry
        PRG "I only remembered one thing so far!"
        MC "Well, I'll keep throwing out facts from the book, and we'll see how well you keep up!"
        show PRG happy
        PRG "Y-You might be surprised!"
        "As the day wore on, the two of us referenced the book and wrote thorough notes. For every fact I'd take from the book, Aida would have two more waiting from her memory. In just over an hour, we had four pages of notes written, and we hadn't even finished the early years section of the book."
    MC "Care to call it a day? I think we have a good foundation here to go off of."
    show PRG neutral
    PRG "Yes. I think this should do for now."
    "We both got up and grabbed our bags. Aida stowed her notebook before slinging her bag over her shoulder."

    scene Hallway with fade
    show PRG neutral with dissolve
    MC "I was going to ask, who got you into baseball? A friend or something?"
    PRG "My dad did. He was really into it when I was younger."
    MC "That's cool. It must've been nice to share something that special with him."
    show PRG aroused
    PRG "I-It was. He taught me how to play catch and how to bat correctly. He even took me to a game once."
    MC "That must've been amazing. I know their games have a reputation for being a little crazy."
    PRG "Not in a bad way. It's more of an exciting type of crazy. It was a little much for me as a little kid, though."
    MC "I'm sure it can be a lot for anyone not accustomed to it."
    
    scene black with fade
    "The two of us walked out of the classroom buildings and toward the dorms, chatting about baseball and the Dragons all the way. As we went, my mind drifted from baseball, and went back to that drawing I had seen in Aida's notebook."
    "Even if it had just been a drawing, I couldn't help but tease the thought in my mind. I mean, sure, we'd already kissed once, but would there be more someday?"
    jump daymenu
    
label PRG024:
    $setProgress("PRG", "PRG025")
    scene black with fade
    RM "Dude! Wake up!"
    scene Dorm Interior with fade
    play music Busy
    show RM angry with dissolve
    "I blinked awake to Daichi's face looming over my bed. He had this piercing gaze that reminded me of laser beams being directed straight at me, and he had the lasers at full power today."
    MC "Argh... what?!"
    RM "It's official, no classes today."
    MC "Wha... ?"
    show RM neutral
    RM "There's some sort of faculty inservice today, a sort of meeting of the minds for the teachers and staff. In short, we have the day off."
    MC "That's nice."
    MC "Tell me one thing:  Why, if we have the entire day off, couldn't you have just let me sleep in? Leave a note or something."
    show RM smug
    RM "And waste the precious early morning hours of the day? Pah, I'll have none of that, thank you!"
    hide RM with dissolve
    "I shut my eyes to yawn, and by the time I opened them again, Diachi was gone, the nearby curtain flapping in the breeze from the open window he had no doubt jumped from."
    "Once I had shuffled to the window and reached groggily for the latch, I heard the tiniest rustling sound coming from the bushes across the path, next to the girl's dorm."
    "As I looked on, Aida slid silently out from behind them, and glanced around to make sure she was alone. Held tightly against her chest was a wrinkled and creased piece of paper, which despite its condition looked important. She began to hurry down the nearby path towards the classrooms."
    MCT "... what the?"
    "I could have called out to her, but by the way she was acting, I didn't want her to think I had been spying on her. The way I saw it, I only had one option."
    "Without hesitation, I put my hands on the windowsill and hoisted myself onto the ledge."
    MCT "Shit! Shit! Shit! Okay, relax. Daichi does this all the time."
    "I gulped as I looked down. Our room was on the second floor of the building, giving me a considerable drop to the ground below."
    "I turned to put my hands on the windowsill once more to climb down the side of the building... "
    "... That is until the leg of my pajama bottoms snagged in a small crack and I fell backwards out the window."
    stop music
    scene black
    #(SCREEN SHAKE)
    #(CRASH SFX)
    MCT "..."
    "Thank mother nature and her affinity for bushes."
    MC "Urgh... auh..."
    scene Dorm Exterior with fade
    play music Schoolday
    "I opened my eyes and gasped for air. I blinked as I started seeing stars. Soon, I heard footsteps and what looked like two Aidas came running towards my crash site."
    show PRG surprised with dissolve
    PRG "H-H-HOTSURE-SAN!"
    "She ran and slid in the grass next to me, her eyes wide as two saucepans."
    PRG "A-Are you okay?! What happened?!"
    MCT "I was curious about what you were up to this early, and rather than being sensible and asking you later, decided to pull an olympic swan dive out the window."
    MC "I... fell."
    PRG "Doing what?"
    MCT "Think man, think!"
    MC "I... uh... I couldn't sleep last night and had the window open to get some air. When I woke up this morning, I still felt groggy. And then when I walked over to shut the window, I tripped and fell."
    show PRG sad
    PRG "O-Oh my... Are you feeling okay? Did you hit your head at all? Does it hurt? Does... does anything hurt?"
    MC "I'm fine... I think. I just feel a little winded, I guess."
    "With a heave, I began to pull myself to my feet, before Aida put her hand lightly on my shoulder."
    show PRG neutral
    PRG "I-I'll help."
    "Aida wrapped her arm around my back and tucked her hand under my arm, lifting with me. I got shakily to my feet before collapsing down on one knee."
    MC "M-My ankle..."
    show PRG sad
    PRG "You must've twisted it when you landed."
    "Aida set her paper down on the grass and put a rock on it to serve as a makeshift paper weight."
    PRG "I-I'm gonna help you get up again, but keep your bad ankle raised."
    "I nodded as she tightly gripped me tightly once more and hoisted me to my feet. Following her orders, I kept my ankle raised."
    MC "K-Kodama-sa-!"
    "I began flailing my arms as I lost my balance. I closed my eyes and braced myself as I slammed..."
    "... Right into Aida."
    show PRG angry
    PRG "I-I've got you!"
    "She'd ducked underneath my arm and had caught me in such a way that I was now using her entire body as a crutch."
    PRG "I-I'm taking you to the infirmary. You need to get that ankle looked at."
    menu:
        "Thanks, but I'll be fine.": #+2
            jump PRG024_c1_1
        "Are you sure?": #-3
            jump PRG024_c1_2

label PRG024_c1_1:
    MC "Kodama-san, I appreciate the help, but really, I'm fine. I'll just go lay in bed and rest my ankle for the day, and I'll be fit as a fiddle by tomorrow."
    show PRG sad
    PRG "I-I really think you should get it looked at..."
    "I glanced down at my wounded appendage. The swelling had taken hold already, and since I hadn't had shoes on, nothing was there to stop the swelling."
    MC "...All right, you lead."
    $setAffection("PRG", 2)
    PRG "Right."
    jump PRG024_c1_after

label PRG024_c1_2:
    MC "Are you sure that's really necessary? I mean, it's just a twisted ankle. People twist their ankles all the time and I'm sure very few of them schedule a doctor's visit for it."
    show PRG sad
    $setAffection("PRG", -3)
    PRG "I... I'm just trying to help you..."
    "Aida's eyes began to well up with tears as she retrieved her paper and turned to leave, leaving me leaning against a nearby tree trunk."
    MCT "Good going man. Bite her head off, why don't you?"
    MC "Kodama-san... I'm sorry. I didn't mean to sound ungrateful."
    "Aida turned around, but still kept her distance."
    PRG "It's all right."
    "She walked back over to me and took hold of me once more."
    MCT "That was... surprisingly easy."
    PRG "S-So... infirmary, then?"
    MC "Please."
    jump PRG024_c1_after

label PRG024_c1_after:
    hide PRG with dissolve
    "As crazy as it was, Aida stayed exactly where she was all the way to the infirmary. By the time we got there, she looked exhausted in every sense of the word, but also pleased with herself."

    scene Nurse Office with fade
    "Soon I was seated on the paper-covered examination table. Instead of catching her breath in the chairs across from me, Aida stood next to the table as if to console me."
    show PRG neutral with dissolve
    MC "I have to say..."
    PRG "Hmm?"
    MC "You are way stronger than what I would've ever imagined."
    show PRG unique
    PRG "I-It's nothing. I'm nowhere near Mizutani-san's level..."
    MC "But still, that was pretty crazy. I mean, you didn't stop the entire way across the courtyard."
    PRG "I-I saw that you needed help... Not like you would've gotten very far on your own..."
    "The nurse walked into the room, holding a large brown clipboard. She looked tired, yet alert, with her long secretary nails tapping nonchalantly on the clipboard."
    Nurse "Let's see... Hotsure-san, right?"
    MC "Yep."
    Nurse "My, quite a doozy of an ankle you've got there. Let's have a quick look."
    "She gently examined the skin of my ankle, gently poking here and there."
    Nurse "Well, no breaks in the skin, so that's good, but I'd like to check to see if there's any internal damage. I'm going to test your range of motion, so this might sting a little."
    "I nodded as she placed both hands on my foot, one on the front near the ball of my foot, and one on the back, supporting my heel. She carefully, yet firmly moved the ankle forward, then back. I winced as she rolled my ankle to the left and right sides, before letting it hang naturally."
    Nurse "Seems like just a simple twisted ankle. It's nothing serious, but you'd best take today and rest. Thankfully, you guys have the day off, so you can afford taking a day to relax."
    "She left the room momentarily and came back with a large steel crutch held in her hands."
    Nurse "You can borrow this for the time being. That way, you don't need to use your friend here as a support."
    MC "Thank you very much."
    Nurse "My pleasure. Now then, for your file, I'll need to notate how the injury occurred."
    MC "Oh, I fell out of my dorm room window."
    "The nurse looked at me, her eyes wide and her mouth slack jawed."
    MCT "It does sound a little far fetched out loud."
    Nurse "A... uh... Are you telling me the truth? Seriously?"
    PRG "Um... I was there Ma'am. It's true."
    Nurse "I... wow. I've been here for over 10 years and this is my first case of injury by window."
    "She jotted down something into her notes quickly, before looking to Aida."
    Nurse "And you were with him when the injury occurred?"
    PRG "Um... Not exactly. I was walking on the path between the two dorms and I happened to glance at the boy's dorm and saw Hotsure-san fall."
    Nurse "I see, and your name, miss?"
    PRG "Kodama Aida."
    Nurse "Wait... Kodama Aida? Didn't you have an appointment set up with us for later today?"
    PRG "I-I did, but could you cancel that? I-I'd better help get Hotsure-san back to his dorm."
    Nurse "Suit yourself. Just let us know if you'd like to reschedule, okay?"
    PRG "I-I will."
    Nurse "Alright. Now, as far as this ankle goes, I'd be icing this as much as possible. You're going to want that swelling gone ASAP. Try to avoid using it too much today, maybe limit yourself to 15 minutes on your feet at one time. The last thing you want to do is stress the injury."
    Nurse "If you treat this ankle right today, I can guarantee you that you'll feel completely better by tomorrow!"
    "I nodded at her as she stood and led Aida and I out of the room into the lobby. On the way, she ducked into a side room and brought forth an ice pack."
    Nurse "In case you don't have one already."
    "She lead us to the front desk where we filled out some quick paperwork before leaving."
    Nurse "Take care, you two! Enjoy your day off!"
    "I bowed to her as best I could with only one foot and hobbled my way out the door, with Aida holding it open for me."

    scene Campus Center with fade
    play music Sunset
    #[SCENE CHANGE CAMPUSCENTER_DAY]
    MC "Thanks by the way, Kodama-san."
    show PRG neutral with dissolve
    PRG "Y-You're welcome."
    MC "You know, you didn't have to reschedule your appointment just to take care of me. I can get myself to my dorm just fine."
    show PRG unique
    PRG "I-I know. But it wasn't anything too important anyway. Just a... a check up."
    MC "Well, if you say so. Sorry that I put a damper on your day off."
    PRG "Oh, it's all right! I didn't really have anything planned for my day off anyway, so now I have something to do."
    MC "Uhm, last time I checked, taking care of your injured friend wasn't exactly the ideal way to have a good time."
    PRG "Well... consider it a thank you for all that you've been helping me with lately."
    MC "I... uhm... you're welcome."
    
    scene Dorm Exterior with fade
    "After a painfully slow trip up the stairway leading to my room, I realized one crucial detail was missing."
    MC "Crap. I don't have my keys."
    show PRG sad with dissolve
    PRG "Where did you leave them?"
    "I pointed at my door and smiled sheepishly."
    MC "On my nightstand. I never grabbed them before I took my unplanned tumble."
    PRG "Is your roommate around? Maybe he'd let us in."
    "I shrugged and pounded my fist on the door firmly."
    MC "Diachi? You home?"
    show RM neutral at Position(xpos=0.55, xanchor=0.5, yanchor=1.0) behind PRG with dissolve
    UNKNOWN "Not yet."
    "I turned my head in surprise to see Diachi standing directly behind Aida. Noticing my gaze, she turned and nearly jumped out of her skin."
    show PRG surprised
    PRG "Eya!!"
    RM "What happened to you?"
    MC "Look man, let me in so I can lay down. I'll explain later."
    show RM neutral:
        linear 0.5 xpos 0.25
    "Diachi looked from me to Aida and back again before sighing and unlocking the door. Aida looked nervously over to Diachi before quickly sliding into my room in front of me. Diachi, in a sudden moment of politeness, held the door for me so I could enter."

    scene Dorm Interior
    show RM neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show PRG sad at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    RM "Okay, so details. What happened to you?"
    "Aida helped lower me onto my bed, before taking a seat at my chair by my desk. Over the next ten or so minutes, I filled him in on the whole story."
    MC "And then, the nurse had us fill out a bit of paperwork before we-"
    hide RM with dissolve
    "I had turned to Aida for her input, but when I turned back to Diachi, he was gone. Neither I nor Aida had heard the door open."
    show PRG surprised at Position(xpos=0.5, xanchor=0.5, yanchor=1.0) with dissolve
    PRG "W-Where did he go?"
    MC "He does that from time to time. At first, I didn't know what to make of it, but now I think the man just has a penchant for dramatic entrances and exits."
    "Aida nodded before standing and walking around my room, taking it all in as she went."
    MC "If I knew I was going to have company today, I would've taken the time to clean up a little."
    show PRG neutral
    PRG "It's fine. I-I don't think either of us planned for this morning. Just promise me that you'll keep an eye on any window you come across."
    MC "Hey, that window came at me from out of nowhere!"
    show PRG happy
    "Aida laughed as I turned away from her to grab a water bottle from my nightstand."
    show PRG unique
    "When I turned back to her, she was standing in one spot, staring blankly at something on the ground. I leaned over to get a better look and froze."
    "She was staring at a pair of my boxers that I'd left on the floor."
    MC "I-uh... I should really pick those up."
    MCT "Ah yes, hello awkwardness. So nice to see you again."
    PRG "..."
    "Aida's face flushed as she tried to make eye contact with me, but she kept sneaking glances at the boxers on the floor."
    "I shifted myself to the edge of the bed and stood on my one foot. Using my crutch for support, I leaned over and grabbed the boxers, and threw them into my laundry tub, which sat near the door. Rather than making it in, my shot veered to left and my boxers hung from the side of the tub."
    MC "There, all clean!"
    "I laid back down in bed and sunk back into my pillow. Aida shifted uncomfortably, her gaze still falling on the boxers."
    PRG "I... um... I'd better... get going Hotsure-san. I just remembered I have to... uh... write down something I thought I was maybe going to forget!"
    MC "Oh... uh, okay? I'll see you soon then?"
    show PRG sad
    PRG "Mhm! Yeah, I'll see you soon!"
    hide PRG with dissolve
    "I shut my eyes and sighed as Aida shuffled out of my room and shut the door, leaving me alone. A few minutes later, I got up and grabbed my handheld from my desk. With nothing else to do, grinding a handful of levels seemed like the best idea."
    jump daymenu

label PRG025:
    $setProgress("PRG", "PRG026")
    scene Dorm Interior with fade
    "I walked out of the bathroom, drying my hair after my shower. Daichi was out on some sort of “spying of the academic kind,” as he put it, so I had the place to myself for the night. Thankfully, from the time I woke up this morning, I had no pain in my ankle at all, so I didn't need my crutch anymore."
    "I'd have to remember to return it in the morning. I planned to spend the night playing video games and laying in bed, living the dream, of course. But something still was still nagging at me from the night before."
    "Before Aida left the day before, she had been acting so stiff. Almost as if she was hiding something and wanted to make sure it stayed private. Even this morning in class, she'd seemed stiff and uptight, like she was a balloon ready to burst."
    "I finished drying my hair and put on a pair of sweatpants and an old T-shirt, the perfect gaming attire. Just as I went to my bedside to lay down, I heard a rapidfire knock coming from the door."
    "Groaning, I went to the door and opened it, expecting it to be Daichi, forgetting something important for his “mission” tonight."
    show PRG sad with dissolve
    "There stood Aida, fist raised as if she was about to knock again."
    MC "Augh! K-Kodama-san?!"
    PRG "Oh Hotsure-san, thank god!"
    "Aida threw herself into my arms, knocking me backwards into my room. One touch of her skin showed that she was sweaty... very sweaty. Her skin was clammy and quite warm to the touch, and she seemed to be quivering slightly."
    "She raised her head to look at me, and I saw the unmistakable trail of tear stains. Her face was flushed, yet her cheeks were still red. She looked as if she'd ran all the way here. "
    MC "W-What's going on, Kodama-san? Is everything alright?"
    show PRG angry
    PRG "No! Everything isn't all right!"
    MC "Hey. Take a breath and collect yourself. Now..."
    extend " what's going on?"
    PRG "I-I need you, Hotsure-san! I need you right now!"
    MC "Okay? What for? Did you and Nikumaru-san get in a fight or something?"
    PRG "No! That isn't what I mean!"
    show PRG aroused
    PRG "I mean I need you, Hotsure-san! I knew that the time was coming soon, but I know that tonight is the night. It's finally time!"
    MC "For what, Kodama-san? What is it that you need me for?"
    play music Steamy
    PRG "It... It's time for us to make love, Hotsure-san!"
    show PRG aroused with vpunch
    MC "WHAT?!"
    MC "Are you serious, Kodama-san?!"
    show PRG sad
    PRG "Yes. I can't hold these feelings back any longer. They've been building up inside of me like crazy. I've tried to hold them back and suppress them, but I just... I can't do it anymore!"
    "I sat there stunned, unable to even comprehend what I was hearing. Aida was usually so reserved and a bit of a wallflower, but now, here she was telling me that she needed to sleep with me, and it had to be now apparently."
    PRG "Please, Hotsure-san! I need this worse than you'll ever know. I need to take care of these urges."
    "Aida kicked her shoes off on the floor and immediately threw herself into a heap on my bed and looked at me expectantly. The white sweater she was wearing and her extra jiggliness made it especially clear that she wasn't wearing a bra."
    "Even the skirt that she usually wore looked shorter, almost like she was wearing it higher than usual."
    MC "Kodama-san..."
    menu:
        "Let's think about this first.":
            jump PRG025_c1_1
        "No way.":
            jump PRG025_c1_2
        "Alright, let's do it.":
            jump PRG025_c1_3

label PRG025_c1_1:
    MC "Let's just give this some thought first. That's a... pretty heavy request."
    PRG "What's there to think about? You like being with me and hanging out with me, right?"
    MC "Of course I do."
    PRG "And you think I'm a good person?"
    MC "Yes, of course."
    PRG "And... you find me attractive?"
    MC "Well... I, uh... I mean..."
    "As I looked at her, Aida brought her arms together, forcing her breasts to pop up on top of her arms. I couldn't take my eyes off of them. Even in the sweater, their presence and size alone was almost otherworldly."
    show PRG aroused
    PRG "Do you... Do you think I'm sexy, Hotsure-san?"
    MC "I... uh... you're a very beautiful girl, Kodama-san. It's just, I don't think you're looking at this rationally. Sex has a lot of baggage that comes with it, not only in the moment, but even afterwards."
    PRG "You mean pregnancy?"
    MC "Well... in a way, yes. Pregnancy is a big part of that."
    PRG "Do you want kids, Hotsure-san?"
    MCT "Jeez, what kind of heavy questions float around in her head?"
    MC "I mean, probably someday. But that's a long ways off."
    MC "..."
    MC "Do you want kids?"
    "Aida leaned towards me and pulled me close to her."
    PRG "Soooo badly."
    "I stared at her in disbelief. She didn't just want sex, she wanted me to actually get her pregnant. And, just going by her body language, I could tell that turning her down wouldn't go over well."
    "Aida stood and looked me straight in the eyes, her expression unyielding."
    show PRG angry
    PRG "So, what's it going to be? You know, I don't have to do this with you, Hotsure-san. I can just as easily find someone else who can do it."
    menu:
        "Alright, fine. Let's do it.":
            jump PRG025_c2_2
        "I can't. This is wrong.":
            jump PRG025_c2_no

label PRG025_c1_2:
    MC "N-No way! It's way too early!"
    show PRG sad
    PRG "Cmon! Pleeeeeeease?"
    MC "Kodama-san, sex is usually for couples who're in a committed relationship. It's used as a sign and showing of union and togetherness. You and I aren't even dating!"
    PRG "But I feel so close to you, Hotsure-san! I feel as though we ARE together! Please, just do this for me!"
    MC "But, that's the thing, we aren't together! And we can't just call ourselves a couple just for sexual reasons."
    PRG "But..."
    MC "Look, Kodama-san. I like you, and I think you're great, but this is ludicrous and you know it."
    show PRG unique
    PRG "H-Hotsure-san. I-I don't care what I have to do. I need this and I know it may seem crazy, especially so soon, but I want this more than anything in the world. But, with you going on about how you don't want this... I guess... "
    PRG "So... that's it then. You won't have sex with me? If you won't, I know I can find someone else..."
    menu:
        "The answer is no.":
            jump PRG025_c2_no
        "If you're dead set on this.":
            jump PRG025_c2_3

label PRG025_c1_3:
    MC "All right... Let's do it."
    show PRG aroused
    PRG "You really mean it?!"
    MC "Of course I do. It's no secret that I have feelings for you, and if they're there, then why fight against them? If the feelings are there, then let's capitalize on them."
    show PRG happy
    PRG "Oh, Hotsure-san!"
    "Aida threw herself at me in a big hug, her body shaking even harder with excitement. I could feel her heart pounding away through her breasts."
    MC "Wait... I should probably have protection or something, right? I wouldn't want something..."
    extend " unplanned to happen."
    show PRG neutral
    PRG "Well... that's the thing. I'd love to be a mother someday. So I say we go into this with open minds: If I get pregnant, great! If not..."
    extend " then that's fine too."
    "What she said made sense theoretically, but a slight pause and her voice breaking ever so slightly was all I needed to know that she was really trying to hold herself together."
    MC "I... I guess that's okay?"
    MCT "There's supposed to be a handful of days in a woman's cycle where she is the most fertile, right? What're the odds that she'd be at her most fertile point on today of all days?"
    MC "All right, let's not waste any more time."
    jump PRG025_c2_1

label PRG025_c2_1:
    $setFlag("PRG_father")
    "I sat on the bed next to Aida and put my arms around her, pulling her close for a passionate kiss."
    if getFlag("PRG020_c1_1"):
        "Already, this kiss felt far more intense than the one we had shared on the rooftop."
    else:
        "I wasn't sure what to expect from Aida's kiss, but she seemed to know what she was doing, not too hard, yet enough to show that she was there, for sure."
    "Eventually, her tongue worked its way into my mouth and began to co mingle with my own tongue. Her hands began to wander from my back, travelling downwards until they reached my butt."
    "I placed my hands on her waist and carressed her as we made out. After a few moments, Aida pulled away from me and smiled."
    show PRG aroused
    PRG "Let me look the part, at least."
    "Aida took hold of the bottom of her sweater and began to tug it up, until the very bottom of her breasts were poking out. If my heart could've popped out of my chest, this would've been the appropriate time."
    "Aida pulled her sweater a bit higher, and her breasts lifted up with it, as if her sweater was stuck on something. With one of her hands, she pulled the bottom of the sweater outwards and I finally was what had held them up."
    "Her enormous breasts fell free of the confines of her sweater, her nipples stood rock hard and erect. Even though her breasts couldn't beat Honoka's for size, their presence alone was astounding."
    "They had a slight bounce to them and even though they hung just a bit, they were quite perky for their size. Aida noticed me staring at her chest and brought her breasts closer until I was barely an inch away from them."
    PRG "What do you think? Big enough?"
    "I wanted to speak, but the words wouldn't come to me. Instead, I felt my body do the talking for me as my sweat pants pulled away from me. My erection protruded inside of my sweatpants, pushing them out like a tent with a pole inside of it. I was ready to go."
    show PRG surprised
    PRG "..."
    "Aida reached down to my sweatpants and gently caressed my throbbing cock, her eyes wide, like she'd never seen a dick before. If she was this excited just seeing it from outside of my pants, I couldn't wait to see her reaction when my pants came off."
    MC "How does it feel?"
    PRG "It's big... and thick. I've never felt one before now."
    "It hadn't occurred to me until then that Aida was almost definitely a virgin, but I did my best not to draw attention to it. The last thing I wanted to do was scare her off by insulting her."
    show PRG neutral
    "Aida reached up and tugged at my shirt, pulling it up and over my head. I followed her lead by taking hold of her skirt and working it off of her hips and down, leaving her in her pink panties."
    MC "Wow..."
    "It was my turn to give her some attention. I sat on the bed and motioned for her to take a seat next to me. Once she was in position, I placed my hands on her abdomen and pulled her back in for another kiss."
    "Without any warning, Aida placed her hands on my hands and guided my hands up to her boobs. I got butterflies the minute I felt her nipples brush against my fingertips."
    PRG "Mm-mmm..."
    "Aida shut her eyes and moaned ever so softly as I caressed her breasts. I ventured a guess that, for their size, they must've been incredibly sensitive. So sensitive in fact, that when I bent over and began to suck on her nipples, her body shook as if she had an electrical current flowing through her."
    show PRG surprised
    PRG "H-H-Hotsure-san! T-That feels a-amazing!!"
    "She put her hands on the back of my head and pushed me against her breast, which made me suckle even harder. The skin on her breasts was incredibly soft and smooth, like silk, making it all the more comfy to be smashed into."
    "Once I felt I had teased her boobs enough, I leaned backwards so I was laying on my back, my erection sticking up inside of my sweatpants like a flagpole. Aida's eyes immediately shot to it and stayed stuck there."
    show PRG aroused
    PRG "My turn?"
    MC "By all means."
    "Aida wrapped her hands around my sweatpant's waistband and slid them down, leaving me in just my boxers. By now, my heart was nearly beating through my chest, I was so ready to go."
    "Finally, Aida took hold of my boxers and pulled them down, her jaw dropping when my dick sprung up in front of her."
    PRG "..."
    PRG "I want it. Now."
    "Aida lifted her legs and slid her panties off, revealing her perfectly plump ass and tantalizing, delicate pussy."
    PRG "I know what I'm doing for the most part, but, since this is my first time, could you help guide me?"
    MC "It's alright, I'll help."
    "Before we got started, I placed my hand on Aida's thigh and slowly worked my way up until I was just touching her needy pussy."
    MCT "She's nearly dripping wet down there. Perfect."
    MC "Alright, so swing your leg over me so you're on top."
    "Aida did what she was told, bringing her leg over the top until she was loosely straddling me."
    MC "Yes, perfect, but keep your ass in the air for now."
    "Aida nodded and raised her lower half so it was about half a foot above me and my waiting cock."
    MC "Alright, now gently ease yourself down onto me."
    "Aida lowered her ass slowly, as I held my dick in place, until we were perfectly lined up. Then, Aida pressed down and I slid inside of her waiting pussy."
    #CG
    #pause
    PRG "Oh... OHHHHH!! It... It feels..."
    MC "Y-Yeah?"
    PRG "God... I didn't think it would feel this good!"
    "Aida leaned back and put her hands on my legs to brace herself, and began to work her way up and down on my member. I took hold of her hips and held her in place, thrusting into her deeper and deeper with every bounce. Her breasts bounced wildly on top of her chest as I pounded her harder with every passing minute."
    PRG "Ooh... H-Hotsure-san!!"
    MC "Ah...nngh..."
    "Aida shut her eyes and threw her head back, each breath becoming quicker and more shallow. She gripped harder onto my thighs, in a sort of desperate sex balancing act. All the while, I felt her soaking wet pussy engulfing my cock, my balls slapping against her with every movement."
    "I gritted my teeth and focused on the plump, curvy girl riding me. She was unbelievably tight, but with how wet she was, lube was merely an afterthought at this point."
    MC "A-Ah... Kodama-san!"
    PRG "W-Wha...?"
    MC "I-I'm... I'm gonna... nngh..."
    PRG "Do it... let yourself go..."
    "Aida cried out loudly as I exploded inside of her, leaving me no chance to pull out. Aida smashed my cock as far into her as she could, making sure that nothing could escape."
    #REMOVE CG
    show PRG aroused
    PRG "That was... so good."
    "We sat there for a moment, breathing heavily and staring into each others eyes. Aida brought herself down until she was laying on top of my chest. She craned her neck and locked lips with me once more, my dick still inside of her."
    "The lustful, almost lunatic behavior had faded from her psyche, and I had no doubt that her kiss was genuine and her touch was true."
    "She stayed where she was for a few minutes, panting softly, until she righted herself and carefully stood back up, with one of her hands holding the lips of her pussy shut so nothing could escape. Hardly one drop of semen fell from her as she slipped her panties, skirt, sweater, and shoes back on."
    PRG "I'd love to do this again, Hotsure-san. Don't leave me hanging though."
    MC "I... uh?"
    hide PRG with dissolve
    "I watched as she blew me a kiss and happily pranced out of my room, leaving me lying on my bed with a million thoughts passing through my head. Not even one of them concerning my future."
    jump daymenu

label PRG025_c2_2:
    $setFlag("PRG_father")
    MC "Look, I don't want you going to any random guy in the school for that sort of thing. Sex is supposed to be something special, and I feel honored that you'd ask me. So... if you want babies that badly and you are one hundred percent sure... I'll give them to you."
    show PRG happy
    PRG "You will?!"
    MC "I will."
    PRG "Oh, Hotsure-san!"
    "Aida threw herself at me in a big hug, her body shaking even harder with excitement. I could feel her heart pounding away through her breasts."
    "I could feel her genuine happiness through her hug. Even though Aida was acting far from her norm, I could tell she wanted this more than anything, and I'd be a fool to not help her."
    MC "Alright, let's not waste any more time."
    show PRG neutral
    "Aida nodded. A sudden look of nervousness came across her face, and I realized a rather important bit of information."
    MC "You've... never had sex, have you?"
    PRG "No, never. But I'm set on this, Hotsure-san. I want you as my first!"
    "I sat on the bed next to Aida and put my arms around her, pulling her close for a passionate kiss."
    if getFlag("PRG020_c1_1"):
        "Already, this kiss felt far more intense than the one we had shared on the rooftop."
    else:
        "I wasn't sure what to expect from Aida's kiss, but she seemed to know what she was doing, not too hard, yet enough to show that she was there, for sure."
    "Eventually, her tongue worked its way into my mouth and began to co mingle with my own tongue. I laid myself back, pulling Aida along as I fell back onto my pillow, her lips never breaking from mine."
    "She gently pulled her lips from me, and stood up next to the bed."
    PRG "Since you're doing this for me, let me do something extra special for you."
    "Aida took hold of the bottom of her sweater and began to tug it up, until the very bottom of her breasts were poking out. If my heart could've popped out of my chest, this would've been the appropriate time."
    "Aida pulled her sweater a bit higher, and her breasts lifted up with it, as if her sweater was stuck on something. With one of her hands, she pulled the bottom of the sweater outwards and I finally was what had held them up."
    "Her enormous breasts fell free of the confines of her sweater, her nipples stood rock hard and erect. Even though her breasts couldn't beat Honoka's for size, their presence alone was astounding. They had a slight bounce to them and even though they hung just a bit, they were quite perky for their size."
    PRG "Like them?"
    "I wanted to speak, but the words wouldn't come to me. Instead, I felt my body do the talking for me as my sweat pants pulled away from me. My erection protruded inside of my sweatpants, pushing them out like a tent with a pole inside of it. I was ready to go."
    show PRG aroused
    PRG "And I see you're ready to go, so it's time for your present."
    "Aida reached for me and slid me to the very edge of the bed. She pulled my sweatpants and boxers to my ankles all in one motion, leaving me naked on my bed, and rock hard to boot."
    "She got on her knees in front of me, and placed her tits on my lap, where they sat perched on my legs for a moment before she put her hands on either side and slammed my cock between them. She began pumping her chest up and down, giving me the most fantastic titjob."
    MC "Ah-AHH! Oh my... Kodama-san!"
    show PRG happy
    "Aida smiled and licked her lips. The tip of my dick just barely poked up from the top of her breasts. As my tip stuck up on her downstroke, she put her chin to her chest and licked the tip of my dick ever so gently."
    "The feeling was beyond anything I'd ever felt in my life."
    "Aida smiled at the sound of my moans, and, releasing her boobs, took my dick in one hand and began to slide it into her mouth. She relaxed her throat and took nearly the entire length of my cock, her now free hand caressing my balls as she sucked."
    MC "K-Kodama-san! If... If you don't stop now... I'll..."
    "I hadn't even finish my sentence before Aida released my cock and backed away, pulling her skirt down to her ankles."
    MC "You're... really good at that."
    PRG "I watched a few videos. I wanted to be the best I could at this."
    "Aida went back to the bedside where I sat and grabbed a hold of my cock."
    show PRG aroused
    PRG "Now. Put this in me."
    "Aida lifted her legs and slid her panties off, revealing her perfectly plump ass and tantalizing, delicate pussy."
    "Not wanting to keep a lady waiting, I moved to the center of the bed and moved my legs into position. Aida was on me in a flash, and without even waiting for me to say I was ready, she lowered herself onto my waiting cock."
    #CG
    #pause
    PRG "Oh... OHHHHH!! It... It feels..."
    MC "Y-Yeah?"
    PRG "So good!!"
    "Aida leaned back and put her hands on my legs to brace herself, and began to work her way up and down on my member. I took hold of her hips and held her in place, thrusting into her deeper and deeper with every bounce. Her breasts bounced wildly on top of her chest as I pounded her harder with every passing minute."
    PRG "Ooh... H-Hotsure-san!!"
    MC "Ah...nngh..."
    "Aida shut her eyes and threw her head back, each breath becoming quicker and more shallow. I could feel her ass slapping against my pelvis, and I took hold of it, feeling her soft, squishy cheeks in my hands."
    PRG "I..."
    extend " I want babies in me!"
    MC "A-Ah... Kodama-san!"
    PRG "W-Wha...?"
    MC "I-I'm... I'm gonna... nngh..."
    PRG "Yes! Please!!"
    "Aida cried out loudly as I exploded inside of her. She let herself slide down as far as she could onto me, my cum blasting deep inside of her."
    #REMOVE CG
    show PRG neutral
    "We sat there for a moment, breathing heavily and staring into each others eyes. Aida laid her hands on her middle and smiled, rubbing her hands across her abdomen."
    PRG "Thank you, Hotsure-san. This couldn't have been done without you."
    "She stayed where she was for a few minutes, panting softly, until she stood back up and crawled off of my bed. Surprisingly, not a single drop of semen fell from her pussy."
    "She gathered her clothing and got dressed as I watched her from my bed. She glanced at me as she did so and smiled, almost as if she was pleased that I was watching her dress herself."
    PRG "I hope this won't be the last time we do this."
    MC "I hope the same."
    hide PRG with dissolve
    "I watched as she blew me a kiss and happily pranced out of my room, leaving me lying on my bed with a million thoughts passing through my head. Even with everything that had just happened, I was surprisingly calm, and in a way, excited for what could happen."
    jump daymenu

label PRG025_c2_3:
    $setFlag("PRG_father")
    "I took a deep breath. Despite how irrational she was acting, I knew that she wouldn't stop until she was knocked up."
    MC "Kodama-san... If you're dead set on this..."
    extend " I'll do it."
    show PRG neutral
    PRG "W-What? Really?!"
    MC "Yes, even though I think it's a rash decision. But, I can also tell how much this means to you. And besides, if it's me that's doing the deed, then I know that some asshole isn't going to be getting you pregnant and abandoning your kids."
    show PRG happy
    PRG "Thank you, Hotsure-san! Thank you so much!"
    "Aida engulfed me in a hug, her heart pounding away inside her chest."
    MC "Alright, ready then?"
    show PRG neutral
    "Aida nodded and pulled me in close, enveloping me in a firm kiss. She was eager, working her tongue in my mouth straight away."
    "We sat there on the bed, gently making out for quite some time, until Aida stood and faced me on the bed."
    PRG "I want to see..."
    "Aida pulled my shirt over my head and threw it across the room. Without even stopping to look at my chest, she was onto my pants and had them down to my ankles in a flash. Out of pure surprise, and the fact that an extremely curvy girl was undressing me, I felt myself swelling and getting hard as she looked down to my boxers."
    "Noticing the bulging front of my boxers, she giggled and pulled them down as well, revealing my fully erect cock."
    show PRG aroused
    PRG "Perfect. Just perfect."
    "She reached her hand down and began to stroke me, gently at first, then increasing in speed rapidly. I laid myself back on the bed and moaned softly."
    "My heart began to pound and I felt myself getting more in the mood. I was so ready for this now, despite me knowing deep down that I wasn't fully on board."
    "I sat back up and gently pulled Aida's hand from my member. I guided her down onto the bed beside me, working my hands under her sweater and pulling it over her head, her tremendous rack falling from within and hanging freely from her chest."
    "I moved down to her skirt and slid it off as well, leaving her in just a pair of delicate, pink panties."
    "Aida was panting hard by now from anticipation alone. I hadn't done a thing to her yet, but already, her face was turning red and her breath had shortened."
    "Looking down, I noticed the faintest wet spot on her panties. I took hold of the sides and pulled them down slowly, revealing her puffy pink pussy lips, and clit to match."
    "Before she could speak, I had my head between her legs and I was licking her clit. She was wet beyond belief, and she was trembling slightly from the excitement. I felt her entire body move as I sped up my licks, working in circles around her clit."
    PRG "O-Oh!! Y-Yes, Hotsure-san! Eat me out!"
    "I had heard of how to eat out a girl before, but had never done it myself, so I was flying somewhat blind, but I did manage to make her moan, so I consider that a win."
    MCT "Wow. She actually tastes good."
    "I stood up, wiped my face, and got a look at Aida. She was panting like a runner after a marathon, her legs spread as wide as she could manage. All I had to do was enter."
    "I lined myself up and brought my cock right up to her pussy lips, before I gripped onto her hips and slowly penetrated her."
    show PRG surprised
    "Her cry was loud, but filled with pleasure, and her face gave those feelings away. I started slowly, letting her get used to the feeling, before picking up speed and power, moving deeper and deeper inside her."
    "I grabbed her ankles and put one onto each of my shoulders, letting me get even deeper inside of her. I felt my balls slap against her as I thrusted, feeling how wet her skin was down there. It was fairly safe to say that I was doing well."
    "Feeling myself draw closer and closer to climax, I rolled myself back so I was lying down on the bed, and Aida mounted on top of me. I had to admit, the view was remarkably pleasant."
    #CG
    #pause
    "The feeling of Aida on top of me was like if heaven had joined with earth. Our bodies just seemed to fit together like a human puzzle piece."
    PRG "H-Hotsure-san... nghh... this is... sooo good!"
    MC "I-I know!"
    PRG "I-I never want this to stop!!"
    "Of course, just then, I felt the familiar creeping feeling inside of me and I knew what was coming next."
    MC "K-Kodama-san! I-I'm coming!!"
    PRG "Yes! It's finally time!"
    "Aida put her full force onto me as I blasted into her, feeling my cock throbbing away inside of her."
    #REMOVE CG
    show PRG aroused
    "Instantly, I felt weak, and a feeling of shame washed over me. I knew that this was it."
    PRG "I-I can feel it... inside of me."
    "Aida rubbed near her vagina as she smiled at me with thankful eyes."
    show PRG neutral
    PRG "I don't know what to say, Hotsure-san, but that was everything I had hoped for."
    "Aida stood up finally and let me slide out of her gently. Hopping off the bed and dressing quickly, I noticed that, even though we had just had sex, she seemed more faded, as if she was already dreaming of everything pregnancy would bring her."
    MC "Happy?"
    PRG "Yes, I'm very happy."
    "Aida finished getting dressed and went to my side."
    PRG "Thank you again, Hotsure-san. I'll see you soon, okay?"
    hide PRG with dissolve
    "I nodded as she happily let herself out of my dorm. I pulled my legs to the side of my bed and sat, putting my face in my hands. I knew that Aida was ready for this and she thought she was ready to handle it, but I still wondered. Would I be ready?"
    jump daymenu

label PRG025_c2_no:
    show PRG sad
    "Aida shook her head, and in frustration, threw her hands in the air. She stood and pulled her shoes back on, her eyes never meeting mine."
    PRG "I don't see your point of view, Hotsure-san. I'm going to go find someone who actually understands why I want this."
    MC "I know why, I just-"
    hide PRG with dissolve
    "She spun to glare at me one final time before throwing the door open and stomping out into the hallway, her fists balled up so tight they had turned white. I walked to the door to follow after her, but by the time I got out the door, I had lost sight of her, and the thud of her shoes on the hard floor faded off into nothingness."
    "I stepped back into my room and sat on the bed, throwing my face in my hands. Everything between us had just changed in the span of only a handful of minutes."
    jump daymenu

label PRG026:
    $setPregnant()
    if getFlag("PRG_father"):
        jump PRG026_father
    else:
        jump PRG026_nofather

label PRG026_father:
    $setProgress("PRG", "PRG027")
    scene Dorm Interior with fade
    play music Rain
    "I smoothed my shirt with my hand and smiled. It had been a few days since Aida and I had... made love, and weirdly, I hadn't seen her since."
    "She hadn't been in class for two days. According to Alice, she hadn't been feeling well as of late and was resting in their dorm. Although, even with Alice's assurance that she would be alright, I still was worried."
    "I ran a brush through my hair in a failed attempt to look less shaggy than I was. After our special moment together, I wanted to make sure that I at least looked presentable."
    "After one last glance in the mirror, the door was open and I was off down the hall."

    scene Dorm Exterior with fade
    "I hoped that conversation wouldn't be awkward between us. I still wasn't completely sure how I felt about the whole experience. I mean, yeah, I'd slept with her, but she had been acting so strangely that day, almost like she was in a trance. I just hoped that she'd look back on it as a positive experience."
    "Soon, I stood outside her door, which looked much more imposing than I remembered from my last visit."
    MCT "Alright, you can do this. Just knock."
    "I took a deep breath and knocked lightly on the door."
    PRG "W-W-Who is it?"
    MC "It's me, Kodama-san. How are you feeling?"
    "There was a pause from the other side of the door."
    PRG "H-Hotsure-san?!"
    MC "Yeah? Everything okay?"
    PRG "G-Go away! I... I don't want to get you sick!"
    MC "Kodama-san... if you're really sick, you need to go to the infirmary."
    PRG "I-I-I was already there! They just told me to rest and try not to get anyone else sick."
    MC "Oh, alright. Is Nikumaru-san staying somewhere else while you're sick, then?"
    "There was an even longer pause from behind the door."
    PRG "I... um..."
    MC "Look, don't worry about it. It's not really any of my business where she's staying. I'll let you get your rest, Kodama-san. Don't be a stranger, alright?"
    "As I turned to leave, I heard the tiniest of creaks, and as I turned, I saw that Aida's door was now open a crack."
    PRG "Y-Y-You can come in... just... keep your eyes shut."
    stop music

    scene black with fade
    "I shrugged and shut my eyes, instinctively bowing my head, as I pushed open Aida's door. I felt a hand grab me and lead me to sit on something soft. A bed."
    PRG "H-Hold on."
    "I heard fumbling in the room around me. A drawer slammed shut, a closet door opened and was promptly shut, and the rustling of fabric caught my attention."
    PRG "..."
    PRG "... Y-You can open your eyes now."

    scene Dorm PRG Day with fade
    "I opened my eyes slowly and lifted my head."
    show PRG sad with dissolve
    play music PRG
    MC "Ah... ?! Y-You... Uhh..."
    "My eyes nearly blew out of their sockets. Aida stood before me, her face more red than I'd ever seen it, which was an achievement in and of itself. Her usual school issued uniform was stretched nearly to its breaking point, doing its best to cover her breasts, which were definitely much larger than I last remembered."
    "My heart nearly stopped when my gaze went lower and stopped at her newly grown stomach, which jutted out from her as if she'd put a beach ball up her shirt. Going down her shirt, the buttons held as tightly as they could, barely restraining her new girth."
    "Aida looked at the floor before walking to her desk and handing me a piece of paper, the same wrinkled paper from the day I fell from my window."
    MC "T-This is..."
    PRG "R-Right. This is my growth factor."
    "I scanned over the sheet with lightning speed, until my eyes fell flat on one word."
    MC "Hyperfertile."
    PRG "The day after you and I made love, I-I woke up with this belly. I wasn't sure what to do, and I was really scared... So I went to the infirmary right away that morning."
    show PRG unique
    PRG "The nurse told me to keep an eye on it, and come back in two days if anything changed. When I woke up the next morning, my... breasts grew too."
    "I stared at her dumbfounded, in awe at her new form."
    PRG "Then, I woke up this morning... and I had grown even more. So, like the nurse instructed, I went back to the infirmary."
    "Aida passed me one more sheet of paper with an official stamp from the Seichou Academy infirmary. As I skimmed over it, a lump formed in my throat. When I made it to the end, I swung my gaze back to Aida, as she nervously wrung her hands in front of her."
    PRG "I-I..."
    show PRG sad
    PRG "I-I'm pregnant, Hotsure-san..."
    PRG "And..."
    extend " you're the father."
    show PRG sad with vpunch
    MC "WHAT?!"
    "Aida nodded solemnly, unable to meet my eyes."
    PRG "I... I lied about being sick. I didn't want anyone to see me like this, not until I had a chance to speak with you first."
    MC "K-Kodama-san. I-I don't... I mean... we're barely adults. How are we going to care for a kid? I don't even know the first thing about being a parent!"
    PRG "I-It's not like I do either, Hotsure-san."
    MC "But..."
    PRG "The academy is going to help pay for any medical expenses I'll have, so I'll be alright finance wise, at least for a while. But... I need to ask you something, Hotsure-san."
    MC "Y-Yes?"
    stop music
    PRG "There... there isn't an easy way to ask this, but in this situation, a lot of fathers would probably..."
    extend " leave."
    PRG "Will you still be there for me?"
    "I felt a drop in my chest. I knew what she was going to ask even before she asked the question, but the notion still hit me like a ton of bricks. I knew the honorable thing to do was to stand by her and be a man. But, I'd be swapping that out for a good majority of my time and freedom."
    MC "I..."
    menu:
        "Yes":
            jump PRG026_c1_1    #+6
        "No":
            jump PRG026_c1_2    #-20, routelock

label PRG026_c1_1:
    MC "I... "
    MC "Yes. Yes, I'll be there. I'm not about to run away, let alone leave you a single mother."
    show PRG neutral
    play music PRG
    "Aida's eyes shone as a smile finally crept onto her face, like a light in a dark room."
    PRG "D-D-Do you really mean it? Truly?"
    MC "Yes, Kodama-san. I'll stand by y-urk!"
    show PRG happy
    $setAffection("PRG", 6)
    "The last half of my sentence was caught off by Aida slamming herself into me and engulfing me in a big, pregnant girl hug."
    PRG "T-Thank you, Hotsure-san! Thank you, thank you, thank you!"
    "I brought my arms down around her and sighed, letting my head rest on top of hers."
    PRG "I'll do my best. I want to be the best mom I can be."
    MC "And I... I'll try to be the best dad I can be."
    show PRG neutral
    PRG "I'm going to hold you to that, you know."
    MC "I know."
    PRG "..."
    PRG "We'd better be getting to class, Hotsure-san."
    MC "We should. Are you ready for your grand entrance? Everyone is going to be floored when they see you."
    PRG "I know... but I'm ready. I'm proud of myself, and of what I'm carrying."
    "She wrapped her arms around her stomach and grinned."
    MC "I'm proud of you too, Kodama-san. It takes a lot of bravery to be out and proud about yourself."
    PRG "I-I have to be brave, us moms have to be tough, you know. No matter what circumstances we may come across."
    MC "Here here! Well, let's get going then!"
    
    scene Dorm Exterior with fade
    "Aida nodded and led us out the door and down the hallway, making no effort to hide herself whatsoever. Even still, I had my suspicions that all was not well with her. She seemed like she was in a state of shock. Hell, if I woke up one day and had a gut that size hanging off of me, I probably would've been out of it, too."
    "As I followed behind her, I couldn't help but let my eyes take in the view in front of me. While it was blatantly obvious that she was pregnant if you saw her from the front, from behind, you'd be forgiven for thinking that she was just a well endowed woman."
    "I noticed then how, whenever Aida walked, both her legs and butt would jiggle ever so slightly. If you weren't looking directly at her lower half, you most likely wouldn't notice it, but... my eyes had their own agenda."
    "Even as I admired Aida's newly grown assets, the fact that I was going to be a father hung heavily over me. Excitement was stirred in with general anxiety, making for an odd feeling of nervous excitement. I knew that I had no idea what it took to be a father, but I also knew that I had no choice in the matter."

    scene Campus Center with fade
    "We walked out into the main courtyard, and made way towards the classrooms. The campus was fairly empty, mainly because it was still early, but I couldn't help but notice the occasional side glance or wide eyed stare."
    "Aida noticed this too, and fell back to my side, reaching for my hand."
    show PRG unique with dissolve
    PRG "E-Everyone is looking at me..."
    MC "I know, but chin up. You're a mom now, remember?"
    PRG "I..."
    show PRG happy
    PRG "Y-You're right, I am."
    "She smiled and walked forward with pride once more, until we reached the classrooms."

    scene Hallway with fade
    play music Schoolday
    "The hallways shared the emptiness of the courtyard, and were strangely quiet. I was never here this early, so I guess it just wasn't as lively as it was five minutes before classes began."

    scene Classroom with fade
    #[SCENE CHANGE CLASSROOM_DAY]
    "The classroom was bare as we walked in. Out of habit, Aida took her seat and I proceeded to hover next to her, butterflies fluttering about in my stomach as we both anxiously awaited our first classmate's arrival."
    show PRG angry at Position(xpos=0.6, xanchor=0.5, yanchor=1.0) with dissolve
    PRG "Mmph!"
    MC "You okay?"
    PRG "F-Fine! I just... I'm not used to sitting down... with this here."
    "She gestured at her belly, which had been pressed against the desk's edge. She scooted her chair out to give herself a bit more room."
    "Then, a thought clicked into my mind."
    MC "Kodama-san. Does Nikumaru-san know about your factor?"
    show PRG unique
    PRG "Yes, but she doesn't know that I actually am pregnant now."
    MCT "Ooo boy."
    MC "I wonder how she'll react. I hope she won't be upset that you didn't mention anything, being that she's your roommate and everything."
    PRG "She knew that it would probably happen eventually I don't think she'll make too big of a deal out of it."
    show PRG surprised
    "Both of us stopped as we heard a familiar sound:  the sound of shoes clicking down the hallway."
    MC "Someone's coming. Get ready."
    "Aida nodded and did her best to put on a brave face."
    show PRG neutral
    show GTS neutral at Position(xpos=0.8, xanchor=0.5, yanchor=1.0) with dissolve
    GTS "Oh! Good morning, Hotsure-san and Kodama-sa-!"
    show GTS surprised
    "She stopped short when she noticed Aida's grown stomach, the surprise on her face shone clear."
    GTS "I... um, I don't usually see you two out and about this early."
    MC "We both decided to hit it early today. Doesn't pay to waste precious daylight, you know."
    GTS "I-I agree."
    "I had never seen Naomi as surprised as this. In fact, I'd barely seen her surprised period."
    GTS "I don't mean to pry, but..."
    PRG "I-It's alright, Yamazaki-san. You're the first of our classmates to see me. This is my... growth. It's going to be a bit of a shock for everyone."
    GTS "I-I see."
    hide GTS with dissolve
    "Naomi bowed courteously to both of us. She took her seat and began rifling through her bag. I leaned over to Aida so I could whisper in her ear."
    MC "Weren't you going to mention the pregnancy too?"
    PRG "I'm going to tell the class all at once. It'll be a little easier."
    show FMG neutral at Position (xpos=0.8, xanchor=0.5, yanchor=1.0) with dissolve
    show BBW neutral at Position (xpos=0.2, xanchor=0.5, yanchor=1.0) with dissolve
    "I nodded, not noticing Akira and Alice as they walked in. I turned to the door, spotting them and their glances at us."
    BBW "Good morning Kodama-san and Hotsure-san."
    PRG "Good morning, Nikumaru-san."
    BBW "I trust you are feeling better? I'd rather not catch anything today."
    PRG "I-I'm fine now, thank you."
    show FMG surprised
    "As the two spoke, Akira's gaze traveled to Aida, her eyes glued onto her. If Akira was good at anything besides working out, it was wearing her emotions on her sleeve."
    BBW "Well, do take care of yourself from here on out. And I'm assuming I'm safe to move back into our dorm?"
    PRG "Yes. Whenever you'd like."
    BBW "Excellent. I'll make sure to stop by for some more of these so called “late night chat sessions,” Mizutani-san."
    show FMG happy
    FMG "You'd better! I'm gonna miss having you around. It was a ton of fun while it lasted."
    hide FMG with dissolve
    hide BBW with dissolve
    show BE happy at Position (xpos=0.9, xanchor=0.5, yanchor=1.0) with dissolve
    "Behind the two of them, Honoka hurried into the room and plunked down in the desk directly in front of Aida. Shiori followed closely behind her and took her seat immediately. Grabbing a notebook from her bag, she started writing something across the top of her page."
    BE "Morning guys! Feeling any better, Kodama-sa-"
    show BE surprised
    "The words caught in her throat as she looked down for the first time and spotted Aida's new growth."
    BE "W-Whoa..."
    MC "Honoka!"
    BE "I'm sorry! It's just, I didn't expect you to blossom so much in the span of a few days, Kodama-san. I guess your factor is a bit of a mix of some ours, hm?"
    PRG "I-In a way."
    MC "Em... Honoka?"
    show BE neutral
    BE "Kei-chan, please. You're interrupting girl talk."
    MC "There's something you need to know."
    BE "Alright shoot. Tell ol' Honoka the tea."
    MC "Aida is... um..."
    PRG "I'm pregnant, Inoue-san."
    show BE surprised
    BE "What?! Kodama-san is pregnant?!"
    show AE surprised at Position (xpos=0.15, xanchor=0.5, yanchor=1.0)
    show BBW neutral at Position (xpos=0.3, xanchor=0.5, yanchor=1.0)
    show FMG surprised at Position (xpos=0.45, xanchor=0.5, yanchor=1.0) behind PRG
    show GTS surprised at Position (xpos=0.75, xanchor=0.5, yanchor=1.0) behind PRG
    show PRG surprised
    stop music
    "Every conversation in the room came to a halt. Akira looked at Aida in surprise. Naomi was so shocked, she dropped the book she'd been skimming through and stood to join the newly formed group. Even Shiori set down her pencil and came to join the circle."
    BE "A-Are you messing with me, Kodama-san?"
    "Aida looked around frantically at the suddenly crowded area around her and put her arms over her stomach, as if to protect herself."
    show PRG unique
    PRG "N-No... It's the truth. I-I'm pregnant."
    "She looked at everyone's faces and slowly lifted her arms, putting her new belly on display for everyone to see for themselves."
    BE "Oh my god! Wait, hold on a sec. Who's the father then?"
    show PRG neutral
    PRG "Well..."
    "She turned to me and smiled sweetly. Honoka looked from Aida and then to me, an increasing level of surprise clearly building within her."
    BE "Oh my god!"
    FMG "Whoa! Hotsure-san is gonna be a dad?"
    GTS "C-Congratulations you two! You'll make amazing parents!"
    "Only two people didn't speak up."
    hide AE with dissolve
    "Shiori shook her head, turned, and went back to her desk, clearly wanting no part in this."
    hide BE with dissolve
    hide GTS with dissolve
    hide FMG with dissolve
    "Alice came to stand next to Aida's desk. Surprisingly, she didn't look remotely upset."
    BBW "Is this true, Kodama-san? It happened?"
    show PRG unique
    PRG "Y-Yes, Nikumaru-san."
    BBW "Kodama-san, I'm pleased for both you and Hotsure-san."
    play music Schoolday
    show PRG surprised
    PRG "W-What? You aren't mad?"
    BBW "Not in the slightest. Surprised, yes, but not upset at all. Motherhood is a wonderous thing, and you should do your best to cherish it and all that it brings."
    show PRG happy
    PRG "T-Thank you, Nikumaru-san. I will."
    BBW "As for you, Hotsure-san. I expect you to act as a proper father would. There is no excuse for anything less."
    "I nodded at her as Tashi-sensei finally entered the room to begin class."
    jump daymenu

label PRG026_c1_2:
    $setFlag("PRG026_c1_2")
    play music Bittersweet
    MC "I..."
    MC "I- I can't, Kodama-san... I just can't."
    "Aida didn't say a word as her head drooped down. Her shoulders began to shiver as the tears began to fall."
    PRG "B-B-But... but why?"
    MC "I'm not ready to be a father, Kodama-san. No matter how you slice it, I'm not mature enough, and I sure as hell don't think I can handle the responsibility."
    MC "I-I'm sorry."
    "Aida didn't say anything as she continued sobbing. She sat on her bed gently and buried her head into her pillow, muffling her sniffles."
    MC "I..."
    $setAffection("PRG", -20)
    $disableRoute("PRG")
    PRG "Just... please go, Hotsure-san."
    "I nodded. A weight in my chest hung heavily on me as I made my way to the door, stopping once my hand reached the brass knob."
    MC "Will I see you in class then?"
    PRG "You probably will, but..."
    extend " just leave me alone, Hotsure-san. For the good of my feelings, please..."
    MC "I... Alright. I'm sorry."
    PRG "J-Just go."
    scene Dorm Exterior with fade
    "I opened the door and showed myself out. Almost immediately after the door shut, I heard the lock click shut behind me."
    "I sighed and trudged back to my dorm."
    scene Dorm Interior with fade
    "I didn't go to class that day. Daichi brought me my homework after, which I left to gather dust on my desk."
    "I had never felt so lost."
    jump daymenu

label PRG026_nofather:
    $setProgress("PRGend_nofather")
    scene Dorm Interior with fade
    play music Rain
    "I brushed a stray piece of hair off of my uniform and took a breath. I was going to go to Aida's room and I planned to walk her to class."
    "She'd been sick the last few days, so I hadn't seen her recently, but from the occasional text here and there, I gathered that she was feeling at least passable."
    "It was strange. Even though I felt comfortable with Aida, having spent so much time with her, after our latest encounter, I wasn't quite sure how to feel."
    "Would she be upset that I hadn't slept with her? Or would she find it noble that I didn't take advantage of her when she wasn't thinking clearly?"
    "Quickly dismissing the thought, I finished getting ready and was out the door, heading for the girl's dorm."
    
    scene Dorm Exterior with fade
    "After a brief walk, I stood before her door and knocked gently. From behind the door, I heard a bit of rustling and a slight moan."
    PRG "Hello? Who is it?"
    MC "It's me, Kodama-san. Good morning!"
    PRG "H-Hotsure-san? What're you... doing here?"
    MC "I was wondering if I could walk you to class? I figured on your first day back, an escort may not be the worst idea."
    "A tension filled pause was all I got in reply. I heard the same rustling sound again, but this time, it was more rushed sounding, as if Aida were looking for something."
    PRG "Um... That's very nice of you, Hotsure-san, but uh... y-you should've given me a bit more of a warning."
    MC "Oh, I'm sorry. I just wanted to surprise you, do something to help make you feel better, you know?"
    PRG "I-I understand, and I appreciate the gesture."
    MC "Well..."
    extend " could I at least see you before I leave? As much as I like talking to this door, it'd be nice to see you too."
    "Another pause, even longer this time."
    MCT "Geez, it's like pulling teeth."
    PRG "A...Alright. Just... keep your eyes closed until I tell you, okay?"
    MC "Um... whatever you say, I guess."
    stop music

    scene black with fade
    "I shut my eyes as told and heard the door open. I jumped when I felt a hand grab my arm and pull me into the room. The hand pulled me over to something soft and pushed me onto it."
    PRG "O-One second. Could you put your head down as well? So you're looking at the floor?"
    "Rather than arguing, I put my chin to my chest and waited. Even with my eyes shut, I could tell that Aida was nervous about something, but I had no idea why."
    "Along with Alice, I was one of Aida's closest friends, so she had no reason to be nervous..."
    extend " right?"
    PRG "Alright. I have to tell you something, Hotsure-san. And... I don't think you'll believe me when I say this."
    MC "You didn't kill someone did you?"
    PRG "A-Ach! No! Of course not!"
    MC "Alright, now that that one is out of the way, please continue."
    PRG "Um..."
    PRG "Okay. The other day, when I came over to your dorm and begged you to... have sex with me?"
    MC "Yeah? What about it?"
    PRG "Well... after I left, I went to the cafeteria. I had this feeling inside of me, it was unlike any other feeling I've ever had. Like a mix of passion and lust all at once, swirling together like a storm inside of me."
    PRG "When I walked into the cafeteria, I-I saw a boy sitting by himself in the corner. I... went over to him, and without introducing myself, asked him..."
    "She stopped. I could hear from her tone of voice that she was beginning to get choked up."
    MC "Asked him what?"
    PRG "I asked him..."
    PRG "I asked him if he would have sex with me."
    "Instantly, a whole colony of butterflies hit my stomach. Even though I had turned Aida down that day, I still had feelings for her. The idea of her and another guy doing... that. It was nauseating."
    MC "Well... what happened next?"
    PRG "He... accepted, and he took me back to his dorm room, and we... had sex."
    MC "I see..."
    PRG "B-But that's not all..."
    "I heard Aida begin to cry, her sniffles and sobs interrupting nearly every word."
    MC "What else happened?"
    PRG "H-H-Hotsure-san, I'm... I-I..."
    PRG "I'm pregnant!"
    
    scene Dorm PRG Day
    show PRG sad with vpunch
    play music Bittersweet
    "My eyes opened in a flash and my head shot up. There stood Aida no more than four feet in front of me. Immediately, my eyes shot to her stomach, which in only two days, had already swollen a considerable amount. Her breasts perched on top of her impressive belly like two boulders, each one slightly bigger than usual."
    MC "W-Whoa..."
    "I couldn't think of anything else to say. I think my head had blown a circuit."
    PRG "... I'm so sorry."
    "The tears continued to fall, dropping from the end of her chin down onto her enormous rack."
    MC "K-Kodama-san... for you to get this big in only two days, that's impossible no matter how you look at it."
    "As I finished speaking, the pieces suddenly fell into place. I immediately knew what was going on."
    MC "Kodama-san. Is this your growth factor?"
    "Aida looked at me through her sad eyes and after a moment's hesitation, nodded."
    show PRG unique
    PRG "Mhmm... I'm hyperfertile. As the nurses put it, I can get pregnant very easily. And that leads into what I wanted to tell you, Hotsure-san."
    MC "W-What's that?"
    PRG "I'm... I'm a mom now, Hotsure-san. And I really wanted you to be the father to my baby, but since you aren't..."
    PRG "W-We can't become anything more than friends."
    MC "Oh."
    "I hung my head lamely. As much as I wanted to be with Aida, I knew deep down that this was her decision, and I understood. She was the pregnant one, and it was her choice who she wanted around."
    PRG "I-I'm sorry, Hotsure-san... I'm so sorry."
    "She laid her hands on her belly and sighed, her gaze never breaking from me."
    MC "I understand."
    PRG "You do?"
    MC "Yes. Like you said, you're gonna be a mom, and it's your choice who you'd like to be around your kids."
    show PRG sad
    PRG "I-It's not that I don't want you around at all, Hotsure-san! I still want to see you, just... we can't be together in a romantic way. I'd still love to be friends though, if you'd still like to."
    "I looked up at her again and pursed my lips. I wanted to be with AIda more than anything, but I knew that, after this, it probably wasn't meant to be."
    MC "I'd still love to be friends too, and if there's anything I can do to help you, don't hesitate to ask. I'll always be here to help."
    show PRG neutral
    PRG "T-Thank you, Hotsure-san. I'll make sure to remember that."
    "Aida walked over to the bed and hugged me, her belly and swollen breasts pressing against my torso. As I pulled away from the hug, she leaned over and kissed me gently on the cheek."
    PRG "I'll see you in class, Hotsure-san."
    MC "Count on it."
    
    scene Dorm Exterior with fade
    "I let myself out of her dorm and began walking to my first class. Even though it didn't start for awhile, the room would be deserted so I could think."
    "I had a lot of thinking to do."
    jump daymenu

label PRG026b:
    $setPregnant()
    scene black with fade
    play sound AlarmClock
    pause 2
    scene Dorm Interior with fade
    play music Rain
    MCT "Urgh."
    "Leaning forward in my bed, I shut off my alarm clock and stretched, feeling my back pop and crack as I reached for the ceiling."
    MCT "God, I feel old."
    "I gently twisted my neck to crack it, stopping when I felt a searing pain coming from my head. Trying not to yelp, I stopped twisting and felt around. Nothing was out of the ordinary up there. Puzzled, I looked down and silently cursed."
    "My hair had grown so long that it had gotten caught in my armpit, and when I had tried to crack my neck, it started tugging away at my scalp. Wincing, I freed my hair and gave my neck another twist, this time accompanied by a satisfying pop."
    "After a quick shower and a run of the brush through my junglesque hair, I threw on my uniform and headed out the door."
    
    scene Campus Center with fade
    "It was almost time for first period, yet there was hardly a single student on the path to the classrooms. Even the main courtyard was almost entirely empty."

    scene Hallway with fade
    play music Schoolday
    "I soon found out why. The space around my usual morning classroom was congested with students, all trying to push through the door. I spotted an opening on the far side near the door and tried to snake my way through, but was instantly pushed out of the group."
    MC "Hey, could I get through? Unlike the rest of this crowd, I actually have class here."
    "One of the boys that pushed me turned around and sneered, an almost angry tone in his voice."
    Student "Yeah right, pal. You're just looking to get in there and get a good look at her, aren't you?"
    MC "Uh... who?"
    Student "Pshhh, as if you don't know!"
    "The boy turned around again and attempted to force his way through the growing crowd."
    "Nearby him, I saw a small gap open in the sea of people and dove for it, somehow crawling my way into the room with all of my limbs intact."
    
    scene Classroom with fade
    #[SCENE CHANGE CLASSROOM_DAY]
    show BE surprised at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    BE "Kei-chan! Are you alright?"
    "Honoka plowed through the other students and helped me to my feet, dusting off the front of my uniform."
    MC "I'm fine. What the hell is all of this?"
    BE "I don't even know! All of these students just showed up to see her. Who this mystery girl is, and why everyone wants to get a look at her, I have no idea."
    "Next to the door, Shiori stood guard, helplessly barking orders and trying to control the horde of people."
    show AE neutral-annoyed at Position(xpos=0.75, xanchor=0.5, yanchor=1.0), Transform(xzoom=-1) with dissolve
    AE "Everyone, disperse immediately."
    hide AE with dissolve
    "Over the roar of the crowd, the bell to signal that class would begin in one minute sounded. Students scattered in all directions, followed by Shiori hustling them along, leaving everyone in our classroom speechless."
    AE "Please make your way to your respective classrooms {i}without{/i} running! The school thanks you for your cooperation."
    show FMG angry at Position(xpos=0.85, xanchor=0.5, yanchor=1.0) with dissolve
    FMG "Dang, what the hell was that about?"
    show BBW neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    stop music
    "Across the room, Alice sat at her desk, nonchalantly scribbling in a notebook. She lifted her eyes when the students had disappeared and leaned down next to her, whispering at what appeared to be the floor tiles."
    "Crawling out from behind Alice's sizeable frame came..."
    show PRG unique with dissolve
    play music PRG
    extend " Aida."
    show FMG surprised
    FMG "W-Whoa!"
    BE "A-Ah... Hello, Kodama-san."
    PRG "H-Hi everyone. S-Sorry for causing all the commotion."
    hide FMG with dissolve
    hide BE with dissolve
    BBW "It wasn't your doing. Don't blame yourself for something you couldn't control, Kodama-san."
    PRG "I-I... Alright."
    PRG "T-There's something all of you need to hear."
    "She stopped and looked around at all of us, as if making sure we were all listening. Shiori emerged from the hallway, her expression changing the minute she saw Aida."
    PRG "E-Everyone, I'm..."
    extend " pregnant."
    show BE surprised at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) behind PRG with vpunch
    BE "Whoa! I mean... uhm... congrats, Kodama-san!"
    show AE surprised at Position(xpos=0.85, xanchor=0.5, yanchor=1.0) behind PRG, BBW with dissolve
    AE "Y-You're..."
    "I stared at Aida in complete bewilderment. Aida, the most quiet and reserved person I'd ever met, was pregnant. What was even more amazing was how quickly she had grown. I had no way of knowing when... it happened, but she had barely a trace of a belly last week, and now here she was, looking as if she were eight or nine months pregnant."
    PRG "This..."
    "Aida stopped, as if she had a lump in her throat. Surprisingly, Alice gave her a reassuring pat on the arm."
    BBW "Best to tell them now, as long as you have their undivided attention."
    PRG "This... is my growth factor."
    "Everyone gaped at her in total shock, before Tashi-sensei entered the room."
    hide BE with dissolve
    hide AE with dissolve
    hide BBW with dissolve
    hide PRG with dissolve
    show HR neutral with dissolve
    HR "Everyone to your seats, if you please. Just because someone has grown a few inches doesn't excuse unprofessionalism."
    "Going to my seat, I took one last glance back to Aida, who was trying to space herself the correct amount from her desk to accommodate her new belly."
    MCT "Who would've thought?"
    "I looked back once more to the demure, mousey girl. She was practically shaking in her seat as Nikumaru-san took the off glances at her belly. Out of all of the girls in this classroom, I would have never expected that the small woman who'd never uttered so much as a peep would have ended up pregnant at such a young age."
    "Regardless, I nodded and looked back to the front of the class as Tashi-sensei began his lecture. This isn't the first mind boggling thing to happen in this place, and based purely on the fact that Kodoma-san's belly was as flat as a board just the night prior..."
    "I doubt it will be the last."
    jump daymenu

label PRG026b_BE:
    scene Hallway with fade
    "After class, I decided to avoid getting entangled in the Q&A that was surrounding Aida's desk, and made my way down the hall."
    BE "HEEEEEYYY! KEI-CHAN!!"
    "Honoka came running after me, both arms wrapped around her chest to avoid giving herself a black eye."
    show BE happy with dissolve
    BE "Trying to avoid the craziness in there?"
    MC "Yeah, something like that. Crowds of people were never my thing."
    show BE neutral
    BE "I'm sure no one enjoys being smothered by people, especially not that many. But hey, Kodama-san, am I right?"
    MC "What do you mean?"
    show BE surprised
    BE "I mean, look at her! She was gone for only a handful of days, and if we assume that she was actually diagnosed with the babies on the first day, that means that she grew that much in only two to three days!"
    show BE angry
    BE "I mean, at the very least, we know what her factor is now."
    MC "You've got a point there. But if getting pregnant was the key to get her growth factor moving, then maybe a tiny jumpstart like that is to be expected."
    show BE neutral
    BE "Uhh... not sure that tiny is the right word in this case, Kei-chan. But that's a good thought."
    show BE surprised
    BE "Ooh! Do you think she'd let me be Auntie Honoka! I'd be a good aunt, I know I would! I wonder if she has any sisters..."
    MC "You could ask, but I'm not sure if now is the right time. She's probably dealing with a lot right now. Not to mention that her body changed so much in such a short period."
    show BE aroused
    BE "Ha! Imagine this body if I got knocked up. Big ol' belly and all. Hey, when my milk came in, I'd probably end up flooding the place."
    "Suddenly, the roar of the crowd died down from the room behind us. We spun around to see Aida leave the room first, followed by the rest of the class. Behind them, I could've sworn I caught a glimpse of Tashi-sensei shaking his head. All of the students broke apart from the crowd and went their separate ways, but Aida came directly towards us."
    show BE happy at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    BE "Hey Kodama-san!"
    show PRG sad at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    PRG "O-Oh... hey guys."
    BE "Congrats, by the way. I'm sure you've already heard that a couple of times today."
    show PRG neutral
    PRG "Just a few times, but thank you, Inoue-san."
    show BE neutral
    BE "Did you come up with any names yet? How about like, like... something really cool, like..."
    show PRG happy
    PRG "No, not yet. I'm thinking I may just wait until they're actually born, and come up with something on the spot."
    show BE surprised
    BE "Wait... they?! As in, more than one?!"
    show PRG unique
    PRG "See... I really don't know how many I'm having. When I went to the infirmary the other day, they said it was too soon to tell, but they did say that me having more than one is quite likely. Of course, with how big I am already..."
    show BE neutral
    BE "Well, if you ever need an emergency babysitter, you know where to find me!"
    show PRG neutral
    PRG "I'll keep that in mind, thanks Inoue-san."
    "The two of them went on, while I sort of stood there and spaced out. The idea of Honoka lactating was both an interesting thought, and a slightly terrifying one, especially the idea of drowning in milk."
    BE "You in, Kei-chan?"
    MC "Uh... wha?"
    BE "Kodama-san asked if you and I wanted to have lunch with her. Are you in?"
    MC "Oh! Yeah, of course!"
    jump daymenu

label PRG026b_FMG:
    "The minute the bell rang, the whole class crowded around Aida's desk, asking her question after question with a congratulations thrown in here and there. Off to one side, Akira noticeably hung back, taking awkward glances at Aida."
    MC "You alright?"
    show FMG surprised with dissolve
    FMG "Huh?! Oh... yeah. I'm good."
    MC "You know, body language can say a lot about how a person is feeling, Akira."
    show FMG sad
    FMG "Look, I..."
    extend " okay. Meet me in the cafeteria for lunch later. I'll fill you in."
    MC "You got it."
    hide FMG with dissolve
    "Akira smiled weakly and spun around to leave. Even her pace, which was pretty much one step below a run, gave away her feelings."

    scene Cafeteria with fade
    "After barely entering the cafeteria, I spotted Akira sitting at a table near the wall, unenthusiastically picking at a bowl of rice. I hurried through the line as quick as I could, and took the seat across from Akira."
    MC "Yo, Akira!"
    show FMG neutral
    FMG "Oh, hey."
    MC "Alright, I know you and I both aren't people that beat around the bush, so what's eating you?"
    "Akira sighed before finally looking up at me."
    show FMG sad
    FMG "That obvious, huh?"
    MC "Yeah, more than just a little."
    show FMG neutral
    FMG "Augh... alright. Pregnancy and childbirth just kind of freaks me out, alright?"
    "I sat and politely listened, choosing the high road and not butting in until she had finished speaking."
    FMG "It's just, the very idea of it gives me chills. Don't get me wrong, it's cool that Kodama-san is having kids and all that, and yeah, I'm happy for her. But at the same time... I don't think I could ever see myself going through that myself."
    MC "Really? No kids?"
    FMG "Maybe I'd adopt someday. But the idea of pushing something that big out of me is just crazy. And, if my stomach grew that huge, I couldn't lift like I do anymore."
    FMG "I've heard of what pregnancy does to your body, and I don't want anything to do with that. The pain alone was a big turn off for me, but when I thought of how having a kid can mess up your body so much, it totally pushed me away from it."
    FMG "And don't even think about mentioning the epidural shots. I've heard that some women still feel the pain from those even years after childbirth. Yeah, no thanks. Screw that."
    "I hadn't even considered how a woman's body could change after childbirth, but what Akira said made sense. And, given her strong opinions on needles, no wonder she didn't want to have kids."
    MC "I guess I've never thought about all that. As a guy, it isn't really something that comes up often."
    FMG "Well, as a girl, the idea does pop into my head from time to time, and I shut it down any time it does."
    FMG "But, thanks for asking, dude. Nice to know that someone's looking out for my feelings. You're like a... hairy guardian angel, or something."
    MC "Heh. I'll add that to the list of aliases that I have."
    "Akira began digging more heartily into her rice, and even though she had finished eating long before I did, she stayed and chatted with me until I had finished."
    jump daymenu

label PRG027:
    $setSize(3)
    $setTimeFlag("size3")
    $setProgress("PRG", "PRG028")
    #[SCENE CAMPUSCENTER_DAY]
    scene Campus Center with fade
    play music Busy
    MCT "Music is best when it makes you go deaf later."
    "I was walking to my first period class with one of my favorite morning jams blasting through my earbuds. Something about tuning out the world for a little while when you're tired is just special."
    "Out of nowhere, my text notification beeped in my ears, making me jump so suddenly, that my poor, innocent cup of coffee dropped and splattered on the worn walking path."
    "Doing my best not to start blasting obscenities in public, I pulled my phone from my pocket and looked down at the screen."
    PRGCell "Hey. Are you busy right now?"
    "I checked my phone's clock. I had maybe 5 minutes at best until class started. If I helped Aida, I'd be late to class for sure."
    menu:
        "No, why?": #(PRG.AFFECTION -2)
            jump PRG027_c1_1
        "I'm on my way to class, but I have time.": #(PRG.AFFECTION +3)
            jump PRG027_c1_2

label PRG027_c1_1:
    MC "No, why?"
    "Another text came through almost immediately."
    PRGCell "I need help with something. Can you come to my dorm?"
    $setAffection("PRG", -2)
    "I began typing another message. Even with having a class to get to, helping Aida with her pregnancy was my top priority now."
    MC "Be right there."
    "I slid my headphones into my pocket and sped walked back to the dorms."
    jump PRG027_c1_after

label PRG027_c1_2:
    MC "I'm on my way to class, but I have time."
    "Another message came through almost immediately."
    $setAffection("PRG", 3)
    PRGCell "Are you sure? I don't want to get you in trouble."
    "I began walking back to the dorms while typing at the same time."
    MC "Don't worry about it. I'll be there in a sec!"
    "I shoved my phone in my pocket and unplugged my headphones. I felt my phone buzz against my thigh as it bounced around in my pocket, but I didn't bother to check. I'd see her soon enough."
    jump PRG027_c1_after

label PRG027_c1_after:
    scene Dorm Exterior with fade
    "I had barely knocked when I heard Aida call from inside her dorm. She sounded hurried and a little panicked."
    PRG "H-Hotsure-san?"
    MC "Yeah, Kodama-san. It's me."
    PRG "C-Come in!"
    
    scene Dorm PRG Day with fade
    "I opened the door with a creak and was surprised by the lack of Aida in the room."
    MC "Kodama-san? Where are you?"
    PRG "I-I'm in the bathroom, but don't come in!"
    "I look around, trying to think of anything that she could need my help with. Looking around her and Alice's room, everything seemed normal, as far as I could tell anyway."
    PRG "T-Thank you for coming."
    show PRG neutral with dissolve
    "I turned to see Aida standing in the doorway to her bathroom. My eyes flew to her stomach immediately, which I still wasn't completely used to yet. It was amazing how natural it seemed to fit on her, as if she had already been accustomed to having something that large hanging from her torso. Her shirt, in turn, looked incredibly strained."
    MC "Good morning miss, how may I be of assistance?"
    "I bowed deeply and with grandeur as Aida's face lit up with soft giggles. Her face stiffened again as she looked away from me."
    show PRG unique
    PRG "T-This is a little embarrassing."
    MC "It's alright. Whatever you need help with, I'm there!"
    PRG "O-Okay."
    "Aida went to her desk where a large stack of books sat. Comprised of several textbooks, the tower looked like it could fall over at any second."
    PRG "Alice helped me bring some of these books from the library yesterday so I could catch up on the class I missed while I was gone. I told the librarian I'd have them back today, but I... I can't lift the stack myself. My... belly gets in the way."
    MC "Oh, is that all? You got it!"
    "I picked up all of the books with no problem. Sure, they were a little heavy, but not unbearable by any means."
    show PRG happy
    PRG "Yay! Thank you so much!"
    "Aida smiled as she threw a couple of her notebooks into her bag and zipped it up. She slung the bag over her shoulder before joining me by the door."
    PRG "All ready!"
    hide PRG with dissolve

    scene Dorm Exterior with fade
    "I nodded at her as she led the way out of her dorm, locking the door behind us. Once we were outside, we picked up the pace a bit, heading straight for the library."
    MC "Are you all caught up from your time off then? Looks like you had a lot of material to cover in one night."
    show PRG neutral with dissolve
    PRG "It wasn't too tough. I'm a fairly quick note taker."
    MC "Heh, good for you."
    PRG "All it is is just writing down the important pieces of the lecture and leaving the stuff that doesn't matter as much. It isn't hard once you get the hang of it."
    MC "Yeah, I'm sure you're right. I just don't enjoy taking notes."
    PRG "Ok. How many pages of notes do you have after one class period? Give or take."
    MC "Um... maybe a third of one page?"
    show PRG surprised
    PRG "A-A third?!"
    MC "Why? How many do you have?"
    PRG "G-Generally around four pages if it's a more in depth topic! For something that's more simple, I'm lucky if I have two pages."
    MC "So at the absolute minimum, you're taking approximately six times the amount of notes that I am."
    show PRG unique
    PRG "W-Well, I take a lot of notes. Tashi-sensei recommends having at least a page and a half of notes every day."
    MC "Eh, the way I see it, recommendations are a lot like speed limits. They tell you what you're supposed to do, but no one ever follows them exactly, right?"
    PRG "I-I wouldn't know. I don't have a driver's license."
    MC "Oh really? Are you more of a “ride the train” type of person?"
    PRG "N-No. I always thought that it'd be really scary. Especially in heavy traffic. I feel like I'd crack under the pressure."
    MC "It can be a little hard to deal with, but once you get the hang of it, driving in traffic isn't too difficult. It's all about using common sense."
    show PRG neutral
    PRG "Hotsure-san?"
    MC "Oi?"
    PRG "Y-You realize you took this conversation from note taking to driving in traffic, right?"
    MC "Eh, tis the miracle of random tangents, They can take you anywhere, anytime."

    scene Hallway with fade
    "Aida chuckled at me as we neared the library. We opened the door quietly and deposited the books in the library's returned books bin and hurried toward our class, which we were now almost 20 minutes late for."
    show PRG neutral with dissolve
    PRG "I-I hope we don't get in too much trouble."
    MC "I don't think we will. If anything, Matsumoto-san will be more irritated with us than Tashi-sensei will."
    MCT "Actually, that thought is more terrifying than Tashi-sensei could ever be."
    MC "Actually... maybe we could just..."
    extend " skip class?"
    show PRG surprised
    "Aida stopped and stared at me, her eyes wide with a combined look of wonder and fear."
    PRG "W-What?!  Are you serious, Hotsure-san? I've never played hooky in my life!"
    MC "As they say, there's a first time for everything. What do you say?"
    if getAffection("PRG") <= 10:
        show PRG sad
        PRG "I-I can't, Hotsure-san. I... I've already missed too much class."
        MC "Ah. Alright, best to go then."
        hide PRG with dissolve
        "I followed behind Aida, hoping that my gut feeling was right about Tashi-sensei not being upset with us."
        "I was right about Shiori being upset with us. I was wrong about Tashi-sensei not being upset with us."
        
        scene Dorm Exterior with fade
        "After class that day, Aida and I made our walk back to the dorms together in silence."
        show PRG unique
        MC "Hey, sorry I got you into trouble."
        PRG "I-It's alright. It was bound to happen anyway. Sorry for making you late."
        MC "If I had to choose carrying books for you or sitting in class, I'm taking the books ten times out of ten!"
        show PRG neutral
        "Aida laughed as we neared the dorms, which after class today, looked heavenly in the afternoon sun."
        PRG "I'll... I'll see you tomorrow, Hotsure-san."
        MC "Alright, take it easy tonight, Aid- I mean Kodama-san."
        PRG "Actually... can you call me Aida from now on? I-I kind of prefer it."
        MC "Aida it is then. You can call me Keisuke, if you want."
        PRG "I will. Bye."
        MC "See you tomorrow!"
    else:
        PRG "I..."
        show PRG neutral
        PRG "Okay. Let's go."
        MC "Great! How much longer until this class ends?"
        PRG "Uhm... about half an hour, give or take a little. Counting the break afterwards, we probably have about 45 minutes."
        MC "Okay. I've got it."
        "I led Aida down multiple corridors and through a few different doorways until we emerged in the garden."
        
        scene School Planter with fade
        show PRG aroused with dissolve
        PRG "T-The garden? Why are we here?"
        MC "Well, I figured after the stress that you've probably had over the last few days, relaxing in the calm garden for a little while could be therapeutic."
        PRG "That... actually does sound really nice."
        "Aida and I walked through until we found a spot under a large, shaded tree. Luckily, the bushes next to the tree obscured vision at the base of it, hiding us from any teacher's gaze."
        "As I went to sit, I looked over and saw Aida with her hand against the tree. She was trying to lower herself onto the ground to sit, but couldn't quite catch her balance. I went to her side and offered her my hand."
        MC "Here. Use me to help you lower yourself."
        show PRG neutral
        PRG "T-Thank you."
        "She took my hand and brought herself gently to the ground. I took a seat next to her and listened to the soothing morning breeze blow through the trees."
        PRG "It's funny..."
        MC "Hmm?"
        PRG "Before I came here, I wouldn't have even thought of doing something like this. Skipping class, I mean."
        MC "Really? I used to do it from time to time. This is my first time doing it here though."
        PRG "That's probably for the best. Matsumoto-san probably wouldn't tolerate people skipping class. Especially in a consistent fashion."
        MC "True. I'll save it for important times."
        PRG "Good idea. I-I'd hate to see you get into trouble."
        MC "You and me both. I doubt that skipping is something they handle lightly here."
        "Aida nodded before leaning her head against the tree trunk and inhaling deeply, closing her eyes as she did. I listened to the morning air blowing between the tree branches and bushes, the leaves rustling this way and that with the swells of the wind."
        "In no time, the bell was rung to signal the end of the first class period. Aida put her arm on the tree behind her and shakily got to her feet. I reached out my hand to help, but she shook her head."
        PRG "I-I'm fine, thanks. Balancing is just a little tricky. I'm not used to the extra weight yet."
        MC "You'll get there, don't worry."
        PRG "I-I know I will. I'm going to head over to my next class. Are you coming too, Hotsure-san?"
        MC "I'll catch up with you later, Kodama-san. I'm going to go grab a coffee or something quick."
        MCT "After losing my first one this morning."
        PRG "Oh. Okay, Hotsure-san. I'll see you later."
        MC "Okay, Kodama-san. See ya."
        hide PRG with dissolve
        "I was nearly at the door to leave the garden when Aida hurried back over to me."
        show PRG neutral with dissolve
        PRG "Oh, and Hotsure-san?"
        MC "Yeah?"
        PRG "Can you... call me Aida?"
        MC "Hah, of course! And you can call me Keisuke then, if you'd like."
        show PRG happy
        PRG "O-Okay. Sounds good!"
        MC "Alright, I'll see you later, Aida."
        PRG "Y-Yeah, see you, Keisuke!"
    jump daymenu

label PRG028:
    $setProgress("PRG", "PRG029")
    scene Campus Center with fade
    play music Sunset
    #[SCENE- CAMPUS CENTER-DAY]
    show PRG neutral with dissolve
    PRG "What would you think if I made fried rice today?"
    MC "I'd commend you for the delicious, yet simple rice, but also suggest that you try making something more complex."
    PRG "I-I'm glad you think so highly of my skills in the kitchen! A-And who said that the rice would be simple?"
    "I let loose a wry chuckle. I was on my way to the cooking classroom with Aida. She hadn't been in the kitchen since she'd gotten pregnant, and she had decided to make today her official return to the kitchen. I, being the kind and caring friend that I was, agreed to tag along and taste whatever she fancied cooking."
    "Tucked under Aida's arm was her trusty recipe book, which had seen better days. It's pages were torn in every which way, yet somehow, she had no trouble deciphering it's contents."
    MC "So, how many recipes do you have in that notebook anyway?"
    PRG "Probably around 40, give or take a few. The majority of them haven't been put into use yet, so I just save them for whenever inspiration strikes."
    MC "Is it just recipes? It looks like there's way more than 40 pages used up."
    PRG "N-Not necessarily. I also keep a list of every spice or herb I use, along with what type of flavor it has, and what it works best with."
    "She flipped open her book and leafed through the pages until she came across one particularly worn page near the end."
    PRG "See? T-This helps me keep everything straight in the kitchen. Without this book, I don't know what I'd do."
    "Across the sheet was easily 50 individual herbs and spices, each one with a brief description, and a small list of meats, vegetables, and other spices that paired well with it. All of the ingredients were separated by type, as in, spicy goes with spicy, woodsy or mint type flavors went together, and so on."
    MC "Wow. I'm sure anyone could cook something incredible if they had access to this book."
    PRG "They could. That's why I never go anywhere without it. If I lost this, I'd have my work cut out for me."

    scene Hallway with fade
    show PRG neutral with dissolve
    PRG "The only person I've ever allowed to look through this book besides you is Sakura. With how much she helps me in the kitchen, I wouldn't feel right keeping all of this work from her."
    MC "Damn, I must be pretty special to have access to such important documents!"
    PRG "Keisuke, it's a notebook of my ideas, not some sort of government file."
    MC "Well, it carries the same value, no?"
    "Aida giggled as she led the way into the cooking classroom."

    scene Cooking Classroom with fade
    #[SCENE CHANGE - CLASSROOM_DAY]
    "Everything looked just as it had the last time Aida and I had been here. The countertops were clean and freshly polished, and every utensil was put neatly in it's spot."
    show PRG neutral with dissolve
    MC "So, what's on the menu today, chef?"
    PRG "I-I feel like making something a bit more simple today, as a warm up. Maybe lamb chops and a small salad?"
    MC "Sounds good. Need any help?"
    PRG "I-I'll call you over if I need you."
    "I nodded and sat down in a spare chair across the room. I had pulled my phone from my pocket and was browsing the internet when I heard a frustrated sigh. Looking up, I saw Aida bending over and peering into the pantry. Her bend accentuated the curves of her hips and butt, pulling her skirt neatly across."
    MC "Everything alright?"
    PRG "I-It's fine. All of the ingredients are all mixed up in the cabinet. It'll make the whole process a little slower."
    MC "I'm not in a rush or anything, so don't feel like you need to hurry."
    "Aida leaned back over and began pulling several bottles from the cabinet and setting them on the counter, followed by the occasional glance at her notebook."
    show PRG angry
    PRG "I just don't understand why they can't keep everything in the same places. It's not that hard."
    MC "I suppose everyone has their own system of organization that they follow, and odds are it won't mix well with the next person's system."
    show PRG unique
    PRG "I-I know. It's just frustrating."
    "Aida reached into the nearby fridge and pulled out some lamb chops, freshly cut and ready for the oven."
    MC "Did you plan ahead for this?"
    show PRG aroused
    PRG "What do you mean?"
    MC "I mean that you just happened to find some thawed lamb chops just hanging out in the fridge. I'm sure that the rest of the cooking club wouldn't just leave those there."
    "Aida did her best to hide her smile, but failed miserably."
    PRG "Y-Yeah, I came here yesterday after class and took these out to thaw. I wanted to make you something special, but I obviously had to thaw these beforehand. I was just hoping that you would be okay with my suggestion, otherwise, these would've gone to waste."
    MC "Well, I certainly am surprised! And I can't wait to try them, so let's get these chops cooking!"
    show PRG happy
    PRG "Yes sir!"
    hide PRG with dissolve
    "I helped Aida make the salad while she handled the lamb chops. Thankfully, all I had to do for the salad was chop some lettuce, cucumber, and carrots into a bowl, and then give it a mix, so even I couldn't screw this up."
    MC "Salad's all do-"
    PRG "W-Where is it?!"
    MC "Eh?"
    "I spun around to see Aida bending over again, this time she was searching through the fridge, albeit much more frantically than when she'd been looking through the cabinet."
    MC "Where is what?"
    show PRG angry with dissolve
    PRG "My lamb sauce. I threw some together last night while the chops were thawing on the counter, but now the sauce isn't here. The lamb chops will be really dry without it."
    "Aida walked over and threw herself onto my chair, running her hands through her hair."
    PRG "I-I just don't get it. Where is the lamb sauce?"
    menu:
        "Let me look in the fridge.": #(PRG.AFFECTION -4)
            jump PRG028_c1_1
        "We can make some more.": #(PRG.AFFECTION +3)
            jump PRG028_c1_2

label PRG028_c1_1:
    MC "Let me take a look once."
    "I bent over and looked into the fridge. The first thing that hit me was how overstocked the fridge was, with extra bottles of nearly everything filling the door, and containers galore filled with uncooked food."
    MC "What kind of container was it in?"
    show PRG unique
    PRG "L-Like a glassware type thing. It had a red cover."
    "I began pulling out cartons and containers from the front of the fridge and setting them on the floor. Nearing the back of the fridge, I unstacked some more food, and underneath it all was a glass bowl with a red cover, with the name “Aida” written on the top."
    MC "I think I've got it!"
    "I held my prize up happily and showed it to Aida. Rather than getting all excited, like she usually would, she looked at it and smiled weakly."
    PRG "T-Thanks, Keisuke."
    MC "So, when do we add this to the chops?"
    PRG "Actually... I don't really feel like cooking anymore today..."
    MC "W-Why not?"
    PRG "I-I shouldn't be making amateur mistakes like that. I feel like... since I took so much time off, that I'm not going to be good enough to compete anymore. I'm thinking..."
    extend " I may quit the cooking club."
    MC "Aida..."
    show PRG sad
    PRG "It's not just losing the sauce that brought this on. It's kind of been everything lately. My classes, taking so much time off, me getting pregnant. Just everything!"
    $setAffection("PRG", -4)
    "Aida burst into tears, throwing her head into her hands and sobbing heavily. I stood there stunned. For Aida to want to give up her favorite hobby, she must've been truly upset."
    "Sliding a chair over, I sat down next to Aida and threw my arm over her, rubbing her shoulders lightly."
    PRG "I-I-I don't know what to do! I don't want to let Sakura-san down! But, I don't know if I'll be able to cook like I used to again!"
    MC "Why wouldn't you be able to?"
    PRG "I-I took so much time off. Before I got pregnant, I was practicing my cooking every day. But ever since then, I haven't cooked anything. I..."
    MC "I'll help you."
    PRG "W-What?"
    MC "I'm going to help you get back into it, and we'll get you back into your element."
    PRG "B-But how?"
    MC "We can come here every day after our classes. You can make something different each day, and I'll help you however I can. Eventually, you'll start to pick everything back up again."
    MCT "Shouldn't be too difficult. I mean, how out of practice can a person get? Especially after only a week or so."
    show PRG neutral
    PRG "Would... Would you do that?"
    MC "Of course I would. I know how much you adore cooking and for you to have to step away from something you love just because you lost your touch is unthinkable."
    PRG "O-Okay. Thank you, Keisuke. W-We wouldn't have to practice every single day together, but every so often, we could. Doing it everyday wouldn't leave either of us with much free time."
    MC "Alright. Now, let's get cooking! We have lamb to make!"
    PRG "Yes, we do!"
    "Soon, Aida had the lamb chops plated, with her sauce on top. My sad excuse for a salad sat next to it, looking much less extravagant."
    jump PRG028_c1_after

label PRG028_c1_2:
    "In response, I pulled out my phone and went to my internet browser. I did a quick search and pulled up the first recipe I could find for lamb sauce."
    show PRG unique
    PRG "W-What're you doing?"
    MC "Making some more lamb sauce."
    PRG "Keisuke... It's fine. I can just make some more myself."
    MC "Nope! You offered to cook all of this for me today! On top of that, you've made me so many other fantastic meals. It's high time that I repay the favor. Now..."
    extend " uh, where do I start?"
    show PRG neutral
    "Aida smiled and shook her head, rising from her chair and grabbing a recipe book from a nearby counter."
    $setAffection("PRG", 3)
    PRG "Don't follow online guides. T-They tend to never turn out quite right."
    "Aida took two cloves of garlic and began to chop them up into fine pieces. She instructed me to pat the lamb until it was dry and dust it with salt and pepper, which I did."
    "From the cupboard below the countertop, Aida pulled out a heavy cast iron skillet and set it on the stove adding just a bit of olive oil before turning it to medium-high heat. Once the pan had reached a warm enough temperature, Aida took the lamb chops and seared them for about five minutes before pulling them from the pan and placing them on two plates."
    "As I watched her work, she told me to measure out some rosemary, lemon juice, butter, and chicken stock."
    PRG "I'm going to call out what I need. Pass the ingredients to me in the order I tell you, okay?"
    MC "Yes, chef!"
    PRG "Okay, garlic first!"
    "I passed her the small cup of garlic, which she added to the pan with a tantalizing sizzle."
    PRG "Next. give me rosemary and lemon juice."
    "Those were added, as well."
    PRG "Chicken stock!"
    "I handed her the cup of stock, which she poured in slowly. She turned the dial on the stove to high and began to stir, deglazing the pan as she went, until juicy bits of lamb floated in the sauce."
    PRG "Alright, now add the butter slowly."
    "I grabbed the butter and began adding it into the pan bit by bit. Meanwhile, Aida had taken a whisk and was slowly stirring the butter into the pan. The smell was heavenly."
    PRG "Could you pass me an oven mitt?"
    "I handed her one and with it, she lifted the pan over the two plates and gently poured the sauce over the lamb. I busied myself with setting silverware on the countertop, until the lamb was finally ready. Aida took the two plates and set one in front of me, and then one for herself. She grabbed my extravagant bowl of salad, and set that next to our plates, completing our meal."
    jump PRG028_c1_after

label PRG028_c1_after:
    PRG "Alright, tell me what you think."
    "I picked up a chop by the bone and lifted it to my mouth, taking a small bite. The taste was both sweet and savory, with the rosemary accenting the juiciness of the lamb. The sear was perfect and the meat itself was amazingly tender."
    MC "It's... Ohh..."
    PRG "Is... that a good oh?"
    "All I could do was nod. Aida reached for the salad and pulled up a smaller bowl and some tongs."
    PRG "Let me try what you made now. What do you call this dish?"
    MC "Uh... cucumbers, lettuce, and carrots thrown together in a bowl? Possibly with some dressing?"
    show PRG happy
    "Aida giggled and produced a bottle of dressing from the fridge. She took what she wanted from the salad bowl before dousing it in dressing and scooping some into her mouth."
    PRG "D-Delectable."
    MC "Delectable, you say?"
    PRG "Y-Yeah. I've heard Nikumaru-san use that word sometimes."
    MC "It does sound like her. Speaking of, what's the status with you and working for her?"
    show PRG neutral
    if getFlag("PRG020_c1_1"):
        PRG "Well, she told me the other day that she's looking for a new assistant. She said it wasn't anything personal, just that she didn't want me worrying about helping her when I should be focused on being a mom."
    else:
        PRG "I asked her the other day if I could have my job back. She told me that she wanted me to focus on my pregnancy, and not worry about her."
    MC "It makes sense, I suppose. You should be taking it easy throughout this process. "
    PRG "I know. It's just hard because I don't really feel any different. But, then I look down. I... I can't even see my feet anymore!"
    MC "Even so, just because you're feeling good doesn't mean you should push it."
    PRG "I know. Thanks, Keisuke."
    "After we had finished, I took the liberty of doing the dishes, while Aida relaxed, but not before she corrected me when I tried to put soap in the cast iron pan. Apparently that's a big no-no."
    jump daymenu

label PRG029:
    "This marks the current end of Aida's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance
    
label PRGend_nofather:
    "This marks the current end of Aida's route if you are not the father of her children."
    "Her story in this scenario will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance