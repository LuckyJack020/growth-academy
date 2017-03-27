define GTS = Character('Naomi', color="#66FF33")

image GTS neutral = DynamicImage("Graphics/GTS-[globalsize]-neutral.png")
image GTS happy = DynamicImage("Graphics/GTS-[globalsize]-happy.png")
image GTS sad = DynamicImage("Graphics/GTS-[globalsize]-sad.png")
image GTS surprised = DynamicImage("Graphics/GTS-[globalsize]-surprised.png")
image GTS angry = DynamicImage("Graphics/GTS-[globalsize]-angry.png")
image GTS aroused = DynamicImage("Graphics/GTS-[globalsize]-aroused.png")

init python:
    #mostly linear for now
    eventlibrary['GTS001'] = {"name": "GTS001", "girls": ["GTS"], "location": "schoolplanter", "conditions": [], "priority": 0}
    eventlibrary['GTS002'] = {"name": "GTS002", "girls": ["GTS"], "location": "schoolplanter", "conditions": [[ConditionEnum.EVENT, "GTS001"]], "priority": 0}
    eventlibrary['GTS003'] = {"name": "GTS003", "girls": ["GTS"], "location": "cafeteria", "conditions": [[ConditionEnum.EVENT, "GTS002"]], "priority": 0}
    eventlibrary['GTS004'] = {"name": "GTS004", "girls": ["GTS"], "location": "library", "conditions": [[ConditionEnum.EVENT, "GTS003"]], "priority": 0}
    eventlibrary['GTS005'] = {"name": "GTS005", "girls": ["GTS"], "location": "hallway", "conditions": [[ConditionEnum.PRESET]], "priority": 0}
    eventlibrary['GTS006'] = {"name": "GTS006", "girls": ["GTS"], "location": "schoolfront", "conditions": [[ConditionEnum.EVENT, "GTS004"]], "priority": 0}
    
label GTS001:
    scene black with fade
    "The words from Tashi-Sensei stayed with me long after class had concluded. I just wasn’t sure how to properly process what we were told."
    "What Daichi had told me earlier was starting to resonate more and I began to wonder if perhaps others knew about the purpose of this school before they were enrolled into it."
    scene School Planter with fade
    "I hadn’t realized how long I was lost in my own thoughts until I finally noticed my surroundings; I was at the school’s garden."
    "It was nice here, the breeze along with the sounds of leaves and grass moved by the flow of wind had a sort of calming factor to them."
    "I stood there for a few moments longer until a figure walked beside me, catching me by surprise."
    show GTS neutral with dissolve
    MC "Huh? Oh Naomi. sorry, I wasn’t aware you were here."
    GTS "It’s alright Keisuke. I shouldn’t have intruded unannounced."
    "She stood there, smiling ever so slightly, the flow of wind causing her long hair to dance ever so tenderly until I decided to break the silence."
    MC "So what are you doing here in the garden?"
    GTS "Oh, I merely wanted to spend a little more time here. Reflect on my thoughts and think about how the day went so far."
    MC "I see, were you also possibly thinking about what Tashi Sensei told us earlier?"
    GTS "A little yes, I think many of the students are. Were you as well?"
    MC "Yeah I was. It really came out of left field so I guess I needed some time to think about it."
    menu:
        "What do you think about it?":
            jump GTS001_c1
        "I'm curous about what changes I might go through...":
            jump GTS001_c2
        "I’m concerned about what that might mean for my little sister honestly.":
            jump GTS001_c3
            
label GTS001_c1:
    GTS "It’s a little concerning I will admit; however, I think some of those feelings come from the sudden nature in which we were told."
    GTS "I’m sure if we take more time to process it and reflect on it, the situation won’t feel as frightening as it possibly does for some."
    extend " Thank you for asking though."
    MC "No problem, we’re all in this together, after all right?"
    GTS "An interesting way to put it, but indeed I would say so."
    jump GTS001_after

label GTS001_c2:
    GTS "It’s good to see you’re looking at the news with more curiosity rather than concern. It’d be rather pointless to worry about it now, especially without knowing all the facts first."
    extend " I’m sure they have methods to tell what will be changing in us, though I’m sure with some students it’d be more obvious than others."
    extend " Oh sorry! That sounded rather rude didn’t it? I don’t mean to judge any of the other students."
    MC "Heh, it’s okay Naomi I can tell you’re not the type to do that."
    GTS "Thank goodness, I wouldn’t want to start making the wrong impression on the first day of school after all."
    jump GTS001_after

