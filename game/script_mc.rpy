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
            "(DEBUG) Skip intro":
                jump daymenu
            "View intro":
                pass

    #SFX Light Motor SFX
    $showQuickMenu = True

    pause 1.5
    scene Ferry with fade
    play music MC
    "The hard bench under me lightly hummed with the vibrations of the ferry. Two hours of sitting here twiddling my thumbs and scrolling through my phone had left me beyond bored."
    "I leaned against the side of the boat, looking out across the shimmering, tranquil sea as the salty air blew through my thick, brown hair."
    "Not finding anything interesting to look at aside from water and sunshine, I turned back and glanced at my sister beside me, her gaze buried deep in the glass of her phone."
    MC "Nervous at all?"
    $setTomoOutfit(OutfitEnum.CASUAL)
    show Tomoko distracted with dissolve
    Tomoko "Mm... nah."
    MC "Not even some new school jitters?"
    Tomoko "Nope."
    MCT "Don't know what I expected. Even earthquakes couldn't freak her out."
    play sound ClockTower
    "Overhead, one of the many loudspeakers dotted throughout the ferry whined."
    Announcer "Your attention, please. We will be docking in five minutes. If you aren't already, please take your seats. Thank you."
    "A few of the other students that had been milling around came to sit back down."
    "I leaned my head against the glass beside me. Ahead, a large, lush, green island loomed over us."
    MC "Well, that's welcoming."
    show Tomoko distracted
    Tomoko "Did you say something?"
    MC "You know, since we're not going to know anyone else here, the least you could do is be a little more social."
    show Tomoko neutral
    Tomoko "For what? We're only going to be here for a year. Odds are that we'll never see most of these people again anyway."
    MC "A lot can happen in a year, Tomo."
    show Tomoko annoyed
    Tomoko "Yeah, yeah. I don't need a full inspirational speech, Kei."
    show Tomoko neutral
    "I scoffed and looked back at the island."
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
    "The voice over the PA system rang out through the deck, causing a few of the other students to look up from their phones while others readied their bags for departure."
    Announcer "Group one, please exit off of the left side of the ferry. An attendant will be ready to lead you to registration on arrival."
    Announcer "Group two, please exit off of the right. Groups three and four, please wait until we're ready for you."
    hide Tomoko neutral with dissolve
    "Tomoko and I got up from our spots and shuffled in the crowd of students toward the center of the ferry."

    scene Dock with fade
    play music Country
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
    "On her chest hung a bright nametag that read ‘Aoi Takamura'."
    show Tomoko neutral with dissolve
    Takamura "Can I get your name, please?"
    Tomoko "Tomoko Hotsure."
    Takamura "Right... there you are! Here's a key for your dorm. We have a mandatory assembly tomorrow morning, so be sure not to miss it!"
    Takamura "Group one, right over there. Just follow them to the academy. Welcome to Seichou!"
    Tomoko "Alright. Later bro."
    MC "Yeah. See ya."
    hide Tomoko with dissolve
    Takamura "And, your name, please?"
    MC "Keisuke Hotsure."
    Takamura "Another Hotsure? Okay... one second...{w} Ah! There you are."
    "The teacher blinked a few times."
    Takamura "Hmm... two Hotsures and two Utagashis. Curious..."
    "The teacher briefly scanned the table and grabbed something from it, then turned and glanced off at the group of students who were already almost out of sight."
    Takamura "Well, looks like they were a little eager to get a move on. Just follow this path here all the way down."
    Takamura "And, here's a key for your dorm! As I'm sure you heard, assembly is tomorrow morning in the auditorium. Welcome to Seichou, Hotsure-san. Hope you enjoy your stay here!"
    MC "Alright. Thank you very much."
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
    MC "I swear. Your words were, and I quote: 'I'll end up a beautiful princess, and you'll probably end up living in ooze.'"
    show BE happy
    BE "Noooo, I said 'living the... schmooz...y life?'"
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
    MC "...swimming at the beach."
    $setSkill("Athletics", 3)
    show BE surprised
    BE "Whoa, really? Kei{i}-chan{/i} the beach bum?"
    show BE happy
    BE "I'd never figured you the type. Are you a hunk now? Can I squeeze your bicep?"
    MC "Oh, hush."
    jump global000_cbreak_after

label global000_cbreak_2:
    MC "...at the library."
    $setSkill("Academics", 3)
    show BE surprised
    BE "The library?!"
    show BE sad
    BE "Were you kidnapped or something...?"
    "I laughed in spite of myself."
    MC "No! I just, I was curious about stuff we never learned in high school."
    MC "Things like how to say 'hello' and 'thank you' and stuff in a bunch of languages, weird science things they don't let us play with in chemistry class, all sorts of neat stuff..."
    show BE happy
    BE "Gosh, when you put it like that, it doesn't sound like studying!"
    show BE happy with hpunch
    "I let out a guffaw, and Honoka slugged me on the shoulder."
    BE "That means I can copy off your notes, now that you're a brainiac, right?"
    jump global000_cbreak_after

label global000_cbreak_3:
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
    RM "Don't get any funny ideas, 'Keisuke Hotsure.' I've got my eye on you..."
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
    RM "Haven't you ever seen those people on the news?{w} The giants over ten feet tall,{w} the gravure idols with 40kg breasts,{w} all the record holders for biggest this and longest that?"
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
    if getAffection("RM") >= 0:
        show RM neutral
        RM "Today's the welcoming ceremony. I'm going to go get the lay of the campus."
        MC "You're going to skip the opening ceremony?"
        show RM angry
        RM "Of course not.{w} I need to get the official story so I know where to start investigating."
        hide RM with dissolve
        "I shook my head, but waved goodbye nonetheless as Daichi left. At least he seemed in good spirits."
        $ setFlag("global000_RM_friendly")
        jump global000_part2
    if getAffection("RM") < 0:
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
    MCT "Now... where should I sit...?"
    menu:
        "I should sit in the front where the Principal can see me.":
            jump global000_sit_c1
        "I should sit somewhere in the middle.":
            jump global000_sit_c2
        "I should sit in the back, where no one will notice me.":
            jump global000_sit_c3

