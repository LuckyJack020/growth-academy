##
## Notes to potential writers:
##
## I'll be leaving comments as I learn so that I can refer back to them,
## and anyone that looks as this script afterwards will be able to tell what's going on. -- SaburoX
##
##
#You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# Images go in the Graphics folder, and so their file names are prefaced by 'Graphics/'.

# Backgrounds
image Lake Road = "Graphics/Lake Road.png"
image School Front = "Graphics/School Front.png"
image School Inner = "Graphics/School Inner.png"
image Gate Front = "Graphics/Gate Front.png"
image School Planter = "Graphics/School Planter.png"
image Hallway = "Graphics/Hallway.png"
image Classrroom Day = "Graphics/Classroom.png"
image Dorm Exterior = "Graphics/DormExterior.jpg"
image Dorm Interior = "Graphics/DormInterior.jpg"

# Charactr Portraits
image BE-1a = "Graphics/BE-1a.png" #BE Girl Neutral Portrait
image BE-1b = "Graphics/BE-1b.png" #BE Girl Happy Portrait
image BE-1c = "Graphics/BE-1c.png" #BE Girl Surprised Portrait
# image BE-1d = "Graphics/BE-1d.png" #BE Girl Angry Portrait
# image BE-1e = "Graphics/BE-1e.png" #BE Girl Sad Portrait
image BE-SC-1 = "Graphics/BE-SC-1.png" #BE Girl Scene 1
image BE-SC-2 = "Graphics/BE-SC-2.png" #BE Girl Scene 2
image GTS-1a = "Graphics/GTS-1a.png" #GTS Girl Neutral Portrait
image AE-1a = "Graphics/AE-1a.png" #AE Girl Neutral Portrait
image FMG-1a = "Graphics/FMG-1a.png" #FMG Girl Neutral Portrait
image BBW-1a = "Graphics/BBW-1a.png" #BBW Girl Neutral Portrait
image PRG-1a = "Graphics/PRG-1a.png" #PRG Girl Neutral Portrait
image RM-1a = "Graphics/RM-1a.png" #Roommate Neutral Portrait
image RM-1b = "Graphics/RM-1b.png" #Roommate Angry Portrait
image RM-1c = "Graphics/RM-1c.png" #Roommate Stern/Glum Portrait
image RM-1d = "Graphics/RM-1d.png" #Roommate Flustered/Embarrassed Portrait


# Declare characters used by this game.
# Remember that character codes are case sensitive. 
define MC = Character('Keisuke', color="#0066CC") # Main Character, speaking.
define MCT = Character('Keisuke', color="#0066CC", what_prefix='(', what_suffix=')') # Main Character, Thought. Note the special prefix and suffix tags to  place his thoughts in parentheses.
define BE = Character('Honoka', color="#FCCF20")
define AE = Character('Shiori', color="#FF3300")
define FMG = Character('Akira', color="#FF9900")
define BBW = Character('Alice', color="#CC33FF")
define PRG = Character('Kodama', color="#FF3399", what_prefix='{size=-6}', what_suffix='{/size}')
#Since Preg Girl is timid, her text is smaller by default. When she grows out of it, we can use a text tag to make her speech regular sized.
define GTS = Character('Naomi', color="#66FF33")
define RM = Character('Daichi', color="#BDB8A5")
define UNKNOWN = Character('???', color="#FFFFFF")

init python:
    style.menu_choice_button.background = Frame("choice_bg_idle.jpg",28,9) #These two commands set the background of all in-game choice-buttons.
    style.menu_choice_button.hover_background = Frame("choice_bg_hover.jpg",28,9)
    style.menu_choice.color = "#fff" #These two commands set the color of the font in the in-game choice buttons.

# The game starts here.