label GTS001_c3:
    GTS "Oh? You have a younger sister Keisuke?"
    MC "Yeah, she’s going to school here too."
    extend " I’m just thinking about what Sensei said, about how sometimes siblings are transferred to this school simply because of the results of the other."
    extend " I’m sure I can cope with whatever might happen to me, but I’m worried about her. I just don’t want her to go through something that might hurt her."
    GTS "It’s only natural to worry as the older sibling Keisuke, but you mustn’t let it concern you too much. There’s no way to know for certain at the moment, so it’s best to just be hopeful and keep your chin up."
    MC "Yeah I guess that’s true. Sorry for sounding like a mother hen here."
    GTS "It’s not worry Keisuke, like I mentioned it’s just natural to feel that way. I know I’m very much the same with my own sister."
    MC "You have a sister too?"
    GTS "Yes, she’s much younger though so there’s no worry about her predicament in this situation. But just know that you’re not the only one who can sometimes come off as a mother hen."
    jump GTS001_after

label GTS001_after:
    "She gave a soft chuckle and kept her warm smile."
    "I guess she must have noticed me staring, because she soon chimed in."
    GTS "It’s quite rude to stare."
    "There was a hint of red on her cheeks as she said that."
    MC "O-Oh! Sorry... I was just thinking again haha... so are you going to be doing anything else later today?"
    "She placed a finger on her lip as she thought about her plans for the evening before finally replying."
    GTS "Well I had planned to return to my dorm room so I can tell my family about how my first day went. I just wanted to see the garden a little bit before I did so."
    GTS "However, I do plan to explore the garden later this evening. There’s a surprisingly large variety of flowers here."
    extend " At least more than I would expect so I want to make a mental list of what’s here and maybe ask the groundskeeper about where they obtained the seeds for them."
    MC "Oh I see; I won’t hold you up then. I should probably do the same myself really. I’m sure my family would love to hear about how my day went as well. I’ll see you around Naomi."
    GTS "Farewell Keisuke, I hope the rest of your day goes well. Do try to visit the garden every so often, you’ll be surprised how much good can come from resting in a garden for a few moments."
    MC "Heh, I might take you up on that advice. Later Naomi."
    "She gave me a small bow before I departed."
    jump daymenu

label GTS002:
    scene School Planter with fade
    "I always found the sky to have quite the alluring palette around late afternoon. Clouds coated to degrees of red that ranged from rose color to pink and even orange and yellow. And while I normally didn’t find myself staring up at the sky, it was simply something I couldn’t resist as I step into the school’s garden once more."
    "The breeze had become cooler but still flowed with a sense of gentleness to it. Making some pink colored flowers dance before me. In the distance, I heard a faint voice and as I turned to look I spied Naomi giving a gracious bow to who I assumed was the gardener."
    MC "Yo Naomi!"
    show GTS neutral with dissolve
    "I called out, lifting one arm up to give a slight wave. This seemed to surprise her as she jumped a little and looked back towards me. Giving a small nod, she walked over with a few small bags held against her bust by her arm."
    GTS "Hello again Keisuke, I’m sorry you startled me a little there."
    MC "Heh, sorry. I just wanted to make sure you heard me. I see you talked to the gardener."
    "She blushed very faintly and gave a gentle nod."
    GTS "I did yes, he’s quite a nice person to speak to. I was just asking about the flowers and before we knew it we got wrapped up in a rather long conversation about them and other plants. He even gave me some for free."
    "She shifted her arm a little to draw my attention to the three bags she was carrying."
    menu:
        "Oh, that's cool. How did the rest of your day go?":
            jump GTS002_c1
        "Really? That was cool of him. What kind are they?":
            jump GTS002_c2

