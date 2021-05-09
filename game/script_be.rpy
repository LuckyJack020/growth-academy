label BE001:
    $setProgress("BE", "BE002")
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
    show BE happy at center with dissolve
    BE "It does. And it's about to look a whole lot better!"
    play music BE
    "My introspection was suddenly interrupted by my elbow getting pressed into something warm and soft."
    MC "What the... Honoka? How'd you get up here?"
    BE "Heh, the same way as you, Kei-chan. Steps. I've been behind you for a while now, did you really not notice?"
    MCT "Not until you bumped into me with that chest of yours..."
    MC "I guess not. My head's kind of all over the place after learning why we're here. How about you? You said you didn't know what this academy was for, right?"
    show BE neutral
    BE "Nope, no clue until teach explained it. It's so weird, don't you think something like this would be more public knowledge?"
    MC "I'd say so. But, if it's only a small group of people affected by this weird growth hormone thing, maybe it's better to not cause a panic of people assuming they've got it."
    extend " 'Oh gosh, I shot up two inches over the summer, I'm going to end up ten feet tall!'"
    show BE happy
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
    extend "What did I just say?"
    show BE surprised
    BE "Kei-chan! To think you'd be so forward..."
    show BE surprised at center, Transform(xzoom=-1)
    BE "I know I said I was in your care, but I didn't think you'd take in that way..."
    MC "Wait, wait, that was a big misunderstanding, I didn't mean to imply anything that-"
    show BE happy at center, Transform(xzoom=1)
    BE "Bahahaha, oh, wow, Kei-chan, heh, it's too easy to mess with you sometimes, you know that?"
    MC "Yeah, you've certainly taught me that lesson many times in the past. Ow..."
    "I winced as she gave me a playful punch in the arm. One that went a little too deep to be completely painless."
    jump BE001_after

label BE001_c2:
    BE "That's true. Still, I think I've got a pretty good idea what mine could be. It starts with 'B' and rhymes with 'goods'."
    MC "...Boods?"
    show BE sad
    BE "What? Shoot, no, I messed that up. I was talking about my boobs."
    show BE neutral
    BE "Like everyone at my old school seemed to do on a daily basis. Hard to blame them really, I made these cans faster than a soda factory."
    MC "Oh, heh. Well, that could have just been some lucky puberty at work, you know?"
    show BE happy
    BE "Sure. Still, if it was my boobs, I wouldn't mind it."
    MC "You wouldn't? But you just said everyone at your old school mentioned them all the time."
    show BE angry
    BE "Eh, I don't care about that. I doubt I'll care here, either, if everyone's got a chance of getting giant knockers, too."
    extend " Besides, big breasts, well, they kind of seem like the most normal thing I could get, right? I've heard of models or actresses with oddly-sized boobs in the past, so it's not that unusual."
    MC "Hm, guess you've got a good point. You're already used to big boobs, anyway."
    show cg BE001
    pause 0.5
    hide cg
    show BE happy at center
    BE "Exactly! Hehe, you know, Kei-chan, most boys wouldn't be so brazen about talking about a girl's chest, especially to her face."
    MC "W-Well, you're the one who brought them up in the first place!"
    show BE neutral
    BE "Did I now? Oh, I guess I did. Yep."
    MC "Not the least bit apologetic about it, are you?"
    show BE happy
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
    show BE sad
    BE "Yeah but then it'd be hard to talk with you. That'd stink."
    MC "Yeah, it didn't look that appealing, did it?"
    show BE neutral
    BE "Nope. You know what did look appealing though?"
    MC "What?"
    show BE happy
    BE "Come on, I know you saw it."
    MC "Saw what?"
    show BE neutral
    BE "It was staring you right in the eyes!"
    MC "Honoka I really don't-"
    show BE happy
    BE "Pff, I'm talking about my breasts, Kei-chan. Don't think I didn't catch you sneaking a peek when we met up outside the academy."
    MC "Oh, well, listen, if I'd known you were Honoka, I wouldn't have-"
    show BE unique
    BE "Mm-hmmmmmm. Don't be embarrassed, Kei-chan, it's fine. You're a young man with healthy ambition. Though, I do think I deserve a little payment for you staring hard enough to melt my shirt."
    MC "What do you me-ouch..."
    show BE happy:
        linear 0.1 xpos 0.8
        linear 0.1 xpos 0.5
    BE "There!"
    "I quickly moved my hand to rub a sore spot on my upper arm where Honoka had given me a gentle punch. Hopefully her growth factor isn't her hands, or those punches are going to get a lot harder..."
    jump BE001_after

label BE001_after:
    show BE happy
    BE "Ahh... just like old times, huh Kei-chan?"
    MC "What do you mean?"
    BE "I mean, you, me, and the roof! The original power trio. How many times do you think we snuck up to the roof when we were younger? 100? 200?"
    MC "It was probably a few dozen times if that."
    show BE sad
    BE "Eh, you're exaggerating. Still, it's a great wave of nostalgia being up here with you Kei-chan."
    BE "You know, this academy's definitely a weird place, and we're gonna go through some strange stuff by the sound of it. But, I'm really glad you're here, Kei-chan. Makes things a bit easier."
    MC "Please, Honoka, when have you ever backed down from a challenge, anyway?"
    show BE happy
    BE "Never! And that's why they call me Hard-To-Beat Honoka!"
    MC "I can guarantee nobody has ever called you that."
    BE "Well I'm sure they call me something. I'll get a nickname by the end of the year, I guarantee it. One that suits me! Just you wait Kei-chan."
    "Honoka chuckled before she turned her attention back to the view from the roof."
    "Even through the chain link fence, it was clear she'd been captivated by the sight of the big buildings before her."
    "Her face was bright; she was no doubt thinking of all the new possibilities this academy would bring. I had to admit, I was a bit excited to see what was going to happen as well."
    "But at the moment, my focus was on Honoka. More specifically, the way her chest pushed against the chain link fence, making it look like she was wearing chainmail armor over her school uniform."
    jump daymenu

label BE002:
    $setProgress("BE", "BE003")
    scene Campus Center with fade
    play music Rain
    show BE neutral:
        xpos 1.0 xanchor 0.5 yalign 1.0
        linear 0.5 xpos 0.5
    pause 0.5
    show BE sad
    BE "Oof! Sorry about that, slippery ground!"
    MC "Ah, heh, it's no problem, Honoka. Hard to stop when you get moving, huh?"
    show BE neutral
    BE "Yep, not to mention I slept great last night so I've got tons of energy. I'm so excited, new school, new opportunities."
    MC "Sounds almost like you should have had a tough time getting to sleep then. I had trouble myself, my roommate is... weird. Plus, I'm a bit nervous about this whole thing."
    show BE happy
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
    BE "Yeah, should be fun!"
    show BE neutral at center, Transform(xzoom=-1)
    BE "It was a tough call between that and basketball actually, but I think I picked the right one."
    show BE sad at center, Transform(xzoom=1)
    BE "Though, I dunno, maybe something more physical, I didn't see if there was a wrestling club, hm."
    MC "Well, maybe just stick to one club for now, yeah? Not like you can join them all, anyway, so don't worry about one club you missed out on, because there's no way you'd be able to do them all regardless."
    show BE happy
    BE "Oh yeah? You think it'd make me too tired?"
    MC "No, I mean I'm sure that's literally impossible. There's no way they'd have the clubs all worked out in a way where it would be possible for you to attend every event, along with leaving time for schoolwork."
    show BE sad
    BE "...Well when you put it that way it sounds pretty silly, doesn't it? You sure are clever, Kei-chan."
    "I think that qualified more as 'common sense' as opposed to 'cleverness', but, I'll take it."
    show BE neutral
    BE "What about you, Kei-chan, were you thinking of joining a club?"
    MC "Me? Honestly I'm not sure. I hadn't given it much thought yet. I think I might hold off until I know for sure what my growth factor is. I really don't have any clue yet. I wouldn't want to pick something I'd be unable to do once I started growing."
    BE "That's a good point. Would be really lame to get good at something and then end up being unable to do it. So, probably best if you don't pick something like tap-dancing for when you end up getting gigantic feet."
    MC "If I end up getting gigantic feet, I'll join the soccer club just to show you how hard I'll be able to kick."
    show BE happy
    BE "Hehehe, I'd like to see that."
    "Honoka smiled as she gave me a little tap on the arm. I gave a sharp inhale and laughed as I began to rub the spot where she hit me. Forget worrying about her kicks, her punches still had a good sting to them after all these years."
    "Maybe it's her subconscious way of making up for when she bumped into me with her chest earlier?"
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
    show BE unique
    BE "Because it makes my boobs bounce?"
    "Damnit."
    MC "No, it's just, I dunno, making one another laugh, seems like something only friends do for each other?"
    show BE happy
    BE "Heh, I guess so. I can see your logic there, Kei-chan. But then you really need to work on your sense of humor."
    MC "Hey, you make me laugh all the time, so my sense of humor is fine. You need to get one instead."
    show BE neutral
    BE "I'll get one when you get fitted for your size 38 feet."
    MC "Hehehe, dangit, Honoka. See, got me laughing that easily."
    BE "I know. That's because I'm awesome."
    "Honoka smiled and put her fists on her hips in a haughty pose, reminding me of Alice for a moment. Only while Alice was unbelievably serious in her holier-than-thou attitude, Honoka was obviously kidding."
    "We stood there chuckling for a bit more before Honoka noticed the time and decided to get going. I nodded and waved goodbye, sticking my hands in my pockets before heading off myself."
    jump daymenu

label BE003:
    $setProgress("BE", "BE004")
    scene Campus Center with fade
    play music Hallway
    "The sun was scorching today. The kind of heat that tricked you into thinking it would be all right to go outside for a while, but once you were in the rays of the sun, you realized what a horrible mistake that was."
    "I had already drank a whole bottle of water to cool off, but it wasn't enough. Thankfully, there were vending machines scattered around, and I had a few coins burning a hole in my pocket."
    MC "All right, let's see. What do I want? Soda, juice, eh, water's healthier... but, soda's tastier."
    "After sliding in my change and selecting my drink, I bent over to retrieve my precious bounty. The sharp hiss of carbonation escaped the can as I opened it up and took a refreshing swig."
    MC "Mmm, much better."
    "I turn around to walk off and end up bumping into someone. More specifically, I bumped into Honoka. Even more specifically, I bumped into the spot where one was most likely to bump into Honoka."
    "After I caught my balance from the impact of stepping right into her chest, I cleared my throat and looked at her."
    MC "Whoops, uh, hey Honoka. Sorry about that. Wasn't watching where I was going."
    show BE athletic-happy at center with dissolve
    BE "Hehe, hey Kei-chan. Don't worry about it, was an accident, right?"
    MC "Right."
    "I noticed that Honoka wasn't wearing the normal school uniform, having traded out the classic skirt and shirt combo for a pair of spats and a more tightly-fitted t-shirt."
    MC "What's with the get-up?"
    show BE athletic-neutral:
        ypos 1.0 yanchor 1.0
        linear 0.1 ypos 1.05
        linear 0.1 ypos 1.0
    BE "Oh, I had soccer practice in a bit, this is the official uniform. Bit snug, though."
    "Honoka tugged down on her shirt and stuffed it into her shorts. Clearly that was the way it was supposed to be, but when she stood straight up, the front of the shirt kept coming out of the spats, exposing a tiny sliver of her waist."
    MC "Why didn't you just get the next size up?"
    show BE athletic-angry
    BE "I dunno. Figured I'd try it out first, no sense causing a fuss about the size if I end up not liking soccer, after all."
    MC "I guess that makes sense. Damn, but it's going to suck having soccer practice today when it's this hot out. Hopefully it doesn't last too long."
    show BE athletic-sad
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
    show BE athletic-neutral
    BE "Ooh, what did you get?"
    MC "Ah, like, a lemon-lime soda. It's pretty good. Want a sip?"
    show BE athletic-happy
    BE "Heh, sure."
    "I handed the can over to Honoka and saw her sniff it a bit."
    BE "Mm, smells good."
    "Honoka tilted her head back and took a swig. Then another, and another. With each swallow of soda that went down her gullet, she tilted her head further back."
    "Gradually, this showed off more and more of her stomach as her shirt was lifted out of her gym shorts, showing off her thin waist and tiny belly button."
    "It also made me wonder how much of her lower vision was blocked off by her chest, because as she arched her back, her breasts were raised up higher, sticking out like buoyant balloons from her torso."
    "By the time she finished off my drink, they were practically pointed straight up, only to come swinging back down to their normal height when she swallowed the last drop and stood straight up again."
    show BE athletic-happy
    BE "Ah, that really hit the spot! Thanks Kei-chan!"
    MC "Yeah, no problem."
    "My tongue felt like a desert. I rifled in my pockets to see if I had enough change for another drink."
    show BE athletic-neutral
    BE "Hm..."
    MC "What's up?"
    "Wordlessly, Honoka took the now-empty can and placed it against her chest, right between her breasts. She held it there for a moment, obviously in contemplation, but it wasn't clear what she was thinking about."
    show BE athletic-unique
    BE "..."
    "After a while it ended up being a moot point as she just tossed the can in the nearby recycling bin."
    show BE athletic-neutral
    BE "Never mind, probably not big enough anyway. Would hurt, I bet."
    MC "Huh?"
    show BE athletic-happy
    BE "Nothing, hehe. Thanks for the drink, Kei-chan, but I better get going. Next time I'll owe you a drink, okay? I'll make sure to take a sip from it first so we're even. Tricking a young girl into getting a secondhand kiss, you playboy."
    "Honoka winked and made her way over to the soccer field, leaving me there, speechless for a moment."
    hide BE with dissolve
    MC "Wait, what? That wasn't why I gave you the drink, I was just, oh, darnit... I'm still thirsty."
    jump daymenu

label BE003_c2:
    show BE athletic-neutral
    play music BE
    BE "Yeah that's probably a good idea. Hm..."
    "Honoka walked over to the vending machine as I took another sip of my soda."
    "She hummed to herself for a while as she looked over the various options, eventually deciding on something and paying for it. As she opened a bottle of water, I racked my brain for a point of conversation."
    MC "So... soccer, huh?"
    BE "Yep, should be pretty fun. Lots of running and kicking things."
    MC "I bet. Don't know a lot about it myself, but is there any specific position you want to do?"
    BE "Just anything besides the goalie. I'm sure it's tough work but I want to make sure I'm out in the field getting the most exercise, running around and sweating it out."
    MC "Right. Well if that's the case you really do need to make sure you stay hydrated."
    show BE athletic-surprised
    BE "Of course, I'm not a numbskull, Kei-chan!"
    MC "Never said you were. Just, it's an easy thing to forget when you're focused on something and I know you, Honoka. When you get focused on something, occasionally you can get a bit of tunnel vision."
    "Honoka tilted her head from side to side several times like a metronome."
    show BE athletic-sad
    pause 0.5
    show BE athletic-happy at center, Transform(xzoom=-1)
    show BE athletic-angry at center, Transform(xzoom=1)
    show BE athletic-neutral at center, Transform(xzoom=-1)
    BE "Yeah you've kind of got a point there. Well if you wanted to, you could probably come watch me. I doubt they'd mind. Then you can remind me to drink if I forget."
    MC "Maybe I'll do that, I don't think I have anything else going on."
    show BE athletic-neutral at center, Transform(xzoom=1)
    BE "Heh, sounds good. Well, if you come I'll see you over at the soccer field. If not, well, see you whenever. Have a good day, Kei-chan."
    MC "You too."
    "Honoka raced off to the soccer field as I took another drink, and decided whether to go follow her or chill somewhere else for the rest of the afternoon. It was really hot, after all."
    jump daymenu

label BE003_c3:
    #should this be an affection loss? she even calls it a "fun talk"
    $setAffection("BE", -1)
    play music Tension
    show BE athletic-angry
    BE "Kei-chan, you should have called them udders if you were gonna make a cow joke."
    MC "Darn, you're right. Haha."
    show BE athletic-neutral
    BE "Though..."
    MC "Though, what? Are you really, I mean, I didn't mean to insult you if you were. Not that I'd think it was a bad thing or something like that, I just, if you weren't cool with it, I, uhhh."
    show BE athletic-sad
    BE "No no, it's not that. Just, now you've got me wondering if that's possible."
    BE "I mean, I'm not an expert on female mammaries or anything but, there's obviously parts of the breast meant to make milk, so what would happen if they swelled up and started getting bigger?"
    show BE athletic-neutral
    BE "Would that mean the woman would start making a ton of milk, or would it just increase the size of the breasts around them, but keep the level of lactation about the same?"
    MC "I uh, I don't really know how to answer that. I think it'd be weird for a tiny part of the body to be affected like that, though. If it was, I'd say, probably a bit of both?"
    BE "Huh. Interesting to think about."
    "Honoka and I both stood there for a moment, saying nothing to each other. Our eyes weren't really focused on one another either. It took a good minute or two before I finally broke the silence."
    play music BE
    MC "Have we both been thinking about milky breasts now?"
    show BE athletic-happy
    BE "Probably! But I'm a girl, it's okay for me to think about it. You're just a pervert."
    MC "That's not fair, you put the idea in my head."
    BE "I just planted the seed. You're the one who watered it and let it grow. Could have plucked it out at any time."
    MC "That's not how thoughts work. That's not how anything works."
    BE "Apparently it is, ehehehe."
    "Honoka chuckled, and licked her lips. She looked over at the vending machine, but then pulled out her phone and checked the time."
    show BE athletic-sad
    BE "Darn, I need to get going or I'm going to be late. Won't do good to be tardy for the first soccer club meeting."
    MC "Ah good point, don't let me hold you up then."
    show BE athletic-neutral
    BE "Thanks. Thanks for the fun talk, too. See you around, Kei-chan."
    MC "See ya, Honoka!"
    "I gave a nod to Honoka as she ran to the soccer field, then leaned against the vending machine as I continued to drink my beverage. It was too hot today."
    jump daymenu

label BE004:
    $setTimeFlag("testday")
    $setProgress("BE", "BE007")
    scene Track with fade
    play music Busy
    "I decided to head over to the soccer field. Before I even got on the grass, I heard the sound of a coach whistle blowing, directing students in their training. I picked up the pace a little bit so I could see what was going on."
    "Among the small crowd was a familiar face. I waved over to Honoka, who enthusiastically waved back to me. She seemed happy to see me. I looked around for a place to sit."
    "There were bleachers nearby, but I decided to just sit down on the grass for a while, making sure I stayed out of the way."
    MC "This is cool. Good to see there's still a sense of normalcy in this place, doesn't look like the soccer field is anything special or different."
    "The coach didn't look that special either. Not that he was ugly or anything, but there wasn't anything on the cap-wearing man that I recognized as being overly-large."
    "It made sense, I guess. While there must have been enough students in the country to require a facility like this, it didn't mean that there'd be an equivalent number of faculty members who shared odd growths as well."
    "The academy probably had to take what they could get."
    MC "Man, Honoka's pretty good at this."
    "That wasn't all that big of a surprise. She always was pretty athletic. We even played soccer together when we were younger, whether it was just kicking the ball around or actually trying to score goals."
    "Maybe I'd look into joining the soccer club myself, it would give me something to do after classes, for one. Plus, it wouldn't hurt to have more chances to see a childhood friend."
    MC "Phew, it's really hot today..."
    "I wondered if there was anything nearby to drink. Fortunately, it looked like they provided a water cooler. Good, at this heat the students were likely to pass out if they didn't get any hydration."
    "Still, I couldn't just go over there and take some when I'd just been sitting on my butt for twenty minutes. Thankfully the coach called for a break after a while, and I walked over to get some water with the others."
    MC "Hey Honoka!"
    show BE athletic-surprised at center with dissolve
    BE "Woo, hey, Kei-chan. Glad you came by!"
    MC "Well, you know I've always had a thing for soccer."
    show BE athletic-neutral
    BE "Sure. I'm surprised you didn't join the soccer club, actually. Were you just afraid I'd beat you whenever we were asked to go against each other? If I recall I won more of our games when we used to play."
    MC "What? No, that can't be right. I'm positive I won more."
    BE "You beat me a lot, but I remember two wins over you that gave me the edge."
    MC "That one where you hit me in the nose with a soccer ball shouldn't count!"
    BE "It wasn't intentional or anything! And besides, you still wanted to play, it was just your mom that pulled you out before you could get another goal on me, but I'm counting that as a win anyway."
    MC "Fine, what was the other win that gives you the majority over me?"
    BE "It must have been in the summer, I guess the last one before we had to split up. You tried to shoot a goal like, four times in a row, and you just kept hitting the side of the goal."
    BE "Every. Single. Time. It was funny the first three times, but the fourth one was just sad."
    BE "I didn't even try to block it, I just stood there as it bounced up in the air and landed in the other goal instead. It was nuts."
    MC "...Oh geez I remember that now. Ugh, I don't know what was wrong with me that day, but yeah, I must have been super distracted about something."
    BE "I'm just glad you conceded the match right there. If you tried to do a fifth shot, you probably would have kicked the side of the goal again and then the ball would have gone through one of the windows in your house instead."
    BE "A sixth attempt would have knocked you out cold."
    MC "I can't believe you remember that."
    show BE athletic-happy
    BE "Hey I remember a lot about when we were kids, those were fun years! Lotsa good memories."
    "Honoka smiled as she finally poured herself some of the water from the cooler and took a big drink. I helped myself to some as well, after double-checking that there would be plenty for the others who needed it more."
    MC "It's good to hear that, I have to say. Definitely had some fun times together, didn't we?"
    BE "Mm-hm."
    "Honoka sat down in the grass, probably to rest her legs for a bit, and I joined her. She started scratching at her calves where the grass tickled her legs, groaning as she did so."
    BE "Ah, that's so much better."
    MC "What, you forgot running would make your legs tired?"
    show BE athletic-sad
    BE "No not that. Just, I dunno, soccer's still fun but there's something missing. Maybe it'll just take me a bit to get back into it, but, it's not quite got that 'umph' I was looking for."
    MC "Well, don't give up yet. Only the first day, right? Like you said, you probably just need a bit of time to get back into it."
    show BE athletic-neutral
    BE "Yeah that's probably it. Heh."
    "The coach blew his whistle again and called up the students to line up and run some more drills."
    show BE athletic-happy
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
    show BE happy at center with dissolve
    BE "Oh, Kei-chan!"
    "Honoka bounced over towards me, clutching a few pieces of papers in one hand. She stopped, but a little too late, and her breasts collided into my side. She just brushed it off and stepped back, shoving the papers inside her sizable chest for safekeeping."
    MC "Oh, Honoka. Hey. What's up?"
    BE "Well, just got my test results back."
    MC "Test results? Oh! Right, for the growth factor. That's why I'm here too. I guess it's time to finally bite the bullet and figure out what's going to grow on me."
    BE "I bet it'll be your feet or something lame like that, haha."
    MC "Ugh I hope not, buying shoes would be such a pain. Besides, you can't make fun of me for whatever mine is if I can't return the favor, what'd you get?"
    "Honoka smirked, and cupped her breasts in her arms. She lifted them up until the top curves of her fleshy spheres covered up the bottom half of her face. Her expression became hard to read once most of it was blocked by her bosom."
    "But, it was easily assumed that she was being playful about the fact that her palms overflowed with breast flesh."
    BE "What do you think it was?"
    MC "Was it really that obvious?"
    show BE neutral
    BE "If it hadn't been my boobs, I would have been really surprised. Would have had to go see a regular doctor to check on my breasts if that was the case, these puppies are pretty large already. A bit more growth would have been cause for concern, I think."
    MC "And finding out that your, uh, your boobs are going to get supersized isn't a concern?"
    "Honoka shrugged, throwing up her arms and giving a grunt."
    BE "Eh, can't be worse than what most of the others here are going to deal with, right? Besides, they gave me some good information about it. The nurse already had these printed out, too. I think the testing they did was more a formality than anything."
    "She eyed me up and pretty much said 'So, you know what you've got, right?' Not in those words, exactly, but I got what she meant."
    "Honoka reached into the expanse of her cleavage and pulled out the papers to flip through them."
    BE "I guess I'd been mentally preparing myself for this news to begin with, so, a lot of what the nurse said made sense. Plan ahead for when it comes to clothing, and they gave me a place where I can work on getting stuff fitted."
    BE "A few exercises to strengthen the back and shoulder muscles, just to be safe."
    MC "Well, now that you know for sure, how do you feel about it? I mean, it's boobs. So, most girls would probably be all for that, right?"
    show BE happy
    BE "Heh, I'm sure that's the male fantasy for sure. Eh, I'm sure it's true, though. I think in general, yeah, I'm excited!"
    MC "Yeah? Well, that's good. Are you going to have to keep buying new uniforms, or will they at least supply those for you?"
    BE "It looked like the deal was regular clothes I was mostly on my own with, but school uniforms would be provided and tailor-made for me, which is nice."
    BE "I mean, if you figure a normal school week anyway, uniforms are what I'll be wearing most of the time anyway. I wonder if they'll be standard or if they'll let me show off a little cleavage or something?"
    MC "Honoka! This is a school, I doubt they'll intentionally sexify the uniforms."
    BE "Well it would seem like a shame, otherwise. But I guess with my own things I'll be able to get them however I want them to look."
    MC "Why do I get the feeling you're only saying these things to mess with me?"
    BE "You'd be about... 80%% accurate if you're really thinking that."
    MC "What's the other 20%% then?"
    BE "That's me thinking 'boobs are fun'."
    MC "Heh, so, have you always wanted bigger boobs since you were younger or something?"
    BE "Hm, I don't know if I ever really thought about it that way. Like you said, I think pretty much every girl has that moment of breast envy at some point in their youth."
    BE "But, considering how much I blossomed, I guess I acclimated to the idea of huge knockers pretty easily."
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
    BE "It had to have been a couple of years ago, at least. I guess I grew a good amount to start off with. After they started growing, I was easily a c-cup in most brands by the end of that year. But then they just kept growing, and growing."
    BE "I never really thought it was anything to be concerned about though."
    MC "I don't think it is, really."
    show BE neutral
    BE "Right? They haven't been much trouble so far."
    MC "Did you get, well, picked on, at all?"
    show BE sad
    BE "Eh, a little bit here and there. Girls that were jealous, boys that wanted some. Both ended up calling me the same names though, people are so unimaginative."
    BE "There must be a hundred different words for boobs and they rarely ever used more than three. Got boring pretty quick."
    MC "Only you would get a bit bullied and school and call it boring because their taunts weren't creative enough."
    show BE happy
    BE "Yep, because I rock, Kei-chan. The girl with big boulders rocks as hard as mountains."
    MC "Think you tried a little too hard there."
    BE "Hard as my ni-"
    MC "Please stop."
    BE "Spoilsport."
    MC "Tease."
    jump BE005_after_old

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
    jump BE005_after_old

label BE005_after_old:
    MC "Well, I guess I should get going, need to find out what I'm getting after all."
    show BE neutral
    BE "The way you say it makes it sound like you're in line to get a superpower or something. Unless you get ultra-muscles, I don't think you'll be fighting any crime soon."
    MC "I doubt I'd get anything that cool. Anyway, thanks for talking to me, Honoka. I'll see you later."
    show BE happy
    BE "Bye Kei-chan, was nice running into you!"
    jump daymenu

label BE005:
    $setTimeFlag("aftertest")
    scene Classroom with fade
    play music Rain
    "So. I ended up with ever-growing hair. All things considered, that didn't sound too bad. After all, that Rapunzel character dealt with it just fine, and unlike her, I'll actually have access to scissors and razors."
    "I scratched my chin, wondering if it'd apply to facial hair as well. That would be a bit more troublesome to deal with, but still manageable."
    "At the worst, it just meant that a few days without a trim would have me looking like an old wizard, which was kind of cool..."
    "As I entered homeroom, it was obvious that everyone was talking about their discoveries already."
    "It was just much louder than it typically was. Tones ranged from excitement and pride to confusion and sadness. Well, that's what the school was for, I suppose."
    "To give everyone here a place to discuss their bodies in a safe environment. Still, it made me wonder if my trait was common or an oddity. I guess there was plenty of time to find out."
    show BE happy at center with dissolve
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
    extend "Really? That's it? Huh, I was hoping for something a little stranger. Is that why you've always got your bangs covering your eyes then?"
    MC "I guess so? I've never really noticed it before if that's the case. I mean, I suppose I might have gotten haircuts a bit more often but it wasn't really something I paid much attention to."
    show BE neutral
    BE "That's fair. Me on the other hand, I've known what I was going to be growing for a while now."
    "To emphasize her point, Honoka slumped forward and let her sizable bust sit on the desk for extra comfort. It was hard not to stare, but then again she was practically begging me to look."
    MC "So you're going to be the official boob queen of Seichou Academy. Shall I fetch you a crown and scepter, my lady?"
    BE "Don't go throwing titles at me yet. I'm sure there's other girls in this school who are going to end up with massive breasts. It surely can't just be me, right?"
    BE "I wonder if that's a club here, now that I think about it. Clubs for each type of growth people can get?"
    MC "Eh, I wouldn't count on it. There might be people here who really are the only ones with that particular affliction. This school's all about inclusion, they wouldn't want people to feel left out because of that."
    MC "Plus, grouping everyone together might make them feel more, I don't know how else to say it, 'freakish'?"
    show BE surprised
    BE "What do you mean?"
    MC "Like, if there was a club where everyone who had a growth factor where they'd end up ridiculously obese, it would feel like they were being bunched together. Excluded from everyone else."
    MC "It wouldn't be much different from cliques back in 'regular' school, you know?"
    show BE neutral
    BE "Yeah, I guess you've got a good point."
    "Honoka smiled and straightened herself up in her chair. We both took a moment to look around the room and observe everyone else for a bit."
    "Some students were looking at their own bodies, or examining their friends. One or two were just staring down at their desks."
    BE "I guess depending on how big people get, it might not make sense to shove everyone with the same growth factor into one room, either. Otherwise, like in your case, you'd just end up with a waterfall of hair."
    BE "It'd get all tangled up and messy, knotted together. Like when rats get all matted together and gross. Bleh."
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
    "Honoka chuckled, and then went silent as our teacher walked in. The other students all began to hush after a while, ready for class to begin."
    "We'd all been in classes for several days already, but now that we all knew what was going to change about our bodies, it really sank in that this would be a new learning experience for us all."
    jump daymenu

label BE007:
    $setProgress("BE", "BE008")
    scene Classroom with fade
    play music Schoolday
    "I had to give credit where credit was due. Despite having such a long tongue, Tashi-sensei seemed to be pretty good at talking without it getting in the way."
    "It was fairly easy to understand him, and he was more than willing to repeat himself if somebody misheard."
    "That was really the only thing unusual about class. The lessons weren't that different from what I was used to back at my old school. There was just that ever-prevalent undercurrent that everyone was at this school for a very specific reason."
    "But, oddly enough, it seemed like it was already starting to fade away, bit by bit. I suspected it wouldn't be long before I wouldn't even think about it. Though, logically once my growth really kicked in, I'd be stewing on that for quite a while."
    show BE neutral at center with dissolve
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
    show BE neutral
    BE "I mean if you had reservations at some other cafeteria, I would understand."
    MC "No no, only the finest school lunch will do for me. Let's go."
    "I stood up from my desk and followed Honoka down to the cafeteria, spending the walk deciding on what I would get that day. Yesterday I had seen they had some pretty good-looking soba noodles, so that might be a good choice."
    scene Cafeteria with fade
    "Once we got to the cafeteria, we both stopped right inside the entranceway, peering at the tables to look for a good spot."
    show BE neutral at center with dissolve
    MC "See any open seats?"
    BE "Yeah, right there."
    "Honoka pointed out two seat opposite of each other."
    MC "Cool. All right, let's grab our food and hope they're still there when we get back."
    "It wasn't like the seats were packed to the brim like a baseball stadium, but my head was still remembering moments from my last school where all the good seats would be taken in the first three minutes of the lunch bell ringing."
    "Honoka and I walked to the lunch line and grabbed our food, and got back to our seats after a few minutes, leaving us plenty of time to chat."
    MC "So."
    BE "Ba."
    MC "Wait, what?"
    show BE happy
    BE "Soba. How are the soba noodles?"
    MC "Oh! Heh, pretty good actually. What did you get?"
    show BE neutral
    BE "Just some fried chicken and rice. Tasty stuff, they've got some good chefs back there."
    MC "Well I sure hope so. I would think that since everyone here is going to be doing some big growing, they'd need to know how to feed some big students."
    show BE happy
    BE "Makes me think of how many times my mom would throw out that phrase 'Eat, you're a growing girl!' She didn't know how right she was."
    MC "And you're not even the biggest."
    "Honoka and I both turned our gazes to look over at Alice, who, despite evidence to the contrary, didn't appear to have that much food on her plate."
    show BE neutral
    BE "I wonder... I haven't asked her yet. But, I wonder what is actually going to grow on her."
    MC "What do you mean?"
    BE "Like, you're going to get longer hair, I'm going to get bigger boobs. Is Alice just going to get a bigger stomach, or is it an all-over deal?"
    menu:
        "I actually know the answer to that." if getAffection("BBW") >= 3:
            jump BE007_c1
        "I actually know the answer to that. (disabled)" if getAffection("BBW") < 3:
            pass
        "I'm not really sure.":
            jump BE007_c2
        "Maybe it's just hidden under all that weight.":
            jump BE007_c3

label BE007_c1:
    MC "I actually know the answer to that."
    show BE surprised
    play music BBW
    BE "Oh?"
    MC "Yeah, I've talked to Alice a couple of times. I don't want to give out too much if she hasn't said anything herself, but, it's more the second option."
    MC "She's not going to end up with a big gut. I mean, well, that'll be part of it naturally, but it's not the focus."
    MC "She's basically going to get extremely overweight. Thankfully she's not going to end up with the negative effects of that."
    show BE happy
    BE "Oh, well that's good. Nothing fun about heart disease."
    MC "No, definitely not."
    show BE aroused
    BE "So, you've chatted Alice up a couple of times then? I didn't know you were into big girls, Kei-chan. Not 'that' kind of big, anyway."
    MC "Huh? Oh, heh, Honoka. It wasn't like that. I was just being nice. She may have come off as a little pompous when we first met her, but she didn't seem 'mean', exactly. I figured it wouldn't hurt to get to know her better."
    show BE neutral
    BE "Of course. I should have known. That's just like you, Kei-chan. But, be careful, or you're going to end up being responsible."
    MC "Responsible for what?"
    show BE happy
    BE "My weight of course! Stick around with Alice too much and I might be compelled to put on some kilos to keep your attention on me."
    play music Schoolday
    jump BE007_after

label BE007_c2:
    MC "I'm not really sure. I don't think it would be good to go right up and ask her about it, but, I would think it's probably something to do with fat cells in the body. So, maybe it's going to be like she is now, just scaled up."
    show BE neutral
    BE "I guess that makes sense. Do fat cells get bigger or do they just multiply? Wait, I guess if it's a cell it can't really be a different size, can it?"
    MC "That's... a question for someone smarter than me. All I know is, it's got to be something with her body."
    MC "She's definitely got a good appetite, but it doesn't seem like she's eating anything too bad. It's not like her tray is loaded up with pizza and snack cakes."
    show BE happy
    BE "Oh, why did you have to bring up snack cakes? Now you've got me thinking of them. This is all your fault. Now what am I going to do?"
    jump BE007_after

label BE007_c3:
    MC "Maybe it's just hidden under all that weight."
    $setAffection("BE", -1)
    show BE sad
    BE "Uh, what do you mean?"
    MC "Maybe her being fat isn't actually related to her growth, it's just coincidental that she eats so much."
    show BE neutral
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
    show BE sad at center, Transform(xzoom=-1)
    BE "Oh, man, those things were good. But now I can't look at them without getting queasy."
    MC "You know they make chocolate cream-filled ones, now."
    show BE happy at center, Transform(xzoom=1)
    BE "They do?! Oh my god I want ninety."
    MC "What happened to looking at them and feeling queasy?"
    BE "Yes, but that was before you mentioned chocolate, and chocolate overrides every other human emotion. Fear, disgust, anger. All fall to chocolate."
    MC "So, you're saying that when White Day rolls around, all you need is some of those cakes and you'll be good to go."
    show BE neutral
    BE "It doesn't even need to be White Day really."
    MC "So, if I were to point out that they had some of those chocolate cream-filled cakes in the vending machine over there, and went to get two, you'd like one?"
    show BE happy
    BE "Are you kidding? Two might not be enough, I'll make the trip myself!"
    "I chuckled as Honoka ran over to the vending machine to grab her delicious snack cakes, making a mental note to myself not to get between her and a box of them if she ever got hungry."
    jump daymenu

label BE008:
    $setProgress("BE", "BE009")
    scene Dorm Interior with fade
    play music Hallway
    "It was another hot day outside the campus. Too hot for me to bear going outside for any reason that didn't involve diving into a pool of ice cold water."
    "Instead I figured I'd spend the day in my room, catching up on updates of some weekly manga I'd lost track of."
    "I had barely gotten started when the door knocked. Daichi was out, so I figured he'd simply forgotten his key."
    MC "Hey, what's up?"
    show BE happy at center with dissolve
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
    "Without even waiting, she looked at what I'd been reading."
    show BE happy
    BE "Oh neat I haven't seen this one yet. The main character in this is so cool, isn't he?"
    MC "Oh you read this one too?"
    BE "I only recently got into it, but the action's nice. It just stinks the chapters are always so short. But it's got some good characters in it too, doesn't it?"
    MC "Heh, yeah, it does. I just finished this one actually, keep reading, it gets really good in a second."
    "Honoka nodded and scanned along the pages. I waited for the moment I had been surprised by, and saw her hit that point where her eyes opened up wide."
    show BE surprised
    BE "Whoa! Holy cow, I did {i}not{/i} expect that. I thought Tomoko died like, gosh, chapter 20? How did she survive that attack she took?"
    MC "I have no clue, but I'm guessing it has to do with how she was so powerful, strong enough to take down that robot in one punch. Maybe she became a cyborg or something."
    show BE neutral
    BE "Maybe. Though, I'd hope if they turned her into a cyborg they did more than just make her more powerful."
    MC "What do you mean?"
    show BE happy
    BE "You know. Like, it's no fun to just {i}be{/i} a cyborg if you don't look like one too."
    BE "You need a cybernetic eye or some wacky hair color, some crazy speech patterns or a constant whirring sound. Make people know you're half-machine, half-badass, all-woman."
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
    MC "I have to be thorough now, I need to make sure there's not any robotic parts hiding under there. Daichi would be distraught as hell if he knew I brought a cyborg enemy into this place without his approval!"
    "Laughing like a mad scientist, I kept poking Honoka in whatever places I could reach. Eventually I managed to reach her waist, which made her squirm and giggle as she recoiled from the contact."
    MC "Aha, it appears I've found a weakness here. I must examine further!"
    "Spurred on by her reaction, I couldn't help but keep poking her belly wherever I could reach, though by this point it was essentially tickling rather than just poking. It didn't take long to get Honoka stuck in a cycle of laughter."
    show BE happy:
        linear 0.1 xpos 0.48
        linear 0.1 xpos 0.52
        repeat
    BE "Ahaha, K-Kei-chan, hahaha, stop! Ah! Hahaha, oh, not there, ah! Hehehe, you can't, ah! I'm t-too ticklish there, ha! K-Kei-chan!"
    "It was too late to stop now, I was a man on a mission. What that mission was, exactly, I couldn't say, but hearing her laugh like a little kid brought me back to when we used to hang out pretty much every day. "
    "Before I could be brought back too far to the memories of us as kids, I was thoroughly distracted by something that was definitely not there when we were kids."
    "Obviously, since we've spent a fair amount of time together at school already, I'd seen Honoka's breasts bouncing a lot."
    "It hadn't yet gotten to the point where I was used to it and it had lost its appeal, but normal movement had nothing on what was going on in front of me now."
    "My breath hitched in my throat as I saw her bosom heaving up and down with her giggles, the high-pitched squeals coming from her making me feel a bit light-headed."
    "I watched her mounds bounce up and down, a feast of jiggling that I had directly caused thanks to my ceaseless tickling."
    show BE happy:
        linear 0.05 xpos 0.5
    "It only ceased now because I was staring at them so hard I gave Honoka a chance to catch her breath, and slowly settle her mammaries back down."
    "Unfortunately for me, before I could try and defend myself, she went on the offensive, knocking me over and grabbing one of my feet."
    MC "Oh god, Honoka, no!"
    BE "Ahahaha, so this is still your weak spot then?! Perfect! Suffer Kei-chan, suffer the wrath of Honoka Inoue!"
    "I was a goner. How on earth did she remember that I had ticklish feet? She must have a special section in her head for saving embarrassing memories."
    "The girl was relentless, using both hands to torture me. As much as I wanted to kick at her to knock her away, I couldn't, afraid of what exactly I might hit."
    "The suffering only ended when my laughter stopped completely because I was simply unable to take a breath."
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
    BE "Oh come on. Who would you rather see in real life: Marumarucha, the awesome green-haired cyborg with visible jetpacks, or Kurasani, the lame detective who's only a cyborg when she peels off her skin?"
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
    "Honoka and I spent the rest of the afternoon together, just hanging out and catching up on manga. It was nice, something I hadn't really had a chance to do with a friend in a long time."
    "Daichi was not exactly the type of guy who would just sit and read unless it was a bunch of conspiracy theories. Honoka was much, much more fun."
    jump daymenu

label BE009:
    $setTimeFlag("size2")
    $setProgress("BE", "BE011")
    scene Track with fade
    play music Busy
    "Honoka's soccer club had a match that afternoon. It wasn't too hot, so I decided to come out and watch her for a while."
    "The bleachers weren't filled up that much, but I supposed it was so early in the year that there wasn't much interest in the game yet. Most of them were rookies, most likely, or at least shaking off the dust."
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
    "It wasn't long after I made a fool of myself that Honoka managed to snatch the ball away from the opposition in the last minutes of play and kick it into the goal."
    "She ended up falling over from the huge force she put onto getting the ball from midfield all the way past the goalie, but it did the trick."
    "After the game was won, Honoka jogged off the field, coming up to where I was sitting on the sidelines. Her gym clothes were ringed with sweat, the bottom curves of her breasts forming a crooked sweat-stain smile across her front."
    show BE happy at center with dissolve
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
    "After saying goodbye to Honoka, I stretched my legs out a bit; still sitting on the bleachers. It was so nice seeing her have fun and getting excited about something. A huge dose of normalcy in this weird school was definitely needed. "
    "I sat there for a few more moments before getting on my way, smiling as I walked back to my room."
    jump daymenu

label BE009_c2:
    MC "Dribbling balls, jiggling chest, Ho-no-ka is the best!"
    "I wasn't a poet by any means, but it was the best I could come up with on short notice. I couldn't even tell if Honoka was able to hear me, I assumed there was a lot of chatter between the soccer players that would drown out whatever I said."
    "Then again, maybe she was able to hear me. It wasn't long after I made a fool of myself that Honoka managed to snatch the ball away from the opposition in the last minutes of play and kick it into the goal."
    "She ended up falling over from the huge force she put onto getting the ball from midfield all the way past the goalie, but it did the trick."
    "The whole crowd cheered after that, including me. She definitely heard that. Honoka ended up scoring the goal with only a few more minutes on the timer."
    "It wasn't enough for the other team to score again. Meaning that for all intents and purposes, Honoka had just won the game."
    MC "Heck yeah! Go Honoka!"
    "After the timer for the game went off, both teams celebrated for a while, hoots and hollers all around. It wasn't until a lot of people had left that Honoka came over to the stands."
    show BE happy at center with dissolve
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
    "She really was good. It wasn't long after I arrived that Honoka managed to snatch the ball away from the opposition in the last minutes of play and kick it into the goal."
    "She ended up falling over from the huge force she put onto getting the ball from midfield all the way past the goalie, but it did the trick."
    "After the game was won, Honoka jogged off the field, coming up to where I was sitting on the sidelines. Her gym clothes were ringed with sweat, the bottom curves of her breasts forming a crooked sweat-stain smile across her front."
    show BE neutral at center with dissolve
    play music BE
    BE "Oh hey Kei-chan, I didn't know you were watching! How long have you been here?"
    MC "Long enough to see you're pretty good still."
    show BE happy
    BE "Heh, thanks. Let me know next time so I can show off for you."
    hide BE with dissolve
    "She gave me a wink and shook her shoulders a bit before leaving to follow the rest of the soccer club. Wondering what kind of 'showing off' she meant, but satisfied that I'd hung around long enough, I got going myself."
    jump daymenu

label BE010:
    $setSize(2)
    $setTimeFlag("aftersize2")
    scene Dorm Interior with fade
    "Once again, I found myself hanging out in my room after doing my homework for the day. I had been in desperate need of some video game time, so I wasn't doing much except resting on my bed, playing a handheld system."
    "KNOCK! KNOCK!"
    "The door to the room knocked and I went to open it, still focused on the game. Pausing during boss battles always threw off my rhythm."
    MC "Hello?"
    "I opened the door, still looking at my system the entire time. I was forced to listen to the sound of my character taking a critical hit as two large, white-clad breasts dropped into my field of view and pressed down on the screen."
    "I knew who it was without even looking up. I was grateful for the view, less grateful that I had to pause my game, but even more grateful that Honoka's boobs weren't so big and heavy that they broke my handheld."
    show BE neutral at center with dissolve
    play music Schoolday
    MC "Hi Honoka."
    show BE surprised
    BE "Oh, you recognize me?"
    "I looked up at her in confusion. She sounded oddly serious."
    "Stepping away, I took a better look at her face, somewhat worried that she'd cut her hair or something had happened to her face. Just something that would make me have trouble recognizing her. Nothing seemed out of the ordinary, though."
    MC "Of course I recognize you. Is something the matter? Why do you think I wouldn't recognize you?"
    show BE neutral
    BE "Because I'm bigger?"
    MC "Bigger?"
    "I held my hand to the top of my head, and then moved it flat towards Honoka. Seemed to be the same height difference as before..."
    show BE happy
    BE "Kei-chan, you dork. I mean, 'bigger'."
    "Her gaze made it obvious what she was referring to, but clearly Honoka wasn't sure that I got the hint."
    "To ensure I knew exactly what she was talking about, she reached down and grabbed her chest, lifting up a breast in each hand, as if she were presenting them to me."
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
    play music BE
    BE "Touch 'em."
    MC "What?"
    BE "I want you to touch them, so you have proof that they've grown significantly since you first saw them again."
    MC "You... you wha... Uh..."
    "My brain struggled to comprehend what Honoka had just offered. Her tone of voice wasn't like she was trying to be flirtatious or intentionally sexy."
    "It was more like a judo instructor demanding you try and grab their arm so they could perform a flip and toss you onto your back."
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
    hide cg
    show BE sad at center
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
    "Honoka's hands greedily reached out for a nonexistent soda. If anyone performed the same gesture at her it would have been very obvious what they were trying to grab, but Honoka's was more about soda cans, not cellulite cans."
    "I invited her in to share a drink and relax anyway. As tempting as it would have been to grab some of Honoka's chest, it didn't feel quite right. We're friends. Friends shouldn't do that. At least, that's what I thought."
    jump daymenu

label BE010_c2:
    MC "Well, if you insist."
    "At Honoka's pleading, I reached out towards her chest. It was only when my hands were an inch or so away that I realized I had no idea what I was doing. Was I supposed to just push my palms in? Or should I try and support them from the bottom?"
    MC "You know, this will be my first time doing this."
    BE "Well, then I'm honored to be your first."
    MC "Oh, please don't say it like that. It's going to make this sound way naughtier than it already is."
    show cg BE010 with dissolve
    "Seeing Honoka zip her lip, I finally crossed the threshold and pushed my hands into her chest. I don't know what sensation I expected her chest to have, but somehow it felt like everything all at once."
    "It was soft, that was for sure, it was easy to discern that from how my hands sank into their masses a good couple of inches."
    "Honoka still had a smile on her face, so I kept examining them. I felt like a doctor, medically probing her, but really all I was doing was trying to take in the feel. Soft, yes. Squishy as well."
    "I swore they made sounds like stress balls being squeezed as I applied a bit of pressure to them."
    "But, also, they were... dense. It seemed like an odd term to describe breasts, but it was accurate. For as big as they were, they still felt heavier than I expected them to."
    "I carefully moved my hands so they cupped Honoka's boobs instead, and pushed up."
    "They took a slight bit more effort to move than I thought they would, and when I finally pulled my hands away, I got to see them bounce for a few seconds before stopping."
    MC "Wow."
    hide cg with dissolve
    show BE happy at center
    BE "Heh, heh. Get yourself a good handful? How did they feel? Were they as soft as you imagined? Were they warm? Tell me!"
    MC "Whoa, um, well. They're... big?"
    show BE happy at center, Transform(xzoom=-1)
    BE "And?"
    MC "Soft?"
    show BE neutral at center, Transform(xzoom=1)
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
    BE "Ah, ah. Think back, Kei-chan. I just asked you to {i}touch{/i} them. You could have easily just poked them, and that would have sufficed. Or even just gave them a quick little grope."
    BE "But, nope. You took hold, and you didn't let go for eighteen seconds. I counted."
    show BE neutral
    BE "You know what that means?"
    MC "N-No?"
    show BE happy
    BE "Hehehe..."
    "Honoka suddenly loomed forward, her breasts inches away from my face. My knees buckled. I felt like I was suddenly talking to Shiori, not my childhood friend."
    show cg BE010
    BE "It means I know what kind of guy you are."
    MC "I... um."
    BE "A guy who takes charge and opportunity when he can."
    "Honoka pulled back and smirked at me, her smile looking like it could slide off of her face. She grabbed the handle of my door with one hand, and then turned to wink at me."
    hide cg
    show BE happy at center
    BE "And I like that kind of guy."
    hide BE with dissolve
    "With that, Honoka shut the door behind her, leaving me to wonder what just happened."
    $setAffection("BE", 1)
    jump daymenu

label BE010_c3:
    MC "..."
    "I just couldn't say anything. My mouth felt like it dried up. Something about this was wrong. I wasn't sure what her game was, but I felt like the smart thing to do was just shut up."
    hide cg
    show BE neutral at center
    stop music
    BE "Hello, Kei-chan?"
    "The only sound that managed to come out of my mouth was a weak, guttural stutter."
    show BE sad
    "Okay, Kei-chan. I get the message."
    "Honoka pulled back her balloons and wordlessly left my room, leaving me utterly confused. She only came in to show off her breasts? It just didn't make sense. Maybe she wasn't feeling well."
    "Hopefully she went off to her room to relax for a bit, it seemed like she needed it."
    $setAffection("BE", -1)
    jump daymenu

label BE011:
    $setProgress("BE", "BE012")
    scene Track with fade
    play music Busy
    "It was another gorgeous day here at Seichou Academy."
    "Though the weather as of late was beginning to edge towards the cooler side of temperatures, the sun was still bright enough, and warm enough, that many people were still hanging around outside in summer clothing."
    "I'd heard that Honoka's soccer club was having another game today, so I thought it'd be nice to pay her another visit."
    "I'd brought along a sweatshirt in case it did begin to get too cold, but if I figured out some cheers again, I'd have some reasons to move around and get the blood flowing."
    MC "Huh, wonder where Honoka is."
    "I hadn't been to enough games of soccer to recognize most of the players, but there was a certain brunette friend that wasn't visible in the masses."
    MC "Huh. I wonder if she's sick or something? Maybe I should go check on her. Maybe there's a place around here that sells chanko, a bowl of that always helps when I'm sick."
    "I soon found out that Honoka wasn't sick, because two large spheres pressed against my shoulders from above me."
    show BE happy at center with dissolve
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
    BE "It was just something I'd already done before, you know? You and I used to play all the time and I never really stopped liking it."
    BE "I just felt it was time to move onto something else. We're in this huge school after all, with dozens of clubs. Something out there's just bound to be right for me."
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
    MC "Ah okay. Fair enough. Yeah, I uh, sorry I didn't mean to imply anything. Trust me, I had a whole list of non-boob-related chants all ready for you to cheer you on."
    MC "They're all going to go to waste now! Whatever club you do next I'll have to come up with new ones."
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
    BE "Yeah. It would. But, I think I really want to stick to something athletic. It's good for exercise, you know? Plus it's always nice to get outside."
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
    $setProgress("BE", "BE014")
    scene Campus Center with fade
    play music Busy
    "It was sometimes a bit annoying to track down Honoka when I wanted to find her. She was never really the type to have a regular hangout spot."
    "With some of my other friends, I had a vague idea of where I could find them. With Honoka, she could have been in a dozen different places at least. I suppose it came with being such a free spirit."
    "Heck, if we hadn't lived next door to each other, I don't know if we'd have met enough times to be considered friends, let alone best friends."
    "It wasn't anything of vital importance I wanted to discuss with her, so it easily could wait until the next time we ran into each other."
    play sound Boing
    "Then Honoka, as she often did, literally bumped into me."
    show BE happy at center with dissolve
    BE "Kei-chan! Woo, hey! What's going on?"
    "Honoka was always a happy-go-lucky sort but she seemed extra cheerful today. That was a good sign. Maybe she'd be willing to hear me out, then."
    MC "Hi Honoka. Oh, not much, really. I was looking for you, actually."
    BE "Oh, yeah? Why didn't you just call me?"
    MC "Um, well now that you mention that, I don't think I have your phone number."
    show BE surprised
    BE "Wait, really? How on earth did I go this long without getting yours? Dummy!"
    "Honoka laughed to herself as she stuck out her tongue and playfully rapped her knuckles on the top of her head. It had the very pleasant side-effect of making her bosom jiggle."
    MC "Well here, let's fix that now..."
    "With embarrassment lurking behind our actions, Honoka and I exchanged our contact information."
    MC "Really? Your email address starts with 'beach balls'?"
    show BE happy
    BE "Hey I came up with that email when I was at the beach like six years ago!"
    MC "Uh-huh, I'm sure."
    show BE neutral
    BE "Anyway, now that you can buzz me any time, what did you want to talk about?"
    "As she put her phone away, I tried not to stare too long at that lucky cell phone that didn't even have the ability to realize it was nestled in a breast pocket."
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
    show BE neutral at center with dissolve
    BE "Yeah?"
    MC "It's that way."
    "I pointed in the opposite direction."
    BE "Oh. Heh. Okay, fixed!"
    scene Town with fade
    show BE neutral at center with dissolve
    "Now that she was headed in the right direction, I followed Honoka to the bus stop, where we were just in time to hop aboard. With a little more hop in Honoka's case. After a few stops, we ended up in a small shopping district in the city."
    MC "Now, if I remember the directions right, we just go this way, and take a right, and we should be there soon."
    show BE happy
    BE "Perfect."
    scene Arcade with fade
    "Honoka and I shared a lovely, albeit quick walk over to the arcade. Even before we stepped inside we could tell what it was, thanks to the many noises of buzzers and bells going off from pachinko machines."
    "But, Honoka and I preferred games of skill. Or at least games that were more fun than sitting at a machine, watching balls drop. So we searched out one of our old favorites."
    show BE neutral at center with dissolve
    BE "Oh, hey, check it out. I think I see a Mecha Killer Xtreme DX cabinet that's free. You want to play one match for old time's sake?"
    MC "Sure. But only if I get to be Delta Debonair."
    show BE happy
    BE "Psh, if you want to be the lamest character on the roster, go for it. Beta Beautifully is all mine."
    "I chuckled as Honoka went over to the other side of the cabinet. We slid in our tokens and each picked our characters."
    "With my hands on the controls I prepared myself for the game. I've had lots of practice with this game. I could crush Honoka if I wanted. But would that be too mean?"
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
            "While we'd played together a few times since coming to Seichou Academy, it had been years since we were able to play MKXD together, especially on a classic machine like this one."
            "I didn't want to get her upset either, so I thought it would be best to play it safe and easy."
            BE "Come on, Kei-chan, you ready to play yet?"
            MC "Yep. Sorry I'm just nervous, it's been a while since I played."
            BE "Oh is that so? Well, I'll go easy on you, then. Let's go!"
    scene black with fade
    pause 1
    scene Arcade with fade
    show BE happy at center with dissolve
    play music Tension
    "As soon as the game began, I was doomed. Before I could even move my character, Honoka had leapt across the stage, performed a 14-hit combo on me, and removed a third of my health bar in one go."
    "From her side of the cabinet, I could hear the announcer cheering her on for her devastating attacks, while he berated me on my side."
    MC "Geez, Honoka. How many, gah, times have you played this?!"
    "I had no idea what I was doing anymore. Any semblance of strategy went out the window as soon as Honoka began destroying me with such ease. My fingers ended up becoming a frenzy of button-mashing. "
    BE "Hehehe, hah, take that. Yeah. Nngh. Oh, only about ten hours a week for the last five years. Mega-Combo!"
    MC "What the heck is a Mega-Combo?!"
    "Apparently it was a cheat move designed for only Honoka to use, because that's what it felt like when she eliminated the rest of my health bar with a single attack."
    "The announcer crying out the second round only dashed my hopes instead of encouraging me that I could make a comeback."
    "I hadn't landed a single hit on Honoka the whole first round, and now she had a full special meter charged up, unbridled confidence, and a devious cackle that chilled me to the heart."
    MC "Hey uh, Honoka? You know this is just a game, right?"
    BE "Hahahaha!"
    "All the combos I'd learned playing the game. All of the special attacks. Gone. Like flames in a rainstorm. I may as well have taken my hands off of the controls for all the good it did me."
    BE "Now behold my final attack!"
    "I was too scared to even ask what that could be. My character was reduced to a pile of scrap metal in seconds."
    "Then the scrap was crushed into a cube, and the cube was fed to a robotic dog. The cinematic thankfully ended before the inevitable next step in the process."
    "I stepped out from behind the cabinet to stare at her."
    MC "..."
    play music Schoolday
    BE "So was I good?"
    MC "Good?! How the heck did you do all that? You could go professional with those skills."
    show BE sad
    BE "You know, I actually looked into that. But apparently all the pros have moved onto Mecha Killer Ultratopia Nice Fight instead, and MKUNF just isn't as good as MKXD."
    MC "Uh, why's that?"
    show BE neutral
    BE "Because there's no Beta Beautifully, duh."
    MC "I... I see."
    show BE happy
    BE "But that was fun! I hadn't played you in that in forever. Hey, you wanna rematch?"
    MC "..."
    MC "Let's uh, let's play something else next."
    scene black with fade
    "We continued playing for a little while, but it started getting late..."
    menu:
        "Stay at the arcade":
            $setFlag("BE013_unlock")
            jump daymenu
        "Leave":
            "We left the arcade together."
            jump daymenu

label BE013:
    scene Arcade with fade
    play music Busy
    "After the devastating loss I suffered at Honoka's skilled hands, I needed something simpler. Preferably something where she wouldn't destroy me. Which likely meant a game that wasn't even competitive."
    MC "Hey, do you want to try out that Citizen Wicked light gun game? It's two player co-op."
    show BE happy at center with dissolve
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
    show BE angry at center with dissolve
    BE "Grr, this stupid boss is totally crap. You wanna stop?"
    MC "Yeah, I can't get two shots on him before he hits me."
    "We both holstered our pistols and left the game as the countdown timer ticked down to zero."
    MC "So, let's see, what next? Air hockey?"
    show BE happy
    BE "Sure! Bet I'll beat your score at least three times over."
    "At this point I didn't doubt she would. But she tilted her head as we approached the table."
    BE "Oh snap, Koneko! Hey, wassup!"
    "Honoka dashed over to a darker-skinned girl and threw herself into a strong hug that squeezed the blonde tight and made it look like her spine was about to snap."
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
    BE "Mm... Kei-chan, you know anyone who would hook up with Koneko?"
    "My mind attempted to flip through a list of all the guys I knew. Unfortunately the only name that came up was Daichi."
    MC "No. Not at all. Sorry."
    Koneko "Lame. Well, whatev, I'll see what I can find. Have fun you two. Wait..."
    BE "Huh, what's up?"
    Koneko "Is this like, the guy you were talking about?"
    show BE angry
    BE "Koneko shut up! Get out of here, already, god..."
    "I couldn't help but look confused as Koneko snickered and walked away, leaving Honoka looking flustered for some reason."
    MC "Are you okay?"
    show BE surprised
    BE "Yeah I'm fine. Koneko's just a, she's..."
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
    $setProgress("BE", "BE015")
    play music Peaceful
    scene Hallway with fade
    "The day started off rather frustratingly. Mainly due to my own indecision about whether to have miso soup or oatmeal for breakfast that morning. In the end, I waffled so much over the decision that I had to settle for toast instead."
    "There was a welcoming bounce in my step soon after, as a familiar set of wobbling breasts collided into my back, while Honoka's arms wrapped around my sides."
    show BE happy at center with dissolve
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
    "I nodded and took her snack, munching on it as she let go of me so I could face her."
    "Once I did, I was immediately drawn to her cleavage. Not for normal reasons, however. Instead it was thanks to the myriad of crumbs I saw dotting the curves of her bosom."
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
    "Honoka then proceeded to reach into her cleavage and come out with a small can of fruit juice, then after popping the top open and taking a swig she handed it over."
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
    BE "Heh..."
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
    MC "No no no. Well, it's related to that. When you heard 'drink out of your breasts', did you think, like... pouring it down the cleavage?"
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
    BE "Yeah, heh. All girls' basketball team too, so there's going to be lots of bouncing around for sure. Though not from Misao. She's like a piece of cardboard, that girl..."
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
    $setProgress("BE", "BE016")
    scene Hallway with fade
    play music Schoolday
    show BE sad at center with dissolve
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
    BE "Great! Can we just do it at your room?"
    MC "Okay. Tell you what. I'll meet you there, I'll be over in a few minutes. I just want to pick something up first."
    BE "Gotcha. I'll meet you there, then. Don't be late!"
    "Honoka ran off to the dormitories as I looked at the time. I had to make a quick stop first. I had a feeling there was an easy way to help Honoka with her studying."
    scene black with fade
    "When I made my way back to my dorm room, Honoka was waiting outside."
    scene Dorm Interior with fade
    show BE happy at center with dissolve
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
    BE "We're not? But, ugh that was like... fifteen minutes of studying already."
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
    BE "That's... okay. X equals... negative B plus or minus 4A squared over 2C?"
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
    BE "That's N factorial over... um."
    "I dangled the cookie between my fingers."
    show BE neutral
    BE "N factorial over N-K... with the whole bottom factorial as well."
    MC "Awesome. Good work."
    "Despite getting two right in a row, Honoka's next question was answered incorrectly, meaning I got to enjoy another cookie myself. I wanted her to do well. These cookies had a serving size of '1 cookie'. More than five would hurt."
    "But, it definitely seemed to be working. Maybe it was just the rush of sugar helping Honoka focus, but she was definitely getting more right than she got wrong."
    "By the time she'd gotten to the end of the box, I'd wager she ate about 75%% of its contents."
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
    MC "Yeah..."
    BE "Uh-huh. We're studying again tomorrow."
    "As I chuckled, Honoka left the room. Hopefully she got a good night of sleep. I probably would be hitting the sack soon myself. But... one more cookie wouldn't hurt."
    jump daymenu

label BE016:
    $setProgress("BE", "BE017")
    scene Gym with fade
    play music Busy
    "With nothing particularly exciting to do tonight, I decided to go and check on Honoka. She told me that there was a practice for the basketball club tonight. Would be good to give her encouragement."
    "The basketball court was fairly typical, from what I remembered of my old school."
    "Everything seemed pretty standard, although the stands for people to sit seemed to be permanently out. I was used to seeing ones that could be put away during school."
    "They also were more heavily-reinforced, which explained why they were permanent fixtures. Better seating for a constantly-growing school, I figured."
    "Not everyone in the club was out on the court when I arrived. It looked like there were a dozen or so players, so with five players to a team they had enough for a full game and more."
    "I decided to sit down next to one of the other players who was sitting."
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
    "I guess I shouldn't have judged so soon. She hadn't been doing basketball very long, but she'd been playing soccer since we were kids."
    "Honoka made shots, and blocked well enough, but it didn't feel like it had the same spark I was used to seeing in her."
    play sound Whistle
    Coach "Inoue, Charanko, hit the bleachers. Kosuke, Iwata, you're up."
    "The girl I sat next to carefully stood up, and stepped down to the ground. Her sneakers looked like they were twice my size. Honoka was able to come sit next to me, and the large-foot girl didn't say a word to either of us."
    MC "Is she always like that?"
    show BE neutral at center with dissolve
    BE "Who, Sakie? Yeah she tends to be on the quiet side of things. You didn't say anything to upset her did you?"
    MC "I was pretty sure I didn't. I just asked about her wristband."
    show BE happy
    BE "Oh, that was mine. She forgot hers today."
    MC "Well, certainly was nice of you to lend her yours."
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
    MC "...Maybe."
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
    MC "Even, uh..."
    show BE angry
    BE "Yeah, even Sakie. She's just a bit of a space cadet. But, she's a killer at free throws."
    MC "I like hearing about all the people you get to meet in these clubs. One of these days I really should... do that."
    show BE happy
    BE "What, make friends?"
    MC "Join a club!"
    BE "I know, I'm just kidding. But really, I'm so awesome I count as, like, five friends."
    MC "Three tops."
    show BE neutral
    BE "Okay we'll say four and compromise. But yeah you totally need to join a club. How about this one? They've already been talking about getting Yamazaki-chan here."
    MC "Huh. Yeah, she'd be a good fit. But, I'm not sure how aggressive she could be. Seems like you need to have some force behind your actions."
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
    BE "Whoops, gotta move. Catch you later, Kei-chan!"
    MC "Wait?! What the hell are suicides?!"
    BE "Oh they're much worse but I'll be fine."
    hide BE with dissolve
    "Honoka's face faltered from her smile as she said that, but she had no choice but to get back on the court and listen to her coach."
    "I don't think the basketball club is for me."
    jump daymenu

label BE017:
    $setProgress("BE", "BE018")
    scene Arcade with fade
    play music Schoolday
    show BE happy at center with dissolve
    BE "You see, I told you that I could get a perfect score."
    MC "Yeah, you've definitely picked up some skills from basketball club, that's for sure."
    "Honoka had told me the previous day that she'd gotten much better at shooting free throws after several meetings at her club. I believed her, but she insisted on proving it."
    "Hence, the two of us arranged to get to the arcade, where they had a basketball challenge. As many free throws as she could make in sixty seconds."
    "She'd managed eighteen. Only two misses, which was an impressive score by any means. That was an A on a test, and enough to get the highest amount of tickets the game would give out."
    show BE neutral
    BE "Well, the club definitely practices a lot."
    BE "Sometimes you just stand there throwing the ball from as many spots as you can. They've got so many balls, it's ridiculous. Makes it easier, so you don't have to keep running to catch one you've thrown."
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
    BE "I dunno. Think it looks cool. All the balls clacking against each other is fun. And if Shiori gets annoying I can bring it to class one day and break it out. All that noise would drive her..."
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
    BE "Maybe. But it feels so cliché doesn't it? Why can't the guns be like, purple and orange or something. That'd be weird and different!"
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
    BE "I mean... "
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
    BE "You're sweet, Kei-chan..."
    $setAffection("BE", 1)
    "Honoka giggled, then pointed at the screen."
    show BE surprised
    BE "Oh crap, kill it!"
    jump daymenu

label BE017_c1_2:
    MC "You're not, what's wrong?"
    BE "Why do you think something's wrong with me?"
    MC "Not necessarily wrong 'with' you. You're just acting... 'off'. I can't describe it."
    "Honoka sighed and scratched the side of her cheek in worry."
    play music Bittersweet
    BE "...They keep benching me."
    MC "Huh?"
    show BE sad
    BE "The basketball club. I've been on the bench every game so far. They put me in eventually, but I've never been one of the starters. So for most of the game I just sit there. It's... boring."
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
    BE "It is, but, ugh... you just don't get it if you're not out there moving about the whole time."
    MC "I guess not. I don't get it. You're on the club, but..."
    $setAffection("BE", -1)
    show BE angry
    BE "Kei-chan, just... just leave it alone, okay? This is why I didn't want to talk about it."
    MC "Okay. Sorry."
    jump daymenu

label BE017_c2_2:
    BE "What do they think, I just want a yearbook photo or something? Why even let me on the team if they're just going to have me warming the bench?"
    show BE surprised
    BE "You think maybe the captain knows me?  The coach?  Did I do something wrong?  I pulled some pranks in high school, but nothing I think anyone would hold a grudge over..."
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
    BE "Not really. I can only assume it's because the others are just better."
    BE "Even if I've gotten good at free-throws, everything else is different. I don't know if I can't undo my soccer skills to learn new basketball ones or what, but I'm floundering."
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
    $setProgress("BE", "BE019")
    scene Dorm BE with fade
    show BE neutral at center with dissolve
    "I was hanging out in Honoka's room, playing video games with her, as had become a fairly frequent occurrence."
    "She was kicking my butt pretty handily, something that also had become a frequent occurrence. In the middle of us picking our next fighters, a knock came at her door."
    MC "I thought you said your roomie was going to be out until evening?"
    BE "That's what she said... Maybe it's someone else?"
    "Honoka stood up to open the door, and I peered over to check out who it was. Surprisingly, there stood Aida, fiddling with her fingers, but otherwise waiting patiently."
    show BE happy at Position(xpos=0.25, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    play music PRG
    BE "Oh hey! Aida-chan, what's going on?"
    PRG "Hello Inoue-san. I'm not interrupting you, am I? I was hoping to ask you something."
    BE "No, no, not at all. I was just hanging out with Kei-chan. Come on in. No point just standing in the middle of the door."
    "Aida took a step into the room, and then paused."
    MC "Hi, Kodama-san."
    show PRG surprised
    PRG "Oh! You really meant, he, ah, I didn't think Hotsure-san would be here. I didn't realize boys were allowed to be on our dorm rooms, though..."
    show BE angry
    BE "Well I guess anything's allowed as long as nobody finds out about it. But nah, it's cool. If I get in trouble for it, I'll deal with it later."
    show PRG unique
    PRG "I'm not sure if... That doesn't exactly sound like a um, a reasonable attitude to take on it."
    MC "Honestly, I'd probably be the one to get in trouble."
    show BE happy
    BE "Ah! Good point. So see, not a problem for me if he's up here."
    MC "Honoka..."
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
    show BE neutral at Position(xpos=0.45) with dissolve
    show PRG neutral at Position(xpos=0.55) with dissolve
    "Apparently I didn't as Aida leaned up into Honoka's ear and whispered something I couldn't make out. I turned away from them as well to make it easier for Aida."
    show BE unique at Position(xpos=0.25) with dissolve
    show PRG neutral at Position(xpos=0.75) with dissolve
    BE "Oh, I getcha. Heh, I guess as far as our class goes I'm the go-to girl, aren't I? Well I'll see if I can help out with this. "
    show BE happy
    BE "Come on, here, sit down."
    show PRG neutral at center with dissolve
    "Honoka sat down on her bed and ushered Aida to move next to her, which she did."
    MC "So it's okay then?"
    show PRG aroused
    PRG "I suppose so..."
    show BE neutral
    BE "Yeah. Aida-chan's just been having some bra problems lately."
    MC "Oh. And... you thought that was okay for me to hear?"
    show BE aroused
    BE "Pff, Kei-chan, does a week go by when my boobs don't become a point of conversation?"
    MC "I mean..."
    "I rattled my brain trying to decide if it really was that common before deciding, yes, that seemed likely. Honoka turned to Aida and spoke in a hushed, but audible tone."
    show BE angry
    BE "I think he actually might be getting blasé about it."
    show PRG neutral
    PRG "Oh, I see..."
    MC "I wouldn't say that. But, don't let me stop your conversation."
    show PRG sad
    PRG "Well, I've just been going through a bit of a... growth spurt lately, and my bras are getting too tight."
    show PRG unique
    PRG "I hope I'm not being presumptuous by, um, assuming you've had issues with that in the past?"
    show BE happy
    BE "Ha! Had, and continue to have."
    show BE neutral
    BE "So what's the deal then, you're not sure how to get good, new ones when you're packing more in your blouse than you're used to?"
    show PRG aroused
    PRG "Uh, um..."
    MC "Yes, Kodama-san, I'm pretty sure that's the issue and Honoka's just putting it in a dumb way."
    BE "Yeah, sounds like me."
    show PRG happy
    PRG "Well, um, yes. But to be frank, even my last set of bras weren't all that comfortable to begin with. I just wanted some advice."
    BE "Alright. I think I can help. Let me think."
    show BE happy
    BE "Hey, Kei-chan. There's a measuring tape in my desk, can you grab it?"
    MC "Yeah, one sec."
    "I looked in her drawers and found a strand of measuring tape that looked like it would work for Honoka's needs."
    MC "This good?"
    show BE neutral
    BE "Yes, yes, that's perfect."
    "Honoka started unspooling the measuring tape and cleared her throat, looking at Aida with a smile."
    BE "Okay. So, like, when it comes to bra measurements, it's not just one size, really. They're going to need two measurements. At least, a good place to get bras will."
    BE "So you can't just assume you're a certain cup size because of how big ya look."
    "I watched as Honoka whipped the measuring tape around Aida's chest so it went underneath Aida's arms. Honoka pulled the two halves of the tape together and made them meet in the middle."
    stop music
    show PRG surprised
    PRG "I-I-Inoue-san!"
    show BE happy
    BE "Now normally, you would wanna do this completely naked. I mean, not naked naked, but topless at least. Maybe it's more fun just going all-the-way, though..."
    show PRG sad
    PRG "I-Inoue-san..."
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
    PRG "N-No. But, y-you may, I just..."
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
    BE "I mean I'm certainly not one to judge. Just make sure your roommate's cool with it. I walked around topless for a while with mine here just to see how long it'd take her to say something..."
    show PRG surprised at center, Transform(xzoom=-1)
    PRG "Hotsure-san? H-Help..."
    "I vaguely heard Aida's voice but was a bit distracted. Honoka's hands were still holding onto the measuring tape, but she kept pulling and pulling on the ends, making Aida's bust bounce. Not to mention her own bosom was so close to Aida's..."
    show PRG sad at center, Transform(xzoom=1)
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
    BE "Second part is the..."
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
    BE "So, for this example rack, the difference is thirty centimeters. A new cup size is given every two and a half centimeters, give or take. So that's, let's see..."
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
        BE "30 / 2.5, or 300 / 25, which would be 3 instances of 4, so... 12 total!"
        "I blinked a few times. Honoka wasn't stupid, or particularly bad at math even. But the way she puzzled out division in her head using cup sizes was not something I expected to see."
    show BE neutral
    BE "So this example bosom would be 12 cup sizes in. That would make them an... L-cup. With their band size, that would make them an L80."
    show PRG surprised
    PRG "That sounds rather large, erm."
    show BE sad
    BE "Yeah I don't think you'd be able to grab something that big right off of a shelf. Oh, and Honoka tip, if for some reason you ever find yourself in America, they do inches there. So you'd be way smaller-sounding at least. Like, a 32L, instead."
    show BE happy
    BE "Though you'd also be in America. So your band size would probably be going up a few sizes too while you're over there, hehe."
    MC "I think everyone's would. I mean, look at Nikumaru-san..."
    show BE unique
    BE "Exactly! That's a good example of someone who might have a bigger band size than she does a bust size. Though... she's pretty stacked too, isn't she?"
    show PRG unique
    PRG "Well, I don't think I have any plans to visit America soon. But, thank you, Inoue-san. I think that will be helpful."
    show BE happy
    BE "Glad to help! And hey, having Kei-chan here wasn't too bad, was it?"
    show PRG happy
    PRG "N-No. Thank you both then."
    MC "Do you want to stick around, Kodama-san? We only have two controllers but we could swap out if you want to play."
    if getAffection("PRG") > 8:
        show PRG surprised
        PRG "Oh, um... sure! I suppose I could, if it's alright with Inoue-san. It is her room."
        show BE happy
        BE "Yeah come on, and take a load off! Plus it'll be funny to see how long it take Kei-chan to squirm when he's in a room with two beautiful ladies."
        show PRG happy
        PRG "*giggles*"
        MC "Honoka I'm right here. And I'm gonna squirm right away if you make it so obvious."
        "That got Honoka giggling as well. She then handed the controller over to Aida and began showing her the controls. I don't know if she really played games much, but it was very nice getting to play with both of them."
        "Aida didn't play for very long, about a half hour, but she seemed to have a good time before she decided it was time to leave."
        PRG "That was... that was very nice."
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
    show BE neutral at center with dissolve
    BE "Hahhh. That was nice. Glad to help her out."
    MC "I never knew you were so well-informed about bras."
    show BE angry
    BE "Hey, are you saying you haven't picked up an article or something about long hair since you got your diagnosis?"
    MC "Uh..."
    show BE happy
    BE "Haha. Kei-chan, you can be a real dork sometimes. Ooh!"
    "Honoka grabbed my measuring tape and smirked, before tossing it over my head."
    MC "Ah right, I should put this away."
    show BE neutral
    BE "Wha? Not gonna sniff it first?"
    MC "Why on earth would I do that?"
    show BE unique
    BE "Cuz maybe it's still got some of Aida-chan's scent on it. Being rubbed up against a lovely lady's bosom for that long? Might have picked up some of her trace."
    MC "Honoka, don't be weird. Besides..."
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
    "Honoka picked up her controller and proceeded to do just that, once again destroying my character 2-0."
    "After that I decided to pack up and head back to my room as well. It was getting late. I said my goodbyes, and was soon under my sheets, proceeding to doze off."
    jump daymenu

label BE018_c2_2:
    MC "I'd prefer if it was your scent on it."
    $setAffection("BE", 1)
    show BE surprised
    BE "You, wha, uh, you..."
    "Honoka had already unpaused the game, and her befuddlement at my confession was enough for me to take the lead in our last match of the night."
    scene black with fade
    "After that I decided to pack up and head back to my room as well. It was getting late. I said my goodbyes, and went to get under my sheets and doze off."
    "Though now I was wondering what my sheets would have smelled like if Honoka had been rubbing against them... Stupid brain."
    jump daymenu

label BE019:
    $setProgress("BE", "BE020")
    scene Cafeteria with fade
    play music Schoolday
    "Lunch was simple today. I just grabbed a sandwich and chips, along with some water. I didn't expect anything unusual to happen, even when Honoka sat across from me without introducing herself."
    show BE neutral at center with dissolve
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
    MC "Agh. I'm kind of remembering..."
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
    MC "Ha. Lucky. I... can't remember what I had but if we had pancakes, it was only regular."
    "Honoka's hand suddenly reached out and grasped mine, as a solemn look came to her face. "
    show BE sad
    BE "Kei-chan. That's terrible. I'm so, so sorry for your loss."
    MC "Er, I didn't get chocolate for breakfast, Honoka. It's not a big deal."
    show BE angry
    BE "I'm trying to have a nice, reminiscent moment of nostalgia, so I'll ignore that you said that."
    MC "..."
    show BE happy
    BE "Anyway! It was just so nice getting a chance to hang out with you. I think I had been feeling really down that week about the fact we were moving. I didn't want to go."
    MC "Hey, I mean... I didn't want you to go either. I was losing my best friend."
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
    BE "I think it was seeing a bit of Alien Festival 3 on TV last night. Brought up some old memories. Made me think about the good old days."
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
    BE "It doesn't matter, Kei-chan. It was you. That means... That means..."
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
        "Honoka hurriedly grabbed her trash to throw it away, and I soon followed after her, getting my own garbage to toss away as well."
        "Skip day might be pretty fun, but, I had to imagine if Matsumoto-san found out that she definitely would not approve. I guess she just wouldn't find out, in that case!"
    jump daymenu

label BE020:
    $setProgress("BE", "BE021")
    scene Campus Center with fade
    "Classes were over for the day, thankfully. Today's lessons hadn't been hard, necessarily. But they'd been mentally draining. The dining hall for dinner wouldn't open up for another hour or two, so I pondered over what I could do in the interim."
    show BE happy at center with dissolve
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
    hide BE with dissolve
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
    BE "You know, I honestly didn't check. But it's free, so..."
    MC "Fair enough. I was just wondering if this was something that needed, like, a collared shirt or they'd kick you out."
    show BE neutral
    BE "I don't think they would. But, hey, try it out. Could be fun. I'll find something nice too."
    MC "Sounds like a plan. Okay. Meet you at the bus stop then?"
    show BE happy
    BE "Yeah! Okay, I'm excited. Hehe, awesome. See you then, Kei-chan!"
    "I smiled as Honoka left."
    hide BE with dissolve
    "I'm sure I had something decent I could put on in order to look presentable. This sounded like it would be fun."
    jump BE020_c1_after

label BE020_c1_3:
    if getAffection("BE") > 10:
        MC "I'm sure Nikumaru-san would be interested."
        show BE sad
        BE "Aw. Heh. Are you worried we're hanging out too much? I like our classmates a lot too, but, well... I really wanna go with you."
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
        "Honoka nodded and headed off to her dorm to change."
        hide BE with dissolve
        "I figured I'd do the same, maybe see if I could get a shower in as well."
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
        "Honoka nodded and headed off to her dorm to change."
        hide BE with dissolve
        "I figured I'd do the same, maybe see if I could get a shower in as well."
    jump BE020_c1_after

label BE020_c1_after:
    scene School Front with fade
    stop music
    "After I got back to my dorm room, I decided on what to wear. My school uniform was already a collared shirt, so changing into another one seemed redundant, but the red one I pulled out of my closet seemed nice, and more comfortable."
    play music Rain
    "I went to the bus stop to meet Honoka after checking my homework load, and making sure it wouldn't be too much for that night after we got back. She was already waiting when I arrived."
    MC "Hey, Honoka. Have you been waiting long?"
    show BE neutral at center with dissolve
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
    "We sat together during the short trip, watching the nice atmosphere. Seichou Academy was nestled in quite a nice area. Which was probably intentional."
    "A school would have a tough time helping the self-esteem of young people with odd quirks if it was dingy."
    scene Town with fade
    "Eventually our bus stopped, and we found ourselves in the middle of a small street, with several people walking around, coming in and out of various buildings."
    MC "Alright. We're here. You said the restaurant was close?"
    show BE neutral
    BE "Yep. Should be up that block, and then around the corner."
    "Honoka pointed towards our destination and led the way."
    scene Sushi Restaurant with fade
    "The restaurant looked small, but looked very nice when we stepped inside. Once we got in, we saw only six tables, along with a small area where people could sit at stools."
    show BE neutral at center with dissolve
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
    MC "Yeah basically. Anago is more... I would say sweet, maybe?"
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
    MC "No, no, I mean... I'm pretty sure it was a myth, but I remember reading about female archers having a breast cut off to make it easier to aim a bow."
    show BE sad
    BE "Oh gross. No, I'm not doing that."
    MC "I, I know that. I mean, more in the effect that the string comes back really hard and whips you. You're big enough that it's almost guaranteed to hit you."
    BE "No... come on, Kei-chan. This is a club at a school meant for bigger guys and girls. They'd have to have safety equipment, right?"
    MC "Well yeah. They do make arm guards and chest guards."
    show BE happy
    BE "That's fine then! I'll just wear a chest guard! I'll wear two if I have to."
    MC "I don't think that will be super comfortable."
    show BE sad
    BE "I don't care, Kei-chan..."
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
    MC "I know I should..."
    "Honoka and I discussed possible clubs I could join for a bit as we munched our edamame, tossing the pods in the extra plate provided. Soon our sushi arrived. Four plates between us, two in the middle and one directly in front of each of us."
    MC "Well. Thanks for the meal!"
    show BE happy
    BE "Eat up, Kei-chan."
    "Honoka giggled, and grabbed a piece of her eel roll."
    show BE surprised
    BE "Mm! Ooh. That's good!"
    "She already had the second piece in her mouth before I had finished my first piece. Which, as I finally started chewing, realized was delicious. "
    MC "Ooh. Mm, the crunch of the shrimp really like... goes well with the soft rice."
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
    show BE aroused at Position(yalign=0.0), Transform(zoom=2.0)
    BE "Ahhh."
    "Honoka took a piece of sushi and plopped it in my mouth."
    MC "Mm..."
    "It was good. This place would have to stay on our radar."
    MC "That's nice. Thanks for sharing. Here, you want one of mine?"
    show BE happy at center, Transform(zoom=1.0)
    BE "Yes please!"
    "I smiled and grabbed my shrimp roll, and put it towards her waiting mouth. Honoka closed my eyes, which seemed a bit weird. But she still accepted the sushi piece."
    "Along with the tip of my finger as her lips wrapped around it."
    show BE surprised
    BE "Omf. Hmm..."
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
    show BE neutral at center, Transform(xzoom=-1)
    BE "Okay. I have a gift card to cover most of that."
    "Honoka reached into her pocket to grab the card, along with her wallet."
    MC "Oh, I'll cover the difference."
    show BE neutral at center, Transform(xzoom=1)
    BE "What? No, it's okay, Kei-chan. I'm the one who invited you, I should pay."
    MC "No, seriously, it's only 1,000 yen more, I can cover that."
    BE "So can I, it's fine, Kei-chan."
    menu:
        "Insist on paying the difference":
            jump BE020_c2_1
        "Allow Honoka to pay the rest":
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
    show BE happy at center, Transform(xzoom=-1)
    BE "But still."
    show BE happy at center, Transform(xzoom=1)
    BE "Having you pay for the meal at the end... I think that makes this official."
    MC "Makes what official?"
    "Honoka stood on her toes and leaned up, planting a kiss on my cheek. The warmth of her lips on the side of my face in that one moment felt hotter than the heat that had been rubbing against my side since she stood next to me."
    show BE surprised
    BE "That this is our first real date, silly."
    "Honoka giggled and got back down on her feet, holding my arm closer."
    MC "Y-yeah? I mean. We've been out on dates before."
    show BE happy
    BE "As friends. But friends don't typically feed each other like we did today. I'm not saying we have to make anything official."
    BE "But... this was a really nice time. I think the only way it could be nicer is if it was our official first date. Don't you?"
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
    BE "A bunch, I figure. But this is the first date in terms of, like... dating."
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
    MC "Er, um... maybe not 'thinking', as much as... 'hoping'?"
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

label BE021:
    scene Woods with fade
    play music Hallway
    show BE happy at center with dissolve
    $setProgress("BE", "BE022")
    MC "Honoka, why am I here again?"
    BE "Kei-chan, you still haven't decided on a club yet. You sounded like you'd be into archery. So I thought you could come and try out."
    MC "Sure, no, I get that. What I mean is. Why are we out here in the woods?"
    show BE angry
    BE "Oh. Well, that's where the club leader said we had to meet to see if we could practice. I'm not sure if this is the right place, though. This seems pretty similar to any other spot of woods."
    UNKNOWN "Negative! The trees here are in fact, made of the same type of wood that we use for our training arrows. Meaning that if you recruits find yourselves incapable of landing a hit, the wood returns to the earth, as it should!"
    "Honoka and I turned to find a male student had approached us from behind."
    "His eyes were hidden under a long-brimmed hat, but his glare was pretty obvious despite that. His ears were surprisingly large, big enough to lift up as high as the brim of his hat."
    show BE neutral
    BE "Uh, hi. So are we in the right place, then?"
    play music Tension
    UNKNOWN "Negative! You were meant to meet me fifty yards to the east. Follow me."
    "Honoka and I looked at each other in confusion."
    MC "This guy is kind of intense. Is he the head of the club?"
    show BE angry
    BE "I guess so? I thought this was supposed to be a fun club, but-"
    UNKNOWN "Negative! Archery is a very serious and dangerous endeavor. Even training arrows are capable of causing serious injury. This is no laughing matter."
    BE "This is still a club, right? You're making this sound like some sort of military operation."
    UNKNOWN "Affirmative. This is the official Seichou Archery Club. SAC."
    show BE happy
    BE "I thought the SAC was the Seichou Art Club."
    UNKNOWN "...Yes. Unfortunately, they obtained the initials first. Move on."
    MC "Honoka, I'm having second thoughts about this."
    show BE neutral
    BE "Me too. But I still want to give it a chance. So let's just push through for now."
    "The two of us followed the club leader for a minute until we came to a better clearing. At the ground were two quivers of arrows, and two bows."
    MC "So. Going to make sure we are capable of firing a bow before we get into the club?"
    UNKNOWN "Affirmative."
    MC "Fair enough. Could we at least know your name first?"
    Haruhiro "Haruhiro Haganeya. Leader of the Seichou Archery Club. I-"
    BE "Yeah, yeah, we got it."
    stop music
    Haruhiro "Hmph."
    "Haruhiro adjusted his hat over his eyes and pouted."
    MC "So, what's the official test, club leader?"
    Haruhiro "It is honestly pretty simple."
    "His tone was suddenly much more different than it had been. Honoka notably stepped back in surprise."
    Haruhiro "Sorry. I just... really like archery. Ahem. But, this is pretty serious so, uh, talking normally might be best."
    show BE happy
    BE "No no, it's appreciated! I could get used to the drill leader thing, it's just kind of off-putting right out of the gate."
    MC "Yeah same. But, um, please, show us what to do."
    "Haruhiro nodded and pointed to the quivers."
    play music Hallway
    Haruhiro "Are you both right-handed?"
    show BE neutral
    "Honoka and I both nodded. Haruhiro stepped next to one of the quivers and steadied himself."
    Haruhiro "The first step is the stance. Make sure you stand like this. You will be facing at a 90 degree angle from your target. Feet should be shoulder-width apart."
    "He moved to the side and motioned for Honoka and I to take his place. We did so and got into position."
    Haruhiro "Good, now pick up your bows and hold them in your left hand. Let the string go up, towards your armpit, then stand up again."
    BE "Do we need different bows if one of us is stronger than the other?"
    Haruhiro "Typically yes, but this is just a basic rule-following test. At the club proper we have different strengths of bows for you to use."
    "Honoka and I bent over to get our bows. They were directly under our feet. But, I noticed that Honoka had to tilt her torso to the side to peer under her chest, in order to find hers."
    MC "What's our target going to be?"
    Haruhiro "Right now just try and hit a tree. But first, nock the arrow. Pick up an arrow, and lift it up and over your head. I know it looks silly but, it's safety rules. Place it in the bow."
    "Honoka and I did as asked."
    show BE happy
    BE "Does the arrow go on the side of the bow closest to me, or away from me?"
    Haruhiro "Closer to you. Let it rest on the small protrusion on the grip. Right there."
    "Haruhiro assisted us with making sure our arrows were in place and nocked. Then guided us until we had our arrows pulled back, and took aim at trees in the distance."
    Haruhiro "Okay, now this is the crux of the part. Keisuke, you can put your arrow down for now. I'll focus on Honoka first."
    "He got up behind Honoka and watched her pull the arrow back."
    show BE neutral
    BE "Uh, how am I doing?"
    "Haruhiro went over to Honoka and attempted to adjust her stance for her. He placed one hand on her arm and tried to push them closer to her torso. The issue quickly became evident and he backed off."
    Haruhiro "No, more like... ah, hm, carry on."
    "Honoka's arms weren't entirely as flat against her torso as they should have been. I couldn't see it from my angle, but, I just assumed."
    Haruhiro "Put your elbow down more. Try and make your arms just one straight line, parallel to the ground."
    BE "Like this?"
    Haruhiro "Almost."
    "Haruhiro took her hand and adjusted it so Honoka's thumb went under her jawline."
    if getAffection("BE") > 8:
        "Seeing how close he got to Honoka was... upsetting to say the least."
    show BE happy
    BE "Okay. And I put my finger out to point where I'm aiming, right?"
    MC "NO."
    Haruhiro "Very no. Not unless you want to shoot it off. But please, don't do that. The goal of archery is to make sure there's nothing in the way of where you're aiming, except the target."
    show BE surprised
    BE "Oh. Gotcha. Lesson learned."
    Haruhiro "Okay. Nearly there. Now, you've got the fletching between your forefinger and middle finger. Now let all three fingers go at once, and don't move your hand. Keep everything still until the arrow connects."
    "Honoka took a breath as Haruhiro stood back. She let go, and a second later, a thunk sounded as an arrow landed in a distant tree."
    show BE happy
    BE "Hey! I did it!"
    Haruhiro "Well done. See, it's relatively simple. At the club you'll learn more on how to be more accurate and adjust for wind and distance. Ready to try yourself, Keisuke?"
    MC "I am."
    if getSkill("Athletics") > 5:
        jump BE021_testpass
    else:
        jump BE021_testfail

label BE021_testpass:
    Haruhiro "Okay. Your stance looks good. Draw your bow."
    "I took a breath and lifted up my bow, pulling back the arrow and locking my hand into place."
    Haruhiro "Good. Maybe lift up your elbow just a little bit."
    MC "Okay."
    Haruhiro "Yeah, this looks good. Just like I told Honoka. Let go of the arrow and string in one fluid motion, but keep your body still. If you shift at the last second it could change your trajectory."
    MC "Got it."
    stop music
    "I waited for Haruhiro to step back before letting go, aiming a little higher than Honoka had. My arrow landed in the middle of a tree trunk with a resounding thunk, embedding into the wood."
    play music Schoolday
    Haruhiro "Wonderful."
    $setAffection("BE", 1)
    show BE surprised
    BE "Holy crud! Good job, Kei-chan! That was excellent."
    MC "Oh, uh, heh. Thanks Honoka... That was just beginner's luck, I'm sure."
    show BE happy
    BE "Maybe, but look at how much further yours went! And deeper, too."
    show BE neutral
    BE "Should we go get the arrows out?"
    Haruhiro "Negative! I shall retrieve the ammunition. It is unwise for new recruits to perform this task if they are not educated in that manner."
    "Honoka and I sighed as the drill sergeant routine returned."
    MC "Oh. So are we done then?"
    Haruhiro "Affirmative! Both of you are welcome in the organization if you so wish!"
    show BE happy
    BE "I'm definitely in!"
    Haruhiro "Welcome then, Cadet Honoka!"
    MC "I'm not sure. I'll give it a think."
    Haruhiro "If you decide to join our ranks, meet us at the clubroom tomorrow at 1600 hours. You two can have the rest of your afternoon back, now! Dismissed!"
    jump BE021_after

label BE021_testfail:
    Haruhiro "Okay, widen your stance more. And make sure your feet are pointed straight ahead."
    MC "Like that?"
    Haruhiro "Yes. Okay, now pull your string back as you lift the bow, and point it towards a tree in front of you. Got it?"
    MC "Yeah. I think so."
    "I lifted the bow, and pulled the string back until my fingers were pressed against my cheek. Haruhiro took my hand and adjusted my grip."
    Haruhiro "A little further forward, basically make that bone rest between thumb and forefinger."
    MC "Damn."
    Haruhiro "It's your first time. Just a small adjustment. You should be good now."
    MC "Okay. Let go and don't move, right?"
    Haruhiro "Whenever you're ready. Try and breathe out when you release, it'll keep your body steady."
    MC "Let's do this."
    stop music
    "I released my breath and let go of the string. The arrow went sailing for a few seconds before it landed at an angle in the dirt, several meters away."
    MC "Crud..."
    "I let out a sigh, then dropped the bow to the ground."
    MC "I guess I'm not in the club then, am I?"
    play music Schoolday
    Haruhiro "Negative! Both of you are still welcome to join the organization if you deem yourselves fit!"
    MC "Huh? But I missed the shot."
    Haruhiro "Affirmative! However, the point of this examination was to make sure you followed instructions and shot an arrow correctly without goofing off. There'll be plenty of time to fix your aim during actual club proceedings."
    show BE surprised
    BE "Oh, that's great then. We can both be in the club, Kei-chan."
    MC "Oh. Great. I really thought I screwed that up. What did I do wrong?"
    Haruhiro "There are indeed, many possible reasons, but none that would be due to your form! A breeze could have caught you off guard or you weren't aimed at the right spot. But you aimed properly. That's the point."
    MC "Well, that's better?"
    show BE happy
    BE "See, Kei-chan. I think that's worth it to come here, isn't it?"
    MC "Yeah. Pretty neat, but I'm not totally sure if I want to join."
    Haruhiro "Very well! Either way, both of you are welcome to come to tomorrow's meeting if you want. Arrive at 1400 hours on the dot! You can do as you want the rest of the day, I shall remove the traces of our training. Dismissed!"
    jump BE021_after

label BE021_after:
    show BE happy
    BE "Thanks, Haruhiro! I'll see you at the club then!"
    "Honoka and I started walking back towards campus."
    show BE neutral
    BE "So, what do you think. Want to join me in the archery club? It was easier than it looked, wasn't it?"
    MC "Yeah. It was. It might be neat. I just hope he doesn't go all super-serious on us, again."
    BE "Aw, I thought it was funny. For a bit at least. "
    MC "Maybe. I'm just not entirely sure I'm a club person. I like hanging out in my room or just spending time with you."
    show BE unique
    BE "Well duh, you can spend time together with us in the club, silly."
    MC "Of course we can. But it's not quite the same if we're doing work there."
    show BE happy
    BE "I'm gonna be in the club either way, Kei-chan. You won't be able to spend that time with me if you're not in the club!"
    MC "That's a... good point."
    BE "Well, hehe. Think about it. Would be fun to spend some club time with you where you're not just watching me!"
    MC "Okay. I'll sleep on it, then."
    show BE neutral
    BE "Cool."
    show BE surprised
    BE "So, hey... you think Haruhiro like... part-elf or something?"
    Haruhiro "I HEARD THAT."
    "Honoka and I turned around. Haruhiro was still back at the training area, we'd walked a significant amount since then."
    show BE sad
    BE "Okay. Um. Now I don't want to be at the club, tomorrow."
    MC "You... may want to bring him something to apologize."
    show BE neutral
    BE "I'll make a second trip to the vending machine beforehand."
    "I put my arm on Honoka's shoulder and smiled."
    MC "You'll be fine. I'm gonna head back home and take a shower. You good?"
    show BE happy
    BE "Yeah, I'll do the same. Okay, see you later then, Kei-chan. Thanks for coming!"
    "Honoka snuck forward and planted a kiss on my cheek before skipping off, leaving me snickering as I changed direction to get back to my room."
    jump daymenu

label BE022:
    scene Cafeteria with fade
    play music Peaceful
    $setProgress("BE", "BE023")
    "After the last school lunch bell rang for the day, I walked down to the cafeteria, to look for a snack. There were a wide variety of quick eats to grab and I was feeling pretty peckish."
    show BE happy at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show BBW neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BE "Oh, hey, Kei-chan. Come over here!"
    "Near the vending machine section of the cafeteria, Honoka was seated at a table with Alice across from her. The table looked quite cluttered, and caught my attention."
    MC "Yeah, sure."
    "I took a seat next to Honoka and looked at Alice's spread."
    MC "Hey, Honoka. What's going on?"
    BE "I'm helping Alice-chan do some sort of experiment."
    BBW "'Assessment' would be a more accurate way of phrasing it."
    BBW "I realize that vending machines are a valid alternative to the regular lunch line, but surely not every item in them is worth the space or cost."
    if isEventCleared("PRG002"):
        BBW "If I recall, Hotsure-san, you're aware that Kodama-san brings me snacks. I've been taking notes on what I eat."
    show BBW happy
    BBW "For a possible future project, I'm asking Inoue-san to test a variety of snacks from the machine, to see which have merit."
    BE "I'm the sampler!"
    show BBW neutral
    BBW "A third opinion would be helpful here. Hotsure-san, would you care to assist as well?"
    BBW "I do not intend to eat all of these myself. Especially not if they are below par. I can portion them out and you are welcome to whatever you like."
    MC "I don't know. It's not exactly a healthy meal, is it?"
    BE "It means we get dinner for free, Kei-chan."
    MC "I'm in."
    "Alice's setup was quite in-depth. Just at a glance, I saw twenty or so snacks laid out before Alice. Cakes, candy bars, and chips of various kinds laid before her."
    show BBW happy
    BBW "Now, here..."
    "Alice pulled out two extra pencils, and ripped two pieces of paper off of her notepad, then handed them over."
    BBW "I simply want your opinion on this. I'll be regarding it in more detail."
    BBW "But I simply want a rank of 1 to 3. 1 for you would not eat this normally. 2 for you would eat it willingly if offered, or free. 3 for you would pay money to eat it. Understood?"
    BE "Oh yeah, got it. This'll be fun!"
    MC "Sure, I understand. Just our personal preference?"
    show BBW neutral
    BBW "Exactly."
    show BBW happy
    BBW "Let's start with this pastry. This one intrigues me; chocolate and raspberry filling in the middle is not a common vending product."
    BE "Ooh it sure isn't. Gimme."
    "Alice swiftly took a knife and sliced the pastry into three sections, taking one for herself and handing the other two to me and Honoka."
    show BBW neutral
    BBW "Hmm..."
    "Alice took a bite of her pastry and closed her eyes, holding the rest of the section in her hand as she chewed."
    "Honoka on the other hand, had already consumed her chunk of pastry."
    BE "Mm. That's good. I didn't have a lot of filling in mine, though."
    MC "Me either, but the bit I had was good."
    "Honoka and I looked at Alice's piece and saw the slightly-red chocolate oozed from the center. Poor distribution of chocolate, clearly."
    show BBW happy
    BBW "The filling is surprisingly creamy, and doesn't affect the interior of the pastry to the extent that it becomes gummy. The outside is fairly crisp but I don't believe that's due to any stale state of the pastry..."
    MC "I think I'd give that a 2..."
    "I scribbled down my note as Honoka did the same. Alice took another bite to further mull over her decision. Her eyes were still closed."
    "Out of the corner of my eye I noticed Honoka snicker as she grabbed a candy bar from the far end of the pile. She quickly snuck it into her cleavage, making sure to place it so deep that there was no trace."
    "She placed her index finger up to her mouth as she looked at me, and winked. I rolled my eyes as Alice finished her bite, and wiped her mouth with a napkin."
    show BBW neutral
    BBW "Next, these crisps."
    "Again, Alice parsed out a bag of chips between the three of us. Honoka scarfed hers down fairly quickly while I took my time. As did Alice."
    show BE neutral
    BE "Hm, yeah. These crisps are really... crispy."
    "As Honoka spoke, she once again reached down the table and grabbed one of Alice's chosen products, stuffing it down her shirt. I had no idea what her plan was."
    BBW "Hm. A delicate texture but it might be over-encumbered with too much seasoning, which overpowers the potato flavor."
    "Alice went through the rest of the items on her list, writing down her long notes while Honoka and I went through our numerical scores. Every once in a while, Honoka continued to add another item to the growing collection of food in her cleavage."
    "I was surprised how much she had inside, and that Alice hadn't noticed yet."
    BBW "Now we'll move on to..."
    show BBW sad at Transform(xzoom=-1)
    BBW "Wait."
    show BBW angry at Transform(xzoom=1)
    BBW "Where... are the fruit gums?"
    show BE happy
    BE "Hm?"
    BBW "The fruit gums. A small pack of gummy candies in a selection of flavors. It was next on the list. I had them in the set, and they are not here."
    show BE surprised
    BE "Oh no. Are you sure you actually got them?"
    BBW "I'm positive."
    show BBW neutral at Transform(xzoom=-1)
    BBW "Well, we'll move on to the pocky until the fruit gums decide to make themselves present..."
    show BBW neutral at Transform(xzoom=1)
    BBW "..."
    show BBW angry
    BBW "These are missing as well."
    "I cast a look at Honoka, who continued to play coy."
    MC "Well, we've already done a lot. I think we're okay for now, right?"
    show BBW neutral
    BBW "Not at all. The entire point of this was to purchase them all at once, to judge the freshness when removed from the machine. This invalidates their future judging if I can't locate them."
    MC "It's okay, Alice, I'm sure they're here."
    show BBW angry
    BBW "They clearly are not."
    BE "Yeah! Where else could they be, Kei-chan? They just vanished!"
    menu:
        "You've been hiding them in your cleavage, Honoka.":
            jump BE022_c1_1
        "I don't know, we'll just have to help with this experiment again later?":
            jump BE022_c1_2
        "(Convince Honoka to come clean)" if getAffection("BE") > 6 and getAffection("BBW") > 6:
            jump BE022_c1_3
        "(Convince Honoka to come clean) (disabled)" if getAffection("BE") <= 6 or getAffection("BBW") <=6:
            pass
        "(Say nothing)":
            jump BE022_c1_4

label BE022_c1_1:
    MC "You've been hiding them in your cleavage, Honoka."
    show BE surprised
    BE "Wh-What? Nooooo I haven't."
    show BBW angry
    BBW "Inoue-san, if this is indeed true, release them immediately."
    show BE neutral
    BE "I don't know what you're talking about!"
    show BE angry
    BE "I'm innocent I tell ya!"
    show BE unique
    BE "There's nothing in here at all!"
    "Honoka squeezed her boobs a little too firmly, and the sound of crumbling cookies followed."
    show BE neutral
    BE "Uh... oops."
    "Alice rubbed the bridge of her nose with her fingers."
    $setAffection("BBW", 1)
    BBW "Inoue-san, if you would be so kind as to remove all those items immediately, we can conclude this test. Those cookies first, please."
    show BE sad
    BE "Eh-heh..."
    "Honoka blushed as she pulled treat after treat out of her bosom. The cookies first, which Alice quickly snatched and examined."
    "Despite their location moments ago, she found three cookies in the bag that weren't broken and handed them out. She refused to let Honoka's shenanigans deter her."
    BBW "I can only hope the quality of these have not been diminished due to your... boobery, Inoue-san."
    show BE angry
    BE "Hey, if anything, that would make them taste better! Right, Kei-chan?"
    MC "It's not like you touched the cookies, Honoka. But, crushed cookies are... less good than un-crushed cookies."
    show BE surprised
    BE "Gasp! Oh Kei-chan!"
    show BE sad
    BE "To think you'd prefer a cookie held in a warm, soft hand, than in my heaving, full breast!"
    show BBW neutral
    BBW "Inoue-san. Please end your nonsense."
    "Alice pat down her lips with a napkin."
    BBW "And please remove the rest of the snacks. "
    show BE surprised
    BE "That was all of them!"
    BBW "..."
    MC "..."
    show BE neutral
    BE "..."
    show BE unique
    BE "Okay, yeah, here."
    "Honoka reached back into her cleavage and pulled out a bottle of soda, then placed it on the table."
    show BBW surprised
    BBW "That... was not part of my selection, Inoue-san."
    show BE surprised
    BE "Oh, right."
    show BE happy at Transform(xzoom=-1)
    BE "I had that from earlier."
    show BE happy at Transform(xzoom=1)
    BE "Sorry. That's all of it, then."
    show BBW happy
    BBW "Well. Then. We can finish this test. If you are free of any further urges to distract us."
    show BE sad
    BE "I aaaam..."
    BBW "Good!"
    "Alice took a deep breath and resumed portioning out the snacks. Honoka continued eating her snacks for a while, judging them accordingly. It wasn't until we neared the end that Alice asked the question that deserved to be asked."
    show BBW neutral
    BBW "May I ask why you thought it necessary to hide some of the snacks?"
    BE "Um. Honestly, I thought if we got to do this again, it would just be fun. I don't spend that much time with you!"
    show BBW surprised
    BBW "You, huh?"
    show BE happy
    BE "Mm-hm. I mean, the free snacks are nice, for sure. But, hey, it's something fun to do with one of my classmates. And Kei-chan too. I like that. Don't you?"
    show BBW neutral
    BBW "Oh. Well."
    show BBW happy
    BBW "I thought I had mentioned there would be more experiments like this. There are more treats in those vending machines, after all."
    show BE neutral
    BE "Oh! You mean..."
    show BBW happy
    BBW "Yes, Inoue-san, I was planning on calling you forward to do more of this. It would help to have the same palette each time."
    show BE happy
    BE "Well gosh, I guess I should have paid better attention, then!"
    MC "Yeah, you probably should have."
    BE "Oh, hush, Kei-chan. Chocolate makes it hard to focus."
    MC "Still. As... entertaining as it is. Maybe don't hide other people's things in your boobs."
    show BE neutral
    BE "Gah, it's so tempting, though."
    show BBW neutral
    "Alice and I sighed."
    show BBW happy
    BBW "I suppose now that we're finished I should look at your scores. I... Inoue-san, did you give everything a 3?"
    show BE happy
    BE "Yeah. It was all so good."
    "Alice suddenly leaned forward and slumped her head into her hands."
    show BBW sad
    BBW "There may have been a flaw in my thinking process."
    MC "Er, you still have mine."
    show BBW neutral
    BBW "Yes. Thank you for that, Hotsure-san. It's very much appreciated. I'll put this to good use."
    show BE happy
    BE "And my results too, right?"
    "I saw Alice physically struggle with how to answer her."
    MC "Yep, yours too, Honoka. Nice work. "
    MC "But you lose points for hiding stuff in your cleavage."
    show BE sad
    BE "Dang it."
    BBW "Thank you, Hotsure-san."
    show BE happy
    BE "Yeah, thanks, Kei-chan, food is always better with more people."
    BE "Here, Kei-chan and I will help clean up."
    show BBW happy
    BBW "Thank you. I'll just peruse your scores a bit more."
    hide BBW with dissolve
    hide BE with dissolve
    "Honoka and I grabbed the bevy of wrappers and brought them over to the bins to toss them out. As we left the cafeteria, Honoka nudged my ribs with her elbow."
    MC "Ow."
    show BE sad at center with dissolve
    BE "Kei-chan, why'd you sell me out like that?"
    MC "I, I wasn't trying to do that. I just wanted Alice's experiment to work and it wasn't gonna work right if you were hiding stuff."
    show BE neutral
    BE "I guess. Hm. You think Alice is mad at me?"
    MC "She seemed to be fine by the end. I think you just struck a nerve."
    show BE happy
    BE "Good. Didn't mean to upset her."
    MC "I know. Just... gotta think more carefully next time."
    show BE neutral
    BE "Right. Right. Anyway. I'm full of snacks so I'm gonna go lay down! I'll talk to you later, Kei-chan."
    MC "Heh, okay, Honoka. Talk later."
    jump daymenu

label BE022_c1_2:
    MC "I don't know, we'll just have to help with this experiment again later?"
    show BBW angry
    BBW "No no no. That won't do. If you're judging things, they have to be on equal terms."
    show BE neutral
    $setAffection("BE", 1)
    BE "Does that really work with vending machine goods? I don't think everything in there was packaged on the same day."
    show BBW surprised
    BBW "Why... had I not thought of that?"
    show BE happy
    BE "I mean, with how many students we have here, it's possible they're restocked pretty regularly."
    MC "Honoka has a good point. I've seen some sections of the machine that go empty pretty regularly, because they're pretty popular."
    BE "Right! But some of that seems to sit there for ages. I've seen a vending machine once where, no kidding, twenty of the slots were for diet cola. What's the point! If you're on a diet you're not getting crap from a vending machine."
    show BBW neutral
    BBW "You make some fair points. But then, what else could I do in this situation?"
    MC "The idea is to see what we'd rank each snack, right?"
    BBW "That's correct."
    MC "Then, maybe the best thing to do would be, something where we try them from a convenience store, or supermarket. A vending machine doesn't guarantee as much freshness."
    BBW "But my idea behind this is, what are your thoughts on the product as they're presented in the vending machine."
    show BE neutral
    BE "Hm. Well, if your plan is to like, have your own vending machine in the future, then wouldn't you make sure it was stocked full of items everyone liked?"
    show BBW happy
    BBW "Of course."
    show BE happy
    BE "Then, you wouldn't need to worry about freshness. Ideally, it would be getting stocked so often that the turnaround time is really low."
    show BBW happy
    BBW "A large amount of stock would be beneficial, then. It would be good to maybe limit the machine to the most popular snacks out there, and then work from there to stock multiples of each."
    BE "Like how there's usually a few for sodas, because those go quickly. But even more for water."
    show BBW neutral
    BBW "Precisely. This is a better way of thinking. Hm."
    show BBW happy
    BBW "Thank you. This might be helpful. I suppose, even with that said, there's still these to test out, and there's no sense letting them go to waste. Shall we finish?"
    BE "Yes, please!"
    MC "I'm game."
    "As Alice portioned out the snacks that Honoka hadn't stuffed away, I looked to Honoka to see if she was going to come clean. She just snatched the first bit of food placed in front of her. So, the answer was, 'no she wasn't'."
    "After we'd eaten what we could, Alice collected our scores."
    BBW "Once again, thank you for this information. It may change how I value your scores, but it's important to have feedback like this either way."
    MC "Well, we're happy to help. Do call us over again if you need more help."
    BE "Absolutely. This was fun. I never knew you had such a refined palate, Alice-chan."
    show BBW neutral
    BBW "Oh, I don't think it's all that impressive."
    show BE surprised
    BE "It totally is! I never heard potato chips described in such a beautiful way before."
    show BBW aroused
    BBW "Oh... thank you."
    show BE happy
    BE "Hehe, you're welcome. Yes, please let me know if you need me to eat more food. I'll do it."
    show BBW happy
    BBW "I'm sure you will."
    MC "Here, I'll help take care of all this."
    "I gestured to the wrappers and empty containers."
    show BBW neutral
    BBW "Thank you, Hotsure-san. I shall see you in class tomorrow, then?"
    MC "Yeah. Have a good night."
    hide BBW with dissolve
    hide BE with dissolve
    "I nudged Honoka to have her help me grab the food wrappers and we brought them over to the trash cans."
    MC "So, what was the deal with hiding her food?"
    show BE neutral at center with dissolve
    BE "Honestly I did it for a laugh. But, then I had an idea about the reasoning for her doing this and it felt off all of a sudden."
    BE "I would have shown her if she got really mad, but, she kind of forgot about it when we brought up a better way to do the test."
    MC "I guess she did. Still, what are you going to do with that now?"
    "Honoka fished in her cleavage, and looked up at the ceiling."
    show BE happy
    BE "Second dinner, by the feel of it."
    "I sighed."
    MC "Well, you enjoy that, Honoka. I'm gonna head back to my room. I'll see you at class tomorrow, okay?"
    show BE neutral
    BE "Sounds good, see you later, Kei-chan!"
    hide BE with dissolve
    "Honoka dashed off, holding an arm under her chest to make sure her bounty didn't escape, as I left to my room."
    jump daymenu

label BE022_c1_3:
    "I turned to Honoka and lowered my voice."
    MC "Honoka, come on, fess up."
    "Honoka whispered back to me."
    show BE neutral
    BE "What? Come on, this is funny."
    "I stared at her, and when she didn't get the message, flicked the side of her thigh."
    show BE sad
    BE "Ow. Okay..."
    show BE neutral
    BE "Ahem. Um, sorry, Alice-chan."
    "Honoka reached into her breast pocket and slowly pulled the snacks out, placing them on the table in front of Alice."
    show BBW neutral
    BBW "Inoue-san, I'm going to assume you had a reason for doing this?"
    BE "Partly just to see if I could, honestly?"
    BBW "And the other reason would be?"
    BE "Well, I guess to eat them later."
    show BBW sad
    BBW "But the point of this test is to eat them now."
    BE "Right, but, I guess I don't understand that?"
    show BBW angry
    BBW "How could you say that now when I explained it earlier?"
    MC "H-Hold on a second. Honoka, what's the problem with this?"
    BE "Vending machines aren't really thought of as 'fresh' to begin with. If it's stale, that's a problem for sure. But it's not like steak. A candy bar doesn't taste different on a day to day basis."
    MC "Alice, does that make sense?"
    show BBW neutral
    BBW "I suppose it does. But if you had an issue with my setup you could have simply explained it to me, rather than try to scurry food away and assume I would change my idea."
    MC "That's fair. Honoka, you understand that it was a mistake to do that?"
    show BE happy
    BE "I do. I'm sorry, Alice-chan. I didn't think that it would upset you that much but, that was still stupid."
    BBW "I appreciate and accept your apology, Inoue-san. Is this all of the snacks we had left to test?"
    BE "It is!"
    show BBW happy
    BBW "Well then, I shall clearly need to re-evaluate what I had planned. But if you had more ideas, I'd like to hear them. We can continue this as well."
    show BE neutral
    BE "I am still hungry."
    MC "I am too. Glad to see this didn't get into an argument."
    $setAffection("BBW", 2)
    show BBW neutral
    BBW "You should know me better, Hotsure-san. I'm a rational person."
    $setAffection("BE", 1)
    show BE surprised
    BE "And arguments are stupid anyway. We can just eat our problems away!"
    MC "Not what I would have said, but I suppose that's a fair point."
    show BBW happy
    BBW "I'll admit, I do not tend to go for these kind of snacks. But in good company, they're much more enjoyable."
    show BE happy
    BE "Exactly. It's like, if everyone always had to eat together with someone, everybody would be friends with everybody else."
    BBW "Er, I can't say I necessarily understand that sentiment, but it's a nice one all the same."
    BE "Oh my gosh, hey, Alice-chan. Have you ever fed someone?"
    show BBW neutral
    BBW "I'm feeding you right now, aren't I?"
    show BE neutral
    BE "No no, I meant, like, feeding someone hand-to-mouth."
    BBW "No. Why would I have done that before?"
    show BE surprised
    BE "What?! You've gotta try, it's so great. It feels fantastic. Watch."
    "Honoka grabbed my shoulder and flipped me towards her."
    show BE happy
    BE "Open wide, Kei-chan!"
    MC "Hono-mph!"
    show BBW surprised
    "Before I could respond, Honoka grabbed one of her fruit snacks and fed it to me, keeping her finger on my mouth until I swallowed."
    MC "U-um, thanks."
    BE "See! It's so fun!"
    BBW "I... see."
    show BBW neutral
    BBW "May I try it as well?"
    BE "Go for it."
    show BBW aroused
    BBW "A-Ahem, Hotsure-san, if you wouldn't mind... "
    "Honoka's eyebrows raised as she looked at me, and turned my body back towards Alice. I leaned forward and opened my mouth as she fed me the gummy snack."
    MC "Ah, th-thank you."
    BBW "You're... quite welcome..."
    show BE happy
    BE "Okay Alice-chan, my turn!"
    show BBW surprised
    BBW "Hm?!"
    "Honoka leaned all the way forward out of her seat, and plopped another gummy snack in Alice's mouth, giggling all the while."
    show BBW happy
    BBW "Um, th-thank you. That was quite good."
    BE "Hehe!"
    "Honoka stayed there. Her butt was higher up than the back of the chair as she stayed leant forward, her mouth open."
    show BE neutral
    BE "Ah."
    show BBW surprised
    BBW "Oh! Um. Yes. Here."
    "Alice hesitantly placed a gummy snack in Honoka's mouth, who snatched it like a snapping turtle."
    show BE happy
    BE "Mm. Yum."
    MC "I guess... my turn then. Here, Honoka."
    show BE aroused
    BE "Ooh, taking initiative, I like that."
    "Honoka closed her eyes and opened her mouth, blushing faintly as I popped a snack past her lips."
    show BE happy
    BE "Mm, so tasty, Kei-chan."
    MC "Alice?"
    show BBW surprised
    BBW "I-If only to be fair..."
    "Alice leaned forward and opened her mouth, blushing heavily as I slipped the gummy onto her tongue."
    show BBW happy
    BBW "I-It is quite delicious. Thank you."
    MC "You're welcome."
    show BBW neutral
    BBW "I, ah, think I must be going. I have some things to think over."
    show BE neutral
    BE "I better get goin' too."
    MC "Yeah, me three."
    "I reached for some of the wrappers on the table. Honoka and Alice did as well so we could dispose of them."
    show BE happy
    BE "Thanks for inviting me, Alice-chan. This was fun!"
    MC "Yeah, I had a fun time. Was certainly interesting."
    show BBW happy
    BBW "Well, thank you for your cooperation. I will remember to keep you informed on what I have planned. Have a pleasant evening, you two."
    hide BBW with dissolve
    "Alice turned to leave as Honoka waved goodbye."
    BE "I'm off too. Bye Kei-chan!"
    hide BE with dissolve
    "And with that, Honoka skipped away, leaving me to walk back to my room alone. As I did, my fingers faintly rubbed against my lips."
    jump daymenu

label BE022_c1_4:
    "I clammed up. I didn't want to call Honoka out. But Alice was looking more frustrated by the minute. She even looked under the table and didn't find anything."
    "I hoped Honoka would use that chance to empty her breast pocket, but she just sat there."
    show BBW angry
    BBW "Neither of you have any idea where the remaining snacks went?"
    show BE neutral
    BE "Nope!"
    BBW "I am not stupid. It is just the three of us here. There is clearly some foul play at work and I do not appreciate it!"
    play sound Thud
    show BBW angry with vpunch
    "Alice suddenly slammed her hand on the table and stood up, tossing the used wrappers up in the air from the impact of the punch."
    BBW "Tell me now. What is going on?"
    "Honoka hurriedly held up her hands."
    show BE sad
    BE "O-Okay, sorry, just hang on a moment."
    "Honoka reached into her cleavage and began pulling out the snacks she had pilfered from Alice's stash. With each item extracted, Alice's face grew more red, until Honoka stopped."
    "Alice's eyes looked over all the goodies that Honoka had hidden away, and exhaled a breath she had been holding in."
    show BBW neutral at Transform(xzoom=-1)
    BBW "Inoue-san, I do not appreciate this."
    BE "S-Sorry, Alice-chan, I thought it would be funny."
    show BBW angry
    BBW "I repeat. Inoue-san, this is in every way; unfunny, unappreciated, and unwanted. Do you have anything to say about this, Hotsure-san?"
    MC "Well, um. Honoka didn't mean anything by it. It was just meant to be a joke."
    $setAffection("BBW", -1)
    show BBW angry at Transform(xzoom=1)
    BBW "You saw I was getting upset, and that did nothing to change your mind?"
    MC "I'm, I'm sorry. That was clearly a mistake."
    if getAffection("BBW") > 4:
        BBW "Really, Hotsure-san, I thought you were a better judge of character..."
    else:
        BBW "Thank you for your unique, valuable input. Clearly you were a boon to this test."
    BE "H-Hey. Kei-chan didn't mean anything, he meant less than me. Even if he tried to get me to stop, there's no guarantee I would have..."
    show BBW sad
    BBW "The fact he did not even try is indictment enough."
    MC "I, I really am sorry, though."
    "Alice was still standing up. She grabbed her backpack, and with one sweep, pulled most of the treats into the bag. She left the ones that Honoka had hidden originally."
    show BBW angry
    BBW "Never mind. If you wanted them so much, you can just have them."
    "Alice turned around and began walking out of the cafeteria."
    MC "Wait, please, let us make it up to you!"
    hide BBW with dissolve
    show BE at center with dissolve
    "Honoka opened her mouth to speak, but nothing came out. Alice left the room in a huff. I slumped back down in my seat and looked over at Honoka."
    BE "I feel... like a real jerk."
    "Honoka's elbows rested on the table, her hands resting on one another. She pulled her torso back enough to get... a majority of her breasts under the table, at least, then tilted forward and rested her head on her hands with a sigh."
    MC "Yeah. So do I. I hope she's okay."
    "Honoka just made an affirmative sound, her mouth muffled by her uniform's sleeves."
    MC "Do you think we should go after her?"
    BE "I wouldn't."
    "Honoka sat back up and took another deep breath."
    show BE neutral
    BE "I don't think I'd have the energy to go after her right now anyway. But it feels like a bad idea."
    MC "You're probably right."
    show BE sad
    BE "I'm sorry, Kei-chan. I didn't mean to get Alice-chan upset at you."
    if getAffection("BBW") > 4:
        BE "I really hope I didn't screw up your relationship with her. You two seem close."
    else:
        BE "She's always been hard to get friendly with, I hope this doesn't wreck everything."
    MC "I think everything will be okay once she gets time to cool off. Do you want to come back to my room and play video games or something?"
    BE "No. I kind of want to just crawl into a hole for a bit. But beds are more comfy. I'll do that instead."
    "Honoka stood up, sighed for a third time, and put her hand on my shoulder."
    show BE neutral
    BE "Sorry again, Kei-chan. I'll see you later. Be well."
    MC "Okay, Honoka. Feel better."
    hide BE with dissolve
    "With nobody else in the cafeteria, there wasn't any reason for me to stay. I grabbed my backpack and left as well."
    jump daymenu

label BE023:
    scene Track with dissolve
    $setProgress("BE", "BE024")
    "It was after school, and I had promised Honoka earlier that I'd go see her in the archery club. The introductory lesson we'd done together had been interesting, but I decided that archery wasn't for me."
    "Compared to other clubs that Honoka had joined, there didn't seem to be much to archery in terms of different activities they did. Apart from making sure they used the proper technique, and firing at targets, there was no variety."
    "The benefit of actually being in the club was the extra protective gear they could get for their members. Apart from the arm guards and gloves, every student got their own chest guard as well. Which was vitally important for Honoka."
    "Apart from the sound of the captain's commands telling the members when to draw, aim, and shoot, there weren't many sounds."
    "Just the swishes of the bowstrings getting released, the thuds of arrows hitting targets, and occasionally the duller thuds of arrows landing in the grass."
    play sound Whistle
    Haruhiro "Good work so far. Let's break for ten. Get yourselves some drinks and snacks if you need."
    "The captain whistled again to let everyone know to stay away from the target area so he could go retrieve the arrows. I waved over to Honoka."
    MC "Honoka!"
    show BE happy with dissolve
    BE "Yo, Kei-chan, hehe. Glad to see you."
    MC "Same. Doing good out there. How far away are the targets?"
    show BE neutral
    BE "About fifteen meters, I think. But that's only for this lesson, to get us ready for a regular distance. Thirty is the normal minimum."
    MC "Huh, and then if you go to a competition, it's what, fifty?"
    show BE happy
    BE "Haha, nope! It's ridiculous, it's like ninety meters away or something crazy like that. So yeah, you've got to be pretty good to hit a target from that far away."
    MC "That... does sound insane. Holy crud. But you've hit the target every time so far, so I think you can do it."
    show BE happy
    BE "I sure hope so."
    show BE angry
    BE "Though I hope we get out of these early training distances soon. These are for babies."
    MC "Gotta learn to crawl before you can walk."
    show BE sad
    BE "Yeah, guess so."
    show BE happy
    BE "I wanna be like Artemis, just piercing through targets hundreds of meters away, like pyow!"
    MC "Well if you get that good I'm pretty sure you'd be set for life. So aim for that, and then even if you don't get that amazing, you still will be kilometers ahead of other competitors."
    BE "That's the plan!"
    UNKNOWN "Honoka!"
    "Honoka turned her head towards the other club members, as did I, but we didn't see who addressed her."
    UNKNOWN "Behind you..."
    show BE surprised
    BE "Oh!"
    "After turning around we saw the voice who called out to her. The voice belonged to a small girl with dark black hair down to her shoulders."
    "More notable were her sneakers, which looked far bigger than any I'd ever seen. One shoe could have fit both of my feet, and maybe both of Honoka's as well."
    if isEventCleared("BE016"):
        "Seeing her large feet helped me remember. This girl was in the basketball club back when Honoka was a member."
        show BE neutral
        BE "Um, hey, Sakie. What's up?"
        MC "Oh, Sakie. Right. We met at one of Honoka's basketball practices, remember?"
        "Sakie looked at me and my outstretched hand, but then simply sidestepped me to get closer to Honoka. It looked like she'd have gotten closer if she could have, but she stopped when Honoka's shoes met hers."
    else:
        "I looked over to Honoka to see if there was any expression of remembrance on her face. She sighed and glanced over at my direction, confirming yes, she did."
        show BE neutral
        BE "Um, hey, Sakie. What's up? Kei-chan, this is Sakie, she was in the basketball club with me."
        MC "Oh. I see. Good to meet you."
    "I extended my hand out towards Sakie, but she rebuffed my attempt to introduce myself. Instead, she just walked up to Honoka and stopped when her large feet met the ends of Honoka's."
    show BE surprised
    BE "Sakie, is everything okay?"
    Sakie "No. You missed basketball practice again. That's the fifth one you've missed."
    show BE neutral
    BE "Basketball practice? I..."
    show BE happy
    BE "Heh, Sakie, I haven't been in basketball club for over a week now!"
    Sakie "I know. That's why I came to find you. You can do two clubs but you can't do both if one takes away time from the other's practices."
    MC "Honoka. You did quit the basketball club, right?"
    BE "Of course I did!"
    show BE neutral at Transform(xzoom=-1)
    BE "I mean... I stopped going..."
    Sakie "You did not tell any of us that you had actually quit."
    MC "Not even the coach?"
    show BE sad
    BE "No..."
    menu:
        "Call Honoka out on leaving without saying anything.": # BE.Feminine +1
            jump BE023_c1_1
        "Defend Honoka's choice to leave without saying anything.": # BE.Tomboy +1
            jump BE023_c1_2
        "Say Nothing.": #BE.Affection +1
            jump BE023_c1_3

label BE023_c1_1:
    $setVar("BEFeminine", getVar("BEFeminine") + 1)
    MC "Honoka. Why would you do that?"
    show BE surprised
    BE "Huh?"
    MC "You can't just... leave a club like that. Look how upset Sakie is, because she didn't know. She looks worried."
    Sakie "I was not worried."
    MC "You weren't?"
    Sakie "No. She hasn't come back, so I haven't been able to return her hairpin."
    MC "Hairpin?"
    show BE neutral
    BE "Oh, wow, honestly I forgot I let you borrow one."
    BE "{size=-6}She forgets a lot of stuff.{/size}"
    BE "Sakie, you can just keep that if you want. I didn't even worry about it."
    Sakie "...But it's yours."
    show BE happy
    BE "It's yours now! It's... a gift."
    Sakie "Ah. I'll take it, then..."
    Sakie "..."
    Sakie "So you aren't coming back to basketball club?"
    show BE sad
    BE "No, I'm not. Sorry..."
    Sakie "Why not?"
    BE "Do I really have to say it?"
    MC "I would normally say you're not obligated to, but considering how abruptly you left, I think Sakie deserves a bit of an explanation."
    "Honoka sighed. Her gaze turned away as she scratched a cheek and muttered to herself."
    show BE angry at Transform(xzoom=-1)
    BE "Because it was getting annoying."
    Sakie "What was?"
    show BE sad at Transform(xzoom=1)
    BE "All of the... bouncing."
    Sakie "Bouncing is part of the game, Honoka."
    show BE angry
    BE "Not the ball!"
    show BE unique
    BE "These."
    show BE neutral
    BE "Soccer was a lot of running, but most of the time it was more fluid and, I don't know, easier to change momentum. Basketball had a lot more stops and quick changes, and it started hurting by the end of the game."
    show BE angry
    BE "That is, whenever I was put in the game instead of just on the bench."
    Sakie "Honoka, we had over fifteen people in the club, regulation games are five on five, we couldn't always all play together."
    show BE sad
    BE "I know. I just..."
    MC "Didn't feel like anyone would notice if you just left?"
    BE "Oof, yeah. That's pretty much it. Oh boy, that sounds really bad when you put it like that."
    Sakie "We noticed you were gone. I didn't realize you'd actually left, though."
    show BE neutral
    BE "That was my fault. I shouldn't have just bailed on everything. But I didn't have anything to turn back in, so it felt like it could be a clean cut."
    MC "Can you go to the basketball coach after this is done and apologize?"
    show BE happy
    BE "Yeah, I will. This is university after all. We're adults, now. I gotta act like one."
    show BE neutral
    BE "It's just not fun when I have to admit that the girls get in the way of what I want to do."
    Sakie "I get what you mean."
    show BE surprised
    BE "You do?"
    "Sakie lifted up one of her feet, and pointed it towards the sky. The heel rested on the ground as the toes shot upward, and as she lifted the foot it lightly brushed against the underside of Honoka's bosom."
    Sakie "It's not easy to play with these. But I make do. Simple. Big feet means basketball. So I do it."
    show BE happy
    BE "Heh, that's a nice, basic outlook, Sakie. I kind of dig it."
    Sakie "Good. Are you going to come back to the basketball club?"
    show BE neutral
    BE "No, I don't think so. I'm gonna keep with these guys for now. Shooting arrows is pretty badass."
    Sakie "I see. Sounds dope."
    show BE happy
    BE "Yeah, you should give it a try. I tried to get Kei-chan hooked in here..."
    "Honoka roped her arm around my shoulder and suddenly yanked me in to a hug, pressing my face right against her chest."
    show BE neutral
    BE "But he's more wishy-washy than a laundromat and can't commit to a club."
    MC "Hi pot, I'm kettle."
    show BE happy
    BE "Oh, hush."
    "Honoka released me from her pleasant prison-hold, and cracked her neck to the side."
    show BE neutral
    BE "Whether you want to or not, make sure you at least tell the coach if you ever get done with basketball. Don't be like me. Do as I say, not as I do."
    Sakie "Got it. Thank you for the apology."
    BE "Eh, sorry I needed to give one in the first place. Take care, score some big hoops, okay?"
    "Sakie nodded and made her way off of the archery field. I checked my phone for the time, and pointed it out to Honoka. There wasn't much time left for her break."
    show BE sad
    BE "Ah nuts, I'm starving, too."
    "Honoka raced over to the snack table to scarf down some of the offered goods. I sat back down on the nearby grass to watch as the whistle was blown, and the team went back to practicing."
    jump BE023_c1_after

label BE023_c1_2:
    $setVar("BETomboy", getVar("BETomboy") + 1)
    MC "Well, I mean, how long were you in the club, a week?"
    show BE sad
    BE "Something like that? Not very long, at least."
    "I turned to face Sakie, standing a bit directly in front of Honoka."
    MC "So yeah, it's fine she did what she did. She wasn't even being utilized in the club. I remember. She told me that she was barely being put on the court."
    BE "Kei-chan..."
    MC "And I mean, you come to track her down? That doesn't seem cool to me."
    Sakie "It's not cool to leave without telling anybody."
    MC "Maybe she left because she felt embarrassed about something, and it was just easier to-"
    "Honoka suddenly cut me off by placing her hand on my shoulder and pulling me back a step."
    BE "Thanks, Kei-chan, but I'm a big girl, I can fend for myself here."
    "She cleared her throat and stepped forward, looking down for a second before lifting her gaze."
    show BE neutral
    BE "Yeah, as much as it stinks, Kei-chan kind of hit the nail on the head. It was embarrassing."
    show BE sad
    BE "Basketball was fun, but it was clear I wasn't that good with it. But, there were some more obvious issues that made me wanna leave."
    Sakie "Is it not more embarrassing to wuss out of something?"
    show BE surprised
    BE "What?! Hey, I didn't wuss out!"
    Sakie "..."
    MC "..."
    show BE neutral
    BE "..."
    BE "Okay, yeah I wussed out. I shouldn't have, but I did. It was just... simpler, you know? So much easier to just step away and consider it wasn't my problem."
    Sakie "It is your problem."
    "Honoka looked like she was about to slump down into her knees. Sakie didn't mince words."
    show BE sad
    BE "Gah, I know... I'm sorry, Sakie. It was lame of me to just bail on everybody. I just didn't think that people would notice."
    Sakie "The coach noticed. So did the rest of us. It's more than normal but it's a small team. Your lack of presence was felt."
    BE "Ah, geez."
    show BE neutral
    BE "Normally I think I'm tough enough to stick through hard times like that. But it's hard to stay in one spot when the school has so many opportunities."
    show BE happy
    BE "I just wanted to move on to something else, and not feel like I was wasting time in a club I wasn't enjoying all that well. Do you understand?"
    Sakie "Hm. I suppose."
    BE "I do apologize for letting everyone down, though. I'll try and stop by the club later and tell everyone in person. At least the coach."
    MC "That's cool. Good of you to do so."
    show BE neutral
    BE "Eh, if I had done that in the first place, I'd have been better off. Now I'm doing it out of guilt instead of obligation."
    MC "At least you're going to do it, that's to your benefit."
    show BE happy
    BE "I guess you're right."
    BE "So hey, Sakie, did you want to stick around and watch for a bit? Maybe archery appeals to you too."
    Sakie "No thanks. I just came to see what was up."
    show BE neutral
    BE "Fair enough, fair enough. Well hey, good luck with the club, score some three-pointers for me."
    Sakie "I would have to. You never did any yourself."
    show BE surprised
    BE "Hey! I was... close."
    MC "Close only counts in horseshoes and hand grenades."
    "I put my hand on Honoka's shoulder as Sakie turned and left."
    MC "Sorry about earlier. Was I doing that thing where I spoke for you and you didn't appreciate it?"
    show BE neutral
    BE "Kind of. But it got me talking at least, so it was probably to the benefit of the conversation that you did so. I normally react quicker than that."
    MC "Speaking of, time for the break is almost up, you better get a snack or something so you don't collapse later."
    show BE surprised
    BE "Oh shoot, you're right! The granola bars will all be gone! Talk to you in a bit, Kei-chan!"
    "Honoka jet herself to the snack table to grab something quick before the club resumed, while I sat down and watched it continue."
    jump BE023_c1_after

label BE023_c1_3:
    "This confrontation seemed awkward. I didn't want to interrupt, or assume Honoka's intentions. Eventually, she stepped forward and spoke up."
    show BE sad
    BE "Yeah, I did just leave, didn't I? At the time I thought it wouldn't matter, but I guess it did."
    Sakie "One missed meeting would be understandable. You missed more. That's not cool."
    show BE neutral
    BE "It's not. But what made you decide to track me down instead of just assuming I had left?"
    Sakie "To double-check. Don't assume. That's simple stuff."
    show BE happy
    BE "Ah... heh, like how I assumed everyone would just be cool with me leaving without saying anything?"
    Sakie "Exactly."
    show BE neutral
    BE "But you're the only one who came to find me. So thank you, Sakie."
    Sakie "Don't thank me. You left behind a hairpin of yours, too. I wanted to return it."
    "Sakie handed over a small hairpin to Honoka. She looked at it, confused. It was a simple, nondescript pin. One that probably came out of a gachapon machine, at the most."
    BE "Oh, um. Thank you. I forgot I lent you this."
    Sakie "Now we're even."
    show BE happy
    BE "I guess so. Will you tell the others that I've quit, then?"
    Sakie "I think you should do that."
    show BE neutral
    BE "...Yeah you're right. What am I saying? That's me passing the buck of responsibility again. Stupid."
    MC "Don't say stupid. Making mistakes doesn't make you stupid."
    $setAffection("BE", 1)
    show BE happy
    BE "Heh... you're right. Never mind, Sakie. I'll go tell the others when I'm done with archery club, okay?"
    Sakie "Okay."
    show BE neutral
    BE "Good. Yeah, a promise is a promise. And right now my promise is to get back to archery, okay?"
    Sakie "Okay. If you quit this one too, make sure to tell them."
    "Sakie glared a bit at Honoka before turning around and leaving the field. It also left Honoka with a metaphorical dagger through the heart."
    MC "She's... pretty direct, isn't she?"
    show BE happy
    BE "Yeah, but it means she makes good point. Sorry if that was awkward, Kei-chan. But I didn't really want to tell her my reasons for leaving the club. I know it wasn't cool, but..."
    MC "Can you tell me the reasons? Was it just because you weren't playing as much?"
    show BE neutral
    BE "That's definitely part of it. But also, well, the puppies were getting in the way."
    MC "Puppies?"
    show BE unique
    BE "The sweater-puppies. Even with a good bra, they were bouncing all over and making it hard to focus."
    MC "Oh. No, I understand. But, archery is doing okay?"
    show BE happy
    BE "I'm managing! They have good equipment here, and I haven't thwacked my boob with the bowstring yet, so that's nice."
    MC "Yeah. You don't want to be like those Amazons that had to cut off a boob in order to use a bow."
    show BE surprised
    BE "Oh!"
    show BE happy
    BE "Haruhiro actually said that's just a bunch of bull! There's no proof that it was ever a thing!"
    MC "Really? Huh, wow, I thought that was true."
    BE "Nope. Ladies with luscious lumps can still draw a bow! It's pretty awesome."
    MC "Well, that's good. Though, speaking of, you better get back there, your break time is coming to a close."
    show BE surprised
    BE "Agh shoot I'm so hungry too, better eat quick. Thanks Kei-chan, see you in a bit!"
    "Honoka went to the snack table to grab some food before they got back to practice. I sat down and waited for it to be over."
    jump BE023_c1_after

label BE023_c1_after:
    hide BE with dissolve
    "After a few more sessions of shooting targets at the short distance, the club members moved them from fifteen meters down to thirty meters, and tried again."
    "It was clear that there was a difference in difficulty now that the targets were further away. But, Honoka still seemed to be doing great. Several of her shots were bullseyes, judging by her happy reactions. "
    "Eventually the practice ended, and after helping back up, Honoka came over."
    show BE happy with dissolve
    BE "Whew, that was awesome. It's so satisfying hearing that thud when an arrow smacks into the target."
    MC "I can tell. You're getting better at this."
    BE "Hehe, thanks."
    MC "So what did you wanna do now?"
    show BE neutral
    BE "Hm. Honestly, I'm pretty tired. But, I promised I'd go to the basketball club and apologize for leaving earlier. So I should do that."
    MC "Okay. Sounds good. I'm glad Sakie came down then, it's important for you to fix that. Don't do it again, okay?"
    show BE happy
    BE "Heh, I won't. Lesson learned. Promise."
    MC "Good. Okay, well I'm going to head back to my room. Just text me if you want to do something later."
    BE "Sounds good. See you later, Kei-chan."
    "Honoka pulled me into a deep hug, grunting a bit, and released me with a smile. After that she walked towards the basketball court to apologize, and I walked home, relishing that nice warmth from her hug."
    jump daymenu

label BE024:
    scene black with fade
    play music Steamy
    $setProgress("BE", "BE025")
    show BE angry with dissolve
    #panting
    BE "Mmm, Kei-chan, it's so hot!"
    MC "I know. Just keep going at it. It'll help."
    #panting
    show BE aroused
    BE "I'm trying. It just, there's so much of it!"
    MC "You can handle it. I've seen you gobble down more than that before."
    #panting
    show BE unique
    BE "But nothing else has ever been this good before."
    MC "It'll be over soon. Then you can relax."
    #panting
    show BE happy
    BE "I just think it'd be so much better if I took my shirt off..."
    stop music
    show BE neutral
    BE "Here, Kei-chan, hold my ice cream for me."
    MC "What?! Honoka, no, you can't just strip in the middle of town."
    scene Town with fade
    play music Busy
    show BE sad with dissolve
    BE "But it's so ho-o-o-ottttt..."
    "Honoka wasn't kidding. The heat was pretty bad that day. Still, it had been her own idea to brave the heat and get some ice cream. We would have been fine at our rooms, with the air conditioning on."
    MC "Do you want to go back into the ice cream shop and finish there?"
    show BE neutral
    BE "Nah, what's the point of getting a cone if you can't eat it on the go? Besides, I wanna see what else there is around here."
    MC "Fair enough. I offered."
    "My own double-scoop was struggling in the heat. Honoka had wanted soft-serve at first, but it was a good thing I changed her mind. The hard stuff was melting enough as it was."
    MC "Mm, cookie dough."
    show BE happy
    BE "Heh, is it good?"
    MC "Sooo good."
    menu:
        "Offer Honoka a bite.":
            jump BE024_c1_1
        "Keep it to yourself.":
            jump BE024_c1_2

label BE024_c1_1:
    $setFlag("BE024_c1_1")
    MC "Do you want a bite?"
    show BE happy
    BE "Ooh, sure!"
    "Apparently, Honoka's own quadruple-scoop of chocolate, chocolate strawberry, double-fudge, and chocolate chip wasn't enough chocolatey goodness for her."
    "I smirked and lifted the cone up to her mouth. Honoka blushed for a second, and then took a small bite."
    BE "Mm. Ooh yeah, that's good cookie dough in there."
    MC "Yeah you can tell they actually make the dough and don't just buy frozen dough pellets or something."
    "I kept the ice cream over her chest for a moment as I turned my gaze elsewhere. We walked by a storefront with some local band posters that caught my attention."
    show BE surprised
    BE "Kya!"
    MC "What? What happened?!"
    show BE sad
    BE "C-Cold..."
    "I pulled my cone back towards me, and saw the telltale splatter of off-white cream on Honoka's exposed cleavage."
    show BE neutral
    BE "Hah. I guess it really is too hot out here. Do you have a napkin, Kei-chan?"
    menu:
        "Wipe up Honoka's spill yourself.":
            jump BE024_c2_1
        "Lick it up.":
            jump BE024_c2_2
        "Decline that you have any way to clean it.":
            jump BE024_c2_3

label BE024_c1_2:
    "I felt it would have been the polite thing to offer Honoka a bite of my ice cream. But she already had more than I did, she probably didn't want one."
    "I was mistaken. Despite her having four flavors to my one, Honoka leaned to the side and tried to take a bite of my ice cream."
    MC "H-Hey, that's mine!"
    "I pulled my hand away but Honoka insisted. Though she had difficulty coming at the ice cream with her bust getting pressed up against me so firmly."
    show BE happy
    BE "But Kei-chan, ice creaaaam!"
    show BE neutral
    BE "It would be the proper thing to do."
    MC "It's less proper to expect something."
    "Trying to keep my ice cream out of Honoka's greedy clutches, I kept moving the cone around. I stopped when Honoka pulled back unexpectedly, shivering where she stood."
    show BE surprised
    BE "Kya!"
    MC "What? What happened?!"
    show BE sad
    BE "C-Cold..."
    "Honoka invited me to look with a gesture of her hand, and I saw the telltale splatter of off-white cream on Honoka's exposed cleavage."
    show BE neutral
    BE "Hah. Well, that's what I get, I suppose. Do you have a napkin, Kei-chan?"
    menu:
        "Wipe up Honoka's spill yourself.":
            jump BE024_c2_1
        "Lick it up.":
            jump BE024_c2_2
        "Decline that you have any way to clean it.":
            jump BE024_c2_3

label BE024_c2_1:
    $setVar("BEFeminine", getVar("BEFeminine") + 1)
    MC "Sure. Hold on a second."
    if getFlag("BE024_c1_1"):
        "My own cone had already been wrapped in a napkin in an attempt to stop my fingers from getting sticky. But, my pocket had a few extra. I grabbed one and placed it on Honoka's ample chest to wipe the ice cream away."
    else:
        "My own cone had already been wrapped in a napkin in an attempt to stop my fingers from getting sticky. Honoka's playfulness had negated that idea."
        "But, my pocket had a few extra napkins. I grabbed one and placed it on Honoka's ample chest to wipe the ice cream away."
    MC "It's really sticky."
    show BE neutral
    BE "No kidding. Maybe you need to moisten it first."
    if not getFlag("BE024_c1_1"):
        MC "Oh, I'm doing the work am I?"
    "Thinking back to something my mom always did, I took the napkin and just blotted it on my tongue. With a bit of dampness, I was able to clean up the rest of the dessert from Honoka's bosom."
    MC "Did I miss any spot?"
    BE "Hmm."
    "Honoka looked at her chest for a moment, contemplative. After a few seconds of staring, she looked over at me."
    MC "What?"
    show BE sad
    BE "Dude, you just rubbed your drool on my boobs."
    MC "What? No I didn't! That... okay maybe but don't put it like that, that's gross."
    show BE happy
    BE "Exactly! I deserve to do something to make it equal."
    if getFlag("BE024_c1_1"):
        MC "Uh, like what?"
        show BE neutral
        BE "Hmm."
        show BE happy
        BE "I get to drool on your boobs."
        MC "Honoka, I don't have boobs."
        $setAffection("BE", 1)
        BE "Sure you do, they're just not as awesome as mine are! Come here, Honoka needs to make things equal!"
        MC "H-hey watch it!"
    else:
        MC "How is that? You tried stealing my ice cream to start."
        show BE neutral
        BE "So... you want a bite of mine?"
        MC "Depends. If I do, will we be even?"
        BE "No, because I didn't get any drool on you then."
        MC "You should not want that. Ever."
        show BE unique
        BE "What if I do something even better than that to make us so unbalanced that there's only one way to make it even?"
        MC "Huh?"
    "Honoka leaned towards me, her breasts swinging in my direction like two missiles about to be launched. I backed up into the nearest wall, and felt her chest push me into it."
    MC "H-Honoka!"
    show BE neutral
    BE "What's wrong, Kei-chan?"
    show BE unique
    $setAffection("BE", 1)
    BE "I thought all guys dreamed of a girl pushing them into a wall, saying they wanted to swap bodily fluids?"
    if getFlag("BE024_c1_1"):
        MC "Th... This isn't really what I had in mind..."
    else:
        MC "I don't... think this is what they mean."
    show BE surprised
    BE "No?"
    show BE unique
    BE "Well let me change your mind, then."
    "With nowhere to go, Honoka loomed closer. Her chest squished into mine, creating a vacuum seal that felt like it stuck me to the wall. Honoka's face leaned in near, a devilish smirk on her face."
    show BE happy
    BE "Are you ready, Kei-chan?"
    MC "M-Maybe?"
    "Honoka leaned closer, and soon, I felt the cold touch..."
    "Of Honoka's ice cream as she nudged it into my cheek. She giggled like an idiot as she reached into my pocket for another napkin."
    BE "Hehe, did you think I was gonna kiss ya?"
    MC "I mean... yeah?"
    "Honoka licked the napkin and rubbed it against my cheek. I squinted and grumbled as she rubbed it against my face far more than necessary for the small dab of ice cream she left there."
    MC "Did you get it?"
    BE "Mm, yeah. I think so. Now we're even."
    "Like clinking wine glasses at a toast, Honoka took her ice cream cone and pushed it into mine. She left it there for a few seconds, letting the flavors mingle as the sun melted them further."
    BE "Perfect."
    MC "Huh? What's perfect? What did you do?"
    "Honoka didn't answer right away. Instead she sucked on some of the frozen treat for a bit, only turning back towards me after swallowing."
    show BE neutral
    BE "Heh, don't you get it? Now I can taste a little bit of Kei-chan in every bite."
    "If the sun hadn't been melting my ice cream, the heat coming off of my flushed cheeks would have done the job."
    MC "You make me sound like a breakfast cereal."
    show BE happy
    BE "I bet they'd be yummy. But you know what the trick to cereal is, Kei-chan?"
    MC "What's that?"
    "I feared the answer."
    show BE unique
    BE "You can't have cereal without a nice, big splash of milk~"
    "It was a good thing I still was near the wall to support myself. I never thought of flirting as something that could be 'won' before, but Honoka won this time for sure."
    jump daymenu

label BE024_c2_2:
    MC "Sure, I can take care of it. Stay still for a second."
    "Honoka stopped moving for a second, except for still licking at her ice cream to slow the inevitable melting it went through."
    "I reached into my pocket, where I had a stash of napkins from the ice cream parlor. I picked one up and held it to Honoka's chest."
    "But, instead of placing the napkin on the spot where the ice cream fell, I leaned forward, with my tongue extended. I saw Honoka's chest shudder as she tried to pull back."
    "My tongue was too quick, and I only needed a second to slide my tongue up the spot where my ice cream had fallen."
    show BE surprised
    $setAffection("BE", 1)
    BE "K-Kei-chan!"
    if not getFlag("BE024_c1_1"):
        MC "Hush. This is my payment for you getting a bite of my ice cream."
        $setAffection("BE", 1)
        BE "..."
        "Hearing those words come out of my mouth shocked me, but it seemed to stun Honoka enough that I could continue my work."
    "Doing such a thing in public made me feel like a hole opening up beneath my feet would be preferable to being called out. But it was a rare time I could get one over on Honoka!"
    "Even once the ice cream was gone, I didn't stop sliding my tongue up her breast. I reached as far as my neck and tongue could reach, until I just barely grazed the nape of Honoka's neck."
    "With the ice cream thoroughly gone, I pulled back, and licked my lips."
    MC "There we go. All gone."
    "I stared at Honoka for a moment. She stared back. I could visibly see the gulp of anxiousness go down her throat."
    MC "W-Was that too much? So-Sorry, I thought it'd be-"
    "Honoka looked down at her chest for a moment, still holding her ice cream cone. She moved her cone right over her rack again, and pulled her other hand up to the top scoop."
    "With a quick flick, she knocked the top scoop right off, landing the thick hunk of ice cream into her cleavage."
    MC "Wh-What the? Honoka, what are you doing?!"
    show BE unique
    BE "Oops. I spilled more. Can you help me out again, Kei-chan?"
    MC "Bwuh."
    "The scoop was slowly drifting south. There were already rivulets of chocolate moving down the pale curves of her breasts, ready to stain her blouse at any moment."
    MC "Muh."
    BE "Get in there."
    "Before I could reply, though it's not like I was about to decline, Honoka grabbed the collar of my shirt and yanked me into her cleavage. Her aim was great, with my mouth landing right on the scoop of ice cream."
    "Honoka held a firm grip on my collar. It was a struggle to not drop my own ice cream as she heaved her chest up insistently into my face. I gulped, and began eating away at the ice cream on her bust."
    "Despite how enjoyable the situation was at its core, I was desperate to get it finished, on the off chance anyone we knew saw us."
    "My tongue just dragged over her chest again and again, until there wasn't a droplet of ice cream that remained. She made sure of that. She only let go when she no longer felt the chill of the dessert on her chest."
    "When I stood back, I couldn't help but notice the obvious bumps in her shirt, despite the heat outside. The ice cream had really been cold..."
    show BE happy
    BE "..."
    MC "..."
    BE "Well. That was a thing."
    MC "Yeah."
    BE "Was it tasty?"
    MC "..."
    MC "It was, yes."
    show BE unique
    BE "And how did the ice cream taste?"
    MC "I already said-"
    BE "Oh I know what you said. I know what I meant."
    "I had nothing to say back as we walked further down the street. I thought that move would get me one up on Honoka."
    "Turns out we weren't even playing the same game..."
    jump daymenu

label BE024_c2_3:
    $setVar("BETomboy", getVar("BETomboy") + 1)
    MC "No, sorry, I don't."
    if getFlag("BE024_c1_1"):
        "I wasn't sure what voice in my head told me to say that. I had napkins in my pocket, I could have helped, obviously."
        "Maybe it was my curiosity at just seeing the bit of cookie dough ice cream run down Honoka's cleavage. She hadn't ever really buttoned it up all the way since we've arrived here."
        "Though, in this heat, I couldn't blame her this time. It probably helped with ventilation. I bet the ice cream falling on her chest felt nice as well."
    else:
        "That oughta teach her. She'd have to deal with sticky boobs as penance for taking my ice cream!"
    show BE neutral
    BE "Ah, hm, don't worry about it. I've got an idea."
    MC "Oh, you brought napkins?"
    show BE happy
    BE "Nope. Something better."
    show BE unique
    BE "Pillows."
    MC "Huh?"
    "Refusing to answer my question with words, Honoka heaved up one of her breasts with her forearm. She lifted it close to her face, and leaned forward until her face nearly touched it."
    "With a long, slow lick, she cleaned up her breast of the ice cream that had melted onto it. Her expression as she stared at me, giving it one last lick, should have been criminal."
    "Honoka repeated her action with the other breast after swapping which hand held her ice cream cone. Even after both boobs had been licked, there was still a small amount in the middle."
    "That should have been the moment that I offered to help. But instead, Honoka beat me to the punch, pushing her head down further and getting one last lick in to make sure her boobs were perfectly pristine."
    show BE happy
    BE "There we go. Much better now."
    "I kept watching her so intently that I nearly tripped. Judging by her reaction, it was exactly what she'd wanted."
    show BE neutral
    BE "That wasn't what I expected to happen when it got on me, but it turned out quite well in the end, didn't it?"
    MC "Honoka, geez... how do you think to do that stuff in public?"
    BE "How? Hm..."
    show BE happy
    BE "I guess because it makes it easier to think about what kind of stuff I won't do in public. And, well..."
    BE "It makes you happy, doesn't it, Kei-chan?"
    MC "Um. Yeah I suppose that makes me pretty happy."
    BE "Hehe, good."
    show BE neutral
    BE "Oh gosh I just realized the best idea ever."
    "Honoka's 'best idea ever' was simple, but effective. She took her ice cream cone and plunged it into her cleavage. With both hands free, she lifted up her boobs and licked at it that way."
    "I tripped."
    show BE surprised
    BE "Oh no, Kei-chan!"
    "Honoka rushed over to help me, helping me back up. Thankfully there hadn't been any scrapes, just wounded pride."
    show BE sad
    BE "Are you okay, Kei-chan?"
    MC "Y-Yeah, I'm fine. Ice cream survived, too."
    show BE happy
    BE "Phew, good. Didn't mean to go that far."
    MC "Just in case, you should have stood in front of me. I could have used the airbags."
    show BE neutral
    BE "..."
    show BE happy
    BE "Hahaha!"
    "Honoka giggled, her chest making the ice cream wobble in her chest. It was a miracle that the heat from her bosom wasn't making it melt faster."
    BE "Okay, that was a good one. But it wouldn't have worked right now, you'd have fallen right into ice cream, instead."
    MC "Yeah about that, won't you just get more ice cream on your boobs?"
    show BE neutral
    BE "Maaaaaybe. But I can always lick it up again!"
    show BE unique
    BE "Unless you'd prefer to do that, Kei-chan?"
    "I urged Honoka to stop before I tripped again. I didn't think going out to get ice cream would be so memorable, but I wouldn't be forgetting that date for a while..."
    jump daymenu

label BE025:
    scene Field with fade
    $setProgress("BE", "BE026")
    play music Schoolday
    "As much as I wanted to be close to the action for Honoka's archery competition, I had to keep a good distance away from the archers. Not just for safety's sake, but the whistling happened frequently enough that it bothered me to no end."
    "It was a simple enough contest. No other school was involved. Just a way for the archery club members to see how they did against one another. The targets were placed at a competitive distance. "
    "Honoka said they'd only practiced at that distance once before. So this would be a challenge for her. Still, I was cheering her on. Quietly. Unlike a regular sport, archery liked to be nice and quiet."
    Haruhiro "Ready!"
    "The club members stood at attention, even Honoka. It was nice to see her taking this seriously. She looked nice, with the specialized chest plate over her bust, and the leather glove on her string-pulling hand."
    "Each member grabbed one of the arrows from their quiver and nocked it in the bowstring."
    Haruhiro "Aim!"
    "Again, all members moved in pretty close synchronicity with each other, pulling the arrow back until their hands cupped their jawbone. There was a bit of a difference in the speed of each person, but it was still pretty impressive."
    Haruhiro "Fire when ready!"
    "A few fired off their arrows right away, as several arrows thunked into the targets a few second later. Honoka shot her projectile somewhere in the middle. It was hard to see where the arrows hit, when the targets were so far away."
    "The process repeated a few more times as Haruhiro let the members go through their quivers, letting loose a half-dozen arrows before they put them all down."
    Haruhiro "Clear field!"
    "Everyone put their bows down, and the club captain and co-captain went to collect the arrows and see how everyone did."
    show BE happy with dissolve
    BE "Phew. This is exciting!"
    MC "Oh, hey, you're doing great!"
    "Honoka had zoomed over to me as soon as they could leave their stations."
    BE "Can't say I'm doing great, yet, we've gotta see my scores first."
    MC "The anticipation must be killing you."
    show BE neutral
    BE "Agh, it's the worst, really. In the Olympics they can tell you right away what your score is. Here I can kind of estimate, so I can like, adjust my shot a bit?"
    show BE happy
    BE "But otherwise, it's just trying to be consistent."
    MC "I can tell. You looked super focused on everything when Haruhiro was giving out the instructions."
    show BE neutral
    BE "Eh, you've gotta be smart about it. These are real arrows, after all. And Haruhiro's such a dork about it that upsetting him would be like... I dunno, it'd be like bullying Aida-chan. Just feels wrong."
    MC "I see."
    Haruhiro "Scores up!"
    "Honoka and I turned around to hear Haruhiro giving out the scores. He went through them all in alphabetical order."
    Haruhiro "Inoue: 39."
    show BE sad
    BE "Hm. 39. So, that's, what, nearly 2/3 of the best score possible?"
    MC "It's 10 for a bullseye, right? Yeah. Seems so. But most of the others have done about the same. The most I've heard is like, 46."
    show BE neutral
    BE "Right. That's pretty good."
    MC "And you're also new to this. Some of the others have probably been doing this all through high school."
    show BE happy
    BE "That's true! So for being a rookie, I'm kicking booty, aren't I?"
    MC "Yeah, I'd say so. And nothing says you won't get better with practice, either. I haven't seen you this intense in a club before. I think it's a good fit for you."
    BE "Hehe, thanks Kei-chan. Got any motivation for me if I win?"
    MC "Motivation? Hm."
    menu:
        "If you win, I'll treat you to a chocolate feast.": # BE_Affection + 1
            jump BE025_c1_1
        "If you win, I'll give you a kiss.": # BE_Feminine + 1
            jump BE025_c1_2
        "If you win, I'll be your slave for a day.": # BE_Tomboy + 1
            jump BE025_c1_3
        "If you win, we'll switch clothes the next time we go out.": # BE_Affection + 2
            jump BE025_c1_4

label BE025_c1_1:
    MC "If you win, I'll treat you to a chocolate feast."
    show BE happy
    $setAffection("BE", 1)
    BE "Ooh, a chocolate feast, huh? What would that entail?"
    MC "We'll go to a chocolate shop and whatever you think you can eat in one sitting, I'll pay for it."
    show BE neutral
    BE "Iiiinteresting. Even if it's an entire cheesecake?"
    MC "I'd like to see that, either way."
    show BE happy
    BE "Ha! You're on then, Kei-chan! I'll kick butt and get that chocolate, hahahahaha!"
    "I really, really wanted Honoka to win. Really. But when Honoka jogged down to her quiver, laughing maniacally, I wondered if I was going to be out more cash than I could afford..."
    jump BE025_c1_after

label BE025_c1_2:
    $setVar("BEFeminine", getVar("BEFeminine") + 1)
    MC "If you win, I'll give you a kiss."
    show BE neutral
    BE "Oh, just a kiss?"
    MC "Well, I suppose it could be just a kiss. I also haven't specified where I'd be kissing you..."
    show BE surprised
    BE "Huh?"
    MC "And if you blow them away, there'll be more than kissing. And I might get so excited about doing it that I just take you right there in front of all the other club members."
    show BE happy
    BE "F-For a kiss?"
    MC "Maybe I've got something more planned, and you'll just have to find out."
    show BE surprised
    BE "..."
    show BE happy
    BE "O-Okay!"
    "Honoka raced back to her quiver of arrows, while she vibrated on the spot. I hope her anticipation didn't make her too jittery to focus."
    jump BE025_c1_after

label BE025_c1_3:
    $setVar("BETomboy", getVar("BETomboy") + 1)
    MC "If you win, I'll be your slave for a day."
    show BE happy
    BE "Oh ho. Going for the classic cartoon prize, huh?"
    BE "That's tempting, Kei-chan. Very tempting."
    MC "Only for a day, though!"
    show BE neutral
    BE "Oh, but a day is more than enough to have my way with you in every possible way."
    MC "...this does not mean you can do anything illegal, you know. Like you can't have me rob a bank for you."
    show BE happy
    BE "Pff. Why would I do that? There's so many more entertaining ways to play with my little Kei-chan slave~"
    show BE neutral
    BE "You just wait right there, Kei-chan."
    show BE unique
    BE "Your master will return soon."
    "Honoka cackled, holding an outstretched hand to the side of her mouth as she laughed. It may have motivated her, but it also may have been a big mistake."
    jump BE025_c1_after


label BE025_c1_4:
    MC "If you win, we'll switch clothes the next time we go out."
    show BE neutral
    BE "Hm, that's an unusual proposition. What's the benefit for me?"
    MC "Well, you'll get to tease me the entire time we're out because I'll be wearing your clothes."
    MC "You could wear my clothes and get away with it. I'll have to wear a skirt and everything."
    show BE happy
    BE "Not just the skirt, surely. You'd also need to wear my underwear. "
    MC "Um. I guess, yeah I would, if we're going that far."
    BE "Oh trust me, Kei-chan, we'll go that far."
    show BE neutral
    BE "Now if we do that, I can't wear a bra, so that's going to be problematic on my back, you know."
    show BE unique
    BE "Which means we'd need to stuff my bra for you, so you have to walk around with giant cans all day, and see how it feels."
    MC "That, um, that wasn't really part of my plan?"
    show BE happy
    BE "Too late! Done, signed, and sealed tight. It's a closed deal, Kei-chan."
    $setAffection("BE", 2)
    show BE unique
    BE "Oh ho ho I'm going to make you look so ~pretty~."
    "Honoka skipped back to her quiver as I stayed there, watching. That... may have been a bad idea."
    jump BE025_c1_after

label BE025_c1_after:
    hide BE with dissolve
    "After giving Honoka her motivation, she readied herself with all the other members. The quivers had been refilled. Haruhiro came out with a small anemometer to measure the wind speed, and gave everyone the appropriate info."
    Haruhiro "Clear field!"
    "Honoka looked over at me and puckered her lips, blowing a small kiss as she winked. She quickly got back into focus mode and prepared for the next instruction."
    Haruhiro "Ready!"
    "Over the next few minutes, the members fired off another six volleys of arrows at the targets. If it weren't for Haruhiro's whistle and yelling, the sounds of the bowstrings and the arrow thunks would have been kind of enjoyable."
    Haruhiro "Clear field!"
    "Eventually, it was signaled for everyone to put their bows down again, and Honoka came back up to me. This time I stood up and followed her towards the field."
    MC "So, how do you think you did?"
    show BE happy with dissolve
    BE "Gah, I really hope I did great. I really want that prize you offered!"
    MC "Well, seems like it was good motivation for you."
    show BE neutral
    BE "Oh it really was. Here come on, let's see how everyone did."
    "Honoka took my hand and led me towards the other members as they gathered their scores and helped Haruhiro pull the targets back to be stored."
    show BE happy
    BE "Nnngh, come on. What's my score, what's my score?"
    Haruhiro "Inoue: 47. Well done. Total score is 86."
    MC "Wow. Well done, Honoka! That's what, a B?"
    show BE neutral
    BE "Heh. Well, it's out of 120, so that's more of a C, I think."
    MC "That's still impressive for your first outing!"
    show BE happy
    BE "Heh. It is. Buuuut, definitely not enough to win. Belle-mere there got 102. She scored like, five bullseyes."
    "Honoka sighed as she took off her chest guard, letting out a big breath of relief."
    MC "Ah, nuts."
    MC "Well, I'll tell you what. When you win one, that motivational prize will still be there waiting for you."
    BE "Oh yeah? Good. Hehe. It really got me excited."
    MC "I'm glad. I just wanna support you."
    show BE neutral
    BE "You're so good to me, Kei-chan, I-"
    Haruhiro "HEY!"
    "Honoka and I looked and saw what Haruhiro was yelling at. One of the club members had brought a sibling, and they'd gotten hold of a bow, nocking it."
    Haruhiro "PUT THE BOW DOWN! PEOPLE DOWN RANGE!"
    "The kid panicked, and let go of the string after turning the bow away from down range."
    "Right towards Honoka and I."
    hide BE with dissolve
    if getSkill("Athletics") <= 0:
        jump BE025_c2_1
    elif getSkill("Athletics") <= 5:
        jump BE025_c2_2
    else:
        jump BE025_c2_3

label BE025_c2_1:
    "Suddenly, I was pushed onto the ground. I winced a bit as my elbow dug into the grass. Honoka's chest pushed into me from below."
    "She'd thought quickly, and managed to knock us both down to the ground. I looked over at the arrow and saw it land harmlessly a good five meters away."
    MC "Holy crap..."
    "Honoka quickly stood up and pat herself down. My heart raced. I felt numb, paralyzed. I didn't even think to get up until Honoka reached down and offered her hand."
    show BE sad with dissolve
    BE "Kei-chan, are you okay?"
    MC "Yeah, I'm fine. You're not hurt, are you?"
    show BE neutral
    BE "No no, I'm good. Good thing I still had my arm guard on."
    MC "I'm so sorry, I just froze up. I don't know what happened, I-"
    show BE happy
    BE "Hey, it's okay."
    "Honoka pulled me suddenly deep into a hug, and stroked the back of my head."
    show BE neutral
    BE "You weren't under any obligation to do anything. And besides, it missed where we were standing anyway."
    MC "I still feel I should have done something."
    show BE happy
    BE "Nah. Don't stress. But maybe start working out a bit just in case. Pushing you down was like knocking over a lamp."
    MC "Heh... yeah you've got a point..."
    jump BE025_c2_after

label BE025_c2_2:
    "Seeing the arrow move, I quickly pushed Honoka over onto the ground. I wasn't sure why it was the best course of action, but I figured making ourselves smaller targets was good."
    "I winced as my knees skidded into the dirt, and looked to the side at Honoka who looked surprised."
    MC "Honoka are you okay?"
    "Before she answered, there was a pitiful 'thwick' as the arrow landed in the ground, many meters away from us."
    show BE neutral with dissolve
    BE "Oh, I'm a little banged up, but I think I'm okay. Are you hurt?"
    MC "No, the arrow didn't hit us, thankfully."
    "Honoka and I stood up, brushing ourselves off with dust, and looking over at Haruhiro who was giving a club member a good verbal thrashing."
    MC "I see what you meant earlier about strict safety rules."
    BE "Yeah. That was bad."
    show BE happy
    BE "Very manly of you to push me out of the way like that, though."
    MC "Oh, heh, I was just... acting on instinct."
    BE "Hehe. Well, it's a good instinct to have."
    jump BE025_c2_after

label BE025_c2_3:
    "Thinking quickly, I grabbed Honoka by the waist and spun. A small yelp came from her as I lifted her up and we both fell to the ground. I knew her back would hit the ground, but hoped my hands around her waist would cushion her fall some."
    "I wanted Honoka safe, and this way if the arrow hit us, I was the bigger target. I landed right on top of her, and did my best to brace us with my body."
    "I didn't feel anything, and Honoka didn't make a sound, so after a few seconds, I looked over. The arrow hadn't even managed to pierce the dirt, falling flat into the grass."
    MC "Honoka, you okay?"
    "Looking down at Honoka, her face was flushed, and I wasn't sure why. One of my hands quickly went to her arm."
    MC "You didn't get hit by anything, did you?"
    "I'd literally just seen that the arrow missed us. But... worry doesn't tend to be logical."
    show BE happy with dissolve
    BE "N-No, I'm fine. It's just. You're, um."
    MC "I know. Sorry. I just acted and wanted you safe."
    BE "No, it's not that. Your hand is just..."
    "Oh."
    MC "Ah, sorry!"
    "I quickly took my other hand off of her breast and placed it flat on the ground. I moved my other hand as well, just for safety."
    show BE sad
    BE "I didn't say you had to stop..."
    MC "Oh! W-Well... this probably would look weird if we stayed on the ground for too long."
    "I stood up, and took Honoka's hand, easily pulling her back up with me. I helped her dust off her uniform from the dirt on the ground, and just double-checked to make sure she was okay."
    MC "You sure you're okay?"
    show BE happy
    BE "Heh, I'm fine, Kei-chan. Being saved by a rogue arrow, and ending up with Kei-chan on top of me? Yeah that's pretty okay in my book."
    MC "Heh, you're acting like I planned it..."
    jump BE025_c2_after

label BE025_c2_after:
    "Haruhiro, the club captain, came up to us in a huff, shaking his head."
    Haruhiro "I swear if I see that kid on the field again after this incident, I'm going to... just... do things to them! Gah!"
    Haruhiro "Are you two okay?!"
    show BE neutral
    BE "Yeah, we're okay, Haruhiro. Is everything all right over there?"
    Haruhiro "Takiya brought his little brother with him today and was showing him the equipment. He got distracted and his brother started playing with it. I'm so sorry, I should have seen that."
    MC "Well. Thankfully the arrow didn't hit anyone."
    show BE happy
    BE "Yep, we're all okay! Nothing to worry about."
    "Haruhiro shook his head."
    Haruhiro "Negative. Safety protocols are in place to prevent this from happening. I may need to look at the guidelines again and see what can be done to make sure this doesn't happen."
    MC "Well. Good luck with that."
    BE "Yeah. Doesn't sound fun."
    Haruhiro "Thank you. In the meantime, great work today, Inoue. Go get some rest. Take care, you two. I'll see you next practice."
    "After Haruhiro left, Honoka and I let out a big sigh."
    show BE neutral
    BE "Phew. Well. He's got a point, let's go relax. Wanna come to my room and hang out?"
    MC "Sure. Sounds like fun."
    "We left the archery field after Honoka handed in the rest of her equipment. She joked about taking a shower and asking if I wanted to help get her clean."
    "I said that could be motivation for me the next time I wanted to win a contest."
    jump daymenu

label BE026:
    #Setting: Field or Flowery Area
    scene Field with fade
    $setProgress("BE", "BE027")
    show BE happy with dissolve
    play music Hallway
    BE "Kei-chan, I've got an idea, and you're not gonna believe what it is."
    "Honoka had bumped into me, in her usual fashion. It was good to know that despite it happening more often than not, that it still was a pleasant way to say hello."
    MC "What's up, Honoka?"
    "Honoka was dressed normally. Except she seemed to have swapped out her normal skirt for a pair of cargo shorts, with baggy pockets down to the knees. "
    "In her left hand, Honoka held two small nets."
    MC "Are you a lepidopterist?"
    show BE sad
    BE "No? At least I don't think so, both my parents were born in Japan..."
    show BE happy
    BE "Look, I've been hearing cicadas a bunch lately! I haven't gone cicada catching in ages. I think maybe, like, twice since I was a kid."
    show BE neutral
    BE "Today's as good a day as any to get back into the hobby. Here!"
    "Honoka tossed me a net."
    MC "Hm. Bug-catching, huh? I dunno. I guess I didn't have any plans, but it feels a little childish, and-"
    "Honoka cut me off by thrusting the bottom of her net in her cleavage and chuckling."
    MC "Yeah never mind, this sounds fun."
    "The weather wasn't scorching hot, but definitely warm enough that the cicadas would be out. The trick was finding them. After walking around for a while, it was hard to ignore the telltale sounds of them rubbing their wings together."
    #SFX: Cicada noise
    MC "So, what's the plan? Wanna try to see who can catch the most?"
    BE "Hmm..."
    show BE angry
    BE "Nah, let's just hang out and see if we can catch a few."
    MC "That's fine! Sounds like a plan to me."
    show BE happy
    BE "I'd totally get more, anyway."
    MC "..."
    MC "'Oh, I'd love to debate you, but my argument is so superior I'd just win anyway, so there's no point in bothering.'"
    BE "Yeah, you got it!"
    "Honoka and I looked around the nearby trees, trying to find a trace of the bugs. Honoka started snapping her fingers now and then as she walked around."
    MC "What are you doing that for?"
    show BE neutral
    BE "It's supposed to help make them expect you. Like it sounds similar enough to their mating call to trick them."
    MC "Huh. Well it's better than any idea I have."
    "I started snapping as well. Eventually, Honoka and I zoned in on a cicada, resting on the bark of a tree. Its wings fluttered back and forth, letting out its high-pitched noise every few seconds."
    BE "There we go. Oh it's a big one."
    MC "Sweet. You wanna go for it?"
    "Honoka nodded and gave a quick lick of her upper lip."
    BE "I think I can get it, but I'll need to get into the bushes to grab it."
    menu:
        "Go for it.": #BE_Tomboy  +1
            jump BE026_c1_1
        "What about your clothes?": #BE_Feminine +1
            jump BE026_c1_2

label BE026_c1_1:
    $setVar("BETomboy", getVar("BETomboy") + 1)
    MC "Go for it. Gotta move quick, though."
    "Honoka nodded again, and crouched down on her knees. Her breasts squished down into her thighs, as she began crawling towards the bush. She watched the bug intently, stone-still, and I found myself holding my breath."
    "Then, with a jump, Honoka leaped towards the tree. Her net thwacked into the bark, as Honoka hurtled to the bush. Her breasts impacted into the shrub as she landed near-horizontal in the greens."
    show BE happy
    BE "Haha, I got it!"
    MC "Awesome, let's see!"
    "Honoka twisted the net to get the bug at the bottom of the mesh, and extracted herself from the bush."
    BE "Ow. Ow. Haha. That was fun."
    MC "Let's take a look."
    "The mesh of the net was sparse enough to get a good view of the cicada inside. It was obviously freaked out, so we couldn't keep it for very long."
    MC "You forget how big these things get. Even as an adult, they're still huge."
    BE "Yeah, it's pretty crazy. They don't live really long either, if I remember. It's like, years spent as a larva and then weeks or months as something actually cool."
    MC "Well. Hope it's having fun at least, if it can even process what fun is."
    "Honoka tilted the net upside down, and the cicada stopped clinging to the net after a few seconds. It dropped into Honoka's empty hand, and stayed there for a few seconds."
    BE "This really is the perfect image for something that's ugly and cute."
    MC "I think he just looked at you. I'm not sure if he's offended at being called ugly or enjoyed being called cute."
    show BE neutral
    BE "Pff, it's just a cicada, Kei-chan. It probably can't even hear me."
    "The cicada proceeded to jump out of Honoka's hand, and flew towards her cleavage. Her eyes widened as the bug landed on her breast and began trying to scurry inside."
    show BE surprised
    BE "Oh my god get it out get it out get it out get it out."
    MC "Yoink!"
    "I reached into her breasts as fast as I could and yanked the cicada out, trying my best to only grab it enough to pull it, and not to hurt it. As soon as it was pulled out, it flew away from my hand, leaving a traumatized Honoka."
    BE "Ew, oh god, gah, I'm gonna be scrubbing those for an hour tonight. "
    MC "The joke is... obvious. But, Honoka, you got hurt."
    show BE sad
    BE "Oh, what? I didn't think cicadas bit..."
    MC "No, no, here."
    "I took hold of Honoka's hand, and twisted her arm a bit, to show her the cut on the side of her upper arm. It dripped a bit of blood onto the torn sleeve of her shirt."
    BE "Aw, shoot. Well, a new shirt's no big deal. But, ow, now that you mention it, that stings."
    menu:
        "Take Honoka to the nurse's office.":
            jump BE026_c2_1
        "Take Honoka back to your room.": #BE_Affection + 1
            jump BE026_c2_2

label BE026_c2_1:
    MC "Let's just head to the nurse's office, and get a bandage for it."
    "Honoka nodded. It sucked to put our bug-hunt to a short stop, but better to make sure Honoka didn't get an infection or anything."

    scene Nurse Office with fade
    "We were surprised when the nurse was actually there to help Honoka."
    Nurse "Hello. How can I help you?"
    show BE sad with dissolve
    BE "I got a cut on my arm here..."
    Nurse "Oh my. How did that happen?"
    "The nurse took Honoka to sit down as she pulled out the standard array of disinfectant and bandages. Honoka explained how she got it from a bush, trying to catch a cicada."
    Nurse "Cicada-catching?"
    Nurse "...A little old for that, aren't you?"
    show BE angry
    BE "You're never too old to enjoy fun stuff!"
    Nurse "Fun stuff, of course. But is hunting for bugs really fun? Now this is going to sting a little."
    show BE sad
    BE "Ow. Ow. Ow. OW!"
    Nurse "Sorry! I said it was going to sting. It's a large cut, dear. You'll need to make sure to stay away from sharp, thorny bushes for a while, until this heals at least."
    BE "All right..."
    MC "Well. At least we caught one!"
    show BE neutral
    BE "Heh, we did. Am I good to go?"
    Nurse "Just about, just making sure that bandage is on nice and secure. Yes. Now you're fine. A regular adhesive strip should be fine if that happens to come off. But that should last until it heals."
    Nurse "If it doesn't seem to be getting better after a few days, just come on back."
    BE "Okay. Will do. Thank you."
    "Honoka hopped off of the bed and walked over, taking my hand and leaving the nurse's office."
    MC "So, what do you want to do now?"
    BE "Hm. I guess I want to go back to my room and wash my boobs, honestly. It's one thing to hold a cicada, having it crawl on you is not fun."
    MC "Ah, that's fair."
    MC "..."
    MC "Can I help?"
    "Honoka smirked and leaned forward, planting a kiss on my cheek."
    show BE happy
    BE "Maybe another time, Kei-chan, hehe. But thanks for coming to play with me today. "
    MC "Anytime, Honoka. Take care."
    "Honoka walked off to her room, and I returned to mine, carrying both of our cicada nets back with me. I suppose we'd have to figure out what to do with them later."
    jump daymenu

label BE026_c2_2:
    MC "My room's pretty close. I have some stuff I could use to help clean you up. "
    show BE happy
    $setAffection("BE", 1)
    BE "Okay!"

    scene Dorm Interior with fade
    "I took Honoka back to my room. In my drawer, I'd kept a few basic first-aid supplies. Presenting a bottle of hydrogen peroxide to Honoka, she visibly winced."
    show BE sad with dissolve
    BE "Kei-chan, that stuff sucks."
    MC "I know, but it'll help."
    if getSkill("Academics") > 5:
        MC "I'll put it on a cotton ball and make it easier on you."
    MC "Go ahead and sit down."
    show BE happy
    BE "Hehe, okay. And should I take off my shirt, Doctor Kei-chan?"
    MC "I mean... if you want. Wait. That's not the way these fantasies are supposed to play out. You're supposed to be the nurse."
    BE "I can still be the nurse! Nurses get injuries."
    MC "Yeah, that's fair."
    if getSkill("Academics") > 5:
        "I took the moistened cotton ball and brought it up to Honoka's arm."
        MC "Now, nurse, this might sting a little."
        "Rubbing the peroxide on Honoka's cut, she took my hand and squeezed it to help diffuse the discomfort. After rubbing a bit of antibacterial cream on it, I slapped two bandages on the cut to cover it up completely."
        $setAffection("BE", 1)
        MC "There. You should be all better, nurse."
    else:
        "I took Honoka's arm, and tipped the bottle of peroxide over the cut to pour a small amount on the wound."
        MC "Nurse, this is going to hurt."
        show BE sad
        BE "Ow, ow..."
        "Honoka's hand dug into the mattress she sat on as I dried up her arm and covered the cut with a bandage, making sure to cover it completely."
        MC "There you go. All better."
    show BE happy
    BE "Oh, thank you, Dr. Kei-chan. How could I ever make it up to you? I don't have any money on me..."
    MC "Well, it's part of the job, obviously. But. Well, you mentioned taking off your shirt earlier?"
    show BE surprised
    BE "Oh, doctor. Taking advantage of a wounded woman like that. I think I might faint. Oh no, but then I'd just be in an even more vulnerable state!"
    show BE unique
    BE "I suppose I have no choice in the matter..."
    "Before I could tell Honoka that she didn't have to, Honoka reached down and undid a button on the bottom of her shirt. "
    "Honoka's face was beet-red as she undid another two buttons from the bottom up. There was no more exposure of her breasts, at this point. It made it all the more tantalizing in a way. "
    show BE happy
    BE "I, I have to get a new shirt, anyway. So..."
    "Honoka took the middle of her shirt, which still had a few buttons attached near the center, hiding the middle of her breasts and the bra beneath. She pulled, and thrust her chest out, causing the last buttons to explode off of her."
    "Honoka's breasts burst out, covered in a white, lacy bra that gave her melons support. Without the barrier of her shirt, nearly all of her bosom was exposed."
    "I never realized how much her shirt actually held them back. There was easily a few extra inches exposed now."
    MC "I, I... I..."
    show BE aroused
    BE "Heh... I've always wanted to do that..."
    "I held my mouth and nose as I stared at Honoka's bra-clad chest. What could be done? There were so many options, and none seemed better than the other. It was like winning the lottery and not knowing what to buy first."
    MC "Honoka, they're spectacular."
    show BE happy
    BE "Oh, go on."
    MC "I mean, I don't know enough words to describe them. They're so... big, and round, and..."
    BE "No, Kei-chan, I mean..."
    show BE aroused
    BE "Go on."
    MC "Go... on... I..."
    "I stepped forward, hands outstretched, towards Honoka's quivering rack. Her face grew more red as I approached. My hands landed on her chest, and I looked up at her. My hands sunk in, and I just kept pushing."
    "It seemed the most natural thing to do. I just pushed, letting the flesh envelop the tips of my fingers as I pushed down on her breasts. Honoka took my wrists, and shoved them in deeper."
    "Eventually, I reached a point where my hands wouldn't go in any deeper. I looked at Honoka hesitantly. She grabbed my head and pulled me down. She stopped, just an inch before my face reached her cleavage."
    MC "H-Honoka?"
    show BE aroused
    BE "S-Sorry, Kei-chan. I've got no problems with this. But, I feel all icky cuz of the bug earlier and... it's kind of killing the mood."
    MCT "God damn bugs."
    "Honoka cleared her throat, and gulped. "
    show BE unique
    BE "I don't want you digging into these babies if they're not pristine. You know?"
    MC "Urgh... I think I could look past that, Honoka."
    show BE happy
    BE "Hehe, I'm sure you could. But... don't worry. It's gonna happen. I just need a better time. Okay?"
    "I sighed. But she had a point."
    MC "You're right, you're right. But you did also ruin your shirt just now."
    "Honoka looked at her de-buttoned shirt and laughed."
    show BE neutral
    BE "Ha. Oh, well. I can still wear it well enough. I've got more. But I guess for now I should go back to my room and take a shower."
    "Honoka put her shirt back on, doing up the few buttons she hadn't intentionally destroyed. She chuckled, and looked at the bra still visible."
    show BE happy
    BE "Well, it'll get me back to my room if I move quick. I don't want anyone but my Kei-chan seeing my cans."
    "She leaned forward and pulled me into a quick smooch on the cheek again."
    BE "I had fun, Kei-chan. Thanks for hanging out with me."
    hide BE with dissolve
    "Honoka left to go back to her room, and I slumped down on my bed. My head hit the pillow, but hit something hard. I reached back and felt around, until I found the button of Honoka's left behind."
    "I hesitated a moment, and placed the button up to my nose. It still smelled like her."
    "She was right, it would be worth the wait."
    jump daymenu

label BE026_c1_2:
    $setVar("BEFeminine", getVar("BEFeminine") + 1)
    MC "What about your clothes?"
    show BE neutral
    BE "Huh? Oh, hm. That bush does look a bit thorny. There's gotta be a way to deal with this. Hm."
    "Honoka got down in a crouched position, causing her breasts to squish into her knees as she lowered herself."
    "She slowly urged herself forward, around the outside of the bush. She held her net tightly in her hands as she searched for a different angle."
    BE "Okay, I'm going to try from here. You let me know when I should strike, if you see it about to fly off, maybe."
    MC "Got it."
    menu:
        "Let Honoka get closer before swinging":
            jump BE026_c3_1
        "Tell Honoka to swing for the bug right away.":
            jump BE026_c3_2

label BE026_c3_1:
    MC "A little more, get a little closer."
    "Honoka slowly got closer to the cicada. After a few seconds, I gave the go-ahead. Her net swung at the bug."
    "Unfortunately, the angle was off, and her net didn't land with a perfect seal around the cicada. The bug began to run away from the net, and fluttered into the air."
    show BE surprised
    BE "Darnit! Get it, Kei-chan!"
    if getSkill("Athletics") <= 5:
        "I grabbed my net, and tried to watch for the flight of the cicada. It didn't zoom straight up into the air. After a few seconds, I swung my net, and landed it on the ground."
        MC "I think I got it!"
        BE "You did?!"
        MC "Yeah, come here and see."
    else:
        "I didn't feel like there was enough time to grab my net. I just reached out with both hands and clasped them together."
        "My heart nearly jumped out of my chest when I felt the flutter of the cicada's wings in my grasp."
        MC "Holy crap, I caught it!"
        $setAffection("BE", 2)
        BE "You did? With your bare hands? You didn't hurt it, did you?"
        MC "No no, it's right here, and it's okay. You've gotta check this out!"
    "Honoka stood up, and dusted herself off. She rushed off to my position as quick as she could, making sure to keep the cicada contained."
    show BE neutral
    BE "Oh my gosh, I can't believe you caught it!"
    MC "Yeah, here, take a look..."
    if getSkill("Athletics") <= 5:
        "I carefully opened up my hands so Honoka could peer inside and see the cicada."
        show BE happy
        BE "It looks perfectly fine. Hehe, I can't believe you were quick enough to grab it like that."
        MC "It wasn't exactly easy, to be fair."
    else:
        "I carefully moved the net, so Honoka could see the cicada inside."
        show BE surprised
        BE "Wow! Good catch, Kei-chan."
        MC "Heh, I'm surprised I got it in one swing."
    jump BE026_c3_after

label BE026_c3_2:
    "Honoka seemed to be in a good position. I waited just half a second before telling her to swing for the cicada."
    MC "Go, right now. You're at a good spot."
    "Honoka swung her net at the tree, and managed to nail it right in the center. The cicada was perfectly trapped in the net."
    show BE happy
    BE "Haha, I got it! Perfect. Kei-chan, come here a bit and help me with this."
    "From her position, crouched down, it looked hard for her to maneuver the net without falling over. I approached Honoka, and helped grip the net while she stood back up."
    MC "Here, got it."
    show BE neutral
    BE "Thanks, Kei-chan. Didn't wanna ruin the moment. Let's put it over here to get a better look at it."
    "Honoka took the net and brought it into a more open section. She slipped the net around, so we could see the chirping cicada through the mesh."
    MC "This is so cool. Yeah, I'm glad you wanted to do this, Honoka."
    show BE happy
    BE "Me too. You told me the right time to swing, too."
    MC "That's barely anything compared to you actually catching it."
    "Honoka and I chuckled, and took another look at the cicada."
    jump BE026_c3_after

label BE026_c3_after:
    show BE happy
    BE "They get so big, don't they? Look at it. I wonder if it's a guy or a girl."
    MC "I don't plan on getting close enough to it to find out, honestly."
    show BE neutral
    BE "It's kind of odd, isn't it?"
    MC "What's odd?"
    BE "Well, they don't live for very long, or at least, they don't get seen by the public that often. So you'd think they'd, well, look prettier."
    MC "I guess not everything in nature has to stylistically be appealing. Like, camouflage, or animals with bright colors to show they're poisonous."
    BE "Good point, yeah. Not everything can be stellar and beautiful."
    MC "If everything was. Then, well, we wouldn't have that, what's the word?"
    BE "Baseline?"
    MC "Yeah, I think that's it. Like that line about 'you can't appreciate a sunny day without a few rainy days'."
    BE "Yeah, I do like that."
    BE "We should probably let the little thing go now, I don't want it to get upset."
    MC "Right."
    "Honoka and I let the little cicada go. It wandered around on the grass for a bit, before flying off. We laughed as we saw it landed on a tree right away."
    MC "Well, that looked like an easy one. Should we try for something harder?"
    show BE happy
    BE "Hm. You know. It's a nice enough day, and I don't feel like getting dirty now."
    BE "Want to just walk around, and take in the sights?"
    MC "Sure, I'd like that."
    "I took Honoka's hand and we walked around for a while more, just enjoying the sights of the various bugs and flora. Looking for cicadas was pretty fun. But when you're not looking for anything specific, you see a lot more."
    jump daymenu

label BE027:
    $setProgress("BE", "BE028")
    #Setting: School Grounds
    scene Campus Center with fade
    play music Busy
    "It wasn't typically something I noted, but the birds were particularly loud today. It started with the sounds of their chirping helping to wake me up that morning, and their various tweets followed me throughout the school grounds."
    "Usually, birds singing would be a sign of something good happening. But I didn't have anything planned, so I chalked it up to a coincidence."
    "Honoka's chest collided with my back, like two silk balloon missiles. That certainly could be considered something good happening to me, but it was such a regular occurrence by this point that it didn't feel 'exceptional'."
    show BE happy with dissolve
    BE "Heyyyy, Kei-chan. Wanna come clothes-shopping with me? I wanted to grab a new outfit since it was getting hotter out. I could use a second opinion!"
    "Helping Honoka pick out a new outfit? Well, that could definitely be considered a nice turn of events."
    MC "Sure, I could help you out. I don't think I'd consider myself much of a fashion expert. But I can at least help make sure you pick out something that's not tacky."
    BE "That's all I need. Let's go now, I found this neat-looking store on the Internet that had a good variety of stuff."
    "I checked my pockets, making sure I had my wallet and ID on me. Seeing no reason I couldn't leave right then and there, I followed Honoka to the bus stop so we could travel into town."
    "The short ride there was uneventful. Honoka and I sat next to each other on the next bus we could grab, and made our way to the stop nearest her chosen shop."

    scene Town with fade
    MC "'Clothes and Shoes'. That's... is that really the name of the shop?"
    show BE neutral with dissolve
    BE "Yep. Nice isn't it? Straightforward and to the point. Would be better if more things were like that. 'Let's go to 'Grocery Store' to get some food for dinner and then we'll head to 'Movie Theater' later.'"
    "I mulled over Honoka's statement as we walked into the store."
    MC "But then you wouldn't be able to differentiate between good and bad places."
    BE "Hmm..."
    show BE happy
    BE "Well then they should just stop having bad places. Easy fix."
    "Honoka threw her arms up in victory as if she'd just solved a world crisis."
    MC "Well, we're here. What were you looking for in particular?"
    show BE neutral
    BE "Hm."

    scene Clothes Store with fade
    "Honoka looked back and forth around the store. It seemed to be geared mainly towards women, but had a fair share of men's clothes as well."
    "Going from one side to the other was like examining a display of paint swatches, as the colors shifted from blacks and blues to reds and pinks. Shoes in the middle, with underwear and socks in the back."
    show BE neutral with dissolve
    BE "I guess I'll just look around and see what looks cool, what catches my eye. You know, do the whole 'browsing' thing."
    BE "Do you want to look around with me? Or check stuff out for yourself? They have some nice looking men's duds here."
    MC "What, are you saying I need a makeover?"
    show BE happy
    BE "Naaah. But I mean, a new shirt never hurts, does it?"
    menu:
        "Browse around with Honoka.":
            jump BE027_c1_1
        "Look for something for yourself.":
            jump BE027_c1_2

label BE027_c1_1:
    MC "I guess not, but, we're here for you, so I'll stick with you for a while."
    BE "Heh. Sounds fine to me. Let's start over here, I saw a cool tank top on the mannequin when we came in."
    "I followed Honoka around the store, going from one end to the other. Honoka selected a couple different pieces of clothing as she browsed."
    show BE sad
    BE "Hmm. No, definitely not grey. Too dreary. Blue's always good."
    MC "I always got the impression that girls picked clothes based on what's in style, but you're really focused on the colors, by the looks of it."
    show BE happy
    BE "Well, that's what people notice first, I figure. If they get up close to ya, sure. But at a regular distance they'll probably just see the color pattern, so as long as it's pleasing to the eye, I think that works."
    "Honoka leaned in closer."
    show BE unique
    BE "Plus, I've got a feeling that most people spend more time looking at my chest then they do at my clothes. Just a hunch."
    MC "Whatever would give you that impression?"
    "It surely had nothing to do with the fact that, standing a normal distance away from me, a slight lean was enough for her bosom to rest on my arm."
    show BE happy
    BE "Hehe. Anyway, colors say a lot about a person. I don't know what they say, exactly. But it's probably good."
    "Honoka took the small selection of clothes she'd found so far and laid them in my arms."
    BE "You chose to browse around with me, so you become the honorary cart. The duty of every guy who goes shopping with a gal."
    MC "Joy."
    "Honoka continued to browse around the shop, pulling off the odd item here or there. After a while I wasn't paying too much attention. It was definitely more than she could buy, so hopefully she'd whittled them down to a few choices."
    "Before I knew it, we ended up in the dressing rooms. Honoka entered one of the stalls and put out some of the clothes she'd selected, staring intently at them. With all the focus of a scientist trying to remember a complex formula."
    jump BE027_c1_after

label BE027_c1_2:
    MC "Maybe. I'll take a look then. Maybe there's something here I like."
    BE "Alrighty then. I'll give you a holler when I'm ready to try stuff on."
    "Giving Honoka a nod, I walked over to the significantly-smaller men's section."
    hide BE with dissolve
    #(possibly bump into Minori here, if they've been introduced to Keisuke by this point, otherwise this proceeding scene)
    "I wasn't entirely sure what to look for as I picked through the various collared and non-collared shirts they had available. Should I look for something Honoka would like?"
    "Was her suggestion a hint that she wanted to see me in something particular?"
    "If that was the case, I had no idea what that was, though. I haven't worn much else around her besides the Seichou uniform."
    "Back when we were kids, she always liked my Starchaser United t-shirt, but I doubt they made shirts for that show anymore."
    MC "This looks nice. Maybe? I guess if I tried it on for Honoka, she could decide for me."
    "I pulled the tag closer to my face, and brushed some of my hair out of the way to get a better look."
    MC "Jeez. That feels pricy for just a shirt. It feels nice enough. But, egh, I don't know."
    "Shopping usually didn't feel this hard. Then again, typically I would have just strolled in, found the first shirt that looked good, and bought as many similar-styled ones as I could to avoid trying on different ones."
    "Maybe shopping with Honoka nearby was affecting my judgement. It wasn't just clothes for me, it felt like clothes for Honoka as well. "
    MC "Bleh, I need a haircut."
    "My hair had gotten in my eyes again. Though, I supposed that was going to be a more recurring problem as time went on. Clothes, hair... Neither of those were things I felt like dealing with at the moment."
    show BE happy with dissolve
    BE "Hey, Kei-chan, I think I'm ready to try some stuff on. Come over to the dressing room when you're ready!"
    "Honoka gave a good distraction at least. I put the shirt I was holding back in the stack, as neatly-folded as I could muster, and wandered over to the dressing room. "
    jump BE027_c1_after

label BE027_c1_after:
    show BE neutral
    BE "Okay. I think I've narrowed it down to three choices. Which of these do you like the most?"
    "I looked at Honoka's pile of clothes in the dressing room. She'd kept it fairly neat, at least. So the workers wouldn't have to clean up much if she really only planned on buying a single outfit."
    BE "So, this is the first one."
    "Honoka held up two different pieces of clothing. The first was a pair of jean shorts. They looked like they'd go down to her knees or higher, with a little skull print on one of the thighs."
    "In her other hand, Honoka had a jacket, one that didn't look like it was meant to come down past the chest area either way. It was loosely fit around a black and red t-shirt, the colors splashed on like tiger stripes."
    show BE happy
    BE "And I think if I get this one I'll get this sweet little belt I saw in the corner of the shop. "
    show BE neutral
    BE "Second outfit is this one."
    "Honoka only held up one outfit this time and I could barely believe that she considered buying it. It looked more like a fetish get-up than any actual piece of clothing."
    "Lace leggings, a short camisole that barely seemed capable of going down past her hips, with an extremely low-cut top. The material was all extremely sheer, so it looked practically see-through."
    show BE happy
    BE "And this is the third one I liked."
    "Honoka's last outfit of choice was a light blue sundress. It had thin straps, and was just a one-piece dress that went down to her thighs. It looked like the kind of outfit that would go perfect with a large, floppy hat."
    show BE neutral
    BE "So, what do ya think? Which one should I try on?"
    jump BE027_c2

label BE027_c2:
    menu:
        "The jean shorts and jacket.": #BE_Tomboy +1
            jump BE027_c2_1
        "The skimpy lingerie." if not getFlag("BE027_c2_2"):
            jump BE027_c2_2
        "The skimpy lingerie. (disabled)" if getFlag("BE027_c2_2"):
            pass
        "The sundress.": # BE_Feminine +1
            jump BE027_c2_3

label BE027_c2_1:
    $setVar("BETomboy", getVar("BETomboy") + 1)
    MC "That first one seemed pretty cool, with the little half-jacket thing. How about that one?"
    show BE happy
    BE "You got it, boss-man."
    hide BE with dissolve
    "Honoka took the outfit and closed the dressing room door behind her. I waited a minute outside, checking my phone, and just waiting for the go-ahead."
    show BE happy with dissolve
    BE "Here's Honoka, ready for action!"
    "Honoka exited the dressing room stall, looking devilishly good in her chosen getup. The jean shorts stopped just above her knees. The material was intentionally a little ragged-looking, but seemed sturdy."
    "Up above, the t-shirt she'd chosen clung to her bosom pretty tightly, though she'd chosen enough of a large size that it managed to cover up her belly as well. The half-jacket seemed ill-fitting, but somehow, Honoka made it work."
    "The way the two halves of the jacket attempted to connect made it seem like two hands of fabric were trying to grope her chest at all times."
    MC "Wow."
    BE "Hehe, so what'cha think?"
    menu:
        "It looks awesome.":
            MC "It looks awesome."
            BE "Damn straight. How awesome?"
            menu:
                "Like you could star in a rock and roll band.":
                    MC "So awesome, you look like you could star in a rock and roll band."
                    BE "Ooh yeah, that's hot. One of those heavy ones with a lead female singer like Thrashing Pixies or The Widowmakers! I dig it!"
                "Like you could beat up an entire martial arts club.": #BE_Affection +2
                    MC "So awesome, you look like you could beat up an entire martial arts club."
                    show BE surprised
                    BE "Yessssss!"
                    show BE happy
                    $setAffection("BE", 2)
                    BE "Haha! That's just the look I was going for!"
                    BE "Just imagine it, all the tough clubs at school cowering in fear as I walk by."
                    show BE angry
                    BE "'Oh gosh, we may as well quit. We'll never be as tough as Hardass Honoka!'"
                    show BE happy
                    BE "That's perfect, Kei-chan, thanks!"
                "Like you could pilot a fighter jet.":
                    MC "So awesome, you look like you could pilot a fighter jet."
                    BE "Ooh I hadn't considered that. I like it though. Ones with tons of missiles and machine gun turrets. With a badass name like Sky Queen or something. Sweet."
                "Like you could get into a VIP lounge.":
                    MC "So awesome, you look like you could get into a VIP lounge."
                    BE "Mmm, like one of those exclusive club dealies. I'd need a pair of sunglasses to go with that, I think."
                    BE "Gotta say, pretty cool to think about strolling into a place and everyone going 'Whoa, this place must rock. Inoue the Incredible is here.' Excellent."
        "It looks nice.":
            MC "It looks nice."
            show BE neutral
            BE "Nice, huh? That's pretty good."
        "It looks cute.":
            MC "It looks cute."
            show BE neutral
            BE "Cute, huh? Not really what I was going for, but it works."
        "It looks cool.":
            MC "It looks cool."
            show BE neutral
            BE "Cool, huh? Heh, yeah that's pretty much what I wanted to hear."
    MC "So, you're going to buy that?"
    show BE happy
    BE "Yeah, totally. It looks great, you like it. And the price is pretty good too. May as well!"
    MC "Perfect. I'm glad I could help. Just getting the one thing, though?"
    show BE neutral
    BE "Yeah. I mean there's not many opportunities to dress super casually, so no point in buying a lot of clothes, you know?"
    MC "Nah, that makes sense."
    BE "Give me a second to change back and we can head to the register. I don't really like wearing new clothes out of a store. It feels weird."
    MC "No, you've got a point. It's definitely weird."
    "Honoka retreated back into the dressing room as I waited once more. She came out with her new outfit in hand. As we walked back to the register, she grabbed a small, black belt with a studded buckle to wear with her new shorts."
    "As we waited in line, I looked over the cheap, small items they had nearby, wondering if I needed anything. I decided against it, thinking nobody ever really needed anything from the 'gotcha' section of the register."
    "Just as I thought that, Honoka grabbed one of the fancy chocolate bars and added it to her purchase. She was happy, though. So I couldn't judge."
    Owner "Thank you very much. Please come again. Have a nice day."
    show BE happy
    BE "Thank you!"
    MC "All happy?"
    BE "The happiest, is the expression on my face not obvious enough?"
    MC "Hm. It's hard to say. You smile like that a lot."
    BE "Well, I assure you, I'm smiling a bit more than normal, then. I'm gonna look so awesome in this outfit. Just gotta wash it first, and we're good to go. Ready to head back?"
    MC "Yep, I'm good."
    MC "I gotta say, Honoka. This is the first time I've enjoyed shopping with a girl."
    show BE surprised
    BE "Oh, you did this often?"
    MC "I mean... with my mom."
    show BE neutral
    BE "Ah. I'll let you in on a secret, Kei-chan. Shopping with parents is never fun."
    "I nodded as Honoka and I walked back towards the bus stop to head back to campus. She held her bag in one hand, and the other wrapped around my chest, pulling me into a side hug."
    "We might need to go shopping more often."
    jump daymenu

label BE027_c2_2:
    $setFlag("BE027_c2_2")
    MC "I mean, if I'm honest. I really want you to try on that lingerie number."
    show BE neutral
    BE "..."
    MC "..."
    show BE happy
    BE "Hahaha. Oh, oh, I was reallllly hoping you'd say that! "
    "I just stared, unsure what the gag is."
    BE "Kei-chan, you can't just 'try on' lingerie. And I'm here looking for an outfit, remember? I can't really wear this out and about."
    show BE sad
    BE "Plus, this thing costs like, 28,000 yen. Which is insane for something that, by all rights, is meant to be worn for five seconds and then ripped off in a lustful frenzy."
    MC "So, you're... just teasing me."
    show BE happy
    BE "Yep."
    MC "... That's cold-blooded."
    show BE neutral
    BE "You're just too much fun to tease, Kei-chan. I can't help it. Haha. Okay. But, seriously, the two outfits here, I do genuinely want to get one of them. Which should I try?"
    jump BE027_c2

label BE027_c2_3:
    $setVar("BEFeminine", getVar("BEFeminine") + 1)
    MC "The last one seemed nice. Was that a sundress? I think that would look good."
    show BE happy
    BE "Heh, if you insist. I'll give it a shot!"
    "Honoka closed the door to the dressing room, leaving me to wait a moment as she got gussied up. After a while, Honoka's head peeked out of the door."
    show BE neutral
    BE "Kei-chan, can you come in? Check this out, make sure it looks okay?"
    MC "Huh? Sure."
    "I walked into the dressing room and closed it behind me."
    "When I saw Honoka standing there, I wasn't sure why she wanted me to come in, instead of her coming out. The sundress exposed a good amount of cleavage, but nothing that seemed out of her comfort level."
    "The straps around her shoulders were thin, but the rest of the dress seemed to be a nice, thicker material that hugged her curves well. The dress ended halfway down her calves, with a curved pattern on the fringe."
    MC "Wow, that looks nice, Honoka."
    show BE happy
    BE "You really think so? It's not too much?"
    menu:
        "Not at all, it's cute.":
            jump BE027_c3_1
        "Not at all, you're beautiful.": # BE_Affection +1
            jump BE027_c3_2

label BE027_c3_1:
    MC "Not at all, it's cute."
    BE "Hehe... you really think it's cute, huh?"
    MC "It is cute. It's definitely not something I've seen you wear all that often. Maybe that helps. A bit of... what's the word I'm thinking of?"
    show BE neutral
    BE "I'm not sure, but I think I know what you mean."
    "Honoka moved a strand of her brunette hair behind her ear, and looked at the mirror installed in the dressing room."
    show BE happy
    BE "It's definitely a bit of a different look for me, but it looks pretty good."
    MC "I think it does. I really picture you like, wearing a big, floppy sun hat, too."
    BE "Hehe, that would be pretty adorable."
    "It was nice to see she agreed with me. She seemed a bit unsure of the outfit, otherwise."
    MC "The blue is a nice color for you as well. It's still blue, I know you like blue a lot."
    "Honoka nodded."
    show BE neutral
    BE "They had one that was more of a darker blue, but the material didn't feel as nice. It felt more... fuddy-duddy. This felt hipper, for a younger, cuter girl."
    MC "Well, I'd have to say it's an accurate assessment."
    show BE happy
    BE "Hehe, thanks, Kei-chan."
    jump BE027_c3_after

label BE027_c3_2:
    MC "Not at all, you're beautiful."
    "Honoka blushed a bit harder, and I leaned in closer."
    show BE neutral
    $setAffection("BE", 1)
    BE "I asked about the dress, not me..."
    MC "Can't they be the same? You look beautiful as it is, you look even more beautiful in a pretty dress like that."
    BE "Heh, you can't mean that."
    MC "Oh, can't I?"
    "I double-checked that the door was locked, and stepped behind Honoka, making sure she looked into the mirror."
    MC "How could I be lying about this figure being beautiful?"
    if getSkill("Art") > 5:
        MC "When you look so stunning that the mirror can't even properly show all of your beauty, limited by what's achievable by the science of mirrors?"
        MC "When every part of you, from your cocoa-brown hair, to your soft, gentle lips, seems to have been crafted to perfection?"
        MC "How could I deny that I'm staring at a dress that somehow took the most magnificent set of breasts I've ever seen, and elevated them to levels that goddesses wish they could muster?"
        MC "When you're looking this lovely that my heart aches, knowing I have to blink, and that split-second of time with my eyes closed is just one moment missed where I'm not staring at your gorgeous beauty?"
        MC "Honoka, if you think you don't look beautiful in this dress, then I'm going to pick you up right now and take you to the nearest eye doctor, because everything I'm looking at right now makes me so happy that I forget all the world's problems."
        $setAffection("BE", 1)
    else:
        MC "I don't think there's words to properly describe how pretty you look right now, Honoka. If there are, I just don't know them."
        MC "But I do know that you look beautiful. If you walked out of here in this outfit girls would be feeling so jealous about you, and it wouldn't just be because of your amazing boobs."
        MC "Not just any girl could pull off this outfit, you know. They need the right, luscious figure to really fill it out. You're all that and more, Honoka."
    "Honoka gulped, as I leaned in towards her ear for that last sentence, whispering it as softly as I could."
    show BE aroused
    BE "K-K-Kei-chan..."
    "Whether I realized what I was doing or not, my hands reached up to Honoka's chest, and grabbed her melons with a firm, hard squeeze. The squeaking moan that came out of her mouth was something to die for."
    MC "If I can get a little more blunt, Honoka... "
    "I punctuated my words with another squeeze from below, trying to push her breasts up, until I saw her nipples peek out over the tops of the dress."
    MC "One thing I really like about this dress is how splendid it makes your breasts look."
    BE "Kei-chan, y-you can't say things like that."
    MC "No? But it's true. Like two huge mounds of pudding ready to be nibbled on. That deep line of cleavage. For a cute dress, you really picked out something erotic, didn't you?"
    "Another squeeze was all it took to get Honoka's cans out of the confines of her dress, plopping down back onto the blue of the sundress. Her nipples were perky and erect. I gave her breasts one more grope before moving up to the obvious targets."
    MC "Maybe that was your plan all along, wasn't it? Get me here, alone, so you could lock the two of us in a room and get me all hot and bothered with this sexy little number."
    "I just kept squeezing every few words, letting my body grind into her back as I whispered. Honoka's face was as crimson as a chili pepper, letting out little oohs and eeps as I massaged her nipples."
    BE "Th-That's not true, hahhh. Nngh, you, hahh..."
    MC "Look what it's done to me, Honoka. Turned me into this horny little beast. If you buy it, and you know you want to, who knows what'll happen the next time you wear it?"
    "This time I twisted them, just a bit, and Honoka bit down on her lip. Her hands grabbed mine, and I quickly stopped, just to be safe."
    BE "Th-They won't let me buy it if they see it's dirty."
    MC "Hm, I guess we better stop short then, shouldn't we?"
    "Honoka nodded. My hands remained on her chest, as did her own hands on mine. But we remained in that spot for a moment before I pulled back. I cleared my throat and unlocked the door."
    jump BE027_c3_after

label BE027_c3_after:
    MC "So... you're going to get that outfit?"
    show BE happy
    BE "How can I not? When you liked it so much..."
    MC "Sounds wonderful. Just that one, then?"
    show BE neutral
    BE "Well, who knows how long this one will fit as it is? It's a good fit for now, but I don't want to buy too many things I'll outgrow."
    MC "That makes sense. Well I'll just wait outside for you, then."
    BE "I'm going to just change really quick."
    "I nodded and waited outside for Honoka, looking around. The shop had a lot of things, but unfortunately, no hats to be found. Shame, one would have looked really nice with that dress."
    "Honoka came back out a few minutes later, back in her original outfit. Her sundress was hung back on the hook to take to the register. She was smiling, and still blushing a bit."
    MC "Ready to check out?"
    show BE happy
    BE "Yep."
    "Honoka and I approached the register and waited in line until it was her turn to check out."
    "I looked over the cheap, small items they had nearby, wondering if I needed anything. I decided against it, thinking nobody ever really needed anything from the 'gotcha' section of the register."
    "Just as I thought that, Honoka grabbed one of the small bottles of perfume they had for sale. She smiled my way as she added it to her purchase."
    Owner "Thank you very much. Please come again. Have a nice day."
    BE "Thank you!"
    MC "All happy?"
    BE "Very much so. This was a nice trip, Kei-chan. Thank you for coming with me."
    MC "Well it was definitely a fun shopping trip. You really did look great in that dress, you know."
    BE "Hehe, you'll see more of it, then. Just need to give it a wash first. I'll need to learn how to deal with something like this, it's gentler than what I normally wear. Ready to head back?"
    MC "Yep, I'm good."
    MC "I gotta say, Honoka. This is the first time I've enjoyed shopping with a girl. "
    show BE surprised
    BE "Oh, you did this often?"
    MC "I mean... with my mom."
    show BE surprised
    BE "Ah. I'll let you in on a secret, Kei-chan. Shopping with parents is never fun."
    "I nodded as Honoka and I walked back towards the bus stop to head back to campus. She held her bag in one hand, and the other grabbed my hand, squeezing it tightly as she smiled my way."
    "We might need to go shopping more often."
    jump daymenu

label BE028:
    $setProgress("BE", "BE029")
    scene Arcade with fade
    play music Schoolday
    #BGM: Light chatter or some sort of electronic music
    "Honoka and I were on a date at the arcade. It was late at night, and moderately crowded. It meant there were occasional waits for some of the games we wanted to play, but nothing that was unbearable."
    "Honoka and I just finished a co-op light gun game, and had decided to stop before we spent all our coins trying to kill one boss."
    show BE angry with dissolve
    BE "Guh, that guy was ridiculous! We each died like five times and he was still at half health."
    MC "And he was only the second boss too. There were still two more worlds after that. We'd be here all night, and broke, if we tried to beat him legitimately. "
    show BE neutral
    BE "There must have been some way to stun him when he was charging that attack, but nothing we unloaded on him seemed to make a difference."
    MC "Well, lesson learned. We'll skip that one next time. You hungry for anything? I'm kind of craving a pretzel or something."
    show BE happy
    BE "Hm, no, I'm okay. I'm just hungry for more games."
    MC "Heh, not a problem. Let's see if there's a big line at the snack bar or anything."
    "Honoka and I walked towards the snack area. There were a few vending machines and a small stand near the ticket counter that sold quick snacks. Unfortunately for me, it looked closed."
    MC "Darn."
    MC "Well, no sense fretting about it. Let's find something else. I know there's stuff here we haven't played yet."
    "Honoka and I walked around for a while, enjoying the lights and sounds of all the various machines."
    "Soon, my eyes caught sight of something I hadn't noticed on our previous visits. Maybe it was a new installation, or simply a machine I hadn't paid any mind to."
    MC "Hey, Honoka. Check this out. One of those old-fashioned love testers."
    BE "Haha, really? Gosh I didn't think they still existed. I would have thought they were all buried in a landfill somewhere."
    MC "I don't think that's accurate."
    MC "But yeah, looks like it's plugged in. Let's see... takes two tokens. 'One for each partner to see how much love you share.'"
    show BE neutral
    BE "Gosh, that's cheesy."
    MC "Extra cheesy. A lactose-intolerant person's nightmare."
    "Honoka approached one side of the machine and squeezed the handle. But without being paid for, the trigger on the joystick couldn't be pulled. "
    show BE angry
    BE "You know, I'm pretty sure I remember reading somewhere that these things don't even work right."
    MC "Well, I doubt there's actually a way to judge how much two people love each other just by squeezing handles."
    show BE neutral
    BE "No no no, not in that way. Like, it didn't even matter how much you squeeze the handles. It just did a random roulette to determine what result you received."
    MC "Ah, that's kind of lame."
    show BE happy
    BE "Haha, well it was easier to do than actually programming, I bet. But that means two people could squeeze it the same way a bunch of times and get different results!"
    MC "Well, that's just silly then, isn't it?"
    BE "Heh, yeah."
    show BE neutral
    BE "I mean, you'd have to be a real putz to use one of these and think it actually worked."
    MC "Right."
    BE "..."
    MC "..."
    BE "I mean, I can't get too mad at the concept. It's cute. People decades ago didn't know what games were."
    MC "Yeah. It's harmless fun. Even if it's too outdated for us to use."
    BE "..."
    MC "..."
    BE "..."
    MC "You want the right side or the left?"
    show BE happy
    BE "I'll take the right. A bit easier to grip it from my angle."
    "I couldn't help but sigh at our predictability. But, it just seemed unavoidable. It was there, we weren't going to not use it."
    show BE neutral
    BE "Let's see, where's the coin slot. Theeere we go!"
    "Honoka and I took our coins and slid them into the slots. A tiny little heart on each side of the machine lit up, slightly out of sync with one another."
    "The machine had eight rankings that appeared to go from 'Not compatible at all' to 'You better be married if you aren't already'."
    MC "We better not end up as 'Isolated Icebergs'."
    show BE happy
    BE "Haha. Don't set your sights so low, Kei-chan! I think we're at least going to end up as 'Close Comrades'."
    "It was a nice midpoint on the ranking scale. The top point was 'Wedding Wishers'. Between the low and mid points on the tester were a few more humorous terms."
    "'Deadly Daters', 'Feeble Friends', and 'Merry Match-Ups' were lower than what Honoka wanted, so I had to hope the machine gave us a good squeeze."
    MC "Okay, so when this lights up, just squeeze as hard as you can, right?"
    BE "No!"
    MC "No?"
    show BE sad
    BE "I can't believe we forgot the most important part of this."
    "Honoka's spare hand reached over and grabbed mine. I chuckled. "
    MC "Oh, duh. It can't really test our compatibility if we're not holding hands."
    MC "Okay. Here we go!"
    show cg BE028 with dissolve
    "The machine lit up 'Squeeze Now' and Honoka and I both grit our teeth as we pulled on the handle with all our might. Slowly, the marker on the display moved upwards, past the worst position and up towards the middle."
    #show BE happy
    BE "Come on, Kei-chan, we can do this."
    if getAffection("BE") < 8:
        jump BE028_test_1
    elif getAffection("BE") < 16:
        jump BE028_test_2
    else:
        jump BE028_test_3

label BE028_test_1:
    "As Honoka and I squeezed the handle as hard as we could, the display on the machine moved up and down. It passed by the first two titles easily, and continued to waver around the remaining ones."
    "The rhythm was unsteady and strange. Honoka and I looked at each other and squeezed our hands as well, just to make sure it worked as well as legend said it was supposed to."
    "Eventually the device stopped, and the selection stopped third from the top, glowing a pale yellow-orange LED."
    hide cg with dissolve
    show BE sad
    BE "Aw, Satisfying Soulmates? Darn, we should be way higher than that!"
    MC "I think it's pretty good, we're really high up. Most of the names given here aren't super flattering anyway, at least we got one of the good ones."
    show BE angry
    BE "Hmmmm. You're being too good-hearted about this one, Kei-chan. As far as I'm concerned, we should always be on the top! We must be doing something wrong."
    MC "Heh, you're the one who brought up that these things are mostly garbage to begin with."
    show BE neutral
    BE "That's true... and I guess this proved it! Clearly it's wrong. I was squeezing as hard as I could, and you were too, right?"
    MC "Of course I was."
    BE "Hmmmmmmmmmmm..."
    BE "Did you now?"
    BE "That's interesting. "
    MC "How is that interesting?"
    BE "Well, I guess it just has me thinking, if that's how hard you can squeeze, then I haven't seen some things. Things I'd like to see."
    MC "..."
    MC "Honoka, I think it's a little early for me to show you my-"
    BE "You have not once squeezed my boobs that hard since we've started dating."
    MC "Wh-what?"
    show BE happy
    BE "Oh, to be fair, I've lost track of exactly how many times you've squeezed my boobs. But, yeah, if that's how hard you can normally squeeze, and not some fluke, then I'm disappointed."
    MC "If I squeezed you that hard, wouldn't that hurt?"
    BE "Ha! Are you kidding? These puppies are basically my own airbags. They're meant to take some assault."
    "Honoka pat the top of her left breast to prove her point."
    BE "Besides, it's not like you're gonna be punching me in the rack. It'll be fine."
    "Honoka stared at me, expectantly."
    MC "Um... I get the feeling you want me to do it right here, right now."
    show BE neutral
    BE "I wouldn't be opposed to the concept..."
    "It was an opportunity to squeeze Honoka's chest. I looked around to see if anybody was staring right at us, and didn't notice anyone glaring in our direction."
    "So, after a deep breath, I reached forward and pressed my palm into the side of Honoka's left breast. I felt the soft flesh fill my palm, as I squeezed as hard as I could."
    show BE aroused
    BE "Oof..."
    "Honoka's face turned red as I squeezed, and began biting down on her lip. I saw her take a deep breath and exhale, which is when I took my hand away."
    BE "Okay... yeah..."
    show BE unique
    BE "You can do that more often. That felt good."
    MC "It did, not too hard?"
    show BE happy
    BE "I think these are so soft that any hardness you can give me would just be smothered."
    show BE aroused
    BE "Yes, that was intentional."
    MC "Honoka, that is... incredibly hot. But now I'm physically unable to walk away from this love tester machine after hearing that."
    show BE happy
    BE "Haha, you perv. Nobody's gonna look down there when I've got all this cleavage on display. Come on, I wanna do a racing game next!"
    "Honoka grabbed my hand and yanked me away to another attraction in the arcade. The date wasn't over yet, but I felt super distracted now."
    "I had a feeling I'd be losing the next few matches with Honoka."
    jump daymenu

label BE028_test_2:
    "The two of us looked at the display as we squeezed the handles on the love tester. A light moved back and forth between the top and bottom choices."
    "Honoka's hand was still in mine, and squeezed my hand tighter as we waited for it to make its decision. My other hand felt sweaty as it tugged on the joystick, trying to pull in the trigger as hard as it could go."
    "It eventually stopped, and to my surprise it landed only one away from the top title."
    MC "Wow. Linked Lovebirds. That's really good."
    hide cg with dissolve
    show BE happy
    BE "Huh, yeah it is. I think I'm happy with that. We got sooo close to the top though."
    MC "Hm. Well if this thing does work, we're doing pretty good considering how it's not been that long since we started dating."
    BE "True. But on the other hand, I had the benefit of the childhood friend bonus."
    MC "Childhood friend bonus?"
    show BE neutral
    BE "Of course. Childhood friends are more likely to end up the wife like, 80%% of the time. Love-College, Space Romance Epoch, Honey-kouhai is All Grown Up, Samurai Society, Hyper-Dimension Ranger Eri-chan..."
    show BE happy
    BE "If you start out with a childhood friend, they're gonna end up the wife."
    MC "Even if they've been separated for a long time, like you and I were?"
    BE "Oh! Especially in that case. Then it goes up to 98.2%%."
    MC "I think I may want to see your data on this and draw my own conclusions."
    show BE neutral
    BE "I have another thesis on this that you might like to see."
    MC "Oh, what's that?"
    "Honoka smirked, and took my hands in hers. She pulled them into her chest, letting my palms rest right on the front of her chest as she closed in on me."
    "As my hands sank into the warm flesh of her bosom, she pressed her lips against mine. Her hands let go of me, but I kept my fingers right where they were. I don't think I could have moved them even if I wanted to."
    "Honoka broke the kiss and gave another little smooch as she moved her chest up my hands, until they forced themselves to rest on my palms. She giggled and reached around to grab my hips, pulling me into a hug as tight as she could."
    show BE aroused
    BE "How's that for a convincing argument?"
    MC "Wha... argument? Huh? We were arguing? Why is it so hot in here?"
    show BE happy
    BE "Hehe. Uh-oh, did I fry your brain, Kei-chan? These things are more dangerous than I thought! Let's get you out and get your brain back to normal."
    "Honoka stepped back, letting go of me so I could come back to my senses. I stared at her chest for a moment, and cleared my throat."
    MC "Um... yeah, I believe you then. I have no retort."
    show BE unique
    BE "I don't think you totally believe me, still. You're just saying that."
    show BE happy
    BE "Come on, I'll go kick your butt in Whip-Whap, that'll prove I'm right."
    "Honoka yanked me away to another machine and began pushing tokens into the slot. I don't think it mattered that I already believed her, she was going to steamroll me anyway. "
    "I was very distracted."
    jump daymenu

label BE028_test_3:
    "Honoka and I watched the love tester as it responded to our synchronized squeezing. The lights on the machine went wild as a display moved up and down between the best and worst options. We were obviously hoping for the best."
    MC "Come on, come on."
    #show BE happy
    BE "We got this, Kei-chan!"
    "Honoka's fingernails dug slightly into my hand as she squeezed mine. I grit my teeth, and tugged as hard as I could until the display stopped moving."
    "Lights went off in several spots and a weary sound played, so distorted and fragmented that we couldn't make out what it originally was. But the light had stopped right at the top, signifying us as Wedding Wishers."
    hide cg with dissolve
    show BE surprised
    BE "Holy crap, Kei-chan. Weeee did iiiit!"
    "Honoka jumped in the air, cheering for joy. She landed back down with a thud, and then a jiggle. It was hard not to notice."
    MC "Well, what else could it be?"
    "I tried to act as confident as my body and voice would allow."
    MC "I mean, I'm pretty sure this is proof that the whole thing isn't a scam. It wouldn't do this for just anyone, would it?"
    show BE happy
    BE "Hehehe, no sir-ee, only for Kei-chan and me."
    "Honoka clenched her fists and pushed them together above her bust. "
    BE "So what do you think? Is there a place near here that does wedding ceremonies? I bet Naomi-chan could make us a really nice bouquet set for cheap... Alice-chan's probably got a lead on who would make good wedding cake."
    MC "Uh."
    BE "Haha, relax, Kei-chan. I'm kidding. I mean, I'm definitely not saying 'no' to the idea! But geez, that would be rushing into things, wouldn't it?"
    MC "Yeah, I was about to say. There's quite a few things you're supposed to do before you get married."
    show BE neutral
    BE "Oh, is there now?"
    show BE unique
    BE "What would they be?"
    MC "I'm... struggling to come up with an answer to that right away. But, you know, like... meeting each other's parents."
    show BE happy
    BE "Kei-chan, we literally have spent the night at each other's houses before."
    MC "Oh, right."
    MC "Well, we also need to go on some dates."
    show BE neutral
    BE "Which we have."
    MC "Uh. There's gotta be more that I can't think of."
    show BE happy
    BE "Hehehe. I can think of a few things we haven't done yet."
    MC "Oh, please tell me, I'm desperate for a way out of this conversation."
    "Honoka smiled and looked around. She took my hand and led me to the side of the love tester. I wasn't sure what she was doing. But soon she had my back against the wall."
    "Suddenly her foot pressed into the wall next to me, trapping me between her leg and the love tester. I looked up at her, confused, until she shakily reached out towards me."
    "Honoka grabbed the hem of my pants, and yanked it down. It didn't get far, only a few inches, but enough to make my boxers visible. "
    "I was not as distressed by this as I should have been, especially not when Honoka got down on her knees, and suddenly her chest was up against my groin."
    "Honoka's face was beet-red and a bit moist as she lifted up her cans, and I suddenly felt even more softness push into my crotch. Honoka let them linger there for a moment before she stood up, and turned around."
    show BE neutral
    BE "Uh, uh, well, um, there... that's one thing we haven't done yet..."
    MC "I'm... not sure what that was."
    "I pulled my pants back up."
    BE "W-Well, I didn't want to go all the way with it... right now, at least. Then we would be one step closer to getting married, and you were clearly nervous about that!"
    show BE surprised
    BE "It had nothing to do with the fact that the idea of me touching you down there with these in public made me freeze up like a popsicle!"
    "I couldn't help but chuckle."
    MC "Well, we're not quite there yet. This machine's decades old, it's not quite up to what romantic standards have evolved to."
    "I stepped forward and placed my hand on Honoka's chest, and then pushed down and through the cleavage she had on display, until I was nearly up to my elbow. "
    MC "I'm pretty sure, for example, that this would be unheard of in 1920."
    "Honoka looked so red that I swore steam would come out of her ears. I retracted my arm quickly, and then stepped to the side for a hug."
    MC "I think it's clear we're attracted to each other. But we don't need to rush into anything. I'm happy with just being near you, Honoka."
    MC "Occasional kisses of course, those are always nice."
    MC "And if I can feel these luscious boobs you're so proud of, I just consider that a nice bonus."
    "I leaned forward and gave her a kiss, giggling as I did so."
    show BE happy
    BE "Hehe... you make some good points, Kei-chan. I think I just wanted to be adventurous, but, woof... just a bit much for me right now, haha."
    MC "It's all good, Honoka."
    MC "Hey, how about we go play a fighting game? You want to be adventurous, play a character you're less sure you can destroy me at."
    BE "Mm, nah, I think I'll whoop your butt anyway! "
    "Honoka and I approached the fighting game section of the arcade. I snickered as she perked up again. We might not be ready to be extra physical yet, but... "
    "I didn't think that stopped us from being 'Wedding Wishers'."
    jump daymenu

label BE029:
    $setProgress("BE", "BE030")
    scene Classroom with fade
    play music Peaceful
    #Setting: School. Science Room
    show BE sad with dissolve
    BE "So, explain this to me one more time, because, I'm just not getting it."
    "I couldn't help but sigh. Explaining something once was necessary. A second explanation could be useful for clarification. A third time would be seen as worrisome."
    "I was on the fifth explanation. At that point, it could also be my fault. Maybe I had to approach this in a different way."
    MC "Okay, look at it this way. Imagine all of these minerals are a variety of bad guys in a video game."
    MC "You know ahead of time that each one is weak to a specific combination of weapons. But they aren't named. So you need to figure out what they are."
    MC "All these tests we can do are like testing out the weapons on the minions of them we've captured ahead of time. So we can try one thing after another and make sure we know exactly what we have in our sights."
    "Honoka and I had a small tray in front of us. Twenty different minerals rested on it in five columns of four, numbered, with no other indicators of what they actually were."
    MC "So, we'll start with 1, for example. Now the first thing you look at it is color. But this is the... weakest option, I guess you'd say. Some minerals can be multiple colors. Quartz is like a mimic, it could be practically any color."
    MC "So then, you can look at the luster. Think of it as you're wanting to know if you need metal-piercing rounds for your weapon. It's either going to be metallic, or non-metallic. Or, basically, shiny or not-shiny."
    show BE neutral
    BE "Okay, got it. So this is not shiny, so it's non-metallic. And it also feels really weak. If that makes sense?"
    MC "It does! That could do with its hardness. See how your fingernail scratches the surface, that means it's very soft."
    MC "So we could tell the weapons engineers in our fictional video game to save some of the budget for the harder enemies. Er, minerals."
    "I continued to assist Honoka as we went down the list of different tests we could do, to narrow down what minerals we had here."
    show BE happy
    BE "I... think I'm actually getting it. Guh, somehow when you describe it, it actually sounds a lot simpler than I thought it was."
    MC "Well, hey. Geology can be tricky too. Like this here. "
    MC "This is kind of a gimme. Fool's gold, or pyrite. It's not like they're going to give us real gold to work with. There's a lot of obvious clues. The cube shape, the shine, the color, obviously. But, watch this."
    "Unable to hide my smirk, I took the gold chunk and rubbed it across the material given to us."
    MC "Black streak."
    BE "But... it's gold."
    MC "Yep. I don't know how to explain that one. But it helps prove it's pyrite. You don't need to do every test for all the minerals, but most of them will help you narrow it down."
    show BE neutral
    BE "That's cool. Okay. I think I've got a handle on this now. Thanks, Kei-chan."
    MC "I'll let you take it from here, then."
    "Honoka had asked me for help with this assignment, and I had been happy to do so. Though the only reason I'd known so much was from struggling with it myself early on..."
    show BE happy
    BE "And this one's shaped like, a diamond prism or something... so that would be this then. Yeah, that makes sense. Okay, I'm getting the hang of this."
    MC "Yeah, see? I knew you could do it yourself."
    "Honoka nodded and wrote down her answer, then moved onto the next one. I was working on an assignment myself. For the most part things stayed quiet, except for Honoka's occasional chattering."
    BE "Hehe."
    MC "What's up?"
    show BE neutral
    BE "Well, I'm having trouble figuring out this one. Can you take a look?"
    "I nodded and stepped over."
    MC "Which number is it?"
    show BE unique
    BE "Number 12."
    MC "Okay, so..."
    "I looked at the tray, but couldn't see a mineral in the twelfth spot. The number was missing as well."
    MC "I'm confused. Where is it?"
    "Honoka chuckled, bringing my gaze to her."
    "In the middle of her breasts was the missing mineral, the tiny chunk looking like it would be lost forever if it sank into the depths of her bosom. The paper with the number on it rested just below the mineral."
    show BE aroused
    BE "This cleavage is just so ridiculous, I can't figure out how it's so massive and full. Can you help me?"
    MC "Oh, Honoka..."
    MC "If you're trying to force me into a higher ranking on the Mohs Scale, it's definitely working."
    show BE happy
    BE "Hahaha! Good one, Kei-chan."
    "I reached forward, and gently plucked the piece out of her breasts, wagging it at her."
    MC "But science is no time for flirting!"
    show BE sad
    BE "Aw. That was clever, too."
    MC "Yes, it was. I'm rather proud of that. But I'll be prouder when you ace this assignment."
    show BE angry
    BE "Grrrr."
    show BE neutral
    BE "Just tryin' to have a little fun, is all."
    MC "Heh, I get that. But it's important to focus on the work. You don't want to lose your luster after all. "
    BE "Yeah, three puns is too many. Back to work."
    "I got back to my own assignment as well, until Honoka called me back over."
    show BE sad
    BE "Um, Kei-chan, I actually do need help with this last one."
    MC "Number 20?"
    show BE neutral
    BE "Yeah. It seems like it could be one of a bunch of things. Maybe a chunk of iron? It's shiny, it's like, medium hard, looks like it has some cleavage but it's not obvious where..."
    MC "Ah, hm. Let me take a look."
    if getSkill("Academics") > 9:
        MC "Ahhh, wait a second. I think I know what's going on here. Hm, where's the... ah, see, you forgot to grab something from the toolset."
        show BE surprised
        BE "I did? I got the coin, and the little tablet to do the streaks, and the nail."
        MC "Yep. One sec, I'll grab it."
        "I walked over to where the geology kits had been stored, and grabbed something off of the table. When I got back to Honoka, I kept it hidden in my hand."
        MC "Behold."
        "I dropped the item right above the specimen and watched as it clung to the mineral. Honoka's eyes widened in confusion."
        BE "You have gravity powers?"
        MC "Haha, no. Magnetism powers!"
        "I took the mineral and the magnet and separated them, then brought them together again. As the two items touched, there was a distinct click of the two getting magnetized."
        MC "It's easy to forget this one because not a lot of minerals are automatically magnetized. This is magnetite."
        show BE happy
        $setAffection("BE", 1)
        BE "Oh, darn. That's tricky then! Haha, you fixed it for me, though. You're so smart, Kei-chan."
        MC "Nah. It's just a lot of studying. This kind of stuff would trip me up a lot too without hitting the books. But now that you're caught up it'll be a piece of cake."
        BE "Heh, hopefully. Okay, let me just finish this up here and I'll be done, I think."
    else:
        MC "Hm. I don't really know what this one would be. You did all the tests for it, that you can find?"
        BE "Yeah."
        MC "So, hm."
        "Honoka had written down a few examples on her paper of what it could be. But they were all so similar in their attributes that it was hard to get it down to one specific mineral."
        MC "Well. I suppose you may just have to guess here. But you have your notes here, and proof that you did the tests. "
        MC "I'd say to just pick one of these three. With the work you showed you should still get partial credit. And everything else seems right, so you still will get enough to ace this paper for sure."
        BE "Hm, I guess that's the best option then. Okay, Kei-chan. Let me add a few things here, and I'll be done."
    "Honoka finished up her assignment and packed up the geology samples. I packed up my things as well, and helped her get everything back where it was supposed to go."
    show BE happy
    BE "Thank you for the help, Kei-chan. I really struggled there. But, yeah, it's a lot easier now."
    MC "It's amazing how changing the context of something makes it easier to understand, huh?"
    BE "It does. But now I just want to play some video games. The last one I was playing, I think I screwed up the order of my research, and now the aliens are way ahead of me in what technology they can create."
    MC "Yeah, I can't help you there."
    show BE neutral
    BE "Well, maybe if I think about it in geology terms, I can figure it out..."
    MC "I think you might just be better off with restarting your save and save-scumming."
    show BE sad
    BE "Aw, phooey."
    jump daymenu

label BE030:
    $setProgress("BE", "BE031")
    $lockRoute("BE")
    scene School Planter with fade
    play music Hallway
    "As usual, there was only a certain amount of time I could handle Daichi before I felt the need to escape my room. Maybe 'escape' was a strong word."
    "It certainly wasn't one I would ever use around him, or else he might think I was so invested about his theories on Seichou Academy that I wanted to flee."
    "That certainly wasn't the case, not when it had been made clear multiple times that it'd been helpful for me and others. Not to mention I had people I considered friends here."
    "The weather as I stepped outside was warmer than I expected. Not so hot as to make me miserable, but enough to make staying still for too long seem like a bad idea."
    "Still, I thought it would be nice to spend some time walking around the campus for a while. "
    "I decided to make my first stop by the garden area, figuring that the sunlight would make the blooming plants look particularly pretty."
    "I just about felt the sun starting to bake my skin a little. It was relieved by a breeze that rolled against me and brushed my hair back."
    "I didn't consider myself a botanist by any means, but the flowers did look splendid. Naomi was doing a good job, it seemed. I'd have to compliment her the next time I ran into her."
    "It would have to wait though, because not long after I reached the garden, someone ran into me instead."
    "By now I was able to recognize who it was simply by the way her breasts pushed into my back. Like a pillow fight was about to break out right behind me, and I was the first casualty. At least it would have been a nice way to go."
    MC "Hey, Honoka."
    show BE happy with dissolve
    BE "Helloooo Kei-chan! What are you up to?"
    MC "Honestly, not much. Was just kind of killing time, strolling around. Did you want to do something? I'm free."
    BE "Sounds good, I was hoping you'd say something like that. Wanted to hang out, and you're my go-to hanging-out person."
    MC "I'm flattered you think so highly of me."
    "Honoka giggled, and took my hand. I eagerly squeezed her fingers in return."
    show BE neutral
    BE "Do you want to just, walk around for a while or something?"
    MC "Sure, I didn't really have any plans. I was just looking at the flowers. You don't have any zany ideas for how to spend the day?"
    BE "I don't always have some zany plot. You make me sound like some thrill-seeking anime heroine."
    MC "...Are you not?"
    show BE happy
    BE "Haha. No. I don't have the purple eyes or the blue hair or a wicked scar."
    MC "No, I guess not. You do have the boobs though. You can't be the main character of an anime without big boobs."
    show BE neutral
    BE "Hmm. But would an anime character with breasts as big as mine be able to do any fighting? No sense being the heroine if you can't kick butt."
    MC "I'm sure you could. I can only withstand your boob-airbag attacks because I've built up resistance to them. If you smash into someone not used to it, you'll knock them right over."
    show BE unique
    BE "Breast ballistics. I like it."
    MC "Haha, of course you would."
    "We kept strolling by the gorgeous agriculture of Seichou. It really was pretty. Far nicer than they needed to make it, considering the cost it took to deal with all the growing students."
    MC "So, how's everything going with you, grades all right and everything?"
    show BE neutral
    BE "Yeah, that's not a problem. Least, I hope it's not. Would hate to take a test soon and totally flake on it. "
    show BE sad
    BE "You know that feeling you get sometimes where it seems something's really easy, but when it comes time to actually do it, all of a sudden the difficulty shoots up?"
    MC "Yeah, more than you know."
    show BE neutral
    BE "Good, so it's not just me. When you help me study it does help. But even still, there's some tests where I'm all ready, and then I sit down to take it..."
    show BE sad
    BE "My brain just goes splat, thud, poof. Like a magic trick."
    MC "Well hey, I'm always free to study with you. I'm not the smartest brick in the wall myself but I'll always help."
    show BE happy
    BE "Aw, you're so sweet, Kei-chan. May have to take you up on that! We'll have to skip an arcade trip or two though, I'm sure."
    MC "Well, we can always relax after a good study session with something fun in our rooms instead. Makes things simpler."
    BE "Yeah, but, arcades are just so much more fun. Especially when I've got you with me."
    "Honoka rubbed her fingers along mine as we strolled along. No destination in mind, just meandering for the sake of staying in motion. The temperature was just perfect for such a casual stroll."
    "Something about Honoka's hand felt extra soft today. The way her fingers squeezed my hand was comforting. With the gentlest bit of heat coming down on us, her lazy touch was soothing."
    "She even smelled super nice. I never knew if she wore perfume or not, but she'd done something today. Maybe it was just a new shampoo or soap, but the aroma was intoxicating."
    "We soon found ourselves strolling closer to the outer gates of the academy, where the sounds of other students grew further away until we couldn't even hear them."
    show BE neutral
    BE "Ah, this school really is pretty. We lucked out coming here, didn't we, Kei-chan?"
    MC "Did we? I mean, the location's nice. But, the reason for us being here feels like it takes away from that a bit."
    show BE sad
    BE "Sure, I guess."
    show BE happy
    BE "But if we hadn't come here, we wouldn't have learned what was going on with us in a safe environment."
    BE "We wouldn't have met a bunch of new friends."
    show BE sad
    BE "I wouldn't have been able to meet you again..."
    MC "Oh, you, you would have been fine without me."
    show BE happy
    BE "Don't kid yourself, Kei-chan. Without you I wouldn't have had nearly as much fun here."
    BE "Stuff's just better when you're around."
    MC "You've... wow, you've really got a way with words sometimes, you know that?"
    show BE neutral
    BE "I do."
    "The two of us found ourselves at a familiar little spring, standing at a bridge that crossed the flowing water. We both stared into it, resting on the arch of the bridge."
    "It was quiet. Which by itself wasn't a bad thing. It really helped me appreciate the stillness of the lake. I rested my arms against the wood and leaned forward, watching the serene scene."
    "Eventually a dragonfly stopped by and broke the surface of the water, sending a faint ripple across the water until the waves ceased."
    MC "It's funny. I don't think the two of us have been back here since the first day of school."
    show BE surprised
    BE "We haven't?"
    MC "Nope. It's usually been the arcade, or one of our dorms, or at a club or something."
    show BE neutral
    BE "Yeah, I guess you're right."
    MC "Though, it doesn't matter where we are. I'm always happier around you."
    show BE happy
    BE "Oh is that so?"
    MC "Yes, but not for that reason. You're just so easy to talk to, Honoka."
    MC "We met back up after years and it was just like we'd never left each other. That's not the kind of relationship you have with anyone."
    MC "Thinking about all the stuff we do together, and then thinking about doing it myself, it's just not as fun."
    BE "I know. I'm pretty great."
    if getVar("BEFeminine") > getVar("BETomboy"):
        jump BE030_feminine
    elif getVar("BETomboy") > getVar("BEFeminine"):
        jump BE030_tomboy
    else:
        jump BE030_neutral

label BE030_feminine:
    BE "Gorgeous, too."
    MC "Yeah..."
    "I turned towards Honoka. Her hands were trapped under her bosom, pinning them to the railing. I gently slid my hands under her chest to hold her hands."
    MC "You know, you're more gorgeous than you think you are."
    show BE surprised
    BE "Eh?"
    MC "It's not easy being as upbeat as you are all the time. That's a very rare, and enviable quality. It's rare to meet someone who can light up a room just by walking into it."
    show BE happy
    BE "Ah, heh, well..."
    MC "Even rarer to find someone that radiant who's also stunningly beautiful."
    show BE surprised
    BE "I mean, s-stunning..."
    "I brought her hands up closer, bringing them between our chests."
    MC "That really is something special that you don't want to let go."
    MC "Do you remember when we played that cheesy love tester machine in the arcade?"
    MC "It doesn't matter what it said. None of the options it displayed matched what I really felt."
    MC "I think it was that moment I knew what I felt was real, Honoka. By all rights our hands squeezing those levers should have made the machine explode."
    BE "..."
    MC "You've gone through a lot since coming here, Honoka. A lot of clubs, a lot of bras, a lot of chocolates. Nothing you've done, or ever will do, is going to make me feel differently about you."
    MC "Honoka, I don't want to go a day without being able to feel your touch. I want to stay with you and watch you blossom further, into the beautiful young woman you are."
    MC "I want both of us to be the happiest we can be, and I think the easiest way to do that is for us to be together."
    MC "I love you, Honoka."
    "There was an emotion on Honoka's face I had never seen before. Her cheeks were hot red, and her eyes were glimmering with all the moisture refusing to leak down her cheeks."
    "She tried to speak, but her throat gave her issues, letting out nothing more than loud exhalations."
    "Once I pressed my lips against hers, she was better able to express herself, by making a delighted, warm, satisfied moan as she returned the kiss."
    "Our arms wrapped around one another as I leaned back against the arch of the bridge. Honoka stood on her tiptoes and pressed her lips more firmly into mine."
    "The peace of the brook, the warmth of her body against mine, the utter elation of my heart pounding like a hummingbird's wings. It felt beyond comparison."
    "Breaking the kiss was the hardest thing I'd had to do. Watching her lower herself back to standing on her soles, it felt like we'd both entered a new chapter of our lives together."
    "Honoka brought up a hand and carefully wiped away the joyful tears from the corners of her eyes, before holding my hands again."
    show BE neutral
    BE "W-Wow. I, I love you too."
    show BE happy
    BE "You've really got a way with words sometimes, you know that?"
    "I smiled, saying two words before leaning into to kiss her again."
    MC "I do."
    jump daymenu

label BE030_tomboy:
    show BE happy
    BE "Awesome, too."
    MC "Yeah."
    "I turned towards Honoka. She leaned against the bridge's side, with her arms crossed underneath her chest. I walked behind her, and slid my hands around her waist, then rested my head on her shoulder."
    MC "You know, you're more awesome than you think you are."
    show BE surprised
    BE "Huh?"
    MC "I've yet to see something keep you down for long. You're always trying new things. And if it doesn't work out you just pick yourself on and move to the next. It's hard to do that, to keep pushing yourself forward."
    show BE happy
    BE "Aw, shucks, Kei-chan."
    MC "And to have all that, and still be drop-dead hot... that's a hell of a feat."
    show BE surprised
    BE "Hot? Y-Yeah, I guess, heh..."
    "I grasped her hands from underneath her chest, not caring about my thumbs pushing into the underside of her breasts."
    MC "It's a great package. It makes me want to make sure I never lose you."
    MC "Do you remember when we played that goofy love tester machine in the arcade?"
    MC "I remembered looking at it, and thinking 'none of these seem right... it needs to go higher'."
    MC "We shouldn't have even needed to touch the sensors for the machine to go off, Honoka. I think just being next to it should have fried the device."
    BE "..."
    MC "Despite everything you've gone through since coming here, you're still that amazing girl I was best friends with all those years ago. The goofy, sporty gal with enough spunk to last a dozen lifetimes."
    MC "That's never going to change, I'll always admire that."
    MC "Honoka, I don't want there to be a day where you and I aren't together. Your energy is addictive, and I just can't get enough."
    MC "I know we've been dating, but I need you to know that this is serious for me. Boyfriend and girlfriend, and in the future, something more. "
    MC "I love you, Honoka."
    "From my position, I couldn't see Honoka's reaction. I was dying to know, so my arms flipped her around until we were face to face."
    "Her hand went up to her throat, as she struggled to find the words. Her mouth opened a few times, but nothing came out."
    "I kissed her, pressing my lips deeply into hers, and pushing myself into her bosom as far as I could go. I felt the tension in her body melt away as she kissed me back."
    "She wrapped her arms around me, and I squeezed harder into her. With a bit of effort, Honoka's butt was raised onto the bridge railing, and we continued kissing."
    "Everything seemed to go numb except for the kiss, and the sensation of my body against Honoka's. The sounds of nature faded away until all I heard was her breath and her heartbeat. It felt like my pulse matched hers."
    "I felt out of breath by the time I stopped the kiss. We both stood there, taking deep breaths, panting with emotion and lust."
    "Honoka coughed a few times, breaking the hard knot in her throat that formed when she tried to reply to me earlier."
    show BE neutral
    BE "Damn... I love you too."
    show BE happy
    BE "You've really got a way with words sometimes, you know that?"
    "I smiled, saying two words before leaning into to kiss her again."
    MC "I do."
    jump daymenu

label BE030_neutral:
    MC "Yeah."
    "I turned towards Honoka. I placed my hand on her shoulder, and took a deep breath, trying to come up with the right words to say."
    MC "You're not just great, you know."
    show BE surprised
    BE "I'm not?"
    MC "You're great, yes. You're also pretty, fun, adventurous, clever, hard-working, kind and helpful. It should be illegal to have so many good qualities all at once, you're leeching them from the rest of us."
    show BE happy
    BE "Hehe, thanks, Kei-chan."
    MC "Seriously, to think you're dating me is nuts. How did I score such a babe?"
    show BE surprised
    BE "Ooh, a babe?"
    "I let go of her shoulder, and she slowly turned to face me. She must have sensed that I had more to say."
    MC "I feel so lucky to have you, Honoka. Beyond reason."
    MC "Do you remember when we played that silly love tester machine in the arcade?"
    MC "It felt fun at first, but when we held our hands and squeezed those levels, something didn't feel right. But for a good reason."
    MC "Thinking we needed a machine to decide how much we love each other was foolish. I think it's obvious I'm head over heels for you, and I think you're the same for me."
    BE "..."
    MC "I get the feeling that you've been having some trouble figuring things out, Honoka. But, that's okay. The fact you still get up every day, and push through with a smile and a joke is proof that you're doing great."
    MC "I want to be there for you as much as possible. To help you, or just be there when you need it, like you've been there for me so many times."
    MC "I want to take the next step forward. And I think it's been a long time coming. You deserved to hear this ages ago."
    MC "I love you, Honoka."
    "Honoka's mouth dropped open, and her fingers gently brushed against her lips for a moment."
    "She nodded rapidly in reciprocation, sniffling already as emotions welled up within her. Good ones, I assumed, judging by her reaction."
    "The second her mouth wasn't covered, I moved in for a kiss, grasping her hand in both of mine and pulling her in tight for a deep, loving smooch."
    "Her free hand grabbed my waist and pulled me in close. My chest bumped into one of her breasts, and it cascaded into my torso as I leaned in further."
    "This felt right. Like a puzzle with one piece missing, this was something that had to be done for both of us. She tasted sweet, her hands were soft, and her body was warm. I felt deeper in love already."
    "The kiss broke mutually as we split apart, with me still holding her hand. I let go with one, and gently rubbed her cheek."
    "Honoka leaned into my touch, smiling warmly and looking back up at me. Nothing could have made this better."
    show BE neutral
    BE "Gosh. I love you too."
    show BE happy
    BE "You've really got a way with words sometimes, you know that?"
    "I smiled, saying two words before leaning into to kiss her again."
    MC "I do."
    jump daymenu

label BE031:
    $setProgress("BE", "BE032")
    scene Dorm Exterior with fade
    play music Hallway
    "I'm not quite sure what Honoka had planned for us tonight. She had told me it would be a surprise, but didn't even indicate if she wanted to go out, or stay in."
    "I was fine with both choices, but knowing Honoka, she probably just forgot to tell me if it was one or the other."
    "Either way, whichever she wanted to do, I couldn't deny her. If she wanted to go to the arcade, to dinner, or watch anime inside. It was nearly impossible to say no to that face of hers."
    "She had told me to meet her at her dorm room, so that's where I went. It was fairly late in the day, so there wasn't much foot traffic to be had in the dormitories."
    "In general it was fairly quiet, with just the low buzz of fluorescent lights making most of the noise."
    "It hadn't crossed into nighttime yet, so I didn't get any odd looks from the few girls I passed by as I made my way to Honoka's room. Room 08 on this floor."
    "As I approached the door I noticed a small sticky note to the left of the room number, with '80' scribbled on it."
    play sound Knock
    MC "Honoka?"
    "I stood there for a moment and waited for an answer."
    MC "Honoka?"
    BE "Sorry! Just a sec. Dang socks all over the place. Coming!"
    #[SFX- Door_Open]
    show BE neutral with dissolve
    "A few seconds later, Honoka opened the door. We greeted each other, but as I looked at Honoka, something was different. I couldn't quite put my finger on it."
    MC "So, what's the plan for tonight?"
    show BE surprised
    BE "Plan?"
    "Honoka blinked, looking slightly confused. I still struggled to figure out what was different about her. Her hair was the same. Her boobs might have been bigger, but that was hard to catch at first glance. What was it?"
    MC "Yeah, you said you wanted to hang out tonight. To meet you here?"
    show BE neutral
    BE "Right. We're not going anywhere though."
    MC "Oh! You just want to chill and watch a movie?"
    stop music
    "Honoka peered her head outside her door and looked down the hallway, twice on both sides, before grabbing my hand and yanking me inside."
    #[Effect- Screen Shake (1 time, low intensity)]

    scene Dorm BE with hpunch
    show BE surprised
    #[Transition- wipe][(S)Or other  fast  transition, I'm not sure what options we have?]
    play music Steamy
    "Being unprepared for such an act, I was caught off-balance. My feet tripped over each other, and I began fumbling towards Honoka's chest."
    "She luckily reached out to grab me, preventing me from falling onto the floor, and ensuring I fell right onto her bust instead."
    "That, while nice as it always was, gave me the final clue to figuring out what was different about Honoka."
    "She was wearing a black bra."
    "I hadn't kept tabs on what color bra she wore on a day-to-day basis. Typically whatever bra she had was hidden by her shirt, and it wasn't easy to tell the color. But the black she wore now stood out against the white of her uniform top."
    show BE aroused
    BE "Heh, don't get started, yet, Kei-chan. Let me lock the door first."
    "Honoka helped me up, and giggled to herself as she made her way to the door. She locked it and gave it a firm tug for good measure."
    show BE happy
    BE "Okay!"
    MC "What's up, Honoka? My brain is thinking things."
    BE "Heh, that's what brains doooo, Kei-chan."
    MC "I know, but, you brought me to your room, after school hours, and you locked the door. Plus you're wearing a, um..."
    show BE neutral
    BE "Wearing my school uniform? I know, I couldn't think of anything else to wear."
    MC "No, I mean, the bra, I can see it."
    show BE aroused
    BE "Yeah, sure, you can!"
    "Honoka smiled and grabbed the top button on her shirt."
    MC "Wait, wait, I said 'I can' see your bra. Not 'can I' see your bra."
    "Honoka looked visibly confused."
    show BE sad
    BE "But, you're going to anyway, right? Don't you want to? It's going to be hard if I keep my shirt on."
    "Finally, I sat down in a chair, and Honoka approached, blushing. The gears in my head turned, creaking and cranking, but finally started putting the pieces together."
    MC "You... want to do... that?"
    BE "Do you not?"
    "Honoka's hands still lingered on the buttons of her uniform's top. The button undid itself without her seeming to notice, exposing another solid inch or more of that succulent, enticing cleavage."
    BE "I didn't think we were moving too fast. But if you want to slow down, it's okay too."
    menu:
        "No, I'm excited. I was just caught off-guard.": #+1
            jump BE031_c1_1
        "Of course I want to. I'm just flustered you had to be so forward about it. That's my job.": #+2
            jump BE031_c1_2
        "Maybe we should take it slower. Why don't we just make out, and see where it goes from there?":
            jump BE031_c1_3

label BE031_c1_1:
    MC "No, I'm excited. I was just caught off-guard. If you'd told me ahead of time, I'd have been more prepared. I feel like I should have brought chocolate or something."
    show BE happy
    BE "I mean. I wouldn't have been opposed to chocolate."
    $setAffection("BE", 1)
    "Honoka snickered and licked her lips a bit."
    BE "But, I guess I wanted this to be a surprise. A treat, kind of. So telling you ahead of time would ruin it."
    MC "That's fair, I guess. But, I, ah, wow. The idea of, of, of..."
    show BE unique
    BE "Getting a boobjob from your girlfriend?"
    "Honoka smiled and lifted up her boobs as another button was undone on her uniform. It was like a countdown to a rocket launch, and the explosion left in its wake would be one to remember."
    MC "Yeah."
    BE "You can't tell me you haven't thought about it before. Fantasized. Not with how many times you've run into them."
    "Another button came undone, less than half remained. I could now see the edges of her bra peeking past the confines of her shirt. It was haunting, and slightly terrifying as well."
    "I also didn't have the heart to tell her that most of my chest collisions had been her fault."
    jump BE031_c1_after

label BE031_c1_2:
    MC "Of course I want to. I'm just flustered you had to be so forward about it. That's my job. I feel I should have been the one to initiate this."
    show BE happy
    BE "Hey, we're a couple, that means we need to be equal about things, right?"
    MC "That makes sense."
    "At her behest, Honoka grabbed the center of her shirt and undid another button on her top, releasing more breastflesh unto the world."
    "Every inch that revealed itself just made it more obvious how blasphemous it was that Honoka had to cover up her boobs so much."
    MC "So, what can I do to make this more equal?"
    "Honoka paused for a moment, and tapped her chin with her finger. With a grin, she then reached down, and gently placed her hand on my trousers. With a deft flick of her wrist, my belt came undone, and slid out to fall upon the floor."
    MC "Y-Yeah that's a good start."
    "My hands reached up, to caress Honoka's boobs. If we were being equal, she'd just undone part of my pants. It was only fair I undid the next button. It felt like unlocking one of the padlocks to a bank vault."
    show BE aroused
    $setAffection("BE", 2)
    BE "Heh, are you sure you haven't done this before?"
    MC "Buttons I can do."
    "Honoka's hands went to the top of my pants and undid the button on top."
    BE "As can I."
    MC "It's your bra I'm going to have trouble with."
    "Honoka smiled as she placed a finger down her cleavage, stopping at the clasp on her bra."
    show BE unique
    BE "Well, I'll handle that."
    jump BE031_c1_after

label BE031_c1_3:
    MC "Maybe we should take it slower. Why don't we just make out, and see where it goes from there?"
    show BE happy
    BE "Sure, I'm okay with that. But, you don't get to move from your seat."
    MC "Yeah. I'm okay with that, too."
    "There was only a brief second before Honoka was sitting on my lap, the weight of her body pressing down on me. Thankfully I was seated in a comfortable position, or I would have lost control far too quickly."
    "Honoka's lips pressed against mine, and as always, I savored that touch of her mouth against mine."
    "Those soft, sweet kissers always knew just when to be tender, or when to get more forceful. She hadn't slipped any tongue yet, so I waited a bit before going that far."
    "Sometimes, when Honoka had hit the vending machine, her lips still tasted like chocolate. This time there was a faint bit of mint, instead. I blushed, hoping my breath wasn't bad, but she didn't show any sign of it being distasteful."
    "Eventually, I let my tongue slide between her lips, and at the same time, she grasped my hands and pulled them up to her bosom."
    "No matter how many times I felt those mounds of dough between my hands, the sensation never got boring. I prayed that it never would."
    "As we made out, Honoka undid two more buttons on her top. I kept my grip on the sides, and sometimes the bottoms of her boobs, feeling them overflow my hands."
    "There was just so much to them, that I couldn't imagine how they'd feel when they were bared."
    show BE aroused
    BE "So."
    "Honoka stared knowingly at me. She'd been sitting on me the whole time. She knew how hard I was."
    show BE unique
    BE "You ready?"
    MC "Yes, definitely."
    jump BE031_c1_after

label BE031_c1_after:
    "As if she wanted to better present herself, Honoka moved until she stood three feet away from where I sat, hands clasped at her shirt."
    "Another button undid itself, and the pillows of flesh that tried to escape looked like someone had overfilled cake tins."
    "My mouth went dry thinking about what hid behind the fifth button, and the bra beneath. I begged my mind not to overthink it. I didn't want expectations, whether they be exceeded or not. I just wanted to see them."
    "Honoka let out the cutest groan as the last button was undone, and her shirt soon hit the floor afterwards. I was pretty sure I made a whimpering sound, like a puppy that saw a treat held just out of its reach."
    show cg BE031 with dissolve
    BE "Well. This is it. Or, rather. These are them."
    "Honoka undid the clasp of her bra as quickly as she could. Rather than letting it fall, she carefully placed it aside, before standing up straight to let me get the best view of her breasts."
    "My hand went up to my mouth in shock. I knew they were big. I'd felt them."
    "But seeing them naked, it was better than I could have dreamed. They were perfect, rounded teardrop shapes. Huge spheres that hung on her torso and somehow still remained perky despite their massive size."
    "I couldn't see a single sign of imperfection on the skin. Just immaculate, soft flesh that had been expertly taken care of."
    "I wouldn't've doubted that she'd applied lotion or oil on them ahead of time to make them look even better. But, maybe they just looked that grand constantly."
    "While I'd seen parts of her boobs before, this was the first time I saw her nipples, and they were great to look at as well."
    "Firm and erect, pointing at me and begging me to take hold of them. Honoka moved closer, the slightest motions making her rack wobble up and down."
    "With her bosom up closer to my face, I could even see the soft bumps of her areolae, and how my exhalation against her skin made more goosebumps appear."
    "Honoka's body shivered as I looked up at her, past what seemed like a mile of cleavage just to see her smiling visage."
    "There was a thwump, and suddenly my lap overflowed with Honoka's breasts. Her hands worked magic underneath them, as her fingers found what they needed to, in order to get my pants fully undone."
    "A quick lift of my backside and soon I was completely bottomless."
    "Honoka was totally topless. It was a scenario I'd dreamed of, but wasn't sure would ever happen in reality. But here it was. My penis throbbed less than a centimeter away from the entrance to her smothering melons."
    "Honoka and I looked at each other, our eyes glimmering, breath haggard, hands shaky. Hers rested as well as they could at the sides of each boob, unsteady and unsure. But willing, at the very least."
    "I placed my hands upon hers, and smiled as our fingers clasped. With a deep breath, Honoka pushed herself forward, intent on covering as much of my erection as she could with her breasts."
    "She didn't need to do much to have it completely engulfed in seconds."
    "The feeling was immaculate. Better than I could have imagined, and she hadn't even begun to stroke it yet."
    "Just the way that her breasts covered every bit of my shaft sent shivers down my spine. When she began moving her breasts, I felt myself twitch immediately."
    "I bit down gently on my knuckles to stifle the sensation as best as I could, letting go of Honoka's hands now that she had taken control. Watching her work, I could have sworn she'd practiced this somehow."
    "Each hand knew just what to do, moving a breast in a circular motion. Clockwise for a while, then the opposite way, letting my penis rub around the sensitive insides of her bosom."
    "The sounds coming out of my mouth were embarrassing, but Honoka paid them no mind."
    "The look on her face was a mix of determination and lust. Her tongue slightly stuck out from between her lips as her body moved back and forth with the motions of her boobs."
    "It was two tidal waves of titflesh, and Honoka was trying not to get swept up in the tsunami."
    "But it was clear that, for as amazing as it felt for me, Honoka was enjoying herself as well. The redness on her cheeks and the cute panting said it all."
    "Her hands soon switched, and moved from being on the sides of her rack to being on top. She pressed down on her own breasts, flattening them a bit until the tip of my erection poked out for a brief second."
    "She let her breasts return to a rounded shape, and then pressed again."
    "Honoka's hands then moved to the bottoms of her boobs as fast as they could and lifted them up, so high that I couldn't see her face at the apex."
    "Then as they swung back down on my lap, she pressed on them. She repeated this motion over and over, making me shudder every time."
    "It was incredible. I wanted to do something. Anything to repay her for this right now. But my arms were useless noodles. All the blood in my head was gone, rushed down south for more important matters."
    "When this began, I thought I could last for ages. I just wanted to let myself rest in Honoka's boobs eternally. But I underestimated how sensual it felt. I could sense the inevitable coming, and had to at least summon some strength to let her know."
    "I don't know how long it was when I finally had to pat on her boobs as fast as I could to let her know what was going on. But those minutes had been, without a doubt, marvelous."
    "I gulped as I heard Honoka's pants reach a fever pitch, and she kept building up speed as she returned her hands to the sides."
    show cg BE031b with dissolve
    "With her vigor renewed, I stood no chance. As soon as the first sound of a grunt left my throat, Honoka squeezed her boobs as tightly together as she could, and I came all over the inside of her cleavage."
    "With how much there was, it was like trying to coat a barn with a few teaspoons of paint."
    "The ceiling of Honoka's room was blue. I hadn't noticed it before. But with my head hung back on the chair, it was all I could see for a while."
    "My head was dizzy and the color was the only thing my blurred vision could recognize. Vaguely, I grew worried about the mess I made."
    MC "H-Honoka..."
    "I finally found my voice, as weak and groggy as it was. With a gulp, and the arms of the chair, I straightened my posture to look at Honoka. God, she was gorgeous."
    hide cg
    stop music
    "Even sporty, peppy Honoka seemed somewhat exhausted after the workout she'd given herself, and I couldn't blame her."
    show BE aroused with dissolve
    BE "It, heh, it was good, right?"
    "The thought that Honoka could be unsure about such a thing was a travesty to me."
    MC "Honoka, it was perfect. I don't even know how to describe how good that felt."
    show BE happy
    BE "Really?"
    MC "Of course."
    "Honoka smiled, and gave what might have been one of the most pleasant, cheerful laughs I'd ever heard from her."
    BE "I'm glad, Kei-chan. I'm so glad."
    "Honoka looked down at her boobs, with her eyes closed."
    show BE angry
    BE "It's not that I hate my boobs or anything. But, knowing that you love them so much, it really makes it easier to handle."
    MC "Hey."
    "Honoka looked up, just in time for my lips to meet hers."
    show cg BE031c with dissolve
    pause 2
    "She kissed me back for a few seconds before I broke it, and put my hands on her shoulders."
    show BE happy
    hide cg with dissolve
    MC "Remember this, Honoka. I don't love your boobs. I love you."
    BE "Oh, g-gee, Kei-chan... I love you too."
    jump daymenu

label BE032:
    $setSize(3)
    $setTimeFlag("size3")
    $setProgress("BE", "BE033")
    scene Classroom with fade
    "I didn't get to sleep right away the previous night. How could I? Even an hour after Honoka's boobjob, I felt flushed and excited. We didn't know what to do with ourselves."
    "Honoka took some time to clean up, as did I. Then we spent a bit more time together, watching television. It wasn't awkward, per se, but we kept looking back at each other the whole time."
    "Maybe we just wanted to go for another round, but I hadn't been sure that my heart could take it."
    MC "Wonder where she is."
    "Honoka wasn't in class yet, but it started shortly. I brushed a strand of hair out of my eyes and pushed it behind my ears. I really needed a trim."
    show BE happy with dissolve
    play music BE
    BE "Goood morning, everybody!"
    "Honoka bounced her way into class, giving a giddy smile to everyone as she passed by. She stopped over by me and crouched down, just enough so that her breasts flopped onto my desk."
    BE "And especially good morning, Kei-chan!"
    "She brought an index finger forward and booped me on the nose, making me blush. Honoka snickered and pushed her elbows into her bosom, using her palms to support her cheeks."
    BE "I had a lot of fun last night."
    MC "Yeah, me too."
    BE "Hehehe, I'm so glad."
    "Honoka's finger left my finger, and moved up to my hair, moving another strand of it behind my ear. She giggled, and ran her palm along my cheek."
    BE "Your hair's so shaggy. I like it."
    show BE happy at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show AE neutral at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    AE "Inoue-san, class is about to begin. It would be prudent for you to return to your seat."
    "Shiori had stood up and trotted over to the opposite side of my desk. She pressed her glasses further up her nose and crossed her arms together."
    show BE neutral
    BE "Aw, don't be such a spoilsport, Shiori-chan. I'm just talking to Kei-chan."
    MC "Yeah, there's no problem. Class hasn't started yet."
    "Shiori tapped the side of her temple and rubbed it in a small circle with her eyes closed."
    AE "Indeed, but what I mean is that the two of you are... oddly close today."
    AE "In addition, Inoue-san is acting odd. Her giddiness is through the roof, her pupils are dilated, and her sense of personal space is even smaller than normal."
    show AE neutral-annoyed
    AE "What's going on?"
    show BE angry
    BE "Jeez, can't a girl just be happy without being called cuckoo?"
    MC "Yeah, it's fine, Shiori-san. Honoka and I just had fun last night and I think we're still riding the high."
    "I swore I saw Shiori's glasses glimmer as her jaw slowly slackened."
    show AE angry
    AE "{i}What{/i} did you just say?"
    "Honoka and I stiffened as a cold chill overcame us."
    AE "I'm sorry, but I think I misheard you-"
    MC "Whoa, whoa, no no no. Not at all!"
    AE "Oh, so I didn't?"
    MC "N-Not like that! It's just an expression!"
    show BE happy
    BE "Yeah, it's just an expression, Shiori-chan. Take a chill pill."
    AE "That was {i}terrible{/i} wording on your behalf. Unless, of course, it was a Freudian slip."
    MC "Again, it's an expression. Are you all right, Shiori-san? You're acting a bit more wound up than usual."
    show AE neutral
    AE "I'm just fine, thank you, but if the two of you are doing something against the rules, {i}I{/i} need to know what's going on."
    BE "Well you don't have to worry about us, class rep. Kei-chan and I are fine. We're making sure we stay safe."
    MC "Right."
    AE "Well that's good to hear. But..."
    AE "Staying safe?"
    AE "..."
    "Shiori stopped herself, and stood up straight again. She looked between me and Honoka, and made a small, noncommittal sound."
    AE "Hm."
    AE "I see. Well... I'll trust you."
    AE "But."
    show AE angry
    AE "Regardless, the two of you should act responsibly."
    AE "If not, I'll have your hide."
    hide AE with dissolve
    "With that, Shiori turned around and walked away, her rump shaking to and fro as she did."
    show BE neutral at center with dissolve
    BE "Ahh, I see. She might make good on that threat. Clearly she's been taking everyone's butts and simply adding them to her own."
    "I couldn't help but snicker at that."
    MC "As long as she doesn't go for your chest, I don't mind losing my own."
    show BE happy
    BE "Please, I've got more than she can handle. Especially now."
    MC "What do you mean, especially?"
    BE "Oh, can't you tell, Kei-chan? Why do you think I'm extra happy today?"
    "Honoka leaned in, letting her boobs glide over my hands and cover them completely."
    show BE aroused
    BE "I really thought you'd be able to figure it out, considering how... up close and personal you got with them last night."
    "Flustered, I tried to pull my hands back. Honoka simply pushed down more insistently, until my palms were flat on the desk."
    show BE unique
    show cg BE032
    BE "My boobs got bigger. You know that bra I wore last night? I was already close to outsizing it. When I went to put it on today, I couldn't close the clasps."
    "I gulped."
    hide cg
    BE "But I didn't have any time to get a new one, you see. So, fun fact, Kei-chan, I'm going braless today. I'll have to get a new one later. But for now, oof, my yummy, full breasts are just hanging free~"
    MC "Ahaha... well, that really is some fun news."
    "With a bit of effort, I flipped my hands over from underneath her breasts. Soon my palms were directly touching the large curves of Honoka's chest, and I pushed upwards."
    MC "I suppose I could always act as your bra for the time being, if they really start to ache on your back."
    show BE happy
    BE "Fufufu. Don't tempt me, Kei-chan, or I'll make sure I never wear a bra ever again."
    MC "Now I'm confused as to how that's meant to be a threat in any way."
    "Honoka just laughed again, and gave me a smug grin."
    BE "Because, Kei-chan."
    show BE unique
    BE "How in the world would you ever focus with these beauties you love constantly pressing into you? You'd never get any other work done."
    MC "Maybe I don't want to get work done. Maybe I just want you."
    show BE happy
    BE "Well, then, maybe we'll need to have a repeat of last night soon."
    MC "I wouldn't be opposed to that..."
    "A chill suddenly ran down my back. I couldn't figure out where it came from. But as I looked to the other side of the classroom, I saw Shiori's cold, steely stare focus in our direction."
    MC "Ah, b-but, maybe now would be a good time to sit down so Tashi-sensei doesn't call you out for not being in your seat."
    show BE neutral
    BE "Good idea, Kei-chan. Need a bit to calm down, anyway."
    "I could tell what she  meant by the large indentations in her white shirt. Her nipples were poking out obscenely into the fabric, aimed at the opposite wall."
    "Honoka lifted up her chest and winked, before she moved back over to her desk. She may have been right, having such breasts in my hand would be a major distraction."
    "But like hell was I going to be able to think about anything else for a while, regardless!"
    jump daymenu


label BE033:
    $setProgress("BE", "BE034")
    scene School Planter with fade
    play music Schoolday
    "Honoka and I were enjoying the cooler weather outside. The sky was clear, and the air was crisp, making it comfy to walk around the campus."
    show BE happy at Position(xpos=0.7, xanchor=0.5, yanchor=1.0) with dissolve
    BE "...and so that's why I don't mix every single flavor in soda machines anymore."
    MC "Well, if you went to a normal one, maybe it'd be fine. But, why would you have tried it at one of those that have over a hundred options?"
    BE "For the same reason that people climb Mt. Fuji, duh!"
    MC "Because it's hazardous to their health?"
    show BE neutral
    BE "Exactly."
    MC "I don't agree with you. But I still love you."
    show BE happy
    BE "Hehe, I love you too. Oh hey, what's Shiori-chan up to?"
    "Honoka skipped over to Shiori, who had seated herself on the grass, the girth of her backside being on ready display as she crossed her legs. Honoka sat down next to her."
    BE "Yo, Shiori-chan, what's up?"
    show AE neutral at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    "Shiori took a moment to answer. On the ground in front of her was a flattened slab of cardboard and some spray paint. She leaned in very close with an extremely fine paintbrush and dabbed a section of the item too small for me to notice."
    show AE neutral at Transform(xzoom=-1)
    AE "Ah, good day, you two. I'm painting."
    "There was indeed a small set of acrylic paints nearby, and she had the leaves of a newspaper tucked around her lap as a makeshift smock."
    show AE happy
    AE "A gift from a friend, you see."
    show BE angry
    "Shiori took another moment to dab more paint on her object, holding it up by the base she'd brought and examining it closely for imperfections."
    show AE neutral
    AE "Mm. The primer is an aerosol, and I figured it would be pertinent to use it in the open air."
    MC "Yeah, that's a good idea."
    "Honoka tilted her head at the item Shiori was painting when a look of recognition came to her face."
    show BE surprised
    BE "Oh my gosh, is that Captain Buzzface?!"
    "Shiori's paintbrush hovered inches away from the figurine."
    show AE surprised
    AE "I... I beg your pardon?"
    AE "Captain... Buzzface?"
    show BE happy
    BE "Yeah, from the Warblade game!"
    show AE angry
    AE "I... believe you're mistaken. This character is Lord Judicator Septorum the IV."
    show BE neutral
    BE "Yeah yeah that's it. He's got the wicked chainsaw teeth, right?"
    show AE neutral
    AE "W-Well, no, they aren't chainsaw teeth, they're power dentures. They allow him to consume the volatile ingredients in-"
    AE "W-Wait, never mind. How do you know of him?"
    show BE happy
    BE "From the Warblade game, duh. He's my favorite multiplayer character. I never knew they made a figure out of him! Would have thought they'd go for Lieutenant Metal-Butt first."
    "Shiori rubbed her forehead."
    show AE angry
    AE "...Amaryllis of Stirn?"
    show BE happy
    BE "Yeah!!"
    "Shiori muttered tersely under her breath."
    AE "Maybe if he wasn't nerfed to high hell..."
    MC "Eh?"
    show AE neutral
    AE "But that's not the point, you play Warblade too?"
    show BE happy
    BE "Yeah! I had it on my dad's desktop back home!"
    show AE surprised
    AE "Oh? You played it on your father's desk? That... I doubt that'd be enough room."
    show BE neutral
    BE "Ehehe, no, his computer."
    show AE neutral
    AE "Com...puter?"
    BE "Uhh, yeah? It's a device you type in and has a screen."
    show AE angry
    AE "I know that! But... Warblade on a computer?"
    show BE angry
    BE "Well, duh. Warblade: Dynasty Killers, Warblade: Children of the Scourge, Warblade: Battle Rebellion... Is there some other kind of game?"
    show AE neutral
    AE "I..."
    "Shiori-san looked at first to me and then to Honoka."
    show AE angry
    AE "Is this some kind of injoke? I don't-?"
    show BE angry
    BE "It's not a joke! It's a fun game!"
    AE "I {i}highly{/i} doubt that a computer game is able to capture the complexities of the tabletop game."
    show BE happy
    BE "Well my video game is a lot more fun than whatever you do with those tiny little things!"
    show AE angry
    AE "They're miniatures."
    "Honoka and Shiori stared at each other from their respective seats. The air felt electrified..."
    menu:
        "Side with Honoka":
            jump BE033_honokaside
        "Side with Shiori":
            jump BE033_shioriside
        "They're both just games for kids. Relax!" if getSkill("Academics") > 7:
            jump BE033_academics
        "They're both just games for kids. Relax! (disabled)" if getSkill("Academics") <= 7:
            pass
        "Both versions bring different parts of the same world to life, focus on the commonalities." if getSkill("Art") > 7:
            jump BE033_art
        "Both versions bring different parts of the same world to life, focus on the commonalities. (disabled)" if getSkill("Art") <= 7:
            pass
        "Say nothing":
            jump BE033_silence


label BE033_honokaside:
    $setAffection("BE", 1)
    $setAffection("AE", -1)
    MC "Well, Honoka does have a bit of a point."
    "The two looked at me, awaiting further details."
    MC "I mean, tabletop games are a real hassle to get into. They can be fun, sure. But they require a lot of reading to know what you can do, memorizing all sorts of units and everything."
    show BE happy
    BE "Right! When you play a video game, it's just, boom. Hit start, and you're golden."
    MC "Right. And not for nothing, but a video game version makes it a lot cheaper to get into it as well. For the tabletop version you have to buy all sorts of minis, and painting supplies, which can add up."
    MC "I mean, how much of that stuff did you have on hand before you got into the game?"
    "Shiori seemed taken aback."
    show AE angry
    AE "I-I don't think that's... entirely {i}comparable{/i}, I-..."
    AE "... Hmph. Fine. I suppose you have a point."
    MC "Playing a video game version also has the benefit of, you know... you can play it by yourself. Anytime. In a few seconds."
    AE "However, the interactivity of not only painting your miniature, but setting up the field and collecting the necessary dice-"
    MC "It's a lot more grueling then handing someone a controller if they wanna play and saying 'A Button jumps'."
    show AE neutral
    AE "Haah... very well. I'll... accept that you have a differing opinion."
    MC "That's it?"
    show AE angry
    AE "You're lucky to be getting even that."
    show AE neutral-annoyed
    "Shiori-san dabbed the end of her paintbrush on a piece of paper towel, before lightly dusting her miniature with it."
    MC "Er, you're right. We'll leave you be. Sorry, Shiori-san. Um, see you around later."
    "Shiori didn't say anything back, and just went to painting as Honoka and I left her. Honoka looked at me sheepishly."
    show BE happy
    BE "Sorry to drag you into that. But feels good to be sided with. But, uh, better watch out for Shiori-chan now, you think?"
    MC "She's never seemed the type to hold a serious grudge... Why?"
    show BE sad
    BE "Eh, just the way she was brandishing that paint brush. I don't wanna take off my bra one day and find there was paint smeared inside."
    MC "That does not sound like it would be pleasant."
    "Honoka nodded as we walked towards the dining hall, leaving Shiori to her figures."
    jump daymenu

label BE033_shioriside:
    $setAffection("AE", 1)
    $setAffection("BE", -1)
    MC "I understand what Shiori's talking about."
    show AE neutral
    AE "Mind elaborating?"
    MC "Well. It's like any adaptation, right? There's rarely ever an adaptation of a medium that perfectly encapsulates the original. Anime will have filler arcs, movies will cut characters, games will weed out scenes for the gamer experience..."
    show BE neutral
    BE "Oh. Maybe, yeah. But, I mean, there's way more video games, and it's just one board game."
    AE "Technically there have been several editions and re-releases, and each edition is improved by a series of new units and rule updates. They are constantly working on it."
    show BE sad
    BE "Ah..."
    "Honoka stood up, and paced for a few seconds, clearly trying to think of a rebuttal."
    show BE happy
    BE "Well games do have downloadable stuff too!"
    MC "Honoka, you did complain about how it was obvious they cut out stuff from the main game just to sell you later."
    show BE sad
    BE "Gah, curse you Kei-chan and your adequate memory."
    "Honoka clenched her fist towards me, muttering at the ground."
    BE "Yeah, but-!"
    MC "Season pass."
    show BE sad:
        easeout 0.4 ypos 1.15 xpos 0.7
        easein 0.07 ypos 1.14
        easein 0.07 ypos 1.15
        easein 0.07 ypos 1.14
        easein 0.07 ypos 1.15
    "Honoka slumped down onto the ground. Her knees made contact with the earth as her calves splayed out. She hung her head in an over-dramatic defeat."
    BE "I can't believe it."
    BE "My own boyfriend disagrees with me when I'm debating with another girl!"
    AE "Inoue-san, just because Hotsure-san came to the correct conclusion, that does not mean his affection for you has been lessened."
    show BE surprised
    BE "How can I believe that! Were my boobs just a replacement for your huge butt?!"
    show AE angry at Transform(xzoom=1)
    show BE unique
    BE "I squeeze them together like this and it looks like a butt crack, is that your kink, Kei-chan?!"
    MC "N-no, not at all. I don't think that's anybody's kink. Honoka-"
    show AE neutral
    show BE angry
    BE "Nay."
    show BE sad:
        ease 1 ypos 1.01
    "Honoka stood up and stuck her hand out towards me, her other hand pressed against her forehead."
    "She was clearly being overdramatic. But she did seem wounded by me choosing Shiori over her."
    show BE sad
    BE "Clearly, you've won this fight, Shiori-chan. I shall relinquish Kei-chan to you! Have fun playing your silly tabletop games together."
    "Shiori had gone back to painting midway through Honoka's soliloquy."
    show AE neutral at Transform(xzoom=-1)
    AE "Indeed."
    show BE sad at Transform(xzoom=1):
        linear 0 xpos 0.7
        ease 1.5 xpos 0.85
    "Honoka took several steps away from Shiori, and then turned back."
    show BE happy
    BE "Um, we're still doing dinner, right?"
    MC "Yeah."
    show AE neutral at Transform(xzoom=1)
    BE "Okay, cool. Oh, and... hurt feelings, and... stuff. See you later."
    show BE happy:
        ease 3 xpos 1.5
    "Shiori did a few more brush strokes on her figure, not looking back up towards me."
    AE "Hotsure-san. If by some small chance, I do catch you leering at my backside in the future. There will be consequences, understood?"
    "I sighed."
    MC "Yes..."
    jump daymenu

label BE033_academics:
    $setAffection("BE", -1)
    $setAffection("AE", -1)
    MC "I mean. Really girls. They're just games, they're meant for kids, relax."
    stop music
    "Honoka and Shiori both looked at me, then at each other."
    show BE neutral
    play music Tension
    BE "What does that mean?"
    show AE neutral
    AE "Now Inoue-san and I are in agreement. Pray tell what exactly about either of this series is for kids, Hotsure-san."
    show BE sad
    BE "I mean, most of the games are rated for older teens at least."
    show AE angry
    AE "And the tabletop versions don't have any strict age limits given, but even I would admit that the ruleset would be too complicated for a younger child."
    MC "I, uh, I don't mean literally for kids. I just meant, they're games, they're supposed to be fun."
    AE "Being fun doesn't exclude the possibility that something has mature themes."
    show BE neutral
    BE "Oh for real. I mean, Dynasty Killers had... I mean, it's right there in the name, Kei-chan. They killed an entire dynasty."
    AE "Would you let your child play something as graphic as Warblade? Violence in media is the responsibility of parents to help guide their children through! If you just leave your children to their own devices-!"
    BE "It'd be like having a kid play those weird H-games!"
    show AE neutral
    AE "You'd be talking about the erosion of family values at its core-!"
    MC "I, I did not think you two would take my answer so seriously."
    show BE sad
    BE "Hmph, perhaps you should have thought more!"
    AE "Agreed."
    show BE neutral
    BE "Shiori-chan, would you like to talk more about the games, perhaps away from this nerd?"
    MC "Ne- Who are we talking about?!"
    AE "I wouldn't mind, but I am still in the middle of painting. Though this spot now reeks of casual."
    MC "I'll go, I'll go. I can see I screwed up here. Sorry, I thought I was being smart, I was just being stupid."
    "I backed away from the two to let them cool down and discuss the game further. There was no need for me to get in deeper water with either girl."
    jump daymenu

label BE033_art:
    $setAffection("BE", 1)
    $setAffection("AE", 1)
    MC "Well, if I remember, the first Warblade game did come out in the early 90s, so it wasn't too long after the first edition was released."
    MC "So they probably did design it, knowing it would get adapted to another medium at some point. I would say, both have their merits."
    MC "There's no reason to exclude either. They bring different benefits and reasons to play. Like, the video game is good for quick play, by yourself. Tabletop would be for friends and a longer session."
    show BE happy
    BE "I mean, I guess that's a good point. But which one's better then?"
    MC "I don't think either needs to be better. Think of it as just the video games being more pragmatic, using what they can to give a good experience."
    MC "It's probably better for people who aren't too imaginative, the games let you get a better read on how the technology and mechanics work, and then look at the characters in action."
    BE "Hm. Yeah that's true! Then you could... better understand it if you play the tabletop setting later?"
    show AE neutral
    AE "I would also submit in return that the tabletop version allows you to get a better understanding of the minutiae for the characters."
    show AE happy
    AE "There are so many different facets of the units that you can delve into."
    AE "I suppose one good example would be giving different units buffs based on how you paint them. Like painting Orcs purple giving them a stealth bonus."
    BE "Wait for real? Why?"
    AE "Have you ever {i}seen{/i} a purple Orc?"
    show BE neutral
    BE "... Ha! Haha! For real?! That's a thing?!"
    "Shiori chuckled softly, and pushed up her glasses."
    AE "Eheheh, so you're truly not familiar with Warblade putting details of lore into the game manuals?"
    "Honoka shook her head."
    BE "Nope!"
    show BE happy
    BE "But there's a ton of detail and story in the games still. They do get a bit crazy with the cutscenes in Reign of Temptation, though. But it lets you find out where Tellion got his prosthetic torso."
    show AE surprised
    AE "It does?!"
    BE "Yeah! I would be happy to show you. But you can probably find a video of it online, and find someone playing through it without talking over the story and stuff."
    show AE neutral
    AE "I see. I might have to search for some videos. I wouldn't want to neglect possible story threads, they could be useful for my campaigns."
    BE "Wicked. Yeah, if you're not watching the actual gameplay, I think most games would give you like, six or eight hours of material?"
    AE "Fascinating. Well, I suppose I have a new outlook to view. Thank you for enlightening me, Hotsure-san."
    MC "Oh, well. I mean, Honoka knew more about it than me. I just like video games, I guess."
    AE "That much is clear. Still. As for me, I should return to my painting, if you do not mind. These can, as you rightly pointed out, be quite expensive."
    MC "Sure. Hey when you're done, we'd like to see them. Right, Honoka?"
    BE "Totally. Send us some pics at least!"
    show AE happy
    AE "I shall endeavor to do so. Have a pleasant evening."
    jump daymenu

label BE033_silence:
    MC "..."
    show BE neutral
    BE "Yeah, well, miniature golf is just the worse version of regular golf."
    show AE neutral
    AE "How dare you? Especially when miniature golf relies on all sorts of angle calculations and acceleration mechanics!"
    show BE happy
    BE "Oh my gosh, haha. You're trying to make golf boring too. Yawn."
    show AE angry
    AE "Just because I know facts about things does not make me boring. Quite the opposite, if all you have in return for video games is 'ooh buttons, shiny'."
    show BE angry
    BE "There's way more to it than that! The game versions have so much more money pumped into them, they're higher quality!"
    AE "Tabletop games are a passion project worked on by small teams instead of nameless peons forced into crunch time!"
    BE "You probably only like them so much because you spend 90%% of your time sitting on your big butt and have alll the time in the world to set up an eight-hour game."
    AE "Oh! Then clearly your hatred from my superior version clearly stems from the fact that you can't even see the table."
    show BE surprised
    BE "Agh!"
    AE "Humph."
    show BE surprised at Transform(xzoom=-1):
        easeout 2 xpos 1.5
    "Honoka stood up with a pout and glared back at Shiori. She marched in the opposite direction quicker than I've ever seen her walk."
    "Shiori was silent, huffing, and flustered. When I caught back up with Honoka, she was the same, and didn't talk to me for a while. Shiori had gotten her really worked up."
    "Then again, Honoka hadn't exactly helped matters."
    jump daymenu

label BE034:
    scene Field with fade
    pause 1
    play sound ReleaseArrow
    pause 1.5
    play sound Thud
    "With nothing important to do during the afternoon, I'd gone to one of Honoka's archery club meetings to watch her perform."
    play music Hallway
    "I suppose it was wrong to say it was unimportant. Considering what we'd done, and how we felt for one another, coming to support someone you cared about seemed to be pretty vital."
    "Unfortunately, my cheers couldn't do much for Honoka today. She seemed to be off her rhythm, as another arrow didn't manage to make it to the target, making it one of several failures she'd had so far."
    "There was only one arrow actually in Honoka's practice target, and I wasn't even sure it was hers."
    show BE angry with dissolve
    BE "Urgh. Come on..."
    MC "You got this Honoka. Next one's gonna be a bullseye, I know it!"
    "Honoka took a deep breath. Her eyes closed for a second, before she pulled up the next arrow and nocked it, ready to fire. The members at this point could fire at will until 'quiver empty', so she let go when she was ready."
    "The arrow limped through the air and weakly stuck into the edge of the target. If it had been any further off, it would have been in the grass instead."
    BE "Oww..."
    "Honoka put her bow down after Haruhiro called the whistle. She came over and sat down next to me, instead of going to retrieve her arrows."
    MC "The wind must be pretty rough today, huh?"
    show BE sad
    BE "You don't have to fib to me, Kei-chan. I suck."
    MC "..."
    MC "It was rough today, yeah."
    "Honoka reached behind her shoulder and unstrapped her breast guard. With the garment on the ground, she rubbed at the side of her boob, wincing as she did."
    BE "This is the biggest size they have. But even if they had one that fit, I just can't spread my arms out far enough to avoid smacking a boob without losing out on power."
    show BE angry
    BE "But a full-power shot means I have to be close which means, bowstring against the titty and ow, it really smarts..."
    MC "Hm. Maybe there's another kind of bow you could use? Do they make them horizontal?"
    show BE happy
    BE "Ha. Ha, no."
    show BE neutral
    BE "..."
    show BE sad
    BE "I kind of asked that already. They said crossbows didn't count."
    MC "Well, glad it's not just my idea."
    show BE neutral
    BE "I'm pretty sure the only reason Haruhiro hasn't kicked me off the club yet is because he feels bad. But this is getting dangerous."
    MC "So, what does that mean for you?"
    "Honoka pulled up her legs, until her breasts pushed into her knees and squished around the joints. She pressed her face into the pillow her chest formed."
    show BE sad
    BE "Means I gotta stop doing archery."
    MC "I want to support you, but, I think you're right. Last thing I need is for you to get hurt."
    show BE happy
    BE "Heh, yeah. Nobody likes a bruised melon."
    MC "It's more than that, you goof. It's clear you're not having fun. That's just not good for your mental health. You need to do something you enjoy, even if you're not good at it."
    MC "I think it's clear you don't enjoy this anymore. Right?"
    show BE neutral
    BE "Right. Right."
    show BE sad
    BE "Ugh, Kei-chan, I don't want to deal with looking for another club again. But I can't just sit on my butt and do nothing. It's not as soft as Shiori's, it would hurt after a while."
    MC "Hehe..."
    MC "Um, well, I'd been looking at some recently myself. Maybe we can pick one out for you together? I'd written down a few. There might be one here you would like. "
    show BE happy
    BE "Oh? That's so thoughtful, Kei-chan. Sure, let's take a look at what you've got."
    "I pulled out my phone, and scrolled through my notes to find the last list I'd worked on for possible clubs."
    MC "Here. There should be something here."
    "Honoka and I looked through my ideas."
    show BE neutral
    BE "Hm. I'm pretty sure the kendo club would be out of the running for me."
    show BE unique
    BE "These puppies pretty much prevent me from holding a sword straight up with both hands."
    MC "Right. Well, what about a music club? Not a violin, maybe. But, could do something like a flute?"
    show BE neutral
    BE "Maybe. But I've never been one for musical ability. You remember that time we went to karaoke?"
    MC "..."
    MC "Moving on then."
    MC "Hm. Softball would be interesting. Do you think you could still swing a bat?"
    BE "Hmmmm."
    BE "I think I could."
    "Honoka pushed her arms to one side and pantomimed the act of swinging a bat to test the waters."
    show BE happy
    BE "Feels pretty good. Catching shouldn't be impeded. Actually, my breasts might help out there if a ball lands in them."
    MC "Well, didn't think of that. But yeah that could be a benefit."
    BE "Hahaha, and I think if you get beaned with a ball while at bat, you get a free base, right? So at least there, getting hit would be a positive. Still would hurt, though."
    "We kept scrolling for a bit until we came across another option that piqued Honoka's interest."
    show BE neutral
    BE "Cooking club?"
    MC "It's one of the bigger groups on campus, from what I was told. Part of it is training and informational but most of the time they let you experiment and learn on your own."
    BE "Huh. But, a kitchen's full of knives and fire."
    MC "You would just need to turn to the side to chop. It's real life, not a game show, you can take a few minutes to slice a carrot if you need to. As for fires, same thing, just stay away from heating elements."
    "Honoka nodded."
    show BE happy
    BE "Do you think I could learn how to make chocolate?"
    MC "Probably not. That's just, like, a process that happens in factories."
    BE "I could make things {i}with{/i} chocolate, though."
    MC "You absolutely could."
    BE "Haha, okay. Remember that one, then."
    "Honoka and I looked for a few more before my list ran dry. A few just weren't feasible with Honoka's size, and others weren't things she was interested in."
    MC "So, here's the way I see it. You like these two the most. Softball, or cooking. I suppose if you wanted you could do both?"
    show BE neutral
    BE "Hm, maybe. But then that would really cut down on my time to spend with you. One's fine for me. They both sound so fun, though. Not sure how to pick."
    MC "Well, softball would be more your speed as far as athletics go, and keep you healthy. Cooking is just a nice life skill to have."
    show BE happy
    BE "Yeah. Hmmm."
    show BE sad
    BE "I guess there's only one option, Kei-chan."
    MC "What's that?"
    show BE happy
    BE "Choose for me!"
    menu:
        "Cooking Club":
            jump BE034_cooking
        "Softball Club":
            jump BE034_softball

label BE034_cooking:
    $setProgress("BE", "BE035A")
    $setFlag("HONOKA_COOKING")
    $setVar("BETomboy", getVar("BETomboy") + 2)
    MC "I think you should join the cooking club."
    BE "Oh? Heh, how come?"
    MC "I think it would be nice to do something different. Take a break from physical activity for a while and do something that's more chill."
    show BE neutral
    BE "That's a good point... Plus, you never know. Maybe I'm really good at it. I could go on Steel Cook and show everyone who's the boss with my double-scoop meringue."
    MC "Setting your hopes high already, I see."
    show BE happy
    BE "Yeah, why not! You don't aim to get a C- in a class. You try and get an SSS rank, so even if you screw up you can still get an A."
    MC "If that works for you, I'll be pleased as can be. Just, try and start easy okay. Don't try and make an omurice before you learn to... make regular rice."
    show BE surprised
    BE "Oh my gosh wait, I didn't even think about this until now. Would they provide the food and stuff for me?"
    MC "I assume so."
    show BE happy
    BE "Oh, hell yes. Then I'm so in. I can screw up, at no cost, and still eat leftovers or anything that turns out good?"
    show BE neutral
    BE "Chef Inoue at your service, then."
    MC "Wonderful. I think this will be a good fit for you."
    show BE happy
    BE "Me too!"
    BE "Hey, wait a minute..."
    MC "What?"
    show BE neutral
    BE "This isn't some trick to get me into doing a naked apron routine for you, is it?"
    MC "No no, not at all."
    show BE unique
    BE "Hehe, Kei-chan, I'm not upset by the idea."
    BE "I'd just need a huge apron for it to work properly, is all."
    MC "That you would. But maybe a small apron would make it even better."
    show BE happy
    BE "Better, but not as pitifully practical! If it doesn't actually cover my boobs then what's the point?! The point is I'm still cookin', just with my butt out."
    show BE sad
    BE "And I am not cooking bacon without a top on."
    show BE angry
    BE "Never again..."
    MC "I don't think I want to know any more details about that..."
    MC "But for now, I think you should go tell Haruhiro you're quitting the club so he can fill a spot if he needs to."
    show BE neutral
    BE "You're right. Be back in a bit."
    jump BE034_end

label BE034_softball:
    $setProgress("BE", "BE035B")
    $setFlag("HONOKA_SOFTBALL")
    $setVar("BEFeminine", getVar("BEFeminine") + 2)
    MC "I think you should join the softball club."
    show BE neutral
    BE "Heh, somehow I knew you were going to pick that."
    MC "Oh. Is that bad?"
    show BE happy
    BE "No, not at all! It sounds like fun. I get to swing a huge bat around and run around. It should be good. Keeps the blood moving and the legs active."
    MC "Exactly. I don't think you could handle staying inside for most of the day. I've seen you outside in blazing heat and freezing cold."
    MC "I'm not entirely certain that you're free of animal DNA considering how much you like being outdoors."
    BE "Haha. Yeah, I've got two huge cow chromosomes, Kei-chan."
    show BE neutral
    BE "I think about the only thing I couldn't be is a catcher, just because the pad they make you wear might be too hard to make in my size."
    MC "Sure, but you just need a mitt, a helmet, shoes, and like, a uniform. And they've easily got the ability to sew the right-sized uniform for you."
    show BE happy
    BE "That's right! Oh? Wait a sec, Kei-chan..."
    MC "Huh?"
    show BE aroused
    BE "Do you have like, some softball-based fetish I didn't know about?"
    MC "Th-That's a thing?"
    show BE unique
    BE "Oh sure, a girl, every inch of flesh covered up in a nice uniform, that gets it dirty as can be. Her skin stays pristine, with that 'hot and dirty' look some guys are into."
    MC "I, ah, this is new to me. So no, that's not why I suggested the softball club."
    show BE neutral
    BE "Hmm..."
    show BE happy
    BE "Okay, I'll believe you, Kei-chan."
    BE "But if I come into your room one day wearing nothing but a baseball hat, and you get turned on, I'll know you're lying."
    MC "I'm not even sure if that's the same fetish at that point. That's just you naked."
    MC "Um, either way, you should go tell Haruhiro you're leaving. Not nice to leave club presidents in the lurch, remember?"
    show BE neutral
    BE "Right right. Okay, be right back, Kei-chan."
    jump BE034_end

label BE034_end:
    show BE neutral at Transform(xzoom=-1):
        ease 1.5 xpos 0.9
    "Honoka walked away for a bit to tell Haruhiro the bad news. I wasn't close enough to hear the conversation, but he looked like he understood."
    show BE neutral at Transform(xzoom=1):
        ease 1.5 xpos 0.5
    "She sighed as she walked back towards me, and slung an arm around my neck."
    show BE neutral
    BE "Well. The deed is done. I am once again club-less."
    MC "Not for long, though. We'll go get you signed up, ASAP. Heck I can go with you right now if you want."
    "Honoka smiled and pulled me in closer, until the entire right side of my face was buried in her chest."
    show BE happy
    BE "Hehe, I like the way you think, Kei-chan."
    "Honoka and I walked towards campus to get her signed up for her next club. Hopefully she'd have more success with this one."
    jump daymenu


label BE035:
    if getFlag("HONOKA_COOKING"):
        jump BE035A
    elif getFlag("HONOKA_SOFTBALL"):
        jump BE035B

label BE035A:
    $setProgress("BE", "BE036")
    scene Cooking Classroom with fade
    #general chatter sfx
    play music Busy
    "When Honoka and I first visited the cooking club to get her signed up, there had only been a few people in the cooking space. Now that we were at an actual meeting, it was a lot more crowded."
    "There was a large row of ovens and stoves lined up, with a wide amount of space for food preparation. On the wall were various types of knives for different cooking purposes, and all sorts of cooking utensils stacked up nearby."
    Kanami "Hello everyone. Thank you all for coming today. I hope your week has been well. We have some new people today who will be joining us in the world of cooking. Please be kind to them and offer your guidance if they need it."
    "The cooking club was large enough that there were several 'heads' of the club, but it was the spokesperson who spoke to us currently."
    "Kanami Tozakura was a soft-spoken woman with very long black hair. Her posture looked perfect. She looked like she'd been designed to wear an apron, like she did currently."
    Kanami "As always, before you begin today, please make sure to wash your hands thoroughly, and to do so whenever you switch between ingredients to be safe. Those of you with long hair should tie it back, as I have."
    Kanami "For those of you in the beginner level, we have a few recipes available for you to try out today. I'd recommend the fried rice, personally. If you're more advanced, the same goes for you but my recommendation would be the okoyamonaki. "
    Kanami "Be safe. Be clean. Be delicious. Let me or the others know if you need aid."
    MC "Well, Honoka, what should we try?"
    show BE happy
    BE "..."
    MC "Honoka?"
    BE "Oh! Right. Let's see. The fried rice sounds good, then."
    MC "You seem distracted, everything okay?"
    BE "Hehe, yeah. It's just, did you notice, Kei-chan?"
    MC "Notice what?"
    show BE neutral
    BE "Kanami-chan. She's got the same growth factor as me."
    MC "Oh!"
    "It wasn't that I'd missed that Kanami had a large chest. Looking again, her breasts were very full, and clearly lifted up her apron quite a lot. She was only a bit smaller than Honoka."
    MC "I, I guess I didn't notice."
    show BE unique
    BE "I know I've got a bit of a leg up on her but, hey, if she can do all this cooking stuff, so can I!"
    MC "Very good point. Let's get started then, shall we? Got your apron on. Let's take a look at these instructions."
    show BE neutral
    BE "First step is to cook the rice and then cool it down."
    MC "Huh, okay. Well that's easy enough."
    "Honoka went to retrieve a rice cooker while I grabbed some rice and brought it back over to our station. As the rice cooked, we took a further look at the instructions."
    MC "That'll take a bit of time. So until then we've got a lot of vegetables to chop up and the shrimp need to be shelled and cooked."
    BE "Cool. How about you handle the shrimpies and I'll do the vegetables?"
    MC "Sounds like a plan."
    "Honoka and I placed our cutting boards down and got to work. She pulled over a few carrots and peppers and lined them up, while I started to shell the shrimp."
    MC "Why is it 'shelling' the shrimp? Aren't I really 'de-shelling' them?"
    BE "Ha. Yeah I don't know. One of those dumb quirks of language I guess."
    "As Honoka and I worked, Kanami came up and observed for a moment."
    Kanami "Very nice, Hotsure-kun. Please don't forget to check the intestinal tract on the back there. If you take a small knife, you can gently slice into the end and lift it up to pull it out."
    MC "Oh, right. Thanks. That wouldn't exactly taste good, would it?"
    Kanami "Ufufu, no, no it wouldn't. How are you doing, Inoue-chan?"
    BE "Ha. I think I'm doing okay. How does it look?"
    Kanami "Your cuts are okay. But your hands aren't quite in the right position. May I?"
    show BE happy
    BE "Sure."
    "Kanami reached over to Honoka's hands and pulled her fingers in. I stopped my own work to watch, to learn better myself."
    Kanami "Imagine your fingers like a cat's paw, you want to keep them curled in so you don't cut them accidentally. As long as you don't lift your blade above the knuckle, you should be okay."
    show BE neutral
    BE "Ah, okay. Like this?"
    "Honoka adjusted herself as Kanami moved her hands away. The older girl nodded."
    Kanami "Yes, yes. Perfect, Inoue-chan. Now for the peppers, that's a little trickier. Do you mind if I show you?"
    "As Honoka learned how to properly cut up peppers, our rice finished cooking. With Kanami's written instructions I dumped it out onto a baking sheet, spread it thin, and put it in a freezer to cool. By the time I finished, Honoka was done slicing."
    Kanami "You two seem to be doing well. Enjoy. Let me know if you need anything."
    Kanami "Oh my. Koumori-chan, please be careful with how much of that you add..."
    "Kanami left Honoka and I together to continue our cooking while she tended to another student."
    BE "Phew, this is hard work. But, hey, cutting stuff is kind of fun."
    MC "Good to hear. So, we need to cook the shrimp a bit first, and then some eggs to mix into the rice, while the rice itself cools down."
    show BE happy
    BE "I've got the skillet on. Should be warm enough now."
    "We dropped the shrimp into the skillet and began the process of cooking them. The rest of the recipe was pretty simple. Soon everything else was prepared and all we had to do was actually bring in the rice."
    show BE neutral
    BE "I'll grab it."
    "As Honoka walked to the freezer to grab the rice, I put some oil in the skillet to get things ready. She came over with the tray perched on top of her bust with her hands on the sides for support."
    show BE happy
    BE "Hehe, one delivery of cooled rice ready for dispersal, Kei-chan."
    MC "Perfect. Toss it in?"
    "Honoka smiled, and used a spatula to scrape the rice into the skillet. We took turns adding the rest of the ingredients into the pan, tossing in the veggies, shrimp, and egg."
    show BE neutral
    BE "Are we forgetting anything?"
    MC "Hmm..."
    if getSkill("Art") > 6:
        jump BE035A_sauce
    else:
        jump BE035A_nosauce

label BE035A_sauce:
    $setAffection("BE", 1)
    MC "Oh, yes. We almost forgot to put in the soy sauce."
    show BE surprised
    BE "Oops!"
    show BE neutral
    BE "Well let's get it in there, then."
    "I grabbed the bottle and opened it, upending it over the skillet."
    MC "It said three tablespoons so one..."
    MC "Two..."
    MC "And three."
    BE "Perfect. Let that mix in a bit. Do you think we can do that flippy-tossy thing they do in restaurants?"
    MC "Ah. No. I don't think we can. I don't wanna make a mess. Maybe we can try it some other time with just like, an egg or something."
    show BE happy
    BE "Bah. Fine. Just use the spatula then."
    "I made sure everything was incorporated properly, until the fried rice was a nice color. After a minute passed, I spooned some out onto a plate for us to share."
    BE "Ohhhh."
    show BE aroused
    BE "This looks so {i}good{/i}."
    "Honoka grabbed a spoon, and took a huge bite."
    show BE surprised
    BE "Mmf!"
    MC "Good?"
    BE "HOT."
    "Honoka opened up her mouth and fanned into it a few times to cool down the hot food in her mouth. Eventually she swallowed. Taking a cue from her, I blew on my spoon before taking my bite."
    MC "Mmf. Wow. Yeah, that is good. It was pretty simple to make as well."
    Kanami "Oho. Everything come out well for you two?"
    "Honoka gave a thumbs-up to Kanami, her mouth already full with another bite."
    Kanami "I take it that's a yes. Wonderful. So glad you could learn something new today. Next lesson we'll be doing something sweet."
    show BE happy
    BE "Happy: Schweet? Mmf, dat schounds goohd."
    MC "Honoka. Swallow."
    show BE neutral
    BE "{i}gulp{/i}"
    Kanami "Ufu, it's always a delight to see people enjoying the food they create. Please make sure to clean up well. A clean kitchen is a good kitchen."
    MC "Yes, we will."
    BE "After eating."
    MC "Which won't be long if you keep scarfing it down like that! Gimme more."
    "After Honoka and I finished eating, we moved everything over to one of the big sinks to clean up. That was the less-fun part, but necessary. Didn't want to make a bad first impression."
    MC "So what did you think of the club?"
    BE "It's great. Kanami's nice and it seems like everyone here is having fun. Which is good. And getting to eat extra food is always a plus."
    MC "Good. Sounds like we found a good fit for you."
    show BE happy
    BE "Well you suggested it. So thanks, Kei-chan. Soon I'll be able to cook a big feast for you to celebrate."
    show BE unique
    BE "And if you're a good boy, you'll get to eat off someplace special."
    MC "..."
    MC "How am I not used to you making those kinds of comments yet?"
    show BE happy
    BE "I'm just too good, Kei-chan. I'm just too good."
    jump daymenu

label BE035A_nosauce:
    MC "No, I don't think so. Looks like we've got everything here."
    BE "Perfect. Let that mix in a bit. Do you think we can do that flippy-tossy thing they do in restaurants?"
    MC "Ah. No. I don't think we can. I don't wanna make a mess. Maybe we can try it some other time with just like, an egg or something."
    show BE happy
    BE "Bah. Fine. Just use the spatula then."
    "I made sure everything was incorporated properly, until the fried rice was a nice color. After a minute passed, I spooned some out onto a plate for us to share."
    MC "Ladies first."
    "It was a bit of an unnecessary comment. Honoka already had a spoonful ready."
    show BE neutral
    BE "Ooh, ah, it's hot. Mm. Hm."
    MC "Mm. It's pretty good."
    BE "Yeah..."
    MC "What's up?"
    BE "I'm not sure. It tastes different from what I'm used to."
    Kanami "Mm, hello you two. How did your dish come out?"
    MC "Fine, thanks."
    BE "Yeah, it's okay. I think something's off, though."
    Kanami "Oh? Do you mind if I try?"
    "Honoka nodded, so Kanami took a spoon for herself and sampled it. She closed her eyes and tilted her head as she chewed on the rice."
    Kanami "Hm. The rice is cooked well. Nothing seems overdone. But, oh, I see. It's missing soy sauce."
    MC "Ah, nuts. We forgot something."
    Kanami "Don't fret too much, Hotsure-kun. It was your first time. Excitement can make you a bit klutzy, ufu, but it's not a problem."
    Kanami "If you like you could still mix in some soy sauce with it, but I would only use a tablespoon as there's going to be less heat in the rice at this point, and it won't be able to incorporate as much."
    BE "Okay. Thanks for the tip."
    "Honoka did as suggested and put a bit of soy sauce in the rice. Now we could see the color we were used to with fried rice, though it still wasn't 100%% correct. It was better than before, though."
    MC "Hm. Mm-hm. Yeah that does taste better."
    BE "Nuts. Oh well. Lesson learned. This was still fun."
    Kanami "I'm glad to hear. Don't let a simple mistake beat you down. We have had students start fires who learned to make scrumptious food. "
    Kanami "Next time we'll be making some sweet food. So make sure to follow the recipe to the letter to be safe. Baking's less fixable if you forget an ingredient, but it's also easier to come out like you expect!"
    show BE happy
    BE "Sounds good! We'll be here for sure. Thanks Kanami."
    Kanami "Anytime, Inoue-san."
    "Kanami left, so Honoka and I finished up and cleaned up our station. As we stood by one of the sinks and scrubbed our dishes I turned to Honoka, elbow-deep in the sink."
    MC "So what did you think of the club?"
    BE "It's very nice. Kanami's great and it seems like everyone here is learning cool stuff. It's cool. And getting to eat extra food is always a plus."
    MC "Awesome. Sounds like we found a fitting club for you."
    show BE happy
    BE "Well you brought it to my attention. So thanks, Kei-chan. Soon, I'll be able to cook a big feast for you to celebrate."
    MC "I look forward to it. But you'll have to beat me to the punch, cuz I plan on doing the same to you."
    BE "Oof, Kei-chan you know how to tease a girl."
    MC "Tease? Nah. Just a promise. I'll make you full and satisfied."
    show BE surprised
    BE "..."
    MC "... Not remotely how I meant it."
    jump daymenu

label BE035B:
    $setProgress("BE", "BE036")
    scene Baseball Field with fade
    #SFX: General chatter
    "When Honoka and I checked out the softball club, joining was contingent on one thing. She wouldn't be put into the team right away. They'd already split into two teams early in the year and played matches against each other on a regular basis."
    "They didn't want to put new players in the running right off the bat. So the first few meetings would be learning the basics and seeing where she performed."
    "As seemed traditional by this point, I offered to go with her to the first meeting to check it out, and try it for myself."
    #SFX: Whistle
    Naoki "All right, everyone. Huddle up, huddle up."
    "The assembled members approached a young man with three whistles around his neck. We joined with the others."
    Naoki "Okay. Here's the deal. I've got a wicked headache today, so I don't want to hear any bellyaching because it's gonna drive me crazy. Our next match is scheduled in two days, so spend this time brushing up on your catching and throwing."
    Naoki "We've got three batting stations reserved. So if you see one is empty, just go for it with your partner. Try not to hog it. Collect your balls when you're done. We don't wanna leave a mess anywhere."
    Naoki "Any questions? Good. Get out there, have fun."
    MC "Huh. Well, he was a bit rough around the edges, huh?"
    show BE neutral with dissolve
    BE "Eh. Headaches are a pain. Literally. What are ya gonna do about it?"
    show BE happy
    BE "Let's go and knock some balls around. Get a good warm-up in!"
    "Honoka and I grabbed some gloves and balls and found a good spot on the field for us to practice."
    MC "What do you wanna try first, just some pitches?"
    show BE neutral
    BE "Nah, let's just throw it back and forth first, until we get a feel for it."
    show BE sad
    BE "This ball's weird. It's all big and soft."
    MC "Well."
    MC "Yes, Honoka. Hence why they call it 'softball'."
    show BE happy
    BE "Well doi, Kei-chan! I just mean it's weird in my hand. Guess I won't know how it flies through the air until I throw it. Heads up!"
    "Honoka chucked the ball through the air. I raised my gloved hand, and with a 'plop', it handed in my glove."
    MC "Nice throw. How'd it feel?"
    "I tossed it back towards Honoka as she considered it. As I reached back to grab her return throw, she answered."
    show BE neutral
    BE "Pretty good I guess. It's not so big I can't get my hand around it. And it doesn't really hurt when it lands in the glove."
    MC "That's good. Yeah. This is pretty fun. Here, go a bit longer, I'm going to see how long I can throw this one."
    "Honoka jogged backwards, keeping her eyes on me as I threw the ball as far back as I could. The ball went sailing through the air, and right over Honoka's head. With a jump, she hopped up and caught the ball."
    show BE happy
    BE "Woo! Rock on. I got it."
    BE "Here, catch this one!"
    "Honoka stepped forward, and tossed her arm underhand in order to pitch the ball at me. This throw had more speed to it, and went closer to my chest."
    "I still caught it, but could tell that it had more heat behind it than her earlier throws."
    MC "Hey, that was pretty good. Here, try doing it that way again. Underhanded. That's how you have to pitch anyway."
    "I threw it back at a normal speed, and Honoka repeated the motion to pitch the ball again. Her arm went around, towards her back, and as her arm hit the underside of her bust, she let go of the ball."
    MC "Damn. That's a good pitch, Honoka. Keep that up."
    "Honoka and I kept up this pace for a while. I would throw her the ball and she'd swing it towards me, much faster than I could get. Eventually I had to ask the obvious."
    MC "Honoka, is that, like, bruising your boob at all?"
    BE "Huh? No, nope. It's pretty soft and it's not as if I'm jamming into it or anything. It just seems to be a good point for me to pitch. Kinda cool."
    MC "Seems so. You should be a good pitcher if you show that off to the coaches."
    show BE neutral
    BE "I'll definitely show her. But for now, it looks like one of the batting positions is open. Want to take a crack at it?"
    MC "Sure."
    "We walked over to the batter's box and looked at the bats that had been placed there."
    MC "I have no idea whether I want a heavier one or a lighter one. I guess I'll just use this one for now and if I really suck, I'll switch."
    BE "Hehe, sounds like a plan. Want me to pitch first then?"
    MC "Sure, that'd work."
    "I discarded by glove to grab the bat, and had the implement in my hand, ready to go."
    UNKNOWN "Oh crap, heads up!"

    if getSkill("Athletics"):
        jump BE035B_pass
    else:
        jump BE035B_fail

label BE035B_pass:
    "I turned towards the direction the voice yelled from. One of the softballs went wide and barreled through the air."
    MC "Watch out!"
    show BE surprised
    "Dropping the bat, I reached out with my dominant hand and grabbed the ball before it hit Honoka. It quickly fell out of my grasp as I pulled my hand back."
    MC "Ow, ow. Hot."
    BE "Oh my god, Kei-chan, are you okay?"
    "I yanked my hand back. It was sore. I could already see the redness."
    MC "Yeah, yeah I'm okay. But I know now why they make you wear gloves when you play this game. But my ungloved hand was just closer so, that's the one I used."
    Student "Hah, hah, oh my god, I'm so sorry, that pitch was totally screwed up. Are you all right?"
    MC "Yes, I'm okay."
    Student "Did you catch that?"
    MC "Yeah."
    Student "Dude. That's impressive. That ball was really zooming. It could have really hurt you if you didn't catch it right. Again, I'm so sorry, can I make it up to you somehow?"
    MC "Uhh..."
    $setAffection("BE", 1)
    show BE happy
    BE "Yooou could get some ice cream~ One for me, since you almost hit me. And one for my big hero so he can hold it until the stinging in his hand goes away."
    "Honoka smirked and clung to my arm, holding it within her chest."
    MC "That would be nice, actually."
    Student "Of course, not a problem. I'll be right back."
    "The young man who nearly beamed Honoka in the chest ran off to get our ice cream, leaving Honoka and I alone for a bit."
    MC "Ice cream sounds good, but it might not be the best thing for us if we're playing softball."
    show BE neutral
    BE "Huh? How come?"
    MC "Well, my fingers will get all sticky."
    show BE happy
    BE "Hehe, don't worry. I'll take care of that."
    MC "Ah, okay. Waait, take care of it how?"
    "Honoka simply giggled and grabbed my hand, where it still stung from the impact of the softball. She clutched it, and placed it between her breasts, then pushed her arms forward."
    "Her pose created a cushion of her boobs that pressed on both sides of my hand, with my palm left basically clutching her left breast."
    show BE unique
    BE "Hehe, we've gotta make sure your hand doesn't swell up."
    show BE aroused
    BE "Anything else is free to swell up as much as it wants."
    MC "Hahaha..."
    MC "Is my hand at least free to squeeze as much as it wants?"
    BE "Your hand is in my tits, Kei-chan."
    MC "Right, right."
    "That was all the confirmation I needed to have a bit of fun rubbing and squeezing Honoka's chest. I had to admit that it actually helped numb the pain. By the time our mysterious assailant returned, I barely felt anything."
    "In his hand were two individual bowls of ice cream from a vending machine, the spoons already detached for us."
    Student "Here you go. And again, I'm so so sorry. I'll be more careful!"
    "He gave a quick bow before turning back to his partner and presumably explaining where he'd been for the last few minutes."
    #SFX: Squeeze squeeze
    "Honoka held the ice creams in both of her hands, and smirked at me."
    show BE happy
    BE "Now, I'm currently in the position to have two servings of ice cream while being groped. This is basically my dream."
    show BE unique
    BE "But if you want to share this ice cream, you're gonna have to let go."
    "Sadly I pulled my hand out. Ice cream did sound nice right now."
    "Honoka handed me the ice cream and we dug in."
    MC "Well, not how I expected this visit to go."
    show BE neutral
    BE "Me either!"
    MC "Do you still want to try and hit some balls?"
    show BE sad
    BE "...But ice cream?"
    MC "After the ice cream."
    show BE happy
    BE "Oh! Yeah, sure. Let's eat then."
    "Honoka and I finished up our ice cream. By the time we'd completed them, the pain in my hand was completely gone."
    jump BE035B_after

label BE035B_fail:
    "I turned towards the direction the voice yelled from. One of the softballs had gone wide and barreled through the air right towards Honoka."
    MC "Look out!"
    "I shoved Honoka aside. There was a painful smacking sound as the softball impacted my back."
    MC "Gaaah!"
    "There was a sharp, stinging pain, and then suddenly there wasn't any serious pain. I crumbled forward."
    "It was only Honoka's reaction that kept me from falling into the dirt. Her arms caught me before I went tumbling."
    MC "Ugggh..."
    Student "Damn it, shit. Shit."
    "Whoever was the cause of the projectile heading towards Honoka had run up, panting hard as he arrived."
    Student "Agh, oh my god. Are you okay?"
    MC "Well, it really smarts. But I don't think it actually broke anything."
    Student "Do we need someone to come take a look at you?"
    MC "I really hope not. Hang on. Honoka, do you mind taking a look?"
    show BE neutral
    BE "Of course!"
    "It was a bit embarrassing, but I pulled up my shirt so Honoka could take a look at my back. Her hand touched the top, near my armpit."
    show BE sad
    BE "Was it here?"
    MC "Ah... yeah. That stings. But. Well, push a little harder."
    "Honoka did so, but nothing seemed to feel worse."
    show BE neutral
    BE "I think you at least managed to avoid all the important bits. You should be good, maybe get some ice on that?"
    Student "I can do that! I'll be right back."
    "Our mysterious assailant left to go get ice, leaving Honoka and I alone. She snickered, and I soon felt the touch of her fingers under my arm."
    MC "Hahaha, h-hey, haha, stop that!"
    show BE happy
    BE "Hehehe, sorry, Kei-chan. Opportunity arose. Still stings a bit?"
    MC "Yeah. Some pressure and ice will help."
    show BE aroused
    BE "Pressure, huh?"
    show BE unique
    BE "I can do that..."
    "Honoka stepped behind, and swiftly pushed her boobs into my back. The force of the squish naturally made me want to step forward, but after a while, I just leaned back into it."
    "It helped her get a grip around my waist, where she could properly keep the pressure on the sore spot with her bust. Her hands held on to each other as her breasts squished together, overflowing her top and pressing up into her chin."
    "I just really wished I could have seen it. But feeling it felt pretty awesome, too."
    show BE aroused
    BE "Is this helping, Kei-chan?"
    MC "..."
    MC "I was gonna say that your boobs always make me feel better. But, it is helping the soreness go away."
    show BE happy
    BE "That's because boobs are magic. If I could, I would bottle it up and sell it."
    MC "Only if it didn't cause your own essence to be leeched out. What a crime that would be."
    show BE neutral
    BE "Heh, as if. I'd never sacrifice my chest for anyone."
    show BE unique
    BE "Well, almost anyone. But you'd need to buy me, like, an entire sweet shop to make up for it."
    MC "Sorry, I can't quite hear you, I think your boobs are covering up my ears."
    show BE happy
    BE "Pff, they'll cover up your nostrils if you get smart with me~"
    "Soon our unintentional attacker came back, winded from running so fast to get the aid I wanted."
    Student "So. Here, I got you an ice pack, and some pain relievers if you want. And then I brought a few water bottles for you as well."
    MC "Ah, perfect. Thanks a bunch. This'll help."
    "I opened up a bottle of water and swallowed down some of the pain relievers, then looked over to Honoka."
    MC "Honoka, could you hold the ice pack on me for a while?"
    BE "Sure, Kei-chan. Here, why don't we sit down for a bit?"
    "We took Honoka's suggestion and sat down for a bit, getting the weight off of our feet and recovering. It didn't take too long for it to feel okay."
    MC "Wanna try and hit some balls?"
    show BE surprised
    BE "Are you sure? What about your back?"
    MC "Eh, it feels okay now, and besides it's for you, so I'll throw and you can swing to start."
    show BE neutral
    BE "Hmm, if you're up for it. Sure. Let's give it a shot."
    jump BE035B_after

label BE035B_after:
    "With a little bit of nourishment in our systems and my slight injury healed, the two of us made our way back to the batting area, which had thankfully remained unattended."
    MC "You bat first, actually. I'll try and swing some balls to you."
    show BE happy
    BE "Cool. Shoot some zingers at me, Kei-chan."
    "I got to the pitching mound and readied myself. After giving Honoka the signal, I flew a ball her way. The first one whizzed by her."
    "I'd brought some spares, so I was able to throw another one towards Honoka. This one she hit, but it dinged off to the side, out of bounds."
    "I continued to pitch for her. Bit by bit, she got better. It was a different type of ball than what we'd sometimes used as kids, after all. Learning anything new was a challenge. But she stuck by it."
    "By the end of a short pitching session, she was able to mostly hit them in-field, which was pretty good progress for a rookie."
    BE "You know what, Kei-chan? I think this club's pretty cool. I like it. Hitting stuff feels great. Is there, like, a hammer club where you just slam things with a sledgehammer?"
    MC "Er. There might be something like an architecture group or a craft club but that might not be in this school's wheelhouse."
    show BE sad
    BE "Bummer."
    MC "But, hey, you like it. That's good."
    show BE happy
    BE "Yeah. Just a rough go of it for you this time around, huh?"
    MC "Ah I've already healed up magnificently. I don't remember much except for these two heavenly pillows comforting me in my time of need."
    "Honoka rolled her eyes."
    show BE neutral
    BE "Come on, let's get back to the dorms, Kei-chan. I got my exercise for the day. Time for video games and sweatpants."
    MC "That sounds good to me."
    jump daymenu

label BE036:
    $setProgress("BE", "BE037")
    scene School Planter with fade
    play music Busy
    "Honoka and I had some free time after classes today. She didn't have a club meeting to get to, and my own responsibilities were limited to what homework I had for that night. So we decided to just walk around the campus and get some mild exercise."
    show BE happy with dissolve
    BE "Ahhh. The sun is shining. The wind is nice. There's literally birds chirping nearby."
    MC "Yep. it's quite a nice day isn't i-"
    show BE surprised
    BE "I am so borrrrrred!"
    MC "I should have known that was coming. Well, we could go play video games if you wanted."
    show BE neutral
    BE "No no, I was the one who suggested we just stroll around for a bit. I have to stick to that. I don't want people thinking Honoka Inoue's a flake."
    MC "Mmm..."
    MC "I'll be honest, Honoka. Right now I'm looking around for anything that could be considered a conveniently-timed distraction to change the topic."
    BE "That's totally reasonable."
    show BE neutral:
        xpos 0.5 xanchor 0.5 yalign 1.0
        linear 0.5 ypos 0.9
        linear 0.5 ypos 1.0
    "Apart from having to sidestep a squirrel that was busy chewing on a nut in the middle of grass, Honoka and I didn't come across anything interesting to get us talking."
    "The squirrel finished its snack and then darted under a bench back towards a tree."
    "Until after a while, we heard some faint humming around the corner. Heading over, we saw Naomi standing around a large flower bed, in the middle of watering a variety of blooming flowers."
    show BE neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show GTS happy at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    GTS "La la la~"
    show BE happy
    BE "Oh, hey, Naomi-chan! What's up?"
    show GTS surprised
    GTS "Hm?!"
    show GTS neutral
    GTS "Oh. Ah. Hello, you two. I didn't hear you coming. You snuck up on me a bit."
    MC "Sorry about that. Were you, ah, singing anything in particular?"
    show GTS happy
    GTS "No, not really. I was just trying that old wife's tale about singing to plants helping them grow larger."
    show BE neutral
    BE "Huh. I haven't heard that one before."
    show BE happy
    BE "Hehehehe, guess you listen to a lot of music, huh, Naomi-chan?"
    "Naomi blushed with a faint smile and looked down at herself, and then back over at us. She easily stood two heads taller than us now."
    show GTS happy
    GTS "W-Well, no, that's not... I mean it's simply my growth factor, I don't think music would exacerbate that, do you think that's possible?"
    MC "No, not at all. Honoka's just teasing you."
    "I fixed a glare in Honoka's direction, as she stuck out her tongue and scratched the back of her head."
    BE "Haha, yeah. Just messing with ya, Naomi-chan. It's not like drinking milk would make my growth factor kick into extra, mega-powered overdrive or anything like that."
    MC "But, hey. It seems like you're using your new height for an excellent purpose. I remember you trying to water those plants around the first day of school. You were struggling to reach them all."
    GTS "Hehe, that is true. It's much easier to tend to them all now. I suppose if I wanted to consider it a little further, being higher up also allows me a chance to see them from a better angle."
    GTS "That makes it easier to see them when they've all bloomed, and make sure they've been spaced out properly when they've just been planted."
    show BE surprised
    BE "Ooh! I just got a wicked cool idea."
    show BE neutral
    BE "If you get a bit taller, then you would be a wizard at making those floral displays where people plant a whole bunch of things in the ground, like an entire field's worth."
    show BE happy
    BE "Then when they bloom, they make something cool like a country's flag or a famous picture or even just a neat rainbow spiral!"
    show GTS neutral
    GTS "I've seen those before. Not in person, on a grand scale. But I know what you mean. That would be quite the project to tackle."
    MC "If you wanted to do it I'm sure it would be great."
    show GTS happy
    GTS "Hehe, well, if Seichou ever decides to reserve a large amount of space for such a thing for several years, I'll let you know and perhaps the two of you can assist me in coming up with a design for it."
    "I pointed to a group of flowers near the side closest to Naomi."
    MC "I like these ones. What are they? It looks like a..."
    if getSkill("Academics") > 5:
        jump BE036_c1_1
    else:
        jump BE036_c1_2

label BE036_c1_1:
    MC "A chrysanthemum?"
    GTS "Oh, yes, that's correct."
    show GTS neutral
    GTS "It's name comes from ancient Greek, I believe, translating to 'gold flower'. But like most flowers they've been bred and crossbred so many times that you can find so many colors that are still technically considered 'chrysanthemums'."
    MC "I was about to say this one isn't very gold in color."
    show GTS happy
    GTS "Indeed. But I think they have some more gold-tinted ones on the other side of the school? It's a bit tricky keeping track of them all."
    show GTS neutral
    GTS "But chrysanthemums are quite old in terms of cultivating them. Over 2,000 years of history in these cute little petals. They're rather special, in a way."
    show BE angry
    BE "Errrrr, they are?"
    MC "Well, 'special' in a sense, right? I know they've been used before. I've definitely read about them. I think it was..."
    menu:
        "Cultural History.":
            jump BE036_c2_1
        "Warfare History.":
            jump BE036_c2_2

label BE036_c2_1:
    MC "Yeah, the Chrysanthemum Festival... I've never been to one, but it's a big deal on the ninth of September."
    MC "People literally make tea or alcohol out of the flowers. Neither sounds particularly tasty but it's what they chose as the symbol for driving away danger."
    MC "Or celebration, too. Festivals never really keep their initial meaning for very long do they? But, whatever excuse people will come up with to have a bit of a party. I think it's done in a few other countries too. China, for sure."
    show GTS happy
    $setAffection("GTS", 1)
    GTS "Oh, you're very knowledgeable. Don't take this as me knowing every little detail about every little flower out there; but chrysanthemums were one of those flowers believed to have special properties."
    GTS "Better health, driving out demons. All that spiritual sort of talk they tended to apply to special sigils or traditions."
    show BE neutral
    BE "Bwuhzat? Demons?"
    "Honoka's head perked up suddenly, a small trail of drool visible on the side of her lips."
    MC "We were talking about flower festivals. Not as famous as the cherry blossom one, but still a neat idea."
    BE "Ah yes. Flower festivals. Mm. Riveting. Shame you can't really eat flowers, though."
    GTS "Actually, every part of a dandelion is edible! Though that's technically a weed, not a flower. Though even speaking of weeds, even plants like stinging nettles can be eaten if they're just treated properly..."
    show BE neutral
    BE "Ah, I... I actually meant more in a 'put it in a candy bar' sense of 'edible'."
    show GTS sad
    GTS "Oh. I see. Well. I should return to watering these plants. They won't water themselves. I mean, rain would do it, but I don't think it's predicted for a few more days."
    MC "I got what you meant, it's cool. Come on, Honoka. Now you've got me in the mood for a candy bar."
    jump BE036_after

label BE036_c2_2:
    MC "Something we learned in history class. We were being taught about the Sengoku period. All those armies and generals and legendary heroes fighting for a chrysanthemum-engraved throne."
    show BE happy
    BE "Aw yeah. That's the good stuff. Everyone was fighting and warring just to get on the Chrysanthemum Throne!"
    BE "It was like a war every other year just to sit on a big chair. I mean, that was more symbolic but you're right, they made a big deal out of the sigil."
    MC "Right, right, it's literally our Imperial Seal. Big gold flower. Kind of hard to miss now that I actually remember what it looks like."
    MC "Ha, in fact, if I remember correctly, there was an Emperor who was exiled at one point and made his own seal based on the flower. But while the official one had sixteen petals, his had seventeen."
    MC "He was basically saying 'Nyeh, screw your government, I'll make a better one. And mine is going to have MORE petals. Deal with that!'"
    BE "Ooh, ooh, I know this one! Emperor Go-Daigo! I think the story about him taking on a unique seal like that is kind of a myth but I like to think it's true. Because it's a hilarious amount of pettiness."
    $setAffection("BE", 1)
    BE "When I become the Empress of Japan, I aspire to be that smug. I'll make a nineteen-petal seal. We're skipping right past eighteen."
    show GTS neutral
    GTS "Empress of Japan?"
    MC "I'll admit that idea worries me a bit as well."
    BE "Ha. What? Are you kidding? I'd be an excellent ruler. Nobody would be getting their butt in that throne while I'm around!"
    show BE unique
    BE "Unless Shiori-chan managed to sit in it first. Then nobody's ever getting her out of it, unless she grows too big and busts out of it, hehehehe."
    show GTS sad
    GTS "Ah, I was unaware that it was used for something so... unseemly."
    MC "Ah. Sorry to bust the oblivious bubble. Just, kind of interested in stuff like that. Nothing's ever kept pure or wholesome for very long."
    show GTS happy
    GTS "I suppose that's true. Well, I'll stick to the happy, joyful flowers for the time being. I think I saw some weeds earlier that need pulling."
    MC "Gotcha. Good luck with that. Think Honoka and I will head back and play something, then... I think she's got a craving for battle now."
    BE "Yesss... all shall be crushed."
    jump BE036_after

label BE036_c1_2:
    MC "An azalea?"
    show GTS sad
    GTS "Oh, no. Not quite. There are actually chrysanthemums. Azaleas are typically large shrubberies so you wouldn't typically see them mixed in with a variety of other flowers like this."
    MC "Ah, nuts. Heh, it was just a guess, though. I just pulled the fanciest-sounding flower name out of my head."
    show GTS neutral
    GTS "Of course. I can see where you made a mistake. The basic chrysanthemum is golden in color but these are a pinkish variety which is close to a common azalea in shade."
    show GTS happy
    GTS "And both flowers actually have festivals dedicated to them, though I would say the chrysanthemum one is more famous, though I believe I heard azalea festivals have spread to America while others have not."
    show GTS neutral
    GTS "That may just be due to how easier it is to grow azaleas in their climate, though? I haven't really read up on the specifics, it's just something I've noted when passing the time learning about these."
    show GTS happy
    GTS "Oh, now I'm wondering if it would be possible to successfully cross-pollinate the two species. It's probably been attempted already but it would be something interesting to look into..."
    show GTS neutral
    GTS "Oh! I'm sorry. I've been rambling. What were we talking about?"
    $setSkill("Academics", 1)
    MC "Ah, heh. I don't really remember anymore? But I got a quick lesson out of it, so I can't say it was time wasted, right?"
    show GTS happy
    GTS "Well, according to a nobel prize-winning philosopher, 'The time you enjoy wasting is not wasted time.'"
    show BE neutral
    BE "Hmmm. That may be true. But that impromptu factoid burst just overloaded the amount of info I can learn in one day."
    show BE happy
    BE "Kei-chan, wanna head back to the dorms and just, hang out inside and watch tv or something?"
    MC "Heh, sure. That's fine. It was good seeing you, Naomi-san. Have a pleasant day."
    GTS "You as well."
    jump BE036_after

label BE036_after:
    "With our impromptu discussion about flowers finished, I grabbed Honoka's hand and headed back to my room so we could hang out inside."
    "We'd had enough outside time, it was candy and couch time."
    jump daymenu

label BE037:
    if getFlag("HONOKA_COOKING"):
        $setProgress("BE", "BE038A")
    elif getFlag("HONOKA_SOFTBALL"):
        $setProgress("BE", "BE038B")
    scene Lake Road with fade
    play music Schoolday
    show BE happy with dissolve
    BE "Kei-chan. You're very comfy."
    MC "The feeling is mutual, Honoka."
    "Having Honoka's breasts on top of my head was a bit of a pain on my neck, but the soft, comforting embrace of her bosom against my head was too good to pass up."
    "Occasionally, Honoka squeezed them together or moved them around in a circular fashion just to make my head move around. It was quite nice being her boob-rest."
    MC "Your back must really be sore for you to want to leave them on my head so often."
    BE "Oh, absolutely. It's just killing me. If they get any bigger, you'll just have to carry them around all the time. It'll save me money on bras, too."
    MC "Gosh I would hate for that to happen. What a life I would lead if I just had to follow you around and hold your breasts. It's not something that anyone at all would envy."
    "I was fairly certain that if anyone had been around, their eyes would have rolled so hard from the thickness of our sarcasm that they'd be turned permanently cross-eyed."
    "Honoka and I had spent the afternoon working on homework together with Aida and Shiori, just working together on some difficult assignments. It had taken longer than both of us figured."
    "Now we hung out by the outskirts of the campus. My shoes laid beside me as I dipped my feet in the water of the small river nearby, while Honoka rested her rack on my head from behind."
    show BE unique
    BE "I really like this place."
    MC "My head?"
    show BE happy
    BE "No, goober. This little dock. It's always so quiet, it's nice. It's not like Seichou's loud or anything, but it's just..."
    show BE neutral
    BE "I dunno, it's neat that there's something this peaceful right next to a big campus full of big people."
    MC "No, I think I get it. And it's like our own little spot too."
    "I looked up when I felt a shift in Honoka's weight, and could just barely make out her looking from one side of the bridge to the other. It was mainly my own hair that blinded me, surprisingly."
    MC "What are you looking at?"
    BE "Mm, I'm just considering something."
    show BE unique
    BE "I mean, clearly I'm 'not' done growing yet... I'm wondering if they could get big enough to fill up this entire bridge."
    MC "The whole thing? That's certainly a lot of room to cover."
    show BE neutral
    BE "Mm-hm."
    show BE happy
    BE "I'm sure it could be done somehow! Naomi-chan's getting up there in height. If she keeps it up, she might be able to reach from one end to the other."
    show BE surprised
    BE "Oh no."
    MC "What?"
    show BE neutral
    BE "Well. If Naomi-chan could fill this space first, that's fine. That's understandable. But what if Shiori-chan's booty gets so massive it fills this place first?!"
    show BE sad
    BE "Then she could stake a claim on it."
    BE "Name it 'Matsumoto Mounds Bridge'."
    show BE unique
    BE "And my poor little breasts would be trying desperately to catch up to try and push her out!"
    MC "Honoka, I'm only getting out from under your boobs to look you in the eyes. Because it's still really comfy down here. But this is important."
    MC "Ahem. Nobody is staking a claim on this bridge besides the two of us. We'll either name it after my hair or your boobs. But if we wanted tourism here, your boobs would certainly be a better draw."
    show BE surprised
    BE "Tourists?! Oh no wait, that's a terrible idea. Then it will be so crowded that we won't be able to do this!"
    MC "This? Wha-"
    "'This' wound up being Honoka pressing her breasts into my chest so hard that I was pushed down to the ground, though thankfully I was able to catch myself and soften the blow."
    "Honoka's lips then met mine, and I felt the swiftest touch of her tongue slide into my mouth for a moment. I closed my eyes and returned the smooch, letting my hands reach down to her waist."
    show BE neutral
    BE "Mmf?"
    show BE unique
    BE "Kei-chan, you've got all this titty on top of you, and you're reaching for my waist?"
    "I smirked. What an easy opening to tease her."
    MC "You didn't let me finish."
    "My hands wandered down further, and quickly slipped up under her skirt to grab her backside instead."
    "I'd seen her blush before. But the flushed expression on her cheeks this time was different. It grew fiercer when I squeezed her cheeks."
    show BE surprised
    BE "Wh-what are you doing?"
    MC "Your talk about Matsumoto-san must have gotten me in the mood for some butt, I suppose. You know, Honoka, you have a rather cute one yourself."
    show BE aroused
    BE "Sh-shut up."
    "Oh I just can't though. It's soft, too. Maybe I'll move my affection down here instead. Would you mind sitting on my head next time instead of doing a boobhat?"
    show BE surprised
    BE "D-Don't you dare."
    "Honoka was moaning, and shifting around on top of me. That shifting did nothing but push her boobs more insistently into my torso, and press her rump into my palms."
    MC "What's wrong, Honoka?"
    show BE aroused
    BE "Why, mmf, why aren't you playing with my boobs?"
    MC "Because they're not the only part of you that's sexy, Honoka. I'm thinking you've forgotten that."
    show BE happy
    BE "Hah, you really like my butt?"
    MC "Your butt is fantastic, yes. But not just that. Your lips..."
    "I leaned forward, through her cleavage, and met her lips once again, kissing them a few times before pulling back."
    MC "I swear they always taste like candy."
    MC "Your legs are cute too. Just a nice level of fit, and smooth, and lovely."
    "My hands went up to her head after giving her rump a quick smack, and moved some of her brunette locks behind her ears."
    MC "Your hair's very silky. I should get some tips."
    MC "But you know, I haven't even mentioned my favorite part about you yet, Honoka?"
    show BE aroused
    BE "Yeah? Go, go, go on then?"
    "I smiled, and placed my hands on her chest."
    MC "Your eyebrows."
    pause 1
    show BE surprised
    BE "Buh?"
    MC "I can't explain it. But I'll try. They're so full of life! Every little expression you make is so cute and they're a big reason why."
    show BE sad
    BE "You've gotta be kidding me."
    MC "Why would I kid about that? Each part of you is wonderful, Honoka. Even if your eyebrows are one of the smaller pieces. Especially in comparison to these huge, soft melons you're rubbing into me."
    show BE happy
    BE "Nnngh, Kei-chan, you're just the sweetest. How are you so good? Gah!"
    "Honoka grabbed onto me and rolled over so I wound up on top of her instead. My hair had gotten fairly long as of late, so as I stared into her eyes my hair formed a curtain around our heads."
    "The fading sun still shone through my own hair and allowed us to see each other as I pressed down on her chest and took a deep breath."
    MC "I'm only as good as you make me feel. So you must make me feel 'pretty' darn wonderful if you think I'm that incredible."
    "Honoka smiled and pulled me into another kiss. I didn't break this one for a while. It was too nice to stop right away. It was cozy."
    "And warm."
    "And delicate."
    BE "Mm. I'm not sure if making out in our 'sacred place' is a good thing or not?"
    MC "It's certainly memorable, isn't it?"
    show BE neutral
    BE "Oh it is. But we can't do it 'every' time we hang out here or it'll all bleed together."
    MC "Then we'll just have to make out other places instead."
    show BE happy
    BE "Yes, I like the way you think."
    MC "Should we make a schedule? Sundays here, Mondays in the dorms, Tuesday in the garden? Or should it just be a nice random-"
    BE "Kei-chan, just shut up and kiss me."
    "I did just that, and we proceeded to not worry about when or where we next kissed, and just enjoyed the moment until we packed up and went back to our dorms."
    jump daymenu

label BE038:
    if getFlag("HONOKA_COOKING"):
        jump BE038A
    else:
        jump BE038B

label BE038A:
    jump BE039

label BE038B:
    $setProgress("BE", "BE039")
    scene Baseball Field with fade
    play music Busy
    #SFX: General chatter
    MC "Let's goooo, Honoka!"
    "It was a day off of classes, and what perfect weather for it too. Honoka and her softball club were doing a match within the club."
    "With the secrecy of the school as it was, they couldn't exactly go to challenge another academy's softball club. Honoka was first at bat. The pitcher was a rather short girl with impressive thighs."
    "Her hips were fairly thick as well, but her thighs simply were the most notable part of her anatomy. Each of them looked nearly twice as wide around as her torso. While the pants for the softball uniform tended to be fairly tight they looked especially so on her."
    Umpire "Strike One."
    MC "Come on, Honoka, get it in there!"
    "Honoka swung hard at the next pitch that came her way. The pitcher turned and watched the ball go a short distance past the infield. Honoka dropped her bat and raced towards first base as quickly as she could."
    MC "Yes!"
    "Honoka made it to first base and stopped there as the second-base player had caught the grounded ball and was already back at base."
    MC "Nice job, Honoka!"
    Student "Hey, um, I don't want to be rude, but, c-could you keep it a bit quieter. I know it's exciting and all, but it's literally the first inning..."
    MC "O-Oh, yes, yes. I'm sorry. So sorry. My bad. Just excited, I'll cool off."
    "My cheeks turned red after being called out. Maybe it had been a little much. I also hadn't needed to get there as early as I had, there were still some open seats in the front benches. Thankfully I wasn't the only one, at least."
    "It would have been far more awkward if I had been the only one coming to cheer Honoka on. Whether the others with me were friends of the players, enjoyed softball, or simply had nothing better to do, it was good to give the club encouragement."
    "Honoka smiled as she readied herself for the next batter to take a swing. I could see her on as small of the base as she could possibly get without being off of it. It was the first inning, so there was no need for her to risk stealing a base."
    show BE happy with dissolve
    BE "Come on, Ichiya, smack it outta there! Make this a double!"
    "She was certainly fired up. The moment the bat connected with the ball, Honoka took off. But then came a thud from the softball landing in someone's mitt."
    Umpire "Out!"
    "Honoka hurried back to her base as quickly as she could. She hadn't been halfway across yet but the ball already had sailed back to first base."
    Umpire "Out!"
    "Various cheers and yells came from the crowd and other players at the play. Honoka stood up and grumbled, but didn't dispute it. She'd run towards base too late, the ball touched her before she stopped."
    show BE angry
    BE "DAAAAAAAAAANGGGIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIITTTTTTTTTTTT!"
    MC "Nice try, Honoka. You'll get 'em next time."
    "After losing two of their runners already, motivation for Honoka's side must have been down, as their third hitter struck out. They switched sides and Honoka took her position at one of the bases."
    "I had no clue if the infield was supposed to be a more skilled position than the outfield, but either way Honoka looked raring to go. Payback time."
    "Honoka and her team held steady on the second half of the inning. Nothing came Honoka's way but it looked like she was always ready to go, no matter what."
    "At the end of the fourth inning, a break was called so the teams could grab food, water, and take a bathroom trip if they needed. I took the time to go down and see Honoka."
    show BE sad
    BE "Phew, dang. Down 2 to 1. Thought we'd be doing better than this!"
    MC "Hey you're doing good. There's still five innings left, right?"
    show BE neutral
    BE "Three. Softball's only seven, Kei-chan."
    MC "Oh! Well, still you're only down by one point. You just need two runs to win the game, you can easily do that."
    show BE happy
    BE "Heh, it shouldn't be hard. But this is a lot more tense than other sports I've played."
    MC "How so?"
    show BE neutral
    BE "I dunno. It's like, Because you're not always active, it kind of makes my brain slow down. Soccer or basketball or whatever, I'm always moving around. So the blood stays flowing."
    show BE angry
    BE "Here, you spend so much time sitting down or waiting for a ball to be hit that you get stupid. I feel myself becoming more of a bimbo with each passing inning!"
    show BE surprised
    BE "Help me, Kei-chan, by the end of the game I'll start wanting to dye my hair blonde and get nail extensions."
    "I pinched Honoka's cheek."
    show BE angry
    BE "Ow ow ow ow."
    MC "No no, no dum-dum Honoka. You're gonna do fine. Besides you'd make a terrible blonde and you know it."
    show BE happy
    BE "Ha. Yeah, I would. Mmm, I probably will only be at bat once more before the game's over so, I gotta focus. I wanna get one of those points!"
    "I figured she needed some extra encouragement. But I wasn't sure what to say. She walked off for a bit to grab an orange, leaving me to ponder what I could cheer her on with..."
    "The minute whistle ran out letting the players know they were supposed to get back to their positions for the fifth inning. I grabbed Honoka before she walked back over, having come up with a cheer."
    menu:
        "Encouraging cheer.":
            jump BE038B_c1_1
        "Flirtatious cheer.":
            jump BE038B_c1_2

label BE038B_c1_1:
    MC "Honoka's our champ, brighter than a lamp!"
    extend " She can win the team this game and put it on a stamp!"
    extend " Power-hungry Inoue, she can so go all the way!"
    extend " Swing that bat and hit the ball to make her teammate's day!"
    MC "Goooooooo Honoka!"
    "I grabbed Honoka's wrists and threw them up in the air to get her cheering along with me. My cheeks were beet red as she giggled and giggled."
    BE "Hehehehehe, oh, Kei-chan. You're not exactly cut out for the poetry club but I liked it. Thanks. I'll do my best!"
    "With that, Honoka got back on the bench, waiting for her turn to come up again."
    jump BE038B_c1_after

label BE038B_c1_2:
    MC "Honoka's the beauty queen who'll make her debut on the scene!"
    extend " She'll win this game and get her fame and be the hottest dame!"
    extend " Her bust will bust their heads and send them crawling to their beds!"
    extend " I'll share a kiss to give her bliss and make sure she won't miss!"
    MC "Goooooooo Honoka!"
    "Then I quickly pecked her on the lips as I held her hands. My cheeks were fairly pink from the cheesy lines I'd come up with. But Honoka's were even more red."
    show BE aroused
    BE "Hah... hahaha... Kei-chan, yo-you... mm. You tease! How am I gonna focus like this, now? Oof, I'll get you back for this! Thank you! I'm all fired up now!"
    "Honoka laughed as she got back to her position and smacked her cheeks a few times to try and get rid of her blush."
    jump BE038B_c1_after

label BE038B_c1_after:
    show BE happy
    "The game kicked back into gear, and the teams didn't miss a beat in regards to their energy levels. The first player on Honoka's team hit a wide ball that went so far that the outfielder couldn't catch it in time."
    "The runner wound up getting to second base before the ball got into play, and took third base before they had to stop. It was a very tall student with extremely long legs. I couldn't help but wonder if that gave him an advantage."
    "The inning finished soon after, but thankfully the player was able to score a point before it ended, tying the score. It stayed stable as it went into the eighth inning. After the first person on Honoka's team struck out, it was time for her to be at bat again."
    "I could see Honoka's chest heave deeply as she took a breath to steady herself. The first ball whizzed past her. The second ball clipped her bat and flung off into the side of the cage. With the next hit, she smashed the ball straight into the gap between first and second base."
    MC "Go go go go go!"
    BE "Woo!"
    "Honoka yelped as she raced towards first base and slid into position just to be safe. The game was tied with two innings left, meaning there was just as much time to lose as there was to win."
    "When the next batter came up, they hit a ball that landed safely in the third baseman's mitt, making them go out instantly."
    "Honoka looked nervous. Her foot was planted more firmly on the plate than it was the first time she got on base."
    "The next person at bat managed to push them both forward a base, leaving Honoka halfway to home plate. She was antsy as she moved back and forth on the base."
    "Honoka watched the pitcher as they threw the ball and it got a nice solid hit up in the air. It looked easily-caught, so she was careful and stayed put. Her intuition was right on the money as the ball was caught leaving her stuck there with only one out left."
    if getSkill("Athletics") > 8:
        jump BE038B_pass #+1
    else:
        jump BE038B_fail

label BE038B_pass:
    "I looked over at the third base player. They seemed a bit focused on the batter, and seemed to not notice Honoka was unsure about whether to steal or not."
    MC "Honoka! Steal!"
    "I wasn't sure if Honoka heard me or not, but she made her move. She raced towards third base as quick as she could. The pitcher noticed right before she was about to throw, and chucked the ball towards the third base."
    "They whiffed. The ball missed the third baseman and landed in the ground behind them. Giving Honoka time to get to the third base. But she didn't stop there. Her feet smacked into the ground hard as she zoomed to home plate."
    MC "Go go go go go go, Honoka go!"
    "A few others began cheering for her as the ball was recovered and thrown towards home plate. Honoka dove for the plate and jumped at the last second."
    "Her hands were right on the base as she wound up bust-down in the dirt."
    Umpire "Safe!"
    BE "Wooooooo yeah that's what I'm talking about!"
    "Honoka looked happy as could be as she stood up, despite being covered from head to toe in dirt."
    show BE surprised
    BE "Yeah, I scored. I scored, I scored, I scored."
    "She sang musically as she made her way back to the dugout. The player who'd been on first looked stunned and hadn't moved an inch, which was probably for the best. When the next player swung, they seemed to take on Honoka's energy."
    "They wound up getting all the way to home base before the ball managed to tag their other player out. But they'd managed to score, currently leading at 4-2."
    "After that, there was an inning and a half left but the other team couldn't make any points to round up the score. Leaving Honoka's team the victor."
    show BE happy
    BE "Keiiiiiiii-chaaaaan!"
    "Despite hearing her approach for once I still wasn't able to get out of the way of Honoka's tackle. She wound up smashing into me, knocking us both into the grass. She snickered as she looked down at me from above her twin mountains."
    $setAffection("BE", 1)
    show BE neutral
    BE "I won."
    MC "Yeah, yeah ya did. You're also crushing me."
    show BE unique
    BE "Yeah that happens. We lost two other teammates this week."
    "Honoka chuckled at her silly joke as she helped me up. Now my back was streaked green while her front was covered in tan dirt."
    MC "Well congrats. That was a nice steal you did at the end there. Did you hear me say that, by the way?"
    show BE happy
    BE "Hehehe, yeah. I did. I dunno I was nervous about it but when you told me to do it, I just went for it! It worked. I mean, we maaaay have won either way, but this feels more dramatic."
    show BE sad
    BE "I just wish it had been like, the end of the seventh inning, with a huge dust cloud around me when I landed."
    MC "Well life isn't a movie, unfortunately."
    show BE neutral
    BE "I guess not."
    "Honoka placed her hands on her bust and stuck her bosom out more prominently."
    show BE unique
    BE "Besides, who'd be able to accurately play me?"
    MC "There was this one actress that my roommate told me about recently..."
    show BE surprised
    BE "What?! Oh no, that won't do. I'm sure mine are perkier even if hers are bigger."
    MC "I'm sure they are. She does have ten years on you, after all."
    "That seemed to appease her. But then she snickered."
    MC "What is that look?"
    show BE happy
    BE "You know, Kei-chan. I'm quite dirty now."
    MC "Yeah."
    BE "So are you."
    MC "Yeah and whose fault is that?"
    show BE aroused
    BE "Well, why don't I help clean you off?"
    MC "..."
    MC "Yeah. That sounds fair."
    "Honoka took my hand and we left the field before she even had a chance to regroup with her club. Victory did tend to make her feel a lot more excitable."
    jump daymenu

label BE038B_fail:
    "Honoka looked like she considered trying to steal third base. But she decided against it, simply staying a few inches away from the plate so she had a slight lead on the next base."
    "When the batter finally connected with the ball, Honoka had a nice head start, which allowed her to get to third quickly. The softball slammed into the mitt of the third base player, which was bad news as there was a player currently headed towards him."
    "Honoka picked up speed and raced by the home plate as fast as she could. A second later one of the other players was tagged out and that half of the inning was over. Honoka was panting, hands on her knees."
    BE "Hah, hah, hah. Woo! Did I score?"
    "The cheers of her other teammates helped tell Honoka that yes, she'd managed to give them a lead. The score was now 3-2 as it went into the second half of the inning. Honoka gave a thumbs-up."
    "Then Honoka gave a massive jumping fit of glee, bouncing up and down several times in happiness as she pumped her fists in the air. Even once she stopped jumping, her breasts continued to bounce for a few seconds after."
    "She seemed too giddy from the point to get to her base properly, wandering around in a high for a moment before someone pulled her in the direction of her spot."
    "Despite her brief lack of focus, Honoka didn't miss the ball that came her way early on, and the opponent team was struck out after that. The last inning came and went fast as well, with no real threat to Honoka's team's lead."
    "By the end, Honoka pulled through with a one point lead, and went over to celebrate with her team. I gave a moment before coming back up with her to say hello."
    MC "Honoka! Congrats. Nice job there. Good win."
    BE "Hahaha. Thanks, Kei-chan. That was a close call."
    show BE neutral
    BE "Considering we didn't get any points in that last inning there, if I hadn't made it to home base on time, we wouldn't have won."
    MC "What happens if it goes into a tie, would you have played an extra inning?"
    show BE angry
    BE "Eh. Sometimes but not today because we were kind of more on a time limit. Some of the others were already getting worn out too."
    show BE happy
    BE "But, hey. A win's a win, I'm not going to argue that!"
    MC "Well I'm glad I could be here to witness a win."
    show BE unique
    BE "I like to think your little cheer helped me out. Gave me that extra little oomph I needed. Ha, what am I saying, nothing 'little' about me."
    MC "I'd say... your patience is little."
    show BE surprised
    BE "Ha, what do you mean by that?"
    MC "Hehe, I saw you trying to steal base at the end there. You looked like you were gunning for it."
    show BE neutral
    BE "Ah. Yeah. I thought it'd be cool but I guess it doesn't matter since we won. If I tried, we might have been taken out. So, I'm okay with that."
    MC "Heh. I'm glad."
    "I pulled Honoka into a quick hug and squeezed her tight."
    MC "Did you want to do anything right now? Need a shower, I bet."
    "Honoka laughed and stretched her arms above her head, causing her rack to stick out more prominently for a second."
    show BE happy
    BE "Mmf, yeah. I do. So, I think I'll want some chill time after that. Gonna hit the showers and head back to my room, wanna meet up there and we can play some games?"
    MC "Sure. That sounds good. See you in a bit."
    BE "Great! Thanks Kei-chan. Love ya."
    MC "Love you too."
    "Honoka gave another fist pump as she walked back over to her team and helped pick up the last few supplies so they could clear the field. I slowly made my way back to the dorms to have a nice relaxing time with Honoka."
    jump daymenu

label BE039:
    $setProgress("BE", "BE040")
    scene Dorm BE with fade
    UNKNOWN "Kukuku... so Honoka-chan, this is the boy I've heard far, far too much about."
    MC "Eh?"
    play music Schoolday
    "I turned around to see who else had come in. It was only after looking at the young woman walking into the room that I remembered Honoka also had a roommate."
    show BE happy at Position(xpos=0.2, xanchor=0.5, yalign=1.0) with dissolve
    show Kokutan neutral at Position(xpos=0.7, xanchor=0.5, yalign=1.0) with dissolve
    BE "Yep. Well, I mean, what other guy would I bring in here?"
    MC "Ha. Yeah, um, I'm Keisuke Hotsure. Nice to meet you."
    "She was fairly short, nearly a foot smaller than Honoka. It felt embarrassing to look down so far in order to meet her gaze. It did make it more obvious to see that she wore colored contacts that made her eyes look bubblegum pink."
    UNKNOWN "Hmm..."
    "She took my hand and turned it around. Her fingers began to run along the lines on my palm. I looked over to Honoka for help."
    show BE angry with dissolve
    BE "Just go with it."
    show BE neutral with dissolve
    BE "What do you see, Kokutan?"
    Kokutan "I see a dark, mysterious backdrop to your life. Your decades forward will be fraughtfrought with even more misery and woe, and there is absolutely no hope for you."
    MC "Uh."
    Kokutan "You will be beset by demons and devils of all sorts. You'll find yourself facing corruption and temptation from all manner of foes, and your only hope of salvation will be..."
    MC "...What? What will my salvation be."
    Kokutan "I cannot tell. I only see a large moon. Perhaps two? The lines are not yet perfected, I cannot truly tell your fate, you may wind up crushed beneath your own misfortune."
    "Honoka clenched her hand into a fist and gently bopped the young woman on the head."
    Kokutan "Owwwwwww!"
    "Kokutan's somewhat-intimidating demeanor immediately faltered, and her big, pink eyes teared up to a comical degree."
    show BE happy with dissolve
    BE "Don't let her scare ya, Kei-chan. Kokutan isn't even in the fortune telling club or anything like that. She's a tailor."
    MC "Ah, I suppose that explains the uniform."
    "Kokutan's uniform was decked out with a lot more lace than should be expected from the Seichou uniform. A nice trail of black ruffles along the bottom, with a matching bow on the front of her skirt."
    "The cuffs of her sleeves were similarly dyed black, along with the fancy lace covering the buttons on her blouse. All the black she wore matched the dark color of her hair, wrapped up into a ponytail."
    "She'd also seemed to have done something with her sleeves to make the shoulders puffier, giving her a look like she belonged more in Victorian England than modern Japan."
    Kokutan "Ah, you like? It's been fastened by a squadron of skeletal warriors, with silks dyed from the blackened blood of angelic saviors."
    BE "That means she worked on it herself."
    MC "Got it. I was not expecting to need a translator today. Honoka said your name was Kokutan?"
    Kokutan "My full name is Kokutan, the Ebony Lord of Destruction, Master of A Thousand Demons, Emperor of the New World!"
    "Kokutan extended her arms upward, as if expecting a bolt of lightning to strike the ground where she stood."
    MC "Is that really your name?"
    BE "Hahahahaha. It hasn't gotten old yet. I'm preeeetty sure her name's not actually Kokutan but she hasn't told me what it is yet."
    show BE neutral
    BE "Because if her name really just meant a specific shade of black, then fate's really messed up, because clearly I should have been named Chichi if that was the case."
    Kokutan "D-Don't laugh at my dark deeds."
    "Kokutan stuck out her tongue at Honoka, and crossed her arms over her chest. With Honoka in the same room as her, it made Kokutan's lack of breasts all the more obvious."
    "Somehow it felt more impolite to stare at a woman's lack of a chest rather than someone's over-endowment of one."
    MC "Well, Kokutan, I would never laugh at one of your dark deeds. I was just, hey, what are you doing?"
    "Kokutan approached and grabbed a thick handful of hair that reached down my back."
    Kokutan "With this amount of hair you shed on a daily basis, your body is ripe for possession if someone gets a hold of a strand. You should take care to ensure you don't leave traces of your aura around the campus."
    MC "Thankfully I don't think there's that many people here who'd be into that sort of ritual. Right?"
    Kokutan "Kukuku, if you can't know the answer for sure, then it's best to be wary either way. You don't want some fool trying to steal you away from your beloved."
    "Honoka smiled and walked back over to me. With a slight swing of her chest, she knocked Kokutan to the side."
    Kokutan "Gya!"
    "Honoka's arms wrapped around my midsection as her breasts pushed into my back. She giggled, and tilted her head to the side."
    show BE unique
    BE "Muahahaha. Foolish Kokutan. Do you truly believe that anyone could manage to wrench my soulmate away from me?"
    show BE happy
    BE "I would race through a swarm of a million stinging beasts of hellfire to ensure he never left my side. Isn't that right, Kei-chan? Even worse than that time in the woods."
    "It took a moment for me to remember."
    MC "Haha, of course."
    "I gained a smirk as well and covered one of my eyes with some outstretched fingers."
    MC "In the summer of the most blazing heat, Honoka did race through a hornet's nest to help save me from becoming a swollen mess of injuries."
    BE "And I came out from it without a scratch! Clearly they were afraid to sting my body, my entire figure too powerful for them to touch!"
    MC "There are legends in our hometown to this day of how Honoka eviscerated the entire population of hornets with just her steely gaze!"
    "Kokutan was taken aback. She stepped away, arm splayed out in fright."
    Kokutan "W-What?! Such power. How have I not sensed this impeccable killing intent before?"
    MC "Honoka's true power only comes out when I'm nearby."
    show BE neutral
    BE "And we can link our bodies as one to make a powerful being capable of anything!"
    MC "She's powerful enough to halt the Massive Bully Squad of Inaba!"
    show BE happy
    BE "And the Storm of the Decade!"
    "Kokutan fell to her knees, shivering in place."
    Kokutan "P-Please, stop. This aura. It's overwhelming. I can feel my shadow melting beneath me."
    BE "The bigger my boobs get the more my power grows! Bahahahaha!"
    "That was the line that finally broke me, and I had to catch my breath from laughing so hard. I leaned over on Honoka and looked down at poor Kokutan."
    MC "Hahaha, oh, I'm sorry Kokutan. You're okay, right?"
    Kokutan "What?"
    "I offered a hand to help her up. She scoffed, but took it and lifted herself up."
    Kokutan "Of course I'm fine. Such a brief display of power isn't enough to put down the Ebony Lord of Destruction. But your list of feats was impressive."
    MC "Heh, they're not as impressive as they sound."
    BE "Hehehe. The Bully Squad of Inaba was a trio of dogs a neighbor of ours had. They were tiny little things that would still tackle you like they were American footballers."
    MC "All you had to do to placate them was give them head pats."
    show BE neutral
    BE "And the Storm of the Decade famously only knocked over a street sign. A couple of the kids in the neighborhood talked about it with hushed voices in school as some great destruction."
    MC "It was all a big joke, really. The weatherman kind of sucked."
    Kokutan "I see. What about Honoka-chan charging through a storm of hornets?"
    MC "They were actually hornets. But, paper mache hornets that a convenience store sold as part of a display. Honoka rushed through them to help me up because I was trying to hold onto my ice cream."
    "Kokutan held onto her face in shock."
    Kokutan "Such foul trickery."
    "She smiled, and laughed uproariously"
    Kokutan "I like it! You've met with my approval, Keisuke-kun. Welcome to the fold of shadow."
    MC "...Thanks? Hey, if you're interested, Honoka and I were going to play some video games, there's room for a third player and we've got enough controllers. Wanna join in?"
    Kokutan "I have no time for the games of mere mortals."
    show BE happy
    BE "It's Breathless Warriors 4."
    Kokutan "...Can I get dibs of Ethernia?"
    BE "Sure."
    "Honoka turned to me."
    show BE neutral
    BE "You'll figure out how to get her attention. It's easy after a while. She's pretty fun."
    MC "Ah she's fine. Is Ethernia gonna whip my butt, Kokutan?"
    "I couldn't help myself and placed the palm of my hand on the top of her head."
    Kokutan "Grr... yes. And for that indignancy your character will be cursed for a thousand winters."
    "Honoka and I sat down along with Kokutan to crank out some rounds of Breathless Warriors 4. Kokutan was a bigger fan of the game than even I was. Though the fact the narration was as edgy and brooding as humanly possible was probably the main reason."
    jump daymenu

label BE040:
    "This marks the current end of Honoka's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance

label BEGTS001:
    $setTime(TimeEnum.EVE)
    scene Dorm Exterior with fade
    play music Hallway
    #Forces Feminine costume
    if getVar("BEMode") == "Tomboy":
        $setVar("BEMode", "Feminine")
        $setFlag("BEGTS001_TomFix")
    "I walked out of my dorm to get some fresh air. The sun was hanging just above the horizon, tinting the sky in a vibrant orange."
    "I pulled my arms back, then folded my hands together while rotating my neck slowly to give my body a good stretch. I had been sitting down so long during my lectures, I had become stiff."
    "Afterward, I checked my phone for any new messages. There was a single unread text from Honoka."
    BECell "<Thank you for a wonderful evening.>"
    "I read the text with a smile, then decided to send a response. I took a seat upon one of the benches outside the dorm while I typed."
    MCCell "<You're welcome, Honoka.>"
    "Within seconds, I saw Honoka's icon show that she was typing a message."
    BECell "<Oh hey, Kei-chan! Are you doing anything right now?>"
    MCCell "<Not in particular.>"
    BECell "<Would you like to meet up on the roof?>"
    "I thought it over for a few seconds before responding. Something seemed different about Honoka's texts, but I couldn't quite pin down what it was."
    MCCell "<Sure thing. I'll see you in a bit.>"

    scene Roof with fade
    "I returned to the school building and walked up three flights of stairs to the school's roof. Since beginning our classes here, Inoue-san and I had made this our little hangout spot."
    "It looked very different at sunset, however. Usually, the Sun was almost directly above us in the afternoon. When I looked towards the horizon through the safety fence, however, the Sun wasn't even visible. It had disappeared behind the trees and buildings surrounding the campus."
    show BE happy with dissolve
    "Honoka was there to greet me when I arrived."
    BE "Hey, Kei-chan! Glad you could make it!"
    MC "Nice to see you too, Honoka. What'd you call me up here for?"
    show BE neutral
    BE "Oh, nothing special. I just wanted to talk. Catch up a bit."
    "I gave a small nod in response."
    MC "Ah, okay. Wanna sit down?"
    show BE happy
    BE "Certainly. Let's."
    show BE neutral
    "Honoka took my hand, and we walked towards a bench upon the roof. I took the left side while she sat on the right."
    "We both reclined, watching the sun slowly begin to disappear under the treeline. We still had about an hour before the school locked down for the evening, but I made sure to keep my eye on the clock."
    "Honoka turned towards me. The sunlight reflected off of her hair clip as she turned."
    BE "How have you been handling your factor since you arrived? Has the medical staff given you any... special instructions?"
    MC "Special instructions?"
    show BE angry
    BE "Yeah, you know, like... stuff to do daily between classes."
    MC "Oh, you mean that. Not really. I was told to avoid cutting my hair so they can get an accurate reading on its limits, but other than that, they just... check up on me every week."
    show BE neutral
    BE "I'm glad, I'm glad. We can forget about the factor stuff every now and then while we're here. Sure, it'll always be part of us, but it shouldn't control our lives."
    show BE happy
    BE "This... this is very nice, though. I'm happy that we can take time off to just... breathe, and forget about the world."
    MC "You and me both."
    show BE neutral
    "We sat beside each other for a few more moments. That's when I heard the pattering sounds of light footsteps approaching from the stairwell."
    "Within seconds, the door clicked open. We were greeted with a familiar face."
    show GTS sad-2:
        xpos 0.0 xanchor 0.5 yalign 1.0 xzoom -1.0
        linear 2 xpos 0.2
    play music GTS
    "Naomi stepped through the door, arriving on the roof. She held a small watering can in her hands."
    GTS "Oh, ah. I apologize. I didn't think anyone else was up here."
    show BE happy
    BE "Hey, Naomi-chan! It's been a while, hasn't it?"
    MC "Good evening, Yamazaki-san."
    show BE happy:
        linear 1 xpos 0.8
    GTS "Am I interrupting something?"
    menu:
        "Not at all. We're just hanging out.":
            show GTS neutral
            GTS "Ah, that's fortunate. I just wanted to make sure the rooftop planters were watered."
        "Well, Inoue-san wanted to show me something...":
            GTS "Ah, is that so? Well, if that's the case, I suppose I can wait."
            show BE surprised
            BE "No, no! It's fine, I insist. It's not like we own the rooftop or anything!"
        "Oh! Are you checking on your garden?" if isEventCleared("GTS008"):
            show GTS happy
            GTS "That's exactly right. Have you come to appreciate the planters too?"
            show BE neutral
            BE "Actually, we were just talking. They're nicely maintained, though!"
        "Oh! Are you checking on your garden?(disabled)" if not isEventCleared("GTS008"):
            pass
    show BE neutral
    "I could tell that Naomi was scanning her eyes over Honoka with a look of confusion. She clearly had noticed something different."
    show GTS surprised
    "Her expression slowly turned from one of confusion to one of astonishment."
    "Honoka and I sat there silently for a few moments, while Naomi kept her focus on Honoka. After a few seconds had passed, Naomi spoke."
    GTS "Inoue-san, I... didn't recognize you at first."
    show BE doubt
    BE "What do you mean? Am I that easy to mistake for someone else?"
    show GTS sad-2
    GTS "No, I didn't mean it like that. I meant that your attire is different."
    show GTS neutral-2
    "Naomi paused for a few seconds as she approached the two of us to get a closer look."
    GTS "You look incredible, Inoue-san. I love how you're dressed."
    show BE embarrassed
    BE "Aww. Thanks, Naomi-chan!"
    GTS "What prompted the wardrobe change? Just a personal preference?"
    show BE neutral
    BE "Yeah, pretty much! That, and Kei-chan seems to like it."
    show GTS unique-2
    GTS "I see. Well, he's certainly helped you pick out a lovely outfit."
    show BE embarrassed
    BE "Oh stop, Yamazaki-san! You're flattering me!"
    GTS "The praise is well deserved, though!"
    "Honoka and Naomi continued to talk while Naomi slowly watered the rooftop planters."
    MC "Well, you two certainly seem to be getting along."
    show GTS neutral-2
    GTS "There usually isn't anyone here during the evening. You caught me off guard, is all~"
    show BE happy
    BE "Still. It's been a while since we've all been together like this. We sat next to each other at orientation, right?"
    GTS "That we did."
    show BE sad
    BE "Gosh, it feels like that was forever ago, though. I know it hasn't been THAT long, but--"
    show GTS unique-2:
        linear 0.3 xpos 0.3
    GTS "Inoue-san?"
    show BE neutral
    BE "Yeah?"
    GTS "Would you like to hang out more often?"
    "Honoka's eyes darted to attention as Naomi spoke. Naomi had finished tending to the planters, and was now looking directly at Honoka."
    show BE happy
    BE "Well... sure! That'd be fun! Do you have any particular place in mind?"
    show GTS unique-2:
        linear 0.3 xpos 0.2
    show GTS happy
    GTS "A few. Shall I add your number so we can make the arrangements?"
    BE "Sure, sure!"
    "I watched as Naomi and Honoka pulled out their phones to add each other's numbers."
    show BE neutral
    BE "I guess I'll see ya around, then!"
    show GTS neutral-2
    GTS "We certainly shall. I'll see you then, Inoue-san."
    MC "See you later, Yamazaki-san."
    "Naomi gave us both a respectful, graceful bow as she opened the door to the stairwell and returned to the school building."
    play music HigherEdu
    show GTS neutral-2:
        xzoom 1.0
        linear 2 xpos 0.0 xanchor 1.0
    play music Schoolday
    show BE neutral:
        linear 2 xpos 0.5
    BE "It's about time we head out too, isn't it, Kei-chan?"
    MC "Would you like me to walk you back to your dorm?"
    show BE happy
    BE "I'd like that very much!"

    scene Campus Center with fade
    show BE neutral with dissolve
    "Honoka and I walked down the stairwell and exited the school building. The sun was still hanging just above the treeline, so we had a few hours left in the day."
    BE "I'm glad that Naomi-chan is in such a good mood. We really hit it off today, huh?"
    MC "She was the first person we met when we first arrived here, after all. Would you say that it's more than coincidence?"
    show BE happy
    BE "It might! She seemed to really like my new clothes."
    MC "You know... depending on where you two end up hanging out, you could surprise her with your dress."
    show BE angry
    BE "Something that formal? For a casual get-together?"
    MC "Well, no. It'd have to be something appropriate. I'm sure she'd love it, though."
    show BE neutral
    BE "We could bring her along for a nice meal at that sushi place, or... see a show at the theater! I wonder if Naomi-chan would be into arcades?"
    MC "As long as she fits under the ceiling, she might."
    BE "Right, right... well. Regardless of what we end up picking, this was fun!"
    show BE happy
    "Honoka turned towards the cherry tree with a smile as she began to depart."
    MC "It was! I'll see you around, Honoka."
    BE "See ya!"

    scene black with fade
    "As I headed back to my own dorm, I reflected on what had happened."
    "I just witnessed the beginnings of what could potentially be a strong friendship between Inoue-san and Yamazaki-san. Was it really just her change in clothes that sparked their interest, or did they already have that kind of bond?"
    "Regardless of what it was, I felt good today. I was very happy to see them get along, since our meeting was partially responsible."
    "I unlocked the door to my dorm room, then headed back inside for the evening."
    if getFlag("BEGTS001_TomFix"):
        $setVar("BEMode", "Tomboy")
    jump daymenu

label BEGTS002:
    $setTime(TimeEnum.EVE) #night?
    scene Dorm Exterior with fade
    if getVar("BEMode") == "Tomboy":
        $setVar("BEMode", "Feminine")
        $setFlag("BEGTS002_TomFix")
    play music Peaceful
    "The weekend had arrived, and I found myself sitting outside my dorm room just as the sun had gone down. It was a Friday night, so I considered what I'd be doing over the weekend."
    "Unless I actively make plans with someone else, I'll usually just browse the internet, watch videos, or play games. Daichi usually has something to stream, so I'll occasionally peek in and watch what he's watching."
    "That is, when Daichi lets me see his computer. He's often documenting his findings or browsing conspiracy websites, so he'll never share his screen unless he's watching anime."
    "I was just about to head back inside when I saw a distinctively tall figure. She was even taller than the light poles, which made her stand out even more in their brightness."
    show GTS neutral-2 with dissolve
    "Another figure was standing next to her. Seeing Naomi stand next to another person made me realize just how tall she was. It was easy to forget her height when she's the only one present."
    show GTS neutral-2 at Position(xpos=0.3, xanchor=0.5, yalign=1.0), Transform(xzoom=-1.0) with dissolve
    show BE neutral at Position(xpos=0.7, xanchor=0.5, yalign=1.0) with dissolve
    "Both Honoka and Naomi stood next to the light pole. They were illuminated by the white glow covering the sidewalk."
    show GTS unique-2
    show BE happy
    "I couldn't quite make out what they were saying from here, but they seemed to be deep into a conversation."
    "I decided to approach them. The sidewalk was still brightly lit, so seeing me wouldn't come as a surprise."
    show GTS neutral-2
    GTS "...Though, most people think that they are."
    BE "Well, yeah! Unless you're familiar with the field, I'd assume the same thing."
    "Their conversation seemed to halt as I got close, though. I gave them a small wave, which Honoka repeated."
    show BE neutral
    BE "Hey, Kei-chan."
    MC "Hey, Honoka."
    show GTS neutral
    GTS "Ah, Hotsure-san. Hello."
    "Naomi gave me a small bow."
    MC "What were you guys talking about, if I may ask?"
    GTS "I was telling Inoue-san about common misconceptions with botany."
    show BE happy
    BE "Yup! Apparently most home-grown plants require way less water than most people provide."
    show GTS surprised
    GTS "It's a mistake that non-enthusiast plant owners make quite often. If they're just maintaining a basic flower display for their home, the display often goes overwatered."
    show BE neutral
    BE "That, and some store owners only remember to maintain them when they get a really fancy display."
    show BE angry
    BE "Those like... specialty fruits that they display in the store window as a status symbol."
    MC "I've seen those before, yeah. Like the cube watermelons, right?"
    show GTS neutral
    GTS "The very same."
    show BE confused
    BE "What were we talking about before the botany, though?"
    GTS "You were considering what to do tonight."
    show BE embarrassed
    BE "Right, right! I was thinking about doing stuff all week! I hardly had any time with all my classes and clubs."
    show GTS happy-2
    GTS "Oh, don't feel bad about it! We got to play volleyball, didn't we?"
    show BE shrug
    BE "Yeah, but you cheat!"
    show GTS happy
    "Naomi let out a loud, forceful laugh while covering her mouth. The imposing sound of her voice was so great, our bodies shook slightly."
    GTS "My factor is hardly a form of cheating!"
    "Honoka gave a sarcastic scoff in response."
    show BE seductive
    BE "We'd belong in different divisions anyway. I can hardly hit the ball over you!"
    show GTS unique
    GTS "Hmm? Would you rather I gave basketball a try, then?"
    show BE embarrassed
    MC "Wouldn't you get shot-clocked for holding the ball over everyone?"
    show GTS neutral
    GTS "Sarcastic as I might have been, I'd be willing to give it a try. I'm certain that Seichou has specific rules geared towards factors, after all."
    show BE happy
    BE "We'd be unstoppable, Naomi-chan! Maybe I can convince Akira-chan to join us too!"
    GTS "My knowledge is limited, but I don't think there are any body checks in basketball."
    BE "She knows how to use her strength, Naomi-chan! Just like you~!"
    show GTS happy
    GTS "I admire your athletic discipline and positive attitude, Inoue-san. It's truly something to behold."
    show BE embarrassed
    BE "I could learn a few things from you myself, Naomi-chan. You're so... well-spoken and refined and stuff. It's not easy disciplining yourself to stay like that."
    show GTS neutral
    GTS "Oh, hardly. You give me too much credit, Inoue-san."
    "The evening air billowed around us as we spoke. An audible gust of wind caused the nearby trees to rustle and stir. Honoka made a motion as if to respond, then tilted her head upwards to look at the darkened sky in silence."
    show BE happy
    BE "Oh, hey! I know what we can do tonight."
    "Naomi and I repeated her gesture, craning both of our heads to look up. There didn't appear to be a single cloud in the sky. The night had been completely clear, allowing us to see every star dotting the expansive airspace."
    MC "Would you like to watch the stars, Honoka?"
    show BE neutral
    BE "I'd like that very much, Kei-chan."
    show BE shrug
    BE "What about you, Naomi-chan? You wanna join us?"
    show GTS embarrassed
    GTS "If you would have me."
    show BE happy
    BE "Of course we'll have you! Right, Kei-chan?"
    MC "Absolutely."
    show GTS sad
    GTS "I appreciate it. I'm fully aware that our options are limited due to my size, so if you're just trying to accommodate me--"
    "Honoka held up her hand with a wide smile before Naomi could finish her sentence."
    BE "Naomi-chan. It's fine. Really, it is! We've all got factors. You don't need to be so hard on yourself."
    show GTS neutral
    "I could see the fog surrounding Naomi's expression clear up as she listened to Honoka talk. Clearly, she had said something right."
    show GTS embarrassed
    GTS "Thank you, Inoue-san. Thank you. I... need to remember to see value in my company. Our factors don't make us burdens."
    MC "I'm glad that she's helped you see it that way, Yamazaki-san."
    GTS "The thoughts of what difficulties my size will bring come and go, but Inoue-san helps keep me positive. Mental fortitude can only get one so far."
    show GTS neutral
    GTS "Shall we be off?"
    MC "I'm ready if you're ready. Honoka?"
    show BE neutral
    BE "Right behind ya!"

    #night sky
    scene black with fade
    #BGM: To be decided
    "The three of us walked to an open field with a small, steadily inclining hill to the Northeast of campus. It was just passed the entrance to the GTS dorm, so the walk only took us a few minutes."
    if not isEventCleared("GTS020"):
        "Naomi struggled to find the correct pace to her strides. Due to her immense height, she needed to stop in her tracks every time she outpaced us."
        "She swayed idly on her heels as she waited for Honoka and I to catch up. It looked like she clearly didn't intend to walk so fast. Her strides just naturally took her further."
    else:
        "Since I had been spending a lot of time with Naomi, we had already gotten used to walking alongside each other. She kept perfect pace with the two of us, intentionally placing her strides at the perfect distance."
        "She was a natural at it by this point. If not for the occasional heavy pulse in her footsteps, It'd be almost impossible to tell we were walking next to someone so tall."
        "...Well, until we looked to our sides, that is."
    "Honoka stretched her arms up with two fists clenched. She seemed eager to lay down in the grass."
    BE "This seems like a good spot!"
    MC "Works for me."
    "Honoka seated herself, then rocked backwards until she was laying flat upon the ground. Her entire body wobbled before it finally came to a halt."
    "With an imposing thoom, Naomi soon joined us. Despite being over double our heights, she still found a spot for herself upon the hill. She rested herself to Honoka's right, while I reclined to her left."
    "Honoka's body made it somewhat difficult to see Naomi, but it didn't matter much since the three of us were focused on the sky."
    "Honoka inhaled as she relaxed. Naomi inhaled as well, with a much lower and hollower tone."
    BE "Really takes you back, doesn't it, Kei-chan?"
    MC "To the sleepovers we used to have when we were kids?"
    BE "Mhm. Exactly."
    "I could hear Honoka shifting her position and moving her arms. From my peripheral vision, I could see her faintly crack a smile."
    BE "Hey, do you remember that one time..."
    MC "Oh, here we go..."
    BE "--That one time we watched a DVD before we were supposed to sleep?"
    MC "The one that was way above our age rating at the time?"
    GTS "Did you two lose your innocence that early?"
    BE "Pff, nah! It wasn't porn. It was more of a horror film."
    MC "I thought the cover looked really cool, which is why I chose it..."
    BE "The one with all the silhouettes of the students, right?"
    MC "Yep. Where they're all sent to an island with limited supplies, food, and water... and told to kill each other."
    "I heard Naomi physically recoil at my summary."
    GTS "I think I know which one you're talking about. That sounds horrific to watch during a sleepover. How old were you two?"
    MC "Around 11 or 12."
    BE "We were so afraid, we shut the DVD player down and kept the lights on the entire night!"
    GTS "Having the lights on can be very comforting when you're afraid."
    GTS "Though, to watch a film like that when you're 11..."
    MC "Believe me, I regret it. In a way, though... it was okay. I got to see a new side of Honoka that day. She has this natural talent of just... saying the right thing to make you feel better."
    BE "Even back when I was a kid?"
    MC "Your friendliness was, and still is, one of your best traits, Honoka. You can always find a reason to smile."
    BE "For better or for worse!"
    "I could hear Naomi roll over, causing the grass around her to crunch and rumble. She then slightly shifted her position, laying on her side rather than her back. Honoka and I sat up in response."
    show BE neutral at Position(xpos=0.3, xanchor=0.5, yalign=1.0), Transform(xzoom=-1.0) with dissolve
    show GTS neutral at Position(xpos=0.7, xanchor=0.5, yalign=1.0) with dissolve
    GTS "It certainly sounds like you two had a fun childhood."
    show BE seductive
    BE "What about you, Naomi-chan? Do you have any fun stories to share?"
    show GTS embarrassed
    GTS "You're gonna think it's stupid."
    show BE happy
    BE "Ooh, I promise I won't! C'mon, tell me!"
    show GTS neutral-2
    GTS "All right, all right~"
    show BE neutral
    "Naomi let out a defeated exhale, followed by a giggle. We could hear the idle sounds of crickets chirping in the distance as the night breeze continued to rustle the trees."
    GTS "Once, I wanted to prepare takoyaki by myself. I saw it a few times on those home shopping shows where they demonstrate different appliances."
    show GTS neutral
    GTS "We had most of the necessary ingredients at our house, but we didn't have a specialized tray specifically for making takoyaki."
    MC "Those trays with the little circles on them?"
    show GTS unique
    GTS "Correct. The very same."
    show GTS neutral
    GTS "Since we didn't have a tray small enough for takoyaki, I ah-"
    show GTS embarrassed
    GTS "I ended up using a muffin tray instead. So instead of having a neat serving of 8 perfectly cut takoyaki balls, I ended up just making around -- two muffin-sized wads of octopus."
    show BE confused
    BE "Did they taste good, at least?"
    show GTS neutral
    GTS "My dad was genuinely impressed that I made something edible, even if the serving was completely wrong. That was the first time I had ever seen him laugh."
    show BE doubt
    BE "Wait... how old were you at the time?"
    GTS "Around 8 years old. My dad wasn't usually one to break tradition or display a lot of emotion, but to see his daughter make something so hilariously off--"
    show BE happy
    BE "You didn't make a mistake! You invented a completely original cuisine!"
    show GTS embarrassed
    GTS "I suppose that's one way of looking at it~"
    stop music
    "The night air came to a halt as the three of us spoke. The wind had calmed, leaving the trees completely still. Silence surrounded us as we looked up at the stars once more."
    show GTS neutral-2
    show BE neutral
    BE "I don't know if there are any constellations among those. I've never really looked for them outside of a textbook."
    GTS "Neither have I. Still, a clear night sky has a very strong calming effect, doesn't it?"
    show BE happy
    BE "Yeah, it does. I had a chance to just... slow down, and watch the stars. Even if I focus on just one point, I can slowly shift my eyes and just... get lost in the sea of darkness."
    show GTS unique-2
    GTS "You're a poet, Inoue-san."
    show BE embarrassed
    BE "Oh, shut up~! I bet you could come up with something better, since you can see them closer."
    GTS "I'll trust your judgement, Inoue-san. Your phrase was a lovely way to describe a sea of stars."
    show BE neutral
    BE "Would you like to head back now?"
    show GTS neutral-2
    GTS "Sounds good to me. Are you ready to go, Hotsure-san?"
    MC "Right behind you."

    scene Dorm Exterior with fade
    "We made our way back to the dorms. We had been out for quite a while, so the school building was locked down. The light poles that previously illuminated the sidewalk were now off."
    show GTS neutral-2 at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    show BE neutral at Position(xpos=0.2, xanchor=0.5, yalign=1.0), Transform(xzoom=-1.0) with dissolve
    BE "Thank you for spending time with me, Naomi-chan. This was wonderful."
    show GTS unique-2
    GTS "I'm glad you had fun, Inoue-san. It was your idea, though!"
    show BE happy
    BE "It doesn't matter that it was my idea. Your company made it better."
    GTS "I feel the same way, Inoue-san. I value your company just as much."
    show BE embarrassed
    BE "Awww~"
    show GTS neutral-2
    GTS "Shall we schedule something else next week?"
    show BE neutral
    BE "If I'm not too busy with school work, sure!"
    show GTS unique-2
    GTS "Fantastic. I'll see you again soon."
    "Naomi gave us both a small bow. She was so tall, however, that a bow from her loomed over both of our heads."
    MC "See you around, Yamazaki-san."
    GTS "Farewell, Hotsure-san."
    hide GTS with dissolve
    show BE neutral at Position(xpos=0.5, xanchor=1.0, yalign=1.0) with dissolve
    BE "I never knew how outgoing Naomi-chan was. When we first arrived, all I saw was a timid girl in the school garden. I thought there was something mysterious about her, but I never thought..."
    "Honoka seemed to pause midway through her sentence, like she didn't know what to say."
    MC "You never thought what?"
    show BE sad
    BE "I never thought she'd be so special to me."
    "Honoka's expression clouded up in deep thought, then slowly returned to a beaming look of happiness."
    show BE happy
    BE "It's all because of you, Kei-chan. If it hadn't been for you, we would have never clicked in the way we did."
    MC "You wouldn't have hung out on the roof?"
    show BE shrug
    BE "I might have by myself, but... you were the reason we met, and I'm so happy that we did."
    MC "I appreciate that, Honoka."
    "Honoka pulled me into a firm hug before she left for the night. It was pretty difficult to wrap my arms all the way around her, but we managed to make it work."
    hide BE with dissolve
    "I took one last look at the vast, open night sky before returning to my dorm and heading to sleep."
    if getFlag("BEGTS002_TomFix"):
        $setVar("BEMode", "Tomboy")
    jump daymenu

label BEGTS003:
    $setTime(TimeEnum.EVE)
    if getVar("BEMode") == "Tomboy":
        $setVar("BEMode", "Feminine")
        $setFlag("BEGTS003_TomFix")
    scene Dorm Interior with fade
    play music HigherEdu
    "The sunlight filtered in through the windows as I brushed the hair out of my eyes. I then proceeded to brush my hair back over my eyes. I liked how my hair looked that way."
    "After checking my appearance in the mirror, I stepped out of the bathroom and made my way over to the front door."
    show RM neutral with dissolve
    "Daichi was at his computer like he usually was. I picked up my phone from the dresser and placed my hand on the doorknob."
    MC "Daichi."
    show RM concerned
    RM "Yeah?"
    MC "Headin' out."
    show RM neutral
    RM "'Kay."
    "The doorknob clicked as I rotated it. I pulled the door open and stepped outside."
    "Daichi's ability to focus on the reports he was typing was still something to behold. He barely glanced away from the screen when he responded."

    scene Dorm Exterior with fade
    "The clean air surrounded me after I headed out. I took a slow, heavy breath to take in the fresh air. It was slightly chilly, but not enough to need a jacket. A perfect temperature to just relax and take in the sights for a while."
    "I took my time as I walked. Aside from the occasional breeze and branches swaying in the wind, the campus was completely silent. I traced around the sidewalk for a while before doubling back towards the main building."
    "I pushed open the double doors to the main building and headed inside."

    scene Hallway with fade
    "I didn't often walk into the school building this late. Usually when classes were over, I'd be hanging out in my dorm or out visiting the town."
    "It seemed like I had been finding reasons to head back during the evening, however. I thought about how beautiful the orange sky looked when Honoka invited me over."
    "As I walked through the halls, I wondered how many other students checked out the roof. It was 'our little hangout spot,' sure, but we didn't often see anyone else up there. Honoka saw the work that Naomi was putting in, but did anyone else?"
    "When I neared the end of the hallway, I turned right to enter the cafeteria. Coincidentally, someone I knew was seated at one of the center tables."

    scene Cafeteria with fade
    show BE neutral with dissolve
    "She was arched over the edge while looking at her phone, which had been placed flat upon the surface of the table. She scrolled through messages with her pointer finger, giggling as she read them."
    show BE happy
    "I watched as she typed a message, energy flowing from her fingertips as they danced around the screen. I didn't look *too* close, however. Looking over her shoulder to read her messages would be awkward."
    show BE embarrassed
    "After tapping her pointer to send the message, she became awash with happiness only seconds later. I wondered what could have been sent to make her so happy and blush-filled."
    show BE happy
    "She turned towards me after reading the message, waving me closer to the table."
    BE "Oh! Hey, Kei-kun!"
    MC "Hi, Honoka."
    BE "I don't usually see you here after school. Are you following me?"
    "She punctuated her words with a sarcastic, sing-song tone."
    MC "Not exactly. I was just going to get something from the vending machine."
    show BE angry
    BE "Oooh, I see! Out for some fine dining!"
    MC "Only the best. What were you watching that made you so happy?"
    show BE neutral
    BE "Oh, it wasn't a video. I was just texting Yamazaki-chan."
    MC "Ahh. Do you have plans?"
    show BE happy
    BE "Not really. A TV drama we both like is gonna be on tonight, and I wanted to make sure we both tuned in. I don't wanna spoil anything if she hasn't seen it."
    MC "I didn't know she was into TV dramas."
    show BE embarrassed
    BE "She wasn't! I convinced her to give one a try, and now she's hooked. She said it reminded her of Japanese theater."
    show BE neutral
    BE "I believe her exact words were 'not quite as exciting as seeing the actors in person, but it still gets you invested in the story.'"
    MC "I'm glad you two found something you both like. What else have you been up to?"
    "Honoka was about to respond, but the chime from her phone indicated that she received a new message. It was impossible for her to see her phone on the table while standing."
    "With a slight chuckle and a shift of her weight, she stepped backwards and crouched to pick her phone off the table."
    show BE angry
    BE "I can't see anything below me with these things..."
    show BE confused
    BE "Maybe it'd be easier if I just set my phone on top."
    MC "If it works, it works."
    show BE seductive
    BE "I knew you'd be open to the idea."
    show BE neutral
    "I watched as Honoka placed the phone on top of her personal shelf, scrolling through the messages that way. Despite their appearance, it... was somehow a sturdy hold."
    BE "Oh, hey. Yamazaki-chan's asking me where I am. Wonder why..."
    "Honoka tapped the screen of her phone as she wrote a response to the text."
    MC "She probably just wants to hang out."
    show BE shrug
    BE "If that's the case, then-"
    "*THUNK THUNK*"
    "We heard a heavy, audible clunk which sounded like it was coming from the cafeteria window."
    show BE surprised
    BE "...So that's why she wanted to know."
    "A pair of large kneecaps and shins could be seen occupying the entire height of the first floor windows."
    "I could see the slight hem of a blue skirt pressed against the top of the window frame, but the rest of it was completely shrouded in darkness due to the immense size of the figure on the other side."
    "An upside down hand the size of a baseball mitt soon accompanied the towering set of legs. It dangled from a forearm above the window frame, belonging to an un-seen face."
    show BE happy
    "The hand slowly contorted itself so that two fingers were raised, creating a peace sign. Honoka chuckled in response."
    BE "Pfff! That's Yamazaki-chan for ya~"
    MC "She does that a lot?"
    show BE embarrassed
    BE "All the time! I'll be sitting in my dorm room, and she'll just be... there, waving at me from the 2nd story window!"
    show BE happy
    BE "C'mon, Kei-kun. She's not gonna crawl into the building, so let's go meet her outside~"
    hide BE with dissolve
    "I let out a quiet laugh as Honoka walked towards the exit."
    MC "All right."
    MCT "I never got anything from the vending machine..."

    scene Campus Center with fade
    play music MC
    "I made my way back through the hallways and out the double doors. It didn't take long to find the massive maiden that was waving earlier. She tended to stand out."
    show GTS neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    GTS "Oh my, oh my. It seems that our secret handshake is working on other people, Inoue-chan."
    show BE happy at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    BE "It's hardly a secret when you show off in front of the whole cafeteria like that!"
    MC "I thought it was a pretty good show."
    show GTS surprised
    GTS "All I did was pose with a peace sign!"
    #Following line only appears if Kei has romanced Naomi: [GTS##, filling later]
    #show GTS aroused
    #GTS "Besides, you know where to find me if you want a better show."
    #End of route-exclusive line.
    show BE neutral
    BE "Even if it was just an idol pose, people pay attention when you're so tall! You sure you're not gonna get in trouble, being so close to the main building?"
    show GTS neutral
    GTS "There aren't any rules that specifically say that I can't approach or enter. It's just ill-advised for obvious reasons."
    show BE happy
    if getSize() >= 3:
        BE "Right, right! I heard the other giants talking about that."
        MC "You've been in the giants' dorm, Honoka?"
        BE "I have, and It's so roomy! Can't wait to see how Yamazaki-chan personalizes that hangar they gave her."
    else:
        BE "Right, right! I heard the other students talking about that."
        show GTS wink
        GTS "It made having a sleepover rather difficult, though. I kept bonking my head on the door frame."
    "Honoka and Naomi shared a giggle, as well as a repeat of the unique handshake Naomi demonstrated. Since there wasn't any glass separating them this time, I could actually see them lock their fingers together."
    "Honoka's hand looked absolutely tiny inside Naomi's, but it was charming seeing how they made it work."
    "Both girls made peace signs with their index and middle fingers, slid them across each other, then pulled them apart while Honoka mimicked an explosion with her palm."
    show BE wink
    show GTS neutral
    BE "Ka-pow!"
    show BE neutral
    BE "What else have we been up to lately, Yamazaki-chan?"
    show GTS unique
    GTS "You showed me what it was like to go to an arcade."
    MC "Honoka dragged you there in my place?"
    show BE angry
    BE "Your place is still reserved, Kei-kun. I've just added someone to keep my other shoulder company~"
    show GTS unique-2
    GTS "I'm afraid your shoulder is far too low, Inoue-chan. Would you prefer that I rest my elbow on your head instead?"
    MCT "I'd like to see that, actually..."
    show GTS neutral-2
    GTS "I'll just be standing around waiting for the train, while using you to support my arm~"
    show BE happy
    BE "Is that your idea of 'leaning on each other'?"
    show GTS angry
    GTS "Hmph... not exactly. The phrase is a bit less literal than that."
    show BE shrug
    BE "Kinda like when you said we needed a 'table for two' at the café?"
    show GTS embarrassed
    GTS "No, that time we actually needed a table for two. We just ended up using a booth because it's easier for me to sit there."
    show BE happy
    BE "Hey, we made it work! Your height kinda freaked out the staff, though."
    show GTS wink
    GTS "Oh, and your breasts didn't?"
    show BE angry
    BE "Point taken."
    "Honoka and Naomi shared a sarcastic chuckle."
    show BE neutral
    "I could see them start to relax after they shared their experiences with me. Clearly, they had been through a lot these past few weeks."
    show GTS neutral-2
    "Naomi's powerful shadow loomed over both of us once more as the sun continued to set. Her head was nearly in line with the second story window of the school."
    GTS "Talking about the café made me remember how good the drinks were. I'd love to travel there again, Inoue-chan."
    BE "They're probably still open. Do you wanna head out?"
    show GTS happy
    if getRoutelock() == "GTS":
        GTS "As long as Kei-kun is okay with having you here too~"
        MC "I've known Honoka for a long time. It'll be fine having all three of us."
    elif getRoutelock() == "BE":
        GTS "As long as you don't feel that I'm not a third wheel. I know you two are an item~"
        MC "I don't mind. It was Honoka's idea, after all."
        BE "I wouldn't have asked if I didn't want us to go!"
    else:
        GTS "As long as Hotsure-san doesn't mind us talking about TV dramas all evening~"
        MC "Really, I don't mind at all. We can talk about anything."
    show GTS neutral
    show BE happy
    BE "Are we all set, then?"
    MC "Sure, I'm ready."
    GTS "You two can lead the way. I'll make sure my strides aren't too long~"

    scene Town with fade
    "Honoka and I walked alongside each other as we made our way off campus. True to her word, Naomi followed behind us. Her walking was intentionally slow, her strides deliberately short."
    show BE neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    "Naomi's shadow slowly crept up behind us as we stopped at one of the intersections to get our bearings."
    show GTS neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    "Honoka stretched her arms behind her back, bending her elbows to rub her shoulders. Naomi reclined against a light pole, which sparkled subtly in the evening sun."
    "I scanned my eyes across the illuminated signs lining the street."
    MC "There are plenty of places we haven't been. Was there anywhere in particular you wanted to go?"
    show BE happy
    BE "It doesn't need to be anything fancy. We could even just get some snacks and eat 'em outside!"
    show GTS neutral-2
    GTS "That sounds wonderful, actually. It'd be a nice change of pace from what we usually do, Inoue-chan."
    show BE shrug
    BE "You don't like ducking through door frames?"
    show GTS sad-2
    GTS "Not if I can avoid it. Feeling big is only fun for a little while. Once I've had my share of inconveniences, I begin to feel like a cat in a cardboard box."
    show BE happy
    BE "Might be more fun with packing peanuts!"
    show GTS unique-2
    GTS "Hmm. It definitely would."

    scene Store with fade
    "We made our way to a convenience store tucked away in one of the alleys on the right side of the road."
    "The path was much more narrow than the road itself, but it provided a bit more walking space than the sidewalk. A small lot with a swingset, vending machine, and phonebooth could be seen directly behind us."
    show BE neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show GTS neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    "Honoka rotated herself to the left and sidestepped in order to make room for Naomi and I. It wasn't a tiny alley, but walking was still extremely compact."
    "Naomi ducked underneath a neon sign mounted to the wall when entering the alley, then contorted herself under the heating ducts mounted to the alley walls."
    show BE happy
    "By the time we had all reached the storefront, Naomi was bracing her hands near the overhead heating ducts while craning her body downward. Honoka stood next to me, smiling innocently."
    BE "Would you mind heading inside, Kei-kun? You know, because..."
    MC "No problem. What are we getting?"
    "Honoka pulled out a pile of yen coins from a small bag. Naomi did the same from her purse."
    GTS "This should cover the cost, I feel."
    show BE neutral
    BE "We'll all pitch in, Yamazaki-chan. Don't worry about it."
    show GTS surprised
    GTS "I would still feel guilty if I felt that I didn't contribute. Please, use it."
    "I then had a generous handful of yen coins, combined with the money I happened to bring with me."
    MCT "This should be plenty. We'll be able to get a decent meal for the three of us."
    "Naomi shifted in her posture slightly, still awkwardly slouched due to the size of the alley. She was eyeing the interior of the store with a worried expression."
    show BE doubt
    BE "Is something up, Yamazaki-chan?"
    GTS "No, nothing is wrong. I just felt that I should consider how much I'll need. Two bento boxes should be plenty."
    show BE happy
    BE "Oh, yeah! Bento sounds great! Want some cup noodles to go along with it?"
    show GTS neutral
    GTS "Perhaps. I think something to drink would be more important, though. A bottle of oolong tea would be ideal."
    BE "Tea is fine! You could also get some of that protein jelly stuff I heard about, if you want. It's supposed to be really tasty."
    MC "I'll keep a look out for it. Anything else?"
    show GTS unique
    GTS "I believe we've asked for plenty, Inoue-chan."
    show BE embarrassed
    BE "You're right, you're right."
    "I proceeded into the store and picked up a stack of four bento boxes. Two for Naomi, one each for Honoka and myself."
    "I then walked over to a small cabinet in the corner of the store and picked up two bottles of oolong tea. For myself, I decided to get..."
    menu:
        "A bottle of water.":
            "I walked over to a small refrigerated cabinet in the store, and picked up a bottle of water for myself."
        "A can of cola.":
            "I walked over to a refrigerated mini-display in the store, and picked up a can of cola for myself."
        "A jar of protein jelly.":
            "I browsed the wall on the opposite end of the convenience store and found a packet of protein jelly hanging on the display."
    "I stacked it on top of the bento boxes and proceeded towards the register. There were a few impulse items lined up on a shelf underneath the display."
    "One item in particular that caught my eye was a bag of hard candy with a unique, bumpy texture."
    MCT "Why not? It'll be a nice little treat."
    "I set the stack of bento boxes on the table with the register, then placed the drinks and bag of candy next to them. With a combination of our money, there was still a decent amount left over."
    Cashier "Thank you very much."
    MC "You're welcome."
    "I proceeded out of the store, carrying the stack of food. Honoka's eyes immediately lit up with an excited smile. Naomi seemed peacefully content."
    show BE happy
    show GTS unique
    BE "Aww, yeah! Chow time~"
    GTS "I appreciate this a lot, Hotsure-san. Thank you for spending time with us."
    GTS "Would you like me to carry everything~?"
    MC "No, thanks. I've got it."
    show GTS aroused
    GTS "I insist. Allow me to carry it all."
    "A heavy, looming aura could be felt from Naomi as she craned her posture slightly lower to look at the two of us. A smile could be seen as she enveloped Honoka and I in her presence."
    show BE shrug
    BE "Sounds like she means business, Kei-kun."
    MC "Hah... all right, if you insist. Here, Yamazaki-san."
    "Naomi bent down and gathered everything I was carrying in her powerful hands. They were nearly triple the size of Honoka's."
    "She then rose to her full height, coaxing her head to the left to avoid the heating ducts in the alley."
    show GTS neutral
    GTS "Shall we be off, then?"
    show BE happy
    BE "Of course! I'm starving!"
    hide BE with dissolve
    hide GTS with dissolve
    "Naomi ducked herself underneath the neon sign and proceeded back out of the alleyway. Honoka and I followed behind, returning to the main road."

    scene Park with fade
    stop music
    show BE neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show GTS neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    "The park was only a brief walk from main street. It was a much shorter distance from here to the store we visited than from the store to Seichou."
    "Naomi was less cautious in her strides this time around. Her pace was much more 'normal' compared to the slow and deliberate steps she usually took. Her strides were also longer."
    "By the time Honoka and I had caught up, she had realized that her pace had quickened."
    show GTS surprised
    GTS "Ah. I apologize. I suppose I was eager to see this place again."
    MC "You've been here before?"
    show GTS neutral
    GTS "Once. Inoue-chan and I took a detour when we were walking through town. We didn't really stop to appreciate the scenery, though."
    show BE happy
    BE "It's absolutely gorgeous, Yamazaki-san. Thank you for recommending this place."
    show BE neutral
    BE "It's so quiet, too. Way quieter than campus."
    MC "It's true. Seichou has much fewer students than a traditional school, but even then, it's never this quiet."
    show GTS neutral-2
    GTS "I like it very much. The air is incredibly still here, and I can focus. I can't think of any better place to have a conversation."
    "Naomi slightly twisted her neck twice, scanning the area for a place to sit."
    show GTS sad-2
    "She appeared to be indecisive, prompting Honoka to walk up next to her and offer assistance."
    #Slide BE so that her sprite is directly next to GTS without overlap
    GTS "Hmm..."
    BE "Why don't we just have a seat underneath one of the trees? We can all sit in the shade."
    GTS "I wouldn't want to deprive you two of the bench."
    show BE happy
    BE "We don't mind! Right, Kei-kun?"
    menu:
        "Actually, the bench does sound nice.":
            $setFlag("BEGTS003_c1_1")
            show BE neutral
            BE "Well, you can sit on a bench nearby while Yamazaki-chan and I sit on the grass. How about that?"
            MC "That works for me, sure."
            $setAffection("GTS", -2)
            GTS "I'd rather hoped we could all share a seating space, but it seems that my height has inconvenienced you."
            #Slide BE back to her original position, screen left
            BE "You're fine, Yamazaki-chan. We're all together, here. You're not being fair to yourself if you think you're inconveniencing us."
        "We can sit underneath the tree.":
            BE "That's perfect! We'll all be able to sit together that way."
            show GTS neutral-2
            GTS "I'm glad that you two are open to the idea."
            MC "No sense in hanging out together if we can't all share a spot, right?"
            show GTS neutral
            $setAffection("BE", 1)
            $setAffection("GTS", 1)
            GTS "I suppose you're right."
    "Naomi briefly paused to collect her thoughts."
    show GTS unique
    GTS "Thank you, Inoue-chan."
    show BE happy
    BE "Don't mention it, Yamazaki-chan. You deserve more credit."
    show BE neutral
    show GTS neutral
    "The three of us then took our seats. Honoka lowered herself onto the grass first with an audible crunch. Naomi followed, with a resonating pulse forcing Honoka to bounce."
    if getFlag("BEGTS003_c1_1"):
        "I took a seat on the park bench directly next to them, turning my body to face them both."
    else:
        "I took a seat on the grass next to both of them, the three of us forming the points of a triangle."
    "Naomi handed Honoka and I each a bento box, keeping two for herself. We each tore open the cardboard package, sliding the tray out from the side."
    "The smell of noodles, chicken, steamed vegetables, salad, and rice soon filled the air. We each looked at the meals with content, satisfied smiles."
    show BE happy
    BE "God, it all looks so good!"
    show GTS happy-2
    GTS "It's very impressive the amount of variety they offer."
    show BE shrug
    BE "Something something, spice of life, right?"
    show GTS happy
    GTS "Something like that."
    "I started by eating the chicken and noodles, occasionally combining it with the steamed broccoli to create a noodle salad."
    show BE neutral
    show GTS neutral
    "I occasionally glanced at both of them while I ate. Honoka started with the rice, whereas Naomi was eating much larger bites of the chicken and vegetables."
    "Save for the occasional chirp of a bird or the leaves of the trees rustling, the area was completely silent."
    BE "..."
    MC "..."
    GTS "..."
    "We sat in silence for a few moments, before Honoka started speaking."
    show BE happy
    BE "It's been a crazy semester, hasn't it?"
    MC "What do you mean?"
    BE "I just mean, everything that's happened, you know? I've gotten used to my schedule by now, but it still feels so surreal."
    show GTS surprised
    GTS "You're referring to Seichou University, correct?"
    show BE neutral
    BE "Yeah. It's a school like any other, but getting to know all of the people I've met... it's been fun. Not many people can say they've met such a diverse set of people."
    show BE happy
    BE "I wouldn't trade the experience for anything!"
    show GTS unique
    GTS "That's very flattering, Inoue-chan. I treasure the time we spend together too."
    BE "Kei-kun's been my friend for as long as I can remember, but I made a note to get to know everyone else, too."
    if getRoutelock() == "BE":
        BE "That, and... he's much, much more than just a friend now."
    show GTS neutral
    GTS "Everyone else? Are you referring to the other students in our homeroom?"
    BE "Yeah! I think I know everyone decently well."
    MC "A regular social butterfly."
    show BE embarrassed
    BE "You know me!"
    show BE neutral
    BE "Do you hang out with the others, Yamazaki-san? I'm curious."
    GTS "I share interests with a few of them, certainly. Kodama-san asks me for botany tips occasionally. She's considering growing her own ingredients."
    BE "Kodama-san's such a sweet girl. It's impossible to get mad at her."
    MC "We also joked about forming an invincible basketball team with Mizutani-san a couple days ago."
    show GTS happy
    GTS "Hah! I remember. I said something about body checking."
    show BE seductive
    BE "She's gonna challenge you to a weightlifting competition soon, Yamazaki-chan. You can bet on that."
    show GTS unique
    GTS "I'll be certain to give her a formidable challenge."
    "The three of us paused for a few moments while we continued to eat. I decided to tear open the bag of bumpy candy, offering a handful to Honoka."
    show BE happy
    BE "Appreciated, Kei-kun."
    if getRoutelock() == "GTS":
        MC "You're welcome. Do you want some, Naomi-chan?"
        show GTS neutral
        GTS "Certainly. Thank you, Kei-kun."
    else:
        MC "You're welcome. Do you want some, Yamazaki-san?"
        show GTS neutral
        GTS "Certainly. Thank you, Hotsure-san."
    "Naomi's hand scooped up roughly the same amount as Honoka. She deliberately slowed her arm movements down to avoid crushing the pieces in her hand."
    "I could hear Honoka lick and crunch the candy for a few moments, before pressing a few pieces into her cheek so she could talk."
    show BE neutral
    BE "Who else..."
    show BE happy
    BE "Oh, yeah. What do you think of Matsumoto-san?"
    "Naomi rolled the pieces of candy in her palms for a few seconds, responding before she placed them in her mouth."
    GTS "I've got a lot of respect for the student council. A role like that must be stressful at times."
    GTS "Matsumoto-san and I both have a clear idea of self-discipline and drive. I want to present the best possible person I can be when others look at me."
    show GTS sad
    GTS "The similarities stop there, however. My idea of one's best possible self comes from inner discipline and being at peace with the person we see in the mirror."
    show GTS neutral
    GTS "Matsumoto-san is much more focused on morality and established rules. I can respect that philosophy, even if I don't necessarily agree with it."
    show BE neutral
    BE "I think that inner peace and established moral rules can coexist, since they usually agree with each other. If they conflict, though, that's when you need the wisdom to decide what you should do."
    MC "That's... pretty high brow, Honoka. I don't usually hear you talk like that."
    show BE seductive
    BE "I'm just full of surprises, Kei-kun."
    show GTS unique
    GTS "That's why I'm happy to have you, Inoue-chan. You help ease my spirits when I'm feeling conflicted."
    show BE happy
    BE "I try my best!"
    show GTS happy-2
    GTS "You succeed."
    MC "That just leaves Nikumaru-san."
    show GTS surprised
    GTS "Hm."
    "I could see Honoka focus on Naomi's face as she gradually lost her smile, a fog of uneasiness washing over her."
    show BE doubt
    BE "We didn't exactly have the best first impression. All Kei-kun and I saw was her bossing Kodama-san around."
    show GTS angry
    GTS "That's exactly why I don't have much respect for Nikumaru-san at all."
    BE "I see the good in everyone. I'm sure you just got off on the wrong foot."
    show GTS surprised
    GTS "I... envy people who have not met Nikumaru-san."
    MC "That bad, huh?"
    "Naomi paused for a few seconds, inhaling with her nose while she collected her thoughts. She then exhaled forcefully, as if quieting the storm of her mind."
    GTS "I apologize. I don't like to speak ill of other people behind their backs."
    show GTS sad-2
    GTS "Gah..."
    BE "Did something happen, Yamazaki-chan?"
    show GTS surprised
    "Naomi briefly held her wrist while her hands shook, her fists briefly clenched."
    GTS "I only felt comfortable expressing my dislikes because of how much I like you, Inoue-chan."
    if getRoutelock() == "GTS":
        GTS "Doubly so, because of how much time I've spent with Kei-chan."
    GTS "Nikumaru-san has a personality type that I just... cannot stand. I don't want to express that with the others, though. It'd make me appear hostile."
    show BE neutral
    BE "Well... you don't need to see eye to eye with her, Yamazaki-chan. As long as you don't see each other, it shouldn't be a problem."
    show BE doubt
    BE "I wish you'd tell me what happened, though."
    show GTS sad-2
    GTS "I will, Inoue-chan. I promise you. I just find it difficult to organize my thoughts right now."
    show GTS sad
    GTS "Again, I deeply apologize. I didn't intend to make the conversation so tense."
    show BE sad
    BE "Hey... Yamazaki-chan. Do you remember what I said?"
    show GTS surprised
    "Naomi slowly craned her head down, looking at Honoka with a sorrowful expression."
    GTS "Be fair to myself. I deserve credit. I'm a good person."
    show BE neutral
    BE "That's right. You need to remind yourself."
    GTS "I know... I know."
    BE "Now, give me a hug."
    #[Potential CG here.]
    show BE happy
    BE "Are you ready to head back? We can take as much time as you need."
    show GTS neutral
    GTS "I'll be all right. You don't need to worry about me, Inoue-chan."
    "Honoka gathered up the empty bento boxes and stacked them up into her hands."
    show BE neutral
    BE "Mind if I take that, Kei-kun?"
    MC "Go ahead."
    BE "I hope you had fun today, even if it got a little melancholy."
    MC "I like spending time with you two. This was nice."
    if getRoutelock() == "BE":
        show BE aroused
        "Honoka leaned closer to me to whisper into my ear."
        BE "We'll have some real fun later. I promise."
        MC "I look forward to it."
    show BE happy
    BE "Are you ready to head home?"
    show GTS wink
    GTS "I'm ready. I can carry you two, if you like."
    show BE surprised
    BE "I'd... love to see that, actually."
    show GTS neutral
    GTS "Hold on tight."
    hide GTS with dissolve
    hide BE with dissolve
    "With both of us in tow, Naomi proceeded to pick us up and carry us back to the dorms just as the sun began to disappear beyond the horizon."
    "Their discussion had me thinking about just how much more they had done with just the two of them. I was even more curious what Naomi planned on telling Honoka later."
    "I didn't need to worry about my curiosities right this moment, however. I had a pleasant walk with Honoka and Naomi before I turned into my dorm for the night."
    if getFlag("BEGTS003_TomFix"):
        $setVar("BEMode", "Tomboy")
    jump daymenu

label BEGTS004:
    scene Library with fade
    play music HigherEdu
    "I sat with my back leaned up against one of the chairs in the library. They weren't exactly comfortable, but with headphones on, I was able to space out for a while."
    "I rose the front two legs of the chair slightly off the ground, keeping my hands on the sides of the seat. When I shifted my balance, the chair tilted back and forth."
    "After I stretched and stared at the ceiling for a few moments, I set the legs of the chair back down. When the song I had been listening to ended, I took a brief glance at the clock."
    stop music
    "It was almost 3:00 PM, so I had been relaxing for just under an hour. I stood up, rolled my neck, and decided to pack up my things."
    "Once my books, phone, and headphones were inside my bag, I stepped out into the hallway."

    scene Hallway with fade
    "Reflections in the sunlight gave off a small sparkle as I passed the windows. Each time one of the clouds blocked the sun's rays, the hallway darkened."
    "I could hear the clacking and sliding of various footsteps in front of and behind me. It was passing time, so a lot of students were heading to their final class for the day."
    "As I turned one of the corners, I saw a familiar face."
    show PRG neutral with dissolve
    play music PRG
    "Aida had just exited one of the rooms on the left side of the hallway, and was walking towards the double doors at the end of the hall."
    PRG "Oh! Hi, Hotsure-san."
    MC "Hi, Kodama-san. Did you just get out of class?"
    show PRG worried
    PRG "I did. Why? Was there... something you needed me for?"
    MC "No, nothing like that. I was just curious."
    show PRG happy
    PRG "Right... right! I actually don't have any classes after this. I'm looking forward to heading back to my dorm early."
    "Aida and I began walking down the hallway together while we talked. Her pace was steady and deliberate, like she took caution with every stride."
    MC "Heading home early sounds nice. What do you usually do?"
    show PRG neutral
    PRG "Well, ah... usually, I'll catch up on my sleep if I need to. Or, I'll do homework, or draw, or something..."
    MC "Oh? You draw?"
    PRG "N-Not very well, but yes. It's a good way to keep busy whenever I find some free time."
    show PRG unique
    PRG "What have... you been up to?"
    "Aida fidgeted slightly as she spoke. Her voice didn't carry very much, so a lot of what she said had a breathy wisp to it."
    MC "School work, mostly. More recently, though, I've been spending time with Inoue-chan and Yamazaki-san."
    show PRG happy
    "Aida's pupils dilated quickly when she heard me speak, her eyes widening for a split second. She returned to a relaxed, collected expression just as quickly."
    show PRG neutral
    PRG "O-oh! That's interesting. I haven't seen those two together very often."
    "I nodded in response."
    MC "It's actually pretty recent. Yamazaki-san noticed that Inoue-chan started dressing up more, and she... liked it. She saw a side of her that she hadn't before. After that, they completely hit it off."
    "Aida inhaled slowly, then exhaled with a content huff."
    show PRG happy
    PRG "I know that feeling really well. Seeing someone in a new light can really change your perceptions. It's like... seeing someone do something you'd never think they'd do can completely change how you view them."
    "I pushed open one of the doors leading out into the courtyard. Fresh air poured into the hallway as I held the door open. The howling sound of the wind took us by surprise as a gust deafened us for a few seconds."
    "After the billowing sound of the wind died down, Aida looked at the open door with a smile."
    PRG "Oh, ah.. thank you!"
    "The two of us walked through the doors and headed outside to the courtyard."

    scene Campus Center with fade
    show PRG neutral with dissolve
    "The wind made the courtyard a bit chillier than it usually was, but it wasn't uncomfortable. Aida rubbed her hands together, then returned them to her lap."
    PRG "It's a little windy, but the weather is really nice. I hope it stays that way."
    "Aida looked whimsically content as she looked across the courtyard. She locked her vision in place once she looked past the tree, however. A quiet, audible gasp escaped her mouth."
    show PRG surprised
    PRG "O-Oh..."
    "It didn't take long to figure out what Aida was staring at."
    play music GTS
    show PRG surprised at Position(xpos=0.2, xanchor=0.5, yalign=1.0) with dissolve
    show GTS_S neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    "Naomi stood in the courtyard, her height rivaling the cherry tree in the center. As she idly swayed and coaxed her body, light vibrations could be felt in the air."
    "Her movements disturbed the cherry blossoms upon the nearby branches, causing them to bounce and sway in response to the wind."
    "While Naomi wouldn't be one to intentionally get too close to buildings, there was still enough room inside the courtyard for her to stand."
    if getSize() >= 4:
        "Naomi's head was nearly in line with the roof of the main building. Any further growth would cause her to exceed three stories tall."
    show PRG worried
    PRG "She's so tall..."
    "Naomi's sheer size made her visible from all the way across the courtyard, but Kodama-san and I were still out of earshot."
    MC "We all knew that our factors would change us, but... talking to Yamazaki-san is a completely different experience now."
    show PRG neutral
    PRG "I-I feel so sorry for her. Gigantism completely changes everything about your life... from how you walk, to where you can travel."
    menu:
        "Naomi feels sorry for you, too.":
            jump BEGTS004_c1_1
        "It's a difficult factor to handle, but she's made the best of it.":
            jump BEGTS004_c1_2
        "[Remain Silent]":
            jump BEGTS004_c1_after

label BEGTS004_c1_1:
    $setFlag("BEGTS004_c1_1")
    MC "Naomi feels sorry for you, too."
    show PRG worried
    PRG "I... really? In what way?"
    MC "Back when you were working for Nikumaru-san, Yamazaki-san felt that she was taking advantage of you. She... really disliked that."
    show PRG sad
    PRG "She shouldn't feel that way. I liked working for Alice. Why would she-?"
    jump BEGTS004_c1_after

label BEGTS004_c1_2:
    MC "It's a difficult factor to handle, but she's made the best of it."
    show PRG happy
    PRG "I'm glad that she's found ways to stay positive! It can't be easy coping with such extreme changes."
    show PRG neutral
    $setAffection("PRG", 2)
    PRG "And, I'm sure that you and Inoue-san have been a big part of that."
    jump BEGTS004_c1_after

label BEGTS004_c1_after:
    BE "Oh, hey! Kodama-san!"
    "Honoka rose from her seat, turning around to greet the two of us."
    "From where Aida and I were standing, the other students in the courtyard were completely blocked by Naomi's legs."
    show BE happy with dissolve
    "When she shifted her stance in response to Honoka shouting, the shadows that spread across the courtyard moved in response."
    PRG "H-Hi, Inoue-san. It's been a while since we've hung out, hasn't it?"
    BE "Sure has! C'mon, have a seat."
    PRG "...Oh? You're certain? I wouldn't want to interrupt anything..."
    extend " or anything..."
    BE "Pff, you're not interrupting. Right, Yamazaki-chan?"
    GTS_S "Not at all. I actually had something I'd like to discuss with you, Kodama-san."
    PRG "With me? O-Okay..."
    "I watched as Aida and Honoka shared a seat on one of the courtyard benches. Naomi stood beside them for a moment, before carefully lowering herself to a seated position next to them."
    "Naomi might have been able to have a bench to herself. The sturdy construction of Seichou was built for students of her scale. She didn't strike me as someone that would risk the bench breaking, however."
    "I took a seat on a second bench next to one that Aida and Honoka were using. With Naomi seated on the ground, the four of us could easily see each other."
    GTS_S "Something came up earlier that could use your input."
    "Naomi leaned slightly closer to Aida."
    BE "This again? I didn't think it was that big of a deal."
    GTS_S "It isn't healthy to delay something that needs to be said."

    if getFlag("BEGTS004_c1_1"):
        PRG "Is this about me working for Alice?"
        "Naomi leaned backward slowly, her encompassing body becoming less overwhelming."
        GTS_S "Ah. Did Hotsure-san tell you?"
        MC "I did. We were talking about you, and it came up."
        $setAffection("GTS", 2)
        GTS_S "I see. I suppose that makes sense. I've been vocal about it recently."
    else:
        PRG "W-What is it?"
        "Aida tilted her head slightly in curiosity."
    GTS_S "Inoue-chan wanted me to explain why I felt the way I do about Nikumaru-san."
    BE "I never said that."
    GTS_S "You didn't respond well when I made snide comments about her."
    BE "Because I thought you were being unfair. We're all friends here."
    "Honoka's usual bubbly expression was replaced with a foggy look of disapproval. Naomi exhaled deeply in response, causing a small gust of wind."
    PRG "Is... that why you brought me here? To give my opinion?"
    GTS_S "That wasn't the initial intention, but I thought this was as good a time as any."
    play music PRGChallenge
    BE "I wanted to have a good time, Yamazaki-chan. You didn't have to bring it up."
    GTS_S "We are having a good time. I just wanted to make sure that we're all being treated fairly."
    PRG "If this is about me and Alice, you don't have to worry. She always treated me right."
    "Naomi leaned closer to Aida again with her hands in her lap, as if trying to assert herself in the conversation."
    GTS_S "Is she a completely different person behind closed doors, then? I've never once seen her kindness outweigh her ego."
    PRG "She... she's my friend. I did some work for her on the side, and I got paid. T-That's all...."
    BE "Back off, Yamazaki-chan. You're doing that thing where you lean forward to look bigger again."
    "In response, Naomi returned to sitting upright."
    GTS_S "I apologize."
    PRG "I-It's okay.."
    MC "Is that all you wanted to know, Yamazaki-san?"
    GTS_S "I wanted to make it clear that Nikumaru-san has been treating us poorly. That's all. Since Kodama-san has spoken to her the most, I wanted to know what she thought."
    "Aida shifted her position several times, grasping the side of the bench for support. She twitched in place as she spoke, in a clear look of discomfort."
    PRG "I-I... didn't... really see it as a problem, I guess. She's really been treating you poorly?"
    "Naomi returned a blunt, objective stare."
    GTS_S "I can't stand her."
    PRG "I'm... sorry that you feel that way."
    "Naomi's expression softened up when Aida spoke."
    GTS_S "Why are you apologizing? Alice is the one that needs an attitude adjustment, not you."
    PRG "I-I just don't want you to think I'm an enabler, or anything..."
    "Honoka exhaled deeply, crossing her arms with a faded, low-energy sigh."
    BE "Well, Yamazaki-chan. There's your answer. Are you satisfied?"
    show GTS sad
    "Naomi paused for a few seconds, slouching slightly while she collected her thoughts."
    GTS "I suppose I was looking for confirmation. I wanted to know that others saw the same thing I was seeing."
    BE "I don't like her attitude either, but that's no reason to put Kodama-san on the spot like that!"
    GTS "What's the alternative? To pretend that nothing is wrong and keep our emotions bottled up?"
    BE "You should see the positive in the situation! No one's hurt, and we're all still here. We'll handle problems as they come, just like we always do."
    GTS "We don't need to be bound by ideals. We can just... avoid confrontation. Let Nikumaru-san and Kodama-san support each other, and leave it at that."
    GTS "I appreciate that you're trying to be a mediator, Inoue-chan, but you don't have to be."
    BE "Well, excuse me for always trying to see the good in people."
    GTS "You'd need to look extremely thoroughly to find any good in Alice."
    BE "Why are you being so negative?"
    GTS "I'm not being negative. I'm doing the best I can to suppress my irritation."
    BE "People can improve. You shouldn't talk behind people's backs like that."
    GTS "Alice hasn't improved. There are certain pieces of one's personality that you just... can't remove completely. I fear that her ego is a lost cause."
    BE "You didn't give up on me."
    GTS "I've always liked you, Inoue-chan."
    "Honoka gripped her hands upon her forehead and ran her fingers through her bangs, breathing heavily in frustration."
    BE "If that's true, then why the fuck are we fighting?!"
    stop music
    "The courtyard went silent for a few seconds. With the exception of Naomi's breathing, nothing else could be heard. The conversations around us ceased, and a few of the other students began to stare."
    MC "Are you all right, Honoka?"
    "Honoka's breathing was heavy and forced, but she progressively began to calm herself. Her expression was still extremely tense, however."
    BE "Maybe... maybe we just need some space."
    "Naomi slowly frowned in response, blinking once. She kept her view firmly focused on Honoka."
    GTS "I feel that would be best."
    BE "Fine."
    GTS "Fine."
    "Honoka was the first to stand up. She turned around and quietly walked away. The sound of her shoes tapping against the sidewalk accompanied the cherry tree rustling in the afternoon breeze."
    "I didn't clearly see Honoka's face. With the way she was hunched over, though, I presumed that she was crying."
    hide BE with dissolve
    GTS "...."
    show GTS despaired-thought
    "Naomi slowly closed her eyes and placed her hand upon her neck, inhaling firmly. Her free hand twitched at her side while she made a gentle fist."
    "I didn't know what she was thinking about. She had a deep look of regret upon her face. A suppressed anger that she continued to contain."
    "Without another word, she slowly rose from her seated position, bit by bit, until reaching her full height. With heavy footsteps, the giantess began to walk back to her hangar."
    hide GTS with dissolve
    show PRG nervous at Position(xalign=0.5, yalign=1.0) with dissolve
    MC "Well... that could have gone better."
    PRG "I-I had no idea..."
    "I stood up from my seat and slowly walked towards Aida."
    MC "Kodama-san. Listen to me. You're not at fault. No one could have prepared for this. You did everything you could."
    show PRG sad
    "Aida sniffled while she sat upon the bench."
    PRG "I-I know. Still... I hate that this had to happen. I should have seen the early signs..."
    MC "You couldn't have known."
    "I held out my hand, offering it to Aida. She took my hand and stood up in front of me, the sadness slightly fading from her face."
    PRG "Thank you, Hotsure-san."
    MC "You're welcome."
    "Aida swayed a little bit, twisting her neck as she scanned around the courtyard. She looked like she really wanted to say something."
    show PRG neutral
    PRG "Do you ever wish you could... go back in time? Do things differently, hoping that things will go better?"
    menu:
        "Sometimes, yeah, I do.":
            MC "Sometimes, yeah, I do."
            PRG "That's... how I'm feeling right now."
            MC "It's natural to feel that way sometimes. I'm just... hoping that we'll all be happy where we are right now."
            show PRG sad
            PRG "Y-yeah, one can hope..."
        "It's more important to look forward, rather than back.":
            MC "It's more important to look forward, rather than back."
            MC "Stressing out over the what-ifs and hypotheticals will only cause you pain. I think it's more important to look towards the future, rather than worry about the past."
            $setAffection("PRG", 2)
            PRG "I... suppose I hadn't thought of it that way. That's... nicely put, Hotsure-san. Thank you. Things seem... clearer."
    MC "What would you do, though, if you were in my position?"
    show PRG neutral
    PRG "W-what exactly do you mean?"
    MC "Well, do you think I should say something? Try to calm things down? They both looked pretty upset..."
    "Aida pondered for a few moments, darting her head left and right while steadying her breath. After a few seconds, she returned a confident exhale."
    PRG "If... I were you, Hotsure-san, I'd just leave the situation alone for now. I think they both need some time to cool off. Neither of them are thinking clearly right now..."
    PRG "I-if you were to try to calm them down right away, it'd probably just make them angrier. I-I think you should wait a while."
    MC "You raise a good point, Kodama-san. I shouldn't say anything right away. Then again, I'm going to see them both sooner or later..."
    show PRG nervous
    PRG "A-and I suppose you'll need to speak to one of them first... which might lead to misunderstandings."
    MC "For now, Kodama-san, I think we all need some rest. I'll sleep on it, give it some thought, then... we can go from there, okay?"
    show PRG happy
    PRG "O-okay. Sounds good."
    MC "Thank you for your help, today. I know it was unexpected, but you did well."
    show PRG neutral
    PRG "You're welcome, Hotsure-san. That means a lot to me."
    MC "I'll talk to you soon."
    PRG "Bye, Hotsure-san."
    hide PRG with dissolve
    "Aida slowly departed from the courtyard, using the opposite set of double doors that Honoka had used. The wind rolling against the trees and windows soon overtook the sounds of the other students once more."
    "I made my way out of the courtyard, and returned to my dorm."
    jump daymenu