label start:
    $ BE_Affection = 0
    $ GTS_Affection = 0
    $ AE_Affection = 0
    $ FMG_Affection = 0
    $ BBW_Affection = 0
    $ PRG_Affection = 0
    $ RM_Affection = 0
    
    # Stops the title music with a fadeout of half a second.
    stop music fadeout 0.5
    
    # Begin the character introduction scene.
    scene characterintro:
        
    
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
    centered "Art assets are placeholders or otherwise unfinished and in general content has yet to be finalized."
    centered "For more information, visit\n http://growthacademy.socialparody.com"
    centered "Enjoy."
    
    # Move to Lake Road screen with a fade in transition.
    scene Lake Road
    with fade

    MCT "Ahh... It's really hot today."
    "I came to a stop on a wooden bridge overlooking a lake."
    "My name is Hotsure Keisuke. My spring vacation coming to an end,\n and I'm starting at a new school tommorrow."
    MCT "To be honest, I'm a little nervous."
    "It's supposed to be a boarding school, which is why I've got my luggage with me."
    "But..."
    MC "Where the heck am I?!\nI've been walking for an hour already!"
    "I was sure that I was lost, but as I was thinking that, I saw someone walking ahead of me."
    MCT "I guess I'd better ask for directions."
    MC "Good afternoon!"
    "At the sound of my voice, she turned around and faced me."
    
    show BE-1a
    with dissolve
    
    "It turned out to be a fairly cute girl, with brown hair."
    MC "Sorry, but can you tell me where I am? I'm a little lost."
    UNKNOWN "..."
    "She stared at me intently for a long time. Had I surprised her or something?"
    MC "See, I'm trying to find Seichou Academy."
    UNKNOWN "Seichou..."
    "Because of that, the girl seemed to realize something."
    
    show BE-1c
    
    UNKNOWN "Kei{i}-chan{/i}? Hey, you're Kei{i}-chan{/i}, right?!"
    MC "Wait, How do you know my name?"
    BE "What are you talking about? It's me! Honoka!"
    MC "Eh?!"
    "Come to think of it... I guess she is a little familiar."
    "I didn't recognize her at first because it's been so long, but this girl is Inoue Honoka."
    "We used to live in the same town a long time ago, and played together all the time."
    "But then her father got transferred, and she moved away..."
    BE "I can't believe you really don't remember me!"
    MC "Ahahaha... Sorry! It's been, what, seven years already?"
    show BE-1a
    BE "That's true, it has been that long already, hasn't it..."
    BE "...I guess I have to forgive you then. You've grown up so much, so it's unreasonable to expect you to remember me if I've changed just as much."
    MCT "Exactly! There are limits to a guy's memory, you know? Besides..."

    play sound "Audio/Boing.ogg"
    show BE-SC-1
    with vpunch
    
    MCT "I'm pretty sure I would have remembered those!"
    
    show BE-1a
    with dissolve
    
    BE "Kei{i}-chan{/i}?  You kind of spaced out there for a second."
    MC "Er... I was just thinking, have I really changed that much?"
    
    show BE-1a
    
    BE "Well, your hair is the same, but I remember when I used to be taller than you."
    
    show BE-1b
    
    extend " What about me, I've changed, right?"
    MC "...Maybe a little."
    MC "So, what are you doing out here?"
    
    show BE-1a
    
    BE "I'm actually on the lookout for new students coming to Seichou the long way around. I didn't imagine I'd run into you, Kei{i}-chan{/i}!"
    
    show BE-1c
    
    BE "Ah, wait! You said you were looking for Seichou Academy, right?"
    BE "Could it be that you're attending there?"
    
    show BE-1b
    
    extend "That's going to be my school starting tomorrow!"
    
    show BE-1a
    
    "...Now that I think about it, it looks like she's wearing a school uniform. I guess this means I might even be in the same class as Honoka."
    BE "Come on, Kei{i}-chan{/i}.\nI'll show you the way there."
    "So with that, I picked up my luggage and followed Honoka."
    
    show BE-SC-2
    with dissolve
    
    BE "So, how have you been?\nHow about Tomo{i}-chan{/i}, her too!"
    "Tomo{i}-chan{/i} is Hotsure Tomoko, my younger sister."
    MC "She's doing fine. So am I."
    MC "Actually, she and I will be attending this school together, but she's still packing, so she's not arriving today."
    MC "But anyway, I was really surprised, Honoka."
    BE "Yeah, I was a little nervous too, moving to a new boarding school and all."
    BE "But if you're going to be here, I'm sure it'll be great!"
    BE "I guess we'll both be in your care, Kei{i}-chan{/i}, so do your best!"
    MC "Right."
    BE "Ah! We're here!"
    
    scene School Front
    with fade
    "Before I realized it we had arrived at a huge school building. This was Seichou Academy."
    "This would be my new home for the next year.\nIt was really awe-inspiring at the time."
    "But even then, I had no idea just how much my life was going to change."
    jump GTSScene
    
