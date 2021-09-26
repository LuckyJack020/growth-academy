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
    "The hard bench under me lightly hummed with the vibrations of the ferry. Two hours of sitting here twiddling my thumbs and scrolling through my phone had left me beyond bored."
    "I leaned against the side of the boat, looking out across the shimmering, tranquil sea as the salty air blew through my thick, brown hair."
    "Not finding anything interesting to look at aside from water and sunshine, I turned back and glanced at my sister beside me, her gaze buried deep in the glass of her phone."
    MC "Nervous at all?"
    $setTomoOutfit(OutfitEnum.CASUAL)
    show Tomoko distracted with dissolve
    Tomoko "Mm... nah."
    MC "Not even some new school jitters?"
    Tomoko "Nope."
    MCT "Don’t know what I expected. Even earthquakes couldn’t freak her out."
    "Overhead, one of the many loudspeakers dotted throughout the ferry whined."
    Announcer "Your attention, please. We will be docking in five minutes. If you aren’t already, please take your seats. Thank you."
    "A few of the other students that had been milling around came to sit back down."
    "I leaned my head against the glass beside me. Ahead, a large, lush, green island loomed over us."
    MC "Well, that’s welcoming."
    show Tomoko distracted
    Tomoko "Did you say something?"
    MC "You know, since we’re not going to know anyone else here, the least you could do is be a little more social."
    show Tomoko neutral
    Tomoko "For what? We’re only going to be here for a year. Odds are that we’ll never see most of these people again anyway."
    MC "A lot can happen in a year, Tomo."
    show Tomoko annoyed
    Tomoko "Yeah, yeah. I don’t need a full inspirational speech, Kei."
    show Tomoko neutral
    "I scoffed and looked back at the island."
    "A fairly decent sized cluster of buildings jutted out from the trees, which parted around them to form a homey looking town."
    "And, since that was all I could see from here, I figured that the school had to be nestled in with those buildings."
    MCT "Not like they’d just stick it out in the boonies."
    pause .5
    MCT "At least I hope not."
    "That is what this island felt like compared to home, though. Compared to Tokyo, this was a complete 180."
    "I looked over to my sister once more, and my mom’s words rang true in my head once again."
    MCT "Take care of your sister!"
    MCT "Yeah, will do, Mom."
    "I didn’t have a problem with looking out for her. She was my twin after all. But, it was hard to do that when I didn’t even know what to expect."
    MC "So, do you-"
    Announcer "Please remain seated until the ferry comes to a full stop, then make your way to the boarding dock, following the yellow lines on the floor. An attendant will be available should you need assistance!"
    "The voice over the PA system rang out through the deck, causing a few of the other students to look up from their phones while others readied their bags for departure."
    Announcer "Group one, please exit off of the left side of the ferry. An attendant will be ready to lead you to registration on arrival."
    Announcer "Group two, please exit off of the right. Groups three and four, please wait until we’re ready for you."
    hide Tomoko neutral with dissolve
    "Tomoko and I got up from our spots and shuffled in the crowd of students toward the center of the ferry."

    scene Dock with fade
    "Hiking up my bag, I waited in line for a few minutes before reaching a small booth at the end of the dock, where I was handed a small welcome gift bag by a female teacher who bore a bright nametag that read ‘Takamura’."
    show Tomoko neutral with dissolve
    Takamura "Can I get your name, please?"
    Tomoko "Tomoko Hotsure."
    Takamura "Right... okay! Group one, right over there. Just follow them to the academy."
    Tomoko "Alright. Later bro."
    MC "Yeah. See ya."
    hide Tomoko with dissolve
    Takamura "And, your name, please?"
    MC "Keisuke Hotsure."
    Takamura "Another Hotsure? Okay... one second...{w} Ah! There you are."
    "The teacher turned and glanced off at the group of students who were already almost out of sight."
    Takamura "Well, looks like they were a little eager to get a move on. Just follow this path here all the way down."
    MC "Alright. Thank you very much."
    "I took off at a brisk pace, and left the rest of the students behind as I tried to catch up with my group."
    scene black with fade
    pause 1

    scene Lake Road with fade
    #BIRD SFX
    pause .5
    MCT "Geez... it’s cooking out here."
    "I came to a stop on a wooden bridge overlooking a lake, taking the bottle of water from my gift bag and taking a sip."
    MCT "And, why haven’t I seen anyone else?"
    "I looked back behind me, down the winding path I’d been following."
    "I knew that I was well away from the town by now."
    MCT "Where is this place, anyhow?"
    "I let out a loud sigh, taking another large gulp of water."
    "After I’d graduated from my last school, I’d assumed that I’d be just doing what the rest of my friends were, and going on to bigger and better things. University and all that."
    "But nope. My sister and I had both gotten letters in the mail regarding our attendance here, and that had derailed almost anything else going on."
    "And, I couldn’t find any information about this place either. Seichou Academy."
    "Every online search I’d done had come up blank and barebones, giving me little more than a phone number and an email."
    "All this ambiguity didn’t help the cesspool of nerves grinding together in my stomach."
    "I was gonna be living away from home and on my own, with my sister, my cell phone, and my personal belongings as my only ties back."
    "My luggage seemed to only be getting heavier as the minutes passed, my heart pounding away with each step I took. I had talked a big game to my parents about how I was fine..."
    "But... I had no clue if that was true or not."
    "I shook my head and looked around. All I saw was trees, the path in front of me, and the lake."
    MCT "Where even am I?! I've been walking for half an hour, shouldn't I have gotten there already?!"
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
    MC "Yep, she’s here! She’s doing about the same as always. Finally got her to come out of her room."
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
    MC "Look, it’s not my fault that Tokyo has such confusing metro lines!"
    BE "True, true. I’ve got a map, though. Came with the gift bag."
    pause .5
    MC "... Seriously?"
    BE "Eh... yeah? Take a look."
    "I dug my hand back into the bag and felt around for anything that resembled the texture of paper."
    pause .5
    MC "Okay... I’ve recently learned that I have a map. So, we’re not lost."
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
    "But even then, I had no idea just how much my life was going to change."
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
    "We approached the small garden just as the student extracted themselves from the planter, dusting the dirt from her skirt."
    show GTS sad at Position(xpos=0.75, xanchor=0.5) with dissolve
    UNKNOWN "Oooh, darn..."
    show BE surprised at Position (xpos=0.25, xanchor=0.5) with dissolve
    BE "Are you okay?"
    UNKNOWN "Eeep!"
    "The pale-skinned girl turned to us, looking briefly terrified.\nShe was wearing a skirt and short-sleeved shirt."
    UNKNOWN "Yes, sorry. I just fell. The planters are just rather large."
    UNKNOWN "I can't reach the middle of the bed without crawling on the outer ones..."
    "She gestured behind her, and we could see inside the planter were several rows of vegetables, the tops of radishes and carrots and the like poking through the soil."
    "Aside from the divot where she fell, the center row of vegetables did indeed look less well-watered than the ones closest to the edge."
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
    UNKNOWN "{size=-6}I-I’m sorry.{/size}"
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
    PRG "... Y-You don’t have to. It’s okay..."
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
    MC "But, nothing. We’re helping."
    PRG "Oh! Uhm..."
    PRG "T-Thank you! T-Thank you very much!"
    jump global000_RM

