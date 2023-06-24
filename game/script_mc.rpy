label global000:
    stop music

    # Without a defined character code before the dialogue, it's unattributed speech. Good for narration.
    #EX - "This is the narrator, introducing our characters."

    # This is what text will look like with those codes attached.
    # Line breaks are done by inserting the command \n where you want to start a new line. No spaces allowed.
    #Italics, bold, etc are done with curly brackets {i}{/i}{size=-5}{/size}
    # Position(xpos=.99, xanchor=0.5, yalign=1.0)
    #

    #EX - MC "Yo. I'm the player character, Hotsure Keisuke.\nI'm transferring to Seichou Academy this year."
    #EX - BE "I'm the BE character, Inoue Honoka!\nIt's good to see you again, Kei{i}-chan{/i}!"



    show black
    if debugenabled:
        menu:
            "(DEBUG) Skip Prologue":
                jump daymenu
            "View Prologue":
                $save_name = "Prologue"
                pass

    #SFX Light Motor SFX
    $showQuickMenu = True

    pause 1.5
    scene Ferry with fade
    play music MC
    "The hard bench under me lightly hummed with the vibrations of the ferry. Two hours of sitting here twiddling my thumbs and scrolling through my phone had left me beyond bored."
    "I leaned against the side of the boat, looking out across the shimmering, tranquil sea as the sun shimmered across its waves."
    "Not finding anything interesting to look at aside from water and sunshine, I turned back and glanced at my sister across from me, her gaze buried deep in the glass of her phone."
    MC "Nervous at all?"
    $setTomoOutfit(OutfitEnum.CASUAL)
    show FerryTomo1
    show Tomoko distracted at Position(ycenter=0.70, xcenter=0.5) behind FerryTomo1
    with dissolve
    Tomoko "Mm... nah."
    MC "Not even some new school jitters?"
    Tomoko "Nope."
    MCT "Don't know what I expected. Even earthquakes couldn't freak her out."
    play sound ClockTower
    "Overhead, one of the many loudspeakers dotted throughout the ferry whined."
    Announcer "Your attention, please. We will be docking in five minutes. If you aren't already, please take your seats. Thank you."
    show cg MC000 with dissolve
    "A few of the other students that had been milling around came to sit back down."
    "I leaned my head against the glass beside me. Ahead, a large, lush, green island loomed over us."
    MC "Well, that's welcoming."
    Tomoko "Did you say something?"
    MC "You know, since we're not going to know anyone else here, the least you could do is be a little more social."
    hide cg with dissolve
    pause 0.25
    show Tomoko neutral
    Tomoko "For what? We're only going to be here for a year. Odds are that we'll never see most of these people again anyway."
    MC "A lot can happen in a year, Tomo."
    show Tomoko annoyed
    Tomoko "Yeah, yeah. I don't need a full inspirational speech, Kei."
    show Tomoko neutral
    "I scoffed and looked back at the island."
    show Tomoko distracted
    "A fairly decent sized cluster of buildings jutted out from the trees, which parted around them to form a homey looking town."
    "And, since that was all I could see from here, I figured that the school had to be nestled in with those buildings."
    MCT "Not like they'd just stick it out in the boonies."
    pause .5
    MCT "At least I hope not."
    "That is what this island felt like compared to home, though. Compared to Tokyo, this was a complete 180."
    "I looked over to my sister once more, and my mom's words rang true in my head once again."
    MCT "Take care of your sister!"
    MCT "Yeah, will do, Mom."
    "I didn't have a problem with looking out for her. She was my twin after all. But, it was hard to do that when I didn't even know what to expect."
    MC "So, do you-"
    play sound ClockTower
    Announcer "Please remain seated until the ferry comes to a full stop, then make your way to the boarding dock, following the yellow lines on the floor. An attendant will be available should you need assistance!"
    show Tomoko neutral
    "The voice over the PA system rang out through the deck, causing a few of the other students to look up from their phones while others readied their bags for departure."
    Announcer "Group one, please exit off of the left side of the ferry. An attendant will be ready to lead you to registration on arrival."
    Announcer "Group two, please exit off of the right. Groups three and four, please wait until we're ready for you."
    hide Tomoko
    hide FerryTomo1
    with dissolve
    "Tomoko and I got up from our spots and shuffled in the crowd of students toward the center of the ferry."

    scene Dock with fade
    play music ClearSkies
    "Leaving the ferry, I spotted a small dock with red pillars and a red roof. The whole thing looked new, as if it had been built literally moments before I stepped off the boat."
    "From there, I could look around and see the town nearby."
    MCT "That's comforting. Kinda feels like home."
    "As my eyes left the comfort of the town, I looked over to the other half of the island. Hills graced the entire area that stretched out and away from me."
    MCT "Eesh..."
    "I did my best to clear my thoughts and joined the rest of the students, hiking my bag up around my shoulders."
    Student1 "... You heard of this place before?"
    Student2 "No. I didn't even have the time to look it up or anything. I just got the letter and... didn't really have a ton of options."
    Student2 "Thing is, I didn't even apply."
    Student1 "Wait, you didn't apply either?"
    pause .75
    MCT "... Weird."
    "I waited in line for a few minutes before reaching the building line at the end of the dock, where I was handed a small welcome gift bag by a warm looking woman with raven black hair."
    show Takamura neutral with dissolve
    "On her chest hung a bright nametag that read \"Aoi Takamura\"."
    show Takamura neutral at altMove(0.5, 0.75)
    show Tomoko neutral at Position(xcenter=0.25, yalign=1.0), Transform(xzoom=-1) with easeinleft
    Takamura "Can I get your name, please?"
    Tomoko "Tomoko Hotsure."
    show Takamura reassuring
    Takamura "Right... there you are! Here's a key for your dorm. We have a mandatory assembly tomorrow morning with the principal's annual speech, so be sure not to miss it!"
    Takamura "Group one, right over there. Just follow them to the academy. Welcome to Seichou!"
    Tomoko "Alright. Later bro."
    MC "Yeah. See ya."
    show Takamura neutral at altMove(0.5, 0.5)
    hide Tomoko with dissolve
    Takamura "And, your name, please?"
    MC "Keisuke Hotsure."
    Takamura "Another Hotsure? Okay... one second...{w} Ah! There you are."
    "The teacher blinked a few times."
    Takamura "Hmm... two Hotsures and two Utagashis. Curious..."
    "The teacher briefly scanned the table and grabbed something from it, then turned and glanced off at the group of students who were already almost out of sight."
    show Takamura reassuring
    Takamura "Well, looks like they were a little eager to get a move on. Just follow this path here all the way down."
    Takamura "And, here's a key for your dorm! As I'm sure you heard, assembly is tomorrow morning in the auditorium. Welcome to Seichou, Hotsure-san. Hope you enjoy your stay here!"
    MC "Alright. Thank you very much."
    hide Takamura with dissolve
    "I took off at a brisk pace, and left the rest of the students behind as I tried to catch up with my group."
    scene black with fade
    pause 1

    scene Lake Road with fade
    #BIRD SFX
    pause .5
    play music MC
    MCT "Geez... it's cooking out here."
    "I came to a stop on a wooden bridge overlooking a lake, taking the bottle of water from my gift bag and taking a sip."
    MCT "And, why haven't I seen anyone else?"
    "I looked back behind me, down the winding path I'd been following."
    "I knew that I was well away from the town by now."
    MCT "Where is this place, anyhow?"
    "I let out a loud sigh, taking another large gulp of water."
    "After I'd graduated from my last school, I'd assumed that I'd be just doing what the rest of my friends were, and going on to bigger and better things. University and all that."
    "But nope. My sister and I had both gotten letters in the mail regarding our attendance here, and that had derailed almost anything else going on."
    "And, I couldn't find any information about this place either. Seichou Academy."
    "Every online search I'd done had come up blank and barebones, giving me little more than a phone number and an email."
    "I hadn't even known that this place existed, let alone that it was between Hokkaido and Sakhalin."
    "I was gonna be living away from home and on my own, with my sister, my cell phone, and my personal belongings as my only ties back."
    "But even with those ties, they didn't make me feel any more at home."
    MCT "Those guys on the dock... that's what happened to Tomo and I too."
    "It happened literally on a random Tuesday evening. I'd gotten home from... something. Think I was helping Mom get groceries if I remember right."
    "My dad had been sitting at the kitchen table going through the mail, and he handed me a letter with some esoteric logo on it."
    "My sister and I packed, and we were in front of the ferry receiving tearful hugs goodbye from our mother only a few days later."
    "The entire thing had been a hodgepodge of conversations and confusion, on top of just getting ready to be sent here."
    "My luggage seemed to only be getting heavier as the minutes passed, my heart pounding away with each step I took. I had talked a big game to my parents about how I was fine..."
    "But... I had no clue if that was true or not."
    pause 0.75
    MCT "Did I take the wrong path? Like... I think I'd see a huge school by now."
    MCT "It's like Tokyo's metro lines all over again..."
    "I shook my head and looked around. All I saw was trees, the path in front of me, and the lake."
    MCT "Where even am I?! I've been walking for like, half an hour already!"
    "I walked through the forested path for a few more minutes, trying to catch my bearings as I searched desperately for any indication of civilization."
    "I picked up my pace as I came to a river and followed the path close to it."
    "Ahead of me, I spotted a flash of pure white. A young woman was bent down beside the river, trawling one hand through the water."
    MCT "Oh, thank God."
    MC "Excuse me!"
    show BE neutral with dissolve
    "The girl looked up from the river in surprise as I bounded up to her, panting and out of breath."
    play music BE
    MC "Hey! Hi, uh...{w} heh... Sorry, one sec..."
    show BE confused
    "As I knelt over with my hands on my knees, panting from the heat, I got a better look at the woman I was addressing."
    "Her face looked soft and feminine, though it was hard to tell based on the confusion plastered on her face; her brown eyes complimenting her chin-length mahogany hair well."
    MC "Sorry about that. Uh... do you know where the school is around here?"
    UNKNOWN "The... school?"
    "She stared at me intently, studying my face."
    MC "Yeah. Seichou Academy? I think I took a wrong turn or something on my way here."
    UNKNOWN "Uh..."
    pause .5
    UNKNOWN "Oh, wait! Are you with the new students?"
    MC "Yep. I got here like, half an hour ago."
    show BE neutral
    UNKNOWN "Okay, cool, cool. Yeah, I can get you to the main path."
    MC "Awesome."
    UNKNOWN "So! Lead the way."
    MC "Uh..."
    show BE embarrassed
    UNKNOWN "Oh! Tch- Duh, sorry. Follow me..."
    show BE neutral
    "I followed by the girl's side for a while without saying much."
    "As the minutes passed though, I couldn't help but start to feel a tad curious and inquisitive."
    MC "So, uh... you got here today too?"
    UNKNOWN "Yesterday."
    MC "Cool, cool."
    MCT "...I swear I know this girl from somewhere."
    MC "Sooo... It'd be rude of me to not ask the name of the girl who saved me, eh?"
    show BE happy
    BE "Oh! Um... Honoka."
    MC "Ah. Cool. That's a good name."
    MCT "..."
    MCT "Oh my god. There's no way."
    MC "...So, how did that all-girls' school treat you?"
    show BE confused
    BE "...Excuse me? How did you know I went to an all-girls' school?"
    "I bit my bottom lip and put my hands into my pockets, shrugging off her question."
    MC "Because you never forget the girl who kicks your ass in a Beetle Fighting Tournament-"
    show BE surprised
    BE "OH. MY.-"
    MC "What's good, Hon-"
    BE "Keisuke?! Keisuke Hotsure!?"
    MC "Took you long enough!"
    show BE happy
    BE "I-I thought, but I... Oh my god, it's been years!"
    MCT "There's that boyish grin I remember."
    "Honoka Inoue. My old childhood friend. The two of us were thick as thieves back in the day. When we weren't terrorizing Shibuya, we were spending our days chilling out in the countryside."
    "Until one day, she was just gone. Moved over to an all-girls' school in a different part of the country. We never saw each other again."
    BE "You dork! Why didn't you say anything the first time..."
    MC "What would be the chances?!"
    MCT "I mean, you look so different! You look..."
    play sound Boing
    show cg BE000 with vpunch
    MCT "H-Holy crap!!!"
    hide cg with dissolve
    show BE aroused with dissolve
    BE "Nehehe! You can't say you just now noticed {i}these{/i}."
    MC "The hell were they feeding you girls out there?! "
    show BE embarrassed
    BE "Pfff, you butthead!"
    MC "Tsssh"
    show BE wink
    BE "I {i}told{/i} you they'd get bigger eventually! But you never listened!"
    MC "How could I have known? We were both kids!"
    show BE happy
    BE "A woman's intuition is never wrong."
    MC "Is that so?"
    BE "Yep!"
    MC "What about when you said I was going to end up being a mutant monster that lived in the sewer?"
    show BE shrug
    BE "Hmm. I don't remember that. So it must never have happened. You're just making it up to toy with me."
    MC "I swear. Your words were, and I quote: \"I'll end up a beautiful princess, and you'll probably end up living in ooze.\""
    show BE happy
    BE "Noooo, I said \"living the... schmooz...y life?\""
    MC "Did you now?"
    show BE neutral
    BE "Probably! Hehe."
    show BE happy
    BE "Well, maybe that was the ooooone thing I was wrong about. It's weird, looking at you, I can't believe I didn't see it sooner."
    show BE neutral
    BE "You look so familiar, but just different enough. Like a disguise that almost worked."
    MC "And you..."
    MC "So, what are you doing out here?"
    show BE neutral
    BE "Not much. Trying to catch some frogs."
    MC "Cool. Cool. Didn't know you still did that."
    BE "Yep! Frogs are cooool~"
    BE "Oh! Is Tomo-chan here too?"
    MC "Yep, she's here! She's doing about the same as always. Finally got her to come out of her room."
    BE "Really? What, did you finally manage to afford that crowbar?"
    MC "Nah, doughnut on a stick. Works every time."
    BE "Ehehe~"
    BE "And how about you? How are you doing?"
    MC "I'm doing fine. I spent the break..."
    menu:
        "Swimming at the beach.":
            jump global000_cbreak_1
        "At the library.":
            jump global000_cbreak_2
        "Touring the local museums.":
            jump global000_cbreak_3

label global000_cbreak_1:
    $setFlag("global000_beach")
    MC "...swimming at the beach."
    $setSkill("Athletics", 3)
    show BE surprised
    BE "Whoa, really? Kei{i}-chan{/i} the beach bum?"
    show BE happy
    BE "I'd never figured you the type. Are you a hunk now? Can I squeeze your bicep?"
    MC "Oh, hush."
    jump global000_cbreak_after

label global000_cbreak_2:
    $setFlag("global000_library")
    MC "...at the library."
    $setSkill("Academics", 3)
    show BE surprised
    BE "The library?!"
    show BE sad
    BE "Were you kidnapped or something...?"
    "I laughed in spite of myself."
    MC "No! I just, I was curious about stuff we never learned in high school."
    MC "Things like how to say \"hello\" and \"thank you\" and stuff in a bunch of languages, weird science things they don't let us play with in chemistry class, all sorts of neat stuff..."
    show BE happy
    BE "Gosh, when you put it like that, it doesn't sound like studying!"
    show BE happy with hpunch
    "I let out a guffaw, and Honoka slugged me on the shoulder."
    BE "That means I can copy off your notes, now that you're a brainiac, right?"
    jump global000_cbreak_after

label global000_cbreak_3:
    $setFlag("global000_museum")
    MC "...touring the local museums."
    $setSkill("Art", 3)
    show BE happy
    BE "Oh wow! That sounds really neat!"
    MC "Yeah, it was. Art, music, botanical gardens, theater... All sorts of neat stuff!"
    BE "You'll have to tell me about it! I mostly played video games and wandered around outside."
    MC "Sure, anytime!"
    BE "Kei{i}-chan{/i} the cultured gentleman... Ha!"
    MC "Ha yourself."
    jump global000_cbreak_after

label global000_cbreak_after:
    MC "Anyways..."
    show cg BE000b with dissolve
    MC "Yeah, I'm doing all right."
    BE "Sweet. I came here yesterday, so I already know the lay of the land, y'know."
    BE "Speaking of which, how exactly did you get lost?"
    MC "Ah... well, I got off of the boat with the wrong group, and kind of just lost my way from there."
    BE "Some things never change, do they?"
    MC "Seems like it, I guess...?"
    MCT "She {i}still{/i} remembers that?"
    MC "Look, it's not my fault that Tokyo has such confusing metro lines!"
    BE "True, true. I've got a map, though. Came with the gift bag."
    pause .5
    MC "... Seriously?"
    BE "Eh... yeah? Take a look."
    "I dug my hand back into the bag and felt around for anything that resembled the texture of paper."
    pause .5
    MC "Okay... I've recently learned that I have a map. So, we're not lost."
    BE "Not yet, anyway."
    BE "Also, walking around's helped me get all the nervousness out of my system. It was childhood all over again, moving to a new boarding school and all."
    BE "But if you're going to be here too, I'm sure it'll be great!"
    BE "I guess we'll both be in your care, Kei{i}-chan{/i}, so do your best!"
    MC "Yeah, yeah. I gotcha."
    "As we continued to walk up the forested path, the canopy eventually gave way to a view of the horizon."
    MC "H-Holy crap!"
    BE "Just noticed the mountains, eh?"
    MC "Well, I saw them from the boat! But, oh my God!"
    BE "You can get a better view from the front of the school. There's a trail headed to the front."
    MC "Aren't we supposed to enter through the back entrance?"
    BE "Naaah, it'll be fine! The gates are cool anyway! C'mon!"
    "Taking Honoka's squirrel route, we ended up walking along the edge of the forest along the hillside until we reached the front gates."
    BE "Ah! We're here!"
    scene School Front with fade
    stop music
    "Before I realized it, we had arrived at a huge school building. This was Seichou Academy."
    "This would be my new home for the next year. It was really awe-inspiring at the time."
    jump global000_GTS

label global000_GTS:
    scene black with dissolve
    play music GTS
    "As we entered the school grounds, I couldn't help but notice how big everything was."
    scene School Planter with dissolve
    "What looked to be normal-sized buildings turned out to be a trick of perspective."
    "As Honoka and I walked and walked, the school seemed to grow before my eyes."
    "The doors became large and imposing, the floors far taller than normal, everything just seemed to be super-sized at Seichou Academy."
    UNKNOWN "Aaah!"
    "Honoka and I looked down to see a pair of legs flailing over the edge of one of the planters lining the building."
    show cg GTS000 with dissolve
    "We approached the small garden just as the student extracted themselves from the planter, dusting the dirt from her skirt."
    UNKNOWN "Oooh, darn..."
    BE "Are you okay?"
    UNKNOWN "Eeep!"
    "The pale-skinned girl turned to us, looking briefly terrified.\nShe was wearing a skirt and short-sleeved shirt."
    UNKNOWN "Yes, sorry. I just fell. The planters are just rather large."
    UNKNOWN "I can't reach the middle of the bed without crawling on the outer ones..."
    "She gestured behind her, and we could see inside the planter were several rows of vegetables, the tops of radishes and carrots and the like poking through the soil."
    "Aside from the divot where she fell, the center row of vegetables did indeed look less well-watered than the ones closest to the edge."
    hide cg
    show GTS sad at Position(xpos=0.75, xanchor=0.5)
    show BE surprised at Position (xpos=0.25, xanchor=0.5)
    with dissolve
    menu:
        "That's dumb, whose idea was that?":
            jump global000_GTS_c1
        "Do you need help?":
            jump global000_GTS_c2

label global000_GTS_c1:
    MC "That's dumb, whose idea was that? Why plant stuff where people can't reach?"
    UNKNOWN "It may be easier for someone who is taller..."
    show BE neutral
    BE "Hey, you're plenty tall enough! Don't be down on yourself, miss... Uh..."
    GTS "Oh, I'm sorry, I forgot entirely! My name is Naomi Yamazaki."
    "She bowed, and we returned the gesture."
    BE "I'm Honoka Inoue, nice to meet you. This is Keisuke Hotsure."
    MC "Nice to meet you."
    GTS "Well, I've done as much as I can today, it seems. I'll leave the rest to the groundskeepers."
    GTS "I'll see you all at orientation tomorrow."
    show BE happy
    BE "Goodbye! See you around!"
    hide GTS with dissolve
    BE "..."
    show BE neutral at altMove(0.5, 0.5)
    BE "...Boy, that's kind of a fancy lady to be kneeling in the dirt, don't you think?"
    "I nodded, and we continued on to the front doors of the school."
    jump global000_AE

label global000_GTS_c2:
    MC "Do you need help?"
    show GTS happy
    UNKNOWN "Oh, thank you, that'd be lovely. Here, let me give you the can..."
    $setAffection("GTS", 1)
    "I leaned way over the planter and watered the middle row of plants, having to stretch as far as I could reach but managing to get all of them."
    show BE neutral
    show GTS unique
    GTS "Thank you so much! Oh, I'm sorry, I didn't even introduce myself properly. My name's Naomi Yamazaki."
    "She bowed, and we returned the gesture."
    show BE neutral
    MC "I'm Keisuke Hotsure, and this bundle of smiles here is Honoka Inoue. Nice to meet you."
    show BE happy
    BE "Hi there!"
    GTS "Well, it's been a pleasure."
    GTS "Perhaps I'll see you around school?"
    MC "Yeah, sure."
    BE "Yeah! See you later!"
    hide GTS with dissolve
    BE "..."
    show BE neutral at altMove(0.5, 0.5)
    BE "Well that was nice of you to help her, Kei-chan!"
    $ setAffection("BE", 1)
    "I nodded, and we continued on to the front doors of the school."
    jump global000_AE

label global000_AE:
    scene black with dissolve
    UNKNOWN "YOU..."
    "With only a single word, Honoka and I stopped in place as a deep paralyzing chill ran down my spine..."
    "When we caught our bearings{w} (and Honoka's bust stopped jiggling){w} the owner of the voice passed us from behind. Though I didn't see her face, my jaw nearly dropped when I got a look at her behind..."
    scene Gate Front with dissolve
    UNKNOWN "Mizutani-san, what do you think you're doing?"
    play music FMG
    show cg AE000 with dissolve #show AE angry at Position(xpos=0.75, xanchor=0.5) with vpunch
    FMG "Check it out!"
    "Around the corner came a tanned girl somehow managing to carry a wooden bench under each arm, her short-sleeved shirt baring her defined muscles for all to see."
    #show FMG neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    FMG "I was getting two benches at once! I thought you'd like me getting twice what ya asked!"
    UNKNOWN "Not if it takes you three times as long."
    #hide AE with dissolve
    #hide FMG with dissolve
    #show BE surprised at center with dissolve
    BE "Oh boy... I feel awkward just standing here..."
    #hide BE with dissolve
    hide cg with dissolve
    show AE angry at Position(xpos=0.75, xanchor=0.5)
    show FMG neutral at Position (xpos=0.25, xanchor=0.5)
    with dissolve
    menu:
        "She was just trying to help...":
            jump global000_AE_c1
        "You should listen to your boss, you know.":
            jump global000_AE_c2
        "(Do nothing)":
            jump global000_AE_c3

label global000_AE_c1:
    MC "She was just trying to help...{w} No need to be mean."
    $setAffection("BE", 1)
    $setAffection("FMG", 1)
    $setAffection("AE", -1)
    UNKNOWN "Hm?"
    MCT "I'm going to die. I've only been here a day and I'm going to die."
    UNKNOWN "And just who are y-?"
    show FMG upbeat
    FMG "Yeah, Matsumoto, get that stick out of your huge butt."
    "At that, the girl's attention turned back from me to the girl behind her."
    "It was hard not to notice the very prominent backside on her otherwise stiff and lithe frame."
    AE "..."
    show AE angry-3
    AE "Do you really think it wise to speak to your class representative in such-"
    hide FMG with dissolve
    show BE confused at Position (xpos=0.25, xanchor=0.5) with dissolve
    BE "You're class rep already? But I thought classes didn't start until tomorrow."
    show AE neutral-annoyed
    AE "I was granted the position along with my internment here. The school expects much of my abilities, and I expect to live up to those expectations..."
    show BE doubt
    BE "(Keisuke, this girl is kinda scary...)"
    show AE neutral
    AE "I can only assume you two are Honoka Inoue and Keisuke Hotsure?"
    MC "Huh? How did you-"
    show AE neutral-eyebrow
    AE "Your appearance matches your files..."
    MC "Oh, well, um... Yeah, we're in room 3-B?"
    AE "Then listen well. Go to room 3-B and make sure Kodama-san and Nikumaru-san have the first-day decorations put up properly."
    show AE angry
    AE "Nikumaru fancies herself a negotiator. I don't have faith in her abilities to work well with others."
    MC "Er, okay, sure."
    hide AE with dissolve
    show BE doubt
    "Turning around once more, she continued to go about her business, and we made sure to get out of there as soon as possible."
    "Honoka and I looked at each other and headed for class 3-B."
    jump global000_WG

label global000_AE_c2:
    MC "You should listen to your boss, you know."
    MC "If she's got a plan, going off on your own doesn't really help."
    $setAffection("FMG", -1)
    show FMG angry
    FMG "My WHAT? Matsumoto's not the boss of anyone, despite what she'll tell you."
    show AE neutral
    AE "I've told no-one anything of the sort, you offered to lift and I obliged-"
    FMG "Yeah, yeah, yeah. Listen, you two in 3-B? Might as well get up there and help."
    FMG "Whatever the princess and her pet're doing can't be as bad as having lard-butt boss you around..."
    hide FMG with dissolve
    "Matsumoto shot daggers at Mizutani as she left to get more benches, then turned to regard me with a glare."
    show AE neutral-annoyed
    AE "There was no reason to get yourself involved in that. "
    MC "I-I just thought-"
    AE "You thought wrong."
    show AE neutral
    AE "...My apologies, but I can handle things on my own."
    AE "Now, if you will, please get up to 3-B and help with the decorations and cleaning."
    "Honoka and I quickly fled the scene before the temperature dropped so low as to be freezing."
    jump global000_WG

label global000_AE_c3:
    "I didn't want to get involved in the fight. {w}Especially after seeing Mizutani lift one of those big wooden benches under each arm."
    UNKNOWN "Look, it doesn't matter if you bring all the benches at once if I can't get them organized properly."
    UNKNOWN "One at a time lets us get each one in its place and ready for the next without-"
    show FMG sad
    FMG "All right, all right, I get it, sheesh. Don't get your panties in a bunch, Matsumoto..."
    show FMG happy
    extend " with a butt that size, you'll never fish 'em back out."
    hide FMG with dissolve
    "Matsumoto shot daggers at Mizutani with her eyes until she left to get more benches, then she turned to me in a huff."
    "My eyes snap to hers, momentarily mesmerized by just how sizable her rear was underneath the school-issue uniform."
    $setAffection("AE", 1)
    show AE neutral
    AE "Thank you for waiting. Was there something you needed?"
    MC "Oh, y-yeah... no worries. I just got here, and we were looking around is all."
    AE "I see."
    "Frigid was the closest word I could use to describe this girl. Her admittedly comedic backside completely betrayed her cold, piercing eyes."
    AE "I am Shiori Matsumoto. I will be your sitting Student Council President during your stay here."
    MC "Nice to meet you. I'm Keisuke Hotsure, class 3-B."
    AE "Is that so?"
    MC "M-Mhm..."
    AE "Then I suppose that means I will also be your class representative. Would you like a tour of our facilities?"
    MC "Ah, n-no thanks, ma'am. My friend here is helping out."
    AE "Then perhaps you could check on the students I sent to prepare the room while you're there? I sent one, however I doubt her... resolve, so to speak."
    MC "Understood."
    hide AE with dissolve
    show BE neutral at center with dissolve
    BE "You think she's ever happy with anyone? Doesn't seem the type..."
    jump global000_WG

label global000_WG:
    scene black with dissolve
    "We left the arguing pair behind and entered the school proper.{w} Honoka led me through the hallways with ease, until we came to one classroom in particular..."

    scene Classroom with dissolve
    play music WG
    "So this was Classroom 3-B. I would be spending a lot of time here for the next year."
    "The first thing I noticed was that, much like the rest of the school, the classroom seemed very big. It was much larger than any that I had been in before."
    "Whether or not this meant that there would be more students, or if this was just some unique design concept for a classroom, I had no idea."
    "The next thing I noticed was that Honoka and I weren't alone in the room. Sitting across from us, at the head of the classroom, was another girl."
    show cg WG000 with dissolve
    "She had a round face, and bright blue eyes framed by gold colored hair.{w} It seemed as though we had a foreigner in our midst."
    "She was leaning back against one of the desks, looking pretty satisfied with herself, for whatever reason."
    "She casually turned her gaze, perking her eyebrows up in interest as she saw us enter, but not so interested as to move from her comfortable position."
    UNKNOWN "Oh? What have we here? I guess that Shiori told you to come up here too?"
    UNKNOWN "Not to worry, I have everything under control here."
    BE "Who are you?"
    hide cg with dissolve
    show WG neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    WG "I'm Alice Nikumaru.{w} Charmed, I'm sure."
    "After introducing herself, Alice sat back down on her makeshift throne. Before I could open my mouth to speak, she looked past us."
    show WG angry
    WG "Do try to hurry now, if you'd please."
    WG "I would like to go get something to eat, but I'll miss the opportunity if we tarry any further."
    hide WG
    show PRG neutral at Position(xpos=0.75, xanchor=0.5)
    with dissolve
    "I followed Alice's gaze. Across the room, another girl was walking awkwardly, a large globe in her arms."
    show PRG sad-2
    UNKNOWN "{size=-6}I-I'm sorry.{/size}"
    show BE happy at Position (xpos=0.25, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    BE "Oh, hello!"
    BE "I'm Honoka Inoue! Pleased to meet ya!"
    MC "Keisuke Hotsure. Nice to meet you."
    show PRG neutral
    PRG "...M-My name is Aida Kodama."
    hide BE
    show WG stern at Position (xpos=0.25, xanchor=0.5)
    with dissolve
    WG "Great, great.{w} Now everybody knows everybody, and Aida can finish decorating. She's almost done anyway."
    menu:
        "Well, if you've got this under control...":
            jump global000_WG_c1
        "Shouldn't you be doing something too?":
            jump global000_WG_c2

label global000_WG_c1:
    MC "Well, if you've got this under control, I guess I'll be going then."
    $setAffection("WG", 1)
    $setAffection("PRG", -1)
    $setAffection("BE", -1)
    WG "Glad to see at least someone can follow orders."
    show BE surprised at center with dissolve
    BE "{i}Kei-chan{/i}!"
    "I winced. I might not have seen Honoka for years, but I remembered that tone well enough."
    hide BE with dissolve
    MC "Okay, okay. We'll help too."
    show PRG sad
    PRG "... Y-You don't have to. It's okay..."
    WG "Hmph. {w}Well, if you insist, I'm sure I can find something for you to do. {w}The sooner we're done here, the better."
    jump global000_RM

label global000_WG_c2:
    MC "Shouldn't you be doing something too?"
    $setAffection("WG", -1)
    $setAffection("PRG", 1)
    show WG neutral at Position (xpos=0.25, xanchor=0.5)
    WG "I am doing something!"
    show WG happy
    WG "I'm su{w}per{w}vi{w}sing!"
    show BE neutral at center with dissolve
    BE "Supervising? There's only two of you..."
    show WG haughty
    WG "I did the work of figuring out an optimal floor plan for furniture and composition of decorations. That was my half I did earlier. Now Aida is doing her half."
    PRG "It's okay...{w} I-I can do this myself."
    MC "It's fine. We're all supposed to be working together, right?"
    show PRG happy
    PRG "W-Well, yes. But..."
    MC "But, nothing. We're helping."
    PRG "Oh! Uhm..."
    PRG "T-Thank you! T-Thank you very much!"
    jump global000_RM

label global000_RM:
    scene Hallway
    show BE neutral
    with fade
    stop music
    BE "All right, well, it looks like everything's ready for tomorrow...{w} (No thanks to queenie over there.){w} Time to get back to the dorms, I guess!"
    MC "They wouldn't happen to be co-ed, would they?"
    show BE happy
    BE "Oh, Kei-chan! You're such a kidder!{w} Of course not!"
    "Honoka's laugh caused her impressive bust to shake violently, which was a small consolation prize as we parted ways."
    hide BE with dissolve
    scene black with fade
    pause 1
    scene Dorm Exterior with fade

    "I headed over to the boy's dormitories, noticing that they were just as enlarged as the rest of the school."
    "On my walk over, I slid my phone out of my pocket."
    MCCell "Hey, get yourself situated okay?"
    "A moment later, my phone buzzed in my hand."
    $setAffection("TM", 1)
    TomokoCell "Yeah."
    MCCell "Good. Meet your roommate yet?"
    scene Dorm Hallway with fade
    "Another few steps, capped off with a vibrate."
    TomokoCell "Mhm."
    MCCell "Cool. Let me know if you need anything."
    pause .5
    TomokoCell "K"
    "I put my phone back in my pocket and walked up to the dorm that had been assigned to me."
    "I felt like a literal child, trying the doorknob that I couldn't even get my entire hand around."
    pause .5
    "*Kunk-Kunk*"
    MCT "Right. Doors generally lock."
    play music RM
    show cg RM000 with dissolve
    UNKNOWN "Who is it?!"
    MC "Agh?!"
    UNKNOWN "Who is it? Who are you with? Identify yourself!"
    menu:
        "Uh... Pizza delivery?":
            jump global000_RM_c1
        "Keisuke Hotsure. I... think this is my room?":
            jump global000_RM_c2
        "Don't worry, sir. I'm from the government, just making an inspection!":
            jump global000_RM_c3

label global000_RM_c1:
    MC "Uh...{w} Pizza delivery?"
    UNKNOWN "I didn't order any pizza!{w} Scram!"
    MC "Hahaha... It was just a joke, this is my dorm room.{w} I guess you're my roommate?"
    UNKNOWN "This is your dorm?{w} Are you sure?"
    MC "Preeeetty sure...{w} Says right here on my paperwork, see?"
    "I pulled out my transfer documents from the top pocket of my luggage, but he snatched them away before I could even unfold them."
    "The door shut briefly, then opened again, the boy inside still glaring at me through one narrowed eye."
    UNKNOWN "Keisuke Hotsure... {w}Let's see some ID."
    MC "Haha, no way, really?"
    UNKNOWN "Really."
    "Just wanting to get inside and get things over with, I sighed and handed over my ID."
    "More squinting, and then finally he opened the door all the way."
    hide cg with dissolve
    show RM neutral with dissolve
    RM "All right, you check out...{w} My name's Daichi Utagashi."
    $setAffection("RM", -1)
    scene Dorm Interior
    show RM neutral
    with fade
    jump global000_RM_after

label global000_RM_c2:
    MC "Keisuke Hotsure. I...{w} think this is my room?"
    UNKNOWN "Hotsure, huh?{w} Let's see some ID."
    MC "Haha, no way, really?"
    UNKNOWN "Really."
    "Just wanting to get inside and get things over with, I sighed and handed over my ID."
    "More squinting, and then finally he opened the door all the way."
    hide cg with dissolve
    show RM neutral with dissolve
    RM "All right, you check out...{w} My name's Daichi Utagashi.{w} Come in, I don't like leaving the door open."
    scene Dorm Interior
    show RM neutral
    with fade
    jump global000_RM_after

label global000_RM_c3:
    MC "Don't worry, sir. I'm from the government, just making an inspection!"
    hide cg with dissolve
    "I thought my fake-authoritative voice would have been at least worth a laugh, but the door slammed shut in my face."
    "I knocked again with more force, but only received silence in return."
    "I put my ear against the door, though all I heard was movement followed by the occasional slamming sound."
    "Sighing, I reached into my pocket and dug through random pocket junk until I felt the cold, blunt edge of my key."
    "Producing it, I shoved it into the lock and turned it."
    show cg RM000_escape1 with dissolve
    "Rather than being shoved out of the room and cussed straight off of campus, I opened the door to find the door slammer hurling an enormous suitcase straight over the balcony. Beside him were two more large bags, primed and ready for tossing."
    MC "Whoa, whoa! Can we just talk for a sec? I'm not with the-"
    show cg RM000_escape2 with dissolve
    RM "That's what you want me to think! I'm not for it! Daichi Utagashi will not go down without a fight!"
    "He leaned down and clutched two more bags, a mess of papers and cloth sticking through one of the zippers."
    "Daichi leaned over to throw one, and in a panic...{w} slipped and threw himself straight over the edge, somehow managing to catch the rail in one flailing hand."
    show cg RM000_escape3 with vpunch
    RM "Gah! Rgh, dammit!"
    "I heard the sound of the bag hitting the ground, but all I saw was his knuckles ratcheted onto the railing."
    MC "Calm down for a second! I promise I'm not with the government!"
    RM "D-Don't even start!"
    MC "Okay, if I really was out to get you, would I have just revealed myself in plain conversation like that?"
    pause .5
    RM "You do have a point there."
    pause .25
    RM "Okay, help me get back over! But don't you dare try {i}anything{/i}!"
    "I dropped my bags at my feet and hurried over, grabbing his wrist firmly with one hand and his shoulder with the other."
    MC "Ngh..."
    pause .5
    show dummy with vpunch
    MC "Ragh!"
    "I pulled with all my might, and yanked Daichi up enough where he could get his footing."
    "He threw himself back over the railing and landed in a heap on the floor, breathing like an olympic athlete."
    scene Dorm Interior
    show RM angry
    with fade
    RM "Bah... hagh... eh..."
    MC "You're... hah... you're welcome."
    show RM distrustful
    RM "Alright... let's... see some ID."
    MC "... Seriously? I save you from falling and {i}that's{/i} your opening line?"
    show RM doubt
    RM "Card. Now."
    "I huffed and yanked my wallet out of my back pocket, pulling out my ID."
    pause .25
    RM "Hmph..."
    pause .5
    show RM distrustful
    RM "Don't get any funny ideas, \"Keisuke Hotsure.\" I've got my eye on you..."
    $setFlag("RM_govagent")
    $setAffection("RM", -2)
    jump global000_RM_after

label global000_RM_after:
    "When I finally got inside, it was obvious Daichi had claimed half of the room for himself.{w} Half the furniture had been crammed into one corner of the room, with blankets and sheets erected into a kind of tent over his desk and dresser."
    show RM neutral with dissolve
    MC "Er, so, do you want to-"
    show RM distrustful
    RM "Do you know why you're here?"
    MC "Er, what?"
    RM "Why you're here, at this school?"
    MC "Well, I got the letter..."
    show RM doubt
    RM "Right after your health exam, right?"
    MC "Uh... yeah? Close to it, anyway."
    RM "Hmph. Just as I thought."
    MCT "What's this guy's deal?"
    show RM concerned-2
    RM "Haven't you ever seen those people on the news?{w} The giants over 300 centimeters tall,{w} the gravure idols with 40kg breasts,{w} all the record holders for biggest this and longest that?"
    "Thinking back on it, I had seen some reports, starting when I was a little kid."
    "It wasn't often, but every now and then there'd be some picture or other of a giant-sized man or woman, always Japanese."
    MC "I... Yeah, I guess?"
    RM "If you look into the histories and records of all these people, one thing is common to all of them-{w} they {i}ALL{/i} went to school at Seichou Academy after graduation!"
    MC "So, what are you saying?"
    show RM distrustful
    RM "I'm saying the government brings certain students here and-{w} and does {i}something{/i} to them!"
    show RM angry
    RM "This kind of growth isn't natural,{w} it's statistically impossible for all of these one-in-a-million conditions to keep happening {i}just{/i} to Japanese school-age teens!"
    show RM distrustful
    "I sat down on my bed, lost in thought.{w} Daichi certainly seemed to have a few screws loose, but then again,{w} why {i}had{/i} my sister and I been sent to this school with so few details?"
    "I had just accepted it as some new schooling program, like the papers had said, but now?"
    "I never paid much attention to the news, but if every one of those reports and articles over the years could be traced back to Seichou Academy,{w} that was definitely something to wonder about."
    scene black with dissolve
    stop music fadeout 1.0
    pause 1
    MCT "What have my sister and I gotten ourselves into...?"
    scene white with dissolve
    play sound AlarmClock
    "{color=#FF0000}BREEET BREEET BREEET BREEET!{/color}"
    scene Dorm Interior with dissolve
    play music Peaceful
    "I was startled awake by a shrill electronic alarm clock. I looked around confused for a moment, before remembering where I was."
    MCT "Hard to believe that just yesterday I was in my hometown, and now I'm off on this little island..."
    "I got up and got into my uniform, doing my best to comb my shaggy hair into something approaching proper. In the corner of my eye I saw Daichi watching me."
    if checkAffection("RM", ">=", 0):
        show RM neutral
        RM "Today's the welcoming ceremony. I'm going to go get the lay of the campus."
        MC "You're going to skip the opening ceremony?"
        show RM angry
        RM "Of course not.{w} I need to get the official story so I know where to start investigating."
        hide RM with dissolve
        "I shook my head, but waved goodbye nonetheless as Daichi left. At least he seemed in good spirits."
        $ setFlag("global000_RM_friendly")
        jump global000_part2
    else:
        show RM sad
        "As soon as he realized I'd noticed him, he spun on his heel and headed out the door."
        hide RM with dissolve
        "I looked after him, puzzled, but after yesterday's oddness I figured this was the sort of behavior I could look forward to all year."
        jump global000_part2

label global000_part2:
    scene Campus Center with fade
    MCT "It's way too quiet here. No cars honking. No people shoving past you. Nothing like the city at all."
    "As I followed the signs to First Day Welcoming, I couldn't help but notice how flat the campus seemed. Despite the large buildings, most of them were divided into a handful of floors at most."
    "Also, there didn't seem to be any stairs anywhere. Any dips or slopes in the elevation were all traveled with ramps."
    scene Auditorium with dissolve
    "When I finally reached the auditorium, I found I was still early enough to have my choice of seats."
    $setTomoOutfit(OutfitEnum.DEFAULT)
    show Tomoko neutral with dissolve
    "I spotted my sister all uniformed up, walking toward one of the back rows."
    MC "Hey, Tomo!"
    Tomoko "Oh, hey."
    MC "How was your first night?"
    Tomoko "Fine."
    Tomoko "My roommate talks a lot."
    MC "Well, do you two get along at least?"
    show Tomoko annoyed
    Tomoko "Yeah. She talks and I kind of just nod."
    MCT "Seems accurate enough."
    show Tomoko neutral
    MC "Right, well. I'll see you around, Tomo."
    Tomoko "Yeah. Later."
    hide Tomoko with dissolve
    "My sister walked off and took a spot in the back row off to one side."

label global000_sitmenu:
    MCT "Now... where should I sit...?"
    menu:
        "I should sit in the front where I can see.":
            jump global000_sit_c1
        "I should sit somewhere in the middle.":
            jump global000_sit_c2
        "I should sit in the back, where no one will notice me.":
            jump global000_sit_c3

label global000_sit_c1:
    "I decided to sit in the front row, where the principal could see me. If I ever needed to speak with him, recognizing my face might make him better disposed toward me."
    MCT "This is a good seat... Got spaces on either side of me."
    play sound Boing
    "{color=#FF69B4}*FLUMPH!*{/color}"
    MCT "!!"
    MCT "I... Is that..."
    show AE neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    MCT "Shiori's butt is overflowing her seat and pushing against me...{w} I can't say anything about it with everyone else around..."
    MCT "I'll just quietly scoot away from her-"
    play sound Boing
    "{color=#FF69B4}*PLOMF!*{/color}"
    MCT "Oh no!"
    show WG neutral at Position(xpos=0.25, xanchor=0.5) with dissolve
    MCT "Alice! She's taking up all of her seat and half of mine! What do I do??"
    MCT "I'm in the middle of a womanly butt-sandwich and it's like I'm the only one to notice! I've got to distract myself before something even more embarrassing happens!" #with Shake((0, 0, 0, 0), 0.75, dist=20)
    menu:
        "So, Matsumoto-san...":
            jump global000_sit_c1_1
        "Hi there, Nikumaru-san...":
            jump global000_sit_c1_2
        "Maybe I should sit elsewhere?":
            "I decided to look around just in case there were any other available spots left elsewhere."
            hide AE
            hide WG
            with dissolve
            jump global000_sitmenu

label global000_sit_c2:
    "I decided to sit in the middle of the auditorium, where I could still hear the speeches without being so front-and-center."
    MCT "Let's see, somewhere around here should be-"
    BE "Pssst! Kei-chan!"
    show BE happy at Position(xpos=0.25, xanchor=0.5) with dissolve
    MC "Honoka?"
    BE "Kei-chan, over here! I've got a seat saved for you!"
    "I made my way down the row of chairs to the seat Honoka was patting next to her."
    "I noticed when I passed by Honoka, she had to lean back slightly to keep her bosoms from dragging across me, and the thought made me blush."
    "When I sat down and let the breath I'd been holding out, I realized I was sitting next to the girl we'd met gardening the evening before."
    show GTS neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    show BE happy
    BE "Isn't this great, Kei-chan? It's just like grade school again!"
    GTS "You two... went to school together?"
    show BE neutral
    BE "Oh, hey there Yamazaki-san! Yeah, when we were kids we went to the same school. Different middle schools, though."
    menu:
        "Find your dorm okay, Honoka?":
            jump global000_sit_c2_1
        "What was your previous school like, Yamazaki-san?":
            jump global000_sit_c2_2
        "Maybe I should sit elsewhere?":
            "I decided to look around just in case there were any other available spots left elsewhere."
            hide GTS
            hide BE
            with dissolve
            jump global000_sitmenu

label global000_sit_c3:
    "I decided to sit in the back, where I wouldn't have to worry about anyone seeing me."
    show FMG neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    "The back rows were sparsely filled, so much so that I saw Mizutani-san could afford to hang her toned arms off of the backs of the chairs on either side of her."
    "The rest of the row was nearly empty, save for a small girl in the corner who I recognized from the night before as Aida."
    show PRG neutral at Position(xpos=0.25, xanchor=0.5) with dissolve
    "I also noticed she was looking at me, but as soon as our eyes met she turned away...{w} before slowly turning back to watch me from the corner of her eye."
    menu:
        "Needed the room to stretch out, Mizutani-san?":
            jump global000_sit_c3_1
        "Seems kinda lonely back here, Kodama-san...":
            jump global000_sit_c3_2
        "Maybe I should sit elsewhere?":
            "I decided to look around just in case there were any other available spots left elsewhere."
            hide FMG
            hide PRG
            with dissolve
            jump global000_sitmenu


label global000_sit_c1_1:
    $setFlag("global000_sitAE")
    hide WG with dissolve
    MC "So, Matsumoto-san..."
    show AE neutral at altMove(0.5, 0.5)
    "Wordlessly, she glared at me through the side of her eye before looking back to the stage and nodding."
    AE "The ceremony is about to begin, sir."
    MC "I know, but I was just, ah, wondering-"
    AE "Quiet..."
    MC "M-Mhn..."
    "A compulsion. I wasn't even purposefully following her orders, it was more like a compulsion. Either way, my head snapped to attention as I noticed the principal and a handful of faculty on stage."
    "It definitely seemed sparse, despite the size of the stage, but I wasn't about to attribute it to anything nefarious like Daichi would."
    AE "...Though I do appreciate you coming up to pay attention to the administrators. It's an important first step."
    "I opened my mouth to try and ask about the ass-squishing she was giving me, but the principal clearing his throat into the microphone called attention to the room."
    MCT "No use talking now, I suppose... but it's nice she thought I was clever enough to notice."
    $ setAffection("AE", 1)
    jump global000_sit_after

label global000_sit_c1_2:
    $setFlag("global000_sitWG")
    hide AE with dissolve
    MC "Hi there, Nikumaru-san..."
    show WG neutral at altMove(0.5, 0.5)
    WG "Just call me Alice, please, no need to be so formal. In the west, it is unheard of for students to refer to classmates by their surnames."
    MC "Ah, so, uh, Alice..."
    WG "Hm?"
    MC "Well, your seat- ah, I mean, the seat, it's a little..."
    show WG happy
    WG "Hm? Yes, I do suppose they are quite tacky. It's hard to imagine that they could have picked something that could clash with the present setting more than this. I take it you have a flair for design yourself?"
    MCT "Uh, that's not what I was getting at, but on second thought..."
    MCT "This is much less awkward to explain than calling attention to the fact she's taking up more than her fair share of the space as I squeezed in next to her."
    MC "I guess you could say so."
    show WG neutral
    WG  "Oh? Quite interesting. Hmm, it appears they are starting. Very well, let's get this over with."
    $setAffection("WG", 1)
    jump global000_sit_after

label global000_sit_c2_1:
    $setFlag("global000_sitBE")
    hide GTS with dissolve
    MC "Find your dorm okay, Honoka?"
    show BE happy at altMove(0.5, 0.5)
    BE "Yep! It's amazing how big it is...{w} Makes my bedroom at home look like a closet!"
    MC "Yeah, and for new students, even!"
    show BE neutral
    BE "But you know what's weird? I haven't seen a single upperclassman yet. Like, not anywhere. They're all starting today, right? Aren't they?"
    MC "I don't know, really. Maybe this is some kind of half-day for upperclassmen, they start later than us?"
    show BE surprised
    BE "That could be! I've never heard of a school doing that on the first day, though..."
    MC "I'm sure they'll explain it to us in homeroom. Hopefully we can get seats next to each other!"
    show BE happy
    BE "Yeah! That'd be great, Kei-chan! Just like old times!"
    MC "Shhh, not so loud, they're starting! But yeah, just like old times..."
    $setAffection("BE", 1)
    jump global000_sit_after

label global000_sit_c2_2:
    $setFlag("global000_sitGTS")
    MC "What was your previous school like, Yamazaki-san?"
    show GTS neutral
    GTS "Mine?"
    MC "Sure, you heard about ours..."
    show BE neutral
    BE "Yeah, what was yours like, Yamazaki-san?"
    show GTS neutral
    GTS "Well, ah, it was...{w} pleasant, I suppose."
    MC "\"Pleasant\"?"
    GTS "That is, ah...{w} It was rather...{w} Mm...{w} My old schools were always very well organized and regimented."
    MC "...Not very fun, then?"
    show GTS happy
    GTS "They had a wonderful garden in the back."
    MC "Well, hopefully this school will be fun for you."
    show BE happy
    BE "Yeah! We'll do all we can to make sure you have at least one fun school!"
    show GTS happy
    GTS "...Thank you, both of you. Now, we mustn't be speaking once the principal starts..."
    $setAffection("GTS", 1)
    jump global000_sit_after

label global000_sit_c3_1:
    $setFlag("global000_sitFMG")
    hide PRG with dissolve
    MC "Needed the room to stretch out, Mizutani-san?"
    show FMG neutral at altMove(0.5, 0.5)
    FMG "Oh hey, it's, uh, Hotsure, right?"
    MC "Yep! So, ah, not interested in the speech?"
    FMG "Eh, whatever, I don't mind. Just like the back because I hate being squeezed between people. Gets a little claustrophobic."
    MC "Yeah, and like, on the trains..."
    show FMG happy
    FMG "Oh I know, those are even worse! Especially for a tall girl..."
    MC "I hope no one's ever given you trouble..."
    show FMG neutral
    FMG "Heh heh...{w} One guy tried to cop a feel, once."
    MC "What happened?"
    "Mizutani's smile tightened into a predatory, self-satisfied grin."
    show FMG flex
    FMG "Busted his finger. Wasn't even trying to."
    MCT "Ooooo-kay, I'm suddenly very interested in what the principal has to say..."
    $setAffection("FMG", 1)
    jump global000_sit_after

label global000_sit_c3_2:
    hide FMG with dissolve
    $setFlag("global000_sitPRG")
    MC "Seems kinda lonely back here, Kodama-san..."
    show PRG sad at altMove(0.5, 0.5)
    PRG "Oh! Uhm... I-I guess..."
    PRG "B-But, there's three of us here now."
    MC "Heh. Yeah, you're right."
    MC "Would you mind if I sat by you?"
    show PRG surprised
    PRG "Uh... n-not at all!"
    MCT "Geez. It's like she's never spoken before."
    pause .25
    MC "So... nervous about starting at a new school?"
    PRG "A little...{w} yeah."
    MC "I can relate to that. It is definitely different."
    PRG "Yeah..."
    pause 1
    "Aida went quiet."
    MCT "Well... guess that's all."
    "I sat back and took a deep breath, while I waited for the ceremony to get under way."
    $setAffection("PRG", 1)
    $setFlag("global1000_aidasit")
    jump global000_sit_after

label global000_sit_after:
    hide PRG
    hide WG
    hide GTS
    hide FMG
    hide AE
    hide BE
    with dissolve
    "The ceremony continued, all dreadfully familiar and rote, but at the end there was something different. The principal settled the papers behind the podium and hesitated for a too-long moment."
    Principal "Thank you to each and every one of you for your attendance today. My name is Manabu Noguchi, and I'm the principal of this academy."
    Principal "The future is forever uncertain. But no matter what the future holds, years hence or any day now, one thing is important above all else."
    Principal "\"Nosce te Ipsum.\" {w}Latin, \"To thine own self be true\". Remember that you are more than your station, {w}skills, {w}and especially appearance. If you need help, your teachers are always available to help you with whatever you need."
    Principal "I'm sure you all have many questions as to why you're here. And, I assure you that the rest of the faculty and I will do our best to answer all of those for you."
    Principal "Now, each of you have been assigned a homeroom teacher. They will give you more information during class in a few minutes."
    Principal "Feel free to reach out to them should you need to. As is the same with every member of our faculty, they're here to help."
    MCT "What's he going on about...? I'm beginning to wonder if Daichi was on to something..."
    "Finally, the ceremony ended, and we all began to file out."
    stop music
    show AE neutral with dissolve
    play music AE
    "I saw Shiori hustle out to stand by the doors ahead of nearly everyone else, her rear wobbling side to side in a way that was impossible to not draw the eye."
    MC "Matsumoto-san? What's going on?"
    show AE neutral-annoyed
    AE "A more apt question would be \"Where is Utagashi-san\"? This assembly is mandatory."
    AE "He's your roommate, is he not?"
    menu:
        "I haven't seen him...":
            jump global000_aftersit_c1
        "He said he wouldn't miss the ceremony..." if getFlag("global000_RM_friendly"): #This menu item will only appear if this variable is True
            jump global000_aftersit_c2
        "He left the dorm pretty early..." if not getFlag("global000_RM_friendly"): #Likewise, this item only appears if the variable is False
            jump global000_aftersit_c3


label global000_aftersit_c1:
    $setFlag("global000_RMUnknown")
    MC "I haven't seen him..."
    MCT "He was acting kind of strangely this morning. No telling where he went off to."
    show AE neutral
    AE "Well... I certainly have no reason not to trust you, so that's that."
    hide AE with dissolve
    "I left to go to my homeroom class, worrying no excuse would be good enough for Shiori..."
    $setAffection("RM", 1)
    jump global000_homeroom

label global000_aftersit_c2:
    $setFlag("global000_RMCover")
    MC "Well, he said he was going to make sure not to miss the ceremony..."
    show AE neutral
    AE "I've accounted for every student that came through this door. He wasn't one of them?"
    MC "He said he was going to walk around campus a bit this morning, get a feel for the place. Maybe he came in some different door?"
    "Shiori looked back into the mostly-empty auditorium, eyes scanning the walls."
    AE "Unlikely... but possible. Please, keep an eye on your roommate. I'll have to have a word with him when I can..."
    hide AE with dissolve
    "She nodded and left her post, satisfied with the answer, and we both walked to homeroom."
    $setAffection("AE", 1)
    $setAffection("RM", 1)
    jump global000_homeroom

label global000_aftersit_c3:
    $setFlag("global000_RMLeft")
    MC "He left the dorms pretty early, don't know where he was off to..."
    show AE neutral
    AE "Perhaps I need to pay him a visit, then, hm?"
    MC "A-Ah."
    AE "In any case. Thank you for your cooperation."
    hide AE with dissolve
    "With a derisive grunt, Shiori left her post by the doors and we walked to homeroom together."
    $setAffection("AE", 1)
    $setAffection("RM", -1)
    jump global000_homeroom

label global000_homeroom:
    scene School Exterior with fade
    play music Schoolday
    "With the principal's strange welcome still echoing in my ears, I headed for the class building, ready to start my academic career at Seichou Academy..."

    scene Hallway with fade
    "It was very strange to be in the hallways with so few people. Well, there were a normal amount of students, but in Seichou's oversized architecture we all felt miniscule."
    "I spied Honoka and some of my other classmates as we walked along, feeling like ants in a dog carrier."
    show BE surprised
    BE "Just how many students are there here, that they need such big hallways?"
    hide BE with dissolve
    show FMG neutral with dissolve
    FMG "Beats me...{w} I feel like I should be putting up a volleyball net or something."

    scene Classroom
    show GTS surprised
    with fade
    GTS "These seats are... rather far apart."
    hide GTS surprised with dissolve
    show AE neutral with dissolve
    AE "Some kind of anti-cheating measure...?"
    hide AE with dissolve
    "I walked to a desk and gazed down at it."
    MCT "Why exactly is this seat so huge? Hell, the whole desk could fit three or four of me."
    "One by one, we all took our seats, looking around at the sparse classroom. All the usual educational aids seemed to be on shelves or set into the wall, making the room seem even more like an empty box than it already was."
    "If not for the teacher's lectern at the front of the class, you'd be forgiven for thinking we were in a pen instead of a classroom."
    "Finally the bell rang, and at the last possible second one could enter and not be late, our homeroom teacher slid open the door and entered."
    show HR unique with dissolve
    MCT "\"Dour\" is the first word that comes to mind... Guy looks like he's been middle-aged his entire life."
    "The man was tall, thin but not fit, wearing a collared shirt and dress slacks, with a jacket draped over one arm until he casually tossed it on the lectern. He swiped a piece of chalk up off the board and quickly scratched out his name on it."
    "{i}Kaeru Tashi{/i}"
    "Tashi-sensei dropped the chalk back on the tray, turned to us, and stepped forward, leaning against the lectern."
    stop music
    HR "..."
    hide HR
    show GTS neutral
    GTS "..."
    hide GTS
    show HR unique
    HR "..."
    hide HR
    show RM neutral
    RM "..."
    hide RM
    show HR unique
    HR "..."
    MC "..."
    show HR neutral with vpunch
    "Without a word, Tashi-sensei opened his mouth, and the classroom gasped as a four foot long tongue flopped out, unfurling down past Sensei's belt."
    hide HR
    show AE surprised with vpunch
    AE "Gch-!"
    hide AE
    show BE surprised with vpunch
    BE "Oh, ick!"
    hide BE
    show WG angry with vpunch
    WG "Keep that thing away from me!"
    hide WG
    show HR neutral-2
    "..."
    "..."
    play music Busy
    HR "All right, go ahead, get it out now."
    show HR unique
    "The nonchalance in the teacher's voice quickly turned the class' mood from panic to confusion, especially as that giant tongue continued to flop around as Tashi-sensei got into his bag and set his papers down on the lectern."
    show HR neutral
    HR "All done? {w} Good. Here's how this works."
    HR "Welcome to Seichou Academy. You're here because you, or a sibling, have expressed a certain trait that causes unusual growth of some kind."
    hide HR
    show BE surprised at Position (xpos=0.25, xanchor=0.5)
    with dissolve
    HR "Some of your growths are already obvious..."
    show PRG neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    HR "Others...{w} Not so much."
    hide BE
    hide PRG
    show HR neutral with dissolve
    HR "But make no mistake, unless you've got a sibling here at Seichou Academy, you're {i}going{/i} to change; even if you do, you've got good odds of changing yourself."
    HR "I know the Principal likes to dance around it, but I'm not going to mince words:{w} Seichou Academy is here to help you deal with whatever you're going to become. Key word being \"Help\"."
    HR "We can get you uniforms that fit, doors you can walk through, and gym classes for any shape and size.{w} What we can't give you is resolve, self-acceptance, the courage to make a life for yourself after whatever life makes out of you."
    HR "Simply put, we can give you tools. How you choose to use them falls onto your shoulders."
    HR "You'll find in your time here that, as are teaching styles, each teacher has a different approach to these... growths, as it were."
    HR "Some have a more tender approach and prioritize your comfort throughout this process, which of course, there is nothing wrong with."
    HR "As for me, I see more value in focusing on self-acceptance."
    HR "If you and your peers can learn to accept yourselves and your growth, then in theory, you should be able to tackle a number of things that life will throw your way, no?"
    show HR unique-2
    "Tashi-sensei scanned the room, taking in the fear and confusion, then shrugged."
    show HR neutral
    HR "Anyways, that's my big first day speech. Don't expect more.{w} So, roll call. Matsumoto-san?"

    scene black with dissolve
    stop music fadeout 1.0
    "So I found myself at Seichou Academy, orientation behind me and a long, strange journey ahead."
    "What was I supposed to do, knowing what I did about the bodies of the student body?"
    jump daymenu

label MC001:
    scene Dorm Interior with fade
    play music MC
    "The first day of class was certainly interesting... {w}bizarre, surreal, confusing— all manner of strange and unsettling characterizations came to mind, but I chose to stick with interesting for the sake of my own sanity."
    "Normally I'd like to sleep in as late as feasibly possible while still avoiding being late to class. I was pretty good at the first part, but hadn't mastered the second, even after 18 years of practice."
    "After recent events, I'm not too sure who would have slept soundly all through the night. Well, maybe Tomo. I don't think she'd even wake up for a firestorm during an earthquake."
    "Since I was already awake, I decided to just get up and get ready for class. After getting dressed, I was ready to head out."
    "I cracked the door open to leave when I noticed a lanky, clammy hand slowly shoving the door back shut."
    if not getFlag("RMRoute_Unlocked"):
        $setFlag("RMRoute_Unlocked")
    play music RM
    show RM neutral with dissolve
    "Oh yeah, that guy. My roommate. I'm pretty sure he said his name was Daichi. How did I not notice him standing there before?"
    MC "Uhhh, good morning?"
    RM "That remains to be seen. The morning hasn't started yet."
    MC "Right, I suppose... {w}Uh, did you need something?"
    RM "Do you know why you're here?"
    MC "Umm, because I have some kind of growth or something. I'm not—"
    show RM doubt
    RM "Yes, I know what they {i}told{/i} us. I'm asking you the {i}real{/i} reason you're here."
    MC "Are you implying that the real reason is something different than what we were told?"
    show RM distrustful
    RM "I'm asking the questions here."
    show RM doubt
    extend " But the answer is yes, {w}well perhaps, {w}probably at least."
    MC "Was there something unconvincing about seeing a man with a meter long tongue talk about body parts growing in unusual ways?"
    show RM concerned-2
    RM "No, but maybe that's the point— a little {i}too{/i} convincing."
    "My eyes were beginning to glaze over at this point. It was a bit too early in the morning to put on a tin foil hat."
    show RM smug
    RM "Think about it. What better way to get students to completely fall in line and accept what they've been told than to be shown something that seemingly confirms the story they've planted in our minds?"
    MC "I did think about it. I saw it and now I can't forget it, even if I wanted to. If that was the point then Tashi-sensei did a pretty good job, because I'm convinced."
    show RM doubt
    RM "{i}Tck{/i}. Don't be so quick to accept just anything. Ever heard the expression \"Don't believe anything you hear, and only half of what you see.\"?"
    MCT "No, but in light of this conversation it sounds like useful advice."
    menu:
        "Tell him he's not making sense.":
            MC "Well, that's the first I've heard it, but I guess I'm not supposed to believe it."
            show RM distrustful
            RM "Ugh, {i}listen{/i}... You can't just accept at face value people will tell you everything you want to know from them. It takes real {color=#0066CC}skill{/color} to read between the lines and extract everything out of them."
        "Just humor him.":
            MC "Alright, I'm listening."
            $setAffection("RM", 1)
            RM "Look, you can't just accept at face value people will tell you everything you want to know from them. It takes real {color=#0066CC}skill{/color} to read between the lines and extract everything out of them."

    MC "Skill? Like what kind of skill?"
    MCT "More to the point, what are you even talking about?"
    show RM happy
    RM "Well, aside from good intuition and a healthy sense of skepticism {size=-6} both of which you are sorely lacking... {/size}"
    show RM smug
    RM "Most people respond more favorably to people with skills they respect. That's where you have to read between the lines, to figure out how someone ticks. Then maybe they'll open up to you more."
    if isHighestSkill("Art"):
        RM "You seem like someone who's more artistically inclined. That can help you come off as thoughtful and creative to more sensitive minded individuals. Pretentious types really eat that stuff up."
    elif isHighestSkill("Athletics"):
        RM "You seem like someone who's more athletically inclined. People that are always active respect that kind of stuff."
    elif isHighestSkill("Academics"):
        RM "You seem like someone who's more academically inclined. Keeping your grades up is important. People are always looking for a study buddy for the tough courses."
        show RM doubt
    RM "Regardless of your forté, rest assured, if you don't keep all your skills sharp you {i}will{/i} miss things."
    MC "Why are you telling me this?"
    show RM distrustful
    RM "Because someone here must know something about why we're here, something more."
    show RM happy
    extend " I want you to be on the lookout, get some feelers out there. Report back to me if you find any interesting tidbits."
    MCT "Aye aye Captain Weirdo!"
    MC "Uh, sure. I'll try to keep that in mind. {w}Can I go now?"
    show RM concerned-2
    RM "Yes, I don't have anything else... {w}for now."
    show RM doubt
    extend " Just remember what I told you. Stay sharp."
    MC "Yeah, no problem. Uh... See you in class, I guess?"
    hide RM with dissolve
    play music MC
    "Daichi had walked back to his side of the room, already completely engrossed with typing away at his laptop, oblivious to my presence after having just cornered me for an impromptu interrogation."
    "Not bothering to wait for a response, I just headed out the door."
    scene Dorm Hallway with fade
    "Daichi was certainly... eccentric, to put it lightly. As off-putting as our initial interactions had been, I decided not to judge him too harshly for it. We've all been thrust into something no one could have really prepared for."
    "People cope with the stress of the unknown in different ways and I didn't know the guy well enough to know if that was his true personality, or if he just needed some time to wind back down."
    "I wasn't holding out for the latter any time soon though."
    scene Dorm Exterior with fade
    "Still though, there was something about his advice to read between the lines that stuck with me. That I'd be missing out if I didn't develop myself to my full potential. {w}Something to think about at least."
    "More importantly though, this was the start of something new, there were a lot of new people to meet. Hopefully some were worth getting to know."
    jump daymenu

label MC002:
    scene Classroom with fade
    play music Schoolday
    if not getFlag("Meet_Takamura"):
        $setFlag("Meet_Takamura")
    $setFlag("Meet_Hageshi")
    $setFlag("Meet_Tsubasa")
    pause .25
    "The knowledge I'd picked up over my first week or so at the academy had been, for the most part, things completely outside of my scope."
    "The oversized doorways and halls, the remote campus and island, and the looming idea of our bodies morphing in ways that would have to be seen to believe were, in every way, the stuff of fiction."
    pause .25
    "And, the more I thought about it, the more I was wondering if I'd fallen into some wicked fever dream."
    "Even in this fever dream realm, however, I still sat in class."
    "Apparently, classes were the same no matter where I was, same sort of subjects and all."
    "I rubbed my eyes a bit. That post lunch haze had set in like a bird in a nest, and the effects of my bowl of zaru soba had more than shown themselves."
    show HR neutral with dissolve
    pause .25
    HR "... created from bone, shells, antlers, and..."
    "I rubbed my eyes a bit to shake off my laziness, and brought pencil back to paper."
    MCT "It's Saturday tomorrow... just pull through."
    pause .25
    HR "With hunting and gathering being the main focus during this time, it led to a much more simple life. However, that's not to say things were easy."
    HR "Could anyone tell me when the middle Jōmon period specifically began?"
    show HR neutral at altMove(0.5, 0.75)
    show WG neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    pause .25
    HR "Nikumaru-san?"
    show HR unique
    WG "... 3500 BC."
    show HR neutral
    HR "Not quite. Anyone else? Anyone?"
    hide WG
    show AE neutral at Position(xcenter=0.25, yalign=1.0)
    with dissolve
    pause .25
    HR "Matsumoto-san?"
    show HR unique
    AE "3520 BC."
    show HR neutral
    HR "Correct."
    hide AE with dissolve
    pause .25
    HR "This time period saw the rise of pottery vessels and figurines, as well as jewelry."
    show GTS neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    "Across the room, Naomi put her hand up."
    HR "Yes, Yamazaki-san?"
    show HR unique
    GTS "This is when the migrating communities began to move into the more mountainous regions of Japan, correct?"
    show HR neutral
    HR "That is correct, yes. The land was warming quite a bit during this time, and these groupings of people became much more sedentary in their lifestyles."
    hide GTS with dissolve
    pause .25
    "I quickly made a heading for the Middle Jōmon period and underlined it, then jotted these notes down as quickly as I could."
    HR "Now, we're running short on time, so I would like you all to do a bit of research tonight and over the weekend."
    HR "Write a short summary of each of the Jōmon sub-periods, with some detail of the defining features of each. It doesn't have to be anything crazy long. Two paragraphs for each will be sufficient."
    HR "However, I do mean two paragraphs of solid work. Show that you have a grasp of the topic, and you'll do fine."
    show HR unique
    if isEventCleared("BE001"):
        show BE neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
        pause .25
        "I glanced over to Honoka's desk."
        "Surprisingly, she was actually jotting down some notes and not... I don't know, looking out the window or something?"
        MCT "Seems like she's learned to be more productive since our childhood days."
        if getFlag("global000_sitBE"):
            MCT "I do wonder how she's getting along since that first day in the auditorium. Think we all got a sufficient mental shock that day."
        hide BE with dissolve
    elif isEventCleared("AE001"):
        pause .25
        show AE neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
        "Ahead of me, I could hear Shiori writing away fervently at her paper."
        MCT "Well, I don't doubt that she'll have two pages for each period."
        "The back of her head told me nothing, but I could already imagine the look on Tashi-sensei's face after collecting her work."
        if getFlag("global000_sitAE"):
            MCT "At least she seems a little more relaxed since that first day in the auditorium."
            MCT "Though, it's not like the back of her head really has feelings..."
        hide AE with dissolve
    elif isEventCleared("FMG001"):
        pause .25
        "I glanced over toward Akira's desk."
        show FMG neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
        "To her credit, Akira did have her notebook out on her desk. But from what I could see, she seemed to have more scribbles and the occasional doodle than anything else."
        MCT "Well... guess she'll figure it out."
        if getFlag("global000_sitFMG"):
            MCT "She seems more comfortable, at least compared to that day in the auditorium."
        hide FMG with dissolve
    elif isEventCleared("GTS001"):
        show GTS neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
        pause .25
        "Across the room, Naomi jotted down more notes and looked up expectantly at the front of the room."
        MCT "Based on her question, she seems to already have a grasp on this stuff pretty well."
        MCT "Maybe she comes from a background riddled with history buffs and the like."
        if getFlag("global000_sitGTS"):
            MCT "She's got that same sort of careful precision that I saw during the principal's address that day. Like laser focus."
        hide GTS with dissolve
    elif isEventCleared("WG001"):
        show WG neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
        pause .25
        "I glanced over at Alice as she jotted down some notes."
        MCT "Geez, after that shut down from Tashi-sensei, I'm surprised Alice isn't giving him a death glare or something."
        MCT "... Though, that could easily happen down the line."
        hide WG with dissolve
    elif isEventCleared("PRG001"):
        pause .25
        "I glanced across the room."
        show PRG neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
        pause .25
        "Aida sat quietly nearby Alice, writing quickly."
        MCT "Huh. By the looks of her paper, she's almost writing... too much."
        if getFlag("global000_sitPRG"):
            MCT "... Guess she really wants to have all of her bases covered."
        hide PRG with dissolve
    pause .25
    "Overhead, the bell rang out over the masses."
    show HR neutral
    HR "And that'll be it. Have a good weekend."
    hide HR with dissolve
    "The class began to pack up around me, and I glanced down at my notebook with a feeling of shame nibbling at me."
    pause .25
    "I had... three lines of notes."
    MCT "Damn... stupid zaru soba. Totally skipping lunch next week."
    if isEventCleared("BE001"):
        show BE happy with dissolve
        "I looked up and watched as Honoka packed herself up and left the room."
        hide BE with dissolve
    elif isEventCleared("AE001"):
        show AE neutral with dissolve
        "In front of me, Shiori rose from her seat and put her supplies back into her bag in an incredibly organized fashion, especially as far as bookbags were concerned."
        hide AE with dissolve
    elif isEventCleared("FMG001"):
        show FMG neutral with dissolve
        "I happened to glance across the room and watched as Akira almost literally swept the contents of her desk off and into her bag, then got up and left. All of this in under five seconds."
        hide FMG with dissolve
    elif isEventCleared("GTS001"):
        show GTS neutral with dissolve
        "I looked lazily toward the windows and watched Naomi finish a page of notes, then store her notebook away."
        "She got up, then set to work organizing her bag on her desk."
        hide GTS with dissolve
    elif isEventCleared("WG001"):
        show WG neutral with dissolve
        "At the sound of the bell, Alice rose from her seat and began storing the contents of her desk away piece by piece, so organized in fact that I was picturing her cleaning up after a business conference instead of an average university styled class."
        hide WG with dissolve
    elif isEventCleared("PRG001"):
        show PRG sad with dissolve
        "As I slipped my notebook into my bag, I looked over and saw Aida slipping her notebook away and into her bag. From where I sat, I couldn't really make much out, especially with the glare of the window, but she got up and hurried off and out of the room."
        hide PRG with dissolve
    pause .25
    show RM neutral with dissolve
    "Following the rest of the class, Daichi got up from his seat and walked near-silently out of the room."
    MCT "He even walks like he's got some sort of off-the-wall plan."
    if getFlag("RM_govagent"):
        MCT "Maybe I'd better remind him to look out for oncoming balconies..."
    else:
        MCT "Well, whatever he's on about is his problem."
    hide RM with dissolve
    pause .25
    "I put my bag back on my back. I knew that what I had for notes wasn't going to cut it."
    show HR unique with dissolve
    "At the front of the room, Tashi-sensei was packing up his things as most of the students left, save for a few stragglers."
    MCT "Alright. The key is to look interested, not lazy."
    pause .25
    MC "Excuse me, Tashi-sensei?"
    show HR neutral
    HR "Mm? Yes, Hotsure-san? Need something?"
    show HR unique
    MC "Yes, Sensei. I was wondering if you had an idea where I could look for more information on the Jōmon period."
    MC "I'd try the internet, but I'd rather find information that I know is sound instead of flipping a coin for it online."
    show HR neutral
    HR "Ah, understandable. Yes, information online can be rather dubious."
    HR "I do have a book on the topic that I've been using to brush up on the topic myself. You're free to borrow it, if you'd like. Of course, I expect to see it again on Monday."
    show HR unique
    MC "That would be wonderful, Sensei. And thank you. I'll make sure to get it back to you on Monday."
    show HR neutral
    HR "Fine then. I have it back in the faculty room."
    "Tashi took his bag and walked toward the door."
    pause .25
    HR "Come along. I'd rather not have to take extra time to run the book back here to you."
    show HR unique
    MC "Ah... students are allowed in the faculty room, Sensei?"
    show HR neutral
    HR "Alone? Far from it. However, I'm accompanying you, and it'll be a few minutes at most. It's no trouble."
    show HR unique
    MC "Alright. Thank you, Sensei."
    "Tashi nodded and walked out the door, holding the door behind him so I could follow."
    scene Hallway with fade
    pause .25
    "Walking down the hallway alone was usually like what I imagined a fish felt like in a river."
    "Everything rushed by quick, and split second decisions felt like they'd save you time, or add on minutes."
    pause .5
    "Walking with Tashi-sensei felt like being a remora on a shark."
    pause .25
    "... A very tired looking shark."
    "Tashi and I walked silently down the hall together, neither of us saying a word."
    scene Hallway2 with fade
    "We passed clubrooms, other classrooms, and students as we went down the halls."
    scene HallwayStairs with fade
    "Near the end of one hall, we passed a set of stairs and went along down another hall, where I saw a door with a light on off to one side."
    "Tashi reached out and opened the door, holding it open as he walked in, followed by me."
    scene Faculty Room with fade
    stop music
    pause .25
    "Inside, the room was quiet. However, it was far from empty."
    "In the middle were some desks pressed together to form a sort of \"mega-desk.\""
    play music Rain
    if isEventCleared("BE006"):
        show Takamura neutral with dissolve
        "At it sat a familiar looking teacher, Takamura-sensei."
        hide Takamura with dissolve
    else:
        show Takamura neutral with dissolve
        "At it sat a familiar looking teacher, who upon further inspection, I recognized from when I'd first arrived on the island with Tomo."
        hide Takamura with dissolve
    pause .25
    show Tsubasa neutral with dissolve
    "Across from her was a man that I could only describe as a stereotypical professor type, with thick, black-rimmed glasses perched on his nose."
    "He held a newspaper in front of him, and was skimming through it with a bored look on his face."
    hide Tsubasa with dissolve
    pause .25
    show Hageshi neutral with dissolve
    "At the other end of the megadesk sat a guy who I swear, looked like he'd been at the gym for the last four years of his life. His shoulders bulged out against the fabric of his shirt as he made some notes on some papers."
    hide Hageshi with dissolve
    pause .25
    "All the way across the room stood two other teachers, who were literally standing around the water cooler."
    "One of them had not just one, but three whistles around his neck, and was chatting warmly with the other teacher."
    MCT "Who the hell's attention is he trying to get with those?"
    show Takamura happy with dissolve
    Takamura "My my, Tashi-chan. You look like you could use a nap or three."
    pause .25
    show Takamura happy at altMove(0.5, 0.25)
    show HR annoyed at Position(xcenter=0.75, yalign=1.0) with dissolve
    HR "... I've told you not to call me that."
    show Takamura reassuring
    show HR unique
    Takamura "Oh, I'm just teasing. Always such a stiff, Tashi-chan."
    "Tashi waved his hand and shook his head in disbelief, choosing instead to rummage through one of his bags."
    show Takamura neutral
    if isEventCleared("BE006"):
        Takamura "Ah, another Hotsure. My word. What brings you here?"
    else:
        Takamura "Ah, another Hotsure. My word. What brings you here?"
        MC "Ah... pardon, Sensei?"
        Takamura "You're the brother of my Hotsure, aren't you?"
        MC "Another Hotsure? You're Tomo's homeroom teacher then?"
        Takamura "Indeed."
    pause .25
    show Takamura reassuring
    Takamura "Guess you and I both get to teach the members of the Hotsure clan, hm Tashi-chan?"
    show HR annoyed
    HR "Egh... {w}He's borrowing a book from me for an assignment I'm having his class work on."
    HR "Do me a favor, Hotsure-san, and have a seat over by Takamura-san."
    hide HR with dissolve
    "I nodded as the look in his eyes turned from a dull, blasé look to one that asked \"please do this for me for the love of all that's holy.\""
    show Takamura happy at altMove(0.5, 0.5)
    "I walked around the table and took a seat by Takamura-sensei. In front of her was a large binder with multiple colored tabs sticking out from hoards of paper."
    Takamura "So, how have your first few days been here, Hotsure-san? Well enough, I hope."
    MC "Yeah, I'd say so. Thank you for asking, Takamura-sensei."
    Takamura "Of course!"
    show Takamura reassuring
    Takamura "And, if I may, how are you feeling in regards to the knowledge of what the academy is here for? And, how it applies to you?"
    MC "I... well, I'm doing my best to keep doing what I'm doing, I suppose."
    MC "It is definitely not what I was expecting upon coming here, though."
    show Takamura neutral
    Takamura "Your perspective is one of realism. I can't fault you there."
    Takamura "I'm glad to hear you've been able to keep yourself grounded through all of these admittedly hectic first few days."
    show Takamura neutral at altMove(0.5, 0.25)
    show HR annoyed at Position(xcenter=0.75, yalign=1.0) with easeinright
    HR "No privacy for him at all, Takamura-san?"
    show Takamura strict
    show HR unique
    Takamura "Well, my apologies for assuring that our students are feeling alright."
    show HR annoyed
    HR "All I'm saying is that you ought to keep your eyes on your own responsibilities. Not everyone needs the close talk treatment."
    Takamura "Maybe you'd be comfortable with that sort of approach if you'd had someone reach out to you in a similar way when you were younger."
    pause .25
    show HR unique
    HR "..."
    pause .25
    show HR annoyed
    HR "There's nothing wrong with presenting the facts."
    show HR unique
    Takamura "No there isn't. But, those facts aren't exactly light on new ears, Tashi-chan."
    pause .25
    show HR annoyed
    HR "So, let me ask you this, then. Why all of the fuss over this extra... fluff?"
    "Tashi waved one hand over Takamura's overstuffed binder."
    HR "Why worry so much over it?"
    show Takamura happy
    show HR unique
    Takamura "Someone has to."
    "Takamura clicked her tongue twice and raised her eyebrows at Tashi."
    "Tashi rolled his eyes and dug his head into a larger locker off to one side."
    hide HR with dissolve
    show Takamura neutral at altMove(0.5, 0.5)
    if isEventCleared("BE006"):
        MC "I know we discussed it earlier, Sensei, but how is Tomo doing in your class?"
        Takamura "Well, she's always on time. She does seem a tad quiet, but that's nothing unusual, especially given the circumstances of a new academy with all new people to get to know."
    else:
        MC "So, if I may, Sensei. How is my sister doing in your class?"
        Takamura "Well, she's always on time. She does seem a tad quiet, but that's nothing unusual, especially given the circumstances of a new academy with all new people to get to know."
    "In front of her, Takamura shut her binder and set it on the desk."
    pause .25
    Takamura "You'll have to excuse me. I'm finishing some references for an upcoming project that I'm working with the principal on."
    Takamura "It's a rather tall order, but I think that with proper application, we could have something wonderful here."
    Takamura "Oh, but come to think of it, I suppose you haven't met most of the rest here, have you?"
    MC "Ah... not yet, no."
    show Takamura reassuring
    Takamura "Well, we can't have a guest here feeling unintroduced."
    pause .25
    show Takamura happy
    Takamura "Tsubasa-sensei? Rest your eyes for a moment."
    "Across from us, the older teacher lowered his paper just enough to look over the top."
    show Takamura neutral at altMove(0.5, 0.25)
    show Tsubasa neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    Tsubasa "Hm?"
    Takamura "We have a visitor, courtesy of Tashi-chan."
    HR "..."
    "The older teacher lowered his paper to the desk, and I recognized him as one of the biology or math teachers. The subjects kind of blended together for me."
    Tsubasa "And you are?"
    MC "Keisuke Hotsure. It's nice to meet you, Sensei."
    Tsubasa "Likewise."
    "And, the paper went right back up, hiding his face."
    Takamura "Tsubasa-sensei has been here for ages. Longer than anyone else, I think."
    Tsubasa "How are your parents, Aoi-san? Doing well, I trust?"
    pause .5
    MCT "... He could at least lower the paper."
    pause .25
    show Takamura happy
    Takamura "Quite well, thank you. Just celebrated their anniversary a few weeks ago actually."
    Tsubasa "How nice."
    pause .25
    show Takamura neutral
    Tsubasa "I assume that your efforts are going into the recent Caverns project?"
    Takamura "They are, Sensei. I think you'll find it quite intriguing once our ideas take shape."
    "Tsubasa-sensei coughed twice, then flicked his paper a bit and turned the page."
    show Takamura happy at altMove(0.5, 0.5)
    hide Tsubasa with dissolve
    "I glanced over at Takamura, and she waved one hand with a small laugh."
    Takamura "And at the end there is our young pup. Yoshito Hageshi."
    show Takamura neutral at altMove(0.5, 0.75)
    show Hageshi neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    "Hageshi-sensei glanced up from his pile of papers."
    Takamura "How long have you been here now, Hageshi-san? Five years now?"
    pause .25
    Hageshi "... Four, actually."
    show Hageshi satisfied
    Hageshi "And, last time I checked, you've been here for only three years. So, by my count, you'd be the \"young pup.\""
    show Takamura happy
    Takamura "And, who's the youngest teacher in the room?"
    pause .5
    show Hageshi neutral
    Hageshi "..."
    pause .25
    "My eyes immediately went to his bulging biceps and shoulders. The dude was freaking ripped! Did he have like 1%% body fat or something?"
    show Takamura neutral
    "In addition, he was tall, and seemed to fill the entire room around him, especially compared to Takamura."
    Takamura "He's the academy's math teacher, so you'll probably see him sooner or later."
    show Takamura neutral at altMove(0.5, 0.5)
    show HR neutral at Position(xcenter=0.75, yalign=1.0) with easeinright
    HR "Do yourself a favor and don't start any fights around campus."
    HR "Yeah, you might start it with some guy that looked at you funny, but you'll end it with Hageshi-san. And trust me, you don't want that."
    HR "By the time he was your age, he was already a nationally ranked judo champion."
    hide HR neutral with easeoutright
    "I looked back at Hageshi-sensei, who somehow managed to look even more intimidating in light of that information. {w}He just gave a slight nod, confirming Tashi's story about him without saying anything for himself."
    show Takamura neutral at altMove(0.5, 0.75)
    "Behind Hageshi-sensei, the two teachers by the water cooler left their positions and exited the room. As they left, I noticed the whistles around the neck of that one faculty member wearing an athletic outfit."
    if isEventCleared("BE003"):
        MCT "Huh. That's the same outfit that Honoka had on the other day."
    pause .25
    MC "If I may, Takamura-sensei, what's with the... uh..."
    Takamura "The whistles?"
    MC "Yes, Sensei."
    Takamura "Well, I'll allow him to introduce himself to you another time, but he's in charge of a number of clubs around the academy."
    Takamura "Ergo, lots of whistles."
    MC "I... see..."
    pause .25
    Hageshi "I thought the whistle thing was a joke between students?"
    Takamura "Well, joke or not, he's a busy man."
    show Tsubasa annoyed with dissolve
    Tsubasa "Pardon? Are you saying that my-last-name-is-too-long-san is wearing whistles for every club he coaches?"
    hide Hageshi with dissolve
    Tsubasa "Ridiculous compensation."
    pause .2
    show Takamura neutral at altMove(0.5, 0.25)
    hide Tsubasa with dissolve
    show HR neutral at Position(xcenter=0.75, yalign=1.0) with easeinright
    HR "Alright, Hotsure-san. Here you are."
    show HR unique
    "Tashi handed me a thick book with some light wear to the front cover and spine. On the cover was what appeared to be some old pottery and a typical, cheesy \"I had no idea what to put on the cover, so here's a landscape\" image."
    pause .25
    MC "Thank you, Sensei. I really appreciate it."
    show HR neutral
    HR "Take a look through there. It should have some information on every sub-period."
    HR "Again, I'll expect it back on Monday."
    MC "Yes, Sensei."
    pause .25
    show Takamura reassuring
    show HR unique
    Takamura "Pardon me, Tashi-chan, but why all the worry over this extra fluff?"
    show Takamura flattered
    Takamura "Bending over backwards to help a student? Could it be that the cold and brash Tashi-chan does have a warmer side?"
    HR "..."
    show Takamura neutral
    pause .5
    show HR annoyed
    HR "Have a good day, Hotsure-san."
    show HR unique
    MC "Y-Yes. You as well, Sensei."
    Takamura "Lovely to meet you again, Hotsure-san."
    hide HR
    hide Takamura
    with dissolve
    "Tsubasa and Hageshi both nodded politely at me from where they sat as I left the room, shutting the door quietly behind me."
    scene HallwayStairs with fade
    "I was no more than 15 steps down the hall when I heard more banter from the faculty room behind me."
    "I held the heavy book under my arm and went off to immerse myself in ancient history."
    jump daymenu

label MC003:
    scene Dorm Interior with fade
    play music HigherEdu
    "{i}*Riiinnnng! Riiinnnng!*{/i}"
    "The digitized dial tone of my phone rang out, only to the notice of myself, rather than the intended recipient."
    "I'd been trying to get a hold of Tomo since finding out about my factor. I wanted to know how she was taking the news about hers too. I suspected she was going through the same thing..."
    "Well I didn't know for sure, but I {i}assumed{/i} she would be. {w}But that's what gnawed at me. This was my little sister after all. I wasn't too keen to just rely on assumptions."
    MC "Arrggh! Pick up your stupid phone Tomo!"
    play music RM
    show RM neutral with dissolve
    RM "Something the matter?"
    MC "Oh, hey. You're here."
    show RM doubt
    RM "I live here."
    MCT "Could've fooled me, you don't act like it."
    MC "Sorry if I seemed surprised. You don't seem to spend much time here."
    show RM smug
    RM "I've been busy gathering information."
    MCT "Oh, here we go again."
    show RM distrustful
    RM "It's all a bit too convenient that they supposedly have a test that will predict a person's growth, now of all times, when they've already recruited people based on the presence of their growth."
    MC "Well maybe it just takes time to mature?"
    show RM doubt
    RM "That would make sense, {w}{i}if{/i} they understood how they worked and what caused them."
    RM "The fact that they are so short on details about what they are, claiming to know so little— yet they can somehow reliably inform students not only that they do or do not have a growth, but the exact kind it will be..."
    show RM neutral
    RM "It doesn't add up."
    MC "You suspect they're keeping us in the dark?"
    show RM doubt
    RM "I've always suspected that, but now I know."
    "Daichi's suspicions didn't seem entirely unfounded, not much of this really made sense."
    if isEventCleared("MC002"):
        "Like the tall buff teacher Hageshi-sensei that was supposedly \"small\" for his growth. The guy is more than twice normal size with like zero percent body fat."
    "Then again, after seeing Tashi-sensei's tongue flop out of his mouth on the first day, I wasn't really sure how much of any of this was going to make sense to anyone."
    "For the moment, I had other questions on my mind than probing the seedy underbelly of Seichou Academy."
    MC "Wait a second, backup there a bit. You said this test they do tells students if they have a factor or not. I thought we all had something. Isn't that why they brought us here?"
    show RM neutral
    RM "Not quite. Most, but not all students do. The official explanation is that close relatives of similar age are brought on board as both emotional support and to help them adapt to the changes in their family members as well."
    RM "Though I suspect the real reason is that relatives of those with factors are closely eyed as suspected candidates for having a growth factor."
    MC "So it's a genetic thing?"
    show RM concerned
    RM "No. In fact I can confirm that is not the case. At least, there isn't a direct correlation."
    MC "What do you mean?"
    show RM concerned
    RM "I don't have a factor... but my sister does."
    MCT "So it's possible Tomo doesn't have anything at all? That's a relief."
    show RM neutral
    if isEventCleared("RM002"):
        MC "Funny you should mention Yuki. I was trying to get a hold of my sister just now. I hadn't gotten to talk to her since before the test."
    else:
        MC "Funny you should mention your sister. I was trying to get a hold of mine just now. I hadn't gotten to talk to her since before the test."
    RM "You're wondering if she has a hair growth factor like you?"
    MC "Yes, exactly! {w}Wait."
    show RM sad
    extend " When did I tell you I had a hair growth factor?"
    RM "Umm, well... it's fairly obvious for you isn't it? ...{size=-6}Yes, that'll work{/size}..."
    show RM smug
    extend " I mean it's already covering half your face."
    MCT "Well, he's got me there."
    RM "Some people tend to manifest them earlier than others."
    MC "Like Matsumoto-san?"
    show RM happy
    RM "Correct. Some things are too obvious to hide."
    MCT "Kind of what I thought when I first saw Honoka off the boat."
    "This all put my mind at ease. I was probably worried for nothing. Could be she didn't have any factor, even if having longer hair wasn't {i}that{/i} big a deal. {w}Still though... that feeling of ill-ease was still gnawing at me."
    show RM neutral
    MC "But... Tomo and I are twins. Not identical twins obviously, but still, would that make it more likely she would have the same factor?"
    show RM concerned
    RM "My initial assumption would have been yes, but I've heard reports of identical twins having completely different growth factors."
    "An image of Tomo flashed into my mind of her sticking her tongue out at me in response to my usual teasing, only to have it flop out of her mouth all the way down to the floor."
    show dummy with vpunch
    MC "{i}GUAHH!{/i}"
    show RM doubt
    RM "Something the matter?"
    MC "Umm, no. I just remembered I gotta do something. Thanks for your insight with this stuff."
    MC "I'm going to try to contact my sister again. I'd just knock on her door but I don't even know her room number."
    show RM sad
    RM "You seem pretty concerned. I guess I can understand why."
    show RM neutral
    extend " I'll call my sister so she can tell her to answer her phone."
    MC "Wait, what? You mean to tell me your sister knows my sister? And you know that she knows my sister? When did all of this happen?"
    RM "Slow down, it's not that complicated. My sister Yuki tells anybody everything— for better or worse. {w}She told me about her new roommate and I can't imagine there are too many other Hotsure's in a school this size."
    MC "So there are two Hotsure's paired with two Utagashi's? Isn't that a bit of a coincidence?"
    MCT "Come to think of it, the teacher at the docks also found it curious... {w}Wait a second— now I'm starting to sound like the crazy one here."
    show RM doubt
    RM "It probably has to do with some randomized pairing based off of alphabetical order. Not every coincidence is that intriguing."
    MC "That's as good an assumption as any."
    MCT "Let's just leave it at that for now."
    MC "Anyway, I appreciate the help. When Tomo sleeps, she's dead to the world— and she sleeps a lot. {w}Well, that and I'm not exactly expecting her to eagerly await a text from me."
    show RM happy
    RM "Alright, I sent my sister a text. She said she'll wake her up when she gets back to her dorm."
    MC "Thanks again man."
    show RM doubt
    RM "Don't mention it. Now all of this has got me thinking again. There's gotta be some common thread here with all of this, even if it isn't initially obvious."
    hide RM with dissolve
    "Apparently the answers he sought weren't here because he had seemingly vanished in the half second I turned away from him to check my phone."
    MCT "I guess it hasn't been that long. I'll just have to wait."
    stop music
    scene black with fade
    pause 1

    play music MC
    show cg MC003 with dissolve
    "What felt like hours for me was probably just 20 minutes before Tomo texted back."
    TomokoCell "What do you want? Why did you have my roommate wake me up?"
    MCCell "Just meet me outside the dorm. I got something for you."
    TomokoCell "This better be good."
    "I knew Tomo wasn't going to set any landspeed records with her level of urgency, so I just bided my time sitting on one of the benches outside the dorm until she came out."
    hide cg
    scene Dorm Exterior
    with fade
    show Tomoko neutral at Position(xcenter=1.10, yalign=1.0)
    pause 0.1
    show Tomoko neutral at altMove(2.0, 0.5)
    Tomoko "What was so important you couldn't have just texted me for instead?"
    MC "Nice to see you too, Tomo."
    Tomoko "Ugh, don't be like that. You know I didn't mean it like that."
    MC "Fine, I'll spare you the guilt trip. I haven't exactly been doing a good job keeping up with you either, but I'm trying to fix that."
    show Tomoko distracted
    Tomoko "You said you had something for me."
    MCT "I knew I'd have to sweeten the deal to get her to come."
    MC "Here you go."
    show Tomoko neutral
    Tomoko "This is just some pocky you got from a vending machine."
    MC "I'll take it back if you don't want it."
    Tomoko "I didn't say that."
    MCT "Yeah, that's what I thought."
    MC "Besides, it's strawberry. I figured you'd like it."
    Tomoko "It's one of the better ones. Thanks, I guess. {w}Was that it?"
    MC "How are things, Tomo?"
    Tomoko "Alright I guess. People here seem nice. My roommate seems okay, but she wants to talk my ear off and blow up my phone with every piece of gossip that she comes across. {w}It's all a bit much, to be honest."
    MC "Interesting, I hear my fair share of rumors from my roommate as well. But at least he seems quiet for the most part."
    Tomoko "She's not that bad though, it's whatever. Still, though, there doesn't seem much to do around here though."
    MCT "I don't know why you care. If there were a million things to do, you'd still choose to nap."
    MC "Well, what I meant more was how are you holding up after, you know, the test?"
    show Tomoko distracted
    Tomoko "We haven't been here that long. I haven't had any major tests in classes."
    MCT "This is going nowhere fast."
    MC "Okay, I'll just go first. I mean the factor test. It told me my hair was going to grow really long... or was it really fast? Maybe both, I don't quite remember now that I think about it."
    "Part of me didn't want to ask the next question, afraid of the answer, but I knew I had to."
    MC "What did yours say, if you don't mind me asking?"
    show Tomoko neutral
    Tomoko "Oh that test. Yeah they told me the same thing. Something about my hair was going to start growing."
    "Her answer was simultaneously assuring and anti-climatic. As much as I was relieved that it wasn't anything major or too odd, I couldn't help but feel like I wasted a lot of energy worrying about all the other possibilities."
    MC "So... how are you taking the news?"
    Tomoko "I mean my hair has always been growing. Didn't seem like that big a deal to me."
    MC "But you never do anything with your hair, you're probably going to have to style it or brush it a lot, or something..."
    "I probably should have admitted that I didn't know either, but I felt like I needed to say something to get through to her this was probably a bigger deal than she realized."
    Tomoko "Eh, I'll just cut it off."
    MC "I guess. Maybe it is that simple."
    Tomoko "Is that it? Was that what you wanted to talk about?"
    "As ungrateful as her tone was, she kind of had a point. Here I was trying to be the hero big brother when his little sister needed him the most, but instead I just felt like a jackass from having overblown everything in my mind."
    MC "{i}Sigh{/i}. I was just worried, you know? {w}Like what if you were going to grow a tongue that stretched out a whole meter, or have giant feet (if that even is a thing), or big puffy lips, like the nurse."
    MC "Not that it'd be the end of the world if you did, but some of these things can make a person stand out... and not in a good way. I just didn't want that for you."
    Tomoko "I don't know why you were so worried if you knew you had a hair growth thing too. We're twins."
    MC "My roommate told me that isn't any guarantee."
    show Tomoko surprised
    Tomoko "Oh,"
    show Tomoko sad
    extend " I guess I understand why you were making such a big deal out of it then..."
    "I thought about teasing her for finally taking me seriously, but my emotional energy had been spent from being wound up about this all day. At that moment I was just glad my little sister was going to be okay."
    show Tomoko neutral
    MC "It's what big brothers do. They worry about their little sister."
    show Tomoko annoyed
    Tomoko "You're barely even 30 minutes older than me."
    MC "And don't you forget it."
    Tomoko "Ugh. Yeah I've only heard it almost every day for the past eighteen years."
    show Tomoko neutral
    extend " If it's all the same to you, can I head out?"
    MC "Not so fast. Give me a couple of those."
    Tomoko "No way! Get your own."
    MC "They were mine, until I gave them to you. Consider it a finders fee."
    Tomoko "Okay, fine. Here."
    MC "Text me your room number in case I need to find you again."
    Tomoko "Alright Dad. Geesh, if it will put you at ease."
    MCT "She knows I hate it when she says that, but I'll let that slide for now."
    MC "Tomo?"
    show Tomoko distracted
    Tomoko "Yeah?"
    MC "Don't be afraid to come see me, if you need anything."
    show Tomoko happy
    $setAffection("TM", 1)
    Tomoko "Okay. I'll keep that in mind. Later."
    hide Tomoko with dissolve
    "I suppose I got all worked up for nothing. But something about all this was strange. I had no idea what we were getting into, but something told me it wasn't all going to go away with just a haircut."
    jump daymenu

label MC004:
    $setTime(TimeEnum.EVE)
    scene Dorm Interior with fade
    play music Schoolday
    "In under five seconds, I had my shoes off, backpack flung onto my bed, and head jammed into the fridge."
    MCT "Gah... after class munchies. Always welcome, yet always ruining my dinner."
    "I retrieved an apple that had been there for... some time{w}, at least based on the rest of the slim pickings in the fridge. Without any other real prospects, I rinsed it in the sink, then took a bite of it."
    "I walked over to my desk and sat, gazing out the window."
    MCT "Alright. Friday afternoon, and I have no homework for once. Maybe I can actually chill out for a while."
    "..."
    MCT "Who am I kidding? I do that even when I do have homework."
    "I watched the fluffy clouds fluff lazily across the sky overhead, and glanced towards my balcony."
    "I could probably have counted the amount of times on one hand that I'd been on the balcony."
    if getFlag("RM_govagent"):
        MCT "One of them being Daichi nearly hurling himself off the damn thing..."
    "I took another bite of apple, working my way in a straight line down the middle of it."
    MC "Mngh...?"
    MC "Acgh-"
    "I opened my mouth and reached in, withdrawing one long strand of hair."
    MC "{i}Egh{/i}."
    MCT "Better get used to this, I suppose..."
    "I dropped the strand to the floor then swept my hair away from my face."
    MCT "There. I don't need any extra toppings on this."
    "I took another, less fuzzy bite and chewed thoughtfully, glancing around my dorm."
    "It didn't have that warm, welcoming feeling of a well lived-in home yet, but it did feel nice all the same. Especially after a long day of classes."
    "Nights there felt relaxing enough, save for when Daichi got a little too rambunctious. And even then, he wasn't... too out there."
    "I took the last bite of the middle line, then started nibbling at the upper edge of the apple."
    "I put my arms over my head and leaned back in my desk chair, stretching backwards and letting out a near primal groan."
    MCT "This is sad. I should be out doing fun, young adult things. Not sitting here stretching and... getting my daily dose of vitamin D."
    "I stood up and walked to the balcony, gazing out through the glass."
    MCT "It's... actually really serene here. All things considered."
    "The academy was quiet, for the most part."
    "No city sounds. Not a lot of cars. Not even really that many people, save for the town and the academy."
    "I glanced up at the sun, shimmering through a cover of clouds."
    "One moved in the sky and broke, sifting apart and letting the sun shine down onto the courtyard outside, and my balcony."
    MCT "Hm. Maybe some time in the sunshine could help get me in the action-y mood."
    pause .5
    MCT "Or just make me feel like taking a nap."
    "I glanced over at my headphones that I kept in the corner of my desk."
    MCT "... Then again, I could always just listen to something. Find a playlist online or something."
    MCT "That way, I can get myself in the mood to do something, or in the mood to catch up on my sleep."
    "I took another bite of apple and cleaned it up before walking and trashing the core."
    menu:
        "Listen to music":
            $setFlag("MC004_music")
            "I walked back to my desk and grabbed my headphones, then took my phone out and flicked a switch on the side of my headphones, connecting them to my phone."
            MCT "No headphone jack. Because why not?"
            stop music
            "I sighed, thinking back to every cell phone reviewer online, and laid on my bed, scrolling through to one of my music streaming apps."
            MCT "..."
            MCT "... Heard that twice this week already."
            MCT "Huh... people still listen to Dimefront?"
            "I scrolled past the mediocre rock band and clicked on another playlist."
            play music FullKnowMyself
            pause .5
            "♪...Love is just a game...♪"
            "♪...If I'm having fun then it's okay...♪"
            MCT "..."
            MCT "Wait, isn't this-"
            MCT "Oh, this is a cover. I remember this song. Mom used to listen to this all the time."
            MCT "Who covered this?"
            "I glanced down at the screen."
            MCT "Hm. Never heard of... Pre-Bop before. Kind of a unique name, I guess."
            "I rested my head on my pillow and shut my eyes, letting myself enjoy in a guilty pleasure sort of manner."
            scene black with fade
            MCT "Hmn..."
            if getHighestAffection() == ("BE"):
                MCT "I wonder if Honoka knows this group. She seems like she'd be pretty in the know with newer bands."
            elif getHighestAffection() == ("AE"):
                pause .5
                MCT "..."
                MCT "Matsumoto-san would never listen to this. That much I know."
                MCT "It is good music to shake it to, though..."
                pause .5
                MCT "Or wobble, in her case."
            elif getHighestAffection() == ("GTS"):
                MCT "I wonder... what would Yamazaki-san think of this?"
                MCT "I can totally picture her judging a song by the feelings it implies, rather than any technical aspects."
                MCT "Not like I could pick out the rhythm or the harmony myself. Wouldn't know a good one from a bad one anyhow."
            elif getHighestAffection() == ("WG"):
                MCT "Huh."
                MCT "Part of me feels like Alice would absolutely despise this song."
                MCT "At the same time, though... maybe not?"
            elif getHighestAffection() == ("PRG"):
                "I listened as the music swelled in my headphones."
                MCT "I wonder what Kodama-san listens to in her spare time."
            elif getHighestAffection() == ("FMG"):
                "..."
                MCT "Mizutani-san totally has at least five different workout playlists saved to her phone. Guaranteed."
            "I felt my thoughts drift away a bit as I turned up the volume a touch."
            "The idea of going out and having fun tonight was really nice, and did sound like the \"in\" thing to do... but my bed was comfy, and this music was-"
            scene Dorm Interior with vpunch
            stop music
            "I jerked up, my eyes jolting open as my ringtone blasted my eardrums multiple centimeters deeper into my skull, halting my music in the process."
            MC "ACH!! WHO THE-"
            pause .25
            MC "Oh..."
            "I gazed in a slightly worried fashion at my Mom's caller ID on my phone screen."
            MCT "Alright... I guess I have to do this eventually."
            pause .5
            MC "Hello?"
            MomCell "Keisuke? Are you alive?"
            MC "Uh... yeah?"
            MomCell "Could have fooled me. I heard Tomoko's voice before I heard yours."
            MC "Wait, seriously?"
            play music MC
            MomCell "... Well, I heard her voice via her voicemail, but still. I was hoping to hear from you sooner."
            MCT "She acts as though I've had better luck talking to Tomo..."
            MC "Yeah. Sorry about that, Mom. Things have been a little crazy here."
            MomCell "I would imagine so."
            MomCell "What are you up to today?"
            MC "Just got back to my dorm. I had some classes earlier, and now I'm just relaxing for a little bit."
            MomCell "I see. Make sure you take some time for that. It's not good to run yourself ragged."
            MC "Yeah, I know."
            MomCell "So, how is it otherwise, Keisuke? Are you doing alright? Feeling okay?"
            MC "I-I'm fine, Mom. No need to worry."
            MomCell "I... I know, Dear. I know. I just worry about you and Tomoko."
            "The line went dead for a few seconds."
            MomCell "So... do you know what... growing thing you have?"
            MC "You mean my growth factor? Yeah. Yeah I do."
            MomCell "Well, out with it then. Don't hold me in suspense."
            MC "I have a hair factor."
            pause .5
            MomCell "Ah... {w}hair factor?"
            MomCell "Like... the hair on your head, right?"
            MC "Yes, Mom. I'm not turning into a sasquatch. At least as far as I can tell so far."
            MomCell "Alright, alright. So, how does that work?"
            MC "Well, my hair has been growing faster and faster now. Like, I can cut it, and it'll grow back really quick."
            MomCell "Wow... I'll be frank, Keisuke. With what I'd heard, I assumed it was going to be something more severe. Like you'd be as tall as a building when I saw you next."
            MomCell "What about your sister? Is she doing okay?"
            MC "She's about the same. She has the same factor as I do."
            MC "And, she's really not overly fired up about the whole thing."
            MomCell "I see. And it works the same in women as it does for men?"
            MC "As far as I know, yes."
            MomCell "I see."
            MomCell "I... I'm relieved to hear that you two are okay, Keisuke."
            MomCell "Your father and I... well, we didn't know what to think."
            MomCell "The whole thing seems so out there..."
            MC "I know, Mom. It still feels a little far-fetched for me too sometimes. But... it's real."
            MC "Oh, you won't believe this. Remember Honoka Inoue? She's here too."
            MomCell "Honoka? As in, your old friend Honoka?"
            MC "Mhm. We bumped into each other when I got off the ferry."
            MomCell "Wow. Small world. How is she doing?"
            MC "Good. She's definitely grown up."
            MomCell "I'm sure. I remember her playing in the mud in our backyard when you two were little. Remember that mud castle she tried making? She was so adorable.."
            MC "I... yeah. I think I remember that too."
            MCT "I also wouldn't put it past Honoka to try something like that now."
            MomCell "Well, I'm glad you have someone you know there with you and Tomoko. Hopefully, it'll make the whole process a lot easier."
            MomCell "Have you met anyone else?"
            MC "Yeah, quite a few people."
            if getHighestAffection() == ("BE"):
                MC "I've been mainly hanging out with Honoka, though."
                MomCell "That's good to hear, Dear. She was always a sweetheart."
            MomCell "I'm glad to hear that you've been putting yourself out there. I think it'll help make this whole thing a lot easier to deal with."
            MC "Yeah, hopefully."
            MC "Is Dad doing okay?"
            MomCell "He's about the same. Working a lot of hours, but he's doing well. He misses you two, though."
            MomCell "Feels strange being empty nesters now, you know."
            MC "Heh, I suppose so."
            MC "Feel old yet?"
            MomCell "Oh, don't even start that."
            "My mom and I both laughed over the phone."
            MomCell "Have you made any plans for Golden Week yet?"
            MC "Not yet. Probably gonna see what there is to do here when that gets a little closer and figure it out then."
            MC "We have a test right after the holiday break, so I'll probably try to study for that a little."
            MomCell "I know you, Keisuke. You say that, but will you really?"
            MC "Ouch."
            MomCell "I'm just teasing, Dear. I'm sure you'll put in the time."
            MomCell "Well, Dear. I'll let you go. I'm sure you've got something fun planned for tonight, and I wouldn't want to interrupt that."
            MomCell "It was nice to hear from you though, Honey. Keep us in the loop if you can, okay?"
            MC "I will, Mom. Sorry it took me so long."
            MomCell "Oh, it's okay. I understand. New school, new people, crazy body changes going on. I don't blame you."
            MC "Thanks Mom. I love you."
            MomCell "Love you too, Keisuke. And tell Tomoko to give me a call, would you?"
            MC "I'll try, but she never listens to me."
            MomCell "It's the effort that counts."
            MomCell "Bye, Honey. Have a good night."
            MC "You too, Mom. Bye."
            "I hung up the phone and glanced down at the screen as the \"call ended\" sat there for a moment."
            "Talking to Mom...felt nice."
            "It was different from when I was at home. When I was here, it was nice to know that she was thinking of me and Tomo. Made me feel loved."
            "I grunted a bit and sat up on my bed."
            "..."
            MCT "It feels more like a home already."
            jump daymenu

        "Head out to the balcony":
            $setFlag("MC004_balcony")
            "I glanced at my balcony, and the sunlight that was streaming onto it, illuminating the deck in a soft glow."
            MCT "If video games have taught me anything, I should head out there."
            "I walked to the door and pulled it open, stepping outside."
            scene Dorm Exterior with fade
            MCT "Hm. Not bad."
            "I glanced around, and at the balconies on either side of my own."
            "All of them were made in quite a sound manner, and based on the heavy duty hardware that I could see under the one beside mine, it could likely handle more than a few people."
            MCT "Or one or two with a heavy duty factor."
            "I put both hands on the railing and gazed out, then looked back to the balcony beside mine."
            "A white shirt and some blue shorts hung over the railing and flapped in the breeze."
            MCT "I've been here for... at least a few weeks, and it's just striking me now that I have neighbors."
            "I'd never met the students on either side of my dorm, though I was sure that Daichi likely knew their home address, legal first and last names, blood type, favorite colors, and name of the first person they kissed."
            "I glanced back at the clothes hanging from the railing."
            if checkSkill("Athletics", ">", 3):
                MCT "Seems like the dude takes his fitness seriously. Those are athletic clothes."
            else:
                MCT "I... wait, aren't those the clothes they gave us for athletic stuff? I think I have some like that somewhere too."
                MCT "I should really find those..."
            "Each student had been given an athletic outfit, and had been instructed to come to them should we need to order a new size."
            "It was comforting to know that the support was there... but also kind of foreboding."
            if isEventCleared("BE003"):
                MCT "Maybe the dude is into soccer or something?"
                MCT "And that reminds me that Honoka has a soccer game tomorrow."
            else:
                MCT "Guess he's a fan of air-drying."
                "I glanced down at the ground below."
                MCT "Screw that. I'm not going chasing my boxers if they flutter down to the courtyard."
            "I sighed and looked out over the courtyard between the two dorm buildings."
            "There was sort of a mini-terrace looking area in between, with a pathway and some plants around it."
            if getHighestAffection() == ("BE"):
                show BE neutral with dissolve
                MCT "Oh, shit!"
                MC "Heeeyyy! Honoka!"
                "I waved one arm overhead as Honoka stopped in her tracks and looked around for whoever was calling her name."
                show BE happy
                "Finally, she looked up."
                BE "Hey! Kei-chaaaaan!"
                "Both of us started laughing as she waved back and continued on her way."
                hide BE with dissolve
                "I smiled and put both hands on the railing around my dorm, grateful for the feeling of familiarity that Honoka brought."
            elif getHighestAffection() == ("AE"):
                show AE neutral with dissolve
                "Down the path, Shiori walked in a quick sort of manner, heading off toward the direction of the school."
                "I raised one arm to wave, but brought it back down as she walked past, already out of the range of my gesture."
                MCT "Probably heading to a student council meeting most likely."
                hide AE with dissolve
            elif getHighestAffection() == ("FMG"):
                show FMG neutral with dissolve
                "Below, Akira walked by, looking about and admiring the foliage and the like."
                MC "Ey! Mizutani-san!"
                show FMG happy
                "Akira looked up toward me."
                "She waved at me vigorously as I returned the gesture, then let her go on her way."
                hide FMG with dissolve
            elif getHighestAffection() == ("GTS"):
                show GTS neutral with dissolve
                "I glanced toward the side away from the campus and spotted Naomi walking slowly, looking at the various bits of shrubbery and foliage in the terrace."
                "Her eyes went up along the sides of the building and rested there, then went over, finally landing on me."
                show GTS happy
                "Naomi beamed and waved at me as I returned the gesture."
                hide GTS with dissolve
                "I watched her continue on and back around the dorms, likely to her own as I put both hands on the railing and inhaled the clean sea air, then glanced back at Naomi."
                "..."
                MCT "I think... she's a little taller."
            elif getHighestAffection() == ("WG"):
                "I glanced down and along toward the school."
                show WG neutral with dissolve
                "Alice was walking slowly along, the sunshine making her golden hair shimmer."
                "I considered calling out to her, but thought better of it. I didn't want to frighten her."
                hide WG with dissolve
                "I simply rested my hands on the railing and watched her walk around the dorms, her body swaying gently with each step."
            elif getHighestAffection() == ("PRG"):
                "I brushed the hair out of my face, only for it to flop back down as I looked toward the side away from the school."
                show PRG neutral with dissolve
                pause .5
                "Aida was walking alone in the middle of the terrace, heading for the school."
                "In her arms was a cream colored file folder, held tightly to her chest, and based on her gait, she seemed to be in a hurry to get that document to... somewhere."
                MCT "Probably running an errand for Alice."
                "I leaned over the railing a bit and held my arm out, waving over my head."
                MC "Hey, Kodama-san!"
                show PRG surprised
                "Aida immediately whipped her head up toward me."
                show PRG embarrassed
                "Seeing me, she blushed a bright red and waved quickly with one hand, before continuing on her way."
                hide PRG with dissolve
            Student "Ey."
            "I blinked and glanced toward the voice beside me."
            "On the balcony with the clothes hanging was who I assumed to be the clothes' owner. He was a fairly skinny, slightly shorter guy, with a bit of stubble."
            MC "Yo."
            Student "You got nothing going on tonight either?"
            MC "What gave you that idea?"
            Student "Do you stand on your balcony when you have major plans going on?"
            MC "Good point."
            $setFlag("Meet_Genji")
            Student "Genji Nakayama. Fukuoka."
            MC "Ah..."
            MC "Keisuke Hotsure. Tokyo."
            MC "Nice to meet you."
            Genji "Likewise."
            "Genji felt the t-shirt hanging from the railing."
            Genji "Hagh. Still damp."
            MC "Dryer break down?"
            Genji "Nah. I have practice soon and was hoping that hanging it in the wind would get the job done faster."
            MC "Ah."
            Genji "So Tokyo, what's your story?"
            MC "My story?"
            Genji "Mhm. Before you got all factorized."
            MC "Well, there isn't too much to tell. Grew up in the Shibuya ward of Tokyo with my sister. Lived in a smaller house with my parents. Pretty standard. You?"
            Genji "Pretty much the same deal, to be honest."
            MC "Cool. Island feels pretty small by comparison, doesn't it?"
            Genji "Tell me about it. The quiet has been messing with me a bit. Makes me feel like something bad is about to happen."
            MC "I get that. Can't take the big city out of you, I suppose."
            Genji "Guess not."
            Genji "So... how'd your family take the news when you came here?"
            MC "Well... Dad was curious and a little... I guess unbelieving of the whole thing. Mom was panicky, I guess. She definitely was the more concerned of the two."
            Genji "Same deal with me as well, save for a different city and no siblings. The thing I always think about though, is what would they say?"
            MC "Huh? Like, in what context?"
            Genji "Here. What would they say if they saw all of this?"
            Genji "Like the history teacher, for instance. What would they say if they saw that tongue flop out down to his waist right before their eyes?"
            Genji "It sounds fictional if you don't see it yourself. But it's right there."
            Genji "It's... strange to think that that sort of thing can happen to us."
            MC "Yeah. I suppose they'll see it eventually, like it or not. It's nice to know that this isn't happening when we're all alone, though. Like, it's nice to have a support system for it."
            MC "Doesn't make the concept of it any less wild though. Like... it's pretty mind blowing to consider that I can look and see something on my body having grown considerably larger in the matter of a few hours."
            Genji "It is."
            Genji "Well anyways, nice chatting with you."
            MC "Yeah, likewise. See ya."
            "Genji nodded and walked back into his dorm."
            stop music
            MCT "Hm. Nice guy."
            MCT "Wonder what his factor is, though. Maybe he's got a weight gain factor or something."
            "I stopped myself and glanced up at the sky."
            MCT "... Maybe I should be focusing more on the kind of person he is, rather than how his body is going to change. These are people that are growing, after all."
            "I turned and walked back into my dorm, shutting the door behind me."
            scene Dorm Interior with fade
            MCT "..."
            MCT "Yeah, I'm still hungry."
            "I walked to my fridge again and opened it, rummaging through."
            "My phone erupted with rings from my pocket, and I sighed, standing up and reaching into my pocket."
            "I glanced down at the screen with a slightly worried pit in my gut."
            MCT "Well... talk about her, and she shall appear."
            "I swiped over on my screen."
            MC "Hello?"
            MomCell "Keisuke? Are you alive?"
            MC "Uh... yeah?"
            MomCell "Could have fooled me. I heard Tomoko's voice before I heard yours."
            MC "Wait, seriously?"
            play music MC
            MomCell "... Well, I heard her voice via her voicemail, but still. I was hoping to hear from you sooner."
            MCT "She acts like I've had better luck than her..."
            MC "Yeah. Sorry about that, Mom. Things have been a little crazy here."
            MomCell "I would imagine so."
            MomCell "What are you up to today?"
            MC "Just got back to my dorm. I had some classes earlier, and now I'm just relaxing for a little bit."
            MomCell "I see. Make sure you take some time for that. It's not good to run yourself ragged."
            MC "Yeah, I know."
            MomCell "So, how is it otherwise, Keisuke? Are you doing alright? Feeling okay?"
            MC "I-I'm fine, Mom. No need to worry."
            MomCell "I... I know, Dear. I know. I just worry about you and Tomoko."
            "The line went dead for a few seconds."
            MomCell "So... do you know what... growing thing you have?"
            MC "You mean my growth factor? Yeah. Yeah I do."
            MomCell "Well, out with it then. Don't hold me in suspense."
            MC "I have a hair factor."
            pause .5
            MomCell "Ah... {w}hair factor?"
            MomCell "Like... the hair on your head, right?"
            MC "Yes, Mom. I'm not turning into a sasquatch. At least as far as I can tell so far."
            MomCell "Alright, alright. So, how does that work?"
            MC "Well, my hair has been growing faster and faster now. Like, I can cut it, and it'll grow back really quick."
            MomCell "Wow... I'll be frank, Keisuke. With what I'd heard, I assumed it was going to be something more severe. Like you'd be as tall as a building when I saw you next."
            MomCell "What about your sister? Is she doing okay?"
            MC "She's about the same. She has the same factor as I do."
            MC "And, she's really not overly fired up about the whole thing."
            MomCell "I see. And it works the same in women as it does for men?"
            MC "As far as I know, yes."
            MomCell "I see."
            MomCell "I... I'm relieved to hear that you two are okay, Keisuke."
            MomCell "Your father and I... well, we didn't know what to think."
            MomCell "The whole thing seems so out there..."
            MC "I know, Mom. It still feels a little far-fetched for me too sometimes. But... it's real."
            MC "Oh, you won't believe this. Honoka Inoue is here too."
            MomCell "Honoka? As in, your old friend Honoka?"
            MC "Mhm. We bumped into each other when I got off the ferry."
            MomCell "Wow. Small world. How is she doing?"
            MC "Good. She's definitely grown up."
            MomCell "I'm sure. I remember her playing in the mud in our backyard when you two were little. Remember that mud castle she tried making? She was so adorable.."
            MC "I... yeah. I think I remember that too."
            MCT "I also wouldn't put it past Honoka to try something like that now."
            MomCell "Well, I'm glad you have someone you know there with you and Tomoko. Hopefully, it'll make the whole process a lot easier."
            MomCell "Have you met anyone else?"
            MC "Yeah, quite a few people."
            if getHighestAffection() == ("BE"):
                MC "I've been mainly hanging out with Honoka, though."
                MomCell "That's good to hear, Dear. She was always a sweetheart."
            MomCell "I'm glad to hear that you've been putting yourself out there. I think it'll help make this whole thing a lot easier to deal with."
            MC "Yeah, hopefully."
            MC "Is Dad doing okay?"
            MomCell "He's about the same. Working a lot of hours, but he's doing well. He misses you two, though."
            MomCell "Feels strange being empty nesters now, you know."
            MC "Heh, I suppose so."
            MC "Feel old yet?"
            MomCell "Oh, don't even start that."
            "My mom and I both laughed over the phone."
            MomCell "Have you made any plans for Golden Week yet?"
            MC "Not yet. Probably gonna see what there is to do here when that gets a little closer and figure it out then."
            MC "We have a test right after the holiday break, so I'll probably try to study for that a little."
            MomCell "I know you, Keisuke. You say that, but will you really?"
            MC "Ouch."
            MomCell "I'm just teasing, Dear. I'm sure you'll put in the time."
            MomCell "Well, Dear. I'll let you go. I'm sure you've got something fun planned for tonight, and I wouldn't want to interrupt that."
            MomCell "It was nice to hear from you though, Honey. Keep us in the loop if you can, okay?"
            MC "I will, Mom. Sorry it took me so long."
            MomCell "Oh, it's okay. I understand. New school, new people, crazy body changes going on. I don't blame you."
            MC "Thanks Mom. I love you."
            MomCell "Love you too, Keisuke. And tell Tomoko to give me a call, would you?"
            MC "I'll try, but she never listens to me."
            MomCell "It's the effort that counts."
            MomCell "Bye, Honey. Have a good night."
            MC "You too, Mom. Bye."
            "I hung up the phone and glanced down at it, then went and sat down at my desk."
            MCT "Hm."
            MCT "Somehow... it already feels better in here."
            jump daymenu

label MC005:
    scene Dorm Interior with fade
    play music HigherEdu
    "{i}CREEEEAK{/i}"
    pause .5
    "{i}CREEEEEEEEEAK{/i}"
    "I brought all four legs of my chair back down to the floor, looking up from my phone screen to my laptop screen staring coldly back at me."
    MCT "Take a picture. It'll last longer."
    MC "Augh..."
    "I rubbed my forehead and set down my phone, setting properly once more so I could actually do what I sat down to do."
    "On my screen was a blank text document with about a sentence and a half of lines typed out."
    MCT "What sort of sadist gives an assignment over Golden Week?"
    "I looked back at the page, then to my notebooks beside it, where I had some notes from the last day of class prior to our short break jotted down. And above it all were the words \"TEST\" written near the top."
    MCT "And a test, too. I'm gonna lose it, I swear."
    "I let loose a groan and leaned back in my chair again, putting my feet onto my desk and looking at my phone again."
    "It was around two in the afternoon, and as I looked at the time, my eyes wandered down to the date."
    MCT "God... a month already?"
    "It really didn't feel that long, especially in the grand scope of things."
    "Sitting on the ferry with Tomo watching the island appear in front of us had seemed so unnerving at the time. But now a month later, the island was beginning to feel fairly routine, even a little homey at times."
    "I got up from my chair and shuffled into the kitchen for some water."
    play music RM
    show RM neutral with dissolve
    RM "Yo."
    MC "Ey."
    "Daichi shut the door behind himself as he came in and set his bag down on his bed."
    show RM doubt
    RM "Hm."
    MC "What? What's with the inspection?"
    show RM neutral
    RM "Nothing. I'm simply a little taken aback that you aren't out spending time with your beloved. Especially on Showa day."
    MC "My... what?"
    if getHighestAffection() == "BE":
        RM "Inoue-san. I'd expect you'd be off with her instead of sitting around here."
        MC "Well, the paper from class seemed to take priority."
        MC "Besides. Honoka won't be upset if I take some time to work on homework."
    elif getHighestAffection() == "AE":
        RM "You know. Matsumoto-san. I'm surprised that you aren't off spending time with her instead of sitting around."
        MC "I figured the paper ought to come first. And, I believe she'd agree with me."
    elif getHighestAffection() == "GTS":
        RM "Yamazaki-san, of course. I assumed you'd be spending your time with her rather than sitting around here."
        MC "The paper and studying for the test coming up seemed a little more important for the moment. And, I don't doubt Yamazaki-san is doing something similar."
    elif getHighestAffection() == "FMG":
        RM "All I'm saying is shouldn't you be off lifting things with Mizutani-san or something?"
        RM "Why exactly are you here and not with her?"
        MC "I... wanted to get some work done on the paper and test we've got coming up."
    elif getHighestAffection() == "WG":
        RM "The heiress, obviously. Nikumaru-san, if I'm remembering her name correctly. I've noticed the shine you've taken to her."
        MC "It's... there's no shine."
        show RM smug
        RM "Of course there isn't."
        show RM neutral
        RM "Anyway, what brings you here?"
        MC "Working on the paper and studying a bit for that test coming up. Getting it out of the way sounded nice."
    elif getHighestAffection() == "PRG":
        RM "You've been hanging out with that one girl, haven't you? Kodama-san, right?"
        MC "Uh... yeah?"
        RM "So, why are you here and not with her?"
        MC "Just... working on the paper. Probably gonna study for the test, too. I'm sure Kodama-san is doing the same."
    show RM doubt
    RM "And, how is your work going?"
    MC "... I wrote a few lines."
    show RM concerned-2
    RM "Well, look. I'm not going to push you into socialization. That's not the way I do things."
    RM "But, it is a holiday, so don't go too crazy."
    MCT "You telling {i}me{/i} not to go too crazy? Sounds a bit hypocritical."
    MC "I'll try to remember to take a break. Thanks."
    MCT "As if my work so far hasn't been one giant procrastination mess."
    show RM neutral
    RM "Of course."
    RM "And, if you want to have some real Golden Week adventures, you know where to find me."
    MCT "Do I?"
    MC "Uh... yeah. It'll be a long week, but I'll keep that in mind."
    hide RM with dissolve
    play music HigherEdu
    "Daichi walked off to his desk and sat down as I went back to mine, my tall glass of H2O in hand."
    "I sat forward in my seat and opened a few tabs in my internet browser for research."
    MCT "If I finish the paper first, then I'll have more time to study for the test."
    MCT "Obviously both are important, but I have to get my nose to the grindstone on something here."
    "I brought my fingers to the keys and stared at the blinking line in the search engine bar."
    "..."
    "..."
    MCT "Come on..."
    "I looked back at my notes, then looked back at my screen."
    MCT "Dammit..."
    "Suddenly, a blinding ray of sunshine curled in through the window and hit me right in the face."
    MC "Ach..."
    MCT "No. Not now, Mother Nature. You aren't helping."
    "I stared out the window for a bit."
    MCT "... Yeah, this blows."
    "I shut my notebook and closed my laptop lid, which even though I hadn't really gotten anything done, felt amazing as all heck."
    "I got up and sat on my bed, pulling my phone back out."
    "I had total holiday break-itis. Technical definition being the feeling of having all the time one could ask for, but having no idea how to spend it."
    "I leaned over to my nightstand and opened up the drawer to fish for my handheld. Some mind numbing games for a while seemed to fit the bill perfectly."
    MCT "... What the hell is that?"
    "I fished around and yanked up the foreign object from within and looked at it."
    if isEventCleared("MC002"):
        "It was a bag. The same one I'd received from Takamura-sensei on my first day on the island."
    else:
        "The same one I'd received from that teacher at the dock on my first day."
    pause .5
    "... And it was still mostly full."
    MCT "Good agency, me."
    "I pulled it out and into my lap, and spread its contents out in front of me."
    MCT "Hmm... nothing super interesting."
    MCT "It's mostly just introduction stuff."
    "I pulled out a trifold brochure from inside and unfolded it."
    "Images of the island and different locations on it were spread all across it, with little descriptions and text bubbles alongside them, pointing out different odds and ends."
    MCT "Hm... almost forgot about the town."
    "Pictures of the town stuck out to me, featuring a ton of different locations, some of which were new to me."
    if isEventCleared("BE012"):
        MCT "Oh dang... that's the arcade I went to with Honoka that day."
        MCT "I'll have to remember to hit up the bus sometime and head down there."
        "I looked at the arcade in the photo."
        MCT "Even in photo form, I can almost see the flashing lights."
        pause .75
        show RM neutral with dissolve
        MCT "Yeah, I'm heading out."
        "I got off of my bed and walked to the door, yanking my shoes on, and stuffing the brochure into my pocket."
        MC "I'll see you later."
        RM "Hm?"
        MC "Going out."
        RM "Ah. Yeah, see you."
        hide RM with dissolve
    elif isEventCleared("GTS009"):
        MCT "This totally reminds me of that day I went down there and ran into Honoka and Yamazaki-san."
        if getFlag("GTS009_Honoka"):
            MCT "And I got Honoka that pin, too."
        if getFlag("GTS009_Naomi"):
            MCT "And I picked up that headband for Naomi."
            MCT "She really knows how to show appreciation. Can't deny that."
        if getFlag("GTS009_None"):
            MCT "And I totally skimped out on buying something for either of them."
            MCT "Well, chalk that down as a way to look like a dick."
        "I looked at the photos of the streets of the town in the sunshine and the welcoming, friendly looking storefronts streaming down the length."
        MCT "Think I've done enough work today."
        "I slid the brochure into my pocket and got up."
        show RM neutral with dissolve
        MC "I'll be back later."
        RM "Hm?"
        MC "Don't wait up."
        RM "Ah... alright?"
        hide RM with dissolve
    else:
        MCT "That's... a decent sized supermarket for such a small island."
        MCT "Oh God... burgers..."
        MCT "And a..."
        MCT "... That's an arcade."
        MCT "I need to go see this town."
        "I hoisted myself off the bed and to the door, quickly putting my shoes on, and stuffing the brochure into my pocket."
        show RM neutral with dissolve
        MC "I'll see you later."
        RM "Hm? Yeah, later."
        hide RM with dissolve

    scene Dorm Hallway with fade
    play music DayByDay
    "I walked out the door and locked it behind myself."
    MCT "I know I have to do that paper. Like, I have to."
    MCT "But, it feels good to just be out for a bit."
    MCT "Hell, it's a holiday. It's meant to be enjoyed."
    "I set my key back in my pocket and walked off down the hall with a bit of extra spring in my step."
    "I was an explorer. A man with drive."
    "Not drive to write papers, of course. No, drive for seeing that which must be seen."
    scene Dorm Exterior with fade
    pause .5
    MC "Ohhh yeah..."
    "The sun lovingly wrapped around my body as I walked into it. As if telling me that shirking my studies had been the right call."
    MCT "Perfect..."
    MCT "Okay. Bus stop, bus stop... should be this way."
    "I started walking a bit, going from the dorms toward the center of campus."
    scene Campus Center with fade
    "Seeing as how the center of campus had become a sort of landmark for me, I always felt a sort of comfort in seeing the large tree in the middle, and the benches on the paths around it."
    MCT "Now... left here. Yep."
    play music AE
    show AE neutral with dissolve
    "Up ahead, Shiori was walking on the path out of the academy, coming toward me."
    "With each step she took, a certain... jiggle caught my eye."
    MCT "God... she really is growing."
    if isEventCleared("AE010"):
        MCT "Like, I didn't really notice it until she deliberately started hiding it, but... wow."
    else:
        MCT "It's a little hard to tell when she's seated in front of me in class. But out and about... it really shows."
        MCT "... What do the coming months have in store around here?"
    MC "Hey. Afternoon, Matsumoto-san."
    AE "Good afternoon, Hotsure-san."
    MC "I presume you're off to celebrate Golden Week in your own way? Maybe explore the island a bit?"
    show AE neutral-eyebrow
    AE "You presume?"
    MC "W-Well, I mean it like... you know what I mean, yeah?"
    show AE neutral
    AE "Hm. Well, no, actually. I will be performing an inspection of the campus to ensure the festivities don't cause too much uproar. Afterwards, I plan on filing documents and finishing my studies for this chapter."
    MCT "Geez! Don't say that like it's normal!"
    AE "..."
    MCT "I legitimately dread the idea she can somehow read my mind and the scary part is that I wouldn't put it past her."
    MC "I see. Well, have a good time all the same."
    AE "Same to you, Hotsure-san."
    hide AE with easeoutleft
    MCT "Preparing for class on a holiday? Of all things?"
    "I made sure she wasn't looking and shook my head as I walked toward the bus stop."
    MCT "Damn..."

    scene School Front with fade
    play music Sunset
    "A few minutes and some steps later, the bus stop outside the gates of the academy loomed ahead."
    "Being the only one there, I sat down and stretched myself out a bit, looking out at the road in front of me."
    MCT "After spending so much time here now, leaving even for a bit feels so alien. Almost like I'm doing something I'm not supposed to be."
    if getFlag("VisitedTown"):
        MCT "But why though? I've done this before."
    else:
        MCT "But why? It's advertised along with the rest of the island."
    "I shook my head."
    MCT "Think I'm just going stir crazy."
    "I looked down at my feet, and picked a spot on my fingernail."
    "It wasn't too long until a sound I hadn't heard in what felt like years hit my ears, and I glanced up."
    "The bus pulled up to the stop in front of me and halted, the doors swinging open, as I, in a way, welcomed the smell of gasoline and off-patterned seating and climbed aboard."
    scene Bus Interior with fade
    "As I chose my seat, I sat down and rested my head against the headrest."
    MCT "Mmngh... long drive time."
    "The academy faded out of view behind me as I watched the mountains and forests pass by the window."
    "The bus was empty, save for the driver, who I hadn't really gotten a solid look at, but who I imagined knew this route like the back of his hand."
    menu:
        "Read the brochure":
            $setFlag("MC005_readbrochure")
            "I pulled the now slightly wrinkled brochure out of my pants pocket and unfolded it again."
            MCT "Nice of them to actually have a brochure."
            pause .5
            MCT "Would've been nicer if I'd read it before now, but hey, hindsight."
            "I found the section where I'd left off and picked up by the academy."
            MCT "Hm... I didn't know the school was founded by a member of the National Diet."
            pause .5
            MCT "Hold up..."
            if isEventCleared("FMG011"):
                MCT "That's the rec room I accidentally found my way into the other day. Right..."
            else:
                MCT "The academy has a rec room?"
                MCT "... With arcade games?"
                MCT "Why the hell didn't I read this earlier?!"
            "I kept reading through the brochure as the bus rode on into town."
        "Browse the internet":
            $setFlag("MC005_browseweb")
            "I slipped my phone out of my pocket."
            MCT "Thank God for smartphones."
            "I scrolled through, eventually clicking my internet browser to catch up on the latest news articles and stuff."
            "Going past the more topical crap at the top, I came down to the weirder articles near the bottom."
            MCT "15 worst pop songs of the 2000's. Five things you didn't know about Legends of the Stormfall."
            MCT "Ugh. All the same shit."
            MCT "Hold on... 14 unusual plants?"
            "I clicked on the article and scrolled through a bit."
            MCT "Hm... there's a flower called \"chocolate cosmos?\" Sounds more like a fancy candle or something than a flower."
            MCT "And it's insanely rare? Huh."
            MCT "Yamazaki-san would have a field day with this."
            $setSkill("Art", 1)

    scene Town Bus with fade
    play music BrightLights
    #sfx crowd chatter
    MCT "Eesh. Crowded."
    "I took my few steps down off of the bus and stared down the street, taking in the clusters of people around me."
    MC "Okay..."
    "I turned myself around, gathering myself."
    if getFlag("VisitedTown"):
        MC "So, I should go this way again."
    else:
        MC "I guess... this way?"
    "I picked a direction and started off on a sort of reconnaissance walk. Not really having anywhere specific to go, but still taking everything in around me."
    scene Town Shops with fade
    "One of the first places I saw across the street was a large, high end looking restaurant, made up in a traditional style, with lamps to accent its look."
    MCT "Don't know if I'll ever need to go there for anything, but hey, better to know of it than not. Maybe if my parents come to town... erm, island, I guess."
    "A few doors down from it was a large clothing store, and a burger restaurant alongside it."
    MCT "Ooh Lord. A burger... gah, that sounds perfect."
    "I walked along, ignoring the cries of my pathetic, weakling stomach, and glanced ahead."
    "A café lay nestled amongst the other buildings along the right hand side of the road. Even just walking by it brought on feelings of sitting at a table with a mug in two hands and a sweater tied around my waist."
    "I waited for the one or two cars to pass by before crossing the road with some other waiting pedestrians, and glanced down the side street."
    "I saw the sign of a konbini store peeking out from behind a building, along with a pharmacy across the street from it, and a supermarket nearby."
    MCT "Huh. Good to keep that in mind."
    "Before I'd even finished crossing the street, a smell that reminded me of home, holiday get-togethers, and the word \"comfort\" shot up my nose."
    MCT "Oh my..."
    if isEventCleared("FMGWG001") or isEventCleared("MC007"):
        "I turned right just as I crossed and spied the source of the devilish scent. Kazomazumi Bakery. Right on the other side going down toward the konbini."
        MCT "Ah, I remember you. Smelling lovely today."
        pause .5
        MCT "... For whatever reason, that sounds creepy."
    else:
        "I turned right just as I crossed and spied the source of the devilish scent. A bakery. Right on the other side going down toward the konbini."
        MCT "..."
        MCT "This makes me happy on so many levels."
    "Once again, I fought every urge to dive into the bakery and devour every bit of gluten-y goodness within, and I kept up my stride."
    MCT "God, I knew there was some stuff down here, but I never expected this."
    "Down toward the end of the street was a large park, and on the block leading up to it was a bright, shiny arcade, a quiet, almost isolated looking game shop, and down a small side street, an ice cream parlor."
    "As I stopped to admire, the crowd of people that had been around me kept moving and passed me, heading onward."
    MCT "Huh? Where is...?"
    "The crowd of people worked their way to the park near the end."
    MCT "Hm."
    "I became the best of sheep and followed the crowd into the park."

    scene Park with fade
    play music DifferentPaths
    "The park, for its size, was about as crowded as I could've imagined it being."
    "Every bench along the walking paths was taken, and picnickers sat out on blankets, enjoying the sunshine with their meals."
    MCT "Wow... this is so much like home."
    "The whole thing was really shaping up to be a fairly large event, by the looks of it. Especially so, given that I could've never imagined so many people on the island at once."
    "And yet, the whole thing carried a cover of respect to it. That, no matter what had led up to it, there was a reason everyone was gathered."
    MCT "Reminds me of that one year with the bonfire in Yoyogi Park with Honoka back home."
    MCT "She stole my burger and was sprinting around with it, if I remember right."
    MCT "Never got that burger back, either."
    MCT "And Tomo was there, too. She loved the fire."
    "I smiled, reminiscing on running around with my childhood best friend and my sister while simultaneously taking breaks to watch the bonfire blaze brightly."
    "I glanced around a bit as I came back down to Earth."
    show HR unique at Position(xcenter=0.25, yalign=1.0)
    show Tsubasa neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    #show Chiyo neutral with dissolve
    if isEventCleared("MC002") or isEventCleared("PRG011") or getFlag("Meet_Tsubasa"):
        MCT "Oh! Tashi-sensei and Tsubasa-sensei!"
    else:
        if not getFlag("Meet_Tsubasa"):
            $setFlag("Meet_Tsubasa")
        MCT "Oh! Tashi-sensei and... that's Tsubasa-sensei... I think. The biology teacher, if I'm remembering right."
    MCT "And... who's that?"
    "Just as I started to walk toward them..."
    hide HR
    hide Tsubasa
    with dissolve
    #hide Chiyo with dissolve
    "Speaker" "On this day, we remember the great Emperor Showa, and the period of shining peace that he granted us in his reign!"
    "A man came up to a microphone on one edge of the park and began to tell the story behind the Showa era, and Emperor Showa himself."
    "I listened and looked down for a moment."
    "This whole celebration reminded me of home, and of my parents."
    "The tale the speaker told was a familiar one, and though I still held respect for it, I had heard it many times before, so by the time it ended, I raised my head and continued onward to Tashi and Tsubasa."
    show HR neutral-2 at Position(xcenter=0.25, yalign=1.0)
    show Tsubasa neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    #show Chiyo neutral with dissolve
    HR "... deeper than that. It's representative of Japan, and every person who lives-"
    show HR unique-2
    Tsubasa "Hotsure-san. Morning."
    "Tashi quickly turned his head and adjusted his collar a bit."
    show HR annoyed
    HR "Ahrm... yes, hello Hotsure-san."
    show HR unique
    "I bowed to both of them politely."
    $setFlag("Meet_Chiyo")
    show HR unique-2
    Chiyo "Hotsure-san? I don't believe we've met."
    Chiyo "A student of yours, dear?"
    Tsubasa "Not in my homeroom, no. This is Keisuke Hotsure, one of Kaeru's students."
    Tsubasa "Hotsure-san, this is my wife, Chiyo Tsubasa."
    MC "It's wonderful to meet you, Tsubasa-san."
    "I bowed to her as well as she did the same to me, giving me a gentle smile of greeting."
    MC "My apologies. I didn't mean to interrupt you, Sensei."
    show HR neutral
    HR "It's not any trouble."
    show HR unique
    Tsubasa "Kaeru-san was simply reiterating his passion for this holiday as a whole."
    Chiyo "You make it sound so childish, Michi-kun. The man has a passion for the past. When images and text might fail, the spoken word will last the test of time."
    show Tsubasa annoyed
    Tsubasa "I understand darling, and meant no such thing. Go on, Kaeru."
    show Tsubasa neutral
    show HR neutral
    HR "I... didn't exactly have an ending in mind. All I was saying was simply that I believe that many people have lost their perception on how important this time of year is, and what it represents."
    HR "I believe it not only important to use the time for reflection, but also for taking in the historical significance of it all. Why we celebrate, and what it all means."
    HR "It's much more than just \"a topic to assign homework to.\""
    show Tsubasa intrigued
    show HR unique-2
    Tsubasa "I understand entirely. Times have changed immensely, and keeping a memory of the way things were is a sound idea."
    Tsubasa "Take this, for example. I remember, clear as day, the 1964 Summer Olympics in Tokyo."
    MC "You went to the Olympics, Tsubasa-sensei?"
    show Tsubasa satisfied
    Tsubasa "I did, indeed. I was quite young at the time, however, my father took me to Tokyo and somehow managed to secure us two tickets through some wild stream of favors and I-owe-yous."
    MC "Wow..."
    Tsubasa "Quite right. It was an astounding sight to see. The first modern Olympics after World War II, and the first ones held in Asia."
    Tsubasa "The pure energy of the crowd, the efforts of each athlete, it all felt done in celebration. It was... wonderful."
    show Tsubasa neutral
    Chiyo "Hmph. Always a surefire way to turn you into a child again, dear."
    Chiyo "I followed it in newspapers myself as a child. Since my family lacked a TV, I couldn't watch along like I would have preferred. But all the same, it was a wonderful time indeed."
    Chiyo "However, going back to what you were saying, Michi-kun, times have changed quite a bit since we were young."
    Chiyo "Oftentimes, it feels almost difficult to stop and smell the roses, you know."
    MC "I understand completely."
    Chiyo "In what way?"
    MC "Ah... well, I'd say in reference to how things always seem to just move faster, in comparison to the years past."
    Chiyo "Ah."
    Chiyo "Smart class you two have this year, hm?"
    Tsubasa "Well, you've done your part in winning my wife over, Hotsure-san."
    MC "Do you also work at the academy, Tsubasa-san?"
    Chiyo "Oh, no. I'm not quite fit for lesson plans and so on."
    Chiyo "I run a small convenience store in Satoyama Village. It's not necessarily an exciting position, but it's simple and keeps me on my toes."
    MC "I see. I'll have to remember to pay a visit sometime."
    Chiyo "See to it that you do, Hotsure-san. I'll be expecting you."
    "I nodded at her."
    MC "Anyways, I'll let you three mingle."
    Tsubasa "Enjoy the celebrations, Hotsure-san."
    Chiyo "It was wonderful meeting you."
    MC "You as well, Tsubasa-san."
    "I bowed to her politely, and nodded at Tashi-sensei as I left the small circle."
    MCT "Eesh. Pressure times three. Damn."
    #hide Chiyo
    hide HR
    hide Tsubasa
    with dissolve
    "I walked around the park for a little longer and admired the light decor for a bit."
    "It was kind of nice just milling about during this whole thing. Felt very... homey."

    scene Town with fade
    "After likely around half an hour of walking about and small talking my way through the park, I walked back onto the main street, which was now much less packed, and walked toward the bus stop."
    "It was kind of weird with the town being so quiet. The contrast was amazing, and when it was dead like this, you could likely walk down the middle of the street all the way and encounter nothing but open air."
    "I sighed to myself."
    MCT "Mnnngh... this is relaxing..."
    "I passed by the arcade, bakery, pharmacy, and the like, noting how many of them, save for the pharmacy and konbini store, were closed."
    "I continued on and managed to catch the bus just as it was leaving and climbed aboard."
    scene black with fade
    $setTime(TimeEnum.EVE)
    pause .5

    scene School Front with fade
    play music HigherEdu
    "I stepped off the bus and walked stiffly back through the academy's gates."
    "My legs felt like concrete after the long bus ride and the walking around prior to it."
    scene Campus Center with fade
    MCT "I really should've grabbed some food or something while I was there."
    MCT "Eh, I'll snack on something at my dorm."
    "My dorm."
    "The paper."
    "... And the test."
    "I let out a groan."
    MCT "Dammit, I really didn't wanna come back to that."
    "I took a deep breath."
    MCT "It's all good. I have a few more days for all that."
    scene Dorm Exterior with fade
    "I continued along the path toward the dorms, and turned off toward the men's dorms, heading down the hall toward mine."
    scene Dorm Interior with fade
    pause .5
    MC "Of course. No Daichi."
    MCT "Probably off doing his \"Golden Week Shenanigans\" or whatever."
    "I yanked my shoes off, set them by the door, then walked into the kitchen."
    MC "Mkay... what sounds good?"
    "I found a healthy college meal of a bag of chips and some water and sat down at my desk...{w} for a minute."
    "I got up almost immediately and crash landed into my bed, setting my water and chips down prior to this crash landing, of course."
    MC "Mmmmngh... yeah."
    MC "I've got a few days for tests and stuff."

    "..."
    $setTime(TimeEnum.NIGHTLIGHTS)
    show dummy with dissolve
    "..."
    $setTime(TimeEnum.NIGHT)
    show dummy with dissolve
    "..."
    $setTime(TimeEnum.DAY)
    show dummy with dissolve
    "..."
    $setTime(TimeEnum.EVE)
    show dummy with dissolve
    "..."
    $setTime(TimeEnum.NIGHTLIGHTS)
    show dummy with dissolve
    "..."
    $setTime(TimeEnum.NIGHT)
    show dummy with dissolve
    "..."
    scene black with fade
    $setTime(TimeEnum.DAY)
    pause 1

    scene Bathroom with fade
    play music MCGuitar
    MC "Agh... there."
    "I shook my head out in the water to rid myself of my shampoo and shut off the water, reaching for my towel."
    "I got out of the shower and dried my body off a bit, then ravaged my hair in the towel, tossing it like a salad."
    "I'd spent the last few days doing... well, almost nothing."
    "The bulk of it had consisted of trying to work on my paper or study for my test, getting bored, then getting distracted with something else, thereby yanking me away from anything productive."
    "Even at that, though, I had still gotten a bit of progress in on the paper. A bit meaning that it no longer looked like a blank canvas."
    "I had actually gotten some more references saved online, though, so when I did start working, I'd be able to hopefully just piece all of the bits together and go from there."
    "As for the test..."
    "...{w} Well, that would come in time."
    "I threw my hair out of the towel and wiped the remnants of the water from my shoulders."
    "I'd even had a quiet form for practically the entire time. I could count on one hand the amount of words I'd spoken to Daichi since the first day of Golden Week."
    "He'd been gone almost the entire time, only coming back at wickedly late hours of the night."
    "He'd gotten so good at making his exits, that I scarcely even heard the door open at night or in the morning."
    MCT "Now, how the hell does he not get curfewed? Like ever? Does he carry around one of those leaf-covered suits for \"emergency ducking and covering?\""
    "I scoffed. Daichi didn't seem like the kind of guy who enjoyed dirtying his clothes, but then again, he wasn't exactly the type to not do that, either."
    "I ran my brush through my hair and shook it out a bit, then brushed my teeth, put on deodorant, and cleaned off my excess trimmings from before my shower."
    scene Dorm Interior with fade
    play music Peaceful
    "I walked into my dorm, towel around my waist for my nonexistent roommate, and grabbed a pair of boxers."
    "I glanced around for my sanity, then dropped the towel and pulled my boxers on."
    "As the rest of my body dried a bit, I sat on my bed in just my boxers and took my phone from the nightstand."
    MCT "Hm... wonder how Tomo has been spending her Golden Week?"
    pause .5
    MCT "I'm an idiot."
    "I went to my messages with her and looked at the last one."
    MCCell "Yo."
    "I sent my admittedly short form text and clicked off onto my internet browser to scroll for a bit while she responded."
    "I'd seen her response times, and I wasn't about to sit there waiting."
    TomokoCell "Hey"
    "I clicked on it right away, hoping that now that she was texting back, if I responded fast enough, I could keep her in the active texting chain."
    MCCell "You care if I come over and annoy you?"
    "Surprisingly, another text came through very fast."
    TomokoCell "Sure? You know where I live, right?"
    if isEventCleared("MC003"):
        MCCell "Yep. Remember u gave it to me after we talked in the courtyard that day??"
    else:
        MCCell "Yep. You texted it to me awhile ago."
    TomokoCell "K"
    "I set my phone down and started finishing getting dressed. That was about as solid of a yes as one could get out of Tomo."
    "It was kind of nice not having to be anywhere at a specific time for a little bit. Classes weren't exactly difficult, of course, but the whole \"being up at X time\" got real old real fast."
    scene Dorm Exterior with fade
    MC "Damn. Nice day out."
    MCT "Or, by Tomo logic, \"better not waste it outside.\""
    "I walked along the path between the two dorms."
    MCT "I know the town had that celebration in the park the other day, but is the school going to do anything like that coming up?"
    MCT "I haven't heard of anything noteworthy, outside of the flower festival, but I feel like that's more of a town thing as well."
    Student1 "She's planning at least one a week. Maybe even two."
    "My ears pricked up, and I glanced at two male students walking toward the dorms."
    Student2 "Two movie nights in a week? Seems like something that the academy wouldn't let slide."
    Student1 "She's selling the idea based on making it as accessible to any student that wants to take part, so if they miss a day, they can just hit the other one."
    Student2 "But, wouldn't they just... miss that section, and part of the discussion about the movie, then? It sounds like it'll just leave everyone in the dust more than anything."
    Student1 "I... actually, I have no idea how she's going to make that work."
    "I passed by them and over to the women's dorms."
    "As I passed over, I glanced between the two dorms."
    show RM neutral with dissolve
    "Daichi was walking over to a group of people."
    "He struck up some sort of conversation with them, then just..."
    hide RM with dissolve
    "Walked away, a look of dejection on his face."
    MCT "... What the?"
    "I simply shook my head. Every time I saw him just cemented that he was likely from another planet."
    scene Dorm Hallway with fade
    pause .5
    MC "... Here it is."
    "I knocked at Tomo's door and waited a moment."
    pause .75
    MCT "... Okay?"
    "I knocked once more."
    MC "Tomo?"
    "{i}BSSSHIIIEW{/i}"
    "{i}CSSH! CSSSSH!{/i}"
    MC "..."
    "I reached down and turned the door knob, pushing the door in."
    scene Dorm Tomoko with fade
    #$setTime(TimeEnum.NIGHT)
    "Behind the door was a sea of pitch black dark. Amidst it, the only light was a square shaped laptop light bouncing up onto one wall."
    "Based on what I could see, blackout curtains were yanked shut over the window, along with what appeared to be a sweatshirt flung up on the curtain rod."
    $setTomoOutfit(OutfitEnum.CASUAL)
    show Tomoko neutral with dissolve
    "Tomo sat at her desk off to one side, a blanket over her shoulders as her laptop flashed in front of her. And, as usual, she had her enormous gaming headphones on, but based on how loud her speakers were, she'd forgotten to plug them in again."
    "I walked into the room and shut the door, then walked closer to her side of the room."
    MC "Headphones are out again, Tomo."
    "... Nothing."
    MC "TOMO! HEADPHONES!"
    show Tomoko surprised with vpunch
    Tomoko "AGH!"
    "Tomo yelped and turned around, her eyes wide."
    MC "Whoa, whoa. Sorry, sis. Didn't mean to scare you."
    show Tomoko annoyed
    Tomoko "It's... whatever."
    "She yanked her headphones off and set them aside."
    show Tomoko neutral
    Tomoko "I have to finish this game."
    MC "How's the connection speeds here? Haven't tried online much."
    Tomoko "A lot better than what I imagined."
    "I went to sit on her bed and nearly tripped backwards over a pile of clothes."
    MC "God, Tomo. Ever hear of a clothes hamper?"
    Tomoko "Heard of em."
    MC "Do you own one?"
    Tomoko "Yes, Dad."
    MC "Egh..."
    "I walked over to her blinds and threw them open."
    #$setTime(TimeEnum.DAY)
    MC "There."
    Tomoko "Uuugh..."
    MC "Come on, Sis. You could use some sun."
    show Tomoko annoyed
    Tomoko "You used to love the dark..."
    MC "Still do. I just realize that one needs balance."
    show Tomoko neutral
    "As I glanced down at the bed before sitting down, I noticed a smiley face sticker on the bed."
    MCT "Well, I see she's still into that. I wonder how many of these I could find around her room with some effort?"
    "I sat on the bed beside Tomo's polar teddy bear with the red hoodie."
    MCT "Wait... she actually brought this?"
    #show CG MC005_bear
    "I picked up the bear and looked at it in my hands."
    "The bear had been around so long that I didn't even remember Tomo receiving it, but I did remember her dragging it around everywhere she went as a kid."
    MCT "Polar. That's it's name."
    MCT "Huh. I know the bear means a lot to her, but I never would've pictured her bringing it along here."
    #show Tomoko side neutral
    Tomoko "Come on... go go go go go go go!"
    #show Tomoko side happy
    Tomoko "Yes! You suck!"
    "Tomoko raised one triumphant fist."
    "I smiled at her. For as quiet as she could be, she was a total nerd at heart."
    #hide Tomoko side
    #hide CG
    #show Tomoko neutral with dissolve
    MC "You still have Polar?"
    Tomoko "..."
    pause .5
    Tomoko "... Shut up."
    MC "I'm just teasing. No worries."
    MC "So, what's up?"
    Tomoko "Uh... nothing?"
    MC "Just... chilling out?"
    Tomoko "Mhm."
    MC "How's the hair?"
    Tomoko "It's there. My roommate helps me trim it from time to time."
    Tomoko "I really don't care, though. It's fine long."
    MC "Understandable."
    "I swished one hand through my own locks."
    MC "Your roommate out?"
    Tomoko "Yeah. She's in town or something."
    MC "You didn't want to go along?"
    Tomoko "Nah."
    MC "What about the last few days?"
    Tomoko "She went to town those days too."
    MC "Did you go?"
    Tomoko "Mm... no."
    MC "Oh... just been playing games?"
    Tomoko "Mhm. That and sleeping."
    "I glanced into the kitchen and noticed a few empty cups of ramen on the counter, and a dirty pot left on the stove."
    "On her now illuminated desk, a number of soda cans littered the surface of it, carefully pushed off to the side so as not to get in the way of complex mouse movement."
    MC "... Hey, Tomo?"
    MC "When... was the last time you went out?"
    Tomoko "I..."
    Tomoko "I went to the cafeteria for an energy drink the other day."
    MC "Which day?"
    Tomoko "The last day of classes."
    Tomoko "Look... I just don't like people, okay? I just want to play my games."
    MC "Tomo..."
    MC "You really shouldn't sit in here all day. It's going to drive you nuts."
    Tomoko "I've been enjoying it."
    MC "No, agch. Look, Tomo."
    MC "It's not healthy."
    show Tomoko annoyed
    Tomoko "Whatever."
    "She turned back to her computer, and I rolled my eyes."
    show Tomoko neutral
    MCT "... She's isolating again."
    MCT "She's always been rough in social situations, but if she keeps bowing out of society like this, her social anxiety is going to wreck her."
    MC "Tomo, please."
    Tomoko "Kei, I'm fine, okay? I don't need-"
    "{i}VREEEEEEM{/i}"
    show Tomoko distracted
    "Tomo glanced down at her phone."
    Tomoko "Hahhh..."
    MC "Mom?"
    show Tomoko annoyed
    Tomoko "No, worse. My roommate."
    show Tomoko distracted
    MC "I thought you said your roommate was okay?"
    Tomoko "She is, but... look."
    show Tomoko neutral
    "She turned her phone to me, which was open to her texts. In the string of messages from her roommate was one long column of text, and based on how far down Tomo had scrolled, I couldn't actually make out the top nor bottom of it."
    MC "What's she trying to tell you, there?"
    show Tomoko distracted
    Tomoko "Gossip. It's all gossip. Nearly every message."
    Tomoko "I don't hate her or anything, but she doesn't shut up sometimes."
    "She scrolled down through the string a bit."
    Tomoko "Today's slice is about our homeroom teacher, Takamura-sensei."
    if isEventCleared("MC002") or isEventCleared("BE006"):
        MC "Takamura-sensei? I've seen her around a few times. What about her?"
    else:
        MC "Okay? What about her?"
    Tomoko "Well, according to Count Blabbula, she was a super talented chef somewhere in Europe, and she was going to go on into 5-star restaurants and stuff."
    Tomoko "Then, out of nowhere, she just dropped that entirely, moved here, and applied for a position here."
    show Tomoko neutral
    MC "Huh... that sure is something. But is there any proof of this?"
    Tomoko "Sometimes there is with Yuki, sometimes there isn't. She basically hears something, then passes it on, proof or not."
    MC "Noted."
    MC "Well, look. I-"
    Tomoko "Egh, hold on."
    show Tomoko distracted
    "She looked down at her phone again."
    Tomoko "... I swear to God."
    show Tomoko neutral
    Tomoko "Look at this."
    "She handed her phone to me."
    Tomoko "Start at the top."
    if isEventCleared("RM002"):
        YukiCell "OMG! You aren't going to believe this!! Takamura-sensei was a chef in PARIS!! In like, a FIVE STAR restaurant with branches all over the world!"
        YukiCell "One is in Kyoto! And she left all of that behind to teach HERE! HOW CRAZY IS THAT?!! XOXO Yuki"
    else:
        UNKNOWNCell "OMG! You aren't going to believe this!! Takamura-sensei was a chef in PARIS!! In like, a FIVE STAR restaurant with branches all over the world!"
        UNKNOWNCell "One is in Kyoto! And she left all of that behind to teach HERE! HOW CRAZY IS THAT?!! XOXO Yuki"
    MC "Good Lord."
    Tomoko "... This is a daily thing."
    MC "I... see."
    if isEventCleared("BE006"):
        MC "Actually, come to think of it, Honoka mentioned something similar to me."
        MC "Apparently, she did attend culinary school in Paris."
        Tomoko "Hm."
    MC "Anyway, I'm gonna head back to my dorm and put some time in on the books for an assignment."
    MC "We should hang out more often, though. Get out and explore or something."
    if isEventCleared("MC003"):
        Tomoko "Hm, sure."
        Tomoko "Maybe next time you call, I'll actually pick up instead of letting you wait."
        MC "Ahp, ahp, hold on. I believe you mean \"wait for {i}days{/i}.\""
        Tomoko "As you can see by my texts, I have a lot to catch up on."
        MC "Yeah, right."
    else:
        Tomoko "Uh... okay, bro. If you really want to."
        MC "Hey, of course I do."
        MC "We can go into town or something. I saw an arcade there the other day."
        Tomoko "Okay, cool."
    MC "Alright. I'll see you around."
    Tomoko "Yeah. Later."
    scene Dorm Hallway with fade
    "I shut the door behind me."
    MCT "Ugh. She's like what younger me used to be like."
    "I thought back to the old days of playing online games until the sun came up, and downing soda like water."
    MCT "Good times."
    $setAffection("TM", 1)

    scene black with fade
    pause 2
    scene Dorm Exterior with fade
    play music Schoolday
    MC "Well, the scenery fits the day."
    "I walked out from the dorms and toward the center of campus."
    "It was Greenery Day. The day of plants, and all things that sprouted from the earth."
    scene Campus Center with fade
    "I'd never really been the biggest expert on the day, but just as it was with the other days of Golden Week, it was a remembrance holiday."
    "As such, I was doing my remembering by walking around campus and taking it all in. Admiring the foliage and whatnot."
    UNKNOWN "Psst."
    pause .5
    MCT "What..."
    UNKNOWN "PSSSST."
    "A super small stone clattered onto the walkway and just nicked the edge of my shoe."
    "I turned my head to the left to see a rather unassuming bush right up against the wall of the academy."
    "From it, I saw the top of a shaggy black head of hair, and the refraction of light from a pair of glasses."
    MCT "..."
    "I walked over to the bush."
    MC "Yes, Daichi?"
    show RM smug with dissolve
    "He popped his head up."
    RM "Golden Week Adventure. You in or out?"
    MC "I... now?"
    RM "I'm going to be outside the dorms in an hour. Be there if you want in."
    MC "W-Wait. What exactly are you up to?"
    "Daichi plunged back into the bush."
    hide RM with dissolve
    MC "... Nevermind."
    MCT "God, that guy is a damn wild card. What has he even been doing the last few days?"
    pause .5
    MCT "Anyway... speaking of, what do I want to do today?"
    "I walked further along, admiring the foliage as I went along."
    MCT "God, Tomo would hate today. An entire day about the world outside. Her own personal hell."
    MCT "... Though, she could use some time outdoors, probably. That is if her past activities have anything to say about her."
    scene School Planter with fade
    MCT "Not to mention that some time hanging out with her does sound fun."
    MCT "Seems like all she's done since we got here is sit in her room. Save for that roommate of hers, I'm pretty sure I'm the only company she's got."
    "I looked up, only then realizing that I'd wandered straight into the garden."
    MCT "Well...{w} green as ever."
    "If it was possible, the garden almost seemed more lush and vibrant than usual, as if someone had taken the saturation dial and cranked it past 11."
    "The trees were brighter, the flowers were more colorful, and the bushes seemed even more... bushy than usual."
    "Off to one side, Naomi stood, hanging a potted plant from a tree branch."
    MC "Good morning, Yamazaki-san!"
    show GTS surprised with dissolve
    GTS "Hm?"
    show GTS happy
    GTS "Oh! Good morning to you as well, Hotsure-san! And a very happy Greenery Day to you!"
    MC "Same to you!"
    "Naomi grinned and turned back to her potted plant."
    show GTS happy at Transform(xzoom=-1)
    if not isEventCleared("GTS002"):
        MCT "Wow, she's never this chipper. Is she like a \"plant mom\" or something?"
    show GTS neutral
    MC "So, what have you got planned today? Any Greenery Day adventures?"
    GTS "Well, I wanted to come here before I did anything else, so I could make sure the garden looked proper for Greenery Day."
    GTS "Of course, I'm planning to attend the flower festival in town once I'm finished here."
    MC "Oh? Where's that located? In the park?"
    GTS "Oh, no. There's a field just outside of town, absolutely replete with tulips. You will have no trouble finding it, I'm sure."
    GTS "I have the feeling the planners of the event wanted to hold it in a place as close to nature as possible. Untouched by humanity, if you will."
    MC "Yes... I can see that."
    if not isEventCleared("GTS002"):
        MC "You seem pretty excited, Yamazaki-san."
        MCT "For probably the most boring day of Golden Week."
        show GTS neutral
        GTS "Ah, not to excess, I hope. But I do love a well-tended garden, and this is a day for people of all stripes to share in an appreciation for the greenery in our lives."
        GTS "It's quite a beautiful thing in itself."
    "Naomi brushed her hands together and stood back to admire the pot."
    GTS "There."
    MC "Looks great!"
    GTS "Thank you!"
    pause .5
    GTS "Well then, what do you have planned for today, Hotsure-san?"
    MC "Me? Ah...{w} well, I'm really not sure yet. I've got a handful of ideas."
    GTS "I see. Well, if you'd like, you're more than welcome to join me at the festival."
    MC "Oh, really? That's really kind of you to offer, Yamazaki-san."
    pause .5
    if isEventCleared("GTS002"):
        MCT "I could hang out with Naomi. She's all about the flowers and anything and everything plant."
    else:
        MCT "I could take Yamazaki-san up on the offer. Probably won't be the most exciting day but it could be a good way to get to know the island a little more."
    MCT "Then again, it might be better to go meet up with Tomo. She could definitely use the time out and about."
    pause .5
    MCT "Or...{w} what the hell was Daichi on about?"
    menu:
        "Hang out with Naomi":
            $setFlag("MC005GTS")
            jump MC005_GTS
        "Hang out with Tomo":
            $setFlag("MC005TM")
            jump MC005_TM
        "Hang out with Daichi":
            if not getFlag("RMRoute_Unlocked"):
                $setFlag("RMRoute_Unlocked")
            $setFlag("MC005RM")
            jump MC005_RM

label MC005_GTS:
    MC "And, you know what? That sounds like a great time! Let's go!"
    show GTS unique
    GTS "Wonderful!"
    show GTS neutral
    GTS "Shall we, then?"
    MC "Sure! If you're all set."
    GTS "I am."
    "She put away her supplies, then joined me as we left together."
    $eventname = "Prairie Genteel"
    $save_name = "Prairie Genteel"
    scene Campus Center
    show GTS happy
    with fade
    GTS "My, it's a wonderful day today."
    MC "It is. Perfect temperature."
    MC "I suppose that there are some serious Greenery Day celebrations going on, then?"
    show GTS neutral
    GTS "From what I've heard, there should be. I look forward to seeing how it's done here, especially compared to back home."
    MC "Well, I'm curious as well. It'll be a bit of a new experience for me."
    GTS "Oh, it will? Then I will be honored to share in your first Greenery Day celebration away from home."
    scene black with fade
    pause .5
    play music BrightLights
    scene Town Street with fade
    "When Naomi and I got off the bus, I was surprised to see all of the decor and such for Greenery Day."
    "But I was more surprised to see the insanely large crowds going down the sidewalks in town."
    MC "Oh, wow. That's some crowd."
    show GTS unique with dissolve
    GTS "It's wonderful, isn't it?"
    GTS "So many people, all showing their love and appreciation of the Earth's greenery. It's quite special, isn't it?"
    MC "I'd agree, yes."
    "We started down the sidewalk, the two of us working our way through crowds of people, and making our way toward the field outside of town."
    "I was also aware of Naomi now being just a stone's throw above my height, and the slight bit of awkwardness to her gait as we journeyed down the town's streets."
    play music GTSAlt
    scene Flower Field with fade
    MC "Oh, whoa."
    "The fields of flowers stretched out in front of us in every direction. Every color and shade of the rainbow seemed to be present as we entered."
    show GTS surprised with dissolve
    "Naomi gasped, putting a hand to her collar."
    GTS "Heavens!... it's gorgeous, isn't it, Hotsure-san?"
    MC "Amazingly so..."
    "Flowers were being planted in sections around the field, and small paths were made to walk around them."
    MC "What's that orange-ish one by that tree?"
    show GTS neutral
    GTS "Mm... I believe that's an Osmanthus, or an Orange Sweet Olive. They tend to be used in teas, although they do have medicinal purposes used in some cultures."
    MC "Oh? What sort?"
    show GTS embarrassed
    GTS "Ah... I will tell you later. Their use is for something... rather private."
    MC "Ah. Of course."
    show GTS neutral
    "Naomi walked ahead, admiring a small cluster of yellow flowers, before something caught her eye and she made a beeline across the field."
    show GTS surprised
    "By the time I caught up with her, she was kneeling down by a flower redder than blood."
    show GTS happy
    GTS "Remarkable! Hotsure-san, do you see this flower?"
    if getFlag("MC005_browseweb"):
        MC "Yeah... wait, is that a Chocolate Cosmos? Woah."
        GTS "My stars, it is! What luck! I never imagined I would get to see one in person."
        MC "Yeah, didn't they go, like, actually extinct?"
        GTS "Indeed they did! Luckily, a nursery in New Zealand managed to produce cultivars with fertile seeds."
        show GTS neutral
        GTS "Nevertheless, they're still exceedingly rare, and they fare poorly in cold climates. Whoever owns these must be truly dedicated to their craft."
        MC "Wow, that's really something."
        GTS "Quite!"
        show GTS happy
        GTS "I must say, it's all the more splendid to have made this discovery with a fellow horticultural enthusiast."
        MC "Oh, me? I wouldn't say that, I just happened to read about them recently."
        $setAffection("GTS", 1)
        GTS "Well, I commend your choice of literature all the same."
        show GTS happy at Transform(xzoom=-1)
        pause 0.1
        show GTS happy at altMove(0.5, 0.75)
        GTS "Well here, come smell them for yourself. They're delightful!"
    else:
        MC "Y-Yeah, I do. What is it?"
        GTS "It's a Chocolate Cosmos! These are incredibly rare flowers, Hotsure-san!"
        MC "Wow! It looks like it would be rare, look at that color."
        MC "Are they found in, like, only one place on Earth or something?"
        GTS "Even rarer than that! For about a hundred years, they were extinct."
        MC "What? Seriously?"
        show GTS unique
        GTS "Quite! They were extinct, then brought back! But even after that, they're an incredibly rare find!"
        show GTS surprised
        GTS "What's more, they fare very poorly in cold weather. Whoever owns these plants must work very hard to keep them alive."
        show GTS unique at Transform(xzoom=-1)
        pause 0.1
        show GTS unique at altMove(0.5, 0.75)
        GTS "Well, why don't you see for yourself? Come, smell them!"
    "I smiled and knelt beside her, bringing my face to the dainty, red flower."
    MC "Mm... oh wow, that's... that's just like chocolate!"
    UNKNOWN "Isn't it?"
    show GTS surprised
    "Naomi and I both looked up at a tall, fairly built looking man, standing over us with his hands behind his back."
    GTS "Oh! E-Excuse us!"
    UNKNOWN "Hah, no trouble at all. Flowers are for enjoying, are they not?"
    GTS "Oh, most certainly. Are you the one who planted this Chocolate Cosmos?"
    $setFlag("Meet_Florist")
    Ren "I am, indeed. My name is Ren Hirano. It's always nice to meet a fellow botanist. May I ask your name, miss?"
    show GTS embarrassed
    GTS "Ah... I am Naomi Yamazaki, sir. A pleasure to meet you. But... I don't believe I'd call myself a botanist. I'm simply a hobbyist."
    if isEventCleared("GTS008"):
        menu:
            "You do a lot of work to just call it a hobby.":
                show GTS embarrassed at Transform(xzoom=-1)
                GTS "I don't spend that much time in the dirt, do I?"
                Ren "Well, what's wrong with that if you do? It's a very rewarding pursuit, dirt and all."
                Ren "Anyway, I have a store close by, if you two would care to have a look."
            "Well, you certainly have the know-how. I'd call you a botanist.":
                show GTS embarrassed at Transform(xzoom=-1)
                GTS "You would, Hotsure-san?"
                MC "I would. I've learned more about flowers from you than likely all other sources combined."
                GTS "I... well, I'm still a long way from being a professional, and the title ought not to be cheapened for my sake. But... thank you."
                $setAffection("GTS", 1)
                Ren "Well, I have a store close by, if you two would care to have a look."
    else:
        MC "You sure? Half the time when I see you outside class you're watering something or other."
        GTS "Well, it is a pastime I love dearly, but a professional title ought not to be cheapened for my sake."
        Ren "Well, it sounds like you would have the disposition for it, that's for sure."
        show GTS embarrassed
        GTS "High praise indeed coming from you, sir."
        Ren "You know what, I have a store close by if you two would like to have a look."
    show GTS surprised at Transform(xzoom=1)
    GTS "You do?... Erm, would that be alright, Hotsure-san?"
    MC "Sure! I'll be right behind you."

    scene Town with fade
    play music BrightLights
    "Ren led us out of the field and back into town."
    "We headed down a side street and to a storefront, which he unlocked with a key."
    show GTS surprised with dissolve
    GTS "Oh, my..."
    "Naomi walked back and forth among many of the different flowers, stopping here and there to admire one or examine."
    show GTS happy
    GTS "This is incredible, Hirano-san! Such an amazing collection. I imagine it's difficult to keep up with so many different species."
    Ren "It takes work, it's true. But, with some planning, a little ingenuity, and some drive, it all comes to you."
    Ren "Gather your supplies, make a plan, and act on it, and you have some healthy flowers."
    show GTS pondering
    GTS "It must be costly, though. Some of these species are as rare as the Chocolate Cosmos."
    Ren "Well, you certainly have an eye, don't you? Well, yes, it can be a costly affair, it's something I don't mind spending the money on."
    Ren "When you love something, collecting it is never a chore, no matter the cost or time sink."
    show GTS unique
    GTS "I understand completely."
    GTS "Do you have the more delicate and valuable flowers organized in some fashion?"
    Ren "Not as in-depth as I'd like to. I'd prefer an actual greenhouse, but due to space limitations, I've had to settle for more of an in-house controlled space for them. But, one can dream."
    "I smiled and embraced my third wheel status as the two geeked out over floral arrangements and such."
    show GTS neutral at Transform(xzoom=-1)
    GTS "Will you be alright alone for a moment, Hotsure-san? Hirano-san is going to show me some more arrangements in the back of the store."
    MC "Oh, totally! Go have fun!"
    show GTS happy
    GTS "Thank you, Hotsure-san."
    hide GTS with dissolve
    "She disappeared into the back with Ren as I perused the aisles, checking out this and that."
    "One flower was rather elongated and pink with a form that almost resembled a trombone."
    "Along with it, there were others on another wall that had a rather sweet appearance to them, looking rather similar to little, white bells with their shape and the way they hung from their stem."
    "Then, there was a rather alluring looking flower that was planted in the corner. It was a baby blue color with thick petals that formed a star shape."
    Ren "You look to have found a favorite flower, hm?"
    MC "They are pretty amazing looking, I have to say."
    Ren "Well, here, take one with you, then. On me."
    MC "I... that's very nice of you, Hirano-san, but I couldn't."
    Ren "Oh, please do. Strange as it may sound, after working with plants for a long time... you can sense when they want to be with someone."
    MC "Well... thank you very much."
    "I picked up the small pot that held the flower."
    MC "I'll take good care of it. Anything special I should know?"
    Ren "Just make sure to water it and give it some shade. Though, I'm sure your friend could have told you that."
    Ren "Anything else, she's the one to talk to."
    MC "Sounds good, thank you again."
    Ren "My pleasure."
    "Naomi came out of the back, the widest of grins on her face."
    show GTS happy with dissolve
    GTS "Pardon the delay, Hotsure-san. There was just... so much to see."
    MC "Hey, no apologies needed. You were barely gone a minute or two."
    show GTS neutral
    GTS "Thank you, Hotsure-san. It is quite easy to get lost in here."
    "Naomi had some packs of seeds in her hand that she brought to the register for purchase. She took another glance back at me, and her face brightened."
    GTS "Oh! Are you buying that flower, Hotsure-san?"
    Ren "Actually, that's a gift from me."
    MC "Think you could help me plant it, Yamazaki-san?"
    show GTS happy
    GTS "Ah, of course!"
    MC "Thank you. I'd trust it to no one else."
    "Naomi handed Ren some yen as he rang up the seeds."
    Ren "Thank you both. It was wonderful meeting you. Have a great day, and enjoy Greenery Day."
    GTS "Thank you very much, sir! Likewise!"
    scene black with fade
    pause 1

    scene School Front with fade
    "The entire ride back on the bus, Naomi showed me her seeds, and told me her plans of where to plant them and how to make them look best in the school's gardens. Complementary colors and all that."
    scene School Planter
    show GTS neutral
    with fade
    play music Nostalgia
    GTS "Would you like to plant your flower together, Hotsure-san?"
    MC "Yeah, let's do it!"
    show GTS unique
    GTS "Wonderful!"
    "Naomi walked around the garden a bit with me."
    GTS "Mm... here? No... no, here. Perfect."
    "She glanced up at the sky."
    show GTS neutral
    GTS "This spot should get partial sun during the morning. Perfect for this type of flower."
    "The two of us soon had a small hole dug, then had transferred the flower from its pot and into the soil."
    "I helped her pat it down, then got some water while Naomi handled smoothing the earth out."
    GTS "Perfect."
    MC "It looks just right there. Good call on the spot!"
    GTS "Well, I'm very grateful that you trusted me to plant it with you."
    MC "Hey, it made my Greenery Day all the more special to plant it with you, so thanks for helping me."
    show GTS unique
    GTS "It was my pleasure."
    "I smiled at her, and looked down at the flower we'd planted together."
    "We talked for a bit longer, then spent the rest of our day together walking around the garden and finding places for Naomi's seeds to be planted."
    jump MC005_finale

label MC005_TM:
    MC "Oh... shoot, I'm sorry, Yamazaki-san. That sounds like a wonderful time, but I should really spend some time with my sister today."
    GTS "Oh, no harm done at all, Hotsure-san. I think that's a wonderful idea."
    GTS "I do hope you have a splendid time with your sister."
    MC "Thank you. I'm sure I will."
    MC "I hope you have a pleasant Greenery Day, Yamazaki-san."
    show GTS happy
    GTS "A pleasant day to you, as well."
    hide GTS with dissolve
    "I turned from the garden as Naomi headed out the door toward the bus stop."
    $eventname = "It's On!"
    $save_name = "It's On!"
    scene Campus Center with fade
    play music Peaceful
    "Instead, I headed back across campus toward the dorms."
    pause .5
    MCT "Really. Where else would she be?"
    MCT "I highly doubt Tomo will be out doing anything extreme on Greenery Day of all days."
    MCT "Unless her roommate dragged her out or something."
    MCT "I somehow doubt that, though."
    MCT "Plus, Tomo and extreme... don't really go together."

    scene Dorm Exterior with fade
    MCT "What exactly can we do, though? It's not like Tomo will be down to go into town and check out the festivities or anything."
    MCT "We could always play games or something together at her dorm, I guess."
    MCT "Seems a little lame for a holiday, though."
    "I stopped outside the dorms."
    MCT "What... do I really want to do with her?"
    "That question stuck with me for a second."
    "Back home, the two of us would sometimes just sit at home and play games together, and there definitely wasn't anything wrong with having some R&R."
    "But, for some reason, the idea of Tomo just sitting alone in her dorm... it bothered me."
    scene Dorm Hallway with fade
    "I walked into the hallways of the women's dorms and walked on to Tomo's door."
    play sound Knock
    "I knocked at the door twice and stepped back."
    pause .5
    "..."
    pause .5
    MCT "Goddammit..."
    "I pulled my phone out and clicked Tomo's number."
    "..."
    "..."
    TomokoCell "Hello?"
    MCCell "Hey. Answer your door."
    TomokoCell "Who's at my door?"
    MCCell "I... it's me, Tomo."
    TomokoCell "Oh."
    pause .5
    $setTomoOutfit(OutfitEnum.CASUAL)
    show Tomoko neutral with dissolve
    Tomoko "Hey."
    MC "Hey. What are you up to?"
    Tomoko "I was watching a movie."
    MC "Ah. Well, care if I come in for a bit?"
    Tomoko "... Sure."
    scene Dorm Tomoko with fade
    #$setTime(TimeEnum.NIGHT)
    MC "You know, normally I'd call you out for sitting in the dark, but it's a perfect movie atmosphere."
    show Tomoko neutral with dissolve
    MC "What are you watching?"
    Tomoko "Sky Wars Episode 12."
    MC "Oh, that's a good one..."
    Tomoko "Mhm."
    "Tomo walked back across her room and sat on her bed, pulling her laptop up onto her blankets."
    Tomoko "So... why are you here?"
    MC "Well, do you feel like doing anything? It's Greenery Day after all."
    show Tomoko annoyed
    Tomoko "Ugh... that's why you're here?"
    MC "Eh... yeah? I just thought it would be fun."
    Tomoko "Mmngh... fine."
    show Tomoko neutral
    MC "Cool."
    MCT "Don't sound so excited."
    "Tomoko slid her laptop off and flipped her blankets off and half onto the floor."
    Tomoko "What do you want to do?"
    if isEventCleared("FMG011") or getFlag("MC005_readbrochure"):
        MC "Um..."
        MC "Oh, what about that rec room place?"
        Tomoko "Rec room? What do you... oh, you mean where they have those arcade games and stuff?"
        MC "Yeah, that place. How's that sound?"
        Tomoko "Uh... fine? I guess..."
    else:
        MC "Uh..."
        MC "I... really didn't get that far."
        MC "Whatever you want, I guess."
        Tomoko "... We could go to that place where they have the arcade games."
        MC "In... town?"
        Tomoko "Agh... no."
        Tomoko "At the school. Like... the recreation room thing."
        MC "The school has that?"
        Tomoko "Eh? ... How do I know about this and you don't?"
        MC "Your roommate tells you everything?"
        Tomoko "..."
        Tomoko "You aren't wrong."
    "Tomo slipped off of her bed and shuffled toward the door, taking her shoes from the floor and shoving her feet into them, kicking her heels in."
    Tomoko "Let's go."
    MC "Eh? Just like that?"
    Tomoko "The sooner we go, the sooner I can get back to my movie."
    MC "Ah... right."
    pause .5
    MCT "Ouch."

    scene black with fade
    #$setTime(TimeEnum.DAY)
    pause .5
    scene Dorm Exterior
    show Tomoko neutral
    with fade
    "The sun shone down on us as we headed out from the dorm together."
    Tomoko "Agh... it's too hot out."
    MC "It's not even summer out. It's not that bad yet."
    show Tomoko unique
    Tomoko "I have hair growth, you know."
    Tomoko "It's like insulation."
    MC "... What factor do I have again?"
    show Tomoko neutral
    Tomoko "... I know. But, I can still complain."
    scene Campus Center
    show Tomoko neutral
    with fade
    if isEventCleared("FMG011") or getFlag("MC005_readbrochure"):
        "We passed through the center of campus toward where I remembered the rec room being."
        "Past the main entrance to the academy, I spotted the small side entrance that led to the rec room."
        MC "Here we are."
    else:
        MC "So, where do we go?"
        Tomoko "This way."
        "Tomo led us into the center of campus and past the school buildings."
        "Past the main entrance to the academy, there was a much less conspicuous entrance, which by the looks of it, looked more like a side door into the halls than anything."
        Tomoko "This is it."
        MC "Just right here?"
        Tomoko "What did you expect?"
        MC "Ah..."
        MC "Maybe a bit more signage than just \"side entrance.\""
        Tomoko "Well, it is what it is."
    scene Recreation
    show Tomoko neutral
    with fade
    play music Tomoko
    "As we walked in, I glanced around the room."
    if isEventCleared("FMG011"):
        "It looked much the same as it had the last time I'd been here."
        MC "Well, here we are."
        show Tomoko sad
        Tomoko "..."
    else:
        MC "Huh. I'm shocked I haven't heard of this place till now."
        show Tomoko sad
        Tomoko "..."
    MC "So. What should we check out first?"
    Tomoko "..."
    MC "Tomo? What's up?"
    "Tomo looked around, as did I."
    "For the first time, I noticed just how many people were here."
    "And, I'd never met any of them."
    MCT "And, if I haven't met any of these people before..."
    "I glanced over at my \"social\" moth of a sister."
    MCT "... Right."
    "I walked a little deeper into the room, with Tomo nearly glued to my side."
    MC "Mmm. Nice of them to have some arcade games here."
    show Tomoko neutral
    Tomoko "... Yeah."
    "I took another quick look around."
    MCT "There has to be something here."
    "Across the room, somewhat out of the way of everything else was an unmanned air hockey table, with two paddles sitting on it, ready for hands to knock them around like mad."
    MC "Hey, Tomo. Wanna play some air hockey for a bit?"
    Tomoko "... No."
    MC "Oh, come on."
    MC "You're worried I'm gonna kick your ass, aren't you?"
    MC "Don't want your roommate to tell everyone that your brother is a better hockey player than you?"
    Tomoko "..."
    show Tomoko happy
    Tomoko "... Pick up a paddle, smartass."
    "She walked away to one side of the table and took the red paddle for herself, leaving me with the blue one."
    MC "You're on."
    show Tomoko neutral
    "I took the blue paddle and grabbed the puck from my side, slinging it onto the table, where it hovered."
    MC "Go!"
    "Tomo and I smashed the puck at the same time, but my paddle won out, and shot the puck into the left side, where it ricocheted off and back toward the right, bouncing in my direction."
    "I backpedaled my paddle, and knocked the puck toward the left to bounce it across the table."
    "Tomo was ready for me, and slapped the puck away from her goal, knocking it back toward me."
    "She focused her eyes on my hands as I gently pushed it toward my goal, then let it hover for a moment."
    pause .5
    "{i}CRACK!{/i}"
    "I smacked the puck, and rocketed it across the table toward Tomo. However, due to the force of my shot, the puck got airborne for just a second, and wobbled on one edge, causing it to smack the lip of Tomo's goal and bouncing it back."
    MC "Dammit!"
    Tomoko "Went too hard, bro."
    "Tomo smacked her paddle on top of the puck to steady it, and centered the puck."
    Tomoko "Hmm..."
    "Tomo brought her hand to the left, then floated her paddle over to her other hand, then back over."
    "She knocked the puck sideways, then bashed it off to the left, shooting it out toward my goal."
    "I hit it back to the left, where it shot off of the backboard beside Tomo's goal, and came shooting back toward me."
    "I moved to intercept, but at the last minute, my hand slipped, and I lost grip on my paddle, causing me to slide it too far, and letting the puck slide harmlessly into my goal."
    MC "Shit..."
    Tomoko "Point for me."
    "Tomo slid a plastic scoring piece over to her side of the table."
    MC "My serve, then."
    "I took the puck from the little... holder thing."
    MCT "Seriously, what is that thing called? The puck return? The slot? The puck retrieval thing?"
    "I set the puck down on the table and geared up, slapping the puck across the table before Tomo could react and sending it straight for a goal."
    show Tomoko surprised
    Tomoko "Wha?!"
    MC "Think faster, Tomo!"
    show Tomoko neutral
    Tomoko "Rgh..."
    Tomoko "You're going down!"
    scene black with fade
    pause .5

    scene Recreation with fade
    "A few goals later, I set my paddle down and rubbed my wrist a bit."
    MC "So, how are things?"
    show Tomoko neutral with dissolve
    Tomoko "Mn... fine? Why?"
    MC "Just... asking to ask."
    MC "How's your homeroom?"
    Tomoko "Eh... my teacher is super hyper."
    Tomoko "Like... she's into everything."
    MC "Huh."
    MC "That's a 180. My homeroom teacher is kind of dull."
    MC "I don't think I've even seen him smile."
    MC "Oh, by the way, I ran into Honoka."
    Tomoko "Honoka? Like... childhood best friend Honoka?"
    show Tomoko surprised
    MC "Mhm."
    Tomoko "She's here?"
    MC "Surprising, isn't it?"
    Tomoko "Eh... yeah."
    show Tomoko neutral
    Tomoko "She has a factor?"
    MC "Mhm."
    Tomoko "Hm."
    Tomoko "..."
    Tomoko "Wonder what it is."
    pause .5
    if getHighestAffection() == ("BE"):
        $setFlag("MC005TM_BE")
        Tomoko "... I bet it's boobs. Big knockers."
        MC "Huh?"
        MCT "How in the..."
        MC "Why would you guess that?"
        Tomoko "You've always liked big boobs."
        MC "..."
        MC "You're my sister. Don't say that."
        Tomoko "Am I right?"
        MC "... That's her personal information."
    elif getHighestAffection() == ("AE"):
        $setFlag("MC005TM_AE")
        Tomoko "Butt factor, probably."
        MC "Butt factor?"
        Tomoko "Mhm. I could picture her with a wide load in back."
        Tomoko "Not to mention your tastes."
        MC "My... what do you mean?"
        Tomoko "Oh, come on, bro. You're an ass man through and through."
        Tomoko "Walking past someone on the street and doing the half head turn to look back. It's as obvious as the hair on your head."
        MC "..."
    elif getHighestAffection() == ("WG"):
        $setFlag("MC005TM_WG")
        Tomoko "Maybe she's got the... what's it called... fat girl factor?"
        MC "That's kind of rude."
        Tomoko "Weight gain, big bones factor, whatever."
        MC "What would give you that idea?"
        Tomoko "Easy."
        Tomoko "You like fat chicks."
        MC "Eh?! I..."
        Tomoko "You're easy to read, bro. You turning your head toward a girl is a dead giveway."
        Tomoko "You don't need to see your eyes to see that."
        MC "... Look, let's not talk about that here, okay?"
        Tomoko "Whatever."
    elif getHighestAffection() == ("GTS"):
        $setFlag("MC005TM_GTS")
        Tomoko "Maybe she'll be like, as tall as a building or something."
        MC "Like, giant growth?"
        Tomoko "Mhm."
        Tomoko "Be perfect for you."
        MC "Perfect for... what? What makes you say that?"
        Tomoko "You like tall girls. Nothing wrong with it."
        Tomoko "Building high might be a little extreme, but hey, a lot of people like people with extreme stuff."
        MC "Where do you get me liking tall girls from?"
        Tomoko "It isn't hard to tell. I'm your sister, I know how you work."
        Tomoko "Any time a girl is taller than you, you fawn over her. It's pretty clear."
        MC "..."
    elif getHighestAffection() == ("FMG"):
        $setFlag("MC005TM_FMG")
        Tomoko "Muscle."
        MC "Muscle? Why would you-"
        Tomoko "You like girls with muscles, Kei. It's so obvious."
        Tomoko "Like, you'd get a gym membership just to gawk at a girl on a leg press."
        MC "Hey, there's... there's nothing wrong with a girl being in shape."
        Tomoko "In shape is one thing. Thighs so hard they could crush your head into paste is another."
        MC "Tomo, don't be so blunt. Geez."
        Tomoko "Well, am I wrong?"
        MC "..."
    elif getHighestAffection() == ("PRG"):
        $setFlag("MC005TM_PRG")
        Tomoko "Eh, she'll probably have an hourglass factor or something."
        MC "That's not a real factor."
        Tomoko "How do you know? It could be."
        Tomoko "Watch her walk in, boobs bouncing, butt jiggling, and thighs rubbing. You'd be drooling."
        Tomoko "You like girls with the whole package, Kei. The knockout thicc body type. The goddess body."
        MC "I..."
        MC "H-Hey, you're my sister. That's messed up to talk about."
        Tomoko "So?"
        Tomoko "Just watch. Someday, you'll be ready to have kids with a girl set up like that."
        MC "TOMO!"
        "Tomo simply shrugged."
    MC "Look... all I wanted to say is that Honoka is on the island too."
    Tomoko "Bet I could kick her butt in air hockey."
    MC "Well, ask her to play you sometime."
    "I smacked the puck across just as I said that and scored another goal."
    show Tomoko annoyed
    "Now, I only needed one more point to win the whole thing."
    "I looked over at Tomo as she grit her teeth."
    MCT "I haven't heard her say this much in ages..."
    MCT "Must be the \"love of the game\" or something."
    show Tomoko neutral
    "I looked down at the score once again."
    menu:
        "Play hard":
            $setFlag("MC005TM_PlayHard")
            "I stared down as the puck came flying at me."
            "I swiped it away and knocked it back at her, to which I received it back not half a second later."
            "I swiped it back once more, bringing my hand far to the right in my followthrough, and not a second later, the puck sailed past me and into my goal."
            MC "Hrgh..."
            MC "My serve."
            "I set the puck down and let it float there."
            MCT "Okay. One point. Send that thing home."
            "I smacked the puck as hard as I could dead center."
            pause .5
            "..."
            show Tomoko happy
            "The puck hit right beside Tomo's goal, came back, and flew right into my goal."
            Tomoko "Hah! Tryhard!"
            MC "Oh, come on!"
            "I had to try to not slam down my paddle in sheer gamer rage."
            Tomoko "Some of us have it, and some don't."
            Tomoko "Guess I got the skill out of the two of us."
            MC "At least I got the looks."
            Tomoko "You got dogshit."
            pause .5
            show Tomoko neutral
            MC "You wanna play anything else?"
            Tomoko "Mm... nah. I kind of just wanna go watch my movie."
            MC "Ah... alright. I'll probably go chill out, too."
            MC "But, good game."
            Tomoko "Yeah, you too."
            MC "Oh, I'll text you my dorm number, so you have it. Feel free to come over whenever."
            Tomoko "'Kay."
            hide Tomoko with dissolve
            "The two of us walked out of the rec room together. And as we went back to our dorms, I let my head take over my consciousness."
            MCT "For a bit there...{w} that's how I remember Tomo. Poking fun and laughing."
            $setAffection("TM", 1)
            jump MC005_finale

        "Let her win":
            $setFlag("MC005TM_LetTomoWin")
            "I looked at Tomoko, looking all determined across from me."
            MCT "Okay. I can't make this look obvious."
            "I saw the puck coming at me and batted it to the side, knocking it to her in a slow, more controlled manner."
            "She swatted it back, and I swiped at it, knocking it sideways."
            "It rattled on the table, and I sent it back to her, only to receive the puck back seconds later."
            "I swung at it once more, and purposely missed, letting it fly through and into my goal."
            MC "Shit."
            Tomoko "One more."
            "I put the puck up and let it sit for a minute, looking across at Tomo, ready for my onslaught."
            "I aimed my shot toward the wall beside Tomo's goal instead of right at her and smacked it, sending the puck flying."
            "It bounced against the wall, and flew back at me at high speed."
            "I could have stopped it, but I let the puck fly in."
            MC "Ach!"
            show Tomoko happy
            Tomoko "Yes! Eat it, tryhard!"
            "Tomo cried out, despite the crowds of people around us."
            MC "Ach, dammit."
            MC "Good game, Tomo."
            Tomoko "Yeah... you too."
            show Tomoko neutral
            MC "Wanna play another? Or hit up an arcade game or something?"
            Tomoko "Mm... I kind of just want to go finish my movie."
            MC "Alright, sounds good then. I'll see you soon, okay?"
            MC "I'll text you my dorm number too. Come over whenever."
            Tomoko "Kay."
            hide Tomoko with dissolve
            "We left the room together, and as I walked back to my dorm, I thought to that moment when I'd let that last shot fly into my goal."
            MCT "That victory cry... that was old Tomo. She used to be like that all the time."
            $setAffection("TM", 1)
            jump MC005_finale

label MC005_RM:
    MC "I... I'm really sorry, Yamazaki-san, but I should really touch base with my roommate today."
    GTS "Of course, Hotsure-san. Your roommate is Utagashi-san, correct?"
    MC "Mhm. He asked me earlier to join him on something he calls a \"Golden Week Adventure.\" So... yeah."
    show GTS pondering
    GTS "Ah... I see."
    GTS "I can't help but wonder what that might mean."
    MC "You and me both. But, thank you so much for the offer. I hope you have a pleasant Greenery Day."
    show GTS happy
    GTS "The pleasure is mine, Hotsure-san. A pleasant day to you, as well."
    hide GTS with dissolve
    "I turned from the garden and headed back outside."
    $eventname = "Following the Thread"
    $save_name = "Following the Thread"
    scene Dorm Exterior with fade
    MCT "..."
    MCT "This feels slightly insane."
    "I had walked all the way across the campus, and at no point had I thought of a good reason as to why I was doing this, outside of pure curiosity."
    show Tako neutral at Transform(xzoom=-1), Position(xcenter=0.25, yalign=1.0)
    show Jineko neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    "The whole area was awash with students, and I spotted a few that I hadn't met prior milling about and chatting with each other, as well as the occasional familiar face dotted around."
    hide Tako
    hide Jineko
    show RM neutral
    with dissolve
    play music RM
    "Up ahead, Daichi stood near the men's dorms, slightly in the shadows, observing the crowd of people like a hawk."
    "I walked over to him, unsure whether I should approach him from the front, or sidle alongside him like a cringey 80's movie villain."
    RM "You in then?"
    MC "In."
    show RM happy
    $setAffection("RM", 1)
    RM "Great. Let's go."
    MC "Go? To... where, exactly?"
    show RM smug
    RM "Town, obviously."
    MC "Ah... the \"adventure\" takes place in town?"
    RM "It does."
    MC "This isn't some investigation thing, is it? Like, I'm not going to end up on a watch list by the end of today, right?"
    show RM neutral
    RM "Do you think that everything I do is strictly for investigation?"
    MC "I..."
    MCT "Well, he has been AWOL for the last handful of days."
    RM "Anyways. We're heading to town. Let's go."
    MC "I..."
    pause .5
    MC "Alright."
    MCT "Maybe he'll calm down on the bus or something."
    scene black with fade
    pause .5

    scene Campus Center
    show RM neutral
    with fade
    RM "So, how's classes for you?"
    MC "Uh... fine?"
    RM "Cool."
    RM "You still hanging out with that one girl?"
    if getHighestAffection() == ("BE"):
        MC "If you're talking about Honoka, then yeah."
        RM "Mhm. Cool."
    elif getHighestAffection() == ("AE"):
        MC "You mean Matsumoto-san? Yeah, we're spending time together."
        RM "Well be careful of her! She gives me the creeps."
        MC "Ahhh, c'mon."
        RM "I'm serious! She gives me the vibes of a human security camera."
        MC "You know, she really isn't that bad once you get talking to her."
        MCT "When you can understand her..."
    elif getHighestAffection() == ("GTS"):
        MC "Yamazaki-san? Yep."
        MC "I'll have you know that she asked me if I'd like to hang out with her, and I chose to be here with you instead."
        MC "So yeah. Feel special."
        RM "That I do."
        $setAffection("RM", 1)
    elif getHighestAffection() == ("WG"):
        MC "Alice? Yeah."
        RM "And how is she?"
        MC "Uh... fine?"
        RM "Nice."
        MCT "God. Tomo is a better conversationalist..."
    elif getHighestAffection() == ("PRG"):
        MC "You mean Kodama-san?"
        RM "Yes."
        MC "Then yes, I am."
        RM "And how is she?"
        MC "Fine."
        RM "Good."
        MC "..."
        MCT "Small talk much?"
    elif getHighestAffection() == ("FMG"):
        MC "Mizutani-san? Yeah, we're still spending time together."
        RM "Cool."
        "Daichi walked on as I tagged along behind him."
    "I kept the conversation light as we reached the bus stop. Clearly all attempts at small talk would be half-assed."
    scene School Front with fade
    "As we got to the bus stop, I sighed and glanced at Daichi."
    "The feeling that I was somehow being roped into some grand plot still was lingering about. However, getting to check out the town would likely be a good time, so there was that."
    show Tako neutral at Transform(xzoom=-1), Position(xcenter=0.25, yalign=1.0)
    show Jineko neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    "As we waited, a few of the other students from around the campus showed up at the stop as well."
    show Tako unique at Transform(xzoom=-1)
    "Beside us, one of the girls whispered something to another, and the second girl burst into laughter."
    MCT "At least someone is having a grand ol' time."
    scene black with fade
    pause .5
    scene Town with fade
    play music DayByDay
    "The bus spat us out on one end of the main drag. I looked down it, admiring the lush greenery and flowers that were out for the holiday."
    show RM neutral with dissolve
    MC "So, what did you have in mind? Now that we're here."
    RM "Let's just walk a bit."
    "Daichi started down the street with me in tow."
    RM "You know something interesting I learned the other day?"
    MC "I can only imagine."
    show RM happy
    RM "The academy was founded by a member of the Diet."
    if getFlag("MC005_readbrochure"):
        MC "You just learned that now?"
        show RM doubt
        RM "... H-How did you know that?"
        MC "I read it in the brochure that we were all given."
        MC "Honestly, I'm surprised you didn't see that."
        pause .5
        MC "... You did read it, didn't you?"
        show RM concerned
        RM "You mean the one from the gift bag that the hourglass teacher gave us?"
        MC "Yes?"
        show RM concerned-2
        RM "I..."
        show RM angry
        RM "Look, I don't have time for their propaganda! I want actual {i}FACTS{/i}!"
        pause .5
        show RM neutral
        pause .5
    else:
        MC "Huh... didn't know that."
        RM "Mhm."
        RM "It's interesting, for sure. But... I'm after something more than generic facts."
        show RM neutral
    MC "Okay, look."
    MC "I get that you're suspicious of the school, okay? I get that."
    MC "But, do you have any solid proof? Like, anything past doubts?"
    RM "Nothing hard. But, think of the coincidences."
    RM "For instance, how would they know about my..."
    MC "..."
    "Daichi simply shook his head and walked on."
    MC "Your...?"
    RM "Agh... it doesn't matter."

    "As we walked along through town, we saw all manner of townsfolk and students alike out and about, admiring the foliage and such, with a large group of them heading outside of town."
    MCT "Must be that festival Naomi mentioned."
    MCT "I wonder if she's there already."
    "The town was practically painted in green, and every other color of the rainbow on top of it, giving the once ordinary looking buildings a flash of color."
    show RM concerned-2
    RM "Have you and your sister spent any time together recently?"
    MC "Eh? Why do you ask?"
    RM "Simple curiosity."
    if isEventCleared("MC003"):
        show RM neutral
        RM "And, I haven't heard you mention Tomoko for a bit."
        MCT "Did... I mention that her name is Tomo?"
        MCT "Maybe his sister told him?"
    else:
        show RM neutral
        RM "And, I haven't heard you bring up..."
        pause .5
        RM "Tomoko, was it?"
        MC "Uh... yeah."
        RM "I haven't heard you bring her up in awhile."
        MCT "..."
        MCT "Did I ever tell him my sister's name?"
    MC "Yeah, well. I did think about hanging out with her today, but I'm not sure how she would have enjoyed all of this."
    MC "Holidays are... kind of crowded for her tastes."
    RM "I can relate."
    pause .5
    MCT "Huh. Maybe Daichi {i}did{/i} want to just spend time with me. He actually seems almost... nice."
    MCT "Well, nice aside from his usual sprinkling of lunacy."
    scene black with fade
    pause .5

    scene Town
    show RM neutral
    with fade
    play music BrightLights
    "About half an hour later, Daichi and I were sitting on a bench, each of us with some food from a nearby food truck out for the day."
    "I glanced at Daichi as I dug into my gyoza and sighed as the warm filling hit my tongue."
    "Surprising on all fronts... I was actually having a decent time with Daichi. The conversation wasn't overly heavy, but the time spent just relaxing in town was pretty chill."
    "Not to mention that people watching carried a sort of lazy fun with it."
    MC "You wanna head back soon, Daichi? Or did you wanna check something else out?"
    pause .75
    show RM sad
    MC "Daichi?"
    "My roommate hadn't even moved since we'd sat down, his food outright leaking from its container and hitting the ground."
    "I glanced at him, then followed his gaze."
    hide RM with dissolve
    show Tako happy at Transform(xzoom=-1), Position(xcenter=0.25, yalign=1.0)
    show Jineko happy at Position(xcenter=0.75, yalign=1.0)
    show Sakura happy
    with dissolve
    "A crowd of students stood nearby, also enjoying some of the food from the truck."
    "Among them, one of the girls held her food in one hand, and a bag with the logo of a nearby store on it."
    show Jineko happy at altMove(0.5, 0.5) with None
    hide Sakura
    hide Tako
    with dissolve
    MCT "That's... I think that's the hardware store's logo."
    MCT "Hm. Strange."
    MCT "This girl with a blazer tied around her waist..."
    MCT "Where the hell do I..."
    MCT "Oh! The bus stop!"
    MCT "..."
    MCT "... And outside the dorms."
    MCT "Huh. She sure gets around."
    "Two of the girls with her waved to her and headed off in different directions, while this girl stood for a bit, finishing off her food."
    hide Jineko
    show RM distrustful
    with dissolve
    "My eyes went to Daichi, and I watched as his gaze stayed laser focused on this one girl, hardly even shifting to either of the other two."
    MCT "..."
    MCT "Don't tell me..."
    MC "Daichi."
    show RM concerned-2
    RM "..."
    MC "Look, do you like this girl? Or, is this part of your master scheme?"
    RM "I... n-not at all."
    "I looked over and watched as the girl threw her takeout container in a trash bin and headed off down the sidewalk."
    RM "L-Look, I'll explain later, okay?"
    "Daichi got up and tossed his entirely uneaten meal in the bin and walked down the sidewalk in the same direction, weaving in and out of the crowd."
    MCT "Dude..."
    "I got up and walked toward him, not even bothering to maintain his \"cover.\""
    MC "Okay, fill me in, or I'm out."
    RM "I..."
    "He halted, eyes wide and staring at me."
    "Five or six other people around us were staring at the two of us... and that girl was gone."
    show RM angry
    RM "Urgh!"
    RM "Stay here, okay? I'll explain everything later!"
    hide RM with easeoutright
    "Daichi wormed his way between shoulders and faded into the crowd."
    MC "Ugh..."
    "I walked out of the crowd to get a bit of open air, inhaling deeply to quell the angry fizz in my stomach, which I wasn't quite sure if it was from fried food or Daichi's BS."
    play music Busy
    Student "Howdy, Stranger."
    show dummy with vpunch
    MC "Ach?!"
    "I whipped around quickly to the voice behind me."
    show Jineko neutral with dissolve
    "Seeing her up close only made me now realize that Daichi's \"target\" was a few centimeters taller than I. I looked up at her, trying not to look like I'd just been shocked back into reality."
    Student "So, question."
    Student "What's with the lanky dude that's been hanging around with you?"
    MC "Uh... I'm sorry for him. He's... something."
    Student "Is he... like, does he want to ask me on a date or something?"
    MC "I... I guess I couldn't tell you, to be honest. You likely know about as much as I do right now. Though, I don't think he's looking for a date."
    MC "He's a bit of an odd duck."
    show Jineko surprised
    Student "Oh, one of those, huh?"
    Student "I saw him around yesterday too. I was expecting him to walk up and talk to me or something, but he just bailed."
    Student "You're sure he's not looking for a night out?"
    MC "About 95 percent sure, yes."
    show Jineko happy
    Student "Good."
    Student "He's not quite my type."
    show Jineko neutral
    MC "Understood."
    MC "So, you here for the festivities as well?"
    Student "Well, I'd planned on visiting the park with some friends."
    Student "I'm only here because I know the owner of the hardware store, and I needed some tools from him."
    Student "Normally, I would've had to wait till next week, but he let me in early so I could get what I needed."
    MC "Oh, cool."
    Student "Mhm. Then, of course, I saw the food truck, and my friends wanted something, so naturally, I joined in."
    MC "As one does. I would've done the same."
    Student "Natch!"
    Student "But anyway! It was good meeting you, Stranger! Enjoy your Greenery Day!"
    MC "Same to you!"
    hide Jineko with dissolve
    MCT "Well, I met someone new, and no watch list. Things are looking up."
    "Not seeing anything better to do, I started walking back down the block toward the bus stop. I'd had enough drama for one day."
    play music RM
    pause .5
    "... Of course, as I started back, I spotted Daichi turning the corner of a building in front of me."
    show RM doubt with easeinright
    "He put one hand on it, and bent his neck down, his chest heaving up and down like broken bellows."
    "I sighed for probably the nine hundredth time and walked over to him."
    pause 1
    MC "What the fuck, man?"
    if isEventCleared("MC003"):
        RM "Agh... mmn... gagh... I... I can explain."
        MC "I'm listening."
        RM "Hah... okay, so... gah..."
        show RM concerned-2
        RM "I've... I've been trying to learn more about students with factors, specifically siblings... like I told you a few weeks ago."
        RM "I'm trying to find out if there's a pattern to it, and how this whole thing is going to affect my sister."
        MC "Alright... I can understand that."
    else:
        RM "Agh... mmn... gagh... I... I can explain."
        MC "I'm listening."
        RM "Hah... okay, so... gah..."
        show RM concerned-2
        RM "I... I've been looking into siblings with factors, and trying to learn more about what's behind them."
        RM "So, my sister is here too, and she has a factor, yet I don't."
        RM "I... I'm trying to find if there's any pattern with it, and just how much this thing is going to affect her."
        if isEventCleared("RM002"):
            MC "So, you're worried about Yuki. I can understand that."
            MCT "This place is... a little suspicious to be fair. Like, how exactly did they know we had factors before we did?"
            MCT "He does have some points."
        else:
            MC "So, you're worried about your sister. I can understand that."
            MCT "This place is... a little suspicious to be fair. Like, how exactly did they know we had factors before we did?"
            MCT "He does have some points."
    RM "I've... I've managed to find a few examples. You and your sister with the same one, and my sister and I, with me being factorless."
    RM "I also found some cases of former students with the same last name, yet having two entirely different factors."
    show RM concerned
    RM "Doing all of that, I found some records for more siblings... but the data was incomplete. Like, there was an error or it wasn't updated, I don't know."
    MCT "He better have not broke into a facility for this..."
    show RM neutral
    RM "I'm trying to track down a pair of twins to learn more about them. I've found the first one... but I can't find the second for the life of me."
    show RM concerned-2
    RM "Some... \"Hikari Watanabe\". I've found nothing."
    RM "I've checked literally every possible lead. Checking different classrooms and asking various students, but no one has heard of her."
    show RM neutral
    RM "Most of them just told me to back off... which must mean there's something more."
    MCT "Does it though?"
    RM "I've been digging up all I can lately, and have still come up dry. So, I decided to follow the easiest lead."
    RM "Follow her sister."
    RM "Unfortunately... all she's done is hang out with that one girl with the beanie and an ass the size of Matsumoto-san's and that other girl with the braid."
    RM "And... I still don't have a clue on her factor."
    MC "So... lemme throw something out here."
    MC "Just ask her sister about her. Simple."
    show RM angry
    RM "ARE YOU INSANE?!"
    RM "There HAS to be a reason why no one knows about her! You think her sister would tell me?! Some random guy?!"
    MC "She seemed really nice when I spoke to her. Maybe just try?"
    show RM distrustful
    RM "You {i}TALKED{/i} to her?"
    "Daichi near hissed the question and gave me the same look he might give a chimp with a machine gun."
    MC "Well, yeah. She overheard us, and I'm assuming, came up to me to ask what the fuss was all about."
    show RM doubt
    RM "What did she say?!"
    MC "Well, she assumed that you were looking for a date with her."
    RM "I-I... urgh..."
    RM "..."
    pause .5
    RM "Fine. Maybe this all is some big misunderstanding."
    MC "Figure that one out by yourself, did you?"
    RM "..."
    show RM sad
    RM "Let's go back to the academy."
    MC "Good call."
    "I let Daichi lead the way back to the bus stop, and as he sat down, I sat beside him and glanced over."
    MC "She did say you weren't her type, by the way, so don't get your hopes up."
    show RM angry
    RM "WHAT?!"
    "I snickered as the bus pulled up and we got on, Daichi shooting me death glares for a good portion of the ride thereafter."
    jump MC005_finale

label MC005_finale:
    scene black with fade
    $setTime(TimeEnum.EVE)
    pause 0.5
    play music TwilightBright
    $eventname = "Reflection"
    $save_name = "Reflection"
    scene Dorm Interior with fade
    pause .5
    "{i}CREEEEAK{/i}"
    pause .5
    "{i}CREEEEEEEEEAK{/i}"
    "I brought all four legs of my chair back down to the floor."
    pause .5
    "Again."
    MCT "Hah... so much for being studious on break."
    "I looked at my laptop screen once again, where I had my assignment pulled up. Beside it were my notes for my test, flipped to the first page."
    MCT "Okay... nothing to it but to do it."
    "I sat up and scrolled to the next line of text."
    "It was the final day of Golden Week. Children's Day."
    "Outside my window, I could make out seas of Koinobori hung out for the occasion, blowing in the sunny early afternoon breeze."
    "The colors all swam amongst each other, making the entire outside world shimmer like the ocean itself."
    MCT "Ech... I shouldn't."
    MCT "I've got an assignment and a test to take care of."
    "I stretched back in my chair and took a sip from the can of soda I'd treated myself to for the day."
    "I glanced out the window once more, and a smile crept to my face."
    MCT "Not like I've been sitting here doing nothing, anyway."
    MCT "I had the esteemed pleasure of seeing Tashi-sensei and Tsubasa-sensei out in the wild. Something that felt like seeing a fish out of water, no doubt."
    if getFlag("MC005RM"):
        MCT "Though... Daichi's whole thing is still... gray to me."
        MCT "The sister thing and the idea of him on a date?"
        MCT "Egh."
    elif getFlag("MC005GTS"):
        MCT "And, I did get to spend all that time with Naomi, and do some green thumb work."
        MCT "Points for me."
        MCT "And, getting to see Tomo was nice, too."
        MCT "Kind of weird to think that I actually missed my sis."
    elif getFlag("MC005TM"):
        MCT "Speaking of that, Tomo."
        MCT "Don't remember the last time I've seen her that much. Two trips to her dorm, and some time in the rec room with her just catching up."
        MCT "Even with her... remarks on my tastes in women, still... it was nice."
    "I took one more sip of soda, glanced down at my laptop, and somehow found the inner will to start typing."
    MCT "Let's hope Tashi-sensei's in a good mood coming up."
    MCT "He mentioned that thing about a surprise next week, and..."
    MCT "Huh... should I be nervous for that, or excited?"
    pause .5
    MCT "Curious. Yep, going with curious."
    "I gave myself a mental high five as I reached the bottom of the page and kept moving on in my flow."
    jump daymenu

label MC006:
    scene Auditorium with fade
    play music Schoolday
    $setBEOutfit(OutfitEnum.ATHLETIC)
    $setAEOutfit(OutfitEnum.ATHLETIC)
    $setWGOutfit(OutfitEnum.ATHLETIC)
    $setGTSOutfit(OutfitEnum.ATHLETIC)
    $setPRGOutfit(OutfitEnum.ATHLETIC)
    $setFMGOutfit(OutfitEnum.ATHLETIC)
    "We were told our class had some kind of special assembly today. There weren't too many details, but we all had to show up to the auditorium in our gym clothes."
    if not checkSkill("Athletics", ">", 0):
        "It'd been a while since I'd done anything athletic. I was probably going to be sore tomorrow, whatever this was."
    elif checkSkill("Athletics", ">=", 3):
        MCT "Seems like it could be fun— I'm ready."
    show BE neutral at Position(xcenter=0.2, yalign=1.0) with dissolve
    BE "Does anyone know why we're here?"
    show FMG happy at Position(xcenter=0.4, yalign=1.0) with dissolve
    FMG "Who cares? If it gets us out of class it can't be that bad."
    show WG doubt at Position(xcenter=0.6, yalign=1.0) with dissolve
    WG "This better not be one of those lame corporate team builder activities."
    show AE neutral at Position(xcenter=0.8, yalign=1.0) with dissolve
    AE "It is a special assembly. The teachers did not disclose the nature of the activity on purpose."
    hide WG
    show GTS neutral at Position(xcenter=0.6, yalign=1.0)
    with dissolve
    GTS "I can only assume it is some kind of athletic activity if we were told to wear our gym clothes."
    hide FMG
    show PRG nervous at Position(xcenter=0.4, yalign=1.0)
    with dissolve
    PRG "I-I hope not... I-I'm not very good at sports."
    MC "Looks like everyone's here, where's Tashi-sensei?"
    AE "Not quite. I don't see Utagashi-san."
    MCT "Since when did he count?"
    AE "Have you seen him, Hotsure-san?"
    MC "You'd be surprised how little I see him, despite living with him."
    AE "This won't do. He does not get to pick and choose his attendance to these events."
    show BE happy
    BE "What does he even do all day outside of class?"
    MC "I couldn't tell you."
    hide GTS
    show WG stern at Position(xcenter=0.6, yalign=1.0)
    WG "Who cares? The less anyone has to listen to his craven conspiracy theories the better."
    hide AE
    show FMG neutral at Position(xcenter=0.8, yalign=1.0)
    FMG "Yeah, he is a little... eccentric."
    hide WG
    show GTS angry at Position(xcenter=0.6, yalign=1.0)
    GTS "It is rude to speak ill of someone behind their back."
    show PRG worried
    PRG "T-Tashi-sensei is here."
    hide BE
    hide GTS
    hide PRG
    hide FMG
    with dissolve
    pause 0.2
    show HR neutral with dissolve
    HR "You're probably wondering why you're all here today instead of regular class. Me and some of the other teachers have something special planned for you all."
    HR "As I said on the first day of class, if you're here, {i}you{/i}, or at the very least someone you know, {i}will{/i} be growing."
    HR "Some people try to ignore this fact for as long as possible, but trust me, it's best to confront this sooner rather than later. All of you have likely noticed the changes taking place in your fellow classmates already."
    HR "But that doesn't necessarily mean you've fully noticed the changes in yourself. Though you will today if you haven't already."
    HR "This little activity was Hageshi-san's idea, so blame him if you'd rather be somewhere else, but it's been pretty successful ever since we started it in the few years since he's been here."
    HR "Hmm? {w}Speaking of Hageshi-san..."
    play music RM

    show HR unique at altMove(0.5, 0.25) with None
    show Hageshi neutral
    show RM concerned-2 at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    Hageshi "Look what I found crawling in the vents."
    "Hageshi-sensei was carrying Daichi by his collar, like he had pulled out a stray cat from a storm drain."
    Hageshi "Nice try Utagashi-san, but no one gets out of this."
    show HR neutral
    HR "Thank you, Hageshi-san."
    hide RM with dissolve
    extend " Well, looks like the gang's all here. Let's get into what you'll be doing. I'll let Naoki-san give you the run-down."
    hide HR
    hide Hageshi
    with dissolve
    play music Busy
    #show Naoki neutral with dissolve
    if not getFlag("Meet_Naoki"):
        $setFlag("Meet_Naoki")
    Naoki "Thanks Tashi-san. You can all just call me Coach Naoki or Naoki-sensei."
    if isEventCleared("MC002"):
        MCT "That's the guy I saw in the faculty room with three whistles. I guess that explains why he has {i}a{/i} whistle— but not three."
    Naoki "Today we're going to be playing a game called handball. As you might have guessed by the name, you handle a ball... with your hands. It's not that complicated really."
    Naoki "Sort of like soccer where you pass the ball and score only using your feet, just think the opposite of that."
    Naoki "To score, you throw the ball into the goal. {w}Have I lost anyone yet? Good. {w}Doesn't matter if you bounce it off the floor, if it's in, it's in."
    Naoki "Now the caveat is that when shooting a goal, you can't step into the goal zone near the goal. That's only for the goalie, no one else. You have to shoot it behind that line."
    Naoki "You can't hold on to the ball for more than three seconds, and you can't take more than three steps with the ball, but you're allowed to dribble it to get around this."
    Naoki "No pushing, shoving, or trying to pull the ball out of another player's hand, but you are allowed to block them and their throws, obviously. Other than that, you need to be trying to score— no stalling."
    Naoki "That's basically everything, any questions?"
    show RM doubt with dissolve
    RM "Yes, what is the point of all of this?"
    Naoki "You will see soon enough, Utagashi-san. {w}You all will, trust me."
    hide RM with dissolve
    Naoki "Alright, let's set the teams here, give us a second."
    Naoki "{size=-6}How should we balance them out, Hageshi-san?{/size}"
    #hide Naoki with dissolve

    if getHighestAffection() == ("BE" or "GTS" or "AE"):
        $setFlag("MC006_Team1")
        jump MC006_Team1
    elif getHighestAffection() == ("WG" or "FMG" or "PRG"):
        $setFlag("MC006_Team2")
        jump MC006_Team2
    else:
        $setFlag("MC006_Team1")
        jump MC006_Team1

label MC006_Team1:
    show RM neutral with dissolve
    #show MC neutral with dissolve
    Hageshi "{size=-6}Well, we should probably split the guys between the two teams to be fair.{/size}"
    Naoki "{size=-6}Yup, good call.{/size}"
    hide RM with dissolve
    #hide MC with dissolve
    Hageshi "{size=-6}We definitely need to spread out the power.{/size}"
    show GTS neutral at Position(xcenter=0.2, yalign=1.0)
    show FMG neutral at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    extend " {size=-6}So I'd say put the tall one opposite the strong one.{/size}"
    hide GTS neutral
    hide FMG neutral
    with dissolve
    pause .3
    show BE neutral at Position(xcenter=0.2, yalign=1.0)
    show PRG neutral at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    Naoki "{size=-6}The top-heavy ones are going to have similar issues to each other.{/size}"
    Hageshi "{size=-6}Agreed, should spread them out too.{/size}"
    hide BE neutral
    hide PRG neutral
    with dissolve
    pause .3
    show AE neutral at Position(xcenter=0.2, yalign=1.0)
    show WG neutral at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    Naoki "{size=-6}Which leaves the bottom-heavy ones.{/size}"
    Hageshi "{size=-6}Seems to be about the best we can do to make things fair.{/size}"
    Naoki "Alright, Team 1 is Hotsure-san, Inoue-san, Yamazaki-san, and Matsumoto-san. Team 2 is Utagashi-san, Nikumaru-san, Mizutani-san, and Kodama-san."
    show WG doubt
    WG "Just what exactly are we hoping to gain by winning?"
    show WG doubt
    show HR neutral at Position(xcenter=0.4, yalign=1.0) with dissolve
    HR "Good question, Nikumaru-san. Since the self-satisfaction of a job well done is a rather lack-luster reward, we decided to offer that the winning team will be taken off the class clean up rotation for the next month."
    show WG surprised-2
    show HR unique
    WG "That is not a paltry incentive..."
    hide AE
    show FMG happy at Position(xcenter=0.2, yalign=1.0)
    FMG "Sweet! Anything to get out of that boring stuff."
    show BE happy at Position(xcenter=0.6, yalign=1.0) with dissolve
    BE "Not before me you aren't!"
    Naoki "Alright. We'll do a quick coin toss. Heads Team 1 starts with the ball, tails Team 2 starts with it."
    pause .3
    Naoki "Heads! Team 1 starts with the ball."
    show BE shrug
    BE "I still don't know what we're supposed to be doing."
    show WG neutral
    WG "It sounds simple enough, it can't be that hard."
    show FMG flex
    FMG "Yeah, just grab the ball and throw it in the goal, that's all there is to it!"
    hide BE
    hide WG
    hide FMG
    hide HR
    show RM sad
    with dissolve
    RM "Can I just go back to my dorm?"
    hide RM
    show AE pondering at Position(xcenter=0.2, yalign=1.0)
    show BE neutral
    show GTS neutral at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    AE "We should probably think of a strategy for the team positions."
    MC "I don't know if it's that big of a difference what people do. Why don't we just go with what people want to do?"
    show GTS pondering
    GTS "I'm not sure where I could best be utilized."
    MC "Personally, I think you'd be great up front to help block shots, Yamazaki-san."
    show GTS neutral-2
    GTS "If you think so, I will give it my best effort."
    MC "Honoka, you've played soccer before, would you be up for being our goalie? It doesn't seem that different for this game."
    show BE happy
    BE "Sounds good to me!"
    show AE neutral
    AE "That is fine with me as well. I don't claim any remarkable athletic ability, so I would not want to bear the responsibility for preventing the opposing team from scoring."
    MC "Okay, sounds like we got something worked out."
    Naoki "Alright, Team 1, here you go."
    play sound Whistle
    hide BE with dissolve
    "Coach Naoki tossed the ball to Shiori. Naomi and I scrambled up the field to get in position for a pass."
    "Shiori tossed up a leading pass to Naomi... only for her to completely blow past it with unexpected speed, landing it out of bounds."
    show GTS surprised
    show AE pondering
    GTS "Oh my... I apologize for my error."
    "Naomi had clearly covered a lot more ground with each stride than she had estimated."
    AE "It's alright. I'm not the best thrower."
    Naoki "Out of bounds, Team 2 gets the ball."
    hide GTS
    hide AE
    show WG neutral
    with dissolve
    "Coach Naoki tossed the ball to Alice, who took a casual pace dribbling it up the court until she saw me rushing to defend against her."
    show WG neutral at altMove(0.25, 0.2)
    show FMG happy at Position(xcenter=0.8, yalign=1.0) with dissolve
    "Seeing an opening, she passed the ball to Akira."
    FMG "We're getting on the board with this one!"
    "Akira fired off a shot like a cannon toward the goal..."
    show WG surprised-2
    show FMG surprised
    extend " {w}Only to have it sail clean over the goal by more than a meter."
    FMG "Oops! A little too much on that one I guess."
    show WG doubt
    WG "You weren't even close."
    show FMG angry-2
    FMG "Hey now..."
    hide WG
    hide FMG
    show BE neutral
    with dissolve
    Naoki "Team 1 gets the ball."
    play sound Thud
    show BE surprised
    MC "Ow!"
    "Coach Naoki apparently had tossed the ball to me, from the side, but I didn't see it, and it smacked me upside the head."
    show BE surprised at altMove(0.5, 0.4)
    show AE angry-2 at Position(xcenter=0.6, yalign=1.0) with dissolve
    AE "Pay attention, Hotsure-san."
    show AE neutral-eyebrow
    MC "I am! I didn't see it."
    "Picking up the ball I began to dribble down field looking for an opening to pass."
    hide BE
    hide AE
    show GTS neutral-2 at Position(xcenter=0.2, yalign=1.0)
    show RM distrustful at Position(xcenter=0.4, yalign=1.0)
    with dissolve
    "Naomi made that an easy decision, standing a head taller than Daichi who was trying to guard her. I tossed it over and she caught it with both hands."
    show GTS surprised
    "Seeing an opening, she bounced it across the floor toward the goal."
    show PRG scared at Position(xcenter=0.6, yalign=1.0)
    with dissolve
    "Aida was clearly surprised at the realization the ball was headed directly towards her. She could have easily blocked the overly cautious toss, but her hesitancy caused too much delay while the ball went into the goal."
    show PRG worried
    PRG "I-I'm sorry. I-I could've stopped that."
    hide GTS
    show WG neutral at Position(xcenter=0.2, yalign=1.0) behind RM
    with dissolve
    WG "Don't worry too much about it Aida."
    show WG stern
    extend " {i}Someone{/i} didn't do their job of blocking the pass."
    show RM angry
    RM "Hey! Just what exactly was I supposed to do to block Yamazaki-san?"
    show WG doubt
    WG "{i}Anything{/i}— for a start."
    show PRG sad-2
    PRG "P-Please don't fight..."
    "It didn't take someone as sensitive as Aida to realize frustrations and tensions were already starting to mount."
    Naoki "Team 2, here you go!"
    hide PRG
    hide WG
    hide RM
    show FMG happy at Position(xcenter=0.2, yalign=1.0)
    show GTS neutral at Position(xcenter=0.4, yalign=1.0)
    with dissolve
    "Coach Naoki tossed it to Akira. With Naomi rushing up to guard her,"
    show AE neutral at Position(xcenter=0.6, yalign=1.0)
    show RM neutral at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    extend " she didn't have a shot, so she tossed it to Daichi, who was being guarded by Shiori."
    play sound Boing
    show RM doubt at altMove(0.35, 1.2)
    show AE surprised at altMove(0.5, 0.8)
    "In her eager attempt to give her best efforts, Shiori unexpectedly hip-checked Daichi out of bounds, catching the ball like it was intended for her."
    "There wasn't going to be enough time for Shiori to process what just happened before others closed in."
    hide FMG
    hide RM
    hide GTS
    with dissolve
    MC "Matsumoto-san, toss it here!"
    play sound Thud
    show AE angry-3
    "What should have been a simple pass alluded me as I lost track of its arc when I looked up into my bangs and it hit me smack dab in the middle of my forehead."
    show WG haughty at Position(xcenter=0.4, yalign=1.0) with dissolve
    WG "Got it!"
    show WG at altMove(0.5, 0.5)
    hide AE with dissolve
    "Seizing on the confusion, Alice snatched up the ball and ran it back up the court before anyone reacted."
    show WG surprised
    "Looking to get close to take a shot, she was caught off guard by the momentum she was carrying as her inertia pulled her into the goal zone before she could stop herself."
    Naoki "Out of bounds, Team 1 gets the ball back."
    hide WG
    show GTS neutral at Position(xcenter=0.25, yalign=1.0)
    show AE neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    "Naoki tossed the ball to Naomi. She was looking for an opening and tossed it to Shiori—"
    show FMG neutral with dissolve
    extend " but Akira unexpectedly jumped up to intercept it."
    "But as athletic as Akira was, she couldn't contend that well with Naomi, who immediately turned back around to guard her."
    hide AE
    show RM neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    extend " Akira ditched the ball to Daichi, who threw a pretty basic throw that was way too predictable for Honoka."
    show FMG sad-2
    show RM sad
    with None
    show BE happy at Position(xcenter=0.25, yalign=1.0)
    hide GTS
    with dissolve
    BE "Too easy. Here you go, Kei-chan!"
    show BE surprised
    "Honoka's toss that was intended for me came up way too short and off to the side. It seemed her chest had gotten in the way of her throwing arc."
    MC "What was that?"
    BE "I don't know! Grab it Kei-chan!"
    show FMG happy
    "Before I could process what just happened, Akira snatched up the ball."
    "Despite what was by all accounts a wild shot that ended up hitting the goal bar,"
    show FMG flex
    extend " it still managed to bounce into the goal."
    show BE sad
    play sound Whistle
    hide FMG
    hide BE
    hide RM
    with dissolve
    Naoki "Alright, the first half is done. Score is 1 to 1. {size=-6}Usually handball games have higher scores than this...{/size}"
    show WG doubt at Position(xcenter=0.4, yalign=1.0) with dissolve
    WG "Would it kill you to pass the ball every now and then?"
    show FMG angry-3 at Position(xcenter=0.6, yalign=1.0) with dissolve
    FMG "Hey, I got us on the board, what more do you want?"
    show PRG sad-2 at Position(xcenter=0.2, yalign=1.0) with dissolve
    PRG "W-We'd be ahead already if it wasn't for me..."
    show RM distrustful at Position(xcenter=0.8, yalign=1.0) with dissolve
    RM "Why are they making us do this?"
    pause .3
    hide PRG
    hide WG
    hide RM
    hide FMG
    show BE sad at Position(xcenter=0.25, yalign=1.0)
    with dissolve
    BE "Sorry I didn't stop Mizutani-san, guys."
    show GTS sad at Position(xcenter=0.75, yalign=1.0) with dissolve
    GTS "You shouldn't put so much pressure on yourself, Inoue-san. If anything, I haven't performed that well."
    MC "What are you talking about Yamazaki-san? You're our best defender and you're the only one that scored."
    show GTS neutral
    show AE neutral with dissolve
    AE "I agree with Hotsure-san."
    show AE pondering
    extend " My efforts at defense were of... mixed results, I would say, for comparison."
    show BE doubt
    BE "This hasn't really been going well, has it?"
    MC "Oh come on, we can't be the worst class to have ever done this."
    hide AE
    hide BE
    hide GTS
    with dissolve
    pause .2
    #show Naoki neutral with dissolve
    show HR neutral at Position(xcenter=0.25, yalign=1.0)
    show Hageshi neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    HR "{size=-4}...I think this is the worst any class has ever done.{/size}"
    show HR unique
    Naoki "{size=-4}I can't think of any exceptions myself.{/size}"
    Hageshi "{size=-4}That may be so, but try not to say that too loudly.{/size}"
    "I may have been half blind, but I wasn't deaf to what the teachers were murmuring to themselves. {w}This was even worse than I thought."
    hide HR
    #hide Naoki with dissolve
    hide Hageshi
    show FMG sad-2 at Position(xcenter=0.10, yalign=1.0)
    show WG angry at Position(xcenter=0.28, yalign=1.0) behind FMG
    show PRG sad at Position(xcenter=0.45, yalign=1.0)
    show BE doubt at Position(xcenter=0.6, yalign=1.0) behind PRG
    show GTS sad at Position(xcenter=0.75, yalign=1.0)
    show AE sad-2 at Position(xcenter=0.9, yalign=1.0) behind GTS
    with dissolve
    "No one was used to their changing bodies. Everyone was feeling frustrated with themselves and everyone else."
    $setSkill("Athletics", 1)
    "Not to mention I was already feeling beat. Keeping up in a game of handball was proving much tougher than I had initially suspected."
    "This was a complete disaster. Something had to change if we were going to turn this around. Not just for myself, but everyone else."
    "But what was I going to do to change any of that? I could barely see anymore with this tangled mess in front of my face!"
    hide FMG
    hide WG
    hide AE
    hide GTS
    hide PRG
    with dissolve
    MCT "Wait a second..."
    MC "Honoka, do you have any spare hair clips?"
    show BE confused at altMove(0.5, 0.5)
    BE "I do, gotta be prepared after all. Why?"
    MC "I gotta do something to get this thing growing out of my head under control. {w}Just give me everything that you have."
    "Honoka reached into her pocket and gave me nearly a handful."
    MC "Just how prepared did you think you had to be?"
    show BE shrug
    BE "You never know."
    show BE happy
    extend " Shouldn't you be glad?"
    MC "Probably, but I'm just more confused than anything."
    "I didn't have a mirror to see what I was doing, but I don't know if it would have made a difference. Frankly, I had no idea what the hell I was doing."
    "I just started pinning clips in my hair and tying off wads of it with purple scrunchies a handful at a time. I had never really thought too much about having to style my hair before."
    show BE surprised-2 at altMove(0.5, 0.65)
    show PRG surprised at Position(xcenter=0.35, yalign=1.0) with dissolve
    "I knew it had to have been a little jumbled, but judging by everyone's reactions, I must have looked like a mangled doll that was styled by a toddler."
    show BE wink
    BE "Oooooh, looking hot, Kei-chan~"
    MC "That bad?"
    show BE happy
    BE "Bahaha! You wouldn't believe!"
    hide BE
    show AE smile at Position(xcenter=0.65, yalign=1.0)
    with dissolve
    AE "{i}Hm! Pft{/i}... hehe!"
    "I knew it was bad, but if Shiori couldn't fully stifle her chuckle then I obviously looked like a total doofus."
    hide PRG
    show GTS surprised at Position(xcenter=0.35, yalign=1.0)
    with dissolve
    GTS "Is everything alright, Hotsure-san?"
    hide AE
    show WG doubt at Position(xcenter=0.65, yalign=1.0)
    with dissolve
    WG "You look completely ridiculous."
    hide GTS
    show FMG neutral at Position(xcenter=0.35, yalign=1.0)
    with dissolve
    FMG "Haha! Sweet doo, dude!"
    hide WG
    show PRG embarrassed at Position(xcenter=0.65, yalign=1.0)
    with dissolve
    PRG "I-I'm not sure that's quite... um, your style, Hotsure-san."
    "Okay, so it was really bad if even Aida had to say something."
    hide FMG
    hide PRG
    show RM neutral
    with dissolve
    RM "Even I don't know what is going on anymore."
    MC "Hey now, you may not like it, but this is what peak performance looks like... or at least peak peripheral vision."
    hide RM
    show HR unique at Position(xcenter=0.25, yalign=1.0)
    show Hageshi neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    #show Naoki with dissolve
    Hageshi "Adapt and overcome. I'm actually impressed with your effort, Hotsure-san."
    Naoki "That's the kind of determination we like to see."
    show HR neutral
    HR "I don't know if anyone likes to see that."
    show HR unique
    MCT "I'm not going back to playing blind, at this point it's best if I just own it."
    hide HR
    hide Hageshi
    #hide Naoki with dissolve
    show FMG sad at Position(xcenter=0.10, yalign=1.0)
    show WG doubt at Position(xcenter=0.25, yalign=1.0) behind FMG
    show BE doubt at Position(xcenter=0.6, yalign=1.0) behind PRG
    show GTS pondering at Position(xcenter=0.75, yalign=1.0)
    show AE pondering at Position(xcenter=0.9, yalign=1.0) behind GTS
    show RM sad at Position(xcenter=0.4, yalign=1.0)
    show PRG worried at Position(xcenter=0.5, yalign=1.0)
    with dissolve
    MC "Alright guys, come on now. Let's get back out there and get at it. {w}Maybe we all look a little ridiculous, but we can't let that stop us from trying to do better."
    show BE neutral
    show AE neutral
    show GTS neutral-2
    show WG neutral
    show FMG neutral
    show PRG neutral
    show RM neutral
    MC "Besides, no matter what you're worried about with yourself before, just remember you can't do anything to look worse than this."
    hide AE
    hide GTS
    hide WG
    hide FMG
    hide PRG
    hide RM
    with dissolve
    show BE happy
    BE "You can say that again, Kei-chan!"
    MC "Can you be a little more supportive, Honoka?"
    show BE angry at altMove(0.5, 0.5)
    BE "Okay, okay!"
    show BE happy
    extend " Kei-chan's right. Let's go out there and kick some butt!"
    hide BE
    show FMG happy
    FMG "Yeah! We got this. Let's go, team!"
    hide FMG
    show WG doubt
    WG "We certainly can't do any worse than before."
    hide WG
    show RM neutral
    RM "That remains to be seen."
    hide RM with dissolve
    "Some things needed to change if we were going to do our best. I had a few ideas."
    show AE neutral at Position(xcenter=0.25, yalign=1.0)
    show BE neutral
    show GTS neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    MC "I take back what I said earlier. Matsumoto-san is right. We should strategize. {w}I think Yamazaki-san's reach would be best utilized for our goalie."
    BE "Good thinking, Kei-chan."
    show GTS neutral-2
    GTS "If you think that is best."
    MC "Don't worry, you'll do fine."
    MC "Honoka, why don't you try an underhand pass to get around, erm..."
    show BE seductive
    BE "Get around what, Kei-chan?"
    MC "You know what I mean."
    show AE happy
    AE "Any insight as to how I could improve?"
    MC "Don't be afraid to get in there and block them with your body, Matsumoto-san. It's certainly allowed in the rules."
    show AE smile
    AE "Right. I'll try to keep that in mind."
    hide BE
    hide AE
    hide GTS
    with dissolve
    Naoki "Alright, Team 1 won the coin toss, so Team 2 gets the ball at the start of this half."
    show RM smug at Position(xcenter=0.25, yalign=1.0) with dissolve
    play music Motivation
    "Coach Naoki tossed the ball to Daichi. With a bit more pep in his step than I had anticipated, he trotted up field a few strides before passing it to Alice."
    show WG neutral at Position(xcenter=0.85, yalign=1.0) with dissolve
    "Alice ran up close to the goal zone, this time leaving adequate time to stop herself short before going over the line."
    show WG angry at altMove(0.4, 0.65)
    show GTS neutral at Position(xcenter=0.85, yalign=1.0) with easeinright
    extend " Her effort to score though was thwarted when Naomi swatted the ball away before it could reach the goal."
    show RM sad
    show GTS unique
    GTS "Here, take the ball, Inoue-san."
    hide RM
    hide WG
    show BE happy at Position(xcenter=0.45, yalign=1.0)
    with dissolve
    "Honoka grabbed the toss and quickly ran up the court."
    show BE surprised-2
    show FMG upbeat at Position(xcenter=0.25, yalign=1.0) with easeinleft
    extend " Realizing she was about to be blocked by Mizutani-san, she sailed an underhand toss to me."
    MCT "I got it this time!"
    show BE surprised
    BE "Shoot it, Kei-chan!"
    MC "R-Right!"
    "I fired off a shot, not thinking too much about it, but just trying to aim for the center."
    hide GTS
    show PRG surprised at Position(xcenter=0.85, yalign=1.0)
    with dissolve
    "In a surprising show of confidence, Aida got in front of my shot, and batted the ball to the ground."
    show FMG happy
    FMG "Nice block Kodama-san!"
    show PRG unique-happy
    PRG "Th-Thank you!"
    hide BE with dissolve
    "Aida picked up the ball that had bounced harmlessly into the goal zone and passed it to Daichi."
    show RM smug with dissolve
    "Daichi looked a bit more confident in himself than before and managed to work his way down the court with a surprising degree of elusiveness."
    hide FMG
    hide PRG
    show WG haughty at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    extend " Seeing an opening to toss it to Alice, he lobbed it over to her."
    show AE neutral-smug at Position(xcenter=0.65, yalign=1.0) with easeinright
    show WG angry
    "But Shiori had other plans, as she managed to body block Alice out of a clean catch and blocked the pass."
    hide RM
    show BE surprised-2
    with dissolve
    BE "I got it!"
    "Honoka scrambled for the dropped ball. I did my best to keep pace with her as we both ran toward the goal zone. {w}In a last second change up, she passed me the ball."
    hide BE
    hide AE
    hide WG
    show PRG surprised
    with dissolve
    "The sudden confusion about where the ball was coming from was enough to let me lob a straight shot into the goal before Aida could adjust."
    Naoki "Team 1 scores, 2-1."
    show PRG embarrassed
    PRG "S-Sorry."
    show FMG neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    FMG "Don't worry about it, Kodama-san."
    show WG neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    WG "I think we were all caught off guard by what just happened."
    Naoki "Team 2 gets the ball."
    hide WG
    hide PRG
    hide FMG
    show RM smug
    with dissolve
    "Daichi got the hand off this time again."
    show AE surprised at Position(xcenter=0.75, yalign=1.0) with dissolve
    "Dribbling the ball up the court, he managed to fake out Shiori with where he was going. {w}I still don't understand how this pasty nerd was so quick and agile."
    hide AE
    show WG neutral at Position(xcenter=0.25, yalign=1.0)
    with dissolve
    "He managed to get a clean pass off to Alice."
    show BE happy at Position(xcenter=0.35, yalign=1.0) with dissolve
    "But Honoka was eager to pounce in her face to block the shot."
    show FMG happy at Position(xcenter=0.75, yalign=1.0) with dissolve
    extend " Realizing the lost opportunity, Alice passed it to Akira."
    hide BE
    hide RM
    hide WG
    with dissolve
    "Grabbing the ball, Akira elected for a more reserved throw this time,"
    show GTS surprised at Position(xcenter=0.45, yalign=1.0) with dissolve
    extend " tossing it low and bouncing it off the floor before Naomi could reach down fast enough to block the shot, it went in easily."
    Naoki "Team 2 scores! 2-2. {w}Team 1 gets the ball."
    hide GTS
    hide FMG
    show AE neutral-smug at Position(xcenter=0.25, yalign=1.0)
    show BE neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    "Coach Naoki served me the ball. My plan was to toss it to Shiori to buy time for Honoka to get into position..."
    play sound Whistle
    hide AE
    hide BE
    pause 1
    Naoki "Times up. Final score 2 to 2. It's a tie."
    play music Peaceful
    show HR neutral at Position(xcenter=0.45, yalign=1.0) with dissolve
    HR "Looks like no one wins the prize then."
    show HR unique
    All "Awww!"
    Hageshi "No whining now. You should be proud of yourselves. I have to admit, it was quite impressive to see everyone turn things around."
    Naoki "Hageshi-san is right. This started off as one of the worst games I'd seen, only to turn into one of the better ones in the second half."
    show HR neutral
    HR "So in a way, you're all winners."
    show WG doubt at Position(xcenter=0.15, yalign=1.0) with dissolve
    show HR unique
    WG "If no one won anything, it sounds like we're all losers."
    show HR neutral
    HR "That's one way of looking at it certainly, but I would suggest looking on the positive side of things. {w}Look, I don't say this often, but I'm proud of how you all were able to turn things around for yourself."
    show HR unique
    show AE happy at Position(xcenter=0.9, yalign=1.0) with dissolve
    AE "Thank you, Tashi-sensei."
    show HR neutral
    HR "Don't mention it. {w}Like literally, {w}ever again."
    show HR unique
    show FMG happy at Position(xcenter=0.3, yalign=1.0) behind HR with dissolve
    FMG "I think Tashi-sensei likes us!"
    show WG neutral
    show GTS happy-2 at Position(xcenter=0.75, yalign=1.0) with dissolve
    GTS "My sincerest gratitude, Tashi-sensei."
    show PRG unique-happy at Position(xcenter=0.6, yalign=1.0) behind HR with dissolve
    PRG "W-We like you too Tashi-sensei..."
    show HR neutral
    HR "{i}Ugggh{/i}.... please, no..."
    show HR unique with None
    hide AE
    hide GTS
    hide WG
    hide FMG
    hide PRG
    #show Naoki with dissolve
    show Hageshi neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    Naoki "I knew this guy was a softy at heart."
    Hageshi "You're not the only one, Aoi-san seems to think so too."
    show HR neutral
    HR "Alright, we're done here. Class dismissed."
    hide HR
    hide Hageshi
    with dissolve
    "So it wasn't exactly the greatest game of handball ever played. It was pretty clear things were starting to change. {w}{i}We{/i} were starting to change."
    "I wasn't sure what the future held for all of us, but for now I was glad we all got to have a little fun."
    jump daymenu

label MC006_Team2:
    show RM neutral with dissolve
    #show MC neutral with dissolve
    Hageshi "{size=-6}Well, we should probably split the guys between the two teams to be fair.{/size}"
    Naoki "{size=-6}Yup, good call.{/size}"
    hide RM with dissolve
    #hide MC with dissolve
    Hageshi "{size=-6}We definitely need to spread out the power.{/size}"
    show GTS neutral at Position(xcenter=0.2, yalign=1.0)
    show FMG neutral at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    extend " {size=-6}So I'd say put the tall one opposite the strong one.{/size}"
    hide GTS neutral
    hide FMG neutral
    with dissolve
    pause .3
    show BE neutral at Position(xcenter=0.2, yalign=1.0)
    show PRG neutral at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    Naoki "{size=-6}The top-heavy ones are going to have similar issues to each other.{/size}"
    Hageshi "{size=-6}Agreed, should spread them out too.{/size}"
    hide BE neutral
    hide PRG neutral
    with dissolve
    pause .3
    show AE neutral at Position(xcenter=0.2, yalign=1.0)
    show WG neutral at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    Naoki "{size=-6}Which leaves the bottom-heavy ones.{/size}"
    Hageshi "{size=-6}Seems to be about the best we can do to make things fair.{/size}"
    Naoki "Alright, Team 1 is Utagashi-san, Inoue-san, Yamazaki-san, and Matsumoto-san. Team 2 is, Hotsure-san, Nikumaru-san, Mizutani-san, and Kodama-san."
    show WG doubt
    WG "Just what exactly are we hoping to gain by winning?"
    show WG doubt
    show HR neutral at Position(xcenter=0.4, yalign=1.0) with dissolve
    HR "Good question, Nikumaru-san. Since the self-satisfaction of a job well done is a rather lack-luster reward, we decided to offer that the winning team will be taken off the class clean up rotation for the next month."
    show WG surprised-2
    show HR unique
    WG "That is not a paltry incentive..."
    hide AE
    show FMG happy at Position(xcenter=0.2, yalign=1.0)
    FMG "Sweet! Anything to get out of that boring stuff."
    show BE happy at Position(xcenter=0.6, yalign=1.0) with dissolve
    BE "Not before me you aren't!"
    Naoki "Alright. We'll do a quick coin toss. Heads Team 1 starts with the ball, tails Team 2 starts with it."
    pause .3
    Naoki "Heads! Team 1 starts with the ball."
    show BE shrug
    BE "I still don't know what we're supposed to be doing."
    show WG neutral
    WG "It sounds simple enough, it can't be that hard."
    show FMG flex
    FMG "Yeah, just grab the ball and throw it in the goal, that's all there is to it!"
    hide BE
    hide WG
    hide FMG
    hide HR
    show RM sad
    with dissolve
    RM "Can I just go back to my dorm?"
    hide RM
    show FMG neutral at Position(xcenter=0.2, yalign=1.0)
    show PRG neutral
    show WG stern at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    WG "I'm counting on a good performance out of the rest of you. I for one am {i}sick{/i} of wasting my time on cleaning duty when it comes up."
    show FMG flex
    show WG doubt
    FMG "Nothing to worry about. I'm gonna carry this team!"
    "Akira was strong, but between me, Aida and Alice... {w}Well, um... mostly Alice... That was a pretty heavy load."
    show PRG worried
    PRG "..."
    if isEventCleared("PRG007"):
        "But I was most worried about Aida."
        "Yeah, she was a fan of baseball and all, so I figured she had some knowledge of sports."
        "However, she was easily the smallest out of everyone, and athletic skill or no, I didn't want to see her get body checked from a defensive block."
    else:
        "But I was most worried about Aida."
        "She was easily the smallest of all of us and she didn't look to have the athleticism to make up for it. I didn't want to see her get body checked from a defensive block."
    MC "Aida, would you be interested in being our goalie?"
    FMG "{size=-6}Are you sure that's a good idea, dude?{/size}"
    MC "{size=-6}Do you really want to see Kodama-san try to guard Yamazaki-san?{/size}"
    show FMG surprised-2
    FMG "{size=-6}Good point.{/size}"
    show FMG neutral
    show WG neutral
    PRG "I-If you think so..."
    WG "I think that is a good idea as well."
    MC "Okay, sounds like we got something worked out."
    Naoki "Alright, Team 1, here you go."
    play sound Whistle
    hide FMG
    hide PRG
    hide WG
    show AE neutral at Position(xcenter=0.25, yalign=1.0)
    show GTS neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    "Coach Naoki tossed the ball to Shiori. Naomi scrambled up the field to get in position for a pass while our team tried to get in position to defend."
    "Shiori tossed up a leading pass to Naomi... only for her to completely blow past it with unexpected speed, landing it out of bounds."
    show GTS surprised
    show AE pondering
    GTS "Oh my... I apologize for my error."
    "Naomi had clearly covered a lot more ground with each stride than she had estimated."
    AE "It's alright. I'm not the best thrower."
    FMG "Looks like we dodged a bullet there."
    Naoki "Out of bounds, Team 2 gets the ball."
    hide GTS
    hide AE
    show WG neutral at Position(xcenter=0.25, yalign=1.0)
    with dissolve
    "Coach Naoki tossed the ball to Alice, who took a casual pace dribbling it up the court until she saw Daichi rushing to defend against her."
    show FMG happy at Position(xcenter=0.75, yalign=1.0) with dissolve
    "Seeing an opening, she passed the ball to Akira."
    FMG "We're getting on the board with this one!"
    "Akira fired off a shot like a cannon toward the goal..."
    show WG surprised-2
    show FMG surprised-2
    show BE confused with dissolve
    extend " {w}Only to have it sail clean over the goal by more than a meter."
    show FMG surprised
    FMG "Oops! A little too much on that one I guess."
    show WG doubt
    WG "You weren't even close."
    show FMG angry-2
    FMG "Hey now..."
    hide BE
    hide WG
    hide FMG
    with dissolve
    Naoki "Team 1 gets the ball."
    show RM concerned with dissolve
    "Coach Naoki apparently had tossed the ball to Daichi, who honestly looked like he didn't know what to do with it."
    show RM doubt with None
    show GTS neutral at Position(xcenter=0.25, yalign=1.0)
    show FMG neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    "Looking for a way to ditch it as I came running up to block him, Naomi made herself the easy choice with her extra reach above Akira."
    show GTS surprised
    "Seeing an opening, she bounced it across the floor toward the goal."
    hide RM
    show PRG scared
    with dissolve
    "Aida was clearly surprised at the realization the ball was headed directly towards her. She could have easily blocked the overly cautious toss, but her hesitancy caused too much delay while the ball went into the goal."
    show PRG worried
    PRG "I-I'm sorry. I should've stopped that."
    hide GTS
    show WG neutral at Position(xcenter=0.25, yalign=1.0)
    with dissolve
    WG "Don't worry too much about it, Aida."
    show WG stern
    extend " {i}Someone{/i} didn't do their job of blocking the pass."
    show FMG angry-3
    FMG "Like you could have done any better guarding Yamazaki-san."
    show WG stern
    WG "I thought you were supposed to \"carry this team\"?"
    show FMG angry
    FMG "..."
    show PRG sad-2
    PRG "P-Please don't fight..."
    "It didn't take someone as sensitive as Aida to realize frustrations and tensions were already starting to mount."
    Naoki "Team 2, here you go!"
    hide PRG with dissolve
    show FMG neutral
    show WG neutral
    "Coach Naoki tossed it to Akira."
    show GTS neutral with dissolve
    extend " With Naomi rushing up to guard her, she didn't have a shot, so she passed it"
    play sound Thud
    hide GTS with dissolve
    MC "Ow!"
    "Akira had apparently tossed the ball to me from the side, but I didn't see it, and it smacked me upside the head."
    show WG angry
    WG "Pay attention, Keisuke!"
    show WG stern
    MC "I am! I didn't see it."
    "Luckily I recovered the ball before someone thought to guard me after sending too many against Akira. I began to dribble down field looking for an opening to pass."
    "I had a clear line to Alice when suddenly—"
    play sound Boing
    hide FMG
    show AE surprised at Position(xcenter=0.75, yalign=1.0)
    show dummy with vpunch
    "In her eager attempt to give her best efforts, Shiori unexpectedly hip-checked me out of bounds, which led to me inadvertently tossing the ball right into her hands."
    "There wasn't going to be enough time for Shiori to process what just happened before others closed in."
    show RM smug at Position(xcenter=0.25, yalign=1.0)
    hide WG
    with dissolve
    RM "Matsumoto-san, toss it here!"
    play sound Thud
    show WG haughty
    "What should have been a simple pass was thwarted as Alice got in a solid body block that completely walled out Daichi."
    WG "Got it!"
    hide AE
    hide RM
    with dissolve
    "Seizing on the confusion, Alice snatched up the ball and ran it back up the court before anyone reacted."
    show WG surprised
    "Looking to get close to take a shot, she was caught off guard by the momentum she was carrying as her inertia pulled her into the goal zone before she could stop herself."
    Naoki "Out of bounds, Team 1 gets the ball back."
    show FMG angry-3 at Position(xcenter=0.75, yalign=1.0) with dissolve
    FMG "What was that?"
    show WG doubt at altMove(0.5, 0.25)
    WG "Oh, shut it!"
    MC "Well, I kind of dropped the ball too there, like literally dropped the ball."
    WG "Honestly Keisuke I don't know how you see anything with your hair like that."
    show FMG neutral
    FMG "I don't really get it either to be honest."
    MCT "That makes three of us."
    hide FMG
    hide WG
    show GTS neutral at Position(xcenter=0.25, yalign=1.0)
    show AE neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    "Naoki tossed the ball to Naomi. She was looking for an opening and tossed it to Shiori—"
    show FMG neutral with dissolve
    extend " but Akira unexpectedly jumped up to intercept it."
    show FMG surprised-2
    "But as athletic as Akira was, she couldn't contend that well with Naomi, who immediately turned back around to guard her."
    hide AE with dissolve
    extend " Akira ditched the ball to try to pass to me."
    play sound Thud
    show FMG surprised
    "Which ended up bouncing off my head before I caught it. {w} Still jumbled out of sorts from the impact, I scrambled to toss the ball into the goal in an arc that was way too predictable for Honoka."
    show FMG sad-2 with None
    show BE happy at Position(xcenter=0.75, yalign=1.0)
    hide GTS
    with dissolve
    BE "Too easy. Here you go, Utagashi-san!"
    show BE surprised
    show RM concerned at Position(xcenter=0.25, yalign=1.0) with dissolve
    "Honoka's toss that was intended for Daichi came up way too short and off to the side. It seemed her chest had gotten in the way of her throwing arc."
    show RM angry
    RM "What was that?"
    BE "I don't know! Just Grab it!"
    show FMG happy
    "Before they could process what just happened, Akira snatched up the ball."
    show FMG surprised
    "Despite what was by all accounts a wild shot that ended up hitting the goal bar,"
    show FMG flex
    extend " it still managed to bounce into the goal."
    show BE sad
    play sound Whistle
    hide FMG
    hide BE
    hide RM
    with dissolve
    Naoki "Alright, the first half is done. Score is 1 to 1. {size=-6}Usually handball games have higher scores than this...{/size}"
    show WG doubt at Position(xcenter=0.4, yalign=1.0) with dissolve
    WG "Would it kill you to pass the ball every now and then?"
    show FMG angry-3 at Position(xcenter=0.6, yalign=1.0) with dissolve
    FMG "Hey, I got us on the board, what more do you want?"
    show PRG sad-2 at Position(xcenter=0.2, yalign=1.0) with dissolve
    PRG "W-We'd be ahead already if it wasn't for me..."
    show RM distrustful at Position(xcenter=0.8, yalign=1.0) with dissolve
    RM "Why are they making us do this?"
    pause .3
    hide PRG
    hide WG
    hide RM
    hide FMG
    show BE sad at Position(xcenter=0.25, yalign=1.0)
    with dissolve
    BE "Sorry I didn't stop Mizutani-san, guys."
    show GTS sad at Position(xcenter=0.75, yalign=1.0) with dissolve
    GTS "You shouldn't put so much pressure on yourself, Inoue-san. If anything, I haven't performed that well."
    show BE neutral
    BE "What are you talking about Yamazaki-san? You're our best defender and you're the only one that scored."
    show GTS neutral
    show AE neutral with dissolve
    AE "I agree with Inoue-san."
    show AE pondering
    extend " My efforts at defense were of... mixed results, I would say, for comparison."
    show BE doubt
    BE "None of us have really been doing that well, have we?"
    MC "Oh come on, we can't be the worst class to have ever done this."
    hide AE
    hide BE
    hide GTS
    with dissolve
    pause .2
    show HR neutral at Position(xcenter=0.25, yalign=1.0)
    #show Naoki neutral with dissolve
    show Hageshi neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    HR "{size=-4}...I think this is the worst any class has ever done.{/size}"
    show HR unique
    Naoki "{size=-4}I can't think of any exceptions myself.{/size}"
    Hageshi "{size=-4}That may be so, but try not to say that too loudly.{/size}"
    "I may have been half blind, but I wasn't deaf to what the teachers were murmuring to themselves. {w}This was even worse than I thought."
    hide HR
    hide Hageshi
    #hide Naoki with dissolve
    show FMG sad-2 at Position(xcenter=0.10, yalign=1.0)
    show WG angry at Position(xcenter=0.28, yalign=1.0) behind FMG
    show PRG sad at Position(xcenter=0.45, yalign=1.0)
    show BE doubt at Position(xcenter=0.6, yalign=1.0) behind PRG
    show GTS sad at Position(xcenter=0.75, yalign=1.0)
    show AE sad-2 at Position(xcenter=0.9, yalign=1.0) behind GTS
    with dissolve
    "No one was used to their changing bodies. Everyone was feeling frustrated with themselves and everyone else."
    $setSkill("Athletics", 1)
    "Not to mention I was already feeling beat. Keeping up in a game of handball was proving much tougher than I had initially suspected."
    "This was a complete disaster. Something had to change if we were going to turn this around. Not just for myself, but everyone else."
    "But what was I going to do to change any of that? I could barely see anymore with this tangled mess in front of my face!"
    hide FMG
    hide WG
    hide AE
    hide GTS
    hide PRG
    with dissolve
    MCT "Wait a second..."
    MC "Honoka, do you have any spare hair clips?"
    show BE confused at altMove(0.5, 0.5)
    BE "I do, gotta be prepared after all. Why?"
    MC "I gotta do something to get this thing growing out of my head under control. {w}Just give me everything that you have."
    "Honoka reached into her pocket and gave me nearly a handful."
    MC "Just how prepared did you think you had to be?"
    show BE shrug
    BE "You never know."
    show BE happy
    extend " Shouldn't you be glad?"
    MC "Probably, but I'm just more confused than anything."
    "I didn't have a mirror to see what I was doing, but I don't know if it would have made a difference. Frankly, I had no idea what the hell I was doing."
    "I just started pinning clips in my hair and tying off wads of it a handful at a time. I had never really thought too much about having to style my hair before."
    show BE surprised-2 at altMove(0.5, 0.65)
    "I knew it had to have been a little jumbled, but judging by everyone's reactions, I must have looked like a mangled doll that was styled by a toddler."
    show BE wink
    BE "Oooooh, looking hot, Kei-chan~"
    MC "That bad?"
    show BE happy
    BE "Bahaha! You wouldn't believe!"
    hide BE
    show AE smile at Position(xcenter=0.65, yalign=1.0)
    with dissolve
    AE "{i}Hm! Pft{/i}... hehe!"
    "I knew it was bad, but if Shiori couldn't fully stifle her chuckle then I obviously looked like a total doofus."
    hide PRG
    show GTS surprised at Position(xcenter=0.35, yalign=1.0)
    with dissolve
    GTS "Is everything alright, Hotsure-san?"
    hide AE
    show WG doubt at Position(xcenter=0.65, yalign=1.0)
    with dissolve
    WG "You look completely ridiculous."
    hide GTS
    show FMG neutral at Position(xcenter=0.35, yalign=1.0)
    with dissolve
    FMG "Haha! Sweet doo, dude!"
    hide WG
    show PRG embarrassed at Position(xcenter=0.65, yalign=1.0)
    with dissolve
    PRG "I-I'm not sure that's quite... um, your style, Hotsure-san."
    "Okay, so it was really bad if even Aida had to say something."
    hide FMG
    hide PRG
    show RM neutral
    with dissolve
    RM "Even I don't know what is going on anymore."
    MC "Hey now, you may not like it, but this is what peak performance looks like... or at least peak peripheral vision."
    hide RM
    show HR unique at Position(xcenter=0.25, yalign=1.0)
    show Hageshi neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    #show Naoki with dissolve
    Hageshi "Adapt and overcome. I'm actually impressed with your effort, Hotsure-san."
    Naoki "That's the kind of determination we like to see."
    show HR neutral
    HR "I don't know if anyone likes to see that."
    show HR unique
    MCT "I'm not going back to playing blind, at this point it's best if I just own it."
    hide HR
    hide Hageshi
    #hide Naoki with dissolve
    show FMG sad at Position(xcenter=0.10, yalign=1.0)
    show WG doubt at Position(xcenter=0.25, yalign=1.0) behind FMG
    show BE doubt at Position(xcenter=0.6, yalign=1.0) behind PRG
    show GTS pondering at Position(xcenter=0.75, yalign=1.0)
    show AE pondering at Position(xcenter=0.9, yalign=1.0) behind GTS
    show RM sad at Position(xcenter=0.4, yalign=1.0)
    show PRG worried at Position(xcenter=0.5, yalign=1.0)
    with dissolve
    MC "Alright guys, come on now. Let's get back out there and get at it. {w}Maybe we all look a little ridiculous, but we can't let that stop us from trying to do better."
    show BE neutral
    show AE neutral
    show GTS neutral-2
    show WG neutral
    show FMG neutral
    show PRG neutral
    show RM neutral
    MC "Besides, no matter what you're worried about with yourself before, just remember you can't do anything to look worse than this."
    hide AE
    hide GTS
    hide WG
    hide FMG
    hide PRG
    hide RM
    with dissolve
    show BE happy
    BE "You can say that again, Kei-chan!"
    MC "Can you be a little more supportive, Honoka?"
    show BE angry at altMove(0.5, 0.5)
    BE "Okay, okay!"
    show BE happy
    extend " Kei-chan's right. Let's go out there and kick some butt!"
    hide BE
    show FMG happy
    FMG "Yeah! We got this. Let's go, team!"
    hide FMG
    show WG doubt
    WG "We certainly can't do any worse than before."
    hide WG
    show RM neutral
    RM "That remains to be seen."
    hide RM
    show PRG neutral
    with dissolve
    "Some things needed to change if we were going to do our best. I had a few ideas."
    MC "I think we can win this, we just need to play to our strengths."
    MC "Alice, you're our best defender,"
    show WG doubt at Position(xcenter=0.75, yalign=1.0) with dissolve
    extend " don't be afraid to get in there and use your..."
    show WG haughty
    extend " Um, commanding presence. Yes."
    show FMG happy at Position(xcenter=0.25, yalign=1.0) with dissolve
    MC "Akira, you're our best scorer..."
    show FMG neutral
    extend " Just try to ease up on those tosses."
    show FMG happy
    FMG "Right! I got this!"
    if isEventCleared("PRG007"):
        MC "Kodama-san, remember, this is just like baseball. Only, you don't even have to catch it. Just get in front of it and make sure it doesn't get past you. I know you can do it."
        PRG "I... r-right. I can do that."
    else:
        MC "Kodama-san, don't be afraid of the ball. I know it can be fast, but it isn't very hard. Just put out your hands and it'll bounce right off of you, I promise."
        PRG "I-I think I can do that."
    MC "Trust me, you'll do fine. We all will."
    Naoki "Alright, Team 1 won the coin toss, so Team 2 gets the ball at the start of this half."
    hide FMG
    hide PRG
    hide WG
    with dissolve
    play music Motivation
    "Coach Naoki tossed the ball to me, which to everyone's surprise, (including myself) I caught with no problem. {w} I trotted up the field looking for an opening before I tossed it to Alice."
    show WG neutral with dissolve
    "Taking it and running with it, Alice ran up close to the goal zone, this time leaving adequate time to stop herself short before going over the line."
    show WG angry
    show GTS neutral-2 at Position(xcenter=0.75, yalign=1.0) with dissolve
    extend " Her effort to score though was thwarted when Naomi swatted the ball away before it could reach the goal."
    MC "Dangit, that was clever of them to switch out Yamazaki-san for Honoka as the goalie."
    show GTS unique
    GTS "Here, take the ball, Inoue-san."
    hide WG
    show BE happy at Position(xcenter=0.2, yalign=1.0)
    with dissolve
    "Honoka grabbed the toss and quickly ran up the court."
    show BE surprised-2 with None
    show FMG upbeat at Position(xcenter=0.35, yalign=1.0)
    hide GTS
    with dissolve
    extend " Realizing she was about to be blocked by Mizutani-san, she sailed an underhand toss to Daichi."
    show RM doubt at Position(xcenter=0.75, yalign=1.0) with dissolve
    RM "What am I supposed to do with this?"
    show FMG neutral
    show BE surprised
    BE "Just shoot the ball for crying out loud!"
    show RM happy
    RM "R-Right!"
    "Daichi fired off a shot, not thinking too much about it, but just trying to aim for the center."
    show PRG surprised at Position(xcenter=0.55, yalign=1.0) with dissolve
    "In a surprising show of confidence, Aida got in front of Daichi's shot, and batted the ball to the ground."
    hide RM with dissolve
    show FMG happy
    FMG "Nice block Kodama-san!"
    show PRG unique-happy
    PRG "Th-Thank you!"
    hide BE with dissolve
    "Aida picked up the ball that had bounced harmlessly into the goal zone and passed it to me."
    "Dribbling it up the court, I felt a lot more confident in myself now that I could see what was going on around me."
    hide FMG
    hide PRG
    show WG haughty
    with dissolve
    extend " Seeing an opening to toss it to Alice, I lobbed it over to her."
    show AE neutral-smug at Position(xcenter=0.65, yalign=1.0) with dissolve
    show WG angry
    "But Shiori had other plans, as she managed to body block Alice out of a clean catch and disrupt the pass."
    show BE surprised-2 at Position(xcenter=0.25, yalign=1.0) with dissolve
    BE "I got it!"
    hide AE
    hide WG
    with dissolve
    "Honoka scrambled for the dropped ball. I did my best to keep pace with her as I tried to follow her to the goal zone."
    show RM smug at Position(xcenter=0.75, yalign=1.0) with dissolve
    " In a last second change up, she passed Daichi the ball."
    show PRG surprised with dissolve
    "The sudden confusion about where the ball was coming from was enough to let him lob a straight shot into the goal before Aida could adjust."
    Naoki "Team 1 scores, 2-1."
    hide BE
    hide RM
    with dissolve
    show PRG embarrassed
    PRG "S-Sorry."
    show FMG neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    FMG "Don't worry about it, Kodama-san."
    show WG neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    WG "I think we were all caught off guard by what just happened."
    Naoki "Team 2 gets the ball."
    hide WG
    hide FMG
    hide PRG
    with dissolve
    "I got the hand off this time again."
    show AE surprised with dissolve
    "Dribbling the ball up the court, I somehow managed to fake out Shiori with a sudden pivot in direction."
    hide AE
    show WG neutral
    with dissolve
    "Seeing an opening, I got a clean pass off to Alice."
    show BE happy at Position(xcenter=0.65, yalign=1.0) with dissolve
    "But Honoka was eager to pounce in her face to block the shot. {w}Realizing the lost opportunity, Alice passed it to Akira."
    show FMG happy at Position(xcenter=0.25, yalign=1.0)
    hide WG
    with dissolve
    "Grabbing the ball, Akira elected for a more reserved throw this time,"
    show GTS surprised with dissolve
    extend " tossing it low and bouncing it off the floor before Naomi could reach down fast enough to block the shot, it went in easily."
    Naoki "Team 2 scores! 2-2. {w}Team 1 gets the ball."
    show BE neutral at altMove(0.5, 0.75) with None
    show AE neutral-smug at Position(xcenter=0.25, yalign=1.0)
    hide GTS
    hide FMG
    with dissolve
    "Coach Naoki served Honoka the ball. My plan was to get up in her face to force a pass that Akira would intercept..."
    play sound Whistle
    hide AE
    hide BE
    pause 1
    Naoki "Times up. Final score 2 to 2. It's a tie."
    play music Peaceful
    show HR neutral at Position(xcenter=0.45, yalign=1.0) with dissolve
    HR "Looks like no one wins the prize then."
    show HR unique
    All "Awww!"
    Hageshi "No whining now. You should be proud of yourselves. I have to admit, it was quite impressive to see everyone turn things around."
    Naoki "Hageshi-san is right. This started off as one of the worst games I'd seen, only to turn into one of the better ones in the second half."
    show HR neutral
    HR "So in a way, you're all winners."
    show HR unique
    show WG doubt at Position(xcenter=0.15, yalign=1.0) with dissolve
    WG "If no one won anything, it sounds like we're all losers."
    show HR neutral
    HR "That's one way of looking at it certainly, but I would suggest looking on the positive side of things. {w}Look, I don't say this often, but I'm proud of how you all were able to turn things around for yourself."
    show HR unique
    show AE happy at Position(xcenter=0.9, yalign=1.0) with dissolve
    AE "Thank you, Tashi-sensei."
    show HR neutral
    HR "Don't mention it. {w}Like literally, {w}ever again."
    show HR unique
    show FMG happy at Position(xcenter=0.3, yalign=1.0) behind HR with dissolve
    FMG "I think Tashi-sensei likes us!"
    show WG neutral
    show GTS happy-2 at Position(xcenter=0.75, yalign=1.0) with dissolve
    GTS "My sincerest gratitude, Tashi-sensei."
    show PRG unique-happy at Position(xcenter=0.6, yalign=1.0) behind HR with dissolve
    PRG "W-We like you too Tashi-sensei..."
    show HR neutral
    HR "{i}Ugggh{/i}.... please, no..."
    show HR unique with None
    hide AE
    hide GTS
    hide WG
    hide FMG
    hide PRG
    show Hageshi neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    #show Naoki with dissolve
    Naoki "I knew this guy was a softy at heart."
    Hageshi "You're not the only one, Aoi-san seems to think so too."
    show HR neutral
    HR "Alright, we're done here. Class dismissed."
    hide HR
    hide Hageshi
    with dissolve
    "So it wasn't exactly the greatest game of handball ever played. It was pretty clear things were starting to change. {w}{i}We{/i} were starting to change."
    "I wasn't sure what the future held for all of us, but for now I was glad we all got to have a little fun."
    jump daymenu

label MC007:
    if not getFlag("RMRoute_Unlocked"):
        $setFlag("RMRoute_Unlocked")
    scene black with fade
    "..."
    RM "Hey, wake up!"
    MC "Wah?"
    scene Library with fade
    MCT "Why am I in the library?"
    MC "!"
    MC "Aw crap! I must have fallen asleep while studying."
    show RM neutral with dissolve
    play music RM
    RM "That much is obvious."
    MC "Hey, I've been studying hard. I deserve a break."
    show RM doubt
    RM "I'm sure that sounded more convincing in your head."
    MC "Alright, fine. You're right. I probably only got a solid five minutes of studying before I conked out. {w}What are you doing here anyway?"
    show RM happy
    RM "I'm searching for information."
    MC "I suppose the library would be the place for that. Trying to get a head start on the Yayoi Period paper for Tashi's class?"
    show RM distrustful
    RM "No. Not {i}school{/i} information. Information {i}about{/i} the school."
    MC "You've lost me already. What are you talking about?"
    show RM neutral
    RM "I'm not interested in the library {i}per se{/i}, but the library archives. Students aren't normally allowed access unless supervised by the librarian, but she's going to go on her break soon."
    MC "How do you know that? Did you canvas this place like you're going to pull off a bank heist?"
    show RM sad
    RM "..."
    MCT "On second thought, I'm probably better off not knowing."
    show RM neutral
    MC "Nevermind."
    RM "As I was saying. She's about to go on break. There's information in the archives I need to retrieve, information I'm sure the school doesn't want students to know."
    RM "This is where you come in. I need a lookout for when she comes back."
    menu:
        "No thanks. I'm busy studying.":
            show RM doubt
            MC "No thanks. I'm busy studying."
            RM "And how's that going for you?"
            MC "Alright, fine. I'm bored to tears, I'm up for anything but more studying."

        "Not like I have anything better to do.":
            show RM happy
            MC "Alright fine. Not like I have anything better to do."
            $setAffection("RM", 1)
            RM "Trust me, it'll help."
    show RM neutral
    "We walked towards the back of the library until we stopped at the threshold of a dimly lit room that seemed to be nothing but file cabinets."
    "It was small— for this school anyway— accessed by what appeared to be the first normal sized door I had seen in this entire place."
    MCT "Maybe Daichi is onto something here. This looks fishy {i}as hell{/i}."
    show RM distrustful
    RM "Alright, just pretend to cough or something if you spot the librarian coming back in."
    MC "What are you looking for anyway?"
    RM "I'll know it when I see it."
    MC "Well that's reassuring."
    show RM neutral
    "I split my attention between eyeing the door and eyeing what Daichi was doing in the room."
    "I had expected him to go haphazardly tearing through all the files he could get his hands on, but I began to be intrigued when I realized he seemed to actually have some idea what he was looking for."
    pause .5
    show RM smug
    "Appearing to have found something, Daichi nodded and smirked, having finally settled on one of the cabinets to open. Pulling out a noticeably worn, but intact file, he wiped away the years of dust off of it before reading its contents."
    MCT "Alright, now I'm curious."
    MC "What did you find?"
    show RM happy
    RM "Something that may lead to a breakthrough. Give me a minute to read it."
    show RM neutral
    RM "Alright, so most of these articles are dead ends, but look here. This is an article by the investigative journalist D.A. Kusoreikā."
    RM "{i}This{/i} particular article is about the first record of a growth factor. Apparently it was a female in her late teens. Name: Chie Kazomazumi."
    MC "The first one huh?"
    show RM doubt
    RM "First {i}official{/i} one anyway."
    MCT "Always the skeptic, this one."
    MC "What does it say about her?"
    show RM neutral
    RM "Apparently, she was about as average as average can be. However, around her eighteenth birthday in the early 1980s, her breasts started to enlarge to an extreme size."
    MCT "Huh, he might actually have found something worth a damn, assuming it's legit."
    MC "How big we talking here?"
    show RM doubt
    RM "Seriously? Is that what you're wondering?"
    MC "Just curious. These boobs literally made history after all."
    if getHighestAffection() == "BE":
        show RM neutral
        RM "Bigger than Inoue-san is currently, if that's what you're wondering."
        MCT "Man, wouldn't that be a sight... {w}Wait a second? Am I that easy to read?"
        MC "Um, well..."
        show RM smug
        RM "Hmph, thought so. You're pretty easy to read for a guy whose hair covers half his face."
        MC "Oh come on."
        RM "Heh. This is a great lead. I need to follow up on it."
    else:
        show RM neutral
        RM "Big enough then, apparently."
        show RM smug
        RM "Heh. This is a great lead. I need to follow up on it."
    MC "Alright, well good luck with that."
    show RM doubt
    RM "Where are you going?"
    show RM neutral
    MC "I'm headed back to the room. I'm obviously wasting time here if I can't keep my eyes open. Might as well catch a nap and get some real rest instead of tweaking my neck from using a textbook as a pillow."
    RM "Alright, I'll head back with you. I gotta start looking to see if I can find anything more online about this person."
    "Unfortunately for me we didn't get too far before something tripped Daichi's suspicion. Apparently we weren't the only people in the library at this time."
    "Before I could check who it was, Daichi grabbed me, forcing me to crouch down with him."
    show RM angry
    RM "Keep it down, who is that?!"
    MC "How should I know!?"
    RM "Well, go check! I made you the watch, what else am I paying you for?!"
    MC "I'm not being paid jack!"
    show RM smug
    RM "Not with that attitude you aren't. Now go check!"
    MC "Ugh, fine."
    hide RM with dissolve
    "Reluctantly, I sneaked around one of the bookshelves, and to my surprise..."
    show FMG neutral with dissolve
    MC "It's Akira Mizutani, why do you care if she catches us in the back?"
    RM "The fewer questions people ask, the better."
    hide FMG with dissolve
    show RM angry with dissolve
    RM "Why is she here?!"
    MC "Uh, because it's a school library and we have a big assignment coming up in one of our classes? {w}Besides, she's not the only one here."
    RM "What? Who's with her? Move over, let me see!"
    MCT "Just what else did he take from that file cabinet that's got him this paranoid?"
    "Daichi moved to the side to get a look for himself."
    hide RM with dissolve
    show FMG neutral at Position(xcenter=0.25, yalign=1.0), Transform(xzoom=-1)
    show WG neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    "Noticing the two of them, Daichi's eyes darted across the room in suspicion, no doubt looking for others. He had tried to be slick about his little heist, but it was obvious to see he was pretty worried about being found out."
    RM "Alice Nikumaru? Why's she here with Mizutani-san? And without the assistance of Kodama-san. That alone raises some red flags."
    MC "Yeah, about your mental state. {w}What is so unusual about seeing our classmates around campus?"
    RM "Shhh! Be quiet. I think they're about to talk..."
    WG "Mizutani-san? I must say I didn't expect to run into you here of all places."
    show FMG angry-2
    FMG "What's that supposed to mean?"
    show FMG neutral
    WG "I just hadn't expected you to be so industrious to start working on the paper for Tashi-sensei's class ahead of time."
    FMG "Eh, sorta. The gym was closed this morning because they were buffing the floors."
    show FMG sad-2
    extend " Why they had to pick chest day to do it, I'll never know."
    show FMG neutral
    FMG "I figured I might as well take the time to start something with the project while they finished, but I'm getting bored already."
    show WG worried
    WG "Admittedly I'm having trouble staying focused on the task at hand as well."
    show WG neutral
    extend " There isn't exactly an urgency to this task given how far out the assignment is, and quite frankly I think I could use a snack to help me focus better."
    show FMG happy
    FMG "You and me both!"
    show FMG flex
    extend " Hey! That gives me an idea."
    show FMG neutral
    extend " Do you know Kazomazumi Bakery on Genki Street?"
    show WG neutral-2
    WG "I do. Why do you ask?"
    FMG "Well, why don't we get out of here and head over there for some cupcakes? My treat."
    show WG pondering
    WG "Hmm, normally I'd be far too busy for such spurious changes to my schedule..."
    show WG haughty
    extend " but I think I can spare the time to work this in today."
    show WG happy-2
    extend " Especially if cupcakes are involved."
    show FMG happy
    FMG "That's what I figured."
    show WG doubt
    WG "What's that supposed to mean?"
    show FMG neutral
    FMG "Oh nothing..."
    show FMG flex
    extend " Come on, let's go."
    hide FMG
    hide WG
    with dissolve
    MC "Well there you go. Has your voyeuristic itch been scratched now?"
    show RM neutral with dissolve
    RM "Not so fast."
    MCT "Oh here we go..."
    show RM doubt
    RM "Don't tell me you didn't notice something peculiar mentioned in that conversation."
    MC "What? The thing with Kazomazumi Bakery you mean?"
    show RM angry
    RM "EXACTLY! Why would those two meet up at that specific bakery that shares the same name as the article of the first record growth I found on the same day!?"
    MC "...That it's a coincidence that they share the same name?"
    if getFlag("MC005RM"):
        show RM sad
        MC "You know, like the last time when you sent us on a wild goose chase on a hunch about someone's last name that turned up nothing?"
        MCT "In no small part because you were a giant chicken."
        show RM doubt
        RM "Being wrong once doesn't establish a pattern."
        MC "Yeah, well, it sure establishes precedence."
        show RM angry
        RM "Not every lead is going to be a big break, but never following up on any is the fastest way to get nowhere."
        show RM smug
        extend " Besides, how many Kazomazumi's do you know?"
    else:
        show RM neutral
        RM "...Well, how many Kazomazumi's do you know?"
        MC "..."
    MC "Alright, fine! It does seem like a strange coincidence, but so what?"
    show RM angry
    RM "What do you mean, \"so what\"? {w}There's something going on, and this is the best way I can think of to follow up on this lead. We should follow them over there."
    show RM neutral
    "Normally, I would have thought about this... but part of me did think this was a bit too convenient to just dismiss as coincidence."
    MC "Still though, why do we have to follow them?"
    if isEventCleared("MC001"):
        show RM happy
        RM "This is exactly the type of lead I told you about before you should be paying attention to in conversations. If you keep your senses sharp, you'll be able to pick up on things people don't even realize they're telling you."
        MCT "You mean like with this conversation and your mental diagnosis?"
        show RM distrustful
        MC "I'm not really picking up the significance of this to be honest."
        show RM doubt
        RM "Look, I'll admit, it's not much of a thread, but something's there. I mean {i}I{/i} hadn't heard of this place before, maybe they know something I don't? It's worth checking out every viable lead."
    else:
        RM "I hadn't heard of this place before, maybe they know something I don't. It's worth checking out every viable lead."
    show RM neutral
    "Following, tailing, spying, whatever you wanted to call it, I wasn't exactly comfortable with the notion, but I thought it might be best for me to go with Daichi since I didn't trust him not to make a scene without me."
    MC "Alright, let's go."
    RM "Alright, but first take this."
    "He handed me a baseball hat before putting one on himself."
    RM "We don't want those two to catch us spying on them."
    MC "W-Why do you even have these in the first place?"
    RM "You can never be too careful. Now then..."
    show RM smug
    RM "Operation \"Stakeout at the Bakeout\" starts now!"
    "Groan inducing puns aside, at this point I was just glad he didn't expect me to wear one of those pairs of glasses with the fake nose."
    scene black with fade
    pause 1
    scene Town with fade
    play music Peaceful
    "It didn't take us too long to get into town, there were plenty of buses running this time of day."
    if isEventCleared("MC005"):
        "I had definitely been to this part of town before. I recognized the sign of that konbini store with the pharmacy across the street. That, and the smell of fresh baked goods in the air left little doubt this was the spot."
        show RM neutral with dissolve
        RM "Is this the place?"
        MC "It has to be, it's the only bakery on this street, as far as I can tell."
        RM "I suppose the obvious sign that reads \"Kazomazumi's Bakery.\" gives it away."
    else:
        MC "Is that the place?"
        show RM neutral with dissolve
        RM "It has to be, it's the only bakery on Genki Street, as far as I can tell."
        RM "Not to mention the obvious sign that reads \"Kazomazumi's Bakery.\""
    MC "The obvious has never stopped your skepticism before."
    show RM angry
    RM "Just be quiet for a second. This is a stakeout after all."
    show RM doubt
    MC "Is that why we're hiding behind a pole?"
    RM "Well if you see an open alley with a good view of the front of the place, you let me know."
    show RM neutral
    MC "...Fair point."
    RM "Alright, the coast looks clear. I think we beat them to the punch. We'll be less likely to be spotted if we can get inside first. Let's head in!"
    scene Bakery Entrance
    show RM neutral
    with fade
    if not getFlag("VisitedBakery"):
        $setFlag("VisitedBakery")
    "We entered the bakery, a small but cozy establishment with a caramel-brown and cream-white decorative theme."
    "It only had half a dozen tables and a counter with stools for seating. There was another table seated besides us, but beyond that the only other person I could see was the counter girl."
    "The girl looked to be in her late twenties, early thirties maybe, mid-cut curly dark hazel hair, bright brown eyes, slightly chubby with big breasts, maybe an E-cup by my estimation, and I considered myself an expert on such estimates."
    if getHighestAffection() == "BE":
        "Then again, hanging out with Honoka so much had probably skewed my perspective on the matter."
    "The girl wore a caramel-brown and cream-white patterned baker outfit. We approached the counter to get our order in, hopefully before Alice and Akira walked in."
    Haruko "Hi, welcome to Kazomazumi Bakery! My name is Haruko, what can I get for you two?"
    MC "Yeah, hi! This is our first time here, what do you recommend?"
    Haruko "Well, today we have a special on pies and our cupcakes."
    show RM concerned-2
    RM "..."
    "I had to assume Daichi was nervous about his motives for visiting the establishment being perceived somehow. At this point I realized it was up to me to play the part to act naturally."
    MC "We'll have the cherry pie please."
    Haruko "Sure!"
    Haruko "So I'm guessing you two are students at Seichou Academy?"
    show RM sad:
        ease 1.5 xpos 0.45
        xzoom -1
        ease 1.5 xpos 0.55
        xzoom 1
        ease 1.5 xpos 0.45
        xzoom -1
        ease 1.5 xpos 0.55
        xzoom 1
        ease 0.75 xpos 0.5
    RM "!"
    MC "I guess the school outfit gave it away, huh."
    Haruko "Well, that and I couldn't help but notice you look like you had a growth with your hair."
    MC "Is it that obvious already?"
    show RM neutral at Position(xcenter=0.5, yalign=1.0), Transform(xzoom=1)
    Haruko "Maybe not to most people outside the island, but most people on the island are familiar with them. Many are even former students."
    Haruko "My mom had a growth thing as well, but the school wasn't around back then. Best I've got is that it had been there a while before I went there, over fifteen years ago."
    if isEventCleared("MC002") or getFlag("Meet_Tsubasa"):
        MC "Huh, didn't know the school was that old."
        Haruko "Oh, it's even older than that."
        Haruko "By the way, is Tsubasa-sensei still around?"
        MC "The biology teacher? He is, yeah."
        Haruko "Could you send the old geezer my regards? He was a great teacher!"
        MC "Will do."
        "Couldn't say I particularly agreed with that assessment, but I figured the old geezer might want to know someone remembered him."
        $setFlag("MC007_regards")
    else:
        MCT "Huh, didn't know the school was that old."
    Haruko "Anyways, here you guys go."
    scene Bakery with fade
    "We paid the cashier in advance before we left, we took the pie, thanked her, and planned our next move."
    MC "So where should we sit?"
    show RM doubt with dissolve
    RM "Hmm, we cannot risk them walking past us, that will give away our position."
    RM "Let's pick this table in the back corner. The lights are dim enough so at a distance they can't tell us apart from any other students."
    #scene cafe seats
    show RM neutral
    #with fade
    "We took our seats in the corner and did our best to keep our heads down. I tucked my hair into my collar so as to not give myself away. Though that probably wasn't necessary considering my bangs cover half my face anyway."
    MC "Hey, maybe you can ask the owners about this place?"
    show RM angry
    RM "Are you nuts!? I'm not going to show my hand right away! I'll keep coming as a regular, and calmly ask one or two questions, at the most, by the third visit."
    MC "Well, I'm just saying it wouldn't hu-"
    #*Door chime*
    RM "Zip it."
    scene Bakery Entrance
    show FMG neutral at Position(xcenter=0.25, yalign=1.0), Transform(xzoom=-1)
    show WG neutral at Position(xcenter=0.75, yalign=1.0)
    with fade
    "Both Akira and Alice entered the building. They were a few meters away from us but not close enough to not recognize us."
    Haruko "Oh hey! Is it just you two?"
    FMG "Yes ma'am, just me and my friend here."
    Haruko "Well, what would you two like?"
    FMG "Let's see... we'll have a box of cupcakes, please."
    WG "And I'll have coffee too. Cream and sugar."
    show FMG happy
    FMG "Oh, that sounds good. Put me down for that too."
    show WG surprised-2
    WG "Oh? You take your coffee sweet as well?"
    show FMG neutral
    FMG "Sure, so long as it's not that water downed sludge the school cafeteria serves."
    show WG happy
    WG "Haha!"
    show WG happy-2
    extend " Exactly. I couldn't have said it better."
    show WG neutral
    extend " Is it too much to ask for a nice cup of coffee to start the day off? With the budget the school has, you would think they could put some aside for an espresso machine."
    FMG "Wouldn't be surprised, their chefs aren't exactly winning any awards for niceness."
    WG "That is certainly the truth. I knew I couldn't be the only one that noticed that. It's nice to meet someone who gets it, Mizutani-san."
    show FMG happy
    FMG "Hehe, yeah. Hey, you can just call me Akira, no need for formalities."
    show WG neutral
    WG "Good to know. I have to agree. I've never cared for such conventions myself."
    scene Bakery
    show FMG happy at Position(xcenter=0.25, yalign=1.0), Transform(xzoom=-1)
    show WG happy at Position(xcenter=0.75, yalign=1.0)
    with fade
    #scene cafe seats
    WG "Now, where shall we take a seat?"
    show FMG neutral
    show WG neutral
    "They got their food and sat at the table behind us, which was basically the worst spot possible if we didn't want to get found out."
    "After they got seated, Daichi did a zipping motion around his lips and slumped farther into the table. I followed suit while we listened in while pretending to read the menus."
    show WG haughty
    WG "Alright Akira, so why did you invite me to come here with you?"
    show WG neutral-2
    show FMG sad-2
    FMG "I don't know. I just wanted to get away from campus,"
    show FMG neutral
    extend " seemed like a good opportunity since we were both craving something sweet."
    show FMG happy
    extend " Plus, I figured it couldn't hurt to get to know one of my classmates."
    FMG "We're all going to be stuck with each other for a while it seems, might as well try to get to know each other."
    FMG "So, like, are you from America?"
    show WG pondering
    WG "Well, I was born in Japan, and I've lived most of my life here, but to answer your question— sort of, in a way. My mother is from there and I did most of my schooling there."
    show WG neutral-2
    WG "I've lived in both countries off and on growing up."
    show FMG happy
    FMG "That's cool! You speak like a native, so I wasn't sure if you were from there or not."
    show WG happy
    WG "I'm glad you noticed that, rather than just my appearance."
    FMG "Heh, most people probably would think something similar about me, since I come from Okinawa."
    show FMG neutral
    show WG neutral-2
    WG "Okinawa huh? I've heard it's beautiful there. I hope to visit one day."
    FMG "You definitely should."
    FMG "So was there anything you'd like to ask me?"
    show WG pondering
    WG "Well, I guess if I wanted to get to know someone, I'd have to ask, where do you see yourself in five years?"
    FMG "I dunno."
    show WG surprised-2
    WG "..."
    WG "T-that's it? You don't know?"
    FMG "Well, how can any of us expect how the future will turn out? I like to think about the future as much as the next girl, but you gotta put in some room for the unknown."
    show WG worried
    WG "I can understand that rationale, but leaving so much to chance..."
    show WG pondering
    "Alice shook her head, flummoxed."
    show WG neutral-2
    WG "{i}Sigh{/i}, to each her own, I guess..."
    FMG "Now for this next question, I want you to be honest."
    show FMG happy
    FMG "Is it true that Americans deep fry soda and junk food?"
    show WG surprised-2
    WG "Wha-? Where did you hear that?"
    show FMG neutral
    FMG "The Internet."
    show WG doubt
    WG "...Just to be clear, I do not partake of that kind of food."
    show WG neutral
    extend " But yes, some places deep fry soda, Tronkos, chocolate bars..."
    "I heard Akira sipping her coffee as she processed the idea of deep-fried candy."
    FMG "Huh. No offense, but Americans seem kinda weird."
    show WG neutral
    WG "It is a large country and there are many... eccentrics on the fringes."
    show WG doubt
    extend " I've not partaken in any such... cuisine myself, if it can even be called that."
    show WG neutral-2
    FMG "Man, the coffee is a hell of a lot better here than the stuff at school."
    WG "Mmm, yes. Not my preferred choice, but it's one of the more palatable brands I've had since coming here."
    FMG "I take it you're used to the more fancy stuff?"
    WG "\"Fancy\" is often overrated. There isn't often too much of a difference in quality between a top tier brand at ten times the price than a typical premium quality product that manages to live up to the hype— at least when it comes to coffee."
    FMG "Hmm, good to know. I guess I should spring for an extra ten yen on a cup of coffee every now and then."
    show WG haughty
    WG "I'd highly recommend so."
    show WG neutral
    extend " Curious, if I may ask, why did you pick cupcakes?"
    show FMG sad
    "Akira put down the cupcake she was eating and looked down at it before answering."
    FMG "Growing up, whenever I was really down, my mom would always bake cupcakes. She would do it all by hand, and it made it that much more tasty."
    show WG surprised-2
    FMG "Even now, I still always go eat a cupcake when I'm sad."
    show FMG neutral
    extend " I do it to remind myself that whenever something bad happens, there will always be something to make life a little bit sweeter."
    show WG neutral-2
    WG "We all could use a pick-me-up every now and then. That's something I've learned sweets are definitely good for."
    FMG "For sure. {i}I guess it's my turn.{/i} Why did you agree to come join me?"
    show WG sad
    WG "I came to see..."
    show WG happy
    extend " If you were a fellow connoisseur of cupcakes."
    "It seemed like she wanted to say something else at first, but Akira didn't seem to notice."
    show FMG happy
    FMG "Heh, yeah I am."
    show FMG surprised-2
    FMG "Oh, it's almost 12:30, we should probably get going."
    show FMG neutral
    show WG surprised-2
    WG "Oh you're right."
    show WG neutral-2
    extend " Well, in that case, go on ahead. I'll handle the check."
    show FMG surprised
    FMG "What? But I-"
    show WG happy
    WG "Please, this is nothing to me. Consider it a show of my enjoyment of this get-together."
    show FMG happy
    FMG "All right, that's cool. I hope we can do this again."
    WG "As do I. I'll see you later, Akira."
    FMG "You too. Later."
    hide FMG with dissolve
    show WG worried
    WG "{i}Sigh{/i}. You had a potential sale there Nikumaru, until that personal matter cropped up..."
    show WG pondering
    WG "No way to foresee that though. Next time, keep the mood light."
    "After talking to herself, she paid the bill and left."
    hide WG with dissolve
    show RM angry with dissolve
    play music DayByDay
    RM "Wait... That's it? We've been here for over 20 minutes listening to girl talk, and they didn't even mention a single thing about this Kazomazumi person, let alone this stupid bakery!?"
    MC "I can't believe {i}I'm{/i} the one to say this, but would you keep your voice down? {w}I mean, look at where we are."
    MC "Not to say \"I told you so\", but maybe it really was all just a coincidence."
    show RM sad
    RM "B-But the timing was too perfect! How could-"
    UNKNOWN "Excuse me, but are you students at that academy?"
    MC "Um yes ma'am, we-"
    MCT "HOLY MILK JUGS!"
    "From the back of the store I saw a figure emerge that had a chest beyond anything I'd ever seen before. If I had to guess a bra size, I'd say a big triple P— at LEAST!"
    "Craning my neck slightly above chest height I could now see the woman, who looked to be middle aged, possibly older, I couldn't tell if it was longevity, good genes, or one hell of a skincare routine."
    "I notice her chestnut hair formed in a bun, dark brown eyes, a very voluptuous figure with a bit of a belly. She was dressed about the same as the cashier, but with a different fit to it, for obvious reasons."
    "There was no telling how old she actually was given the gravity defying perkiness her breasts possessed that put even the cashier lady's to shame."
    Haruko "Mom! Quit bugging the customers!"
    Chie "Oh hush dear, I just wanted to see how fellow growers were handling things."
    MCT "Fellow growers? Does that mean..."
    MC "You must be Chie Kazomazumi-san."
    Chie "Why yes I am. I'm surprised you'd know. I didn't realize students were aware of the precedent of my particular case."
    Chie "And can I say you two look so cute, especially you, mister shaggy hair. I saw all that hair stuffed down your shirt. Is that your factor? You don't need to be ashamed of it."
    MC "Oh no, it's just... a pain to deal with you know? A hat or hair gel can only do so much."
    Chie "That is fair enough, sweetie. Lord knows I had trouble dealing with my chest when I was your age, but I managed to make do."
    show RM neutral:
        ease 2 xpos 0.01
    "While I was talking to her, Daichi was trying to stealthily leave out the front door... Too bad everyone could see him. I felt like it was better just to ask and get it over with."
    show RM concerned
    MC "Look, my roommate is too shy to ask, but are you really the first person to have a growth factor?"
    show RM angry at Transform(xzoom=-1):
        ease 0.5 xpos 0.3
    "Upon hearing me speak, he spun around as if to try and stop me, unfortunately for him he was cut off by Chie."
    show RM doubt
    Chie "Well, I am the first person to actually be recognized as having tested positive for a growth factor..."
    Chie "...But I'm sure there were others that had growth factors long before I came around. Sorry, but I can't really tell you how it started."
    show RM sad
    Chie "The school wasn't even finished when I got here. At the time it was the first major building in that part of the island after they closed the rock quarry."
    "Daichi's reaction was obviously disappointed that Chie hadn't offered anything particularly insightful related to the nature of the growths from her experience."
    show RM smug
    "But a flicker of intrigue from his eyes made me suspect he had somehow managed to glean something from what she said."
    show RM neutral
    Chie "But hey, it's not like everyone knows about that! Thanks for asking."
    MC "Well, thanks for the pie, we'll be sure to come back."
    Chie "Thanks for coming! You'll always be welcome here!"
    Haruko "Thanks for coming. Please come again!"
    scene Town
    show RM neutral
    with fade
    "With that we left the store, and once we were out of sight of the windows I turned to see Daichi looking like he's trying to take things in stride."
    RM "Well, I am disappointed this wasn't the big break I've been searching for, but it gives me an idea of how far this may actually go. Not to mention that last comment she made, about the rock quarry..."
    show RM happy
    RM "Plus, I got some pretty great pie out of it."
    MC "See? It wasn't a total bust!"
    show RM neutral
    RM "...Really now?"
    MC "The pun was unintentional."
    show RM doubt
    RM "That seems like too much of a coincidence to me..."
    MCT "Ugh, this is never going to end."
    jump daymenu

label MC008:
    if not getFlag("Meet_Tsubasa"):
        $setFlag("Meet_Tsubasa")
    Tsubasa "-that's tomorrow. As for today, Carbohydrates."
    pause .25
    MCT "Mn..."
    play music HigherEdu
    scene ClassroomAlt
    show Tsubasa neutral
    with fade
    MCT "Did I... actually fall asleep?"
    "Sitting up in a way that wouldn't draw a huge measure of attention, I looked up at the board,
    then compared my notes."
    MC "Alright. Still up to speed. Sweet."
    Tsubasa "Carbohydrates are aldehyde or ketone compounds with multiple hydroxyl groups.
    They represent a group of substances such as sugars, starches, gums and celluloses, and
    their common attribute is that they contain only the..."
    MCT "..."
    MCT "Yeah. Not gonna be a biologist anytime soon."
    "At the front, Tsubasa-sensei started noting down different terms as he spoke."
    MCT "Sugars."
    MCT "Starches."
    MCT "Gums..."
    MCT "I could go for a stick of gum right now."
    MCT "Maybe one of the cinnamon ones. Or a mint. Always seems to make the day a little   more interesting when I have a flavor to focus on."
    "I turned back up to the board."
    MCT "Cellulose..."
    MCT "What the hell is-"
    MCT "Oh, dammit."
    "I sighed. Foiled by chewing gum."
    Tsubasa "Carbohydrates, or carbs, serve as energy stores, fuels, and metabolic intermediates."
    Tsubasa "They're vital at every stage of life, being a primary source of energy for our body, acting as a fuel to our brains, kidneys, central nervous system and heart muscles."
    Tsubasa "Their next function is they form the..."
    MCT "... part of the structural framework of DNA and RNA."
    Tsubasa "Deoxyribonucleic acid and ribonucleic acid are perhaps the most essential molecules in cell biology, responsible for the storage and reading of genetic information underpinning all life."
    "I rubbed my head."
    "Tsubasa-sensei was... definitely skilled in what he knew."
    "But, his way of delivering that information was..." 
    "Well, watching food spin in a microwave was a decent step more exciting."
    MCT "Tashi always sounds pissed, but he has a decent tone of passion all the same."
    MCT "I bet it doesn't help that he's probably said the same phrases and repeated the same lectures over and over again, year after year. The guy's probably bored himself."
    if isEventCleared("MC002"):
        MCT "Hm... wonder how long he's been teaching." 
        "Didn't Takamura-sensei mention he's been a teacher here for a few decades? How many students fall asleep at his lectures? Does he even care anymore?"
        "I looked at Daichi, who was lying down at his desk and having a nap."
        MCT "No. Probably not."
    if isEventCleared("MC002") or isEventCleared("MC006") or isEventCleared("FMG018"):
        "Well, at least this semester had a few classes that were interesting enough."
    if isEventCleared("MC006"):
        "Like that one time when Tashi-sensei took us for the handball game with Naoki-sensei and Hageshi-sensei."
        "It was... a little awkward. But hey, at least we had a good time."
    if isEventCleared("FMG018"):
        if getflag ("FMG018_AE_CookingPartner"):
            "Plus, when Tashi-sensei took us for that cooking lesson with Takamura-sensei. Cooking with Akira and Shiori was... interesting at least."
        if getflag ("FMG018_GTS_CookingPartner"):
            "Plus, when Tashi-sensei took us for that cooking lesson with Takamura-sensei. Cooking with Akira and Naomi was fun."
        if getflag ("FMG018_BE_CookingPartner"):
            "Plus, when Tashi-sensei took us for that cooking lesson with Takamura-sensei. Cooking with Akira and Honoka was... interesting at least. Going full blown French cuisine in it."
    if isEventCleared("MC002") or getFlag("Meet_Hageshi"):
        "And math with Hageshi-sensei. He's not bad."
        MCT "I mean, I do okay. But, I sure hear enough people complain about it."
    "I took another glance at the board and started writing down what Sensei had written."
    MCT "Structural elements in the cell walls of bacteria and plants."
    MCT "Linked to many proteins and lipids."
    MCT "Key role in cell to cell recognition process."
    "I reached up and adjusted my bangs a bit, then set my head in one hand, still writing with the other."
    hide Tsubasa with dissolve
    "I wanted cover in case my bored eyes happened to shut."
    if isEventCleared("AE020"):
        show AE neutral with dissolve
        "Right in front of me, Shiori, as always, was fully focused on the class, thoroughly noting down everything that came out of Tsubasa-sensei's mouth." 
        if lockRoute("AE") and if not isEventCleared("AE025"):
            MCT "Agh... just hope she says yes."
        hide AE with dissolve
    elif isEventCleared("BE020"):
        show BE happy with dissolve
        "I looked over to the left side of the classroom and focused my sight on my childhood friend, who seemed to be busy scribbling something on her notebook." 
        MCT "Should I say \"girlfriend\"?"
        MCT "The date. Her dress. Just... mngh. Perfect."
        hide BE with dissolve
    elif isEventCleared("PRG020"):
        show PRG worried with dissolve
        "I glanced up and forward a bit, looking over at Aida jotting down notes quickly in front of me, her legs crossed politely."
        if getflag ("PRG020_c1_1"):
            MCT "I wonder if she's thinking about our kiss."
            MCT "Still... even now, I can't believe it."
            "Aida kissed me."
            pause .5
            "Or... {w}did I kiss her?"
            "Either way, it still seemed so farfetched to me."
            MCT "Like, Aida of all girls."
            "I looked up at her once more, and watched her hand move across the page as she wrote."
            hide PRG with dissolve
        elif getflag ("PRG020_c1_2"):
            "I thought about my time on the roof with her."     
            "I hoped she wasn't still mad about what I'd told Alice."
            "In retrospect... yeah, not a good call."
            MCT "She did hold my hand, though. So... that's a good sign."
            hide PRG with dissolve
    elif isEventCleared("GTS020"):
        show GTS neutral-2 with dissolve
        "I turned a little in my seat."
        "Naomi sat directly behind me, writing notes diligently."
        "As if sensing my eyes, she looked up and smiled a small, delicate smile, then glanced back down."
        if getFlag("GTS020_c1_2"):
            "I took my leave and looked back to my notes."
            MCT "Ahh... I can't wait."
        hide GTS with dissolve
    elif isEventCleared("FMG020"):
        show FMG neutral with dissolve
        "I looked to the middle of the room and smiled."
        if getFlag("FMG020_c1_1"):
            MCT "Akira is... kind of adorable when she's nervous."
            MCT "I should ask her on dates more often. Get a look at the nervous nelly herself."
        elif getFlag("FMG020_c1_2"):
            MCT "Yeah... blew that one hardcore."
            MCT "Always next time, I guess."
        hide FMG with dissolve
    elif isEventCleared("WG020"):
        show WG neutral with dissolve
        "Alice sat nearby, her form filling out her seat wonderfully."
        MCT "Could really just... not pay attention. There's a lot more interesting things that aren't on the board."
        hide WG with dissolve
    elif isEventCleared("WG027"):
        show WG neutral with dissolve
        "I looked to Alice, seated close by in the middle."
        MCT "... Hope our date goes well."
        MCT "If the asking out process is any indicator, then I'll be a total nervous wreck by the time the day actually comes."
        hide WG with dissolve
    else:
        show Tsubasa neutral with dissolve
        "I kept my eyes forward, watching Tsubasa-sensei erase the notes on the board, only to quickly swap them out for new ones."
        MCT "For such a slow, precise dude, the man races through information."
        "I flipped to a new page and started in on the next few lines."
        hide Tsubasa with dissolve
    play music BE
    UNKNOWN "... -Kei-chan, please?"
    "I looked up and to my left."
    "Honoka was leaned over, and whispering something to Akira, before pressing a piece of paper into Akira's palm."
    if getHighestAffection() == ("BE"):
        "I let my gaze linger on Honoka's chest."
        MCT "Dude... those things have gotten huge..."
    else:
        "I gazed across the room, looking mainly at Honoka's swollen chest."
        MCT "I never notice in the moment... but God, those things have gotten bigger since we first caught up."
        MCT "She was big then, too. Man."
    "Akira turned and glanced back at Alice, whispering something to her."
    "Alice sighed, taking the paper from Akira."
    "She glanced over to me, then underhanded the paper over and right onto my desk, landing right in the middle of my notebook."
    MCT "... Ooookay."
    "I unfolded the paper and glanced at the corner, where there was something written, going down vertically."
    MCT "... What the... hell?"
    MCT "uohs... naoni.... hcat... ihsataw...?"
    MCT "The hell is this?"
    MCT "It's... romaji... I think?"
    show BE neutral with dissolve
    "I looked up to Honoka, putting one hand at an angle, in an \"explain\" fashion."
    "But, Honoka was busy taking notes, her paper pushed way out so she could see over her chest pillows."
    show BE wink
    "She glanced over after a moment, and grinned. She gestured with both arms, moving them back in toward herself, her chest bouncing rhythmically up and down."
    MCT "Open the mental channel, Honoka. I've got nothing here."
    "I looked forward, where Shiori was glaring over at Honoka."
    MCT "Am I supposed to just guess? I don't know, pig latin?"
    MCT "Actually... is it a code? Like a cipher or something?"
    MCT "Would Honoka even know how to-"
    pause .5
    MCT "Ohh... yeah, she would."
    show BE happy
    "I looked up at her and smiled cheekily."
    MCT "Been awhile."
    hide BE with dissolve
    "I jotted the letters down on a spare sheet of notebook paper, then swapped them around."
    MCT "Got it."
    $eventname = "our code"
    $save_name = "our code"
    MCT "watashitachinoanshou."
    MCT "Our secret code."
    "I went back to Honoka's paper."
    MCT "iesnes-iami. Perfect."
    "I folded the paper back up and went to hand it to Alice."
    "Alice simply sighed."
    "She held her hand out and I passed it to her."
    "The note went forward to Akira, then back to Honoka."
    "Honoka unfolded it, glanced down, then looked back over, beaming."
    $setAffection("BE", 1)
    "I grinned, thinking far back to the first time we'd done this."
    "We'd had the most boring teacher ever in third grade. So to pass the time, Honoka and I took up writing notes to each other."
    "Of course, we eventually were caught... {w}well, Honoka was."
    "Our teacher, Imai-sensei, had read Honoka's note out in front of class, embarrassing the hell out of her in class."
    "Honoka and I met up after school then, and she was so frustrated, she wanted to find a way to really get back at our teacher."
    "So, we went back to her house, and wrote up a fake language. Totally the idea that two rebellious eight year olds would cook up. Basically, writing out our notes in reverse, so if a teacher ever got ahold of it, they'd have no idea what we were saying."
    "This became our game in school for the rest of that school year."
    MCT "... Never got caught after that, but hey, coding was a lot of fun."
    "Waiting for a reply, I looked up to Tsubasa-sensei."
    Tsubasa "-ter they are absorbed, they therefore will..."
    MCT "Good lord..."
    "I caught up on the board, and was nearly at the end, when a folded piece of paper flapped down onto my desk again."
    show WG stern with dissolve
    "I looked to Alice, who gave me a sort of scowl before facing front again."
    hide WG with dissolve
    BECell "<hell yeah! Imai's classes were just as boring!>"
    MCT "Jeez... almost forgot that. So boring to the point that Honoka and I had to take lessons from Honoka's dad just to learn romaji."
    MCT "Of course, him teaching us led us to create our little game, so hey... who's fault is that?"
    MCT "I think Fujio-san taught English, if I remember properly."
    MCCell "<how is your dad?>"
    MCT "I... kind of remember all of the details? Pretty sure her dad got a job offer and he, Honoka, and Maegami-san, her mom moved away to the Kagoshima prefecture."
    play music Peaceful
    "I folded the note back up, and passed it to Alice, who while taking it, rolled her eyes."
    if getHighestAffection() == ("WG"):
        "By this point I could tell I was exhausting her patience, but it's not like we do this all the time. Hopefully it's not too big a deal."
    "I couldn't quite explain it, but I suddenly had the feeling of eyes on me, and glanced about."
    "No one else was really paying attention to us, that I could see anyhow."
    "I sighed lightly."
    "Honoka and I had tried to keep contact for a while. Sending messages back and forth and such. But, as a lot of long distance friendships do, we had lost touch."
    MCT "I still have that postcard from Kagoshima City that she sent me, too. Got that giant volcano in the background."
    "I glanced back over my shoulder."
    show GTS pondering with dissolve
    "Naomi watched the note move from Alice to Akira, then over to Honoka."
    GTS "{size=+6}Pray forgive me for prying; what is that note for, Hotsure-san?{/size}"
    MC "It's a game Honoka and I used to play in grade school years ago."
    show GTS neutral
    GTS "{size=+6}Oh? You two knew each other prior to coming here?{/size}"
    MC "We did. I was surprised to see her, too."
    GTS "{size=+6}Indeed. That must have been quite the happy coincidence.{/size}"
    show Tsubasa neutral at Position(xcenter=0.8, yalign=1.0) with easeinright
    Tsubasa "{i}Ahem.{/i}"
    show GTS surprised
    "Both of us looked back down at our notes and continued writing."
    if isEventCleared("GTS026"):
        "Out of the corner of my eye, I caught her staring at my back for a curious moment before she continued."
    GTS "{size=+4}...Apologies, Hotsure-san. I did not imagine my voice should carry so much...{/size}"
    if isEventCleared("GTS004"):
        MCT "So it's not just me..."
    MC "No worries."
    hide GTS
    hide Tsubasa
    with dissolve
    "As I copied down more terms from the board, my mind wandered off of bread and carbs and more on how I now had to look up slightly to talk to Naomi, instead of straight on."
    if isEventCleared("MC007") or isEventCleared("RM004"):
        MCT "I wonder... those \"giants\" dorms. Will... will Yamazaki-san be sent there?"
    "The paper came back, smack onto my notes."
    MCT "Okay... this is a long one."
    BECell "<good! still teaching. how are Ryuta-san and Himari-san?>"
    "I moved over a line and jotted in a response."
    MCCell "<dad received a promotion and is a manager now, mom still writes her romance novels>"
    "The note went back to Alice, and I looked forward again."
    "But, I couldn't focus. All I could think of was all the fun I'd had with Honoka when we were kids."
    "We'd ran around Shibuya with Tomo like it was our own personal playground. The parks had been our yards, and the subway tunnels had been our own giant game of hide and seek, and the arcades were our amusement parks."
    MCT "I still remember when we got lost in the Shibuya tunnels."
    MCT "Mom was pissed."
    MCT "But, as I kept telling her, it's not my fault that Tokyo's metro lines are ungodly hard to traverse."
    "I smiled to myself, as the note came back to me."
    "I looked up. Alice looked... noticeably uncomfortable."
    "I gave her a soft, thankful smile, glad that she was helping us have some fun."
    "Unfolding the note, there was a new writing at the bottom of the paper. Fully uncoded and written in romaji."
    "{i}What is this???{/i}"
    "I glanced up."
    "Akira was looking back at me. Seeing me notice her, she gestured with one hand, her head cocked."
    "I smiled at her and looked down to my note."
    "Right next to her question, I drew a small emoji of a man shrugging, then looked to Honoka's code."
    BECell "<nice! and how's Tomo-chan doing?>"
    BECell "<she's still not leaving her room, right?>"
    if not isEventCleared("MC003") or not isEventCleared("MC005"):
        MCCell "<unfortunately not. her roommate has been trying to get her out though>"
        MCCell "<speaking of, how is your roommate?>"
    if isEventCleared("MC003") or isEventCleared("MC005"):
        MCCell "<unfortunately not, but we recently spent some time together>"
        MCCell "<her roommate has been trying to get her moving>"
        MCCell "<speaking of, how's your roommate?>"
    "I folded the paper."
    MC "Alice..."
    show WG angry with dissolve
    "By this point Alice was expecting it, at first not even looking at me before finally extending her hand out just enough to avoid detection, though none too amused about it." 
    MC "Thanks."
    "Alice didn't respond, and just passed it on to Akira."
    hide WG with dissolve
    show FMG happy with dissolve
    "Upon getting the paper back, Akira opened the paper."
    FMG "{i}Hngh!{/i}"
    show Tsubasa neutral at Position(xcenter=0.8, yalign=1.0) with easeinright
    show FMG surprised
    Tsubasa "Is there a problem, Mizutani-san?"
    "Akira played her part perfectly, and put the folded paper on her desk, nudging it under her notebook with a finger."
    FMG "Sorry, Sensei. Allergies."
    Tsubasa "Yes... of course. That time of year, isn't it?"
    hide FMG
    hide Tsubasa
    with dissolve
    "Tsubasa-sensei turned back around to the board, and Akira passed the note off to Honoka."
    "Seeing him turn around, I saw a good deal of new material since I'd last checked in."
    menu:
        "Pay attention":
            $setFlag("MC008_PayAttention")
            "I did my best to shut out the surroundings and focus only on the board and Tsubasa-sensei."
            "I needed the decent grade."
        "Take it easy":
            $setFlag("MC008_TakeItEasy")
            "I kept writing down the notes, but didn't really listen in too hard."
            MCT "What was that... in the Shibuya tunnels, what was that game called that Honoka and I used to play?"
            MCT "Not like a video game. It was more like tag or hide and seek or something..."
            "After a few minutes of this, I glanced back at the board, only to see a brand new wall of text."
            MCT "... Dammit."
    "Back came my new friend, the paper."
    BECell "<we should think about resurrecting TomoHono>"
    BECell "<not much to say, my roommate is weird>"
    BECell "<PS. No dozing off!>"
    MCT "Good ol' TomoHono. Honoka and Tomo's weird gal-pal alliance."
    "I started jotting down my response."
    MCT "Pretty sure her roommate isn't that crazy."
    "I looked back toward Daichi, who by the look of his eyelids, was about to lose a long fought battle."
    MCT "No. Not even close."
    MCCell "<oh yeah, definitely! weird?>"
    MCCell "<don't blame me. not my fault that Tsubasa's lectures are so boring>"
    "I folded it and handed it back to Alice."
    show WG surprised with dissolve
    WG "..."
    WG "Hotsure-san? What exactly is this?"
    MC "It's just a stupid game that Honoka and I play to pass the time."
    "Alice swiped the note from my hand and unfolded it."
    WG "I've seen this sort of writing back during my time in America."
    WG "Though... it didn't look like gibberish."
    show WG stern
    "Alice sighed, tossing the note back at me."
    WG "You can play your game, but I'll have no part in it."
    MCT "Agh, come on, Alice."
    "I sighed. I knew I wouldn't get anywhere with her, and an argument wasn't worth it."
    hide WG with dissolve
    "I glanced past her, where Honoka was looking expectantly at me."
    "I nodded to Alice and made an X with my hands."
    "I took the paper and unfolded it, then balled it up into the smoothest sphere I could manage, and held it up."
    show BE surprised-2 with dissolve
    if checkSkill("Athletics", ">=", 5):
        play music Busy
        "I hurled the ball straight over Alice... and right to Honoka."
        "She got it right in her hands, but the momentum of the toss carried the ball right out of her hands."
        "Honoka lunged for it, knowing the noise of paper hitting the floor would alert Tsubasa-sensei."
        play music Peaceful
        "{i}Brrrrrch-IIIIT!!{/i}"
        "Everyone in the class jolted as Honoka's chest bumped her desk, knocking her desk forward, and popping the paper right onto her desk."
        show BE surprised-2 at altMove(0.5, 0.25)
        show Tsubasa neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    else:
        "I hurled the ball straight over Alice... and totally biffed it."
        "The ball curved to the side, and nailed Daichi right in the head."
        stop music
        hide BE
        show RM angry with vpunch
        RM "YOU'LL NEVER TAKE ME ALIVE!!"
        "Daichi jolted up, knocking his desk over, the note springing right onto Honoka's desk."
        hide RM with None
        show BE surprised at Position(xcenter=0.15, yalign=1.0)
        show PRG surprised at Position(xcenter=0.26, yalign=1.0)
        show FMG surprised at Position(xcenter=0.40, yalign=1.0) behind PRG
        show WG surprised at Position(xcenter=0.60, yalign=1.0)
        show AE surprised at Position(xcenter=0.75, yalign=1.0)
        show GTS surprised at Position(xcenter=0.90, yalign=1.0) behind AE
        with vpunch
        "Everyone in the class turned around, looking right at Daichi."
        pause .5
        hide BE
        hide PRG
        hide FMG
        hide WG
        hide AE
        hide GTS
        show RM angry at Position(xcenter=0.25, yalign=1.0)
        show Tsubasa neutral at Position(xcenter=0.75, yalign=1.0)
        with dissolve
        Tsubasa "... Utagashi-san, may I ask what exactly the problem is?"
        show RM concerned
        RM "I-I have a cramp!"
        Tsubasa "And that requires an outburst delivered at maximum volume? And, I can't recall a mild cramp having ever taken someone's life."
        show RM smug
        RM "That's what I always say when I have a cramp, Sensei."
        "Tsubasa-sensei, brushing aside the interruption, glanced to the floor by Honoka's desk."
        hide RM
        show BE surprised-2 at Position(xcenter=0.25, yalign=1.0)
        with dissolve
    Tsubasa "What have we here, Inoue-san?"
    show BE surprised
    BE "Ah... I-I..."
    MCT "Shit..."
    MCT "I had to go say his classes are boring. Now Honoka's gonna get a real ass chewing."
    MCT "It's just backwards text. It isn't that hard..."
    Tsubasa "Now, let's see."
    Tsubasa "And... {w}hmp..."
    Tsubasa "This is..."
    hide BE
    show PRG worried at Position(xcenter=0.25, yalign=1.0)
    with dissolve
    Tsubasa "Hmph. Kodama-san."
    PRG "Y-Yes, Sensei?"
    Tsubasa "Read this. Aloud, please. So we all can hear."
    "He handed Aida our note."
    show PRG unique
    PRG "Um..."
    PRG "Uuu... oh... s-snoan... ichcat?"
    "I glanced around through my shield of hair. Everyone, save for Honoka, looked more than a touch confused."
    Tsubasa "That's enough, Kodama-san. Thank you."
    hide PRG
    show BE neutral at Position(xcenter=0.25, yalign=1.0)
    with dissolve
    Tsubasa "I merely wished to ensure that my eyes weren't failing me yet. Though, it seems both of my eyes and my glasses are in good working order."
    "Tsubasa-sensei took the note and glanced at it once more."
    play music HigherEdu
    Tsubasa "\"What is this?\" {w}My thoughts exactly."
    "He tossed the note into the trash and stepped back to the board."
    Tsubasa "Now... I was... here, yes."
    "Across the room, Honoka shot me a knowing grin."
    show BE wink
    MCT "Undefeated."
    hide BE with dissolve
    show Tsubasa neutral at altMove(0.5, 0.5)
    Tsubasa "Afterwhich, the-"
    "The bell chimed overhead."
    Tsubasa "Mgh? Yes, well. Prepare for a test on this material coming up."
    if getFlag("MC008_PayAttention"):
        "I checked my notes once before sliding my notebook away. Those would come in handy."
        $setSkill("Academics", 1)
    else:
        "I looked down at my open, half-finished page of notes."
        MCT "Agh. Well, I'll have to get them from someone else."
        MCT "Maybe Daichi...?"
        MCT "Ah... no. He's been napping for at least half the time."
        if getHighestAffection() == ("AE"):
            MCT "Shiori will almost certainly have everything I'll need. Though... I'll have to sit through a small lecture from her on not disrupting classes."
            if lockroute("AE") and not isEventCleared("AE025"):
                MCT "... If she'll actually talk to me."
        elif getHighestAffection() == ("GTS"):
            MCT "Naomi probably took good  notes... if I wasn't distracting her."
        elif getHighestAffection() == ("WG"):
            MCT "..."
            MCT "I doubt Alice will hand over her notes willingly. Not after today."
            MCT "Well, worth a try anyway."
        elif getHighestAffection() == ("PRG"):
            MCT "I'm sure Aida would be willing to lend me a hand."
        elif getHighestAffection() == ("BE"):
            MCT "Did... Honoka even write anything?"
            MCT "I... well, I'll ask her later."
        elif getHighestAffection() == ("FMG"):
            MCT "Well... Akira probably didn't get the whole board down... if half of it. But hey, worth a shot."
    "As we packed, a ringing came from the front of the room."
    Tsubasa "Hm?"
    "Tsubasa-sensei went to his desk and fished through his bag."
    Tsubasa "Hahhh..."
    Tsubasa "Impeccable timing..."  
    "As I stood up and swung my bag over my shoulder, Shiori didn't move from her desk, still writing away."     
    if getFlag("MC007_regards") and not getFlag("RM004_RegardsPassed"):
        $setFlag("MC008_RegardsPassed")
        MCT "Oh! Shoot, that's right. I was supposed to give Tsubasa-sensei regards from the bakery owner's daughter."
        MCT "Mmn... God, just thinking back to that is wild enough."
        MCT "Those were the biggest boobs I've ever seen. Bar none."
        MCT "Wonder if Honoka's boobs will get to that point. Though, I doubt she'd mind even if she did. The extra baggage has never gotten to her anyway."
        MCT "She's getting close already, and we're not even through the first semester yet."
        "I went forward, down the aisle and to the front of the room."
        Tsubasa "Yes, I did."
        pause .5
        Tsubasa "I have it with me. I've hung one up already, and I'll be pinning another up later today."
        pause .75
        Tsubasa "Yes, Dear. I know it's important."
        if getFlag(Meet_Chiyo):
            MCT "Talking to his wife, most likely. Chiyo-san, if I remember right."
        "Tsubasa-sensei glanced up, rubbing his forehead."
        Tsubasa "Yes, I will. I have a student waiting for me, Dear. I'll see you tonight."
        "He hung up the phone promptly."
        Tsubasa "Yes, Hotsure-san?"
        MC "I'm sorry for interrupting, Sensei. I can wait if you need to finish something."
        Tsubasa "Nothing that can't wait, Hotsure-san. What can I do?"
        MC "I just wanted to tell you that I ran into an old student of yours. A girl named Haruko. She works at a bakery in town. She asked me to give you her best."
        Tsubasa "Kazomazumi Bakery?"
        MC "Yes, Sensei."
        Tsubasa "Ah, of course. The daughter of Chie Kazomazumi, the first diagnosed factor holder. It has been some time."
        show AE neutral at Position(xcenter=0.25, yalign=1.0) with easeinleft
        "As Tsubasa-sensei and I were talking, Shiori stood up from her desk and gently tapped my shoulder."
        show AE neutral
        AE "For you, Hotsure-san."
        MC "Ah... thank you?"
        show AE neutral
        "She nodded and pressed a folded sheet of paper into my palm, then turned and left."
        show AE neutral at Transform(xzoom=-1)
        pause 0.1
        hide AE with easeoutleft
        Tsubasa "As I was saying, when Haruko was enrolled, we were still studying the correlation between factors possibly being inherited genetically."
        Tsubasa "Through my own research, I learned that... well, it's a complete roll of the dice. Sometimes, nothing will happen. Another time, they might have an exaggerated body shape while not exactly having a factor directly."
        Tsubasa "Other times, they might have an entirely different factor. And occasionally, they might even share a factor with their parent, rare as it is."
        Tsubasa "Haruko doesn't actually have a growth factor herself. Rather, her shape is the result of genes passed from her mother, most likely."
        Tsubasa "She was at the academy solely for her mother's status. The academy wanted to monitor her, to see if there was a link between mother and daughter. Of course, that resulted in nothing."
        MC "I see. That's interesting, Sensei."
        Tsubasa "Yes. We know much compared to then. But, compared to what we could theoretically know about the factors, we... have precious little."
        Tsubasa "However, I'm holding you up. Enjoy your day, Hotsure-san."
        MC "You as well, Sensei. Thank you."
        scene Hallway with fade
    else:
        scene Hallway with fade
        "I left the room, Tsubasa-sensei listening carefully to his phone call."
        AE "Hotsure-san."
        show AE neutral with dissolve
        MC "Oh, hello Matsumoto-san."
        AE "For you."
        "Shiori handed me a note, folded neatly into quarters."
        MC "What is...?"
        show AE neutral
        AE "I think you'd best read it with Inoue-san."
        show AE neutral
        AE "Have a good day."
        "Shiori stepped curtly around me and down the hall, as I glanced down at the paper."
        hide AE with dissolve
        Tsubasa "- it with me. I've hung one up already."
        "Tsubasa-sensei's words echoed down the hall, and I turned toward where Shiori had gone."
    show BE happy with dissolve
    "As I went down the hall, I spotted Honoka off to one side, grinning at me in only the way she could."
    MC "Hngh. Old guy looked more worried about his glasses than the note."
    BE "I mean, it's gibberish, right?"
    MC "Hey, not to us."
    BE "I'm... I'm just glad you remembered, Kei-chan. It had been so long, I wasn't sure if you'd still have it."
    MC "Now now, don't doubt my ability to zone out in class."

    if not isEventCleared("BE020") and checkAffection("BE", "<=", 6):
        $setAffection("BE", 1)
        MCT "Mm... this is familiar."
        MCT "We've been apart for so long. It... it feels like I have my old best friend back again."
    BE "Whatcha got there? I didn't pass another one over."
    MC "Oh, it's from Matsumoto-san."
    MC "She passed it to me on my way out. Weird, right?"
    BE "Totally weird."
    BE "Crack it open."
    "Honoka peered at it as I unfolded it, holding it before us both."
    MC "usedemad aw nakuok ot-on ed uhc uoyguj."
    BE "Exchanging notes in class is forbidden."
    BE "How in the heck did she-"
    MC "I have no idea."
    "The two of us just looked at each other, then down the hall toward where Shiori had gone."
    jump daymenu

label MC009:
    scene Dorm Interior with fade
    play music MC
    pause .5
    "..."
    "On my desk, my laptop screen shone in my eyes as the cursor blinked steadily."
    MCT "I've never considered myself anything close to a prolific writer, and my time in Tashi-sensei's class has been slowly proving that to me."
    "I usually spent more time watching that little cursor blink than anything, broken up by occasional clicks, trying to start a sentence that actually made sense, which was very quickly deleted."
    "Idly, I clicked open a new tab and typed in the search bar."
    "<What is that little blinking line for typing called?>"
    pause .5
    MCT "..."
    MCT "Oh, a caret."
    MCT "Cool."
    "I closed out my new tab and went back to staring at my nearly blank paper on... well, it was supposed to be on the Kofun period, according to Tashi-sensei."
    "At the moment, however, it bore more resemblance to some general facts put into rough sentences and some odds and ends thoughts."
    "I had probably four or five tabs open to various sites on the topic, most of which looked like they'd been created around 2004."
    MCT "Okay. Let's actually make some headway."
    "I forced myself to click on one and scrolled a bit."
    MCT "Hm... 300-538 AD. Okay."
    "I went back to my word doc and typed in some Keisuke Hotsure shorthand."
    MCT "And... the Kofun period was when politics essentially began in Japan. Cool... {w}I think."
    MCT "... Wait, what?"
    MCT "'The name of the Kofun period originates from keyhole shaped burial mounds saved especially for the ruling class?'"
    MCT "What the hell?"
    "I typed it in regardless and rubbed my eyes under my front hair fringe."
    if isEventCleared("MC007"):
        MCT "Could Tashi-sensei just... not give us papers for once? Makes my damn brain hurt..."
        MCT "We legit {i}just{/i} wrote about the Yayoi period. Like... maybe show a movie in class or something? On one of the TVs from the 90's."
        MCT "If only. School was so much simpler way back when."
    "This was all so much. Like, I didn't mind history, but this all seemed to bleed together so much. It was hard to keep it all straight."
    if isEventCleared("MC008"):
        "I scratched at my collar and twisted, my gaze falling on a pile of books at the end of my desk."
        MCT "And I still have to study Biology yet, too. That carbohydrates exam can't be over with soon enough."
    "In all likelihood, though, I was beating myself up a bit too much. I actually did have a fairly sizable amount written thus far, and I had enough notes for likely three to four more pages that I could hopefully pound out before studying."
    "I rubbed my ear a bit as I got that weird high pitch ear ring thing, and got up from my chair, feeling my shirt stick to my back a little as I got up."
    play music MCGuitar
    "I peeled the fabric away from me and walked into the kitchen, rummaging through a cabinet for something to nibble on."
    "..."
    MCT "... Is that?"
    "I stood still and listened closely."
    MCT "A... guitar?"
    MCT "Who..."
    MCT "Well, whoever it is knows what they're doing."
    if getFlag("MC004_balcony") or getFlag("Meet_Genji"):
        MCT "It sounds close. Maybe Genji plays in his spare time, or his roommate or something?"
    else:
        MCT "It sounds close, though. Maybe a neighbor or something?"
    "I walked back across the room as the music drew to a close, and looked dejectedly at my seat and desk."
    MCT "..."
    MCT "Maybe I should just get some lunch or something. I'm already up."
    MCT "I miss the days when it was Mom's job to keep the fridge stocked. This is hellish."
    "Much like my head during the early morning hours, my fridge was bare. I had a few condiments, a stick of butter, and an energy drink that I'd gotten... somewhere. No clue where."
    "I pulled my head up and glanced at the clock. If I moved quickly, I could catch the bus and be in town in no time for the store."
    ".. {w}Or I could just go to the cafeteria. It was still early enough."
    MCT "Yeah. Cafeteria it is."
    "I sat on my bed and pulled my shoes on, then adjusted my hair in the mirror in my bathroom."
    MCT "No clue why I'm trying anymore. It really doesn't matter anyhow."
    MCT "Maybe I should try dying it and see just how fast it actually grows based on that."
    MCT "Do something wild. Like blue or something."
    "Chuckling, I left my dorm, though not completely disregarding my hair dye experiment."
    scene black with fade
    pause .5

    scene Dorm Exterior with fade
    stop music fadeout 1.0
    "As opposed to my quiet, and honestly, kind of stuffy dorm, the campus was bright and welcoming."
    "A few birds flew by, tweeting and chirping away some sort of song together as they landed on the dorm buildings or into the treeline."
    "The sun shone overhead, and a warm, comfy breeze wrapped around me like a blanket, congratulating me on my choice to strike out from my homework littered prison."
    MCT "Good job, me. Job well done."
    play music Rain
    "I started walking away from the dorms and toward the ol' caf, shaking my head to let the breeze get under my underlayers of hair."
    if not isEventCleared("global026") and not isEventCleared("PRG023"):
        "Across the way, over at the women's dorms, I heard a door open and shut."
        show PRG sad at Position(xcenter=0.75, yalign=1.0) with easeinright
        pause .5
        "Aida emerged and walked stiffly away from the dorms. Her shoulders were scrunched in a bit, her pace that of a speed-walk."
        MC "Hey, Kodama-san."
        show PRG surprised
        pause .5
        show PRG worried
        pause .5
        PRG "Ah, h-hello Hotsure-san."
        MC "Hey! Sorry if I startled you."
        PRG "I-It's okay..."
        MC "How's your day going?"
        PRG "Um... okay. Yours?"
        MC "I'm doin' well. Just heading off for some lunch. I've been working on that paper from Tashi-sensei all morning."
        PRG "Oh... right."
        MC "What are you up to?"
        PRG "I-I'm going to meet Tozakura-san in town to pick up some ingredients for the cooking club."
        if isEventCleared("BE006") or getFlag("Meet_Kanami"):
            MCT "Right. That's Kanami. That girl I met with Honoka a few weeks back."
        MC "Nice. Got a competition coming up?"
        PRG "Not... for a little while. Every week or so, the club takes an inventory of the ingredients. Then, either Takamura-sensei, or the students that volunteer will go to the supermarket to stock everything that's needed."
        MC "Ah, I see. So, you and Tozakura-san are the delivery girls?"
        PRG "Mhm."
        MC "Nice."
        scene Campus Center
        show PRG worried
        with fade
        "As we walked into the center of campus, Aida glanced to the side, toward the academy's gates, and turned toward them."
        MC "Well, I'll let you get your shopping done. It was good seeing you, Kodama-san. Give my best to the club."
        show PRG neutral
        PRG "I-I will."
        PRG "I-It was nice seeing you too, Hotsure-san."
        "I nodded and turned as Aida went off toward the gates, the sound of her footfalls fading on the path behind me."
    elif isEventCleared("PRG023") and not isEventCleared("PRG025"):
        "Across the way, over at the women's dorms, I heard a door open and shut."
        show PRG sad at Position(xcenter=0.75, yalign=1.0) with easeinright
        pause .5
        "Aida emerged and walked stiffly away from the dorms. Her shoulders were scrunched in a bit, her pace that of a speed-walk."
        MCT "Okay... there she is. Breathe."
        MC "Kodama-san!"
        show PRG surprised
        pause .5
        show PRG unique
        PRG "Ah, h-h-hello H-Hotsure-san."
        MC "Hey! Sorry if I startled you."
        PRG "I-It's okay..."
        MC "How are you feeling? I didn't expect to see you up and about so quickly."
        PRG "I-I'm... o-okay, I guess..."
        "I thought back to her doubling over in pain back in her dorm that day."
        MC "That's good then. I'm glad to see you looking yourself again."
        show PRG unsure
        PRG "T-Thank you..."
        pause 1
        MC "So, where are you off to?"
        PRG "Um... I-I'm... I'm g-going into town with Tozakura-san to stock up for the cooking club."
        if isEventCleared("BE006") or getFlag("Meet_Kanami"):
            MC "Right. Kanami. That girl I met with Honoka."
        MC "Cool. I didn't think you guys would have a contest so soon after the last one."
        PRG "I-It's just normal stocking."
        MC "Ah."
        scene Campus Center
        show PRG unsure
        with fade
        "Aida and I walked into the center of campus, and I stole a side-glance at her."
        "She was walking with her hands folded over her skirt, her form looking more like someone trying to hide in plain daylight."
        PRG "I-I'm sorry, I-I... I should g-get to the bus stop. I-I don't want to keep Tozakura-san waiting."
        MC "Of course. Have a good day, Kodama-san. Be well."
        PRG "Y-You too, Hotsure-san."
        "Aida turned and sped-walked, almost ran away from me toward the bus stop."
        "I turned as well and headed off for the cafeteria, my feelings of hunger slightly tamed by the anxious stomach flutters that Aida's presence had flared up."
    elif isEventCleared("global026"):
        "Walking away from the dorms, I glanced across and over at the large fountain surrounded by benches."
        show PRG unsure at Position(xcenter=0.25,yalign=1.0) with dissolve
        pause .25
        "Aida sat alone on one of the benches, her gaze transfixed on the ground in front of her."
        "I didn't want to stare, but... the idea of Aida, of all girls, getting pregnant made it hard not to be curious."
        "Yet, there she was. She sat silently on the bench all alone, her gaze slowly turning to the fountain in front of her."
        menu:
            "Try to talk to her":
                $setFlag("MC009_PRGTalk")
                MCT "She... does not look well at all. I should probably check in on her."
                "I turned myself away from my food-based path and walked over to her, taking care to skirt around to one side to avoid jump-scaring her from behind."
                MC "Hey, Kodama-san."
                pause .25
                show PRG worried
                pause .75
                show PRG unsure
                PRG "H-Hello, H-Hotsure-san..."
                "Aida's gaze only met mine for less than a second before she looked back down."
                MC "I..."
                "I glanced around just a bit, just to make sure that no one was around. I didn't want to make her feel anymore uncomfortable than she might already be."
                MC "I was just heading to the cafeteria and saw you sitting by yourself."
                MC "I wanted to make sure that everything was okay."
                PRG "..."
                PRG "I-I'm..."
                PRG "..."
                MC "Would you mind if I sat with you for a moment?"
                PRG "... N-No... t-that's okay."
                MC "You mean... you'd rather I didn't?"
                PRG "N-No. I-I mean..."
                PRG "I-I... mm... y-you can sit down."
                MC "Oh, thank you."
                "I sat down on the same bench, though not directly beside her and looked out as the fountain made its relaxing splashing sound."
                "I glanced at her, and I watched her adjust herself on the bench beside me. Her pregnant belly hovered ever so slightly above her legs."
                "She let out a small nose exhale and rubbed one arm."
                MC "Are you... doing okay from class the other day?"
                MC "I really don't want to seem like I'm trying to pry or anything. I just... I can imagine that... all of that was a little... tough."
                pause .25
                show PRG nervous
                pause 1
                PRG "... People stare now."
                PRG "T-That... n-never used to happen."
                PRG "I-I c-could walk anywhere, and no one would even look at me..."
                PRG "But now... I-I'm the... the pregnant girl. A-And everyone knows."
                PRG "I... I can't even go to the cafeteria without someone staring at me..."
                PRG "T-The last few days have been..."
                pause .25
                show PRG unique
                PRG "... I just wanted to go to the park in town for a walk today, so I could think."
                PRG "B-But I accidentally locked my keys in my dorm..."
                pause .25
                PRG "So I-I'm... waiting for Alice to return and let me in."
                "I nodded in understanding and crossed one leg over the other."
                "Aida went to put her elbows on her knees and leaned forward. But, her belly getting in the way, she simply put her hands on it and looked down."
                "From where I sat, I could see bags under her eyes, and that sort of purple undertone that comes with them."
                MC "I see."
                MC "You could always head off to the cooking club in the meantime, couldn't you? Isn't that your main extracurricular?"
                PRG "I-It is... but I'm not active with them... right now."
                PRG "I... I decided to... t-take a little bit of time off until I feel less..."
                MC "Stressed?"
                PRG "Mhm..."
                pause .75
                show PRG nervous
                pause .5
                PRG "... I miss it, though."
                MC "It's a stress reliever for you, isn't it?"
                PRG "I-It is. B-But, I know I need to take the time away."
                PRG "I need to get used to... cooking like this. And moving around with this here..."
                "She looked down at her belly. Unlike someone like Alice, Aida's belly had a bit more curve to it, and was more round, which I supposed was how a pregnant belly looked compared to a... well, a fat one."
                MC "Yeah... you definitely do there. Don't wanna make a mistake in the kitchen, especially with a baby on board."
                PRG "Mhm..."
                PRG "I-I was... {i}mngh{/i}"
                "Aida shut her eyes and shook her head."
                show PRG sad-2
                PRG "..."
                PRG "T-Today is inventory day, most likely. S-So, I could've helped if I wanted to..."
                MC "Inventory day is...?"
                PRG "I-It's when the cooking club members look at what ingredients they need, and write it all down for someone to get from the store."
                PRG "Sano-san, Tozakura-san, and Sakura are probably working on that right now, actually..."
                MC "I see."
                MC "And, you don't feel up to going?"
                show PRG unique
                PRG "... N-Not really."
                MC "Well, you're more than welcome to join me for a bite in the cafeteria, if you'd like. I was just on my way there, myself."
                PRG "Um... n-no thank you, Hotsure-san. B-But I do very much appreciate your invitation."
                PRG "I... I think I'd just like to rest for today, though."
                MC "Totally understandable."
                pause .5
                "I glanced at the fountain before us and got up. Then walked over and glanced in."
                MC "Hm."
                show PRG worried
                PRG "Is... everything okay?"
                MC "Oh, yeah. Just checking to see if anyone made any wishes here."
                PRG "Like, throwing money into it?"
                MC "Mhm."
                PRG "I..."
                show PRG nervous
                pause .75
                PRG "... N-Nevermind."
                MC "Hm? What's up?"
                PRG "N-Nothing. I was just... remembering this story..."
                MC "Oh? Well, I'm down to hear it. I love a good story."
                PRG "I... i-it's a little long..."
                MC "I don't have to be anywhere."
                show PRG worried
                PRG "W-Weren't you going to have lunch?"
                MC "Well... yes, but now I'm talking to you. Food can wait."
                MC "C'mon. Let's hear it."
                PRG "..."
                PRG "... {w}When I was... six years old, I-I think... m-my mother and I used to go into town to go shopping."
                PRG "And everytime we'd go, we'd pass by this fountain in the middle of town. I-It looked a little bit like this one..."
                PRG "A-Anyway, I would always ask my mother for a coin to throw in, a-and she'd always tell me to shut my eyes, make my wish, then throw it in."
                PRG "A-And, I-I'd always wish for the same thing. A matcha cookie."
                PRG "After a few times, my mother noticed, a-and started bringing a matcha cookie wrapped up in her purse. T-Then, when I would shut my eyes, she'd put it down on the stone of the fountain, so I'd think my wish came true."
                MC "Aw. Your mom sounds sweet."
                show PRG unique-happy
                PRG "S-She is..."
                PRG "But once, I wished for a butter cookie instead, and she only had the matcha one in her purse."
                MC "Did she not put one down then? Tell you the fountain was taking the day off or something?"
                PRG "Um... n-no."
                PRG "She put down the matcha cookie anyway, and blamed the fountain. She told me that the fountain wasn't listening."
                PRG "S-So every time after that, I would make sure that I enunciated properly, and that I was speaking clearly."
                PRG "She told me a few weeks later, b-but still."
                PRG "I-I still like to throw a coin into the water sometimes."
                MC "I can see that. There's something innocent to it."
                MC "So, how do you like to relax? Are you a big fan of books or manga or anything?"
                show PRG neutral
                PRG "Um... I... well..."
                UNKNOWN "Aida?"
                show PRG worried at altMove(0.5, 0.25)
                show WG neutral at Position(xcenter=0.75, yalign=1.0) with easeinright
                PRG "H-Hello, Alice. T-Thank you for coming back so quickly."
                show PRG unique
                PRG "I-I'm sorry for being so careless."
                WG "Don't fret, Aida. It's quite alright."
                hide WG with easeoutright
                "Alice kept on her way toward the dorms."
                MC "Well, I'll let you be on your way, Kodama-san. Have a good day."
                show PRG unique at altMove(0.5, 0.5)
                PRG "T-Thank you, Hotsure-san."
                $setAffection("PRG", 1)
                pause .25
                show PRG worried
                pause .5
                PRG "And... {w}t-thank you... {w}f-for sitting with me."
                MC "Don't mention it, Kodama-san. I'll see you real soon."
                hide PRG with dissolve
                "I smiled at her as she turned to head back to her dorm, now having at least a bit more of a spring to her step."
            "Leave her be":
                $setFlag("MC009_PRGleave")
                "I glanced once more over at Aida."
                MCT "She... kind of looks like she wants to be left alone."
                "I continued on away from the dorms, giving Aida her space."
                "I could never say I truly understood how she felt, but it wasn't hard to empathize. She had a super wild factor compared to some of the others. I didn't blame her for being a little quiet."
    elif lockRoute("PRG") and not isEventCleared("PRG028") and not isEventCleared("PRG0029"):
        scene Dorm Entrance with fade
        "I shook my head and glanced back, hearing one of the doors shut heavily behind me."
        show PRG worried with dissolve
        "I glanced back, seeing Aida leaving the women's dorms."
        MC "Hey, Kodama-san!"
        show PRG surprised
        pause .5
        show PRG neutral
        pause .25
        PRG "H-Hello, Hotsure-san."
        MC "Hey! Did I startle you?"
        PRG "Um... a bit. I-I guess... I-I'm not used to having my name called so loudly."
        MC "Ah... my bad."
        PRG "I-It's okay..."
        MC "So, how goes your day today? Anything fun going on?"
        PRG "Um... n-not really. I-I... w-was just going to go for a walk. I feel like I haven't been outside at all lately."
        MC "Hah, yeah. I get that."
        MC "The sun is refreshing, for sure. Feels like a nice reinvigoration for the soul."
        PRG "Mhm. It's nice and warm today."
        PRG "Um... w-what about you? W-What are you doing today?"
        MC "Well, I was working on that Kofun paper for Tashi-sensei's class, and I decided to head out for some food."
        show PRG worried
        PRG "Oh."
        pause .5
        show PRG unique
        pause .25
        PRG "... I should work on that today."
        MC "Yeah, well. At least there's no shortage on papers around here. The one that you and I are working on together plus this one. That's quite the surplus of reading material for him."
        MC "But, anyway. I won't keep you from your walk. Have a good day, Kodama-san."
        show PRG neutral
        PRG "Y-You too, Hotsure-san."
        hide PRG with dissolve
        "Aida smiled at me, before she turned and walked down the path away from the dorms."
        "Even as I watched her skirt swish behind her as she went along, it made me happy to know that, after everything lately, everything between us was intact and well."
        "It gave me a nice, comfortable feeling in my chest."

    scene black with fade
    pause .5
    scene Hallway with fade
    "The hallways were... sparsely populated. Just enough where they didn't feel like horror movie adaptations of a school."
    "I headed down the hall toward the cafeteria, the smell of... well, something hitting me in the schnozz."
    if getHighestAffection() == "BE" and isEventCleared("BE022"):
        MCT "It... would be a bit more fun having Honoka here for some break-time lunch. Make the halls a little more lively."
        MCT "Though, that liveliness would turn into an inevitable conversation about aliens, or some sort of boob goblin or some such thing, and yeah. We'd be in the thick of it."
        "My generic text ringtone chimed from my pocket and I slid my phone out, putting up the metaphorical area radar so I could text and walk at once."
        BECell "Hey, Kei-chan! What's up??"
        "..."
        MCT "I swear someone is listening to my thoughts."
        MCT "But hey, good timing."
        MCCell "Hey! I'm just grabbing some lunch. Took a break from working on that paper for Tashi-sensei for a little while"
        BECell "Oh. I meant to work on that too but I ran into some of the archery club peeps and decided to hang out with them."
        MCT "Hm. I joined that whole thing so I could spend some time with her and give her some support, too."
        MCCell "That sounds fun. Is that Haruhiro guy there?"
        BECell "The guy with the elf ears?"
        MCCell "Mhm"
        BECell "He is, yeah. Why??"
        MCCell "He's a little different, isn't he? And I say that knowing my roommate."
        BECell "You're so mean!!"
        MCCell "Shh. It's called being observant."
        MCCell "Anyway I miss you and I'm looking forward to seeing you tomorrow after class!"
        "I gazed down at my phone, waiting on her reply..."
        "..."
        MCT "And... there's an emoji blowing a kiss."
        "Shaking my head, I smiled and continued down the hallway toward the cafeteria."
    elif getHighestAffection() == "AE" and isEventCleared("AE022"):
        "I brought my eyes around the hall, scanning like a sonar on a submarine."
        MCT "Alright... no Minori and no Yuki. Perfect."
        MCT "I guess, in a weird-ass way, that thing with Daichi actually worked, and Shiori kept her promise."
        "I let out a gentle sigh of relief."
        MCT "If I had to take one more day of dealing with those council goons riding my coattails, I was going to scream."
        MCT "Such a relief."
    elif getHighestAffection() == "GTS" and isEventCleared("GTS022"):
        "As I walked, some sunlight glinted into my eyes, though not much actually made contact thanks to my helmet of flowing locks."
        "I glanced out the window and shielded my eyes."
        scene School Planter with fade
        "Outside was the garden, and from the hallway, I could see Naomi moving about inside. I wasn't like, {i}right{/i} there, but I could still tell she was setting out a few different pots of... something."
        if getFlag("MC005GTS"):
            "I could also make out the flower we'd gotten from Ren Hirano during Golden Week, the one we planted together."
            "She bent to add some water to it, then let it be."
        else:
            "I watched her place a pot back into its place, having received some water, and then going back to her business with the others."
    elif getHighestAffection() == "FMG" and isEventCleared("FMG022"):
        "Breaking up the silence, footsteps echoed from around the corner."
        "I stood up straight, preparing myself should it be a teacher or someone whose opinion I cared about."
        show FMG neutral with dissolve
        pause .5
        show FMG happy
        pause .25
        FMG "Ey! What's up, Kei-kun?"
        "I let out my breath in a sigh of relief."
        MC "Hey! Not too much. You look like you've been getting a sweat in."
        FMG "Totally! I hit the track earlier for some endurance training. Got a good dozen or so laps in."
        MC "Nice!"
        MCT "... For you. My ass would be in the dirt after half a lap."
        MC "So, what brings you in here, then?"
        "Akira held up a bottle of water."
        FMG "Gotta stay hydrated, Kei-kun."
        MC "Hah, I suppose so."
        FMG "But since you asked, what brings you to the halls?"
        MC "Just grabbing lunch. I took a break from working on the Kofun period paper to get some thinking food."
        FMG "The..."
        show FMG surprised
        FMG "Oh shit!"
        FMG "I totally forgot about that damn paper!"
        FMG "And I had other assignments to get done, and I was going to try to hit the track again later!"
        FMG "Shit! Thanks, Kei-kun! I'll see you on a different day!"
        hide FMG with dissolve
        "Her last words were echoing down the hall as she nearly ran down it, away from me and toward the dorms."
        MCT "Well... at least I'm not the only procrastinator."
        "I shook my head, feeling slightly less alone as I walked for the cafeteria."
    elif getHighestAffection() == "WG" and isEventCleared("WG020"):
        "As I was alone, and really had nothing else critical to ponder, my mind went to the most recent, and most prominent conversation in recent memory."
        MCT "More intimate possibilities with classmates."
        MCT "What did Alice mean by that?"
        MCT "Is she hinting at me just outright asking her on a date? Would she even say yes to that?"
        MCT "Or is this one of those testing moments from her? Should I just keep it in mind for a while and ask her later?"
        MCT "Urgh... whatever."
        MCT "I'm too damn hungry to critically analyze right now."
        "I kept pace down the hall and toward the cafeteria."
    elif getHighestAffection() == "PRG" and isEventCleared("PRG027"):
        MCT "..."
        MCT "Going on a walk with Aida actually sounds really nice."
        MCT "Though, I'd probably be begging for a drive-thru no more than a minute or two in. I'm starving."
        "I rubbed my stomach and walked down the hall."
    elif getHighestAffection() == "PRG" and not isEventCleared("global026") and not isEventCleared("PRG023"):
        MCT "..."
        MCT "I could have gone for some time in town. Especially with Aida."
        MCT "If she can make grocery shopping a good time, then I think she's definitely something special."
        MCT "Though, last I saw her, she'd had a bit of a rough day, so maybe it's for the best that I didn't try to weasel my way in."
        "I continued on down the hall, silently running the events of that day in my head."
    elif getHighestAffection() == "PRG" and isEventCleared("PRG023") and not isEventCleared("PRG025"):
        "The walk to the cafeteria was loaded with other thoughts, however. And my mind kept being sucked back to Aida."
        "Even today, she looked like a ghost. Her usual spark seemed restrained, yet she was forcing herself back into the world."
        "And while we walked beside each other, I could have sworn that I'd heard her whimper or something."
        MCT "Why the hell is she trying to go to town like that? She should be in bed resting, not trying to tough it out."
        "I sighed. Hindsight thoughts did nothing but stress me out, and I trudged down the hall."
    else:
        pause .5
        MCT "It's kind of wild."
        MCT "Feels like almost no time has passed since Tomo and I first got here, but... so much has gone down."
        "I remembered that first day, when I'd met Tashi-sensei for the first time, and seen his tongue in all its glory."
        "Even Golden Week felt like it was a long time ago."
        MCT "God... time is flying."
        "I headed down the hall, hunger building with every step."
    scene Cafeteria with fade
    stop music fadeout 1.0
    "The scent of food was in full force as I stepped in."
    "I pictured my body being lifted by my nose and floated over by a low opacity ghostly scent hand and deposited by a meal of-"
    show dummy with vpunch
    UNKNOWN "Oh, excuse-"
    show Takamura neutral with dissolve
    if isEventCleared("MC002") or isEventCleared("BE006") or getFlag("Meet_Takamura"):
        Takamura "Oh! Hotsure-san, pardon me!"
        MC "Oh, no. I wasn't watching where I was going at all. That's my bad, Sensei."
        Takamura "Well, we can mark it as a wash and start fresh then."
        MC "Sounds good, Sensei."
        "Takamura-sensei smiled reassuringly at me."
    else:
        $setFlag("Meet_Takamura")
        Takamura "Oh! Pardon me! Keisuke Hotsure, yes?"
        MC "That's me. And no harm done, Sensei. I should open my eyes a bit too."
        "I recognized her immediately as the teacher who had given me my gift bag and dorm key on my first day."
        MCT "Takamura-sensei. Right."
    play music HigherEdu
    Takamura "Wonderful. Now, your timing is actually quite remarkable. Would you have a free moment?"
    MC "Ah..."
    "I focused my energy almost entirely on not letting my stomach growl in front of her."
    MC "Yeah, of course."
    Takamura "Thank you. Come along, then."
    "She turned and headed back into the halls. I looked across and toward the trays of food on the tables."
    MCT "Soon..."
    pause .25
    scene Hallway with fade
    "I turned and followed her into the hall."
    if isEventCleared("MC002") or isEventCleared("BE006") or isEventCleared("MC005"):
        MC "Sensei? Could I ask you something?"
        Takamura "Of course, Hotsure-san."
        MC "I know that my sister is in your homeroom. This... isn't regarding something with her, is it?"
        Takamura "Well... my, you've got some intuition, Hotsure-san. But, yes."
        Takamura "I have some... well, concerns that I'd like to discuss with you."
        MC "Of course."
    else:
        MC "Sensei?"
        Takamura "Yes, Hotsure-san?"
        MC "If I may... what is this regarding?"
        Takamura "Well... you see, your sister, Tomoko, is in my homeroom."
        Takamura "And recently, I've noticed some things that are a touch... concerning with her, and I was hoping that perhaps you could shed some light."
        MC "Oh, yes... I can try my best."
        Takamura "Then you have my thanks, Hotsure-san."
    scene Classroom2 with fade
    "Takamura and I turned from the hall into a classroom on the other side from good ol' classroom 3-B."
    show Takamura neutral with dissolve
    Takamura "Here we are."
    "She shut the door behind us and stepped inside further, taking a seat at her desk."
    "She nodded at the row by the window, and glanced to the far back corner."
    Takamura "Your sister usually sits there, if you were curious."
    Takamura "Now, the reason for my intrusion on your day is regarding... well, some traits in your sister that have me worried."
    MC "I see..."
    Takamura "I've noticed, not only in class, but in the few times I've seen her outside of classes, that she's quite the quiet girl, yes?"
    MC "Very."
    Takamura "Right. However, within classes, I've noted that she doesn't seem to initiate conversations with her classmates. In addition, she quite literally will refuse to take part in anything to do with a group of students."
    Takamura "She tends to make her disapproval... quite clear, as well."
    MCT "That'd be the Tomo I know."
    Takamura "And, she outright refuses to speak in any public setting. I don't believe she's ever spoken in a way that the entire class would be able to hear her."
    Takamura "Now, all of that to say that recently, I had overheard a group of students refer to her as a 'specter,' and they had mentioned that she hardly ever leaves her dorm."
    MC "That is... unfortunately quite true. She is quite the homebody."
    Takamura "Which is quite alright. There is nothing wrong with someone enjoying their time at home."
    Takamura "However, all of these stacked together leads me to believe that your sister is dealing with something quite intense, if I may be so blunt."
    Takamura "Has she ever exhibited any signs of social anxiety that you may have noticed?"
    MC "I..."
    MC "Well, Tomo is the type to choose a night at home over something more engaging."
    MC "Though, to be fair, it wasn't always that way."
    "Takamura leaned forward in her seat, listening carefully."
    MC "Far from it, actually. She used to be quite active. She had her own social circle, and she spent quite a bit of time with my close friend and I when we were kids."
    MC "She still liked her time at home, and she always enjoyed more calming activities, like video games, movies, and whatever. But not to the extent she does now."
    MC "I... I can't say that I really could tell you when she started to shift. It was gradual. Though, I do feel like something did happen at some point."
    MC "I've had theories and the like, but I've never really spoken to her, or anyone about them."
    MC "Most of the time, when it comes to anything emotional or sensitive, Tomo just shuts down the conversation entirely, either by diverting to a new topic, or flat out not responding."
    "Takamura nodded, and jotted something down onto some paper."
    MCT "She's... she really knows how to get to the heart of an issue. I don't think I've gone that in-depth on Tomo before."
    Takamura "That's all good to know. Anything else that you can think of?"
    MC "Well... I know she isn't a fan of her appearance."
    MC "She thinks she's 'way too short,' and she's not a fan of... well... her body. She thinks she has too many curves."
    MC "I can't say if that has anything to do with having anxiety, though. That being said, it has been quite the touchy subject for her for some time."
    Takamura "It could. Physical appearance, factor related or not, can weigh heavily on the mind's perception of oneself."
    Takamura "As such, I can relate to her scrutiny of her own body."
    MC "Well, at the very least here, you can feel comfortable with your factor. This is the place for it after all."
    show Takamura flattered
    Takamura "Ahhh..."
    Takamura "W-Well, I..."
    Takamura "{i}Ahem{/i}... I do hate to be frank, Hotsure-san, but I'm actually factorless."
    Takamura "I'm all genetics... {w}and sweets, I'm afraid."
    MC "Ah..."
    MC "I... m-my apologies, Sensei. That was... untactful of me."
    show Takamura reassuring
    Takamura "Oh, no. It's quite alright, Hotsure-san. You aren't the first to assume as such, and you won't be the last."
    show Takamura neutral
    pause .5
    Takamura "Now, that does finish off the questions I had for you. Thank you, Hotsure-san."
    MC "Of course, Sensei, but if I may..."
    MC "How would you... recommend addressing this... issue, I guess?"
    Takamura "Well, for starters, I would do your best to not overthink the matter. Sometimes, putting forth too much of an effort will simply smother the problem, rather than solving it."
    Takamura "I would recommend something quite simple. Just spend some time with her."
    Takamura "That time doesn't have to be something over-inflated with grandeur either. Standing by her side when she could use some support and staying in regular contact are good starting points."
    Takamura "If I were her, I'd feel quite comforted by someone close to me caring so much. And, I believe that each showing of that would bolster my connection to them."
    MC "I see. Thank you, Sens-"
    pause .25
    "A loud voice echoed down the hall, that of a woman shouting something."
    Takamura "Hrm... that's unusual."
    Takamura "Apologies. Please go on, Hotsure-san."
    MC "Ah... yes, thank you, Sensei."
    Takamura "Of course. Now, does your sister have any hobbies? Things she enjoys?"
    MC "Well, she..."
    MCT "Movies and video games are hobbies, yes. But... they kind of feel like the same sort of vein."
    MC "She hasn't really-"
    if isEventCleared("PRG013") or getFlag("Meet_Sakura"):
        pause .25
        show dummy with vpunch
        pause .25
        show Takamura neutral at altMove(0.5, 0.25)
        show Sakura frustrated at Position(xcenter=0.75, yalign=1.0) with easeinright
        pause .5
        "The door slammed open across the room, and in came Sakura, her arms covered in some sort of white powdery substance."
        "Behind her, more shouting echoed in."
        Sakura "Takamura-sensei, I'm really sorry for barging in, but I... urgh, they won't stop."
        Takamura "Myoga-san, what are you referring to? Who won't stop?"
        Sakura "Chisaka-san and Wada-san. They're nearly at each other's throats."
        Sakura "Some argument over a date or something."
        show Takamura sad
        Takamura "I see."
        Takamura "Hotsure-san, I'm very sorry, but you'll have to excuse me."
        MC "Of course, Sensei."
        show Takamura neutral
        Takamura "Actually... you might as well join us. We can discuss this further on the way back."
        MC "I... okay?"
    else:
        pause .25
        show dummy with vpunch
        pause .25
        show Takamura neutral at altMove(0.5, 0.25)
        show Sakura frustrated at Position(xcenter=0.75, yalign=1.0) with easeinright
        pause .5
        "The door slammed open across the room, and in came a girl with an apron on, her arms covered in some sort of white powdery substance."
        "Behind her, more shouting echoed in."
        Student "Takamura-sensei, I'm really sorry for barging in, but I... urgh, they won't stop."
        Takamura "Myoga-san, what are you referring to? Who won't stop?"
        Student "Chisaka-san and Wada-san. They're nearly at each other's throats."
        Student "Some argument over a date or something."
        Takamura "I see."
        Takamura "Hotsure-san, I'm very sorry, but you'll have to excuse me."
        MC "Of course, Sensei."
        Takamura "Actually... you might as well join us. We can discuss this further on the way back."
        MC "I... okay?"
    "Takamura rose from her chair and walked swiftly to the door, heading out as I followed behind her."
    scene black with fade
    pause .5

    scene Cooking Classroom with fade
    if isEventCleared("PRG013") or getFlag("Meet_Sakura"):
        "The two girl's escalating voices echoed down the hall, growing in volume as we grew closer and closer, to the point where I was legitimately surprised that someone wasn't filming them for the internet as I walked in with Takamura and Sakura."
    else:
        "The two girl's escalating voices echoed down the hall, growing in volume as we grew closer and closer, to the point where I was legitimately surprised that someone wasn't filming them for the internet as I walked in with Takamura and Myoga-san."
    "The two girls stood in the middle of the room, nearly nose to nose with one another."
    "One of them, clearly quite muscular, had one finger pointed directly at the other girl's face, literally screaming insults at her."
    "While the other, taller than her by a head or two, was bent down a bit, matching the first girl in volume and insult harshness."
    if isEventCleared("PRG013") or getFlag("Meet_Michiko"):
        "Close by, a third girl, who I recognized as Michiko Sano, stood, trying to bring the two of them back down."
    else:
        "Close by, a third girl stood, trying to bring the two of them back down."
    Student1 "Like he'd ever take a beanpole like you to a dance! He couldn't even reach your head for a kiss up on that stalk of a neck!"
    Student2 "You're one to talk! It must be so comforting to put his hands on a girl's stone-firm hips! Ever the image of softness and grace, aren't you, Chisaka-san?"
    Student1 "At least I know how to look out for my figure! I can see your gut flab from here, miss 'perfect cinnamon pancakes!' Those breakfast desserts are going to your damn head and your ass!"
    show Takamura strict with dissolve
    Takamura "Girls."
    stop music fadeout 1.0
    pause .5
    "Despite Takamura's voice going barely above her normal speaking tone, both girls went silent and turned to her."
    Takamura "I think you both are well aware that there's no need for such volume. I believe half of the dorms could hear you."
    Student1 "But she-"
    Takamura "I will be hearing from both of you. However, not at the same time."
    Takamura "Wada-san? If you would?"
    Student2 "..."
    "The taller girl blushed a bit, standing up to her full height."
    Student2 "It's Takeda-san. I... I've had a crush on him for quite some time, and he's single now-"
    Student1 "And likes me!"
    Takamura "Chisaka-san. In time."
    "Takamura glanced over to her, then back to Wada-san."
    Student2 "He was dating another girl, but since they aren't together anymore, I was hoping to ask him to the Matsuri."
    Takamura "I see."
    Takamura "And, Chisaka-san? You were intending the same?"
    Student1 "Well, yeah. I've had a thing for him longer than Wada-san has. Plus, he's talked to me more. I know he likes me more than her."
    Takamura "Mmn."
    show Takamura neutral
    Takamura "Perhaps... have either of you considered asking Takeda-san how he feels?"
    "A thick silence hung in the air as both girls glanced at each other, then down."
    Takamura "Consider this. Are you even certain that he'll be attending the festival?"
    Student2 "Who wouldn't?"
    Takamura "He might have a previous engagement in mind."
    Takamura "Either way, though I can understand the passion you both have, would it not make more sense to ask him directly and let him choose, rather than standing here bickering over it?"
    Takamura "Because, if you're seeking his approval, I believe you need to actually have him here to get said approval."
    Student1 "But-"
    play music Rain
    Takamura "I know. The pulls of affection can drive the heart mad."
    Takamura "However, someone who can control those feelings and use them in a proper manner will achieve far greater success than someone trying to simply bash another over the head with their deep rooted attraction."
    Student1 "I... I see."
    Student2 "Yes. That... makes a lot of sense."
    Student1 "Thank you, Sensei."
    Takamura "Of course."
    Takamura "Now, while I'm here, Sano-san. How stands the inventory? Managing alright, I hope?"
    if isEventCleared("PRG013") or getFlag("Meet_Michiko"):
        Michiko "Yes, Sensei."
        if isEventCleared("PRG022") and not isEventCleared("global026") and not isEventCleared("PRG026"):
            Michiko "Tozakura-san and Kodama-san are in town shopping right now."
        elif isEventCleared("PRG026") or isEventCleared("global026"):
            Michiko "Tozakura-san is in town shopping right now."
        Takamura "I see. Wonderful, then."
    else:
        Student "Yes, Sensei."
        if not isEventCleared("global026"):
            Student "Tozakura-san and Kodama-san are in town shopping right now."
        if isEventCleared("global026"):
            Student "Tozakura-san is in town shopping right now."
        Takamura "I see. Very good, then."
    Takamura "Oh, Hotsure-san? This is Michiko Sano. The cooking club president."
    if isEventCleared("PRG013") or getFlag("Meet_Michiko"):
        Michiko "Oh, we've met, Sensei. Remember? On the day Kodama-san joined up?"
        Takamura "Ah, of course. You're correct, Sano-san."
    else:
        MC "It's nice to meet you, Sano-san."
        Michiko "Likewise."
    Michiko "Now, as I was saying, Sensei, we're sticking to the bare essentials until the next competition comes up. That should leave us with enough for now."
    Takamura "Yes. Best not to overdo it."
    Michiko "Right. Thank you, Sensei."
    Takamura "Yes. And thank you for keeping me in the loop. I'm quite certain you could keep the club afloat without my intervention."
    Michiko "You're the cooking teacher, Sensei. We wouldn't get too far."
    if isEventCleared("FMG018"):
        MC "You're the cooking club teacher, Sensei?"
        Takamura "You're surprised, Hotsure-san? I did have a cooking lesson with you once, you know."
        MC "Well, yeah, but I would have assumed you were the school's counselor or something, and just so happened to have a penchant for cooking."
    elif isEventCleared("BE006") or isEventCleared("PRG013"):
        MC "I... honestly, you could've fooled me if I didn't know better."
        MC "I totally would've thought of you as a school counselor, Sensei."
    else:
        MC "You're the cooking club teacher, Sensei? I could have sworn you were the school's counselor."
    Takamura "Hah, you flatter me, Hotsure-san."
    Takamura "But yes. Aside from being a homeroom teacher, I also supervise the cooking club and have some elective classes in cooking as well."
    Takamura "However, I have no doubts that you all could run the club without me."
    Michiko "You aren't leaving, are you, Sensei?!"
    Takamura "Oh, no no. Not now, of course. Take it as me having a great deal of trust in you all."
    Takamura "And my my, I seem to have once again forgotten my manners."
    show Takamura neutral at altMove(0.5, 0.25)
    show Sakura neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    Takamura "Hotsure-san, you already know Sano-san. This is Sakura Myoga, Etsuko Chisaka, and Hotaru Wada."
    if isEventCleared("PRG022"):
        Sakura "Pleasure, Hotsure-san."
        MC "Yeah, yeah. Nice to see you again, Myoga-san."
        Takamura "My, Hotsure-san. Got friends in all places, haven't you?"
        Sakura "Well, it's kind of by extension."
        show Sakura happy
        Sakura "He usually tends to spend more time chatting up my cooking partner than talking to me."
        Etsuko "Can you blame him? Kodama-san's a gem, in case you haven't noticed. Girl has a smile that could attract any dude."
        show Sakura neutral
        Hotaru "Would you rather take Kodama-san to the festival instead, Chisaka-san? Seems like you've got quite the eye for her."
        Etsuko "I-I was just saying!"
        Hotaru "I know, I know. Kodama-san does have a special sort of charm to her. I heard her laugh once and just about melted."
        Sakura "Melted?"
        Hotaru "It's so joyous sounding! Like, it fills the entire room!"
        if isEventCleared("PRG026"):
            Michiko "Speaking of, when is she planning to return?"
            Takamura "When she feels ready, Sano-san. She has some personal matters to take care of."
            Michiko "I... of course."
        else:
            Michiko "Very true."
    else:
        $setFlag("Meet_Sakura")
        $setFlag("Meet_Michiko")
        "I bowed to each of them politely."
        MC "Nice to meet you all."
    Takamura "The cooking club is a bit different from other clubs, Hotsure-san."
    Takamura "We have competitions, of course. But, the club as a whole is largely based on personal achievement over the competition results."
    Takamura "I have no issue with the competitions, and I do look forward to the excitement of them. But, I do also see great value in the process of learning, and perfecting the art of cooking."
    MC "That makes sense."
    Michiko "Oh, Takamura-sensei? I did have a question on the rotation of the vegetables. Could we go over them once more?"
    Takamura "Oh, yes yes, of course."
    hide Takamura with dissolve
    Sakura "So... to make sure I have this straight, you two were planning to tousle over Takeda-san, right?"
    Hotaru "I actually intend to win, thank you."
    Sakura "Ah... {w}you do know that he's planning to go to the festival with Koneko-san, right?"
    "Hotaru & Etsuko" "WHAT?!"
    Etsuko "The soccer club girl?!"
    Sakura "Yeah? I heard it in the halls earlier. Koneko-san was talking to her friends about it."
    Hotaru "But they broke up! It's been a few weeks since then!"
    Sakura "Apparently they got back together then, because I heard that no more than a couple of hours ago."
    Hotaru "That BITCH!"
    Etsuko "For real! Screw her!"
    Hotaru "Well, there goes my Matsuri plans. Guess I'm going stag now..."
    Etsuko "I know! Stupid skank..."
    "I glanced at Sakura, who rolled her eyes as the other two girls kept throwing around different expletives to describe this abhorrent 'date stealer.'"
    MC "So. Inventory day, huh?"
    Sakura "Mhm. The most exciting day of days."
    Sakura "Checking and double checking, you know."
    MC "Right."
    MC "Oh, lucky to catch Takamura-sensei in the classroom when she was, huh? Saved you some searching."
    Sakura "Ah, not really."
    Sakura "I've worked with her long enough to know where she'll be when."
    Sakura "She's involved in... well, a lot. But, even when she isn't available, she tries to make herself accessible in case of any problems or anything."
    MC "Wow. Proactive on her end."
    "Across the room, Takamura and Michiko headed back over, Michiko scribbling away on a clipboard, yet somehow being able to walk in a totally straight line."
    show Takamura neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    Takamura "Girls? I thought we were through with this argument."
    Sakura "Oh, they aren't fighting each other now, Sensei. They found out someone else is going with Takeda-san."
    Takamura "Ah... I see."
    "The two girls glanced over from their hate and trash-talk session."
    Etsuko "Who are you taking to the festival, Sensei? Someone special?"
    Takamura "Me? I... well..."
    Takamura "I-I'm a bit too focused on my work at the moment for dating."
    show Takamura happy
    Takamura "Though, I have greatly missed the Matsuri. Such a wonderful time. Filled with such lively excitement in the air."
    MC "You... missed them?"
    Takamura "Oh, yes. I've spent the last decade or so in Europe, Hotsure-san."
    Sakura "What are the festivals like there, Sensei? Compared to the Matsuri."
    show Takamura neutral
    Takamura "Well, firstly, no yukatas."
    MC "That's different."
    Takamura "Indeed. The parades also lack a sort of... vibrance. Far less colors than here, I'd certainly say."
    Takamura "And, as a whole, it struck me that Europeans have quite the different approach to tradition than here in Japan."
    Hotaru "Sounds a little dull to me..."
    Takamura "Not even close, Wada-san. It's simply a matter of cultural differences. The European festivals have their own sort of charm to them, which while different from what we have here, still has the same feeling of celebration."
    Takamura "Personally, I quite enjoyed The Fête des Lumières in Lyon, France."
    Sakura "Sorry... what was that?"
    Takamura "The Fête des Lumières. Or, the Festival of Light. It's a series of light shows and street performances over the course of a few days. It's quite the spectacle."
    Takamura "Though, by far, my favorite aspect was the tradition of every house placing candles along the outsides of the windows."
    Takamura "All together, they give off the most breathtaking lights at night. Truly unforgettable."
    Takamura "It felt as though I was living in a fairy-tale. And to this day, I still remember that feeling of excitement. That sort of child-like wonder that comes when experiencing something new and spectacular."
    Takamura "... {w}Ah... pardon my rambling."
    Michiko "Is it true that you were a chef at a five star restaurant in Paris, Sensei?"
    Takamura "Technically, Sano-san, restaurants only have a three star rating system there."
    Takamura "One star is a very good restaurant. Two is a place that's 'worth a detour'. And three is a truly special restaurant, and one well worth the trip."
    MC "You... didn't really say no, Sensei. And, your knowledge on European restaurants is definitely something."
    Takamura "Yes... thank you, Hotsure-san."
    "As Sakura went on to ask Takamura about some vague french dish with lamb that I hadn't heard of, I glanced up at the clock on the wall."
    MCT "Oh, geez... that took a bit."
    MCT "Hope the caf' is still open..."
    Takamura "-find that adding the garlic and rosemary to the slits on top yields a more vibrant flavor."
    Sakura "I see."
    MC "Well, I'd best be going. I have some lunch to have in the cafeteria."
    Takamura "Oh, indeed you do. My apologies for keeping you, Hotsure-san. You must be famished."
    Takamura "A shame, though. On a normal day, you could have taken home some of the leftovers from the club members. No food goes wasted here."
    if isEventCleared("PRG022"):
        Sakura "I'm sure he knows that, Sensei. He's tasted Kodama-san's cooking."
        Takamura "Ah, yes. Then you know quite well."
    MC "Very true."
    MC "But anyways, it was wonderful meeting you all."
    hide Sakura with dissolve
    "I bowed to them all politely, and glanced to Takamura, who ushered me toward the door where we wouldn't be overheard."
    show Takamura at altMove(0.5, 0.5)
    Takamura "I do hope that you take our earlier conversation to heart, Hotsure-san. And please keep in mind what I told you."
    MC "Of course, Sensei. Thank you for letting me know."
    "I bowed to her politely."
    Takamura "You're very welcome, Hotsure-san. I'm more than happy to do my job."
    Takamura "Have a wonderful lunch, and a pleasant rest of your day."
    MC "You as well, Sensei."
    scene Hallway2 with fade
    "I headed back out into the hall and down to the cafeteria."
    "Any thoughts that I could have had about what she had said were drowned out by the sudden jab of hunger in my guts."
    jump daymenu

label MC011:
    scene Cafeteria with fade
    play music Schoolday
    if not isEventCleared("BE032"):
        MCT "Alright, time to eat. I could use the break."
        show BE neutral with dissolve
        MC "Yo, Honoka, mind if I sit here?"
        show BE happy
        BE "Of course, Kei-chan. You don't have to ask you know?"
        MC "Heh, good to know."
        BE "How are you doing?"
        MC "Could be better."
        show BE doubt
        BE "Same, to be honest."
        "Today had been a particularly stressful day of classes, and it wasn't even halfway over. It was still early in the semester, but just late enough when classes were starting to drop notice of their first big test."
        show BE neutral
        "That was normal school stuff, but what wasn't normal was the very noticeable transformation that was taking place across much of the student body at school."
        "By now it was pretty clear what was going on with everyone."
        show BE unique
        extend " Some, like Honoka, seemed to be enjoying it,"
        show BE happy
        " but most everyone wasn't all too happy about it and there wasn't any way of hiding it anymore."
        show BE neutral
        "For my money, I hadn't had to deal with too much more than an uncooperative hairdo and a slightly obscured view. It still felt weird feeling it halfway down my back. Still though, it was pretty mild compared to most. Honestly, I got off easy."
        "Putting it all in perspective though, it was easy to see that people here were starting to feel on edge."
        "Which is why it wasn't too hard to imagine that an innocent bump into someone might instigate a full blown incident."
        play sound Thud
        play music Tension
        show BE surprised
        UNKNOWN "Hey watch where you're going, {i}fatass{/i}!"
        "Fat Student" "Maybe you shouldn't lean back into the isle where people are walking, {i}dumbass{/i}. {w}I guess I shouldn't be too mad about it since you obviously got more meat than brains growing in that head of yours."
        hide BE with dissolve
    else:
        MCT "Alright, time to eat. I could use the break."
        "The cafeteria was packed, but I was looking around for a familiar face to sit next to so I wouldn't have to sit with strangers."
        show AE neutral with dissolve
        MC "Hello Matsumoto-san, mind if I sit here?"
        show AE neutral-eyebrow
        AE "You're certainly welcome to, Hotsure-san"
        MC "Cool. So, how are things going?"
        show AE neutral
        AE "Coursework has started to pick up, but it hasn't proved too difficult as long as I keep on top of my studies. I've been more preoccupied with matters pertaining to the student council."
        MC "Oh? Is that so, like what?"
        show AE neutral-annoyed
        AE "There's been an uptick in student disciplinary matters."
        show AE glasses
        extend " I'll spare you the details, but it has been rather distracting."
        show AE neutral
        MCT "Sounds like I'm not the only one feeling a bit strung out lately."
        "Today had been a particularly stressful day of classes, and it wasn't even halfway over. It was still early in the semester, but just late enough when classes were starting to drop notice of their first big test."
        "That was normal school stuff, but what wasn't normal was the very noticeable transformation that was taking place across much of the student body at school."
        "By now it was pretty clear what was going on with everyone."
        extend " Some, seemed to be enjoying it,"
        show AE pondering
        " but most everyone, like Matsumoto-san, wasn't all too happy about it and there wasn't any way of hiding it anymore."
        show AE neutral
        "For my money, I hadn't had to deal with too much more than an uncooperative hairdo and a slightly obscured view. It still felt weird feeling it halfway down my back. Still though, it was pretty mild compared to most. Honestly, I got off easy."
        "Putting it all in perspective though, it was easy to see that people here were starting to feel on edge."
        "Which is why it wasn't too hard to imagine that an innocent bump into someone might instigate a full blown incident."
        play sound Thud
        play music Tension
        show AE surprised
        UNKNOWN "Hey watch where you're going, {i}fatass{/i}!"
        "Fat Student" "Maybe you shouldn't lean back into the isle where people are walking, {i}dumbass{/i}. {w}I guess I shouldn't be too mad about it since you obviously got more meat than brains growing in that head of yours."
        show AE neutral-annoyed
        AE "Please excuse me Hotsure-san."
        hide AE with dissolve
    "Muscle Student" "Now that's uncalled for, aren't you people supposed to be jolly?"
    "Fat Student" "Oh that's {i}real{/i} funny. You think I wanted this? On second thought, I'll be feeling pretty jolly once I knock your sorry ass out."
    "Muscle Student" "You think I'm supposed to feel sorry for you just because you got the shit end of the stick? I've been itching to try these babies out, I'll wreck you in a heartbeat porkchop."
    "Fat Student" "You're all talk, I'll lay you out right here, {i}right now{/i}!"
    if not isEventCleared("AE029"):
        show Tako excited with dissolve
        Student "FIGHT!"
        show Tako happy
        extend " {i}We got a fiiiight{/i}!"
    else:
        show Tako excited with dissolve
        Tako "FIGHT!"
        show Tako happy
        extend " {i}We got a fiiiight{/i}!"
    "Crowd" "{i}Fight! {w}Fight! {w}Fight!{/i}"
    hide Tako with dissolve
    "Whether it was an expression of their own tensions, or an amusing distraction, the entire cafeteria seemed just as eager as the participants to see a fight go down."
    "I was pretty curious myself to be honest. {w}But just before either could start swinging, they both met a significant roadblock."
    show Hageshi neutral with dissolve
    stop music
    Hageshi "What seems to be the issue here, gentlemen?"
    "Both would-be fighters froze in place as they looked out the corner of their eyes to see where the eerily calm voice had come from. {w}The rest of the cafeteria took notice too— you could hear a pin drop in the place."
    "Students" "Hageshi-sensei! {w}He started it!"
    "Sensing it best not to instigate anything further, the rest of the cafeteria went back to their usual business,"
    play music Schoolday
    extend " likely in hopes of escaping the ire of Hageshi in the process as the usual cacophony slowly resumed."
    Hageshi "Oh? Is that so? Tell me, why are you both so quiet? You both seemed so worked up just now. What changed?"
    "Hageshi-sensei slowly approached both students, gently placing one hand on each of their shoulders, towering over them in the process. Both were shaking like they were about to piss themselves."
    "Muscle Student" "N-Nothing... W-We were just joking... {size=-6}hehe{/size}"
    "Fat Student" "Y-Yeah, j-just having a laugh... {size=-6}haah{/size}"
    Hageshi "Why don't we have a seat gentlemen?"
    "Hageshi tightened his grip on their shoulders, nearly crumpling them to the ground if he hadn't shoved them into seats in the process."
    "Students" "{i}Giiaak! {w}{size=-6}Ow!{/size}{/i}"
    Hageshi "Gentlemen, I didn't come here to tell you to stop what you were about to do, moreso to offer up a perspective that might make you... reconsider your current course of action."
    "Muscle Student" "S-Sure thing Hageshi-sensei... I've reconsidered. Can I go now?"
    Hageshi "No."
    "Judging by the wensing on their faces, Hageshi must have tightened his grip on them even further."
    Hageshi "Listen. Every man has to decide for himself what's worth fighting for. That's not for me to say to you. But what I want to impress upon you is that when you choose to fight— whether you know it or not— you're putting your life on the line."
    "Fat Student" "It wasn't supposed to be that serious..."
    Hageshi "It never is. A clean shot. An unexpected knockout. A poorly placed ledge. A bad bump on the head. And {i}boom{/i}— it's all over for someone."
    Hageshi "It might not be what you're looking for, but it's what you're asking for when you decide to throw down with someone."
    if isEventCleared("FMG030"):
        Hageshi "You want to know how I got these scars? It's a funny story really, but that's for another time. I can assure you though that the other guy looks a lot worse than I do."
        Hageshi "The point is, just know that the consequences of a split second can stick with you the rest of your life."
    else:
        Hageshi "You've seen the scars on my face, yes? There's nothing to be done to undo them, and I can assure you that the other guy looks a lot worse. Just know that the consequences of a split second can stick with you the rest of your life."
    Hageshi "Do with that knowledge what you will. But if you still have the will to fight, why don't you join me and some of your fellow students at judo club practice tomorrow?"
    "Muscle Student" "{size=-4}O-Okay, Hageshi-sensei...{/size}"
    "Fat Student" "{size=-4}S-Sure thing, Hageshi-sensei...{/size}"
    Hageshi "Good. That's what I like to see. {w}Now get the hell out of here."
    "Students" "Yes Hageshi-sensei!"
    "Both students scurried away about as fast as they could, despite neither one of them having gotten a chance to eat their lunches."
    if isEventCleared("MC002"):
        MC "Man Hageshi-sensei, you really spooked them."
        Hageshi "Oh, hello, Hotsure-san. You think so? I suppose that's a useful outcome in its own right, but I was just trying to impress upon them the gravity of their decisions."
        Hageshi "You're all adults now. It's high time you all realized how the decisions you make today will have lasting effects throughout the rest of your life."
    else:
        "Hageshi-sensei, the math teacher. I had heard rumors he wasn't someone you wanted to mess with, but I thought that was just because of his size. Those two guys were pretty big themselves— and they were terrified of him."
        Hageshi "Hm?"
        MCT "Looks like he noticed me."
        Hageshi "Hello there, Hotsure-san. Hope that little incident didn't ruin your lunch."
        MCT "To be honest, I kind of wanted to see a fight..."
        MC "No big deal, you certainly taught them a lesson though."
        Hageshi "One too few know, sadly. You're all adults now. It's high time you all realized how the decisions you make today will have lasting effects throughout the rest of your life."
    Hageshi "This school is here to help you with those decisions, at least in so far as how they relate to your growth, but anything can be a life lesson if you let it."
    MC "Hmm, that's good advice, Hageshi-sensei. I'll try to keep that in mind."
    Hageshi "Good to hear. {w}I wanted to ask, have you given any thought to signing up for my discrete mathematics course next semester? You're one of the better students, I think you'd enjoy it."
    MC "Ummm, I'll have to think about it more, Hageshi-sensei."
    Hageshi "You can say no, it's fine. You're an adult now, make your own decisions. Besides, if you're here, that means you have a lot of other more important things going on that are weighing on your mind."
    Hageshi "I know hair growth probably doesn't seem like much compared to what a lot of other people are going through, but I know it's not without its own issues."
    MC "Thanks Hageshi-sensei. It hasn't been that bad so far."
    Hageshi "Someone might be dealing well with their growth now, but that might not be the case come next semester. Keep that in mind, and have a bit more empathy than those two stooges."
    MC "Right."
    Hageshi "Just know that we're here to help, but more importantly, your fellow students are going to need your help as well."
    MCT "I'm not sure I'm in a position to help anyone, but okay..."
    MC "Sounds good. Thanks Hageshi-sensei."
    Hageshi "I'll see you in class later, Hotsure-san."
    #hide Hageshi with dissolve
    "I didn't really know what to think of everything any more. Seeing people growing and changing in strange ways, myself included— what did it mean? How was this going to affect us? What were things going to be like after leaving this place?"
    "It was quite a bit to take in. I didn't have all the answers, but after listening to Hageshi-sensei, I at least felt better that my time here might help me find some."
    jump daymenu

label MC024:
    scene Cafeteria with fade 
    play music Schoolday
    if routelock == "AE":
        "As I sat and gazed at the jello in front of me, my reflection gazed back, moving slightly along with the jiggling surface of the dessert as I poked it with my spoon."
        MC "Heh."
        show AE neutral with dissolve
        "I was about to look to Shiori with a grin and a sideways comment, however before I could even get a word in edgewise..."
        show AE angry-2
        AE "Not. A. Word."
        MC "Whaaaat, you didn't even know what I was gonna say!"
        show AE angry-3
        AE "Some sort of asinine comment about my backside?"
        MC "W-What? No! That would be rude and... uh..."
        show AE neutral-annoyed
        AE "... I have a feeling that you WERE thinking of making a comment, and then you would subsequently realize how I would react, and so you'd try to change the topic to save yourself."
        MC "How do you already know me so well?"
        AE "..."
        MC "You were thinking of the same thing looking at that jello, weren't you?"
        show AE aroused-3
        AE "Quiet."
        show AE neutral
        "I chuckled at Shiori's bashfulness as I looked around the lunchroom. Though sparse, the students who were here seemed to be pretty glum; more so than usual."
        MC "Sheesh, someone die?"
        AE "Approximately 106 per minute."
        MC "Ooookay, that's dark, but I mean why is everyone so down?"
        AE "Ah. Anxiety most likely. There's a lot of talk about preparing for college already, and what the outside world will hold. Though the council has thought of ways to be reassuring to the student body, the worries have spread like wildfire."
    else:
        "As I finished my lunch, I sat and stared at the empty tray in awkward unease. Normally, I'd sit and listen in on the murmurs of other students, but the silence in the lunch hall was deafening."
        "Quietly, I hummed to myself, accompanied by the buzzing of the lights above."
        MCT "The hell is going on? Usually there's some kind of sound or action happening. The only time people are this quiet is when-"
        "As I thought to myself, the silence was broken by the sound of heavy footfalls, along with the hearty sound of clapping with each step."
        show AE neutral with dissolve
        MCT "S-Speak of the devil."
        AE "Hotsure-san."
        MC "M-Matsumoto-san. Good afternoon."
        MCT "Seriously, I figured her titanic tush would have at least made her less threatening! How can someone with such a big butt be so scary!?"
        show AE glasses with vpunch
        AE "I trust things are proceeding well for you today?"
        show AE neutral
        MC "Y-Yeah! It's a bootyful day out- b-beautiful day out!"
        show AE neutral-eyebrow
        "Matsumoto-san raised an eyebrow as she caught my slip, yet said nothing."
        show AE neutral
        AE "... Indeed. All the better to get your work done and enjoy it, if you have any."
        MC "Ah. Nah, I'm uh... all sorted out, eheh."
        AE "Then you're far ahead of your peers, it seems."
        MC "Eh? Why do you say that?"
        AE "This week has brought with it talks about preparing for life outside of the school. While many have dutifully taken everything in stride, others... prefer not to think about future responsibilities at this time."
    MC "What about yourself?"
    show AE neutral-annoyed
    "Shiori bristled a bit at my question, but after clearing her throat, she shook her head."
    show AE neutral
    AE "... Nothing in particular. I'd originally believed that the application for the scholarship would be far more strenuous, however I was quickly disappointed."
    MCT "That's a weird way to say relieved!"
    MC "Sorry? Why do you say that?"
    AE "A scholarship generally denotes a student of high achievement. If that is to be the case, then it would make logical sense for the minimum requirements of the scholarship to be rather difficult to reach."
    MC "Well, it's based on grades, yes? Then, how low are you talking?"
    AE "Firstly, there is a system to it. And, the deadline is coming soon, so don't dawdle if you're looking to apply."
    AE "You'll need to take note of all of your grades and assign points to them, with an S grade being the highest, followed by A, B, and all the way down to D."
    AE "There are four points awarded for S, three for A, and so on, down to the worst score of zero for a D."
    MC "Right."
    AE "After you calculate your total sum of points, you then divide it by the number of classes to determine your average grade overall."
    AE "And, students who have managed to achieve a score of 3.2 or higher are eligible for the scholarship."
    MC "I... see."
    MCT "That's low, then? Doubt I even hit that. I wouldn't call myself the biggest brain in the class by a long shot. Especially compared to Alice, Aida, or Shiori."
    pause .5
    AE "With that in mind, are you considering applying?"
    MC "Maybe. I'm not sure of my eligibility, to be honest with you."
    AE "Hm. Bear in mind, expediency is the heart of efficiency."
    MC "Urgh... right. Okay, where do I go to apply?"
    AE "You can either request a paper document from the main office or print a copy from the school website. Take that to the secretariat near the principal's office, which itself is in the same wing as the school entrance."
    MC "Sounds easy enough."
    AE "In which case, I believe you should have what you need."
    MC "Awesome. Thanks, Shiori. I'm gonna head back to do that now."
    AE "That would be wise."
    "I got up, picking up my tray to dump in the garbage."
    UNKNOWN "Pardon me. Matsumoto-san?"
    show Minori neutral at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    show Yuki neutral at Position(xcenter=0.2, yalign=1.0)
    with dissolve
    if not routelock == "AE" or not getFlag("Meet_Minori"):
        MCT "Ohh... this is one of the student council members I've seen with Matsumoto-san. Minori... Minori Tomoe. Yeah, that sounds right."
        AE "Mm? Yes?"
        Yuki "Couldgh you..."
        pause .75
        Yuki "Hgh... importanth sthtudenth..."
    if routelock == "AE":
        "Yuki struggled to get out what she wanted to say, and Minori began to speak up on her behalf."
        Minori "Um, I believe what she's trying to say-"
        show AE pondering
        AE "Hold a moment, Tomoe-chan."
        "Only to be stopped by Shiori."
        show AE sad
        AE "Keep trying, Utagashi-chan."
        "Yuki, who only a moment ago was clearly distressed at her inability to speak, suddenly was surprised at Shiori's response... before looking determined."
        show AE neutral
        AE "Breathe. Keep calm. Go slow. You've got this."
        Yuki "Hoooh... Ohgkey... Couhgd... Couwd... yoo... hewp... wiff... importantph sthtudenth... counthil... wowk."
        show AE smile
        "Shiori smiled gently and nodded as Minori just looked on, just as shocked as I was."
        AE "Do you feel comfortable telling me what kind of work?"
        Yuki "... Mmph... Chompawe... ah nothes... tooo tscheshk... accuwashee."
        show AE neutral
        AE "Right. I'll make sure to make sure our accounts are accurate. For the recent club allocations, correct?"
        "Yuki, elated that Shiori understood, smiled as best she could and nodded."
        Yuki "Yuh!"
        AE "Very well, then. Tomoe-chan, do you have them ready for comparison?"
        "Minori was still dumbstruck, however, after a moment, she merely smiled and nodded."
        Minori "Of course ma'am. Whenever you're ready."
    else:
        Yuki "Mghh... importanth... {w}sthhhhtudenthh..."
        show AE pondering
        "Shiori nodded solemnly, her expression falling a bit as she glanced to Minori."
        Minori "What Yuki-san is trying to say is that we have important student council matters to attend to, Ma'am. Club allocations."
        show AE neutral
        AE "Very well, then. Tomoe-san, do we have our accounts ready for comparison?"
        Minori "Of course ma'am. Whenever you're ready."
    AE "Understood."
    AE "Farewell, Hotsure-san. Best of luck."
    MC "Thank you. Take care."
    pause .5
    MCT "Poor girl..."
    hide AE
    hide Minori
    hide Yuki
    with dissolve
    "Turning, I dumped my tray then headed out into the hall, heading for the library."
    scene black with fade
    pause .25
    play music LastBell

    scene Library with fade
    "Among the rest of the students, I was able to find myself a fine looking computer and sat down at it, clicking the mouse a few times, then typing in my login info."
    "Now logged in, I was able to pull up the website and access the Academy's private pages and such, since everything was so tucked away from the public's eyes."
    MCT "Okay... she said documents... {w}ah, there you are."
    MCT "Form... okay. Looks like form B-1 is what I need."
    "I printed it off and brought it to my computer, where I pulled out a pen from my bag and started marking numbers on lines and such."
    pause .5
    MCT "Right... that should cover it, then."
    MCT "Actually... hold on. Do electives go on here too?"
    "I moused over to the grades section of the website and punched in my info again."
    MCT "Physical edu-"
    MCT "I have an S in that?!"
    MCT "We had one class of that, and Tashi-sensei said that was like, not a regular thing!"
    if isEventCleared("MC006"):
        MCT "Even with that, though, handball was still a good time. With Naoki-sensei and his band of merry whistles..."
    if isEventCleared("FMG018"):
        MCT "Oh, there's that elective in cooking with Takamura-sensei."
        if getFlag("FMG018_FMG_CookingPartner"):
            MCT "Explains the grade level, then. Having Shiori around made that fairly simple to ace."
        elif getFlag("FMG018_GTS_CookingPartner"):
            MCT "Well... the grades don't lie. That class was a rough one."
        elif getFlag("FMG018_BE_CookingPartner"):
            MCT "Hah... we did clutch that, though. Especially making that French dish."
    "I penciled those grades in, then checked the others."
    MCT "... S in math. That's four points."
    MCT "History... {w}S."
    MCT "So that's... four points. Nice."
    MC "Biology is... an A."
    MC "For economics and civics... B."
    "I jotted all of these down as I went, until my list was full."
    MCT "Okay... two for a B. Three for an A. Ach, that B drags me down a bit."
    pause 1
    MCT "Oh, wow. I actually qualify."
    "I took my papers and got up, logging out from the computer mid-stand and heading to the door."
    MCT "Okay. The main entrance is... that-a-way."
    "Heading out, I hung a left in the hall and hurried off."
    scene black with fade
    pause .5
    play music Schoolday

    scene Gate Front with fade
    "Walking into the main entryway, I stopped for just a moment."
    MCT "This goes back a long time."
    MCT "Akira moving those benches with Shiori at her throat."
    if isEventCleared("RM002"):
        MCT "Or when I met Yuki-san while Daichi was doing his shenanigans."
    MCT "Good times..."
    "I glanced along one wall, and spotted the Principal's office."
    MCT "Well, that's not the secretariat. Shiori did say it was nearby, though."
    "I walked down a little further."
    MCT "Ah, here we are."
    "The door was marked \"Education and Student Support Department\". I headed in quickly."
    scene Info Desk with fade
    "I could make out the sound of a printer chugging along almost before I was inside, and I wasn't wrong."
    "Two women sat at computers, with one more standing near a printer along the rear wall."
    "None of them looked up as I entered, but by the looks of the three of them, they'd all likely been here long enough and seen things that made a guy with long hair look pretty run of the mill."
    "I stepped up to the woman closest to me on her computer."
    MC "Ehm... pardon me."
    "The woman glanced up at me, her brown eyes dull behind her thick glasses."
    "One eyebrow went up quizzically, yet with a degree of intensity, as if I were disturbing her life's work."
    MC "I was... just wondering where I can drop off my scholarship application?"
    "The woman glanced back at her computer screen and gestured with one hand toward the other woman on the computer."
    MC "Ah... thank you."
    "I stepped over to the other window, paper in hand."
    MC "Pardon me, Ma'am. I would like to submit my form for the scholarship application?"
    Secretary2 "Name?"
    MC "Ah... Keisuke Hotsure."
    Secretary2 "Class?"
    MC "3-B."
    "The secretary's eyebrows went up for just a moment as she clattered away on her keyboard."
    "The secretary plunked a few more keys, then got up and went to a file cabinet, pulling out one drawer."
    UNKNOWN "-tiring at the end of third semester."
    UNKNOWN "Who was this?"
    "I glanced over, seeing the woman by the printer now at the first secretary's desk, a cup of what I presumed to be coffee or tea in hand."
    Secretary3 "One of the counselors. It was just a consideration, but that's the news."
    Secretary1 "Hmph. Figures."
    Secretary1 "Think I'd better get working on the job advertisement for MEXT then?"
    Secretary3 "Hold off for now."
    Secretary3 "Noguchi-san is planning to discuss things with the counselor first, just to set things in stone."
    "The first secretary nodded and went about her business."
    "I glanced around the room a bit. Aside from books, office supplies, and well... the more than cheerful secretaries, there wasn't much going on."
    "The woman who had been helping me sat back at her computer, a folder in hand."
    Secretary2 "Do you have the form for your application with you? Please ensure that it has your grades from the first semester."
    MC "This would be it."
    "I handed the sheet to her, to which she glanced down at it."
    Secretary2 "..."
    MC "Is... that's the right form, correct?"
    Secretary2 "This is an attachment for the main document. This only lists your grades and the average. You'll still need to fill out a form for the actual application. Form A38."
    MC "I... alright."
    MC "Where can I get that from?"
    Secretary2 "I can print it for you here. You'll need to sign it and notate this document on the main application to show it's an attachment."
    "The woman turned to her computer and clicked some keys for a good minute or so."
    pause .75
    Secretary2 "Hm."
    MC "Is... something wrong?"
    Secretary2 "There seems to be an irregularity in your semester grade protocol that will prevent me from actually accepting your application for scholarship. Seems there is a missing signature from one of your teachers."
    MC "Oh. Does it say which one?"
    Secretary2 "Saemonsaburokouji-sensei."
    MC "... Sorry, which one?"
    Secretary2 "Saemonsaburokouji-sensei."
    MC "I... don't know who that would be. I'm sorry."
    Secretary2 "The grade comes from Naoki Saemonsaburokouji. From your physical exercise elective."
    if isEventCleared("MC006") or isEventCleared("BE046"):
        MC "Ohh... right. My fault."
        MCT "Naoki-sensei. Of course."
    else: 
        MC "Ah... right. Okay."
        MCT "... Who?"
    MC "So, what can be done to solve the irregularity?"
    Secretary2 "I'll do what I can to see if I can solve the problem from here. However, by the time requests pass through the proper links and all of the paperwork has reached where it ought to be, we'll likely be a good measure past the deadline for application."
    MC "Well, is there anything I can do to help things go a little faster?"
    Secretary2 "I'd recommend finding Saemonsaburokouji-sensei yourself and asking him for his signature. It will likely be quite a bit faster that way."
    pause .5
    MC "Hahh... alright."
    MC "Do you happen to know where I could find him about now?"
    Secretary2 "He's quite the busy man, but I'd imagine he's coaching a club at the moment."
    Secretary2 "As for which one, I'm afraid I'm not sure. But, I am certain he's somewhere on campus."
    MC "Alright. Well, thank you all the same."
    Secretary2 "You're welcome."
    scene Gate Front with fade
    MC "Agh."
    "I ran one hand through the back of my hair."
    MCT "This is such a headache..."
    MCT "Okay... where to start off?"
    pause .5
    MCT "The first logical place would be any and every place athletic. So, the track or possibly the pool."
    MCT "There's always the faculty room too, though I doubt he'd be there. Especially if he's coaching stuff."
    MCT "Auditorium is inside, though. May as well give that a once over first."
    "I turned down the hall, keeping my paperwork literally clamped in my left hand."
    scene Hallway with fade
    MCT "Why can't they just like, call him and get his approval over the phone? Do an auditory signature or something."
    pause .25
    MCT "Yeah, right. That wouldn't fly on any legal document."
    MCT "Feel like I barely know Sae... S..."
    "I unfolded the paper in my hand."
    pause .25
    MCT "Sae.... {w}mon... {w}saburo... {w}kouji-sensei."
    MCT "I feel like I've hardly met him."
    if isEventCleared("MC006"):
        MCT "Well, okay. There was the handball game after Golden Week."
    if routelock == "BE":
        MCT "I... think that he might coach the softball club, though. I don't even know where I'm pulling that from, but I feel like I heard that somewhere..."
        MCT "One of Honoka's clubs maybe?"
        "I sighed and pulled out my phone."
        MCCell "<Hey! You happen to know where I can find Naoki-sensei??>"
        pause 1
        "A minute or so later, no response."
        MCT "Well... gotta start somewhere."
    if isEventCleared("MC002"):
        MCT "He does wear a lot of whistles..."
    if not isEventCleared("MC002") or not isEventCleared("MC006"):
        MCT "I... think he was there for that handball game we had? Maybe?"
        MCT "... What does he look like again?"
    MCT "I just feel like I'm spitballing here."
    MCT "Regardless, the auditorium is the best bet. I'm like halfway there now anyway."
    if routelock == "PRG":
        "{i}VMMMM!{/i}"
        "I reached into my left-front pocket and yanked my phone out, unlocking it."
        PRGCell "<Hi, Keisuke. I'm going to be watching the softball game in about half an hour if you'd like to join.>"
        "I smirked to myself."
        MCT "I think Aida is the only person I've ever met to use perfect punctuation in text messages."
        MCCell "<Hey! Yeah for sure. Im running some errands for something right now but I can meet you there. I'll probably be a little late tho>"
        PRGCell "<That's okay. I'll see you when you get there!>"
        "I slipped my phone back into my pocket."
        MCT "That's going to be nice."
    pause .25
    scene black with fade
    pause .5

    scene Auditorium with fade
    pause .5
    MC "..."
    MCT "Where the hell is this guy?"
    "I walked through the empty, almost cathedral-esque room, hearing nothing but my footsteps on the wooden flooring."
    MCT "Wait, isn't the gym close to here, too?"
    "I picked up my pace and headed out the door again, heading left."
    scene Gym with fade
    "The gym wasn't exactly... busy as I walked in. Definitely no one that bore any resemblance to a teacher or a coach."
    "Down at one end, I spotted a flash of reddish brown hair."
    play music FMG
    show dummy with vpunch
    "{i}CLANG!{/i}"
    "I glanced down at the floor, praying that whatever this floor was built with wouldn't splinter under me."
    $setFMGOutfit(OutfitEnum.GYM)
    show FMG angry-2
    with dissolve
    "I glanced up as Akira pounded out one more rep."
    show dummy with vpunch
    "{i}CLANG!{/i}"
    FMG "Agh!"
    "Akira stood up and swung her arms at the shoulder, glanced over."
    if routelock == "FMG":
        show FMG flex
        FMG "Kei-kun!"
    else:
        show FMG happy
        FMG "Yo!"
    "Akira waved a bit as I smiled and walked over."
    if routelock == "FMG":
        "I stole a glance down."
        "Akira's sports bra and shorts clung to her body tightly as she walked over. That and her arms swinging as she walked nearly sent me over the edge right there."
        MCT "... Especially with so little left to the imagination."
    MC "Hey! What's going on?"
    show FMG upbeat
    FMG "Chest press, at the moment. From there... well, we'll see."
    MC "Sweet. You wouldn't be able to help me find someone quick?"
    show FMG neutral
    FMG "Uh... depends, I guess. Who's the target?"
    MC "Naoki-sensei."
    FMG "Naomi?"
    if routelock == "GTS":
        show FMG happy
        FMG "I... dude, she's like how tall now? You seriously can't find her? Also, I know she's mature and all, but Sensei?"
        MC "I..."
        MC "... No, I meant Naoki-sensei. The phys ed teacher." 
    else:
        FMG "Ah... pretty sure she's at the giants' dorms, dude. Maybe check there?"
        MC "Oh, no no. I meant Naoki-sensei. The phys ed teacher."
    show FMG neutral
    MC "Naoki... Sae... ach, Sae... monsaburokouji."
    show FMG surprised-2
    FMG "I..."
    FMG "Geez... that's a long-ass last name."
    show FMG neutral
    FMG "Well, it doesn't matter. What do you need him for?"
    MC "I need his signature for that scholarship thing that the Academy is doing. There was some paperwork error with my files and now I have to go searching."
    FMG "Hm. Yeah, no clue who that is."
    if isEventCleared("MC006"):
        MC "He was the coach when we all played handball that time?"
        FMG "Ohh..."
        FMG "Yeah, sorry. Still nothing."
    if isEventCleared("MC002"):
        MC "The teacher with... you know, the whistles?"
        FMG "OH! That guy!"
        FMG "Yeah, I did see him at the pool. I'm pretty sure Inoue-san was there too."
        MC "Oh, seriously? That makes things easier! Thanks!"
        FMG "No prob!"
        FMG "Now, I've got things to press."
    elif not isEventCleared("MC002"):
        pause .75
        FMG "Wait... hold on. Isn't that that guy with a ton of whistles around his neck?"
        FMG "Because I know I saw that guy at the pool earlier."
        if routelock == "BE":
            MC "Awesome! Thanks! That was my next stop if he wasn't here anyway."
            FMG "Sick! Hope you find him!"
            FMG "For now, I've got things to pick up and put down."
        else:
            MC "Oh, seriously? Sweet! Thank you!"
            FMG "No prob! Back to the grind for me, though."
    if routelock == "FMG":
        FMG "But, before I do."
        "Akira stepped closer and leaned forward."
        "I grinned and planted a kiss on her lips."
        MC "You're killin' those plates. Don't let them catch their breath."
        FMG "Never would!"
        "Akira hurried back to the chest press, and began unloading the plates and moved to the next machine."
        "I watched her for a moment, particularly as she wrenched the plates free of the machine and re-racked them, then headed out the door."
    else:
        MC "Sounds good. I'll see you later."
        FMG "See ya, Kei-kun!"
    scene black with fade
    pause .5

    scene Pool with fade
    play music Peaceful
    pause .75
    MCT "I swear..."
    "There was no coach or teacher or anyone of school staff at the pool, save for the fairly bored looking lifeguard watching from the chair."
    if isEventCleared("WG043"):
        MCT "Being here with a mission kind of sucks. I much preferred playing water polo with Alice and the other girls."
    if routelock == "BE":
        MCT "Huh... Honoka isn't here."
        MCT "Damn. I could've sworn..."
        "I pulled out my phone, glancing at my notifications and looking around with my hand behind my head like a lost tourist."
        MCT "She could at least one word text me."
    if isEventCleared("FMG032"):
        MCT "Reminds me of hanging out with Akira and finding that cat with Chibuki."
        MCT "What was his name? Chumley? Cher...ee?"
        pause .5
        MCT "Oh, Chumby. That was it."
        MCT "... {w}Weird ass cat."
    if not routelock == "WG" or not routelock == "BE" or not routelock == "FMG":
        MCT "I really should check this place out more often. Reminds me of summer."
    "I watched the few students there swimming laps, doing stretches, and so on."
    MCT "Honestly, swimming is probably pretty great for muscle soreness and such. Especially with the proportions around here." 
    $setWGOutfit(OutfitEnum.SWIM)
    if routelock == "WG":
        "One particular swimmer caught my attention. Moving gracefully through the water, despite her size, I realized now I should have expected to run into her this time of day."
        show WG neutral with dissolve
    else:
        "I watched as one girl got out of the water. Most of her lower half was still in the water, belying her true size, but once I noticed her blond locks I realized it could only have been one person."
        show WG neutral with dissolve
    MCT "Oh!"
    "I smiled at Alice and walked across the pool deck toward her, while simultaneously trying to avoid thinking about how sinful wearing street shoes next to a pool felt."
    MC "Hey, Alice!"
    if routelock == "WG":
        WG "Good afternoon, Dear. I hadn't expected you to stop by the pool. Were you looking for me?"
        "My gaze scanned over her as she pulled herself up from the pool, taking the steps at the corner of the pool. ."
        "The thoughts and frustrations of paperwork and the like momentarily left me as I found myself thinking more... fun thoughts."
        MC "I actually wandered in here by accident, but I suppose it wasn't a waste of time if I managed to run into you."
        show WG happy
        WG "Flatterer."
        show WG sly
        WG "Though I suppose I'll let it slide this time."
        show WG neutral
    else:
        WG "Good day, Hotsure-san."
    WG "You have the look of someone in search of something."
    if routelock == "WG":
        pause .25
        show WG happy-2
        WG "And, I'm assuming that something isn't a sneaky glance."
        MC "I-I-"
        show WG neutral
        "Alice simply smiled and rested one hand on the railing of the pool."
    MC "Well... you would be right, there."
    MC "I'm running an errand so I can-"
    MCT "Ugh... I've had to repeat this damned chain of events enough."
    if routelock == "WG":
        MC "I'm trying to track down Naoki-sensei. I need him to sign this paper work for a scholarship I'm applying for. I heard, but I don't know for sure, that he's the coach for the swimming club."
    elif routelock == "BE":
        MC "I'm trying to track down Naoki-sensei. I remembered that he coached the swimming club from when I was here with Honoka, and figured I could find him here."
    else:
        MC "I'm trying to track down Naoki-sensei, and I'd heard he might be coaching the swimming club."
    WG "Ah."
    show WG neutral-2
    WG "I'm afraid that I haven't seen anyone from the faculty here. And, as far as I know, the swim club doesn't meet today."
    if routelock == "BE":
        WG "I believe you'd be better off asking Honoka, especially if she's a member of said club."
        MC "Yeah, I tried that. No answer."
    else:
        WG "I believe you'd be better off asking Honoka. If memory serves correct, she is a member of that club."
        MCT "Is she, though? Her club status changes practically daily."
    MC "Right. Thank you, Alice."
    show WG neutral
    WG "Of course. I'd also recommend asking the lifeguard as well. It couldn't hurt."
    MC "Will do. Enjoy your swim."
    if routelock == "WG":
        "I stepped forward and leaned in for-"
        WG "Ut-uh. Careful now, Dear."
        "Alice took a measured step back. Just enough to get her front out of the way."
        WG "After what you've likely already been through, it would be a shame to soak that paper up against me."
        "I was suddenly well aware of the worth of the document in my hands, and the amount of legwork I'd already put in."
        MC "Ach, right. Thank you."
        WG "Of course."
        WG "Save that for next time. However, I expect the same gusto."
        MC "Will do there."
    else:
        WG "Thank you, Hotsure-san."
    hide WG
    "I turned to the sound of Alice's body involuntarily splashing back into the water from her simple push off back into the pool, and walked to the lifeguard's chair."
    MC "Pardon me."
    "The lifeguard glanced over, and based on the dryness of his skin, clearly hadn't seen much in the ways of action that day."
    MC "I was wondering if you could tell me where Naoki-sensei is?"
    Lifeguard "He's not here right now. He did stop by earlier."
    MC "Do you know where I could find him?"
    Lifeguard "Try the track. I saw a few students training earlier. He's supposed to be supervising a club or two today, and I believe the track team is one of his, so that's likely where he'd be."
    MC "Eesh. Busy guy."
    pause .25
    MC "Alright. Thank you very much."
    "I bowed to the lifeguard and turned to walk back across the pool deck."
    if routelock == "BE":
        "{i}BMMMPH{/i}"
        "I slipped my phone out."
        BECell "<Hey, Kei-chan!! I'm so sorry, I was in the shower!! I dont know where Naoki-sensei is right now, though. I'm sorry!!>"
        "I had to smile at the queen of the exclamation as I typed."
        MCCell "<It's all good Honoka. Thank you anyway. I'm on some stupid scavenger hunt of a mission for this damn scholarship. Ill fill you in later.>"
        BECell "<K! I'm going to study rn but I'll see you later!>"
        MCCell "<See ya!>"
        "I slipped my phone back into my pocket as I walked into the hall."
    if routelock == "WG": 
        "As I left, I glanced over at Alice backstroking her way across the pool."
        "After taking a moment of admiration, I stepped out and back into the hall."
    else:
        "I stepped out the door and back into the hall."
    scene black with fade
    pause .5

    scene Track with fade
    play music Busy
    pause .5
    MCT "I was not counting on a scavenger hunt today."
    MCT "And there's only a handful of students here. Doesn't really seem like club practice."
    "I sighed, scanning the track."
    "I didn't see anyone who bore any sort of resemblance to a teacher, much less a coach."
    "Nearby, I spotted a guy stretching beside one of the bleachers and walked to him."
    MC "Excuse me. You wouldn't happen to know where Naoki-sensei is, would you? Not around here, I'm assuming. I heard he was coaching out here today."
    Student "I... hmm..."
    Student "He is coaching our team, but he isn't with us today. I'd imagine he's coaching another club right now."
    MC "I..."
    MC "Right."
    UNKNOWN "Takeda-san! You're up!"
    Student "Try the auditorium. I think he has a club or two there."
    MC "Ah... thanks."
    Student "No problem. Later."
    pause .75
    MCT "For the love of-"
    "I turned on my heel and sped-walked my way back to the main building."
    MCT "I just came from there!"
    scene Auditorium with fade
    pause .25
    MCT "Well, at least this is something new."
    "I could hear the sound of a dribbling basketball from down the hall, and the sight of actual life here made me hopeful that Naoki-sensei would be somewhere associated with it."
    if isEventCleared("BE016"):
        "I did a quick once-over of the players, noting Sakie Iwata, the girl who I'd met back when Honoka played basketball, playing defense against a girl with rather plump thighs."
        MCT "I wonder if Honoka ever got around to having that conversation with everyone?"
        "I pondered this for a moment, and ran over my conversations with Honoka in my head."
        MCT "Well... I'll ask her sometime."
        "I walked along the edge of the gym toward the lone teacher I'd spotted in the room, leaning against one wall watching."
    if routelock == "AE":
        "I glanced over the players, noticing no one of note, save for a girl with rather large, jiggling thighs."
        "My eyes tracked her as she dribbled the ball along."
        MCT "Those shorts are a little... tight."
        pause .5
        "I blinked twice."
        MCT "Shiori would quite literally strangle me with both hands if she caught me checking another girl out like that."
    elif isEventCleared("GTS018") or getFlag("Meet_Fumika"):
        "I watched the players run back and forth down the court, only after a few passes did I spot Fumika Usui, the girl on a perpetual energy drink high, trying to shoot the ball over the head of a girl with... quite large feet."
        "I glanced down."
        MCT "The last time I saw her, her thighs were big. But now... those are huge. Especially compared to the rest of her."
        "I sighed, remembering against my will how hurtful she'd been to Naomi with her basketball club offer."
        "I resisted the urge to shake my head and walked along the edge of the gym, noticing a teacher up against one wall."
    "Walking closer, I noticed the height of this teacher. Though he seemed to be on the more mild end, he was still a good meter taller than me. And, based on his age, he couldn't be much older than Takamura-sensei."
    MCT "Was Naoki-sensei that tall? Did... he even have a factor?"
    MCT "... Whatever, I'll find out soon enough."
    pause .5
    MC "Pardon me?"
    Teacher "Mm? Yes?"
    if isEventCleared("MC006") or isEventCleared("BE046") or getFlag("Meet_Naoki"): 
        MC "Have you seen Naoki-sensei anywhere?"
        Teacher "I... well, I saw him this morning, but not since. I would try the faculty room."
        MC "Ah. Good idea, thank you."
        Teacher "No prob."
    else:
        MC "You're Naoki-sensei, correct? I just need your signature for this scholarship form thing."
        Teacher "Oh, I'm sorry. But, I'm not Naoki-sensei."
        Sugiyama "The name is Sugiyama-sensei."
        MC "Oh... oops. My apologies."
        Sugiyama "No trouble at all. Not the first time that's happened. 'S' last names and all that."
        Sugiyama "If you're looking for him, I'd maybe try the faculty room. If he isn't there, I'm sure someone might be able to point you in his direction."
        MC "Right... good idea. Thank you."
        Sugiyama "No prob."
    "I headed back around and toward the door, timing my walk so all of the players were on the opposite side of the auditorium while I passed. I did not need a basketball to the melon today."
    scene HallwayStairs with fade
    MCT "I swear... to all things sacred..."
    show HR unique with dissolve
    MCT "... Goddammit."
    show HR neutral
    HR "Good afternoon, Hotsure-san."
    show HR unique-2
    MC "Hey, Tashi-sensei."
    show HR neutral-2
    HR "You look... well less than your best if I'm being honest."
    show HR unique-2
    MC "Eugh... you wouldn't happen to know where Naoki-sensei is, would you? I can't find him anywhere, and I need to get this scholarship thing signed by him."
    "I held up the piece of paper to Tashi."
    show HR neutral
    HR "Mm. Well, he isn't in the faculty room. That much I can say."
    show HR neutral-2
    HR "Actually, unless I'm remembering incorrectly, he told me earlier that he's serving as the umpire for the softball game going on today. He's supervising two teams, so he wanted to get up close and personal to watch."
    show HR unique
    if routelock == "PRG":
        pause 1
        MCT "So I could have just gone to the game, spent a nice relaxing time with my girlfriend, and caught Naoki-sensei all at the same time?"
        MCT "I swear to God... I swear to..."
    MC "That helps a lot. Thank you, Sensei."
    "I bowed to him graciously, of which I truly meant it, and hurried off down the hall, some spring springing its way back into my step."
    scene School Exterior with fade
    play music ClearSkies
    "The baseball diamond was a bit of a walk from campus, but the breeze served to calm my nerves."
    pause .5
    "The distance, however... not so much."
    "My feet were {i}screaming{/i} from the incredibly unnecessary cardio."
    $setSkill("Athletics", 1)
    "Based on the amount of treading and retreading of the school that I'd done, I was sure that I could pinpoint any and every tile of flooring in those buildings by now, and know them all by first and last name, plus birthday."
    "I heard the crack of a bat, and watched a white sphere go flying up and away, followed by the smack of leather on ball."
    UNKNOWN "OUUUUTTT!!"
    MC "And there he is..."
    MCT "... Fucking finally."
    "I walked up to the diamond and glanced through the fencing around it."
    if routelock == "PRG":
        MCT "Well, I can't exactly head out there for his autograph right now."
        MCT "In the meantime, though, where is my darling?"
        "I turned toward the bleachers and glanced down toward the end."
        "Given that this was an actual game, I suppose I had expected a bit more of a turn-out."
        "As it was, I literally could count the amount of spectators on one hand."
        "Though, I would quickly run out of fingers."
        show PRG neutral with dissolve
        "I smiled, noting that half of the spectators were... well, unborn."
        show PRG happy
        "Aida waved at me from the end of the bleachers, and I hobbled down in front."
        MCT "At least I don't have to duck so I don't block people's view."
        show PRG neutral
        pause .5
        PRG "You look tired."
        MC "Eugh, you don't know the half of it."
        if checkAffection("PRG", ">", 13):
            PRG "C-Can I help?"
            MC "I appreciate it, but don't-"
            "My thought was immediately severed by Aida turning and kissing me on the cheek."
            MC "I-I... well, that does feel better now."
            show PRG blush-2
        else:
            PRG "I-I'm sorry..."
            MC "Eh, it's alright. At least I'm sitting now."
        MC "So, how's the game going?"
        show PRG neutral
        PRG "There was a home run a few innings ago. And someone stole second base the inning after."
        MC "Well, I wish I hadn't missed that. Crowd go wild?"
        PRG "Um... a few people cheered."
        PRG "But... there isn't really too much of a crowd."
        MC "Yeah, I noticed."
        PRG "So... how has your day been?"
        MC "Ah, I can tell you later. We have a game to watch, and I don't want to interrupt your viewing experience."
        PRG "Oh, I-I don't mind."
        PRG "I-I think that talking and having fun while watching is just as much fun as the game itself."
        MC "Hm... alright."
        MC "Well, basically I wanted to apply for that scholarship thing. You know the one, right?" 
        PRG "Y-Yes. I-I applied for it too."
        MC "So, when I went to apply, I still needed a signature from Naoki-sensei. And, the secretaries that were handling this whole thing in the main building told me that it would be faster if I went to get the signature myself."
        MC "So, since right before you texted me, I've been running around campus trying to find him."
        PRG "So... for the last two hours?"
        MC "Mhm. Saw like probably half of the faculty in that time. But no Naoki-sensei."
        show PRG worried
        PRG "Oh..."
        show PRG unique
        PRG "I-It's a shame you didn't ask. I could have told you he was here earlier."
        MC "Yeah... I really should've brought that up to you, come to think of it."
        show PRG neutral
        PRG "B-But, you're here now, right? You can get your signature, and then go turn it in right after."
        MC "Yeah... weight off my mind, I'll say."
        "I turned back to the diamond as she did, only then glancing at her."
        "Her belly had long since filled her lap. In fact, she long ago passed up the size achievable by most women."
        "Her baby belly jutted forward, with her breasts piled on top, in a way seeming to rest on top of Aida's belly."
        "In fact, she seemed to be hitting a bit of a growth spurt, as her legs were now spread well apart, to let her belly rest between them instead of on them."
        "Lastly, she had her back almost in the position of perfect posture. Were it not for being in public, I could have very well seen her leaning back into the next row of bleachers to give herself a back rest."
        MC "Oh, where are my manners? How has your day been?"
        PRG "I-It's been nice. After class, I went to my dorm and made some lunch, then did some laundry and came here."
        MC "Awesome. I'm glad to hear it."
        scene black with fade
        pause .5
        scene School Exterior with fade
        "A little under an hour later, the game came to an end."
        "The players bowed to each other, and made their way off of the diamond."
        MC "Well, that was a good one, hm?"
        show PRG excited with dissolve
        PRG "Yeah! The double play in the eighth inning was really exciting!"
        MC "Totally was!"
        "I glanced over, seeing Naoki-sensei going over to congratulate the winning team."
        MC "Well, time to get my autograph. At long last."
        show PRG worried
        "I got up, and beside me, Aida rose to her feet as well... though notably slower than me."
        PRG "Hngh... mnh..."
        show PRG neutral
        PRG "I-I'll come with."
        "I smiled at her, then pulled an about face to head toward Naoki-sensei."
        "From what I could see, Naoki was a little over my height, with a fairly trim stature."
        "He wore the standard athletic outfit with longer hair tied in a bun, and some light facial hair." 
        Naoki "-tastic strategy. You all really turned that around at the end."
        "I stopped close to the fence and waited for the players to clear out."
        pause .5
        MC "Excuse me? Say... mon-"
        Naoki "Hagh..."
        Naoki "Naoki-sensei, please."
        if not getFlag("Meet_Naoki"):
            $setFlag("Meet_Naoki")
        MC "Right. My apologies."
        MC "I was wondering if you could sign this for me? It's for my scholarship."
        MC "I had gone to apply, and the secretaries had every signature for my classes save for yours, and they told me that I should come find you to help expedite the process."
        Naoki "Oh. Oh, my-"
        Naoki "I... I'm very sorry to have put you through all of this trouble. That's something I should have taken care of, not you."
        Naoki "Yes, right away."
        "Naoki-sensei patted his front pockets, then the pocket on his shirt."
        Naoki "You wouldn't happen to have a pen on hand, would you?"
        MC "... I didn't think to bring one."
        PRG "I-I have one."
        "Aida reached with her left hand up to her breast pocket, and with a bit of a stretch of her arm, managed to produce a pen, which she handed to Naoki."
        Naoki "Thank you, Kodama-san."
        PRG "Y-You're welcome, Sensei."
        Naoki "Alright..."
        "Naoki-sensei pulled one leg up and pressed the paper to it, using his thigh as a makeshift clipboard."
        "He signed his name on the line, then halted before a short following line."
        Naoki "{size=-6}Today's date... or... end of July for the due date?{/size}"
        Naoki "{size=-6}Mn... today's. Best not to upset those harpies from the secretariat's nest.{/size}"
        pause .5
        Naoki "Right. Here you are."
        "Naoki-sensei passed me my now completed form, and handed Aida her pen back."
        MC "Thank you very much, Sensei."
        Naoki "Yes. Is that everything you have for me?"
        MC "I believe so, yes."
        Naoki "Good. Then, I wish you both a pleasant day. I've a track team to monitor."
        MC "You as well, Sensei."
        "Aida and I both bowed to him, as he hurried off on his way."
        PRG "Feel better?"
        MC "You have no earthly idea."
        PRG "Are you... going to go turn that in now, then?"
        MC "You bet. I can't wait to not have to worry about this damn thing anymore."
        PRG "W-Would you like me to walk with you to the administration office? I-I don't have any plans until later."
        MC "Sounds like a plan. Let's move."
        pause .25
        scene black with fade
        pause .5
        scene Campus Center with fade
        pause .25
        MC "You know, I didn't know you were in one of his clubs."
        show PRG worried with dissolve
        PRG "Naoki-sensei?"
        MC "Mhm. He knows your first name, but doesn't really seem to remember mine."
        PRG "Ohh..."
        PRG "A few weeks ago, I-I was having lunch in the cafeteria with Michiko and Sakura. I... I think it was a Saturday?"
        PRG "A-Anyway, Michiko had to eat fast so she could get to the pool. She was going swimming with her roommate, if I remember correctly." 
        PRG "She left in such a hurry though, that she forgot her cell phone at the table."
        PRG "S-So, I offered to take it to the pool, and left it with Naoki-sensei."
        MC "Aw. Well that was nice of you."
        show PRG unique-happy
        PRG "I-I just wanted to help."
        scene Hallway
        show PRG neutral
        with fade
        PRG "B-But anyways, while I was there, he... he asked me if I wanted to join the swimming club, not realizing I was already with the cooking club."
        MC "Ahh. What did you tell him, then?"
        PRG "I-I told him that... I couldn't. That I didn't want to give up cooking. He understood, of course."
        PRG "B-But even still, he asked me if I would be interested in swimming sometime. Even if I'm not officially on the team, I could still use the pool."
        PRG "I had heard of it already, but water aerobics are supposed to be really beneficial when you're pregnant."
        MC "That does make sense, and I think I've heard of that too. Gonna give it a try?"
        show PRG worried
        PRG "I-I might. I'm... really not sure, though."
        show PRG unique
        PRG "I... I just want to make sure that I don't lose any mobility or anything as I grow..."
        MC "It sounds like a smart idea, then. Let me know if you decide to go for it, and I could try it with you."
        show PRG neutral
        PRG "Are... are you pregnant too?"
        MC "I... it's for moral support! I promise I don't have a uterus!"
        show PRG excited
        PRG "{i}Snrgh!{/i}"
        "Aida covered her mouth with one hand to hold back a laugh."
        scene Gate Front
        show PRG neutral
        with fade
        MC "Kinda trippy being back here, huh?"
        PRG "Mhm. Before I submitted my scholarship paperwork, I-I hadn't been here... since I first arrived."
        MC "How much earlier did you get here before me that day?"
        show PRG worried
        PRG "Um... I got here that morning. I dropped off my suitcases in my dorm, then went with Alice to our homeroom."
        MC "Feels like a lot has changed since then, huh?"
        PRG "Yes..."
        PRG "But... it hasn't been bad."
        PRG "... Stressful sometimes, yes. But... not bad."
        show PRG neutral
        "As we stopped walking in the middle of the entry hall, Aida slipped one hand into mine, and I turned to face her head-on."
        PRG "A lot of good has happened here, too."
        MC "You can say that again, Sweetheart."
        show PRG blush-2
        PRG "Y-You should go turn in your scholarship forms."
        MC "I know. I'll get this done, then maybe we could talk on the phone later tonight or something? After your plans, of course."
        show PRG neutral
        PRG "O-Okay."
        MC "What are these mystery plans, by the way?"
        PRG "A-Alice and I are making brownies and catching up. With her being gone, then us being away, then just... being busy, we haven't had much time to talk."
        MC "Ahh, I ran into her earlier. Tell her I say hey."
        MC "Anyway, text me when you're all set, and we can chat later."
        PRG "'Kay."
        "I smiled and glanced around, noticing only right then how close we were to the principal's office and the administrative wing."
        show PRG aroused
        "I took Aida's hand and pulled her back into the adjoining hall for just a moment."
        "I came in close and wrapped my arms around her belly, then leaned in over her for a kiss."
        "Aida craned her neck up, pushing back against me with her lips. The way our faces were shaped, Aida's jaw and chin seemed to interlock with mine, almost. As though our faces were the perfect shape for each other."
        MCT "I have a feeling I'm going to have to start going from the side soon. I'm getting boxed out from the front."
        pause .5
        MCT "Not that I'm complaining."
        "I pulled back just a bit from Aida and stood there, my arms still around her belly."
        MC "I'll see you later, okay?"
        show PRG blush-2
        PRG "O-Okay. B-Bye."
        "My hand received a welcome squeeze as I let go of our embrace, letting Aida head off down the hall."
        hide PRG with dissolve
        "I watched her walk away, noticing the ample shake that came from her backside as she made her way down the hall."
        "Smiling like an award winner, I turned and walked across the entry hall."
    else:
        MCT "Well, I can't exactly head out there for his autograph right now."
        "I walked to the bleachers and took a seat right in the front row."
        MCT "These teams have to be made up of just students from here, right? So... is it just the same two teams constantly against each other?"
        MCT "Can they like... trade players?"
        "I watched the game go on as the player at bat let two balls fly over the plate, before swatting the third far out to left field."
        MCT "Eesh... must be real easy to accidentally bean the batter."
        "I glanced up as a girl who was clearly dealing with a breast factor came up to the plate next."
        "She bent in a slightly awkward stance, but held up the bat."
        "I leaned back in the empty bleachers, using the row behind me as an armrest/backrest, and glanced down a bit."
        "The stands were empty. Well, nearly. Maybe a few meters away, a girl and guy sat, watching the game, the two hand in hand."
        MCT "Huh. I guess other people find romance here as well."
        "Down from them, a heavier set guy sat, a laptop on the bleacher beside him as he watched the game."
        "A few more seats down, a more muscular girl sat, leaning forward intently watching."
        "From behind this girl, however, a sort of... white sphere stuck out."
        "From where I was, I couldn't tell if it was a boob or a ball, or... what exactly."
        "The muscular girl leaned back in the way I was, her arms on the bleachers behind her."
        pause .5
        show PRG neutral with dissolve
        pause .25
        MCT "Oh, it's-"
        if isEventCleared("PRG007"):
            MCT "Kodama-san? What's-"
            MCT "Oh, that's right. She's super into baseball. Almost forgot that."
        else:
            MCT "Wait, Kodama-san? What's she doing here?"
        "I heard the crack of a bat as the next player shot a pop fly off the bat, and straight into right field, where it was caught easily."
        "Aida followed the ball through the air with her eyes, watching the player pluck it from the air."
        show PRG happy
        "She was sitting straight up, with the hand I could see from my side resting on her skirt. She, along with one or two other people, applauded politely as the players changed sides."
        MCT "God... she's huge."
        MCT "Seeing her in class... yeah. I can see it there too."
        MCT "But seeing her outside of the desks and aisles, sitting on a bench showing it all..."
        MCT "And in a few months... she's going to be even bigger."
        "Aida was focused hard on the game. She hadn't noticed me, or really anything going on outside of the baseball diamond."
        MCT "I could go talk to her. It'd be a nice reprieve from zig-zagging around campus."
        menu:
            "Go talk to Aida.":
                $setFlag("MC024_PRGTalk")
                "I waited till the current batter managed to take a base off of balls, then headed across the walkway in front of the bleachers."
                if checkAffection("PRG", ">", 4) or getFlag("MC009_PRGTalk"):
                    show PRG neutral
                    "As I drew closer, Aida glanced to her left."
                    show PRG happy
                    "She smiled at me, and waved politely."
                else:
                    show PRG neutral
                    "As I drew closer, Aida glanced over."
                    "She smiled up at me, as I sat down close by."
                MC "Hey, Kodama-san!"
                show PRG neutral
                PRG "H-Hello, Hotsure-san."
                if isEventCleared("PRG007"):
                    MC "How's the game goin'?"
                    PRG "I-It's a really close game. They're dead even."
                    MC "Wow. Mind if I watch with you?"
                    PRG "P-Please do."
                else:
                    pause .5
                    MC "I uh..."
                    MC "I'm... kind of surprised to see you here."
                    show PRG unique-happy
                    PRG "I-I... I really enjoy baseball."
                    MC "Seriously? I never knew that."
                    PRG "Mhm. I-It's my favorite sport."
                    MC "Wow. Well, mind if I watch with you then? It's been awhile since I watched a game live."
                    PRG "Y-You can, if you'd like."
                show PRG neutral
                "I smiled and turned forward, watching as the current batter swung at... nothing, the ball flying straight past and into the catcher's glove."
                if isEventCleared("PRG007"):
                    MC "Correct me if I'm wrong, but your favorite team is... the Koi, right?"
                    PRG "Y-You remembered!"
                    MC "Of course! So, are you into any other teams?"
                else:
                    MC "So, if I can ask, what is it that you enjoy so much about baseball? Like, what's your favorite part of it?"
                    PRG "Um... that's a hard question."
                    MC "Hm. Well, what's your favorite team, then?"
                    PRG "The..."
                    PRG "... The Kanagawa Koi."
                    MC "Oh, cool. I... don't believe I've heard of them."
                    PRG "T-They've been my favorite team since I was little."
                    MC "That's so awesome. Are you into any other teams?"
                PRG "Um... I don't follow any others like I do the Koi. B-But, I do enjoy the game no matter who's playing."
                PRG "T-That probably sounds a little... stereotypical for me to say."
                MC "No, not at all. I get that too."
                PRG "Do you watch a lot of baseball?"
                if isEventCleared("PRG007"):
                    show PRG worried
                    PRG "I-I may have asked you that when we talked before. I... I can't remember."
                    MC "Hah, no worries."
                MC "I have watched some in the past, yeah. Not really anything that I would call habitual, but I knew the basics."
                show PRG neutral
                PRG "That's really all you need to understand, though. Even with that, you can figure everything else out so easily."
                "The two of us watched as the first baseman eased out from the base about a meter or so."
                PRG "See that?"
                MC "Hm? That guy stepping off of the base? Yeah."
                MC "Think we should let someone know about that?"
                PRG "Hm?"
                MC "That's illegal in baseball, isn't it?"
                PRG "Oh, no no. He's trying to steal second."
                MC "Oh, {i}that's{/i} stealing! I guess I never paid attention to the player getting ready to steal. I always just assumed he ran straight from base to base. Like, I didn't know he could ease into it like that."
                PRG "Mhm. Watch him."
                "The player took a few more steps. Up on the mound, the pitcher eyed up the batter."
                "Slowly..."
                "The runner took off, sprinting to second and making it just as the ball sailed to the second baseman beside him."
                show PRG happy
                PRG "He got it!"
                "Aida clapped her hands, which required her to reach over her breasts to actually bring her hands together... which in turn, landed her hands just under her face."
                "The pitcher gazed forward again and threw, the batter smacking the ball far out to center field as the runner on second took third, then hauled ass to home plate, sailing across with less than half a second to spare."
                show PRG excited
                PRG "YES!"
                "Aida applauded again, as a few other spectators, plus myself, joined her."
                scene black with fade
                pause .25

                scene School Exterior
                show PRG neutral
                with fade
                "About an hour later, the game closed out with both teams giving the classic ggs and so on."
                "One of the teams had managed to swing the game {i}hard{/i} in their favor, leaving the other in the dust."
                MC "That's what I call a game!"
                show PRG excited
                PRG "I-I know! That was a really intense final few innings!"
                MC "What did you think of that home run for three runs at the end?"
                PRG "T-That was my favorite part!"
                "I smiled at her, then glanced over, noticing Naoki-sensei congratulating the winning team."
                MC "Well, almost at my cue."
                show PRG neutral
                PRG "Uh... w-what?"
                MC "Oh, duh. I probably should have mentioned what brought me out here."
                MC "I'm applying for that scholarship thing, and I still need Naoki-sensei's signature. I was all over campus this afternoon looking for him."
                PRG "O-Oh my..."
                PRG "I... w-well, I think that the academy does a... really nice job with their financial aid. Not to mention their student social programs..."
                MC "Did you apply for the scholarship as well?"
                PRG "I-I did."
                MC "I'm sure you were a shoo in, in that case."
                PRG "I-I..."
                MC "Well, anyway, I'd better go get that signature then turn this in."
                PRG "A-Alright."
                PRG "I-I had fun watching the game with you, Hotsure-san."
                MC "Yeah! It was a great time!"
                MC "Have a good rest of your day, Kodama-san. Don't get into too much trouble."
                PRG "I-"
                MC "I'm kidding."
                show PRG blush-2
                pause 1
                hide PRG
                "Aida waved to me as I walked back down the bleachers, seeing my target finally in my sights." 
                $setAffection("PRG", 1)

            "Wait till after the game.":
                $setFlag("MC024_Wait")
                "I took a long glance over at her."
                "Aida's eyes were about as close to literally being glued to the action as possible. She had her hands folded, watching another batter eye up the pitcher."
                MCT "Nah. I'll wait till after the game."
                hide PRG with dissolve
                "I claimed a small section of unfilled bleacher for myself and sat. My feet were searing from the fevered tracking session around campus, and the breeze outside brought some traces of energy back to me."
                scene black with fade
                pause .5
                scene School Exterior with fade
                "Close to an hour later, the last batter struck out, and I glanced over at Naoki-sensei, who trotted across the diamond to congratulate the winning team."
                "I sat back again."
                MCT "I'll look like a real asshat if I just barge my way in. I've waited this long. A couple more minutes won't hurt."
                "In front of me, a few other students walked out from the bleachers."
                pause .5
                show PRG neutral with dissolve
                pause .25
                "At the back, Aida waited for the main group to move out, then began making her way out."
                show PRG surprised
                PRG "H-Hotsure-san?"
                MC "Hey, Kodama-san. Enjoy the game?"
                if isEventCleared("PRG007"):
                    show PRG neutral
                    PRG "I-I... I did. What did you think of it?"
                    MC "Oh, it was great! I haven't actually seen a baseball game in person for quite some time."
                    PRG "M-Me either."
                else:
                    show PRG neutral
                    PRG "I-I did. Um... I-I didn't know you liked baseball."
                    MC "I wouldn't call myself the biggest sports nut ever, but I definitely don't mind watching a game live."
                "Aida smiled as I stood up."
                MC "Mngh... stiff."
                PRG "H-Have you had a long day?"
                MC "Hah. You have nooo idea."
                PRG "W-What happened?"
                MC "Well, you know that scholarship thing that's being offered for grades?"
                PRG "Y-Yes."
                MC "So, I decided to apply for it earlier today. But, when I went to administration to finalize everything, they told me they were missing a signature from one of my teachers. Specifically Naoki-sensei's. From that handball thing we did."
                PRG "Oh... right."
                MC "So yeah... I've made circles around the school today. Like, you name a place, I've been there."
                PRG "T-That sounds..."
                MC "Annoying?"
                PRG "I... w-well, I didn't want to sound so negative, but... i-it does sound irritating."
                MC "Yeah. I asked a ton of people, but no one could tell me where he was. Not until I found Tashi-sensei anyway."
                MC "But anyway, I've complained enough. How has your day been today?"
                PRG "I-It's been going okay. I... I..."
                pause .5
                show PRG embarrassed
                pause .25
                PRG "... I did some laundry."
                show PRG neutral
                PRG "T-That's... about it."
                MC "... You're reminding me about my own laundry situation that I need to take care of."
                show PRG happy
                PRG "Ehehe!"
                show PRG neutral
                PRG "W-Well... I-I won't distract you anymore. I really hope that everything goes okay with your application, Hotsure-san."
                MC "Thanks, Kodama-san. Have a good rest of your day, okay?"
                PRG "S-Same to you."
                "Aida smiled at me in her usual kind, sweet manner, and continued on her way."
                hide PRG with dissolve
                "I watched her for a moment as she left, more just taking in her form as she waddled away. Only then did I turn back to Naoki-sensei, hearing various metal bats clanging against the fencing."
        MCT "This is it. All trials and tribulations end here."
        "I stood up and hurried to him."
        "From what I could see, Naoki was a little over my height, with a fairly trim stature."
        "He wore the standard athletic outfit with longer hair tied in a bun, and some light facial hair." 
        pause .5
        MC "Pardon me. Say... mon-"
        if not getFlag("Meet_Naoki"):
            $setFlag("Meet_Naoki")
        Naoki "Hahh... Naoki-sensei, please."
        MC "Right. My apologies, Sensei."
        MC "I was wondering if you could sign this for me? It's for my scholarship."
        MC "I had gone to apply, and the secretaries had every signature for my classes save for yours, and they told me that I should come find you to help expedite the process."
        Naoki "Oh. Oh, my-"
        Naoki "I... I'm very sorry to have put you through all of this trouble. That's something I should have taken care of, not you."
        Naoki "Yes, right away."
        "Naoki-sensei patted his front pockets, then the pocket on his shirt."
        Naoki "You wouldn't happen to have a pen on hand, would you?"
        MC "... I didn't think to bring one."
        Naoki "Urgh..."
        "Naoki-sensei patted his pockets once more, as if a ballpoint would just appear there."
        Naoki "Oh, there's one."
        "Naoki-sensei walked past me to the bleachers and bent down, plucking a pen from the dirt and wiping it off on his pants."
        Naoki "Right... I'm sure the owner won't mind helping another student."
        "Naoki-sensei pulled one leg up and pressed the paper to it, using his thigh as a makeshift clipboard."
        "He signed his name on the line, then halted before a short following line."
        Naoki "Today's date... or... end of July for the due date?"
        Naoki "Mn... today's. Best not to upset those harpies of secretaries..."
        pause .5
        Naoki "Right. Here you are."
        "Naoki-sensei passed me my now completed form, and pocketed the pen."
        MC "Thank you very much, Sensei."
        Naoki "Yes. Is that everything you have for me?"
        MC "I believe so, yes."
        Naoki "Good. Then, I wish you a pleasant day. I've a track team to monitor."
        MC "Thank you, Sensei. Same to you."
        "I bowed to him as he hurried away. Wasting not a minute more, I practically sprinted for the administrative building, any pain in my feet well gone."
        scene black with fade
        pause .5
        play music Schoolday
        scene Gate Front with fade
        MCT "Yes. YES."
        MCT "Whatever deity happens to be listening, thank you thank you thank you."
        "I hauled across the entrance hall and right for the administration offices."
    scene Info Desk with fade
    MCT "This is the most triumphant I will ever feel."
    "I walked in, ready to slam my paperwork down on the counter and walk off into the sunset. Possibly ride, if given the opportunity."
    "The three secretaries were in a cluster at the back of the room behind the desks, all whispering to each other, bearing more than a passing resemblance to gossiping students in the hallways."
    "I stepped up to the desk I'd been helped at earlier, and craned my neck a bit."
    Secretary1 "... Oh, you're doing Halloween parties?"
    Secretary2 "Are you dressing up for it?"
    Secretary1 "You kidding? Why? I have a career to uphold."
    "I raised one hand up in a pseudo attention-getting move."
    "The secretaries didn't make a single motion toward the desk, not even seeing me."
    Secretary3 "I forget you've only been here a few months."
    Secretary3 "The Academy does a few parties like those throughout the year. They're fairly popular."
    Secretary2 "It's always fun! I love this time of year. The parties, pumpkin carving, all of it is wonderful. Though I do look forward to the pumpkins the most, I'd be remiss to say that I won't be admiring costumes."
    MC "{i}MMG-CHM!{/i}"
    "The three of them glanced over, the smiles on their faces falling to blank dissociation."
    Secretary2 "If you can't see the sign on the desk, we're on break."
    "I glanced at another counter, where a laminated sign was posted."
    MCT "Oh, what the f-"
    MC "How much longer?"
    Secretary2 "As long as it takes. A break is a break."
    MC "... Fine. Could I at least have form A38 to fill out while I'm waiting around?"
    "The secretary raised one eyebrow and nodded to the sign, then turned back."
    Secretary3 "I did hear that that Hitomi-san is planning her wedding this winter, too."
    Secretary1 "She did not!"
    Secretary3 "She did. Apparently, her fiance moved from the mainland to the town here and found himself a job and everything."
    Secretary1 "My husband won't even do breakfast in bed for me..."
    "I sighed, possibly a bit more audibly than I had planned, and sat in a chair in the corner, nearby a coffee table and some other chairs, clearly set up for waiting students."
    $setTime(TimeEnum.EVE)
    scene Info Desk with fade
    play music LastBell
    pause .75
    Secretary1 "-Saw her the other day. She looked over the moon."
    Secretary2 "I would be, too. A new home and marriage all at once is cause for celebration."
    "The three secretaries glanced at the clock and stood up, all taking their positions."
    "I waited about... three-ish seconds and stood up, walking back to the counter with a stiffness that I doubted hid my impatience."
    MC "I have the grades all of my classes and all of the signatures that I need and I would like to apply for the scholarship... {w}please."
    Secretary2 "Ah. Well, you don't have everything yet."
    Secretary2 "Any and all changes to the grade protocol must be authorized by the principal."
    pause 1
    MCT "... Why wasn't I told this earlier today?"
    MC "Alright... what's the procedure?"
    Secretary2 "Our office collects all of the documents at the end of the day and sends them to reception at the principal's office, which the principal checks in the morning."
    Secretary2 "We can take care of it for you tomorrow during our office hours, or, since you've already gotten Saemonsaburokouji-sensei's signature, you can talk to him yourself right now and get his authorization." 
    "I glanced down at the paper."
    pause .5
    MCT "I've already done so much for this damned thing..."
    MC "I'll get it myself."
    pause .5
    "I didn't even bother to wait for a reply."
    scene Gate Front with fade
    play music Sunset
    pause .75
    MCT "Okay... where was that?"
    MCT "I just saw it like... two hours ago? Three?"
    MCT "Agh... can't even keep track anymore."
    "I walked along the outskirts, until I came upon a large door with a plaque. On it was the words \"Principal's office.\""
    MCT "Least this part didn't take half the day."
    "Normally, I would've at least knocked, but I was in no mood."
    "Inside was an entry lobby, with a small desk with a woman seated at it, going through some paperwork. Behind her were some filing cabinets and a large wardrobe."
    MC "Excuse me?"
    Receptionist "Good afternoon. Here for the principal?"
    MC "Yes, I am."
    "I set my form down on the desk and slid it to her."
    MC "I was going to apply for the scholarship today, and I... I mean my forms didn't have Sae... Naoki-sensei's signature, so I had to go find him and..."
    MC "I... I'm sorry. Here's my form."
    MC "I just need the principal to authorize it."
    "I glanced up for a moment, following a shadow from the corner of my eye that seemed to move by the wardrobe."
    MCT "God, I really am that tired."
    Receptionist "Yes, of course. One moment, please."
    "The receptionist got up and walked into the nearby double doors."
    pause 1
    show RM neutral with moveinright
    with vpunch
    RM "{size=-6}Gah! Hagh...{/size}"
    RM "{size=-6}T-Thanks. I've been stuck with my leg up by my waist for the last half an hour.{/size}"
    "Thanks to my advancing grogginess, I was hardly surprised to see Daichi wrestling himself from the inside of the wardrobe."
    MC "{size=-6}... Yeah, I got nothing. I've had enough wildness today. Even though this takes the cake for that.{/size}"
    pause .5
    MC "{size=-6}Should I even ask?{/size}"
    RM "{size=-6}Mm. Probably not.{/size}"
    "I watched Daichi straighten up the wardrobe, then make his exit."
    hide RM with dissolve
    MCT "..."
    MCT "I'm not even surprised anymore."
    if isEventCleared("MC005"):
        MCT "Somehow, slightly more elegant than the bush during Golden Week."
    "I shook my head, and took a chair near the desk, and waited patiently."
    pause .75
    "A few minutes later, the receptionist emerged from the office."
    Receptionist "The principal would like to speak with you, Hotsure-san."
    "My stomach flipped just a touch as I stood."
    MCT "Going into a principal's office never feels good..."
    "I walked to the door and through it, noting another plaque by the door that read \"Manabu Noguchi, Seichou Academy Principal.\""
    scene Principal Office with fade
    "As the door shut behind me, I glanced forward into the room."
    "Large windows let the waning sunlight into the room, as the principal sat behind the large desk in the room, jotting something down on a pad of paper."
    "He looked about the same as he had at the assembly near my beginning at the academy. He had short gray hair, with some balding in the middle, and he wore a clean looking suit."
    "I glanced at him, standing a couple of meters or so from his desk."
    MCT "Weird. Now that I think of it, it's almost unusual for him to not have a growth factor himself..."
    Principal "Feel free to have a seat. I'll be with you in just a moment."
    "The principal waved absently at one of the chairs in the room, and I sat right away, keeping my paperwork on my lap."
    pause .75
    Principal "There we are..."
    pause .25
    Principal "My apologies. How may I help you?"
    MC "Yes. My name is Keisuke Hotsure. I'm applying for the scholarship that's being offered and I was hoping you could authorize my paperwork for me."
    "I set my files on the desk, to which the principal slid them over to himself and leafed through them."
    Principal "I see."
    Principal "How has your experience been here so far, Hotsure-san?"
    MC "My... experience?"
    MC "Well... you have a very nice office. And your receptionist is quite nice."
    Principal "Oh, no no. I was referring to the academy as a whole."
    MC "Oh... yeah."
    MC "My apologies, Sensei. I... I've spent most of today chasing down a signature for this scholarship paperwork. I'm afraid I'm not the most alert mentally at the moment."
    "The principal had set my paperwork down and was giving me his full attention."
    "He nodded and smiled at me, his eyes warm and friendly despite his formal appearance."
    Principal "Ah, I can understand. For something so simple, a signature can be quite the hassle."
    MC "You've no clue, Sensei."
    Principal "I think I just might."
    Principal "However, in any case, has all been well with you? Acclimation going okay?"
    MC "I... would say so, yes. Thank you for asking."
    MC "The first few weeks were tough, I won't lie. But, I have been enjoying my time here."
    Principal "I am glad to hear that. As I'm sure you're well aware, all the faculty are here to help, should you need any support."
    Principal "However, the most important thing is acceptance, and being willing to take action yourself to assure your own well being."
    Principal "We can give you the tools, but your hands are the ones who will use them."
    Principal "Though, I'm sure you've heard the same from your homeroom teacher."
    MC "Tashi-sensei did say something along those lines, yes."
    Principal "I figured as such. I couldn't help but notice that you were in his homeroom."
    Principal "Very knowledgeable man. Straightforward and to the point as well, though he's always been that way."
    Principal "History was always his forte, as well. Even during his time here."
    Principal "Speaking of, I have actually heard a bit about his class already."
    MC "Oh? Well, I hope only good things."
    Principal "Oh, of course. No need to fret."
    Principal "Though, I have heard that there are only two male students in that particular homeroom."
    MC "Tashi-sensei mentioned that?"
    Principal "He did. Specifically, if I'm to use his phrasing, he mentioned a \"level-headed one\" and a... well, an \"eccentric one.\""
    Principal "And you are... which?"
    MC "I..."
    Principal "Ahaha! Only rhetorical, Hotsure-san. As they say, \"{i}acta, non verba{/i}.\""
    Principal "I had heard some good reports from Tashi-sensei about this level-headed one, so it's wonderful to finally associate a name to the face."
    "Principal Noguchi gave me a smile and a nod, then flipped open my paperwork, and taking a pen to sign with."
    "I glanced down at his desk. Far neater than what I would've expected from the administrator of the entire Academy, his desk was well organized and polished, much like that of a well worn businessman."
    "Near one corner was a picture frame, showing Principal Noguchi kneeling down with a younger girl, likely no older than eight years old."
    "Principal Noguchi was smiling proudly, the little girl clinging to him."
    Principal "My granddaughter, Moriko-chan."
    Principal "She lives with her parents off in Kobe."
    Principal "Due to the hecticness of the Academy, I've only been able to see her two or three times a year. However, I do my best to make time."
    Principal "She's just started elementary school this year, so of course, I get to hear all about her adventures there."
    MC "You must be a proud grandfather, then."
    Principal "Oh, of course! She's her grandfather's girl! The apple of my eye, if you will."
    "Principal Noguchi placed a stamp beside the grade protocol, and handed my papers back to me."
    Principal "Here you are. I do apologize for the wild nature of this whole matter, though I can't say I'm surprised by it."
    Principal "This isn't the first time this sort of thing has taken place."
    MC "No harm done, Sensei. Thank you very much."
    Principal "You're quite welcome, Hotsure-san. Everything should be in order here now."
    MC "Thank you, Sensei. And thank you for your time."
    Principal "My pleasure. I'm glad to have met you."
    MC "I'm glad as well."
    "I stood up and bowed to him, then turned, my paperwork all but glued to my palm."
    MC "Thank you very much for your time."
    Secretary1 "You're welcome. Thank you!"
    scene black with fade
    pause .5
    scene Info Desk with fade
    pause .5
    play music LastBell
    MC "Here you are."
    "I walked right up to the woman who had been helping me and set the paperwork down in front of her, ready to be rid of the infernal thing."
    Secretary2 "Thank you."
    "She clicked her nails against her keyboard, the prehistoric aged printer clunking to life and spitting out a sheet."
    Secretary2 "Sign your name here, then specify here that form B-1 is added in as an attachment."
    MC "Thank you."
    "I gripped one of the pens tightly, and quickly jotted my name down on the first line."
    pause .5
    "A first line that clearly indicated \"Last Name.\""
    MCT "..."
    "I sighed, then looked back at my full name, written out on the first name line."
    MC "... Do you have another form, please?"
    jump daymenu

label MC033:
    scene Dorm Interior with fade
    play music MC
    "Just another day, nothing really all that exciting. {w}I had to buckle down to start studying for this trimester's finals though. But that was no fun. I needed a distraction."
    "{i}*Bzzt Bzzt*{/i}"
    if checkAffection("TM", ">=", 6):
        MCT "Speaking of a distraction... A text from Tomo?"
        TomokoCell "<Hey Bro>"
        "What a coincidence, just when I was looking for something to do."
        MCCell "<Yo. What's up?>"
        TomokoCell "<I feel sick today. Can you drop off my homework today so it won't get counted as late?>"
        MCCell "<Sure, no problem. I'll be on my way shortly.>"
        MCT "Not exactly what I had in mind, but I hope she's alright. Honestly I think she could use a little more fresh air now and then and maybe she probably wouldn't have gotten sick."
    else:
        MCT "Looks like I got a text from Tomo. Not exactly the distraction I was looking for. Must mean she either wants something or she's dying."
        TomokoCell "<Hey Bro, I feel sick today. Can you drop off my homework today so it won't get counted as late?>"
        MCT "Called it."
        MCCell "<What's in it for me?>"
        TomokoCell "<I'll tell Mom if you don't.>"
        MCCell "<I suppose I'll be a good brother and help you out. I'm on my way. See you soon.>"
        MCT "Kind of annoying, but not the worst thing that could have come up."
    scene black with fade
    pause .5

    scene Dorm Hallway with fade
    play sound Knock
    "After a short delay, Tomo answered the door."
    show Tomoko neutral with dissolve
    extend "Wearing a blanket no less."
    MCT "Yikes. She looks like shit. I guess she wasn't kidding. Glassy eyes, red nose, that and she's practically shivering— I probably shouldn't stay long or I might catch what she's got."
    Tomoko "Gnhey. Nhere's my omework that was du taday. Can yu get me thu class assignments fum the tweachers so I dwon't fall behind?"
    MC "You sound really stuffed up."
    Tomoko "Ey gnow."
    if checkAffection("TM", ">=", 9):
        MC "Don't worry, it's no problem, but why don't you ask Yuki-san? You share the same classes."
    else:
        MC "Don't worry, it's no problem, but why don't you ask your roommate?"
    Tomoko "Who do yu thenk guve me twis cold? Fwigures, she can't keep awnything to herswelf anyway."
    MC "Ah, gotcha. Well that sucks."
    Tomoko "Oy, there's one uther thwing. I ned you to gwive this form to Takamera-sunsei. It's the lawst day to regaster for electwives for the mext trimester of cwlasses."
    MCT "I'd ask why she waited so long but I'm almost as bad of a procrastinator as she is."
    MC "Alright, I'll make sure this gets taken care of. Feel better Tomo."
    Tomoko "Twhanks. It's mot so bad. I dun't feel well enough to goo to class, but I still weel alright unough to play wideo games."
    MC "Still though, get some rest. Not like I need to tell you that."
    Tomoko "Dhat's not a bad idea. I do feel tiired."
    MC "Heh, I figured. Later."
    Tomoko "Later."
    scene black with fade
    pause .5

    scene Classroom with fade
    "I did my best to track down the various teachers before I had class, but didn't quite make it to all of them. I'd have to catch up with them later. I had my own classes to get to."
    pause 1
    show HR neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    HR "Alright, I'm feeling generous, so no new assignment since you have a quiz on the Azuchi-Momoyama period next class."
    show HR unique
    show BE happy at Position(xcenter=0.75, yalign=1.0) with dissolve
    BE "Yes!"
    HR "Don't count on it in the future though."
    show HR unique
    show BE angry
    BE "Boo!"
    show BE shrug
    show HR neutral
    HR "I heard that."
    show HR unique
    play sound ClockTower
    hide BE with dissolve
    "Finally, class was over. But I still needed to track down the rest of the teachers for Tomo."
    MC "Tashi-sensei, I gave you Tomoko's homework earlier, but I'm still trying to track down a few more teachers to give them her homework and get the new assignments."
    MC "I tried to find them this morning but they weren't around. Do you know where they might be?"
    show HR neutral at altMove(0.5, 0.5)
    HR "Who are you looking for?"
    show HR unique
    if isEventCleared("MC009") or isEventCleared("PRG030"):
        MC "Takamura-sensei. I checked the cooking room before class this morning but I didn't find her there."
        show HR neutral
        HR "Hmm, she was probably busy with what she's been working on to help with the school's counseling program."
        HR "You probably won't find her there now since it's the lunch period. Just follow me, we can probably find her in the faculty lounge."
    else:
        MC "Takamura-sensei. I didn't see her in her room before class this morning."
        show HR neutral
        HR "Did you check the kitchen? She's usually there if she's not in her home room. Unless she's pulling double duty with helping the school counselor."
        show HR unique
        MC "No, I didn't. I'll go check now."
        show HR neutral
        HR "I'd hold off on that. It's lunch period now. Just follow me, we can probably find her in the faculty lounge."
    if isEventCleared("MC002"):
        HR "It wouldn't be the first time you got to step in there."
    scene HallwayStairs with fade
    "I followed Tashi-sensei to the faculty lounge, but stopped just short of getting there when we heard an argument breaking out between students. And these guys were big."
    "Giant 1" "What did you just call me?"
    "Giant 2" "I called you a shrimp— shrimp. Get used to it."
    "Giant 1" "That makes no sense. I'm 296 centimeters tall."
    "Giant 2" "And I'm 318 centimeters. You're tiny compared to me, so know your place and get out of my way."
    show Takamura neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    Takamura "Now now, boys, that's not necessary."
    show HR unique with dissolve
    "Unfortunately, Takamura-sensei's polite warning was completely ignored by those two hot heads."
    "Giant 1" "You'll think I look pretty damn tall once I knock your ass to the floor!"
    "Giant 2" "Like your short little reach is going to let you land a punch on me."
    show Takamura strict
    Takamura "That's quite enough boys!"
    show HR unique
    "Tashi-sensei for his part just rolled his eyes impatiently as Takamura-sensei's more stern tone failed to instill any sense of threat to the two bickering goliaths."
    "I had to imagine he didn't want to undermine Takamura's efforts to handle the situation herself, but it was fairly obvious he was trying hard to hold his tongue... {w}At least, more so than usual in Tashi-sensei's case."
    "Giant 1" "Take a swing then if you're so confident."
    "Giant 2" "Is that an invitation?"
    stop music
    "{i}*clack* {w}*clack* {w}*clack*{/i}"
    "The previous ruckus suddenly faded into complete silence, save for the clipping of a pair of dress shoes echoing throughout the now still halls."
    show Hageshi neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    Hageshi "Mind what Takamura-san tells you, gentlemen."
    "Hageshi-sensei just walked on pass them, not even bothering to turn his head when addressing the two."
    "Giant 1" "Y-Yes H-Hagashi-sensei! {w}My apologies Takamura-sensei!"
    "Giant 2" "{size=-6}Like you're gonna do anything to me if I don't.{/size}"
    Hageshi "..."
    "Hageshi-sensei stopped dead in tracks, straighten himself up, only to turn his eyes towards the student with a very perplexed raised eyebrow."
    "Giant 2" "I-I'll be good. {w}S-Sorry Takamura-sensei."
    "Now recognizing their audience, both of the two would be brawlers bowed deeply at Takamura-sensei."
    show Takamura reassuring
    "Takamura-sensei in turn nodded and smiled."
    Takamura "I accept your apologies."
    show HR annoyed
    HR "Alright, get going you two. There's still half a day of classes. Go cool off somewhere else."
    show HR unique
    show Takamura neutral
    "The two students scrammed in separate directions after that."
    show HR neutral
    HR "Thanks for your help with that Hageshi-san."
    show HR unique
    play music HigherEdu
    Hageshi "What did I do?"
    show HR neutral
    HR "Heh. Like you don't know."
    show HR unique
    Takamura "Would you like to join us for lunch in the faculty lounge, Hageshi-san?"
    Hageshi "I'll take you up on the offer another time. I was going to monitor the cafeteria today. I find it helps to remind the students every now and then that someone is watching."
    hide Hageshi with dissolve
    "As Hageshi-sensei walked down the hall, Takamura-sensei's gaze shifted from him over towards me."
    Takamura "Oh, Hotsure-san! What a pleasant surprise."
    if isEventCleared("MC002"):
        Takamura "Here to visit us again?"
    MC "My sister is sick. She asked me to drop off her homework and get the next assignment from you."
    Takamura "Ah yes, I suspected as much. Both Hotsure-san and Utagashi-san were not in attendance this morning."
    Takamura "Thank you for letting me know. I will visit them later to see how they are doing."
    if checkAffection("TM", ">=", 4):
        MC "Thank you Takamura-sensei. I would appreciate that."
    Takamura "Well come in. I'll put her assignment in with my bag. The homework is a little tricky, I'll have to write out the instructions for you to pass on."
    MC "Actually, Takamura-sensei, it wasn't just that. Tomo asked me to give you this. She said it was a registration form for an elective class."
    Takamura "Oh, thank you Hotsure-san. I'm glad your sister decided to take me up on my recommendation for her to enroll in a new course that will be offered next trimester."
    Takamura "With her joining now there'll be enough students to offer it this time."
    scene black with fade
    pause 1

    scene Faculty Room
    show Takamura neutral
    with fade
    Takamura "I'm sorry you had to see that little incident earlier there Hotsure-san. Such things do not properly reflect the safe and supportive environment the school tries to offer with those going through these kinds of changes."
    show Takamura at altMove(0.5, 0.75)
    show HR neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    HR "All I can say is it's a good thing Hageshi-san showed up."
    show HR unique
    Takamura "Yes, while I do appreciate his effectiveness in such manners, I don't understand why the students are so afraid of him. He's such a sweet and kind person. I've never known him to hurt a fly."
    show Tsubasa neutral with dissolve
    Tsubasa "Beware the fury of a patient man, as the saying goes."
    Takamura "I'm not sure I'd use the word \"fury\" to describe Hageshi-san. I've never even heard him raise his voice."
    show HR neutral
    HR "Believe me Takamura-san, he's far from harmless."
    show HR unique
    Tsubasa "The true strength of a strong man comes from his ability to contain his wrath, not his willingness to unleash it."
    Tsubasa "He has matured well since his time as a student at the academy."
    MC "You had Hageshi-sensei as a student, Tsubasa-sensei?"
    "Finally turning his gaze up from the newspaper he was reading, Tsubasa-sensei only just now realized there was a guest in the faculty lounge."
    Tsubasa "Oh, hello there Hotsure-san."
    if isEventCleared("MC002"):
        Tsubasa "Come for another visit have we?"
    Tsubasa "To answer your question, yes. Tashi-san was one of his teachers as well. It may seem like half a lifetime to you, Hotsure-san, but eight years is not a very long time to an old man like myself."
    MC "What was he like as a student, if you don't mind me asking?"
    show HR neutral
    HR "Well for one, you wouldn't have recognized him back then. I can scarcely believe they were the same person myself."
    show HR unique
    Tsubasa "Yes, he was quite the sight for sore eyes, as they say. Not just figuratively, but literally as well."
    show HR neutral
    HR "He certainly stood out, and not in a good way. I'll never forget it. Fresh off the ferry, he had a black eye, a busted lip, and scraped up knuckles. He looked like trouble."
    show HR unique
    Tsubasa "Or attracted trouble, as seemed to be the case. His unusually diminutive stature at 151cm made him an obvious target for harassment and ridicule, along with a physique that looked like his last meal had been weeks ago."
    show Takamura sad
    Takamura "Oh my! That seems hard to visualize, knowing him now."
    show Takamura neutral
    extend " It's hard to imagine him being smaller than me even. I suspect he was still a good student though, in spite of those things."
    show HR neutral
    if isEventCleared("MC002"):
        MC "Wait a second, I thought you told me he was a nationally ranked judo athlete by the time he graduated high school."
        HR "Yeah, in the under 55kg class. Doesn't quite send the same message to students, so I tend to leave that part of the story out."
        HR "To hear him tell it, his parents enrolled him in martial arts classes from a young age because he got picked on so much."
    HR "When he first got here, he was very sullen and quiet. There was even a rumor amongst the students that he couldn't talk."
    HR "But he never had an issue with answering a question when called upon in class. Though I didn't know him to speak a word beyond that myself either."
    show HR unique
    Tsubasa "In that regard, not as much has changed."
    Takamura "He certainly fits the \"strong silent\" type."
    if isEventCleared("MC002"):
        MC "Sounds like he got picked on a lot, even here."
        show HR neutral
        HR "As faculty we do our best to stop that from happening when we see it, but as far as what I could piece together from other students, yes, quite frequently here as well."
        HR "It seemed like every other day he had a fresh gash or bruise on his body. {w}Despite his training, he still just looked like a scrawny kid."
        Takamura "Oh goodness! That sounds awful!"
        HR "I'm sure it was, but he was a tough kid. He never once tattled on anyone or even complained about being hurt."
    else:
        MC "I take it he got picked on a lot?"
        show HR neutral
        HR "As faculty we do our best to stop that from happening when we see it, but as far as what I could piece together from other students, yes, quite frequently too."
    show HR unique
    Tsubasa "Hmph. I never saw any such incident myself, but I suspect those who did pick on the poor young man were in for a nasty surprise once his factor started to manifest."
    MC "Yeah what happened later? Besides somehow growing over 40cm in less than a year?"
    show HR neutral
    HR "I take you're interested in his ugly duckling story?"
    show HR unique
    show Takamura strict
    Takamura "That doesn't seem like a nice way of putting it, Tashi-chan."
    show HR neutral
    HR "And how else would you describe it? If only we could all be so lucky..."
    show Takamura neutral
    show HR unique
    Tsubasa "Ah yes, Hageshi's growth factor. Rum thing really. He's certainly one of the more unique cases."
    MC "He is? How so? I thought he was considered \"small\" for a muscle growth factor."
    if routelock == "WG" or routelock == "FMG":
        Tsubasa "While this may be true, keep in mind your perspective is quite skewed from what you've seen with Mizutani-san and Okamoto-san."
    else:
        Tsubasa "While this may be true, keep in mind your perspective is quite skewed from what you've seen with Mizutani-san."
    Tsubasa "Hageshi-san's case is still remarkable with regards to the degree in which his height and size have increased relative to his starting point, at least among those with muscle growth factors."
    Tsubasa "It's a peculiar thing really. Most growth factors follow a fairly predictable trajectory, even if the final degree of development is unknown."
    Tsubasa "The different factors obviously have common elements, or else there would not be discernibly distinct types, as we understand them today. But, every so often, some of them possess their own little idiosyncrasies."
    if routelock == "WG" or routelock == "PRG":
        MC "You mean like how Nikumaru-san and Myoga-san look different, despite having the same factor?"
    elif routelock == "AE":
        MC "You mean like how Matsumoto-san and Yureno-san look different, despite having the same factor?"
    elif routelock == "BE" or routelock == "FMG":
        MC "You mean like how Inoue-san and Blackburne-san look different, despite having the same factor?"
    else:
        MC "You mean like how all the different giant students vary so much in height?"
    Tsubasa "Precisely. It's a peculiar thing, as interesting as it is maddening, if I'm being honest."
    Tsubasa "In all my studies of the factors, it's still not clear if the growths are influenced by the underlying physiology of the person or if they simply transform it entirely."
    MC "Is there something special about Hageshi-sensei then?"
    Tsubasa "A few things at least. He's unusually lean even among those with muscle growth factors that are known for their leanness."
    Tsubasa "I do not know if this is due to his body's natural propensity or the fact that he doesn't eat much. He never developed the prodigious appetite that typically characterizes other muscle growth students."
    if routelock == "FMG":
        MC "Huh, that is odd. You should see how much Akira eats. That girl can pack it away."
    elif routelock == "WG":
        MC "Huh, that is odd. Mitzutani-san eats a lot. Maybe not as much as Alice... but still a lot."
    else:
        MC "Huh, that is odd. Mitzutani-san eats a lot. Maybe not as much as Nikumaru-san... but still a lot."
    show HR neutral
    HR "He's also known to have remarkably fast reflexes. Then again, he was, and still is, a trained fighter. Maybe that has something to do with it besides his growth."
    show HR unique
    Tsubasa "It's a possibility I've considered as well."
    Tsubasa "Those are rather minor nuances of his condition by comparison though. THe most peculiar attribute of his is his unusual strength to bodyweight ratio."
    Tsubasa "Though rather small in size across the growth distribution of those with muscle factors, his strength approaches the level of some of the past record breakers."
    Tsubasa "I suppose in that regard I should come to expect these things. In all my years of studying the factors, just as we think a definitive pattern can be established, a new outlier like Hageshi-san seems to emerge."
    Tsubasa "{size=-6}Not unlike this current crop of students this year...{/size}"
    Tsubasa "It's fascinating, if not a bit disheartening at the same time."
    MC "I hadn't realized he was such a special case."
    show HR neutral
    HR "Yes, which is why I like to impress that fact upon students to dissuade them from causing trouble."
    show HR unique
    MC "Still though, some of those giant students are pretty big. Like those guys in the hall arguing earlier. Seems like even he would have trouble keeping them in line if they really wanted to press the issue."
    show HR neutral
    HR "Heh. Trust me, he's dealt with much worse than those two."
    show HR unique
    MC "Really? Like how big are we talking here?"
    Tsubasa "As Hageshi-san is fond of saying, \"The bigger they are, the harder they fall.\"."
    show HR neutral
    HR "We've probably said too much already. You'd have to ask him sometime, he might tell you."
    show HR unique
    Tsubasa "Hotsure-san, you do understand that we would not normally be at liberty to talk about another faculty member so freely when they are not present. We discuss these things for Aoi-san's benefit, as a colleague of Hageshi-san."
    Tsubasa "Not only that, but with the understanding that Hageshi-san wants his story and experience with his growth factor to be an inspiration and source of hope to students that struggle with theirs."
    Tsubasa "If you want to know more, I'd encourage you to talk with him yourself sometime."
    MC "Gotcha. Will do. I won't pry any further. Thanks for the history lesson Tsubasa-sensei and Tashi-sensei."
    Tsubasa "You're welcome."
    MC "For what it's worth, it does help to know that others have been through the same thing as students here, and come out the other side just fine."
    Tsubasa "I'm sure Hageshi-san would be happy to hear that."
    "Tsubasa-sensei returned to reading his newspaper, seemingly no longer interested in further conversation."
    Takamura "Oh, I almost forgot with this whole discussion, here's the assignment for your sister. I do hope she starts feeling better. If you see her before then, be sure to let her know I plan to stop by."
    MC "Thanks, Takamura-sensei. Sure thing. I'll get going now."
    scene black with fade
    pause 1
    scene Campus Center with fade
    "I was on my way back to Tomo's dorm when I came across someone I recognized from earlier. Sulking around like a whipped puppy."
    "Giant 2" "Stupid Hageshi. Everyone thinks he's so tough. He can't do shit to me, I'm nearly twice his height. Where does he get off giving me his stupid little stinkeye?"
    MC "..."
    "Giant 2" "Huh!?"
    MCT "Looks like he noticed me listening to him mumbling to himself."
    "Giant 2" "What are you looking at, pipsqueak?"
    "I should have just kept on walking, but I couldn't resist putting this whiney jackass in his place one more time."
    MC "You do realize you wouldn't even stand a chance against Hageshi-sensei right?"
    "Giant 2" "Just who the hell are you and where do you think you get off telling me that?"
    MC "He's taken down much bigger guys than you with ease."
    "At this point I was bluffing based off what I heard from Tsubasa-sensei and Tashi-sensei, but I could tell from earlier whatever he must have heard about Hageshi-sensei he believed too."
    "Playing it up was my best bet to avoid being on the receiving end of a pounding after opening my mouth."
    "Giant 2" "Is that so? Color me skeptical."
    MC "You had your chance to express your skepticism, but you backed off like a little bitch when all he did was twitch his eyebrow at you. Just move on with your life dude, and stop talking shit to people."
    "Giant 2" "How about I just pound you into the ground right now. What are you going to do about it when Hageshi-sensei's nowhere in sight?"
    MC "Do you really think starting something with me isn't going to end with him breaking his foot off in your ass?"
    "Giant 2" "{i}Arrgh!{/i} Just get lost."
    MC "Yeah I'm going... {size=-6}loser.{/size}"
    scene Dorm Hallway with fade
    play sound Knock
    pause 1
    show Tomoko neutral with dissolve
    MC "Here's your homework."
    Tomoko "Thanks, I guess. Not the most fun present."
    MC "Feeling better?"
    if checkAffection("TM", ">=", 6):
        Tomoko "A little. It's just a cold, it's not a big deal. I'll be fine."
        MC "You sound better. Still though, you don't look so good. I think you should rest more."
        Tomoko "You're probably right."
        $setAffection("TM", 1)
        Tomoko "I guess I'll rest up a bit before trying to get this homework done."
    else:
        Tomoko "It's just a cold. Not a big deal. Why do you care?"
        MC "Eh, I care a little. At least enough to ask."
        "I was at least relieved she didn't seem so stuffed up like she did this morning."
        $setAffection("TM", 1)
        Tomoko "Thanks."
        MC "You sound cranky. I can't believe I'm saying this, but maybe you need a nap."
        Tomoko "I probably should have taken a nap, but I was just playing games. I guess I'll rest up a bit before trying to get this homework done."
    MC "Sounds like a plan. I'll see you later Tomo. Feel better."
    Tomoko "Thanks Bro, later."
    MC "Oh, and Takamura-sensei said she planned on stopping by to check up on you."
    Tomoko "That's nice of her, I guess. Thanks for the head's up."
    MC "No problem."
    MCT "Can't say I'd be thrilled to see Tashi-sensei if he showed up at my door, but at least Takamura-san means well."
    "Tomo didn't say, and I didn't want to pry, but I was curious about this elective course that she seemed keen on making sure she made it in before the registration deadline."
    "If nothing else, it was a convenient opportunity to get to know the teachers a bit better."
    "I knew Hageshi-sensei was a tough customer from having him in class. But now I understand a bit more why the other students were so terrified of him if they were caught causing trouble."
    jump daymenu

label MC034:
    "This marks the current end of the Keisuke-centric scenes."
    "More are planned for a later release. Until then, feel free to explore the main routes."
    jump daymenu

label global005:
    $setTimeFlag("testday2")
    scene Dorm Interior with fade
    play music Schoolday
    pause .5
    play sound AlarmClock
    pause .5
    MC "Agh..."
    "I let a groan slip out from my lips as I swung my arm over to grab my phone and silence my infernal alarm."
    MC "Daichi? You..."
    "..."
    "I sat up in bed and looked around."
    MC "Huh?"
    MC "The heck is he?"
    "I put my elbows on my knees and rubbed my eyes."
    "Today, instead of normal classes, was something that Tashi-sensei had called \"Measuring Day.\""
    MCT "What exactly are we measuring anyway? Height or something?"
    "I got out of bed and staggered into the bathroom."
    scene Bathroom with fade
    "I did up my toothbrush and started scrubbing away at my teeth in a sleepy sort of manner."
    MCT "Is... Measuring Day about factors, maybe? Like, is it going to tell all of us what we're going to be dealing with?"
    MCT "Do I... even have anything?"
    "I finished with my teeth then examined my face in the mirror."
    "I didn't really have anything prominent that I could really imagine swelling like crazy on me, but then again, who said it had to be prominent?"
    MCT "Tashi-sensei did say we're here because we, or a sibling, have expressed a certain trait that causes unusual growth..."
    MCT "Wait, shit... what about Tomo?"
    MCT "What if she has something crazy? Like some sort of crazy muscle growing gene or something?"
    MCT "...{w} Or tongue growth."
    MCT "God..."
    scene Dorm Interior with fade
    "I walked back into my room and got uniformed up, then headed promptly outside, trying my damndest to keep my fears internalized."

    scene Hallway with fade
    play music Busy
    "As I made my way inside the classroom building, I glanced down the hall."
    "Up ahead were most of my classmates, all seeming to be waiting, much like I was."
    if getHighestAffection() == "BE":
        show BE neutral with dissolve
        BE "Hey there, Kei-chan! How are things going for you?"
        MC "Oh, pretty good. You?"
        BE "Still getting used to how big this campus is! I've been spending some time walking around each night and I still haven't seen it all!"
        MC "Wow, I haven't been around much either..."
        BE "Maybe we can go exploring together sometime!"
    elif getHighestAffection() == "WG":
        show WG neutral with dissolve
        WG "Hotsure-san."
        MC "Oh, hello Nikumaru-san."
        WG "Please, I've told you before, call me Alice. Formalities are for business, I find them so tiresome in normal conversation."
        MC "Er, okay, Alice... but you called me Hotsure-san."
        WG "Because you were expecting it, of course. In any case, I trust you are adjusting to your new setting. Settling into a new routine by now?"
        MC "As well as anyone I suppose..."
        show WG haughty
        WG "Good to hear. Some find adherence to a routine to be restrictive, but I find the gains in productivity from an optimized schedule to be far more freeing than leaving idle time for its own sake."
    elif getHighestAffection() == "GTS":
        "I noticed Naomi walking next to me as we made our way to class. Like, noticeably close."
        show GTS neutral with dissolve
        GTS "..."
        MC "Hey there, Yamazaki-san.."
        GTS "Oh, h-hello."
        MC "..."
        GTS "..."
        MC "Nice day we're having, yeah?"
        GTS "...Yes."
        MCT "Boy, she's not much for conversation today... but she seems happy."
    elif getHighestAffection() == "FMG":
        show FMG neutral with dissolve
        FMG "Keisuke! How ya doin'?"
        "I cringed as Akira slapped me on the back in what she probably thought was a friendly manner."
        MC "Hrrrk!"
        FMG "Haha, catch you by surprise, did I? Well, hopefully that'll wake you up a bit!"
        MC "It's nice to see you too..."
        FMG "Guess what I found out yesterday? They've got an outdoor weight area behind the gym! Can't wait to try it out!"
        MC "Does that make a difference?"
        FMG "Sure! Morning and evening workouts can go harder than normal because you're being naturally cooled by the cold air!"
        MCT "I boggled to think what a \"harder\" workout was for Akira, seeing how hard she already pushed herself..."
    elif getHighestAffection() == "PRG":
        show PRG neutral with dissolve
        PRG "H-Hello, H-Hotsure-san...!"
        MC "Oh, hi Kodama-san."
        PRG "H-Having a good morning?"
        MC "Yeah, I'd say so. Pretty typical day. You?"
        PRG "Y-Yes. I-It's g-good for me too."
        MC "That's good to hear."
    elif getHighestAffection() == "AE":
        show AE neutral with dissolve
        AE "Hotsure-san."
        MC "Oh, hello Matsumoto-san."
        AE "Good to see you on time. I may have need of your assistance later."
        MC "Oh?"
        AE "It's measuring day for our class. I might need help corralling the student bodies through the process in an efficient manner."
        MC "Er, all right, sure."
        AE "Thank you."
        MC "So, what exactly is Measuring Day all about, anyway?"
        AE "..."
        AE "You'll see."
    scene Classroom
    show HR unique
    with fade
    "When we got to Room 3-B, Tashi-sensei was standing at the front of the room. He nodded at us as we all came in."
    show HR neutral
    HR "Alright, everyone. Today is Measuring Day for this class."
    HR "In layman's terms, it's the day when you'll all learn the nature of your specific factor."
    HR "You'll be taken privately into separate areas, and have the basics of your factor laid out for you."
    HR "From there, the rest of today will consist of measurements and such, to essentially give each of you a starting baseline."
    show HR unique
    show WG neutral at Position(xcenter=0.8, yalign=1.0) with dissolve
    WG "Baseline?"
    show HR neutral
    HR "So, I'll be leading you all into the gym where everything will be occurring. Matsumoto-san, would you mind getting everyone together?"
    show HR unique
    show AE neutral at Position(xcenter=0.2, yalign=1.0) with dissolve
    AE "Understood. Everyone, please form a line at the door, single file, please."
    scene black with fade
    pause .5

    scene Auditorium with fade
    play music LastBell
    "The auditorium had been set up with what amounted to a field clinic, privacy dividers erected in a series of squares, with various testing and measuring devices set on folding tables."
    "I noticed that unlike at my previous schools, it seemed there were no student volunteers; every station seemed to be manned by a medical professional of some sort."
    show HR neutral with dissolve
    HR "Alright. Class 3-B over by this wall. Alphabetically, please."
    hide HR with dissolve
    show BE neutral with dissolve
    "I lined up by the wall near the front of the line, and due to the nature of the alphabet, Honoka was right behind me."
    BE "Nervous, Kei-chan?"
    MC "Ahh... maybe a bit? Helps that everyone here is in the same boat, though."
    hide BE with dissolve
    "I could see other classes lining up as well, but couldn't really make out any familiar faces among them. Not even Tomo."
    if isEventCleared("MC002"):
        show Takamura neutral with dissolve
        "That being said, though, I did see Takamura-sensei walk to the front of a group and get them settled into line, so Tomo was likely somewhere around."
        hide Takamura with dissolve
    "The lines were small, but given how thoroughly they were measuring everyone- I supposed being here meant there was a much wider set of variables that could be changing- each person took as long as several might at my older schools."
    "I didn't have much time to think about it, though- my name was one of the first few called up. I was directed first to a small cubicle in the corner, where I was to hear the specific results of my growth factor test."
    "I went into the little corner-cubicle, halting in my tracks as soon as the nurse turned to face me."
    Nurse "Hello, Hotsure-san, please have a seat."
    Nurse "My name is Hitomi Kiyomi. Or, as I usually go by, Nurse Kiyomi."
    "I sat on the stool, my amazement at the size of her lips only slightly eclipsing my amazement that she could talk without a lisp."
    "They were so enormous and puffy I literally couldn't see her chin, the top curve of her upper lip nestled against the bottom of her nose."
    "What was more, she had decided to cover them in bright red lipstick. It was nearly impossible not to stare as she looked down at a clipboard full of papers."
    Nurse "So, your growth factor has been confirmed to be..."
    Nurse "Heh, you like them?"
    MC "Ah... eh..."
    MC "No! I-I mean, yes! I-I mean... they're-"
    "Her lips actually managed to pull out into a smile, making nearly the entire bottom half of her face hidden behind them."
    Nurse "It's all right, I know they can be surprising. Whenever I go off-campus I have to wear a surgical mask or I can hardly do anything for all the gawking and questions."
    "I just nodded and looked away, wondering what I would have to do to live a normal life."
    Nurse "Anyways, your growth factor. According to these results, you have hyper-productive hair follicles."
    Nurse "Not hypertrichosis, so you don't need to worry about having to shave your nose and forehead and so on, but you'll definitely need a barber more often than most."
    MC "My hair? It's always grown like a weed, that's not really anything new."
    Nurse "Well, the degree is never certain, but remember that it's not fully manifested yet. Whatever rate of growth you're used to, it will increase by some amount, guaranteed."
    MC "And... and my sister? Does she have the same thing? Does she have anything at all?"
    Nurse "I'm sorry Hotsure-san, but I'm not allowed to share her medical information with anyone she hasn't specified..."
    MC "But I'm her brother..."
    Nurse "All the same, Hotsure-san. I can't."
    "I mulled over this for a few seconds while she wrote on her clipboard."
    MC "So, that's it? Is like every hair follicle on my body going into overdrive?"
    Nurse "Body and head hair grow at different cycles and intensities, so it's hard to say. But we'll be sure to check up on all of your growth throughout the year, so please try and keep a record of each time you cut any of your hair."
    MC "... Do I have to?"
    Nurse "No, but we're only here to help. If you're comfortable only knowing what you know now about your condition, we won't force you. But you still have to come in for measurements and such."
    MC "So, can I go?"
    Nurse "Right after we take some blood, yes. Just sit still and roll up your sleeve..."

    scene Auditorium with fade
    "I walked out of the nurse's cubicle, rubbing the cotton ball taped to the crook of my elbow. Next was the height and weight measurements, then an eye test, then several other stations I didn't even know the purpose of."
    "I craned my neck to see over the various heads."
    MCT "Who am I kidding? Tomo isn't that tall."
    MCT "But, come on... where is she?"
    "I walked on to the next station where my height and weight would be taken."
    scene black with fade
    pause .25
    scene Auditorium with fade
    MCT "God... still nothing."
    "About half an hour of measurements later, and I was free of all the poking and prodding."
    MCT "Where the hell is Tomo?"
    if isEventCleared("MC002"):
        show Takamura neutral with dissolve
        "I glanced off to one side and noticed Takamura-sensei with some of the members of her class."
        MCT "Takamura-sensei! Tomo's probably with her!"
        "I had to force myself to not sprint straight at her."
        Takamura "Hotsure-san? What's going on?"
        "Takamura walked forward as I came to her and put one hand on my shoulder, looking at me with a worried expression."
        show Takamura sad
        MC "I... do you know my sister's factor? I can't find her anywhere."
        Takamura "Oh... Hotsure-san, I'm afraid I can't give out that information. I'm very sorry."
        Takamura "That information is not public to allow each student to process the news at their own pace, and to allow them to disclose that information when they feel ready.."
        show Takamura neutral
        Takamura "I understand your concern. I do. However, your sister is another student as far as the academy is concerned, and these protocols have to be upheld."
        Takamura "If I were you, I would go see her this afternoon, and have a heart to heart with her. I'm certain that'll help ease your mind."
        MC "I... I see."
        MC "Thank you, Sensei."
        hide Takamura with dissolve
        "I turned and walked away from her, feeling slightly dejected."
        "I understood the logic behind it. The factors did affect some pretty personal things about each student."
        MCT "But come on! She's my goddamn sister!"
        "I let out a groan."
        MCT "Guess I'll find her later."
        jump daymenu
    else:
        "I glanced around one last time for any sight of my sister, then sighed."
        MCT "She should be here... what the hell?"
        MCT "Is it so hard just to get a damn answer?"
        MC "I... guess I'll find her later."
        jump daymenu

label global026:
    $setPregnant()
    scene Dorm Hallway with fade
    play music HigherEdu
    "I walked out of my door and turned to lock it, shoving my key down into my pocket while also throwing my bag over my shoulder."
    MCT "Dammit... the one day I mess up my alarm."
    "I headed off, not needing to run, but also not able to take my usual pace all the way to class."
    "I didn't think I was going to be late, but I had to speed up my routine that morning, resulting in a quick dressing and a complete disregard for my hair trim that morning."
    scene Dorm Entrance with fade
    MCT "I'm so trimming the hell out of my head when class is-"
    Student1 "Hey! Watch yourself!"
    MC "Ahp! Sorry!"
    "I stepped off to the side, in my haste, almost plowing into a group of four students, all walking to class together."
    "The four glanced at me, then continued on their way."
    "I followed behind them to class. Near the front of the group, one girl was talking to the other three, two of which were guys, while the last was another girl."
    Student1 "But anyway, I saw her this morning."
    Student2 "No way. I'd think people would've known about something like that before now. Like... come on."
    Student1 "That's just it. It came out of nowhere."
    "I normally tried my hardest to not eavesdrop... but they were literally {i}right{/i} in front of me."
    Student3 "So, wait. She just... walked out like that?"
    Student1 "Yes! Her roommate was with her, of course. The roommate gave me a hell of a dirty look, too."
    Student4 "Well, you were staring at her in the halls."
    Student1 "What do you expect?! We've all been here for a bit now. And {i}no one{/i} has grown like that!"
    Student1 "How could I not be curious?!"
    "The group continued on ahead of me, the other three students seeming to lay into the first one a bit."
    MCT "Huh... Wonder what they were talking about?"
    scene Campus Center with fade
    "As the group hit the center of campus, they dispersed, all heading off in different directions as I continued on."
    scene Hallway with fade
    "The halls were still filled with students as I entered, bringing a huge sense of relief as I saw that I still had some time."
    MCT "..."
    MCT "I should grab some water before class."
    "I turned for the cafeteria and hurried along, knowing I had a bit of a hike."
    scene Cafeteria with fade
    "When I got there, I put some yen into a machine and punched in the number for a bottle of water."
    "Usually, I'd just fill one up at my dorm. But, with my mad morning preparations, I'd completely forgotten that part, and my mouth felt like a seared dry desert."
    "Hearing the clunk of my bottle hitting the dispenser, I took it and unscrewed it, taking a long sip as I started walking."
    scene Hallway with fade
    "Reaching the hall once more, I passed more students heading to their classes."
    stop music fadeout 1.0
    Student1 "- some girl in 3-B."
    Student2 "Seriously?"
    "I turned my head, slowing down just a bit."
    Student1 "I heard she was totally fine like two or three days ago. Then she just like blew up."
    pause .5
    MCT "What the hell?"
    "I glanced back, seeing the two girls disappear down the hall together."
    MCT "I... guess Shiori's ass has been getting a bit more plump lately."
    MCT "The way they sounded though... almost makes it seem like something super drastic."
    MCT "And it's something that appeared overnight. Did a girl grow to like five meters tall and sprout a third arm or something?"
    play music Schoolday
    "I continued down. However, as I kept going, the hall was growing quieter and quieter as I neared my classroom."
    "As I walked to the door, a few students glanced my way as I entered."
    MCT "... I didn't have a chance to wash these pants. I hope there's not a stain somewhere that I'm not seeing."
    scene Classroom with fade
    "I walked into class and sat immediately, getting my books out onto my desk."
    "Compared to the halls, the classroom was quiet. Almost eerily so. Especially with everyone being there and seated prior to my arrival."
    show AE neutral with dissolve
    "Shiori sat in front of me, of course, jotting something into her notebook."
    hide AE with dissolve
    pause .25
    show BE neutral with dissolve
    pause .25
    "Honoka sat in her usual place by the window, twirling a pencil between her fingers."
    show BE happy
    "She turned and met my gaze, giving me a warm, welcoming wave."
    hide BE with dissolve
    pause .25
    show FMG neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    "Akira sat between her and I, her hand deep in her bag as she rummaged around for something."
    show RM neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    "In the back, Daichi sat jotting something down, taking a glance toward the front of the room, though I couldn't exactly tell what he was looking at."
    "Whatever it was didn't really matter, but he would write something after every time he glanced up."
    hide FMG
    hide RM
    with dissolve
    pause .25
    show GTS neutral with dissolve
    pause .25
    "Finally, my gaze went behind me."
    MCT "It... is Naomi the one they're talking about?"
    MCT "I haven't seen a ton of people with her specific factor around, I guess..."
    if getHighestAffection() == ("GTS"):
        MCT "Though... wouldn't I have noticed if she'd had a growth spurt recently? I see her damn near every day."
    else:
        "And, I couldn't tell her height just by looking at her now. With her sitting, it made it a little tough."
        MCT "She looks... about the same... I think?"
    "I thought this as she was literally the highest head in the room."
    "And, based on that alone, she {i}did{/i} stick out a lot. Especially given how her height had essentially doubled since the day I'd first met her."
    hide GTS with dissolve
    pause .25
    show HR unique with easeinright
    "Tashi-sensei walked in just then, pulling my attention from Naomi and to the front."
    show HR neutral
    HR "Alright, everyone. We have a lot to cover today, so page 484. Quickly now. We're going into the Asuka period next."
    if isEventCleared("MC009"):
        HR "Also, a thank you to all of you who were quick to hand in your papers on the Kofun period."
        HR "For those of you who haven't, the deadline is coming, so get on it."    
    else:
        HR "As a quick aside, the deadline for your papers on the Kofun period is coming up. Best to get a move on."
        MCT "... Shoot, I need to work on that."    
    "I turned to that page and stole a glance over at Naomi."
    HR "Okay. As a brief summary, this period marks the rule of Emperor Kinmei, the first Japanese emperor whose exact reign can actually be verified."
    HR "The first emperor, according to legends, was Jimmu, considered the founder of our imperial dynasty. Though, we don't have any conclusive evidence {i}when{/i} they ruled, nor if they existed beyond some ancient sources."
    pause .5
    scene black with fade
    pause .5
    scene Classroom
    show HR neutral
    with fade
    HR "Alright. Now, make a note at the bottom. Tomorrow, we'll be picking up right where we left off, and it would be best to make sure your notes link up together."
    play sound ClockTower
    "I jotted down a reminder and shut my notebook right as the bell rang, pulling my bag onto my lap so I could unload everything into it easier."
    hide HR with dissolve
    pause 0.5
    if getHighestAffection() == ("BE"):
        show BE neutral with dissolve
        "At the end of the aisle, Honoka waited patiently for me, sliding over to let Shiori pass, then walking down to me."
        BE "Eesh. Snoozer of a lesson, huh?"
        MC "Yeah, totally."
        BE "Get some notes down?"
        MC "A handful. Enough to get by."
        BE "That's really all ya need."
        "I rolled my eyes."
        MC "Then, how much is that for you? How many is enough to get by?"
        BE "Eh, depends on the topic."
        show GTS neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
        "Across from us, Naomi finished packing her bag and headed out of the room."
        "I watched her leave, still keeping an eye on her."
        hide GTS with easeoutright
        show BE happy
        BE "Got a thing for Yamazaki-san, Kei-chan? I know those legs are long, but I could've sworn you were a man of more top-focused tastes."
        MC "Huh? No, no. I was just thinking about something."
        show BE neutral
        BE "Sup?"
        MC "I... well, I was heading to class today, and I overheard some girls gossiping about some other girl. Some girl in our homeroom who apparently had some wicked growth overnight or something."
        MC "I thought they may have been talking about Yamazaki-san, since she does tend to stick out a little."
        show BE doubt
        BE "Mm... no, I don't think that's who they were discussing."
        MC "You... you know who it might be?"
        BE "I... yeah."
        BE "You missed the commotion earlier, Kei-chan."
        MC "Commotion?"
        BE "Mhm. Before class started, and before you came in."
        MC "... Oops."
        BE "Still... I don't think this is the right place to go over it, though."
        "Honoka didn't make a move, but she turned her head a bit, and her eyes went over her shoulder."
        hide BE 
        show WG neutral
        with dissolve
        "Behind her and a few desks over, Alice was busy getting herself situated before heading out."
        "And, in front of her, Aida sat with her bag on her desk, leaned toward herself."
        show RM neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
        "The two watched Daichi get up and leave, and only then did Alice get up."
        hide RM with easeoutright
        "She made a motion to Aida and said something to her."
        "Aida stood up behind Alice and moved her bag, pulling it over her shoulders."
        pause .5
        show PRG unsure at Position(xcenter=0.25, yalign=1.0) with easeinleft
        pause .75
        MCT "Holy..."
        BE "Keisuke..."
        BE "Don't make it so obvious."
        pause .25
        hide PRG
        hide WG
        with dissolve
        "Alice and Aida walked out of the room together, the two standing quite close to each other."
        show BE doubt with dissolve
        MC "What the... what the hell happened to Kodama-san?!"
        MC "I-I just saw her a few days ago, and that sure as hell wasn't there!"
        BE "That's why everyone was quiet when you came in, Kei-chan."
        BE "We were all... well... shocked."
        MC "But wait... hold on a second."
        MC "Is... is that kind of growth even possible? Like, coming out of nowhere like that?"
        MC "That... almost looks like a weight gain factor. But... not."
        MC "Can a weight gain factor even focus on one part of the body like that?"
        BE "Ah... Kei-chan. I'm not an expert here either."
        pause .25
        stop music fadeout 1.0
        BE "But... look."
        BE "So, the reason everyone is talking is..."
        pause .75
        BE "... {w}Kodama-san is pregnant."
        MC "..."
        MC "Okay, now I know that you're messing with me."
        BE "Kei-chan, I'm not. I {i}promise{/i} you that I'm not."
        "I met Honoka's gaze."
        show BE sad
        pause .5
        BE "... It's been all over the girl's dorms."
        BE "Her factor is apparently somehow based around pregnancy."
        MC "That can happen?"
        MC "Also... who's the father, then?"
        show BE doubt
        BE "I... have no clue. No one knows."
        play music Rain
        MC "So... hold on, back up. How do people know that it's a pregnancy and not just weight gain?"
        BE "Because one girl happened to be in the infirmary when Kodama-san went in to get her exam."
        BE "She overheard Kodama-san mention the word \"hyperfertility\" to the nurse, apparently."
        BE "That was yesterday afternoon, I think."
        BE "And now, that girl went and blabbed to everyone, so now most of the women's dorms know about it."
        MC "Geez..."
        show BE sad
        BE "Mhm... poor girl."
        BE "I know I haven't really spent a ton of time with her, but I feel horrible for her."
        BE "Like... every girl on campus is talking about her. And it's about something that's supposed to be really personal."
        BE "She already keeps to herself a lot. I just... I can't imagine how she's feeling now."
        MC "Yeah..."
        MC "Still, I can't believe it. I didn't even know that a pregnancy factor was a thing."
        show BE neutral
        BE "Same here."
        MC "So... how did the reveal go? Like... did she just come out and say it?"
        BE "Kind of..."
        BE "She walked in with Alice, of course. And, I think she was trying to cover herself up, but with her already being on the high end of a normal nine month pregnant girl's size, it really wasn't doing much."
        BE "I was here a little early. Didn't sleep the best last night, so I took a little morning walk before class to help wake myself up. So, I think that only Yamazaki-san and I were here."
        BE "Anyway, I made some conversation with her and Alice as they walked by. You know, just small talk stuff."
        BE "And as she went to sit down, I saw her belly."
        show BE sad
        BE "I... I guess she and Alice saw me look down at it, because before I knew it, Alice told her that it was okay. That seemed to make Kodama-san feel a bit more at ease, and then she told me."
        show BE neutral
        BE "Of course, Yamazaki-san overheard and came over to congratulate her."
        BE "Then Matsumoto-san came in and, of course, had to examine the commotion, so then Kodama-san told her."
        BE "And finally Mizutani-san came in and heard, too."
        MC "So that's... like three different instances of having to retread that same conversation in like five minutes?"
        BE "Mhm."
        MC "I... wow. I'm still stunned."
        BE "I know."
        MC "Like... her? Of all girls? She doesn't seem the type to even date much, let alone have sex."
        BE "I know! That's part of what has me floored too."
        pause .5
        BE "But anyway. Wanna get some lunch? I didn't eat breakfast this morning."
        MC "Do you ever?"
        BE "Sometimes."
        MC "Well, yeah. I'm down."
        BE "Cool."
        hide BE with dissolve
        "I got up and slipped my bag on, and the two of us headed out toward the cafeteria."
        jump daymenu

    if getHighestAffection() == ("AE"):
        show AE neutral with dissolve
        "Ahead of me, Shiori had begun packing up her desk, and organizing it neatly into her bag as around us, the other students got up to leave."
        "Eventually, most of the room had cleared out, save for Shiori, Alice, Aida, and I."
        hide AE
        show WG neutral
        with dissolve
        "Off to my left, Alice stood up and walked to Aida's desk, taking her bag for her."
        pause .5
        show PRG sad-2 at Position(xcenter=0.25, yalign=1.0) with easeinleft
        MCT "What the..."
        MCT "Holy shit!"
        MCT "Kodama-san is the girl?"
        hide WG
        show AE neutral with dissolve
        "Aida stood up from her desk, and turned to the side to get her bag over her shoulders. Deftly, Shiori had immediately placed down her bag and, gently, assisted Aida in getting her bag secured."
        "Her enormous belly that now jutted off from her middle moved with her as she got her bag on and started forward with Alice, the fabric of her shirt shifting slightly with her body."
        "I blinked a few times and watched Alice and Aida leave the room in a rather quick fashion."
        hide PRG
        with dissolve
        show AE sad-2
        "Quietly, I walked over to Shiori, who had her eyes trained on Aida the entire time."
        MC "S-So uh... never a dull day, eh?"
        AE "... Mm."
        "Shiori looked on at Aida with concern in her eyes, an almost melancholy look overtaking her usually staunch visage."
        MC "What... is going on with Kodama-san?"
        pause .25
        show AE neutral
        pause .5
        "However, my questioning immediately caused her normal, emotionless self to return."
        AE "That's classified."
        MC "Eh? I mean, I'd expect that response for anyone else but... I figured you'd tell me."
        AE "Hotsure-san, this matter is one of the personal wellbeing of another student; I will not let it devolve into gossip. Unless I have Kodama-san's direct consent to discuss her situation, I will not divulge any further information."
        MCT "Hmm... I really feel I need to know, hell, even for Shiori's sake, it may give me some insight into what's going on in her mind."
        MCT "But... looking at her belly and Shiori's face... I think I know what's going on."
        menu:
            "She already told me she's pregnant.": 
                MC "She's already told me that she's pregnant."
                AE "..."
                MC "So... I just want a bit more information, is all."
                AE "... Fascinating."
                stop music fadeout 1.0
                show AE neutral-annoyed
                "Her eyes locked on to me with a subtle look of hostile and icy disdain."
                AE "She's told you she's pregnant, and you start the conversation by asking me what is going on with her as well as asking why I was so eager to look out for her?"
                MC "A-..."
                $setAffection("AE", -3)
                AE "So she told you, rather than you figuring it out while talking to me and then using your guess in order to press me for more information, believing I wouldn't have anticipated it?"
                MC "I... uh..."
                MCT "DAMN she's good."
                AE "This conversation is over."
                MC "W-Wait, hold on. I'm sorry I just... I wanted to know."
                show AE neutral
                AE "... Then ask her yourself."
                "Shiori let loose a sigh."
                play music Schoolday
                AE "... Regardless, Kodama-san has been blessed with a gift. And, I believe it is only right to help her through this difficult time as best we can."
                jump global026_AE_end

            "I just want to know if there's anything I can do to help.": 
                MC "I just... want to know if there's anything I can do to help. I think I know what's going on so... I'll leave the conversation there. Instead, I want to focus on how I can support her as best as possible."
                AE "..."
                $setAffection("AE", 3)
                AE "Hotsure-san, you have my sincerest gratitude for the sentiment. It will be difficult for our entire class, I'm sure, but..."
                AE "Stay vigilant."
                "She bowed gently, her skirt lifting up off of her gargantuan rump enough to compel her to pull it down. Despite this, she smiled."
                show AE happy
                AE "... Thank you."
                show AE neutral
                AE "In any case, Kodama-san has been blessed with a gift. And, I believe it is only right to help her through this difficult time as best we can."
                jump global026_AE_end

            "Assuming she's pregnant...":
                MC "So... assuming that she's pregnant..."
                show AE neutral-annoyed
                AE "..."
                MC "How did it happen? Well, I mean, I know how it happened, but I mean-"
                AE "Hotsure-san."
                "Almost immediately, the chill that overtook my spine and the seeming void of all sound completely shut down my line of questioning."
                AE "As I said, questions in regards to such matters are strictly classified. I cannot and will not betray Kodama-san's trust in telling you or anyone else."
                MC "Y-Y-Yes, ma'am. S-Sorry."
                show AE neutral
                AE "A change in behavior is the sincerest form of remorse. No need for an apology otherwise."
                AE "Regardless, Kodama-san has been blessed with a gift. And, I believe it is only right to help her through this difficult time as best we can."
                jump global026_AE_end

    if getHighestAffection() == ("GTS"):
        "After assembling my things as neatly as I could manage into my backpack, I rose from my desk and turned to sidle up to Naomi's, where she was taking her sweet time putting away her writing supplies."
        if getFlag("GTS025_kiss"):
            "Her cheek wrinkled as she turned her head to regard me with a warm smile."
        else:
            "Awaking shortly from her thoughts, she turned her head to regard me with a warm smile."
        show GTS neutral with dissolve
        GTS "Good afternoon, Hotsure-san. Quite the intriguing subject matter today, wasn't it?"
        MC "Uh... hey. Quite the lesson today indeed."
        show GTS happy
        GTS "Oh, to live in those times! It must have felt as if an entire new world were opening up and spilling forth."
        MC "Uh huh."
        show GTS neutral
        MC "So, uh, I think some people might have been talking about you."
        show GTS surprised 
        GTS "How do you mean? What did it concern, exactly?"
        MC "When I was heading to class I overheard some people talking about some girl from our class. I guess somebody had a major growth spurt, like, overnight."
        "The very second I said \"growth spurt\", Naomi's eyebrows shot up."
        show GTS neutral
        "But in a second she recollected herself."
        GTS "How curious. I'm glad, if nothing else, that they had the decency to keep their gossip out of earshot."
        if checkAffection("GTS", ">", 43):
            "She glanced behind me and gave me the faintest nod, which I had to chew on for a second before returning it."
            MC "So... did you?"
            GTS "Well, it was nothing major overnight, but the other day as I was walking out of my dormitory, I was somewhat careless..."
            "Behind me I heard the scrape of two desks being abandoned, followed by one lighter and one much, much heavier set of footsteps headed towards the door."
            show GTS embarrassed at Transform(xzoom=-1)
            GTS "I, erm, bumped my head on the doorframe. It happened again as I was going to lunch that day."
            MC "Oh shi- shoot, I had no idea. Are you alright?"
            GTS "I am perfectly fine, though one could see where one inclined to gossip might take notice."
            "I heard the footsteps step out of the doorway and out of earshot, at which Naomi's polite smile turned upside down, and she sighed."
            show GTS sad 
            GTS "I appreciate your discretion."
            GTS "However... I do not believe the rumors were about me."
            pause 0.75
            GTS "Apparently... Kodama-san is with child."
            MC "Oh... {w}{i}oh{/i}."
            MC "That poor girl, she's barely out of high school..."
            GTS "Indeed. One can hardly imagine how she must be feeling."
            show GTS embarrassed 
        else:
            "She glanced behind me and then gave me the faintest nod."
            show GTS surprised 
            extend " I registered her eyes going wide as I turned around to see what she was looking at."
            hide GTS 
            show WG neutral at Position(xcenter=0.75, yalign=1.0)
            show PRG unique at Position(xcenter=0.5, yalign=1.0)
            with dissolve 
            "Filing out of the room in a conspicuously inconspicuous manner, Alice walked with Aida between her and the wall, the former's bulbous figure obscuring most of the former's from my sight. Aida was strangling the straps of her book bag."
            "But when they got out the door, I had just enough of an angle to see that she was now sporting a taut, round bowling ball belly."
            hide WG
            hide PRG
            with dissolve
            "I tried to screw my jaw back on before I turned back to face Naomi."
            show GTS angry with dissolve 
            MC "That... wasn't there yesterday."
            $setAffection("GTS", -3)
            GTS "Please mind Kodama-san's feelings, Hotsure-san. She's facing down quite an ordeal."
            MC "Sorry. {w}So... I take it that wasn't just Nikumaru-san rubbing off on her."
            show GTS sad
            GTS "No, apparently not. If what I've heard is to be believed... Kodama-san is with child."
            pause 0.75
            MC "She..." 
            MC "{i}But she looks like she's already due.{/i}"
            show GTS surprised 
            GTS "{i}I know!{/i}"
            show GTS embarrassed 
        GTS "It's not all bad, of course. She'll be a wonderful mother, indubitably."
        MC "Oh, absolutely, just... {w}man, I don't think any of us have been out of high school a year. Like, imagine getting pregnant this early in the year, so far away from her family."
        GTS "Well..."
        show GTS neutral
        GTS "What's done is done. The best we can do now is to give her plenty of support and understanding."
        GTS "Heaven knows she will want for both."
        MC "Mm..."
        MC "So... if that just happened {i}literally{/i} overnight..."
        MC "Could that be her factor? {w}...Somehow?"
        show GTS neutral at Transform(xzoom=-1)
        GTS "It would seem so."
        "She at last stood from her desk, looked out into the pale sunlight as her shadow blanketed me, and sighed."
        show GTS neutral at Transform (xzoom=1)
        "She spared one more dainty glance down at me over her shoulder."
        GTS "Stiff upper lip, eh Hotsure-san?"
        MC "Indeed."
        jump daymenu

    if getHighestAffection() == ("WG"):
        "I glanced down at my desk and started getting myself packed up."
        show WG neutral with dissolve
        "Looking up, I spotted Alice... well, the tail end of her, leaving the room."
        hide WG with dissolve
        MCT "Welp, okay. Guess I'll see her later. I thought she said she'd have some deliveries for me."
        "I finished packing my bag, then got up, glancing about as everyone else left."
        scene Hallway with fade
        "Walking into the hall, I glanced down it, seeing one head poking up above most of the rest."
        MCT "I... think Naomi is about as tall as she was last time I saw her?"
        scene black with fade
        pause .5
        scene Dorm Hallway with fade
        "An hour or so later, I headed down the hall toward Alice's dorm."
        "Now backpackless, I was keen to get my deliveries finished with, so I could spend less time running around and more time with Alice."
        MCT "... Or maybe in my dorm in sweatpants. Never know. I could use a breather after this clustered mess of a day."
        "I glanced up at the doors to make sure I had the right one, then knocked."
        play sound Knock
        pause .75
        MCT "Hm."
        play sound Knock
        "I knocked once more, stepping back a bit."
        pause .5
        show WG neutral with easeinright
        pause .25
        WG "Good afternoon, Keisuke."
        MC "Afternoon! You have some deliveries on deck, I assume?"
        show WG surprised-2
        "Apparently what I said must have jogged Alice's memory. She's usually the one reminding me, so this seemed odd."
        show WG neutral
        WG "Ah yes, indeed. I'll have them ready in a moment."
        MC "I didn't get a chance to catch you after class, but I wanted to make sure I was staying on top of things."
        WG "I appreciate the follow up, Keisuke."
        scene Dorm WG
        show WG neutral-2
        with fade
        "Alice held the door as I stepped in, leaving my shoes on and staying by the door while Alice dipped into her bedroom."
        MC "How was your day today?"
        WG "Quite ordinary, I'd say. Uneventful might be a more proper term."
        MC "Ah. {w}Doing anything fun later to make up for that?"
        "Alice wasted no time, and stepped back out, two boxes in her arms, while not bothering to answer my last question."
        WG "I'll have two more for you in just a moment."
        hide WG with dissolve
        stop music fadeout 1.0
        MCT "I guess this is just time for business then."
        "I nodded and took those two, setting them down by my feet for a moment."
        show PRG neutral with dissolve
        pause .8
        show PRG worried
        pause 1
        show PRG scared
        pause .5
        hide PRG with dissolve
        MCT "..."
        MCT "Did I just-"
        show WG neutral with dissolve
        WG "Here you are, Keisuke."
        show WG haughty
        WG "On the double, now. Wouldn't want to leave anyone waiting."
        MC "Alice, hold on. Is Aida-"
        show WG doubt
        WG "She's sleeping at the moment."
        pause .5
        show WG surprised
        PRG "Alice?"
        pause .75
        show WG surprised-2 at altMove(0.5, 0.25)
        show PRG unique at Position(xcenter=0.75, yalign=1.0) with easeinright
        pause .75
        PRG "... It's okay."
        show WG worried
        WG "..."
        PRG "H-Hi... Hotsure-san..."
        MC "Ehm... hello, Kodama-san."
        play music PRG
        "My eyes stayed trained right on Aida's face, though I'd seen her body, not only in the moment prior, but also in my peripherals."
        show WG neutral
        WG "..."
        PRG "... E-Everyone else knows by now. And... I-I'd rather if... I told you myself, then you hearing from a rumor."
        show PRG nervous
        PRG "... T-This is... my factor, Hotsure-san."
        PRG "I... I have a..."
        show PRG unsure
        pause .5
        PRG "... I-I have a... hyperfertility factor."
        PRG "I... I-I'm... {w}pregnant."
        MC "I... ah..."
        MC "Well... congratulations, Kodama-san."
        show PRG worried
        PRG "T-Thank you..."
        PRG "Alice has been... up until recently, the only person who knew my factor."
        show PRG unique
        PRG "A-As you can... imagine. M-My factor is... s-something a little... p-personal."
        MC "Right."
        show WG neutral-2
        MC "Well, I'd say your trust was well placed."
        WG "And, I appreciate your trust in me, Aida."
        WG "However, unfortunately it's human nature to talk, and a few students have taken to gossiping about Aida's condition, as you may or may not have heard, Keisuke."
        show PRG worried
        PRG "I... I can't really blame them."
        PRG "I just... {w}don't want to feel like the odd one out."
        MC "I can understand that sentiment. People can be pretty inconsiderate sometimes... well, a lot of the time honestly."
        PRG "That's... t-that's true."
        PRG "Well, I... I'll let you two be. It was... n-nice seeing you, Hotsure-san."
        MC "And you as well, Kodama-san. Always a pleasure."
        pause .25
        show PRG neutral
        pause .5
        "Aida smiled once more at me," 
        hide PRG with dissolve
        extend " then shuffled back into her room and closed the door."
        show WG neutral at altMove(0.5, 0.5)
        WG "I would appreciate your discretion in this matter, Keisuke."
        show WG worried
        WG "As I'm sure you can imagine, Aida has gone through... quite the torrent of emotions over the last few days."
        show WG neutral
        MC "Of course. And you can count on that. I make an effort to keep my conversations between only those I have to have them with."
        show WG neutral-2
        WG "Wonderful. Thank you very much."
        stop music fadeout 1.0
        show WG haughty
        WG "And, on that note, those deliveries are liable to be late if you stay where you are."
        "Alice stepped forward and handed me two more boxes."
        MC "Ah... right. I'll get on it."
        show WG happy
        play music Schoolday
        WG "Thank you, Keisuke."
        "I stacked the boxes up and turned to leave."
        MC "Have... mngh... a good rest of your day, Alice."
        WG "And you as well."
        scene Dorm Hallway with fade
        "Alice helped me with the door once more as I stepped into the hall and adjusted the boxes in my hands."
        "I didn't really know how to process what I just learned, but in an attempt to focus on the matter at hand, I checked the first label."
        MCT "Okay... think I know where that is."
        "I headed off in that direction, eager to lighten my load."
        jump daymenu

    if getHighestAffection() == ("FMG"):
        show FMG neutral with dissolve
        "As most students rose from their seats, Akira was up a full pace ahead of them, and turned toward me."
        "She looked over as Shiori got up and left, then made her move toward me."
        MC "You know you can just walk over, right? No need to plan like a chess player."
        FMG "Have you even played chess?"
        MC "I've dabbled."
        FMG "Anyway, you hear the news?"
        MC "Should I have? The only thing I've been hearing today as I walked the halls were a couple of students talking about some crazy growth a student had. I assumed it was Yamazaki-san."
        FMG "Nah, it's Kodama-san."
        MC "Ah... huh?"
        MC "Yeah, no way. I saw her the other day and she looked just fine, maybe a little wider down below. Nothing out of the ordinary for this place at least."
        "Saying nothing, Akira nodded over her shoulder and turned a bit, so she could face me and peek over at Aida."
        hide FMG with dissolve
        "Alice stood beside Aida's desk, the two chatting somewhat idly as Aida gathered her things into her bag."
        pause .5
        show PRG neutral at Position(xcenter=0.25, yalign=1.0)
        show WG neutral at Position(xcenter=0.75, yalign=1.0)
        with dissolve
        pause .5
        "Aida got her bag over her shoulders, turning in a way that I could see her... and the beach ball-esque belly she now had."
        hide PRG
        hide WG
        with dissolve
        pause .5
        show FMG neutral with dissolve
        MC "Well, I'll be."
        FMG "Before I heard the news, I was under the assumption she had gotten really fat after hanging out with Alice all the time. {w}One of the times I like being wrong."
        MC "So... that's not fat?"
        FMG "..."
        FMG "No. That would be baby, Kei-kun. Kodama-san has a preggo factor."
        MC "Baby? As in..."
        MC "... Oh. {i}Ohh...{/i}"
        FMG "She's adorable though. I'm so happy for her."
        MC "I... I'm at a loss for words." 
        MC "That isn't who I expected at all. Or {i}what{/i} I expected at all."
        show FMG happy
        FMG "It's a lot to take in for her, I'm sure. I know she'll be a great mom though. She's a sweetheart."
        show FMG neutral
        FMG "And, she can cook. {i}Huge{/i} bonus."
        MC "Are you sure weight gain isn't your factor? You're always going on and on about food."
        show FMG angry
        FMG "A high calorie intake is a part of my diet."
        MC "Uh-huh, I bet it is."
        jump daymenu

    if getHighestAffection() == ("PRG"):
        "I loaded up my bag, managing to cram everything in my usual unorganized fashion without too much trouble."
        "Glancing up, I watched Honoka leave the room, followed by Akira, Naomi, Daichi, and finally, Shiori."
        show WG neutral with dissolve
        "Alice was standing beside Aida's desk, the two seeming to be deep in conversation about something as Aida packed her desk away into the bag that sat on her lap."
        hide WG with dissolve
        "I got up from my desk and threw my bag over, heading out into the hall."
        scene Hallway with fade
        pause .25
        MCT "... So, who the hell was everyone talking about? I didn't notice anyone looking too massively different..."
        "The halls were cleared out a bit, and I reached back to take a swig from my bottle."
        MCT "Ach, crap. Time to refill."
        "I changed directions from the courtyard and headed for the cafeteria instead."
        scene Cafeteria with fade
        "Walking in, I went to the drinking fountain and stuck my bottle into the stream of water, filling it mostly full once more and taking a long drink."
        MCT "Alright. I'm going back to the dorm to chill. I need some TV or something after this weird-ass day."
        scene Hallway with fade
        stop  music fadeout 1.0
        "I walked back into the hall and turned toward the courtyard, turning a corner into another hall."
        "As I turned, I glanced down the hall."
        show WG neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
        pause .75
        show PRG unsure at Position(xcenter=0.75, yalign=1.0) with dissolve
        pause .5
        MCT "... What the hell?"
        MCT "Where did... huh?!"
        "I gaped, staring at the beach ball sized mound now erupting from Aida's abdomen as she and Alice turned to open the door, and I got a glimpse at it from the side."
        hide WG
        hide PRG
        with dissolve
        MCT "Oh my G-"
        MCT "Kodama-san is the girl?!"
        "Shaking the shock away, I took off down the hall, following the two girls."
        scene Campus Center
        show WG neutral at Position(xcenter=0.25, yalign=1.0)
        show PRG unsure at Position(xcenter=0.75, yalign=1.0)
        with fade
        "Coming to the center of campus, Aida and Alice stopped."
        hide WG neutral with easeoutleft
        extend" The two exchanged words, then Alice broke off and headed toward the entrance to campus, while Aida turned and headed for the dorms."
        "Without a second thought, I turned toward the dorms."
        scene Dorm Exterior
        show PRG unsure at Position(xcenter=0.75, yalign=1.0), Transform(xzoom=-1)
        with fade
        "I didn't sprint ahead or anything. I definitely didn't want to startle Aida."
        "Rather, as we got to the dorms, Aida walked silently toward the women's dorms, while I stopped, sure as hell not wanting it to look like I was following her home."
        "Nearby, a small group of girls walked out and past her, the majority turning their heads to glance back as they went past."
        Student1 "That's her..."
        Student2 "Kumagai-san wasn't kidding..."
        "I let the group pass, looking forward as Aida slowly glanced over her shoulder."
        show PRG surprised at Transform(xzoom=1)
        pause .75
        show PRG scared at altMove(0.8, 0.5)
        play music PRGDramatic
        PRG "H-H-Hotsure-s-san?"
        MC "Hey, Kodama-san..."
        show PRG sad-2
        PRG "..."
        "She looked back at me, her face pale."
        PRG "..."
        PRG "... {w}You heard too?"
        PRG "Everyone else has..."
        MC "Hear what?"
        PRG "..."
        PRG "... {w}A-About me..."
        MC "No... I was running late this morning, so I didn't really have time to talk to anyone."
        PRG "..."
        PRG "... I..."
        pause .5
        PRG "... I'm pregnant."
        MC "What?! You..."
        MC "Wait a minute... hold on."
        MC "This... this..."
        MC "Your... factor?"
        "Aida looked down at herself and nodded."
        PRG "It's... it's the rarest kind..."
        PRG "My factor... causes me to..."
        PRG "... I-I... I can get pregnant... r-really easily. And... my growth is based around that..."
        MC "I..."
        MC "Wow..."
        PRG "..."
        PRG "{i}Sniff{/i}"
        pause .5
        PRG "... C-Could I... t-talk to you... {w}a-another time, H-Hotsure-san?"
        MC "Ah... o-of course. That's totally fine."
        PRG "T-Thank you..."
        "Aida turned and shuffled quickly through the door."
        "As she turned, I could make out the telltale puffiness in her eyes, and a slight glint of tears in the sunlight."
        "I turned away, glanced at the other students going about their business."
        MCT "Aida's factor... that's possible?"
        "I glanced down."
        MCT "That's... so different from everyone else's..."
        MCT "And the rarest factor."
        "I took a slow breath and started on my way back to my dorm."
        jump daymenu

label global026_AE_end:
    MC "How... did she get so big so fast?"
    show AE neutral
    AE "Metabolic and hydrostatic functions have been altered by her body to such a degree that it's caused extreme swelling. I don't think it's too unreasonable but... by how she looks, I have an idea of what is to come."
    MC "What... is to come?"
    AE "... Well, as I said, she's been blessed with a gift... if that's the case, it must be her birthday, if I may be so gauche to say."
    AE "Many more soon enough, I reckon."
    jump daymenu

label RM001:
    scene Dorm Interior with fade
    play music Schoolday
    MCT "Another day of classes over..."
    "When I arrived back at my room, Daichi was already there, poking some device on his desk very intently with a soldering iron."
    MCT "What on earth is he up to?"
    "Part of me wondered if he was going to burn the whole place down with that thing. It was definitely some kind of electronic piece he was working on."
    "It was hard to tell what exactly it was from over here, beyond some kind of circuit board. I guess he looked like he knew what he was doing though."
    show RM neutral with dissolve
    RM "..."
    "By any reasonable measure, the guy seemed like an odd duck— and that's if I'm being polite about it."
    if isEventCleared("MC007") or isEventCleared("FMGWG001") or getFlag("MC005RM"):
        "It didn't help that he'd already established a penchant for spying on people if he thought it might somehow help him \"gather information\", as he put it. To be honest, I didn't know that much about him beyond that."
    else:
        "Outside of our first encounter and the rather strange conversation where he basically asked me to be part of his personal spy network, I honestly hadn't gotten a chance to talk with him that much."
    "The better part of me thought I should probably keep it that way, but it was only going to be increasingly awkward to live with someone I barely knew or talked to. I decided it was best to try to break the ice."
    play music RM
    MC "Hey, Daichi."
    RM "Yes? {w}You got anything for me?"
    MCT "What the hell is he talkin- Oh. I remember now. {w}He must be thinking about that weird favor he asked about to report to him if I find anything suspicious about the school."
    MC "Uh, not really no. Just wanted to talk."
    RM "Okay. What did you want to talk about?"
    MC "Well, what do you got going on there?"
    if getFlag("RM_govagent"):
        "He put down the soldering iron and glared over his shoulder at me."
        show RM angry
        RM "None of your business."
        MC "Uhh, did I do something to offend you?"
        show RM neutral
        RM "For one, you don't appreciate the situation we're in."
        MC "Are you still upset over the \"I'm a government agent\" thing?"
        show RM neutral
        RM "Yes."
        MCT "I thought it was pretty funny at the time, but the guy did seem pretty spooked if he was ready to jump out the window when I told him I was from the government. Probably need to tread more lightly in the future."
        MC "Look, I'm sorry. I didn't realize it was such a... sensitive subject. It was just an off the cuff joke, I didn't mean anything with it."
        $setAffection("RM", 1)
        RM "Alright I guess."
        show RM smug
        extend " Apology accepted - I'll forgive your ignorance. If you're willing to take this seriously, I can enlighten you on a few things. Interested?"
        MCT "Can't say I'm too excited about what he might mean by the word \"enlighten\", but I guess it wouldn't hurt to humor him for a bit if it will help smooth things over."
        MC "Sounds good. So, what are you working on there?"
        show RM neutral
    else:
        "He answered me without turning around, opting instead to continue tinkering with the device."
    RM "It's nothing. Don't worry about it."
    MC "Seems like something to me. Judging by the audio input you're attaching to it, it's probably some kind of recording device."
    show RM distrustful
    "That got his attention. He put the soldering iron down and turned to me, with his eyes narrowed."
    RM "Alright. You're more clever than I gave you credit for, I'll give you that much. Just forget about it, okay? I'm not doing anything illegal here."
    MC "Spying on people sounds like it {i}could{/i} be illegal."
    show RM concerned
    RM "Look, I'll level with you, this concerns something that I {i}need{/i} to know. I've already exhausted more conventional means of obtaining information, so this is what I'm left with."
    MC "Are you sure about that?"
    show RM distrustful
    RM "Why? Are you going to rat me out?"
    MC "No. I'm not a rat. Just as long as it's nothing pervy okay?"
    show RM angry
    RM "I'm not some kind of voyeuristic creep, if that's what you're implying."
    MC "I'm not saying you are, I'm just telling you what it looks like."
    show RM neutral
    RM "Don't worry, it isn't."
    "That didn't give me a lot of assurances, but I decided to just roll with it for now."
    show RM doubt
    RM "If you must know, I'm busy investigating."
    MC "The school, you mean?"
    RM "Of course."
    MC "You still think there's something else going on here?"
    show RM distrustful
    RM "There has to be. I'm surprised you don't."
    MC "I mean it's certainly an unusual circumstance, but given what I've seen so far it seems to check out."
    RM "What did I tell you about just believing what you see?"
    MC "Fair enough I suppose, but have you ever heard the expression \"Sometimes a cigar is just a cigar\"?"
    show RM doubt
    RM "If you're satisfied with the way things seem to be, I'll leave you to it, but some of us require more evidence to be convinced."
    MCT "I'm not sure you as a single person counts as \"some of us\" but whatever."
    "I didn't really care for his not-so-subtle suggestion that I was some kind of simpleton, but I resisted the urge to be snarky and tried to get him off the topic of this supposed \"grand conspiracy\"."
    MC "This can't be the only thing you spend time on. I'm sure there's something you do for fun, right? Got any hobbies?"
    RM "Not really. Haven't had time lately. Been too busy trying to figure out what's going on here."
    MCT "You're killing me here dude."
    MC "Well, what about before you came to the school?"
    show RM neutral
    RM "...I read manga, I guess?"
    MC "See, there you go. That's a start! What did you read?"
    RM "I liked Two Pieces. Is that still going?"
    MC "It's been going on longer than we've been alive. I don't know if it will ever stop at this rate."
    RM "Nice. I should probably get back into it then."
    MC "You read anything else?"
    show RM neutral
    RM "When it comes to leisurely reading, mostly novels I guess."
    MC "Like detective novels?"
    show RM doubt
    RM "... {w}Not just detective novels, I'll have you know."
    MCT "Suuure."
    MC "What about other stuff? Games? Movies? Music?"
    show RM concerned
    RM "I used to play Suncraft, a few years back. Haven't played in a while, though."
    MC "Oh, yeah. I had some friends that were really into that. I've never played it though."
    show RM angry
    RM "What do you mean you've never played it? It's one of the most popular strategy games of all time."
    show RM neutral
    MC "I know, I'm probably missing out, but I never really got into those kinds of games."
    show RM sad
    RM "Oh, I see..."
    MC "..."
    MCT "Well that died out pretty quickly."
    menu:
        "Ask him about the device.":
            $setFlag("RM001_Device")
            MCT "Honestly, is it my job to keep this conversation going?"
            MC " Sooo, what about your project there? Do you like tinkering with stuff?"
            show RM neutral
            RM "Sometimes I suppose. I know a thing or two, if that's what you're asking."
            MC "I see. {w}What about when you graduate? You going to go into electrical engineering or something?"
            RM "Maybe? I haven't decided yet."
            RM "I've thought about becoming a teacher, too."
            MC "Why a teacher? You like learning?"
            show RM happy
            RM "I want kids to get more critical thinking skills, so they won't just mindlessly obey authority."
            MC "I suppose that would be a good thing."
            MCT "Unless they turn into paranoid weirdos like you..."
            MC "Well, hey, why don't you show me your... Whatever it is."
            show RM doubt
            "He sighed and held up a lens, which was hiding behind some other components."
            RM "It's a recording device."
            MC "Yeah, that."
            "He paused for a moment."
            $setAffection("RM", 1)
            show RM happy
            "Eventually his expression relaxed a little."
            RM "Sure, why not? Pull up a chair."
            scene black with fade
            "We spent most of the evening working on his audio device. He got a lot more talkative once he started talking about something he was more comfortable with."
            "He taught me quite a bit about how all the components work: the capacitor, resistor, diode, transistor, etc. I'd seen the stuff before and they were talked a little bit about in the physics class I had before."
            $setSkill("Academics", 1)
            "But now I felt like I understood what was happening. Maybe he'd make a good teacher after all."
            jump daymenu
        "Focus on your homework.":
            $setFlag("RM001_Study")
            MC "Alright, well looks like you're busy. I'll leave you to it. Good talk."
            show RM neutral
            RM "Okay, sounds good. Thanks for asking though. Since we'll be living together for the foreseeable future, we should probably talk more often."
            MC "For sure."
            RM "And let me know if you hear anything of interest, okay?"
            MC "Sure thing. No problem."
            hide RM with dissolve
            "Yikes, that whole thing was awkward, but I suppose he isn't such a bad guy, just a little odd, as I suspected."
            "Still though, not having a chatty roommate was probably a good thing for my studies."
            $setSkill("Academics", 1)
            if isEventCleared("MC002") and not isEventCleared("global005"):
                "Using it as an excuse to exit the conversation, I decided to get a headstart on the Jōmon period paper for Tashi's class."
                MCT "Hmm, now where did I put that book I borrowed from him?"
            elif isEventCleared("MC008") and not isEventCleared("global026"):
                "Using it as an excuse to exit the conversation, I decided to get a headstart with studying for the test on carbohydrates for Tsubasa's class."
            else:
                "Using it as an excuse to exit the conversation, I decided to get a headstart on the assignment for Tashi's class."
            jump daymenu


label RM002:
    scene Cafeteria with fade
    if not getFlag("Meet_Yuki"):
        $setFlag("Meet_Yuki")
        play music Peaceful
        "I was sitting in the cafeteria picking at my food. Not that it was bad, but the monjayaki wasn't looking particularly appetizing and I just wasn't that hungry." 
        "I was more so staring out the window wishing I could have had the chance to enjoy the nice warm weather more, instead of being stuck in classes all day. Part of me thought about taking a walk outside instead of sitting here trying to finish this thing."
        "This place was still pretty new to me and nothing really felt all that familiar."

    if not isEventCleared("MC003"):
        "One would think that wouldn't be the case going to the same school as your sister, but even she was seemingly nowhere to be found."
        MCT "I need to talk to her sooner or later. Might as well give her a shout."
        MCCell "<Hey, how's things been going with you?>"
        pause 1
        "I waited a little bit for a response but gave up when I didn't get anything in response."
        MCT "Lotta good that phone does when you never check your messages Tomo."
        "By this point I would have at least tried to pop in for a visit, but I never even bothered to ask for her room number, so I had no idea how to find her. Not that I imagined it would've been hard to, yet here we are."
        MCT "I worry about her sometimes."
    else:
        "The whole place, and this whole {i}scenario{/i} (for a lack of a better term) still wasn't sitting well with me. Probably not with anyone for that matter."
        "Though if what Tashi-sensei said is true, with himself being the prime example, it sounded like Tomo and I were getting off easy with this hair growth thing." 
        "She especially didn't need something that was going to make it harder to meet new people and make friends. As strange as this all was, part of me hoped this smaller school setting will be easier for her in that regard."
        MCT "I guess I worry too much about her. She's an adult now. She can make her own choices— or at least learn to live with them."

    UNKNOWN "Tehehe!"
    "My train of thought was interrupted by the sound of obnoxious laughter between a group of students at the next table over that had been prattling on about all manner of inane gossip."
    "I had no idea who these girls were, but I recognised the arm band on one of them to at least know she was one of the student council members."
    Student1 "So, who's your pick? There's more than a few good ones to choose from here."
    MCT "Hmm, already sizing up the guys at the school? Not that I'm particularly interested in any of them over there, but I'd be curious how I rank."
    CMF "Isn't it obvious? It's easily Hageshi-sensei. He's tall, super buff, and those eyes... I could just stay lost forever in their gaze. Girl, you don't even know!"
    Student1 "Hehe! Oh, believe me, I know. He's a total dreamboat!"
    MCT "Yeesh. They're talking about the faculty. Girls in high school would do this too. {w}Hageshi I kind of understand, but some of these dudes are old enough to be their dads. What the hell is wrong with these chicks?"
    Student1 "What about you Etsuko?"
    Student2 "There's a certain someone I have in mind... he's a PE teacher."
    Student1 "You mean Sugiyama-sensei?"
    Student2 "I'm not sure, I've never heard his name. He has long hair that's tied in a bun, and a scruffy beard that's... oo! He's definitely my type for sure."
    Student1 "That doesn't sound like Sugiyama-sensei. His hair is super short, like a buzz cut."
    Student2 "You seem to know the who's who on campus Yuki-chan, you know who I'm talking about, right?"
    CMF "Sorry, it's not really ringing a bell. Being on the student council is great for having my finger on the pulse of things, but it doesn't usually involve anything with the staff that run the sports and other physical activities."
    CMF "But I'll see what I can dig up. I'm definitely curious if he's caught your eye already."
    Student2 "Hey, easy now! He's my pick!"
    "Girls" "TEHEHE!"
    "At this point I was ready to tune it all out. I wasn't interested in their blithering nonsense, or at least I thought I wasn't until I heard the next little tidbit."
    CMF "What about you Fumika-chan? Who's your pick?"
    Student1 "Well, you already took my first pick with Hageshi-sensei, so I feel like I should pick another."
    Student2 "Who do you have in mind? I want to know the juicy details."
    Student1 "Well, it's a little embarrassing... Promise me you won't make fun of me?"
    CMF "Promise. Now I gotta know. Who?"
    Student2 "I'll try, but I ain't promising nothing. Come on, you gotta tell us now."
    Student1 "Oh, might as well get it over with. I was thinking... {size=-6}Tashi-sensei{/size}..."
    "Girls" "Eeeeehh?!"
    Student1 "I know, I know. Don't get me wrong, his tongue is still like... super gross. But he's got this broody bad-boy vibe. {w}I kinda dig it."
    Student1 "He just strikes me as someone who's deep and interesting, more than he lets on at least. If I were ten years older I'd certainly try to flirt the hell out of him, just to see how he'd react!"
    "Girls" "TEHEHEHE!"
    "If I wasn't planning on finishing my lunch before, I was certainly planning on losing it after learning anyone was getting warm between the legs after seeing that python flop out of Tashi-sensei's mouth."
    MCT "That's it. I'm getting the hell out of here."
    "I was gathering my tray so I could leave, but paused for a second after realizing the subject had changed to something slightly more interesting." 
    Student1 "So how have you been managing with yours, Yuki-chan?"
    "Daichi did say he wanted me to keep my ear to the ground when it came to information about the factors around the school." 
    "I didn't feel particularly compelled to join in his hairbrained schemes, but I was curious enough myself to try to learn a bit more about them if the opportunity presented itself."
    CMF "I've noticed it a little so far. What do you think? Do they look puffy to you?"
    "The council member looked to be pointing at her lips. It was hard to tell, she was the one facing away from me."
    Student1 "A little yeah. But it's nothing to worry about. It's nothing that a little make-up and lipstick can't cover up."
    CMF "I hope so..."
    Student1 "What apparently can't be covered up is my fat ass with a pair of jeans. I tried fitting into my favorite pair the other day."
    Student1 "I huffed and I puffed and pulled and pulled, until finally after 20 minutes of struggling to get them over my thighs I finally managed to button them up— only for my butt to blow out the middle seam!" 
    Student1 "I really liked that pair too..."
    Student2 "That sucks, I'm sorry Fumika-chan."
    Student1 "...I should have just given up when they wouldn't even pull over my thighs."
    "Seemingly normal up top, this girl was, true to her word, quite a chunkster around her thighs, with a butt not so far behind to boot."
    if getHighestAffection() == "AE" or getHighestAffection() == "WG":
        "Needless to say, my interest was piqued." 
    Student2 "My clothes haven't been fitting quite the same either."
    Student1 "Yeah but you're looking tight in the right places." 
    CMF "You're looking so toned, I'm jealous girl."
    if getHighestAffection() == "FMG":
        "The school uniforms weren't exactly the most revealing clothes in the world, but giving her a once over I noticed the girl did have some pretty toned arms on her. She looked like she spent a decent amount of time at the gym."
    Student2 "I'm still not sure how I feel about it to be honest. I don't feel like anything I have really flatters my figure."
    Student1 "I bet it feels good though right? To be in better shape I mean. {w}Think you'll try out for any of the sports clubs? We could always use a few more in the basketball club."
    Student2 "I'm actually thinking of trying the cooking club. It's something I've always kind of been interested in. My grandma was such a good cook, but my mom sure wasn't, so I never got to learn how."
    Student1 "I suppose that's fine too..."
    Student2 "How would I go about joining? I'd been meaning to ask Takamura-sensei, but is there some kind of protocol I should follow? I figure you'd both know since you have her for homeroom class."
    CMF "Takamura-sensei is super nice, I'm sure she'd love to talk to you about the club, but she'd probably just send you to the club president."
    Student1 "Oh yeah, Sato-san, or something like that."
    CMF "Close, Fumika-chan. Her name is Michiko Sano, she handles the matters related to the club applications, so you should go ask her."
    Student2 "Thanks, I'll try to find her."
    CMF "Bye Etsuko-chan!"
    Student1 "Bye."
    "By this point in my little investigation, I was starting to feel like a real private eye." 
    "Seriously, like the real life kind where they sit in a car for five hours hoping to catch some fat dude with a back injury lifting something heavy so the insurance company that hired them can cancel the guy's disability policy."
    MCT "I have to imagine this is what Daichi spends most of his free time doing."
    "These girls were boring me to tears. Whatever courtesy I owed Daichi to \"investigate\" this matter I had paid in full by this point. It was just by mere chance I could still continue to hear their conversation since we got up to leave at the same time."
    Student1 "So, got any plans for today?"
    CMF "Nothing that exciting. I have hall monitor duty on the lower floors after lunch. My shift starts in about fifteen minutes, but that gives me a bit of time to drop off these forms to the council president's office."
    "I couldn't help but notice the council member paused to take a long gulp, being noticeably unsettled after mention of the council president."
    Student1 "Hm? What's a matter? {w}Oh, {i}Oh!{/i} {w}I take it you have to talk to the \"Specter\"?"
    "The council member visibly frowned at the mention of that name."
    CMF "No, it's not that. Why would you say that?"
    Student1 "I don't know, she just seems like someone who's hard to talk to."
    Student1 "Speaking of her, funny enough, I got assigned to be on a group project with her. We need to have the paper ready in a few days but I haven't even been able to get in touch with her to start." 
    Student1 "Think you could let her know I've been trying to reach her?"
    CMF "I'll be sure to pass along your message, but in the future, could you please not use that name?"
    CMF "It's not her title or anything, it's just a rude nickname someone came up with for her. She's really not that bad." 
    "Judging by the skeptical reaction of the other girl, she didn't seem to be buying that assessment."
    CMF "Sure she has her own quirks and particular way of doing things, but so does everyone, and that's fine with me."
    Student1 "Okay... Well, thanks for passing that along for me."
    "Miss chunky thighs checked her phone more time had passed than she thought."
    Student1 "Shoot! I gotta head out and get ready for club practice. I've been working on my three-point shots and I'm hoping to blow out the scoreboard tonight."
    CMF "Sounds like more fun than blowing out your pants. Teehee!"
    Student1 "Haha! You got that right. I'll catch you later!"
    "The two girls split off from each other as they exited the cafeteria. I took a turn down a different hallway."
    play music HigherEdu
    scene School Inner with fade
    "Looking out the window, the rest of the campus seemed to be enjoying the warmer spring weather. Students hanging out on the lawn with their books out or just chilling to some music on their ear buds."
    "There appeared to be a lot of activity out on the track with people running back and forth. I had to assume the track team was in the middle of their practice."
    MCT "Man, it's actually surprising how many clubs they have at this school. I don't remember there being this many back in high school, and my school had a lot more students."
    "Then again, part of me supposed it wasn't too surprising though." 
    "The school probably wanted to provide lots of opportunities for activities that could keep the students' minds occupied, instead of nothing to do but dwell on what was going to happen to them with their factors."
    "Even I found myself feeling overwhelmed by the recent news from time to time, and I didn't have nearly as much to worry about what might go wrong compared to others."
    MCT "Looks like most everyone else has found something to do with the afternoon. Wonder what I should do?"
    if getSize() <= 2:
        if isEventCleared("BE004"):
            MCT "Maybe I could stop by the soccer field and see Honoka while she's at practice."
        elif isEventCleared("AE004"):
            MCT "Maybe I could pop into the office and see if Shiori-san could use a break? {w}On second thought, she'd probably ask me straightaway how my studying has been going." 
            MCT "I should probably get working on that so I have a good answer to give her next time I run into her."
        elif isEventCleared("FMG004"):
            MCT "Maybe I should hit the gym. Don't want to start slacking on my fitness like most people do after high school. Might even run into Akira again while I'm there."
            MCT "Ehh, but I'm tired already from the day. I don't have enough in the tank. Besides, I'd probably just embarrass myself in front of her." 
        elif isEventCleared("GTS004"):
            MCT "I should probably do the more diligent thing and get working on my homework and catch up on my study materials."
            MCT "Though I wouldn't mind taking a stroll through the garden as a slight detour on my way back to my room. Maybe I'll see Yamazaki-san there."
        elif isEventCleared("WG004") and not isEventCleared("WG006"):
            "Seeing all these athletic clubs made me wonder what sort of club Alice might be part of. She didn't exactly strike me as the athletic type, so I had to wonder if there was anything available that would strike her fancy."
        elif isEventCleared("WG006"):
            "Thinking about all the club activities going on made me think about Alice and the music club. She hadn't exactly handled the news well about not being voted as the club president."
            MCT "That does remind me, I should probably pick up practicing music again myself."
        elif isEventCleared("PRG004") and not isEventCleared("PRG013"):
            "Thinking about all the club activities going on made me think about if Kodama-san found any she found interesting. {w}She didn't strike me as the sports type, but surely they had other types of clubs."
            "Then again, even if she was interested in joining a club, she probably has her hands full enough already assisting Alice."
        else:
            "Since it was a nice day outside, I thought about just taking a stroll across campus to get a little more familiar with the place before just heading back to my dorm." 
            "I'd been procrastinating on my homework and study time, and I told myself I needed to at least get {i}something{/i} done on it tonight."
    else:
        "Since it was a nice day outside, I thought about just taking a stroll across campus to get a little more familiar with the place before just heading back to my dorm." 
        "I'd been procrastinating on my homework and study time, and I told myself I needed to at least get {i}something{/i} done on it tonight."

    scene Gate Front with fade
    "I was about to head outside to the quad from the main campus building when I heard something odd."
    MCT "..."
    "Looking around and seeing nothing, I assumed it was just my imagination. Maybe someone left a window open and it was the wind blowing in. It was a nice day after all."
    "I took a few more steps closer to the exit, the click of my shoes echoing through the empty entryway, but I quickly stopped when I realized something wasn't quite right."
    MCT "Hm?"
    "A brief flicker of movement out of the corner of my eye confirmed my suspicions: {w}I was being watched."
    UNKNOWN "{size=-6}Psst! It's me.{/size}"
    MC "Well that doesn't exactly tell me anything."
    "Peaking around the pillar where I saw the movement from earlier revealed none other than who I should have suspected from the get-go."
    play music RM
    show RM neutral with dissolve
    MC "Oh, it's you. What's going on? {w}...You weren't tailing me, were you?"
    show RM neutral-2
    RM "No, I've got a lead on something far more interesting."
    "It should be noted that even after being found out, he was still hiding behind the pillar as we had our conversation."
    MC "Gee thanks. Although I guess a guy who's hair is starting to get long isn't terribly interesting compared to other things going on here."
    show RM smug
    RM "Precisely. Besides, I can get a hair sample from you any time."
    "The way he said it made me suspect he might have already collected one in my sleep."
    MC "Alright, what's so interesting then?"
    show RM doubt
    RM "{size=-6}Shhhh. Keep it down. I'll explain, but for now we have to hide— quick!{/size}"
    "Not that I was eager to play along with him, but I figure if he really was onto something just standing in plain sight talking to him would be kind of a dick move if it did end up blowing his cover."
    "I ducked behind the pillar with him, but without a clue as to why I should."
    MC "Okay, so what are you doing here?"
    show RM neutral
    RM "I'm doing some surveillance work."
    "Not that he would know, or that I would even want to explain, but by this point I already have my fill of \"surveillance work\" for the day."
    MC "Surveillance on what?"
    show RM neutral-2
    RM "The Academy, of course. What else would it be?"
    "I just sighed. He was being purposefully short on the details, but part of me was just glad to know he wasn't stalking one of the girls."
    MC "Alright then, have you found anything interesting at least?"
    "Daichi turned his eyes to the big clock on the wall."
    show RM smug
    RM "We'll see in a few minutes."
    scene black with fade
    pause .5
    scene Gate Front with fade
    "After what definitely felt like more than \"a few minutes\" I contemplated just leaving, and that was saying something since I wanted to use any excuse in the world to continue procrastinating on my homework."
    "But before I could fully consider that notion we noticed two of the faculty staff ladies leaving one of the rooms. This was the one with the label \"Education and Student Support Department\"."
    show RM distrustful with dissolve
    "Daichi eyed them as they both disappeared down the hallway."
    RM "Two down, one more to go."
    MC "What are you even talking ab-"
    show RM doubt
    RM "Shhh!"
    "Just then another one of the office workers trickled out of the room."
    show RM happy
    "A sly grin crept across Daichi's face."
    RM "Jackpot."
    MC "What's going on now?"
    hide RM with dissolve
    pause 1
    MC "!"
    "I turned my head only to realize my last question had not been directed at anyone, seeing as Daichi was gone."
    "Looking all around, wondering how he could have just vanished, I then noticed he had somehow already made it across the entryway and was attempting to sneak into the empty room."
    show RM smug at Position(xcenter=0.9, yalign=1.0) with dissolve
    "At this point I didn't know what to do other than stare dumbfounded as to what was unfolding in front of my eyes." 
    "On one hand I was impressed with how fast he managed to work, which then made me realize this couldn't have been the first time he's tried something like this." 
    "On the other, I became increasingly aware of the possibility I had unknowingly made myself an accomplice to the crime of breaking and entering." 
    MCT "Well, I mean, {i}technically{/i} I didn't help him. I just stumbled on to him while he was already going to do it. {w}And I most certainly didn't encourage him to break in anywhere, no siree."
    hide RM with dissolve
    MCT "..."
    MCT "Goddamit, why of all people did I get stuck with the voyeuristic, paranoid, conspiracy nut for a roommate!"
    UNKNOWN "Is everything okay?"
    show Yuki neutral with vpunch
    MC "{i}GAAAH!{/i}"
    play music HallowedHalls
    UNKNOWN "You don't look so good..."
    MC "Bah? Wha?"
    "After briefly recovering from my soul nearly leaving my body from the sudden startle, I turned to see the source of the voice behind me." 
    MCT "Blazer, red sleeve band... wait a second, this is the same girl from earlier!"
    MCT "Oh shit! That means she's from the student council. I'm 100%% going to get expelled if she figures out what's going on here."
    MCT "But that's not going to happen! Stay calm Kei, STAY CALM!!!"
    MC "Ahem. {w}Hello. Can I help you?"
    CMF "Actually, I was wondering if I could help you. You look a bit... frazzled. Is everything alright?"
    MC "Oh. That. Yeah. {w}I'm alright. Just been a long day you know? That and I guess I'm still not that used to this place."
    "Not the real reason, but it wasn't exactly a lie either."
    show Yuki happy
    CMF "It's okay. I understand."
    show Yuki neutral
    CMF "I've had a long day myself, and I still only just started my hall monitor shift."
    CMF "My name is Yuki by the way. What's yours?"
    MC "It's Keisuke... nice to meet you."
    "I didn't exactly want to offer my last name. After all, she hadn't offered hers."
    MCT "Crap! I should have just told her a made up name all together. I need to get her off my tail somehow."
    MC "So uh, hall monitor duties eh? Notice anything suspicious?"
    "Pure projection at its finest, but a suitable distraction nonetheless."
    Yuki "Suspicious? Well not really. Most of it is just making sure people aren't running in the building or if they are lost, help them find where to go."
    MC "Ah, I see."
    Yuki "Is that why you're here?"
    MC "What's that now?" 
    show Yuki gossip
    Yuki "You're lost aren't you- Why else would you be standing around the administration wing after all- So, this here is the administration wing if you haven't been to it before- which you probably haven't because they don't have classes over here-"
    MC "Uh..."
    Yuki "You must have got lost trying to take a shortcut through to the other side of the quad- It's an easy mistake to make- Ohmygosh you must be in a hurry then to get to club practice so that's why you took the shortcut-"
    MC "Well..."
    Yuki "Oo you're probably in the soccer club- their practice is just about to start so you're gonna want to go out these doors and loop back around to the lockers to go change- or maybe you want to head back and do that at your dorm-"
    MCT "Geesh, does she ever stop talking? I'm feeling out of breath just listening to this chick."
    if isEventCleared("MC003"):
        MCT "Wait a second... is this Tomo's roommate she was talking about? The one that talks her ear off all the time? {w}I mean I can't imagine too many people that rise to this level, so maybe not."
    Yuki "I know I had a real hard time deciding what club I was going to join-"
    "Apparently we had changed subjects in the conversation and I hadn't noticed."
    Yuki "At first I thought about joining the debate club-"
    show Yuki neutral
    MC "Pfft! Hehe."
    Yuki "Hm? Is there something wrong?"
    MC "What? Oh, nothing, I'm fine. Uh, continue..."
    show Yuki gossip
    Yuki "Oh yeah, so anyway I went back and forth on that for what seemed like forever and-"
    MCT "...When I said continue, I didn't mean indefinitely."
    "By this point my mind was reeling but I kept the same polite smile on my face from when she first started up."
    Yuki "But I settled on the student council instead because I figured I could learn all sorts of stuff about administration by practice and learn something I could translate into a job- You see for a job I was thinking of getting into-"
    MC "Uh huh."
    MC "Uh huh."
    MC "Uh huh."
    MCT "That's it Kei, just smile and nod while pretending you still have active brainwaves and she'll eventually go away."
    "It was a terrible plan, but one that was sure to defray suspicion of any involvement on my part with Daichi's illicit snooping. {w}At least that's what I thought."
    MCT "Wait, what's that?"
    "Out of the corner of my eye I noticed one of the clerical staff that had left the room earlier was coming back."
    MCT "Oh shit!"
    "I had been keeping an eye on the door the entire time and Daichi still hadn't come out. He probably needed more time, even though I had bought him plenty by standing here listening to motormouth blabbering on about everything under the sun."
    "I didn't exactly feel like sticking my neck out for the guy on this any more than I already had. Then again, he is my roommate and I'll be stuck with him the entire year. I might not hear the end of it if I don't at least try something."
    menu:
        "Approach the staff member and stall her.":
            jump RM002_C1_1
        "Stay where you are.":
            jump RM002_C2_1

label RM002_C1_1:
    $setFlag("RM002_Favor")
    MCT "You owe me big time for this Daichi."
    Yuki "But then sometimes I wonder what if I hand joined a different club- and then like I could be working something else that I might use in the future- I mean there's just so many-"
    MCT "I'm going to be stuck here till the end of time if I keep waiting for a break in the conversation."
    show Yuki surprised
    MC "Shhhh. Shhh!"
    "I put my arm out and my finger up towards her lips to signify I needed her to be quiet."
    MC "Sorry— just one second!"
    hide Yuki with dissolve
    MC "Uh, {size=+4}EXCUSE ME!{/size}"
    MCT "I hope Daichi can hear this."
    MC "Ma'am, excuse me. I'm a bit lost, I was wondering if you could tell me..."
    "Not having thought through my lie enough to come up with an answer, I quickly looked around to see what I thought was supposed to be here."
    MC "Uh... the Principal's Office?"
    "The staff member gave me a confused look, like I was a particularly special kind of idiot."
    Secretary1 "You're in luck, you've already found it."
    "She pointed towards the door of the office next to the one Daichi had gone into earlier."
    MCT "He broke into the office right by the Principal's Office? What the hell is wrong with this guy?"
    "At this point I couldn't really tell if Daichi had brass balls or just a bunch of head trauma to pull a stunt like that."
    MC "Thank you for your help!"
    "I bowed in a slightly more dramatic fashion than I had planned, but my diversion had run its course as the staff member proceeded to walk back to her office and disappeared inside."
    MCT "Well, at least I tried."
    show Yuki neutral with dissolve
    Yuki "I had a feeling you were lost- don't be afraid to ask you know- the Academy does have a confusing layout- I find myself still getting lost sometimes too- that reminds me of this story I read about the Tokyo Metro."
    Yuki "Apparently the layout is so confusing even locals get routinely lost on them."
    MC "Yeah, I uh, heard that before too."
    Yuki "Really? I was skeptical at first but I guess it is true- have you ever gotten lost at a city metro station before?"
    MC "Nope... can't say that I have... {w}Yup, we'll go with that..."
    show Yuki happy
    Yuki "Really? That's good- apparently it happens all-the-time and it's a really big problem for some-"
    show Yuki surprised
    extend " Daichi-kun?"
    MC "?"
    jump RM002_After_C1

label RM002_C2_1:
    "Watching the staff member walking back into the office, there wasn't really an opportunity for me to further stall the situation even if I wanted to. Seeing her disappear back into the office, his fate was sealed."
    MCT "He made his bed, now he can lie in it. {w}I should probably leave so he doesn't have an opportunity to point fingers while I'm still around."
    Yuki "It's crazy how often I help people with directions as a hall monitor- I don't blame people because the Academy's layout is like super confusing- I find myself still getting lost sometimes too- that reminds me of this story I read about the Tokyo Metro-"
    MCT "On second thought, I have the perfect alibi with Miss Chatterbox here to verify I hadn't done anything this whole time."
    "I tried listening for any commotion in the office, but my ability to discern subtle noises was being drowned out by the unrelenting auditory assault of Yuki's flapping gums."
    Yuki "Apparently the layout is so confusing even locals get routinely lost on them- I mean that sounds really bad if people that take the train everyday still get switch around- why does it have to be confusing? trains can only go two directions-"
    MCT "Since when did we start talking about the Tokyo Metro system? Thing's a nightmare, I got lost riding it more times than I cared to remember."
    Yuki "I wish they had a train on this island- it'd be so much faster than taking the bus- but I guess there's not enough people here- I guess it's not that bad since we don't have to walk to get to town- oh my gosh could you imagine!"
    MCT "Why is she still talking?"
    show Yuki happy
    "I was beginning to lose my patience over how she could be so oblivious about anyone wanting to continue this conversation, but looking at her smile and hearing the excitement in her voice, I realized she was just happy to have someone listen to her."
    MC "Sorry, I didn't get that last part, could you repeat it?"
    Yuki "Oh, sure. I guess I was going a little fast. What I was saying was-"
    show Yuki surprised
    extend " Daichi-kun?"
    MC "Hm?"
    jump RM002_After_C1

label RM002_After_C1:
    show Yuki surprised at altMove(0.5, 0.25)
    show RM neutral at Position(xcenter=0.75, yalign=1.0) with easeinright
    play music Rain
    "I turned around to see Daichi, opting for the \"hiding in plain sight\" approach rather than stealth after pulling off the heist."
    "Seeing as he wasn't being escorted out of the building by security, Daichi must have managed to slip away undetected. {w}How, I have no idea, and I doubted he'd even tell me, but I was impressed." 
    MCT "Wait a second... Daichi-kun? {w}How does she know him? I don't even see him talk to other people besides me. {w}Does the student government already have a file on him? He must already be rattling some cages."
    show RM doubt
    show Yuki neutral
    RM "Yuki-chan."
    Yuki "I know that look, just what are you up to Daichi-kun?"
    MCT "Maybe the heat really is on him."
    "Perhaps not without reason either. I noticed he was carrying the same audio device he built in his hand."
    MCT "Wait, did he have that before he went into the office?"
    if getFlag("RM001_Device"):
        MCT "Shit! I really could get pegged as an accomplice in this whole thing since I helped him with that damn device. I should have known nothing good could have come of that thing."
    show RM happy
    RM "Nothing. Just, uh, taking a walk across campus trying to familiarize myself with the place."
    MCT "Says the guy who's probably committed the blueprints to memory."
    Yuki "I was suspicious before but now I'm certain you're hiding something."
    show RM distrustful
    RM "It's nothing. You don't need to worry about me."
    Yuki "I'm tired of this Daichi-kun. I've put up with your shenanigans for a long time because I hoped some day you'd eventually let things go. I thought this new school could be a new start in a new place where you could leave things behind."
    show RM sad
    Yuki "How long are you going to keep up with all of this? You're always so paranoid and obsessed, you never make time for your friends or to hang out and have fun like a normal person. It's hurting you."
    Yuki "Why do you keep doing this?"
    show RM angry
    RM "This time it's something different. You know {i}exactly{/i} why. This time it's even more important."
    Yuki "But it's not just nothing is it? What were you doing just now? Tell me for real."
    show RM concerned-2
    "Daichi clutched the device closer to himself, but mulling it over he reluctantly decided to hand it over to Yuki."
    "Yuki took the device from him, obviously upset once she realized what it was. She quickly looked around to make sure none of the staff were in sight before laying into him."
    show RM concerned
    Yuki "{size=-6}Is this what I think this is? What on earth is wrong with you? I can't understand how you could be so stupid. Do you know what would happen to you if you were caught with this? You could be expelled!{/size}"
    show RM distrustful
    RM "It's not what you think. {w}Look, there are a lot of suspicious things going on here. It's not just me either, anyone can see that. I've got to get to the bottom of this."
    Yuki "Knowing you, it's exactly what I think. Did you ever stop to think what kind of position this puts me in as part of the student council? What would our father think if he caught you doing this?"
    MC "Father? So this is-"
    show RM neutral
    RM "My sister, Yuki Utagashi. Yuki, this is my roommate Keisuke Hotsure."
    show Yuki happy
    "Yuki's expression suddenly perked up in contrast to the diatribe she had just laid into her brother with."
    show RM smug
    Yuki "Oh! Very pleased to meet you Hotsure-san. It's exciting to finally meet Tomoko-chan's brother. I mean I feel like we already kind of know each other since we've been talking for a while, but now it feels like we really met!"
    hide RM with dissolve
    if isEventCleared("MC003"):
        MC "Uh, likewise, it's nice to-"
    else:
        MC "Oh, speaking of Tomo I was wonder-"
    show Yuki neutral
    show RM concerned at Position(xcenter=0.75, yalign=1.0) with dissolve
    Yuki "Not so fast! Get back here Daichi-kun." 
    "Apparently Yuki was used to Daichi's Houdini bit because she didn't fall for the distraction."
    Yuki "Just what are you hoping to accomplish with all of this anyway? How is this supposed to help anyone?"
    show RM distrustful
    RM "To answer your question, I think dad would absolutely understand it. {w}Sometimes people keep the truth behind closed doors." 
    RM "If that means I have to get my hands dirty to get a hold of it, so be it. {w}But a truth brought to light always has major consequences for those that would try to hide it."
    Yuki "What you're doing and how you're going about it is wrong."
    show RM angry
    RM "So I'm supposed to just politely ask people to turn over documents and divulge information that incriminates them in a cover-up? Turn a blind eye to deception because that's the more polite and decent thing to do?" 
    show RM neutral-2
    RM "Even you should know these things don't always fit into nice little boxes of \"right\" and \"wrong\". The truth is more nuanced than that. It always has been."
    Yuki "Oh, don't pull this truth crusader crap with me. You know full well this isn't the kind of thing our father would approve of."
    show RM doubt
    Yuki "I'm taking this. You're going to go back to your room and consider where this behavior is leading and the path you're choosing to go down." 
    Yuki "You're lucky I had hall monitor duties today and not someone else, or you would have landed yourself in big trouble. {w}You're welcome by the way."
    show RM concerned-2
    RM "..."
    "Before walking away, Yuki turned her attention back to me."
    Yuki "{i}Sigh{/i}. I have to ask Hotsure-san, since you are Daichi-kun's roommate, are you caught up in this stuff too? Does he have you going along with this conspiracy nonsense?"
    MC "Huh? I was just passing by, I hadn't planned on being here in the first place."
    if getFlag("RM002_Favor"):
        $setAffection("RM", 1)
        show RM smug
        "Over Yuki's shoulder, Daichi gave me a knowing look."
        if checkAffection("RM", ">", 2):
            show RM neutral-2
            RM "He's telling the truth Yuki-chan. It wasn't his fault, he was just passing by."
    else:
        show RM distrustful
        "Over Yuki's shoulder, Daichi was eyeing me curiously. Probably wondering why I didn't just snitch on him instead."
    show RM neutral
    Yuki "Well, that's a relief. Please, look out for my brother. I can't keep an eye on him all the time."
    MC "Sure, no problem."
    MCT "As if I can keep him in my sight when he's standing next to me."
    Yuki "Thanks, Hotsure-san. You seem like a decent guy, I trust you."
    hide Yuki with dissolve
    "Wasn't exactly how I planned on spending my time after classes. I guess it was a bit of an adventure, but not really a good one. By this point I was exhausted and just wanted to go back to my room and rest."
    MC "Hey, you heading back to the dorm?"
    show RM concerned-2 at altMove(0.5, 0.5)
    "Daichi only nodded his head in return, and kept his head down as we started walking back."
    MC "Uh, hey. You, um, what to talk about what happened back there?"
    RM "No, not really."
    MC "That's fine."
    show RM concerned
    RM "{size=-6}...the records... why were they incomplete?{/size}"
    MC "Hm? Did you say something?"
    show RM concerned-2
    RM "Nah, it's nothing."
    jump daymenu

label RM003:
    if checkAffection("RM", ">=", 2):
        scene Dorm Interior with fade
        play music MC
        "Coming back to my dorm after classes, it felt good to take a load off at the end of the day as I tossed my backpack at the foot of my bed and jumped on my bed, landing starfish style face down on my bed."
        MC "{i}Ahhhh{/i}..."
        MCT "That hits the spot."
        scene black with fade
        "I slowly began to drift off into a peaceful slumber as the pent up frustrations and boredom of a full day of classes began to melt away."
        pause 1
        RM "Are you seriously going to take a nap right now?"
        MCT "... Huh?"
        play music RM
        scene Dorm Interior
        show RM neutral
        with fade
        MC "It's as good a time as any."
        show RM neutral-2
        RM "Is that so?"
        MC "Yes. Or at least it was. I'm feeling wide awake now, for {i}some{/i} reason. What are you doing here anyway?"
        RM "I live here."
        MC "Could have fooled me. You're hardly ever here."
        RM "The amount of time you spend sleeping would make anyone seem absent."
        show RM smug
        RM "It's honestly impressive sometimes the things you manage to sleep through."
        MCT "What does that mean? Just what the hell is he working on late at night in his room then?"
        MC "Yes, well this vampire needs to retire to his cotton sheet coffin before he turns to dust. Nice catching up with you Daichi, good to know you're still alive."
        show RM doubt
        RM "Actually, before you slip back into your usual comatose slumber, I was wondering if you'd be up for going with me to follow up on something." 
        show RM happy
        extend " I think I got a promising lead, but I could use another set of eyes."
        "The more sensible part of me thought I should dismiss this as more of his usual nonsense, but admittedly it did manage to spark a bit of intrigue with me."
        "Though certainly not my first choice, curiosity ultimately prevailed, in no small part however to Daichi ruining my efforts to fall asleep in the first place."
        MC "Alright, let's go."
        show RM smug
        RM "Perfect."
        scene black with fade 
        pause .5
        scene Lake Road with fade
        play music MC
        MC "Where exactly are we going?"
        show RM neutral-2
        RM "You'll see."
        "Daichi for his part wasn't much of a conversationalist. He seemed a bit on edge, which I attributed to him making sure we weren't being followed, for whatever reason that was relevant for." 
        hide RM with dissolve
        if getFlag("MC005RM") or isEventCleared("FMGWG001") or isEventCleared("MC007"):
            "Part of me began to wonder if this was just another wild goose chase based on another one of his hairbrained theories, but it was too late to back out now."
        "Without any real conversation, my mind began to be preoccupied by the scenery. Even though I had been here before, I still felt kind of lost. I hadn't actually navigated this part of the island by myself to know where I was going."
        "I probably should have paid better attention at the time when I ran into Honoka and she led me back to campus, but I had been so bowled over by running into a long lost friend I hadn't bothered to drink in the scenery like I was now." 
        if getHighestAffection() == ("BE"):
            "I should invite her back here one of these days. We could do something fun by the riverside just like old times."
        else:
            "It reminded me of that sensation I felt then, starting something new that I didn't completely understand... and well, still don't. Hell, I don't even know what I'm doing here now."
            "But I'm not so worried about that anymore. I still got time to figure things out. Though with all the odd things I've seen so far, that'll be easier said than done."
        scene Dock with fade
        "After a brief stroll down memory lane (more literally than figuratively in this case) we eventually arrived at the dock. The first place Tomo and I arrived at on the island." 
        "I recognised the red gate, just as large and imposing as the day I arrived. At the time it felt like it marked a point of no turning back." 
        "Looking at it now with the ocean in front of me though, it felt more like a locked door to keep us from leaving. It was a little unsettling to be honest."
        show RM smug with dissolve
        play music RM
        jump RM003_After1
    else:
        scene Dorm Interior with fade
        play music MC
        "Coming back to my dorm after classes, it felt good to take a load off at the end of the day as I tossed my backpack at the foot of my bed and jumped on my bed, landing starfish style face up."
        MC "{i}Ahhhh{/i}..."
        MCT "That hits the spot."
        "The warm sunbeams peaking through my glass balcony door beckoned me outside to enjoy the mild spring weather."
        MCT "Not today I'm afraid."
        "Breaking from the soft embrace of my mattress cushion, I got up to draw the blinds from my window to make sure the pesky light wasn't going to interfere with the quality snooze session I had planned."
        MCT "Assuming Daichi doesn't interrupt it somehow either."
        "I don't know why that thought entered my mind. Despite living with him and having classes with him, I hardly ever saw the guy. I assumed in his spare time he was always out doing reconnaissance on... well whatever it is that he does."
        MCT "Odd fellow, that's for sure. I wonder what he's up to?"
        "I had no real way of knowing, seeing as he was around, but looking over to his side of the room something odd stuck out to me."
        MCT "What's this?"
        "It appeared to be a bright neon green sticky-note attached to the back of his chair with today's date marked on it." 
        MC "\"Suspicious activities - sea ferry dock - 16:30\""
        MCT "What?"
        "Were these some kind of plans of his? He wasn't exactly the type to leave a note telling me where he went. Quite frankly, I didn't need to know and he didn't need to tell me."
        "I wanted to forget this whole notion and just crawl back into bed, but now I couldn't help but suspect he was the one getting into suspicious activity at the dock." 
        "And if this was anything like his little listening device scheme, I had a feeling it would be a good idea to make sure he wasn't doing anything too drastic."
        MCT "Crap, that only gives me 20 minutes to get over there. Hopefully I remember the way." 
        scene Lake Road with fade
        "I was relieved to find my memory allowed me to retrace my steps. Maybe that wasn't a good thing though because the only reason I knew this path was because I got lost the first time." 
        "Even though I was in a hurry, I slowed down a bit to take in the view of the lake once I realized where I was at. I hadn't been here since the start of the school year when I ran into Honoka on that first day."
        if getHighestAffection() == ("BE"):
            "I'm glad I did, too. It was like we picked up right where we left off. She helped make the whole experience of moving to a new school not be so bad."
        else:
            "Starting something new that I didn't completely understand... and well, still don't, but it was a fortunate accident getting to run into a long lost friend once again. And I eventually did meet up with Tomo."
            "I guess it just goes to show things will work out if you give them a chance. I try to keep that in mind while I'm here, but with all the odd things I've seen so far, that's easier said than done most days."
        scene Dock with fade
        "After my brief jog down memory lane (more literally than figuratively in this case) I eventually arrived at the dock. The first place Tomo and I arrived at on the island." 
        "I recognised the red gate, just as large and imposing as the day I arrived. At the time it felt like it marked a point of no turning back." 
        "Looking at it now with the ocean in front of me though, it felt more like a locked door to keep us from leaving."
        stop music
        MCT "{i}Ack!{/i} What the hell is that?"
        "I had been lost in my thoughts as the memories rushed back to me, but that was interrupted as an annoying flash of light flickered in my eyes."
        "I just dismissed it as some kind of errant reflection across the water but the repeated nature of it felt more like a signal than a fluke."
        MCT "Wait a second..."
        play music RM
        show RM smug with dissolve
        MCT "A signal huh?"
        "There he was, sitting on one of the benches dockside \"reading\" a newspaper."
        MC "You could have just called my name you know."
        show RM doubt
        RM "I suppose I should have if I had known you were going to just saunter over here in broad  daylight to blow our cover."
        MC "Students walking about is a common sight on the island. Being the only person under 50 that still reads a newspaper sticks out."
        show RM neutral
        RM "Hmm, perhaps hiding in plain sight is the best option for the moment."
        MC "What are you doing here?"
        show RM distrustful
        RM "I could ask you the same question."
        MC "Oh, don't give that. You just tried to get my attention using your eyeglasses to blind me. I have to assume you were expecting me."
        show RM smug
        RM "And to think I thought you'd just sleep through the afternoon. I was curious to see if you'd manage to pick up the bread trail I left to come." 
        $setAffection("RM", 1)
        extend " You didn't disappoint."
        jump RM003_After1
        
label RM003_After1:
    play music Beach
    MC "So what's going on here, why this place?"
    RM "You tell me. Take a look. Anything stick out to you?"
    "Looking out across the pier, we were far from the only people here. Foot traffic was starting to pick up as people moved about to and fro." 
    "It looked like people were getting tickets from a nearby kiosk while others who already had theirs in had lined up on the pier to begin boarding on the ferry that just docked."
    "Despite the sudden hustle and bustle normally absent on this sparsely populated island, nothing seemed out of the ordinary to me."
    MC "Not really, what do you see?"
    RM "Not {i}what{/i}, but {i}who{/i}."
    "Daichi's nod in the general direction helped me to zero in on what he had managed to pick out from the crowd. A young woman in a white nursing outfit with a surgical mask on."
    MC "Wait a second, that's the school nurse."
    show RM happy
    RM "Exactly. Hitomi Kiyomi is her name."
    MC "Oh yeah, I remember now. How could I forget? That shot hurt."
    MC "What is she doing? It's a weekday. The ferry trip seems a bit too long for a daily commute."
    show RM neutral-2
    RM "Correct. Even though it's not that late, it's still the last one of the day."
    "Not exactly the reaction I was expecting. Daichi was usually keen to jump on anything that could possibly be construed as a little too convenient."
    MC "I take it you were expecting her to be here then?"
    RM "Like clockwork."
    if isEventCleared("FMGWG001") or isEventCleared("MC007"):
        MC "Is this another stakeout? Between Kazomazumi-san and now Nurse Kiyomi I'm starting to think you got a thing for older women."
        show RM angry
        RM "Tch, shut up."
        MC "Don't worry, your secret is safe with me."
    elif getFlag("MC005RM"):
        MC "Is this another stakeout? Honestly I didn't think you had a thing for older women after the last time."
        show RM angry
        RM "Tch, shut up."
        MC "Don't worry, your secret is safe with me."
    else:
        MCT "At this point, I don't think I even want to know how long he's been tailing her to know her schedule this well."
    MC "So what's the deal with her then and her schedule then if I'm supposed to ignore the stalker angle?"
    show RM neutral
    RM "Let's just say she's been a person of interest to me since the day they all had us measured and told us our factors."
    MC "Why's that?"
    show RM distrustful
    RM "I have a sneaking suspicion she knows a lot more about the factors than she lets on. After so many years of observation, how could she not?"
    MC "I thought you skipped out on measuring day? Matsumoto-san asked me where you were and I was just as clueless as she was."
    show RM sad
    RM "I was there. I planned to observe unseen, but I had severely underestimated Hageshi-sensei's auditory acuity."
    "A sly smile crept across my face as I imagined Hageshi-sensei dragging Daichi by the ear up to the nurse's station."
    show RM angry
    RM "What's so funny?"
    MC "Oh, nothing. {w}Go on, you were talking about how Nurse Kiyomi might know about the factors."
    show RM neutral-2
    RM "One of the people anyway."
    MC "What? You have a list going or something?"
    show RM neutral
    RM "...Yes."
    MC "Probably should have guessed that already."
    RM "Nurse Kiyomi caught my attention for being a staff member as well as a former student."
    MC "So? Tashi-sensei and Hageshi-sensei would have been former students too. Heck, plenty of other faculty and staff now that I think about it."
    show RM neutral-2
    RM "You didn't let me finish. Nurse Kiyomi is an interesting case in that she also has a sibling with a factor as well."
    "Suddenly, I was much more curious about where Daichi was going with this."
    RM "I was initially curious about her anyway. During the \"Measuring Day\", as they called it, I had attempted to ask her more about what growth my sister had been diagnosed with." 
    show RM distrustful
    RM "But she completely stonewalled me when I asked any questions, citing school policy."
    if isEventCleared("MC003"):
        show RM neutral
        RM "A similar experience to what you had apparently."
        MC "Yeah I wasn't too happy about it either."
    else:
        MC "Sounds pretty similar to what I had to deal with from her."
    show RM doubt
    RM "Considering her and my sister share the same factor, her adamant silence on the matter was all the more frustrating in retrospect. Having since learned she also has a sibling with a factor, I find it to be down right infuriating." 
    MCT "So that's what his sister's factor was... {w}I thought she just went a bit too heavy on the lip gloss when I saw her."
    MC "That is kind of shitty. You'd think she'd at least want to help out. Though I guess she could have gotten in trouble if she made an exception just because she felt sorry for either of us."
    MC "I mean, to be fair it does seem like something people need time to process on their own."
    show RM angry
    RM "And who's to say that's the best way for everyone?" 
    MC "You're not here because you hold a grudge towards her or something, right?"
    show RM neutral-2
    RM "I wouldn't go that far, but her evasiveness on the matter led me to believe she knew more than she let on." 
    RM "So I did a bit of digging into her, which yielded some interesting peculiarities I would like to get to the bottom of."
    MC "Like what?"
    show RM smug
    RM "Like here. She frequently leaves the island by ferry, mostly in the evening after her shift. It doesn't always match up with the days off on her schedule either. Sometimes she returns the next day."
    RM "The natural question is, why does she leave the island so often?"
    show RM doubt
    MC "I don't know. She's a nurse. Maybe it's to get more medical supplies? Maybe it's easier to just pick them up on the Mainland?"
    RM "That's what I would have thought, but all she takes with her is a small purse, both coming and going. You'd think if she was bringing supplies she'd at least have a case or a backpack to haul something."
    show RM neutral
    RM "Besides, Seichou Town has a hospital, she could just go there if she needed something like that."
    MCT "As peculiar as that might be, this wasn't anything to go by as far as I was concerned."
    if isEventCleared("MC003") or isEventCleared("FMGWG001") or isEventCleared("MC007"):
        MCT "Which wasn't a surprise, given what his hunch led to last time."
    menu:
        "This doesn't seem to be leading anywhere.":
            show RM concerned
            MC "Look, you seem smart enough, and pretty resourceful, but you're way too eager to jump on loose threads, and obvious red herrings."
            show RM distrustful
            RM "All leads need to be followed up on or I risk having blindspots in my investigation."
            MC "What investigation? You're stalking a person somehow hoping some magical insight is just going to drop out of the sky."
            show RM doubt
            RM "You're just impatient, these things take time."
            MC "You're willing to scrounge for the slightest thread to connect your theories but you won't bother to do the most basic of investigative work, which is interviewing witnesses. Just go talk to her and ask. What's so hard about that?"
            jump RM003_After2
        "What are you hoping to find?":
            "I figured I'd humor him to help get him to come to his senses, and he in turn seemed eager to fill me in."
            $setAffection("RM", 1)
            show RM happy
            RM "I want to know what she knows. If she's not going to tell me, then I'm going to have her show me."
            MC "Just because she didn't want to tell you about your sister's growth prior to having her tell you doesn't mean she's going to stonewall you about everything."
            show RM doubt
            RM "...I somehow doubt that."
            MC "Or you just hadn't bothered to try. Let's just go talk to her."
            jump RM003_After2

label RM003_After2:
    show RM angry
    RM "What!? No! That'll blow our cover and jeopardize everything! {w}Hey wait, come back here—"
    hide RM with dissolve
    "I left Daichi behind as I walked across the dock boardwalk to catch her before she got in the boarding queue, much to his continued protests."
    "At this point, I was getting impatient with Daichi's approach, which seemed to be \"If it's worth thinking over, it's worth overthinking.\"." 
    "I figured it couldn't hurt to try the direct approach for once."
    #show nurse with dissolve
    play music Peaceful
    MC "Kiyomi-san, nice to run into you this evening. Are you heading out on a trip?"
    show RM concerned-2 with dissolve
    Nurse "Oh! Nice to see you as well Hotsure-san, and Utagashi-san. I didn't expect to run into any students at the dock. Were you planning a trip to Wakkanai as well?"
    show RM neutral
    MC "Uh, maybe eventually, I guess. We just happened to take a walk around the area and noticed people gathering and came to see what all the commotion was. I didn't realize the ferry port was still active after it dropped us off."
    Nurse "Oh, well it's quite active. It's the main form of transportation off the island, at least for this side of the island. There is another dock and a small airport on the other side, but those are mostly for commercial purposes, not for commuters."
    Nurse "It's not uncommon for locals and academy staff to take a trip back to the mainland to see their families too. If your family ever comes to visit you they'll most likely come through here."
    MC "Why am I just learning about this now?"
    if getFlag("MC005RM") and getFlag("MC005_readbrochure"):
        show RM smug
        RM "Didn't you read the brochure?"
        MCT "Heh, surprised he remembered that."
        RM "Students have a week's worth of time they can leave the island and not attend classes with no questions asked."
        Nurse "Utagashi-san is correct. We want to foster a supportive environment at the academy, and we understand that may also necessitate some time off to help collect oneself and recenter during a time of uncertainty and changes."
    else:
        Nurse "I'm surprised you hadn't. It isn't an intentional secret by any means. Students have a week's worth of time they can leave the island and not attend classes with no questions asked."
        MC "Really?"
        Nurse "We want to foster a supportive environment at the academy, and we understand that may also necessitate some time off to help collect oneself and recenter during a time of uncertainty and changes."
    show RM neutral-2
    MC "Good to know."
    Nurse "I have to imagine it was stressful for you if you've been under the impression you've been stuck here for a while, but the academy is quite understanding and accommodating when it comes to things like family emergencies if you need to leave."
    Nurse "You also don't need to take all your time off in an entire week for it to be honored. It's for you to use as you see fit. Just be sure to inform the administration and your homeroom teacher ahead of time."
    MC "Gotcha. Well, I feel a bit better about being stuck on this rock, knowing there's a way back at least if need be."
    show RM distrustful
    "At this point Daichi was beginning to look irritated. For all my thinking of going for the \"direct approach\" I hadn't managed to probe into anything significant so far, which is probably why he was losing his patience."
    "If I didn't extract something useful out of her soon, Daichi was probably going to pounce on her with a surprise interrogation."
    MC "So, you're heading to Wakkanai?"
    Nurse "Yes, I'm visiting my fiance who lives there. We try to see each other as often as possible, but it's difficult with our schedules and his current job."
    MCT "Well that solves that mystery at least."
    Nurse "My fiancé works as a curator in the history museum at Wakkanai. He does great work, you should definitely visit next time you take a trip back to the Mainland."
    MC "Not a bad idea, Wakkanai seemed like a nice place when we drove up here and my parents dropped us off."
    "Needless to say I didn't plan on going out of my way to make a trip any time soon, but I figured if I could keep things casual it might continue to loosen her lips."
    MC "Hey, if you're gone though, does that mean no one's at the nurse's station?"
    show RM neutral
    Nurse "Oh not to worry, the medical staff on campus rotate their shifts so that someone is always on duty. You never know when an emergency might come up, so we make sure we are prepared, just in case."
    "She was certainly being helpful, but was hoping for a bit more insight about the school than that."
    MCT "I've kept things cordial for long enough to seem natural, I should be able to slip in something nonchalant to get her to talk about her factor, since that's probably what Daichi really wants to know about— even if he is too chicken to ask."
    play sound ClockTower
    show RM doubt
    Nurse "Oh! That's the call for boarding." 
    "At this point the line was starting to move and she didn't really have a choice to stay and continue the conversation."
    Nurse "I'm sure I'll see you two boys in a few days when I return. Enjoy the rest of your afternoon."
    #hide nurse with dissolve
    "As Nurse Kiyomi got swept up in the moving line onto the ferry, I couldn't help but think of the contrast between her staunch unwillingness to tell me anything about Tomo on Measuring Day, and her personable cordialness today." 
    "Listening to her talk about him, she seemed genuinely happy she was going to see her fiance. Something I never expected in a million years, given the intrusive, if not completely problematic, nature of her factor."
    "A factor, mind you, that was arguably equally shocking as Tashi-sensei's tongue. To think someone with a factor like that can still find true happiness after all..."
    MCT "{i}Blek!{/i} {w}On second thought, let's stop thinking about that."
    show RM sad
    RM "{i}Sighhh{/i}. Well that was disappointing. {w}She seemed to have her guard down. You had her on a roll there for a bit, but still, I was hoping she would offer at least a little bit of information on her factor."
    MC "Well, at least we figured out why she leaves the island so much."
    show RM concerned
    RM "I guess it ties up that loose thread, but it doesn't relate to anything with the school."
    MCT "Color me surprised."
    MC "If it's any consolation prize it seems like she's pretty happy in spite of her growth."
    show RM concerned-2
    RM "..."
    "Daichi mulled over my words in silence. Perhaps I had a point, but not one he was so willing to accept."
    show RM doubt
    RM "Seems like a far cry from a normal life to still be tethered to this island, even if she goes back to the Mainland."
    MC "What's normal anyway? Especially after what we've already seen. Seems like she found a way to move about in public without drawing attention to herself."
    show RM neutral
    RM "You mean the mask?"
    MC "I mean it's pretty common to see people wear them in crowded areas or just any time during flu season. Given that she's a health care worker, no one would bat an eye at her wearing it all the time."
    show RM neutral-2
    RM "Now that you mention it, if I hadn't been aware of what was underneath it, I wouldn't have thought twice about how much it bulged out from her face."
    MC "Maybe that's something that could work for Yuki? {w}If it comes to that I mean."
    $setAffection("RM", 1)
    show RM happy
    RM "I appreciate the thought." 
    show RM concerned-2
    extend " But it's a bit naive to assume Yuki would accept just covering up herself to hide from the world. She's so talkative and loves to chat with people, just seems like something she'd find uncomfortable and restricting."
    MCT "\"Talkative\" was an understatement based on what I heard from Tomo. \"Motor-mouth\" was the term Tomo used."
    MC "I've heard from my sister she can be rather... umm... {i}verbose{/i}."
    show RM neutral
    RM "You don't need to dance around it, I'm quite aware of the impression she makes." 
    MC "Has she always been like that?"
    show RM sad
    RM "I'm afraid so, for better or worse." 
    show RM neutral-2
    "Without any more to say on the matter, Daichi and I just stood there for a while, not saying much of anything while we watched the rest of the passengers board."
    "There were more than a few passengers where it was apparent they had some kind of growth. One gentleman in particular was so tall most of the passengers didn't even come up to chest height on him."
    if getHighestAffection() == ("GTS"):
        "This person was at his full height (I mean I had to assume given his age) but Naomi was already just as tall as he was and the year seems like it's barely started." 
        "Seeing him, I couldn't help but wonder just how much growing Naomi still had to go."
    show RM doubt
    play music RM
    RM "Hm, that's curious..."
    MC "What's that? Notice something else?"
    "At this point, given the whole thing with his sister, I was feeling a bit more patient with him, even if I'd preferred to call it for the day and head home."
    show RM smug
    RM "Look at the dock station itself. Do you notice anything?"
    MC "Not particularly, it looks like a fairly standard sea station, not all that different from what you might find on the Mainland at other dock stations."
    MC "If I had to pick out something, I suppose the red color is an interesting touch. It's a nice contrast with the backdrop of the blue ocean." 
    MC "Red being a symbol of protection and peace, while blue being a symbol of luck, which can have a soothing effect. If I had to guess, this was intended to invoke a wish for a safe journey for those coming in and going by sea."
    "Daichi nodded in agreement."
    RM "Yes, which is quite suspicious considering so many arrivals are coming into the unknown, or ending up living here forced to deal with the changes to their bodies. Doesn't really fit with this sense of \"soothing\"."
    MC "You think there's some particular significance to it? It's most likely done for cultural and spiritual tradition reasons, which are commonly incorporated into architecture. You're stretching things a bit too far here I think."
    show RM doubt
    RM "Perhaps. {w}Perhaps not."
    show RM happy
    RM "Look at this roof over the pillars. Typical for shelter from rain and snow while people wait for the ferry to arrive. But, consider where we are."
    MC "I'm not following."
    show RM smug
    RM "Think about it. This academy is intended for people with various growths that are well above normal, and that's just what the school has told us. All manner of things, from breasts bigger than our heads or people as tall as small trees!"
    if isEventCleared("FMGWG001") or isEventCleared("MC007"):
        "I hadn't seen anyone that tall, but he did have a point. Seeing the bakery owner that one day and the size of her chest was quite the shock. I hadn't seen anything like it outside of a hentai comic."
        MCT "Was Honoka going to grow that big?"
    MC "So they should have built this thing bigger or something? Seems big enough to me."
    show RM neutral-2
    RM "Big enough for us maybe, but the taller passenger that was boarding earlier made me think of something."
    RM "I had heard some rumors about a so-called giant's dorms, a residential area for giants, hidden from normal view of the public."
    show RM neutral
    RM "But why isn't the existence of such giant people more well known if, as Nurse Kiyomi suggested, every student can leave the island when they see fit?"
    "I wasn't that keen on forming a conclusion based purely on his assumptions stacked on top of assumptions, but it was curious nonetheless." 
    "You would expect something like an entire community of giant people, beyond taller than what was considered to be humanly possible, would make international headlines."
    MC "It does seem odd, but what does that have to do with the sea dock?"
    show RM doubt
    RM "Think about it. The dimensions of everything at the school are completely outsized compared to normal dimensions to accommodate the student population. If it weren't, then there's a risk some might not fit."
    MC "Maybe this was built here before the school."
    show RM distrustful
    RM "Maybe it wasn't though, and was purposefully made this size."
    MC "Purposefully not fitting students?"
    show RM smug
    RM "Exactly. What if this is an actual gateway, one that bars those that have grown too tall from leaving on the ferry?"
    "Looking at the height of the gate's ceiling, the thought of someone standing tall enough for their head to touch the roof seemed surreal to imagine." 
    "But if someone were in fact that big, how would they get on the passenger ferry, even if they did have to duck under to get through?"
    "It was a mad jump in logic to pull such a conclusion based on a seemingly small architectural oversight, but it somehow managed to make enough sense to have a kernel of plausibility."
    show RM happy
    MC "I don't know if this has to do anything with it, but it could explain why the existence of these so-called giants aren't more widely known."
    "I could feel my stomach rumbling, which led me to check my watch."
    show RM neutral
    MC "Ouch, it's getting kind of late. We should probably head back if we want to catch dinner at the cafeteria."
    show RM distrustful
    RM "Food can wait. I think we're onto something here."
    MC "Yes, food can wait. It can wait while I walk back to campus before I eat it." 
    RM "I'll catch up with you later."
    MC "Oh come on, let's go. We've spent enough time out here already and I don't think we're going to learn anything new from the dock after today anyway."
    if isEventCleared("MC002"):
        MC "Why not just ask Tsubasa-sensei? He'd probably know something. He's been teaching at the school for a really long time. Heck, he might have been around before they built the thing."
        show RM doubt
        RM "Nothing about him suggests he takes notice of these kinds of things. He's always so disinterested in everything I doubt he'd even remember these kinds of small details, even if he was around at the time."
        MC "Still though, might be worth a shot."
    MC "Besides, you could always just ask Tashi-sensei about it when we have class with him. Although you might want to wait for a day when he's in a good mood."
    show RM neutral
    RM "You're probably right. He's not typically in the mood for conversation, but he would likely be pretty keen on the historical details of this place, being the history teacher and all and having lived here most of his life."
    play music MCGuitar
    scene Lake Road with fade
    "I honestly didn't expect my reasoning to convince him to temporarily suspend his investigation, but it seemed to satisfy him for the moment."
    scene Cafeteria 
    show RM neutral
    with fade
    "We went back to campus and managed to get to the cafeteria before it closed. He spent most of the time jotting down notes in his little black book while muttering to himself." 
    "In spite of the lack of conversation, I realized eating dinner in the cafeteria here with him was the first time we actually hung out together that didn't involve something to do with his investigations."
    jump daymenu