label GTSScene:
    
    scene black
    with dissolve
    "As we entered the school grounds, I couldn't help but notice how big everything was."
    
    scene School Planter
    with dissolve
    "What looked at first to be normal-sized buildings turned out to be a trick of perspective."
    "As Honoka and I walked and walked, the school seemed to grow before my eyes."
    "The doors became large and imposing, the floors far taller than normal, everything just seemed to be super-sized in Seichou Academy."
    UNKNOWN "Aaack!"
    "Honoka and I looked down to see a pair of legs flailing over the edge of one of the planters lining the building."
    "We approached the planter just as the student extracted themselves from the planter, dusting the dirt from her long skirt."
    
    show GTS-1a at right
    with dissolve
    UNKNOWN "Oooh, darn it darn it darn it..."
    
    show BE-1c at left
    BE "Are you okay?"
    UNKNOWN "Eeep!"
    "The pale-skinned girl turned to us, looking briefly terrified.\nShe was wearing a long skirt and long-sleeved shirt."
    UNKNOWN "Uhm, yeah, sorry, I just, uhm, fell. Just, these planters are so big." 
    UNKNOWN "I can't reach the middle of the bed without crawling on the outer ones..."
    "She gestured behind her, and we could see inside the planter were several rows of vegetables, the tops of radishes and carrots and the like poking through the soil."
    "Aside from the divot where she fell, the center row of vegetables did indeed look less well-watered than the ones closest to the edge."
    
    menu:
        "That's too bad.":
            jump Choice1a
            
        "Do you need help?":
            jump Choice1b
            
label Choice1a:
    
    MC "That's too bad, hope you can figure something out."
    UNKNOWN "Yeah...If only I was a little taller, I could reach to the middle..."
    GTS "Oh, I'm sorry, I forgot entirely! My name's Yamazaki Naomi."
    "She bowed, and we returned the gesture."
    show BE-1a at left
    BE "I'm Inoue Honoka, nice to meet you. This is Kei- {i}Ahem{/i}-Hotsure Keisuke."
    MC "Nice to meet you."
    GTS "Well, I've done as much as I can today, it seems. I'll leave the rest to the groundskeepers."
    GTS "I'll see you all at orientation tomorrow."
    show BE-1b at left
    BE "Goodbye! See you around!"
    hide GTS-1a
    with dissolve
    BE "..."
    show BE-1a
    BE "...Boy, that's kind of a fancy lady to be kneeling in the dirt, don't you think?"
    jump Choice1End

label Choice1b:
    MC "Do you need help?"
    UNKNOWN "Oh, thank you, that'd be lovely. Here, let me give you the can..."
    $ GTS_Affection += 1
    "I leaned way over the planter and watered the middle row of plants, having to stretch as far as I could reach but managing to get all of them."
    GTS "Thank you so much! Oh, I'm sorry, I didn't even introduce myself properly. My name's Yamazaki Naomi."
    "She bowed, and we returned the gesture."
    show BE-1a at left
    MC "I'm Hotsure Keisuke, and this bundle of smiles here is Inoue Honoka. Nice to meet you."
    show BE-1b at left
    BE "Hi there!"
    GTS "Well, it's been a pleasure."
    GTS "Perhaps I'll see you around school?"
    MC "Yeah, sure."
    BE "Yeah! See you later!"
    hide GTS-1a
    with dissolve
    BE "..."
    show BE-1a
    BE "Well that was nice of you to help her, Kei-chan!"
    $ BE_Affection += 1
    jump Choice1End
    
label Choice1End:
    "I nod, and we continue on to the front doors of the school."
    jump AEScene