label global000_sit_c1:
    "I decided to sit in the front row, where the principal could see me. If I ever needed to speak with him, recognizing my face might make him better disposed toward me."
    MCT "This is a good seat... Got spaces on either side of me."
    "{color=#FF69B4}*FLUMPH!*{/color}"
    MCT "!!"
    MCT "I... Is that..."
    show AE neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    MCT "Shiori's butt is overflowing her seat and pushing against me...{w} I can't say anything about it with everyone else around..."
    MCT "I'll just quietly scoot away from her-"
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


label global000_sit_c1_1:
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
    MC "What was your previous school like, Yamazaki-san?"
    show GTS neutral
    GTS "Mine?"
    MC "Sure, you heard about ours..."
    show BE neutral
    BE "Yeah, what was yours like, Yamazaki-san?"
    show GTS neutral
    GTS "Well, ah, it was...{w} pleasant, I suppose."
    MC "'Pleasant'?"
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
    $setFlag("global000_satPRG")
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
    Principal "'Nosce te Ipsum.' {w}Latin, 'To thine own self be true'. Remember that you are more than your station, {w}skills, {w}and especially appearance. If you need help, your teachers are always available to help you with whatever you need."
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
    AE "A more apt question would be 'Where is Utagashi-san'? This assembly is mandatory."
    AE "He's your roommate, is he not?"
    menu:
        "I haven't seen him...":
            jump global000_aftersit_c1
        "He said he wouldn't miss the ceremony..." if getFlag("global000_RM_friendly"): #This menu item will only appear if this variable is True
            jump global000_aftersit_c2
        "He left the dorm pretty early..." if not getFlag("global000_RM_friendly"): #Likewise, this item only appears if the variable is False
            jump global000_aftersit_c3


label global000_aftersit_c1:
    MC "I haven't seen him...{w} but he was acting kind of strangely this morning. No telling where he went off to."
    show AE neutral
    AE "Well... I certainly have no reason not to trust you, so that's that."
    hide AE with dissolve
    "I left to go to my homeroom class, worrying no excuse would be good enough for Shiori..."
    $setAffection("RM", 1)
    jump global000_homeroom

label global000_aftersit_c2:
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

    scene Classroom with fade
    MC "Whoa!"
    show WG neutral with dissolve
    WG "...Is this for real?{w} How come there are so few seats?"
    hide WG with dissolve
    show PRG neutral with dissolve
    PRG "And... so far away..."
    hide PRG with dissolve
    show AE neutral with dissolve
    AE "Some kind of anti-cheating measure...?"
    hide AE with dissolve
    "I walked to a desk and gazed down at it."
    MCT "Why exactly is this seat so huge? Hell, the whole desk could fit three or four of me."
    "One by one, we all took our seats, looking around at the sparse classroom. All the usual educational aids seemed to be on shelves or set into the wall, making the room seem even more like an empty box than it already was."
    "If not for the teacher's lectern at the front of the class, you'd be forgiven for thinking we were in a pen instead of a classroom."
    "Finally the bell rang, and at the last possible second one could enter and not be late, our homeroom teacher slid open the door and entered."
    show HR unique with dissolve
    MCT "'Dour' is the first word that comes to mind... Guy looks like he's been middle-aged his entire life."
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
    show HR neutral
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
    show HR neutral
    "..."
    "..."
    play music Busy
    HR "All right, go ahead, get it out now."
    "The nonchalance in the teacher's voice quickly turned the class' mood from panic to confusion, especially as that giant tongue continued to flop around as Tashi-sensei got into his bag and set his papers down on the lectern."
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
    "Tashi-sensei scanned the room, taking in the fear and confusion, then shrugged."
    HR "Anyways, that's my big first day speech. Don't expect more.{w} So, roll call. Matsumoto-San?"

    scene black with dissolve
    stop music fadeout 1.0
    "So I found myself at Seichou Academy, orientation behind me and a long, strange journey ahead."
    "What was I supposed to do now, knowing what I do about the bodies of the student body?"
    jump daymenu

