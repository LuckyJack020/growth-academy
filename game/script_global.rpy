image white = Solid((255, 255, 255, 255))
image black = Solid((0, 0, 0, 255))
#TBI: re-add condition switches
image Lake Road = "Graphics/ui/bg/lakeroad.png"
image School Front = "Graphics/ui/bg/schoolfront.png"
image School Inner = "Graphics/ui/bg/schoolinner.png"
image Gate Front = "Graphics/ui/bg/gatefront.png"
image School Planter = "Graphics/ui/bg/schoolplanter.png"
image Hallway = "Graphics/ui/bg/hallway.png"
image Classroom = "Graphics/ui/bg/classroom_day.png"
image Dorm Exterior = "Graphics/ui/bg/dormexterior.png"
image Dorm Interior = "Graphics/ui/bg/dorminterior.png"
image Campus Center = "Graphics/ui/bg/campuscenter_day.png"
image Auditorium = "Graphics/ui/bg/auditorium.png"
image School Exterior = "Graphics/ui/bg/schoolexterior.png"
image F1 Hallway = "Graphics/ui/bg/schoolhallway1.png"
image Library = "Graphics/ui/bg/library.png"
image Office = "Graphics/ui/bg/office_day.png"
image Cafeteria = "Graphics/ui/bg/cafeteria.png"
image Cooking Classroom = "Graphics/ui/bg/cooking.png"
image Music Classroom = "Graphics/ui/bg/music_day.png"
image Gym = "Graphics/ui/bg/auditorium.png"
image Track = "Graphics/ui/bg/track_day.png"
image Roof = "Graphics/ui/bg/roof_day.png"
image Nurse Office = "Graphics/ui/bg/office_day.png"
image Pool = "Graphics/ui/bg/schoolpool_day.png"
image Festival = "Graphics/ui/bg/festival.png"
image Bathroom = "Graphics/ui/bg/bathroom.png"
image Recreation = "Graphics/ui/bg/NYI.png"
image Town = "Graphics/ui/bg/town.png"
image Arcade = "Graphics/ui/bg/arcade.png"
image Cafe = "Graphics/ui/bg/cafe.png"
image Woods = "Graphics/ui/bg/NYI.png"
image Restaurant = "Graphics/ui/bg/restaurant.png"
image Hill Road = "Graphics/ui/bg/hillroad.png"
image Theater = "Graphics/ui/bg/NYI.png"

image splash = "Graphics/ui/bg/splashscreen.png"
image daymenubg = "Graphics/ui/bg/menubg-day.png"

image RM neutral = "Graphics/minor/RM-neutral.png"
image RM angry = "Graphics/minor/RM-angry.png"
image RM happy = "Graphics/minor/RM-happy.png"
image RM sad = "Graphics/minor/RM-sad.png"
image RM smug = "Graphics/minor/RM-smug.png"

image Yuki neutral = "Graphics/minor/yuki-1-neutral.png"
image Yuki happy = "Graphics/minor/yuki-1-happy.png"
image Yuki sad = "Graphics/minor/yuki-1-sad.png"
image Yuki gossip = "Graphics/minor/yuki-1-neutral.png"

image HR neutral = "Graphics/minor/HR-neutral.png" #Homeroom Teacher Neutral Portrait