label GTS002_c1:
    GTS "Hm? Oh, the rest of my day was rather peaceful. I spoke with my family as I mentioned earlier and they seemed rather happy to hear from me."
    MC "That’s good to hear, did you happen to mention what you thought about the news we got earlier?"
    "She was silent for a moment as if reflecting on that question before she answered me."
    GTS "No, I didn’t. I don’t see a reason to mention it to them. Without any knowledge, all it’d accomplish is make them worry about me needlessly. I will be sure to discuss my feelings about it to them when we learn more about it ourselves and I know exactly what to expect."
    MC "Yeah I guess that’s true... So, did you do anything else?"
    "She shook her head softly."
    GTS "No, not much else really. Basically, just made sure everything was completely unpacked and organized. Then I came here and well you know where that part leads."
    jump GTS002_after
    
label GTS002_c2:
    "Her eyes brightened ever so slightly at that question as her smile grew a little larger."
    GTS "Indeed, it was rather nice of him. Well as for the flowers themselves. These ones are Burūberu (Bluebells), a lovely plant with quite the bold color. They’re known to symbolize gratefulness."
    "She handed the bag to me, allowing me to see the blue bell like shape they had on the cover of the bag."
    GTS "Now this breed here is the Tsutsuji (Azalea) which you might have seen here at the garden."
    "She pointed over to the pink flowers I had seen when I first entered the garden. The second look allowing me to notice the purplish patterns within the petals of the flower."
    GTS "They’re popular here in Japan with a flower festival which showcases them in Motoyama taking place each year on March 25th. They’re known to symbolize patience and modesty."
    "She handed me this bag as well as I was soon finding myself carrying her flowers for her."
    GTS "Now these last ones may seem rather plain due to their simple color, but you’ll be surprised the amount of color variety you’ll find with Anemones. Though the white ones are the one’s you’ll usually find here in Japan. Their name is Greek, meaning 'Daughter of the wind' and they represent Sincerity."
    "As she handed me the last bag which displayed white 5 petal flowers I could see her smiling warmly as she finished explaining."
    MC "Heh, I can tell you really have a thing for flowers huh?"
    "Her smiled quickly vanished and instead a light blush formed across her cheeks."
    GTS "O-oh yes, indeed I do. Sorry for getting rather carried away there. I didn’t mean to just ramble on like that. I surely hope you don’t mind."
    MC "Not at all, it’s nice to learn a little bit about you really. I also admit it was interesting to learn a bit about these flowers as well. I wasn’t aware they have hidden symbolic meanings."
    "She continued to smile, but became more reserved, as if to not allow herself to accidentally get too excited again."
    GTS "They do yes, but I wouldn’t want to take up more of your time chattering about my interests."
    jump GTS002_after
    
label GTS002_after:
    GTS "How did the rest of your afternoon go, if you don’t mind my asking?"
    MC "Taking what we learned about ourselves earlier aside, the rest of my afternoon was actually pretty good. I spoke with my family and told them I’m fine.  I then took some time to learn a bit more of the school and found out there’s a sports club. I might give them a look and see if I can join in the future."
    "She nodded her head as I spoke to her, taking in everything I was saying attentively. It felt rather nice honestly, knowing that she was truly listening to me as she kept eye contact with me during the entirety of my small ramble."
    GTS "What sport are you interested in Keisuke?"
    MC "Oh, I’m rather interested in Soccer. I might give it a shot later this year if my condition doesn’t hinder it in some way."
    "I chuckled lightly, kind of realizing that we couldn’t plan our futures for the moment. Without any knowledge about what might happen to us, everything was up in the air. I pushed that thought to the back of my mind though."
    GTS "Hopefully you’ll be able to do so Keisuke. Soccer has always seemed like a rather enjoyable sport, a lot of endurance needed so it’s good exercise. I wish you luck Keisuke."
    "She gave me another soft warm smile that made me smile in return as I scratched the back of my head."
    MC "Heh, Thanks. Well it’s getting rather late and I don’t want to keep you from any plans you possibly have with your flowers, so I think I’ll be heading off now. Before I go though, do you need any help with those?"
    "I ask, point to the small bags of seeds she had with her. This caused her to give the slightest of giggles as she shook her head lightly."
    GTS "No, I’m okay thank you. It was nice speaking with you again though Keisuke. Hopefully we’ll talk again soon."
    MC "Yeah, hopefully. I’ll catch you later Naomi."
    GTS "Have a pleasant evening Keisuke."
    "She replied before once again giving me a light bow, yet this time it was her who left first. I couldn’t help but smile at the small conversation we had, slightly curious about where I might bump into her again."
    jump daymenu

label GTS003:
    scene Cafeteria with fade
    "The morning found itself to be quite the chaotic time as many students rushed down the corridors to make it to the Cafeteria to beat the morning rush. This didn’t really pressure me to speed up my stride however."
    "When I finally arrived to the cafeteria I saw that it was surprisingly calmer than what was transpiring throughout the hallways. I got in line behind a few other students who were getting their breakfast, which allowed me time to properly examine what was on the menu."
    "I will admit I was rather surprised by what I saw. Instead of finding precooked items like eggs or fish, I saw the cook personally making each item that was requested by the students. By the time it was my turn in the line I was slightly uncertain of what I wanted."
    "Not wishing to hold up the line though, I quickly ordered what I felt would be a decent quick breakfast, getting some steamed rice, a rolled omelette, and a small bowl of miso soup. I thanked the cook before searching for a place to sit."
    "There was a good amount of unfamiliar faces among those sitting at various tables, but one face was rather familiar. Sitting down with a slight smile, I spoke to my neighbor."
    show GTS neutral with dissolve
    MC "Hey there, Naomi. Nice to see someone I know here."
    "I must have startled her again as she flinched slightly and looked up at me."
    GTS "Good morning Keisuke. I hope you had a pleasant morning so far."
    "She answered back, her hands gently repositioning her utensils and her napkin in an extremely orderly fashion before wiping off her hands with a moist towelette. She then looked at me as if to give me a hint as I had almost forgotten."
    GTS "Itadakimasu."
    MC "Itadakimasu." #I wonder if there's a good way to convey both of them saying it at the same time?
    "We both stated thankfully, before I finally answered her."
    MC "Yeah it’s been a pretty good morning so far, I managed to wake early so it gave just the right amount of time to fully wake up, which is a pretty good start of the day in my opinion. Thankfully since I woke up so early it allowed me to shower without being disturbed by anyone."
    "I stated with a slight chuckle as she gave a small smile in response before picking up her chopsticks. Her hand softly slid her hair back as she picked up some cooked vegetables to eat. This let me notice that her other bang was currently held back by a flower shaped hairclip."
    "I had no idea what type of flower it was, only knowing that it had 5 white petals in a sort of star configuration."
    MC "How was the start of your day if you don’t mind me asking?"
    "Naomi perked up lightly as I asked my question, taking her napkin to delicately wipe her lips and properly placing it back in place."
    GTS "Myself? Well, I woke up rather early as well and took the time to properly make my bed. I then showered and prepared myself for the rest of the day. Things like properly combing my hair, getting everything organized, and planning out my schedule for the day."
    GTS "I think it’s good to take the time in the morning to plan the day, allows you to optimize the time you spend as well as get your brain working early on in the day."
    "She grew a little quiet as if worried she overstepped her bounds by stating her opinion."
    MC "I can see that yeah. Gets the juices flowing and your mind ready for more work, so I think it’s a good analogy."
    "She gave me another small smile as she learned that I agreed with her before she went back to have another piece of her meal."
    "This time I noticed how she used her chopsticks to take an almost perfect rectangular piece out of some of her grilled fish, she then carefully took some steamed rice and pieced it atop it before eating both. Her movements seemed so precise and slightly rigid that it was slightly captivating as I never seen someone eat so strictly."
    menu:
        "That’s a cute hairclip, though I’m not sure what type of flower that is. What kind of flower is it?":
            jump GTS003_c1
        "I mean no offense, but you have a very interesting way of eating.":
            jump GTS003_c2

label GTS003_c1:
    "For the briefest of moments I could see Naomi’s cheeks flash a slight crimson in what I assumed was embarrassment as her hand went to touch the accessory. She looked away for a second but returned her eyes back to mine and retrieved that small smile she had before."
    GTS "Oh, why thank you so much. It’s just a little something I decided to add to the rest of my attire for today. I have a bit of a collection of them, various species and things of that nature."
    MC "Well I think it suits you rather well."
    GTS "Thank you..."
    GTS "As for your question, this flower is a Jasumin (Jasmine) which do tend to confuse some people since they happen to look slightly generic."
    MC "I will admit it does look like what most people picture as a flower in their heads."
    "She gave me a small nod of confirmation to my remark before continuing."
    GTS "Well Jasumin does come in other forms, like the Grand Duke of Tuscany which almost resembles a white rose, to those that look much like the one in my hair. China even uses it as an ingredient for their teas."
    MC "Really? Which one?"
    GTS "Jasmine tea."
    MC "Oh... I guess I should have put that together."
    "I scratched the back of my head, feeling a little silly now but she didn’t seem to mind my mental trip, simply answering me as if it were any other question."
    GTS "They’re known to symbolize friendliness and gracefulness."
    MC "Seems like it suits you rather well then."
    "This caused her blush to return once more as her eye contact finally broke to look at her food."
    jump GTS003_after

label GTS003_c2:
    "Her body stiffened up lightly as I brought mention towards her table etiquette as she looked me in the eyes."
    GTS "How do you mean?"
    MC "I just mean that the way you conduct yourself it’s very stiff but also very formal."
    GTS "Well it was how I was raised. It’s important for one to keep proper posture and etiquette when eating. You don’t want to come off as rude unintentionally after all."
    MC "Heh, well you don’t have to worry so much about being so formal around me. You can relax."
    GTS "I see, I’ll keep that in mind, though if you don’t mind I would like to move pass the subject."
    MC "Heh... yeah okay. Sorry about that."
    GTS "It’s fine."
    jump GTS003_after

label GTS003_after:
    "We ate for a few moments in silence after that. It was rather nice to have someone to eat with, even if we weren’t having much of a conversation at the time. As we finished I had decided to ask Naomi."
    MC "So is there any particular subject you’re looking forward to this year?"
    GTS "I think Science should be rather fun this year, how about yourself?"
    MC "I’m not too sure yet, but I can tell you already that I’m dreading the thought of math."
    GTS "Not much for math?"
    MC "I’m horrible at math, but maybe this year I’ll get lucky."
    "She gave me a small nod and smile as she stood up from the table, collecting her tray."
    GTS "I wish you good luck then Keisuke."
    MC "Why thank you ma’am and I wish you luck with science."
    "I replied which caused her to give me a small chuckle in response. She gave a small bow and walked off as I gathered all my things."
    jump daymenu
    
label GTS004:
    scene Library with fade
    "The sun shone highly in the sky as the middle of the day came by. It’s rays seeping through the many windows that surrounded the vast two floor room. I’ll be honest, I was a little surprised to see so many people using the library found on campus."
    "To its credit, both floors seemed absolutely packed with shelves upon shelves of books. Which in turn would make one aisle look like the splitting of the red sea but with books as opposed to water. This didn’t mean that every part of the library was stuck in the past as there was a series of smaller rooms that have lines of computers for more convenient research and study."
    "Something else that was rather clear was just the amount of space found between each shelf as it seemed capable of easily fitting six people across the width of the aisle. The reason for this was easy to put together, but it did leave me with the thought of just how large some of the students might become if this was the norm for the school."
    "As I walked among the shelves in search of the right book needed for my Contemporary Society course, I spotted a familiar face at a nearby table."
    show GTS neutral with dissolve
    extend " Naomi was seated with her focus entirely on her book as she seemed somewhat perplexed by what she was reading. Unable to resist, I strolled over to Naomi and suddenly spoke up."
    MC "Hey there!"
    "This caused Naomi to jump and cup her chest as she was yanked out of her studying. She looked up at me and sighed slightly in relief, though her expression showed she hadn’t taken joke too well."
    GTS "Please don’t do that."
    "She said politely, though the inflection in her voice was laced with annoyance as she recomposed herself. Her eyes never left mine as I scratched the back of my head and took a seat across from her."
    MC "Sorry sorry, I just couldn’t resist a little startle."
    "I had a small chuckle which caused her to narrow her eyes a little but she eventually seemed to settle down as she looked at the book I had placed down. I had an opportunity to see what she was reading herself, seeing the symbols that showed what appeared to be another language."
    MC "What language is that? English?"
    "She gave me a nod in response and shifted her book slightly so I’d be able to see it better."
    GTS "I’m trying to get a bit more studying of it done on my free time. Just get a better understanding of it for myself."
    MC "That’s neat, are you planning to visit the United States in the future?"
    GTS "I can’t be certain truthfully, but I think it’s best to be prepared for it in case it ever happens. It’s also a good skill to have if your work might require it or if you might have international guests."
    MC "Heh, that’s quite the foresight to have. I barely even think about what I’ll be doing in a month from now. Hey, if you manage to make it work though that’s one massive advantage you’ll have over others in the job field so good luck!"
    GTS "Thank you."
    "She showed hints of a smile as I wished her luck."
    MC "How well did you take in what we learned in homeroom today?"
    "She gave the smallest sigh as she reached to her back and retrieved a rather large book."
    GTS "Unfortunately, not as well. Science is proving that it might be harder than I originally thought. As you know, our professor seems rather adamant that we start of the year sooner rather than later and the crash course we were given made it a little difficult to retain all the information we went over regrettably."
    MC "Well I don’t think we’re expected to get everything memorized from the start. I’m sure it’ll ease up a bit in the next few days."
    GTS "We were told that we’d be given a quiz at the end of this week so I can’t afford to fall behind. I’ll just have to shift my focus a bit, keep my English studies to an hour while devoting more of the afternoon to this."
    MC "Heh... Why not just get a study partner? I remember when I was younger one of my teachers told me that the best way to learn and retain knowledge was to teach others. So, if you have someone who you can bounce information to and maybe even quiz then you’ll understand it better. After all, if you’re making the quizzes then that means you have the answers already."
    "She placed her hand on her chin as she seems to consider that option."
    GTS "I’m not sure, I’d hate to impose on anyone and add to their studies."
    MC "Well then. I volunteer!"
    "I said in exaggerated fashion, though she quickly put a finger over her lips as I had just remembered we were in the library. Chuckling nervously, I decided to repeat myself in a more subdued fashion."
    MC "Oops. But yeah, I’ll be glad to help you out."
    GTS "Are you sure? I feel bad asking you to take time out of your schedule simply to help me."
    MC "Don’t worry, it’s fine. Plus, I get to learn more so it’ll help me out a lot too."
    GTS "Hmm. Oh, how about I help you with one of our other subjects then? Is there any you think will be an issue?"
    MC "Math. Haha, it’s going to be math, I can already tell that’s going to be a disaster for me this year."
    "She gave a light giggle though covered her mouth ever so slightly."
    GTS "Well that’s something I know I can help you with. Very well then, I accept your help and am pleased you accept mine as well."
    "She extended her hand for me to shake to solidify our agreement. Taking her hand into mine, I gave her a smile and shook."
    MC "Glad to be of assistance study partner. Let’s get this done!"
    Student1 "Sssh!"
    "We both tensed up as someone at another table once again reminded me of my surroundings. Naomi was blushing slightly but neither of us could stop a small giggle from slipping out as we started working more quietly."
    jump daymenu

label GTS005:
    scene Hallway with fade
    "I wandered about the campus for quite some time after visiting the nurse. The news of my particular condition leaving me with a feeling of uncertainty. As I walked, my hand would occasionally touch the tip of my bangs as I wondered just how quickly they might change."
    "As I stepped pass the double doors, my eyes shut from the blast of sunlight that I was exposed to. After a few seconds my eyes would readjust and I’d see Naomi’s form kneeling in front of a patch of flowers. Calmly walking over, my footsteps on the path alerting her to my presence as she looked back at me and gave a soft wave."
    show GTS neutral with dissolve
    GTS "Hello there Keisuke."
    MC "Hey Naomi. How are you doing?"
    "I ask as she stands up and dusts off her legs before returning her full attention to me."
    GTS "I’m doing well. I came here to do some reflecting and thinking. I feel rather inattentive though, I somehow had missed this small patch of Botan flowers here."
    "I looked pass her to the flower patch behind her to see the pink plants."
    MC "Botans huh? I thought they were roses honestly."
    "She gave me a soft smile but shook her head slightly."
    GTS "It’s a common mistake, they do have a somewhat common appearance so I can see how you’d make that assumption. One way to tell the difference is that botans have a lot more petals and because of that are a bit puffier looking. I like to think of them as wedding gowns personally, the petals being the ends of the gown that swirl towards the middle which is the bride."
    MC "That’s quite the romance way to look at it."
    "This made her cheeks redden a bit as she tried to move pass that statement."
    GTS "Apologies, I didn’t ask how you were doing. I can never seem to stop talking about flowers with you it seems."
    menu:
        "Hey, you have a passion for it, I can’t fault you for that.":
            jump GTS005_c1
        "I’m doing okay, thinking about the results from the test.":
            jump GTS005_c2

label GTS005_c1:
    MC "Hey, you have a passion for it, I can’t fault you for that."
    GTS "Thank you, I just don’t wish to come off as annoying or disinterested in talking about you."
    MC "Heh, you worry too much about that. It’s fine to talk about what you like, that’s what friends do."
    GTS "I... I see. Thank you again."
    MC "What else can you tell me about Botans?"
    GTS "Well, I know that their name in other countries is peony and that they symbolize having bravery and courage. Besides looking rather lovely they are commonly used in some herbal medicines which makes them a somewhat common flower."
    MC "That’s pretty cool actually, both cute and helpful."
    "She smiled in return."
    GTS "Yes, very much so I would say. That’s a nice way to see it."
    jump GTS005_after
    
label GTS005_c2: 
    MC "I’m doing okay, thinking about the results from the test."
    GTS "Yes... I would think quite a few students are thinking about that. I assume that’s why the campus is a bit quieter than normal."
    MC "Yeah, I think a lot of people are trying to come to terms with what’s going to happen to them. I’m not really sure how I feel about my condition though, it’s rather strange if I say so."
    GTS "Strange in what way?"
    MC "Well I’m basically going to turn into Cousin It heh."
    GTS "Cousin... It?"
    "She tilted her head in confusion as it was clear that reference flew well over her head."
    MC "Heh... never seen that show or movie huh? Well basically cousin it is a character from the Addams Family who was basically a mass of hair that came from the top of his head and completely covered his body. In other words, apparently, my hair is going to grow a lot and rather quickly. So, I had better learn how to cute my own hair or else I’ll be spending a ton of money just so people can see me."
    GTS "Oh my, yes, I can see how that’d be an issue. Not to mention caring and maintaining it."
    MC "Yeah... that’s a lot of hair products I’m going to have to learn about. But hey, at least I can cosplay any character I want now since I’ll always have the right amount of hair for it."
    "I said with a grin, trying to be positive which in turn made her giggle and nod her head in agreement."
    GTS "Yes, that is one plus. Not to mention you’ll be able to change your style to whatever suits you, letting you accessorize more ways than others would be able to."
    "I showed her my smile which made her smile back as she seemed to enjoy my positive outlook at the news of my condition."
    jump GTS005_after

label GTS005_after:
    MC "So, what did you hear from the nurse?"
    "The happy mood on Naomi’s face seemed to have left with those words as she looked back at the floors for a moment then looked back at me."
    GTS "Well, my condition is rather unique. That’s not to say the others aren’t as well, I don’t want to minimize the problems others may have. It’s just, I don’t really see many with what they say I have."
    MC "Is it bad?"
    GTS "I don’t believe so. At least I don’t know and am not sure how one would tell. My results showed that I’ll start growing taller over the course of the year."
    MC "Really? Yeah, that is a tricky one. Do they know how much?"
    GTS "No. There are estimates but one can never be truly certain."
    MC "Well I think you’ll be okay, after all that’s what this school is here for. To help anybody with any issues."
    "This did bring a small smile back to her as she looked back up at me."
    GTS "Yes, you’re right. Thank you, Keisuke. It does help knowing that I will have help with this."
    MC "Yep! And I’m here to help you too! So, don’t hesitate to ask for anything, or rant more about your flowers."
    "I gave her a teasing smirk as she gave back a playful pout but did smile."
    GTS "I don’t rant about flowers... not that much anyway."
    "We both had a small chuckle as we spent a bit more time just talking in the garden."
    jump daymenu

