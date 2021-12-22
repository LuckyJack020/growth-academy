label GTS001:
    $setProgress("GTS", "GTS002")
    scene Campus Center with fade
    play music Peaceful
    "The words from Tashi-Sensei stayed with me long after class had concluded. I just wasn't sure how to properly process what we were told."
    "What Daichi had told me earlier was starting to resonate more, and I began to wonder if others knew about the purpose of this school before they were enrolled."
    "If only to focus on the things I could understand for a while, I decided to take a walk and take stock of the new campus; the little pamphlet map they gave us, I figured, would only do for so long."
    UNKNOWN "Excuse me!"
    if getSkill("Athletics") > 2:
        "No sooner had the shout crossed my ears than something smacked hard into my shoulder, and some guy my age stumbled in front of me before breaking back into a stampede."
    else:
        "A fraction of a second after I processed the machine-gun footsteps behind me, their owner smashed into me like someone throwing a machine gun at me."
        "I just recovered my footing in time to see a half-flailing student running off without a glance back."
    MC "Ay, watch it!"
    UNKNOWN "Sorry!"
    "He didn’t look back, fading into the crowds alongside the wind."
    MCT "Dick."
    UNKNOWN "Hotsure-san? Are you alright?"
    "The next thing to catch me off guard was a girl’s voice, one enveloping and immaterial, like spring mist."
    show GTS surprised:
        xpos 0.99 xanchor 0.0 yalign 1.0
        linear 5.0 xpos 0.5 xanchor 0.5
    extend " I twisted around; one of the girls from my class was walking up to me from behind while raven locks waved behind her in the breeze."
    MC "Yamazaki-san, right? Yeah, I’m okay. That dude just surprised me."
    GTS "It would seem so. How peculiar. I wonder what compelled him to act so brashly?"
    MC "Dunno. He’s probably not available for interview."
    GTS "I suppose he wouldn’t."
    GTS "Well now, what are you up to?"
    MC "Nothing much, just checking out what’s on campus. How about you?"
    GTS "Much the same. For all its peculiarities, this place has a sort of charm to it, does it not?"
    MC "I guess so. I’m kinda distracted by all the ‘peculiarities’ at the moment."
    show GTS happy
    "She closed her eyes in a genteel, whispered chuckle, which she moved to cover with her hand."
    show GTS neutral at Transform(xzoom=-1)
    GTS "Who could blame you? It's one thing to hear about this phenomenon in passing, it's entirely another to walk through the midst of it."
    MC "Tell me about it. First time I heard about these... growths? Mutations? When I first saw 'em on TV, I thought it was special effects, some kind of hoax."
    show GTS despaired-thought
    GTS "They appeared on television? The things the stations will do for ratings these days, I swear..."
    MCT "You... didn't know that?"
    show GTS neutral at Transform(xzoom=1)
    GTS "But let us contemplate more wholesome things."
    if getAffection("GTS") > 1:
        extend " If you are also getting familiar with the campus, would you perhaps like to take a walk together?"
        MC "Sure, I'm down for that. Did you have anywhere you wanted to check out next, or?..."
        GTS "Oh, no. It is well with me if you lead the way, if you would."
    else:
        MC "Uh... yeah, sure."
        MC "Hey, if we're both doing the same thing, you wanna take a tour around campus together?"
        GTS "That is a fine idea, Hotsure-san. Please, lead the way."
    "She joined me by my side, and we resumed the walk. Even with her keeping a polite distance, I couldn't help but steal a glance or two at her."
    "The demure, waifish little thing walked with posture that, frankly, put me to shame. The flowing wind across the campus set her long, jet hair to a swaying dance as gentle as her pace."
    "Every time I looked, she nodded at me with a polite suggestion of a smile."
    scene School Exterior with fade
    "It didn't take long until our walk turned less into a tour and more into a friendly chat with a scenic backdrop."
    show GTS neutral with dissolve
    MC "So, uh... were you thinking about what Tashi-sensei told us, too?"
    GTS "A little, yes, as I think most of the students have been. Were you as well?"
    MC "Yeah, I was. It's just... weird, isn't it? It's been lingering in my brain all day."
    menu:
        "What do you think about it?":
            jump GTS001_c1
        "I'm curious about what changes I might go through...":
            jump GTS001_c2
        "I'm concerned about what that might mean for my younger sister, honestly.":
            jump GTS001_c3

label GTS001_c1:
    GTS "It is a little concerning, I will admit; however, I think some of those feelings come from the suddenness with which we were introduced to this world, as it were."
    GTS "I'm sure if we take more time to reflect on it and take it in, the situation won't feel quite so frightening.{w} Thank you for asking, though."
    MC "No problem. We're in this together after all, right?"
    GTS "I daresay that is a wise and uncommon sentiment. I agree."
    jump GTS001_after

label GTS001_c2:
    GTS "Oh, it is surely better to be curious than fearful. Too easily are we tempted into worry and turmoil."
    MC "Yeah, yeah. Come to think of it, I wonder how the school figures out what we'll end up like."
    GTS "I'm sure they have methods. I understand the academy's medical facilities are superbly furnished and staffed. Though I daresay intuition suffices for some cases..."
    MC "Heh, yeah, I get you."
    show GTS embarrassed
    GTS "Oh, I'm sorry! That sounded rather rude, didn't it? I don't mean to disparage any of the other students."
    MC "Heh, it's okay, Yamazaki-san. I can tell you didn't mean anything by it."
    show GTS neutral
    GTS "Thank goodness, I wouldn't want to start making the wrong impressions on the first day of school."
    jump GTS001_after

label GTS001_c3:
    $setAffection("GTS", 1)
    GTS "Oh? You have a younger sister, Hotsure-san?"
    MC "Yeah, she's going to school here, too. I'm just thinking about what Sensei said, about how sometimes siblings are transferred to this school simply because of the results of the other."
    MC "I'm sure I can cope with whatever might happen to me, but I'm worried about her. I just don't want her to go through something that might hurt her."
    GTS "It's only natural to worry as the older sibling Hotsure-san, but you mustn't let it concern you too much. There's no way to know for certain at the moment, and as such it may be best to be hopeful and keep your chin up."
    MC "Yeah, I guess that's true. Sorry for sounding like a mother hen here."
    GTS "There's no need to apologize for it. I know I'm very much the same with my own sister."
    MC "You have a sister too?"
    GTS "Yes, she's a couple years younger than me. I hope it's some comfort that you're not the only one who can come off as a mother hen at times."
    jump GTS001_after

label GTS001_after:
    GTS "And you know... just this morning I went to buy a pack of nori from the vending machine by the administrative building... not something I am wont to do, I confess... "
    MC "Yeah?"
    GTS "Yes... but as I withdrew a bill from my money clip, a 5000 yen note slipped out and blew away in the wind."
    show GTS unique-2
    GTS "But as the saying goes, easy come, easy go. The nori was quite satisfying regardless."
    show GTS neutral
    MC "I..."
    MC "You..."
    MC "I'm sorry, you lost {i}how{/i} much? And you're just... {i}okay{/i} with it?"
    GTS "Attachments are the root of suffering in this life, Hotsure-san. Attachments to our status quo and attachments to yen notes alike."
    MC "That's... that's interesting."
    GTS "I am glad you think so."
    scene School Planter with fade
    show GTS neutral with dissolve
    "Through my half-stunned silence, she gave a soft chuckle and kept her warm smile that soothed my worries."
    "In the midst of it, I just processed that we had wandered back to the spot where I'd first met her, before an array of massive planters that shone emerald-green in the afternoon sunlight."
    "But my eyes shortly found their way back to Naomi; I guess she must have noticed me staring, because she soon chimed in."
    show GTS neutral at Transform(xzoom=-1)
    GTS "I wasn't going to say anything, Hotsure-san, but it's rather rude to stare."
    MC "O-Oh! Sorry... I was just thinking again, haha... So, are you going to be doing anything else later today?"
    show GTS neutral at Transform(xzoom=1)
    "She placed a finger on her lip as she thought, before finally replying."
    GTS "Well, I had planned to return to my dormitory so I could tell my family about how my first day went."
    GTS "However, before I do that, I may take in these gardens more. There's a surprisingly large variety of flowers here, more than I expected."
    GTS "In particular, I would like to perhaps ask the groundskeeper about where the school obtained the seeds."
    MC "You're into gardening, huh? I never put it together but it makes a lot of sense."
    show GTS unique
    GTS "Hmhm, very much so. Ever since I was little, I've loved the way one cultivates himself alongside the plants, and the inimitable beauty it can bestow on one's space."
    MC "That's really cool, Yamazaki-san."
    MC "Well hey, I won't hold you up, then. I should probably send my family a text, too. They'd probably love to hear about how my day went, too. I'll see you around, Yamazaki-san."
    GTS "Farewell, Hotsure-san. I hope the rest of your day goes well. Do try to visit the garden every so often. You might be surprised how much good can come from a moment's repose in the right environs."
    MC "Heh, I might take you up on that advice. See you later, Yamazaki-san."
    "She gave me a small bow before I departed."
    hide GTS with dissolve
    MCT "Heh. Nice girl."
    jump daymenu

label GTS002:
    $setTimeFlag("testday")
    $setProgress("GTS", "GTS006")
    scene School Planter with fade
    "I always found the sky to have quite the alluring palette around late afternoon. Clouds coated in degrees of red that ranged from rose color to pink and even orange and yellow."
    "And while I normally didn't find myself staring up at the sky, it was simply something I couldn't resist as I stepped into the school's garden once more."
    "The breeze had become cooler, but still flowed with a sense of gentleness to it, making some pink colored flowers dance before me."
    "In the distance, I heard a faint voice, and as I turned to look I spied Naomi giving a gracious bow to who I assumed was the gardener."
    show GTS neutral at Position(xcenter=0.75, yalign=1.0), Transform(xzoom=-1) with dissolve
    play music HigherEdu
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
    "Her smile quickly vanished and instead a light blush formed across her cheeks."
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
    MC "Oh, I'm rather interested in soccer. I might give it a shot later this year, if my condition doesn't hinder it in some way."
    "I chuckled lightly, kind of realizing that we couldn't plan our futures for the moment."
    "Without any knowledge about what might happen to us, everything was up in the air. I pushed that thought to the back of my mind though."
    GTS "Hopefully you'll be able to do so, Hotsure-san. Soccer has always seemed like a rather enjoyable sport, a lot of endurance needed so it's good exercise."
    "She gave me another soft, warm smile that made me smile in return as I scratched the back of my head."
    MC "Heh, thanks. Well, it's getting rather late, and I don't want to keep you from any plans you possibly have with your flowers, so I think I'll be heading off now. Before I go, though, do you need any help with those?"
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
    "This let me notice that her other bang was currently held back by a flower shaped hair clip. I had no idea what type of flower it was, only knowing that it had five white petals in a sort of star configuration."
    MC "How was the start of your day, if you don't mind me asking?"
    "Naomi perked up slightly as I asked my question, taking her napkin to delicately wipe her lips and properly placing it back in place before answering."
    show GTS neutral
    GTS "Myself? Well, I woke up rather early as well, and took the time to properly make my bed."
    GTS "I then showered and prepared myself for the rest of the day. Things like properly combing my hair, getting everything organized, and planning out my schedule for the day."
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
    "For the briefest of moments I could see Naomi's cheeks flash a slight crimson in what I assumed was embarrassment as her hand went to touch the accessory."
    "She looked away for a second, but returned her eyes back to mine and retrieved that small smile she had before."
    show GTS embarrassed at center, Transform(xzoom=1)
    GTS "Oh, why thank you so much. It's just a little something I decided to add to the rest of my attire for today. I have a bit of a collection of them, various species and things of that nature."
    MC "Well, I think it suits you rather well."
    GTS "Thank you..."
    show GTS neutral
    GTS "As for your question, this flower is a Jasmine, which tends to confuse some people, since they happen to look slightly generic."
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
    $setProgress("GTS", "GTS006")
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
    "I let out a small chuckle which caused her to narrow her eyes a little but she eventually seemed to settle down as she looked at the book I had placed down."
    "I had an opportunity to see what she was reading herself, seeing the symbols that showed what appeared to be another language."
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
    GTS "I'm trying to get a bit more studying of it done in my free time. Just to get a better understanding of it for myself."
    MC "That's neat, are you planning to visit the United States in the future?"
    GTS "I can't be certain truthfully, but I think it's best to be prepared for it in case it ever happens. It's also a good skill to have if your work might require it, or if you might have international guests."
    MC "Heh, that's quite the foresight to have. I barely even think about what I'll be doing a month from now. Hey, if you manage to make it work, though, that's one massive advantage you'll have over others in the job market, so good luck!"
    GTS "Thank you."
    "She showed hints of a smile as I wished her luck."
    MC "How well did you take in what we learned in homeroom today?"
    "She gave the smallest sigh as she reached to her back and retrieved a rather large book."
    GTS "Unfortunately, not as well. Science is proving that it might be harder than I originally thought."
    GTS "As you know, our professor seems rather adamant that we start off the year sooner rather than later, and regrettably the crash course we were given made it a little difficult to retain all the information we went over."
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
    "I wandered about the campus for quite some time after visiting the nurse, the news of my particular condition having left me with a feeling of uncertainty."
    "As I walked, my hand would occasionally reach up to touch the tip of my bangs as I wondered just how quickly they might change."
    scene School Planter with fade
    play music Peaceful
    "As I stepped past the double doors and into the garden, my eyes shut from the blast of sunlight that I was exposed to. After a few seconds my eyes readjusted and I saw Naomi's form kneeling in front of a patch of flowers."
    "Calmly walking over, my footsteps on the path nevertheless alerted her to my presence, and she looked back at me and gave a soft wave."
    show GTS neutral at center with dissolve
    GTS "Hello there, Hotsure-san."
    MC "Hey Yamazaki-san. How are you doing?"
    "She stood up and dusted off her legs before turning her full attention to me."
    GTS "I'm doing well. I came here to do some reflecting and thinking. I feel rather inattentive though, I somehow had missed this small patch of botan flowers here."
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
    MC "What else can you tell me about botans?"
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
    MC "Heh... Not a fan of horror movies then, huh? Well don't worry, I'm mostly teasing, I wouldn't actually do that.{w} Well okay, maybe on Halloween."
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
    "A little time passed before the dog's owner finally showed up and thanked everyone for finding their dog before taking it back home."
    "As the crowd dispersed, I saw Naomi walk by and notice me. Flashing her trademark smile, she gave me a small wave of her hand."
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
    $setFlag("GTS006_c2")
    MC "Yeah, he was extremely cute!"
    show GTS happy
    GTS "Indeed, he was. Did you get a chance to play with him?"
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
    show GTS embarrassed at Position(xcenter=0.4, yalign=1.0)
    "There was the faintest hint of a blush on Naomi's face as she broke eye contact and looked to the side for a second, before returning her attention."
    show GTS embarrassed
    GTS "My father always said he picked that breed because the Hokkaido has the three characteristic he looks for in people: bravery, loyalty, and intelligence."
    GTS "I can say he was right about that description, because she's probably been one of the most loyal dogs I've met."
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
    "Petals danced in the breeze, carried aloft by the wind. They flowed rhythmically down the pathway, where I saw a familiar figure sitting underneath the shade of a tree. Naomi's hair moved much like the flower petals had. I noticed a piece of paper in her hand."
    MC "Hey there, Yamazaki-san. How are you?"
    "She looked up from a letter when I called out to her, and responded with a gentle wave of her hand."
    show GTS neutral at center with dissolve
    GTS "Hello, Hotsure-san. I was reading a letter that my mother sent me. How are you?"
    "Naomi’s direct and formal language was somewhat different from the others I talked to at school. She appeared to be very disciplined and tactful, the way that she spoke."
    MC "I've been pretty good, for the most part. Also, a handwritten letter? I'm surprised people still make those."
    "A faint smile crossed her face as she folded up the letter and placed it back into the envelope."
    GTS "Yes, they seem to be quite rare nowadays. However, my mother really enjoys traditional writing. It's become sort of a thing she does for those living far from home."
    MC "That's pretty cool. I bet the post office loves having actual mail to give out that aren't just bills or packages people ordered online. That's a neat little postcard, too. Where is it from?"
    "She looked down at the postcard in her hand that had come with the letter and lifted it towards me. It was a picture of Kyoto, adorned with a wax seal."
    MC "Oh hey, it's Kyoto. I thought I recognized that tower there. Are you from there?"
    "Naomi nodded."
    GTS "Yes, I am."
    MC "Interesting. I've never been to Kyoto, but it always looked like a pretty neat place. I've heard that it's one of the best places to go for food, too."
    "There was the faintest smirk out of Naomi as her smile grew a little, giving a nod of acknowledgement as I sat down beside her."
    GTS "Yes, Kyoto is very well known for its cuisine. Specifically, our tofu and Kaiseki cuisine."
    GTS "My friends and I made it our personal goal to visit a new restaurant every weekend. It was rather fun, and it gave me a deep appreciation for my hometown. It lets you explore more, and sometimes you find little underappreciated establishments."
    MC "Wow, that sounds like it'd be cool to do. Though, it also sounds like it’d be pretty heavy on the wallet after a while, wouldn't it?"
    GTS "Some places were more expensive than others, yes. You'd be surprised by some of the places you find, though. Every now and then, we'd stumble across a place that not only had great dishes, but reasonable prices too."
    GTS "We had really expanded our list of places we could socialize. We’d claim that a new spot was our favorite, only to change it again a few weeks later."
    MC "Heh, that doesn't sound like a bad habit to have. Though, now I'm trying to think if I ever did anything like that."
    MC "I mean, I think I did a normal amount of exploring, but it was never too extensive. It might just be because of how crowded it often gets where I'm from."
    GTS "Where are you from, if you don’t mind me asking?"
    MC "Oh, I'm from Tokyo. The big city, Gojira's favorite playground. Just a little bit off of Shibuya."
    GTS "Oh, wow! That must have been exciting, being so close to the center of all the action. You must have seen and experienced many interesting things."
    MC "Yeah, especially during the holidays when all the tourists take over the streets. You basically turn an already crowded intersection into an impenetrable wall of people."
    MC "I felt bad for the people driving because, well... they weren't going anywhere for quite a long while."
    GTS "I do hope that you were careful during those times. I've heard stories of how overwhelming Shibuya can get during the holidays."
    show GTS sad
    GTS "I’ve also heard quite a few horror stories about some of the nastier incidents that can take place due to the massive amount of traffic."
    MC "Yeah, I was okay. I knew well enough to not get too absorbed into the larger crowds, and kept away from people who could have looked like trouble."
    MC "Plus, it's always good to have a couple of friends with you. Makes some of the troublemakers think twice before trying anything."
    MC "That's just Shibuya during the big times of the year, though. How about Kyoto? Does it get as crowded as Tokyo?"
    show GTS neutral
    GTS "Well, it would depend on the time of year, I suppose. It's the same as any big city, I imagine. Around Christmas time, though, restaurants tend to start charging more for meals -- sometimes even doubling their prices."
    MC "Because of all the people, I assume?"
    GTS "It’d make sense, yes. A lot of people see Christmas as a big date night event in Kyoto."
    GTS "I don’t exactly approve of their tactics, but I can understand why it happens. Dining out on a holiday is a lot more difficult when you consider how many places will close."
    GTS "I recall that many of my friends enjoy going out on dates to places like La Part Dieu, this wonderful French restaurant. Alternatively, they might go to Daimaru to visit the stores and see the decorations."
    MC "I bet they saved up all year long for that night, if it's as expensive as you say it is. I can't say I've ever found myself in a scenario like that, though."
    MC "Which is probably for the best, because I don't know any fancy places to eat. But how about you? Did you ever do anything with someone special?"
    "Naomi's cheeks turned quite the adorable shade of red as her composure broke and she looked down at her letter."
    show GTS embarrassed
    GTS "M-me!? Oh no, I haven’t...  I never had any time for things like that. I was always too focused on other things like helping around the house or preparing for other social events."
    MC "Oh? Are you telling me that you've never been on a date, then?"
    show GTS embarrassed at center, Transform(xzoom=-1)
    "I could see her face brightening up more as she tried avoiding eye contact. It was rather sweet seeing this side of her."
    GTS "I'll admit... I have not. My schedule was -- and to an extent, still is -- filled up with many responsibilities. It would have been nice to have seen what it was like, but I suppose fate hadn’t said it was the right time yet."
    show GTS neutral at center, Transform(xzoom=1)
    "She looked back towards me as she managed to regain her composure. I gave her a small nod, as I didn't want to push the issue too hard."
    MC "Yeah, I guess it would be pretty tough if you're always busy. But at the same time, I wouldn't worry too much about it."
    MC "Back on the topic of hanging out with friends, have you managed to make any new ones here?"
    GTS "...No, not really. It's been a chaotic time since everyone’s trying to get settled in, so I try not to impose on them. I hope that more people open up to me in the next few weeks."
    GTS "Maybe then, it'll be a bit easier to introduce myself to more people."
    MC "Well if you’d like, you could hang out with me and my friends. I can't promise you'll hit it out of the park right away but it's worth a shot, right?"
    "Naomi silently pondered to herself for a few moments."
    GTS "Would it be okay if I took a little time to figure out my schedule before giving you an answer, Hotsure-san?"
    MC "Heh, yeah... it's okay, Yamazaki-san. We're still young, after all. Take your time."
    "I gave her a small chuckle, and she returned a brief nod. I leaned back a little, enjoying the calm of the garden and the gentle breeze."
    "The two of us remained silent for several minutes. We breathed rhythmically, entering a zen state."
    "I didn’t mind the quiet. It was probably the most peaceful I had felt in quite some time."
    jump daymenu

label GTS008:
    $setProgress("GTS", "GTS009")
    scene Roof with fade
    play music HigherEdu
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
    MC "By the way Yamazaki-san, Honoka and I are going to head into town in a couple of days. Would you like to join us?"
    GTS "Oh? That sounds lovely. I haven't had a chance to visit myself."
    MC "Yeah, I think it'd be good for us if we got to know the neighborhood, since we're going to be here a while."
    MC "Plus it could be fun; just a day of exploring. So what do you say?"
    GTS "I agree, it would be nice to learn more about the area as well as meet the people."
    show GTS happy
    GTS "I say yes, I'd be delighted to join you two - if you don't mind my intrusion?"
    MC "Heh, nah, we'd love to have your company. Great, though! I'll let you know when we're meeting up and where. Now if you'll excuse me, I have to find Honoka and let her know too."
    MC "Talk to you later."
    GTS "Goodbye Hotsure-san, have a pleasant day."
    "I waved at her as she bowed before I left the roof. This seemed like a good way for all of us to just relax and have fun. Now if only I could find Honoka..."
    jump daymenu

label GTS009:
    $setTimeFlag("size2")
    if getFlag("GTS011_unlock"):
        $setProgress("GTS", "GTS011")
    else:
        $setProgress("GTS", "GTS011b")
    $setTime(TimeEnum.EVE)
    scene Town with fade
    play music HigherEdu
    #Afternoon, gentle music, scene becomes locked after scene 10.
    "My stride was rather lax as I wandered the various blocks of the town. It was rather quaint and not crowded."
    "Well, that wasn't entirely true, as on occasion I'd spot someone with a rather large endowment and see them journey through the other people. A faint reminder on what may be the future for some of the others."
    "I didn't get to stay on that train of thought for long however as I faintly heard a gentle voice speaking."
    show GTS neutral at Position(xcenter=0.25, yanchor=1.0) with dissolve
    GTS "... Are you certain, Inoue-san? I know many lovely tailors and vendors who could find you the loveliest yukata."
    show BE neutral at Position(xcenter=0.75, yanchor=1.0) with dissolve
    BE "Heh, nah, I'm good. They just really aren't my thing. Plus, with these girls, it's more of a hassle than you'd think."
    GTS "Well, if you're certain. Though I'd gladly help you get dressed, if you're concerned about your bust getting in the way..."
    BE "Well, I appreciate the help, Yamazaki-san, but it's okay. I'm good. Besides, right now I need the support, and I know if you're wearing a yukata properly, you're not wearing anything underneath it. That goes for bras, too! Oh, look."
    "I was immediately spotted as I rounded the corner and saw the girls in a more casual attire than I was used to."
    BE "Yo! Kei-chan!"
    "She waved as she called out to me. Though my eyes immediately widened as Honoka ran over, her bountiful bust bounding towards me before she came to my side and tossed an arm around my shoulders."
    show BE happy
    BE "How's it going?"
    MC "Hey you two! Wow, Yamazaki-san, you look great."
    "Upon seeing them, I cracked a small smile, as at least in Naomi's case, this had been the first time I'd seen them out of uniform."
    show GTS happy
    GTS "Thank you."
    BE "Hey! What about me?"
    MC "Heh, you look great too, Honoka."
    BE "Thanks! Well, now that you're finally here, let's go explore!"
    "We embarked on our adventure to learn more about the town, but didn't get too far as Honoka's went wide eyed whenever any tasty sweet was shown to her from a vendor."
    "She'd look back at me like a begging puppy, asking for money, which seemed to always win me over. Well... at least the first 5 times."
    MC "Honoka, I can't keep buying you things... I'm going to run out of money."
    show BE sad
    BE "But Kei-chan! It's shaved ice! What afternoon with friends be complete without some?"
    show GTS neutral
    GTS "It's okay Hotsure-san, I can pay for this one. To be honest, I was hoping to get some myself. Which flavor would you like, Inoue-san?"
    show BE happy
    BE "Really? Thanks! Umm... hmmm... let's go with some watermelon and blue raspberry!"
    GTS "Very well. Hotsure-san, would you like some?"
    MC "Sure, if you're okay with the expense."
    GTS "Oh, it's truly no bother, Hotsure-san. Which flavor would you prefer?"
    MC "I think I'll go for some mandarin."
    show BE angry
    BE "Booooooring. Come on, try something exciting, or mix them up."
    GTS "It's quite alright if you just want mandarin, Hotsure-san. I'm sure Inoue-san is merely teasing."
    GTS "As for myself, I think I'll have strawberry."
    "She placed the order and then compensated the vendor before she gently handed the shaved ice to each of us."
    show BE happy
    BE "Thanks, Yamazaki-san!"
    MC "Yeah, thank you."
    GTS "You're very welcome. Please enjoy, oh and try not to eat too fast. Don't want to brain freeze after all."
    "Our pace through town slowed considerably at that point as we enjoyed our treats. Thankfully, it was enough to distract Honoka from asking for other things until we eventually came upon a store that seemed to catch Naomi's eye."
    GTS "Hm?"
    MC "Huh? Something up Yamazaki-san?"
    show GTS embarrassed
    GTS "Oh. Nothing. Just thinking."
    show BE neutral
    BE "See something in that store you like? If you ask I'm sure Kei-chan will buy it for you."
    MC "H-hey, I'm not a bank."
    GTS "N-no, it's fine. I didn't mean to delay our trip."
    show BE happy
    BE "It's no problem. I mean that's why we're walking through town for anyway right?"
    "She smiled and tried finishing the last bit of her shaved ice quickly. Her smile quickly melting as her brain froze over and she did a little dance as she rubbed her head."
    show BE sad
    BE "Ahhhh! Brain freeeeeeze!"
    MC "Yamazaki-San warned you..."
    MC "But yeah Honoka is right, exploring was the whole point for the trip so let's check it out."
    GTS "If it's truly alright..."

    scene Pharmacy with fade
    "Entering the store I had to admit I was surprised that it seemed to mostly be just an assortment of knickknacks."
    show GTS neutral at Position(xcenter=0.25, yanchor=1.0)
    show BE neutral at Position(xcenter=0.75, yanchor=1.0)
    with dissolve
    MC "Was there... anything particular that caught your eye Yamazaki-san?"
    GTS "No, I just wanted to look around. My mother has a tendency to give me some random items like these whenever she goes away on a trip."
    show BE neutral
    BE "Ooooooh, I get it. You're homesick."
    GTS "Possibly."
    MC "Well, take as long as you need."
    show GTS neutral
    GTS "Thank you Hotsure-san."
    hide GTS
    hide BE
    with dissolve
    "We explored the store out our own leisure, Naomi seeming distracted with some postcards while Honoka was examining small trinkets."
    "As for myself, I was mostly just examining some accessories when one really caught my interest. It was a headband that had a fake flower on one side of it. But its color was what made it so alluring."
    "It was a baby blue flower with a golden ring in the middle. My first thought was Naomi possibly liking it."
    "However I then looked a bit further down and noticed an assortment of pins. I recalled Honoka having a thing for these when we were younger."
    "She was always so loud with the giggling of all the pins on her bag. Getting a small chuckle from the memory, I pulled out my wallet and sighed."
    MC "Damn it Honoka... did you really need to bug me for all those treats?"
    "I only had enough money left to get one of the items as I looked back down the aisles as the girls were still examining things."
    menu:
        "Buy a pin for Honoka": #+5 Affection Honoka
            jump GTS009_c1_1
        "Buy the headband for Naomi": #+5 Affection Naomi
            jump GTS009_c1_2
        "Save your money": #+0 Affection.
            jump GTS009_c1_3

label GTS009_c1_1:
    "Making up my mind, I took a pin with a silly nerdy design on it and took it to the cashier. The girls seemed to notice me pay for the item as they came over."
    show GTS neutral at Position(xcenter=0.25, yanchor=1.0)
    show BE neutral at Position(xcenter=0.75, yanchor=1.0)
    with dissolve
    BE "Hm? Whatcha get Kei-chan?"
    MC "Well I was looking around and I found one of these."
    "I showed her the pin, making her smirk as she examined the pin."
    show BE happy
    BE "You sly dog! Damn, I would have totally gone for that if I had seen it first. Nice design on it too."
    MC "Well, that's why I bought it for you. I remember you used to collect these."
    show BE surprised
    BE "W-what?"
    MC "Didn't you use to collect these? I was pretty sure you did. I can keep it if you don't want it."
    show BE angry
    BE "No I want it!"
    show BE surprised
    BE "I just didn't think you'd remember something like that..."
    $setAffection("BE", 5)
    show BE happy
    BE "Thanks Kei-chan."
    GTS "That was rather sweet of you Hotsure-san."
    MC "I just thought it'd make her happy."
    BE "Well you were right. Come on, let's keep exploring."
    scene black with fade
    "She grabbed my hand as she took the lead on our expedition. Naomi following behind as she held a smile on her face as she watched Honoka's renewed excitement as she dragged me around town until the sun began to set."
    jump daymenu

label GTS009_c1_2:
    "Making up my mind, I took the headband with the flower and took it to the cashier. The girls seemed to notice me pay for the item as they came over."
    show GTS neutral at Position(xcenter=0.25, yanchor=1.0)
    show BE neutral at Position(xcenter=0.75, yanchor=1.0)
    with dissolve
    GTS "Did you find something Hotsure-san?"
    show BE happy
    BE "Pfft! Hahahaha! Kei-chan! Already preparing to accessorize when your hair grows out?"
    MC "W-what!? N-no! This isn't for me."
    BE "Oooh? Is it for Tomo?"
    MC "No. But now that you mention it, I should probably get her something at some point too."
    MC "Either way. I got this for you Yamazaki-san."
    "Naomi placed a hand over her mouth as she let out a faint gasp upon seeing the headband."
    show GTS embarrassed
    GTS "Oh my."
    MC "I don't know why but I just thought of you when I saw it. I'm not really sure what type of flower that is, but I thought it was pretty. So... here you go."
    show GTS happy
    $setAffection("GTS", 5)
    GTS "Ara ara. Thank you very much Hotsure-san. Remind me later and I'll be more than happy to tell you what flower this is."
    "Naomi carefully put the headband on as I felt a nudge on my side as Honoka smirked and whisper."
    BE "Nicely done! Keep it up stud."
    "I felt a blush come over me as Naomi smiled at me after putting on the headband."
    GTS "Thank you again Hotsure-san. Shall we continue looking around town?"
    scene black with fade
    "There was a spring to her step as she left the store and we followed, Honoka spending the rest of the day whispering into my ears. It was either pickup lines or just general advances I could make."
    "Still, I didn't mind the constant advice as we enjoyed the rest of our journey until the sun began to set to signal the end of our day."
    jump daymenu

label GTS009_c1_3:
    "I looked at both items once more and then back to my wallet again. Sighing in defeat, I put my wallet away and left the items where they were. I may need the money later, so it was probably for the best."
    "I moved over to Naomi and observed the various landscapes on display."
    MC "Like postcards?"
    show GTS neutral at Position(xcenter=0.25, yanchor=1.0) with dissolve
    GTS "Yes. These are usually the things my mother sends me when she travels. These and occasionally a small trinket."
    MC "I take it she travels a lot then."
    GTS "On occasion. Normally with my father."
    MC "Did you travel a lot?"
    GTS "A decent amount yes. More so when I was younger."
    MC "You're lucky. I've always wanted to travel, see some landmarks and try out new foods. Must have been fun."
    show GTS happy
    GTS "Indeed it was. My sister and I did enjoy seeing other areas of Japan. We never left the country though unlike my parents."
    show BE neutral at Position(xcenter=0.75, yanchor=1.0)
    BE "Oh? Secret second honeymoons?"
    "Naomi and I both jumped as Honoka suddenly peeked around the corner of the aisle at us."
    show GTS embarrassed
    GTS "I... uh wouldn't know if that was the case."
    show BE happy
    BE "I'd love to travel too. Be cool seeing a lot of new places and experiencing other cultures."
    show GTS happy
    GTS "Hopefully you two get a chance to travel some time."
    show BE happy
    BE "As if I'd be so lucky. I'd need someone else to chip in to even get that chance. How about it Kei-chan? Want to circle the global together?"
    MC "I don't think I could so voluntarily put myself in endless debt like that with how much you like to spend."
    show BE angry
    BE "Oh hush! Traveling is all about enjoying life to the max. Money expenses be damned!"
    MC "Hence why I'm so hesitant to travel even off the island with you."
    show BE sad
    BE "So cruel..."
    show BE neutral
    BE "Oh well. Hopefully Yamazaki-san is right and we get that chance."
    GTS "I'm positive you will."
    show BE happy
    BE "Anyway, let's not spend the whole day in here. Come on! We got more of the town to explore!"
    scene black with fade
    "She bounced out of the shop as Naomi giggled and followed, leaving me shaking my head as I followed the two."
    "I later felt grateful that I hadn't spent my money as in another store Honoka's bust knocked over a display and I offered to buy an item that had broke. Naomi had offered to help to, but I didn't want her spending more than she already had that day."
    "Still, we shared a laugh over it by the end of the day. Honoka being annoyed with my suggestion of wearing a, CAUTION: WIDE TURNS, sign on her shirt. Either way it had been a good day and we even discussed possibly doing it again sometime."
    "I know I'd be more than willing to spend another day like that. Though next time I'll make sure I have a lot more money on me..."
    jump daymenu

label GTS010:
    $setSize(2)
    $setTimeFlag("aftersize2")
    scene Classroom with fade
    "A defeated sigh vacated my body. My hands had been slicking back my bangs all morning, and I could already tell this growth was going to be annoying."
    "I had only just recently had my hair trimmed, and already it was as long as before I had first gotten it cut."
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
    show GTS embarrassed at center
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
    $setProgress("GTS", "GTS013")
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
    show Ryoko neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    UNKNOWN "Howdy! You must be Hotsure-san."
    MC "Uh... yeah, I am. Hello."
    show GTS happy at Position(xcenter=0.75, yalign=1.0), Transform(xzoom=-1) with dissolve
    GTS "Hotsure-san, this is Ryoko Tanaka. Tanaka-san, this is Keisuke Hotsure. Tanaka-san is my next-door neighbor who I met a couple days ago, so I invited her over for some tea as well. I hope that isn't a problem."
    MC "No, it's all right. It's nice to meet you, Tanaka-san."
    Ryoko "Likewise, come on, have a seat."
    show GTS neutral
    GTS "Yes, Hotsure-san, please make yourself comfortable."
    "I nodded my head and removed my shoes before taking my place at the table. Naomi soon kneeled down beside me and poured me a cup of tea, to which I gave her a small nod."
    MC "Thank you."
    "Naomi gave a small nod in response as she gently set the teapot down, her hands subconsciously fixing her top to better hide her slightly exposed stomach before they rested in front of it to act as a cover."
    "Meanwhile, Ryoko scooted a little bit closer to me."
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
    Ryoko "Thanks Yamazaki-san. Yeah, me and a couple of students in the film club are working on a small movie together."
    MC "Oh wow, that's pretty cool."
    GTS "That does sound like it would be fun."
    show Ryoko happy
    Ryoko "Oh, it's totally a lot of fun! Sure, they're just silly no-budget videos but it's still a blast. You two should join us sometime, we're always open for auditions."
    show GTS embarrassed
    GTS "Me!? Oh no, I couldn't possibly do something like that. I wouldn't be capable of remembering a single line, or ignoring the camera. Or are you supposed to look at the camera? I'd gladly watch them, though."
    MC "Heh, I actually wouldn't mind giving it a go sometime. Also, with enough experience in front of the camera I'm sure you'd get the hang of it, Yamazaki-san."
    show Ryoko camera
    Ryoko "Yeah Yamazaki-san, you'd be a natural! You'd bring a sense of elegance last seen in the classic era of films. The tall, slender beauty the men are drawn to, who gives an aura of maturity and confidence."
    Ryoko "Just like um... Jessica Rabbit! That's the name."
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
    $setProgress("GTS", "GTS013")
    scene School Planter with fade
    play music Busy
    "I stepped into the garden expecting the normal serenity one would find there, but surprisingly it was more active than usual."
    UNKNOWN "Okay, this is a good spot right. Now if I set up here..."
    "The garden was normally a place of solitude for the students, but it was interrupted by a red haired girl carrying around what appeared to be a film camera. "
    "Noticing Naomi sitting under a tree and watching the girl, I decided to investigate what was going on."
    MC "Hey Yamazaki-san, what's going on here?"
    show GTS neutral at Position(xcenter=0.75, yanchor=1.0) with dissolve
    GTS "Good afternoon Hotsure-san. It appears Tanaka-san is location scouting."
    MC "Tanaka-san?"
    GTS "Yes, she's my neighbor at the dorm. We had been discussing-"
    UNKNOWN "Oh hey!"
    "The shout caught my attention as I turned to spot Tanaka rushing over with her camera in hand. The quirky girl smiling as she arrived back at us."
    show Ryoko neutral at Position(xcenter=0.25, yanchor=1.0) with dissolve
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
    MC "Um no..."
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
    Ryoko "..."
    Ryoko "Well okay, maybe not an animation. I can't draw to save my life and I especially don't know how to 3D model. But doesn't mean I can't find someone who does!"
    MC "Well films are a collaborative effort after all."
    Ryoko "Exactly right! Speaking of which. I should get back to the club to discuss ideas. Thanks so much for inviting me here Yamazaki-san. Got some great ideas for filming locations here."
    show GTS neutral
    GTS "You're welcome Tanaka-san. Please feel free to stop by from time to time."
    Ryoko "Oh I will be, after all have to see how this place looks at night. I already got ideas of where to place our ghost. This place is just perfect for a surprise haunted setting. I mean you can see it too right?"
    show GTS embarrassed
    GTS "I rather not think about it..."
    MC "Yeah this could work for a good ghost surprise."
    Ryoko "Mhm, well I'll see you two around. Oh and remember, if either of you two are interested in doing some acting just let me know. Later!"
    "She gave us a wink and a bow which Naomi returned in kind before Ryoko took off, barely giving me the chance to say goodbye."
    "We stood there for a second or two, but soon enough I gave a small chuckle and looked at Naomi."
    MC "Heh, me in a movie. I'd be a terrible main character, I'm better off being an extra. I'm a natural at just blending in to the background."
    show GTS neutral
    GTS "I think you'd do quite well."
    MC "Well thank you for the vote of confidence. Maybe I'll take her up on her offer. Who knows, maybe I'll win an award for best hair and makeup."
    "Naomi placed a hand over her mouth as I heard the faintest giggle at my joke. The corner of her smile peeking out from behind her hand which in turn got a smile from me."
    jump daymenu

label GTS012:
    scene School Planter with fade
    show GTS neutral at center with dissolve
    play music HigherEdu
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
    GTS "After all, the whole process is not about drinking tea, but about aesthetics; preparing a bowl of tea from one's heart."
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
    "We were silent for a little while after that, both sipping tea as I occasionally looked at her."
    "She didn't look taller since the last time we had tea, but it was honestly hard to notice on a day to day basis. Still, I hoped she was okay and not just saying so for my benefit."
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
    GTS "Anytime, Hotsure-san. We are study partners, after all, and it'd show poorly on me if I let you down already."
    "She giggled very softly, which resulted in a chuckle from me as we relaxed for a little longer before needing to go our separate ways."
    jump daymenu

label GTS013:
    $setProgress("GTS", "GTS014")
    scene Campus Center with fade
    play music Peaceful
    "{i}Shkt shkt shkt{/i}"
    MC "Hm."
    "{i}Pff pff{/i}"
    "{i}Shkt shkt shkt shkt shkt{/i}"
    MC "Hmmm..."
    if getSkill("Academics") > 4:
        MCT "The videos did not prepare me for this."
        "On a whim one calm Sunday afternoon, I found myself sketching an architectural diagram of the structure of the class building."
        "And yet, despite walking those halls almost every day for the past month..."
        MCT "How {i}did{/i} they place those ramps?"
    else:
        "I was pretty satisfied with the ninja I was drawing that calm Sunday afternoon. Nice shading on the hood, the fire on his katana was good and wavy."
        "But try after try, I couldn't make the face of his pet tiger look decent. Its eyes were too far apart, or the stripes looked wrong, or it looked like it was screaming into the void, et cetera."
    "I absently bounced my eraser tip off the pad as my brain spun in slow, creaky circles."
    MCT "...I {i}am{/i} feeling kind of hungry..."
    MCT "And there's a vending machine just inside the gym over there..."
    "Thus resolved, I slid my pencil into the spiral binding, closed the book, and stood."
    "The vending machine had just come into view within the concrete confines of the gym; that was when I spotted Naomi walking like a Heian countess my way, carrying a plate; the pristine white tea towel covering it wavered more for the breeze than her motion."
    show GTS neutral with dissolve
    GTS "Good afternoon, Hotsure-san. How do you do?"
    MC "Hey Yamazaki-san, I'm doing fine, thanks. What's that there?"
    GTS "It's a batch of shortbread cookies I made."
    MC "Oh, sweet, you made cookies? Can I try one?"
    show GTS surprised
    GTS "Well, I'm not sure they would be to your liking, Hotsure-san. This is my first time making this sort of thing."
    menu:
        "Please? I'm super hungry and they're probably just fine.":
            jump GTS013_c1_1
        "Well, if you insist. What are they for?":
            jump GTS013_c1_2

label GTS013_c1_1:
    $setFlag("GTS013_try")
    if isEventCleared("GTS012"):
        MC "If it's anything like your tea, I'm sure it'll taste lovely."
    else:
        MC "I'm sure you put heart and soul into them like everything you do."
    show GTS embarrassed
    "She glanced down at the cookies, biting her lips inwards, then looked back at me and nodded; she crouched down until the platter was at my chest level and lifted the tea towel."
    "Beneath it, like sugary embers, was a pile of crumbly-looking rounded square cookies which nigh glowed a golden cream color. I grabbed one from the edge and held it before my face."
    MC "Thanks, Yamazaki-san."
    "She looked down at the cookies and nodded."
    "And so, I brought it to my mouth and bit down with a crunch."
    $renpy.music.set_pause(True)
    scene black
    play sound "<from 0.0 to 2.0>Audio/SFX/sfx_bell.mp3"
    MC "Ng!"
    MCT "This is it. This is how I go out. I'll leave this world face down in a puddle of spittle and crumbs."
    "After penetrating the rock-like shards of the cookie's flesh, I found the texture gritty and the flavor an obscene subversion of all that is saccharine and mild. The anti-sweet aftertaste stuck to my gums like a bitter ghost."
    scene Campus Center with fade
    show GTS surprised with dissolve
    $renpy.music.set_pause(False)
    MC "Could use some salt."
    $setAffection("GTS", -2)
    show GTS sad
    GTS "I take your meaning."
    "My stomach sank to depths I didn't think the human body possessed."
    MC "Sorry, that was really rude of me, it just... kinda... caught me off guard."
    show GTS neutral
    GTS "Well, that's why I'm trying to learn."
    GTS "In fact, since you've already sampled my work as it were, perhaps you could provide a second opinion once Kodama-san has shown me the basics."
    GTS "Would you like to come with me to my lesson?"
    MCT "Well I {i}am{/i} still hungry."
    MC "Sure, sounds like a hoot."
    jump GTS013_c2

label GTS013_c1_2:
    show GTS happy-2
    GTS "Kodama-san is showing me how to bake like she does, and these are for her to judge how I can most improve."
    MC "Oh, wow, that's cool. You're really going the extra mile to be a good hostess."
    show GTS neutral
    GTS "It's only the right thing to do, by my reckoning."
    GTS "In fact, would you perhaps like to join me? I believe you could provide a much-needed second opinion."
    MCT "You're too good, Hotsure, too good."
    MC "Yeah, I'd love to. "
    if getAffection("PRG") > 6:
        extend " Maybe we'd both learn a thing or two. Kodama-san really knows her stuff."
        show GTS happy
        GTS "Manifestly."
        show GTS neutral
    jump GTS013_c2

label GTS013_c2:
    GTS "Very good, then. We had agreed to meet in the cooking classroom."
    MC "After you, Yamazaki-san."
    "She resumed walking with me following after; even with her taking such methodic, piecemeal steps to keep the plate so motionless, it was a trick to keep pace."
    stop music
    scene Hallway with fade
    show GTS neutral with dissolve
    "And yet, as we came within sight of the heavy doors it was she who puffed out a single, muted, yet alien sharp breath."
    menu:
        "Feeling a bit nervous?":
            jump GTS013_c2_1
        "(Say nothing)":
            jump GTS013_c3

label GTS013_c2_1:
    GTS "A bit. One never aspires to look the fool."
    GTS "Rationally, however, there is nothing to fear. Kodama-san is a long-suffering woman."
    MC "For sure, yeah. Worst case scenario, I try to make a batch and set the building on fire."
    GTS "Well, we did both agree to furnish our own supplies."
    "I gave her my most appreciative nod."
    MC "Sensible."
    jump GTS013_c3

label GTS013_c3:
    "Naomi, in a smooth motion, opened the door for us and stepped inside; my face sank into the gregarious, tickling scent of a labor of love at once."
    scene Cooking Classroom with fade
    play music PRG
    show GTS neutral at Position(xcenter=0.3, yalign=1.0)
    show PRG worried at Position(xcenter=0.7, yalign=1.0)
    with dissolve
    "A labor indeed, as we found Aida standing behind the counter, scanning an array of ingredients and instruments arranged with impeccable consideration for both ease of instruction and Naomi's reach."
    "Her hands were folded as she observed in silence, the young queen ruling softly but surely."
    show PRG neutral at Transform(xzoom=-1) with dissolve
    PRG "Hello, you two."
    "She bowed to us and we to her."
    PRG "Hotsure-san, ah... are you here to make something too?"
    MC "Oh, no, I'm just here to observe. Yamazaki-san invited me to try out her finished batch."
    PRG "Oh, uhm, okay."
    GTS "Thank you kindly for your patience, Kodama-san."
    PRG "I-It's no problem."
    PRG "So, um, first... we need to get the oven heated to 177 Celsius."
    show GTS happy
    GTS "Right away!"
    show PRG neutral at Transform(xzoom=1)
    show PRG neutral at center
    show GTS neutral at Position(xcenter=0.25, yalign=1.0)
    with dissolve
    "Naomi set her plate aside and tapped the oven screen to the tune of a staccato of beeps, winding down to a halt at the display of 177."
    show GTS at Transform(xzoom=-1) with dissolve
    "Meanwhile, Aida was peering under the tea towel at Naomi's cookies, smiling."
    PRG "Are these the ones you made, then?"
    if getFlag("GTS013_try"):
        show GTS sad
        GTS "They are, but I would like to tell you in advance that the taste may not be up to snuff."
        show PRG happy
        PRG "It's okay, Yamazaki-san. Everyone has to start somewhere."
    else:
        GTS "Yes, they are."
        PRG "They're really pretty."
        GTS "That's very kind of you, Kodama-san. Of course, I wouldn't expect them to live up to appearances. I'm rather unpracticed."
        PRG "Well, I don't think there's anything wrong with that. I-I'll do what I can to help you."
    "She brought one golden wafer to her face, and slipped one corner past her lips. With a modicum of effort, she bit it off."
    show PRG worried
    show GTS embarrassed
    PRG "Mm..."
    "Her jaw sashayed back and forth as she stared up at the ceiling."
    "She swallowed, then after a few moments more bit off a larger chunk; a few moments more, and she crunched down the rest of the cookie."
    PRG "Mmhm..."
    PRG "Okay, um, I think the... ingredients were a little off-balance... here."
    PRG "The salt and the... the vanilla are a bit strong."
    if getFlag("GTS013_try"):
        MCT "R.I.P. me."
    show GTS surprised
    GTS "Oh, I see. I confess, when I was preparing these I added more of those things than the recipe called for."
    show GTS embarrassed
    extend " I thought it would balance out all the butter."
    show PRG neutral
    PRG "It really does call for a lot, doesn't it?"
    show GTS neutral
    show PRG unique-happy
    PRG "A-And it's good to experiment. They do taste pretty good just going by the recipe, though."
    show GTS happy
    GTS "I will take that to heart."
    show PRG neutral at Position(xcenter=0.65, yalign=1.0)
    show GTS neutral at Position(xcenter=0.4, yalign=1.0)
    with dissolve
    "Naomi picked up the forearm-sized whisk laid out for her with one hand, and with the other, a bowl full of drooping little slabs of butter."
    GTS "It's 150 milliliters of butter, as I understand?"
    PRG "I think it's actually closer to 142 or 143, but 150 will do. You'd just have to add a little extra dash of every other ingredient."
    "Naomi nodded with billowing vigor as she coolly folded the butter, salt, and sugar over itself in waves."
    PRG "Oh, um... it's also important to mix the butter pretty vigorously, especially since you've thrown in the salt and sugar."
    GTS "Oh, that makes sense."
    PRG "And after that, you can pour in two and a half milliliters of vanilla extract."
    PRG "That stuff can be... pretty overpowering, too, if there's too much of it."
    "Naomi, watching the butter whip into un-shape with easy vigilance, laid the whisk down in the bowl and grabbed a petite glass bowl of the deep amber extract. She raised the vessel higher as she poured, a rock-steady flourish."
    PRG "Okay, that's looking good, you've got more of a cake frosting texture going. Now, you can mix in the flour. Just about a third of it at a time, though."
    PRG "That's 60 grams if you want to be exact."
    GTS "I see, I see."
    GTS "..."
    PRG "..."
    MC "..."
    GTS "..."
    PRG "..."
    MC "..."
    PRG "Y-You can um... go a bit faster than that, Yamazaki-san."
    GTS "Ah, but it is good to take one's time and do things as they ought to be done, is it not? Faster, slower, change shall come; that is the way of things."
    PRG "O-Okay, but the mixture is, um, starting to dry out."
    GTS "Ah. So it is."
    "The rest she mixed together just as Aida instructed, and repeated twice more."
    show PRG happy
    PRG "That looks good!"
    show PRG neutral
    PRG "Okay, once it's all mixed together, you can form it into a ball and... um... "
    PRG "Have you ever seen someone make the dough for a pizza?"
    "Naomi put a finger to her lips, and tapped it."
    GTS "I don't well remember it if I have."
    if getSkill("Academics") > 2:
        MC "Where you like mush the dough ball into itself?"
        show PRG neutral at Transform(xzoom=-1) with dissolve
        PRG "Yeah, exactly. That helps make sure there aren't any cracks or gaps in the dough."
        $setAffection("GTS", 1)
        show GTS happy
        GTS "Thank you, Hotsure-san."
        show PRG neutral at Transform(xzoom=1) with dissolve
        PRG "So yeah, you can do that, and then take it over to the mat and sort of... lightly throw it down, so it forms a brick shape."
        show GTS neutral
    else:
        MC "Where you like toss it up into the air?"
        show PRG worried at Transform(xzoom=-1) with dissolve
        pause 0.5
        show PRG unique-happy
        PRG "Um... not quite."
        show PRG neutral at Transform(xzoom=1) with dissolve
        PRG "The idea is to, um, kind of mush the dough into a ball to get rid of any cracks."
        PRG "After that, you just lightly throw it down on the mat until it forms a rough brick shape."
    GTS "Oh, I see. Very good."
    "She took the ball between her hands and rolled it tight, pausing every so often to press in each side."
    "With the dough formed into a near-perfect sphere, she cupped it in her hands over the floured mat..."
    "{i}pap{/i}{w}{i} pap{/i}{w}{i} pap{/i} "
    "...And sort of just let it plop down out of her hands, repeatedly, until it formed what could, with some trepidation, be described as like a brick."
    show PRG worried at Transform(xzoom=-1) with dissolve
    "As she was absorbed in this, I caught a glimpse of Aida's eyes diverting to the wall clock and her slight frown."
    show PRG neutral at Transform(xzoom=1) with dissolve
    PRG "That should do it. Next, we wrap it in seran wrap and use the dough cutter to refine its shape."
    GTS "And then allow it to chill for a few minutes in the refrigerator, if I'm not mistaken?"
    show PRG happy
    PRG "Mhm!"
    "In the most delicate use of plastic wrap I'd seen before or since, Naomi swaddled the dough in that crystalline sheet and patted its faces into flat, even planes, and at last deposited it into the refrigerator."
    show PRG neutral
    GTS "There we are."
    GTS "Well, where are my manners? How have you been, Kodama-san?"
    PRG "N-Not too bad. Thanks for asking."
    PRG "How about you two?"
    MC "Can't complain."
    GTS "Quite well. I've been very excited for you to teach me. I've always wanted to learn how to bake."
    PRG "You're welcome, Yamazaki-san. This is actually kind of fun."
    show GTS happy
    GTS "Nevertheless, I hope I can one day furnish an adequate repayment for your kindness."
    show PRG aroused
    PRG "Oh, um, y-you don't need to do that..."
    GTS "Surely your time merits something, as much skill as you clearly show."
    show GTS neutral
    GTS "Ah, but pardon me for gushing."
    show PRG neutral
    "Some milder talk came and went, where even I got in a word or two, and at last it came to our attention that a few minutes had passed."
    "Naomi took the dough back out, and her dancing fingers shortly undid the seal of the seran wrap."
    PRG "Okay, it looks like the oven's heated up..."
    PRG "So, for the last part, you'll wanna cut the dough into wafers a little less than two centimeters thick... pretty much exactly what you did with the practice batch."
    show PRG happy
    PRG "And then just put them in the oven! It, uh, should take about ten minutes, but you can tell when they're done when the bottom edges start to turn golden brown."
    GTS "That sounds simple enough."
    show PRG worried
    PRG "Yeah... but, um..."
    show GTS surprised
    PRG "I, um, have to go... Alice needs my help with... something."
    show GTS neutral
    show PRG neutral
    PRG "I think you've got it from here anyway."
    GTS "Thank you for the vote of confidence, Kodama-san. Thank you as well for your patience and superb instruction."
    PRG "Oh... well... thanks..."
    PRG "...Oh! If you save one or two of the cookies, I'd like to see how they turn out."
    GTS "Absolutely. I'll see you then. Be well, Kodama-san!"
    "She merely gave a sweet little nod and then a quick, yet proper bow to each of us before turning to leave."
    hide PRG with dissolve
    stop music
    show GTS neutral at Position(xcenter=0.55, yalign=1.0) with dissolve
    GTS "...Well, how fortunate that you came along, Hotsure-san."
    play music HigherEdu
    MC "Guess so. I had no idea Kodama-san's schedule was that tight, wow."
    "Naomi began slicing into the pine-colored dough with pensive precision. Her eyes held hazily on the task, as though her mind were elsewhere."
    GTS "One can't help but admire her sense of duty. It's just rather a shame where it seems to lead her."
    GTS "A bit more balance in her life would do wonders for her, I'd wager."
    MC "Tell me about it, that girl needs a vacation or something. Did I ever tell you the day I got here she was doing Nikumaru-san's chores for her?"
    GTS "I don't believe you did."
    "She shook her head slowly as she placed the cookie tray in the oven and set a timer for ten minutes."
    GTS "Well, I believe more than a vacation would be in order. The root of it is that her energies are invested in an irreciprocal relationship."
    if getSkill("Academics") < 2:
        MC "A what relationship?"
        GTS "In other words, she gives a good deal more in the relationship than she receives."
        MC "Oh."
        MC "Well, at least she gets paid for her time."
    else:
        "I shrugged."
        MC "At least she gets paid for her time."
    show GTS neutral at Transform(xzoom=1) with dissolve
    GTS "That's true. And yet there is clearly a certain lack of harmony for which the pay does not fully compensate. The effect on Kodama-san's nerves is apparent."
    menu:
        "I don't know if that's totally fair.":
            jump GTS013_c3_1
        "What do you mean, exactly?":
            jump GTS013_c3_2
        "I know, Nikumaru-san's such a douche sometimes.":
            jump GTS013_c3_3

label GTS013_c3_1:
    MC "We don't really know what their relationship is like in private, after all."
    show GTS angry
    GTS "I shudder to think of how much Nikumaru-san demands of her {i}away{/i} from prying eyes."
    MC "You asked her for some of her time, too, didn't you?"
    show GTS neutral
    GTS "That is true, and I will try to make her glad she agreed."
    GTS "I, however, would not offer her something as common as money as a ploy to oblige her to more than I could rightly ask."
    GTS "We must respect our fellows in matters small and great alike."
    if getSkill("Academics") > 4:
        MC "...Yamazaki-san, are you trying to... teach me something?"
        show GTS embarrassed
        GTS "I like to think of it more as sharing my thoughts."
        show GTS neutral
    jump GTS013_c4

label GTS013_c3_2:
    GTS "Well, I'll put it this way. We're both aware of all the things Kodama-san must keep track of and attend to simply as a matter of course."
    show GTS angry
    GTS "Add onto this all of the things Nikumaru-san demands of her as if she were merely an appendage; of course, no one in their right mind would go along with such a thing, unless one were to wave around some cash."
    GTS "In effect, Kodama-san has been goaded into exchanging half of her life for someone else's. Something as common as money hardly constitutes a fair trade."
    show GTS neutral
    GTS "Simply put, we must respect our fellows in matters small and great alike."
    if getSkill("Academics") > 4:
        MC "...Yamazaki-san, are you trying to... teach me something?"
        show GTS embarrassed
        GTS "I like to think of it more as sharing my thoughts."
        show GTS neutral
    else:
        MC "I guess that makes sense."
    jump GTS013_c4

label GTS013_c3_3:
    $setAffection("GTS", -1)
    GTS "Well, I don't know that I would go that far. In fairness, there very well {i}could{/i} be something I'm missing."
    GTS "I simply disagree with the nonchalance with which Nikumaru-san passes off such a volume of tasks onto Kodama-san."
    MC "Yeah, that's fair."
    jump GTS013_c4

label GTS013_c4:
    "I took in what she had to say for a second or two."
    MC "You know, I really never realized how much thought you must put into etiquette. It's kind of impressive."
    $setAffection("GTS", 1)
    show GTS happy
    GTS "Hm hm, thank you. I like to think my parents raised a lady."
    show GTS neutral
    "She paused and gave a glance over at the oven."
    GTS "Now I suppose there's no better time to think of what to do for Kodama-san as thanks."
    if isEventCleared("PRG007"):
        MC "You know... I saw her reading a book about the Kanagawa Koi the other day. Apparently she's a big fan."
        show GTS neutral
        $setAffection("GTS", 1)
        GTS "Oh, you don't say? That's very handy indeed, Hotsure-san. Perhaps I could obtain some memorabilia for her."
        show GTS despaired-thought
        GTS "Or see about treating her to an official baseball game, but then there's the question of how to arrange such a thing at her convenience."
        show GTS neutral
        GTS "Regardless, thank you for telling me that."
        MC "Sure. Like you said, she could use a little pick-me-up."
        "She nodded, and her eyes fell back upon the oven timer; the warmth flowing from the machine now carried a homey vanilla scent that settled like an old friend in my chest."
    else:
        MC "Hmm... maybe she'd like some high-end cooking gear?"
        GTS "That would be sensible. Unfortunately I'm rather unsure what to look for with that sort of thing."
        MC "Welp. That makes two of us."
        GTS "Oh well. It need not be decided this instant."
        "Thus, her eyes fell back upon the oven timer; the warmth flowing from the machine now carried a homey vanilla scent that settled like an old friend in my chest."
    "We passed the ticking minutes away ruminating over Naomi's technique during the preparation process, always with the unspoken question of 'how are they going to turn out this time?'"
    "And yet, somehow the hanging uncertainty didn't feel like tension."
    "Naomi ambled over to the oven just in time to turn off the timer a bare second before the alarm was due to go off."
    "Then, getting down on her knees, she reached into the oven with a pair of mitts the size of my head, withdrew the gold-beige bounty within, and set the sheet down on the stovetop. She at once began scooping them onto a cooling rack."
    MC "That smell's killing me already. How long do they have to cool for?"
    GTS "I would let them rest for at least a couple of minutes. You may have to blow on it."
    MC "Oh, okay."
    if getFlag("GTS013_try"):
        MCT "Be lying if I said I wasn't a {i}liiittle{/i} hesitant."
    "A few moments of silence passed, before Naomi spoke up from watching the windows in the hallway."
    GTS "Whatever happens, thank you for coming with me today."
    MC "Pff, you say that like it's gonna kill me."
    show GTS embarrassed
    MC "And there's only one way to really judge."
    GTS "You're right."
    "She clutched her skirt and hung unto a smile as I grabbed a still-hot wafer and puffed sharp breaths onto it."
    "After a few rounds of switching hands and repeating, I was content to take a bite."
    MC "{i}kholm{/i}"
    "I chewed it with the pensiveness of a judge. It was... buttery. Crumbly. A little sweet."
    MC "That was..."
    show GTS surprised
    extend " okay."
    show GTS happy
    GTS "Hooray!"
    "That made it all the sweeter. And so, I took another bite."
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
    MC "Yeah, have you ever given any thought about what job you might want to strive for?"
    GTS "I don't believe I have really. Did you have something planned already?"
    MC "I've been thinking about architecture as something I could do when I get out of school."
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
    "A cheer from the field attracted our attention as it seemed Honoka managed to score a goal. She ran along cheering before suddenly lifting her shirt and placing it over her head and sliding on the grass."
    "I couldn't help but chuckle as Naomi covered her mouth at Honoka flashing her sports bra to the rest of the team."
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
    show Ryoko happy at Position(xcenter=0.3, yalign=1.0) with dissolve
    "The bedroom had been transformed into a makeshift set, with extra curtains put up to eliminate any natural sunlight while other lights were set up to enhance the shot's lighting."
    "Two students I assumed were actresses were casually chatting to themselves while a couple of students worked to start putting away the camera, lighting, and various other bits of equipment."
    show GTS neutral at Position(xcenter=0.7, yalign=1.0) with dissolve
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
    "There was a gentle chirping up above as I looked up to see some birds, their chirping accompanying the soothing hum coming from Naomi."
    "A smile had been occupying my face throughout the course of our time together, but quickly vanished as a little yellow mass floated by my face."
    show GTS neutral with hpunch
    "Startled, I flinched lightly as the bee resumed its business, inspecting the flowers we were planting. Naomi must have noticed my movement."
    GTS "Is everything all right, Hotsure-san?"
    MC "Yeah, just got startled by a bee."
    GTS "Oh? You're not allergic, are you?"
    MC "No, just don't want to get stung is all."
    GTS "I see. No need to worry, then. As long as they are allowed to do their duty, they'll be more than happy to leave you be."
    MC "Heh, I guess you're pretty used to seeing bees around you, then?"
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
    "Her hands moved more delicately as she ensured the flower was securely buried while the bee did its business."
    "A grin appearing on my face as I watched them work together for a few moments before the bee moved on to another flower and Naomi was allowed to give the flower some water."
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
    "My brow lowered in annoyance as the wind blew my hair across my face yet again, my hands constantly trying to tuck it behind my ears or slick it back to keep my hair from doing so. I could see Naomi in our usual meeting place, attending to something."
    show GTS neutral at center with dissolve
    "Making my way over, I spotted a small collection of balls that appeared to be made of mud as I looked at Naomi."
    MC "What's with all the mud? Planning a mud ball fight?"
    GTS "Heh, no. This is merely something I used to do as a child whenever I had to wait for a while."
    MC "Ah, sorry to keep you waiting then."
    GTS "No need to apologize Hotsure-san, I merely arrived early."
    MC "I see... So does what you're doing have a name, or is it just something you came up with?"
    GTS "The activity is called the art of the hikaru dorodango. Which are these."
    "She placed a mud dumpling that she had been crafting into my hands, the orb roughly the size of a softball."
    "I could feel how compacted the dirt within was, but as my digits pressed a little bit more, cracks began to form on the surface of the ball before finally it started to crumble in my hands."
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
    GTS "There are a few ways one can do this. Just keep in mind that the process is more about patience rather than force. You can press the mud together through your own strength, but too hard and you'll end up breaking it."
    GTS "The process requires more of a gentle but frequent touch."
    "She demonstrated by adding another layer of mud, but this time rotating the ball in her palm as her other hand tenderly pressed on small imperfections."
    "Experience shined through as she was able to manipulate the ball faster, yet with more care as her palm would give small squeezes to the ball."
    MC "Okay, I think I see what you mean. How did you find out about this?"
    GTS "From my mother. She said that my sister and I used to be so impatient so she showed us something her parents had taught her. It seemed really silly to us at the time, simply playing with mud."
    GTS "But when she showed us what the end results looked like and we didn't believe her, we had her teach us."
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
    GTS "You carefully dust the ball with a fine dirt, and make a new layer along the surface."
    GTS "You then repeat this process a number of times with finer sifted dirt until you get the degree of smoothness you want. After which you gently wipe down the ball with a cloth."
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
    "I kept looking towards her as she remained silent. Occasionally she'd reach for more mud, increasing the size of her ball as it filled out more of her grasp."
    "I had to do the same to keep the ball evenly shaped, though I began to notice the more mud I added, the more delicate I would have to be, as too much pressure would make small flakes of mud crumble off."
    MC "Am I... doing it correctly?"
    $setAffection("GTS", 1)
    show GTS happy
    GTS "Yes, maybe be a little gentler. But you're doing well, Hotsure-san. Just keep in mind that the process is more about patience than force. You can press the mud together through your own strength, but too hard and you'll end up breaking it."
    GTS "The process requires more of a gentle, but frequent, touch."
    "She demonstrated by adding another layer of mud, but this time rotating the ball in her palm as her other hand tenderly pressed on small imperfections."
    "Experience shined through as she was able to manipulate the ball faster yet with more care than myself as her palm would give small squeezes."
    MC "Okay, I think I see what you mean. When did you learn about these?"
    show GTS neutral
    GTS "From my mother. She said that my sister and I used to be so impatient so, she showed us something her parents had taught her. It seemed really silly to us at the time, simply playing with mud."
    GTS "But she showed us what the end results looked like and we didn't believe her so we had her teach us."
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
    "Retrieving her canteen, she poured some more water onto the mud ball before her hand cupped my smaller one."
    "She placed her other hand underneath my turned palm to add some more stability, guiding my hand in hers while turning the ball and applying light pressure."
    show GTS neutral
    GTS "There's multiple ways one can go about doing this, so don't feel like you need to do it the way I'm showing you Hotsure-san. But sometimes being shown the way once is all one needs to find their own path."
    "Her voice was as soft as her hands as she showed me the way. Even with the mud from earlier, her hands were still warm and soft to the touch. As we worked together, a gentle humming came to emanate from her."
    "A soothing melody that went in pace with her hands, and I found it easier to gain a rhythm by following hers."
    "In no time at all, my dorodango was a passable appearance of sphere-like. It had some lumps still, and a little uneven here and there, but it would do."
    show GTS happy
    GTS "There we go. Now we just let these fully dry, and if you'd like we can continue the next steps at a later time, Hotsure-san."
    MC "What do the next steps involve?"
    show GTS neutral
    GTS "You carefully dust the ball with a fine dirt, and make a new layer along the surface."
    GTS "You then repeat this process a number of times with finer sifted dirt until you get the degree of smoothness you want. After which you gently wipe down the ball with a cloth."
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
    play music HigherEdu
    #SFX wind
    "There it was, again. The spring breeze always managed to blow my hair right over my eyes."
    MCT "One of these days, I'm just gonna gel my hair back..."
    "I continued down the path for a little bit longer, trying to ignore the raucous dance of my bangs. The breeze soon carried something else with it, however, as I could hear a faint giggle."
    "Further down the path I could spot Naomi waiting for me, a smile on her face framed by her deep black hair flowing majestically behind her, like silken smoke."
    "She looked upwards as the breeze made the tree branches above her sway, showering her cherubic face with illuminating sunlight."
    "The way she glowed in the light, the way she moved in harmony with the wind, made me think back to what Ryoko had said. Naomi really did capture the essence of a traditional beauty."
    "Her hand slid through her hair with her eyes closed, enjoying the chilly wind upon her face. When she opened her eyes again, she spotted me."
    show GTS happy at center with dissolve
    "Naomi's smile widened a bit as she greeted me."
    GTS "Good afternoon, Hotsure-san. I hope your day is going well."
    MC "Hello, Yamazaki-san. Did I keep you waiting?"
    GTS "Not at all. Please, have a seat."
    "Naomi patted the spot next to her upon the bench, and I sat there. Sitting this close to her, I must have looked like a child now at a full two heads shorter."
    GTS "Days like these are simply wonderful. A nice breeze, a warm sun, and the rustling of the leaves dancing high above the ground."
    MC "Yeah, it really is just about a perfect day out today."
    MC "So, did you want to get started on our studies?"
    show GTS neutral
    GTS "Yes, apologies for delaying us."
    MC "C'mon, no need to apologize. What should we cover today?"
    stop music
    UNKNOWN "Whoa! You're perfect!"
    "We both flinched at the sound of a new voice, and quickly looked over as another student jogged toward our bench. Her rather plump thighs jiggled rhythmically to each step."
    UNKNOWN "Hey there! Sorry for startling you, but you're just perfect!"
    "She beamed at Naomi with a fiery spark in her eyes."
    show GTS embarrassed
    GTS "I'm sorry, but I don't quite know what you mean."
    UNKNOWN "I mean that you're perfect! Like literally, you're just what we're looking for."
    "Naomi's lips hung parted, silent, her brow wringing. I couldn't blame her, as long as the girl's sudden approach remained a mystery. To my relief, she quickly continued."
    Fumika "Oh, I should introduce myself first, duh! I'm Fumika Usui, and I'm part of the basketball club! It's a real pleasure to meet you, miss...?"
    show GTS neutral
    GTS "Er... Naomi Yamazaki. A pleasure to meet you."
    "She gave a seated bow as the girl giggled and looked at me, making me realize that I needed to introduce myself too."
    MC "Keisuke Hotsure."
    play music Tension
    Fumika "Hey there! Is she your girlfriend?"
    MC "Huh...?"
    show GTS surprised
    GTS "P-Pardon?..."
    Fumika "Ah I see, still on the hush hush. Don't worry, I won't tell! Hee hee..."
    show GTS embarrassed
    GTS "..."
    MC "..."
    Fumika "Anyway, as I was saying. You're just perfect! Have you ever been interested in joining the basketball team? It's a ton of fun, and we’re in need of new players."
    GTS "Well... I hadn't really thought about it before, in truth."
    Fumika "Whaaa? How could you not? With your height and build, you'd be a {i}natural{/i}."
    GTS "It's simply something that hasn't crossed my mind. I do apologize, but I'm not much for athletic pursuits."
    Fumika "That's totally fine, we wouldn't throw you into the deep end at the start. We'd help you get the basics of the game down. Plus, there are other girls around your height. You won’t be alone!"
    GTS "Around my height?"
    Fumika "Of course! I mean, it's only natural to take what you're given as an advantage. Someone as tall as you would make an amazing center, but we typically leave point guard to the students who are... you know, more gifted in the chest!"
    Fumika "What do you think, Hotsure-san? She'd fit right in, wouldn't she?"
    "I was a little taken back at suddenly being reintroduced into the conversation. I spaced out for a few seconds, my unsuspecting brain cells weighing the case before me."
    "Naomi remained silent but turned to look down at me, her expression flat and muted... but expectant."
    menu:
        "You should totally give it a try, Yamazaki-san. I bet you'd be great at it.":
            jump GTS018_c1_1
        "You don't have to if you don't want to, Yamazaki-san. I'm sure she'll understand.":
            jump GTS018_c1_2

label GTS018_c1_1:
    Fumika "Totally!"
    GTS "Are you quite sure?"
    MC "Yeah! You’ll get to learn something new, and maybe make some new friends, too."
    GTS "That is true. I only worry that I have never been particularly good at sports."
    Fumika "Don't worry, when we're done with you you'll be an unstoppable dunking machine! I mean just picture it, being the star of the team!"
    $setAffection("GTS", -1)
    show GTS sad
    GTS "Apologies, I'm just not sure. Would it be alright if I took some time to think it over?"
    Fumika "Oh yeah, take as much time as you need! There’s no rush. We're normally practicing at the gym after class on Thursdays, so if you want, you can just stop by. We'll introduce you to the rest of the team."
    show GTS neutral at Transform(xzoom=-1)
    GTS "Thank you. I'll see if I have time to stop by."
    Fumika "Great! I'll see you there, then! Later you two!"
    stop music fadeout 1.0
    "With only a wave Fumika took off back towards the campus. I waited for a little bit to make sure she was gone before looking back towards Naomi."
    "I almost spoke before I noticed that she was looking away, her hand gently gripping her skirt."
    MC "Yamazaki-san? You okay?"
    GTS "Hm? Oh, yes, I'm fine. Well now, shall we commence to studying?"
    MC "Uh, yeah... here, let me get the textbook."
    show GTS neutral at Transform(xzoom=1)
    GTS "Thank you."
    pause 1.0
    MC "{i}ahem{/i}"
    pause 1.0
    MC "In 1185..."
    jump GTS018_c2

label GTS018_c1_2:
    stop music
    "There was a faint smile on Naomi's lips as she gave a slight nod."
    $setAffection("GTS", 2)
    show GTS neutral
    GTS "Would it be alright if I took some time to think it over?"
    Fumika "Yeah, that's perfectly fine. If you want, you can stop by some time and meet the other girls, too. We're at the gym after class on Thursdays, so if you're ever curious, just come visit and I'll be happy to introduce you!"
    GTS "Thank you, Usui-san. I'll be sure to come by and meet everyone."
    Fumika "Great! Can't wait to see you there. Well, I'll see you two later, then."
    play music HigherEdu fadein 1.0
    "She gave us a small wave as she took off back to the campus. I waited until I was sure she was out of earshot before I spoke."
    MC "Well, that was something."
    GTS "Indeed it was."
    MC "At least she's passionate about the team, so I can't fault her. Still, really random to just ask you like that. Are you okay? You seemed really uncomfortable there."
    GTS "Yes, I am fine. I do confess I'm unaccustomed to being approached like that. Well, apart from family get-togethers or my father's meetings. But even then, it was never so... impassioned."
    GTS "She spoke so rapidly, I could scarce make out half of what she was saying."
    MC "Yeah, it seemed so. I don't think anyone could have prepared for something as abrupt as that."
    show GTS happy
    GTS "Thank you very much for understanding."
    MC "Still... can't believe she thought we were dating."
    show GTS embarrassed
    GTS "...I can’t believe it, either. I didn’t think I was giving off that impression."
    "We both sat there silently for a few moments. Naomi idly swayed her long legs as she sat."
    MC "So... where were we?"
    GTS "We were about to study."
    MC "Oh, yeah! Let me just... get the book out."
    "I lingered on the thought for a while longer. The assumption about our relationship caught me off guard."
    "I could sense my face getting a little warmer as I opened the textbook, hoping to focus on something else."
    jump GTS018_c2

label GTS018_c2:
    stop music fadeout 1
    scene black with fade
    pause 1
    scene Campus Center
    show Ryoko neutral at Position(xpos=1.8, xanchor=1.0, yanchor=1.0)
    with fade
    play music Schoolday
    "The next morning was calm and sunny, only songbirds there to accompany the light chatter of the other students. That's how I immediately heard the clacking footsteps rapidly approaching me from the side."
    show Ryoko neutral:
        ease 0.75 xpos 0.65
    #Review this movement code above for use elsewhere.
    Ryoko "Morning, Hotsure-san! How you sleeping, good?"
    "In place of her usual pen, one hand clutched a crinkled bag of shrimp puffs, and the other a rolled-up sheet of what looked to be floral burgundy drapes."
    MC "Uh... yeah, fine?"
    "She didn't flinch a bit as I looked at her with palpable puzzlement."
    MC "How about you?"
    show Ryoko happy
    Ryoko "Just peachy, thanks!"
    show Ryoko neutral
    Ryoko "So hey, I got you a little pick-me-up if you want."
    "She held out the bag with a rustle and a smile, and out of instinct I slowly reached out to take it."
    pause 1
    MC "Thank you."
    pause 1
    MC "So you must realize that this looks extremely sus."
    show Ryoko annoyed
    "She faintly and briefly grimaced, looking down, as I took the bag and popped it open."
    show Ryoko neutral
    Ryoko "Well, it just so happens I saw the tail end of that little moment between you, Yamazaki-san, and Usui-san."
    show Ryoko embarrassed
    Ryoko "It also just so happens I sort of had something to do with that a bit."
    MC "Huh? How's that?"
    Ryoko "Well first, the facts. My roommate is in the women's basketball club. I told her about our good friend Yamazaki-san the other day which included, you know, describing her."
    Ryoko "And while I was aware that they were recruiting, I didn't think any harm would come if they happened to approach her."
    show Ryoko confused
    Ryoko "I didn't think {i}that{/i} would be how they approached her, either."
    MC "Yeah, a woman like Yamazaki-san you have to ease into things. There's a right way and a wrong way."
    show Ryoko neutral
    Ryoko "Apt. Which is why I've developed a contingency plan."
    MC "I see that. And what's the other half of your contingency plan?"
    show Ryoko happy
    "She patted the rolled cloth, hard."
    Ryoko "Tea mat! Thought the color would go great with her Hagi set."
    Ryoko "Speaking of whom, I'd better get moving if I'm gonna catch her in time. See you around Hotsure-san!"
    MC "See you."
    show Ryoko neutral:
        ease 0.5 xpos 0.01
    MCT "Hm...{w}tasty. Could use some water to go with these, though."
    show Ryoko tongue at Transform(xzoom=-1):
        ease 0.5 xpos 0.6
    Ryoko "Oh, and Hotsure-san... don't look so shocked next time someone mistakes Yamazaki-san for something she's not."
    Ryoko "If there {i}is{/i} a next time."
    show Ryoko neutral at Transform(xzoom=1):
        ease 0.5 xpos 0.01
    MC "Wait, what!?"
    jump daymenu

label GTS019:
    $setProgress("GTS", "GTS020")
    scene School Planter with fade
    "A gentle humming floated through the air as I stared up towards the clouds. There was a faint swishing noise a foot or two away from me as I laid in the shadow cast by Naomi."
    "A mixture of the sun's warmth along with the soothing melody caused my eyelids to begin growing heavy, as I hadn't a thought in the world besides taking in the moment."
    scene black with fade
    "Eventually a soft chuckle made me realize that I had fallen asleep at some point..."
    scene School Planter with fade
    show GTS happy at Position(xcenter=0.8, yalign=1.0) with dissolve
    "...as my eyes opened and I saw Naomi smiling down at me."
    play music Schoolday
    GTS "Very sorry Hotsure-san, I didn't mean to wake you."
    MC "That's okay. I, uh... wasn't aware that I had fallen asleep."
    GTS "Well, it is a very lovely day, so I can understand the appeal of just taking a nap."
    MC "Yeah, it's pretty peaceful today. How is the shodō going?"
    show GTS neutral
    GTS "It's going well, would you like to see?"
    "I sat up as Naomi placed her brush down onto the inkstone while I peeked at what she had created. The Kanji made me blush a little as I read, 'Dream' upon the paper before hearing a giggle above me."
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
    "I had no idea what I'd go with as I stared at the white canvas before me. Then, just like I had been inspiration for Naomi earlier, I decided she would act as my inspiration here."
    "I got to work, planning out my movements before my hands executed them. As long as I focused, I could get this done."
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
    "I pondered on what I could write down as a soft breeze blew my hair. That gave me the inspiration I needed, as I thought back to how peaceful the day felt and how it made me feel."
    "Smiling, I got to work with my project, making short strokes as I finished the art piece in a few minutes."
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
    GTS "True. Still, it's nice having company on days like these. So thank you."
    MC "Thanks for inviting me, is what I should be saying."
    "I leaned back and closed my eyes as I let the warmth of the sun bathe over me, my ears picking up Naomi shifting a little as she must have been getting comfortable as well. Laying back on the grass, I let out a sigh and smiled. This was a great day."
    jump daymenu

label GTS020:
    $setProgress("GTS", "GTS021")
    scene Roof with fade
    play music GTS
    "A light melody slid through my lips as I whistled to myself waiting, on the roof of the classroom building. Naomi seemed rather nervous when she had asked me to come by after class, so I was more than curious to see what was up."
    "This thought was interrupted, though, as my bangs drooped over my face again. Sighing in annoyance, I combed them back once more with my hand and cursed myself for not remembering to gel my hair back this morning."
    "I then heard the door open and saw Naomi walk through with a modest-sized bag."
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
    GTS "I practiced with Kodama-san a couple more times since my first attempt. She's very talented, so I learned a lot from her."
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
    MC "I said sure, where would you like to go?"
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
    "I raised a cookie up to her, her cheeks still a shade of crimson as she nodded and took it. We continued our conversation, shifting to more causal topics, but the mood was much happier."
    "Naomi smiled a little wider than usual, and I noticed her shift her body a little so it was slightly closer to mine."
    "We talked so long that we lost track of time, but that was okay since every moment felt better than the last."
    jump daymenu

label GTS021:
    $setProgress("GTS", "GTS022")
    scene School Planter with fade
    show GTS neutral at center with dissolve
    play music Peaceful
    "Having received a message from Minori about Naomi wishing to see me, I wandered into the garden with my eyes peeled and ears perked."
    "As my footsteps bent the blades of grass underneath, I spotted Naomi at her usual spot, a mat underneath her and another laid beside her. She sat with her hands rested peacefully on her lap as her eyes laid shut."
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

label GTS022:
    $setProgress("GTS", "GTS023")
    MCT "Huh boy, this isn't gonna look good."
    scene Library with fade
    "I kept one hand on the knob behind me to ensure it closed quietly."
    "The library was still as stone and the sun wouldn't shine through the windows for several hours, rendering the air gently illuminated in pale blue and white."
    "I passed by various students at various stages of growth, minds all silently at work, with steps as soft as I could manage. At last, perched by a window to the courtyard, I found her."
    show GTS neutral with dissolve
    play music Schoolday
    GTS "Good morning, Hotsure-san."
    MC "Good morning, Yamazaki-san."
    "She squinted a little and looked me up and down as I approached."
    GTS "Did something delay you?"
    MC "Indeed it did."
    GTS "...You're wearing slippers."
    "She squinted harder."
    GTS "Is that the remains of a tomato sauce stain I see on the bottom of your pant leg?"
    MCT "Ah nuts, I left that in?"
    MC "Suffice to say, I think whoever's in dorm 104 is going to have a very long day."
    GTS "Ah. I see."
    "I eased out a chair across from her and set my backpack by the leg of the table."
    MC "Hope you'll pardon the wait."
    GTS "You need not trouble yourself about it. I hardly noticed."
    "It struck me at that point that Naomi had a book open in her hands; moreover, she didn't set it down as I sat down myself."
    "Once I noticed that, I also noticed it was no math or science textbook, but a biography. 'The Life and Works of Nijō Yoshimoto', its cover of weathered gray fabric and its lettering of simple, bold strokes."
    MC "Hm! Got an itching for the classics, eh?"
    GTS "Yes, quite! I very much like the presentation here. The way the author weaves Nijō-sama's poems into accounts of his life is very thoughtful and evocative."
    GTS "I borrowed it yesterday, and I must confess I continued reading a bit after I would normally go to bed."
    MC "Wow, sounds like interesting technique. Maybe I should check that out."
    if getSkill("Academics") > 2:
        MC "Nijō-sama was a regent of the old Northern court for a while in the 1300s, if I remember right."
        GTS "Indeed. That's really what I find fascinating about it."
    else:
        MC "He was, like, Matsuo-sama's master, right?"
        GTS "Not quite. They actually lived about 300 years apart."
        MC "Oh."
        GTS "Nijō-sama was a regent and advisor of the high Northern court during the Northern and Southern Courts period."
        GTS "He was also quite a renowned poet, credited with bringing the renga style into much more widespread popularity."
        GTS "Its increased popularity likely paved the way for experimentation which eventually led to the development of the haiku as a genre, which is where Matsuo-sama came in."
        MC "Ohhhh, I see."
        GTS "Right. Really, that's what I find fascinating about it all."
    GTS "His time was one of relentless civil war. It's inspiring that he could take a step back and appreciate the subtle pleasures of life."
    MC "Wow, you really have some insight on this stuff."
    GTS "I have my dutiful father's tutelage to thank, and thankful I am."
    show GTS embarrassed with dissolve
    "Naomi suddenly looked down into the book, head tilting back and forth like a high branch in a whispering wind. Meanwhile, I found myself leaning forward on my elbows."
    GTS "I do admit, reading about it makes me think of some other aspirations I once had."
    MC "What kind of aspirations?"
    "She slipped a plain paper bookmark in the book and silently closed it. While putting the book into her own backpack, she answered."
    show GTS neutral with dissolve
    GTS "How familiar are you with the art of poetry itself?"
    menu:
        "Whose woods these are I think I know..." if getSkill("Academics") > 6:
            jump GTS022_frost
        "On a bright, calm day..." if getSkill("Academics") > 4:
            jump GTS022_nijou
        "There was an old drunkard from Devon..." if getSkill("Academics") > 2:
            jump GTS022_limerick
        "Not very, to tell you the truth.":
            jump GTS022_none

label GTS022_frost:
    MC "His house is in the village, though;{w} he will not see me stopping here to watch his woods fill up with snow."
    show GTS surprised with dissolve
    MC "My little horse must think it queer to stop without a farmhouse near,{w} between the woods and frozen lake, the darkest evening of the year."
    MC "He gives his harness bells a shake to ask if there is some mistake.{w} The only other sound's the sweep of easy wind and downy flake."
    show GTS aroused with dissolve
    MC "The woods are lovely, dark and deep.{w} But I have promises to keep, and miles to go before I sleep."
    MC "And miles to go before I sleep."
    "I let the silence hang a moment, as I deemed was fitting. As I looked across at Naomi, and gave thanks to whatever spirit helped me recite that piece from memory, I took in her swimming eyes and speechless, just-parted lips."
    GTS "Heavens, I don't quite know what to say. That was beautiful."
    MC "I had a feeling you'd like it."
    show GTS neutral with dissolve
    $setAffection("GTS", 1)
    GTS "That was astute of you, Hotsure-san. That piece was incredibly evocative and dare I say, more than a bit relatable."
    GTS "Pray tell, who wrote it?"
    MC "Robert Frost, a rather esteemed American poet from the 20th century. That particular piece was called, if I remember right, 'Stopping by Woods on a Snowy Evening'."
    GTS "Such a title is as fitting as any, I suppose. Well, interesting. Perhaps some branching out in my literature is in order."
    GTS "As a matter of fact, that's what I wanted to discuss with you."
    MC "Oh?"
    jump GTS022_c2

label GTS022_nijou:
    MC "...During a spring festival,{w} blossoms shine bright, and when the wind is at peace,"
    MC "I will bow my head and pray."
    MC "...Wow, I just realized how much of a showoff I must sound like."
    GTS "Not at all. I should think it perfectly appropriate under the circumstances."
    GTS "Was that from memory? That was rather impressive."
    MC "I can't take all the credit. It's very succinct, you know? In conjunction with the powerful imagery, maybe that's why it's so memorable."
    GTS "I agree entirely. I suppose in a way that's why we still read about him."
    MC "Well, anyway, what was your idea?"
    show GTS neutral with dissolve
    jump GTS022_c2

label GTS022_limerick:
    MC "...who died and ascended to heaven.{w} But he cried, 'This is Hades!{w} There are no naughty ladies,"
    show GTS surprised
    extend " and the pubs are all shut by eleven.'"
    show GTS angry
    $setAffection("GTS", -1)
    GTS "Hotsure-san, need I remind you that we are in public?"
    "I could just see her chewing the inside corners of her frown."
    MC "Sorry... I always thought that one was kinda funny."
    show GTS neutral with dissolve
    GTS "While that is quite novel, I suppose, it is not what I had in mind."
    MC "It'd, uh, probably be easier if you just tell me."
    jump GTS022_c2

label GTS022_none:
    GTS "That's fair, and your honesty is appreciated."
    GTS "I wonder if you might be willing to hear out an idea I was contemplating regardless?"
    MC "Of course, Yamazaki-san. Whatever you have in mind, I'll try not to bring you down too hard."
    "She nodded briskly."
    GTS "Nor I you."
    jump GTS022_c2

label GTS022_c2:
    GTS "So, I was wondering..."
    GTS "What if we were to collaborate on a renga poem of our own?"
    MC "You know... that could be fun."
    MC "It's been a good while since I went over the technique and rules and stuff, but yeah, I think we can brush up."
    show GTS happy with dissolve
    GTS "Admittedly, I have been."
    MC "Well!"
    GTS "Hm hm hm. I hope you don't think me overzealous."
    MC "Um, no, to be frank you're a long ways off from overzealous."
    show GTS neutral with dissolve
    GTS "That is comforting."
    MC "Well, I guess that's on me, then. Will it be alright if I take this evening to get ready?"
    GTS "Of course. Is there a time you would prefer?"
    MC "Say... tomorrow, after classes get out?"
    GTS "At the cornerstone of the day. That sounds perfect."
    MC "Perfect."
    MC "And what about the setting? Do you think the school courtyard would be suitable?"
    GTS "Oh, quite. And I don't think we would be disturbing anyone."
    MC "Well, there we are, then. Signed and sealed."
    menu:
        "Continue with the study session":
            jump GTS022_c3
        "Suggest inviting someone else":
            jump GTS022_invite

label GTS022_invite:
    $setFlag("GTS022_scribe")
    MC "...{w} Actually, though..."
    GTS "Hm?"
    MCT "I have a feeling she might like a little more authentic approach."
    MC "There's supposed to be a scribe who writes stuff down and, like, arbitrates the rules, right?"
    GTS "That's correct, yes."
    MC "Are you thinking what I'm thinking?"
    "She rested her chin on her upright palm, strumming her cheek once or twice."
    GTS "Matsumoto-san?"
    MC "Matsumoto-san."
    "I mimicked Naomi's posture as I glanced over toward the far wall of the room."
    MC "Shall I go extend an invitation?"
    show GTS happy with dissolve
    GTS "I think that's a fine idea, if you would."
    hide GTS with dissolve
    "I quietly slid out my chair, stood, and pushed it back in again before crossing back over to the far side of the library. I stopped and leaned against the wall next to the student organizations door."
    "And I pondered. I added and took away words in my head until I thought I had it just right. After half a minute or so, I bit the bullet and gently rapped on the door."
    play sound Knock
    pause 2
    AE "Come in."
    scene Office with fade
    show AE neutral with dissolve
    "Behind Matsumoto-san atop her desk were two perfectly level, perfectly square and, to me, frightfully tall stacks of documents. She stood facing me with the tip of a pen peeking out from between her fingers."
    AE "Good morning Hotsure-san. Do you need help finding something?"
    MC "No, not quite. Yamazaki-san and I were going to sit down tomorrow and compose a renga poem together, and we were wondering if you might be interested in joining as the scribe."
    "My error hit me like a snowball from the shadows."
    MC "Or you could be a poet too, if you want."
    AE "Beg pardon?"
    MC "A poet, like, for a renga poem?"
    AE "A... a what now?"
    MCT "Does she... not know what renga is?"
    MC "So, it's like this collaborative poem where one guy puts in a stanza, then another guy puts one in, and you go around in a circle. There's what they call a scribe who writes stuff down and arbitrates rules and stuff."
    MC "Yamazaki-san can probably fill you in more if you're interested."
    AE "I see."
    MC "Yeah. So, if we were to meet in the courtyard tomorrow after classes get out, would you want to join us?"
    "Without breaking eye contact, she put her free hands to her chin, where it lingered a moment or two."
    AE "Yamazaki-san is aware that you're inviting me?"
    MC "Yeah, 'course."
    show AE happy with dissolve
    AE "That could be fun, and I can fit it into my schedule provided we don't go on longer than two hours. I accept."
    MC "Awesome! Thank you so much, Matsumoto-san."
    show AE neutral
    AE "Now, how long after class ends, exactly?"
    "Snowball number two."
    MC "...Thirty minutes?"
    show AE neutral-eyebrow
    AE "Thirty minutes?"
    MC "Yes, um, thirty minutes."
    show AE neutral
    AE "Do you have the necessary supplies?"
    MC "Oh, yeah, natch. I even have a paperweight for you."
    AE "You've procured a writing desk?"
    MC "Writing..."
    MC "Um..."
    MC "A textbook probably wouldn't work, right?"
    show AE neutral-annoyed
    AE "No, it would not."
    MC "Right, yeah. Well, what if I bought a big cutting board? Would that be doable?"
    show AE neutral with dissolve
    AE "I imagine it would be."
    MC "Cool, I'll do that."
    "She nodded."
    AE "Very well then, I'll look into the rules and customs later. Is there anything else you wished to discuss?"
    MC "Nope, that was it."
    MC "Thank you again."
    "We exchanged a shallow bow and I turned to leave."
    hide AE with dissolve
    scene Library with fade
    show GTS neutral with dissolve
    "I took my seat again on the other side of the room while Naomi watched me with visible interest."
    MC "She agreed."
    GTS "Wonderful! I do believe her presence will enhance the experience a great deal."
    MC "For sure. I just gotta get some stuff tonight to prepare. And Matsumoto-san might have some questions for you about it beforehand."
    GTS "I'll be glad to explain whatever she needs."
    GTS "But what sort of supplies were you going to get? Perhaps that should be my responsibility, as hostess."
    MC "Not much. I was gonna pick up a cutting board or something for Matsumoto-san to use as the writing desk."
    GTS "There's no need to go out of your way. I think the writing desk in my room would serve perfectly fine."
    MC "Oh... okay, yeah."
    jump GTS022_c3

label GTS022_c3:
    MC "Anyway, should we get down to business?"
    GTS "We should."
    "She set the book back in her backpack and slid a neat stack of notecards into place in front of her. Meanwhile, I took out my notebook."
    GTS "Are you ready?"
    MC "Shoot."
    GTS "Very good."
    "She slid a nail under the top card, tucked it into her palm, and lifted it up to her face."
    GTS "What is the square root of sixteen squared plus eleven cubed?"
    MC "Uhhhh..."
    hide GTS with dissolve
    scene black with fade
    $setSkill("Academics", 1)
    "And so on for a few hours."
    if getAffection("GTS") > 20:
        "I was genuinely surprised how much seemed to stick afterward, even if it wasn't everything. Something about the way she relayed things just cleared the blocks in my brain."
        "I told her that, in fact. She thanked me with grace and efficiency."
    scene Dorm Interior with fade
    "By the end of the day I returned to my room and buckled down for... something, in retrospect, I'd have never guessed I'd end up doing in a hundred years."
    "It came a hell of a lot easier than algebra, though. This time there was a light at the end of the tunnel, and Naomi's veiled, giddy smile behind me."
    scene black with fade
    stop music
    pause 1.5
    scene School Planter with fade
    play music Peaceful
    "By my watch, I'd arrived at the courtyard with some five minutes to spare after emptying out my backpack at my dorm."
    if getFlag("GTS022_scribe"):
        jump GTS022_scribe
    else:
        jump GTS022_noscribe

label GTS022_scribe:
    "The task, then, was to actually find Naomi and Shiori in time."
    "I peered out with my hand over my eyes to try and spot them, but despite their distinct combination of figures I couldn't see them anywhere."
    AE "Hotsure-san."
    "Shiori's flat register sounded from a few meters away directly to my right; I looked, and lo, there they were tucked in the shade under a young painted maple."
    show GTS neutral at Position(xcenter=0.75, yalign=1.0)
    show AE neutral at Position(xcenter=0.25, yalign=1.0), Transform(xzoom=-1)
    with dissolve
    "I joined them in its spotted shadow; up close I could see a single branch hanging just by Naomi's head."
    GTS "I hope you approve the spot."
    "I nodded with consideration."
    MC "It's lovely."
    AE "Now then, this gives us a few minutes for you to contemplate your themes and composition. Hotsure-san, as I understand you took the initiative in organizing this session, the first stanza falls to you. We will alternate from there."
    MC "Oh yeah! Sure, lemme think."
    "I sat back with the grass and dirt snaking around my palms, and I cast my eyes on high. Warm sighs of breezes came floating down on needles of sunlight. A hundred white-green leaves waved to a tune I couldn't hear."
    "So I closed my eyes, to let myself hear the birds, frogs, and cicadas; it seemed they had more to say than the students all around."
    if getSkill("Art") > 4:
        MC "'Neath our thickest shade, your voice we oft have heard, yes... the noon o'er heaven."
        show AE happy with dissolve
        AE "Well!"
        AE "A surprise to be sure, but a welcome one. Good work, Hotsure-san."
        MCT "...I don't know what she thinks I did but I'm just gonna roll with it."
        MC "Thanks."
        show AE neutral with dissolve
    else:
        MC "..."
        "My eyes opened."
        MC "Hm..."
        MC "Take us under wing, maple and nests high above; haze again rolls off."
        AE "I believe you're missing a cutting word."
        MC "Oh yeah. Uh..."
        MC "Takes us under wing, we below and nests above; haze again rolls off."
        AE "Good."
    "Shiori wrote down my contribution in straight, speedy lines."
    AE "Yamazaki-san?"
    show GTS happy with dissolve
    "She seemed to barely suppress a grin as her stanza flowed out like a stream."
    GTS "Dew on the blossom, we pray. Flutter in the sky, we learn."
    show GTS neutral with dissolve
    AE "Very good."
    AE "Hotsure-san?"
    "I was, however slowly, realizing the challenge of maintaining a coherent flow on top of the various regulations Shiori so dutifully held us accountable for."
    "I leaned forward to think."
    MC "..."
    if getSkill("Art") > 4:
        extend " Skylark in her nest, never fearing the far earth, chirps up to the sun."
        "Another nod, another scribble."
    else:
        extend " Skylark in her humble nest, never fearing the far earth, chirps up to the sun."
        AE "Your first line contains seven mora. You have to shorten it to five."
        MC "Ah, crud. Hmm..."
        MC "Skylark in her nest, never fearing the far earth, chirps up to the sun."
        AE "That'll suffice."
    AE "Yamazaki-san?"
    "At the very least, I was not alone. Naomi leaned back against the tree in the muffled throes of ponderment."
    GTS "...Earth and sun and wind betwixt, gladly received, never missed."
    AE "Hotsure-san?"
    if getSkill("Art") > 4:
        MC "Let them to and fro, write their journeys on the wind bound from east to west."
    else:
        MC "Nutshell plunges, crack! Up again on mother's wings, her young ones to feed."
        AE "I think you need to try a bit harder to connect it to the previous verse. Try again, please."
        "My head bowed, my neck suddenly bereft of strength."
        MC "I writhe and I groan, praying the spirits aid me. Poems hurt my soul."
        show AE neutral-annoyed
        AE "You were the one to organize this session, Hotsure-san. Kindly take it seriously."
        GTS "Don't give up, please. You've been doing rather well."
        show AE neutral
        MC "Right, sorry. Lemme try that one again."
        MC "Uh... earthworm swimming up, up again on mother's wings, her young ones to feed."
        "Shiori nodded."
    "At once I saw Naomi's gaze float up and away from us, while her oscillating fingers gently pinched her skirt.{w} She pondered a moment or two more after Shiori finished writing, then raised a finger."
    GTS "Let us dine in kind someday soon, and bestow each other kinship."
    show GTS sad with dissolve
    GTS "Oh, drat, that's too long."
    AE "Right."
    "She labored in silence at revising her stanza, fingers strumming, teeth on her lips."
    show GTS neutral with dissolve
    GTS "Let us sit down one day and, see our selves in a tea cup."
    MCT "Not a twinge of enjoyment on her face that time, either."
    MCT "She was obviously really looking forward to this, but now I don't know if this is what she really wanted."
    MCT "Could it be partly my fault? I know I'm probably not throwing out the best material to work with..."
    menu:
        "Keep going":
            jump GTS022_c4a
        "Call off the session":
            jump GTS022_cutoff_a_early

label GTS022_c4a:
    MCT "Probably just growing pains."
    show AE neutral-eyebrow
    show GTS neutral at Transform(xzoom=-1) with dissolve
    MCT "Heh."
    MCT "Oh crap, they're staring. Uh..."
    if getSkill("Art") > 6:
        MC "Pray scatter the mist, you mountain wind among us, that the warmth be clean."
        show GTS neutral at Transform(xzoom=1) with dissolve
        "Naomi, suddenly roused to attention, gave me a gentle nod."
    else:
        MC "Let's have another, because green tea tastes awesome, even with a... bird?"
        show GTS neutral at Transform(xzoom=1) with dissolve
        AE "The tone is too far off from the rest of the body. Try again."
        MC "Uh... please disperse the mist, oh great, howling mountain wind, for it's too humid."
        AE "I suppose that fits."
    pause 1
    GTS "Well..."
    pause 1
    GTS "Hmm..."
    GTS "Ah! The high chill may stay a while, 'till...{w} 'till, um..."
    show AE neutral-eyebrow
    GTS "'Till off it goes its own way."
    "I barely caught Shiori giving me a stony yet expectant glance, but it was gone like the flicker of a candle."
    menu:
        "Keep going":
            jump GTS022_c5a
        "Call off the session":
            jump GTS022_cutoff_a

label GTS022_c5a:
    show AE neutral
    if getSkill("Art") > 4:
        MC "So all has been drank, now let us straighten ourselves, for her, down below."
        GTS "Oh!"
    else:
        $setFlag("GTS022_late")
        MC "I think now, we should hurry down the side, for my love awaits."
        GTS "Oh, interesting."
    GTS "Let me think, now..."
    show GTS neutral at Transform(xzoom=-1) with dissolve
    pause 1
    show GTS sad with dissolve
    "Every stanza, I could now tell, was taking longer. What I couldn't tell was how much of Naomi's visible displeasure was effort or just simple disappointment."
    show GTS neutral at Transform(xzoom=1) with dissolve
    GTS "She awaits among cedars, roots below, her leaves in heav-"
    GTS "No."
    GTS "She awaits among cedars, roots below, leaves in heaven."
    AE "I think that lingers a bit too long on the theme of nature...{w} but I don't think any harm will come if we overlook that."
    GTS "No, no, you were right. I think I can fix it."
    pause 1
    GTS "Her face is like a blossom, yet in her hands rests my heart."
    menu:
        "Keep going":
            jump GTS022_c6a
        "Call off the session":
            jump GTS022_cutoff_a

label GTS022_c6a:
    if getSkill("Art") > 4:
        $setFlag("GTS022_late")
        MC "Eyes command the heart, but her temp'rance guides my feet down a peaceful road."
        show GTS embarrassed with dissolve
    else:
        MC "Long is the journey, but not too long I don't think, while she's at the end."
    pause 1
    show GTS sad with dissolve
    GTS "Hmm..."
    GTS "Ahh..."
    "Shiori looked down at the notebook with her pen perched."
    GTS "Behold...{w} on the mountainside, a cane, a cloak, and a hearth."
    menu:
        "Keep going":
            jump GTS022_c7a
        "Call off the session":
            jump GTS022_cutoff_a

label GTS022_c7a:
    MC "Behold in the vale, a phoenix, a nightingale, and an eight-span crow."
    "Naomi nodded, looking down at the dust below."
    GTS "..."
    AE "..."
    MC "..."
    GTS "Their eyes have observed all sums; all that's left now is the morning sun."
    AE "I'm afraid your second line is two mora too long. Please try again."
    show GTS sad with dissolve
    GTS "I see..."
    GTS "Would it be too inconvenient... if we picked this up again some other day?"
    AE "Not at all."
    MC "No, if you want to, that oughta be okay."
    GTS "Very well."
    show GTS neutral with dissolve
    GTS "Thank you very much for sitting down with us, Matsumoto-san."
    AE "Likewise, Yamazaki-san. That was rather nice while it lasted."
    AE "If it's all the same to both of you, I believe I'll keep what we have so far."
    GTS "Oh, uh, yes. If you wish."
    MC "Yeah, for sure."
    GTS "Do take care, Matsumoto-san."
    show AE happy with dissolve
    AE "Likewise, Yamazaki-san."
    "We all stood to leave, nothing more to say left among us."
    hide AE
    hide GTS
    with dissolve
    scene Hallway with fade
    "Naomi said nothing as we took the same path out of the building."
    MC "How did you feel about that whole thing? It might not've lived up to expectations, I guess."
    "She slowed to a stop, and sighed."
    show GTS angry with dissolve
    $setAffection("GTS", -1)
    GTS "No, it didn't."
    MC "Well, I'm sorry. Not much we can expect from our very first time doing something that involved."
    GTS "I know, but I thought after all I've read and studied, I could at least stick to regulations, let alone keep the prose thematically balanced."
    show GTS neutral with dissolve
    "She continued walking but said nothing for a moment."
    GTS "I suppose there's little use dwelling on it."
    MC "Think you'll feel more up to it down the line?"
    GTS "Perhaps. One never can tell, can they?"
    MC "I guess not."
    jump daymenu

label GTS022_cutoff_a_early:
    MC "Uhh..."
    MC "Sorry to do this, but is it cool if we pick this up some other time?"
    show GTS surprised
    GTS "Hm? Are you quite sure?"
    MC "I'm afraid so. Maybe this just isn't my scene but I'm not feeling it today."
    AE "I see."
    show GTS sad with dissolve
    GTS "Perhaps we could try again some other time, then?"
    MC "Oh, for sure, yeah. We can do that."
    AE "Very well. If it's all the same to you, I think I'll keep what we have so far."
    show AE happy with dissolve
    AE "Thank you for inviting me. It may have been awkward with my doing this for the first time, but I thought that was quite enjoyable for what it was."
    show GTS neutral with dissolve
    MC "'Course!"
    GTS "Thank you very much for joining us."
    "We bowed in turn and gathered our things to part ways."
    hide AE
    hide GTS
    with dissolve
    scene black with fade
    $setAffection("GTS", -2)
    "To my surprise, Naomi said nothing to me whatsoever afterward."
    "I didn't exactly lie, but I wouldn't have done it if I didn't think she felt the same."
    "And I could've sworn she was giving off hints that she did."
    "I guess not."
    jump daymenu

label GTS022_cutoff_a:
    MC "Uhh..."
    MC "Sorry to do this, but is it cool if we pick this up some other time?"
    show GTS surprised
    GTS "Hm? Are you quite sure?"
    MC "I'm afraid so. Maybe this just isn't my scene but I'm not feeling it today."
    AE "I see."
    show GTS sad with dissolve
    GTS "Perhaps we could try again some other time, then?"
    MC "Oh, for sure, yeah. We can do that."
    AE "Very well. If it's all the same to you, I think I'll keep what we have so far."
    show AE happy with dissolve
    AE "Thank you for inviting me. It may have been awkward with my doing this for the first time, but I thought that was quite enjoyable for what it was."
    show GTS neutral with dissolve
    MC "'Course!"
    GTS "Thank you very much for joining us."
    "We bowed in turn and gathered our things to part ways."
    hide AE
    hide GTS
    with dissolve
    scene Hallway with fade
    "We split off each our own way; as for me, I went back inside to let my mind wander to the next diversion."
    "That is, until Naomi approached me from behind and gently, distinctly called my name."
    show GTS neutral with dissolve
    GTS "That must have been a difficult position. Please believe me when I say I didn't intend to put you on the spot."
    MC "Maybe. I wouldn't worry about it, though."
    MC "To be honest, I did it as much for you as for me."
    GTS "How do you mean?"
    MC "Well... was I wrong thinking you started to really have to force yourself?"
    MC "And the effort didn't look enjoyable for you at all."
    show GTS sad with dissolve
    GTS "I see."
    GTS "I hope it wasn't so obvious to Matsumoto-san. But..."
    MC "I'm sure she gets it."
    show GTS neutral with dissolve
    GTS "I'm sure, too."
    "She looked down and puffed out a sigh."
    GTS "If only life were gentler about showing us our shortcomings."
    MCT "Don't say it don't say it don't say it"
    MC "Well, clearly you have a number of strengths to balance things out."
    show GTS neutral at Transform(xzoom=-1) with dissolve
    if not getFlag("GTS022_late"):
        $setAffection("GTS", 1)
    GTS "In any case, I appreciate your discretion."
    MC "I try to take my shots when I see 'em, Yamazaki-san."
    "She only chuckled softly."
    MC "Well... until next time?"
    GTS "Until next time."
    hide GTS with dissolve
    "We parted ways one more time that day. And I thought at that moment that a can of tea sounded just lovely."
    jump daymenu

label GTS022_noscribe:
    "The task, then, was to actually find Naomi in time."
    "I peered out with my hand over my eyes to try and spot her, but despite her distinct silhouette I couldn't see her anywhere."
    GTS "Hotsure-san?"
    "The singular, soft rustle of Naomi's voice pointed me a mere couple of meters to my right. She was sat in the mottled shadow of a young painted maple, with her hands on her folded knees and a small writing desk in front of her."
    show GTS neutral with dissolve
    GTS "I hope you approve the setting."
    "I sat down next to her in its shade and nodded with consideration."
    MC "It's lovely."
    GTS "If I may say so, I agree entirely."
    GTS "Now then, we may as well start by taking a minute or two to think of what we want to write."
    MC "Right, yeah. Think I'm gonna need it."
    GTS "Well, as this was my idea in the first place, I believe the composition of the hokku falls to me."
    MC "I guess so..."
    "I leaned back as I said it, and took in the scene to see what to reflect on."
    "And I felt myself taking in the scene literally, as the grass snaked around my palms and the shift of my weight pressed bare, cool dirt into my skin."
    "The airier elements meanwhile danced above without a care, the needles of the sun's heat and light swayed by the sky's whispers."
    MC "..."
    "Some changeless minutes went by... admittedly, I wasn't sure how many... and then Naomi eased herself straight upright."
    GTS "Take us under wing, maple and nests high above; haze again rolls off."
    if getSkill("Art") > 4:
        MC "Good prose... but..."
        GTS "I forgot the cutting word."
        "She stared dead ahead, at nothing I could see."
        GTS "Thank you, Hotsure-san."
    else:
        "She stared dead ahead, at nothing I could see."
        GTS "I forgot the cutting word."
        MC "Oh, um... yeah."
        GTS "Bother. Hmm..."
    MC "Well hey, what about...{w} like..."
    MC "Take us under wing, we below and nests above; haze again rolls off."
    GTS "Ah, yes, that fits the bill."
    GTS "Actually, would you mind if I composed the waki? I know it's unorthodox, but I feel I have a good idea."
    MC "Go right ahead!"
    "She closed her eyes for barely a stanza's breadth."
    GTS "Dew on the blossom, we pray. Flutter in the sky, we learn."
    MC "Hm! I'd say that's worth it."
    GTS "Thank you."
    "She silently recorded our first two stanzas in long, wistfully fading lines on her notebook sheet."
    GTS "And {i}now{/i} it's your turn."
    MC "Right."
    MCT "I still got nothing."
    "I leaned forward to think, spreading some dirt on my knee and chin."
    MC "..."
    if getSkill("Art") > 4:
        MC "Skylark in her nest, never fearing the far earth, chirps up to the sun."
    else:
        MC "Skylark in her humble nest, never fearing the far earth, chirps up to the sun."
        GTS "Ah, Hotsure-san, that first line is just two mora too long. How might you amend it?"
        MC "Oh, um..."
        MC "Skylark in her nest, never fearing the far earth, chirps up to the sun."
        GTS "See? That sounds much better."
    "She wrote it down with a nod, sending her long raven locks aflutter. Would it have been too much to bring the topic around to that? For the moment, I deemed so."
    "I realized as she came to an utter stillness that she was thinking just as hard as I was."
    GTS "...Earth and sun and wind betwixt, gladly received, never missed."
    "She paused a moment, and wrote it down."
    if getSkill("Art") > 4:
        MC "Let them to and fro, write their journeys on the wind bound from east to west."
    else:
        MC "Nutshell plunges, crack! Up again on mother's wings, her young ones to feed."
        show GTS happy
        "She suddenly smiled."
        GTS "I like the use of onomatopoeia."
        MC "...But?"
        show GTS embarrassed with dissolve
        GTS "One might consider it a marked departure from the theme of the last verse."
        MC "Ah, yeah, you're right."
        "I leaned back again and the puff of hot breath from my lips brushed the errant strands from my face."
        MC "Dude, this is, like, hard."
        show GTS neutral with dissolve
        GTS "Please don't give up. You're actually doing rather well, it's just a question of adhering to standards."
        MC "Thank you, Yamazaki-sensei."
        GTS "Hm hm. Perhaps more homework is in order?"
        MC "Oh please, God, no."
        GTS "Very well then, let's settle for practice. Continue, if you please."
        MC "Okay, uh..."
        MC "Earthworm swimming up, up again on mother's wings, her yound ones to feed."
    GTS "Very good."
    "Naomi set her pen down, and I saw her gaze float up and away from me. Her oscillating fingers pinched her skirt in waves."
    "And she sat there for a moment or two, brewing."
    "And in that couple of moments, with no other verse to contemplate, all I could contemplate was Naomi."
    "She then raised a finger as the words came to her."
    GTS "Let us dine in kind someday soon, and bestow each other kinship."
    show GTS sad with dissolve
    GTS "Oh, drat, that's too long."
    "She labored in silence at revising her stanza, teeth on her lips."
    show GTS neutral with dissolve
    GTS "Let us sit down one day and, see our selves in a tea cup."
    MCT "Not a twinge of enjoyment on her face that time, either."
    MCT "She was obviously really looking forward to this, but now I don't know if this is what she really wanted."
    MCT "Could it be partly my fault? I know I'm probably not throwing out the best material to work with..."
    menu:
        "Keep going":
            jump GTS022_c4b
        "Call off the session":
            jump GTS022_cutoff_b_early

label GTS022_c4b:
    MCT "Probably just growing pains."
    show GTS neutral at Transform(xzoom=-1)
    MCT "Heh."
    MCT "Oh crap, she's staring. Uh..."
    if getSkill("Art") > 4:
        MC "Pray scatter the mist, you mountain wind among us, that the warmth be clean."
        show GTS neutral at Transform(xzoom=1)
        "Naomi, suddenly roused to attention, gave me a gentle nod."
    else:
        MC "Let's have another, because green tea tastes awesome, even with a... bird?"
        show GTS neutral at Transform(xzoom=1)
        GTS "I think that could be made a bit more tonally consistent."
        MC "Uh... please disperse the mist, oh great, howling mountain wind, for it's too humid."
        "She absently wrote down my contribution."
    pause 1
    GTS "Well..."
    pause 1
    GTS "Hmm..."
    GTS "Ah! The high chill may stay a while, 'till...{w} 'till, um..."
    GTS "'Till off it goes its own way."
    menu:
        "Keep going":
            jump GTS022_c5b
        "Call off the session":
            jump GTS022_cutoff_b

label GTS022_c5b:
    if getSkill("Art") > 4:
        MC "So all has been drank, now let us straighten ourselves, for her, down below."
        GTS "Oh!"
    else:
        $setFlag("GTS022_late")
        MC "I think now, we should hurry down the path, for my love awaits."
        GTS "Oh, interesting."
    GTS "Let me think, now..."
    show GTS neutral at Transform(xzoom=-1) with dissolve
    pause 1
    show GTS sad with dissolve
    "Every stanza, I could now tell, was taking longer. What I couldn't tell was how much of Naomi's visible displeasure was effort or just simple disappointment."
    show GTS neutral at Transform(xzoom=1) with dissolve
    GTS "She awaits among cedars, roots below, her leaves in heav-"
    GTS "No."
    show GTS neutral with dissolve
    GTS "She awaits among cedars, roots below, leaves in heaven."
    "She was about to write it down, but stopped in the midst of her first stroke."
    GTS "That's lingering a bit too long on the theme of nature, isn't it?"
    MC "I mean, it sounds solid to me. Maybe we can bend the rules this once?"
    GTS "We've bent the rules a few times already, have we not? Committing to the art means committing to the form."
    MC "That's true, I suppose."
    "She nodded, and set to pondering once again."
    GTS "Her face is like a blossom, yet in her hands rests my heart."
    menu:
        "Keep going":
            jump GTS022_c6b
        "Call off the session":
            jump GTS022_cutoff_b

label GTS022_c6b:
    if getSkill("Art") > 4:
        $setFlag("GTS022_late")
        MC "Eyes command the heart, but her temp'rance guides my feet down a peaceful road."
        show GTS embarrassed with dissolve
    else:
        MC "Long is the journey, but not too long I don't think, while she's at the end."
    pause 1
    show GTS sad with dissolve
    GTS "Hmm..."
    GTS "Ahh..."
    GTS "Behold...{w} on the mountainside, a cane, a cloak, and a hearth."
    menu:
        "Keep going":
            jump GTS022_c7b
        "Call off the session":
            jump GTS022_cutoff_b

label GTS022_c7b:
    MC "Behold in the vale, a phoenix, a nightingale, and an eight-span crow."
    "Naomi nodded, looking down at the dust below."
    GTS "..."
    MC "..."
    GTS "..."
    MC "..."
    GTS "Their eyes have observed all sums; all that's left now is the morning sun."
    "After a second, she looked off into the distance and mouthed some numbers in sequence."
    GTS "That's..."
    show GTS sad with dissolve
    GTS "Too long."
    pause 1
    GTS "Would it be too inconvenient... if we picked this up again some other day?"
    MC "No, I don't think so."
    MC "Is anything wrong?"
    show GTS neutral with dissolve
    GTS "Well, I think it would be best to see this more as a practice run."
    GTS "We can pick this up again some other time, and we'll have a better idea of how to maintain the flow."
    MC "That... makes sense..."
    MC "Are you sure we can't keep this one to, like, punch it up or something? I think you're selling your contributions short."
    GTS "That's kind of you to say."
    GTS "I suppose we can keep it if you really want to. Would you mind holding onto it in the meantime?"
    MC "For sure."
    "She folded the perforation in the paper twice on its self and then, *{i}shrip{/i}*, she cleanly tore it from the binding. I took it with a nod."
    MC "Thanks."
    GTS "You're welcome."
    GTS "I suppose this is goodbye for now."
    MC "I suppose so. Take care, Yamazaki-san."
    GTS "And you as well, Hotsure-san."
    "I stood and she crouched to leave."
    hide GTS with dissolve
    $setAffection("GTS", -1)
    "I paced slowly back towards the door, opting to look over our work; we had produced just short of a page, one-sided."
    "My eye lingered on a little longer, but at last I folded it into the neatest quarters I could manage and slipped it into my pocket. Perhaps we would get back around to it, in time."
    jump daymenu

label GTS022_cutoff_b_early:
    MC "Uhh..."
    MC "Sorry to do this, but is it cool if we pick this up some other time?"
    show GTS surprised
    GTS "Hm? Are you quite sure?"
    MC "I'm afraid so. Maybe this just isn't my scene but I'm not feeling it today."
    show GTS sad with dissolve
    GTS "Perhaps we could try again some other time, then?"
    MC "Oh, for sure, yeah. We can do that."
    show GTS neutral with dissolve
    MC "And, y'know, thanks for putting this all together. It's a nice idea, and I think I'd like to try again with you sometime."
    GTS "I would as well. I suppose we can talk about it later."
    MC "Yeah, 'course. Have a good day, Yamazaki-san."
    GTS "You as well."
    "We bowed and gathered our things to part ways."
    hide GTS with dissolve
    scene black with fade
    $setAffection("GTS", -2)
    "To my surprise, Naomi said nothing to me whatsoever afterward."
    "I hadn't exactly lied, but I wouldn't have done it if I didn't think she felt the same."
    "I guess not."
    jump daymenu

label GTS022_cutoff_b:
    MC "Uhh..."
    MC "Sorry to do this, but is it cool if we pick this up some other time?"
    show GTS surprised
    GTS "Hm? Are you quite sure?"
    MC "I'm afraid so. Maybe this just isn't my scene but I'm not feeling it today."
    show GTS sad with dissolve
    GTS "Perhaps we could try again some other time, then?"
    MC "Oh, for sure, yeah. We can do that."
    MC "And, y'know, thanks for putting this all together. It's a nice idea, and I think I'd like to try again with you sometime."
    GTS "I would as well. I suppose we can talk about it later."
    MC "Yeah, 'course. Have a good day, Yamazaki-san."
    GTS "You as well."
    "We bowed and gathered our things to part ways."
    hide GTS with dissolve
    scene Hallway with fade
    "We split off each our own way; as for me, I went back inside to let my mind wander to the next diversion."
    "So I thought, until Naomi approached me from behind and gently, distinctly called my name."
    show GTS neutral with dissolve
    GTS "That must have been a difficult position. Please believe me when I say I didn't intend to put you on the spot."
    MC "Maybe. I wouldn't worry about it, though."
    MC "To be honest, I did it as much for you as for me."
    GTS "How do you mean?"
    MC "Well... was I wrong thinking you started to really have to force yourself?"
    MC "And the effort didn't look enjoyable for you at all."
    show GTS sad with dissolve
    GTS "I see."
    GTS "I had hoped it wasn't so obvious. But..."
    MC "It's okay, you know."
    show GTS neutral with dissolve
    GTS "I appreciate the sentiment."
    "She looked down and puffed out a sigh."
    GTS "If only life were gentler about showing us our shortcomings."
    MCT "Don't say it don't say it don't say it"
    MC "Well, clearly you have a number of strengths to balance things out."
    show GTS neutral at Transform(xzoom=-1) with dissolve
    if not getFlag("GTS022_late"):
        $setAffection("GTS", 1)
    GTS "In any case, I appreciate your discretion."
    MC "I try to take my shots when I see 'em, Yamazaki-san."
    "She only chuckled softly."
    MC "Well... until next time?"
    GTS "Until next time."
    hide GTS with dissolve
    "We parted ways one more time that day. And I thought at that moment that a can of tea sounded just lovely."
    jump daymenu

label GTS023:
    $setProgress("GTS", "GTS024")
    $setTime(TimeEnum.EVE)
    scene School Exterior with fade
    play music Busy
    Ryoko "Cut!"
    "The actors broke their self-imposed stasis and looked up and over at Tanaka-san."
    show Ryoko neutral with dissolve
    FemStudent1 "Is that the take?"
    Ryoko "I think not, unfortunately."
    Ryoko "There's something {i}just{/i} off about the {i}mise-en-scène{/i}. Not quite sure what."
    BE "The what on the what?"
    Ryoko "The {i}feeling{/i} of the scene, the mood. It's French. Tell you what, just do it again the same way, I'll sniff out what it is we're missing."
    "The actors nodded with some delay. Honoka sighed, punctuated with a short raspberry. I may have been standing off to Ryoko's side, but I could feel it, too."
    "The cameraman and the actors trudged back down the concrete, and the extras took their places behind them. I myself couldn't imagine what was wrong the last couple times."
    "With more insight than I might've expected, Honoka and her co-star went through a resolute young woman being interrogated by her mother about a boy."
    "It was... both funny and not to see Honoka do the daughter role so well."
    "Pedestrians passed by behind them as they walked into the sunset, and it was all captured by the cameraman carefully performing a dolly shot by hand."
    Ryoko "Cut!"
    if getSkill("Art") > 2:
        MC "Think it's something to do with the delivery of the lines?"
        Ryoko "No, no, the lines are fine."
        MC "Something visual?"
        Ryoko "Maybe?... yes, I think so. Something I'm {i}seeing{/i} here doesn't feel right."
    else:
        MC "...Yeah, sorry, I don't have anything to add here."
        Ryoko "Don't worry about it. I just... hmph..."
    show Ryoko annoyed
    "Tanaka-san rolled her pen between her teeth and scowled."
    "And then she stopped."
    Ryoko "...Oh, brother."
    show Ryoko neutral
    Ryoko "Hotsure-san, I left a black pen with some of the other props back by the parking lot, it's from the bank on Genki street. Would you mind going to get it, please?"
    MC "...What about the one you're holding?"
    Ryoko "Con{w}ti{w}nu{w}i{w}ty.{w} It needs to be the exact same pen she had from the previous scenes. Plus, it has symbolic value for the character's role in the story, y'see? She's taking account of our protagonist's feelings."
    MC "Ah, alright, I get it. Yeah, I'll go grab it."
    Ryoko "Thanks. No need to sprint, but we've only got this lighting for another forty-five minutes, so try not to dawdle."
    "I gave her another affirmative as I walked off toward the parking lot."
    hide Ryoko with dissolve
    stop music
    "Twilight had cast all the world in deep black and fiery orange. It was more of the former the closer I got, where the titanic shadows of the school buildings fell."
    "The quiet conversations on set had faded entirely, leaving a hollow of near-complete silence beneath a sleepy sky."
    "My eyes soon adjusted to the light, and I spotted a tandem bike and other miscellany piled up and leaning on the corner of a wall."
    "I crossed my fingers that I wasn't about to rifle through some {i}other{/i} person's pile of random crap, crossed the barren parking lot, and crouched down to search."
    "Feeling through a few articles of cool, shaded clothes felt nice in the still summer air, but there was no writing utensil to be found. I set them aside and picked up a clear plastic box they'd been draped over."
    "A pack of gum... an empty envelope sealed with a cat sticker... a jar of sand..."
    MCT "I don't even recognize half this stuff..."
    MCT "Ooh, pen!"
    MCT "Ah, wait, it's red."
    "I resealed the box and set it, too, aside. A glance inside the basket on the tandem bike revealed nothing pertinent either."
    "With everything else exhausted, I took out my phone to shine its flashlight on the ground."
    "Insects scattered under the sudden, ghost-white flood, which I waved to and fro with... a little haste."
    "I tried to remember what exactly the pen looked like as more than one twig cloaked in dim shadows fooled me, if only for a split second."
    "But just then, nearly pinned under the bike's front wheel..."
    MCT "'Suave Bank'. Gotcha!"
    "I grabbed my quarry, tucked it in my pocket, and stood."
    show GTS surprised with vpunch
    MC "Bwoah!"
    GTS "Goodness!"
    "From just around the corner, Naomi stood before me clutching a platter while a few cookies bounced and crumbled on the ground."
    menu:
        "Aw sick, you made cookies?" if getSkill("Art") > 6:
            jump GTS023_c1_1
        "Jeez, I didn't see you coming.":
            jump GTS023_c1_2

label GTS023_c1_1:
    $setFlag("GTS023thinkfast")
    GTS "Er, yes, I did."
    MC "Awesome. Uh, sorry I made you drop 'em."
    show GTS embarrassed
    GTS "It's fine. It looks like only a couple fell off."
    MC "Good, good."
    MC "Looks like you made quite a few. Are they for the film crew?"
    show GTS neutral with dissolve
    GTS "Precisely. I didn't quite feel comfortable lending a hand to Tanaka-san's project, but I have been practicing my baking. I thought providing some refreshments would be a neighborly thing to do."
    MC "Well, we're on take fifty bajillion of one scene, so I think you're probably right."
    "Naomi re-folded the cloth covering the remaining cookies, her brows raised."
    GTS "My! I should say so."
    "I knelt down to pick up the fallen cookies."
    show GTS neutral at Transform(xzoom=-1)
    GTS "Oh, you don't have to do that."
    MC "Figure it's my fault they fell. I might as well throw them away."
    GTS "Well, alright..."
    MC "Anyway, I got what I was looking for. Let's go meet the director, shall we?"
    hide GTS with dissolve
    "She readily agreed, but as we parted from the lot I could see her mild smile turning slightly crooked. Something was puzzling her."
    "I only hoped {i}my{/i} answer to things was answer enough."
    jump GTS023_c2

label GTS023_c1_2:
    GTS "I'm very sorry if I scared you, I had no idea you were there."
    MC "No worries, you just caught me by surprise."
    show GTS embarrassed with dissolve
    "I looked up at her pinched smile, glowing in the last of the sunlight, and shrugged."
    MC "Probably the lighting."
    show GTS neutral with dissolve
    GTS "It {i}is{/i} rather dim here in the shade, isn't it?"
    MC "Uh huh. So, what're the cookies for?"
    GTS "Just a little gift for you, Tanaka-san, and everyone working on the set."
    GTS "I didn't quite feel comfortable lending a hand directly, but I have been practicing my baking. I thought providing some refreshments would be a neighborly thing to do."
    "She re-wrapped the remaining cookies on the platter with a large cloth napkin and bent down to pick up the fallen cookies.{w} It occurred to me that was the first time her eye level had been lower than mine in a good while."
    MC "Well, that's thoughtful of you. We're currently on take fifty bajillion of one scene, so I think everyone could use a cookie about now."
    GTS "Really, now? It seems refreshments really are in order."
    MC "For sure. And since I got what I needed here, shall we go meet the director?"
    "She nodded and followed me toward the indigo horizon."
    hide GTS with dissolve
    "Once or twice I caught her expression, when she didn't seem to notice me glancing up at her. She wore a more austere serenity than usual, more blank. Behind that look could only be still waters, or a storm."
    jump GTS023_c2

label GTS023_c2:
    play music Peaceful
    "We arrived on the scene with Tanaka-san visibly brainstorming with herself in her chair, extras standing around chatting, and Honoka, her co-star, and the cameraman doing the same over packs of seaweed, sitting down. After the jumpstart a few moments ago, the stillness eased my heart to a contented rhythm."
    show GTS neutral at Position(xcenter=0.25, yalign=1.0)
    show Ryoko neutral at Position(xcenter=0.75, yalign=1.0)
    with dissolve
    BE "Hey, Yamazaki-san!"
    Ryoko "Oh, Yamazaki-san! You disappeared after class, how's your evening going?"
    GTS "Rather well, thank you. I brought some refreshments for the film crew here, as a matter of fact, hence my sequestering myself in my room."
    Ryoko "Fantastic, they look gorgeous, thanks a million."
    Ryoko "And Hotsure-san, you got the goods?"
    "I handed her the goods in question."
    Ryoko "You're a lifesaver."
    show Ryoko neutral with vpunch
    Ryoko "Places everyone, we're back in business and we're taking it from the top! Except you, Tsukasa-san, c'mere a sec."
    Ryoko "And Yamazaki-san made us cookies for when we're done, so let's all tell her thanks!"
    BE "Niiiiiice! Thanks, Yamazaki-san!"
    "Apart from Honoka's fanfare, there was a general, grateful commotion. Ryoko handed off the proper pen to the mom character's actress, then turned again to us."
    Ryoko "So hey, this should only be a couple more takes on this scene, then we'll try for one more shot and we'll be done for today. Do you wanna stick around, Yamazaki-san?"
    if getFlag("GTS023thinkfast"):
        show GTS happy with dissolve
        GTS "It would be my pleasure. Especially to see if people have anything to say about the cookies."
        MC "There oughta be plenty to say if the last batch is anything to go by."
        "We smiled at each other, though hers was the wider."
        BE "Hold on, hold on!"
        show GTS neutral with dissolve
        show BE happy with dissolve
        BE "I've been working hard, I gotta refuel."
        "Honoka bounced up to the sidetable and snatched up a pair of cookies, which shortly vanished into her mouth."
        show BE neutral
        "Her head tilted, ruminating, drawing on nearly decades of experience."
        BE "Hrm, oz're prey gub."
        GTS "Thank you, I'm glad you like them."
        "Honoka swallowed and realized at the last second to wipe the crumbs off the slope of her chest, setting it faintly aquiver."
        Ryoko "You ready, Inoue-san?"
        BE "Yep! 'Scuse me."
        hide BE with dissolve
        "She jogged back into place in front of the camera, where the quivering would not be faint for another half a minute. She exchanged a brief chat with her co-star, inaudible to me, in the meantime."
        hide GTS with dissolve
        hide Ryoko with dissolve
        "Just as Ryoko said, with the magic of the pen at play it was only a couple more takes before she called the final cut."
        MC "So Yamazaki-san, what do you think of that scene?"
        show GTS neutral with dissolve
        GTS "Me?"
        "She stared ahead in deep thought while Ryoko shouted out first congratulations and then directions for the next shot."
        GTS "Well, those two rather have a knack for acting, don't they? It's quite believable."
        MC "Oh yeah, they're good together. Both very good at expressing strong emotions in a way that isn't too overwrought."
        MC "'Course, Inoue-san's always been a pretty good actor. She certainly has a lot of amateur experience."
        GTS "She {i}is{/i} quite the card."
        GTS "I do admit, it's hard for me to relate to the protagonist speaking that way to her mother. It's very impassioned, almost defiant."
        MC "It {i}would{/i} be a weird position to be in in real life, eh?"
        MC "But that's love for ya, or so it goes. Everything says it makes you do things you'd never do otherwise."
        GTS "We also love our mothers and fathers, do we not?"
        GTS "Not that my opinion should be taken as an invalidation of your work. Clearly there's a tremendous amount of artistry here, I look forward to seeing it when it's finished."
        "I nodded."
        MC "Me, too."
        "Soon after, Ryoko shouted everything into place and shooting resumed one more time for the evening."
        "I didn't quite catch the beats that time; I was weighing in my head whether I should take a cookie or not."
        "It was sorta my fault a few of them were wasted, after all."
        show GTS neutral at Position(xcenter=0.25, yalign=1.0)
        show Ryoko neutral at Position(xcenter=0.75, yalign=1.0) with vpunch
        Ryoko "Cut!"
        Ryoko "And that's a wrap, great job everybody!"
        MC "Anything you want me to do?"
        Ryoko "I... think you're good? Yeah, if you wanna have a cookie and call it a day, go ahead. Thanks for helping out today."
        MC "Sure, you're welcome."
        hide Ryoko with dissolve
        show GTS neutral at center with dissolve
        "I paused a moment and unfolded the cloth, and took my piece of the treasure hoard beneath."
        MCT "Shortbread. Crumbly but soft, and still quite warm. Hm!"
        MC "Even better yet, Yamazaki-san."
        show GTS happy with dissolve
        $setAffection("GTS", 1)
        GTS "Thank you."
        jump daymenu
    else:
        GTS "It would be my pleasure, but making these meant sacrificing some time for study. I should probably return to my room and start making up for it."
        Ryoko "Uh huh, gotcha. Well, thanks again, Yamazaki-san. See you around."
        show GTS happy with dissolve
        GTS "A pleasant evening to all of you."
        MC "You too, Yamazaki-san."
        hide GTS with dissolve
        show Ryoko neutral at center with dissolve
        Ryoko "Alright, this time extras are gonna be off-screen! Tsukasa-san, Inoue-san, I want you guys right under that light pole. We're picking up right where we left off on the script!"
        MC "Hey, Tanaka-san, is there anything else you need help with?"
        Ryoko "Nothing I can think of right now. Why?"
        MC "Ah, I think I'm gonna head out, too."
        "She chewed on that for a second."
        Ryoko "Go ahead, I guess. Thanks for the help today, Hotsure-san."
        MC "You're welcome. Seeya later."
        Ryoko "Mhm."
        hide Ryoko with dissolve
        "Naomi was still in sight as I walked off the set, pacing like a prowling cat into the sunset despite her elongated gait. I hurried up behind her with as much ease as I could muster."
        MC "Hey, Yamazaki-san, don't you wanna stick around?"
        show GTS neutral with dissolve
        GTS "I do. Or I would."
        show GTS sad with dissolve
        GTS "However, I do worry about lingering where I'm not welcome."
        MC "Not welcome? You baked everybody cookies, for God's sake."
        MC "Tanaka-san even gave you an open invitation to drop by whenever you want."
        GTS "I know. Even still, I can't help but think my height is beginning to make people uncomfortable."
        GTS "...It's an unfortunate consequence of how I try to approach people gently; sometimes I inadvertently sneak up on people. But I've never {i}frightened{/i} anyone."
        MC "Okay, yeah, I spazzed out a little. But like you said, it was super shady over there. It's not, like, a regular thing."
        GTS "It's not just that. I keep thinking back to that day when I was sitting in class all day with a nearly-ruined uniform. It was so embarrassing..."
        GTS "And I feel so rude whenever I accidentally see over someone's shoulder, or someone can't see what's on the menu in the cafeteria because of me."
        menu:
            "You underestimate what people are willing to forgive. Think of it as a quid pro quo situation.":
                jump GTS023_c2_1
            "Who cares what they think?":
                jump GTS023_c2_2

label GTS023_c2_1:
    show GTS neutral with dissolve
    GTS "I'm not sure what you're getting at."
    MC "Nobody else in our class except maybe Kodama-san is as patient, or as selfless, or just... generally chill to be around as you."
    show GTS embarrassed with dissolve
    GTS "That's... very flattering."
    MC "Really, who else?"
    show GTS neutral with dissolve
    GTS "That's a rather impious question to ask oneself, is it not?"
    MC "Well..."
    MC "The way I see it, until someone actually goes out of their way to avoid you, it'd be healthier for you to go about as if there were nothing wrong."
    GTS "I see."
    GTS "You do raise a good point. I'll try to adopt that mindset."
    MC "Thank you, Yamazaki-san. I do hope you feel better."
    GTS "No, Hotsure-san. Thank you."
    jump daymenu

label GTS023_c2_2:
    $setAffection("GTS", -1)
    GTS "I care."
    MC "I..."
    show GTS neutral with dissolve
    MC "Right. That was insensitive of me, sorry."
    GTS "I don't hold it against you. You were only trying to help."
    "I nodded, but wanted to let nothing more past my lips for a moment."
    "Instead, we walked a little farther together in silence. Her hair was aflame in the dusk sunlight, as mine likely was as well."
    MC "So, I guess this is good night?"
    GTS "That sounds agreeable to me."
    show GTS surprised with dissolve
    pause 0.75
    show GTS embarrassed with dissolve
    GTS "Oh, dear, I didn't mean it like that..."
    MC "Heh, nah, I get you. Take care, Yamazaki-san."
    show GTS neutral with dissolve
    GTS "And you also."
    hide GTS with dissolve
    "With that, we parted ways, the distance growing between us in the shade."
    "And I stuck my hands in my pockets, felt a pen or two inside them, and sighed."
    jump daymenu

label GTS024:
    $setProgress("GTS", "GTS025")
    scene Roof with fade
    play music GTS
    "Mottled mists flowed in the heavenly river above, beckoning the eye to see."
    "Their scattered sunlight cast the shimmer and shadow of a diamond's faces on treetop and riverbank and mountainside."
    "And their cold breath blew back my shoulder-length hair in whipping branches, letting an unseasonal chill blanket my cheeks and writhe on my scalp."
    "Then, the wind turned, and draped a tress suddenly across my eye. I peeled it away and let out a quiet little laugh."
    "I never used to do this."
    show GTS neutral with dissolve
    "I stepped away from the fence to see Naomi kneeling by her verbena planters, her skirt a gentle blue cascade over her knees and the watering can tipped nearly sideways, dribbling over the soil by her gentle hand."
    MC "Think it'll rain?"
    GTS "Hmm...{w} It might. I believe it will be gentle if it does."
    MC "Next time maybe you could let me do that."
    GTS "Perhaps, if you so wished."
    MC "Yeah. I mean, I probably can't do it like you, but... I've had some time to observe your technique."
    GTS "How nice. But I don't know that I have anything you don't."
    MC "...Let's agree to disagree."
    show GTS embarrassed with dissolve
    MC "This floor can't be good for your knees, in any case."
    MCT "The bending probably isn't good for your back, either."
    show GTS neutral
    GTS "Hm, well... you might be right. It's starting to chafe a little."
    "Kneeling on one knee and then the other, she brushed the dust off her shins and stood. I walked over to get a look at her handiwork, rolling in blue waves."
    "It was a marvel to see what seemingly just a little diligence had reaped, and I then looked down to see the fresh, welling water quickly seeping down into the darkening earth. All to be drank up by Naomi's rainbow flowerbed."
    stop music
    "Though as I took the sight in, I noticed a flower or two near the middle with petals splotchy brown and curling. I pointed at them."
    MC "Hey, what's that? Blight?"
    show GTS surprised at Transform(xzoom=-1)
    "Her gaze shot to where I was pointing and her mouth fell open in genuine surprise."
    GTS "Oh, my. Let me see..."
    "She knelt down again, daintily pulling her skirt just out of the way of her shins, and squinted."
    show GTS neutral
    GTS "No lesions, and it doesn't seem overexposed... it doesn't look like blight, but malnutrition."
    show GTS sad with dissolve
    "She stood back up with a creased brow and a hint of a frown."
    GTS "I don't quite know how that escaped me."
    play music Rain
    MC "Well, hey, it's fixable, right?"
    show GTS neutral at Transform(xzoom=1) with dissolve
    "She gave me a brisk nod."
    GTS "Very much so. I suppose I just happened to miss that spot when I was pouring out the plant food. We need only set it gently back on the path to health."
    MC "Okay, cool. "
    if getSkill("Academics") > 4:
        MC "So, do you have some plant food and, I guess, an eyedropper handy?"
        GTS "But of course."
    else:
        MC "So, uh, what do we... do, exactly?"
        GTS "A light dosage of plant food for this week should do the trick, and I'll have to make absolutely sure they get an even portion from now on."
    GTS "In fact, would you perhaps like to come with me to get what we need?"
    MC "Of course."
    show GTS happy
    GTS "Splendid! Well, first, let's go downstairs."
    "She glanced up at the sky and her glossy black hair fell a little further down her back, wavering in the gray like silken strands."
    show GTS neutral
    GTS "It may be wise to make haste."
    MC "Probably."
    "Though Naomi was still moving at a fairly easy pace, she reached the door first and held it open for me to go through. Just before I went through, I turned around and called out,"
    MC "Bye, plants! We'll be back in a jiffy, so no wild parties."
    scene Hallway with fade
    show GTS happy with dissolve
    GTS "Hm hm hm. I believe the idea is to talk to the plants up close."
    show GTS neutral with dissolve
    MC "I'm sure they got the picture."
    GTS "The ease of your levity never ceases to amaze me."
    "We proceeded down the ramps towards the ground floor, passing small, dispersed groups of students hanging around and chatting in the dim gray light."
    "Naomi began walking with a little more oomph once we neared the entrance, and I found myself having to full-on fast walk to keep up."
    scene Gate Front with fade
    show GTS neutral with dissolve
    MC "Where are we going, exactly?"
    GTS "Well, the groundskeeper graciously allowed me to keep a jug of my plant food by the supply shed. And I believe I have a suitable eyedropper in my dormitory."
    GTS "I hope you don't mind a bit of a trip."
    MC "Just those places and back? Nah, not at all."
    "She gave me a shallow but considered bow."
    GTS "Thank you."
    hide GTS with dissolve
    scene Campus Center with fade
    show GTS neutral with dissolve
    if getSkill("Athletics") > 2:
        "I honestly had no trouble keeping up with her after the initial surprise, but nonetheless we remained silent for a good minute or two crossing behind the admin building. Something was occuring to me that held my tongue."
        "However, Naomi stole a glance at me and must have noticed my drastically quickened pace. She covered her mouth and came gently to a stop."
    else:
        "Almost immediately on contact with fresh air and even filtered sunlight, I started to wither."
        "We weren't halfway to the admin building when I started to flag behind, and the gap between me and Naomi grew by the second. She shortly noticed and came to a gentle stop so I could catch up."
    show GTS sad at Transform(xzoom=-1) with dissolve
    GTS "Oh dear, I'm sorry. That was horribly inconsiderate."
    MC "No worries, gotta work out all that sitting down in class one way or another."
    show GTS neutral with dissolve
    GTS "Regardless, I shouldn't think we strictly {i}need{/i} to rush."
    show GTS neutral at Transform(xzoom=1) with dissolve
    "We kept going, this time at a more accommodating pace. I had time to observe the patches of light and shadow flowing across every surface, and hear the birds chirping from the obscurity of the hedges."
    "The tidy little... well, relatively little... supply shack sat just on the edge of the surrounding forest, behind the towering admin building."
    "Just as Naomi said, right in its faint shadow, sitting in a tuft of just slightly longer grass, there was a jug of slightly foggy, colorless liquid."
    "We came closer and I noticed a couple long strips of painting tape on the side; a message was written on them in marker, the characters large but tipped with fine, perfectly angled curves and tapers."
    "'Plant Food'"
    "'Please do not drink'"
    "Naomi knelt down on the shaded grass and looped three fingers through the jug's handle, the fourth having no room, and then stood; the liquid didn't slosh a bit as she cupped her other hand under the jug."
    MC "Alright, there's step one."
    GTS "Indeed. Now, we just have to get my eyedropper."
    MC "Right, right. Ladies first, of course."
    show GTS happy
    GTS "Such a gentleman!"
    "I only just heard her chuckle under her breath, and we began treading directly across the grass to the girls' dorms."
    hide GTS with dissolve
    scene Dorm Exterior with fade
    show GTS neutral with dissolve
    GTS "Well now, I understand this is a bit unusual, but would you mind waiting out here for a minute or two?"
    "I thrummed my fingers on my pockets while contemplating the question for a second."
    MC "I can do that, sure."
    show GTS neutral
    GTS "Thank you, sincerely. I'll be as quick as I can."
    hide GTS with dissolve
    "I waved her off with a thin smile, and she turned and made her own smooth hustle through the front door."
    "More quiet. Chirping distant and close. Gray concrete beneath a gray sky. Momentary exchanges muffled by windows."
    MCT "Ah, crap, the windows."
    "In a desperate bid not to look like a massive creep, I set my backpack down and leaned against the wall. Momentarily I thought to take out my phone to flip through for good measure."
    "A minute or two went by. So did a number of hopefully inconsequential emails."
    MCT "Did she lose the thing, maybe?"
    MCT "Maybe she ran into Tanaka-san or...{w} um...{w} her roommate, what was her name?..."
    "*plip*"
    "Quiet as everything was, I only just heard something small and wet hit the ground a few inches to my left."
    "To my relief, it {i}wasn't{/i} rain, but I couldn't explain how a tiny, dampened, off-white wad of notebook paper had appeared at my side. There was no one nearby and the wind wasn't strong enough to blow it around."
    "*plip*"
    "The mystery was solved shortly after a second wad landed in my hair."
    BE "Jordan!"
    "I looked up to see Honoka in a sniper's perch by her windowsill, with her indomitable pair of sandbags providing her cover."
    MC "Honoka! Matsumoto-san's gonna rip you a new one if she sees these lying around!"
    BE "Let them come. I have enough wads to hold this dorm against a thousand men."
    "I one hundred percent believed her."
    "To demonstrate her point, she produced a third spitball, licked it, loaded it into her straw, and fired it at me with a steely gaze and a puff of her cheeks. It missed, splatting against the wall and tumbling down."
    BE "Dangit.{w} Anyway, whatcha doing Kei-chan?"
    MC "Helping Yamazaki-san with her garden. She's getting something from her room, I'm just waiting out here."
    BE "Ooh, mysterious!"
    MC "Heh, far as I know she's just going in to get an eyedropper. Drip some plant food on one specific patch, y'know?"
    BE "Sure, Kei-chan. She's making you wait outside when it's about to rain because she doesn't want you to know where to find her top secret eyedropper stash."
    BE "Nothin' going on there, huh?"
    "I couldn't come up with anything to say for a second; I shook my head and looked up at her."
    MC "First of all, it's not about to-"
    "*plip*"
    "That one, alas, was not Honoka, as the sudden coin-sized dark spot on my shirt testified. She did, however, look down at me with one finger over her broad grin."
    BE "Better take cover under the awning, Kei-chan. You're so sweet doing all this for your girlfriend, you must be made of sugar. You'll melt~"
    MC "Thanks for the tip."
    "She gave me a sharp salute, a dainty little wave, and slid her window closed. I took her advice and moved."
    "I played over what Honoka said once or twice in my head.{w} Then, as raindrops began to dot the now stony-smelling ground, it occurred to me to take my umbrella out and have it ready."
    pause 1
    MCT "..."
    MCT "I forgot the damn thing in my room."
    "Just in time to see Naomi approaching the front door."
    show GTS neutral with dissolve
    GTS "Thank you for waiting."
    "I shrugged."
    MC "What am I gonna do, run off and join the circus?"
    show GTS happy
    GTS "I suppose not. That would hardly be suitable for one such as yourself."
    show GTS neutral
    GTS "Moreover, it seems we were due for rain after all."
    "At that point I noticed the oversized clear umbrella folded in her hand. And by the rising of her eyebrows, I take it she noticed I had no such thing."
    show GTS surprised with dissolve
    GTS "Hotsure-san, do you have your umbrella?"
    MC "'Fraid not. I just realized I left it back in my dorm."
    MC "Don't worry, though, I got a notebook I can use to cover my head for the short distance to the boys' dorms."
    GTS "That seems rather wasteful."
    MC "Um... well, yeah, probably. Maybe you could lend me your umbrella and I could run over there real quick?"
    if getAffection("GTS") < 30:
        show GTS neutral with dissolve
        GTS "Yes, that sounds like a fine plan."
        "She handed me her umbrella, which I took with a bow."
        MC "Be back in no time."
        GTS "No need to trouble yourself by hurrying. A few moments of reflection wouldn't be the worst thing in the world."
        MC "Oh, certainly not."
        hide GTS with dissolve
        "Thusly, I raised the umbrella and briskly set out on newly pitter-pattering, damp ground down to my dorm."
        scene black with fade
        pause 2
        scene Dorm Exterior with fade
        "I fear I ended up forcing Naomi to wait some time as well. I searched every nook and cranny of my dorm that I could conceive in the quest for my umbrella...{w} ultimately to find it in my raincoat pocket."
        "This done, I hastened to beneath the awning where Naomi was standing, hands folded in front of her thighs and eyes cast aloft to the sky."
        show GTS neutral with dissolve
        GTS "You found it?"
        MC "Eventually. Apologies about the delay."
        GTS "Think nothing of it. If absolutely nothing else, turnabout is fair play."
        "I took cover from the rain and did my best to shake off some stray droplets from Naomi's umbrella. Once satisfied, I gave it back to her."
        GTS "Thank you. Now, let's head back to the classroom building."
        MC "Let's."
        hide GTS with dissolve
    else:
        GTS "Well, I have another, faster idea..."
        "She craned her neck to look over at the boys' dormitories; I did too, and saw that there didn't seem to be anyone around there, either."
        show GTS embarrassed with dissolve
        GTS "It might be considered a bit uncouth..."
        MC "You? Having uncouth thoughts? Please, do tell."
        GTS "Well, what if we were to walk over there together?{w} At the same time...{w} under my umbrella?"
        "Some air caught in my chest for a second and I prayed the clouds obscured the blush I could feel coming on."
        if getSkill("Academics") > 1:
            MC "On the contrary, that sounds like a perfectly lovely idea."
            GTS "If you really think so... then by all means, let's try it."
            show GTS neutral with dissolve
        else:
            MC "That idea sounds perfectly couth to me."
            show GTS neutral with dissolve
            pause 1
            GTS "Very well, let's try it."
        MC "So, how will this work, exactly?"
        GTS "I'll hold my umbrella over us, and you can walk directly in front of me. I'll do my best to match your pace."
        MC "Okay, that should work for me, um... that should work."
        "She was blushing a little, too, through a teacher's gently unrevealing expression."
        show cg GTS024 with dissolve
        pause 2
        "Naomi unfurled her umbrella to its span of a little over two meters, and stepped out from under the awning with a space in front of her."
        "It looked like just slightly more than enough room for me. I stepped inside it, and without a word, took a few slow steps forward."
        "She indeed matched my pace rather well, though the space under the umbrella necessitated that we stay quite close together."
        "I could just see a hint of her arm in my peripheral vision, and the swish of her skirt as she walked caused it to occasionally brush against my lower back."
        "She didn't say a word, though.{w} I couldn't say why it occurred to me, but I couldn't hear her breathe, either. The only thing between us was the soft pitter-patter of rain just a little ways over my head."
        "We shortly reached my dorm. She walked up to the point where I could get into the lobby without getting wet, and stopped."
        hide cg with dissolve
        MC "Ah... thank you, that worked out pretty well."
        MC "...I'll be back in just a minute, okay?"
        "She nodded."
        GTS "I'll be right here."
        hide GTS with dissolve
        scene black with fade
        pause 2
        scene Dorm Interior with fade
        "As it happened, I would not be back in just a minute."
        MCT "C'mon, show yourself you stupid piece of junk..."
        "I had overturned just about every conceivable umbrella-sized object in my section of the room and was halfway considering checking the bathroom or cutting open my mattress."
        "And as I looked at that mattress, I noticed my wrinkled raincoat half-buried under the sheets."
        "I pulled it out and chanced to feel around inside the pockets."
        MCT "...Yep."
        "I thanked the stars at least Daichi wasn't there to see that in person as I left again and headed back down to the entrance."
        scene Dorm Exterior with fade
        show GTS neutral with dissolve
        GTS "You found it?"
        MC "Eventually. Apologies about the delay."
        GTS "Think nothing of it. If absolutely nothing else, turnabout is fair play."
        MC "Very well, then. I do believe we have a garden to attend to."
        show GTS happy with dissolve
        GTS "Precisely."
        hide GTS with dissolve
    scene Campus Center with fade
    "As we crossed the campus back to the building where the garden awaited, the rain began to come down more regularly but not much harder. It was a quintessential lukewarm spring drizzle."
    scene Hallway with fade
    "We got back inside to more or less the same scene of fellow students hanging out in small groups, though one or two such had apparently left."
    "With the rain also faded into the background, something Honoka said, and a few things Naomi said, too, came back to me. We reached the top floor, and with no one in earshot, I spoke up."
    MC "Naomi..."
    show GTS neutral with dissolve
    GTS "Oh? Yes?"
    MC "Why exactly did you want me to come with you to get the stuff?"
    GTS "Well, would I be mistaken in supposing that you're at least a little invested in the garden?"
    MC "You wouldn't be mistaken at all."
    show GTS happy
    GTS "Well then, I can tell you that I simply thought it would come in handy for you to know some of the basics."
    GTS "See? Now you really have everything I have."
    MCT "That was... spontaneous."
    menu:
        "C'mon, something's up, just tell me. You can trust me, can't you?":
            jump GTS024_c1_1
        "That's very kind, Yamazaki-san.":
            jump GTS024_c1_2

label GTS024_c1_1:
    show GTS neutral
    GTS "Of course, Hotsure-san, I trust you dearly. If something were wrong you would be among the first people I'd tell."
    MC "So, everything's okay?"
    GTS "Everything's okay."
    GTS "Although I must ask, is there anything you'd like to talk about? You're usually quite relaxed."
    MC "Uh... no, not really. Nothing I can think of."
    GTS "As you wish. But please, know that you can tell me anything you like."
    MC "Okay, I'll keep that in mind."
    show GTS happy with dissolve
    GTS "Wonderful."
    show GTS embarrassed with dissolve
    GTS "I do mean it. Our friendship is precious to me."
    "All the remaining chill from the winds outside evaporated in an instant."
    MC "I feel exactly the same."
    show GTS neutral with dissolve
    GTS "Come to think of it, why don't we go down to the cafeteria after I finish feeding the flowers? A nice apple sounds quite lovely right about now."
    MC "Oh, definitely! That and a bag of shrimp puffs, too."
    show GTS happy with dissolve
    GTS "That, too."
    "At last, we proceeded up to the stairs up to the roof. I stole one last glance out at the misty grounds, with the sky whispering sustenance down upon it. The sight was, in a word, lovely."
    jump daymenu

label GTS024_c1_2:
    show GTS neutral with dissolve
    GTS "Of course, Hotsure-san. I daresay you're my best and closest friend."
    MC "I feel exactly the same for you. As long as I've known you you've been endlessly warm and gracious. I feel I could trust you with anything."
    show GTS happy
    GTS "I greatly appreciate the confidence."
    MC "Something so precious ought to be cherished and protected."
    show GTS neutral with dissolve
    GTS "Ah, yes, I agree. It's all too easily lost."
    GTS "But it's also important to let things be what they are. After all, decay is just as natural and healthy as growth."
    "I paused for a second."
    MC "Some might say otherwise. It's why we sharpen pencils, water our plants, help our friends who are falling behind."
    show GTS angry
    GTS "Some might say that's a bit presumptive."
    stop music
    pause 1
    show GTS sad with dissolve
    GTS "I'm..."
    GTS "Apologies, that was uncalled for."
    "I walked up to her, took her jug of plant food, and set it gently down on the ground. Slow and easy, like I saw her do."
    "Then, I took her hand in mine."
    MC "Please, Yamazaki-san, allow me to try and do the same for you."
    "She looked down into my eyes. Her lips were pursed inward, and she started to blink more, slower, more drawn out. Her whole heart-shaped face seemed to flutter."
    MC "Please."
    show GTS neutral with dissolve
    pause 0.5
    show GTS sad at Transform(xzoom=-1) with dissolve
    pause 0.5
    show GTS neutral at Transform(xzoom=1) with dissolve
    pause 0.5
    show GTS sad with dissolve
    "She breathed in, still as a cage, and sighed through her nose."
    "I held onto her hand as she fully regained her composure. After a moment of stillness, she gently slipped our hands apart."
    GTS "I received some... news, the other day."
    MC "What was the nature of it?"
    GTS "Apparently, there are limits to what the main facility here can accommodate. Students whose height increases beyond a certain threshold must be moved to separate facilities on campus."
    MC "How sure are you that that'll apply to you?"
    GTS "I simply don't know."
    GTS "I've been growing fairly slowly, but now that it's started it hasn't stopped at all."
    GTS "I already struggled just to pick up my eyedropper, I don't want to lose touch with you, I don't want the flowers to die, I don't want what friendships I have here to die..."
    MC "Do you need to breathe again?"
    "She considered it, calmly, and nodded."
    play music GTS
    MC "So, they said they have to move. They didn't say they're forbidden from going anywhere else."
    show GTS neutral with dissolve
    GTS "Yes... that's true."
    GTS "What about the garden?"
    MC "That's what this was all for, wasn't it?"
    MC "And if there's something I don't know... and there probably will be..."
    GTS "Hm hm. Perhaps."
    MC "Well, I'll just ask you. I know I want to stay in touch with you no matter where you go."
    $setAffection("GTS", 2)
    GTS "Likewise, Hotsure-san."
    GTS "Something gives me a feeling... we can lean on each other. Like you said."
    "I closed my eyes and nodded, then opened them to look deep in her amber eyes."
    GTS "Let us cultivate each other, as well."
    MC "I think we've got something else to cultivate right now."
    show GTS surprised
    GTS "Oh!"
    show GTS happy with dissolve
    extend " Yes, you're absolutely right. Let's tend to that right away."
    hide GTS with dissolve
    scene black with fade
    "She picked up her jug and we made our way up the stairs, umbrellas ready. I managed to reach the door first, and soaking up a few seconds of unabated rain before holding the door for Naomi to huddle through."
    "I resolved, to myself, to appreciate the open air more."
    jump daymenu

label GTS025:
    $setProgress("GTS", "GTS026")
    $setTime(TimeEnum.EVE)
    scene Campus Center with fade
    "I tapped my foot on the grass as I checked my watch once more. It was already half past five, and yet Ryoko still hadn't shown up."
    show GTS neutral at center with dissolve
    play music GTS
    "Naomi seemed more patient than me as she sat under the tree, drinking tea from her cup."
    MC "I wonder what's keeping Tanaka-san. She was supposed to be here thirty minutes ago."
    GTS "It could possibly be some sudden school work she realized she needed to do. I'm sure she'll be here soon, though. By the way, would you like some tea, Hotsure-san? I brought some extra cups in case you and Tanaka-san wanted some."
    MC "Sure, I'll have some. Thank you, Yamazaki-san."
    "As I sat down and took the cup, a small jingle came from my pocket. Retrieving my phone, I read the newest text message I had received while sipping tea."
    "It appeared Ryoko had indeed become bogged down with some last-minute assignments she had been putting off."
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
    scene black with fade
    "From there, we took a miniature tour of the campus. We stayed outside for as long as we could, partially to take in the scenery and partially to allow Naomi total comfort, as once we entered the school that'd change."
    "Upon entering the school, Naomi immediately began to adjust herself to avoid possibly bumping into obstacles that I wouldn't have even considered. From there it was short trips to the cafeteria, library, and music club."
    scene Roof with fade
    "The voyage came to its conclusion on the school roof. Bathed in the light of a setting sun, I breathed in deeply, taking in the aroma of the flowers Naomi had planted earlier."
    MC "This is nice, I don't really take many chances to go out late in the afternoon."
    GTS "I would recommend it. The way the breeze journeys along, the colors the sun paints across the land, and the calm the setting provides... It's truly a lovely hour."
    MC "Poetic."
    show GTS embarrassed
    GTS "I, my apologies, Hotsure-san."
    MC "Don't worry, I like it. And I would say I agree with you, it's nice just being out here and seeing the world through this filter."
    "I moved closer to the fence and sat down, giving myself the best view that I could before Naomi sat next to me."
    show cg GTS025 with dissolve
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
    menu:
        "Yes":
            jump GTS025_c1_1
        "No":
            jump GTS025_c1_2

label GTS025_c1_1:
    $setFlag("GTS025_kiss")
    MC "Uh... y-yes, it um... would be okay..."
    "I felt like an idiot for being unable to just say what I wanted to say. I saw her close her eyes as she leaned into me. My eyes noticing her hands clenching and slightly shaking, and she flinched once I actually moved."
    "There was a moment of pause however, as Naomi's nose bumped my forehead, causing me to smirk as in our anxiety we failed to make the necessary height adjustment."
    GTS "S-sorry..."
    MC "It's okay."
    "Reaching up, I placed my hand on her cheek as I guided her until our lips met. She was soft and warm, tender and timid as she tried not to press against me, but also feared pulling away."
    "I felt her tense up, then relax, only to tense once more as she seemed scared to ruin the kiss. My thumb gently caressed her cheek, and soon her tension eased away. We allowed ourselves to enjoy this, rather than let fear mess it up."
    "We stayed like this for merely a few seconds before I finally moved back. Her eyes opened, and while she was still deeply red, I saw the warmest smile form as her eyes looked directly into my own."
    hide cg with dissolve
    show GTS happy
    "Her joy coaxed out my own as I smiled in response to hers. We didn't talk again, instead we looked back out into the sunset as she leaned back into me once more. This time however, I felt her gentle hand rest upon mine."
    "Softly, I shifted my hand and took what of hers I could within its grasp. Squeezing her hand tenderly, we enjoyed the view until the sun vanished behind the horizon."
    jump daymenu

label GTS025_c1_2:
    MC "Are you... certain that we're ready for that?"
    "Naomi returned a deeply embarrassed, apologetic look. She recoiled backwards, holding her hands upon her shoulders as she crouched. The peaceful air of the moment was silenced by her look of regret."
    GTS "I deeply apologize, Hotsure-san. It was improper of me to ask so suddenly."
    MC "No, no. It's not an issue at all. I'd just like to take it slower. You've done nothing wrong."
    GTS "Are you certain?"
    MC "I'm certain. There's no need to apologize."
    GTS "I still feel foolish for having asked."
    jump daymenu

label GTS026:
    $setProgress("GTS", "GTS027")
    "I awoke in the same bed in the same room, where I could look out the window and see the same otherworldly campus under the same vermillion sky."
    "Time stopped yesterday on the roof."
    scene Dorm Interior with fade
    "And all the tiny vibrations of the outside world flooded into me. My heart wrung itself in the emptiness, sending sweet vines up into my throat."
    "Lying down, eyes glued to the ceiling, I couldn't stop smiling."
    "As the air moved in blind circles in my chest, I thought about how everything could go so right. Could it have been a dream? I didn't remember a single other thing that happened yesterday."
    "I soon realized I was moving in circles, too, and so I flung off my blanket and stood to get ready for day two."
    show RM neutral with vpunch
    MC "PFWUGAH"
    play music RM
    MC "Jeez, can I put my clothes on first?"
    "Daichi had gone back to shotgunning a can of coffee while I processed the shock from the impromptu wakeup call."
    "Apparently finished, he set the can back onto his lap."
    show RM concerned
    RM "I just need to know why you were sitting in bed wide awake at four-thirty this morning."
    "For a second, I had no answer but to stare back at him agape."
    MC "Why is that any business of yours?"
    "He shrugged."
    RM "Seemed like something was bothering you. I know I'm not the most charming guy, but if we're gonna be living together for a year..."
    MC "I do not have the time nor the pants for a therapy session right now, Utagashi-san."
    show RM neutral
    RM "Just tell me what's up, maybe I can help."
    MC "...Alright, if it'll end this conversation, it's not something I need help for. All it was was..."
    MC "...I had kind of a moment with Yamazaki-san yesterday."
    "His eyebrows rose a little bit and he said nothing for a moment."
    RM "Okay, well good luck with that."
    MC "Thanks, doc."
    "He shrugged."
    RM "I said 'maybe'."
    show RM happy
    RM "And hey, she seems like a good person to be friends with. Good for you."
    "I mulled over his phrasing as I reached for my pants. The stiffness of the day's first waking moments fought me a little on the way."
    MC "Yeah, thanks."
    hide RM with dissolve
    "At that, he took his backpack and slinked out of the room, holding the door tight against him all the way."
    "And I just took a deep breath, stretched and stood. I spared a glance at the clock: forty-five minutes to class."

    scene black with fade
    pause 1
    scene Hallway with fade
    play music HigherEdu
    "Things didn't feel much more real as I collected myself and headed to class."
    "There was a breeze out; silhouettes of leaves milled to and fro on the windows, on the walls beyond, while our scattered procession crawled towards room 3B."
    "Motion was coming creaking back to the world around me."
    "That was when my eye catapulted past the mottled shades of gray and beige high above toward a jewel of jet gleaming with streaks of white; in a second she vanished past the door."
    MCT "Yamazaki?"
    MCT "Not often she's not first in..."
    "Moments later, I squeezed my way into class, too."

    scene black with fade
    pause 1
    scene Classroom with fade
    show HR neutral with dissolve
    HR "...And if there are no other questions, remember there's a quiz on chapter 4 tomorrow."
    HR "And for whoever needs to hear this, any copy that comes back to me with glitter on it is getting a zero. Hope that's clear enough."
    HR "Alright, dismissed."
    "I slapped together my things and dumped them into my backpack as gracefully as I could manage, before standing to try and follow Naomi out the door."
    "As I did so, passing the head of the room, I caught Tashi-sensei glancing at me; I stopped."
    MC "..."
    HR "Got a question, Hotsure?"
    MC "No, sensei."
    HR "Fantastic. See you tomorrow."
    "His expression didn't change at all for the entire exchange. I bowed, and he nodded and returned to his paperwork."

    scene Hallway with fade
    "Luckily, I had a strong hunch where Naomi was going."
    "I picked up the pace in her footsteps; just as we came within sight of the exit out to the roof, she turned her head slowly and I caught a glimmer of amber."
    show GTS neutral with dissolve
    GTS "Good afternoon, Hotsure-san."
    MC "Same to you, Yamazaki-san. How're you doing?"
    GTS "I am well, and I'm glad you have decided to join me."
    MC "'Of course! Shall we?"

    scene Roof with fade
    "A handful of students were treating themselves to snacks and conversation under the noon sun there already; Naomi was almost ethereal among them, stepping in a silent, measured pace, hands folded, face like a pearl."
    "I followed her to her mist-blanketed tulip planters, matching her meditative pace. She turned around, and revealed the swift return of her characteristic sober countenance."
    show GTS neutral with dissolve
    GTS "How quickly things change."
    MC "Yeah..."
    MC "How are the verbenas looking?"
    GTS "Just fine. The one that was withering has just about fully recovered."
    if getFlag("GTS025_kiss"):
        "To my surprise, she wasn't looking at me nor at the garden as she said it; I traced her gaze as subtly as I could and peered upon a bench by the planters. Our bench."
        "But then she turned back to me, and after a flash of surprise put on a gentle smile."
    MC "Well, that's not so bad, right?"
    show GTS neutral at Transform(xzoom=-1)
    "She shook her head, and then took up her watering can and began to pour. The flowers sounded off with a grateful pitter-patter, and their faces gleamed with the droplets."
    MC "Yamazaki-san..."
    MC "If you don't mind, I think we have something to talk about."
    GTS "Perhaps we do."
    "She finished watering her flowers... and looked them over for a moment or two, before turning to me."
    GTS "Patience, however. What do you say we talk about it on the way to lunch?"
    MC "Yeah! Yeah, sure."
    "She smiled at me, bowing her head, and set aside her watering can while I went to open the door."

    scene Hallway with fade
    show GTS neutral with dissolve
    "Naomi didn't seem to mind at all as I considered what to say."
    "It occurred to me, stealing a glance at the mild portrait of her face, if I should've said anything at all. In time, however, I realized I didn't have a choice."
    menu:
        "I think we should talk about yesterday.":
            jump GTS026_c1_1
        "Seeing the verbenas getting better must be a relief, huh?":
            jump GTS026_c1_2

label GTS026_c1_1:
    show GTS neutral at Transform(xzoom=1)
    GTS "I see..."
    GTS "What do you wish to talk about?"
    MC "I've been thinking..."
    if getFlag("GTS025_kiss"):
        "And it was time to act."
        MC "Would you be available to have dinner this evening?"
        show GTS surprised
        GTS "Well!..."
        show GTS happy
        GTS "Yes, I think that should be perfectly fine."
        MC "The sushi joint on Genki street, like five o' clock?"
        GTS "A lovely idea. Shall I meet you at the bus stop?"
        MC "If you would."
        show GTS neutral
        "Her smile drifted down over me as she nodded."
        MCT "It's a..."
        "I didn't say it. She didn't look quite straight at me, pulled askew by some string I couldn't see. But in a wave of time's hand I would have my answer either way."
        MC "Well, I hope we're not too late for the mackerel soba, eh?"
        "Naomi looked straight ahead as we meandered down the hall."
        $setAffection("GTS", 2)
        GTS "We will just have to wait and see."
        jump GTS026_c2
    else:
        MC "Well, reconsidering."
        "I thought about it for a second, as her eyes drifted over and down to me from those high corners, and dampened my voice a few decibels."
        MC "I'm sure you understand why I don't go into too much detail right now, but I think my unreadiness was just sort of a... momentary thing."
        "My flitting tongue dredged up my words like iron slag."
        MC "And I think that now, I'm ready to say..."
        show GTS surprised
        GTS "Ah..."
        MC "Hm?"
        show GTS sad
        $setAffection("GTS", 1)
        GTS "I appreciate the sentiment, but..."
        MC "Right... right, of course."
        MC "Well, hey, what about a change of scenery? Are you free tonight?"
        show GTS neutral
        GTS "I believe I am, yes."
        MC "We could have dinner at the sushi place on Genki street. Have you been there yet?"
        show GTS neutral at Transform(xzoom=-1)
        "The first creases of a smile blossomed on her face."
        GTS "There were a few dishes there I still wanted to try."
        MC "Cool. Let's say we meet by the bus stop at five tonight."
        GTS "Let's."
        jump GTS026_c2

label GTS026_c1_2:
    show GTS happy
    GTS "A balm to be sure. Thank you for asking."
    MC "Another one brought back from the brink, Doctor Yamazaki."
    show GTS embarrassed at Transform(xzoom=1)
    GTS "Oh, I don't know that that's necessary."
    show GTS neutral
    GTS "What about you, Hotsure-san? I've tried to leave you a stable foundation, if it should come to that."
    MC "And I appreciate that. It does satisfy the monkey brain to see that hole filled in, doesn't it?"
    GTS "Indeed."
    show GTS neutral at Transform(xzoom=-1)
    "A silence settled in the golden warmth of the hall, if only for a moment."
    MCT "...{w} Damn, she's playing on another level."
    MC "So hey, do you think you'd want to have dinner tonight? Just you and me?"
    GTS "I think I would. Did you have anything in mind?"
    MC "What about... the sushi place on Genki street? Like around five tonight."
    GTS "How auspicious. There {i}were{/i} some dishes there I wanted to try. I think sitting down would be lovely."
    MC "Same. Well, guess I'll see you then."
    show GTS happy-2
    GTS "Splendid!"
    jump GTS026_c2

label GTS026_c2:
    hide GTS with dissolve
    "We continued together to have lunch with what time remained. Of course, we spared a second to say 'itadakimasu'."
    stop music
    scene black with fade
    pause 1
    scene Dorm Exterior with fade
    "My blood was ice."
    "Breathing in, breathing out. I was alive."
    "And yet, as I ambled through the school grounds with my legs clanking along on their own, I felt like an invertebrate crammed into a not-very-new school dress shirt."
    if getFlag("GTS025_kiss"):
        "I couldn't help but think that run over as it might, how easily my cup could shatter."
        "What was I to her, really?"
        "We'd known each other a couple months, and this cheesy-ass date was my idea to escalate things. One little flower in the patch that went without food for a while."
    else:
        "I knew by then, with needles swimming under my skin, exactly what my relationship with Naomi meant to me. And how precarious I had made it."
        "I had to know that by tonight it could be over before it had begun. Who could blame her, really?"
    "Breathing in, breathing out. I was alive. And I stayed the course."
    scene School Front with fade
    $setGTSOutfit(OutfitEnum.CASUAL)
    "I arrived, no less becalmed within but steady without. I set my eyes flat and my back straight; there was a certain image required, after all."
    "And as I partook of the late afternoon quiet, a distinctly straight, gentle line of footsteps grew closer behind me. I turned to behold her."
    play music Peaceful
    show GTS neutral with dissolve
    "Silently, I ceased to breathe."
    "Her very presence cast me in blessed shade, as her wavering straw hat did for her. The rest of her statuesque frame was wreathed in the sleepy, swaying grays and blues of a distant mountain."
    if getSkill("Art") > 3:
        MC "Yamazaki-san, you look like a work of art, and an original at that."
        show GTS happy
        $setAffection("GTS", 1)
        GTS "Well! One might accuse you of flattery, but your face looks especially candid right now."
        GTS "Erm... pardon me. Thank you, Hotsure-san."
    else:
        MC "Wooow, is that a new outfit? You look really good."
        show GTS happy
        GTS "Why, thank you. I actually bought this hat for working out in the sun, but I had a feeling it would be a proper cap-off for my ensemble."
        MC "About how long were you thinking that up?"
        show GTS wink
        GTS "I, for one, believe it's the thought that counts."
    show GTS neutral
    GTS "You've put yourself together impressively, as well. I recognized you from across the plaza."
    GTS "...I don't know if anyone has ever looked at me quite that way before."
    MC "Heh heh... hope you'll pardon my tactlessness."
    show GTS happy
    "She subtly shook with a muffled chuckle."
    GTS "Not at all."
    show GTS neutral
    GTS "Well then, are we waiting for a bus, or shall we walk into town?"
    "I shrugged."
    MC "Seems like a fine hour for a walk."
    show GTS neutral at Transform(xzoom=-1)
    GTS "It surely does."
    "I put one hand behind my back and held the other up by my neck, whereupon she took it in her own, smiling."

    scene Field with fade
    show GTS neutral with dissolve
    "As we made our way down the sidewalk through the valley, the vastness of the wind struck me; grasses cast in a mild pre-evening ochre swayed just in time with the folds of Naomi's skirt and jacket."
    "It struck me how all this way she'd just been inching her feet along."
    "She was still holding my hand as the edge of town crept into view; hers encased mine entirely, and in the direct sunlight the inside was beginning to grow damp. I decided, then, to disturb the otherwise comfortable silence."
    MC "Should we let go now?"
    GTS "Do you want to?"
    MC "Well... I think it'd be best."
    "She nodded, and I slid our hands apart. She folded hers together and kept on with her drowsy, contemplative eyes forward."
    pause 0.5
    "I suppose at the same time we came to notice the up-and-down whooshing of the cars and buses going by on the road; even they were low and mild."
    "Naomi's gaze lingered on them for a few moments, while I perceived her expression shift just slightly downwards."
    menu:
        "What're you thinking about?":
            jump GTS026_c2_1
        "(Remain silent)":
            jump GTS026_c2_2

label GTS026_c2_1:
    if getAffection("GTS") > 20:
        $setFlag("GTS026_bus")
        GTS "It occurs to me that if I do become tall enough to warrant moving to special facilities..."
        show GTS neutral at Transform(xzoom=-1)
        GTS "...I suppose public transport on the mainland will be closed off to me for good."
        MC "I mean, you could probably squeeze into a..."
        MC "Hm... that'd be difficult with the crowds."
        show GTS neutral at Transform(xzoom=1)
        GTS "More than difficult. Practically speaking, it would be unconscionable."
        MC "You don't seem particularly bothered."
        GTS "Oh, hardly. I must confess, I was hoping you would propose a stroll."
        GTS "It's merely an observation."
        "I twirled my finger over my scalp."
        MC "Like how I'm never gonna be hired at a restaurant?"
        $setAffection("GTS", 1)
        show GTS happy
        "Her sharp, chirping guffaw told me that caught her off-guard."
        GTS "I suppose so!"
        MC "Well hey, I clipped it not too long ago. Maybe we can get a free meal if I can convince the waiters some of theirs got in my food."
        GTS "Don't you dare, Hotsure-san, I {i}will{/i} hold you to your honor."
        MC "If you say so."
        "She smiled down at me a moment, before cracking one last inaudible chuckle."
        jump GTS026_c3
    else:
        GTS "Oh, nothing in particular apart from taking in the view."
        MC "It's a great one."
        show GTS happy
        GTS "It really, really is."
        jump GTS026_c3

label GTS026_c2_2:
    "The moment passed, and I wondered if I'd really seen anything at all."
    "I took in the view alongside her, then, and I could feel myself begin to warm in spite of the uncertainty in the air. For the first time, in its way, the island began to feel a little homey."
    jump GTS026_c3

label GTS026_c3:
    scene Town with fade
    play music BrightLights
    "Town was alive, but thankfully not crowded. We rounded a few corners and found our destination with nary a line, and I gave thanks in my head as I ushered Naomi in."
    scene Restaurant with fade
    "She stooped in, and after I followed suit and the door jangled behind me, I greeted the waitress; she kindly directed us to a table buffered at least one away from any other."
    show GTS neutral with dissolve
    Waitress "Alright, welcome! Would you guys like a drink to start off?"
    MC "Hm... what'll you have, Yamazaki-san?"
    GTS "Do you have sencha, perchance, miss?"
    Waitress "We do, would you like that?"
    show GTS happy
    GTS "Yes, please!"
    Waitress "Great! And for you, sir?"
    show GTS neutral
    MC "I think I'll have some matcha, please."
    Waitress "Absolutely, you guys can have a look at the menu if you please and I'll bring your drinks right out for you."
    MC "Thanks!"
    GTS "Thank you!"
    "The waitress bowed with a well-crafted smile and left us."
    MC "So what did you get last time?"
    GTS "...The unagi roll, I believe it was. I wanted to try the crab roll as well."
    MC "That does look good. As does the shimesaba... hmm..."
    GTS "I should say so, looking at it."
    "Out of the corner of my eye I spotted our server approaching the table with two steaming glass tea cups, one a familiar green and the other a more verdant gold. She set each in its place in front of us and bowed."
    Waitress "Have you had a chance to decide?"
    "I gave Naomi an inquisitive glance, and she nodded."
    GTS "I would like an unagi roll, please."
    "The woman nodded and rattled off enthusiastic affirmatives as she scratched in the order."
    Waitress "And for you sir?"
    menu:
        "One crab roll, please.":
            jump GTS026_c3_1
        "One crab roll and a plate of shimesaba, please.":
            jump GTS026_c3_2

label GTS026_c3_1:
    Waitress "Mm hm... coming right up!"
    "Thanks were given, and she went away once more."
    jump GTS026_c4

label GTS026_c3_2:
    Waitress "Mm hm... coming right up!"
    MC "Thanks!"
    GTS "Thank you, miss."
    "She bowed once more and went away."
    show GTS surprised at Transform(xzoom=-1)
    GTS "Hotsure-san... I should tell you, their proportions are generous. Do you intend to eat all of that yourself?"
    MC "Oh, no, not at all. I figured we'd split the shimesaba."
    show GTS happy
    GTS "Oh, I see. Thank you kindly."
    show GTS neutral at Transform(xzoom=1)
    jump GTS026_c4

label GTS026_c4:
    "Naomi took the moment to ease her finger through her teacup handle and lift it for a sip."
    "Her eyes drifted closed as she took it in, and I could see the languor with which she savored the hot brew."
    "I felt compelled to take a sip of mine, too. Her eyes opened as I did, but she waited for me to finish."
    GTS "Well now, I think it best that we clear the air."
    GTS "There is something I would like to say first, if you wouldn't mind."
    MC "Of course."
    "I took another sip. It tasted not unlike what they served at my high school cafeteria."
    show GTS neutral at Transform(xzoom=-1)
    GTS "Well, I've tried to consider what's probably been going through your mind in, well, what feels like no time at all."
    GTS "If you find I have misunderstood you, I apologize."
    GTS "But to tell you the truth as I see it..."
    "I had to lock what felt like every muscle in my body to maintain eye contact."
    "And by God, for what?"
    GTS "I think we should be together."
    if getAffection("GTS") > 20:
        GTS "There's a wholesomeness in you, Hotsure-san, and I can tell that it's genuine."
        GTS "So often you know just what to say, and not just to me, it seems, but to almost everyone."
        if getSkill("Academics") > 5:
            GTS "You clearly have a good head on your shoulders, as well."
        if getSkill("Art") > 5:
            GTS "And even more than that, you're such a soulful person, full of life."
        GTS "It is not my nature to put it so plainly, but even for what time we've spent together, all of that means a great deal to me."
    else:
        GTS "It may not be particularly natural for me to put it so bluntly, but I earnestly like you, Hotsure-san."
        GTS "I sincerely would like to get to know you better."
    GTS "That is my truth."
    "She folded her hands and wrung out the slightest smile."
    GTS "I do hope I haven't just made a fool of myself."
    "To my chagrin, I was simply gobsmacked for a few seconds. At last I let out a puff of... relief, I guess."
    MC "Well, you didn't misunderstand me, Yamazaki-san. I feel much the same about you, to put it plainly."
    if not getFlag("GTS025_kiss"):
        MC "To be totally honest, I was a bit worried that I had missed my chance yesterday."
        show GTS happy
        GTS "Certainly not. I perfectly understand why you might need time to consider it."
        show GTS neutral
    else:
        GTS "That puts me greatly at ease."
    GTS "However, there's something else I would like to share with you, Hotsure-san."
    MC "I'm listening."
    GTS "Well, if we were to call what we have by its more proper nomenclature, I would prefer to abide by more proper channels."
    "I took another quiet sip of the rich matcha as I pondered her meaning."
    if getSkill("Academics") > 2:
        MC "I see."
        MCT "Probably should've seen this coming now that I think of it."
        MC "Yeah, I understand, and that's fine. But what does that mean for us now?"
    else:
        MC "I'm, uh, not sure I follow."
        GTS "Well, my parents' guidance is paramount to me. I would like to have their explicit blessing before I'm comfortable with anything official."
        MCT "Well... there goes that plan."
        MC "Oh, I get it. I respect that."
        MC "But then... what do we do until then?"
    show GTS neutral at Transform(xzoom=1)
    GTS "That's not to say I don't want to see you or be with you."
    GTS "Oh, how do I put it?"
    MC "Committed in all but name?"
    MC "I can live with that."
    show GTS happy
    "I got to see another glimpse of her perlescent grin as we looked over each other. I could feel that I was wearing a similar expression."
    show GTS neutral
    "The waitress at once appeared by our table, having deftly escaped my notice, and she bore down an unequivocally generous trio of crab rolls and shimesaba betwixt us. Lastly, she set down a pair of wrapped chopsticks."
    Waitress "Is there anything else I can help with?"
    MC "Oh, no, this oughta be just fine. Thanks."
    "She bade us to enjoy the meal and bowed out."
    MC "Hmmm... ah. That marinade smells choice."
    GTS "I agree entirely."
    "I picked up my chopsticks and tore the top off while Naomi did the same. But then I saw her lay them down, a babe into a cradle, and she clasped her hands together."
    "I followed."
    MC "Itadakimasu."
    GTS "Itadakimasu."
    jump daymenu

label GTS027:
    if getFlag("GTS015_movie"):
        $setProgress("GTS", "GTS028T")
    elif getFlag("GTS015_shopping"):
        $setProgress("GTS", "GTS028S")
    else:
        $setProgress("GTS", "GTS029")
    scene Dorm Interior with fade
    "I was sitting at my desk playing Left to Die 2 when my phone buzzed."
    GTSCell "Do you have a pair of scissors?"
    MCCell "I do. Do you need them now?"
    GTSCell "If it's not a problem, it would be appreciated."
    MCCell "Be over soon."
    "Saving my game, I grabbed the scissors from my supply drawer and headed over to her dorm."

    scene Dorm GTS with fade
    play music GTS
    "Stepping inside, I saw Naomi sitting in a Seiza position next to the table. Her hands worked on something obscured by her body."
    "Walking over I saw that on the table in front of her was a Bonsai tree."
    MC "Oh, a Bonsai tree. Now the scissors make sense."
    show GTS neutral with dissolve
    GTS "They are not ideal but aren't a terrible option either."
    MC "What's the other option? I've only ever seen people use scissors on these trees."
    GTS "Ideally you want to use Bonsai shears. The difference isn't very visible but means a lot to the tree's health."
    GTS "Regular scissors are often too blunt to properly cut and will normally tear the tree fiber. Shears are much sharper allowing for cleaner cuts that don't damage the tree fiber so severely."
    GTS "Do you have much experience with Bonsai trees?"
    menu:
        "I've worked on many Bonsai trees in my time.":
            jump GTS027_c1_1
        "Not really, only what I've seen in movies or TV.":
            jump GTS027_c1_2

label GTS027_c1_1:
    show GTS happy
    GTS "Really? That's amazing to hear! Can you do the pinching? My hands aren't as precise as they used to be with it."
    MC "Oh... sure, I can do it."
    "I sit down next to her and begin desperately attempting to remember anything I'd ever seen on TV and from movies about Bonsai trees."
    "I slowly started clipping at various leaves and branches that I assumed weren't uniform to the tree's shape."
    show GTS angry
    GTS "Hotsure-san, if you actually don't know I'd appreciate it if you stopped."
    MCT "Was it that obvious? Well, no use hiding it I suppose."
    MC "Sorry, just wanted to impress you."
    $setAffection("GTS", -1)
    GTS "Lying for the sake of impressions is very unbecoming."
    MC "My apologies, Yamazaki-san. Sorry if I ruined your tree. I can get going if that's what you want."
    "I felt her hand rest on my shoulder just as I began to stand up."
    show GTS neutral
    GTS "While lying is something I'm not pleased with, I can't deny that you at least had the right idea."
    MC "I'm confused what you mean by that. I was just going off what I'd seen others do."
    show GTS unique
    GTS "Which is a great place to start and you showed you at least understood them. When you were cutting randomly I could see you were aiming for a static visual balance."
    show GTS neutral
    GTS "Visualizing and acting out the changes to shape the tree in such a manner takes some skill to execute well. I think you have the skill, just not the understanding."
    MC "That's really sweet of you Yamazaki-san, I was afraid you would be furious I maimed your tree."
    GTS "The tree will heal and the mistakes will fade. There's no reason to get angry over small mistakes. Just don't lie to impress me in the future, ok?"
    MC "I won't Yamazaki-san, I promise."
    show GTS happy
    GTS "That's great to hear and I hope you mean it."
    show GTS wink
    GTS "Now then, would you be open to taking some lessons from me? I would be disappointed if you didn't get to use those great visualization skills you possess."
    MC "It would be rude to deny such a beautiful offer."
    show GTS aroused
    GTS "Please remain focused on the tree, Hotsure-san. it would be a shame if I caused you to make more mistakes."
    MCT "I know she forgave me, but now I feel like an idiot for trying to be good at something she cares alot about. I wouldn't be surprised if she was a little insulted by me doing that."
    "We still worked on the tree, but the incident had blown a pretty big hole in my ego."
    jump daymenu

label GTS027_c1_2:
    MC "Not really. My only experience with them has been what I've seen in movies or on TV."
    GTS "That is most people's exposure to them; they are the symbols of Japan to many people."
    MC "Did you ever see the movie Karate Boy?"
    show GTS embarrassed
    GTS "I can't say I have seen that particular title."
    MC "Better hope Ryoko doesn't hear that or she'll pull out a projector and screen."
    show GTS happy
    GTS "You are probably right on that assumption."
    MC "Anyway, in the movie the main character's teacher gives him a Bonsai tree to practice with. That was my first exposure to these plants as a kid."
    show GTS neutral
    GTS "In the movie, did the teacher say why he gave the kid the Bonsai tree?"
    MC "I think he said it was to teach patience and balance. I never did understand how you learn balance from a tree."
    GTS "That is actually a nice detail for them to include with a Bonsai tree. Balance is very important to the shape of a Bonsai tree as it determines how the tree is to be interpreted."
    GTS "A static balance is a very common design, which through symmetry leads to a clean, restful shape. A dynamic balance is asymmetric and implies movement or instability."
    GTS "So the teacher was probably trying to have the student learn a static balance since that's very important in Karate."
    MC "You know alot about these trees, you must've worked on these things for years."
    GTS "This tree here I've had for nearly eight years. My mother's grandmother originally had it before giving it to me as a birthday gift."
    MC "It must mean alot to you. I can't imagine how you'd react if something happened to it."
    GTS "Depends, but I was always taught that things often happen without your input. In those cases it's best not to be angry about them and instead forgive and forget."
    MC "That's a very good mindset to have. I doubt I could keep a level head if I was in a similar position."
    MC "So, are you gonna show me how this stuff is done?"
    show GTS sad
    GTS "Well, that is something I wanted to ask you. You see, my hands have gotten too big to work with its intricate branches. Could you trim it?"
    MC "You sure about this? I have no idea what I'm doing."
    "Naomi pulled me down onto the ground between her and the table, planting her hands on my arms."
    show GTS aroused
    GTS "I can guide you, if you'd accept my help."
    MC "Su..su..sure, that would be great."
    $setAffection("GTS", 1)
    show GTS neutral
    GTS "Well, let's start visualizing in our head what we want this tree to look like. The shape we want to imagine is this tree with a half dome. Once we have that image in our head apply it to the tree to see where we need to start trimming."
    MCT "Alright, let's try this. It shouldn't be too hard, right? Just a half dome."
    pause 1
    MCT "I think I got the picture, now let's hope I can remember it."
    show GTS neutral
    GTS "Do you have a clear image of what you want in your head?"
    MC "I believe so, a half dome like you said."
    GTS "Excellent, now comes a slightly harder task to execute. The next step is to pinch new growths that would disrupt the uniformity of the design. This can be tricky as we want to give the tree shape, but don't want to leave an artist trace."
    MC "I thought Bonsai trees were understood to be designed and sculpted like art pieces."
    GTS "It would be inaccurate to call them art pieces. They are still living plants that grow and change over time, unlike a statue or painting that is static and unchanging."
    GTS "The idea of not leaving an artist's trace is to shape the tree in a way that could be seen as natural."
    MC "Ok, I see what you mean now. So, trim it like a tree would normally appear, but just remove the shaggy bits that would make it unbalanced."
    show GTS happy
    GTS "Precisely Hotsure-san, that is the exact idea. Now that you understand what to do as far as shaping the tree, the rest should be easy. This particular tree is a juniperus communis, so we should be looking for this tree's budding shoots."
    "She pointed to a branch that resembled the texture of a lizard's scales."
    show GTS neutral
    GTS "This shoot needs to be trimmed back to maintain our future balance. Insert the scissors parallel to the shoot and cut."
    "I gingerly maneuvered the scissors into position, making sure not to snag any other branches, and cut."
    show GTS happy
    GTS "Perfect job, Hotsure-san. Now, let's repeat that for this shoot here."
    "For the next couple hours we sat together, Naomi guiding my arms and mind in the ways of Bonsai maintenance. The hours of the day slipped away as she held me until long after the sun had set behind the horizon."
    show GTS neutral
    GTS "I think that's all we can do today. The tree will be blooming until August, so you'll have more time to practice on it."
    MC "Wait, I'll have more time to practice? Aren't you gonna be helping me?"
    show GTS sad
    GTS "As I said earlier, at my current size I can't work with this delicate tree. I doubt by August the situation will be any different."
    MC "So you want me to have your family's tree? You sure you can part with it to someone you only recently met?"
    show GTS embarrassed
    GTS "I can tell in my heart you will take good care of this tree since you know what it means. You can always bring the tree to me if you have any questions when summer fully arrives and you'll need to repot it."
    MC "I don't think I can thank you adequately for trusting me with this. I'll make sure it will be cared for properly at all times."
    "I stood up and grabbed the tree from the table, making sure I had a firm grasp on the pot."
    show GTS unique
    GTS "I had a feeling you would. Now then, you'd better be heading back to the dorms. I'd hate for you to get chewed out by Matsumoto-san for being in the girls' dorms after dark."
    MC "I enjoy living, so I'll make sure to make haste. Thank you again for the evening Yamazaki-san."
    "She leaned over and kissed me on the cheek for a brief moment before leaning back."
    show GTS aroused
    GTS "I'm glad you enjoyed yourself as much as I did tonight. I hope we can do something similar to this in the future."
    MC "That is a lovely idea, and one I look forward to making a reality."
    "I waved goodbye and briskly made my way back to my dorm."
    jump daymenu

label GTS028S:
    $setProgress("GTS", "GTS029")
    scene Town with fade
    "I realized then that I couldn't remember ever seeing Naomi in a hurry."
    play music Busy
    $setGTSOutfit(OutfitEnum.CASUAL)
    show GTS surprised with dissolve
    "But I was certainly enjoying the sight of her in her elegantly understated ensemble... even if it was a bit clingier than last week."
    "Despite her wide-brimmed hat, she was fanning herself. Her hand, like dragonfly wings, moved with blurring speed and delicate grace as she breathed through the sliver of her open mouth."
    "I could even feel some of the puffs of air as she waved, her palm now big enough to cover my face, and boy, could I ever use the refreshment."
    MC "Hah... well, mission accomplished, huh?"
    GTS "Yes, erm... I do apologize for my lack of foresight."
    MC "I told you Tanaka-san was chill. They probably wouldn't have cared if we {i}were{/i} a few minutes late."
    show GTS neutral
    GTS "A lesson learned, indeed."
    MC "Where are they, anyway? Tanaka-san wouldn't just bail, Tomoe-san {i}definitely{/i} wouldn't."
    GTS "Perhaps the bus has been delayed."
    MC "Could've been. I guess you do make a pretty good pace now, too, even when you're walking."
    show GTS surprised
    GTS "Yes, well, life is rather a complicated machine, is it not?"
    MCT "She's cute when she deflects."
    MC "Guess so.{w} Well, what do you wanna do today?"
    show GTS neutral
    GTS "The day affords us many options, doesn't it? Hmmm..."
    "She contemplated in silence as cars rolled leisurely by; the swaying canopies of the trees shimmered by her head, and the effect as I looked up at her was..."
    "I couldn't fully absorb it, as her eyes widened at some sight behind me."
    show GTS happy
    GTS "Ah, that looks to be them now!"
    "I looked down the street behind me to see a beastly, rumbling curmudgeon of a bus heading our way."
    MC "...Wow. Look who rolled up all the way from the Koizumi administration."
    show GTS neutral
    GTS "My, that {i}is{/i} a relic."
    "Its arthritic axles ground to a slow halt at the stop before us; it was then that I observed how close Naomi was, standing there with her hands folded, to being able to see over even the island's enlarged buses."
    "The door folded open, and glossy heads filed out into the sunlight; one was a fiery red, and one right behind it clay brown."
    show Ryoko neutral at Position(xcenter=0.8, yalign=1.0)
    show Minori neutral at Position(xcenter=0.2, yalign=1.0)
    with dissolve
    Ryoko "Yamazaki-san, Hotsure-san!"
    show Ryoko annoyed
    extend " We finally meet."
    Minori "Apparently the normally scheduled bus needed maintenance."
    GTS "Ah, I see. Well, I'm glad you two made it without too much difficulty."
    show Ryoko happy
    Ryoko "The feeling's mutual!"
    show Ryoko neutral
    extend " Now, where are we headed first?"
    MC "...How about lunch? I think I saw a ramen joint a block over."
    show Ryoko happy
    Ryoko "I'd go for that!"
    Minori "Agreed."
    GTS "Let's."
    show Ryoko neutral
    "We made our way over to the spot; I could tell Naomi wasn't having such an easy time keeping pace with the three of us."
    "Minori strolled with easy leisure behind us, while Ryoko had to slow down every so often as she realized she had passed me, her eyes otherwise always scanning the scenery for... I don't know what."
    "And there it was, Akashi's Up North Noodles. A walrus-like entity with soba whiskers watched, with joyous eyes, the procession of hungry salarymen meandering in as they muttered the day's gossip amongst each other."
    "None of us could really be surprised to see the line very nearly stretching out the door, but nevertheless I saw we still had just enough room to squeeze the four of us in."
    stop music fadeout 2.0
    "And squeeze we did... Naomi, of course, ducked too."

    scene Cafe with fade
    play music DayByDay
    MC "'Scuse me!"
    "The air was hot and soupy, its thick smell like a potpourri of meats with just a pinch of salt."
    #I give up trying to figure out how to do this without everyone's Y axis going nuts.
    #show Ryoko neutral:
    #    xanchor 0.5 yanchor -0.055 xpos 1.1
    #    linear 0.4 xpos 0.95
    #    pause 0.5
    #    linear 0.4 xpos 0.8
    Ryoko "Coming through, sorry!"
    show Ryoko neutral at Position(xcenter=0.8, yalign=1.0) with dissolve
    "With the first of my companions coming in behind me I was suddenly reminded of the subways back home. I couldn't afford to linger on the thought, though, if I didn't want to be frenching the t-shirt on the guy in front of me."
    #show GTS neutral:
        #xanchor 0.5 yanchor 0.0 xpos 1.2
        #linear 1.5 xpos 0.9
        #pause 0.5
        #linear 1.0 xpos 0.8
        #pause 0.5
        #linear 1.0 xpos 0.7
        #pause 0.5
        #linear 1.0 xpos 0.6
        #pause 0.5
        #linear 1.0 xpos 0.5#
    GTS "Pardon me, my apologies."
    show GTS neutral with dissolve
    "Behind the counter were two men; one with a frazzled, weathered brown beard scribbling down and dishing out orders like a well-oiled machine..."
    "...And the other stood a head above his coworker, and everyone else in the room except Naomi, his rippling, oaken forearms expertly composing bowls of ramen with only the occasional pause to wipe his thick, grease-splattered glasses."
    #show Minori embarrassed:
    #    xanchor 0.5 yanchor -0.04 xpos 1.1
    #    linear 1.5 xpos 0.9
    #    pause 0.5
    #    linear 1.0 xpos 0.8
    #    pause 0.5
    #    linear 1.0 xpos 0.7
    #    pause 0.5
    #    linear 1.0 xpos 0.2
    Minori "Oh, um, pardon me, sorry."
    show Minori neutral at Position(xcenter=0.2, yalign=1.0) with dissolve
    "They worked almost like one mind in two bodies; I watched the line shrink ahead of us as if we were all on a wood paneled conveyor belt. That was when I realized I hadn't actually thought of what I wanted."
    "Nevertheless, we sidled up against the counter as the man scanned us with a notepad in his hand and a warm crinkle in his beard. I quickly glanced up at the menu on the wall."
    Cashier "Hey, how are ya? What can I do for you guys?"
    MC "I'll have, uhhh... bowl of shoyu with a can of matcha, please."
    Cashier "You betcha, bud! And what do you lovely ladies want?"
    Minori "Tonkotsu, please."
    GTS "I would like a bowl of hakodate with a bottle of water, please."
    Ryoko "I want a bowl of shio with narutomaki, soba cooked extra firm, some carrot straws, a splash of orange juice and no egg white. Oh, and a bottle of water, please."
    Cashier "You betcha!"
    "He turned his head halfway back towards the muscular gentleman behind him."
    Cashier "Order up, Kazunari! One sho, one ton, one ha, and a shio extra firm redhead with goo, make it dizzy and paint it orange."
    Chef "You betcha, dad!"
    Cashier "Alrighty, that'll be thirty-six hundred there, if ya please."
    show GTS happy
    GTS "Allow me."
    menu:
        "Accept":
            MC "Thanks, Yamazaki-san."
            $setAffection("GTS", 2)
            show Ryoko confused
            Ryoko "We could've just split the bill."
            show Ryoko neutral
            extend " Appreciate the gesture, though. Thanks."
            $setAffection("GTS", 2)
            show GTS neutral
            GTS "My pleasure."
            "She produced a slender leather coinpurse from her jacket, and counted out the exact amount before she bowed and lowered the neat stack of bills down to the cashier's wrinkled hands."
            Cashier "Thankya miss! I'll getcha your drinks."
        "Offer to pay for the group":
            $setFlag("GTS028S_pay")
            MC "Hey, don't worry about it, I'll get it."
            show GTS surprised
            show Ryoko confused
            GTS "Oh? Are you quite sure?"
            MC "Yeah, for sure. Consider it my contribution to the gang."
            show GTS neutral
            $setAffection("GTS", 1)
            GTS "Well, that is very generous. Thank you, Hotsure-san."
            Ryoko "We could've just split the bill, Hotsure-san."
            show Ryoko neutral
            extend " Appreciate the gesture, though. Thanks."
            Minori "Very much."
            MC "No problem."
            "I fished out my wallet, gazed down into the flap as I unfurled it..."
            MCT "Yeesh, chivalry hurts. Me and my big mouth..."
            "I produced the requisite bills and handed them over. The gaunt stack of wan yellow bills that remained stared up at me as I shut them away back into my pocket."
            Cashier "Thankya sir! I'll getcha your drinks real quick."
    "We each took our drinks in turn as he set them out; the can was cold and dewy in my hand, and in the midst of the steamy air I savored the feeling."
    "The muscled young cook’s quick work soon made good on his father’s promise, hardly breaking a sweat through Ryoko’s spiderweb of an order."
    "We were off with warm ceramic bowls in our hands... Naomi quickly found it easier to hold hers in one... and we scanned the room for a bench table."
    "Minori squeezed by first with a muttered apology and sat in one corner, laying her clipboard on her lap."
    "Ryoko followed, bending her arms to avoid a handful of idle customers, and scooched in next to her faithful companion."
    show GTS surprised #note to self, an embarrassed sprite would be ideal
    GTS "Would you like to go first, Hotsure-san?"
    MC "Nah, I wouldn’t want you squished up against the wall. You can go if you want."
    GTS "Well, that’s very considerate of you."
    "She brought her arms in around her waist as close as she could, at which point most of the people standing around made some room."
    GTS "Pardon me..."
    "She shimmied around the table’s edge and up next to Ryoko before seating herself; though the seating was clearly built with factors in mind, I yet beheld Naomi’s head-sized silken shoes and just a bit of her shins peeking out from the shadow of the table."
    show GTS surprised
    "She noticed, too, and promptly drew them back until her knees hit the plywood."
    show GTS neutral
    "Then it was my turn, and thankfully it looked like I had just enough room."
    MC "Hm..."
    "I was squeezed against the wall, but also the stiff but still soft plastic cushion, as well as Naomi’s skirt-swaddled left hip, more like a giant, warm pincushion. Not bad accommodations, all told."
    "I looked up at the faintest blush on her cheeks as she closed her eyes and brought her hands together. I followed suit."
    All "Itadakimasu."
    Ryoko "-kimasu."
    MC "Smells pretty good."
    show GTS happy
    GTS "That it does."
    "I bundled up some in my chopsticks and took a bite; I was not disappointed."
    show Ryoko happy
    Ryoko "Mm-mm! They nailed it, it’s flawless."
    MC "Against all odds."
    show GTS aroused
    "Naomi let out a cough that sounded an awful lot like a stifled laugh. I smiled."
    show GTS neutral
    show Ryoko tongue
    Ryoko "Not a crime to know what you like, Hotsure-san."
    GTS "How are yours, Tomoe-san and Hotsure-san?"
    show Ryoko neutral
    MC "Pretty good."
    Minori "Pretty good."
    pause 1.0
    MC "How’s yours, Yamazaki-san?"
    "She tapped her chin with the thick ends of her chopsticks."
    GTS "It reminds me a great deal of when my friends and I would try out different restaurants in Kyoto."
    MC "I see. Not your favorite?"
    show GTS neutral #another spot where an embarrassed sprite would be useful
    GTS "I do usually prefer a bit crisper scallions."
    show GTS neutral
    extend " Otherwise, it’s rather tasty."
    stop music fadeout 2.0
    "I nodded, and then tucked into my own bowl. We had a full afternoon ahead of us, after all."
    scene black with fade
    pause 1

    play music Sunset
    scene Town
    show Ryoko neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0)
    show Minori neutral at Position(xpos=0.2, xanchor=0.5, yalign=1.0)
    show GTS neutral
    with fade
    Ryoko "Okay, one thing down. Since Tomoe-san and I know where we're going, where do you two wanna hit today?"
    menu:
        "I think I'm good on supplies. Anybody mind if we stop by the manga shop?":
            jump GTS028S_c2_1
        "I think I'm good, actually.":
            jump GTS028S_c2_2
        "Hmm... Yamazaki-san?":
            jump GTS028S_c2_3

label GTS028S_c2_1:
    $setFlag("GTS028S_manga")
    Ryoko "Nah. In fact, that's a little closer, isn't it? Let's stop there first."
    MC "Cool, let's go."
    "Naomi and Minori nodded along, and away we went."
    "We stopped for a moment at a crosswalk shaded under a pine. Naomi looked up and sighed with a smile by my side."
    Ryoko "Out of curiosity, Hotsure-san, what are you looking for?"
    "Inexplicable anxiety poured into my stomach at the question, like I was being asked by the mangaka themselves on exam day in my underwear."
    MC "Uhhh, it's called Cyborg Girl Detective Re:Make."
    show Ryoko happy
    Ryoko "Oh yeah, I remember that series! Fun read. Never really followed it, though."
    show GTS pondering
    GTS "Pray tell, what in particular do you like about it?"
    "I shrugged."
    MC "I like the art style, and a lot of the mysteries were pretty good."
    MC "And I do like a good mystery. It's almost like its own game, trying to figure what's going on in each character's head."
    show GTS neutral
    GTS "I see; that would be rather enticing."
    Ryoko "Speak of the devil, I think that's the place just ahead."
    scene black with fade
    pause 0.5

    scene Library with fade
    MC "Woah."
    show Ryoko neutral at Position(xcenter=0.6, yalign=1.0)
    show GTS surprised at Position(xcenter=0.8, yalign=1.0)
    show Minori neutral at Position(xcenter=0.2, yalign=1.0), Transform(xzoom=-1)
    with dissolve
    GTS "Is something the matter?"
    MC "Nothing, it's just... I am very not used to seeing a manga shop with aisles this wide."
    MC "Honestly it's kinda nice."
    show GTS neutral
    MC "Alright, it should be around this aisle here..."
    "I walked down a few rows, only to stop with a start just short of my destination."
    MCT "Wait, is that..."
    MC "Hey, Honoka!"
    "She broke her focus on the shelves and turned around with a light, quizzical expression, before breaking into a full, sunny grin as she jogged towards me, her watermelon breasts and her shopping bag dancing the samba the whole way over."
    show BE happy at Position(xcenter=0.4, yalign=1.0), Transform(xzoom=-1) with dissolve
    BE "Hey hey, wassup Kei-chan?"
    show BE neutral at Transform(xzoom=1)
    pause 0.5
    show BE happy at Transform(xzoom=-1)
    BE "And you brought the whole squad, very nice. Whatcha guys doing?"
    MC "Just out on the town. I was gonna see if they have the new issue of CGDR."
    show BE wink
    BE "Oh, I see... so you're looking for {i}this{/i}?"
    "She plucked a copy out from her shopping bag between two fingers, out of which they promptly fell to the hard-packed carpet."
    show BE sad
    BE "Hah... {w}Crap."
    "Without a word, I knelt down, picked it up, and handed it back to her."
    show BE happy
    BE "Thanks, Kei-chan."
    show BE neutral
    BE "So, is there anything {i}you{/i} guys are looking for? I'm kind of a local expert."
    GTS "Nothing in particular."
    Ryoko "Just here for the camaraderie."
    Minori "Actually..."
    show BE neutral at Transform(xzoom=1)
    Minori "There's this one series I've been wanting to read, and since we're here..."
    BE "What's it called?"
    Minori "Vegetables Bushel."
    show BE embarrassed
    BE "Awww, I love that one!"
    show BE neutral
    BE "Right this way, I'll show you where they keep the goods."
    Minori "Wow, quite a bit to choose from."
    BE "Best place to start is from the beginning, I say."
    show BE neutral at Transform(xzoom=1)
    BE "Yamazaki-san, you might even like it. I dunno how big of a manga reader you are, but this series has some really well-written romance."
    GTS "Well... it could be worth a read, I suppose. To patronize fine art is to cultivate it, after all."
    show BE happy
    BE "Yep, sure is!"
    show BE surprised
    BE "Oh, Kei, that reminds me, you wanna help me look for the new issue of Cool Summer Ride? It should be just in today!"
    MC "Oh, uh... yeah, sure."
    "She squeezed past the rest of the group and beckoned me to follow."
    hide Minori
    hide Ryoko
    hide GTS
    with dissolve
    pause 0.5
    show BE neutral at altMove(0.5, 0.5)
    MC "What if any of them knew the new issue dropped last week?"
    BE "C'mon, as if it wasn't obvious what I was {i}really{/i} looking for."
    show BE happy
    BE "So the dinner last week! Gimme deets!"
    if getAffection("GTS") > 20:
        MC "It honestly went... awesome."
        BE "Yeah?"
        MC "I've met some girls where the niceness was an act, but her... nah, she's genuine. Really smart and talented, too."
    else:
        MC "It was pretty good. From talking to her, I guess she really likes me."
    BE "Nice, nice."
    BE "Man, Kei-chan, a couple months and you already got a lady on your arm! Slay, king."
    show BE happy
    BE "Or in this case, maybe it's the lady who's got {i}you{/i} on her arm."
    MC "Right? Crazy to think she used to be up to my chin, now I'm not even up to her waist."
    BE "Well, it couldn't have happened to a better person. If {i}I{/i} grew as big as Godzilla, I would absolutely use my powers for evil."
    BE "I'd steal all the chocolate in the world, put my annoying neighbors on top of a building..."
    show BE aroused
    extend " make people kiss..."
    MC "Yeah, Yamazaki-san wouldn't dream of taking chocolate that doesn't belong to her. I don't think she'll even get that big, really."
    MCT "I don't think..."
    show BE neutral
    BE "Yep, she's a lady of class and sophistication."
    "Honoka took one step towards me."
    BE "So remember that you gotta put in work if you really want her."
    MC "I know. I'm gonna really try and impress her from here on out."
    BE "Good. I'm happy for you, Kei-chan."
    MC "Thanks, Honoka."
    pause 0.5
    MC "So, would you wanna come with us for the last little bit of our escapade? I'm sure they'd all love to have you."
    BE "Nah, I got a club meeting I gotta get to at three. Actually, I should probably leave pretty soon. Thanks for offering, though."
    MC "'Course, any time."
    MC "Well, it's good talking to you, Honoka. See you around."
    BE "Seeya!"
    hide BE with dissolve
    "I waved her goodbye before heading back to the group; Naomi accepted blithely when I told her Honoka was bound elsewhere, and Minori and I collectively gathered up a hefty pile of manga to drop by the register."
    "Of course, I let her go first."
    scene black with fade
    $setTime(TimeEnum.EVE)
    pause 0.5

    scene Town with fade
    "The sky had begun to yellow as we headed on, passing a pharmacy. The traffic thickened with spent, homebound workers, and with the twinkle of the first few streetlamps came the suggestion of the town shutting its eyes."
    show Ryoko neutral at Position(xcenter=0.8, yalign=1.0)
    show Minori neutral at Position(xcenter=0.2, yalign=1.0)
    show GTS neutral
    with dissolve
    Minori "Oh! {w}That reminds me, I need to stop in to pick up a prescription. Would you guys mind waiting a little bit for me?..."
    MC "Not at all, do what you gotta do."
    Ryoko "We'll be right here."
    Minori "Thank you."
    hide Minori with dissolve
    "She marched in through the sliding doors with quiet determination etched on her face."
    "After kicking my foot to and fro, I turned to Ryoko."
    MC "So what's the story with her clipboard? It seems like she literally takes it everywere."
    Ryoko "She doesn't have work on her mind 24/7, if that's what you're wondering."
    Ryoko "You could say it's a fidget, or a keepsake. She told me it gives her comfort."
    GTS "That would explain why she's always holding it so closely."
    Ryoko "Mmhm. Even so, I think there's deeper strength in her than her modesty would suggest."
    show GTS happy
    GTS "On the contrary, modesty, diligence, and stoicism are some of the surest expressions of inner strength."
    MC "...You know, maybe to cap off the day, we should get her a little something. Do either of you know if she has a favorite snack or something?"
    show GTS pondering
    GTS "I'm afraid I do not."
    show Ryoko annoyed
    Ryoko "Hmm..."
    Ryoko "When we're shooting, she often shows up to the set with a particular brand of seaweed. I'd recognize the package if I saw it."
    show Ryoko neutral
    show GTS neutral
    MC "Well, it sounds like we've got a plan."
    show Minori neutral at Position(xcenter=0.2, yalign=1.0) with dissolve
    "The doors slid open again and there she was, smiling meekly with a little white bag clipped to her clipboard."
    Minori "Well then, where shall we head next?"
    MC "I say we hit the Kozaku-mart before we head home, my treat. Does that sound alright?"
    show GTS surprised
    Minori "I'd like that."
    GTS "My, my. That's very kind of you, Hotsure-san."
    $setAffection("GTS", 1)
    MC "Don't mention it. Shall we?"
    jump GTS028S_c3

label GTS028s_c2_2:
    Ryoko "Alright, that makes it easy. What about you, Yamazaki-san?"
    $setFlag("GTS028S_noask")
    jump GTS028s_c2_3

label GTS028s_c2_3:
    if not getFlag("GTS028S_noask"):
        $setAffection("GTS", 1)
    GTS "Me? Oh, well..."
    show GTS neutral at Transform(xzoom=-1)
    GTS "Would it be alright if we paid a visit to a video game shop?"
    show Ryoko surprised
    show Minori neutral at Transform(xzoom=-1)
    with vpunch
    Ryoko "Huh? Really?"
    show GTS surprised
    GTS "I don’t mean to impose, of course. I could go some other day."
    MC "No, no, it’s fine. Just... that was kinda the plot twist of the century just now."
    show Minori neutral
    show GTS happy at Transform(xzoom=1)
    GTS "I’m no stranger to electronics, you know. My parents furnished me with a cell phone."
    show Ryoko confused
    show GTS neutral
    GTS "After all, isn’t this the time to broaden our horizons?"
    MC "Can’t argue with that."
    show Ryoko neutral
    Ryoko "You make a good point. Well then, let’s head over there."
    MC "I think this way’s the shortest way."
    "I led the way again through the streets."
    "And so as much as I wanted to steal a glance at Yamazaki-san’s face, I couldn’t."
    MCT "It hasn’t even been a week since we had dinner together. I knew there’d be a lot more to learn about her, but... how many of my other assumptions are wrong?"
    scene black with fade
    pause 0.5

    scene Game Store with fade
    MC "...Sheesh, I thought it would be a little deader than this."
    "I took a few steps forward as Ryoko and Minori followed me,"
    show Ryoko neutral at Position(xcenter=0.8, yalign=1.0)
    show Minori neutral at Position(xcenter=0.2, yalign=1.0)
    with dissolve
    extend " a moment before Naomi bowed her head through the threshold. When her face rose again, she had the eyes of an astronaut taking the first step onto an uncharted planet."
    show GTS surprised with dissolve
    GTS "My, my..."
    Ryoko "There's no better time than the weekend to cut life's strings, I suppose."
    show GTS neutral
    Ryoko "{i}But...{/i}"
    Ryoko "Minori-chan, do you wanna head to the pharmacy while they look around here?"
    show Minori neutral at Transform(xzoom=-1)
    Minori "Oh, well, yes, that would be nice to get the boring stuff out of the way."
    Ryoko "{i}Très bon!{/i} Do you guys mind if we meet at the convenience store on Chōwakabamachi street when you're done here?"
    "I looked up at Naomi."
    GTS "That is well with me. See you both soon, then, and take care crossing the street."
    show Ryoko tongue
    Ryoko "Yes, mother dearest."
    hide Ryoko
    hide Minori
    with dissolve
    show GTS pondering
    GTS "Mother dearest?"
    MC "I think it was just some friendly ribbing."
    show GTS neutral
    GTS "I'm sure, it's just an odd thing for one to be seen as, especially by a friend."
    MC "Well... it's not that far-fetched. Remember what you said to me that one time Kodama-san was teaching you how to make cookies?"
    "She nodded, and let her voice fall a little softer."
    GTS "Only what I felt to be true and right."
    MC "Exactly."
    MC "Anyway, what are you looking for exactly?"
    GTS "Well, to be honest, I'm not entirely sure. I was hoping you could help me pick something."
    MC "Fair enough, I've got some experience under my belt. What console do you have? Pretendo? Ayystation?"
    GTS "Ah, I'm afraid there's a bit of a complication in that regard."
    MC "...Right, apologies, that's on me. Well, let's browse a little and see what catches your eye."
    show GTS happy
    GTS "Splendid!"
    show GTS neutral
    "I, her faithful guide, led her into the Pretendo section first and cleared my throat."
    MC "So these little ones are what's called 'handheld', the console for these is portable."
    GTS "I see... oh, that one looks interesting."
    "She daintily pinched the corner of one box depicting a pale, wide-eyed woman in a kimono, looking through a spiderweb. Naomi beheld the cover with an appreciative smile as I glanced at the title:{w} Onku: Fatal Siren."
    MC "I, uh, don’t think you would like that one."
    GTS "Oh, I see."
    "She gingerly put it back and bent down a little to scan the other games on display."
    GTS "This one has some enticing cover art as well. What do you make of it?"
    "I looked down and saw the cover’s depiction of a blue-haired girl... I think... standing in shallow water, a cardinal perched on her outstretched finger. ‘Chrysanthemum Tussle: Farewell, My Friend.’"
    MC "Oh, I think I heard of that."
    GTS "Do you think I would enjoy it?"
    MC "You... might? I can’t really comment, visual novels kinda put me to sleep."
    GTS "I see. Well, let’s try a different tack. What are some video games {i}you{/i} regard highly?"
    MC "Uh, me? Hm...{w} I play Silver Moon a lot. It’s pretty fun."
    GTS "What about it?"
    MC "The gameplay’s fun, and it does some interesting stuff with how you can use the characters’ abilities."
    MC "I used to play the two-player mode with Tomo-chan when we were tweens. So I guess you could say it’s all my fault."
    show GTS surprised
    GTS "Oh? How do you mean?"
    MC "She’s, uh... {w}how do I put this...{w} she prefers alternatives to sunlight."
    show GTS happy
    "A crackling chuckle escaped her."
    GTS "I’m sure your intentions were unimpeachable."
    MC "Ha, yeah."
    show GTS neutral
    MC "If I had to pick, like, my favorite game ever, I’d have to say... Magiria Knight 2."
    GTS "What is it about?"
    MC "So you play as this young kid with a magic sword, and he gets his arm cut off early in the story..."
    show GTS surprised
    GTS "Goodness!"
    MC "Yeah, and so he gets this robot arm instead, and you go through the game helping people fight this evil empire, and he gets more gadgets to put on his arm as you go along."
    show GTS neutral
    MC "It had a really good story, too. I won’t spoil it too much but there’s some really good subtle stuff as the story progresses, the characters are all really good, and the way the main guy’s character develops is really..."
    MC "..."
    stop music fadeout 1.5
    GTS "Really what?"
    "I smirked."
    MC "You don’t really want to try it yourself, do you?"
    play music GTS fadein 1.0
    show GTS surprised
    GTS "Oh... was it so obvious? I meant no offense..."
    MC "None taken. But you know, Yamazaki-san, you don’t have to go to all that trouble just to get to know me. Anything you want to know, {i}anything{/i}, all you have to do is ask."
    show GTS neutral
    GTS "That is good to know. But would you have answered as plainly or thoroughly as you did had I simply asked you?"
    MC "Of course I... uh... maybe?"
    "I stood in upended silence there in the Pretendo aisle, realizing I’d never much considered {i}why{/i} Naomi did things the way she did."
    MC "Uh... well... I guess you’re right."
    pause 0.75
    MC "Should we go meet back up with Tanaka-san and Tomoe-san?"
    GTS "Whatever you prefer, Hotsure-san."
    MC "What do {i}you{/i} prefer?"
    show GTS surprised
    GTS "What do... I?"
    GTS "Well..."
    show GTS happy
    GTS "I believe I would be most delighted if you continued with your review."
    show GTS neutral
    GTS "Perhaps some additional recommendations would be edifying as well... if you felt so inclined."
    "I smiled as I looked up at her, not knowing how she had just the words for every occasion. But I didn’t care anyway."
    MC "Well, where was I..."
    stop music fadeout 1.5
    scene black with fade
    $setTime(TimeEnum.EVE)
    pause 1
    scene Town with fade
    "Naomi shut out everything, it seemed, except what I was telling her. Eventually, I was the one who had to remind her that Ryoko and Minori would be waiting for us."
    show Ryoko neutral at Position(xcenter=0.8, yalign=1.0)
    show Minori neutral at Position(xcenter=0.2, yalign=1.0)
    show GTS neutral with dissolve
    play music Sunset fadein 1.0
    jump GTS028S_c3

label GTS028S_c3:
    #scene Convenience Store
    "After a short, winding walk under the flaming evening clouds, we came into the mellower, snow-white glow of the conbini's open storefront. A music of footsteps and beeps accompanied today's pop hits."
    "Clearly we weren't the only students to think to head here on a free evening, as we had to wait for one or two other groups to exit before going in ourselves; Naomi let another couple guys in before she at last ducked her head through."
    if getFlag("GTS028S_manga"):
        hide Minori with dissolve
        "Ryoko gently elbowed me in the ribs as Minori walked away, and then jabbed her thumb towards a case of beige seaweed packets."
        Ryoko "{size=-6}That's them.{/size}"
        MC "{size=-6}Thanks.{/size}"
        Ryoko "{size=-6}Alright, I'm gonna go fi-{/size}"
        show Ryoko happy
        extend " Yes! Melonpan!"
        hide Ryoko with dissolve
    else:
        Ryoko "Now, where do they keep the melonpan?"
        Minori "Perhaps I can help you find it."
        show Ryoko tongue
        Ryoko "Pfff. You can take a day off once in a while, Tomoe-san."
        show Ryoko neutral
        Ryoko "Let's split up, and you just find something you like, good?"
        "The two nodded briskly in tandem, and split off into separate aisles."
        hide Ryoko
        hide Minori
        with dissolve
    "And so, it was just me, and Naomi with her hands folded over her lap."
    "I looked up at Naomi; she blanketed me in a faint shadow as her head eclipsed the ceiling light directly above. In fact, it looked like she could've hopped and broke it."
    menu:
        "Would you like some mochi, Yamazaki-san?":
            jump GTS028S_c3a
        "Would you like some tea, Yamazaki-san?":
            jump GTS028S_c3a

label GTS028S_c3a:
    stop music fadeout 2.0
    GTS "Thank you for the offer, but I'm quite content."
    MC "Oh. What about something else, then?"
    GTS "No, thank you. As I said, desire is the very thing that proliferates suffering. My needs are fulfilled, and I am content."
    play music Memories
    GTS "Besides... "
    show GTS happy
    extend " what you've all given me today is much more a benefit to my soul than any food or drink in the world."
    MC "Y-yeah..."
    MC "I'd say the same to you."
    show GTS neutral
    GTS "Thank you."
    MC "You've really gotten stronger, you know. The more I get to know you, the more you amaze me."
    "Her head tilted and she looked to my side, blushing."
    MC "I hope you know that if you have to move, I'll make sure you never feel alone."
    "Her eyes, still waters, met mine."
    GTS "And I want you to remember that you can always come to me for a listening ear."
    MC "Thanks, Na- Yamazaki-san."
    "More languid beeping and a new old song filled in the silence."
    "I wanted to step forward and wrap my arms over the swell of her hips, press my face into her, and I didn't care if I was only just taller than her crotch. I just wanted to stay there a while."
    if getFlag("GTS028S_manga"):
        "But you know what they say about desire. Instead, smiling wide, I grabbed a couple packets of seaweed and went to look for my favorite canned matcha."
    else:
        "But you know what they say about desire. Instead, smiling wide, I went to look for my favorite canned matcha."
    "When we turned back, the other girls were lined up at the register, Ryoko strumming her fingers in a machine gun pattern."
    show Ryoko neutral at Position(xcenter=0.8, yalign=1.0)
    show Minori neutral at Position(xcenter=0.2, yalign=1.0)
    with dissolve
    Ryoko "Have we found everything we need?"
    "I nodded as I stepped up to the counter beside them."
    if getFlag("GTS028S_manga"):
        Minori "Oh? Do you like that brand of seaweed too, Hotsure-san?"
        MC "Well, I'm sure it's delicious. But I got it for you."
        show Minori with vpunch
        Minori "You got it... for me? How did you..."
        Minori "Ah. {w}All of you are too sweet, you know."
        Ryoko "Nothing to it."
        "By the time I turned to address the register, the cashier bobbed aside her dark brown pixie cut and repeated to me, in a pleasantly disinterested register,"
        Cashier "Your total today is 1701, please."
        if getFlag("GTS028S_pay"):
            MC "Sure thing, lemme just..."
            "I didn't even have to count, as I looked down into the graveyard of my gaping wallet, to tell I was short the funds."
            "I laughed, despite the rising throbbing in my neck."
            MC "Must've left some in my pocket, uh, maybe..."
        else:
            MCT "Oof, hurts just a little bit. Have to stop by the ATM later..."
    else:
        "Ryoko speedily transacted for both her and Minori's items amidst the pleasantly disinterested register of the cashier."
        "Sooner than I thought, it was my turn to step up; the cashier bobbed her pixie cut out of the way and gave a wan smile."
        Cashier "Your total today is 340, please."
        MC "Sure thing, lemme see here..."
    show GTS pondering
    GTS "Hold on. I believe I have something for this."
    "She opened up her purse and pawed around inside it for a moment or two."
    GTS "Oh, this confounded..."
    show GTS neutral
    "She shortly paused and lowered it down to my chest height."
    GTS "Erm, Hotsure-san, would you please grab that little green slip of paper in the middle?"
    MC "Certainly."
    "I fished it out to see the Kozaku-Mart logo emblazoned upon it, which I promptly presented."
    show GTS happy
    GTS "I have a rebate voucher, ma'am, if you please."
    Cashier "Looks like it. Lemme see..."
    show Ryoko happy
    Ryoko "Quick thinking, Yamazaki-san!"
    show Ryoko neutral
    show GTS neutral
    if getFlag("GTS028S_manga"):
        Cashier "Okay, that brings you to 500 for today."
        if getFlag("GTS028S_pay"):
            MCT "Holy shit, she's a lifesaver."
        "More than a little relieved, I handed over the cash and quickly shut away my frail, vulnerable wallet."
    else:
        Cashier "Okay, that brings your total to zero, and ma’am, you’ve got 900 left on this voucher."
        MC "Oh... wow, really? Sweet!"
        "I clapped my wallet shut and pocketed it, then passed the slip back to Naomi and took my tea."
    Cashier "Thanks guys, come back soon."
    MC "Thanks, you too!"
    show Ryoko happy
    show GTS happy
    show Minori neutral
    with vpunch
    "Everything Naomi did was so involuntarily grand and exaggerated now, I could tell without looking right at her that Naomi bit her lips for a second as we walked out of the store."
    "Funny enough, it made me feel a little better."
    scene black with fade
    pause 0.5

    scene Town with fade
    show Ryoko neutral at Position(xcenter=0.8, yalign=1.0)
    show Minori neutral at Position(xcenter=0.2, yalign=1.0)
    show GTS neutral
    with dissolve
    MC "Man, Yamazaki-san, you saved my bacon with that voucher. How'd you think to bring that?"
    show GTS happy
    GTS "It was nothing. A lady who means to keep her house in order must shun no financial advantage."
    "Just then, in the warm hues of a late summer afternoon, I felt just like I did out with my friends on Saturday nights in Shibuya. Of course, I never stopped to consider that until I laid down in bed that night."
    "I cracked open my tea can, and raised it to the heavens."
    MC "Well, here's to a successful outing!"
    show Ryoko tongue
    Ryoko "Hear, hear."
    Minori "Definitely."
    show Ryoko happy
    "Naomi, having nothing to raise, stepped back and bowed deeply."
    GTS "Thank you all dearly for having me. Whatever lies on our horizons, may our fellowship live on."
    MC "Heh, yeah."
    MCT "We've gotta do this again sometime."
    "Over our general accord, a silence settled slow and fluttering. Soon enough, we were back on our way to the bus stop."
    jump daymenu

label GTS028T:
    $setProgress("GTS", "GTS030")
    scene Movie Theater with fade
    play music Peaceful
    "I scanned the various posters that decorated the inside of the theater, wondering what might be good. Naomi leaned down slightly to get a closer look at the posters as well."
    show GTS neutral at Position(xcenter=0.8, yanchor=1.0) with dissolve
    GTS "I like the artwork used in some of these posters."
    MC "Yeah, I like it when the poster is more than just a character standing in the center with the title on them. "
    show GTS surprised
    GTS "Oh, this one reminds me of those ancient paintings you'd see in a museum."
    show Ryoko happy at Position(xcenter=0.4, yanchor=1.0) with dissolve
    Ryoko "That's Koichi: A battle of love and honor. It's a period piece. Also hey you two!"
    show Minori neutral at center with dissolve
    Minori "Good afternoon. I hope we didn't keep you two waiting long."
    "Naomi gave a small bow in greetings as Ryoko and Minori waved."
    MC "Not at all, we got here only a couple of minutes ago."
    show Ryoko neutral
    Ryoko "Great! I wasn't sure what you'd all like to watch so I picked a time that I knew would have a couple of movies starting in a relatively soonish time. So we could discuss what we want to see."
    MC "But what if we can't agree on any of the choices?"
    Ryoko "Well... then I didn't plan this out properly heh."
    Minori "As ill planned as that was, I'm sure we'll agree on one of the choices we have to choose from."
    MC "Alright, we do we have then?"
    Ryoko "We have The Last Call, a horror movie about patrons in a bar learning they're stuck in a bar with ghosts. There's Koichi, which is a period piece of a man fighting for his stolen love after being dishonored by the murder of his master."
    Ryoko "And then there's My Lover, My Sister!? A comedy which is about a guy who learns that the lady he's been dating is actually his sister in law."
    show GTS embarrassed
    GTS "I'm... not sure how I feel about those other two..."
    Ryoko "So those are our choices people, which would you like to see?"
    Minori "Hm, I could go for a fun comedy."
    GTS "I'm rather curious about Koichi."
    Ryoko "And I've been meaning to watch The Last Call. Well Hotsure-san, what's it gonna be?"
    MC "Great... Um..."
    menu:
        "I think a comedy is a safe choice since we don't know how the others will be.": # -1 Affection
            jump GTS028T_c1_1
        "Koichi sounds like it can be pretty cool. I haven't watched many ronin movies.": # +1 Affection
            jump GTS028T_c1_2
        "I'm not gonna lie, I'm interested to see how drunk people deal with a ghost.": # -2 Affection
            jump GTS028T_c1_3

label GTS028T_c1_1:
    $setFlag("GTS028T_c1_1")
    MC "I think a comedy is a safe choice since we don't know how the others will be."
    show Ryoko happy
    Ryoko "It's like my teacher always said, 'If you don't know what to watch, go with the jokes.'"
    $setAffection("GTS", -1)
    show GTS sad
    GTS "I hope it's not too vulgar..."
    Minori "Don't worry Yamazaki-san, I wouldn't pick something if I thought it'd bother anyone too much."
    jump GTS028T_c1_after

label GTS028T_c1_2:
    $setFlag("GTS028T_c1_2")
    MC "Koichi sounds like it can be pretty cool. I haven't watched many ronin movies."
    Ryoko "It's pretty great, I'm sure you'll enjoy it."
    GTS "You've already seen it Tanaka-san?"
    show Ryoko happy
    Ryoko "Of course! But don't worry I won't spoil anything."
    Minori "It's not uncommon for Tanaka-san to see a movie multiple times at the theater."
    Ryoko "Nope! Sometimes the second viewing is when you really get the whole story."
    GTS "Is that so?"
    Ryoko "Totally! Give it a shot some time. You may find you like a movie even more when you give it another watch."
    jump GTS028T_c1_after

label GTS028T_c1_3:
    $setFlag("GTS028T_c1_3")
    MC "I'm not gonna lie, I'm interested to see how drunk people deal with a ghost."
    show Ryoko happy
    Ryoko "It's sure to be pretty funny I think."
    show GTS sad
    GTS "..."
    Minori "What's the matter Yamazaki-san?"
    GTS "N-nothing..."
    Minori "Are you worried it might be too scary?"
    GTS "..."
    MC "Yamazaki-san, if you don't want to see it we can pick something else."
    $setAffection("GTS", -2)
    GTS "N-no... it's okay. I'll be okay..."
    MC "If you say so..."
    show Ryoko neutral
    Ryoko "Don't worry Yamazaki-san, it won't be too bad. I promise."
    jump GTS028T_c1_after

label GTS028T_c1_after:
    show Ryoko neutral
    Ryoko "Come on, let's go get the tickets."
    "Ryoko lead us to the box office where she ordered the appropriate tickets but we still had a little time to kill. We moved over to a small seating area where Naomi took a seat, which I couldn't help notice bought her at equal height to the rest of us."
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
    GTS "I-I'm sorry...?"
    MC "Don't worry Yamazaki-san, She's just playing it up. Though I can't say I've gone to many plays or musicals."
    Minori "Unfortunately I haven't as well."
    Ryoko "Yeah, I already spend enough on movies. Live shows are far too costly for me to support both."
    show GTS neutral
    GTS "I can see how that could be an issue. I wouldn't say we went often, but I think that's what made it a bit more special."
    GTS "Unlike movies which come out each week, live performances are rarer. My family made an event out of going to them. There's also something special about seeing a play."
    GTS "You know the actors have truly honed their craft for they have to be at top form every single night. Where I feel movies have it a bit easier since they get the benefit of multiple attempts and we only see the one take that was used."
    GTS "I wouldn't say movie actors have it easier, just that it's not the same I suppose."
    show GTS embarrassed
    GTS "Ah! I'm sorry."
    MC "Huh? Why?"
    GTS "That was incredibly rude of me. I wasn't attempting to demote the merits of films over plays. I hope I didn't offend you Tanaka-san and Tomoe-san. Apologies."
    show Ryoko happy
    Ryoko "Haha, no offense taken. It's just your opinion Yamazaki-san. No harm in sharing it."
    show Minori happy
    Minori "Indeed, and I would agree with your point. Stage actors truly go through the gauntlet for every single one of their performances. That's no small task."
    Ryoko "Yeah, don't sweat it Yamazaki-san. Oh! We forgot the snacks! Don't wait up for us, go get some seats!"
    hide Ryoko
    hide Minori
    with dissolve
    "Ryoko took Minori's hand and quickly vanished towards the concession stand as I chuckled and looked back at Naomi who seemed a little bothered."
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
    "Ryoko merely winked at me while Minori's smile widened. The two taking their snacks and wandering to a different section of the room. Leaving me and Naomi alone."
    scene black with fade
    if getFlag("GTS028T_c1_1"):
        "The movie started out rather surprisingly as a sex scene was the first scene to greet us. I felt Naomi tense up as it might have been a little much for her."
        "Still, once the scene pass and the movie continued she ended up relaxing and laughing quite a few times. I felt her hand move a couple of times as it seemed she was trying to muffle her laughing to not be rude."
        "However one time when her hand settled back down, it laid on top of mine."
        "Blushing lightly, I wasn't sure if I should mention it as her hand completely covered mine. Once I noticed her softly squeeze it, I finally looked up towards her and saw her smiling which in turn made my lips smile."
        "She laughed more openly as the film progressed and so did I, as I moved my hand so it could hold hers."
    elif getFlag("GTS028T_c1_2"):
        "The movie opened on a long lingering shot of a quiet field of flowers. Their colors muted as the sky itself was gray. The drama that would soon play out captivated us, as I could see Naomi lean closer to me as she got lost in the film."
        "She'd gasp when the action picked up, awe at set pieces, and when the ronin found his love she'd clutch my hand softly."
        "I was caught by surprise when she did that, looking up at her as she looked back down at me and smiled. My cheeks grew a little warm though, as while we looked at each other the ronin spoke all his loving feelings."
        "Sensing my nervousness, she ended up blushing as well and looked away, though her smile remained as did her hand for the remainder of the film."
    else:
        "The movie began innocently enough, a brief scene to establish all the characters and their reasons for drinking that night. There was minor tension and suspense the entire time though, yet nothing really happened for quite some time."
        "This seem to leave Naomi feeling a little more comfortable as it seemed it might not be too bad. But then just like that, the first major scare happened and Naomi let out a startled yelp."
        "The noise resulting in some others in the audience to snicker and laugh which resulted in her embarrassment. Her body remained tense the rest of the film as my chair shook a little from her shaking."
        "She was leaning back, as if providing distance would result in protection. Frowning, I gently placed my hand on her which made her flinch but then look down to see me."
        "I squeezed her hand to let her know I was there. And she squeezed back and held my hand for the rest of the movie, squeezing it whenever she was startled."
        "Granted... maybe that wasn't the best thing as I learned that with her added height, Naomi was stronger than normal too..."
    jump daymenu

label GTS029:
    $setProgress("GTS", "GTS030")
    scene Cafeteria with fade
    play music HigherEdu
    "I moved along the cafeteria line with the other students, and picked out a few food items, such as a bowl of beef teriyaki with rice, and some miso soup. I turned towards the tables and scanned the crowd."
    "It didn't take long to spot Naomi. Even sitting down I could spot the back of her head resting above everyone else's. I headed over to her table where she was currently sitting alone and took a seat."
    MC "Hey Yamazaki-san!"
    "Naomi glanced up at me, but then quickly glanced back down towards her meal, slowly picking at her bowl of rice with her chopsticks."
    show GTS sad with dissolve
    GTS "Oh, hello, Hotsure-San."
    MC "Is something the matter?"
    GTS "It's... nothing I'd want you to worry about."
    MC "It's no trouble at all, really. What's on your mind?"
    "I pushed my food tray to the side, giving her my undivided attention."
    GTS "It's just... I knew there would be some changes I'd have to get used to with my new height, but I suppose I wasn't prepared for everything."
    MC "How do you mean? It doesn't look like you're eating much more food than before."
    GTS "I... I found that my kimono no longer fits me this morning."
    MC "Oh. I see."
    "Naomi nodded softly, looking down to her tray of food before taking a bite. She chewed it quietly before responding again."
    GTS "It might sound silly, but it was my favorite one, and it saddens me that I won't be able to wear it anymore."
    menu:
        "Could you get a tailor to make it bigger?":
            jump GTS029_c1_1
        "Well, I think you look good no matter what you wear.":
            jump GTS029_c1_2
        "Hey, you can always get a new one, right?":
            jump GTS029_c1_3

label GTS029_c1_1:
    MC "Well, could you get a tailor to make it fit your new size?"
    "Naomi shakes her head, now poking her food with her chopsticks idly."
    GTS "While it would be possible, I don't believe it would do me much good. I can definitely afford it, but there's no telling how much taller I'm going to get. It would just be a waste of time."
    $setAffection("GTS", 1)
    show GTS neutral
    GTS "It was a good idea though, thank you."
    MC "Oh, I see. Well, could you just buy another, bigger one? Or get a really big one made for you once you stop growing?"
    show GTS sad
    GTS "I could, but that's only part of the problem."
    GTS "Not only was it my favorite one, but this kimono belonged to my great-great grandmother, and has been passed down along my family. There's a lot of history behind it, and that's not something that can be so easily replaced."
    MC "I'm sorry to hear that, Yamazaki-san. It sounds very important to you."
    show GTS neutral
    GTS "It is. My parents gave me it in preparation for my Maiko training."
    if getSkill("Art") > 35:
        MC "Oh, you were training to be a Geisha?"
        GTS "That's right. That was what my parents originally intended for me at least."
        MC "Did something change?"
        show GTS shy
        GTS "Yes, but I'd rather not get into that at the moment."
        MC "My apologies. I think you would've made a beautiful Geisha."
        $setAffection("GTS", 1)
        show GTS unique
        GTS "You're too kind, Hotsure-san."
        "She turned back to her food with a soft smile on her face, and I looked back to start eating mine. We continued to eat the rest of our lunch together, and took off for our next class."
    else:
        "I crinkle my nose, unsure of what that is."
        MC "I don't believe I've heard of a Maiko before."
        GTS "Oh, a Maiko is just a girl who's training to be Geisha. You have to learn dances, how to play songs, how to make tea properly, and other such things."
        MC "Ah, so that's why they're so important to you. You were training to be a Geisha, then?"
        "Naomi nodded, and looked over at me."
        GTS "Thank you for the talk, Hotsure-san. I'm not sure if I'm feeling particularly hungry right now. I'll see you later."
        "She picked up her tray of food, and I watched her walk away between the tables, her tall figure bobbing up and down away from me."
    jump daymenu

label GTS029_c1_2:
    MC "Well, I think you look good no matter what you wear."
    $setAffection("GTS", 2)
    show GTS unique
    GTS "T-Thank you Hotsure-San. Though I'm not sure if that helps my problem much."
    MC "Is there a reason this particular kimono was your favorite?"
    show GTS neutral
    GTS "Mhm. It belonged to my great-great grandmother, and has been passed down in my family line, before my parents gave it to me for my Maiko training."
    if getSkill("Art") > 35: #this is WAY too high
        MC "Oh, you were training to be a Geisha?"
        GTS "That's right. That was what my parents originally intended for me at least."
        MC "Did something change?"
        show GTS shy
        GTS "Yes, but I'd rather not get into that at the moment."
        MC "My apologies. I think you would've made a beautiful Geisha."
        $setAffection("GTS", 1)
        show GTS blush
        GTS "You're too kind, Hotsure-San."
        "She turned back to her food with a soft smile on her face, and I looked back to start eating mine. We talked more while we ate, before finally finishing our meals. We said our goodbyes, and she waved at me as we parted ways."
    else:
        "I crinkle my nose, unsure of what that is."
        MC "I don't believe I've heard of a Maiko before."
        show GTS neutral
        GTS "Oh, a Maiko is just a girl who's training to be Geisha. You have to learn dances, how to play songs, how to make tea properly, and other such things."
        MC "Ah, so that's why they're so important to you. You were training to be a Geisha, then?"
        "Naomi nodded, turning back to her food and I did the same. We continued to eat the rest of our lunch together, and once we finished, we said our goodbyes and parted ways."
    jump daymenu

label GTS029_c1_3:
    MC "Hey, you can always get a new one, right? It's just a kimono after all."
    $setAffection("GTS", -1)
    show GTS angry
    GTS "No! It was my great-great grandmother's kimono! It's not something that's so easily replaceable."
    "I froze for a second, turning back remorsefully as I tried to apologize."
    MC "I... I didn't know! I thought it was just something you got at a store!"
    show GTS sad
    GTS "No, no, it's alright. It just means a lot to me. My parents gave it to me in preparation for my Maiko training. I was going to be a Geisha."
    MC "Really? I had no idea you were going to be a Geisha! But wait, did something happen?"
    GTS "Yes, but... I'd rather not talk about it now."
    "Naomi picked up her tray, standing high above me."
    show GTS neutral
    GTS "I'm afraid I'm not feeling too hungry at the moment, so I'll take my leave. I'll see you later Hosture-San."
    "I merely watched her walk away, and pulled my tray back in front of me, picking at my food. I suppose I wasn't feeling particularly hungry at the moment either."
    jump daymenu

label GTS030:
    $setSize(3)
    $setTimeFlag("size3")
    $setProgress("GTS", "GTS031")
    scene Dorm Interior with fade
    "I awoke to my alarm reminding me to go over to Naomi's dorm to grab the notes from last week's lecture that I let her borrow."
    RM "Are you gonna turn that thing off, or do I have to?"
    MC "I got it, I'm up now."
    "Swinging myself out of bed, I got dressed and, after some basic grooming, made my way towards Naomi's dorm."

    scene School Inner with fade
    play music Schoolday
    "As I made my way towards Naomi's dorm, I noticed a board full of flyers for upcoming events. One of the flyers is for the local Children's Day Festival."
    MCT "I'll take one of these, maybe Naomi would like to go to this."
    "After grabbing a copy of the flyer and stuffing it in my pocket, I spotted Ryoko walking my way briskly. I stopped and bowed to greet her."
    MC "Morning, Ryoko."
    show Ryoko neutral with dissolve
    Ryoko "Oh, sweet, just the person I needed to find!"
    MC "Hm? What's up?"
    Ryoko "I was supposed to tell you, Yamazaki-san got moved to the giants' dorm the other day."
    MC "The giants' dorm, what do you mean?"
    Ryoko "You know that old pit mine just northeast of campus?"
    MC "Oh, that what that's used for? Seems a bit bleak to be a school facility."
    Ryoko "Well, that's what you can see."
    MC "You mean it's more than just a pit?"
    Ryoko "Yeah. You see, at the bottom of the pit is an entrance to these massive caverns. That's where they have their cafeteria and classrooms."
    MC "Oh, that's interesting. Still odd though, how big can these caverns be?"
    Ryoko "If I remember right, when I visited there with a friend the ceiling had to be like 25 to 30 meters tall. The place makes everyone feel small, but at least it means no one is outgrowing it any time soon."
    MC "Suppose so, better than having them stand outside or kneel beside the buildings to attend class."
    Ryoko "Before I get ahead of myself, she told me to give you this."
    "She handed me a sticky note with a four digit code on it."
    Ryoko "There's a fence around the place to prevent outside people from accidentally wandering in. Use this to get through the gate."
    MC "Do the giants have to use these?"
    Ryoko "Only the smaller ones. The larger ones can just step over the fence."
    MC "That makes sense, now that you mention it."
    MC "Thanks for this. I better go over and see how she's settling in."
    Ryoko "Tell her good luck from me."
    MC "I will."
    "I turned and, after consulting a map of the school, made my way towards the giant's dorms."

    scene Giant Dorm Exterior with fade
    "After following the directions Ryoko had given me, I found the chain-link fence gate with a large number pad mounted on it."
    "After punching in the code, I eventually made my way to the edge of a large, abandoned quarry. A wide road wound down the edge of the pit lined with weathered grey buildings."
    "From down the road, I can see Naomi waving at me."
    GTS "Hotsure-san!"
    show GTS neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    MC "Hey Naomi, Ryoko said you were moving into your new dorm."
    GTS "Indeed. I suppose that is simply the way of things with my growth."
    MC "This place is pretty big."
    show GTS unique
    GTS "Oh, you should see the rooms themselves."
    MC "Sure, lead the way."

    scene Giant Dorm Interior with fade
    "The exterior of the room was similar to an aircraft hangar, rather dull and plain-looking. The inside was very similar in appearance, with only basic furniture being provided."
    MC "Seems very utilitarian, don't you think?"
    show GTS neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    GTS "...Why yes, it certainly seems that way at face value, doesn't it... but, instead let us focus on the possibilities that it could be, hm? Maybe a nice baby blue wallpaper with some small rugs, that would be a good start."
    MC "How can you imagine those sorts of things with such a bland canvas, so to speak?"
    GTS "Well, each building can be thought of as a flower. Each one may be the same in looks and design, but each still has their own unique quirks and flaws."
    GTS "These dorms are the same way; they may be the same design, but none have aged the same. This gives them their own unique personalities."
    MCT "That is an incredibly deep way to put that idea, it sounds like a great idea for a proverb."
    menu:
        "Certainly seems like you enjoy this room.":
            jump GTS030_c1_1
        "How soon do you move in?":
            jump GTS030_c1_2

label GTS030_c1_1:
    GTS "I do, but I am a bit nervous about all this moving stuff."
    MC "How so? I thought you'd be quite happy to be in a more accommodating environment."
    hide GTS
    show GTS_S sad
    GTS_S "I am, I'm grateful for everything this academy is doing to accommodate for me, but I can't help but feel I'm becoming ever so slightly distant from everyone."
    MCT "Literally, yes..."
    MC "I'm still here, and we all still take the same classes. No one is going anywhere any time soon."
    hide GTS_S
    show GTS happy
    GTS "Thank you, Hotsure-san."
    GTS "That is really nice to know right now."
    $setAffection("GTS", 1)
    show GTS neutral
    GTS "I'm looking forward to seeing how my new situation will be like, now."
    jump GTS030_c1_after

label GTS030_c1_2:
    GTS "I should be moved in by tomorrow."
    MC "That's surprisingly fast, but it's good to know the school is quick to assist."
    GTS "I just hope it wasn't too much of a hassle."
    MC "I doubt it was, they probably do these adjustments all the time for students."
    GTS "You are probably right, I'd still hate to be a burden on their resources."
    jump GTS030_c1_after

label GTS030_c1_after:
    MC "Anyway, are you thinking you'll need some help moving in?"
    GTS "No, I can handle it just fine, it's not too much stuff."
    menu:
        "(Press her to accept your help)":
            jump GTS030_c2_1
        "(Let her handle herself)":
            jump GTS030_c2_2

label GTS030_c2_1:
    MC "I know you have a bunch of stuff in your dorm. You shouldn't have to move it alone."
    show GTS surprised at Position(xpos=0.5, xanchor=1.0, yalign=1.0) with dissolve
    GTS "No. I can handle this. It's my mess to worry about, not yours."
    MC "Yamazaki-san..."
    show GTS angry
    GTS "I won't have any more of it Keisuke, these are my things. So I should be the one to handle it."
    MC "Yamazaki-san, I insist, I don't want you hurting yourself by taking on more than you can handle."
    $setAffection("GTS", -1)
    GTS "*sigh* I can't be too mad if you are trying to look out for me, though I had hoped you might have a little more trust in me."
    MCT "I might've pressed too hard, better back off."
    MC "Sorry. I should probably be heading back. I have some math homework I need to complete before tomorrow."
    hide GTS
    show GTS_S sad
    GTS_S "Take care, Hotsure-san."
    "I quickly made my way out and back to the dorm. Today turned out in a way I wasn't expecting."
    jump daymenu

label GTS030_c2_2:
    MC "I trust you can handle yourself, Yamazaki-san. The stuff you have left should be of no problem to you at your current size."
    show GTS happy at Position(xpos=0.5, xanchor=1.0, yalign=1.0) with dissolve
    GTS "It shouldn't be a problem at all. I'd hate for you to waste your time with such a menial task."
    if getAffection("GTS") > 15: #FIXME
        $setFlag("GTS030_festival")
        MC "Oh, I nearly forgot, would you be interested in going to the Children's Day festival later this month?"
        GTS "Oh my, of course, that's a wonderful idea. It has been quite some time since I last partook in a festival."
        MC "I'm happy to hear that, I'll make sure to note it on my calendar."
        MC "It's getting late, so I better be departing. Take care, Yamazaki-san."
        "Naomi waves as I turn and head back to my dorm."
    else:
        MC "Then I wish you luck in your task. It's getting late, so I should be heading out."
        show GTS neutral
        GTS "Take care, Hotsure-san."
        "Naomi waved as I turned and headed back to my dorm, holding the flyer for the festival in my pocket."
        MCT "A later time would be better when she's not busy with moving."
    jump daymenu

label GTS031:
    scene Giant Dorm Interior with fade
    $setProgress("GTS", "GTS032")
    play music GTS
    "I headed over to the giants' dorm after class to check in on Naomi. I hoped that she had moved in well."
    "As I approached her dorm, I noticed her placing a flower box on the front porch."
    MC "That's a good way to add some color to this place."
    show GTS happy with dissolve
    GTS "Oh, Hotsure-san! I didn't even hear you approach. I'm glad you approve of the flowers. I had a feeling it was a good choice to brighten up this place."
    show GTS neutral
    GTS "Are you thirsty, by chance? I'm considering brewing a pot of tea for myself."
    MC "I could go for a cup. It’s been a while since I've had a cup of home-brewed tea."
    "She held open the door for me. I suppose she didn't want it to hit me on the way in."
    "The dorms inside had changed slightly since I'd visited yesterday. For one, there was some more furniture, like a couch, a table, some chairs, and nearly a full kitchen."
    "Though all the new additions had a similar utilitarian aesthetic as the rest of the dorm, it was good to see some of the space filled."
    MC "Did the school provide furniture and appliances?"
    GTS "Yes, they did. Early this morning, several trucks showed up and delivered all this stuff. I'm glad they did, as last night I was worrying where I'd get furniture my size."
    MC "Now you’ve got me curious. Where DOES Seichou get furniture this big?"
    GTS "One of the other students here mentioned there's a shop away from town disguised as a hill."
    GTS "I believe they said it was called Mt. Fuji Outfitters. It's run by a former student, like many of the other shops around town. They mainly sell clothes, which is pretty good to know since mine are starting to get a bit tight."
    MC "I’m glad that the island and the school have ways to provide for everyone. Now all we need is a place that makes wigs, and I'll be their first customer."
    "Naomi chuckled as she began prepping a pot of tea on the stove."
    MC "I hope that moving your stuff from your old dorm wasn't too hard."
    "Naomi's expression sank a little at the question."
    hide GTS
    show GTS_S sad
    GTS_S "Yes, it was quite easy to move everything over. However, I realized something while I was doing it."
    "She grabbed two moderately-sized boxes off of the nearby tabletop and placed them in front of me."
    GTS_S "I can’t wear any of the clothing that I brought with me anymore. None of my clothes fit, and all of my school supplies don't fit my hands. None of this is usable."
    "She paused for a moment before shaking her head and turning her mood around."
    hide GTS_S
    show GTS neutral
    "Although she was clearly feeling unwell, Naomi seemed to be able to collect herself almost immediately. With a deep breath, she slowly returned to her original position."
    GTS "Well, it's best to not dwell on what has been lost. If you find anything in here that you can use, you can keep it. Otherwise, I'm gonna donate them."
    "I opened one of the boxes, finding some mugs and silverware resting atop what I assumed was her wardrobe."
    MC "You know, you could probably keep some of these things for visitors. You can't use them, but whenever you have company, they can use the dishes and silverware."
    show GTS happy
    GTS "That is a good point. I'm glad you thought of that. I was so caught up in getting myself settled, I hadn't stopped to consider future guests."
    MC "I’m glad I could help you with that. I hope you weren't concerning yourself with the idea of having guests so soon after moving in."
    show GTS neutral
    GTS "Well, it would be rude of me to not think of others visiting my dorm."
    MC "Yes, but so soon after moving?  That seems a bit weird. I didn't even consider guests coming to my dorm until maybe three days after settling in."
    GTS "It's just good etiquette to always be mindful of guests if they ever enter your home. Not being prepared for guests would show a host who is inconsiderate of others."
    MC "I'm just saying, you should look out for yourself sometimes. Once you have yourself settled, then you accommodate others."
    "Naomi stopped like she's trying to formulate a proper response, but before she could respond the teapot began to whistle. Taking the pot, she carefully poured me a cup of hot water before pouring herself one."
    "She offered me a teabag, which I accepted before she dumped 4 bags total into her cup."
    MC "Won't that be extremely strong? Four bags seems a little excessive."
    GTS "With this much water, it balances out. You have to remember, your mug is roughly one pint, while mine is about one liter. I'm glad one of the graduating students was kind enough to donate these oversized cups and teapot."
    MC "Well, it's good to hear that the other students here are very welcoming. I guess when there are only a few of you, everyone is a neighbor."
    show GTS happy
    GTS "It is extremely pleasant to be welcomed with open arms. It's like we are one big family..."
    "She stopped for a moment before shaking her head again."
    GTS "I can't complain about anything so far. It’s very nice here."
    MCT "She's not admitting something but I'd hate to ruin her mood by digging into it."
    MC "I'm happy to hear that. I'm sure Ryoko will be happy to hear that you’re doing well."
    show GTS neutral
    GTS "If you could tell her, I'd appreciate it. I'd hate for her to be worrying about me."
    MC "Did you speak to her when you went back to the dorm?"
    hide GTS
    show GTS_S sad
    GTS_S "No, she was out filming, I suppose. Either that, or hanging with her friends from the film club."
    MC "Well then, I will make sure to speak with her since you asked so nicely."
    hide GTS_S
    show GTS neutral
    GTS "Only do it if it isn’t a bother, please. Otherwise, I'm sure I can find time to do it myself."
    MC "It's fine Yamazaki-san, it's a simple favor. Plus I occasionally pass her between classes, so more than likely I will see her tomorrow."

    if not getFlag("GTS030_festival"):
        $setFlag("GTS030_festival")
        MC "Oh, and before I forget, I meant to ask you something yesterday."
        "I pulled out the Children's Day flyer from my pocket and handed it to her."
        GTS "Oh, the Children's Day festival, I haven't been to a festival in a long time."
        MC "Would you like to go with me?"
        show GTS happy-2
        GTS "Really?! I'd love to!"
        show GTS neutral
        GTS "I mean if you are available to go as well, then it would be perfect."
        MC "Of course I can, I just wanted to ask you since I was planning on making it a date."
        show GTS embarrassed
        GTS "Oh, Hotsure-san. That's a wonderful idea. I'll need to figure out something to wear for such an occasion but I would love to go with you."
        MC "Then I look forward to our night out together."
    "Naomi sips her tea with a face of displeasure, before adding some more water."
    MC "Is the tea a bit too strong?"
    show GTS neutral
    GTS "Unfortunately. I need to work on estimating how many packets I need."
    MC "You know, that brings up a good question. Where do you get food? You can't go to the normal cafeteria anymore."
    GTS "Oh, this will be fun to explain. You see, at the bottom of the pit is the entrance to a place simply called The Caverns. It's like a second school down there, complete with classrooms, some club rooms, and a cafeteria."
    GTS "Maybe sometime during the school day you can come down and see it. It truly is a marvel of engineering."
    MC "Do you take separate classes, or how do classes work?"
    GTS "The way it works is that every classroom has a camera that is connected to a projector. That projector then displays the class in real time to us in our lecture hall."
    GTS "Class participation, unfortunately, doesn't work. We’re still required to submit our homework on time."
    MC "How does that work? I can't recall seeing giant sheets of paper on Tashi's desk before."
    GTS "One of the students here works as a teacher's assistant. They handle all the homework grading and just pass the results to the correct teacher for entry into the system."
    GTS "Even with all that, do you want to know what the craziest thing about The Caverns is?"
    show GTS happy-2
    GTS "Being inside there makes me feel normal. It's hard to describe, but inside there, the ceiling is nearly 30 meters tall. Everything feels so natural and safe. I don't have to hunch over, or squeeze through doors. I'm free again."
    "I could see some tears forming in her eyes as she said those last words until she wiped them away. She took a moment to recompose herself before continuing."
    show GTS neutral
    GTS "Sorry about that. The tea is still quite strong, so it made me tear up."
    MC "You don’t need to apologize. I was interested in all of it. The giants' area isn't an area many students get to see often, so hearing how it operates is quite fascinating."
    GTS "I'm glad you enjoyed my rambling there, I was afraid I got lost there for a moment in my own world."
    "She pauses again staring into her tea for a moment before sipping it."
    hide GTS
    show GTS_S sad
    GTS_S "Do you like me, Hotsure-san?"
    MC "Of course I do, Yamazaki-san. I wouldn't have shared a kiss with you if I didn't."
    GTS_S "Why me, though? There are plenty of normal-sized people at school, yet you chose me."
    MC "Well, you are incredibly kind to everyone you meet. Your knowledge of gardening and plants is beyond compare. I suppose you've never given me a moment to doubt that you are an amazing person."
    MC "That's why I've stuck with you, regardless of whatever problems you believe it’ll cause."
    hide GTS_S
    show GTS embarrassed
    GTS "Thank you, Hotsure-san. I'm not sure why, but I feel like I really needed to hear something like that."
    MC "Any time, Yamazaki-san."
    "Naomi wiped a tear from her eye before finishing her tea."
    show GTS neutral
    GTS "It's getting late, shouldn't you be returning to the main campus?"
    MC "That's probably a good idea, I know Matsumoto-san doesn't patrol this area but I'd hate to encounter her once I return."
    show GTS aroused
    GTS "Would you like me to walk back with you?"
    menu:
        "Yes":
            jump GTS031_c1_1
        "No":
            jump GTS031_c1_2

label GTS031_c1_1:
    MC "Yes, I would love for you to walk back with me."
    scene black with fade
    pause 1
    $setTime(TimeEnum.NIGHT)
    scene Giant Dorm Exterior with fade
    $setAffection("GTS", 1)
    "Naomi blushed as she stood up to walk with me. Once outside, I looked up and realized how nice the stars are here."
    MC "The sky looks amazing from here."
    show GTS neutral
    GTS "My first night here, I laid down at the bottom of the pit staring into the sky. The view was beyond amazing, you can watch the stars travel across the heavens without even moving. Nothing I've seen so far can compare."
    MC "Perhaps I could join you next time? You’ve confirmed that this is an experience I can't miss."
    show GTS aroused
    GTS "Just tell me when it works for you, and I'll make it happen. Not only that, but I have a few ideas on how it can be made even better."
    "We both ended up chuckling as we headed back to campus."
    jump daymenu

label GTS031_c1_2:
    MC "No, I think I'm good to go back alone. You might raise some suspicion with Matsumoto-san, and then she'll yell at both of us."
    show GTS neutral
    GTS "You certainly aren't wrong with that assumption. She would probably do exactly that. Do take care, Hotsure-san."
    "I waved back to her as I exited the dorm and began my trek back to the school."
    jump daymenu

label GTS032:
    $setProgress("GTS", "GTS034")
    scene Dorm Interior with fade
    play music Busy
    "The sunlight poured in through the window as another day began. My alarm miraculously went off, and I began my daily routine on schedule."
    "I brushed my hair into a semi-presentable style before I dressed myself, walking out of the bathroom to see Daichi typing away at his computer."
    "His shoulders were squared and firmly locked into position, defensively blocking the screen as he leaned closer to the monitor."
    MC "Make sure you use incognito mode. You never know who might be watching."
    show RM neutral with dissolve
    "While keeping his chest pointed towards the screen, he turned to look over his shoulder to send me a brief dismissive glance, before returning to the computer."
    RM "I generate random passwords for every single device, website, and account that I use. Do you really think that I'd be the kind of person who wouldn't remember to browse the internet discreetly, ESPECIALLY when you consider what I'll uncover at this school?"
    MC "So you're telling me that you DON'T enable cookies."
    show RM angry
    RM "Enough."
    MC "What the hell {i}do{/i} they mean by 'cookies,' anyway..."
    show RM neutral
    RM "Don't you have a class to attend?"
    MC "Don't you?"
    RM "...."
    MC "...."
    "I made my way out of the dorm to make sure the intense, passive-aggressive energy within the room didn't cause it to implode."

    scene School Inner with fade
    "The hallways leading up to the classrooms felt as empty as they always have. The building was meant to accommodate people at least double the size of any human."
    "This made sure everything was spacious and open, to allow free movement for nearly anyone with a factor. {i}Nearly{/i} anyone."
    "Despite having taken this route dozens of times by now, I had a lingering feeling that something was different about today."
    "Unconsciously, I knew what it was, but my mind was already on auto-pilot for the morning. All I could focus on was walking the usual hallways to class."

    scene Classroom with fade
    play music Rain
    "I took my usual seat in the center of the room as the students filtered in. By the time class had officially begun, we had all settled into our seats."
    "That was when the reality set in about what would be different about today. Naomi wasn't anywhere to be found."
    show BE neutral at Position(xpos=0.65) with dissolve
    "As if on cue, Honoka was first to address her absence. Because of the distance between each of the desks, simply whispering or passing notes wasn't an option."
    "Class had officially begun, but Tashi-sensei was still at his desk. His eyes were scanning over his lesson plan folder, silently pondering to himself what to cover today."
    BE "Hey, has anyone seen Naomi?"
    "Her voice broke the silence in the room, which then immediately fell silent once more. The air in the classroom froze. The punctuating tick of the clock was the only audible sound for several seconds."
    show HR neutral at Position(xpos=0.15) with dissolve
    "Tashi-sensei stood up from his desk at the corner of the room with a firm, confident look in his eyes, as if about to say something. I decided to address the lingering question before he began the lesson."
    MC "I... helped Yamazaki-san move out over the weekend. She's been transferred to the giant dorm."
    show FMG surprised at Position(xpos=0.30)
    show WG surprised at Position(xpos=0.45)
    show PRG surprised at Position(xpos=0.60)
    show BE surprised at Position(xpos=0.70)
    show AE neutral at Position(xpos=0.85)
    with dissolve
    "Mixed expressions of surprise, relief, and intrigue filled the room as I answered Honoka's question. Tashi-sensei seemed to be the only one that didn't visibly react at all."
    HR "Ah, so that's what's happened, then. I'm certain that they'll have an appropriate lesson plan for her."
    MC "You don't exactly sound surprised, Tashi-sensei."
    HR "I was informed ahead of time that Yamazaki-san's condition would mean that she wouldn't be staying with us. Since it all depended on her growth rate, no exact date was given."
    hide FMG
    hide WG
    hide PRG
    hide BE
    with dissolve

    AE "Is there any specific height threshold where the transfer is made?"
    HR "The medical staff make the call as soon as a student begins brushing the ceiling. Even with our custom-built amenities, this campus is only equipped to deal with heights of 300cm and below. Beyond that, it becomes far too inconvenient to move around."
    AE "...I see. That's the cutoff point, then."
    HR "More or less. I've seen students come and go many times before, often for that very reason. It's best to transfer them right away, to avoid any potential property damage."
    hide AE with dissolve
    show FMG sad with dissolve
    FMG "Does that mean Naomi's never coming back?"
    hide FMG with dissolve
    HR "While there aren't any rules explicitly stating that she CANNOT ever enter the building again, it's extremely ill-advised for her to try."
    HR "Naomi is still free to walk around the outdoor areas of campus however she pleases, as long as she avoids property damage."
    show BE happy with dissolve
    BE "Well hey, that doesn't sound bad at all! She could even peek in through the window!"
    hide BE with dissolve
    show HR neutral with dissolve
    HR "Our class will be livestreamed to her via video call. She won't miss anything, and you'll still be able to talk to her outside of class."
    "A heavy sense of relief circulated throughout the rest of the room. I slowly saw the faces of all of my classmates return to their usual, collected selves."
    "It seemed that this wouldn't be as big of an adjustment as we had initially thought. Naomi wasn't even moving very far; she'd still be mere meters away, talking to us in a video call."
    show HR neutral with dissolve
    HR "If there are no further questions, I'd like to begin today's lesson plan."
    "Those who had left their seats returned to them as Tashi-sensei returned to the board. Despite the expanded bodies of my classmates, the room still felt spacious and empty without Naomi. Even so, my classes proceeded as usual."
    "After saying my goodbyes and packing up for the day, I knew where I'd be heading next."

    scene Giant Dorm Exterior with fade
    "Before long, I had found myself at the door to Naomi's room. Once again, I found myself at the front of an aircraft hangar, painted only with very basic colors and numerical labels."
    "It was still rather foreign to me how it looked more like a military base with all of the repurposed hangars lined up in a row."
    "I could tell that the architects at least made SOME effort to make the place look 'homey,' though. The lighting rigs adorning the tops of the doors bathed the area in white light, which illuminated all of the walking space."
    "I checked the plate upon the shutter door to make sure it was the right room before I gave it a knock. The metal surface clanged under my knuckles, rattling for a few seconds before going silent. A familiar voice greeted my arrival."
    GTS "Ah... who is it?"
    MC "It's Kei."
    "I could hear a heavy, relieved exhale coming from the other side of the shutter."
    GTS "Hello, Kei-chan. Please, come in."
    "I heard a tiny click coming from the side of the hangar as the massive door reeled itself open, the titanic slab of metal swinging on its hinges as it revealed the room inside."

    scene Giant Dorm Interior with fade
    "Naomi stood on the other side, folding her arms and greeting me with a shallow bow."
    show GTS neutral with dissolve
    GTS "I'm very glad you could make it."
    MC "How have you been since I saw you last?"
    hide GTS
    show GTS_S sad
    "As I walked past the hangar doors and into Naomi's makeshift dorm, I could see her face visibly cloud up. She had been presenting a cool, collected smile to me as the metal plates were opening, but as soon as we were inside, she just... shifted."
    "Her entire body sunk as she kneeled onto the floor, keeping her torso straight."
    "She turned her foggy, lost expression towards me and slowly spoke."
    GTS_S "Adjusting has been challenging, but it's nothing that I've been unable to manage. I thought that I had everything figured out in my head. I had a plan, you helped me with it, and there wasn't a single doubt in my mind mere hours ago."
    GTS_S "As I settled in, however..."
    "Naomi exhaled once more as she gathered her thoughts, pausing for a few seconds."
    GTS_S "...You can feel that you have everything figured out on paper, or in your head, and yet when it comes time to actually make the necessary adjustments, reality hits. You finally understand that you aren't just imagining the scenario..."
    GTS_S "You're in it."
    "I kneeled upon the floor, opposite Naomi as she spoke."
    MC "It's frustrating when the reality is nothing like how you pictured it in your head. When you notice your new surroundings and you're still mentally adjusting, it's never easy. I take it your first day could have gone better, then?"
    GTS_S "Nothing specific really {i}happened{/i}, I'd say. The medical staff and faculty walked me through my new routine, where I'd be eating, how I'd keep up with my classes, stuff like that. It's nothing {i}horrible{/i}; it's just different."
    MC "How's the food?"
    GTS_S "The selection is less diverse than the other campus, but it's still palatable. They serve it to you with much larger portions offered. I imagine they need to use surplus crates to provide that much food."
    GTS_S "A lot of the entrees appear to be heavy in protein and fat, so we stay fuller longer."
    hide GTS_S
    show GTS happy
    "I could see Naomi's usual happiness return as the hangar lights buzzed quietly above our heads. Having company set her mind at ease; seeing a familiar face definitely helped."
    MC "It can't be easy keeping students that big fed. Surplus crates and bulk food palettes were the only option. Not to mention the amount of space you'd need just to {i}seat{/i} all of them."
    show GTS neutral
    GTS "The caverns are built to allow for freedom of movement. The cafeteria is carved out to be the size of a quarry, so there's never a shortage of seating space. The same goes for the auditorium."
    MC "Tashi-sensei said that you'd get a livestream of our class. Is that true?"
    "Naomi responded with a small, shallow nod as she looked at me."
    GTS "I'll be watching his lectures on the giant screen in the auditorium. It's about the size of a movie theater, so the audio can be rather overwhelming if one isn't adjusted to the volume. I'm certain that I'll get used to it."
    MC "They really {i}did{/i} think of everything when they created this section, didn't they? A theater screen would feel just like you're watching TV."
    GTS "How have you been, yourself? I've yet to ask how your day went."
    menu:
        "It was about the same.":
            GTS "I'm very glad that my move was seamless. The last thing I'd want is to cause a disruption."
        "It felt lonely without you.":
            show GTS embarrassed
            GTS "Oh, I'm certain it wasn't that bad. You'd hardly notice that I'd be gone."
            $setAffection("GTS", 1)
            MC "Well, of course it'd be lonely. We value your company. It's just not the same if we see you over a stream."
            show GTS aroused
            GTS "The importance of remembering those close to you is a value that often goes unnoticed. I'm flattered that you were thinking about me."
            show GTS neutral
        "The others were asking about you.":
            GTS "I... I see. What, exactly, was said about me? Have I caused them to worry?"
            MC "I wouldn't say 'worried,' no. They were just... asking about you. Wondering where you were."
            GTS "Did you tell them that I moved without any issues?"
            MC "I'd say so, yeah. They would have found out either way. Might as well have heard it from me."
            GTS "...I'm glad. I don't want our classmates going uninformed. Though some, I'd prefer to stay away from."
    MC "Other than that, is it... livable, at least?"
    GTS "It'll do, Kei-chan. I have little choice in where I stay."
    MC "That doesn't mean you should settle for a bad living space."
    GTS "Having someone like you visit will put my spirits at ease, Kei-chan. Perhaps with further adjustments, this hangar can genuinely feel like a home. I'll begin preparing a new garden tomorrow morning."
    MC "Already getting back to routine, huh?"
    show GTS happy
    GTS "The best way to work towards one's goals is to develop good habits and develop the discipline to maintain them. The sooner I can get back to finding my schedule, the sooner I can continue improving myself."
    MC "I can agree with that. Hell, the only reason I'm still able to see is because I have the discipline to actually wash and comb this haystack I call 'hair.'"
    "Naomi giggled, keeping her hand close to her mouth to keep it covered."
    GTS "Hygiene is important, of course, but I meant your drive. What motivates you, Kei-chan? What would you consider to be your greatest strength?"
    if getSkill("Art") > getSkill("Athletics"):
        if getSkill("Art") > getSkill("Academics"):
            if getSkill("Art") >= 7:
                $setAffection("GTS", 1)
            jump GTS032_art
        elif getSkill("Art") == getSkill("Academics"):
            if getSkill("Art") >= 7:
                $setAffection("GTS", 1)
            menu:
                "My artistic prowess.":
                    jump GTS032_art
                "My supreme intellect.":
                    jump GTS032_academics
        else:
            if getSkill("Academics") >= 7:
                $setAffection("GTS", 1)
            jump GTS032_academics
    elif getSkill("Art") == getSkill("Athletics"):
        if getSkill("Art") == getSkill("Academics"):
            if getSkill("Art") >= 7:
                $setAffection("GTS", 1)
            menu:
                "My artistic prowess.":
                    jump GTS032_art
                "My supreme intellect.":
                    jump GTS032_academics
                "My athletic pursuits.":
                    jump GTS032_athletics
        elif getSkill("Art") > getSkill("Academics"):
            if getSkill("Art") >= 7:
                $setAffection("GTS", 1)
            menu:
                "My artistic prowess.":
                    jump GTS032_art
                "My athletic pursuits.":
                    jump GTS032_athletics
        else:
            if getSkill("Academics") >= 7:
                $setAffection("GTS", 1)
            jump GTS032_academics
    else:
        if getSkill("Athletics") == getSkill("Academics"):
            if getSkill("Athletics") >= 7:
                $setAffection("GTS", 1)
            menu:
                "My supreme intellect.":
                    jump GTS032_academics
                "My athletic pursuits.":
                    jump GTS032_athletics
        elif getSkill("Athletics") > getSkill("Academics"):
            if getSkill("Athletics") >= 7:
                $setAffection("GTS", 1)
            jump GTS032_athletics
        else:
            if getSkill("Academics") >= 7:
                $setAffection("GTS", 1)
            jump GTS032_academics

label GTS032_athletics:
    MC "My physical fitness, and the dedication I have to keeping my body healthy."
    GTS "You've been hanging out with Mizutani-san, then?"
    show GTS happy
    if isEventCleared("FMG030"):
        MC "I've been working with her all the time since the school year began."
    elif isEventCleared("FMG020"):
        MC "Yes, I occasionally work out with Mizutani-san. She's very helpful."
    elif isEventCleared("FMG010"):
        MC "Hey, she has {i}nothing{/i} to do with my desire to look good! Though, yes, I'll admit that we've been hanging out."
    else:
        MC "Not much, but she's definitely a good example."
    GTS "Regardless, there's absolutely nothing wrong with caring for your body. When you're physically healthy, you can achieve everything else you desire so much more easily."
    jump GTS032_after

label GTS032_academics:
    MC "The dedication I have to my studies, and my constant desire to learn new things."
    GTS "I'm glad that you're so dedicated to your academics, Kei-chan. You've got the makings of a model student. When your mind has been exposed to so many different topics, you can make an informed decision on any problem life may throw at you."
    jump GTS032_after

label GTS032_art:
    MC "My ability to see the world through a different lens, and turn my imagination into reality."
    GTS "I'm happy that you allow your imagination to motivate you, Kei-chan. When our thoughts are too deeply focused on reality, we forget the possibilities open to us in our futures."
    GTS "We... let our minds become locked. We believe that 'this is our reality, and nothing can be done to change it.'"
    jump GTS032_after

label GTS032_after:
    GTS "Just don't forget to give yourself some 'me' time every now and then. Discipline and drive can only get us so far, Kei-chan. We need happiness, enjoyment, and leisure time just as much as our goals."
    MC "I'm giving myself 'me' time right now!"
    show GTS surprised
    GTS "Simply talking to me is your idea of personal time?"
    MC "Yeah. Hanging out with you is way more exciting than anything else I might have had planned."
    show GTS happy
    GTS "I am thankful that you made that decision, Kei-chan. The happiness you bring me is far more valuable than anything material."
    MC "I'm glad to have been here, Yamazaki-san."

    scene Giant Dorm Exterior with fade
    "After I left Naomi's dorm for the evening, I saw her expression brighten. Seeing her relax just by talking to me raised my hopes that she'd be able to move into her new life without trouble."
    "Naomi had always been the mature one of the group, and if anyone could mentally collect herself after such a dramatic shift in scenery, it'd be her."
    jump daymenu

label GTS034:
    $setTime(TimeEnum.EVE)
    $setProgress("GTS", "GTS035")
    scene Campus Center with fade
    play music GTS
    "I checked my phone once more to make sure I was headed to the right place."
    MCT "The campus plaza, yeah that's where she wants me to go. Not sure why she couldn't tell me why she needed me to come."
    "As I approached, I noticed Naomi slowly pacing near the tree."
    MC "Hey Yamazaki-san! You wanted to see me?"
    show GTS happy-2 with dissolve
    GTS "Oh, good afternoon, Hotsure-san. I hope you're doing well today."
    MC "Yeah I'm alright. What's up?"
    show GTS happy
    GTS "I was just thinking of my plans for the weekend. I wanted to make sure I had all my things in order."
    "She stepped over towards her garden and began inspecting the various flowers."
    MC "You gonna leave me in the dark? What are you exactly planning?"
    show GTS embarrassed
    GTS "Well, would you like to spend time with me this weekend?"
    MC "Of course I would, what did you have in mind?"
    GTS "{i}{size=-6}A dinner with my parents.{/size}{/i}"
    MC "Sorry, I didn't quite catch that."
    GTS "A dinner with my parents."
    MC "Wait, y-your parents?! Isn't this a little sudden?"
    show GTS neutral
    GTS "Apologies for springing it on you like this, but my parents insisted I ask you."
    MC "Hold on, your parents know about me? Do they know about us?"
    "She gently nods as I can feel my palms growing rather sweaty."
    MC "Uh... okay. That's a bit to take in so quickly."
    menu:
        "(Decline her)" if not getFlag("GTS034_c1_1"):
            jump GTS034_c1_1
        "Are you sure about this?":
            jump GTS034_c1_2
        "I suppose it is about time.":
            jump GTS034_c1_3

label GTS034_c1_1:
    $setProgress("GTS", "GTS034")
    $setFlag("GTS034_c1_1")
    MC "I'm sorry Yamazaki-san, but I can't, not on such short notice. I'm not even sure if we've been together long enough for this."
    hide GTS
    show GTS_S sad
    GTS_S "I understand, I suppose I got a little ahead of myself and didn't account for how you might feel in this. My apologies."
    MC "Maybe a later time would be better. I just feel like it's a little soon to be making those introductions."
    hide GTS_S
    show GTS neutral
    GTS "I understand completely, Hotsure-san. Hopefully they return at some point and you can meet them then."
    MC "That sounds like a great plan. Let's do that when the time is better."
    jump daymenu

label GTS034_c1_2:
    $setFlag("GTS034_c1_2")
    MC "You sure about me meeting them? This is the first time you'll be seeing them since coming here. Wouldn't it be better for them to acclimate to the changes first?"
    $setAffection("GTS", -1)
    #show GTS nervous
    hide GTS
    show GTS_S sad
    GTS_S "You think they'll be scared of me?"
    MC "No, I just think it's best to address two large topics separately. That way they have room to digest both things without being bombarded."
    "Naomi looked incredibly panicked for a moment before shaking her head and returning to her normal composure."
    hide GTS_S
    show GTS neutral
    GTS "You are probably right, I've never had a boyfriend before so I'm pretty sure that alone is enough to overwhelm them. They are my parents after all, so I know they will be looking for something to worry about."
    GTS "Maybe once they have seen me I can then bring you in."
    MC "That's a good idea, I still want to meet them. Just maybe one surprise at a time for them."
    jump daymenu

label GTS034_c1_3:
    $setFlag("GTS034_c1_3")
    MCT "I suppose it is about time I meet them."
    MC "...Okay. Dinner with your parents? I can do that."
    show GTS happy-2
    GTS "Are you sure, Hotsure-san? It's okay if you'd rather not. I won't be mad, as it is my fault for not informing you sooner."
    MC "No it's okay, I don't mind meeting your parents. Is there anything I need to know before I meet them?"
    "Naomi gives me a smile, part pure happiness, part uncertainty."
    show GTS neutral
    GTS "Yes, quite a bit."
    MC "Alright, what do I need to learn?"
    GTS "Table etiquette, proper attire, manners, a couple more things that are mostly for formality."
    MCT "Oh boy I've got a lot to do."
    GTS "Please don't take that list the wrong way, Hotsure-san. I just want to make sure that you're fully prepared for when you meet my father. Would it be okay if we went over a few things?"
    MC "If it's to prove to your parents I'm right for you, then I can do it. So, when should we start?"
    "Naomi's eyes tear up a bit but she quickly wipes them away."
    show GTS happy
    GTS "We can start tonight if you want. But before that, can I ask you a favor?"
    MC "Sure, what do you need me to do?"
    "She pulls out an envelope with Alice's name written on it."
    show GTS neutral
    GTS "If you could, I need this delivered to Miss Nikumaru."
    MC "Is there a reason you need me to deliver it? Wouldn't giving it to Aida make more sense since you see her nearly every day?"
    GTS "Beyond the physical limitations, I'm not very keen on Miss Nikumaru so I'd like to keep my distance. As for me not giving it to Aida, I just didn't want to bother her. She already has to worry about enough."
    MCT "Is she still mad about that one fight they had a couple of weeks ago?"
    MC "Alright I'll take it over now and then head back to your dorm so we can begin my training."
    show GTS happy
    GTS "Thank you for doing this for me. I'll see you soon."
    "I turned and headed towards Alice's dorm."

    scene Dorm Exterior with fade
    "As I approached the dorm, I spotted Alice stepping out the door."
    MC "Nikumaru-san, do you have a moment?"
    show WG neutral with dissolve
    WG "Hello Hotsure-san. What do you need?"
    "I passed her the letter, which she plucked from my hands and began to read."
    WG "Hmph. Well, you can tell her that I can fulfill her request, though if she wants to discuss payment she'll need to talk to me in person."
    MC "I will tell her, thank you Nikumaru-san."
    "She nodded and headed off to wherever she was heading. I made my way back to Naomi's dorm."

    scene Giant Dorm Interior with fade
    "As I entered Naomi's dorm I could see her digging through a box of her old belongings."
    MC "Nikumaru-san said she can fulfill your request, though about payment you'd need to speak with her in person."
    show GTS neutral with dissolve
    GTS "She accepted my request? That's wonderful to hear. I was quite nervous if I was asking too much."
    MC "What did you request from her?"
    show GTS wink
    GTS "You will see when the time comes. Now then, I've gone ahead and set up a mock dinner table. Please show me what you know about proper dining etiquette."
    if getSkill("Academics") > 5: #tbd?
        "As I had done many times before, I served Naomi and myself a bowl of rice."
        "Next, I looked to Naomi and we both said 'itadakimasu'; with that out of the way we dug into our meal. Once finished, I placed my chopsticks back into place and we both said 'gochisōsama deshita'."
        show GTS unique
        GTS "I'm impressed by your familiarity with formal dining, though there's still room for improvement."
        MC "What did I miss?"
        "She reaches over and places the lid back on the pot of rice."
        show GTS neutral
        GTS "It is good manners to return all dishes to their places and replace any lids that were removed."
        MC "I'll make sure to remember that when your parents arrive."
        GTS "Your skills are much better than some others I've seen."
        MC "Thank you, that's quite nice to hear coming from someone who knows much more about this formal stuff than me."
        GTS "Thank you for the faith. Now then, let's continue with the other things you need to have down-pat before they arrive."
    else:
        "Taking a seat at our makeshift table, I served myself some rice and tea before digging in. Naomi, I noticed, paused for a moment before also eating her food. Once I had finished my food I set my chopsticks back in their place."
        MC "How was that?"
        show GTS neutral
        GTS "It certainly has room for improvement. You do have some understanding, which is good to see."
        MCT "At least she was polite about saying I'm bad at this."
        MC "How much time do we have till your parents arrive?"
        GTS "A week, which is more than enough time to get you familiar with everything I have in mind."
        MC "Well, I did say I'm committed to this."
        "She grins and cleans up our dishes."
        GTS "Good. We have much more to go over."
    jump daymenu

label GTS035:
    $lockRoute("GTS")
    $setProgress("GTS", "GTS036")
    scene Dorm Interior with fade
    play music Peaceful
    "My hands shook a little as I checked my hair in the mirror once more. I knew it didn't grow that quickly yet, but my anxiety had me constantly double-checking."
    "I was going to meet Naomi's parents today. I didn't know much about them, and I wasn't sure just how much they even knew about me."
    MCT "Gotta make a good first impression."

    scene School Front with fade #Courtyard GTS potentially, later
    "I stood alongside Naomi as we waited. As I looked up at her, she showed no hesitation as she looked down at me and smiled."
    show GTS_S neutral with dissolve
    GTS_S "You look handsome today, Hotsure-san."
    MC "Eh? Oh, thanks. You look lovely too. Where did you get that kimono? It looks new."
    GTS_S "From the local clothing store. I had it special ordered a couple of weeks ago but asked for a slightly larger size than my height at the time."
    MC "Good foresight on your part. It looks good on you."
    GTS_S "Thank you, Hotsure-san. Hm?"
    "Naomi focused her vision off to the distance, placing her hand over her forehead to shield her eyes from the sunlight."
    GTS_S "Ah, I see them. Shall we be off?"
    "Naomi began walking out past the gates of the school, and I followed her."
    "I could see two figures approaching us, a middle-aged couple with the man dressed in what I would consider an expensive suit, while the woman was adorned in an elegant kimono similar to Naomi's."
    "As we drew near, there was a pause as Naomi's mother suddenly clutched her husband's arm and concern wrung her face. Naomi stopped too, but as I turned to see what was wrong a voice called out."
    UNKNOWN "Hey! Heads up! Dog incoming!"
    "I turned back just in time to see a white dog run up and reach up towards me. It gave me a quick lick and began to sniff me before focusing its attention on Naomi, barking excitedly."
    "I heard a small giggle as Naomi kneeled down and tenderly pet the dog."
    show GTS_S happy
    GTS_S "Hello Kimiko, it's been a while. I hope you've been a good girl for Kazumi."

    if getFlag("GTS006_c2"):
        "I joined Naomi in the petting, kneeling beside her as a smile grew on my face and I rubbed Kimiko's fluffy fur."
        MC "Hey there, girl. Wow, you're just as cute as Naomi said. Such nice fur, too."
        UNKNOWN "Thanks. I spend a lot of time taking care of her fur."
        hide GTS_S with dissolve
        show GTS neutral at Position(xcenter=0.4, yalign=1.0) with dissolve
        #show Kazumi at Position(xcenter=0.6, yalign=1.0) with dissolve
        "I looked up and saw a smiling face that reminded me of Naomi."
    else:
        "I smiled as the dog seemed happy to receive Naomi's affection before I turned my focus to the figure who had called out earlier."
        hide GTS_S with dissolve
        show GTS neutral at Position(xcenter=0.4, yalign=1.0) with dissolve
        #show Kazumi at Position(xcenter=0.6, yalign=1.0) with dissolve
    Kazumi "Hello, I'm Kazumi Yamazaki. It's a pleasure to meet you."
    MC "Keisuke Hotsure, nice to meet you as well."
    "We both gave each other a light bow as Naomi's father came up alongside Kazumi."
    show Akihiro neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    UNKNOWN "Kazumi, I thought you said you'd keep Kimiko in the car."
    Kazumi "Apologies, Father. She must've smelt Naomi and became rather restless, so I thought it'd be best to let her out."
    UNKNOWN "Hm, just make sure that she doesn't run off again."
    "Kazumi nodded and gave a light snap of her fingers, which made Kimiko bark and move to Kazumi's side before sitting on her own."
    UNKNOWN "Now, then. Who might you be, young man?"
    hide GTS
    show GTS_S embarrassed
    GTS_S "Ah! Yes, sorry! Father, Mother, this is my... boyfriend, Keisuke Hotsure."
    "Her father didn't react much to the news, as he only gave a small nod while, Kazumi had a more surprised expression, as did her mother."
    MC "It's an honor to meet you, sir!"
    "I bowed deeply."
    show Miko neutral at Position(xcenter=0.9, yalign=1.0) with dissolve
    Akihiro "Hotsure-san, I'm Akihiro Yamazaki, and this is my wife Miko."
    Miko "A pleasure, Hotsure-san."
    MC "Likewise, ma'am."
    Miko "Oh, so polite. And handsome too, you've done well Naomi."
    GTS_S "U-uh, t-thank you Mother."
    MCT "It's strange seeing Naomi so hesitant and shaky. I always took her as the collected, mature one of the group, but she appears to be just as nervous as I am."
    MC "T-thank you ma'am. Where will you be staying, if you don't mind me asking?"
    Akihiro "I saw that there was a respectable hotel in Satoyama Village, so we'll be staying there for the weekend."
    Akihiro "My wife and I have been more than a little curious to see the island ever since Naomi was enrolled in this school, so we will be taking in the sights."
    MC "Sounds like a good time, sir."
    Akihiro "I am hoping it will be, as I was hoping you'd be willing to join us."
    MC "H-huh?"
    Akihiro "I must admit, the sudden news of your relationship to Naomi has left me intrigued to know more about you."
    MC "U-uh..."
    show GTS_S shy
    GTS_S "Father..."
    Akihiro "Please, Naomi, as a father, I watch out for my family. So what do you say, Hotsure-san? Will you join us for a small trip tomorrow, as well as dinner perhaps?"
    menu:
        "S-sure, I came with Naomi to meet you. So might as well dive right in.":
            jump GTS035_c1_1
        "U-um actually... I-I'm rather busy this weekend...":
            jump GTS035_c1_2

label GTS035_c1_1:
    MC "S-sure, I came with Naomi to meet you. So might as well dive right in."
    show GTS_S happy
    GTS_S "Keisuke..."
    Akihiro "Good. Now, if you'll excuse us, we have to get checked in to our hotel. Please be by the hotel around 5 A.M."
    MC "W-what!?"
    GTS_S "Of course Father, we'll be there on time."
    Akihiro "Good, good. It was nice meeting you, Hotsure-san."
    hide Akihiro with dissolve
    Miko "It was a pleasure. Please rest well."
    hide Miko with dissolve
    Kazumi "See you two tomorrow morning. Later! Come on, Kimiko."
    #hide Kazumi with dissolve
    "She snapped her fingers once more and the dog barked excitedly before following after her."
    MC "N-nice to meet you all too..."
    $setAffection("GTS", 10)
    GTS_S "Thank you so much for accepting, Hotsure-san."
    MC "It was bound to happen eventually. So why not now, right?"
    GTS_S "Still, I'm happy you decided to join us."
    MC "Well that's all the reason I need to go, then."
    "I saw her face blush as I smirked. Taking her hand in my own I began to walk back to the school."
    MC "Come on, I'm gonna need to get to sleep early if I'll be waking up before 5 A.M..."
    if getFlag("GTS034_c1_3"):
        jump GTS035_testpass
    jump daymenu

label GTS035_c1_2:
    MC "U-um actually... I-I'm rather busy this weekend..."
    Akihiro "Hm."
    MC "I'm sorry... I-I wasn't expecting to be asked to join you all. I assumed I would have been intruding if I invited myself so I didn't plan around it."
    Miko "That's unfortunate, but understandable. After all, dear, we shouldn't risk hindering Hotsure-san's school work."
    Akihiro "Yes, I suppose that's true. Very well, Hotsure-san. It was still nice to meet you."
    hide Akihiro with dissolve
    "He gave me a light bow to which I bowed deeper, and he left without another word."
    Miko "It was a pleasure to meet you, Hotsure-san. I hope we get another chance to get to know you soon."
    hide Miko with dissolve
    Kazumi "Yeah, that's a bummer, but hey, what can you do? We'll be waiting at the hotel tomorrow morning, Naomi. You know what time Father likes."
    show GTS_S neutral
    GTS_S "Indeed. Thank you, Kazumi."
    Kazumi "Later! Come on, Kimiko."
    #hide Kazumi with dissolve
    "She snapped her fingers once more and the dog barked excitedly before following after her."
    "I felt a small lump form in my throat as I looked down before finally looking towards Naomi."
    MC "I'm sorry..."
    $setAffection("GTS", -10)
    GTS_S "It's fine, Hotsure-san. It was too sudden. I apologize for my father putting you on the spot like that."
    MC "I would have loved to go. It's just... maybe a little too soon to spend the whole day with them?"
    show GTS_S sad
    GTS_S "Yes, I understand. Still, thank you for joining me in seeing them today."
    MC "I'll... make it up to you. I promise."
    show GTS_S neutral
    GTS_S "It's perfectly okay. The last thing I'd want is for you to be uncomfortable."
    GTS_S "Would it be okay to head back to the dorm? I need to prepare for tomorrow."
    MC "Yeah, sure."
    "We walked back towards the school in silence as I looked down, thinking of some way to make it up to her."
    #if getFlag("GTS034_c1_3"):
    #    jump GTS035_testpass
    jump daymenu

label GTS035_testpass:
    scene Dorm Interior with fade
    "When I awoke the next morning, it wasn't due to my alarm ringing but of someone singing."
    MCT "The heck? That's not my alarm."
    UNKNOWN "Sekai wa kawari dasu, Inori mo todokanai, Boku ga kawari dasu."
    MCT "Sounds like it's coming from outside."
    scene Dorm Exterior with fade
    "I walk over and open my window. Naomi was leaning against the side of the dorm, humming and singing to herself."
    show GTS_S unique with dissolve
    GTS_S "Kimi wo motomete hashiri tsuzukete, Jibun ga dare ka wakaranaku naru, Naki-sōdakedo maketakunaikara."
    MC "Good morning, Yamazaki-san."
    show GTS_S surprised
    GTS_S "Eep! Oh, it's you, Hotsure-san. Please don't spook me like that."
    MC "Apologies, I was just listening to your singing."
    show GTS_S embarrassed
    GTS_S "Oh, I didn't realize you could hear me. I'm sorry if I disturbed your slumber."
    MC "There's no need to apologize. I needed to get up anyway to prepare for our day with your parents."
    GTS_S "Hotsure-san... I just wanted to say 'thank you' again for doing this. If you don't wish to do this, you can just say so. I know we've only been dating for a little while, so this may be rather sudden."
    MC "Trust me, Naomi-chan. I'm certain that I want to do this. I'm interested in you, and if that means meeting your parents, then I'll do it."
    show GTS_S neutral
    GTS_S "Thank you, Hotsure-san... wait, did you just call me 'Naomi-chan?'"
    MC "I did. Must've slipped out on accident."
    GTS_S "Let's keep the names formal for today and discuss the matter later."
    MC "I understand, Yamazaki-san. Now, pardon me while I get ready."
    "I closed my window and got ready all the while I could hear Naomi humming the same tune to herself."
    if getSkill("Art") >= 6:
        "When deciding what to wear, I decided that since this is a very special kind of event and I should dress appropriately."
        "Reaching under my bed and I produced my dark blue Yukata that hadn't been used in some time. Throwing on the article and tying the sash I headed outside."
        MC "How do I look?"
        show GTS_S surprised
        $setAffection("GTS", 1)
        GTS_S "Oh my, that looks wonderful. I'm quite surprised you have one of those here."
        MC "My mom made me bring it in case I found myself needing a date with a hot girl."
        show GTS_S embarrassed
        GTS_S "Your mother sounds like a thoughtful woman."
        show GTS_S neutral
        GTS_S "Anyway, we better be going, it's nearly 5. Thankfully this place is quite close so I don't need to rush."
        MC "I'm right behind you."
    else:
        "When deciding what to wear I decided that a suit will be more than suitable for the occasion. Slipping on my dress shoes and straightening my tie I heard downstairs."
        MC "How do I look?"
        "Naomi cocked her head and looked at me like she was deciding the best way to describe a bad situation."
        GTS_S "Well it should be adequate for today, though maybe at some point we could get you a proper Yukata."
        GTS_S "Anyway, we better get going. It's nearly 5, and my father is very particular about timeliness."
        MC "Just lead the way, since you appear to know where this place is."

    scene Hill Road with fade
    play music GTS
    if getSkill("Athletics") >= 7:
        "As we made our way down the road towards the inn I began to notice just how much effort it was taking to keep pace with Naomi. Every eight steps for me was like one for her which made keeping pace a good workout."
        MCT "Man, I better not slack off on the track. Otherwise, I can't see myself keeping pace with her much longer."
    else:
        "As we made our way down the road toward the inn, I found myself struggling to keep pace with Naomi."
        MC "Yamazaki-san, can you stop for a moment?"
        "She stops and finds me trying to catch my breath."
        show GTS_S surprised with dissolve
        GTS_S "Hotsure-san, are you ok?"
        MC "Yeah, just finding it a bit hard to keep pace with you. Your strides are a bit longer than mine now."
        GTS_S "I'm sorry, Hotsure-san. I didn't mean to wear you out like that."
        MC "It's all right. Just give me a minute to catch my breath."
        hide GTS_S with dissolve
        "After a minute or so I felt my energy return and we continued on our way, though I noticed how much shorter Naomi took her strides."
    "We reached the inn just as the first rays of the sun could be seen creeping up on the horizon. The inn was several small huts in a circle around the cul-de-sac entrance."
    "As we approached, we heard the sound of scampering feet before the family dog came rushing up to us. Eventually, Kazumi showed up wearing her kimono."
    if getSkill("Art") >= 6:
        #kazumi position left, face right
        Kazumi "Good to see you made it early. Father will be quite pleased to know you're here."
        show GTS_S neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
        GTS_S "Then we best not keep him waiting. He probably already has the plans for today made."
        "Kazumi called the dog back and went back to grab her parents."
    else:
        "When Kazumi approached she paused, looking me over before looking at her sister. Some sort of signal I supposed, between sisters."
        #kazumi position left, face right
        Kazumi "Good to see you made it early. Father will be quite pleased to know you're here."
        show GTS_S neutral with dissolve #pos r face l
        GTS_S "Then we best not keep him waiting, he probably already has the plans for today made."
        "Kazumi called the dog back and led us back to the front of the inn building their family was staying in."
    "Dressed in formal kimonos were both of their parents, looking more prepared for a formal dinner then a day on the town."
    #hide kazumi
    MCT "I had some idea how traditional her parents were, but this is a bit more than I was led to believe."
    show Akihiro neutral at Position(xcenter=0.25, yalign=1.0), Transform(xzoom=1.0) with dissolve
    Akihiro "Good Morning, Hotsure-san. I'm pleased to see you joining us this early."
    MC "It was no trouble, sir. Yamazaki-san made sure that we made it here in a timely manner."
    Akihiro "I expect nothing less from my daughter. Now then, we should make our way to town. There is a coastal trail we can take."
    MC "That sounds like a wonderful suggestion, sir."
    GTS_S "That does sound wonderful. I haven't seen much of the ocean since arriving."
    "Her father took the lead and guided our group through the trees behind the inn onto a well-kept trail. Kazumi and Miko followed behind Akihiro while Naomi and I brought up the rear of the party."
    "As we walked I would occasionally peek back at Naomi and noticed her swiping and pushing away many branches that were far out of reach of the rest of us."
    "Her strides were still much longer than ours, forcing her to deliberately take shallower steps if she didn't want to outpace the rest of the group. Considering the alternative, keeping Naomi at the back seemed like the best option."
    "The woods faded into grassland as we approached the cliffside. When Naomi emerged, I spotted that more than a few twigs had found their way into her hair."
    MC "Yamazaki-san, you have a bit more natural radiance than normal. Have you become one with the Earth?"
    "Naomi gives me a blank stare for a moment before hastily yanking the twigs from her hair."
    show GTS_S embarrassed
    GTS_S "Thank you, Hotsure-san."
    "We exchange smiles before rejoining her family along the cliffside."
    "The sunrise was quite radiant as its beams rested on the water. The day had just begun."
    Akihiro "When Naomi was younger, we'd take her to visit our family's summer home on the coast. We would constantly find her up at the break of dawn sitting on the porch watching the sun rise."
    MC "I can't blame her, this is quite a sight. I've rarely visited the coast, and even when I did, I never considered watching the sunrise."
    Akihiro "We watched many New Years Sunrises from those steps. Hopefully, the stars will align for us to revisit that special place."
    MC "Did something happen to prevent a return?"
    Akihiro "Time passes and places fade."
    "A silence fell over the group before her father spoke up again."
    Akihiro "We should head into town and see what the local treasures are."
    Miko "I wonder if they have any places to shop or entertainment."
    MC "There are certainly a few good shops from what my friend Honoka has said."
    "With a nod from Akihiro, we begin heading for town."

    scene Town with fade
    play music BrightLights
    "The town was quite busy for a weekend; it was a surprise to me but I could see it was very uncomfortable for Naomi. She was constantly having to look down, watching every single one of her delicately placed footsteps."
    MC "Would you like to do anything in particular?"
    show GTS_S neutral with dissolve
    GTS_S "There are few places that I can fully enjoy, I'm afraid."
    "I didn't like seeing Naomi with that mindset. I wanted to figure out a way to let her feel at least {i}somewhat{/i} normal. There must have been {i}something{/i} we could do to pass the time."
    MC "Why don't we walk around the shopping district? We might find something you like."
    GTS_S "Oh? I suppose there are a few essentials I could pick up while we're here."
    MC "No, I meant... fun stuff. I was offering you a gift."
    show GTS_S embarrassed
    GTS_S "Ah, right! I apologize. I'm not used to being offered presents."
    MC "Really? You aren't?"
    show GTS_S neutral
    GTS_S "I usually just buy the things that I want myself. I haven't had someone offer to buy things for me since I was little."
    MC "Well, there's no harm in window shopping. We can just pace around; see if there's anything you like."
    GTS_S "Don't hesitate to purchase something for yourself too, Hotsure-san. It's important to love yourself just as much as you love others."
    "We walked around the shopping district for several minutes. Naomi kept pace with me by intentionally slowing down her strides. Every step Naomi took was roughly three for me."
    "Eventually, we came across a hobby store that specialized in various arts and crafts. The window display had a wide assortment of scrapbooking supplies available, including premium folder sets and binders."

    "Some of them were very professional looking, like what one would see in a magazine display."
    "Others were more intended for enthusiasts, with binders that featured characters from various anime and video games. A bright, vibrant 'OPEN' sign accompanied the display."
    "Naomi seemed interested as we walked past, crouching down to make herself eye-level with the glass."
    show GTS_S happy
    GTS_S "Ahh, that reminds me. I should really get back into painting."
    MC "You enjoy painting, Yamazaki-san?"
    show GTS_S neutral
    GTS_S "Well, calligraphy. I enjoyed painting banners when I was a kid. There's something innately satisfying about seeing a bold, perfectly shaped line of kanji painted in an appropriate color."
    GTS_S "To me, it's like a statement using far more than writing alone. The brushstroke can accent the word, or create a dichotomy where it doesn't match the word at all."
    GTS_S "For example, if one were to write the character for 'anger' in a very thin, subtle brushstroke."
    MC "Would you like me to get you a calligraphy pen?"
    show GTS_S sad
    GTS_S "Unfortunately, I don't think I'll be able to write as well as I used to."
    MC "Well, you said yourself that adapting to your new body would be necessary. What better way to do that than to do something you love?"
    GTS_S "You're absolutely certain? I don't want to crush something that you've given me. I'd be worried about it every single time I use it."
    MC "It isn't an issue at all, Yamazaki-san. I promise."
    show GTS_S embarrassed
    GTS_S "Would you like to head inside, then? I'd like to accompany you, but ah..."
    "I chuckled in response."
    MC "I'll be right back, Yamazaki-san."

    scene Supermarket with fade
    "I walked inside the hobby store while Naomi waited outside. I could see her awkwardly cross the street and stand as far away from the sidewalk as possible to avoid blocking traffic."
    "I paced around the aisles for about a minute before I found exactly what I was looking for. It was a set of calligraphy pens, arranged neatly in a case."
    "On the bottom row were pre-built pens which already had the ink inside them, covering every basic color."
    "In addition, the set also came with several pens which allowed you to insert your own inkwell and select different tips to allow for a wide variety of unique fonts and brushstrokes. Of course, they were perfectly sized for human hands."
    MC "These are perfect."
    "They were a little on the pricier side at 3000 yen, but for such a large variety of pens, I felt that the price was fair. I paid for the pens at the checkout before returning outside."

    scene Town with fade
    play music BrightLights
    "Naomi was still standing across the street, standing just as tall as the light poles. She still looked uncomfortable, but as I got closer, I noticed that she was breathing deeply to calm herself."
    "Occasionally, a pedestrian would walk past to stare at her in confusion. Once I returned to her side, I showed her the sealed case."
    show GTS_S neutral with dissolve
    GTS_S "Welcome back. I hope they weren't too much trouble to find."
    MC "Not at all."
    "I gave her a smile as I held up the calligraphy set."
    show GTS_S surprised
    GTS_S "..."
    "Naomi stood on the sidewalk in stunned silence for several seconds."
    GTS_S "Oh my, oh my...."
    MC "Do you like it?"
    GTS_S "Hotsure-san, I... wasn't expecting something so elaborate. Even a single pen would have been perfectly acceptable!"
    MC "Well, now you have 20 to practice with."
    show GTS_S unique
    GTS_S "Hotsure-san... thank you. With deep sincerity, thank you so much. I will treasure them always."
    MC "I'm glad you're happy with them!"
    MCT "Naomi took the calligraphy set from my hands and held it at her side. Unsurprisingly, they looked a lot smaller in her hands."
    show GTS_S neutral
    GTS_S "Shall we see what else the town has to offer?"
    show GTS_S neutral at Position(xcenter=0.75, yalign=1.0)
    show Akihiro neutral at Position(xcenter=0.25, yalign=1.0), Transform(xzoom=1.0)
    with dissolve
    Akihiro "I spotted a flyer in there advertising a local boardwalk if you two would be interested?"
    MC "What do you say, Yamazaki-san?"
    show GTS_S happy
    GTS_S "It sounds like a lovely idea. Hopefully, they have some stuff I can do."
    MC "Let's go find out."

    scene Festival with fade
    "The boardwalk area wasn't too far from the main street. The boardwalk was a standard Carnival Matsuri but with the additional flair of an American one."
    "Stalls full of games, food, and all sorts of fun littered the area. Carnies called out to people walking, trying to reel people over to play their games."
    show GTS_S neutral with dissolve
    GTS_S "This place is quite lively. Even this early in the day they are this energetic."
    MC "Have you ever been to a carnival?"
    GTS_S "I can't recall having gone to one previously. This is all quite new to me."
    MC "Oh, that's a shame; these places are always good fun. My family used to visit a seasonal one that would pop up in the town near us, always had great food and activities."
    MC "My sister always wanted to do the ring toss game even though I told her it was rigged."
    GTS_S "That's adorable, you ought to bring your sister around some time. I don't think we've formally met."
    MC "I could ask her if she's available sometime. She's typically off doing something else with Yuki."
    "Naomi was about to respond when a Barker rushed up to me and began speaking rather fast."
    Barker "Step right up and test your strength. Can you ring that bell?"
    "He handed me a large mallet."
    Barker "C'mon kid you can do it, you'd hate to disappoint the fine lady."
    "Naomi blushes as I raise the mallet."
    if getSkill("Athletics") >= 7:
        "I slammed the hammer down and watched the little peg rocket up but fall a mere inch away from the bell."
    else:
        "I slammed the hammer down and watched the little peg get about halfway up before falling back down."
    Barker "Ooh, better luck next time boy. Work those arms out and try again some other time."
    MCT "Ouch, watch the pride, dude. We all know these things are rigged anyway."
    GTS_S "Excuse me, sir, would you mind if I tried?"
    Barker "Well we normally have a rule on giants, but who am I to deny a pretty lady?"
    "Naomi picked up the hammer that was more like a kid's toy in her hand and brought it down hard. The peg hit the bell so quickly I couldn't even watch it move, but the loud ring certainly made it clear."
    "The carnie blinked several times, scratching his head before handing Naomi what would normally be a massive teddy bear but in her hands seemed normal."
    GTS_S "Thank you, sir."
    "She bowed at the still quite shocked Barker. As she stepped away I could swear I heard him muttering under his breath, 'But that shouldn't have worked.'"
    MC "Nice work on that game. Remind me next time I need a nail fixed to call you up."
    GTS_S "It was nothing, Hotsure-san. That man was rude to you so I needed to protect your honor."
    "We shared a chuckle but as I looked back at the game once more I noticed that the bell now had a large peg-shaped dent in the bottom."
    MCT "Geez, didn't know she was getting that strong."

    scene Ryokan Room with fade
    "As we approached the inn for dinner, it dawned on me that we hadn't considered Naomi's size at all."
    MC "If I may suggest, can dinner be held on the back porch? The weather is quite nice tonight, and it may be beneficial so that everyone can be included in tonight's meal."
    show Akihiro neutral with dissolve
    Akihiro "The weather is quite nice, but I'd hate for our food to be interrupted by pests."
    MC "I don't think all members present will fit within the building, sir."
    "Naomi blushed and sunk her face into her hair, slouching as she tried to turn invisible. Her father tapped his chin for a moment."
    Akihiro "I suppose the pests can be tolerated for this evening."
    MC "Thank you, sir."
    "Stepping around the house, Naomi, Akihiro, and I stood around the table as her mother and sister gathered the dishes and utensils for the meal. Glancing at Naomi, I could see that while she was smiling, there was a hint of sadness in her eyes."
    show cg GTS035 with dissolve
    "Eventually her family stepped out with the tea and food for the evening. We exchanged bows and took the Seiza position around the table. Naomi reached for the tea set but her father raised his hand."
    Akihiro "No Naomi, I believe Kazumi should do the ceremony tonight. She has been practicing, so let us observe her work."
    "Her mouth fell open, but she quickly snapped it shut as her sister began the tea ceremony. Kazumi exhibited a level of skill with the making of the tea, always making sure that each step was done precisely as the last."
    "One by one she served us our tea, though I noticed her hesitation on giving Naomi her cup."
    Akihiro "Well done, Kazumi. I see the school has taught you as well as they did your sister. Now then, let us begin our meal."
    "Kazumi lays out some tempura, sashimi, and miso soup. I served myself a bit of every dish and was about to begin eating when I realized that Naomi hadn't been served."
    "Taking her plate, I served her some of the available food as well. She smiled and softly thanked me."
    Akihiro "So Hotsure-san, how long have you known my daughter?"
    MC "Only since the beginning of the semester, sir. We have the same classes, so we see each other every day."
    Akihiro "I assume that, since you also attend this institution, you must also have one of those abnormalities."
    MC "A factor? Yes, I do, though mine is much more manageable. My hair grows much faster than normal."
    Akihiro "That's quite interesting. I wasn't aware that they came in less extreme forms."
    MC "Some don't have factors, but still attend the school. Like my roommate. Though he is there mainly for his sister who does have a factor."
    Akihiro "Why?"
    MC "His sister wanted him for emotional support if I recall correctly."
    Akihiro "I see. And this is common?"
    MC "Well, I... believe so? At least a good amount of students don't have any abnormalities."
    #(Possibly add a check here if a relation with Daichi becomes a factor)
    Akihiro "Ah. Well, I certainly hope they can manage resources and... space, with this program."
    "I noticed him glance towards Naomi as he took a bite of his food."

    menu:
        "(Interject/comment)":
            $setFlag("GTS035_int1")
            MC "You can refer to her by her name at least."
            "Naomi quickly shot me a glare that made me quickly drop my attitude."
            MC "Sorry, what I meant was-"
            "Her father held up his hand before anyone could speak further."
            Akihiro "You are quite the outspoken one, young man. Your solicitude is very apparent indeed."
            MC "My apologies, sir."
        "(Let it slide)":
            pass
    Akihiro "When we first heard the news, we went to the temple and prayed to be spared from further misfortune."
    MC "Are you referring to the factors?"
    Akihiro "Indeed so."
    MC "Ah. In which case, surely it's good to know that it's not like a virus."
    Akihiro "So it has been said. But it is by providence, then, that I must continue to contemplate this wisdom for the sake of my remaining daughter."
    "Suddenly, a faint SNAP could be heard from Naomi's direction. I looked over to see that her chopstick was now shattered into several fragments between her fingers."
    GTS "Ah, excuse me, it seems I've unduly and clumsily damaged my chopstick."
    Akihiro "Mm."
    Miko "Kazumi, please get your sister another pair, please."
    Kazumi "Yes mother."
    "Naomi's mother nodded as Kazumi bowed leaving the room, placing a hand on her husband's leg."
    Miko "Dear, I believe Naomi put too much pressure on her chopsticks. Quite rare, is it not?"
    Akihiro "Indeed. Her newfound strength is difficult. Very difficult indeed."
    Miko "... Hmm~"
    "Naomi's mother cocked her head to the side for a moment before turning to me."
    Miko "Hotsure-san. Surely this situation is of great misfortune to you."
    MC "Ah, you mean me being, well, afflicted?"
    Miko "So you say, indeed."
    "The room fell silent as Kazumi returned with a new set of chopsticks."
    Akihiro "What are your fields of study?"
    MC "I'm looking to study architecture in college."
    Akihiro "How did that desire manifest?"
    MC "When I was little my father gave me a book on famous architecture across the world. I read that thing over and over until I decided that I wanted to design something that could be in that book."
    Akihiro "A noble endeavor to build a legacy for oneself. Though I can see your ambitions having secondary utility in more personal matters if you so choose."

    menu:
        "(Comment)":
            $setFlag("GTS035_int2")
            MC "If matters continue as they are then I suppose that your point is valid. However, you don't need to be so passive addressing the elephant in the room sir."
            Akihiro "I can assure you that my words are meant to make sure that you can provide for my daughter. Any other inference you may take from my words are unintended."
            "I recoiled a bit realizing I must've taken his bait."
            MC "My apologies, sir."
        "(Remain silent)":
            pass
    hide cg with dissolve
    "Eventually we finished our supper with Kazumi and Miko taking care of the dishes. Naomi had wandered off towards a koi pond at the edge of the inn's yard. I stood and was preparing to walk towards her when I noticed her father stand up and approach me."

    Akihiro "They say a tree is only as strong as the ground beneath it, but that is not true. A tree can grow on a rock and still thrive, but it's the support it receives that keeps it alive."
    if getFlag("GTS035_int1") and getFlag("GTS035_int2"):
        Akihiro "Was it out of passion?"
        MC "Pardon?"
        Akihiro "As I mentioned before you were only reacting as any man should when one's passion is threatened. You wear your passion for my daughter openly and for that, I cannot be mad at you."
        Akihiro "Such passion is very awe inspiring, very awe inspiring indeed. Ensure that you do not bite your tongue with the quickness of your speech from such overwhelming passion."
        "As I stumbled for words he turned and left me standing on the porch."
    elif getFlag("GTS035_int1") or getFlag("GTS035_int2"):
        Akihiro "I never doubted my daughter and she has never disappointed me. Your burst of passion, while rude, was striking. Carry that on."
        MC "Apologies for that."
        Akihiro "I understand how it is to love. Just make sure to direct that energy in the proper channels, please."
        "We share a brief moment of silence."
        $setAffection("GTS", 5)
        Akihiro "She taught you well I have to say."
        MC "Pardon?"
        Akihiro "You ate with the same subtle movements she does."
        "As I searched for a response he patted me on my back and departed the porch."
    else:
        $setAffection("GTS", 10)
        Akihiro "Your love for my daughter must be strong for you to follow her directions for tonight."
        MC "Pardon?"
        Akihiro "Your manners tonight were quite splendid but showed obvious signs of underutilization and lack of polish. My daughter's subtle movements and mannerisms were a tad obvious in your body movement and posture during dinner."
        MC "My family doesn't practice these sorts of traditions at home so I was a bit rusty."
        if getSkill("Art") < 6:
            Akihiro "I suggest the next time we meet, invest in some more appropriate attire."
        else:
            Akihiro "It is reassuring to know you were able to dress properly for this occasion."
        "Before I could form a response he patted my arm and headed inside, leaving alone on the porch."
    hide Akihiro with dissolve
    MCT "Well, he certainly is blunt when he wants to be."
    show GTS neutral with dissolve
    GTS "Is everything alright, Hotsure-san?"
    "I jumped a little from Naomi's sudden appearance."
    MC "Oh! Yes, sorry, just thinking over some stuff your father told me."
    show GTS happy
    GTS "Oh, I bet it was one of his many proverbs."
    MC "About a tree on a rock."
    show GTS neutral
    GTS "Yes, though that one is certainly new."
    MC "Are you ready to head back to school? It's getting dark and I'd hate for us to be on the road at this hour."
    GTS "Of course, let me just tell them we are leaving. I'll meet you in the parking lot, ok?"
    MC "Sure thing."
    "I only had to wait a few minutes before I saw Naomi walking back from the inn with a wide smile."
    MC "Someone has heard some good news."
    show GTS happy
    GTS "Father approves!"
    MC "That's great! I was scared I'd failed his tests."
    GTS "You shouldn't doubt yourself so much Hotsure-san. If anything I'm happy you met him as it means a lot to me."
    MC "It certainly was nerve-wracking but I think I just worried about myself too much."
    "She leaned down and tapped the top of my head with her finger."
    show GTS neutral
    GTS_S "Now then let's get on our way back to school."
    "I reshuffled my hair as we walked back to school."
    jump daymenu

label GTS036:
    $setProgress("GTS", "GTS037")
    scene Dorm Interior with fade
    "It had been two days since the meeting with Naomi’s parents, and things had been quiet between us."
    "This left me plenty of time to repeat the dinner scene over and over. Her father had been particularly difficult to deal with, but not in a way that was malicious."
    "It had grown apparent the task that lay ahead of me in rising not only to Naomi's standards, but her family's too."
    if getAffection("GTS") > 30:
        extend " But it would be a small price to pay."
    "Eventually, I had to roll out of bed and get to work on my homework. A shower would hopefully allow me some time to destress."
    play sound Knock
    play music RM
    RM "Hey Hotsure-san, you got some mail."
    MCT "...From who?"
    show RM neutral with dissolve
    "Opening the door, I could see a box wrapped in brown paper clutched under Daichi’s arm."
    RM "There's this letter, too. They're both addressed to you."
    "He produced a small envelope with a green wax seal."
    RM "Whoever sent you this evidently has no idea what email is. Who the hell owns a wax stamp?"
    MC "Not everyone owns a top end laptop. Some people don’t even have internet."
    RM "I'm not sure how some people survive."
    hide RM with dissolve
    stop music
    "He handed me the box and returned to his room. Looking over the package, there appeared to be no markings besides the address."
    MCT "I wonder who could've sent me this. I doubt my parents would; they normally only send that stuff to Tomoko for some reason."
    Letter "Dear Hotsure-san,{w} our meeting the other night was reassuring in many ways to my wife and I. We know that our eldest is a special person, and she deserves someone of equal kind.{w} Please accept this gift as a display of hope towards your futures."
    "After I set the letter down, I began disassembling the brown packaging. Lifting the lid, I spotted an ornate, lacquered black box sitting amongst the packing material. With leaden curiosity, I lifted the box out, and gently opened the smaller box."
    "Inside was a tanto, its flawless blade glaring white in the afternoon sun."
    MCT "...How the hell did this get through customs?"
    "Looking the blade over, I decided to set it on the bookshelf hanging over my desk. I began wondering if Naomi knew they had done this."
    "After fiddling with it a bit more, I eventually found a spot on my shelf to display it. The tanto must’ve had a link to Naomi, because the moment the metal left my fingers my phone buzzed."
    GTSCell "Hotsure-san, do you mind meeting me at Chūkan Point in a few minutes?"
    menu:
        "Sure thing, see you in a few.":
            jump GTS036_c1_1
        "I have some stuff to take care of, but I'll meet you as soon as I'm done.":
            jump GTS036_c1_2

label GTS036_c1_1:
    GTSCell "Thank you."
    MCT "What's up with that? She isn't normally that hasty."
    "...But I shrugged, and put on my shoes."
    scene black with fade
    $setTime(TimeEnum.EVE)
    pause 1
    jump GTS036_c2

label GTS036_c1_2:
    $setAffection("GTS", -1)
    GTSCell "This is rather important. Are you sure you cannot find the time?"
    MCCell "sorry but yes. You won't have to wait long i promise"
    GTSCell "As you wish. I hope your errands go well."
    MCCell "thanks"
    "At least I wasn't too dense to take a hint. I snatched up my laundry basket and marched out the door."
    scene black with fade
    $setTime(TimeEnum.EVE)
    pause 1
    jump GTS036_c2

label GTS036_c2:
    scene Chukan Point with fade
    play music GTS
    "As I approached the small park area, I couldn’t help but be in awe how Naomi was nearly as tall... or taller... than the trees around her. Granted, many were cherry blossoms, but it was still a considerable line to cross."
    MC "Yamazaki-san!"
    show GTS despaired-thought with dissolve
    GTS "Oh. Good evening, Hotsure-san."
    "Her tone was different, like cracked glass, her usual smoothness absent and poorly substituted."
    MC "Sooo, uh... why the short notice text?"
    GTS "I will explain shortly. Did you receive the package from my parents?"
    MC "The tanto? Yeah, I picked out a spot for it above my desk."
    show GTS neutral
    GTS "I’m glad that you took it so well. I was unsure how you would receive it when father informed me that he’d given that to you. I assume that he attached a letter as well?"
    MC "Yep, he said he hoped that it would serve as a visual symbol of hope for our relationship."
    GTS "He normally isn’t that forward with people, especially concerning matters related to his family."
    MC "I guessed not. So again, what was with the short notice text?"
    show GTS sad-2 at Transform(xzoom=-1) with dissolve
    "Naomi seemed to look for a place to sit, glancing at the various benches, each time considering her options before remembering her size. A few times, she opened her mouth as though to say something."
    show GTS despaired-thought at Transform(xzoom=1) with dissolve
    GTS "Do you remember that evening on the roof?"
    if getFlag("GTS025_kiss"):
        MC "You mean when we first kissed? The suddenness of that moment, I doubt I could forget if I tried."
        show GTS neutral
        GTS "I am glad that we experienced similar feelings."
    else:
        MC "Yeah, I do."
        MC "I know nothing really happened, but... it kind of did, you know?"
        show GTS neutral
        GTS "I understand completely."
    GTS "Well, back then I wasn’t certain what to think, or even where I’d be in due time. This past weekend brought that feeling back, and I wanted to find out if it's mutual."
    GTS "So, there's something I need to ask you."
    MC "Okay... I'm ready."
    show GTS embarrassed
    pause 0.5
    GTS "Do you love me?"
    jump GTS036_menu

label GTS036_menu:
    menu:
        "I do.":
            $setFlag("GTS036_declare")
            jump GTS036_c2_1
        "What do you mean, exactly?" if not getFlag("GTS036_middlepath"):
            $setFlag("GTS036_middlepath")
            jump GTS036_c2_2
        "Well, that's complicated.":
            $setFlag("GTS036_nodeclare")
            jump GTS036_c2_3

label GTS036_c2_1:
    MC "I wasn’t sure when we first met what the feeling in my chest meant, but the more we’ve talked, I’ve only grown more certain that it's love."
    $setAffection("GTS", 1)
    show GTS happy
    GTS "I shared those feelings, but wasn’t sure if I could trust them."
    show GTS neutral
    GTS "I know, despite that, I've asked of you a number of things you would be well within your rights to move on for."
    MC "You know there was no real choice."
    show GTS unique
    "A sputtering grin escaped her, before with a wave of her hand she composed herself again."
    if getAffection("GTS") > 70:
        show GTS aroused
        GTS "I love you, too, Hotsure-san."
        show GTS aroused at Transform(yoffset=90) with move
        "She knelt down beside me in one smooth motion, her countenance still warm and her face growing warmer."
        GTS "Oh my, that felt good."
        GTS "I confess I've been trying to maintain my composure for some time now."
        "And then, I couldn't help but chuckle as my eyes drifted up to the sky."
        MC "You wouldn't be you if you didn't, would you? That's part of what makes you so special."
        show GTS unique
        "She covered her mouth, and I could hear her chest rumbling with uneven laughter punctuated with a dreamy sigh."
        "What more was there to say? I stepped in closer, felt her presence, and raised my arms around the back of her neck in a gentle embrace. Naomi reciprocated, bracing my back with one bending arm and catching my arm in her other hand. "
        "For a moment, she was the air around me, warmly hazy and still."
        show GTS aroused
        "She lingered a moment longer as I ran my hand down one pearl-like cheek, and kissed the other; while I felt her breath flutter, she turned her head to plant a kiss on my cheek... and despite herself, a bit of my neck and my hair, too."
        MC "Ksh..."
        "She sputtered, puffing the hair off her lips. At last, we parted together."
        show GTS neutral
        MC "Heh, would you believe me if I said I cut it this morning?"
        GTS "There's nothing to be done about it, I suppose."
        show GTS neutral at Transform(yoffset=0) with move
        GTS "Ah well... where was I?"
        jump GTS036_c3
    else:
        "She clasped her hands together, now large enough that I could see the faintest trembling, and then she looked into the depths of me."
        GTS "I love you too, Keisuke-chan."
        "I stepped closer to run my hands on the backs of hers, and in the embrace of Naomi's warm aura, I leaned up and in for a kiss on the cheek, which she reciprocated."
        "After a very comfortable moment, I stepped away."
        jump GTS036_c3

label GTS036_c2_2:
    show GTS sad
    GTS "Well... how do I put this?"
    show GTS neutral
    GTS "I feel that you’ve expressed an interest in me, since you were willing to go so far as to meet my family."
    GTS "I hope that I have conveyed my interest in you as well. But then, to answer your question, I want to know how {i}you{/i} see our relationship."
    if getAffection("GTS") < 40:
        MC "I’m still figuring that out for myself."
    else:
        MC "Well, I've sort of... been in this kind of thing before, I guess. But never with someone like you. I guess I sort of feel like... I want to try to live life the way you do."
    "She nodded."
    GTS "Based on your experience, how do you feel? Do you see us as a couple? Are you comfortable with saying that you love me?"
    jump GTS036_menu

label GTS036_c2_3:
    MC "Well, ‘love’ is a very complicated word. I don’t know if I’m ready to say it yet."
    show GTS neutral
    GTS "Then what are you ready to say?"
    MC "Huh?"
    GTS "If not ‘love,’ then what?"
    MC "I mean, I respect you a lot. You've got a lot of talents, and you're always so chill and nice. I just like spending time with you."
    show GTS despaired-thought
    GTS "So, you enjoy spending time with me, but you're afraid of the implications that come with saying that you love me. I understand. It can't be an easy thing to say."
    GTS "I'm curious about one other thing, if you would indulge me. What is love to you?"
    if getAffection("GTS") > 60 and getSkill("Art") > 5:
        MC "Love is an unbreakable bond. You don't think about it, you feel it. The way you light up when the other person's happy. The way they can cover each other's weaknesses. How you can know they'll be there for you, even on your darkest days..."
        MC "...That's what love means to me."
        show GTS unique
        "An uneasy laugh peeked out from between her lips."
        GTS "You were able to conjure that up, just now?"
        "I shrugged."
        MC "For what it's worth, it's been crystalizing for a long time."
        show GTS embarrassed with dissolve
        "Blushing, her stoic countenance regarded her hands wringing in her lap."
        GTS "Indeed, nothing worth having is easily gained."
        show GTS neutral
    elif getAffection("GTS") > 40:
        MC "...Something to be cultivated, I suppose."
        $setAffection("GTS", -5)
        show GTS embarrassed
        "She pursed her lips and stared off into the treeline. The wind and the leaves spoke for her for a moment or two, before she looked back down upon me."
    else:
        "My tongue writhed around on itself, until at last I sighed."
        MC "I don't really know."
        "She nodded, her face a stone mask."
        GTS "As I said, it can't be an easy thing to say."
        $setAffection("GTS", -10)
    jump GTS036_c3

label GTS036_c3:
    MC "Well, since we're talking about this, I have to ask you something, too."
    show GTS neutral
    GTS "Yes?"
    MC "That dinner we had with your parents... that wasn't normal, right?"
    MC "I mean, I know it wasn't like... I don't know how to feel about all that."
    show GTS despaired-thought
    GTS "It was rather unfortunate, yes. Of course I didn't mean to disturb the meal by breaking my chopsticks, but I suppose one could see it as a sign that I should exercise more caution..."
    MC "What? No, Akihiro-san was totally icing you out. Like, he was reading the look on your face just as well as I was, and it was like nothing was happening. What's with that?"
    MC "A father's supposed to be loving and supportive. He just looked like he was scolding you for even showing up."
    show GTS sad
    GTS "The look on my face?..."
    show GTS neutral
    GTS "Well, it is no secret that I did err. The mood would not have been so harsh but for my carelessness, and one can understand how it might be disappointing when one has poured so much effort into giving his child a proper upbringing."
    "I began to wonder whether she was missing the point, or ignoring it."
    MC "So... that wasn't a normal interaction between you and your family, is what you're saying?"
    "She reached up and pinched one of the tree trunks hanging centimeters above her head, and bent it down slightly."
    GTS "Manifestly."
    MC "Alright, well, I'm glad to hear that. So then what's he like normally?"
    GTS "As loving as any father should be. When I said my parents raised a lady, I quite meant it, especially as Kazumi-chan was growing up."
    MC "Especially?"
    GTS "Well, of course. It's only right that the elder sibling should help as well."
    MC "...Yeah, that's fair."
    MC "I just want to say that all this leaves me wondering if they see you differently because of your condition."
    "Naomi, like a judge, slowly but firmly shook her head."
    GTS "I cannot believe that to be true. With respect, I know them, and you do not yet. Believe me when I say their love has not faltered."
    MC "Then why didn't they ever address your condition during dinner? It only came up when I said we should dine outside."
    MC "Do they not see it as a part of you? Don't they see it's not something you can control?"
    hide GTS
    show GTS_S angry
    GTS_S "Please do not speak of my mother and father so impertinently."
    hide GTS_S
    show GTS neutral
    GTS "But you are right, Keisuke-san. I can't control it."
    GTS "But I need not let it control me or my loved ones, either. I have no intention of creating more disharmony than is absolutely unavoidable."
    show GTS sad
    "She folded her hands together."
    GTS "...Can you accept that?"
    "I felt compelled to roll my answer around in my head. Really, I couldn't be surprised she would react this way, nor could I be upset for her just doing the best she could."
    "Nodding, I put my insubstantial hand on her knee."
    show GTS neutral
    MC "I can accept that."
    show GTS happy
    "I felt, I thought, her whole being relax as I said it."
    show GTS happy at Transform(yoffset=90) with move
    "She then brushed my hand aside with the motion of her kneeling on the ground in front of the bench."
    "She was facing me, smiling warmly, as she wrapped her arms around me in a familial embrace. As her head floated close to mine, I heard her whisper."
    show GTS unique
    GTS "Thank you."
    stop music
    "I returned the hug, probably tighter than she was giving me. Her delicately perfumed warmth mixed with the sunny summer evening air, drawing me in, such that her embrace enveloped all of me."
    "I rubbed my arm up and down her back, feeling the tidal ebb and flow of her pensive breaths."
    play music Sunset
    pause 1
    "She didn't part from me, but her hold loosened just a bit after a moment or two."
    MC "Do you want me to walk you back to your dorm?"
    show GTS neutral
    GTS "I would rather... like to stay here for a while."
    "She righted herself, and sat back on the bench. She was looking off into the citrus glow of the horizon, and I joined her."
    if getFlag("GTS036_declare"):
        show GTS unique
        GTS "I love you, Keisuke-chan."
        MC "I love you too, Naomi-chan."
    else:
        GTS "I'm glad that you were here tonight."
        MC "I'm glad to be here."
    "After a pause, she turned her head back down to face me and put her hand over my knees. Her smile was like candlelight."
    MC "You know, after all this, it feels like some kinda veil's been lifted. I feel a lot closer to you."
    show GTS happy
    GTS "As do I, Keisuke-chan, as do I."
    pause 1
    show GTS aroused
    GTS "And yet, I should like to be much closer."
    MCT "...{w} Meaning?..."
    show GTS embarrassed
    "It was at that point I realized I was staring directly ahead... directly into Naomi's chest."
    "She looked away, and gently took her hands off my lap to cover her mouth in advance of a demure cough."
    GTS "Well... yes, I'll stay behind a little longer."
    MC "Alright, I'm gonna get going. See you tomorrow."
    show GTS neutral
    "She nodded but once."
    GTS "Have a pleasant evening."
    hide GTS with dissolve
    "Just a little longer, and I started walking back to the dorms on my own. Naomi remained in the park, only partially obscured by the trees."
    "She remained in my sight only until I exited the park gate. I walked out on surer steps than I came in with; energy that I didn’t know I had powering my strides."
    jump daymenu

label GTS037:
    $setProgress("GTS", "GTS039")
    scene Classroom with fade
    play music Schoolday
    "Another day of my classes had come and gone. I sat in my chair, packing up my supplies as the other students prepared to leave. Tashi-sensei chimed in with a personal anecdote after the lesson was over."
    show HR neutral with dissolve
    HR "...and that's why you should never use a power drill in place of a dental drill."
    hide HR with dissolve
    show BE surprised with dissolve
    BE "That was an ACTUAL warning label?! But... why?!"
    hide BE with dissolve
    show HR neutral with dissolve
    HR "I imagine it's because at least one person has tried it before. It's the same reason we needed to amend the code of conduct to include a rule against asking giant students to step on you."
    hide HR with dissolve
    show WG stern with dissolve
    WG "Students have... actually agreed to that willingly?"
    hide WG with dissolve
    show HR neutral at Position(xcenter=0.25, yalign=1.0) with dissolve
    HR "I've seen the results of it several times, as a matter of fact."
    show AE neutral at Position(xcenter=0.75, yalign=1.0) with dissolve
    AE "Why am I not the least bit surprised by that information?"
    "I briefly glanced over to my phone. On the screen, my most recently dialed contact was Naomi. I stared at her contact icon for several seconds, before darting my vision back over to Matsumoto-san."
    "My eyes wandered back and forth between my phone and the active conversation a few more times before I slowly slid my phone into my bag and casually stood up to leave the room. This news... probably wasn't anything to worry about. Probably."

    scene Hallway with fade
    "After I had packed up and returned to the hallway, I once again wandered for a few minutes as the quiet, occasional sound of footsteps accompanied my walk."
    "With all of my classes complete, I had plenty of free time. For now, I decided to return to my dorm for the evening. I hadn't made any plans today, so relaxing seemed like the best option."

    scene Dorm Exterior with fade
    "I made my way back to the dorms. After I stopped in front of my door and turned my key into the lock, I heard the distinctive sound of typing coming from the other side."
    "Perhaps Daichi was taking his usual notes. I closed the door behind me after setting my supplies on the floor."

    scene Dorm Interior with fade
    show RM neutral with dissolve
    MC "Good day, sir. May I interest you in a VPN service? If you use the promo code Illuminati001, you'll receive a free 30-day trial for-"
    show RM smug
    MCT "I must have said something right, if I managed to get Daichi of all people to chuckle."
    RM "Good impression. I actually believed you for a second."
    MC "You should believe me! I just spoke to the boss of the internet, and he's pissed!"
    show RM happy
    "Daichi was getting used to my humor. I could tell he was playing along with my sarcasm."
    RM "Oh, dear. I hope I didn't annoy everyone down at the internet."
    MC "Well, they're still pretty ticked off, but I think I can make it up to them if you hire my tech support service."
    RM "The tech support service that definitely exists?"
    MC "Yes!"
    RM "...and definitely won't install malware onto my PC?"
    MC "The very same!"
    show RM smug
    RM "...and will be mysteriously absent from all internet searches if I were to look up their name?"
    "I was going to see just how long I could keep up the charade, but that's when my phone buzzed with a text notification. I walked to the front of the room and picked up my bag, fishing my phone out from within."
    hide RM with dissolve
    "A small speech bubble had appeared next to Naomi's portrait. I smiled in response, tapping the image to read the text message."
    GTSCell "<Hello, Hotsure-san. Are you available?>"
    "Daichi had already returned to his laptop, but he chimed in, as if on cue."
    show RM smug with dissolve
    RM "It's from Yamazaki-san, isn't it?"
    menu:
        "Send a text message back.":
            jump GTS037_c1_1
        "Call Naomi.":
            jump GTS037_c1_2

label GTS037_c1_1:
    $setFlag("GTS037_c1_1")
    MCCell "<Yes, I'm available. Would you like to do something today?>"
    "I tapped away at my phone as I responded to the message."
    MC "Lucky guess."
    RM "Hardly. No one else on your contacts would make you smile that much from a single text."
    hide RM with dissolve
    "I waited for a few seconds while Naomi typed up a response."
    GTSCell "<I would. Shall I meet you at the courtyard, then?>"
    MCCell "<Sounds good. I'll see you there.>"
    jump GTS037_c1_after

label GTS037_c1_2:
    hide RM with dissolve
    "Without hesitation, I tapped on the phone icon. The speaker chimed with a low, droning dial tone as I waited for Naomi to pick up. The sound was silenced after only a few seconds."
    GTSCell "Hello?"
    MCCell "Hello, Yamazaki-san. I saw your text."
    "I heard a deep, yet muffled giggle coming from the opposite end of the phone."
    $setAffection("GTS", 2)
    GTSCell "I trust that means you're available, then?"
    MCCell "Absolutely. Do you have something in mind?"
    GTSCell "I do. I'd like to fill you in on the details in person, however. Shall we meet at the courtyard?"
    MCCell "Sounds good. I'll be right there."
    jump GTS037_c1_after

label GTS037_c1_after:
    scene Campus Center with fade
    "Within a few minutes, I found myself at the school's central courtyard. Naomi wasn't exactly difficult to find. I was thankful that enough walking space remained for her to move around, even if she couldn't enter the building anymore."
    show GTS neutral with dissolve
    GTS "There you are~"
    MC "Here I am."
    "As Naomi stood, I could tell that she was still making adjustments to her posture. She was speaking to someone less than half her size, which made her question how she should position herself during conversation."
    "She awkwardly draped her body down, slouching slightly to make herself shorter. She placed a hand upon each of her knees to support her upper body, looking at me as one would if addressing a child."
    "Only a second passed before she seemed to reconsider her decision, once again rising to her full height, bending only her chin down without slouching."
    GTS "Hm..."
    MC "Is something on your mind, Naomi-chan?"
    show GTS sad
    GTS "I was just pondering how it'd be best to speak to others. On one hand, craning my neck down might be seen as intimidating, but on the other hand, slouching and leaning might be seen as condescending."
    "I don't want to come across as scary, but I don't want others to think I'm belittling them either. What should I do?"
    MC "I don't think you can take the same approach with every single person you meet. It might just be something that doesn't have a universal answer."
    MC "What do the other giants do?"
    show GTS neutral
    GTS "You know, that is a good question. Most often, when I see the other giant students, they're either speaking amongst themselves, or just watching their classes on the projector screen."
    "The few times I've seen the giants and faculty interact, they'd be sitting down while the medical staff run diagnostics on them."
    MC "In that case, It's probably best to just stand at your full height when speaking. If you plan on being there for a longer amount of time, you can sit."
    GTS "That's reasonable. What about you, though? How would you like me to speak to you?"
    menu:
        "Standing.":
            jump GTS037_c2_1
        "Kneeling.":
            jump GTS037_c2_2
        "Sitting.":
            jump GTS037_c2_3

label GTS037_c2_1:
    MC "I'm okay with looking up, Naomi-chan. You don't need to change your posture for me."
    show GTS surprised
    GTS "Really? You're okay with just looking at my legs? Won't your neck begin to hurt after a while?"
    MC "It's perfectly fine, Naomi-chan. Trust me."
    jump GTS037_c2_after

label GTS037_c2_2:
    MC "Well, since we usually kneel when eating anyway, why not sit on your knees?"
    show GTS happy
    GTS "That could certainly work! It's a comfortable pose for me, and we'll be much closer to eye level."
    MC "It's settled, then. Sitting on your knees will allow us to see eye to eye."
    jump GTS037_c2_after

label GTS037_c2_3:
    MC "Why not just sit cross-legged?"
    show GTS embarrassed
    GTS "The same pose that I take when the medical staff look at me? Ha..."
    MC "No, no. Nothing like that. I meant that it'd be more comfortable than looking down all the time."
    show GTS neutral
    GTS "I understand. I suppose sitting cross-legged would work."
    jump GTS037_c2_after

label GTS037_c2_after:
    if getFlag("GTS037_c1_1"):
        MC "What did you want to talk about, though? I was curious when you sent the text."
    else:
        MC "What did you want to talk about, though? You sounded eager over the phone."
    show GTS happy
    GTS "I was curious if you'd like to go on a nature walk with me. There is a particular shrine I would like to visit near the campus."
    MC "Ah, a shrine? You'd like to meditate?"
    show GTS neutral
    GTS "Exactly. I've even got a few sticks of incense to burn. The shrine is in a rather secluded location near the hilltops, though, so it may take a while for us to get there."
    MC "It might take awhile for me to get there, you mean."
    "Naomi covered her mouth before she let out a powerful, brief chuckle."
    GTS "Does that mean that you're interested?"
    MC "Absolutely. Let's go."
    scene black with fade
    pause 1

    scene Woods with fade #mountain forest?
    "Naomi was generous with her strides as we walked away from the campus, Northeast to the secluded forests which rested just past the borders of the island town."
    "Even though her strides were more than double the length of mine, Naomi intentionally walked in slow motion, pacing herself so we could walk alongside each other."
    "It took us several minutes to get the correct rhythm down, but once we did, I kept perfect pace with her."
    show GTS happy with dissolve
    GTS "I'm very fond of this place. I can finally forget about the grid network of downtown, and just... live. Enjoy myself for a while, without any fear of not having enough space."
    MC "Did you prefer the outdoors, even before your factor started taking effect?"
    show GTS neutral
    GTS "Not necessarily. I was raised with a very closed and restricted view of the world, having never really been exposed to any hobbies outside from traditional Japanese teachings. Botany, calligraphy, origami, martial arts... stuff like that."
    GTS "I suppose that being outside wasn't really preference of mine, but rather it was just what I happened to do most."
    MC "Still. It must be a welcome change of scenery from being in the hangar so much."

    scene Mountains Tori Gate with fade
    show GTS neutral with dissolve
    "Naomi nodded while looking down at me."
    GTS "If nothing else, being outside in the wilderness allows me to breathe much fresher air. Sometimes, I forget what 'outside' is like in the giant dorms."
    MC "I've only been in there a few times, but from what I've seen, the only open part is the central pit. Otherwise, you're traveling the caverns."
    GTS "Exactly. I hardly ever see the sky, unless I walk to the auditorium. It's why I prefer to walk around as much as possible."
    MC "Personally, I think that's a really weird design. Why stick all of the giants underground in caverns? Wouldn't it be easier to just repurpose an airport instead of building hangars in caverns?"
    show GTS surprised
    GTS "You raise a good point. I'd much rather walk around on an airstrip bathed in sunlight, than an underground cave."
    show GTS sad
    GTS "Still... I imagine there must be some sort of justification for that design. Perhaps it'd be too inconvenient to convert an airport, since it'd be too far away from the campus?"
    MC "If that's the case, why not just build hangars north of the dorms?"
    show GTS neutral
    GTS "A valid question. Having a dorm on the surface would feel much more natural than an underground cavern."
    MC "Would you like me to present the idea to Masumoto-san? I'm sure she'd know who to talk to."
    show GTS happy
    GTS "We may be onto something, Kei-chan. You'd certainly have my support."
    hide GTS with dissolve
    "As we continued to walk, the trail slowly began to ascend up a shallow, manageable hill. Naomi's strides made quick work of the trail, clearing it in a matter of three steps. We had been walking alongside each other for the past half hour."

    scene Mountains Shrine with fade
    "When Naomi spotted a peculiar stone statue tucked away in a nearby hilltop, however, she took the lead. Within seconds, I saw her kneeling at the foot of the shrine with a careful, yet heavy thud."
    show GTS_S neutral with dissolve
    "It was somewhat surreal, seeing the person kneeling at the shrine bigger than the shrine itself. Usually, they were large enough for several people at once to gather around them. Naomi's presence barely left any room for me."
    "Still, once I had caught up, I was able to kneel beside her."
    #[Naomi can be chanting additional un-translated Japanese here.]
    "Attached to the shrine was a small prayer bowl filled halfway with water. Upon the water's surface, there were many one yen coins floating about."
    "They were so thin and flat, they were light enough to seamlessly float upon the water's surface. The larger coins had sunk to the bottom."
    "Once Naomi had finished her brief chant, she pulled a large bundle of incense sticks from her bag. This particular bundle was bound with a green rubber band."
    "Naomi's large hands made the incense sticks resemble toothpicks. I could tell that her movements were very, very deliberate and slow. She was conserving all of her focus to be able to avoid snapping the incense in two."
    GTS_S "Could you please unwrap these?"
    "Naomi held the bundle of incense sticks towards me. Even as careful as she had been, her massive fingers would have difficulty unwrapping the rubber bands."
    MC "Sure thing."
    "I pulled upon the green rubber band, freeing the bundle of incense sticks. I pulled two of them from the bundle, placing one of them in a small hole upon the base of the shrine."
    "I handed Naomi the other one. Once again, she carefully and deliberately pinched her pointer and thumb upon it, using only the faintest amount of pressure to carefully grip it between two fingers. She then placed the incense stick next to mine."
    show GTS_S happy
    GTS_S "Thank you, Kei-chan. I wouldn't have been able to do this without you."
    MC "I'm a man of many talents."
    "Naomi covered her mouth with a deep, booming laugh. Several of the birds nearby scattered in response to her powerful voice."
    GTS_S "I'll be certain to call upon you whenever I need to defeat another rubber band."
    "Naomi then pulled out a small lighter from her bag. It was silver and featureless, with a small dial on the side for lighting the flame."
    GTS "Would you like to do the honors?"
    menu:
        "Certainly, I'll light them.":
            jump GTS037_c3_1
        "You can light them, if you'd like.":
            jump GTS037_c3_2

label GTS037_c3_1:
    "I picked up the lighter from Naomi's hands, flicking it open with my thumb. I then carefully lowered the flame onto the tips of the two incense sticks, allowing them to burn."
    $setAffection("GTS", 1)
    jump GTS037_c3_after

label GTS037_c3_2:
    show GTS_S neutral
    GTS_S "I think my hands are too big for the lighter, Kei-chan."
    "Naomi smiled at me with a warm, inviting presence while giggling slightly underneath her breath. She might have been imagining how goofy she looked, holding such a small lighter."
    menu:
        "In that case, I'll light them for you.":
            jump GTS037_c3_1
        "Perhaps it'd be good practice?":
            jump GTS037_c3_3

label GTS037_c3_3:
    show GTS_S sad
    GTS_S "Are you absolutely certain, Kei-chan? The last thing I'd want is to cause damage to the shrine."
    MC "Don't worry about it. I trust you."
    GTS_S "Well, if you insist..."
    "I watched as Naomi used her thumb to flick the lighter open with relative ease, despite how small it looked in her oversized hands."
    "Holding the flame between her finger and thumb, she gently lowered the lighter's flame to both of the incense sticks. They let out a low crackling sound in response."
    "When Naomi pulled her arm back, however, the incredible amount of force caused the lighter to slip from her fingers, landing right in the prayer bowl."
    "Naomi's arm movements were so forceful, a strong gust of wind lingered for a few seconds. Regardless, the incense still burned."
    show GTS_S angry
    GTS_S "Gyaaaah..."
    MC "Hey, you did well. The incense is lit, isn't it? Your hand movements have gotten gentler."
    $setAffection("GTS", -2)
    GTS_S "I know, I know. I'm still rather upset with myself over the chopsticks, is all."
    jump GTS037_c3_after

label GTS037_c3_after:
    show GTS_S neutral
    "A strong, minty scent wafted through the air as the incense burned. Naomi folded her hands, bowing slightly while kneeling at the shrine. I did the same."
    "Naomi went quiet. Her strong, hollow breaths made the air surrounding her pulse and shift with every subtle movement she made. She closed her eyes, peacefully meditating."
    "I copied her movements as best I could. While still kneeling, I folded my hands, bowed, and closed my eyes."

    scene black with fade
    "I could still hear Naomi breathing next to me as I focused. I listened to all of the other noises in the area, focusing on them."
    "The idle chirp of the birds slowly returned as we both kneeled, completely motionless aside from our breaths. The minty scent of the incense filled my nostrils."
    "The mountain breeze washed upon the both of us as we sat there. So close to the mountain range, yet so comparatively far from its peak... I slowly began to hear the whispering wind blow past my ears."
    "I wasn't certain how long Naomi and I remained kneeling at the shrine. It felt like several minutes, but I wasn't keeping track."
    "Soon, the sounds of Naomi's breathing, the hum of the wind, and the chirp of the nearby birds all blended together into low, white noise. I had completely tuned out all distractions."
    "I kneeled in place with my eyes closed for a while longer, before I eventually opened my eyes."

    scene Mountains Shrine with fade
    show GTS happy with dissolve
    "Naomi's face met mine as I opened my eyes, her smile taking up most of my field of vision. She had lowered her position even further to meet my gaze, still in the same position as she was when we first arrived."
    GTS "Thank you for being here with me today. This was fun."
    MC "It's so quiet out here. I almost forgot where we were."
    show GTS neutral
    GTS "It is quite a ways away from campus, isn't it? It's difficult to believe that such a vast mountain range is out here. It feels rather disconnected from the rest of the world."
    MC "Not that it matters, as long as I’m here with you."
    GTS "I’m flattered that you feel that way, Kei-chan."
    "The two of us turned around, leaving the shrine behind. The smoke trails from the burning incense still lingered, coating the area outside the shrine in a thin layer of white vapor."
    GTS "Do you mind if we take our time walking back down the trail? I’d like to... remember this view. Take in all of the scenery."
    MC "Not at all."
    "The two of us proceeded to walk back down the trail. Naomi walked in front of me, intentionally making her strides slow and delicate so I could keep up. The stones were sturdy, and didn’t vibrate at all under Naomi’s light steps."

    scene Mountains Tori Gate with fade
    show GTS unique with dissolve
    "By the time we had returned to the gate leading up to the shrine, Naomi had entered a complete state of relaxation. Her walking was rhythmic and precise, her breathing perfectly paced."
    "Naomi shifted her position, raising her head as she scooted slightly closer, rotating so her knees were pointed towards me rather than towards the shrine. She had a broad, content smile upon her face."
    GTS "May I have a hug?"
    MC "Of course you may."
    "Naomi pulled me into a strong, yet cautious embrace. Even with both of us kneeling, her arms could wrap around me twice over. I could barely reach her lower back. It felt more like I was trying to hug a support beam than an actual person."
    "Even then, we made it work. Naomi held me in a firm, but not painful, hug. I heard the calming, low tone of her heartbeat for several seconds."
    hide GTS with dissolve
    "Naomi guided me back to campus after we had finished hugging. The meditation I had done at the hillside shrine lingered in my memory. Perhaps we would revisit it someday."
    "The mountain range to the northwest likely held many more landmarks we had yet to see."
    jump daymenu

label GTS038:
    jump GTS039

label GTS039:
    $setProgress("GTS", "GTS040")
    scene Campus Center with fade
    play music Schoolday
    "I walked through the central courtyard as the sun had just reached its highest point in the afternoon. It was the weekend, so I had plenty of time to myself."
    "I decided to have a seat upon one of the benches surrounding the big cherry tree in the center of campus. I passed by it almost every single day, and even used it as a study spot on several occasions."
    "This was the first time I ever took a close look at it, however. Blossoms periodically fell from its branches as the gusts of wind made them sway from side to side."
    "Despite being one of the oldest trees on campus, it looked very well maintained. I can understand why this became the centerpiece for Seichou University."
    "I sat underneath the cherry tree for several minutes, scrolling through the messages on my phone. I heard rhythmic, steady pulses on the ground as I looked down."
    "I was used to the sound of the occasional heavy, pulsing footsteps by now, but I still recoiled in surprise upon looking up."

    play music GTS
    show GTS_S neutral-2 with dissolve
    "A familiar face greeted me, standing as tall as the cherry tree itself."
    GTS_S "Good afternoon, Kei-chan."
    "I returned a coy smile, remaining seated on the bench. From my position, I was only as tall as Naomi's knees. Her shadow eclipsed me completely as I looked up, completely blocking the sun."
    MC "Don't sneak up on me like that!"
    show GTS_S unique-2
    "Naomi chuckled, failing to cover her mouth in time. This only made her laugh even harder as she tried to maintain her grace."
    GTS_S "You say that as if I could actually sneak!"
    MC "Hey, you've got the technique almost down. If you tiptoe a bit, you'll be a ghost."
    show GTS_S embarrassed
    GTS_S "I'd be some sort of... abnormally tall secret agent?"
    MC "Part of an elite tactical stealth giant unit."
    "Naomi slowly regained her usual composure and stance. I could tell that she loved to laugh, even if she wobbled slightly as she did so."
    "Hearing the word 'giant' appeared to unsettle her, however. While her composure quickly returned, I could tell that she didn't appear comfortable being called one."
    show GTS_S neutral-2
    GTS_S "As much as I prefer to stay subtle and discreet, you've helped me learn that I don't need to be a ghost. I'd much rather present my true self."
    MC "I'm happy that I can give you that kind of confidence, Naomi-chan."
    show GTS_S aroused
    GTS_S "I certainly hope that the feeling is mutual, Kei-chan."
    MC "It is. You've inspired me to become the best possible person I can."
    show GTS_S neutral-2
    GTS_S "I'm flattered that I have that effect on you."
    "Naomi lowered herself slowly into a seated position, crossing her legs and scooting next to the bench. She awkwardly positioned herself next to me while I remained on the bench, trying to fake the image of us sitting on the same seat."
    "We sat next to each other in silence for a few moments, just taking in the scenery around us. The campus was beautifully maintained, now that I stopped to really appreciate how it looked."
    "I turned towards Naomi as the spring breeze created a slightly chilly, but comforting gust of wind."
    MC "So, did you have any plans for the weekend? I don't usually see you walking around campus."
    show GTS_S sad-2
    GTS_S "Admittedly, I was working on my spatial awareness. I'm not clumsy by any extent of the imagination, but it always helps to be prepared. Prepared to carefully walk over or around things, that is."
    "I nodded in response, listening closely to Naomi's words."
    MC "It's always a good idea to adjust yourself to your new body. The staff at this school are here to help with that, but they can only do so much."
    MC "Unless we get used to our factors and learn how to cope with them, we're just going to keep having the same problems."
    "Naomi frowned slightly, but after a deep exhale, she picked herself up with a motivated nod."
    hide GTS_S
    show GTS neutral-2
    GTS "You're right. You're absolutely right. There is no reason for us to try to fight our factors. We need to have the discipline to act on what we can change, and the wisdom to understand what we cannot change."
    MC "We also can't be afraid to rely on others for support."
    "Naomi and I looked at each other as the spring breeze rolled through the cherry tree once more. We said nothing for several seconds, smiling at each other. Naomi responded with a calm, somber voice."
    GTS_S "I will be with you every step of the way."
    MC "I appreciate that, Naomi-chan."
    hide GTS
    show GTS_S happy
    "The two of us sat next to each other beneath the cherry tree for several more moments, just staring at each other. We didn't speak for at least a minute. It felt wonderful to stop and breathe for a while; to take in the scenery and just... share time together."
    "After a few moments had passed, Naomi spoke up. She had unconsciously started to lean upon the bench, which whined under her substantial weight."
    show GTS_S neutral-2
    GTS_S "That reminds me. I was considering taking a martial arts course to better train my body."
    GTS_S "Exercising alone is perfectly acceptable, but coordinating myself with a group will help me not only with spatial awareness, but also force control and limb coordination."
    GTS_S "Does that sound like something you'd be interested in, Kei-chan?"
    if isHighestSkill("Athletics"):
        MC "Absolutely! I'd feel right at home, since I already exercise a lot."
        show GTS_S happy-2
        GTS_S "I knew it'd be perfect for us. You're already so disciplined in your health, you'll be incredible at it."
    else:
        MC "It's not exactly my strong suit, but I'd be willing to give it a try."
        GTS_S "I applaud your willingness to adapt and try things outside of your comfort zone, Kei-chan."
    MC "Which martial art were you considering, though? There are a lot of courses to choose from."
    show GTS_S surprised
    "Naomi's eyes widened in surprise as the excessive force from her leaning caused the bench to dent and slide away from her."
    "Thankfully, it didn't break. It was built to withstand growth factors, after all."
    "I saw Naomi's breathing briefly quicken and panic, but once she saw that she didn't cause any major damage, she looked relieved."
    show GTS_S neutral-2
    GTS_S "Admittedly, I didn't consider that. I enjoy Karate and Taekwondo, but considering that Tai Chi is the least... well, combat focused, I imagine they'd be far more accepting of someone of my size."
    MC "Sounds like we've got a plan, then. Would you like to see if there are any Tai Chi clubs available after school?"
    hide GTS_S
    show GTS wink
    GTS "Absolutely. I'm eager to see if they'll still accept me."
    MC "If they don't, they aren't exactly accommodating your factor. I mean, they still let Honoka play volleyball."
    "Naomi covered her mouth as she rose to her full height once more, letting out a deep and imposing laugh."
    hide GTS
    show GTS_S unique-2
    GTS_S "Very true. Let's go."

    scene School Exterior with fade
    "Naomi guided me to the recreation area behind the school. She intentionally shortened her strides so that we could walk alongside each other. The afternoon sun was almost perfectly above us, so Naomi's shadow was as short as possible."
    "It was funny, seeing the shadow of such a tall person only as big as me. Naomi's pace allowed her to control the force of her limbs, softening the miniature earthquakes I had heard before."
    "Once she stopped at the bulletin board posted along the side of the school, she stood still with both of her feet shoulder-width apart."
    "We could see various other clubs being held in the recreation area as well. Students of all shapes and sizes were out playing soccer, lacrosse, tennis, and basketball. It was surreal seeing just how accommodating they were for students of such varied sizes!"
    show GTS neutral:
        xpos 0.0 xanchor 0.5 yalign 1.0 xzoom -1.0
        linear 2 xpos 0.5
    GTS "Are there any openings for a martial arts class?"
    "Naomi peered over my shoulder as I looked through the bulletin."
    MC "There is an opening for a Tai Chi class, as a matter of fact. Led by a... Kutabaro Ono, looks like."
    show GTS happy-2
    GTS "Does it say there are any height restrictions?"
    MC "No height restrictions. We're in luck."
    "Naomi sprung up from her leaning position. She straightened her knees with a slow, heavy bound as she jumped in excitement. She was airborne for about one second before crashing down onto the dirt with a mighty earthquake."
    "The force of her jump was so strong, I stumbled backwards and bent my knees."
    show GTS happy
    GTS "That's excellent! We'll be able to coordinate! It'll be so refreshing to have a class outside of the quarry."
    "It was strange seeing Naomi so expressively happy! She wasn't usually so dramatic."
    MC "You certainly seem happy about that!"
    show GTS neutral
    GTS "I am, Kei-chan. Believe me, I am. I'll need to adapt to my new body, of course. That much is inevitable. Being able to reteach myself how to move while also getting to do something I love is miraculous."
    show GTS happy
    GTS "I'm so, so thankful that we've got an opportunity like this!"
    "I picked up the attached pen next to the bulletin board and neatly wrote my name upon the sign-up sheet."
    show GTS neutral-2
    "Naomi did the same, using her recent calligraphy skills to write her name using the undersized pen. It looked more like a piece of chalk between her fingers, yet she wrote the kanji flawlessly."
    MC "I suppose we'll be seeing each other every week, then."
    show GTS aroused
    GTS "You mean aside from the time we usually spend together?"
    "I let out a brief laugh, copying Naomi's movements by covering my mouth."
    MC "Exactly."
    hide GTS
    show GTS_S neutral-2
    GTS_S "Would you like to do anything else this afternoon?"
    MC "We could walk around campus, if you like."
    show GTS_S unique-2
    GTS_S "Certainly. Lead the way."
    "Naomi and I shared each other's company for the rest of the afternoon. It was incredible how well we had learned to walk in sync. Part of me hoped that it would stay that easy, considering Naomi's factor."
    "That didn't matter for the moment, though. All that mattered was us, here and now, enjoying the immaculate spring air."
    jump daymenu

label GTS040:
    $setProgress("GTS", "GTS041")
    scene Dorm Interior with fade
    MC "Ooh, suck that crit down babycakes."
    play music Schoolday
    "Two o’ clock on the hottest Sunday afternoon since summer began. My scuffed-up old copy of Silver Moon was spinning away in my Aystation and Typhon was down to a third of his health. I couldn’t remember the last time I got that far."
    "Golden sunrays shone in piercing the glass and the curtains; the angels themselves were witnessing me."
    MC "Oh what the hell, now you get {i}three{/i} turns?"
    "Lest my confidence drown me, I suddenly found half my party poisoned and the other half knocked out."
    "I slumped backwards onto the floor while hissing a sigh through my teeth, as if I were pneumatic. There I formed my own dark sun, with hair spread out a meter in every direction as I formulated my strategy."
    MCT "Oy, I gotta get this cut before tomorrow... huh?"
    "I didn’t hear, but saw a disembodied backpack slip inside the slightly-opened balcony door,"
    show RM sad with dissolve
    extend " followed by my grimacing roommate."
    MC "Utagashi-san."
    show RM neutral
    RM "Hotsure-san."
    MC "Lock broke?"
    RM "A situation arose, and I adapted."
    MC "Uh huh. I’ll call the maintenance guy after I’m done with this boss."
    show RM angry
    RM "No, don’t do that. If you must know, Matsumoto's on patrol right out in front of the dorms, and I’d rather not have her rooting through my notebook. I doubt she’ll fall for a decoy twice."
    MC "So is it, like, actually possible to get expelled from here?"
    show RM neutral
    RM "Not for that, no. Now, I’ve got some things to work on."
    MC "You do that."
    hide RM with dissolve
    "He sat down at his desk and began laying out notes and assorted colors of pens; I, too, sat up and beheld the disarray before me on the TV."
    MCT "Hmm..."
    pause 1
    MCT "I wonder how Naomi-chan’s doing..."
    "I took out my phone."
    MCCell "<hey Naomi-chan, how are u doing?>"
    "I laid it down again and returned my attentions to the ongoing battle; it buzzed a couple minutes later."
    GTSCell "<Quite well, Keisuke-kun, thank you. You’ve just caught me in the midst of some reflection. How are you this lovely day?>"
    MCCell "<pretty good thx, playing some video games>"
    pause 0.5
    GTSCell "<It certainly is a day for indoor diversions. I trust your other affairs are in order?>"
    MCCell "<yeah don't worry>"
    MCCell "<what are u thinking about?>"
    pause 0.5
    GTSCell "<The view around the facilities today reminded me of when I was little, when my mother would read me fairytales.>"
    MCCell "<ha ha that's sweet, my mom used to tell me fairytales too>"
    pause 0.5
    GTSCell "<They can be very edifying for a child. More than that, there's a certain magic to them that seems broadly lost on modern literature.>"
    MCCell "<there is, isn't there?>"
    stop music fadeout 3.0
    "As I waited for her reply, I reached for the remote and clicked the raging battle into black silence. I stood, checking my pockets, and headed out the door."

    scene Dorm Hallway with fade
    play music HigherEdu fadein 2.0
    GTSCell "<Did you have a favorite book in your childhood?>"
    if isHighestSkill("Athletics"):
        "I tapped my phone, chewing the inside of my cheek."
        pause 0.75
        MCT "What was that one mom made me read?..."
        MCCell "<I forget the title but theres this one book about shun sakurai>"
        MCCell "<u know, the hitter for the koi?>"
        pause 0.5
        GTSCell "<I’m afraid I don’t follow baseball much.>"
        MCCell "<I didn’t think u did>"
        MCCell "<it made me appreciate his achievements tho reading how hard he worked to get there>"
        pause 0.5
        GTSCell "<A wonderful thing, indeed.>"
    if isHighestSkill("Art"):
        $setFlag("GTS040_art")
        MCCell "<well.. it’s not really a traditional book>"
        MCCell "<when I was 10 I got this like booklet for making little charms with bottlecaps and glue>"
        MCCell "<i ended up making a ton of them and tomo-chan even pitched in a couple times>"
        MCCell "<it was kinda cheesy but I ended up making lots of crafty projects like that>"
        MCCell "<after I destroyed all the soap in the house trying to carve figurines my dad just bought me a sketch pad lol>"
        MCCell "<srry for the wall of text>"
        pause 0.5
        GTSCell "<Not at all, Keisuke-kun.>"
        GTSCell "<I think it’s perfectly lovely that you’ve been in touch with your creative side for so long.>"
        MCCell "<thank you>"
    else:
        MCCell "<this is gonna sound weird but do you remember that book you were reading about Nijō Yoshimoto?>"
        pause 0.5
        GTSCell "<Of course.>"
        MCCell "<well when i was starting high school i had this book about famous buildings around the world>"
        MCCell "<the gugenheim museum, the sydney opera house, stuff like that>"
        pause 0.5
        GTSCell "<I could see how that could be interesting, in that light. Was there anything in particular you enjoyed about it?>"
        MCCell "<there were some pretty interesting stories about the history behind them>"
        MCCell "<I guess what really grabbed me was the sections about what went into the design of each one>"
        MCCell "<its kinda crazy how something as big as a building can be practically a work of art>"
        pause 0.5
        GTSCell "<Most certainly. I would imagine that much fine detailing goes into designing such a thing.>"
        pause 0.5
        GTSCell "<It's a bit ironic, but it takes as delicate a hand as any high art.>"
        MCCell "<tru>"
        MCCell "<you could say that's what civilization boils down to>"
        MCCell "<a roof over your head, and striving for a better roof>"
        pause 0.5
        GTSCell "<That rather sum things up these days, doesn't it?>"

    scene black with fade
    pause 1
    scene Dorm Exterior with fade
    MC "Bruhhh..."
    "I stepped out of the dormitory entrance hall and straight into the armpit of summer, where its glaring sun, wavering air, and shrieking cicadas scolded my intrusion."
    MCT "All this hair isn’t so bad sometimes..."
    "I glanced ahead of me to the path to the main building, which I headed down as I resumed typing."
    scene Campus Center with fade
    MCCell "<how about you, what was your favorite book?>"
    "The screen was tantalizingly still for many moments."
    GTSCell "<I will tell you, but I hope you won’t find it too terribly common.>"
    MCCell "<nothing about you is common, Naomi-chan. please do share>"
    scene black with fade
    pause 1
    scene School Front with fade
    GTSCell "<It was a romance novel. A period piece, as I’m sure you’ve guessed.>"
    pause 0.5
    GTSCell "<I remember being perfectly entranced by how the characters were written; the more you learned about them as people, and the more they did about each other, the closer they grew. It was absolutely wonderful.>"
    if getFlag("GTS040_art"):
        pause 0.5
        GTSCell "<Moreover, much like your favorite, it wasn't just the book itself that sealed its place in my memory.>"
    else:
        pause 0.5
        GTSCell "<However, that was not the only element to elevate it to its place in my memory.>"
    GTSCell "<I had to wait quite a while to read it, you see. Whenever I wanted to read a book, first my mother had to do so herself. Usually she would only skim chapters, but apparently it rather cast a spell on her as well.>"
    pause 0.5
    GTSCell "<Of course that heightened my anticipation tremendously.>"
    scene Hallway with fade
    MCT "Wait... what?"
    "I began typing a reply, at the sight of which Naomi's three blinking dots vanished."
    MCCell "<wait why did your mom read your books first?>"
    pause 0.5
    GTSCell "<She was simply doing her part in raising me properly. In theory, if she came across any iniquitous or disturbing themes, I would be spared exposure to them.>"
    menu:
        "<i guess that makes sense>":
            jump GTS040_c1_1
        "<dont you lose something when all youre exposed to is sunshine and rainbows?>": #This choice will contribute towards unlocking the Nun, Rebel, and Lady endings.
            jump GTS040_c1_2

label GTS040_c1_1:
    GTSCell "<Of course, Keisuke-kun. Worry is seldom useful and often misplaced.>"
    jump GTS040_c2

label GTS040_c1_2:
    GTSCell "<That's quite the leap. My parents well knew that unpleasant realities are necessary to one's moral constitution. They simply did not allow me to wallow in them.>"
    MCCell "<individually scanning books for objectinable content tho?>"
    MCCell "<that seems like a step or two beyond looking after your kid>"
    pause 1.0
    $setAffection("GTS", -3)
    GTSCell "<If I previously failed to impress upon you how dearly I hold my family, I would again ask you to show more respect for them.>"
    MCCell "<your right, sorry>"
    MCCell "<so, you were saying?>"
    jump GTS040_c2

label GTS040_c2:
    pause 0.5
    GTSCell "<Right, as I was saying, even after I finished reading it, my mother and I would continue to talk about it in our idle hours for more than a year, perhaps two.>"
    pause 0.5
    GTSCell "<We'd never quite bonded so intimately before; it was like she was my schoolmate. I came to understand her like I never had prior.>"
    scene Library with fade
    MCCell "<awww, that's pretty sweet>"
    MCCell "<what was it called?>"
    "I scanned the sparsely-populated library for a moment as I waited for her reply."
    GTSCell "<'By Your Word', if I recall correctly. But I am quite certain of that. It was by one Yoko Yoshimoto.>"
    MCCell "<oh, cool. what was the plot like?>"
    "I stowed my phone in my pocket as she answered and got to work strumming my fingers along the rows of books, gritty and fibrous hardback intermingled with smooth, fresh plastic sheets."
    MCT "Okay, she’s probably gonna be near the back, let’s see..."
    MCT "Ha... fu... mi... yo!"
    MC "Da da da da..."
    MCT "Hmm... {w}Crud... must not be here."
    "I picked up my phone again to see the fine-pointed essay that surely awaited me in the couple of minutes I was idle.{w} There was none."
    GTSCell "<You know, I do wonder if perhaps it would be better if we spoke on the phone.>"
    "After kicking myself for thinking I was slick, I pounded out a quick reply."
    MCCell "<id love too but first i gotta go somewhere else Utagashi-sans working on stuff>"
    pause 0.5
    GTSCell "<Of course. Hearing your voice shall be all the sweeter for the wait.>"
    MCCell "<back atcha. call you in a few>"
    "I fought back a blush as I stared down at the black screen, but my reflection reminded me it was time to improvise."
    "My eyes pivoted to the children's section..."
    MCT "Kinda obvious... might be a little gauche..."
    pause 0.5
    MCT "Did I just think the word 'gauche'? Who am I anymore?"
    "I clicked my tongue softly as I set about looking for an adequate replacement."
    "And then, my strumming finger fell on a certain tome, as no similar label felt quite right; its life of many loving embraces had left it a mottled spine, frayed edges, and pages clumped into jagged stacks."
    "A little assured, I eased it out from amongst its neighbors and proceeded to the front desk."
    scene black with fade
    pause 0.5

    scene Field with fade
    "It didn't take long to reach a point where I was secluded enough to call her; the campus had grown even more sparse, and the road to the giants' facilities was alone but for the ghosts shimmering and wavering over the ground."
    "Apparently, I was just about the only idiot willing to go outside that day. But I did take some comfort in the fact that I was never really alone anymore. She was much quicker to answer this time."
    GTSCell "Good afternoon, Keisuke-kun. Pardon my delay in answering."
    MCCell "Oh, don't worry about it. For you, I'll wait however long I need to."
    GTSCell "Hmhm, I appreciate your understanding. "
    GTSCell "Operating my phone has become rather... troublesome of late."
    MCCell "...Oh... I see."
    menu:
        "Maybe you’re turning into an old lady? Like, faster than normal.":
            GTSCell "Even under the circumstances, that seems rather improbable, does it not?"
            MCCell "The evidence seems pretty unassailable. I mean, we know you’re majorly into gardening. Have you noticed any white hairs? What’s your stance on doilies? Or Nortfight dances?"
            GTSCell "I haven’t noticed any such thing, no. I’ll be sure to check again after this conversation."
            GTSCell "And I happen to have a good deal of respect for the craftsmanship and visual aesthetic of the doily, though I myself prefer other modes of ornamentation."
            GTSCell "...I confess, before I offer an opinion, I must ask precisely what a ‘Nortfight dance’ is."
            MCCell "Eh... honestly I don’t think knowing would enhance your life."
            GTSCell "I do find myself inclined to believe you."
            jump GTS040_c3
        "I guess it was just a matter of time. Do you know if they can provide you with a replacement?":
            GTSCell "I believe I have heard that they can. I shall have to see about that soon."
            MCCell "Good, good."
            MCCell "..."
            MCCell "So, can I ask you a weird question?"
            GTSCell "Whatever you please."
            MCCell "Of course there’s a lot of downsides to your factor. What are some of the good things? The silver linings?"
            "She was silent for a moment or two."
            GTSCell "That’s a rather good question, as a matter of fact. It is important, after all, to be mindful of the narrowness of our perceptions."
            pause 1
            GTSCell "Hmm..."
            "I wiped my wrist across my damp forehead, smiling."
            GTSCell "Well, when my family came to visit and I looked down at Kimiko, it was just like she was a puppy again. That brought back some fond memories, indeed."
            GTSCell "...As discomforting as it is to reflect on, having a new perspective on the world around oneself is edifying, in some ways."
            MCCell "I bet. Ever look up and wonder what’s going on in the canopy of the trees?"
            $setAffection("GTS", 1)
            GTSCell "Hmhmhm, so I have."
            GTSCell "I also wonder... what do you think of it?"
            MCCell "Of... your factor?"
            GTSCell "Yes."
            MCCell "I...{w} uh, kinda like it."
            if getSkill("Academics") > 3:
                MCCell "It fits you, in a weird way."
                GTSCell "I'm not sure I take your meaning."
                MCCell "Just all the things that make you someone you can look u... uh... "
                MCCell "Like, I'll say it again, you're one of the nicest, sweetest girls I've ever met. Maybe it's not so bad if, you know, your presence can be felt a little more."
                GTSCell "Thank you. I wouldn't want to forget my virtues for anything."
                GTSCell "I confess it is something that worries me, in my more idle moments. My tai chi lessons are no small help in developing self-control..."
                GTSCell "...But as necessary as these facilities are, it seems impossible to put what I'm learning into practice where it is truly needed."
                if getSkill("Academics") > 6:
                    MCCell "Like you can't help but think of all the divisions in your life."
                    $setAffection("GTS", 3)
                    GTSCell "That is {i}precisely{/i} what I was thinking."
                    GTSCell "I have been making an effort to meditate more often, as well. I must only trust that in time it all shall not seem so daunting."
                    jump GTS040_c3
                else:
                    MCCell "Yeah... that sucks."
                    jump GTS040_c3
            else:
                MCCell "I always thought you were really beautiful, and it's sorta like I'm always noticing new things about you."
                GTSCell "That's very sweet of you to say. I have rather made a vice of missing the forest for the trees of late..."
                jump GTS040_c3

label GTS040_c3:
    "I heard a whisper of a sigh come through, as though she'd pulled away."
    GTSCell "But let's not dwell on that particular conundrum. I pray you're still well."
    MCCell "Doing fine. Perhaps a bit more affected by the heat, but... that's okay now."
    GTSCell "Hmhmhm, I'm glad. Be sure to stay near a drinking fountain, now. Dehydration is a very real danger at these temperatures."
    MCCell "Waaay ahead of you. I just got done chugging some primo cloud juice."
    GTSCell "Ah, how I missed your turns of phrase."
    MCCell "Heh... well..."
    MCCell "Hey, you were gonna talk about that book, right?"
    GTSCell "Indeed I was.{w} Well, where do I begin?"
    scene Chukan Point with fade
    "Now, maybe I wasn’t the greatest listener."
    "As Naomi got deeper into the story, I realized however many years had passed, she still knew it like her hometown, its turns and loops and landmarks which had bucked me a few chapters ago."
    "Nevertheless, I looked out over the scintillating colors of the horizon around the hilltop, and sighed. Beauty seemed to follow her everywhere."
    GTSCell "Now, if I were to name my favorite part of it, it would undoubtedly be the climactic chapter. It's especially memorable for me because my mother made a day of reading it."
    MCCell "Really? How'd she do that?"
    GTSCell "It was nothing terribly presumptuous. She took me to Okazaki Park... in Kyoto, that is. She found a lovely patch of shade under a tree, in sight of the Heian shrine, and laid down a sheet for us."
    "She chuckled."
    GTSCell "Getting the sheet to stay put took some doing. It was quite breezy that day."
    pause 0.75
    GTSCell "Please do nudge me if I should start to talk in excess."
    MCCell "You're fine, Naomi-chan. Please continue."
    GTSCell "Thank you."
    GTSCell "Well, the novel's denouement took a rather unexpected turn. On the eve that the hero was to be sent off to live with a distant relative..."
    GTSCell "The heroine snuck into his family's estate, confessed her love for him with {i}impeccable{/i} eloquence on the author's part, and stole him away in the night back to her own family's estate."
    MCCell "...Wow.{w} Obviously I'm not really into that genre, but it sounds like it must've been really moving."
    GTSCell "Hmhmhm, so it was, ever so much. I was forced to ask my mother to pause for a moment so I could regain my composure."
    MCCell "Heh."
    GTSCell "I was thirteen then, and to this day it remains my favorite work of fiction."
    scene black with fade
    pause 1

    scene Field with fade
    "I held my phone away to wipe my brow one more time and puff out a sigh. Just behind the shimmering veil, the giant facilities were starting to come piecemeal into view."
    MCT "Alright, just a little ways now..."
    MCT "...Wait, I can't just show up dripping sweat all over. Shit..."
    "And as I looked over my shoulder at how far I'd come, I realized I didn't have much of a choice."
    MCCell "So what was the ending like?"
    GTSCell "That was also rather unexpected."
    GTSCell "I suppose it shouldn't have been, really, but in the end, filial duty prevailed. After a night of elopement, the hero of the story returned to his family to embark on his journey."
    MCCell "And the heroine?"
    GTSCell "Did her duty, as well."
    GTSCell "Oh, what's the word?... it sort of glossed over scenes from the few years they were apart, how they each got along. Until, one day, he showed up at her gates again."
    GTSCell "Well, I haven't quite done it justice, but that was the long and short of it."
    scene Giant Dorm Exterior with fade
    MCCell "Oh, so sort of a vague, sudden ending. I take it it was still satisfying?"
    GTSCell "Oh, quite. When we finally finished the book, my mother asked me what I thought about the ending. It was a bit like a koan."
    "Stepping up to Naomi's door, I held my knuckles over it."
    MCCell "Oh, interesting. And what {i}did{/i} you think of it?"
    GTSCell "Well, I-"
    play sound Knock
    GTSCell "Ah!"
    GTS "{size=-6}Hello?...{/size}"
    "I hung up and tucked my hands behind my back, seconds before Naomi opened the door with muted grace."
    show GTS surprised with dissolve
    pause 0.5
    show GTS unique
    GTS "Keisuke-kun, did you walk all the way through this dreadful heat just to visit me?"
    MC "Pssh, of course. I hope I'm not interrupting anything."
    show GTS neutral
    GTS "Not at all. Do come in, I'll get you some cold water."
    MC "Thanks, I... could sure use it."
    scene Giant Dorm Interior with fade
    show GTS neutral with dissolve
    "Giving me a wide berth, she trotted over to her sink and produced from the cupboards what looked like a shotglass between her fingers. The sides of the glass were already fogging up as she walked it back over to me."
    GTS "I hope you'll pardon my lack of preparation."
    MC "Oh, none of that. I never told you I was coming, did I?"
    GTS "Well, indeed."
    GTS "And, pray tell, is there a reason you brought that book over?"
    MC "Uh, oh, you... saw..."
    MC "Heh... I guess I didn't account for the angle. Well... I thought we could pass an hour or two reading it together. Or, uh, I could read it to you."
    show GTS happy-2
    "I held it up for her to see, and watched her lips upturn and her stooped breast shudder with soft laughter."
    GTS "I think that's a lovely idea. Here, let me set it on the couch."
    show GTS neutral at Transform(xzoom=-1):
        ease 2.0 xpos 0.8
    MC "Thanks. Lemme just grab a washcloth or something and I'll at least dry off a little."
    show GTS neutral at Transform(xzoom=1)
    GTS "Oh, allow me."
    show GTS neutral at altMove(0.5, 0.6)
    "She daintily plucked a dish cloth from one of her kitchen drawers and turned to kneel down in front of me; it was funny, if not a little baffling, to realize she was still about double my height as I gazed into her navel."
    "Not showing a bit of concern, she put one hand behind my damp mane while the other brushed the towel-sized cloth across my brow, temples, and cheeks."
    MCT "Seems like yesterday she was 'only' twice my height fully standing up..."
    MC "Mm, thanks, that feels a lot better. You're very gentle."
    GTS "The pleasure is mine. Now, would you like to sit down?"
    MC "Ladies first."
    "She sat herself down with the book in her lap, and glanced at me hoisting myself up for a moment... I hardly noticed, focused as I was on keeping my drink level... before she turned the book over and stared at the back cover."
    MC "Yeah, I figured you might not be quite as comfortable reading that on your own."
    show GTS pondering
    GTS "What a coincidence that you should bring that up. It is rather odd, but I don't seem to have any trouble reading normal-sized text."
    MC "Really? At all?"
    GTS "Well, I still cannot read it at a greater distance than I could before, but yes. I comprehend the text on the spine perfectly well just holding it in hand."
    show GTS embarrassed
    GTS "Although turning the pages is another matter entirely."
    show GTS neutral
    GTS "That is why I would be quite delighted if you would care to do it in my stead."
    MC "I aim to please."
    "I took the book from her outstretched hand... well, outstretched over her lap... and took a sip of water before I scooted up against her hip and flipped to the quaint illustrations marking the first tale."
    GTS "Ah, Momotaro. I always did love that one."
    MC "Heh, it's a classic."
    "I cleared my throat as Naomi laid her arm down at my side, one pointer finger mostly covering my thigh, and I held it at as perfectly neutral an angle between us as I was able to perceive. I paused, heard her breathe in."
    MC "Once upon a time..."
    jump daymenu

label GTS041:
    $setProgress("GTS", "GTS043")
    play music DayByDay
    "More frequently than ever, I found myself going straight over to the Giants' Dorm after class. I didn’t even need a call from Naomi."
    "She didn’t mind me coming by; she treasured my company just  as much as I treasured hers."
    "Normally when I came over, we didn’t tend to do much. If we did, it was small things, pun intended, like homework, cooking, or just watching a show I could stream from my phone onto her tv."
    "Today however, was a bit different..."
    scene Giant Dorm Interior with fade
    show GTS neutral with dissolve
    GTS "Kei, could you tell me which color you think looks better? The red,"
    show GTS neutral at Transform(xzoom=-1)
    extend " or the blue?"
    "She put each dress in front of her, swapping between the two."
    MC "They’re both quite flattering. The blue matches your personality, while the red has a sort of fierceness to it."
    show GTS neutral at Transform(xzoom=1)
    GTS "Fierceness? I don't think I want to project that image. I don’t want anyone to think I’m scary."
    MC "Not that kind of fierce, more of the..."
    MCT "I’m gonna expose myself saying this, won’t I?"
    GTS "..."
    GTS "Oh, well I’ll just keep that in mind, the blue will do just fine then."
    MCT "Smooth is not my middle name apparently."
    "Naomi disappeared into her bedroom and reappeared in the blue dress, which to say was form fitting would be an understatement."
    "The dress was probably a few sizes too small and was hugging every inch of her body that the poor fabric could reach."
    MC "Is that comfortable? Looks a little tight."
    GTS "It’s a little tight, but it should be fi..."
    stop music
    show GTS surprised
    "*{i}RIIIIIP{/i}*"
    "In an instant, starting from the bottom of the dress, up her thigh and past her hips, the seams holding the side together gave out. Naomi flailed wildly to grab the two sides to retain some modesty."
    play music Sunset
    show GTS sad
    GTS "If you can excuse me for a moment.... I need to correct my appearance."
    MC "Take your time, I don’t mind."
    hide GTS with dissolve
    "With a glum expression she shuffled back into the bedroom. Eventually she reemerged holding the fallen garment."
    show GTS sad with dissolve
    MC "Where did you get that dress? Was it from Alice?"
    GTS "No, there is a small store inside the caverns that has some old clothes that previous students have donated. I was hoping this one was a bit looser, but I may have underestimated how much I’ve grown in the past weeks."
    MC "Is that the only place for giants to get clothes?"
    show GTS neutral
    GTS "There {i}is{/i} a shopping district that specializes in Giant clothing, but I haven’t made the journey to visit it."
    MC "It’s not too late. Would you want to go find this place?"
    "She glanced at the blue dress."
    GTS "I {i}would{/i} like to have more than just my set of school uniforms."
    MC "Do you have a map of the area?"
    GTS "We just need to follow the road that stretches northeast  towards the mountains."
    MC "Is there a thing with giants and mountains, or do I need to lay off playing Skyledge?"
    show GTS pondering
    GTS "I’m not sure why it’s there, but... that IS a rather ironic coincidence, yes. But pray tell, what is 'Skyledge'?"
    MC "It’s one of the video games I play. I can explain it on the way there if you’d like."
    show GTS happy
    GTS "I would love to hear about it if you would like to."
    MC "Um, one thing before we head off, would you mind... uh... carrying me?"
    show GTS pondering
    GTS "...May I ask why?"
    MC "I’ve been having a hard time keeping up with your pace. If we're gonna travel far, it may be better for you to carry me."
    show GTS neutral
    GTS "If you wish, I can do that for you."
    "She crouched down and let me step onto her hands."
    "The sensation as she lifted me back up was one I can safely say I’ve never encountered before. I’ve taken a plane before so the lifting sensation was similar, but the openness while experiencing this did rattle me."
    show GTS surprised
    "I noticed Naomi make a face of concern seeing my expression of shock. If she wanted to say something, she decided against it."
    MC "Alright, I’m ready to go. So, what would you like to know about Skyledge?"
    show GTS neutral
    GTS "The beginning will do."
    scene black with fade
    pause 1
    stop music fadeout 0.5

    scene Field with fade
    show GTS neutral with dissolve
    MC "...and you’re in a cart after being captured because you were crossing the border illegally. Once you’re in control, some guy says he's glad you are awake."
    GTS "I wish I could recall all that kind of stuff as well as you can."
    MC "I’ll be honest I’ve just played the game and the others in the series too much."
    GTS "Oh, I think that we are here."
    scene Giants Town with fade
    show GTS neutral with dissolve
    "I had been so caught up in my tale that I hadn’t noticed us reach the large gate. A pair of guard towers bracketed the gate."
    MC "You sure this is the place?"
    GTS "Someone had mentioned it was government run, but I’m not entirely sure."
    MC "I wonder how you actually enter."
    "Looking around, I spotted a large metal plate in the ground ahead of the gate."
    MC "You may need to step on that to get in."
    GTS "It seems rather odd to need someone to weigh a certain amount just to get some clothes."
    MC "I guess they suspect that if you’re coming here, then you are of a certain type. It’s likely put in place to keep non-giants safe."
    "As she gingerly stepped onto the plate, the sound of clicking could be heard. The gate slowly parted to reveal a road leading towards a cluster of buildings."
    MC "A rather curious place so far, a lot of odd security and engineering for a rather secluded place."
    GTS "It {i}is{/i} government run, so that would make sense."
    "Approaching the buildings, we could see more people walking around. While everyone’s height varied, I could guess everyone here exceeded 4 meters in height."
    show GTS pondering
    GTS "I’m surprised to see this many giants outside the dorm. I do wonder what the greater purpose of this place is."
    MC "Is there a more formal map of the area?"
    GTS "I don’t see one, but maybe we could  head over to that large shop at the end of the road ahead."
    "Looking down the road I noticed the building she was pointing out. It was by far the largest building in the 'small' town. The sign clearly read 'Mt.Fuji Outfitters' which was rather fitting for a place located in the mountains of the island."
    MC "That’s probably a good spot to head towards, seems popular."
    show GTS neutral
    GTS "I hope they may have some clothing as well, it seems like some sort of general store."
    "As we approached the store, the sheer size of the building was becoming more apparent. The entirety of the school could easily have fit in this place three or four times over, and that was what I could see."
    "The front doors slid open revealing a massive warehouse-like building. Everything from minute trinkets to whole TVs was on display, except these were five to seven times their normal size."
    MC "See any clothes? I can’t see a whole lot from here."
    GTS "I don’t see any from right here. Perhaps there's someone to talk to about finding them."
    MC "I don't think I'll be much help in that regard. I can barely see past these shelves."
    GTS "I can see a larger gentleman at a counter ahead of us. It’s safe to assume he’s an employee here right?"
    MC "That’s up to you, I can’t see to judge that."
    GTS "Oh right, apologies."

    scene Giants Town Store
    play music BrightLights
    show GTS neutral with dissolve
    "Going further into the store from my perspective brought on this feeling of truly entering a foreign world. Items that are so common to me are now taller than my entire body, or even taller than my house."
    "A feeling of alienation I could feel welling in my stomach, though there was another feeling I wasn’t sure how to describe in there as well."
    "As we rounded the endcap of an aisle, I found myself looking higher still. Ahead of me was a gentleman that towered even over Naomi. He was quite toned as evident by the muscles outlined by his button down shirt."
    UNKNOWN "Welcome to Mt. Fuji Outfitters. How can I help you, young lady?"
    GTS "Thank you, sir. My boyfriend and I were just looking for some more fitting clothing... for me, obviously. I can get my school uniform replaced, but casual wear is a little tricky."
    UNKNOWN "I understand, that was a problem when I went to Seichou as well. Never really could find a nice casual shirt or jeans."
    UNKNOWN "Come along, and I’ll show you our clothing selection. This place can be a maze at times."
    GTS "That would be appreciated. This is our first time here."
    "The gentleman looked over the counter to look down at me, before breaking into a smile and laughing."
    UNKNOWN "Apologies, it's rare that a normal sized person wanders in here. Especially one not associated with the government."
    "Stepping out from behind the counter, he began taking us through the winding pathways of the store."
    MCT "I think I wasn’t far off in assuming this place is much bigger then I assumed it was."
    GTS "If I may ask sir, you did say you went to Seichou correct?"
    UNKNOWN "I went there some years ago. I do wonder what the place looks like now."
    GTS "Are you by chance Akio Fumihiro?"
    Akio "I am, indeed. Where’d you get my name from?"
    GTS "You were much taller than everyone at the dorms by a good margin, and I recall seeing a name on the record wall that was above everyone else’s."
    Akio "I’m surprised that the record wall is still a tradition. From what I heard, the record wall was established by the class before me and only had about a dozen names or so."
    "When I left and recorded my name on it, there was a certain surprise since I was a head taller than nearly everyone."
    Akio "I take it I’m still the record holder?"
    GTS "Indeed, a few have come close I recall but none have surpassed you."
    Akio "Interesting, surprising that someone hasn’t grown past me."
    GTS "There is an upward trend with heights I observed."
    Akio "Guess it's only a matter of time until someone else takes the crown."
    Akio "Anyway, enough of my rambling and reminiscing. You were looking for some new clothes, well here we are."
    "Stepping aside he revealed rack after rack of clothing, all in sizes that could be measured in square footage of cloth."
    MC "Now {i}this{/i} is quite a selection."
    show GTS surprised
    GTS "Where do you get all the material?"
    Akio "The government may be difficult to work with, but they do have the supply line to provide the resources for an army, or in this case, a few giants."
    show GTS neutral
    GTS "So you work for the government?"
    Akio "Somewhat. I run the store, and they provide the goods that I have specified for sale. There's some other interactions but that's unimportant."
    GTS "Fair enough, it is rude to poke too much into another’s business."
    Akio "It’s fine, though I do need to return to the front counter. I hope you find everything you are looking for."
    "He waved and disappeared behind the shelves."
    MC "He’s quite nice. I didn’t expect him to also be the record holder."
    show GTS unique
    GTS "That was quite a nice surprise."
    MC "So were you only looking for a dress or were you looking for something else?"
    show GTS neutral
    GTS "A new dress would be good, but I did have some other things in mind. I wonder if they may have a new kimono? The one I used for dinner is getting rather short."
    MC "Possibly. You know, I’ve never considered if those are common items. I got mine a few years ago, but I can’t recall seeing them on a clothing rack at a store."
    GTS "It depends on the store, I would assume. Though you certainly have a point that they're a rather niche item outside of holidays."
    MC "What else were you thinking?"
    GTS "I may not be using the school's primary pool anymore, but I have heard of a spring in the caverns as well as a good beach spot. I wonder if they have bathing suits?"
    MCT "Please be bikinis. Please be bikinis. Please be bikinis."
    MC "I wasn’t aware there was a spring in the caverns. At least you haven’t mentioned it before."
    GTS "It's a warm spring, but I’d still need a suit. ...Ah, there they are!"
    "Past a few racks of pants was a single rack of just bathing wear. Like someone was listening above, every single option was a two piece suit."
    MCT "I think I just used up all my luck for the year, but so worth it."
    show GTS despaired-thought
    GTS "Oh, drat. I was hoping they had a one piece I could pick, but I suppose that may use a little too much material."
    menu:
        "I think you would look great in a two piece.":
            jump GTS041_A1
        "You might be able to order a one piece, but get a two piece till then.":
            jump GTS041_A2

label GTS041_A1:
    MC "I think you would look great in a two piece."
    show GTS sad
    GTS "You flatter me, Kei, but I’m not sure I’m comfortable showing that much skin to anyone else."
    MC "I hate to sound ignorant, but I don’t think you have a choice if this is their selection."
    GTS "You’re fine, I can see that my preferences aren’t possible with this selection."
    GTS "*sigh*"
    show GTS neutral
    jump GTS041_After_C1

label GTS041_A2:
    $setFlag("GTS041_A2")
    MC "You might be able to order a one piece, but get a two piece until then."
    show GTS pondering
    GTS "That may be, he did mention that he orders through the military. He might have a design I could order."
    show GTS neutral
    GTS "I’ll grab one of these in case he doesn’t. It’s not my preference, but I think I may be losing my ability to have a choice on these matters."
    jump GTS041_After_C1

label GTS041_After_C1:
    "She grabbed off the rack a plain white two piece suit, the bottoms had a sort of skirt on them which was quite flattering as I imagined Naomi strutting down the sand in it."
    GTS "This is a nice color. Can’t say I’ve considered a lot of white in my wardrobe outside of my uniform shirt."
    MC "I think it would look great on you."
    GTS "Then I guess it’s settled, can’t disagree with such an expert assessor."
    "She picked out a few more items before making her way back to the front counter where Akio was standing."
    Akio "I see you found everything you were looking for."
    if getFlag("GTS041_A2"):
        GTS "I was wondering if it would be possible to order a one piece swimsuit. I noticed you only had two pieces."
        Akio "I could but the price would be pretty steep. The material cost alone would be higher than 10 to 11 two pieces. Not to mention shipping time."
        GTS "Ah I see, then in that case this is fine."
    "He quickly scanned all the items before handing the bag back to us."
    Akio "Thank you.  I hope to see you again soon."
    "Naomi gave Akio a deep bow in appreciation."
    GTS "I suppose I will from now on. Thank you."
    "Exchanging parting waves, we began our trek back to the school."
    MC "I wonder what sorta lives await giants when they finish school..."
    GTS "Although it may sound bad on my part, I haven’t really looked into it. I was hoping that I would stay below the 4 meter threshold, but as we both can see that ship has sailed."
    GTS "I’d love to return to the mainland someday, but I fear I may not be permitted to."
    MC "I assume you mean ‘without resistance from the government’."
    GTS "Correct."
    MC "Yeah, that already brings up a lot of issues. I was surprised to hear how involved they are in the store."
    GTS "It was quite surprising, but considering how prominent they are in the dorms, I shouldn’t be."
    MCT "I do wonder how much the government will get involved as she grows taller."
    MCT "{i}Bleck{/i}. I’m starting to sound like Daichi now."
    "I was left to wonder as the sun finally set upon our return to school."
    jump daymenu

label GTS043:
    $setProgress("GTS", "GTS044")
    scene Hallway with fade
    play music HigherEdu
    "The day had finally arrived. Now that my usual classes were complete, I had made plans to begin the Tai Chi course with Naomi after school."
    "It was still the middle of the afternoon, so I had plenty of time to prepare. I decided to head to the locker room to fetch my uniform."
    "The tiles of the hallway floor let out a subtle tapping noise as I hastily made my way towards the gym."

    scene Auditorium with fade
    "Once inside, I made my way to the opposite end. The gym was lively with several groups of students and instructors. It seemed that they were preparing for their own after-school activities."
    "The girls' volleyball team was practicing in the center of the court closest to the front door, while the girls' basketball team practiced on the court closest to the locker rooms."
    "Aside from the few times I had watched Honoka participate in her clubs, it was the first time I had gotten a good look at each of the teams. Despite the vastly different array of factors on display, the instructors kept them coordinated."
    "Naomi had mentioned an interest in how well they managed the teams at Seichou Academy before. As I entered the locker room to retrieve my uniform, I remembered how thankful I was that we found the Tai Chi course."
    "After retrieving my uniform from the locker room, I neatly folded it inside a light blue duffle bag bearing Seichou's insignia."
    "I slung the duffel bag over my shoulder and returned to the hallway."

    scene Hallway with fade
    "I was just about to head back to my dorm, when I noticed someone familiar walking towards me."
    show FMG neutral with dissolve
    pause 1
    show FMG happy
    FMG "Oh hey, Kei-kun! What's that you've got there?"
    "Akira subtly gestured towards the bag on my shoulder. The sheer amount of muscle mass she was packing became much clearer as she held her forearm out."
    MC "Hi, Mizutani-san. It's just my athletic clothes."
    FMG "Oh, yeah? Are you planning on working out?"
    "Akira stared at me with a fiery, passionate expression. I could tell that she was clearly interested in this conversation already."
    MC "In a way, yeah. Yamazaki-san and I are planning to do some Tai Chi later."
    show FMG flex
    "She returned an even more passionate, excited expression. Akira was practically rumbling with anticipation as she heard me speak."
    FMG "You're gonna see just how much power Naomi's packing in her punch?!"
    MC "Well, Tai Chi is more about achieving coordination with your body. We're going to use it as a way for her to get used to her new size."
    MC "She needs to be able to step lightly when she needs to, after all. If she gets even larger, it'll be necessary."
    "I could see Akira's body language slowly relax, returning her to a more neutral level."
    show FMG neutral
    FMG "Ah, I gotcha. That makes sense. Still, aren't you a little bit curious?"
    MC "Curious? I suppose. Why, did you have something planned?"
    show FMG happy
    FMG "No, not really! But..."
    MC "...You want to test Naomi's strength, don't you?"
    show FMG surprised
    "Akira responded with a sarcastic gasp as she faked absolute bewilderment."
    FMG "No way! How'd you know?"
    MC "You seemed slightly interested in the idea."
    show FMG happy
    FMG "Well, I am! Admittedly, I've been interested ever since we learned our factors."
    play music PRG
    FMG "I just... haven't been speaking to Yamazaki-san much."
    show FMG sad
    FMG "When I learned that she'd been transferred to the other dorm, I was worried that I might have missed my opportunity. I wanted to get to know her."
    FMG "I've got respect for everyone, as long as they extend the same level of respect. Yamazaki-san was just so... refined, though. I didn't really know how to start, you know? Especially when it feels like our hobbies completely differ."
    FMG "I might not have really shown it when we found out, but when I learned that we'd still get to talk after class... I was really happy."
    FMG "I was happy that... we wouldn't have to say goodbye. That she'd still be close, and I'd still be able to become friends with her. Even if some of us rarely talk... I like our little group. I don't wanna lose that."
    show FMG neutral
    FMG "Ah... sorry. I rambled there for a bit."
    MC "There's nothing wrong with feeling passionate about your friends. I feel the same way, to an extent."
    show FMG happy
    FMG "Thank you, Kei-kun. I really appreciate that."
    MC "Would you like to see if Naomi wants to practice for a while?"
    show FMG neutral
    FMG "I'll ask, yeah! Do you think she'd want to break some boards or do some lifting?"
    MC "She's definitely more into cardio and balance training, but I did see her decimate the 'Test Your Strength' machine at the carnival..."
    show FMG flex
    FMG "Damn! I wish I coulda been there to witness it."
    MC "The attendant looked so confused. It was incredible."
    "I set my bag on the floor and pulled out my phone, sending a message to Naomi telling her where I was."
    MCCell "Mizutani-san wants to know if you'd like to get some practice in before Tai Chi class. Would you like to meet me behind the courtyard a little early?"
    "With the message sent, I placed my phone back into my bag."
    MC "I let Naomi know where we'll be. Are you ready?"
    show FMG happy
    FMG "You know me, Kei-kun! I'm always ready."

    scene School Exterior with fade
    play music HigherEdu
    show FMG neutral with dissolve
    "Akira and I made our way outside, taking the sidewalk behind the main school building. Within a minute, we had arrived at the field."
    "A large wire fence surrounded the corners. The field was originally designed to hold baseball games, but it also doubled as a spot for all of the outdoor after-school clubs to gather."
    "The rhythmic crunch of sand beneath our shoes punctuated our walk towards the center."
    show FMG happy
    FMG "This looks like a good spot. It's perfect for what I had in mind."
    "Akira quickly made her way to the other side of the field, walking towards a storage shed between the sand pit and the grass."
    show FMG flex
    FMG "Be right back! Don't move an inch!"
    hide FMG with dissolve
    "Despite how bulky she was, Akira managed to take off at a decent pace. She made it to   the storage shed across the field in seconds."
    "I had a few moments to myself. I decided to set my bag down and have a seat on one of the benches near the field."
    "With the weight now off my shoulders, I gave my neck a quick stretch before I paced around a bit. The slightly chilly breeze made my hair billow backwards."
    "I was only walking for a few moments before I saw a monolith coax itself around the walls of the school, delicately pacing itself while its long strides brought them closer to me."
    "Naomi wasn't a difficult person to spot, that was certain. I still lit up with happiness every time I saw her."
    show GTS neutral with dissolve
    "She was nearly as tall as the wire fence itself. She lowered herself slightly with a crouch, waving to me as she approached."
    GTS "Hello, Kei-chan."
    MC "Hello, Naomi-chan. I take it you saw my message?"
    GTS "I did. You said that Mizutani-san had some sort of practice planned?"
    MC "Yep! She saw me with the uniform, and she thought it'd be something fun to try."
    GTS "Knowing Mizutani-san, I imagine she--"
    FMG "Found 'em!"
    "Akira came running back with two large objects, one in each arm. They didn't appear to slow her down in the slightest as she galloped along the sand pit with both perched on her shoulders."
    show GTS neutral at Position(xcenter=0.8, yalign=1.0), Transform(xzoom=-1.0) with dissolve #slide ani?
    show FMG flex at Position(xcenter=0.2, yalign=1.0) with dissolve
    "Once Akira had made her way back to the center of the field, she lowered a large wooden stand to the ground to free up her right arm. The stand was painted black, with two long wooden prongs jutting out from the top to form a U-Shape."
    "Not finished, she then lowered her left arm to place a gigantic stack of wooden boards upon the sand. There had to have been at least 20 wooden squares in the stack, possibly more."
    show FMG neutral
    "With both of her hands now free, Akira stretched her left arm across her torso and patted her tricep with her right hand. She then repeated the process with her right arm and left hand."
    show FMG happy
    show GTS surprised
    FMG "Aww, yeah! Still got it!"
    GTS "A very efficient means of moving a lot of materials, Mizutani-san."
    FMG "THANK YOU! See, you understand it, unlike Masumoto-san."
    show GTS unique
    GTS "As long as you don't injure yourself, it seems like a great method. You're never supposed to lift without a spotter, correct?"
    show FMG neutral
    FMG "You should always have a spotter if you're planning on lifting your maximum, yeah. I thought this was light enough to do on my own, though. Regardless, we've got everything we need now!"
    MC "I actually haven't seen these board-breaking stands up close before. They're a lot smaller than I thought."
    show FMG happy
    FMG "Are you sure it's not because we aren't exactly to scale?"
    MC "Point taken."
    show GTS neutral
    GTS "Breaking boards is more of a taekwondo or karate thing, Mizutani-san."
    show FMG flex
    FMG "Right! What'd you say you were getting into, again?"
    show GTS embarrassed
    GTS "Tai Chi."
    show FMG sad
    FMG "...Oh."
    show FMG surprised
    "Naomi let out a loud, imposing giggle with her hand covered. Akira must not have been used to the volume, because it startled her just as much as I did the first time I heard it."
    show GTS happy-2
    GTS "It's perfectly fine, Mizutani-san. I'd be willing to try my hand at it regardless."
    "I could see Akira's brief moment of fogginess quickly recover. Within seconds, she was sporting her trademark smile again."
    show FMG happy
    FMG "Awesome! I'm... I'm glad."
    show GTS neutral
    "Akira placed one of the square boards atop the prongs of the stand,adjusting it to make sure it was centered. She slowly backed away from the stand, clearing the field for Naomi."
    "Naomi's giant, encompassing shadow stretched nearly halfway across the entire sand pit. Akira, completely unfazed, crossed her arms across her pecs and confidently smiled at her."
    FMG "We haven't really hung out like this before, have we?"
    GTS "I suppose we haven't. It's very fortunate that martial arts have brought us together."
    show FMG neutral
    FMG "I wanted to get to know you earlier, but then you got transferred to the giant's dorm and everything, so..."
    "Naomi slowly nodded as she listened to Akira speak. She looked like she was equally troubled by the situation."
    GTS "The move wasn't easy on my part, either. I had many worries of my own."
    FMG "I'll bet. I was pretty scared when I first discovered that I had a factor, but after a while I... learned to adjust and appreciate it more."
    show FMG sad
    FMG "Still, though. I totally get it. Adjusting to your new height isn't going to be easy. I might have problems with doorways, but you've got even more of a challenge."
    hide GTS
    show GTS_S neutral-2 at Position(xcenter=0.8, yalign=1.0), Transform(xzoom=-1.0)
    GTS_S "Kei-chan and Inoue-san have helped me cope. The medical staff offered sound advice as well, but setting my spirits at ease is another matter entirely."
    show FMG neutral
    play music PRGChallenge
    FMG "Mental health is tricky, Yamazaki-san. Even the experts have trouble explaining everything. That's why I always fall back to physical health. It's simple, concrete, and easy to understand."
    show FMG happy
    FMG "If you're fit and your body thanks you after a solid workout, well... everything else falls into place. That high you get when you finish your last set never fails to make me happy."
    hide GTS_S
    show GTS neutral at Position(xcenter=0.8, yalign=1.0), Transform(xzoom=-1.0)
    GTS "I imagine it's very similar to the feeling one gets after a long, effective meditation. That's very sound advice, Mizutani-san. Thank you."
    FMG "You're welcome! Now, put that advice to use and BREAK THAT THING!"
    show GTS happy-2
    GTS "All right, here goes!"
    "I watched as Naomi raised her right hand up to shoulder level while she crouched over the wooden board. With her size, the square panel better resembled a coaster."
    "I expected her to be able to snap the board without a problem, but Naomi's crouched position made it so that the apex of her swing wasn't in line with the board. She needed to settle for the end of the swing, where her strike would be weaker."
    FMG "You know, crouching over like that makes it harder to-"
    "SNAP!"
    "Nevertheless, the sheer amount of force carried by Naomi's oversized arms allowed her to effortlessly bisect the wooden square. Both halves fell onto the sand pit with a light thud."
    show FMG flex
    FMG "Oh, damn! She's unstoppable!"
    show GTS surprised #pondering
    "Naomi curiously looked at the two halves of the board. Despite opting for a sideways chop, the impact had completely caved the center of the wood in. The board looked as if it had been broken with a closed fist instead."
    GTS "I can definitely see why this is used for practice. It requires a certain amount of coordination just to hit your target."
    show FMG happy
    FMG "Yeah, and you nailed it! Your raw physical strength doesn't actually matter that much. It's all about the form of your strike and how well you can aim it."
    show GTS neutral
    GTS "That actually reminds me of the 'energy distribution' lesson from when I did other martial arts as a kid. The tiger was meant to symbolize fierce, powerful energy, whereas the crane represented gentle, balanced energy."
    show FMG neutral
    FMG "So I'm the tiger?"
    show GTS unique
    GTS "I think you're both, Mizutani-san."
    "Naomi bowed in a sageful manner."
    show FMG happy:
        xzoom -1.0
        linear 2.0 xpos 0.05
    "Akira then walked over to the pile of boards and picked up another square. She then returned to the stand and set it up once again."
    show FMG flex:
        xzoom 1.0
        linear 2.0 xpos 0.2
    FMG "All right, Kei-kun. You're up."
    "I gave Akira a small smirk before walking up to the board."
    MC "I can't possibly allow these boards to keep insulting me."
    show FMG happy
    FMG "Eliminate them with extreme prejudice! And violence!"
    "I squared my shoulders, lowered both of my hands to my sides, bent my knees slightly, then exhaled."
    "After a few seconds of breathing, I raised my right hand with my fingers locked together. I slightly bent my fingers as I quickly lowered my wrist, sending it directly into the center of the board."
    show FMG neutral
    show GTS happy
    "Akira gave a satisfied nod with her arms at her sides. Naomi smiled brightly in response. Seems like I managed to earn their respect with that one."
    FMG "Niiiice, Kei-kun. Very nice."
    GTS "A very respectable form, Kei-chan."
    MC "I'm glad I can still remember how to do that. That anticipation when you exhale... hooh. You were right, Mizutani-san. It's a wonderful feeling."
    show FMG flex
    show GTS neutral
    FMG "Right?! See, I told ya!"
    show FMG happy
    "Akira then smiled towards the pile of boards in a sinister manner."
    FMG "We've still got tons of boards, though... you wanna see how many Miss Powerhouse can smash?"
    MC "Powerhouse?"
    FMG "Yeah! I cleverly combined the height of a lighthouse with her sheer strength to create the perfect wrestler alias!"
    show GTS surprised
    GTS "'Powerhouse' is already a term by itself though, isn't it?"
    FMG "That only makes it even more fitting~"
    "Naomi tossed the idea around in her head for a few seconds, then let out a defeated exhale."
    show GTS embarrassed
    GTS "Oh, all right. Line up ten boards for me."
    show FMG flex #fired up
    "Akira then lit up with a fiery, blazing passion that I could only describe as... otherworldly. Defying everyone's assumptions, Akira took off like a world class sprinter and began vigorously stacking board after board upon the stand, aligning them perfectly each time."
    show GTS surprised
    "With the stand fully set up, Akira banged her fists together with a mighty lunge, then gestured towards Naomi with both of her pointer fingers aimed at the sky."
    FMG "Hyaaaaa! Give it everything you've got, Yamazaki-san! ANNIHILATE!"
    show GTS neutral
    GTS "Hooooh..."
    "Naomi corrected her stance from the previous attempt, bending her knees even sharper than she did before. She then lowered both of her hands to her sides with her fingers locked and thumbs pointed up."
    show GTS happy-2
    GTS "KYAAA!"
    "With a mighty roar, Naomi raised her arm. There was so much weight and winding force to her heavy, lumbering movements. Even a swift downward strike from her looked like it was moving in slow motion."
    "When her arm made a complete circle and sailed downward, her giant right hand cleaved through the stack of ten wooden squares like it was made of tissue paper."
    "The stack folded and buckled like an accordion, stray pieces of wood falling to the ground in sequence mere seconds later."
    "{i}CRACKLE!{/i}"
    show FMG surprised
    "The shockwave from Naomi's arms was enough to send the sides of the board stand tumbling over, leaving everything in a pile of dust. While the stand itself remained intact, the impact of the stand falling over kicked up a massive cloud of sand from the field."
    "The stray bits of yellow dust clouded up near the earth, then faded as the cloud of sand disappeared."
    "{i}Fizzle...{/i}"
    "Once the cloud disappeared, Akira and I stood in awe at the display of power we had just witnessed. Naomi was still following through with her heavy strike, exhaling proudly."
    FMG "Yamazaki-san... that was AMAZING!"
    show GTS embarrassed
    GTS "I'm very glad that you liked it, Mizutani-san."
    MC "Maybe ten was underestimating it."
    show FMG flex
    FMG "You raise a good point, Kei-kun! I'll get more!"
    show GTS neutral
    GTS "I believe that's enough power training for now, Mizutani-san. We need to get ready for Tai Chi very soon."
    MC "Oh yeah, that's right! We still have about half an hour, though."
    show FMG happy
    FMG "You two go get ready, then! I'm just happy we got to do this today!"
    show GTS unique
    GTS "Likewise, Mizutani-san.Thank you for proposing such a fun idea ."
    show FMG neutral
    FMG "See ya around, guys. We should definitely do this again sometime."
    show GTS neutral
    GTS "We shall, we shall. It was wonderful spending time with you."
    MC "Later, Akira."
    FMG "Later, Kei-kun!"
    hide FMG with dissolve
    show GTS neutral at Position(xpos=0.5, xanchor=1.0, yalign=1.0) with dissolve
    "The two of us waved Akira goodbye as we left the field. We could see her packing up the equipment she brought out as Naomi's long, powerful strides took her further away from the setup."
    show GTS embarrassed
    GTS "You know, I didn't think I'd be breaking boards today."
    MC "Can't say I thought I would be either. It was fun though, wasn't it?"
    show GTS neutral
    GTS "It was, yes. I'm glad I got to spend some time with Mizutani-san. I haven't really done so since the school year began."
    MC "She was really interested in you, it seemed. Akira gets along with everyone pretty well, but she seemed the most upset when she found out you were moving."
    show GTS surprised
    GTS "Really? I didn't know she felt that way."
    MC "Perhaps you should ask her about it the next time you see her."
    show GTS neutral
    GTS "Gladly. If Mizutani-san expressed interest like that, I should definitely return the favor."
    "The two of us spent a few more minutes talking while we prepared for Tai Chi. I already had everything  with me, but Naomi needed a few minutes to grab some things from her dorm."
    "I followed her back to the giant's hangars to make sure we had everything we needed."
    jump daymenu

label GTS044:
    $setProgress("GTS", "GTS045")
    scene Classroom with fade
    "At that moment, I was at peace with the world around me."
    "All that remained was total acceptance of the events to come."
    MCT "Yep, I'm boned."
    play music Schoolday
    "The test material? Organic chemistry. My notes? Three lines and a doodle of a molecule I could no longer name. My will to live? Eminently negotiable."
    HR "I'll say again, this material tends to trip people up. So all of you make absolutely sure you know these concepts like the back of your hands. Understood?"
    "His speech concluded, he dismissed class without another word."
    MCT "Well, looks like I got a night ahead of me."
    "I stood, glad to withdraw my arm from the ray of sunlight that had been creeping up my shoulder all through class."
    scene Hallway with fade
    "Filing out of the room, I resolved to head to the library to break ground in my head with hopefully minimal distractions. But first, with the sun-baked heat still wavering off my upper arms, I decided to stop by a drinking fountain."
    "One twist of my fingers, and a shimmering, cool, glassy arch sprouted up from the chrome spigot; I leaned down to drink."
    stop music
    "But I stopped."
    MCT "Hold on..."
    MCT "Naomi-chan said she was gonna text me after class."
    MCT "Odd, it's been a couple minutes...{w} probably going back to her room or something."
    play music MCGuitar
    "Without another thought, I drank a few hearty gulps of the wonderful coolness, some splashing on my chin, and went on my way."
    scene black with fade
    pause 1.5
    scene Library with fade
    if getSkill("Academics") > 7:
        MCT "Alright, I'm maybe kinda sorta starting to get this."
        "After skimming and re-skimming a couple times, I had filled in my notes a lot more, never mind the several times I wrote something down thrice for good measure. I felt, should I stay the course, that I would actually pass the exam."
        "I set to copying down a table of bond types in my own abbreviated notation, when another insight struck me."
    else:
        MC "Pssshhhhhh..."
        MC "It's on the tip of my tongue..."
        "It was not on the tip of my tongue."
        "Ten or fifteen minutes into my emergency study session, I was staring down at the exact same page of notes I came in with."
        MCT "The hell is chirality? Unless I start making meth there's no way I'd ever need to know this."
        MCT "Ugh, this would be so much easier with..."
        "And then a silence filled my ears."
    "I slid my phone out of my pocket and held it up, only to see my unadorned lock screen."
    MCT "Still nothing? Did she forget?"
    MCT "Wonder if I should say something..."
    menu:
        "Don't be clingy":
            jump GTS044_c1_1
        "Text her":
            jump GTS044_c1_2

label GTS044_c1_1:
    MCT "Mm, nah, it's probably nothing to get worked up over."
    MCT "She's a big girl, she can handle the little stuff."
    MCT "..."
    "Like a crazy person, I cracked a smirk amidst the speechless library."
    MCT "Might be a little early to be thinking about that..."
    MCT "God, my brain."
    "I absently tapped my pencil once or twice on my notepad and my smirk gently melted."
    MCT "God, my brain."
    "I continued, with the aid of a rapidly dulling pencil, to chip away at the text in a bubble of silence."
    "And then, my phone buzzed. There it was, Naomi's belated text; I didn't hesitate to lay down my lead pickaxe and read it."
    GTSCell "Good afternoon, Keisuke-kun. How do you do?"
    MCT "This is what she wanted to tell me all this time?..."
    jump GTS044_c3

label GTS044_c1_2:
    MCT "Yeah, I'm gonna say something. That's the responsible thing to do."
    "I held my phone over my study materials and got typing at once."
    MCCell "hey naomi-chan, i missed your text. something up?"
    "Naturally, I stared at a still screen for a few moments."
    if getSkill("Academics") > 7:
        extend " I tried to resume a little of my study for a moment while I awaited a response."
    GTSCell "Pardon me, Keisuke-kun. I should have said something earlier."
    GTSCell "During class I couldn't help but notice you were tugging on your hair a bit."
    menu:
        "Oh yeah, honestly I've been stressing a bit over this upcoming test.":
            jump GTS044_c2_1
        "Oh yeah, I've kinda developed a tic since my hair started getting longer." if getSkill("Art") > 3:
            jump GTS044_c2_2

label GTS044_c2_1:
    $setFlag("GTS044_meet")
    GTSCell "It is rather complicated material. Would you like to meet tonight and study, perhaps?"
    MCCell "i think that would help"
    MCCell "you wanted to say something else before tho, rigt?"
    MCCell "*right"
    pause 2
    GTSCell "Yes, I did."
    GTSCell "I don't know if you've since heard, but there will be a supermoon visible later tonight."
    GTSCell "We also seem to be due for a clear sky."
    GTSCell "I was going to ask you if you would like to view it together, but that can wait until you've properly fortified your notes."
    MCCell "i think i can probably finish up before it gets too late, we should be able to catch some of it"
    GTSCell "That would be very nice indeed. Just remember that your future comes first."
    MCCell "I understand. i'll finish this section, get my stuff together back at my dorm, and come over"
    GTSCell "I look forward to seeing you."
    MCCell "i look forward to seeing you, too"
    GTSCell "Out of curiosity, where are you right now?"
    MCCell "at the library"
    GTSCell "Ah, very good."
    GTSCell "Oh, by the way, how has your day been? Aside from the matter of the exam, of course."
    jump GTS044_c3

label GTS044_c2_2:
    $setFlag("GTS044_lie")
    MCT "I mean, it's {i}kinda{/i} true."
    GTSCell "Oh, I see. My apologies, I was wrong to presume."
    MCCell "don't worry, it's nothing"
    MCCell "there was something else you were gonna say before too tho, rigt?"
    MCCell "*right"
    GTSCell "Indeed."
    "Rapt, I watched the dots fade in and out as she composed her message."
    "Compose... a word thrown around a lot about so many emails and texts and interfaces. But there really was no other word for what Naomi did every time we talked."
    GTSCell "I don't know if you've since heard, but there is going to be a supermoon visible over the island later tonight as well as a nice and clear sky."
    GTSCell "Granted your essential tasks were complete, would you perhaps like to view the event with me? We could make an evening of it."
    MCCell "i'd love to. what time works for you?"
    GTSCell "Well, of course I wouldn't want you to be reprimanded for walking back to your dormitory past curfew."
    GTSCell "I thought we could instead view the event concurrently. Do you think you might enjoy that?"
    "It was at that moment that I realized that I had entered turbo overdrive dumbass mode."
    "A little more slumped than before, I put on a virtual happy face and typed my answer."
    MCCell "oh yeah good idea"
    MCCell "how long do you think you'll be up?"
    GTSCell "I will probably go to bed around midnight."
    MCCell "ok good"
    GTSCell "By the way, where are you right now?"
    MCCell "at the library"
    GTSCell "Ah, very good."
    GTSCell "Apart from the matter of the exam, how has your day gone?"
    jump GTS044_c3

label GTS044_c3:
    MCCell "pretty good, thanks."
    "I began typing again, until I saw her typing a reply. I stopped, and then so did she."
    MCT "..."
    MCT "Heh. Sweet as honey."
    MCCell "remember oyama-san? he came to class dressed as elvis."
    GTSCell "Pardon?"
    MCCell "he obviously spilled a ton of glitter on his only clean shirt so he popped his collar, slicked his hair back, and told everyone he was cosplaying"
    GTSCell "Goodness, what a sight. That must've been a delight to see in person."
    MCCell "me and about 18 followers agreed"
    GTSCell "I do hope you didn't identify the poor fellow by name."
    MCCell "nah nah course not"
    GTSCell "I'm glad to hear it."
    GTSCell "Too many forget all compassion for their fellow man once the proverbial screen goes up."
    MCCell "lol yeah"
    MCCell "how was your day Naomi-chan?"
    GTSCell "Rather well. I had been looking forward to talking to you today."
    MCCell "aww"
    GTSCell "I'm starting to get to know my neighbors as well. The young lady next door to me is a member of student council, which is quite interesting although it seems to leave her little time for chit-chat."
    MCCell "that's pretty cool. bet you'll be thick as thieves in no time"
    GTSCell "She has certainly made a good impression."
    pause 2
    GTSCell "I suppose I should leave you to your work."
    MCCell "probably should get back to it"
    if getFlag("GTS044_meet"):
        MCCell "see you tonight"
        GTSCell "I await the hour."
    else:
        MCCell "i'll call you tonight"
        GTSCell "Please do!"
        GTSCell "I'll talk to you then, Keisuke-chan."
    MCCell "see you later."
    "With the locking of my phone, my spirits were restored. I set my pencil back to paper and my finger to my chin, now a little surer that I had it in me."
    scene black with fade
    $setTime(TimeEnum.EVE)
    pause 2
    if getFlag("GTS044_meet"):
        jump GTS044_c3a
    else:
        jump GTS044_c3b

label GTS044_c3a:
    scene Dorm Interior with fade
    stop music
    MCT "Notebook, check, pencils and pens, check, umbrella, check..."
    MCT "Water bottle would be a good idea."
    MCT "Oh, right, the book."
    "With my backpack laden and no goodbyes to say, I headed out to the yellowed reaches of the giants' dorms."
    scene black with fade
    pause 1
    scene Giant Dorm Interior with fade
    show GTS neutral at Position(xpos=0.2, xanchor=1.0, yanchor=1.0) with dissolve
    "Naomi, after letting me in, stepped aside to gather some things from a middle shelf that I could probably touch standing tiptoe."
    GTS "It's good to see you again, Keisuke-chan, even if I might prefer more auspicious circumstances."
    MC "It could be worse, there could be two tests."
    GTS "Hmhm... there could be indeed."
    show GTS unique-2 at Transform(xzoom=-1) with dissolve:
        ease 2.0 xpos 0.7
    show GTS neutral with dissolve
    GTS "There we are. How far did you get on your own, exactly?"
    if getSkill("Academics") > 7:
        MC "121?... Yeah, 121."
        GTS "Oh my, you're almost done as it is. Well, what would you say to going on a bit of a stroll to pass the time afterward?"
        MC "I'd say it's a gorgeous night for it."
        GTS "I would wager we don't know the half of it."
        "I smiled as she sat down beside me on the oversized couch and began tracing her finger over my notes. The end was at last in sight."
        scene black with fade
        pause 1
        $setTime(TimeEnum.NIGHT)
        scene Mountains with fade
        $setAffection("GTS", 1)
        "Naomi had insisted on bringing her calligraphy set; sensing her intent, I brought my notebook and my freshly-sharpened pencil."
        "Our walk was ponderous, as for the first time I really took in the greener environs of the old strip mine; Naomi and I talked on things fond and shadowed on the occasion the view wasn't enough to grip us."
        "This was where she really belonged."
        "Eventually, with the sun disappeared behind its jagged black veil, we came to a stop before a sprawling sapphire amidst the crown of the mountains."
        jump GTS044_c4a
    else:
        MC "I think page 114."
        GTS "That's a decent amount of progress. Let's get started then, shall we?"
        "She sat down on the oversized couch beside me, punctuated by a palpable puff of air through the cushion beneath me. I half-smiled as she began turning pages one by one, with one finger on my notes."
        scene black with fade
        pause 1
        $setTime(TimeEnum.NIGHT)
        scene Mountains with fade
        "The sun had set by the time we finished, though my chances didn't seem quite so dim anymore. Naomi then proposed a stroll out to the surrounding wilderness before we sat down to stargaze."
        "Naomi insisted on bringing her calligraphy set; sensing her intent, I brought my notebook and my freshly-sharpened pencil."
        jump GTS044_c4a

label GTS044_c4a:
    show GTS happy with dissolve
    play music GTS
    MC "Would you look at that!..."
    MC "It's crazy how different the sky is this far out from campus, it's like..."
    show GTS neutral
    GTS "Night and day?"
    MC "Oh my, how {i}terribly{/i} common, Yamazaki no kimi."
    show GTS happy
    GTS "You ought to know that holds little sway with {i}me{/i}, Keisuke-kun."
    MC "I guess. Otherwise you wouldn't be dating me."
    show GTS neutral with dissolve
    GTS "Now {i}that{/i} is absurd."
    "She chuckled, as did I. I sat, as did she."
    show cg GTS044_stars1 with dissolve
    "It seemed every star ever given a name smiled down on her that shimmering night, along with their sisters and brothers suspended on the glassy sheen of the lake."
    "But the misty periwinkle sheen of the grass we sat on was all thanks to the moon above. ‘Super’ was right; it was bigger and brighter and a purer white than ever I’d seen, its divine glow casting the night into its own kind of day."
    "It occurred to me to look over to Naomi; her calligraphy set was nestled in the grass beside her, while she had settled into a meditative pose."
    menu:
        "Kiss her":
            jump GTS044_c4a_1
        "Join her":
            jump GTS044_c4a_2

label GTS044_c4a_1:
    "As quietly as I could, I eased myself to my feet and stalked across the grass, until I was directly beside her."
    "At the last instant I pounced, craning my neck up to kiss her warm, creased cheek."
    show GTS unique
    hide cg with dissolve
    "Her serene mask broke along with her focus to the sound of her girlish laugh."
    GTS "I suppose it was rather ungenerous of me to keep you waiting."
    MC "Oh, pshaw. I'm the one who can't keep my hands off you."
    MC "It reminds me of you, you know."
    show GTS neutral
    GTS "Oh?"
    "I pointed up."
    MC "Pure... always giving off light, looking down on everything with this... serenity, understanding. Unchanging no matter what happens down here on earth."
    show GTS happy
    MC "In a way it feels like you're with me everywhere."
    $setAffection("GTS", 2)
    GTS "Ohhh!"
    show GTS aroused
    GTS "Whatever I've done to earn such adulation, I haven't the foggiest."
    MC "Lucky you don't have to."
    "I cupped her chin in my hand, but she turned to face me anyway, leaning in for a kiss that didn't break for a precious few moments."
    "My hand slid down her arm as I sat down closer beside her. She sighed deeply into the night, gazing down at me with sleepy eyes."
    MC "So... what'd you want to do with your calligraphy set?"
    show GTS neutral
    GTS "Ah, right."
    jump GTS044_c5a

label GTS044_c4a_2:
    MCT "Perfect time for it, that's for sure."
    "I shifted my legs into half-lotus, folded my hands, and closed my eyes."
    scene black with fade
    pause 1
    MCT "..."
    MCT "..."
    MCT "..."
    MCT "I wonder what she's thinking about."
    MCT "..."
    MCT "..."
    MCT "..."
    if getAffection("GTS") > 70:
        MCT "Meh. None of my concern."
    else:
        MCT "Man, it's pretty out tonight..."
    $setAffection("GTS", 2)
    #pending approval, this choice gives weight towards the Nun ending
    "I continued to sit there, listening to the air blow in circles inside me. That is, until I heard a rustle in the grass at my side."
    scene Mountains with fade
    show GTS neutral with dissolve
    jump GTS044_c5a

label GTS044_c5a:
    "She picked the items up again out of the grass, wet her brush on the inkstone, and steadied her hand over the unfurled scroll."
    "I myself took the hint, and took up my pencil and paper before I began to really study the scene in earnest. Soon after putting lead to paper, I found myself lost."
    "Once or twice, I stole a glance at Naomi's vision as it emerged from the ink; she eschewed many details I thought essential, and yet, the consideration with which she laid each stroke left her in about the same place as me."
    "I looked up, some time later, to see the moon inched higher in the sky."
    MC "Hm... there."
    GTS "Ah, you've finished?"
    MC "I have. Shall we?"
    "Gingerly she set the scroll down beside her and I handed over my notebook; patches of ink still shimmered."
    GTS "Impressive... this is quite a faithful portrayal."
    MC "Thanks. I wasn't sure about the technique I used for the dark spots on the moon but I think it worked out in the end."
    GTS "Hmhm, I should say so. The level of detail you captured here, it's... mesmerizing..."
    MC "Heh, thanks. Now, what do we have here..."
    "My finger hovered, yearning but afraid to mar the thing before me."
    MC "Wow, this is..."
    if getSkill("Academics") > 4 or getSkill("Art") > 7:
        extend " hold up."
        "I leaned in, studying Naomi's brushstrokes slower and closer."
        MC "'Harvest moon: around the pond I wander, and'... That's from Matsuo-sama, isn't it?"
        show GTS unique
        GTS "Quite astute. Yes, yes it is."
        MC "You worked this into a painting? D- wow, Naomi-chan, I know you've got an eye for calligraphy, but this is another level."
        GTS "Oh, it's nothing so exceptional. I couldn't have made it without such splendid inspiration."
        MC "Respectfully, Naomi-chan, hell no. {i}This{/i} takes vision."
        show GTS unique at Transform(xzoom=-1)
        "She shifted in place, then smiled with piercing warmth at me as she cocked her head just so."
        GTS "Thank you, Keisuke-chan. I’m very glad you like it."
        MC "Heh. You're a beautiful soul, Naomi-chan."
    else:
        extend " really pretty!"
        show GTS happy
        GTS "Thank you, Keisuke-chan. I hope I've done this night justice."
        MC "Heaven knows you have."
    show GTS neutral
    "Smiling, Naomi closed her eyes and leaned back on her arms, open to the sky."
    MC "Haah..."
    MC "Well... should we head back?"
    GTS "Do you think it would be well if we took a bit of a cat nap here?"
    GTS "Even the crickets are at peace, it seems... a night like this comes by precious few times in life."
    MC "Mm... I guess it's not that late. I suppose I could set an alarm for an hour."
    show GTS happy
    GTS "Ah, wonderful..."
    "She laid down, spreading the watery mess of her bare raven hair on the grass, as I set the alarm on my phone. At last I lay my head down too..."
    show GTS happy with hpunch
    MC "Gwoh!..."
    "When Naomi's arm reached out like pale, vengeful seaweed, she lashed her hand around my forearm and pulled."
    show cg GTS044_stars2 with dissolve
    "Before I processed my new, salmon-like state, she caught me with her other hand and laid me face-up over her torso. Naomi sighed while I said nothing."
    "I decided, with my feet nestled between her knees and my head between her plush breasts, that I was pretty okay with this."
    "But..."
    MC "Naomi-chan? Are you sure you're comfortable like this?"
    GTS "Ahhh... yes, thank you. I'm quite comfortable."
    GTS "Moments like these come by precious few times."
    MC "Indeed they do."
    pause 2
    GTS "I love you, Keisuke-chan. With all my heart."
    MC "I love you just the same, Naomi-chan."
    "She laid her arms over my stomach and gently squeezed, and I reached back to tousle her hair."
    "For a while, that was the last of it; with my arms resting over hers I shut my eyes to the brightness of the sky, in favor of Naomi's deep breaths humming a lullaby and with such tenderness rocking me."
    scene black with fade
    "Very soon, I fell asleep."
    jump daymenu

label GTS044_c3b:
    scene Library with fade
    if getSkill("Academics") > 7:
        "I'd made some good progress in the hours to follow, but not enough that I felt I'd totally grasped the chapter before the library was about to close."
    else:
        "I'd made some progress... technically... but not enough to close the proverbial book on it before the literal library was about to close."
    "With the footsteps and chatter from the hall outside dying down, I gathered my things and prepared to head back to my dorm."
    scene black with fade
    pause 1
    scene Dorm Interior with fade
    MC "Home sweet home. Did you miss me, pillows, sheets, and Aystation? 'Cuz I missed you."
    "But our love would have to go unrequited a while longer. I dropped my backpack on my desk with plenty of slack on the arm and went to grab a glass of water before sitting down."
    MC "Okay, where was I..."
    scene black with fade
    $setTime(TimeEnum.NIGHTLIGHTS)
    pause 1
    scene Dorm Interior with fade
    "After beginning my second run-through of the material, I took notice of the waning light and flipped on the overhead lights."
    if getSkill("Academics") > 7:
        "I was, at that point, actually pretty sure of myself... but I was still cramming, after all. I made a point to review more than felt necessary."
    else:
        MCT "Uggghhh, this is so dumb. I'm giving this one more go before I drop this pencil and do something that doesn't make me want to die."
    "The dark peeking through the curtains grew deeper as I passed the hours in the padded walls of my textbook."
    "Eventually, there was a ripple in the muttering footsteps outside the hallway door. It fell utterly silent for a few seconds, before the muffled scrape of a key sliding in the lock replaced it."
    show RM neutral with dissolve
    "My roommate slunk into the room and gave me a curt, polite smile."
    show RM smug
    RM "Hey, Hotsure-san. How's studying?"
    MC "Cancer. How's your night been?"
    show RM happy
    "He chuckled."
    RM "Yuki-chan was finally free for a night, so I took her to see Quantum of Skyspecter."
    MC "The spy flick? Whose idea was that, exactly?"
    show RM neutral
    RM "Hers. I don't mind a good movie, but they usually don't grab me."
    MC "Huh. And was it good?"
    RM "Good enough. Yuki-chan liked it."
    MC "Cool. I'd take Tomo-chan to see it if she weren't allergic to theaters and paying for things."
    RM "There's merit to that mindset. Being social might do her some good, though."
    MC "Don't have to tell me."
    RM "And, uh... how are things with Yamazaki-san?"
    MC "Pretty good. It was pretty weird when she had to move out to that quarry, but she's made of tougher stuff."
    RM "Yeah?"
    MC "Yeah. She's adapted pretty well."
    RM "Hm... good to hear."
    show RM concerned
    RM "Of course, I imagine she's not the type to... stay down for long."
    RM "Damned if I don't feel a little sorry for her though."
    "I turned on my chair to look at him as I set down my pencil."
    MC "You gotta work on your routine, Utagashi-san. Besides, there's plenty she can do with her life even with her factor."
    show RM neutral
    RM "I'm not talking about her factor. Good for her for always putting up a stiff upper lip, but what I heard about her mom and dad..."
    RM "...Puts a new light on things."
    MC "What do you mean?"
    show RM distrustful
    pause 1
    show RM concerned
    RM "Okay, let me paint a picture for you."
    RM "There's a rustic old mansion out deep in the woods..."
    RM "And in that mansion lives an old, old family of rich recluses, clutching their wax stamps and obsessing over the old ways..."
    RM "And then there's their sweet, perfect daughter, who only likes things father dearest says she can and winces whenever she says something wrong."
    show RM neutral
    RM "That don't sound like Charlotte Brontë to me, Hotsure-san, that sounds like H.P. Lovecraft."
    if getSkill("Academics") < 4:
        MC "...Who?"
        RM "Brontë was a British romance and drama novelist and poet. Lovecraft was an American horror writer. Who specialized in reclusive families being depraved in their mansions in the woods."
    MC "Okay, yeah, they're a little stuffy, maybe it's a little weird the way they dress in public, but I highly doubt they’re in some kind of death cult or whatever you’re saying."
    RM "Probably not. But obviously there’s a difference in culture with them."
    RM "Just keep an eye out. My money says Yamazaki-san’s got a lot of stuff bottled up."
    MC "Who doesn't?"
    RM "More than you might expect. Or maybe just different."
    MC "I never took you for a psychoanalyst."
    RM "Far from it, but it's still helpful to consider what motivates people."
    menu:
        "...Well, uh, thanks for the tip, I guess.":
            jump GTS044_c4b_1
        "...So, like, if you were to guess what sort of stuff she's got going on...":
            jump GTS044_c4b_2

label GTS044_c4b_1:
    RM "But at the end of the day, I'm just one guy. Draw your own conclusions."
    show RM happy
    RM "And you're welcome."
    hide RM with dissolve
    $setAffection("RM", 1)
    "He walked away as he said it and disappeared under the tent obscuring his desk, which prodded me back to my own classwork."
    jump GTS044_c5b

label GTS044_c4b_2:
    RM "You serious? You're the one dating her, what do {i}you{/i} think?"
    if getAffection("GTS") > 70 and getSkill("Academics") > 4:
        MC "...Sometimes I think she has issues with self-worth. Like she can't live up to what's expected of her."
        RM "Uh huh... I could see that, a woman of 'breeding' like her. She probably holds herself to pretty high standards."
        MC "Yeah. I remember way back when she was still learning to bake... she was really sensitive about her skills for a long time."
        MC "Something to think about, I guess. I should probably get back to studying."
        RM "Probably. Hope you do well."
        MC "Thanks."
        MC "And thanks for listening, I know other people's relationships isn't the most engaging topic."
        RM "Don't mention it. I'd be a fool to turn down new intel when it's presented to me."
        MC "Wow, I instantly regret everything I ever told you."
        show RM smug
        RM "Hey, if nothing else, I'm an honest man."
        hide RM with dissolve
        "After spending a moment or two futilely trying to process that, I turned back around and he sat down at his own clandestine desk. 'One more read-through and you'll be fine', I told myself as I lifted up my pencil one more time."
    else:
        MC "Uhhh... well, she was pretty sad about being away from the other people in class. I think she gets lonely living in a metal box in a dirt pit."
        "He nodded and started unzipping his backpack by his desk."
        RM "Well, who wouldn't?"
        MC "True. At least she won't be here forever."
        RM "Yeah."
        MC "Something to think about, I guess. I should get back to studying."
        RM "Probably. Hope you do well on the test."
        MC "Thanks."
        hide RM with dissolve
        "I turned back around and he sat down at his own clandestine desk. 'One more read-through and you'll be fine', I told myself as I lifted up my pencil one more time."
        "A minute or two of unmolested silence passed under the increasingly artificial light."
        RM "You know, that gets me thinking. How does the penal system work with giants?"
        MC "...Dunno. I bet it would be mostly the same, most of the time."
        RM "Yeah. But what if someone ten or twenty feet tall commits an actual serious crime? Do they just get a bigger fine?"
        RM "What do you do when they can't be detained?"
        pause 1
        MC "Dunno. I'm no lawyer."
        "Thus, we went back to business."
    jump GTS044_c5b

label GTS044_c5b:
    scene black with fade
    pause 1
    scene Dorm Interior with fade
    MCT "Whew... okay... I think I should be good for tomorrow."
    MCT "And if I'm not... next time I'm just gonna march up to that mountain shrine and leave a fat wad of cash for the gods."
    "I let my book slap closed and breathed the free air around me."
    "It was suffused with quiet energy, quiet buzzing, as my roommate worked in such silence that he may as well have been asleep. If I hadn't known better, I might've guessed he was."
    "I checked my phone; it was past ten, nearer eleven."
    if getFlag("GTS044_lie"):
        "And with breath again in my lungs, I stood."
        scene Dorm Exterior with fade
        "The air was alive in a soothing dance across my face as I stepped beyond the shadowed glass. Like lightning bugs, a dozen lamps still glowed behind glassy veils, just about to wink out."
        "I leaned on the railing as I looked up at the sky, a sparkling ebon jewel, and into its great, misty white eye, a sun for the lonesome."
        "It stared back down at me, kindly. In the quiet of the night, my mind began to wander."
        scene white with fade
        pause 0.5
        #For the following segment, a different character called "Keisuke" should be defined in the code which is the same as the normal MC except for not showing a side portrait
        Mom "Do you know why the moon is white, Keisuke-kun?"
        AltMC "It’s made of cheese."
        Mom "Close. It’s covered in mochi."
        AltMC "Ohhhhh. That must be a lot, how’d it get on the moon?"
        Mom "Well, a long time ago, a god who lived on the moon decided to take a walk through the forest, disguised as a beggar."
        AltMC "What’s a beggar?"
        Mom "A beggar is someone who doesn’t have a house, or money, or sometimes even food. So when the little critters in the forest saw him, they decided to all pitch in to make dinner for him."
        Mom "The fox brought fish he just caught from the stream; the monkey brought fruit picked from his favorite trees."
        Mom "But all the rabbit had was grass. So, he brought his greenest, tallest grass to the moon god and told him to make a little fire with it. Once the fire was nice and hot, the rabbit threw himself into it."
        AltMC "What!? No!"
        Mom "Don’t worry, Keisuke-kun, the rabbit was fine. The second the moon god saw what the rabbit had done, he plucked him out of the fire and revealed his true self. He thanked all the other forest critters for the meal, and then, as a special thanks to the rabbit..."
        Mom "The moon god carried the kind, brave little rabbit back to the moon with him, where he could pound mochi all day and eat it all night."
        Mom "That rabbit’s still up there pounding mochi to this day, you know."
        AltMC "...Woah."
        Mom "Well, the moon god doesn’t walk around here much anymore..."
        Mom "But I want you to remember that even today, very good things can happen to you when you be kind to others... even if you lose something at first."
        AltMC "O-okay. I’ll remember."
        Mom "That’s good! Now, do you want some tsukimi dango?"
        AltMC "Yes... please."
        scene Dorm Exterior with fade
        MC "Haah..."
        MCT "I bet Naomi-chan would like a picture to remember this by..."
        "Without any further ado, I took out my phone and pointed the camera lens up at the moon."
        "I wasn't quite sure I was seeing it right, so I knelt down and brushed my fallen bangs from my eyes."
        MCT "Ah, what the hell, it's tiny!"
        "My camera registered the biggest, brightest moon I'd ever seen as a large-ish lightbulb floating above the clock tower."
        MCT "I need some way to zoom in farther..."
        MCT "...{w} Wait..."
        scene Dorm Interior with fade
        MC "Hey, Utagashi-san, can I borrow your binoculars?"
        show RM neutral
        RM "For?"
        MC "I can't get a good picture of the moon. I wanna try to magnify it."
        pause 1
        if getAffection("RM") > 1:
            show RM happy
        RM "Sure."
        "He slid open his desk drawer and from it passed me a compact pair of binoculars."
        MC "Thanks, man."
        hide RM with dissolve
        scene Dorm Exterior with fade
        "I stepped back out onto the balcony and, gripping both my roommate's binoculars and my phone for dear life, lined up another shot."
        MCT "Much better. Now to take the shot..."
        "{i}click{/i}"
        "I set the binoculars down and admired my handiwork; I decided it would do as I punched in Naomi's phone number."
        "It rang just a few seconds, and then I was answered by the soft, deep howl of a breeze."
        GTS "Hello?"
        MC "Hey, Naomi-chan. Good to hear from you."
        GTS "Likewise, Keisuke-chan. I was beginning to miss your voice."
        MC "Heh, people always tell me that I have an addictive personality."
        GTS "They must be referring to your skill at video games."
        MC "Whoah whoah whoah, was that a sneak diss just now?"
        GTS "Heavens, no. I would never come between you and your first love."
        "At that, I began to crack up, to the tune of Naomi's giggling on the other end of the line. This woman could throw lead just like she threw sugar."
        MC "Ahhh..."
        GTS "So then, have you had a chance to look at the moon?"
        MC "I'm doing that as we speak."
        GTS "It is a marvel, isn't it? In thousands of years its splendor has not faded."
        MC "I was thinking about that just now. I actually took a picture, I'll send it to you."
        GTS "Oh?"
        pause 0.75
        if getSkill("Art") > 7:
            $setAffection("GTS", 1)
            GTS "Oh! Gracious, that's beautifully composed. It almost looks professional."
            MC "I dunno about that. I was just trying to make it look good."
        else:
            GTS "Oh, that's quite lovely."
        GTS "Thank you dearly for this, Keisuke-chan. This will be a fine token to remember this evening by."
        MC "I hoped it would. So, what are you up to?"
        GTS "Oh, just taking it in. I meditated for a while, and now I feel inspired to try painting the scene."
        MC "What I wouldn't give to see that."
        GTS "You needn't wonder, Keisuke-chan. Of course I'll show it to you tomorrow."
        MC "Of course you will, you're sweet like that."
        GTS "Hmhmhm"
        GTS "What of your studies? Have you completed them satisfactorily?"
        MC "Yeah. Took a while, but I got it."
        GTS "Excellent. I'm sure you will find your diligence rewarded."
        GTS "I myself found this particular material a bit confusing."
        MC "That makes me feel better. Maybe not about my chances on the test, but in general."
        GTS "I'm glad to be of some assistance, however slight."
        MC "You assist plenty."
        GTS "Thank you, Keisuke-chan."
        "Silence then prevailed for a few moments... maybe minutes?... as we just admired the sprawling sky."
        MC "It must be nice, just being able to look up at the stars and forget about Earth for a couple minutes."
        GTS "Nice... hardly does it justice. It's like water in the desert."
        GTS "Keisuke-chan, could you please send me a picture of yourself?"
        MC "Huh? Yeah, of course. One sec."
        "I brought it to my face, twisting around to find just the right light, smiled, and took the shot."
        menu:
            "Make it spicy":
                jump GTS044_c5b_1
            "Send it as is":
                jump GTS044_c5b_2
    else:
        "Well and truly ready to drop unconscious for several hours, I nevertheless picked up my phone and tapped Naomi's name. I lifted it to my ear as it beeped."
        "A few pensive moments came and went... I passed them thinking how she must be taking her phone easily in her hand, about to tap the button with serenity and grace. In my mind, she was unshakable."
        "At last the beeping cleared to be replaced by a soft but deep howl."
        MC "Naomi-chan?"
        GTS "Good evening, Keisuke-chan. How do you do?"
        MC "I'm good. I missed your voice."
        "A mostly-muffled chuckle came through."
        GTS "Likewise. Have you completed your studies to satisfaction?"
        MC "I think so... yeah, I think so. How's your night been?"
        GTS "Quite well. I took a walk just after sunset. Seeing all the stars out tonight, I felt inspired to paint the scene."
        MC "Oh, that's what that sound in the background is. Well, that sounds lovely. You'll have to show me it tomorrow, I might need the pick-me-up after the test."
        GTS "Keisuke-chan, you must not let yourself be troubled by hypotheticals. The best thing you can do is to live in peace with the moment."
        MC "I'm very at peace with this moment."
        GTS "I'm glad. Now, you need only let yourself be at peace with the moment tomorrow as well."
        MC "No promises."
        GTS "Oh well."
        "There was an interluding silence; I walked over to my bed and lay down, dreaming up some way to keep us talking."
        MC "Will you be up long?"
        GTS "I don't intend to stay up too much longer."
        GTS "I imagine you're rather tired by now."
        MC "Well... yeah. Yeah."
        GTS "I suspected as much. Your diligence is quite admirable, Keisuke-chan."
        "I smiled yet wider as I stared up at the blank canvas of the ceiling."
        MC "I hope it actually does something for me. If I had time I might just go up and leave an offering at the shrine."
        GTS "I think that’s a fine idea regardless. Would you like to go together tomorrow?"
        MC "I’d love to."
        GTS "As would I."
        GTS "Well, for now, I suppose you need your rest. I love you, Keisuke-chan."
        MC "I love you too, Naomi-chan. Good night."
        GTS "Good night."
        "The flesh of my back lay slack on the mattress, and I laid my phone on the side table before I shut my eyes."
        jump daymenu


label GTS044_c5b_1:
    $setFlag("GTS044_seductive")
    "And then I got an idea. An awful idea."
    "I deleted the picture, undid the top few buttons on my shirt, and parted the hems to bare my chest like a dimestore crook."
    "With one hand tucked deep in my mane and my mouth in a crooked, one-fanged smirk, I took another shot and sent it."
    "And then deleted that, too."
    "As I redid my buttons, I asked her what she thought."
    GTS "Ah, it seems it just arrived."
    $setAffection("GTS", -1)
    GTS "Oh, that's- why is your shirt undone? Aren't you cold?"
    MC "Just thought I should give you something memorable."
    GTS "...You {i}are{/i} incorrigible sometimes, Keisuke-kun."
    GTS "Don’t you believe that your unadorned self is memorable enough for me?"
    MC "Um... uh..."
    GTS "Please, why don’t you send me a nice smile?"
    MC "Uh...{w} yeah! Yeah, sure."
    GTS "Thank you dearly."
    "Not quite processing what just happened, I smiled for her earnestly, snapped the picture and sent it."
    jump GTS044_c5b_2

label GTS044_c5b_2:
    MC "Okay, I sent it."
    if not getFlag("GTS044_seductive"):
        $setAffection("GTS", 1)
    "She sighed over the wind."
    GTS "It’s like you’re really here."
    MC "I could’ve gone over to visit you."
    GTS "You could have, of course. But duty comes before pleasure."
    MC "Yeah, I guess."
    GTS "...You sound a bit tired."
    MC "A bit."
    GTS "I confess I feel the same. Shall we see each other tomorrow?"
    MC "We shall."
    GTS "Splendid. I love you, Keisuke-chan. Pleasant dreams."
    MC "I love you, too. Good night."
    "I hung up, and spared one last glance up at the brightness of the sky. I wished the kind little rabbit good night before I went back to my room."
    jump daymenu

label GTS045:
    "This marks the current end of Naomi's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance

label GTSPRG001:
    scene School Planter with fade
    play music Busy
    "As I was heading to the dorms after class I spotted Naomi and Aida down in the garden."
    MC "Hey girls."
    show GTS neutral at Position(xpos=0.7, xanchor=1.0, yanchor=1.0)
    show PRG neutral at Transform(xzoom=-1), Position(xpos=0.3, xanchor=1.0, yanchor=1.0)
    with dissolve
    GTS "Hey Hotsure-san."
    PRG "G-Good evening, Hotsure-san."
    MC "What is going on here?"
    PRG "Well... we're working on something for the cooking club. See, the school pays for all of the food for the club to use, provided that it's all used up."
    PRG "We've had so many new students join lately, that the school isn't able to provide as much food."
    PRG "So, I thought that, with Yamazaki-san's assistance, we could plant a school garden, so that we could take the money that is being spent on produce and move it to other ingredients."
    MC "That sounds like a brilliant idea."
    show PRG happy
    PRG "Thanks."
    GTS "It's surprising the school didn't already have one setup, but it'll be a nice project to work on."
    menu:
        "I'd be down to help.":
            jump GTSPRG001_c1_1
        "I suppose this is something best left to the experts.":
            jump GTSPRG001_c1_2

label GTSPRG001_c1_1:
    MC "I'd be down to help with this project."
    GTS "You sure Hotsure-san?"
    MC "Sure, this sounds like it would be a fun way to relax after class."
    show GTS happy
    GTS "Well I can't deny that it's relaxing but it does mean getting a little dirty."
    MC "A little dirt never hurt anyone, plus you can teach me about these plants."
    $setAffection("GTS", 1)
    GTS "I'd be more than happy to do that."
    show PRG neutral
    $setAffection("PRG", 1)
    PRG "I'm glad you'll be joining us Hotsure-san. With the three of us, it should be easy to get this started in time for next season's competitions."
    jump GTSPRG001_c1_after

label GTSPRG001_c1_2:
    MC "I suppose this is something best left to the experts."
    GTS "I'd be more than happy to teach you Hotsure-san."
    MC "It's fine Yamazaki-san, gardening isn't as much my forte as it is yours."
    show PRG neutral
    PRG "I-I'm not really an expert either. I just follow Yamazaki-san's instructions."
    MC "I mean I'm with Yamazaki-san on this one, I am equally surprised the school didn't already have a dedicated produce garden."
    MC "So I look forward to seeing what you two can put together, I bet it'll be impressive."
    "The two girls giggle."
    PRG "T-Thanks, Hotsure-san. We'll both try our hardest."
    jump GTSPRG001_c1_after

label GTSPRG001_c1_after:
    MC "What crops are you planning on planting?"
    show GTS neutral
    GTS "Some basic tomato, basil and pepper plants should be a good start. Those grow quite easily with only basic tending."
    show PRG neutral
    PRG "Those would be nice to start with, especially since we use those with nearly every dish."
    GTS "What are some other foods you use often that we could grow?"
    PRG "Let me think..."
    PRG "Well carrots, peas, scallions and onions are other vegetables we use often."
    GTS "The scallions and peas should be easy to grow, the carrots and onions may take longer but shouldn't be too challenging."
    GTS "Do you make much tofu?"
    PRG "Not really, I'm still trying to get the recipe right."
    GTS "Alright, so no Wakegi."
    MC "Wakegi?"
    GTS "It's similar to scallions, but it's most commonly used as a topping for tofu."
    $setSkill("Academics", 1)
    PRG "Oh, that's the name of it. I always thought they were scallions as well."
    GTS "The only real difference is it being a form of tree onion it has a stronger taste than a normal green onion."
    PRG "I better make a note of that when I make tofu again."
    show PRG happy
    PRG "Thanks for the tidbit Yamazaki-san."
    show GTS unique
    GTS "It's nothing, Kodama-san."
    MC "Sounds like a pretty good starting list of veggies you have."
    show GTS neutral
    GTS "It's more than enough to get us moving, I may plant some smaller herbs like sage and rosemary since they don't take much space."
    show PRG neutral
    PRG "Those would be lovely too."
    GTS "I'll make sure to pick those up as soon as I can, that way we have the maximum amount of time for them to grow."
    MC "Sounds like you have this already planned out for the next couple months."
    "Naomi blushed."
    PRG "Well I need to be leaving, Alice said she needed me for something."
    MC "I should be leaving too, I'm behind on some homework for class."
    MC "Take care girls."
    Girls "Bye, Hotsure-san."
    jump daymenu
