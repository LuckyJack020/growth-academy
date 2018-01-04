define GTS = Character('Naomi', color="#66FF33")
define Vendor = Character('Vendor', color="#FFFFFF")
define LittleGirl = Character('Little Girl', color="#FF91DC")
define Ryoko = Character('Ryoko', color="#FF91DC")

image GTS neutral = ConditionSwitch(
    "gametime > datelibrary['GTS_size_2']", "Graphics/GTS-2-neutral.png",
    "True", "Graphics/GTS-1-neutral.png")
image GTS happy = ConditionSwitch(
    "gametime > datelibrary['GTS_size_2']", "Graphics/GTS-2-happy.png",
    "True", "Graphics/GTS-1-happy.png")
image GTS sad = ConditionSwitch(
    "gametime > datelibrary['GTS_size_2']", "Graphics/GTS-2-sad.png",
    "True", "Graphics/GTS-1-sad.png")
image GTS surprised = ConditionSwitch(
    "gametime > datelibrary['GTS_size_2']", "Graphics/GTS-2-surprised.png",
    "True", "Graphics/GTS-1-surprised.png")
image GTS angry = ConditionSwitch(
    "gametime > datelibrary['GTS_size_2']", "Graphics/GTS-2-angry.png",
    "True", "Graphics/GTS-1-angry.png")
image GTS aroused = ConditionSwitch(
    "gametime > datelibrary['GTS_size_2']", "Graphics/GTS-2-aroused.png",
    "True", "Graphics/GTS-1-aroused.png")
image GTS embarassed = ConditionSwitch(
    "gametime > datelibrary['GTS_size_2']", "Graphics/GTS-2-embarassed.png",
    "True", "Graphics/GTS-1-embarassed.png")

image Dorm GTS = "Graphics/dorminterior.png"

init 2 python:
    datelibrary['GTS_size_6'] = datetime.date(2005, 12, 10)
    datelibrary['GTS_size_5'] = datetime.date(2005, 12, 10)
    datelibrary['GTS_size_4'] = datetime.date(2005, 12, 10)
    datelibrary['GTS_size_3'] = datetime.date(2005, 12, 10)
    datelibrary['GTS_size_2'] = datetime.date(2005, 4, 14)
    datelibrary['GTS009_date'] = datetime.date(2005, 4, 10)
    datelibrary['GTS011_date'] = datetime.date(2005, 4, 21)
    
    eventlibrary['GTS001'] = {"name": "GTS001", "girls": ["GTS"], "location": "schoolplanter", "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.EQUALS, datelibrary["day_1"]]], "priority": 1}
    eventlibrary['GTS002'] = {"name": "GTS002", "girls": ["GTS"], "location": "schoolplanter", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.LESSTHAN, datelibrary["testday"]]], "priority": 0}
    eventlibrary['GTS003'] = {"name": "GTS003", "girls": ["GTS"], "location": "cafeteria", "conditions": [[ConditionEnum.ISDAYTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.LESSTHAN, datelibrary["GTS_size_2"]]], "priority": 0}
    eventlibrary['GTS004'] = {"name": "GTS004", "girls": ["GTS"], "location": "library", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.LESSTHAN, datelibrary["GTS_size_2"]]], "priority": 0}
    eventlibrary['GTS005'] = {"name": "GTS005", "girls": ["GTS"], "location": "schoolplanter", "conditions": [[ConditionEnum.PRESET]], "priority": 0}
    eventlibrary['GTS006'] = {"name": "GTS006", "girls": ["GTS"], "location": "schoolfront", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.LESSTHAN, datelibrary["GTS_size_2"]]], "priority": 0}
    eventlibrary['GTS007'] = {"name": "GTS007", "girls": ["GTS"], "location": "campuscenter", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.NOEVENT, "GTS009"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.LESSTHAN, datelibrary["GTS_size_2"]]], "priority": 0}
    eventlibrary['GTS008'] = {"name": "GTS008", "girls": ["GTS"], "location": "roof", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]], [ConditionEnum.GAMETIME, ConditionEqualityEnum.LESSTHAN, datelibrary["GTS_size_2"]]], "priority": 0}
    eventlibrary['GTS009'] = {"name": "GTS009", "girls": ["GTS", "BE"], "location": "festival", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.EVENT, "GTS008"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["GTS009_date"]], [ConditionEnum.GAMETIME, ConditionEqualityEnum.LESSTHAN, datelibrary["GTS_size_2"]]], "priority": 0}
    eventlibrary['GTS010'] = {"name": "GTS010", "girls": ["GTS"], "location": "classroom", "conditions": [[ConditionEnum.ISDAYTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["GTS_size_2"]]], "priority": 1}
    eventlibrary['GTS011'] = {"name": "GTS011", "girls": ["GTS"], "location": "dormexterior", "conditions": [[ConditionEnum.ISDAYTIME], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["GTS011_date"]], [ConditionEnum.FLAG, "GTS011_unlock"]], "priority": 0}
    eventlibrary['GTS012'] = {"name": "GTS012", "girls": ["GTS"], "location": "dormexterior", "conditions": [[ConditionEnum.ISNIGHTTIME], [ConditionEnum.EVENT, "GTS011"]], "priority": 0}
    
label GTS001:
    scene black with fade
    "The words from Tashi-Sensei stayed with me long after class had concluded. I just wasn't sure how to properly process what we were told."
    "What Daichi had told me earlier was starting to resonate more, and I began to wonder if perhaps others knew about the purpose of this school before they were enrolled into it."
    scene School Planter with fade
    "I hadn't realized how long I was lost in my own thoughts until I finally noticed my surroundings; I was at the school's garden."
    "It was nice here, the breeze along with the sounds of leaves and grass moved by the flow of wind had a sort of calming factor to them."
    "I stood there for a few moments longer until a figure walked beside me, catching me by surprise."
    show GTS neutral with dissolve
    MC "Huh? Oh, Yamazaki-san. sorry, I wasn't aware you were here."
    GTS "It's all right Hotsure-san. I shouldn't have intruded unannounced."
    "She stood there, smiling ever so slightly, the flow of wind causing her long hair to dance tenderly until I decided to break the silence."
    MC "So what are you doing here in the garden?"
    GTS "Oh, I merely wanted to spend a little more time here. Reflect on my thoughts and think about how the day went so far."
    MC "I see... Were you also possibly thinking about what Tashi-sensei told us earlier?"
    GTS "A little yes, I think many of the students are. Were you as well?"
    MC "Yeah I was. It really came out of left field so I guess I needed some time to think about it."
    menu:
        "What do you think about it?":
            jump GTS001_c1
        "I'm curous about what changes I might go through...":
            jump GTS001_c2
        "I'm concerned about what that might mean for my little sister honestly.":
            jump GTS001_c3
            
label GTS001_c1:
    GTS "It's a little concerning I will admit; however, I think some of those feelings come from the sudden nature in which we were told."
    GTS "I'm sure if we take more time to process it and reflect on it, the situation won't feel as frightening as it possibly does for some."
    extend " Thank you for asking though."
    MC "No problem, we're in this together after all, right?"
    GTS "An interesting way to put it, but indeed I would say so."
    jump GTS001_after