define MC = Character('Keisuke', color="#0066CC") # Main Character, speaking.
define MCT = Character('Keisuke', color="#0066CC", what_prefix='(', what_suffix=')')
define RM = Character('Daichi', color="#BDB8A5")
define HR = Character('Tashi-Sensei', color="#C0C0C0")
define Yuki = Character('Yuki', color="#FF91DC")
define TS = Character('Tsubasa-sensei', color="#C0C0C0")
define Nurse = Character('Nurse', color="#FF91DC")
define UNKNOWN = Character('???', color="#FFFFFF")
define Student = Character('Student', color="#FF3300")
define Student1 = Character('Student 1', color="#FF3300")
define Student2 = Character('Student 2', color="#FF3300")
define Student3 = Character('Student 3', color="#FF3300")
define Cell = Character('Cell', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Computer = Character('Computer', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')

define audio.Daymenu = "Audio/BGM/menu_daymenu.ogg"
define audio.AE = "Audio/BGM/scene_AE.ogg"
define audio.BE = "Audio/BGM/scene_BE.mp3"
define audio.BBW = "Audio/BGM/scene_BBW.mp3"
define audio.FMG = "Audio/BGM/scene_FMG.mp3"
define audio.GTS = "Audio/BGM/scene_GTS.mp3"
define audio.RM = "Audio/BGM/scene_RM.ogg"
define audio.PRG = "Audio/BGM/scene_tbi.ogg" #NEED
define audio.Bittersweet = "Audio/BGM/scene_bittersweet.mp3"
define audio.Busy = "Audio/BGM/scene_busy.mp3"
define audio.Festival = "Audio/BGM/scene_festival.mp3"
define audio.Rain = "Audio/BGM/scene_rain.mp3"
define audio.Romance = "Audio/BGM/scene_tbi.ogg" #NEED
define audio.Peaceful = "Audio/BGM/scene_peaceful.mp3"
define audio.Schoolday = "Audio/BGM/scene_schoolday.mp3"
define audio.Steamy = "Audio/BGM/scene_tbi.ogg" #NEED
define audio.Sunset = "Audio/BGM/scene_sunset.mp3"
define audio.Tension = "Audio/BGM/scene_tbi.ogg" #NEED

define audio.EventStart = "Audio/SFX/sfx_eventstart.ogg"
define audio.AlarmClock = "Audio/SFX/sfx_alarmclock.ogg"
define audio.Bird = "Audio/SFX/sfx_tbi.ogg" #NEED (current one too long)
define audio.Cheer = "Audio/SFX/sfx_cheer.mp3"
define audio.ClockTower = "Audio/SFX/sfx_clocktower.mp3"
define audio.Crash = "Audio/SFX/sfx_thud.wav" #NEED UPDATE
define audio.Boing = "Audio/SFX/sfx_boing.ogg"
define audio.Knock = "Audio/SFX/sfx_knock.mp3"
define audio.Stomach = "Audio/SFX/sfx_tbi.ogg"
define audio.Thud = "Audio/SFX/sfx_thud.wav"
define audio.Thunder = "Audio/SFX/sfx_thunder.wav"
define audio.Victory = "Audio/SFX/sfx_victory.ogg"
define audio.Whistle = "Audio/SFX/sfx_whistle.mp3"

init 1 python:
    eventlibrary['global005'] = {"name": "And the Results Are In", "girls": [], "type": EventTypeEnum.OPTIONAL,            "location": "auditorium",    "priority": PrioEnum.ALL, "next": "", "obsflags": [],           "conditions": [[ConditionEnum.TIMEFLAG, "testday"]]}
    eventlibrary['RM001'] = {"name": "Getting to Know Your Roommate", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,  "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": []}
    eventlibrary['RM002'] = {"name": "Yuki", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                           "location": "hallway",       "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": [[ConditionEnum.EVENT, "RM001"]]}
    
    #Causes minor character scenes to be disabled if thime is between the first and second time in a tuple
    #(In other words, if XOR any two scenes in a tuple, then disable optional events with minor characters)
    minorDisableTimes = [("testday2", "aftertest"), ("size2", "aftersize2")]
    #Japanese holidays:
    #January 1: New Year’s Day
    #2nd Monday of January: Coming of Age Day (9th for year 2)
    #February 11: National Foundation Day
    #March 21: Spring Equinox Day
    #Spring Vacation: March 25 - April 5
    #April 29: Showa Day
    #May 3: Constitution Day
    #May 4: Greenery Day
    #May 5: Children’s Day
    #3rd Monday of July: Marine Day (18th)
    #Summer Vacation: July 20 - August 31
    #August 13-August 15: Obon
    #3rd Monday of September: Respect for the Aged Day (19th)
    #September 23: Autumn Equinox Day
    #2nd Monday of October: Health and Sports Day (Sports Festival) (10th)
    #November 3: Culture Day (Beginning/End of Culture Festival)
    #November 23: Labor Thanksgiving Day
    #December 23: Emperor’s Birthday
    #Winter Vacation: December 26 - January 6 (Christmas is usually off too)
    
label global000:
    stop music
    
    # Without a defined character code before the dialogue, it's unattributed speech. Good for narration.
    #EX - "This is the narrator, introducing our characters."
    
    # This is what text will look like with those codes attached.
    # Line breaks are done by inserting the command \n where you want to start a new line. No spaces allowed. 
    #Italics, bold, etc are done with curly brackets
    #
    
    #EX - MC "Yo. I'm the player character, Hotsure Keisuke.\nI'm transferring to Seichou Academy this year."
    #EX - BE "I'm the BE character, Inoue Honoka!\nIt's good to see you again, Kei{i}-chan{/i}!" 

    # I'll stick new characters above so that anyone that wants to just copy those lines and replace the actual dialogue can do so without worry.
    show black
    centered "The following represents a work in progress."
    centered "Art assets are placeholders or otherwise unfinished and all general content has yet to be finalized."
    centered "This is a work of fiction. Any resemblance to actual events or locales or persons, living or dead, is entirely coincidental."
    centered "For more information, visit\n https://discord.gg/Hs6ggpp"
    centered "Enjoy."
    if debugenabled:
        menu:
            "(DEBUG) Skip intro":
                jump daymenu
            "Continue":
                "Playing intro."
        
    # Move to Lake Road screen with a fade in transition.
    scene Lake Road with fade
    MCT "Ahh... It's really hot today."
    "I came to a stop on a wooden bridge overlooking a lake."
    "My name is Hotsure Keisuke. My spring vacation is coming to an end,\nand I'm starting at a new school tommorrow."
    MCT "To be honest, I'm a little nervous."
    "It's supposed to be a boarding school, which is why I've got my luggage with me."
    "But..."
    MC "Where the heck am I?!\nI've been walking for an hour already!"
    "I was sure that I was lost, but as I was thinking that, I saw someone walking ahead of me."
    MCT "I guess I'd better ask for directions."
    MC "Good afternoon!"
    "At the sound of my voice, she turned around and faced me."
    show BE neutral with dissolve
    play music BE
    "It turned out to be a fairly cute girl, with brown hair."
    MC "Sorry, but can you tell me where I am? I'm a little lost."
    UNKNOWN "..."
    "She stared at me intently for a long time. Did I surprise her or something?"
    MC "See, I'm trying to find Seichou Academy."
    UNKNOWN "Seichou..."
    "Because of that, the girl seemed to realize something."
    show BE surprised
    BE "Kei{i}-chan{/i}? Hey, you're Kei{i}-chan{/i}, right?!"
    MC "Wait, How do you know my name?"
    BE "What are you talking about? It's me! Honoka!"
    MC "Eh?!"
    "Come to think of it...I guess she is a little familiar."
    "I didn't recognize her at first because it's been so long, but this girl is Inoue Honoka."
    "We used to live in the same town a long time ago, and played together all the time."
    "But then her father got transferred, and she moved away..."
    BE "I can't believe you really don't remember me!"
    MC "Ahahaha...Sorry! It's been seven years already!"
    show BE neutral
    BE "That's true, it has been that long already, hasn't it..."
    BE "...I guess I have to forgive you then. You've grown up so much, so it's unreasonable to expect you to remember me if I've changed just as much."
    MCT "Exactly! There are limits to a guy's memory, you know? Besides..."
    play sound Boing
    show cg BE001 with vpunch
    MCT "I'm pretty sure I would have remembered those!"
    hide cg with dissolve
    show BE neutral with dissolve
    BE "Kei{i}-chan{/i}?  You kind of spaced out there for a second."
    MC "Er...I was just thinking, have I really changed that much?"
    show BE neutral
    BE "Well, your hair is the same, but I remember when I used to be taller than you."
    show BE happy
    extend " What about me, I've changed, right?"
    MC "...Maybe a little."
    MC "So, what are you doing out here?"
    show BE neutral
    BE "I thought that it was a nice day, so I should go for a little walk. I didn't imagine I'd run into you, Kei{i}-chan{/i}!"
    show BE surprised
    BE "Ah! You said you were looking for Seichou Academy, right?"
    BE "Could it be that you're attending there?"
    show BE happy
    extend " That's going to be my school starting tomorrow!"
    show BE neutral
    "...Now that I think about it, it looks like she's wearing a school uniform. I guess this means I might even be in the same class as Honoka."
    BE "Come on, Kei{i}-chan{/i}!\nI'll show you the way there."
    "So with that, I picked up my luggage and followed Honoka."
    show cg BE002 with dissolve
    BE "So, how have you been?\nHow about Tomo{i}-chan{/i}, her too!"
    "Tomo{i}-chan{/i} is Hotsure Tomoko, my younger sister."
    MC "She's doing fine. So am I."
    MC "Actually, she and I will be attending this school together, but she wasn't finished packing yet so she's not arriving today."
    MC "But anyway, I was really surprised, Honoka."
    BE "Yeah, I was a little nervous too, moving to a new boarding school and all."
    BE "But if you're going to be here, I'm sure it'll be great!"
    BE "I guess we'll both be in your care, Kei{i}-chan{/i}, so do your best!"
    MC "Right."
    BE "Ah! We're here!"
    scene School Front with fade
    stop music
    "Before I realized it, we had arrived at a huge school building. This was Seichou Academy."
    "This would be my new home for the next year.\nIt was really awe-inspiring at the time."
    "But even then, I had no idea just how much my life was going to change."
    jump global000_GTS

label global000_GTS:
    scene black with dissolve
    play music GTS
    "As we entered the school grounds, I couldn't help but notice how big everything was."
    scene School Planter with dissolve
    "What looked to be normal-sized buildings turned out to be a trick of perspective."
    "As Honoka and I walked and walked, the school seemed to grow before my eyes."
    "The doors became large and imposing, the floors far taller than normal, everything just seemed to be super-sized in Seichou Academy."
    UNKNOWN "Aaack!"
    "Honoka and I looked down to see a pair of legs flailing over the edge of one of the planters lining the building."
    "We approached the small garden just as the student extracted themselves from the planter, dusting the dirt from her skirt."
    show GTS sad at Position(xpos=0.75, xanchor=0.5) with dissolve
    UNKNOWN "Oooh, darn it darn it darn it..."
    show BE surprised at Position (xpos=0.25, xanchor=0.5) with dissolve
    BE "Are you okay?"
    UNKNOWN "Eeep!"
    "The pale-skinned girl turned to us, looking briefly terrified.\nShe was wearing a skirt and short-sleeved shirt."
    UNKNOWN "Uhm, yeah, sorry, I just, uhm, fell. Just, these planters are so big." 
    UNKNOWN "I can't reach the middle of the bed without crawling on the outer ones..."
    "She gestured behind her, and we could see inside the planter were several rows of vegetables, the tops of radishes and carrots and the like poking through the soil."
    "Aside from the divot where she fell, the center row of vegetables did indeed look less well-watered than the ones closest to the edge."
    menu:
        "That's too bad.":
            jump global000_GTS_c1
        "Do you need help?":
            jump global000_GTS_c2
            
label global000_GTS_c1:
    MC "That's too bad, hope you can figure something out."
    UNKNOWN "Yeah...If only I was a little taller, I could reach to the middle..."
    GTS "Oh, I'm sorry, I forgot entirely! My name's Yamazaki Naomi."
    "She bowed, and we returned the gesture."
    show BE neutral at Position (xpos=0.25, xanchor=0.5)
    BE "I'm Inoue Honoka, nice to meet you. This is Kei-{i}Ahem{/i}-Hotsure Keisuke."
    MC "Nice to meet you."
    GTS "Well, I've done as much as I can today, it seems. I'll leave the rest to the groundskeepers."
    GTS "I'll see you all at orientation tomorrow."
    show BE happy at Position (xpos=0.25, xanchor=0.5)
    BE "Goodbye! See you around!"
    hide GTS with dissolve
    BE "..."
    show BE neutral
    BE "...Boy, that's kind of a fancy lady to be kneeling in the dirt, don't you think?"
    "I nod, and we continue on to the front doors of the school."
    jump global000_AE

label global000_GTS_c2:
    MC "Do you need help?"
    show GTS happy
    UNKNOWN "Oh, thank you, that'd be lovely. Here, let me give you the can..."
    $ setAffection("GTS", 1)
    "I leaned way over the planter and watered the middle row of plants, having to stretch as far as I could reach but managing to get all of them."
    GTS "Thank you so much! Oh, I'm sorry, I didn't even introduce myself properly. My name's Yamazaki Naomi."
    "She bowed, and we returned the gesture."
    show BE neutral at Position (xpos=0.25, xanchor=0.5)
    MC "I'm Hotsure Keisuke, and this bundle of smiles here is Inoue Honoka. Nice to meet you."
    show BE happy
    BE "Hi there!"
    GTS "Well, it's been a pleasure."
    GTS "Perhaps I'll see you around school?"
    MC "Yeah, sure."
    BE "Yeah! See you later!"
    hide GTS with dissolve
    BE "..."
    show BE neutral
    BE "Well that was nice of you to help her, Kei-chan!"
    $ setAffection("BE", 1)
    "I nod, and we continue on to the front doors of the school."
    jump global000_AE

label global000_AE:
    scene black with dissolve
    UNKNOWN "Mizutani!"
    "The yell made both of us jump in place, so sudden and forceful was it so soon after stepping inside."
    "When we caught our bearings{w} (And Honoka's bust stopped jiggling){w} \nwe saw the owner of the voice."
    scene Gate Front with dissolve
    play music FMG
    "Stern and impatient-looking, the woman surveyed the front area of the school like a forewoman on a construction site, barking orders and taking notes on a clipboard."
    show AE angry at Position(xpos=0.75, xanchor=0.5) with vpunch
    UNKNOWN "Mizutani! Quit goofing off and get over here!"
    FMG "I'm comin', I'm comin'! Geeze!"
    "Around the corner came a tanned girl somehow managing to carry a wooden bench under each arm, her short-sleeved shirt baring her defined muscles for all to see."
    show FMG neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    UNKNOWN "What took you so long?"
    FMG "I was getting two benches at once!  I thought you'd like me getting twice what ya asked!"
    UNKNOWN "Not if it takes you three times as long!"
    hide AE
    hide FMG
    show BE surprised at center
    BE "Oh boy...I feel awkward just standing here..."
    hide BE
    show AE angry at Position(xpos=0.75, xanchor=0.5)
    show FMG neutral at Position (xpos=0.25, xanchor=0.5)
    menu:
        "She was just trying to help...":
            jump global000_AE_c1
        "You should listen to your boss, you know.":
            jump global000_AE_c2
        "(Do nothing)":
            jump global000_AE_c3

label global000_AE_c1:
    MC "She was just trying to help...{w} No need to be mean."
    $ setAffection("BE", 1)
    $ setAffection("FMG", 1)
    $ setAffection("AE", -1)
    UNKNOWN "Ex{i}cuse{/i} me?"
    FMG "Yeah, Matsumoto, get that stick out of your huge butt."
    "Matsumoto's face tightened and she shot daggers with her eyes."
    "It was hard not to notice the very prominent backside on her otherwise stiff and lithe frame."
    AE "My reasons for being at Seichou are not relevant to this conversation."
    hide AE
    show AE neutral at Position(xpos=0.75, xanchor=0.5)
    AE "As class rep it's my responsibility to make sure-"
    hide AE
    hide FMG
    show BE surprised at center
    BE "You're class rep already? But I thought classes didn't start until tomorrow."
    show BE surprised at Position (xpos=0.25, xanchor=0.5)
    show AE happy at Position(xpos=0.75, xanchor=0.5)
    AE "Well, not yet, technically, but I'm sure I will be. I always am."
    BE "(She's awfully self-assured...)"
    show AE neutral at Position(xpos=0.75, xanchor=0.5)
    AE "Are you two assigned to class 3-B? Inoue and Hotsure?"
    MC "Uh, I don't know, actually..."
    AE "I do. You're on the roster. I was just being polite."
    MC "Oh, well, okay then. Yeah, I guess?"
    AE "Get up there and make sure Aida and Nikumaru have the first-day decorations put up properly."
    show AE angry at Position(xpos=0.75, xanchor=0.5)
    AE "{i}Sigh{/i} Even though I'll probably have to fix it myself."
    MC "Er, okay, sure."
    hide AE with dissolve
    show BE surprised at Position (xpos=0.25, xanchor=0.5)
    "Without another word, Matsumoto turned and began barking more orders and directions to the other students arranging the decorations."
    "Honoka and I looked at each other and headed for class 3-B."
    jump global000_BBW
    
label global000_AE_c2:
    MC "You should listen to your boss, you know."
    MC "If she's got a plan, going off on your own doesn't really help."
    $ setAffection("FMG", -1)
    show FMG angry
    FMG "My WHAT? Matsumoto's not the boss of anyone, despite what she'll tell you."
    show AE neutral
    AE "I never claimed to be anyone's \"boss\", I just had a plan to-"
    FMG "Yeah, yeah, yeah. Listen, you two in 3-B? Might as well get up there and help."
    FMG "Whatever the princess and her pet're doing can't be as bad as having lard-butt boss you around..."
    hide FMG with dissolve
    "Matsumoto shot daggers at Mizutani as she left to get more benches, then turned to regard me with a glare."
    show AE sad
    AE "I did not need your help, but she's right. Get up to 3-B and help with the decorations and cleaning."
    "Honoka and I quickly fled the scene before the temperature dropped so low as to be freezing."
    jump global000_BBW
    
label global000_AE_c3:
    "I didn't want to get involved in the fight. {w}Especially after seeing Mizutani lift one of those big wooden benches under each arm."
    UNKNOWN "Look, it doesn't matter if you bring all the benches at once if I can't get them organized properly."
    UNKNOWN "One at a time lets us get each one in its place and ready for the next without-"
    show FMG sad
    FMG "All right, all right, I get it, sheesh. Don't get your panties in a bunch, Matsumoto..."
    show FMG happy
    extend "with a butt that size, you'll never fish 'em back out."
    hide FMG with dissolve
    "Matsumoto shot daggers at Mizutani with her eyes until she left to get more benches, then she turned to me in a huff."
    "My eyes snap to hers, momentarily mesmerized by just how sizable her rear was underneath the school-issue uniform."
    $ setAffection("AE", 1)
    show AE happy
    AE "Hmph. Thank you for not butting in on that...{w}spectacle.{w}\nI'm Matsumoto Shiori, and you are?"
    "We introduced ourselves, and Matsumoto informed us that we were in the same class as her, class 3-B."
    "She asked us to go to our room and help two other students she'd sent earlier in the day to prepare the room, expressing some doubt as to their competence."
    hide AE with dissolve
    show BE neutral at center with dissolve
    BE "You think she's ever happy with anyone? Doesn't seem the type..."
    jump global000_BBW

label global000_BBW:
    scene black with dissolve
    "We left the arguing pair behind and entered the school proper.{w} Honoka led me through the hallways with ease, until we came to one classroom in particular..."
    
    scene Classroom with dissolve
    play music BBW
    "So this was Classroom 3-B. I would be spending a lot of time here for the next year."
    "The first thing I noticed was that, much like the rest of the shool, the classroom seemed very big. It was much larger than any that I had been in before."
    "Whether or not this meant that there would be more students, or if this was just something that made this school different, I had no idea."
    "The next thing I noticed was that Honoka and I weren't alone in the room. Sitting across from us, at the head of the classroom, was another girl."
    show cg BBW001 with dissolve
    "She had a round face, and bright blue eyes framed by gold colored hair.{w} It seemed as though we had a foreigner in our midst."
    "She was sitting with her feet on one of the desks, but stood up and grinned when she saw us enter."
    UNKNOWN "Oh? What have we here? I guess that Shiori told you to come up here too?"
    UNKNOWN "I have everything under control here."
    BE "Who are you?"
    hide cg with dissolve
    show BBW neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    BBW "I'm Alice Nikumaru.{w} Charmed, I'm sure."
    "After introducing herself, Alice sat back down in her makeshift throne. Before I could open my mouth to speak, she looked past us."
    show BBW angry
    BBW "Will you hurry up already?!"
    BBW "I want to go get something to eat and I can't do that if you're slacking off!"
    "I followed Alice's gaze. I hadn't noticed at all but there was a mousy girl in the room as well."
    hide BBW with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    "Her hair was tied up in a pair of tails, and she was carrying a globe."
    show PRG sad
    UNKNOWN "{size=-6}Sorry!{/size}"
    show BE surprised at Position (xpos=0.25, xanchor=0.5)
    BE "Oh wow! Sorry about that, but I totally didn't see you there!"
    show BE neutral
    BE "I'm Inoue Honoka! Pleased to meet ya!"
    MC "Hotsure Keisuke."
    show PRG neutral
    PRG "Aida...Kodama Aida."
    hide BE
    show BBW neutral at Position (xpos=0.25, xanchor=0.5)
    BBW "Great, great.{w} Now everybody knows everybody, and Aida can finish decorating. She's almost done anyway."
    menu:
        "Well, if you've got this under control...":
            jump global000_BBW_c1
        "Shouldn't you be doing something too?":
            jump global000_BBW_c2
            
label global000_BBW_c1:
    MC "Well, if you've got this under control, I guess I'll be going then."
    $ setAffection("BBW", 1)
    $ setAffection("PRG", -1)
    $ setAffection("BE", -1)
    BBW "Glad to see at least someone can follow orders."
    show BE surprised at center with dissolve
    BE "{i}Kei-chan{/i}!"
    "I winced. I might not have seen Honoka for years, but I remembered that tone well enough."
    hide BE with dissolve
    MC "Okay, okay. We'll help too."
    show PRG sad
    PRG "...I don't want to be a bother."
    BBW "Hmph. {w}Well, if you insist, I'm sure I can find something for you to do. {w}The sooner we're done here, the better."
    jump global000_RM
            
label global000_BBW_c2:
    MC "Shouldn't you be doing something too?"
    $ setAffection("BBW", -1)
    $ setAffection("PRG", 1)
    show BBW neutral at Position (xpos=0.25, xanchor=0.5)
    BBW "I'm doing something!"
    show BBW happy
    BBW "I'm su{w}per{w}vi{w}sing!"
    hide BBW with dissolve
    PRG "It's okay...{w}I don't need any help."
    MC "It's fine. We're all supposed to be working together, right?"
    show PRG happy
    PRG "T-thank you! Thank you very much!"
    jump global000_RM
     
label global000_RM:
    scene Hallway with fade
    stop music
    show BE neutral with dissolve
    BE "Alright, well, it looks like everything's ready for tomorrow...{w}(No thanks to queenie over there.){w} Time to get back to the dorms, I guess!"
    MC "They wouldn't happen to be co-ed, would they?"
    show BE happy
    BE "Oh, Kei-chan! You're such a kidder!{w} Of course not!"
    "Honoka's laugh caused her impressive bust to shake violently, which was a small consolation prize as we parted ways."
    hide BE with dissolve
    scene School Inner with fade
    
    "I headed over to the boy's dormitories, seeing they were just as enlarged as the rest of the school.{w} I felt like a child, trying the doorknob that I couldn't even get my entire hand around."
    "*Kunk-Kunk*"
    MC "Locked? I'm sure I had the right--"
    play music RM
    UNKNOWN "Who is it?!"
    MC "Aaah!"
    UNKNOWN "Who is it? Identify yourself!"
    menu:
        "Uh...Pizza delivery?":
            jump global000_RM_c1
        "Hotsure Keisuke. I...think this is my room?":
            jump global000_RM_c2
        "Don't worry, I'm from the government!":
            jump global000_RM_c3
            
label global000_RM_c1:
    MC "Uh...{w}Pizza delivery?"
    UNKNOWN "I didn't order any pizza!{w} Scram!"
    MC "Hahaha...It was just a joke, this is my dorm room.{w} I guess you're my roommate?"
    "The door opened a crack and a single narrowed eye looked out at me."
    UNKNOWN "This is your dorm?{w} Are you sure?"
    MC "Preeeetty sure...{w} Says right here on my paperwork, see?"
    "I pulled out my transfer documents from the top pocket of my luggage, but he snatched them away before I could even show them."
    "The door shut briefly, then opened again, the boy inside still glaring at me through one narrowed eye."
    UNKNOWN "Hotsure Keisuke...{w}Let's see some ID."
    MC "Haha, no way, really?"
    UNKNOWN "Really."
    "Just wanting to get inside and get things over with, I sighed and handed over my ID."
    "More squinting, and then finally he opened the door all the way."
    show RM neutral with dissolve
    RM "Alright, you check out...{w}My name's Daichi Utagashi."
    $ setAffection("RM", -1)
    scene Dorm Interior with fade
    show RM neutral
    jump global000_RM_after
    
label global000_RM_c2:
    MC "Hotsure Keisuke. I...{w}think this is my room?"
    "I could hear movement behind the door, like someone searching for something.{w} After a bit, the door opened a crack, a single narrowed eye looking me up and down."
    UNKNOWN "Hotsure, huh?{w} Let's see some ID."
    MC "Haha, no way, really?"
    UNKNOWN "Really."
    "Just wanting to get inside and get things over with, I sighed and handed over my ID."
    "More squinting, and then finally he opened the door all the way."
    show RM neutral with dissolve
    RM "Alright, you check out...{w}My name's Daichi Utagashi.{w} Come in, I don't like leaving the door open."
    scene Dorm Interior with fade
    show RM neutral
    jump global000_RM_after
    
label global000_RM_c3:
    MC "Don't worry, I'm from the government!"
    "I thought my fake-authoritative voice would have been worth a laugh, but instead there was silence.{w} I knocked again, tried the knob, called out a few times, but there was no answer."
    "I put my ear against the door and could hear movement, so I moved over to one of the windows and took a peek in,{w} only to see the mystery occupant hurling his bags out the opposite window!"
    scene Dorm Exterior with fade
    "I left my luggage by the door and ran around the dorm, coming around the other side just in time to see him struggling out the window."
    show RM angry with vpunch
    UNKNOWN "Aaah! D-Damn you!"
    RM "Daichi Utagashi isn't going without a fight!"
    "Daichi tried to go back inside, but he had already squirmed too far out to get back through the window."
    RM "Rrrgh!{w} Hrff!{w} Nnngh...{w}Dammit, I'm s-stuck!"
    MC "Will you calm down for a second and tell me what's wrong???"
    RM "Don't play coy with me!{w} You're one of them!"
    MC "\"Them\" who?"
    RM "The government! You're here to monitor me, drag me off to some secret prison!{w} Put electrodes in my brain!"
    MC "It was just a joke!{w} I'm Hotsure Keisuke, I just got here, this is supposed to be my dorm!"
    "Daichi twisted around to look at me, his eyes narrowed."
    show RM sad
    RM "...If you really were one of them, I suppose you would have grabbed the evidence while I was helpless.{w} Help me back in and I'll open the door."
    MCT "Am I really going to have to live with this guy?"
    scene Dorm Interior with fade
    "After helping Daichi back through the open window and handing his bags to him {w}(He wouldn't let me carry them out of his sight){w} then checking my admission papers and ID, he finally unlocked the door and let me in."
    show RM angry
    RM "Don't get any funny ideas, 'Hotsure Keisuke'. I've got my eye on you..."
    $setFlag("RM_govagent")
    $ setAffection("RM", -3)
    jump global000_RM_after

label global000_RM_after:
    "When I finally got inside, it was obvious Daichi had claimed his half of the room.{w} Half the furniture had been crammed into one corner of the room, with blankets and sheets erected into a kind of tent over his desk and dresser."
    show RM neutral with dissolve
    MC "Er, so, do you want to--"
    RM "Do you know why you're here?"
    MC "Er, what?"
    RM "Why you're here, at this school?"
    MC "Well, I got the letter..."
    RM "Right after your health exam, right?"
    MC "Yeah..."
    RM "Hmph. Just as I thought."
    MCT "???"
    show RM sad
    RM "Haven't you ever seen those people on the news?{w} The giants over ten feet tall,{w} the gravure idols with 40kg breasts,{w} all the record holders for biggest this and longest that?"
    "Thinking back on it, I had seen some reports, starting when I was a little kid."
    "It wasn't often, but every now and then there'd be some picture or other of a giant-sized man or woman, always Japanese."
    RM "If you look into the histories and records of all these people, one thing is common to all of them--{w}they {i}ALL{/i} went to school at Seichou Academy!"
    MC "So, what are you saying?"
    RM "I'm saying the government brings certain students here and--{w}and does {i}something{/i} to them!"
    show RM angry
    RM "This kind of growth isn't natural,{w} it's statistically impossible for all of these one-in-a-million conditions to keep happening {i}just{/i} to Japanese school-age teens!"
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
    MCT "Hard to believe just yesterday I was in my hometown, and now I'm off on this little island..."
    "I got up and got into my uniform, doing my best to comb my shaggy hair into something approaching proper.  In the corner of my eye I saw Daichi watching me."
    if getAffection("RM") >= 0:
        show RM neutral
        RM "Today's the welcoming ceremony. I'm going to go get the lay of the campus."
        MC "You're going to skip the opening ceremony?"
        show RM angry
        RM "Of course not.{w} I need to get the official story so I know where to start investigating."
        hide RM with dissolve
        "I shook my head, but waved goodbye nonetheless as Daichi left.  At least he seemed in good spirits."
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
    "As I followed the signs to freshman welcoming, I couldn't help but notice how flat the campus seemed.  Despite the large buildings, most of them were divided into a handful of floors at most." 
    "Also, there didn't seem to be any stairs anywhere. Any dips or slopes in the elevation were all traveled with ramps."
    scene Auditorium
    with dissolve
    "When I finally reached the auditorium, I found I was still early enough to have my choice of seats."
    MCT "Where should I sit...?"
    menu:
        "I should sit in the front where the Principal can see me.":
            jump global000_sit_c1
        "I should sit somewhere in the middle.":
            jump global000_sit_c2
        "I should sit in the back, where no one will notice me.":
            jump global000_sit_c3

label global000_sit_c1:
    "I decided to sit in the front row, where the principal could see me. If I ever needed to speak with him, recognizing my face might make him better disposed toward me."
    MCT "This is a good seat...  Got spaces on either side of me."
    "{color=#FF69B4}*FLUMPH!*{/color}"
    MCT "!!"
    MCT "I... Is that..."
    show AE neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    MCT "Shiori-san's butt is overflowing her seat and pushing against me...{w} I can't say anything about it with everyone else around..."
    MCT "I'll just quietly scoot away from her-"
    "{color=#FF69B4}*PLOMF!*{/color}"
    MCT "Oh no!"
    show BBW neutral at Position(xpos=0.25, xanchor=0.5) with dissolve
    MCT "Alice-San! She's taking up all of her seat and half of mine! What do I do??"
    MCT "I'm in the middle of a womanly butt-sandwich and it's like I'm the only one to notice! I've got to distract myself before something even more embarrassing happens!" #with Shake((0, 0, 0, 0), 0.75, dist=20)
    menu:
        "So, Shiori-san...":
            jump global000_sit_c1_1
        "Hi there, Nikumaru-san...":
            jump global000_sit_c1_2

label global000_sit_c2:
    "I decided to sit in the middle of the auditorium, where I could still hear the speeches without being so front-and-center."
    MCT "Let's see, somewhere around here should be--"
    BE "Pssst!  Kei-chan!"
    show BE happy at Position(xpos=0.25, xanchor=0.5) with dissolve
    MC "Honoka?"
    BE "Kei chan, over here!  I've got a seat saved for you!"
    "I made my way down the row of chairs to the seat Honoka was patting next to her."
    "I noticed when I passed by Honoka, she had to lean back slightly to keep her bosoms from dragging across me, and the thought made me blush."
    "When I sat down and let the breath I'd been holding out, I realized I was sitting next to the girl we'd met gardening the evening before."
    show GTS neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    show BE happy
    BE "Isn't this great, Kei-chan?  It's just like grade school again!"
    GTS "You two... Went to school together?"
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
    "The rest of the row was nearly empty, save for a small girl in the corner who I recognized from the night before as Aida-san."
    show PRG neutral at Position(xpos=0.25, xanchor=0.5) with dissolve
    "I also noticed she was looking at me, but as soon as our eyes met she turned away...{w}before slowly turning back to watch me from the corner of her eye."
    menu:
        "Needed the room to stretch out, Mizutani?":
            jump global000_sit_c3_1
        "Seems kinda lonely back here, Aida...":
            jump global000_sit_c3_2


label global000_sit_c1_1:
    hide AE
    hide BBW
    MC "So, Shiori-san..."
    show AE neutral
    AE "Shhh! {w}They're about to start."
    MC "I know, but I was just, ah, wondering--"
    AE "You noticed too? It's weird, isn't it? Normally you have the whole faculty on-stage for these things, but it's just the principal and a few others..."
    "I nodded dumbly, realizing only then that behind the principal on stage there were only a handful of faculty members."
    "It definitely seemed sparse, despite the size of the stage, but I wasn't about to attribute it to anything nefarious like Daichi would."
    "I opened my mouth to try and ask about the ass-squishing she's giving me, but the principal clearing his throat into the microphone snapped Shiori's attention to the stage."
    MCT "No use talking now, I suppose...  But it's nice she thought I was clever enough to notice."
    $ setAffection("AE", 1)
    jump global000_sit_after

label global000_sit_c1_2:
    hide AE
    hide BBW
    MC "Hi there, Nikumaru-san..."
    show BBW neutral
    BBW "Alice, please, no need to be so formal. *giggle* {w}But I'll accept 'Princess' if you insist..."
    MC "Ah, so, uh, Alice..."
    BBW "Hm?"
    MC "Well, your seat- ah, I mean, the seat, it's a little..."
    show BBW happy
    BBW "Ahahaha~! Yes, the seats are a little small...{w}but you don't mind, I'm sure?"
    "The wink she gave me made me wonder how much of her pressing into me was accidental and how much was intentional."
    show BBW neutral
    BBW  "Oop, they're starting. Eyes forward."
    $ setAffection("BBW", 1)
    jump global000_sit_after

label global000_sit_c2_1:
    hide BE
    hide GTS
    MC "Find your dorm okay, Honoka?"
    show BE happy
    BE "Yep!  It's amazing how big it is...{w}makes my bedroom at home look like a closet!"
    MC "Yeah, and for freshmen, even!"
    show BE neutral
    BE "But you know what's weird? I haven't seen a single upperclassman yet. Like, not anywhere. They're all starting today, right?  Aren't they?"
    MC "I don't know, really.  Maybe this is some kind of half-day for upperclassmen, they start later than us?"
    show BE surprised
    BE "That could be! I've never heard of a school doing that on the first day, though..."
    MC "I'm sure they'll explain it to us in homeroom. Hopefully we can get seats next to each other!"
    show BE happy
    BE "Yeah! That'd be great, Kei-chan! Just like old times!"
    MC "Shhh, not so loud, they're starting! But yeah, just like old times..."
    $ setAffection("BE", 1)
    jump global000_sit_after

label global000_sit_c2_2:
    hide BE
    hide GTS
    MC "What was your grade school like, Naomi?"
    show GTS neutral at Position(xpos=0.75, xanchor=0.5)
    GTS "Mine?"
    MC "Sure, you heard about ours..."
    show BE neutral at Position(xpos=0.25, xanchor=0.5)
    BE "Yeah, what was yours like, Naomi-san?"
    show GTS neutral
    GTS "Well, ah, it was...{w}pleasant, I suppose."
    MC "\"Pleasant\"?"
    GTS "That is, ah...{w}it was rather...{w}Mm...{w}My old schools were always very well organized and regimented."
    MC "...Not very fun, then?"
    show GTS happy
    GTS "They had a wonderful garden in the back."
    MC "Well, hopefully this school will be fun for you."
    #hide GTS
    show BE happy
    BE "Yeah! We'll do all we can to make sure you have at least one fun school!"
    show GTS happy
    GTS "...Thank you, both of you. Now, we musn't be speaking once the principal starts..."
    $ setAffection("GTS", 1)
    jump global000_sit_after

label global000_sit_c3_1:
    hide PRG
    hide FMG
    MC "Needed the room to stretch out, Mizutani?"
    show FMG neutral
    FMG "Oh hey, it's, uh, Hotsure, right?"
    MC "Yep! So, ah, not interested in the speech?"
    FMG "Eh, whatever, I don't mind. Just like the back because I hate being squeezed between people. Gets a litle claustraphobic."
    MC "Yeah, and like, on the trains..."
    show FMG happy
    FMG "Oh I know, those are even worse! Especially for a tall girl..."
    MC "I hope no one's ever given you trouble..."
    show FMG neutral
    FMG "Heh heh...{w}one guy tried to cop a feel, once."
    MC "What happened?"
    "Mizutani's smile tightened into a predatory, self-satisfied grin."
    show FMG happy
    FMG "Busted his finger. Wasn't even trying to."
    MCT "Ooooo-kay, I'm suddenly very interested in what the principal has to say..."
    $ setAffection("FMG", 1)
    jump global000_sit_after

label global000_sit_c3_2:
    hide PRG
    hide FMG
    MC "Seems kinda lonely back here, Aida..."
    show PRG sad
    PRG "Oh!  Uh, ah, well, there's three of us now, right?"
    MC "Heh, I suppose."
    show PRG neutral
    PRG "W-well, you can sit next to me...{w}if you like."
    MCT "Boy, she's acting strange...{w}like she wants to get close but is spooked of it..."
    MC "Nervous about starting at a new school?"
    PRG "A little. Could use a friend..."
    MC "Well, can't everyone?"
    PRG "Yeah...{w}Could- could you be my friend?"
    "She smiled at me, and I felt her lean over in her seat, lightly touching my side with her shoulder."
    MC "Heh, sure...{w}if you need one."
    show PRG happy
    PRG "I do..."
    "We sat there, listening to the Principal's speech. I noticed Aida-san leaning a little closer into me as it went on."
    $ setAffection("PRG", 1)
    $ setFlag("global1000_aidasit")
    jump global000_sit_after

label global000_sit_after:
    hide PRG
    hide BBW
    hide GTS
    hide FMG
    hide AE
    hide BE
    "The ceremony continued, all dreadfully familliar and rote, but at the end there was something different. The principal settled the papers behind the podium and hesitated for a too-long moment."
    "\"The future is forever uncertain,\" he said.{w} \"But no matter what the future holds, years hence or any day now, one thing is important  above all else.\""
    "\"{i}Nosce te Ipsum{/i}. {w}To thine own self be true. Remember that you are more than your station, {w}skills, {w}and especially appearance. If you need help, your teachers are always available to help you with whatever you need.\""
    MCT "What's he going on about...? I'm beginning to wonder if Daichi was on to something..."
    "Finally, the ceremony ended, and we all began to file out."
    stop music
    show AE sad
    play music AE
    "I saw Shiori hustle out to stand by the doors ahead of nearly everyone else, her rear wobbling side to side in a way was impossible to not draw the eye."
    MC "Shiori-san?  What's going on?"
    AE "I didn't see Utagashi in the assembly. He'd better not have skipped out on the first day or there will be hell to pay.  Hey, isn't he your roommate?"
    menu:
        "I haven't seen him...":
            jump global000_aftersit_c1
        "He said he wouldn't miss the ceremony..." if getFlag("global000_RM_friendly"): #This menu item will only appear if this variable is True
            jump global000_aftersit_c2
        "He left the dorm pretty early..." if not getFlag("global000_RM_friendly"): #Likewise, this item only appears if the variable is False
            jump global000_aftersit_c3


label global000_aftersit_c1:
    MC "I haven't seen him...{w}but he was acting kind of strangely this morning. No telling where he went off to."
    show AE neutral
    AE "Hmph. He'd better have a good excuse!"
    hide AE with dissolve
    "I left to go to my homeroom class, worrying no excuse would be good enough for Shiori..."
    $ setAffection("RM", 1)
    jump global000_homeroom

label global000_aftersit_c2:
    MC "Well, he said he was going to make sure not to miss the ceremony..."
    show AE neutral
    AE "He did? Then why didn't I see him come in?"
    MC "He said he was going to walk around campus a bit this morning, get a feel for the place. Maybe he came in some different door?"
    "Shori looked back into the mostly-empty auditorium, eyes scanning the walls."
    AE "You know, I didn't consider that he could have come from a non-proscribed entrance, actually. I'll have to quiz him on the announcement's content later."
    hide AE with dissolve
    "She nodded and left her post, satisfied with the answer, and we both walked to homeroom."
    $ setAffection("AE", 1)
    $ setAffection("RM", 1)
    jump global000_homeroom

label global000_aftersit_c3:
    MC "He left the dorms pretty early, don't know where he was off to..."
    show AE neutral
    AE "Hmph.  Well, he certainly wasn't here. Bah, I don't have time to waste on the likes of him.  Thank you for telling me, though, so I didn't stand there until the bell rang."
    hide AE with dissolve
    "With a derisive grunt, Shiori left her post by the doors and we walked to homeroom together."
    $ setAffection("AE", 1)
    $ setAffection("RM", -1)
    jump global000_homeroom

label global000_homeroom:
    scene School Exterior with fade
    play music Schoolday
    "With the principal's strange welcome still echoing in my ears, I headed for the class building, ready to start my academic career at Seichou Academy..."
    
    scene F1 Hallway with fade
    "It was very strange to be in the hallways with so few people. Well, there were a normal amount of students, but in Seichou's oversized architecture we all felt miniscule.{w} I spied Honoka and some of my other classmates as we walked along, feeling like ants in a dog carrier."
    show BE surprised
    BE "Just how many students are there here, that they need such big hallways?"
    hide BE
    show FMG neutral
    FMG "Beats me...{w}I feel like I should be putting up a volleyball net or something."
    
    scene Classroom with fade
    MC "Whoa!"
    show BBW neutral
    BBW "...Is this for real?{w} How come there are so few seats?"
    hide BBW
    show PRG neutral
    PRG "And so far away?"
    hide PRG
    show AE neutral
    AE "Some kind of anti-cheating measure...?"
    hide AE
    "Eventually we all took our seats, looking around at the sparse classroom. All the usual educational aids seemed to be on shelves or set into the wall, making the room seem even more like an empty box than it already was."
    "If not for the teacher's lectern at the front of the class, you'd be forgiven for thinking we were in a pen instead of a classroom."
    "Finally the bell rang, and at the last possible second one could enter and not be late, our homeroom teacher slid open the door and entered."
    MCT "'Dour' is the first word that comes to mind... Guy looks like he's been middle-aged his entire life."
    "The man was tall, thin but not fit, wearing a collared shirt and dress slacks, with a jacket draped over one arm until he casually tossed it on the lectern. He swiped a piece of chalk up off the board and quickly scratched out his name on it."
    "{i}Tashi{/i}"
    "Tashi-Sensei dropped the chalk back on the tray, turned to us, and stepped forward, leaning against the lectern."
    stop music
    HR "..."
    show GTS neutral
    GTS "..."
    hide GTS
    HR "..."
    show RM neutral
    RM "..."
    hide RM
    HR "..."
    MC "..."
    show HR neutral
    "Without a word, Tashi-Sensei opened his mouth, and the classroom gasped as a four foot long tongue flopped out, unfurling down past Sensei's belt."
    hide HR
    show AE angry with vpunch
    AE "Kyaa~! What is that?!"
    hide AE
    show BE surprised with vpunch
    BE "Oh, ick!"
    hide BE
    show BBW angry with vpunch
    BBW "Keep that thing away from me!"
    hide BBW with dissolve
    show HR neutral with dissolve
    "..."
    "..."
    play music Busy
    HR "All right, go ahead, get it out now. But don't run away or you'll be marked tardy."
    "The non-chalance in the teacher's voice quickly turned the class' mood from panic to confusion, especially as that giant tongue continued to flop around as Tashi-Sensei got into his bag and set his papers down on the lectern."
    HR "All done? {w} Good. Here's how this works."
    HR "Welcome to Seichou Academy. You're here because you, or a sibling, have expressed a certain trait that causes unusual growth of some kind."
    hide HR
    show BE surprised at Position (xpos=0.25, xanchor=0.5) with dissolve
    HR "Some of your growths are already obvious..."
    show PRG neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    HR "Others...{w}Not so much."
    hide BE
    hide PRG
    show HR neutral with dissolve
    HR "But make no mistake, unless you've got a sibling here at Seichou Academy, you're {i}going{/i} to change; even if you do, you've got good odds of changing yourself."
    HR "I know the Principal likes to dance around it, but I'm not going to mince words:{w} Seichou Academy is here to help you deal with whatever you're going to become. Key word being \"Help\"."
    HR "We can get you uniforms that fit, doors you can walk through, and gym classes for any shape and size.{w} What we can't give you is resolve, self-acceptance, the courage to make a life for yourself after whatever life makes out of you." 
    "Tashi-Sensei scanned the room, taking in the fear and confusion, then shrugged."
    HR "Anyways, that's my big freshman speech. Don't expect more.{w} So, roll call. Matsumoto-San?"

    scene black with dissolve
    stop music

    "So I found myself at Seichou Academy, orientation behind me and a long, strange journey ahead."
    "What was I supposed to do now, knowing what I do about the bodies of the student body?"
    jump daymenu

label global005:
    $setTimeFlag("testday2")
    scene Dorm Interior with fade
    "When I woke up this morning, Daichi was nowhere to be found."
    "I thought it was unusual for him, usually the mornings were filled with the clicking of mice and keyboards as he did his 'research'.  Still, it was a welcome break to not have him eyeing me as I brushed my teeth or whatever."

    scene Hallway with fade
    play music Busy
    "As I made my way inside the classroom building, I ran into a few of my classmates."
    
    if prefgirl == "BE":
        show BE neutral with dissolve
        BE "Hey there, Kei-chan!  How are things going for you?"
        MC "Oh, pretty good. You?"
        BE "Still getting used to how big this campus is! I've been spending some time walking around each night and I still haven't seen it all!"
        MC "Wow, I haven't been around much either..."
        BE "Maybe we can go exploring together sometime!"

    if prefgirl == "WG":
        show BBW neutral with dissolve
        BBW "Hotsure-san."
        MC "Oh, hello Nikumaru-san."
        BBW "Please, I've told you before, call me Alice. Formalities are for business, I find them so tiresome in normal conversation."
        MC "Er, okay, Alice... but you called me Hotsure-san."
        BBW "Because you were expecting it, of course. In any case, I'm looking forward to today's lessons. You?"
        MC "I suppose..."

    if prefgirl == "GTS":
        "I noticed Naomi-san walking next to me as we made our way to class.  Like, noticeably close."
        show GTS neutral with dissolve
        GTS "..."
        MC "Hey there, Naomi-san."
        GTS "Oh, h-hello."
        MC "..."
        GTS "..."
        MC "Nice day we're having, yeah?"
        GTS "...Yes."
        MCT "Boy, she's not much for conversation today... but she seems happy."

    if prefgirl == "FMG":
        show FMG neutral with dissolve
        FMG "Hotsure-san! How ya doin'?"
        "I cringed as Akira slapped me on the back in what she probably thought was a friendly manner."
        MC "Hrrrk!"
        FMG "Haha, catch you by surprise, did I?  Well, hopefully that'll wake you up a bit!"
        MC "It's nice to see you too, Mizutani-san..."
        FMG "Guess what I found out yesterday?  They've got an outdoor weight area behind the gym!  Can't wait to try it out!"
        MC "Does that make a difference?"
        FMG "Sure!  Morning and evening workouts can go harder than normal because you're being naturally cooled by the cold air!"
        MCT "I boggled to think what a 'harder' workout was for Akira, seeing how hard she already pushed herself..."

    if prefgirl == "PRG":
        show PRG neutral with dissolve
        PRG "H-hi Kei-sama!"
        MC "Oh, hi Kodama-san."
        PRG "I... I'd like it if you'd call me Aida..."
        MC "Yeah?"
        PRG "Yeah.  Like... a lot."
        MC "Okay, Aida. How are you today?"
        PRG "I'm fine. How are you? Did you sleep good? Get enough breakfast? I've got a snack if you're hungry..."

    if prefgirl == "AE":
        show AE neutral with dissolve
        AE "Hotsure-san."
        MC "Oh, hello Matsumoto-san."
        AE "Good to see you on time. I may have need of your assistance later."
        MC "Oh?"
        AE "It's measuring day for our class. I might need help corralling the student bodies through the process in an efficient manner."
        MC "Er, all right, sure."
        AE "I wasn't asking."

    scene Classroom with fade
    MC "When we got to Room 3-B, we found a message written out on the blackboard, announcing that we were all supposed to head to the gymnasium."
    show AE neutral at Position (xpos=0.8, xanchor=0.5) with dissolve
    AE "All right, everyone, it's measuring day for our class, so let's get an orderly line going."
    show FMG happy at Position (xpos=0.25, xanchor=0.5) with dissolve
    FMG "Oooh, neat! I've been wanting to get my guns professionally measured for a while!"
    BBW "..."
    hide FMG with dissolve
    AE "Kodama-san, you stay behind, we've got... five stragglers, it looks like."
    show PRG neutral at Position (xpos=0.5, xanchor=0.5) with dissolve
    show BBW neutral at Position (xpos=0.2, xanchor=0.5) with dissolve
    BBW "Excuse me, but Aida is otherwise engaged."
    show PRG neutral at Transform(xzoom=-1)
    AE "Not now she isn't, unless there's some other class president I'm unaware of."
    show PRG neutral at Transform(xzoom=1)
    BBW "I'm sure you can find someone else. Aida is developing a set of very specialized skills."
    show PRG neutral at Transform(xzoom=-1)
    AE "I'm sure she is. AFTER classes. During school hours she'll submit to school authority."
    show PRG neutral at Transform(xzoom=1)
    show BBW angry
    show AE angry
    BBW "..."
    AE "..."
    show PRG neutral at Transform(xzoom=-1)
    pause 1
    show PRG neutral at Transform(xzoom=1)
    BBW "..."
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
    show BBW neutral
    BBW "...Hmph!"
    MCT "...Those two aren't used to accepting 'no' for an answer, that's for sure..."

    scene Auditorium with fade
    play music Rain
    "The auditorium had been set up with what amounted to a field clinic, privacy dividers erected in a series of squares, with various testing and measuring devices set on folding tables."
    "I noticed that unlike at my previous schools, it seemed there were no student volunteers; every station seemed to be manned by a medical professional of some sort."
    AE "Class 3-B, over here! Line up along this partition, and- no, not alphabetically, by seat number. What do you mean you don't know what your seat number is??  Haven't you been paying attention at all?"
    "The lines were small, but given how thoroughly they were measuring everyone- I supposed being here meant there was a much wider set of variables that could be changing- each person took as long as several might at my older schools."
    "I didn't have much time to think about it, though- my name was one of the first few called up. I was directed first to a small cubicle in the corner, where I was to hear the specific results of my growth factor test."
    "I went into the little corner-cubicle, halting in my tracks as soon as the nurse turned to face me."
    Nurse "Hello, Hotsure-san, please have a seat."
    "I sat on the stool, my amazement at the size of her lips only slightly eclipsing my amazement that she could talk without a lisp. They were so enormous and puffy I literally couldn't see her chin, the top curve of her upper lip nestled against the bottom of her nose."
    "What was more, she had decided to cover them in bright red lipstick. It was nearly impossible not to stare as she looked down at a clipboard full of papers."
    Nurse "So, your growth factor has been confirmed to be... Heh, you like them?"
    MCT "Oh crap, she caught me staring!"
    MC "No, I, uh, I mean, they're-"
    "Her lips actually managed to pull out into a smile, making nearly the entire bottom half of her face hidden behind them."
    Nurse "It's all right, I know they can be surprising. Whenever I go off-campus I have to wear a surgical mask or I can hardly do anything for all the gawking and questions."
    "I just nodded and looked away, wondering what I would have to do to live a normal life."
    Nurse "Anyways, your growth factor.  According to these results, you have hyper-productive hair follicles. Not hypertrichosis, so you don't need to worry about having to shave your nose and forehead and so on, but you'll definitely need a barber more often than most."
    MC "My hair? It's always grown like a weed, that's nothing new."
    Nurse "Heh heh... Well, the degree is never certain, but remember that it's not fully manifested yet. Whatever rate of growth you're used to, it will increase by some amount, guaranteed."
    MC "And... And my sister? Does she have the same thing?  Does she have anything at all?"
    Nurse "I'm sorry, but since she's not a minor anymore I'm not allowed to share her medical information with anyone she hasn't specified..."
    "I mulled over this for a few seconds while she wrote on her clipboard."
    MC "So, that's it? Is it going to be all of my hair, er, everywhere?"
    Nurse "Body and head hair grow at different cycles and intensities, so it's hard to say. But we'll be sure to check up on all of your growth throughout the year, so please try and keep a record of each time you cut any of your hair."
    MC "...Do I have to?"
    Nurse "No, but we're only here to help.  If you're comfortable only knowing what you know now about your condition, we won't force you. But you still have to come in for measurements and such."
    MC "So, can I go?"
    Nurse "Right after we take some blood, yes. Just sit still and roll up your sleeve..."

    scene Auditorium with fade
    "I walked out of the nurse's cubicle, rubbing the cotton ball taped to the crook of my elbow.  Next was the height and weight measurements, then an eye test, then several other stations I didn't even know the purpose of."
    "All told, except for a few walled-off areas for privacy, all the tests happened in the same open area. I wondered if I would get to see/hear some of my classmates as I went through..."
    jump daymenu

label RM001:
    scene Dorm Interior with fade
    MCT "Another day of classes over..."
    "When I arrived back at my room, Daichi was already there, poking some device on his desk very intently with a soldering iron."
    "I couldn’t really tell what it was, beyond some kind of circuit board."
    show RM neutral with dissolve
    RM "..."
    MCT "To be honest, I still haven’t had a good chance to talk with him yet. Mostly because I don’t really see much of him outside of class."
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
            MC "So I can’t help but notice you usually come home kind of late. Are you in a club, or something?"
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
    RM "It’s something I need to know. Whether it’s a good idea or not is irrelevant."
    show RM angry
    RM "Unless you know someone in the class below us who’d be willing to spy for me, this is my best option."
    MC "Can’t say that I do."
    MCT "I’m *not* getting my sister involved with this guy."
    show RM neutral
    RM "Then I’m using the camera."
    "I didn’t really have a good response to that. He took the opening to continue his work."
    MCT "Maybe I should try a lighter topic?"
    jump RM001_after

label RM001_c1_2:
    "He answered me without turning around, opting instead to continue tinkering with the device."
    RM "I’m busy investigating."
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
        MC "Are you still upset over the ‘I’m a government agent’ thing?"
        show RM neutral
        RM "Yes."
        MC "Look, I’m sorry. I didn’t realize it was such a... sensitive subject."
    else:
        MC "Did I do something to offend you?"
        show RM neutral
        RM "You don't appreciate the situation we're in, for one."
        MC "I'm... sorry?"
    show RM smug
    RM "Apology accepted - I’ll forgive your ignorance. If you’re willing to take this seriously, I can enlighten you on a few things. Interested?"
    MCT "Is it too late to change roommates?"
    MC "Maybe another time."
    show RM neutral
    RM "Suit yourself."
    "An awkward silence descended as he went back to working on... whatever it was."
    MCT "Maybe I should try a lighter topic?"
    jump RM001_after

label RM001_after:
    MC "Hey, what do you like to do for fun? Got any hobbies?"
    RM "Not really. Haven’t had time lately. Been too busy trying to figure out what’s going on here."
    MC "Well, what about before you came to the school? Or was it just more conspiracies?"
    "That comment caused him to finally stop working and turn around to face me."
    show RM angry
    RM "Please. I’m not some kind of conspiracy nut. It’s just that this school is too weird."
    RM "The fact that more people aren’t suspicious of this place is mind-boggling to me."
    MC "Fine, fine, whatever. What did you do before you came here?"
    show RM neutral
    RM "...I read manga, I guess?"
    MC "That’s a start! What did you read?"
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
    RM "I used to play Suncraft, a few years back. Haven’t played in a while, though."
    MC "Oh. I’ve never heard of it."
    RM "It’s a strategy game. I always thought it was pretty fun."
    MC "I see."
    show RM sad
    RM "..."
    MC "..."
    MC "Well, what about your project there? Do you like tinkering with stuff?"
    show RM neutral
    RM "It’s alright, I guess."
    MC "What about when you graduate? You going to go into electrical engineering or something?"
    RM "Maybe? I haven’t decided yet."
    RM "I’ve thought about becoming a teacher, too."
    MC "Why a teacher? You like learning?"
    RM "I want kids to get more critical thinking skills, so they won’t just mindlessly obey authority."
    MC "Oh."
    RM "..."
    MC "..."
    MCT "This is going great."
    menu:
        "Can you show me what you’re working on?":
            jump RM001_c2_1
        "Well, time to study!":
            jump RM001_c2_2

label RM001_c2_1:
    if getFlag("RM001_c1_1"):
        MC "Well, hey, why don’t you show me what you’re doing with your camera?"
    else:
        MC "Well, hey, why don’t you show me your... whatever it is."
        "He sighed and held up a lens, which was hiding behind some other components."
        RM "Camera. It’s a camera."
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
        MCT "I don’t know if it’s ever going to be useful, but it was pretty informative."
        $setSkill("Academics", 1)
        jump daymenu
    else:
        show RM angry
        "...But then turned back around in a huff."
        RM "I’m busy. I’ve wasted enough time answering your questions."
        MC "Fine."
        jump RM001_c2_2

label RM001_c2_2:
    MC "Well, I need to study. Have fun with your project."
    show RM neutral
    RM "Mmm."
    "We didn’t say anything to each other for the rest of the night."
    "The quiet room helped me focus, though."
    $setSkill("Academics", 1)
    jump daymenu

label RM002:
    scene Hallway with fade
    "I followed the crowd out of the classroom as everyone shuffled toward the cafeteria."
    "Out of the corner of my eye, inside another classroom, I noticed..."
    show RM neutral at Position (xpos=0.95, xanchor=0.5) with dissolve
    play music RM
    pause 2
    show RM angry
    "He glared at me and made a beckoning motion."
    "Resigned, I walked over to him and hissed..."
    hide RM with dissolve
    show RM neutral at Position (xpos=0.5, xanchor=0.5) with dissolve
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
        "What are you doing, exactly? (disabled)" if getFlag("RM002_c1_2"):
            pass
        "This is a stupid idea.":
            jump RM002_c1_3

label RM002_c1_1:
    $setFlag("RM002_c1_1")
    MC "You’re right, that does sound simple. Alright, go ahead."
    show RM happy
    $setAffection("RM", 1)
    RM "Thanks. I’ll be quick."
    jump RM002_c1_after
    
label RM002_c1_2:
    $setFlag("RM002_c1_2")
    MC "What exactly are you doing in there?"
    "After scanning the hallway to make sure nobody was paying attention, he discreetly showed me a familiar circuit board from his bag."
    RM "I’m placing the camera I made earlier. It shouldn’t take long."
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
        "Let her in (disabled)" if getFlag("RM002_c1_1"):
            pass
        "Signal Daichi":
            jump RM002_c2_2
        "Make up a story":
            jump RM002_c2_3

label RM002_c2_1:
    "I never agreed to play lookout for him. To be honest, I wasn’t even really sure why I was still there..."
    MC "Sure, go ahead."
    show Yuki happy
    UNKNOWN "Thanks!"
    RM "Wait! Wait wait wait!"
    show Yuki happy at Position (xpos=0.25, xanchor=0.5)
    show RM angry at Position (xpos=0.75, xanchor=0.5) with dissolve
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
    MC "Why? What’s wrong?"
    UNKNOWN "Oh, no big deal. I just left some books behind by accident."
    MC "Your books? Where are they? I can go find them for you, if you want."
    "While saying all this, I knocked on the door repeatedly. Judging by her lack of response, I don’t think she noticed."
    UNKNOWN "Oh, no worries. I can get them myself."
    MC "What books, if you don’t mind me asking?"
    UNKNOWN "...Math? Why does it matter?"
    "Before I could think of another way to stall her, Daichi came out of the room."
    hide Yuki with dissolve
    show Yuki neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    show RM neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    RM "Yuki-chan! What a pleasant surprise."
    Yuki "Daichi-kun? What are you doing here?"
    jump RM002_c2_after

label RM002_c2_3:
    MC "I wouldn’t go in there. They’re... de-roaching."
    UNKNOWN "Roaches? In just the one classroom?"
    MC "..."
    extend "Yes."
    show Yuki sad
    UNKNOWN "...Hmm."
    "Suddenly, the door opened."
    show Yuki sad at Position (xpos=0.25, xanchor=0.5)
    show RM neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
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
        MCT "‘What I was looking for?’ He said he was placing a camera... What’s with the act?"
        MCT "But he’ll probably get upset if I don’t play along."
    MC "Oh, good. Alright, I’ll see you back at the dorm, then."
    RM "Yeah, sure. Talk to you later, man."
    hide RM with dissolve
    hide Yuki with dissolve
    stop music
    "I began to walk down the hallway, but after a couple of seconds Yuki ran up to me."
    show Yuki neutral with dissolve
    Yuki "Hey... Hotsure-senpai."
    MC "Huh? What’s wrong?"
    Yuki "Do you think that there’s something weird happening at this school?"
    MC "What do you mean?"
    Yuki "Like... Do you think the staff are doing something strange to us?"
    MCT "Oh, no. Has Daichi filled her head with his nonsense?"
    MCT "Should I play along?"
    menu:
        "There’s a conspiracy":
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
    MC "No. I don’t know who told you that, but it’s ridiculous."
    show Yuki happy
    Yuki "All right."
    Yuki "For a minute there I was worried you were like my brother."
    show Yuki neutral
    Yuki "Um... Please don’t think too badly of him when he says stuff like that. I think he’s just stressed out about what’s going on."
    MC "I think we all are, at least a little bit. I’m not holding it against him."
    Yuki "Thanks. Don’t be afraid to say no if he’s making you do something weird. He might be mad for a little bit, but trust me - he gets over it fast."
    show Yuki happy
    Yuki "I’ll see you around, ok?"
    hide Yuki with dissolve
    "She walked back to Daichi, with a slight spring in her step."
    jump daymenu

label End:
    show black
    with dissolve
    centered "You have reached the end of this demo of Growth Academy."
    centered "If you'd like to keep up to date with the game's development or contribute and make it a reality, please visit us at: \n https://www.expansiongames.net"
    centered "During each scene, an \"affection\" score for each of the girls were recorded based on your choices."
    centered "In the full game, they will be very important in where the story will lead; including some exclusive plot events and the chance for the girl to fall in love with you."
    centered "For now, they're just plain numbers; here's how you did!"
    centered "Inoue Honoka: [BE_Affection] \n Yamazaki Naomi: [GTS_Affection] \n Mizutani Akira: [FMG_Affection] \n Matsumoto Shiori: [AE_Affection] \n Alice Nikumaru: [BBW_Affection] \n Kodama Aida: [PRG_Affection] \n Daichi Utagashi: [RM_Affection]"
    
    centered "Thanks for playing!"

    return   # Complete Game and Return to Main Menu; End Game conditions can be taken into account for potential rewards (such as exclusive images or the ability to view full-credits for having completed the game).