label global000_RM:
    scene Hallway with fade
    stop music
    show BE neutral with dissolve
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
    scene Dorm Interior with fade
    show RM neutral
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
    scene Dorm Interior with fade
    show RM neutral
    jump global000_RM_after

label global000_RM_c3:
    MC "Don't worry, sir. I'm from the government, just making an inspection!"
    hide cg with dissolve
    "I thought my fake-authoritative voice would have been at least worth a laugh, but the door slammed shut in my face."
    "I knocked again with more force, but only received silence in return."
    "I put my ear against the door, though all I heard was movement followed by the occasional slamming sound."
    "Sighing, I reached into my pocket and dug through random pocket junk until I felt the cold, blunt edge of my key."
    "Producing it, I shoved it into the lock and turned it."
    scene Dorm Interior with fade
    "Rather than being shoved out of the room and cussed straight off of campus, I opened the door to find the door slammer hurling an enormous suitcase straight over the balcony. Beside him were two more large bags, primed and ready for tossing."
    MC "Whoa, whoa! Can we just talk for a sec? I’m not with the-"
    RM "That’s what you want me to think! I’m not for it! Daichi Utagashi will not go down without a fight!"
    "He leaned down and clutched two more bags, a mess of papers and cloth sticking through one of the zippers."
    "Daichi leaned over to throw one, and in a panic...{w} slipped and threw himself straight over the edge, somehow managing to catch the rail in one flailing hand."
    #show new RM cg here
    RM "Gah! Rgh, dammit!"
    "I heard the sound of the bag hitting the ground, but all I saw was his knuckles ratcheted onto the railing."
    MC "Calm down for a second! I promise I’m not with the government!"
    RM "D-Don’t even start!"
    MC "Okay, if I really was out to get you, would I have just revealed myself in plain conversation like that?"
    pause .5
    RM "You do have a point there."
    pause .25
    RM "Okay, help me get back over! But don’t you dare try {i}anything{/i}!"
    "I dropped my bags at my feet and hurried over, grabbing his wrist firmly with one hand and his shoulder with the other."
    MC "Ngh..."
    pause .5
    show dummy with vpunch
    MC "Ragh!"
    "I pulled with all my might, and yanked Daichi up enough where he could get his footing."
    "He threw himself back over the railing and landed in a heap on the floor, breathing like an olympic athlete."
    #hide cg with dissolve

    scene Dorm Interior with fade
    show RM angry with dissolve
    RM "Bah... hagh... eh..."
    MC "You’re... hah... you’re welcome."
    show RM distrustful
    RM "Alright... let’s... see some ID."
    MC "... Seriously? I save you from falling and {i}that’s{/i} your opening line?"
    show RM doubt
    RM "Card. Now."
    "I huffed and yanked my wallet out of my back pocket, pulling out my ID."
    pause .25
    RM "Hmph..."
    pause .5
    show RM distrustful
    RM "Don't get any funny ideas, 'Keisuke Hotsure.’ I've got my eye on you..."
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
    MC "Yeah..."
    RM "Hmph. Just as I thought."
    MCT "???"
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
    stop music
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
    MCT "It’s way too quiet here. No cars honking. No people shoving past you. Nothing like the city at all."
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
    MC "Right, well. I’ll see you around, Tomo."
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
    MCT "Shiori-san's butt is overflowing her seat and pushing against me...{w} I can't say anything about it with everyone else around..."
    MCT "I'll just quietly scoot away from her-"
    "{color=#FF69B4}*PLOMF!*{/color}"
    MCT "Oh no!"
    show WG neutral at Position(xpos=0.25, xanchor=0.5) with dissolve
    MCT "Alice-San! She's taking up all of her seat and half of mine! What do I do??"
    MCT "I'm in the middle of a womanly butt-sandwich and it's like I'm the only one to notice! I've got to distract myself before something even more embarrassing happens!" #with Shake((0, 0, 0, 0), 0.75, dist=20)
    menu:
        "So, Shiori-san...":
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
    BE "Oh, hey there Naomi-san! Yeah, when we were kids we went to the same school. Different middle schools, though."
    menu:
        "Find your dorm okay, Honoka?":
            jump global000_sit_c2_1
        "What was your grade school like, Naomi?":
            jump global000_sit_c2_2

