define BE = Character('Honoka', color="#FCCF20")
define Sakie = Character('Sakie', color="#C0C0C0")
define Koneko = Character('Koneko', color="#C0C0C0")
define Coach = Character('Coach', color="#C0C0C0")
define Waitress = Character('Waitress', color="#C0C0C0")

image BE neutral = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE/2/neutral.png",
    "True", "Graphics/BE/1/neutral.png")
image BE happy = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE/2/happy.png", 
    "True", "Graphics/BE/1/happy.png")
image BE sad = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE/2/sad.png",
    "True", "Graphics/BE/1/sad.png")
image BE surprised = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE/2/surprised.png",
    "True", "Graphics/BE/1/surprised.png")
image BE angry = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE/2/angry.png",
    "True", "Graphics/BE/1/angry.png")
image BE aroused = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE/2/aroused.png",
    "True", "Graphics/BE/1/aroused.png")
image BE unique = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE/2/unique.png",
    "True", "Graphics/BE/1/unique.png")

image cg BE001 = "Graphics/ui/gallery/BE-001.png"
image cg BE002 = "Graphics/ui/gallery/BE-002.png"

image Dorm BE = ConditionSwitch(
    "gametime_eve", "Graphics/ui/bg/BEdorm_eve.png",
    "True", "Graphics/ui/bg/BEdorm_day.png")
image Sushi Restaurant = "Graphics/ui/bg/sushirestaurant.png"

init 2 python:
    datelibrary['BE001_deadline'] = datetime.date(2005, 4, 13)
    datelibrary['BE007_deadline'] = datetime.date(2005, 4, 13)
    datelibrary['BE_size_6'] = datetime.date(2005, 12, 10)
    datelibrary['BE_size_5'] = datetime.date(2005, 12, 10)
    datelibrary['BE_size_4'] = datetime.date(2005, 12, 10)
    datelibrary['BE_size_3'] = datetime.date(2005, 12, 10)
    datelibrary['BE_size_2'] = datetime.date(2005, 4, 20)
    
    eventlibrary['BE001'] = {"name": "Rooftop Reunion", "girls": ["BE"], "location": "roof", "time": (TimeEnum.NIGHT, WeekendEnum.WEEKDAY), "priority": False, "startdate": "day_0", "enddate": "BE001_deadline",                               "conditions": []}
    eventlibrary['BE002'] = {"name": "Campus Collision", "girls": ["BE"], "location": "campuscenter", "time": (TimeEnum.ANY, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "testday",                                   "conditions": []}
    eventlibrary['BE003'] = {"name": "Cool Drinks with Honoka", "girls": ["BE"], "location": "campuscenter", "time": (TimeEnum.AFTERSCHOOL, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",                    "conditions": []}
    eventlibrary['BE004'] = {"name": "Chatting at Soccer Practice", "girls": ["BE"], "location": "track", "time": (TimeEnum.AFTERSCHOOL, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",                       "conditions": []}
    eventlibrary['BE005'] = {"name": "Possible Clubs", "girls": ["BE"], "location": "classroom", "time": (TimeEnum.ANY, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",                                        "conditions": [[ConditionEnum.PRESET]]}
    #eventlibrary['BE006'] = {"name": "BE006", "girls": ["BE"], "location": "classroom", "conditions": [], "priority": 0}
    eventlibrary['BE007'] = {"name": "Lunchtime with Honoka", "girls": ["BE"], "location": "cafeteria", "time": (TimeEnum.DAY, WeekendEnum.WEEKDAY), "priority": False, "startdate": "day_0", "enddate": "BE007_deadline",                      "conditions": []}
    eventlibrary['BE008'] = {"name": "Manga Breaktime", "girls": ["BE"], "location": "dorminterior", "time": (TimeEnum.AFTERSCHOOL, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",                            "conditions": []}
    eventlibrary['BE009'] = {"name": "Goal(s)!", "girls": ["BE"], "location": "track", "time": (TimeEnum.ANY, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",                                                  "conditions": []}
    eventlibrary['BE010'] = {"name": "Surprise, Honoka's Boobs are Bigger", "girls": ["BE"], "location": "dorminterior", "time": (TimeEnum.NIGHT, WeekendEnum.WEEKDAY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",      "conditions": []}
    eventlibrary['BE011'] = {"name": "Quitting the Soccer Club", "girls": ["BE"], "location": "track", "time": (TimeEnum.AFTERSCHOOL, WeekendEnum.ANY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",                      "conditions": []}
    eventlibrary['BE012'] = {"name": "Action at the Arcade", "girls": ["BE"], "location": "arcade", "time": (TimeEnum.DAY, WeekendEnum.SUNDAY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",                              "conditions": [[ConditionEnum.EVENT, "BE011"]]}
    eventlibrary['BE013'] = {"name": "Recovering from a Defeat", "girls": ["BE"], "location": "arcade", "time": (TimeEnum.NIGHT, WeekendEnum.SUNDAY), "priority": True, "startdate": "BE_size_2", "enddate": "day_end",                         "conditions": [[ConditionEnum.PRESET]]}
    eventlibrary['BE014'] = {"name": "Bouncing All Over", "girls": ["BE"], "location": "hallway", "time": (TimeEnum.DAY, WeekendEnum.WEEKDAY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",                               "conditions": [[ConditionEnum.EVENT, "BE011"]]}
    eventlibrary['BE015'] = {"name": "Chocolate Study", "girls": ["BE"], "location": "dorminterior", "time": (TimeEnum.NIGHT, WeekendEnum.WEEKDAY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",                          "conditions": []}
    eventlibrary['BE016'] = {"name": "Basketball Practice", "girls": ["BE"], "location": "gym", "time": (TimeEnum.NIGHT, WeekendEnum.WEEKDAY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",                               "conditions": [[ConditionEnum.EVENT, "BE014"]]}
    eventlibrary['BE017'] = {"name": "Shooting Hoops", "girls": ["BE"], "location": "arcade", "time": (TimeEnum.AFTERSCHOOL, WeekendEnum.ANY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",                               "conditions": [[ConditionEnum.EVENT, "BE015"]]}
    eventlibrary['BE018'] = {"name": "Bra Fitting", "girls": ["BE", "PRG"], "location": "dormBE", "time": (TimeEnum.NIGHT, WeekendEnum.ANY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",                                 "conditions": []}
    eventlibrary['BE019'] = {"name": "The Fabled Skip Day", "girls": ["BE"], "location": "cafeteria", "time": (TimeEnum.DAY, WeekendEnum.WEEKDAY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",                           "conditions": []}
    eventlibrary['BE020'] = {"name": "First Date?", "girls": ["BE"], "location": "hallway", "time": (TimeEnum.NIGHT, WeekendEnum.ANY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",                                       "conditions": []}

label BE001:
    scene Classroom with fade
    play music Schoolday
    "After the bell rang, there was the familiar sound of chairs getting scraped along the ground as everyone prepared to leave."
    "The only difference was the volume. Compared to what I was used to at my old school, it was a lot quieter."
    "The loudest came from the direction of the blonde with the crazy hair, no doubt due to all the extra pressure she was putting on her seat."
    "Then again, there was another seat in the room that easily caught my attention, thanks to how big it was. It was without a doubt, the largest I'd ever seen, and now it was clear why."
    "Though, the teacher said not everyone's growth factor was visible right away, it could have been something else."
    "The classroom slowly started to empty out, and I made my way out of the room as well."
    "There were two questions that ran through my head."
    extend " First, what was going to grow on me?"
    extend " Second, where was I? It was hard getting used to a new school so quickly."
    "I decided to walk around a bit, to get the lay of the land. Maybe if I lucked out I could find it..."
    scene Hallway with fade
    "The school seemed relatively normal, apart from the size and the people within. It didn't take me long to get the gist of where everything was. Hopefully I'd remember it all when tomorrow came around."
    "But, eventually, I found what I was looking for. Without even checking my surroundings to see if I was being watched, I turned the knob and walked up the steps into the warm sunny sky above."
    scene Roof with fade
    MC "Fantastic. It was a long shot, but I figured they'd forget to lock the roof entrance while they were busy setting up the welcoming assembly."
    MC "Wow, from up here the school really looks huge. I guess it has to be big if they only put a few students in each classroom."
    MC "Wonder how many teachers there are, then? And if they all have weird things like Mr. Akaname down there. Probably. It'd help the students adjust if they knew what it was like too."
    MC "I just wonder why they didn't tell us the reason for coming here until we were already inside? This doesn't seem like a prison or anything, does it?"
    MC "No, the view is too good up here to be a prison. I'd say it's better than what my old school had. Just looks really nice."
    show BE happy with dissolve
    BE "It does. And it's about to look a whole lot better!"
    play music BE
    "My introspection was suddenly interrupted by my elbow getting pressed into something warm and soft."
    MC "What the...Honoka? How'd you get up here?"
    BE "Heh, the same way as you, Kei-chan. Steps. I've been behind you for a while now, did you really not notice?"
    "Not until you bumped into me with that chest of yours..."
    MC "I guess not. My head's kind of all over the place after learning why we're here. How about you? You said you didn't know what this academy was for, right?"
    show BE neutral
    BE "Nope, no clue until teach explained it. It's so weird, don't you think something like this would be more public knowledge?"
    MC "I'd say so. But, if it's only a small group of people affected by this weird growth hormone thing, maybe it's better to not cause a panic of people assuming they've got it."
    extend " 'Oh gosh, I shot up two inches over the summer, I'm going to end up ten feet tall!'"
    BE "Yeah I guess that makes sense. Still, it's a lot to take in. I have to say though, part of me is kind of excited. They didn't make it sound like it was a bad thing, just a bit of an inconvenience. Maybe I'll get something cool."
    BE "What do you think my growth factor is?"
    menu:
        "I'd say it's kind of obvious, isn't it?":
            jump BE001_c1
        "I don't want to jump to conclusions, it could be anything, really.":
            jump BE001_c2
        "Maybe your feet. It would be good karma after all the times you kicked my butt at those dancing games at the arcade.":
            jump BE001_c3

label BE001_c1:
    show BE surprised
    BE "Oh, I haven't the foggiest idea what you could be talking about. A girl's hair does tend to get a bit longer after you haven't seen her for years, Kei-chan."
    MC "Um, actually I was talking about-"
    show BE happy
    BE "Hehehe, I'm kidding, Kei-chan. Yeah, I'd say bigger boobs is definitely the most likely choice for me."
    BE "I guess you were never there to see them grow, were you? Wow, you really missed out. Then again, you'll probably be seeing a lot more of them if our hunch is correct!"
    "It was pretty clear that Honoka wasn't all that upset about this situation."
    extend " If anything, she looked pleased as punch, considering she lifted up her boobs like she was about to serve them on a silver tray."
    MC "Well if that is the case, hopefully I grow something big that you'll enjoy, too."
    "..."
    extend " What did I just say?"
    show BE surprised
    BE "Kei-chan! To think you'd be so forward... I know I said I was in your care, but I didn't think you'd take in that way..."
    MC "Wait, wait, that was a big misunderstanding, I didn't mean to imply anything that-"
    show BE happy
    BE "Bahahaha, oh, wow, Kei-chan, heh, it's too easy to mess with you sometimes, you know that?"
    MC "Yeah, you've certainly taught me that lesson many times in the past. Ow..."
    "I winced as she gave me a playful punch in the arm. One that went a little too deep to be completely painless."
    jump BE001_after

label BE001_c2:
    BE "That's true. Still, I think I've got a pretty good idea what mine could be. It starts with 'B' and rhymes with 'goods'."
    MC "...boods?"
    show BE sad
    BE "What? Shoot, no, I messed that up. I was talking about my boobs."
    show BE neutral
    BE "Like everyone at my old school seemed to do on a daily basis. Hard to blame them really, I made these cans faster than a soda factory."
    MC "Oh, heh. Well, that could have just been some lucky puberty at work, you know?"
    BE "Sure. Still, if it was my boobs, I wouldn't mind it."
    MC "You wouldn't? But you just said everyone at your old school mentioned them all the time."
    BE "Eh, I don't care about that. I doubt I'll care here, either, if everyone's got a chance of getting giant knockers, too."
    extend " Besides, big breasts, well, they kind of seem like the most normal thing I could get, right? I've heard of models or actresses with oddly-sized boobs in the past, so it's not that unusual."
    MC "Hm, guess you've got a good point. You're already used to big boobs, anyway."
    show BE happy
    BE "Exactly! Hehe, you know, Kei-chan, most boys wouldn't be so brazen about talking about a girl's chest, especially to her face."
    MC "W-Well, you're the one who brought them up in the first place!"
    BE "Did I now? Oh, I guess I did. Yep."
    MC "Not the least bit apologetic about it, are you?"
    BE "Hey, they're my boobs, and I shall address them as I please!"
    MC "I... well, fair enough I guess."
    BE "Heh, you're still easy to mess with, I see."
    "Honoka gave me a little love-tap on the arm, one that stung for several minutes later."
    MC "...Yep, that's me. Easy to mess with."
    jump BE001_after

label BE001_c3:
    show BE happy
    BE "Oh wow you still remember that! Haha I really did whoop you at all those games, didn't I? Still, huge feet? That's so weird. Imagine how many socks and shoes I'd need to buy!"
    MC "Well, regardless of what we end up getting, we'll all probably have to change our wardrobes eventually. Hopefully they'll help cover expenses."
    show BE neutral
    BE "That'd be nice. Heh, though I doubt Alice would need the help, Little Miss Fancy down there."
    extend " Then again, she's practically bursting out of her uniform already, so she's probably too lazy to get new clothing or something."
    MC "Maybe. Hm, I guess you could get a big long tongue, too. That wouldn't require new clothes."
    BE "Yeah but then it'd be hard to talk with you. That'd stink."
    MC "Yeah, it didn't look that appealing, did it?"
    BE "Nope. You know what did look appealing though?"
    MC "What?"
    BE "Come on, I know you saw it."
    MC "Saw what?"
    BE "It was staring you right in the eyes!"
    MC "Honoka I really don't--"
    show BE happy
    BE "Pff, I'm talking about my breasts, Kei-chan. Don't think I didn't catch you sneaking a peek when we met up outside the academy."
    MC "Oh, well, listen, if I'd known you were Honoka, I wouldn't have-"
    show BE neutral
    BE "Mm-hmmmmmm. Don't be embarrassed, Kei-chan, it's fine. You're a young man with healthy ambition. Though, I do think I deserve a little payment for you staring hard enough to melt my shirt."
    MC "What do you me-ouch..."
    "I quickly moved my hand to rub a sore spot on my upper arm where Honoka had given me a gentle punch. Hopefully her growth factor isn't her hands, or those punches are going to get a lot harder..."
    jump BE001_after

label BE001_after:
    show BE happy
    BE "Ahh... just like old times, huh Kei-chan?"
    MC "What do you mean?"
    BE "I mean, you, me, and the roof! The original power trio. How many times do you think we snuck up to the roof when we were younger? 100? 200?"
    MC "It was probably a few dozen times if that."
    show BE sad
    BE "Eh you're exaggerating. Still, it's a great wave of nostalgia being up here with you Kei-chan."    
    BE "You know, this academy's definitely a weird place, and we're gonna go through some strange stuff by the sound of it. But, I'm really glad you're here, Kei-chan. Makes things a bit easier."
    MC "Please, Honoka, when have you ever backed down from a challenge, anyway?"
    show BE happy
    BE "Never! And that's why they call me Hard-To-Beat Honoka!"
    MC "I can guarantee nobody has ever called you that."
    BE "Well I'm sure they call me something. I'll get a nickname by the end of the year, I guarantee it. One that suits me! Just you wait Kei-chan."
    "Honoka chuckled before she turned her attention back to the view from the roof."
    "Even through the chainlink fence, it was clear she'd been captivated by the sight of the big buildings before her."
    extend " Her face was bright; she was no doubt thinking of all the new possibilities this academy would bring. I had to admit, I was a bit excited to see what was going to happen as well."
    "But at the moment, my focus was on Honoka. More specifically, the way her chest pushed against the chainlink fence, making it look like she was wearing chainmail armor over her school uniform."
    jump daymenu
    
label BE002:
    scene Campus Center with fade
    show BE sad
    play music Rain
    BE "Oof! Sorry about that, slippery ground!"
    MC "Ah, heh, it's no problem, Honoka. Hard to stop when you get moving, huh?"
    show BE neutral
    BE "Yep, not to mention I slept great last night so I've got tons of energy. I'm so excited, new school, new opportunities."
    MC "Sounds almost like you should have had a tough time getting to sleep then. I had trouble myself, my roommate is... weird. Plus, I'm a bit nervous about this whole thing."
    BE "Oh I was jittering all over the place last night. But I still got like, four hours of sleep which is a lot for me!"
    MC "Really? That seems unhealthy."
    show BE happy
    BE "Hehe, probably. Good thing I'm just messing with you then."
    "I chuckled and rolled my eyes, then snickered in the direction of the ground as I crossed my arms. Honoka always was a bit of a jokester."
    MC "So, what have you been up to, Honoka?"
    show BE neutral
    BE "Oh, you know, mostly just checking out the campus. There's quite a few clubs here, more than I expected, considering how 'special' this place is."
    "She rolled her eyes a bit and gave finger quotes in the air, before planting her hands on her hips and looking around. I could practically see the energy rippling off of her, trying to break free. Clearly she wanted to go and do something more active."
    MC "Oh yeah, anything good?"
    show BE happy
    BE "Definitely! I've already signed up for the soccer club, but there were a bunch of others that looked really fun too. There was a jogging club, a basketball club, archery, kendo. You know, all the classic stuff."
    play music Busy
    MC "Soccer, huh? Yeah, that's definitely a good fit for you."
    BE "I know, right? Wait until they see how hard I can kick!"
    MC "I'd be wary of being the goalie, that's for sure. Or the ball, for that matter."
    BE "Yeah, should be fun! It was a tough call between that and basketball actually, but I think I picked the right one. Though, I dunno, maybe something more physical, I didn't see if there was a wrestling club, hm."
    MC "Well, maybe just stick to one club for now, yeah? Not like you can join them all, anyway, so don't worry about one club you missed out on, because there's no way you'd be able to do them all regardless."
    BE "Oh yeah? You think it'd make me too tired?"
    MC "No, I mean I'm sure that's literally impossible. There's no way they'd have the clubs all worked out in a way where it would be possible for you to attend every event, along with leaving time for schoolwork."
    show BE sad
    BE "... Well when you put it that way it sounds pretty silly, doesn't it? You sure are clever, Kei-chan."
    "I think that qualified more as 'common sense' as opposed to 'cleverness', but, I'll take it."
    show BE neutral
    BE "What about you, Kei-chan, were you thinking of joining a club?"
    MC "Me? Honestly I'm not sure. I hadn't given it much thought yet. I think i might hold off until I know for sure what my growth factor is. I really don't have any clue yet. I wouldn't want to pick something I'd be unable to do once I started growing."
    BE "That's a good point. Would be really lame to get good at something and then end up being unable to do it. So, probably best if you don't pick something like tap-dancing for when you end up getting gigantic feet."
    MC "If I end up getting gigantic feet, I'll join the soccer club just to show you how hard I'll be able to kick."
    show BE happy
    BE "Hehehe, I'd like to see that."
    "Honoka smiled as she gave me a little tap on the arm. I gave a sharp inhale and laughed as I began to rub the spot where she hit me. Forget worrying about her kicks, her punches still had a good sting to them after all these years. Maybe its her subconscious way of making up for when she bumped into me with her chest earlier?"
    MC "Well I can assure you, you won't."
    "Honoka chuckled again, and started to meander around the campus. I kept up with her, still unfamiliar with the surroundings, but wanting to know the place better."
    MC "Actually, speaking of growth factor and everything, did you find out what yours is, yet?"
    show BE neutral
    BE "No, I think that I'll find out later. I mean, I'm like, 95%% positive it's my chest to begin with so even once I find out, it probably won't be a big deal."
    MC "Technically, no matter what you're getting, it's going to be a 'big' deal."
    show BE happy
    BE "Pfff, that was lame, Kei-chan."
    MC "Hey, I'm trying. I like seeing you laugh."
    "Don't say 'Because it makes my boobs bounce?'. Don't say 'Because it makes my boobs bounce?'. Don't say 'Because it makes my boobs bounce?'."
    BE "Because it makes my boobs bounce?"
    "Damnit."
    MC "No, it's just, I dunno, making one another laugh, seems like something only friends do for each other?"
    BE "Heh, I guess so. I can see your logic there, Kei-chan. But then you really need to work on your sense of humor."
    MC "Hey, you make me laugh all the time, so my sense of humor is fine. You need to get one instead."
    BE "I'll get one when you get fitted for your size 38 feet."
    MC "Hehehe, dangit, Honoka. See, got me laughing that easily."
    BE "I know. That's because I'm awesome."
    "Honoka smiled and put her fists on her hips in haughty pose, reminding me of Alice for a moment. Only while Alice was unbelievably serious in her holier-than-thou attitude, Honoka was obviously kidding. We stood there chuckling for a bit more before Honoka noticed the time and decided to get going. I nodded and waved goodbye, sticking my hands in my pockets before heading off myself."
    jump daymenu
    
label BE003:
    scene Campus Center with fade
    play music Sunset
    "The sun was scorching today. The kind of heat that tricked you into thinking it would be all right to go outside for a while, but once you were in the rays of the sun, you realized what a horrible mistake that was.I had already drank a whole bottle of water to cool off, but it wasn't enough. Thankfully, there were vending machines scattered around, and I had a few coins burning a hole in my pocket."
    MC "All right, let's see. What do I want? Soda, juice, eh, water's healthier... but, soda's tastier."
    "After sliding in my change and selecting my drink, I bent over to retrieve my precious bounty. The sharp hiss of carbonation escaped the can as I opened it up and took a refreshing swig."
    MC "Mmm, much better."
    "I turn around to walk off and end up bumping into someone. More specifically, I bumped into Honoka. Even more specifically, I bumped into the spot where one was most likely to bump into Honoka. After I caught my balance from the impact of stepping right into her chest, I cleared my throat and looked at her."
    MC "Woops, uh, hey Honoka. Sorry about that. Wasn't watching where I was going."
    show BE happy with dissolve
    BE "Hehe, hey Kei-chan. Don't worry about it, was an accident, right?"
    MC "Right."
    "I noticed that Honoka wasn't wearing the normal school uniform, having traded out the classic skirt and shirt combo for a pair of spats and a more tightly-fitted t-shirt."
    MC "What's with the get-up?"
    show BE neutral
    BE "Oh, I had soccer practice in a bit, this is the official uniform. Bit snug, though."
    "Honoka tugged down on her shirt and stuffed it into her shorts. Clearly that was the way it was supposed to be, but when she stood straight up, the front of the shirt kept coming out of the spats, exposing a tiny sliver of her waist."
    MC "Why didn't you just get the next size up?"
    BE "I dunno. Figured I'd try it out first, no sense causing a fuss about the size if I end up not liking soccer, after all."
    MC "I guess that makes sense. Damn, but it's going to suck having soccer practice today when it's this hot out. Hopefully it doesn't last too long."
    show BE sad
    BE "Woof, yeah, I wasn't planning on that, either. Hopefully there'll be some refreshments there, though. They can't really keep us out for too long without giving us some water at least."
    menu:
        "You uh, want some of my drink?" if getAffection("BE") > 3:
            jump BE003_c1
        "You uh, want some of my drink? (disabled)" if getAffection("BE") <= 3:
            pass
        "Maybe grab something to drink then before you get going":
            jump BE003_c2
        "Are you telling me those melons of yours don't produce milk?":
            jump BE003_c3

label BE003_c1:
    show BE neutral
    BE "Ooh, what did you get?"
    MC "Ah, like, a lemon-lime soda. It's pretty good. Want a sip?"
    show BE neutral
    BE "Heh, sure."
    "I handed the can over to Honoka and saw her sniff it a bit."
    BE "Mm, smells good."
    "Honoka tilted her head back and took a swig. Then another, and another. With each swallow of soda that went down her gullet, she tilted her head further back. Gradually, this showed off more and more of her stomach as her shirt was lifted out of her gym shorts, showing off her thin waist and tiny belly button."
    "It also made me wonder how much of her lower vision was blocked off by her chest, because as she arched her back, her breasts were raised up higher, sticking out like buoyant balloons from her torso."
    "By the time she finished off my drink, they were practically pointed straight up, only to come swinging back down to their normal height when she swallowed the last drop and stood straight up again."
    show BE happy
    BE "Ah, that really hit the spot! Thanks Kei-chan!"
    MC "Yeah, no problem."
    "My tongue felt like a desert. I rifled in my pockets to see if I had enough change for another drink."
    BE "Hm..."
    MC "What's up?"
    "Wordlessly, Honoka took the now-empty can and placed it against her chest, right between her breasts. She held it there for a moment, obviously in contemplation, but it wasn't clear what she was thinking about. After a while it ended up being a moot point as she just tossed the can in the nearby recycling bin."
    show BE neutral
    BE "Never mind, probably not big enough anyway. Would hurt, I bet."
    MC "Huh?"
    show BE happy
    BE "Nothing, hehe. Thanks for the drink, Kei-chan, but I better get going. Next time I'll owe you a drink, okay? I'll make sure to take a sip from it first so we're even. Tricking a young girl into getting a secondhand kiss, you playboy."
    "Honoka winked and made her way over to the soccer field, leaving me there, speechless for a moment."
    hide BE with dissolve
    MC "Wait, what? That wasn't why I gave you the drink, I was just, oh, darnit.... I'm still thirsty."
    jump daymenu

label BE003_c2:
    show BE neutral
    play music BE
    BE "Yeah that's probably a good idea. Hm...."
    "Honoka walked over to the vending machine as I took another sip of my soda. She hummed to herself for a while as she looked over the various options, eventually deciding on something and paying for it. As she opened a bottle of water, I racked my brain for a point of conversation."
    MC "So... soccer, huh?"
    BE "Yep, should be pretty fun. Lots of running and kicking things."
    MC "I bet. Don't know a lot about it myself, but is there any specific position you want to do?"
    BE "Just anything besides the goalie. I'm sure it's tough work but I want to make sure I'm out in the field getting the most exercise, running around and sweating it out."
    MC "Right. Well if that's the case you really do need to make sure you stay hydrated."
    show BE surprised
    BE "Of course, I'm not a numbskull, Kei-chan!"
    MC "Never said you were. Just, it's an easy thing to forget when you're focused on something and I know you, Honoka. When you get focused on something, occasionally you can get a bit of tunnel vision."
    "Honoka tilted her head from side to side several times like a metronome."
    show BE neutral
    BE "Yeah you've kind of got a point there. Well if you wanted to, you could probably come watch me. I doubt they'd mind.Then you can remind me to drink if I forget."
    MC "Maybe I'll do that, I don't think I have anything else going on."
    BE "Heh, sounds good. Well, if you come I'll see you over at the soccer field. If not, well, see you whenever. Have a good day, Kei-chan."
    MC "You too."
    "Honoka raced off to the soccer field as I took another drink, and decided whether to go follow her or chill somewhere else for the rest of the afternoon. It was really hot, after all."
    jump daymenu

label BE003_c3:
    #should this be an affection loss? she even calls it a "fun talk"
    $setAffection("BE", -1)
    play music Tension
    show BE angry
    BE "Kei-chan, you should have called them udders if you were gonna make a cow joke."
    MC "Darn, you're right. Haha."
    BE "Though..."
    MC "Though, what? Are you really, I mean, I didn't mean to insult you if you were. Not that I'd think it was a bad thing or something like that, I just, if you weren't cool with it, I, uhhh."
    show BE sad
    BE "No no, it's not that. Just, now you've got me wondering if that's possible."
    BE "I mean, I'm not an expert on female mammaries or anything but, there's obviously parts of the breast meant to make milk, so what would happen if they swelled up and started getting bigger? Would that mean the woman would start making a ton of milk, or would it just increase the size of the breasts around them, but keep the level of lactation about the same?"
    MC "I uh, I don't really know how to answer that. I think it'd be weird for a tiny part of the body to be affected like that, though. If it was, I'd say, probably a bit of both?"
    BE "Huh. Interesting to think about."
    "Honoka and I both stood there for a moment, saying nothing to each other. Our eyes weren't really focused on one another either. It took a good minute or two before I finally broke the silence."
    MC "Have we both been thinking about milky breasts now?"
    show BE happy
    play music BE
    BE "Probably! But I'm a girl, it's okay for me to think about it. You're just a pervert."
    MC "That's not fair, you put the idea in my head."
    BE "I just planted the seed. You're the one who watered it and let it grow. Could have plucked it out at any time."
    MC "That's not how thoughts work. That's not how anything works."
    BE "Apparently it is, ehehehe."
    "Honoka chuckled, and licked her lips. She looked over at the vending machine, but then pulled out her phone and checked the time."
    show BE sad
    BE "Darn, I need to get going or I'm going to be late. Won't do good to be tardy for the first soccer club meeting."
    MC "Ah good point, don't let me hold you up then."
    show BE neutral
    BE "Thanks. Thanks for the fun talk, too. See you around, Kei-chan."
    MC "See ya, Honoka!"
    "I gave a nod to Honoka as she ran to the soccer field, then leaned against the vending machine as I continued to drink my beverage. It was too hot today."
    jump daymenu
    
label BE004:
    scene Track with fade
    play music Busy
    "I decided to head over to the soccer field. Before I even got on the grass, I heard the sound of a coach whistle blowing, directing students in their training. I picked up the pace a little bit so I could see what was going on. Among the small crowd was a familiar face. I waved over to Honoka, who enthusiastically waved back to me. She seemed happy to see me. I looked around for a place to sit. There's bleachers nearby, but I decided to just sit down on the grass for a while, making sure I stayed out of the way."
    MC "This is cool. Good to see there's still a sense of normalcy in this place, doesn't look like the soccer field is anything special or different."
    "The coach didn't look that special either. Not that he was ugly or anything, but there wasn't anything on the cap-wearing man that I recognized as being overly-large. It made sense, I guess. While there must have been enough students in the country to require a facility like this, it didn't mean that there'd be an equivalent number of faculty members who shared odd growths as well. The academy probably had to take what they could get."
    MC "Man, Honoka's pretty good at this."
    "That wasn't all that big of a surprise. She always was pretty athletic. We even played soccer together when we were younger, whether it was just kicking the ball around or actually trying to score goals. Maybe I'd look into joining the soccer club myself, it would give me something to do after classes, for one. Plus, it wouldn't hurt to have more chances to see a childhood friend."
    MC "Phew, it's really hot today..."
    "I wondered if there was anything nearby to drink. Fortunately, it looked like they provided a water cooler. Good, at this heat the students were likely to pass out if they didn't get any hydration. Still, I couldn't just go over there and take some when I'd just been sitting on my butt for twenty minutes. Thankfully the coach called for a break after a while, and I walked over to get some water with the others."
    MC "Hey Honoka!"
    show BE surprised with dissolve
    BE "Woo, hey, Kei-chan. Glad you came by!"
    MC "Well, you know I've always had a thing for soccer."
    show BE neutral
    BE "Sure. I'm surprised you didn't join the soccer club, actually. Were you just afraid I'd beat you whenever we were asked to go against each other? If I recall I won more of our games when we used to play."
    MC "What? No, that can't be right. I'm positive I won more."
    BE "You beat me a lot, but I remember two wins over you that gave me the edge."
    MC "That one where you hit me in the nose with a soccer ball shouldn't count!"
    BE "It wasn't intentional or anything! And besides, you still wanted to play, it was just your mom that pulled you out before you could get another goal on me, but I'm counting that as a win anyway."
    MC "Fine, what was the other win that gives you the majority over me?"
    BE "It must have been in the summer, I guess the last one before we had to split up. You tried to shoot a goal like, four times in a row, and you just kept hitting the side of the goal. Every. Single. Time. It was funny the first three times, but the fourth one was just sad. I didn't even try to block it, I just stood there as it bounced up in the air and landed in the other goal instead. It was nuts."
    MC "...Oh geez I remember that now. Ugh, I don't know what was wrong with me that day, but yeah, I must have been super distracted about something."
    BE "I'm just glad you conceded the match right there. If you tried to do a fifth shot, you probably would have kicked the side of the goal again and then the ball would have gone through one of the windows in your house instead. A sixth attempt would have knocked you out cold."
    MC "I can't believe you remember that."
    show BE happy
    BE "Hey I remember a lot about when we were kids, those were fun years! Lotsa good memories."
    "Honoka smiled as she finally poured herself some of the water from the cooler and took a big drink. I helped myself to some as well, after double-checking that there would be plenty for the others who needed it more."
    MC "It's good to hear that, I have to say. Definitely had some fun times together, didn't we?"
    BE "Mm-hm."
    "Honoka sat down in the grass, probably to rest her legs for a bit, and I joined her. She started scratching at her calves where the grass tickled her legs, groaning as she did so."
    BE "Ah, that's so much better."
    MC "What, you forgot running would make your legs tired?"
    show BE sad
    BE "No not that. Just, I dunno, soccer's still fun but there's something missing. Maybe it'll just take me a bit to get back into it, but, it's not quite got that 'umph' I was looking for."
    MC "Well, don't give up yet. Only the first day, right? Like you said, you probably just need a bit of time to get back into it."
    show BE neutral
    BE "Yeah that's probably it. Heh."
    "The coach blew his whistle again and called up the students to line up and run some more drills."
    show BE happy
    BE "Whoops, better get going. You going to stick around?"
    MC "Yeah, probably. Good luck!"
    "Honoka gave a quick wave and trotted over to the lineup, while I went and sat back down outside of the actual field."
    hide BE with dissolve
    extend " I sat there for a while and continued watching Honoka and the other students kick the ball around, run drills, and do some exercises. Seemed like good fun, and I was tempted to see if I could just join in."
    "But, as I looked at the sweat running down my shirt, I remembered that it was way too hot today. Maybe next time."
    jump daymenu
    
label BE005_old:
    #This scene needs to be rewritten or something, it doesn't make sense as an 005
    scene Hallway with fade
    show BE happy with dissolve
    BE "Oh, Kei-chan!"
    "Honoka bounced over towards me, clutching a few pieces of papers in one hand. She stopped, but a little too late, and her breasts collided into my side. She just brushed it off and stepped back, shoving the papers inside her sizable chest for safekeeping."
    MC "Oh, Honoka. Hey. What's up?"
    BE "Well, just got my test results back."
    MC "Test results? Oh! Right, for the growth factor. That's why I'm here too. I guess it's time to finally bite the bullet and figure out what's going to grow on me."
    BE "I bet it'll be your feet or something lame like that, haha."
    MC "Ugh I hope not, buying shoes would be such a pain. Besides, you can't make fun of me for whatever mine is if I can't return the favor, what'd you get?"
    "Honoka smirked, and cupped her breasts in her arms. She lifted them up until the top curves of her fleshy spheres covered up the bottom half of her face. Her expression became hard to read once most of it was blocked by her bosom. But, it was easily assumed that she was being playful about the fact that her palms overflowed with breastflesh."
    BE "What do you think it was?"
    MC "Was it really that obvious?"
    show BE neutral
    BE "If it hadn't been my boobs, I would have been really surprised. Would have had to go see a regular doctor to check on my breasts if that was the case, these puppies are pretty large already. A bit more growth would have been cause for concern, I think."
    MC "And finding out that your, uh, your boobs are going to get supersized isn't a concern?"
    "Honoka shrugged, throwing up her arms and giving a grunt."
    BE "Eh, can't be worse than what most of the others here are going to deal with, right? Besides, they gave me some good information about it. The nurse already had these printed out, too. I think the testing they did was more a formality than anything. She eyed me up and pretty much said 'So, you know what you've got, right?' Not in those words, exactly, but I got what she meant."
    "Honoka reached into the expanse of her cleavage and pulled out the papers to flip through them."
    BE "I guess I'd been mentally preparing myself for this news to begin with, so, a lot of what the nurse said made sense. Plan ahead for when it comes to clothing, and they gave me a place where I can work on getting stuff fitted. A few exercises to strengthen the back and shoulder muscles, just to be safe."
    MC "Well, now that you know for sure, how do you feel about it? I mean, it's boobs. So, most girls would probably be all for that, right?"
    show BE happy
    BE "Heh, I'm sure that's the male fantasy for sure. Eh, I'm sure it's true, though. I think in general, yeah, I'm excited!"
    MC "Yeah? Well, that's good. Are you going to have to keep buying new uniforms, or will they at least supply those for you?"
    BE "It looked like the deal was regular clothes I was mostly on my own with, but school uniforms would be provided and tailor-made for me, which is nice. I mean, if you figure a normal school week anyway, uniforms are what I'll be wearing most of the time anyway. I wonder if they'll be standard or if they'll let me show off a little cleavage or something?"
    MC "Honoka! This is a school, I doubt they'll intentionally sexify the uniforms."
    BE "Well it would seem like a shame, otherwise. But I guess with my own things I'll be able to get them however I want them to look."
    MC "Why do I get the feeling you're only saying these things to mess with me?"
    BE "You'd be about... 80%% accurate if you're really thinking that."
    MC "What's the other 20%% then?"
    BE "That's me thinking 'boobs are fun'."
    MC "Heh, so, have you always wanted bigger boobs since you were younger or something?"
    BE "Hm, I don't know if I ever really thought about it that way. Like you said, I think pretty much every girl has that moment of breast envy at some point in their youth. But, considering how much I blossomed, I guess I acclimated to the idea of huge knockers pretty easily."
    "I nodded, and started to stretch my arms. After that, I lean against the wall nearby, and Honoka coincidentally does the same thing as well, so we both turned our heads to keep looking at each other."
    MC "I guess I never asked, probably because I thought it wasn't appropriate..."
    show BE neutral
    BE "Asked what?"
    MC "Well..."
    menu:
        "When did you start noticing that your boobs were oddly huge?":
            jump BE005_c1
        "How do they feel? Your boobs, I mean.":
            jump BE005_c2
            
label BE005_c1_old:
    show BE surprised
    BE "Gee, honestly, I'm not really sure. It's not like they just shot out like bazookas one day, you know?"
    BE "It had to have been a couple of years ago, at least. I guess I grew a good amount to start off with. After they started growing, I was easily a c-cup in most brands by the end of that year. But then they just kept growing, and growing. I never really thought it was anything to be concerned about though."
    MC "I don't think it is, really."
    show BE neutral
    BE "Right? They haven't been much trouble so far."
    MC "Did you get, well, picked on, at all?"
    show BE sad
    BE "Eh, a little bit here and there. Girls that were jealous, boys that wanted some. Both ended up calling me the same names though, people are so unimaginative. There must be a hundred different words for boobs and they rarely ever used more than three. Got boring pretty quick."
    MC "Only you would get a bit bullied and school and call it boring because their taunts weren't creative enough."
    show BE happy
    BE "Yep, because I rock, Kei-chan. The girl with big boulders rocks as hard as mountains."
    MC "Think you tried a little too hard there."
    BE "Hard as my ni-"
    MC "Please stop."
    BE "Spoilsport."
    MC "Tease."
    jump BE005_after

label BE005_c2_old:
    "Why does the mouth say things the brain wants to say, yet knows is dumb to state at the same time? Luckily, Honoka's reaction was as upbeat as ever."
    show BE happy
    BE "Oh... the urge to taunt you and go 'Why not find out for yourself, big boy?' is palpable."
    MC "Ha."
    "..."
    "Please say something else."
    BE "No, see, this is supposed to be the point where you say 'Out here, where anyone could see? You're such a naughty girl, Honoka.'"
    MC "No, I wouldn't say something like that."
    show BE neutral
    BE "I guess you're right, you're too polite to do that, right?"
    MC "Well, that, and I know you're not really a naughty girl. You just like teasing me."
    show BE happy
    BE "Oh, I really do, don't I?"
    MC "You do, which is why I wouldn't call you naughty. I would call you a staller though, because you still haven't answered my question."
    BE "Really curious about that, huh?"
    MC "Shouldn't I be? I'm looking at it from the perspective of someone who hasn't found out what they're going to get, asking someone who knows and has already experienced their growth. I'm curious."
    BE "Huh, that's a good point. Well, heh... they feel good. Bouncy, soft, warm. But, more than that, they're nice. They don't feel unnatural, you know? They're part of me, they feel like they belong there."
    MC "Well, that's good to know. Thanks, Honoka. That's actually a bit comforting."
    BE "If you really want comfort, you should be jealous of having some pillows like these, if I lay them on a table right they make a great headrest."
    MC "And the comfort goes to awkwardness in three seconds flat..."
    jump BE005_after

label BE005_after_old:
    MC "Well, I guess I should get going, need to find out what I'm getting after all."
    show BE neutral
    BE "The way you say it makes it sound like you're in line to get a superpower or something. Unless you get ultra-muscles, I don't think you'll be fighting any crime soon."
    MC "I doubt I'd get anything that cool. Anyway, thanks for talking to me, Honoka. I'll see you later."
    show BE happy
    BE "Bye Kei-chan, was nice running into you!"
    jump daymenu
    
label BE005:
    scene Classroom with fade
    play music Rain
    "So. I ended up with ever-growing hair. All things considered, that didn't sound too bad. After all, that Rapunzel character dealt with it just fine, and unlike her, I'll actually have access to scissors and razors. I scratched my chin, wondering if it'd apply to facial hair as well. That would be a bit more troublesome to deal with, but still manageable. At the worst, it just meant that a few days without a trim would have me looking like an old wizard, which was kind of cool..."
    "As I entered homeroom, it was obvious that everyone was talking about their discoveries already. It was just much louder than it typically was. Tones ranged from excitement and pride to confusion and sadness. Well, that's what the school was for, I suppose. To give everyone here a place to discuss their bodies in a safe environment. Still, it made me wonder if my trait was common or an oddity. I guess there was plenty of time to find out."
    show BE happy with dissolve
    BE "Oi, Kei-chan."
    MC "Hey, Honoka. What's going on?"
    "Honoka smiled, and took a seat next to me. She groaned with a yawn and stretched out her back, closing her eyes and looking extra cute as she popped something in her back."
    BE "Not a lot. Did you happen to figure out how to do that last question on our math homework last night?"
    MC "I think so. I at least gave it a good effort, but let's just say I'm glad it was only an extra credit question. I guess they didn't want to overload us with hard questions right when we were going to find out what our growth factor was."
    show BE happy
    BE "Right. Oh! So, tell me, tell me, what did you end up getting? Fingernails? Ears? Feet?"
    MC "Hair."
    show BE surprised
    play music Schoolday
    BE "..."
    extend " Really? That's it? Huh, I was hoping for something a little stranger. Is that why you've always got your bangs covering your eyes then?"
    MC "I guess so? I've never really noticed it before if that's the case. I mean, I suppose I might have gotten haircuts a bit more often but it wasn't really something I paid much attention to."
    show BE neutral
    BE "That's fair. Me on the other hand, I've known what I was going to be growing for a while now."
    "To emphasize her point, Honoka slumped forward and let her sizable bust sit on the desk for extra comfort. It was hard not to stare, but then again she was practically begging me to look."
    MC "So you're going to be the official boob queen of Seichou Academy. Shall I fetch you a crown and scepter, my lady?"
    BE "Don't go throwing titles at me yet. I'm sure there's other girls in this school who are going to end up with massive breasts. It surely can't just be me, right? I wonder if that's a club here, now that I think about it. Clubs for each type of growth people can get?"
    MC "Eh, I wouldn't count on it. There might be people here who really are the only ones with that particular affliction. This school's all about inclusion, they wouldn't want people to feel left out because of that. Plus, grouping everyone together might make them feel more, I don't know how else to say it, 'freakish'?"
    show BE surprised
    BE "What do you mean?"
    MC "Like, if there was a club where everyone who had a growth factor where they'd end up ridiculously obese, it would feel like they were being bunched together. Excluded from everyone else. It wouldn't be much different from cliques back in 'regular' school, you know?"
    show BE neutral
    BE "Yeah, I guess you've got a good point."
    "Honoka smiled and straightened herself up in her chair. We both took a moment to look around the room and observe everyone else for a bit. Some students were looking at their own bodies, or examining their friends. One or two were just staring down at their desks."
    BE "I guess depending on how big people get, it might not make sense to shove everyone with the same growth factor into one room, either. Otherwise, like in your case, you'd just end up with a waterfall of hair. It'd get all tangled up and messy, knotted together. Like when rats get all matted together and gross. Bleh."
    MC "Yeah, heh, thanks for that lovely mental image, Honoka."
    show BE happy
    BE "I aim to please. So, tell me, any plans for how you're going to deal with your hair? Going to go ahead and grow it out for a while, to try something new?"
    menu:
        "Eh, I don't really care, it's just hair.":
            jump BE005_c1
        "Maybe. You think it'd look good?":
            jump BE005_c2

label BE005_c1:
    $setAffection("BE", -1)
    show BE sad
    BE "Well, yeah, sure. But it's still part of you. Not going to embrace it, even a little?"
    MC "I just, I don't know yet. I might, I might not."
    BE "Come on, I think you should try it. Maybe you could grow out a pair of pigtails, or a mohawk, or one of those huge pompadour things."
    MC "Honoka, really, it's, I just don't want to do anything different with it. I like it the way it is."
    show BE angry
    BE "Oh, okay. Understood."
    jump daymenu
    
label BE005_c2:
    BE "Well, it couldn't hurt to try something out, right? Plus you've got the benefit of it growing super fast, so you could try out a new hairstyle, say it sucks, then chop it all off."
    MC "That's a good point."
    BE "The downside is you'll never be able to go into the military. They'd spend thousands trying to keep your hair nice and trim and fail miserably."
    MC "That's not the worst of it, either."
    BE "No, what is it then?"
    MC "I won't be able to ever dye my hair! If I do, it'll grow out so fast that I'd spend way too much on dye and upkeep trying to keep it blond or black or whatever color I wanted it to be."
    BE "Well, be thankful your normal hair color is just fine then."
    MC "Thanks. Actually, I wonder... people still buy hair for wigs, right?"
    show BE happy
    BE "I assume so. Wigs are still needed. You could probably donate it super easy, I don't know if they exactly buy it anymore. You could probably find a crazy artist who'd want to do something with all that hair though. "
    MC "Maybe a scientist could use it as a fuel source."
    BE "Or they could fuse you with a spider to create a never-ending source of powerful brown silk."
    MC "Or I could just get locked in a tower and need to have a princess come save me by climbing up it."
    BE "Well if that happened I'd be happy to give it a shot. It would just depend on whether you'd be able to handle my weight at that point."
    "I looked around and smirked when I saw Alice rubbing her engorged stomach with one hand."
    MC "I don't think you'll need to worry about getting too heavy, Honoka."
    show BE neutral
    BE "Hopefully not soon at least. Got a soccer match coming up I want to make sure I kick butt in. Only been in the club for a few days and we've already got a game, they like to be active I guess."
    MC "Well that's good. Maybe I'll be able to come see it."
    BE "That'd be nice."
    "Honoka chuckled, and then went silent as our teacher walked in. The other students all began to hush after a while, ready for class to begin. We'd all been in classes for several days already, but now that we all knew what was going to change about our bodies, it really sank in that this would be a new learning experience for us all."
    jump daymenu

    
label BE007:
    scene Classroom with fade
    play music Schoolday
    "I had to give credit where credit was due. Despite having such a long tongue, Tashi-sensei seemed to be pretty good at talking without it getting in the way. It was fairly easy to understand him, and he was more than willing to repeat himself if somebody misheard."
    "That was really the only thing unusual about class. The lessons weren't that different from what I was used to back at my old school. There was just that ever-prevalent undercurrent that everyone was at this school for a very specific reason."
    "But, oddly enough, it seemed like it was already starting to fade away, bit by bit. I suspected it wouldn't be long before I wouldn't even think about it. Though, logically once my growth really kicked in, I'd be stewing on that for quite a while."
    show BE neutral with dissolve
    BE "Hey there Kei-chan."
    "Meanwhile, there was someone who wouldn't be having that problem. Mainly because her growth was obvious, especially to her, but also because I didn't see Honoka as the type of person who ever had real 'problems'."
    MC "Hi Honoka."
    "I turned to face Honoka, and then tilted my head up to actually look at her face. As appealing as an eyeful of breasts was, it wasn't the most polite way to look at a childhood friend."
    MC "How's it going?"
    BE "Not bad, just, you know. Class. Never the most interesting part of the day, yet it takes up most of it."
    MC "Maybe, but what can you do? Can't really do anything without having a decent education. At least you have a club you can go to later to kill some time and have more fun. I should really look into that, soon."
    show BE happy
    BE "Yeah, it's pretty fun. Would be a lot more fun if you were there, though."
    MC "I'll definitely think about it. Would be great to have more opportunities to hang out with you."
    BE "Well, you've got one right now. Want to go grab lunch and sit together?"
    MC "Sure. I could do that. Didn't have any other plans."
    BE "I mean if you had reservations at some other cafeteria, I would understand."
    MC "No no, only the finest school lunch will do for me. Let's go."
    "I stood up from my desk and followed Honoka down to the cafeteria, spending the walk deciding on what I would get that day. Yesterday I had seen they had some pretty good-looking soba noodles, so that might be a good choice. Once we got to the cafeteria, we both stopped right inside the entranceway, peering at the tables to look for a good spot."
    scene Cafeteria with fade
    show BE happy with dissolve
    MC "See any open seats?"
    BE "Yeah, right there."
    "Honoka pointed out two seat opposite of each other."
    MC "Cool. All right, let's grab our food and hope they're still there when we get back."
    "It wasn't like the seats were packed to the brim like a baseball stadium, but my head was still remembering moments from my last school where all the good seats would be taken in the first three minutes of the lunch bell ringing."
    "Honoka and I walked to the lunch line and grabbed our food, and got back to our seats after a few minutes, leaving us plenty of time to chat."
    MC "So."
    BE "Ba."
    MC "Wait, what?"
    BE "Soba. How are the soba noodles?"
    MC "Oh! Heh, pretty good actually. What did you get?"
    BE "Just some fried chicken and rice. Tasty stuff, they've got some good chefs back there."
    MC "Well I sure hope so. I would think that since everyone here is going to be doing some big growing, they'd need to know how to feed some big students."
    BE "Makes me think of how many times my mom would throw out that phrase 'Eat, you're a growing girl!' She didn't know how right she was."
    MC "And you're not even the biggest."
    "Honoka and I both turned our gazes to look over at Alice, who, despite evidence to the contrary, didn't appear to have that much food on her plate."
    BE "I wonder... I haven't asked her yet. But, I wonder what is actually going to grow on her."
    MC "What do you mean?"
    BE "Like, you're going to get longer hair, I'm going to get bigger boobs. Is Alice just going to get a bigger stomach, or is it an all-over deal?"
    menu:
        "I actually know the answer to that." if getAffection("BBW") > 3:
            jump BE007_c1
        "I actually know the answer to that. (disabled)" if getAffection("BBW") <= 3:
            pass
        "I'm not really sure.":
            jump BE007_c2
        "Maybe it's just hidden under all that weight.":
            jump BE007_c3

label BE007_c1:
    #is there actually a point where this is given out? maybe this should be associated with WG005 instead of an affection check or something
    show BE surprised
    play music BBW
    BE "Oh?"
    MC "Yeah, I've talked to Alice a couple of times. I don't want to give out too much if she hasn't said anything herself, but, it's more the second option. She's not going to end up with a big gut. I mean, well, that'll be part of it naturally, but it's not the focus."
    MC "She's basically going to get extremely overweight. Thankfully she's not going to end up with the negative effects of that."
    show BE happy
    BE "Oh, well that's good. Nothing fun about heart disease."
    MC "No, definitely not."
    BE "So, you've chatted Alice up a couple of times then? I didn't know you were into big girls, Kei-chan. Not 'that' kind of big, anyway."
    MC "Huh? Oh, heh, Honoka. It wasn't like that. I was just being nice. She may have come off as a little pompous when we first met her, but she didn't seem 'mean', exactly. I figured it wouldn't hurt to get to know her better."
    BE "Of course. I should have known. That's just like you, Kei-chan. But, be careful, or you're going to end up being responsible."
    MC "Responsible for what?"
    BE "My weight of course! Stick around with Alice too much and I might be compelled to put on some pounds to keep your attention on me."
    play music Schoolday
    jump BE007_after

label BE007_c2:
    show BE neutral
    BE "I guess that makes sense. Do fat cells get bigger or do they just multiply? Wait, I guess if it's a cell it can't really be a different size, can it?"
    MC "That's... a question for someone smarter than me. All I know is, it's got to be something with her body. She's definitely got a good appetite, but it doesn't seem like she's eating anything too bad. It's not like her tray is loaded up with pizza and snack cakes."
    BE "Oh, why did you have to bring up snack cakes? Now you've got me thinking of them. This is all your fault. Now what am I going to do?"
    jump BE007_after

label BE007_c3:
    $setAffection("BE", -1)
    show BE sad
    BE "Uh, what do you mean?"
    MC "Maybe her being fat isn't actually related to her growth, it's just coincidental that she eats so much."
    BE "..."
    MC "What?"
    show BE angry
    BE "That's kind of mean, Kei-chan. Alice is pretty abrasive but, if there really wasn't a biological reason for her being heavy then it would be something to be concerned about, not something to joke about."
    MC "Oh. Wow, yeah, I guess you're right, Honoka. Sorry. I was just joking around."
    BE "I know, but, well, I wouldn't like it if I heard you were making jokes about my boobs behind my back. When it's you and me and I bring it up that's one thing, but, talking behind someone's back just isn't cool."
    MC "Right, right. Won't happen again."
    show BE neutral
    BE "Good. Phew. Got me a bit riled up now. I think you need to do something to make it up to me."
    MC "Oh boy, like what?"
    show BE happy
    BE "Like, buying me a snack. Or several snacks."
    jump BE007_after

label BE007_after:
    MC "You're just looking for an excuse to eat those cream-cakes until you get sick again like you did in second grade."
    show BE sad
    BE "Oh, man, those things were good. But now I can't look at them without getting queasy."
    MC "You know they make chocolate cream-filled ones, now."
    show BE happy
    BE "They do?! Oh my god I want ninety."
    MC "What happened to looking at them and feeling queasy?"
    BE "Yes, but that was before you mentioned chocolate, and chocolate overrides every other human emotion. Fear, disgust, anger. All fall to chocolate."
    MC "So, you're saying that when White Day rolls around, all you need is some of those cakes and you'll be good to go."
    BE "It doesn't even need to be White Day really."
    MC "So, if I were to point out that they had some of those chocolate cream-filled cakes in the vending machine over there, and went to get two, you'd like one?"
    BE "Are you kidding? Two might not be enough, I'll make the trip myself!"
    "I chuckled as Honoka ran over to the vending machine to grab her delicious snack cakes, making a mental note to myself not to get between her and a box of them if she ever got hungry."
    jump daymenu
    
label BE008:
    scene Dorm Interior with fade
    play music Sunset
    "It was another hot day outside the campus. Too hot for me to bear going outside for any reason that didn't involve diving into a pool of ice cold water. Instead I figured I'd spend the day in my room, catching up on updates of some weekly manga I'd lost track of."
    "KNOCK ! KNOCK !"
    "I had barely gotten started when the door knocked. Daichi was out, so I figured he'd simply forgotten his key."
    MC "Hey, what's up?"
    show BE happy with dissolve
    BE "Oh hi Kei-chan! Good, you're hanging out here, can I come in?"
    MC "Oh!"
    "Seeing Honoka outside of my door was definitely something I didn't expect. But it was far from unwanted. Besides, it was nice to see her head-on without having her run into me like she often did." 
    MC "Yeah, sure, come on in. There's not a rule about having girls in my room is there?"
    show BE neutral
    BE "I don't think so. I can't see why. Unless you were planning something naughty, in which case I am {i}not{/i} prepared at all."
    MC "Naughty? Um. No, wait. No, I can't have been planning anything naughty, you were the one who showed up here in the first place!"
    show BE happy
    BE "Oh. Right. I did do that, didn't I?"
    "Honoka giggled as she walked into my room and slumped down on a nearby seat with a smile. I couldn't help but notice how the forceful way she planted herself down onto the chair made her boobs bounce for quite a while."
    show BE neutral
    BE "So, how's it going?"
    MC "Oh, not bad I guess. Was just hot outside so I was just catching up on some manga."
    show BE surprised
    BE "Ooh, fun, anything good?"
    MC "Without even waiting, she looked at what I'd been reading."
    show BE happy
    BE "Oh neat I haven't seen this one yet. The main character in this is so cool, isn't he?"
    MC "Oh you read this one too?"
    BE "I only recently got into it, but the action's nice. It just stinks the chapters are always so short. But it's got some good characters in it too, doesn't it?"
    MC "Heh, yeah, it does. I just finished this one actually, keep reading, it gets really good in a second."
    "Honoka nodded and scanned along the pages. I waited for the moment I had been surprised by, and saw her hit that point where her eyes opened up wide."
    show BE surprised
    "Whoa! Holy cow, I did {i}not{/i} expect that. I thought Tomoko died like, gosh, chapter 20? How did she survive that attack she took?"
    MC "I have no clue, but I'm guessing it has to do with how she was so powerful, strong enough to take down that robot in one punch. Maybe she became a cyborg or something."
    show BE neutral
    BE "Maybe. Though, I'd hope if they turned her into a cyborg they did more than just make her more powerful."
    MC "What do you mean?"
    show BE happy
    BE "You know. Like, it's no fun to just {i}be{/i} a cyborg if you don't look like one too. You need a cybernetic eye or some wacky hair color, some crazy speech patterns or a constant whirring sound. Make people know you're half-machine, half-badass, all-woman."
    MC "Hmm."
    menu:
        "So what you're saying is, you're not a cyborg.":
            jump BE008_c1
        "Then I guess I need to check you for mechanical parts...":
            jump BE008_c2
        "Error. Does not compute.":
            jump BE008_c3
            
label BE008_c1:
    MC "So what you're saying is, you're not a cyborg."
    show BE sad
    BE "Aw, I'm not?"
    MC "Nope. After all, you don't have any of that fun stuff you mentioned a moment ago. Your hair's plain and brown, you don't smoke or whir when you move. You're all human."
    BE "Ah shoot. You know, I was realllly hoping that offhandedly mentioning my desires for cyborg-ness would suddenly turn me into one for no reason."
    MC "Them's the breaks, Honoka. You're not turning into a cyborg unless you get your hand cut off or something horrible like that."
    show BE angry
    BE "Curses. Then my plot for world domination will be totally useless."
    MC "Pff. Please. What would you do if you took over the world?"
    BE "I'd make snack cakes free for everyone on the planet! And outlaw diet foods."
    MC "That sounds more like something Alice would do if she took over the world. Which, I might add, is the more likely possibility between the two of you."
    show BE neutral
    BE "Hm, you may be right. It's hard to beat wealth like that, even if I'd be all oiled up and ready to go."
    MC "You... You really have a way with double entendres, you know that?"
    show BE surprised
    BE "Huh? What'd I say? I didn't mean to that time..."
    MC "Oh. Well. Never mind then. I must have been mistaken."
    show BE happy
    BE "Heh, or your mind was naughtier than you initially thought, eh?"
    "Don't blame me, Honoka. You're the one who's like a computer virus for my head whenever you come around."
    MC "No, that's not it at all. Let's just, let's get back to reading manga."
    $setAffection("BE", 1)
    jump BE008_after
            
label BE008_c2:
    MC "Then I guess I need to check you for mechanical parts..."
    show BE surprised
    BE "Oh? And how are you supposed to do that, exactly? Going to wave a magnet around me?"
    MC "No, I have a much more efficient method."
    "Honoka actually looked confused and taken aback, which was rare for her. Meaning that I'd be a fool to not take this opportunity."
    MC "Boink."
    "As quickly as I could, I reached out and poked her forehead."
    MC "Hm, nothing there. Boink."
    "This time I prodded her shoulder."
    MC "Boink."
    "That time her hand, which retracted after I poked it."
    show BE happy
    BE "Heh, Kei-chan what are you doing?"
    MC "I have to be thorough now, I need to make sure there's not any robotic parts looking under there. Tachi would be distraught as hell if he knew I brought a cyborg enemy into this place without his approval!"
    "Laughing like a mad scientist, I kept poking Honoka in whatever places I could reach. Eventually I managed to reach her waist, which made her squirm and giggle as she recoiled from the contact."
    MC "Aha, it appears I've found a weakness here. I must examine further!"
    "Spurred on by her reaction, I couldn't help but keep poking her belly wherever I could reach, though by this point it was essentially tickling rather than just poking. It didn't take long to get Honoka stuck in a cycle of laughter."
    BE "Ahaha, K-Kei-chan, hahaha, stop! Ah! Hahaha, oh, not there, ah! Hehehe, you can't, ah! I'm t-too ticklish there, ha! K-Kei-chan!"
    "It was too late to stop now, I was a man on a mission. What that mission was, exactly, I couldn't say, but hearing her laugh like a little kid brought me back to when we used to hang out pretty much every day. "
    "Before I could be brought back too far to the memories of us as kids, I was thoroughly distracted by something that was definitely not there when we were kids."
    "Obviously, since we've spent a fair amount of time together at school already, I'd seen Honoka's breasts bouncing a lot. It hadn't yet gotten to the point where I was used to it and it had lost its appeal, but normal movement had nothing on what was going on in front of me now."
    "My breath hitched in my throat as I saw her bosom heaving up and down with her giggles, the high-pitched squeals coming from her making me feel a bit light-headed as I watched her mounds bounce up and down, a feast of jiggling that I had directly caused thanks to my ceaseless tickling."
    "It only ceased now because I was staring at them so hard I gave Honoka a chance to catch her breath, and slowly settle her mammaries back down."
    "Unfortunately for me, before I could try and defend myself, she went on the offensive, knocking me over and grabbing one of my feet."
    MC "Oh god, Honoka, no!"
    BE "Ahahaha, so this is still your weak spot then?! Perfect! Suffer Kei-chan, suffer the wrath of Honoka Inoue!"
    "I was a goner. How on earth did she remember that I had ticklish feet? She must have a special section in her head for saving embarrassing memories."
    "The girl was relentless, using both hands to torture me. As much as I wanted to kick at her to knock her away, I couldn't, afraid of what exactly I might hit. The suffering only ended when my laughter stopped completely because I was simply unable to take a breath."
    BE "Whew... heh. Well... that was a thing."
    MC "Guh. Honoka, you, geez."
    show BE surprised
    BE "Wow, you seem even more ticklish than you used to be, Kei-chan. That's something. But, I have to say you were a gentleman about when you did it to me."
    MC "Eh?"
    "Honoka helped me up to my feet and we both sat back down, catching our breath."
    MC "What do you mean?"
    show BE neutral
    BE "I mean, I've got some big, obvious, sensitive targets. I was sure you'd go for them once you got started."
    MC "Heh, well. They're actually the reason I stopped."
    show BE surprised
    BE "Is that so? Got cold feet? If so, then I helped you warm them up."
    MC "Haha, no, no, not that, just. Distracted, memories, jiggling. Things."
    show BE neutral
    BE "Mm-hm. I see. I think I see anyway. Well that certainly helped my boredom, which was the reason I came in the first place, but I don't gotta go just yet! Here."
    "Honoka tossed me one of my manga."
    show BE happy
    BE "Let's chill and read for a while. I think you wore me out too much to walk right away."
    MC "Heh, like you're one to talk..."
    $setAffection("BE", 2)
    jump BE008_after
            
label BE008_c3:
    MC "Does not compute."
    show BE neutral
    BE "Oh come on. Who would you rather see in real life: Marumarucha, the awesome green-haired cyborg with visible jetpacks, or Kusanagi, the lame detective who's only a cyborg when she peels off her skin?"
    MC "Uh. I'm not sure if I'd want to see either of those in real life. That sounds dangerous either way."
    show BE sad
    BE "Boooo. You can be a bore, sometimes, Kei-chan. Here, read this and come up with some better ideas then if you're so creative!"
    "Honoka tossed a manga at my head that splayed open to a page that was very flattering for the woman it portrayed, but not at all appropriate to be seen in mixed company."
    show BE surprised
    BE "Oh wow, Kei-chan. I didn't know you liked that kind of manga."
    MC "Oh it's clearly just the fanservice pinup to sell some extra copies..."
    show BE happy
    BE "Heh, I'm kidding. But, hey, you don't mind if I hang for a while, right? I'm kind of bored."
    MC "No, not at all."
    jump BE008_after

label BE008_after:
    "Honoka and I spent the rest of the afternoon together, just hanging out and catching up on manga. It was nice, something I hadn't really had a chance to do with a friend in a long time. Tachi was not exactly the type of guy who would just sit and read unless it was a bunch of conspiracy theories. Honoka was much, much more fun."
    jump daymenu
    
label BE009:
    scene Track with fade
    play music Busy
    "Honoka's soccer club had a match that afternoon. It wasn't too hot, so I decided to come out and watch her for a while."
    "The bleachers weren't filled up that much, but I supposed it was so early in the year that there wasn't much interest in the game yet. Most of them were all rookies, most likely, or at least shaking off the dust."
    "It had been years since I got to see Honoka kick a ball around. She was still just as quick on her feet as I remembered, maybe even more, years of playing since we were separated as kids evident in her skills."
    "She worked the backfield a lot, keeping the ball away from her goalie and sending it back towards the opposing team's half of the field. Both teams were rusty, but Honoka kept the field covered long enough to keep the score at 2-2."
    MC "Boy, she's really holding her own out there. Maybe I should give her a cheer."
    menu:
        "Ho-no-ka! Ho-no-ka! Kick-ing, scor-ing, rah rah rah!":
            jump BE009_c1
        "Dribbling balls, jiggling chest, Ho-no-ka is the best!":
            jump BE009_c2
        "Say nothing.":
            jump BE009_c3

label BE009_c1:
    MC "Ho-no-ka! Ho-no-ka! Kick-ing, scor-ing, rah rah rah!"
    "Several players looked over to the sideline to see who was cheering, Honoka chief among them. She looked down at the ground, but even from this distance you could see an impish grin on her face."
    "It wasn't long after I made a fool of myself that Honoka managed to snatch the ball away from the opposition in the last minutes of play and kick it into the goal. She ended up falling over from the huge force she put onto getting the ball from midfield all the way past the goalie, but it did the trick."
    "After the game was won, Honoka jogged off the field, coming up to where I was sitting on the sidelines. Her gym clothes were ringed with sweat, the bottom curves of her breasts forming a crooked sweat-stain smile across her front."
    show BE happy with dissolve
    play music BE
    BE "Hey Kei-chan! Nice to see you out here!"
    MC "Well I had to at least come see your first match, right?"
    BE "Yeah, that's really nice. I liked your little chant, too."
    $setAffection("BE", 1)
    MC "Sorry it wasn't that good. Next time I'll work on it beforehand."
    show BE neutral
    BE "You better! No slacker cheerleaders in {i}my{/i} section."
    show BE happy
    BE "Just kidding! It was sweet of you to cheer me on."
    MC "I'm glad to hear it. So you're saying you made that last goal because of my encouragement?"
    BE "Hehe, well I wouldn't go {i}that{/i} far. But it definitely helped."
    MC "Awesome. So you're liking the soccer club, then?"
    show BE neutral
    BE "Yeah. It's pretty fun. The coach is nice and the other players are neat to hang out with. Still, almost feels like..."
    show BE sad
    BE "I dunno."
    show BE neutral
    BE "Almost like 'I've done soccer already. Should I try something new?'."
    MC "Huh. Well, it's still early in the year. I guess you could change if you wanted."
    show BE happy
    BE "Yeah, that's the spirit! Thanks Kei-chan!"
    hide BE with dissolve
    "After saying goodbye to Honoka, I stretched my legs out a bit, still sitting on the bleachers. It was so nice seeing her have fun and getting excited about something. A huge dose of normalcy in this weird skill was definitely needed. "
    "I sat there for a few more moments before getting on my way, smiling as I walked back to my room."
    jump daymenu

label BE009_c2:
    MC "Dribbling balls, jiggling chest, Ho-no-ka is the best!"
    "I wasn't a poet by any means, but it was the best I could come up with on short notice. I couldn't even tell if Honoka was able to hear me, I assumed there was a lot of chatter between the soccer players that would drown out whatever I said."
    "Then again, maybe she was able to hear me. It wasn't long after I made a fool of myself that Honoka managed to snatch the ball away from the opposition in the last minutes of play and kick it into the goal."
    "She ended up falling over from the huge force she put onto getting the ball from midfield all the way past the goalie, but it did the trick."
    "The whole crowd cheered after that, including me. She definitely heard that. Honoka ended up scoring the goal with only a few more minutes on the timer. It wasn't enough for the other team to score again. Meaning that for all intents and purposes, Honoka had just won the game."
    MC "Heck yeah! Go Honoka!"
    "After the timer for the game went off, both teams celebrated for a while, hoots and hollers all around. It wasn't until a lot of people had left that Honoka came over to the stands."
    show BE happy with dissolve
    play music BE
    BE "Hey there Kei-chan!"
    MC "Hey, Honoka."
    show BE neutral
    BE "Heh, thanks for the cheer back there, goofball."
    $setAffection("BE", 1)
    MC "Oh! You're welcome. Glad you liked it. I didn't have much time to come up with something."
    show BE happy
    BE "Really? I couldn't tell. Though maybe the fact you immediately went to 'booooobs' was a clue."
    MC "Come on, when we played it was either just 'get the ball in the goal' or 'hit each other with the ball'. I don't know enough about the sport to make insightful comments!"
    show BE neutral
    BE "Yeah I guess that's fair. Though that does remind me of something."
    MC "What's that?"
    "Honoka took that opportunity to kick the soccer ball right at my head, knocking me back a bit."
    MC "Oof!"
    show BE happy
    BE "Hahaha, who's up for a classic game of soccer tag? You're it!"
    hide BE with dissolve
    "Honoka immediately took off running, but only retreated to the soccer field, before beckoning me over."
    MC "Oh you asked for it!"
    "It may have been a while, but I still got on my feet and began chasing after Honoka, dribbling the ball between my feet. Soccer tag was a simple game, as we were young when we made it up. Hit the other person with the ball, and that was about it."
    "Even after playing a full game, it was nice to know that Honoka still had the energy to screw around with me."
    "I wasn't at all surprised when I ended up being the one that needed to sit down and take a break first, but just for a while. It had been a while since we were able to have this much fun with each other."
    "Plus, all the running around felt good. It was always nice to get some air back into the lungs."
    $setSkill("Athletics", 1)
    jump daymenu

label BE009_c3:
    "I didn't want to interrupt the game with a silly chant, especially when the stakes were so low, so I just stayed quiet and watched Honoka play."
    "She really was good. It wasn't long after I arrived that Honoka managed to snatch the ball away from the opposition in the last minutes of play and kick it into the goal. She ended up falling over from the huge force she put onto getting the ball from midfield all the way past the goalie, but it did the trick."
    "After the game was won, Honoka jogged off the field, coming up to where I was sitting on the sidelines. Her gym clothes were ringed with sweat, the bottom curves of her breasts forming a crooked sweat-stain smile across her front."
    show BE neutral with dissolve
    play music BE
    BE "Oh hey Kei-chan, I didn't know you were watching! How long have you been here?"
    MC "Long enough to see you're pretty good still."
    show BE happy
    BE "Heh, thanks. Let me know next time so I can show off for you."
    hide BE with dissolve
    "She gave me a wink and shook her shoulders a bit before leaving to follow the rest of the soccer club. Wondering what kind of 'showing off' she meant, but satisfied that I'd hung around long enough, I got going myself."
    jump daymenu

label BE010:
    scene Dorm Interior with fade
    "Once again, I found myself hanging out in my room after doing my homework for the day. I had been in desperate need of some video game time, so I wasn't doing much except resting on my bed, playing a handheld system."
    "KNOCK ! KNOCK !"
    "The door to the room knocked and I went to open it, still focused on the game. Pausing during boss battles always threw off my rhythm."
    MC "Hello?"
    "I opened the door, still looking at my system the entire time. I was forced to listen to the sound of my character taking a critical hit as two large, white-clad breasts dropped into my field of view and pressed down on the screen."
    "I knew who it was without even looking up. I was grateful for the view, less grateful that I had to pause my game, but even more grateful that Honoka's boobs weren't so big and heavy that they broke my handheld."
    show BE neutral with dissolve
    play music Schoolday
    MC "Hi Honoka."
    show BE surprised
    BE "Oh, you recognize me?"
    "I looked up at her in confusion. She sounded oddly serious. Stepping away, I took a better look at her face, somewhat worried that she'd cut her hair or something had happened to her face. Just something that would make me have trouble recognizing her. Nothing seemed out of the ordinary, though."
    MC "Of course I recognize you. Is something the matter? Why do you think I wouldn't recognize you?"
    show BE neutral
    BE "Because I'm bigger?"
    MC "Bigger?"
    "I held my hand to the top of my head, and then moved it flat towards Honoka. Seemed to be the same height difference as before..."
    show BE happy
    BE "Kei-chan, you dork. I mean, 'bigger'."
    "Her gaze made it obvious what she was referring to, but clearly Honoka wasn't sure that I got the hint. To ensure I knew exactly what she was talking about, she reached down and grabbed her chest, lifting up a breast in each hand, as if she were presenting them to me."
    MC "Oh! Duh, right. That makes sense."
    "It did, but it was strange that she was so surprised about it."
    MC "Did you, like, not believe that your breasts were going to get bigger? You were all about it when you received your confirmation."
    BE "Well yeah, obviously. It's not like I just jumped up a bunch this morning. They've been growing for a while now. Bit by bit. I've been measuring. It's usually somewhere around a centimeter every day."
    MC "Wait, really?"
    "I looked at her chest again. It looked bigger than before, maybe? It was kind of hard to tell. All the past weeks being constantly surrounded by bigger-than-average everything made it a bit difficult to judge growth, oddly enough."
    MC "Huh. Yeah, I guess so."
    show BE sad
    BE "You don't believe me?"
    MC "No no, I believe you. It's just hard for me to see. I've seen you so often, you know? It just kind of snuck up on me, I guess."
    show BE neutral
    BE "Hm."
    show BE angry
    BE "Well that's no good."
    MC "Huh?"
    BE "I came all this way here to show you how proud I am that I grew like thirty centimeters since the start of the year and you didn't even realize it!"
    MC "Oh, um, sorry, I didn't meant to upset you."
    show BE neutral
    BE "You want to apologize to me?"
    MC "Yeah?"
    BE "Alright then."
    "Honoka stepped forward and gained a devious smirk on her face."
    show BE happy
    play music BE
    BE "Touch 'em."
    MC "What?"
    BE "I want you to touch them, so you have proof that they've grown significantly since you first saw them again."
    MC "You... you wha... Uh..."
    "My brain struggled to comprehend what Honoka had just offered. Her tone of voice wasn't like she was trying to be flirtatious or intentionally sexy. It was more like a judo instructor demanding you try and grab their arm so they could perform a flip and toss you onto your back."
    "It just felt like a trap. But, my hand still twitched a bit, trying to fight the impulse in my head. There was nothing that sounded bad about getting a handful of Honoka's chest, it might be worth any potential repercussions..."
    menu:
        "No thanks.":
            jump BE010_c1
        "Well, if you insist.":
            jump BE010_c2
        "Say nothing.":
            jump BE010_c3

label BE010_c1:
    MC "No thanks."
    show BE sad
    BE "Aw, really. Why not?"
    MC "I just... don't think it's appropriate, Honoka. We're friends."
    show BE neutral
    BE "Right, and I'm asking you to touch my breasts. As friends. That's it."
    MC "It just feels weird to me."
    BE "Kei-chan, I've been in female locker rooms before, and a hot spring once too. I've seen at least four girls either offer their breasts or beg to fondle another girl's breasts. It's not as bad as they make it seem in certain anime."
    show BE happy
    BE "But if girls can do it to other girls I don't see why I can't do it with my best friend, right? I have to at least make the offer."
    MC "Oh. Well, when you put it that way I guess it makes more sense."
    show BE neutral
    BE "But, you said you're not comfortable with it, right?"
    MC "I don't think so. Something about it just rubs me the wrong way."
    show BE happy
    BE "Hm, I can't decide if I should reply 'And here I was hoping you'd rub me the right way' or 'Why don't you let {i}me{/i} rub {i}you{/i} the right way then'."
    MC "Ah, heh... for now how about just 'Can I come in and play some video games?' instead?"
    show BE neutral
    BE "Hmmmm."
    show BE happy
    BE "Yeah that sounds good. But you missed a golden opportunity Kei-chan. Heaven forbid, what if that's it and my growth stops there? You'll have missed your chance, the magic will be gone."
    MC "Well, er, if the offer was still on the table, couldn't I take it up at some point in the future?"
    show BE neutral
    BE "Sure, but then, they won't be, you know, freshly-grown. They'll be like, overripe. This would have been grabbing a melon right at its peak of freshness, when the rind is just right and the insides are the juiciest."
    MC "I'm not really sure if you should be describing your breasts as juicy."
    show BE happy
    BE "Well, I considered comparing them to coconuts, and then I could have said they were milky inside, but then you would have made a crack about them being brown and hairy, right?"
    MC "I will not admit to something that didn't even happen, nor will it ever happen."
    show BE sad
    BE "I suppose that's a smart move."
    MC "Thank you."
    show BE happy
    BE "Which makes that the smartest thing you've said since I came in to visit."
    MC "Hey! Take that back or I won't invite you in for a choco-cola."
    BE "Ooh what, you've got some?! Gimme gimme gimme."
    "Honoka's hands greedily reached out for a nonexistent soda. If anyone performed the same gesture at her it would have been very obvious what they were trying to grab, but Honoka's was more about soda cans, not cellulite cans. I invited her in to share a drink and relax anyway."
    "As tempting as it would have been to grab some of Honoka's chest, it didn't feel quite right. We're friends. Friends shouldn't do that. At least, that's what I thought."
    jump daymenu

label BE010_c2:
    MC "Well, if you insist."
    "At Honoka's pleading, I reached out towards her chest. It was only when my hands were an inch or so away that I realized I had no idea what I was doing. Was I supposed to just push my palms in? Or should I try and support them from the bottom?"
    MC "You know, this will be my first time doing this."
    show BE happy
    BE "Well, then I'm honored to be your first."
    MC "Oh, please don't say it like that. It's going to make this sound way naughtier than it already is."
    hide BE with dissolve
    "Seeing Honoka zip her lip, I finally crossed the threshold and pushed my hands into her chest. I don't know what sensation I expected her chest to have, but somehow it felt like everything all at once. It was soft, that was for sure, it was easy to discern that from how my hands sank into their masses a good couple of inches."
    "Honoka still had a smile on her face, so I kept examining them. I felt like a doctor, medically probing her, but really all I was doing was trying to take in the feel. Soft, yes. Squishy as well. I swore they made sounds like stress balls being squeezed as I applied a bit of pressure to them."
    "But, also, they were... dense. It seemed like an odd term to describe breasts, but it was accurate. For as big as they were, they still felt heavier than I expected them to. I carefully moved my hands so they cupped Honoka's boobs instead, and pushed up. They took a slight bit more effort to move than I thought they would, and when I finally pulled my hands away, I got to see them bounce for a few seconds before stopping."
    MC "Wow."
    show BE happy with dissolve
    BE "Heh, heh. Get yourself a good handful? How did they feel? Were they as soft as you imagined? Were they warm? Tell me!"
    MC "Whoa, um, well. They're... big?"
    BE "And?"
    MC "Soft?"
    show BE neutral
    BE "Yes, yes, and?"
    MC "I, I, I don't... they're awesome?"
    show BE happy
    BE "Thaaat's the ticket. Boobs are awesome, aren't they?"
    MC "Well. Not by default, no."
    BE "Ah, you're saying they have to be at my size to be any good at all?"
    MC "Not necessarily. Yours definitely... transcend most sizes though. And probably eclipse a lot of them in softness too. They've bumped into me before but, it really feels different in the hand compared to the back of the head."
    show BE sad
    BE "That's good to know. It kind of stinks I don't get to experience them in that way."
    show BE happy
    BE "Though, since they're attached to me, I guess I get a whole unique experience that nobody else would get. So, that's pretty cool, too."
    MC "Right. I'm sure there are lots of girls who would like to be in your position."
    show BE neutral
    BE "Haha, probably. But, only a few girls in the world are going to get big whompers like this, and they're not done growing yet."
    MC "Well. Here's hoping."
    "Something still bugged me. Honoka seemed completely fine, still, but, I had to probe a bit deeper."
    MC "Hey, Honoka?"
    BE "Yeah?"
    MC "In all seriousness, why did you ask me to grab your breasts?"
    show BE happy
    BE "Oh, is that what happened?"
    MC "Yeah, it is."
    BE "Ah, ah. Think back, Kei-chan. I just asked you to {i}touch{/i} them. You could have easily just poked them, and that would have sufficed. Or even just gave them a quick little grope. But, nope. You took hold, and you didn't let go for eighteen seconds. I counted."
    show BE neutral
    BE "You know what that means?"
    MC "N-No?"
    show BE happy
    BE "Hehehe..."
    "Honoka suddenly loomed forward, her breasts inches away from my face. My knees buckled. I felt like I was suddenly talking to Shiori, not my childhood friend."
    BE "It means I know what kind of guy you are."
    MC "I... um."
    BE "A guy who takes charge and opportunity when he can."
    hide BE with dissolve
    "Honoka pulled back and smirked at me, her smile looking like it could slide off of her face. She grabbed the handle of my door with one hand, and then turned to wink at me."
    show BE happy with dissolve
    BE "And I like that kind of guy."
    hide BE with dissolve
    "With that, Honoka shut the door behind her, leaving me to wonder what just happened."
    $setAffection("BE", 1)
    jump daymenu

label BE010_c3:
    MC "..."
    "I just couldn't say anything. My mouth felt like it dried up. Something about this was wrong. I wasn't sure what her game was, but I felt like the smart thing to do was just shut up."
    show BE neutral
    stop music
    BE "Hello, Kei-chan?"
    "The only sound that managed to come out of my mouth was a weak, guttural stutter."
    show BE sad
    "Okay, Kei-chan. I get the message."
    "Honoka pulled back her balloons and wordlessly left my room, leaving me utterly confused. She only came in to show off her breasts? It just didn't make sense. Maybe she wasn't feeling well. Hopefully she went off to her room to relax for a bit, it seemed like she needed it."
    $setAffection("BE", -1)
    jump daymenu
    
label BE011:
    scene Track with fade
    play music Busy
    "It was another gorgeous day here at Seichou Academy. Though the weather as of late was beginning to edge towards the cooler side of temperatures, the sun was still bright enough, and warm enough, that many people were still hanging around outside in summer clothing."
    "I'd heard that Honoka's soccer club was having another game today, so I thought it'd be nice to pay her another visit. I'd brought along a sweatshirt in case it did begin to get too cold, but if I figured out some cheers again, I'd have some reasons to move around and get the blood flowing."
    MC "Huh, wonder where Honoka is."
    "I hadn't been to enough games of soccer to recognize most of the players, but there was a certain brunette friend that wasn't visible in the masses."
    MC "Huh. I wonder if she's sick or something? Maybe I should go check on her. Maybe there's a place around here that sells chanko, a bowl of that always helps when I'm sick."
    "I soon found out that Honoka wasn't sick, because two large spheres pressed against my shoulders from above me."
    show BE happy with dissolve
    BE "Hehe, no I'm not sick. But for future reference, if I do get sick, I much prefer chocolate to feel better."
    MC "I'm fairly certain that has no basis in fact."
    BE "Hey, I don't control what my body does. In more than one way."
    "Honoka stuck her tongue out in a joking matter, before sliding off the bleacher above me to join me on my row."
    MC "Well, if you're not sick, mind explaining why you're not on the soccer field? You did great the last time I saw you play."
    show BE sad
    BE "Ah, yeah. Sorry, I guess I forgot to tell you. I decided to quit the soccer club."
    MC "Huh? Why?"
    show BE neutral
    BE "Honestly it was just getting a bit boring. No, boring isn't the right word. It was still exciting going up against another team. But, I guess I felt like I wanted something more."
    MC "So you're not going to join another club?"
    show BE happy
    BE "Oh no no! I'm definitely going to join another club. I've already got a few that I'm thinking of joining. Soccer was fun, but, how do I put this? Oh!"
    show BE neutral
    BE "It was just something I'd already done before, you know? You and I used to play all the time and I never really stopped liking it. I just felt it was time to move onto something else. We're in this huge school after all, with dozens of clubs. Something out there's just bound to be right for me."
    MC "So, you just quit because of your past experience with it then?"
    show BE happy
    BE "Yep, that's it!"
    menu:
        "Are you sure it wasn't because it was getting harder to see the soccer ball?":
            jump BE011_c1
        "It's okay, that club was dumb anyway.":
            jump BE011_c2
        "Oh, makes sense. Hope you find a new club soon.":
            jump BE011_c3

label BE011_c1:
    MC "Are you sure it wasn't because it was getting harder to see the soccer ball?"
    show BE neutral
    BE "Eh?"
    MC "I mean, you just went through a sizable growth spurt. Soccer can't be the easiest thing in the world when you look down and just can't see the soccer ball. Your, uh, endowments were probably getting in the way, weren't they?"
    show BE happy
    BE "Pff. Kei-chan, always thinking about boobs. I know they're magnificent. But, no, that wasn't the reason. I just needed a change. That's all."
    MC "Ah okay. Fair enough. Yeah, I uh, sorry I didn't mean to imply anything. Trust me, I had a whole list of non-boob-related chants all ready for you to cheer you on. They're all going to go to waste now! Whatever club you do next I'll have to come up with new ones."
    MC "Unless you end up in like, the chess club or something."
    BE "Are you kidding? You better come up with cheers for that, or it'd be boring otherwise!"
    MC "You know chess matches are supposed to be quiet, right?"
    show BE angry
    BE "Kei-chan if, heaven forbid, I join a chess club, I demand that you call me the Castling Castellan!"
    MC "I... I don't even know what that is."
    show BE happy
    BE "Then come up with something better, because that was obviously terrible."
    MC "You have my word I'll make something cheery that doesn't get confusing. Now, we should probably watch the game now, huh?"
    BE "Sounds good to me."
    jump daymenu

label BE011_c2:
    MC "It's okay, that club was dumb anyway."
    $setAffection("BE", -1)
    show BE neutral
    play music Tension
    BE "Excuse me?"
    MC "I mean, it, um, why do you look angry?"
    show BE angry
    BE "Because, Kei-chan. I was literally just in that club. Are you saying I'm dumb because I was in it?"
    MC "What?! No, no, not at all. I was just trying to make you feel better."
    BE "I didn't leave the club on bad terms, Kei-chan. I liked a lot of the people I played with. It's not like I just walked out and never thought I'd see them again. I came here to watch them play."
    MC "I, I'm sorry. I didn't think that through."
    show BE sad
    BE "It was hard to leave it, you know? I knew it was the right thing to do, what I wanted to do. But that didn't make it any easier, regardless of how short my time there was."
    MC "You're, you're absolutely right, Honoka. I'm sorry, I, I just shouldn't have said anything."
    show BE neutral
    BE "Yeah well, it's, it's fine."
    "It was easy to see that it wasn't fine."
    MC "I'm sorry. Here, I don't want to sour your mood anymore."
    "I stood up to leave the game."
    MC "I'm really sorry for what I said, Honoka. Here, enjoy the game, I hope you have fun, sincerely."
    hide BE with dissolve
    BE "I tried not to look back at the bleachers as I left the soccer field. Honoka was never the type to hold grudges, so I didn't think this would come back to bite me later. But I still felt like an idiot saying what I said..."
    jump daymenu
    
label BE011_c3:
    MC "Oh, makes sense. Hope you find a new club soon."
    show BE happy
    BE "Thanks! I hope so too. Any recommendations?"
    MC "Hm. I haven't really looked around all that much myself in terms of clubs. If there's any sort of video game club that would be fun."
    show BE neutral
    BE "Yeah. it would. But, I think I really want to stick to something athletic. It's good for exercise, you know? Plus it's always nice to get outside."
    MC "That's a good point, but the weather seems like it's going to get cool soon. You may want to look at something that would keep you inside for the semester."
    BE "I guess that would cut out things like baseball, right?"
    MC "Yeah, baseball would definitely be a no-go. What about, um, basketball? I know we have one of those here."
    show BE happy
    BE "Basketball. Yeah, that might be a good idea. Hm, maybe I'll look into that then."
    show BE surprised
    BE "Ooh, Koneko-chan just scored a goal already! Woo, go Koneko!"
    MC "Oh wow, what? Dang that was quick. I guess I should be paying attention, huh?"
    show BE happy
    BE "Hehe, yeah, come on. Let's keep watching, this should be fun!"
    MC "Yeah looks like a good game, go Koneko!"
    $setAffection("BE", 1)
    jump daymenu

label BE012:
    scene Campus Center with fade
    play music Busy
    "It was sometimes a bit annoying to track down Honoka when I wanted to find her. She was never really the type to have a regular hangout spot. With some of my other friends, I had a vague idea of where I could find them. With Honoka, she could have been in a dozen different places at least. I suppose it came with being such a free spirit."
    "Heck, if we hadn't lived next door to each other, I don't know if we'd have met enough times to be considered friends, let alone best friends."
    "It wasn't anything of vital importance I wanted to discuss with her, so it easily could wait until the next time we ran into each other."
    play sound Boing
    "Then Honoka, as she often did, literally bumped into me."
    show BE happy with dissolve
    BE "Kei-chan! Woo, hey! What's going on?"
    "Honoka was always a happy-go-lucky sort but she seemed extra cheerful today. That was a good sign. Maybe she'd be willing to hear me out, then."
    MC "Hi Honoka. Oh, not much, really. I was looking for you, actually."
    BE "Oh, yeah? Why didn't you just call me?"
    MC "Um, well now that you mention that, I don't think I have your phone number."
    show BE surprised
    BE "Wait, really? How on earth did I go this long without getting yours? Dummy!"
    "Honoka laughed to herself as she stuck out her tongue and playfully rapped her knuckles on the top of her head. It had the very pleasant side-effect of making her bosom jiggle."
    MC "Well here, let's fix that now…"
    "With embarrassment lurking behind our actions, Honoka and I exchanged our contact information."
    MC "Really? Your email address starts with 'beachballs'?"
    show BE happy
    BE "Hey I came up with that email when I was at the beach like six years ago!"
    MC "Uh-huh, I'm sure."
    show BE neutral
    BE "Anyway, now that you can buzz me any time, what did you want to talk about?"
    "As she put her phone away, I tried not to stare too long at how envious I felt of a simple cell phone that didn't even have the ability to realize it was nestled in a breast pocket."
    MC "Right! I've been a bit cooped up lately. I wanted to head out to the city. There's an arcade there. You wanna go with?"
    show BE surprised
    BE "Arcade?! Heck yeah I wanna go with you. When were you thinking of going?"
    MC "Now, if you're able."
    show BE happy
    BE "Yeah, I'm totally able to go right now, I've got everything I need with me. Was it close enough to walk?"
    MC "If we move quickly we can catch a bus there that'll make it much quicker."
    show BE neutral
    BE "Well what are we waiting around for? Hurry up!"
    hide BE with dissolve
    "Honoka immediately began running."
    MC "Honoka!"
    show BE neutral with dissolve
    BE "Yeah?"
    MC "It's that way."
    "I pointed in the opposite direction."
    BE "Oh. Heh. Okay, fixed!"
    scene Town with fade
    show BE neutral
    "Now that she was headed in the right direction, I followed Honoka to the bus stop, where we were just in time to hop aboard. With a little more hop in Honoka's case. After a few stops, we ended up in a small shopping district in the city."
    MC "Now, if I remember the directions right, we just go this way, and take a right, and we should be there soon."
    show BE happy
    BE "Perfect."
    scene Arcade with fade
    "Honoka and I shared a lovely, albeit quick walk over to the arcade. Even before we stepped inside we could tell what it was, thanks to the many noises of buzzers and bells going off from pachinko machines."
    "But, Honoka and I preferred games of skill. Or at least games that were more fun than sitting at a machine, watching balls drop. So we searched out one of our old favorites."
    show BE neutral with dissolve
    BE "Oh, hey, check it out. I think I see a Mecha Killer Xtreme DX cabinet that's free. You want to play one match for old time's sake?"
    MC "Sure. But only if I get to be Delta Debonair."
    show BE happy
    BE "Psh, if you want to be the lamest character on the roster, go for it. Beta Beautifully is all mine."
    "I chuckled as Honoka went over to the other side of the cabinet. We slid in our tokens and each picked our characters. With my hands on the controls I prepared myself for the game. I've had lots of practice with this game. I could crush Honoka if I wanted. But would that be too mean?"
    menu:
        "Thrash her.":
            "It had been too long since we played this together. When we were younger she used to beat me all the time. But now, I had the upper edge. I would beat the crap out of her."
            MC "Alright, Honoka. I'm ready whenever you are. Get ready for a pounding!"
            BE "Bring it!"
        "Play fair.":
            "I decided that it was just supposed to be a fun game. Besides, for all I knew she had been playing as well. I figured that I would just play reasonably well and see what happened."
            MC "Okay, Honoka. Are you ready to play?"
            BE "Oh yeah. This is gonna be fun."
            MC "Heh, it is. Play well."
        "Let her win.":
            "While we'd played together a few times since coming to Seichou Academy, it had been years since we were able to play MKXD together, especially on a classic machine like this one. I didn't want to get her upset either, so I thought it would be best to play it safe and easy."
            BE "Come on, Kei-chan, you ready to play yet?"
            MC "Yep. Sorry I'm just nervous, it's been a while since I played."
            BE "Oh is that so? Well, I'll go easy on you, then. Let's go!"
    scene black with fade
    pause 1
    scene Arcade with fade
    show BE happy with dissolve
    play music Tension
    "As soon as the game began, I was doomed. Before I could even move my character, Honoka had leapt across the stage, performed a 14-hit combo on me, and removed a third of my health bar in one go. From her side of the cabinet, I could hear the announcer cheering her on for her devastating attacks, while he berated me on my side."
    MC "Geez, Honoka. How many, gah, times have you played this?!"
    "I had no idea what I was doing anymore. Any semblance of strategy went out the window as soon as Honoka began destroying me with such ease. My fingers ended up becoming a frenzy of button-mashing. "
    BE "Hehehe, hah, take that. Yeah. Nngh. Oh, only about ten hours a week for the last five years. Mega-Combo!"
    MC "What the heck is a Mega-Combo?!"
    "Apparently it was a cheat move designed for only Honoka to use, because that's what it felt like when she eliminated the rest of my health bar with a single attack."
    "The announcer crying out the second round only dashed my hopes instead of encouraging me that I could make a comeback. I hadn't landed a single hit on Honoka the whole first round, and now she had a full special meter charged up, unbridled confidence, and a devious cackle that chilled me to the heart."
    MC "Hey uh, Honoka? You know this is just a game, right?"
    BE "Hahahaha!"
    "All the combos I'd learned playing the game. All of the special attacks. Gone. Like flames in a rainstorm. I may as well have taken my hands off of the controls for all the good it did me."
    BE "Now behold my final attack!"
    "I was too scared to even ask what that could be. My character was reduced to a pile of scrap metal in seconds. Then the scrap was crushed into a cube, and the cube was fed to a robotic dog. The cinematic thankfully ended before the inevitable next step in the process."
    "I stepped out from behind the cabinet to stare at her."
    MC "…"
    play music Schoolday
    BE "So was I good?"
    MC "Good?! How the heck did you do all that? You could go professional with those skills."
    show BE sad
    BE "You know, I actually looked into that. But apparently all the pros have moved onto Mecha Killer Ultratopia Nice Fight instead, and MKUNF just isn't as good as MKXD."
    MC "Uh, why's that?"
    show BE neutral
    BE "Because there's no Beta Beautifully, duh."
    MC "I… I see."
    show BE happy
    BE "But that was fun! I hadn't played you in that in forever. Hey, you wanna rematch?"
    MC "…"
    MC "Let's uh, let's play something else next."
    scene black with fade
    "We continued playing for a little while, but it started getting late..."
    menu:
        "Stay at the arcade":
            $addMeeting("BE013", DeltaTimeEnum.NUMDAYS, 0, True)
        "Leave":
            "We left the arcade together."
    jump daymenu
    
label BE013:
    scene Arcade with fade
    play music Busy
    "After the devastating loss I suffered at Honoka's skilled hands, I needed something simpler. Preferably something where she wouldn't destroy me. Which likely meant a game that wasn't even competitive."
    MC "Hey, do you want to try out that Citizen Wicked lightgun game? It's two player co-op."
    show BE happy with dissolve
    BE "Sure, that looks good. Wanna see who can get the better score?"
    MC "N-No, let's just see if we can get to the end of the game without blowing a few thousand in yen on it, huh? These things are coin thieves."
    BE "Eh, what else are we going to spend it on? School supplies and food? Nah, video games, Kei-chan. Video games."
    MC "Your nonchalant attitude towards education is worrying."
    BE "Hey, school's important, but video games give good real world experience."
    MC "Oh? How's that, exactly?"
    "I wondered if she even had an answer to the question as we walked up to the cabinet and began paying our initial fee."
    show BE angry
    BE "It teaches how to survive a zombie apocalypse."
    MC "I'm not quite sure if you can put that on, say, a job application."
    show BE happy
    BE "Oh hush and grab your pistol."
    "I was fully aware that the gun that Honoka held was entirely made of plastic, had no capacity to shoot bullets, and could not harm me in any way."
    "I still decided that the best course of action was to do as she commanded, lest I incur her wrath."
    BE "Right on, let's go."
    hide BE with dissolve
    "Honoka selected the two-player option and we began our quest to annihilate every zombie we could find. With the other sounds of the arcade creating a cacophony in the background, it was somewhat hard to hear the game."
    "Not that it mattered much. It was just point and shoot action. Then dying, and putting in more tokens. Then dying again, more tokens. "
    "Death, token."
    "...Death, token."
    "Until eventually we realized that we had spent way too much money on one game and would be done with the trip before it even began if we kept playing the game."
    show BE angry with dissolve
    BE "Grr, this stupid boss is totally crap. You wanna stop?"
    MC "Yeah, I can't get two shots on him before he hits me."
    "We both holstered our pistols and left the game as the countdown timer ticked down to zero."
    MC "So, let's see, what next? Air hockey?"
    show BE happy
    BE "Sure! Bet I'll beat your score at least three times over."
    MC "At this point I didn't doubt she would. But she tilted her head as we approached the table."
    BE "Oh snap, Koneko! Hey, wassup!"
    MC "Honoka dashed over to a darker-skinned girl and threw herself into a strong hug that squeezed the blonde tight and made it look like her spine was about to snap."
    Koneko "Oof, like, what are you doing here, Honoka?"
    BE "I'm hanging out with Kei-chan. Kei-chan, this is Koneko, she's in the soccer club."
    MC "Oh, oh, cool!"
    "I extended my hand to shake hers. Every finger on Koneko's hand was studded with rings, and at least three bracelets on each wrist. Her hair was clearly dyed, and her makeup was thick, to say the least."
    Koneko "Yep. You may know me as the, like, gal who scored the winning goal this last game."
    if isEventCleared("BE011"):
        MC "I do, in fact. Good to meet you."
        Koneko "Oh yeah, totes same."
    else:
        MC "Oh, really? Wow. Congrats. Sounds like a close game, then."
    BE "So, Koneko, what are you up to? Me and Kei-chan were going to play some air hockey."
    Koneko "Oh, you know, like, seeing if there were any cute boys around."
    show BE neutral
    BE "Again? I thought you were dating that Takeda guy?"
    Koneko "Yeah for like, two weeks. Then he got weird and mopey."
    BE "Mm… Kei-chan, you know anyone who would hook up with Koneko?"
    "My mind attempted to flip through a list of all the guys I knew. Unfortunately the only name that came up was Daichi."
    MC "No. Not at all. Sorry."
    Koneko "Lame. Well, whatev, I'll see what I can find. Have fun you too. Wait…"
    BE "Huh, what's up?"
    Koneko "Is this like, the guy you were talking about?"
    show BE angry
    BE "Koneko shut up! Get out of here, already, god…"
    "I couldn't help but look confused as Koneko snickered and walked away, leaving Honoka looking flustered for some reason."
    MC "Are you okay?"
    show BE surprised
    BE "Yeah I'm fine. Koneko's just a, she's…"
    show BE angry
    BE "Let's just play air hockey!"
    MC "Er, yeah okay."
    hide BE with dissolve
    "Honoka slipped a token into the table and the air began to push out as she grabbed the disc and made the first shot before I really had time to react. I still managed to hit the puck, but she bounced it back at me."
    "She scored the first point. Then the second and third. By the fifth point we were both hunched over the table, trying to outdo the other. She wanted a perfect record. I just wanted to score a measly point."
    "But it didn't matter. She ended up destroying me with 12 points to 0. As she cheered and mocked I didn't have the heart to tell her what an unfair advantage she had."
    "With her torso bent over, her boobs completely blocked her goal."
    jump daymenu
    
label BE014:
    play music Peaceful
    scene Hallway with fade
    "The day started off rather frustratingly. Mainly due to my own indecision about whether to have miso soup or oatmeal for breakfast that morning. In the end, I waffled so much over the decision that I had to settle for toast instead."
    "There was a welcoming bounce in my step soon after, as a familiar set of wobbling breasts collided into my back, while Honoka's arms wrapped around my sides."
    show BE happy with dissolve
    BE "Morning, Kei-chan!"
    MC "Good morning, Honoka."
    BE "How's your morning going?"
    MC "Oh, pretty good all things considered. Just a bit hungry."
    show BE surprised
    BE "Hungry? Didn't you eat breakfast?"
    MC "Yeah, not much though."
    show BE sad
    BE "That won't do. Here, I'll split this with you."
    "Honoka, still behind me, pulled one of her hands away from my side. It returned moments later with half of a granola bar resting on its palm."
    MC "You're sure?"
    show BE happy
    BE "Of course. I can't have you starving in the middle of class!"
    "I nodded and took her snack, munching on it as she let go of me so I could face her. Once I did, I was immediately drawn to her cleavage. Not for normal reasons, however. Instead it was thanks to the myriad of crumbs I saw dotting the curves of her bosom."
    MC "Uh, hey Honoka?"
    show BE neutral
    BE "What's up?"
    MC "Where exactly were you keeping this granola bar?"
    show BE happy
    BE "In my pocket, silly."
    "Honoka chuckled as a hot blush came to my face. It was obvious where I was staring, and where my brain was."
    MC "Sorry, I just, well, I know girls do that sometimes."
    show BE neutral
    BE "Sure, but not with these things, they crumble like dust. It'd be like trying to keep a piece of styrofoam between two wrecking balls. You're just asking for trouble."
    MC "Heh, yeah, you're right. It is crumbly. Kinda dry too."
    show BE unique
    BE "Oh, then here."
    "Honoka then proceeded to reach right into her cleavage and come out with a small can of fruit juice. She proceeded to pop the top open and take a swig before handing it over."
    "I grabbed it gingerly between two fingers and stared at it."
    show BE angry
    BE "It's a drink, Kei-chan. Not some alien snake."
    menu:
        "Now you're going to put the thought of cleavage-snakes in my head.":
            jump BE014_c1_1
        "I'm just relishing the moment, that's all.":
            jump BE014_c1_2

label BE014_c1_1:
    MC "Now you're going to put the thought of cleavage-snakes in my head."
    BE "Hey I said alien snakes, that's completely different."
    "Honoka snickered to herself as I held the drink to my lips. With a shrug I took a few sips so I could finish my granola bar and handed it over."
    show BE neutral
    BE "Heh…"
    "Honoka gave a look at the can as she took a drink herself, looking oddly pensive."
    MC "What's up?"
    show BE happy
    BE "Oh, just thinking about how some guys, or girls, would make a big deal out of sharing a drink. But it's not like it's the first time we've done that. We used to split milkshakes, what, once a week?"
    MC "Well yeah, the good ones were so expensive. And fattening, too."
    show BE happy
    BE "True. But we always worked it off playing afterwards. Oh! Speaking of, I applied to the basketball club. They're going to let me in."
    MC "Cool."
    show BE angry
    BE "That's it? Just 'cool'?  Show some enthusiasm, ya jerk."
    "Honoka gave a teasing punch on my arm. I really was concerned that spot was going to bruise one day, regardless of how light the taps were."
    MC "Sorry. I mean, that's awesome. Congratulations. So you're going to be bouncing around all over the place, huh?"
    show BE neutral
    BE "Oh yeah. Lots of bouncing. But in basketball they call it dribbling. But it's clearly just bouncing. Same thing. They just had to throw their 'sporty' word on it."
    MC "When does that club play?"
    BE "I think it's like, twice a week. I want to say Tuesdays and Fridays but there's practices and stuff all the time too. So if you ever swing by the basketball court you'll probably see me."
    MC "Hey sounds fun. I'll have to check it out."
    jump BE014_c1_after

label BE014_c1_2:
    MC "I'm just relishing the moment, that's all. It's not every day a woman lets you drink out of her breasts."
    show BE unique
    BE "To clarify, you're having a drink that was located between my breasts."
    MC "Right, I don't want people getting the wrong idea. Though I'm curious now."
    BE "About what? No, they aren't leaking."
    "Honoka stuck her tongue out at me jokingly and I couldn't help but laugh."
    MC "No no no. Well, it's related to that. When you heard 'drink out of your breasts', did you think, like… pouring it down the cleavage?"
    show BE aroused
    BE "No, that was not what I was thinking."
    MC "Oh, okay."
    show BE happy
    BE "Was it what you were thinking?"
    MC "Not at all."
    $setAffection("BE", 1)
    BE "Cool, so we're both perverts then."
    MC "I guess when it comes to that turn of phrase, yeah we are."
    "The laughter between us lasted for several seconds before it devolved into an awkward silence. It was hard to transition a dialogue away from discussions like that. Thankfully Honoka didn't need proper segues to move onto a new topic."
    show BE neutral
    BE "I uh, joined the basketball club."
    MC "Good! Basketball's good. Good for, uh. Good things. Like shooting, and passing, and bouncing."
    BE "Yeah, heh. All girl's basketball team too, so there's going to be lots of bouncing around for sure. Though not from Misao. She's like a piece of cardboard, that girl..."
    MC "Well you never know. Maybe she'll end up having, uh, massive hands or something and nobody will be able to steal the ball from her."
    show BE happy
    BE "Maybe. Not like they'll get a chance to take it away from me, anyway. If you come to my first game, watch, I'll score 20 points all by myself."
    MC "You will? That's a lot, you think you're up to it?"
    "Honoka puffed up her chest and smiled, closing her eyes."
    BE "I'm up for anything!"
    jump BE014_c1_after

label BE014_c1_after:
    play sound ClockTower
    "Our discussion was cut by the sound of the morning bell signaling that class would start soon."
    MC "Ah, we better hurry. Don't want to be late."
    show BE neutral
    BE "Yep, let's get a move on."
    "Honoka and I began the walk to homeroom as we tossed our trash in a receptacle nearby."
    MC "Oh, hey, Honoka. Thanks for breakfast."
    show BE happy
    BE "Heh, anytime Kei-chan."
    jump daymenu

label BE015:
    scene Hallway with fade
    play music Schoolday
    show BE sad with dissolve
    BE "Kei-chan, can you help me with some studying?"
    "Honoka looked at me with pleading eyes. It was like staring at a squirrel begging you to throw some granola at it so it could scurry away. I hadn't expected her to run into me after class today. By this point, I really should be prepared."
    MC "Studying? I guess I could help. What subject, specifically?"
    show BE angry
    BE "I need help for the math test tomorrow. If I have the formulas with me, I can work out the problems, most of the time."
    MC "But we're not allowed to use formula guides on the test."
    show BE neutral
    BE "Right. I just need some help kickstarting my brain to help me memorize the formulas."
    MC "Well that doesn't sound too hard. Do you want to come over later?"
    BE "Actually, I was hoping we could do it now, if you're free? I have a club meeting later."
    MC "Hm. Sure, yeah, don't see why not."
    show BE happy
    BE "Great, can we just do it at your room."
    MC "Okay. Tell you what. I'll meet you there, I'll be over in a few minutes. I just want to pick something up first."
    BE "Gotcha. I'll meet you there, then. Don't be late!"
    "Honoka ran off to the dormitories as I looked at the time. I had to make a quick stop first. I had a feeling there was an easy way to help Honoka with her studying."
    scene black with fade
    "When I made my way back to my dorm room, Honoka was waiting outside."
    scene Dorm Interior with fade
    show BE happy with dissolve
    BE "Good, you're here. Let's get going!"
    "She looked at me quizzically for a moment as she noticed the bag in my hand."
    show BE neutral
    BE "What's the stuff for?"
    MC "Here, let's sit down and I'll show you."
    "After settling in and grabbing some water for both of us, I pulled out some index cards I purchased at the school store."
    MC "So the first thing I want you to do is to make some flash cards. Write down the formulas on one side, then the name and what they're for on the back."
    show BE sad
    BE "Okay. Then you'll help me answer when given one or the other?"
    MC "Yeah. But we'll get to that. Here I bought enough for myself, too. I figured it would be good for me to study as well."
    show BE neutral
    BE "Sure. Okay, toss me a pencil."
    "I handed Honoka a pencil, and a notebook to write on, and we started working on making ourselves flash cards. It was something I really should have done on my own volition, but better late than never."
    "It gave us more time to discuss the formulas themselves. What each symbol meant and when to use them, allowing us to give more accurate descriptions on the backs."
    "After a while we'd both finished a small stack of cards."
    show BE happy
    BE "Perfect. Thanks, Kei-chan. This is going to be a big help."
    MC "Hang on, we're not done yet."
    show BE sad
    BE "We're not? But, ugh that was like… fifteen minutes of studying already."
    MC "Yeah but you're never going to remember anything from that small amount of time. That's why I had this idea."
    "I reached back into the bag from the school store and pulled out a box of choco-cream cookies."
    show BE aroused
    BE "Ooh, can I have one?"
    "I knew she'd ask even before I offered, or went on to explain why I had them."
    MC "Only if you can tell me the quadratic formula."
    show BE surprised
    BE "Oh."
    show BE neutral
    BE "Crap."
    show BE sad
    BE "We're doing this?"
    "I couldn't help but feel a bit of a smirk come to my face as I saw Honoka's expression change from joy at the cookies to utter fright."
    MC "Yep. So, quadratic formula."
    show BE neutral
    BE "That's… okay. X equals… negative B plus or minus 4A squared over 2C?"
    "I shook my head."
    MC "Sorry. Nope."
    "Giving her a moment to notice, I ate the cookie."
    show BE surprised
    BE "Ah! Kei-chan! Those only come twenty to a pack!"
    MC "Oh I know, and while I could eat all twenty I'd prefer if I didn't have to. So, next up."
    "I looked over my own flash cards for a question."
    MC "What is the name for the probability formula, where the probability of the union of A and B... is equal to the probability of A, plus the probability of B, minus the probability of the intersection of A and B."
    "I held up the card with the formula on it so she could read it properly, as well."
    show BE neutral
    BE "That's the rule of addition."
    MC "Got it."
    "I handed Honoka her cookie as her reward."
    MC "Okay, next up. What is the permutation formula?"
    "Honoka munched on her cookie, and focused for a moment."
    show BE sad
    BE "That's N factorial over… um."
    "I dangled the cookie between my fingers."
    show BE neutral
    BE "N factorial over N-K… with the whole bottom factorial as well."
    MC "Awesome. Good work."
    "Despite getting two right in a row, Honoka's next question was answered incorrectly, meaning I got to enjoy another cookie myself. I wanted her to do well. These cookies had a serving size of '1 cookie'. More than five would hurt."
    "But, it definitely seemed to be working. Maybe it was just the rush of sugar helping Honoka focus, but she was definitely getting more right than she got wrong. By the time she'd gotten to the end of the box, I'd wager she ate about 75%% of its contents."
    "I felt like it helped me as well. More than just the flash cards, reading them out loud for Honoka's studying made me feel like I had a better grasp on the topic as well."
    $setSkill("Academics", 1)
    MC "So. You think you're ready now?"
    show BE happy
    BE "Yeah I think so. It's better than I was doing before anyway."
    MC "Glad to hear it. If I had any other advice, mm. Look at the cards in the morning but not right before the class starts or you'll get confused. That's what they say anyway."
    BE "Okay. I'll keep that in mind. Thanks, Kei-chan, I really appreciate the help. Oh, before I go, I had one more thing to ask."
    MC "What's up?"
    show BE aroused
    BE "Did you really only buy one box of cookies?"
    "I stared at Honoka for a moment as my foot slowly pushed the bag underneath my bed."
    MC "Yeah…"
    BE "Uh-huh. We're studying again tomorrow."
    "As I chuckled, Honoka left the room. Hopefully she got a good night of sleep. I probably would be hitting the sack soon myself. But… one more cookie wouldn't hurt."
    jump daymenu

label BE016:
    scene Gym with fade
    play music Busy
    "With nothing particularly exciting to do tonight, I decided to go and check on Honoka. She told me that there was a practice for the basketball club tonight. Would be good to give her encouragement."
    "The basketball court was fairly standard, from what I remembered of my old school. Everything seemed pretty standard, although the stands for people to sit seemed to be permanently out. I was used to seeing ones that could be put away during school."
    "They also were more heavily-reinforced, which explained why they were permanent fixtures. Better seating for a constantly-growing school, I figured."
    "Not everyone in the club was out on the court when I arrived. It looked like there were a dozen or so players, so with five players to a team they had enough for a full game and more. I decided to sit down next to one of the other players who was sitting."
    MC "Hi. I'm Keisuke."
    Sakie "Ah. Hello."
    "She stuck out her hand to grab mine, where I took note of her sweatband."
    MC "Oh, neat. Dungeon Doom fan?"
    Sakie "Huh?"
    "I pointed to her wristband, that had the game's trademark logo emblazoned on the side."
    MC "Dungeon Doom, the RPG?"
    Sakie "Oh. Not mine. Borrowed it."
    MC "Oh, sorry. So, you play basketball here?"
    Sakie "Yes."
    MC "Cool. How is it?"
    Sakie "Fun."
    "It didn't take a genius like Matsumoto-san to realize that she wasn't one for conversation. I turned my attention to the basketball game in progress and watched for a while."
    "I could tell Honoka enjoyed herself on the court. She always had a huge smile on her face even if she didn't have control of the ball. After watching for a while though, it became pretty clear that she was better at soccer. "
    "I guess I shouldn't have judged so soon. She hadn't been doing basketball very long, but she'd been playing soccer since we were kids. Honoka made shots, and blocked well enough, but it didn't feel like it had the same spark I was used to seeing in her."
    play sound Whistle
    Coach "Inoue, Charanko, hit the bleachers. Kosuke, Iwata, you're up."
    "The girl I sat next to carefully stood up, and stepped down to the ground. Her sneakers looked like they were twice my size. Honoka was able to come sit next to me, and the large-foot girl didn't say a word to either of us."
    MC "Is she always like that?"
    show BE neutral with dissolve
    BE "Who, Sakie? Yeah she tends to be on the quiet side of things. You didn't say anything to upset her did you?"
    MC "I was pretty sure I didn't. I just asked about her wristband."
    show BE happy
    BE "Oh. That was mine. She forgot hers today."
    MC "Well, certainly was nice of you to lend you hers."
    show BE neutral
    BE "Ah. yeah. That's what happened."
    MC "Are you saying she took it without asking?"
    show BE angry
    BE "I don't even think she realized what she did. She saw she had no wristband, saw one of mine and knew she needed one. Wasn't done out of any sense of maliciousness."
    MC "Weird. But, hey, glad to hear you're still into Dungeon Doom."
    show BE happy
    BE "Haha. Well. Maybe 3, 4, and 9. The rest all feel kind of boring or aren't as fun to play anymore."
    "I stared at Honoka, with a wide gaze, and my jaw slack."
    MC "You're kidding. 5 is easily the best one, how could you not have included that?"
    "Honoka thought for a minute, rubbing her chin before she smirked back at me."
    show BE aroused
    BE "Wait a minute. Wasn't 5 the game that had that scene where all the girls had to strip to their underwear?"
    MC "....maybe."
    BE "Uh-huh. I'm sure you had a save point right before that scene and loaded it up every night."
    MC "I. You. Um. Hey, basketball, right? How's that going?"
    "Honoka was kind enough to ignore my pathetic attempt to change the subject."
    show BE sad
    BE "It's pretty fun. I'm not great at it yet though. But I hope with enough practice I'll get into it."
    MC "I'm sure you will. You pick up a lot of things pretty quickly."
    show BE neutral
    BE "Yeah I mean, it's pretty similar to soccer in a way. Just hands instead of feet, and the net's much smaller and in the air."
    MC "Right, once you figure out how to sink baskets left and right, you won't have any problems."
    show BE happy
    BE "That's the plan. The people here are pretty nice too."
    MC "Even, uh…"
    show BE angry
    BE "Yeah, even Sakie. She's just a bit of a space cadet. But, she's a killer at free throws."
    MC "I like hearing about all the people you get to meet in these clubs. One of these days I really should… do that."
    show BE happy
    BE "What, make friends?"
    MC "Join a club!"
    BE "I know, I'm just kidding. But really, I'm so awesome I count as, like, five friends."
    MC "Three tops."
    show BE neutral
    BE "Okay we'll say four and compromise. But yeah you totally need to join a club. How about this one? They've already been talking about getting Yamazaki-chan here."
    MC "Huh. yeah, she'd be a good fit. But, I'm not sure how aggressive she could be. Seems like you need to have some force behind your actions."
    BE "Not always. You can be passive."
    play sound Whistle
    Coach "Get the lead out! I need to see hussle! Toss that ball like you're trying to take someone's head off!"
    show BE angry
    BE "Okay, yeah, maybe she wouldn't be the best. But she would be great at dunking for sure."
    MC "Something less physical seems more her speed. And maybe mine as well. If the goal is to know people it'd be better to have a lot more downtime."
    BE "Yeah I guess. But downtime is boring. Uptime is the fun stuff. Being active is the best, so why do anything else?"
    MC "Well, I-"
    play sound Whistle
    Coach "Alright, everyone. Line up, let's get some suicides going! Move your butts!"
    show BE happy
    BE "Woops, gotta move. Catch you later, Kei-chan!"
    MC "Wait?! What the hell are suicides?!"
    BE "Oh they're much worse but I'll be fine."
    hide BE with dissolve
    "Honoka's face faltered from her smile as she said that, but she had no choice but to get back on the court and listen to her coach."
    "I don't think the basketball club is for me."
    jump daymenu

label BE017:
    scene Arcade with fade
    play music Schoolday
    show BE happy with dissolve
    BE "You see, I told you that I could get a perfect score."
    MC "Yeah, you've definitely picked up some skills from basketball club, that's for sure."
    "Honoka had told me the previous day that she'd gotten much better at shooting free throws after several meetings at her club. I believed her, but she insisted on proving it. Hence, the two of us arranged to get to the arcade, where they had a basketball challenge. As many free throws as she could make in sixty seconds."
    "She'd managed eighteen. Only two misses, which was an impressive score by any means. That was an A on a test, and enough to get the highest amount of tickets the game would give out."
    show BE neutral
    BE "Well the club definitely practices a lot. Sometimes you just stand there throwing the ball from as many spots as you can. They've got so many balls, it's ridiculous. Makes it easier, so you don't have to keep running to catch one you've thrown."
    MC "Makes sense. So basketball club is still going well?"
    show BE happy
    BE "Yeah. It's pretty good."
    "Honoka smirked and grabbed her tickets from the machine, quickly stuffing them in her cleavage. Several of the stubs stuck out from the initial plunge and she had to shove them back into place."
    MC "They..."
    MC "They probably won't take those."
    show BE unique
    BE "Oh. Well, I'm saving up anyway. I'll just rinse them off or something before I collect them all again. That should help. They're not gonna keep them anyway, just toss them in recycling."
    MC "It's still the principle of the thing."
    show BE happy
    BE "I'll be fiiine. I'm trying to save up for a home-version pachinko machine."
    MC "Why do you want a pachinko machine?"
    show BE neutral
    BE "I dunno. Think it looks cool. All the balls clacking against each other is fun. And if Shiori gets annoying I can bring it to class one day and break it out. All that noise would drive her…"
    show BE surprised
    BE "Craaaazzzzyyyyy."
    MC "Honoka, are you feeling all right? You're acting a bit more unhinged than normal."
    show BE angry
    BE "Yeah. I'm fine, I'm fine."
    menu:
        "Okay, if you say so.": # Affection + 1
            jump BE017_c1_1
        "You're not, what's wrong?":
            jump BE017_c1_2

label BE017_c1_1:
    MC "Okay, if you say so."
    show BE neutral
    BE "..."
    MC "..."
    BE "Why are you looking at me like that?"
    MC "Sorry, didn't mean to look in any specific way. You said nothing's wrong, so, I'm not going to push it. When has that ever made anything better?"
    show BE sad
    BE "Um."
    MC "If you wanna talk to me about it, you'll talk to me about it. Right?"
    show BE neutral
    BE "I guess so."
    MC "Well good. Then let's not worry about it for now. How about we do some light gun game?"
    show BE happy
    BE "Okay, sure, that sounds good."
    "Honoka and I walked towards the cabinets with various shooting-related games, picking out one where the two of us could play cooperatively."
    MC "You wanna be blue, or pink?"
    show BE aroused
    BE "Well I'm the girl. So obviously it's funnier if you take pink."
    "Honoka stuck out her tongue teasingly, as I slid into the second-player position."
    MC "Nothing wrong with pink."
    show BE happy
    BE "Maybe. But it feels so cliche doesn't it? Why can't the guns be like, purple and orange or something. That'd be weird and different!"
    MC "This game is older than both of us. I don't think they were that concerned about that sort of stuff back then."
    BE "Jeez, this arcade needs to get with the times then. They've released like, four sequels to this since then!"
    "Honoka and I got in the game, skipping the cutscenes and getting right into the action, mowing down everything shaped like a bug that came into our vision."
    MC "Yeah, but only Insecticyde 4 was any good, and that one is way bigger than this. They probably don't have room for it."
    show BE neutral
    BE "Heh, you would think with Seichou so close by that they'd look into expanding."
    "Honoka's pun was so terrible that I ended up missing an enemy and took a hit. Green goo splattered on my side of the screen as the bug slammed into my character."
    MC "That was awful, Honoka."
    show BE sad
    BE "I mean it though! Bigger arcades means more room for games. I'd love for this place to get this one I played when I was younger. I don't even remember the name of it, but, you wore these combination boxing glove/brass knuckles."
    show BE happy
    BE "There was motion detectors in a grid around you showing when you punched or dodged, it was really cool. But the rig was very big, and couldn't have much around it or it would mess with the sensors."
    MC "Dang. That sounds fun."
    BE "Yeah."
    "Honoka splattered a few more enemies with her special ammo before reloading her weapon."
    show BE sad
    BE "But at this point playing it would be a pain in the ass, anyway."
    MC "What do you mean?"
    BE "I mean… "
    "Honoka sighed, and her focus returned to the game for a few seconds in silence."
    show BE unique
    BE "I mean that swinging my arms forward repeatedly would hurt when I risk punching my own rack every time."
    MC "Oh. Well, how often is that going to come up in your daily life anyway? You should hope to go through your day without needing to punch someone."
    show BE neutral
    BE "That's true."
    MC "And you're still able to do the things you want to do, right? Play games, go to your club, hang out and eat chocolate?"
    BE "Right."
    MC "Think about it this way. You said you hadn't played that game in years. I assume it was before your breasts started to grow."
    BE "Probably yeah. I think last time I played I was, like, ten?"
    MC "So then, there's no reason to blame your breasts on your inability to play it anymore. It's just a hard game to find. You can't blame your own body for stuff like that."
    "Honoka's screen suddenly splattered with yellow. The color of bugs that were the easiest to kill. She had dropped her trigger hand off of her weapon and slinked it through my arm, before grabbing her gun again."
    MC "Honoka?"
    show BE happy
    BE "You're sweet, Kei-chan…"
    $setAffection("BE", 1)
    "Honoka giggled, then pointed at the screen."
    show BE surprised
    BE "Oh crap, kill it!"
    jump daymenu

label BE017_c1_2:
    MC "You're not, what's wrong?"
    BE "Why do you think something's wrong with me?"
    MC "Not necessarily wrong 'with' you. You're just acting… 'off'. I can't describe it."
    "Honoka sighed and scratched the side of her cheek in worry."
    play music Bittersweet
    BE "...They keep benching me."
    MC "Huh?"
    show BE sad
    BE "The basketball club. I've been on the bench every game so far. They put me in eventually, but I've never been one of the starters. So for most of the game I just sit there. It's… boring."
    menu:
        "At least you're on the team.": # Affection - 1
            jump BE017_c2_1
        "(Say Nothing)":
            jump BE017_c2_2
        "Sorry to hear that.": #Affection + 2
            jump BE017_c2_3

label BE017_c2_1:
    MC "At least you're on the team. You still get credit for wins and stuff."
    show BE angry
    BE "That doesn't count. It sucks! In soccer I was on the starting roster every time. Now I'm just sitting there with a towel and a water bottle. Looking like a sloth."
    MC "But why are they benching you then. I thought your free-throws were good?"
    show BE neutral
    BE "Good, fine. But everyone else is just better. There's something different about running in basketball. It's so much more exhausting somehow."
    MC "But the court is way shorter than a soccer field, isn't it?"
    show BE sad
    BE "It is, but, ugh… you just don't get it if you're not out there moving about the whole time."
    MC "I guess not. I don't get it. You're on the club, but…"
    $setAffection("BE", -1)
    show BE angry
    BE "Kei-chan, just... just leave it alone, okay? This is why I didn't want to talk about it."
    MC "Okay. Sorry."
    jump daymenu

label BE017_c2_2:
    BE "What do they think, I just want a yearbook photo or something? Why even let me on the team if they're just going to have me warming the bench?"
    show BE surprised
    BE "You think maybe the captain knows me?  The coach?  Did I do something wrong?  I pulled some pranks in high school, but nothing I think anyone would hold a grudge over…"
    show BE sad
    BE "Maybe I just suck and they're humoring me."
    BE "It sucks, Kei-chan. It just really, really sucks."
    show BE neutral
    BE "But thanks for listening to me vent."
    "Honoka sighed."
    show BE sad
    BE "Let's just go home. I don't feel like playing anymore."
    "I couldn't exactly say no to that. We headed home right away."
    jump daymenu

label BE017_c2_3:
    MC "Sorry to hear that. Have they given you a reason why they're not letting you play as much?"
    BE "Not really. I can only assume it's because the others are just better. Even if I've gotten good at free-throws, everything else is different. I don't know if I can't undo my soccer skills to learn new basketball ones or what, but I'm floundering."
    MC "Well, that's not fair then, if they won't let you play. How do they expect you to get better if you're not in the thick of it on a regular basis? You won't get any experience that way."
    show BE sad
    BE "That's what I want to say. But, I don't know. Maybe the basketball club isn't for me."
    MC "You can't say that if you haven't had the chance to get a full game going. Maybe you can ask the coach if you can get at least one full game in. Make you last a full half. Then if you don't like it, you can find something else?"
    show BE neutral
    BE "Maybe."
    "Honoka quickly tossed a token into a lottery-style game and pulled out her sheet of tickets that came from the minor victory."
    BE "Just feels weird. I want to be good but, I thought it'd be easier. You know?"
    MC "Learning new games is tough. Maybe you can find something else. Baseball, archery, kendo?"
    show BE happy
    $setAffection("BE", 2)
    BE "The school's definitely not lacking in choices. I'll think about it. Thanks, Kei-chan."
    jump daymenu

label BE018:
    scene Dorm BE with fade
    show BE neutral wth dissolve
    "I was hanging out in Honoka's room, playing video games with her as had become a fairly frequent occurrence. She was kicking my butt pretty handily, something that also had become a frequent occurrence. In the middle of us picking our next fighters, a knock came at her door."
    MC "I thought you said your roomie was going to be out until evening?"
    BE "That's what she said... Maybe it's someone else?"
    "Honoka stood up to open the door, and I peered over to check out who it was. Surprisingly, there stood Aida, fiddling with her fingers, but otherwise waiting patiently."
    show BE happy at Position(xpos=0.25, xanchor=0.5), Transform(xzoom=-1) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5) with dissolve
    play music PRG
    BE "Oh hey! Aida-chan, what's going on?"
    PRG "Hello Inoue-san. I'm not interrupting you, am I? I was hoping to ask you something."
    BE "No, no, not at all. I was just hanging out with Kei-chan. Come on in. No point just standing in the middle of the door."
    "Aida took a step into the room, and then paused."
    MC "Hi, Kodama-san."
    show PRG surprised
    PRG "Oh! You really meant, he, ah, I didn't think Hotsure-san would be here. I didn't realize boys were allowed to be on our dorm rooms, though…"
    show BE angry
    BE "Well I guess anything's allowed as long as nobody finds out about it. But nah, it's cool. If I get in trouble for it, I'll deal with it later."
    show PRG unique
    PRG "I'm not sure if… That doesn't exactly sound like a um, a reasonable attitude to take on it."
    MC "Honestly, I'd probably be the one to get in trouble."
    show BE happy
    BE "Ah! Good point. So see, not a problem for me if he's up here."
    MC "Honoka…"
    MC "Anyway. What's going on, Kodama-san? Is everything all right?"
    if getAffection("PRG") > 6:
        "With Aida's condition, I was fairly concerned over what she could be worried about. "
    else:
        "Hopefully nothing was wrong with Aida. She didn't look sick, but it could have been something else, I supposed."
    show PRG neutral
    PRG "Yes, I'm feeling okay. I just had an issue that made Inoue-san the best person to come to."
    BE "Oh yeah? This oughta be good! Lay it on me, then!"
    show PRG unique
    PRG "Well, I was, it's something that would probably be best left unsaid if Hotsure-san is still here."
    MC "Oh."
    MC "Well, do you want me to leave then?"
    show BE neutral
    BE "Aida-chan, I think he should stay. If it really is embarrassing we'll boot him out, but Kei-chan's a good guy. Plus he may be able to help if I can't."
    show PRG neutral
    PRG "You're sure?"
    BE "Tell you what, here, just whisper the problem to me and if I think he can't handle it, we'll get him outta here."
    MC "Do I get any say in this whatsoever?"
    "Apparently I didn't as Aida leaned up into Honoka's ear and whispered something I couldn't make out. I turned away from them as well to make it easier for Aida."
    show BE unique
    BE "Oh, I getcha. Heh, I guess as far as our class goes I'm the go-to girl, aren't I? Well I'll see if I can help out with this. "
    show BE happy
    BE "Come on, here, sit down."
    "Honoka sat down on her bed and ushered Aida to move next to her, which she did."
    MC "So it's okay then?"
    show PRG aroused
    PRG "I suppose so…"
    show BE neutral
    BE "Yeah. Aida-chan's just been having some bra problems lately."
    MC "Oh. And… you thought that was okay for me to hear?"
    show BE aroused
    BE "Pff, Kei-chan, does a week go by when my boobs don't become a point of conversation?"
    MC "I mean... "
    "I rattled my brain trying to decide if it really was that common before deciding, yes, that seemed likely. Honoka turned to Aida and spoke in a hushed, but audible tone."
    show BE angry
    BE "I think he actually might be getting blase about it."
    show PRG neutral
    PRG "Oh, I see…"
    MC "I wouldn't say that. But, don't let me stop your conversation."
    show PRG sad
    PRG "Well, I've just been going through a bit of a… growth spurt lately, and my bras are getting too tight."
    show PRG unique
    PRG "I hope I'm not being presumptuous by, um, assuming you've had issues with that in the past?"
    show BE happy
    BE "Ha! Had, and continue to have."
    show BE neutral
    BE "So what's the deal then, you're not sure how to get good, new ones when you're packing more in your blouse than you're used to?"
    show PRG aroused
    PRG "Uh, um…"
    MC "Yes, Kodama-san, I'm pretty sure that's the issue and Honoka's just putting it in a dumb way."
    BE "Yeah, sounds like me."
    show PRG happy
    PRG "Well, um, yes. But to be frank, even my last set of bras weren't all that comfortable to begin with. I just wanted some advice."
    BE "Alright. I think I can help. Let me think."
    show BE happy
    BE "Hey, Kei-chan. Do you happen to have any sort of measuring tape on you?"
    MC "Yeah one sec."
    "I looked in my drawers and found a strand of measuring tape that looked like it would work for Honoka's needs, something I had grabbed to start checking how long my hair grew."
    MC "This good?"
    show BE neutral
    BE "Yes, yes, that's perfect."
    "Honoka started unspooling the measuring tape and cleared her throat, looking at Aida with a smile."
    BE "Okay. So, like, when it comes to bra measurements, it's not just one size, really. They're going to need two measurements. At least, a good place to get bras will. So you can't just assume you're a certain cup size because of how big ya look."
    "I watched as Honoka whipped the measuring tape around Aida's chest so it went underneath Aida's arms. Honoka pulled the two halves of the tape together and made them meet in the middle."
    stop music
    show PRG surprised
    PRG "I-I-Inoue-san!"
    show BE happy
    BE "Now normally, you would wanna do this completely naked. I mean, not naked naked, but topless at least. Maybe it's more fun just going all-the-way, though…"
    show PRG sad
    PRG "I-Inoue-san…"
    MC "Honoka..."
    menu:
        "Tell Honoka to ease up": #PRG.Affection + 1
            jump BE018_c1_1
        "Let Honoka continue":
            jump BE018_c1_2

label BE018_c1_1:
    MC "Honoka. Slow down some. Kodama-san's getting freaked out."
    show BE surprised
    BE "Oh. Crud. Sorry, Aida-chan. I wasn't thinking right. Um, I didn't even ask if I could do this, did I?"
    show PRG neutral
    PRG "N-No. But, y-you may, I just…"
    "Aida looked over in my direction and I turned my head to the side, trying to avert my gaze."
    MC "Not looking!"
    $setAffection("PRG", 1)
    show PRG happy
    PRG "S-Sorry, but thank you, Hotsure-san."
    show BE happy
    BE "Okay, let me try and do this a bit more delicately then."
    jump BE018_c1_after

label BE018_c1_2:
    show BE aroused
    $setFlag("BE018_c1_2")
    BE "I mean I'm certainly not one to judge. Just make sure your roommate's cool with it. I walked around topless for a while with mine here just to see how long it'd take her to say something…"
    show PRG surprised
    PRG "Hotsure-san? H-Help…"
    "I vaguely heard Aida's voice but was a bit distracted. Honoka's hands were still holding onto the measuring tape, but she kept pulling and pulling on the ends, making Aida's bust bounce. Not to mention her own bosom was so close to Aida's…"
    show PRG sad
    PRG "*whimper*"
    BE "Oh, wow. Heh, hands getting a little zany there. Where was I?"
    jump BE018_c1_after
    
label BE018_c1_after:
    play music Schoolday
    show BE happy
    BE "Anyway! So, here, you need to make sure it's nice and snug. Don't pinch anything in, just make sure you can feel the tape around your boobs as much as possible. Try and think of it like you're wrapping yourself up with it."
    show BE neutral
    BE "You need to get it over the fullest part of your breasts, though, so move it up higher."
    show PRG angry
    PRG "L-Like this then?"
    show BE happy
    BE "Yes, that's perfect. Okay, so call that your bust size, bam. Halfway done."
    show PRG happy
    PRG "What's next?"
    show BE neutral
    BE "Second part is the…. "
    show BE unique
    BE "I think it's called the band size. And for that, we want to measure right underneath your bust. So it's going to be a smaller number about 99%% of the time, unless you're really flat and really fat at the same time."
    show BE neutral
    BE "Same deal, though, pull the two halves together, right in the middle, and jot down that number. That's your band size."
    show PRG neutral
    PRG "Okay, so, what do I do with these, then?"
    show BE angry
    BE "Well the band size is the number you'll give when you go to a tailor, or clerk, or looking on the shelves. That's what you hear a lot when you see them mentioned in movies."
    show BE happy
    BE "So, say for example, and I'm using example numbers here, Kei-chan, so don't go fantasizing too much. Aida will get so flustered she'll set this measuring tape on fire."
    MC "Honoka I haven't even said anything at all yet."
    show BE aroused
    BE "Oh I can hear your brain going haywire over there."
    if getFlag("BE018_c1_2"):
        "It's not my fault. What else is a healthy boy supposed to do when two busts are bouncing right next to each other?"
    show BE unique
    BE "Say for example, your band size is 80 centimeters, and your bust size is 110 centimeters. So you would let the person know you need a size 80 bra. But then what about cup size? That's a very good question."
    show PRG surprised
    PRG "I, I didn't ask about-"
    show BE happy
    BE "Cup size is found by subtracting the band size from the bust size!"
    "Honoka raised her hand in such a studious, professor-ly manner that I'm surprised glasses didn't manifest on her face."
    show BE neutral
    BE "So, for this example rack, the difference is thirty centimeters.  A new cup size is given every two and a half centimeters, give or take. So that's, let's see…"
    if getSkill("Academics") > 5:
        MC "That'd be 12."
        $setAffection("BE", 1)
        $setAffection("PRG", 1)
        show BE happy
        BE "Oh! Nice. Thanks, Kei-chan."
        show PRG happy
        PRG "Very clever, Hotsure-san."
    else:
        show BE happy
        BE "30 / 2.5, or 300 / 25, which would be 3 instances of 4, so… 12 total!"
        "I blinked a few times. Honoka wasn't stupid, or particularly bad at math even. But the way she puzzled out division in her head using cup sizes was not something I expected to see."
    show BE neutral
    BE "So this example bosom would be 12 cup sizes in. That would make them an… L-cup. With their band size, that would make them an L80."
    show PRG surprised
    PRG "That sounds rather large, erm."
    show BE sad
    BE "Yeah I don't think you'd be able to grab something that big right off of a shelf. Oh, and Honoka tip, if for some reason you ever find yourself in America, they do inches there. So you'd be way smaller-sounding at least. Like, a 32L, instead."
    show BE happy
    BE "Though you'd also be in America. So your band size would probably be going up a few sizes too while you're over there, hehe."
    MC "I think everyone's would. I mean, look at Nikumaru-san..."
    show BE unique
    BE "Exactly! That's a good example of someone who might have a bigger band size than she does a bust size. Though… she's pretty stacked too, isn't she?"
    show PRG unique
    PRG "Well, I don't think I have any plans to visit America soon. But, thank you, Inoue-san. I think that will be helpful."
    show BE happy
    BE "Glad to help! And hey, having Kei-chan here wasn't too bad, was it?"
    show PRG happy
    PRG "N-No. Thank you both then."
    MC "Do you want to stick around, Kodoma-san? We only have two controllers but we could swap out if you want to play."
    if getAffection("PRG") > 8:
        show PRG surprised
        PRG "Oh, um… sure! I suppose I could, if it's alright with Inoue-san. It is her room."
        show BE happy
        BE "Yeah come on, and take a load off! Plus it'll be funny to see how long it take Kei-chan to squirm when he's in a room with two beautiful ladies."
        show PRG happy
        PRG "*giggles*"
        MC "Honoka I'm right here. And I'm gonna squirm right away if you make it so obvious."
        "That got Honoka giggling as well. She then handed the controller over to Aida and began showing her the controls. I don't know if she really played games much, but it was very nice getting to play with both of them."
        "Aida didn't play for very long, about a half hour, but she seemed to have a good time before she decided it was time to leave."
        PRG "That was… that was very nice."
    else:
        show PRG neutral
        PRG "Oh, no thank you."
    show PRG happy
    PRG "I'll um, I'll go back to my room now. I'll see you both in class tomorrow. Have a good night."
    MC "You too, Kodama-san. Be safe."
    show BE happy
    BE "Yep! Good talkin' to ya, Aida-chan!"
    hide BE with dissolve
    hide PRG with dissolve
    "Honoka got up to walk Aida over to the door, and then came back to sit down next to me after she'd left."
    show BE neutral with dissolve
    BE "Hahhh. That was nice. Glad to help her out."
    MC "I never knew you were so well-informed about bras."
    show BE angry
    BE "Hey, are you saying you haven't picked up an article or something about long hair since you got your diagnosis?"
    MC "Uh…."
    show BE happy
    BE "Haha. Kei-chan, you can be a real dork sometimes. Ooh!"
    "Honoka grabbed my measuring tape and smirked, before tossing it over my head."
    MC "Ah right, I should put this away."
    show BE neutral
    BE "Wha? Not gonna sniff it first?"
    MC "Why on earth would I do that?"
    show BE unique
    BE "Cuz maybe it's still got some of Aida-chan's scent on it. Being rubbed up against a lovely lady's bosom for that long? Might have picked up some of her trace."
    MC "Honoka, don't be weird. Besides…"
    menu:
        "It's probably been too long since it touched her anyway":
            jump BE018_c2_1
        "I'd prefer if it was your scent on it":
            jump BE018_c2_2

label BE018_c2_1:
    MC "It's probably been too long since it touched her anyway."
    "I rolled up the measuring tape and put it back in my desk."
    show BE sad
    BE "Aw, but you're probably right. Eh well, let's get back to me kicking your butt."
    "Honoka picked up her controller and proceeded to do just that, once again destroying my character 2-0. After that I decided to pack up and head back to my room as well. It was getting late. I said my goodbyes, and was soon under my sheets, proceeding to doze off."
    jump daymenu

label BE018_c2_2:
    MC "I'd prefer if it was your scent on it."
    $setAffection("BE", 1)
    show BE surprised
    BE "You, wha, uh, you….."
    "Honoka had already unpaused the game, and her befuddlement at my confession was enough for me to take the lead in our last match of the night."
    scene black with fade
    "After that I decided to pack up and head back to my room as well. It was getting late. I said my goodbyes, and went to get under my sheets and doze off."
    "Though now I was wondering what my sheets would have smelled like if Honoka had been rubbing against them…. Stupid brain."
    jump daymenu

label BE019:
    scene Cafeteria with fade
    play music Schoolday
    "Lunch was simple today. I just grabbed a sandwich and chips, along with some water. I didn't expect anything unusual to happen, even when Honoka sat across from me without introducing herself."
    show BE neutral with dissolve
    BE "You remember when we had our skip day?"
    menu:
        "No":
            jump BE019_c1_1
        "Yes":
            jump BE019_c1_2
            
label BE019_c1_1:
    MC "Skip day? No, I don't know what you're talking about."
    show BE sad
    BE "You don't? Aw, come on Kei-chan. It was right before my family moved away."
    MC "Agh. I'm kind of remembering…"
    show BE neutral
    BE "Our parents let us get out of school one day? And we hung out together."
    MC "Oh! Right! Duh. Gosh, I can't believe I forgot about that."
    jump BE019_c1_after

label BE019_c1_2:
    MC "Skip day? When you were getting ready to move out?"
    show BE happy
    BE "Right! I think your mom came up with the idea."
    MC "She did, I remember that. Thankfully your parents were fine with it too."
    show BE surprised
    BE "Yeah. Wow, you know, I hope they didn't say anything embarrassing to the school about why I missed school that day."
    MC "Even if they did, it's not like it matters at this point. But, gosh. I haven't thought about that day in years. That was fun."
    jump BE019_c1_after

label BE019_c1_after:
    show BE happy
    BE "It was super, mega-awesome fun."
    MC "I think my favorite part was honestly that our moms let us sleep in a little too."
    BE "Well, yeah. But then we got to have a good breakfast instead of something quick. I had chocolate-chip pancakes and syrup."
    MC "Ha. Lucky. I… can't remember what I had but if we had pancakes, it was only regular."
    "Honoka's hand suddenly reached out and grasped mine, as a solemn look came to her face. "
    show BE sad
    BE "Kei-chan. That's terrible. I'm so, so sorry for your loss."
    MC "Er, I didn't get chocolate for breakfast, Honoka. It's not a big deal."
    show BE angry
    BE "I'm trying to have a nice, reminiscent moment of nostalgia, so I'll ignore that you said that."
    MC "..."
    show BE happy
    BE "Anyway! It was just so nice getting a chance to hang out with you. I think I had been feeling really down that week about the fact we were moving. I didn't want to go."
    MC "Hey, I mean…  I didn't want you to go either. I was losing my best friend."
    show BE sad
    BE "It sucked. Hardcore."
    show BE happy
    BE "But then we got to see Alien Festival the day it came out! There was nobody in the theater except for us."
    MC "Yeah. I think my mom didn't realize how much, uh, blood was going to be in the movie."
    show BE angry
    BE "The movie was called 'Alien Festival'. What did she think they were going to come down and put up food carts and rides?"
    MC "I can't answer that honestly."
    "Honoka laughed and I smiled back at her."
    MC "So, what brought this up, anyway? I mean it was fun, but it was such a long time ago."
    show BE neutral
    BE "I think it was seeing a bit of Alien Festival 3 on tv last night. Brought up some old memories. Made me think about the good old days."
    MC "Honoka, you're not even 20 yet. You didn't have 'good old days'. You had days."
    show BE unique
    BE "Hey there's a big difference in a woman's life between when she was a kid, and when she gets hooters."
    "Honoka snickered, and her hand went up to her mouth as I watched her cheeks puff up."
    MC "You just thought 'A really big difference in my case', didn't you?"
    show BE happy
    BE "Pfff, yeah."
    "I shook my head, and took a hearty bite of my sandwich."
    MC "Heh. After the movie, we went and got lunch, then we went to the arcade after that."
    show BE neutral
    BE "Oh. Yeah. But we don't need to talk about that."
    MC "Hm. I think we do. Because, now it's reminding me of something very important Honoka."
    "I couldn't stop the smirk on my face from forming. Honoka looked worried."
    show BE sad
    BE "Uh, it is? No. Can't be that important."
    MC "Yep, it is. I remember that's the only time I was able to beat you at Redlight Racer."
    show BE angry
    BE "Gahhhh. I can't believe you remember that part. That's the only time you ever beat me! It's the only time anyone's ever beaten me!"
    MC "Oh now that I remember this, I'm going to bring it up every chance I get."
    BE "No you won't! Not when I challenge you to a rematch!"
    MC "Like hell I'm going to play you again in that game. I'm taking that victory to the grave with me."
    show BE neutral
    BE "It's only 1 win against my 24 wins."
    MC "Yeah, but it was the last match we played. If I leave it like it is it's a triumphant underdog story. If I raced you again, I'd just be the loser who's 1-25."
    "Honoka slumped over on the table. Her head sank right into her chest with her mouth and nose covered up completely by her bosom, as she muttered under her breath."
    MC "Honoka? I couldn't quite hear you."
    "She lifted her head out of her bust, staring at me as deadpan as could be."
    show BE happy
    BE "25-1 would still be better than 24-1."
    MC "Which is why I'm not playing that ever again. Not even when we're eighty years old."
    show BE unique
    BE "Ugh, I don't even want to think about what my boobs would look like at that point."
    MC "Haha. Well, think about something else. Do you remember what we did for dinner? I think we went to one of those grill places."
    show BE happy
    BE "That sounds right. I just remember being really full."
    MC "Yeah. Then we went back to my place and hung out watching cartoons until we went to bed."
    show BE neutral
    BE "Oh. I slept over?"
    MC "I'm pretty sure you did. I think my mom just let us sit on the couch until we fell asleep."
    show BE sad
    BE "Wait."
    "I looked at Honoka in confusion."
    MC "What?"
    show BE neutral
    BE "So both of us were on the couch, sleeping together all night?"
    MC "Um. Yeah, that's what I remember."
    "Honoka suddenly blushed, her cheeks getting as red as licorice."
    show BE happy
    BE "That means you were the first boy I spent the night with."
    MC "Wh-What? I mean. Yeah, that's true. But, not like, in that way!"
    show BE aroused
    BE "It doesn't matter, Kei-chan. It was you. That means…. That means..."
    "Honoka shuddered and put her clenched fist up to her mouth as she turned her head away."
    "It was at this point I began to suspect that this was a bit of an act she was putting on."
    "She turned her head back to face me, and took both my hands in hers."
    BE "That means you took my purity, Kei-chan!"
    MC "Honoka. I woke up with your foot on my face, and your pillow utterly soaked in drool. It was not a glamorous evening by any definition."
    show BE happy
    BE "Hm. Yeah. That's not exactly the best way to say we spent our first night together, is it?"
    MC "I mean, it was a fun day! Nothing wrong in my book."
    show BE neutral
    BE "Still. Maybe we should think about doing another skip day some time while we're here."
    if getAffection("BE") > 8:
        show BE aroused
        BE "Maybe if we do, then we can have a better night together."
        "Honoka stared at me and winked, then stuck out her tongue as she grabbed her trash to throw it away, leaving me slightly dumbfounded about her last words."
    else:
        MC "I'm not sure if that's the best idea. We have more responsibilities. We're older now."
        "Honoka looked down at the table, and worked her finger in a figure-eight around the surface of the table."
        show BE happy
        BE "Yeah but. Since we're older, we can do some stuff we didn't do last time."
        MC "Huh?"
        show BE neutral
        BE "Oh, better clean up. Gotta get back to class soon!"
        "Honoka hurriedly grabbed her trash to throw it away, and I soon followed after her, getting my own garbage to toss away as well. Skip day might be pretty fun, but, I had to imagine if Matsumoto-san found out that she definitely would not approve. I guess she just wouldn't find out, in that case!"
    jump daymenu
    
label BE020:
    scene Hallway with fade
    "Classes were over for the day, thankfully. Today's lessons hadn't been hard, necessarily. But they'd been mentally draining. The dining hall for dinner wouldn't open up for another hour or two, so I pondered over what I could do in the interim."
    show BE happy with dissolve
    play music BE
    BE "Hi, Kei-chan!"
    "Honoka appeared as she often did, out of nowhere. The major clue that it was her being the two soft lumps pressed into my back when she leapt into me. She quickly jumped back and smiled."
    show BE neutral
    BE "What are you up to?"
    MC "Nothing really. I think I was going to go to my room and just chill until it was time to eat."
    BE "Oh? Well, hey. I'm glad I found you. See, I got this gift card from my mom."
    "Honoka reached into her cleavage and extracted a small certificate."
    show BE happy
    BE "Apparently she got it at a work raffle, and she saw there was a location near here. I haven't ever been to this restaurant before. I was looking for someone to go with."
    menu:
        "Are you asking me out?":
            jump BE020_c1_1
        "I'd love to go, if you're offering.":
            jump BE020_c1_2
        "I'm sure Nikumaru-san would be interested.":
            jump BE020_c1_3

label BE020_c1_1:
    MC "Are you asking me out?"
    BE "Pff. Kei-chan you're like my best friend. I can have dinner with you without it being a 'date', right?"
    MC "Yeah. I guess so. Just, I dunno. Wasn't sure."
    show BE neutral
    BE "I mean, if it 'was' a date, you wouldn't be opposed to it, would you?"
    MC "No. Not at all."
    show BE happy
    BE "Good. Glad we're on the same page then."
    MC "Are we?"
    BE "Yep! Now I already looked into it and there's a bus that leaves in 45 minutes that will drop us off close to the restaurant, so by the time we sit and order, it should be good for dinner time. Does that sound fine?"
    MC "Sure. Should I, like, dress up or something?"
    "Honoka looked at the gift card."
    show BE angry
    BE "Uh, I really don't know. This doesn't say there's a dress code or anything like that. So I guess the answer to that is 'It's optional'?"
    MC "Okay. Well, yeah that sounds good then. So, I guess I'll meet you at the bus stop when it's time to leave?"
    show BE happy
    BE "Yep! All right, I'm going to go change. See you in a bit, Kei-chan!"
    "With that, Honoka left towards her dorm room and I did the same."
    MCT "I should probably get out of my uniform, at least."
    jump BE020_c1_after

label BE020_c1_2:
    MC "I'd love to go, if you're offering."
    BE "Oh! Well, good! Yeah, I mean, you were clearly my first choice. I thought it would be nice for us to go out some place that wasn't an arcade. I mean, not that I'm sick of arcades."
    MC "If you said that, I'd decline the invite if only because you'd need to go to the doctor."
    show BE neutral
    BE "Ha. So. If you want to go, then, there's a bus that leaves campus in like, 45 minutes, and it stops within walking distance."
    MC "That sounds perfect. What kind of restaurant is it, actually?"
    show BE angry
    BE "You know, I honestly didn't check. But it's free, so…"
    MC "Fair enough. I was just wondering if this was something that needed, like, a collared shirt or they'd kick you out."
    show BE neutral
    BE "I don't think they would. But, hey, try it out. Could be fun. I'll find something nice too."
    MC "Sounds like a plan. Okay. Meet you at the bus stop then?"
    show BE happy
    BE "Yeah! Okay, I'm excited. Hehe, awesome. See you then, Kei-chan!"
    "I smiled as Honoka left. I'm sure I had something decent I could put on in order to look presentable. This sounded like it would be fun."
    jump BE020_c1_after

label BE020_c1_3:
    if getAffection("BE") > 10:
        MC "I'm sure Nikumaru-san would be interested."
        show BE sad
        BE "Aw. Heh. Are you worried we're hanging out too much? I like our classmates a lot too, but, well… I really wanna go with you."
        MC "Oh. Gosh. No no it's not that I'm tired of spending time with you. I just, I didn't even put it together. Sorry. I'm dumb."
        show BE neutral
        BE "Mm. Dumb? No. Oblivious at times, definitely."
        MC "Yeah, heh. Sorry. My bad. But, um, yeah, I'd love to go with you!"
        show BE aroused
        BE "Good. Cuz if you didn't, I was gonna have to knock you out and drag you there, caveman-style."
        "Honoka stuck out her tongue, then looked at the gift certificate."
        show BE neutral
        BE "Alice would probably find some way to critique the place anyway. I'm not sure what kind of cuisine it serves, actually."
        MC "Well like I said, I had no plans. So unless it serves, like, insects, then I'm still down to go."
        BE "Cool. We can catch a bus there. Leaves at a quarter 'til. Meet up there?"
        MC "Yeah, I can do that. Should I put something else on?"
        BE "Probably just anything other than your school uniform would work. Might be kind of weird otherwise."
        MC "Good call. All right, I'll see you then."
        "Honoka nodded and headed off to her dorm to change. I figured I'd do the same, maybe see if I could get a shower in as well."
    else:
        MC "I'm sure Nikumaru-san would be interested."
        show BE sad
        BE "I'm sure she would, Kei-chan. But I came to you for a reason."
        "The realization hit me and I couldn't help feel like a bit of an idiot."
        BE "You ah. You were asking me if I wanted to go, weren't you?"
        show BE angry
        BE "Yeah. Duh."
        MC "Well, If I didn't embarrass myself enough to get booted off of your list, I could still go."
        show BE aroused
        BE "May as well go with you."
        "Honoka stuck out her tongue, then looked at the gift certificate."
        show BE neutral
        BE "Alice would probably find some way to critique the place anyway. I'm not sure what kind of cuisine it serves, actually."
        MC "Well like I said, I had no plans. So unless it serves, like, insects, then I'm still down to go."
        BE "Cool. We can catch a bus there. Leaves at a quarter 'til. Meet up there?"
        MC "Yeah, I can do that. Should I put something else on?"
        BE "Probably just anything other than your school uniform would work. Might be kind of weird otherwise."
        MC "Good call. All right, I'll see you then."
        "Honoka nodded and headed off to her dorm to change. I figured I'd do the same, maybe see if I could get a shower in as well."
    jump BE020_c1_after

label BE020_c1_after:
    scene black with fade
    stop music
    "After I got back to my dorm room, I decided on what to wear. My school uniform was already a collared shirt, so changing into another one seemed redundant, but the red one I pulled out of my closet seemed nice, and more comfortable."
    scene Town with fade
    play music Rain
    "I went to the bus stop to meet Honoka after checking my homework load, and making sure it wouldn't be too much for that night after we got back. She was already waiting when I arrived."
    MC "Hey, Honoka. Have you been waiting long?"
    show BE neutral with dissolve
    BE "Nope. Just got here a minute ago. Just waiting on you and the bus."
    MC "Good. Did you happen to find out what kind of restaurant it is?"
    show BE happy
    BE "Yeah, actually. It's a sushi place. The gift card was for 5,000 yen. So I figure we can get some drinks, and then a few rolls. Maybe an order of edamame to go with it?"
    MC "Oh. Great. I love sushi. Yes, that sounds great. Shouldn't take too long to make it either."
    BE "That's the hope."
    "Honoka smiled and checked the time on her phone as we waited for the bus. She looked nice. She wasn't wearing anything flashy. Just a blue blouse with a matching pencil skirt, and a shawl over her shoulders. It still looked good on her. "
    "Eventually our bus arrived. We appeared to be the only two headed on it at this time. I approached the door and waited to the side for her."
    MC "Ladies first."
    BE "Thank you, Kei-chan. Such a gentleman."
    "Honoka seemed to direct the second comment more to the bus driver, who barely paid it mind as he closed the doors behind us and went underway."
    "We sat together during the short trip, watching the nice atmosphere. Seichou Academy was nestled in quite a nice area. Which was probably intentional. A school would have a tough time helping the self-esteem of young people with odd quirks if it was dingy."
    "Eventually our bus stopped, and we found ourselves in the middle of a small street, with several people walking around, coming in and out of various buildings."
    MC "Alright. We're here. You said the restaurant was close?"
    show BE neutral
    BE "Yep. Should be up that block, and then around the corner."
    "Honoka pointed towards our destination and led the way."
    scene Sushi Restaurant with fade
    "The restaurant looked small, but looked very nice when we stepped inside. Once we got in, we saw only six tables, along with a small area where people could sit at stools."
    show BE neutral with dissolve
    BE "Hi. Table for two please."
    "Honoka had already gone up to the head waitress while I was looking around. The waitress led us to a small table in the corner of the restaurant, where we sat opposite each other. "
    Waitress "Here are your menus. Could I get you started with anything to drink?"
    MC "Ah. Not sure. Honoka?"
    show BE happy
    BE "I'll have a lemonade, please."
    MC "I'll just take a water for now, thank you."
    "The waitress left so we could mull over our options."
    MC "This is a nice place. Small but nice. Surprised it had gift cards."
    show BE neutral
    BE "There must be a few locations."
    "We only had to wait a moment before our drinks arrived, and Honoka asked for a plate of edamame. We still were deciding on what sushi we wanted to get."
    MC "There's not too many choices but, I'm sure it's all going to be good."
    show BE happy
    BE "Yeah. Hm, I think I'm gonna get a spicy eel roll."
    MC "Hm. Oh, it's unagi. That's good, I like that one more."
    show BE neutral
    BE "That means it's like, more rich?"
    MC "Yeah basically. Anago is more… I would say sweet, maybe?"
    BE "Ah, okay. Much as I like sweet, I don't know if that'd go good with sushi. Yeah, I'll get this one then."
    MC "Sounds good. Hm. I'm leaning towards either the shrimp tempura or a crab roll."
    BE "I was thinking about a crab roll too. How about we get that one to share, and we also get, maybe a tuna roll, and then you can get the tempura for yourself?"
    MC "Will that all fit on your gift card?"
    show BE happy
    BE "Yeah, I think so!"
    MC "Okay then, that sounds good."
    "After putting our menus down, our waitress came over to take our orders almost instantly. The service here was impeccable. Now with nothing but our drinks, and two small bowls for soy sauce, we sat."
    show BE neutral
    BE "So, uh. How's school going?"
    MC "Pretty good, I suppose. Same as you. Though, I don't know. Some days it's hard, some days it's soft, you know?"
    "Honoka raised an eyebrow at me as she sipped her lemonade through a straw."
    MC "I mean the classes, Honoka."
    show BE unique
    BE "I knew that. What did you think I was thinking?"
    MC "I haven't the foggiest idea what you're talking about."
    "Honoka snickered."
    MC "But, what about you? Club situation the same?"
    show BE neutral
    BE "Yeah, I think I'm moving on to archery club."
    MC "Archery huh? That's pretty cool. That was one of the gym activities I always liked. Maybe because there's not much moving around."
    show BE happy
    BE "Ha. Yeah. It seems pretty simple. There's only like, seven steps to shooting a bow and arrow anyway. And two rules. Don't point your bow at people, and don't be a person in the way of a bow. Sounds easy."
    "I brushed a lock of hair out of my eyes, behind my ear, and sighed. I should have trimmed it a bit before heading out. Though that did remind me of something that could give Honoka difficulty."
    MC "You think you'll be able to do archery?"
    show BE neutral
    BE "I don't see why not. It's just learning how to adjust for wind. I'm not saying I'll win competitions or anything like that."
    MC "No, no, I mean… I'm pretty sure it was a myth, but I remember reading about female archers having a breast cut off to make it easier to aim a bow."
    show BE sad
    BE "Oh gross. No, I'm not doing that."
    MC "I, I know that. I mean, more in the effect that the string comes back really hard and whips you. You're big enough that it's almost guaranteed to hit you."
    BE "No… come on, Kei-chan. This is a club at a school meant for bigger guys and girls. They'd have to have safety equipment, right?"
    MC "Well yeah. They do make arm guards and chest guards."
    show BE happy
    BE "That's fine then! I'll just wear a chest guard! I'll wear two if I have to."
    MC "I don't think that will be super comfortable."
    show BE sad
    BE "I don't care, Kei-chan…"
    MC "..."
    show BE angry
    BE "Can't I just do it now before I get so big that it's impossible, and not just difficult?"
    MC "You're right. Sorry, I didn't mean to upset you or anything."
    "Honoka sighed, and slumped back in her seat, a tiny thud on the table as her chest smacked into it."
    show BE sad
    BE "It's okay. Sorry, I just want to make sure I have a full experience. You know?"
    MC "Right. I'm sorry too."
    "I sighed next, sipping my water."
    "Soon the awkward silence was broken by the edamame arriving, giving us a few minutes to chew on those as our sushi were finished."
    show BE neutral
    BE "So, what about you? You're still not in a permanent club either?"
    MC "No. I just always feel kind of drained after classes. Too much to go to another function."
    BE "You've gotta stick with something for at least a week though."
    MC "I know I should…"
    "Honoka and I discussed possible clubs I could join for a bit as we munched our edamame, tossing the pods in the extra plate provided. Soon our sushi arrived. Four plates between us, two in the middle and one directly in front of each of us."
    MC "Well. Thanks for the meal!"
    show BE happy
    BE "Eat up, Kei-chan."
    "Honoka giggled, and grabbed a piece of her eel roll."
    show BE surprised
    BE "Mm! Ooh. That's good!"
    "She already had the second piece in her mouth before I had finished my first piece. Which, as I finally started chewing, realized was delicious. "
    MC "Ooh. Mm, the crunch of the shrimp really like… goes well with the soft rice."
    show BE happy
    BE "Heh. Easy there culinary boy. You sound like you want to join a cooking club."
    MC "I mean, if I get to eat food all the time."
    show BE neutral
    BE "Yeah actually that's not a bad idea."
    MC "Probably won't be as good as this if we're making it though."
    show BE happy
    BE "Not worth the risk then."
    "Honoka popped another piece in her mouth, then took a piece of ginger in her mouth before switching to one of the center plates. I followed her lead."
    show BE surprised
    BE "Ooh. Mm. I know that's not real crab meat. But it's so good."
    MC "The tuna's good quality too. Nice and fatty."
    "The two of us continued to switch back and forth between pieces of sushi every once in a while. Conversation was light. Sushi was meant to be eaten quickly and we'd ordered quite a bit."
    "But we whittled it down bit by bit. The shared portions were finished up, leaving us with just our own selections."
    show BE happy
    BE "Okay, Kei-chan, here, you've gotta try one of these eel rolls before I eat the last one."
    "Honoka had two of her rolls left, same as me."
    MC "Sure."
    "I reached over to the plate, but Honoka took it and yanked it back."
    BE "Uh-uh. Open your mouth."
    MC "Huh?"
    BE "Open your mouth, Kei-chan."
    MC "Um. Okay."
    "I'd have had to be an idiot to not recognize what she was doing, but it still seemed odd. I opened my mouth and leaned forward."
    show BE aroused
    BE "Ahhh."
    "Honoka took a piece of sushi and plopped it in my mouth."
    MC "Mm…"
    "It was good. This place would have to stay on our radar."
    MC "That's nice. Thanks for sharing. Here, you want one of mine?"
    show BE happy
    BE "Yes please!"
    "I smiled and grabbed my shrimp roll, and put it towards her waiting mouth. Honoka closed my eyes, which seemed a bit weird. But she still accepted the sushi piece."
    "Along with the tip of my finger as her lips wrapped around it."
    show BE surprised
    BE "Omf. Hmm…"
    MC "What'd you think?"
    show BE angry
    BE "Mmm. Not sure. Give me the other to make sure."
    MC "Heck no, this last one's mine."
    "I tossed the last one in my mouth without even bothering to cleanse my palette. Honoka did the same as I jokingly reached for her last piece, leaving us both with mouthfuls of sushi."
    show BE happy
    BE "Pff."
    MC "Hehe."
    BE "Hehehehehehe."
    "The two of us probably looked stupid, laughing at each other just from eating sushi. But there was nothing to be done about it. We kind of were stupid."
    "Honoka let out a sigh and leaned back in her chair, placing a hand on her stomach."
    BE "Woo, that was good. Mm. We should probably get going though. The next bus back to school leaves soon and we don't want to miss it."
    MC "Right."
    "We stood up and walked over to the register to pay."
    Waitress "Did you enjoy dining with us today?"
    BE "Yes we did."
    MC "Agreed. It was delicious."
    Waitress "Thank you very much. Your bill today comes to 6,000 yen."
    show BE neutral
    BE "Okay. I have a gift card to cover most of that."
    "Honoka reached into her pocket to grab the card, along with her wallet."
    MC "Oh, I'll cover the difference."
    BE "What? No, it's okay, Kei-chan. I'm the one who invited you, I should pay."
    MC "No, seriously, it's only 1,000 yen more, I can cover that."
    BE "So can I, it's fine, Kei-chan."
    menu:
        "Insist on paying the difference": #BE.Feminine + 1
            jump BE020_c2_1
        "Allow Honoka to pay the rest": #BE.Tomboy + 0
            jump BE020_c2_2

label BE020_c2_1:
    $setVar("BEFeminine", getVar("BEFeminine") + 1)
    MC "Honoka, I'm paying the rest, it's only proper. Here you go, miss."
    "I took out my wallet and handed the waitress a 1,000 yen note before Honoka could fish her note out of her wallet."
    show BE happy
    BE "Oh, okay, Kei-chan. Thank you."
    "Honoka blushed, and I swore I saw a faint smile before she put her wallet away."
    "The waitress took Honoka's gift card and my note, and closed the register after the bill was paid."
    Waitress "Thank you again for dining with us. We hope to see you again."
    MC "I'm sure we'll be back. It was delicious."
    "Honoka nodded, and we turned to leave, so we could head back to our bus stop. As we left the building, Honoka wrapped her arm in mine."
    BE "Thanks for covering the rest, Kei-chan. That was really nice of you."
    MC "Oh. It's no trouble. You paid most of it."
    BE "But still. Having you pay for the meal at the end… I think that makes this official."
    MC "Makes what official?"
    "Honoka stood on her toes and leaned up, planting a kiss on my cheek. The warmth of her lips on the side of my face in that one moment felt hotter than the heat that had been rubbing against my side since she stood next to me."
    show BE surprised
    BE "That this is our first real date, silly."
    "Honoka giggled and got back down on her feet, holding my arm closer."
    MC "Y-yeah? I mean. We've been out on dates before."
    show BE happy
    BE "As friends. But friends don't typically feed each other like we did today. I'm not saying we have to make anything official. But… this was a really nice time. I think the only way it could be nicer is if it was our official first date. Don't you?"
    MC "...Yeah. Yeah I do."
    "I intentionally pulled Honoka closer with my arm until she was as close to my torso as she could get. She smiled back up at me, and we stood like that, waiting at the bus stop, until the bus came to take us home."
    "Yeah, this was a good day."
    jump daymenu

label BE020_c2_2:
    $setVar("BETomboy", getVar("BETomboy") + 1)
    MC "Ah, go ahead then. Sorry."
    "Honoka was trying to be polite after all. Eventually it became rude to try and insist on something, I figured."
    "She took out two 500 yen notes in addition to her gift card and handed them over to the waitress. She began putting it in the register and smiled back once it was finished."
    Waitress "Thank you again for dining with us. We hope to see you again."
    show BE happy
    BE "It was super tasty. I'd love to come back some time. Thank you!"
    MC "Yes, thanks very much."
    "Honoka smiled as we walked out of the restaurant. She stretched her arms up in the sky and smiled as she cracked her back."
    show BE aroused
    BE "Ah. That was a good meal. Mmf."
    MC "It was. Thank you again for treating me."
    show BE happy
    BE "Hey, nothing says the guy has to be the one to pay for stuff on dates, right?"
    MC "I guess I wasn't sure if this was a date or not."
    BE "Oh it's totally a date. I just wasn't sure if you'd come if I told you that upfront."
    MC "Is that so? How many dates have we been on, then?"
    show BE neutral
    BE "A bunch, I figure. But this is the first date in terms of, like… dating."
    MC "So we're dating now?"
    show BE happy
    BE "Haha. Of course we're dating. Why? Doesn't seem official enough yet?"
    MC "Well if I knew that I really would have insisted on paying."
    show BE unique
    BE "Nah. That's not what makes a first date important. Ooh, I know what does, though."
    MC "What?"
    "Honoka suddenly stepped in front of me, and nudged me towards a wall, until my back was up against it. I let out a stutter of confusion before she stepped on my feet, leaning up."
    MC "Uh."
    "Honoka smirked, staring at me right in the eyes, before leaning up and kissing me on the nose. Her boobs pushed right up underneath my chin, smothering my jaw. My knees started to wobble and it wasn't due to her feet pressing on mine."
    show BE happy
    BE "Hehe. First date's too early for mouth-kissing. But maybe next time."
    "Honoka smirked coyly and wagged her finger."
    show BE unique
    BE "But I bet you were thinking I'd do something naughty, didn't you, Kei-chan?"
    MC "Er, um… maybe not 'thinking', as much as… 'hoping'?"
    BE "That's why I've gotta pace out the affection, Kei-chan! You're already enough of a perv. Gotta make sure you don't get too outta control or you'll end up like some lame harem protagonist."
    MC "Heh, okay. "
    "I rubbed the bridge of my nose. It was somewhat damp. I didn't see any lipstick on her, but had she put on some lip balm or something?"
    MC "I still got a kiss, though, I'm counting that."
    show BE aroused
    BE "Nuh-uh. There's rules to this. It's our first date, but not our first kiss. Okay?"
    "Honoka stuck her hands behind her head as we walked back to the bus stop, to wait for our ride home."
    MC "Okay, Honoka. If you insist."
    MCT "I'm still counting it."
    jump daymenu