label MC001:
    scene Dorm Interior with fade
    play music MC
    "The first day of class was certainly interesting... {w}bizarre, surreal, confusing— all manner of strange and unsettling characterizations came to mind, but I chose to stick with interesting for the sake of my own sanity."
    "Normally I'd like to sleep in as late as feasibly possible while still avoiding being late to class. I was pretty good at the first part, but hadn't mastered the second, even after 18 years of practice."
    "After recent events, I'm not too sure who would have slept soundly all through the night. Well, maybe Tomo. I don't think she'd even wake up for a firestorm during an earthquake."
    "Since I was already awake, I decided to just get up and get ready for class. After getting dressed, I was ready to head out."
    "I cracked the door open to leave when I noticed a lanky, clammy hand slowly shoving the door back shut."
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
    RM "{i}Tck{/i}. Don't be so quick to accept just anything. Ever heard the expression ‘Don't believe anything you hear, and only half of what you see.'?"
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
        "Like the tall buff teacher Hageshii-sensei that was supposedly ‘small' for his growth. The guy is more than twice normal size with like zero percent body fat."
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
    RM "It probably has to do some randomization pairing based off of alphabetical order. Not every coincidence is that intriguing."
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

    scene Dorm Exterior with fade
    play music MC
    "What felt like hours for me was probably just 20 minutes before Tomo texted back."
    TomokoCell "What do you want? Why did you have my roommate wake me up?"
    MCCell "Just meet me outside the dorm. I got something for you."
    TomokoCell "This better be good."
    "I knew Tomo wasn't going to set any landspeed records with her level of urgency, so I just bided my time sitting on one of the benches outside the dorm until she came out."
    show Tomoko neutral with dissolve
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
    Tomoko "Alright I guess. People here seem nice. There doesn't seem much to do around here though."
    MCT "I don't know why you care. If there were a million things to do, you'd still choose to nap."
    MC "I mean how are you holding up after, you know, the test?"
    show Tomoko distracted
    Tomoko "We haven't been here that long. I have had any major tests in classes."
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
    Tomoko "Okay. I'll keep that in mind. Later."
    hide Tomoko with dissolve
    "I suppose I got all worked up for nothing. But something about all this was strange. I had no idea what we were getting into, but something told me it wasn't all going to go away with just a haircut."
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
    if getSkill("Athletics") == 0:
        "It'd been a while since I'd done anything athletic. I was probably going to be sore tomorrow, whatever this was."
    elif getSkill("Athletics") >= 3:
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
    #show Hageshi neutral with dissolve
    show HR at altMove(0.5, 0.25)
    show RM concerned-2 at Position(xcenter=0.75, yalign=1.0) with dissolve
    Hageshi "Look what I found crawling in the vents."
    "Hageshi-sensei was carrying Daichi by his collar, like he had pulled out a stray cat from a storm drain."
    Hageshi "Nice try Utagashi-san, but no one gets out of this."
    HR "Thank you, Hageshi-san."
    hide RM with dissolve
    extend " Well, looks like the gang's all here. Let's get into what you'll be doing. I'll let Naoki-san give you the run-down."
    hide HR with dissolve
    #hide Hageshi with dissolve
    play music Busy
    #show Naoki neutral with dissolve
    Naoki "Thanks Tashi-san. You can all just call me Coach Naoki or Naoki-sensei."
    Naoki "Today we're going to be playing a game called handball. It's not that difficult to explain, it's basically like football where you pass the ball and score only using your feet, but with your hands instead."
    show WG doubt with dissolve
    WG "In America, football means something entirely different."
    Naoki "Hmm, yes in Australia too. Okay, maybe that wasn't the best analogy, but it is still a simple sport by most standards."
    hide WG with dissolve
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
        jump MC006_Team1
    elif getHighestAffection() == ("WG" or "FMG" or "PRG"):
        jump MC006_Team2
    else:
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
    Naoki "Alright, Team 1 is Hotsure-san, Inoue-san, Yamazaki-san, and Matsumoto-san. Team 2 is Utagashi-san, Nikumaru-san, Mitzutani-san, and Kodama-san."
    show WG doubt
    WG "Just what exactly are we hoping to gain by winning?"
    show WG doubt
    show HR neutral at Position(xcenter=0.4, yalign=1.0) with dissolve
    HR "Good question, Nikumaru-san. Since the self-satisfaction of a job well done is a rather lack-luster reward, we decided to offer that the winning team will be taken off the class clean up rotation for the next month."
    show WG surprised-2
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
    "As athletic as Akira was, she couldn't contend that well with Naomi's reach as she tried to guard her."
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
    Naoki "Alright, the first half is done. Score is 1 to 1. {size=-6}Usually handball games have higher scores than this..."
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
    show HR neutral with dissolve
    #show Naoki neutral with dissolve
    #show Hageshit neutral with dissolve
    HR "{size=-4}...I think this is the worst any class has ever done.{/size}"
    Naoki "{size=-4}I can't think of any exceptions myself.{/size}"
    Hageshi "{size=-4}That may be so, but try not to say that too loudly.{/size}"
    "I may have been half blind, but I wasn't deaf to what the teachers were murmuring to themselves. {w}This was even worse than I thought."
    hide HR
    #hide Naoki with dissolve
    #hide Hageshi with dissolve
    show FMG sad-2 at Position(xcenter=0.10, yalign=1.0)
    show WG angry at Position(xcenter=0.28, yalign=1.0) behind FMG
    show PRG sad at Position(xcenter=0.45, yalign=1.0)
    show BE doubt at Position(xcenter=0.6, yalign=1.0) behind PRG
    show GTS sad at Position(xcenter=0.75, yalign=1.0)
    show AE sad-2 at Position(xcenter=0.9, yalign=1.0) behind GTS
    with dissolve
    "No one was used to their changing bodies. Everyone was feeling frustrated with themselves and everyone else."
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
    show HR neutral
    with dissolve
    #show Hageshi with dissolve
    #show Naoki with dissolve
    Hageshi "Adapt and overcome. I'm actually impressed with your effort, Hotsure-san."
    Naoki "That's the kind of determination we like to see."
    HR "I don't know if anyone likes to see that."
    MCT "I'm not going back to playing blind, at this point it's best if I just own it."
    hide HR
    #hide Hageshi with dissolve
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
    All "Awww!"
    Hageshi "No whining now. You should be proud of yourselves. I have to admit, it was quite impressive to see everyone turn things around."
    Naoki "Hageshi-san is right. This started off as one of the worst games I'd seen, only to turn into one of the better ones in the second half."
    HR "So in a way, you're all winners."
    show WG doubt at Position(xcenter=0.15, yalign=1.0) with dissolve
    WG "If no one won anything, it sounds like we're all losers."
    HR "That's one way of looking at it certainly, but I would suggest looking on the positive side of things. {w}Look, I don't say this often, but I'm proud of how you all were able to turn things around for yourself."
    show AE happy at Position(xcenter=0.9, yalign=1.0) with dissolve
    AE "Thank you, Tashi-sensei."
    HR "Don't mention it. {w}Like literally, {w}ever again."
    show FMG happy at Position(xcenter=0.3, yalign=1.0) behind HR with dissolve
    FMG "I think Tashi-sensei likes us!"
    show WG neutral
    show GTS happy-2 at Position(xcenter=0.75, yalign=1.0) with dissolve
    GTS "My sincerest gratitude, Tashi-sensei."
    show PRG unique-happy at Position(xcenter=0.6, yalign=1.0) behind HR with dissolve
    PRG "W-We like you too Tashi-sensei..."
    HR "{i}Ugggh{/i}.... please, no..."
    hide AE
    hide GTS
    hide WG
    hide FMG
    hide PRG
    with dissolve
    #show Naoki with dissolve
    #show Hageshi with dissolve
    Naoki "I knew this guy was a softy at heart."
    Hageshi "You're not the only one, Aoi-san seems to think so too."
    HR "Alright, we're done here. Class dismissed."
    hide HR with dissolve
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
    Naoki "Alright, Team 1 is Utagashi-san, Inoue-san, Yamazaki-san, and Matsumoto-san. Team 2 is, Hotsure-san, Nikumaru-san, Mitzutani-san, and Kodama-san."
    show WG doubt
    WG "Just what exactly are we hoping to gain by winning?"
    show WG doubt
    show HR neutral at Position(xcenter=0.4, yalign=1.0) with dissolve
    HR "Good question, Nikumaru-san. Since the self-satisfaction of a job well done is a rather lack-luster reward, we decided to offer that the winning team will be taken off the class clean up rotation for the next month."
    show WG surprised-2
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
    "But I was most worried about Aida. She was easily the smallest of all of us and she didn't look to have the athleticism to make up for it. I didn't want to see her get body checked from a defensive block."
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
    "Coach Naoki tossed the ball to Alice, who took a casual pace dribbling it up the court until she saw me rushing to defend against her."
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
    RM "Like you could have done any better guarding Yamazaki-san."
    show WG stern
    WG "I thought you were supposed to ‘carry this team'?"
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
    "As athletic as Akira was, she couldn't contend that well with Naomi's reach as she tried to guard her."
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
    Naoki "Alright, the first half is done. Score is 1 to 1. {size=-6}Usually handball games have higher scores than this..."
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
    show AE neutral
    AE "I agree with Inoue-san-san."
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
    show HR neutral with dissolve
    #show Naoki neutral with dissolve
    #show Hageshit neutral with dissolve
    HR "{size=-4}...I think this is the worst any class has ever done.{/size}"
    Naoki "{size=-4}I can't think of any exceptions myself.{/size}"
    Hageshi "{size=-4}That may be so, but try not to say that too loudly.{/size}"
    "I may have been half blind, but I wasn't deaf to what the teachers were murmuring to themselves. {w}This was even worse than I thought."
    hide HR
    #hide Naoki with dissolve
    #hide Hageshi with dissolve
    show FMG sad-2 at Position(xcenter=0.10, yalign=1.0)
    show WG angry at Position(xcenter=0.28, yalign=1.0) behind FMG
    show PRG sad at Position(xcenter=0.45, yalign=1.0)
    show BE doubt at Position(xcenter=0.6, yalign=1.0) behind PRG
    show GTS sad at Position(xcenter=0.75, yalign=1.0)
    show AE sad-2 at Position(xcenter=0.9, yalign=1.0) behind GTS
    with dissolve
    "No one was used to their changing bodies. Everyone was feeling frustrated with themselves and everyone else."
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
    show HR neutral
    with dissolve
    #show Hageshi with dissolve
    #show Naoki with dissolve
    Hageshi "Adapt and overcome. I'm actually impressed with your effort, Hotsure-san."
    Naoki "That's the kind of determination we like to see."
    HR "I don't know if anyone likes to see that."
    MCT "I'm not going back to playing blind, at this point it's best if I just own it."
    hide HR
    #hide Hageshi with dissolve
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
    MC "Kodama-san, don't be afraid of the ball. I know it can be fast, but it isn't very hard. Just put out your hands and it'll bounce right off of you, I promise."
    PRG "I-I think I can do that."
    MC "Trust me, you'll do fine. We all will."
    Naoki "Alright, Team 1 won the coin toss, so Team 2 gets the ball at the start of this half."
    hide FMG
    hide PRG
    hide WG
    with dissolve
    "Coach Naoki tossed the ball to me, which to everyone's surprise, (including myself) I caught with no problem. {w} I trotted up the field looking for an opening before I tossed it to Alice."
    show WG neutral with dissolve
    "Taking it and running with it, Alice ran up close to the goal zone, this time leaving adequate time to stop herself short before going over the line."
    show WG angry
    show GTS neutral-2 at Position(xcenter=0.75, yalign=1.0) with dissolve
    extend " Her effort to score though was thwarted when Naomi swatted the ball away before it could reach the goal."
    MC "Dangit, that was clever of them to switch out Yamazaki-san for Honoka for the goalie."
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
    "Coach Naoki served Honoka the ball. My plan was to toss it to block her to force a pass that Akira would intercept..."
    play sound Whistle
    hide AE
    hide BE
    pause 1
    Naoki "Times up. Final score 2 to 2. It's a tie."
    play music Peaceful
    show HR neutral at Position(xcenter=0.45, yalign=1.0) with dissolve
    HR "Looks like no one wins the prize then."
    All "Awww!"
    Hageshi "No whining now. You should be proud of yourselves. I have to admit, it was quite impressive to see everyone turn things around."
    Naoki "Hageshi-san is right. This started off as one of the worst games I'd seen, only to turn into one of the better ones in the second half."
    HR "So in a way, you're all winners."
    show WG doubt at Position(xcenter=0.15, yalign=1.0) with dissolve
    WG "If no one won anything, it sounds like we're all losers."
    HR "That's one way of looking at it certainly, but I would suggest looking on the positive side of things. {w}Look, I don't say this often, but I'm proud of how you all were able to turn things around for yourself."
    show AE happy at Position(xcenter=0.9, yalign=1.0) with dissolve
    AE "Thank you, Tashi-sensei."
    HR "Don't mention it. {w}Like literally, {w}ever again."
    show FMG happy at Position(xcenter=0.3, yalign=1.0) behind HR with dissolve
    FMG "I think Tashi-sensei likes us!"
    show WG neutral
    show GTS happy-2 at Position(xcenter=0.75, yalign=1.0) with dissolve
    GTS "My sincerest gratitude, Tashi-sensei."
    show PRG unique-happy at Position(xcenter=0.6, yalign=1.0) behind HR with dissolve
    PRG "W-We like you too Tashi-sensei..."
    HR "{i}Ugggh{/i}.... please, no..."
    hide AE
    hide GTS
    hide WG
    hide FMG
    hide PRG
    with dissolve
    #show Naoki with dissolve
    #show Hageshi with dissolve
    Naoki "I knew this guy was a softy at heart."
    Hageshi "You're not the only one, Aoi-san seems to think so too."
    HR "Alright, we're done here. Class dismissed."
    hide HR with dissolve
    "So it wasn't exactly the greatest game of handball ever played. It was pretty clear things were starting to change. {w}{i}We{/i} were starting to change."
    "I wasn't sure what the future held for all of us, but for now I was glad we all got to have a little fun."
    jump daymenu