label AEScene:
    
    scene black
    with dissolve
    UNKNOWN "Mizutani!"
    "The yell made both of us jump in place, so sudden and forceful was it so soon after stepping inside."
    "When we caught our bearings{w} (And Honoka's bust stopped jiggling){w} \nwe saw the owner of the voice."
    
    scene Gate Front
    with dissolve
    "Stern and impatient-looking, the woman surveyed the front area of the school like a forewoman on a construction site, barking orders and taking notes on a clipboard."
    
    show AE-1a at Position(xpos=0.75, xanchor=0.5)
    with vpunch
    UNKNOWN "Mizutani! Quit goofing off and get over here!"
    FMG "I'm comin', I'm comin'! Geeze!"
    "Around the corner came a tanned girl somehow managing to carry a woooden bench under each arm, her short-sleeved shirt baring her defined muscles for all to see."
    
    show FMG-1a at Position (xpos=0.25, xanchor=0.5)
    with dissolve
    UNKNOWN "What took you so long?"
    FMG "I was getting two benches at once!  I thought you'd like me getting twice what ya asked!"
    UNKNOWN "Not if it takes you three times as long!"
    
    hide AE-1a
    hide FMG-1a
    show BE-1c at center
    BE "Oh boy... I feel awkward just standing here..."
    
    hide BE-1c
    show AE-1a at Position(xpos=0.75, xanchor=0.5)
    show FMG-1a at Position (xpos=0.25, xanchor=0.5)
    
    menu:
        
        "She was just trying to help...":
            jump Choice2a
            
        "You should listen to your boss, you know.":
            jump Choice2b
            
        "(Do nothing)":
            jump Choice2c

label Choice2a:
    
    MC "She was just trying to help... {w}No need to be mean."
    $ BE_Affection += 1
    $ FMG_Affection += 1
    $ AE_Affection -= 1
    UNKNOWN "Ex{i}cuse{/i} me?"
    FMG "Yeah, Matsumoto, get that stick out of your huge butt."
    "Matsumoto's face tightened and she shot daggers with her eyes."
    "It was hard not to notice the very prominent backside on her otherwise stiff and lithe frame."
    AE "My reasons for being at Seichou are not relevant to this conversation."
    AE "As class rep it's my responsibility to make sure-"
    hide AE-1a
    hide FMG-1a
    show BE-1c at center
    BE "You're class rep already? But I thought classes didn't start until tomorrow."
    show BE-1c at left with dissolve
    show AE-1a at Position(xpos=0.75, xanchor=0.5) with dissolve
    AE "Well, not yet, technically, but I'm sure I will be. I always am."
    BE "(She's awfully self-assured...)"
    AE "Are you two assigned to class 3-B? Inoue and Hotsure?"
    MC "Uh, I don't know, actually..."
    AE "I do. You're on the roster. I was just being polite."
    MC "Oh, well, okay then. Yeah, I guess?"
    AE "Get up there and make sure Aida and Nikumaru have the first-day decorations put up properly."
    AE "{i}Sigh{/i} {w}Even though I'll probably have to fix it myself."
    MC "Er, okay, sure."
    hide AE-1a with dissolve
    show BE-1a at left
    "Without another word, Matsumoto turned and began barking more orders and directions to the other students arranging the decorations."
    "Honoka and I looked at each other and headed for class 3-B."
    jump BBWScene
    
label Choice2b:
    
    MC "You should listen to your boss, you know."
    MC "If she's got a plan, going off on your own doesn't really help."
    $ FMG_Affection -= 1
    FMG "My WHAT? Matsumoto's not the boss of anyone, despite what she'll tell you."
    AE "I never claimed to be anyone's \"boss\", I just had a plan to-"
    FMG "Yeah, yeah, yeah. Listen, you two in 3-B? Might as well get up there and help."
    FMG "Whatever the princess and her pet're doing can't be as bad as having lard-butt boss you around..."
    hide FMG-1a with dissolve
    "Matsumoto shot daggers at Mizutani as she left to get more benches, then turned to regard me with a glare."
    AE "I did not need your help, but she's right. Get up to 3-B and help with the decorations and cleaning."
    "Honoka and I quickly fled the scene before the temperature dropped so low as to be freezing."
    jump BBWScene
    
label Choice2c:
    
    "I didn't want to get involved in the fight.{w} Especially after seeing Mizutani lift one of those big wooden benches under each arm."
    UNKNOWN "Look, it doesn't matter if you bring all the benches at once if I can't get them organized properly."
    UNKNOWN "One at a time lets us get each one in its place and ready for the next without-"
    FMG "All right, all right, I get it, sheesh. Don't get your panties in a bunch, Matsumoto...{w} with a butt that size, you'll never fish 'em back out."
    hide FMG-1a with dissolve
    "Matsumoto shot daggers at Mizutani with her eyes until she left to get more benches, then she turned to me in a huff."
    "My eyes snap to hers, momentarily mesmerized by just how sizable her rear was underneath the school-issue uniform."
    $ AE_Affection += 1
    AE "Hmph. Thank you for not butting in on that...{w} spectacle.{w}\nI'm Matsumoto Shiori, and you are?"
    "We introduced ourselves, and Matsumoto informed us that we were in the same class as her, class 3-B."
    "She asked us to go to our room and help two other students she'd sent earlier in the day to prepare the room, expressing some doubt as to their competence."
    hide AE-1a with dissolve
    show BE-1a at center with dissolve
    BE "You think she's ever happy with anyone? Doesn't seem the type..."
    jump BBWScene

label BBWScene:
    scene black
    with dissolve
    "We left the arguing pair behind and entered the school proper.{w} Honoka led me through the hallways with ease, until we came to one classroom in particular.."
    
    scene Classrroom Day
    with dissolve
    "So this was Classroom 3-B. I would be spending a lot of time here for the next year."
    "The first thing I noticed was that, much like the rest of the shool, the classroom seemed very big. It was much larger than any that I had been in before."
    "Whether or not this meant that there would be more students, or if this was just something that made high school different, I had no idea."
    "The next thing I noticed was that Honoka and I weren't alone in the room. Sitting across from us, at the head of the classroom, was another girl."
    show BBW-1a at left with dissolve
    "She had a round face, and bright blue eyes framed by gold colored hair.{w} It seemed as though we had a foreigner in our midst."
    "She was sitting with her feet on one of the desks, but stood up and grinned when she saw us enter."
    UNKNOWN "Oh? What have we here? I guess that Shiori told you to come up here too?"
    UNKNOWN "I have everything under control here."
    show BE-1a at right with dissolve
    BE "Who are you?"
    BBW "I'm Alice Nikumaru.{w} Charmed, I'm sure."
    "After introducing herself, Alice sat back down in her makeshift throne. Before I could open my mouth to speak, she looked past us."
    BBW "Will you hurry up already?!"
    BBW "I want to go get something to eat and I can't do that if you're slacking off!"
    "I followed Alice's gaze. I hadn't noticed at all, but there was a mousy girl in the room as well."
    hide BE-1a with dissolve
    hide BBW-1a with dissolve
    show PRG-1a at right with dissolve
    "Her hair was tied up in a pair of tails, and she was carrying a globe."
    UNKNOWN "{size=-6}Sorry!{/size}"
    show BE-1c at left
    BE "Oh wow! Sorry about that, but I totally didn't see you there!"
    show BE-1a at left
    BE "I'm Inoue Honoka! Pleased to meet ya!"
    MC "Hotsure Keisuke."
    PRG "Aida...Aida Kodama."
    hide BE-1a
    show BBW-1a at left
    BBW "Great, great.{w} Now everybody knows everybody, and Aida can finish decorating. She's almost done anyway."

    menu:
        "Well, if you've got this under control...":
            jump Choice3a
            
        "Shouldn't you be doing something too?":
            jump Choice3b
            
label Choice3a:
    
    MC "Well, if you've got this under control, I guess I'll be going then...?"
    $ BBW_Affection += 1
    $ PRG_Affection -= 1
    $ BE_Affection -= 1
    BBW "Glad to see at least someone can follow orders."
    show BE-1c at center with dissolve
    BE "{i}Kei-chan{/i}!"
    "I winced. I might not have seen Honoka for years, but I remembered that tone well enough."
    hide BE-1c with dissolve
    MC "Okay, okay. We'll help too."
    PRG "...I don't want to be a bother."
    BBW "Hmph. {w}Well, if you insist, I'm sure I can find something for you to do. {w}The sooner we're done here, the better."
    jump RMScene           
            
label Choice3b:
    
    MC "Shouldn't you be doing something too?{w}"
    $ BBW_Affection -= 1
    $ PRG_Affection += 1
    show BBW-1a at left
    BBW "I'm doing something!"
    BBW "I'm su{w}per{w}vi{w}sing!"
    hide BBW-1a with dissolve
    PRG "It's okay...{w} I don't need any help."
    MC "It's fine. We're all supposed to be working together, right?"
    PRG "T-thank you! Thank you very much!"
    jump RMScene            
     
