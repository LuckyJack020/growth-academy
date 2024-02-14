label GTS001:
    $setProgress("GTS", "GTS002")
    $setVar("GTS_selfhood", 0)
    scene Campus Center with fade
    play music Peaceful
    "The words from Tashi-sensei stayed with me long after class had concluded. I just wasn't sure how to properly process what we were told."
    "What Daichi had told me earlier was starting to resonate more, and I began to wonder if others knew about the purpose of this school before they were enrolled."
    "If only to focus on the things I could understand for a while, I decided to take a walk and take stock of the new campus; the little pamphlet map they gave us, I figured, would only do for so long."
    UNKNOWN "Excuse me!"
    if checkSkill("Athletics", ">", 2):
        "No sooner had the shout crossed my ears than something smacked hard into my shoulder, and some guy my age stumbled in front of me before breaking back into a stampede."
    else:
        "A fraction of a second after I processed the machine-gun footsteps behind me, their owner smashed into me like someone throwing a machine gun at me."
        "I just recovered my footing in time to see a half-flailing student running off without a glance back."
    MC "Ay, watch it!"
    UNKNOWN "Sorry!"
    "He didn't look back, fading into the crowds alongside the wind."
    MCT "Dick."
    UNKNOWN "Hotsure-san? Are you alright?"
    "The next thing to catch me off guard was a girl's voice, one enveloping and immaterial, like spring mist."
    show GTS surprised:
        xpos 0.99 xanchor 0.0 yalign 1.0
        linear 5.0 xpos 0.5 xanchor 0.5
    extend " I twisted around; one of the girls from my class was walking up to me from behind while raven locks waved behind her in the breeze."
    MC "Yamazaki-san, right? Yeah, I'm okay. That dude just surprised me."
    GTS "It would seem so. How peculiar. I wonder what compelled him to act so brashly?"
    MC "Dunno. He's probably not available for interview."
    show GTS neutral
    GTS "I suppose he wouldn't."
    GTS "Well now, what are you up to?"
    MC "Nothing much, just checking out what's on campus. How about you?"
    GTS "Much the same. For all its peculiarities, this place has a sort of charm to it, does it not?"
    MC "I guess so. I'm kinda distracted by all the \"peculiarities\" at the moment."
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
    if checkAffection("GTS", ">", 1):
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
        "I'm concerned about what that might mean for my sister, honestly.":
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
    GTS "Oh? You have a sister, Hotsure-san?"
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
    scene School Planter
    show GTS neutral
    with fade
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
    $setProgress("GTS", "GTS004")
    scene School Planter with fade
    $setGTSOutfit(OutfitEnum.WORK)
    "All around in the garden was orange and yellow, peach pink and rose red."
    "I didn't normally find myself staring up at the clouds, but this was one spring evening that merited an exception as its light bathed the flowers in warmth. Yet the air was cool, even a little chilly, carried by the lackadaisical breeze."
    "I turned a corner and my silence was broken by a faint voice in the distance. When I looked around, because why not, I spied Naomi bowing deeply to a man whose face was as weathered as his dungarees; he smiled, nodded, and the two parted ways."
    show GTS neutral at Position(xcenter=0.75, yalign=1.0), Transform(xzoom=-1) with dissolve
    play music HigherEdu
    MC "Yo, Yamazaki-san!"
    "I lifted one arm up to give a slight wave. This seemed to surprise her, as she jumped a little and looked back towards me. Giving a small nod, she walked over with a few small bags clasped between her hands."
    show GTS embarrassed:
        xzoom 1.0
        linear 0.75 xanchor 0.5 xpos 0.5
    GTS "Good evening, Hotsure-san. I must say you startled me a little."
    MC "Heh, sorry. I just wanted to make sure you heard me. I see you talked to the gardener."
    show GTS neutral
    GTS "I did yes. I was asking him about some of the flowers on the grounds, and before I knew it we were engaged in quite a lengthy conversation."
    GTS "Fittingly, he's quite the enthusiast himself. He even gave me these seeds to plant."
    "She opened her palms to show me the handfuls of little paper baggies resting in them."
    menu:
        "Oh, that's cool. How did the rest of your day go?":
            jump GTS002_c1
        "Really? That was cool of him. What kind are they?":
            jump GTS002_c2

label GTS002_c1:
    GTS "Oh, it has been peaceful. I spoke with my family on the phone and they seemed pleased to hear as much."
    MC "Cool, cool. Do they, uh, know the big news yet?"
    "She touched her finger to her lips for a moment, in silence, before she answered."
    GTS "I haven't told them, no. I do not wish to cause them undue worry."
    GTS "I will discuss it with them once the... situation has been clarified more."
    MC "Fair enough. No need to report that until we have something to report."
    GTS "Precisely."
    MC "So, uh... what else have you been up to today?"
    GTS "Not much. I unpacked the last of my things, tended to my plants, and worked with my roommate on how to organize the space."
    GTS "Once that was done, I decided to take a walk through the grounds, and here we are."
    jump GTS002_after

label GTS002_c2:
    $setAffection("GTS", 2)
    $setFlag("GTS008_flowers")
    show GTS happy
    "She grinned and her eyes brightened ever so slightly at that question."
    GTS "Indeed, it was quite generous of him. As for the flowers, these ones are irises, a lovely plant with quite the bold color. In the art of ikebana, they traditionally symbolize hope, faith, and wisdom."
    show GTS neutral
    "She crooked her finger around her chin as she regarded the bag."
    GTS "Hm, I hadn't noticed before. How germaine."
    MC "What is?"
    GTS "That a representative of the academy should give us students a gift symbolizing hope."
    MC "Oh... {w}oh yeah, it is, isn't? Germaine and what not."
    "Smiling a little, she let out an accommodating chuckle."
    GTS "Quite."
    GTS "Now this one is the lily, which you might have already noticed."
    "She looked over to the white starburst-shaped flowers I had seen when I first entered the garden."
    GTS "Their shape makes them particularly striking, I find. The white color symbolizes purity, although other colors have perhaps less wholesome connotations."
    MC "Oh, for real? Like what?"
    GTS "The orange is said to be associated with hatred and revenge, and the crimson spider lily with a final farewell."
    MC "Huh. Wow, that's a little dark. And I thought flowers were just supposed to look pretty."
    show GTS happy
    GTS "It is perfectly fine to appreciate them simply for that. But the depth of the floral language has lent much to the art world as well."
    "She handed me the lily seed bag as well, hardly realizing I was practically carrying them for her."
    show GTS neutral
    GTS "Now, these last ones may seem rather plain compared to the others, but azaleas are deservedly popular the world over. I know of more than a few festivals dedicated to them here in Japan."
    show GTS unique
    GTS "I've read that in Chinese culture they're associated with nostalgia... looking at them, one could imagine why."
    "She handed me the last bag, which displayed flatly pink, six-petaled flowers; a warm, simple, pure smile illuminated her countenance as she did."
    $setSkill("Art", 1)
    MC "Heh, you must really have a thing for flowers."
    "Her smile faltered, she pursed her lips, and a light blush formed across her cheeks."
    show GTS embarrassed
    GTS "Well, I do apologize for prattling on like that. I'm sure you had other plans for this evening."
    MCT "A generous assumption."
    MC "Nah, nah, you're good. It's actually pretty interesting, and if I'm gonna hear about it I'd like to hear it from someone who clearly cares. I just kinda don't know squat about it."
    GTS "I am glad to serve, then."
    show GTS neutral
    GTS "And it is understandable that you wouldn't know much. Traditionally, ikebana is more of a woman's art."
    show GTS neutral at Transform(xzoom=-1)
    GTS "Nevertheless, it is a singularly meditative art. Anyone could benefit."
    GTS "To purify one's intentions, to unite the mind and body in purpose, to unite oneself with the cultivation of living beauty..."
    pause 0.5
    show GTS embarrassed
    GTS "Oh fiddlesticks, I've done it again."
    "Against my better judgment, I broke into a laugh."
    MC "No worries, Yamazaki-san, I'm still interested."
    MC "Tell you what, you ever feel that uncontrollable urge to talk about flowers, come to me and I'll lend you my ear."
    GTS "Erm... thank you. I shall try not to overstay my welcome regardless."
    show GTS neutral at Transform(xzoom=1)
    jump GTS002_after

label GTS002_after:
    GTS "Well now, if I may ask, how has your day gone, Hotsure-san?"
    MC "I'm, uh, still thinking over what Tashi-sensei told us a little bit, but... it's been pretty good. I called my mom and dad earlier, told them I'm doing okay."
    MC "Oh, I do think I might join one of the sports clubs, I saw they're offering quite a few of them."
    "Her eyes were locked on me and she nodded as I spoke, taking in everything I said. It was pretty nice, being so listened to so closely even if we were just a step above strangers."
    GTS "Have any of them caught your eye?"
    MC "I used to be pretty into soccer. I might give it a shot later this year... if whatever condition I have still allows that to happen, I guess."
    "I chuckled lightly, suddenly aware of the barrier to any future planning."
    GTS "I hope so, Hotsure-san. I understand a game of soccer can be quite invigorating, and excellent exercise besides."
    show GTS happy
    "She gave me another soft, warm smile that made me smile in return as I scratched the back of my head."
    MC "Heh, thanks. {w}Well, it's getting pretty late, I don't want to keep you from, uh, your plants. See you later, Yamazaki-san."
    GTS "Certainly. A pleasant evening to you, Hotsure-san."
    hide GTS with dissolve
    "She bowed, and we turned from each other to walk away."
    pause 0.25
    "Seconds later, I spun on my heel and jogged back up behind her."
    show GTS surprised with dissolve
    GTS "Oh? Is something the matter?"
    MC "Oh, I, uh... your seeds."
    show GTS embarrassed
    "Her lips parted for a second as I held the baggies out to her, and then, in the warm evening light, her cheeks began to just slightly redden, and she took the seeds with a courteous bow."
    GTS "Good heavens, I'll forget my head next. Thank you, Hotsure-san."
    MC "Heh, no problem. Have a good evening."
    GTS "Farewell."
    hide GTS with dissolve
    "This time I watched her walk away for a second or two before I went on my way, even if it was rather rude to stare."
    "She was hardly the type I usually hung out with, and yet I found I was enjoying the occasional conversation with her."
    "I walked away wondering when I might bump into her next."
    jump daymenu

label GTS003:
    scene Cafeteria with fade
    play music Schoolday
    "The morning found itself to be quite the chaotic time, as many students rushed down the corridors to make it to the cafeteria in time to beat the breakfast rush."
    "When I finally arrived to the cafeteria, I saw that it was surprisingly calmer than what was transpiring throughout the hallways. I got in line behind a few other students who were getting their breakfast."
    "I will admit I was rather surprised by what I saw. There were trays upon trays of warm food prepared for us, a lot of which looked just heavenly to the eyes and assuredly tasted as wonderful."
    "Not wishing to hold up the line though, I quickly grabbed what I felt would be a decent quick breakfast, getting some steamed rice, a rolled omelette, and a small bowl of miso soup. I thanked the cooks before searching for a place to sit."
    "There were a good amount of unfamiliar faces among those sitting at various tables, but one face was rather familiar. Sitting down with a slight smile, I spoke to my neighbor."
    show GTS neutral
    show HairpinGTS1
    with dissolve
    MC "Hey there, Yamazaki-san. Nice to see someone I know here."
    GTS "Good morning, Hotsure-san. I hope you're having a pleasant day so far."
    "Her hands gently repositioned her utensils and napkin in an extremely orderly fashion before wiping her hands off with a moist towelette. She then looked at me, as if to give me a hint, until I realized what I'd forgotten."
    MC "Oh! Uh, itadakimasu."
    show GTS happy
    GTS "Itadakimasu."
    MC "Yeah it's been a pretty good morning so far, I managed to wake early so it gave me just the right amount of time to fully wake up, which is a pretty good start of the day in my opinion."
    MC "Thankfully since I woke up so early it allowed me to shower without feeling rushed."
    "She gave a small smile in response before picking up her chopsticks. Her hand softly slid her hair back as she picked up some cooked vegetables to eat."
    "This let me notice that her other bang was currently held back by a flower shaped hair clip. I had no idea what type of flower it was, only knowing that it had six white petals in a sort of star configuration."
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
    show GTS embarrassed at Transform(xzoom=-1)
    show HairpinGTS1 at Transform(xzoom=-1)
    "For the briefest of moments I could see Naomi's cheeks flash a slight crimson in what I assumed was embarrassment as her hand went to touch the accessory."
    "She looked away for a second, but returned her eyes back to mine and retrieved that small smile she had before."
    show GTS embarrassed at Transform(xzoom=1)
    show HairpinGTS1 at Transform(xzoom=1)
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
    $setTimeFlag("testday")
    $setProgress("GTS", "GTS006")
    scene Library with fade
    play music Peaceful
    "The afternoon sun trickled, glowing, through the library's large and numerous windows, and through the gaps in my bangs."
    "I still wasn't used to this place; as I passively guessed at the number of students there, in and between the vast, blocky shadows of the bookshelves, I realized there really were quite a few."
    "It just really didn't look like it at a glance, with the bookshelves noticeably taller than any I'd ever seen and the aisles between them looking wide enough for six normal people."
    "The space was well-used, too. Every row of shelves constituted a veritable wall of books, intermittent plastic coverslips gleaming in the sun, some of the signs claiming whole aisles for topics I'd never heard of."
    if isHighestSkill("Athletics"):
        "Well, I never found the library all that exciting, but my assignment wasn't gonna do itself."
    if isHighestSkill("Art"):
        "I stopped for a moment, absorbed. In spite of the strangeness of this academy's very existence, the air in the library still lazily swirled with silent discoveries, lazy afternoons in the sunlight, hushed and cheery chats between friends."
    else:
        "The sight of it all made me a little more confident in the face of the unanswerable strangeness of this academy's existence. Looking the aisles up and down, I could imagine they could answer just about any question I cared to ask."
    "As I walked among the shelves in search of the book I needed for my Contemporary Society course, out of the corner of my eye I spotted Naomi sitting at a nearby table."
    "Though her expression was characteristically mild, she raised an eyebrow once or twice at whatever she was reading, with one hand holding the book down flat and the other hovering a pencil over a notebook. Her attention didn't drift for a second."
    "Curious, I walked up behind her."
    menu:
        "Hey there!":
            jump GTS004_c1
        "(Read over her shoulder)":
            jump GTS004_c2

label GTS004_c1:
    $setAffection("GTS", -1)
    show GTS surprised with vpunch
    "Naomi jumped in her seat with a light gasp and clapped her hand to her sternum."
    show GTS angry at Transform(xzoom=-1) with dissolve
    "She closed her eyes before turning to face me, air hissing through her nose."
    GTS "Please don't do that."
    "There wasn't a hint of anger in her voice; no, the faint furrow in her brow as she went right back to her book was hint enough that she hadn't taken it as just a friendly greeting."
    MCT "Didn't think I said it that loud..."
    MC "Sorry, sorry. I just wanted to drop by and say hey."
    show GTS neutral
    "I let out a small chuckle, which softened her expression a bit. Nevertheless, she didn't take her eyes off her book."
    GTS "Would you like to have a seat?"
    MC "Don't mind if I do."
    "I took the opportunity to see what she was reading: on one page, a couple blocks of strange, angular characters arranged in an odd fashion, and on the other... some really dumbed-down story about a lumberjack and his pet ox."
    jump GTS004_after

label GTS004_c2:
    "I stooped down and peeked over her shoulder to see what she was reading, letting myself hover into her peripheral vision."
    show GTS neutral with dissolve
    GTS "Good afternoon, Hotsure-san."
    MC "Hey, Yamazaki-san. Sorry if I'm intruding, I just wanted to say hello and I was curious what you're reading."
    "She looked up at me, her face a characteristic portrait of mellowness and hospitality."
    GTS "That's quite alright. I appreciate that you didn't want to interrupt."
    MC "Mind if I sit down?"
    GTS "By all means."
    "I took a seat across from her. I also peered over at what she was reading: on one page, a couple blocks of strange, angular characters arranged in an odd fashion, and on the other... some really dumbed-down story about a lumberjack and his pet ox."
    jump GTS004_after

label GTS004_after:
    MC "What language is that? English?"
    "She nodded and angled her book a little more towards me."
    GTS "It is; rather, it's a book of short, simple stories in both English and Japanese. I'm trying to brush up on what I retained from my high school classes in my free time."
    MC "Neat. Thinking of taking a vacation in Hawaii in the near future?"
    show GTS surprised
    GTS "Not in particular, though I suppose one never knows. "
    show GTS happy
    extend "It's also a good skill to have should your job require it, or if you're ever hosting international guests."
    MC "Heh, quite the foresight. I barely even think about what I'll be doing a month from now. But hey, if you manage to make it work, that's one big advantage in the job market. Good luck!"
    show GTS neutral
    GTS "Thank you."
    "A certain warmth and a hint of a smile lingered on her face as she looked back down."
    "Perhaps I should've left her to her studies, but some intangible thing made me want to keep the talk going."
    MC "So, uh, did you get what sensei was talking about in class today?"
    "She puffed out the smallest sigh as she reached over to her backpack and retrieved the paper brick we had for a chemistry textbook."
    "Her wrist strained visibly lifting it; her prim, trim hand covered barely a sixth of the front of the book, and it almost dragged on the table as it hung at an angle in her grip."
    GTS "To be honest, not as well. Our science courses have proven more difficult than I expected."
    GTS "Even with the quick review sensei gave us, the new material seems quite advanced in comparison."
    MC "Well, I doubt we're expected to get everything memorized from the start. I'm sure it'll ease up a bit in the next few days."
    GTS "That is true, but there is still the matter of the quiz at the end of the week. I'll just have to shift my focus a bit, keep my English studies to an hour while devoting more of the afternoon to this."
    show GTS neutral
    GTS "No matter. I'll simply make plenty of room in my schedule for studying, even if I may have to set aside other pursuits for a while."
    MC "Hmm... you know, why not get a study partner? I remember when I was younger one of my teachers told me that the best way to learn and retain knowledge was to teach others."
    show GTS neutral at Transform(xzoom=-1)
    MC "So, if you have someone you can bounce information to and maybe even quiz, then you'll understand it better. After all, if you're making the quizzes then that means you have the answers already."
    "She placed her hand on her chin and tapped it once or twice."
    GTS "I'm not sure... the reasoning seems sound, but I would hate to impose on another."
    MC "Ah... yeah, fair enough. Other than Honoka-chan and me, we're all still pretty much strangers."
    if checkAffection("GTS", ">", 3):
        GTS "Indeed. Although, I don't think a stranger typically would just drop by for an impromptu chat."
        pause 0.25
        MC "Heh... yeah, good point. Maybe not {i}all{/i} of us."
    MC "Well... tell you what, I volunteer."
    show GTS surprised
    GTS "Oh! Are you sure? You really needn't take time out of your schedule simply to help me."
    MC "Well, I have my price of course, as an experienced quiz-taker. If you don't mind 5000 yen blowing away in the wind, surely you wouldn't mind 5000 yen blowing away into my hand?"
    GTS "Oh, well... what would your rates be, exactly? Would that cover a month?"
    pause 0.5
    MC "I... I'm joking, Yamazaki-san."
    show GTS embarrassed
    GTS "Ah. Very good."
    MC "Heheh, yeah, I'd be glad to help you, free of charge. I bet we'd both learn a lot."
    show GTS neutral
    GTS "Hmm. Perhaps I could help you with one of our other subjects, then. Is there any you think might give you trouble?"
    MC "Oh, math, a hundred percent. Pre-calc was the {i}bane{/i} of my {i}existence{/i}."
    show GTS unique
    "She gave a light giggle, covering her mouth as she did."
    GTS "I do believe I would be of help on that front. Very well then, it seems we have a deal."
    MC "Glad to be of assistance, study partner. Let's take care of business!"
    show GTS surprised
    Student1 "Sssh!"
    "We both tensed up as someone at another table once again reminded me of my surroundings. "
    show GTS embarrassed
    GTS "{size=-6}I didn't think you said it that loudly...{/size}"
    "Naomi was blushing slightly, but neither of us could stop a small giggle from slipping out as we started working more quietly."
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
    MC "\"Botans\", huh? I thought they were roses, honestly."
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
    GTS "My father always said he picked that breed because the Hokkaido has the three characteristics he looks for in people: bravery, loyalty, and intelligence."
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
    play music HigherEdu
    "Petals, dancing, fluttered down in the whispering wind, roosting on my shoulders and at my feet. They were almost ghostly, so light I hardly felt or heard them."
    "I cast my view languidly from side to side, in no particular hurry to take in the view of the courtyard."
    "I saw, faintly under the shade of a painted maple, Naomi reclined against the trunk, one hand supporting her chin while the other held a piece of paper. Her expression was as tall grass swaying in the breeze."
    MC "Hey there, Yamazaki-san. How are you?"
    "She looked up from her reading, and stood at a gentle pace before bowing with immaculate posture."
    show GTS neutral at center with dissolve
    GTS "Good afternoon, Hotsure-san. I was reading a letter from my mother. How are you?"
    MC "Pretty good, pretty good. So, a handwritten letter, eh? Didn't know people still made those."
    "A faint smile crossed her face as she folded up the letter and placed it back into the envelope."
    GTS "One could hardly blame you. They're a bit of a rarity these days, perhaps to our detriment. The writing of a letter cultivates grace and compassion when properly done."
    pause 0.25
    show GTS embarrassed
    GTS "But yes, my mother is quite fond of writing letters. I enjoy reading them."
    MC "That's pretty cool. I bet it gives the mailman warm fuzzies, delivering handwritten letters instead of bills and packages. That's a neat little postcard, too, where's it from?"
    show GTS neutral
    GTS "Kyoto."
    "She pulled the postcard away from the letter in her hand and held it out for me. It was a skyline picture centered on a distinctive red tower, the shimmering paper adorned with a wax seal."
    MC "Oh yeah, there it is. I thought I recognized that tower there. Are you from there, then?"
    show GTS unique
    GTS "Indeed I am."
    MC "Huh, neat. I've never been to Kyoto, but I've heard it's pretty cool. I've heard it's one of the best places to go for food, too."
    "I walked over and sat down next to her spot, and after a moment she sat down, too."
    GTS "Deservedly so! It's the birthplace of several forms of kaiseki cuisine... including the old imperial court style, naturally."
    show GTS neutral
    GTS "My friends and I made it our personal goal to visit a new restaurant every weekend. It was quite fun, and it gave me a deep appreciation for my hometown. Sometimes one can find a veritable diamond in the rough, as well."
    MC "Wow, that sounds like it'd be cool to do. Though, it also sounds like it'd be pretty hard on your wallet after a while, wouldn't it?"
    GTS "Well, it was valuable practice when it came to budgeting expenses. And we most certainly made lasting memories."
    show GTS happy
    GTS "Once we visited a novelty restaurant wherein the customer would catch a fish out of a pond that the cooks would then prepare. Heavens, my mother nearly fainted when I returned home with a bloodstain on my shirt."
    MC "PFFF"
    show GTS embarrassed
    MC "That's... a pretty funny image. You, of all people, showing up like that after dinner out with your high school friends."
    GTS "Hmhm, it is rather amusing, isn't it?"
    GTS "My friends and I thought so, at any rate."
    MC "Heh. Personally, me and my friends never did much exploring, at least not like that. Of course, not far from my house, traffic could get preeetty insane."
    GTS "Where are {i}you{/i} from, if you don't mind my asking?"
    MC "Oh, I'm from Tokyo. The big city, Gojira's old stomping grounds. Our house was just a little bit off of Shibuya."
    GTS "My, my! That must be a lively place to grow up. I imagine you've seen some interesting sights."
    MC "Oh for sure, especially around the holidays when all the tourists take over the streets. You turn an already crowded intersection into basically an impenetrable wall of people."
    MC "I felt bad for the people driving because, well... they weren't going anywhere for quite a while."
    show GTS surprised
    GTS "I've heard stories of how overwhelming Shibuya can get during the holidays."
    show GTS sad
    GTS "I've also heard quite a few horror stories about some of the nastier incidents on account of the excessive traffic."
    MC "Yeah, some bad accidents happened from time to time. I knew well enough to not get too absorbed into the larger crowds, and my dad made sure I knew to stay away from shady types."
    MC "That's where my friends came in handy. Said shady types usually think twice before they try anything when they're outnumbered."
    MC "Does, uh, Kyoto get pretty crowded, or nah?"
    show GTS neutral
    GTS "It can be, yes. Around Christmas in particular, it can be rather difficult to find seating in a restaurant if one is not reserved well in advance. It's a popular time for couples to have a date night."
    MC "Ohhh, yeah, it's kinda like that in Tokyo, too."
    GTS "I would imagine so. A couple of my friends would call weeks in advance to reserve a table for two at a French restaurant called L'Atelier du Goût. As you can imagine, it was dreadfully expensive normally, and prices were marked up considerably for Christmas."
    GTS "At the very least, they could also go see the decorations in Daimaru for free."
    MC "{i}Whew{/i}. I can't imagine saving up that much money and going through that much hassle just to choke down some French food. I could get the same experience eating a baguette on the subway."
    show GTS unique
    GTS "Goodness, Hotsure-san!"
    MC "Of course, I never really had a reason to go somewhere fancy. But how about you? Did you ever do anything with someone special?"
    show GTS surprised
    pause 0.5
    show GTS embarrassed at Transform(xzoom=-1)
    GTS "Oh, my, no."
    GTS "My responsibilities to my household never allowed for that sort of thing."
    GTS "In truth, being away from it all still feels rather... like something is missing."
    MC "So you've really never been on one date? You seem like you must've been pretty popular in school."
    show GTS embarrassed at Transform(xzoom=1)
    "Her cheeks began to turn a peachy red and she looked away."
    GTS "I believe I made a good impression on most of my classmates. I never went quite that far, though, no."
    show GTS neutral
    "She looked back towards me as she breathed back in her composure. I nodded gently, not wanting to press the issue."
    MC "Yeah, I guess it would be pretty tough if you're always busy. But hey, it'll come when it comes."
    GTS "Indeed, as with everything in life."
    MC "Well... anyway, on the topic of friends, have you made any new ones yet?"
    if checkAffection("GTS", ">", 7):
        GTS "{i}Our{/i} friendship has been quite worthwhile."
        "I smiled."
        MC "Yeah, I think so too."
        MC "What about other people?"
    GTS "...Not to speak of, so far. There's still a sort of distance between many of us from adjusting to this whole situation."
    GTS "Perhaps then, it'll be a bit easier to introduce myself to more people."
    MC "Well if you'd like, you could hang out with me and my-"
    show GTS surprised at Transform(xzoom=-1)
    pause 0.1
    show GTS surprised at altMove(0.5, 0.45)
    show BE happy at Position(xcenter=0.75, yalign=1.0) with easeinright
    BE "'Sup, guys?"
    "Somehow, I hadn't noticed Honoka, of all people, coming towards us at all. I waved, prompting one in return from her."
    show GTS neutral
    MC "Just shootin' the breeze. How's it going, Honoka?"
    show BE neutral
    BE "Good, just taking a cooldown walk after soccer practice. Thought I'd say hey."
    MC "Oh, actually, I wanted to ask you something."
    show BE neutral at Transform(xzoom=-1)
    extend " You think it'd be cool if Yamazaki-san tagged along next time we hang out?"
    show BE happy at Transform(xzoom=1)
    BE "Oh, that'd be swell! We could go to the park, grab some coffee, start up that weed farm we've been talking about. You do pretty good with plants, dontcha Yamazaki-san?"
    show GTS surprised
    GTS "W-what? Are you-"
    MC "Joking? Yes, she's hilarious."
    show BE aroused
    BE "I'm hilarious."
    show GTS unique
    show BE neutral
    BE "But yeah, that sounds fun. If our schedules line up, let's get together sometime!"
    GTS "Thank you kindly, you two."
    MC "Of course."
    show BE happy
    BE "No problem!"
    pause 0.5
    show BE neutral
    BE "And hey, favor for favor, you guys mind if I have a seat next to you?"
    show GTS neutral
    "Naomi firmly patted a soft, grassy patch on her side opposite me."
    BE "Thanks."
    "She stepped over, turned around, and {i}thwump{/i}ed down onto the spot; I tried not to stare at her chest bouncing from the force, but unlike Naomi's, I think my effort was more apparent."
    "But then... we just sat there for a bit. Nothing disturbed us, not even the lazy flutter of the wind as it carried away our old breath in exchange for the new. There was no time but the metronomic shift of the leaves and beams of sunlight overhead."
    show BE embarrassed
    BE "Haaahn... this is nice."
    MC "Yeah."
    GTS "I couldn't agree more."
    "Naomi opened her mouth again, looking skyward, but only closed her mouth in silence."
    "I puffed out the quietest snort I could, and I too looked to the sky."
    MCT "Y'know... I'm starting to like it here."
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
    $setGTSOutfit(OutfitEnum.WORK)
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
    GTS "They are a species of small flowers with six petals and borne in dense spikes. They come in a nice variety of colors so it could add to the visual appeal of the garden."
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
    $setFlag("VisitedTown")
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
            $setFlag("GTS009_Honoka")
            jump GTS009_c1_1
        "Buy the headband for Naomi": #+5 Affection Naomi
            $setFlag("GTS009_Naomi")
            jump GTS009_c1_2
        "Save your money": #+0 Affection.
            $setFlag("GTS009_None")
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
    if checkAffection("GTS", ">=", 7):
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
    if not getFlag("Meet_Ryoko"):
        $setFlag("Meet_Ryoko")
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
    if not getFlag("Meet_Ryoko"):
        $setFlag("Meet_Ryoko")
    MC "Nice to meet you too, I'm Keisuke Hotsure."
    Ryoko "Pleasure. Saw you talking to Yamazaki-san, you two friends?"
    if checkAffection("GTS", ">=", 2):
        MC "Yeah, a bit."
    else:
        MC "We're in the same class."
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
    scene School Planter
    show GTS neutral
    with fade
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
    $setFlag("XX12")
    $setProgress("GTS", "GTS014")
    scene Campus Center with fade
    play music Peaceful
    "{i}Shkt shkt shkt{/i}"
    MC "Hm."
    "{i}Pff pff{/i}"
    "{i}Shkt shkt shkt shkt shkt{/i}"
    MC "Hmmm..."
    if checkSkill("Academics", ">", 4):
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
    scene Campus Center
    show GTS surprised
    with fade
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
    if checkAffection("PRG", ">", 6):
        extend " Maybe we'd both learn a thing or two. Kodama-san really knows her stuff."
        show GTS happy
        GTS "Manifestly."
        show GTS neutral
    jump GTS013_c2

label GTS013_c2:
    GTS "Very good, then. We had agreed to meet in the cooking classroom."
    MC "After you, Yamazaki-san."
    "She resumed walking with me following after; even with her taking such methodic, piecemeal steps to keep the plate so motionless, it was a trick to keep pace."
    stop music fadeout 3.0
    scene Hallway
    show GTS neutral
    with fade
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
    scene Cooking Classroom
    show GTS neutral at Position(xcenter=0.3, yalign=1.0)
    show PRG worried at Position(xcenter=0.7, yalign=1.0)
    with fade
    play music PRG
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
    if checkSkill("Academics", ">", 2):
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
    stop music fadeout 3.0
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
    if checkSkill("Academics", ">=", 2):
        "I shrugged."
        MC "At least she gets paid for her time."
    else:
        MC "A what relationship?"
        GTS "In other words, she gives a good deal more in the relationship than she receives."
        MC "Oh."
        MC "Well, at least she gets paid for her time."
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
    if checkSkill("Academics", ">", 4):
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
    if checkSkill("Academics", ">", 4):
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
    "We passed the ticking minutes away ruminating over Naomi's technique during the preparation process, always with the unspoken question of \"how are they going to turn out this time?\""
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
    scene Track
    show GTS neutral
    with fade
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
    $setFlag("XX15")
    scene Dorm GTS with fade #this should change eventually
    play music Busy
    Ryoko "...And cut! Good job everyone!"
    "These were the first words Naomi and I heard as we waited outside of Ryoko's dorm room before we were allowed in, the \"QUIET! Filming inside!\" sign taped on the door preventing us from knocking."
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
    if not getFlag("Meet_Minori"):
        $setFlag("Meet_Minori")
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
    MCT "Since when were we \"the gang\"...?"
    jump daymenu

label GTS016:
    scene School Planter
    show GTS neutral
    with fade
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
    if not getFlag("Meet_Fumika"):
        $setFlag("Meet_Fumika")
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
    Fumika "Anyway, as I was saying. You're just perfect! Have you ever been interested in joining the basketball team? It's a ton of fun, and we're in need of new players."
    GTS "Well... I hadn't really thought about it before, in truth."
    Fumika "Whaaa? How could you not? With your height and build, you'd be a {i}natural{/i}."
    GTS "It's simply something that hasn't crossed my mind. I do apologize, but I'm not much for athletic pursuits."
    Fumika "That's totally fine, we wouldn't throw you into the deep end at the start. We'd help you get the basics of the game down. Plus, there are other girls around your height. You won't be alone!"
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
    MC "Yeah! You'll get to learn something new, and maybe make some new friends, too."
    GTS "That is true. I only worry that I have never been particularly good at sports."
    Fumika "Don't worry, when we're done with you you'll be an unstoppable dunking machine! I mean just picture it, being the star of the team!"
    $setAffection("GTS", -1)
    show GTS sad
    GTS "Apologies, I'm just not sure. Would it be alright if I took some time to think it over?"
    Fumika "Oh yeah, take as much time as you need! There's no rush. We're normally practicing at the gym after class on Thursdays, so if you want, you can just stop by. We'll introduce you to the rest of the team."
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
    GTS "...I can't believe it, either. I didn't think I was giving off that impression."
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
    scene School Planter
    show GTS happy at Position(xcenter=0.8, yalign=1.0)
    with fade
    "...as my eyes opened and I saw Naomi smiling down at me."
    play music Schoolday
    GTS "Very sorry Hotsure-san, I didn't mean to wake you."
    MC "That's okay. I, uh... wasn't aware that I had fallen asleep."
    GTS "Well, it is a very lovely day, so I can understand the appeal of just taking a nap."
    MC "Yeah, it's pretty peaceful today. How is the shodō going?"
    show GTS neutral
    GTS "It's going well, would you like to see?"
    "I sat up as Naomi placed her brush down onto the inkstone while I peeked at what she had created. The Kanji made me blush a little as I read, \"Dream\" upon the paper before hearing a giggle above me."
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
        "(Draw the Symbol for \"Human\")": # +0 Affection, +1 if stat higher than 2
            jump GTS019_c1_1
        "(Draw the Symbol for \"Cherry Blossom\")": # +2 Affection, +3 if art stat higher than 6
            jump GTS019_c1_2
        "(Draw the Symbol for \"Happiness\")": # +1 Affection, +2 if art stat higher than 4
            jump GTS019_c1_3

label GTS019_c1_1:
    "My mind drew a blank as I simply let my hand move with the first thought that came to mind, and as such my work was done almost as soon as it started."
    GTS "Let's see what you did."
    if checkSkill("Art", ">=", 2):
        $setAffection("GTS", 1)
        GTS "Ah, human. Interesting choice, Hotsure-san."
    else:
        show GTS embarrassed
        GTS "O-oh, a very... interesting style, Hotsure-san..."
        MC "Thanks, been a while since I did this."
    MC "Yeah... I kind of blanked there, so I let my hand take the wheel."
    GTS "That's all right. I'm sorry for putting you on the spot like that. Still, I think it came out nicely."
    "She carefully removed the paper and placed it in the pile along with the ones she had done."
    jump GTS019_c1_after

label GTS019_c1_2:
    "I had no idea what I'd go with as I stared at the white canvas before me. Then, just like I had been inspiration for Naomi earlier, I decided she would act as my inspiration here."
    "I got to work, planning out my movements before my hands executed them. As long as I focused, I could get this done."
    "After a few minutes passed, I finally let out a sigh of relief and placed the brush down."
    GTS "Let's see what you did."
    if checkSkill("Art", ">=", 6):
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
    else:
        $setAffection("GTS", 2)
        show GTS embarrassed
        GTS "Ah... I see what you went for, Hotsure-san. That was quite the brave effort."
        show GTS embarrassed at Transform(xzoom=-1)
        GTS "{size=-6}At least... I think I know what this is...{/size}"
        MC "Uh thanks..."
        show GTS embarrassed at Transform(xzoom=1)
        GTS "Ah! I mean no offense, Hotsure-san. Here, let's put it with the others..."
        "She carefully removed the paper and placed it in the pile along with the ones she had done."
    jump GTS019_c1_after

label GTS019_c1_3:
    "I pondered on what I could write down as a soft breeze blew my hair. That gave me the inspiration I needed, as I thought back to how peaceful the day felt and how it made me feel."
    "Smiling, I got to work with my project, making short strokes as I finished the art piece in a few minutes."
    GTS "Let's see what you did."
    if checkSkill("Art", ">=", 4):
        $setAffection("GTS", 2)
        GTS "Heh, a nice mood to have, Hotsure-san."
        MC "Yeah, I have to admit the atmosphere of today has made me rather happy."
        show GTS happy
        GTS "It makes me happy to hear that. The piece came out well, too."
        MC "Thanks, it's been a while since I've done shodō, but it was fun."
    else:
        $setAffection("GTS", 1)
        GTS "Ah, I see it. Happiness. A nice choice to go with, Hotsure-san."
        MC "Thanks, just went with how I was feeling."
        GTS "Well, I'm glad you're happy."
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
    $setTimeFlag("XX20")
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
    $setFlag("GTS020_c1_2")
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
    scene School Planter
    show GTS neutral
    with fade
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
    $setFlag("XX22")
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
    "Once I noticed that, I also noticed it was no math or science textbook, but a biography. \"The Life and Works of Nijō Yoshimoto\", its cover of weathered gray fabric and its lettering of simple, bold strokes."
    MC "Hm! Got an itching for the classics, eh?"
    GTS "Yes, quite! I very much like the presentation here. The way the author weaves Nijō-sama's poems into accounts of his life is very thoughtful and evocative."
    GTS "I borrowed it yesterday, and I must confess I continued reading a bit after I would normally go to bed."
    MC "Wow, sounds like interesting technique. Maybe I should check that out."
    if checkSkill("Academics", ">", 2):
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
        "Whose woods these are I think I know..." if checkSkill("Academics", ">", 6):
            jump GTS022_frost
        "On a bright, calm day..." if checkSkill("Academics", ">", 4):
            jump GTS022_nijou
        "There was an old drunkard from Devon..." if checkSkill("Academics", ">", 2):
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
    MC "Robert Frost, a rather esteemed American poet from the 20th century. That particular piece was called, if I remember right, \"Stopping by Woods on a Snowy Evening\"."
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
    MC "...who died and ascended to heaven.{w} But he cried, \"This is Hades!{w} There are no naughty ladies,"
    show GTS surprised
    extend " and the pubs are all shut by eleven.\""
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
    scene Office
    show AE neutral
    with fade
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
    scene Library
    show GTS neutral
    with fade
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
    if checkAffection("GTS", ">", 20):
        "I was genuinely surprised how much seemed to stick afterward, even if it wasn't everything. Something about the way she relayed things just cleared the blocks in my brain."
        "I told her that, in fact. She thanked me with grace and efficiency."
    scene Dorm Interior with fade
    "By the end of the day I returned to my room and buckled down for... something, in retrospect, I'd have never guessed I'd end up doing in a hundred years."
    "It came a hell of a lot easier than algebra, though. This time there was a light at the end of the tunnel, and Naomi's veiled, giddy smile behind me."
    scene black with fade
    stop music fadeout 4.0
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
    if checkSkill("Art", ">", 2):
        $setFlag("GTS022_artPass")
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
    if getFlag("GTS022_artPass"):
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
    if getFlag("GTS022_artPass"):
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
    if getFlag("GTS022_artPass"):
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
    if getFlag("GTS022_artPass"):
        MC "So all has been drank, now let us straighten ourselves, for her, down below."
        GTS "Oh!"
    else:
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
    if getFlag("GTS022_artPass"):
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
    $setAffection("GTS", 2)
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
    if checkSkill("Art", ">", 2):
        $setFlag("GTS022_artPass")
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
    if getFlag("GTS022_artPass"):
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
    if getFlag("GTS022_artPass"):
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
    if getFlag("GTS022_artPass"):
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
    if getFlag("GTS022_artPass"):
        MC "So all has been drank, now let us straighten ourselves, for her, down below."
        GTS "Oh!"
    else:
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
    if getFlag("GTS022_artPass"):
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
    $setAffection("GTS", 2)
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
    if checkSkill("Art", ">", 2):
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
    stop music fadeout 4.0
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
    MCT "\"Suave Bank\". Gotcha!"
    "I grabbed my quarry, tucked it in my pocket, and stood."
    show GTS surprised with vpunch
    MC "Bwoah!"
    GTS "Goodness!"
    "From just around the corner, Naomi stood before me clutching a platter while a few cookies bounced and crumbled on the ground."
    menu:
        "Aw sick, you made cookies?" if checkSkill("Art", ">", 6):
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
    show GTS neutral
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
    "We arrived on the scene with Tanaka-san visibly brainstorming with herself in her chair, extras standing around chatting, and Honoka, her co-star, and the cameraman doing the same over packs of seaweed, sitting down."
    "After the jumpstart a few moments ago, the stillness eased my heart to a contented rhythm."
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
        hide GTS
        hide Ryoko
        with dissolve
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
        show GTS sad
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
    show GTS neutral
    GTS "I'm not sure what you're getting at."
    MC "Nobody else in our class except maybe Kodama-san is as patient, or as selfless, or just... generally chill to be around as you."
    show GTS embarrassed
    GTS "That's... very flattering."
    MC "Really, who else?"
    show GTS neutral
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
    show GTS neutral
    MC "Right. That was insensitive of me, sorry."
    GTS "I don't hold it against you. You were only trying to help."
    "I nodded, but wanted to let nothing more past my lips for a moment."
    "Instead, we walked a little farther together in silence. Her hair was aflame in the dusk sunlight, as mine likely was as well."
    MC "So, I guess this is good night?"
    GTS "That sounds agreeable to me."
    show GTS surprised
    pause 0.75
    show GTS embarrassed
    GTS "Oh, dear, I didn't mean it like that..."
    MC "Heh, nah, I get you. Take care, Yamazaki-san."
    show GTS neutral
    GTS "And you also."
    hide GTS with dissolve
    "With that, we parted ways, the distance growing between us in the shade."
    "And I stuck my hands in my pockets, felt a pen or two inside them, and sighed."
    jump daymenu

label GTS024:
    $setProgress("GTS", "GTS025")
    $setTime(TimeEnum.RAIN)
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
    if checkSkill("Academics", ">", 4):
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
    scene Hallway
    show GTS happy
    with fade
    GTS "Hm hm hm. I believe the idea is to talk to the plants up close."
    show GTS neutral with dissolve
    MC "I'm sure they got the picture."
    GTS "The ease of your levity never ceases to amaze me."
    "We proceeded down the ramps towards the ground floor, passing small, dispersed groups of students hanging around and chatting in the dim gray light."
    "Naomi began walking with a little more oomph once we neared the entrance, and I found myself having to full-on fast walk to keep up."
    scene Gate Front
    show GTS neutral
    with fade
    MC "Where are we going, exactly?"
    GTS "Well, the groundskeeper graciously allowed me to keep a jug of my plant food by the supply shed. And I believe I have a suitable eyedropper in my dormitory."
    GTS "I hope you don't mind a bit of a trip."
    MC "Just those places and back? Nah, not at all."
    "She gave me a shallow but considered bow."
    GTS "Thank you."
    scene Campus Center
    show GTS neutral
    with fade
    if checkSkill("Athletics", ">", 2):
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
    "\"Plant Food\""
    "\"Please do not drink\""
    "Naomi knelt down on the shaded grass and looped three fingers through the jug's handle, the fourth having no room, and then stood; the liquid didn't slosh a bit as she cupped her other hand under the jug."
    MC "Alright, there's step one."
    GTS "Indeed. Now, we just have to get my eyedropper."
    MC "Right, right. Ladies first, of course."
    show GTS happy
    GTS "Such a gentleman!"
    "I only just heard her chuckle under her breath, and we began treading directly across the grass to the girls' dorms."
    scene Dorm Exterior
    show GTS neutral
    with fade
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
    if checkAffection("GTS", ">=", 30):
        GTS "Well, I have another, faster idea..."
        "She craned her neck to look over at the boys' dormitories; I did too, and saw that there didn't seem to be anyone around there, either."
        show GTS embarrassed with dissolve
        GTS "It might be considered a bit uncouth..."
        MC "You? Having uncouth thoughts? Please, do tell."
        GTS "Well, what if we were to walk over there together?{w} At the same time...{w} under my umbrella?"
        "Some air caught in my chest for a second and I prayed the clouds obscured the blush I could feel coming on."
        if checkSkill("Academics", ">", 1):
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
        scene black with fade
        $setTime(TimeEnum.DAY)
        pause 2
        scene Dorm Interior with fade
        "As it happened, I would not be back in just a minute."
        MCT "C'mon, show yourself you stupid piece of junk..."
        "I had overturned just about every conceivable umbrella-sized object in my section of the room and was halfway considering checking the bathroom or cutting open my mattress."
        "And as I looked at that mattress, I noticed my wrinkled raincoat half-buried under the sheets."
        "I pulled it out and chanced to feel around inside the pockets."
        MCT "...Yep."
        "I thanked the stars at least Daichi wasn't there to see that in person as I left again and headed back down to the entrance."
        scene black with fade
        $setTime(TimeEnum.RAIN)
        pause 1
        scene Dorm Exterior
        show GTS neutral
        with fade
        GTS "You found it?"
        MC "Eventually. Apologies about the delay."
        GTS "Think nothing of it. If absolutely nothing else, turnabout is fair play."
        MC "Very well, then. I do believe we have a garden to attend to."
        show GTS happy with dissolve
        GTS "Precisely."
        hide GTS with dissolve
    else:
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
    scene black with fade
    "She picked up her jug and we made our way up the stairs, umbrellas ready. I managed to reach the door first, and soaking up a few seconds of unabated rain before holding the door for Naomi to huddle through."
    "I resolved, to myself, to appreciate the open air more."
    jump daymenu

label GTS025:
    $setTimeFlag("XX25")
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
    RM "I said \"maybe\"."
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
    scene Classroom
    show HR neutral
    with fade
    HR "...And if there are no other questions, remember there's a quiz on chapter 4 tomorrow."
    HR "And for whoever needs to hear this, any copy that comes back to me with glitter on it is getting a zero. Hope that's clear enough."
    HR "Alright, dismissed."
    show HR unique
    "I slapped together my things and dumped them into my backpack as gracefully as I could manage, before standing to try and follow Naomi out the door."
    "As I did so, passing the head of the room, I caught Tashi-sensei glancing at me; I stopped."
    MC "..."
    show HR neutral
    HR "Got a question, Hotsure?"
    show HR unique
    MC "No, sensei."
    show HR neutral
    HR "Fantastic. See you tomorrow."
    show HR unique
    "His expression didn't change at all for the entire exchange. I bowed, and he nodded and returned to his paperwork."

    scene Hallway with fade
    "Luckily, I had a strong hunch where Naomi was going."
    "I picked up the pace in her footsteps; just as we came within sight of the exit out to the roof, she turned her head slowly and I caught a glimmer of amber."
    show GTS neutral with dissolve
    GTS "Good afternoon, Hotsure-san."
    MC "Same to you, Yamazaki-san. How're you doing?"
    GTS "I am well, and I'm glad you have decided to join me."
    MC "Of course! Shall we?"

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

    scene Hallway
    show GTS neutral
    with fade
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
    "We continued together to have lunch with what time remained. Of course, we spared a second to say \"itadakimasu\"."
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
    if checkSkill("Art", ">", 3):
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

    scene Field
    show GTS neutral
    with fade
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
    if checkAffection("GTS", ">", 20):
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
    stop music fadeout 3.0
    "Naomi took the moment to ease her finger through her teacup handle and lift it for a sip."
    "Her eyes drifted closed as she took it in, and I could see the languor with which she savored the hot brew."
    "I felt compelled to take a sip of mine, too. Her eyes opened as I did, but she waited for me to finish."
    play music GTS
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
    if checkAffection("GTS", ">", 20):
        GTS "There's a wholesomeness in you, Hotsure-san, and I can tell that it's genuine."
        GTS "So often you know just what to say, and not just to me, it seems, but to almost everyone."
        if checkSkill("Academics", ">", 5):
            GTS "You clearly have a good head on your shoulders, as well."
        if checkSkill("Art", ">", 5):
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
    if checkSkill("Academics", ">", 2):
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
    "The muscled young cook's quick work soon made good on his father's promise, hardly breaking a sweat through Ryoko's spiderweb of an order."
    "We were off with warm ceramic bowls in our hands... Naomi quickly found it easier to hold hers in one... and we scanned the room for a bench table."
    "Minori squeezed by first with a muttered apology and sat in one corner, laying her clipboard on her lap."
    "Ryoko followed, bending her arms to avoid a handful of idle customers, and scooched in next to her faithful companion."
    show GTS surprised #note to self, an embarrassed sprite would be ideal
    GTS "Would you like to go first, Hotsure-san?"
    MC "Nah, I wouldn't want you squished up against the wall. You can go if you want."
    GTS "Well, that's very considerate of you."
    "She brought her arms in around her waist as close as she could, at which point most of the people standing around made some room."
    GTS "Pardon me..."
    "She shimmied around the table's edge and up next to Ryoko before seating herself; though the seating was clearly built with factors in mind, I yet beheld Naomi's head-sized silken shoes and just a bit of her shins peeking out from the shadow of the table."
    show GTS surprised
    "She noticed, too, and promptly drew them back until her knees hit the plywood."
    show GTS neutral
    "Then it was my turn, and thankfully it looked like I had just enough room."
    MC "Hm..."
    "I was squeezed against the wall, but also the stiff but still soft plastic cushion, as well as Naomi's skirt-swaddled left hip, more like a giant, warm pincushion. Not bad accommodations, all told."
    "I looked up at the faintest blush on her cheeks as she closed her eyes and brought her hands together. I followed suit."
    All "Itadakimasu."
    Ryoko "-kimasu."
    MC "Smells pretty good."
    show GTS happy
    GTS "That it does."
    "I bundled up some in my chopsticks and took a bite; I was not disappointed."
    show Ryoko happy
    Ryoko "Mm-mm! They nailed it, it's flawless."
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
    MC "How's yours, Yamazaki-san?"
    "She tapped her chin with the thick ends of her chopsticks."
    GTS "It reminds me a great deal of when my friends and I would try out different restaurants in Kyoto."
    MC "I see. Not your favorite?"
    show GTS neutral #another spot where an embarrassed sprite would be useful
    GTS "I do usually prefer a bit crisper scallions."
    show GTS neutral
    extend " Otherwise, it's rather tasty."
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
    if checkAffection("GTS", ">", 20):
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

label GTS028S_c2_2:
    Ryoko "Alright, that makes it easy. What about you, Yamazaki-san?"
    $setFlag("GTS028S_noask")
    jump GTS028s_c2_3

label GTS028S_c2_3:
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
    GTS "I don't mean to impose, of course. I could go some other day."
    MC "No, no, it's fine. Just... that was kinda the plot twist of the century just now."
    show Minori neutral
    show GTS happy at Transform(xzoom=1)
    GTS "I'm no stranger to electronics, you know. My parents furnished me with a cell phone."
    show Ryoko confused
    show GTS neutral
    GTS "After all, isn't this the time to broaden our horizons?"
    MC "Can't argue with that."
    show Ryoko neutral
    Ryoko "You make a good point. Well then, let's head over there."
    MC "I think this way's the shortest way."
    "I led the way again through the streets."
    "And so as much as I wanted to steal a glance at Yamazaki-san's face, I couldn't."
    MCT "It hasn't even been a week since we had dinner together. I knew there'd be a lot more to learn about her, but... how many of my other assumptions are wrong?"
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
    MC "So these little ones are what's called \"handheld\", the console for these is portable."
    GTS "I see... oh, that one looks interesting."
    "She daintily pinched the corner of one box depicting a pale, wide-eyed woman in a kimono, looking through a spiderweb. Naomi beheld the cover with an appreciative smile as I glanced at the title:{w} Onku: Fatal Siren."
    MC "I, uh, don't think you would like that one."
    GTS "Oh, I see."
    "She gingerly put it back and bent down a little to scan the other games on display."
    GTS "This one has some enticing cover art as well. What do you make of it?"
    "I looked down and saw the cover's depiction of a blue-haired girl... I think... standing in shallow water, a cardinal perched on her outstretched finger. \"Chrysanthemum Tussle: Farewell, My Friend.\""
    MC "Oh, I think I heard of that."
    GTS "Do you think I would enjoy it?"
    MC "You... might? I can't really comment, visual novels kinda put me to sleep."
    GTS "I see. Well, let's try a different tack. What are some video games {i}you{/i} regard highly?"
    MC "Uh, me? Hm...{w} I play Silver Moon a lot. It's pretty fun."
    GTS "What about it?"
    MC "The gameplay's fun, and it does some interesting stuff with how you can use the characters' abilities."
    MC "I used to play the two-player mode with Tomo-chan when we were tweens. So I guess you could say it's all my fault."
    show GTS surprised
    GTS "Oh? How do you mean?"
    MC "She's, uh... {w}how do I put this...{w} she prefers alternatives to sunlight."
    show GTS happy
    "A crackling chuckle escaped her."
    GTS "I'm sure your intentions were unimpeachable."
    MC "Ha, yeah."
    show GTS neutral
    MC "If I had to pick, like, my favorite game ever, I'd have to say... Magiria Knight 2."
    GTS "What is it about?"
    MC "So you play as this young kid with a magic sword, and he gets his arm cut off early in the story..."
    show GTS surprised
    GTS "Goodness!"
    MC "Yeah, and so he gets this robot arm instead, and you go through the game helping people fight this evil empire, and he gets more gadgets to put on his arm as you go along."
    show GTS neutral
    MC "It had a really good story, too. I won't spoil it too much but there's some really good subtle stuff as the story progresses, the characters are all really good, and the way the main guy's character develops is really..."
    MC "..."
    stop music fadeout 1.5
    GTS "Really what?"
    "I smirked."
    MC "You don't really want to try it yourself, do you?"
    play music GTS fadein 1.0
    show GTS surprised
    GTS "Oh... was it so obvious? I meant no offense..."
    MC "None taken. But you know, Yamazaki-san, you don't have to go to all that trouble just to get to know me. Anything you want to know, {i}anything{/i}, all you have to do is ask."
    show GTS neutral
    GTS "That is good to know. But would you have answered as plainly or thoroughly as you did had I simply asked you?"
    MC "Of course I... uh... maybe?"
    "I stood in upended silence there in the Pretendo aisle, realizing I'd never much considered {i}why{/i} Naomi did things the way she did."
    MC "Uh... well... I guess you're right."
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
    "I smiled as I looked up at her, not knowing how she had just the words for every occasion. But I didn't care anyway."
    MC "Well, where was I..."
    stop music fadeout 1.5
    scene black with fade
    $setTime(TimeEnum.EVE)
    pause 1
    scene Town with fade
    "Naomi shut out everything, it seemed, except what I was telling her. Eventually, I was the one who had to remind her that Ryoko and Minori would be waiting for us."
    show Ryoko neutral at Position(xcenter=0.8, yalign=1.0)
    show Minori neutral at Position(xcenter=0.2, yalign=1.0)
    show GTS neutral
    with dissolve
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
        Cashier "Okay, that brings your total to zero, and ma'am, you've got 900 left on this voucher."
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

    scene Town
    show Ryoko neutral at Position(xcenter=0.8, yalign=1.0)
    show Minori neutral at Position(xcenter=0.2, yalign=1.0)
    show GTS neutral
    with fade
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
    $setProgress("GTS", "GTS029")
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
    Ryoko "It's like my teacher always said, \"If you don't know what to watch, go with the jokes.\""
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
    if checkSkill("Art", ">", 35):
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
    if checkSkill("Art", ">", 35): #this is WAY too high
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
    GTS "I'm afraid I'm not feeling too hungry at the moment, so I'll take my leave. I'll see you later Hotsure-San."
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
    $setVar("GTS_selfhood", getVar("GTS_selfhood") + 1)
    MC "I trust you can handle yourself, Yamazaki-san. The stuff you have left should be of no problem to you at your current size."
    show GTS happy at Position(xpos=0.5, xanchor=1.0, yalign=1.0) with dissolve
    GTS "It shouldn't be a problem at all. I'd hate for you to waste your time with such a menial task."
    if checkAffection("GTS", ">", 15): #FIXME
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
    MC "I could go for a cup. It's been a while since I've had a cup of home-brewed tea."
    "She held open the door for me. I suppose she didn't want it to hit me on the way in."
    "The dorms inside had changed slightly since I'd visited yesterday. For one, there was some more furniture, like a couch, a table, some chairs, and nearly a full kitchen."
    "Though all the new additions had a similar utilitarian aesthetic as the rest of the dorm, it was good to see some of the space filled."
    MC "Did the school provide furniture and appliances?"
    GTS "Yes, they did. Early this morning, several trucks showed up and delivered all this stuff. I'm glad they did, as last night I was worrying where I'd get furniture my size."
    MC "Now you've got me curious. Where DOES Seichou get furniture this big?"
    GTS "One of the other students here mentioned there's a shop away from town disguised as a hill."
    GTS "I believe they said it was called Mt. Fuji Outfitters. It's run by a former student, like many of the other shops around town. They mainly sell clothes, which is pretty good to know since mine are starting to get a bit tight."
    MC "I'm glad that the island and the school have ways to provide for everyone. Now all we need is a place that makes wigs, and I'll be their first customer."
    "Naomi chuckled as she began prepping a pot of tea on the stove."
    MC "I hope that moving your stuff from your old dorm wasn't too hard."
    "Naomi's expression sank a little at the question."
    hide GTS
    show GTS_S sad
    GTS_S "Yes, it was quite easy to move everything over. However, I realized something while I was doing it."
    "She grabbed two moderately-sized boxes off of the nearby tabletop and placed them in front of me."
    GTS_S "I can't wear any of the clothing that I brought with me anymore. None of my clothes fit, and all of my school supplies don't fit my hands. None of this is usable."
    "She paused for a moment before shaking her head and turning her mood around."
    hide GTS_S
    show GTS neutral
    "Although she was clearly feeling unwell, Naomi seemed to be able to collect herself almost immediately. With a deep breath, she slowly returned to her original position."
    GTS "Well, it's best to not dwell on what has been lost. If you find anything in here that you can use, you can keep it. Otherwise, I'm gonna donate them."
    "I opened one of the boxes, finding some mugs and silverware resting atop what I assumed was her wardrobe."
    MC "You know, you could probably keep some of these things for visitors. You can't use them, but whenever you have company, they can use the dishes and silverware."
    show GTS happy
    GTS "That is a good point. I'm glad you thought of that. I was so caught up in getting myself settled, I hadn't stopped to consider future guests."
    MC "I'm glad I could help you with that. I hope you weren't concerning yourself with the idea of having guests so soon after moving in."
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
    GTS "I can't complain about anything so far. It's very nice here."
    MCT "She's not admitting something but I'd hate to ruin her mood by digging into it."
    MC "I'm happy to hear that. I'm sure Ryoko will be happy to hear that you're doing well."
    show GTS neutral
    GTS "If you could tell her, I'd appreciate it. I'd hate for her to be worrying about me."
    MC "Did you speak to her when you went back to the dorm?"
    hide GTS
    show GTS_S sad
    GTS_S "No, she was out filming, I suppose. Either that, or hanging with her friends from the film club."
    MC "Well then, I will make sure to speak with her since you asked so nicely."
    hide GTS_S
    show GTS neutral
    GTS "Only do it if it isn't a bother, please. Otherwise, I'm sure I can find time to do it myself."
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
    GTS "Class participation, unfortunately, doesn't work. We're still required to submit our homework on time."
    MC "How does that work? I can't recall seeing giant sheets of paper on Tashi's desk before."
    GTS "One of the students here works as a teacher's assistant. They handle all the homework grading and just pass the results to the correct teacher for entry into the system."
    GTS "Even with all that, do you want to know what the craziest thing about The Caverns is?"
    show GTS happy-2
    GTS "Being inside there makes me feel normal. It's hard to describe, but inside there, the ceiling is nearly 30 meters tall. Everything feels so natural and safe. I don't have to hunch over, or squeeze through doors. I'm free again."
    "I could see some tears forming in her eyes as she said those last words until she wiped them away. She took a moment to recompose herself before continuing."
    show GTS neutral
    GTS "Sorry about that. The tea is still quite strong, so it made me tear up."
    MC "You don't need to apologize. I was interested in all of it. The giants' area isn't an area many students get to see often, so hearing how it operates is quite fascinating."
    GTS "I'm glad you enjoyed my rambling there, I was afraid I got lost there for a moment in my own world."
    "She pauses again staring into her tea for a moment before sipping it."
    hide GTS
    show GTS_S sad
    GTS_S "Do you like me, Hotsure-san?"
    MC "Of course I do, Yamazaki-san. I wouldn't have shared a kiss with you if I didn't."
    GTS_S "Why me, though? There are plenty of normal-sized people at school, yet you chose me."
    MC "Well, you are incredibly kind to everyone you meet. Your knowledge of gardening and plants is beyond compare. I suppose you've never given me a moment to doubt that you are an amazing person."
    MC "That's why I've stuck with you, regardless of whatever problems you believe it'll cause."
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
    MC "Perhaps I could join you next time? You've confirmed that this is an experience I can't miss."
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
    MC "What the hell {i}do{/i} they mean by \"cookies,\" anyway..."
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
    show HR unique at Position(xpos=0.15) with dissolve
    "Tashi-sensei stood up from his desk at the corner of the room with a firm, confident look in his eyes, as if about to say something. I decided to address the lingering question before he began the lesson."
    MC "I... helped Yamazaki-san move out over the weekend. She's been transferred to the giant dorm."
    show FMG surprised at Position(xpos=0.30)
    show WG surprised at Position(xpos=0.45)
    show PRG surprised at Position(xpos=0.60)
    show BE surprised at Position(xpos=0.70)
    show AE neutral at Position(xpos=0.85)
    with dissolve
    "Mixed expressions of surprise, relief, and intrigue filled the room as I answered Honoka's question. Tashi-sensei seemed to be the only one that didn't visibly react at all."
    show HR neutral
    HR "Ah, so that's what's happened, then. I'm certain that they'll have an appropriate lesson plan for her."
    show HR unique
    MC "You don't exactly sound surprised, Tashi-sensei."
    show HR neutral
    HR "I was informed ahead of time that Yamazaki-san's condition would mean that she wouldn't be staying with us. Since it all depended on her growth rate, no exact date was given."
    hide FMG
    hide WG
    hide PRG
    hide BE
    with dissolve
    show HR unique
    AE "Is there any specific height threshold where the transfer is made?"
    show HR neutral
    HR "The medical staff make the call as soon as a student begins brushing the ceiling. Even with our custom-built amenities, this campus is only equipped to deal with heights of 350cm and below. Beyond that, it becomes far too inconvenient to move around."
    show HR unique
    AE "...I see. That's the cutoff point, then."
    show HR neutral
    HR "More or less. I've seen students come and go many times before, often for that very reason. It's best to transfer them right away, to avoid any potential property damage."
    show HR unique
    hide AE with dissolve
    show FMG sad with dissolve
    FMG "Does that mean Naomi's never coming back?"
    hide FMG with dissolve
    show HR neutral
    HR "While there aren't any rules explicitly stating that she CANNOT ever enter the building again, it's extremely ill-advised for her to try."
    HR "Yamazaki-san is still free to walk around the outdoor areas of campus however she pleases, as long as she avoids property damage."
    show HR unique
    show BE happy with dissolve
    BE "Well hey, that doesn't sound bad at all! She could even peek in through the window!"
    hide BE with dissolve
    show HR neutral
    HR "Our class will be livestreamed to her via video call. She won't miss anything, and you'll still be able to talk to her outside of class."
    show HR unique
    "A heavy sense of relief circulated throughout the rest of the room. I slowly saw the faces of all of my classmates return to their usual, collected selves."
    "It seemed that this wouldn't be as big of an adjustment as we had initially thought. Naomi wasn't even moving very far; she'd still be mere meters away, talking to us in a video call."
    show HR neutral
    HR "If there are no further questions, I'd like to begin today's lesson plan."
    show HR unique
    "Those who had left their seats returned to them as Tashi-sensei returned to the board. Despite the expanded bodies of my classmates, the room still felt spacious and empty without Naomi. Even so, my classes proceeded as usual."
    "After saying my goodbyes and packing up for the day, I knew where I'd be heading next."

    scene Giant Dorm Exterior with fade
    "Before long, I had found myself at the door to Naomi's room. Once again, I found myself at the front of an aircraft hangar, painted only with very basic colors and numerical labels."
    "It was still rather foreign to me how it looked more like a military base with all of the repurposed hangars lined up in a row."
    "I could tell that the architects at least made SOME effort to make the place look \"homey,\" though. The lighting rigs adorning the tops of the doors bathed the area in white light, which illuminated all of the walking space."
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
            $setVar("GTS_selfhood", getVar("GTS_selfhood") + 1)
            show GTS embarrassed
            GTS "Oh, I'm certain it wasn't that bad. You'd hardly notice that I'd be gone."
            $setAffection("GTS", 1)
            MC "Well, of course it'd be lonely. We value your company. It's just not the same if we see you over a stream."
            show GTS aroused
            GTS "The importance of remembering those close to you is a value that often goes unnoticed. I'm flattered that you were thinking about me."
            show GTS neutral
        "The others were asking about you.":
            GTS "I... I see. What, exactly, was said about me? Have I caused them to worry?"
            MC "I wouldn't say \"worried,\" no. They were just... asking about you. Wondering where you were."
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
    MC "I can agree with that. Hell, the only reason I'm still able to see is because I have the discipline to actually wash and comb this haystack I call \"hair.\""
    "Naomi giggled, keeping her hand close to her mouth to keep it covered."
    GTS "Hygiene is important, of course, but I meant your drive. What motivates you, Kei-chan? What would you consider to be your greatest strength?"
    if checkSkill("Art", ">", getSkill("Athletics")):
        if checkSkill("Art", ">", getSkill("Academics")):
            if checkSkill("Art", ">=", 7):
                $setAffection("GTS", 1)
            jump GTS032_art
        elif checkSkill("Art", "==", getSkill("Academics")):
            if checkSkill("Art", ">=", 7):
                $setAffection("GTS", 1)
            menu:
                "My artistic prowess.":
                    jump GTS032_art
                "My supreme intellect.":
                    jump GTS032_academics
        else:
            if checkSkill("Academics", ">=", 7):
                $setAffection("GTS", 1)
            jump GTS032_academics
    elif checkSkill("Art", "==", getSkill("Athletics")):
        if checkSkill("Art", "==", getSkill("Academics")):
            if checkSkill("Art", ">=", 7):
                $setAffection("GTS", 1)
            menu:
                "My artistic prowess.":
                    jump GTS032_art
                "My supreme intellect.":
                    jump GTS032_academics
                "My athletic pursuits.":
                    jump GTS032_athletics
        elif checkSkill("Art", ">", getSkill("Academics")):
            if checkSkill("Art", ">=", 7):
                $setAffection("GTS", 1)
            menu:
                "My artistic prowess.":
                    jump GTS032_art
                "My athletic pursuits.":
                    jump GTS032_athletics
        else:
            if checkSkill("Academics", ">=", 7):
                $setAffection("GTS", 1)
            jump GTS032_academics
    else:
        if checkSkill("Athletics", "==", getSkill("Academics")):
            if checkSkill("Athletics", ">=", 7):
                $setAffection("GTS", 1)
            menu:
                "My supreme intellect.":
                    jump GTS032_academics
                "My athletic pursuits.":
                    jump GTS032_athletics
        elif checkSkill("Athletics", ">", getSkill("Academics")):
            if checkSkill("Athletics", ">=", 7):
                $setAffection("GTS", 1)
            jump GTS032_athletics
        else:
            if checkSkill("Academics", ">=", 7):
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
    GTS "We... let our minds become locked. We believe that \"this is our reality, and nothing can be done to change it.\""
    jump GTS032_after

label GTS032_after:
    GTS "Just don't forget to give yourself some \"me\" time every now and then. Discipline and drive can only get us so far, Kei-chan. We need happiness, enjoyment, and leisure time just as much as our goals."
    MC "I'm giving myself \"me\" time right now!"
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
    if checkSkill("Academics", ">", 5): #tbd?
        "As I had done many times before, I served Naomi and myself a bowl of rice."
        "Next, I looked to Naomi and we both said \"itadakimasu\"; with that out of the way we dug into our meal. Once finished, I placed my chopsticks back into place and we both said \"gochisōsama deshita\"."
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
    $setFlag("XX35")
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
    GTS_S "Hotsure-san... I just wanted to say \"thank you\" again for doing this. If you don't wish to do this, you can just say so. I know we've only been dating for a little while, so this may be rather sudden."
    MC "Trust me, Naomi-chan. I'm certain that I want to do this. I'm interested in you, and if that means meeting your parents, then I'll do it."
    show GTS_S neutral
    GTS_S "Thank you, Hotsure-san... wait, did you just call me \"Naomi-chan?\""
    MC "I did. Must've slipped out on accident."
    GTS_S "Let's keep the names formal for today and discuss the matter later."
    MC "I understand, Yamazaki-san. Now, pardon me while I get ready."
    "I closed my window and got ready all the while I could hear Naomi humming the same tune to herself."
    if checkSkill("Art", ">=", 6):
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
    if checkSkill("Athletics", ">=", 7):
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
    if checkSkill("Art", ">=", 6):
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
    "Others were more intended for enthusiasts, with binders that featured characters from various anime and video games. A bright, vibrant \"OPEN\" sign accompanied the display."
    "Naomi seemed interested as we walked past, crouching down to make herself eye-level with the glass."
    show GTS_S happy
    GTS_S "Ahh, that reminds me. I should really get back into painting."
    MC "You enjoy painting, Yamazaki-san?"
    show GTS_S neutral
    GTS_S "Well, calligraphy. I enjoyed painting banners when I was a kid. There's something innately satisfying about seeing a bold, perfectly shaped line of kanji painted in an appropriate color."
    GTS_S "To me, it's like a statement using far more than writing alone. The brushstroke can accent the word, or create a dichotomy where it doesn't match the word at all."
    GTS_S "For example, if one were to write the character for \"anger\" in a very thin, subtle brushstroke."
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
    if checkSkill("Athletics", ">=", 7):
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
    "She bowed at the still quite shocked Barker. As she stepped away I could swear I heard him muttering under his breath, \"But that shouldn't have worked.\""
    MC "Nice work on that game. Remind me next time I need a nail fixed to call you up."
    GTS_S "It was nothing, Hotsure-san. That man was rude to you so I needed to protect your honor."
    "We shared a chuckle but as I looked back at the game once more I noticed that the bell now had a large peg-shaped dent in the bottom."
    MCT "Geez, didn't know she was getting that strong."

    scene Ryokan Room with fade
    stop music fadeout 1.0
    play music GTS
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
        if checkSkill("Art", ">=", 6):
            Akihiro "It is reassuring to know you were able to dress properly for this occasion."
        else:
            Akihiro "I suggest the next time we meet, invest in some more appropriate attire."
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
    "It had been two days since the meeting with Naomi's parents, and things had been quiet between us."
    "This left me plenty of time to repeat the dinner scene over and over. Her father had been particularly difficult to deal with, but not in a way that was malicious."
    "It had grown apparent the task that lay ahead of me in rising not only to Naomi's standards, but her family's too."
    if checkAffection("GTS", ">", 30):
        extend " But it would be a small price to pay."
    "Eventually, I had to roll out of bed and get to work on my homework. A shower would hopefully allow me some time to destress."
    play sound Knock
    play music RM
    RM "Hey Hotsure-san, you got some mail."
    MCT "...From who?"
    show RM neutral with dissolve
    "Opening the door, I could see a box wrapped in brown paper clutched under Daichi's arm."
    RM "There's this letter, too. They're both addressed to you."
    "He produced a small envelope with a green wax seal."
    RM "Whoever sent you this evidently has no idea what email is. Who the hell owns a wax stamp?"
    MC "Not everyone owns a top end laptop. Some people don't even have internet."
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
    "After fiddling with it a bit more, I eventually found a spot on my shelf to display it. The tanto must've had a link to Naomi, because the moment the metal left my fingers my phone buzzed."
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
    "As I approached the small park area, I couldn't help but be in awe how Naomi was nearly as tall... or taller... than the trees around her. Granted, many were cherry blossoms, but it was still a considerable line to cross."
    MC "Yamazaki-san!"
    show GTS despaired-thought with dissolve
    GTS "Oh. Good evening, Hotsure-san."
    "Her tone was different, like cracked glass, her usual smoothness absent and poorly substituted."
    MC "Sooo, uh... why the short notice text?"
    GTS "I will explain shortly. Did you receive the package from my parents?"
    MC "The tanto? Yeah, I picked out a spot for it above my desk."
    show GTS neutral
    GTS "I'm glad that you took it so well. I was unsure how you would receive it when father informed me that he'd given that to you. I assume that he attached a letter as well?"
    MC "Yep, he said he hoped that it would serve as a visual symbol of hope for our relationship."
    GTS "He normally isn't that forward with people, especially concerning matters related to his family."
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
    GTS "Well, back then I wasn't certain what to think, or even where I'd be in due time. This past weekend brought that feeling back, and I wanted to find out if it's mutual."
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
    MC "I wasn't sure when we first met what the feeling in my chest meant, but the more we've talked, I've only grown more certain that it's love."
    $setAffection("GTS", 1)
    show GTS happy
    GTS "I shared those feelings, but wasn't sure if I could trust them."
    show GTS neutral
    GTS "I know, despite that, I've asked of you a number of things you would be well within your rights to move on for."
    MC "You know there was no real choice."
    show GTS unique
    "A sputtering grin escaped her, before with a wave of her hand she composed herself again."
    if checkAffection("GTS", ">", 70):
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
    GTS "I feel that you've expressed an interest in me, since you were willing to go so far as to meet my family."
    GTS "I hope that I have conveyed my interest in you as well. But then, to answer your question, I want to know how {i}you{/i} see our relationship."
    if checkAffection("GTS", ">=", 40):
        MC "Well, I've sort of... been in this kind of thing before, I guess. But never with someone like you. I guess I sort of feel like... I want to try to live life the way you do."
    else:
        MC "I'm still figuring that out for myself."
    "She nodded."
    GTS "Based on your experience, how do you feel? Do you see us as a couple? Are you comfortable with saying that you love me?"
    jump GTS036_menu

label GTS036_c2_3:
    MC "Well, \"love\" is a very complicated word. I don't know if I'm ready to say it yet."
    show GTS neutral
    GTS "Then what are you ready to say?"
    MC "Huh?"
    GTS "If not \"love,\" then what?"
    MC "I mean, I respect you a lot. You've got a lot of talents, and you're always so chill and nice. I just like spending time with you."
    show GTS despaired-thought
    GTS "So, you enjoy spending time with me, but you're afraid of the implications that come with saying that you love me. I understand. It can't be an easy thing to say."
    GTS "I'm curious about one other thing, if you would indulge me. What is love to you?"
    if checkAffection("GTS", ">", 60) and checkSkill("Art", ">", 5):
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
    elif checkAffection("GTS", ">", 40):
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
    "She remained in my sight only until I exited the park gate. I walked out on surer steps than I came in with; energy that I didn't know I had powering my strides."
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

    scene Dorm Interior
    show RM neutral
    with fade
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
    GTS "I don't want to come across as scary, but I don't want others to think I'm belittling them either. What should I do?"
    MC "I don't think you can take the same approach with every single person you meet. It might just be something that doesn't have a universal answer."
    MC "What do the other giants do?"
    show GTS neutral
    GTS "You know, that is a good question. Most often, when I see the other giant students, they're either speaking amongst themselves, or just watching their classes on the projector screen."
    GTS "The few times I've seen the giants and faculty interact, they'd be sitting down while the medical staff run diagnostics on them."
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

    scene Mountains Torii Gate
    show GTS neutral
    with fade
    "Naomi nodded while looking down at me."
    GTS "If nothing else, being outside in the wilderness allows me to breathe much fresher air. Sometimes, I forget what \"outside\" is like in the giant dorms."
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

    scene Mountains Shrine
    show GTS happy
    with fade
    "Naomi's face met mine as I opened my eyes, her smile taking up most of my field of vision. She had lowered her position even further to meet my gaze, still in the same position as she was when we first arrived."
    GTS "Thank you for being here with me today. This was fun."
    MC "It's so quiet out here. I almost forgot where we were."
    show GTS neutral
    GTS "It is quite a ways away from campus, isn't it? It's difficult to believe that such a vast mountain range is out here. It feels rather disconnected from the rest of the world."
    MC "Not that it matters, as long as I'm here with you."
    GTS "I'm flattered that you feel that way, Kei-chan."
    "The two of us turned around, leaving the shrine behind. The smoke trails from the burning incense still lingered, coating the area outside the shrine in a thin layer of white vapor."
    GTS "Do you mind if we take our time walking back down the trail? I'd like to... remember this view. Take in all of the scenery."
    MC "Not at all."
    "The two of us proceeded to walk back down the trail. Naomi walked in front of me, intentionally making her strides slow and delicate so I could keep up. The stones were sturdy, and didn't vibrate at all under Naomi's light steps."

    scene Mountains Torii Gate
    show GTS unique
    with fade
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
    "Hearing the word \"giant\" appeared to unsettle her, however. While her composure quickly returned, I could tell that she didn't appear comfortable being called one."
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
        show GTS_S happy
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
    "Two o' clock on the hottest Sunday afternoon since summer began. My scuffed-up old copy of Silver Moon was spinning away in my Aystation and Typhon was down to a third of his health. I couldn't remember the last time I got that far."
    "Golden sunrays shone in piercing the glass and the curtains; the angels themselves were witnessing me."
    MC "Oh what the hell, now you get {i}three{/i} turns?"
    "Lest my confidence drown me, I suddenly found half my party poisoned and the other half knocked out."
    "I slumped backwards onto the floor while hissing a sigh through my teeth, as if I were pneumatic. There I formed my own dark sun, with hair spread out a meter in every direction as I formulated my strategy."
    MCT "Oy, I gotta get this cut before tomorrow... huh?"
    "I didn't hear, but saw a disembodied backpack slip inside the slightly-opened balcony door,"
    show RM sad with dissolve
    extend " followed by my grimacing roommate."
    MC "Utagashi-san."
    show RM neutral
    RM "Hotsure-san."
    MC "Lock broke?"
    RM "A situation arose, and I adapted."
    MC "Uh huh. I'll call the maintenance guy after I'm done with this boss."
    show RM angry
    RM "No, don't do that. If you must know, Matsumoto's on patrol right out in front of the dorms, and I'd rather not have her rooting through my notebook. I doubt she'll fall for a decoy twice."
    MC "So is it, like, actually possible to get expelled from here?"
    show RM neutral
    RM "Not for that, no. Now, I've got some things to work on."
    MC "You do that."
    hide RM with dissolve
    "He sat down at his desk and began laying out notes and assorted colors of pens; I, too, sat up and beheld the disarray before me on the TV."
    MCT "Hmm..."
    pause 1
    MCT "I wonder how Naomi-chan's doing..."
    "I took out my phone."
    MCCell "<hey Naomi-chan, how are u doing?>"
    "I laid it down again and returned my attentions to the ongoing battle; it buzzed a couple minutes later."
    GTSCell "<Quite well, Keisuke-kun, thank you. You've just caught me in the midst of some reflection. How are you this lovely day?>"
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
        GTSCell "<I'm afraid I don't follow baseball much.>"
        MCCell "<I didn't think u did>"
        MCCell "<it made me appreciate his achievements tho reading how hard he worked to get there>"
        pause 0.5
        GTSCell "<A wonderful thing, indeed.>"
    if isHighestSkill("Art"):
        $setFlag("GTS040_art")
        MCCell "<well.. it's not really a traditional book>"
        MCCell "<when I was 10 I got this like booklet for making little charms with bottlecaps and glue>"
        MCCell "<i ended up making a ton of them and tomo-chan even pitched in a couple times>"
        MCCell "<it was kinda cheesy but I ended up making lots of crafty projects like that>"
        MCCell "<after I destroyed all the soap in the house trying to carve figurines my dad just bought me a sketch pad lol>"
        MCCell "<srry for the wall of text>"
        pause 0.5
        GTSCell "<Not at all, Keisuke-kun.>"
        GTSCell "<I think it's perfectly lovely that you've been in touch with your creative side for so long.>"
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
    MCT "All this hair isn't so bad sometimes..."
    "I glanced ahead of me to the path to the main building, which I headed down as I resumed typing."
    scene Campus Center with fade
    MCCell "<how about you, what was your favorite book?>"
    "The screen was tantalizingly still for many moments."
    GTSCell "<I will tell you, but I hope you won't find it too terribly common.>"
    MCCell "<nothing about you is common, Naomi-chan. please do share>"
    scene black with fade
    pause 1
    scene School Front with fade
    GTSCell "<It was a romance novel. A period piece, as I'm sure you've guessed.>"
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
    MCT "Okay, she's probably gonna be near the back, let's see..."
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
    MCT "Did I just think the word \"gauche\"? Who am I anymore?"
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
        "Maybe you're turning into an old lady? Like, faster than normal.":
            GTSCell "Even under the circumstances, that seems rather improbable, does it not?"
            MCCell "The evidence seems pretty unassailable. I mean, we know you're majorly into gardening. Have you noticed any white hairs? What's your stance on doilies? Or Nortfight dances?"
            GTSCell "I haven't noticed any such thing, no. I'll be sure to check again after this conversation."
            GTSCell "And I happen to have a good deal of respect for the craftsmanship and visual aesthetic of the doily, though I myself prefer other modes of ornamentation."
            GTSCell "...I confess, before I offer an opinion, I must ask precisely what a \"Nortfight dance\" is."
            MCCell "Eh... honestly I don't think knowing would enhance your life."
            GTSCell "I do find myself inclined to believe you."
            jump GTS040_c3
        "I guess it was just a matter of time. Do you know if they can provide you with a replacement?":
            $setVar("GTS_selfhood", getVar("GTS_selfhood") - 1)
            $setFlag("GTS040_c2_2")
            GTSCell "I believe I have heard that they can. I shall have to see about that soon."
            MCCell "Good, good."
            MCCell "..."
            MCCell "So, can I ask you a weird question?"
            GTSCell "Whatever you please."
            MCCell "Of course there's a lot of downsides to your factor. What are some of the good things? The silver linings?"
            "She was silent for a moment or two."
            GTSCell "That's a rather good question, as a matter of fact. It is important, after all, to be mindful of the narrowness of our perceptions."
            pause 1
            GTSCell "Hmm..."
            "I wiped my wrist across my damp forehead, smiling."
            GTSCell "Well, when my family came to visit and I looked down at Kimiko, it was just like she was a puppy again. That brought back some fond memories, indeed."
            GTSCell "...As discomforting as it is to reflect on, having a new perspective on the world around oneself is edifying, in some ways."
            MCCell "I bet. Ever look up and wonder what's going on in the canopy of the trees?"
            $setAffection("GTS", 1)
            GTSCell "Hmhmhm, so I have."
            GTSCell "I also wonder... what do you think of it?"
            MCCell "Of... your factor?"
            GTSCell "Yes."
            MCCell "I...{w} uh, kinda like it."
            if checkSkill("Academics", ">", 3):
                MCCell "It fits you, in a weird way."
                GTSCell "I'm not sure I take your meaning."
                MCCell "Just all the things that make you someone you can look u... uh... "
                MCCell "Like, I'll say it again, you're one of the nicest, sweetest girls I've ever met. Maybe it's not so bad if, you know, your presence can be felt a little more."
                GTSCell "Thank you. I wouldn't want to forget my virtues for anything."
                GTSCell "I confess it is something that worries me, in my more idle moments. My tai chi lessons are no small help in developing self-control..."
                GTSCell "...But as necessary as these facilities are, it seems impossible to put what I'm learning into practice where it is truly needed."
                if checkSkill("Academics", ">", 6):
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
    "Now, maybe I wasn't the greatest listener."
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
    scene Giant Dorm Interior
    show GTS neutral
    with fade
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
    MCT "Seems like yesterday she was \"only\" twice my height fully standing up..."
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
    $setProgress("GTS", "GTS042")
    play music DayByDay
    "More frequently than ever, I found myself going straight over to the Giants' Dorm after class. I didn't even need a call from Naomi."
    "She didn't mind me coming by; she treasured my company just  as much as I treasured hers."
    "Normally when I came over, we didn't tend to do much. If we did, it was small things, pun intended, like homework, cooking, or just watching a show I could stream from my phone onto her tv."
    "Today however, was a bit different..."
    scene Giant Dorm Interior
    show GTS neutral
    with fade
    GTS "Kei, could you tell me which color you think looks better? The red,"
    show GTS neutral at Transform(xzoom=-1)
    extend " or the blue?"
    "She put each dress in front of her, swapping between the two."
    MC "They're both quite flattering. The blue matches your personality, while the red has a sort of fierceness to it."
    show GTS neutral at Transform(xzoom=1)
    GTS "Fierceness? I don't think I want to project that image. I don't want anyone to think I'm scary."
    MC "Not that kind of fierce, more of the..."
    MCT "I'm gonna expose myself saying this, won't I?"
    GTS "..."
    GTS "Oh, well I'll just keep that in mind, the blue will do just fine then."
    MCT "Smooth is not my middle name apparently."
    "Naomi disappeared into her bedroom and reappeared in the blue dress, which to say was form fitting would be an understatement."
    "The dress was probably a few sizes too small and was hugging every inch of her body that the poor fabric could reach."
    MC "Is that comfortable? Looks a little tight."
    GTS "It's a little tight, but it should be fi..."
    stop music
    show GTS surprised
    "*{i}RIIIIIP{/i}*"
    "In an instant, starting from the bottom of the dress, up her thigh and past her hips, the seams holding the side together gave out. Naomi flailed wildly to grab the two sides to retain some modesty."
    play music Sunset
    show GTS sad
    GTS "If you can excuse me for a moment.... I need to correct my appearance."
    MC "Take your time, I don't mind."
    hide GTS with dissolve
    "With a glum expression she shuffled back into the bedroom. Eventually she reemerged holding the fallen garment."
    show GTS sad with dissolve
    MC "Where did you get that dress? Was it from Alice?"
    GTS "No, there is a small store inside the caverns that has some old clothes that previous students have donated. I was hoping this one was a bit looser, but I may have underestimated how much I've grown in the past weeks."
    MC "Is that the only place for giants to get clothes?"
    show GTS neutral
    GTS "There {i}is{/i} a shopping district that specializes in Giant clothing, but I haven't made the journey to visit it."
    MC "It's not too late. Would you want to go find this place?"
    "She glanced at the blue dress."
    GTS "I {i}would{/i} like to have more than just my set of school uniforms."
    MC "Do you have a map of the area?"
    GTS "We just need to follow the road that stretches northeast  towards the mountains."
    MC "Is there a thing with giants and mountains, or do I need to lay off playing Skyledge?"
    show GTS pondering
    GTS "I'm not sure why it's there, but... that IS a rather ironic coincidence, yes. But pray tell, what is \"Skyledge\"?"
    MC "It's one of the video games I play. I can explain it on the way there if you'd like."
    show GTS happy
    GTS "I would love to hear about it if you would like to."
    MC "Um, one thing before we head off, would you mind... uh... carrying me?"
    show GTS pondering
    GTS "...May I ask why?"
    MC "I've been having a hard time keeping up with your pace. If we're gonna travel far, it may be better for you to carry me."
    show GTS neutral
    GTS "If you wish, I can do that for you."
    "She crouched down and let me step onto her hands."
    "The sensation as she lifted me back up was one I can safely say I've never encountered before. I've taken a plane before so the lifting sensation was similar, but the openness while experiencing this did rattle me."
    show GTS surprised
    "I noticed Naomi make a face of concern seeing my expression of shock. If she wanted to say something, she decided against it."
    MC "Alright, I'm ready to go. So, what would you like to know about Skyledge?"
    show GTS neutral
    GTS "The beginning will do."
    scene black with fade
    pause 1
    stop music fadeout 0.5

    scene Field
    show GTS neutral
    with fade
    MC "...and you're in a cart after being captured because you were crossing the border illegally. Once you're in control, some guy says he's glad you are awake."
    GTS "I wish I could recall all that kind of stuff as well as you can."
    MC "I'll be honest I've just played the game and the others in the series too much."
    GTS "Oh, I think that we are here."
    scene Giants Town
    show GTS neutral
    with fade
    "I had been so caught up in my tale that I hadn't noticed us reach the large gate. A pair of guard towers bracketed the gate."
    MC "You sure this is the place?"
    GTS "Someone had mentioned it was government run, but I'm not entirely sure."
    MC "I wonder how you actually enter."
    "Looking around, I spotted a large metal plate in the ground ahead of the gate."
    MC "You may need to step on that to get in."
    GTS "It seems rather odd to need someone to weigh a certain amount just to get some clothes."
    MC "I guess they suspect that if you're coming here, then you are of a certain type. It's likely put in place to keep non-giants safe."
    "As she gingerly stepped onto the plate, the sound of clicking could be heard. The gate slowly parted to reveal a road leading towards a cluster of buildings."
    MC "A rather curious place so far, a lot of odd security and engineering for a rather secluded place."
    GTS "It {i}is{/i} government run, so that would make sense."
    "Approaching the buildings, we could see more people walking around. While everyone's height varied, I could guess everyone here exceeded 4 meters in height."
    show GTS pondering
    GTS "I'm surprised to see this many giants outside the dorm. I do wonder what the greater purpose of this place is."
    MC "Is there a more formal map of the area?"
    GTS "I don't see one, but maybe we could  head over to that large shop at the end of the road ahead."
    "Looking down the road I noticed the building she was pointing out. It was by far the largest building in the \"small\" town. The sign clearly read \"Mt.Fuji Outfitters\" which was rather fitting for a place located in the mountains of the island."
    MC "That's probably a good spot to head towards, seems popular."
    show GTS neutral
    GTS "I hope they may have some clothing as well, it seems like some sort of general store."
    "As we approached the store, the sheer size of the building was becoming more apparent. The entirety of the school could easily have fit in this place three or four times over, and that was what I could see."
    "The front doors slid open revealing a massive warehouse-like building. Everything from minute trinkets to whole TVs was on display, except these were five to seven times their normal size."
    MC "See any clothes? I can't see a whole lot from here."
    GTS "I don't see any from right here. Perhaps there's someone to talk to about finding them."
    MC "I don't think I'll be much help in that regard. I can barely see past these shelves."
    GTS "I can see a larger gentleman at a counter ahead of us. It's safe to assume he's an employee here right?"
    MC "That's up to you, I can't see to judge that."
    GTS "Oh right, apologies."

    scene Giants Town Store
    show GTS neutral
    with fade
    play music BrightLights
    "Going further into the store from my perspective brought on this feeling of truly entering a foreign world. Items that are so common to me are now taller than my entire body, or even taller than my house."
    "A feeling of alienation I could feel welling in my stomach, though there was another feeling I wasn't sure how to describe in there as well."
    "As we rounded the endcap of an aisle, I found myself looking higher still. Ahead of me was a gentleman that towered even over Naomi. He was quite toned as evident by the muscles outlined by his button down shirt."
    UNKNOWN "Welcome to Mt. Fuji Outfitters. How can I help you, young lady?"
    GTS "Thank you, sir. My boyfriend and I were just looking for some more fitting clothing... for me, obviously. I can get my school uniform replaced, but casual wear is a little tricky."
    UNKNOWN "I understand, that was a problem when I went to Seichou as well. Never really could find a nice casual shirt or jeans."
    UNKNOWN "Come along, and I'll show you our clothing selection. This place can be a maze at times."
    GTS "That would be appreciated. This is our first time here."
    "The gentleman looked over the counter to look down at me, before breaking into a smile and laughing."
    UNKNOWN "Apologies, it's rare that a normal sized person wanders in here. Especially one not associated with the government."
    "Stepping out from behind the counter, he began taking us through the winding pathways of the store."
    MCT "I think I wasn't far off in assuming this place is much bigger then I assumed it was."
    GTS "If I may ask sir, you did say you went to Seichou correct?"
    UNKNOWN "I went there some years ago. I do wonder what the place looks like now."
    GTS "Are you by chance Akio Fumihiro?"
    Akio "I am, indeed. Where'd you get my name from?"
    GTS "You were much taller than everyone at the dorms by a good margin, and I recall seeing a name on the record wall that was above everyone else's."
    Akio "I'm surprised that the record wall is still a tradition. From what I heard, the record wall was established by the class before me and only had about a dozen names or so."
    Akio "When I left and recorded my name on it, there was a certain surprise since I was a head taller than nearly everyone."
    Akio "I take it I'm still the record holder?"
    GTS "Indeed, a few have come close I recall but none have surpassed you."
    Akio "Interesting, surprising that someone hasn't grown past me."
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
    GTS "Fair enough, it is rude to poke too much into another's business."
    Akio "It's fine, though I do need to return to the front counter. I hope you find everything you are looking for."
    "He waved and disappeared behind the shelves."
    MC "He's quite nice. I didn't expect him to also be the record holder."
    show GTS unique
    GTS "That was quite a nice surprise."
    MC "So were you only looking for a dress or were you looking for something else?"
    show GTS neutral
    GTS "A new dress would be good, but I did have some other things in mind. I wonder if they may have a new kimono? The one I used for dinner is getting rather short."
    MC "Possibly. You know, I've never considered if those are common items. I got mine a few years ago, but I can't recall seeing them on a clothing rack at a store."
    GTS "It depends on the store, I would assume. Though you certainly have a point that they're a rather niche item outside of holidays."
    MC "What else were you thinking?"
    GTS "I may not be using the school's primary pool anymore, but I have heard of a spring in the caverns as well as a good beach spot. I wonder if they have bathing suits?"
    MCT "Please be bikinis. Please be bikinis. Please be bikinis."
    MC "I wasn't aware there was a spring in the caverns. At least you haven't mentioned it before."
    GTS "It's a warm spring, but I'd still need a suit. ...Ah, there they are!"
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
    GTS "You flatter me, Kei, but I'm not sure I'm comfortable showing that much skin to anyone else."
    MC "I hate to sound ignorant, but I don't think you have a choice if this is their selection."
    GTS "You're fine, I can see that my preferences aren't possible with this selection."
    GTS "*sigh*"
    show GTS neutral
    jump GTS041_After_C1

label GTS041_A2:
    $setFlag("GTS041_A2")
    MC "You might be able to order a one piece, but get a two piece until then."
    show GTS pondering
    GTS "That may be, he did mention that he orders through the military. He might have a design I could order."
    show GTS neutral
    GTS "I'll grab one of these in case he doesn't. It's not my preference, but I think I may be losing my ability to have a choice on these matters."
    jump GTS041_After_C1

label GTS041_After_C1:
    "She grabbed off the rack a plain white two piece suit, the bottoms had a sort of skirt on them which was quite flattering as I imagined Naomi strutting down the sand in it."
    GTS "This is a nice color. Can't say I've considered a lot of white in my wardrobe outside of my uniform shirt."
    MC "I think it would look great on you."
    GTS "Then I guess it's settled, can't disagree with such an expert assessor."
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
    GTS "Although it may sound bad on my part, I haven't really looked into it. I was hoping that I would stay below the 4 meter threshold, but as we both can see that ship has sailed."
    GTS "I'd love to return to the mainland someday, but I fear I may not be permitted to."
    MC "I assume you mean \"without resistance from the government\"."
    GTS "Correct."
    MC "Yeah, that already brings up a lot of issues. I was surprised to hear how involved they are in the store."
    GTS "It was quite surprising, but considering how prominent they are in the dorms, I shouldn't be."
    MCT "I do wonder how much the government will get involved as she grows taller."
    MCT "{i}Bleck{/i}. I'm starting to sound like Daichi now."
    "I was left to wonder as the sun finally set upon our return to school."
    jump daymenu

label GTS042:
    $setProgress("GTS", "GTS043")
    scene Cafeteria with fade
    play music Schoolday fadein 30.0
    MCT "There's hair in my rice."
    "At the very least, I knew exactly where it came from. I plucked out the stray tress and squeezed my fingers down its length until every stray grain was stripped away."
    "I made quite sure it was tucked into my hairband this time before resuming my lunch."
    pause 1
    MCT "Hm... wonder who those people over there are."
    MCT "Must be from another homeroom..."
    "The rice was a little drier today, not as fluffy; I looked down to see quite a pile of fallen grains."
    show Ryoko neutral with dissolve
    "I was almost relieved to see Ryoko walk up to my corner of the table, planting a hand down across from me."
    Ryoko "Is this seat tagen?"
    MC "Nah, go ahead."
    Ryoko "Thanggus."
    show Ryoko confused
    "As she sat down, she scrunched her brow and her cheeks bulged out one after the other. Then, she swallowed."
    show Ryoko neutral
    Ryoko "Glm... Pardon my enunthhiation. My tonguethhs gotten to a thize where I have to re-learn how to uthe it."
    MC "I know the feel. I thought I'd skip my usual trim just once last night, and now I'm fishing hair out of my lunch."
    MC "Come to think of it, our homeroom teacher, uh, Tashi-sensei, he's got the same factor as you. He'd probably give you some tips for adjusting if you wanted to ask him."
    Ryoko "I'll do that. Directing'th not half ath fun when nobody can underthtand your directionth."
    Ryoko "Which bringsth me to what I wanted to assk you. Are you doing anything after clath today?"
    MC "Well, I definitely gotta get a haircut today. And water Naomi-chan's flowers, especially with how hot it is out."
    show Ryoko confused
    Ryoko "Hang on, {i}you{/i} do that? I thought the school'sth groundsthkeeper handled it."
    MC "I mean, he handles everything else on the grounds, but I take care of the rooftop garden. I told Naomi-chan I would before she moved."
    if checkAffection("GTS", ">", 40):
        MC "Besides, like... I don't want all of her effort to be forgotten. You know?"
    show Ryoko happy
    Ryoko "{i}Now{/i} I get it."
    MC "Get what?"
    pause 0.5
    show Ryoko tongue
    Ryoko "Yamathaki-san speakth {i}pretty{/i} highly of you on the occathion we get to talk, you know."
    show Ryoko neutral
    Ryoko "Anyway, thi-...mm... ssince you know the code to get into the old mine, could you pleasse come with me so I can ask Yamazaki-san to do a voiceover? It'th for a film project."
    if checkSkill("Academics", ">", 3):
        MC "Wait, why can't Tomoe-san handle that for you? Isn't she on the student council?"
        Ryoko "Yep. The trouble is she lookths to have come down with a pretty wicked sstomach bug. She's in no shape to walk all the way over there."
        MC "Oh, really? Well damn, I hope she feels better soon."
        Ryoko "I'll passth that along. Sso, what do you thay? Can you thpare the time?"
    MC "...Yeah, sure! Let's do it!"
    show Ryoko happy
    Ryoko "Ecthellent! She'll knock it outta the parg, I jusst know it."
    MC "No doubt. So, I should have all my stuff done a couple hours after class gets out. Wanna meet me at Chūkan Point around that time?"
    show Ryoko neutral
    Ryoko "Will do. Later, Hotsure-than."
    stop music fadeout 3.0
    scene black with fade
    pause 1

    scene Hallway with fade
    play music Rain fadein 2.0
    "After yawning, doodling, and chickenscratching my way through the last few hours of classes, I donned my backpack..."
    "...And prepared to enter the breach. Seichou's enlarging student populace was starting to give the subways back home a run for their money."
    "I breathed a quiet, thankful sigh as the crowds shortly thinned, and made a beeline for the supply shed."
    scene black with fade
    pause 0.5
    scene Roof with fade
    "But it was there, on the roof, where I really felt at peace."
    "I wasn't alone, of course, but I couldn't feel alone even if I were. Immediately, my eyes fell on the verbena patch; like sapphire waters they shimmered and swayed in the high breeze."
    "Alongside them danced the lilies, the tulips, the peonies, together contributing their personal hues to the great, unassuming show."
    "I couldn't help but look around, smiling at nothing, as I tilted the watering can downward. So many memories fluttered around the pattering flower bed... sharing thoughts with her, sharing hopes, sharing sorrow and joy."
    "With every recollection, my eyes kept coming back to the flowers."
    MC "Haaaah..."
    MC "Ksh..."
    MCT "What kinda guy just stares at flowers?"
    "I shook the last drops out of the can, and started to head back to my dorm. I had a date to keep, and quite a mess to clean up before I'd look presentable."
    scene black with fade
    pause 1.0
    scene Chukan Point
    show Ryoko neutral
    with fade
    "Ryoko was already there sitting on a bench, striking lines across a notepad atop a stack of papers on her lap; every couple moments a few centimeters of her tongue would peek out the side of her lips."
    Ryoko "Ah, great, you're here."
    "With a few snapping hand motions, she gathered up her things, and stood."
    Ryoko "Hm... collar length? Wouldn't you give yoursself a little more time if you cut it a bit shorter?"
    MC "Huh? I did cu..."
    "I reflexively patted the back of my neck to discover that my hair had sprouted back a couple centimeters during the walk over. I patted once or twice more just to assure myself it was real."
    MC "Ugh... I'm gonna just pretend I cut it wrong or something."
    Ryoko "I'd be a little ssurprised if you actually {i}could{/i} give yourself a decent cut. Did you ever do it before you came here?"
    "She waved me along as she started walking down the path, shortly followed by myself."
    MC "Uh... don't think so, actually. If we somehow couldn't find a single barber in Shibuya, my mom did a pretty good job."
    "She looked ahead and nodded appreciatively as we stepped out of the park gates."
    scene black with fade
    pause 0.5
    scene Field
    show Ryoko surprised
    with fade
    Ryoko "Y'know, I feel bad for not finding the time to visit Yamazaki-th... glm... san."
    show Ryoko neutral
    extend " When I was first getting used to being in charge of the film club, nothing helped me unwind like a cup of tea in her dorm."
    MC "Well, she'll be happy to see you. I'm sure she'll pour you a cup."
    show Ryoko confused
    Ryoko "Can she? Does she even have..."
    show Ryoko embarrassed
    Ryoko "What am I saying, of course she does."
    MC "Heh, yeah. Taller or no, she's still Naomi Yamazaki."
    show Ryoko neutral
    MC "By the way, what's that script you want her to read about?"
    Ryoko "Ever watched Il Lago and or Ognum Pond?"
    if checkSkill("Art", ">", 6):
        MC "I think I {i}heard{/i} of them... one's a romance, and the other's a weird horror movie, right?"
        MC "I don't think she'd care much for the latter..."
    else:
        MC "Sorry, I don't speak Italian."
        Ryoko "The former is a romance about two people who live by a lake in different time periods, the latter's about a girl's ghost haunting her family after disappearing."
        MC "So... a horror flick? I don't think she particularly likes those..."
    Ryoko "That's not what I'm going for though, it's more of a character study. Like..."
    Ryoko "Well here, you can read it yourself. Yamazaki-san's part is right at the beginning."
    "She stopped to hold it out with both hands, which I accepted in kind."
    "And there it was, highlighted in neon green; I began to read."
    pause 1
    MC "Huh..."
    MC "This is... {w}actually perfect for her."
    Ryoko "Thanks. I like to think I apply my actresseth' talents well."
    "I nodded and passed the script back to her, much reassured as the pale metal gates grew higher on the horizon."
    scene black with fade
    pause 0.5
    scene Giant Dorm Exterior
    show Ryoko happy at Position(xpos=0.8, xanchor=1.0, yalign=1.0)
    with fade
    "Ryoko stared down into the open pit as we skirted it, and whistled."
    Ryoko "Would you look at that drop! What I wouldn't give to work in a dolly shot of that ssomeday."
    MC "You've never been here, I take it?"
    Ryoko "Nah. I've been {i}meaning{/i} to."
    MC "Well, thank you for choosing Hotsure Lines to be your guide. We roll out the brown carpet for you every time."
    show Ryoko tongue
    "I flipped my hair; Ryoko smirked."
    Ryoko "Depending on availability."
    MC "Oh, don't worry. It's coming."
    MC "Ah, here's her dorm."
    show Ryoko confused
    Ryoko "...Wow. {w}Spacious."
    MC "Very."
    show Ryoko neutral
    "Lest we delay further, I raised my hand and rapped on the door."
    play sound Knock
    pause 0.5
    GTS "Coming!"
    "Even after a few weeks of coming to visit Naomi, it messed with my brain to know she was several meters away, but still register her voice as though she were just behind the door. It was just something special about her, I suppose."
    show GTS happy at Transform(xzoom=-1), Position(xpos=0.45, xanchor=1.0, yalign=1.0) with dissolve
    "She opened up the door, already smiling warmly down at us, but she nearly gasped to see Ryoko there too."
    GTS "Oh, Tanaka-san! How lovely to see you again, it's been far too long."
    Ryoko "Hasn't it just? How are you doing, Yamazaki-san?"
    GTS "Quite well, thank you. Would you like to come in? I would love to offer you some refreshments."
    show Ryoko happy
    Ryoko "Yesth please!"
    show GTS neutral at Transform(xzoom=-1)
    "She bowed deeply, draping her hair just over our heads, and stepped out of the way."
    scene Giant Dorm Interior
    show Ryoko neutral at Position(xpos=0.7, xanchor=1.0, yalign=1.0)
    show GTS neutral at Position(xpos=0.45, xanchor=1.0, yalign=1.0), Transform(xzoom=-1)
    with fade
    GTS "Allow me to put on the kettle. To what do I owe this delightful visit?"
    MC "We wanted to ask for your help with something, but we can sit down for a while."
    Ryoko "Yeah, let's catch up a little. Can I just sit down on the couch?"
    GTS "By all means."
    hide GTS with dissolve
    "Naomi walked away to gather the essentials in the kitchenette, while Ryoko took a look beside her at the oversized couch, her face starting to unwind as reality washed over her."
    Ryoko "Wow, this place really is a study. You just have to hoist yourself up there?"
    MC "Basically. You need any help?"
    Ryoko "I oughta be fine, thanks. My morning jogs are about to come in handy."
    "I nodded and started toward the couch myself; indeed, on a first try she managed to claw her way up and crawl to a seated position."
    show GTS neutral at Position(xpos=0.45, xanchor=1.0, yalign=1.0), Transform(xzoom=-1) with dissolve
    GTS "Ah, pray pardon the inconvenience. I do need to find a way to better accommodate guests."
    Ryoko "You're good, Yamazaki-san, you're good. How are you liking the new room?"
    GTS "The room itself is... liveable, at least. My hope is that my renovations will make it more than that. I have missed you and Tomoe-san especially, and I should think the mere remoteness of these facilities is partly to blame."
    show GTS pondering
    GTS "By the way, is Tomoe-san in good health? It strikes me that she isn't with you."
    Ryoko "Afraid not, but it's nothing serious, just a sstomach bug. She just needs to stay in bed for a day."
    show GTS neutral
    GTS "I'm sorry to hear that. The next time you see her, please offer my well-wishes."
    Ryoko "Sure thing. So the room could be better, you think?"
    GTS "Well, I must confess there have been unqualified benefits. My prior dormitory and its amenities were beginning to feel singularly cramped just before I relocated."
    GTS "Now, by contrast, nearly everything feels perfectly suited to me, down to the finest detail. In fact, some things still feel a bit... grand, as it were."
    show GTS unique
    GTS "I'm certain you relate."
    MC "Yeah, \"grand\" is perhaps an understatement."
    show GTS neutral
    "Naomi slowly rocked her body backward, returning to a relaxed position. Due to the size and strength of the room's furniture, nothing creaked under weight. It still felt like a major event every time she moved."
    GTS "Well, that's quite enough about me, I'm sure. What can I do for you today?"
    Ryoko "Well, I... "
    show Ryoko annoyed
    extend " oh brother, it got crumpled."
    "Ryoko straightened out the stack of papers with a few sharp, snapping yanks with her fingers, and then held it up."
    show Ryoko neutral
    Ryoko "I've got a short little film script here, and I was wondering if you wouldn't mind me recording you reading it aloud."
    show GTS surprised
    GTS "Recording me? Does that mean you intend to use the recording in your film?"
    show Ryoko happy
    Ryoko "Exactly! Would that be okay?"
    GTS "Well, I certainly do not object out of hand, but surely it wouldn't be right for me to deprive more talented actresses of the opportunity."
    show Ryoko neutral
    Ryoko "Don't worry about that! They've got plenty to do either way. You're actually my first choice, after all."
    GTS "Am I?"
    Ryoko "Yeah. Your voice has this soft yet resonant quality that I think would fit the lines flawlessly."
    MC "But don't feel bad if you don't want to do it, Naomi-chan. It's completely okay."
    show GTS neutral
    "She nodded to me, warm recognition in her eyes."
    Ryoko "Yep! If you don't, like you said there are others."
    GTS "Well... I would like to aid in your artistic endeavors so much as I am able. I accept."
    show Ryoko happy
    Ryoko "Excellent! Thanks a ton, Yamazaki-san."
    show Ryoko neutral
    Ryoko "I'll just plug in my microphone and recording device and we can get started."
    pause 1
    Ryoko "There's not a normal-sized outlet in here, is there?"
    GTS "I believe I saw one right next to the electric range."
    Ryoko "Ah, there it is. Thanks."
    MC "But how are we gonna get it all the way over here?..."
    "By the time I finished asking, Ryoko had pulled a mildly intimidating amount of extension cables from her backpack."
    MCT "Holy fire hazard..."
    hide Ryoko with dissolve
    "She rolled the cables over her arm, in a beeline towards the outlet, and a mousey, gravelly {i}pop{/i} from the microphone told of the success of her expedition."
    show Ryoko neutral at Position(xpos=0.7, xanchor=1.0, yalign=1.0) with dissolve
    Ryoko "{i}Hup{/i}... okay, should be good to go."
    "I bobbed up and down to the tune of Naomi gently shimmying herself directly in front of the microphone, meanwhile feeling nothing as Ryoko rolled back up onto the couch."
    MCT "God, even her tiniest movements are so powerful... it's addicting to watch..."
    MCT "Nope, nope, gotta focus..."
    Ryoko "So, I imagine you'll want to read through it before we actually start."
    GTS "That would be sensible. Yes, please."
    "Ryoko passed the script over, which Naomi took with a shallow bow using both hands... or she tried to, before opting to pinch it between her pointers and thumbs."
    show GTS surprised
    "Without another word, Naomi began reading with appreciative rumination; her eyebrows inched upward throughout, at which I couldn't help a self-satisfied smile bubbling up on my face."
    show GTS neutral
    "She came to a slow stop, with a thin smile of her own."
    GTS "My, my, this is {i}superb{/i}. Very good then, let us commence."
    show Ryoko happy
    Ryoko "Fantastic! Just sort of face the mic and tell me when you're ready."
    "She put her fist up in front of her mouth and, as quietly as she could, cleared her throat, and finally hummed a few different notes to herself."
    GTS "I am ready."
    show Ryoko neutral
    "Ryoko simply nodded, produced a tiny black remote, and pressed on it."
    stop music fadeout 3.0
    "I sat rapt to hear Naomi's voice bring life to the words I'd read."
    pause 1
    GTS "The winter isn't quite as cold anymore."
    GTS "I've learned to see the snow's perennial brightness, and when the frigid winds begin to seize my throat I look out onto our frozen reflection pool, and I am relieved utterly."
    GTS "And so I have hope that there's time left to learn the other things you meant to teach me."
    pause 0.5
    GTS "At times I find myself grieving how ill I carried on our family name; redemption rests now in the hands of my sons, scattered as they are now on the more auspicious winds."
    GTS "But I know you wouldn't want me to grieve overlong, my Yukiko, and so I shall not."
    GTS "That, I shall always remember, as the ice grows mottled and my shoulders grow wet with droplets. Even as stiffness binds more stubbornly to my bones with every winter passed... I shall carry your hope."
    show GTS embarrassed with dissolve
    pause 0.5
    GTS "If I should not return to meet you by the pond, please know that when my last breath should escape through my bedroom window, it will whisper your name."
    pause 0.5
    GTS "My dear Yukiko, I will remember your face always."
    pause 1
    Ryoko "Cut."
    show Ryoko happy
    Ryoko "That was {i}amazing{/i}! You might've just gotten a perfect take on the first tr-"
    MC "Naomi-chan, are you... alright?"
    show GTS surprised
    show Ryoko surprised
    "Naomi looked down at me with a start, but it wasn't enough to hide the shimmer I thought I saw growing at the edge of her eye, now trailing down her cheek."
    "A deft swipe of her finger confirmed my suspicions."
    play music Peaceful
    show GTS unique
    GTS "Mm... ah, pardon my ill composure. It seems my constitution was, erm, not quite equal to the prose."
    MC "...Heh. You really did amazing, you know."
    show Ryoko neutral
    Ryoko "No question. Are you happy with it, Yamazaki-san?"
    show GTS neutral
    GTS "Well... I hardly have any expertise by which to judge. If you two are pleased with my rendition, then I must be as well."
    "Just then, a shaky whistling grew louder on the other side of the room."
    show GTS happy
    "Naomi's face brightened as she stood."
    GTS "Ah, the water's ready! One moment, please, while I pour our cups."
    show GTS neutral
    "She made good on her word with the grace of pouring water and rising steam, and grassy scents floating before one's face."
    show Ryoko happy
    "A few moments more, and she set before us a tray of two steaming, mottled brown goki chawans... right next to her plain black chawan the size of a mixing bowl."
    MC "Smells delicious. Thanks, Naomi-chan!"
    Ryoko "Ditto!"
    show GTS happy
    GTS "The pleasure is all mine."
    show Ryoko neutral
    "She eased herself down beside us, hands on her knees, and we all took a sip before commencing to some light, easy conversation."
    "I soon found there was more to catch up on than I expected, Naomi sharing the goings-on around the mine and Ryoko gushing about the film club's projects and inner workings."
    "And in the middle... was something that wasn't there before. Naomi was ever the attentive listener, but never did she hang onto every word with such beaming glee when she used to have these little chats in her room."
    "Several times, the conversation came back to me, and each time I had to pull my mind away from the enchantment of Naomi's sunny smile. Each time, I couldn't imagine what I wouldn't do to keep that free, unguarded smile just a little longer."
    pause 0.5
    "Maybe an hour passed just talking through the days, and in time the talk dried up alongside the tea."
    "Ryoko drained her dregs and set her bowl down."
    Ryoko "Well, I think I should get going, start working on my paper. Thanks a ton for having us, Yamazaki-san. Hanging out with you's always a treat."
    GTS "Of course, Tanaka-san. Your company is welcome here whenever you please. Take care, now, and be safe on your way back."
    show Ryoko happy
    Ryoko "Heh, thanks."
    hide Ryoko with dissolve
    "One more time she dropped down off the couch, gathered her things, and after turning back to wave me goodbye, headed out the door."
    show GTS neutral at altMove(1.5, 0.65)
    "And so, it was just me and her."
    GTS "I'm glad you're staying with me a little longer. And... thank you very much for arranging that little meeting."
    MC "I admit it was actually Tanaka-san's idea. I was a bit busy tending the garden and, oh... getting things ready."
    show GTS wink at Transform(xzoom=1)
    GTS "Really, now? Well, I should very much like to see the fruits of your labor when the time is right."
    MC "{i}That{/i} can be arranged."
    show GTS neutral
    GTS "Hmhmhm... well now, how has your day been thus far?"
    pause 0.5
    show GTS embarrassed
    GTS "Ah... you already told me."
    MC "Heheh... a little better since you last asked me."
    show GTS unique
    "She grinned, began to giggle, and soon the air between us bubbled with irresistible laughter."
    show GTS aroused
    "As it drew to a close, she eased herself down until she was lying on her side behind me. With her chin resting on her chair-sized hand and a modest blush on her cheeks, she looked just slightly down at me, with lax, dreamy eyes."
    "As luck would have it, her plush lips were still just close enough for me to reach... and so I did, raising a hand to stroke her velvety, maidenly jawline, and plunged into her lips with a kiss."
    "She returned the gesture in kind, pulling me close for moment after sweet moment, until at last we parted; she sighed with her eyes closed, anointing my chest in her minty breath."
    GTS "It's ever so lovely that even now my friends can find the time to visit me."
    "I didn't say anything as I stared into her eyes... fixing once or twice, just for a moment, on the now-invisible trail beneath them."
    "But I knew by then, that's just who she was."
    MC "You know I'll always find the time. I love you, Naomi-chan."
    show GTS unique
    GTS "I love you, too."
    show GTS neutral
    GTS "I thought of that as I was reading, as well. I hope our bond shall endure every last winter we see."
    MC "I feel the same way."
    pause 1
    MC "I... should probably go back and take care of my homework. {w}I'll call you tonight."
    GTS "Very good. I hope your studies are fruitful."
    show GTS embarrassed at Transform(xzoom=-1)
    pause 1
    show GTS aroused at Transform(xzoom=1)
    GTS "Might I have a hug before you go?"
    MC "Of course."
    "I lifted my arms and waved my hands inward."
    MC "C'mon, bring it in!"
    show GTS happy with vpunch
    "She brought it all the way in, snatching me up two meters off the ground, nuzzled against her neck in a warm, blanketing embrace. Happy little hums vibrated against my side as she rocked me, gently, to and fro."
    "Her grip was strong, but ever in moderation. Just enough to keep me pinned to her torso without causing any pain."
    "Once she was done savoring it, she knelt down off the couch and set me down."
    GTS "Be well, Keisuke-kun."
    "I nodded."
    MC "Likewise."
    scene black with fade
    pause 0.5
    scene Giant Dorm Exterior with fade
    MCT "Ahhh... that felt good."
    "I dug out my phone and glanced at the lock screen..."
    MC "Ngh..."
    "...Then angled it away from the glare."
    MCT "The fourth... still got a week. But might as well make hay while the sun shines."
    "Next, I dug out my pen and notepad."
    MCT "Time to pay a visit to Kodama-san."
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
    MC "She's definitely more into cardio and balance training, but I did see her decimate the \"Test Your Strength\" machine at the carnival..."
    show FMG flex
    FMG "Damn! I wish I coulda been there to witness it."
    MC "The attendant looked so confused. It was incredible."
    "I set my bag on the floor and pulled out my phone, sending a message to Naomi telling her where I was."
    MCCell "Mizutani-san wants to know if you'd like to get some practice in before Tai Chi class. Would you like to meet me behind the courtyard a little early?"
    "With the message sent, I placed my phone back into my bag."
    MC "I let Naomi know where we'll be. Are you ready?"
    show FMG happy
    FMG "You know me, Kei-kun! I'm always ready."

    scene School Exterior
    show FMG neutral
    with fade
    play music HigherEdu
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
    GTS "That actually reminds me of the \"energy distribution\" lesson from when I did other martial arts as a kid. The tiger was meant to symbolize fierce, powerful energy, whereas the crane represented gentle, balanced energy."
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
    GTS "\"Powerhouse\" is already a term by itself though, isn't it?"
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
    show cg GTS043_planks1 with vpunch
    "When her arm made a complete circle and sailed downward, her giant right hand cleaved through the stack of ten wooden squares like it was made of tissue paper."
    "The stack folded and buckled like an accordion, stray pieces of wood falling to the ground in sequence mere seconds later."
    "{i}CRACKLE!{/i}"
    "The shockwave from Naomi's arms was enough to send the sides of the board stand tumbling over, leaving everything in a pile of dust. While the stand itself remained intact, the impact of the stand falling over kicked up a massive cloud of sand from the field."
    "The stray bits of yellow dust clouded up near the earth, then faded as the cloud of sand disappeared."
    hide cg with dissolve
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
    if checkSkill("Academics", ">", 7):
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
    if checkSkill("Academics", ">", 7):
        extend " I tried to resume a little of my study for a moment while I awaited a response."
    GTSCell "Pardon me, Keisuke-kun. I should have said something earlier."
    GTSCell "During class I couldn't help but notice you were tugging on your hair a bit."
    menu:
        "Oh yeah, honestly I've been stressing a bit over this upcoming test.":
            jump GTS044_c2_1
        "Oh yeah, I've kinda developed a tic since my hair started getting longer." if checkSkill("Art", ">", 3):
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
    scene Giant Dorm Interior
    show GTS neutral at Position(xpos=0.2, xanchor=1.0, yanchor=1.0)
    with fade
    "Naomi, after letting me in, stepped aside to gather some things from a middle shelf that I could probably touch standing tiptoe."
    GTS "It's good to see you again, Keisuke-chan, even if I might prefer more auspicious circumstances."
    MC "It could be worse, there could be two tests."
    GTS "Hmhm... there could be indeed."
    show GTS unique-2 at Transform(xzoom=-1) with dissolve:
        ease 2.0 xpos 0.7
    show GTS neutral with dissolve
    GTS "There we are. How far did you get on your own, exactly?"
    if checkSkill("Academics", ">", 7):
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
    "But the misty periwinkle sheen of the grass we sat on was all thanks to the moon above. \"Super\" was right; it was bigger and brighter and a purer white than ever I'd seen, its divine glow casting the night into its own kind of day."
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
    $setVar("GTS_selfhood", getVar("GTS_selfhood") - 1)
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
    if checkAffection("GTS", ">", 70):
        MCT "Meh. None of my concern."
    else:
        MCT "Man, it's pretty out tonight..."
    $setAffection("GTS", 2)
    #pending approval, this choice gives weight towards the Nun ending
    "I continued to sit there, listening to the air blow in circles inside me. That is, until I heard a rustle in the grass at my side."
    scene Mountains
    show GTS neutral
    with fade
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
    if checkSkill("Academics", ">", 4) or checkSkill("Art", ">", 7):
        extend " hold up."
        "I leaned in, studying Naomi's brushstrokes slower and closer."
        $setVar("GTS_selfhood", getVar("GTS_selfhood") + 1)
        MC "\"Harvest moon: around the pond I wander, and\"... That's from Matsuo-sama, isn't it?"
        show GTS unique
        GTS "Quite astute. Yes, yes it is."
        MC "You worked this into a painting? D- wow, Naomi-chan, I know you've got an eye for calligraphy, but this is another level."
        GTS "Oh, it's nothing so exceptional. I couldn't have made it without such splendid inspiration."
        MC "Respectfully, Naomi-chan, hell no. {i}This{/i} takes vision."
        show GTS unique at Transform(xzoom=-1)
        "She shifted in place, then smiled with piercing warmth at me as she cocked her head just so."
        GTS "Thank you, Keisuke-chan. I'm very glad you like it."
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
    if checkSkill("Academics", ">", 7):
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
    if checkSkill("Academics", ">", 7):
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
    if not checkSkill("Academics", ">=", 4):
        MC "...Who?"
        RM "Brontë was a British romance and drama novelist and poet. Lovecraft was an American horror writer. Who specialized in reclusive families being depraved in their mansions in the woods."
    MC "Okay, yeah, they're a little stuffy, maybe it's a little weird the way they dress in public, but I highly doubt they're in some kind of death cult or whatever you're saying."
    RM "Probably not. But obviously there's a difference in culture with them."
    RM "Just keep an eye out. My money says Yamazaki-san's got a lot of stuff bottled up."
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
    if checkAffection("GTS", ">", 70) and checkSkill("Academics", ">", 4):
        MC "...Sometimes I think she has issues with self-worth. Like she can't live up to what's expected of her."
        RM "Uh huh... I could see that, a woman of \"breeding\" like her. She probably holds herself to pretty high standards."
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
        "After spending a moment or two futilely trying to process that, I turned back around and he sat down at his own clandestine desk. \"One more read-through and you'll be fine\", I told myself as I lifted up my pencil one more time."
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
        "I turned back around and he sat down at his own clandestine desk. \"One more read-through and you'll be fine\", I told myself as I lifted up my pencil one more time."
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
    "And with breath again in my lungs, I stood."
    scene Dorm Exterior with fade
    "The air was alive in a soothing dance across my face as I stepped beyond the shadowed glass. Like lightning bugs, a dozen lamps still glowed behind glassy veils, just about to wink out."
    "I leaned on the railing as I looked up at the sky, a sparkling ebon jewel, and into its great, misty white eye, a sun for the lonesome."
    "It stared back down at me, kindly. In the quiet of the night, my mind began to wander."
    scene white with fade
    pause 0.5
    #For the following segment, a different character called "Keisuke" should be defined in the code which is the same as the normal MC except for not showing a side portrait
    Mom "Do you know why the moon is white, Keisuke-kun?"
    AltMC "It's made of cheese."
    Mom "Close. It's covered in mochi."
    AltMC "Ohhhhh. That must be a lot, how'd it get on the moon?"
    Mom "Well, a long time ago, a god who lived on the moon decided to take a walk through the forest, disguised as a beggar."
    AltMC "What's a beggar?"
    Mom "A beggar is someone who doesn't have a house, or money, or sometimes even food. So when the little critters in the forest saw him, they decided to all pitch in to make dinner for him."
    Mom "The fox brought fish he just caught from the stream; the monkey brought fruit picked from his favorite trees."
    Mom "But all the rabbit had was grass. So, he brought his greenest, tallest grass to the moon god and told him to make a little fire with it. Once the fire was nice and hot, the rabbit threw himself into it."
    AltMC "What!? No!"
    Mom "Don't worry, Keisuke-kun, the rabbit was fine. The second the moon god saw what the rabbit had done, he plucked him out of the fire and revealed his true self. He thanked all the other forest critters for the meal, and then, as a special thanks to the rabbit..."
    Mom "The moon god carried the kind, brave little rabbit back to the moon with him, where he could pound mochi all day and eat it all night."
    Mom "That rabbit's still up there pounding mochi to this day, you know."
    AltMC "...Woah."
    Mom "Well, the moon god doesn't walk around here much anymore..."
    Mom "But I want you to remember that even today, very good things can happen to you when you be kind to others... even if you lose something at first."
    AltMC "O-okay. I'll remember."
    Mom "That's good! Now, do you want some tsukimi dango?"
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
    show RM neutral with dissolve
    RM "For?"
    MC "I can't get a good picture of the moon. I wanna try to magnify it."
    pause 1
    if checkAffection("RM", ">", 1):
        show RM happy
    RM "Sure."
    "He slid open his desk drawer and from it passed me a compact pair of binoculars."
    MC "Thanks, man."
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
    if checkSkill("Art", ">", 7):
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
    GTS "Don't you believe that your unadorned self is memorable enough for me?"
    MC "Um... uh..."
    GTS "Please, why don't you send me a nice smile?"
    MC "Uh...{w} yeah! Yeah, sure."
    GTS "Thank you dearly."
    "Not quite processing what just happened, I smiled for her earnestly, snapped the picture and sent it."
    jump GTS044_c5b_2

label GTS044_c5b_2:
    MC "Okay, I sent it."
    if not getFlag("GTS044_seductive"):
        $setAffection("GTS", 1)
    "She sighed over the wind."
    GTS "It's like you're really here."
    MC "I could've gone over to visit you."
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
    $setProgress("GTS", "GTS046")
    scene Dorm Hallway with fade
    play music Peaceful
    "I listened to the ringing of clashing blades and cries of dying men from the other side of the door."
    "And once it quieted down for a moment, I knocked."
    play sound Knock
    pause 0.5
    Tomoko "One sec."
    MC "It's me."
    Tomoko "Oh. Door's open then."
    "Thus invited, I ventured into my little sister's lair."
    scene Dorm Tomoko
    show Tomoko neutral
    with fade
    "With the TV's many-hued glow blanketing the front of her, her mass of tangled black hair looked more like a shadow cascading behind her."
    "With a thrust of her chin she chomped a dangling pocky stick back into her mouth."
    Tomoko "Hey big brother. What's going on?"
    MC "Oh, just checking to see how you're doing."
    Tomoko "Pretty good. As you can see I just took Luoyang. Might burn and pillage it later, idk."
    "I flipped on the light, at which she winced, before closing the door."
    MC "Mhm. Speaking of which, are you making good progress on that history assignment? You need any help?"
    Tomoko "'Mgood."
    MC "Aight. How's things with Utagashi-san?"
    Tomoko "We get along. When she starts rambling she usually doesn't care if I tune her out."
    "This again; I rolled my eyes and sighed."
    MC "You remember what Dad said before we left? You'd probably like having real life friends if you gave them a chance."
    Tomoko "I know, but she ain't it chief. Nobody's got time to listen to all that crap."
    MC "Bruh, you go to bed at two in the morning."
    Tomoko "Yeah. Still. You'd think her hotdog lips would've slowed her down just a little."
    MC "Well, nobody said it had to be her."
    "I walked up to the bed and brushed aside some of her hair; meanwhile she scooched away a few centimeters."
    MC "And... how are you dealing with this mop?"
    "She silently milled her jaw, staring at the pause menu."
    Tomoko "Washing it kinda sucks."
    MC "Yep."
    Tomoko "Yep. Other than that I guess it's not too bad. I'll just tie it up or something once it starts dragging the floor."
    MC "Yeah... looking at you, that might be sooner rather than later. And I thought {i}mine{/i} was a pain in the ass."
    "She gave no response except to breathe in deep... and blow a raspberry. I chuckled, and then we sat in silence for a moment or two."
    Tomoko "So how are you doing?"
    MC "Pretty good. I've been putting the finishing touches on a birthday date with Naomi-chan."
    Tomoko "That's coming up?"
    MC "Yeah, tomorrow."
    show Tomoko annoyed
    Tomoko "Ugh, does that mean I have to-"
    MC "Nah, nah, I told her about you. She won't expect a card or a present or anything."
    show Tomoko neutral
    MC "Probably be prepared to meet her in the near future, though."
    Tomoko "Kay."
    Tomoko "So what are you guys doing anyway? Can she still fit in a restaurant?"
    MC "Uhhh... {w}not... {w}really."
    MC "Nah, I was just gonna have a little picnic with her."
    MC "Picked out this spot by a patch of wild lupins, got some cooking tips from Kodama-san, got her a nice present..."
    MC "Heh, I think she'll like it."
    Tomoko "Wow. Sounds like it's getting pretty serious."
    MC "Yeah, we're getting pretty close. She really is a one-of-a-kind girl."
    Tomoko "Uh huh. And you're sure about that?"
    Tomoko "You thought the last chick was pretty special too."
    stop music
    pause 1
    MC "Yeah, I did."
    MC "But I've known Naomi-chan about as long by now, and they're completely different. I've been keeping my eyes open, you know."
    MC "I'm not going to let it happen again."
    Tomoko "Alright. Just don't take any shit."
    MC "I know."
    pause 1
    show Tomoko happy
    $setAffection("TM", 1)
    "I leaned in, then, to squeeze her far arm in a side hug which she half-returned."
    MC "I better head back. Good to hear you're doing okay, Tomo-chan. And if you ever need something, you shoot me a text, okay?"
    show Tomoko distracted
    Tomoko "Got it."
    pause 0.5
    MC "Aight, well, later."
    Tomoko "Later."
    stop music fadeout 5.0
    scene black with fade
    pause 1
    $setTime(TimeEnum.EVE)

    scene Dorm Interior with fade
    "After returning to my dorm, I settled in for the evening with a bundle of red and white mizuhiki."
    MC "I swear, if you split on me one more damn time..."
    "A particularly unfriendly bundle of mizuhiki."
    "I replayed the video for... I dunno, the eighth time, and finally I conceded to slow down the playback speed a little."
    MC "Wait, are they... {w}{i}ohhhhh{/i}, I get it..."
    "With some trepidation, I reshaped the delicate caress of my fingers around the bands, and massaged the tiny cords into what eventually coalesced into, dare I say, a passably piebald butterfly knot."
    "I nodded at my handiwork with a thin smile of satisfaction, and gently pulled the knot apart to repeat the cycle a few times more."
    "With a tenth try the knot was looking clean and symmetrical, and I was content to lay it down."
    "One last parting measurement, just to be sure the material would fully encircle the necessary circumference; and I turned to the less pleasurable labor of the day's assignments."
    "But I couldn't be too chagrined. I had the next day off classes, and I aimed to make the absolute most of it."
    scene black with fade
    pause 2
    $setTime(TimeEnum.DAY)
    MC "Hmmmmmm..."
    pause 2
    MC "Haaaahhhh..."
    "I'd woken up a few hours ago. Small talk with Daichi was unusually pleasant; breakfast was, too."
    "So now, I was waiting, even if I wasn't supposed to be. Eyes closed, counting my breaths. The longer I went, the more similar the soft rush in my chest sounded to the faint cries of the cicadas outside the window."
    MC "Hmmmmmm..."
    "And that's when I noticed just the faintest vibrations in the floor."
    "Little by little, they grew just barely louder and stronger... only to calm down again until I could barely sense them... and then they were silent."
    "In their place, the ambient light over my eyelids darkened just a bit; perhaps some clouds had rolled in."
    scene Dorm Interior with fade
    "Nevertheless, I opened my eyes, stood, donned my backpack, and walked out onto the balcony."
    scene Dorm Exterior
    show GTS neutral
    with fade
    play music Sunset
    "Waiting for me just off the edge of the balcony... was Naomi's head."
    "Her chin was level with the floor I was standing on, and the top of her head with the top of the railing. And her face, her peach blossom face, simply smiled up at me."
    GTS "Good morning, Keisuke-kun. I hope you slept well."
    MC "I did. You?"
    GTS "Splendidly."
    show GTS unique
    "She broke eye contact momentarily as she puffed out a curt, breezy laugh."
    GTS "It feels like an eon since I last looked up at you. Heavens, I never imagined I would miss it so!"
    "I leaned on the railing with a grin."
    MC "Well, I know you're easy on the eyes no matter what angle I look at you from."
    show GTS aroused
    "Her lips parted only a second before she pinched them closed, looking to and fro along the ground as a blush began to blossom on her ivory cheeks."
    GTS "Really now..."
    pause 0.5
    MC "Oh! Eheh, where are my manners? Happy birthday, Naomi-chan!"
    show GTS happy
    GTS "Why, thank you! It's been a perfectly pleasant morning thus far."
    MC "Nice, nice. Well, do you wanna check out the gardens? I know it's been a while for you."
    show GTS neutral
    GTS "I'd love to. Just hold out your arms, please."
    "I obeyed, and her head rose another half meter before her hands rose up over the railing to catch either side of my ribs."
    "She tightened her grip, just enough to hold me fast without squeezing, and lifted me up off the balcony and down onto her warm, cushioned breast."
    "Increasingly, I felt more comfortable lying back in the crook of her elbow, my head back on her shoulder; her gait was as smooth, steady, and graceful as ever, even if she still held me with both arms every time."
    "It might've gotten {i}too{/i} hot in her embrace, but the late summer air was as even-tempered as she was, and her movement produced just the right amount of wind."
    "And yet, if I closed my eyes I could hardly tell we were moving... apart from the rhythm of her side tresses brushing against mine."
    scene black with fade
    pause 1

    scene Campus Center
    show GTS neutral
    with fade
    MC "Tai chi's really paying off, huh? You seem to be doing pretty well with moving around in a, uh... non-giant environment."
    GTS "Indeed, it's a tremendous relief. I'll have to thank my instructor properly later."
    MC "Heh, yeah. I'm proud of you, overcoming such a big change."
    GTS "Oh, I should think little credit at all is due me, when you've so tirelessly supportive."
    MC "Oh, who are you fooling?"
    "I gave her shoulder a light smack, at which she looked down at me with an amused smirk."
    scene School Planter
    show GTS neutral
    with fade
    "We at last arrived at the edge of the enclosure of the campus garden; Naomi got down and sat back on her knees before setting me on my feet with the slowness and care one would show a baby... I guess the scale wasn't far off, in all fairness."
    show GTS embarrassed
    "Luckily it wasn't particularly busy out, but Naomi drew a number of not-so-subtle stares and headturns from what passers were by. It dawned on me, too, how truly unusual she looked even in a place where people near three meters tall were quite usual."
    "The difference was, I knew how she felt about being unusual."
    MC "So yeah, you can see they're still doing fine."
    show GTS neutral
    GTS "So they are. Thank heavens for the school's dutiful gardener."
    show GTS happy
    GTS "And for you as well!"
    MC "Heh, I try. Sorry I can't show you the old rooftop plot except through pictures."
    show GTS neutral
    GTS "It is well, Keisuke-kun. Your gesture alone means a great deal to me."
    "She scooted on her knees a little more towards the planters, and then stooped down to peer closer, touching her hands to the ground before putting her weight onto them."
    show GTS happy
    GTS "Ah... how our lives abound with vices of material pleasure, and yet one finds nothing quite as invigorating as the sight and scents of a well-kept flower bed."
    "Her misty gaze floated over the whole garden, drifting to and fro in the richness of it. I suppose I became similarly absorbed, looking on her simple joy; seeing her gentle, easy smile, every time I yearned just a little more to give her that again."
    show GTS surprised
    "But her face jolted and she gasped just loud enough to hear."
    GTS "Erm, Keisuke-kun... my posture isn't too... immodest, is it?"
    MC "Huh? Uh..."
    "I looked up and down the rest of her statuesque form... trying to remain impartial. Suddenly it was growing difficult to put her first."
    "As I traced with my eyes down the slope of her back, a certain suspicion welled up in me; I circled around behind her to be sure."
    "And sure enough, it was. Resting atop shoes each almost as long as my legs, Naomi's rump, swaddled in pleated blue, jutted proudly up into the sky as tall as I was."
    "The dip of her back, the splay of her hips, her sheer immensity all exaggerated its flawlessly round shape, and being as big as a loveseat I felt powerless to resist the way it commanded my eye."
    menu:
        "Tell her she's fine":
            $setVar("GTS_selfhood", getVar("GTS_selfhood") + 1)
            MC "I think you're fine, don't worry."
            GTS "You're sure?... Very well, then. I trust you."
            show GTS neutral
            "Her shoulders laxed and she resumed her quiet admiration; I indulged some quiet admiration of my own before I circled back around to join her."
        "Tell her to adjust herself":
            "I thought after a few seconds to put my hand to my chin."
            MC "You might wanna straighten your back a bit more."
            show GTS despaired-thought
            GTS "...Oh dear."
            "She promptly heeded my advice and straightened herself, and seeing no further issue I came back around to join her."
            show GTS neutral
            $setAffection("GTS", 1)
            GTS "Thank you for telling me."
            MC "Of course."
    MC "Heh... and to think, the {i}very{/i} first time I laid eyes on you, you were stuck in one of those things, covered in dirt."
    show GTS unique
    GTS "Hmhmhm! Quite the impression I must've made."
    GTS "Ahhh... one could get lost in the memories that simple flowers can evoke."
    MC "Yeah... I think about that every time I water the ones on the roof."
    show GTS neutral
    "She chuckled again, and said nothing more."
    pause 1
    MC "What do you think of reflecting on the past?"
    GTS "A good question."
    GTS "It can be quite edifying to review one's deeds, to see how one might do better in the future. I do believe the past has much to teach us, generally."
    GTS "However, it does no good to compartmentalize the past. The spring, the river, the pond and the lake, all are the same water."
    MC "Huh..."
    pause 0.5
    MC "Yeah. That's pretty insightful."
    GTS "Well, I can only hope those they conjure up in {i}you{/i} are as happy as those they do in me."
    "I looked over at the breezy contentment on her face as it reflected on mine."
    MC "Y-yeah."
    "Tripping over my own tongue, I tried to clear the air of my misstep with something more eloquent."
    MC "Of course."
    "At that travesty what was, for her, a generous flicker of puzzlement sparked in her eyes for a forgetful half-second, "
    show GTS unique
    extend "before she gave me a pearly, expertly reassuring smile."
    show GTS neutral
    GTS "Well then, as I recall you wanted to show me something else today."
    MC "I sure did. You know that lake with the wooden walkway along the shore? There's a spot near there I want you to see, I'll show you when we're down there."
    show GTS happy
    GTS "Intriguing! Let's not tarry, then."
    "She eased herself back into a sitting position and held out her arms as though expecting a hug. That probably {i}was{/i} some small part of it, for her."
    "At that moment, too... it suddenly struck me how very strange it was that this had become so normal."
    "I stepped into her arms, reached up to secure my arms around the back of her neck, and up I went."
    scene black with fade
    pause 0.5
    scene Lake Road
    show GTS neutral
    with fade
    GTS "There we are. So, which way is it?"
    MC "To the left, if you follow the shore there's a little creek with a fallen tree lying across it."
    GTS "Ah, very good."
    "She turned, and looked down at the railing that didn't even reach her knees."
    show GTS embarrassed
    GTS "Somehow this feels a bit improper."
    "I reached out to rub her cheek."
    MC "It's okay, you can step over the fence, nobody's gonna see you."
    MC "And if somebody does, well we can live on the lam together. I'll hunt squirrels, you'll grow vegetables, we'll figure it out."
    show GTS happy
    "She snickered through her teeth, then turned sideways and lifted one dainty leg over the railing followed by the other."
    "And as we... well, she... strolled leisurely down the shimmering lakeside, I began to notice something of a snag in my plan."
    show GTS embarrassed
    "Followed by a few more snags, as tree branches hanging lower than I'd perceived from the ground kept brushing coarsely over her scalp and occasionally mine."
    MC "Nch... Naomi-chan, would you wanna let me down, then maybe you can just try to crouch a little."
    GTS "That sounds like a fine idea."
    MC "Oh, but lift me up a little first, I'll get those leaves and twigs out of your hair."
    show GTS neutral
    GTS "Ah, thank you."
    "She boosted me up higher until I was seeing over her head again, and I swept my arms across the broad, domed crest of her hair. {w}I thought I heard her breathe a lax sigh as I did so, and finally patted down the few stray knots."
    MC "Okay, I think it's all gone."
    "She nodded and lowered me down onto the damp, pebbly soil, and she bent her knees until she looked to be below the branches again."
    MC "I, uh, don't know how I forgot to account for that. I'm sorry."
    show GTS unique
    GTS "One cannot enjoy the peach without accepting the pit. I trust it's not too much farther?"
    MC "No, not at all. In fact..."
    "I stepped to the side and peered past her hips to see the stream well within sight."
    MC "Yeah, that's it over there."
    GTS "Splendid."
    show GTS neutral
    "With Naomi walking in a very peculiar-looking-for-her hunched posture, I was just able to keep up with her with a light jog."
    show GTS neutral at Transform(xzoom=-1)
    "But I found myself staggering to a stop, pebbles clacking under my shoes, as I saw her come to a slow halt at the edge of the stream."
    MC "Hm? Why'd you stop?"
    GTS "Before we go any further... well..."
    show GTS pondering
    GTS "Erm, when we were talking about the flowers just a bit ago, it seemed to me that something about the conversation made you uneasy. You're seldom so tongue-tied."
    MC "Oh, uh... yeah, I guess my brain did sort of glitch out back there."
    GTS "...Glitch out?"
    MC "A brain fart, pardon my French."
    GTS "I see."
    MC "But no, don't worry about that. It had nothing to do with the flowers."
    GTS "Well, if not that, then what? I apologize if I'm prying, but I felt it only right I should ask."
    MC "C'mon, it's your birthday, we shouldn't be talking about me."
    pause 0.5
    show GTS neutral at Transform(xzoom=1)
    GTS "When I said I love you, Keisuke-kun, I meant it sincerely. Even if this is to be \"my day\", as it were, I can scarcely overstate how much your wellbeing matters to me. My wish is for you to be happy."
    GTS "I won't press further if you do insist, but please know that I want to share your burdens whatever they may be."
    pause 0.5
    "I sighed, releasing a pressure in my chest I didn't realize was there. Naomi, with her hands folded over her lap, sat down in Seiza position in front of me."
    MCT "I guess I... don't really have a choice."
    MC "Eheh, it's... it's funny."
    MC "I love tending the garden for you because I know how important it is to you, and I think I even sorta get it myself, what you see in it."
    show GTS happy
    MC "But... every time I do it... I dunno, I feel like an herbivore."
    show GTS surprised
    GTS "What? You're patently no such thing."
    show GTS neutral
    GTS "You've won my heart, haven't you?"
    MC "Yeah, when I actually think about it I realize that pretty quick. It's just some personal baggage."
    stop music fadeout 5.0
    show GTS pondering
    GTS "If that's the case... why do you feel that way at all?"
    "For a second more I looked up at her, her big, patient amber eyes washing over me, making me realize that for both our sakes, I had to do this."
    pause 0.5
    play music Bittersweet
    MC "When I was in high school, I was dating this girl for a while."
    MC "Wasn't anything too deep, but you know, I liked her a lot. She was always smiling around me, always positive."
    pause 0.5
    MC "I think it was a couple months in, and I start hearing rumors floating around..."
    MC "And I find out..."
    "My teeth clenched the insides of my cheeks, involuntarily."
    MC "She fu-{w} {i}ahem{/i}. She'd... cheated on me. With our school's soccer captain."
    show GTS surprised
    "She gasped, sharply."
    GTS "Wh- I... why..."
    hide GTS
    show GTS_S angry with vpunch
    GTS_S "That perfidious harlot! How could she betray you?"
    "My staggering legs carried me backwards a meter or so as Naomi's voice resounded, shattering the air like I'd never heard it before. And though I knew she could be stern, I'd never seen the sort of intense, pointed scowl that now hardened her huge face."
    GTS_S "Of all the selfish, thoughtless, wanton..."
    hide GTS_S
    show GTS sad
    GTS "Mm... "
    GTS "Please forgive me, that was atrociously undignified of me. I didn't mean to speak for you."
    MC "It's okay Naomi-chan, it's just... I didn't expect you to get so mad over something that happened to {i}me{/i}."
    GTS "Well, why would I not? I may have overstepped, but it {i}is{/i} personal to me."
    GTS "I find such callous iniquity thoroughly odious, never mind that someone I hold dear should suffer the consequences."
    MC "Well... if nothing else, it's good to know you've got my back."
    show GTS neutral
    GTS "Of course, Keisuke-kun. I always shall."
    GTS "I'm sure that was extraordinarily difficult to say aloud. I'm sorry to have dredged up bitter memories, but I'm thankful for your trust and I hope that airing them has brought you some peace."
    MC "Heh... Yeah, I do feel better."
    GTS "As do I."
    stop music fadeout 5.0
    scene black with fade
    "She leaned down to envelop me in a tender hug; her folded hands caught my back and gently pushed me up against the pillowy slopes of her chest."
    "With my head buried in the crook of her neck, all light, all distraction was closed from my eyes. It was just me and her; I reached up and put my arms around her shoulders."
    "I felt something welling up in my chest as we lingered in each other's embrace, a tightness, until at last I expelled it as a hard, softening sigh."
    "We enjoyed a quiet moment or two more, yielding to the babbling water and the whistling songbirds."
    "Finally, I pulled away."
    scene Lake Road
    show GTS neutral
    with fade
    MC "Well... shall we continue on? It's just a little ways up the stream."
    GTS "Yes, let's."
    "I tilted my head towards the corridor of trees through which the waters ran, and we advanced through the speckled light of the forest floor together."
    scene black with fade
    pause 0.5

    scene Woods with fade
    play music LoveA
    MC "There, in that clearing off to the side."
    show GTS surprised with dissolve
    GTS "Ohhh..."
    "She looked around, and even her gentle rasp softened to a lackadaisical wind of wonderment."
    show GTS neutral
    GTS "Heavens, how exquisitely picturesque."
    hide GTS
    show GTS_S happy
    GTS_S "And how delightful it is to be able to stand up straight again!"
    MC "I thought you'd enjoy that."
    hide GTS_S
    show GTS pondering
    GTS "Is that..."
    show GTS surprised
    pause 0.5
    show GTS happy
    GTS "My goodness, look at all the lupins! They're beautiful!"
    GTS "I've never seen them in the wild, never mind so many!"
    show GTS unique
    "She knelt down to brush her hand slowly over the patch, at which their pale pinks and violets shimmered in the sun."
    "In the midst of her appreciation, I saw her head shift towards something in her periphery."
    show GTS pondering
    GTS "Hm? What's that over there?"
    MC "Huh?... That thing?"
    GTS "Yes. It looks to be some kind of... brazier? What on earth is it doing in the middle of the woods?"
    MC "Who knows... I guess it's a surprise."
    GTS "What do you..."
    "Preempting her question, I walked over beside the brazier and slid my backpack off my shoulders."
    show GTS happy
    "I watched the comprehension dawn on her face and turn her cheeks a rosy hue, as I drew from my backpack several bags of lax beef shoulder cutlets soaked in aromatic brown juices, a few bags of assorted vegetables, and another few bags of charcoal."
    GTS "A yakiniku picnic? Heavens above, how did you find the time to arrange all of this?"
    MC "I have my ways. I couldn't really find a way to store the dipping sauce without, uh, marinating my notebook, so I just marinated the filets instead."
    show GTS unique
    GTS "How clever."
    MC "Well c'mon, have a seat. I'll get everything ready."
    show GTS neutral
    "She cleared the five or so meters between us in a couple steps, and eased herself down into an immaculate posture while I began to light the charcoal."
    MC "I imagine you've had yakiniku before."
    show GTS unique
    GTS "Once or twice with my friends, yes. I found that I was quite fond of it."
    "I smiled as an orange glow began to spread from the match to the pile of briquettes, and I withdrew and blew the withered match out."
    MC "Well, I don't know how this compares to the sorts of birthday celebrations you're used to, but I hope you like it anyway."
    GTS "Perhaps it's too early to say... but I already feel it's the best one I've ever had."
    "Hearing that, I felt a sudden kinship with the flames swelling brighter before me."
    if checkSkill("Academics", ">", 2):
        MC "..."
        MC "You... never had birthday parties, did you?"
        show GTS despaired-thought
        GTS "...Well, that's not entirely true."
        show GTS neutral
        GTS "On my sixteenth birthday my friends treated me to a performance of Sugawara Denju Tenaraikagami."
        GTS "But generally, no, our family simply never adopted the custom. To expect to be lavished with gifts and attention, even one day out of the year, is rather unconducive to building a virtuous character."
        MC "But that's not all they are, of course."
        MC "It's {i}also{/i} a chance for friends and family to express how much they appreciate you."
        GTS "Indeed. There are two sides to every coin, as it were."
    "At last the brazier was nursing a low, steady flame; I laid the gridiron over it by the edges, and then two of the drizzling cutlets."
    "They hissed lowly at the touch of the flames, breathing out a savory scent that did for my stomach what the sunlight did for my scalp."
    GTS "They already smell positively scrumptious!"
    MC "You could say it's a family tradition. My dad's got a black belt in barbecue."
    MC "...Although admittedly I just asked Kodama-san to point me to a good recipe."
    GTS "Just as well. It used to be quite common to study various skills under a distant relative or a family friend."
    GTS "The results speak for themselves."
    "After a minute or two of searing, the meat had turned a glistening brown and its scent had grown heavy; I reached into my backpack once more, withdrew a pair of tongs, and raised them up towards Naomi."
    "She stared at the proffer a moment, her lips contorting into a polite smile, and she took it."
    GTS "Thank you."
    MC "You're very welcome."
    "She wedged the tongs between her pointer and thumb, then reached down to pick up a filet."
    show GTS surprised
    "Her eyes widened as she popped it into her mouth."
    if getSkill("Academics") > 2 and getSkill("Art") > 2:
        $setAffection("GTS", 2)
    else:
        $setAffection("GTS", 1)
    GTS "This is... exquisite."
    MC "You like it?"
    show GTS happy
    GTS "Very much so! Perhaps you inherited more from your father than you thought!"
    MC "Heh, I wouldn't have guessed, from the couple of times I tried to help my dad on the grill..."
    show GTS embarrassed
    GTS "It does take some doing, doesn't it..."
    "After prodding the charcoal, I began laying down more meat on the grill."
    show GTS neutral with dissolve
    "..."
    "And as funny as it is to say, in the proceeding minutes, not a word was said between us."
    "What I shared with her instead was a full appreciation of the sights and sounds, dancing smoke and pensive flowers. It was the easiest thing in the world now, like opening my eyes."
    "I saw hers grow lax and sleepy; at first they swayed to and fro like a hunted woman as she effortlessly put away steak after steak. But she settled in soon enough."
    "I grilled some vegetables and beef tongue medallions for myself, too, and soon all the bags sat empty in a pile."
    "Naomi raised a hand to her side, but stopped."
    GTS "By any chance did you bring some handkerchiefs for the two of us?"
    MCT "..."
    MCT "I may be stupid."
    MC "That, uh, may have slipped my mind."
    show GTS unique
    GTS "Oh well. One hardly remembers a meal for the napkins."
    hide GTS
    show GTS_S neutral
    "Naomi wiped the sparse stains on her lips with a smooth swipe on the back of her hand, stood, and ambled toward the stream."
    "The water murmured, rolling under and over her fingers; then she was satisfied, and flicked the gleaming droplets off her fingers one by one, casting rippling ghosts of broken rings on the surface of the water."
    "She walked back my way but didn't sit."
    GTS_S "Moreover, that may have been the best meal I have had since arriving here."
    MC "I'm honored. But, I have just one more thing before we go."
    hide GTS_S
    show GTS pondering
    GTS "Oh?"
    MC "Wait here a second."
    hide GTS with dissolve
    "I stepped just inside the veil of the trees, turned left at the arched branch, and there was the prize just where I'd left it."
    "I withdrew the baggy of mizuhiki from my pocket and set to work tying a nice bow around it."
    MC "...Perfect."
    if checkSkill("Athletics", ">", 2):
        "I knelt down, hugged the base, and stood to carry it into the clearing."
    else:
        "I knelt down, wrapped my arms as far as they would go around the base, and tried to lift."
        MC "Hrmph!..."
        "Immediately reviving the withering ache in my arm bones from dragging it out there in the first place."
        MC "{size=-6}Fuck's sakes, you better behave for her...{/size}"
        "The first attempt was a wash, but I lifted with my knees on the second try and managed, with the graceful swagger of a gazelle with brain damage, to stagger backwards to a full standing position."
        "Step by plodding step, I carried the burdensome thing out into the clearing."
    show GTS surprised with dissolve
    "Her wide eyes as I emerged from the treeline instantly rewarded the effort."
    GTS "Keisuke-kun... how..."
    MC "I, uh, got up a little early this morning to hide it. I figured it wasn't terribly likely anyone would steal it, so, yeah."
    GTS "Is that... a persimmon sapling?"
    MC "Yeah! It's a pretty hardy variety, so it {i}should{/i} grow okay in this climate."
    pause 0.25
    MC "At least, that's what the clerk said."
    MC "It's still young, but I thought it'd be something you could reasonably work with, and also eventually give you a little something to offer whenever you have guests over."
    MC "The planter's biodegradable too, so you can use that for compost. I think?... I know these apparently don't like regular fertilizer."
    MC "I... hope you like it."
    show GTS happy
    "She clasped her hands together over her breast as she beamed with a blush at the tree."
    GTS "I {i}adore{/i} it! Living by that barren old pit with nothing to grow or care for, I almost felt as though I'd lost a part of myself."
    GTS "But you've... brought it back."
    show GTS aroused
    GTS "Two words scarcely seem adequate for such a wonderful gesture, but... thank you. Thank you ever so much."
    "I came closer, warmed by her bright, shining face."
    MC "Happy birthday, Naomi-chan."
    show GTS unique
    "She said nothing, but rather leaned down to plant a lingering kiss on the entirety of my cheek, with her palm bracing my torso and her finger stroking the back of my head just so."
    "My face grew hot from the contact."
    "At last, a soft smack of her lips signaled her parting from me, and her head rose up toward the canopy."
    GTS "I love you Keisuke-kun, and I endeavor to show it as will make you feel as wonderful as you've made me."
    MC "You do it effortlessly."
    show GTS neutral
    GTS "Ah, well then... I don't suppose you have any other surprises up your sleeve?"
    MC "Well, that sort of was the big thing just now... but I brought along a book of modern haiku, if you'd like to read through that for a little while."
    GTS "That does sound lovely..."
    GTS "Although, I would like to return to my dormitory soon to pick out a suitable spot for the tree."
    MC "Sounds good. I can carry it over there, if you like."
    show GTS unique
    GTS "Oh, please don't trouble yourself on my behalf. I would feel rather guilty if I allowed you to toil any more than you already have."
    MC "As you wish. I... suppose I should probably take care of the grill anyway."
    show GTS neutral
    GTS "That would be considerate, yes."
    GTS "Ah, and that reminds me of something."
    GTS "I've been doing a bit better with the recipes Kodama-san showed me, and so I've been trying to try my hand at other kinds of cookies."
    GTS "Would you perhaps like to visit my dormitory later this afternoon and let me know how they turn out?"
    MC "Yeah, I'd love to! You've gotten a {i}lot{/i} better since that one time I sat in on your lesson."
    show GTS unique
    GTS "Splendid! In that case, I shall see you again soon."
    show GTS neutral
    "She treaded gingerly past me to pick up the sapling, and then turned."
    GTS "Thank you for a truly unforgettable birthday celebration."
    MC "The pleasure is all mine."
    show GTS unique
    GTS "Indeed."
    hide GTS with dissolve
    "With the sapling nestled close in her arms, she ambled down the stream and out of the clearing, soon vanishing into green shadow."
    "As for me, I knelt down to clean up."
    MCT "Looks like I was just about right. It looked like a potted fern in her arms. That oughta be manageable for her."
    pause 0.25
    "I snorted as I stuffed the bags into one another."
    MCT "Figures she wants to give {i}me{/i} something on {i}her{/i} birthday."
    MCT "Oh well. Whatever makes her happy."
    jump daymenu

label GTS046:
    $setProgress("GTS", "GTS047")
    scene Giant Dorm Interior with fade
    play music HigherEdu
    "After a couple hours of chilling at my dorm and digesting lunch, I headed over to Naomi's dorm, guided by the light of promised cookies."
    show GTS neutral with dissolve
    "I looked up to see her face brighten as she greeted me at the door, as ever."
    GTS "Ah, you've brought your backpack. Is there some material you'd like to review together while you're here?"
    MC "Ah, heh, yeah, I kinda forgot about our lit assignment. I'll just work on it while you're making the cookies."
    show GTS happy
    GTS "Ah, very well. Come on in then, make yourself comfortable. I've just begun making them."
    show GTS neutral
    "She bent down to give me a peck on top of my scalp and turned to walk back to her kitchen counter; I headed for the couch, and immediately noticed a stack of wooden crates assembled into a staircase leading up to it."
    MC "Huh. Did you put that together yourself?"
    GTS "Well, of course I obtained permission from the school administration first. They're filled with styrofoam blocks for a bit of extra support."
    GTS "The prior arrangement, when I considered it, was not very accommodating to guests."
    MC "Good thinking. Can't expect everyone to be able to climb up there, right? Imagine if Nikumaru-san came over here."
    GTS "Yes, that would be a conundrum."
    "I climbed the makeshift staircase, finding it sturdy underfoot, and sat myself down. I peeled off my backpack as I began to watch my girlfriend at work."
    "She treated her first time making chocolate chip cookies like her first time performing brain surgery. She did each step at either breakneck pace or slow as a circling buzzard, with nothing in between."
    show GTS embarrassed
    "She threw in a measuring cup full of chocolate chips, only to pour in just a little bit more a second later. With lips pursed and brow furrowed, her every movement was rock-solid with determination,{w} sprinkled with just a pinch of fear and frustration."
    MC "Is everything okay over there, Naomi-chan?"
    show GTS neutral
    GTS "Oh, quite, never fear. I just want to make sure I have everything in order and done properly."
    MC "I can tell. You've got such laser focus I'm half expecting you to burn a hole through the counter."
    GTS "Hah... I aim to please."
    MC "Well, I don't mean to intimidate you but hanging out with Honoka-chan means I've become {i}quite{/i} the cookie connoisseur."
    show GTS wink
    GTS "Well then, I've quite a standard to live up to, don't I? Nevertheless, I'm sure you will enjoy what I have to offer."
    MC "As am I, Naomi-chan, as am I."
    show GTS happy
    "She laughed as she turned right back to folding the dough, visibly much more relaxed. I opened my backpack."
    MC "!..."
    "...But my notebook staunchly resisted its removal."
    show GTS neutral
    MCT "What could it {i}possibly{/i} be stuck on..."
    "The bottom was curved under the textbook beneath it, and after a couple firmer tugs it still wouldn't budge."
    "The time had come to play hardball."
    show GTS pondering
    "I shoved my hand deep in, dug my fingers into the cardboard, and..."
    "{i}snap{/i}"
    show GTS surprised
    "Completely disemboweled my backpack with one hard rip, extracting my warped notebook and launching a box of pencils across the floor."
    MC "Shhhhh..."
    MC "Sheep."
    GTS "Are you alright?"
    MC "Ah, I'm fine."
    "I held up my notebook and saw that the bottom portion of the wire binding had been pulled taut."
    MC "Looks like the binding of my notebook got caught on something. Hold on, I'll clean up these pencils."
    show GTS neutral
    GTS "Thank you. I'll stay as still as possible."
    "I made my way down the makeshift steps to the floor, and crossed its gray expanse towards Naomi's huge, wan, elliptical shadow, picking up pencils every meter or so."
    hide GTS with dissolve
    "The last pencil was only just visible, looking like an infant of a twig nestled up by Naomi's shoe. I got on my knees as my face came up against the hem of her skirt, and I crawled under to grab it."
    pause 0.5
    "And that's when I realized where I was."
    menu:
        "Peek upwards":
            jump GTS046_c1_1
        "Keep your eyes on the ground":
            jump GTS046_c1_2

label GTS046_c1_1:
    $setFlag("GTS046_peek")
    "I slowly craned my neck upwards and saw what truly lay hidden beneath her skirt."
    $ persistent.unlock_cgGTS046_upskirt = True
    show cg GTS046_upskirt with dissolve
    "Up above me, almost gleaming in the darkness, was a pair of brilliant red silken panties, outlined in their center an obscure but distinctly plump ridge that I could only assume was the entrance I'd only dreamed of seeing."
    stop music fadeout 1.0
    "A humble {i}clink{/i} rang in my ears as I, with thoughts elsewhere entirely, dropped the pencil."
    pause 0.5
    "Naomi continued stirring in complete silence. For a moment, anyway, until she started humming a jaunty tune."
    "I shook my head when I realized I'd just stared at her nethers without permission, retrieved the pencil and withdrew from under her."
    hide cg
    show GTS_S neutral
    with dissolve
    "I noticed as I turned around that her skirt was almost invisibly swaying side to side; lo and behold, I could see that it was coming from her hips, their languid, out-of-tune swagger."
    GTS_S "Is everything accounted for?"
    MC "Uh, yep. Pardon the ruckus."
    GTS_S "Think nothing of it."
    play music Rain fadein 5.0
    "She spoke up as I turned around."
    GTS_S "Did you see something pleasant down there?"
    MC "Um, why do you, uh, ask?"
    show GTS_S aroused at Transform(xzoom=-1)
    GTS_S "Because you're smiling, Keisuke-kun. And blushing."
    MC "Oh, uh... yeah. It was pretty... pleasant. Nice on the eyes, y'know?"
    "She closed her eyes over a knowing smile and turned back to her mixing bowl."
    GTS_S "I'd hoped you would think so."
    "And then... I don't know if I was really surprised... she laid her spatula down. Her eyes were open, but just a bit narrowed as she turned to face me."
    hide GTS_S
    show GTS aroused
    GTS "Perhaps you'd like a closer look."
    MCT "Buddha, Kannon, God, I owe you all big time. Oh sweet mercy this is happening."
    "Whatever puppy-like expression was on my face at the moment was reply enough. Before I said a word, she gently raised an arm and pointed to the couch behind me."
    GTS "Why don't you make yourself comfortable?"
    MC "It'd, uh, be my pleasure!"
    "I scolded my own tactlessness as I heeded Naomi's invitation and climbed, maybe a little too fast, up onto the couch; as I did, I felt the distant tremors of her footsteps slowly pursuing me."
    "I turned around and beheld the muted joy in her pursed smile; defying her posture, she was blushing too. For my part, force greater than I could ever defy held my eyes on her, and for all Naomi's stature it seemed she felt just the same."
    "Impeccably steady hands lifted the veil."
    GTS "Was this it?"
    "Now, it couldn't be a dream, could it? There they were, her taut panties red as a heart's desire at the center of legs taller than any man I'd met, and a trim waist as pale, as smooth, as mighty as a block of polished marble."
    "I tried to think of something adequate to say to her as my breath bucked out of my control and my deepest muscles twisted upon themselves."
    "Again, she stepped in my place."
    GTS "It is a perfectly delightful sight, isn't it?"
    MC "Yeah... amazing..."
    "And then, a rush of hot air subsumed what breath I had, as she stepped right up to the edge of the couch, one by one rested her knees on either side of me and lowered those crimson panties down onto my lap."
    GTS "Hmhmhm... but you of all people know, Keisuke-kun, that art we best remember is not content to satisfy sight alone."
    MC "And you {i}are{/i} a work of art."
    show GTS unique
    "I gasped through my teeth as her seated form towered over me, both of us grinning openly. Her body was hot as a furnace and almost heavy enough to crush my legs like so many twigs... almost. By design, I had no doubt."
    show GTS aroused
    "She lowered a hand to my face, stroking my cheek with one finger."
    if getFlag("GTS040_c2_2"):
        GTS "Do you remember the day you brought me that fairy tale book? You said you... kind of liked this condition of mine."
        MC "Yeah. I like it a lot..."
        "I rubbed my splayed hand over her knee, and with her free hand she lifted her skirt a little further still; I at once saw the invitation to explore as much of her thigh as I could reach. So I did."
        "But I couldn't quite reach all the way; there was always more of her, it seemed, and that was more than enough for me."
        "All the while, I could feel a certain heat from her oppressive weight, burgeoning through my pants into my lap. And maybe it was just my imagination, but I thought I felt a certain, subtle dampness, too."
        GTS "It relieved me {i}ever{/i} so much to hear that."
    else:
        GTS "May I share an observation?"
        MC "Of course."
        GTS "It seems to me that you... like this condition of mine. Am I correct in thinking so?"
        MC "Heh... well, what can I say? There's a certain allure to how... tangible your presence is."
        MC "How I look up and all I see is you..."
        "I rubbed my splayed hand over her knee, and with her free hand she lifted her skirt a little further still; I at once saw the invitation to explore as much of her thigh as I could reach. So I did."
        "But I couldn't quite reach all the way; there was always more of her, it seemed, and that was more than enough for me."
        "All the while, I could feel that certain heat from her oppressive weight, burgeoning through my pants into my lap. And maybe it was just my imagination, but I thought I felt a certain, subtle dampness, too."
        GTS "Ahhh... I can scarcely express what a relief that is to hear."
    "Her caressing finger slipped down my cheek and slid languidly down my chest, like a careless drop of honey the size of a ping pong ball. A darker shade of honey grew warmer in her eyes."
    show GTS happy
    if getFlag("GTS044_meet"):
        GTS "And after that wonderful night sleeping under the stars, well... I've come to realize how at peace I feel, simply having you in my arms."
    else:
        GTS "In fact, I've come to realize how lucky I really am. To have you in my life, to have moments with you like this..."
    "Her finger tickled my abs as gently as a digit the size of my forearm could, before floating back up to catch my underarm in her palm."
    "As I stared dumbfounded, she caught my other arm too..."
    show GTS aroused
    "And with a rush of air and a mild pit in my stomach, there I hung, face to giant face with her."
    "She looked at me, and I saw within her at once; the upward slant of her brows and the misty adoration of her eyes churned with her radiant blush, and the way she tried to hide how she gnawed her lower lip."
    MC "Heh... been a while since I looked you in the eyes this close."
    show GTS unique
    GTS "Far too long."
    MC "And the closer I look at you, the better I see how flawless your beauty really is."
    GTS "Ara ara, how flattering."
    GTS "I do understand the sentiment. Having you so close to me... it's enchanting."
    show GTS aroused
    "I sank a little as she withdrew one hand to brush aside my bangs, casting a shadow down my face."
    GTS "Such life and warmth in those eyes..."
    "She closed hers and pulled me in for a few hot kisses on the lower half of my face, which I reciprocated in my smaller way; her cheeks were hot and yielding under my palms."
    pause 0.5
    GTS "I want to show you how much I adore you.{w} However uncouth it may be."
    "She lowered me down a little, until my suspended arms were about level with the topmost button of her shirt."
    GTS "Would you be so kind?"
    MC "...Uh, y-yeah. Love to."
    show cg GTS046_hold1
    hide GTS
    with dissolve
    "Even knowing exactly where we were headed, there was some whisper in my mind telling me to show some restraint, against every tingling muscle and tempting thought in my body. How could I say no to the birthday girl, anyway?"
    "I reached forward and began undoing her shirt, and with each button released Naomi gently lowered me down to the next one."
    "With each one, the pale, bulbous teardrops of her breasts, each bigger than my head, peeked out a little more boldly, at last down to her stark crimson brassiere."
    "With each one, I saw the quiver of those plush mounds like a dance for newfound freedom. And with each one, I noticed how strained the buttons really were, how eagerly they ripped apart under my fingers."
    MCT "She's still growing, alright."
    MC "...When did you get this shirt again?"
    GTS "Hmm... a little over a week ago or so."
    MC "I see..."
    "She lifted me up again once I'd gone halfway down her abdomen."
    $ persistent.unlock_cgGTS046_hold2 = True
    show cg GTS046_hold2 with dissolve
    "And hugged me tight to her now-exposed chest. I sank in deep."
    MC "Mmm..."
    GTS "Mmm... hmhm..."
    MC "God, you're gorgeous."
    GTS "And I'm {i}all{/i} for you."
    "As one finger reached up to tousle my hair, her excited heartbeat thrummed away, so close to my ears. And the cycle of her breath, as I listened wordlessly, was deep, resounding, and meditative, a high wind over the ocean."
    "Altogether, I was in her world, and I loved it."
    "I splayed out my arms to catch her breasts, clutching my fingers to her sides."
    "It was some time before I noticed, definitively, a throbbing tightness growing between my legs. I didn't doubt she did, too."
    hide cg
    show GTS_S aroused
    with dissolve
    "And then, like releasing a field mouse back into the grass, she lowered me down."
    GTS_S "You needn't be so high-strung, you know."
    "Her hand cupped my backside as she began to speak in a lower register... God, it really was like a little chair."
    MC "Who, me? Psssh, nah. I'm capital G Gucci, babe."
    GTS_S "You know that I want you to be happy, don't you?"
    MC "Yeah... of course."
    GTS_S "Good."
    "Then, smiling down at me, she hooked one finger into the seat of my pants and underwear..."
    "{i}foomph{/i}"
    "And pulled the lot down around my ankles in one effortless tug."
    MC "Ng!"
    "The air was cold enough to jolt through my core, until her hand, swaddled in heat and ladylike softness, eased me down to a seated position. Her other fingertip caught nearly the entirety of my stiffened dick, and I took in one sharp breath."
    MC "Holy shit that's good, you're so, y- whew..."
    "I bit my tongue from saying \"you're so huge\", even if her towering, curvaceous body occluded anything else from my mind."
    "And it was enveloping, her warmth, her {i}size{/i}. I was putty in her hands, while she exerted no greater effort than that to stroke a cat. But stroke she did, curling her finger around most of my length and gently squeezing."
    GTS_S "Oh, this will be easier than I thought. What a specimen~..."
    "While she looked fondly down between us, every slow, accelerating crooking of her soft finger sent Heaven's lightning up my belly. I was going mad, mad for her."
    "My chest shuddered. My cock tightened, fuller by the second in her plush, unbreakable grip. I reached over to clutch the upholstery, and she gently guided my arms to her vast hips instead. Slowly, they were rocking."
    MC "Hooooh shit, oh shit, I'm close..."
    "Amidst my ecstatic throes she leaned down and my head was near swallowed between her hanging breasts. My face steamed over between her heat and mine."
    "She licked her lips, parted them with a quiet {i}pop{/i}, and turned towards my ear. The only other thing in my world was her breathy whisper..."
    GTS_S "Hold on, my love."
    hide GTS_S
    show GTS aroused
    "As I was seconds from exploding she lifted me up again..."
    show GTS aroused with vpunch
    MC "G-Gah!..."
    $ persistent.unlock_cgGTS046_hold3 = True
    show cg GTS046_hold3 with dissolve
    "And pressed my body into her face, slipping my dick in between her slick wet lips. She squeezed my backside a little, lapped her tongue on my tip, gasped a dreamy sigh that rolled up my chest."
    "And I burst."
    "I flooded into her, harder than ever in my life, convulsing, blind under crashing waves of joy."
    "When my sight shakily returned, it was consumed entirely by her blushing face, eyes closed, cheeks pulsing, gulping down every spurt as it came."
    "As my breath fluttered out of my chest and up toward the sky, she slowly opened her eyes."
    MC "Naomi-chan..."
    pause 0.25
    GTS "Thank you, Keisuke-kun... for the best birthday I've ever had."
    hide cg
    show GTS aroused at Transform(xzoom=-1)
    with dissolve
    GTS "Was that, erm, satisfactory?"
    MC "Satisfactory?...{w} Holy shit, not even my {i}dreams{/i} are that good."
    MC "Uh, pardon my language."
    GTS "That's quite alright."
    show GTS neutral
    GTS "I do apologize if I kept you waiting too long."
    MC "Well... likewise."
    show GTS surprised
    GTS "Oh... oh my, have I really been so crass?"
    MC "N-No... no, it wasn't {i}obvious{/i}. I just like to think... you know... I know you a little."
    show GTS neutral
    GTS "That you do."
    MC "Kssh, where did you even learn to do that?"
    GTS "Well, part of a girl's proper upbringing, of course...{w} is learning how to keep a good man."
    show GTS embarrassed
    GTS "I attempted to do some research on the internet, as it were, but there was very little, er, applicable information."
    GTS "In fact, essentially none."
    MCT "Oh but there is, if you know where to look."
    MC "So, all that was... you improvised that?"
    show GTS neutral
    GTS "Well, yes."
    pause 0.25
    MC "Jesus..."
    show GTS pondering
    GTS "Pardon?"
    MC "Nothing, nothing."
    MC "You really are something special, you know that?"
    show GTS happy
    "She nodded briskly, jolting me with the aftershock, and broke into a laugh that shortly proved infectious."
    "After a second or two when it died down, she cleared her throat."
    show GTS neutral
    GTS "I suppose I should finish making the cookies now. And, ah, put you down."
    MC "I imagine it's about time."
    "She carefully shuffled off the edge of the couch, and lowered me down onto it; remembering my state of dress, I stuck out my legs to land feet-first."
    GTS "Ah, I nearly forgot."
    "She knelt down in front of me and held my torso firm with one hand while the other shimmied my underwear back up my legs, followed by my pants."
    MC "Uh, heh... thanks, Naomi-chan. Want me to get your shirt?"
    GTS "Oh, yes please."
    "Her chest drew closer, looming over and around me; I reached out and... with some effort... closed the buttons on her shirt one by one. I did my best to flatten out the wrinkles."
    show GTS unique
    GTS "Thank you."
    hide GTS
    show GTS_S neutral
    "At last she stood and returned to the kitchen counter."
    "I watched her for a little while; she shortly returned to humming in the midst of her labors, and after some time I got my study materials together to start working. Not that my mind had really left her. Of course not."
    hide GTS_S with dissolve
    "A threshold had been crossed that day, one I knew, on some level, had hung open for some time. I just didn't really think it'd be her who would pull me through."
    "I knew my eyes were on my notebook but seeing nothing. All I could think about was all that could come after, now."
    "I knew I was smiling, too, and that, I was content to keep."
    show GTS_S neutral with dissolve
    jump GTS046_c2

label GTS046_c1_2:
    "I picked up the last pencil without any further ado, and crawled out from under her. It was tempting... more than a little, to be honest... but I was better than that."
    show GTS_S neutral with dissolve
    GTS_S "Is everything accounted for?"
    MC "Seems to be. I'll get out of your hair now."
    "She only nodded with a stiff smile as I turned to head back to the couch."
    "A few seconds later, she cleared her throat and began to hum a tune I couldn't recognize."
    jump GTS046_c2

label GTS046_c2:
    "Some minutes later, as I pored lazily over my notes, I heard the bassy squeak of an oven door being eased open, and then shut. I looked up to see Naomi slipping off a pair of oversized oven mitts."
    GTS_S "Your batch should be done in about ten minutes."
    MC "Huh? My batch?"
    show GTS_S unique
    GTS_S "Ah, yes. While I certainly don't expect you to eat all of them, I imagined you would prefer ones that were of more manageable size."
    MC "Oh, I thought you'd break off a chunk for me or something."
    hide GTS_S
    show GTS neutral
    "She shook her head as she approached the couch."
    GTS "Heaven forbid. That is how one treats a dog, not one's boyfriend."
    MC "...But am I a good boi?"
    show GTS unique
    "Naomi covered her mouth, giggling. She then patted my head with the tip of her finger."
    GTS "As adorable, cute, and precious as you are, I think you deserve a more dignified address than {i}that{/i}."
    if getFlag("GTS046_peek"):
        show GTS aroused with dissolve
        GTS "But if you must know... yes. You are."
        MC "Heh, I try."
        "I tried to laugh it off, but her widening smile told me she could see my blush."
    show GTS neutral
    GTS "Well now, let's see if we can't fortify your notes a tad."
    "I nodded and set my notebook and my lap, with my pencil poised; she eased herself down beside me, and scooted closer, and a little closer, with her hands folded over her knees."
    "We promptly got to work, sharing a laugh or two every so often wherever conversation carried us; all the while the warm scent of gooey, chocolatey cookies floated into my chest."
    "The anticipation was killing me."
    jump daymenu

label GTS047:
    $setProgress("GTS", "GTS049") #Change to 48 once it's been written
    scene Field with fade
    play music HigherEdu
    "No matter how many times I made the long walk to the giant dorms, the change in scale never ceased to put me off my footing, even if just a little."
    $setSkill("Athletics", 1)
    "Even still, visiting Naomi after class was just about a daily routine by now; making the trip so many times every week through the baking summer haze was good for cardio, that was for sure."
    "I was easily working off Naomi's steady line of experimental baked goods and then some."
    "I guess... she was just getting a little harder to resist these days. I really looked forward to getting to see her, and I could tell the feeling was mutual."
    scene Giant Dorm Exterior with fade
    "A butterfly resting on the chain link fencing whisked away as the gate rattled open before me. I spared a glance at it, flickering leafy green against the vast blue, as I strolled past and off towards Naomi's dorm."
    "I entered the building's engulfing shadow and stepped up to knock on the door."
    play sound Knock
    "After a few seconds, I heard a familiar booming voice from a few meters above me. Light and airy as it was, the reverb from the high ceilings and the sheer volume of her unrestrained voice still produced a potent echo."
    GTS "Hello, Keisuke-kun! One moment, I'll be right there!"
    "Hearing Naomi assume it was me brought some of the old butterflies fluttering back. And then I thought... she must not get a lot of visitors..."
    "A few moments later, the lock on the giants' door opened with a CLUNK and swung open; it looked as if the entire wall were opening up."
    scene Giant Dorm Interior
    show GTS neutral
    with fade
    "Naomi smiled down at me as she eased the big door closed. After a second, her eyes drifted to the small bag that I brought."
    GTS "It's good to see you again."
    show GTS pondering
    "The glint in her wayward eye told me she was curious. The more time passed, the more obvious her true thoughts were becoming."
    MC "Hey, Naomi-chan. You're probably wondering what's in the bag, right?"
    show GTS neutral
    GTS "My curiosity {i}has{/i} been piqued. Will you show me?"
    "Naomi slowly knelt down in front of me to get a better look. I rustled around in my bag, and her eyes widened, a slight motion greatly exaggerated by her size, the exact moment I pulled it out."
    show GTS surprised
    GTS "Looking Up to Nobi-Sensei'? What's that?"
    MC "Oh, just a show I watched a couple years ago. I was in the mood to rewatch it, I thought I'd offer if you wanted to join me. I think you might like it."
    show GTS happy
    GTS "Why, that sounds perfectly lovely."
    show GTS neutral
    GTS "What's it about?"
    MC "Well, during the reign of Emperor Saga, there's a yōkai named Nobiagari who attacks somebody on the road one day... but they turn out to be an imperial court wizard."
    MC "And as punishment for attacking people, he cast a spell to send Nobiagari into the future, where she'll be trapped in human form until she redeems herself..."
    show GTS surprised
    MC "...By becoming a middle school teacher for a year."
    GTS "A yōkai schoolteacher! What an outlandish idea!"
    MC "Yeah, it's pretty cool."
    MC "Oh, but first, is there anything you wanna do today?"
    show GTS happy
    "She nodded with vigor, her smile widening."
    GTS "Well, I finally found a suitable spot to transplant the sapling you gave me. And as lovely as it is, it did look a bit lonely..."
    show GTS neutral at Transform(xzoom=-1)
    GTS "I was wondering if you wouldn't mind coming with me to the nursery in town."
    MC "Not at all. That actually works out, the plant food jug for the roof is almost empty."
    show GTS happy with vpunch
    "She knelt down with a swiftness that was almost frightening in conjunction with her size... and gave me a peck on the forehead. Her lower lip half-covered my eyes and the suction pulled me a step towards her."
    GTS "You are the sweetest, Keisuke-kun."
    show GTS surprised
    "She shortly noticed my wide-eyed stare up at her."
    GTS "I apologize for that outburst. I should calm myself."
    MC "Heh... it's okay. Still... don't know your own strength, huh?"
    GTS "I, erm... suppose it will take more discipline on my part."
    MC "Well hey, don't sweat it. We'll just have to figure it out together."
    pause 0.5
    GTS "...Yes, you're quite right."
    "For a second, I pondered what I just signed myself up for with the woman who just knocked me around like a toy with only a breeze of a kiss."
    "Not that I would've ever chosen different."
    MC "Well! Should we go take care of business?"
    show GTS neutral
    GTS "Yes, let's. I'll show you where I planted the sapling on our way out."
    scene Giant Dorm Exterior with fade
    "I followed her outside and she beckoned me toward the back of the hangar."
    show GTS_S neutral with dissolve
    GTS_S "Here we are. These are rather humble beginnings, I admit, but it seems to be dealing with the soil well enough."
    show GTS_S embarrassed
    pause 0.25
    GTS_S "I do apologize about its placement."
    MC "What do you mean?"
    GTS_S "Well, this spot has the best light for a persimmon tree. Yet... it hardly seems appropriate to sequester away such a thoughtful gift behind a shack in a pit of dirt."
    MC "Well, for the time being there's nothing really to be done about the whole \"dirt pit\" part."
    show GTS_S sad
    GTS_S "Indeed."
    MC "So, let's just be thankful it's found a home where it'll flourish. Okay?"
    show GTS_S surprised
    "I sidled up next to her and put my arm around her knee; her hip took in a good portion of my face, like a mother songbird."
    show GTS_S happy
    GTS_S "Yes, let's."
    "After a moment of savoring the embrace, I looked again at the persimmon tree and noticed a handful of X's the size of throw pillows drawn in the dirt."
    MC "What are those marks? Are you planning on planting more stuff here?"
    "Naomi slowly nodded while she lowered herself, almost like a parent addressing her child. The height gap was so big at this point, we couldn't be next to each other without looking awkward."
    hide GTS_S
    show GTS neutral
    GTS "Luckily, saplings and small shrubs are permitted by the dormitory policy. As such, I thought planning out a small plot would be a nice little pastime."
    show GTS pondering
    GTS "Although, I have wondered if the administration might hear a petition for further efforts."
    MC "Efforts to do what?"
    show GTS neutral
    GTS "Well, I have also been contemplating the possibility of introducing some more greenery to these facilities as a whole. I know that I'm hardly the only one who's been rather put off by all this desolation."
    menu:
        "Isn't that kind of futile? We're only going to be here another six months or so, and half of that will be winter.":
            GTS "In a certain light, yes. But our enjoyment here and now is not the point."
            MC "Oh. That's fair, I guess."
            $setAffection("GTS", -3)
        "But how would you do that? Autumn's only a month away.":
            GTS "Well, I may be able to overwinter some plants inside my dormitory. The lighting is not quite ideal, but I think hardier plants shall have to rule the day regardless."
        "But is it not that yearning for greenery that is the cause of all the discontent?" if checkSkill("Academics", ">", 5):
            $setVar("GTS_selfhood", getVar("GTS_selfhood") - 1)
            $setAffection("GTS", 1)
            show GTS happy
            GTS "Well said."
            show GTS neutral
            GTS "Nevertheless, I do think it would be kind to do something small to help future students reckon with the changes they will face."
        "You think they'll approve that plan? There's probably a lot of red tape to go through.":
            GTS "That is true. One cannot say for sure."
        "What about, like, turning the top and bottom levels into a giant rock garden?":
            show GTS surprised
            GTS "Oh!"
            show GTS pondering at Transform(xzoom=-1)
            "Her eyes went wide and meandered over the parched, craggy landscape; her fingers curled over her chin in contemplation."
            show GTS surprised
            $setAffection("GTS", 1)
            GTS "Keisuke-kun, that's an excellent idea!"
            show GTS pondering
            GTS "Granted, even for the sort of person these facilities are intended for, that scale {i}would{/i} be rather ostentatious for a rock garden. The theming would be rather stretched thin, and it would be quite the chore to maintain properly, besides."
            show GTS neutral
            GTS "Hmm... but one or two well-placed gardens could make for a lovely setpiece, lovely indeed..."
    GTS "..."
    show GTS despaired-thought
    "Naomi looked around the quarry as a whole, scanning her head slowly as she viewed one end of the mining pit to the other."
    GTS "Mmm... it'd take far more than a few trees and shrubs to make the area feel liveable, though."
    GTS "First, the soil would need to be tilled to plant grass. That would make conditions more favorable for some flowering weeds, which would liven up the space a bit whilst we begin proper landscaping."
    MC "So, similar to the courtyard on the main campus."
    show GTS neutral
    GTS "Exactly. While we may not get the luxury of a sidewalk, I should think most would prefer to tread on grass over sandy dirt."
    MC "That'd definitely help with the whole, uh, \"construction site\" chic this place's got going on."
    show GTS happy
    "Naomi chuckled."
    GTS "One can hope."
    MC "Do you think your classmates will appreciate the changes?"
    show GTS neutral
    GTS "I certainly hope so. I can understand if some of them would prefer a more modern aesthetic with tile and sidewalk, but I need to think realistically. There's only so much that an individual can do."
    MC "You know, it doesn't {i}have{/i} to just be you. I bet your neighbors would pitch in, if you asked."
    "Naomi nodded."
    GTS "Yes... you're right. So often, I forget that I can go to my fellow man for help."
    show GTS sad
    GTS "I always did wish dearly to be the proverbial heart of the home. I am proud of how I contributed to my family, but now... {w}now..."
    MC "Now?..."
    show GTS neutral
    "A warm smile bloomed again on her face as she looked at me."
    GTS "Now, you're here... to show me how to live another way."
    "I smiled in return."
    MC "I'm glad that I helped make a difference."
    show GTS unique
    GTS "Thank you for being here for me."
    "We both stood there quietly, enjoying the moment. Time slowed down around us once more as a gentle breeze rolled through the quarry."
    "Specks of dust and sand flitted across my cheeks on the wind, but we could still find a brief moment of inner peace."
    hide GTS
    show GTS_S neutral
    "Naomi took a deep, hollow breath, then stood to her full height. Her shadow loomed over the trail connecting the dorms to the center of the quarry."
    MC "Well, should we head into town? Maybe we can add grass seed to the list."
    show GTS_S happy
    GTS_S "That would be wonderful."
    MC "The only trouble will be finding a grass dealer in a town this small."
    show GTS_S aroused
    "Smirking, she shot me a judgmental glare and lightly swung her leg out towards me."
    show GTS_S surprised with vpunch
    "Her playful kick rammed into me with the force of a clock tower pendulum, and I staggered on my toes with the world swirling around me..."
    hide GTS_S
    show GTS surprised with vpunch
    "But as I began to fall over, I found Naomi's massive yet graceful hands waiting for me. She caught my abdomen in her hands and gently righted my posture; there was the faintest tremble in her palms."
    show GTS sad
    GTS "I'm terribly sorry. Are you hurt?"
    MC "Heh, no. Maybe a little in awe."
    show GTS embarrassed
    GTS "I myself am a little in awe of all I have yet to learn."
    MC "Hey, turn that frown upside down, okay? No harm, no foul."
    show GTS neutral
    GTS "Mhm... as you say, Keisuke-kun."
    MC "That's the spirit. Now let's hit town, shall we?"
    stop music fadeout 5.0
    "She nodded, hoisted me up against her chest, and we made our way to the main road."
    scene black with fade
    pause 1
    $setTime(TimeEnum.EVE)
    scene Town with fade
    play music TwilightBright
    "After setting me down just as we were entering the town proper, Naomi seemed to want to set the pace this time around."
    "Every time her colossal legs made a stride in front of me, Naomi briefly stopped and turned her head to ensure I was keeping pace."
    "All that practice that we had with her slowing her strides helped a lot. Even though she was leading this time, her rhythm was perfect."
    show GTS neutral with dissolve
    "Naomi briefly exhaled, a very subtle look of nervousness upon her face as she returned to the tiled sidewalks in town."
    show GTS despaired-thought
    GTS "This perspective always feels so... unnatural."
    GTS "Part of me hopes that I never get used to this, while another part is telling me that I must. I'm not certain which I should listen to."
    menu:
        "You won't need to think about it all the time.":
            MC "I think you shouldn't have to \"get used to it\". Sure, it'll change you, but it's not a part of who you are. You'll still be Yamazaki-san to everyone else... and Naomi-chan to me."
            show GTS pondering
            "Naomi stood still for a few seconds as she slowly appeared more relieved."
            $setAffection("GTS", 2)
            GTS "That's very well put, Kei-chan. It's a very idealistic point of view."
            MC "Don't let it occupy your thoughts too much. You shouldn't worry about adjusting everything you do. Only... well, the walking stuff."
            show GTS neutral
            GTS "As well as holding things and speaking to others."
            MC "Well, yeah, that too."
            GTS "Though, you mean to say that... while my body may change, I can still present myself the same way to others. I'll still be myself. The essence of my spirit will be the same."
            MC "Exactly."
        "You should come to terms with it. It's something you can't stop.":
            $setVar("GTS_selfhood", getVar("GTS_selfhood") - 1)
            MC "You'll need to get used to your new size eventually."
            show GTS sad
            "Naomi slowly lowered her head as a gloomy air washed over her."
            GTS "Yes. I suppose you're right."
            MC "I... didn't mean to make you upset."
            show GTS neutral
            GTS "No, no. Don't worry about it. You haven't done anything wrong. If anything, I feel like that's what I needed to hear."
            MC "Something you needed to hear?"
            GTS "Exactly. I tell myself all the time about what I \"should\" do, or what a disciplined person ought to do. Left alone to one's own thoughts, though, we slowly become clouded with doubt."
            MC "That's why we rely on the people close to us. To hear more opinions, and gather advice."
            GTS "Right. I need to come to terms with my growth. I'll need to lean on others for support, just as you said."
            MCT "I hope I didn't sound too harsh..."
    scene Store with fade
    "We eventually made our way to a family-owned general store."
    show GTS happy with dissolve
    "Naomi needed to crouch down to see inside, but I could tell that she liked this place."
    GTS "Aha, perfect."
    MC "You found the seeds already?"
    show GTS neutral
    GTS "Actually, I was looking at that travel brochure."
    #MC "Mount Lanakila?"
    MC "Mount Kikai?"
    GTS "Well, that's one possible destination, yes. I was moreso pointing out the fact that the island is full of beautiful structures."
    GTS "For being such a small landmass, we're home to a lot of different biomes. Forests, plains, mountains, beaches..."
    MC "Would you wanna go there sometime?"
    show GTS pondering
    GTS "To where, specifically? There are so many choices, it'd be difficult to select just one."
    MC "Mountain climbing sounds enjoyable. It's challenging, but rewarding. It's a lot more interesting than a simple nature walk, isn't it?"
    show GTS surprised
    GTS "You think I'd be suited for mountain climbing?"
    "I chuckled."
    MC "Well, it'd be easier for you, certainly, but that's not what I was getting at. I meant it more as... like, a spectacle thing."
    show GTS neutral
    GTS "A spectacle?"
    MC "Yeah. The mountain range is nature's tallest formation, right? I guess I was trying to point out that it... suited you, for lack of better terms."
    show GTS embarrassed
    GTS "Ah. That's what you meant."
    MC "I didn't want it to sound too obvious."
    GTS "I understand. It's just funny that you mention mountaineering in particular."
    MC "Oh? Why is that?"
    show GTS neutral
    GTS "Winter happens to be my favorite season. I love the aesthetic of freshly fallen powder evenly coating a rolling field. The way that the snow weaves and curls as it gets blown by the wind..."
    GTS "I've always been curious what the peak of a mountain looks like when you're actually standing there. I've seen pictures, of course, but I imagine the experience can't accurately be captured in an image."
    show GTS happy
    GTS "Coincidentally, did you know that not all mountains are covered in snow year-round? Apparently, the trail we climbed to the shrine is often covered in a reddish-brown ash due to the volcanic crater at the top."
    MC "Really? I never thought about that. Every single travel brochure and postcard depicts it covered in snow. It's hard to imagine a mountain peak without it."
    show GTS neutral
    GTS "Exactly. It almost sounds like a foreign concept, doesn't it?"
    MC "I would like to go with you, if that's what you're suggesting."
    GTS "I'll need to make sure that there's proper equipment for someone my height, but... yes."
    GTS "I don't look forward to finding a winter coat in my size, but hopefully the academy should be able to accommodate me."
    MC "You mentioned that your favorite season is Winter?"
    GTS "That's correct."
    MC "It isn't Spring? I just sort of assumed, with all the projects you do..."
    "Naomi gave me a cold, piercing stare."
    GTS "There's a lot that you don't know about me, Keisuke."
    MC "..."
    MC "..."
    show GTS unique
    "Naomi began to laugh under her breath. She covered her mouth as a billowing breeze flowed through her cupped fingers."
    show GTS neutral
    GTS "Joking aside, I can understand why you'd feel that way. I appreciate the bounty that Spring gives us, but... Winter just has a certain inimitable beauty. It's like nature's way of resetting itself."
    GTS "It's as if the plains are being wiped clean, ready for another season of gorgeous flowers and crops."
    MC "I can see the wisdom in that."
    MC "...I actually believed you for a second, there."
    show GTS happy
    GTS "I can sound quite serious when I need to be. I hope I assured you that it was all sarcastic, though."
    MC "You did."
    "I briefly looked at the storefront, then slowly craned my view upwards towards Naomi."
    MC "Ah, right. How many bags of grass seed should I get?"
    show GTS neutral
    GTS "Two bags should be enough for my... er, grounds. I'll start with that, then go from there. I would like to make sure it can actually grow in the quarry before I invest more."
    MC "Got it."
    stop music fadeout 5.0
    "I walked inside the hobby store and picked up two moderately-sized bags of grass seed, about the size of a cereal box each."
    "With one bag in each hand, I paid for the bags at the register, then exited the store."
    show GTS neutral
    "Naomi was waiting for me outside, awkwardly trying to recline herself on the side of the neighboring building."
    show GTS unique
    GTS "Thank you, Kei-chan. I really appreciate this."
    show GTS embarrassed
    GTS "I would have loved to walk alongside you, but, ah- doorways."
    GTS "And ceilings."
    "I chuckled."
    MC "I understand. You can walk next to me now, though."
    show GTS unique
    GTS "I'll do just that."
    "I handed Naomi one of the bags, and she cradled it in her left hand. The bag, which I had to hold under my arm, fit like a graham cracker box in Naomi's enormous grip."
    "The two of us walked next to each other as the sun slowly began to set."
    jump daymenu

label GTS048:
    "Scene not yet implemented."
    jump daymenu

label GTS049:
    $setProgress("GTS", "GTS050")
    $setTime(TimeEnum.NIGHTLIGHTS)
    scene Dorm Interior with fade
    play music Rain fadein 5.0
    MCT "\"What does the author mean with his choice of curtains?\" What kind of question is that?"
    play sound Thunder
    "The shadowy sky behind the curtains gave its unhelpful reply as a deep boom of thunder, followed by the rattling of small objects in the room."
    MCT "I swear, these teachers grasp at straws sometimes trying to find questions to ask us about these books."
    "It was becoming clear that just trying to bang my head against my homework was more likely to give me a headache than results."
    MCT "Who would be awake right now AND able to help with this stuff? Daichi? {w}Probably not, he said he had to study for a test anyway. {w}Honoka? Nah, she was never strong with literature."
    play sound Thunder
    "My thoughts were again interrupted by a sky-shaking crack of thunder,"
    play sound Thunder
    extend " shortly followed by another, like the footfalls of a distant colossus."
    pause 0.5
    MCT "Naomi! Oh, I'm an idiot, of {i}course{/i} it'd be her."
    "I glanced out the window at the looming wall of darkness approaching the school, black clouds swallowing the gray sky. Checking my phone, I saw the no battery symbol flash."
    MCT "Well... I don't think she'll mind me showing up unannounced..."
    "I hurriedly stuffed my bag with my homework and jogged down the halls and stairs towards the Giants' Dorms."
    scene black with fade
    pause 0.5
    $setTime(TimeEnum.NIGHT)
    scene Giant Dorm Exterior with fade
    "I crossed the open fields with an unimpeded wind whipping, howling, slicing across my back. My skin grew cold where it touched, and I could feel my ponytail trying, with insufficient but surprising strength, to pull me away with the gale."
    play sound Thunder
    "I punched in the gate code and darted towards Naomi's dorm."
    play sound Knock
    pause 1.0
    "{i}plip{/i}"
    MCT "C'mon, c'mon..."
    GTS "{size=36}Hello?{/size}"
    "I jumped; that was Naomi alright, but her voice..."
    GTS "{size=36}Is someone there?...{/size}"
    play sound Knock
    GTS "Oh!..."
    show GTS_S surprised with dissolve
    GTS_S "Keisuke-kun! Come inside, posthaste!"
    "I marched through the door and around her legs without another word."
    scene Giant Dorm Interior
    show GTS surprised
    with fade
    GTS "Goodness gracious, what are you doing out in this dreadful weather? You would have caught your death out there!"
    MC "Eheh... funny story... I was, uh, stuck on my literature homework and I was hoping you might be able to help me out."
    pause 0.25
    show GTS unique
    "She just laughed."
    GTS "Gladly, Keisuke-kun. You had me quite worried, I'll have you know."
    MC "Sorry. It wasn't this bad when I left, I promise."
    show GTS neutral
    GTS "Oh, it's water under the bridge. No matter why, I'm glad you're here."
    GTS "Well then, have a seat and I'll get you some tea. Are you hungry?"
    MC "Nah, I'm good."
    MC "You scared the daylights out of me just now though, yelling like that."
    show GTS pondering
    GTS "When did I yell?"
    MC "...Just now, when I knocked on your door."
    GTS "I see."
    show GTS neutral
    GTS "My apologies, I didn't mean to keep you in the dark."
    GTS "I made yet another peculiar discovery not long ago. Whenever I would hum a tune whilst I was studying or doing chores, I noticed that over time the echo from my voice became louder."
    show GTS pondering
    GTS "I asked some of the school faculty about it, and apparently... I ought to expect my voice to become, er, significantly louder as my condition progresses."
    MCT "Why is that kinda hot?"
    if checkSkill("Academics", ">", 5):
        MC "I guess that makes sense. Presumably your vocal cords are growing in proportion."
        GTS "Indeed. It is as logical as one can expect for these circumstances."
        MC "So... have you just been... whispering for all this time, then?"
        show GTS neutral
        GTS "I would characterize it more as lowering my voice a tad."
        GTS "I'm certain you're well aware of the value of small acts of courtesy, in that light."
        MC "So aware I almost had a heart attack."
        show GTS embarrassed
        "She smiled a bit, though it was a rusty and strained smile."
        if checkSkill("Academics", ">", 8):
            MC "Wait, though, if that's the case... wouldn't the lower frequency of the air in your vocal cords also make your voice deeper? Except for the volume, you sound exactly like you did before."
            $setAffection("GTS", 1)
            show GTS pondering
            GTS "Astutely observed. In {i}theory{/i}, you are correct."
            pause 0.5
            GTS "...Unfortunately, the faculty whom I asked about it were as lacking in answers as I am now."
            GTS "Apparently our conditions here on this island are little understood, generally speaking."
            MC "Huh. Weird."
            GTS "Quite so."
    else:
        MC "Huh. Weird."
        GTS "Quite so."
        MC "So... have you just been... whispering for all this time, then?"
        show GTS neutral
        GTS "I would characterize it more as lowering my voice a tad."
        GTS "I'm certain you're well aware of the value of small acts of courtesy, in that light."
        MC "So aware I almost had a heart attack."
        show GTS embarrassed
        "She smiled a bit, though it was a rusty and strained smile."
    show GTS neutral
    "She cleared her face with a nod and walked off toward the kitchen, while I clambered up the stairs to the couch."
    GTS "Pray tell, what is it that's giving you grief?"
    "I wiggled back into the warm, yielding cushions, unzipping my backpack."
    MC "This question about what the author means by their choice of curtains. I was stuck on it for like forty-five minutes."
    GTS "I see. Is it what the question is asking you to find, or not understanding how to interpret the author's subtext?"
    MC "Both, maybe? Might be more towards understanding the author's subtext cause I'm not sure how to understand his choice of curtains."
    GTS "I see."
    "I could hear the wind picking up to a bestial howl just behind the metal walls as Naomi set out her teamaking kit; the metallic patter of the raindrops on the roof was speeding up bit by bit."
    GTS "Well, I don't wish to patronize you, but what is the fundamental purpose of a curtain?"
    MC "To... give privacy? Or block light?"
    GTS "Indeed. Curtains isolate. They obscure."
    GTS "And we know the curtains in the story were of a thin white material. Based on that, how might we interpret their significance?"
    MC "Hmm... white..."
    MC "...Oh my God, it wasn't one of those stupid \"actually dead all along\" stories, was it?"
    GTS "Hmhmhmhm! Fortunately, I think not."
    GTS "To tell you what I made of it, I think their significance lay more with the {i}villain{/i} than the protagonist."
    MC "How's that?"
    show GTS pondering
    GTS "The villain's motive appeared to be some misguided crusade to save people he favored, as it were, from the ills of society. He mentioned things like impurity and corruption."
    show GTS neutral
    GTS "And if that were the case... would it not be fitting that such a person would keep their view of the outside veiled by an illusion of moral purity?"
    GTS "The illusion of moral purity, after all, is far more within reach."
    pause 0.25
    MC "Ksh..."
    show GTS embarrassed
    GTS "Did I... say something funny?"
    MC "Intelligent, charming, and drop-dead gorgeous. I must've been a saint in a past life to wind up with you."
    show GTS aroused
    "She looked away, but I could still see the rosy hue blossoming on her cheeks."
    GTS "As ever, Keisuke-kun, you do know how to make me blush..."
    MC "I bet you could lift a couch over your head, too."
    show GTS embarrassed
    GTS "Perhaps, but... er, well, let's not wander too far astray. Keep at your homework, the water's almost to a boil."
    MC "Yes, mommy."
    show GTS surprised
    MC "..."
    GTS "..."
    pause 0.5
    MCT "Why did I say that..."
    MC "...Eh, sorry, I'm just joking. I know you're just looking out for me."
    GTS "That's quite alright."
    "I looked back down at my notebook, firmly planting it over my lap."
    show GTS neutral
    stop music fadeout 3.0
    play music LoveA fadein 1.0
    "She began humming a tune, softly, just before pouring the water and whisking in the tea powder."
    "At last, she brought the cups over on a tray and sat down beside me; air rushed past my cheeks as, gentle though she was, the sudden crater in the upholstery caused me to tip over towards her."
    show GTS unique with vpunch
    "By instinct I flung my arm out to stabilize myself, planting a palm on her hip and sinking in a few centimeters. She giggled as I righted myself, and in a second I was laughing, too."
    GTS "I'm sorry, that was a bit careless of me."
    MC "Don't be. It's actually pretty comfy down here."
    show GTS neutral
    GTS "Quite...{w} Well now, let's get to work, shall we? I'm sure you'll have it in no time."
    "We chipped away at the assignment together, but we did it chatting, joking, laughing. I wouldn't really call it work."
    "Too soon, in fact, I'd punctuated my last answer."
    MC "Well, that's a load off. Thanks for helping me out, Naomi-chan."
    show GTS happy
    GTS "It was my pleasure."
    "I paused for a second, wrestling with the sense of obligation that alone compelled me to say goodbye."
    show GTS neutral
    "That's when I heard the raindrops again."
    "The mad staccato of the downpour had now blended into an unbroken ambient rumble; the windows showed nothing but glossy black, save a few bands of glowing white that wavered in the reflections of the raindrops."
    MC "It's really coming down out there..."
    show GTS surprised
    GTS "So it is... I would hate to see you walk all that way, it wouldn't be safe."
    show GTS neutral
    GTS "Well, under the circumstances... I'm sure the school administration would understand if you spent the night here."
    "I gulped."
    MC "Well, tonight, there's nowhere I'd rather be."
    show GTS happy
    GTS "The feeling is mutual, as I'm sure goes without saying."
    "I huddled up next to her hip and lifted up her hand to kiss it, only partly noticing the substantial effort it took to lift."
    show GTS aroused
    "It didn't seem much more difficult for her to gently grab me around my middle and hold me up to her waiting, puckered lips."
    "It never got old, basking in her ambient body heat for a moment."
    "Then, rather than let me down, she pressed me against her chest in a hug, turned to the side, and laid us down on the couch. The moment I took in the view of her looking up at me, her sleepy expression like starlight, I forgot all about the storm."
    MC "Heheh, not in the mood for meditation, are you?"
    show GTS embarrassed with dissolve
    pause 1
    show GTS sad with dissolve
    "But rather than the coy reply I'd come to expect, she looked away for a second or two, her features wrinkling; in those wrinkles I saw her heart writhing."
    MC "Naomi-chan? What're you thinking about?"
    pause 0.5
    GTS "You."
    GTS "I love you, Keisuke-kun. I feel for you like I never have for anyone else."
    GTS "So much so, that sometimes..."
    GTS "Well..."
    GTS "In my idle moments, it can be difficult for me to keep my mind clear as it should be. I think about you, our love. I can't... keep myself from desiring you."
    show GTS neutral
    "Staring deep into me, a thin smile returned to her face. I was awash in loving moonlight."
    "It was strange; even so far along, it felt strange for her to open up even as much as that.{w} At the same time, it was immediately intoxicating."
    "I thought over what she said in a mutual silence."

    menu:
        "Support her":
            jump GTS049_c1_1
        "Embrace her":
            jump GTS049_c1_2

label GTS049_c1_1:
    $setVar("GTS_selfhood", getVar("GTS_selfhood") - 10)
    MC "Naomi-chan..."
    "I crawled forward, to be nearer to her."
    MC "If you're ever struggling with anything, you should tell me. Why suffer in silence?"
    show GTS surprised
    GTS "I'm not!..."
    stop music fadeout 5.0
    show GTS sad with dissolve
    GTS "...It's rather silly of me to dance around it with you, isn't it?"
    play music GTS fadein 1.0
    pause 0.5
    GTS "Please know that you could never be anything but precious to me, but..."
    GTS "Heavens above, it sounds so cruel."
    MC "It's okay, it's okay. I'm listening."
    GTS "But... {w}that's exactly the problem."
    GTS "I love thinking about you, but some days I can't spend my idle moments doing anything else. I try to meditate, but it's fruitless. I keep coming back to you."
    GTS "This... attachment..."
    GTS "It's as if everything my parents meant to instill in me to lead a virtuous life... was for naught."
    "Naomi sank lower in her seat as she went on, wilting."
    show GTS aroused
    if getFlag("GTS046_peek"):
        GTS "I thought a lot on what we did on my birthday... on what I'd like to do if we got another moment together like that... what I'd like to do to you..."
        show GTS embarrassed
        GTS "So much..."
        show GTS sad
        GTS "Please believe me when I say I never meant to mislead you."
        GTS "I suppose, for all my elders meant to teach me, I... don't really understand how to be a good girlfriend."
    else:
        GTS "Especially after that wonderful picnic you threw, I thought so much about just getting some time alone with you."
        GTS "I went so far as to go back to the outfit shop and purchase some rather, erm, racy undergarments... just so I could imagine you taking them off."
        GTS "I..."
        show GTS embarrassed
        extend " hmm..."
        show GTS sad
        GTS "I'm sorry, Keisuke-kun. Please believe me when I say I never meant to mislead you."
        GTS "I suppose, for all my elders meant to teach me, I... don't really understand how to be a good girlfriend."
    GTS "Oh, how have I so easily lost my way?"
    MC "Naomi-chan..."
    "If I could kick myself in the ass for what I was about to say, I would've. I was lying atop my greatest, most outlandish fantasy made real as my own two hands, and I was just about to let it slip through my fingers. Perhaps never to return."
    pause 1
    "But for the woman I love, I knew I had to do it."
    MC "I know how important your virtues are to you. And I... can guess how it must feel to have those kinds of feelings at the same time."
    MC "I don't want anything to come between us."
    show GTS surprised
    GTS "I don't either!"
    MC "So... I want you to know that I accept you no matter what. And you don't have to sleep with me just because you feel like you'll lose me if you don't."
    GTS "I... I see."
    MC "And if you feel like your own desires are keeping you from being the best person you can be, well..."
    MC "Then I want to help you in whatever way I can."
    pause 0.5
    GTS "Is that to say you don't want to... be more intimate?"
    "I sighed."
    MC "I won't lie to you, I do. I really do."
    MC "But not at the cost of your happiness in the long term."
    show GTS sad
    GTS "You know... the way my condition is, I don't know how long we'll still be able to be... intimate, in that way."
    GTS "That's a dreadful burden to put on yourself..."
    MC "I know.{w} I had an inkling going into it."
    MC "For you, it's a burden worth bearing."
    $setAffection("GTS", 10)
    show GTS surprised with dissolve
    pause 1
    show GTS happy with dissolve
    "The clouds of austerity broke with illuminating sunlight as she hugged me tight to her shoulder."
    GTS "There's still so much I don't know..."
    GTS "And I was so scared of how much I had to lose, but you..."
    "She squeezed a little tighter; I felt a droplet, big as my thumb, soak into my scalp."
    GTS "Meeting you was the best thing that ever happened to me!"
    "Her misty voice settled over me, and I felt all the warmer."
    "I was content, then, just to be close to her, experiencing oneness as never I had before. For that moment, I was sure to the depths of me that I'd reached her."
    "Naomi sniffled and wiped her cheek."
    GTS "My apologies. Your hair got a bit wet."
    MC "It's okay. I kinda like it."
    GTS "Hmhm..."
    stop music fadeout 3.0
    "After a moment of silence, she gently turned her head toward me and ran one hand up my back to rest on my shoulder."
    show GTS neutral
    GTS "Would you like to hear something funny?"
    MC "Yeah, I would."
    pause 0.25
    play music LoveA fadein 1.0
    GTS "When I was very young, one of my tutors asked me what I wanted to be when I grew up. "
    show GTS unique
    extend "I said I wanted to be a bodhisattva."
    MC "Pfff... heheh."
    GTS "Hmhmhm... my mother was quite proud of that answer."
    MC "I bet. It's heartwarming to see you're still chasing that dream."
    show GTS neutral
    GTS "Well, \"chasing\" per se would be rather futile, would it not?"
    MC "Er, right, right."
    "I turned aside and kissed her neck."
    show GTS aroused
    MC "I love you all the same."
    GTS "I love you, too."
    "I chewed my inner cheek for a moment or two as she gently glided her hand over my back."
    MC "Can I ask you something?"
    show GTS neutral
    GTS "Mm... of course."
    MC "You were a little closer with your mom, weren't you?"
    pause 0.75
    GTS "Well, in truth, my mother's duties as a mother did not demand quite the degree of stoicism as my father's did as a father."
    "I smirked."
    MC "So... yes?"
    show GTS unique
    GTS "Eheheh, yes, that's the word I was looking for."
    show GTS neutral
    GTS "What about you?"
    MC "Me? {w}I wouldn't say I was closer to one or the other. My mom was home more often, but my dad still made plenty of time to do stuff with Tomoko and me."
    GTS "Which reminds me, I still need to meet your sister one of these days."
    MC "Yeah, we'll have to do that. I'm sure she'd approve of you, but..."
    show GTS pondering
    GTS "But what?"
    MC "I'll just say be prepared to not have that much in common. Of course I love you both, but you're {i}very{/i} different people."
    show GTS neutral
    GTS "Even still, it would be an honor and a pleasure to grow closer to your family."
    GTS "At times I do wonder if I've made a bad habit of focusing on the differences between my fellow man and me."
    MC "Well, isn't that just human nature?"
    show GTS aroused
    "She breathed deep, and nodded once."
    GTS "So it is. You're right."
    "We both settled in after a moment; the storm rumbled on against the walls outside, with the low growl of faraway thunder as the last suggestion of its wildness."
    "It all seemed a little gentler now, just lying in her embrace."
    "Some time later, she stirred under me and slowly put her hands around my middle, raising me to her eye level."
    GTS "I don't suppose you have any other homework to do?"
    MC "I don't think so, actually."
    if checkSkill("Academics", "<", 5):
        MCT "At least, nothing I really wanna do right now."
    MC "...I think I still have that haiku book in my backpack. Wanna read it together?"
    GTS "That sounds wonderful."
    show GTS neutral
    "She sat up, placed me down on her lap, and pinched her index finger and thumb through the strap of my backpack to hold it up next to me. After fishing out the book, I opened it and cleared my throat in a storytellery manner."
    show GTS pondering
    GTS "...Erm, now that I think of it, wouldn't that book be due back at the library by now?"
    MCT "...Crap."
    MC "Well, you see, there were extenuating circumstances."
    show GTS wink
    GTS "Extenuating circumstances such as?"
    MC "...I was stuck on a boss in Magiria Knight 2 Remastered and I forgot."
    show GTS pondering
    GTS "Remastered? Did they make it again?"
    if getFlag("GTS028S_manga"):
        MC "Not quite. They updated the graphics and added some extra content where you..."
        MC "Wait, how do you know what that is?"
        show GTS neutral
        GTS "Well, I had been doing a little research with Inoue-san, and she told me about some of your likes and dislikes."
        pause 0.25
        GTS "It perhaps would have been simpler to just ask you."
        MC "Heh, maybe. But hey, it shows you care."
        show GTS happy
        "She nodded briskly."
        GTS "Dearly so."
        MC "Heh. {w}Anyway, yeah, I'll take it back first thing in the morning. Now, shall I?"
        show GTS unique
        GTS "But of course. Please continue."
        MC "Thank you."
    else:
        MC "Not quite, they just updated the graphics and added some bonus content."
        show GTS neutral
        GTS "Ah, I see."
        "I looked down at the book, though my thoughts were elsewhere."
        MC "...Heh. You remembered."
        show GTS unique
        "She leaned down and gave me a peck on the top of my head."
        GTS "If you care, I care, too."
        "Warmth sparked in my cheeks. Maybe I'd just tumbled into perfection."
    "I flipped the page."
    MC "Oh, a classic."
    MC "\"Clouds come from time t-"
    stop music
    scene black
    GTS_S "Oh!"
    "With a rustle of her shirt I felt Naomi's huge arms clutch me tight to her navel as the whole room was cast into abject blackness."
    GTS_S "Are you all right?"
    MC "Yeah, I'm fine. The power go out or something?"
    GTS_S "It would seem so."
    MC "It must be the storm."
    "My eyes drifted ineffectually down to the book that I could now only feel in my hands."
    MC "Well, there goes that idea."
    GTS_S "Hmm... perhaps not. I have an idea."
    GTS_S "Keisuke-kun, do you have a firm grip on the book?"
    MC "...Uh, lemme just close it."
    pause 0.3
    MC "Okay."
    GTS_S "I'm going to carry you to my bedroom. I have some candles and matches in my closet."
    MC "Oh, how romantic."
    GTS_S "...I'd hoped you would think so..."
    "Without any further ado, Naomi scooped one arm under me and lifted me up against her chest, a rush of air brushing my cheek."
    "She held me close as she leaned over the table, then eased me upward through the darkness; she made tenuous steps toward her bedroom door, each one punctuated by a shockwave through my body."
    "There was a click not far from my face, the yawn of hinges in the dark. A few moments more, and she laid me down on what felt like a tranquil sea of silk sheets."
    GTS_S "I've set you beside the nightstand; please take great care not to fall off."
    MC "I'll be careful."
    "I heard her walk away maybe a few meters and open another rickety-sounding door. Next came slow, hesitant rustling, metal tinkling, wood rattling."
    "I heard her walk back over and set the alleged candles on the nightstand."
    GTS_S "Ah... would you mind lighting the candles for me? I confess, I don't trust myself to manage it in the dark."
    MC "Of course. Lemme just find them."
    "After a moment's slow, blind groping, I laid hands on a thin cardboard box that emitted a woody rattle to the touch. On the third try, I struck the match at the right angle and it swelled to radiant life."
    "I found the two candles by its light, and they too sprouted flames; though most of the room remained in darkness, the neatly-made bed and Naomi's lower body were at last illuminated in the candles' pallor."
    show GTS_S neutral with dissolve
    play music LoveA
    GTS_S "There we are. Do you think you can comfortably read in this light?"
    MC "I think so. Thanks, Naomi-chan."
    GTS_S "The pleasure is mine entirely."
    hide GTS_S
    show GTS aroused
    "She bent down, bringing her face into the candlelight. Her expression as she looked down at me, painted in pale yellow crescents and ovals, was perfectly befitting of it."
    "Once more, she reached down and cradled me over her shoulder as she untucked the sheets and blankets, ever so lightly sat down on the mattress and scooted us under the blankets."
    MC "Mm, this is nice."
    show GTS unique
    GTS "Quite."
    "She reached down to rub her knuckle on my cheek, gently shaking me to and fro where I lay, and twirled my hair between her fingers."
    show GTS unique
    "Reaching out, I brought her nearest pointer finger to my mouth to kiss it, at which she giggled low and curtly."
    "With my sight returned, I glanced at the candles themselves; their shape had a distinctive taper, a faint, homespun roughness, and they sat on antique iron stands."
    MC "By the way... some fancy candles you got there. Are they homemade?"
    GTS "Why, thank you. And indeed they are. My grandmother taught me how to make them."
    GTS "She always kept such a lovely house and garden. She taught me much of what I know about homemaking."
    show GTS neutral
    GTS "It's a pity that my candlemaking days are quite past, but so things go."
    MC "Mm, yeah, I guess so."
    MC "Now, where was I?"
    "I opened the book again..."
    "And heard Naomi begin to mutter something before stopping herself."
    MC "Hm? Were you gonna say something?"
    GTS "My apologies for interrupting.{w} Thank you for coming to visit me tonight."
    MC "Of course. I... think we both said some things that needed to be said."
    GTS "Yes... we did."
    pause 0.5
    MC "Okay, here we go... \"Clouds come from time to time...\""
    pause 1
    "About a quarter of the way through the book, Naomi's occasional comments and exhortations of the prose faded away to appreciative mumbles."
    "A little bit longer, and all that remained was the ebb and flow of her breath, gliding over the crash of rain over our heads."
    "I saw no reason not to join her; I closed the book, sent it to the ground with a lax thrust of my arm, and shut my eyes. Maybe dreams really do come true."
    jump daymenu

label GTS049_c1_2:
    $setVar("GTS_selfhood", getVar("GTS_selfhood") + 3)
    $setFlag("GTS049_embrace")
    MC "Do you think I'm a good boyfriend?"
    show GTS happy
    GTS "Of course! You're a treasure among men."
    MC "Well then... you should know I want you to be just as happy as I am."
    MC "And you make me {i}very{/i} happy."
    MC "I know you have your doubts about some things, Naomi-chan. So let me try and put them to rest."
    show GTS surprised
    MC "I \"desire\" you, too. And it's not just that I admire who you are as a person.{w} Everything about you is fucking {i}hot{/i}."
    MC "{i}Especially{/i} your size."
    "I dragged myself a little further up her chest, eyes locked, held her smooth, regal jawline in my arms, and kissed her."
    show GTS aroused
    "She closed her eyes just before I did mine, and reciprocated with the force of a rolling cloud. Her sucking breaths held me tighter, tighter to her; my lips tingled, uncomfortably but enticingly, from the negative pressure."
    "One huge hand followed me up her chest; though her breasts spared me most of the weight of it, I nevertheless jolted a little from the sensation of her pinky finger lovingly but firmly stroking my ass."
    "I didn't say a word. Instead, I bore deeper into her, rubbing one hand in a tiny circle on her porcelain, reddening cheek."
    "There was the deep rumble of a moan in her breast, a shuddering giggle that rocked me up and down. A sudden wettening of my face from a nub of her tongue peeking out, and..."
    MC "GLM"
    "More of the wet, muscular mass shot up into my mouth, filling it completely and robbing me of air for a second."
    show GTS surprised with vpunch
    extend " I sputtered and sat up on my haunches, backed against her suddenly tensed hand."
    show GTS embarrassed
    GTS "I'm sorry!"
    MC "Pfhuah... hah... hey..."
    GTS "Yes?..."
    MC "Don't be. That was incredible."
    show GTS aroused
    "A devilish smile crept over her face again."
    GTS "Incredible? Really?"
    MC "Incredible. There's so much you can do with your size."
    GTS "Well... let's not grow complacent, now."
    GTS "There's so much better I could do."
    hide GTS
    show GTS_S aroused with vpunch
    "Before I could reply, she sat up halfway, sending me sliding back down her chest until she clasped her forearms tight against my back; an involuntary exhale puffed up out of my lungs."
    "She sashayed across the floor with bouncing steps, like she'd just won me from the claw machine and couldn't wait to take me home to play with."
    "The door groaned open, my head bounced against her chest, and I looked down just in time to see her sitting us down on her cloudlike, white silk bedspread."
    "She squeezed me tight to her side one more time before she let me go, laughing with her mouth closed. With my ear pressed to her ribs, the sound was thunderous. I couldn't help but think back to when I needed to help her water the flowers in the back."
    hide GTS_S
    show GTS embarrassed
    with dissolve
    "She leaned back a bit to look at me, seated on her leg, and as though I'd thought it into existence, the surety on her face had receded somewhat before an encroaching blush."
    GTS "I, erm... don't suppose you have experience with this sort of thing?"
    MC "Uh... once or twice. I can't say I ever had sex with a girl as tall as my house before, though."
    show GTS aroused
    "She blushed harder still."
    GTS "Oh, you cad..."
    GTS "Well then... shall I get us dressed for the occasion, or... would you like to?"
    menu:
        "Allow me.":
            jump GTS049_c2_1
        "Would you mind doing it?":
            jump GTS049_c2_2

label GTS049_c2_1:
    show GTS unique
    GTS "With pleasure."
    "I pushed myself up to standing position atop her lap and reached up for the top button of her shirt."
    "I {i}could{/i} touch it... but to my growing embarrassment, it was just barely too high to get a good grip on. I stopped to think of how to close the gap."
    MC "Hold on..."
    show GTS surprised
    "I hooked my legs as far around her midsection as I could reach, planted my hands on the tops of her breasts, and, already exerting myself more than I ever had for a woman, began a laborious climb up her body."
    if checkSkill("Athletics", ">", 4):
        "I'd never really imagined applying my workout regimen in this way, but nevertheless it was just enough. I worked my way up until I could rest my forearms fully atop her breasts as they filled my lap, and I finally had her top button within easy reach."
        "If I wasn't rock hard before, I certainly was after grinding up against her with vigor just to start taking off her shirt."
        show GTS aroused
        GTS "I would have gladly lifted you up, you know."
        MC "I know you would. But I'm a man of my word."
        GTS "Of course."
        "One by one I undid the buttons, a much easier task with each one bigger than a teddy bear's eye. Her hot, burgeoning breasts puffed up against my elbows as I did so, as though she were increasing before my eyes."
        "I looked down to see, now that I'd fully exposed her cleavage, they were just slightly overflowing the bounds of her navy blue brassiere."
        show GTS unique
        "I took great pleasure in the view as I shimmied back down to undo the rest of the buttons and then untuck her shirt; for every time I reached down through her waistband, I ran my hands over the supple plains of her hips, eliciting a curt giggle."
    else:
        "But even with gallons of manly adrenaline throbbing in my blood, I continued to mostly just wriggle against Naomi's navel, like a caterpillar ascending the Burj Khalifa."
        GTS "I would gladly lift you up, you know."
        MC "No s'good, m'almost there."
        show GTS aroused
        "With one final burst of strength I started inching up against and then over her chest; every grasp sent a wobbling shockwave through it, forcing me to hold fast for a second or two."
        "At last... at last... I rested my abs atop her, pounced, and got my hands around her top button."
        show GTS surprised with vpunch
        "{i}KRRRCH{/i}"
        "The next thing I knew, I was flat on my back, a giant button perched on my nose, staring up into a pale, pillowy canyon overflowing a navy blue brassiere. Naomi watched over the whole scene, agape and red of cheek."
        MC "...How tight are your {i}clothes{/i} right now?"
        GTS "They have tended to squeeze me a bit these past few days..."
        show GTS wink
        GTS "All the more reason to help me out of them."
        MC "Don't have to tell me twice, {i}sheesh{/i}."
        "I got up on my knees, buttons tumbling off the front of me, and re-mounted Naomi's lap to undo the rest of her shirt."
        show GTS unique
        "When it came time to untuck the hem, I took every opportunity, as I reached into the steaming air beneath her waistband, to scuttle my fingers against her hips; they sunk as into warm pillows."
        "Each time I did, Naomi giggled curtly and gripped the sheets a little tighter."
    MC "Heh, ticklish?"
    GTS "Mm... a little. Excited is more like it."
    "Once I was done, she pulled her arms through the sleeves and tossed the garment to the floor. Then, she leaned back onto her arms, and gave me a coy little smile over the peaks of her wobbling hills."
    show GTS wink
    GTS "Pardon my impatience. You may continue."
    "I nodded up at her, grinning, started circling around behind her, and reached up to unclasp her bra; the hooks put up a fight by virtue of their sheer mass, but in the end, I conquered them too."
    show GTS aroused
    "When the task was done, the garment halfway popped off her chest on its own; she helped it the rest of the way down onto her sheets, where it landed with a quiet, poofy {i}thud{/i}."
    GTS "Ahhh... much better."
    GTS "Now then..."
    "She adjusted herself again, as though she were about to sit in Seiza, but at the last second she splayed her feet out to either side; her resplendent ass sat before me almost as high as my chest, a promise of a full, round, pale moon behind deep blue clouds."
    "All I had to do was part them."
    "Up above, an oversized zipper lapped at the edges of a sea of porcelain skin."
    MC "God, talk about ass for days. You're mesmerizing..."
    show GTS unique
    "I sidled up against her generous backside, and there was a vibration in the air as she was about to say something..."
    "Only to be interrupted when I leaned down and kissed the small of her back; even that was soft as down."
    MC "Were you going to say something?"
    GTS "It's nothing. Please, go on."
    "That was all I needed. I gripped the hem with one hand and the zipper with the other, and tugged."
    "And tugged again. Even for the resistance I was expecting, the waistband was rather..."
    MC "Mph... don't tell me this skirt's a week old, too..."
    show GTS embarrassed
    GTS "Er, no, not quite. Whenever possible these days, I try to buy clothes that are a size or two too large for me."
    MC "Uh huh... God, Naomi-chan, you're getting huge..."
    MC "I mean, uh..."
    show GTS surprised
    GTS "It's alright."
    show GTS aroused
    GTS "It's alright."
    GTS "...I must confess, I like this side of you."
    "As she said it, I finished dragging the zipper down, and I parted her skirt with a {i}click{/i} and a {i}pop{/i}; I tore it away like a magician's tablecloth."
    "And there it was: a perfect, maidenly ass that, in that moment, took up the whole of my vision. A symmetrical pair of dimples, like sake saucers, joined her trim glutes and a thin cushion of smooth baby fat."
    "It was marred only by a pair of blue panties standing in my way."
    show GTS aroused
    "Much more easily, I began pulling her underthings down her hips, alternating one side to the other. The undersides of them were much better visible in the light."
    MCT "\"Excited\" is one way to put it, eh?"
    "With my face brushing down the length of her hips, I finally finagled them down to her knees; she responded to the sensation by lying down and lifting her legs just a little; her breast squished and bulged out to the side."
    "Taking in once more the mind-boggling length and thickness of her legs, I dragged her panties off them and flung the pair aside."
    hide GTS
    $setGTSOutfit(OutfitEnum.NUDE)
    show GTS aroused
    with dissolve
    "And then, like the earth itself moving, Naomi folded her legs and spread them to the sides; with such little effort she corralled my attention directly to her open gate, a peach blossom glistening in the rain."
    "And the next thing I knew, my clothes, too, were good and shed."
    stop music fadeout 10
    "I approached, well and truly awestruck. Her immaculate beauty, the hand-sculpted aesthetic of her every curve... if she'd never had to come to this island, the sight would have stuck in my memory forever."
    "It was all made even more dramatic by Naomi's sheer size. I would never have been able to see this much detail on a normal woman. Even the pulsing heat of her body was overwhelming."
    "And yet, miraculously, all that divine splendor stretched out before me, blown up as great and mighty as a statue in a plaza. I got down on my knees as I came within the emanating heat of her clean-shaven womanhood."
    "Planting a hand on her inner thigh, I felt her twitch and her sharp inhale, and then I leaned down to kiss right next to my hand. I sucked at her a little, foolish though I knew it was to truly take her all in."
    "I released with a {i}pop{/i}, then leaned in to kiss a little further up. I heard the rustle of silken sheets being strangled on the other end of her."
    show GTS unique
    GTS "Oh, Keisuke-kun!..."
    "Grinning, swathed in an aroma like strawberries, I bowed down once more, {w}and plumbed the depths face-first."
    show GTS surprised
    GTS "Ah!"
    "I parted from her after a lingering moment; my cheeks came up slick and my budding sideburns soaked."
    MCT "Knew I shoulda shaved these..."
    "However, I also came to realize my mouth wouldn't quite reach her clit. I had to think."
    "I sat down, scooted up against her crotch and raised my hand."
    "...Glancing at my two outstretched fingers, however, I shortly realized my error. I made a fist instead, and eased it into her."
    GTS "Mmmmhuh... hoh!... H-Heavens!"
    "Like blossoming petals her legs outstretched behind me; I glanced up to see her toes curling, down again to see her pillow-like glutes tensing as, in a meandering canter, I massaged her drenched pussy with my fist and her not-so-little pink rosebud with my open palm."
    show GTS aroused
    GTS "Faster, please...!"
    "I obeyed at once, began putting my back into it; second by second the massage turned into full-steam-ahead pounding, raking my knuckles on the roof of her vag."
    MC "Jesus, you're taking half my arm like it's nothing!"
    "Another earthquake struck as the hillocks of Naomi's ass squirmed and shifted in time with her fluttering gasps and her choked-back yet air-filling moans."
    "Her waters were flowing free now; they sloshed and splashed ever more on my now fully-soaked arms."
    GTS "{size=24}Deeper! I need more!{/size}"
    "Her breathless voice was getting higher-pitched, and louder, each time she spoke. She was bigger than a car and I felt every pound of that raw power going wild."
    "I fought through a rising ache in my arm, barely feeling it, every nerve in my body dedicated to servicing Naomi."
    "I don't know how much time had passed when suddenly I felt my arm being gripped white-knuckle tight."
    GTS "Mmmmm..."
    GTS "{size=24}MmmMmmffff... hah!... hah!...{/size}"
    show GTS surprised with vpunch
    GTS "{size=36}Gah!{/size}"
    if checkSkill("Athletics", ">", 8):
        "I got a split second's warning as her massive hips began to buck in the climactic throes of pleasure."
        "I withdrew my arm and hugged her thigh like a boa snake; for that handful of seconds, the room became a blur, my ponytail whipped one way and then the next twice per second, and I knew in my soul that I was at the mercy of the gods."
        "My head rattled once more as she came to a stop."
        show GTS aroused
        GTS "My... g-goodness..."
        GTS "That was simply divine... Keisuke-kun."
        "With my brain still rotating, like a rotisserie chicken, in its casing, I mumbled something, let go of Naomi's thigh, and flopped limp onto the mattress."
        show GTS surprised
        GTS "Keisuke-kun?"
        pause 0.5
        MC "Holy fuck."
        GTS "A-Are you alright?"
        MC "Mm... better than alright. God, that was amazing."
        show GTS aroused
        "She sighed."
        GTS "Er... truly?"
        MC "I take it you, uh... finished?"
        GTS "Well, I..."
        show GTS pondering
        pause 0.25
        show GTS surprised
        GTS "Ah."
        show GTS aroused
        GTS "...I do believe I did."
    else:
        "I got about a split second of warning as her hips started bucking, "
        play sound Thud
        extend "then her right ass cheek squished into my face and next thing I knew I was on my back a couple meters behind where I'd been."
        show GTS surprised with vpunch
        GTS "K-Keisuke? A-Are you alright?"
        MC "Better than alright, holy fuck."
        show GTS happy
        GTS "Pfhaha! Heavens, I was worried for a moment."
    "I worked my elbows until I was sitting up; Naomi, too, got up and turned around to face me."
    show GTS surprised
    MC "Bwoah!-"
    "...The resulting tremors through the springy mattress once again knocked me on my backside."
    show GTS aroused
    "Pinching her lips, she held still while I tried again."
    MC "See? I'm fine."
    MC "Just like I said... no holding back."
    "I craned my neck up, up, passing nipples as long as my thumbs which punctuated her bulbous tits, catching on her hungry golden eyes."
    GTS "Hmmm..."
    GTS "If that is the case..."
    GTS "Would you please lie down on your back and hold still?"
    MC "Okay."
    "Once I'd done so, she planted her hands on either side of me, and I felt yet more intense tremors as she scooched her hips up and over me."
    "The sensation of my whole body being rocked by ocean waves as Naomi loomed higher and higher above me..."
    "There's no words for it."
    "And then, she scooched up a little bit further, teasing my shaft with overwhelming heat and wetness."
    "Followed by an almost crushing pressure, as she lowered a little more of her bulk down."
    GTS "Hmhmhm... I must confess, it's rather intoxicating the way you look up at me, Keisuke-bō."
    jump GTS049_c3

label GTS049_c2_2:
    GTS "Not at all."
    "She leaned forward again to pick me up, and I had the bizarre but exhilarating sensation of two arms rooting around between my clothes and my abdomen; with those two fingers she made short work of my shirt, pants, and finally underwear."
    "With the final item, a brush of her finger made tangible what she was expecting; she grinned at the prospect just as I was."
    "It only widened as she looked my naked form up and down, like an offering, before setting me down."
    show GTS aroused at Transform(xzoom=-1)
    "Her finger traced down the heart-like contour of her face, down, down, halting at the base of her neck and the topmost button of her cloud-white shirt. She wouldn't be stopped for long."
    "With each button undone, the diamond-shaped gaps between the buttons over her chest widened; as her pillowy, porcelain cleavage came fully into view, they even began to creak under the strain of holding the woman in."
    MC "Daaaamn... don't tell me {i}those{/i} are a week old."
    show GTS neutral
    GTS "Well, not quite. I've since learned to buy a few sizes in advance... as it were."
    MC "And now you're outgrowing them."
    MCT "Fuck {i}me{/i}, man."
    MC "Well, hurry and get that shirt off so you can wear me instead."
    show GTS wink
    GTS "Oh, I don't believe you really want that."
    MC "You... huh?"
    show GTS aroused
    "She leaned forward on her hands and knees, growing suddenly and extremely close. I was just eye level with her chin as her wry golden eyes loomed over me."
    GTS "I think what you really want..."
    "She put a finger to my chest and tapped gently, pushing me back even still."
    GTS "...Is for me to take my own, {w}good, {w}time."
    "I stared up at her, dumb and also mute."
    MC "Y-yeah... you're right. I do."
    show GTS unique
    "She leaned back again, reaching behind her back and expounding with a serene surety on her face."
    GTS "That's good, my Keisuke-bō. A moment like this was meant to be savored, after all."
    GTS "Simply trust me, and I promise you will want for nothing."
    "She capped off her proclamation by giving her voluminous breasts a shake... even that nearly made me stumble... and at last uncovering them."
    "As she stooped to lay her bra aside, her immaculately round teats hung heavy and ripe, just level with my chest. I stood transfixed at their every youthful quiver."
    show GTS aroused
    stop music fadeout 10
    "She caught me from the corner of her eye."
    GTS "Well? Come and smell the roses."
    "I nodded, and stepped forward while she began to unzip her skirt with one hand. I extended my arms in a broken ring and cupped my hands to the sides of them."
    "They were so... inviting. Huge, warm, sloshing, swaying, in a word, heavenly. My hands slid down to meet her palm-sized nipples. It was strange and wonderful, {i}feeling{/i} them harden and grow millimeter by millimeter as I waved them to and fro."
    "And so, after a moment more, I did the only sensible thing."
    scene black with fade
    "I got in touch with my inner ostrich, knelt down and buried my head between them, down to my shoulders and then some."
    MC "Mmmm... Ohmmngggodddd..."
    "I arched my back, sinking in deeper."
    "I felt the vibrations before I heard her voice."
    GTS "Oh, m-my... that feels... positively divine."
    MC "Mmph, tell me about it. I always wanted to bury myself in my girlfriend's jugs, and just... Goddamn..."
    GTS "Hmhm... I'm happy I could make your wish come true."
    MC "You are my fantasy, Naomi-chan."
    GTS "...Would you hold still for a moment?"
    MC "Myeah."
    "Her hand caught my back, pushing my legs out in front of me and jiggering me into a supine position... as I felt her own body lowering down."
    MC "C-careful!"
    "Under any other circumstances I would've relished being pinned under Naomi's bulk, but just then I happened to have highly sensitive, fragile equipment sticking straight up into the air."
    GTS "Of course, Keisuke-bō. I won't let a hair on your head be harmed."
    "She inched down at a teasing pace until her abdomen just kissed the tip, and then slid forward; I groaned once more from the friction and subsequent pressure."
    "As I lay there, powerless to move and swallowed in hot darkness, great tremors shook me to my core, alternating one side to the other from her lower body."
    $setGTSOutfit(OutfitEnum.NUDE)
    pause 0.7
    GTS "I'm ready."
    "Light returned as Naomi sat back up."
    scene Giant Dorm Interior
    show GTS aroused
    with fade
    MC "Oh my {i}God{/i}. {w}You look {i}incredible{/i}."
    GTS "I would say the same of you."
    "She scooched forward a little and settled the increasingly crushing weight of her hot womanhood onto my lap, eyes locked on me all the while. She grinned. My lap grew damp, then wet as she continued."
    GTS "How you look up to me with your flawless, emerald eyes, it's simply enchanting."
    jump GTS049_c3

label GTS049_c3:
    "She laid her finger on my chest and stroked; the curl of her finger, the just-palpable tremor in it told how much she was fighting herself to not just grab me and squeeze."
    show GTS aroused at Transform(xzoom=-1)
    GTS "If I may speak my truth..."
    GTS "Unsightly as this condition may be, I really have come to love how easily I can just pick you up and hold you close..."
    GTS "And do {i}whatever{/i} I please with you. {w}Because you're mine."
    "My eyes went wide. For a minute I couldn't tell if I was getting feverish or if she really just said that."
    GTS "And as delightful as all of this has been, Keisuke-bō, I believe I'll have you inside me the old-fashioned way."
    MC "{i}Yes ma'am{/i}."
    show GTS wink at Transform(xzoom=1)
    "Then, with nothing more than a wolfish smile, she tucked two fingers under my legs, giving my bare ass one more avaricious squeeze, and then pulled me inexorably into her."
    "For just that moment she was like a demon, her strength unearthly and her desire overpowering."
    hide GTS
    show GTS_S unique
    GTS_S "HAAAaaahnke-Keisuke!"
    "I couldn't answer. As she started working my body up and down I realized her pussy long ago grew too vast to be filled by my dick."
    "It didn't matter. Naomi's huge, powerful hand had me sandwiched against a wall of flesh as warm and womanly as it was indomitable."
    "I heard, hell, {i}felt{/i} her heartbeat rising. She knew just what she wanted out of me. She directed my cock to grind right on the magic spot, while my tensed lower abs slapped against her cherry-sized clit."
    GTS_S "{size=24}Ah!... Ah!!...HmmmmmMMM...{/size}"
    "She stroked faster and faster; the drumbeat of tits as big as beanbag chairs patting against her abdomen joined in the chorus, mere centimeters from my head."
    "Never in my life did I ever think that the heartbeat of another woman would send physical pulses through my body. Even Naomi's involuntary movements thrummed with awesome power and strength."
    "Insensate, I kissed and rubbed on her supple midsection; it was like layers and layers of fine velvet wrapped around an oak tree. Everything I'd kept pent up for the last few minutes was flooding straight into my shaft, moments from bursting."
    "My gargantuan goddess girlfriend was so rapt with ecstasy as she fucked me, I couldn't help but absorb some of her radiance."
    "Down below, she squeezed tighter, completely engulfing my lower body in iron-soft thigh thickness. The countdown had begun."
    "I stretched my arms out to rub on her ass, couldn't reach, settled for her hips. Every second Naomi was growing tighter, louder, wilder."
    "Then... there was stillness."
    "While my body was captive to hers, my thoughts wandered."
    "And all I could think of was how incredible she was. Naomi was in my head, in my heart, and as I stared into a pale, sweaty wall of her, I wanted nothing but more, and more, and more of her {w}until she was my whole world..."
    "More!"
    "More!"
    MC "N-Naomi-chan!"
    GTS_S "{size=36}G-GAH!{/size}"
    show GTS_S surprised with vpunch
    "My ears rang, her pussy squeezed and gushed, spraying just up to my chest in a couple of spurts."
    "A few seconds later, I realized from the waning, involuntary pumping of my hips that I'd joined her. I sighed, and kept on breathing from my navel for a few more moments."
    show GTS_S aroused
    "The lightning in my brain began to thin to a hanging mist of purest delight as my body went limp piece by piece."
    pause 0.5
    "Naomi, overhead, breathed deep, and uttered a tremulous sigh."
    pause 0.25
    "Just before my hair began to tilt."
    MC "Huh... woah!"
    "With no further warning, she collapsed backwards onto the bed with her eyes closed, sending a cooling gust whipping past my head on either side."
    GTS "Mmm... {w}I love you so..."
    MC "I love you too..."
    "Naomi held me a little tighter against her crotch."
    show GTS_S surprised
    pause 0.5
    hide GTS_S
    show GTS embarrassed
    "Then, she pulled me loose and scooted me forward to nestle between her breasts."
    $setAffection("GTS", 10)
    play music LoveA fadein 1.0
    GTS "Apologies, Keisuke-kun. You've gotten a bit, er, dirty."
    "I raised one hand and brought it down with feeling on her chest; she didn't flinch, though the resulting jiggle promptly shook my arm off."
    MC "Naomi-chan, only you could lose your V card and then apologize immediately after."
    show GTS pondering
    GTS "V card?..."
    pause 0.25
    show GTS embarrassed
    GTS "Ah, my..."
    "She scrunched up a little and looked away."
    MC "Heh, yeah."
    pause 0.5
    MC "Oh. {w}My. {w}God."
    show GTS surprised
    GTS "What is it?"
    MC "How could I not see the signs, it all adds up!"
    show GTS pondering
    GTS "What does? What do you mean?"
    MC "{i}You have an apology fetish.{/i}"
    show GTS unique
    GTS "What?"
    MC "All those times you said sorry were just you getting your rocks off, weren't you? Why else would you say it so much?"
    GTS "What on {i}Earth{/i} are you talking about?"
    MC "You sick, considerate pervert."
    "Her chest shuddered and so did I with her chirping giggle,{w} which faded away into a countenance wrought with worry as she tried to hide behind her hand."
    show GTS sad
    GTS "...Please... don't tell my family. My mother would be dreadfully disappointed."
    MC "...Don't... wait... w-what?"
    show GTS wink
    if getFlag("GTS044_meet"):
        GTS "For shame, Hotsure no kimi. It takes two to tango, you know."
    else:
        GTS "For shame, Keisuke-kun. It takes two to tango, you know."
    MC "Pfff, ya got me."
    show GTS unique
    GTS "Ahaha!"
    MC "I guess now we know what you really like, anyway. Maybe being big has its perks, doesn't it?"
    show GTS embarrassed
    pause 0.5
    show GTS neutral
    GTS "I suppose it rather does."
    show GTS aroused
    extend " Please don't tell my family."
    MC "Your secret's safe with me."
    show GTS happy
    "I started scooting up towards her face, when she put her hands around my sides and pulled me up. She inclined her cheek to me when she saw where I was reaching, and I kissed her long and deep, held close in her embrace."
    "I could've slept forever there, in that world of enveloping warmth and easy breathing and faraway, pattering rain."
    play sound Thunder
    show GTS neutral
    GTS "Well, I suppose we ought to clean up a bit before we go to bed."
    show GTS aroused
    GTS "...We can have a shower together, if you like."
    MC "\"Like\", Naomi-chan, is the understatement of the week."
    show GTS wink
    GTS "As I suspected."
    "She held me close and began shimmying to the edge of the bed."
    stop music
    scene black
    GTS_S "Oh!"
    "With a loud, dull click the entire room was cast into abject blackness and Naomi squeezed me tight to her chest, popping a couple of my joints."
    GTS_S "Are you alright?"
    MC "Mph... yeah, I'm fine. The power go out?"
    GTS_S "It seems so. It must've been the storm."
    MC "Huh."
    MC "So... I don't suppose we could still have that shower?"
    pause 0.5
    GTS_S "I do not believe that would be safe to do in the dark."
    MC "Hm... yeah, true."
    MCT "Dammit. Divine wind, my ass."
    GTS_S "We'll just have to settle for toweling off. Just as well, I will need to do my laundry anyway."
    "She gently slid me off her torso and onto the mattress, which I heard creak alongside the characteristic breeze from Naomi standing up."
    "After a moment alone with the clamor of the rain, she held me around my waist and slid me over the mattress."
    MC "My legs still work, you know."
    GTS_S "Of course. I just wanted to make sure you didn't fall off the edge."
    GTS_S "I'm going to retrieve some candles and matches from my closet. Would you please light them? I'll set them on the nightstand next to you."
    "I reached out and felt a wooden pole almost as thick as my torso."
    MC "Yeah, of course."
    GTS_S "Please be very careful... {w}and, thank you."
    "The thuds of her footsteps got a little quieter, then stopped before I heard hinges squeaking in the dark. Next came slow, hesitant rustling, metal tinkling, wood rattling."
    "Another squeak, and the footsteps quickly fell back upon me. A pause, then a pile of tinkling, rattling objects settled on a tabletop a meter or so to my right."
    GTS_S "I'll be back in a moment. I am going to dry off, and then I'll bring you a washcloth."
    MC "Thanks, Naomi-chan."
    "She walked away again; I carefully stood up, on all fours at first, then I planted a hand on the nightstand as I rose to full height."
    "Turning around, I felt in the dark for the candles, which I arranged in a rough circle, and at last retrieved a match."
    "The third strike did the trick."
    "One by one the candles sprouted sputtering, pale orange flames. Looking around, I saw the still waves and crests of Naomi's sheets only just illuminated in a wan but golden glow, though the edges of the room were still largely invisible."
    "I realized I could still smell strawberries, with but a hint of salt. I breathed a sigh."
    "The candles, as I looked at them closer, had a distinctive taper, a faint, homespun roughness, and they sat on antique iron stands."
    "Again, footsteps both resounding and gentle, padding across the floor."
    play music LoveA fadein 1.0
    show GTS neutral with dissolve
    "I turned just in time to see Naomi's impeccable nakedness enter the candlelight. Her expression as she looked over at me, painted in pale yellow crescents and ovals, was perfectly befitting of it."
    MC "I can do it myself, if you want. I don't want you dirtying your hands all over again."
    GTS "It is well, my love. I am happy to do it."
    "She inched herself down onto the mattress, and once I walked over to her she braced my back with one hand and began to wipe down my abs and lower body."
    GTS "Heavens, I never imagined the whole affair would make such a mess."
    GTS "But... it goes to show what preconceived notions are worth."
    MC "I 'spose it does."
    MC "By the way... some fancy candles you got there. Are they homemade?"
    show GTS happy
    GTS "Why, thank you. And indeed they are. My grandmother taught me how to make them."
    GTS "She always kept such a lovely house and garden. She taught me much of what I know about homemaking."
    show GTS neutral
    GTS "It's a pity that my candlemaking days are quite past, but so things go."
    MC "Mm, yeah, I guess so."
    GTS "Mm... {w}There you are. Did I miss anything?"
    MC "Don't think so. I feel good and dry."
    show GTS unique
    GTS "Very good."
    hide GTS with dissolve
    "She walked away again in the direction of the bathroom, and I heard a faint rustle of cloth."
    show GTS unique with dissolve
    "When she returned, she promptly tucked me under her arm and tucked herself under the blanket... after straightening the pillows."
    "Half my face rubbed across her bare breasts as she positioned me between them and laid the hem of the blanket on my chest. I was really starting to realize Naomi could be a bit of a card herself."
    show GTS neutral
    GTS "Are you comfortable?"
    MC "I'm in heaven."
    show GTS happy
    GTS "Hmhmhm, that makes two of us."
    show GTS neutral
    GTS "Ah, but please do nudge me if you need anything."
    MC "Will do."
    "A warm breeze blew past me as she sighed."
    pause 0.75
    MC "...Will a nudge from me actually wake you up?"
    show GTS pondering
    pause 1
    show GTS neutral
    GTS "Erm, perhaps you should just shout something."
    MC "Okay."
    "I reached down and rubbed her side."
    MC "Good night, Naomi-chan."
    GTS "Sleep well, dearest."
    hide GTS with dissolve
    "I took in one more spent, joyous groan from her as I shut my eyes."
    "Maybe dreams really do come true."
    jump daymenu

label GTS050:
    $setProgress("GTS", "GTS051")
    $setSize(4)
    $setTimeFlag("size4")
    "I was shaken from the best sleep I'd had in years... {w}by the return of one of the most pernicious storms I'd ever seen..."
    "The wind had come back with a bloody vengeance, pounding on the black walls alongside thunder that rattled my innards."
    "If that wasn't enough, each boom was preceded by a flash of searing, ghostly white from the high windows; closing my eyes only showed me red light instead."
    if getFlag("GTS049_embrace"):
        $setGTSOutfit(OutfitEnum.NUDE)
        MCT "Urgh... I'm grateful for what you did earlier, but now I just wanna sleep..."
    else:
        MCT "Urgh... I just wanna sleep, go away already..."
        MCT "Hope Naomi's at least getting some decent shut eye..."
    "Grunting and prodding my own sluggish muscles, I rolled over onto my side and peered back toward her serene, slumbering face."
    "There was no such thing."
    "What little detail I could make out in the deep darkness planted a swelling cold in my belly... her brow knitted and unknitted, her frown weakly gasping."
    MCT "Is she having a bad dream?"
    MCT "Does she have bad dreams often?"
    MCT "She looks so scared..."
    MCT "What's she dreaming about? Her family? The storm?{w} Me?"
    "Then she jumped and drowned everything in her bloodcurdling scream."
    GTS "{size=24}{i}Help me!{/i}{/size}"
    "The only reason I wasn't struck deaf was that her spasm had thrown me under the blanket, tucked me down by her ribs. I scrambled back up as best I could on her bucking torso."
    GTS "{size=24}K-Keisuke-kun? Where-w-where are you?{/size}"
    MC "I'm here, I'm here! What's wrong!?"
    "She almost sighed... but the sound was wet and shaky as it left her, like a stray in the autumn night rain."
    GTS "Keisuke-kun..."
    "Another sigh that became the faintest whimper; I could hear her choking back tears."
    GTS "Mmng... you're... here... Th-thank heavens..."
    MC "I'm here, Naomi, I'm here. You're gonna be alright, don't worry."
    GTS "Thank you..."
    "When she breathed out, I took the opportunity to climb back up onto her chest."
    MC "What happened, Naomi-chan? You sound like you saw a ghost."
    GTS "It... it was... ngh..."
    "She took a few deep breaths as I rubbed my hand in circles on her ribs."
    pause 0.75
    GTS "I... I think I would like a cup of tea. W-would you... like me to pour a cup for you, Keisuke-kun?"
    MC "Um... sure."
    "Naomi folded the blankets off of her legs and I heard a cacophony of rustling from her rising out of bed. Then, she trod with slow, quiet steps to the bedroom door and flipped on the kitchen light on the other side."
    MCT "..."
    MCT "Something's up..."
    MCT "What could shake her that bad?"
    play sound Thunder
    "Indeed, her shadow in the doorframe lingered right where it was for a moment or two more, hand clinging to the lightswitch."
    "Whatever the disturbance was, she kept on walking into the kitchen. The cabinet, roused from nocturnal slumber, groaned open, and then came the bassy {i}clunk{/i} of Naomi setting her tea making kit down on the counter. I could hear it rattling."
    "Another {i}clunk{/i} from her setting down her tea 'cup'."
    pause 0.75
    "Silence blew in from the other room in the few moments after that; I began crawling towards the edge of the bed by the light pouring in from the doorway."
    "Just at the edge, I jolted at the crash of something small and ceramic shattering on the ground."
    GTS "{size=24}Aggh, God damn it!{/size}"
    MC "Naomi-chan, are you okay?"
    "A choked whimper was my only reply."
    MC "I'm coming out!"
    "I slid my legs down the edge of the mattress and began crossing the piebald concrete until I stood full in the light through the door."
    scene Giant Dorm Interior with fade
    "I winced and squinted as my eyes took a few seconds to adjust to the light."
    play sound Thunder
    "I needed a moment more to process what I saw there."
    "Naomi stood there under the cold light, her face cupped and hidden in her hands, her trim stomach writhing under burdensome, trembling breaths, and her black hair hung low."
    "I came closer."
    show GTS_S surprised with dissolve
    "The next thing I came to realize was that Naomi had grown. {w}Substantially."
    if getFlag("GTS049_embrace"):
        "I looked her up and down, almost without conscious thought. The first thing I met with was the realization that my view had shifted dramatically downward as I looked straight into her huge, pale knees."
        "Farther up, and I saw that the countertop now stopped at her upper thighs rather than her trim crotch. Hardly thinking, I let my jaw drop."
        "Every meter of her perfect, bare body had swelled with still greater mass, beauty and power."
        "The modest tush I once knew was now a voluptuous ass that jutted out into the pale light."
        "My eyes kept climbing up her; her teats had likewise grown noticeably beyond her original proportions, plumper, rounder, hanging lower and bulging out farther."
        "They squished between her upheld arms, a truly insufficient cage for her new, burgeoning proportions."
        "But her arms... down them each ran a single glassy rivulet, beyond the black veil of her hair. She wouldn't look at me."
    else:
        "My eye was immediately drawn to the way the slightly-taut outfit she was wearing last night now looked several sizes too small on her."
        "Her proud, round breasts had exploded out of her suddenly-unbuttoned shirt, now draped over them like curtains in a mansion foyer, accented by her hanging bra straps. The ensemble didn't even reach her navel."
        "I looked down a little further to see that the now-pronounced swell of her hips, too, had burst the confines of her skirt and had turned them into what was functionally a pleated blue loincloth."
        "Looking ahead I saw the puddle and shattered remains of something."
    GTS_S "I broke your teacup."
    MC "...Don't worry about it, okay?"
    GTS_S "Apologies, I'll prepare another cup."
    "On the occasion she allowed me to see her tortured face, I saw her hair which was normally so well kept was disheveled, with loose strands falling across her face."
    "I took a seat on the table as she set a cup of tea in front of me. She had tried to fix her frazzled hair, but her expression of concern and worry remained."
    show GTS_S sad
    GTS_S "I pray it's not too hot, I pulled it off a little early to try and keep it cool enough to drink."
    MC "It's fine. Thanks."
    "She took a seat and sipped her tea but her expression remained unchanged."
    MC "Do you want to talk?"
    GTS_S "I'm..."
    GTS_S "I'm not sure how to."
    MC "What startled you in bed?"
    GTS_S "It was a nightmare, a ghastly one."
    MC "Well... well, how did it start? What was the first thing you saw?"
    GTS_S "At first, I thought it was just a memory. I was back home... walking with Kazumi on the way we always took to fetch groceries."
    menu:
        "...You and your sister did that? Why not your mom?":
            GTS_S "Mother had to attend to affairs of the home. Moreover, it was one way for us to learn responsibility."
            MC "I see, okay. Um, sorry to interrupt."
            $setAffection("GTS", 1)
            GTS_S "No, no, it's fine. Thinking about that sort of thing helps to... ground me."
            "She wrung her fist over her breast as she breathed in; I could hear her throat shudder as she breathed out."
            GTS_S "Erm... where was I, then..."
            MC "You were in the shopping district, right?"
        "(Say nothing)":
            "She paused, her eyes rolling over to dig up fading memories."
    GTS_S "Ah... y-yes. We were walking along, and I think I caught myself growing taller. It was subtle at first, like only a head taller than my sister and then most people."
    GTS_S "...But then, it came... faster and faster, and soon I could see over the two story buildings."
    "She paused and sipped her tea."
    $ persistent.unlock_cgGTS050_nightmare1 = True
    show cg GTS050_nightmare1 with dissolve
    GTS_S "For a few moments I was just frozen, and then I started growing again. Even though I couldn't see their eyes, I could tell everyone was watching me. I tried to shout... for help, to tell them to run, but I couldn't even utter a whisper."
    GTS_S "Soon I was as tall as those office buildings in the city, yet it just wouldn't... wouldn't stop. I tried to run away, but I had grown so much that... every step, I destroyed houses, shops... schools. There was nowhere I could go."
    GTS_S "I tripped on something, eventually... I couldn't tell what I was going to land on. There were so many... {w} That's when I awoke."
    hide cg with dissolve
    "I could see the tears welling up in her eyes moments before she collapsed onto the table."
    "I stepped forward to pat her head as a realization struck me. At her size, what do gestures like that really mean, coming from someone like me?"
    "I want to wrap her up in a hug and hold her close... but I can't.."
    MCT "Can the best I can muster really only be head pats and caresses?"
    GTS_S "Keisuke... do I ever scare you?"
    MC "What? Of course not, you are the kindest person I know."
    GTS_S "That's not what I mean. Am I physically scary? Like intimidating?"
    MC "I..uh..I wouldn't say that. You are still you and people are gonna worry more about how you act with them."
    GTS_S "I'd like to believe that, but... those faces. Those faces I saw in that horrible dream had nothing but fear and terror on them. Like I was a... a... monster."
    "She bit her lips at that last word, and she wept anew. Once again the best I could try to do was pat her head."
    MC "The last thing you are is a monster. You are still the Naomi people know you as and nothing's gonna change that."
    pause 0.5
    GTS_S "Thank you Keisuke, but I don't think you quite understand what I mean."
    "She slowly stood up, allowing herself to loom over me."
    "I guess I had gotten so used to my perspective that I had stopped considering just how much taller Naomi had become."
    "In the dim lighting and deep darkness of the night she did look rather imposing. The occasional flashes of lightning backlighting her only added fuel to the fire."
    MC "I... uh...I can sorta see what you mean better."
    "She gently sat back down and buried her head in her hands."
    GTS_S "...Will I live the rest of my life like this?"
    "I felt an urge to reach out and give her my hand but something kept me from reaching her. There was the literal distance between us, but some other force wouldn't let me bring my arm up to her."
    MC "Is this the first time this has happened?"
    hide GTS_S
    hide GTS
    show GTS pondering at Position(ycenter=0.35)
    GTS "No, I had a similar dream my first night here. It wasn't as dramatic but still scared me terribly."
    MC "What scared you so bad about it?"
    GTS "I initially thought it was the feeling of being so tall, but after this I think it's something deeper."
    MC "Like growing apart from people?"
    GTS "I had not really considered that, but maybe a little."
    hide GTS
    show GTS_S neutral-2
    GTS_S "Keisuke, have you thought about when your growth will end?"
    MC "It was something I pondered when we were first diagnosed, but I think I got used to it after a while that it would continue its slow creeping growth."
    MC "I guess I just started hoping it would stop one day and I'd notice it eventually. Is that what is scaring you?"
    show GTS_S sad
    GTS_S "The growths are slow, which makes it quite anxiety inducing. You don't know when it will finally stop."
    show GTS_S neutral
    "She stood up from the bed and slowly closed the bedroom door revealing several chalk marks on the wall. Each mark had a date on it showing a continuous steady daily growth."
    GTS_S "I guess I'm more scared of when it may decide to cease... or if it doesn't cease."
    GTS_S "Being taller than the average door was never something I could have imagined. Especially when I was often the shortest person in the room for most of my life."
    show GTS_S neutral at Transform(xzoom=-1)
    GTS_S "Of course now, I'm far taller than most of the other students living here in the quarry. I observed the wall of fame in the caverns and I am above many of the previous students already."
    MC "Are you the tallest now?"
    GTS_S "No, Akio is still taller than me.Though the margin has continued to shrink day by day."
    MC "I think the margin may have shrunk again."
    if getFlag("GTS049_embrace"):
        show GTS_S surprised
        GTS_S "Wh-what do you mean?"
        MC "Ah... Look around you."
        show GTS_S surprised at Transform(xzoom=1)
        "She turned her head hither and thither as though pulled by chains; soon enough, comprehension dawned."
        show GTS_S sad
        GTS "I don't have any more clothes..."
    else:
        "Naomi looked blankly at me before looking down at her clothing. Registering for the first time the damage to her clothing. A single tear rolling down her cheek and splashing into her tea."
    show GTS_S sad
    GTS_S "And they fit me so well just yesterday."
    "A silence filled the room, neither one of us daring to make a move on our tea as wispy steam curled from the cups."
    "The sounds of the storm outside gradually faded away, while the silence between us remained. The steam from the tea had faded as well, both cups sitting cold and untouched."
    MC "The worst of the storm seems to have passed us now. I think I may go back to my dorm if that's the case."
    show GTS_S surprised
    GTS_S "Oh? Are you sure that it's safe to go out there?"
    MC "It's probably just muddy right now. I haven't heard any thunder in the past several minutes, so it should be clear."
    show GTS_S neutral
    GTS_S "Alright, just be careful please."
    MC "I'll make sure to do so just for you."
    "She gave me a weak smile for a moment before her face returned to one of worry."
    "Climbing down from the table and grabbing my amenities, I headed out and towards the dorms."
    MCT "All that growth in one night, that can't feel normal or remotely sane."
    "I absentmindedly stroked my own hair as though to remind myself that what we were all experiencing was nothing near normal."
    MCT "I do hope for her sake that this slows cause I'm not sure how much more she can endure."
    "Staring up at the sky I spotted the full moon peek out for a moment. It's bright white light illuminating the ground for a moment, before slowly being snuffed out by more dark storm clouds."
    "As I approached the school another round of thundering could be heard in the distance, as I tried not to think of what it meant."
    jump daymenu

label GTS051:
    $setProgress("GTS", "GTS052")
    scene Giant Dorm Interior with fade
    play music Peaceful
    "It was a surprise for sure, but a welcome one when Tashi dismissed us early with the optimistic idea that we would be working on our report."
    "Oh, that poor fool. His optimism would be tragically misplaced when procrastination was an option. Especially procrastination shaped like a tall elegant lady."
    show GTS neutral at Position(ycenter=0.55) with dissolve
    GTS "My love, is everything alright?"
    MC "Oh, uh, yeah I'm fine. Just got lost in thought for a moment."
    GTS "Ah, I see. Apologies for interrupting."
    MC "It's cool, I was just thinking about what I was gonna do for the rest of the day. Tashi let us out to work on our report but it's not due for several more days."
    GTS "The sooner you start, the sooner it is completed. And then you have time to work on other passions."
    show GTS happy-2 at Position(ycenter=0.35)
    GTS "And with longer assignments, it leaves more time to catch mistakes and make revisions."
    menu:
        "I never bothered with revisions, I normally catch my mistakes as I'm writing.":
            jump GTS051_c1_1
        "Being thorough is never a bad thing.":
            jump GTS051_c1_2

label GTS051_c1_1:
    $setFlag("GTS051_c1_1")
    show GTS surprised
    GTS "Your confidence in your writing ability is admirable, but are you sure that's best?"
    MC "I've found that my first thoughts normally pan out better than me second guessing myself."
    GTS "Didn't you mention that on your last paper that you got marked off a lot for grammar?"
    MC "A few times, but only some small details."
    show GTS unique at Position(ycenter=0.55)
    GTS "I can help you with the grammar if you want. The linguistic arts {i}are{/i} one of my stronger subjects."
    MC "{i}*sigh*{/i}"
    MC "I may take you up on that for this report. My last one didn't go so well, though that may have been because I wasn't too familiar with the Renaissance stuff."
    show GTS neutral 
    GTS "I'm no expert on the subject, but if you would like some company while studying I'm more than happy to accompany you."
    jump GTS051_afterc1

label GTS051_c1_2:
    $setFlag("GTS051_c1_2")
    GTS "A second pair of eyes can sometimes catch what you overlook."
    MC "I could be a second pair of eyes for your stuff."
    GTS "I would appreciate that."
    jump GTS051_afterc1

label GTS051_afterc1:
    MC "Is there anything you wanted to do today since we have some time?"
    GTS "Nothing particularly, though I wanted to adjust the plants outside as well as water them."
    MC "Not sure how well I can help with that, but I'll sit by and watch."
    GTS "That's fine Kei, it's nice just to have you around."
    scene Giant Dorm Exterior
    show GTS neutral at Position(ycenter=0.55)
    with fade
    "We stepped outside and I found myself a comfy spot to sit beside the building."
    "Scanning the rocky, barren horizon, I began to grow curious."
    MC "How many people do you think live here?"
    GTS "I haven't done a proper count but over a dozen, at least I think. It's a rather small group."
    MC "Are you the most recent one to move in?"
    GTS "I think so, but they say that it's not uncommon for more people to move in as the semester goes on."
    MC "I mean there are certainly some students that are nearing the ceiling I've noticed but none I can see moving here immediately."
    GTS "I think the quarry has room for 30 people, so we have capacity to add more."
    stop music fadeout 2.0
    show GTS pondering at Position(ycenter=0.35)
    "As we sat and chatted I could hear someone singing; looking around I could spot a figure walking down the road lugging a box with them."
    UNKNOWN "She caught the Katy, and left me a mule to ride. The train pulled out, I swung on behind. Crazy 'bout that hard headed woman of mine..."
    MC "Guess I spoke too soon."
    show GTS neutral at Position(ycenter=0.55)
    GTS "Her singing voice is pleasant."
    play music Busy
    show Jineko neutral at Position(xcenter=0.85, yalign=1.0) with dissolve
    "The woman was built for how thin she was, and not just vertically. Dressed like she'd walked fresh out of the mines, she was hauling some sort of box while her feet kicked up what was to me a prodigious dust cloud." 
    UNKNOWN "Afternoon folks, any idea where I can find dorm 18?"
    GTS "Oh, it's next door."
    "Naomi gestured to the buildings directly beside us."
    UNKNOWN "Good, this box was getting heavy."
    if getFlag("Meet_Jineko"):
        UNKNOWN "Wait, didn't I meet you at the festival?"
        MC "You were that girl Daichi was looking for, Jineko right?"
        Jineko "The one and only."
        "She set her box of stuff down and did a little stretch."
        MC "Well you already know me. This is Naomi Yamazaki."
    else:
        $setFlag("Meet_Jineko")
        Jineko "Well, I'm Jineko Watanabe, pleasure to be your neighbor."
        "She set her box down and did a little stretching."
        MC "I'm Keisuke Hotsure and this is Naomi Yamazaki."
    show GTS happy 
    GTS "Oh the pleasure is mine, it's nice to have a new face here."
    Jineko "I take it that things move a little slowly down here."
    GTS "They can, but a meditative pace is not the burden it may seem at first."
    Jineko "Well, for my money, slow equals boring. I like some action in my life... Well, unless it's hauling something, but that's a whole other set of circumstances."
    MCT "I hope she heard herself when she said that."
    show GTS neutral 
    GTS "...Well, everyone has their own pace in life." 
    Jineko "Say, those are some fine plants you have there. Some real treats for the eyes."
    GTS "Oh, thank you. I put a lot of time and effort into making them look their best."
    Jineko "Have you considered getting yourself a small shelf so you don't need to lean down to water them?"
    GTS "I would like one, but I doubt they make them tall enough."
    Jineko "I could slap one together for you if you'd like."
    GTS "That would be most kind, and I would gladly compensate for your labor."
    Jineko "Don't sweat it, I love doing handy work in my spare time." 
    MC "That could be handy around here."
    Jineko "Why do you say that?"
    MC "The quarry seems like a place ripe with things that could use some extra hands."
    Jineko "I suppose that's a pretty good assessment, and that's something I can hopefully help with."
    GTS "I don't suppose you would happen to know how to fix a minor pipe leak?"
    Jineko "Matter of fact I do, you asking for a friend?"
    GTS "No, I was just curious. I have one with my sink and wasn't sure how to fix it myself."
    Jineko "I'd be happy to look at it once I'm settled in."
    show GTS happy
    GTS "Thank you very much."
    show GTS neutral 
    GTS "Er... If you don't mind me asking, is that a binder clip holding your bun up?"
    Jineko "Oh that thing? Yeah I found it easier to locate a binder clip than a scrunchy so I just began using it daily."
    GTS "That's... certainly resourceful."
    Jineko "I hate to let stuff go to waste. Speaking of which, do you know where the storage vault is?"
    show GTS pondering at Position(ycenter=0.35)
    GTS "Storage vault?"
    Jineko "Yeah, one of the school admins mentioned it was down here somewhere. I need to grab some wood and metal from there at some point."
    show GTS neutral at Position(ycenter=0.55)
    GTS "I can't recall seeing anything resembling a vault either out here or in the caverns."
    Jineko "It's fine, I take it the government put it down here to keep it out of sight. Probably around a hidden bend or something."
    MC "Did they give you a key or combo for it even if you found it?"
    Jineko "They gave me a key. Hm, let me see here..."
    "She reached into her pocket and pulled out a long chain that had a pair of keys attached to the end. The chain and keys looked a little bigger than my fingers, but in her hand they looked quite small."
    Jineko "I'm gonna need to make another copy of this one. They said there used to be a bigger version available but it disappeared some time ago."
    MC "I'm not sure how you lose track of something that big."
    Jineko "I guess I'll find out. I feel like I'm the unofficial queen of misplacing things."
    if checkAffection("BE", "<", 4):
        MCT "I feel like Honoka might dispute that."
    MC "I mean, I'm no clean freak myself, but I wonder why you say that?"
    Jineko "Oh, when I'm building models I always seem to lose a little piece for a few days before it reappears. Thankfully I've gotten better, but it still happens."
    GTS "You do modeling work?"
    Jineko "Oh I love it. I've got the steady hands to make it work. I'm {i}mean{/i} with a pair of tweezers."
    show GTS happy
    GTS "It shows. Your eyebrows are immaculate."
    Jineko "Certainly helps. And thanks for noticing, I was beginning to wonder how they came out."
    GTS "If it's no trouble, perhaps you could help with mine? I normally used an arching tool but I... misplaced mine, unfortunately."
    Jineko "No problem girl, I can get those things looking sharp in no time."
    MCT "Can't say I ever expected to hear this conversation."
    "She seemed to stifle a grin as she looked over at Naomi, then down at me."
    Jineko "Now I gotta ask, are you two a thing?"
    MC "Is it that obvious?"
    Jineko "I mean {i}something's{/i} gotta be going on for anyone besides a giant to be down here."
    "She kneeled down beside me and attempted to whisper."
    Jineko "Nice catch, little guy."
    show GTS pondering at Position(ycenter=0.35)
    #(if possible a wink expression for Jineko in the future)
    MCT "Not sure how to feel about being called that."
    Jineko "Well, better get my stuff settled in cause I'd like to get to that vault before night time."
    hide Jineko with dissolve
    "She picked up her box of stuff and entered the adjacent building."
    MC "She is certainly a character."
    show GTS neutral at Position(ycenter=0.55)
    GTS "She certainly is, but that's not a bad thing. Aren't a person's quirks the essence of their character?"
    MC "Fair, fair. Did you notice that patch on her blazer?"
    GTS "No, I must have overlooked it."
    MC "That was the same design as the student council armband, wasn't it? Like Matsumoto-san wears..."
    GTS "That's interesting indeed. I wonder if she's meant to be the representative for this area? I don't recall us having one at the current moment."
    MC "Wonder how she interacts with them at school."
    GTS "Good question... perhaps she speaks through the window."
    MC "Guess that may be something to ask one of the other representatives if I remember."
    stop music fadeout 2.0
    GTS "By the way, what did you make of the way she addressed you a moment ago?"
    MC "You mean the 'little guy' comment?"
    GTS "Yes... that."
    play music Sunset
    menu:
        "Honestly didn't care for it.":
            jump GTS051_c2_1
        "Not to jump to conclusions, but a little suspicious":
            jump GTS051_c2_2

label GTS051_c2_1:
    "The usual hardness of her lips that came from her observing rudeness... didn't come so easy this time."
    GTS "I should think not. How very familiar to act on a first meeting..."
    MC "Yeah... She seems very sure of herself. I'll give her that. She's probably taking this whole thing instride a little {i}too{/i} well.."
    GTS "That's rather astute. I'm inclined to agree with you."
    jump GTS051_afterc2

label GTS051_c2_2:
    GTS "Oh? Do you mean to say you sense some surreptitiousness?"
    MC "The wording sounds just a little bit like headgames, doesn't it?"
    GTS "I cannot dispute that. My, my..."
    MC "Well... maybe she's just awkward. We just met her."
    GTS "Hm... yes, that's rather a more pleasant outlook. I look forward to becoming better acquainted."
    $setAffection("GTS", 1)
    jump GTS051_afterc2

label GTS051_afterc2:
    MC "She'll certainly be someone to keep an eye out for."
    show GTS wink
    GTS "I get the feeling she will make her presence known whether we ask her to or not."
    MC "...Hey, by the way, you said you lost your arching tool? You could've told me, I can help you find it."
    show GTS happy
    GTS "Thank you, Keisuke-kun. However, I'm afraid that's not quite the whole story."
    MCT "...I think I know how it ends, though."
    MC "What happened to it?"
    show GTS neutral
    GTS "I did momentarily lose it, rather, I dropped it while using it..."
    GTS "But as I stepped away to try and find it, I... well..."
    MC "Oh."
    MC "Bummer."
    GTS "Bummer indeed."
    "Despite myself, laughter crackled out of my closed mouth; Naomi crossed her arms and made a show of thumbing her nose at me."
    GTS "Whatever is so funny, Keisuke-kun?"
    MC "Just... you... kmphhh..."
    show GTS happy
    "This time, she joined me in cracking up a little. Even as her voice drowned the air more and more as she grew, her sweet, chirping laughter was still there, pure as ever."
    MC "Guess that's what you'd call irony."
    GTS "I... suppose so."
    "Maybe involuntarily, her hand slid up her abdomen, easing it until it was still. I could actually hear her breath slowing as her face reclined back into understated contentment."
    MC "I'm serious though... if you ever lose something again and you can't find it, gimme a call and I'm there."
    "She nodded once, and pondered for a moment."
    GTS "Thank you. I shall certainly bear that in mind."
    jump daymenu

label GTS052:
    $setProgress("GTS", "GTS053")
    scene Mountains with fade
    play music GTSAlt fadein 2.0
    show GTS_S neutral with dissolve 
    MC "A hike?"
    show GTS_S unique 
    "Naomi chuckled, jostling me a little despite how she muffled it."
    GTS "You say it as if it's so bizarre!"
    GTS "Just look at the world around us!"
    "Naomi shifted her arm to make me face to her right, so as to put on display a grand panorama of the mountains and the forests in their autumnal beauty."
    "Unfortunately, almost all of it was blocked out by the swell of Naomi's immense, quivering bust a few centimeters from my face."
    if getFlag("GTS049_embrace"):
        MC "Quite a view indeed. So vast... and natural... and per... uh, pervasive."
        show GTS_S embarrassed 
        "She looked down at me with a puzzled expression that quickly grew red and contorted."
        GTS "You could've told me."
    else:
        MC "I, uh, assume it's gorgeous."
        show GTS_S embarrassed 
        GTS "Ah. My apologies."
    "She lifted me in the crook of her arm until I could see over her chest."
    MC "Heheh... oh... woah..."
    "The landscape blurred before my eyes, mountains watching over green fields alike dressed in lordly gold and crimson."
    show GTS_S unique 
    "I put my arm around Naomi's shoulder as I delighted in the sight."
    MC "It's like flying on an airplane."
    "She only chuckled and held me up higher, to just nuzzle my face against her cheek."
    GTS "You know, I've never ridden on an airplane."
    MC "I... uh, heh, actually haven't either."
    show GTS_S unique 
    GTS "Well, I've heard the sights are incomparable."
    stop music fadeout 10.0
    "Like the edge of a great, green mist, we began to pass through sparse trees as the path drew us into the forest; it was strange, floating through the speckled, leafy realm of the songbirds."
    scene Woods
    show GTS_S neutral 
    with fade
    play music Nembutsu fadein 2.0
    GTS "In truth, I had a few particular reasons for doing this."
    MC "Oh?"
    GTS "First, I've come to learn that there's a grove of Japanese larches near the hiking trail."
    show GTS_S aroused
    GTS "Have you ever seen a whole grove of Japanese larches in autumn, Keisuke-kun?"
    MC "I... don't believe I have."
    show GTS_S unique
    GTS "Well, your deprivation ends today!"
    "I chuckled and, not really thinking about it, reached up to rub my hand over her cheek."
    MC "You're precious, Nacchan."
    GTS "Mmm!..."
    GTS "Thank you for bringing out the best in me."
    show GTS_S neutral
    GTS "So... the other reason I wanted you to come out here with me..."
    extend " was that, should the need ever arise, I would like to practice walking safely around other people."
    MC "Other people like me."
    show GTS_S embarrassed 
    "Her lips' edges pinched in on themselves as the cheeks around them bloomed with the faintest scarlet."
    GTS "...Especially you."
    MC "Ah, does this mean no more shoulder rides?"
    show GTS_S surprised with hpunch
    GTS "Perish the thought! I don't know that I'm quite ready to leave {i}that{/i} behind."
    MC "Heh, good. In that case, it would be my pleasure and honor to aid you."
    show GTS_S happy
    GTS "Thank you, my love."
    hide GTS_S
    show GTS neutral 
    with dissolve 
    "She then eased herself into a proper, ladylike sitting position, and then gently lowered me to the ground."
    "More and more, despite the gentle grace with which she did everything, even the lightest flits of her only-proportionally slender muscles sent shockwaves through me. It was like being caressed by an excavator."
    "I stumbled just so out of her embrace and onto the dirt path, my shoe crunching on a leaf as red as a stormy day's sunset."
    GTS "I want to try and match your pace, like we did before."
    MC "Oh, okay."
    pause 0.75
    MC "Won't that be, erm... extremely slow?"
    show GTS happy
    GTS "Oh, it'll be fine! I'll be going just as fast as when we first met!"
    "I smiled; I couldn't help it, whenever I got to see her like this."
    "I could count the rays of light coming down from heaven, I felt the brotherhood in the birdsongs, and the warmth off her radiant face amidst the infinite forest horizon."
    "It seemed to me that every little bit she grew made her even more a fixture wherever she roamed."
    show GTS wink
    GTS "Are you quite well? You seem positively transfixed by something."
    MC "You are so... enchantingly beautiful."
    show GTS happy
    GTS "Hmhmhm, thank you."
    MC "Hm... well then, shall I?"
    GTS "Please."
    hide GTS
    show GTS_S neutral 
    with dissolve 
    "I started off, and after I had put a few meters between us, Naomi rose and followed after."
    "Every minute or so, the slight {i}thumph{/i} from the topsoil deforming under her footsteps would get louder or quieter, speed up a little, slow down some more."
    "I glanced over my shoulder; with her hands folded over her lap, Naomi was..."
    "When I took in her whole body, my brain registered her as tip-toeing at a glacial pace across the forest floor; even the sound of the effortless pulverization of so many leaves at once blended together into a single, sandy but unabrasive rasp."
    "But when I focused on just one colossal leg thrusting through the air, with toes en pointe to pierce the very face of the earth, I was once again totally slapped in the face with the vastness of her speed and power, even under such thorough restraint."
    GTS "How am I doing, my sunshine?"
    MC "Excellent, so far."
    MC "That said, we may want to take some of the... circumstantial aspects of your movement into account from now on."
    show GTS_S pondering 
    GTS "Hm..."
    GTS "Is it... difficult to walk near me?"
    menu:
        "No, just good to be mindful.":
            GTS "You're sure?"
            MC "Completely."
            MC "Being away from you is {i}much{/i} more difficult."
            show GTS_S aroused with dissolve
            GTS "I'm glad you feel that way. It's much too late to back out now."
            MC "I couldn't if I wanted to, could I?"
            if getFlag("GTS049_support"):
                show GTS_S neutral 
                GTS "You {i}don't{/i} want to."
                "I couldn't conjure a response, so I turned my head back forward, my cheeks getting a little hot in the sultry forest floor."
                MC "..."
                show GTS_S unique 
                GTS "Hmhmhm!"
        "Well... not yet.":
            GTS "...I see."
            pause 1
            GTS "What if, someday, it is? What will we do?"
            "At the moment, I didn't really know."
            MC "We find a way to go on, I guess."
            show GTS_S neutral 
            GTS "I imagine we shall."
            $setAffection("GTS", 1)
    "We kept going for a while before another concern seeped into my head."
    MC "Naomi-chan?..."
    pause 0.5
    GTS "Yes?"
    pause 1
    MC "Do you ever regret what we've become?"
    show GTS_S sad
    GTS "Hm?..."
    pause 0.5
    show GTS_S neutral 
    GTS "Well... to yearn for a path long past is folly."
    if checkSkill("Art", ">", 5):
        MC "To err is human." 
    else:
        MC "So, you don't?"
    "Save for her footfalls, she was quiet for a moment."
    pause 0.75
    GTS "...I am thankful for the virtues that have been instilled in me. Even still, my lot in life entails certain bonds and responsibilities that I cannot duly honor while adhering to the precepts."
    MC "Bonds and responsibilities like what?"
    GTS "Well, chiefly, to help maintain my family's station. Our primary enterprise is in managing property and land holdings."
    show GTS_S surprised 
    GTS "I do admit, as long as our household has been around, it adds up to a rather intimidating figure, even divided between Kazumi and me."
    MC "How long {i}has{/i} your family been around, exactly?"
    show GTS_S happy
    GTS "We were founded in 871 A.D. as retainers of the Ōuchi clan."
    MC "{i}Oh{/i}.{w} So like {i}old{/i} old."
    show GTS_S unique 
    GTS "Indeed."
    MC "It's kinda cute that you know the exact number off the top of your head."
    GTS "Erm... thank you. I do try."
    show GTS_S neutral 
    "Not really thinking about it, I stepped around a thick tree branch that had fallen on the path."
    MC "So... where do I fit into your bonds and responsibilities?"
    GTS "Well..."
    show GTS_S neutral with vpunch
    "I jumped as something exploded behind me; a volley of wood chips bounced off my back and bit into my hair."
    show GTS_S surprised with vpunch 
    GTS "Goodness gracious! Are you alright?"
    MC "Y-yeah? Was that you?"
    GTS "I... I was so absorbed in thought, I stepped on that tree branch without even realizing it."
    "I turned around, patting the back of my ponytail; Naomi, fingers pinching the hem of her skirt, was gingerly withdrawing her foot from the middle of the tree branch, which had been shattered to powder."
    "Her face was red as a stormy morning."
    "She stepped over the broken halves of the branch after a beat and looked down at me, her expression indiscernible."
    show GTS_S pondering 
    GTS "Keisuke-kun? Erm... shall we proceed?" 
    MC "...Can you do that again?"
    GTS "You want me to step on a tree branch?"
    MC "...{w}You don't have to if you don't want to."
    pause 0.75
    if getFlag("GTS049_embrace"):
        show GTS_S aroused with dissolve 
    else:
        show GTS_S neutral with dissolve 
    GTS "Well... if it pleases you, my love."
    "Another rumble in the woods as she stepped back; her raised, bowing skirt framed her dainty footwork, one leg circling behind the other; how effortlessly she commanded those two mighty columns of alabaster."
    "Shoe en pointe, she raised her front shin up over one half of the branch, and perched it atop the jagged bark."
    "There was something more than accommodation in the smile she flashed me as she released her full weight onto the groaning timber."
    show GTS_S happy 
    GTS "Hmph!"
    "And then she pressed. The log turned oblong, a cluster of pale, deep fractures ripped into the side..."
    show GTS_S happy with vpunch
    "And the thing cracked and burst, shattered into a rain of slivers as long as my forearm, while her untoned calf quivered from hitting bare soil."
    "A {i}crack{/i} that I could feel echoed through the trees, muddling among the rustles and squawks and hoofbeats of fleeing animals. As though foretelling a spirit, the scent of sawdust suddenly flooded over me."
    show GTS_S neutral 
    GTS "I'll be sparing the other half. The beetles and centipedes could use a habitat."
    MC "Uhh..."
    "One swift sweep of her leg sent the remaining shards flying off the trail into the ferns and trees, kicking up a tall plume of dust with it. The ground trembled poignantly as she took two steps toward me."
    show GTS_S wink
    GTS "I trust I won't have to worry about you looking privily at other girls, Keisuke-kun."
    MC "No ma'am, not a chance."
    show GTS_S unique 
    GTS "As expected."
    "After a second of rather mindlessly watching the cloud of dust and pulverized lumber twinkling down in the beams of sunlight behind her, I turned around and kept walking."
    MC "So, uh... you were saying earlier?..."
    show GTS_S neutral
    GTS "Mmm..."
    "She puffed out a sigh."
    GTS "Please don't misunderstand me, but to carry on a family affair, I will eventually need a family. I will need a husband."
    MC "..."
    MC "Am I husband material?"
    GTS "I think you are."
    GTS "My father, at the very least, doesn't disagree out of hand."
    MC "Is that... {w}why he approved in the first place? Like, us dating?"
    GTS "Most likely, yes."
    "My eyes opened a little wider, if only for Naomi's sudden candidness. The deep forest was growing a little brighter, a little warmer."
    MC "Heh... I almost wonder how I cleared the bar that early."
    GTS "Hmhm... I don't."
    pause 0.25
    GTS "You're so abundant in kindness and understanding, all the time. Goodness is perennial in you like no one I've ever met."
    GTS "If tomorrow you were spirited away from me..."
    pause 0.5
    GTS "Well, I would count these the best days of my life."
    MC "Well... I'm not going anywhere, blossom."
    "She didn't respond for a second."
    show GTS_S happy with vpunch 
    MC "Gwuh-!"
    "Until I felt a set of impossibly huge fingers wrap around my middle from behind. The G force as she pulled me up and behind to her face pressed my neck against my shoulder and whipped my ponytail around over {i}my{/i} face."
    "Gently she flipped my hair out of the way with her fingertip, and gave me the softest, warmest peck on the forehead with her lower lip."
    show GTS_S embarrassed 
    "Her face soured as she withdrew."
    GTS "Erm, would you kindly pull your hair off my lip? I am... unsure I can muster the delicacy required."
    MC "Yeah."
    MC "And on the subject of, uh, delicacy, you may wanna take it a little slower next time you pick someone up, Nacchan." 
    show GTS_S surprised 
    GTS "Ah! Of course, I'm sorry."
    "Once I'd extracted the stray tresses, she eased down on one knee and then the other, and set me down."
    "Her eyes fixed behind me just as she was about to stand."
    show GTS_S neutral 
    GTS "Hm?..."
    show GTS_S happy 
    GTS "Look, Keisuke-kun!"
    "I turned and, just from this angle, saw a sliver of gold shine in the midst of the bark, squinting from the radiance of it."
    MC "Is that... the larch grove?"
    show GTS_S neutral 
    GTS "So it is. Let's get closer, shall we?"
    "We stepped off the trail together... more or less... and while she was worming her way through the tree branches, breaking as few as she could, I traipsed through the grassy underbrush until my shoes kissed the edge of a dropoff, down a hill."
    "Beyond was a saffron abyss, a mountain valley cloudy with the autumnal canopies of the larches receiving the bountiful sunlight and most generously reciprocating it."
    show GTS_S unique
    MC "...Woah..."
    "I was struck, too, by their antiquity. Some of them dwarfed even my towering girlfriend several times over. The very tops fluttered just faintly in a breeze I could now feel on my cheek."
    show GTS_S neutral 
    GTS "There was a valley much like this one on Mount Hiei."
    GTS "My grandmother would take me there some weekends to practice sitting meditation, and sometimes we would chat a while with monks, from the nearby temples."
    MC "I can see why."
    GTS "Indeed."
    pause 0.5
    "A stronger gust rolled down the mountain, shaking a rustling sigh from the forest all around."
    pause 0.5
    GTS "One can hardly imagine everything these trees have witnessed."
    GTS "Some of them could be over a hundred years old... a hundred years standing up here, watching all the striving, the tumult, the sorrow."
    GTS "And then, watching life go on."
    GTS "And watching the cycle begin anew."
    if getFlag("GTS049_embrace"): #if they had sex
        pause 1
        MC "Do you... think the trees... watched us fuck?"
        show GTS_S unique 
        "Naomi's high, resonant titter shattered the quiet air as she nearly doubled over."
        "She tried to say something, but it got caught between her lips and her teeth in another shuddering laugh."
        show GTS_S happy
        GTS "L-{i}Language{/i}, mister!"
        MC "Sorry. Do you think the trees watched us prepare tea?"
        GTS "{i}Khm{/i}... likely not, we were inside."
        MC "Ah, you got me there."
        show GTS_S neutral 
    MC "Did you ever envy them?"
    show GTS_S pondering 
    pause 0.75
    GTS "The trees?"
    show GTS_S surprised 
    GTS "Ah, the monks."
    MC "Yeah."
    show GTS_S neutral 
    GTS "As much as the next five-year-old girl, I'd wager. Even dreaming of becoming a boddhisattva one day, I was... not quite ready, spiritually, to jump into that life of interminable chores and doldrums."
    GTS "Now that I'm older, well... I imagine there are worse ways to live life."
    MC "I imagine so. Personally I think I'll stick to my life of sin, though. I've gone too far to turn back now."
    "Naomi smirked."
    show GTS_S pondering 
    GTS "Hmm..."
    GTS "Pray tell, are your parents religious in particular?"
    MC "My dad owes his soul to Kazoku Mart, if that counts."
    show GTS_S neutral 
    GTS "Hmhm, that wasn't quite what I meant."
    MC "Well, definitely not like yours. You can probably tell Tomo-chan and I were not raised in a monastery."
    MC "We'd visit shrines every so often, but I never got the impression my mom and dad were that passionate about it."
    GTS "I see. I imagine most families are something like that."
    MC "Yeah."
    "I stared down the hillside for a second."
    menu:
        "Let's get closer":
            GTS "I shall go first. I shouldn't like to trip and fall with you in front of me."
            "I stepped to the side, extending my arm."
            show GTS_S unique 
            GTS "Ever the gentleman."
            show GTS_S neutral 
            "Naomi extended her hands out to either side, palms down, as though headpatting two Saint Bernards at once, and made a first tentative step down the slope."
            "As expected, she was hardly in any danger of falling over. One foot hooked gracefully around the other, leaving nearly a straight line of flat divots in the grass as she descended."
            "I noted how long it took before my eyeline was about level with hers. Surprised isn't the right word... brought back to reality, I suppose."
            "Once she was about halfway down, I began following, literally, in her footsteps. At the bottom, she turned to crook her finger at me to come, before slipping in through the trees."
            hide GTS_S with dissolve
        "Let's roll down":
            show GTS_S pondering 
            GTS "Roll down?"
            MC "Like on our sides."
            pause 0.75
            MC "C'mon, it'll be fun!"
            GTS "It's rather a silly idea, isn't it?"
            show GTS_S unique 
            extend " Let's do it!"
            "I reached over to slap the back of her calf."
            MC "Yeah, YOLO!"
            show GTS_S neutral 
            GTS "Come again?"
            MC "Oh, uh, it's like an expression. It stands for 'you only live once'."
            GTS "I'm afraid I must disagree on theological grounds."
            MC "Fair enough. Still wanna do it?"
            GTS "I do. Allow me to go first."
            hide GTS_S
            show GTS neutral 
            with dissolve
            GTS "Mm..."
            "Naomi lowered herself down on her stomach, her bent arms framing her boulder-like bust as if about to attempt a push-up. Her legs gave a couple languid kicks as she looked down the hill, assessing the landing."
            "Satisfied, she pushed off."
            show GTS surprised with vpunch 
            GTS "Hwah!"
            show GTS surprised with vpunch
            "She plummeted, rolling like thunder, and for that second and a half I could've believed I was caught in a minor earthquake, the way her unfettered mass sent goosebumps through the skin of the earth, just like mine."
            show GTS unique with vpunch 
            "With one final shockwave up the hill and up my legs, she thrust out her arm to stop herself just short of crashing into a larch."
            GTS "{size=36}Hahahaha!{/size} Oh, what a delight!"
            show GTS neutral 
            GTS "Your turn, my love! I'll catch you!"
            MC "Coming!"
            "I got on my stomach too, roughly in Naomi's direction, and I went a-tumbling."
            "It flew by as a dream, a cacophony of wind and scrunching grass and blurs of green and yellow and blue, a smile, a bigger smile as my head rattled on the dirt."
            show GTS happy
            "The stop was smooth, apart from the sudden sinking in my stomach. I recollected myself and gradually perceived the upper boughs waving to and from me."
            GTS "Look, you're flying!"
            MC "Kheheheh, you dork."
            "After swirling me around in the air a couple more times, Naomi set me down."
            $setAffection("GTS", 1)
            hide GTS
    show GTS_S neutral 
    with dissolve
    GTS "Well now, shall we see it from the inside?"
    MC "Capital idea, old sport."
    "Naomi chuckled and squeezed her body in between the carrot—leaf—like trunks of the larches."
    "I followed her, keeping up pretty well on account of her tender wrestling with all the sticks and branches about her face, and found myself in a small otherworld, divine in its warmth, its quiet, its radiance."
    show GTS_S unique 
    "Fortunately, the trees grew taller towards the center of the grove, granting even Naomi a little reprieve."
    GTS "Keisuke-kun? You seem rather befuddled."
    MC "I... guess I've never really seen anything like this before."
    GTS "I suppose I haven't either, after a fashion."
    show GTS_S embarrassed 
    GTS "As vast as Mount Hiei's groves seemed when I was a child, now they feel rather more... personal."
    MC "...Probably just about everything does."
    GTS "Not untrue."
    show GTS_S neutral 
    GTS "Ah, it looks as though there's a clearing ahead. Let's sit and appreciate these environs a while, shall we?"
    "I looked, and there it was: a patch of bare grass around a small cluster of rock stupas, themselves encircling six jizo statues, robbed by the elements of their wrappings. All of it was awash in sunrays."
    show GTS_S embarrassed 
    "Naomi crouched under the lower boughs at the edge of the clearing, and then tiptoed more slowly than I'd ever seen her move before."
    "It was like she was in slow motion, from cat-stepping up close... but not too close... to the little old memorial, to ever-so-gently lowering herself down into half-lotus position."
    hide GTS_S
    show GTS sad 
    with dissolve
    "I sat down next to her."
    GTS "Mm... poor things. We shall have to return someday soon with baby blankets."
    show GTS pondering 
    GTS "Or hats."
    MC "Yeah... we should."
    stop music fadeout 7.0
    pause 0.5
    show GTS neutral with dissolve 
    "After a moment, she breathed out and shut her eyes; I joined her."
    scene black with fade
    pause 3
    "{i}creaaaaak{/i}"
    pause 2
    "{i}creak{/i}"
    pause 3
    "{i}creaaaaaaaak{/i}"
    MC "...What's that sound?"
    scene Woods
    show GTS pondering 
    with fade
    GTS "Hm? What sound?"
    MC "Like a tree branch bending. You don't hear that?"
    GTS "I... don't."
    hide GTS
    show GTS_S pondering 
    with dissolve
    "I stood up and looked around, at first perceiving nothing out of the ordinary. Naomi got on one knee and stood as well."
    MC "I think it came from over there."
    hide GTS_S with dissolve 
    "Indeed, I picked up the sound again, a little louder, as I walked to the edge of the clearing, next to a thin corridor of younger trees."
    "In a moment I realized the noise was right above me; I looked up."
    MC "?..."
    if isEventCleared("BE021") or getFlag("Meet_Haruhiro"):
        MC "...Haru... Haruhiro? What are you doing out here?"
        "Shakily clinging to a couple tree branches some seven meters above me was a familiar elephant-eared archer with his trusty longbow and a bandolier of various first aid supplies slung around his shoulder."
    else:
        MC "...Do you, uh... need some help, dude?"
        "Shakily clinging to a couple tree branches some seven meters above me was a young man with a longbow and... a bandolier of first aid supplies slung over his shoulder."
        "His saucer-sized ears and the emblem on the breast of his button-up marked him as a fellow student."
    "He immediately made the most violent shushing gesture I've ever seen, and frantically jabbed his finger back the way I came."
    MC "You... want me to leave you alone?"
    "I then heard rustling in the grass out among the younger trees, and looked over to see who it was."
    "Just under it, I also heard a low, bestial grumble. Out from behind a tree plodded a grizzly bear as high as my shoulder."
    "It turned its head to look directly at me, its wet black nose pulsating."
    MC "Uh... Naomi?..."
    "It grumbled louder and began trotting towards me, then broke into a charge."
    MC "{i}Naomi!{/i}"
    "She didn't answer. {w}As I turned to run, I staggered at the sight of Naomi diving through the air, sailing past me like a runaway freight car. Her arms were outstretched and grasping, her huge, white eyes and clenched teeth a mask of ghastly fury."
    "The four-hundred-kilogram beast faltered at the sight, too, and began to turn just as Naomi was about to hit the dirt."
    "{i}THOOM{/i}"
    "My legs unsteady as they already were, the impact put me hard on my ass. I sucked in a breath while listening to Naomi's grunts of effort and the bear's distressed baying, and jumped to my feet."
    show GTS angry
    "Wrestling with the beast, Naomi tried to roll onto her back, leaning her hips against a young larch, her weight snapping its trunks one by one, each one a thunderclap. Wood chips rained down on me, again."
    "The dust began to settle with Naomi holding the grizzly up in the air; it flailed but was completely pinned in her hands."
    GTS "{size=36}I've got him!{/size}"
    GTS "{size=36}Keisuke, are you alright?{/size}"
    MC "Holy shit!"
    GTS "{size=36}Keisuke!{/size}"
    MC "Y-Yeah! I'm fine!"
    GTS "Oh, thank the stars!"
    MC "Do you..."
    MCT "What the hell could I possibly do to help?"
    "My mind flew to the man in the tree."
    "He wasn't in the tree, however; he was on the ground in front of it, wincing and rubbing his arm."
    if isEventCleared("BE021") or getFlag("Meet_Haruhiro"):
        MC "Haruhiro-san!"
        GTS "Who? Is someone else here?"
        Haruhiro "Affirmative!"
        MC "It's the president of the archery club, he was up in the trees for some reason."
        "After staring in Naomi's direction for a second or two, agape, he sprung to his feet with surprising vigor."
        "I was about to ask him again what he was doing when Naomi cut in."
    else: 
        MC "Who are you, anyway?"
        GTS "Who? Is someone else here?"
        UNKNOWN "Affirmative! A-And acknowledged!"
        MC "Some guy was up in the trees. I think he's another student."
        show GTS surprised 
        GTS "Heavens! Is he really?"
        "After staring in Naomi's direction for a second or two, agape, he sprung to his feet with surprising vigor."
        UNKNOWN "I'm-"
        "He gave me a sharp bow that flung his other bow off his shoulder. After bending down to pick it up, he cleared his throat."
        Haruhiro "I'm Haruhiro Haganeya, president and company commander of the Seichou Academy Archery Club."
        $setFlag("Meet_Haruhiro")
        MC "Alright then. Can I ask you what you were doing in that tree?"
        "Naomi cut in before he could answer."
    show GTS surprised 
    GTS "There's an arrow in its posterior!"
    MC "An arrow?"
    GTS "Yes. Heavens, what a dreadful sensation..."
    MC "..."
    "I thought over the facts as I let the veins in my neck gradually stop throbbing."
    MC "You know who shot that bear, Haruhiro-san?"
    "He chewed his lips for a second."
    Haruhiro "At eleven hundred hours I was conducting periodic one-man shooting drills approximately one-point-five klicks from the trail when at least one ursine belligerent entered my perimeter."
    show GTS neutral 
    GTS "Shhhh... easy now, you're alright..."
    "I glanced over to see Naomi petting the bear's belly with her fingers. Somehow, it did seem to be relaxing a little."
    Haruhiro "Then, uh, once contact was established, pursuant to R.O.E. I took position and readied my weapon."
    "He looked away from me."
    Haruhiro "At that point, the known ursine belligerent initiated a rearward withdrawal.{w}.. however, a failure of morale caused a misfire of my weapon, which struck the K.U.B. mid-withdrawal."
    show GTS pondering 
    Haruhiro "Upon being hit, the K.U.B. reversed its withdrawal and advanced on my position. I then elected to conduct a tactical retreat and regroup at an elevated position."
    if checkSkill("Academics", ">", 7):
        pause 0.5
        MC "You know bears can climb, right?"
        pause 0.5
        Haruhiro "Aforementioned failure of morale may also have caused a deficit of field applications of information."
        pause 0.5
        MC "Jesus..."
    else:
        pause 0.5
        MC "Alright, I'm gonna need a translation for whatever the hell you just said."
        Haruhiro "I got scared and I shot it in the ass, okay?"
    show GTS angry
    "Naomi sat up, her brow furrowed as she regarded Haruhiro. As though feeling it, he bowed deeply."
    Haruhiro "Please accept my sincere apologies if I put you in harm's way."
    "'If'. And then there was fire in my throat." 
    MC "No {i}shit{/i} you did, I was two seconds from getting mauled by a goddamn bear!"
    MC "Were you just gonna sit and hide!?"
    Haruhiro "I-"
    GTS "Peace, Keisuke-kun."
    "Carefully adjusting her grip on the bear, Naomi got into a sitting position."
    GTS "Look at me, Haruhiro-san."
    "He obeyed, without hesitation."
    if getVar("GTS_selfhood") > 5:
        GTS "I must impress upon you the gravity of the situation. There is no honor in pressing a fight you cannot win."
        GTS "If you thought this creature a threat, then you ought to have fled without needlessly spilling blood and putting innocent people in danger."
        GTS "Do you understand, Haruhiro-san?"
    else:
        GTS "From the sounds of it, you very well knew this bear had no ill intent toward you until it was attacked. Leaving it in peace would have spared my boyfriend's safety {i}and{/i} your dignity."
        GTS "In that light, the shadow of some illusion of personal glory were a small price to pay."
        GTS "Wouldn't you agree, Haruhiro-san?"
    Haruhiro "Y-Yes, ma'am."
    MCT "I feel a little better."
    show GTS neutral 
    GTS "Very good."
    GTS "Now, if you would atone for this lapse of judgment, I think a fine first step would be to use some of those supplies you've got around your shoulder to help treat the wound."
    Haruhiro "On the {i}bear{/i}? Are you crazy?"
    GTS "Do you wish to be a man who runs from his problems? Or do you wish to be a man who stands up and takes charge of what is his?"
    "I could see on his face that the question struck him through the heart."
    Haruhiro "I... {size=9}Agh... dammit.{/size}"
    Haruhiro "...{w}Understood. Here, I have some antiseptic."
    GTS "Do you have any vulnerary materials?"
    Haruhiro "Yes, ma'am."
    GTS "Very good. Please smear a generous dab of it over the site once you've applied the antiseptic."
    Haruhiro "Yes ma'am."
    "Holding down its back legs, Naomi lowered the bear to Haruhiro's level. He slunk towards the hulking creature's backside, the bottle vibrating in his hand."
    "He gulped and put his free hand on the arrowshaft."
    GTS "Shhhhhh..."
    show GTS surprised with vpunch 
    "The howl when he yanked it out nearly sent him tumbling, and even Naomi jumped, but thank God she didn't let go."
    "She kept on murmuring gentle platitudes as Haruhiro frantically squirted antiseptic on the wound, pouring down its leg mixed with trickling blood, and then slapped a gob of pale yellow goop on the spot."
    "Seeing some blood about to drip onto her leg, Naomi winced, looked away, and held her captive out over the grass."
    "A few minutes more, and it had quieted down enough to talk again."
    Haruhiro "So... is the objective complete?"
    show GTS neutral 
    GTS "I suppose it is. Moreover, perhaps it would be best if you chose another site in which to conduct your drills."
    Haruhiro "I will... consider rectifying operational procedure."
    Haruhiro "Requesting dismissal, ma'am."
    GTS "Keisuke-kun, are you satisfied?"
    MC "Yeah, I suppose so."
    "She nodded."
    GTS "You may take your leave."
    Haruhiro "Yes ma'am!"
    "With that, he bowed and started jogging back to the trail."
    play music GTS
    "I waited until he was most definitely out of the grove."
    MC "I almost died because of {i}that{/i}. Isn't life funny?"
    show GTS angry
    GTS "What a pompous applejack. If he had truly..."
    "She closed her eyes, and gulped."
    GTS "Thank heavens we were here together, and not some other poor, hapless soul."
    show GTS neutral 
    GTS "Though I must admit, that your first instinct upon seeing a bear charging at you was to warn me was quite commendable. I don't know how many would stand their ground under the circumstances."
    MC "I mean, {i}your{/i} first instinct was to tackle it."
    GTS "I could hardly stand by and watch, now could I?"
    GTS "After all, courage is one of the most esteemed virtues for us Yamazaki."
    MC "I imagine it helps that it's like the size of a shiba inu to you now."
    show GTS embarrassed 
    GTS "I suppose my strategy would otherwise have been rather unsound."
    MC "And by the way... how did you get that guy to just... do what you say?"
    show GTS neutral 
    GTS "Elementary."
    GTS "At the heart of social harmony is mutual compassion and understanding."
    GTS "Recognize the wants, needs, and merits of your fellow man, and often he will reciprocate in kind."
    $setSkill("Academics", 1)
    MC "...Huh."
    if checkSkill("Academics", ">", 8):
        MC "So, how did you know what {i}he{/i} wanted?"
        GTS "As is often the case, simply listen and he will tell you."
        MC "Heh, I guess so."
        MC "Did I ever tell you I'm glad you're on my side?"
        show GTS happy
        GTS "You don't need to, my love."
    show GTS neutral 
    "She looked down; the bear had more or less calmed down, its fury reduced to the occasional bassy whimper."
    GTS "Speaking of which, it appears this poor fellow is ready to be let go."
    GTS "I'll walk a fair distance away and then release him."
    show GTS pondering 
    GTS "I hope the vulnerary doesn't wash off."
    MC "Hopefully not, but I dunno what else we can do for him."
    GTS "Nothing for it but to pray for good will to prevail, I suppose."
    hide GTS
    show GTS_S neutral 
    with dissolve
    "Thus she arose and, with the same graciously glacial steps she'd gotten here with, walked to the edge of the clearing."
    hide GTS_S with dissolve 
    "I can't be sure, but I thought I saw the bear turn its head around her shoulder to give me one plaintive parting glance."
    "When she was out of earshot, I let out a long sigh, longer than I knew was in me."
    "I looked around the grove; all the legion of the golden leaves waving in the afternoon sunlight had begun to look more like the wriggling boundaries of a dreamscape."
    "Before I could contemplate too much on why, I registered Naomi coming back my way."
    MC "All taken care of?"
    show GTS_S neutral with dissolve
    "She nodded, and casually looked to the side, back toward the little jizo shrine."
    show GTS_S surprised
    extend " Her hand floated up to her mouth."
    MC "Nacchan?"
    "I turned my head."
    MC "Oh..."
    "The statues lay on their sides, sprayed over with dirt and grass. The stupas were crumbled into a loose, ruinous ring of stones."
    hide GTS_S
    show GTS sad
    with dissolve
    "She got down on her hands and knees after stepping softly up to the shrine; she reached out, faltered, then pushed each of the statues up with her fingertip, one by one."
    "She sighed, and then pinched some of the larger stones between her fingers."
    "It slipped, clattering on the bones of its brothers. She pinched it again.{w} And again.{w} Five times.{w} Ten."
    MC "Naomi-chan..."
    pause 0.75
    show GTS sad-2
    "She bowed her forehead to the ground."
    GTS "Please forgive me, little ones. I did not... have it within me to act for the greater good."
    GTS "I promise I will make this right."
    "And she looked up, and kept on trying to stack the stones."
    "Amid the silence, apart from that clattering like a languid clock, I stepped, too, knelt down, and started stacking the rocks around the little jizo statues."
    pause 0.75
    show GTS neutral with dissolve 
    "She was still for a while, until she started trying to slide the larger stones atop each other for me; it worked."
    pause 0.5
    GTS "You're so brave."
    "I smiled a little."
    MC "If you need me to be, I will be."
    jump daymenu

label GTS053:
    "This marks the current end of Naomi's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance

label GTSFMG001:
    scene Campus Center
    show Natsuko neutral at Position(xcenter=0.25, yalign=1.0)
    show GTS neutral at Position(xcenter=0.75, yalign=1.0)
    with fade
    play music Busy
    if isEventCleared("FMG016"):
        Natsuko "Watch your step, Hotsure-san. Some idiot spilled something."
    else:
        UNKNOWN "Watch your step, Hotsure-san. Some idiot spilled something."
    MC "Yep..."
    "So there I was, dodging soup puddles with my arms wrapped around bundles of brooms and shovels, as we're wont to do in the more wayward days of our lives."
    "I'd been lucky enough to be assigned to groundskeeping chores with the impenetrably serene Naomi Yamazaki. But then, just to be sure my karma was good and balanced, it was decided a third helper was needed, and the universe sent Natsuko Okamoto."
    if not isEventCleared("FMG016"):
        "She was apparently from a different homeroom, which was something of a relief. She had the build of a mob enforcer and a disposition to match."
    else:
        "I never ran into her much, but Natsuko's warm smile and sunny disposition hadn't changed a bit."
    "She was in front with her unmoving arms clutching four bags of dirt over her shoulders, while Naomi was silent behind me cradling a stack of flowerpots atop a lacquered black kimono chest. Three laboring ants under the full, teasing mid-spring sun."
    "Granted, of the three of us, I was the one closest to an ant."
    "It's funny how life works."
    if checkSkill("Athletics", ">", 3):
        MC "We going to the campus garden or the front entrance first?"
        Natsuko "Just the campus garden. Usui-san, Inoue-san, and Oyama-san got assigned the front entrance."
        MC "Oh, okay."
        show GTS sad
        GTS "I am rather glad... these pots really are starting to weigh on me..."
        MC "Want me to take some of those off your hands?"
        show GTS embarrassed
        GTS "Oh, no, it would scarce be worth the trouble since we're so close. You are very kind to offer, though."
        MC "'Course."
        $setAffection("GTS", 1)
        jump GTSFMG001_c1
    elif checkSkill("Athletics", ">", 0):
        MC "We going to the campus garden or the front entrance first?"
        Natsuko "Just the campus garden. Usui-san, Inoue-san, and Oyama-san got assigned the front entrance."
        MC "Oh, okay."
        show GTS sad
        GTS "I am rather glad... these pots really are starting to weigh on me..."
        MC "Well hey, not too much longer, right?"
        show GTS neutral
        GTS "Right you are, Hotsure-san. Moreover, this is a splendid opportunity to reflect on the ephemerality of the body, indeed, the corruption perennial with it."
        Natsuko "Seems a little dramatic when you could just lift weights once in a while..."
        jump GTSFMG001_c1
    else:
        MCT "{i}Uggghhhh{/i}, why did I agree to this..."
        "I was also probably the closest to death."
        MC "Hah... you know, mebbe we... {i}hagh{/i}... shoulda use the pushcart..."
        Natsuko "Suck it up, Hotsure-san. It's too late for what-ifs. Besides I'm sure you don't want to walk all the way back to shed and grab it."
        MC "No, nope, mm-mm."
        Natsuko "I'll carry those if you can't do it anymore. We've wasted enough time as it is."
        MC "Nah, mgood, thanks though."
        "A cool bead of sweat trickled down from my salty, matted hair, trailing over my brow and settling on my eye; half my world turned foggy and distorted. And so it would remain, with no free hand to wipe it."
        Natsuko "We're almost there. Surely, you can last a few more minutes."
        MC "Ngkay."
        jump GTSFMG001_c1

label GTSFMG001_c1:
    show FMG neutral at Position(xcenter=1.1, yalign=1.0)
    "Our fellowship journeyed on across the vast green plain; with our hardy, stalwart redhead at the fore and our lanky sage keeping watch, no force could forestall us."
    show FMG flex at Position(xcenter=1.1, yalign=1.0):
        ease 0.5 xpos 0.5
    show GTS surprised
    FMG "Hey guys, whatcha doin'?"
    "Except maybe a sufficiently buff jogger. Naomi's eyes went wide and she staggered trying not to let anything fall. Natsuko just turned around, rolling her eyes."
    show FMG angry-3
    "As Akira looked over our group, she noticed Natsuko and her gaze turned to stone."
    if isEventCleared("FMG016"):
        MCT "Oh no."
    else:
        MCT "What's with that look?..."
    show FMG surprised
    FMG "Ah... ah..."
    FMG "ACHYOUSUCK!"
    show FMG sad
    FMG "Ah, 'scuse me, I'm allergic to bitches  who slap raw nori on their heads and call it a hairdo."
    GTS "Er... bless you."
    Natsuko "The next words out of your mouth better be an apology, Akira, or else the garden won't be the only thing having problems today."
    show GTS neutral
    show FMG neutral
    FMG "Wow, that's so cool, Nat. I don't recall asking!"
    FMG "You want some help with whatever it is you're doing, Yamazaki-san? I know bird's nest over here isn't the most helpful."
    MCT "...Wait a minute..."
    GTS "I suppose having an extra pair of hands couldn't hurt..."
    show GTS happy at Transform(xzoom=-1)
    FMG "'Course not! C'mon, gimme something to carry, I'll help you guys out."
    menu:
        "Speak up":
            jump GTSFMG001_c1_1
        "Remain silent":
            jump GTSFMG001_c1_2

label GTSFMG001_c1_1:
    $setFlag("GTSFMG001_c1_1")
    MC "Well, if you're offering... you wanna grab a couple of these shovels?"
    FMG "Sure thing!"
    jump GTSFMG001_c2

label GTSFMG001_c1_2:
    show GTS despaired-thought
    GTS "Well, do you think you could relieve me of some of these flowerpots, please?"
    show FMG neutral at Transform(xzoom=-1)
    FMG "Sure!"
    show GTS neutral with dissolve
    show GTS neutral at Transform(yoffset=10) with move
    "Naomi crouched down to allow Akira to grab the stacked flowerpots, and winced just slightly when she hefted them in each arm."
    if getSkill("Athletics") > 3:
        MCT "...Why didn't she want me to help?..."
    GTS "Thank you very much, Mizutani-san."
    FMG "You want me to get that box too?"
    show GTS neutral
    GTS "Thank you, but I would like to hold onto this one. It has a set of Hagi vases inside, a gift from a family friend in Yamaguchi."
    FMG "Woah woah woah... you don't mean like someone descended from the Mōri clan?"
    show GTS unique
    GTS "As a matter of fact, I do! It is quite an honor, hence why I wish to personally see to their safety."
    show FMG surprised
    FMG "Daaamn, you got connections! That's like getting a private jet from the Wright brothers!"
    show GTS embarrassed
    GTS "It rather is. They were quite gracious to entrust them to our school. I hope they will make other students feel more at home as they go about their days."
    jump GTSFMG001_c2

label GTSFMG001_c2:
    Natsuko "Yamazaki-san, Hotsure-san, are we about ready to move on?"
    show FMG neutral at Transform(xzoom=1)
    FMG "Aww, are you sad nobody wants to talk to you?"
    Natsuko "Keep talking and I'll bury you with the flowers."
    show GTS embarrassed at Transform(xzoom=-1)
    FMG "It's always empty threats with you, Nat. How about you follow through with it for once?"
    show GTS embarrassed at Transform(xzoom=1)
    GTS "Perhaps we should continue on, yes."
    "The two amazons exchanged searing glances before silently following the third's lead; Naomi kept her stoic gaze forward as we walked the rest of the way to the campus garden."
    scene black with fade
    pause 1

    scene School Planter
    show GTS neutral at Position(xcenter=0.75, yalign=1.0)
    show FMG neutral at Position(xcenter=0.5, yalign=1.0)
    show Natsuko neutral at Position(xcenter=0.25, yalign=1.0)
    with fade
    if getFlag("GTSFMG001_c1_1"):
        "Akira let the shovels thump onto the grass as I began handing out the brooms."
    else:
        "I passed out the brooms first, letting the shovels thump onto the grass."
    FMG "Alright, let's get to work!"
    Natsuko "There's only three brooms, Akira. You're gonna have to go."
    show GTS despaired-thought
    FMG "Crazy how I still didn't ask. If all you're gonna do is complain, maybe {i}you{/i} should go."
    if getAffection("FMG") > 5:
        $setFlag("GTSFMG001_natsupots")
        MC "Okamoto-san, why don't you put out the vases and start filling them with dirt?"
        show GTS unique
        GTS "A splendid idea. We ought to be done in no time."
        Natsuko "Fine. Pass me the vases."
        show GTS neutral
        "Naomi bowed and set down the box, and Natsuko sloughed off a couple bags of dirt and opened the chest, regarding no one in particular as she grabbed a couple glazed, oak-brown vases and set about her task."
        hide Natsuko with dissolve
        "The rest of us got to work too, taking brooms and sweeping the walkways that crisscrossed the garden."
        "I stole glances at Akira and Naomi working side-by-side; they were a study of yin and yang. Akira, like a tiger with its claws, swept in swift, powerful arcs that kicked up visible plumes of dust and the occasional wrapper."
        "Naomi, meanwhile, made slow, unintrusive strokes that eased the dirt off the path... though it was also pretty obvious she wasn't quite used to the way she had to hold a broom now. I saw her alter her course for a passing beetle."
        hide FMG with dissolve
    else:
        MC "Mizutani-san, why don't you put out the vases and start filling them with dirt?"
        show GTS unique
        GTS "A splendid idea. We ought to be done in no time."
        FMG "Alright, sure, pass me some."
        show FMG flex
        show GTS neutral
        "Naomi bowed and set down the box, and Akira opened it, pulling out two glazed oak-brown Hagi vases. She winked at Natsuko as she passed by."
        FMG "Better set those down, Imma need 'em in a second."
        hide FMG with dissolve
        "The rest of us got to work too, taking brooms and sweeping the walkways that crisscrossed the garden."
        "I stole glances at Natsuko and Naomi working side-by-side; they were a study of yin and yang. Natsuko, like a tiger with its claws, swept in swift, powerful arcs that kicked up visible plumes of dust and the occasional wrapper."
        "Naomi, meanwhile, made slow, unintrusive strokes that eased the dirt off the path... though it was also pretty obvious she wasn't quite used to the way she had to hold a broom now. I saw her alter her course for a passing beetle."
        hide Natsuko with dissolve
    show GTS neutral at altMove(0.5, 0.5)
    "I almost didn't notice her gradually sidling up to me, coincidentally sweeping in just the right pattern to converge with my path."
    show GTS despaired-thought
    "With her eyes down, she sighed a soft, wistful lament just within my earshot."
    GTS "It's such a shame when two good people can't seem to see the good in each other."
    MC "...Huh? Are you talking to me?"
    show GTS neutral
    GTS "Ah, Hotsure-san. Well, I suppose I'm curious what you think about it."
    MC "Oh... hm... well yeah, I agree."
    MC "It's sort of the natural result with, uh, competitive types, though."
    GTS "Undoubtedly. Nevertheless, there is a point where competitiveness may sour into disharmony. Perhaps even enmity."
    GTS "It is good to be content with the nature of things. I simply believe it would be kind, were the opportunity to arise, to nudge such persons toward a more illuminated perspective."
    MC "...Aight you lost me. What are we talking about?"
    GTS "I would like to see if we could look for some common ground between Mizutani-san and Okamoto-san that they can't seem to recognize themselves. Then, perhaps, we can try and bring it up to them."
    GTS "We'll hardly make friends out of them in an afternoon, but who knows... raindrops and time can dull the sharpest rocks."
    menu:
        "Ohhhh. Sure, let's do that.":
            $setFlag("GTSFMG001_help")
            GTS "I greatly appreciate it. I think we'd best stand back and observe for a while before we think of something specific."
            MC "Got it."
        "I dunno, I don't really wanna get between two girls who can each bench press a car.":
            GTS "As you wish. I hope you will not be offended if I attempt it on my own regardless."
            MC "Knock yourself out. I just wouldn't expect to make much progress today."
            GTS "'Go into battle expecting to die.'"
            MC "Uh... yes?"
            MCT "God forbid those two come to blows, you just might."
            "She nodded."
            GTS "Thank you for listening."
        "We should trick them into stepping in dog dookie.":
            $setFlag("GTSFMG001_help")
            show GTS surprised
            GTS "Preci- wait, what? Hotsure-san, with all due respect, I fail to see how that would help matters."
            MC "It would... uh... that way they have some kind of common... ground? It made sense in my head."
            GTS "I... think a different tack may avail us better."
            show GTS neutral
            GTS "Perhaps we should simply observe them for a while and think of something later."
            MC "Fair enough."
    "Naomi, still looking down, curved her path once again away from mine."
    hide GTS with dissolve
    if getFlag("GTSFMG001_help"):
        "I soon found the sidewalks were almost completely swept; it would be time to start placing the flower pots."
        MCT "Alright, detective mode. I gotta figure out what makes these girls tick."
        MCT "Hm..."
        menu:
            "The color red?":
                MCT "Akira's always wearing red shirts under her uniform..."
                MCT "And Natsuko's got her firetruck hair..."
                MCT "Or is that her natural color? It could be... probably shouldn't come right out and ask her, though. The consequences could be deadly."
                MCT "Maybe there's another way to bring it up..."
                "I took a breath; it was time to light the fuse."
                show GTS neutral at Position(xcenter=0.75, yalign=1.0)
                show FMG neutral at Position(xcenter=0.5, yalign=1.0)
                show Natsuko neutral at Position(xcenter=0.25, yalign=1.0)
                with dissolve
                MC "So... am I crazy, or would the school look better if they painted it, like, uh, red? Or something."
                FMG "Kind of a random question, but I guess that'd be cool. Beats all this generic eggshell crap everywhere."
                Natsuko "You can't just paint everything red, it'd be ugly as sin."
                FMG "This is a {i}fantasy{/i} scenario Okamoto, keep up."
                show GTS surprised
                Natsuko "Why don't {i}you{/i} keep up with the chores you insisted on butting into?"
                show GTS sad
                show FMG angry
                MCT "Well, that backfired literally instantly."
            "The gym?":
                MCT "Oh! Duh, they're both in the gym ten hours a day. Damn, I'm good."
                "I took a breath; it was time to light the fuse."
                show GTS neutral at Position(xcenter=0.75, yalign=1.0)
                show FMG neutral at Position(xcenter=0.5, yalign=1.0)
                show Natsuko neutral at Position(xcenter=0.25, yalign=1.0)
                with dissolve
                MC "So hey, after we're done here, I was thinking of hittin' the gym. Would either of you have some tips for me? I know you both are pretty serious about fitness."
                show GTS happy
                $setAffection("FMG", 1)
                $setAffection("GTS", 1)
                FMG "Sure! You looking to bulk up, get stronger, or what?"
                Natsuko "I've seen Mizutani's technique, Hotsure-san. Save yourself a sprain and get your advice from someone else."
                show Natsuko flex
                extend " Like me."
                show GTS pondering
                show FMG angry
                FMG "Oh shut up, I put in more hours than you by a longshot."
                Natsuko "Ever heard the phrase \"quality over quantity\"?"
                show FMG flex
                FMG "Yeah, which is funny 'cuz you got neither."
                show GTS sad
                show Natsuko neutral
                Natsuko "I've got more refinement in my pinky finger than you have in your whole body."
            "I dunno, kittens?":
                MCT "...I mean, I never met a girl who {i}hates{/i} kittens."
                MCT "Is that sexist?{w} ...Nah, nah, kitties can't be sexist."
                "I took a breath; it was time to light the fuse."
                show GTS neutral at Position(xcenter=0.75, yalign=1.0)
                show FMG neutral at Position(xcenter=0.5, yalign=1.0)
                show Natsuko neutral at Position(xcenter=0.25, yalign=1.0)
                with dissolve
                MC "You know, whenever I'm sweeping the sidewalk, I find it always helps to think about cute little kittens."
                show GTS pondering
                FMG "Uh... cool?"
                Natsuko "I guess that's fair. I like cats, too."
                FMG "Yeah, they're pretty cute."
                show GTS unique
                $setAffection("GTS", 1)
                MCT "Oh my God, is this actually working?"
                GTS "They can be quite the adorable little creatures, can't they? One of my old friends would always give some of her food to the stray cats around our neighborhood."
                show FMG happy
                FMG "Hah, same. Sometimes I'd give strays around my hometown pieces of melonpan."
                Natsuko "Let me guess, most of them didn't come back."
                show FMG angry
                FMG "What's that supposed to mean?"
                Natsuko "Yeast products are poisonous to cats, not that I'd expect you to know what yeast is."
                show GTS sad
                show FMG happy
                FMG "Hey, at least I know what having friends is. But I'm sure being the local bread expert is just as fulfilling."
                MCT "Ah, yep, that's more like it."
        show GTS neutral
        GTS "Well, let's keep at the task at hand, shall we? We're nearly finished."
        show FMG angry
        "I saw Akira and Natsuko exchange glances that could've welded steel, and we all went back to work."
        "The pots were almost a quarter of the way filled by the time the rest of us were done and began pitching in."
        show GTS pondering
        MCT "I gotta admit, if she hadn't told me, I'd have no idea she was up to something..."
        show GTS neutral
    else:
        "I soon found the sidewalks were almost completely swept; it would be time to start placing the flower pots."
        show GTS neutral at Position(xcenter=0.75, yalign=1.0)
        show FMG neutral at Position(xcenter=0.5, yalign=1.0)
        show Natsuko neutral at Position(xcenter=0.25, yalign=1.0)
        with dissolve
        GTS "Crackerjack! We made short work of that, didn't we?"
        Natsuko "At least {i}someone's{/i} pulling their weight."
        FMG "Say again? I was too busy, y'know, working."
        MCT "It's the ride that never ends."
    if getFlag("GTSFMG001_natsupots"):
        show GTS neutral
        GTS "Okamoto-san, perhaps you could begin placing the pots that are already filled?"
        Natsuko "Already on it."
        "As the rest of us three together rapidly filled the remaining pots, Natsuko's crimson hair whipped like a comet while she dashed between the pots and their destinations."
        "I stared a little when she wasn't looking; it was like a relay race between an almost-blurry Natsuko and a bunch of inanimate objects, and she was damned sure taking home the gold."
        show FMG angry-2
        "Then, I felt a speck of cold, moist soil fly into my left cheek; I looked there to see Akira, brow furrowed with steel resolve, shoveling dirt at a dizzying and highly imprecise speed. Maybe half was actually going into the pot."
        MCT "There is literally no win condition here, can you two chill?"
        show Natsuko flex
        show GTS surprised
        "At last, the final {i}clack{/i}; Natsuko triumphantly slammed the last pot into place, to Naomi's momentary horror."
    else:
        show GTS neutral
        GTS "Mizutani-san, perhaps you could begin placing the pots that are already filled?"
        show FMG upbeat
        FMG "Way ahead of you."
        "As the rest of us three together rapidly filled the remaining pots, Akira's burgundy ponytail whipped like a comet through the air while she dashed between the pots and their destinations."
        show FMG angry
        "I stared a little when she wasn't looking; it was like a relay race between an almost-blurry Akira and a bunch of inanimate objects, and she was damned sure taking home the gold."
        "Then, I felt a speck of cold, moist soil fly into my left cheek; I looked there to see Natsuko, brow furrowed with steel resolve, shoveling dirt at a dizzying and highly imprecise speed. Maybe half was actually going into the pot."
        MCT "There is literally no win condition here, can you two chill?"
        show FMG flex
        show GTS surprised
        "At last, the final {i}clack{/i}; Akira victoriously slammed the final pot into place as Naomi looked on in momentary horror."
    show FMG neutral
    show Natsuko neutral
    show GTS unique
    GTS "My my, would you look at that! In a blink of the eye we've finished the job entirely."
    FMG "Yep!"
    Natsuko "Thank God."
    if getFlag("GTSFMG001_help"):
        MC "...{w}Oh! Uh, yeah, that's church."
    GTS "Let us be thankful that we could come to see just what we can accomplish when we set aside our differences."
    FMG "Yep!"
    Natsuko "Sure, whatever."
    if getFlag("GTSFMG001_help"):
        MC "Go off, queen."
    show GTS happy
    GTS "It really is wonderful what becomes possible when we allow ourselves to see each other's strengths. {w}Wouldn't you agree?"
    "At this, Akira and Natsuko, to Naomi's credit, looked at each other with a mutual and heartfelt confusion."
    FMG "Yyyyyeah?"
    Natsuko "I suppose that's true."
    if getFlag("GTSFMG001_help"):
        MC "I have literally never agreed with anything so strongly in my entire life ever."
    show GTS neutral
    GTS "After all, you kept us steadfastly on task, Okamoto-san..."
    FMG "Hm..."
    GTS "...While you, Mizutani-san, so generously offered your time and abundant energy simply to help us."
    Natsuko "...Hmph."
    "Naomi put a finger to her chin and stood up straight as a board, only accentuating her statuesque height and posture."
    GTS "Oh, I have an idea! Why don't we all rendezvous at my dormitory? Some tea would be just the thing to help us all unwind."
    "The response was swift and enthusiastic."
    Natsuko "Thanks for offering, but you probably don't want Mizutani sweating all over your furniture."
    FMG "Look who's talking, Drownedratsuko. But hey, don't sweat it, 'cuz I'm done dealing with you today anyway. You're welcome, by the way."
    show GTS surprised
    Natsuko "Sure, thanks for bumbling in and distracting everybody trying to actually work."
    FMG "Ohhhhh, that was you trying? Oof, sorry, I had no idea."
    "I could see Natsuko's jaw grinding and I instinctively took a step back."
    Natsuko "Whatever. You can be a child on your own time, I'm leaving."
    hide Natsuko with dissolve
    show FMG angry-2
    "Akira's face scrunched up without even a glance at either of us."
    FMG "Pff... bumbling in... freaking jerk."
    "She raised her phone to her face and scowled at whatever it showed her, before turning around without a word and resuming her jog, pounding her feet as though she were off to beat up the sun."
    hide FMG with dissolve
    pause 0.5
    MC "Hm."
    pause 0.5
    show GTS pondering
    GTS "Well, drat. That was rather a wash."
    if getFlag("GTSFMG001_help"):
        MC "Well, I'm glad we tried... but, that turned out about how I expected."
    else:
        MC "Well, uh... sorry that didn't work out the way you hoped."
    GTS "Hmm... I fear I acted too rashly."
    GTS "I acted only on surface information, and only with minimal planning. I shall have to get to know them better for the next time I have the chance to act."
    "She turned aside, eyes still on me."
    show GTS neutral
    GTS "Shall we walk back to the dormitories together?"
    "I nodded and simply began walking, shortly joined by Naomi to my side."
    MC "So, 'the next time'... how much time do you think you'll devote to trying to patch things up between them?"
    "Hands folded behind her back, she looked down at me and smiled."
    show GTS happy
    GTS "I wish to make use of every chance to do good that I am given."
    "Not long after, I was smiling back."
    MC "Heh. And... you think it'll work?"
    show GTS neutral with dissolve
    "She looked away, the faintest pink blooming in her cheeks, and then straightened herself forward."
    pause 1
    GTS "They're good people."
    MC "Hm... yeah."
    jump daymenu

label GTSPRG001:
    scene School Planter with fade
    play music Busy
    "As I was heading to the dorms after class I spotted Naomi and Aida down in the garden."
    MC "Hey girls."
    $setGTSOutfit(OutfitEnum.WORK)
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

label GTSWG001:
    scene Classroom with fade
    play music Schoolday
    "Class was almost done for the day, yet I was decidedly not looking forward to the ending."
    MCT "I probably should've studied more for this..."
    MCT "Alright, last question..."
    MCT "..."
    MCT "I don't know these words."
    MCT "On second thought I {i}definitely{/i} should've studied."
    play sound Bell
    MCT "Crud. Not even five minutes to make something up."
    show HR neutral with dissolve
    HR "Alright, time's up. Hand in your quizzes on my desk on your way out of class."
    show HR unique
    "A collective whiney \"Awwwww!\" from the class sparked in me some bittersweet reassurance."
    show HR neutral
    HR "And no complaining. Two days is plenty of time to prepare for a quiz. You have only yourself to blame if you failed to study properly."
    show HR unique
    "I was in no position to argue, but he could have at least conceded it was way harder than a normal person would expect a quiz to be."
    "I dropped my quiz off on Tashi-sensei's desk on my way out of class."
    scene Hallway with fade
    MC "Fare ye well, GPA, I hardly knew ye."
    "Some of the students were still hanging around outside the classroom. Judging by their dejected looks,"
    show BE sad at Position(xcenter=0.2, yalign=1.0) with dissolve
    extend " most of them must have done about as well as I did."
    show FMG sad at Position(xcenter=0.8, yalign=1.0) with dissolve
    "Not that I gained anything from the misery of others, but admittedly I did feel a bit better knowing I wasn't the only one that bombed that quiz."
    hide BE
    hide FMG
    with dissolve
    show GTS happy with dissolve
    "However, one face stood out among the dour and disappointed expressions."
    MC "Hey, Yamazaki-san. You don't look particularly depressed. I take it you did pretty well?"
    GTS "Good afternoon, Hotsure-san. You deem rightly. I feel particularly satisfied with my performance."
    show GTS neutral
    GTS "It was certainly a challenging quiz, but I was diligent in my preparation and now I enjoy the fruit thereof. How do you feel about your results?"
    MC "Could have... been better."
    MCT "Could have been a lot better, honestly."
    GTS "Indeed? My apologies, I hope I haven't let you down as your study partner. Perhaps we ought to meet a bit more often."
    MC "Well..."
    WG "This is {i}unacceptable{/i}!"
    show GTS surprised at Position(xcenter=0.2, yalign=1.0)
    show WG angry at Position(xalign=0.5, yalign=1.0), Transform(xzoom=-1)
    show PRG scared at Position(xcenter=0.8, yalign=1.0)
    with dissolve
    "We looked over to see Alice staring down Aida while making sharp chopping gestures; the latter looked even smaller than usual with her stiff deer-in-the-headlights expression."
    WG "First I find that my shirt was not properly pressed this morning, only to then realize you accidentally shrunk it in the wash."
    WG "Now I learn, only moments ago, that you failed to write in the upcoming quiz, along with the appropriate study allotment for it, into my schedule this week."
    show GTS angry at Transform(xzoom=-1)
    GTS "{i}Must{/i} you berate Kodama-san so, Nikumaru-san? She had to take the same quiz you did. Your own due preparations surely cannot be her responsibility."
    show WG stern
    WG "Oh? Tell me then, Yamazaki-san, if she is entrusted with keeping my schedule, would that not then fall under her responsibilities?"  
    show WG haughty
    WG "Not that it is any of your business as to what tasks are to be delegated to {i}my{/i} assistant, anyway. Now if you don't mind, this matter doesn't concern you."
    show WG stern
    WG "As I was saying, before being interrupted, your recent performance has not been keeping up with my expectations."
    show PRG sad
    PRG "I-I'm really sorry Alice!"
    WG "\"Sorry\" does not undo the damage caused by poor performance."
    GTS "The only poor performance here is foisting {i}basic{/i} executive function on your whipping boy and haranguing her over the natural results."
    MCT "Oooooooh, this is getting a little heated."
    show WG angry
    WG "Speaking of {i}basic{/i} executive functions. Why don't you just mind your own business? Aida is well compensated for her time and efforts. If you were paying for her services, perhaps I would appeal to you about the matter."
    WG "But since {i}I{/i} am paying for her services, I am well within my rights to express my level of satisfaction with the services rendered, as I see fit."
    PRG "I-It won't happen again. I-I'll do better."
    show WG haughty
    WG "I'm sure you will."
    GTS "Taking advantage of a fellow student like this is far beyond even what I would have ever expected, even from someone who makes their entitlement so readily apparent to everyone around them."
    show WG doubt
    WG "Spare me the theatrics of whatever sense of concern you're attempting to project, because I'm not buying it." 
    WG "As if I should have to hear it from {i}you{/i} of all people. {w}You accuse {i}me{/i} of being entitled, while at the same time thinking I ought to grovel for your approval as to what I choose to do with my own money and efforts."
    show WG haughty
    WG "I don't have to explain myself to you. No one is taken advantage of in a mutually agreed upon business relationship."
    show WG stern
    WG "I don't question how you choose to manage your own wealth. Perhaps you could extend me the same courtesy?"
    GTS "\"Courtesy\", {i}indeed{/i}. Very well, I shall take my leave. Good afternoon, Nikumaru-san."
    show GTS neutral
    GTS "Take care, Hotsure-san, Kodama-san. I believe I shall retire to the gardens."
    hide GTS with dissolve
    menu:
        "Follow Naomi":
            stop music fadeout 5.0
            "I thought about just going back to my dorm after the bitter exchange ended, but instead found myself following behind Naomi."
            scene HallwayStairs 
            show GTS neutral 
            with fade
            play music HigherEdu
            "It wasn't hard— she was going slow, little regarding her surroundings. Nevertheless, as she turned to go out the door to the garden at the bottom of the ramp, her eye drifted to me and she turned."
            show GTS surprised at Transform(xzoom=-1)
            GTS "Oh, hello again. Did you wish to discuss something?"
            MC "Just to ask if you're alright."
            show GTS neutral 
            GTS "I am, thank you. I do apologize for making a bit of a scene."
            MC "I don't know if you did, I was just surprised. I've never seen you have any kind of conflict with anyone. Or express anger at all, for that matter."
            GTS "Well, I'm glad to have made such a good impression up to this point."
            MC "...Oh no, my impression of you hasn't diminished. You were right to stand up for Kodama-san like that."
            $setAffection("GTS", 1)
            GTS "Thank you. It's rather a weakness of mine, but I cannot idly suffer a bully to walk all over an innocent person."
            MC "Is that really a weakness?"
            show GTS embarrassed 
            GTS "After a fashion. Sometimes, to offer a more wholesome perspective is just what a person needs to examine themselves and fortify themselves morally."
            GTS "Sometimes, it is not."
            MC "Ah, right... somebody's gonna lose face."
            show GTS neutral 
            GTS "Correct. Right conduct is at times obscure, and not always without cost."
            MCT "She needs to be either a philosopher or a talk show host."
            MC "So... you really think she's a bully?"
            GTS "I do not believe that monetary compensation makes abuse impossible as Nikumaru-san seems to."
            show GTS angry
            GTS "At least, I pray she sincerely believes that."
            if isEventCleared("GTSFMG001"):
                MC "Does that mean it once again falls to you to fix your classmates' relationships?"
                show GTS embarrassed 
                "Her eyes went wide as if I'd patted her on her pearly cheek, too."
                show GTS neutral 
                GTS "Talk may be proverbially 'cheap', Hotsure-san, but it also has a tremendous capacity to effect change."
                MC "True enough, Yamazaki-san. If you need help with... that, you know where to find me."
                GTS "Kind of you to offer. For today, however, I should not keep you any longer."
            else:
                MC "Maybe she does. I don't think most people who act that way do it for no reason."
                show GTS neutral 
                GTS "That is a fine and generous perspective, Hotsure-san."
                GTS "Regardless, I should think that enough rumination for today. I ought not keep you any longer."
            pause 0.75
            show GTS surprised 
            GTS "Ah! Did you wish to spend some time this afternoon studying together?"
            MC "Oh... yes, actually. I need to get to town to buy some shampoo, but can we meet in about two hours?"
            show GTS neutral 
            GTS "Of course. See you again soon, Hotsure-san."
            "She bowed and resumed passing through the door, leaving me with my thoughts."
            hide GTS with fade
            MCT "It's almost as surprising as seeing her genuinely mad to see how quickly she switches it off."
            MCT "It's like swallowing poison and expecting the other person to die... I bet that's what she'd say."
            MC "Hm."
            "I brought up the bus schedule on my phone and made my way to the entrance, my clarity of thought fading with the afternoon."
            jump daymenu
        "Stay behind":
            $setFlag("GTSWG001_stay")
            show WG neutral at Position(xcenter=0.2, yalign=1.0) with move
            WG "As I was saying, before being interrupted {i}repeatedly{/i}, I am sure you will do better, Aida. I understand you are new to this role and do not have the years of professional experience of my usual assistants."
            WG "It is to be expected there will be some snafus during the initial onboarding; however, I expect them to be increasingly infrequent and smaller in magnitude." 
            PRG "R-Right, understood Alice."
            WG "That being said, apart from today's uncharacteristic lapse, your performance thus far has been keeping with my expectations. I have no doubts you are the right person for the job."
            show PRG neutral
            PRG "T-Thank you, Alice."
            show WG haughty
            WG "This incident however has brought to my attention that there is much for you to learn and that I need to be more diligent in cultivating your skills."
            WG "Now, with all of that being said, there is no need to dwell on this incident further. Let us proceed with our scheduled afternoon tea."
            show PRG excited
            PRG "Y-Yes, that sounds fun."
            show WG doubt 
            "It appeared I caught Alice's attention as she half-turned to face me, nakedly annoyed."
            WG "And do {i}you{/i} have something to say now?"
            MC "Uh, no, not really."
            show WG haughty
            WG "Splendid. Goodbye, Hotsure-san."
            MC "See you later."
            show WG neutral 
            "I replayed the whole encounter in my head as I walked away."
            hide WG
            hide PRG
            with dissolve
            MCT "Hm... afternoon tea? That was unexpected."
            MCT "Unlike her and Naomi together. I didn't think they'd get along, but sheesh."
            MCT "Well... guess I'd better start hitting the books again..."
            jump daymenu
