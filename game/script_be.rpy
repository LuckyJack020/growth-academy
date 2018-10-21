define BE = Character('Honoka', color="#FCCF20")

image BE neutral = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE-2-neutral.png",
    "True", "Graphics/BE-1-neutral.png")
image BE happy = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE-2-happy.png", 
    "True", "Graphics/BE-1-happy.png")
image BE sad = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE-2-sad.png",
    "True", "Graphics/BE-1-sad.png")
image BE surprised = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE-2-surprised.png",
    "True", "Graphics/BE-1-surprised.png")
image BE angry = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE-2-angry.png",
    "True", "Graphics/BE-1-angry.png")
image BE aroused = ConditionSwitch(
    "gametime > datelibrary['BE_size_2']", "Graphics/BE-2-aroused.png",
    "True", "Graphics/BE-1-aroused.png")

image cg BE001 = "Graphics/BE-SC-1.png"
image cg BE002 = "Graphics/BE-SC-2.png"

init 2 python:
    datelibrary['BE001_deadline'] = datetime.date(2005, 4, 13)
    datelibrary['BE007_deadline'] = datetime.date(2005, 4, 13)
    datelibrary['BE_size_6'] = datetime.date(2005, 12, 10)
    datelibrary['BE_size_5'] = datetime.date(2005, 12, 10)
    datelibrary['BE_size_4'] = datetime.date(2005, 12, 10)
    datelibrary['BE_size_3'] = datetime.date(2005, 12, 10)
    datelibrary['BE_size_2'] = datetime.date(2005, 4, 20)
    
    eventlibrary['BE001'] = {"name": "BE001", "girls": ["BE"], "location": "roof", "time": (TimeEnum.ANY, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "BE001_deadline",              "conditions": []}
    eventlibrary['BE002'] = {"name": "BE002", "girls": ["BE"], "location": "campuscenter", "time": (TimeEnum.ANY, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "testday",             "conditions": []}
    eventlibrary['BE003'] = {"name": "BE003", "girls": ["BE"], "location": "campuscenter", "time": (TimeEnum.AFTERSCHOOL, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",     "conditions": []}
    eventlibrary['BE004'] = {"name": "BE004", "girls": ["BE"], "location": "track", "time": (TimeEnum.AFTERSCHOOL, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",            "conditions": []}
    eventlibrary['BE005'] = {"name": "BE005", "girls": ["BE"], "location": "classroom", "time": (TimeEnum.ANY, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",                "conditions": [[ConditionEnum.PRESET]]}
    #eventlibrary['BE006'] = {"name": "BE006", "girls": ["BE"], "location": "classroom", "conditions": [], "priority": 0}
    eventlibrary['BE007'] = {"name": "BE007", "girls": ["BE"], "location": "cafeteria", "time": (TimeEnum.DAY, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "BE007_deadline",         "conditions": []}
    eventlibrary['BE008'] = {"name": "BE008", "girls": ["BE"], "location": "dorminterior", "time": (TimeEnum.AFTERSCHOOL, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",     "conditions": [[ConditionEnum.OR, [ConditionEnum.EVENT, "BE007"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["BE007_deadline"]]]]}
    eventlibrary['BE009'] = {"name": "BE009", "girls": ["BE"], "location": "track", "time": (TimeEnum.ANY, WeekendEnum.ANY), "priority": False, "startdate": "day_0", "enddate": "day_end",                    "conditions": []}
    eventlibrary['BE010'] = {"name": "BE010", "girls": ["BE"], "location": "dorminterior", "time": (TimeEnum.NIGHT, WeekendEnum.ANY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",       "conditions": []}
    eventlibrary['BE011'] = {"name": "BE011", "girls": ["BE"], "location": "track", "time": (TimeEnum.AFTERSCHOOL, WeekendEnum.ANY), "priority": False, "startdate": "BE_size_2", "enddate": "day_end",        "conditions": []}

label BE001:
    scene Classroom with fade
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
    "Honoka tilts her head back and took a swig. Then another, and another. With each swallow of soda that went down her gullet, she tilted her head further back. Gradually, this showed off more and more of her stomach as her shirt was lifted out of her gym shorts, showing off her thin waist and tiny belly button. It also made me wonder how much of her lower vision was blocked off by her chest, because as she arched her back, her breasts were raised up higher, sticking out like buoyant balloons from her torso."
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
    BE "Nothing, hehe. Thanks for the drink, Kei-chan, but I better get going. Next time I'll owe you a drink, okay? I'll make sure to take a sip from it first so we're even. Tricking a young girl into giving you a secondhand kiss, you playboy."
    "Honoka winked and made her way over to the soccer field, leaving me there, speechless for a moment."
    hide BE with dissolve
    MC "Wait, what? That wasn't why I gave you the drink, I was just, oh, darnit.... I'm still thirsty."
    jump daymenu

label BE003_c2:
    show BE neutral
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
    "It was another hot day outside the campus. Too hot for me to bear going outside for any reason that didn't involve diving into a pool of ice cold water. Instead I figured I'd spend the day in my room, catching up on updates of some weekly manga I'd lost track of."
    "KNOCK ! KNOCK !"
    "I had barely gotten started when the door knocked. Tashi was out, so I figured he'd simply forgotten his key."
    MC "Hey, what's up?"
    show BE happy with dissolve
    BE "Oh hi Kei-chan! Good, you're hanging out here, can I come in?"
    MC "Oh!"
    "Seeing Honoka outside of my door was definitely something I didn't expect. But it was far from unwanted. Besides, it was nice to see her head-on without having her run into me like she often did." 
    MC "Yeah, sure, come on in. There's not a rule about having girls in my room is there?"
    show BE neutral
    "I don't think so. I can't see why. Unless you were planning something naughty, in which case I am {i}not{/i} prepared at all."
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
        "Then I guess I need to check you for mechanical parts…":
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
    MC "You… You really have a way with double entendres, you know that?"
    show BE surprised
    BE "Huh? What'd I say? I didn't mean to that time…"
    MC "Oh. Well. Never mind then. I must have been mistaken."
    show BE happy
    BE "Heh, or your mind was naughtier than you initially thought, eh?"
    "Don't blame me, Honoka. You're the one who's like a computer virus for my head whenever you come around."
    MC "No, that's not it at all. Let's just, let's get back to reading manga."
    $setAffection("BE", +1)
    jump BE008_after
            
label BE008_c2:
    MC "Then I guess I need to check you for mechanical parts…"
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
    BE "Whew… heh. Well… that was a thing."
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
    $setAffection("BE", +2)
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
    MC "Oh it's clearly just the fanservice pinup to sell some extra copies…"
    show BE happy
    BE "Heh, I'm kidding. But, hey, you don't mind if I hang for a while, right? I'm kind of bored."
    MC "No, not at all."
    jump BE008_after

label BE008_after:
    "Honoka and I spent the rest of the afternoon together, just hanging out and catching up on manga. It was nice, something I hadn't really had a chance to do with a friend in a long time. Tachi was not exactly the type of guy who would just sit and read unless it was a bunch of conspiracy theories. Honoka was much, much more fun."
    jump daymenu
    
label BE009:
    scene Track with fade
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
    BE "Hey Kei-chan! Nice to see you out here!"
    MC "Well I had to at least come see your first match, right?"
    BE "Yeah, that's really nice. I liked your little chant, too."
    $setAffection("BE", +1)
    MC "Sorry it wasn't that good. Next time I'll work on it beforehand."
    show BE neutral
    BE "You better! No slacker cheerleaders in {i}my{/i} section."
    show BE happy
    BE "Just kidding! It was sweet of you to cheer me on."
    MC "I'm glad to hear it. So you're saying you made that last goal because of my encouragement?"
    BE "Hehe, well I wouldn't go {i}that{/i} far. But it definitely helped."
    MC "Awesome. So you're liking the soccer club, then?"
    show BE neutral
    BE "Yeah. It's pretty fun. The coach is nice and the other players are neat to hang out with. Still, almost feels like…"
    show BE sad
    BE "I dunno."
    show BE neutral
    BE "Almost like \"I've done soccer already. Should I try something new?\"."
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
    BE "Hey there Kei-chan!"
    MC "Hey, Honoka."
    show BE neutral
    BE "Heh, thanks for the cheer back there, goofball."
    $setAffection("BE", +1)
    MC "Oh! You're welcome. Glad you liked it. I didn't have much time to come up with something."
    show BE happy
    BE "Really? I couldn't tell. Though maybe the fact you immediately went to \"booooobs\" was a clue."
    MC "Come on, when we played it was either just \"get the ball in the goal\" or \"hit each other with the ball\". I don't know enough about the sport to make insightful comments!"
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
    $tmp = setSkill("Athletics", 1)
    "(Your athletics skill has increased to [tmp])"
    jump daymenu

label BE009_c3:
    "I didn't want to interrupt the game with a silly chant, especially when the stakes were so low, so I just stayed quiet and watched Honoka play."
    "She really was good. It wasn't long after I arrived that Honoka managed to snatch the ball away from the opposition in the last minutes of play and kick it into the goal. She ended up falling over from the huge force she put onto getting the ball from midfield all the way past the goalie, but it did the trick."
    "After the game was won, Honoka jogged off the field, coming up to where I was sitting on the sidelines. Her gym clothes were ringed with sweat, the bottom curves of her breasts forming a crooked sweat-stain smile across her front."
    show BE neutral with dissolve
    BE "Oh hey Kei-chan, I didn't know  you were watching! How long have you been here?"
    MC "Long enough to see you're pretty good still."
    show BE happy
    BE "Heh, thanks. Let me know next time so I can show off for you."
    hide BE with dissolve
    "She gave me a wink and shook her shoulders a bit before leaving to follow the rest of the soccer club. Wondering what kind of \"showing off\" she meant, but satisfied that I'd hung around long enough, I got going myself."
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
    MC "Hi Honoka."
    show BE surprised
    BE "Oh, you recognize me?"
    "I looked up at her in confusion. She sounded oddly serious. Stepping away, I took a better look at her face, somewhat worried that she'd cut her hair or something had happened to her face. Just something that would make me have trouble recognizing her. Nothing seemed out of the ordinary, though."
    MC "Of course I recognize you. Is something the matter? Why do you think I wouldn't recognize you?"
    show BE neutral
    BE "Because I'm bigger?"
    MC "Bigger?"
    "I held my hand to the top of my head, and then moved it flat towards Honoka. Seemed to be the same height difference as before…"
    show BE happy
    BE "Kei-chan, you dork. I mean, 'bigger'."
    "Her gaze made it obvious what she was referring to, but clearly Honoka wasn't sure that I got the hint. To ensure I knew exactly what she was talking about, she reached down and grabbed her chest, lifting up a breast in each hand, as if she were presenting them to me."
    MC "Oh! Duh, right. That makes sense."
    "It did, but it was strange that she was so surprised about it."
    MC "Did you, like, not believe that your breasts were going to get bigger? You were all about it when you received your confirmation."
    BE "Well yeah, obviously. It's not like I just jumped up a bunch this morning. They've been growing for a while now. Bit by bit. I've been measuring. It's usually somewhere between a quarter and a half inch every day."
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
    BE "I came all this way here to show you how proud I am that I grew a whole foot since the start of the year and you didn't even realize it!"
    MC "Oh, um, sorry, I didn't meant to upset you."
    show BE neutral
    BE "You want to apologize to me?"
    MC "Yeah?"
    BE "Alright then."
    "Honoka stepped forward and gained a devious smirk on her face."
    show BE happy
    BE "Touch 'em."
    MC "What?"
    BE "I want you to touch them, so you have proof that they've grown significantly since you first saw them again."
    MC "You… you wha… Uh…"
    "My brain struggled to comprehend what Honoka had just offered. Her tone of voice wasn't like she was trying to be flirtatious or intentionally sexy. It was more like a judo instructor demanding you try and grab their arm so they could perform a flip and toss you onto your back."
    "It just felt like a trap. But, my hand still twitched a bit, trying to fight the impulse in my head. There was nothing that sounded bad about getting a handful of Honoka's chest, it might be worth any potential repercussions…"
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
    MC "I just… don't think it's appropriate, Honoka. We're friends."
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
    MC "Ah, heh… for now how about just 'Can I come in and play some video games?' instead?"
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
    "But, also, they were… dense. It seemed like an odd term to describe breasts, but it was accurate. For as big as they were, they still felt heavier than I expected them to. I carefully moved my hands so they cupped Honoka's boobs instead, and pushed up. They took a slight bit more effort to move than I thought they would, and when I finally pulled my hands away, I got to see them bounce for a few seconds before stopping."
    MC "Wow."
    show BE happy with dissolve
    BE "Heh, heh. Get yourself a good handful? How did they feel? Were they as soft as you imagined? Were they warm? Tell me!"
    MC "Whoa, um, well. They're… big?"
    BE "And?"
    MC "Soft?"
    show BE neutral
    BE "Yes, yes, and?"
    MC "I, I, I don't… they're awesome?"
    show BE happy
    BE "Thaaat's the ticket. Boobs are awesome, aren't they?"
    MC "Well. Not by default, no."
    BE "Ah, you're saying they have to be at my size to be any good at all?"
    MC "Not necessarily. Yours definitely… transcend most sizes though. And probably eclipse a lot of them in softness too. They've bumped into me before but, it really feels different in the hand compared to the back of the head."
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
    BE "Hehehe…"
    "Honoka suddenly loomed forward, her breasts inches away from my face. My knees buckled. I felt like I was suddenly talking to Shiori, not my childhood friend."
    BE "It means I know what kind of guy you are."
    MC "I… um."
    BE "A guy who takes charge and opportunity when he can."
    hide BE with dissolve
    "Honoka pulled back and smirked at me, her smile looking like it could slide off of her face. She grabbed the handle of my door with one hand, and then turned to wink at me."
    show BE happy with dissolve
    BE "And I like that kind of guy."
    hide BE with dissolve
    "With that, Honoka shut the door behind her, leaving me to wonder what just happened."
    $setAffection("BE", +1)
    jump daymenu

label BE010_c3:
    MC "…"
    "I just couldn't say anything. My mouth felt like it dried up. Something about this was wrong. I wasn't sure what her game was, but I felt like the smart thing to do was just shut up."
    show BE neutral
    BE "Hello, Kei-chan?"
    "The only sound that managed to come out of my mouth was a weak, guttural stutter."
    show BE sad
    "Okay, Kei-chan. I get the message."
    "Honoka pulled back her balloons and wordlessly left my room, leaving me utterly confused. She only came in to show off her breasts? It just didn't make sense. Maybe she wasn't feeling well. Hopefully she went off to her room to relax for a bit, it seemed like she needed it."
    $setAffection("BE", -1)
    jump daymenu
    
label BE011:
    scene Track with fade
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
    MC "I… I don't even know what that is."
    show BE happy
    BE "Then come up with something better, because that was obviously terrible."
    MC "You have my word I'll make something cheery that doesn't get confusing. Now, we should probably watch the game now, huh?"
    BE "Sounds good to me."
    jump daymenu

label BE011_c2:
    MC "It's okay, that club was dumb anyway."
    $setAffection("BE", -1)
    show BE neutral
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
    BE "I tried not to look back at the bleachers as I left the soccer field. Honoka was never the type to hold grudges, so I didn't think this would come back to bite me later. But I still felt like an idiot saying what I said…"
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
    $setAffection("BE", +1)
    jump daymenu