label GTS001_c2:
    GTS "It's good to see you're looking at the news with more curiosity rather than concern. It'd be rather pointless to worry about it now, especially without knowing all the facts first."
    extend " I'm sure they have methods to tell what will be changing in us, though I'm sure with some students it'd be more obvious than others."
    show GTS embarassed
    GTS " Oh, I'm sorry! That sounded rather rude didn't it? I don't mean to judge any of the other students."
    MC "Heh, it's okay Yamazaki-san, I can tell you're not the type to do that."
    show GTS neutral
    GTS "Thank goodness, I wouldn't want to start making the wrong impressions on the first day of school, after all."
    jump GTS001_after

label GTS001_c3:
    $setAffection("GTS", 1)
    GTS "Oh? You have a younger sister, Hotsure-san?"
    MC "Yeah, she's going to school here too."
    extend " I'm just thinking about what Sensei said, about how sometimes siblings are transferred to this school simply because of the results of the other."
    MC "I'm sure I can cope with whatever might happen to me, but I'm worried about her. I just don't want her to go through something that might hurt her."
    GTS "It's only natural to worry as the older sibling Hotsure-san, but you mustn't let it concern you too much. There's no way to know for certain at the moment, so it's best to just be hopeful and keep your chin up."
    MC "Yeah I guess that's true. Sorry for sounding like a mother hen here."
    GTS "It's not worth worrying about, Hotsure-san, like I mentioned it's just natural to feel that way. I know I'm very much the same with my own sister."
    MC "You have a sister too?"
    GTS "Yes, she's much younger though so there's no worry about her predicament in this situation. But just know that you're not the only one who can sometimes come off as a mother hen."
    jump GTS001_after

label GTS001_after:
    "She gave a soft chuckle and kept her warm smile."
    "I guess she must have noticed me staring, because she soon chimed in."
    show GTS embarassed
    GTS "It's quite rude to stare."
    "There was a hint of red on her cheeks as she said that."
    MC "O-Oh! Sorry... I was just thinking again, haha... So, are you going to be doing anything else later today?"
    show GTS neutral
    "She placed a finger on her lip as she thought about her plans for the evening, before finally replying."
    GTS "Well, I had planned to return to my dorm room so I could tell my family about how my first day went. I just wanted to see the garden a little bit before I did so."
    GTS "However, I do plan to explore the garden later this evening. There's a surprisingly large variety of flowers her. At least, more than I would expect, so I want to make a mental list of what's here and maybe ask the groundskeeper about where they obtained the seeds for them."
    MC "Oh, I see; I won't hold you up, then. I should probably do the same myself, really, I'm sure my family would love to hear about how my day went as well. I'll see you around Yamazaki-san."
    GTS "Farewell Hotsure-san, I hope the rest of your day goes well. Do try to visit the garden every so often, you'll be surprised how much good can come from resting in a garden for a few moments."
    MC "Heh, I might take you up on that advice. Later Yamazaki-san."
    "She gave me a small bow before I departed."
    jump daymenu

label GTS002:
    scene School Planter with fade
    "I always found the sky to have quite the alluring palette around late afternoon. Clouds coated in degrees of red that ranged from rose color to pink and even orange and yellow. And while I normally didn't find myself staring up at the sky, it was simply something I couldn't resist as I stepped into the school's garden once more."
    "The breeze had become cooler, but still flowed with a sense of gentleness to it, making some pink colored flowers dance before me. In the distance, I heard a faint voice, and as I turned to look I spied Naomi giving a gracious bow to who I assumed was the gardener."
    MC "Yo Yamazaki-san!"
    show GTS embarassed with dissolve
    "I called out, lifting one arm up to give a slight wave. This seemed to surprise her, as she jumped a little and looked back towards me. Giving a small nod, she walked over with a few small bags held against her bust by her arm."
    GTS "Hello again Hotsure-san, I'm sorry you startled me a little there."
    MC "Heh, sorry. I just wanted to make sure you heard me. I see you talked to the gardener."
    "She blushed very faintly and gave a gentle nod."
    show GTS neutral
    GTS "I did yes, he's quite a nice person to speak to. I was just asking about the flowers and before we knew it we got wrapped up in a rather long conversation about them and other plants. He even gave me some for free."
    "She shifted her arm a little to draw my attention to the three bags she was carrying."
    menu:
        "Oh, that's cool. How did the rest of your day go?":
            jump GTS002_c1
        "Really? That was cool of him. What kind are they?":
            jump GTS002_c2

label GTS002_c1:
    $setAffection("GTS", 1)
    GTS "Hm? Oh, the rest of my day was rather peaceful. I spoke with my family as I mentioned earlier and they seemed rather happy to hear from me."
    MC "That's good to hear, did you happen to mention what you thought about the news we got earlier?"
    "She was silent for a moment as if reflecting on that question before she answered me."
    GTS "No, I didn't. I don't see a reason to mention it to them. Without any knowledge, all it'd accomplish is make them worry about me needlessly. I will be sure to discuss my feelings about it to them when we learn more about it ourselves and I know exactly what to expect."
    MC "Yeah I guess that's true... So, did you do anything else?"
    "She shook her head softly."
    GTS "No, not much else really. Basically, just made sure everything was completely unpacked and organized. Then I came here and well you know where that part leads."
    jump GTS002_after
    
label GTS002_c2:
    $setAffection("GTS", 2)
    $setSkill("Art", 1)
    $setFlag("GTS008_flowers")
    "Her eyes brightened ever so slightly at that question as her smile grew a little larger."
    show GTS happy
    GTS "Indeed, it was rather nice of him. Well as for the flowers themselves. These ones are Burūberu (Bluebells), a lovely plant with quite the bold color. They're known to symbolize gratefulness."
    "She handed the bag to me, allowing me to see the blue bell-like shape they had on the cover."
    GTS "Now this breed here is the Tsutsuji (Azalea) which you might have seen here at the garden."
    "She pointed over to the pink flowers I had seen when I first entered the garden, the second look allowing me to notice the purplish patterns within the petals of the flower."
    GTS "They're popular here in Japan with a flower festival which showcases them in Motoyama taking place each year on March 25th. They're known to symbolize patience and modesty."
    "She handed me this bag as well, as I was soon finding myself carrying her flowers for her."
    GTS "Now these last ones may seem rather plain due to their simple color, but you'll be surprised the amount of color variety you'll find with Anemones. Though the white ones are the ones you'll usually find here in Japan. Their name is Greek, meaning 'Daughter of the Wind' and they represent sincerity."
    "As she handed me the last bag, which displayed white, five-petaled flowers I could see her smiling warmly as she finished explaining."
    MC "Heh, I can tell you really have a thing for flowers, huh?"
    "Her smiled quickly vanished and instead a light blush formed across her cheeks."
    show GTS embarassed
    GTS "O-oh yes, indeed I do. Sorry for getting rather carried away there. I didn't mean to just ramble on like that. I surely hope you don't mind."
    MC "Not at all, it's nice to learn a little bit about you, really. I also admit it was interesting to learn a bit about these flowers as well, I wasn't aware they have hidden symbolic meanings."
    "She continued to smile, but became more reserved, as if to not allow herself to accidentally get too excited again."
    show GTS neutral
    GTS "They do yes, but I wouldn't want to take up more of your time chattering about my interests."
    jump GTS002_after
    
