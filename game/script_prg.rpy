define PRG = Character('Kodama', color="#FF3399", what_prefix='{size=-6}', what_suffix='{/size}')

image PRG neutral = DynamicImage("Graphics/PRG-[globalsize]-neutral.png")
image PRG happy = DynamicImage("Graphics/PRG-[globalsize]-happy.png")
image PRG sad = DynamicImage("Graphics/PRG-[globalsize]-sad.png")
image PRG surprised = DynamicImage("Graphics/PRG-[globalsize]-surprised.png")
image PRG surprised_flip = im.Flip(PRG surprised, horizontal=True)
image PRG angry = DynamicImage("Graphics/PRG-[globalsize]-angry.png")
image PRG aroused = DynamicImage("Graphics/PRG-[globalsize]-aroused.png")

init 2 python:
    datelibrary['PRG_size_6'] = datetime.date(2005, 12, 10)
    datelibrary['PRG_size_5'] = datetime.date(2005, 12, 10)
    datelibrary['PRG_size_4'] = datetime.date(2005, 12, 10)
    datelibrary['PRG_size_3'] = datetime.date(2005, 12, 10)
    datelibrary['PRG_size_2'] = datetime.date(2005, 12, 10)
    
    eventlibrary['PRG001'] = {"name": "PRG001", "girls": ["PRG"], "location": "dormexterior", "conditions": [], "priority": 0}
    eventlibrary['PRG003'] = {"name": "PRG003", "girls": ["PRG"], "location": "classroom", "conditions": [[ConditionEnum.EVENT, "PRG001"]], "priority": False}
    eventlibrary['PRG004'] = {"name": "PRG004", "girls": ["PRG", "FMG"], "location": "track", "conditions": [[ConditionEnum.EVENT, "PRG003"]], "priority": False}
    eventlibrary['PRG005'] = {"name": "PRG005", "girls": ["PRG"], "location": "auditorium", "conditions": [[ConditionEnum.PRESET]], "priority": 0}
    eventlibrary['PRG008'] = {"name": "PRG008", "girls": ["PRG"], "location": "classroom", "conditions": [[ConditionEnum.EVENT, "PRG004"]], "priority": False}
    eventlibrary['PRG010'] = {"name": "PRG008", "girls": ["PRG"], "location": "classroom", "conditions": [[ConditionEnum.EVENT, "PRG008"]], "priority": False}
    
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
    hide PRG with fade
    "And with that she was on her way again, though I thought about the conversation for a few minutes afterwards. What {i}was{/i} going to change about me?"
    $ setAffection("PRG", 2)
    jump daymenu
    
label PRG003:
    scene F1 Hallway with fade
    "None of the clubs I was interested in were meeting after class today, so I just wandered the halls after class, watching the other students as they filed out of the building."
    "It was amazing to see all the different sizes and shapes and exaggerations of anatomy leaving out the big double doors, but most of the upperclassmen seemed to have adjusted fairly well."
    MC "...sniff, sniff..."
    MC "Wow, something smells good..."
    "I followed the scent to the end of the hallway, a small room in the corner opposite the stairs beckoning me with its open door. I peeked inside, and who should I find at the home ec. stations but mousy, unassuming Aida."
    scene Classroom Day with fade
    show PRG happy with fade
    MC "Hi there, Kodama-san!"
    "I had tried to sound friendly, but she jumped like I'd shouted her name at the top of my lungs."
    show PRG surprised
    PRG "Ah! I'm sorry!"
    show PRG neutral at Position(xpos=0.75, xanchor=0.5)
    PRG "I-is there a club meeting? Am-Am I in the way?"
    menu:
        "No, no one's coming that I know of.":
            jump PRG003_1
        "So you fance yourself a chef?":
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
    MC "So, you fance yourself a chef, Kodama-san?"
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

label PRG_003_2_c:
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
    $ renpy.Fade(0.5, 1.5, 0.5)
    show PRG happy at Position(xpos=0.75, xanchor=0.5)
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
    show PRG neutral with fade
    PRG "Hm? What is?"
    MC "This, just, us, the sky, the sun, the breeze... It's nice to just be out with a friend on peaceful days like this."
    PRG "..."
    #show PRG aroused
    PRG "..."
    PRG "You... y-you think I'm a-"
    "{b}{i}SLAM!{/i}{/b}"
    $ renpy.with_statement(vpunch, always=True)
    show PRG surprised at Position (xpos=0.25, xanchor=0.5)
    show FMG angry at Position (xpos=0.75, xanchor=0.5) with fade
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
    hide GTS neutral
    with fade
    "Akira ran off to find what she needed, yelling for me to follow. I turned to Aida with an apologetic look."
    show PRG neutral with fade
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
    show PRG Happy
    $ renpy.pause(1.5, hard=True)
    show FMG Angry
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
    hide FMG angry with fade
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
    
label PRG005
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
    hide PRG with fade
    "Aida gave a quick, deep bow, and scurried off, leaving me wondering what was so terrible on that sheet she couldn't tell me..."
    jump daymenu
    
label PRG008:
    scene School Inner with fade
    "The day had gone by quickly, classwork barely slowing me down. With little else to do before dinner, I went to find Aida, probably in the cooking classroom again."
    MCT "And maybe get a free sample, heh..."
    
    scene Classroom Day with fade
    show PRG neutral at Position (xpos=0.25, xanchor=0.5) with fade
    PRG "Oohh..."
    hide PRG neutral with fade
    show PRG neutral at Position (xpos=0.75, xanchor=0.5) with fade
    PRG "Not here either..."
    hide PRG neutral with fade
    show PRG neutral at center with fade
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
    
    scene Classroom Day with fade
    show PRG sad with fade
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
    hide PRG with fade
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
    
label PRG010:
    scene Classroom Day with fade
    "I wandered into the cooking clubhouse, knowing it was about the time that Aida started cooking for Alice, but before she got too involved in the meal to socialize."
    show PRG happy with fade
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