label global000_sit_c3:
    "I decided to sit in the back, where I wouldn't have to worry about anyone seeing me."
    show FMG neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    "The back rows were sparsely filled, so much so that I saw Mizutani-san could afford to hang her toned arms off of the backs of the chairs on either side of her."
    "The rest of the row was nearly empty, save for a small girl in the corner who I recognized from the night before as Aida."
    show PRG neutral at Position(xpos=0.25, xanchor=0.5) with dissolve
    "I also noticed she was looking at me, but as soon as our eyes met she turned away...{w} before slowly turning back to watch me from the corner of her eye."
    menu:
        "Needed the room to stretch out, Mizutani?":
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
    MCT "Uh, that’s not what I was getting at, but on second thought..."
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
    MC "What was your grade school like, Naomi?"
    show GTS neutral
    GTS "Mine?"
    MC "Sure, you heard about ours..."
    show BE neutral
    BE "Yeah, what was yours like, Naomi-san?"
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
    MC "Needed the room to stretch out, Mizutani?"
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
    PRG "B-But, there’s three of us here now."
    MC "Heh. Yeah, you’re right."
    MC "Would you mind if I sat by you?"
    show PRG surprised
    PRG "Uh... n-not at all!"
    MCT "Geez. It’s like she’s never spoken before."
    pause .25
    MC "So... nervous about starting at a new school?"
    PRG "A little...{w} yeah."
    MC "I can relate to that. It is definitely different."
    PRG "Yeah..."
    pause 1
    "Aida went quiet."
    MCT "Well... guess that’s all."
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
    Principal "The future is forever uncertain. But no matter what the future holds, years hence or any day now, one thing is important above all else."
    Principal "'Nosce te Ipsum.' {w}Latin, 'To thine own self be true'. Remember that you are more than your station, {w}skills, {w}and especially appearance. If you need help, your teachers are always available to help you with whatever you need."
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
    "Eventually we all took our seats, looking around at the sparse classroom. All the usual educational aids seemed to be on shelves or set into the wall, making the room seem even more like an empty box than it already was."
    "If not for the teacher's lectern at the front of the class, you'd be forgiven for thinking we were in a pen instead of a classroom."
    "Finally the bell rang, and at the last possible second one could enter and not be late, our homeroom teacher slid open the door and entered."
    #show HR unique with dissolve REMOVE WHEN UNIQUE SPRITE IS READY
    MCT "'Dour' is the first word that comes to mind... Guy looks like he's been middle-aged his entire life."
    "The man was tall, thin but not fit, wearing a collared shirt and dress slacks, with a jacket draped over one arm until he casually tossed it on the lectern. He swiped a piece of chalk up off the board and quickly scratched out his name on it."
    "{i}Tashi{/i}"
    "Tashi-sensei dropped the chalk back on the tray, turned to us, and stepped forward, leaning against the lectern."
    stop music
    HR "..."
    #hide HR with dissolve
    show GTS neutral with dissolve
    GTS "..."
    hide GTS with dissolve
    HR "..."
    show RM neutral with dissolve
    RM "..."
    hide RM with dissolve
    HR "..."
    MC "..."
    show HR neutral with dissolve #remove with dissolve when unique sprite is ready
    "Without a word, Tashi-sensei opened his mouth, and the classroom gasped as a four foot long tongue flopped out, unfurling down past Sensei's belt."
    hide HR
    show AE surprised
    AE "Gch-!"
    hide AE
    show BE surprised with vpunch
    BE "Oh, ick!"
    hide BE
    show WG angry with vpunch
    WG "Keep that thing away from me!"
    hide WG with dissolve
    show HR neutral
    "..."
    "..."
    play music Busy
    HR "All right, go ahead, get it out now. But don't run away or you'll be marked tardy."
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
    "Tashi-sensei scanned the room, taking in the fear and confusion, then shrugged."
    HR "Anyways, that's my big first day speech. Don't expect more.{w} So, roll call. Matsumoto-San?"

    scene black with dissolve
    stop music

    "So I found myself at Seichou Academy, orientation behind me and a long, strange journey ahead."
    "What was I supposed to do now, knowing what I do about the bodies of the student body?"
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
        WG "Because you were expecting it, of course. In any case, I'm looking forward to today's lessons. You?"
        MC "I suppose..."
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