label GTS002_after:
    GTS "How did the rest of your afternoon go, if you don't mind my asking?"
    MC "Taking what we learned about ourselves earlier aside, the rest of my afternoon was actually pretty good. I spoke with my family and told them I'm fine. I then took some time to learn a bit more about the school, and found out there are several sports clubs. I might give them a look and see if I can join in the future."
    "She nodded her head as I spoke to her, taking in everything I was saying attentively. It felt rather nice honestly, knowing that she was truly listening to me as she kept eye contact with me during the entirety of my small ramble."
    GTS "What sport are you interested in Hotsure-san?"
    MC "Oh, I'm rather interested in Soccer. I might give it a shot later this year if my condition doesn't hinder it in some way."
    "I chuckled lightly, kind of realizing that we couldn't plan our futures for the moment. Without any knowledge about what might happen to us, everything was up in the air. I pushed that thought to the back of my mind though."
    GTS "Hopefully you'll be able to do so Hotsure-san. Soccer has always seemed like a rather enjoyable sport, a lot of endurance needed so it's good exercise. I wish you luck Hotsure-san."
    "She gave me another soft warm smile that made me smile in return as I scratched the back of my head."
    MC "Heh, Thanks. Well it's getting rather late and I don't want to keep you from any plans you possibly have with your flowers, so I think I'll be heading off now. Before I go though, do you need any help with those?"
    "I asked, pointing to the small bags of seeds she had with her. This caused her to give the slightest of giggles as she shook her head lightly."
    GTS "No, I'm okay thank you. It was nice speaking with you again though Hotsure-san. Hopefully we'll talk again soon."
    MC "Yeah, hopefully. I'll catch you later, Yamazaki-san."
    GTS "Have a pleasant evening, Hotsure-san."
    "She replied before once again giving me a light bow, yet this time it was her who left first. I couldn't help but smile at the small conversation we had, slightly curious about where I might bump into her again."
    jump daymenu

label GTS003:
    scene Cafeteria with fade
    "The morning found itself to be quite the chaotic time, as many students rushed down the corridors to make it to the cafeteria in time to beat the morning rush. This didn't really pressure me to speed up my stride, however."
    "When I finally arrived to the cafeteria I saw that it was surprisingly calmer than what was transpiring throughout the hallways. I got in line behind a few other students who were getting their breakfast, which allowed me time to properly examine what was on the menu."
    "I will admit I was rather surprised by what I saw. There were tray after tray of warm food prepared for us. A lot of which just looked heavenly to the eyes and must have tasted wonderful."
    "Not wishing to hold up the line though, I quickly grabbed what I felt would be a decent quick breakfast, getting some steamed rice, a rolled omelette, and a small bowl of miso soup. I thanked the cooks before searching for a place to sit."
    "There was a good amount of unfamiliar faces among those sitting at various tables, but one face was rather familiar. Sitting down with a slight smile, I spoke to my neighbor."
    show GTS neutral with dissolve
    MC "Hey there, Yamazaki-san. Nice to see someone I know here."
    "I must have startled her, as she flinched slightly and looked up at me."
    GTS "Good morning Hotsure-san. I hope you're having a pleasant day so far."
    "Her hands gently repositioning her utensils and her napkin in an extremely orderly fashion before wiping her hands off with a moist towelette. She then looked at me, as if to give me a hint until I realized what I'd forgotten."
    MC "Oh! Uh, itadakimasu."
    show GTS happy
    GTS "Itadakimasu."
    MC "Yeah it's been a pretty good morning so far, I managed to wake early so it gave just the right amount of time to fully wake up, which is a pretty good start of the day in my opinion. Thankfully since I woke up so early it allowed me to shower without feeling rushed."
    "I stated with a slight chuckle as she gave a small smile in response before picking up her chopsticks. Her hand softly slid her hair back as she picked up some cooked vegetables to eat, letting me see that her other bang was currently held back by a flower-shaped hairclip."
    "I had no idea what type of flower it was, only knowing that it had 5 white petals in a sort of star configuration."
    MC "How was the start of your day, if you don't mind me asking?"
    "Naomi perked up slightly as I asked my question, taking her napkin to delicately wipe her lips and properly placing it back in place before answering."
    show GTS neutral
    GTS "Myself? Well, I woke up rather early as well and took the time to properly make my bed. I then showered and prepared myself for the rest of the day. Things like properly combing my hair, getting everything organized, and planning out my schedule for the day."
    GTS "I think it's good to take the time in the morning to plan the day, it allows you to optimize the time you spend as well as get your brain working early on in the day."
    MC "I can see that, yeah. Gets the juices flowing and your mind ready for more work."
    "She gave me another small smile as she learned that I agreed with her before she went back to have another piece of her meal."
    "This time I noticed how she used her chopsticks to take an almost perfect rectangular piece out of some of her grilled fish, and then carefully took some steamed rice and place it atop before eating both."
    GTS "Her movements seemed so precise and slightly rigid that it was slightly captivating as I never seen someone eat so strictly."
    menu:
        "That's a cute hairclip, though I'm not sure what type of flower that is. What kind is it?":
            jump GTS003_c1
        "I mean no offense, but you have a very interesting way of eating.":
            jump GTS003_c2

label GTS003_c1:
    $setAffection("GTS", 2)
    $setSkill("Art", 1)
    $setFlag("GTS008_flowers")
    "For the briefest of moments I could see Naomi's cheeks flash a slight crimson in what I assumed was embarrassment as her hand went to touch the accessory. She looked away for a second but returned her eyes back to mine and retrieved that small smile she had before."
    show GTS embarassed
    GTS "Oh, why thank you so much. It's just a little something I decided to add to the rest of my attire for today. I have a bit of a collection of them, various species and things of that nature."
    MC "Well, I think it suits you rather well."
    GTS "Thank you..."
    show GTS neutral
    GTS "As for your question, this flower is a Jasumin (Jasmine) which do tend to confuse some people since they happen to look slightly generic."
    MC "I will admit it does look like what most people picture as a flower in their heads."
    "She gave me a small nod to my remark before continuing."
    GTS "Well Jasumin does come in other forms, like the Grand Duke of Tuscany, which almost resembles a white rose, to those that look much like the one in my hair."
    GTS "China even uses it as an ingredient for their teas."
    MC "Really? Which one?"
    GTS "...Jasmine tea."
    MC "Oh... I guess I should have put that together."
    "I scratched the back of my head, feeling a little silly now, but she didn't seem to mind my mental trip, simply answering me as if it were any other question."
    GTS "They're known to symbolize friendliness and gracefulness."
    MC "Seems like it suits you rather well then."
    "This caused her blush to return once more as her eye contact finally broke to look at her food."
    jump GTS003_after

