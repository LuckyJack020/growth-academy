define PRG = Character('Kodama', color="#FF3399", what_prefix='{size=-6}', what_suffix='{/size}')
define fade = Fade(0.5, 0.0, 0.5)

image PRG neutral = ConditionSwitch(
    "gametime > datelibrary['PRG_size_2']", "Graphics/PRG-2-neutral.png",
    "True", "Graphics/PRG-1-neutral.png")
image PRG neutral_flip = ConditionSwitch(
    "gametime > datelibrary['PRG_size_2']", im.Flip("Graphics/PRG-2-neutral.png", horizontal=True),
    "True", im.Flip("Graphics/PRG-1-neutral.png", horizontal=True))
image PRG happy = ConditionSwitch(
    "gametime > datelibrary['PRG_size_2']", "Graphics/PRG-2-happy.png", 
    "True", "Graphics/PRG-1-happy.png")
image PRG sad = ConditionSwitch(
    "gametime > datelibrary['PRG_size_2']", "Graphics/PRG-2-sad.png",
    "True", "Graphics/PRG-1-sad.png")
image PRG surprised = ConditionSwitch(
    "gametime > datelibrary['PRG_size_2']", "Graphics/PRG-2-surprised.png",
    "True", "Graphics/PRG-1-surprised.png")
image PRG surprised_flip = ConditionSwitch(
    "gametime > datelibrary['PRG_size_2']", im.Flip("Graphics/PRG-2-surprised.png", horizontal=True),
    "True", im.Flip("Graphics/PRG-1-surprised.png", horizontal=True))
image PRG angry = ConditionSwitch(
    "gametime > datelibrary['PRG_size_2']", "Graphics/PRG-2-angry.png",
    "True", "Graphics/PRG-1-angry.png")
image PRG aroused = ConditionSwitch(
    "gametime > datelibrary['PRG_size_2']", "Graphics/PRG-2-aroused.png",
    "True", "Graphics/PRG-1-aroused.png")
image PRG unique = ConditionSwitch(
    "gametime > datelibrary['PRG_size_2']", "Graphics/PRG-2-aroused.png",
    "True", "Graphics/PRG-1-aroused.png") #TODO: replace when new sprites get implemented

image PRG surprised_flip = im.Flip("Graphics/PRG-1-surprised.png", horizontal=True)