label GTS006:
    scene School Front with fade
    "There was a quite calming mood to the start of the school day as I wandered near the entrance. Something caught my eye though as I saw what appeared to be a small gathering of students near the front gate. Curious, I wandered over, hearing some excited voices and sounds of affection. The reason for this became clear rather quickly, as it seemed a stray Shiba Inu Puppy had wandered onto the campus."
    Student1 "It's so adorable!"
    Student2 "D'aww! Look at his little paws!"
    "The crowd grew every couple of seconds as more people wanted to see what the commotion was all about. As I kept watching, I saw a familiar figure kneel next to the excited puppy and begin petting it. Naomi held a warm smile on her face as her hand massaged the puppy's ears and even rolled him over to rub his belly. This caused the entire crowd to gush over the cuteness and I couldn't resist a smirk."
    "A little time passed before the dog's owner finally showed up and thanked everyone for finding their dog before taking it back home. As the crowd dispersed I saw Naomi walk by and notice me. Giving me her trademark smile she gave me a small wave of her hand."
    show GTS neutral with dissolve
    GTS "Hello Keisuke, did you see the adorable Shiba Inu that had wandered onto campus?"
    MC "Yeah, I did, well I saw the crowd first and had to see what was up."
    GTS "It was such a cute puppy, and very well behaved. Didn't you think so?"
    menu:
        "Kind of, but I'm mostly into cats myself.":
            jump GTS006_c1
        "Yeah, he was extremely cute!":
            jump GTS006_c2

label GTS006_c1:
    MC "Kind of, but I'm mostly into cats myself."
    GTS "I see, well cats are rather adorable too. Though I always enjoyed the companionship of a dog."
    MC "Yeah, I hear a lot of people are a big fan of how loyal dogs can be. Personally, I enjoy the peace and quiet a cat offers. Plus, they’re so cute!"
    "Naomi gave a little giggle and covered her mouth at that last bit but nodded her head."
    GTS "Sorry, I didn’t mean to laugh, it’s just rather cute seeing that."
    "My cheeks felt a little warm as I rubbed the back of my head."
    MC "What can I say, little cute fluffy things just get to me."
    jump GTS006_after

label GTS006_c2:
    MC "Yeah, he was extremely cute!"
    GTS "Indeed, he was, did you get a chance to play with him?"
    MC "Not really, too big of a crowd and I don’t think it’d be wise to make a scene by barging through everyone to pet him."
    "This made Naomi giggle softly and nod."
    GTS "That’s very true, but I don’t think many people would hold it against you with such an adorable puppy on the other side."
    MC "Yeah... man I wish I had a dog like that."
    GTS "Oh? Never owned a pet before?"
    MC "Nah, our place was always a bit too small for something like a dog, at least the ones my parents like. Plus, we were all mostly too busy to begin with, so it probably was for the best."
    jump GTS006_after

label GTS006_after:
    MC "So what about you? Have you ever had a pet?"
    GTS "Yes actually, we have a Hokkaido."
    MC "Whoa seriously!? Aren’t those extremely rare?"
    GTS "I’ve never heard that, but I suppose they could be. I always thought they were rather common since SoftBank uses one as a mascot."
    MC "I don’t know, I’ve always heard they’re really rare, even in Japan. Your family must be loaded!"
    "There was the faintest hint of a blush on Naomi’s face as she broke eye contact and looked to the side for a second before returning her attention."
    GTS "My father always said he picked that breed because the Hokkaido has the three characteristic he looks for in people, bravery, loyalty, and intelligence. I can say he was right about that description, because she’s probably been one of the most loyal dogs I’ve met."
    MC "She? So it’s a girl."
    GTS "Oh yes! Sorry, yes she’s a girl. Her name is Kimiko and she has wonderfully white fur. She’s been with the family for about 5 years now."
    MC "I see, that’s pretty cool. I bet you can’t wait to see them again."
    GTS "Yes, I do miss her a bit more than I thought, but I plan on heading home this weekend so I’ll be seeing her soon enough."
    MC "That’s good to hear. Hmm, maybe I should see if I should go home this weekend too."
    GTS "Small breaks from school can do the mind a lot of good."
    MC "Yeah, especially with what we will be dealing with here over time. Yeah, maybe I’ll pay home a visit sometime soon."
    "I got a small understanding nod from Naomi and a small yet warm smile."
    GTS "If you’ll pardon me Keisuke. I believe we’re already close to being late for class. It might be best to start heading to our home room."
    "I quickly looked at my watch and then chuckled."
    MC "Oh yeah... heh, I kind of lost track of time. Yeah let’s get going. Maybe if I’m lucky I’ll get a chance to see that puppy again someday."
    GTS "Maybe."
    "She replied with a small giggle as we began walking to class together."
    jump daymenu