label GTS003_c2:
    $setAffection("GTS", -1)
    "Her body stiffened up lightly as I brought mention towards her table etiquette as she looked me in the eyes."
    show GTS embarassed
    GTS "How do you mean?"
    MC "I just mean that the way you conduct yourself, it's very precise but also very formal."
    show GTS neutral
    GTS "Well it was how I was raised. It's important for one to keep proper posture and etiquette when eating. You don't want to come off as unintentionally rude, after all."
    MC "Heh, well you don't have to worry so much about being so formal around me. You can relax."
    GTS "I see, I'll keep that in mind, though if you don't mind I would like to move pass the subject."
    MC "Heh... yeah okay. Sorry about that."
    GTS "It's fine."
    jump GTS003_after

label GTS003_after:
    "We ate for a few moments in silence after that. It was rather nice to have someone to eat with, even if we weren't having much of a conversation at the time. As we finished I had decided to ask Naomi something."
    MC "So is there any particular subject you're looking forward to this year?"
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
    "The sun shone highly in the sky as the middle of the day came by, its rays seeping through the many windows that surrounded the vast two-story room. I was honestly a little surprised to see so many people using the campus library."
    "To its credit, both floors seemed absolutely packed with shelves upon shelves of books. Which in turn would make one aisle look like the splitting of the red sea but with books as opposed to water. This didn't mean that every part of the library was stuck in the past as there were a series of smaller rooms that had lines of computers for more convenient research and study."
    "Something else that was rather clear was just the amount of space found between each shelf as it seemed capable of easily fitting six people across the width of the aisle. The reason for this was easy to put together, but it did leave me with the thought of just how large some of the students might become if this was the norm for the school."
    "As I walked among the shelves in search of the right book needed for my Contemporary Society course, I spotted a familiar face at a nearby table."
    show GTS neutral with dissolve
    extend " Naomi was seated with her focus entirely on her book, seeming somewhat perplexed by what she was reading. Unable to resist, I strolled over to Naomi and suddenly spoke up."
    menu:
        "Hey there!":
            jump GTS004_c1
        "(Read over her shoulder)":
            jump GTS004_c2

label GTS004_c1:
    $setAffection("GTS", -1)
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
    GTS "I can't be certain truthfully, but I think it's best to be prepared for it in case it ever happens. It's also a good skill to have if your work might require it or if you might have international guests."
    MC "Heh, that's quite the foresight to have. I barely even think about what I'll be doing in a month from now. Hey, if you manage to make it work though that's one massive advantage you'll have over others in the job market, so good luck!"
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
    MC "Well then. I volunteer!"
    "She quickly put a finger over her lips just as I had remembered we were in the library. Chuckling nervously, I decided to repeat myself in a more subdued fashion."
    MC "Oops. But yeah, I'll be glad to help you out."
    show GTS embarassed
    GTS "Are you sure? I feel bad asking you to take time out of your schedule simply to help me."
    MC "Don't worry, it's fine. Plus, I get to learn more so it'll help me out a lot too."
    show GTS neutral
    GTS "Hmm. Oh, how about I help you with one of our other subjects then? Is there any you think will be an issue?"
    MC "Math. Haha, it's going to be math, I can already tell that's going to be a disaster for me this year."
    "She gave a light giggle, covering her mouth ever so slightly."
    GTS "Well that's something I know I can help you with. Very well then, I accept your help and am pleased you accept mine as well."
    "She extended her hand for me to shake to solidify our agreement. Taking her hand into mine, I gave her a smile and shook."
    MC "Glad to be of assistance study partner. Let's get this done!"
    Student1 "Sssh!"
    "We both tensed up as someone at another table once again reminded me of my surroundings. Naomi was blushing slightly, but neither of us could stop a small giggle from slipping out as we started working more quietly."
    jump daymenu

label GTS005:
    "I wandered about the campus for quite some time after visiting the nurse, the news of my particular condition having left me with a feeling of uncertainty. As I walked, my hand would occasionally reach up to touch the tip of my bangs as I wondered just how quickly they might change."
    scene School Planter with fade
    "As I stepped past the double doors and into the garden, my eyes shut from the blast of sunlight that I was exposed to. After a few seconds my eyes readjusted and I saw Naomi's form kneeling in front of a patch of flowers. Calmly walking over, my footsteps on the path nevertheless alerted her to my presence, and she looked back at me and gave a soft wave."
    show GTS neutral with dissolve
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
    show GTS embarassed
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
    show GTS embarassed
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
    show GTS embarassed
    GTS "I don't rant about flowers... not that much, anyway."
    "We both had a small chuckle as we spent a bit more time just talking in the garden."
    jump daymenu

label GTS006:
    scene School Front with fade
    "There was quite a calming mood to the start of the school day as I wandered near the entrance. Something caught my eye, though, as I saw what appeared to be a small gathering of students near the front gate. Curious, I wandered over, hearing some excited voices and sounds of affection. The reason for this became clear rather quickly, as it seemed a stray Shiba Inu puppy had wandered onto campus."
    Student1 "It's so adorable!"
    Student2 "D'aww! Look at his little paws!"
    "The crowd grew every couple of seconds as more people wanted to see what the commotion was all about. As I kept watching, I saw a familiar figure kneel next to the excited puppy and begin petting it. Naomi held a warm smile on her face as her hand massaged the puppy's ears and even rolled him over to rub his belly. This caused the entire crowd to gush over the cuteness and I couldn't resist a smirk."
    "A little time passed before the dog's owner finally showed up and thanked everyone for finding their dog before taking it back home. As the crowd dispersed I saw Naomi walk by and notice me. Giving me her trademark smile she gave me a small wave of her hand."
    show GTS happy with dissolve
    GTS "Hello Hotsure-san, did you see the adorable Shiba Inu that had wandered onto campus?"
    MC "Yeah, I did! Well, I saw the crowd first and had to see what was up."
    GTS "It was such a cute puppy, and very well behaved. Didn't you think so?"
    menu:
        "Kind of, but I'm mostly into cats myself.":
            jump GTS006_c1
        "Yeah, he was extremely cute!":
            jump GTS006_c2

label GTS006_c1:
    MC "Kind of, but I'm mostly into cats myself."
    show GTS neutral
    GTS "I see, well cats are rather adorable too. Though I always enjoyed the companionship of a dog."
    MC "Yeah, I hear a lot of people are a big fan of how loyal dogs can be. Personally, I enjoy the peace and quiet a cat offers. Plus, they're so cute!"
    "Naomi gave a little giggle and covered her mouth at that last bit but nodded her head."
    show GTS happy
    GTS "Sorry, I didn't mean to laugh, it's just rather cute seeing that."
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
    "There was the faintest hint of a blush on Naomi's face as she broke eye contact and looked to the side for a second, before returning her attention."
    show GTS embarassed
    GTS "My father always said he picked that breed because the Hokkaido has the three characteristic he looks for in people, bravery, loyalty, and intelligence. I can say he was right about that description, because she's probably been one of the most loyal dogs I've met."
    MC "She? So it's a girl."
    GTS "Oh yes! Sorry, yes she's a girl. Her name is Kimiko and she has wonderfully white fur. She's been with the family for about five years now."
    MC "I see, that's pretty cool. I bet you can't wait to see them again."
    GTS "Yes, I do miss her a bit more than I thought, but I plan on heading home this weekend, so I'll be seeing her soon enough."
    MC "That's good to hear. Hmm, I wonder if I can plan a trip back home at some point too."
    GTS "Small breaks from school can do the mind a lot of good."
    MC "Yeah, especially with what we will be dealing with here over time. Yeah, maybe I'll pay home a visit sometime soon."
    "I got a small understanding nod from Naomi and an equally small yet warm smile."
    GTS "If you'll pardon me Hotsure-san. I believe we're already close to being late for class. It might be best to start heading to our home room."
    "I quickly looked at my watch and then chuckled."
    MC "Oh yeah... heh, I kind of lost track of time. Yeah let's get going. Maybe if I'm lucky I'll get a chance to see that puppy again someday."
    GTS "Maybe."
    "With a small giggle from Naomi, we began walking to class together."
    jump daymenu

