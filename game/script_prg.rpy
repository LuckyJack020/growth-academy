define PRG = Character('Kodama', color="#FF3399", what_prefix='{size=-6}', what_suffix='{/size}')
define Sakura = Character('Sakura', color="#FF3399")
define Announcer = Character('Announcer', color="#C0C0C0")
define fade = Fade(0.5, 0.0, 0.5)

image PRG neutral = DynamicImage("Graphics/PRG/[globalsize]/neutral.png")
image PRG happy = DynamicImage("Graphics/PRG/[globalsize]/happy.png")
image PRG sad = DynamicImage("Graphics/PRG/[globalsize]/sad.png")
image PRG surprised = DynamicImage("Graphics/PRG/[globalsize]/surprised.png")
image PRG angry = DynamicImage("Graphics/PRG/[globalsize]/angry.png")
image PRG aroused = DynamicImage("Graphics/PRG/[globalsize]/aroused.png")
image PRG unique = DynamicImage("Graphics/PRG/[globalsize]/unique.png")

image Dorm PRG Day = "Graphics/ui/bg/PRGdorm_day.png"
image Dorm PRG Eve = "Graphics/ui/bg/PRGdorm_eve.png"

init 2 python:    
    #Core
    eventlibrary['PRG001'] = {"name": "A Bun Tasting", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,             "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "PRG003", "obsflags": [],            "conditions": []}
    eventlibrary['PRG003'] = {"name": "An Inviting Aroma", "girls": ["PRG"], "type": EventTypeEnum.CORE,                "location": "classroom",        "priority": PrioEnum.NONE, "next": "PRG008", "obsflags": [],            "conditions": []}
    eventlibrary['PRG008'] = {"name": "Cups and Measurements", "girls": ["PRG"], "type": EventTypeEnum.CORE,            "location": "classroom",        "priority": PrioEnum.NONE, "next": "PRG009", "obsflags": [],            "conditions": []}
    eventlibrary['PRG009'] = {"name": "Handling with Change", "girls": ["PRG"], "type": EventTypeEnum.CORE,             "location": "campuscenter",     "priority": PrioEnum.NONE, "next": "PRG012", "obsflags": [],            "conditions": [[ConditionEnum.TIMEFLAG, "testday"]]}
    eventlibrary['PRG012'] = {"name": "Archetypes", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                 "location": "classroom",        "priority": PrioEnum.NONE, "next": "PRG013", "obsflags": [],            "conditions": []}
    eventlibrary['PRG013'] = {"name": "Competitive Spirit", "girls": ["PRG"],"type": EventTypeEnum.CORE,                "location": "classroom",        "priority": PrioEnum.NONE, "next": "PRG014", "obsflags": [],            "conditions": []}
    eventlibrary['PRG014'] = {"name": "Cozy Lunch Time", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "PRG015", "obsflags": [],            "conditions": []}
    eventlibrary['PRG015'] = {"name": "Nurturing", "girls": ["PRG"], "type": EventTypeEnum.CORE,                        "location": "dormBBW",          "priority": PrioEnum.NONE, "next": "PRG020", "obsflags": [],            "conditions": []}
    eventlibrary['PRG020'] = {"name": "Aida end", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "library",          "priority": PrioEnum.NONE, "next": "", "obsflags": [],                  "conditions": []}

    #Optional
    eventlibrary['PRG001b'] = {"name": "Tongue Twister", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                  "location": "schoolexterior",   "priority": PrioEnum.NONE, "next": "", "obsflags": ["testday"],     "conditions": []}
    eventlibrary['PRG004'] = {"name": "Mother Nature", "girls": ["PRG", "FMG"], "type": EventTypeEnum.OPTIONAL,             "location": "track",            "priority": PrioEnum.NONE, "next": "", "obsflags": [],              "conditions": []}
    eventlibrary['PRG006'] = {"name": "Double Stacked", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                   "location": "campuscenter",     "priority": PrioEnum.NONE, "next": "", "obsflags": [],              "conditions": []}
    eventlibrary['PRG007'] = {"name": "A (Soft) Wall to Hide Behind", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,     "location": "cafeteria",        "priority": PrioEnum.NONE, "next": "", "obsflags": [],              "conditions": []}
    eventlibrary['PRG011'] = {"name": "Homerun!", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                         "location": "classroom",        "priority": PrioEnum.NONE, "next": "", "obsflags": [],              "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['PRG019'] = {"name": "A Small Touchup", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                  "location": "campuscenter",     "priority": PrioEnum.NONE, "next": "", "obsflags": [],              "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    
    eventlibrary['PRG005'] = {"name": "Hold on Tight", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,                "location": "auditorium",       "priority": PrioEnum.GIRL, "obsflags": ["aftertest"],               "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}    
    eventlibrary['PRG010'] = {"name": "Rapidly Curvy", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,                "location": "cookingclassroom", "priority": PrioEnum.GIRL, "obsflags": ["aftersize2"],              "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}

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
    PRG "Oh...I hoped no one had noticed. Please, don't concern yourself over it."
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
    "I felt hungrier than usual today, so I stopped by the cafeteria for an extra snack.  I had just finished my red bean bun when I spied Aida coming in the door near where I was sitting."
    show PRG neutral at Position(xpos=0.65) with dissolve
    MC "Hi there, Kodama-san!"
    PRG "Oh!  Ah, h-hello Hotsure-san."
    MC "How are you today?"
    PRG "Oh, I'm fine. Just getting Alice-san's between-meal snack."
    MC "I thought you were cooking for her?"
    PRG "Meals, yes, but for snacks she usually prefers something sweet and pre-made. I'm supposed to get a bunch of sweets so she can figure out what she likes..."
    "I used a tissue to wipe up any residual crumbs and threw my trash in the can."
    MC "Well, I'll wait in line with you, how about?  Help it go quicker."
    show PRG happy
    PRG "Oh, really? W-well sure, that'd be wonderful!"
    show PRG neutral
    "We spent a few minutes in line, making small talk and getting to know each other better."
    "When we finally got up to the counter, Aida ordered several bean paste buns and a few jelly rolls. Her large bag of pastries in hand, we set out into the cafeteria seating, looking for Alice."
    BBW "Here, Kodama-san."
    PRG "Ah! C-coming!"
    show BBW neutral at Position(xpos=0.25) with dissolve
    "I followed Aida over to the table Alice was sitting at, a small picnic cloth spread over the table and actual silverware set in front of her. Aida quickle set to work opening each of the packaged sweets and setting them out on the picnic cloth in front of Alice."
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
            MC "I, uh, I should get on my homework.  I'll see you around, okay Kodama-san?  Alice-san, nice to see you too."
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
    "I followed the scent to the end of the hallway, a small room in the corner opposite the stairs beckoning me with its open door. I peeked inside, and who should I find at the home ec. stations but mousy, unassuming Aida."
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
    MC "...Whta's she doing that she needs all that help?"
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
    MC "Yeah, and she... That didn't look like an exercize run..."
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
    PRG "Who...?  Oh! H-hello, Hotsure-san."
    MC "Hello. Those boxes seem pretty heavy, would you like me to take some?"
    PRG "Oh, n-no thanks, I've... I've got it."
    MC "Are you sure?  I don't mind."
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
    "I reached up and grabbed the top half of the pile from her.  She didn't say anything to stop me, and the embarrassed smile let me know he wasn't against it."
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
    "We finally arrived at the women's dorms, Aida slightly red in the face from the exertion.  I knocked on the door for her, and Alice answered after not to long of wait."
    show BBW neutral at Position(xpos=0.75) with dissolve
    BBW "Hm?"
    show BBW happy
    BBW "Oh! Wonderful, they've arrived!"
    "Alice started taking the boxes from Aida, the two of them setting boxes on a large kitchen table in the middle of the room. Having not been invited, I waited patiently outside the open door."
    "After they had gotten all the boxes, Alice started in on opening them, using a boxcutter to slit the tape with fluid, well-practiced motions."
    "Aida wandered over to the door as Alice began casting packing paper and bubble wrap to the floor, looking behind her at the growing mess she'd undoubtedly have to clean up. She looked up at me, leaning against the half-closed door."
    hide BBW happy with dissolve
    PRG "...Good-bye, Hotsure san.  And..."
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
    "Then I spied one of the teahcers turning down the stairs."
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
    "After finishing my homework for the day, I decided to take a walk around, get some fresh air.  As I passed by the vending machines, I saw Aida sitting at one of the picnic tables, looking at something in her hands."
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
    "Aida scooted over for me, even though there was plenty of room on the bench.  I sat down and looked out towards the sunset-lit clouds."
    MC "You know, I was so worried when I first found out what mine was.  The hair, that is."
    PRG "..."
    MC "I was worried I was going to be growing it everywhere- on my arms, on my chest, my back..."
    PRG "..."
    MC "Even on my butt!  Can you imagine, having hair growing out of your butt long enough to style?!"
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
            MC "Absolutely. We're dealing with such major uncharted territory.  I mean, sure, it's 'only' hair, but how fast is it going to grow?  Is it going to suck all the color out of me early, leaving my with white old man hair before I'm 30?"
            MC "Where's all the hair coming from, is it going to, I don't know, leech the hard stuff out of my skull to fuel it?"
            PRG "..."
            MC "I don't think anyone here is completely carefree about being here."
            PRG "Mizutani-san seems pretty okay with hers. She tells just about everyone she meets, it seems."
            MC "Hahaha, well, Mizutani-san might be a special case... She seems excited about everything."
            PRG "Heh..."
            MC "But, so, are you worried about yours? Do you need... I don't know, someone to confide in? Rant to?  If I can help, I'd like to."
            PRG "That's..."
            show PRG happy
            PRG "That's very nice of you, Hotsure-san..."
            show PRG neutral
            PRG "But I... don't want to talk about it."
            show PRG sad
            PRG "I think... I should go now.  I'm sorry for bothering you."
            MC "Are you sure?  It's not a bother, really."
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
            MC "Exactly. But now, what's my hair going to be like?  Are the strands going to be super thick? Are they going to split into smaller hairs as they grow out? Scientists are going to be testing and examining my hair in a laboratory, how neat is that?"
            PRG "But... but what about... what if something goes wrong?"
            MC "So what if it does? It's hair, it'll grow back. And apparently quickly, at that."
            PRG "No, I mean, like, like... I, what if it hurts, or if it goes out of control, or makes you look weird?"
            "I snorted, looking over to Aida and smiling when she met my eyes for a moment, before she quickly glanced back down."
            MC "Well, I mean, I guess I'll deal with it.  It's not like I'm not in the best place in the world to deal with it, right?"
            PRG "I suppose..."
            MC "Come on, we're in probably the most accepting place for these kind of special attributes. Whatever happens to any of us here... well, it will be an adventure, right?  Sure, it'll have its ups and downs, but nothing terrible's going to happen to us, not here of all places."
            PRG "..."
            show PRG unique
            PRG "W-would... I mean, u-um... is it okay, uh, t-to..."
            "I could hear the paper crinkling in her hands as she fidgeted, staring at her knees."
            PRG "W-would you help me, if it's not any t-trouble?  I'm n-n-not much good at adventures..."
            MC "Sure, absolutely. What do you need?"
            show PRG surprised
            PRG "Oh! N-nothing right now, I- I wouldn't put you on the sp-p-pspot like that."
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
                MC "So... mind if I ask what yours is?  I've told you mine.."
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
            MC "Honestly?  I try not to think about it."
            show PRG surprised
            PRG "R-really?"
            MC "Yeah.  Just kinda file it away and leave it there."
            PRG "But how... h-how do you do it?"
            MC "...Do what?"
            PRG "Just- just ignore it! Ignore whatever's changing with you??"
            show PRG angry
            PRG "Th-they said it was permanent! That we'll, we'll, we're never going to get back to the way we were!"
            MC "That's {i}exactly{/i} why it's easy to ignore."
            show PRG neutral
            PRG "...?"
            MC "Let me ask you this: If I told you it was going to rain tomorrow, what would you do?"
            PRG "Eh?  B-but I didn't hear anything about-"
            MC "Hypothetically. Hypothetically, you know 100%% that it was going to rain tomorrow.  What would you do?"
            PRG "W-well, I don't know.  Uh, I, well I'd get my umbrella.. Maybe a raincoat if it was bad... I think I have some galoshes if it was really raining..."
            MC "But what would you do tonight?"
            PRG "Tonight?"
            MC "Yeah. It's raining tomorrow, what do you do different tonight?"
            PRG "I- I don't know, do I have laundry out, is my house in a flood zone...?"
            MC "No, nothing like that. Your home is fine, but it's raining tomorrow. What do you do?"
            show PRG unique
            PRG "I- I don't know. Nothing, I guess?  I mean, it's not raining yet, right?"
            MC "No, it's not. You don't bother doing anything about it because it hasn't happened yet."
            "Aida nodded a few times, brow furrowed, until she closed her eyes and her features fell."
            show PRG neutral
            PRG "Oh... I see."
            MC "Exactly. You can't do anything about the rain before it happens, you can't stop it when it does happen, but you can take care of yourself and protect yourself from the worst of it."
            MC "If everything the nurses, Tashi-Sensei, and the older students have said is true, whatever's going to happen is {i}going{/i} to happen. So why worry about it now?  I might as well worry if the sun is going to come up."
            MC "When whatever changes we have start actually changing us, I'll see what I need to do. Do I just need the umbrella?  Do I need a coat, too?  Is it so bad I need galoshes?"
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
    "My eye wandered down from her chest, and I saw her hips were bigger, too, wider, more thick-looking. Definitely more padding thatn could be explained by a 'freshman 15'."
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
    PRG "A-ah, h-helo Inoue-san..."
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
    "As usual with bento, the box is divided up into sections, each with its own food type. Rice, fruits, meat and vegetables. It was all there. The vibrant colors were a sight to behold."
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
    "I placed the chopsticks on the lunchbox and shoved it to infront of Aida. Even if she made it for me, I wouldn't want her to starve because of it."
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
    $setProgress("PRG", "PRG020")
    scene Dorm BBW with fade
    show PRG sad with dissolve
    play music Sunset
    PRG "I'm sorry to lend your time like this..."
    MC "Don't worry about it! Getting you up to speed is also a way for me to refine my studies, making sure I didn't forget bits."
    show PRG neutral
    "I looked over behind her, the orange sky was slowly transitioning into a dark night. Truthfully I had hoped to spend my evening differently, the day ended up pretty tiring. But when Aida asked me for her help, with those eyes... My heart faltered."
    "Nevertheless, it was intriguing to see how Alice and Aida arranged their dorm room. The divide was eerily similar to mine and Daichi's. Rather than Daichi’s cluttered half, Alice’s looked more like a fancy five-star hotel. The bed, chairs, table, just about everything appeared incredibly luxury. How much did she bring from her home…"
    scene Dorm PRG Day with dissolve
    show PRG neutral
    "And Aida’s side was quite simple, but looked cleaner than any of ours did. Like it was straight out of a magazine cover."
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
            PRG "The Fujiwara and… uhm… Taira clan?"
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
        "I closed my eyes, letting out a deep sigh. It didn’t take long before my subconscious slipped into a deep slumber."
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

label PRG019:
    scene Classroom with fade
    play music Schoolday
    "Morning classes went by in no time at all, as usual.  As the day wore on, I found myself glancing across the room at Aida from time to time.  On occasion, I'd catch her looking at me as well, but she'd turn her head away at the last minute, trying to look inconspicuous.  When we were finally dismissed from our classes, Aida popped up from her desk and walked over to mine."
    show PRG unique with dissolve
    PRG "Hello, Keisuke-kun."
    MC "Hi, Aida-san."
    "I smiled at her.  It was unusual for her to be so relaxed, but her body language told a different story.  She was wringing her hands, clearly trying to keep her composure."
    PRG "I couldn't help but notice that your hair must've grown again recently."
    MC "Really? I didn't notice."
    "I reached a hand up and ran it through my hair.  It did feel longer, and when I pulled my hand back, it all flopped down into my eyes."
    MC "I see what you mean."
    show PRG happy
    "This made Aida bust out laughing.  Aida was usually so worried or nervous about something, that when she did laugh, it seemed to brighten the whole room."
    PRG "D-do you have an appointment made to see a barber?"
    MC "No, and on such short notice, I won't be able to get in for at least a couple of days."
    PRG "Well... Maybe...  I could cut your hair for you?  S-so you wouldn't have to wait!"
    MC "I couldn't ask you to do something like that, Aida.  You already have so much going on, I'd hate to take up more of your time."
    show PRG aroused
    PRG "I guess what I'm asking is... can I please cut your hair?"
    "I was shocked to hear her being so forward, but it would be nice to have her cut my hair for a change.  Plus, I wouldn't have to wait."
    MC "Are you sure it's no trouble?"
    show PRG happy
    PRG "None at all!  I love cutting hair!"
    MC "It's a deal then! So where would you like to do this?"
    PRG "Hmm...  let's go out by the picnic tables after our afternoon classes.  It's nice out today, and any mess we make will be easier to clean out there."
    MC "Good thinking.  Let's head to the cafeteria for now, I'm starving!"
    PRG "O-Okay!"
    "We both left the classroom and hurried down to the cafeteria together."
    scene Hallway with fade
    show PRG neutral with dissolve
    PRG "If it's not too much trouble, would you mind if I brought my radio when I cut your hair?  The dragons are playing again tonight and if they win, they'll be in the Japan Series!"
    MC "Of course not! Bring it, and I'll cheer them on with you!" 
    show PRG happy
    "Aida's face lit up when I said that."
    PRG "Yay! With the two of us cheering together, they can't lose!"
    scene black with fade
    "We made our way into the cafeteria together.  I joined Aida at her table, once again, and we spent what was left of lunch period talking about baseball, classes, and really anything else we could think of."
    scene Campus Center with fade
    "The air was warm as I stepped out into the schoolyard.  Immediately, a strong blast of wind hit me and blew my hair around like some bishounen anime.  Through my blowing tufts of hair, I saw something moving in front of me.  I pulled my hair apart and looked up.  Aida was waving at me from the picnic tables.  I ran up to meet her, trying to not be blinded by my own hair in the process."
    show PRG neutral with dissolve
    PRG "H-Hey Keisuke-kun. Are you ready for your haircut?" 
    MC "Yep, all set!" 
    "I gave Aida a reassuring smile, one of those that hopefully said 'I trust you,' and not 'please, dear god, don't screw up my hair.'"
    "I sat down at the bench, and I felt something drape over my shoulders.  I took a look down to see that Aida had laid a towel down over them."
    MC "Thank you."
    PRG "You're welcome. It's how I was taught, after all."  
    MC "Have you been doing this long, then?" 
    PRG "Not for a while.  My mom taught me how to cut hair when I was little."  
    MC "My mom used to cut my hair all the time when I was little.  She always used to tell me 'It may not be the most glamourous haircut, but it's free.'" 
    show PRG happy
    "Aida laughed out loud at that."
    PRG "What's your family like?" 
    MC "They're not bad.  It's just my mom, my dad, my sister, and I.  We would always do a lot together, and we always enjoyed the time we had, but my dad worked a lot, so we were used to him going away quite often for trips and such."
    PRG "That's so nice. What's your sister like?" 
    MC "We've always been really close.  She actually goes here too, but I haven't seen her much since we got here.  She has a hair growth factor just like I do." 
    PRG "Really? I-I'd like to meet her sometime. What's her name?" 
    MC "It's Tomoko. She's into the Dragons too, so you two would have a lot of fun together. Oh! Did you want to turn the game on?" 
    show PRG surprised
    PRG "Oh, yes! I completely forgot!"
    "Aida spun around and slid her radio out of her bag.  She messed with the channels until we heard the announcer's voice, albeit with a bit of static."
    show PRG neutral
    PRG "I'd hate to miss this." 
    "Aida turned back to my head and leaned over to reach my bangs. As she leaned over, one of her breasts pressed against my back, feeling soft like a pillow, yet surprisingly firm."
    PRG "Your hair is so thick." 
    "She ran a hand through my hair as she backed up."
    MC "It's always been that way, thick hair runs in my family."
    "Just then, the announcer's voice rang out loud and clear."
    Announcer "And it's gone! A home run for the Dragons! The score is now 3-1!  If the Dragons can keep this lead, the World Series may have a new contender on their hands!" 
    show PRG happy
    PRG "YES!!!!!!!" 
    "Aida was bouncing up and down happily.  Thankfully, she had set down the scissors when she had heard the announcer, so I wasn't at risk of a potentially dangerous new piercing.  Suddenly, Aida looked worried."
    show PRG unique
    PRG "I... I hope they can go all the way. They really deserve it." 
    menu:
        "They'll make it for sure!":
            jump PRG019_c1_1
        "Let's hope they can keep their cool.": #-2
            jump PRG019_c1_2

label PRG019_c1_1:
    $setAffection("PRG", 2)
    show PRG happy
    "Aida smiled at me."
    PRG "You're right! It's best to stay optimistic."
    MC "This is their best season in a long time. If anyone can win, I'd put my money on them any day!" 
    PRG "I'm glad you think so. It's nice to have someone else to cheer them on with."
    jump PRG019_c1_after
    
label PRG019_c1_2:
    show PRG neutral
    PRG "W-what do you mean?"
    MC "I mean that any team can get nervous and screw up.  It happens to the best of them.  It's good to be hopeful for them, but don't be upset if they don't make it." 
    show PRG sad
    $setAffection("PRG", -2)
    PRG "Yeah, that makes sense I guess."
    jump PRG019_c1_after

label PRG019_c1_after:
    "Aida went back to cutting my hair, while I sat and listened to the rhythmic snips of her scissors.  Each cut so precise, with no movement wasted."
    show PRG neutral
    PRG "Can I ask you something, Keisuke?" 
    MC "Sure, what's on your mind?" 
    PRG "Um..."
    "She stopped cutting for a moment.  I looked back and she was looking around nervously, like someone was about to attack her or something."
    show PRG unique
    PRG  "I... I know you mentioned your feelings about your growth before, but how are you feeling now?  Are you doing okay?"
    MC "I'm doing pretty well with it, at least I'd say so.  I realized that with regular haircuts, I can keep mine in check, whereas most people won't have that luxury.  By the way, thanks again for doing this, I could never cut it myself and not look like a disaster."
    show PRG neutral
    PRG "It's no trouble: like I said before, it's kinda fun."
    "I closed my eyes as Aida moved to my bangs once more, and just like before, her breasts brushed against me.  All the while, the sound of the radio droned on in the background."
    MC "How have you been dealing with your growth?" 
    show PRG unique
    PRG "...All right, I guess."
    "There it was again. That uneasiness as soon as her growth was brought up.  Whatever her growth was, she wasn't too keen on revealing it."
    MC "I'm sorry, I didn't mean to bring up a touchy subject."
    show PRG neutral
    if getAffection("PRG") > 9:
        PRG "It's alright, Keisuke. It wouldn't be hard to explain anyway, especially to a man."
        MC "Hey! Just because I'm a guy doesn't mean I don't understand things."
        PRG "I'm not saying you aren't smart. This is just... different." 
        "I decided not to press the issue any further.  If she wanted to tell me, she'd tell me when she was ready, and it wasn't my place to push her."
    else:
        PRG "It's okay. Let's just talk about something else. I'm almost done here." 
    "Aida cleaned off her scissors and picked up her towel. I stood up and shook my head, sending little hairs flying in the breeze.  I turned to Aida."
    MC "Thanks so much, Aida!" 
    show PRG happy
    PRG "You're welcome. I'm glad I could help you.  You were starting to look a little shaggy."  
    "I looked in the hand mirror Aida had brought along and threw my head this way and that, examining every angle."
    MC "It looks really good.  Maybe you should look for a career as a personal stylist."
    show PRG aroused
    PRG "I...I could never do that."
    MC "Of course you could! I couldn't pay someone to give me a cut like this.  You have some serious talent."  
    PRG "You're sweet, Keisuke. Maybe I'll have to think about it a bit."
    "Just then, the radio crackled to life as the announcer's voice rang out loud and clear."
    Announcer "THE DRAGONS WIN IT!  THEY'RE ON THEIR WAY TO THE WORLD SERIES!!"
    "Aida dropped her towel in shock, then a huge grin crossed her face."
    show PRG happy
    PRG "YES! FINALLY!! THEY'RE IN!!"
    "She was practically shaking with excitement, jumping up and down like a kid in a candy store."
    "I stood there staring at Aida, dumbfounded.  I'd never seen her so excited, but there she was, cheering for her favorite team. It was pretty cool to see actually."
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
    "Aida gave a me a small, sweet wave, and set out across the courtyard.  The way the wind was blowing pressed her skirt against her hips, accentuating them even further. A thought crossed my mind as I headed back to the boys dorms."
    MCT "She's definitely gained a little weight, probably from the cooking club. But thankfully, it looks good on her."
    jump daymenu

label PRG020:
    "This marks the current end of Aida's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance
