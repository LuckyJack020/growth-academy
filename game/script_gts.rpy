define GTS = Character('Naomi', color="#66FF33")
define Vendor = Character('Vendor', color="#FFFFFF")
define LittleGirl = Character('Little Girl', color="#FF91DC")
define Ryoko = Character('Ryoko', color="#FF91DC")
define Minori = Character('Minori', color="#FF91DC")
define Fumika = Character('Fumika', color="#FF91DC")

image GTS neutral = DynamicImage("Graphics/GTS/[globalsize]/neutral.png")
image GTS happy = DynamicImage("Graphics/GTS/[globalsize]/happy.png")
image GTS sad = DynamicImage("Graphics/GTS/[globalsize]/sad.png")
image GTS surprised = DynamicImage("Graphics/GTS/[globalsize]/surprised.png")
image GTS angry = DynamicImage("Graphics/GTS/[globalsize]/angry.png")
image GTS aroused = DynamicImage("Graphics/GTS/[globalsize]/aroused.png")
image GTS embarrassed = DynamicImage("Graphics/GTS/[globalsize]/embarrassed.png")

image Ryoko neutral = "Graphics/minor/ryoko-neutral.png"
image Ryoko happy = "Graphics/minor/ryoko-happy.png"
image Ryoko annoyed = "Graphics/minor/ryoko-neutral.png"
image Ryoko camera = "Graphics/minor/ryoko-camera.png"
image Ryoko surprised = "Graphics/minor/ryoko-surprised.png"

image Minori neutral = "Graphics/minor/minori-neutral.png"
image Minori happy = "Graphics/minor/minori-happy.png"
image Minori embarrassed = "Graphics/minor/minori-neutral.png"

image Dorm GTS = "Graphics/ui/bg/dorminterior.png"

init 2 python:    
    #Core
    eventlibrary['GTS001'] = {"name": "Girl in the Garden", "girls": ["GTS"], "type": EventTypeEnum.CORE,                  "location": "schoolplanter",    "priority": PrioEnum.NONE, "next": "GTS002", "obsflags": [],         "conditions": []}
    eventlibrary['GTS002'] = {"name": "Planting Seeds", "girls": ["GTS"], "type": EventTypeEnum.CORE,                      "location": "schoolplanter",    "priority": PrioEnum.NONE, "next": "GTS006", "obsflags": [],         "conditions": []}
    eventlibrary['GTS006'] = {"name": "Puppy Love", "girls": ["GTS"], "type": EventTypeEnum.CORE,                          "location": "schoolfront",      "priority": PrioEnum.NONE, "next": "GTS007", "obsflags": [],         "conditions": []}
    eventlibrary['GTS007'] = {"name": "Homesick", "girls": ["GTS"], "type": EventTypeEnum.CORE,                            "location": "schoolplanter",    "priority": PrioEnum.NONE, "next": "GTS008", "obsflags": [],         "conditions": []}
    eventlibrary['GTS008'] = {"name": "Secret Garden", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "roof",             "priority": PrioEnum.NONE, "next": "GTS009", "obsflags": [],         "conditions": []}
    eventlibrary['GTS009'] = {"name": "A tale of Fish and Yukatas", "girls": ["GTS", "BE"], "type": EventTypeEnum.CORE,    "location": "festival",         "priority": PrioEnum.NONE, "next": "GTS011b", "obsflags": [],        "conditions": []}
    eventlibrary['GTS011'] = {"name": "The Director", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "dormexterior",     "priority": PrioEnum.NONE, "next": "GTS014", "obsflags": [],         "conditions": [[ConditionEnum.FLAG, "GTS011_unlock"]]}
    eventlibrary['GTS011b'] = {"name": "The Director", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "dormexterior",     "priority": PrioEnum.NONE, "next": "GTS014", "obsflags": [],         "conditions": [[ConditionEnum.NOFLAG, "GTS011_unlock"]]}
    eventlibrary['GTS014'] = {"name": "A Con or Pro Fession?", "girls": ["GTS"], "type": EventTypeEnum.CORE,               "location": "classroom",        "priority": PrioEnum.NONE, "next": "GTS015", "obsflags": [],         "conditions": []}
    eventlibrary['GTS015'] = {"name": "Decisions, Decisions", "girls": ["GTS"], "type": EventTypeEnum.CORE,                "location": "dormexterior",     "priority": PrioEnum.NONE, "next": "GTS018", "obsflags": [],         "conditions": []}
    eventlibrary['GTS018'] = {"name": "Slam Dunk", "girls": ["GTS"], "type": EventTypeEnum.CORE,                           "location": "schoolexterior",   "priority": PrioEnum.NONE, "next": "GTS019", "obsflags": [],         "conditions": []}
    eventlibrary['GTS019'] = {"name": "All in the Wrist", "girls": ["GTS"], "type": EventTypeEnum.CORE,                    "location": "schoolplanter",    "priority": PrioEnum.NONE, "next": "GTS020", "obsflags": [],         "conditions": []}
    eventlibrary['GTS020'] = {"name": "Confessions of a Lonely Heart", "girls": ["GTS"], "type": EventTypeEnum.CORE,       "location": "roof",             "priority": PrioEnum.NONE, "next": "GTS021", "obsflags": [],         "conditions": []}
    eventlibrary['GTS021'] = {"name": "Taking a Breather", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "schoolplanter",    "priority": PrioEnum.NONE, "next": "GTS025", "obsflags": [],         "conditions": []}
    eventlibrary['GTS025'] = {"name": "Would it be Okay...?", "girls": ["GTS"], "type": EventTypeEnum.CORE,                "location": "campuscenter",     "priority": PrioEnum.NONE, "next": "GTS026", "obsflags": [],         "conditions": []}
    eventlibrary['GTS028T'] = {"name": "Art of Film", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "schoolplanter",    "priority": PrioEnum.NONE, "next": "", "obsflags": [],               "conditions": [[ConditionEnum.FLAG, "GTS015_movie"]]}
    eventlibrary['GTS030'] = {"name": "Naomi end", "girls": ["GTS"], "type": EventTypeEnum.CORE,                           "location": "library",          "priority": PrioEnum.NONE, "next": "", "obsflags": [],               "conditions": []}
    
    #Optional
    eventlibrary['GTS003'] = {"name": "Itadakimasu", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                     "location": "cafeteria",        "priority": PrioEnum.NONE, "obsflags": [],                           "conditions": []}
    eventlibrary['GTS004'] = {"name": "Study Buddy", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                     "location": "library",          "priority": PrioEnum.NONE, "obsflags": [],                           "conditions": []}
    eventlibrary['GTS012'] = {"name": "Tea?", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                            "location": "schoolplanter",    "priority": PrioEnum.NONE, "obsflags": [],                           "conditions": [[ConditionEnum.EVENT, "GTS011"]]}
    eventlibrary['GTS016'] = {"name": "To Bee or not to Bee", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,            "location": "schoolplanter",    "priority": PrioEnum.NONE, "obsflags": [],                           "conditions": []}
    eventlibrary['GTS017'] = {"name": "Getting Dirty", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                   "location": "schoolplanter",    "priority": PrioEnum.NONE, "obsflags": [],                           "conditions": []}
    
    eventlibrary['GTS005'] = {"name": "A Growing Issue", "girls": ["GTS"], "type": EventTypeEnum.OPTIONALCORE,             "location": "schoolplanter",    "priority": PrioEnum.GIRL, "obsflags": ["aftertest"],                "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['GTS010'] = {"name": "A head above the class", "girls": ["GTS"], "type": EventTypeEnum.OPTIONALCORE,      "location": "classroom",        "priority": PrioEnum.GIRL, "obsflags": ["aftersize2"],               "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    
label GTS001:
    $setProgress("GTS", "GTS002")
    scene black with fade
    "The words from Tashi-Sensei stayed with me long after class had concluded. I just wasn't sure how to properly process what we were told."
    "What Daichi had told me earlier was starting to resonate more, and I began to wonder if perhaps others knew about the purpose of this school before they were enrolled."
    scene School Planter with fade
    play music Peaceful
    "I hadn't realized how long I was lost in my own thoughts until I finally noticed my surroundings; I was at the school's garden."
    "It was nice here, the cool breeze along with the sound of it blowing through the leaves had a sort of calming effect. I stood there for a few moments longer until a figure walked beside me, catching me by surprise."
    show GTS neutral:
        xpos 0.99 xanchor 0.0 yalign 1.0
        linear 5.0 xpos 0.5 xanchor 0.5
    MC "Hm? Oh, Yamazaki-san. Sorry, I wasn't aware you were here."
    GTS "It's all right, Hotsure-san. I hope I didn't disturb you."
    "She stood there, smiling ever so slightly, the flow of wind causing her long hair to dance tenderly until I decided to break the silence."
    MC "Not at all, I was just thinking. Were you doing the same?"
    GTS "Yes, I was merely hoping to spend a little time here. Reflect on my thoughts about the day's events thus far."
    MC "I see... Were you also possibly thinking about what Tashi-sensei told us earlier?"
    GTS "A little yes, I think most of the students are. Were you as well?"
    MC "Yeah I was. It really came out of left field, so it's been lingering in my brain all day."
    show GTS neutral at center
    menu:
        "What do you think about it?":
            jump GTS001_c1
        "I'm curious about what changes I might go through...":
            jump GTS001_c2
        "I'm concerned about what that might mean for my younger sister, honestly.":
            jump GTS001_c3
            
label GTS001_c1:
    MC "What do you think about it?"
    GTS "It's a little concerning I will admit; however, I think some of those feelings come from the sudden nature in which we were told."
    GTS "I'm sure if we take more time to process it and reflect on it, the situation won't feel as frightening as it possibly does for some."
    extend " Thank you for asking, though."
    MC "No problem, we're in this together after all, right?"
    GTS "An interesting way to put it, but indeed I would say so."
    jump GTS001_after

label GTS001_c2:
    MC "I'm curious about what changes I might go through..."
    GTS "It's good to see you're looking at the news with curiosity rather than concern. Without knowing all the facts, some may worry needlessly about it."
    MC "I suppose you're right. But I wonder how the school figures out what we'll end up having."
    GTS "I'm sure they have methods to tell what will be changing in us, though with some students it may be more obvious than others."
    show GTS embarrassed
    GTS "Oh, I'm sorry! That sounded rather rude didn't it? I don't mean to judge any of the other students."
    MC "Heh, it's okay Yamazaki-san, I can tell you're not the type to do that."
    show GTS neutral
    GTS "Thank goodness, I wouldn't want to start making the wrong impressions on the first day of school."
    jump GTS001_after

label GTS001_c3:
    MC "I'm concerned about what that might mean for my younger sister honestly."
    $setAffection("GTS", 1)
    GTS "Oh? You have a younger sister, Hotsure-san?"
    MC "Yeah, she's going to school here, too. I'm just thinking about what Sensei said, about how sometimes siblings are transferred to this school simply because of the results of the other. I'm sure I can cope with whatever might happen to me, but I'm worried about her."
    MC "I just don't want her to go through something that might hurt her."
    GTS "It's only natural to worry as the older sibling Hotsure-san, but you mustn't let it concern you too much. There's no way to know for certain at the moment, and as such it may be best to be hopeful and keep your chin up."
    MC "Yeah, I guess that's true. Sorry for sounding like a mother hen here."
    GTS "There's no need to apologize for it. I know I'm very much the same with my own sister."
    MC "You have a sister too?"
    GTS "Yes, she's a couple years younger than me, so just know that you're not the only one who can come off as a mother hen at times."
    jump GTS001_after

label GTS001_after:
    "She gave a soft chuckle and kept her warm smile that soothed my worries."
    "I guess she must have noticed me staring, because she soon chimed in."
    show GTS embarrassed
    GTS "It's quite rude to stare."
    MC "O-Oh! Sorry... I was just thinking again, haha... So, are you going to be doing anything else later today?"
    show GTS neutral
    "She placed a finger on her lip as she thought about her plans for the evening, before finally replying."
    GTS "Well, I had planned to return to my dorm room so I could tell my family about how my first day went."
    GTS "However, I do plan to explore the garden later this evening. There's a surprisingly large variety of flowers here. At least, more than I had expected, so I want to make a list of what's here and maybe ask the groundskeeper about where they obtained the seeds for them."
    MC "Oh, I see; I won't hold you up, then. I should probably do the same myself, really, I'm sure my family would love to hear about how my day went as well. I'll see you around, Yamazaki-san."
    GTS "Farewell, Hotsure-san, I hope the rest of your day goes well. Do try to visit the garden every so often, you'll be surprised how much good can come from resting in a garden for a few moments."
    MC "Heh, I might take you up on that advice. Later, Yamazaki-san."
    "She gave me a small bow before I departed."
    jump daymenu

label GTS002:
    $setTimeFlag("testday")
    $setProgress("GTS", "GTS006")
    scene School Planter with fade
    "I always found the sky to have quite the alluring palette around late afternoon. Clouds coated in degrees of red that ranged from rose color to pink and even orange and yellow. And while I normally didn't find myself staring up at the sky, it was simply something I couldn't resist as I stepped into the school's garden once more."
    "The breeze had become cooler, but still flowed with a sense of gentleness to it, making some pink colored flowers dance before me. In the distance, I heard a faint voice, and as I turned to look I spied Naomi giving a gracious bow to who I assumed was the gardener."
    show GTS neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    play music Sunset
    MC "Yo Yamazaki-san!"
    "I lifted one arm up to give a slight wave. This seemed to surprise her, as she jumped a little and looked back towards me. Giving a small nod, she walked over with a few small bags held against her bust by her arm."
    show GTS embarrassed at Position(xpos=0.5), Transform(xzoom=1) with dissolve
    GTS "Hello Hotsure-san, you startled me a little there."
    MC "Heh, sorry. I just wanted to make sure you heard me. I see you talked to the gardener."
    show GTS neutral
    GTS "I did yes. I was just asking about the flowers and before we knew it we got wrapped up in a rather long conversation about them. He even gave me some seeds to plant."
    "She shifted her arm a little to draw my attention to the three bags she was carrying."
    menu:
        "Oh, that's cool. How did the rest of your day go?":
            jump GTS002_c1
        "Really? That was cool of him. What kind are they?":
            jump GTS002_c2

label GTS002_c1:
    MC "Oh, that's cool. How did the rest of your day go?"
    GTS "Hm? Oh, the rest of my day was rather peaceful. I spoke with my family as I mentioned earlier and they seemed rather happy to hear from me."
    MC "That's good to hear, did you happen to mention what you thought about the news we got earlier?"
    "She was silent for a moment as if reflecting on that question before she answered me."
    GTS "No, I didn't. I don't see a reason to mention it to them yet. Without any knowledge, all it'd accomplish is make them worry about me needlessly."
    GTS "I will be sure to discuss my feelings about it to them when we learn more about it ourselves and I know exactly what to expect."
    MC "Yeah I guess that's a good way to go about it... So, did you do anything else?"
    "She shook her head softly."
    GTS "No, not much else really. Basically, just made sure everything was completely unpacked and organized. Then I came here, and well, you know where that part leads."
    jump GTS002_after
    
label GTS002_c2:
    $setAffection("GTS", 2)
    $setSkill("Art", 1)
    $setFlag("GTS008_flowers")
    MC "Really? That was cool of him. What kind are they?"
    "Her eyes brightened ever so slightly at that question as her smile grew a little larger."
    show GTS happy
    GTS "Indeed, it was rather nice of him. As for the flowers themselves, these ones are Bluebells, a lovely plant with quite the bold color. They're known to symbolize gratefulness."
    "She handed the bag to me, allowing me to see the blue, bell-like shape they had on the cover."
    GTS "Now this breed here is the Azalea, which you might have seen here at the garden."
    "She pointed over to the pink flowers I had seen when I first entered the garden, the second look allowing me to notice the purplish patterns within the petals of the flower."
    GTS "They're popular here in Japan, and even have a flower festival which showcases them each year. They're known to symbolize patience and modesty."
    "She handed me this bag as well, as I soon found myself carrying her flowers for her."
    GTS "Now these last ones may seem rather plain due to their simple color, but you'll be surprised the amount of color variety you'll find with Anemones. Though the white ones are the ones you'll most commonly find here in Japan."
    GTS "Their name is Greek, meaning 'Daughter of the Wind,' and they represent sincerity."
    "As she handed me the last bag, which displayed white, five-petaled flowers I could see her smiling warmly as she finished explaining."
    MC "Heh, I can tell you really have a thing for flowers."
    "Her smiled quickly vanished and instead a light blush formed across her cheeks."
    show GTS embarrassed
    GTS "O-oh yes, indeed I do. Sorry for getting rather carried away there. I didn't mean to just ramble on like that. I surely hope you don't mind."
    MC "Not at all, it's nice to learn a little bit about you, really. I also admit it was interesting to learn a bit about these flowers as well, I wasn't aware they have hidden symbolic meanings."
    show GTS neutral
    GTS "They do yes, but I wouldn't want to take up more of your time chattering about my interests."
    jump GTS002_after
    
label GTS002_after:
    GTS "How did the rest of your afternoon go, if you don't mind my asking?"
    MC "Taking what we learned about ourselves earlier aside, the rest of my afternoon was actually pretty good. I spoke with my family and told them I'm fine."
    MC "I then took some time to learn a bit more about the school, and found out there are several sports clubs. I might give them a look and see if I can join in the future."
    "She nodded her head as I spoke to her, taking in everything I was saying attentively. It felt rather nice honestly, knowing that she was truly listening to me as she kept eye contact with me during the entirety of my small ramble."
    GTS "What sport are you interested in, Hotsure-san?"
    MC "Oh, I'm rather interested in Soccer. I might give it a shot later this year, if my condition doesn't hinder it in some way."
    "I chuckled lightly, kind of realizing that we couldn't plan our futures for the moment."
    "Without any knowledge about what might happen to us, everything was up in the air. I pushed that thought to the back of my mind though."
    GTS "Hopefully you'll be able to do so, Hotsure-san. Soccer has always seemed like a rather enjoyable sport, a lot of endurance needed so it's good exercise."
    "She gave me another soft, warm smile that made me smile in return as I scratched the back of my head."
    MC "Heh, Thanks. Well, it's getting rather late, and I don't want to keep you from any plans you possibly have with your flowers, so I think I'll be heading off now. Before I go, though, do you need any help with those?"
    "I pointed to the small bags of seeds she had with her. This caused her to give the slightest of giggles as she shook her head lightly."
    GTS "No, I'm okay, thank you. It was nice speaking with you though, Hotsure-san. Hopefully we'll talk again soon."
    MC "Yeah, hopefully. I'll catch you later, Yamazaki-san."
    GTS "Have a pleasant evening, Hotsure-san."
    "She replied before once again giving me a light bow, yet this time it was her who left first. I couldn't help but smile at the small conversation we had, slightly curious about where I might bump into her again."
    jump daymenu

label GTS003:
    scene Cafeteria with fade
    play music Schoolday
    "The morning found itself to be quite the chaotic time, as many students rushed down the corridors to make it to the cafeteria in time to beat the breakfast rush."
    "When I finally arrived to the cafeteria, I saw that it was surprisingly calmer than what was transpiring throughout the hallways. I got in line behind a few other students who were getting their breakfast."
    "I will admit I was rather surprised by what I saw. There were trays upon trays of warm food prepared for us, a lot of which looked just heavenly to the eyes and assuredly tasted as wonderful."
    "Not wishing to hold up the line though, I quickly grabbed what I felt would be a decent quick breakfast, getting some steamed rice, a rolled omelette, and a small bowl of miso soup. I thanked the cooks before searching for a place to sit."
    "There were a good amount of unfamiliar faces among those sitting at various tables, but one face was rather familiar. Sitting down with a slight smile, I spoke to my neighbor."
    show GTS neutral at center with dissolve
    MC "Hey there, Yamazaki-san. Nice to see someone I know here."
    GTS "Good morning, Hotsure-san. I hope you're having a pleasant day so far."
    "Her hands gently repositioned her utensils and napkin in an extremely orderly fashion before wiping her hands off with a moist towelette. She then looked at me, as if to give me a hint, until I realized what I'd forgotten."
    MC "Oh! Uh, itadakimasu."
    show GTS happy
    GTS "Itadakimasu."
    MC "Yeah it's been a pretty good morning so far, I managed to wake early so it gave me just the right amount of time to fully wake up, which is a pretty good start of the day in my opinion."
    MC "Thankfully since I woke up so early it allowed me to shower without feeling rushed."
    "She gave a small smile in response before picking up her chopsticks. Her hand softly slid her hair back as she picked up some cooked vegetables to eat."
    "This let me notice that her other bang was currently held back by a flower shaped hair clip. I had no idea what type of flower it was, only knowing that it had 5 white petals in a sort of star configuration."
    MC "How was the start of your day, if you don't mind me asking?"
    "Naomi perked up slightly as I asked my question, taking her napkin to delicately wipe her lips and properly placing it back in place before answering."
    show GTS neutral
    GTS "Myself? Well, I woke up rather early as well, and took the time to properly make my bed. I then showered and prepared myself for the rest of the day. Things like properly combing my hair, getting everything organized, and planning out my schedule for the day."
    GTS "I think it's good to take the time in the morning to plan the day, it allows you to optimize the time you spend as well as get your brain working early on in the day."
    MC "I can see that, yeah. Gets the juices flowing and your mind ready for more work."
    "She gave me another small smile as she learned that I agreed with her before she went back to have another piece of her meal."
    "This time I noticed how she used her chopsticks to take an almost perfectly rectangular piece out of some of her grilled fish, and then carefully took some steamed rice and place it atop before eating both."
    "Her movements seemed so precise and slightly rigid that it was slightly captivating as I never seen someone eat so strictly."
    menu:
        "That's a cute hairclip, though I'm not sure what type of flower that is. Do you know what kind is it?":
            jump GTS003_c1
        "I mean no offense, but you have a very interesting way of eating.":
            jump GTS003_c2

label GTS003_c1:
    $setAffection("GTS", 2)
    $setSkill("Art", 1)
    $setFlag("GTS008_flowers")
    show GTS embarrassed at center, Transform(xzoom=-1)
    "For the briefest of moments I could see Naomi's cheeks flash a slight crimson in what I assumed was embarrassment as her hand went to touch the accessory. She looked away for a second, but returned her eyes back to mine and retrieved that small smile she had before."
    show GTS embarrassed at center, Transform(xzoom=1)
    GTS "Oh, why thank you so much. It's just a little something I decided to add to the rest of my attire for today. I have a bit of a collection of them, various species and things of that nature."
    MC "Well, I think it suits you rather well."
    GTS "Thank you..."
    show GTS neutral
    GTS "As for your question, this flower is a Jasmine, which tend to confuse some people, since they happen to look slightly generic."
    MC "I will admit, it does look like what most people picture as a flower in their heads."
    GTS "Well, Jasmine does come in other forms, like the Grand Duke of Tuscany variant, which almost resembles a white rose, to those that look much like the one in my hair."
    GTS "China even uses it as an ingredient for their teas."
    MC "Really? Which one?"
    GTS "...Jasmine tea."
    MC "Oh... I guess I should have put that together."
    "I scratched the back of my head, feeling a little silly now, but she didn't seem to mind my mental trip, simply answering me as if it were any other question."
    GTS "They're known to symbolize friendliness and gracefulness."
    MC "Seems like it suits you rather well, then."
    "This caused her blush to return once more, as her eye contact finally broke to look at her food."
    jump GTS003_after

label GTS003_c2:
    $setAffection("GTS", -1)
    "Her body stiffened up slightly as I brought mention towards her table etiquette, and she looked me in the eyes."
    show GTS embarrassed
    GTS "How... do you mean?"
    MC "I just mean that the way you conduct yourself, it's very precise but also very formal."
    show GTS neutral
    GTS "Well it was how I was raised. It's important for one to keep proper posture and etiquette when eating. You don't want to come off as unintentionally rude, after all."
    MC "Heh, well you don't have to worry so much about being so formal around me. You can relax."
    GTS "I see, I'll keep that in mind, though it's okay, I would like to move past the subject."
    MC "Heh... yeah, okay. Sorry about that."
    GTS "It's fine."
    jump GTS003_after

label GTS003_after:
    "We ate for a few moments in silence after that. It was rather nice to have someone to eat with, even if we weren't having much of a conversation at the time. As we finished I had decided to ask Naomi something."
    MC "So, is there any particular subject you're looking forward to this year?"
    GTS "I think science should be rather fun this year, how about yourself?"
    MC "I'm not too sure yet, but I can tell you already that I'm dreading the thought of math."
    GTS "Not much for math?"
    MC "I'm horrible at math, but maybe this year I'll get lucky."
    "She gave me a small nod and smile as she stood up from the table, collecting her tray."
    GTS "I wish you good luck then, Hotsure-san."
    MC "Why thank you ma'am, and I wish you luck with science."
    "She gave a small bow and walked off as I gathered all my things."
    jump daymenu
    
label GTS004:
    scene Library with fade
    play music Peaceful
    "The sun shone highly in the sky as the middle of the day came by, its rays seeping through the many windows that surrounded the vast two-story room. I was honestly a little surprised to see so many people using the campus library."
    "To its credit, both floors seemed absolutely packed with shelves upon shelves of books. Which in turn would make one aisle look like the splitting of the red sea but with books as opposed to water."
    "This didn't mean that every part of the library was stuck in the past, as there were a series of smaller rooms that had lines of computers for more convenient research and study."
    "Something else that was rather clear was just the amount of space found between each shelf, as it seemed capable of easily fitting six people across the width of the aisle."
    "The reason for this was easy to put together, but it did leave me with the thought of just how large some of the students might become if this was the norm for the school."
    "As I walked among the shelves in search of the right book needed for my Contemporary Society course, I spotted Naomi at a nearby table."
    "Naomi was seated with her focus entirely on her book, seeming somewhat perplexed by what she was reading. Unable to resist, I strolled over to Naomi."
    menu:
        "Hey there!":
            jump GTS004_c1
        "(Read over her shoulder)":
            jump GTS004_c2

label GTS004_c1:
    $setAffection("GTS", -1)
    show GTS neutral
    MC "Hey there!"
    "This caused Naomi to jump and cup her chest as she was yanked out of her studying. She looked up at me and sighed slightly in relief, though her expression showed she hadn't taken my joke too well."
    show GTS angry
    GTS "Please don't do that."
    "She said the words politely, but the inflection in her voice was laced with annoyance as she recomposed herself. Her eyes never left mine as I scratched the back of my head and took a seat across from her."
    MC "Sorry, sorry, I just couldn't resist a little startle."
    show GTS neutral
    "I let out a small chuckle which caused her to narrow her eyes a little but she eventually seemed to settle down as she looked at the book I had placed down. I had an opportunity to see what she was reading herself, seeing the symbols that showed what appeared to be another language."
    jump GTS004_after

label GTS004_c2:
    "I peeked over her shoulder to see what she was reading, letting her see me."
    show GTS neutral with dissolve
    GTS "Hello there Hotsure-san."
    MC "Hi. Sorry, I was just curious about what you were reading."
    GTS "That's okay, though please ask next time."
    "I took a seat across from her. I had an opportunity to see what she was reading, seeing the symbols that showed what appeared to be another language."
    MC "Will do."
    jump GTS004_after

label GTS004_after:
    MC "What language is that? English?"
    "She gave me a nod in response and shifted her book slightly so I'd be able to see it better."
    GTS "I'm trying to get a bit more studying of it done on my free time. Just get a better understanding of it for myself."
    MC "That's neat, are you planning to visit the United States in the future?"
    GTS "I can't be certain truthfully, but I think it's best to be prepared for it in case it ever happens. It's also a good skill to have if your work might require it, or if you might have international guests."
    MC "Heh, that's quite the foresight to have. I barely even think about what I'll be doing a month from now. Hey, if you manage to make it work, though, that's one massive advantage you'll have over others in the job market, so good luck!"
    GTS "Thank you."
    "She showed hints of a smile as I wished her luck."
    MC "How well did you take in what we learned in homeroom today?"
    "She gave the smallest sigh as she reached to her back and retrieved a rather large book."
    GTS "Unfortunately, not as well. Science is proving that it might be harder than I originally thought."
    GTS "As you know, our professor seems rather adamant that we start of the year sooner rather than later, and regrettably the crash course we were given made it a little difficult to retain all the information we went over."
    MC "Well I don't think we're expected to get everything memorized from the start. I'm sure it'll ease up a bit in the next few days."
    GTS "We were told that we'd be given a quiz at the end of this week so I can't afford to fall behind. I'll just have to shift my focus a bit, keep my English studies to an hour while devoting more of the afternoon to this."
    MC "Heh... Why not just get a study partner? I remember when I was younger one of my teachers told me that the best way to learn and retain knowledge was to teach others."
    MC "So, if you have someone who you can bounce information to and maybe even quiz, then you'll understand it better. After all, if you're making the quizzes then that means you have the answers already."
    "She placed her hand on her chin as she seemed to consider that option."
    GTS "I'm not sure... I'd hate to impose on anyone and add to their studies."
    MC "Well then... I volunteer!"
    "She quickly put a finger over her lips just as I remembered we were in the library. Chuckling nervously, I decided to repeat myself in a more subdued fashion."
    MC "Oops. But yeah, I'll be glad to help you out."
    show GTS embarrassed
    GTS "Are you sure? I feel bad asking you to take time out of your schedule simply to help me."
    MC "Don't worry, it's fine. Plus, I get to learn more so it'll help me out a lot too."
    show GTS neutral
    GTS "Hmm. Oh, how about I help you with one of our other subjects then? Is there any you think will be an issue?"
    MC "Math. Haha, it's going to be math, I can already tell that's going to be a disaster for me this year."
    "She gave a light giggle, covering her mouth ever so slightly."
    GTS "Well, that's something I know I can help you with. Very well then, I accept your help, and am pleased you accept mine as well."
    "She extended her hand for me to shake to solidify our agreement. Taking her hand into mine, I gave her a smile and shook."
    MC "Glad to be of assistance, study partner. Let's get this done!"
    Student1 "Sssh!"
    "We both tensed up as someone at another table once again reminded me of my surroundings. Naomi was blushing slightly, but neither of us could stop a small giggle from slipping out as we started working more quietly."
    jump daymenu

label GTS005:
    $setTimeFlag("aftertest")
    "I wandered about the campus for quite some time after visiting the nurse, the news of my particular condition having left me with a feeling of uncertainty. As I walked, my hand would occasionally reach up to touch the tip of my bangs as I wondered just how quickly they might change."
    scene School Planter with fade
    play music Peaceful
    "As I stepped past the double doors and into the garden, my eyes shut from the blast of sunlight that I was exposed to. After a few seconds my eyes readjusted and I saw Naomi's form kneeling in front of a patch of flowers. Calmly walking over, my footsteps on the path nevertheless alerted her to my presence, and she looked back at me and gave a soft wave."
    show GTS neutral at center with dissolve
    GTS "Hello there, Hotsure-san."
    MC "Hey Yamazaki-san. How are you doing?"
    "She stood up and dusted off her legs before turning her full attention to me."
    GTS "I'm doing well. I came here to do some reflecting and thinking. I feel rather inattentive though, I somehow had missed this small patch of Botan flowers here."
    "I looked past her to see the pink plants in the flower patch behind her."
    MC "'Botans', huh? I thought they were roses, honestly."
    "She gave me a soft smile, but shook her head slightly."
    GTS "It is a common mistake, they do have a somewhat similar appearance so I can see how you'd make that assumption. One way to tell the difference is that botans have a lot more petals, and because of that are a bit puffier-looking."
    GTS "I like to think of them as wedding gowns personally, the petals being the ends of the gown that swirl towards the middle, which is the bride."
    MC "That's quite the romantic way to look at it."
    "Naomi's cheeks reddened a bit as she tried to move past that statement."
    show GTS embarrassed
    GTS "Apologies, I didn't ask how you were doing? I can never seem to stop talking about flowers with you, it seems."
    menu:
        "Hey, you have a passion for it, I can't fault you for that.":
            jump GTS005_c1
        "I'm doing okay, thinking about the results from the test.":
            jump GTS005_c2

label GTS005_c1:
    $setAffection("GTS", 2)
    $setFlag("GTS008_flowers")
    MC "Hey, you have a passion for it, I can't fault you for that."
    show GTS neutral
    GTS "Thank you, I just don't wish to come off as annoying or disinterested in talking about you."
    MC "Heh, you worry too much about that. It's fine to talk about what you like, that's what friends do."
    show GTS embarrassed
    GTS "I... I see. Thank you again."
    MC "What else can you tell me about Botans?"
    show GTS neutral
    GTS "Well, I know that their name in other countries is peony and that they symbolize having bravery and courage. Besides looking rather lovely they are commonly used in some herbal medicines, which makes them a somewhat commonly-cultivated flower."
    MC "That's pretty cool actually, both cute and helpful."
    "She smiled in return."
    show GTS happy
    GTS "Yes, very much so I would say. That's a nice way to see it."
    jump GTS005_after
    
label GTS005_c2:
    MC "I'm doing okay, thinking about the results from the test."
    GTS "Yes... I would think quite a few students are thinking about that. I assume that's why the campus is a bit quieter than normal."
    MC "Yeah, I think a lot of people are trying to come to terms with what's going to happen to them. I'm not really sure how I feel about my condition though, it's rather strange if I say so."
    GTS "Strange in what way?"
    MC "Well I'm basically going to be able to pretend I'm some spooky long haired ghost girl every couple of weeks and scare people."
    "I rose my arms in a zombie like pose and made a rattling noise in my throat which caused her to flinch just slightly."
    show GTS sad
    GTS "I... hope you do not plan on actually doing that."
    MC "Heh... Not a fan of horror movies then, huh? Well don't worry, I'm mostly teasing, I wouldn't actually do that."
    extend " Well okay, maybe on halloween."
    GTS "..."
    MC "Basically though, my hair is going to grow a lot and rather quickly too. So, I had better learn how to cut my own hair, or else I'll be spending a ton of money just so people can see me."
    show GTS neutral
    GTS "Oh my, yes, I can see how that'd be an issue. Not to mention caring and maintaining it."
    MC "Yeah... that's a lot of hair products I'm going to have to learn about. But hey, at least I can cosplay any character I want now since I'll always have the right amount of hair for it."
    "I said with a grin, trying to be positive which in turn made her giggle and nod her head in agreement."
    GTS "Yes, that is one plus. Not to mention you'll be able to change your style to whatever suits you, letting you accessorize more ways than others would be able to."
    "I showed her my smile which made her smile back as she seemed to enjoy my positive outlook at the news of my condition."
    jump GTS005_after

label GTS005_after:
    MC "So, what did you hear from the nurse?"
    "The happy mood on Naomi's face seemed to have left with those words as she looked back at the floors for a moment then looked back at me."
    show GTS sad
    GTS "Well, my condition is rather unique. That's not to say the others aren't as well, I don't want to minimize the problems others may have. It's just, I don't really see many with what they say I have."
    MC "Is it bad?"
    GTS "I don't believe so. At least, I don't know and am not sure how one would tell. My results showed that I'll start growing taller over the course of the year."
    MC "Really? Yeah, that is a tricky one. Do they know how much?"
    GTS "No. There are estimates but one can never be truly certain."
    MC "Well I think you'll be okay, after all that's what this school is here for. To help anybody with any issues, right?"
    show GTS neutral
    "This did bring a small smile back to her as she looked back up at me."
    GTS "Yes, you're right. Thank you, Hotsure-san. It does help knowing that I will have help with this."
    MC "Yep! And I'm here to help you, too! So, don't hesitate to ask for anything, or rant more about your flowers."
    "I gave her a teasing smirk as she gave back a playful pout, but did smile."
    show GTS embarrassed
    GTS "I don't rant about flowers... not that much, anyway."
    "We both had a small chuckle as we spent a bit more time just talking in the garden."
    jump daymenu

label GTS006:
    $setProgress("GTS", "GTS007")
    scene School Front with fade
    play music Busy
    "There was quite a calming mood to the start of the school day as I wandered near the entrance. Something caught my eye, though, as I saw what appeared to be a small gathering of students near the front gate."
    "Curious, I wandered over, hearing some excited voices and sounds of affection. The reason for this became clear rather quickly, as it seemed a stray Shiba Inu puppy had wandered onto campus."
    Student1 "It's so adorable!"
    Student2 "D'aww! Look at his little paws!"
    "The crowd grew every couple of seconds as more people wanted to see what the commotion was all about. As I kept watching, I saw a familiar figure kneel next to the excited puppy and begin petting it."
    "Naomi held a warm smile on her face as her hand massaged the puppy's ears and even rolled him over to rub his belly. This caused the entire crowd to gush over the cuteness and I couldn't resist a smirk."
    "A little time passed before the dog's owner finally showed up and thanked everyone for finding their dog before taking it back home. As the crowd dispersed, I saw Naomi walk by and notice me. Flashing her trademark smile, she gave me a small wave of her hand."
    show GTS happy at center with dissolve
    GTS "Hello Hotsure-san, did you see the adorable Shiba Inu that had wandered onto campus?"
    MC "Yeah, I did! Well, I saw the crowd first, and had to see what was up."
    GTS "It was such a cute puppy, and very well behaved. Didn't you think so?"
    menu:
        "Kind of, but I'm mostly into cats myself.":
            jump GTS006_c1
        "Yeah, he was extremely cute!":
            jump GTS006_c2

label GTS006_c1:
    MC "Kind of, but I'm mostly into cats myself."
    show GTS neutral
    GTS "I see, well, cats are rather adorable too. Though I always enjoyed the companionship of a dog."
    MC "Yeah, I hear a lot of people are a big fan of how loyal dogs can be. Personally, I enjoy the peace and quiet a cat offers. Plus, they're so cute!"
    "Naomi gave a little giggle and covered her mouth at that last bit but nodded her head."
    show GTS happy
    GTS "Sorry, I didn't mean to laugh, it's just rather cute hearing that."
    "My cheeks felt a little warm as I rubbed the back of my head."
    MC "What can I say, little cute fluffy things just get to me."
    jump GTS006_after

label GTS006_c2:
    $setAffection("GTS", 1)
    MC "Yeah, he was extremely cute!"
    show GTS happy
    GTS "Indeed, he was, did you get a chance to play with him?"
    MC "Not really, too big of a crowd and I don't think it'd be wise to make a scene by barging through everyone to pet him."
    "This made Naomi giggle softly and nod."
    GTS "That's very true, but I don't think many people would hold it against you with such an adorable puppy on the other side."
    MC "Yeah... man I wish I had a dog like that."
    show GTS neutral
    GTS "Oh? Never owned a pet before?"
    MC "Nah, our place was always a bit too small for something like a dog, at least the ones my parents like. Plus, we were all mostly too busy to begin with, so it probably was for the best."
    jump GTS006_after

label GTS006_after:
    MC "So what about you? Have you ever had a pet?"
    show GTS neutral
    GTS "Yes actually, we have a Hokkaido dog back home."
    MC "Whoa, seriously!? Aren't those extremely rare?"
    GTS "I've never heard that, but I suppose they could be. I always thought they were rather common, since SoftBank uses one as a mascot."
    MC "I don't know, I've always heard they were really rare, even in Japan. Your family must be loaded!"
    show GTS embarrassed at Position(xpos=0.4, xanchor=0.5, yalign=1.0)
    "There was the faintest hint of a blush on Naomi's face as she broke eye contact and looked to the side for a second, before returning her attention."
    show GTS embarrassed
    GTS "My father always said he picked that breed because the Hokkaido has the three characteristic he looks for in people: bravery, loyalty, and intelligence. I can say he was right about that description, because she's probably been one of the most loyal dogs I've met."
    MC "She? So it's a girl."
    show GTS neutral
    GTS "Oh yes! Sorry, yes she's a girl. Her name is Kimiko and she has wonderfully white fur. She's been with the family for about five years now."
    MC "I see, that's pretty cool. I bet you can't wait to see them again."
    GTS "Yes, I do miss her a bit more than I thought, but I plan on heading home this weekend, so I'll be seeing her soon enough."
    MC "That's good to hear. Hmm, I wonder if I can plan a trip back home at some point too."
    GTS "Small breaks from school can do the mind a lot of good."
    MC "Yeah, especially with what we will be dealing with here over time. Yeah, maybe I'll pay home a visit sometime soon."
    "I got a small, understanding nod from Naomi, then an equally small, yet warm, smile."
    GTS "If you'll pardon me Hotsure-san. I believe we're already close to being late for class. It might be best to start heading to our home room."
    "I quickly looked at my watch and then chuckled."
    MC "Oh yeah... heh, I kind of lost track of time. Yeah let's get going. Maybe if I'm lucky I'll get a chance to see that puppy again someday."
    GTS "Maybe."
    "With a small giggle from Naomi, we began walking to class together."
    jump daymenu

label GTS007:
    $setProgress("GTS", "GTS008")
    scene School Planter with fade
    play music Peaceful
    "Petals danced in the breeze, carried aloft by the wind. They flowed peacefully down the pathway, where I saw a familiar figure sitting underneath the shade of a tree. Naomi's hair moved much like the flower petals had, as I noticed a paper in her hand."
    MC "Hey there Yamazaki-san, how are things?"
    "She looked up from what appeared to be a letter when I called out to her, and gave me a gentle wave of her hand."
    show GTS neutral at center with dissolve
    GTS "Hello Hotsure-san, I was merely reading a letter my mother sent me. How are you?"
    MC "I've been pretty good for the most part. Also, a letter? Hand-written? I'm surprised people still make those."
    "A faint smile crossed her face as she folded up the letter and placed it back into the envelope."
    GTS "Yes, they seem to not be in style much anymore; however, my mother greatly enjoys writing, so it's become sort of a thing she does for those living far from home."
    MC "That's pretty cool, I bet the post office loves having actual mail to give out that aren't just bills or packages people ordered online. That's a neat little post card too, where is it from?"
    "She looked down at the postcard in her hand that had come with the letter and lifted it towards me, showing a picture of Kyoto."
    MC "Oh hey, it's Kyoto. I thought I recognized that tower there. Are you from there?"
    GTS "Yes, I am."
    MC "Interesting. I've never been to Kyoto, but it always looked like a pretty neat place. I've heard that it's one of the best places to go for food, too."
    "There was the faintest smirk out of Naomi as her smile grew a little, giving a nod of acknowledgement as I sat down beside her."
    GTS "Yes, Kyoto is very well known for its cuisine. Specifically, our tofu and Kaiseki cuisine."
    GTS "My friends and I would often make a weekly activity to visit a new restaurant every weekend. It was rather fun and gave me a deep appreciation for my hometown. It lets you explore more, and sometimes you find little underappreciated establishments."
    MC "Wow, that's sounds like it'd be cool to do. Though it also sounds like it would be pretty heavy on the wallet after a while, wouldn't it?"
    GTS "Some places were more expensive than others, yes, but you'd be surprised by some of the places you find. Every now and then, we'd stumble across a place that not only had great dishes, but were also offered at a reasonable price."
    GTS "We had really expanded our list of places we could socialize. We had a bad habit of constantly claiming new spots as our favorite, only to then change it again a couple weeks later."
    MC "Heh, that doesn't sound like quite the bad habit to have, though now I'm trying to think if I ever did anything like that. I mean, I think I did a normal amount of exploring but it was never too extensive. Granted, it might simply be because how crowded it often gets where I'm from."
    GTS "Where are you from if you don't mind my asking?"
    MC "Oh, I'm from Tokyo. The big city, Gojira's favorite playground. Just a little bit off of Shibuya."
    GTS "Oh wow, that must have been something. Being so close to the center of all the action, you must have seen and experienced some rather interesting things."
    MC "Yeah quite a bit, especially during the holidays when all the tourists take over the streets. You basically turn an already crowded intersection into a literal impenetrable wall of humans. I felt bad for the people driving because well... they weren't going anywhere for quite a long while."
    GTS "I do hope you were careful during those times. I've heard stories of how overwhelming Shibuya can get during the holidays, as well as some of the nastier incidents that can take place due to so many people there."
    MC "Yeah, I was okay, I knew well enough to not get too absorbed into the larger crowds, and kept away from people who could have looked like trouble. Plus it's always good to have a couple of friends with you, makes some of the trouble makers think twice before starting anything."
    MC "That's just Shibuya during the big times of the year though, how about Kyoto? Does it get as crowded as Tokyo?"
    GTS "Well it would depend on the time of year I suppose. It's very much like any big city I would imagine, but I do know that around Christmas time restaurants tend to start charging more for meals, sometimes even doubling the prices of their dishes."
    MC "Because of all the people, I assume?"
    GTS "I believe so, though if I recall correctly a lot of people see Christmas as a big date night event, at least in Kyoto."
    GTS "I recall many of my friends going out on dates to places like La Part Dieu, which is this wonderful French restaurant, or they go to Daimaru to visit the stores and see the decorations."
    MC "I bet they saved up all year long for that night, if it's as expensive as you say it is. I can't say I've ever found myself in a scenario like that, though. Which is probably for the best, because I don't know any fancy places to eat. But how about you? Did you ever do anything with someone special?"
    "Naomi's cheeks turned quite the adorable shade of red as her composure broke and she looked down at her letter."
    show GTS embarrassed
    GTS "M-me!? Oh no, I never have... I was always too focused on other things like helping around the house or preparing for other social events. I've never really had time for things like that."
    MC "Oh? So, are you telling me you've never been on a date, then?"
    show GTS embarrassed at center, Transform(xzoom=-1)
    "I could see her face brightening up more as she tried avoiding eye contact. It was rather sweet seeing this side of her."
    GTS "I'll admit... that I have not. My schedule was and to an extent, still is, rather filled up with my responsibilities. It would have been nice to have seen what it was like, but it simply wasn't the right time I suppose."
    show GTS neutral at center, Transform(xzoom=1)
    "She looked back towards me as she managed to regain her composure. I gave her a small nod, as I didn't want to push the issue too hard."
    MC "Yeah, I guess it would be pretty tough if you're always busy. But at the same time, I wouldn't worry too much about it."
    MC "Going back to hanging out with friends, have you managed to make any new friends here?"
    GTS "...No, not really. It's been a chaotic time for many people trying to get settled in, so I try not to impose on them. I'm sure in the next couple of weeks, more people will open up and everything will fall back into a normal flow."
    GTS "Maybe then it'll be a bit easier to introduce myself to more people."
    MC "Well, if it's okay for me to throw out there, you could hang out with me and some of my friends at some point. Can't promise you'll hit it out of the park in the first couple of minutes but it's worth a shot, right?"
    GTS "Hm... Would it be okay if I took a little time to figure out my schedule before giving you an answer, Hotsure-san?"
    MC "Heh, yeah, it's okay Yamazaki-san. We're still young after all, so take your time."
    "I gave her a small chuckle, and she returned a smile and a nod. I leaned back a little, enjoying the calm of the garden as well as the gentle breeze, the two of us remaining silent for quite some time after that. Not that I'm complaining, since it was probably the most peaceful I'd felt in quite some time."
    jump daymenu
    
label GTS008:
    $setProgress("GTS", "GTS009")
    scene Roof with fade
    play music Sunset
    "My footsteps echoed up the stairwell as I ascended to the peak. Upon opening the door, a wave of warm sunlight washed over me."
    "As my eyes adjusted and I stepped out onto the school roof, I scanned the area to see if Honoka might be around. There were a small number of students hanging out and chatting but no sign of Honoka."
    "I didn't call out her name, but I did walk around to see if she might be around the stairway entrance. Surprisingly, it wasn't Honoka I found, but Naomi."
    "She had laid out a blanket and was currently sipping on some tea as what looked like a miniature garden sat in front of her, taking up a small portion of rooftop."
    MC "What do we have here? A secret garden?"
    show GTS neutral at center with dissolve
    GTS "Hm? Oh, hello Hotsure-san. Heh, no the gardener is well aware of this little plot."
    GTS "As a matter of fact, he helped set it up for me."
    MC "Wow, that's rather nice of him. What convinced him to do that?"
    GTS "According to him, he was simply happy to meet a kindred spirit. However, he wasn't able to find a patch in the actual garden for these, so he simply set up these rows of trays and let me plant in them."
    MC "That's pretty cool. When did you set this all up?"
    GTS "Oh, these have been here for about a week, so that's why you don't see any saplings coming out. A bit more time and they'll be ready to greet the world."
    MC "I've never been good with plants; how long does it usually take for them to grow?"
    GTS "It depends on what plant it is. The ones in the first row here are daisies, they'll take a little bit of time but are rather low maintenance. Just give them a little shade and water them from time to time."
    GTS "That's why I placed them in the front row. You see, when the sun is at the right time of day, the stairwell casts a shadow over the garden. With the daisies in front, they'll get the most shade for the longest time."
    MC "Pretty clever thinking there. And the other rows?"
    GTS "Well, the second row I wanted to plant tulips, but... those take anywhere from eight to ten years to fully mature to flowering size from seeds. So, I might just get some that are already grown and plant them there."
    MC "Jeez, are you serious? I never thought any plant that wasn't a tree took that long to grow."
    GTS "It can be a little tricky, but when you plan it all out ahead of time you'll get the results you want. Gardening is about patience and planning. Speaking of planning, I hadn't the slightest clue what I should pick to put in the last row."
    GTS "Any plant will do I suppose, but I want to make it something unique and special. I'm just not sure exactly what that should be, though. I'll need to give it more thought."
    menu:
        "What about one of the flowers you told me about earlier?" if getFlag("GTS008_flowers"): #(Only appears if you learned about the other flowers she's mentioned.)
            jump GTS008_c1
        "What about one of the flowers you told me about earlier? (disabled)" if not getFlag("GTS008_flowers"):
            pass
        "Yeah, I can't really help in that department. Maybe some daisies or roses? Sorry.":
            jump GTS008_c2

label GTS008_c1:
    $setAffection("GTS", 2)
    $setSkill("Art", 1)
    MC "What about one of the flowers we talked about earlier in the week?"
    GTS "Hm... that isn't a bad idea, Hotsure-san. If I were to go by the species I've told you about, then I have a good starting point to work with."
    MC "Yeah, sometimes it's best to break things into smaller groups so you can better analyze them."
    GTS "Indeed, thank you so much for the idea, Hotsure-san. That will make it much easier for me to think up plans of how and when to plant specific species."
    MC "Heh, it's no problem. Sometimes all someone needs is a helping hand."
    show GTS happy
    GTS "A helping hand... Ah! Hotsure-san, that's a wonderful suggestion."
    MC "I, uh... what?"
    GTS "Apologies, but you mentioned cooperation and that made me think about Verbena."
    MC "Verbena?"
    GTS "They are a species of small flowers with five petals and borne in dense spikes. They come in a nice variety of colors so it could add to the visual appeal of the garden."
    MC "Heh... well, glad I could help. Even if accidentally."
    "She giggled lightly and gave a warm smile."
    jump GTS008_after

label GTS008_c2:
    MC "Yeah, I can't really help in that department. Maybe some daisies or roses? Sorry."
    GTS "It's perfectly fine, Hotsure-san. It'll simply require a bit more thought and planning."
    MC "Well, what about sunflowers? That's about the only other flower I know that isn't a rose."
    GTS "A wonderful suggestion, Hotsure-san, but I'm sad to say their size would simply cause too much issue with the limited space I have to work with. Thank you very much for helping, though."
    MC "Heh, yeah... guess I didn't really think that one out too well."
    jump GTS008_after

label GTS008_after:
    show GTS neutral
    GTS "If you don't mind me asking, Hotsure-san, do you often come up to the rooftop?"
    MC "Yeah, from time to time I do. Honoka and I tend to use it as a meeting spot, and because of that I sometimes just wander up here for a breather. So, I guess you could say it's my version of the campus garden."
    GTS "Ah I see. It is a nice spot, I must say. Plenty of space, sunlight, and fresh air."
    MC "Yeah, I would agree with that."
    MC "Honoka and I are going to a festival in a couple of days. Would you like to join us?"
    GTS "Oh? I wasn't aware one was happening so soon."
    MC "Yeah, it's been so hectic here lately I'm not sure many of the students were aware either. Still I think it'd be good for us if we got to know the neighborhood, since we're going to be here a while."
    MC "Plus it could be fun. So what do you say?"
    GTS "I agree, it would be nice to learn more about the area as well as meet the people."
    show GTS happy
    GTS "I say yes, I'd be delighted to join you two - if you don't mind my intrusion?"
    MC "Heh, nah, we'd love to have your company. Great, though! I'll let you know when we're meeting up and where. Now if you'll excuse me, I have to find Honoka and let her know too."
    MC "Talk to you later."
    GTS "Goodbye Hotsure-san, have a pleasant day."
    "I waved at her as she bowed before I left the roof. I had actually only just learned of the festival a couple hours earlier, but this seemed like a good way for all of us to just relax and have fun. Now if only I could find Honoka..."
    jump daymenu

label GTS009:
    $setTimeFlag("size2")
    if getFlag("GTS011_unlock"):
        $setProgress("GTS", "GTS011")
    else:
        $setProgress("GTS", "GTS011b")
    scene Festival with fade
    play music Festival
    "Music and cheers set the mood as the buildings lining the block reflected the lights of various lanterns. Dusk was beginning to set in, and as it did, a wave of multiple-colored lights replaced the sunlight."
    "Booths covered both sides of each walk way as vendors attempted to tantalize visitors  with various knick knacks and home-style delicacies. They didn't get to me, though, as I had my sights set on a more personal venture. As I made my way further into the festival, I could pick out the two familiar voices."
    show GTS neutral at Position (xpos=0.25, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    show BE neutral at Position (xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    GTS "...Are you certain, Inoue-san? I know many lovely tailors and vendors who could find you the loveliest yukata."
    BE "Heh, nah, I'm good. They just really aren't my thing. Plus, with these girls, it's more of a hassle than you'd think."
    GTS "Well, if you're certain. Though I'd gladly help you get dressed if you're concerned about your bust getting in the way..."
    BE "Well I appreciate the help, Yamazaki-san, and I know this is the Yukata festival and all, but it's okay. I'm good. Besides, right now I need the support, and I know if you're wearing a yukata properly, you're not wearing anything underneath it. That goes for bras, too! Oh, look."
    BE "Yo! Kei-chan!"
    "She waved as she called out to me. Upon seeing them I cracked a small smile, as at least in Naomi's case, this had been the first time I'd seen them out of uniform. Honoka opted to wear a simple tank top and shorts, as with the warmth of the night it allowed her to enjoy the breeze. Naomi, on the other hand, got into the spirit of the festival and wore a full Yukata with a floral design, and even had an elegant flower hair clip on."
    # (This is mostly as a placeholder since with the art there will be a picture that negates this. But until then this is simply to describe them.)
    MC "Hey you two! Wow, Yamazaki-san, you look great."
    GTS "Thank you."
    show BE happy
    BE "Hey! What about me?"
    MC "Heh, you look great too, Honoka."
    BE "Thanks! Well, now that you're finally here, let's go explore!"
    GTS "Were you not going to wear a yukata, Hotsure-san?"
    MC "Oh! Um... probably not. I don't own one and I don't think I look good in them."
    GTS "Well, if you would like and if you don't mind, I could help you look for one that you might like."
    MC "You know what, sure, why not? Granted, I can't wear it now, but maybe for a future event."
    GTS "Exactly, one can never be too prepared. And I promise we'll find you something you'll like."
    BE "Fineeeee, but I'm not trying any of them on. So sadly, that's not a fantasy you'll be seeing today Kei-chan."
    MC "I- what?"
    BE "Heh. I know you were hoping to see me in one today. Sash way down past my boobs, hoping I'd spill a snow cone on them, or a goldfish would flop in my cleavage..."
    show GTS embarrassed
    GTS "Inoue-san..."
    MC "I uh... heh, how about we go looking for them, shall we?"
    show BE neutral
    show GTS neutral
    "We walked through the crowd, Honoka going wide eyed whenever any tasty sweet was shown to her from a vendor. She'd look back at me like a begging puppy, asking for money, which seemed to always win me over. Well... at least the first 5 times."
    MC "Honoka, I can't keep buying you things... I'm going to run out of money."
    show BE sad
    BE "But Kei-chan! It's shaved ice! What festival experience would be complete without some?"
    GTS "It's okay Hotsure-san, I can pay for this one. To be honest, I was hoping to get some myself. Which flavor would you like, Inoue-san?"
    show BE happy
    BE "Really? Thanks! Umm... hmmm... let's go with some watermelon and blue raspberry!"
    GTS "Very well. Hotsure-san, would you like some?"
    MC "Sure, if you're okay with the expense."
    GTS "Oh, it's truly no bother, Hotsure-san. Which favor would you prefer?"
    MC "I think I'll go for some mandarin."
    show BE angry
    BE "Booooooring. Come on, try something exciting, or mix them up."
    GTS "It's quite all right if you just want mandarin, Hotsure-san. I'm sure Inoue-san is merely teasing."
    GTS "As for myself, I think I'll have strawberry."
    "She placed the order and then compensated the vendor before she gently handed the shaved ice to each of us."
    show BE happy
    BE "Thanks, Yamazaki-san!"
    MC "Yeah, thank you."
    GTS "It's no problem at all. Please enjoy."
    show BE neutral
    "Our pace through the sea of people slowed considerably at that point as we enjoyed our treats. Thankfully, it was enough to distract Honoka from asking for other things until we eventually came upon a stand that seemed to catch Naomi's eye."
    GTS "Oh, Hotsure-san. This seems like a good stand to look at some yukata. Come take a look, please?"
    MC "Hm? Are there any that stand out to you?"
    GTS "Shouldn't I be asking you that though?"
    MC "Yeah, but I'm really not good at this stuff. Which do you think would suit me best?"
    GTS "I'd need to think it over a bit. Is there a particular color you were looking for?"
    MC "I suppose blue."
    GTS "Very well, I'll see what I can find in that color scheme."
    "She inspected the stand for a few moments, handing me her shaved ice so she could feel the yukatas. Checking every side, every inch as she carefully examined possibly hidden options. All the while Honoka ate more of her shaved ice, wincing at the occasional brain freeze before immediately taking another bite."
    GTS "What do you think of this one, Hotsure-san?"
    "She lifted up a blue-colored yukata, its design having a bold feeling towards it as there was light etching of mountains and clouds faintly imprinted on its surface. Not enough to be too distracting, yet still giving the eye a nice scene to take in if observed."
    MC "Oh wow, that's actually pretty cool."
    show BE happy
    BE "Yeah, looks awesome. I'd say it's a great find. Ow... my head..."
    GTS "I'm very glad you like it Hotsure-san. We'll take this one please."
    show BE neutral
    "She took the yukata to the vendor as she motioned for me to walk over. I handed our two shaved ice cups to Honoka, who snuck a bite from my bowl as I made my way over. Naomi had me stretch my arms outwards from my sides as she expertly placed the yukata on me."
    GTS "There you go, nicely done. And that's it Hotsure-san, thank you for allowing me to help you dress. If we had also gotten one for Inoue-san we would have needed to put another sash just underneath her chest, then smooth out the newer wrinkles before adding the obi."
    show BE happy
    BE "Yeah and that would take forever, so no thanks. Still, you look nice Hotsure-san."
    GTS "Indeed, you look very handsome, Hotsure-san."
    MC "Heh... thanks."
    show BE surprised
    BE "OH OH! Look!"
    hide BE with dissolve
    "She pointed to a new stand and ran off to check it out, Naomi and I quickly following her. We easily found Honoka as she frantically waved for us to hurry up, as there was a small crowd around this stand for some reason."
    "When we arrived, the reason became rather clear, as this stand had a game."
    show BE happy at Position (xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    Vendor "Welcome! Are you a master fisher? Well then test your skills in my little game against my expertly trained goldfish!"
    MC "You can train goldfish?"
    Vendor "Of course! It takes years of training and being one with the fish."
    MC "Uh... okay..."
    "He brought us over to see the game properly. It wasn't your typical scooping, it seemed. Instead the poi were shaped like small baskets and tied on the corners to a string that was attached to a small fishing rod."
    Vendor "Normally in goldfish scooping you do what?"
    show BE neutral
    BE "Scoop... goldfish?"
    Vendor "Correct! But that's not how the true art of fishing is. Fishing is about planning, patience, and execution. So my game reflects the true aspects of fishing! The rules are simple, you place the poi into the water and when a goldfish swims over it you quickly reel up the poi and try to catch it!"
    Vendor "Be warned though, you're not allowed to chase the fish with the poi, that counts as an immediate disqualification. But you also can't take your time, for the longer that poi is in the water, the weaker it'll become until it won't be capable of holding the fish or water!"
    MC "Doesn't that defeat the whole point of being patient?"
    Vendor "It's a balance! Why not give it a try?"
    "As he smiled at me, I noticed the current player reeling up his poi and having seemingly caught one of the goldfish, until... It merely jumped out of the basket right as the rim broke the surface."
    MC "I... don't know..."
    show BE happy
    BE "Come on, Kei-chan! I'm sure you can totally do it! I bet you're a great master fisher. If you can't do it, I bet I could."
    GTS "Yes Hotsure-san, it does seem like some rather harmless fun."
    Vendor "Well your lady friends seem to agree, buddy. How about it?"
    MC "I... guess?"
    Vendor "Great! 500 yen."
    MC "What? Aren't these normally about 100?"
    Vendor "If this was goldfish scooping, yes. But this is fishing good sir. 500 yen."
    "I gave him the money, and he handed me the fishing rod, before quickly replacing the poi basket."
    Vendor "Remember, the hardest test in life is having the patience to wait for the right moment."
    "He grinned at me as I let the basket carefully sink into the little pool. From my angle I realized that I couldn't tell how deep it was or where exactly in depth was my basket. Even the fishes could be at any point above the basket. I gave a couple of test reels, slowly expanding my basket though it seemed that each click of the reel sent a vibration down the wire which disturbed the water, signalling the fishes to move."
    "Taking a chance, I quickly reeled in as a fish swam over, but by the time the basket caught up the fish had already moved on."
    Vendor "Too greedy. Waaaait."
    BE "Come on Kei-chan, we're rooting for you!"
    "I gave a slight nod, as at least I was closer to the surface now. Though that also gave me fewer options, as not as many of the goldfish swam this close to the top. Each second ticked away without even the slightest hint of a fish drawing near, until finally one showed me mercy and swam just over my basket. Instinctively I yanked up to capture the fish, but this was a mistake, as the sudden force along with the erosion of the water had resulted in my poi collapsing and setting the goldfish free."
    Vendor "Ooooh, tooooo bad young man. Better luck next time."
    GTS "You gave it a good shot Hotsure-san."
    show BE sad
    BE "Awww..."
    MC "One more try."
    show BE neutral
    Vendor "Oh? Heh, very well young man. Just don't over extend yourself."
    MC "Don't worry, I got it."
    "I replied as I gave him the 500 yen and got a replacement basket. This time though I didn't carefully let my poi sink. No, instead I casually tossed it to one of the edges of the pool. This startled the goldfish who scurried in random directions. Though as they did this my poi was steadily sinking, all the while the first startled fishes startled those in front of them which repeated again until it was a slight chain reaction which forced some goldfishes to quickly swim back towards the original disturbance."
    "As they hurriedly swam back over my poi which hadn't had time to sink fully, I quickly reeled in as well as yanked, lifting my still sturdy poi out of the water. Honoka and even Naomi gave an audible cheer as the outline of a fish could be seen in the basket."
    show BE happy
    BE "You did it!"
    "I looked at the vendor confidently though when I looked back at the poi the goldfish suddenly lept out of it."
    "I couldn't react as I watched the fish descend back towards the pool, though it never made its target, as a small cup appeared beneath it and caught the goldfish."
    UNKNOWN "Here you go, mister."
    "As I looked down, I saw that the one holding the cup was a little girl."
    MC "Uhh... thanks."
    show GTS happy
    GTS "Ara ara, thank you so much."
    show BE happy
    BE "Nice save, kid!"
    LittleGirl "You're welcome!"
    "She giggled as I took the cup and patted her head, Honoka immediately hugging the child. Thankfully she let go before the kid suffocated. I displayed the fish to the vendor, my hand over the rim of the cup to prevent a repeat."
    show BE neutral
    show GTS neutral
    MC "I believe I've won."
    Vendor "I... huh. I don't know if that's against the rules or not."
    MC "You never mentioned anything about what happens to the fish once it's caught and out of the pool."
    Vendor "Hm. Very well, consider that a freebie kid. Though I'll be sure to add that to the rules."
    "He took out a notepad and began scribbling in it as I turned to Honoka and Naomi."
    menu:
        "Give the fish to Honoka":
            jump GTS009_c1
        "Give the fish to Naomi":
            jump GTS009_c2
        "Keep the fish for yourself":
            jump GTS009_c3

label GTS009_c1:
    $setAffection("BE", 3)
    MC "Here you go, Honoka."
    "I handed the cup over to Honoka, and her mouth opened wide in surprise."
    show BE surprised
    BE "Wahhh!? Why are you handing it to me?"
    MC "You seemed like you really wanted one. After all, you were the one who noticed the game."
    BE "Y-yeah... but that's just because I thought it looked cool. I wasn't trying to make you get one for me."
    MC "Well, I did regardless."
    BE "G-geez, thanks Kei-chan."
    "She carefully took the cup and blushed."
    show GTS happy
    GTS "That was very sweet of you, Hotsure-san."
    MC "Heh, well she looked like she wanted one, so I couldn't just let her not have it."
    jump GTS009_after

label GTS009_c2:
    $setAffection("GTS", 3)
    MC "Here you go."
    "I presented the fish to Naomi, who showed a genuine look of surprise."
    show GTS embarrassed
    GTS "W-what? Are you certain Hotsure-san? After all the effort you went to capture it?"
    MC "Yeah, think of it as a thank-you for paying for the shaved ice and helping with the yukata."
    GTS "But what about Inoue-san?"
    show BE happy
    BE "Heehee, he already bought me a ton of stuff so it's all good to me. Heck, that was the highlight of the night in my mind."
    show GTS happy
    GTS "I-I see. Thank you, Hotsure-san. I'll make sure to take good care of it."
    MC "I'm sure you will."
    jump GTS009_after

label GTS009_c3:
    $setAffection("BE", 1)
    $setAffection("GTS", 1)
    MC "Well... that was something."
    GTS "You did wonderfully, Hotsure-san. A great display that'd make any fisherman proud."
    show BE happy
    BE "Yeah! That was awesome. Heh, if it was me I probably would have just tried chasing the fishes with the poi."
    GTS "But didn't the vendor say that was against the rules?"
    BE "Huh? Oh, yeah. Well, I guess I would have been disqualified then."
    "Naomi couldn't help but let out the smallest giggle as Honoka chuckled to herself and smiled."
    MC "Now I just need to figure out where to put this little guy when I get back to my dorm. As well as find him the right bowl."
    BE "Oh, that'll be easy, I'm sure plenty of people here are selling bowls if you don't want to buy from this vendor."
    MC "I'm pretty sure he'd overcharge me."
    BE "Probably. I know I would."
    jump GTS009_after

label GTS009_after:
    MC "All right then, let's go find a good home for this little guy and enjoy the rest of the night."
    BE "Yeah! Let's party!"
    show GTS neutral
    GTS "Heh, indeed."
    "I led the way as we journeyed on to an eventful night of games, prizes, and food. And besides Honoka having eyes bigger than her stomach, the night was a ton of fun. I'm really glad we got a chance to do this, as well as getting the chance to take a picture of the three of us together."
    jump daymenu
    
label GTS010:
    $setSize(2)
    $setTimeFlag("aftersize2")
    scene Classroom with fade
    "A defeated sigh vacated my body. My hands had been slicking back my bangs all morning, and I could already tell this growth was going to be annoying. I had only just recently had my hair trimmed, and already it was as long as before I had first gotten it cut."
    MC "This is really going to burn a hole in my wallet if I want to keep myself from looking like a mountain man by the end of the month..."
    "As I slumped back in my chair, I heard the door to the classroom open and looked over to see Naomi uncharacteristically rushing to get to her seat."
    play music GTS
    MC "Hey Yamazaki-san."
    "The sound of my voice seemed to make her freeze on the spot like a deer in headlights. As I got up to greet her, I noticed that she was keeping her school bag in front of her."
    show GTS neutral:
        xpos 0.99 xanchor 0.0 yalign 1.0
        linear 5.0 xanchor 0.5 xpos 0.75
    MC "How... are you?"
    "As I walked over, her eyes were looking between me and her desk, and she seemed to be inching her way towards it."
    show GTS embarrassed:
        xanchor 0.5 xpos 0.75
        linear 1.0 xpos 0.7
        pause 1
        linear 1.0 xpos 0.65
        pause 1
        linear 1.0 xpos 0.6
        pause 1
        linear 1.0 xpos 0.55
        pause 1
        linear 1.0 xpos 0.5
    GTS "I'm... doing well Hotsure-san. Yes, rather well today."
    MC "You sure?"
    "I rose an eyebrow, but then tilted my head as something finally connected. Placing my hand flat on the top of my head, I moved it out towards her, making her duck ever so slightly as my hand just barely hovered over her head."
    MC "Huh..."
    GTS "Please excuse me Hotsure-san!"
    "She hurried to her seat and sat down, sighing as she placed her bag to the side of her desk, apparently feeling more secure now that she was seated."
    MC "Don't worry, Yamazaki-san, I don't think it's that noticeable."
    GTS "..."
    MC "I mean, I didn't even notice until just now. So I don't think anyone else has, especially with how everyone else is growing."
    GTS "Thank you..."
    show GTS neutral
    GTS "You're right, it's rude of me to forget that everyone else is undergoing the same thing."
    MC "Heh... Well I didn't mean that you were being rude. Just that it's not something you have to worry about."
    show GTS embarrassed
    GTS "I'm sorry, It's not really the height that bothers me it's just that..."
    "Her cheeks seemed to gain a slight shade of red as she looked away."
    GTS "My clothes don't fit as well, and I don't want to make a poor impression."
    show GTS embarrassed at Position(xpos=0.5, xanchor=0.5)
    menu:
        "(Check to see what she means)":
            jump GTS010_c1
        "I think they'll understand.":
            jump GTS010_c2

label GTS010_c1:
    $setAffection("GTS", -5)
    "I looked around her desk as she mentioned that, and saw just the faintest hint of her midriff before her hands quickly flew down to cover herself."
    #This could act as a special image where you see the faintest hint of her flat stomach.
    show GTS angry
    GTS "Hotsure-san!"
    "The surprising outburst caught the other students attention as I quickly rose my hands like a criminal giving in to the law."
    MC "Sorry! Sorry! Kind of did that subconsciously."
    GTS "Please. Don't do that again."
    MC "Sorry again..."
    jump GTS010_after

label GTS010_c2:
    $setAffection("GTS", 1)
    MC "I think they'll understand. I assume a few people are a little intimidated of the thought of going to the store to constantly to take new measurements for their uniforms."
    show GTS neutral
    GTS "That could be possible yes. I know I wouldn't want to bother them more than is necessary. I might have to see if I can get a seamstress to add a bit of fabric so it covers me better."
    MC "Let me know if you find a hair stylist looking for someone to be a practice dummy, while you're at it?"
    "I chuckled and pointed to my hair, which was more than a little messy looking."
    GTS "Hadn't you just gotten it cut at the start of the week?"
    MC "Yep! Looks like I'm gonna have to start taking notes on how fast it grows so I can properly think of hairstyles to give myself between haircuts. Because there's no way I'm gonna pay for a haircut every couple of weeks."
    GTS "Yes, that would be quite impractical after a while, I'd assume."
    jump GTS010_after

label GTS010_after:
    MC "Still, I think you're in the clear for now Yamazaki-san. Plus if you don't mind me saying, the new height isn't bad on you."
    show GTS embarrassed
    GTS "I..."
    GTS "Thank you..."
    if getAffection("GTS") >= 7:
        $setFlag("GTS011_unlock")
        if getProgress("GTS") == "GTS011b":
            $setProgress("GTS", "GTS011")
        GTS "Apologies for changing the subject so suddenly, but Hotsure-san... I was hoping to ask you..."
        show GTS embarrassed at center, Transform(xzoom=-1)
        GTS "Would you be interested in coming over to my dorm room sometime later? Some things I had forgotten at home will be coming by and I was hoping you wouldn't mind having some tea with me."
        "Like earlier, I saw the barest motion of a blush as her eyes for a split second looked away."
        MC "Totally! That sounds great."
        "For the briefest moment, her lips rose to a slightly larger smile before returning to their normal position."
        show GTS neutral at center, Transform(xzoom=1)
        GTS "I'll be sure to get everything fully prepared, then. I do hope you'll enjoy it."
        MC "Oh, I'm sure I will. After all, with your plant knowledge I'd expect you to be a tea expert."
        GTS "I wouldn't say so, but thank you for the vote of confidence."
        "We shared a smile before the door to the classroom opened once more and the teacher walked in, resulting in me hurriedly rushing to my desk as we began the day."
    jump daymenu

label GTS011:
    $setProgress("GTS", "GTS014")
    scene Dorm Exterior with fade
    "Journeying around the dorm, I heard whispers hang around behind me. The occasional giggle accompanied them as some girls watched me."
    "I could imagine it now, some small-time rumors about me visiting a girl at her dorm. The same happened when I saw my sister at the start of the year, but I had learned to merely ignore it."
    "Upon reaching her door, I gave it a couple knocks, faintly hearing some noise through it. When she opened the door, I found myself looking at the crook of her lip instead of her eyes."
    show GTS neutral at center with dissolve
    GTS "Hello Hotsure-san. I'm glad to see you, please come in."
    GTS "I hope it wasn't difficult finding my room."
    MC "No, it wasn't a problem at all."
    "She opened the door for me and gave a slight bow, the action causing the small of her back to show which in turn caused her hands to immediately try pulling her top to better cover herself."
    scene Dorm GTS with fade
    play music Busy
    "As I entered her dorm room, I saw another girl already inside. She sat kneeling at table, a cup of tea in her hand as she smiled and waved."
    show Ryoko neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    UNKNOWN "Howdy! You must be Hotsure-san."
    MC "Uh... yeah, I am. Hello."
    show GTS happy at Position(xpos=0.75, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    GTS "Hotsure-san, this is Ryoko Tanaka. Tanaka-san, this is Keisuke Hotsure. Tanaka-san is my next-door neighbor who I met a couple days ago, so I invited her over for some tea as well. I hope that isn't a problem."
    MC "No, it's all right. It's nice to meet you, Tanaka-san."
    Ryoko "Likewise, come on, have a seat."
    show GTS neutral
    GTS "Yes, Hotsure-san, please make yourself comfortable."
    "I nodded my head and removed my shoes before taking my place at the table. Naomi soon kneeled down beside me and poured me a cup of tea, to which I gave her a small nod."
    MC "Thank you."
    "Naomi gave a small nod in response as she gently set the teapot down, her hands subconsciously fixing her top to better hide her slightly exposed stomach before they rested in front of it to act as a cover. Meanwhile, Ryoko scooted a little bit closer to me."
    Ryoko "So how long have you known Yamazaki-san?"
    MC "Well, since the first day. I saw her at the garden before orientation, but only really got introduced to her at the orientation."
    Ryoko "I see. Sadly, I've been super busy since the start of the school year, so I only just recently ran into Yamazaki-san myself."
    GTS "I thought it would be nice to start introducing myself to my neighbors."
    Ryoko "She offered me these super tasty crackers and tea, too. Actually, Yamazaki-san, would it be all right to ask if you have any more? They'd go wonderfully with this tea."
    GTS "Ah yes, how rude of me. Please, excuse me."
    "She quickly stood up, her knees lightly bumping the table which she deeply apologized for before she hurried to get some snacks for the us to enjoy as I talked with Ryoko."
    hide GTS with dissolve
    MC "What have you been so busy with?"
    Ryoko "Oh, mostly filming."
    MC "Filming? Oh, thanks Yamazaki-san."
    show GTS neutral at center with dissolve
    "Naomi had already returned with a small tray of crackers and offered one to me and Ryoko, who also took one."
    Ryoko "Thanks Yamazaki-san. Yeah, me and a couple of students in the flim club are working on a small movie together."
    MC "Oh wow, that's pretty cool."
    GTS "That does sound like it would be fun."
    show Ryoko happy
    Ryoko "Oh, it's totally a lot of fun! Sure, they're just silly no-budget videos but it's still a blast. You two should join us sometime, we're always open for auditions."
    show GTS embarrassed
    GTS "Me!? Oh no, I couldn't possibly do something like that. I wouldn't be capable of remembering a single line, or ignoring the camera. Or are you supposed to look at the camera? I'd gladly watch them, though."
    MC "Heh, I actually wouldn't mind giving it a go sometime. Also, with enough experience in front of the camera I'm sure you'd get the hang of it, Yamazaki-san."
    show Ryoko camera
    Ryoko "Yeah Yamazaki-san, you'd be a natural! You'd bring a sense of elegance last seen in the classic era of films. The tall, slender beauty the men are drawn to, who gives an aura of maturity and confidence. Just like um... Jessica Rabbit! That's the name."
    "I could see the faintest hint of blush appear on Naomi's cheeks as she sipped some tea."
    GTS "I-I don't know... I wouldn't want to be distracting, or take away from the story being told."
    GTS "I'm sure Nikumaru-san would be a much better actress than me."
    show Ryoko happy
    Ryoko "I have no idea who that is, but seriously though, we'd love to have you guys come by if you ever want to hang out."
    show Ryoko neutral
    Ryoko "I'm sure you'd quickly win them over with those elegant looks."
    MC "I have to agree with her on that."
    GTS "Thank you..."
    Ryoko "So that's one thing I do on my spare time, what about you two?"
    MC "Well I kind of hop around a lot, so I couldn't really name one thing in particular."
    show GTS neutral
    GTS "I merely tend to my garden, as well as a couple of the plants here. Besides that, most of my time goes to my studies."
    Ryoko "I see I see, well then, I propose another get-together sometime soon."
    show Ryoko happy
    Ryoko "Oh! A movie day! I'll even pick up a pizza for us to enjoy."
    MC "A movie day?"
    Ryoko "Totally! What better way to hang out and relax with friends than a good movie and some tasty hot food?"
    MC "Well I can't disagree with that. ...Sure, that sounds like a fun time to me. What do you think, Yamazaki-san?"
    GTS "I'd have to look at my schedule. But I promise I'll let you know as soon as I get everything figured out."
    Ryoko "Excellent! Well, I'll be going on my way. Thanks so much for the tea and crackers Yamazaki-san, they were great. And it was nice meeting you Hotsure-san, catch you two later."
    hide Ryoko with dissolve
    "She gave us a wink and a bow of respect before heading towards the door, and seeing herself out before Naomi had a chance to get up. We sat there for a second or two, but soon enough I gave a small chuckle and took a sip of tea."
    MC "Heh, I see you started with the most energetic neighbor first."
    GTS "Yes... it seems so."
    jump daymenu

label GTS011b:
    $setProgress("GTS", "GTS014")
    scene School Planter with fade
    play music Busy
    "I stepped into the garden expecting the normal serenity one would find there, but surprisingly it was more active than usual."
    UNKNOWN "Okay, this is a good spot right. Now if I set up here…"
    "The garden was normally a place of solitude for the students, but it was interrupted by a red haired girl carrying around what appeared to be a film camera. "
    "Noticing Naomi sitting under a tree and watching the girl, I decided to investigate what was going on."
    MC "Hey Yamazaki-san, what's going on here?"
    show GTS neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    GTS "Good afternoon Hotsure-san. It appears Tanaka-san is location scouting."
    MC "Tanaka-san?"
    GTS "Yes, she's my neighbor at the dorm. We had been discussing-"
    UNKNOWN "Oh hey!"
    "The shout caught my attention as I turned to spot Tanaka rushing over with her camera in hand. The quirky girl smiling as she arrived back at us."
    show Ryoko neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    UNKNOWN "Hi there, I'm Ryoko Tanaka. Nice to meet you."
    MC "Nice to meet you too, I'm Keisuke Hotsure."
    Ryoko "Pleasure. Saw you talking to Yamazaki-san, you two friends?"
    if getAffection("GTS") < 2:
        MC "We're in the same class."
    else:
        MC "Yeah, a bit."
    Ryoko "I see. So Hotsure-san, you ever been in a movie before?"
    MC "W-what? A movie?"
    Ryoko "Yeah, you ever play a role before?"
    MC "Um no…"
    Ryoko "Aw, that's a shame, you have the looks of a leading man to you. Nice chin, decent build, and the hair over the eyes thing, very mysterious. Women love that, isn't that right Yamazaki-san?"
    show GTS embarrassed
    GTS "Huh? Oh I wouldn't know."
    Ryoko "Heh, she's just shy. But if you're ever interested give me a call alright."
    "She flashed a smile and a business card which she then handed to me. It was rather plain, though the title on the card stood out."
    MC "Oh I see, you're a film director."
    Ryoko "Yep! Film's my passion and storytelling is my art."
    MC "That's pretty cool, I take it you're in the film club then."
    Ryoko "Yeah but it's not quite what I thought it would be."
    MC "How so?"
    Ryoko "Well when I showed up it felt a little dead honestly. Not that the people there weren't interesting or anything, but it seems once word of us all having conditions came to light, everyone just kind of lost focus."
    MC "I think that's kind of understandable."
    Ryoko "Oh yeah I agree, but still, I can't let uncertainty scare me off of my passion."
    MC "Yeah you're right. Oh! I'm so sorry Yamazaki-san, I didn't mean to exclude you from the conversation."
    show GTS neutral
    GTS "Heh, it's alright Hotsure-san. I don't know how I could really contribute to the conversation. Plus it'd be rude for me to simply interject my thoughts."
    Ryoko "Of course not! Can't have a conversation if you don't speak after all."
    GTS "That's true. Do you think there may be a way to lift up the other students spirits?"
    Ryoko "Yeah, I've been thinking about it and came up with something that could be fun. A small group project, after all nothing helps keep your mind off things than having something to do."
    GTS "Indeed, busy work is a good way to ease a worried soul."
    MC "That's pretty neat. Any idea what you might do?"
    Ryoko "I have an idea, something quick, simple, and cheap. Horror movie."
    MC "Horror? That's an interesting direction."
    Ryoko "Oh it's the best! They're so fun that it's impossible not to have a good time. Just need the antagonistic force. Maybe your typical yo-kai."
    show GTS embarrassed
    GTS "A-a ghost?"
    Ryoko "Yeah, those are normally the easiest thing to work with besides like a slasher film. Just some make up, a vacant state, and a good creepy noise."
    "She stuck her arms out and made an oddly disturbing rattling noise with her throat. Due to Naomi's taller size, it was easy to see the slight flinch as she moved a bit closer behind me."
    MC "Isn't that more of a zombie?"
    Ryoko "Yeah, but they we do some lighting effects, proper clothes, and you'll make a slightly luminous effect that has a supernatural aura to it. Then bam, spooky ghost."
    GTS "Well you seem to have a good knowledge of how to handle it."
    Ryoko "Yep! Years of experience, give me a camera and I'll give you a film no matter what it is."
    Ryoko "…"
    Ryoko "Well okay, maybe not an animation. I can't draw to save my life and I especially don't know how to 3D model. But doesn't mean I can't find someone who does!"
    MC "Well films are a collaborative effort after all."
    Ryoko "Exactly right! Speaking of which. I should get back to the club to discuss ideas. Thanks so much for inviting me here Yamazaki-san. Got some great ideas for filming locations here."
    show GTS neutral
    GTS "You're welcome Tanaka-san. Please feel free to stop by from time to time."
    Ryoko "Oh I will be, after all have to see how this place looks at night. I already got ideas of where to place our ghost. This place is just perfect for a surprise haunted setting. I mean you can see it too right?"
    show GTS embarrassed
    GTS "I rather not think about it…"
    MC "Yeah this could work for a good ghost surprise."
    Ryoko "Mhm, well I'll see you two around. Oh and remember, if either of you two are interested in doing some acting just let me know. Later!"
    "She gave us a wink and a bow which Naomi returned in kind before Ryoko took off, barely giving me the chance to say goodbye."
    "We stood there for a second or two, but soon enough I gave a small chuckle and looked at Naomi."
    MC "Heh, me in a movie. I'd be a terrible main character, I'm better off being an extra. I'm a natural at just blending in to the background."
    show GTS neutral
    GTS "I think you'd do quite well."
    MC "Well thank you for the vote of confidence. Maybe I'll take her up on her offer. Who knows, maybe I'll win an award for best hair and make up."
    "Naomi placed a hand over her mouth as I heard the faintest giggle at my joke. The corner of her smile peeking out from behind her hand which in turn got a smile from me."
    jump daymenu

label GTS012:
    scene School Planter with fade
    show GTS neutral at center with dissolve
    play music Sunset
    "A small sigh left my body as I rested back against a tree. I was in the garden, Naomi having invited me for some tea after class had ended."
    "She had set up a blanket on the grass and was preparing the drinks. It was an interesting sight as she sat on her knees, an assortment of items in front of her as she began the long process of making the tea."
    MC "I've never seen someone do this in person before. That's pretty impressive."
    "She ground the tea leaves in a bowl, gently emitting a crackling sound."
    GTS "Thank you, Hotsure-san. It's one of the things I was taught when I was younger. I find the entire process deeply soothing: the preparation, the mixing, and then the tea itself. It can ease the soul and refresh the spirit."
    MC "Sounds really spiritual. Thank you, by the way. For inviting me over, and for the tea."
    GTS "You're most welcome, Keisuke. I felt it was the courteous thing to do after what you said back in class a few days ago."
    "I felt my face get a little warmer as I couldn't hold back a faint smile, the sharp whistle from the tea pot breaking the silence as the water came to a boil."
    MC "Well, you're welcome for that. Guess this would make us even then, heh."
    MC "I like the setup you have here, everything is very organized. It reminds me of how well you had your room organized."
    GTS "I find it makes getting everything ready for the day much easier. You know exactly where everything is and can move along at a fast pace."
    MC "It also made your room look bigger. Well, unless they gave you a bigger room, because I could swear it was larger than mine."
    "I gave a light chuckle but saw that Naomi looked a little tense."
    MC "O-Oh! Sorry, that wasn't meant as some jab at your condition."
    GTS "No, it's okay, I know what you were meaning. Honestly, I'm all right."
    "She appeared to be finished with the preparation, pouring the warm water into the cups, which began changing tint due to the crushed tea leaves within. She then carefully handed me my cup."
    MC "Thank you."
    "I took a sip and let the calming warmth and subtle taste flow into my mouth."
    menu:
        "Tell me a bit more about you learning how to do this with the tea.":
            jump GTS012_c1
        "So how have you been holding up, with your condition?":
            jump GTS012_c2

label GTS012_c1:
    $setAffection("GTS", 2)
    $setSkill("Art", 1)
    MC "Tell me a bit more about you learning how to do this, with the tea?"
    GTS "Oh, I wouldn't want to bore you with it."
    MC "Heh, it's fine, Yamazaki-san. I'm the one who asked."
    GTS "Well, if you insist."
    GTS "My parents thought it'd be wise for me to learn how to properly prepare and serve tea."
    show GTS happy
    GTS "After all, The whole process is not about drinking tea, but about aesthetics, preparing a bowl of tea from one's heart."
    MC "That's rather poetic, and a lot more thought-out than I was expecting."
    GTS "Well, that's because as the host, you always want to be mindful of your guests, so each movement, gesture, and even the placement of the utensils are carefully thought out before beginning."
    "With her mentioning of that, I noticed that she had indeed placed all the utensils in such a way that I'd be given a perfect view of each step she had taken to make the tea."
    MC "Heh, wow, you really did set this up perfectly, then."
    GTS "Thank you so much."
    MC "I was also going to mention that the scent was very familiar."
    show GTS neutral
    GTS "That is most likely because I often use the plants I grow in my room for my tea."
    MC "That's probably it, then. I must say, Yamazaki-san, I'm really impressed."
    show GTS embarrassed
    GTS "You're too kind, Hotsure-san."
    jump GTS012_after

label GTS012_c2:
    $setAffection("GTS", 1)
    MC "So how have you been holding up, with your condition?"
    GTS "I've been okay, Hotsure-san. How about you?"
    MC "Me? Yeah, I've been fine. It's a little annoying, but I can manage. I just wanted to make sure you're okay. I know some of the other girls are still a little worried about themselves."
    show GTS embarrassed
    GTS "That's very thoughtful. But I'm okay, I assure you."
    MC "All right, though if you need to talk, just let me know."
    GTS "I will, Hotsure-san."
    "We were silent for a little while after that, both sipping tea as I occasionally looked at her. She didn't look taller since the last time we had tea, but it was honestly hard to notice on a day to day basis. Still, I hoped she was okay and not just saying so for my benefit."
    jump GTS012_after

label GTS012_after:
    "I finished my tea and placed the cup back down before showing a hint of a smile."
    MC "Thank you again, it was wonderful."
    show GTS happy
    GTS "I'm glad you enjoyed yourself, Hotsure-san."
    MC "Do you mind if I ask you a favor, though?"
    show GTS neutral
    GTS "Oh? What is it?"
    MC "I've been having some trouble with some of our assignments. I was hoping you could possibly give me some help tomorrow in the library."
    GTS "Of course Hotsure-san, I'd be delighted to help you in any way I can."
    MC "Yeah... this subject's been kind of giving me a hard time. Thanks though, I really appreciate it."
    MC "Anytime, Hotsure-san. We are study partners, after all, and it'd show poorly on me if I let you down already."
    "She giggled very softly, which resulted in a chuckle from me as we relaxed for a little longer before needing to go our separate ways."
    jump daymenu

label GTS014:
    $setProgress("GTS", "GTS015")
    scene Classroom with fade
    play music Schoolday
    "I stared blankly at space in front of me as a cascade of thoughts swam around within my mind. It must have been rather noticeable, as I felt a pressure on my shoulder from a hand resting upon it."
    show GTS neutral at center with dissolve
    GTS "Hotsure-san? Are you okay?"
    MC "Huh? Oh, yeah sorry. Kind of spaced out there for a moment."
    GTS "Oh, better not let Tashi-sensei hear that."
    "I looked over as the blackboard was being erased and it seemed like some of the others were filing out of the classroom. "
    MC "Heh, I don't think he'll mind. Come on, let's take a small walk. "
    show GTS embarrassed
    GTS "Okay."
    "Naomi stood up from her desk and waited as I gathered my things before we left together."
    scene Track with fade
    show GTS neutral at center with dissolve
    "Eventually we stepped out into the soccer field, where it appeared a few people were gathering to start a game."
    "Among them was Honoka, whose quick wave I returned before deciding this was as good a place as any for a rest, Naomi and I taking a seat on the bleachers."
    "We observed the game for a few moments, before a random question entered my mind."
    MC "Hey Yamazaki-san. Have you ever thought about what you were going to do after you were done with school?"
    GTS "Hm? Do you mean like a profession?"
    MC "Yeah, have you ever given any thought about what job you might want to strive for."
    GTS "I don't believe I have really. Did you have something planned already?"
    MC "I've been thinking about Architecture as something I could do when I get out of school."
    GTS "That'd be a nice profession to get into. I would be interested in seeing what you could come up with. "
    MC "Thanks for the vote of confidence. ...So, you really haven't thought about what job you'd get after school's done?"
    GTS "Truthfully no, I've mostly focused only on my studies and hobbies. I suppose it just didn't cross my mind."
    menu:
        "So are you just going to keep doing your studies and see what happens when you reach the end?": #-1 Affection
            jump GTS014_c1
        "Well I heard a lot of women tend to get part time jobs, so you could try something like that.": #+0 Affection 
            jump GTS014_c2
        "How about something involving flowers? I'm sure people would enjoy a unique flower shop.": #+1 Affection
            jump GTS014_c3

label GTS014_c1:
    MC "So are you just going to keep doing your studies and see what happens when you reach the end?"
    show GTS embarrassed
    GTS "I-I suppose..."
    MC "Sorry, I'm not trying to put you on the spot or anything."
    $setAffection("GTS", -1)
    GTS "No it's fine Hotsure-san, you gave me something to really think about. So thank you."
    MC "Don't worry, Yamazaki-san, sometimes it takes a while for us to figure what we want to do."
    show GTS neutral
    GTS "This is true, but perhaps I should have put more thought into this than I had up until now."
    MC "I'm sure you'll get it all sorted out in no time, Yamazaki-san."
    jump GTS014_after
    
label GTS014_c2:
    MC "Well, I heard a lot of women tend to get part time jobs out of school, so you could try something like that."
    GTS "That's true, I'm sure there are a lot of jobs I'd be capable of doing."
    MC "Plus, if it's part time it'll leave you more time to do your hobbies."
    GTS "Indeed, it seems like it could be a good place to start."
    show GTS happy
    GTS "Heh, maybe I could be your secretary some time Hotsure-san."
    "I felt my cheeks warm up a bit as I chuckled and rubbed the back of my head."
    MC "Well, I wouldn't need to interview you, I already know how good you are with organizing and managing things."
    GTS "Thank you for the compliment, and it's nice to know I have a good chance then."
    jump GTS014_after

label GTS014_c3:
    MC "How about something involving flowers? I'm sure people would enjoy a unique flower shop."
    GTS "That's an option, I'd say. But would a flower shop really do well?"
    MC "I can't say honestly. I mean, I don't go to the flower shop very often."
    MC "Maybe something else, then. Maybe a gardener so you can help decorate a few places and really add a splash of color."
    show GTS happy
    GTS "That doesn't sound too bad to me. "
    MC "Yeah, and with your decorative skills I'm sure you'll be in high demand. Japan's full of flowers, your wallet's full of money. Sounds like a great deal to me."
    GTS "Heehee, ara ara. Such a high bar I have set before me."
    MC "Well if anyone can rise to the challenge, I'd say it's you."
    $setAffection("GTS", 1)
    GTS "Thank you for the vote of confidence, Hotsure-san. I'll give it some serious thought."
    jump GTS014_after

label GTS014_after:
    "A cheer from the field attracted our attention as it seemed Honoka managed to score a goal. She ran along cheering before suddenly lifting her shirt and placing it over her head and sliding on the grass. I couldn't help but chuckle as Naomi covered her mouth at Honoka flashing her sports bra to the rest of the team."
    MC "Haha, well that's Honoka for you. Still, no need to think about it too hard. We have a lot of time still. So let's just enjoy it for now right?"
    show GTS neutral
    GTS "Indeed, plan for the future but live for today."
    MC "Or as some would say, stop and smell the roses."
    GTS "Heh, yes very much so."
    "We gave Honoka a light cheer as we enjoyed the rest of her game as I eased my mind and let my thoughts float away with the breeze. Simply enjoying the moment with Naomi."
    jump daymenu

label GTS015:
    $setProgress("GTS", "GTS018")
    scene Dorm GTS with fade #this should change eventually
    play music Busy
    Ryoko "...And cut! Good job everyone!"
    "These were the first words Naomi and I heard as we waited outside of Ryoko's dorm room before we were allowed in, the 'QUIET! Filming inside!' sign taped on the door preventing us from knocking."
    show Ryoko happy at Position(xpos=0.70, xanchor=0.5, yalign=1.0) with dissolve
    "The bedroom had been transformed into a makeshift set, with extra curtains put up to eliminate any natural sunlight while other lights were set up to enhance the shot's lighting."
    "Two students I assumed were actresses were casually chatting to themselves while a couple of students worked to start putting away the camera, lighting, and various other bits of equipment."
    show GTS neutral at Position(xpos=0.30, xanchor=0.5, yalign=1.0) with dissolve
    MC "Um... hey there, Tanaka-san."
    show Ryoko happy at Transform(xzoom=-1)
    Ryoko "Hm? Ah! Hotsure-san! Yamazaki-san! I'm so glad you could make it. Please take a seat, we're wrapping up for today."
    GTS "Apologies if we're interrupting anything."
    show Ryoko neutral
    Ryoko "Nah, like I said, we're done for today. They're just getting everything put away. So how you two been?"
    MC "I've been pretty good, just the same old stuff, really."
    GTS "I've been well, thank you for asking."
    Ryoko "That's great, love to hear it."
    "Just then another student walked over and handed Ryoko a tablet."
    show Minori neutral at center with dissolve
    UNKNOWN "Sorry to intrude. Here you go, Tanaka-san."
    UNKNOWN "This is the new shooting schedule I managed to set up for you. We had to shift some things around as I couldn't secure proper locales yet."
    show Ryoko happy
    Ryoko "Wonderful! Thanks so much Tomoe-san. Oh, let me introduce you. Hotsure-san, Yamazaki-san, this is Minori Tomoe, my ever faithful assistant."
    MC "Hey there, nice to meet you."
    show GTS happy
    GTS "A pleasure to meet you."
    show Minori happy
    Minori "Oh! A true delight to meet you two. Tanaka-san has spoken highly of both of you, and I must agree with her that you're a true, natural beauty similar to vintage film actresses, Yamazaki-san."
    show GTS embarrassed
    GTS "Ara ara, I'm flattered but I'm hardly anything special."
    Minori "Nonsense! Hotsure-san, wouldn't you agree?"
    menu:
        "Huh? U-uh...":
            jump GTS015_c1_1
        "Honestly, I can see it.":
            jump GTS015_c1_2
        "I-I don't know. No?":
            jump GTS015_c1_3

label GTS015_c1_1:
    MC "Huh? U-uh..."
    $setAffection("GTS", 1)
    show GTS embarrassed at Transform(xzoom=-1)
    "Naomi's face quickly turned a shade of red before she looked away, my neck feeling a little hot as I loosened my collar."
    show Ryoko neutral
    Ryoko "Heh, don't tease them, Tomoe-san. "
    Minori "Of course. Apologies."
    jump GTS015_c1_after

label GTS015_c1_2:
    MC "Honestly, I can see it."
    show GTS surprised
    GTS "Huh!?"
    show GTS embarrassed at Transform(xzoom=-1)
    "Naomi's face quickly turned a shade of red before she looked away."
    Minori "Right? Such lovely hair, mature features, and an elegant figure. She'd be a hit opening night!"
    MC "A nice voice, too."
    GTS "Truly, I'm nothing extraordinary."
    show Ryoko neutral
    Ryoko "Heh, okay okay, let's not overwhelm the poor girl."
    jump GTS015_c1_after

label GTS015_c1_3:
    MC "I-I don't know. No?"
    show GTS sad
    $setAffection("GTS", -1)
    GTS "..."
    show Ryoko annoyed
    Ryoko "Nice, Hotsure-san..."
    MC "I-I didn't mean that as an insult or anything!"
    show Minori embarrassed
    Minori "Either way, I think you'd make a wonderful leading lady Yamazaki-san."
    show GTS neutral
    GTS "Thank you."
    "There was an awkward silence for what felt like an eternity before Ryoko spoke up again."
    show Ryoko neutral
    show Minori neutral
    jump GTS015_c1_after

label GTS015_c1_after:
    show GTS neutral at Transform(xzoom=1)
    Ryoko "Tomoe-san, do me a favor and please check that all the actors are informed of the shifting schedule and let me know if they have any requests."
    Minori "Certainly. I was truly a pleasure, you two. Hope to see you again soon."
    hide Minori with dissolve
    "Minori gave us a bow which we returned, and with a light twirl of their skirt went on their way, Ryoko thanking them as they left."
    show Ryoko happy
    Ryoko "You know, we should hang out sometime. Probably head off campus to explore the town a bit. Allows me a chance to do some location scouting too."
    MC "Hm, I wouldn't mind that. Could be pretty fun. What do you think, Yamazaki-san?"
    GTS "It would be nice to get a change of scenery."
    show Ryoko neutral
    Ryoko "Right? However, my plans are a little hectic with my current filming schedule. So please allow me some time to figure it out."
    GTS "Please, don't burden yourself on our behalf."
    MC "Yeah, if you're busy we can just wait."
    show Ryoko happy
    Ryoko "No no, it's no issue. Just the hectic life of a filmmaker."
    show Ryoko neutral
    Ryoko "I did do some searching online though, and there are a couple options for us to do in town. There's an old theater and a decently sized shopping district. Either of those catch your interest?"
    GTS "I'm fine with any choice."
    Ryoko "Hotsure-san?"
    menu:
        "Dinner and a movie sounds like it could be fun.": #GTS015_movie
            jump GTS015_c2_1
        "Some shopping and lunch would be nice.": #GTS015_shopping
            jump GTS015_c2_2

label GTS015_c2_1:
    $setFlag("GTS015_movie")
    MC "Dinner and a movie sounds like it could be fun."
    show Ryoko happy
    Ryoko "Awesome! I'll make sure we find the best movie to watch!"
    MC "Is that okay with you, Yamazaki-san?"
    GTS "Yes, I think it would be nice. I've been meaning to see what restaurants they have in town so this is a good opportunity."
    jump GTS015_c2_after

label GTS015_c2_2:
    $setFlag("GTS015_shopping")
    MC "Some shopping and lunch would be nice."
    GTS "I would be interested in seeing if the yukata vendor from the recent festival had a store. Some new materials would be delightful."
    Ryoko "And I could use some new props and equipment. And some new clothes wouldn't be bad either."
    jump GTS015_c2_after

label GTS015_c2_after:
    show Ryoko happy
    Ryoko "That settles it! The gang is hitting the town!"
    "She cheered and I couldn't resist giving a small cheer due to her enthusiasm, the action convincing Naomi to smile and give a delighted clap, and the rest of the film crew to look over at our sudden outburst."
    MCT "Since when were we 'the gang'...?"
    jump daymenu
    
label GTS016:
    scene School Planter with fade
    show GTS neutral at center with dissolve
    play music Busy
    "There was a gentle chirping up above as I looked up to see some birds, their chirping accompanying the soothing hum coming from Naomi. A smile had been occupying my face throughout the course of our time together, but quickly vanished as a little yellow mass floated by my face."
    show GTS neutral with hpunch
    "Startled, I flinched lightly as the bee resumed its business, inspecting the flowers we were planting. Naomi must have noticed my movement."
    GTS "Is everything all right, Hotsure-san?"
    MC "Yeah, just got startled by a bee."
    GTS "Oh? You're not allergic, are you?"
    MC "No, just don't want to get stung is all."
    GTS "I see. No need to worry, then. As long as they are allowed to do their duty, they'll be more than happy to leave you be."
    MC "Heh, I guess you're pretty use to seeing bees around you, then?"
    GTS "Indeed, it comes with the territory. Heh, I will admit I did get my fair share of stings when I was younger."
    MC "Ow, did you swipe at them or something?"
    GTS "No, nothing like that. I actually attempted to catch them. I always saw them flying around flowers, so I wanted to keep some so they could see the flowers in my room."
    MC "So even at a young age you wanted to share your love of flowers?"
    show GTS happy
    GTS "It appears so, but they often stung me instead. I recall one time when my mother was rubbing cream on some fresh bee stings, she told me of the task that is given to all bees."
    GTS "About how they travel far and wide to find flowers. All in an effort to gather the necessary materials to create honey, and how by doing so they help pollinate the flowers."
    GTS "I grew an appreciation for them when I learned about how much they help plant life."
    MC "Like finding comrades in arms, right?"
    show GTS neutral
    GTS "Yes, very much so. And truthfully, I find them cute in a way. Their little fuzzy bodies just floating by to see the flowers."
    MC "Really? I think it's hard to find many people who can say that about insects."
    GTS "True, but I like them well enough. Actually... when I was younger, I asked if I could dress up like a bee for school."
    "The mental image of Naomi in a bee-inspired costume flashed by immediately."
    MC "I guess you'd have been the queen bee then, huh?"
    show GTS happy
    GTS "Ara ara. I never saw myself as the queen. If anything I wanted to be a drone."
    MC "Huh? Really? Why?"
    show GTS sad
    GTS "Queen is a nice title, but she has to stay in the hive all day."
    show GTS neutral
    GTS "The drones, though, get to explore the world."
    GTS "It's certainly dangerous, but the places they find and all the flowers they get to discover... That's all I wanted to do."
    "She tenderly placed another flower in the open patch of dirt and covered it with soil as I handed her the water canister, which she used to carefully water the newly rooted flower."
    menu:
        "I'd probably be too scared of getting eaten by a bird or getting swat at by a human.":
            jump GTS016_c1_1
        "Yeah, that sounds like a fun time to me.":
            jump GTS016_c1_2
            
label GTS016_c1_1:
    MC "I'd probably be too scared of getting eaten by a bird, or getting swat at by a human."
    show GTS sad
    $setAffection("GTS", -1)
    GTS "Oh, yes there's always a risk for the poor things. But that's what makes them more endearing to me, that they're willing to take on the journey for the betterment of their hive and for the betterment of the flowers."
    MC "That's true I suppose, nothing ventured, nothing gained sort of thing?"
    show GTS neutral
    GTS "Yes, I believe so."
    jump GTS016_c1_after

label GTS016_c1_2:
    MC "Yeah, that sounds like a fun time to me."
    MC "Granted, I think for me it's more the freedom of being able to fly around and see things."
    show GTS happy
    $setAffection("GTS", 1)
    GTS "Heh, yes that would be fun. I can picture flying high above and looking down at all the wonderful colors of the flowers down below. Flying down and collecting nectar from various flowers to bring back..."
    MC "Sounds like a dream job for you."
    GTS "It does, though I would miss being able to plant flowers."
    MC "Yeah, maybe being a professional bee isn't the best career path for you. Tempting, but not exactly what you're looking for."
    GTS "Heehee, perhaps not. And here I thought I finally figured out something to do after school."
    jump GTS016_c1_after

label GTS016_c1_after:
    "Naomi halted for a moment as a bee landed on her wrist. She didn't react though, merely giggling as his little feet tickled her skin before climbing onto the flower she was tending to."
    "Her hands moved more delicately as she ensured the flower was securely buried while the bee did its business. A grin appearing on my face as I watched them work together for a few moments before the bee moved on to another flower and Naomi was allowed to give the flower some water."
    MC "Man, all this bee-talk makes me want to get some honey toast."
    show GTS happy
    GTS "Oh, that sounds delightful, Hotsure-san."
    MC "Want to go into town and see if we can get some?"
    GTS "Certainly."
    "We stood up, Naomi gently dusting off her hands as she then looked down at me and smiled. "
    show GTS neutral
    GTS "I believe we've earned a nice reward for all our work today."
    MC "Yep! A nice sweet treat. Come on, let's go check out the town."
    "We left for town, chatting along like normal, though I had to quicken my pace to keep up with Naomi's elongated strides. Behind us, a few more bees came to inspect the additions we had made to the garden together."
    jump daymenu

label GTS017:
    scene School Planter with fade
    play music Busy
    "My brow lowered in annoyance as the wind blew my hair across my face yet again, my hands constantly trying to tuck it behind my ears or slick it back to keep my hair from doing so. I could see Naomi in our usual meeting place, attending to something. "
    show GTS neutral at center with dissolve
    "Making my way over, I spotted a small collection of balls that appeared to be made of mud as I looked at Naomi."
    MC "What's with all the mud? Planning a mud ball fight?"
    GTS "Heh, no. This is merely something I used to do as a child whenever I had to wait for a while."
    MC "Ah, sorry to keep you waiting then."
    GTS "No need to apologize Hotsure-san, I merely arrived early."
    MC "I see... So does what you're doing have a name, or is it just something you came up with?"
    GTS "The activity is called the art of the hikaru dorodango. Which are these."
    "She placed a mud dumpling that she had been crafting into my hands, the orb roughly the size of a softball. I could feel how compacted the dirt within was, but as my digits pressed a little bit more, cracks began to form on the surface of the ball before finally it started to crumble in my hands."
    MC "Ah! I'm sorry!"
    "As the ball fell to pieces, Naomi simply giggled before patting the ground next to her, wordlessly inviting me to take a seat with her."
    GTS "It's okay, Hotsure-san, I should have warned you that they are very fragile. But that's why I made several."
    MC "Still, sorry about that. Is that the finished result?"
    GTS "Not quite, it's the end of the first step. You see, normally you get some mud..."
    "She reached down, picking up a canteen of water which she poured into the small mud pile she had made, before reaching over and pouring some water in front of myself to create my own section of mud."
    GTS "If you wish, you may join me. Though your hands will end up getting messy, so if you don't wish to, that's fine as well."
    menu:
        "(Get an understanding of what she's doing, so sit this one out.)":
            jump GTS017_c1_1
        "(Learn as you go. Join her.)":
            jump GTS017_c1_2

label GTS017_c1_1:
    "She reached down into the damp and gripped a good handful of mud."
    GTS "Once you have a good amount of mud, you begin to shape it with your hands, adding more mud if need be. Your goal is to make it as perfectly round as you can."
    "Her hands flowed with grace as they smoothed the surface of the mud, before applying the faintest amount of pressure to compact it."
    "I kept looking towards her as she remained silent. Occasionally she'd reach for more mud, increasing the size of her ball as it filled out more of her grasp."
    MC "So what's the proper way to do that?"
    GTS "There are a few ways one can do this. Just keep in mind that the process is more about patience rather than force. You can press the mud together through your own strength, but too hard and you'll end up breaking it. The process requires more of a gentle but frequent touch."
    "She demonstrated by adding another layer of mud, but this time rotating the ball in her palm as her other hand tenderly pressed on small imperfections. Experience shined through as she was able to manipulate the ball faster, yet with more care as her palm would give small squeezes to the ball."
    MC "Okay, I think I see what you mean. How did you find out about this?"
    GTS "From my mother. She said that my sister and I used to be so impatient so she showed us something her parents had taught her. It seemed really silly to us at the time, simply playing with mud. But when she showed us what the end results looked like and we didn't believe her, we had her teach us."
    MC "And what do the end results look like?"
    GTS "Hm, I don't have one here. But remind me to show you one I've finished whenever you come by my dorm room. I'll gladly show you what it looks like when you finally complete a dorodango."
    MC "Sounds good to me. So how long does it take to normally get the finished product?"
    GTS "It varies depending on how smooth and shiny you want the ball to become. For me it normally takes a couple of weeks."
    MC "Weeks!? Geez, I thought this was like a single afternoon sort of deal, like gunpla building."
    GTS "Gun...pla?"
    MC "It's a model kit thing, you make a little toy robot from smaller pieces you put together."
    GTS "I see. Yes, that sounds like an appropriate comparison. And it can be done in an afternoon, but I generally enjoy taking my time with these, so I tend to be a bit slower than most."
    show GTS happy
    GTS "There we go. Now we just let this fully dry, and I'll continue the next steps at a later time."
    MC "What do the next steps involve?"
    show GTS neutral
    GTS "You carefully dust the ball with a fine dirt, and make a new layer along the surface. You then repeat this process a number of times with finer sifted dirt until you get the degree of smoothness you want. After which you gently wipe down the ball with a cloth."
    MC "I can see why it'd take a while."
    GTS "Indeed, but I like to think that the reward is far worth the effort and time you place into the act."
    MC "Well, I will admit it was rather relaxing, watching you do that. Maybe I'll give it a try when you start the next step."
    show GTS happy
    GTS "I'm happy to hear that. Now then, shall we go get cleaned up?"
    MC "Yeah, maybe we can get something to eat, too."
    show GTS neutral
    GTS "Sounds great, Hotsure-san."
    jump daymenu

label GTS017_c1_2:
    $setFlag("GTS017_dorodango")
    "She reached down into the damp and gripped a good handful of mud, my hands mimicking hers, though I had to do a little extra work to meld the not-fully damp mud."
    GTS "Once you have a good amount of mud, you begin to shape it with your hands, adding more mud if need be. Your goal is to make it as perfectly round as you can."
    "Her hands flowed with grace as she smoothed the surface of the mud, applying the faintest amount of pressure to compact it. My own hands were a bit firmer as I squeezed the mud to mold it to the desired shape."
    "I kept looking towards her as she remained silent. Occasionally she'd reach for more mud, increasing the size of her ball as it filled out more of her grasp. I had to do the same to keep the ball evenly shaped, though I began to notice the more mud I added, the more delicate I would have to be, as too much pressure would make small flakes of mud crumble off."
    MC "Am I... doing it correctly?"
    $setAffection("GTS", 1)
    show GTS happy
    GTS "Yes, maybe be a little gentler. But you're doing well, Hotsure-san. Just keep in mind that the process is more about patience than force. You can press the mud together through your own strength, but too hard and you'll end up breaking it. The process requires more of a gentle, but frequent, touch."
    "She demonstrated by adding another layer of mud, but this time rotating the ball in her palm as her other hand tenderly pressed on small imperfections. Experience shined through as she was able to manipulate the ball faster yet with more care than myself as her palm would give small squeezes."
    MC "Okay, I think I see what you mean. When did you learn about these?"
    show GTS neutral
    GTS "From my mother. She said that my sister and I used to be so impatient so, she showed us something her parents had taught her. It seemed really silly to us at the time, simply playing with mud. But she showed us what the end results looked like and we didn't believe her so we had her teach us."
    MC "And what do the end results look like?"
    GTS "Hm, I don't have one here. But remind me to show you one I had finished whenever you come by my dorm room. I'll gladly show you what it looks like when you finally complete a dorodango."
    MC "Sounds good to me. So how long does it take to normally get the finished product?"
    GTS "It varies depending on how smooth and shiny you want the ball to become. For me, it normally takes a couple of weeks."
    MC "Weeks!? Geez, I thought this was like a single afternoon sort of deal, like gunpla building."
    GTS "Gun...pla?"
    MC "It's a model kit thing, you make a little toy robot from smaller pieces you put together."
    GTS "I see. Yes, that sounds like an appropriate comparison. And it can be done in an afternoon, but I generally enjoy taking my time with these, so I tend to be a bit slower than most."
    show GTS happy
    GTS "Ah, there we go. I think mine is done for now. How are you doing, Hotsure-san?"
    "Her dorodango was perfectly spherical while the lump in my hand more resembled coal in texture than the smooth ball she had."
    MC "I think I need more practice."
    GTS "Don't worry, I'll help you."
    "Retrieving her canteen, she poured some more water onto the mud ball before her hand cupped my smaller one. She placed her other hand underneath my turned palm to add some more stability, guiding my in hers while turning the ball and applying light pressure."
    show GTS neutral
    GTS "There's multiple ways one can go about doing this, so don't feel like you need to do it the way I'm showing you Hotsure-san. But sometimes being shown the way once is all one needs to find their own path."
    "Her voice was as soft as her hands as she showed me the way. Even with the mud from earlier, her hands were still warm and soft to the touch. As we worked together, a gentle humming came to emanate from her. A soothing melody that went in pace with her hands, and I found it easier to gain a rhythm by following hers."
    "In no time at all, my dorodango was a passable appearance of sphere-like. It had some lumps still, and a little uneven here and there, but it would do."
    show GTS happy
    GTS "There we go. Now we just let these fully dry, and if you'd like we can continue the next steps at a later time, Hotsure-san."
    MC "What do the next steps involve?"
    show GTS neutral
    GTS "You carefully dust the ball with a fine dirt, and make a new layer along the surface. You then repeat this process a number of times with finer sifted dirt until you get the degree of smoothness you want. After which you gently wipe down the ball with a cloth."
    MC "I can see why it'd take a while."
    GTS "Indeed, but I like to think that the reward is far worth the effort and time you place into the act. So give it time, Hotsure-san, and hopefully you'll feel the same when you finish yours."
    MC "Well, I will admit that this was rather relaxing, the thought of doing more doesn't sound half bad."
    show GTS happy
    GTS "I'm happy to hear that. Now then, shall we go get cleaned up?"
    MC "Yeah, maybe we can get something to eat, too."
    GTS "Sounds wonderful, Hotsure-san."
    jump daymenu

label GTS018:
    $setProgress("GTS", "GTS019")
    scene School Exterior with fade
    play music Sunset
    #SFX wind
    "There it was again, the breeze that always blew my hair across my face."
    MC "One of these days I'm going to just gel my hair back..."
    "I continued down the path for a little bit longer, ignoring the fact that my hair was dancing with the motion of the wind. The breeze soon carried something else with it, however, as I could hear a faint giggle."
    "Further down the path I could spot Naomi waiting for me, a smile on her face as the wind made her hair flow majestically behind her. She looked upwards as the breeze made the tree branches above her sway, causing rays of sunlight to sweep through and illuminate her."
    "The way the light showed her, along with the motion of her hair, made me think back to what Ryoko had once said. Naomi truly appeared like a beauty one would have seen in an old-school film. Her hand slid through her hair as she closed her eyes and enjoyed the cool air, before finally spotting me when she opened them."
    show GTS happy at center with dissolve
    GTS "Good afternoon Hotsure-san, I hope your day is going well."
    MC "Hey Yamazaki-san, yeah it's going pretty well. Kept you waiting, huh?"
    GTS "Not at all, please take a seat. "
    "She presented the spot next to her on the bench as I joined her, though being this close to her I realized I must have looked somewhat like a little brother compared to her stature."
    GTS "Days like these are simply wonderful. A nice breeze, a warm sun, and the sounds of leaves dancing high above."
    MC "That's true, it really is just the right temperature out today. So did you want to get started on our studies?"
    show GTS neutral
    GTS "Yes, sorry for delaying us."
    MC "Heh, you didn't, so there's no need to apologize. Okay, so today we should cover-"
    stop music
    UNKNOWN "Whoa! You're perfect!"
    "We both flinched at the sound of a new voice, quickly looking over as another student hurried over to us. Her rather thick thighs jiggling as she came by."
    UNKNOWN "Hey there! Sorry for startling you but you're just perfect!"
    "She beamed as she looked at Naomi with sparkles in her eyes."
    show GTS embarrassed
    GTS "I-I'm sorry, but I don't know what you mean."
    UNKNOWN "I mean that you're perfect! Like literally, you're just what we're looking for."
    "Naomi was at a loss for words.I couldn't blame her, given she had nothing to work off of as the girl seemed heavily invested in her."
    Fumika "Oh, I should introduce myself first, duh! I'm Fumika Usui and I'm part of the basketball club! It's a real pleasure to meet you..?"
    GTS "O-oh! Naomi Yamazaki..."
    "She gave a seated bow as the girl giggled and looked at me, making me realize that I needed to introduce myself too."
    MC "Keisuke Hotsure."
    play music Tension
    Fumika "Hey there, she your girlfriend?"
    MC "W-what?"
    GTS "H-huh!?"
    Fumika "Ah I see, still on the hush hush. Don't worry, I won't tell, hee hee..."
    GTS "..."
    MC "..."
    Fumika "Anyway, as I was saying. You're just perfect! Have you ever been interested in possibly joining the basketball team? It's a ton of fun and we're all super nice."
    GTS "Uh... I hadn't really given it any thought before, truthfully."
    Fumika "Whaaa? How could you not? With your height and build you'd be a natural."
    GTS "It's simply something that hasn't crossed my mind before. I'm not very athletic, sorry."
    Fumika "That's totally fine, we wouldn't throw you into the deep end at the start. We'd help you get the basics of the game down. Plus, there's other girls around your height there too, so they totally can teach you the ropes."
    GTS "Around my height?"
    Fumika "Of course, I mean it's only natural to take what you're given as an advantage. You don't have to if you don't want to, but I'm just saying that you'd be a total shoe-in, and a great addition to the team. Plus I promise it'd be a ton of fun, really it's pretty great. What do you think? Think she should join us?"
    "I was a little taken back at suddenly being reintroduced into the conversation as I spaced out for a second. Naomi turned to look down at me, though it was a little hard to judge how she really felt about the situation."
    menu:
        "Yeah, you should totally give it a try, Yamazaki-san, I'm sure you'd be great at it!":
            jump GTS018_c1_1
        "You don't have to if you don't want to, Yamazaki-san, I'm sure she'll understand.":
            jump GTS018_c1_2

label GTS018_c1_1:
    MC "Yeah, you should give it a try Yamazaki-san, I don't see any harm in at least trying it out."
    Fumika "Totally!"
    GTS "A-are you sure?"
    MC "Yeah, I mean you get to learn something new, and maybe make some new friends, too."
    GTS "This is true. I've just never been too good at sports, though."
    Fumika "Don't worry, when we're done with you you'll be an unstoppable dunking machine! I mean just picture it, being the star of the team!"
    $setAffection("GTS", -1)
    show GTS sad
    GTS "I'm not sure. Would it be okay for me to take some time to think it over?"
    Fumika "Oh yeah, take as much time as you need, no rush. We're normally practicing at the gym after class on Thursdays, so if you want you can just stop by. We'll introduce you to the rest of the team."
    show GTS neutral at Position(xpos=0.7, xanchor=0.5, yalign=1.0), Transform(xzoom=-1)
    GTS "Thank you. I'll see if I have time to stop by."
    Fumika "Great! I'll see you there, then! Later you two!"
    stop music
    "With a wave and without another word Fumika took off back towards the campus. I waited for a little bit to make sure she was gone before looking back towards Naomi. I almost spoke before I noticed that she was looking away, her hand gently gripping her skirt."
    MC "Yamazaki-san? You okay?"
    GTS "Hm? Oh yes I'm fine. Just thinking, so you mentioned wanting to study earlier?"
    MC "Uh yeah... here, let me get the textbook."
    show GTS neutral at Transform(xzoom=1)
    "There was an awkward tension for the next few moments as a part of me wondered if I shouldn't have pushed her to join as our lesson began."
    jump daymenu

label GTS018_c1_2:
    MC "You don't have to if you don't want to, Yamazaki-san, I'm sure she'll understand."
    stop music
    "There was a faint smile on Naomi's lips as she gave a slight nod."
    $setAffection("GTS", 1)
    show GTS neutral
    GTS "Would it be okay for me to take some time to think it over?"
    Fumika "Yeah, that's perfectly fine. If you want, you can stop by some time and meet the other girls, too. We're usually at the gym after class on Thursdays, so if you're ever curious just come visit and I'll be happy to introduce you."
    GTS "Thank you Usui-san. I'll be sure to come by and meet everyone."
    Fumika "Great! Can't wait to see you there. Well, I'll see you two later, then."
    play music Sunset
    "She gave us a small wave as she took off back to the campus. I waited until I was sure she was out of earshot before I spoke."
    MC "Well, that was something."
    GTS "Indeed."
    MC "At least she's passionate about the team, so can't fault her there. Still, really random. You okay, though? Seemed a little taken aback from all that."
    GTS "Yes I'm fine, I'm not really used to being approached like that. Well, besides family get-togethers or my father's meetings, and even then not so... vigorously."
    MC "Yeah it seemed like it, but I don't think anyone would have really been ready for something as abrupt as that."
    show GTS happy
    GTS "Thank you for understanding."
    MC "Still... can't believe she thought we were dating."
    show GTS embarrassed
    GTS "..."
    MC "Heh... Uhh... yeah... so where were we?"
    GTS "About to study."
    MC "Oh yeah! Just um, let me get the book out."
    "There was an awkward silence for the next few moments as a thought lingered on the assumption about our relationship. I could sense my face getting a little warmer at that as I opened the textbook, in hopes of focusing on something else for a moment as to not embarrass myself."
    jump daymenu

label GTS019:
    $setProgress("GTS", "GTS020")
    scene School Planter with fade
    "A gentle humming floated through the air as I stared up towards the clouds. There was a faint swishing noise a foot or two away from me as I laid in the shadow cast by Naomi."
    "A mixture of the sun's warmth along with the soothing melody caused my eyelids to begin growing heavy, as I hadn't a thought in the world besides taking in the moment."
    scene black with fade
    "Eventually a soft chuckle made me realize that I had fallen asleep at some point..."
    scene School Planter with fade
    show GTS happy at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    "...as my eyes opened and I saw Naomi smiling down at me."
    play music Schoolday
    GTS "Very sorry Hotsure-san, I didn't mean to wake you."
    MC "That's okay. I, uh... wasn't aware that I had fallen asleep."
    GTS "Well, it is a very lovely day, so I can understand the appeal of just taking a nap."
    MC "Yeah, it's pretty peaceful today. How is the shodō going?"
    show GTS neutral
    GTS "It's going well, would you like to see?"
    "I sat up as Naomi placed her brush down onto the inkstone while I peeked at what she had created. The Kanji made me blush a little as I read, “Dream” upon the paper before hearing a giggle above me."
    show GTS happy
    GTS "Sorry, but seeing you sleeping inspired me to write that."
    MC "Heh, well I'm glad I could offer some inspiration. Even when I'm sleeping."
    "I gave more attention to the artwork, noticing the motions of the lines. There was a lightness to it, but also an effortlessness. It had almost appeared as if she had let her mind wander, yet somehow retained the perception of a detailed eye."
    MC "I have to say, Yamazaki-san, this came out extremely well. Just the way it looks, I get this sense of ease from it."
    show GTS happy
    GTS "Thank you, Hotsure-san. I did a couple as a sort of practice, and with as lovely as a day this has been, I couldn't help but let my hand play."
    MC "Yeah, there's this free-flowing motion to all of it. Heh, kind of like a leaf in the wind."
    show GTS neutral
    GTS "Hopefully not as chaotic as that."
    MC "No, not as chaotic. You can see that you had a preset destination in your mind, but the way you moved your brush gives the effect that it was a happy coincidence."
    MC "How long have you been practicing?"
    GTS "Since I was very young, before we were taught it in school."
    MC "I assume it's another tradition your family passed on to you."
    GTS "Yes, it is. In fact, my brush was made by my great-grandfather about seventy years ago."
    "She presented the brush to me, which I took with great care and began looking over."
    MC "This is really nicely made, what materials did he use?"
    GTS "The bristles are made from raccoon dog hair, while the handle itself is bamboo."
    MC "Well, he did an amazing job, I'll say that much."
    "As I motioned to give her back the brush, I saw a small smile spread across her lips."
    GTS "Hotsure-san, would you like to do one?"
    MC "Huh?"
    GTS "I imagine it can be a little dull simply watching me take part in the activity. So would you like to do one yourself?"
    MC "Uh sure, I'll give it a shot."
    "I scooted closer to Naomi who placed the dream paper aside, showing the cloth for the ink underneath before she placed a new sheet upon it with a paper weight on that to make sure the wind wouldn't take my project away."
    GTS "There you go, whenever you're ready Hotsure-san."
    MC "Hmm..."
    menu:
        "(Draw the Symbol for 'Human')": # +0 Affection, +1 if stat higher than 25
            jump GTS019_c1_1
        "(Draw the Symbol for 'Cherry Blossom')": # +2 Affection, +3 if art stat higher than 45
            jump GTS019_c1_2
        "(Draw the Symbol for 'Happiness')": # +1 Affection, +2 if art stat higher than 35
            jump GTS019_c1_3
    
label GTS019_c1_1:
    "My mind drew a blank as I simply let my hand move with the first thought that came to mind, and as such my work was done almost as soon as it started."
    GTS "Let's see what you did."
    if getSkill("Art") < 25:
        show GTS embarrassed
        GTS "O-oh, a very... interesting style, Hotsure-san..."
        MC "Thanks, been a while since I did this."
    else:
        $setAffection("GTS", 1)
        GTS "Ah, human. Interesting choice, Hotsure-san."
    MC "Yeah... I kind of blanked there, so I let my hand take the wheel."
    GTS "That's all right. I'm sorry for putting you on the spot like that. Still, I think it came out nicely."
    "She carefully removed the paper and placed it in the pile along with the ones she had done."
    jump GTS019_c1_after
    
label GTS019_c1_2:
    "I had no idea what I'd go with as I stared at the white canvas before me. Then, just like I had been inspiration for Naomi earlier, I decided she would act as my inspiration here. I got to work, planning out my movements before my hands executed them. As long as I focused, I could get this done."
    "After a few minutes passed, I finally let out a sigh of relief and placed the brush down."
    GTS "Let's see what you did."
    if getSkill("Art") < 45:
        $setAffection("GTS", 2)
        show GTS embarrassed
        GTS "Ah... I see what you went for, Hotsure-san. That was quite the brave effort."
        show GTS embarrassed at Transform(xzoom=-1)
        GTS "{size=-6}At least... I think I know what this is...{/size}"
        MC "Uh thanks..."
        show GTS embarrassed at Transform(xzoom=1)
        GTS "Ah! I mean no offense, Hotsure-san. Here, let's put it with the others..."
        "She carefully removed the paper and placed it in the pile along with the ones she had done."
    else:
        $setAffection("GTS", 3)
        show GTS surprised
        GTS "Oh my! This is rather lovely Hotsure-san. I wasn't aware you had a talent for shodō as well..."
        MC "I truthfully haven't done much of it. I've just practiced with ink brushes, but I suppose that helps with other forms in general."
        show GTS happy
        GTS "I would agree with that statement."
        show GTS embarrassed
        GTS "Uh... w-would you mind if I kept it?"
        MC "Hm? U-uh, sure you can keep it."
        GTS "T-thank you..."
        "I watched as she reached over, grabbing her stamp and placing a seal on the bottom portion of the paper. My face grew a little warm, as she really did seem to appreciate the piece quite a bit before she put it away."
    jump GTS019_c1_after

label GTS019_c1_3:
    "I pondered on what I could write down as a soft breeze blew my hair. That gave me the inspiration I needed, as I thought back to how peaceful the day felt and how it made me feel. Smiling, I got to work with my project, making short strokes as I finished the art piece in a few minutes."
    GTS "Let's see what you did."
    if getSkill("Art") < 35:
        $setAffection("GTS", 1)
        GTS "Ah, I see it. Happiness. A nice choice to go with, Hotsure-san."
        MC "Thanks, just went with how I was feeling."
        GTS "Well, I'm glad you're happy."
    else:
        $setAffection("GTS", 2)
        GTS "Heh, a nice mood to have, Hotsure-san."
        MC "Yeah, I have to admit the atmosphere of today has made me rather happy."
        show GTS happy
        GTS "It makes me happy to hear that. The piece came out well, too."
        MC "Thanks, it's been a while since I've done shodō, but it was fun."
    "She took the sheet and placed it on the pile with hers before looking back at me and smiling."
    jump GTS019_c1_after

label GTS019_c1_after:
    show GTS happy
    GTS "I'm happy you joined me today, Hotsure-san."
    MC "It was no problem, it was nice. Plus, with how perfect it is outside today, it'd be silly for me to stay indoors."
    show GTS neutral
    GTS "True. Still, it's nice having company on days like theses. So thank you."
    MC "Thanks for inviting me, is what I should be saying."
    "I leaned back and closed my eyes as I let the warmth of the sun bathe over me, my ears picking up Naomi shifting a little as she must have been getting comfortable as well. Laying back on the grass, I let out a sigh and smiled. This was a great day."
    jump daymenu

label GTS020:
    $setProgress("GTS", "GTS021")
    scene Roof with fade
    play music GTS
    "A light melody slid through my lips as I whistled to myself waiting, on the roof of the classroom building. Naomi seemed rather nervous when she had asked me to come by after class, so I was more than curious to see what was up."
    "This thought was interrupted, though, as my bangs drooped over my face again. Sighing in annoyance, I combed them back once more with my hand and cursed myself for not remembering to gel my hair back this morning. I then heard the door open and saw Naomi walk through with a modest-sized bag."
    show GTS neutral at center with dissolve
    GTS "Apologies, Hotsure-san, I hope I didn't keep you waiting."
    MC "Nah, I only got here a couple of minutes ago. What was it you wanted to show me?"
    show GTS embarrassed
    GTS "Oh. Well... I was hoping I could ask if you'd be willing to possibly... try this latest batch of cookies I've made?"
    "She reached into her bag and retrieved a neatly and carefully folded cloth, which, upon unraveling, revealed a newly-baked batch of cookies."
    MC "Oh, wow! Yeah, sure, I'd love to try some. They smell really good."
    "I took one of the top cookies, feeling the warmth and tenderness to it before placing it in my mouth. I was mentally grateful that this cookie was a vast improvement over the first ones I had tested for Naomi."
    MC "Mmm, that's pretty good. A lot better than last time, I can say that with certainty."
    show GTS happy
    GTS "Truly? Oh, I'm so relieved to hear that Hotsure-san. Please, sit down so you can enjoy them better."
    "We walked over to where her little garden had been set up, the buds of some saplings coming through the soil as Naomi pulled out a blanket from her bag and placed it down for us to sit on."
    MC "Yeah, it's quite the improvement, honestly. Mm, can I have another?"
    GTS "Please do, Hotsure-san. I made them for you to enjoy, after all."
    show GTS embarrassed
    GTS "I practiced with Kodoma-san a couple more times since my first attempt. She's very talented, so I learned a lot from her."
    MC "It shows. These are great, Yamazaki-san."
    show GTS happy
    GTS "Thank you Hotsure-san."
    "As I ate, my vision started to get covered as my hair began to droop forward once more. Letting out a sigh of frustration, I rose my hand but then stopped as something else combed my hair back."
    "I looked over as I saw Naomi, cheeks a shade of red, as her hand rested atop my head. Her eyes focused on mine before she realized what she was doing and quickly moved her hand away, the motion making my hair cover my face once more."
    show GTS embarrassed
    GTS "S-sorry! Apologies, Hotsure-san, I shouldn't have just done that..."
    GTS "I regret invading your personal space like that. I just noticed your hair falling back into place and just... wanted to help."
    MC "Yamazaki-san, it's fine. Don't feel bad, thanks for helping me."
    GTS "You're welcome. I... like your eyes, by the way."
    MC "Huh?"
    GTS "Your eyes. I never really got to see them before because of your hair, no offense. They look... nice."
    MC "Heh, well that's the first time I've ever heard that. Thank you for the compliment. I think your eyes look nice, too."
    GTS "R-really?"
    MC "Yeah, there's something calming about the way you look at people."
    GTS "I-I haven't been staring at people, have I?"
    MC "No no, I simply mean that when you do look at someone, you just give off this relaxing aura."
    "There was an awkward silence that followed as I continued to chew before Naomi spoke up."
    GTS "H-hotsure-san...I was... wondering. Uh, well, if it's not a bother. If, um... you'd like to go into town this weekend?"
    MC "Like, with the others, too? Sort of a group hangout?"
    GTS "..."
    GTS "N-no... I mean, simply you and I."
    MC "O-oh..."
    menu:
        "I... don't know if I'm ready for that...": # -5 Affection
            jump GTS020_c1_1
        "S-sure. Where would you like to go?": # +10 Affection
            jump GTS020_c1_2

label GTS020_c1_1:
    play music Bittersweet
    MC "I... Don't know if I'm ready for that..."
    show GTS sad
    GTS "Oh... I'm sorry, Hotsure-san. I had merely assumed... Apologies, I shouldn't have."
    MC "Don't get me wrong, Yamazaki-san, I like you too, but... I'm just not really sure if I'm ready for that."
    $setAffection("GTS", -5)
    GTS "Yes, I understand. It was far too forward of me. I'm sorry to put you in this situation, Hotsure-san."
    "I placed a hand on hers and looked up at her."
    MC "That doesn't mean we can't go out at some point, though. I would really enjoy that. Just, not now?"
    "It appeared as though my words reached her, as she smiled lightly and nodded."
    show GTS neutral
    GTS "I understand, and... I would like us to at some point."
    MC "We will, don't worry. But hey, I can't finish all these cookies by myself. Have some."
    "We shared the cookies Naomi had baked and chatted about various things. Even though the topics were mundane, the words she spoke carried more weight now, it felt."
    jump daymenu

label GTS020_c1_2:
    MC "S-sure. Where would you like to go?"
    show GTS embarrassed
    GTS "I'm sorry Hotsure-san, that was too forward, I shouldn't have assumed-"
    show GTS surprised
    GTS "W-wait, what did you say?"
    MC "I said sure, where you'd like to go?"
    $setAffection("GTS", 10)
    GTS "R-really!?"
    show GTS embarrassed
    GTS "I-I'm not sure... I-I w-wasn't sure you'd agree..."
    MC "Heh, honestly I wasn't sure for a bit there, either... but... I realized that I would like that."
    GTS "W-w-well I'd need to properly plan everything then."
    show GTS embarrassed at center, Transform(xzoom=-1)
    GTS "W-we could go visit the park,"
    show GTS embarrassed at center, Transform(xzoom=1)
    extend " or go to a restaurant,"
    show GTS embarrassed at center, Transform(xzoom=-1)
    extend " or maybe the movies?"
    show GTS embarrassed at center, Transform(xzoom=1)
    extend " Or-"
    pause 0.5
    show GTS embarrassed at center, Transform(xzoom=-1)
    pause 0.5
    show GTS embarrassed at center, Transform(xzoom=1)
    pause 0.5
    show GTS embarrassed at center, Transform(xzoom=-1)
    pause 0.5
    show GTS embarrassed at center, Transform(xzoom=1)
    MC "Haha, calm down Yamazaki-san. We're in no rush. We'll figure it out. Let's just... enjoy right now."
    show GTS happy
    GTS "Yes... you're right, Hotsure-san. Sorry, I got a little carried away there. I just... well, didn't think this would be how this turned out."
    MC "Trust me, you caught me by surprise, too. And here I thought these cookies would be the only surprise tonight. Speaking of which, I can't finish all these cookies by myself. Come on, try out some of your handiwork."
    "I raised a cookie up to her, her cheeks still a shade of crimson as she nodded and took it. We continued our conversation, shifting to more causal topics, but the mood was much happier. Naomi smiled a little wider than usual, and I noticed her shift her body a little so it was slightly closer to mine."
    "We talked so long that we lost track of time, but that was okay since every moment felt better than the last."
    jump daymenu

label GTS021:
    $setProgress("GTS", "GTS025")
    #$setProgress("GTS", "GTS022")
    scene School Planter with fade
    show GTS neutral at center with dissolve
    play music Peaceful
    "Having received a message from Minori about Naomi wishing to see me, I wandered into the garden with my eyes peeled and ears perked. I . As my footsteps bent the blades of grass underneath, I spotted Naomi at her usual spot, a mat underneath her and another laid beside her. She sat with her hands rested peacefully on her lap as her eyes laid shut."
    MC "Hey Yamazaki-san, you wanted to see me?"
    "She remained silent, raising a finger to her lips for silence before motioning to take a place next her."
    "I took the hint and got on my knees next to her, hands resting on my lap as I mimicked her pose."
    "So we sat."
    "And sat."
    $renpy.music.set_pause(True)
    "And sat..."
    MC "Uh... what are we doing?"
    "My questioned seemed to amuse her as she broke concentration to giggle softly."
    show GTS happy
    GTS "We're meditating."
    MC "Oh! Sorry. Well, I feel stupid."
    $renpy.music.set_pause(False)
    GTS "It's perfectly fine, Hotsure-san. I asked you here to see if you wanted to meditate with me for a little bit."
    MC "Sure thing, so just shut my eyes and breathe in. Easy enough."
    "I took deep breaths, and even though her breathing was soft and steady, her enlarged size still made it audible to me."
    "We sat there for a few moments, and I felt a leaf fall on top of my head."
    MC "How long have you been practicing meditation?"
    show GTS neutral
    GTS "Since I was five years old."
    MC "Another tradition your parents wanted you to follow?"
    GTS "Yes. I hope it isn't an issue."
    MC "Oh no, not at all, I just noticed that they seem to adhere to a very particular lifestyle, at least for you."
    GTS "My father has always been one for carrying on tradition."
    MC "Any particular reason why?"
    GTS "My father would most likely say it's good for an individual's growth to have a strong foundation as they mature. A set of guidelines to ensure a certain path."
    MC "Huh, that's rather insightful."
    MC "I can see why you also follow these traditions."
    menu:
        "It shows a lot of resolve to be able to do so.": # +5 Affection
            jump GTS021_c1_1
        "Have you ever wanted to do something else though?": # +1 Affection
            jump GTS021_c1_2


label GTS021_c1_1:
    MC "It shows a lot of resolve to be able to do so."
    MC "It's... what's really impressive about you."
    "Naomi's body turned rigid for a moment, a subtle action enhanced by her larger frame."
    $setAffection("GTS", 5)
    show GTS embarrassed
    GTS "U-uh, thank you." 
    GTS "It's truthfully not that difficult. It's merely repetition and sticking to a routine."
    MC "Well you've always been pretty good at organizing things, so I suppose that would make it a lot easier for you."
    "A blush was beginning to spread across her cheeks as her line of sight shifted away from me."
    GTS "Compared to Matsumoto-san or Tomoe-san, I'm really not that organized."
    MC "I dunno, everything you've shown me tells me otherwise. How well you organize your room, plan out these get-togethers, and even the lessons you make for when you teach me new traditions."
    GTS "Ara ara, you flatter me. Thank you, but I swear it was merely coincidence."
    "Her face had turned into a crimson mask as she rose a hand to her cheek, an attempt to hide the smile that was forming on her lips. An impossible-to-contain chuckle escaped me as I watched her."
    MC "Well, it's quite the happy accident then. Keep it up."
    "She gave me a small nod as I smiled in return, but then chuckled once more."
    MC "I'm sorry, I'm horrible at meditating it seems."
    show GTS happy
    GTS "Heh, that's okay. I think this conversation was well worth it."
    MC "Yeah, I think so, too."
    jump GTS021_c1_after

label GTS021_c1_2:
    MC "Have you ever wanted to do something else, though?"
    GTS "How so?"
    MC "In the sense that I'm sure there was at least one lesson you took as a child that you weren't fond of."
    GTS "Certainly, but I think most children are like that at first. It's hard to see the benefits of something when you're young."
    MC "True, but I'm sure there has to be something you try to avoid doing."
    GTS "Truthfully, no. I've never found anything I was taught to be a burden in some way."
    MC "Have you ever considered a hobby that wasn't in that traditional spectrum?"
    GTS "I... hmmm..."
    GTS "I suppose not. Though I wouldn't really know where to begin."
    MC "Well I'm not saying you have to. Just that there's no harm in exploring things outside your comfort zone."
    MC "Who knows, maybe you'll discover that you're into pop music and try making some yourself."
    GTS "Oh, I could never do something like that."
    MC "Don't knock it 'til you try it. Heh, maybe you'll even be the next top idol."
    show GTS happy
    $setAffection("GTS", 1)
    GTS "Now you're just teasing me."
    MC "I'd buy a ticket."
    GTS "Heh, stop."
    jump GTS021_c1_after

label GTS021_c1_after:
    show GTS happy
    GTS "Thank you for joining me, Hotsure-san. This was a very pleasant talk."
    MC "It really was, so thank you for asking me to come by. Even if we didn't succeed in our attempt."
    show GTS neutral
    GTS "I suppose we'll have to try again then."
    MC "Sounds great to me. Okay, I'll try to focus this time."
    "I settled back into position on my mat as we shared a last look before closing our eyes together. Taking a deep breath, we let the world's ambiance take hold of us as we began our meditation."
    jump daymenu

label GTS025:
    if getFlag("GTS015_movie"):
        $setProgress("GTS", "GTS028T")
    else:
        $setProgress("GTS", "GTS030")
    scene Campus Center with fade
    "I tapped my foot on the grass as I checked my watch once more. It was already half past five, and yet Ryoko still hadn't shown up."
    show GTS neutral at center with dissolve
    "Naomi seemed more patient than me as she sat under the tree, drinking tea from her cup."
    MC "I wonder what's keeping Tanaka-san. She was supposed to be here thirty minutes ago."
    GTS "It could possibly be some sudden school work she realized she needed to do. I'm sure she'll be here soon, though. By the way, would you like some tea, Hotsure-san? I brought some extra cups in case you and Tanaka-san wanted some."
    MC "Sure, I'll have some. Thank you, Yamazaki-san."
    "As I sat down and took the cup, a small jingle came from my pocket. Retrieving my phone, I read the newest text message I had received while sipping tea. It appeared Ryoko had indeed become bogged down with some last-minute assignments she had been putting off."
    "She apologized a few times and asked me to inform Naomi as well."
    MC "Well, I guess we're not going to show up in one of Tanaka-san's projects today."
    GTS "Oh? Was that her?"
    MC "Yeah. It seems you were right. She has to do some other work that she'd been delaying. You know, it's gotta be tough trying to find time to film things while also doing the normal coursework."
    GTS "I would imagine so. What should we do, though?"
    MC "Hmm, I'm not sure. Hey, why don't we just take a walk around the campus?"
    GTS "A walk? Yes, that sounds lovely, actually."
    "She collected her items while I stood up, and upon her rising up from her spot, our increased height difference quickly became apparent, as I found myself face-to-bust with Naomi."
    "I averted my gaze as to not embarrass her, then looked up at her."
    MC "Ready to go?"
    "From there, we took a miniature tour of the campus. We stayed outside for as long as we could, partially to take in the scenery and partially to allow Naomi total comfort, as once we entered the school that'd change."
    "Upon entering the school, Naomi immediately began to adjust herself to avoid possibly bumping into obstacles that I wouldn't have even considered. From there it was short trips to the cafeteria, library, and music club."
    "The voyage came to its conclusion on the school roof. Bathed in the light of a setting sun, I breathed in deeply, taking in the aroma of the flowers Naomi had planted earlier."
    MC "This is nice, I don't really take many chances to go out late in the afternoon."
    GTS "I would recommend it. The way the breeze journeys along, the colors the sun paints across the land, and the calm the setting provides... It's truly a lovely hour."
    MC "Poetic."
    show GTS embarrassed
    GTS "I, my apologies, Hotsure-san."
    MC "Don't worry, I like it. And I would say I agree with you, it's nice just being out here and seeing the world through this filter."
    "I moved closer to the fence and sat down, giving myself the best view that I could before Naomi sat next to me."
    "There weren't any more words at that point. Just us and the tender solace we had found."
    "My senses felt heightened, everything looked sharper and sounded clearer: The wind blowing through the leaves, the faint chatter of some students, even the soft breathing of the body next to me."
    "I made note of the air washing over me, making my bangs fly briefly. I felt the rough texture of the floor beneath my hands and fingers. And then to my surprise, felt the pressure of another body lean against mine."
    "I didn't move; in fact, I became more rigid. I knew what this warmth was, yet its softness was foreign. My eyes wanted to turn my head to make confirmation, but my brain already knew the answer."
    "I didn't move, I didn't speak. I feared that either would ruin this moment, as Naomi leaned against me to share it. Instead, I chose to get the most of this moment that I could, a smile spreading across my face as I shut my eyes."
    "I don't know how long we stayed like that. Some smart guy once made mention of how your brain changes its perception of time, but at the moment his name and his theorem were irrelevant. Any minute, any second longer that I could have I would accept."
    "But this moment would have to depart, yet I was not prepared for the method in which it chose to leave."
    GTS "Hotsure-san..."
    MC "Yeah, Yamazaki-san?"
    GTS "I..."
    GTS "I uh..." 
    GTS "Would it be okay... to kiss you?"
    "My heart suddenly felt like it was connected to a car whose pedal had been floored as my heart rate soared. I felt my face heat up as I gulped slightly and finally turned to face her."
    "Her face was as scarlet-coated as my own, her eyes avoiding contact with mine. They would, however, quickly glance at me once as she waited for my answer."
    #(Will write a no response later)
    MC "Uh... y-yes, it um... would be okay..."
    "I felt like an idiot for being unable to just say what I wanted to say. I saw her close her eyes as she leaned into me. My eyes noticing her hands clenching and slightly shaking, and she flinched once I actually moved."
    "There was a moment of pause however, as Naomi’s nose bumped my forehead, causing me to smirk as in our anxiety we failed to make the necessary height adjustment."
    GTS "S-sorry..."
    MC "It's okay."
    "Reaching up, I placed my hand on her cheek as I guided her until our lips met. She was soft and warm, tender and timid as she tried not to press against me, but also feared pulling away."
    "I felt her tense up, then relax, only to tense once more as she seemed scared to ruin the kiss. My thumb gently caressed her cheek, and soon her tension eased away. We allowed ourselves to enjoy this, rather than let fear mess it up."
    "We stayed like this for merely a few seconds before I finally moved back. Her eyes opened, and while she was still deeply red, I saw the warmest smile form as her eyes looked directly into my own."
    show GTS happy
    "Her joy coaxed out my own as I smiled in response to hers. We didn't talk again, instead we looked back out into the sunset as she leaned back into me once more. This time however, I felt her gentle hand rest upon mine."
    "Softly, I shifted my hand and took what of hers I could within its grasp. Squeezing her hand tenderly, we enjoyed the view until the sun vanished behind the horizon."
    jump daymenu

label GTS028T:
    $setProgress("GTS", "GTS030")
    scene Theater with fade
    play music Peaceful
    "I scanned the various posters that decorated the inside of the theater, wondering what might be good. Naomi leaned down slightly to get a closer look at the posters as well."
    show GTS neutral at Position(xpos=0.8, xanchor=0.5, yanchor=1.0) with dissolve
    GTS "I like the artwork used in some of these posters."
    MC "Yeah, I like it when the poster is more than just a character standing in the center with the title on them. "
    show GTS surprised
    GTS "Oh, this one reminds me of those ancient paintings you’d see in a museum."
    show Ryoko happy at Position(xpos=0.4, xanchor=0.5, yanchor=1.0) with dissolve
    Ryoko "That’s Koichi: A battle of love and honor. It’s a period piece. Also hey you two!"
    show Minori neutral at center with dissolve
    Minori "Good afternoon. I hope we didn’t keep you two waiting long."
    "Naomi gave a small bow in greetings as Ryoko and Minori waved."
    MC "Not at all, we got here only a couple of minutes ago."
    show Ryoko neutral
    Ryoko "Great! I wasn’t sure what you’d all like to watch so I picked a time that I knew would have a couple of movies starting in a relatively soonish time. So we could discuss what we want to see."
    MC "But what if we can’t agree on any of the choices?"
    Ryoko "Well… then I didn’t plan this out properly heh."
    Minori "As ill planned as that was, I’m sure we’ll agree on one of the choices we have to choose from."
    MC "Alright, we do we have then?"
    Ryoko "We have The Last Call, a horror movie about patrons in a bar learning they’re stuck in a bar with ghosts. There’s Koichi, which is a period piece of a man fighting for his stolen love after being dishonored by the murder of his master. And then there’s My Lover, My Sister!? A comedy which is about a guy who learns that the lady he’s been dating is actually his sister in law."
    show Naomi embarrassed
    GTS "I’m… not sure how I feel about those other two…"
    Ryoko "So those are our choices people, which would you like to see?"
    Minori "Hm, I could go for a fun comedy."
    GTS "I’m rather curious about Koichi."
    Ryoko "And I’ve been meaning to watch The Last Call. Well Hotsure-san, what’s it gonna be?"
    MC "Great… Um…"
    menu:
        "I think a comedy is a safe choice since we don’t know how the others will be.": # -1 Affection
            jump GTS028T_c1_1
        "Koichi sounds like it can be pretty cool. I haven’t watched many ronin movies.": # +1 Affection
            jump GTS028T_c1_2
        "I’m not gonna lie, I’m interested to see how drunk people deal with a ghost.": # -2 Affection
            jump GTS028T_c1_3

label GTS028T_c1_1:
    $setFlag("GTS028T_c1_1")
    MC "I think a comedy is a safe choice since we don’t know how the others will be."
    show Ryoko happy
    Ryoko "It’s like my teacher always said, 'If you don’t know what to watch, go with the jokes.'"
    $setAffection("GTS", -1)
    show GTS sad
    GTS "I hope it’s not too vulgar…"
    Minori "Don’t worry Yamazaki-san, I wouldn’t pick something if I thought it’d bother anyone too much."
    jump GTS028T_c1_after

label GTS028T_c1_2:
    $setFlag("GTS028T_c1_2")
    MC "Koichi sounds like it can be pretty cool. I haven’t watched many ronin movies."
    Ryoko "It’s pretty great, I’m sure you’ll enjoy it."
    GTS "You’ve already seen it Tanaka-san?"
    show Ryoko happy
    Ryoko "Of course! But don’t worry I won’t spoil anything."
    Minori "It’s not uncommon for Tanaka-san to see a movie multiple times at the theater."
    Ryoko "Nope! Sometimes the second viewing is when you really get the whole story."
    GTS "Is that so?"
    Ryoko "Totally! Give it a shot some time. You may find you like a movie even more when you give it another watch."
    jump GTS028T_c1_after

label GTS028T_c1_3:
    $setFlag("GTS028T_c1_3")
    MC "I’m not gonna lie, I’m interested to see how drunk people deal with a ghost."
    show Ryoko happy
    Ryoko "It’s sure to be pretty funny I think."
    show GTS sad
    GTS "…"
    Minori "What’s the matter Yamazaki-san?"
    GTS "N-nothing…"
    Minori "Are you worried it might be too scary?"
    GTS "…"
    MC "Yamazaki-san, if you don’t want to see it we can pick something else."
    $setAffection("GTS", -2)
    GTS "N-no… it’s okay. I’ll be okay…"
    MC "If you say so…"
    show Ryoko neutral
    Ryoko "Don’t worry Yamazaki-san, it won’t be too bad. I promise."
    jump GTS028T_c1_after

label GTS028T_c1_after:
    show Ryoko neutral
    Ryoko "Come on, let's go get the tickets."
    "Ryoko lead us to the box office where she ordered the appropriate tickets but we still had a little time to kill. We moved over to a small seating area where Naomi took a seat, which I couldn’t help notice bought her at equal height to the rest of us."
    MC "Did you go to the movies often when you were younger?"
    show GTS neutral
    GTS "No, not really. We saw maybe two or three films a year."
    show Ryoko surprised
    Ryoko "Are you serious!? I see a movie a week! I couldn't imagine starving myself on film like that."
    Minori "She's not exaggerating. Tanaka-san makes sure she always has time to go to the theater at least once during the weekend. To the detriment of her funds."
    show Ryoko annoyed
    Ryoko "It's not that bad."
    MC "Was there any reason your parents didn't take you often?"
    GTS "Hm, I would say it's because my father has a preference for live art. So we saw plays mostly."
    show Ryoko neutral
    Ryoko "Oh, I see. Supporting the enemy huh?"
    show GTS embarrassed
    GTS "E-Enemy?"
    Ryoko "Movies have a lot of rivals, live theatre being one of them."
    Minori "If I may interject, I would say online video sites are probably the biggest threat."
    Ryoko "Also true!"
    GTS "I-I’m sorr`y..?"
    MC "Don't worry Yamazaki-san, She's just playing it up. Though I can't say I've gone to many plays or musicals."
    Minori "Unfortunately I haven't as well."
    Ryoko "Yeah, I already spend enough on movies. Live shows are far too costly for me to support both."
    show GTS neutral
    GTS "I can see how that could be an issue. I wouldn't say we went often, but I think that's what made it a bit more special."
    GTS "Unlike movies which come out each week, live performances are rarer. My family made an event out of going to them. There's also something special about seeing a play. You know the actors have truly honed their craft for they have to be at top form every single night. Where I feel movies have it a bit easier since they get the benefit of multiple attempts and we only see the one take that was used. I wouldn't say movie actors have it easier, just that it's not the same I suppose."
    show GTS embarrassed
    GTS "Ah! I'm sorry."
    MC "Huh? Why?"
    GTS "That was incredibly rude of me. I wasn't attempting to demote the merits of films over plays. I hope I didn't offend you Tanaka-san and Tomoe-san. Apologies."
    show Ryoko happy
    Ryoko "Haha, no offense taken. It’s just your opinion Yamazaki-san. No harm in sharing it."
    show Minori happy
    Minori "Indeed, and I would agree with your point. Stage actors truly go through the gauntlet for every single one of their performances. That's no small task."
    Ryoko "Yeah, don't sweat it Yamazaki-san. Oh! We forgot the snacks! Don't wait up for us, go get some seats!"
    hide Ryoko with dissolve
    hide Minori with dissolve
    "Ryoko took Minori hand and quickly vanished towards the concession stand as I chuckled and looked back at Naomi who seemed a little bothered."
    show GTS sad at center with dissolve
    GTS "I truly hope I didn't offend her."
    MC "Nah, I'm sure she's perfectly fine Yamazaki-san. I mean, you didn't say anything harsh."
    GTS "Still. This is her passion and it's not my place to question its merits."
    MC "Yamazaki-san, I think you're just overthinking things. Tanaka-san and Tomoe-san are fine, people have preferences and it's perfectly okay. Trust me, you didn't do anything wrong. Come on, let's go find some seats."
    "I offered her my hand which she gently grasped with a smile. As we entered the proper theater, I scanned the available seats and smiled at finding some great seats in the middle."
    "However I quickly remembered something. Looking up at Naomi, I had to account for her height and resumed looking for seats, but now focusing entirely on the back row."
    "We found some decent seats in the back corner, nothing great but it'd have to do. It did offer Naomi a place to sit that wouldn't disturb others though and I'm sure that's all she wanted as we took our seats."
    MC "There we go, this should allow us to fully see the screen without any distractions. Are these fine with you?"
    show GTS neutral
    GTS "Yes they're perfectly fine Hotsure-san. Thank you."
    "We sat there for a few moments as I began to wonder where Ryoko and Minori were until I finally spotted them entering theater. I waved to catch their attention but their response caught me off guard."
    "Ryoko merely winked at me while Minori’s smile widened. The two taking their snacks and wandering to a different section of the room. Leaving me and Naomi alone."
    scene black with fade
    if getFlag("GTS028T_c1_1"):
        "The movie started out rather surprisingly as a sex scene was the first scene to greet us. I felt Naomi tense up as it might have been a little much for her. Still, once the scene pass and the movie continued she ended up relaxing and laughing quite a few times. I felt her hand move a couple of times as it seemed she was trying to muffle her laughing to not be rude. However one time when her hand settled back down, it laid on top of mine."
        "Blushing lightly, I wasn’t sure if I should mention it as her hand completely covered mine. Once I noticed her softly squeeze it, I finally looked up towards her and saw her smiling which in turn made my lips smile. She laughed more openly as the film progressed and so did I, as I moved my hand so it could hold hers."
    elif getFlag("GTS028T_c1_2"):
        "The movie opened on a long lingering shot of a quiet field of flowers. Their colors muted as the sky itself was gray. The drama that would soon play out captivated us, as I could see Naomi lean closer to as got lost in the film. She’d gasp when the action picked up, awe at set pieces, and when the ronin found his love she’d clutch my hand softly."
        "I was caught by surprise when she did that, looking up at her as she looked back down at me and smiled. My cheeks grew a little warm though, as while we looked at each other the ronin spoke all his loving feelings. Sensing my nervousness, she ended up blushing as well and looked away, though her smile remained as did her hand for the remainder of the film."
    else:
        "The movie began innocently enough, a brief scene to establish all the characters and their reasons for drinking that night. There was minor tension and suspense the entire time though, yet nothing really happened for quite some time. This seem to leave Naomi feeling a little more comfortable as it seemed it might not be too bad. But then just like that, the first major scare happened and Naomi let out a startled yelp."
        "The noise resulting in some others in the audience to snicker and laugh which resulted in her embarrassment. Her body remained tense the rest of the film as my chair shook a little from her shaking. She was leaning back, as if providing distance would result in protection. Frowning, I gently placed my hand on her which made her flinch but then look down to see me. I squeezed her hand to let her know I was there. And she squeezed back and held my hand for the rest of the movie, squeezing it whenever she was startled. Granted… maybe that wasn’t the best thing as I learned that with her added height, Naomi was stronger than normal too..."
    jump daymenu

label GTS030:
    "This marks the current end of Naomi's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance