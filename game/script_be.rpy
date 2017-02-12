define BE = Character('Honoka', color="#FCCF20")

image BE neutral = DynamicImage("Graphics/BE-[globalsize]-neutral.png")
image BE happy = DynamicImage("Graphics/BE-[globalsize]-happy.png")
image BE sad = DynamicImage("Graphics/BE-[globalsize]-sad.png")
image BE surprised = DynamicImage("Graphics/BE-[globalsize]-surprised.png")
image BE angry = DynamicImage("Graphics/BE-[globalsize]-angry.png")
image BE aroused = DynamicImage("Graphics/BE-[globalsize]-aroused.png")

image cg BE001 = "Graphics/BE-SC-1.png"
image cg BE002 = "Graphics/BE-SC-2.png"

init python:
    eventlibrary['BE001'] = {"name": "BE001", "girls": ["BE"], "conditions": [], "priority": 0}
    
label BE001:
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

    "The school seemed relatively normal, apart from the size and the people within. It didn't take me long to get the gist of where everything was. Hopefully I'd remember it all when tomorrow came around."
    "But, eventually, I found what I was looking for. Without even checking my surroundings to see if I was being watched, I turned the knob and walked up the steps into the warm sunny sky above."

    MC "Fantastic. It was a long shot, but I figured they'd forget to lock the roof entrance while they were busy setting up the welcoming assembly."
    MC "Wow, from up here the school really looks huge. I guess it has to be big if they only put a few students in each classroom."
    MC "Wonder how many teachers there are, then? And if they all have weird things like Mr. Akaname down there. Probably. It'd help the students adjust if they knew what it was like too."
    MC "I just wonder why they didn't tell the reason for coming here until we were already inside? This doesn't seem like a prison or anything, is it?"

    MC "No, the view is too good up here to be a prison. I'd say it's better than what my old school had. Just looks really nice."

    BE "It does. And it's about to look a whole lot better!"

    "My introspection was suddenly interrupted by my elbow getting pressed into something warm and soft."

    show BE neutral
    with dissolve
    
    MC "What the...Honoka? How'd you get up here?"

    BE "Heh, the same way as you, Kei-chan. Steps. I've been behind you for a while now, did you really not notice?"

    "Not until you bumped into me with that chest of yours..."

    MC "I guess not. My head's kind of all over the place after learning why we're here. How about you? You said you didn't know what this academy was for, right?"

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
    BE "Oh, I haven't the foggiest idea what you could be talking about. A girl's hair does tend to get a bit longer after you haven't seen her for years, Kei-chan."

    MC "Um, actually I was talking about-"

    BE "Hehehe, I'm kidding, Kei-chan. Yeah, I'd say bigger boobs is definitely the most likely choice for me."
    BE "I guess you were never there to see them grow, were you? Wow, you really missed out. Then again, you'll probably be seeing a lot more of them if our hunch is correct!"

    "It was pretty clear that Honoka wasn't all that upset about this situation."
    extend " If anything, she looked pleased as punch, considering she lifted up her boobs like she was about to serve them on a silver tray."

    MC "Well if that is the case, hopefully I grow something big that you'll enjoy, too."

    "..."
    extend " What did I just say?"

    BE "Kei-chan! To think you'd be so forward... I know I said I was in your care, but I didn't think you'd take in that way..."

    MC "Wait, wait, that was a big misunderstanding, I didn't mean to imply anything that-"

    BE "Bahahaha, oh, wow, Kei-chan, heh, it's too easy to mess with you sometimes, you know that?"

    MC "Yeah, you've certainly taught me that lesson many times in the past. Ow..."

    "I winced as she gave me a playful punch in the arm. One that went a little too deep to be completely painless."

    jump BE001_after

label BE001_c2:
    BE "That's true. Still, I think I've got a pretty good idea what mine could be. It starts with 'B' and rhymes with 'goods'."

    MC "...boods?"

    BE "What? Shoot, no, I messed that up. I was talking about my boobs. Like everyone at my old school seemed to do on a daily basis. Hard to blame them really, I made these cans faster than a soda factory."

    MC "Oh, heh. Well, that could have just been some lucky puberty at work, you know?"

    BE "Sure. Still, if it was my boobs, I wouldn't mind it."

    MC "You wouldn't? But you just said everyone at your old school mentioned them all the time."

    BE "Eh, I don't care about that. I doubt I'll care here, either, if everyone's got a chance of getting giant knockers, too."
    extend " Besides, big breasts, well, they kind of seem like the most normal thing I could get, right? I've heard of models or actresses with oddly-sized boobs in the past, so it's not that unusual."

    MC "Hm, guess you've got a good point. You're already used to big boobs, anyway."

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

    BE "Oh wow you still remember that! Haha I really did whoop you at all those games, didn't I? Still, huge feet? That's so weird. Imagine how many socks and shoes I'd need to buy!"

    MC "Well, regardless of what we end up getting, we'll all probably have to change our wardrobes eventually. Hopefully they'll help cover expenses."

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

    BE "Pff, I'm talking about my breasts, Kei-chan. Don't think I didn't catch you sneaking a peek when we met up outside the academy."

    MC "Oh, well, listen, if I'd known you were Honoka, I wouldn't have-"

    BE "Mm-hmmmmmm. Don't be embarrassed, Kei-chan, it's fine. You're a young man with healthy ambition. Though, I do think I deserve a little payment for you staring hard enough to melt my shirt."

    MC "What do you me-ouch..."

    "I quickly moved my hand to rub a sore spot on my upper arm where Honoka had given me a gentle punch. Hopefully her growth factor isn't her hands, or those punches are going to get a lot harder..."
    jump BE001_after

label BE001_after:
    BE "Ahh... just like old times, huh Kei-chan?"

    MC "What do you mean?"

    BE "I mean, you, me, and the roof! The original power trio. How many times do you think we snuck up to the roof when we were younger? 100? 200?"

    MC "It was probably a few dozen times if that."

    BE "Eh you're exaggerating. Still, it's a great wave of nostalgia being up here with you Kei-chan."    
    BE "You know, this academy's definitely a weird place, and we're gonna go through some strange stuff by the sound of it. But, I'm really glad you're here, Kei-chan. Makes things a bit easier."
    
    MC "Please, Honoka, when have you ever backed down from a challenge, anyway?"

    BE "Never! And that's why they call Hard-To-Beat Honoka!"

    MC "I can guarantee nobody has ever called you that."

    BE "Well I'm sure they call me something. I'll get a nickname by the end of the year, I guarantee it. One that suits me! Just you wait Kei-chan."

    "Honoka chuckled before she turned her attention back to the view from the roof."
    "Even through the chainlink fence, it's clear she's captivated by the sight of the big buildings before her."
    extend " Her face was bright; she was no doubt thinking of all the new possibilities this academy would bring. I had to admit, I was a bit excited to see what was going to happen as well."
    "But at the moment, my focus was on Honoka. More specifically, the way her chest pushed against the chainlink fence, making it look like she was wearing chainmail armor over her school uniform."
    jump daymenu