label MC007:
    "This marks the current end of the Keisuke-centric scenes."
    "More are planned for a later release. Until then, feel free to explore the main routes."
    jump daymenu

label global005:
    $setTimeFlag("testday2")
    scene Dorm Interior with fade
    "When I woke up this morning, Daichi was nowhere to be found."
    "I thought it was unusual for him, usually the mornings were filled with the clicking of mice and keyboards as he did his 'research'. Still, it was a welcome break to not have him eyeing me as I brushed my teeth or whatever."

    scene Hallway with fade
    play music Busy
    "As I made my way inside the classroom building, I ran into a few of my classmates."
    if getHighestAffection() == "BE":
        show BE neutral with dissolve
        BE "Hey there, Kei-chan! How are things going for you?"
        MC "Oh, pretty good. You?"
        BE "Still getting used to how big this campus is! I've been spending some time walking around each night and I still haven't seen it all!"
        MC "Wow, I haven't been around much either..."
        BE "Maybe we can go exploring together sometime!"
    if getHighestAffection() == "WG":
        show WG neutral with dissolve
        WG "Hotsure-san."
        MC "Oh, hello Nikumaru-san."
        WG "Please, I've told you before, call me Alice. Formalities are for business, I find them so tiresome in normal conversation."
        MC "Er, okay, Alice... but you called me Hotsure-san."
        WG "Because you were expecting it, of course. In any case, I trust you are adjusting to your new setting. Settling into a new routine by now?"
        MC "As well as anyone I suppose..."
        show WG haughty
        WG "Good to hear. Some find adherence to a routine to be restrictive, but I find the gains in productivity from an optimized schedule to be far more freeing than leaving idle time for its own sake."
    if getHighestAffection() == "GTS":
        "I noticed Naomi-san walking next to me as we made our way to class. Like, noticeably close."
        show GTS neutral with dissolve
        GTS "..."
        MC "Hey there, Naomi-san."
        GTS "Oh, h-hello."
        MC "..."
        GTS "..."
        MC "Nice day we're having, yeah?"
        GTS "...Yes."
        MCT "Boy, she's not much for conversation today... but she seems happy."
    if getHighestAffection() == "FMG":
        show FMG neutral with dissolve
        FMG "Hotsure-san! How ya doin'?"
        "I cringed as Akira slapped me on the back in what she probably thought was a friendly manner."
        MC "Hrrrk!"
        FMG "Haha, catch you by surprise, did I? Well, hopefully that'll wake you up a bit!"
        MC "It's nice to see you too, Mizutani-san..."
        FMG "Guess what I found out yesterday? They've got an outdoor weight area behind the gym! Can't wait to try it out!"
        MC "Does that make a difference?"
        FMG "Sure! Morning and evening workouts can go harder than normal because you're being naturally cooled by the cold air!"
        MCT "I boggled to think what a 'harder' workout was for Akira, seeing how hard she already pushed herself..."
    if getHighestAffection() == "PRG":
        show PRG neutral with dissolve
        PRG "H-hi Kei-sama!"
        MC "Oh, hi Kodama-san."
        PRG "I... I'd like it if you'd call me Aida..."
        MC "Yeah?"
        PRG "Yeah. Like... a lot."
        MC "Okay, Aida. How are you today?"
        PRG "I'm fine. How are you? Did you sleep good? Get enough breakfast? I've got a snack if you're hungry..."
    if getHighestAffection() == "AE":
        show AE neutral with dissolve
        AE "Hotsure-san."
        MC "Oh, hello Matsumoto-san."
        AE "Good to see you on time. I may have need of your assistance later."
        MC "Oh?"
        AE "It's measuring day for our class. I might need help corralling the student bodies through the process in an efficient manner."
        MC "Er, all right, sure."
        AE "I wasn't asking."

    scene Classroom with fade
    "When we got to Room 3-B, we found a message written out on the blackboard, announcing that we were all supposed to head to the gymnasium."
    show AE neutral at Position (xcenter=0.8) with dissolve
    AE "All right, everyone, it's measuring day for our class, so let's get an orderly line going."
    show FMG happy at Position (xcenter=0.25) with dissolve
    FMG "Oooh, neat! I've been wanting to get my guns professionally measured for a while!"
    WG "..."
    hide FMG with dissolve
    AE "Kodama-san, you stay behind, we've got... five stragglers, it looks like."
    show PRG neutral at center
    show WG neutral at Position (xcenter=0.2)
    with dissolve
    WG "Excuse me, but Aida is otherwise engaged."
    show PRG neutral at Transform(xzoom=-1)
    AE "Not now she isn't, unless there's some other class president I'm unaware of."
    show PRG neutral at Transform(xzoom=1)
    WG "I'm sure you can find someone else. Aida is developing a set of very specialized skills."
    show PRG neutral at Transform(xzoom=-1)
    AE "I'm sure she is. AFTER classes. During school hours she'll submit to school authority."
    show PRG neutral at Transform(xzoom=1)
    show WG angry
    show AE angry
    WG "..."
    AE "..."
    show PRG neutral at Transform(xzoom=-1)
    pause 1
    show PRG neutral at Transform(xzoom=1)
    WG "..."
    AE "..."
    show PRG sad at Transform(xzoom=-1)
    pause .5
    show PRG sad at Transform(xzoom=1)
    pause .5
    show PRG sad at Transform(xzoom=-1)
    pause .5
    show PRG sad at Transform(xzoom=1)
    pause .5
    show PRG sad at Transform(xzoom=-1)
    pause .5
    show PRG sad at Transform(xzoom=1)
    pause 1
    show WG neutral
    WG "...Hmph!"
    MCT "...Those two aren't used to accepting 'no' for an answer, that's for sure..."

    scene Auditorium with fade
    play music Rain
    "The auditorium had been set up with what amounted to a field clinic, privacy dividers erected in a series of squares, with various testing and measuring devices set on folding tables."
    "I noticed that unlike at my previous schools, it seemed there were no student volunteers; every station seemed to be manned by a medical professional of some sort."
    AE "Class 3-B, over here! Line up along this partition, and no, not alphabetically, by seat number. What do you mean you don't know what your seat number is? Haven't you been paying attention at all?"
    "The lines were small, but given how thoroughly they were measuring everyone- I supposed being here meant there was a much wider set of variables that could be changing- each person took as long as several might at my older schools."
    "I didn't have much time to think about it, though- my name was one of the first few called up. I was directed first to a small cubicle in the corner, where I was to hear the specific results of my growth factor test."
    "I went into the little corner-cubicle, halting in my tracks as soon as the nurse turned to face me."
    Nurse "Hello, Hotsure-san, please have a seat."
    "I sat on the stool, my amazement at the size of her lips only slightly eclipsing my amazement that she could talk without a lisp."
    "They were so enormous and puffy I literally couldn't see her chin, the top curve of her upper lip nestled against the bottom of her nose."
    "What was more, she had decided to cover them in bright red lipstick. It was nearly impossible not to stare as she looked down at a clipboard full of papers."
    Nurse "So, your growth factor has been confirmed to be... Heh, you like them?"
    MCT "Oh crap, she caught me staring!"
    MC "No, I, uh, I mean, they're-"
    "Her lips actually managed to pull out into a smile, making nearly the entire bottom half of her face hidden behind them."
    Nurse "It's all right, I know they can be surprising. Whenever I go off-campus I have to wear a surgical mask or I can hardly do anything for all the gawking and questions."
    "I just nodded and looked away, wondering what I would have to do to live a normal life."
    Nurse "Anyways, your growth factor. According to these results, you have hyper-productive hair follicles."
    Nurse "Not hypertrichosis, so you don't need to worry about having to shave your nose and forehead and so on, but you'll definitely need a barber more often than most."
    MC "My hair? It's always grown like a weed, that's nothing new."
    Nurse "Heh heh... Well, the degree is never certain, but remember that it's not fully manifested yet. Whatever rate of growth you're used to, it will increase by some amount, guaranteed."
    MC "And... and my sister? Does she have the same thing? Does she have anything at all?"
    Nurse "I'm sorry, but since she's not a minor anymore I'm not allowed to share her medical information with anyone she hasn't specified..."
    "I mulled over this for a few seconds while she wrote on her clipboard."
    MC "So, that's it? Is it going to be all of my hair, er, everywhere?"
    Nurse "Body and head hair grow at different cycles and intensities, so it's hard to say. But we'll be sure to check up on all of your growth throughout the year, so please try and keep a record of each time you cut any of your hair."
    MC "...Do I have to?"
    Nurse "No, but we're only here to help. If you're comfortable only knowing what you know now about your condition, we won't force you. But you still have to come in for measurements and such."
    MC "So, can I go?"
    Nurse "Right after we take some blood, yes. Just sit still and roll up your sleeve..."

    scene Auditorium with fade
    "I walked out of the nurse's cubicle, rubbing the cotton ball taped to the crook of my elbow. Next was the height and weight measurements, then an eye test, then several other stations I didn't even know the purpose of."
    "All told, except for a few walled-off areas for privacy, all the tests happened in the same open area. I wondered if I would get to see/hear some of my classmates as I went through..."
    jump daymenu

label RM001:
    scene Dorm Interior with fade
    MCT "Another day of classes over..."
    "When I arrived back at my room, Daichi was already there, poking some device on his desk very intently with a soldering iron."
    "I couldn't really tell what it was, beyond some kind of circuit board."
    show RM neutral with dissolve
    RM "..."
    MCT "To be honest, I still haven't had a good chance to talk with him yet. Mostly because I don't really see much of him outside of class."
    MCT "I guess now is as good of a time as any to try and get to know him."
    play music RM
    MC "Hey, Daichi."
    RM "Yes?"
    menu:
        "What are you working on?":
            MC "What are you working on, exactly?"
            if getAffection("RM") < -2:
                jump RM001_fail
            else:
                jump RM001_c1_1
        "What do you like to do for fun?":
            jump RM001_after
        "Where do you go after class?":
            MC "So I can't help but notice you usually come home kind of late. Are you in a club, or something?"
            if getAffection("RM") < -2:
                jump RM001_fail
            else:
                jump RM001_c1_2

label RM001_c1_1:
    $setFlag("RM001_c1_1")
    "He answered me without turning around, opting instead to continue tinkering with the device."
    RM "A miniature video camera. I want to keep tabs on someone."
    MC "What, like a teacher? Is that a good idea?"
    "That last question got his attention. He put the soldering iron down and turned to me, eyes narrowed."
    RM "It's something I need to know. Whether it's a good idea or not is irrelevant."
    show RM angry
    RM "Unless you know someone in the class below us who'd be willing to spy for me, this is my best option."
    MC "Can't say that I do."
    MCT "I'm {i}not{/i} getting my sister involved with this guy."
    show RM neutral
    RM "Then I'm using the camera."
    "I didn't really have a good response to that. He took the opening to continue his work."
    MCT "Maybe I should try a lighter topic?"
    jump RM001_after

label RM001_c1_2:
    "He answered me without turning around, opting instead to continue tinkering with the device."
    RM "I'm busy investigating."
    MC "The school, you mean?"
    RM "Of course."
    "An awkward silence descended upon the room."
    MCT "Maybe I should try a lighter topic?"
    jump RM001_after

label RM001_fail:
    "He put down the soldering iron and glared over his shoulder at me."
    show RM angry
    RM "None of your business."
    if getFlag("RM_govagent"):
        MC "Are you still upset over the 'I'm a government agent' thing?"
        show RM neutral
        RM "Yes."
        MC "Look, I'm sorry. I didn't realize it was such a... sensitive subject."
    else:
        MC "Did I do something to offend you?"
        show RM neutral
        RM "You don't appreciate the situation we're in, for one."
        MC "I'm... sorry?"
    show RM smug
    RM "Apology accepted - I'll forgive your ignorance. If you're willing to take this seriously, I can enlighten you on a few things. Interested?"
    MCT "Is it too late to change roommates?"
    MC "Maybe another time."
    show RM neutral
    RM "Suit yourself."
    "An awkward silence descended as he went back to working on... Whatever it was."
    MCT "Maybe I should try a lighter topic?"
    jump RM001_after

label RM001_after:
    MC "Hey, what do you like to do for fun? Got any hobbies?"
    RM "Not really. Haven't had time lately. Been too busy trying to figure out what's going on here."
    MC "Well, what about before you came to the school? Or was it just more conspiracies?"
    "That comment caused him to finally stop working and turn around to face me."
    show RM angry
    RM "Please. I'm not some kind of conspiracy nut. It's just that this school is too weird."
    RM "The fact that more people aren't suspicious of this place is mind-boggling to me."
    MC "Fine, fine, whatever. What did you do before you came here?"
    show RM neutral
    RM "...I read manga, I guess?"
    MC "That's a start! What did you read?"
    RM "I liked Two Pieces. Is that still going?"
    MC "...It ended like three years ago."
    show RM sad
    RM "Oh."
    MC "You read anything else?"
    show RM neutral
    RM "Not really, unless you count studying."
    MC "..."
    RM "..."
    MC "Games? Movies? Music?"
    RM "I used to play Suncraft, a few years back. Haven't played in a while, though."
    MC "Oh. I've never heard of it."
    RM "It's a strategy game. I always thought it was pretty fun."
    MC "I see."
    show RM sad
    RM "..."
    MC "..."
    MC "Well, what about your project there? Do you like tinkering with stuff?"
    show RM neutral
    RM "It's alright, I guess."
    MC "What about when you graduate? You going to go into electrical engineering or something?"
    RM "Maybe? I haven't decided yet."
    RM "I've thought about becoming a teacher, too."
    MC "Why a teacher? You like learning?"
    RM "I want kids to get more critical thinking skills, so they won't just mindlessly obey authority."
    MC "Oh."
    RM "..."
    MC "..."
    MCT "This is going great."
    menu:
        "Can you show me what you're working on?":
            jump RM001_c2_1
        "Well, time to study!":
            jump RM001_c2_2