init 2 python:
    datelibrary['PRG_size_6'] = datetime.date(2005, 12, 10)
    datelibrary['PRG_size_5'] = datetime.date(2005, 12, 10)
    datelibrary['PRG_size_4'] = datetime.date(2005, 12, 10)
    datelibrary['PRG_size_3'] = datetime.date(2005, 12, 10)
    datelibrary['PRG_size_2'] = datetime.date(2005, 4, 10)
    
    eventlibrary['PRG001'] = {"name": "Tongue Twister", "girls": ["PRG"], "location": "dormexterior", "conditions": [], "priority": 0}
    eventlibrary['PRG002'] = {"name": "A Bun Tasting", "girls": ["PRG", "BBW"], "location": "cafeteria", "conditions": [[ConditionEnum.EVENT, "PRG001"]], "priority": 0}
    eventlibrary['PRG003'] = {"name": "An Inviting Aroma", "girls": ["PRG"], "location": "classroom", "conditions": [[ConditionEnum.EVENT, "PRG002"]], "priority": False}
    eventlibrary['PRG004'] = {"name": "Mother Nature", "girls": ["PRG", "FMG"], "location": "track", "conditions": [[ConditionEnum.EVENT, "PRG003"]], "priority": False}
    eventlibrary['PRG005'] = {"name": "Hold on Tight", "girls": ["PRG"], "location": "auditorium", "conditions": [[ConditionEnum.PRESET]], "priority": 0}
    eventlibrary['PRG006'] = {"name": "Double Stacked", "girls": ["PRG"], "location": "auditorium", "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": 0}
    eventlibrary['PRG007'] = {"name": "A (Soft) Wall to Hide Behind", "girls": ["PRG"], "location": "auditorium", "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": 0}
    eventlibrary['PRG008'] = {"name": "Cups and Measurements", "girls": ["PRG"], "location": "classroom", "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": False}   
    eventlibrary['PRG009'] = {"name": "Handling with Change", "girls": ["PRG"], "location": "classroom", "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": False}
    eventlibrary['PRG010'] = {"name": "Rapidly Curvy", "girls": ["PRG"], "location": "classroom", "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["PRG_size_2"]]], "priority": False}

label PRG001:
    scene School Exterior with fade
    "On my way to the vending machines for a drink, I spied Aida-san from my class, frowning down at a can of tea."
    show PRG sad
    "Her worried look made me think back to that first morning with Tashi-Sensei, and how she'd reacted to his tongue."
    "While most students had been shocked, disgusted, or morbidly interested in the meter-long appendage, Aida had covered her face in her hands and slunk down in her seat like she was trying to hide from it."
    "Maybe she was still trying to work through it? I decided to go talk to her."
    MC "Hey, Aida?"
    show PRG surprised
    PRG "Ah! Oh, sorry, do you need me to move?"
    MC "No, I just wanted to see how you were doing."
    PRG "M-Me?"
    MC "After that first speech in class...you didn't seem to take it very well."
    show PRG sad #change to aroused later
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
    

label PRG002:
    scene Cafeteria with fade
    "I felt hungrier than usual today, so I stopped by the cafeteria for an extra snack.  I had just finished my red bean bun when I spied Aida coming in the door near where I was sitting."
    show PRG neutral at Position(xpos=0.65, xanchor=0.5) with dissolve
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
    show PRG neutral with fade
    "We spent a few minutes in line, making small talk and getting to know each other better."
    "When we finally got up to the counter, Aida ordered several bean paste buns and a few jelly rolls. Her large bag of pastries in hand, we set out into the cafeteria seating, looking for Alice."
    BBW "Here, Kodoma-san."
    PRG "Ah! C-coming!"
    show BBW neutral at Position(xpos=0.25, xanchor=0.5) with dissolve
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
    PRG "O-okay, well, the next one here is melon bread…"
    "Again with cutting a piece, tasting, then cleansing her palate."
    BBW "Sweet taste that almost overpowers the fruitiness, perhaps due to whatever preservatives or flavor enhancers are included in this. The bread has the same problem as the red bean sample, thin but dense. Perhaps unavoidable in a mass-produced and distributed product like this. The aftertaste is strong enough to be noted, but not unpleasant."
    BBW "Final verdict: Above average quality."
    "Again Aida took notes, and I just sort of stood there observing as Alice worked her way through the pastries, until I couldn't take the curiosity any longer."
    MC "So... what is this, exactly?"
    BBW "I am familiarizing myself with the different types of snacks available. Like a wine tasting, but appropriate for the school."
    menu:
        "Ask about the food":
            MC "You’re not actually going to eat them all?"
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
    scene F1 Hallway with fade
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
    show PRG neutral at Position(xpos=0.75, xanchor=0.5)
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
    show PRG neutral at center
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
    show PRG sad #replace with aroused
    "I smiled at her reassuringly, but Aida nevertheless blushed hotly."
    PRG "Oh, I don't know a-about that... I just know, um, how to cook."
    MC "People who just \"know how to cook\" don't make smells that can lure people in from halfway down the hall..."
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
    show PRG surprised_flip
    show PRG surprised
    show PRG surprised_flip
    "I don't think Aida could have looked more surprised if I'd told her aliens had just landed."
    show PRG sad #replace with aroused
    PRG "M-me? Why? Did I d-do something wrong?"
    MC "No, I just thought I'd drop by and visit with you for a bit. I like hanging around you."
    "Aida's blush deepened, and she stared intently at her saucepan as she stirred it."
    PRG "B-but all I'm doing is cooking some things..."
    menu:
        "I've always wanted to know more about cooking.":
            jump PRG003_3_a
        "You think you could teach me?":
            jump PRG003_3_b
        "\"All you're doing\"? That's such an important skill to have!":
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
    show PRG happy #replace with aroused
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
    " "
    $ renpy.pause(1.5, hard=True)
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
    #show PRG aroused
    PRG "Oh, okay, w-well, this odd-looking spoon, that's called a pasta fork, actually. A-and this, this is a ravioli stamp. Alice says she enjoys Italian food, but uhm, a lot of \"Italian\" food, like modern pizza, was actually invented in America... Maybe, uhm, inspired by original Italian dishes like Focaccia, but..."
    scene black with fade
    scene Classroom with fade
    show PRG happy at Position(xpos=0.75, xanchor=0.5)
    with dissolve
    PRG "...And now that it's drained in the, uh, in the strainer, I just need to put some of the alfredo sauce- named after an Italian restaurant owner in Rome- over it and it's ready for Alice."
    MC "Wow, you sure do know a lot, Kodama-san."
    show PRG sad at center #replace with aroused
    PRG "I-it's really nothing special..."
    MC "Well, if you say so, but I sure learned a lot. Thanks for letting me hang out with you, hope Alice's happy with her food!"
    show PRG happy
    PRG "R-right! Y-you too, Hotsure-san!"
    hide PRG happy with dissolve
    "Aida hurried off to her dorm, and I snuck a ravioli from the strainer before she returned."
    MCT "Wow, she really {i}is{/i} good..."
    "(Your \"Art\" Skill has increased!)"
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
    MC "\"All you're doing\"? That's such an important skill to have!"
    show PRG surprised
    PRG "It-it is?"
    MC "Well, of course! Everyone has to eat. Being able to take what's available and make something delicious out of it..."
    show PRG neutral
    PRG "W-well, I guess it's useful..."
    MC "It's more than just useful. There's something about a lovingly home-cooked meal, especially shared with others. It shows our better natures to each other in such an important way."
    PRG "You... you really think so?"
    MC "Absolutely. It's one of the purest forms of showing care and love for another, to give up what's yours to make sure they're healthy and happy. It's practically the basis of civilization, preparing and sharing food."
    #show PRG aroused
    PRG "I... never thought of it like that."
    show PRG happy
    PRG "Do... do you really think all that, Hotsure-san?"
    "I nodded, smiling. I'd kind of gone off on a tangent, but hey, if I could give Aida something to lift her mood, I wanted to do it, and the way she was beaming it was pretty obvious I'd succeeded..."
    $ setAffection("PRG", 2)
    jump daymenu
    
label PRG004:
    scene Track with fade
    "Aida had finished making Alice's lunch early, so she and I decided to go for a walk around campus. The weather was nice, the sea breeze was cool... it almost felt like a date. I took a deep breath as we passed in front of the athletics building, and smiled."
    MC "This is nice, isn't it?"
    show PRG neutral with dissolve
    PRG "Hm? What is?"
    MC "This, just, us, the sky, the sun, the breeze... It's nice to just be out with a friend on peaceful days like this."
    PRG "..."
    #show PRG aroused
    PRG "..."
    PRG "You... y-you think I'm a-"
    "{b}{i}SLAM!{/i}{/b}"
    $ renpy.with_statement(vpunch, always=True)
    show FMG angry at Position (xpos=0.75, xanchor=0.5) with dissolve
    show PRG surprised at Position (xpos=0.25, xanchor=0.5)
    "We were interrupted by Akira flying through the front doors of the athletics center at dangerous speeds, sprinting full tilt down the side of the building. We watched with wonder as she made it to the end of the long building in seconds."
    hide FMG angry
    show PRG neutral at center
    PRG "...Was that... That was Mizutani-san, right? From our class?"
    MC "Yeah, and she... That didn't look like an exercize run..."
    PRG "We should go see what's wrong."
    
    scene School Planter with dissolve
    "I nodded, and we hurried around the corner of the building to see if there was any sign of Akira. To our surprise she was only a handful of paces past the corner, kneeling in the grass and looking at something."
    show FMG sad at Position (xpos=0.75, xanchor=0.5)
    FMG "Oh no, oh no, c'mon little guy..."
    "When we got close to Akira, we saw what she was so concerned about. Lying motionless in the grass in an unnatural, awkward heap was a small bird, no bigger than Akira's hands cupped together."
    show PRG sad at Position (xpos=0.25, xanchor=0.5)
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
    show PRG sad #replace with aroused
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
    show FMG sad #replace with aroused
    FMG "...Umm, can- would you mind getting it, Hotsure-san? I... I'm a little worried I might hurt it, too in the zone of holding hard metal right now..."
    MC "Oh, uh, sure thing, yeah."
    "I kneeled down next to the bird, taking off my jacket and bunching it up into a kind of horseshoe around it. Slowly, gently, I closed it around and under the bird, lifting it up off the ground in the makeshift fabric bird's nest."
    MC "Okay... Okay, let's go find someone who can help."
    show FMG neutral
    show PRG neutral
    FMG "Right."
    PRG "..."
    
    scene School Exterior with fade
    MC "Excuse me, do you know anything about birds? This one's injured, and- oh, you don't? Thanks anyways."
    show FMG angry
    FMG "Hey! Hey you! We've got an injured animal here, and- hey! Where are you- stop running!"
    FMG "Sheesh, why does no one want to help?"
    MC "Well, uh... you might be coming on a little too strong."
    FMG "Harumph. Oh hey, you there, lady with the long hair!"
    show FMG neutral at Position (xpos=0.25, xanchor=0.5)
    show GTS neutral at Position (xpos=0.75, xanchor=0.5)
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
    hide FMG happy
    hide GTS neutral with dissolve
    "Akira ran off to find what she needed, yelling for me to follow. I turned to Aida with an apologetic look."
    show PRG neutral with dissolve
    MC "So much for \"peaceful days like this\", I suppose. Sorry you got wrapped up in all this excitement."
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
    $ renpy.pause(1.5, hard=True)
    show FMG angry
    FMG "What?!"
    show PRG sad #replace with aroused
    MC "Well, I mean-"
    FMG "We're not just leaving it here!"
    MC "Well hey, do you know what's wrong with it?"
    show FMG sad #replace with aroused
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
    "Akira was off like a shot, her muscular legs propelling her towards the classrooms with surprising speed."
    show PRG neutral at center
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
    scene Auditorium with fade
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
    MC "Not at all. *ahem* \"Student has hyper-productive keratin in scalp and face, leading to accelerated hair growth. No indications of accelerated hair growth in other areas.\""
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
    show BBW neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
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
    "After our morning classes, I headed over to the cafeteria for lunch. However, the queue was surprisingly long. It seemed I joined in at the peak hour."
    "I took a moment to glance around, looking for potential tables to sit at. A good portion of them were already taken. But then I spotted Aida, sitting alone at one of the big tables, hunched over her food."
    MCT "Huh, she’s not with Alice? I’ll drop by once I’ve got my lunch."
    "Once I had the plastic tray with my lunch, I walked over to the spot where Aida had been sitting before."
    "However, a large group of students now occupied the table alongside her, the only seat available right between her and the group. I made my way to her side of the table."
    show PRG neutral with dissolve
    MC "Hey Kodama-san!"
    show PRG surprised
    PRG "Ah! H-hi, Hotsure-san."
    MC "Mind if I sit next to you? You seem like you could use the company."
    show PRG sad
    PRG "O-oh, really? Hrm..."
    PRG "She looked back down at her boxed lunch for a moment,"
    show PRG neutral
    extend " then nodded gently."
    "I took that as my cue to sit down in the chair next to her, between the group and Aida. We both dug into our food, but after a minute or so, my curiosity got the better of me."
    MC "So, uh… no Alice today?"
    PRG "Well... She’s taking care of something personally, but she wants me on call in case she needs me."
    MC "On call, huh..."
    MCT "That does sound like something she would say."
    PRG "Y-yes."
    MC "Well… let’s make the best of it then, hm?"
    "Before she could get a word out, the environment got a lot louder."
    hide PRG with dissolve
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
            PRG "Y-yes, I’m fine."
            MC "You sure? I mean… I think it’s normal to be concerned when a conflict occurs. Everyone responds differently. I was about to try to stop them, but thankfully there was no need for that."
            "Aida turned and looked at my face, before diverting her eyes again. But she nodded and gave a slight smile."
            show PRG neutral
            PRG "Yeah… Thank you, Hotsure-san."
            MC "No problem."
            MC "Anyway, glad that’s over. Let’s enjoy that free time, shall we?"
            show PRG happy
            PRG "Sure!"
            "Her voice had a sudden cheer to it. She dug her chopsticks into her lunch with more energy than before."
        "Were you scared?":
            $setAffection("PRG", -1)
            show PRG sad
            PRG "Ye-... I mean… sorry."
            MC "Hm? There’s no need to be. I got a bit scared too. It could’ve easily gotten ugly, but fortunately the teacher got between them before that happened."
            "Aida sat there in silence, not even eating her food. I felt I should probably switch topics..."
            MC "Anyway, glad that’s over. Let’s enjoy that free time, shall we?"
            "Aida gave a slight nod... I took that as a sign to continue eating. That’s what we’re here for."
        "Good thing the teacher intervened...":
            show PRG sad
            PRG "Y-yes, I don’t like to think about what would’ve happened if…"
            MC "But it didn’t, fortunately. Even if they would have fought, the students around them would’ve probably stopped them before either of them got seriously injured. That’s what I like to think, anyway."
            show PRG happy
            PRG "Yeah, you’re probably right."
            MC "Anyway, glad that’s over. Let’s enjoy that free time, shall we?"
            show PRG neutral
            PRG "All r-right. Sounds good to me."
    "The remainder of the lunch went smooth. We both enjoyed our lunch, talked about things that happened in class, general small talk. Once we were done, we walked back to our homeroom for the next class."
    jump daymenu

label PRG008:
    scene School Inner with fade
    "The day had gone by quickly, classwork barely slowing me down. With little else to do before dinner, I went to find Aida, probably in the cooking classroom again."
    MCT "And maybe get a free sample, heh..."
    
    scene Classroom with fade
    show PRG neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    PRG "Oohh..."
    hide PRG neutral with dissolve
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    PRG "Not here either..."
    hide PRG neutral with dissolve
    show PRG neutral at center with dissolve
    PRG "Isn't there one anywhere?"
    "Instead of the usual soft, quiet, unobtrusive girl in the corner, Aida was shuffling from one side of the classroom to the other, every cupboard not already locked up opened as she searched for something."
    MC "Uh... Ko-Kodama-san?"
    show PRG surprised
    "Aida jumped in place, turning to me and blushing."
    show PRG sad #replace with aroused
    PRG "Ho-hotsure-san! I'm sorry, I- I didn't see you come in."
    MC "It's okay... What seems to be the problem?"
    PRG "Oh, it's awful, Hotsure-san! Alice, she gave me these fancy dishes for when I was cooking for her, but, but... well, look!"
    "Aida handed me a measuring cup, and I looked at the lines along the side."
    MC "...what's \"oz\" stand for?"
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
    TS "Well, sure, it's actually in the back of the math book here. And it's called \"Imperial\", not \"American\"."
    "Tsubasa-sensei hadn't even finished opening the book to the right page before I snatched it up and started running back to the cooking classroom."
    MC "Thanks, I'll bring it right back!"
    TS "H-hey! That's the teacher's edition!"
    MC "Promise I won't peek!"
    
    scene Classroom with fade
    show PRG sad with dissolve
    MC "I got it!"
    show PRG happy
    PRG "You did! Oh, thank you!"
    MC "Okay, let's see here, measurements, measurements... Ah, okay, so eight ounces in a \"cup\"... and now, over here... twenty-nine-point-five... thirty milliliters in an ounce. What's the recipe say?"
    show PRG neutral
    "Ah, ah, um... A hundred and fifty milliliters."
    MC "Okay, so, five ounces, about, and eight to a cup... You want to fill it to right there."
    "I pointed to the space between the \"1/2 cup\" and \"3/4 cup\" notches on the measuring cup. Aida nodded and we moved to the next ingredient, and then the next, until she had all the measurements down in the more familiar milliliters."
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
    "Aida's pouting made my heart sink, but she refused any more \"help\" from me. Dejected, I headed back to my dorm, trying to think of some way to make things up to Aida..."
    $ setAffection("PRG", -1)
    jump daymenu

label PRG008_3:
    MC "Don't worry, I know the conversion rate. Show me the recipe."
    show PRG surprised
    PRG "R-really?!"
    MC "Yeah, it's about thirty milliliters to the ounce."
    show PRG neutral #replace with aroused
    PRG "Um, \"about\"?"
    MC "Twenty-nine and a bit. Not enough to make a difference."
    show PRG neutral
    PRG "Oh... oh, okay."
    $ setAffection("PRG", 1)
    MC "So what's the first measurement you need?"
    PRG "Ah, ah, um... A hundred and fifty milliliters."
    MC "Okay, so, five ounces, about, and eight to a cup... You want to fill it to right there."
    "I pointed to the space between the \"1/2 cup\" and \"3/4 cup\" notches on the measuring cup. Aida nodded and we moved to the next ingredient, and then the next, until she had all the measurements down in the more familiar milliliters."
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
    scene School Exterior with fade
    "After finishing my homework for the day, I decided to take a walk around, get some fresh air.  As I passed by the vending machines, I saw Aida sitting at one of the picnic tables, looking at something in her hands."
    show PRG neutral at Position (xpos=0.2, xanchor=0.5) with dissolve
    PRG "..."
    "I approached Aida from the side, not trying to be sneaky, just that's how my path wound up intersecting her. As I got close, I recognized the paper she was staring at by the distinct shape and size."
    MC "Looking at your results, huh?"
    show PRG surprised_flip
    PRG "Eep!"
    show PRG neutral_flip
    PRG "O-oh, Hotsure-San! I, uh, y-you... Um..."
    "Aida whipped the paper behind her in the least convincing attempt at hiding something I think I'd ever seen."
    MC "..."
    PRG "..."
    MC "...Soo, checking out your results again?"
    show PRG sad at Position (xpos=0.2, xanchor=0.5) with dissolve
    pause 1.5
    hide PRG sad with dissolve
    show PRG neutral with dissolve 
    PRG "...Yes."
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
            MC "Absolutely. We're dealing with such major uncharted territory.  I mean, sure, it's \"only\" hair, but how fast is it going to grow?  Is it going to suck all the color out of me early, leaving my with white old man hair before I'm 30?"
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
            show PRG neutral_flip at Position (xpos=0.5, xanchor=0.5) with dissolve
            PRG "..."
            show PRG sad
            PRG "No, I-I should get going..."
        "Actually, I'm kind of excited.":
            MC "Actually, I'm kind of excited for it."
            show PRG surprised
            PRG "R-Really?  Why?   How?"
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
            show PRG happy at Transform(xzoom=-1) #TODO: flip
            PRG "...!"
            show PRG neutral
            PRG "*Ahem*, y-yes, I will, i-if, if it's not a bother."
            PRG "...Thank you, Hotsure san. I, I think, um, I'll be going now..."
            MC "Sure, no problem!"
            "Both of us got off the bench and said our goodbyes, but something occurred to me before she turned away."
            if isEventCleared("PRG005"):
                MC "...Still don't wanna tell me what yours is?"
                show PRG neutral_flip
                PRG "I..."
                show PRG neutral
                show PRG neutral_flip
                show PRG neutral
                show PRG neutral_flip
                PRG "..."
                PRG "I'm s-sorry, no."
                MC "*sigh*"
                MC "All right, well... I suppose sooner or later the answer's gonna be obvious one way or another."
                PRG "I... I'm s-sorry, really..."
                hide PRG neutral with dissolve
                pause 0.3
                show PRG neutral with dissolve
                PRG "..."
                show PRG sad
                hide PRG sad with dissolve
                MC "..."
            else:
                MC "So... mind if I ask what yours is?  I've told you mine.."
                PRG "...!"
                PRG "I... I..."
                show PRG sad
                PRG "..."
                MC "Hey, hey, it's okay. I just, a burden shared is a burden halved, you know?"
                PRG "...I'm... I'm sorry, Hotsure-san. I'm not..."
                show PRG sad at Transform(xzoom=-1) #TODO: flip
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
            MC "Hypothetically. Hypothetically, you know 100\%\ that it was going to rain tomorrow.  What would you do?"
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
    scene Classroom with fade
    "I wandered into the cooking clubhouse, knowing it was about the time that Aida started cooking for Alice, but before she got too involved in the meal to socialize."
    show PRG happy with dissolve
    "Aida looked at the sound of someone approaching, her expression momentarily brightening before her usual worried look crossed back over her features."
    PRG "Oh! U-um, hi Keisuke. What brings you here?"
    MC "Nothing much, was just around and thought I'd come visit for a bit, maybe help you with your cooking, if you'd like."
    show PRG sad #replace with aroused
    "As I walked closer, Aida seemed to get more uncomfortable, hunching her shoulders forward oddly and turning red."
    MC "Is something the matter? Do you need a fan for the heat or anything?"
    PRG "No! No, I-I'm fine, just fine."
    "I'd known Aida long enough that her \"Just fine\" was anything but, so I came around to her counter. When I did, her posture shifted again, her apron hanging off her oddly."
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
    show PRG sad #replace with aroused
    PRG "..."
    "I used the awkward silence to confirm what I'd felt. It was subtle, given how loosely she was wearing her clothes, but under the apron it was clear that Aida's bust had gotten larger. Not as big as Honoka, of course, but definitely bigger than that first meeting."
    "My eye wandered down from her chest, and I saw her hips were bigger, too, wider, more thick-looking. Definitely more padding thatn could be explained by a \"freshman 15\"."
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
    MC "no! I mean, yes! I mean, uh, I..."
    $ renpy.with_statement(Shake((0, 0, 0, 0), 0.75, dist=20))
    PRG "Uwaaa~!"
    hide PRG sad with dissolve
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