label GTS007:
    scene Campus Center with fade
    "Petals danced in the breeze, carried aloft by the wind. They flowed peacefully down the pathway, where I saw a familiar figure sitting underneath the shade of a tree. Naomi's hair moved much like the flower petals had, as I noticed a paper in her hand."
    MC "Hey there Yamazaki-san, how are things?"
    "She looked up from what appeared to be a letter when I called out to her, and gave me a gentle wave of her hand."
    show GTS neutral with dissolve
    GTS "Hello Hotsure-san, I was merely reading a letter my mother sent me. How are you?"
    MC "I've been pretty good for the most part. Also, a letter? Hand-written? I'm surprised people still make those."
    "A faint smile crossed her face as she folded up the letter and placed it back into the envelope."
    GTS "Yes, they seem to not be in style much anymore; however, my mother greatly enjoys writing, so it's become sort of a thing she does for those living far from home."
    MC "That's pretty cool, I bet the post office loves having actual mail to give out that aren't just bills or packages people ordered online. That's a neat little post card too, where is it a picture of?"
    "She looked down at the postcard in her hand that had come with the letter and lifted it towards me, showing a picture of Kyoto."
    MC "Oh hey, it's Kyoto. I thought I recognized that tower there. Is that where you're from?"
    GTS "Yes, I am."
    MC "Interesting. I've never been to Kyoto but it always looked like a pretty neat place. I've heard that it's one of the best places to go for food too."
    "There was the faintest smirk out of Naomi as her smile grew a little, giving a nod of acknowledgement as I sat down beside her."
    GTS "Yes, Kyoto is very well known for its cuisine. Specifically, our tofu and Kaiseki cuisine."
    GTS "My friends and I would often make a weekly activity to visit a new restaurant every weekend. It was rather fun and gave me a deep appreciation for my hometown. It lets you explore more, and sometimes you find little underappreciated establishments."
    MC "Wow, that's sounds like it'd be cool to do. Though it also sounds like it would be pretty heavy on the wallet after a while, wouldn't it?"
    GTS "Some places were more expensive than others, yes, but you'd be surprised by some of the places you find. Every now and then, we'd stumble across a place that not only had great dishes, but were also offered at a reasonable price."
    GTS "Heh, we had really expanded our list of places we could socialize. We had a bad habit of constantly claiming new spots as our favorite, only to then change it again a couple weeks later."
    MC "Heh, that doesn't sound like quite the bad habit to have, though now I'm trying to think if I ever did anything like that. I mean, I think I did a normal amount of exploring but it was never too extensive. Granted, it might simply be because how crowded it often got where I'm from."
    GTS "Where are you from if you don't mind my asking?"
    MC "Oh, I'm from Tokyo. The big city, Gojira's favorite playground."
    MC "But yeah, I lived in Tokyo. Just a little bit off of Shibuya."
    GTS "Oh wow, that must have been something. Being so close to the center of all the action, you must have seen and experienced some rather interesting things."
    MC "Yeah quite a bit, especially during the holidays when all the tourists take over the streets. You basically turn an already crowded intersection into a literal impenetrable wall of humans. I felt bad for the people driving because well... they weren't going anywhere for quite a long while."
    GTS "I do hope you were careful during those times. I've heard stories of how overwhelming Shibuya can get during the holidays, as well as some of the nastier incidents that can take place due to so many people there."
    MC "Yeah, I was okay, I knew well enough to not get too absorbed into the larger crowds, and kept away from people who could have looked like trouble. Plus it's always good to have a couple of friends with you, makes some of the trouble makers think twice before starting anything."
    MC "That's just Shibuya during the big times of the year though, how about Kyoto? Does it get as crowded as Tokyo?"
    GTS "Well it would depend on the time of year I suppose. It's very much like any big city I would imagine, but I do know that around Christmas time restaurants tend to start charging more for meals, sometimes even doubling the prices of their dishes."
    MC "Because of all the people, I assume?"
    GTS "I believe so, though if I recall correctly a lot of people see Christmas as a big date night event, at least in Kyoto."
    GTS "I recall many of my friends going out on dates to places like La Part Dieu, which is this wonderful French restaurant, or they go to Daimaru to visit the stores and see the decorations."
    MC "Heh, then I bet they saved up all year long for that night, if it's as expensive as you say it is. I can't say I've ever found myself in a scenario like that, though. Which is probably for the best, because I don't know any fancy places to eat. But how about you? Did you ever do anything with someone special?"
    "Naomi's cheeks turned quite the adorable shade of red as her composure broke and she looked down at her letter."
    show GTS embarassed
    GTS "M-me!? Oh no, I never have... I was always too focused on other things like helping around the house or preparing for other social events. I've never really had time for things like that."
    MC "Oh? So, are you telling me you've never been on a date then?"
    "I could see her face brightening up more as she tried avoiding eye contact. It was rather sweet seeing this side of her."
    GTS "I'll admit... that I have not. My schedule was and to an extent, still is, rather filled up with my responsibilities. It would have been nice to have seen what it was like, but it simply wasn't the right time I suppose."
    show GTS neutral
    "She looked back towards me as she managed to regain her composure. I gave her a small nod, as I didn't want to push the issue too hard."
    MC "Yeah, I guess it would be pretty tough if you're always busy. But at the same time, I wouldn't worry too much about it. It's like adults always told us, 'You're young, there's still plenty of time to fool around.'"
    MC "Going back to hanging out with friends, have you managed to make any new friends here?"
    GTS "No, not really, it's been a chaotic time for many people trying to get settled in, so I try not to impose on them. I'm sure in the next couple of weeks, more people will open up and everything will fall back into a normal flow."
    GTS "Maybe then it'll be a bit easier to introduce myself to more people."
    MC "Well, if it's okay for me to throw out there, you could hang out with me and some of my friends at some point. Can't promise you'll hit it out of the park in the first couple of minutes but it's worth a shot, right?"
    GTS "Hm... Would it be okay if I took a little time to figure out my schedule before giving you an answer, Hotsure-san?"
    MC "Heh, yeah, it's okay Yamazaki-san. We're still young after all, so take your time."
    "I gave her a small chuckle, and she returned a smile and a nod. I leaned back a little, enjoying the calm of the garden as well as the gentle breeze, the two of us remaining silent for quite some time after that. Not that I'm complaining, since it was probably the most peaceful I'd felt in quite some time."
    jump daymenu
    