label RM001_c2_1:
    if getFlag("RM001_c1_1"):
        MC "Well, hey, why don't you show me what you're doing with your camera?"
    else:
        MC "Well, hey, why don't you show me your... Whatever it is."
        "He sighed and held up a lens, which was hiding behind some other components."
        RM "Camera. It's a camera."
        MC "Yeah, that."
    "He paused for a moment."
    if getAffection("RM") > -3:
        $setAffection("RM", 1)
        show RM happy
        "Eventually his expression relaxed a little."
        RM "Sure, why not? Pull up a chair."
        scene black with fade
        "We spent most of the evening working on his camera. He got a lot more talkative once he started talking about something he was more comfortable with."
        "He taught me quite a bit about how all the components work."
        MCT "I don't know if it's ever going to be useful, but it was pretty informative."
        $setSkill("Academics", 1)
        jump daymenu
    else:
        show RM angry
        "...But then turned back around in a huff."
        RM "I'm busy. I've wasted enough time answering your questions."
        MC "Fine."
        jump RM001_c2_2

label RM001_c2_2:
    MC "Well, I need to study. Have fun with your project."
    show RM neutral
    RM "Mmm."
    "We didn't say anything to each other for the rest of the night."
    "The quiet room helped me focus, though."
    $setSkill("Academics", 1)
    jump daymenu

label RM002:
    scene Hallway with fade
    "I followed the crowd out of the classroom as everyone shuffled toward the cafeteria."
    "Out of the corner of my eye, inside another classroom, I noticed..."
    show RM neutral at Position (xcenter=0.95) with dissolve
    play music RM
    pause 2
    show RM angry
    "He glared at me and made a beckoning motion."
    "Resigned, I walked over to him and hissed..."
    show RM neutral at center with move
    MC "What?"
    RM "I need your help with something."
    MC "Daichi, I'm hungry. Can it wait until after lunch?"
    RM "No. This is important. It'll be simple, though."
    RM "All I need you to do is keep watch. If anyone wants to come in here, let me know - just make noise or something, and stall them for a few seconds."
    jump RM002_choice

label RM002_choice:
    menu:
        "Sure.":
            jump RM002_c1_1
        "What are you doing, exactly?" if not getFlag("RM002_c1_2"):
            jump RM002_c1_2
        "This is a stupid idea.":
            jump RM002_c1_3

label RM002_c1_1:
    $setFlag("RM002_c1_1")
    MC "You're right, that does sound simple. Alright, go ahead."
    show RM happy
    $setAffection("RM", 1)
    RM "Thanks. I'll be quick."
    jump RM002_c1_after

label RM002_c1_2:
    $setFlag("RM002_c1_2")
    MC "What exactly are you doing in there?"
    "After scanning the hallway to make sure nobody was paying attention, he discreetly showed me a familiar circuit board from his bag."
    RM "I'm placing the camera I made earlier. It shouldn't take long."
    MCT "I figured it would be something like that."
    jump RM002_choice

label RM002_c1_3:
    MC "This is a stupid idea and you're going to get caught."
    show RM smug
    RM "Your resistance to progress has been noted. I won't get caught as long as you do your job."
    hide RM with dissolve
    "Before I could protest, he headed into the classroom."
    MC "Seriously..."
    jump RM002_c1_after

label RM002_c1_after:
    stop music
    scene black with fade
    pause 2
    scene Hallway with fade
    "A few minutes of inconspicuous door blocking later, and the inevitable happened."
    show Yuki neutral with dissolve
    play music Busy
    UNKNOWN "Hey there! Can I get through?"
    MCT "Oh, great."
    menu:
        "Let her in" if not getFlag("RM002_c1_1"):
            jump RM002_c2_1
        "Signal Daichi":
            jump RM002_c2_2
        "Make up a story":
            jump RM002_c2_3

label RM002_c2_1:
    "I never agreed to play lookout for him. To be honest, I wasn't even really sure why I was still there..."
    MC "Sure, go ahead."
    show Yuki happy
    UNKNOWN "Thanks!"
    RM "Wait! Wait wait wait!"
    show Yuki happy at Position (xcenter=0.25)
    show RM angry at Position (xcenter=0.75)
    with dissolve
    pause .5
    show RM happy
    $setAffection("RM", -1)
    "He gave me a brief glare before turning to the girl."
    RM "Yuki-chan! How's your day been?"
    show Yuki neutral
    Yuki "Daichi-kun?!"
    jump RM002_c2_after

label RM002_c2_2:
    "I leaned back against the door."
    MC "Why? What's wrong?"
    UNKNOWN "Oh, no big deal. I just left some books behind by accident."
    MC "Your books? Where are they? I can go find them for you, if you want."
    "While saying all this, I knocked on the door repeatedly. Judging by her lack of response, I don't think she noticed."
    UNKNOWN "Oh, no worries. I can get them myself."
    MC "What books, if you don't mind me asking?"
    show Yuki sad
    UNKNOWN "...Math? Why does it matter?"
    "Before I could think of another way to stall her, Daichi came out of the room."
    show Yuki neutral at Position (xcenter=0.25)
    show RM neutral at Position (xcenter=0.75)
    with dissolve
    RM "Yuki-chan! What a pleasant surprise."
    Yuki "Daichi-kun? What are you doing here?"
    jump RM002_c2_after

label RM002_c2_3:
    MC "I wouldn't go in there. They're... de-roaching."
    UNKNOWN "Roaches? In just the one classroom?"
    MC "...{w} Yes."
    show Yuki sad
    UNKNOWN "...Hmm."
    "Suddenly, the door opened."
    show Yuki sad at Position (xcenter=0.25) with dissolve
    show RM neutral at Position (xcenter=0.75) with dissolve
    RM "Yuki-chan?"
    Yuki "Daichi-kun? Are you... de-roaching?"
    "Daichi gave me a confused glance before turning back to this Yuki girl."
    RM "Yeah. Why, do you need something?"
    jump RM002_c2_after

label RM002_c2_after:
    MC "Wait, you two know each other?"
    RM "Oh. Right. Keisuke, this is my sister Yuki. Yuki-chan, this is my roommate Hotsure Keisuke."
    show Yuki happy
    Yuki "Nice to meet you! Daichi-kun's talked about you a lot."
    MC "Good things, I hope."
    RM "Haha... yeah."
    if getFlag("RM_govagent"):
        Yuki "Actually, he said you were a no good lying-"
        show RM happy
        RM "Nothing but good things to say about my pal Kei-kun."
        MCT "..."
    show RM neutral
    RM "Anyway, I found what I was looking for."
    if getFlag("RM002_c1_2"):
        MCT "'What I was looking for?' He said he was placing a camera... What's with the act?"
        MCT "But he'll probably get upset if I don't play along."
    MC "Oh, good. Alright, I'll see you back at the dorm, then."
    RM "Yeah, sure. Talk to you later, man."
    hide RM
    hide Yuki
    with dissolve
    stop music
    "I began to walk down the hallway, but after a couple of seconds Yuki ran up to me."
    show Yuki neutral with dissolve
    Yuki "Hey... Hotsure-senpai."
    MC "Huh? What's wrong?"
    Yuki "Do you think that there's something weird happening at this school?"
    MC "What do you mean?"
    Yuki "Like... Do you think the staff are doing something strange to us?"
    MCT "Oh, no. Has Daichi filled her head with his nonsense?"
    MCT "Should I play along?"
    menu:
        "There's a conspiracy":
            jump RM002_c3_1
        "No conspiracy":
            jump RM002_c3_2

label RM002_c3_1:
    $setFlag("RM_Yuki_conspiracy")
    MC "I think so, yeah."
    show Yuki sad
    Yuki "I see."
    "She sighed, pulled out a notepad from her skirt pocket, and began writing something down."
    Yuki "OK, thanks."
    hide Yuki with dissolve
    "She slowly walked back to Daichi."
    MC "...Wait, what?"
    MCT "What was that reaction about?"
    jump daymenu

label RM002_c3_2:
    MC "No. I don't know who told you that, but it's ridiculous."
    show Yuki happy
    Yuki "All right."
    Yuki "For a minute there I was worried you were like my brother."
    show Yuki neutral
    Yuki "Um... Please don't think too badly of him when he says stuff like that. I think he's just stressed out about what's going on."
    MC "I think we all are, at least a little bit. I'm not holding it against him."
    Yuki "Thanks. Don't be afraid to say no if he's making you do something weird. He might be mad for a little bit, but trust me - he gets over it fast."
    show Yuki happy
    Yuki "I'll see you around, ok?"
    hide Yuki with dissolve
    "She walked back to Daichi, with a slight spring in her step."
    jump daymenu