label RMScene:
    scene Hallway
    with fade
     
    show BE-1a with dissolve
    BE "All right, well, it looks like everything's ready for tomorrow...{w} (No thanks to queenie over there.) {w} Time to get back to the dorms, I guess!"
    MC "They wouldn't happen to be co-ed, would they?"
    if BE_Affection < 0:
        show BE-1a
        BE "Uh, no, no they're not..."
        "Honoka cleared her throat and excused herself to the women's dorms."
        hide BE-1a with dissolve
    elif BE_Affection >= 0:
        show BE-1b
        BE "Oh, Kei-chan! You're such a kidder!{w} Of course not!"
        "Honoka's laugh caused her impressive bust to shake violently, which was a small consolation prize as we parted ways."
        hide BE-1b with dissolve
    
    scene School Inner
    with fade
    
    "I headed over to the boy's dormitories, seeing they were just as enlarged as the rest of the school.{w} I felt like a child, trying the doorknob that I couldn't even get my entire hand around."
    "{i}*Kunk-Kunk*{/i}"
    MC "Locked? I'm sure I had the right--"
    UNKNOWN "Who is it?!"
    MC "Aaah!"
    UNKNOWN "Who is it? Identify yourself!"
    
    menu:
        "Uh... Pizza delivery?":
            jump Choice4a
            
        "Keisuke Hotsure. I...think this is my room?":
            jump Choice4b
            
        "Don't worry, I'm from the government!":
            jump Choice4c
            
label Choice4a:
    MC "Uh...{w} Pizza delivery?"
    UNKNOWN "I didn't order any pizza!{w} Scram!"
    MC "Hahaha... It was just a joke, this is my dorm room.{w} I guess you're my roommate?"
    "The door opened a crack and a single narrowed eye looked out at me."
    UNKNOWN "This is your dorm?{w} Are you sure?"
    MC "Preeeetty sure...{w} Says right here on my paperwork, see?"
    "I pulled out my transfer documents from the top pocket of my luggage, but he snatched them away before I could even show them."
    "The door shut briefly, then opened again, the boy inside still glaring at me through one narrowed eye."
    UNKNOWN "Keisuke Hotsure...{w} Let's see some ID."
    MC "Hahaha... {w}no way, really?"
    UNKNOWN "Really."
    "Just wanting to get inside and get things over with, I sighed and handed over my ID."
    "More squinting, and then finally he opened the door all the way."
    show RM-1a with dissolve
    RM "Alright, you check out...{w} My name's Daichi Utagashi."
    $ RM_Affection -= 1
    scene Dorm Interior
    with fade
    show RM-1a
    jump RMClose
    
label Choice4b:
    MC "Keisuke Hotsure. I...{w} think this is my room?"
    "I could hear movement behind the door, like someone searching for something.{w} After a bit, the door opened a crack, a single narrowed eye looking me up and down."
    UNKNOWN "Hotsure, huh?{w} Let's see some ID."
    MC "Hahaha... {w}no way, really?"
    UNKNOWN "Really."
    "Just wanting to get inside and get things over with, I sighed and handed over my ID."
    "More squinting, and then finally he opened the door all the way."
    show RM-1a with dissolve
    MC "Alright, you check out...{w} My name's Daichi Utagashi.{w} Come in, I don't like leaving the door open."
    scene Dorm Interior
    with fade
    show RM-1a
    jump RMClose
    
label Choice4c:
    MC "Don't worry, I'm from the government!"
    "I thought my fake-authoritative voice would have been worth a laugh, but instead there was silence.{w} I knocked again, tried the knob, called out a few times, but there was no answer."
    "I put my ear against the door and could hear movement, so I moved over to one of the windows and took a peek in...{w} only to see the mystery occupant hurling his bags out the opposite window?!"
    scene Dorm Exterior
    with fade
    "I left my luggage by the door and ran around the dorm, coming around the other side just in time to see him struggling out the window."
    show RM-1b with vpunch
    UNKNOWN "Aaah! D-Damn you!"
    RM "Daichi Utagashi isn't going without a fight!"
    "Daichi tried to go back inside, but he had already squirmed too far out to get back through the window."
    RM "Rrrgh!{w} Hrff!{w} Nnngh...{w} Dammit, I'm s-stuck!"
    MC "Will you calm down for a second and tell me what's wrong???"
    RM "Don't play coy with me!{w} You're one of them!"
    MC "\"Them\" who?"
    RM "The government! You're here to monitor me, drag me off to some secret prison!{w} Put electrodes in my brain! Read my Doujins!"
    MC "It was just a joke!{w} I'm Keisuke Hotsura, I just got here, this is supposed to be my dorm!"
    "Daichi twisted around to look at me, his eyes narrowed."
    show RM-1c
    RM "...If you really were one of them, I suppose you would have grabbed the evidence while I was helpless.{w} Help me back in and I'll open the door."
    MCT "Am I really going to have to live with this guy?"
    scene Dorm Interior
    with fade
    "After helping Daichi back through the open window and handing his bags to him {w}(He wouldn't let me carry them out of his sight){w} then checking my admission papers and ID, he finally unlocked the door and let me in."
    show RM-1d
    RM "Don't get any funny ideas, 'Keisuke Hotsure'. I've got my eye on you..."
    $ RM_Affection -= 3
    jump RMClose

label RMClose:
    "When I finally got inside, it was obvious Daichi had claimed his half of the room.{w} Half the furniture had been crammed into one corner of the room, with blankets and sheets erected into a kind of tent over his desk and dresser."
    show RM-1a
    MC "Er, so, do you want to--"
    RM "Do you know why you're here?"
    MC "Er, what?"
    RM "Why you're here, at this school?"
    MC "Well, I got the letter..."
    RM "Right after your health exam, right?"
    MC "Yeah..."
    RM "Hmph. Just as I thought."
    MCT "???"
    show RM-1d
    RM "Haven't you ever seen those people on the news?{w} The giants over teen feet tall,{w} the gravure idols with 40kg breasts,{w} all the record holders for biggest this and longest that?"
    "Thinking back on it, I had seen some reports, starting when I was a little kid."
    "It wasn't often, but every now and then there'd be some picture or other of giant-sized men and women, always Japanese."
    RM "If you look into the histories and records of all these people, one thing is common to all of them--{w} they {i}ALL{/i} went to school at Seichou Academy!"
    MC "So, what are you saying?"
    show RM-1c
    RM "I'm saying the government brings certain students here and--{w} and does {i}something{/i} to them!"
    show RM-1b
    RM "This kind of growth isn't natural,{w} it's statistically impossible for all of these one-in-a-million conditions to keep happening {i}just{/i} to Japanese school-age teens!"
    "I sat down on my bed, lost in thought.{w} Daichi certainly seemed to have a few screws loose, but then again,{w} why {i}had{/i} my sister and I been sent to this school with so few details?"
    "I had just accepted it as some new schooling program, like the papers had said, but now?"
    "I never paid much attention to the news, but if every one of those reports and articles over the years could be traced back to Seichou Academy,{w} that was definitely something to wonder about."
    scene black
    with dissolve
    MCT "What have my sister and I gotten ourselves into...?"
    
    show black
    jump End
    
    #http://growthacademy.socialparody.com
    
label End:
    centered "You have reached the end of this demo of Growth Academy."
    centered "If you'd like to keep up to date with the game's development or contribute and make it a reality, please visit us at: \n http://growthacademy.socialparody.com/main"
    centered "During each scene, an \"affection\" score for each of the girls were recorded based on your choices."
    centered "In the full game, they will be very important in where the story will lead; including some exclusive plot events and the chance for the girl to fall in love with you."
    centered "For now, they're just plain numbers; here's how you did!"
    centered "Inoue Honoka: [BE_Affection] \n Yamazaki Naomi: [GTS_Affection] \n Mizutani Akira: [FMG_Affection] \n Matsumoto Shiori: [AE_Affection] \n Alice Nikumaru: [BBW_Affection] \n Kodama Aida: [PRG_Affection] \n Daichi Utagashi: [RM_Affection]"
    
    centered "Thanks for playing!"

    return   # Complete Game and Return to Main Menu; End Game conditions can be taken into account for potential rewards (such as exclusive images or the ability to view full-credits for having completed the game).