label GTS008:
    scene Roof with fade
    "My footsteps echoed up the stairwell as I ascended to the peak. Upon opening the door, a wave of warm sunlight bathed over me."
    "As my eyes adjusted and I stepped out onto the school roof, I scanned the area to see if Honoka might be around. There were a small number of students hanging out and chatting but no sign of Honoka."
    "I didn't call out her name, but I did walk around to see if she might be around the stairway entrance. Surprisingly it wasn't Honoka I found, but Naomi."
    "She had laid out a blanket and was currently sipping on some tea as what looked like a miniature garden sat in front of her, taking up a small portion of rooftop."
    MC "What do we have here? A secret garden?"
    show GTS neutral with dissolve
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
    GTS "Any plant will do I suppose, but I want to make it something unique and special. I'm just not sure exactly what that should be though. I'll need to give it more thought."
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
    GTS "Apologies, but you mentioned cooperation and that made me think about Bijozakuras (Verbena)."
    MC "Bijozakuras?"
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
    MC "I know I asked before, but Honoka and I are going to a festival in a couple of days. Would you like to join us?"
    GTS "Oh? I wasn't aware one was happening so soon."
    MC "Yeah, it's been so hectic here lately I'm not sure many of the students were aware either. Still I think it'd be good for us if we got to know the neighborhood, since we're going to be here a while."
    MC "Plus it could be fun. So what do you say?"
    GTS "I agree, it would be nice to learn more about the area as well as meet the people."
    show GTS happy
    GTS "I say yes, I'd be delighted to join you two - if you don't mind my intrusion?"
    MC "Heh, nah, we'd love to have your company. Great, though! I'll let you know when we're meeting up and where. Now if you'll excuse me, I have to find Honoka and let her know too."
    MC "Talk to you later."
    GTS "Good bye Hotsure-san, have a pleasant day."
    "I waved at her as she bowed before I left the roof. I had actually only just learned of the festival a couple hours earlier, but this seemed like a good way for all of us to just relax and have fun. Now if only I could find Honoka..."
    jump daymenu

label GTS009:
    scene Festival with fade
    "Music and cheers set the mood as the buildings lining the block reflected the lights of various lanterns. Dusk was beginning to set in, and as it did, a wave of multiple-colored lights replaced the sunlight."
    "Booths covered both sides of each walk way as vendors attempted to tantalize visitors  with various knick knacks and home-style delicacies. They didn't get to me, though, as I had my sights set on a more personal venture. As I made my way further into the festival, I could pick out the two familiar voices."
    show GTS neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    show BE neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    GTS "...Are you certain, Inoue-san? I know many lovely tailors and vendors who could find you the loveliest yukata."
    BE "Heh, nah, I'm good. They just really aren't my thing. Plus, with these girls, it's more of a hassle than you'd think."
    GTS "Well, if you're certain. Though I'd gladly help you get dressed if you're concerned about your bust getting in the way..."
    BE "Well I appreciate the help Yamazaki-san, and I know this is the Yukata festival and all, but it's okay. I'm good. Besides, right now I need the support, and I know if you're wearing a yukata properly, you're not wearing anything underneath it. That goes for bras, too! Oh, look."
    BE "Yo! Kei-chan!"
    "She waved as she called out to me. Upon seeing them I cracked a small smile, as at least in Naomi's case, this had been the first time I'd seen them out of uniform. Honoka opted to wear a simple tank top and shorts, as with the warmth of the night it allowed her to enjoy the breeze. Naomi, on the other hand, got into the spirit of the festival and wore a full Yukata with a floral design, and even had an elegant flower hair clip on."
    # (This is mostly as a placeholder since with the art there will be a picture that negates this. But until then this is simply to describe them.)
    MC "Hey you two! Wow Yamazaki-san, you look great."
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
    MC "I-what?"
    BE "Heh. I know you were hoping to see me in one today. Sash way down past my boobs, hoping I'd spill a snow cone on them, or a goldfish would flop in my cleavage..."
    show GTS embarassed
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
    "Our pace through the sea of people slowed considerably at that point as we enjoyed our treats. Thankfully, this treat was enough to distract Honoka from asking for other things until we eventually came upon a stand that seemed to catch Naomi's eye."
    GTS "Oh, Hotsure-san. This seems like a good stand to look at some yukata. Come take a look, please?"
    MC "Hm? Are there any that stand out to you?"
    GTS "Shouldn't I be asking you that though?"
    MC "Yeah, but I'm really not good at this stuff. Which do you think would suit me best?"
    GTS "I'd need to think it over a bit. Is there a particular color you were looking for?"
    MC "I suppose blue."
    GTS "Very well, I'll see what I can find in that color scheme."
    "She inspected the stand for a few moments, handing me her shaved ice so she could feel the yukatas. Checking every side, every inch as she carefully examined possibly hidden options. All the while Honoka ate more of her shaved ice, wincing at the occasional brain freeze before immediately taking another bite."
    GTS "What do you think of this one, Hotsure-san?"
    "She lifted up a blue-colored yukata, it's design having a bold feeling towards it as there was light etching of mountains and clouds faintly imprinted on its surface. Not enough to be too distracting, yet still giving the eye a nice scene to take in if observed."
    MC "Oh wow, that's actually pretty cool."
    show BE happy
    BE "Yeah, looks awesome. I'd say it's a great find. Ow... my head..."
    GTS "I'm very glad you like it Hotsure-san. We'll take this one please."
    show BE neutral
    "She took the yukata to the vendor as she motioned for me to walk over. I handed our two shaved ice cups to Honoka, who snuck a bite from my bowl as I made my way over. Naomi had me stretch my arms outwards from my sides as she expertly placed the yukata on me."
    "She slid my arms within the sleeves, then made to check the length of the garment by sliding a finger down the center of my spine, which made me shiver slightly. Her hands grabbed onto the cloth and she lifted it so the hemline met just below my ankles, as there was some loose length in the hem."
    "Bringing the right side of the garment to the left side of my waist, she then moved one hand to the left side of the garment and had it over lap the right as it went to the right side of my waist. The vendor seeing that Naomi clearly knew what she was doing, simply handed her the sash as she whispered."
    GTS "Pardon me, Hotsure-san."
    "Before she wrapped the sash around my waist. Once she tied the sash to my waist she smiled lightly and told me."
    GTS "Please do as I do Hotsure-san, we need to smooth out the wrinkles."
    "She shows some holes on the underside of the armpits on her yukata and slid her hands into her own, my hands doing the same with my yukata. Together we slid our hands within the folds as the bunched up parts of cloth earlier began to smooth out and actually cover over the sash, making a seamless look to the gown."
    GTS "Please adjust your collar now Hotsure-san. It should fold just at the center of your collar bone. Simply pull the bottom of the back a tad until you can fit a rolled up fist into the opening behind your neck. Then gently pull at the front from inside the miyatsukuchi to get the desired look. "
    GTS "There you go, nicely done. And that's it Hotsure-san, thank you for allowing me to help you dress. If we had also gotten one for Inoue-san we would have needed to put another sash just underneath her chest, then smooth out the newer wrinkles before adding the obi."
    show BE happy
    BE "Yeah and that would take forever, so no thanks. Still, you look nice Hotsure-san."
    GTS "Indeed, you look very handsome, Hotsure-san."
    MC "Heh... thanks."
    show BE surprised
    BE "OH OH! Look!"
    "She pointed to a new stand and ran off to check it out, Naomi and I quickly following her. We easily found Honoka as she frantically waved for us to hurry up, as there was a small crowd around this stand for some reason."
    "When we arrived, the reason became rather clear, as this stand had a game."
    Vendor "Welcome! Are you a master fisher? Well then test your skills in my little game against my expertly trained goldfishes!"
    MC "You can train goldfish?"
    Vendor "Of course! It takes years of training and being one with the fish."
    MC "Uh... okay..."
    Vendor "Don't focus too much on that young man, instead take in the new direction I've gone with goldfish scooping."
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
    "I narrowed my eyebrows but gave him the money, and he handed me the fishing rod, before quickly replacing the poi basket."
    Vendor "Remember, the hardest test in life is having the patience to wait for the right moment."
    "He grinned at me as I let the basket carefully sink into the little pool. From my angle I realized that I couldn't tell how deep it was or where exactly in depth was my basket. Even the fishes could be at any point above the basket. I gave a couple of test reels, slowly expanding my basket though it seemed that each click of the reel sent a vibration down the wire which disturbed the water, signalling the fishes to move."
    "Taking a chance, I quickly reeled in as a fish swam over, but by the time the basket caught up the fish had already moved on."
    Vendor "Too greedy. Waaaait."
    BE "Come on Kei-chan, we're rooting for you!"
    "I gave a slight nod, as at least I was closer to the surface now. Though that also gave me less options, as not as many of the goldfish swam this close to the top. Each second ticked away without even the slightest hint of a fish drawing near, until finally one showed me mercy and swam just over my basket. Instinctively I yanked up to capture the fish, but this was a mistake, as the sudden force along with the erosion of the water had resulted in my poi collapsing and setting the goldfish free."
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
    "I looked at the vendor confidently though he only smiled as when I looked back at the poi the goldfish suddenly lept out of it."
    show BE surprised
    BE "It escaped!"
    show BE neutral
    "I couldn't react as I watched the fish descend back towards the pool, though it never made its target, as a small cup appeared beneath it and caught the goldfish."
    UNKNOWN "Here you go, mister."
    "A little girl as she rose the cup up to me with a smile."
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
    Vendor "Hm. Very well, consider that a freebee kid. Though I'll be sure to add that to the rules."
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
    show GTS embarassed
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
    "I led the way as we journeyed on to a eventful night of games, prizes, and food. And besides Honoka having eyes bigger than her stomach, the night was a ton of fun. I'm really glad we got a chance to do this, as well as getting the chance to take a picture of the three of us together."
    jump daymenu
    
label GTS010:
    scene Classroom Day with fade
    "A defeated sigh vacated my body as my hands had been slicking back my bangs all morning. I could already tell this growth was going to be annoying as I had only just recently had my hair trimmed and already it was back to before I had first gotten it cut."
    MC "This is really going to burn a hole in my wallet if I want to keep myself from looking like a mountain man by the end of the month..."
    "As I slumped back in my chair, I heard the door to the classroom open and looked over to see Naomi uncharacteristically rushing to get to her seat."
    show GTS neutral with dissolve
    MC "Hey Yamazaki-san."
    "The sound of my voice seemed to make her freeze on the spot like a deer in headlights. As I got up to greet her, I noticed that she was keeping her school bag in front of her."
    MC "How... are you?"
    "As I walked over, her eyes were looking between me and her desk, and she seemed to be inching her way towards it."
    show GTS embarassed
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
    show GTS embarassed
    GTS "I'm sorry, It's not really the height that bothers me it's just that..."
    "Her cheeks seemed to gain a slight shade of red as she looked away."
    GTS "My clothes don't fit as well, and I don't want to make a poor impression."
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
    show GTS embarassed
    GTS "I..."
    GTS "Thank you..."
    if getAffection("GTS") >= 7:
        $setFlag("GTS011_unlock")
        GTS "Apologies for changing the subject so suddenly, but Hotsure-san... I was hoping to ask you..."
        GTS "Would you be interested in coming over to my dorm room sometime in the next week? Perhaps Tuesday after class? Some things I had forgotten at home will be coming by and I was hoping you wouldn't mind having some tea with me."
        "Like earlier, I saw the barest motion of a blush as her eyes for a split second looked away."
        MC "Totally! That sounds great."
        "For the briefest moment, her lips rose to a slightly larger smile before returning to their normal position."
        show GTS neutral
        GTS "I'll be sure to get everything fully prepared, then. I do hope you'll enjoy it."
        MC "Oh, I'm sure I will. After all, with your plant knowledge I'd expect you to be a tea expert."
        GTS "I wouldn't say so, but thank you for the vote of confidence."
        "We shared a smile before the door to the classroom opened once more and the teacher walked in, resulting in me hurriedly rushing to my desk as we began the day."
    jump daymenu

label GTS011:
    scene Dorm Exterior with fade
    "Time had passed relatively quickly since Naomi invited me over for tea earlier. There hadn't been much time to talk or hang out besides the occasional casual greeting as well, so it felt nice to have a chance to catch up a bit."
    "Journeying around the dorm, I heard whispers hang around behind me. The occasional giggle accompanied them as some girls watched me. I could imagine it now, some small time rumors about me visiting a girl at her dorm. The same happened when I saw my sister at the start of the year, but I had learned to merely ignore it."
    "Upon reaching her door, I gave it a couple knocks before faintly hearing some noise through it. When she opened the door, I found myself looking at the crook of her lip instead of her eyes."
    show GTS neutral with dissolve
    GTS "Hello Hotsure-san. I'm glad to see you, please come in."
    GTS "I hope it wasn't difficult finding my room."
    MC "No, it wasn't a problem at all."
    "She opened the door for me and gave a slight bow, the action causing the small of her back to show which in turn caused her hands to immediately try pulling her top to better cover herself."
    scene Dorm GTS with fade
    "As I entered her dorm room, I saw another girl already inside. She sat kneeling at table, a cup of tea in her hand as she smiled and waved."
    #show Ryoko neutral with dissolve
    UNKNOWN "Howdy! You must be Hotsure-san."
    MC "Uh... yeah, I am. Hello."
    show GTS happy with dissolve
    GTS "Hotsure-san, this is Ryoko Tanaka. Tanaka-san, this is Keisuke Hotsure. Tanaka-san is my next-door neighbor who I met a couple days ago, so I invited her over for some tea as well. I hope that isn't a problem."
    MC "No, it's all right. It's nice to meet you Tanaka-san."
    Ryoko "Likewise, come on, have a seat."
    show GTS neutral
    GTS "Yes Hotsure-san, please make yourself comfortable."
    "I nodded my head and removed my shoes before taking my place at the table. Naomi soon kneeled down beside me and poured me a cup of tea to which I gave her a small nod."
    MC "Thank you."
    "Naomi gave a small nod in response as she gently set the teapot down, her hands subconsciously fixing her top to better hide her slightly exposed stomach before they rested in front of it to act as a cover. Meanwhile, Ryoko scooted a little bit closer to me."
    Ryoko "So how long have you known Yamazaki-san?"
    MC "Well, since the first day. I saw her at the garden before orientation but only really got introduced to her at the orientation."
    Ryoko "I see. Sadly, I've been super busy since the start of the school year, so I only just recently ran into Yamazaki-san myself."
    GTS "I thought it would be nice to start introducing myself to my neighbors."
    Ryoko "She offered me these super tasty crackers and tea, too. Actually, Yamazaki-san, would it be all right to ask if you have any more? They'd go wonderfully with this tea."
    GTS "Ah yes, how rude of me. Please, excuse me."
    "She quickly stood up, her knees lightly bumping the table which she deeply apologized for before she hurried to get some snacks for the us to enjoy as I talked with Ryoko."
    hide GTS with dissolve
    MC "What have you been so busy with?"
    Ryoko "Oh, mostly filming."
    MC "Filming? Oh, thanks Yamazaki-san."
    show GTS neutral with dissolve
    "Naomi had already returned with a small tray of crackers and offered one to me and Ryoko, who also took one."
    Ryoko "Thanks Yamazaki-san. Yeah, me and a couple of students in the flim club are working on a small movie together."
    MC "Oh wow, that's pretty cool."
    GTS "That does sound like it would be fun."
    #show Ryoko happy
    Ryoko "Oh, it's totally a lot of fun! Sure, they're just silly no-budget videos but it's still a blast. You two should join us sometime, we're always open for auditions."
    show GTS embarassed
    GTS "Me!? Oh no, I couldn't possibly do something like that. I wouldn't be capable of remembering a single line, or ignoring the camera. Or are you supposed to look at the camera? I'd gladly watch them though."
    MC "Heh, I actually wouldn't mind giving it a go sometime. Also, with enough experience in front of the camera I'm sure you'd get the hang of it, Yamazaki-san."
    #show Ryoko camera
    Ryoko "Yeah Yamazaki-san, you'd be a natural! You'd bring a sense of elegance last seen in the classic era of films. The tall, slender beauty the men are drawn to, who gives an aura of maturity and confidence. Just like um... Jessica Rabbit! That's the name."
    "I could see the faintest hint of blush appear on Naomi's cheeks as she sipped some tea."
    GTS "I-I don't know... I wouldn't want to be distracting, or take away from the story being told."
    GTS "I'm sure Nikumaru-san would be a much better actress than me."
    #show Ryoko happy
    Ryoko "I have no idea who that is, but seriously though, we'd love to have you guys come by if you ever want to hang out."
    #show Ryoko neutral
    Ryoko "I'm sure you'd quickly win them over with those elegant looks."
    MC "I have to agree with her on that."
    GTS "Thank you..."
    Ryoko "So that's one thing I do on my spare time, what about you two?"
    MC "Well I kind of hop around a lot, so I couldn't really name one thing in particular."
    show GTS neutral
    GTS "I merely tend to my garden, as well as a couple of the plants here. Besides that, most of my time goes to my studies."
    Ryoko "I see I see, well then, I propose another get-together sometime soon."
    #show Ryoko happy? excited?
    Ryoko "Oh! A movie day! I'll even order a pizza for us to enjoy."
    MC "A movie day?"
    Ryoko "Totally! What better way to hang out and relax with friends than a good movie and some tasty hot food?"
    MC "Well I can't disagree with that. ...Sure, that sounds like a fun time to me. What do you think, Yamazaki-san?"
    GTS "I'd have to look at my schedule. But I promise I'll let you know as soon as I get everything figured out."
    Ryoko "Excellent! Well I'll be going on my way. Thanks so much for the tea and crackers Yamazaki-san, they were great. And it was nice meeting you Hotsure-san, catch you two later."
    #hide Ryoko
    "She gave us a wink and a bow of respect before heading towards the door, and seeing herself out before Naomi had a chance to get up. We sat there for a second or two, but soon enough I gave a small chuckle and took a sip of tea."
    MC "Heh, I see you started with the most energetic neighbor first."
    jump daymenu

label GTS012:
    scene School Planter with fade
    show GTS neutral with dissolve
    "A small sigh left my body as I rested back against a tree."
    "I was in the garden, Naomi having invited me for some tea after class had ended."
    "She had set up a blanket on the grass and was preparing the drinks. It was an interesting sight as she sat on her knees, an assortment of items in front of her as she began the long process of making the tea."
    MC "I've never seen someone do this in person before. That's pretty impressive."
    "She ground the tea leaves in a bowl, the crackling sound gently emitting."
    GTS "Thank you, Hotsure-san. It's one of the things I was taught when I was younger.  I find the entire process deeply soothing. The preparation, the mixing, and then the tea itself. It can ease the soul and refresh the spirit."
    MC "Sounds really spiritual. Thank you, by the way. For inviting me over, and for the tea."
    GTS "You're most welcome, Keisuke. I felt it was the courteous thing to do after what you said back in class a few days ago."
    "I felt my face get a little warmer as I couldn't hold back a faint smile. The sharp whistle from the tea pot breaking the silence as the water had come to a boil."
    MC "Well, you're welcome for that then. Guess this would make us even then, heh."
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
    GTS "After all, The whole process is not about drinking tea, but is about aesthetics, preparing a bowl of tea from one's heart."
    MC "That's rather poetic, and a lot more thought-out than I was expecting."
    GTS "Well, that's because as the host, you always want to be mindful of your guests, so each movement, gesture, and even the placement of the utensils are carefully thought out before beginning."
    "With her mentioning of that, I noticed that she had indeed placed all the utensils in such a way that I'd be given a perfect view of each step she had taken to make the tea."
    MC "Heh, wow, you really did set this up perfectly, then."
    GTS "Thank you so much."
    MC "I was also going to mention that the scent was very familiar."
    show GTS neutral
    GTS "That is most likely because I often use the plants I grow in my room for my tea."
    MC "That's probably it, then. I must say, Yamazaki-san, I'm really impressed."
    show GTS embarassed
    GTS "You're too kind, Hotsure-san."
    jump GTS012_after

label GTS012_c2:
    $setAffection("GTS", 1)
    MC "So how have you been holding up, with your condition?"
    GTS "I've been okay, Hotsure-san. How about you?"
    MC "Me? Yeah, I've been fine. It's a little annoying, but I can manage. I just wanted to make sure you're okay. I know some of the other girls are still a little worried about themselves."
    show GTS embarassed
    GTS "That's very thoughtful. But I'm okay, I assure you."
    MC "Alright, though if you need to talk, just let me know."
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
    "She giggled very softly which resulted in a chuckle from me as we relaxed for a little longer before needing to go our separate ways."
    jump daymenu