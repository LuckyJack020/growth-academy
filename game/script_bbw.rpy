label BBW001:
    $setProgress("BBW", "BBW002")
    scene Cafeteria with fade
    play music Busy
    MC "Well! That was... a first day. I didn't expect the school to be exactly like my old one, but on a list of unexpected surprises I didn't think..."
    MC "OK, I guess I couldn't have expected it for it to be a surprise."
    extend " But still, if the teacher had ripped off his face to reveal an alien underneath I wouldn't have been more surprised."
    MC "At least food is familiar enough. A nice snack after class is normal, right?"
    UNKNOWN "I'm sorry, you must not realize who you're talking to."
    MC "I wonder who that is."
    "Standing near the doors leading to the kitchen itself was the heavyset girl from my class. There was a man in a chef's outfit standing behind her, and she was arguing with an old woman in an apron and hairnet."
    show BBW angry at center with dissolve
    BBW "The name is Alice Nikumaru."
    BBW "I am sure there was some kind of memorandum circulated among the staff announcing my arrival at this school."
    extend " A missive to let you all know that I am here and that special accommodations to satisfy me would be instituted."
    Lunch "If you have an allergy or other dietary need, I would have been told."
    show BBW angry at Position(xpos=0.4) with dissolve
    BBW "You there. Tell... Madame Hairnet here who I am."
    MC "She's a student. She's in my class."
    show BBW haughty at center with dissolve
    BBW "I am THE student, as far as you are concerned. You may see hundreds of others passing down your line as you ladle warmed over spaghetti sauce onto rubber pasta, but I am not just another stomach to fill."
    MCT "You didn't hear the part about me being in your class, did you?"
    BBW "The meals you mass-produce for the student body may be satisfactory given the level of culinary talent you possess, but I have greater needs."
    BBW "François here studied at the finest institutes in France, Italy and Japan, all for the sake of honing his skills to a level suitable for me."
    Lunch "We make enough food for even the fat kids. Don't worry, you'll get your share."
    show BBW angry
    BBW "I am NOT some 'fat kid'. I am not even obese."
    show BBW neutral at Position(xpos=0.6) with dissolve
    BBW "And it is not a matter of quantity, but quality. My palate is a delicate instrument that needs to be handled with care. I have certain expectations that you - as qualified for this job as you may be - cannot meet."
    show BBW neutral at Position(xpos=0.25) with dissolve
    BBW "Now, I've already gone to the trouble of ordering the equipment you probably don't have - wood-fire pizza oven, rotisserie, espresso machine, meat smoker; just a few odds and ends..."
    show BBW neutral at Position(xpos=0.4) with dissolve
    BBW "But he will need, say, 20%% of your workspace emptied out and handed over to him."
    Francois "And deliveries."
    show BBW happy at center
    BBW "Of course. And he needs to have deliveries made every day, so if you could give him the address and directions to this building, that would be wonderful."
    MCT "Oh, is that all? Your own private chef and special deliveries every day? Just how loaded is this girl?"
    Lunch "Students don't get to bring private chefs with them, princess. Non-faculty don't get access to our kitchen or any other facilities on campus. Either you can take what we offer you, or you can make your own meals in the Home Ec classes."
    show BBW angry
    BBW "What? François cannot perform at his best in a classroom kitchen. He needs a full assemblage of utensils and appliances-"
    Lunch "I said you can make your meals."
    extend " Yourself."
    show BBW haughty
    BBW "Do you really expect me to subject my dainty hands and creamy skin to the raw ingredients that come with making a three-star meal?"
    BBW "Do you have any idea how much this manicure costs? What would handling an ox tongue or a raw Cornish game hen do to it?"
    Lunch "If you don't get out of my kitchen in the next five seconds, you'll be dunking that expensive manicure in cold, greasy dishwater as I have you scrubbing every pot and pan we have."
    show BBW angry
    stop music
    BBW "You... You wouldn't."
    Lunch "You wouldn't be the first student punished with kitchen duty."
    BBW "Very well, but this is not the end. A Nikumaru does not give up."
    show BBW neutral at Position(xpos=0.4) with dissolve
    play music BBW
    BBW "Did you see that?"
    MCT "Did you forget that you talked to me not two minutes ago?"
    menu:
        "Yeah. Typical hard-ass school employee, being cruel for the sake of it.":
            jump BBW001_c1_1
        "That was kind of harsh. She could at least have tried to work something out with you.":
            jump BBW001_c1_2
        "I've heard of spoiled little girls, but your own private chef? That's a whole new level.":
            MC "I've heard of spoiled little girls, but your own private chef? That's a whole new level."
            BBW "Is it 'spoiled' to have the best that money can buy? I am Alice Nikumaru."
            jump BBW001_c1_after

label BBW001_c1_1:
    MC "Yeah. Typical hard-ass school employee, being cruel for the sake of it."
    show BBW haughty
    BBW "Maybe this is how they do it at lesser institutions, but in my experience schools exist for the betterment of the students."
    extend " If this is a taste of how this place operates, perhaps transferring is the sensible thing. There must be other schools that can handle my needs."
    MC "I guess if you can have a private chef, you can also have a private tutor."
    jump daymenu

label BBW001_c1_2:
    MC "That was kind of harsh. She could at least have tried to work something out with you."
    BBW "Absolutely. Life is filled with give and take, and she wouldn't even come to the negotiating table. How is it that so many people cannot understand the basics of business deals?"
    MC "Fancy yourself something of a business-woman, eh?"
    show BBW happy
    BBW "I know a lot about how the world works. It's an inherited trait."
    jump BBW001_c1_after

label BBW001_c1_after:
    show BBW neutral
    BBW "Perhaps you've heard of my father, Daitaro Nikumaru?"
    menu:
        "Daitaro... Isn't he some sort of businessman?":
            jump BBW001_c2_1
        "Oh, yeah! He's the guy who plays in that traveling jug band, isn't he?":
            jump BBW001_c2_2

label BBW001_c2_1:
    MC "Daitaro... Isn't he some sort of businessman?"
    show BBW happy
    BBW "Not just 'some sort' of businessman. He is the leader of the heavy manufacturing and seafood industries in Japan. He is ranked on the list of the richest people in the world."
    MC "Consider me impressed. But if he's so rich, couldn't he just buy this school and install François as head chef?"
    show BBW neutral with dissolve
    BBW "Such a simple thought. Just because you {i}can{/i} buy something, my dear boy, does not mean you should. Not all investments are worth the trouble."
    hide BBW
    MC "D-Did she actually take my joke seriously?"
    jump daymenu

label BBW001_c2_2:
    MC "Oh, yeah! He's the guy who plays in that traveling jug band, isn't he?"
    show BBW angry
    BBW "*scoff* Is there not a single ounce of class or breeding in this place?"
    hide BBW
    MC "I'd settle for an ounce of humor."
    jump daymenu

label BBW002:
    $setProgress("BBW", "BBW003")
    scene Cafeteria with fade
    play music Schoolday
    MCT "This place seems kind of quiet for a high school cafeteria. Everyone's so subdued, it's like someone died. Guess I'm not the only one who was thrown for a loop by yesterday's news."
    MCT "We're all probably wondering the same thing: what's going to happen to me? How... big am I going to get? Am I going to end up like one of those people who can't live in normal society?"
    MCT "Ugh, this is too heavy for first thing in the morning. Let's just get something to eat and take the day as it goes."
    MCT "..."
    MCT "Now to find a table. Oh! There's Alice, eating by herself. I don't think she'd mind if I joined her."
    "I found Alice sitting at a table, a few plates and bowls of food in front of her. She looked unimpressed by the spread."
    show BBW neutral at center with dissolve
    MC "Mind if I join you?"
    BBW "Be my guest. Perhaps you could help me with something."
    MC "Uh, sure! What's on your mind?"
    "Alice held up a fork with a piece of fish on it."
    BBW "This fish. There's something familiar about it."
    MC "It's mackerel. Fish is a common part of Japanese breakfasts."
    show BBW haughty
    BBW "I know that. I've lived here for most of my life. And 'common' may be the best word for what I am eating. I would never have known what this uninspired morsel was if you hadn't told me."
    "She ate the forkful of fish, her face displaying bland disgust."
    BBW "So tell me this: why, when there are literally hundreds of ways of turning even as pedestrian a choice as mackerel into an appetizing entree, did the staff in this kitchen decide to approach their job like they were vulcanizing a piece of rubber?"
    BBW "Is it because they are just that incompetent? What sort of 'cook' treats their ingredients so disdainfully?"
    MC "I don't know. Grilled mackerel's pretty good."
    BBW "I wouldn't mind having mackerel if it was properly prepared. Poach it, bake it in a honey chipotle glaze, something. But I guess that's too much to ask. Just slap it on a grill, turn it after a minute, job's done, right?"
    show BBW neutral
    BBW "Perhaps I should find out who is supplying seafood to this school and have Father undercut them. We could get some decent food in here without profits being too razor thin."
    MCT "Please don't talk about your father influencing the school with his wealth. I don't know if you're joking or if you actually will try it."
    jump BBW002_prechoice

label BBW002_prechoice:
    menu:
        "What do you normally have, if not mackerel?" if not getFlag("BBW002_c1_1"):
            jump BBW002_c1_1
        "What do you normally have, if not mackerel? (disabled)" if getFlag("BBW002_c1_1"):
            pass
        "Well, they have to make food for a few hundred people, you know? There's only so much you can do when you're preparing so much at once.":
            jump BBW002_c1_2
        "(Change the subject) So, how about that news about why we're here? How are you taking that?":
            jump BBW002_c2_1

label BBW002_c1_1:
    $setFlag("BBW002_c1_1")
    MC "What do you normally have, if not mackerel?"
    BBW "Tuna, usually. Though for breakfast I prefer something more like a French menu with coffee, berries in cream, and a croissant. Maybe a poached egg. I'm very particular about my breakfast; a heavy meal to start the day can leave me feeling lethargic for hours."
    "She picked up her mug and drank from it, showing the same mild disgust."
    show BBW angry
    BBW "And this is not coffee. I'll have to call Mother later, have her send my French press here."
    BBW "I suppose it was foolish of me to think this place would have proper coffee, but I was told this was an exclusive institution. So far the only thing 'exclusive' is the most uninspired menu I have ever encountered. Is this what you eat every day?"
    jump BBW002_prechoice

label BBW002_c1_2:
    MC "Well, they have to make food for a few hundred people, you know? There's only so much you can do when you're preparing so much at once."
    show BBW neutral
    BBW "All the more reason to let me have François on hand. It's unnecessary to force every student here to subsist on this food, and to have someone like me - someone accustomed to a certain standard - suffer this becomes downright cruel."
    MC "It's not that bad. I've had better, but I've definitely had worse."
    MCT "Besides, you managed to clear your plates."
    show BBW haughty
    BBW "You must not have had much better than this, but trust me when I say that offering this to my refined palate is like substituting Mascagni with... I don't know, some vulgar pop diva."
    MCT "I don't know who Mascagni is."
    menu:
        "(Change the subject) So, how about that news about why we're here? How are you taking that?":
            jump BBW002_c2_1
        "Other than the food, what do you think of this place?":
            jump BBW002_c2_2

label BBW002_c2_1:
    MC "So, how about that news about why we're here? How are you taking that?"
    show BBW neutral
    BBW "I have never encountered a problem I could not deal with. Whatever sort of... mutation I am about to experience, I will handle it with grace and composure. You will not see me sobbing or wailing my misfortune."
    MC "Hmm-mmm. You have any idea what it might be? Or if they even know?"
    BBW "I haven't the slightest."
    show BBW neutral at Position(xpos=0.5, ypos=0.0, yanchor=0.3), Transform(zoom=2.0)
    MC "Yeah, it's a puzzle. Anyway..."
    show BBW neutral at center, Transform(zoom=1.0)
    jump BBW002_c2_2

label BBW002_c2_2:
    MC "Other than the food, what do you think of this place?"
    show BBW neutral
    BBW "I haven't formed an opinion yet, but my expectations are dropping rapidly. First the unwelcome surprise of this school's true purpose, then the matter of the food. And, of course, being denied the privilege of my servants."
    show BBW angry
    BBW "The term has begun with me being hobbled, almost as if they want me to flounder."
    menu:
        "Do you really need someone to carry your books? Is that beneath you?":
            jump BBW002_c3_1
        "I'm sure you can get by without a butler or whatever.":
            jump BBW002_c3_2

label BBW002_c3_1:
    MC "Do you really need someone to carry your books? Is that beneath you?"
    show BBW haughty
    $setAffection("BBW", -1)
    BBW "Your jealousy is so transparent. Go ahead and mock my situation, as children always make light of what they don't understand. If you had even the basic conception of culture and breeding you would understand how this all degrades me."
    hide BBW
    MCT "I was just teasing..."
    jump daymenu

label BBW002_c3_2:
    $setFlag("BBW002_c3_2")
    MC "I'm sure you can get by without a butler or whatever. I get that you're used to having... help. I'm going to guess that you've gone to private academies, right? Elite places that take care of fewer students."
    show BBW haughty
    BBW "I have attended only the best schools in America and Japan. Yes, this place is... different from them. There are a lot more people, for one."
    MC "But you're not the only one adjusting. I mean, we've all been thrown into it without warning, and none of us know what the future holds."
    MC "Maybe you should reach out to some of the other students. Someone in our class might help you deal with this upheaval. Listen to your problems, help you navigate the school culture. You don't have to deal with this on your own."
    show BBW neutral
    BBW "You do have a point. The uncertainty we are all experiencing is a common ground I can exploit."
    MCT "Exploit?"
    BBW "Thank you, Hotsure-san. You've given me something to think about."
    hide BBW
    MC "Well that ended abruptly. Maybe if I'd been more direct..."
    MC "Wait, did she actually remember my name?"
    jump daymenu

label BBW003:
    $setTimeFlag("testday")
    $setProgress("BBW", "BBW006")
    scene Hallway with fade
    MC "I think the library is this way? Maybe? Wait, that bulletin board doesn't look familiar..."
    MC "Ah! I was supposed to turn left back there."
    UNKNOWN "Amazing!"
    MC "Oh? I know that voice."
    scene Cooking Classroom with fade
    play music Busy
    show BBW happy at Position (xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Simply superb. Where did you study?"
    show PRG neutral at Position (xpos=0.75, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    PRG "I didn't. I just sort of... taught myself."
    BBW "So modest. These are fantastic."
    show PRG happy
    PRG "Oh! K-Keisuke!"
    show BBW neutral
    BBW "Hmm? Hotsure-san, what brings you here?"
    MC "I was walking by and overheard you two. What's supposed to be so awesome?"
    show BBW happy
    show PRG neutral
    BBW "This soufflé Kodama-san has prepared. I've seen enough of Japan's attempts to mimic French cuisine to know to lower my expectations, but this is surprising."
    menu:
        "Oh, is it really that good?":
            jump BBW003_c1_1
        "Can I try some?":
            jump BBW003_c1_2
        "Aida, I didn't know you were a cook.":
            MC "Aida, I didn't know you were a cook."
            jump BBW003_c1_3

label BBW003_c1_1:
    MC "Oh, is it really that good?"
    show BBW neutral
    BBW "It's all relative. I wouldn't tell her to open up a bakery, but for a high school student working with the ingredients and facilities on hand, this is almost revelatory. I can see my judgment was sound as ever to invite her into service."
    MC "Invite who?"
    BBW "Kodama-san, of course. It almost seems destined that my roommate would turn out to be perfectly suited to act as my right-hand woman during my time at this school."
    MC "I think I missed something."
    if getFlag("BBW002_c3_2"):
        BBW "What do you mean? It was your own idea that I should seek help among our classmates. And Kodama-san is all too eager to fill the role of my servants while I'm left to fend for myself here."
        MC "I wasn't really suggesting you find a maid..."
    else:
        BBW "I've decided not to let the loss of my servants hold me back. Just because I cannot have trained professionals on hand to help me does not mean I need to flail around on my own."
        BBW "And Kodama-san is all too eager to fill the role of my servants while I'm left to fend for myself here."
        MC "Seems like you're asking a bit much of your roommate."
    show BBW happy at center with dissolve
    BBW "Nonsense, Kodama-san is more than qualified to act as my chef, secretary, personal trainer, accountant, media relations manager, bodyguard, chauffeur and interpreter. And she's eager to start right away. Aren't you, Kodama-san?"
    PRG "Y-yes, ma'am."
    menu:
        "Is she? I guess that's fortunate for you.":
            jump BBW003_c2_1
        "So are you paying her, or...?":
            jump BBW003_c2_2
        "Aida, do you really just want to be her maid?":
            jump BBW003_c2_3

label BBW003_c2_1:
    MC "Is she? I guess that's fortunate for you."
    show BBW haughty
    BBW "It is. I would have survived just fine had I been left to my own devices, but people like me - those of us who are always looking at the big picture and have so many things to worry about - we benefit from having dedicated subordinates."
    BBW "Having someone to cook for me frees up time and energy I can devote to other things."
    MC "Like what?"
    BBW "Anything. My studies, my hobbies, being the glamorous trendsetter that I am."
    MC "I guess if she's OK helping you, there's nothing wrong with that."
    BBW "Why wouldn't she be okay? I'm giving her focus and direction, at a time when she needs it most. All of us have been blindsided by the news of this school, and I think the best way to deal with it is to carry on as always. It's what I'm doing."
    MC "I can't say you're letting all this get to you. Maybe you have something there."
    show BBW neutral
    BBW "Of course, I could use more help. It's a full-time job being me, and I'm always looking for people I can count on to help me. Would you be interested in such a position?"
    MC "I'll... get back to you on that. I need to be somewhere else right now."
    BBW "Very well, but don't complain if I find someone else in the meanwhile."
    MCT "I think I'll get by."
    MCT "There's a big difference between making friends and becoming someone's butler."
    jump daymenu

label BBW003_c2_2:
    MC "So are you paying her, or...?"
    show BBW haughty
    BBW "It's not polite to talk about money so plainly. But to answer your question, I have offered Kodama-san compensation for her services. And let us leave it at that."
    MC "Didn't mean to offend."
    show BBW neutral
    BBW "I'm sure you didn't, but do be careful in the future. Now, Kodama-san and I have more to discuss, so is there something you need or...?"
    MC "Don't mind me. I have somewhere else to be right now."
    jump daymenu

label BBW003_c2_3:
    show BBW neutral
    MC "Aida, do you really just want to be her maid?"
    PRG "O-Oh no, it's not like that. Alice- M-Madame Nikumaru is very nice, and I enjoy helping others. I'm just happy to have found a f-friend!"
    MC "Okay... I guess that's one way of looking at it."
    BBW "Kodama-san is happy with her position, as you can see."
    MC "Yeah. Sure. Happy. Well, I need to get going..."
    jump daymenu

label BBW003_c1_2:
    MC "Can I try some?"
    BBW "I suppose. There is more than enough here. Try some, and tell me my assessment was wrong."
    menu:
        "Hey, you're right. This is pretty good.":
            jump BBW003_c3_1
        "Aida, this is pretty good.":
            MC "Aida, these are pretty good."
            jump BBW003_c1_3

label BBW003_c3_1:
    MC "Hey, you're right. These are pretty good."
    show BBW haughty
    $setAffection("BBW", 1)
    BBW "Did you think I was being hyperbolic? I don't hand out praise unless it's earned, and even then I'm careful with my words."
    BBW "I have found in Kodama-san a rare talent, waiting to be nurtured and cultivated. And who better to guide her than someone with a palette as refined as mine? No one else at this school can help her like I can."
    MC "That's pretty generous of you."
    BBW "I know, but it's the least I can do. It's one of the burdens of the wealthy seldom talked about: the need to foster talent wherever it is found. With my help Kodama-san will become an excellent chef, someone capable of pleasing even my tastes."
    MCT "And now I'm wondering just how altruistic you are. Still, Aida seems happy with herself, so who am I to butt in?"
    jump daymenu

label BBW003_c1_3:
    $setAffection("PRG", 1)
    PRG "Ohnoit'snothingspecial. I-I-I just like to make treats and share them with people."
    MCT "Cripes. Is she not used to getting compliments?"
    BBW "Kodama-san had mentioned that she was thinking of making treats for our classmates, though I think directing her energy to one person, such as myself, is better than any scattershot approach."
    MCT "Better for who?"
    BBW "I'm afraid we can't stop and chat. Kodama-san has more training to do if I'm to bring her on as my assistant."
    MC "Your assistant?"
    BBW "Naturally I'll need to find someone to help me now that my personal retinue has been barred from the school. And Kodama-san practically begged me for the position."
    MCT "Why do I believe things played out a little differently outside your head?"
    MCT "I'm not up for an argument, though. I should get going."
    MC "Well, I don't want to interrupt you two..."
    hide BBW with dissolve
    hide PRG with dissolve
    "As I left I heard Alice giving Aida notes about the texture of the soufflé."
    jump daymenu

label BBW004:
    scene Classroom with fade
    play music Schoolday
    show BBW neutral at center with dissolve
    MCT "After class clean-up. That's normal. Mind-numbingly boring, but right now I'll take dull over surprising."
    MCT "..."
    MCT "?"
    MC "Um, are you planning to help out?"
    BBW "I have Aida taking care of my share of the work."
    MC "Aida? Where is she- Why are you down there?"
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, ypos=1.0, yanchor=0.3) behind BBW with dissolve
    PRG "Oh! H-hello Hotsure-san. I'm just doing what Nikumaru-san said."
    MC "Did she say to scrub the floor? I'm pretty sure we just need to sweep it."
    show PRG neutral:
        linear 0.75 yalign 1.0
    PRG "I- I know. I just wanted to do a good job."
    MC "But it's not your job. Alice's name was on the roster."
    show BBW haughty
    BBW "And I got Aida to do it for me. It's called delegating. As long as the work gets done, nothing else matters."
    menu:
        "I... guess I can't argue with that.":
            jump BBW004_c1
        "It's not just about getting the work done.":
            jump BBW004_c2
        "Do I have to tell on you? Because that seems like a really childish thing for all of us.":
            jump BBW004_c3

label BBW004_c1:
    MC "I... guess I can't argue with that."
    show BBW neutral
    BBW "Of course not. Aida isn't complaining, so there should be no issue here."
    MC "I'm not saying I agree. I just can't think of a counterargument."
    jump daymenu

label BBW004_c2:
    MC "It's not just about getting the work done. It's about being part of a team."
    show BBW neutral
    BBW "I am part of the team. I'm supplying leadership and direction to Aida. If she's not complaining, is it really any of your business?"
    MC "...You might not want to make a habit of this. That's all I'm saying."
    jump daymenu

label BBW004_c3:
    MC "Do I have to tell on you? Because that seems like a really childish thing for all of us."
    show BBW angry
    $setAffection("BBW", -1)
    BBW "You're threatening to report me? At what point did any of this become your concern, anyway?"
    MC "When I saw someone not doing their share. This is a collective assignment, we all have to carry our weight. You don't get to sit back and take it easy just because you managed to rope someone else in."
    BBW "Are you a figure of authority in this class? No? Then you do not get to tell me that I do not get to do something."
    show BBW haughty
    BBW "As for alerting someone with actual power, go ahead. Play the sniffling toddler, tattle on me. My conscience is clear."
    MC "Guess that's what I'll be doing..."
    jump daymenu

label BBW005:
    $setTimeFlag("aftertest")
    scene Cafeteria with fade
    play music Hallway
    MC "Hair? What kind of mutation is hair growth? This almost seems like a joke."
    MC "Hmm, no open tables. Oh! There's a spot."
    show BBW sad at center with dissolve
    show PRG sad at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    BBW "..."
    PRG "I-Is something wrong, Nikumaru-sama? Did I use too much coriander, or..."
    show BBW neutral
    BBW "No. The dish is exemplary. It's just..."
    MC "Stewing over the test results? Is it something bad?"
    hide PRG with dissolve
    BBW "A Nikumaru does not 'stew.' We take action, we confront problems. Destiny does not come to us, we make things happen."
    MC "So what was it? Or is it too personal to tell?"
    show BBW angry
    BBW "(You might have thought of that before you asked.) To answer your question, yes, I am thinking about the test results. I am questioning what can be done to curtail my... expansion."
    MC "If anything can be done."
    show BBW haughty
    BBW "There is always a way, even if it might be extreme. But the lengths you are willing to go to achieve something demonstrate how much you deserve it. Right, Kodama-san?"
    show PRG neutral at Position (xpos=0.8, xanchor=0.5, yalign=1.0)
    PRG "Ah! Y-yes, Nikumaru-sama!"
    MC "So what is your 'factor?'"
    hide PRG with dissolve
    show BBW neutral
    BBW "They say, and you might have trouble believing this just as I did, that I am inclined to grow... stout."
    MC "Stout?"
    BBW "..."
    extend " Obese."
    extend " Fat."
    MC "Oh. Yeah, that's, um, hard to swallow. But maybe it won't be too bad. They can't tell how 'stout' you'll end up being, right?"
    show BBW angry
    BBW "No, they cannot predict that. But any excessive weight is unbecoming, which brings me to my quandary. Do I restrict my diet even further than the modest regiment I already have, or do I allow the growth to happen and fix things later?"
    MC "You think you can lose the weight after you're done growing? Isn't this supposed to be permanent?"
    show BBW neutral
    BBW "Failure only comes when you give up. Liposuction and similar weight loss treatments have helped others, so why not me?"
    BBW "But I am interested in your thoughts. Which sounds like a better approach, tackling the growth now or dealing with it at a later date?"
    menu:
        "I don't know anything about liposuction, so I'd say try to work at it now. Eat less, eat healthier.":
            jump BBW005_c1
        "Modern medicine is pretty extraordinary. If you ended up getting really fat there's probably some surgery you can get.":
            jump BBW005_c2
        "What if you worked out? Burn those calories before they turn into fat.":
            jump BBW005_c3


label BBW005_c1:
    $setFlag("BBW005_ondiet")
    $setAffection("BBW", -1)
    MC "I don't know anything about liposuction, so I'd say try to work at it now. Eat less, eat healthier."
    BBW "That does seem the best tactic. If I don't give my body the means to get fat..."
    MC "Just don't starve yourself or anything."
    BBW "Of course not. I know exactly what my body needs. Kodama-san!"
    show PRG neutral at Position (xpos=0.8, xanchor=0.5, yalign=1.0)
    PRG "Yes, Nikumaru-sama!"
    BBW "Going forward I want my meals to have a maximum of 650 calories. Adjust my menu accordingly, but be sure to include an appetizer, entree, side dish and dessert."
    hide PRG with dissolve
    MC "So now she's your dietician?"
    BBW "All part of her job description. Did you get all that?"
    show PRG neutral at Position (xpos=0.8)
    PRG "Yes, Nikumaru-sama."
    MCT "Seems a bit much to ask of anyone, even if they're as eager to please as Aida is. But what do I know about cooking?"
    jump daymenu

label BBW005_c2:
    MC "Modern medicine is pretty extraordinary. If you ended up getting really fat there's probably some surgery you can get."
    BBW "I agree, this is the idea most likely to succeed. I don't know enough right now, so how am I supposed to proceed?"
    BBW "What if my growth is miniscule? Would I end up starving myself for nothing? Or what if it is extreme, and denying myself a proper diet is for naught?"
    show PRG neutral at Position (xpos=0.8)
    PRG "N-Nikumaru-sama? The quail is ready."
    show BBW happy
    BBW "Then bring it out! And excellent choice to include the spicy mustard greens in this salad. It was exactly what it needed."
    show PRG happy
    PRG "T-thank you!"
    MCT "Whether this will work or not, it is the path of least resistance. Maybe that's why she's eager to go along with it."
    jump daymenu

label BBW005_c3:
    $setFlag("BBW005_workout")
    $setAffection("BBW", 1)
    MC "What if you worked out? Burn those calories before they turn into fat."
    BBW "Now that is sensible. I admit, the thought of denying myself proper meals is distressing, more so after discovering Kodama-san's talents."
    show BBW haughty
    BBW "I mean, who else at this school is prepared to give her ability the recognition it deserves? And if I can support her while taking care of myself at the same time, so much the better."
    MC "Have your cake and eat it too, you mean?"
    show BBW neutral
    BBW "Quite. You do have a good mind, Hotsure-san, but perhaps humor is outside your reach."
    MCT "I wasn't trying to make a joke."
    jump daymenu

label BBW005A:
    scene Cafeteria with fade
    play music Peaceful
    MCT "Why do I always have trouble finding an open seat? I wonder how much harder this will be once some of the people start growing..."
    MC "Mind if I sit here?"
    show BBW sad at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Oh! G-Good morning, Hotsure-san."
    BBW "...By all means."
    MC "Thanks. Say, did you two get the Lit reading done? I kind of spaced out last night."
    show PRG happy
    PRG "I did it. How far along did you get?"
    MC "About... two pages in."
    BBW "Kodama-san."
    PRG "Yes, Nikumaru-san?"
    BBW "Can you get the other half of the grapefruit? The first half was not adequate alone."
    PRG "Certainly, ma'am. And would you like some more toast?"
    BBW "...Two slices."
    PRG "With jam or butter?"
    BBW "No. Plain."
    PRG "All right. I'll be right back."
    hide PRG with dissolve
    show BBW sad at center with dissolve
    MCT "Someone's in a bad mood. I wonder if I should say something or not."
    stop music
    MC "Light breakfast today?"
    MCT "Mouth, you're not helping."
    BBW "Light breakfast today, and every day. Light lunch every day. Light dinner every day."
    MC "Oh? ...Oh! Yeah. Your factor. I guess you're doing the diet thing, huh?"
    play music Tension
    BBW "If I am to maintain authority over my own body and not be controlled by the whims of fate, then yes, I am doing 'the diet thing.'"
    BBW "Every day, at every meal, I will be watching my intake, limiting the calories, sugars, and fats I take in. I will limit it all to what I need and no more."
    MC "You don't seem too happy about it."
    show BBW angry
    BBW "Is there something here I should be happy about? I have a palate more refined than people twice my age. My appreciation of the arts - culinary or otherwise - exceeds that of professional critics."
    BBW "And now I must cut out my tongue, surviving on simple fruits and steamed vegetables and whatever other staples a Neanderthal wandering the plains of famine would call a meal."
    MCT "That's a bit melodramatic. Better think of some positive way to look at this."
    MC "At least it will help in the long run! That'll be good, right?"
    show BBW neutral
    BBW "I am already beginning to question that. I can endure an existence marked by suffering and lacking. I am strong enough to bear up in the face of abject want, unlike many others."
    show BBW angry
    BBW "But is that a life worth living? Is the path of self-denial, of self-inflicted misery, beneficial to anyone? How can one grow as a person if they have committed their life to depriving themselves of opportunity and experience?"
    BBW "Every bowl of plain rice, every plate of salad, is another act of self-flagellation. Shall my days be marked by anguish, my life's story a tale of torment? Who would live such a life by choice? Who would be inspired by that?"
    MC "But... you just started the diet. This is your first meal."
    BBW "Is my suffering any less brutal for being so brief? Shall I remain silent until I have carried my burden for a certain number of days? No! Pain is pain. It is not to be dismissed for failing to meet some arbitrary metric."
    BBW "You were the one to suggest this trial of deprivation, and now you mock me for not embracing my torture?"
    show BBW angry at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Miss Nikumaru? I brought you your food."
    show BBW neutral
    BBW "Thank you, Aida, but now I want you to go prepare me a real breakfast. Crepes Florentine and smoked salmon to start, along with some coffee and fresh-squeezed orange juice."
    show PRG happy
    PRG "Y-Yes, ma'am... I'll just leave the toast and grapefruit."
    hide PRG with dissolve
    show BBW angry at center with dissolve
    BBW "Or does this not meet your approval, Hotsure-san?"
    MC "Whoa! I'm not judging you. I'm just..."
    BBW "You're just... what?"
    MC "I'm just saying a diet might not be easy, but in the end you might be glad you did it."
    BBW "Is my mood a concern of yours? Is it your business to tell me how I deal with my factor? I assume you have your own condition to deal with, no?"
    MC "Yeah. My hair grows really fast."
    BBW "...That is your condition? That is why you're here?"
    MC "Yep. That's it."
    show BBW neutral
    BBW "I would suggest you withhold any attempts to guide others through their own crises until you have experience with actual problems yourself."
    BBW "Some people seem to just float through life without a care in the world, never understanding how hard and unyielding life can be."
    MC "Uh huh... Consider me properly scolded."
    MCT "I was just trying to help."
    jump daymenu

label BBW005B:
    scene Classroom with fade
    play music Busy
    "The last bell of the day rang and everyone got ready to get up and go. I had nothing in particular I wanted to do this afternoon, but like most everyone else I wanted to get out as quickly as I could."
    "I made it halfway to the door before I was stopped by a hand on my shoulder. Turning around, I saw Alice standing there with Aida hovering behind."
    show BBW happy at center with dissolve
    show PRG neutral at Position (xpos=0.4, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    BBW "It's time we begin our journey."
    MC "Journey?"
    BBW "Our journey towards health and well-being for myself. In order to stave off the effects of my growth factor I will be taking up an exercise routine. An intense calorie-burning regimen to keep myself fit and sleek."
    MC "Where do I come in?"
    show BBW neutral
    BBW "It was your idea, after all. And I can't tackle such a daunting task myself. I remember reading that new habits undertaken with others have a better success rate, and let's be frank, some exercise wouldn't do you much harm."
    MC "I'd be insulted, but... Yeah. What about Kodama-san, though? I thought you said she would be your personal fitness trainer."
    BBW "And she is, but she can't be both working out and coaching me. Plus, she wouldn't do as a spotter. Too frail."
    MC "I think she should be insulted, but..."
    show PRG sad at Position(xpos=0.75) with dissolve
    PRG "..."
    MC "Yeah. Well, I have nothing better to do right now, so why not? Let's hit the gym."
    show BBW happy
    BBW "That's the spirit. Go change, and we'll meet you at the weight room."

    scene Gym with fade
    show BBW neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "OK! Where do we start?"
    MC "Um..."
    BBW "I was asking Kodama-san. She's the official expert here."
    PRG "Uh... Maybe if we did some stretches?"
    show BBW happy
    BBW "Excellent. We'll ease into the workout."
    "We went to a set of mats set up in a corner, away from the weights and machines, and Kodama-san led us in some light stretches and calisthenics that took me back to grade school. I can't say it did anything to burn calories, but it did loosen me up."
    "Eventually she stopped (or she ran out of exercises)."
    PRG "Now how about we... do push-ups?"
    show BBW neutral
    BBW "You're the boss. Come on, Keisuke."
    hide BBW with dissolve
    "Alice and I got down on the mat and started doing push-ups. That is, we tried. I knocked out a couple before I was struggling to keep my form, but Alice was having trouble doing just one."
    show BBW angry:
        xpos 0.25 xanchor 0.5
        ypos 1.0 yanchor 0.0
        linear 1.0 ypos 0.8
    pause 1
    BBW "Nnnnnhg... Gggggrrrr... One!"
    show BBW angry:
        linear 1.0 ypos 1.0
    pause 1
    BBW "Aaaaannnn..."
    show BBW angry:
        linear 1.0 ypos 0.8
    pause 1
    BBW "Two!"
    show BBW angry:
        linear 1.0 ypos 1.0
    pause 1
    show PRG happy
    PRG "Come on, Nikumaru-san! Push it! Unleash the beast! Own your power!"
    "Kodama-san tried encouraging Alice with some slogans I'm sure she got off fitness clothing commercials, and ever so slowly she managed to do a full set."
    show BBW angry:
        linear 1.0 ypos 0.8
    pause 1
    BBW "Ggggggggnnnnnnnn... Ten!"
    PRG "You did it, ma'am! Well done!"
    show BBW happy at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Thank you, thank you. If you'll excuse me, I need to take a quick water break. Hydration is important, after all."
    hide BBW with dissolve
    show PRG neutral
    PRG "OK. We'll wait for you."
    "I wasn't going to say anything; after all, it's not like I'm effortlessly knocking out the push-ups one-handed or anything. And Alice was sweating by the end, so she was putting in some effort."
    "She came back five minutes later, no longer sweating and looking like she had straightened up her hair in the bathroom."
    show BBW neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    BBW "What shall we do next?"
    "Kodama-san looked around, a little bit lost among the machines she clearly had no experience with."
    PRG "Maybe we can start here? And then work our way around?"
    "She was looking at a pulldown bar, the kind where you stay standing and pull the bar in front of your chest."
    BBW "Very well. Keisuke, you go first."
    MC "Why me- No, never mind. I'll go."
    hide PRG with dissolve
    "As I was looking at the weights in increments of five kilos, trying to guess what my limit was, another person came over and joined us."
    show FMG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    FMG "Hey sorry to bother but how much longer are you... Oh hey guys. What brings you here?"
    MC "Hi, Akira. We're just working out, trying to help Alice lose weight."
    show BBW angry
    BBW "I don't need to lose weight. I just need to keep myself from getting fat. There is a world of difference there."
    MC "Right. Anyway, we'll try not to take too long."
    FMG "Nah it's cool, I could use the breather anyways."
    show BBW neutral
    "She stayed standing a bit to the side, watching as I decided how to adjust the weight and making me self-conscious."
    "If it was just me and Alice I could get away with something easy, but with Akira looking over my shoulder I was afraid she would say something if I wasn't going all out."
    "In the end I decided to add 50%% more what I was originally going to lift. To my surprise it weighed more than what I expected. Before I could lift it up, Akira came and grabbed the bar."
    FMG "Sorry but I have a quick question, just how much did you put on the bar?"
    MC "About 70 kilos. Why?"
    show FMG sad
    FMG "Because it looked like it was too much for you. You gotta know your limits and take it one step at a time."
    BBW "You look like you know what you're talking about. Maybe you have some tips you can share."
    show FMG neutral
    FMG "Sure. First off, did you take a protein shake before exercising?"
    BBW "Uh, no? Is that necessary?"
    FMG "Not really but it helps. Here, I have an extra."
    MC "I don't think we need it. We're not trying to build up muscle, are we?"
    FMG "Fair enough I guess."
    "Akira puts the shake away before whispering to me."
    show FMG happy
    FMG "{i}(Between you and me, I just wanted to see Alice's reaction to drinking this sludge.){/i}"
    FMG "All right, tips. The first thing you want to do is, like I said, know your limits and pace yourself. Take short breaks when you need it. Keep consistent and follow a routine. And the most importantly, be patient, don't expect results overnight."
    FMG "As long as you keep it up and actively enjoy it, you won't have any problems."
    show BBW happy
    BBW "Sounds good. Let's get to it."
    show BBW neutral
    BBW "..."
    MC "..."
    BBW "You were about to begin."
    MC "Right."
    "I reset the weight to what I thought was a manageable amount. Akira was still standing by, watching, but I put her out of my mind as I did ten reps with what felt like too little weight in her eyes."
    "When I was done I stepped aside for Alice."
    BBW "My turn."
    "She left the weight where it was, but turned out to be too much for her."
    show BBW angry
    BBW "Nnnnggg! Grrrrr!"
    "She reduced the weight and tried again, then reduced it a third time."
    BBW "Gggnnnn!"
    "She probably would have reduced it again if she wasn't already at the bare minimum. I looked over at Akira as Alice struggled to get to ten reps."
    show FMG sad
    FMG "...Um, you ok Alice? Need anything?"
    BBW "Ggnnnooo, thank you. Just doing what you said and taking it slow."
    FMG "...I didn't mean to the point where you're not even pulling the damn bar. For god's sake, you have it at the lowest level!"
    BBW "Did you not just tell us to know our limits? Are you now reversing yourself and telling me to risk injury by going beyond my limitations? What is it you want me to do?"
    show FMG angry
    FMG "No I... Gar!"
    FMG "Ugh, screw it. I'm getting ice cream before I really get mad!"
    hide FMG with dissolve
    "And she stormed off. For a second I thought about going after her, trying to cool things off so at least she wouldn't leave mad, but then I decided it'd be better this way."
    "Plus, turning back to Alice I another opportunity to play mediator."
    show BBW neutral
    BBW "Well that was uncalled for. It was certainly arrogant of her."
    MC "Arrogant?"
    BBW "Not everyone is gifted with physical prowess, and for her to carry on as if anyone should be able to do what she can... That's arrogant."
    MC "I'm not sure that was her problem, but I agree she could have been a bit more patient... How about I talk to her later, once she's cooled off? She probably could help you with this better than I or Aida could."
    show BBW happy
    BBW "That's thoughtful, but you don't need to put yourself out. This was a worthwhile experiment, but I've reached the conclusion that I'm not cut out to be a gym rat."
    BBW "I don't think this stress of trying to constantly outdo myself would be good for my temperament, if Mizutani-san is any indication. Still, thank you for your assistance."
    MC "You're welcome. (I guess.)"
    BBW "Now, Aida, let's go back to the dorms. I feel a hot bath and massage is the best way to unwind after a workout like this."
    show PRG happy at Position(xpos=0.75)
    PRG "Y-Yes, ma'am! I'll get the oils."
    jump daymenu

label BBW006:
    $setProgress("BBW", "BBW007")
    scene Hallway with fade
    play music Peaceful
    MCT "Classes are done, so what now? Don't want to go back to my room, I've got enough weirdness going on without someone trying to find more lurking around every corner. Maybe I can see if any of the clubs are recruiting yet."
    "..."
    MCT "Sounds like the music club is rehearsing. Not my thing... Oh!"
    show BBW neutral at center with dissolve
    MC "Niku- Alice. Thinking of joining the music club?"
    show BBW haughty
    BBW "Offering my services to the ensemble is one reason I'm here, though I'm disheartened to find out freshmen are not considered for seated positions. Waiting a year just to take my rightful place on the stage..."
    show BBW neutral
    BBW "I'm more sorry for the club, having to endure without my contribution."
    MC "How thoughtful. So what instrument do you play?"
    BBW "I have my own natural instrument: my voice."
    MC "You're a singer?"
    BBW "A soprano. And a gifted one, I should say. I've been coached since I was five."
    MC "I didn't know the music club did operas."
    show BBW neutral
    BBW "According to the club adviser, they do not. Put more accurately, they never have."
    show BBW haughty
    BBW "But the higher arts are not more difficult by nature. With sufficient commitment and practice I'm sure they could put on a fair performance. And with me as the star..."
    show BBW neutral
    BBW "But I'd also hoped to find a talent or two I could nurture during my time here."
    MC "Nurture?"
    BBW "The Nikumarus have a long history of patronage of the arts, one I hope to continue. I hope to get a start on it by finding a budding talent to encourage. Pushing them to refine their art and attain what greatness they were born for."
    BBW "Privilege, after all, comes with the responsibility of helping others."
    MCT "You sound both selfless and selfish as you say that."
    BBW "On that note, do you play any instruments, Hotsure-san?"
    MC "Me? Uh..."
    menu:
        "No, I don't.":
            jump BBW006_c1
        "I've practiced a little, but I'm not really talented.":
            jump BBW006_c2
        "I don't mean to brag, but I'm a pretty skilled musician.":
            jump BBW006_c3


label BBW006_c1:
    MC "No, I don't."
    BBW "Hmm. An honest answer, but a shame."
    MC "Does anybody here catch your eye? Or ear, I should say?"
    BBW "It's too soon to say. None of them are masters, so finding the seed of potential requires a deeper look. I'll need to sit in on a few more meetings."
    MC "I take it you'll be the joining the club, even as a benchwarmer?"
    BBW "...I am unfamiliar with that term. But yes. With my gift it would only be appropriate that I join. And I cannot convince the club president of their folly in keeping me in reserve if I am not here."
    MC "You don't take 'No' for an answer, do you?"
    show BBW haughty
    BBW "I'm a Nikumaru. A 'No' to me is just another obstacle to overcome."
    jump daymenu

label BBW006_c2:
    MC "I've practiced a little, but I'm not really talented."
    BBW "Oh? What instrument?"
    MCT "Immediate regret setting in. What's an impressive instrument?"
    MC "Uh... Violin. I've had a few lessons, but I'm no, you know, virtuoso."
    stop music
    BBW "None of the students here are, if the music club is any indicator. But talent can blossom anywhere when given a guiding hand. Show me what you can do."
    MC "Here? Now? Are you sure it's OK to use the club's instruments?"
    BBW "Of course. The instruments belong to the school, and we're students."
    MC "All right."
    if getSkill("Art") > 3:
        "I played a few strings in sequence. Nothing that required real skill, but it was a pleasant sounding tune."
        BBW "Not bad."
        show BBW happy
        $setAffection("BBW", 1)
        BBW "You should keep practicing, you could definitely make the music club if you really wanted to."
        BBW "I'll see you in class, Keisuke."
        hide BBW with dissolve
        "And with that, she took her leave."
        jump daymenu
    "I squeaked out a few sharp chords that sounded like someone stroking a balloon. Alice's thoughts were too easy to read as she grimaced in pain."
    show BBW angry
    BBW "Enough!"
    MC "Sorry. It's been a while since I've practiced."
    show BBW neutral
    $setAffection("BBW", -1)
    BBW "Maybe I shouldn't have expected much. You... You might have some skill. Some day."
    hide BBW with dissolve
    "She wasn't disappointed, but as she turned away I could tell she was let down."
    jump daymenu

label BBW006_c3:
    MC "I don't mean to brag, but I'm a pretty skilled musician."
    MCT "Oh dear god, why did I say that? I can't even play the triangle."
    BBW "Really? Which instruments do you favor?"
    MCT "Instruments? Plural? Oh, jeez..."
    MC "I mostly play... violin. But I also toy with the oboe."
    MCT "Sure, let's keep lying."
    BBW "The violin? It wouldn't take much to outshine the other students here, but how experienced are you? Have you had many public performances?"
    MCT "Fix this, you dolt. Now!"
    MC "I've never performed in front of an audience. I don't have the nerves for it. Just a lot of practice in private."
    BBW "All that practice must have been worth something. Show me what you can do."
    if getSkill ("Art") > 3:
        stop music
        "She handed me a violin and I played a few notes in sequence. It was pleasant sounding but far below the level I had gloated about."
        show BBW angry
        BBW "Keisuke. That was..."
        show BBW neutral
        BBW "Look, having pride in your work is one thing but it has to be pride to an accurate level. Bragging about that which you do not possess will not take you far in life at all."
        $setAffection("BBW", -1)
        BBW "Keep at it. Maybe one day you'll be able to claim you are that good and actually mean it."
        BBW "I'll see you in class."
    stop music
    "And before I could say anything she was thrusting one of the club's violins into my hands."
    "This was too fast for me to deal with, I couldn't think of anything to say to get out of it. So, nervously, I put the violin under my chin like I had seen people do in movies and I tried stroking the bow back and forth."
    "The disgust on Alice's face was immediate, and I couldn't blame her. If the violin was a living being I would have been arrested for animal cruelty. But I still thought I could fake it if I could, I don't know, figure out how to stroke the chords right."
    show BBW angry
    BBW "Stop! Stop!"
    MC "Sorry. It's been a while since I-"
    $setAffection("BBW", -3)
    BBW "Learned how to tune it properly? I don't know what kind of goofing off you think constitutes 'practice,' but you should keep this musical torture private."
    hide BBW with dissolve
    "And she stormed off. Which, considering her mood, may have been preferred."
    jump daymenu

label BBW007:
    $setProgress("BBW", "BBW008")
    scene Cafeteria with fade
    MCT "First time I haven't had trouble finding a spot. I guess other people are spending lunch up on the roof or in their classrooms, like at a normal school."
    MCT "Looking around, it does seem like a lot of people are drifting into cliques or avoiding certain people."
    MCT "And I'm off by myself, which is par for the course."
    "No sooner had I thought that than someone sat down across from me."
    show BBW neutral at center with dissolve
    MC "Oh, Alice. Didn't know you'd be having lunch here."
    BBW "Why wouldn't I? It is a pleasant day outside, but it seems improper to eat in some random place. Or maybe it is simply proper to eat where the food is served. Structure is an oft-overlooked virtue, in life and in business."
    MC "If you say so."
    "It took me a second to realize Alice wasn't alone. Right behind her was Aida, holding a few packages."
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    MC "Hi, Aida. How did you get so much mail already? It's still the first week of the year."
    PRG "Oh, it's not mine. I was carrying it for Nikumaru-sama. We just came from the mail room."
    show PRG sad
    extend " ...There was nothing for me."
    MCT "She seems a bit sad. Is there something about mail that bothers her? Better change the conversation."
    BBW "Interested in what I got?"
    MC "Uh..."
    hide PRG with dissolve
    BBW "A lot of it is the usual care package stuff. Hand lotion, chewable candies, perfume, a new phone -"
    MCT "That left 'usual' territory pretty quickly."
    BBW "But I also ordered myself some things. White knee-high stockings seem to be 'in' among the other students, and I was not aware how cold winters in this part of the country can get, so I needed a new coat."
    BBW "And Aida confided in me that she only has one pair of shoes and barely any clothing besides her school uniforms. So I ordered some stuff for her."
    MC "That was considerate."
    BBW "Well, she doesn't have a credit card or bank account of her own, so ordering things online are beyond her means. But it was the least I could do to facilitate her shopping."
    MC "Facilitate... You mean she still paid for the stuff herself?"
    BBW "But of course. I'm not running a charity. And I would like to point out that with my connections I was able to buy directly from the manufacturer, saving her money."
    MC "What do you mean by connections?"
    show BBW haughty
    BBW "I know the sons and daughters of many business owners and CEOs. We always turn up at the same hotels in Monaco or ski lodges in Switzerland. You don't think the owner of a factory that makes dresses or suits has to buy off the rack, do you?"
    MC "I guess not. So if I needed to buy a new laptop could you get me one at a discount?"
    show BBW neutral
    BBW "I suppose I could. Hitomi and I - that's Hitomi Ogawa, daughter of the president of Ogawa Electronics - aren't on the closest of terms, but she could get me one for... 90,000 yen. Plus 10%% commission for myself would be 99,000."
    MC "An Ogawa laptop for under a hundred thousand yen? That's pretty steep for some old model being unloaded-"
    BBW "That's for an Ogawa D2300. 55cm monitor, if I remember correctly."
    MC "...For 99,000?! Are you serious?"
    BBW "Completely."
    MCT "Unbelievable. That's a 170,000-yen machine, and she says she can get one for under 100K?"
    BBW "Don't be surprised. I'd be buying direct from the company, so there's no middle-man mark-up. Except for my commission, of course."
    MC "O-Of course."
    BBW "Or would you prefer the Essence 4K? I could probably get that for, let me see..."
    "And she checked her smartphone. Was she checking the manufacturing cost online, or did she know what the mark-up from retailers was?"
    BBW "How does 115,000 yen sound?"
    MC "I think I might faint."
    BBW "Shall I order one? You don't have to pay me now, you can take care of that when it gets here."
    MC "No, no. I don't need a new laptop. I mean, I could use one, but I don't have that kind of money."
    BBW "Well you should have said so."
    extend " ...Idea. Aida, take a note: I am going to start a business here at school. Direct retail, goods offered at a discount."
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    MC "There's already a store on campus, you know."
    BBW "I know, I've seen it. But it lacks many of the essentials of modern living, and the mark-up is scandalous. 300 yen for a soda? I can beat those prices and still make a worthwhile profit."
    PRG "What do you need me to do, Nikumaru-sama?"
    BBW "Our first step will be to get the word out. We'll need some sort of ad campaign, make the people aware of my service."
    BBW "Then we'll need a system of taking orders and fulfilling them. Dorm-room delivery would be an enticing service; convenient for the customer."
    BBW "But the guys' dorm... Keisuke! How would you like a job?"
    if getSkill("Academics") < 3:
        MC "Me? Doing what?"
        BBW "Haven't you been listening? I'll need runners, people to deliver packages as they come in. I can offer you 1,000 yen an hour."
    else:
        MC "Let me guess: you need a deliveryman."
        show BBW happy
        BBW "Got it in one. I'm offering 1,000 yen an hour."
        show BBW neutral
    MC "I... will think about it."
    MCT "She's actually serious about this. I wouldn't have guessed she was this sort of vigorous go-getter. I guess business runs in her blood."
    "The conversation died as Alice started giving instructions to Aida."
    "The idea had just come to her, but she was immediately rattling off ideas about what products to offer, how to acquire, pricing and advertising."
    "I'd thought she was more a spoiled rich girl than anything, but it seemed she wasn't content to spend her daddy's money. She had a mind for business herself."
    "Made me feel a little lazy. I was just trying to keep up with my coursework. Never mind building a business from scratch."
    jump daymenu

label BBW008:
    scene Hallway with fade
    "After another day of classes I found myself not in my dorm and not in my classroom. I wasn't heading anywhere special, I was just wandering around."
    "I eventually found myself passing by the music room."
    scene Music Classroom with fade
    MCT "Maybe I can listen in on them practicing."
    "But the club wasn't meeting right now. There were just two people, Aida and another student. It's not like I wanted to spy on them, but I was curious and they were talking loud enough to overhear them."
    play music Bittersweet
    Student "-alented or not, I have no patience for someone trying to undermine my authority."
    show PRG sad at Position(xpos=0.8, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    PRG "Y-yes, ma'am. But I don't think she means to be-"
    Student "You seem to be the closest thing she has to a friend, so maybe she'll listen to you. Tell her she can either be happy in the chorus or she can look for another club to join."
    PRG "Y-yes, ma'am."
    "The other girl (is she the music club president?) turned away, the conversation over. Head bowed, Aida made for the door. I stepped back, but not fast enough to not get caught."
    show PRG surprised at center, Transform(xzoom=1)
    PRG "Oh! H-Hotsure-san."
    MC "Hey, Aida."
    MCT "Should I ask what that was about? Aida looks pretty bummed."
    MC "Is something wrong? It looked like you were being given the third degree."
    show PRG neutral
    PRG "N-no. I wasn't in trouble. It's Nikumaru-san. She doesn't like being in the chorus, but Mizawa-san won't make her lead vocalist."
    MC "Is that the club president? Is Alice butting heads with her or something?"
    PRG "Yes. They keep getting into arguments, and now Mizawa-san is threatening to kick Nikumaru-san out if she doesn't behave."
    MC "I haven't known her too long, but Alice doesn't seem like much of a team player. Guess I'm not surprised she's already getting into trouble like this."
    show PRG sad
    PRG "I-I'm supposed to t-tell her to mind herself, b-but I don't think Nikumaru will listen to me. She's kind of head strong."
    MCT "And you're kind of a pushover."
    MCT "Oh, that's mean. But it's not wrong."
    menu:
        "Well, good luck with that.":
            $setTimeFlag("size2")
            $setProgress("BBW", "BBW012")
            stop music fadeout 0
            "Well, good luck with that."
            show PRG surprised
            $setAffection("PRG", -1)
            PRG "..."
            MCT "I could go for a soda now."
            jump daymenu
        "Maybe I could help.":
            jump BBW008_prechoice

label BBW008_prechoice:
    MC "Maybe I could help."
    MC "I wouldn't say Alice listens to me so much as she hears what I say. I can pass the word along for you."
    show PRG happy
    PRG "C-could you?"
    show PRG sad
    $setAffection("PRG", 1)
    PRG "I-I don't want to trouble you, but it would be so sad if she got kicked out of the club. She's a stranger here, you know. She doesn't fit in."
    MC "We're all strangers, but I get what you mean. She kind of fits that whole 'pushy American' stereotype, doesn't she?"
    show PRG angry
    PRG "Oh, no! Nikumaru-san is just very determined."
    MCT "Determined. Sure."
    MC "Do you know where Alice is now?"
    show PRG neutral
    if isEventCleared("BBW007"):
        PRG "She should be in the cafeteria. I made some snacks for her to sample while she works on setting up her business."
    else:
        PRG "She should be in the cafeteria. I made some snacks for her to sample."
        MC "Might as well deliver the news now, then."
    stop music

    scene Cafeteria with fade
    play music Hallway
    "We found Alice sitting at her usual table, one hand typing on a laptop and the other picking up high tea pastries from a tray next to her."
    show BBW happy at center with dissolve
    BBW "Hotsure-san, good afternoon. Thank you for bringing Aida back. I've been waiting for her for... five and a half minutes now."
    MC "Actually she brought me here. There's something I need... Something you should know."
    show BBW neutral
    BBW "Oh?"
    MC "Yeah, um... How's the music club? You're still doing that, right?"
    BBW "Despite my feelings on how it is being managed, yes, I am still a member."
    MC "Right, right. So I was told- That is, Aida was told..."
    show BBW angry
    BBW "..."
    "I stammered a few words, and Alice became irritated quickly."
    MC "We were told to tell you to, you know... Maybe ease up on the prima donna thing."
    BBW "Excuse me?"
    MC "It's not that you're... You can be a little..."
    MC "You're going to get kicked out if you don't stop fighting with the president."
    BBW "Oh, really? Aida, is this true?"
    show PRG sad at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Y-yes, Nikumaru-san."
    BBW "I should find her at once and tell her..."
    hide PRG with dissolve
    MCT "She didn't understand anything I just said, did she?"
    menu:
        "Say nothing. Let Alice do what she wants.":
            jump BBW008_c1
        "Suggest Alice not make things worse.":
            jump BBW008_c2
        "Tell Alice she's in the wrong.":
            jump BBW008_c3

label BBW008_c1:
    $setProgress("BBW", "BBW008A")
    MCT "Well, if she wants to pick a fight, let her. Whatever happens is on her head."
    show BBW haughty
    BBW "Thank you for bringing this to my attention, Hotsure-san. My esteem for Mizawa-san was already low, but to use an intermediary like this is pathetic."
    MC "No problem."
    "I decided to excuse myself then. Didn't want to get caught up in this drama."
    jump daymenu

label BBW008_c2:
    $setTimeFlag("size2")
    $setProgress("BBW", "BBW012")
    MCT "Oh man, this is going to get out of hand quickly if I don't do something."
    MC "Maybe you shouldn't push back right away."
    show BBW angry
    BBW "What do you mean? Should I let this stand-?"
    MC "Some people just don't get the message right away, do they? Clearly the club president - this Mizawa girl - hasn't recognized your talent yet."
    show BBW haughty
    BBW "No, she hasn't-"
    MC "So getting in her face again won't do any good. This seems like one of those times where the person needs to realize their failure on their own."
    BBW "And what do I do in the meanwhile? Resign myself to the chorus until Mizawa-san decides to admit she was wrong?"
    MC "I don't think there's much you can do at the moment."
    BBW "Are you not familiar with the phrase 'The squeaky wheel gets the grease'? If I'm supposed to wait for that tone-deaf girl to realize my talent, I will be stuck in the chorus all year."
    MC "And have you ever heard the phrase 'The upturned nail gets hammered down'? If you keep fighting her you won't even be on the chorus."
    show BBW angry
    BBW "..."
    BBW "Hmm..."
    show BBW neutral
    $setAffection("BBW", 1)
    BBW "Is it just me, or are Japanese people excessively non-confrontational?"
    BBW "Very well. Aida, forget my last order. I'll toe the line, for now."
    BBW "But not forever, Hotsure-san. I don't intend to let my genius go ignored indefinitely."
    MC "Wait, why are you making it sound like it's my job to get you out of the chorus?"
    jump daymenu

label BBW008_c3:
    $setTimeFlag("size2")
    $setProgress("BBW", "BBW012")
    MC "Can't you just admit that you're in the wrong here?"
    show BBW angry
    BBW "I beg your pardon?"
    MC "You're not the leader of the music club, are you?"
    BBW "I'm the best singer-"
    MC "That's a 'No,' then. Well, the actual leader has made a decision, and it doesn't matter if you like it or not."
    MC "Maybe you are the best singer, but there's more to an ensemble than any one person getting what they want."
    MC "You're going to have a hard time getting along here if you don't understand that. We're all dealing with some pretty major stuff right now, not just you."
    $setAffection("BBW", -1)
    BBW "How dare you..."
    "She didn't have to say anything, I knew what she was thinking. All the better, as I wasn't looking for a fight or anything."
    MC "Just something to think about."
    "And I turned and walked away. Maybe a bit quicker than I intended, but I didn't want to stay and get chewed out or anything."
    jump daymenu

label BBW008A:
    $setTimeFlag("size2")
    $setProgress("BBW", "BBW012")
    scene Cafeteria with fade
    show BBW angry at center with hpunch
    play sound Crash
    BBW "That impudent egotist!"
    play music Tension
    "I was sitting in the cafeteria, not so much enjoying my lunch as eating it without gagging-"
    show BBW angry at Position(xpos=0.8)
    play sound Crash
    BBW "How could such a woman be put in a position of authority? Bribery? Blackmail? Nepotism?"
    "-when Alice came up to my table and started complaining to me about someone."
    "There was no way to know how long she had already been ranting before reaching me..."
    show BBW angry at Position(xpos=0.2)
    play sound Crash
    BBW "A leader who thinks their job is to simply dictate to others does not understand leadership. A captain who does not know her destination might as well run the boat aground."
    MC "Problem with authority? Is this about the music club thing?"
    show BBW angry at center with dissolve
    BBW "What does it say about a club leader who is more concerned with maintaining a cordial environment where mediocrity can rule than challenging everyone to deliver their best?"
    MC "That... this is more about having some fun than anything else?"
    show BBW neutral
    BBW "And how is it 'fun' to rehearse the same pieces of music without striving for improvement?"
    show BBW angry
    BBW "This Mizawa-san is only wasting everyone's time if she refuses to demand anything of her members."
    MC "It's only the start of the year. I'm sure there must be some period of adjustment for a musical group to come together."
    MC "Maybe if you tell her - politely - that you think she can ask a little more of everyone she'll agree. Maybe she already wants more of them, but she doesn't want to be overbearing."
    show BBW haughty
    BBW "I have already addressed my concerns with Mizawa-san. Just now, when she suspended me from the club."
    MC "What?! She kicked you out?"
    show BBW neutral
    BBW "Not permanently, but I am on forced sabbatical until I have 'adjusted to the upheaval in my life,' as she put it."
    show BBW haughty at Position(xpos=0.2) with dissolve
    BBW "She thinks I am, what were her words, 'behaving out of turn' because I am in an unfamiliar environment, with the news of my condition hanging over me."
    show BBW angry at Position(xpos=0.8) with dissolve
    BBW "Projection. That's what it is. Mizawa-san is uncomfortable being here, and so she is pretending I am the one with the problem."
    show BBW neutral
    BBW "Perhaps that is easier to believe than acknowledging I am in the right."
    MC "So... This isn't about the other students in the club? This is just about you still butting heads with her?"
    show BBW haughty at center with dissolve
    BBW "This is only about the club, and how I know what is best for it."
    show BBW angry
    BBW "Mizawa-san may try to pull rank, but shoving me aside does not win her the argument. I am still of half a mind to press the issue."
    menu:
        "I don't see what good that would do. If she's as headstrong as you say, arguing will only make her dig her heels in.":
            jump BBW008A_c1
        "If you feel this strongly, go for it. You're the one talking about squeaky wheels, right?":
            jump BBW008A_c2
        "Arguing with Mizawa-san obviously isn't doing any good. Maybe try a different tack.":
            jump BBW008A_c3

label BBW008A_c1:
    play music Hallway
    MC "I don't see what good that would do. If she's as headstrong as you say, arguing will only make her dig her heels in."
    show BBW angry
    BBW "Mmmf!"
    BBW "..."
    show BBW neutral
    BBW "She probably would, wouldn't she?"
    BBW "I suppose this is a situation that calls for patience rather than the firm hand of guidance."
    BBW "Very well. I shall endure my sabbatical with my natural grace, and when I return to the music club even Mizawa-san will not be able to deny what a difference my presence makes."
    hide BBW with dissolve
    "And she trotted off. I don't think she was any less angry, but at least things hadn't gotten worse."
    jump daymenu

label BBW008A_c2:
    MC "If you feel this strongly, go for it. You're the one talking about squeaky wheels, right?"
    show BBW neutral
    BBW "You are not wrong. There may still be time to find Mizawa-san before lunch ends, and we can settle this matter before the club meeting this afternoon."
    hide BBW with dissolve
    "And she walked off."
    scene black with fade
    stop music
    "Ten minutes later, she came back."
    scene Cafeteria with fade
    show BBW angry
    play sound Crash
    $setAffection("BBW", -2)
    BBW "There is no word for 'foolishness' in your language that is strong enough for that girl."
    play music Hallway
    MC "She didn't listen to you-"
    BBW "She says that I am a hair's breadth from being cut entirely, and she makes it sound as if she is being reasonable by giving me a 'second chance.'"
    BBW "That my talent, which I have clearly demonstrated by this point, could be dismissed so flippantly..."
    BBW "Argh!"
    BBW "I almost want to leave of my own accord. Being hobbled by this enabler of mediocrity may not be worth it."
    MC "I-"
    hide BBW with dissolve
    "But she was already storming away, as if she wanted to get away from the entire school."
    jump daymenu

label BBW008A_c3:
    $setTimeFlag("BBWclubfail")
    stop music
    MC "Arguing with Mizawa-san obviously isn't doing any good. Maybe try a different tack."
    MC "Instead of taking up this fight yourself, why don't you get some others on your side?"
    MC "Talk to the other members of the music club, see if they'll back you up. Then you can all go up to the club prez and try to reason with her."
    show BBW happy
    BBW "That is not a bad idea, Hotsure-san. Strength in numbers."
    show BBW haughty
    BBW "Or if I can convince enough members to see it my way, I could simply try to oust Mizawa-san as president."
    MCT "OK, that is not what I'm suggesting."
    show BBW neutral
    BBW "There's still time before lunch ends. I need to speak with some of the other members."
    hide BBW
    "And she walked off, holding her chin up as if she had already won a victory."
    scene Hallway with fade
    "As I left the cafeteria and started to make my way back to class, I ran into Alice coming in the opposite direction."
    show BBW angry
    play sound Crash
    $setAffection("BBW", -10)
    BBW "Hotsure-san! How could you possibly suggest such a terrible idea?"
    MC "Me? What did-"
    MCT "Oh, this must be about the music club thing."
    play music Bittersweet
    BBW "I've been kicked out of the music club! Mizawa-san claims I was attempting to mutiny-"
    MCT "Well, you did suggest-"
    BBW "And now I have been expelled entirely."
    "By her expression I had no doubt who she blamed for this, and while there were a number of ways I could have responded, I ultimately decided on staying silent and not making things worse."
    "Alice continued glowering at me, perhaps waiting for me to answer, but after a while she huffed and muttered"
    BBW "What is wrong with this place?"
    "And then she walked away."
    "Which was awkward, because we were headed in the same direction, so I had to hang back a couple feet and try to look anywhere besides directly at her."
    scene Classroom with fade
    "And when we got to class and took our seats she adamantly refused to look in my direction."
    show BBW angry
    BBW "Harumph!"
    hide BBW with dissolve
    "At least I knew where I stood at the moment."
    jump daymenu

label BBW009:
    scene Hallway with fade
    play music Busy
    "It was only the second week of the year and I was already getting cabin fever being stuck at the school 24/7."
    "There was a town not far from the gates, but I hadn't gotten a chance to check it out yet. Hadn't even checked out much of the school, for that matter."
    "That's probably why I found myself at the locker rooms after class. Going back to my dorm room didn't appeal to me; just two weeks in and I was getting tired of that place."
    "And I still didn't belong to a club, so I had no specific place to be..."
    "I was thinking of maybe changing into my gym clothes and doing a little cardio when I was surprised to see Nikumaru-san, of all people, coming out of the women's locker room."
    show BBW happy at center with dissolve
    MC "Oh, Ni- Alice! How's it going?"
    show PRG sad at Position(xpos=0.8, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    PRG "..."
    MC "A-and you, Kodama-san! What were you two up to?"
    BBW "I was doing a light workout."
    MC "I thought you weren't going to try to lose weight just yet."
    hide PRG with dissolve
    show BBW neutral
    BBW "I'm not, but exercise has other benefits besides weight loss."
    show BBW haughty
    BBW "A strong mind in a strong body, as they say."
    BBW "So I was making use of the school's swimming pool. 20 laps, back and forth. A fair workout to get my heartrate up."
    MC "20 laps!? That's... That's actually impressive."
    BBW "I understand how it can seem like that to most people, but I have a natural affinity for the water. I've been an accomplished swimmer since I was a young girl."
    if isEventCleared("BBW008"):
        MC "Maybe you should have joined the swim team instead of the music club."
        BBW "I did consider it, actually, but the school would allow me to join only one club at a time. I find the limitation frustrating but bearable."
        show BBW angry
        BBW "And who knows. If the matter between me and the music club president is not resolved satisfactorily I may take my talents to more appreciative grounds."
    MC "How fast can you swim? Have you ever timed yourself?"
    show BBW neutral
    BBW "Quite fast, actually. I should have had Kodama-san timing me, upon reflection. An accurate chart of my ability would help measure my fitness levels."
    show PRG neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    PRG "I'm sorry, Alice. I'll remember next time, I promise!"
    hide PRG with dissolve
    show BBW haughty
    BBW "I don't have a specific number, but I feel confident that I am the best swimmer in our class. Probably in the top percentile of the school."
    MC "Even better than Mizutani-san? She's pretty athletic, you know."
    BBW "There's more to it than just physical strength. Stamina, hydrodynamics, breathing control."
    stop music
    MC "!"
    "Alice didn't see her, but standing behind her was-"
    BBW "Sheer muscle may be good for lugging heavy weights around, but swimming is a much more graceful art than being a simple pack mule."
    show FMG angry behind BBW at Position(xpos=0.7, xanchor=0.5, yalign=1.0) with dissolve
    play music Tension
    "-was Akira. And judging by her expression she didn't like what she was hearing."
    BBW "It's the difference between composing poetry and punching a sack of meat. Elegance versus brute force."
    "I was just about to interrupt Alice - even though she already seemed to be wrapping up - when Akira beat me to it."
    FMG "Hello Alice What's-your-last-name! Interesting theory you have there!"
    show BBW haughty at Position(xpos=0.6) with dissolve
    show FMG angry at Position(xpos=0.25), Transform(xzoom=-1) with dissolve
    "Alice blanched at the sound of Akira's voice, but she recovered swiftly."
    show BBW happy
    BBW "It's not so much a theory as good common sense."
    BBW "One isn't pushing against the water but rather propelling oneself through it. It's a complete different act, an interplay of body and water rather than a conflict between muscle and weight."
    FMG "Oh yeah! Well how about we test your little 'act of pushing water by being something something BS' by seeing who's the fastest swimmer! Or are you too full of yourself to do it!?"
    "Alice let out a single 'Ha' while brushing one of her curls over her shoulder."
    show BBW haughty
    BBW "Ha!"
    BBW "I would never make a claim I could not back up. If you wish to see the truth of my words in action, then certainly. Let us race."
    FMG "God, are all Americans as snobby as you? Let's do this!"
    "Alice turned to me, her self-satisfied look still there."
    show BBW happy
    BBW "Any objections to Hotsure-san acting as judge? I'm sure he'll be impartial."
    show PRG neutral at Position(xpos=0.45, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    PRG "I... I could, maybe..."
    show FMG neutral
    FMG "Yeah, sure. But Keisuke, don't you think this is a forgone conclusion?"
    MC "Well..."
    hide PRG with dissolve
    menu:
        "You do seem the obvious choice, Mizutani-san.":
            $setAffection("FMG", 1)
            FMG "Heh, well whatever happens, happens I guess!"
            show BBW neutral
            BBW "Indeed..."
        "Alice seems pretty confident. I think this might be an upset.":
            $setAffection("BBW", 2)
            show BBW haughty
            BBW "Not an upset. As Mizutani-san said, it's a foregone conclusion."
            show FMG angry
            FMG "Whatever, 'princess'!"
        "I really don't know.":
            show BBW neutral
            BBW "Well, you shall know soon enough."
    scene Pool with fade
    "I went out to the pool as the two ladies got changed. Aida came out and stood next to me, and then the swimmers showed up."
    show FMG angry at Position(xpos=0.25, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    show BBW happy at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Three full laps should be adequate, I think. Any objections?"
    FMG "Just don't forget your pool cap thingy! Don't want to get your expensive mullet to get ruined by chlorine!"
    "They took their positions, I counted down from three, and they were off."
    stop music
    hide FMG with dissolve
    hide BBW with dissolve
    show cg BBW009 with dissolve
    "It was neck and neck for most of the first lap, but when the two reached the far end and pushed off the wall to return Alice began to pull ahead."
    "By the time she completed her first lap Alice was a full length ahead of Akira, and that lead grew for the rest of the race."
    "When she completed her third lap Alice almost leapt out of the pool, springing to her feet and looking down to watch Akira reach the end."
    hide cg with dissolve
    show FMG sad at Position(xpos=0.25, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    show BBW happy at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    play music Busy
    FMG "...Son of a bitch... Good job I guess... I'm going to bed. Later."
    hide FMG with dissolve
    show BBW happy at center with dissolve
    BBW "At least she's magnanimous in defeat."
    MC "Nice job. That was quite the blowout."
    show BBW haughty
    BBW "Was there ever a doubt? But as much as I enjoyed this contest, I have to get going."
    show BBW neutral
    BBW "Aida, what's next on my agenda?"
    hide BBW with dissolve
    "She was already walking away as Aida answered. Something about 'contacting her distributor.'"
    jump daymenu

label BBW010:
    $setSize(2)
    $setTimeFlag("aftersize2")
    scene Cafeteria with fade
    play music BBW
    "It was a quiet morning. Reminded me of the first day, after we all learned why we were here."
    "Looking around at the faces in the cafeteria when I arrived, I got the same vibe as before. The embarrassment everyone was probably feeling because of their 'second puberty' issue."
    "Standing out in the mildly dark gloom of the other students, one face was unexpectedly shining."
    show BBW happy at center with dissolve
    MC "Good morning, Alice."
    BBW "It {i}is{/i} a good morning, isn't it?"
    "I took another quick scan of the room, at the subdued expressions and lack of light-hearted chatting you would normally find."
    MC "It's subjective, I guess."
    MC "Is there a particular reason you're happy? Did Aida make some really nice treats or something?"
    BBW "Business, my dear Hotsure-san. Business is doing well, and it's set to do even better soon."
    MC "Oh, your, what would you call it... Your..."
    show BBW neutral
    BBW "My requisition agency."
    MC "Yeah... That. Are people coming to you for stuff?"
    show BBW happy
    BBW "Word is beginning to spread of my services, with strong customer satisfaction driving an increase of my market share."
    show BBW haughty
    BBW "And I have set my flag on a particular shore with tremendous growth potential, based on both necessity and a consistent need for replacements."
    MC "What... Cell phones?"
    show BBW happy
    BBW "Clothing, my dear boy."
    show BBW haughty
    BBW "It may have escaped your notice, being a guy and all - one apparently not particularly concerned with your own appearance, at that - but the changes we are experiencing are already making the clothing and other accessories we arrived with obsolete."
    show BBW happy at Position(xpos=0.3), Transform(xzoom=-1) with dissolve
    BBW "The school {i}does{/i} supply new uniforms in larger sizes as we need them, but their system does not have the motivating factor of free market capitalism to push their productivity."
    show BBW happy at Position(xpos=0.7), Transform(xzoom=1) with dissolve
    BBW "And such aid only extends to the clothing we need as students. Personal expression and comfort is left to the individual to provide, a tiresome chore when the only stores are outside the school, all the way in town."
    show BBW angry at Position(xpos=0.3), Transform(xzoom=-1) with dissolve
    BBW "And are we supposed to make that trip while wearing ill-fitting, potentially scandalous clothing?"
    MC "Hey..."
    show BBW happy at center, Transform(xzoom=1) with dissolve
    BBW "Now there's a better choice. I, through my personal contacts with the biggest and best names in clothing retail, can offer you-"
    MC "Hey!"
    show BBW surprised
    BBW "!"
    MC "I don't need a sales pitch. I know what you're doing. You offered to get a computer for me, remember?"
    show BBW neutral
    BBW "Yes, yes. Got carried away there for a second."
    show BBW happy
    BBW "But the fact that you're familiar with this is perfect, because I have a proposition for you."
    BBW "I have more potential customers than I have time and energy to corral myself. I need subordinates out there spreading the word and taking orders."
    BBW "How'd you like the job?"
    MC "What, like a salesman?"
    show BBW neutral
    BBW "Not 'like' a salesman. Actually be one."
    show BBW happy
    BBW "It's child's play. All you have to do is distribute these catalogues I've made-"
    "She handed me a box of tri-folded papers - more like brochures than catalogues - that she must have made on her computer."
    "While they lacked the polish an experienced graphic designer would bring, they did get right to the point, emphasizing the low prices and breadth of available sizes for every body type."
    BBW "-and talk up what a bargain this is. Be sure to emphasize the more prestigious name brands, and that other designer labels will be available in the future."
    show BBW neutral
    BBW "Still have a few more deals to finalize. This school is so remote, bulk shipping out here is a logistical nightmare."
    show BBW happy
    BBW "But we already have most of our selection here at the school, ready to distribute to any interested buyer."
    BBW "And if anyone wants to see our products in real life, you can tell them that I'm already wearing my first new set of clothing."
    BBW "The school told me it would take as much as a week to get me a larger set of uniforms, but I - going directly to the company that has the contract with this school - was able to get this comfortable and properly-fitting outfit before my old set became restrictive."
    "She did a quick modeling job, turning around to show how her top didn't pinch or roll up on her now-wider torso and rounder belly."
    show BBW happy at Position(xpos=0.5, ypos=0.0, yanchor=0.3), Transform(zoom=2.0)
    "I actually hadn't noticed that she had gotten plumper. It hadn't been two weeks yet, and I wasn't expecting to see such changes so quickly."
    "But apparently she had, because unless she had told me I wouldn't have noticed that this was a larger outfit, and it fit her as well as her old set. I could see how she thought this would be a good advertisement for her business."
    show BBW haughty at center, Transform(zoom=1.0)
    BBW "No muffin top, no pinching in the sleeves."
    "I was still looking over her plump middle, my eyes lingering on the soft curves of her belly, when she snapped me out of my reverie."
    show BBW happy
    BBW "Sound good?"
    menu:
        "I could use a little spending money.":
            MC "I could use a little spending money."
            BBW "Can't we all?"
            MCT "I don't think you're hurting..."
            jump BBW010_accept
        "(Might as well agree. I don't think she'd take 'No' for an answer.)":
            MC "Sure, I can do it."
            show BBW neutral
            BBW "I was hoping you'd be a little more fired up, but..."
            BBW "As long as you bring the thunder when you're engaging the customers, it's fine."
            MCT "Bring the thunder?"
            jump BBW010_accept
        "You can count on me!":
            MC "You can count on me!"
            BBW "Excellent! That enthusiasm is exactly what I'm looking for."
            jump BBW010_accept
        "No. I... I don't want to work for you.":
            jump BBW010_decline

label BBW010_accept:
    $setFlag("BBW_working")
    show BBW happy
    BBW "We can discuss your salary and bonuses later. Right now I want you to take advantage of the period before classes."
    BBW "Get out there and distribute those catalogues. I want to see that box at least half-empty before the bell for first period rings."
    "Caught up in her energy and enthusiasm, I sped away to start hawking her services."
    "I tried to think of who would need new clothes. Like Alice, I hadn't noticed any real growth in anybody yet."
    "But maybe necessity wasn't the best avenue to take yet. Maybe there was someone who just wanted something nice and flattering for after school."
    menu:
        "Shiori. She tends to dress conservatively, but doesn't every woman want to look nice?":
            jump BBW010_c1
        "Aida. Alice had mentioned she doesn't have an extensive wardrobe.":
            jump BBW010_c2
        "Honoka. Even if she hasn't grown, her needs already stretch most clothing shops.":
            jump BBW010_c3

label BBW010_c1:
    $setFlag("BBW010_shiori")
    scene Hallway with fade
    show AE angry at center with dissolve
    "I found Shiori prowling the halls, eyes jumping around from student to student, as if she was looking for violations of the school dress code or something."
    "For a second I thought this would be a good lean-in to my sales pitch, but when I saw her expression I scratched that idea."
    "Something a little more subtle would be needed."
    MC "Hey, Matsumoto-san. You sleep well?"
    show AE neutral
    AE "Hotsure-san. Well, I'd say about four hours at this point, however that's neither here nor there. Anything you need?"
    MCT "I could respond with 'Actually, it's about what you need.' Except she looks more serious than usual."
    MC "Just making conversation. We are classmates, after all. We should be friendly with one another."
    AE "Ah, I see. Yes, well, while I'm all for interaction, I'm preoccupied at the moment. Begging your pardon."
    "She started to turn away, but I at least had to give her a 'catalogue' to say I did my job."
    "Gracelessly, I almost shoved one of them at her arm."
    MC " Here. Something to check out at your leisure, when you have some free time."
    show AE surprised
    AE "Hm? What is... The Nikumaru Outlet Direct? Keisuke... is this what I think it is?"
    "Something in her tone told me to tread carefully. But I, not exactly a cat burglar, couldn't do much except flail around."
    MC "Well, it's... I'm not sure what you think it is. What do you..."
    show AE angry
    "She's glaring at me, and I see that playing coy wouldn't work even if I could do so properly."
    MC "Alice... Nikumaru-san has created a direct-market business. She orders stuff from manufacturers and can sell them at a discount. Clothes, school supplies, stuff like that."
    show AE angry
    AE "Hotsure-san... You can't just... ngh... Where is Nikumaru-san? I swear if she thinks she can just undermine the administration with this-this tripe!"
    MC "She should be in the cafeteria..."
    "Only now did I realize what a blunder this was. Of course the school would have some rule about not running a business out of your dorm or something like that, and of course Shiori would memorize it and expect it to be followed to the letter."
    hide AE with dissolve
    "Shiori was already brushing past me, making a direct line for the cafeteria."
    $setAffection("BBW", -1)
    "I looked down at the box of 'catalogues' I was holding, wondering if I should keep handing them out or consider myself fired."
    jump daymenu

label BBW010_c2:
    scene Cooking Classroom with fade
    "My first guess was that Aida would be at the cooking classroom, preparing Alice's breakfast. I wasn't wrong."
    show PRG neutral at center with dissolve
    "When I saw the baggy state of her clothes I thought this was probably a dead end. But then I wondered if she had any casual clothing that fit her and pushed on."
    MC "Good morning, Kodama-san. Making breakfast?"
    show PRG happy
    PRG "Oh! Uh, hello Hotsure-san. Is Nikumaru-sama ready for her food?  I-I can hurry it up..."
    MC "Oh no, it's not that. I was just walking by and thought I'd say hi."
    MC "Is that a new uniform? It looks a bit baggier than your old one."
    show PRG sad
    PRG "Um, d-do you not like it?"
    "For a split-second I thought about suggesting she buy something in her own size, but her doe-eyed expression made her look like she was on the brink of tears and I shot that idea down."
    MC "No, it's... it's cute."
    MC "But when you're cooking you don't really want anything that can get stained or burnt, right?"
    "I took out one of the 'catalogues' and held it out."
    MC "If you're interested in something a bit more form-fitting - for safety purposes - there's..."
    show PRG sad
    "I trailed off, because her expression had turned ashamed, lip bit and eyes downcast."
    MC "What?"
    PRG "I, I'm sorry Hotsure-san, but... W-well, I already got these from Nikumaru-sama. I was her first customer."
    "I suppressed a groan as I realized that of course Aida would already be in on Alice's plans. It was her need for more clothing that had first put the idea of doing this in Alice's head."
    MC "Right, right. Forgot. Well, sorry to bother you."
    show PRG neutral
    PRG "No, no! I'm sorry for, um, wasting your time... I'll, uh, still take one of the pamphlets, if you like..."
    "Hesitantly, I handed her one. I think not doing so would have made her more embarrassed."
    MC "If you'd like to place an order... Well, you know where to find me."
    if getAffection("PRG") >= 3:
        show PRG happy
        PRG "Yes, th-thank you, Hotsure-san... I-I'll see you later."
    else:
        show PRG neutral
        PRG "Yes, th-thank you, Hotsure-san..."
    "As I walked away I wondered who was more embarrassed, me or her. She was doing a better job of putting a happy face on it, at least."
    "My first stab at a sale and I whiffed it. But I still had time before class started, so the morning wasn't a complete waste. Yet."
    jump daymenu

label BBW010_c3:
    scene Hallway with fade
    "I was trying to think of where I could find Honoka when I was tackled from behind, collapsing to the ground."
    play sound Thud
    "A heavy, squishy weight on my back told me my search was over."
    show BE happy at center with dissolve
    BE "Hey, Kei-chan. You're looking a bit more spaced out than usual. You hit your head on something? I mean, besides me, of course."
    "Climbing to my feet, the sales pitch I had been rehearsing in my mind was pushed aside as I tried to think of something sarcastic and/or witty to say in response."
    MC "You ask me that after you run into me? Project much?"
    MC "At least help me clean these up."
    BE "What're these?"
    "I didn't process the question as I found myself distracted by Honoka's chest. After Alice's modeling routine I had curves on the brain, and Honoka was looking particularly big today."
    show cg BE010
    BE "Hey, Earth to Keisuke? You look like you took a hit to the noggin, considering you can't lift your neck above chest level."
    MC "I was just... Um..."
    hide cg
    show BE neutral at center
    "And then, as if struck by inspiration, I realized this was actually perfect."
    MC "I was just noticing that your shirt looks a bit tight. That can't be comfortable, can it?"
    show BE neutral
    BE "Oh yeah! Definitely tighter. Been noticing it get tighter every day recently. Was pretty fun at first, definitely proof that I'm growing where they said I would."
    BE "But, heh, yeah, it's not exactly comfortable. You have no idea how much bras pinch when they aren't made to fit you right."
    MC "Bras... Yeah. Those things."
    "Black lace bras with the cups almost transparent, frilly edges rising from her cleavage like dolphins jumping out of the sea. White cotton cups pulled taut by two great mounds of flesh, the straps digging into her shoulders..."
    BE "..."
    MC "Ah!"
    "I snapped my head downward to escape eye contact with her. Only then did I remember the box I was again holding in my hands. I took out one of the 'catalogues.'"
    MC "If you're looking for new clothing, there's a new service that just opened up. Really affordable clothes, some custom-made, direct from the manufacturer."
    "Quizzical, she looked the 'catalogue' over."
    BE "Huh. Wow, there's a lot of stuff in here. Pretty neat, actually. Most of the time once you get past a certain size, you can only get bras in boring colors or things without patterns. It really takes the fun out of it."
    BE "But, they're saying here they can do more custom patterns? Prices seem okay too, all things considered. How'd you get your hands on this?"
    MC "Ali- Nikumaru-san hired me. She knows people in high places at all these companies, so she has an 'in,' so to speak."
    MC "She's also selling school supplies and other stuff, but I guess she's focusing on clothing right now because... Well."
    "I gestured at her chest, wrapped up in a too-tight shirt and bra."
    show BE happy
    BE "Because it's like starting up an ice cream stand in the middle of a heat wave. She'll make a killing here if she can get everything authorized!"
    BE "You better be getting a cut of all of this if you're going to be helping her out. Don't let her take advantage of you."
    show BE surprised
    BE "Unless you're into that kind of thing. A big girl like Alice? Yeah, I could definitely see that. Was there a dominatrix getup in this catalogue? That'd be something to see on her..."
    "Man, my imagination was getting a workout today."
    "I shook my head to clear my mind."
    MC "I am being compensated (though the specifics haven't been hammered out yet). I believe she even mentioned something about a commission."
    MC "So can I put you down for a sale? I can run your order back to her before class starts, but I'm not sure how long it will be until everything arrives. She did say she already has a lot of stuff here..."
    show BE happy
    BE "Oh absolutely! Here, let me take a look again real quick... Yeah, I think I can spring for three bras and, maybe two shirts."
    BE "No, I'll just stick with this one for now. Luckily I've been looking up how to properly measure busts so I can figure out my own size."
    BE "Well, as long as I'm capable of getting my arms around them that is!"
    MC "Even if you have trouble measuring yourself, we can find clothing big enough..."
    "My voice trailed off as I was hit with the mental image of Honoka carrying a pair of breasts bigger than she was, carting them around in a wheelbarrow..."
    "...and running me over with them."
    "Like I said, my imagination was running on all cylinders today."
    "Salesman-mode had delayed the image conjured by her blithe comments about her growth, but the idea that she would grow so big she couldn't wrap her arms around herself... That was impossible to ignore."
    "I cleared my throat, blushing as I saw her smile mischievously at me, and sputtered."
    MC "I'll get back to you on how soon we can deliver these. Do you just want the plain model for the bras?"
    show BE surprised
    BE "Oh god no. I want one with the heart design, one with the joystick design, and, hm, I dunno, probably one with just some nice color. What do you think would be best; blue, pink, or black?"
    MCT "Black! Black!"
    MC "I think... black might be best. Bold, but not garish."
    show BE neutral
    BE "Sounds good to me. We'll go with the black then. And I circled the shirt I wanted too. Thanks Kei-chan. This is pretty cool, I appreciate it."
    MC "Well, I am being paid. But you're welcome, all the same."
    "She winked playfully and then spun around, jogging away."
    "Even from the back I could see the extra bounce... in her step. I admired it for a moment, and then turned back to the matter at hand."
    $setAffection("BBW", 1)
    "Landing a sale five minutes into my job was great, but I suspected Alice wouldn't ignore a still-full box of 'catalogues' because of it."
    jump daymenu

label BBW010_decline:
    stop music
    MC "No. I... I don't want to work for you."
    show BBW neutral
    "She was quiet for a second, as if she wasn't expecting that answer."
    BBW "I'm sorry? Could you say that again?"
    MC "I'm not interested."
    BBW "Do you understand what an opportunity this is?"
    BBW "Are you worried about balancing a job and your school work? Because I can understand your trepidation."
    menu:
        "It's not a question of time. I just don't want to work for you.":
            play music Bittersweet
            $setTimeFlag("BBWnowork")
            MC "It's not a question of time. I just don't want to work for you."
            $setAffection("BBW", -10)
            show BBW angry
            BBW "So be it."
            BBW "I hope you learn not to dismiss future opportunities so casually."
            BBW "The world can get quite competitive. If you expect things to be handed to you..."
            BBW "I don't have time for this. Good day."
            hide BBW with dissolve
            MCT "That was actually less volatile than I was expecting."
            jump daymenu
        "Well... I guess I can try it out.":
            play music BBW
            MC "Well... I guess I can try it out."
            MCT "It's not like I'm eager to work for her, but a little extra green wouldn't be too bad."
            jump BBW010_accept

label BBW011:
    scene Hallway with fade
    play music Schoolday
    "Another day done, and I find myself with no idea of what I want to do."
    "The afternoon's a blank page, but when you can start in a million different ways it's impossible to pick just one."
    MCT "It's not like I'm hoping to find something to do if I wander around the school long enough, but... maybe I will?"
    scene Gym with fade
    "Half an hour passed. I walked from the classrooms to the gym to the pool to behind the campus. Nothing."
    scene School Planter with fade
    "Another half hour. I went to the rooftop, the garden. Nothing."
    "At one point I thought I saw a person sneaking behind the cafeteria, but they were gone when I got there."
    scene Dorm Exterior with fade
    "Another fifteen minutes of walking, and I started to think maybe I should have gone to the gym and gotten a real workout in."
    "I had finally decided to go back to my dorm and take care of my homework when I was saved from my boredom by almost running into Aida."
    show PRG surprised at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    MC "Whoops. Pardon me."
    show PRG neutral
    PRG "O-oh! I'm sorry."
    "Coming right behind her, albeit not running headlong, was Alice."
    show BBW neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Don't mind her. She's too excited for her own good."
    BBW "Watch where you're going, Kodama-san."
    PRG "Y-yes, ma'am."
    MC "What's going on that has you in such a rush?"
    BBW "Kodama-san wants to join the film club meeting today. Apparently they're screening one of her favorite movies."
    show PRG happy
    PRG "It's called Waiting for the Wrong Bus. It's a romantic-comedy from a couple years ago."
    MC "Yeah, I've heard of that. Typical chick flick, right?"
    PRG "Oh, it's more than that. It's a beautiful and tender tale of two destined souls overcoming circumstances working to keep them apart-"
    MC "Isn't it because they don't like each other at first, but then they do?"
    show PRG angry
    PRG "No! It's not just that. Come watch the movie with us and you'll see."
    BBW "It does sound like every other rom-com I've seen."
    PRG "You're both wrong."
    menu:
        "Sorry, but I've got homework to do. And chick flicks aren't my thing, you know?":
            jump BBW011_fail
        "OK, OK. I'll come with and see for myself.":
            jump BBW011_prechoice

label BBW011_fail:
    MC "Sorry, but I've got homework to do. And chick flicks aren't my thing, you know?"
    show PRG sad
    PRG "Oh... All right."
    show PRG happy
    PRG "Maybe some other time?"
    MC "Uh, maybe."
    jump daymenu

label BBW011_prechoice:
    MC "OK, OK. I'll come with and see for myself."
    show PRG happy
    PRG "!"
    "Aida's face lit up, clearly happy to have another person accompanying her."
    stop music
    scene Hallway with fade
    "The three of us went to the club meeting. There were about a dozen members, the upperclassmen and women showing fully developed factors like muscles or extra-large hands."
    "But the screening room was much bigger than our classroom, which left plenty of seats for guests."
    "100 minutes later we were back out in the hallway."
    show PRG happy at Position(xpos=0.25)
    show BBW neutral at Position(xpos=0.75)
    play music Rain
    PRG "What did you think? Wasn't it beautiful?"
    "Aida had her hands clasped in front of her heart, her cheeks rosy and her eyes closed. She looked like she might swoon at a moment's notice."
    BBW "..."
    "Alice, meanwhile, looked like she was listening to elevator music playing at one-half speed."
    menu:
        "It was... sweet?":
            jump BBW011_c1
        "They didn't like each other at first, and then they did. I called it.":
            jump BBW011_c2
        "Well... Alice? What did you think?":
            $setSkill("Art", 1)
            jump BBW011_c3

label BBW011_c1:
    MC "It was... sweet?"
    PRG "Wasn't it? When Kenji ran into the burning building to get her teddy bear it was so touching."
    PRG "What was your favorite part?"
    MCT "Guess I've got to make a bluff check."
    MC "When Kenji... was complaining about Ayami and then suddenly he was talking about how much he loved her?"
    "That actually had to have been my least favorite scene, but that's why it was the only one I could think off."
    "And the way Alice fought back a snort, it didn't look like the movie had worked on her, either."
    "But this was an opportunity to free myself from the conversation."
    jump BBW011_c3

label BBW011_c2:
    MC "They didn't like each other at first, and then they did. I called it."
    show PRG angry
    $setAffection("PRG", -1)
    PRG "But it's more than that. It's about them realizing what the other means to them, and how happy they are together."
    MC "I have to say, I didn't see that. They spent, like, 75%% of the movie sniping at each other, and then suddenly they want to be together?"
    PRG "It's not sudden. Don't you remember the scene where Kenji warns Ayami not to eat the shrimp that made everyone else sick?"
    PRG "It's because deep down he cared about her."
    MC "That only makes sense if you can believe that neither would come out and say what they were feeling."
    MC "But that seems to be every movie like this. All their problems would be solved if they were just honest for five seconds."
    show PRG happy
    PRG "But then they wouldn't get to show their love. What about when Kenji ran into the burning building to get Ayami's teddy bear? Wasn't that dashing?"
    MC "And then he realizes he could have gone around the building to get to Ayami's room, because the fire hadn't touched that place yet. And then he trips and knocks himself out. It was amusing."
    MC "But running into the building in the first place? I'm really not a fan of the big, showy demonstrations of love. They always come across as manufactured."
    show PRG angry
    MC "That climax in particular... Probably the only realistic thing in the movie was the firefighters berating him for that stupid stunt."
    PRG "But he got the bear!"
    MC "The bear was never in danger."
    PRG "That's not the point!"
    "I could see how quickly this was falling apart, and I didn't want to keep digging myself deeper."
    "Fortunately, I had an out."
    jump BBW011_c3

label BBW011_c3:
    show PRG neutral
    MC "Well... Alice? What did you think?"
    "Alice looked down at Aida, still blushing deeply."
    BBW "I think it was exactly like every other rom-com I've seen."
    MC "Is that a good thing?"
    BBW "If it's what you're looking for, yes. The familiar has its own appeal."
    show PRG sad
    PRG "But you didn't like it?"
    "Alice hesitated again before responding. Despite her bored expression, her quick glances at Aida told me she was being careful with her words."
    "Concern for Aida's feelings, I would assume."
    BBW "The genre is well-established, and as such it has too many ideas that have become clichéd through overuse."
    BBW "And all too often that leads to an attempt to outdo the clichés, rather than to break fresh ground."
    BBW "The once-novel idea of having two people not express their feelings gets turned into an obstinate game, each character over-exaggerated to the point of cartoonishness."
    show PRG neutral
    PRG "Games?"
    BBW "If there is something you want and you do not make every effort to claim it, what are you doing? You are playing around, wasting time and effort."
    MC "That's a pretty harsh view of romance, don't you think? You make it sound like a guy going after a girl sees her as nothing but a prize."
    BBW "Her heart is the prize."
    BBW "Courtship is a challenge, the man is tested and tries to prove himself. And, if he is successful, he is rewarded with her love."
    MC "But the woman doesn't have to do anything? Doesn't have to prove herself?"
    BBW "Women have their own trials in any relationship, but how often are we the pursuer?"
    MC "Not big on women's lib, I take it."
    show BBW haughty
    BBW "Au contraire. I've never met a woman in our generation more dedicated to conquering the world of business and smashing the glass ceiling than I am."
    BBW "I'm simply a realist. Even with advances in women's equality it's considered custom for the man to initiate, to pursue, to 'win.'"
    BBW "But this set-up gives us ladies our own power, as long as we recognize it and use it."
    MC "So you don't mind being considered an object, a trophy?"
    MC "You wouldn't be insulted if, say, I asked you out, dated you, and then 'won' you? Made you my wife?"
    "She chuckled, brushing one of her locks behind her shoulder."
    BBW "Hotsure-san... Do you know what a woman wants?"
    MC "Eh?"
    MC "You mean like flowers and chocolates?"
    show PRG happy
    PRG "Or stuffed animals!"
    show BBW neutral
    BBW "No, I'm not talking about simple gifts."
    BBW "I'm talking about romance. Do you know how to woo a lady?"
    MC "Yeah! I mean... I've dated before. I understand romantic... stuff."
    MCT "I just lost the argument when I called it 'stuff,' didn't I?"
    show BBW haughty
    BBW "Romantic 'stuff.' Heh."
    BBW "I don't think I need to worry about becoming merely your wife."
    BBW "Thinking it is your job to win means you are destined to lose."
    show BBW neutral
    BBW "Fun talk, though. We should do this again."
    BBW "Hopefully with a better movie."
    show PRG sad
    PRG "But {i}I{/i} liked it."
    jump daymenu

label BBW012:
    $setProgress("BBW", "BBW015")
    scene Classroom with fade
    play music Schoolday
    "When the classes ended for the day, I was more than ready to shut my brain off."
    "The whammy of the news of our condition didn't mean we got to stop learning. Tashi-sensei ran the class like a herd of pack mules, just instead of piling loads of goods onto our backs we were packing our brains full of facts and figures."
    "I had several chapters of reading to get through later that day, but first I needed to decompress before my grey matter started to overheat."
    "But as I gathered up my things and made to leave, I felt a hand on my shoulder."
    show BBW neutral at center with dissolve
    BBW "Keisuke, do you have a moment?"
    MC "Uh... Yes?"
    show BBW happy
    BBW "Excellent. We need to have a meeting to discuss the future of The Nikumaru Outlet Direct."
    BBW "I'm calling all employees in, so come along."
    scene Cafeteria with fade
    "I followed Alice to the cafeteria, where Aida had already laid out tea and crumpets at Alice's usual table."
    show BBW happy at center with dissolve
    BBW "Good. We're all here."
    MC "All three of us?"
    show PRG neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    show BBW neutral
    BBW "Both of us. Kodama-san is still operating in her capacity as my personal assistant, so for now this is still a two-person operation."
    show BBW happy
    BBW "There's me in the CEO/CFO/President chair, and you pounding the pavement to get orders and make deliveries."
    hide PRG with dissolve
    BBW "It's exactly the type of humble beginnings that all great corporate empires are born from."
    show BBW angry
    BBW "But we're in the midst of a crisis right now. Our very existence as this school's premiere clothing retailer is under attack."
    show BBW neutral
    BBW "Hence this meeting. We need to address this attack on free enterprise: Matsumoto-san asserts that it violates the school's rules and regulations for a student to run a business on campus."
    if not getFlag("BBW010_shiori"):
        MC "Wait, we're not allowed to be doing this? Then why are we having this meeting?"
        show BBW haughty
        BBW "Don't be so hasty to accept defeat, Keisuke. As in any competition, to win in business is not just to strive for success, but to reject failure."
        BBW "If you allow others to set the terms you're handicapping yourself. It is only when you seize control of the playing field and the rules of the game that ultimate victory becomes possible."
    MC "So you think there's some sort of loophole to exploit?"
    show BBW haughty
    BBW "Over, under or through. There's always a way to get past a mountain."
    BBW "The Nikumaru Outlet Direct will not shutter its doors just because one nosey bureaucrat seeks to hobble us. I've already found a way forward."
    jump BBW012_c1

label BBW012_c1:
    menu:
        "About that name..." if not getFlag("BBW012_c1_1"):
            jump BBW012_c1_1
        "About that name... (disabled)" if getFlag("BBW012_c1_1"):
            pass
        "Maybe we should just stop before we get into real trouble." if not getFlag("BBW012_c1_2"):
            jump BBW012_c1_2
        "Maybe we should just stop before we get into real trouble. (disabled)" if getFlag("BBW012_c1_2"):
            pass
        "I'm all ears.":
            jump BBW012_c1_3

label BBW012_c1_1:
    $setFlag("BBW012_c1_1")
    MC "About that name... It's a bit long, isn't it? And kind of bland."
    show BBW neutral
    BBW "That is one thing addressed in my plans. I admit, marketing is not my strongest suit."
    BBW "But if you have a suggestion, by all means. Share."
    MC "How about... Niku-Knacks!"
    show BBW angry
    BBW "..."
    show BBW neutral
    BBW "OK. Marketing is a weak point for both of us."
    BBW "I'll keep that in mind."
    jump BBW012_c1

label BBW012_c1_2:
    $setFlag("BBW012_c1_2")
    MC "Maybe we should just stop before we get into real trouble."
    show BBW angry
    "Alice scoffed-"
    BBW "Scoff."
    "-and gave me a withering look, but I pushed on."
    MC "Maybe Matsumoto-san's a bit strict, but she's not being a hard-ass-"
    MC "Um, she's not some sort of killjoy that has it out for you personally."
    MC "The school has rules for a reason, even if we don't always like them. It's lame, but true."
    MC "And with everything on our plates right now anyway, with school work and dealing with our conditions, do you really want more drama in your life by starting something with the class president?"
    MC "Or maybe the teachers and administrators?"
    "She didn't respond immediately, but I simply waited. She looked irritated enough already and I knew better than to poke her."
    "After a moment she exhaled."
    show BBW neutral
    BBW "This is how I'm dealing with it."
    MC "I'm... sorry?"
    BBW "The schoolwork isn't too much for me. If anything it's a bit easier than at my old school."
    BBW "But the news about our condition? I've already tried to stop it by dieting and working out. It wasn't successful, and I've come to accept that - for now, at least - my weight gain will run its inevitable course."
    show BBW angry
    BBW "But that doesn't mean I will allow it to change my life."
    BBW "I was already on the path to a life of success and prestige in the world of business before I came here. My size will not be a roadblock, or even an obstacle."
    show BBW haughty
    BBW "I will proceed as I was before, as if nothing has changed."
    BBW "I am not ignoring what is happening, but neither will I allow it to control me or my actions. That is not the Nikumaru way."
    menu:
        "Oh... I think I understand.":
            jump BBW012_c2_1
        "I still think you're making trouble for yourself down the line.":
            jump BBW012_c2_2

label BBW012_c2_1:
    MC "Oh... I think I understand. You're pretty serious about this, huh?"
    $setAffection("BBW", 1)
    BBW "I am always serious about business, Hotsure-san."
    MC "I can respect that, even if I'm not entirely convinced it won't come back to bite you."
    MC "But if you're sure you want to do this, I can help."
    jump BBW012_c1

label BBW012_c2_2:
    $setFlag("BBW012_c1_1")
    MC "I still think you're making trouble for yourself down the line."
    MC "And I've gotta be blunt, I don't fancy getting Matsumoto-san or any of the teachers getting on my case because you're trying to make a few extra dollars."
    show BBW angry
    $setAffection("BBW", -1)
    BBW "If you're that concerned, don't be."
    BBW "You're simply a hired hand. If any hammer is dropped it will be on my head."
    MC "I'm not asking you to take all the blame-"
    show BBW haughty
    BBW "Whatever your objections, you'll be protected. This is my business, after all."
    BBW "You worry about making your deliveries, and I'll handle everything else."
    jump BBW012_c1

label BBW012_c1_3:
    show BBW happy
    BBW "Earlier today I contacted a clerk at a law firm that does occasional out-of-house work for my father's business."
    BBW "As we speak she's filing the paperwork to create the Alice's Wishes Granted LLC."
    BBW "Its official address will be a PO box I've secured in town, with all correspondence coming or going through it. Legally speaking, no business will be conducted on school grounds."
    MC "That's your solution? Won't that be inconvenient for people who want to place orders, having to mail a letter to a PO box?"
    MC "And who's going to collect the mail? I don't think-"
    "Alice held up a hand to stop me."
    show BBW neutral
    BBW "We won't be taking orders through snail mail. That's far too inefficient."
    BBW "If you hadn't interrupted, I would have explained that I also have a software engineer developing a website and business email account."
    BBW "Everything involved in placing the order and paying for it will be handled online. The PO box is merely a formality."
    BBW "Understand?"
    MC "I guess. Is it really necessary?"
    BBW "Yes. As I said, by establishing a storefront off school grounds I am no longer in violation of any rules."
    MC "And what about filling the orders? Will the packages be delivered to you here?"
    show BBW happy
    BBW "Got it in one. While there are prohibitions on what items can be mailed to students here, our selection of products does not include weapons, drugs, or other such items."
    BBW "Everything to be mailed to me is in keeping with permissible personal effects."
    MC "You're still exchanging goods for money."
    BBW "No, I am accepting gifts purchased by my fellow students and then graciously returning them when it turns out they do not suit my needs."
    MC "You're... what?"
    "She grinned deviously, like a smug cat meme."
    show BBW haughty
    BBW "Once the website is up and running you'll see. Or perhaps I should tell you now."
    BBW "The website and order form will be constructed so as to appear as if our customers are buying items on my personal wish list."
    BBW "All orders will be mailed to me, with the customer's information included as a special message so I know who the thoughtful party is."
    MC "And once you have a new skirt or set of underwear you'll say 'Oh, this doesn't fit me' or 'Oh, it's not my style' and you 'give it back' to the person who bought it."
    "Her smile didn't grow wider, but it somehow grew more smug."
    MC "One question: What's the difference between bending the rules and breaking them?"
    BBW "Breaking gets you punished. Bending increases your profit margin."
    jump daymenu

label BBW013:
    scene Hallway with fade
    "My name had come up on the class clean-up schedule again, so when I got out for the day the hallways were mostly empty. Everyone else was back at their dorm or enjoying the pleasant afternoon."
    "It made it easy to recognize the two figures over by the stairs, even if one wasn't the only blonde woman on campus and the other wasn't..."
    show BBW angry at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    MCT "Oh no..."
    "If the other wasn't my roommate."
    play music RM
    show RM angry at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    "I couldn't hear what they were talking about, but I could see Alice standing rigid, her expression stony cold as Daichi held up one of those measuring device clamp things."
    "What were they called? Shiori would probably know..."
    "Anyway, I started walking slower, not wanting to eavesdrop on the two but also fearing I had some idea of what they were talking about."
    RM "Taking these measurements now is vital if we're going to chart your future expansion. We need to know how much you weigh and where your body distributes your fat-"
    BBW "Grrrr!"
    RM "-to compare with how big you - and specific parts of you - will become later."
    show RM neutral
    RM "I also need you to answer some questions about your eating habits, your exercise routine. If you have one."
    RM "Are you eating more than you did before you came here? More often? Are you hungrier than before?"
    RM "Do you find it harder to carry your weight? Do you get tired more quickly?"
    RM "This will all tell us what 'they' are doing to you, which will give us a clue as to their ultimate plans."
    MCT "Yeah, this is exactly what I feared."
    BBW "'They?' 'They' who?"
    show RM angry
    RM "The govern-"
    BBW "Clearly I was being facetious. I don't actually want to know what paranoid fantasy you're harboring."
    MCT "I should probably step in and get Daichi out of there before she really tears into him."
    MCT "Then again, I don't want to bring her wrath upon myself..."
    menu:
        "Stay back. Daichi got himself into this.":
            jump BBW013_c1
        "Rescue Daichi.":
            jump BBW013_c2

label BBW013_c1:
    play music Tension
    "I backed away slowly, not drawing either's attention, and hid inside a classroom door."
    BBW "Do you think I have nothing better to do than be accosted by some conspiracy theorist?"
    BBW "What are you, a 'growth truther?' Do you think they're slipping us hormones in our food?"
    show RM neutral
    RM "That might actually be-"
    show BBW angry with hpunch
    BBW "I DON'T HAVE TIME FOR YOUR GAMES, BOY!"
    BBW "I am stuck here on an isolated rock, shoved away with a bunch of other... people with conditions like mine, dealing with the news that my own body is going to blimp out of its own accord."
    BBW "And you want to get in my face about some secret cabal making me fat?"
    RM "To be honest, I don't know who exactly is doing this."
    show BBW angry with hpunch
    BBW "SHUT! IT!"
    BBW "And answer me this: if there was an insidious conspiracy bent on performing experiments on random people, do you really think that I, Alice Nikumaru, daughter of Daitaro Nikumaru, would be one of those guinea pigs?"
    BBW "My father has connections reaching through every corner of the world's industrial and political. No one would dare subject me to something like this without invoking his wrath."
    RM "There might have been-"
    show BBW angry with hpunch
    BBW "I TOLD YOU TO SHUT IT!"
    BBW "And get out of my sight. Don't ever even think of planting your grimy little paws on me, and don't ever talk to me about my body again."
    show RM sad
    RM "OK. OK."
    hide RM with dissolve
    show BBW angry at center with dissolve
    "Daichi didn't quite run from her, but he didn't drag his feet."
    "Alice stayed standing there and watched him leave. After a while she exhaled, but she didn't look any less tense."
    "I didn't want to take the long way back to the dorms, so I'd have to walk past her. Hopefully she wouldn't-"
    BBW "Hotsure-san."
    MCT "Uh-oh."
    MC "Ali- Nikumaru-san. You look... tense."
    BBW "Did you hear any of that buffoon's rambling?"
    MC "Uh, yeah. I got the gist."
    MC "Daichi's kind of like that-"
    BBW "Daichi? Is that his name?"
    MC "Yep. He's my roommate..."
    "The next words shriveled in my mouth as Alice turned the full intensity of her glare upon me. Too late, I realized my mistake."
    BBW "Your roommate?"
    $setAffection("BBW", -1)
    BBW "So is it a coincidence that out of all the students on campus, he came to me, your classmate, to harass?"
    BBW "Who put it in his mind to come to Alice, the soon-to-be portly girl?"
    MC "Actually he's in our class-"
    MC "Never mind that. I didn't tell him to bother you. I want nothing to do with his ramblings, and I would never put him up to coming after you."
    BBW "(tsk)"
    BBW "You didn't stop him, either."
    MC "No, but... What was I supposed to do?"
    "Alice held up a dismissive hand and turned away."
    BBW "Teach him to have more class. He's in the same boat we all are, isn't he?"
    MC "Actually, he's here because his sister has a growth factor."
    BBW "Either way, he should have some empathy, if not basic social graces."
    hide BBW with dissolve
    "She walked off in a huff, and I wasn't too eager to chase her and explain my noninvolvement."
    "Better to take the hit and let her be angry with me for a while."
    jump daymenu

label BBW013_c2:
    "Daichi was opening his mouth to retort. I couldn't predict his exact words, but I knew they would be some form of doubling down, trying harder to get her to listen to him."
    "I couldn't let that happen. Alice didn't deserve to listen to his ramblings, and Daichi needed to be pulled out of the hole he was digging for himself."
    MC "Daichi! There you are."
    show RM neutral
    RM "Huh? Keisuke?"
    MC "Shiori is looking for you. She said something about a sample the nurse needs to get from you?"
    show RM sad
    RM "Crap! Where was she?"
    MC "Back that way."
    "I hooked a thumb over my shoulder, and Daichi immediately pelted in the opposite direction. He was gone before I even finished walking up to Alice."
    hide RM with dissolve
    show BBW angry at center with dissolve
    play music Rain
    BBW "..."
    BBW "Matsumoto-san wasn't in the classroom, was she?"
    MC "No."
    "Alice let out a gust of air, relaxing in body, but not quite spirit. A feeling of tension hung around her, like an aura."
    show BBW neutral
    BBW "No. At this time she should be in the library, taking care of her paperwork."
    MC "Probably. She is predictable, if nothing else."
    show BBW happy
    $setAffection("BBW", 1)
    BBW "I owe you my thanks, Hotsure-san. If that fool had continued, I'm not sure I could have been held responsible for my actions."
    MC "I wouldn't be surprised. At least you don't have to share a room with him."
    show BBW neutral
    BBW "He's your roommate? Then you must know if he's always like that."
    MC "Yes and no. He's got no shortage of ideas about what's 'really happening' here, but this is the first time I've seen him going that far."
    BBW "Trying to put his hands on someone else?"
    MC "I really don't think he was trying to be grabby or anything. He just... forgot about personal boundaries."
    MC "He is very serious about all this."
    BBW "I suppose some of us are having a harder time dealing with this than others."
    BBW "Assigning blame for this may be more accommodating than accepting it's pure chance. It's easier when you can be angry at someone."
    BBW "What is his growth factor? It must be severe to set him off like that."
    MC "He... It's rather personal."
    "What? It's not like I could tell her Daichi doesn't really belong here."
    "It's not my place to talk about his sister."
    BBW "I understand."
    BBW "Still, one would think that someone in his position would have more empathy for the rest of us. We have all been blindsided by this. None of us should be making it harder for anyone else when it comes to our conditions."
    MC "Yeah. I'll tell him to ease up when I see him later."
    MC "Say, Alice..."
    "I hesitated a moment, but she looked at me, waiting."
    MC "Don't take this the wrong way, but I'm curious. Are you upset about your weight?"
    BBW "No."
    "She answered pretty quickly, in that way that makes it hard to believe someone. But I didn't say anything."
    BBW "I accepted what was happening once I learned the news, and I know I can address my weight gain once it fully happens."
    BBW "In the meantime, I am still Alice Nikumaru. I am not defined by my size or my appetite."
    BBW "Character is revealed in how one deals with tribulation, not what form those trials take."
    MC "You sound like you're dealing with it pretty OK."
    "I was about to walk away, but then I decided..."
    MC "Hey, Alice. I was about to get a snack at the cafeteria. You hungry?"
    BBW "...Hmm..."
    show BBW happy
    BBW "I could go for some cake."
    jump daymenu

label BBW014:
    scene Gym with fade
    play music Peaceful
    "Gym today was a free day, everyone finding something quasi-athletic to do. Afterwards I ended up being one of those called on to clean up the equipment lying around."
    "I wasn't alone, per se, but with a handful of us spread across the entire gym it was dead quiet."
    "After a while I noticed I was drifting over to where Alice was bending down to gather up some croquet mallets."
    show BBW neutral at center with dissolve
    MC "Hey, Alice."
    BBW "Hotsure-san."
    BBW "Can you give me a hand with the mats? Somebody must have been practicing wrestling, or maybe judo."
    MC "I think it was sumo."
    "I inhaled sharply. The idea of sumos made me think of Alice's plump frame destined to grow fatter, and it probably brought the same image to her mind."
    "As we folded up the mats and carried them to the equipment room I scrambled to think of a way to change the subject."
    MC "I don't think I've asked this, but you're from America, right?"
    show BBW neutral at Position(xpos=0.3) with dissolve
    BBW "My mother is. I've lived both there and here in Japan, going to school in both countries."
    MC "What part? Of America, I mean."
    BBW "The east coast. My mom's side of the family has been involved in banking and investing for generations."
    MC "Oh... Are there beaches? Where you lived, I mean."
    "She chortled quietly, her lip turning up in a tiny grin."
    BBW "There are a lot of beaches up and down the east coast. And the west coast. And Hawaii is full of them."
    BBW "But they're not all sun and warm water. Up in New England... You're not doing much surfing or sunning."
    "We finished stacking the mats up, but continued chatting as we cleaned up."
    BBW "Did you grow up near the water?"
    show BBW neutral at Position(xpos=0.8) with dissolve
    MC "No. I just... When I think of America I think of beaches."
    MC "Either that or burgers and fries."
    MC "!"
    "I almost bit my tongue clamping my mouth shut."
    "First the reference to sumo, then greasy American fast food."
    "Did Alice think I was trying to bring up her weight?"
    "She didn't say anything, and I looked around desperately for something else to talk about."
    show BBW neutral at Position(xpos=0.65) with dissolve
    MC "Why are there hockey sticks here?"
    BBW "For the winter, I assume."
    MC "No, out here. Who was trying to play hockey?"
    MC "And dumbbells! This isn't the weight room."
    BBW "I believe I saw Mizutani-san working with those. They may be her personal effects."
    MC "That makes sense. Think we should put them off to the side?"
    "I carried the weights to the bleachers, where I found a large round thing on the floor."
    MC "I don't even know what that is."
    show BBW neutral at Position(xpos=0.2) with dissolve
    BBW "It's used in curling. It's the thing you push across the ice."
    MC "Didn't even know we had stuff like that here. What it's called?"
    BBW "A curling... rock?"
    MC "Rock?"
    BBW "Errrr..."
    show BBW angry
    BBW "Nobody curls in America! That's a Canadian thing."
    "She huffed as she kicked the curling 'rock' across the floor and to the equipment room."
    show BBW neutral:
        linear 1.0 xpos 0.35
    BBW "Grr."
    show BBW neutral:
        linear 1.0 xpos 0.5
    BBW "Bah!"
    show BBW neutral:
        linear 1.0 xpos 0.65
    BBW "Huff."
    show BBW neutral:
        linear 1.0 xpos 0.8
    BBW "Gar."
    "I found a couple skis propped up against the wall and followed her."
    MC "Somebody was messing with the skis as well. Did I sleep through the summer and fall?"
    show BBW neutral
    BBW "Put them over there with the cap gun."
    MC "Why is there a rifle here?!"
    BBW "It's fake, Hotsure-san. I assume it's used for biathlon practice."
    MC "Biath-wha now?"
    BBW "Cross-country skiing and rifle shooting. It's an Olympic sport."
    show BBW neutral at center with dissolve
    MC "Seriously?"
    pause 1
    MC "You're not joking."
    MC "Who thought to put those two things together?"
    BBW "I don't know. I do know it's as ridiculous as it sounds."
    BBW "I saw it at the Winter Games a few years ago. Completely nonsensical."
    MC "You've been to the Olympics?"
    BBW "As a spectator."
    MC "Wow, that's pretty cool."
    "She shrugged."
    show BBW neutral at Position(xpos=0.2) with dissolve
    BBW "Far too many crowds, security checkpoints every twenty feet, and if you wanted to see two different competitions in one day you had to hope they were in the same arena."
    BBW "Too much of a headache to be worth the trouble, if I'm being honest."
    MC "But to travel to another country, meet people from other nations..."
    BBW "Traveling to other countries can actually be tedious. Everywhere you go it's the same franchises, the same highly polished tourist spots where the poverty or unrest is kept at bay to present a picture perfect image of the country."
    BBW "You don't really get a taste for the culture that way."
    show BBW neutral at Position(xpos=0.65) with dissolve
    BBW "As for meeting other people... Only if you speak the same language."
    MC "Oh... hadn't thought of it that way."
    "I didn't have much to say to that, so as Alice and I picked up some kendo sticks I let things get quiet."
    "But things felt even more awkward being next to someone in complete silence."
    "I've never thought small talk was something essential, but as I saw the time needed to finish this stretching out before me I realized I needed to fill it somehow."
    MC "So... have you traveled a lot?"
    "She looked down at a pair of luchador masks she had picked up before answering."
    BBW "I've 'been' to several countries in Europe and Asia, in that I've flown to them while Father conducted business."
    BBW "And we've vacationed in places like Geneva and Tuscany and Monte Carlo. Though we spent almost all our time at exclusive hotels and resorts."
    show BBW sad
    BBW "Tiny little islands within the larger nations, almost isolated from the culture less than a mile away."
    MC "Huh?"
    show BBW neutral
    BBW "The places that cater to the rich tend to have the same trappings, the same luxuries. Sometimes there's an effort to bring a taste of the local cuisine, music and whatnot in, but the separation can become palpable."
    show BBW neutral at Position(xpos=0.8) with dissolve
    BBW "I've always found more amusement and insight in those times when we left the carefully constructed pockets of luxury."
    MC "You like rubbing elbows with the common folk, eh?"
    BBW "Nnnnnn- Sort of."
    BBW "Don't get me wrong, I don't want to sleep on a straw mat or wash myself in an outdoor shower."
    show BBW neutral at Position(xpos=0.2) with dissolve
    BBW "But if I'm going to spend several hours flying just to have the same spa services, the same massages, the same Swiss chocolates and mineral water, why even travel?"
    BBW "When I leave home I want to leave my comfort zone. I want to experience something new."
    MC "So when you were in Geneva did you ever go hiking up the alps?"
    BBW "Oh, no! I'm much too sensitive for so much physical strain."
    show BBW happy at Position(xpos=0.65) with dissolve
    BBW "But I did ride the cable-car up to the top of one of the mountains. A splendid view."
    BBW "And the brisk wind made the hot tub extra luxurious that evening."
    MC "So you want to leave your comfort zone, but you don't want to be uncomfortable while you do it?"
    show BBW neutral
    BBW "Mmmm..."
    show BBW happy
    BBW "Yes!"
    MC "And you don't find that odd?"
    show BBW neutral
    BBW "Why should I?"
    "I had no answer to that, so I distracted myself with gathering up a set of bowling pins."
    "After enough time had passed I shifted the conversation."
    MC "Have you been in touch with any friends from your old school?"
    show BBW neutral at Position(xpos=0.2) with dissolve
    BBW "Not lately."
    BBW "There were several people from my old academy I was friendly with, but we've all gone to different places for our higher education."
    MC "Oh."
    MC "I was just thinking..."
    BBW "..."
    MC "It's been a couple weeks since we all got here. It's starting to feel like I'm used to this place."
    MC "At first I didn't try to get in touch with my friends from back home, because none of them probably know about this place or the whole 'factor' thing. But now that I've come to grips with it I can't think of a reason not to tell them."
    "Too late I realized what I had just done: opened the door to bringing up Alice's factor. Again."
    BBW "Your factor concerns your hair, yes?"
    BBW "It doesn't seem to be that significant a dilemma."
    MC "I didn't mean-"
    show BBW neutral at Position(xpos=0.8) with dissolve
    "She looked at me sideways, not grinning but not frowning. Almost like she was trying to do both at once."
    BBW "You're pretty easy to read, Hotsure-san."
    MC "Uh..."
    BBW "You're thinking of my weight, and you're worried about mentioning it."
    BBW "After the incident with your roommate the other day I can understand your trepidation."
    MC "Sorry."
    show BBW neutral at Position(xpos=0.35) with dissolve
    BBW "You don't have to apologize for making me aware of my condition."
    BBW "Though if you want to apologize for thinking that I am so frail as to need to be shielded from reality, I will accept it."
    MC "What?"
    BBW "{i}Sigh{/i}"
    BBW "I don't need to be reassured or comforted. My condition is not a death sentence."
    BBW "Having everyone here walk on eggshells around one another would be antithetical to this institution's reason for being, would it not?"
    BBW "We're supposed to address our inevitable growth and learn to live with it, aren't we? A direct confrontation is the only way to do so."
    show BBW neutral at center with dissolve
    BBW "I've already done that, thinking of dieting or exercise and deciding not to make myself miserable."
    BBW "And if I can turn that page, what makes you think you need to shoulder my burden?"
    MC "I wasn't... I mean, not everyone is as fine with this as you."
    MC "I can think of a couple girls in our class having more trouble coming to terms with all this."
    BBW "And I hope they can find peace with it. I sincerely do."
    BBW "But I have other things in my future more important than the number on my scale."
    show BBW happy
    BBW "For instance, it looks like we're almost done with this."
    BBW "I need to take care of my studies, and then it's back to work getting our little business venture going."
    show BBW happy at Position(xpos=0.2) with dissolve
    BBW "Pick up the pace, Hotsure-san! We're almost out of here."
    hide BBW with dissolve
    "We stuffed the last pieces of equipment in the closet, closed it, and went our separate ways."
    "An uneventful conclusion to an uneventful day."
    "Getting a chance to have a real, non-business-related conversation with Alice was pretty eventful. Even if it had been out of desperation to kill time."
    jump daymenu

label BBW015:
    $setProgress("BBW", "BBW016")
    scene Hallway with fade
    show BBW happy at center with dissolve
    play music BBW
    BBW "Keisuke! A mission!"
    "I was headed to... breakfast..."
    show BBW neutral
    MCT "There goes my train of thought. How am I supposed to manage if I can't supply a running commentary of my day?"
    BBW "Keisuke."
    MC "Yes? Good morning."
    show BBW happy
    BBW "Good morning. Are you ready to work?"
    MC "I'm ready for breakfast. It's not work, but it's-"
    show BBW neutral
    BBW "Breakfast is important, but so is fulfilling one's obligations."
    BBW "The wheels of business never stop turning, and thus we ourselves can never cease."
    MC "It's a little early to go looking for sales."
    BBW "That's not what I need you for. Do you remember the restructuring of our company?"
    MC "Hmm? Oh! Right."
    MC "That wish list thing."
    "Only now did I notice the thick mailing envelope in Alice's hand."
    MC "Did we already get an order?"
    show BBW happy
    BBW "First of the company's new era."
    BBW "And you have the singular privilege of making this first delivery. The first delivery of any kind for the company."
    "She handed me the brown, bubble interior envelope, already open."
    "Inside was a folded sheet of paper and a small green and white garment wrapped in plastic."
    "The paper was an order form. Turned out the garment was a pair of panties, ordered by one Moriko Fukushi."
    MC "Where can I find this woman?"
    BBW "She's in room 306 of the women's dorm. You'll find it on the sales slip. If you hurry you can probably find her there now."
    show BBW angry
    BBW "But exercise caution."
    BBW "Matsumoto-san is already keeping one eye on me, and I suspect her myopic adherence to the concept of rules blinds her to the actual letter of the law."
    BBW "Which I am fully in line with, as you know."
    BBW "It's a 'forest for the trees' situation. She has her own idea of what the spirit of the law is, and she's unflappable in following that."
    show BBW neutral
    BBW "The most efficient solution is to avoid contact with her. I have no quarrel with her personally, after all."
    MCT "It would only be antagonistic to point out the simplest solution is to drop this whole venture."
    MCT "And hypocritical. It's not as if I'm turning down the promise of money."
    MC "I got it. Stealth."
    "Alice nodded and let me go."
    hide BBW with dissolve
    stop music
    "The question now was, how to get to the dorm? Guys weren't forbidden from going into the women's dorm building, but it stood to reason it was the place I'd most likely run into Shiori."
    menu:
        "Take the direct approach. Get in, get out.":
            jump BBW015_c1_1
        "Go around and come in from the rear. Less chance of getting caught.":
            jump BBW015_c1_2
        "Think outside the box. Go through the vents.":
            jump BBW015_c1_3

label BBW015_c1_1:
    scene Dorm Exterior with fade #FIXME this may need new graphics
    "I tucked the mailing envelope into my backpack and headed for the women's dorm with deliberate speed."
    show AE neutral at Position(xpos=0.65, ypos=0.0), Transform(rotate=-20) with dissolve
    "I ignored the ladies I passed in increasing numbers the closer I got to the building. If anyone asked I had an excuse at the ready-"
    UNKNOWN "Hotsure-san."
    MCT "Eep!"
    hide AE with dissolve
    show AE neutral at center with dissolve
    play music AE
    AE "What are you doing here?"
    "I had made it to the lobby of the women's dorm, mere feet from the elevator and relative safety."
    "Of course I would get stopped here."
    "Worse, I had the sales slip in my hand as I was double-checking the room number."
    menu:
        "Answer.":
            jump BBW015_c2_1
        "Hide the sales slip.":
            jump BBW015_c2_2

label BBW015_c2_1:
    "Folding the slip one-handed, I casually tucked it into my pocket while answering."
    MC "I was trying to find Mizutani-san. I had a manga I had borrowed from her, and I wanted to give it back."
    AE "And you couldn't wait until class?"
    MC "I suppose I could have, but I wanted to do it before I forgot."
    MC "I'm sure you can appreciate the importance of promptness."
    show AE neutral at Transform(xzoom=-1)
    AE "I do..."
    "Her eyes narrowed. I could feel beads of sweat start to appear at the top of my forehead."
    show AE neutral at Transform(xzoom=1)
    AE "Very well. Go return the book."
    AE "But don't dawdle. Access to the women's dorm is a privilege, not a right."
    MC "Yes, ma'am."
    stop music
    scene black with fade
    "After that brief scare the rest of the delivery went off without a hitch."
    "I found the right room, found Fukushi still there, and gave her the package."
    "Later..."
    scene Classroom with fade
    show BBW happy
    play music BBW
    $setAffection("BBW", 1)
    BBW "Excellent work!"
    BBW "Dependable and resourceful. Keisuke, you have the makings of a great Nikumaru delivery agent."
    "Alice seemed more impressed with my job than I felt I deserved, but it wasn't that odd for her to overreact."
    BBW "Be on standby for the next delivery. Business will start slow, but before you know it be flooded with orders."
    MCT "Just so long as they're not all a close call like this one..."
    jump daymenu

label BBW015_c2_2:
    "Before I said anything I needed to hide that sales slip."
    MC "Well..."
    "I folded the slip in two, and then again, and was just about to put the telltale paper into my pocket when Shiori noticed my fumbling."
    AE "What is that?"
    "Her tone made me shiver. It wasn't an idle question, something I could pass off as 'just a piece of paper.'"
    stop music
    $ timer_count = 2
    $ timer_jump = "BBW015_c2_2_menu2"
    show screen choicetimer
    menu:
        "EAT THE SLIP!":
            hide screen choicetimer
            jump BBW015_c3_1

label BBW015_c2_2_menu2:
    menu:
        "Lie.":
            jump BBW015_c3_2
        "Hand the note over.":
            jump BBW015_c3_3
        "EAT THE SLIP!":
            jump BBW015_c3_1

label BBW015_c3_1:
    "I did the first thing that came to mind."
    show AE surprised
    AE "Ah-"
    "I shoved the paper into my mouth and began chewing."
    "It was hard to chew at first, because the paper was folded twice over. I had to work up some spit to get it soft, first."
    show AE angry
    play music Tension
    AE "Hotsure-san..."
    MC "Yesh?"
    $setAffection("AE", -1)
    AE "Did... did you just destroy evidence in front of me? What was that?"
    "I forced myself to swallow. My throat ached as I struggled to get the wet mass of paper down."
    MC "Gasp!"
    MC "It was... nothing. It was private."
    show AE angry at Transform(xzoom=-1)
    AE "..."
    show AE angry at Transform(xzoom=1)
    MC "There was no mistaking her mood, but the exact thoughts running through her head were harder to figure."
    AE "You are in the women's dorm, with a 'private' note you clearly do not want others to see. Any chance you had of clearing your name of suspicion went down your gullet with the paper."
    AE "But since the note is gone, you no longer have any reason to be here, correct?"
    MC "I-"
    show AE neutral
    AE "Rhetorical question."
    AE "I'm afraid I must ask you to leave, and I will keep note of this."
    scene black with fade
    play music BBW
    "I turned around and left, not wanting to give her a chance to change her mind."
    "Alice was surprisingly chill about the news of my failure."
    scene Classroom with fade
    show BBW neutral
    BBW "This is not the desired outcome, Hotsure-san, but you did mitigate any potentially worse results."
    BBW "I compliment you on your unorthodox solution."
    show BBW happy
    BBW "You still have the package, yes?"
    MC "It's in my backpack."
    BBW "Then all is not lost. After classes today you can try again."
    show BBW neutral
    BBW "I don't know if Fukushi-san belongs to any teams or clubs, but I would suggest waiting until after the dinner hour."
    BBW "You are more likely to find her in her dorm then."
    scene black with fade
    "She wasn't wrong. After dinner I went back to the women's dorm and found Fukushi there."
    "The delivery was made, and I apologized for the less-than-prompt service."
    "Not the smoothest operation, but I avoided complete disaster."
    "Still, it was an instructive taste of what I could expect going forward."
    jump daymenu

label BBW015_c3_2:
    "I couldn't hide the slip, but I didn't have to just hand it over."
    play music AE
    MC "This is a private note, meant for one particular individual."
    AE "Which individual? Perhaps I can pass it on for you?"
    MC "Sorry, but that's private."
    AE "..."
    "I could sense she wanted to ask more questions. Maybe some sixth sense was telling her I was up to no good."
    "But as nosy as she was, there was no rule (as far as I knew) granting the student council search and seizure rights."
    "That is what I was gambling on, and sure enough..."
    AE "Very well. But keep your visit here brief."
    AE "I wouldn't to hear of any infractions on your behalf... understand?"
    MC "Yes, ma'am."
    scene black with fade
    stop music
    "I found Fukushi's room, with her still in it. I gave her the package, thanked her for using our service, and left."
    "Alice was more than pleased with how I handled myself."
    scene Classroom with fade
    show BBW happy
    play music BBW
    $setAffection("BBW", 1)
    BBW "Brilliantly done, Keisuke."
    "Maybe more pleased than was justified, but I wasn't going to complain. It felt good to have done a job well."
    show BBW neutral
    BBW "You will have to be more cautious going forward, though. Spending too much time at the women's dorm will draw attention."
    BBW "That's a problem to consider before our business grows too much. But we can deal with it tomorrow."
    show BBW happy
    BBW "In the meantime, you've earned yourself a snack."
    BBW "Go enjoy the rest of your day."
    "I hung around for a moment, wondering if she was going to give me a couple yen to get myself a treat."
    "But no. She just kept smiling, then jerked her head to dismiss me."
    jump daymenu

label BBW015_c3_3:
    "I couldn't think of a lie that Shiori wouldn't see right through, so I pulled the slip back out of my pocket and held it out."
    play music AE
    MC "Here."
    MC "It's a sales slip. I have a delivery to make for Alice..."
    AE "...Well, I'd like to commend you for your honesty. I'm glad you have the sense for basic decency."
    MC "O-oh?"
    show AE angry
    AE "Unfortunately, the fact that you went behind my back to do this makes that wholly irrelevant!"
    "Of course."
    stop music
    scene black with fade
    "I mostly tuned out Shiori's mini-tirade, already fearing what Alice was going to say."
    "At least Shiori could direct her anger elsewhere. Alice..."
    scene Hallway with fade
    show BBW angry at center with dissolve
    play music BBW
    BBW "Hotsure-san! Explain yourself!"
    MC "I got caught."
    BBW "You laid down and died! You didn't even try to avoid discovery."
    MC "I'm not a natural liar. I'm sorry."
    BBW "Who said anything about lying?"
    BBW "Don't you know how to massage the truth? When she asked what the slip was, you should have said 'It is a private matter between me and someone else.'"
    BBW "Being student council president does not entitle her to intrude on our private affairs."
    MC "It's still lying by omission, isn't it?"
    BBW "Grrrrrrr!"
    BBW "Do you even want this job?"
    "I thought about it for a few seconds, weighing the promise of spending money against the idea of getting in trouble."
    MC "I'm not sure."
    BBW "You think on it. And I'll be thinking of whether you deserve this opportunity."
    hide BBW with dissolve
    "She didn't so much as look in my direction for the rest of the day."
    jump daymenu

label BBW015_c1_2:
    scene Dorm Exterior with fade
    "It would mean taking more time, but this seemed like a good time for the less obvious path."
    "After all, everyone leaving the dorms was heading to the cafeteria, going out the front entrance. Nobody would notice me coming in from the back door and heading right for the stairs."
    "I took the stairs two at a time, double-checking the room number."
    "When I got to the third floor I peeked through the door. The coast looked clear."
    "It wasn't."
    show AE neutral at center with dissolve
    play music AE
    AE "Hotsure-san? What are you doing here?"
    "Her eyes flicked down to the mailing envelope. I had to think of something, quick."
    if getAffection("AE") >= 10:
        jump BBW015_test_pass
    if getAffection("AE") >= 4:
        jump BBW015_test_semipass
    jump BBW015_test_fail

label BBW015_test_pass:
    MC "There was a mailing mix-up. Somebody's order got sent to my room."
    MC "They must have put 'Men's dorm' on the address, not 'Women's.'"
    AE "A mailing mix-up?"
    "Shiori-san looked back at the envelope, but then back at me; her eyes showing confusion and possible disappointment. Closing her eyes and exhaling deeply, she looked back to me."
    AE "I understand. I'll have to rectify that from happening again. I... won't keep you."
    show AE happy
    AE "But be sure to be quick. You need to make sure to get breakfast before class."
    hide AE with dissolve
    stop music
    scene black with fade
    "I nodded and walked past her, only mildly guilty about lying like that."
    "Later, Alice complimented me about the job."
    scene Classroom with fade
    show BBW happy at center with dissolve
    play music BBW
    BBW "A satisfying first mission. And you even managed to give Matsumoto-san the slip."
    BBW "Well done. Just be sure to stay on your toes next time as well."
    "The quiet reservations I still had about this entire technically illicit affair were further quieted when Alice smiled at me and gave that encouraging note."
    "I knew this was strictly a business arrangement, but there was still something nice about having her approval."
    jump daymenu

label BBW015_test_semipass:
    MC "There was a mailing mix-up. Somebody's order got sent to my room."
    MC "They must have put 'Men's dorm' on the address, not 'Women's.'"
    AE "That makes no sense. There's not a single female student with the name 'Keisuke Hotsure'."
    MC "Y-yeah, well..."
    "Busted."
    "Shiori-san crossed her arms expectantly, showing deep frustration."
    show AE angry
    AE "Look, I'm willing to trust that you're doing as you say."
    show AE angry at Transform(xzoom=-1)
    AE "Do {i}not{/i} make that trust ill-founded."
    show AE neutral at Transform(xzoom=1)
    AE "Go ahead and take the item to the rightful owner. And then please leave."
    AE "The residents here need to prepare for the day, and I don't want your presence to be distracting."
    MC "Got it."
    stop music
    scene black with fade
    "I nodded and walked past her, not really feeling guilty about lying like that."
    "Later, Alice complimented me about the job."
    scene Classroom with fade
    show BBW happy at center with dissolve
    play music BBW
    BBW "A satisfying first mission. And you even managed to give Matsumoto-san the slip."
    BBW "Well done. Just be sure to stay on your toes next time as well."
    "The quiet reservations I still had about this entire technically illicit affair were further quieted when Alice smiled at me and gave that encouraging note."
    "Her approval was nice, but at the same time I had Shiori's disapproving expression stuck in the back of my mind."
    "I couldn't see a way to keep both ladies happy, but maybe there was a way to not let one down?"
    jump daymenu

label BBW015_test_fail:
    "I tried to think of a plausible lie, but Shiori's gaze was practically stabbing me. So intense, I almost wanted to confess right then and there."
    MC "I... was coming to return a manga I borrowed from Mizutani-san."
    AE "I see. And what is in that envelope?"
    MC "It's just..."
    "She held out a hand."
    AE "Let me see it."
    "I did as instructed. She pulled the panties out, an eyebrow arching as she realized what they were."
    "Fortunately I had the sales slip in my hand, and she didn't look at the label on the envelope. Either of those could have given up the game."
    show AE neutral-smug
    AE "Let me guess. Yours?"
    MC "Don't judge."
    show AE surprised
    AE "!"
    show AE embarrassed
    AE "O-Oh god, I..."
    MCT "Alice, you owe me."
    "She stared at me for a bit, then silently put the panties back in the envelope and handed it back."
    AE "Mizutani-san does not live on this floor. She's one floor down."
    AE "Return her manga and please leave the dorm. The ladies here need to get ready for the day."
    MC "Roger."
    stop music
    scene black with fade
    "I went to the staircase and went down one flight, but I stayed in the stairwell."
    "After a few minutes I went back up to the third and checked the hall again. Shiori was gone."
    "And I hadn't missed Fukushi. I made the delivery and got out of the building."
    "Alice was amused at my cover story, but she was more taken with my commitment to getting the job done."
    scene Classroom with fade
    show BBW happy at center with dissolve
    play music BBW
    $setAffection("BBW", 1)
    BBW "It's not the most airtight story you could have come up with, but you did good, Keisuke."
    MC "Yeah, I've already thought of how I could have handled that in a much less embarrassing way."
    MC "At least I can trust Matsumoto-san to be one of the most tight-lipped people here. Anyone else..."
    "I had a sudden flash of Honoka seeing me with a pair of women's underwear. My blood ran icy."
    BBW "Don't be too hard on yourself. Most others would have crumbled under her stare."
    BBW "Just be more careful next time. Better to not find yourself in that position at all."
    jump daymenu

label BBW015_c1_3:
    scene Nurse Office with fade
    play music Tension
    "It took all of five seconds to realize this was the wrong decision."
    "To avoid detection I had gone into the men's room, waited until it was empty, and then tried to crawl into the ventilation system."
    "Thus when I got stuck nobody was around to see me, or hear me."
    "Almost an hour passed, me half in and half out of the vent, before someone came in to pee. Another twenty minutes were gone before I pulled out."
    "I got banged up and scraped. My clothes took most of the damage, but I still had plenty of scratches to get treated."
    show AE angry at center with dissolve
    $setAffection("AE", -1)
    "And of course the student council president had heard of my little escapade. In trying to avoid running into her I had ended up alone in the nurse's office as she chewed me out."
    "As she chewed me out and I 'Uh-huh'd every now and then I thought to myself 'I have to learn how Daichi does this.'"
    hide AE with dissolve
    stop music
    "Surprisingly, things got a little better when Alice showed up."
    play music BBW
    show BBW neutral at center with dissolve
    BBW "Were you hurt too bad?"
    MC "I'll live."
    BBW "Good."
    show BBW angry with hpunch
    play sound Thud
    BBW "Idiot! What kind of stunt was that?"
    MC "I thought it would be the easiest way to avoid detection."
    show BBW neutral
    BBW "You might as well have climbed to the roof and rappelled down to her room."
    BBW "Do you still have the package?"
    MC "It's in my backpack still."
    BBW "Very well. When you are able you can still finish the job."
    BBW "This is not an auspicious start to your career, but I suppose I cannot fault you for your enthusiasm."
    BBW "Just learn to balance it with some common sense."
    jump daymenu

label BBW016:
    $setProgress("BBW", "BBW017")
    scene Dorm Interior with fade
    play music Hallway
    "Classes were done, my homework was done, and even though I had wandered around the school for over an hour, I hadn't found anything to do."
    "No one to talk to, nobody that needed help with anything. I was left to myself."
    "So I came back to the dorm. Daichi was out - fortunately - so I had a nice quiet room to relax in."
    "I had broken out my laptop and was refamiliarizing myself with Titans of Eververse when my phone buzzed."
    MC "?"
    "It wasn't a call, though. It was a text."
    "I couldn't remember the last time someone had ever texted me, much less the last time I had sent one."
    BBWCell "<Hello, Keisuke. This is Alice. How are you?>"
    "I spent a few seconds staring at the message, confused. What did she want? Why was she texting me?"
    "Then I realized she might not want anything. Didn't Americans text each other all the time?"
    "But was Alice the sort to make small talk just because? She usually had something on her mind."
    "And here I had gotten comfortable and was having fun with my game."
    menu:
        "Text back you're up to nothing special.":
            jump BBW016_c1_1
        "Text back asking if she wants something.":
            jump BBW016_c1_2
        "Text back you're in the middle of something and can't talk.":
            jump BBW016_c1_3

label BBW016_c1_1:
    Cell "<I'm good. Just having a quiet afternoon to myself.>"
    "I unpaused the game - good thing I was between fights - when I heard another beep from my phone."
    MCT "That was fast."
    MCT "Or direct, I should say. Fitting."
    BBWCell "<I am currently idle as well. Kodama-san is working on a new recipe for me to try, and at my insistence she is taking her time to make sure it is perfect.>"
    BBWCell "<Thus, I am waiting later than usual for my afternoon tea and as I have completed my homework and studies I am looking for something else to occupy my time.>"
    if getFlag("BBW_working"):
        "I wasn't sure how to feel that she was hoping I could keep her entertained, but this did imply she wasn't contacting me with a new delivery assignment."
        "Right?"
    else:
        "I wasn't sure how to feel that she was hoping I could keep her entertained."
    jump BBW016_c1_after

label BBW016_c1_2:
    Cell "<Was there something specific you wanted to talk to me about?>"
    "Her response was immediate."
    BBWCell "<No, no. This is just friendly small talk.>"
    BBWCell "<I find myself idle as I wait for Kodama-san to finish working on a new recipe.>"
    jump BBW016_c1_after

label BBW016_c1_after:
    if getFlag("BBW_working"):
        Cell "<Oh. I thought you had another delivery for me to make or something.>"
        "Again, she responded right away."
        "Looked like I wasn't going to make it to the next dungeon anytime soon..."
        BBWCell "<Again, no. Our company is still in its infancy, building a customer base and waiting for word of mouth and customer satisfaction to rise.>"
    BBWCell "<I am not interrupting anything, am I?>"
    menu:
        "Not really.":
            jump BBW016_c2_1
        "Well, actually...":
            jump BBW016_c1_3

label BBW016_c2_1:
    Cell "<Not really. I was just doing some level-grinding.>"
    "I turned my player character back around and headed back to the village."
    "When my phone beeped again I kept one hand on my mouse and used the other read her response."
    play music Schoolday
    BBWCell "<I am not familiar with that term. What does it mean?>"
    Cell "<Video game speak. I'm trying to make my character more powerful.>"
    BBWCell "<That explains my ignorance. I have never been one for frivolities such as that.>"
    Cell "<There's nothing wrong with video games.>"
    BBWCell "<Perhaps not, but there are always better uses of your time.>"
    Cell "<That's subjective. If I'm having fun, if it helps me relax, that's good enough for me.>"
    Cell "<I'm thinking of maybe joining the computer club. I hear they spend most of their time playing MMORPGs.>"
    BBWCell "<Tsk.-"
    "Yes, she actually wrote out 'Tsk' in a text."
    BBWCell "<Tsk. When there are other, more enriching art forms available to you, you choose to wallow in crude power fantasies.>"
    "I didn't want to get into an argument over the merits of video games, but when I saw a flaw in her argument I felt I had to press."
    Cell "<If you've never played video games, then you can't really criticize them, can you?>"
    "That bought me all of a couple seconds. Maybe I had stunned her."
    BBWCell "<I have seen what those games are like.>"
    BBWCell "<Either a cartoonish mascot jumping from one cliff to another, hopping onto creatures that get in his way.>"
    BBWCell "<Or an orgy of ultraviolence that allows the disturbed to play out their grotesque fantasies.>"
    "Now I was getting a little peeved."
    Cell "<I wouldn't have pegged you as a moral prude, Alice.>"
    Cell "<Not that I want to start an argument, but there are far more types of games than just platformers and shoot 'em ups.>"
    jump BBW016_c3

label BBW016_c3:
    menu:
        "Like fighting games." if not getFlag("BBW016_c3_1"):
            jump BBW016_c3_1
        "Like fighting games. (disabled)" if getFlag("BBW016_c3_1"):
            pass
        "Like dating sims." if not getFlag("BBW016_c3_2"):
            jump BBW016_c3_2
        "Like dating sims. (disabled)" if getFlag("BBW016_c3_2"):
            pass
        "Like simulator games.": #(opens up BBW018)
            jump BBW016_c3_3

label BBW016_c3_1:
    $setFlag("BBW016_c3_1")
    "I started to write 'Like fighting games,' before realizing I wasn't doing myself any favors with that."
    if getFlag("BBW016_c3_2"):
        BBWCell "<Such as...?>"
        "I gritted my teeth, trying to think of an example that would blow away her contempt in one move."
    jump BBW016_c3

label BBW016_c3_2:
    $setFlag("BBW016_c3_2")
    "I started to write 'Like dating sims,' and stopped right before I sent it off."
    "If she didn't know what dating sims are, I'd have to explain it. And if she did know, I'd have to explain why that was the genre I went to."
    "I didn't relish the thought of having to defend dating sims to a female classmate."
    if getFlag("BBW016_c3_1"):
        BBWCell "<Such as...?>"
        "I gritted my teeth, trying to think of an example that would blow away her contempt in one move."
    jump BBW016_c3

label BBW016_c3_3:
    $setFlag("BBW016_testpass")
    Cell "<Like simulator games.>"
    "Another pause of a couple seconds followed."
    BBWCell "<Explain. Please.>"
    Cell "<It's right there in the name. They're games that simulate something, like farming or flying an airplane.>"
    Cell "<A lot of them are simple by design, a way to unwind by doing something repetitive.>"
    "I started typing 'I'm not really into them,' but then inspiration hit."
    "My lips curling up in a smile, I deleted what I had typed and then wrote"
    Cell "<The more complex ones have you running a city or a business.>"
    "I hit send, and waited."
    "This time it took almost ten seconds for her to respond. I had enough time to enter the inn and save my game."
    BBWCell "<There are business video games?>"
    Cell "<Yep.>"
    Cell "<Though not like regular businesses where you create a product and sell it.>"
    Cell "<The bigger titles revolve around more exciting things like amusement parks or zoos.>"
    BBWCell "<How do they work?>"
    "Cue victory fanfare."
    $renpy.music.set_pause(True)
    play sound Victory
    pause 3
    $renpy.music.set_pause(False)
    Cell "<You're put in charge of a business that's starting out or is struggling, and your job is to make it profitable.>"
    Cell "<You create rides or buy animals, set ticket prices, add concession stands or whatever.>"
    "Another pause."
    BBWCell "<Do you have any of those types of games?>"
    Cell "<I don't, but I can find one or two.>"
    Cell "<Interested in trying them?>"
    BBWCell "<I suppose I owe it to myself to sample all forms of art, so that I may make a more discerning judgement.>"
    BBWCell "<It is more impressive to appreciate the interplay of light and shadow in a Raphael than to master some violent spectacle.>"
    BBWCell "<But you were right: I cannot judge unless I have experienced it for myself.>"
    Cell "<I'll look into finding some business management simulators.>"
    BBWCell "<Money is no object. I can reimburse you.>"
    BBWCell "<It looks like Kodama-san is ready to serve the dish, so I will take my leave.>"
    "I sent a final message - Enjoy - and put my phone down."
    "I was free to return to Titans of Eververse, but the thought of getting Alice into gaming, even if it was the 'Zoo Manager' variety I'm not interested in, lingered in my mind."
    "So I went to my usual PC gaming store page and started looking through the business management titles."
    jump daymenu

label BBW016_c1_3:
    Cell "<Well actually, I was in the middle of a dungeon crawl. Can I talk to you later?>"
    "This time she actually took a moment to respond."
    stop music
    $setAffection("BBW", -1)
    BBWCell "<Oh. Well I would not want to interrupt whatever childish game you're engaged in.>"
    BBWCell "<Your time is too precious to spend engaged in actual human interaction, I see.>"
    "And that was the last text she sent me."
    "For my part I tried to diplomatically explain I could talk later, but all I got was silence in return."
    "I had a pretty good feeling she wouldn't hide her irritation the next time we met. I just hoped she didn't carry it too long."
    jump daymenu

label BBW017:
    $setProgress("BBW", "BBW020")
    scene Cafeteria with fade
    "I was feeling peckish after class, so I went to the cafeteria looking for something a bit more filling than a candy bar."
    "A bowl of ice cream called out to me, but it did mean I had to stay in the cafeteria as I ate it."
    play music Tension
    "No sooner had I gotten comfortable than Alice huffed her way into the dining area."
    show BBW angry at center with dissolve
    "Her anger was almost palpable. Not in her expression so much as this aura emanating off her."
    "Not a hornet's nest I would want to smack, but the cafeteria was mostly empty and so she noticed me almost instantly."
    BBW "Hotsure-san! What do you know of this?"
    "She thrust a piece of paper at me. It was a list of some sort. I took it and read it over."
    MC "It looks like all the girls in our year."
    BBW "Ranked by preference."
    BBW "Some boy or boys have judged all the women in our class and ranked them according to order of attractiveness."
    MC "Is that what this is?"
    MCT "(That's pretty skeevy, but I can't say I'm surprised. Stuff like that happened at my old school, too.)"
    MCT "(I can see why she's upset. We're all here because of some physical abnormality, and now here's some jerk objectifying all the girls-)"
    BBW "Why am I number 13?"
    MC "Th-That's what you're angry about?"
    BBW "Of course."
    show BBW neutral
    BBW "I have no reason to fear being judged for my beauty, but I have not decided if placing me so low is malicious or ignorant."
    MC "Wait, how are you at 13? There's less than 10 girls in our class."
    BBW "By 'class' I mean 'year'."
    show BBW angry
    BBW "But that is not the worst part. Look at the top of the list."
    MC "Matsumoto... Shiori's number one?"
    BBW "Madame President herself is at the top of the rankings. I want you to explain that to me."
    MC "You think I had something to do with this? Because I didn't."
    show BBW neutral
    BBW "But you are a man, yes? You should have some insight into the thought process."
    BBW "Do you think Matsumoto-san is more attractive than me?"
    MCT "So I'm being put on the spot. Because I'm the one who was here? This is not the first time you've betrayed me, ice cream."
    menu:
        "Yes.":
            jump BBW017_c1
        "No.":
            jump BBW017_c2
        "Square the circle.":
            jump BBW017_c3

label BBW017_c1:
    MC "If you must ask... Yes."
    show BBW angry
    BBW "..."
    MC "It's all subjective, right?"
    $setAffection("BBW", -2)
    BBW "You're honest, at least."
    BBW "That will serve you well. Stupidity and deception are a terrible combination."
    hide BBW with dissolve
    "And that was her final word."
    jump daymenu

label BBW017_c2:
    if getAffection("BBW") >= getAffection("AE"):
        $setFlag("BBW017_testpass")
        MC "If you must ask... No."
        BBW "Go on..."
        MC "Go on? It's all subjective, isn't it?"
        BBW "Yes and no. Any culture has an established ideal of beauty. You're right to say I'm more attractive than Matsumoto-san, but this list indicates you're the exception."
        BBW "Why is that?"
        "I considered sweet-talking her, but something told me she wasn't going to have any of that."
        MC "Well, it might not be physical."
        MC "Personality-wise, you are kind of abrasive."
        "She didn't say anything for a moment, but I could see her thinking over what I just said."
        BBW "Let's say you're right (though I'm not admitting to being unduly proud). How does that explain Matsumoto's popularity?"
        BBW "She goes out of her way to push people away. It's as if she wants to be despised."
        MC "I think you might be overstating it, but you're not entirely wrong. She has the 'tsun' part of the tsundere type going for her."
        MC "It's a paradox. The more you can't have something, the more you want it."
        MC "And with someone like Matsumoto-san there's the fantasy that if you can pierce her icy exterior you can find the sweet center and she'll reciprocate your feelings."
        MC "You... You're seen more as a stuck-up rich girl. People aren't going to be interested in getting to know you if they think that's all there is."
        "She stayed silent a while, her irritated mood melting."
        play music Peaceful
        BBW "And do you think that's all I am? A stuck-up rich girl?"
        MC "I think there's more to you than your money. You have an interest in music, right?"
        show BBW haughty
        BBW "I am cultured, yes."
        MC "Right. Just don't be so elitist about it and you can probably find some other people with the same interest."
        show BBW neutral
        BBW "Elitist? Whatever do you mean?"
        MC "You were butting heads with the music club president after just a couple days, remember?"
        show BBW haughty
        BBW "Is it elitist to let others know when their standards are below acceptable?"
        MC "Yes! Yes, that's the very definition of 'elitist!'"
        show BBW angry
        BBW "!"
        "She looked like she was about to snap, but then quickly relaxed, exhaling slowly."
        show BBW neutral
        BBW "Boys like it when someone like Matsumoto-san orders them around, because they harbor this fantasy that they can win her over. But they don't like it when someone like me chastises them for their shortcomings."
        BBW "It's all about having this illusion of control, isn't it? Some people just can't accept not being in charge of everything."
        BBW "Boys like to play pretend, after all."
        MC "Not all guys are like that, you know."
        show BBW happy
        BBW "Oh, I know. I'm not lumping you in with the children who concocted this list."
        BBW "You are man enough to admit your own feelings, and reasonable in your tastes."
        show BBW neutral
        BBW "I'm not sure if you're mature enough to follow your own path, but we shall see..."
        show BBW happy
        BBW "Enjoy your ice cream."
        hide BBW with dissolve
        "She walked off in a much better mood than when she had shown up, but I didn't think it was so simple as her being complimented by my saying I found her more attractive than Shiori."
        "Something else was on her mind, but I didn't stop to consider what it might have been."
        "You can say she was right about me not being mature enough, if you want, but when the conversation was over my impulse was to get on with my life as if nothing had happened."
        jump daymenu
    else:
        MC "If you must ask... No."
        BBW "..."
        show BBW angry
        BBW "You're a terrible liar."
        MC "I- Wha?"
        show BBW neutral
        BBW "I've seen you and Matsumoto-san. You're rather close, the two of you."
        MC "No, we're... We're friendly, but it's not like we're dating."
        show BBW haughty
        BBW "I understand human behavior, Hotsure-san. It's a necessary trait for anyone looking to enter the jungle of free enterprise."
        BBW "You can't hide what you're feeling whenever you're chatting with the Ice Queen. Maybe she can't figure it out, maybe you're too timid to take the leap, but I know."
        show BBW angry
        BBW "So don't EVER try to sweet talk me like that again."
        MC "Okay. Okay. I guess I do find Shi- Matsumoto-san a bit more attractive than you. A bit."
        MC "But it's not like I would put you at 13 or anything that low."
        "Alice's expression softened a bit, her stony exterior melting into something a little less severe."
        show BBW neutral
        BBW "Of course you wouldn't. Nobody with sense would."
        show BBW angry
        BBW "But I still need to find whatever cretin made this list."
        show BBW neutral
        BBW "Hotsure-san."
        hide BBW with dissolve
        "And she walked off."
        jump daymenu

label BBW017_c3:
    MC "Well... it's all relative. Beauty is in the eye of the beholder and all that."
    MC "I mean, when you say 'attractive' are you talking about pure physical beauty, and do we then go off of classical standards of what a given culture considered ideal?"
    MC "For that matter, how do you compare two different objects that are both, in their own ways, beautiful? A landscape and a portrait differ in their subject matter, but they each have their own criteria for what is beautiful or not."
    show BBW angry
    MC "So while you have your own unique air and... gravitas, someone like Shiori has an equally distinct but undeniably different bearing. Who is to say which is 'right' or 'more attractive?'"
    "As I rambled I could see Alice's expression darkening. This wasn't working."
    $setAffection("BBW", -1)
    BBW "Stop. Just stop."
    MC "..."
    BBW "I don't know what's going on inside your head, but I have no tolerance for weakness."
    BBW "And however I may feel about Madame President, I don't think she's the sort to take pity on a wishy-washy... toad."
    BBW "Figure out what you want and grow the requisite spine to go after it. Playing the middle isn't going to get you anywhere."
    hide BBW with dissolve
    "And our conversation ended there."
    jump daymenu

label BBW018:
    scene Cafeteria with fade
    play music Busy
    "So Alice wanted to try a tycoon game, and since I was the one to suggest them to her it fell on me to hold her hand."
    "Not that I minded. I really had no experience with those games, but playing with someone else or just watching them could be fun in its own way."
    "And when I stopped to think about it, I was having trouble thinking of times I had seen Alice hanging out with anyone besides me. Or Kodama-san, of course."
    "I knew she was in the music club, but from what I'd heard she wasn't exactly endearing herself to anyone there."
    "Was I her only friend at the school? Nah, it couldn't be."
    "Either way, as brusque as she could be, I didn't mind the thought of getting closer to her."
    show BBW happy at center with dissolve
    show PRG neutral at Position (xpos=0.45, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    BBW "Ah, Keisuke. Over here."
    "I found Alice and Aida sitting at her usual table, but instead of tea and cakes there was a full computer set-up. Monitor, tower, keyboard, mouse."
    "And jeez, this wasn't cheap. I wasn't up on the latest gaming hardware, but it looked like a Hayashi ZX-5000. Fresh out of the box, even."
    MC "Is this new?"
    BBW "Indeed. It arrived just this morning."
    BBW "I don't know anything about video game hardware, but the reviews for this model were uniformly good."
    MC "You bought an entirely new computer just to play games?"
    show BBW neutral
    BBW "Well, yes. If I am to give this endeavor the best opportunity I need to have the finest equipment possible, wouldn't you agree?"
    hide PRG with dissolve
    MCT "Not really. Graphics and sound aren't as important as gameplay, and we aren't going to be looking at the latest AAA titles or anything."
    MC "Did you find any games you were interested in? I know the names of some of the more popular titles, though I'm not as familiar with them."
    BBW "I just finished our reading for Literature a few minutes ago, so I haven't had much chance to find anything yet."
    BBW "You have taken care of your homework, yes? I wouldn't want to impose on your time with something as frivolous as this."
    if getSkill("Academics") >= 4:
        MC "Huh? Oh, yeah. I've taken care of everything."
        show BBW happy
        BBW "Excellent."
        jump BBW018_c1_after
    else:
        MCT "Gah! The reading."
        MCT "I haven't even started it yet."
        menu:
            "Sure, I'm all caught up.":
                $setFlag("BBW018_c1_lie")
                MC "Yeah, I'm on top of everything."
                "A blatant lie, but Alice didn't even blink."
                show BBW happy
                BBW "Excellent."
                jump BBW018_c1_after
            "Actually...":
                jump BBW018_c1_2

label BBW018_c1_2:
    MC "No, I still have some stuff to take care of."
    BBW "Hmm."
    BBW "Well, business before pleasure. By which I mean your studies come before games."
    BBW "I will wait here while you go take care of your obligations first. There is still much I can do to familiarize myself with this machine."
    MC "OK..."
    $setAffection("BBW", -1)
    "She wasn't angry as she said that, but she was clearly disappointed."
    "She sounded almost like Shiori in that moment, though I guess with Alice it was less about adhering to the rules and more about striving for excellence or whatever."
    scene black with fade
    "I went back to my dorm and hit the books, double-checking my math homework and trying not to take any shortcuts with the reading."
    "It took almost two hours, but I finished it all and headed back to the cafeteria on the off-chance that Alice was still waiting for me."
    scene Cafeteria with fade
    show BBW neutral at Position (xpos=0.25)
    show PRG neutral at Position (xpos=0.75)
    "I expected her to have started a game already, figuring it out on her own, but nope. She was having tea, not even looking at her computer."
    show BBW happy
    BBW "Finished your work?"
    MC "Yep. All caught up now."
    BBW "Good. I would advise keeping on top going forward."
    jump BBW018_c1_after

label BBW018_c1_after:
    BBW "Have a seat."
    "I sat down next to her and she opened an online game store."
    show BBW neutral
    BBW "Now, what game would you recommend? I am a novice, but I am hoping for something engaging nonetheless."
    MC "Well, the most popular titles are..."
    $setVar("BBW018_gamesplayed", 0)
    menu:
        "Rollercoaster Tycoon":
            jump BBW018_c2_1
        "Railroad Tycoon":
            jump BBW018_c2_2
        "Professional Wrestler Tycoon":
            jump BBW018_c2_3

label BBW018_c2_menu:
    menu:
        "Rollercoaster Tycoon" if not getFlag("BBW018_rollercoaster"):
            jump BBW018_c2_1
        "Rollercoaster Tycoon (disabled)" if getFlag("BBW018_rollercoaster"):
            pass
        "Railroad Tycoon" if not getFlag("BBW018_railroad"):
            jump BBW018_c2_2
        "Railroad Tycoon (disabled)" if getFlag("BBW018_railroad"):
            pass
        "Professional Wrestler Tycoon" if not getFlag("BBW018_wrestler"):
            jump BBW018_c2_3
        "Professional Wrestler Tycoon (disabled)" if getFlag("BBW018_wrestler"):
            pass
        "Imperialis" if getVar("BBW018_gamesplayed") >= 2:
            jump BBW018_c2_4

label BBW018_c2_1:
    MC "It's kind of the standard for these types of games. You're put in charge of an amusement park and you need to make money by putting in rides and concessions, adjusting the ticket prices, stuff like that."
    BBW "Sounds straightforward enough, and running a business - even a simulacrum of one - is perfect for me."
    if not getFlag("BBW018_railroad"):
        "Even though there was an older version of the game discounted 75%% off, Alice went with the latest one."
        BBW "I want to experience the best possible version of the game."
        "Never mind that 'latest' didn't necessarily mean 'best.' But all right, Alice is new to gaming and I didn't feel up to opening that can of worms."
        "I was more bothered by the fact that even the latest version was two years old, and she was using a ZX-5000 to play it. So much processing power called up in service of so little."
        "The game started with a tutorial; how to place or destroy attractions, change ticket prices, read the interface."
        "It took almost 15 minutes, and I could see Alice losing interest. But finally it was done and she got to start her own game."
        "She played in silence for a while, getting the hang of the basics and, as far as I could tell, doing OK."
        "She was making money, expanding her operations and improving the existing ones."
    else:
        "So she bought the game, again going with the latest version, and sat through another tutorial."
        "Once she got into the game proper she seemed to do OK."
    "Her rollercoaster designs were kind of basic, but serviceable. And I think she was overcharging on the pictures you had taken on the rides."
    "Eventually, though, she started to look annoyed."
    "The monthly status report that gauge her park's finances, growth and expenses was on the screen, and something on it was irritating her."
    "She went through the drop-down menus and other screens, searching for something."
    show BBW angry
    BBW "Grrrr..."
    MC "What's up?"
    BBW "Look at that."
    "She pointed to the screen, the tip of her finger on 'Taxes.' It was a deduction taken out of her monthly earning based on how much her park was making."
    MC "What about it?"
    BBW "There's no way to contest this."
    BBW "It's completely unbelievable."
    MC "No... Businesses pay taxes."
    BBW "Not a flat rate like that."
    BBW "If this was real I would be able to make a deal with the local municipality for tax credits in exchange for the revenue my park would bring to the local economy."
    BBW "Hiring local labor to build and expand the park, the extra business people would bring to the surrounding restaurants and shops."
    BBW "I'm constructing a keystone of the local economy, and yet the city or state won't incentivize my work? It's absurd."
    MC "These games aren't supposed to be 100%% realistic."
    MC "I can see how a 'Lobby the mayor' side-mission would be kind of distracting."
    BBW "Whatever. I was losing interest in this game anyway."
    show BBW neutral
    BBW "It's too casual in how it depicts things like pricing and expanding the grounds."
    BBW "You can't even set wages for your workers, or handle advertising!"
    BBW "What other games are there?"
    $setFlag("BBW018_rollercoaster")
    $setVar("BBW018_gamesplayed", getVar("BBW018_gamesplayed") + 1)
    jump BBW018_c2_menu

label BBW018_c2_2:
    MC "Railroad Tycoon is a pretty well-known title. I've never played it, but it must have its fans."
    BBW "'Build your own railroad empire across Europe as you construct routes, upgrade your trains and handle both commercial and passenger business.'"
    BBW "So it's like operating a business, but more concerned with the ground-level operations instead of dealing with shareholders or building a brand."
    show BBW happy
    BBW "I can see how this would be fun."
    if not getFlag("BBW018_rollercoaster"):
        "Even though there was an older version of the game discounted 75%% off, Alice went with the latest one."
        show BBW neutral
        BBW "I want to experience the best possible version of the game."
        "Never mind that 'latest' didn't necessarily mean 'best.' But all right, Alice is new to gaming and I didn't feel up to opening that can of worms."
        "I was more bothered by the fact that even the latest version was two years old, and she was using a ZX-5000 to play it. So much processing power called up in service of so little."
        "The game started with a tutorial; how to place or destroy train tracks, change ticket prices, read the interface."
        "It took almost 15 minutes, and I could see Alice losing interest. But finally it was done and she got to start her own game."
        "She played in silence for a while, getting the hang of the basics and, as far as I could tell, doing OK."
        "She was making money, expanding her operations and improving the existing ones."
    else:
        "So she bought the game, again going with the latest version, and sat through another tutorial."
        "Once she got into the game proper she seemed to do OK."
    "She was more interested in commercial fare than catering to passengers, probably because that brought in more money."
    show BBW neutral
    "After a while, a bored expression crept onto her face."
    MC "Having fun?"
    BBW "No, I cannot say that I am."
    BBW "This isn't exactly the most realistic depiction of the railroad enterprise, is it?"
    MC "No, of course not. It's just a game."
    BBW "I understand that, but to have each country charge the same tax rate? To have the same cost of building and maintaining the tracks no matter where in Europe I go?"
    BBW "And how is it I cannot undercut my competitors when I clearly have the most advanced trains and access to the most routes?"
    MC "Uh, anti-monopoly policies?"
    BBW "I should then be able to lobby the various governments and secure special exemptions."
    BBW "For that matter, why aren't government contracts an option? There's so much revenue unaccounted for!"
    show BBW angry
    BBW "Argh!"
    "She closed her eyes. Inhaled, exhaled."
    show BBW neutral
    BBW "No, I don't think this game is for me."
    BBW "What else is there?"
    $setFlag("BBW018_railroad")
    $setVar("BBW018_gamesplayed", getVar("BBW018_gamesplayed") + 1)
    jump BBW018_c2_menu

label BBW018_c2_3:
    MC "This one is a little off-beat, but it falls under the 'business simulator' banner."
    BBW "Professional Wrestler Tycoon?"
    BBW "I know even less of pro-wrestling than I do video games. Why would I play this?"
    MC "Just give a try. Who knows, maybe you'll get into it."
    "Alice shrugged and bought the game. That it was full-price didn't seem to bother her (though I made a note to myself to point out she could get a refund if she didn't care for the game)."
    "The game downloaded and the instant she opened it the cafeteria was filled with a primal roar."
    show BBW neutral with hpunch
    play sound Crash
    Computer "<RWAAAARRRR!>"
    show BBW angry
    BBW "Ah!"
    show BBW angry with hpunch
    Computer "<DO YOU HAVE WHAT IT TAKES TO BUILD THE GREATEST WRESTLING FRANCHISE THE WORLD HAS EVER KNOWN?!>"
    "I lunged forward and hit the mute button on Alice's keyboard, then looked around the cafeteria."
    "The place was mostly empty, but everyone around had heard the full volume outburst. More than a couple heads turned in our direction, their expressions irritated at best."
    "Nobody was as upset as Alice, though."
    BBW "Oh! What was that assault? Is this game trying to punish you for playing it?"
    MC "It was surprisingly aggressive."
    "I turned the volume down to a reasonable amount, which for this game turned out to be 5 out of 100."
    MC "Still, might as well see how the game plays."
    "I could tell it was futile. From the moment she started the tutorial, directed by a wrestler called 'White Jaguar,' she was put off by everything."
    BBW "..."
    "That the game had almost nothing to do with actual wrestling and was instead built around managing a wrestling federation."
    "You started with a small roster of performers divided into heavyweights, cruiserweights and tag teams, and you made choices about which ones to push, which ones feed to other stars, and which to give championship belts to."
    "The objective was to build up stars that would bring in audiences, but not have them win all the time lest the fans get bored. Having a stable of villains the audience cared about was integral too."
    "So it was more like a resource management game with the twist that you needed both good and bad elements, faces and heels."
    "It wasn't the worst idea for a game, but the mechanics meant nothing to Alice."
    "The surface aesthetics were not doing it for her, and whatever enjoyment she would find in building a business was buried under her disinterest in the spandex-clad beefcakes going through exaggerated poses whenever you selected one."
    show BBW neutral
    BBW "I'm done with this. Surely there must be less off-putting displays than this."
    $setFlag("BBW018_wrestler")
    $setVar("BBW018_gamesplayed", getVar("BBW018_gamesplayed") + 1)
    jump BBW018_c2_menu

label BBW018_c2_4:
    MC "Maybe the regular business simulators aren't for you. They kind of are straightforward."
    MC "How about something like Imperialis? A 4X game might be more your thing."
    BBW "4X?"
    MC "Explore, expand, exploit and exterminate."
    MC "The goal is to build an empire and either conquer the world or achieve some sort of technological achievement before anyone else."
    BBW "An empire? Like ancient Rome or China?"
    MC "Yeah. There actually are games that use ancient civilizations-"
    show BBW happy
    BBW "And I'd be empress?"
    "As I said 'Yes' I could see her eyes taking on a dreamy expression, like she was losing herself to some beautiful vision."
    play sound Cheer
    BBW "Let's play that one!"
    show BBW neutral
    "She bought and downloaded the second-to-latest version of Imperialis, ignoring the space-based game that had come out last year, a giddy smile on her face."
    "It didn't even fade when she had to sit through yet another tutorial, the longest one by far."
    "I probably should have told her how much micromanaging there was in these sorts of games, but she wasn't bothered at all. She drank it all in."
    "When she started the game proper she selected the Roman-esque option, and was mildly put out that she couldn't change her avatar to a female. A fair criticism."
    "Other than that, she was clearly having a ball."
    "She didn't master it right away - there was just too much going on to get a feel for everything all at once."
    "But even when she started to get outclassed by the other empires, and when she engaged in an ill-fated war against one of her neighbors, she was still beaming."
    "It took almost six hours for her to get through her first game. For a while she had the lead, until another continent was discovered and three other empires joined the picture."
    "She ended up in second place after managing to conquer a neighbor, but the game ranked her performance right at the bottom of the charts. 'Andrew Johnson.'"
    "I'd have to look him up later to see just how dismal that was."
    "But Alice was unfazed, even if she knew who he was."
    show BBW happy
    BBW "I admit, Keisuke, I may have been wrong. That was a wonderful game."
    BBW "Obviously there is much room for improvement, so much to learn and master, but I am undaunted."
    BBW "If you have any tips, though, I'm open to them."
    MC "Actually, I don't really play these games."
    if getSkill("Academics") >= 4:
        MC "But I think I noticed a couple things you could have done better. You didn't have to restrict your defenses in each city like you did, for one."
        $setAffection("BBW", 1)
        BBW "Yes, I saw that. And maybe if I had stuck to one path with the technological developments..."
    else:
        MC "But it definitely was interesting. I think you're getting the knack for it."
    BBW "Would you be interested in meeting again over the weekend? I'm practically aching to start another game, but it's getting too late as it is."
    MC "Oh, wow, it's already eight o'clock."
    $setAffection("BBW", 1)
    MC "No, yeah. Let's do this again."
    MC "Do you need help taking your computer back to your room?"
    BBW "Oh, don't worry. Kodama-san will handle that."
    "I was hesitant to leave it for Aida until I saw she had a wheeled cart waiting by the side."
    scene black with fade
    if getFlag("BBW018_c1_lie"):
        "I hurried back to my dorm to take care of my homework."
        "I wasn't too concerned about Alice realizing I had lied to her, but making a habit of it wasn't going to lead to anything good."
        "It looked like I had a long night ahead of me."
    else:
        "So I said my goodbyes and headed back to my dorm."
        MCT "Maybe I could look up some Let's Plays for Imperialis, learn a few tips for Alice."
    jump daymenu

label BBW019:
    scene Dorm Interior with fade
    "It was afternoon and I was bored. I was so bored I can't think of any way more exciting than that to put it."
    "I didn't have any immediate homework to work on, just essays and projects due later in the term."
    "And none of my usual hobbies could even hold my attention long enough to not grab it. As soon as I thought of something to do I'd think 'Nah' and forget it."
    "But it was too nice a day outside to stay cooped up in my room. I could almost hear my parents getting on my case, that if I was so bored I should go out and find some entertainment of my own."

    scene Town with fade
    "I was kind of tired of the school grounds, so I walked to the nearby town. Still nothing caught my eye. It became more a question of, what was the least unexciting thing?"
    menu:
        "The arcade":
            jump BBW019_arcade
        "A cafe":
            jump BBW019_cafe
        "The movie theater":
            jump BBW019_theater

label BBW019_arcade:
    scene Arcade with fade
    play music Busy
    "The arcade was probably the best shot at ending my boredom. With all those bright lights and electronic chimes I at least couldn't zone out."
    "I got some change and walked around the floor once, seeing if maybe something caught my eye. When that failed, I went for one of the racing games."
    "Oddly, driving around in circles turned out to not be the key to shaking off my lethargy. I won a couple races, the changing scenery of each track more interesting than the races themselves, but after the difficulty stepped up I quickly lost."
    "I left to look for another game, and a pattern had been established. I would start a game, play a little, lose because my heart wasn't in it and move on."
    "After a few rounds of this I started thinking of going somewhere else, but then I ran into a familiar face."
    show BBW neutral at center with dissolve
    BBW "Oh, Keisuke. Good afternoon."
    MC "Afternoon. I didn't take you for a gamer, Alice."
    BBW "I'm not, really. I came to town to run some errands, and Kodama-san noticed a plush doll in one of those crane games."
    BBW "So I am waiting as she tries to win it."
    BBW "I cannot say I approve of how she is spending her money, but it is hers to spend."
    BBW "Do you spend much time at these sorts of places? Is she even likely to win, or is this a fool's errand?"
    MC "I actually don't come here all that often, but as I understand it those types of games aren't too easy to win."
    MC "Some people are skilled, though. Or maybe there's a trick."
    if getAffection("BBW") >= 4 and getFlag("BBW_working"):
        MC "Hey, you don't have any delivery jobs for me, do you?"
        $setAffection("BBW", 1)
        show BBW happy
        BBW "Not at the moment. Why so eager, though?"
    MC "I'm just here because I'm bored. Don't have any homework to worry about, got nothing else going on."
    show BBW neutral
    BBW "Hmm..."
    BBW "So with your free time you decided to while away an afternoon playing video games?"
    if getSkill("Athletics") >= 5:
        MC "You make it sound worse than it is."
        MC "I've done my homework, I did a good workout the other day, I've got no other obligations to take care of."
        MC "What's wrong with spending an afternoon playing games and having frivolous fun?"
        "Her expression, slightly judgmental, softened."
        BBW "You do have a point."
        BBW "I personally have little interest in games, particularly ones where you have to keep pumping money in just to play, but it is your time, your money."
        BBW "As long as your priorities are in order an afternoon or evening of, as you say, frivolous fun is defensible."
        BBW "Enjoy yourself, Keisuke."
        hide BBW with dissolve
        "And she wandered off, probably to find Aida."
        "For my part I spent another hour-plus playing different games, never truly getting into them but having enough fun I didn't feel the afternoon was a waste."
        jump daymenu
    else:
        MC "More like I just found myself here. Looking for something to do."
        BBW "'Looking' for something to do."
        BBW "{i}Sigh{/i}"
        BBW "You make it sound as if your only goal is to kill time, to speed through the prime of your life distracted and complacent."
        MC "What do you mean?"
        BBW "Your passive tone, my dear boy. You say you are looking for something to do, rather than going out and doing it."
        BBW "Life either happens to you or you make it happen, but it never comes to you. Understand?"
        MC "Ye-... No."
        "She closed her eyes and breathed in and out slowly."
        BBW "If there is something you want, be it mastering a skill or acquiring an object or achieving something, you must work for it. You have to make it happen."
        BBW "You can't sit back and just wait for it to drop in your lap."
        BBW "For instance, do you get any exercise outside of gym? Staying motionless in front of these flashing screens isn't good for your health in the long run."
        MC "I... Get in workouts now and then."
        "She closed her eyes again and shook her head."
        BBW "You don't sound too confident, Keisuke."
        BBW "Remember, habits you develop now can last a lifetime. If you don't take care of yourself today you can't just make up for it when you're 40 or 50."
        MC "I'm not that lazy."
        "She gave me a look that was one part 'Uh huh' and one part 'Really?'"
        "Then we heard Aida squealing with joy. Apparently she had gotten her plushie."
        BBW "Sounds like our business is done here."
        BBW "Keisuke, have a good afternoon. I hope you put it to good use."
        hide BBW with dissolve
        "She headed to the exit, and I was left to decide if I wanted to play some more games or do something a little more active."
        menu:
            "Keep playing games.":
                "Going back to the school, changing my clothes and hitting the gym sounded like too much work."
                "I found a fighting game to dump a few yen into, doing OK at first but never making it to the boss."
                "I was entertained, at least."
                jump daymenu
            "Hit the gym.":
                scene Gym with fade
                "I went back to my dorm and changed into some workout clothes. Faded shorts, an old shirt."
                "The gym wasn't too crowded, so I had my pick of the machines. Just like the arcade nothing really appealed to me, but going around the weight machines and jogging for half an hour on the treadmill was a better use of my time, I will admit."
                "I saw Akira at one of the other machines, pulling a monstrous amount of weight with her legs. But that area was seeing heavy use and crowds, so I didn't want to bother her."
                $setSkill("Athletics", 1)
                "When I left I felt mildly better. Not as listless, at any rate."
                jump daymenu

label BBW019_cafe:
    scene Cafe with fade
    play music Rain
    "I bought a coffee and a muffin and took a seat by the window, watching the townsfolk walking by."
    "I wondered how much they knew about the school. Surely they had to know about why it existed, but did they keep abreast of the school's operations, or did they avoid even thinking about it?"
    "I wasn't there long before in came Alice and Aida. The latter meekly waved when she saw me, but Alice was bolder, walking up to my table."
    show BBW happy at center with dissolve
    BBW "Keisuke. Are you meeting someone here? A date, perhaps?"
    MC "Wha-? N-no! No, I'm just having a coffee."
    BBW "Relax. I'm just saying 'Hi.'"
    show BBW neutral
    BBW "Aida and I were running errands and we stopped in for refreshments."
    BBW "But are you really just having coffee by yourself on an afternoon like this?"
    if getAffection("BBW") >= 4 and getFlag("BBW_working"):
        MC "Why? You don't have any delivery jobs for me, do you?"
        show BBW happy
        $setAffection("BBW", 1)
        BBW "Not at the moment. You sound eager for work though. Good to hear."
    MC "Well, I don't have anything else going on today. I came to town and found myself here. Drinking my coffee, watching the people go by, having a leisurely afternoon."
    show BBW neutral
    BBW "You don't even have a book with you? Nothing goes better with a cup of coffee than a good book."
    if getSkill("Academics") >= 5:
        MC "Didn't think to bring one with me. I've done plenty of studying lately, I can use a day without sticking my nose in a book."
        show BBW happy
        BBW "I can understand that."
        BBW "Sometimes you need to take a day off and give your brain a chance to rest up."
        if getFlag("BBW_working"):
            BBW "I won't interrupt your day off. But keep your phone handy. If a new order comes in I'll be messaging you."
        else:
            BBW "I won't interrupt your day off."
        hide BBW with dissolve
        "She went back to the counter, where Aida had already placed their order. When they got their drinks they walked out, and I was by myself again."
        "I took my time enjoying the coffee, even though it wasn't particularly great. After I was done I strolled around the town some more, then went back to the school to grab dinner from the cafeteria."
        "An unexciting day, but a restful one."
        jump daymenu
    else:
        MC "No. Wouldn't care to."
        MC "Honestly, the reading we've had to do for class has been kicking my butt. I needed a break."
        "I could see in her expression I had said something wrong."
        BBW "I see."
        BBW "I don't think the course load has been overly burdensome, but this may be subjective."
        BBW "Though I would think that if you are having trouble right now, so early in the term, that you would want to spend more time studying and developing better habits, not less."
        MC "Everyone deserves some time off now and then."
        "I sounded more defensive than I had intended. Alice's expression didn't change that much, but something in her eyes told me I had lost some standing in her mind."
        BBW "Hmm, yes. Leisure time is important, but I find it can be too easy to mistake the necessity of downtime for an entitlement."
        BBW "An important part of success is making sure you earn your downtime by driving yourself in your work."
        BBW "You don't stop running halfway through a race, you reach the finish line first."
        MC "Yeah, but if you get a cramp or something-"
        BBW "It means you should have done more work conditioning yourself beforehand. Preparation is another component of success."
        "She looked back to the counter, where Aida was holding two drinks and hanging back."
        BBW "But how you spend your time is up to you, Hotsure-san."
        hide BBW with dissolve
        "And she went back to Aida, and the two left the cafe."
        menu:
            "Stay at the cafe.":
                "I couldn't find fault in Alice's argument, but that didn't mean a fire had been lit under my seat."
                "I was already off campus, enjoying a change in scenery and general break from the school."
                "I could start studying regularly tomorrow."
                jump daymenu
            "Go back to the dorms and study.":
                MC "{i}Sigh{/i}"
                MC "She's right, of course. I didn't need her to point it out, but sometimes reinforcement of what you know helps make it clearer."
                MC "Or at least harder to ignore."
                "I finished my coffee and trudged back to the school, back to my dorm."
                scene Dorm Interior with fade
                "I had to push myself to ignore possible distractions like the internet or rereading my manga or (and this should tell you how susceptible I was) cleaning my half of the room."
                $setSkill("Academics", 1)
                "But I managed. I spent a couple hours going over the past week's history and literature lessons, refreshing what I already knew and getting a better handle on what had been giving me trouble."
                "Not what I would call an exciting afternoon, but a productive one."
                jump daymenu

label BBW019_theater:
    scene Theater Interior with fade
    play music Hallway
    "I found myself walking by the town's movie theater, looking over the posters."
    "There were a couple blockbuster-type movies showing, but also a historical drama, a romantic comedy and an indie melodrama."
    "I had enough money in my wallet that I could buy a movie ticket, and I could think of worse ways to while away a couple hours."
    "After I had decided to catch a flick, but before I had decided what to see, I heard someone call my name."
    UNKNOWN "Keisuke!"
    show BBW happy at center with dissolve
    MC "Alice. Good afternoon."
    BBW "Good afternoon."
    show PRG neutral at Position (xpos=0.75, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    MC "And Aida."
    PRG "H-Hello."
    hide PRG with dissolve
    BBW "Taking in a show?"
    MC "I was thinking about it."
    if getAffection("BBW") >= 4 and getFlag("BBW_working"):
        MC "Why? You don't have any delivery jobs for me, do you?"
        $setAffection("BBW", 1)
        BBW "Not at the moment. Why so eager, though?"
        MC "No particular reason."
    MC "None of these speak to me, but I've got nothing else going on right now."
    if getSkill("Art") >= 5:
        MC "I might check out this one. The Chrysanthemum Shadow."
        BBW "Ah. A fan of historical dramas?"
        MC "Not exactly, but it's supposed to have gotten good reviews. And the director's well-regarded."
        BBW "I've heard of Hagiwara, but I'm unfamiliar with his work."
        BBW "It's too bad I have other errands to attend to. This looks to be a promising film."
        BBW "Let me know how it is. I might go see it later."
        hide BBW with dissolve
        "She and Aida walked off, and I went to buy a ticket."
        scene black with fade
        pause 2
        scene Town with fade
        "The movie wasn't bad. A bit dry in the second half, and the battle scenes seemed almost perfunctory, but overall it was a solid flick."
        MCT "Need to remember to tell Alice about this one later."
        jump daymenu
    else:
        MC "I was thinking of seeing Iron Fan 5. The last couple ones weren't that great, but the original director is back so maybe this one is good?"
        "Alice looked the over the poster, with its white-suited gangsters, stern-faced police and bloodied asphalt in 'artistic' red, white and black."
        show BBW neutral
        "It wasn't hard to see she wasn't impressed."
        BBW "I wouldn't know how the movie is. I don't have much taste for crime stories."
        BBW "Particularly not ones as... lurid as this series' reputation suggests."
        MC "Nah, it's just silly, over-the-top violence. It's not even trying to be realistic."
        show BBW haughty
        BBW "That's not much of a distinction."
        show BBW neutral
        BBW "But it is your money, after all. Far be it from me to tell you how to spend it."
        "She turned and started to walk away, but then something caught her eye."
        BBW "Oh! The Chrysanthemum Shadow. I've heard good things about this."
        BBW "And Hagiwara-san is rather acclaimed, is he not?"
        MC "Who?"
        "She gave a brief but stinging look, then quietly suppressed a sigh."
        BBW "Never mind. Enjoy your popcorn flick."
        hide BBW with dissolve
        "As she walked off the quasi-dismissive tone in her voice gave me second thoughts."
        "I had only come here to find a way to kill the afternoon, but now I was thinking that Iron Fan might be a little too trashy."
        menu:
            "Iron Fan 5":
                scene black with fade
                "I decided to see Iron Fan."
                scene Town with fade
                "Yes, it was trashy. Yes, it just repeated a lot of stuff from the earlier movies."
                "But it let me shut my brain off for a couple hours, so it wasn't all bad."
                "Maybe not the best use of my free time, but I made my choice."
                jump daymenu
            "The Chrysanthemum Shadow":
                scene black with fade
                "I decided to see Chrysanthemum Shadow."
                scene Town with fade
                $setSkill("Art", 1)
                "It was actually pretty good."
                "The subject matter was a bit dry - too much talk about what might happen if the characters do this or don't do that - but I found the camerawork interesting. The director has an eye for balancing epic sweep with personal experience."
                "Yeah. A good movie."
                jump daymenu

label BBW020:
    $setProgress("BBW", "BBW021")
    play music BBW
    scene Cafeteria with fade
    "I had gotten to the cafeteria earlier than most of the other students, but after the rush had come and gone I was still there."
    "See, I'd brought a book with me to read while I ate, and it turned out to be more engrossing than I expected. 'I'll just finish this chapter,' I told myself, even after my plate was clean."
    "When I found a good place to stop I looked up to find most of the cafeteria empty. Just a few stragglers or members of sports teams coming off practice."
    UNKNOWN "Hotsure-san."
    "I was initially annoyed to have the quiet of the place broken, but when I realized who it was I relaxed a little."
    show BBW happy at center with dissolve
    BBW "Enjoying your dinner? Or it looks like you've already finished."
    MC "Yeah. I was just reading."
    BBW "That's good. Feed the mind as well as the body."
    "As Aida arrived, pushing a cart with a covered tray on top, Alice took the seat opposite me. She let Aida set her place for her, eager to see what she would be having."
    BBW "Stir-fried vegetables and beef, with mushroom soup. It looks delicious, Kodama-san."
    show PRG happy at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Th-Thank you."
    BBW "We should see about going into town this weekend, pick up some seasonal fruits. Summer will be here soon, and I do so enjoy watermelon and strawberries."
    "She was surprisingly happy, considering the recent issue with that list."
    MC "You're in a good mood. Did something happen?"
    BBW "My probation with the music club has come to an end."
    show BBW neutral
    BBW "I am still not satisfied with the club's guiding hand, but I recognize that further instigation will only take me further from my desires."
    BBW "So I will hold my tongue and restrict myself to the role given to me."
    BBW "It is to the club's detriment, but sometimes a flawed leader needs to be given the rope to hang themselves."
    MC "That's a bit heavy."
    MCT "Wrong choice of words, man."
    "But Alice didn't seem to care, she was already enjoying her meal."
    MC "Is that why you're having a late dinner? Club meeting?"
    show BBW happy
    BBW "That, and I found resolution to the... matter we were talking about the other day."
    MC "The list? Did you find out who it was?"
    show BBW neutral
    BBW "Found and confronted them."
    MC "What... What did you do?"
    "She shrugged, as if the entire matter was behind her."
    BBW "I didn't have to do much of anything. The child behind the list is even more pathetic than I expected."
    BBW "So pathetic I didn't have it in me to bring my full wrath down on him."
    BBW "I will simply say that his presence at this school is possibly more tragic than anyone else's. To tear him down more than he must already be would be cruel."
    show BBW angry
    BBW "However, he does understand - in no uncertain terms - that if he continues with this behavior I will identify him to every other woman on the list."
    BBW "Let those less forgiving than me punish him."
    MCT "Yikes. It says something if she thinks threatening to out someone is 'forgiving.'"
    MCT "Can't blame her for being angry, though."
    MC "Did he explain why he ranked you so low, or did you not ask?"
    show BBW neutral
    BBW "He said I am too 'plump' for his tastes."
    BBW "He specifically cited my belly fat, after I asked him about Matsumoto-san's 'plump' rear."
    BBW "I understand that certain body parts are more appealing to men than others, but this did confirm my assumption that this was a purely superficial exercise."
    BBW "Were I in Matsumoto-san's place I would be deeply offended if I was seen as a rear with a woman attached."
    MC "I'm not surprised it was about looks, but he didn't say anything about her 'strong' bearing?"
    BBW "By 'strong' do you mean 'stiff?'"
    BBW "No, he didn't say anything about personality. I got no sense he has looked past any of our bodies."
    MC "So he just doesn't like 'plump' women."
    menu:
        "His loss. Beauty can come in all sizes.":
            jump BBW020_c1
        "To each his own, I guess.":
            jump BBW020_c2

label BBW020_c1:
    $setFlag("BBW020_c1")
    MC "His loss. Beauty can come in all sizes."
    "Alice smiled wryly, almost rolling her eyes."
    BBW "That's a bit platitudinal for my tastes, Hotsure-san."
    BBW "And while I appreciate the gesture, I do not need the affirmation."
    MC "I'm just saying there is no single definition of attractiveness. Different people look good in different ways."
    BBW "That is all subjective. 'Beauty' is a label given by the observer, not claimed by the subject."
    BBW "Some men may find a stout woman pleasing to the eye and the touch, but it is a niche taste."
    MC "So you're worried about your weight. You think you won't look good anymore if you get fatter?"
    show BBW angry
    BBW "!"
    show BBW neutral
    BBW "{i}Sigh{/i}"
    BBW "I have already accepted my condition, and I'm prepared to deal with it if it becomes a genuine issue."
    BBW "Whatever fears may have been planted by my diagnosis will not be acknowledged. We don't deal with what might be wrong, but what can go wrong or is going wrong."
    BBW "I am not worried about my weight."
    "I didn't really believe her."
    "Maybe she wasn't concerned about her weight in a vacuous 'Oh no, I gained a couple kilos' sense, but there was something bothering her."
    BBW "Question."
    MC "Yes?"
    BBW "You said 'anymore.' That I 'won't look good anymore' if I get fat."
    MC "Yeah... You are pretty."
    show BBW haughty
    BBW "I know I am."
    MCT "That was fast."
    show BBW neutral
    BBW "But would I still be pretty if I was fat?"
    MC "You want to know if I like fat women?"
    BBW "I just want to know what your agenda is."
    show BBW haughty
    BBW "Obviously our current relationship as employer/employee would make dating problematic, but I am curious."
    "There was something confrontational about how she asked this. But also something... vulnerable? Like she was a little too eager."
    "I don't know why I felt like I had to hide anything here. Maybe it was just how Alice was so bold that I had to go in the opposite direction."
    MC "You said you are not bothered by your weight. So I take it that you're not looking for a compliment."
    show BBW neutral
    BBW "It's not about me. It's all about you, and your preferences."
    MC "Yes."
    MC "So speaking of what I like in general terms, with no comments about certain individuals, I will say that..."
    MC "I do, in fact, find something... enticing about larger women."
    BBW "Go on..."
    MC "Soft things are inviting. Pillows, sofas, plush jackets. They feel nice, they're relaxing."
    show BBW happy
    BBW "You want to lie down on a fat woman?"
    "I coughed, my mind going straight to the lewdest possible vision, and the way Alice chuckled after a beat I could tell she had surprised herself."
    BBW "That tells me more than you just said, actually."
    "It was more than I wanted to say, definitely."
    "But it was also more than I expected. I've never thought about being with a... a fat woman, but thinking about it now I could see the attraction."
    "I quickly got things back on track."
    MC "There are beautiful women who are larger than normal, to answer your original question."
    MC "As for physical desire..."
    show BBW neutral
    BBW "You do not need to paint any pictures."
    show BBW happy
    BBW "I could simply invoke the stereotype that men are never discerning about where they... Ahem..."
    MC "Hang the bird feeder in the garden?"
    show BBW neutral
    BBW "...What?"
    MC "I don't know. I couldn't think of a euphemism that didn't sound dirty."
    show BBW happy
    BBW "I think they're supposed to. Just not too dirty."
    "She ate the last bit of stir fry, daintily wiped her mouth, and pushed her chair back from the table."
    BBW "That was an excellent meal, and the conversation was... interesting."
    BBW "Hotsure-san, I'll leave you to your book."
    BBW "See you in class tomorrow."
    MC "Yeah. See you."
    hide BBW with dissolve
    "Even after she was gone and Aida had cleaned up the dishes and silverware, my thoughts kept coming back to Alice."
    "I had been invited to consider her body, so it's not like I was a pervert or anything. But now that the idea of being with a large woman was in my mind, I didn't find myself trying to get it out."
    jump daymenu

label BBW020_c2:
    MC "To each his own, I guess."
    "Alice chewed a mouthful of stir fry, thinking."
    show BBW neutral
    BBW "Overweight women aren't that common in Japan, in my experience."
    BBW "America is different. Too much bad junk food, restaurants giving bigger and bigger portions for better value."
    BBW "It's not that being overweight is seen as attractive, but it is unremarkable to see a heavyset man or woman in a relationship."
    MC "I suppose. I've never been outside the country."
    BBW "..."
    stop music
    "Something was on her mind, and I thought I knew what it was, but I didn't want to press things."
    "After the business with the list she must have been sensitive about her appearance, and I wasn't the one who could build her up without sounding like a bad self-help guru."
    "The longer the silence went on the more pressure I felt. Alice was eating, so she had an excuse not to say anything. And besides, it just felt like she was waiting for me to break through whatever wall was being set up."
    MC "Well... I should probably get back to my room. I've still got that history reading to do."
    "Alice nodded, not looking up at me, and I felt tense every step of the way out of the cafeteria."
    scene black with fade
    "Something was supposed to have happened there. I could feel it."
    "And I'd blown it."
    jump daymenu

label BBW021:
    scene Pool with fade
    "I had a creative writing assignment I needed to work on, and I just couldn't think of any ideas. Thus I found myself at the pool."
    "I had read somewhere that physical activity could get the mind working, get those creative juices flowing, so I thought I'd do a little exercising."
    "I came out of the men's locker room to find the pool rather empty."
    "I'd complain it was a waste to let such fancy facilities go unused, but it's not like I was coming here regularly. Who was I to talk?"
    "Among the students in or around the water two caught my eye."
    show BBW swimsuit-neutral at center with dissolve
    "Alice was climbing out of the pool, Aida ready to hand her a towel."
    MC "Hey, Alice."
    BBW "Keisuke."
    "She began drying herself off, and I knew I should just go and get started myself."
    "But at the same time our conversation about 'is big beautiful' had been on my mind since the other day."
    "I had been sneaking glances at Alice now and then, really taking in her figure."
    show BBW swimsuit-neutral at Position(xpos=0.5, ypos=0.0, yanchor=0.3), Transform(zoom=2.0)
    "And I'd come to the decision that there wasn't anything wrong with some extra curves."
    show BBW swimsuit-neutral at center, Transform(zoom=1.0)
    "Especially now, with the bathing suit clinging to her body, her hair wet (yet still keeping its spirals somehow). Stuff like that could make most any woman appealing."
    if getFlag("BBW020_c1"):
        jump BBW021_flagpass
    else:
        jump BBW021_fail2

label BBW021_flagpass:
    "But I hadn't really come out and said that, had I? What I thought about big women was left hanging."
    "This might be a good chance to be clear... Except bringing it up when she's in a bathing suit might make me seem perverted."
    menu:
        "Say something.":
            jump BBW021_beforechoice
        "Wait for a better opportunity.":
            jump BBW021_fail1


label BBW021_beforechoice:
    MC "Hey, you know the conversation we were having before?"
    BBW "?"
    BBW "Was this about the hours you could work making deliveries?"
    MC "No. It was about the list you found, and you had asked me how I felt about 'bigger' women?"
    MCT "Why did I say 'bigger' like it was a euphemism?"
    BBW "Oh, yes. That."
    MC "I just wanted to be clear. I do think bigger women are attractive, and not just in an 'I'll sleep with whoever' way."
    "Standing off to the side, Aida was turning bright red. I angled away from her and acted as if she wasn't there. This was potentially embarrassing for me as it was."
    MC "It's not like I have a type. Maybe more like a spectrum."
    $setAffection("BBW", 1)
    "She nodded agreeably."
    show BBW swimsuit-happy
    BBW "Most people do, I think. Though with such a focus on superficial trappings in our society many may not recognize it."
    if getAffection("BBW") <= 7:
        MC "True. But hey, that's one of the things we're supposed to get out of this school, right? Not being so focused on the superficial."
        show BBW swimsuit-neutral
        BBW "That's not quite what I was thinking. You are correct, but I was going for the fact that there's nothing wrong with having a type."
        BBW "So long as you do not develop myopia, blind to the other options around you."
        MC "Oh, right."
        MC "But like I said, bigger women are attractive. Not automatically more than skinny women, but not less so, definitely."
        show BBW swimsuit-happy
        BBW "I'm glad you got the chance to clear that up, Keisuke."
        BBW "I know you're not trying to soothe my wounded pride..."
        BBW "...but if you're explaining this as part of some larger scheme, I'm afraid I have to cut you off."
        BBW "The music club is meeting soon and I have to change."
        BBW "We can resume this conversation later. If there is anything more you want to say."
        hide BBW with dissolve
        "She said that last part as if there was deeper meaning to it. And no, she wasn't exactly wrong that there was more I would like to say."
        "But I was glad, all the same, that we had to cut this short, because I didn't think I would have been able to seize the moment right now."
        "Still, I felt energized as I dove into the pool and started doing my laps. Today was turning out to be a good day."
        $setProgress("BBW", "BBW022")
        jump daymenu
    else:
        BBW "And you did say I was pretty, of course."
        MC "W-Well, yes."
        "She looked at me like a cat with a bowl of cream just set down in front of it. I wasn't sure I knew what she was thinking until she spoke."
        show BBW swimsuit-aroused
        BBW "Keisuke..."
        MC "Yes?"
        BBW "What I am about to suggest violates every ethical rule about the relationship between an employer and her employee..."
        BBW "But that makes it even more appealing."
        MC "Um... Are you...?"
        BBW "How would you like to go out some time? Just you and me?"
        "I didn't think I had any right to be surprised she would be so forthright, and yet..."
        "It did feel like it had come out of nowhere. I guess Alice isn't the sort to play around."
        menu:
            "I'd love to.":
                $setFlag("BBW_dating")
                $lockRoute("BBW")
                MC "Sure. I'd love to, as long as it wouldn't make things weird over on the 'business' end."
                show BBW swimsuit-happy
                BBW "I don't think it has to. I am mature enough to separate my private life from my business ventures, and I trust that you can learn to do the same."
                MC "Um, OK."
                MCT "I was being a little tongue-in-cheek there..."
                MC "What do you have in mind? Dinner? A movie?"
                BBW "I will leave that up to you."
                BBW "I know that our options are limited here at the school, but I am interested in seeing how you express your romantic side."
                MC "Leave it to me, then."
                "She smiled warmly, and despite how fast everything was going I felt more elated by the thought of success than worried about failure."
                show BBW swimsuit-neutral
                BBW "I'm sorry, but I have to run. The music club is meeting soon."
                BBW "A demain."
                hide BBW with dissolve
                "She waved goodbye and went back to the women's locker room."
                "I almost went back to change myself, until I remembered why I had come there in the first place."
                $setProgress("BBW", "BBW026")
                jump daymenu
            "That's moving a bit fast.":
                $setFlag("BBW021_c2")
                MC "Sorry, but I think that's a bit fast."
                show BBW swimsuit-sad
                $setAffection("BBW", -1)
                BBW "Oh."
                MC "It's not that-"
                show BBW swimsuit-neutral
                BBW "No, I understand."
                BBW "This is a trying time in our lives, there are bigger things on our minds."
                MC "I'm not saying 'No' outright. Just... maybe later?"
                show BBW swimsuit-neutral at Position(xpos=0.8), Transform(xzoom=-1) with dissolve
                BBW "Hmm. Yes, perhaps."
                BBW "I have to go. The music club is meeting soon."
                BBW "I'll see you in class tomorrow."
                MC "Yeah. See you."
                hide BBW with dissolve
                "She went back to the women's locker room."
                "Not storming off, though. It was a plus that she didn't seem legitimately angry."
                "I'd have to be careful, but I thought I could keep things at least civil between us, if not friendly."
                $setProgress("BBW", "BBW022")
                jump daymenu
            "I... don't think that would work.":
                $setFlag("BBW021_c3")
                MC "I... don't think that would work out."
                MC "It's a bit fast. I mean, we're in unfamiliar territory with this school and everything else, and like you said I'm working for you-"
                show BBW swimsuit-angry with hpunch
                $setAffection("BBW", -5)
                BBW "I understand!"
                BBW "..."
                pause 1
                show BBW swimsuit-sad
                BBW "I do tend to be direct, don't I?"
                MC "That's not always a bad thing, but sometimes it can be overbearing."
                BBW "Yes, I know."
                show BBW swimsuit-neutral
                BBW "Forget I said anything, Hotsure-san."
                MC "No, it's-"
                show BBW swimsuit-neutral at Position(xpos=0.8), Transform(xzoom=-1) with dissolve
                BBW "I need to go. The music club is meeting soon and I have to get dressed."
                hide BBW with dissolve
                "She didn't storm off angrily, but it was obvious to anyone watching that she was hurrying to get out of there."
                "I watched her leave, then went into the pool and began to mechanically swim several laps."
                "Instead of thinking about the writing assignment, I was now trying to figure out how to patch things up with Alice."
                jump daymenu

label BBW021_fail1:
    MC "Well, I'm going to get some laps in. I'll see you two later."
    show BBW swimsuit-neutral
    BBW "Work hard, Keisuke, but don't overdo it."
    hide BBW with dissolve
    "I tried to banish the impression of squandering the opportunity by assuring myself I would be on the lookout for a more appropriate time and place."
    "Not that this the end of the world or anything. I just wanted to say that I found women like Alice potentially attractive."
    "It's not as if I'm trying to woo her or anything."
    "Right?"
    $setProgress("BBW", "BBW022")
    jump daymenu

label BBW021_fail2:
    MC "You know..."
    "She turned to look at me, and I felt a little tongue-tied."
    MCT "Just say she looks nice even at her size, don't make it sound perverted, and then move on."
    MC "I just wanted to say, after that whole 'list' thing and the guy saying he doesn't like plump women..."
    MC "Not all guys are turned off by a few extra weight. Some even prefer it."
    show BBW swimsuit-neutral
    BBW "Indeed."
    BBW "I know you wouldn't just be saying that to soothe my wounded pride."
    MC "No. It's the truth."
    MC "I've seen larger women I found attractive. Never dated one, but that was because of circumstances."
    BBW "It's all right, Keisuke. You don't have to try so hard."
    show BBW swimsuit-neutral at Position(xpos=0.65), Transform(xzoom=-1) with dissolve
    MC "I just want you to know... That guy doesn't speak for all men."
    BBW "I know."
    BBW "I just think that it is on each man to speak for himself."
    show BBW swimsuit-neutral at Position(xpos=0.8), Transform(xzoom=-1) with dissolve
    BBW "To say something more than just 'He doesn't speak for me.'"
    BBW "Now I have to run. The music club is meeting soon."
    BBW "So if there is anything else you would like to say to me about this, we can talk later."
    hide BBW with dissolve
    "And she went back to the locker room to change."
    "The way she sounded at the end, I had no doubt she wanted me to say more. And I know what she wanted me to say."
    "Maybe next time I could stop skirting around the issue. You never got anywhere by going halfway."
    $setProgress("BBW", "BBW022")
    jump daymenu

label BBW022:
    $setProgress("BBW", "BBW023")
    scene Dorm Interior with fade
    "I was back in my room relaxing after another day of studies when my phone buzzed."
    "It was Alice."
    BBWCell "<Can you come to my room? I need help with something.>"
    "I wasn't doing anything important right now, but I was leery that she was up to something of questionable permissibility."
    menu:
        "Text back 'Absolutely.'":
            "I texted back an emphatic 'Yes' and headed over."
        "Text back 'I can, but I can't spend the whole afternoon.'":
            $setAffection("BBW", 1)
            "I wrote back saying I still had homework and studying to take care of, but I could swing by and lend a hand."
        "Ehhhh, I don't want to deal with Alice right now.":
            jump BBW022_c1_3
    scene Dorm PRG with fade
    "Aida answered the door."
    show PRG neutral at center with dissolve
    PRG "H-Hello... Thank you for coming. Nikumaru-san needs help-"
    if getAffection("BBW") >= 8:
        BBW "Is that Keisuke?"
    else:
        BBW "Is that Hotsure-san?"
    MC "It's me. You needed help with something?"
    "Aida stepped back to let me into the room. This was first time I was seeing their living space."
    "Aida kept hers almost impossibly clean and neat. It looked like something you would see on a magazine cover."
    "It was hard to believe anyone actually lived here."
    MC "Whoa."
    "But then I saw Alice's half of the room."
    scene Dorm BBW with fade
    MC "None of this came from the school, did it?"
    show BBW happy at center with dissolve
    BBW "No. It's just a few odds and ends I brought from home."
    BBW "I like to be comfortable."
    MCT "This isn't comfort, this is a five-star hotel."
    MC "Why does your half of the room look bigger?"
    BBW "I know how to use space efficiently."
    BBW "Which brings us to why I called you here."
    BBW "I've gotten a bit tired of how my half of the room is decorated. It's time for a change."
    MC "It hasn't even been two months."
    show BBW neutral
    BBW "Yes. And?"
    BBW "I'm not a flighty fashionista, changing styles whenever something new comes along, but I do like to keep things fresh."
    MC "A stale environment leads to a stale mind?"
    BBW "'Familiarity breeds contempt,' is how I would put it. But the conclusion is the same."
    MC "Hey, it's your space. But I don't know much about interior decorating."
    show BBW happy
    BBW "Don't worry yourself about that. I've already planned out how I want to rejuvenate the space."
    show BBW neutral at Position(xpos=0.3) with dissolve
    show PRG neutral at Position(xpos=0.2) behind BBW with dissolve
    BBW "I need your help moving the furniture around. Kodama-san and I aren't strong enough to move the bed."
    MC "Oh. Well, all right."
    MC "Let me limber up here..."
    "I did a few stretches to get warmed up."
    MC "What are we moving first?"
    show BBW happy
    BBW "The bed is the centerpiece, so I want to adjust that first. Everything else will follow from there."
    if getSkill("Athletics") < 3:
        "I went to the head of the bed and bent my knees, while Alice and Aida went to the other side."
        MC "On three."
        MC "1... 2... 3-"
        "The plan was to rise and lift the bed in one fluid motion, but when the legs of the bed left the floor and I was now supporting its weight I felt a fire erupt in my back."
        MC "Ah!"
        "I let go of the bed, causing the ladies to drop their end, both crying out as well. Just not in pain."
        if getAffection("BBW") >= 8:
            show BBW sad
            BBW "Keisuke?"
        else:
            show BBW neutral
            BBW "Hotsure-san?"
        show PRG sad
        PRG "Ho-Hotsure-san?"
        scene black with fade
        "I hadn't thrown my back out, but I had pulled a muscle."
        "I couldn't move for a while, but by the time I was able to walk to the nurse's station I felt more embarrassed than in pain."
        "Alice sent me a text later that evening, making sure I was OK."
        "I played it off as no big deal, but I was sore for a couple days after that."
        "I found out later Alice paid one of the musclebound students to help move her furniture instead."
        "She didn't look at me any less after that, but I could feel I had lost a little standing in her eyes."
        jump daymenu
    else:
        "I went to the head of the bed and bent my knees, while Alice and Aida went to the other side."
        MC "On three."
        MC "1... 2... 3!"
        "We all stood up at the same time, lifting as we did."
        "As big as the bed was, it wasn't particularly heavy. I did have to bear more of the weight than they did, but it wasn't taxing or anything."
        "Alice directed us as we moved the bed, and with a little nudging this way and that we had it positioned just right."

        "After that it was considerably easier. The table, chairs, dresser and TV stand weren't nearly as heavy."
        "But since I was already there I got conscripted into doing most of the grunt work, moving everything heavier than a pillow and adjusting it to Alice's eyeballing whims."
        "She said she had everything planned out, but it ended up taking an hour to get everything just right."
        scene Dorm BBW Flip with fade
        "I couldn't tell you if the room looked better when it was done. It was fancier than anything I was used to, but I guess for Alice this was a step down from whatever mansion she had grown up in."
        "I was thinking of a way to politely excuse myself as Alice set out pictures and knick-knacks on her bookshelf, when suddenly I was blindsided by Aida."
        show PRG neutral at center with dissolve
        PRG "W-would you like a snack?"
        "She was holding up a plate of cheese and cracker concoctions, with... some sort of thinly sliced meat on top."
        MC "Uh, thank you."
        "I couldn't just up and leave now, so I took a closer look at the various affects Alice had around her side of the room."
        hide PRG with dissolve
        "The books on her shelf (a number of biographies, plus a few bodice-ripper romance novels)."
        "The dolls and trinkets (sort of standard 'girly' stuff)."
        "And pictures of her parents and what I took to be friends."
        MC "!"
        "One caught my eye. It was Alice and a man roughly our age, but they weren't standing next to each other as just friends."
        "Their bodies were turned toward each other, though they were looking at the camera, hands clasped and cheeks almost touching."
        "Way beyond familiar with each other."
        "And Alice looked genuinely happier than I could recall her being... ever."
        "(Though I had only known her for a few weeks...)"
        MC "Who's that?"
        show BBW happy at center with dissolve
        "She looked at the picture I was looking at, and her expression turned kind of dreamy."
        BBW "Oh. Forgot I still had that one."
        BBW "He's an old flame. Someone I knew back in Tokyo."
        "She took the picture out of the frame and slid it into a binder at the bottom of her bookshelf."
        "I wasn't surprised or intimidated to know Alice had dated before. We're not children."
        "But that guy in the photo was damningly handsome, and dressed so slick. He was probably rich and worldly too."
        "Did Alice still carry a torch for him?"
        MC "Are you guys... still friends?"
        show BBW neutral
        "She shrugged, her posture and expression poker face blank."
        show BBW happy
        BBW "We were closer once, but after graduating our paths went in different directions."
        show BBW neutral
        BBW "I wasn't interested in a long-distance relationship, and he has his own ambitions for university and beyond, so we called it quits."
        BBW "For now, at least."
        "For now..."
        "So Alice's affections aren't claimed, but I do have a... should I call him a rival?"
        MC "Do you still keep in touch?"
        BBW "A little. We have mutual friends, so we get cc'd emails now and then."
        BBW "But I haven't been too close with anyone from my old school since coming here."
        "I would be surprised if she hasn't told anyone about her condition."
        "I wonder how that other guy would react if he found out."
        "Maybe he's not actually a rival..."
        MC "Well, I need to get back and take care of my homework."
        MC "I'll see you in class tomorrow."
        BBW "Yes, thank you for your help."
        if getAffection("BBW") >= 8:
            show BBW happy
            BBW "Oh, you're perspiring. Here."
            "She handed me a handkerchief, silk with lace around the edges."
            "I almost felt bad wiping my sweat on it, but would it have been impolite to refuse it?"
            MC "Thank you. I'll return it after I wash it."
            "She smiled at me and thanked me again."
        scene Dorm Exterior with fade
        "As I walked back to my dorm I felt amped up."
        "I was simultaneously worried that Alice was still pining for her old boyfriend, while also cheering myself on with the fact that I was here and he wasn't."
        "Maybe there was a chance for me here, if I wanted it."
        jump daymenu

label BBW022_c1_3:
    "I wasn't really in the mood for whatever Alice has in mind right now. Probably some chore she wanted me to do for her, but hopefully not something violating the rules."
    "I texted back that I was in the middle of something, and could I take a rain check?"
    if getAffection("BBW") >= 8:
        $setAffection("BBW", -1)
    "Her response was quick, and kind of curt."
    BBWCell "<If you're busy, you're busy. I shall find someone else to assist me.>"
    "So I was off the hook, but part me wondered if she was going to take this personally..."
    jump daymenu

label BBW023:
    $setProgress("BBW", "BBW025")
    scene Classroom with fade
    show BBW neutral at center with dissolve
    show PRG neutral at Position(xpos=0.6, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    "After classes, Alice called Aida and I together for a business meeting."
    "She played it all straight-laced, going through a list of topics like an actual agenda."
    hide PRG with dissolve
    "The fact that there were only two employees, myself and her, didn't lead her to treat this any less properly."
    "She wasn't playing, and when she looked at me and said"
    BBW "Hotsure-san, could you please give a rundown of your work in deliveries?"
    "She looked as no-nonsense as a teacher calling on a student."
    MC "Uh... I didn't prepare anything."
    if getAffection("BBW") >= 7:
        BBW "I know, I'm dropping this on you out of the blue. This meeting itself was a last-minute change of plans."
    BBW "Just tell us how things have been going with the deliveries. You haven't had any issues, correct?"
    MC "No, no problems so far."
    MC "I do have to avoid Matsumoto-san when I'm carrying a package too big for my bag, I don't think the other members of the student council really care."
    BBW "The deliveries aren't interfering with your studies, are they?"
    MC "No. I've gotten in the groove."
    MC "Waiting until right before or after the dinner hour seems to be the key to catching the students in their dorms."
    BBW "Splendid."
    BBW "Business has been pretty stable across the board. I'm satisfied with our sales so far, they're within range of my projections when we started."
    BBW "But as word of mouth spreads the number of orders will increase, and you'll be working harder than before."
    MC "I think I can handle it."
    BBW "That's what I like to hear."
    BBW "On that note, next on our agenda is the coming sales period."
    BBW "This will cover the next month and a half, with our primary focus being summer clothing and accessories."
    BBW " The weather is warming up, so expect a rise in demand for tank tops, sundresses, and sunglasses."
    BBW "With an emphasis on style."
    BBW "My reconnaissance to the nearby town tells me that the students here won't be hurting for seasonal clothing in even the largest sizes."
    BBW "But so many of the larger-sized pieces sacrifice fashion for function, creating an opening for our enterprise to seize upon."
    BBW "Believe me, no woman at this school is going to keep potential body image issues at bay when they're dressed like a Quaker."
    MC "I don't get it... Quaker...?"
    BBW "Just... Be ready in a day or two to start pushing bikinis and sun hats."
    BBW "I'm working on a revised catalog with our summer line at the forefront, with only the most stylish or boldest designs on offer."
    if getSkill("Academics") >= 4:
        MC "Women want to feel beautiful. Even here."
        BBW "Especially here."
        MC "Yeah, I've noticed a lot of orders have been for things like bath salts and oils."
        MC "There's been some for make-up, but the... I guess you'd call them 'body works'?"
        MC "Those seem to be really popular."
        MC "Maybe we could have a sale for those as well."
        $setAffection("BBW", 1)
        show BBW happy
        BBW "That's an excellent observation, Keisuke. And not a bad suggestion."
    else:
        BBW "In addition, there has been a steady market in our health and beauty section."
        BBW "The more luxurious items like bath oils and perfumes have done especially well."
        BBW "I wasn't expecting there to be too much demand for such indulgences, but I believe that in times such as these people want to pamper themselves."
        BBW "It offsets the blow being here delivers."
    show BBW happy
    BBW "So I'm going to make plans for a sale on bath salts, perfume and assorted beauty products soon as well."
    show BBW neutral
    BBW "Kodama-san. Is there a dance or some form of soiree planned for next month?"
    show PRG neutral at Position(xpos=0.6, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Um... I don't know. I'll check."
    BBW "Thank you."
    hide PRG with dissolve
    show BBW happy
    BBW "Timing is everything in business. If we do this right we can net at least 2,500 yen above our current weekly sales."
    MC "That sounds smart."
    MC "I have seen some of our classmates... you know, getting close."
    MC "You almost wouldn't know there's anything 'off' about this place."
    BBW "People handle change in their own ways. Moving forward as if nothing is different is one way."
    MC "You mean ignoring bad news?"
    show BBW neutral
    BBW "Or accepting that which you can't change. It's a matter of perspective."
    BBW "Ending up here doesn't change the fact that we're young only once. Dating, partying, making mistakes we'll regret when we're older..."
    show BBW happy
    BBW "If you don't do it here, then when?"
    MC "True."
    if getFlag("BBW021_c3"):
        jump BBW023_fail
    elif getFlag("BBW021_c2"):
        menu:
            "I've been thinking about it myself lately. Dating.":
                jump BBW023_c1_1
            "I can understand why others would want to. It might not be for me, though.":
                jump BBW023_cx_2
    else:
        show BBW happy
        BBW "As busy as I've been with everything else - my studies, the music club, starting this enterprise - I've been thinking about my own social life."
        BBW "Not all interaction has to be about networking. My father has always taught me about the value of personal time."
        MC "He's right. A social life is kind of necessary. Part of the human experience and all."
        "She looked me in the eyes, and I could guess what was about to come."
        BBW "Are you talking about hanging out with your classmates, or have you thought about more intimate possibilities?"
        MCT "She's not asking out of idle curiosity. Better tread lightly."
        menu:
            "If the right girl came along.":
                jump BBW023_c2_1
            "That's a bit more serious than I've thought about.":
                jump BBW023_cx_2

label BBW023_fail:
    "She looked back at her agenda, then declared"
    show BBW neutral
    BBW "I think that covers everything for today."
    BBW "We might have another meeting next week, but only if there's anything of importance to discuss."
    BBW "If not, just keep up the good work."
    MC "Thanks. I will."
    scene Dorm Exterior with fade
    "With the meeting adjourned I went back to my dorm to take care of my homework."
    "Just another day. Nothing significant happening."
    jump daymenu

label BBW023_c1_1:
    show BBW happy
    BBW "Oh?"
    MC "Yeah. I mean, you're right. This is the only youth we get."
    MC "And not to be callous, but my condition is pretty easy to deal with."
    MC "I can sympathize with those who have something more extreme, but that's no reason I can't make the best of my time here."
    BBW "Exactly."
    show BBW aroused
    BBW "Has anyone in particular caught your eye?"
    "It was impossible to miss what was going on in her mind, the way she was practically batting her eyes, and how she brushed her hair behind her ear."
    "But my tongue chose this moment to get tongue-tied."
    "All I could think to say was"
    MC "There are one or two girls in our class. And around the school."
    "I started blushing like I was 13. She could see what I was thinking, and that just made me nervous."
    MC "I just want to be sure they're interested, first."
    $setAffection("BBW", 1)
    "It looked like she was holding back a chuckle, but there wasn't anything malicious in her expression."
    "She was probably just bemused. Maybe she was used to being around more decisive people."
    show BBW happy
    BBW "Well, the only real way to be sure they're interested is to ask them, yes?"
    MC "Right. Yeah."
    MC "Just a matter of finding the opportunity."
    BBW "Or creating the opportunity. You can't just wait for things to fall in your lap."
    MC "I guess not."
    "She looked back at her agenda, then declared"
    BBW "I think that covers everything for today."
    BBW "We might have another meeting next week, but only if there's anything of importance to discuss."
    BBW "If not, just keep up the good work."
    MC "Thanks. I will."
    scene Dorm Exterior with fade
    "With the meeting adjourned I went back to my dorm to take care of my homework."
    "But I couldn't stop thinking of Alice, how close I came to asking her out."
    "She was waiting for me to, that much was obvious."
    "But the moment didn't seem right."
    "And now that I was alone, I started thinking about how little we had in common."
    "She's rich and worldly, I'm... not."
    "But going down that rabbit hole would only make me more miserable. If she's interested, what did I have to lose?"
    "Who knows? This could turn out to be something real, whatever our differences."
    "I ended up forgetting about my homework until the next morning, when I did it all in a frantic rush."
    jump daymenu

label BBW023_c2_1:
    MC "I don't want to say 'No' outright, but I've never been the sort to see dating as something to do just for the sake of doing it."
    MC "Maybe I'm kind of square like that, or you could say I'm more discerning."
    show BBW neutral
    BBW "No, that's understandable."
    BBW "If you don't know what you're looking for, you're unlikely to find it."
    BBW "Rushing in blind is more likely to waste a lot of energy than anything."
    BBW "I just hope you don't miss the 'right woman' when she comes along."
    "She looked back at her agenda, then declared"
    BBW "I think that covers everything for today."
    BBW "We might have another meeting next week, but only if there's anything of importance to discuss."
    BBW "If not, just keep up the good work."
    MC "Thanks. I will."
    scene Dorm Exterior with fade
    "With the meeting adjourned I went back to my dorm to take care of my homework."
    "But I was distracted with Alice's rather heavy-handed hinting."
    "Whether she was the 'right girl' or not I couldn't say, but I could see that I was at a fork in the road, and I had to make a decision one way or the other soon."
    "Maybe asking her out would turn out to be a good thing. We might have more in common than I know."
    "Or if I'm this undecided I should just back off, and let her know. She didn't deserve to be left hanging, did she?"
    "Either way, this would have to wait to be settled for another day."
    jump daymenu

label BBW023_cx_2:
    MC "I guess I would say 'Not right now.'"
    MC "I've got plenty on my plate, what with school and this job."
    MC "Once I find my groove, in a month or two, I might have a different answer."
    show BBW neutral
    BBW "I suppose I can understand that."
    BBW "Dating isn't like a passive hobby. If your heart isn't in it, you're better off not doing it."
    MC "It wouldn't be fair to the other person, you know?"
    MC "What if they're more invested in it but I'm just 'Whatever'?"
    BBW "No, I know."
    "She looked back at her agenda, then declared"
    BBW "I think that covers everything for today."
    BBW "We might have another meeting next week, but only if there's anything of importance to discuss."
    BBW "If not, just keep up the good work."
    MC "Thanks. I will."
    scene Dorm Exterior with fade
    "With the meeting adjourned I went back to my dorm to take care of my homework."
    "I hoped she got the message. She's intelligent enough."
    "I just didn't want to come out and say 'I'm not interested in you like that.'"
    "Maybe she could handle it, but no reason to risk being too harsh."
    jump daymenu

label BBW024:
    scene Hallway with fade
    "My turn to clean the classroom had come up again, so I ended up walking through empty halls alone."
    "I thought about going back to my dorm, but I wasn't really 'feeling' it."
    "Maybe if I took the long way around I would find something more interesting than those now familiar four walls."
    show BBW angry at center with dissolve
    MC "Oh, Alice. Good afternoon."
    MC "Something bothering you?"
    BBW "No. Just a minor perturbance."
    MCT "You look a little upset for something you say is minor."
    MC "So what's up?"
    BBW "The library board is having a meeting, so the place is closed for the afternoon."
    MC "Looking for a book?"
    BBW "No, I need a quiet place to meditate."
    MC "Huh. Wouldn't have figured you for that sort of thing."
    show BBW neutral
    BBW "It's quite common among CEOs. Running a business demands a lot, and it's important to, as a former classmate called it, defrag your mental hard drive regularly."
    MC "Do you always do it in the library?"
    BBW "Yes. Not so much because of the quiet - I have noise-canceling headphones for when I use my mindfulness app - but because I want someplace where I don't have to worry about people intruding on my space."
    BBW "It can get distracting to have people walking back and forth, the more obnoxious ones asking me what I'm doing."
    "Then she added, under her breath:"
    BBW "(That I would have my plans upset on today of all days...)"
    menu:
        "What's special about today?": # (If affection < 5, +1)
            jump BBW024_c1_1
        "Recommend a place to meditate.":
            MC "There have to be other places where you can find solitude."
            jump BBW024_c1_2

label BBW024_c1_1:
    MC "What's special about today?"
    if getAffection("BBW") < 5:
        $setAffection("BBW", 1)
    BBW "It's not 'special.' Not in a positive sense."
    BBW "I have a dental appointment coming up this weekend. Those are never pleasant, so I'm on edge."
    BBW "That I would have this trouble now, when I need serenity..."
    MC "There have to be other places where you can find solitude."
    jump BBW024_c1_2

label BBW024_c1_2:
    menu:
        "How about the gardens?": # (+1 affection)
            jump BBW024_c2_1
        "How about the rooftop?":
            jump BBW024_c2_2
        "What about your dorm? (disabled)" if getSkill("Academics") >= 4 or getFlag("BBW024_c2_3"):
            pass
        "What about your dorm?" if getSkill("Academics") < 4 and not getFlag("BBW024_c2_3"):
            jump BBW024_c2_3

label BBW024_c2_1:
    MC "How about the gardens?"
    "She thought about that for a second."
    show BBW neutral
    BBW "Is there a lot of foot traffic there? I've never been to that part of the school."
    if getAffection("GTS") <= 5:
        MC "I don't think so."
    else:
        MC "No. It's an isolated island in the school."
    BBW "That sounds perfect."
    scene School Planter with fade
    "I had to help her find her way to the gardens. Sure enough, the place was empty at first glance."
    "Alice found a seat under a shady tree and put her headphones on."
    "When she closed her eyes I was torn between hanging around until she was done or leaving her. I decided it would seem rude if she finished, opened her eyes and found me gone."
    "Not that I knew how long she would take..."
    "I occupied myself by looking at the flowers. This place really was quiet."
    "At one point I saw Naomi walk by."
    show GTS neutral at center with dissolve
    "I waved, but when she saw Alice she seemed to stiffen."
    "She nodded slightly, then continued on."
    hide GTS with dissolve
    "After ten minutes Alice opened her eyes and took her headphones off."
    show BBW happy at center with dissolve
    MC "Feel better?"
    BBW "Calmer, yes."
    $setAffection("BBW", 1)
    BBW "This place was a good suggestion."
    "She looked at her watch and tsk'd."
    show BBW neutral
    BBW "Tsk."
    BBW "No time to savor the feeling, though. I have too much else to do."
    show BBW happy
    BBW "Keisuke. I'll see you in class."
    hide BBW with dissolve
    "And she was off."
    "Me, I didn't have anywhere to be. Back to my original problem."
    jump daymenu

label BBW024_c2_2:
    MC "How about the rooftop?"
    show BBW neutral
    BBW "The roof? Are we allowed up there?"
    MC "We're not not allowed, I don't think."
    scene Roof with fade
    "I led her to the roof, Alice grumbling about the stairs after the second story."
    show BBW neutral at center with dissolve
    BBW "Such an inconvenient place."
    MC "Sure to be secluded, right?"
    BBW "You're not wrong."
    BBW "Let me find a place to get comfortable."
    hide BBW with dissolve
    "It would have felt odd to just leave her there on the roof, so I hung back and let her get on with it."
    "Unfortunately the place turned out to not be as empty as I was expecting."
    show BE happy at center with dissolve
    BE "Hey, Keisuke, what's up?"
    MC "Alice is here to meditate. This seemed the most quiet place."
    show BE neutral
    BE "Ooooh?"
    BE "Wouldn't have taken her for the spiritual sort."
    MC "I think she just likes to clear her head."
    show BE happy at Position(xpos=0.8), Transform(xzoom=-1) with dissolve
    "As I was talking Honoka walked up to Alice."
    "Not right in her face. She hung back a bit. But it was close enough to disturb Alice."
    show BE happy at Position(xpos=0.65), Transform(xzoom=-1) with dissolve
    show BBW angry at Position (xpos=0.8, xanchor=0.5, yalign=1.0) behind BE with dissolve
    BBW "..."
    "She opened one eye, frowning."
    if getAffection("BBW") >= 8:
        MC "Here, why don't we give her some space?"
        "I went up and pulled Honoka back, but she resisted."
        show BE angry
        BE "Leggo!"
    BBW "Do you mind?"
    "She slipped her headphones down, clearly irritated."
    show BE neutral
    BE "Why are you meditating?"
    show BBW neutral
    BBW "To calm my mind. To find my center."
    show BE angry
    BE "...Sounds boring."
    BE "I could never sit still for so long."
    BBW "Actually, you could do just five minutes a day and derive some benefit from it."
    show BE neutral
    BE "No, still too long."
    show BE happy at Position(xpos=0.65, yalign=1.0), Transform(xzoom=1)
    BE "Hey, Keisuke. Race you to the vending machine! Loser buys!"
    hide BE with dissolve
    show BBW angry
    "And then she was racing to the stairwell before I could even respond."
    "I looked back at Alice, still annoyed."
    MC "She... gets like that."
    MC "Actually, I probably should have expected to find her here. She comes up here now and then."
    show BBW angry at center with dissolve
    BBW "So I see."
    show BBW neutral
    BBW "Well, the place is quiet now."
    BBW "I don't have much time to spare, but maybe I can still salvage a moment's peace."
    MC "Yeah, I'll... I'll go make sure she doesn't fall down the stairs."
    "It didn't seem like she was angry at me personally, but even still, I could read her mood."
    "I quietly retreated, giving her solitude."
    jump daymenu

label BBW024_c2_3:
    MC "How about your dorm?"
    "She gave me a look that mixed irritation with exasperation and pity."
    show BBW angry
    BBW "Tsk."
    $setAffection("BBW", -1)
    BBW "That was my first choice, but Kodama-san has trouble sitting still when she studies."
    BBW "She paces around. It gets distracting."
    MC "Oh... Yeah, I guess there's a reason you're not there already."
    jump BBW024_c1_2

label BBW025:
    $setProgress("BBW", "BBW026")
    scene Cafeteria with fade
    "The music club had a meeting today, which meant Alice was having her dinner later than usual."
    "I had to pass along a delivery payment to her... which was the reason I gave myself for waiting to get my own dinner until later, too."
    "I could have rushed to meet her before the meeting started, get in and out of the music room, but..."
    "Anyway, I found her at her usual table."
    "I wouldn't say this out loud, but it was hard to miss her."
    show BBW neutral at Position(xpos=0.8, xanchor=0.5, yalign=1.0) with dissolve
    "I had noticed it in class this morning. She was eating a bag of potato chips before the lecture started."
    "She had been gaining steadily, but I'd noticed an ever so slight increase in appetite on top of this."
    "It didn't seem to bother her. She had been most pleasant all day, and right now she looked to be enjoying her dinner."
    "Maybe-"
    pause 1
    show BBW happy at center with dissolve
    BBW "Ah! Keisuke! Good evening."
    MC "Good evening."
    MC "I just wanted to make a quick drop-off. Yamaguchi-san apologizes for the late payment."
    BBW "Oh. Thanks."
    BBW "I appreciate your promptness."
    MC "I'll leave you to your meal."
    BBW "Oh, you don't have to rush off. Have a seat."
    BBW "Aida made a bit too much flatbread. Help yourself."
    MC "Thank you."
    MCT "It does look like there's more food than usual. Is her appetite truly growing with her body?"
    "I meant to sneak a quick peek at Alice's belly, round enough that it filled most of her lap when she sat down."
    show BBW neutral at Position(xpos=0.5, ypos=0.0, yanchor=0.3), Transform(zoom=2.0)
    "I must have been staring, because when I looked up I found her watching me."
    show BBW neutral at center, Transform(zoom=1.0)
    MCT "Crap. Say something before she does."
    MC "I hope I'm not overstepping any boundaries, but I like how you're carrying your weight."
    "It sounded a bit more suave in my head, and when she didn't respond at first I was worried she had taken it the wrong way."
    "But then she fluttered her eyes and laughed."
    BBW "That is rather bold, Keisuke. But I like your directness."
    BBW "And thank you, by the way."
    BBW "I believe I've said before one of the side goals of my business is to help our classmates weather these changes."
    BBW "My own continued self-assurance is integral to that. I am the face of the company, after all."
    BBW "Still, it is good to know that others have picked up on that."
    MC "Judging by how the perfumes and cosmetics are selling, I'm not sure if the other ladies are trying to cover up their own growth or if they're like you."
    MC "Determined to keep their chin up regardless of what life is throwing at them."
    BBW "I think it's more the latter."
    BBW "There were a lot of people, men and women, initially despondent when the term started."
    BBW "But the general mood of this place has risen. Most people are more confident, or at least lighter of spirit."
    MC "It is the season for romance, after all."
    BBW "A little late. We're almost in summer."
    BBW "But still, the perfect time to be out enjoying the fresh air and sunshine. Which is always nicer with someone close to you."
    MCT "Can't misread that sign..."
    menu:
        "You're not interested in dating her.":
            jump BBW025_c1_1
        "Ask her out.":
            jump BBW025_c1_2

label BBW025_c1_1:
    MC "Or just having fun with friends."
    MC "Like you, Alice. You're a good friend."
    pause .25
    show BBW neutral
    pause .25
    show BBW angry
    $setAffection("BBW", -10)
    BBW "..."
    MCT "Uh-oh..."
    show BBW neutral
    BBW "{i}Sigh{/i}"
    BBW "Thank you, Hotsure-san. I consider you a friend, too."
    "Her tone was remarkably even, her face stone-like, but there was hellfire in her eyes."
    "Maybe spending so much time with her lately has put me in tune with her emotions..."
    "Or maybe she's just really easy to read."
    "Either way, I knew how to read a room. Looking at my phone, I said"
    MC "Oh, shoot. My mom's been trying to call me."
    MC "I gotta go. I'll see you later."
    hide BBW with dissolve
    "And I made for the exit, not running and certainly not looking back."
    MC "Probably best if I don't run into her for a couple days. Or weeks."
    $disableRoute("BBW")
    jump daymenu

label BBW025_c1_2:
    MCT "Deep breath. Here we go."
    MC "Alice. Would you like to go out some time?"
    if getAffection("BBW") < 9:
        $setFlag("BBW025A_unlock")
        show BBW neutral
        BBW "'Go out' as in 'go out,' I take it."
        show BBW happy
        BBW "I have to compliment you on your taste..."
        show BBW neutral
        BBW "But I don't think this is the right time."
        MC "Oh..."
        MC "I guess you do have a lot to deal with right now, what with your business and all."
        BBW "Hmm?"
        BBW "No, that's not taking up too much of my time."
        MC "Wait. Are you... not doing the 'It's not you, it's me' thing?"
        BBW "Oh, no."
        BBW "The issue isn't me."
        BBW "Not that it's you, per se."
        BBW "It's us, rather."
        BBW "Compatibility-wise, I'm not convinced there's something there."
        MC "What do you mean?"
        BBW "There is a physical connection. You have a certain charm, and just now you mentioned my own glamor."
        show BBW haughty
        BBW "Not in a passive or even placating way, but with a genuine eye for beauty."
        BBW "But you're not the first gentleman I've had swoon over me, mistaking physical attraction for emotional resonance."
        show BBW neutral
        BBW "And I've found those who can't look past the flesh often have nothing under the surface themselves."
        BBW "Convince me this is not an idle fancy of yours, and I might change my answer."
        BBW "I'm not saying you have to sweep me off my feet. Love is not a spontaneous combustion, but a bonfire that must be built and tended."
        BBW "But I know not to go flitting around like a moth drawn to any bright light, and I want to make sure you understand that as well."
        BBW "Do you understand?"
        MC "I think I do."
        show BBW happy
        BBW "Glad to hear."
        BBW "Now if you'll excuse me, I see Aida approaching with my second course."
        hide BBW with dissolve
        "I excused myself, leaving Alice to her dinner."
        "I did understand what she was getting at, though I'm not sure I agreed."
        "If this was purely physical, I could have just asked her out back at the start of the term."
        "Didn't my working for her count for anything?"
        "Well, no. She probably saw that as an employer-employee relationship. I guess I should be happy she didn't outright say 'No' based on that."
        "So, OK. I just have to prove myself more serious."
        "Not impossible."
        jump daymenu
    else:
        $setFlag("BBW_dating")
        $lockRoute("BBW")
        show BBW happy
        BBW "Yes, I would."
        MC "Really?"
        MC "I mean, wonderful. Splendid."
        MC "Say... Saturday night?"
        MC "Dinner and a movie?"
        BBW "That sounds nice."
        MC "OK. I'll meet you at 6."
        "I might have stammered for a few minutes more if Aida hadn't turned up just then, wheeling in Alice's second course."
        "It was the perfect out, so I excused myself and walked out of the cafeteria."
        hide BBW with dissolve
        "It was hard to fight the urge to skip or whoop, until I reached the hall and suddenly realized I had no idea where I was going to take her."
        "I was so focused on just getting the question out I didn't think about what came next."
        jump daymenu

label BBW025A:
    $lockRoute("BBW")
    scene Cafeteria with fade
    "I was having trouble paying attention to the week's company meeting."
    show BBW neutral at center with dissolve
    BBW "Moving on to new business, the recent tariff battle between America and China has me concerned blah blah blah..."
    "After building up the courage to ask Alice out it was hard not to treat her 'Ask me later' response as a loss."
    "A straight up 'No' would have been like ripping the band-aid off, the pain strong but gone quickly."
    show BBW happy
    "And I could have written it off as her just not being into me. Not what anyone wants to hear, but it would have been easier to move on from."
    "But her actual response left the door open, and that just made things worse. Neither 'Yes' nor 'No,' I was left wondering what exactly she was looking for."
    show BBW angry
    "Do I act more manly? More independent? More subservient?"
    "I at least knew that just asking her wouldn't cut it. That would be too desperate, even for someone who enjoyed attention like she did."
    show BBW neutral
    "So I came to the decision to just be myself - as much as that sounded like pablum - and see if her opinion of me wouldn't change."
    "She seemed happy enough lately, but how to tell that was a reflection of her attitude towards me and not just how she felt with her place in life right now?"
    BBW "Thoughts?"
    MCT "Crud. I missed 90%% of that."
    MCT "Something about tariffs?"
    MC "I... have not been paying attention to the news."
    MC "If you have some articles I could read I could catch up, but right now... I can't weigh in."
    "Alice nodded her head."
    BBW "I understand. This probably didn't seem too important as a ground-level salesman. (Even though this does trickle down to what products we'll have for sale and possible price increases...)"
    show BBW happy
    BBW "But the potential for upward mobility is always there for workers who display motivation, drive and initiative."
    BBW "You don't have to be just a salesman forever, Keisuke. Opportunities don't always come flashing neon signs."
    BBW "Next on our agenda blah blah blah."
    show BBW neutral
    "Despite my best efforts, I got lost in my own thoughts again."
    "Was Alice just being encouraging, or was she hinting that there was an opportunity for me right now?"
    "When the meeting broke - coinciding with Aida rolling up the first course of Alice's dinner - I leapt."
    MC "One last thing, Alice. It's not business related."
    show BBW happy
    "Her expectant look perked up, which seemed like a good sign but which also made me nervous."
    "But after going through this once already, I couldn't back down now."
    "Especially since I had what I was sure was a killer offer."
    MC "There's a special showing of The Lace of Heaven this Saturday. Would you be interested in seeing it?"
    "Lace of Heaven wasn't what I would call a 'Keisuke movie,' but the time period arthouse title seemed like the sort of thing Alice would be interested in."
    show BBW happy
    "And it looked like I had chosen well, judging by her reaction."
    $setFlag("BBW_dating")
    BBW "That sounds delightful."
    BBW "I'll trust you to get the tickets, and perhaps we should have dinner before the show?"
    MC "Yeah. Leave it all to me."
    MC "I'll let you know what time to be ready once I have everything sorted out."
    BBW "It's a date."
    "The fact that she was the one to say that made me even giddier, but I managed to keep myself restrained as I left the cafeteria."
    scene Hallway with fade
    "I held out until I made it to the hallway before I pumped fist."
    MC "Mission accomplished!"
    MC "Of course, now I have to work to keep her happy."
    MC "So it's more like 'Level one complete.'"
    MC "But one thing at a time. I've got the day set, I have things planned. Let's get through that first and worry about what comes next later."
    jump daymenu

label BBW026:
    scene Classroom with fade
    $setProgress("BBW", "BBW028")
    if not getFlag("BBW_dating"):
        "After Alice turned down my invitation to a date - not an actual 'No,' but more like 'Try again later' - I'd been racking my brains trying to think of what else I could do to clear that last hurdle."
        "Not that I was sure what the hurdle was. Alice had said she wanted something more than physical attraction, so complimenting her on her fashion wasn't going to cut it."
        "I'd have to dig deeper, but when you aren't even in a relationship what can you do to woo someone?"
        "All my ideas came from movies or TV shows, the big romantic gestures that I had a feeling Alice would dismiss as superficial."
    else:
        "Getting Alice to say 'Yes' to a date had been a minor victory, but it also opened up a new level of challenges."
        "I had already put a lot of thought into what we would do come Saturday night. I had the movie and restaurant picked out, and I had even tried to set a reservation."
        "Turned out they didn't take reservations, but I was able to get the movie tickets in advance."
        "But Saturday wasn't here yet. I'd still be sitting in classes with her, working with (or for, technically) her. There'd be chances to embarrass myself, to turn her off even unintentionally."
    "I wasn't stressed out terrible enough that I couldn't sleep, but I still couldn't keep such thoughts out of my mind as I sat through class."
    MCT "At least I don't have anything else to worry about right now."
    show HR neutral with dissolve
    HR "And yes, that will be on the test."
    MCT "!"
    MCT "Test?! Oh... crud."
    MCT "The test I haven't made time to study for yet."
    MCT "Looks like my evening's been planned."
    hide HR with dissolve
    "But as I was getting ready to leave Alice put a hand on my shoulder."
    show BBW neutral with dissolve
    BBW "May I have a moment?"
    MC "Uh, sure."
    "Her tone of voice almost made my stomach drop. This wasn't good news, whatever it was."

    scene Hallway with fade
    show BBW neutral
    BBW "I have a problem. I need some help."
    MCT "OK, so it's not about me. That's good."
    BBW "I need to mail off some paperwork related to the requisitions company, tax filings and whatnot."
    BBW "It needs to get to my family's accountant within a couple days, and I don't trust regular mail going out of the school."
    MC "Think it'll take too long?"
    BBW "Exactly."
    BBW "But I can't make the trip to the post office to send it express, because I have music club. And Aida is busy with other tasks."
    BBW "Would you be willing to make the trip for me? It would save me the hassle tomorrow, which is already looking to be an ordeal."
    MCT "Great. I have a chance to court Alice's good graces, but only if I shirk my studies."
    menu:
        "Sorry, but I don't have the time.": #(+1 affection)
            jump BBW026_c1_1
        "Sure, I can do it.": #(-1 affection)
            jump BBW026_c1_2
        "(I think I can pull off both the errand and the studying)": #(+2 affection, if Academics score is > / = 12; -1 affection if Academics score is < 12)
            jump BBW026_c1_3

label BBW026_c1_1:
    MC "Sorry, but I don't have the time."
    MC "I need to study for the test tomorrow."
    BBW "I see."
    show BBW happy
    BBW "That is the greater priority, though."
    BBW "I'll see if I can find someone else to help out."
    BBW "Study hard."
    "Now that I had thrown away the chance to score points with Alice, I really had to buckle down and make the most of my time."
    scene Classroom with fade
    "It was worth it, though. I scored higher on the test than I expected."
    "And Alice did notice how well I did."
    show BBW happy with dissolve
    $setAffection("BBW", 1)
    BBW "Well done, Keisuke."
    BBW "You even got question six right. I found that one rather... tricky."
    MC "Yeah, it almost tripped me up."
    MCT "That must be worth something in her eyes, right?"
    jump daymenu

label BBW026_c1_2:
    MC "Sure, I can do it. Just give me the address."
    show BBW happy
    BBW "Really? Excellent."
    BBW "Just bring it back to my room tonight."
    BBW "You're a lifesaver, Keisuke."
    "I felt pretty cocky as I dropped my stuff off in my room and then headed into town."
    scene Town with fade
    "I had hoped it would be a quick jaunt. If I rushed to and from the post office I could get back in time to get some studying done."
    "Unfortunately the post office was pretty busy. I didn't think this town was that active, but there was a line almost to the door of people sending stuff off or picking stuff up."
    "I didn't have any chance to study that night, but as I dressed for bed I made a promise to myself to cram the next morning."
    scene Classroom with fade
    "It did me no good."
    "I wasn't too far off from a passing score. I could see a handful of questions where I was almost right..."
    "And there were several others where I was almost on the right track..."
    "And the ones where I had guessed... Well, if I had guessed differently..."
    "No, I had failed."
    show BBW neutral with dissolve
    BBW "So how did you do, Keisuke?"
    BBW "I thought question six was a bit tricky."
    MC "I... didn't get that one."
    BBW "Did you pick 'D' as well?"
    "Before I could stop her Alice took the sheet from my hand."
    "Her expression was even more crushing than the test score itself."
    show BBW sad
    BBW "Oh... What happened, Keisuke? Didn't you study for this?"
    MC "I didn't get a chance."
    MC "I meant to last night, but I went into town for you and that turned into a whole thing."
    BBW "Why didn't you tell me you needed to study? I could have gotten someone else."
    MC "I just... I thought... I don't know what I was thinking."
    $setAffection("BBW", -1)
    BBW "You're going to have to really work to keep your grades up after this, Keisuke."
    BBW "If you need time to study, just tell me. I can find other people to help me out."
    MC "No, it's-"
    "I wanted to say 'It's fine,' but I realized I'd just be digging myself in deeper."
    MC "I'll keep that in mind."
    MCT "So now Alice thinks I'm sliding towards flunking. Not the best foot forward."
    jump daymenu

label BBW026_c1_3:
    MCT "I think I can pull off both the errand and the studying."
    if getSkill("Academics") < 12:
        jump BBW026_c1_2
    else:
        MC "Sure, I can do it. Just give me the address."
        show BBW happy
        BBW "Really? Excellent."
        BBW "Just bring it back to my room tonight."
        BBW "You're a lifesaver, Keisuke."
        "Alice said it wouldn't take long, but you never knew."
        "I left for town right away, wanting to get the job done quick. And I brought my books with me."
        "I could almost sense there would be some delays, and if that was the case I wanted to get some quick studying in while I waited."
        scene Town with fade
        "It turned out to be the right call."
        "I had hoped it would be a quick jaunt. If I rushed to and from the post office I could get back in time to get some studying done."
        "Unfortunately the post office was pretty busy. I didn't think this town was that active, but there was a line almost to the door of people sending stuff off or picking stuff up."
        "At least I was able to use my time waiting efficiently. Got a lot of studying in."
        scene Classroom with fade
        "And it was worth it. I scored higher on the test than I expected."
        "Alice noticed how well I did, which on top of running the errand had to have raised my standing in her eyes."
        show BBW happy with dissolve
        $setAffection("BBW", 2)
        BBW "Well done, Keisuke."
        BBW "You even got question six right. I found that one rather... tricky."
        MC "Yeah, it almost tripped me up."
        "As casual as I thought I sounded, I was really about to crumble."
        "I had almost bitten off more than I could chew, but I had managed to come out ahead."
        "I just hoped I wouldn't have to juggle so much at once anytime soon again."
        "Maybe Alice wouldn't turn out to be so high-maintenance? Hopefully?"
    jump daymenu

label BBW027:
    scene Hallway with fade
    "Getting out of class didn't free me for the day. It meant my day had just started."
    "When we were dismissed from class I made a beeline for the library to take care of some research for a project I'd been putting off."
    "Then I spent an hour zipping around the girls' dorm delivering orders for Alice's business."
    "Then to the boys' for the same. Then back to the girls' to try again with those who weren't in their room the first time."
    "I wanted to get it all done quickly, because I had to get tomorrow's homework done and I had some long-term assignments weighing on my mind."
    "Eventually I only had one last package to deliver, but after the third time visiting the lady-in-question's dorm I decided to call it a day on that front."
    "I had too much homework to tackle to spend all afternoon on this one thing."

    scene Cafeteria with fade
    "The cafeteria was opening for dinner at this point, and I needed fuel."
    "It felt good to get off my feet, but once I had my food and a seat I pulled out a textbook."
    "I had too much to do right now to relax."
    "I was in the middle of my meal and a description of eukaryotes when Alice appeared."
    show BBW happy with dissolve
    BBW "Hello, Keisuke."
    BBW "Studying while eating? I applaud your efficiency."
    MC "Thanks..."
    "I rubbed my eyes and sighed."
    show BBW neutral
    BBW "Something wrong?"
    MC "Just feeling overwhelmed right now."
    BBW "Hmm... Yes. Our course load is picking up."
    show BBW happy
    BBW "No special treatment because of our condition, right?"
    MC "I'm not asking for things to be easier, I just..."
    MC "You ever feel like you're going as fast as you can just to keep up?"
    show BBW neutral
    BBW "The Red Queen race."
    MC "What?"
    BBW "Literary reference that made its way into scientific terminology. It's an esoteric term for what you just described."
    BBW "Everyone feels it now and then."
    show BBW happy
    BBW "Trust me. I grew up in circles of the most driven and harried people in the world."
    BBW "You're either struggling to get to the top or you're struggling to keep your place. Or both."
    MC "Yeah, that sounds super-stressful."
    show BBW sad
    BBW "It is. I've seen people unable to keep up. They didn't just drop out of the game, they... crashed."
    MC "Cripes. Why do you sound so happy?"
    show BBW happy
    BBW "Because I love the stress."
    BBW "To a point, of course. Everyone has their limits."
    show BBW haughty
    BBW "But when my workload is just right - not too light, not too heavy - I feel invincible."
    BBW "The thought of having so much being hurled at me at once and I remain unbowed... I am a woman on fire."
    MC "I... see."
    MC "But you still need a break now and then."
    show BBW neutral
    BBW "Oh, not just 'now and then.'"
    BBW "Recreation and relaxation have to be part of your schedule. You need time to recover, mentally and physically."
    BBW "Just make sure your downtime is not time wasted. Slowing down doesn't mean being idle."
    BBW "Time is like nothing else. What you lose is gone forever."
    BBW "You can make more money. You can replace worn out or damaged goods. Usually. But when the day is done you don't get it back."
    MC "So even when you're taking it easy you don't actually relax?"
    BBW "Oh, no. I do relax."
    show BBW haughty
    BBW "I wouldn't bother paying for massages if I was still tense afterward, would I?"
    show BBW neutral
    BBW "I just never do nothing. Even when I'm relaxing my decisions about what to do are made with an eye towards replenishing my energy or rejuvenating my mental prowess."
    MC "That still sounds stressful. To have a free afternoon and try to figure out the best way to unwind?"
    MC "I don't know. When I have free time I'm intentionally not thinking about what the most efficient thing to do with my time is."
    BBW "It's not hard, if you plan ahead and know what you want."
    BBW "Like I said before, you have to make your downtime part of your schedule."
    MC "OK, I guess I get that."
    MC "But real life doesn't always accommodate, you know?"
    MC "Things happen. Unexpected problems turn up, or it takes longer to do something than you expect."
    "Alice shook her head, as if I didn't understand her."
    BBW "Of course 'things happen.' Where would the challenge be if you knew exactly what to expect all the time?"
    BBW "But to the well-organized mind even the unexpected can be anticipated."
    show BBW haughty
    BBW "And, if you're good enough, the unexpected won't be a problem."
    show BBW happy
    BBW "But my point stands. You need to slow down now and then."
    BBW "Set aside a chunk of time each day where you don't think about school or work or anything."
    BBW "No matter what you have yet to do, you recharge your batteries at the appointed time. And when you get back to work you'll be ready for come what may."
    show BBW neutral
    BBW "The important thing is that you practice self-care."
    MC "But do you think your life can be so finely planned that you can say 'Now is the time when I will relax'?"
    BBW "I believe in structure, just as a general principle."
    BBW "As you said, life doesn't try to accommodate our plans, so it's on us to make our plans work."
    MC "And you don't think that gets too rigid?"
    BBW "Not at all. I've lived by this for years, and it's served me well."
    show BBW haughty
    BBW "Then again, I do have the benefit of knowing where I'm going in life. It makes it easier to think long-term and, working backwards, in the short term."
    show BBW happy
    BBW "But anyone can be determined and focused if they put a little effort in."
    BBW "Just visualize what you want, divide the path between 'here' and 'there' into manageable tasks, and go after it bit by bit."
    MC "Heh. You sound like a self-help guru."
    show BBW neutral
    BBW "Do I? I suppose I've listened to enough of those kinds of presentations."
    BBW "Life coaches and motivational speakers get a lot of business among the upper echelons of the corporate world."
    BBW "I guess I've picked up some of that that stuff here and there. It's all crept into my brain."
    "I took another bite of my food to give myself a moment to think."
    "I wanted to say that what worked for Alice wouldn't work for everyone, but I couldn't pin down the fault in her argument."
    menu:
        "I can see the logic behind it.":
            jump BBW027_c1_1
        "Do you actually buy it?":
            jump BBW027_c1_2

label BBW027_c1_1:
    MC "I can see the logic behind it."
    MC "The need to take things slow now and then, the importance of focusing."
    MC "I guess I just need to get serious about all this."
    MC "I should have expected the courses to get harder now, and I knew working for you was going to require time and energy."
    BBW "It's not all unmanageable, though."
    BBW "You just have to step it up."
    BBW "Though if your workload gets to be too much, let me know. I can try to hire someone else to help out."
    MC "Oh, no. It's not too much. It's just... a lot."
    show BBW happy
    BBW "If you say so."
    "She looked at her watch."
    BBW "I need to go. The swim team should be done with the pool now, so I'm going to get my workout in."
    BBW "Good luck with everything, Keisuke."
    MC "Yeah, thanks."
    "When she was gone I turned back to my textbook."
    "None of the information seemed to be getting through, so I closed it and turned my attention to my dinner."
    "And for a while after I was done I just sat there, thinking."
    "Next thing I knew, half an hour had passed."
    MCT "Crap! That's exactly what she said not to do. I got nothing done."
    jump daymenu

label BBW027_c1_2:
    MC "Do you actually buy it?"
    "Alice blinked."
    BBW "What do you mean 'buy it?'"
    MC "That it's as easy as... how do I put it? Partitioning everything."
    MC "This is when I work, this is when I play, this is when I get romantic."
    BBW "If you know what you want-"
    MC "Yeah, yeah. You said that."
    MC "'If you know what you want' you can work towards it."
    MC "But that's obvious, isn't it? And it's not always as simple as looking off in the distance and then walking there."
    MC "You'll hit roadblocks, you'll have to take detours."
    MC "Or maybe something more important turns up."
    MC "How do you plan for something like love, for instance?"
    "Alice's expression sort of set. I had given her pause."
    MC "You can't schedule the moment you fall in love. You can't really plan for a major fight-"
    MC "Well, you can try to plan how you would react. Tell yourself not to get heated or say anything out of bounds."
    MC "But when the moment arrives? That'll be when emotion takes over, not logic."
    MC "And if we look at the long term, something like marriage or parenthood could really disrupt your life plans."
    "I stopped at that point, because I could see Alice trying to grapple with what I had said."
    "I guess she didn't have an answer at the ready for this."
    "After a moment she responded."
    BBW "The question of children isn't that hard to deal with. Contraceptives and other things can prevent an unwanted pregnancy."
    BBW "And even if you plan for a child, that is a potential Pandora's Box of issues."
    "She closed her eyes and sighed."
    BBW "But I already said that if you're prepared, you can handle the unexpected."
    BBW "I accept the unexpected will happen. I just don't accept that I have to lay out the welcome mat for it."
    "She looked at her watch."
    BBW "I need to go. The swim team should be done with the pool now, so I'm going to get my workout in."
    BBW "We can continue the conversation later, if you want."
    show BBW happy
    BBW "In the meantime, good luck handling your homework and everything."
    MC "Yeah. Have fun."
    "As she walked off I finished my dinner."
    "I tried to also continue with the science reading, but I saw right away it wasn't going to stick."
    "Alice had been right about the need to slow down at times."
    "I still didn't know about how much one could plan ahead for themselves, but I wasn't about to solve the problem anytime soon."
    "After I was done eating I stayed there for a moment, letting my mind unwind."
    "Then, before too long, I bussed my table and left. Back to the grindstone."
    jump daymenu

label BBW028:
    $setProgress("BBW", "BBW030")
    scene Cafeteria with fade
    play music Schoolday
    "I timed my dinner for when I expected Alice would be here, but her usual spot was empty."
    MCT "Oh, right. Music club practice."
    MCT "Well, I'm already here. Guess I'll grab some grub for myself."
    "I had a nice meal - nice as far as the cafeteria food went - and as I was finishing up Alice appeared on the scene."
    MC "Hey, Alice. How's the music club treating you?"
    show BBW neutral with dissolve
    BBW "It's fine. Just fine. It meets my expectations."
    MC "Uh-oh. You're not fighting with the president again, are you?"
    BBW "No. She and I have an accord. My previous criticisms, while still on the record, notwithstanding."
    BBW "But it is a struggle to keep my peace when she seems committed to watering down our collective effort so thoroughly."
    BBW "Just look at these fliers she's produced for our first concert."
    "She handed me a small stack of blue pages announcing a performance the following weekend."
    "I couldn't see Alice's complaint at first, until I tried to look at it from her perspective."
    MC "They're kind of plain."
    show BBW angry
    BBW "They are practically designed to be ignored!"
    show BBW neutral
    BBW "I'm supposed to post these around the campus, next to all the other bills for every other club or gathering."
    BBW "If the auditorium is even a quarter full with this as our advertising campaign it would be astounding."
    BBW "It's a waste of my time to put them up in the first place."
    MC "Maybe you could redo these. Make them better."
    BBW "If I had the time..."
    if getSkill("Art") >= 7:
        MC "I could do it for you."
        BBW "Could you?"
        MC "It wouldn't be anything too fancy, but give me an hour in the computer lab and I can make something a little more eye-catching."
        show BBW happy
        BBW "That would be nice."
        BBW "Could you do it now? I said I would put them up tonight."
        MC "Sure. I'll bring the finished ones to your room."
        BBW "This is a big help, Keisuke. Here, take these with you so you have the info."
        "She handed me the stack of original fliers."
        scene Hallway with fade
        "The computer lab was busy, but I found an open station and got to work."
        "I didn't spend too long on it, just copying the info from the original fliers and changing the fonts to make them pop."
        "Add a few flourishing patterns in the corners and bold the showtime to have it stand out, and it was a marked improvement over the original."
        "I printed out 50 copies and took them to Alice's dorm."
        show BBW happy with dissolve
        $setAffection("BBW", 1)
        BBW "Oh, these are much better."
        BBW "I still have time to hang them up tonight. Care to join me?"
        MC "Sure. It's a nice night."
        "We walked all over the campus, Alice taping up the fliers as we chatted."
        "It wasn't what I would call 'romantic,' but in its own simple way it was nicer than some dates I'd had."
        jump daymenu
    BBW "As it is, I already have too much on my plate."
    "She looked at her watch and sighed."
    BBW "Could I ask a favor of you? Could you do this for me?"
    BBW "Just post them at all the regular announcement boards and in the halls."
    menu:
        "I guess I can do it.":
            jump BBW028_c1_1
        "I have my own work to do.":
            jump BBW028_c1_2
        "I can't do it for you, but I can help." if getAffection("BBW") >= 14: #(If affection score is > / = 14; +1 affection)
            jump BBW028_c1_3
        "I can't do it for you, but I can help. (disabled)" if getAffection("BBW") < 14:
            pass

label BBW028_c1_1:
    MC "I guess I can do it. It won't take long, will it?"
    BBW "Not if you work fast."
    BBW "Thanks. Here you go."
    "And she unceremoniously dropped the stack on the table in front of me, then walked away."
    scene Hallway with fade
    "As I walked around the campus I couldn't fight the feeling that I had given in too easily."
    "She had said 'Thanks,' but her tone..."
    "Maybe I was imagining it, but she had sounded like my saying 'Yes' was a given. Like she was entitled to my help."
    "It didn't stop me from doing the job, but I made myself a promise that next time I wouldn't roll over right away."
    jump daymenu

label BBW028_c1_2:
    MC "Sorry, but I have my own work to do."
    MC "Not club stuff, but homework, essays, you know."
    BBW "I understand."
    BBW "And the job was given to me, after all."
    MC "On another day I could help."
    BBW "I get it."
    BBW "I guess I need to start on this now, if I'm going to have time to look over our sales figures tonight."
    if getAffection("BBW") >= 10:
        BBW "I'll see you around."
    else:
        BBW "I'll see you in class, Hotsure-san."
    "And she left."
    hide BBW
    "She didn't sound angry, at any rate. That was good."
    jump daymenu

label BBW028_c1_3:
    MC "I can't do it for you, but I can help."
    $setAffection("BBW", 1)
    "She considered it for a second, then nodded."
    show BBW happy
    BBW "That would be appreciated."
    BBW "It won't take as long this way."
    scene Hallway with fade
    "We walked all over the campus, Alice taping up the fliers as we chatted."
    "It wasn't what I would call 'romantic,' but in its own simple way it was nicer than some dates I'd had."
    jump daymenu

label BBW029A:
    #Time: Afternoon
    scene Cafeteria with fade
    MCT "This is a fine mess I've gotten myself into."
    "No, I hadn't come to terms with the news from Aida yet."
    "I'd say this was the worst possible time for something like this to happen, but the news about my growth factor hadn't been too heavy a burden since hey, my only problem was a messy head of hair to tame."
    "Still, if I had been a regular college student, still living at home, with nothing else to worry about it would have been slightly easier to deal with this surprise."
    "Being dressed down by my parents would have been a small price to pay to have them on hand for support in one form or another."
    UNKNOWN "Hotsure-san."
    MCT "Someone calling my name?"
    show BBW neutral with dissolve
    play music BBW
    MC "Oh, Alice."
    MC "Sorry. Got my head in the clouds."
    BBW "I imagine you have a lot going through your head right now."
    MC "What do-? Oh, wait. You're Aida's roommate. You probably heard."
    BBW "Kodama-san needs what support she can get, and since she's not the most outgoing young woman to begin with it is not surprising she confided in me first."
    MC "Yeah. I was just thinking about how much easier this whole thing would be if we were regular college students, still living at home."
    MC "I know my parents would be upset, but they'd help me- us, all the same."
    MC "Aida's parents..."
    MC "I actually don't know anything about her family. That's kind of terrible."
    BBW "It sounds like you're taking this seriously."
    MC "Well, yeah."
    MC "It's my fault she's in this predicament."
    BBW "Mmmmm..."
    BBW "Not entirely. Her genetics are outside her control, or anyone else's."
    BBW "The traditional concept of 'fault' doesn't apply here."
    BBW "But it is good you're not running from your responsibilities."
    MC "I'll be honest, when I first got the news my thoughts included the feasibility of hightailing it out of here. Leave the school, leave the island."
    MC "It wasn't a serious thought, but..."
    BBW "Panic reflex?"
    MC "I'm not proud of it."
    BBW "It's understandable, and you have made the mature choice. I don't think anyone can blame you for it."
    BBW "Have you come to any conclusions about what you're going to do?"
    MC "There's not a lot I can. I'm a college student effectively quarantined on this island."
    MC "I thought about contacting my parents and probing the possibility of Aida and I moving back in."
    BBW "I doubt the school would be willing to let her leave, not while she is in her current state."
    MC "That's what I figured."
    MC "At least I have a few months to figure out how to drop this on them."
    show BBW happy
    BBW "There is that."
    if getFlag("BBW_working"):
        BBW "At least you have a job, part-time though it is."
        BBW "The school will take care of Kodama-san's needs, particularly medical, but I don't foresee them covering 18 years of clothing, food, education, etc."
        MC "Oi... I'll probably have to pick up a few more hours working for you, huh?"
        BBW "Oh, Keisuke. You're going to have a lot more demands on your time soon. Working for me will be the least of it."
    MC "I should probably get back to my room, take care of my homework."
    show BBW neutral
    BBW "You're leaving? Did you already have dinner?"
    MC "Oh!"
    "I mentally slapped my head. That's why I had come here in the first place."
    MC "I'm already losing my mind."
    jump daymenu

label BBW029B:
    #Afternoon
    scene Cafeteria with fade
    MCT "Dinner time. Am I in the mood for anything in particular? No. Do I have to eat something? Yes."
    "I take the path of least resistance and grab the first things that look appealing from the line of food: a thing of melon bread and a bowl of soup."
    "I look around for an open table and spot Alice sitting with a girl I don't recognize."
    "Before I get there the other girl gets up and leaves. Alice writes something down on a piece of paper."
    MC "Room for one more?"
    show BBW neutral with dissolve
    play music BBW
    BBW "Hm?"
    if getAffection("BBW") <= 10:
        BBW "Oh. Hello, Hotsure-chan."
        BBW "Help yourself."
    else:
        show BBW happy
        BBW "Oh! Keisuke! Have a seat."
    MC "Thanks."
    MC "I'm not interrupting anything, am I?"
    show BBW neutral
    BBW "You are referring to Megumi? Our business was concluded."
    MC "Business?"
    BBW "With Kodama-san being in the family way I am in the market for a new assistant."
    BBW "I do not consider any of the other women in our class to be an adequate replacement, so I have turned to outside applicants."
    MC "Does it have to be a woman?"
    "She gave me a smirk, which I didn't understand at first."
    show BBW happy
    BBW "Are you that eager to spend more time with me that you want to handle my cooking, my laundry, and other jobs?"
    MC "No!"
    MC "I mean, I wasn't angling for a job."
    if getFlag("BBW_working"):
        MC "Not another job."
    MC "I was just curious."
    show BBW neutral
    BBW "Hmm."
    BBW "My mention of laundry should answer your question."
    BBW "My assistant will need to do much work in my dorm, dealing with certain personal matters. I can not entrust a man to those duties."
    MC "I see."
    MC "So is... Megumi your new assistant? Or are you still considering other applicants?"
    show BBW sad
    BBW "I have yet to find anyone truly satisfactory."
    BBW "For example, Kodama-san has an unmatched skill in the kitchen."
    "She pushed a plate of some kind of finger food over to me."
    BBW "Salmon pinwheels. Try one."
    MC "..."
    MC "It's good. A bit rich..."
    BBW "It's adequate. Perhaps my palate is too refined for my own good."
    BBW "I truly do not want to subsist on the food the school supplies, so even if I am not floored by submissions like this I must pick someone to serve as my chef."
    MC "There are worse things than 'merely good' cuisine."
    MC "At least you won't be a young, single mother."
    show BBW neutral
    BBW "That is so."
    BBW "Though as I understand it the school will take care of Kodama-san and her progeny. And I will be willing to step in should that prove necessary."
    MC "That's thoughtful of you."
    "She shrugged. 'No big deal,' it said."
    BBW "Philanthropy is an ideal quality in the elite."
    "She pulled the plate of pinwheels back to herself and took a large bite of one."
    "She sighed."
    BBW "{i}Sigh{/i}"
    BBW "I can not chastise Kodama-san for being inconsiderate, but I do not have to be happy with how this turn has affected me."
    MC "You'll get by."
    "She finished the pinwheel."
    BBW "I shall endure."
    jump daymenu

label BBW029C:
    #Time: Afternoon
    scene Cafeteria with fade
    "Things had been pretty intense lately with all that was happening with Aida."
    "But that didn't spare me from classes, homework, or regular bodily needs like food."
    "And today was chicken katsu day. Maybe things were looking up for me-"
    show BBW angry with hpunch
    play sound Crash
    BBW "HOTSURE!"
    play music Tension
    MC "Ah!"
    BBW "Is what I hear true?"
    MC "Aah!"
    BBW "Did you tell Kodama-san that her pregnancy is none of your concern?"
    MC "Aaah!"
    play sound Crash
    BBW "Answer me!"
    show BBW angry with hpunch
    MC "Aaaah!!"
    MC "No! I-"
    MC "I didn't phrase it like that."
    BBW "Did you refuse responsibility for your actions?"
    MC "No-!"
    BBW "Liar!"
    show BBW angry with hpunch
    MC "I mean... I..."
    MC "I said I can't deal with the pressures of fatherhood right now. I have so much going on in my life as it is."
    BBW "And you think Kodama-san doesn't?!"
    BBW "What pressures are you grappling with that she is not doing so ten times more so?"
    MC "Well, being here and everything about that."
    BBW "You are here because of your hair!"
    BBW "Are you claiming to be overwhelmed by the pressures of having to put your hair in a ponytail every morning?!"
    "We had quickly become the center of attention for the entire cafeteria."
    "I knew Alice had training as a vocalist, but I never imagined her voice could be so dominating."
    MC "Can we go somewhere else to have this conversation? People are staring..."
    BBW "I am not concerned with your comfort, you despicable cur!"
    show BBW angry with hpunch
    BBW "Take one second to imagine the situation Kodama-san is in, and what it will be like several months from now."
    BBW "You think no one will be staring at her?"
    BBW "You contemptuous, self-centered egoist."
    BBW "Do you think we all exist to serve at your pleasure, and are to be discarded when you have had your fun?"
    #[BBW_Angry zooms in]
    "And then she leaned in closely, and her voice dropped to a perfectly normal tone, but it was still laced with barbed wire."
    "That was the scariest part."
    BBW "If you are truly abandoning Kodama-san in this, her most trying time, then by all the powers of heaven and hell I am warning you to make a complete break."
    BBW "If I ever see you talking to Kodama-san, or even looking in her direction, I will grind you under my foot like the loathsome worm that you are."
    BBW "She is not your plaything to pick up and drop at your whim."
    BBW "As far as you are concerned, she is forbidden territory to you now."
    #[BBW_Angry moves back to regular size]
    if getFlag("BBW_working"):
        BBW "Needless to say, you are fired."
        BBW "I will bring your remaining salary to class tomorrow morning. And do not think to ask for a letter of recommendation from me."
        $setFlag("BBW_working", False)
    BBW "Perhaps it would be best if you made sure that neither Kodama-san or I will ever run into you outside of class."
    BBW "Maybe take your meals to the roof, or that stretch of dirt behind the gym."
    hide BBW with dissolve
    "I stood there, frozen, as she walked off."
    "Suddenly I wasn't hungry anymore."
    "And staying in my dorm for the rest of the day seemed like a really good idea."
    $disableRoute("BBW")
    jump daymenu

label BBW030:
    $setProgress("BBW", "BBW031")
    scene Dorm Interior with fade
    "The time had come for my first date with Alice."
    "I had to admit, I had prepared for more than a few obstacles."
    "The entire day had been planned out with several different potential routes."
    "Everything we did, the exact path we walked, it was all mapped out in my head."
    MCT "This must be how visual novel writers feel when they write a date scene. Everything planned with no surprises."
    scene Classroom with fade
    play music Schoolday
    "Obviously a woman can be a lot more unpredictable than a roller coaster, but the core idea still held."
    "I wasn't completely at ease, though. In the several minutes leading up to the start of the school day I grew anxious waiting for Alice to appear."
    "There was no reason for it, just nerves."
    "But as the last minute began counting down, Alice hadn't shown up."
    "I don't think she had ever been late before. Something had to be up."
    MC "Hey, Aida."
    show PRG neutral with dissolve
    MC "Where's Alice?"
    show PRG sad
    PRG "Nikumaru-san is not feeling well. She won't be in class today."
    MC "Oh, man. Is it bad?"
    PRG "She wouldn't let me near her. She said she didn't want to risk passing whatever she had to me in my condition."
    PRG "But she took her own temperature. It's 101.2. And she was complaining of aches and chills."
    MC "Bummer. Hopefully it's just a 24-hour thing."
    MC "Either way, our date's off, I guess."
    MC "I'll go see her during lunch. See how she's doing."
    show PRG happy
    PRG "She would like that."

    scene Hallway with fade
    #Time: Afternoon
    "Lunchtime arrived, and I made my way to Alice's dorm."

    scene Dorm BBW with fade
    play music Rain
    "I hoped I wasn't disturbing her sleep, but I knocked lightly all the same."
    show BBW sick with dissolve
    BBW "Keisuke."
    "Her voice was a croak, and she looked pale and tired."
    MC "Sorry for bothering you. Aida told me you were sick, and I wanted to see how you were doing."
    BBW "She told you true."
    BBW "I believe it's only a 24-hour virus, and I will be better tomorrow."
    MC "But we'll have to postpone our date, of course."
    BBW "I'm sorry, but there are things even outside my control."
    MC "Don't worry about it. Rest up, get better."
    MC "Have you taken anything? There's this special kind of tea my mom always gave me when I was sick, and it always helped."
    BBW "I've taken ibuprofen and cold medicine."
    BBW "I think rest and liquids are all I need."
    MC "Maybe."
    MC "I'll let you go back to sleep."

    scene black with fade
    "I grabbed a quick lunch, then went back to class."

    scene Hallway with fade
    "Even while paying attention to the lessons, I was thinking over that tea I had mentioned."
    "I could probably find it in town. It's not a rare brand or anything."
    "Only problem was the weather didn't look too promising. But once the idea was in my head I was pretty much decided."
    "Class got out, I went to my dorm to grab my umbrella, and I left to hit the town."

    scene Pharmacy with fade
    "Because of the ominous clouds I double-timed it down the hill, jogged to the pharmacy, and frantically scanned boxes in the cold and flu section."
    "The packaging for the tea had been changed since I was a kid. I went past it twice before I spotted it."
    "I paid for the tea, shoved it in my backpack, and started speed-walking back to the hill."

    scene black with fade
    play sound Thunder
    "The bottom of the hill was in sight when the sky just opened up and began dumping water by the gallon."
    "I had my umbrella, for all the help it was. With the heaviness of the rain and wind blowing this way and that I got pretty drenched."
    "Nothing to be done about it, I pressed on, scaling the hill and reaching the school grounds."

    scene Dorm BBW with fade
    "I was a sopping mess by the time I got inside the women's dorm. But I had the tea."
    "I knocked lightly again. Alice might be sleeping, but there was a good chance Aida would be in."
    "Sure enough."
    show PRG neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    PRG "Hotsure-san."
    MC "Hey, Aida. Is Alice awake?"
    show BBW sick at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Keisuke. You're drenched."
    MC "Alice. Here."
    "I retrieved the tea. My backpack hadn't be spared the rain's assault, but the insides were blessedly dry."
    MC "I mentioned this tea my mother always gave me. I found some at the pharmacy."
    BBW "Were you out in the rain? It's pouring outside."
    menu:
        "Yeah, I tried to hurry to beat the rain, but...": #(-1 affection)
            jump BBW030_c1_1
        "If the tea helps you, it was worth it.": #(+1 affection)
            jump BBW030_c1_2

label BBW030_c1_1:
    MC "I hope you appreciate what I went through."
    show BBW sick-angry
    BBW "Ugghh..."
    BBW "I appreciate you went out of your way to help me-"
    BBW "Even though I told you this will probably pass with some rest."
    $setAffection("BBW", -1)
    BBW "-but don't try to guilt me because you got caught out in the rain."
    BBW "You chose to run that risk. You're not a victim of circumstance."
    MC "No, I mean..."
    MC "Never mind."
    MC "Enjoy the tea."

    scene Dorm Interior with fade
    "I went back to my room feeling more than a little peeved."
    "I was still soaked from head to toe, and I didn't even have anything to show for it."
    "Shouldn't have even bothered."
    jump daymenu

label BBW030_c1_2:
    "It was hard to tell with her mask, but it looked like Alice was smiling."
    show BBW sick-happy
    $setAffection("BBW", 1)
    BBW "I appreciate the trouble you went through, but you really didn't need to."
    BBW "I said before, I just needed some rest."
    show BBW sick
    BBW "I hope you don't get sick now, though."
    MC "I'm sure I'll be fine."
    MC "Just need to get out of these wet clothes. Maybe take a hot shower."
    show BBW sick-happy
    BBW "Well, here."
    "She opened the tea box and handed me one of the bags."
    BBW "Just in case."
    MC "Thanks. I'll have it tonight and go to bed early."
    MC "Hope you feel better tomorrow."
    BBW "And I hope you still feel well."

    scene Dorm Interior with fade
    "I did as I said I would, changing clothes and showering."
    "Then I made myself the tea while doing my homework."
    "Not the night I had hoped for, but it seemed the best possible outcome given the curveball thrown at me."
    jump daymenu

label BBW031:
    $setSize(3)
    $setTimeFlag("size3")
    $setProgress("BBW", "BBW032")
    scene Dorm Interior with fade
    "Alice's illness had only lasted 24 hours, which meant only one thing."
    "Whether I was ready or not, my first date with Alice had come."
    "It was easy - terrifyingly easy - to be intimidated by her. She was rich, she was used to the finer things, she was a bit... forceful in personality."
    "When I was trying to get to sleep last night, my stomach fluttering like I was in junior high or something, I reassured myself that she must be at least a little open to this."
    "I can't imagine she's ever had trouble saying 'No,' so I wouldn't be here if there wasn't at least a chance."
    MCT "Too late for second-guessing, my man. Let's get this going."
    scene Gate Front with fade
    MC "Alice! Hey!"
    show BBW surprised with dissolve
    "She cocked an eyebrow at my informal 'Hey.'"
    MCT "Right. Gotta be a bit more polished."
    MC "I mean, it's lovely to see you."
    show BBW happy
    BBW "Thank you. You look handsome yourself."
    MC "Uh, thanks."
    "One thing was immediately obvious. She was bigger."
    MCT "Perhaps her immune system was weakened by the upcoming growth spurt? Or maybe it was pure coincidence."
    "Alice's belly was very large now, she looked 9 months pregnant {i}with twins{/i}"
    MCT "I wonder how Kodama-san is handling the news?"
    MCT "I also wonder if I had even dressed appropriately for this date."
    MCT "Just a clean shirt and ironed pants. I guess changing out of my uniform made more of an impact that I expected."
    MCT "Or is she just being polite?"
    MCT "Damn it, don't overthink everything."
    BBW "I can see you glancing at my midsection, Keisuke."
    BBW "Yes, I am bigger. Yes, I am still beautiful. Yes, I did have to replace my wardrobe."
    BBW "But that isn't something to dwell on, we have our date tonight."
    MC "Alice, if you want to postpone our date, that is fine."
    show BBW angry
    BBW "Keisuke!"
    show BBW sad
    BBW "Sometimes a woman wants to be treated well. Made to feel special."
    show BBW neutral
    BBW "A night out will take my mind off... other things."
    "I could see she had her mind made up"
    MC "All right, then."
    MC "Shall we be off?"
    BBW "We shall. What do you have planned?"
    "Such an easy question, but I had spent the past few days agonizing over it."
    "Alice has expensive tastes, but I'm not the guy to meet them."
    "Going over my meager savings, plus what I had scraped together working for her, I had enough for a nice meal out at what the town had in the way of an upscale restaurant."
    "It would make a good first date, but I couldn't take her back anytime soon."
    "On the other hand, if I was more economic I could stretch my money further and take her out more often. Just not to the costlier places."
    MC "I thought about it, and I figured why not..."
    menu:
        "Some place cozy? Stop at a cafe and then a stroll around the town.":
            $setFlag("BBW031_cafe")
        "Something special? Reservations at the restaurant in town.":
            $setFlag("BBW031_restaurant")
    BBW "Sounds delightful."

    scene Hill Road with fade
    show BBW happy
    "We decided to walk to town instead of waiting for the bus. The weather was accommodating and this would give us a chance to talk."
    "Only at first we couldn't think of anything to talk about except classes and papers coming due."
    BBW "I wanted to say, you've been really great with your deliveries."
    BBW "Repeat business is currently 16%% above the rate of equivalent companies, and that might be due to our monopoly-"
    MC "Alice?"
    BBW "?"
    MC "Let's not talk about work today."
    MC "We're not out here as employer/employee, right?"
    show BBW neutral
    "She grimaced a bit, but recovered quickly."
    BBW "You're right. Sorry."
    MC "It's all right."
    MC "..."
    MCT "Damn it, man. Think of something else to talk about."
    MCT "Something to impress her. Maybe talk about the arts, or current events."
    menu:
        "Ask if she's seen the new art film that's playing.":
            MC "Have you heard anything about Autumn Tide? I'm not the biggest fan of costume dramas, but this one looks pretty... intense."
            show BBW happy
            BBW "No, I don't get to the movies that much. What's it about?"
        "Ask what she thinks about the upcoming election.":
            MC "Did you see that analysis about the upcoming election? There's growing expectations that the domestic economy is going to be more of an issue than was first thought."
            show BBW happy
            BBW "I must have missed that. To be frank I don't pay too close attention to Japan's politics."
            MC "It doesn't seem like there're any drastic changes in store for the make-up of parliament, but the LDP might lose a bigger chunk of their majority than first thought..."
    "Having found something not related to school or work to talk about, the rest of the walk to town went by quickly."

    scene Town with fade
    show BBW neutral
    "When we got to the town I felt a brief resurgence of dread."
    "Like I needed to make an excuse for how my plans for today couldn't possibly measure up to her normal expectations."
    MC "There's not a lot to do in this town, have you noticed? Not too many places to eat, not much in the way of entertainment."
    BBW "I've noticed."
    BBW "It makes sense, I suppose. Businesses are like plants; they need the right environment to grow and thrive."
    BBW "A niche biome like this island - dedicated to the school and its student body - can only support so much in the way of capital."
    show BBW happy
    BBW "Still, there's something pleasant in the quaintness of it all."
    MC "Yeah..."
    "We walked through the town, the streets not too crowded, and came to..."

    if getFlag("BBW031_cafe"):
        jump BBW031_cafe
    else:
        jump BBW031_rest

label BBW031_cafe:
    scene Cafe with fade
    "The cafe."
    "I had worried the place would be too busy when we got there - having to stand in line for too long or talking over a dozen other conversations would ruin the mood - but the place was mostly empty."
    "We went up to the counter, and as I scanned the menu Alice asked"
    show BBW happy with dissolve
    BBW "What selection of blends do you have?"
    Waitress "I'm sorry, but we only have one kind of coffee."
    Waitress "It's a French roast. It's very good."
    Waitress "And we do have an espresso machine."
    show BBW neutral
    BBW "Coffee is fine."
    MC "I'll have a coffee as well. Do you want a pastry or anything?"
    BBW "Sure. I'll have..."
    "She looked over the display case, her expression souring slightly."
    BBW "I'll have a cheese danish."
    MC "I'll have a chocolate croissant."
    "When the cashier rang us up I reached for my wallet, and at the same time I saw Alice opening her purse."
    "Time slowed down. Should I pay for her order, as is tradition, or should I let her cover her half? She has the money, after all."
    menu:
        "Pay for Alice.":
            MC "It's all right. I got it."
            "To cut her off, I jerked my wallet out and snatched a couple bills. I had to stop and double-check them to make sure they were the right amount."
            show BBW happy
            BBW "Nice to see chivalry isn't dead."
        "Let Alice pay for her order.":
            "I moved a little slower as I took my wallet out, giving Alice a chance to open her purse."
            "She stopped before she withdrew her own money, turning to me."
            BBW "Shall we each pay for ourselves?"
            MC "I'm a modern guy, but if you want to do it the old-fashioned way..."
            BBW "No, it's fine."
            BBW "I don't mind paying my own way."
    hide BBW with dissolve
    "We took our coffees and pastries to a corner table in the back."
    "At the last second I remembered to pull her chair out for her."
    show BBW happy with dissolve
    BBW "Oh! Thank you."
    "I'd never done that before on a date, but I didn't think the informal approach would fly with Alice."
    "I wondered if I had scored points for that move, or if she expected something like that."
    show BBW neutral
    BBW "Mmmm. The coffee's not terrible."
    "I took a sip before agreeing."
    "Truth be told, I didn't have a particular taste for coffee, but it was alright."
    BBW "Still, you would expect a cafe to have some variety of choice."
    MC "Do you have a favorite type of coffee?"
    show BBW happy
    BBW "I'm rather fond of Sumatran blends. And I do enjoy some Guatemalans."
    BBW "Oh! There's an idea."
    BBW "We can start selling exotic coffee blends through our company."
    MC "Alice..."
    "I put as much 'stern' into my voice as I could manage."
    show BBW neutral
    BBW "Sorry. No business."
    "She took another sip of her coffee, and I did likewise."
    "I tried to think of something else to talk about. Something neutral."
    "Dates are supposed to be the time to get to know the other person, right? Anything should be on the table."
    "I eventually settled on the most mundane thing."
    MC "How's your danish?"
    BBW "It's also not bad."
    MC "But not what you're used to?"
    BBW "I wouldn't put it that way."
    BBW "I am accustomed to more enticing fare, but I don't lack the stomach for the simple."
    BBW "It doesn't speak well for the owners of this place, though. Having the market cornered is no excuse for mediocre offerings."
    BBW "I've seen other examples of this, monopolization leading to a drop in quality."
    MC "Sounds like you don't approve."
    MC "I guess because you enjoy the finer things you want other people to experience them to?"
    show BBW happy
    BBW "Exactly!"
    BBW "I mean, there are some things where scarcity is unavoidable, in which case only those who appreciate it should enjoy it."
    BBW "But fine food isn't the same as an unspoiled beach."
    MC "But isn't the talent or knowledge to make a high-class dish scarce? There are only so many people who go to cooking schools."
    "Our conversation went on from there."
    "Alice argued that if people demanded better cuisine there would be more of a market for real restaurants, not fast food places. And I brought up things like the need for quick-service food that was affordable."

    scene Town with fade
    #time = dusk
    show BBW neutral
    "The conversation ran off on its own tangents from there. Even when we were done with our food we were still chatting as we left the cafe and started walking around the town."
    "I don't know about Alice, but I didn't realize how late it was getting until the streetlamps turned on."
    jump BBW031_afterdate

label BBW031_rest:
    scene Restaurant with fade
    "The restaurant."
    "I had worried the place would be too busy when we got there - even though it was still early, I didn't want to have to compete with a dozen other conversations - but the place was mostly empty."
    "There was a podium just inside the entrance, though not a full-time hostess."
    "A waitress greeted us, I gave her my name, and she showed us to a table."
    "At the last second I remembered to pull Alice's chair out for her."
    show BBW happy
    BBW "Oh! Thank you."
    "I'd never done that before on a date, but I didn't think the informal approach would fly with Alice."
    "I wondered if I had scored points for that move, or if she expected something like that."
    "As we looked over our menus Alice chuckled quietly."
    MC "What?"
    BBW "Oh, it's just..."
    BBW "I haven't seen many Italian restaurants in Japan, and when I first noticed this place I was surprised."
    BBW "But then I guessed it was only the decor, everything designed to give it an Italian flavor."
    BBW "And indeed, the menu is pan-European, with what looks like the American version of group-sized pizzas."
    MC "Oh."
    BBW "I can see why they do it this way."
    BBW "A uniform motif for the restaurant itself is more professional than something more... schizophrenic."
    BBW "You wouldn't believe how chaotically some of the restaurants in America are decorated."
    MC "I guess with the menu their thinking is 'There aren't that many choices in town.' Variety only helps there."
    BBW "Perhaps."
    MC "Not that many people would be upset that an Italian restaurant has..."
    "I struggled to think of something from French cuisine."
    MC "...French bread."
    BBW "No. Though under any other circumstances I would have very high expectations for their alfredo sauce."
    BBW "As simple as it is, it's a favorite of mine."
    BBW "There was one time, a few years ago, when we were in Tuscany..."
    "I thought she was about to go into an anecdote, but as she gazed off into the distance her eyes suddenly went wide."
    BBW "Oh! I just thought of something perfect."
    BBW "Have you ever heard of DeLuca candies?"
    MC "No. What are they?"
    BBW "They're these hard candies made in Italy, with a gooey center. They come in different fruit flavors."
    BBW "They're really good, and they're really popular over there, but I've never seen them outside of Italy."
    BBW "What if we started selling them here?"
    "I did my best to silently scold her, trying to recreate the same look my mother would give my sister or me whenever we were skating on thin ice."
    "She got the hint."
    show BBW neutral
    BBW "Right. Sorry. No work today."
    "Before either of us could help the conversation recover from that moment of awkwardness, our waitress arrived."
    "We took a moment to decide on our orders, and then we were left alone again."
    MC "So you've been to Italy."
    show BBW happy
    BBW "My father's business took him there, so he brought Mom and me and turned it into a vacation."
    "She didn't need much prodding to keep going, and until our food arrived she told me about hiking through Tuscany and the canals of Venice."
    "I found my paella to be pretty good. I didn't have any frame of reference to compare it to."
    "But Alice wasn't that impressed with her linguine in alfredo sauce."
    MC "Is your food okay?"
    show BBW neutral
    BBW "It's fine. Exactly what I was expecting, if that doesn't sound too critical."
    MC "Just not what you're used to?"
    BBW "I wouldn't put it that way."
    BBW "I am accustomed to more enticing fare, but I don't lack the stomach for the simple."
    BBW "It doesn't speak well for the owners of this place, though. Having the market cornered is no excuse for mediocre offerings."
    BBW "I've seen other examples of this, monopolization leading to a drop in quality."
    MC "Sounds like you don't approve."
    MC "I guess because you enjoy the finer things you want other people to experience them to?"
    show BBW happy
    BBW "Exactly!"
    BBW "I mean, there are some things where scarcity is unavoidable, in which case only those who appreciate it should enjoy it."
    BBW "But fine food isn't the same as an unspoiled beach."
    MC "But isn't the talent or knowledge to make a high-class dish scarce? There are only so many people who go to cooking schools."
    "Our conversation went on from there."
    "Alice argued that if people demanded better cuisine there would be more of a market for real restaurants, not fast food places. And I brought up things like the need for quick-service food that was affordable."

    scene Town with fade
    #time = dusk
    show BBW neutral
    "The conversation ran off on its own tangents from there. We were still chatting as we left the restaurant, and I would have enjoyed just walking around the town and talking."
    "But I hadn't realized how late it was. Right as we stepped into the fresh air the streetlamps all turned on."
    jump BBW031_afterdate

label BBW031_afterdate:
    MC "Oh, wow. It's almost night."
    MC "We should probably get back to campus, huh?"
    show BBW angry
    BBW "Yes. We wouldn't want the day spoiled being chewed out by Madame Presidente."
    menu:
        "Agree with Alice":
            MC "Yeah. Sticklers like her have a tendency to squash other people's fun, even if they don't mean to."
        "Defend Shiori":
            MC "Shiori's not the worst stickler I've ever met. I'd say she's reasonable most of the time."
    show BBW neutral
    BBW "Quite."
    show BBW happy
    BBW "Still, if not her then one of the teachers might come down on us. Let's not give them the excuse."
    "We headed back to campus, our conversation dying down as we took in the twilight."
    MC "The island isn't that developed, other than the school and town."
    BBW "No."
    MC "I haven't seen this much nature in one place in... Don't know how long."
    MC "Probably when I went camping as a kid."
    BBW "There's a forest in southern-"
    "And suddenly Alice was falling towards me."
    "I caught her... Or rather, when she fell against me I braced myself and kept us from both sprawling on the ground."
    show BBW angry
    BBW "Sorry. There was a rock..."
    MC "Are you hurt?"
    BBW "No, just..."
    "I helped her stand back up, suddenly aware of my arm reaching around her back."
    "She felt soft, like I expected, but also a little bit firm."
    MCT "I wonder what she'll say if I don't move my arm."
    menu:
        "Leave the arm there.":
            MC "Can you stand? You didn't sprain your ankle or anything, did you?"
            show BBW neutral
            BBW "No, I'm not hurt."
            "Tentatively, she put her weight on both legs. She seemed fine."
            show BBW happy
            BBW "I think I'll be fine on my own."
            "The way she smiled I could see she wasn't bothered by my being so close. But I guess she didn't want to get too familiar on the first date."
            "So I stepped back, returning the smile and (hopefully) not coming across as a creep."
        "Give her space.":
            "I stepped back slowly, making sure she wasn't about to fall again."
            MC "Can you stand? You didn't sprain your ankle or anything, did you?"
            show BBW neutral
            BBW "No, I'm not hurt."
            "Tentatively, she put her weight on both legs. She seemed fine."
    show BBW happy
    BBW "Sorry about that."
    MC "No worries."
    BBW "Now and then I feel a little out of sync with my own body."
    show BBW neutral
    BBW "There's a bit more of me than I'm used to."
    MC "Right."
    menu:
        "Compliment her body.":
            "Even if she wasn't fishing for a compliment, there was no better opening to talk boldly about her weight."
            "It was one of the biggest worries on my mind leading up to tonight, and I have put more than a little thought into how I would seize the opportunity."
            MC "I have to say, you're carrying it well."
            MC "You're still undeniably elegant, no matter your size."
            "Admittedly, it came across as more suave in my own mind."
            "But when she rolled her eyes she also smirked a little, so I hadn't flubbed it too bad."
            show BBW happy
            BBW "Flatterer."
            BBW "But is that what you really think? You're not just feeding me a line?"
            MC "No, I mean it."
            BBW "Uh-huh. And how elegant was I when I was falling onto you?"
            MC "Well... OK, you were clumsy just then."
            MC "But I'm not about to complain about feeling you pressed against me like that."
            show BBW surprised
            BBW "!"
            "That was bolder than I was planning, but it was worth it to see Alice stunned like that."
            "She recovered quickly, though. No surprise."
            show BBW happy
            BBW "That's more than flattery."
            BBW "But it's also the right thing to say."
        "Ask how she's managing with her extra weight.":
            $setFlag("BBW031_muscle")
            MC "Are you... gaining weight faster than you can manage?"
            BBW "Not quite."
            BBW "I've been told my body will acquire muscle a bit easier than most people, if only from carrying around all this weight."
            BBW "I simply need to stay dedicated to my workout routine."
            MC "That's good."
            MC "I do have to say, I think you look quite nice with your extra curves."
            MCT "D'oh."
            "This had been one of my biggest concerns for today, the subject of Alice's body."
            "I had tried to think of just the right thing to say to get across that I find her attractive - sexy, even - at her current size."
            "This wasn't how I had planned it, though. 'Quite nice'?"
            "Maybe I should have gone with stunning, like I had thought of first."

    scene Dorm Exterior with fade
    show BBW neutral
    "We finished the return trip in relative silence."
    "I walked Alice to the girl's dorm, and would have offered to walk her to her room if Shiori wasn't in sight."
    MC "Guess this is where we call it a night."
    show BBW happy
    BBW "Looks like."
    BBW "I had a good time, Keisuke. Aside from the near-tumble."
    BBW "I'd love to do this again. Soon."
    MC "Sure!"
    "For the last time that night I told myself to calm down."
    MC "Yeah. I'd like that."
    "I watched her go into the girls' dorm, then casually made my way back to my room."
    "Well past midnight I was lying in bed, replaying the date in my head."
    "Had I done the right things, said the right things? Had her view of me changed in any dramatic way?"
    "What should I do differently next time? Be more bold? Play it cool?"
    "Eventually I told myself I could figure it out later. For now I needed sleep."
    jump daymenu

label BBW032:
    #Time: Afternoon
    $setProgress("BBW", "BBW034")
    scene Classroom with fade
    play music Hallway
    "Alice and I were on clean-up duty after class."
    "We were both focused on our work, not trying to make conversation or anything. But as we did so, my attention kept drifting over to Alice."
    if getAffection("BBW") < 10:
        "I wanted to make sure she was doing her share of the work."
    elif getAffection("BBW") < 19:
        "Not that I was peeping or anything, just..."
        "I just wanted something to look at besides the floor."
        "Honest."
    else:
        "Not that I was perving on her or anything, just..."
        "OK, maybe I was perving a little."
    "She finally caught me sneaking a glance one too many times."
    if getAffection("BBW") < 10:
        show BBW angry at Position(xpos=0.2, xanchor=0.5, yanchor=1.0) with dissolve
        BBW "What?"
        MC "Nothing."
    else:
        show BBW happy at Position(xpos=0.2, xanchor=0.5, yanchor=1.0) with dissolve
        BBW "What are you looking at?"
        MC "Nothing. Just..."
        BBW "Admiring the scenery?"
        "She said it teasingly, so I tried to return the volley."
        MC "It is a majestic view."
        MCT "Oof. I could have done better."
    "Alice rolled her eyes, then went back to wiping down the desks."
    hide BBW with dissolve
    "When she bent over to grab a fresh towel her expression soured, and she let out a frustrated grunt."
    MC "Are you all right?"
    "She waited until she was upright again, inhaling sharply."
    show BBW neutral at center with dissolve
    BBW "I'm fine."
    "Her attempt to be convincing was undermined by the irritation still evident in her tone."
    "When she saw I didn't accept her response - I guess my own expression gave me away - she sighed and continued."
    BBW "I'm not used to my middle being quite so thick."
    BBW "Bending over is more difficult than it used to be. Not impossible, but the added difficulty is a reminder of my condition."
    MC "Condition."
    BBW "Hmm?"
    MC "You called it a condition."
    BBW "Yes. It's not something under my control. It's going to happen no matter what."
    BBW "What do you call that, if not a condition?"
    MC "Sounds rather negative."
    BBW "It's not exactly welcome."
    "As I tried to think of an appropriate thing to say, the silent pause was broken by a deep gurgling sound."
    "I didn't realize what it was at first, until I saw Alice blushing."
    if getAffection("BBW") < 10:
        MC "If we hurry up we can finish this soon, and you can get something to eat."
        show BBW angry
        BBW "I am working, Hotsure-san. And I'm not so gluttonous I can be motivated by the promise of food."
        MC "Right! Right! I didn't mean to imply anything."
        MC "Um..."
    else:
        MC "Do you want to get a snack after we're done here?"
        "She frowned, but just for a second."
        BBW "That wouldn't be bad."
    MC "I've been wondering, and don't take this the wrong way, but has your appetite, you know, gotten bigger?"
    show BBW neutral
    "She didn't say anything at first, as if she was ignoring me."
    MC "Of course, I know you're not some food-obsessed pig."
    MC "But it's expected, even ordinary, that people going through puberty get bigger appetites as their bodies grow."
    BBW "It is customary. The body needs more calories in such circumstances."
    BBW "And my condition is similar to a second puberty."
    BBW "To answer your question, yes. I have experienced an increased appetite as of late."
    MC "Oh."
    MC "Okay. I was just curious."
    "We continued working, the silence more noticeable than it was before."
    BBW "And as you correctly surmised, I am not a food-obsessed pig."
    BBW "I still have my palate. My appreciation for food has not diminished, even as I crave more of it."
    MC "Of course."
    "More silence."
    "I wanted to say something. To break the silence, and to prevent Alice from thinking I only saw her as 'a fat woman.'"
    "But wouldn't she see through me if I tried to change the conversation?"
    "A bolder act would probably be safer."
    jump BBW032_c1

label BBW032_c1:
    menu:
        "Ask how big she thinks she'll get." if not getFlag("BBW032_c1_1"):
            jump BBW032_c1_1
        "Ask how big she thinks she'll get. (disabled)" if getFlag("BBW032_c1_1"):
            jump BBW032_c1_1
        "Ask if she's working out to help deal with her body." if not getFlag("BBW032_c1_2"):
            jump BBW032_c1_2
        "Ask if she's working out to help deal with her body. (disabled)" if getFlag("BBW032_c1_2"):
            jump BBW032_c1_2
        "Comment about Renaissance art and female nudes." if not getFlag("BBW032_c1_3"):
            jump BBW032_c1_3
        "Comment about Renaissance art and female nudes. (disabled)" if getFlag("BBW032_c1_3"):
            jump BBW032_c1_3
        "I'm sure your growth will level off soon." if getFlag("BBW032_c1_1") or getFlag("BBW032_c1_2") or getFlag("BBW032_c1_3"):
            jump BBW032_c1_after

label BBW032_c1_1:
    $setFlag("BBW032_c1_1")
    MC "Do you have any idea how big you'll get?"
    MC "I imagine it would be easier to deal with if you knew what to expect."
    show BBW neutral
    BBW "I've already looked into my condition, the actual medical diagnosis, though the amount of literature about it is scant."
    BBW "Obesity is hardly a new discovery, and until recently few attempts have been made to diagnose it as something genetic, rather than the result of diet or environment."
    BBW "I would say most of the solid information I've been able to find has come from examining the other students here with the same condition as me."
    BBW "It has given me a rough estimate of what is possible in terms of growth. Which has not been positive."
    BBW "There are a number of both men and women who are much fatter than I have ever seen in real life. Fortunately their health and mobility do not seem impacted."
    show BBW sad
    BBW "Though naturally I am holding out hope I end up on the lower end of the scale."
    MC "I understand."
    jump BBW032_c1

label BBW032_c1_2:
    $setFlag("BBW032_c1_2")
    if getFlag("BBW032_muscle"):
        MC "You mentioned you had a workout routine to help build muscle, right?"
    else:
        MC "Have you been working out to help deal with your weight, or are you building muscle naturally?"
        MC "Like, is your body adapting to your new weight?"
    show BBW neutral
    BBW "I have been making a point to be more active, yes. Not that I was a layabout before coming here and learning of my condition."
    MC "No, of course not."
    BBW "But I don't want to simply trust that my body will adjust to any excess weight."
    MC "And how's that going?"
    BBW "For the most part, well."
    BBW "Finding time to fit regular workouts into my schedule has required some finessing."
    if getFlag("BBW_working"):
        show BBW happy
        BBW "Your help with the requisition business has been a significant boon. Thank you for that."
        MC "No problem."
    show BBW neutral
    BBW "And it is hard to stay motivated when I'm feeling sore and fatigued, but I do believe the results are there."
    BBW "Notwithstanding the problems bending over or the loss of nimbleness because of my acquired..."
    MC "Padding?"
    BBW "Quite."
    BBW "Notwithstanding that problem, I have not experienced any inhibition when it comes to mobility or agility."
    MC "That's good."
    MC "You're keeping control of your body."
    show BBW haughty
    BBW "Of course. I can handle any problem with dedication and willpower."
    jump BBW032_c1

label BBW032_c1_3:
    $setFlag("BBW032_c1_3")
    MC "I was reading something online recently. Did you know that back around the Renaissance the women featured in paintings were thicker than you see in media today?"
    show BBW haughty
    "She looked at me with a mildly smug expression, and I realized at once I wasn't telling her anything new."
    BBW "You're referring to artists such as Rubens?"
    if getSkill("Art") >= 8:
        MC "Yeah. Rubens was one of the ones named. Also Titian."
        MC "I just thought it was interesting that the standard of beauty can change."
        MC "Who knows, maybe things will swing back around?"
        show BBW happy
        BBW "Heh."
        BBW "Do you know why the old masters painted heavier women?"
        MC "Oh! Because the people with money to commission portraits were also usually rich enough to eat more and didn't need to toil away in the fields?"
        BBW "Correct."
        MC "Then what if you got a bunch of commissions of yourself and helped change public perception back?"
        "She chuckled at the suggestion."
        BBW "There's an idea. I wouldn't mind a portrait of myself in the classic style."
        $setAffection("BBW", 1)
        BBW "Maybe as a figure from antiquity, or ancient mythology."
    else:
        MC "Was he one of those artists?"
        show BBW neutral
        "A look of disappointment flashed across her face."
        BBW "His work is associated with heavier women, to the point that the term 'Rubenesque' is a common enough descriptor."
        BBW "I guess the term isn't used in Japan."
        MC "No. I've never heard that."
        show BBW haughty
        BBW "Back in Rubens' day, the arts were more of a patronage system."
        BBW "Wealthy merchants and royals commissioned portraits, and those who could afford it also tended to be people who could eat richly and didn't have to spend all day working in the fields."
        BBW "Thus the 'well-fed' look became a sign of wealth and privilege, and works of art from the time reflected that."
        MC "Oh. I didn't realize that."
        MCT "I guess I should make sure I know what I'm talking about before I try to show off a bit of knowledge."
    jump BBW032_c1

label BBW032_c1_after:
    MC "I'm sure your weight will level off soon."
    MC "None of the other students here have gotten too fat to live a fulfilling life, from what I've seen."
    show BBW neutral
    BBW "Hmm..."
    BBW "'Too fat' is a relative term."
    MC "I guess. But it's not like you were an aspiring track star or..."
    MCT "Don't say 'actress' or 'pop star' or anything like that. Nothing that relies on conventional beauty standards."
    MC "Or... museum tour guide."
    MCT "Ouch. I'm actually hurting over how stupid that was."
    BBW "..."
    BBW "I think I understand what you were trying to say."
    show BBW haughty
    BBW "No, my path was not one that relied on any form of physical ability or conditioning."
    BBW "I am still my father's daughter, destined to become a titan of business. A few extra kilos will not impede me."
    MC "Yeah."
    "The mood seemed noticeably lighter as we finished cleaning up."
    if getAffection("BBW") < 10:
        "We parted ways after we were done, Alice to find Aida and me back to my dorm."
    else:
        "We headed to the cafeteria when we were done to grab a snack, Alice dominating the conversation with her thoughts about a film she had recently seen."
        "I didn't have anything to contribute to that, but I liked listening to her talk about something she enjoyed."
    jump daymenu

label BBW033:
    #Time: Morning
    scene Classroom with fade
    "I came to class thinking today would be no different than any other day, which in turn made me reflect how quickly I had gotten used to... all this."
    "I mean, for myself the knowledge of growth factors didn't mean much. I could stand to go to the barber more often, but really... My life hadn't changed."
    "And even being surrounded by ladies who were getting improbably busty or tall or whatever didn't elicit so much as a second glance."
    "So when I entered the class and saw a very heavy woman arguing with a very muscled woman, my only thought was how the morning's peace was going to be broken by their bickering."
    play music Tension
    show BBW angry at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    BBW "I do not care to repeat myself, and asking again is not going to result in a different answer."
    show FMG angry at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    FMG "At least give me a reason. Would it kill you to not act like a selfish-"
    if getAffection("BBW") >= getAffection("FMG"):
        jump BBW033_BBW
    else:
        jump BBW033_FMG

label BBW033_BBW:
    "Akira was cut off when Alice noticed my arrival and turned to me."
    BBW "Keisuke, can you talk some sense into this woman? I am quickly running out of patience."
    MC "What's the issue?"
    FMG "I just want-"
    BBW "Ms. Mizutani asked if she could borrow a certain garment of mine, I said no, and she will not let matter drop."
    FMG "You won't even explain why, though."
    BBW "Must I? Must I justify the decisions I make concerning my own property?"
    menu:
        "You can at least give her a reason. Saying 'No' just because comes across as rather petty.":
            jump BBW033_BBW_1 #(+1 Alice)(+1 Akira)
        "If she said 'No,' Akira, you should just accept it. She doesn't have to give a reason.":
            jump BBW033_BBW_2 #(-1 Akira)

label BBW033_BBW_1:
    stop music
    FMG "Yeah Alice, it's common courtesy."
    play music Peaceful
    show BBW neutral
    BBW "Very well."
    BBW "The fact is, the article in question was tailored to me specifically. To my proportions."
    BBW "Just because it is... 'expansive' does not mean it's suitable for any plus-sized woman."
    BBW "You don't have the right figure for it, Mizutani-san."
    show FMG sad
    FMG "Oh..."
    FMG "I hadn't thought about that."
    show BBW happy
    BBW "If you would like something appropriate for this special occasion (whatever it may be), I would happy to procure a dress better-suited to you."
    BBW "My business caters to men and women of all dimensions."
    FMG "No. I don't have money for that. That's why I needed to borrow something."
    FMG "It's OK. I'll figure something else out... hopefully."
    hide FMG with dissolve
    show BBW happy at center with dissolve
    $setAffection("BBW", 1)
    $setAffection("FMG", 1)
    BBW "Thank you for your help, Keisuke."
    MC "It was really nothing. People like it when you give them a reason for rejection."
    MC "You can't just say 'Because I said so.' I think any parent could tell you that never works."
    "She raised an eyebrow."
    BBW "Really? I never had trouble acquiescing to my parent's authority."
    "There were several ways I could have responded to that, but Tashi-sensei walked in at that point, so I bit my tongue and found my seat."
    jump daymenu


label BBW033_BBW_2:
    "Akira didn't get any angrier, but having her glare at me instead of Alice was chilling."
    FMG "Of course you'd take her side."
    $setAffection("FMG", -1)
    stop music
    FMG "Fine! Forget I even asked."
    play music Peaceful
    hide FMG with dissolve
    show BBW neutral at center with dissolve
    "Alice clucked her tongue."
    BBW "Most unbecoming. Rejection is an inevitability in life, but disappointment only comes when we open the door to it."
    MC "Maybe you should have just told her why you turned her down."
    BBW "Why? I already said I don't have to justify myself."
    MC "Yeah, but-"
    "And that's when Tashi-sensei walked in, so I shut my mouth and found my seat."
    MCT "Maybe I shouldn't have taken Alice's side so readily."
    jump daymenu

label BBW033_FMG:
    "She cut herself off when she saw me."
    FMG "Keisuke, help me out here."
    FMG "I just asked Queen Belly-"
    #[Crash SFX]
    #[Screen shakes]
    BBW "Grrrr!"
    FMG "...if I could borrow a dress of hers for our date, and she won't even give me a reason why not!"
    BBW "As if I'm going to help you out after insulting me like that."
    menu:
        "Just tell her why not. I'm sure she'll drop the matter if you give her a reason.": #(+1 Alice)
            jump BBW033_FMG_1
        "Saying 'I don't wanna' sounds childish.": #(-1 Alice)
            jump BBW033_FMG_2

label BBW033_FMG_1:
    if getAffection("BBW") < 6:
        MC "Alice-"
        BBW "Nikumaru-san. Let's observe propriety while we're in class."
        MC "OK. Nikumaru-san, can you just tell her why not? I'm sure she'll drop the matter if you give her a reason."
    else:
        MC "Alice, can you just tell her why not? I'm sure she'll drop the matter if you give her a reason."
    stop music
    "She exhaled slowly."
    play music Peaceful
    show BBW neutral
    $setAffection("BBW", 1)
    BBW "Very well."
    BBW "If you must know, I do not believe the dress would flatter Mizutani-san."
    BBW "It was designed for me personally, for my proportions."
    jump BBW033_FMG_after

label BBW033_FMG_2:
    MC "Saying 'I don't wanna' sounds childish."
    MC "You could at least say why you don't want to."
    $setAffection("BBW", -1)
    stop music
    BBW "You want to know why not?"
    play music Peaceful
    BBW "It's because Mizutani is much too bulky to wear the dress."
    FMG "Hey! You're no stringbean yourself."
    BBW "My body may have a little extra here and there-"
    FMG "A lot of extra everywhere, you mean."
    BBW "-which is why I've had my clothes specially made to suit me."
    jump BBW033_FMG_after

label BBW033_FMG_after:
    show FMG neutral
    FMG "Yeah, so it should be big enough to fit me."
    show BBW angry
    BBW "Grrr..."
    show BBW neutral
    BBW "That is not how clothing works. Not everything is designed to be stretchy like tracksuits or yoga pants."
    FMG "Couldn't I at least try it on? It can't be that tight on you, otherwise you'd rip-"
    show BBW angry
    BBW "Grrr..."
    MC "I think what Akira means to say is that your outfits probably have a certain amount of give."
    MC "And with a little work the dress can be adapted to suit her. We could find video tutorials online to help with that."
    BBW "You can't just take 'No' for an answer."
    FMG "Hey, I don't work for you."
    MC "If there's a solution to your objection it's worth trying to work around it."
    show BBW neutral
    BBW "Why don't you just buy a dress that would fit you? I sell clothing for men and women of all dimensions."
    show FMG sad
    FMG "I don't have money for that."
    MC "Think of it as a test-drive. Akira could buy something else later once she sees how fashionable your inventory is."
    show FMG happy
    FMG "Yeah! Think of it like a test-drive."
    if getAffection("BBW") < 6:
        BBW "Well-played, Hotsure-san."
    else:
        show BBW happy
        BBW "Well-played, Keisuke."
    show BBW neutral
    BBW "Very well. Consider this a free trial of the wares the Nikumaru Outlet Direct has for offer."
    FMG "Sweet, thanks Alice!"
    "Tashi-sensei showed up then, so we tabled the conversation as class started."
    stop music

    scene Hallway with fade
    "After class Alice and Akira went to the former's dorm and Akira tried on the dress."
    "Alice said she knew a few tricks for making loose or oversized garments fit better, pinning up excess fabric in ways that didn't show."
    "I thought the matter was solved, trying to imagine how Akira would look dressed up."

    scene Cafeteria with fade
    "But when I went to the cafeteria for dinner I found out things hadn't worked out like I'd hoped."
    play music Tension
    show BBW angry with dissolve
    BBW "Hotsure-san!"
    MC "Gah!"
    MC "What?"
    show BBW angry at Position(xpos=0.25, xanchor=0.5, yanchor=1.0) with dissolve
    show FMG sad at Position(xpos=0.75, xanchor=0.5, yanchor=1.0) with dissolve
    BBW "My custom-made Vantelli dress. Ruined!"
    FMG "I said I was sorry."
    MC "I take it the dress didn't fit?"
    BBW "No, it fit. I made it work."
    BBW "But your girlfriend apparently thought that she could compete in a decathlon while wearing a designer evening gown."
    show FMG angry
    FMG "Hey! All I did was bend over."
    BBW "You can't make any sudden movements while wearing a dress like that!"
    BBW "You have to move elegantly. Slow, sweeping motions."
    show FMG sad
    FMG "Well I know that now."
    MCT "I was almost expecting her to say Akira flexed her arms and the sleeves exploded."
    MC "I'm sure Akira will make it up to you."
    BBW "She'd better."
    show FMG angry
    FMG "I will! I'll pay you back!"
    show FMG sad
    FMG "Somehow..."
    BBW "We'll see."
    BBW "Now if you'll excuse me, I need to get my seamstress on the phone. The dress may still be salvageable."
    hide BBW with dissolve
    show FMG neutral at center with dissolve
    FMG "She didn't have to take it so personally."
    MC "Well, it sounds like it was an expensive dress."
    FMG "But she's loaded."
    MC "That doesn't mean she likes throwing money away."
    FMG "I guess."
    FMG "I just thought it would have been nice to get dressed up for our date."
    MC "Yeah."
    MC "Why don't you grab yourself some food? We can have dinner together."
    "The mood improved as we ate and talked about nothing in particular, the drama with Alice forgotten."
    jump daymenu

label BBW034:
    $setProgress("BBW", "BBW035")
    #Time: Afternoon
    scene Cafeteria with fade
    "After class I went to the cafeteria to get a drink while doing the reading parts of my homework."
    "Despite the place being a somewhat popular hang-out spot after classes (I guess others had the same idea as me, free food to accompany homework), it was fairly quiet at this point."
    BBW "Keisuke!"
    "Quiet enough that Alice calling out my name resounded throughout the entire space, heads turning and Alice looking embarrassed when she reached me."
    play music BBW
    show BBW sad with dissolve
    MC "Something up? Need me to make a delivery?"
    show BBW neutral
    BBW "No."
    BBW "Though I do need your help."
    BBW "The music club is having its first concert on Friday."
    MC "I know. I'm looking forward to it."
    BBW "The head of the club has tasked me (and a couple others) with setting up the auditorium Friday afternoon."
    BBW "This conflicts with my schedule. I've already allotted time for homework and managerial matters with my requisition business."
    show BBW haughty
    BBW "Not mention doing my hair and make-up. Even if I'm one face in the chorus I still want to look my best."
    show BBW angry
    BBW "Not to mention that after being tasked with distributing fliers for the concert I feel I am being either exploited or unduly singled out. There are other capable hands to set up chairs and music stands."
    show BBW neutral
    BBW "So may I ask a favor of you?"
    MC "You want me to take your place setting up the auditorium?"
    show BBW happy
    BBW "Got it in one."
    menu:
        "Sure, I can do it.":
            jump BBW034_c1_1
        "I think it would be better if you did it yourself.":
            jump BBW034_c1_2

label BBW034_c1_1:
    MC "No problem. You've got enough on your plate as it is."
    show BBW haughty
    BBW "Excellent. I knew you were reliable."
    BBW "Be at the auditorium at 3:30 on Friday."
    stop music
    hide BBW with dissolve
    "And she left."
    "She seemed to be in a happier mood, but as I returned to my homework my own grew dimmer."
    "I remembered the thing with the fliers, and how she had asked me to help hang them up."
    "And then I considered the whole thing with Aida essentially being her lackey, for lack of a better word-"
    "Oh, hey. Inadvertent pun."
    "But no, the more I thought about it the more entitled Alice came across as."
    "It wasn't just her, though. Her behavior could be excused by having servants to wait on her, but what about me?"
    "Rolling over so easily, never mind that I have my own responsibilities."
    "It probably would have been better if I had stood up to her. Even if she thought I was being confrontational, would it be worse than being seen as a pushover?"

    scene School Planter with fade
    "I couldn't concentrate on my homework for a while, so I took a walk to clear my head."
    $setAffection("BBW", -1)
    "The more I thought about it, the more certain I was I had made the wrong choice."
    jump daymenu

label BBW034_c1_2:
    MC "You've already gotten in trouble for going against her before, haven't you?"
    MC "Do you really want to anger her again by blowing her off?"
    show BBW angry
    BBW "Why should her anger be the one to be avoided?"
    MC "In this case? Because she's the one in charge."
    MC "And you aren't."
    MC "You know this. You understand how hierarchies work."
    BBW "..."
    show BBW neutral
    BBW "Indeed."
    MC "I get that you don't approve of how she does things, but you can't climb the ladder if you burn your bridges before you even cross them."
    MC "Terrible analogy."
    BBW "Yes."
    MC "My point is, you're either going to have to hold your tongue and keep your head down or you'll be kicked out of the club."
    MC "One choice can lead to you being in a position to change things, the other doesn't."
    if getSkill("Academics") >= 9:
        MC "Plus, showing you're a team player can also help you gain points with the other members of the club."
        MC "If they see you carrying your share of the load they'll remember it when you try to become the club leader."
        MC "Instead of thinking you're only concerned with your prestige, your glory, they'll see that you want what's best for the club."
        $setAffection("BBW", 1)
    "Alice sighed, visibly relaxing."
    show BBW neutral
    BBW "Very sensible."
    show BBW happy
    BBW "It does pay to listen to cooler heads."
    BBW "You're right, Keisuke. It would be beneficial - or at least not counterproductive - to be obedient for the time being."
    show BBW neutral
    BBW "We'll have to reschedule our business meeting for Saturday then."
    MC "Oh, that's no problem."
    show BBW happy
    BBW "Good to hear."
    "She checked her watch."
    BBW "It would also help if I got a start on that biology homework."
    BBW "Removing even minor distractions will make it easier to concentrate on the larger concerns once things get busier."
    BBW "I'd recommend taking care of your responsibilities ahead of time as well, Keisuke."
    MC "I... already am."
    "I indicated the textbook in front of me."
    show BBW neutral
    BBW "Oh. Of course."
    show BBW happy
    BBW "I'll let you get back to it, then."
    stop music
    hide BBW with dissolve
    "And she left."
    "I turned back to my homework."
    "Only later did I reflect that Alice was quite reasonable about the whole thing."
    "It was good to see that she could be appealed to, even if for purely selfish reasons."
    "Still, she was more thoughtful than a basic diva would be."
    jump daymenu

label BBW035:
    $setProgress("BBW", "BBW036")
    #Time: Afternoon
    scene Classroom with fade
    "After class ended for the day I swung over to Alice's desk."
    MC "Hey, boss. Do we have a meeting today?"
    show BBW neutral with dissolve
    BBW "What's that?"
    "She looked confused, but only for the briefest second."
    "If I wasn't used to how she always looked confident and put-together I might not have even noticed that brief slip."
    BBW "Not today. The concert is tomorrow and I need to get my hair and nails done."
    show BBW happy
    BBW "I know one shouldn't put pleasure before business, but if you look at it from the perspective that, as owner and manager, I represent the company, then my putting on my best face ultimately benefits us all."
    MC "You don't have to justify it."
    MC "The concert's a big deal, you want to look good for it. Nobody would fault you for that."
    show BBW neutral
    BBW "Hmm. Yes."
    BBW "We can cover this week's business next week, at our next regular meeting."
    BBW "And now I must go. The salon in town doesn't take reservations, and I dread the wait I may be in for."
    hide BBW with dissolve

    scene Hallway with fade
    "She hurried out of the classroom, and I moseyed out at my own leisure."
    "If there was no meeting today I had some time freed up."
    MCT "So what do I do with it?"
    if getSkill("Academics") < 5:
        MCT "Take care of my homework? I'm not exactly keeping up with that."

        scene Dorm Interior with fade
        "I went back to my room and started on my homework."
        "There was a lot more than I remembered, and it ended up taking all afternoon and well into the evening."
        "But at least I had freed up the next night, so I wouldn't miss the concert."
        jump daymenu
    MCT "Take care of my homework?"
    extend " Naw. I'm on top of it all, and I should enjoy myself a little."
    MCT "Go work out? Go to the library and find a book?"
    extend " No, that doesn't really grab me."

    scene black with fade
    "As I brushed my hair out of my eyes a thought occurred."

    scene Hallway with fade
    MCT "I should clean myself up for the concert."
    MCT "I won't be on stage, but shouldn't I look nice for Alice on a night important to her?"
    "I went back to my dorm to drop off my backpack, then I headed off for town."

    scene Town with fade
    "When I got to town I had to walk around a bit before I found what I was looking for."
    MCT "Barbershop's by the arcade, and there's a menswear store by the movie theater."
    MCT "There's also a department store across from the cafe. I could probably find something to wear for less money over there..."
    menu:
        "Get a haircut." if not getFlag("BBW035_c1_1"):
            jump BBW035_c1_1
        "Get a nice suit.":
            jump BBW035_c1_2
        "Get a suit, but let's not break the bank.":
            jump BBW035_c1_3

label BBW035_c1_1:
    $setFlag("BBW035_c1_1")
    "Of course my hair was going to grow back fast enough to make anything less than a complete shearing redundant, but getting it cut to a normal length meant I wouldn't have to keep brushing it out of my eyes during the concert."
    "And the price was quite reasonable. Even with a nice tip I still had plenty left in my wallet."
    if not getFlag("BBW035_c1_2") and not getFlag("BBW035_c1_3"):
        MCT "Still have enough to get a new outfit, if I want."
        menu:
            "Get a haircut. (disabled)":
                pass
            "Get a nice suit.":
                jump BBW035_c1_2
            "Get a suit, but let's not break the bank.":
                jump BBW035_c1_3
            "That's enough for today. I should get back to campus.":
                jump BBW035_c1_after
    else:
        MCT "I should be getting back to the school."
        jump BBW035_c1_after

label BBW035_c1_2:
    $setFlag("BBW035_c1_2")
    MCT "If I'm going to get dressed up for the concert, I might as well be serious about it."
    #[A3 merges here.]
    "The menswear store didn't reek of class or money, but it still felt just fancy enough to make me uncomfortable."
    MCT "Glad I took that job for Alice. I don't think I'd be able to buy anything here with the allowance my parents are sending me."
    MCT "Well, maybe a new handkerchief."
    "I took my time looking around the shop, trying to put out of mind how much some of these suits would deplete my savings, focusing instead on what looked best."
    "In the end I was stuck trying to choose between two options."
    "There was a silver-gray suit that looked as expensive as it actually was. It looked almost too rich even for a private academy like Seichou."
    "But there was no question it would make an impression, and Alice would certainly recognize luxury like this."
    "The other choice was a dark blue number that was both more affordable and also a lot more subdued."
    "It didn't look extravagant, but I would look nice enough."
    menu:
        "The expensive suit.":
            $setFlag("BBW035_c2_1")
            "I paid for the suit, which drained most of my wallet but, pleasantly, not all of it."
        "The moderate suit.":
            $setFlag("BBW035_c2_2")
            "I still had a tidy sum in my wallet after buying the suit."
        "You know what? Maybe I should check the department store instead." if not getFlag("BBW035_c1_3"):
            MCT "I don't have to buy something at the first store I go to, do I?"
            jump BBW035_c1_3
        "You know what? Maybe I should check the department store instead. (disabled)" if getFlag("BBW035_c1_3"):
            pass
    if not getFlag("BBW035_c1_1") and not getFlag("BBW035_c1_3"):
        MCT "Still have enough to get a haircut. Or maybe there's an accessory I can find at the department store. Something to compliment the suit."
        menu:
            "Get a haircut.":
                jump BBW035_c1_1
            "Get a nice suit. (disabled)":
                pass
            "Get a suit, but let's not break the bank.":
                jump BBW035_c1_3
            "That's enough for today. I should get back to campus.":
                jump BBW035_c1_after
    else:
        MCT "I should be getting back to the school."
        jump BBW035_c1_after

label BBW035_c1_3:
    #if you did not go to the fancy store before
    if not getFlag("BBW035_c1_2"):
        "Maybe I come across as miserly for heading to the department store first, but I could always claim frugality as a virtue, right?"
        "And the store wasn't cheap or anything. There was a nice selection of polos and khakis and sports coats."
        "A fair selection of outfits for a night out, budgeted for most people's bank accounts."
        "It was all fine. Perfectly fine."
        "I found a nice pair of gray slacks and a burgundy sweater. If I wore a collared shirt under it I would be presentable but not overdressed."
        MCT "But do I want to settle for 'presentable'?"
        menu:
            "I should check out the menswear store before making a choice.":
                "While the slacks and sweater looked fine, they didn't scream at me 'This is THE outfit.'"
                "I put them back on the rack and headed to menswear store. It would probably be pricier, but I had a good feeling I'd be more satisfied with what I found there."
                jump BBW035_c1_2
            "'Presentable' is fine. I'm not the one who'll be on stage anyway.":
                $setFlag("BBW035_c1_3")
                MCT "It's not about me. I shouldn't be trying to draw attention to myself."
                "I bought the 'presentable' outfit, my wallet still nice and fat afterwards."
                if not getFlag("BBW035_c1_1"):
                    MC "Still have enough to get a haircut, if I want."
                    menu:
                        "Get a haircut.":
                            jump BBW035_c1_1
                        "Get a nice suit. (disabled)":
                            pass
                        "Get a suit, but let's not break the bank. (disabled)":
                            pass
                        "That's enough for today. I should get back to campus.":
                            jump BBW035_c1_after
                else:
                    MCT "I should be getting back to the school."
                    jump BBW035_c1_after
    #if you went to the fancy store and declined the suits
    if getFlag("BBW035_c1_2") and not getFlag("BBW035_c2_1") and not getFlag("BBW035_c2_2"):
        "Oh yes, this was all much more affordable."
        "And not in a cheap way. The slacks and jackets and shirts were all fashionable enough, to my admittedly non-fashionista eyes."
        "If you wanted to blind someone with haute couture this wasn't the place to come to, but to the average person one would come out looking sharp."
        "I found a nice pair of gray slacks and a burgundy sweater. If I wore a collared shirt under it I would be presentable but not overdressed."
        MCT "But do I want to settle for 'presentable'?"
        menu:
            "I'm going back to the menswear store.":
                MCT "Simply being there for Alice might seem like enough, but if she's getting made up for the concert I should got the extra mile myself."
                "I walked back to the menswear store and found the two suits I had been considering before."
                #[Player choice A2/B2/C2 repeats, with C2 greyed out.]
            "'Presentable' is fine. I'm not the one who'll be on stage anyway.":
                MCT "It's not about me. I shouldn't be trying to draw attention to myself."
                "I bought the 'presentable' outfit, my wallet still nice and fat afterwards."
                if not getFlag("BBW035_c1_1"):
                    MC "Still have enough to get a haircut, if I want."
                    menu:
                        "Get a haircut.":
                            jump BBW035_c1_1
                        "Get a nice suit. (disabled)":
                            pass
                        "Get a suit, but let's not break the bank. (disabled)":
                            pass
                        "That's enough for today. I should get back to campus.":
                            jump BBW035_c1_after
                else:
                    MCT "I should be getting back to the school."
                    jump BBW035_c1_after
    #if you already have a suit
    else:
        "I didn't bother looking at any of the suits or anything. I was already set on that front."
        "But there was a nice selection of hats and gloves and even canes. Accessories for the dapper gentleman enjoying a night out."
        "There was one pair of gloves that I liked, even if I had doubts about my own sense of fashion. Would they, along with my suit, be too much?"
        "As I reached the edge of the men's section of the salesfloor, I noticed a display of female mannequin heads on a counter."
        "There were necklaces and pendants on display, but something else caught my eye. A blue choker."
        "I don't know why, but it made me think of Alice. Think that it might go with her dress for the concert."
        "Assuming they were going with the school colors for their outfits..."
        "But checking the price, then checking my wallet, I saw this was an either/or choice."
        "Either I got the gloves, or the choker."
        "Or neither, of course. That was always an option."
        menu:
            "Buy the gloves.":
                $setFlag("BBW035_c3_1")
                MCT "Alice no doubt has a nice selection of jewelry and accessories already. She probably has her look for the concert picked out by now."
                "I bought the gloves, feeling okay with my purchase but just that. Okay."
                jump BBW035_c1_after
            "Buy the choker.":
                $setFlag("BBW035_c3_2")
                MC "Alice no doubt has a nice selection of jewelry and accessories already, but that doesn't mean she wouldn't like a gift like this."
                "I bought the choker, wondering if I was going too fast."
                "We'd only had one date so far..."
                MCT "Nah, it's fine."
                MCT "I want to do something nice for her. Why overthink it?"
                jump BBW035_c1_after
            "Get neither.":
                "Thinking about it, I decided neither the gloves nor the choker really jumped out to me as a 'must buy.'"
                MCT "Just because I have money doesn't mean I have to spend it, do I?"
                jump BBW035_c1_after

label BBW035_c1_after:
    "Checking my watch, I saw it was later than I expected. Time to head back."

    scene School Front with fade
    "As I reached the school grounds I saw a familiar face."
    MC "Hey, Alice! Coming back from getting your hair done?"
    show BBW happy with dissolve
    BBW "Ah, Keisuke."
    BBW "Yes. The wait was not as terrible as I feared. I was able to get my hair and nails done, and do some shopping as well."
    BBW "I found the perfect shade of lipstick for tomorrow night."
    MC "Oh? That's good."
    if getFlag("BBW035_c1_1") and getFlag("BBW035_c2_1"):
        MC "Yeah, I decided to get a haircut as well. Want to look nice myself for tomorrow."
        show BBW sad
        "Alice looked at me, tilting her head to the left, then the right."
        BBW "I guess I didn't notice, but yes... Your hair is shorter."
        show BBW neutral
        BBW "It's still a bit... untamed."
        MC "Yeah, I'm going to style it tomorrow. Get it under control."
        MC "I also got a suit to wear. Maybe it's too much for a school concert, but I figured 'Hey, it's a big night for you. I should look nice myself.'"
        show BBW happy
        "Alice's mood perked up when I mentioned buying a suit, though as I opened up my bag and pulled it her face drooped a little."
        show BBW sad
        BBW "That's... rather extravagant."
        MC "It was a bit pricey, yeah."
        BBW "How much did it cost?"
        "When I gave her the price she almost winced."
        BBW "Oh, no. That's too much."
        BBW "The suit itself is too much for the concert. That's for something like meeting a foreign dignitary."
        MC "Well, I... I wanted to look nice for your big night."
        BBW "I appreciate that, but..."
        BBW "It's always possible to overdress for an occasion."
        MC "I guess."
        MC "Probably too late to return it today. At least I have the receipt."
        "I sighed."
        BBW "I've got to go. I'll see you tomorrow."
        MC "Yeah. Tomorrow."

        scene Dorm Interior with fade
        "I went back to my dorm, hiding out there for the rest of the night."
        "I had overdone it, that was obvious."
        "I hadn't thought it would be possible to spend too much for someone like Alice. Guess I learned something there."
        "And she hadn't even noticed my haircut."
        jump daymenu
    if getFlag("BBW035_c1_1") and getFlag("BBW035_c2_2"):
        MC "Yeah, I decided to get a haircut as well. Want to look nice myself for tomorrow."
        show BBW sad
        "Alice looked at me, tilting her head to the left, then the right."
        BBW "I guess I didn't notice, but yes... Your hair is shorter."
        show BBW neutral
        BBW "It's still a bit... untamed."
        MC "Yeah, I'm going to style it tomorrow. Get it under control."
        MC "I also got a suit to wear. Maybe it's too much for a school concert, but I figured 'Hey, it's a big night for you. I should look nice myself.'"
        show BBW happy
        "As I pulled the suit out of the bag I was worried that Alice would give me a polite 'Oh, that's nice' response."
        BBW "Oh, that's nice."
        "That's not what I mean. She was being sincere."
        MC "There was a more expensive suit there, but I think it was way too fancy for a school concert."
        MC "I felt this was more appropriate for the occasion."
        $setAffection("BBW", 1)
        BBW "No, it looks perfect."
        BBW "You're going to look quite sharp tomorrow."
        MC "Thanks."
        MC "Hey, did you have dinner yet? I was going to grab something from the cafeteria."
        BBW "That sounds splendid."

        scene black with fade
        "So we grabbed dinner together."
        "She hadn't noticed my haircut, I guess that was a waste, but she did like the suit I had picked out."
        "I'll call that a win."
        jump daymenu
    if getFlag("BBW035_c1_1") and getFlag("BBW035_c1_3"):
        MC "Yeah, I decided to get a haircut as well. Want to look nice myself for tomorrow."
        show BBW sad
        "Alice looked at me, tilting her head to the left, then the right."
        BBW "I guess I didn't notice, but yes... Your hair is shorter."
        show BBW neutral
        BBW "It's still a bit... untamed."
        MC "Yeah, I'm going to style it tomorrow. Get it under control."
        MC "I was also buying an outfit for tomorrow. Nothing special, I just wanted to look presentable for your big night."
        show BBW happy
        "Alice's mood perked up when I said this."
        "But as I pulled the slacks and sweater out of the bag I was worried that she would give me a polite 'Oh, that's nice' response."
        BBW "Oh, that's... nice."
        MCT "She hates it."
        show BBW neutral
        BBW "You'll look good tomorrow."
        MC "I just wanted a change of pace from my school uniform."
        BBW "Yeah, no. It's nice."
        BBW "I have to go. I'll see you tomorrow."
        MC "Yep. Tomorrow."

        scene Dorm Interior with fade
        "Making my way back to my dorm, I felt like I hadn't done enough."
        "I don't think Alice was offended or anything by my choice, but she was clearly unimpressed."
        "And now it was too late to go back to town and find a nice outfit for tomorrow."
        "And she hadn't even noticed my haircut."
        "Should have gone that extra mile."
        jump daymenu
    if getFlag("BBW035_c2_1") and getFlag("BBW035_c3_2"):
        MC "I'm coming back from town myself. Was buying a suit for tomorrow."
        MC "Maybe it's too much for a school concert, but I figured 'Hey, it's a big night for you. I should look nice myself.'"
        "As I opened up my bag and pulled out the suit Alice's face drooped a little."
        show BBW sad
        BBW "That's... rather extravagant."
        MC "It was a bit pricey, yeah."
        BBW "How much did it cost?"
        "When I gave her the price she almost winced."
        BBW "Oh, no. That's too much."
        BBW "The suit itself is too much for the concert. That's for something like meeting a foreign dignitary."
        MC "Well, I... I wanted to look nice for your big night."
        BBW "I appreciate that, but..."
        BBW "It's always possible to overdress for an occasion."
        MC "I guess."
        MC "Probably too late to return it today. At least I have the receipt."
        "I sighed."
        BBW "I've got to go. I'll see you tomorrow."
        MC "Wait. Before you go, I also bought this."
        "I reached into the bag and fished out the choker."
        show BBW neutral
        BBW "Oh! This is nice."
        MC "If your music club is anything like at my old school you're all wearing the same outfit, but you can still stand out with the right accessory."
        MC "That's what I was thinking, at least."
        $setAffection("BBW", 1)
        BBW "Thank you."
        BBW "You shouldn't have spent so much for that suit, but I appreciate this."
        BBW "I'll wear it tomorrow night."
        BBW "I have to go take care of some stuff right now, but I'll see you tomorrow."
        MC "Sure. Looking forward to it."

        scene Dorm Interior with fade
        "I went back to my dorm, feeling neither great nor terrible."
        "Clearly I had overdone with the suit. Apparently it is possible to spend too much with someone like Alice."
        "But she liked the choker, so that had to be worth something. Even if only to offset my mistake with the suit."
        "Call it a draw, I guess?"
        jump daymenu
    if getFlag("BBW035_c2_2") and getFlag("BBW035_c3_1"):
        MC "I'm coming back from town myself. Was buying a suit for tomorrow."
        MC "Maybe it's too much for a school concert, but I figured 'Hey, it's a big night for you. I should look nice myself.'"
        "As I pulled the suit out of the bag I was worried that Alice would give me a polite 'Oh, that's nice' response."
        show BBW happy
        BBW "Oh, that's nice."
        "That's not what I mean. She was being sincere."
        MC "There was a more expensive suit there, but I think it was way too fancy for a school concert."
        MC "I felt this was more appropriate for the occasion."
        $setAffection("BBW", 1)
        BBW "No, it looks perfect."
        BBW "You're going to look quite sharp tomorrow."
        MC "Thanks. I also bought these gloves to go with it. Do you think they're too much?"
        "Alice winced a little when she saw them."
        show BBW neutral
        BBW "I would say those are for a more elegant occasion."
        MC "I guess you're right."
        MC "Hey, did you have dinner yet? I was going to grab something from the cafeteria."
        show BBW happy
        BBW "That sounds splendid."

        scene black with fade
        "So we grabbed dinner together."
        "Alice again complimented the suit I had picked, but I could tell the gloves were too much."
        "Still, I'll call that a win."
        jump daymenu
    if getFlag("BBW035_c2_2") and getFlag("BBW035_c3_2"):
        MC "I'm coming back from town myself. Was buying a suit for tomorrow."
        MC "Maybe it's too much for a school concert, but I figured 'Hey, it's a big night for you. I should look nice myself.'"
        "As I pulled the suit out of the bag I was worried that Alice would give me a polite 'Oh, that's nice' response."
        show BBW happy
        BBW "Oh, that's nice."
        "That's not what I mean. She was being sincere."
        MC "There was a more expensive suit there, but I think it was way too fancy for a school concert."
        MC "I felt this was more appropriate for the occasion."
        $setAffection("BBW", 1)
        BBW "No, it looks perfect."
        BBW "You're going to look quite sharp tomorrow."
        MC "Thanks. I also bought this."
        "I reached into the bag and fished out the choker."
        BBW "Oh! This is beautiful."
        MC "If your music club is anything like at my old school you're all wearing the same outfit, but you can still stand out with the right accessory."
        MC "That's what I was thinking, at least."
        $setAffection("BBW", 1)
        BBW "I love it. I'll wear it tomorrow night."
        MC "Hey, did you have dinner yet? I was going to grab something from the cafeteria."
        BBW "That sounds splendid."

        scene black with fade
        "So we grabbed dinner together."
        "I could tell she loved the choker, and she seemed to like the suit I had picked out."
        "I was feeling pretty pleased with myself"
        "It's not every day you can impress a cultured woman with your own sense of style."
        jump daymenu
    if getFlag("BBW035_c2_1"):
        MC "I'm coming back from town myself. Was buying a suit for tomorrow."
        MC "Maybe it's too much for a school concert, but I figured 'Hey, it's a big night for you. I should look nice myself.'"
        "As I opened up my bag and pulled out the suit Alice's face drooped a little."
        show BBW sad
        BBW "That's... rather extravagant."
        MC "It was a bit pricey, yeah."
        BBW "How much did it cost?"
        "When I gave her the price she almost winced."
        BBW "Oh, no. That's too much."
        BBW "The suit itself is too much for the concert. That's for something like meeting a foreign dignitary."
        MC "Well, I... I wanted to look nice for your big night."
        BBW "I appreciate that, but..."
        BBW "It's always possible to overdress for an occasion."
        MC "I guess."
        MC "Probably too late to return it today. At least I have the receipt."
        "I sighed."
        BBW "I've got to go. I'll see you tomorrow."
        MC "Yeah. Tomorrow."
        if getFlag("BBW035_c3_1"):
            "No way did I want to stop her with 'Oh, I also bought these gloves, just to be even more wasteful.'"

        scene Dorm Interior with fade
        "I went back to my dorm, hiding out there for the rest of the night."
        "I had overdone it, that was obvious."
        "I hadn't thought it would be possible to spend too much for someone like Alice. Guess I learned something there."
        jump daymenu
    if getFlag("BBW035_c2_2"):
        MC "I'm coming back from town myself. Was buying a suit for tomorrow."
        MC "Maybe it's too much for a school concert, but I figured 'Hey, it's a big night for you. I should look nice myself.'"
        "As I pulled the suit out of the bag I was worried that Alice would give me a polite 'Oh, that's nice' response."
        show BBW happy
        BBW "Oh, that's nice."
        "That's not what I mean. She was being sincere."
        MC "There was a more expensive suit there, but I think it was way too fancy for a school concert."
        MC "I felt this was more appropriate for the occasion."
        $setAffection("BBW", 1)
        BBW "No, it looks perfect."
        BBW "You're going to look quite sharp tomorrow."
        MC "Thanks."
        MC "Hey, did you have dinner yet? I was going to grab something from the cafeteria."
        BBW "That sounds splendid."

        scene black with fade
        "So we grabbed dinner together."
        #"She hadn't noticed my haircut, I guess that was a waste, but she did like the suit I had picked out."
        "I'll call that a win."
        jump daymenu
    if getFlag("BBW035_c1_3"):
        MC "I'm coming back from town myself. Was buying an outfit for tomorrow."
        MC "Nothing special, I just wanted to look presentable for your big night."
        "As I pulled the slacks and sweater out of the bag I was worried that Alice would give me a polite 'Oh, that's nice' response."
        show BBW happy
        BBW "Oh, that's... nice."
        MCT "She hates it."
        show BBW neutral
        BBW "You'll look good tomorrow."
        MC "I just wanted a change of pace from my school uniform."
        BBW "Yeah, no. It's nice."
        BBW "I have to go. I'll see you tomorrow."
        MC "Yep. Tomorrow."
        scene Dorm Interior with fade
        "Making my way back to my dorm, I felt like I hadn't done enough."
        "I don't think Alice was offended or anything by my choice, but she was clearly unimpressed."
        "And now it was too late to go back to town and find a nice outfit for tomorrow."
        "Should have gone that extra mile."
        jump daymenu
    if getFlag("BBW035_c1_1"):
        MC "Yeah, I decided to get a haircut as well. Want to look nice myself for tomorrow."
        show BBW sad
        "Alice looked at me, tilting her head to the left, then the right."
        BBW "I guess I didn't notice, but yes... Your hair is shorter."
        show BBW neutral
        BBW "It's still a bit... untamed."
        MC "Yeah, I'm going to style it tomorrow. Get it under control."
        "Suddenly nervous, I coughed, then said"
        MC "Well, I need to go take care of my homework. See you tomorrow."
        show BBW happy
        BBW "Yes. Au demain."
        hide BBW with dissolve

        scene Dorm Interior with fade
        "Making my way back to my dorm, I immediately regretted thinking a simple haircut would be impressive."
        "And now it was too late to go back to town and find a nice outfit for tomorrow."
        "Should have gone that extra mile."
        jump daymenu
    "You shouldn't see this message. Please post a report with the choices you picked if you do."
    jump daymenu

label BBW036:
    $setProgress("BBW", "BBW037")
    #Time: Afternoon
    scene Classroom with fade
    "It had arrived, the day of the concert."
    "Of course I wasn't a member of the music club, so to me it was like any other day."
    "But starting yesterday afternoon and ramping up to today I was wondering more and more about what Alice must be going through."
    "She was probably nervous. I know I would be in her shoes."
    "So when classes got out for the day I caught her before she could leave, ready to help in whatever way I could."
    MC "Alice! Hey."
    show BBW neutral with dissolve
    BBW "'Hey,' Keisuke."
    "I was momentarily taken aback by her dry tone."
    MC "I mean: Hello."
    BBW "Hello."
    "Her mood softened a bit, but she still looked on edge."
    BBW "I do not have time to stop and chat. I am sorry."
    "She made for the door. I followed a step behind."

    scene Hallway with fade
    show BBW neutral with dissolve
    MC "You have the concert tonight, right?"
    MC "That's why I caught you. I wanted to wish you luck."
    MC "Or wait! No! I read somewhere wishing luck is bad luck, right?"
    MC "What's the thing they say in America?"
    show BBW happy
    BBW "Break a leg?"
    BBW "And thank you, but I have never been one for concepts like 'luck.'"
    BBW "With adequate preparation trusting in chance is unnecessary."
    MC "So you're not nervous?"
    "Alice laughed sharply."
    BBW "What do I have to be nervous about?"
    BBW "I have performed for audiences before. Ones I expect will have been more critical than tonight's shall be."
    MC "Hmm?"
    show BBW neutral
    BBW "My old school's prestige was not based on age or exclusivity."
    BBW "It demanded more of its students than any other, even when it came to electives."
    BBW "But this school treats education almost as a second-order concern."
    BBW "Creating a safe environment for us to come to terms with our growth is more important, and I doubt the administrators will judge too harshly our performance tonight."
    MC "Hadn't thought of it like that."
    MC "Though I disagree that our classes aren't challenging."
    MC "But anyway, is there anything you want me to do to help?"
    "She looked at my curiously. Perhaps I had sounded too eager."
    "But I really did want to help in some way."
    BBW "There is nothing for you to do."
    BBW "As I said, preparation is better than hoping for luck."
    BBW "I have been training most of my life - not that tonight's setlist is all that demanding - I had my hair and make-up done the other day, and my dress has been cleaned and ironed."
    BBW "And it is not as if I will be center stage, anyway."
    "This last bit she grumbled none too quietly."
    "The issue between her and the music club president came back to me. Apparently Alice wasn't ready to move on from her perceived slight."
    MCT "I should say something to soothe her ego."
    MC "At least you'll be on stage."
    MC "And remember, if you can make your talent undeniable you're bound to get moved up to head singer."
    "It didn't seem to do the trick exactly, but she did nod."
    BBW "Bigger picture, yes."
    BBW "I have to go now. We're expected at the auditorium half an hour before curtain rises."
    MC "I'll be there."
    MC "Goo-  Break-  Sing well."
    "She smiled and then left."
    hide BBW with dissolve
    "Leaving me with nothing to do."
    "Which was unexpected."
    MCT "Is this the first time Alice has never tried to delegate a job?"
    scene black with fade
    "I passed the afternoon taking care of my homework and idling online."
    if getFlag("BBW035_c2_1"):
        "I took the suit I had bought out of the closet and looked it over."
        "It really was too extravagant for something like a school concert."
        "I just went with my regular uniform. At least it had a collar."
    "Then I grabbed an early dinner to make sure I could get a good seat for the concert."

    #Time: Night.
    scene Auditorium with fade
    "The concert wasn't a required activity, so I can't say I was surprised at how few people showed up."
    "Maybe a third of the auditorium was filled."
    "I was still nervous for Alice, even in spite of how confident she had been, but now I also felt chagrined practically the whole school was ignoring her."
    "And the rest of the music club."
    "The concert lasted a little over an hour, mixing a couple classical-sounding tunes with a lot of modern hits redone for an orchestra and squad of singers."
    "From the audience Alice looked like one singer among several, but I concentrated all my attention on her."
    "She really did have a splendid voice."

    scene School Planter with fade
    #Time: Night
    "After the concert I met up with Alice outside the auditorium."
    MC "You were great."
    show BBW happy with dissolve
    BBW "Thank you. I am satisfied with my performance."
    MC "I assume this doesn't compare to at your old school. Probably more people attended those shows, huh?"
    "Alice smiled ruefully."
    show BBW neutral
    BBW "There would usually be more people back then, yes."
    BBW "Family or other colleagues of the students, the occasional representative of a symphony or recording label."
    MC "Oh, wow. Lots more pressure."
    show BBW happy
    BBW "Not for me. Music has always been a diversion, not a calling."
    BBW "The standards I hold myself to are naturally high, but not that high."
    "I nodded, unable to think of anything to add."
    MC "So... when's the next concert?"
    show BBW neutral
    BBW "It has yet to be scheduled."
    MC "Oh."
    "I tried to think of something else to say, and as I did the silence went on too long and that became all I could think of."
    MC "You had dinner already, right?"
    BBW "Before the concert."
    MC "Same."
    "More uncomfortable silence."
    if getFlag("BBW035_c3_2"):
        show BBW happy
        BBW "Thank you. For the choker."
        BBW "I just wanted to thank you again for it."
        MC "No problem."
    "Then, almost before I knew what I was doing, I leaned in and kissed her."
    "I didn't regret the kiss, though I was afraid of what it might cost me."
    "Alice, for her part, did not immediately shove me to the ground and kick me in the stomach several times."
    "When I leaned back my initial thought was to apologize, but her expression wasn't one of anger or disgust, so I waited a moment to let her respond."
    show BBW neutral
    BBW "..."
    "After a long second, she chuckled and said"
    show BBW happy
    $setAffection("BBW", 1)
    BBW "I cannot fault you for taking the initiative, Keisuke."
    BBW "I guess Japan is more old-fashioned when it comes to dating, but..."
    BBW "Well done seizing the moment."
    show BBW neutral
    BBW "But do not make a habit of forcing yourself on me."
    MC "No, ma'am."
    MCT "Best possible outcome? Probably."
    show BBW happy
    BBW "I am going to head back to my room now."
    BBW "I will see you in class tomorrow."
    MC "Yep. See you."
    "I walked with her as far as the dorms, and then our paths diverged."
    scene black with fade
    "As much as I should have felt bad about rushing her like that, it had been too nice for me to regret it."
    "Her body was as soft as I imagined. Even her lips..."
    jump daymenu

label BBW037:
    $setProgress("BBW", "BBW039")
    #Time: Afternoon
    scene Classroom with fade
    "Approaching Alice after class had become the easiest thing in the world, but not quite for the reasons I wanted."
    "Case in point, when I wanted to quickly reiterate my compliments on her performance at the concert, and also ask how things between her and the club president have been shaping out..."
    MC "Alice, got a minute?"
    show BBW happy with dissolve
    "...she immediately seized control of the conversation."
    BBW "Keisuke. Perfect timing. I need an update from you on your delivery rounds."
    BBW "You have not reported any problems recently, so I trust everything is proceeding smoothly, yes?"
    MC "Buh?"
    MC "Oh, yeah! The deliveries are going great. I've got a system more or less worked out."
    BBW "Excellent."
    show BBW neutral:
        xzoom -1.0
        linear 1.0 xpos 0.75
    MC "That wasn't what I wanted to talk about, though."
    show BBW neutral:
        xzoom 1.0
        linear 1.0 xpos 0.5
    MC "I wanted to say again I thought you were very good during the concert the other night."
    show BBW happy
    BBW "Thank you."
    MC "And I was wondering if things between you and the music club president had improved at all."
    show BBW neutral
    BBW "..."
    "Alice chewed on that for a second."
    BBW "She did compliment my contribution to the concert yesterday."
    BBW "She said I 'showed genuine talent.' When we were alone in the club room, with no one else around."
    MC "Oh..."
    MC "Well, a positive comment-"
    BBW "Blandly positive."
    MC "-like that is better than nothing. Things might be thawing between you two."
    BBW "Perhaps."
    MC "One other thing."
    MC "Are you free Friday? I'd like to go out again."
    show BBW happy
    BBW "I would too. Saturday sounds good."
    MC "I was thinking dinner and a movie. It's nothing spectacular, I know..."
    BBW "Do not overthink it, Keisuke. This would only be a second date."
    BBW "And our options for entertainment on this island are limited."
    MC "Right, but I'd still like to come up with something more than the five or six things we've all already done."
    MC "But anyway... How does Saturday at 5 sound?"
    BBW "That'll work. I'll meet you in the dorm lobby."
    show BBW happy:
        xzoom -1.0
        linear 1.0 xpos 0.75
    "She turned to leave, but one other issue to discuss had been on my mind."
    "How do we handle the issue of me working for Alice while dating her?"
    "It was kind of a heavy matter to bring up, because I could only think of two options: we don't go out anymore, or I quit working for her."
    "Which would put a crimp in my finances. Not the best situation when I was trying to woo someone with expensive tastes like Alice."
    "Was this a Catch 22? Either I can date Alice but not have the money to, or I can not date her but have a nice amount of disposable income."
    "Either way, it was very much the sort of thing that needed to be addressed..."
    "Just maybe not right after securing a second date. Something heavy like this could wait for later, right?"
    menu:
        "Let it rest for now.":
            jump BBW037_c1_1
        "Better bring it up now.":
            jump BBW037_c1_2

label BBW037_c1_1:
    hide BBW with dissolve
    MCT "There's no rush. I can deal with it later."
    scene black with fade
    "I left the classroom and went about the rest of the afternoon like always."
    "Got a snack, did my homework, played some games."
    "And I looked through the showtimes for the only theater on the island. I needed to find a safe but not boring or insipid choice for our date."
    "Pleasure before business, I guess."
    jump daymenu

label BBW037_c1_2:
    MC "Actually, there is one other thing. Sorry."
    show BBW neutral:
        xzoom 1.0
        linear 1.0 xpos 0.5
    MC "If we are going to keep going out, I think we should address the employer/employee matter."
    BBW "Aaah, yes."
    MC "You're professionally minded, so you should understand things would be weird between us if I'm both subservient to you but also an equal."
    "Alice smiled wryly."
    show BBW haughty
    BBW "So you want a promotion. Angling for a full partnership in the company, are we?"
    MC "No, I-"
    "And I stopped, because I realized she wasn't put off by the idea."
    "It wasn't what I was going for, but it was definitely the best outcome. I hadn't even considered it before."
    MCT "And the way she's smiling, does she like my ambition?"
    MCT "No reason not to go for it."
    MC "If not a full partnership, then maybe a title befitting my status as the chief... distribution... manager."
    "Alice chuckled."
    BBW "That is not on the same level as President and Chief Executive Officer, but it would put us closer to equal footing."
    BBW "Yes, I think that would work."
    show BBW happy
    BBW "And as long as we maintain a professional bearing when it comes to the company, I do not foresee any problems."
    $setAffection("BBW", 1)
    BBW "Good job keeping the big picture in view, Keisuke. I knew my ability to read people was strong."

    scene black with fade
    "I think she was still referring to my grab for a promotion. Did she admire my ambition? That seemed to fit her personality."
    "And it would answer the question of what she respected more: subservience or a strong will. I'd have to remember that for the future."
    "For the time being, I had another ordinary day ahead of me."
    "I left the classroom and went about the rest of the afternoon like always."
    "Got a snack, did my homework, played some games."
    "And I looked through the showtimes for the only theater on the island. I needed to find a safe but not boring or insipid choice for our date."
    "If nothing else, I knew Alice wasn't a woman you could court by half-assing things."
    jump daymenu

label BBW038:
    if getProgress("BBW") == "BBW038": #fix for wrong progress issue, delete later
        $setProgress("BBW", "BBW037")
    #Time: Morning
    scene Classroom with fade
    play music Schoolday
    "I got to class early today."
    "I wasn't fully awake yet- hell, I was about to fall asleep sitting at my desk - but out of nowhere an electronic jingle shook me awake."
    #[SFX: Simple electronic melody]
    "It took me a second to realize that even with just five notes I knew that tune."
    "And it took me another second to realize what it was."
    MC "Was that the 'Everything is two' theme?"
    show BE happy at Position(xpos=0.3, xanchor=0.5, yalign=1.0), Transform(xzoom=-1) with dissolve
    BE "Yeah! Someone mentioned it in a comment thread I was looking at yesterday and I ended up watching a bunch of remixes of it yesterday."
    BE "I changed my ringtone to it."
    MC "I remember that. There was that one video with the frog jumping onto a window sill, and it doesn't quite make it."
    MC "It's hanging onto the edge, trying to climb up, and the music gets really dramatic."
    show BE neutral
    BE "Which one's that? I haven't seen it."
    MC "Let me see if I can find it."
    show BBW neutral at Position(xpos=0.7, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Everything is two? What does that mean?"
    show BE happy
    BE "It was the stupid thing from a few years ago."
    BE "Somebody took a snippet of a song from... What was it from, Keisuke?"
    MC "Oh... It was this old ghost kung fu movie."
    MC "There was a scene in the middle, just out of nowhere, where the hero and the girl are stuck in a temple while it rains, and this romantic song plays in its entirety."
    MC "Someone in America posted the scene online because there's a sign in the temple that apparently is really filthy, the way it's written in English."
    BE "Something about grabbing the Buddha's nipples."
    MC "Oh god, is that what it was?"
    BE "But someone else did a cover of the song, and they made the cheesiest, most over-the-top video of romantic cliches to go with it."
    MC "And then other people made their own videos, or they took movie clips. Completely inappropriate stuff, like someone mourning a dead person or a slow pan over a cemetary."
    BE "All with the sappy song playing over it."
    BE "Then people started covering the song, but in completely different musical styles. Thrash metal, ukelele hip-hop, stuff like that."
    MC "Not long after people started taking the most extreme covers and pairing them with the weirdest videos they could find."
    MC "Found it! The frog video."
    show BE happy at Position(xpos=0.25, ypos=0.5, yanchor=0.3), Transform(zoom=2.0)
    show BBW neutral at Position(xpos=0.75, ypos=0.5, yanchor=0.3), Transform(zoom=2.0)
    #[BE_Happy and BE_Neutral zoom in, head and upper torso]
    "I showed Alice and Honoka the video I had been talking about."
    "The love song plays like normal as we watch a frog prepare to jump from a fence post onto a window sill."
    "The video is in slow motion, and as the frog jumps the song immediately shifts to the most dramatic movie score-style rendition."
    BE "Oh!"
    "But the frog doesn't quite make it. Its front legs reach the sill, but its back legs kick in the air, then try to climb up the wall so it can get in."
    "And eventually it does."
    BE "Ha ha ha! It did it!"
    "Honoka found the thing hilarious, but Alice look confused. Then quickly angry."
    show BE happy at Position(xpos=0.3, yalign=1.0), Transform(zoom=1.0)
    show BBW angry at Position(xpos=0.7, yalign=1.0), Transform(zoom=1.0)
    BBW "That's it?"
    BBW "What's so amusing about that?"
    BE "By itself, nothing. But the song is so over-the-top to begin with and the frog looked so determined..."
    "Noticing Alice's irritation, Honoka trailed off."
    MC "It's just a meme. Something goofy to laugh about."
    BBW "Empty frivolity."
    BBW "To think that standards of entertainment can sink so low that thousands of people will share an image of a cat with a goofy expression or... or a frog trying to jump into a window."
    BBW "Why is he even trying to get into the window? Why is he on the fence post to begin with!?"
    show BE surprised:
        linear 0.5 xpos 0.1
    BE "Whoa!"
    BE "Calm down."
    show BE neutral:
        linear 1 xpos 0.3
    BE "It's just a meme."
    BBW "It's a stupid-!"
    show AE neutral at Position(xpos=0.9, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    AE "Is there a problem here?"
    MC "No... No. We just got a little overly exuberant."
    AE "I suggest you save your energy for class."
    AE "Now take your seats."
    hide AE with dissolve
    "The mood was still tense after that interruption. Before turning to leave Alice muttered something at half-volume."
    BBW "Stupid video about a stupid frog."
    hide BBW with dissolve
    "Honoka, meanwhile, looked at me and, in a voice like a drunk robot, said"
    show BE happy
    BE "No, Goro, truck can not go to roof."
    MC "Ha ha ha ha ha!"
    "And I erupted in laughter."
    "Turning in her seat, Alice glared at us."
    show BBW angry at Position(xpos=0.7, yalign=1.0), Transform(zoom=1.0)
    BBW "Grrrrr..."
    hide BE with dissolve
    hide BBW with dissolve
    "I tried to stifle my laughter, but Honoka, taking her own seat, kept chuckling right up until the teacher arrived."
    "It was hard to concentrate on the lesson now that I had that stupid song playing in my head, but at least I wasn't about to fall asleep."
    jump daymenu

label BBW039:
    $setProgress("BBW", "BBW040")
    #Time: Morning
    scene Classroom with fade
    "The day had come for my second date with Alice, with only a few lectures between now and then."
    "Though strangely Alice had not yet arrived and would soon be late."
    "As I recall, I saw her in the cafeteria eating a hearty breakfast and looking as robust as ever this morning."
    "If the place hadn't been so crowded I would have joined her. It would have been a good time to confirm a plan for our date."
    MCT "But she's usually good about showing up early for class. I can ask her then."
    MCT "Speak of the..."
    "The thought died unfinished. Not because referring to Alice as a devil was wrong, but because-"
    show BBW neutral with dissolve
    BBW "Keisuke, I trust you havent forgotten our plans for tonight?"
    MCT "Crap."
    MC "Of course not Alice! They're just a secret, is all."
    MC "Oh and good morning."
    BBW "{i}Sigh{/i}"
    show BBW happy
    BBW "Good morning."
    MC "You're looking lovely today."
    "I had hoped that would be a safely neutral comment, but as Alice sat down she sighed again."
    show BBW neutral
    BBW "{i}Sigh{/i}"
    BBW "I'm getting fatter. Still."
    BBW "I'll likely have another growth spurt during Summer."
    BBW "I don't know if it's noticeable to everyone else, but it certainly is to me."
    BBW "It can not escape my notice that I have had to upgrade my wardrobe yet again."
    MC "You do look lovely, though. Sexy, even."
    "I couldn't help myself from blushing as I added that last part under my breath, just loud enough for her to hear."
    "But it was true. I wasn't just trying to make her feel better."
    BBW "Hmmph."
    "Her facial expression waffled between pleased and dismissive. She settled on pleased."
    show BBW happy
    BBW "I look good no matter what."
    MC "You'll get no argument from me."
    MC "So, our date tonight?"
    show BBW angry
    BBW "Keisuke!"
    show BBW neutral
    BBW "{i}Sigh{/i}"
    show BBW happy
    BBW "Let's just worry about class first, okay?"
    HR "Everyone sit down."
    scene black with fade
    play sound ClockTower
    pause 4

    #Time: Afternoon
    scene School Front with fade
    "I arrived at the school gate a few minutes before 5."
    "Being early is better than being on time, and it gave me a chance to calm my nerves before Alice showed up."
    show BBW casual-happy with dissolve
    BBW "Hello, Keisuke."
    BBW "Shall we be off?"
    MC "If you're ready."
    "We started walking down the hill to town."
    "It was still rather light, the days were getting longer, so I kept stealing glances at Alice."
    "Out of her school uniform and in a more casual - but still fashionable and presumably costly - outfit her recent growth looked even more prominent."
    "I was especially drawn to how her belly swelled out in front of her, reaching further than her breasts and coming down over the top of her legs."
    "She was soft all over, but her middle looked especially inviting. I wanted to lay my head down on it, like an oversized pillow."
    show BBW casual-neutral
    BBW "..."
    MCT "Crap, she saw me staring again."
    MCT "Gotta say something..."
    MC "Your clothes..."
    BBW "...?"
    MC "You look... lovely tonight."
    BBW "You said that this morning."
    MC "Did I?"
    MC "Well... I mean. Your outfit looks nice. On you."
    MC "I thought you had said you had outgrown your wardrobe, but... You had something to wear."
    MC "That's good."
    BBW "I have been hyper-aware of my growth recently, so I have been making sure to have clothes to fit me as I continue to grow."
    MC "You're lucky in that regard, being able to ignore the cost of new clothing."
    BBW "It's one issue out of several related to my size."
    "Her tone sounded sort of maudlin."
    "What she had said this morning about wanting to forget about everything going on came back to me."
    MCT "Better change the subject."
    MC "I'm enjoying the book we're reading in literature."
    BBW "Are you?"
    MC "Yeah. I relate to the main character a lot, despite the different time period setting."
    BBW "Have you read anything by the author before? They're pretty well-regarded in Japan, as I understand it."
    MC "No... Historical fiction isn't my usual cup of tea."

    scene black with fade
    "We made small talk the rest of the way to a restaurant in town."
    "I think I managed to take Alice's mind off her size and related matters."

    scene Restaurant with fade
    "At the restaurant we had to wait a couple minutes before being seated."
    "And then once we were we waited so long just to get some water that we were ready to order our meals by then."
    "Alice was particularly irked."
    show BBW casual-angry with dissolve
    BBW "(Such subpar service.)"
    MC "(Can't blame our waitress. Don't you see that party over there?)"
    "I indicated a group of almost a dozen people, adults and a couple children, gathered around two large tables pushed together in the far corner."
    "The adults were mostly or perhaps all from the school. Not all of them had visible factors, but one man looked like a professional bodybuilder, another was covered in dense hair not just on his head but his face and arms."
    "And there were a couple women who were significantly fatter than a typical middle-aged person who had stopped exercising regularly."
    "And there might have also been an overweight man, but I couldn't see the entire table."
    MC "(And there's just the one waitress working tonight.)"
    show BBW casual-neutral
    BBW "Who are those people? I don't recognize them as teachers or administrators."
    MC "Maybe they're alumni."
    MC "Not enough people for a class reunion, but maybe they're a group of friends getting back together."
    MCT "I wonder if the academy actually does do class reunions..."
    BBW "Maybe."
    "She continued staring for a while before turning back around."
    "I was worried I could guess what had caught her attention."
    BBW "Those women..."
    "She went silent, then shook her head."
    BBW "There's no excuse for dressing so shabbily."
    MC "Lack of money?"
    "But even as I said that I realized that wasn't really what was bothering her."
    "The women were both fatter than Alice was right now. A sign that further growth was possible."
    MCT "Do I say something? Or should I take her mind off this?"
    menu:
        "Try to placate Alice's self-consciousness.":
            jump BBW039_c1_1
        "Get her mind off her body image problems.":
            jump BBW039_c1_2

label BBW039_c1_1:
    MC "There's no guarantee you're going to get that fat, you know."
    show BBW casual-angry
    BBW "Excuse me?"
    MC "You're not exactly hiding your thoughts right now."
    MC "Those women over there? The overweight ones?"
    MC "You see them and you're thinking 'Am I going to end up that fat?'"
    show BBW casual-neutral
    BBW "I don't think both of them are fat."
    BBW "One looks like she is very busty, and the rest of her has gotten soft in middle age."
    "I turned back to the group and saw the one Alice was talking about. She might have been right."
    MC "Okay, but still."
    MC "Am I wrong? Are you not preoccupied with how big you'll get?"
    show BBW casual-angry
    BBW "I came with you tonight because I wanted to take my mind off such things."
    BBW "Had that not been obvious?"
    MCT "Yikes. Maybe I should back off."
    menu:
        "Change the subject.":
            jump BBW039_c2_1
        "Press on.":
            jump BBW039_c2_2

label BBW039_c2_1:
    MC "Never mind."
    $setAffection("BBW", -1)
    BBW "No, don't 'never mind.'"
    BBW "I asked you a question. Was it not obvious why I am upset right now?"
    MC "It is, I just..."
    MC "I didn't know you were that upset."
    MC "You're usually more confident. I didn't realize this had gotten to you so bad."
    MC "I wasn't trying to antagonize you."
    "I stopped myself from rambling further, and a heavy silence came over the table."
    "It took another few, excruciating minutes before our food arrived, and the silence was replaced by the clinks of silverware and the sound of chewing."

    scene black with fade
    "When we were done there was no talk of dessert or anything else. We just left and headed back to the school."

    #Time: Evening
    scene School Front with fade
    "At the entrance Alice gave a curt goodbye."
    show BBW casual-neutral with dissolve
    BBW "Good night."
    hide BBW with dissolve
    "And I was left alone."
    MCT "Which is probably for the best."
    MCT "Can't put my foot in my mouth if I don't open it."
    jump daymenu

label BBW039_c2_2:
    $setFlag("BBW039_c2_2")
    MC "I had guessed as much."
    MC "But it looks like the world isn't going to let you ignore it."
    MC "And I don't expect you're in the habit of ignoring unpleasant truths."
    MC "Or have I misread you?"
    BBW "..."
    "She glared at me for a second, but I didn't look away. I held her gaze."
    "Finally she exhaled, visibly deflating."
    show BBW casual-neutral
    BBW "You're not wrong."
    BBW "Running from problems is not in my nature."
    BBW "But when an issue is outside of my power to control, it..."
    BBW "I get caught up in a clash of different emotions."
    MC "That's understandable. No one could blame you for being upset about this."
    MC "You were probably hoping your factor wouldn't be this strong, huh?"
    BBW "Yes."
    BBW "When I was first told what my factor was I tried to do research into my condition, see if there was any way to predict its severity."
    BBW "No such luck."
    MC "This is all new territory for the medical and scientific communities, isn't it?"
    MC "You kind of have to let it run its course. There's nothing else to do."
    BBW "There's not much comfort there."
    MC "Sorry, but I wasn't trying to be comforting. I'm just stating the facts."
    "That actually made Alice laugh."
    show BBW casual-happy
    BBW "Heh."
    BBW "I have to give you that."
    MC "But if you want to be comforted, you should know it's not any kind of failing that you're getting fatter."
    MC "It was a roll of the dice, and all you can be judged for is how you deal with it."
    MC "And so far you've been handling it admirably, I would say."
    "At that point our food came, and we let the conversation die."
    "But Alice did seem more relaxed, if not in the brightest of moods."

    scene black with fade
    "After the meal we walked around the town for a while, making light-hearted conversation."
    "Alice continued to brighten up as the evening went on, and by the time we headed back to the school she was genuinely happy."

    #Time: Evening
    scene School Front with fade
    show BBW casual-happy with dissolve
    $setAffection("BBW", 1)
    BBW "It wasn't the best date I've been on, Keisuke, but I think it was what I needed."
    BBW "Thank you."
    "And she leaned in and kissed me, her belly pressing into me as she did so."
    "Part of me wanted to return it passionately, but worried about how precarious her good mood was I simply put an arm around her back as we kissed."
    MC "Have a good night."
    BBW "You too. I'll see you tomorrow."
    jump daymenu

label BBW039_c1_2:
    MC "Do you ever listen to Day Shift? They have a new album coming out."
    show BBW casual-angry
    BBW "..."
    show BBW casual-neutral
    BBW "No. I've never heard of them."
    MC "Oh. They're this rock duo. I have a couple of their albums. They're pretty good."
    "I rambled a bit more until, mercifully, our food arrived."
    "We ate in uncomfortable silence, punctuated by a couple attempts on my part to start some small talk."

    scene black with fade
    "After our meal we silently agreed to head back to the school, the date aborted."
    "I took some solace in the feeling that Alice wasn't angry with me personally, but all the same the night had been a failure."
    jump daymenu

label BBW040:
    #Time: Morning
    scene Dorm Interior with fade
    $setProgress("BBW", "BBW041")
    "In the middle of getting dressed for the day my phone buzzed with a text. It was from Alice."
    BBWCell "I need your help with something. Can you come to my dorm room?"
    "A week ago I would have assumed this was something work related, but after our second date I let myself hope this would turn out to be something..."
    "... more intimate, perhaps?"
    "I checked myself in the mirror to make sure I was more than 'classroom presentable,' then left for the girl's dorm."

    scene black with fade
    MC "Alice?"
    play sound Knock
    BBW "Keisuke? Come in and shut the door, please."

    scene Dorm BBW with fade
    "Aida was out, so it was just me and Alice, who had her back to me as she sat on her bed."
    MC "What's up?"
    "When she turned around I got the picture."
    show BBW sad at Position(xpos=0.5, xanchor=0.5, ypos=1.0, yanchor=0.5) with dissolve
    play music BBW
    BBW "Thank you for coming. I am having trouble getting dressed."
    "She was trying to button her shirt, and had fallen short by three buttons."
    BBW "I have a better fitting wardrobe on order, but I had not expected to need it this soon."
    BBW "I believe I can make it through the day if I am cautious and do not move too much, but first I need help getting those buttons around the... widest part of my belly done."
    MC "And it looks like Aida is out... Don't you have a new assistant?"
    BBW "She is on another errand right now, and I have already had to delay my normal routine."
    MC "Couldn't you have asked another woman here?"
    BBW "I suppose, but the thought of letting another woman - or anyone, for that matter - see me in this situation..."
    show BBW happy
    BBW "But I trust you to be circumspect."
    BBW "Just as I trust you not to abuse this opportunity."
    MC "Not sure what you mean by 'opportunity.'"
    BBW "You get to put your hands on me. And we've only gone out twice."
    if getSkill("Academics") > 10:
        MC "Yes, but this isn't undressing you. This is the exact opposite."
        MC "A real opportunity would be to help you take the shirt off later."
        $setAffection("BBW", 1)
        BBW "Don't get cheeky."
    else:
        "She was smiling, but I was about to break out in a cold sweat."
        "I knew enough about her temper not to step out of line."
    MC "All right, I promise to behave."
    hide BBW with dissolve
    #[CG from the perspective of kneeling in front of Alice, her belly filling most of the screen and her breasts at the top. Her shirt is mostly buttoned, with the bottom three undone, the flaps parted to reveal her creamy skin and belly button.]
    "I knelt down in front of her and took the two flaps of her shirt. My thumbs pressed lightly against her belly, and I heard her inhale sharply."
    MC "Are you okay?"
    BBW "I'm fine. It is just... sensitive."
    MC "It?"
    BBW "My belly."
    BBW "I would not have thought it could develop into an erogenous zone, but it seems there are secondary attributes to these physical changes."
    if getAffection("AE") > 12:
        MC "You sound kind of like Shiori."
    else:
        MC "You sound like Matsumoto-san."
    BBW "Hmm?"
    MC "So formal just now. Almost analytical."
    BBW "I am simply stating how things are."
    MC "In a detached sort of way."
    "She did not respond immediately. I expected her to tell me to get one with it, but instead when she spoke she said"
    BBW "Staying detached helps deal with this."
    "I nodded, then realized she couldn't see me."
    MCT "Better get on with it."
    "I took the shirt flaps and pulled them together. Because there was no extra room I had to run my thumbs along Alice's belly, eliciting another moan."
    "She tried to suppress this one, or at least keep it quiet, but it was no use."
    "And, none too surprisingly, her arousal affected me. That and the fact that I was kneeling in front of her with her big, soft, bulging belly inches from my face."
    "I almost wondered if this was a test, but that seemed particularly harsh, almost downright cruel. For all her faults Alice didn't seem the type to tease people."
    "But as my hands ached to stroke that plush middle, I knew there was still a way to fail this."
    MCT "But why should I be so timid? If she thinks I'm going too far what is the worst she will do?"
    menu:
        "Stroke her belly.":
            jump BBW040_c1_1
        "Play it safe.":
            jump BBW040_c1_2

label BBW040_c1_1:
    MCT "The third date is when you're supposed to go all the way, yes?"
    MCT "It's not out of line to treat light petting as a stone on the path to actual sex, is it?"
    if getFlag("BBW039_c2_2"):
        MCT "And on our last date she kissed me. Does that not open any doors for me?"
    "It took a bit to psyche myself up for what I was thinking."
    "But once the idea was in my head I think it was inevitable. The potential risk of angering Alice didn't compare to the anticipated rewards."
    "I thought about starting slow, but decided if I was going to go I had to go all out."
    "I pressed one hand against her belly and rubbed it in a wide circle. Not rough, but as sensual as I could manage with my heart racing."
    "Alice's reaction was instant."
    BBW "Oh!"
    BBW "What are you doing?!"
    MCT "Oh, poopie. I didn't expect her to be that angry."
    "First reaction? Abort mission!"
    "Maybe I could play it off as a joke, or an accident."
    menu:
        "Say it was a joke.":
            jump BBW040_c2_1
        "My hand slipped.":
            jump BBW040_c2_2
        "Don't back down.":
            jump BBW040_c2_3

label BBW040_c2_1:
    MC "Just playing around!"
    "I pulled my hand away immediately, then grabbed the shirt and resumed closing it."
    stop music
    "Alice wasn't having it, though."
    play music Tension
    BBW "What do you mean 'playing around'?!"
    MC "I-! I just thought it would be funny."
    show dummy with hpunch
    BBW "Get your hands off me!"
    #[Return to normal background.]
    show BBW angry at Position(xpos=0.5, xanchor=0.5, yalign=1.0) with dissolve
    $setAffection("BBW", -1)
    BBW "Get out."
    MC "I'm sorr-"
    BBW "No! I don't want to hear it! Out!"
    MC "I..."
    "Her glare shut me up."
    "Trying to not look cowed - I wouldn't meet her gaze, but I also didn't want to be staring at the floor - I left."

    scene black with fade
    "I avoided Alice for the rest of the day, giving her a wide berth in the cafeteria and not giving her a reason to notice me in the class."
    "I rehearsed, to myself, different ways to placate her, to explain myself. I ultimately decided to not be the one to bring it up. If she was still sore tomorrow, I'd deal with it then."
    "But even if she didn't, I was going to be walking on eggshells for a while. Whatever had been building up between Alice and me, it was in a tenuous place now."
    jump daymenu

label BBW040_c2_2:
    $setFlag("BBWdom")
    MC "Sorry! My hand slipped!"
    "I pulled my hand back at once, chastened by the whipcrack of her tone, but I didn't panic."
    "She was simply too intimidationg for me to press further."
    BBW "Hmmm..."
    BBW "Very well... next time I'm sure you'll know to not be rash."
    "Her voice was even-tempered, in a chilling way, but I still let myself give a sigh of relief. Too quiet to be heard, of course."
    "I took her shirt in hand again and buttoned it for her, with just a little difficulty."
    "She was going to have to be careful the rest of the day."
    #[Revert to Int. Alice's room]
    show BBW neutral at Position(xpos=0.5, xanchor=0.5, yalign=1.0) with dissolve
    BBW "This is adequate, which is the best I can hope for in this situation."
    BBW "Thank you, Keisuke."
    MC "Glad to help. And sorry about my hand slipping."
    BBW "Mmmm... Yes. 'Slipping', of course."
    BBW "Sometimes it is better to retreat than to advance."
    show BBW haughty
    $setAffection("BBW", 1)
    BBW "And sometimes it shows who is really in control."

    scene Hallway with fade
    "I was halfway to the cafeteria to grab a quick breakfast when I was suddenly hit with a realization that made me stop."
    MCT "Alice... hadn't actually seemed upset by my hand 'slipping.' Thinking about it, it sounded like she had enjoyed it. Was she..."
    MCT "'In control'? Was she setting herself as the one in charge?"
    "I spent the rest of the morning unable to get that idea out of my mind, thinking of how Alice has been the one to make decisions so far."
    "I suppose if anyone was going to be bold and assertive, it would be Alice."
    "Now I was frustrated, because when was something like that going to come up again?"
    MCT "Next time... Next time she'll be ready."
    MCT "And that doesn't sound bad at all."
    jump daymenu

label BBW040_c2_3:
    $setFlag("BBW040_c2_3")
    "On second thought... no. I came this far, I'm seeing it through."
    MC "I'm rubbing your belly. It's so soft and inviting."
    "Alice didn't have an answer to that. Not right away."
    "So I continued rubbing, my hand moving around in a large, slow circle."
    MC "And I think you like it, too."
    $setAffection("BBW", 1)
    BBW "Oooooh!"
    "She was enjoying it, that was clear as day. And I certainly was, of course."
    "Alice's belly was as soft as I had imagined, but not in a doughy sort of way. There was a firmness to it, not unlike a mattress."
    "I wondered if there was a part of her growth factor that maintained her fat's consistency, avoiding the sagging or oozing qualities I'd seen in other fat people."
    "I thought about mentioning this hypothesis that she was primed to receive only the most pleasing of adipose, but I knew how she would react and I didn't want to spoil the moment."
    MC "This really does feel so nice."
    BBW "Mmmmm... I know..."
    BBW "But I need you to stop, Keisuke. I've got to get ready for class."
    BBW "And I expect Aida will be back soon."
    MC "Oh. Right."
    "I took her shirt in hand again and buttoned it for her, with just a little difficulty."
    MC "You're going to have to be careful for the rest of the day."
    #hide CG
    show BBW neutral with dissolve
    BBW "I should be upset that you would take advantage of me when I needed help like that, but you less crossed the line than stuck your foot over it."
    show BBW happy
    BBW "And it would be an obvious lie if I said I had not enjoyed it."
    show BBW neutral
    BBW "But do not make a habit of letting your hands off the leash like that."
    BBW "Spontaneity can become harassment very quickly."
    MC "Oh! I wasn't trying to force myself on you!"
    show BBW happy
    BBW "I know. And I respect that you took the initiative."
    show BBW neutral
    BBW "Though..."
    MC "What?"
    "Alice placed her hands on the sides of her belly and jiggled it ever-so-slightly."
    BBW "Nothing."
    MC "It's all right to find this enjoyable."
    "She didn't say anything, just looked down to the side."
    "This wasn't the first time she had gone silent when the issue of her growing had come up, but I didn't want to let it spoil the moment this time."
    MC "I mean it. I'm not saying you're wrong to be upset about how things are turning out..."
    MC "...but trying to find the positive doesn't mean 'what's good despite everything else.' Sometimes something isn't good or bad, it's both."
    MC "You can't separate looking bigger and finding it pleasing to be bigger. They're both related to your factor, and true acceptance-"
    BBW "I get it."
    "She wasn't curt, but her tone did sound decisive."
    BBW "Yes, this situation does have its upsides, and no, I should not try to look at it as a collection of parts I consider 'good' or 'bad.'"
    BBW "My father told me something similar shortly after I got here, that I should take this all as it is en total."
    BBW "But I..."
    show BBW sad
    BBW "There is a part of me that does not want to give in to anything positive about this."
    MC "You're afraid accepting any part of it will make you accept all of it?"
    show BBW neutral
    BBW "Not simply accept it as it is, but accept that it is as it must be."
    MC "Even though you're planning to deal with the excess weight once this is all over, right?"
    show BBW sad
    BBW "Assuming I can, yes."
    play sound DoorOpen
    "It wasn't the worst time to be interrupted like this, but Aida showing up just then brought the conversation to a halt."
    show BBW sad at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    if getAffection("PRG") < 10:
        show PRG surprised at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
        PRG "Ah! Hotsure-san! W-what are you doing here?"
        MC "Alice needed help with... opening a jar."
        MC "I was just leaving."
        MC "See you two in class."
        show BBW neutral
        BBW "Thank you for your help, Keisuke."
    else:
        show PRG aroused at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
        PRG "Kei-chan. What are you doing here?"
        MC "Alice needed help with... opening a jar."
        MC "I was just leaving."
        MC "See you two in class."
        show BBW neutral
        BBW "Thank you for your help, Keisuke."
        PRG "Are you sure you can't stay? We can walk to class together."
        MC "I've got to get my backpack. See you later."

    scene black with fade
    "I left the girls' dorm and went back to my room to grab my stuff, frustrated more with myself than anything at how the discussion with Alice had ended unresolved."
    "I don't know what the right thing to say to her would have been, but it felt like she was about to open up more than she had already."
    "And this isn't the sort of thing I could just bring up casually later on, but it was out there, so we were going to talk about it again sooner or later."
    MCT "Maybe it's not even something I can lead her through. Maybe I should let her handle it herself."
    jump daymenu

label BBW040_c1_2:
    MCT "Better play it safe."
    "Being as careful as possible not to rub Alice's belly, holding my fingers away from her middle except for those holding the shirt flaps, I tugged the two sides together and buttoned it up."
    "She was going to have to be careful for the rest of the day, but the job was done."
    #hide CG
    show BBW neutral with dissolve
    BBW "This leaves me little room to breathe, but it will do."
    show BBW happy
    BBW "Thank you, Keisuke. And thank you for not being too handsy."
    BBW "The teasing was unexpected, but not unenjoyable."
    MC "Oh, it was an accident."
    BBW "So you said..."
    BBW "You should probably finish getting ready for class. I will see you later."
    MC "I was- ... Yeah. See you later."

    scene black with fade
    "I really hadn't been trying to get her worked up, but her thinking I had wasn't what bothered me."
    "It was the implication that if I had dived in she would have liked it more. Why did I hold back!?"
    jump daymenu

label BBW041:
    $setProgress("BBW", "BBW042")
    scene Dorm Interior with fade
    MCT "Ugh. So bored."
    MCT "At this point I'd accept a conspiracy theory debate with Daichi."
    "{i}BZZZT{/i}"
    MCT "Even fate wants me to avoid that conversation, it seems."
    "I checked my phone, pleasantly surprised to see a text from Alice."
    play music BBW
    "Yesterday's events were... interesting, to say the least."
    "Just having the chance to get close to her belly like that was exhilarating."
    BBWCell "< Come to the arcade, I have something fun to show you. >"
    MCT "Alice? At the arcade? Oh this {i}will{/i} be fun."
    MCCell "<I'm on my way.>"
    "I got dressed and rushed to the bus stop. I had to be there as soon as possible."

    scene School Exterior with fade
    "I got to the bus stop just in time to see the bus to town pulling away."
    MC "Damnit."
    MCT "Okay. The next bus isn't for half an hour. I can wait or I can run to town."
    MCT "..."
    MC "Better get moving."
    if getSkill("Athletics") == 0:
        stop music
        scene black
        "I was barely 5 minutes into the run when my body simply couldn't take anymore."
        "I decided to text Alice that I couldn't make it and I slowly walked back to my dorm instead."
        $setAffection("BBW", -1)
        MCT "I really need to get in shape."
        jump daymenu

    scene Town with fade
    "I finally reached the arcade, feeling like I had run a marathon."
    show BBW neutral with dissolve
    BBW "Wow you look spent. Did you miss the bus?"
    MC "Yeah but that didn't stop me from getting here to see you."
    MC "So why did you want me to come to the arcade?"
    BBW "Because I knew you'd know where it was. Our actual destination is just around the corner."
    show BBW haughty
    BBW "Plus, I knew you would race here if you thought I wanted to play a game here."
    MCT "Drat. She knows me too well."
    MC "I raced here because seeing you is worth a sprint."
    show BBW happy
    BBW "Charming. Now come with me, I assure you this will be more than those flashing loud 'games' are."

    if isEventCleared("FMG016"):
        jump BBW041_FMG016
    elif isEventCleared("FMG009"):
        jump BBW041_FMG009
    else:
        jump BBW041_FMG000

label BBW041_FMG016:
    "Alice had elected to visit the island's only maid café, where I was about to meet Chibuki again."
    "Avoiding this was suddenly my chief concern."
    MC "A maid café? Alice, are you sure?"
    BBW "Absolutely. I like the idea that businesses have been formed to provide an imitation of maid services to those who cannot afford actual maids."
    BBW "It shows that people needn't money to have fine taste."
    MCT "I guess I'll have to try and convince her."
    menu:
        "Insist.":
            MC "Alice, I don't want to eat here. Can we choose somewhere else?"
            MC "I'm afraid I have to insist."
            show BBW stern
            BBW "You... insist?"
            MC "Yeah, insist."
            BBW "Of course, Keisuke. Whatever you think is best."
            show BBW sad
            $setAffection("BBW", -3)
            BBW "I will see to it."
            MC "..."
            BBW "Well then I suppose I'll see you in school tomorrow."
            hide BBW with dissolve
            "Alice turned around and walked towards the bus stop."
            MCT "She must have really wanted to eat at the café. Was avoiding Chibuki worth upsetting my girlfriend?"
            "I had a heavy conscience as I started the long walk back to Seichou."
            jump daymenu

        "Don't insist.":
            play music Schoolday
            BBW "Come on, this will be fun."

            scene Cafe with fade
            show BBW neutral at center, Transform(xzoom=-1) with dissolve
            "Alice walked to one of the roomier booths and sat down."
            BBW "This is a fine spot. The faux leather seating is of surprisingly good quality."
            BBW "If the food is good, I might just find myself in here regularly."
            MCT "Let's hope not."
            MC "I suppose we shall see."
            show Chibuki neutral at Position(xpos=0.8) with dissolve
            Chibuki "Surprised to see you in here without Miss Akira, Master Kei-chan."
            Chibuki "{size=-5}{i}Looks like he did a full 180 there.{/i}{/size}"
            "Alice squinted, clearly perplexed."
            MC "Yes Chibuki, I'm here with my girlfriend Alice."
            show BBW happy at center, Transform(xzoom=1)
            BBW "Mistress Nikumaru. I'm here for the experience."
            Chibuki "Ahh... Well, Mistress Nikumaru, most people come for the experience and stay for the food."
            "Alice glanced at her watch and a sly smirk quickly spread across her face."
            show BBW haughty
            BBW "Miss Chibuki, I'd like to put your claim to the test. Two coffees and two slices of cake of your choosing."
            Chibuki "Wow, okay! This is going to be fun."
            Chibuki "Right away Mistress."
            hide Chibuki with dissolve
            MCT "This can't end well."
            BBW "Well Keisuke,I told you this would be fun."
            show BBW neutral
            MC "Are you sure about this?"
            BBW "Of course, it'll be fun."
            MC "Well in that case, let's do it!"
            BBW "That's the spirit."
            "As Alice said that, Chibuki emerged from the kitchen."
            BBW "Now we just have to see how good our esteemed maid truly is."
            show Chibuki neutral at Position(xpos=0.8) with dissolve
            Chibuki "It's early so I went back there to help out and get everything set up."
            Chibuki "For Mistress Nikumaru, a rich yet light chocolate cake, house recipe."
            Chibuki "{size=-5}{i}Saves money.{/i}{/size}"
            Chibuki "And a coffee blend that I shall specify the name of afterwards."
            Chibuki "For Master Kei-chan, a slice of plain sponge with generous vanilla frosting, and a double espresso. You really look like you could do with it mate."
            Chibuki "Please enjoy."
            hide Chibuki with dissolve
            "Chibuki went to sit near the door, no doubt awaiting any potential customers walking in."
            "Alice first bit into her cake, while I hastily sipped the coffee."
            MCT "This caffeine will be a life-saver when it hits."
            BBW "The cake is quite good actually, that was unexpected."
            BBW "It certainly is rich but they have used less frosting to account for that, giving a more refined taste."
            BBW "It certainly seems more enjoyable than how yours looks to be."
            MC "Well enjoyment is for the individual, perhaps I prefer a larger amount of frosting at a weaker flavour."
            BBW "I know, and as an individual I say this one is better."
            show BBW haughty
            BBW "It's nothing personal Keisuke, it's just business."
            MC "Well, how's the coffee?"
            show BBW neutral
            BBW "Well, as you know, coffee is not my preferred beverage. Though that isn't to say I don't have preferred blends."
            BBW "But I suppose we are about to find out."
            "Alice sipped her coffee slowly, clearly making sure to properly taste each aspect of it."
            "As she did so, I took the opportunity of her being unable to see me to quickly scrape the frosting from my cake into my mouth."
            show BBW happy
            BBW "I know this coffee. It's Antigua, a Guatemalan variety."
            BBW "One of my favourite coffees actually."
            BBW "Chibuki must have an excellent ability to read people, as well as a fine taste in coffee herself."
            BBW "I know tipping isn't particularly common in Japan at all, but I feel she has earned it."
            BBW "Are you ready to go yet Keisuke?"
            MC "I just need to drink some more coffee."
            "I drank a good third of my espresso, as fast as I could without burning my mouth. I really did need the caffeine."
            MC "I'm ready."
            "Alice and I got up and walked over to the counter. Chibuki immediately stood up and walked behind it when she saw us moving."
            show Chibuki neutral at Position(xpos=0.8) with dissolve
            Chibuki "That comes to 1340 yen total, Master and Mistress."
            "I reached for my wallet but Alice gestured at me to stop."
            BBW "I decided to come here Keisuke, allow me."
            "As she paid Chibuki for the breakfast, she started speaking to her in English."
            "I could only stand there and watch, completely oblivious to what they were saying."
            "I realised it must have been about tipping when Alice took 500 more yen out of her purse. Chibuki was clearly shocked at the amount."
            "Alice then returned to speaking Japanese."
            BBW "Please, take it. You more than deserve it."
            Chibuki "Thank you so much Al-{w} Mistress Nikumaru."
            BBW "You will almost certainly see me in here again, this morning has been a delightful experience."
            BBW "We should leave now, Keisuke. The next bus is in a few minutes."
            hide BBW with fade
            "As Alice walked towards the door I quickly spun around to face Chibuki."
            MC "How did you know exactly which coffee to get for Alice?"
            Chibuki "It's simple, I used the one with the fanciest looking packaging."
            MCT "Wow. The best solution truly is the simplest."
            Chibuki "Bye Master Kei-chan, come back any time."

            scene Town with fade
            show BBW happy with dissolve
            BBW "That was a rather nice way to spend the morning, won't you agree?"
            BBW "Come on now the next bus to Seichou should be here soon."
            jump daymenu

label BBW041_FMG009:
    "Alice had elected to visit a maid café, likely the only one on the island."
    MC "A maid café? Alice, are you sure?"
    BBW "Absolutely. I like the idea that businesses have been formed to provide an imitation of maid services to those who cannot afford actual maids, it shows that people don't need money to have taste."
    MC "Well, alright then. I guess this could be fun."
    BBW "Only one way to find out."

    scene Cafe with fade
    play music Schoolday
    show BBW neutral at center, Transform(xzoom=-1) with dissolve
    show Chibuki neutral at Position(xpos=0.8) with dissolve
    Chibuki "Good morning Miss, Good morning Mast- oh bugger."
    Chibuki "It's Keisuke isn't it?"
    "It suddenly struck me that I remembered this girl from somewhere."
    Chibuki "Please don't tell Akira about this job, she can't know something {i}this{/i} embarrassing about me."
    "That was where I remembered this girl from. She is Akira's roommate, Chibuki."
    MC "It's alright, I promise not to tell."
    Chibuki "Thank you Keisuke. I owe you one for this."
    Chibuki "So, are you going to introduce me?"
    MC "Alice, this is Mizutani-san's roommate, Chibuki."
    MC "Chibuki, this is my girlfriend, Alice."
    BBW "Nice to meet you, though Mistress Nikumaru will suffice for the duration of our experience here."
    Chibuki "Of course Mistress Nikumaru, Master Keisuke. How may I serve you today? Our cakes can't be beat."
    "A sly smirk quickly spread across Alice's face."
    show BBW haughty at center, Transform(xzoom=1)
    BBW "Can't be beat you say?"
    BBW "Well in that case, two slices of cake and two coffees. What kind of each is completely at your discretion."
    Chibuki "Wow, okay! This is going to be fun."
    Chibuki "Right away Mistress."
    hide Chibuki with dissolve
    MCT "This can't end well."
    BBW "Well Keisuke, I told you we would be having some fun today."
    "Alice and I sat at a nice booth and waited for Chibuki to return."
    show BBW neutral
    MC "Well, I suppose this will be an interesting experience."
    MC "At the very least it's a delicious slice of cake"
    BBW "That's the spirit."
    "As Alice said that, Chibuki emerged from the kitchen."
    BBW "Now we just have to see how good our esteemed maid truly is."
    show Chibuki neutral at Position(xpos=0.8) with dissolve
    Chibuki "It's early so I went back there to help out and get everything set up."
    Chibuki "For Mistress Nikumaru, a rich yet light chocolate cake, house recipe."
    Chibuki "And a coffee blend that I shall specify the name of afterwards."
    Chibuki "For Master Keisuke, a slice of plain sponge with generous vanilla frosting, and a double espresso. You seemed drowsy, I hope it helps."
    Chibuki "Please enjoy."
    hide Chibuki with dissolve
    "Chibuki went to sit near the door, no doubt awaiting any potential customers walking in."
    "Alice first bit into her cake, while I hastily sipped the coffee."
    MCT "This caffeine will be a life-saver when it hits."
    BBW "The cake is quite good actually, that was unexpected."
    BBW "It certainly is rich but they have used less frosting to account for that, giving a more refined taste."
    BBW "It certainly seems more enjoyable than how yours looks to be."
    MC "Well enjoyment is for the individual, perhaps I prefer a larger amount of frosting at a weaker flavour."
    BBW "I know, and as an individual I say this one is better."
    show BBW haughty
    BBW "It's nothing personal Keisuke, it's just business."
    MC "Well, how's the coffee?"
    show BBW neutral
    BBW "Well, as you know, coffee is not my preferred beverage. Though that isn't to say I don't have preferred blends."
    BBW "But I suppose we are about to find out."
    "Alice sipped her coffee slowly, clearly making sure to properly taste each aspect of it."
    "As she did so, I took the opportunity of her being unable to see me to quickly scoop the frosting from my cake into my mouth using my finger."
    show BBW happy
    BBW "I know this coffee. It's Antigua, a Guatemalan variety."
    BBW "One of my favourite coffees actually."
    BBW "Chibuki must have an excellent ability to read people, as well as a fine taste in coffee herself."
    BBW "I know tipping isn't particularly common in Japan at all, but I feel she has earned it."
    BBW "Are you ready to go yet Keisuke?"
    MC "I just need to drink some more coffee."
    "I drank a good third of my espresso, as fast as I could without burning my mouth. I really did need the caffeine."
    MC "I'm ready."
    "Alice and I got up and walked over to the counter. Chibuki immediately stood up and walked behind it when she saw us moving."
    show Chibuki neutral at Position(xpos=0.8) with dissolve
    Chibuki  "That comes to 1340 yen total, Master and Mistress."
    "I reached for my wallet but Alice gestured at me to stop."
    BBW "I decided to come here Keisuke, allow me."
    "As she paid Chibuki for the breakfast, she started speaking to her in English."
    "I could only stand there and watch, completely oblivious to what they were saying."
    "I realised it must have been about tipping when Alice took 500 more yen out of her purse. Chibuki was clearly shocked at the amount."
    "Alice then returned to speaking Japanese."
    BBW "Please, take it. You more than deserve it."
    Chibuki "Thank you so much Al-{w} Mistress Nikumaru. Your generosity is astounding."
    BBW "You will almost certainly see me in here again, this morning has been a delightful experience."
    BBW "We should leave now Keisuke. We're not late, but we don't have much time."
    hide BBW with dissolve
    "As Alice walked towards the door I quickly spun around to face Chibuki."
    MC "How did you know exactly which coffee to get for Alice?"
    Chibuki "It's simple, I used the one with the fanciest looking packaging."
    MCT "Wow. The best solution truly is the simplest."
    Chibuki "Goodbye Master Keisuke, please come back any time."
    scene Town with fade
    show BBW happy with dissolve
    BBW "That was a rather nice way to spend the morning, won't you agree?"
    BBW "Come on now the next bus to Seichou should be here soon."
    jump daymenu

label BBW041_FMG000:
    "Alice had elected to stop at a maid café, likely the only one on the island."
    MC "A maid café? Alice, are you sure?"
    BBW "Absolutely. I like the idea that businesses have been formed to provide an imitation of maid services to those who cannot afford actual maids, it shows that people don't need money to have taste."
    MC "Well, alright then. I guess this could be fun."
    BBW "Only one way to find out."
    scene Cafe with fade
    play music Schoolday
    show BBW neutral at center, Transform(xzoom=-1) with dissolve
    show Chibuki neutral at Position(xpos=0.8) with dissolve
    Chibuki "Good morning Miss, Good morning Master."
    "It appeared the only maid working at the moment was foreign. Her accent would be a dead giveaway, if her blue eyes didn't beat it to it. They were a deeper blue than Alice's."
    BBW "Nice to meet you, please call me Mistress Nikumaru."
    Chibuki "Of course Mistress Nikumaru, and you Sir?"
    MC "Keisuke. I guess you have to call me master or something for the job though right?"
    Chibuki "That is correct Master Keisuke."
    Chibuki "Now how may I serve you two today? Our cakes can't be beat."
    "Alice glanced at her watch and a sly smirk quickly spread across her face."
    show BBW haughty at center, Transform(xzoom=1)
    BBW "Can't be beat you say?"
    BBW "Well in that case, two slices of cake and two coffees. What kind of each is completely at your discretion."
    Chibuki "Wow, okay! This is going to be fun!"
    Chibuki "I mean- right away Mistress."
    hide Chibuki with dissolve
    MCT "This can't end well."
    BBW "Well Keisuke, turns out we will actually be having some fun today."
    "Alice and I sat at a nice booth and waited for Chibuki to return."
    show BBW neutral
    MC "Are you sure about this?"
    BBW "Absolutely. Trust me, it'll be fun."
    MC "Well in that case, let's do it!"
    BBW "That's the spirit."
    "A few minutes passed and Chibuki emerged from the kitchen."
    BBW "Now we just have to see how good our esteemed maid truly is."
    show Chibuki neutral at Position(xpos=0.8) with dissolve
    Chibuki "Thank you for waiting."
    Chibuki "For Mistress Nikumaru, a rich yet light chocolate cake, house recipe."
    Chibuki "And a coffee blend that I shall keep the name of a secret for now."
    Chibuki "For Master Keisuke, a slice of plain sponge with generous vanilla frosting, and a double espresso. I hope it helps."
    Chibuki "Please enjoy."
    hide Chibuki with dissolve
    "Chibuki went to sit near the door, no doubt awaiting any potential customers walking in."
    "Alice first bit into her cake, while I hastily sipped the coffee."
    MCT "This caffeine will be a life-saver when it hits."
    BBW "The cake is quite good actually, that was unexpected."
    BBW "It certainly is rich but they have used less frosting to account for that, giving a more refined taste."
    BBW "It certainly seems more enjoyable than how yours looks to be."
    MC "Well enjoyment is for the individual, perhaps I prefer a larger amount of frosting at a weaker flavour."
    BBW "I know, and as an individual I say this one is better."
    show BBW haughty
    BBW "It's nothing personal Keisuke, it's just business."
    "I let out a sensible chuckle."
    MC "How's the coffee?"
    show BBW neutral
    BBW "Well, as you know, coffee is not my preferred beverage. Though that isn't to say I don't have preferred blends."
    BBW "But I suppose we are about to find out."
    "Alice sipped her coffee slowly, clearly making sure to properly taste each aspect of it."
    "As she did so, I took the opportunity of her being unable to see me to quickly scoop the frosting from my cake into my mouth using my finger."
    show BBW happy
    BBW "I know this coffee. It's Antigua, a Guatemalan variety."
    BBW "One of my favourite coffees actually."
    BBW "Our 'maid' must have an excellent ability to read people, as well as a fine taste in coffee herself."
    BBW "I know tipping isn't particularly common in Japan at all, but I feel she has earned it."
    BBW "Are you ready to go yet Keisuke?"
    MC "I just need to drink some more coffee."
    "I drank a good third of my espresso, as fast as I could without burning my mouth. I really did need the caffeine."
    MC "I'm ready."
    "Alice and I got up and walked over to the counter. Chibuki immediately stood up and walked behind it when she saw us moving."
    show Chibuki neutral at Position(xpos=0.8) with dissolve
    Chibuki  "That comes to 1340 yen total, Master and Mistress."
    "I reached for my wallet but Alice gestured at me to stop."
    BBW "I decided to come here Keisuke, allow me."
    "As she paid Chibuki for the breakfast, she started speaking to her in English."
    "I could only stand there and watch, completely oblivious to what they were saying."
    "I realised it must have been about tipping when Alice took 500 more yen out of her purse. Chibuki was clearly shocked at the amount."
    "Alice then returned to speaking Japanese."
    BBW "Please, take it. You more than deserve it."
    Chibuki "Thank you so much Mistress Nikumaru! Your generosity is astounding."
    BBW "You will likely see me in here again, this morning has been a delightful experience."
    BBW "Well Keisuke, let's head back to school."
    hide BBW with dissolve
    "As Alice walked towards the door I quickly spun around to face Chibuki."
    MC "How did you know exactly which coffee to get for my girlfriend? That was her favourite."
    Chibuki "It's simple, I used the one with the fanciest looking packaging. It made sense to me because of her dress."
    MCT "Wow. The best solution truly is the simplest."
    Chibuki "Goodbye Master Keisuke, please come back any time."
    scene Town with fade
    show BBW happy with dissolve
    BBW "That was a rather nice way to spend the morning, won't you agree?"
    BBW "Come on now the next bus to Seichou should be here soon."
    jump daymenu

label BBW042:
    $setProgress("BBW", "BBW043")
    scene Art Classroom with fade
    play music Rain
    "After classes I had wanted to meet up with Alice to touch base on if any deliveries were needed. She wasn't answering any texts, but when I found Aida in the cooking classroom she told me Alice was probably in the arts room."
    "I did indeed find her there, standing at an easel. The painting she had been working on in class earlier that day was in front of her."
    show BBW angry with dissolve
    "Something about it seemed to be frustrating her. I weighed the pros and cons of interrupting her, and ultimately decided to do what I came to."
    MC "Hey, Nik- Alice? Got a second?"
    show BBW stern
    BBW "Hmm? What can I do for you?"
    MC "I just wanted to check with you to see if there were any deliveries I needed to make, or any other work."
    BBW "No. We are all good on that."
    "She was only half-paying attention as she answered me, already turning back to her painting when she finished talking."
    "Curious what was giving her trouble, I glanced at the painting. It was a landscape, a grassy cliff overlooking the ocean."
    MC "Nice picture."
    "I was then going to head out, leave her to her work, but I guess Alice needed to vent."
    show BBW angry
    BBW "This is a bothersome experience. If it were possible to call a piece of art 'insolent,' I would."
    MC "Is it giving you trouble? It looks really good."
    show BBW stern
    BBW "The landscape itself is acceptable, and I am satisfied with the colors."
    BBW "I have had to make due with a limited array of paint tones, the art department is not the best funded, but I was always good with color theory if I say so. Mixing just the right shades was not difficult."
    "I took a longer look at the painting, paying attention to the different shades of greens in the grass and blues in the skies. There was more detail there than I had originally noticed."
    MC "So what's the problem?"
    BBW "The lighting. You see how the sun is supposed to be coming from the east?"
    "I looked to the right side of the frame, then realized from this perspective east was left."
    "I stared for a couple minutes, expecting or rather hoping to see something jump out at me. A problem like something off-model or looking sloppy."
    "Nothing came to me."
    MC "I don't see what the problem is."
    BBW "Hmm..."
    BBW "Have you seen Arisawa's painting?"
    "She indicated a painting done by a classmate of ours, one of the finished pieces sitting on the shelves along the wall."
    "It was also a landscape, looking down at the rock quarry where the giant students lived. Alice's painting was good, but this one looked almost professional."
    MC "That's really good, yeah. But yours isn't bad. It's better than mine."
    BBW "I know mine is good. And I am not concerned about being the best in the class, but in doing the best I can."
    BBW "Look at the lighting in Arisawa's. Do you see how the sunlight reflects off the surfaces of the rocks? How its warmth is muted by the lingering chill of the morning?"
    BBW "I have been trying for hours to get the interplay of light and warmth in my picture perfect, but the more I work on it the more of a mess it becomes."
    MC "Oh. Um... I'm sorry, I don't know anything about painting, really. I can't give any advice there."
    MC "But why not be content with how good your painting is anyway?"
    BBW "Because it is {i}only{/i} good. By my own standards that is merely adequate."
    BBW "I have done better. Not necessarily with the lighting, I am trying something new, but the principle is the same. I do not want to rest at 'good enough.'"
    MC "I see."
    MC "I still think you should be satisfied with it as it is. It's very good."
    BBW "That is not my way. If there are ways for me to improve, I pursue them. Stagnation is death."
    MCT "That's harsh, even if she's applying it to herself. It's just something she's doing for a school assignment."
    MCT "I should say something. Or should I? I don't know Alice that well, but she seems to take everything seriously."
    menu:
        "Reassure her the painting's good.":
            MC "I think the painting looks great. You could be a real artist."
            $setAffection("BBW", -1)
            show BBW angry
            MCT "I guess I didn't sound convincing."
            "Alice turned back to her painting, clearly annoyed."
            BBW "The level of your exuberance is so excessive you almost sound sarcastic. But I would think actual sarcasm would have been more obvious."
            BBW "Whatever your intent, I ask that you let me resume my work. In peace."
            MC "Okay, yeah. Sorry."
            scene black
            "I quietly left, feeling like I had accomplished less than nothing. I had probably come out worse than if I had said nothing."
            MCT "Maybe blatant flattery doesn't work on her as well as I thought it would."
            jump daymenu

        "Ask her if she really needs to try so hard.":
            MC "Even now? You don't want to slow down a bit?"
            show BBW doubt
            BBW "Of course even now. Why would I go easier on myself now?"
            MC "Because of... why we're here. The news about our bodies. We're all still dealing with that."
            show BBW neutral-2
            BBW "My body, you mean. Not all of these 'factors' are equal burdens."
            MC "Yeah..."
            BBW "That has never been my way, shrinking away from bad news. What would it accomplish?"
            BBW "Life will continue to move forward even if I stopped, people our age who are not in our situation are advancing with their lives, so the best choice is to keep moving myself."
            BBW "Is that not what this school is for? To help us both continue our education while learning to live with our changing bodies?"
            MC "..."
            "I didn't have a rebuttal for that."
            "Then I realized that maybe this wasn't about the painting... Maybe this was just her way of dealing with any frustrating experience."
            "I couldn't say I knew Alice well enough to read into her actions like that. It could just be she was exactly that much of a perfectionist."
            "Either way, I saw no benefit to pushing back further."
            MC "I'll leave you to it, then. I just wanted to see if you had anything for me."
            BBW "Not at the moment. I will see you later."
            "She turned back to her painting and I quietly left."
            scene black
            "On the way back to my dorm I thought about things I could have said, or wish I had said."
            "None of which would have been helpful. Bottom line, I needn't have tried to insert myself into her business like that, even if I was trying to be helpful."
            "I was just hoping now that she wasn't bothered by my attempt. Hopefully she would forget about this by tomorrow."
            jump daymenu

        "Tell her she should keep at it until she gets it.":
            MCT "On second thought, who am I to tell her to be satisfied with 'good enough?' If she thinks she can improve, she deserves encouragement."
            MC "You're right. There's nothing wrong with wanting to get better."
            show BBW neutral
            BBW "Mmm."
            BBW "..."
            MC "..."
            BBW "..."
            MCT "I thought she would have appreciated that more."
            BBW "Was that it? The entirety of your thoughts?"
            "She said, turning back to her painting."
            BBW "While I appreciate your attempt at being supportive, I think I will get back to this now. I am certain you have other things to do."
            MC "Yeah, um... I'll see you around."
            MCT "It appeared just agreeing with her wasn't enough. Which was a bit surprising."
            MCT "I guess I'm the fool for thinking her so easily manipulated. Turns out not every pampered elite responds to such blatant ego-stroking."
            jump daymenu

        "Say nothing.":
            "I thought about how to respond to all that. Do I flatter her? Try to soothe her ego? Would agreeing with her accomplish anything?"
            "The pause started to get long enough to be threatening. I had to say something, so I decided... to say nothing."
            MC "Don't let me interrupt you, then. I have some homework to do myself."
            MC "If it's that important to you, best of luck."
            show BBW happy
            BBW "Thank you. I will see you in class tomorrow."
            scene black
            MCT "She wasn't oozing with gratitude, but she seemed to appreciate my leaving her in peace. I think that was the best outcome here."
            jump daymenu

label BBW043:
    $setProgress("BBW", "BBW044")
    scene Dorm Interior with fade
    play music Peaceful
    MCT "Ugh, I'd been wracking my brain trying to study for an upcoming quiz for most of the afternoon. My boredom finally reached a tipping point where I found myself unable to focus. I needed a break."
    scene Dorm Interior with fade
    MCT "I decided my study efforts would be better served if I could get outside and clear my head for a little while. So I figured I'd take a walk around campus."
    MCT "I didn't make it too far before I ran into a lovely, familiar face."
    show BBW haughty with dissolve
    BBW "Keisuke! Just the person I was looking for."
    MC "The one and only! At your service m'lady."
    show BBW happy
    BBW "Heh, cute. Charmed, I'm sure."
    MC "As always. What's up?"
    show BBW neutral
    BBW "I've been thinking lately that I need to do more to stay active."
    show BBW worried
    MCT "Alice's focus shifted away from me and down towards the swell of her belly, where her feet had long since disappeared from her sight."
    BBW "{i}Sigh...{/i}"
    show BBW neutral-2
    BBW "Between classes, the business, and music club I fear I've begun to neglect my usual physical activities."
    if isEventCleared("BBW009"):
        MCT "Alice didn't have the body of an athlete by any means, but from what I'd seen, she was one hell of a swimmer. She didn't seem that rusty to me."
    MC "I thought you swam fairly often in your free time? I mean, maybe not every day, but you seem pretty active to me."
    BBW "True, I do make the time to stay somewhat active with swimming but doing laps by yourself in the pool just doesn't provide the same meaningful push that direct competition does."
    MC "Are you going to join the swim club then?"
    show BBW haughty
    BBW "Close, but no. Unfortunately, their meeting times conflict with the music club. A minor inconvenience, but one I worked out how to overcome. I came up with an even better idea."
    MC "Oh? Sounds interesting. What is it?"
    BBW "I'll merely start my own club. Since I'll be the head of it, I can schedule the meetings when it fits into my schedule. I just need to get enough members to charter the club."
    MC "Let me guess- that's where I come in."
    show BBW neutral
    BBW "Precisely. Though I must say Keisuke, I expected a bit more enthusiasm from you."
    show BBW neutral-2
    BBW "Aren't you interested in doing something that'll let us spend more time together?"
    MCT "Alice was layering on the guilt pretty thick with that remark. By this point I was all too used to getting dragged into doing extra work for her, but despite her obvious guilt trip, her tone was soft and sincere."
    MCT "I suspected this was her way of expressing she was interested in spending more time with me."
    MC "Oh, of course! I didn't mean it like that. I was just thrown off a bit because I thought there couldn't be two of the same clubs."
    show BBW haughty
    BBW "That is true, which is why I came up with something different: a water polo club."
    MC "Like that sport in the Olympics where they throw a volleyball while swimming?"
    show BBW neutral-2
    BBW "Well it's not exactly like a volleyball, though I do suppose they look similar. So do you understand the basics of how it's played then?"
    MC "Uh, no, not really. That was pretty much everything I know about water polo."
    show BBW neutral
    BBW "Well, you aren't the only one it would seem. Unfortunately, that is consistent with the reactions of everyone else I've approached with this idea."
    BBW "No one here seems to know anything about it at all. Such a disappointing lack of culture. In all the schools I've attended prior, it was offered as an extracurricular."
    BBW "No matter, this is just another hurdle to overcome. I'll merely have to teach the new members how to play."
    MC "Is it difficult to play?"
    BBW "It is an extremely demanding sport."
    MCT "Crap."
    BBW "You are basically always swimming, and you need to keep yourself high enough in the water to be able to catch and throw the ball. I asked the best and strongest swimmers I knew to come join because I need people that can keep up."
    MC "I'm one of the best swimmers you know?"
    show BBW neutral-2
    BBW "Well, maybe not the best, but still pretty good. I had to reserve the goalie positions for swimmers I thought would have a hard time keeping up and I need more fielders."
    show BBW happy
    BBW "I'm confident you're up to the task."
    show BBW aroused
    BBW "Especially with the right motivation."
    "I was picking up what she was laying down. This was clearly something Alice was really hoping to make happen and apparently I was the missing piece of the puzzle."
    MCT "I'm not sure I've ever had the upper hand in a negotiation with Alice before. Knowing her, I probably never will again either. Better leverage this to my benefit."
    MC "Alright Alice, I will join your water polo club."
    BBW "Thank you Keisuke. I knew I could rely on you."
    MC "On one condition."
    show BBW stern
    BBW "Oh?"
    MC "You'll owe me a date. How about ice cream after club practice?"
    show BBW aroused
    BBW "Well, that doesn't seem like too hard of a bargain."
    show BBW haughty
    BBW "I accept your offer. Though, honestly Keisuke your negotiation skills could use some work if that's all you've managed to gain from this."
    MC "Isn't the pleasure of your company its own reward?"
    show BBW happy
    MCT "Alice rolled her eyes at my lame attempt to express my affection, but it brought a giddy smile to her face nonetheless."
    BBW "Oh, you're hopeless. But also, very sweet."
    $setAffection("BBW", 1)
    show BBW haughty
    BBW "The first preliminary club meeting is tomorrow afternoon at the pool. I didn't get enough people for a full team, but I at least managed to scrape up enough to form a group charter."
    BBW "Assuming everyone wants to join up that is. I expect to drum up more interest once people have had a chance to play."
    MC "I'll be there."

    scene black with fade
    play music Rain
    MCT "Alice gave me a run-down on the rules so I had a basic understanding of what to expect. The rules weren't too hard to understand, but I could tell I was in for a workout with all the swimming I'd have to do just to keep up."
    MCT "We both had to get going. I still had a lot of studying to do, so I went back to my dorm. I tried to study, but found myself distracted by both the excitement and dread of what was going to happen the next day."

    scene Classroom with fade
    play music Schoolday
    MCT "The studying I put into the day before paid off decently well. Probably didn't get an A, but I felt confident enough I avoided worse than a C."

    scene Lockers with fade
    MCT "With the quiz out of the way along with the rest of the classes I headed to the locker to change into my swimsuit. I had a little extra time to kill before the practice started, but I didn't have anything better to do and it wasn't worth walking back to my dorm."
    MCT "So, I figured I'd show up a bit early and hang out with Alice for a little while beforehand."

    scene Pool with fade
    show BBW haughty with dissolve
    BBW "Ah, Keisuke, you're here early. What a pleasant surprise."
    MCT "Is everyone surprised when I'm not late?"
    MC "Well, I don't think I would have been on time if I went back to my room, so I decided to just come here instead. Do you need help setting anything up?"
    BBW "No, that's quite alright. Thank you for offering though. I have the zone markers and the goals already set up. I'm just waiting for everyone else to show up."
    BBW "With you we'll have just enough to do a three on three. It's not the full experience, but at least we'll be able to have a game."
    MC "You seem like you're pretty excited for this. I guess you missed playing water polo."
    show BBW happy
    BBW "Very much so. My hope is that once people experience it, they'll also come to enjoy it as much as I do."
    show BBW worried
    BBW "{size=-6}Well that and swimming laps in the pool by myself sometimes feels a bit lonely...{/size}"
    MC "Oh, well I could come with you next time if that's the case."
    show BBW surprised
    BBW "Oh! I didn't mean it like that."
    MCT "More like she didn't mean that to slip. Now that I think about it, outside of Aida and me, I don't think Alice has made a lot of friends to hang out with. Maybe there's more to this than just wanting to play water polo."
    show BBW haughty
    BBW "Besides, there will be plenty of others to swim with once I get this club up and running officially. The rest should be coming along soon."
    MC "Come to think of it, I never did ask who else you convinced to come and try this out."
    show BE happy at Position(xpos=0.85, xanchor=0.5, yalign=1.0) with dissolve
    BE "The last person you'd ever expect, Kei-chan."
    MC "Honoka, given how many different clubs you've been in and out of, you're the first person I should have suspected."
    show BE angry
    BE "I don't have the slightest idea what you're talking about Kei-chan."
    show BE neutral
    MC "I'm sure. But I will say I didn't think you'd be up for something that required so much swimming."
    BE "Eh, you know me. I'm always up for something new and exciting, and I'd never heard of water polo before. Alice told me I could be a goalie, so I won't have to swim that much, just keep my head above water most of the time."
    show BE unique
    BE "Besides, with these built-in floatation devices, how hard could that be?"
    "She certainly did have a point, but I thought I should change the subject before I got caught up in Honoka's penchant for calling attention to her chest- especially with Alice right next to me."
    show BE neutral
    MC "If the goalie position doesn't require as much swimming, I think I know who the next person will be."
    show PRG neutral at Position(xpos=0.15, xanchor=0.5, yalign=1.0) with dissolve
    PRG "H-Hello everyone."
    BBW "Right on time, Aida. Thank you for coming. Let me know whenever you think you need a break, but I think you'll be just fine if you can tread water."
    PRG "Thanks, Nikumaru-san. I'll do my best."
    BBW "Don't worry so much about that, I want you to just try to have fun. Our remaining participants on the other hand, I have some pretty high expectations for."
    show Natsuko neutral at Position(xpos=0.35, xanchor=0.5, yalign=1.0) with dissolve
    Natsuko "Hello Alice. Thank you for the invitation again. I'm always up for a new challenge. A contact sport where you need to swim and handle a ball sounds tough. I'm ready to show you what I can do!"
    MCT "When Alice told me yesterday she asked the strongest swimmers that she knew, I didn't think she meant that quite so literally."
    MCT "Thankfully, this wasn't a rugby match, but looking at Natsuko's towering stature and broad shoulders, I had a feeling I was still going to get run over."
    BBW "I'm glad to hear that Natsuko. I'm looking forward to playing with someone who can keep up with my swimming skills."
    MC "So, if you needed more strong swimmers, that means the other person you asked is probably... Ohhh, no."
    show FMG happy at Position(xpos=0.65, xanchor=0.5, yalign=1.0) with dissolve
    FMG "Hey dudes! What's up everyone! I'm ready to crush it in the pool today!"
    show FMG angry-2
    FMG "Wait. What's {i}SHE{/i} doing here?"
    show BBW surprised
    BBW "Oh, I see you two know each other alrea-"
    Natsuko "I should say the same! Alice said this is a sport for strong swimmers. I don't even trust you to not drown in the tub."
    show FMG angry
    show BE surprised-2
    show PRG scared
    FMG "Judging by the stink lines coming off of you, I don't even think you know what a tub is used for."
    MCT "Akira and Natsuko began to bicker back and forth, doing their best to one-up each other as they came up with even more creative ways to denigrate each other's athletic ability."
    MCT "Looking at everyone else's reaction to the scene, this was creating a really toxic environment. While those two were still battling it out I whispered an aside to Alice."
    MC "{size=-8}Alice, you didn't know those two hate each other's guts?{/size}"
    show BBW sad
    BBW "{size=-8}I had no idea. They're both so nice to everyone else, and I'd never heard them talk about the other before.{/size}"
    MC "{size=-8}Well, this looks pretty bad.{/size}"
    show BBW neutral
    BBW "{size=-8}Perhaps, but it's nothing a reasonable person can't get over and act like an adult.{/size}"
    MC "{size=-8}This doesn't look like it's going to end any time soon. I think you should say something. Aida and Honoka look scared.{/size}"
    show BBW doubt
    Natsuko "Why don't you go back to the locker and get your pool floaties if you're planning on lasting the whole match."
    FMG "I don't have any, but I'm sure you have plenty of extra pairs."
    BBW "Alright ladies that's quite enough! Save your energy for the pool. You'll need it."
    BBW "We don't have enough players for substitutions. You're both going to be in there the whole time."
    show BBW stern
    BBW "Whatever rivalry you two have going on, I suggest you channel that animosity towards something constructive. I'll be watching for fouls."
    BBW "Fouls lead to time out penalties, and when teams can't substitute, that leads to the opponent scoring- and you losing. Got it?"
    Natsuko "I see. Very well then."
    show FMG angry-2
    FMG "Yeah, I got it."
    hide PRG with dissolve
    hide BE with dissolve
    hide FMG with dissolve
    hide Natsuko with dissolve
    show BBW haughty
    BBW "Alright then, with that out of the way let's get started. I've explained the rules to each of you earlier, but I'll give a refresher on some of the basics right now before we start."
    BBW "Fielders can only handle the ball with one hand, while goalies can use two. You only have 30 seconds to attempt to shoot once your team gets the ball or you lose possession- this game moves fast."
    show BBW doubt
    BBW "Also, I didn't think I'd have to say this, but there's no deliberate striking or splashing in the face of an opponent."
    show BBW haughty
    BBW "Other than that, you score by getting the ball into the net. The team with the most points wins. Simple enough, right?"
    MC "Easy enough."
    MCT "Easier said than done, more like it."
    BBW "To balance the teams we have to spread out the relative swimming skills of everyone as best as possible. That means I'll be on one team and Natsuko on the other."
    FMG "Hey! She's nothing special compared to me!"
    if isEventCleared("BBW009"):
        show BBW doubt
        BBW "It's nothing personal Mizutani-san, but I am factoring in your performance the last time we raced."
        show BBW haughty
    BBW "You'll have your chance to prove your skills if you want me to change my evaluation of them. Besides, you'll have the fortune of being on my team."
    BBW "That makes it me, Mizutani-san, and Aida versus Natsuko, Keisuke, and Honoka."
    show PRG neutral at Position(xpos=0.15, xanchor=0.5, yalign=1.0) with dissolve
    show FMG neutral at Position(xpos=0.30, xanchor=0.5, yalign=1.0) with dissolve
    show Natsuko neutral at Position(xpos=0.70, xanchor=0.5, yalign=1.0) with dissolve
    show BE neutral at Position(xpos=0.85, xanchor=0.5, yalign=1.0) with dissolve
    MCT "I was a bit relieved that I wasn't going to have Natsuko charging at me through the water like a hungry shark every time I got the ball."
    if isEventCleared("BBW009"):
        MCT "But after seeing Alice and Akira swim before, I could tell I was going to be an anchor around Natsuko's neck if she was expecting us to win."
    MCT "Alice's team seemed a bit stacked, but given Aida's timid nature, Alice probably expected her to give up more points at the goal than Honoka. It was the best that could be done with the numbers we had."
    BBW "Alright, let's get started. The ball starts in the center of the pool. Whoever gets there first to secure it will get the first possession."
    hide PRG with dissolve
    hide FMG with dissolve
    hide BBW with dissolve
    hide Natsuko with dissolve
    hide BE with dissolve
    MCT "With that, we all lined up at the roped lane markers set up as the playing field."
    BBW "Ready, set... GO!"
    MCT "With Alice's mark there was a mad dash to the ball from Alice, Akira, and Natsuko. After the earlier exchanges, it was undoubted that all three were trying to use this as an opportunity to put their swimming skills to the test against each other."
    MCT "I tried my best to keep up, but Natsuko left me in the dust... erm wake I guess, on her way to the ball."
    BBW "Got it!"
    MCT "Alice got there first and tipped the ball back behind her and Akira, blocking any meaningful attempt for me or Natsuko to obtain it and granting them the possession."
    MCT "Akira went back and grabbed the ball to begin advancing to the other half of the field towards our goal."
    MCT "And this was the start of when all hell began to break loose."
    MCT "I used the opportunity to fall back into a more defensive position in front of the goal. I had to be clever if I was going to stay in the game against opponents that could literally swim circles around me."
    MCT "Natsuko on the other hand, lunged forward like a shark that smelled blood in the waters to block Akira."
    MCT "This was of course a poor decision. Natsuko should be covering Alice instead of me."
    MCT "Alice easily slid through the water around my outside, giving a wide-open pass for Akira to send her, which she took full advantage of by immediately sailing it into the goal before Honoka could even react."
    show BE angry with dissolve
    BE "Oops!"
    BBW "Don't worry about it Honoka, even the best goalies can't stop every throw. Now you know what to expect."
    show BE neutral
    BE "Right! I think I got it now."
    hide BE with dissolve
    MCT "This gave us possession as the fielders had to get to the other side. I signaled for Honoka to pass the ball to me, while Natsuko and Akira were already locking horns in the middle of the defender side."
    MCT "This of course attracted Alice's attention. In any other context, her soft body coming aggressively for my ball would be a good thing, but the steely determination in her eyes told me she was going to eat me alive if I didn't get rid of this ball right now."
    MCT "I lobbed up a pass to Natsuko, hoping to exploit the height advantage Natusko had over Akira, which let her catch the ball, even with Akira practically trying to climb over her."
    MCT "In the brief window created by Akira failing to swipe the ball from her, Natsuko sent a screamer pitch straight into the goal."
    show PRG scared with dissolve
    MCT "Aida's 'block' was more of a panicked defense of her face than any real attempt to stop the ball. I couldn't blame her either."
    PRG "Sorry..."
    BBW "You're fine Aida. The goal is pretty wide, so it's difficult to cover- that's part of the challenge. You'll get better as the game goes on."
    show PRG unique
    PRG "Thanks."
    hide PRG with dissolve
    MCT "This pattern continued for most of the game, but much less points were given up as both Honoka and Aida felt more comfortable anticipating and going after the ball."
    MCT "As the game went on, my body was thrashed. Swimming while constantly keeping my head above water and trying not to lose the ball was hard work."
    MCT "Aside from Natsuko, the only advantage I had over the other players to keep myself high enough in the water was my height. Alice had her natural buoyancy, while Akira and Natsuko were built like battleships."
    MCT "I felt like I was riding a piece of driftwood in a maelstrom trying to keep up with the three of them. I was way past my limit, but the pace of the game and the competitive nature was enough to keep my energy levels on life support."
    MCT "I could see why Alice liked this game so much."
    $setSkill("Athletics", 1)
    MCT "What was not so fun however was Akira and Natsuko constantly at each other's throats the whole game."
    MCT "Aside from Alice, who wasn't too phased, the rest of us felt like chum in the water while two great white sharks vied for their portion."
    MCT "They both managed to rack up a couple of personal fouls and a handful of minor fouls from guarding each other so aggressively over the course of the game."
    show BBW angry with dissolve
    BBW "You can't pull on the other person."
    BBW "Hey! No splashing in her face."
    BBW "I don't care if it was an accident- it didn't look like one to me!"
    MCT "To be fair, a little bit of incidental contact was unavoidable. In one of my bouts of frantic flailing to dump the ball before Alice could snatch it away from me, I accidentally slipped an open palm boob grab on her as I tried to push myself back."
    show BBW surprised
    BBW "Easy there Keisuke!"
    MC "Sorry! It was an accident. I panicked!"
    show BBW haughty
    BBW "I understand, just try to be more careful."
    hide BBW with dissolve
    MCT "In my defense though, at that size, her boobs are pretty hard to avoid. If I start drowning, those would be my preferred floatation device."
    MCT "The game was almost done. We trailed Alice's team by 2 points. A time out had been called before the last few minutes so that Honoka could address a wardrobe malfunction that had her spilling out of her swimsuit."
    show BE surprised-2 with dissolve
    MCT "Alice wanted to save her the embarrassment, even though Honoka was probably the least concerned about that kind of thing out of anyone here."
    show BE neutral
    MCT "Going up against Alice and Akira, I honestly hadn't expected to win. Given their respective skills though, we would have fared a lot better if Natsuko was guarding Alice instead."
    MCT "If I couldn't get Natsuko to see reason, maybe I could exploit her competitive nature to give us a better shot."
    hide BE with dissolve
    MC "Natsuko, don't you want to win?"
    show Natsuko neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    Natsuko "Of course! That weakling's team is barely winning, even with Nikumaru-san's help. If we beat her, it would just solidify the fact she's dead weight."
    MC "I wouldn't really characterize Mizutani-san as any of that, but might I suggest you guard Alice instead, since she's the better player and you're the best one on our team, instead of constantly going after Mitzutani-san?"
    Natsuko "I see. Perhaps guarding the anchor hasn't been the best use of my abilities for the team. I think you're right, we should try that."
    MCT "Once the match started up again, our new strategy immediately proved more effective. Natsuko went straight for Alice, catching her off guard and managing a steal."
    MCT "Akira went for Natsuko, leaving me wide open for a pass from her as I made it towards the goal, setting me up for a wide-open pass and a subsequent goal."
    BBW "Hmph, so that's how it is now. I must admit by this point I didn't expect you to adjust your strategy."
    FMG "You too scared to compete with me, Natsy?"
    Natsuko "If you're content to let Hotsure-san swim up to the goal all by himself then you're dumber than even I thought possible."
    show FMG angry at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    FMG "Grrr..."
    MCT "With this change in line up we were able to even the scores up with only 30 seconds to go. Akira was clearly the most distraught about this turn of events, not likely keen on enduring Natsuko berating her for her team's loss."
    MCT "I was guarding Akira, standing, er- rather bobbing, in front of her between her and the goal when she managed to get a pass from Alice."
    Natsuko "You should have shot it Alice, she'll just miss."
    MCT "Mizutani-san clearly heard that. That was the straw that broke the camel's back. Whatever was going on between those two boiled up and over into a fire in Akira's eyes as she lost control."
    FMG "{i}Aaaaarrrrrrgh!{/i}"
    MCT "The last thing I remember seeing was Akira winding up her arm like she was going to throw a fast ball through a steel wall and firing it off like a cannon."
    stop music
    play sound Thud
    "THUMP!"

    scene black with fade
    "The sound of a sickening, dull thud was all that filled the air of the now silent pool."

    scene Pool with fade
    play music Bittersweet
    show PRG scared at Position(xpos=0.15, xanchor=0.5, yalign=1.0) with dissolve
    show FMG surprised-2 at Position(xpos=0.3, xanchor=0.5, yalign=1.0) with dissolve
    show BBW surprised with dissolve
    show BE surprised at Position(xpos=0.7, xanchor=0.5, yalign=1.0) with dissolve
    show Natsuko disappointed at Position(xpos=0.85, xanchor=0.5, yalign=1.0) with dissolve
    BE "Akira-chan! You killed him."
    FMG "It was an accident!"
    BBW "Don't joke about that now Honoka. Look, he's already coming to."
    PRG "Hotsure-chan! Are you okay?"
    MC "Whaa...? What happened? And why does my face hurt so much?"
    Natsuko "Because apparently someone can't aim their throws to save their life, much less yours."
    show BE embarrassed
    BE "Yeah, Akira-chan really plastered you across the face Kei-chan. You're lucky to be alive!"
    FMG "I {i}said{/i} it was an accident!"
    show BBW worried
    BBW "{i}Sigh...{/i}"
    BBW "Practice is over. Thank you for coming, everyone. I'll stay with Keisuke until he feels like getting up. Please go on ahead back to the lockers."
    show PRG sad-2
    show BE doubt
    show FMG sad
    Natsuko "Would you like us to help put away the equipment Nikumaru-san?"
    BBW "No, that's quite alright. Thank you for offering though. Please, everyone- go on."
    hide PRG with dissolve
    hide BE with dissolve
    hide FMG with dissolve
    hide Natsuko with dissolve
    MCT "The rest of the girls left back towards the locker. While slowly recovering from my stupor lying on the ground, Alice sulked by the side of the pool next to me with her legs in the water."
    show BBW sad
    BBW "{i}...sniff...sniff...eee{/i}"
    MCT "Was she crying? I snapped out of my haze and sat up."
    MC "Ow!"
    MCT "Okay so maybe that was a bit fast."
    MC "Alice, it's okay! I'm not hurt! Everything's fine. There's no need to cry."
    MCT "Hoping to get through to her. I scooted next to her and held her hand."
    BBW "{i}...sniff...{/i} You wouldn't say that if you could see the swelling on your face like I can, Keisuke."
    BBW "This was a complete disaster. {i}...sniff...{/i} I couldn't get enough people to do a full match- I didn't even have enough friends that I could ask!"
    BBW "I should have realized Akira and Natsuko were like oil and water. Aida and Honoka were mortified watching those two tear each other apart, but I pushed through with my idea anyway for my own selfish reasons- and you got hurt because of it."
    MCT "At this point Alice really started to cry, wiping her tears with one hand while holding mine tight with the other."
    MC "I don't see what was so selfish about you wanting to do this, and I don't see how you were supposed to foresee all of this happening."
    BBW "As the club president everything is ultimately my responsibility- if there were a club. No one is going to want to join after this catastrophe."
    MC "Well, maybe. But isn't it typical for successful business owners that only a handful of their ventures are ever successful? Not everything can be a smashing success, but you won't know if you don't try it."
    show BBW worried
    MCT "That analogy must have gotten through to Alice. She still looked pretty sad, but she appeared to have stopped sobbing, for the moment."
    BBW "That is true. Success is never certain."
    BBW "But it's not just that Keisuke. I know it's silly and naïve, but I wanted to use this club to help me make more friends."
    show BBW sad
    MCT "Alice started to tear up again. I didn't like to see this, but she clearly needed to get something off her chest."
    BBW "I know you like me Keisuke... but most people here don't. I know what other people say about me- that I'm just an uptight fatty... or some kind of food obsessed glutton."
    MCT "Alice was probably the most self-confident person that I knew. I was a bit surprised to hear her admit she had taken some baseless chatter from the gossip mill so personally."
    MCT "Then again, who wouldn't get worn down from hearing that kind of talk whispered behind their back all the time?"
    MC "Well, no one that I know is going around saying those things, and if they did, I would set them straight."
    BBW "Thank you Keisuke. I appreciate all that you and Aida do for me, but only having two friends... well a friend and a boyfriend, it still feels a bit lonely sometimes."
    MC "I don't think that that's the case. Why else would Honoka come out to join us, despite knowing nothing about water polo?"
    MCT "Don't you think you also have the respect of Natsuko and Akira from outclassing them with your swimming skills?"
    show FMG neutral at Position(xpos=0.7, xanchor=0.5, yalign=1.0) behind BBW with dissolve
    FMG "He is right you know. You were amazing out there today."
    show BBW surprised at Position(xpos=0.3, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Mitzutani-san! I didn't see you there."
    FMG "Don't mind me, I didn't overhear anything else. Here, I felt bad about what happened at practice today."
    FMG "Whether I have a good workout as a reward, or a bad workout as a consolation, I like to end it with an ice cream treat."
    MCT "Akira handed each of us a chocolate coated vanilla ice cream pop."
    FMG "Sorry again about your face Hotsure-san."
    MC "Thanks Mitzutani-san, but don't worry about it. I'm not worried about it."
    show FMG happy
    FMG "Ha! You're pretty tough bro, I'll give you that. I'm going to get going and leave you two love birds to it."
    hide FMG with dissolve
    MCT "Maybe she overheard more than she let on..."
    MC "Well, this wasn't quite the ice cream date I had envisioned, but I think it'll do just nicely."
    show BBW happy at Position(xalign=0.5, yalign=1.0) with dissolve
    BBW "Hehe, I suppose so. But I do think I still owe you, based on our initial deal."
    MC "Well it's more than enough for me."
    MC "Oh and Alice?"
    BBW "What is it, Keisuke?"
    MC "From now on, if you ever need a swimming partner, don't hesitate to ask me."
    show BBW aroused
    BBW "I just might take you up on that offer."
    jump daymenu

label BBW044:
    $setProgress("BBW", "BBW045")
    scene Dorm BBW with fade
    play music BBW
    MCT "It was an off day for the residents of Seichou Academy. Both the faculty and the students were given the day to unwind and destress."
    MCT "Many people liked to use this time to relax by themselves, away from others. This was a perfect opportunity for someone to have some alone time."
    show BBW neutral-2 with dissolve
    MCT "Me? I had been prattling the whole afternoon away with one, Miss Nikumaru."
    BBW "Would you care for some more Broken Orange Pekoe Fanning?"
    MC "You know you don't have to say it in full every time."
    show BBW surprised
    MCT "Alice pretended to look appalled as she poured another cup of tea."
    show BBW happy
    MCT "Her smug smile betraying the attempt at feigned hurt."
    BBW "Keisuke! I believe I have made it very clear before, not all tea blends are the same."
    MC "I know, I know. But honestly, growing up only exposed to green teas like sencha, it's hard to have such a refined palette like yours."
    show BBW neutral
    BBW "Then I feel sorry for you, truly I do."
    MCT "Setting down the kettle after pouring another serving, Alice's eyes widened with a rather sudden idea."
    show BBW haughty
    BBW "Maybe there just so happens to be a way to improve your taste buds' senses."
    MC "Uh, what do you mean by that?"
    BBW "If you may, please close your eyes for just a second-I must go prepare something."
    MC "You're scaring me a bit here, Alice."
    BBW "Oh please, you needn't worry. I just happened upon a rather ingenious idea is all, and you are the perfect recipient for my theory."
    MC "Was that an attempt at making me feel more on edge, or less on edge?"
    show BBW stern
    BBW "It was an attempt at explaining myself, now hurry up and close your eyes."

    scene black with fade
    MCT "Not wanting to pry further, I did as Alice said."
    MCT "I could hear the unmistakable sound of heavy footsteps, accompanied by the resulting vibrations through the floorboards as she made her way across the room."
    MCT "The footfalls stopped, and I could tell that she was opening some sort of cabinet."
    MCT "Only a few seconds later, did the same sound occur again. Once again, Alice's impactful stride sounded off as she approached."
    MCT "The temptation to peek was almost unbearable, my mind raced thinking of what she was planning. And almost as if on cue, I heard the opening of several boxes."
    BBW "It shall be ready in just a second, I do hope that you have not snuck a glance at my setup."
    MC "..."
    MCT "The possibilities flooded my blackened vision, the tension of the situation was almost palpable."
    BBW "There we go... alright! You may open your eyes now."
    scene Dorm BBW with fade
    show BBW haughty with dissolve
    MCT "I wasn't sure what to expect when my vision returned. But 5 teacups lined in front of me was quite possibly the last thing I expected to see."
    MC "Uhhhh, I think you've lost me here. 'Confused' doesn't even begin to describe how I feel right now."
    BBW "You are quite the clever one Keisuke, I am sure that you can deduce what my plan is here."
    menu:
        "You want me to identify tea?":
            jump BBW044_c1_1
        "Do you want to do a drinking game?":
            jump BBW044_c1_2
        "You poisoned one of these cups, and I have to pick one?":
            jump BBW044_c1_3

label BBW044_c1_1:
    $setAffection("BBW", 1)
    show BBW happy
    BBW "That is correct. Now, which cup would you like to try first?"
    jump BBW044_afterchoice_1

label BBW044_c1_2:
    show BBW doubt
    BBW "A drinking game with tea?"
    MCT "Alice paused, contemplating what I said."
    show BBW neutral
    BBW "I shall think about your idea later, but that is not what I had planned for today."
    BBW "Instead what I have devised is a plan to help you understand the various types of tea by taste alone."
    jump BBW044_afterchoice_1

label BBW044_c1_3:
    show BBW surprised
    BBW "...What?"
    MC "I dunno, the way you laid the cups out just really has me worried is all."
    BBW "My word, Keisuke- no, I do not plan to poison you!"
    show BBW haughty
    BBW "The things that go through your head..."
    MC "Well then what's with the setup?"
    BBW "My idea was to simply have you sample these teas, and then attempt to name each one by taste alone."
    jump BBW044_afterchoice_1

label BBW044_afterchoice_1:
    MC "Woah, Woah. Hold on, can I at least get a refresher first before I start sampling?"
    show BBW haughty
    BBW "Well I suppose that would make it more sporting..."
    BBW "Alright, listen closely, as I shan't repeat these hints."
    MCT "Before Alice could start listing off her selections, a knock came from the door."
    MC "Were you expecting anyone else to be here around this time?"
    show BBW doubt
    BBW "No, I am rather sure that-"
    show BBW surprised
    MCT "Alice's eyes shot wide open as a realization hit her. She snapped back to face me, talking in a whispered tone."
    BBW "Honoka!"
    MC "Honoka?"
    BBW "Last week, she came to me with a request for a new bra. The school-issued ones weren't fitting her needs appropriately."
    BBW "At the time she came to me, I had my hands full with other projects. So, I told her to meet me at this time next week."
    MC "And this time being now?"
    show BBW worried
    BBW "Yes..."
    MCT "Another series of knocks rang out, followed by a voice."
    BE "Alice?"
    show BBW surprised
    BBW "I'll be with you in but a second! Just finishing up preparations is all."
    MCT "Alice leaned in close to whisper to me, her breath tense but focused."
    show BBW worried
    BBW "My deepest apologies, Keisuke. But would you mind picking up the stray bits of cloth laying around?"
    MC "What, why?"
    BBW "Well simply look at this place, there are stray clothing articles and swatches everywhere! It's quite unbecoming of me to my customers."
    MCT "Now that she mentioned it, the state of the room became obvious. There were several articles of clothing dotting the room; oddly enough, most of them didn't seem to be her style or size."
    MC "Have you been working on new design ideas recently?"
    show BBW neutral
    BBW "Just a bit here and there, very little has been set in stone as of yet, but we can come back to that later, for now, I am asking you for help."
    MC "I mean, I don't think Honoka would mind it all that much-"
    BBW "Of course she wouldn't, I am well aware of that."
    show BBW stern
    BBW "But a promise was made to her, and I intend to make good on that."
    BE "If now isn't a good time, I could always just come back later."
    show BBW surprised
    BBW "No no, everything is fine."
    menu:
        "Leave the room":
            jump BBW044_c2_1
        "Follow Alice's instructions":
            jump BBW044_c2_2

label BBW044_c2_1:
    $setAffection("BBW", -1)
    MC "You're being ridiculous, Alice. Just because you slipped up on the timing doesn't mean you should lie."
    show BBW doubt behind BE
    BBW "Keisuke, please just-"
    MC "I'm out, I'll talk to you later."
    MCT "With that, I walked over and opened the door."
    show BE surprised at Position(xpos=0.4, xanchor=0.5, yalign=1.0)
    BE "Ahhhh!"
    MCT "Next thing I knew, Honoka came barreling forward into Alice's room. A soft 'plomf' noise sounded as she made contact with the floor."
    MCT "Having landed face or rather breast first onto the floor, Honoka looked up only to find a massive overhang of belly."
    show BE embarrassed at Position(xpos=0.3, xanchor=0.5, yalign=1.0) with dissolve
    show BBW sad at Position(xpos=0.7, xanchor=0.5, yalign=1.0) with dissolve
    BE "I know what this looks like, but I promise that I wasn't listening on the door."
    BBW "{i}sigh{/i} It's alright. I apologize for the distress caused by my lack of time management."
    MCT "Alice and I helped Honoka back to her feet, I said my goodbyes and left."
    show BE neutral
    BE "Keisuke was right, y'know. Trust me, I'm aware that keeping on top of things can be difficult with a factor."
    BBW "But this wasn't an issue with my condition interfering with my life..."
    BBW "I was just enjoying myself so much, a bit caught in the moment. Maybe my sharpened instincts are starting to dull."
    MCT "While I was sure that I had made the right decision for Alice's sake; part of me still wondered what caused her to act like that..."
    jump daymenu

label BBW044_c2_2:
    $setAffection("BBW", 1)
    MCT "Alice let out an ever so quiet sigh of relief before giving me a content smile."
    show BBW happy
    BBW "Thank you, I promise I'll make it up to you."
    MC "Worry about that later, Honoka is still waiting out there."
    MCT "Leaving my seat, I started to quickly snatch up the materials. The amount of obvious clutter was small, so my goal was to focus on that first."
    MCT "Swatches of all colors, shirts, and pants of all sizes; Alice was underselling just how much time she had put into this."
    MC "Where do you want me to put these?"
    show BBW neutral
    BBW "Oh, um..."
    BBW "There is room in my wardrobe, you can set them in there for now."
    MCT "As the wardrobe opened, I was surprised to find it already packed to the brim. Like Alice had told me, I began to hastily stuff the interior."
    MCT "A few bits of clothing were left before I realized that not all of it was going to fit. And no matter how hard I pushed, the wall of fabric refused to make space."
    MCT "Without thinking, I decided to try and shove myself into the blockage. Maybe then it would free some room."
    MCT "Taking a small step back, I bravely leaped forward... This proved to be a major error in planning."
    MC "MMMPH!"
    MCT "The few loose areas in the pile would be my undoing; for as soon as my shoulder pushed forward, I found myself quickly sinking into the mass of clutter."
    show BBW surprised
    BBW "Oh dear!"
    MCT "Upon hearing the commotion, Alice rushed over to check on me. Her cherubic face was awash with panic when she saw the state I was in."
    BBW "Kei, are you ok? Did you hurt yourself?"
    MCT "Try as I may, the weight of all the clothing kept me down. It wasn't a bad sensation, it was rather cozy."
    MC "I'm fine, just a bit stuck is all... could you give me a hand?"
    show BBW neutral-2
    BBW "Of course, here."
    MCT "Alice firmly grasped my one exposed hand and steadied herself to pull back. Her other hand gripping around my wrist as she found her footing."
    BBW "One, two, three!"
    MCT "One would think that several hundred pounds of mass would provide more than enough leverage. But as it turns out, I had gotten myself trapped even deeper than we thought."
    MC "Ow ow ow ow OW! Stop, please!"
    MCT "The sheer force being exerted on my shoulder joint was unbearable. A part of me thought Alice might rip my arm out of its socket if I didn't stop her."
    show BBW angry
    BBW "Damn it all... What to do, what to do?"
    MCT "Upon releasing me from almost certain removal, Alice quickly started to try for new ideas; but I knew that we didn't have much time left."
    MC "Alice, just shut the door."
    show BBW doubt
    BBW "I beg your pardon?"
    MC "Honoka can't see me like this, she'd have too many questions."
    MC "Think about how it'll make you look as well."
    BBW "This is absurd..."
    show BBW worried
    BBW "Please forgive me for this, Keisuke."
    MCT "With a look of both panic and embarrassment, Alice soberly closed the doors to the wardrobe. Leaving me just a sliver of light in the darkness."
    MCT "My eyes followed Alice as she hefted herself to the front door. Taking a few deep breaths to calm her nerves, she opened the door for Honoka."
    play music Peaceful
    show BBW neutral at Position(xpos=0.7, xanchor=0.5, yalign=1.0) with dissolve
    show BE happy at Position(xpos=0.3, xanchor=0.5, yalign=1.0) with dissolve
    BBW "First and foremost, I would like to personally apologize for the wait."
    MCT "Honoka gave a slight chuckle at her apology."
    BE "For what? Not immediately opening the door when I knocked?"
    BE "There's no need to apologize for not being 100%% punctual all the time, Alice."
    MCT "The sound of small talk continued as the two moved from the door to the bedroom."
    BBW "I hope the mess is not too bad, I was busy with other work and didn't notice the mess forming."
    show BE neutral
    BE "Oh you need not worry about it. The mess at my dorm dwarfs this by a good margin."
    MCT "I tried to readjust my position inside to try to listen in better. However, like a bad sitcom, it was this exact moment the wardrobe decided to release me from its grasp."
    MCT "In an instant I found myself staring up at Alice and Honoka, but with a look of surprise."
    show BBW surprised
    show BE surprised-2
    BE "Now that's a surprise for sure. Didn't take you as the peeping kind Kei-chan."
    MC "It's not like that at all! I would never."
    show BE confused
    BE "Then why else would you be hiding inside there unless you were..."
    MCT "She trailed off looking between me and Alice. It took both of us a moment before Alice blushed quite red."
    BBW "I can assure you that nothing of that sort of nature occurred."
    show BBW neutral-2
    BBW "To be forward on the reason, Kei was over helping me earlier with picking out new patterns for the store. He attempted to help me clean up when you arrived but became lodged in the wardrobe."
    BBW "He didn't want me to let you wait and asked to be left in there till our appointment had concluded."
    MC "There was some tea in there but that's about it."
    show BE embarrassed
    BE "Apologies for the insinuation, I do apologize if you took offense to that."
    BBW "You are fine dear, the situation does lend itself to that sort of thinking."
    BBW "Anyway, I suppose now with Kei here I could use the assistance with your request. Are you ok with Kei helping me measure you?"
    show BE seductive
    BE "I don't know if it's proper for a boy to see my bare chest as he will... but Kei-chan's a good boy, right?"
    show BBW happy
    BBW "He most certainly is."
    MCT "Alice reached into a purple polka-dotted bag beneath her desk and produced a measuring tape."
    show BBW neutral
    BBW "If you would please disrobe Honoka."
    MCT "Honoka smiled at me as she slowly unbuttoned her shirt"
    show BE happy
    BE "You certainly are a very lucky boy Kei-chan."
    show BBW stern
    MCT "Looking over Honoka's shoulder I noticed Alice giving me a slight glare. Wait was she..."
    MCT "Before I could consider the possibility Honoka finished with her shirt revealing a very overtaxed black bra."
    show BBW neutral
    BBW "This does certainly look like a task for two people."
    show BE unique
    BE "Hahh, I suppose my breasts are too big to be handled by one person."
    BBW "Could you please remove your bra as well Honoka?"
    MCT "Honoka passed me another teasing glance as she reached back to undo the bra clasp."
    show BE aroused
    MCT "I knew she was teasing me but this was getting to be a bit beyond that point. The overtaxed garment fell to the floor with a dull thud, leaving Honoka's chest bare and her still smiling."
    BBW "Now with that off, I can begin to get measurements. Kei would you stand in front so I can pass you the tape measure."
    MCT "She passed me the end of the tape."
    BBW "Kei please pull this across the very front of her breasts so I can get her bust measurement."
    MCT "At this point I was beginning to wonder whether Alice was doing this more as a test."
    MCT "Carefully, I pulled the tape across Honoka's breasts, trying to avoid grazing her exposed areolas."
    MCT "I tried to dart between looking down at her chest and Honoka's eyes to avoid staring for too long, lest I accidentally incur Alice's wrath."
    show BE happy
    BE "Just like playing Operation."
    MC "I don't remember Operation being this big."
    BE "Does this happen often? You assisting her with other clients that is."
    MC "No this is the first time I've helped with such a task. This fashion stuff is a bit out of my area of expertise so I feel like I'd be more hindrance than a help."
    BE "Nonsense, you have a great sense of fashion. Remember when you went as a cowboy for Halloween that one time?"
    MC "We were 9 and that was a store-bought costume. Plus the pants were very baggy."
    show BE shrug
    BE "It was still a fashion statement."
    MC "It was a fashion crime is what that was."
    show BE neutral
    MCT "Alice let out a muffled chuckle as she finished the last measuring."
    show BBW haughty
    BBW "Certainly sounds like a story you'll need to tell me at some point over tea Honoka. I'm quite interested in hearing about these childhood exploits."
    show BE happy
    BE "Oh certainly, I have many I can share later."
    show BBW neutral
    BBW "You are also good to redress now Honoka. This next part doesn't need you to be bare."
    MCT "As Honoka slung the bra back over her shoulders, Alice grabbed a thick black binder from beside her desk. Flipping the cover open revealed a massive catalog of designs complete with sample patches."
    BBW "One thing I can't stand about the school-issued clothes is they are quite drab, with no character."
    show BBW neutral-2
    BBW "Go ahead and look through and pick whatever suits your fancy. You ordered 3 so you can pick up to 3 if you so choose."
    show BE surprised-2
    MCT "Honoka stared at the assortment before her with eagerness."
    BE "I'm not sure 3 is enough, these are all great choices."
    BBW "Take your time."
    MCT "Honoka flipped through the pages for a few minutes while Alice and I continued to try and clean the earlier mess."
    show BE neutral
    BE "I believe I've come to a decision."
    show BBW happy
    BBW "Wonderful, what have you decided."
    show BE happy
    BE "Pink."
    show BBW surprised
    BBW "Uhh come again?"
    BE "A plain pink is fine. Maybe if it's possible some red roses on the nipple area."
    BBW "Is that for just one or all?"
    BE "All is fine, that way I don't have to worry too much about choosing."
    MCT "I couldn't help but stifle a chuckle watching Alice trying to process the request. For once she truly looked baffled."
    BBW "I can certainly see if that's feasible. I will say that is quite the detail to add, I should maybe add that as a permanent option."
    MC "No harm in adding it to the catalog, might have others who want it to."
    show BBW neutral
    BBW "I'll put it under consideration, as from a marketing perspective you may be onto something."
    BE "Thank you again for doing for me. It was certainly an interesting and fun experience. Who knows maybe I'll come back for another sizing."
    MCT "Naturally Honoka is a little excited about her tits getting bigger even when they are three times the size of her head."
    MCT "Her outfit style may change, but her personality is as consistent as ever."
    show BBW happy
    BBW "It's been no trouble and I'm available if you may need any sort of adjustments or fittings."
    BE "You've got it! Have a great day."
    MCT "With a short exchange of bows, Alice saw Honoka out. I continued cleaning up in the bedroom, noticing the forlorned teacups and pot."
    MCT "Gathering them, I walked them out to the kitchen, setting them on the counter beside some other dishes waiting to be done."
    hide BE with dissolve
    play music Bittersweet
    show BBW haughty at Position(xalign=0.5, yalign=1.0) with dissolve
    MCT "Turning around I was surprised to see Alice standing right behind me. Her belly only a few inches from my own."
    BBW "I would like to thank you for the help today Kei. While I'm no stranger to dealing with large breasts, Honoka-chan's are truly on their own scale and more than I could properly work with."
    MC "Oh it's nothing just..."
    MCT "She gently pressed a finger against my lips, cutting me off."
    BBW "Acknowledging this, I just want to be clear that I expect you to keep a slightly better composure if you want to assist me with her or similarly endowed clients again."
    MCT "She brings her finger down but does so rubbing it down my chest before pulling back."
    BBW "I just hope that if the moment ever comes, I expect you to give me the same sorta looks I saw you giving Honoka-chan. Do you understand?"
    MCT "I just nodded my head slowly."
    MCT "She leaned forward and kissed me. Her body gently pressed me against the counter. The sensation was best  described as being encased in a pillow."
    show BBW happy
    MCT "Pulling back she booped me on the nose before waddling back to her room."
    BBW "I wonder if you'd respond that way to another predicament like mine. Like Sakura, perhaps?"
    MCT "As her door shut I had a million thoughts going through my head. The suddenness of her forwardness had shocked me on many levels and left me with many questions."
    MCT "How much ogling did she see me doing? Would I have done the same with another weight gain girl? Was she inviting me to take things further?"
    MCT "But somehow out of all the questions swirling about, the one that fell from my mouth was."
    MC "Who's Sakura?"
    jump daymenu

label BBW045:
    scene black with fade
    $setProgress("BBW", "BBW046")
    "It's a beautiful Sunday morning."
    MC "zzzzzzzzzz"
    "And I was spending it the best way I could..."
    MC "zzzzzzzzzzzzzzzzzzzzzzzz"
    MC "zzzzzzzzzzzzZZZZZzzzzzzzzz"
    play sound AlarmClock
    "{color=#FF0000}BREEET BREEET BREEET BREEET!{/color}"
    "...or so I thought."
    MCT "Did I really set an alarm for Sunday morning?"
    "I turned over in my bed and fumbled around for the alarm."
    play sound AlarmClock
    "{color=#FF0000}BREEET BREEET BREE-{/color}"
    "I finally found the off button."
    MCT "Damn alarms and them doing exactly what we want them to."
    "I struggled to open my eyes as the battle for body control commenced."
    scene Dorm Interior with fade
    RM "Morning."
    play music RM
    MCT "I will never get used to this."
    MC "Morning."
    "I sat up to face my less than sociable roommate."
    show RM neutral with dissolve
    MC "What time did you wake up?"
    RM "Oh only a couple hours ago."
    MC "The alarm says it's not even 8am yet."
    RM "The early bird gets the worm."
    MC "I guess."
    "I attempted to get out of bed, giving Daichi a performance akin to a corpse reanimating."
    RM "Late night?"
    MC "Who goes to bed early on a Saturday night?"
    RM "Productive members of society."
    MCT "He's got me there."
    MC "I can be productive any other day of the week."
    RM "Well you can be productive in your relationship today at least."
    MC "What's that supposed to mean?"
    RM "Remember how we synced our calendars so if one of us forgets something, the other can remind them?"
    MC "No."
    RM "Well we did and you definitely agreed to it, I'm sure you'll remember as you wake up more."
    RM "Your phone hasn't buzzed once so it should be in do-not-disturb."
    MCT "But what would I even have set on my calen-"
    MCT "{i}Oh no.{/i}"
    stop music
    hide RM with dissolve
    "I quickly disabled do-not-disturb to allow notifications to display."
    "My phone immediately replicated the sound of a beehive as a swarm of texts from Alice came through at once."
    MCT "I forgot that was today."
    "I quickly opened my messages to see everything that I missed."
    BBWCell "Hey, don't forget to sleep at a responsible time tonight, we have a big day tomorrow.    8:32pm"
    BBWCell "I'm assuming you have already fallen asleep, it isn't like you to not respond. I hope your dreams are pleasant. Goodnight.    8:47pm"
    BBWCell "Good morning Keisuke, I hope you slept well. Please come to my dorm at 7:30 so I can tell you what to expect today.    7:10am"
    if getFlag("BBW035_c2_2"):
        BBWCell "Don't forget to wear your suit, you'll look great.    7:11am"
    elif getFlag("BBW035_c2_1"):
        BBWCell "You will look a little overdressed in your suit, but it will still look rather appropriate.    7:11am"
    else:
        BBWCell "I bought you a suit for the occasion, you can get changed in my dorm.    7:11am"
    "I looked at the clock in the corner of my phone screen."
    MCT "7:29am, this is not going to end well."
    "I got up and left Daichi to his book as I went to brush my teeth."
    RM "Keisuke, are you familiar with the story of Moby Dick?"
    MCT "Since when does he read classical literature?"
    MC "Huhr oh it"
    RM "It's about the captain of a whaling ship named Ahab, who dies trying to hunt the whale that bit off his leg."
    MCT "Why is he even telling me this?"
    MC "mm-hm"
    RM "So his ambition led to him being the architect of his own demise."
    MCT "I'll just go along with it."
    MC "Yoh poin?"
    RM "I just think it's a good story and that 'don't lose your rationality to desire' is a good message."
    "I spat out the toothpaste and glanced over my teeth in the mirror. Perfect pearly whites."
    show RM neutral with dissolve
    MC "Are you trying to say some of this applies to me?"
    RM "I'm saying it can apply to anyone."
    if getFlag("BBW035_c2_1") or getFlag("BBW035_c2_2"):
        "I started to get dressed, grabbing my suit from my wardrobe."
    else:
        "I started to get dressed, choosing a simple track suit for the trip to Alice's dorm."
    RM "To be overpowered by willpower is human, it is possible that striving for something more can deny you of it."
    MCT "Where has this philosophical side come from?"
    "I finished tying my shoelaces and headed for the door."
    RM "Goodbye Keisuke, and don't let yourself get swallowed by the white whale."
    "I shut the door and left for the girls' dorms."
    scene School Inner with fade
    MCT "..."
    MCT "He probably didn't intend that..."
    scene School Planter with fade
    "Roaming school grounds without another person in sight was a surreal experience."
    "It was extremely peaceful, it seemed almost separate from the rest of the world."
    MC "I guess this is the calm before the storm."
    scene Dorm Exterior with fade
    "I arrived at the girls' dorms and took out my cell phone, texting Alice rather than knocking."
    MCCell "<Sorry for the delay, I'm outside.>    7:48am"
    "A few moments later, the door opened."
    play music BBW
    show BBW angry with dissolve
    "She may have been furious with me, but the way the morning sun made her hair glow was so alluring."
    "She was stunning."
    BBW "Keisuke."
    "...not that it changed her current emotion."
    BBW "Do you have any idea what this means?"
    MC "Alice I-"
    BBW "No Keisuke, you went to bed far too late and that means you didn't get a healthy amount of sleep."
    show BBW sad
    BBW "I'm not upset that you're late at all, we still have plenty of time to get there. I'm upset that you sacrificed your wellbeing for this."
    MC "Alice I assure you I'm fine, I can function perfectly well on this amount of sleep."
    show BBW neutral
    BBW "Well if you say you're fine then I believe you."
    if getFlag("BBW035_c2_1") or getFlag("BBW035_c2_2"):
         BBW "And you look so handsome in your suit, so I trust your ability to maintain appearances. Now come inside so I can tell you what to expect today."
         jump BBW045_art
    else:
        BBW "Now come inside and change into your suit, you're going to look so handsome."
        jump BBW045_suit

label BBW045_art:
    $setFlag("BBW045_art")
    scene Dorm BBW with fade
    "I entered Alice's dorm rather quietly, only to see that Kodama-san was already wide awake."
    show BBW neutral at Position(xpos=0.8) with dissolve
    show PRG pj-happy at Position(xpos=0.2) with dissolve
    PRG "Keisuke! Good morning!"
    if getAffection("PRG") > 3:
        MC "Good morning Aida."
        BBW "We can sit on my bed Keisuke, I have my laptop here with me."
        hide PRG with dissolve
        "Aida climbed back into bed and started reading a baseball history book, of all things."
    else:
        MC "Good morning, Kodama-san."
        BBW "Come and sit on my bed Keisuke, I have my laptop here with me."
        hide PRG with dissolve
        "Kodama-san climbed back into bed and started to read some sort of science textbook."
    "I sat on Alice's bed. She placed her laptop on my... well... lap, and the image displayed on it was unmistakably Van Gogh's 'Starry Night', a painting anybody could recognise regardless of artistic knowledge."
    MC "Alice, why are you showing me this?"
    BBW "Do you know what this painting is?"
    MC "Yes, Starry Night by Van Gogh."
    BBW "Good, now tell me about the picture."
    if getSkill("Art") > 4:
        MC "It was painted in 1898, and it's debatably his most famous piece, alongside Sunflowers."
    else:
        MC "It was painted in the 1800s right? And it's obviously a famous picture."
    BBW "You're not wrong Keisuke, but anybody can list simple facts about a painting, an individual of good tastes would describe the artistic methods and techniques at play."
    BBW "Notice how each stroke of the brush was {i}physically{/i} done; quick and short individual strokes- but many of them."
    BBW "This is a staple of Van Gogh's work and will allow you to easily identify one of his paintings."
    $setSkill("Art", 1)
    MC "Ok Alice, but {i}why{/i} are you telling me this?"
    BBW "As you know, we are attending a wine tasting in... 40 minutes, minus 15 minutes travel time."
    BBW "The building hosting the event is a small art gallery and a high-class elegant café, which will be closed, for the wealthier residents of this island."
    BBW "Of course this is still just that- an island. You won't meet any world famous CEOs and only the more obscure paintings there are original pieces, but it still provides a high society experience for the island residents who seek it."
    "I had read that we were attending a wine tasting when I disabled do-not-disturb on my phone and the calendar notification displayed, but in my groggy state I had not properly processed the thought."
    "We aren't old enough to drink yet."
    MC "Alice, how are we attending a wine tasting when we aren't old enough to drink?"
    show BBW haughty
    BBW "Keisuke, what kind of businesswoman would I be if I wasn't aware of legal loopholes?"
    BBW "The law states that all citizens and tourists within Japan must be age 20 to purchase or consume alcohol."
    MC "Right, and we aren-"
    BBW "Aren't purchasing or consuming alcohol."
    BBW "There isn't any law against merely tasting alcohol, and we aren't purchasing it from the business, the event is a fundraiser and attendance is free- with invitation."
    show BBW neutral
    MC "Remind me again why your father got us invitations?"
    BBW "He wants {i}me{/i} to attend after I called him to let him know about the charitable work and how it will invest in the development of Seichou and its community."
    BBW "You are naturally my plus one."
    MC "What is the fundraiser for?"
    BBW "Creating jobs around Seichou for former students."
    BBW "Most workers on the island are former students already but every year there are more people with growth factors who cannot be hired, as employers would obviously discriminate based on their bodies."
    BBW "One idea I wanted to put forth was giant students being employed for construction, creating the buildings that would house the jobs for students with other growth factors."
    BBW "Now, if there are no more questions, I'd like to describe the various terminologies of wine tasting to you."
    MC "Alright."
    "I nodded in understanding."
    BBW "Pay very close attention Keisuke, you will need to know this information and refer to it during the event."
    BBW "First is 'acidity,' this is how much a wine tingles in your mouth, like sour candy."
    BBW "If a wine has a very high acidity, to the point of being unpleasant, you may refer to it as 'austere.'"
    BBW "In opposition to this, a wine with no acidity is referred to as... flabby."
    BBW "Don't say it."
    "I fought a smirk attempting to spread across my face."
    MC "I wasn't going to, Alice."
    BBW "Of course you weren't."
    BBW "Now if a wine has high acidity, but not to an unpleasant degree, it can be referred to as 'bright.'"
    BBW "A wine with a low acidity, but not to the point of necessarily lacking in it, is described as 'blowsy.'"
    BBW "Now for more characteristics, if a wine has too much fruit it can be called 'flamboyant,' this is usually a slight insult to the maker as wines with too much fruit are seen as trying to grab attention; A cheap tactic, if you will."
    BBW "A wine that tastes simple, but not necessarily bad, can be called 'crisp.' This is a wine that most people can enjoy just fine, but won't be anybody's favourite."
    BBW "The next term is one I'm sure you'll find amusing. Wine that fills the mouth to a displeasing and negative extent is labelled a 'fat' wine."
    "I had a slight desire to chuckle, purely due to the irony of fat being deemed negative. I guess wine 'intellectuals' aren't all they claim to be."
    "The urge was easily fought."
    BBW "Last up before we leave is 'complex,' it is exactly as it sounds. A complex wine will change as you taste it to not be pinned down by a single label."
    BBW "Absolutely never use the term complex as a last resort, it is only to be used when you can {i}describe{/i} how it is complex. It is better to admit uncertainty than to lie in an attempt to seem more intelligent."
    MC "Only use complex when I can explain why, got it."
    BBW "I think that is everything you'll need to know. This is of course the very basics of wine tasting but as the event is primarily a fundraiser, this should cover everything."
    BBW "We should leave now, I wish to walk there to enjoy this beautiful day- as well as clear my mind for the event."
    BBW "The best things in life aren't free, but a scenic route is."
    jump BBW045_wine

label BBW045_suit:
    "Alice gestured at me to shush and then beckoned me in."
    scene Dorm BBW with fade
    "The lights were turned off, though we could see fine due to the direct sunlight."
    show BBW neutral at Position(xpos=0.8) with dissolve
    "It was quickly apparent that Kodama-san was still asleep."
    "As a roommate with nothing to do should be at this hour."
    #(Alice and Kei whisper from here)
    BBW "Here is your suit, you can just get changed here, Kodama-san won't exactly be able to see."
    "Alice had the suit hung over her bed frame with a clothing hanger, clean and pressed."
    "It was a dark blue number, looking rather subdued compared to 'fancy' suits, but it was a fine piece for most occasions."
    "Alice turned around and I began to undress, using slow movements to make as little sound as possible."
    show BBW neutral at Transform(xzoom=-1) with dissolve
    BBW "Staring at the wall isn't exactly fun, but the bathroom door is creaky so getting changed in there risks waking up Kodama-san."
    MC "I'll try to be as fast as I can."
    BBW "No, it's best you take your time, Kodama-san doesn't deserve to be disturbed."
    "I had finished taking off my tracksuit, and reached for the dress."
    MC "Onto the suit now."
    BBW "Good, good. Let me know when you're done."
    "I slowly pulled up the pants and fastened the belt with careful movements."
    MCT "This silence is like being in a low budget horror film."
    "Fastening the belt buckle at a comfortable tightness, I moved onto the shirt."
    "As I had buttoned the shirt up halfway, I muttered a thought out loud."
    MC "{i}Nearly done.{/i}"
    BBW "Done? Oh good."
    "As I realised the error I had just made, Alice turned around to face me."
    show BBW neutral at Transform(xzoom=1) with dissolve
    show BBW aroused
    BBW "Umm, Keisuke I don't think you're done yet."
    MCT "The fact that she isn't looking away is a great compliment."
    MC "I said nearly done."
    BBW "I must have misheard. Carry on then."
    "It was apparent she didn't intend to turn back around."
    "I suppose that whispering in the dark in the bedroom can be a little sensual."
    "Still though, no reason to tell her to look away, it is only putting a shirt on after all."
    MC "Okay, Alice."
    "I buttoned up my shirt, continuing to be as silent as I could."
    "When I was done, Alice corrected my collar for me and reached for my tie."
    BBW "Now to show you how to properly tie a tie."
    MCT "This is not how I saw my morning going."
    "She put the tie around my neck, somehow performing such an average task with extreme elegance."
    BBW "This is how high society does it."
    "She tightened it rather slowly and deliberately, maintaining eye contact with me the whole time."
    "When she was done, she handed me my jacket."
    show BBW neutral:
        ease 0.5 xpos 0.5
    BBW "Come on now, we are pressed for time and I have to explain wine tasting."
    "Alice sat down on her bed and I quickly threw on my jacket and joined her."
    BBW "Now, I need to describe the various {i}terminologies{/i} of wine tasting to you."
    "I nodded in understanding."
    BBW "Pay very close attention Keisuke, you will need to know this information and refer to it during the event."
    BBW "First is 'acidity,' this is how much a wine tingles in your mouth, like sour candy."
    BBW "If a wine has a very high acidity, to the point of being unpleasant, you may refer to it as 'austere.'"
    BBW "In opposition to this, a wine with no acidity is referred to as... flabby."
    BBW "Don't say it."
    MCT "I fought a smirk attempting to spread across my face."
    MC "I wasn't going to, Alice."
    BBW "Of course you weren't."
    BBW "Now if a wine has high acidity, but not to an unpleasant degree, it can be referred to as 'bright.'"
    BBW "A wine with a low acidity, but not to the point of necessarily lacking in it, is described as 'blowsy.'"
    BBW "Now for more characteristics, if a wine has too much fruit it can be called 'flamboyant,' this is usually a slight insult to the maker as wines with too much fruit are seen as trying to grab attention; A cheap tactic, if you will."
    BBW "A wine that tastes simple, but not necessarily bad, can be called 'crisp.' This is a wine that most people can enjoy just fine, but won't be anybody's favourite."
    BBW "The next term is one I'm sure you'll find amusing. Wine that fills the mouth to a displeasing and negative extent is labelled a 'fat' wine."
    "I had a slight desire to chuckle, purely due to the irony of fat being deemed negative. I guess wine 'intellectuals' aren't all they claim to be."
    "The urge was easily fought."
    BBW "Last up before we leave is 'complex,' it is exactly as it sounds. A complex wine will change as you taste it to not be pinned down by a single label."
    BBW "Absolutely never use the term complex as a last resort, it is only to be used when you can {i}describe{/i} how it is complex. It is better to admit uncertainty than to lie in an attempt to seem more intelligent."
    MC "Only use complex when I can explain why, got it."
    BBW "I think that is everything you'll need to know. This is of course the very basics of wine tasting but as the event is primarily a fundraiser, this should cover everything."
    BBW "We should leave now, I wish to walk there to enjoy this beautiful day- as well as clear my mind for the event."
    BBW "The best things in life aren't free, but a scenic route is."
    jump BBW045_wine

label BBW045_wine:
    scene Dorm Exterior with fade
    show BBW neutral with dissolve
    BBW "The weather on this island truly is a wonder."
    MC "It truly is."
    scene School Exterior with fade
    show BBW neutral with dissolve
    BBW "It's a shame really, a hotel and resort would be perfect here. Mass tourism would greatly improve the economy, though that would directly interfere with the school and its students."
    MC "That is true. The island has a lot of hidden gems to offer."
    BBW "Perhaps when I am an experienced businesswoman in my own right, growth factors will be widely known among the general populace. This would lead to more relaxed regulations on the island."
    MCT "She really does plan these things ahead."
    BBW "... although, mass tourism would severely impact the lives of the students here depending on where the resort is located."
    BBW "It wouldn't be fair to deny students of the academy their largely undisturbed access to the scenic parts of the island, considering of course that students have no say in their attendance of the school."
    MCT "This monologue isn't going to end any time soon, is it?"
    scene Town with fade
    show BBW neutral with dissolve
    "Reaching the town was a sad end to the scenic walkways."
    BBW "Furthermore..."
    MCT "Not that I got to fully enjoy such scenic walkways."
    BBW "There is no denying that some individuals would visit the island for less respectable purposes."
    BBW "I know some people would come here purely to see students with growth factors that they find pleasing; our conditions would be treated like some kind of game for their fetishism."
    MCT "She said she wanted to clear her head for the wine tasting. If business conceptualisations are how she does that, I have no desire to speak up."
    BBW "Of course among students here it is a different story, they would be here regardless and are the same age as the students they find appealing."
    show BBW haughty
    BBW "I know one such student who acted on the opportunity."
    "I could feel my cheeks turning red."
    show BBW neutral
    BBW "However, masses of individuals specifically seeking such things specifically would lead to very very unpleasant experiences, prompting many students to stay in their dorms all weekend and ultimately ruining the island for everyone."
    BBW "I simply cannot allow this to occur. Money will never be worth the malice behind it. Not for moral individuals anyway."
    MCT "So Alice has no malice. Heh."
    BBW "It's such a shame; if people were more decent, this island would be an untapped tourism gold mine."
    BBW "Oh! Here, it's just around this corner."
    "We turned the corner and I saw one building with a security guard at the door, clearly showing this was the gallery."
    "The building was much more modern than I had anticipated, having plenty of window space on the exterior. It looked like a modern office building from the outside."
    "As we approached, the security guard, evidently a man with a muscle growth factor, spoke up."
    Guard "Invitation and name please, Sir."
    BBW "Personally I prefer to be called Miss, but Madam will do too."
    "The guard was clearly surprised it was Alice that was the invitation holder."
    Guard "My apologies Miss. Name and invitation please."
    BBW "Nikumaru Alice. This is my plus one."
    "Alice showed the guard her invitation."
    Guard "Allow me to double check this, standard procedure."
    "The guard took a moment to check the authenticity of the invitation."
    Guard "Everything is in order, welcome to the Usuda Art Gallery, Madam."
    BBW "Thank you."
    "The guard opened the door for us and smiled as we entered."
    scene Art Gallery with fade
    show BBW neutral with dissolve
    BBW "This place certainly looks better than it does on their social media."
    BBW "The art actually gives off a nice atmosphere, even if all of the popular pieces here are imitations."
    MC "I agree, the mood is a lot more relaxed than what I'd anticipated."
    BBW "Here comes the first taste."
    "A waiter approached us with 2 glasses of wine on a serving tray in one hand and a bucket in the other."
    Waiter "Sir, Miss, 'Avignon Southern'."
    "He was obviously instructed to keep all conversation short and to the point."
    BBW "Thank you."
    "Alice and I each took a glass and sipped the contents."
    MCT "It's... simple. It doesn't have any defining characteristics."
    MCT "What was it called again? Avignon? That sounds French."
    MCT "I suppose it was made to appeal to as many consumers as possible, although I doubt anyone would have this as a favourite."
    "Alice spat the wine into the bucket, to which I immediately followed."
    Waiter "Very good."
    "The waiter left to go and get a new wine to begin serving again. It was clear we were the last to drink that wine."
    BBW "So, how was it?"
    menu:
        "Bright.":
            MC "It didn't do anything particularly well, it was simple, so it was bright."
            show BBW sad
            BBW "No Keisuke. A wine that does nothing particular and stays simple is crisp. A bright wine is a wine with high acidity."
            show BBW neutral
            BBW "I can forgive one mistake Keisuke, since you are only talking to me and it's natural you are nervous."
            BBW "However, please remember what I told you when you speak to other guests here."
            BBW "Normally I wouldn't worry so much about appearances to people not involved with my father's company, but these people would likely dismiss my ideas over something so superficial, and I cannot allow that to happen to the giant students of Seichou."
        "Crisp.":
            MC "It was a simple wine, so it was crisp."
            MC "The kind of wine anybody finds acceptable but nobody finds exciting."
            show BBW happy
            BBW "That is absolutely correct Keisuke. I'm glad you remembered."
            BBW "I see we'll face no issues mingling with the guests here now."
            BBW "Normally I wouldn't worry so much about appearances to people not involved with my father's company, but these people would likely dismiss my ideas over something so superficial, and I cannot allow that to happen to the giant students of Seichou."
            show BBW neutral
        "Flamboyant.":
            "It didn't do anything particularly well, it was simple, so it was flamboyant."
            show BBW angry
            $setAffection("BBW", -1)
            BBW "Keisuke, not only does this mean you were not paying attention to me, it means you aren't even capable of knowing what the words mean and making informed assumptions."
            BBW "How on earth would a wine that stays simple and does nothing extra ever be referred to as flamboyant?!"
            BBW "Do you even know what flamboyant means?"
            MC "Alice I-"
            BBW "Keisuke, no."
            show BBW sad
            BBW "I understand you may be nervous and that could lead you to make mistakes but something like this is just silly."
            BBW "It established that when you forget something, you won't even use your own logic and reason to form an opinion."
            BBW "Please Keisuke, try to be better for the duration of this event."
            show BBW neutral
            BBW "I know you're better than this, so please display it."
    "Suddenly the waiter emerged from the back room, carrying the bucket again."
    "Though this time there were 10 glasses on the serving tray."
    "As he did so, a woman came over to speak to Alice."
    "Two things were immediately clear about this woman."
    "The first was that she had attended the school when she was young, as her growth was self-evident."
    "The second was that she had had plastic surgery- her face appears to be almost poorly made. Though her natural beauty was still clear behind this."
    Misaki "You must be Nikumaru-san. It's an honour to meet you."
    BBW "How do you know who I am?"
    Misaki "Well, you were the only person on the guest list with blonde hair and blue eyes. It is quite a giveaway."
    Misaki "But if you're referring to knowing who you are as the daughter of Nikumaru Daitaro- well, when Nikumaru Daitaro contacts you and says he wishes for his child to be invited, it is not a moment you decline nor forget."
    Misaki "Your father has donated a very generous amount of over 20 million yen to this project. It is only natural I thank you personally as you attend in his place."
    BBW "Well thank you for inviting us. We are more than happy to fund such a good cause."
    Misaki "The pleasure is all mine. Now, where are my manners?"
    Misaki "My name is Usuda Misaki, owner of this establishment and general art enthusiast - though I made my money by selling high quality tailored suits and dresses to individuals with growth factors leaving the academy."
    BBW "Alice Nikumaru. Please don't take my surname as a reason to treat me differently, I am my own person despite my father's status. Oh, and call me Alice."
    Misaki "Of course Alice, and who is your plus one?"
    BBW "This is my boyfriend, Hotsure Keisuke."
    MC "It's a pleasure to meet you madam, please call me Keisuke."
    Misaki "As you wish. Oh! Here comes the next wine."
    "The waiter had finished giving out the wine to the others and awaiting their verdict."
    Waiter "Sir, Madams, 'Amalfi Deep-Red'."
    Misaki "Thank you, Yamada-san."
    "We each took a glass and began our tasting."
    MCT "Wow, now that is a low acidity, it almost tastes like a still juice."
    MCT "And the fruit is very strong, the creators of this wine almost seem like they're compensating for something."
    "Misaki was done with her tasting and disposed of the wine, Alice and I followed suit."
    "The waiter went back into the storage room to get the next wine."
    Misaki "So, what did you each think? Specifically about the acidity."
    menu:
        "Blowsy.":
            MC "It's blowsy. The acidity is a little low."
            BBW "I'd say the acidity is far too low. This is a flabby wine, no doubt."
            Misaki "I have to agree with Alice here. Blowsy wines have a low acidity, not an absence of it."
            Misaki "This particular wine is actually Italian, so having a relaxed product naturally reflects the culture. Of course the wine would be sold in far greater quantities there than here in Japan."
        "Flabby.":
            MC "There is a great absence of acidity, I'd certainly call this wine flabby."
            BBW "I agree, the wine is far too relaxed and sweet for most palates. It is almost like juice."
            Misaki "I couldn't agree more. This particular wine is actually Italian, so having a relaxed product naturally reflects the culture. Of course the wine would be sold in far greater quantities there than here in Japan."
        "Bright.":
            MC "It's very bright. The low acidity is rather displeasing."
            Misaki "Keisuke, the wine has a low acidity. Bright is used to define wines with high acidity."
            BBW "I'd call the wine flabby, there was too great an absence of acidity to refer to it as blowsy."
            Misaki "I agree, Alice. The wine is Italian, so I suppose they opted for a sweeter and more relaxed taste to reflect their culture."
    Misaki "So, Alice, are there any ideas you have for making jobs available to individuals with growth factors?"
    BBW "Yes, actually. One idea I have been very anxious to pitch is using giant students for construction."
    BBW "They are the ones most greatly affected by their factors and yet would be so useful in this field. This also guarantees a workforce for the construction of buildings where people with other factors can work, creating even more jobs."
    Misaki "Wow, I had never considered that before. That would greatly speed up any construction project. You really are your father's daughter with this kind of innovation."
    show BBW happy
    BBW "I'm just glad that we can start this process soon. Giant students really have a harder time than the rest of us."
    Misaki "You're absolutely right. Alice I will see to it personally that your father's donation goes to this. We will also be contacting the school about including it in the curriculum for giant students."
    "The waiter once again emerged from the wine storage room."
    show BBW neutral
    Misaki "So, Keisuke, are there any ideas you had?"
    "This caught me off guard, I had expected Alice to be the only one asked such questions."
    "I could quickly make something up to impress Alice or I could admit I don't have an idea."
    menu:
        "Make it up.":
            $setFlag("BBW045_c3_1")
            MC "Well I uhh..."
            MC "I had the idea that uhh..."
            MCT "They're never going to buy this."
            MC "Maybe people with muscle factors can be used for security?"
            $setAffection("BBW", -1)
            Misaki "Did... Did you just make that up on the spot?"
            Misaki "We have a security guard just outside who attended the academy with muscle growth, he and I were in the same class."
            Misaki "You saw him at the door."
            Misaki "Oh now this is just a funny story, I'm going to go and tell him, I'll be right back."
            show BBW angry
            BBW "Keisuke."
            MCT "(gulp)"
            BBW "Why on earth would you attempt something like that?"
            MC "I thought it would impress you."
            BBW "You thought fumbling over your words to suggest something already in place that we experienced first hand just a few minutes ago would impress me?"
            MC "Alice I-"
            BBW "Keisuke, you aren't here to impress me. You're here to very simply do what I ask of you, following extremely simple instructions."
            BBW "Here comes Misaki, don't do something stupid like that again."
            show BBW neutral
            Misaki "Keisuke that was hilarious, Suji- I mean, our security guard loved it."
            "The waiter once again emerged from the wine room with a fresh 12 glasses."
            Misaki "Alright, let's wait for this next one."
        "Tell the truth.":
            MC "No actually, I didn't think of anything that wouldn't have already been suggested. I'm not quite one to think outside the box like Alice is, so to speak."
            Misaki "Ah that's fair, there are only so many possibilities anyway, we have to run out eventually."
            Misaki "It's good that you're honest about it. Some partners would try to make something up to impress their love. It takes a mature individual to be beyond that at your age."
            show BBW happy
            BBW "Of course. I have as fine a taste in men as I do in all things."
            "By now my cheeks were replicating the shade of that last wine."
            MC "Thanks, Alice."
            $setAffection("BBW", 1)
            Misaki "Aww, that's lovely. You two make a great couple."
            show BBW neutral
            Misaki "Now then, here comes Yamada-san with the next wine."
            "The waiter was just finishing with the last group and heading towards us."
    Waiter "Sir, Madam, Usuda-san, 'Kensington Thoroughfare'."
    "Again, we each took the glass closest to us and experienced the wine."
    MCT "Oh wow, that is very tingly. That means high acidity."
    MCT "Too high for some, but not so absurdly high that everybody would be displeasing."
    MCT "There is also not much fruit in this, it is quite bitter."
    "It had been noticeably less time than we had spent tasting the others and Alice had already finished, evidently we were eager to get this wine out of our mouths."
    Misaki "I did not like that one."
    Misaki "Yamada-san, is the next one to be the final one?"
    Waiter "Yes, madam."
    Misaki "Excellent."
    "The waiter entered the storage room once again to retrieve the final wine."
    Misaki "So, Alice?"
    BBW "I did not like this one either, though I don't think the acid was so high that nobody can enjoy it, it is certainly a more niche taste."
    BBW "Keisuke, your verdict?"
    menu:
        "Bright.":
            MC "Yes it was very bright, but not quite austere."
            MC "May I ask what country this wine is made in?"
            Misaki "England."
            MC "Well, British people tend to be direct and hardy, even if it means their own experience is worse for it, so I believe this is reflected by the bitter taste and low fruit."
            Misaki "I believe you're correct. Most wines tend to reflect the qualities of the people who made them, as we saw with the previous two."
            BBW "I agree, culture plays a large role in the development of any product."
        "Austere.":
            MC "The acidity was too high, this wine is austere."
            BBW "I disagree keisuke. Though the 3 of us do not like it, I believe it is not so acidic that it warrants the title of austere."
            Misaki "I agree with Alice, austere is more used for when the acidity is too high for the majority of people to ever even enjoy the wine."
            BBW "Exactly, this wine is bright- the acidity is not so high that nobody can enjoy this, it's just a little more niche."
            Misaki "Like the previous two wines, this one also reflects the culture of those who made it."
            Misaki "The wine is British and, in my experience, British people tend to be a hardy sort, even if it means drinking something generally unpleasant- but not overly so."
            BBW "I personally believe culture has a greater impact on a product than any amount of market research ever will."
    Misaki "While we wait for the final wine, could you two come with me for a moment? I wish to show you an art piece I recently acquired."
    BBW "Of course."
    Misaki "It's just through here."
    hide BBW with fade
    show BBW neutral with dissolve
    Misaki "And here it is, the newest addition to the collection."
    BBW "This is a fine piece, Keisuke what do you know about this painting?"
    if getSkill("Art") > 5 or getFlag("BBW045_art"):
        MC "Well the use of many short, quick brushstrokes is a tell-tale sign of Van Gogh- this is definitely one of his."
        MC "Though I haven't seen this particular one before."
        Misaki "That is absolutely correct. You clearly know your art."
        Misaki "I'm very impressed, I know the current Seichou curriculum doesn't teach such things so you have clearly put the work in yourself."
        MC "Thank you."
    else:
        MC "It's not a painting I recognise, but I like it."
        MC "It looks European."
    Misaki "This is a 'Sower with Setting Sun' by Van Gogh. I'm very proud of owning this original piece."
    Misaki "It's the most famous original at this gallery, the more well known ones are all imitations."
    BBW "It is a fine piece. It must have been expensive."
    Misaki "It was. However, the way I see it is that my children and their children will be able to enjoy this art, and so on."
    Misaki "You know, his full name was actually Vincent Willem van Gogh. In the dutch language, van means 'from' or 'of'."
    Misaki "This means everybody remembers him as being named From Gogh."
    Misaki "I find that rather amusing."
    "The waiter then appeared with the final wine sample for the day."
    Waiter "The final selection, Madam. 'Vilamoura Special', from the resort you invested in."
    Misaki "Thank you Yamada-san, when everyone leaves you may take the rest of the day off, we won't open this evening."
    Waiter "Thank you miss."
    "For the final time this evening we tasted the selected wine."
    MCT "This one is actually quite good. It has a fine amount of fruit and a fine acidity compared to the others."
    MCT "Though, it does get around the mouth a lot- the feeling is unpleasant even if the taste itself is good."
    "Misaki finished her tasting and Alice and I replicated the action."
    Misaki "Now that wine actually had a perfect taste, something I expect from a vacation resort."
    Misaki "However the wine was very fat. It lingers even now in the corners of my mouth."
    BBW "I agree the taste was great, but I don't believe the wine being fat makes it unpleasant."
    Misaki "Alice, a fat wine is a wine that finds its way into all parts of your mouth, a good wine stays on the tongue where it belongs."
    BBW "Why does a fat wine have to inherently be bad?"
    Misaki "That's just how the terminology is."
    BBW "Keisuke, what do you think?"
    menu:
        "Defend Alice.":
            $setFlag("BBW045_c5_1")
            MC "I agree with Alice. If a wine is good, why not let it fill your whole mouth?"
            Misaki "Because that isn't how wine as a beverage is supposed to be."
            Misaki "You two are very mature for your age but I have been doing this a long time so trust me when I say wines are meant to stay neatly on your tongue."
            Misaki "Anyway, that is the end of this morning's event. I truly appreciate your father's donations, Alice, and your construction proposal was great."
        "Defend Misaki.":
            MC "I agree with Misaki on this matter, Alice."
            MC "Wine should stay on the tongue, not fill the mouth. That is simply not how wine is intended to be."
            Misaki "He's right, Alice. Trust me, I have been doing this a long enough time to know how wine should be."
            Misaki "Anyway, that is the end of this morning's event. I truly appreciate your father's donations, Alice, and your construction proposal was great."
    Misaki "I do hope you two enjoyed your time here."
    "Alice and I headed towards the exit."
    scene Town with fade
    show BBW neutral with dissolve
    BBW "Keisuke..."
    MC "Yes?"
    BBW "What I said at the end about fat wines not inherently being bad was a test."
    MC "Oh?"
    if getFlag("BBW045_c5_1"):
        show BBW angry
        BBW "You failed."
        $setAffection("BBW", -1)
        BBW "Fat is used as a negative term in wine tasting, your views on the word in terms of body types is irrelevant."
        BBW "Do you see me as anything more than that word, {i}fat?{/i}"
        BBW "I am a person, Keisuke, not a body type."
        MC "I'm sorry Alice."
        BBW "Of course you are."
        BBW "I'm going back to my dorm. When I see you in class tomorrow I will have forgotten about this, I hope you do the same- and improve in the future."
        hide BBW with dissolve
        MCT "That was bad."
        if getFlag("BBW045_c3_1"):
            MCT "What was it Daichi said this morning?"
            MCT "Wanting something more will deny you of it? Or that we can be destroyed by our own ambition?"
            MCT "I guess he was right after all."
        jump daymenu
    else:
        show BBW happy
        BBW "You passed."
        $setAffection("BBW", 1)
        BBW "You remembered that fat is a wholly negative term in wine tasting."
        BBW "You didn't let your {i}ahem{/i}... other tastes get in the way."
        BBW "I never doubted you for a second."
        MC "Thanks Alice."
        if getFlag("BBW045_art"):
            MC "By the way, how did you know we would be shown that Van Gogh painting?"
            BBW "She boasted about it on the gallery social media recently, so I thought she would try to boast about it at the event too."
        BBW "You know, we may be in the wrong attire but we still have a lovely Sunday ahead of us."
        BBW "The weather is perfect. I'd quite like to go to the park."
        BBW "Come on, this'll be fun."
        jump daymenu

label BBW046:
    $setProgress("BBW", "BBW047")
    scene School Front with fade
    play music Peaceful
    "It was a bright, sunny day outside. The skies were clear, and a faint breeze went against our backs. The weather app said these conditions were expected for the next few days."
    "I looked the street up and down, waiting for Alice's ride to arrive. The giddy feeling in my hands was a mix of nervousness and excitement."
    show BBW summer-ext-haughty with dissolve
    BBW "You do know that watching for the vehicle will not cause the driver to speed up, right?"
    show BBW summer-ext-happy
    "Alice's head remained facing forward, her smirk appeared as she glanced at me from the corner of her eye."
    MC "Heh, yeah. I'm just a little nervous is all, this is probably going to be the most luxurious vacation I've ever been on."
    show BBW summer-ext-neutral
    BBW "Probably? I can assure you that you will be treated as a VIP, that is to say, like a five star guest."
    MC "Honestly, I'd be fine with a regular hotel chain. It's normally an extra if the places I've stayed at had a pool."
    MC "And it's a bonus if the pool water is actually clean."
    show BBW summer-ext-haughty
    "She rolled her eyes sarcastically, but I could tell she got some amusement out of my joke."
    BBW "Well, you needn't worry about filthy swimming waters at the house. The shores have the most beautiful crystal clear waters, and the beaches are always kept free of litter."
    MC "Wow... I can't wait to see it in person."
    show BBW summer-ext-neutral-2
    BBW "Before our driver arrives here, you should probably double check your bag to make sure you have everything."
    MC "Ah, what? You really think I'd forget something?"
    BBW "It's always better to be safe than sorry. You wouldn't want to get there and find out you left your hair comb here or something."
    MC "Don't worry about it, I have it right here in the side pocket of my bag."
    "With a confident grin, I unzipped the compartment of my travel bag where I kept my hair products."
    "My confidence quickly drained as I reached into the bag, fondling around to find my hairbrush, but it didn't seem to be there."
    MC "Hang on, h-hang on, I know it's in here somewhere..."
    show BBW summer-ext-neutral
    BBW "You left it beside your bag, but forgot to put it in when you picked it up."
    MC "Right, r-"
    "I paused, realizing what Alice had just said. My hands stopped frantically shuffling in the bag as I looked up."
    show BBW summer-ext-happy
    "With a genuine smile, Alice put out her hand. In her palm was my hairbrush I was so worried about."
    BBW "I would think by now that you would be more careful with such important items..."
    MC "Heh heh... thanks for getting that for me."
    show BBW summer-ext-haughty
    BBW "I don't imagine spending time in the hot sun with wild hair would be very fun."
    MC "Oh yeah, it really isn't. I actually have a sweatband that I wear secretly on some days when it's sweltering outside."
    "I finished checking my bag and zipped it back up, I was ready for some summer beach fun."
    "It wasn't too long after words that I saw it approaching on the horizon, an absolute behemoth of an RV started making its way down the road."
    "The vehicle could be more charitably referred to as a house on wheels. Quite easily out-scaling any car that tried to pass it; in fact it was so big, I questioned if it could be considered street legal."
    show BBW summer-ext-worried
    BBW "Oh my... I truly did not expect father to go all out with this."
    MC "You mean to tell me that you don't travel in luxury RV's for long distance vacations?"
    BBW "No, that's not it."
    BBW "The shocking part is the... well the size of it. I have traveled in many exquisite transits before, but none of this size."
    menu:
        "You sound uncomfortable, is something wrong?":
            jump BBW046_c1_1
        "Hey, c'mon. Less time worrying and more time relaxing!":
            jump BBW046_c1_2

label BBW046_c1_1:
    show BBW summer-ext-surprised
    BBW "What? No, nothing in particular is wrong."
    MC "Are you sure?  I may not be very observant, but I can tell when something has put you off."
    show BBW summer-ext-worried
    BBW "...{i}sigh{/i}... you are correct, Keisuke. There is something bothering me about this."
    "Alice turned away from the road to face me, her crystal blue eyes locked onto mine."
    show BBW summer-ext-neutral
    BBW "My father knows that my body has... grown, whilst being here. But whenever I would make contact with him, the details of my current size were always kept vague."
    show BBW summer-ext-neutral-2
    BBW "Not because I happen to be ashamed of it, no. But because he is a very caring person, and it just wasn't in my heart to reveal information that might worry him."
    MC "That's very kind of you, and I'm sure he appreciates it. But how does that tie into the RV?"
    show BBW summer-ext-happy
    BBW "Keisuke, you were right, you truly are not all that observant."
    "She gave me a sincere grin as she pointed back to the rapidly approaching vehicle."
    BBW "Look at the absurd size of that transit, even for me, that's far more than enough room. In fact, one could probably fit several of me in there quite comfortably."
    MC "That's a good thing isn't it? All that extra space, plenty of room to stretch your legs during the trip."
    show BBW summer-ext-neutral-2
    BBW "Oh no, I am far from ungrateful, believe me."
    BBW "He's always cared for my comfort, but something about this gives me concerns he's overthinking things."
    MC "I still think it's best not to look a gift horse in the mouth. This is supposed to be a fun time out, yeah?"
    jump BBW046_c1_2

label BBW046_c1_2:
    show BBW summer-ext-neutral
    BBW "Yes, you are correct. Currently I need to take my mind off things, and enjoy my vacation with pleasant company."
    MC "Speaking of pleasant company, where's Aida?"
    BBW "Don't worry, I arranged a separate transit for her. I didn't want her overstressing about us on the way there. Especially in her current state."
    MC "Yeah, you do have a point."
    BBW "She'll get there before we do, the servants shall help her accommodate."
    MC "Servants... you were serious about that five star vacation service, huh?"
    show BBW summer-ext-haughty
    BBW "I, of course, went through the effort of hand picking the staff that will be with us during our stay."
    MC "Wow, even when going on vacation you still put in extra effort."
    BBW "Naturally. No self-respecting entrepreneur ever phones in their work, even when they are planning to relax."
    "Both caught up in our small talk, we hardly noticed the oversized transit pulling up beside us. My initial thoughts upon seeing it, would be how loud it would be."
    show cg BBW046 with dissolve
    "The only kind of automobiles I've seen of this size were normally service vehicles. Billowing out smoke, and making enough noise to wake a neighborhood."
    "But despite the intimidating size, the RV was shockingly quiet. If one wasn't bearing witness to its girth, they would assume it was nothing more than a golf cart."
    "I stood in awe as the double doors on its side jolted open with a mechanical whir. A large set of steps, covered with dark red velvet cascaded like a ramp. And out stepped a very formally dressed chauffeur, sporting the Nikumaru company logo."
    Chauffeur "Miss Nikumaru and her plus-one, correct?"
    "Alice shifted from her normal relaxed demeanor, to the poise she normally took when best presenting herself."
    BBW "You are correct, sir. And if you may, please refer to my 'plus-one' by his name. Hotsure Keisuke."
    "The driver gave me a powerful look, almost sizing me up. It almost looked like he was judging me, seeing if Alice had picked the best person to accompany her."
    Chauffeur "Apologies, Mr. Hotsure. I was unaware that Miss Nikumaru would be bringing along a... male friend with her on this outing."
    BBW "Is there a problem with that?"
    Chauffeur "Of course not, madam. Please, your ride awaits."
    "The chauffeur bowed his head and extended his arm, directing us inside the RV."
    BBW "After you."
    "Alice kept her chin up, calmly gesturing for me to enter first."
    MC "Why thank you, I see that the high-class guest treatment is starting early."
    BBW "Keisuke, please get in the RV before I change my mind about bringing you."
    "I gave her a cheeky grin before climbing up the stairs. It wasn't until I turned around that my mind could truly grasp how spectacular this vehicle was."
    scene RV Interior with fade
    "The entire space was somehow even bigger than it looked on the outside. Not only was there enough room to fit an entire party, but it had an excess of extra amenities as well."
    "There was more room in here than most standard size apartments!"
    "In one corner, there was a full bathroom, with a shower and washer-dryer combo. And in the other, a full kitchen area."
    "It had an electric stove, fully stocked cabinets, and a fridge that was so massive it could probably crush anyone it fell on."
    "All of this living space was colored in a very pleasant dark shade of blue, with black and white accents scattered around. The floor itself was void black and so thick, that I could look down and it seemed as if my feet had melted into the lush comfort of the carpet."
    "I stood there in awe, my eyes were flicking around the room like a pair of flies. Everywhere I looked, there seemed to be more and more unnecessary applications to the passenger area."
    "Coherent thought had left my mind for a second. It wasn't until I felt the entire RV shake, that my focus snapped back to reality."
    "Turning around, I saw Alice calmly making her way up the steps. The look on her face wasn't nearly the same level of shock as mine,"
    show BBW summer-int-surprised
    extend " but from the slight jolt in her expression, I don't think she was really expecting this level of care as well."
    BBW "Goodness, Father has always been one for the occasional splurge. But even for him this is far too much."
    MCT "He considers this a 'splurge?' This thing probably cost more than most low-middle income houses..."
    show BBW summer-int-worried
    BBW "Do you have a problem with the arrangements, Keisuke?"
    menu:
        "No! Not at all.":
            jump BBW046_c2_1
        "I mean, this does seem kind of extra.":
            jump BBW046_c2_2

label BBW046_c2_1:
    show BBW summer-int-neutral
    BBW "Oh, well that's good to hear. You looked quite pale for a second, I was worried we had overwhelmed you."
    MC "Who, me? Nah, I'm just fine. This already looks like it's shaping up to be a great vacation."
    BBW "Indeed! Now, what would you like to drink?"
    stop music
    jump BBW046_arrival

label BBW046_c2_2:
    $setAffection("BBW", 1)
    show BBW summer-int-neutral-2
    BBW "Yes, I was actually a tad bit worried how you would handle all this."
    MC "I'm not complaining, obviously. It's just that- this is a lot to take in."
    show BBW summer-int-worried
    BBW "It may have been silly, but I had hoped that father wouldn't go all out for me again. Not just for my sake, but for yours as well."
    MC "For your sake? Don't you want to live it up on a vacation?"
    show BBW summer-int-neutral
    BBW "That much goes without saying, Keisuke. But moderation is key, even when it comes to relaxing."
    BBW "If you live in moderation, the little things are just as rewarding as the bigger ones. But if you constantly live in excess, you'll burn yourself out fast."
    MC "I dunno, I've never seemed to have a problem with moderating my relaxing."
    show BBW summer-int-haughty
    BBW "That's because you do it far too much. Now come sit down with me, I want to explain the best times to be on the beach."
    stop music
    jump BBW046_arrival

label BBW046_arrival:
    scene black with fade
    pause 2
    scene RV Interior with fade
    play music BBW
    "Several hours in the RV felt like nothing. Normally during road trips, I would find myself getting bored easily, always looking for something to keep myself entertained."
    "But when you're traveling in a mobile hotel suite, with an excellent conversationalist, time really does fly."
    Chauffeur "Miss Nikumaru, and Mr. Hotsure. We have arrived at our destination."
    "The chauffeur's voice came on over the speakers, interrupting the pleasant classical music Alice had put on."
    Chauffeur "And you needn't worry about your luggage, Mr. Hotsure. Someone will be along shortly to help you bring it to your room."
    MC "Is that really going to be necessary? I'm ok with just carrying my stuff in personally."
    Chauffeur "Understood. Please enjoy your trip."
    show BBW summer-int-happy with dissolve
    BBW "Excellent, the journey here seems to take longer and longer each year. Or perhaps that is just the excitement I am feeling?"
    MC "Hey, if we unpack fast, there may still be some sunlight left to hit the beach!"
    BBW "Not a moment wasted, I quite enjoy that enthusiasm. But for now, let us save the beach for sunrise. I can assure you that the sunrise on the beach is the greatest first experience here."
    MC "Awww, well that's fair I suppose-"
    play sound Knock
    "We were interrupted by the sudden rapping on the automobile's door. Someone was waiting for us outside."
    UNKNOWN "Lee! What are you doing?!"
    "The faint sound of a woman whispering could be heard on the other side of the door."
    UNKNOWN "We've been waitin' out here for a while, I jus' wanna make sure sure they're ok!"
    "Another voice emanated, this one was more masculine as well as younger."
    UNKNOWN "Please, Si-Woo. You simply must exercise more patience. Young Miss Alice shall depart from her ride when she is ready."
    "The third, and seemingly final voice spoke up. This one was masculine as well, but significantly older than the other two accompanying it."
    BBW "We best not keep them in suspense."
    MC "They certainly do seem eager. Are your servants normally this energetic?"
    BBW "I should hope so! We don't pay them well above the average servant wages for sub-par service."
    show BBW summer-int-haughty
    BBW "They are also provided with an array of benefits, as well as a very flexible contract. If you want the best, you have to treat them like the best."
    MC "Wow, if architecture doesn't really pan out, make sure to remind me about working for the Nikumaru company."
    BBW "Hmm... tempting offer, but why pay a servant who's already working for free?"
    show BBW summer-int-happy
    "Alice gave me a smug grin as she opened the RV door, letting the vivid orange coloring of the sunset wash in."
    scene Summer House Front with fade
    MC "Hey, hang on. There is no way you just said that-"
    UNKNOWN "Young Lady Alice! What a pleasure it is to see you again after all this time."
    BBW "And I could say the same to you, Takada. I am so glad that you had the time to come out here."
    Takada "Please, even if I was booked to bursting, you know that I would drop everything to come serve you."
    "I followed Alice down the stairs onto the warm tarmac of the driveway. My eyes instantly noticed the three well dressed butlers standing in front of us. They all wore the Nikumaru company logo."
    UNKNOWN "Huh, wasn't expectin' this pal of hers to be a guy friend... What's your name, sir?"
    "The man talking to Alice was the older voice I had heard before. But the one questioning me now was clearly the younger, male voice."
    "The last voice then must have belonged to the young lady standing next to the questioning man. She looked about three seconds away from smacking her brash co-worker over the head."
    MC "Um... I..."
    show BBW summer-ext-neutral with dissolve
    BBW "This is my good friend, Hotsure Keisuke. He shall be staying with us, along with Aida Kodama. Has she arrived safely?"
    Takada "Young Miss Aida arrived here mere moments before you did. She has been shown her room, and is unpacking her bags now."
    UNKNOWN "Keisuke? Cool, it's gotta nice ring to it!"
    play sound Thud
    "{i}Smack{/i}"
    UNKNOWN "Being blunt I can forgive a new recruit, but forgetting basic protocol is unacceptable!"
    UNKNOWN "Aigu Heol! Right, introduce myself first!"
    Lee "Pleased to meet cha'. I'm Si-Woo Lee, but you can just stick to calling me Lee! And I'll be serving you for this vacation."
    UNKNOWN "{i}Sigh{/i} At least you are steadily improving, but you're still far from the standard of quality we expect."
    UNKNOWN "You'll have to forgive him, he's still quite new to this profession. But Miss Alice decided that he would be an invaluable asset for the rest of us."
    BBW "This will be a learning opportunity for him. I picked Lee because he came with high marks from my father, but lacked many of the traits that are present in our other servants."
    Lee "Mr. Nikumaru said that I had serious potential! ...I just gotta learn when to act professional is all."
    Takada "Young Miss Alice, I do believe it would be best to do with the formalities after you unpack."
    show BBW summer-ext-neutral-2
    BBW "Quite right, I better check on Aida to make sure she is adjusting well to all this."
    hide BBW with dissolve
    "With that, I adjusted my bag and set off towards the house."
    scene Summer Living Room with fade
    "Once again, I was astounded by the sheer amount of space inside the beach house. Just like the RV, it was big on the outside, yet even bigger on the inside."
    "The second the door was opened, I was greeted to a living area spanning the entire homestead. It was difficult to tell where some rooms started and ended."
    "Everything was of course, fanciful and glimmering to the nines. But by this point, I would've been more surprised if the place turned out to be cozy and modest."
    "What caught my attention the most was the open wall by the far corner of the room. It led out onto a lovely wooden patio, but more importantly, it gave you an astonishing glimpse at the beach no matter where in the room you were."
    Takada "I see that the accommodations are to your liking, Young Mr. Hotsure."
    MC "Huh? Yeah, you could say that. I'm just shocked by the scale of everything, I've seen a fair share of larger amenities at the school sure... But this is really something else."
    Takada "Mister Nikumaru was very clear with his plans to refurbish the homestead whilst young Miss Alice was away."
    Takada "But enough about that for now, please, let me show you to your room."
    scene Summer Guest Bedroom with fade
    "The guest bedroom was just as lavish as I had expected by this point. Queen sized bed, velvet sheets, and a personal walk-in bathroom."
    Takada "When you are finished setting up in here, feel free to introduce yourself properly to the other two servants. They may not have as many years of experience as me, but I can assure you with full confidence, they are quite talented."
    MC "Will do, thanks for showing me around."
    Takada "It was my pleasure, Mr. Hotsure."
    "With that, Takada gracefully bowed his head and closed the door. Leaving me with my open bag of clothes, and a choice."
    "What do I wear for tonight? I want to make a good first impression..."
    menu:
        "Semi-Formal wear":
            jump BBW046_c1_3
        "Vacation shirt and shorts":
            jump BBW046_c2_3
        "Actually, I should just head to bed early":
            jump BBW046_c3_3

label BBW046_c1_3:
    MC "Just because I'm on vacation doesn't mean I should make myself out to be some boorish oaf."
    "I got changed out of my casual clothing, and donned a fresh pink polo shirt, with brown slacks."
    jump BBW046_afterchoice_3

label BBW046_c2_3:
    MC "Yeah, let's get this vacation started early!"
    "Ditching my current clothing, I hastily threw on a vivid, floral patterned, button-up shirt. To compliment this tropical garment, on my lower half I wore a pair of white khakis."
    "The idea of wearing my sunglasses to complete the look crossed my mind, but I stopped just short of putting them on."
    jump BBW046_afterchoice_3

label BBW046_c3_3:
    MC "It's been a long trip here, the smart thing to do would be to fall asleep early. That way I can be there for Alice in the morning, to watch the sunrise..."
    "With a content smile, and a head full of excitement, I laid myself down onto the bed and drifted off to sleep."
    jump daymenu

label BBW046_afterchoice_3:
    "I opened my bedroom door, and made my way to the living area. Hoping to meet up with Alice and Aida before the day was done."
    scene Summer Living Room with fade
    "Turning a corner, I came face to face with the female staff member I had never gotten the name of."
    UNKNOWN "Oh, Mr. Hotsure, we had assumed that you went to bed like Miss Alice and her friend."
    MC "Alice and Aida already fell asleep?"
    UNKNOWN "Both of the young ladies made it very clear that they wished to be refreshed for tomorrow. As so that they may enjoy the activities to the fullest."
    MC "Huh, guess I should follow suit then."
    UNKNOWN "That would be a wise course of action, Mr. Hotsure. I hope you have a pleasant night."
    "The young servant bowed before continuing past me."
    menu:
        "Hey, wait... I never got your name.":
            jump BBW046_afterchoice_4
        "I should head back to bed.":
            jump daymenu

label BBW046_afterchoice_4:
    UNKNOWN "Ah!"
    "She turned around in shock, her face was flush with embarrassment."
    UNKNOWN "Please forgive me, Mr. Hotsure. It completely slipped my mind after you arrived."
    Shino "You can call me Murakami Shino. Or just Shino if you wish."
    Lee "You really went and called me out, when ya didn't even do properly yourself?"
    "The youngest servant, Lee, slowly approached Shino. A goofy smile plastered across his face."
    Shino "L-Lee! What are you doing here? You should be in the kitchen."
    Lee "I was headin' to the hwajangsil- I mean wash closet... What, is that not allowed?"
    Shino "No, that's fine, just... don't surprise me like that!"
    "Lee changed focus to me."
    Lee "Wait, I see. You were gonna help our guest get to know us better, yeah?"
    Shino "What? No no, I was just-"
    Lee "Don't worry about it! If he's gonna be staying here for a bit, the least we could do is get to know him better."
    MC "Sure, uh..."
    Shino "That's quite alright Mr. Hotsure. Please, I would be negligent in my duties if I were to delay you from getting much needed rest. Miss Nikumaru would be most disappointed if you were unable to rise the next morning in a timely manner."
    MC "That is true, I guess I should be off to bed. Nice to meet you all."
    jump daymenu

label BBW047:
    $setProgress("BBW", "BBW048")
    scene Summer Guest Bedroom with fade
    play music Peaceful
    "Warm, soft, and safe..."
    "Those were the only words that could describe how comfortable I felt in this bed. My entire body felt like it could just sink right into the mattress."
    "Part of me wondered what time it was, maybe I had accidentally slept in? But the other part of me really didn't care, and wanted to stay in this spot for as long as possible."
    stop music
    Shino "Rise and Shine, Mr. Hotsure!"
    "The peaceful silence of the room was shattered by the sound of my door being flung open."
    play music BBW
    Shino "Miss Alice specified that if you weren't awake by this time, I should give you a wake up call."
    MCT "Wake up call? With that much noise it was more like a siren."
    Shino "Make yourself presentable, she is waiting for you on the balcony. Do not fret about breakfast, it will be waiting for you afterwards."
    "Shino practically lept to the side of my bed, and ripped my covers off with such force it was surprising she didn't take me off the bed with them."
    Shino "Please hurry, Mr. Hotsure. I would hate for Miss Alice's first day of vacation to start off on a bad note."
    "With a yawn, I managed to drag myself to the edge of the bed. My eyes slowly opened to look at the time."
    MC "5:50 AM?"
    Shino "The sunrise. Miss Alice has always made it tradition to watch the sunrise the first day she is here."
    MC "Right... shame the sun couldn't wait for me to comb my hair first."
    "Even though I couldn't see much past my own bangs, I could physically feel the dismissive looks that Shino was giving me."
    Shino "I am well aware of your unique condition, Mr. Hotsure. But that is no excuse to look like a lazy slob in the morning!"
    MC "Hey, I was just joking. Believe me, if I don't maintain my hair it becomes more of a problem for me than others."
    Shino "Good, now that that's settled, I have to check in on Lee. The last time I left him alone to cook, he broke a plate..."
    "With the same ferocity Shino had opened my door with, she bolted out of my room like it was on fire."
    MCT "Not exactly the most pleasant good morning, but I guess they really want everything to be perfect for Alice."
    "I managed to slog myself out of the comforting embrace that the linen sheets provided. My eyes barely opened as my feet automatically made me lumber to the bathroom."
    "By the time the haze in my mind had cleared, I was standing in the doorway of my room. Hair neatly combed, dressed in a pair of pajama pants and loose t-shirt."
    MCT "I hope Alice doesn't mind me being a bit tardy to the sunrise."
    scene Summer Balcony Exterior with fade
    "Not halfway down the hall, I turned to see Alice gracefully glancing over the balcony."
    show BBW summer-int-neutral with dissolve
    "The cascading light coming from the early morning sun did wonders. The way she calmly lent against the wall, her head turning to the sunrise, made Alice look like she was right out of a painting."
    "Bright, vivid yellows were reflecting off the golden accents in her clothes. Giving her an almost ethereal aura that beckoned me closer."
    "The gentle orange glow, ever so faint, ended up perfectly complimenting her fair skin. Catching her golden hair as well as her cherubic face, making her features look soft and friendly."
    "Finally the red hints flawlessly captured her contours, outlining her form with vivid colors. Broadcasting an alluring appeal to anyone who was lucky enough to see her in this light."
    "I never truly considered myself to be a man with absurdly high luck. But upon witnessing this spectacle, my opinions might have just changed."
    menu:
        "Greet her.":
            jump BBW047_c1_1
        "Give her a soft hug.":
            jump BBW047_c1_2

label BBW047_c1_1:
    MC "Lovely morning, isn't it?"
    show BBW summer-int-surprised
    "Alice slightly jumped at the sound of my voice. Her head turned toward me with a warm smile"
    show BBW summer-int-neutral
    BBW "Why, yes it is. I am glad that you managed to get out of bed for this."
    BBW "In all honesty, I truly only expected you to be awake in time for the sunset."
    MC "And miss seeing you in this early morning glow? Not a chance."
    "I made my way to Alice's side, leaning on the railing as I took in the stunning sights that cascaded before me."
    MC "In all honesty, it was Shino who made sure that I was here on time. She was deadly serious about me being here."
    BBW "Hmph, that does sound like Shino alright..."
    jump BBW047_c1_after

label BBW047_c1_2:
    $setAffection("BBW", 1)
    "I carefully walked up behind Alice, making sure that my footsteps went unheard."
    "Waiting till the last second, I raised my arms and gently set them over her shoulders. Bringing her into a gentle embrace."
    show BBW summer-int-happy
    BBW "I was hoping that you would do that."
    "Alice tilted her head to look at me, an almost gleeful smile was faint on her lips."
    MC "You heard me?"
    BBW "I would need to be deaf to not hear the chaotic swaying and bouncing of your hair."
    MC "Ah, right. I guess I've just kind of gotten used to the noise by now."
    BBW "A part of me wonders if you can even see out of that mane. Now I'm questioning if you can hear out of it as well."
    "She gave a faint chuckle at the thought."
    MC "Ears and eyes aren't a necessity, I already know that I'm with the most beautiful woman in the world. What else is there to experience?"
    BBW "Hmph, good answer."
    "We spent the next couple of minutes just standing there, enjoying the extravagant lights of the sunrise."
    BBW "My father used to bring me out here when I was young, we made it a tradition to watch the sunrise here together."
    jump BBW047_c1_after

label BBW047_c1_after:
    BBW "That reminds me actually, have you had a chance to get familiar with the other staff members yet?"
    MC "No, actually. I haven't had a chance to meet anyone besides Shino."
    MC "They all seem wonderful, I'm looking forward to getting to know them better."
    show BBW summer-int-haughty
    BBW "That will have to wait unfortunately, I have other plans for you today."
    MC "Hold on, let me guess- you want to spend today at the beach?"
    BBW "Well, just the afternoon. After that, we shall see where the day takes us."
    MC "I can't wait."
    scene Summer Beach with fade
    stop music
    play music Peaceful
    "After finally getting a chance to eat breakfast, I made haste to get changed into my swim trunks."
    "It was midday, the sky's were mostly cloudy with strong rays of sunshine going through the gaps. And one couldn't ask for better weather on the beach."
    "I looked around to find Alice, but the only other person at the beach was Aida."
    show PRG swimsuit-neutral with dissolve
    "Who was reclined in her beach chair, under a large umbrella, reading a book."
    MC "Lovely weather today, yeah?"
    "Aida crooked her head to look at me."
    PRG "It really is! I'm so glad that we get the chance to unwind over the summer like this."
    MC "Yeah, you certainly seem comfortable."
    PRG "I-I am. And, I have a spot set up for you and Alice, too."
    MC "Really? Did Alice ask you to do that?"
    PRG "No. Alice actually told me to focus less on her and more on myself. Especially considering..."
    "Aida glanced down at her enlarged abdomen, which appeared to be covered by a healthy amount of sunblock."
    PRG "...But I couldn't relax while knowing that I would be distracting you two from each other!"
    MC "That's why you set up your own spot further down the beach?"
    PRG "Yep! So now you two can get even closer together."
    MC "Wow."
    menu:
        "Thank her":
            jump BBW047_c2_1
        "Check out the spot she set up.":
            jump BBW047_c2_2

label BBW047_c2_1:
    $setAffection("PRG", 1)
    MC "Thank you so much, Aida. I really don't know how you manage to still be so helpful, even during vacation."
    show PRG swimsuit-happy
    "Aida blushed and gave me a gleeful smile."
    PRG "Oh, don't mention it, Hotsure-san. Really, it was a pleasure."
    PRG "Now, stop worrying about me, and go see Alice!"
    MC "Right!"
    jump BBW047_c2_2

label BBW047_c2_2:
    scene Summer Beach Closed with fade
    "I made my way over to the area that Aida had set up. It was a rather elegant beach tent, almost entirely white with the exception of gold accents around the edges."
    MC "Is there a door knocker on this, or should I just shout 'Ding-Dong?'"
    "Alice's voice came through the cloth cover draping over the entrance."
    BBW "You needn't worry about walking in on me unprepared, I have already changed into my swimming outfit."
    MC "Well that's unlucky for me then, isn't it?"
    BBW "This little ensemble was custom made per my instructions, I must make sure that everything is up to par."
    MC "I'm sure you look fantastic, Alice."
    BBW "Oh trust me, there is no doubt about that. The thing is..."
    "Her voice trailed off, I could hear her pacing around in the tent."
    BBW "They got my requested measurements correct, I asked Aida for a double check. But yet, it still feels ever so slightly too tight."
    MC "It's probably just because the suit is new, you need to break it in."
    BBW "While that is kind of you to say, Keisuke, but we both know that is not the case."
    BBW "..."
    BBW "...I'm going to come out now, but you had better promise to not gawk like a fool."
    MC "I'll try my hardest to not notice how stunning you look."
    "Alice lightly chuckled."
    BBW "Flatterer."
    MC "How can it be flattery if it's just the truth?"
    show BBW swimsuit-neutral with dissolve
    "The privacy cloth door to the tent was lifted, and Alice stepped out into the sunlight. My tongue seemed to stop working as my eyes bared witness to the majesty in front of me."
    "Two luscious pillows of bountiful beauty came forward. Each of them jostling to and fro wildly, as if they each had minds of their own. But both comfortably contained in the skin tight bikini that only accentuated their size."
    "Despite the suit being made of high quality latex, it still seemed to have trouble keeping Alice's chest in check. They seemed to actively want to escape from their damning prison. Part of me wondered if they would eventually make their great escape."
    "The sheer heft of these twin pillows was being supported by a belly that had been packed right into Alice's suit."
    "The simple yet striking black was complemented by the subtle touches of gold; Giving Alice a rather elegant aura."
    "Reaching out ever so slightly past her breasts was a belly that made sure it was the center of attention at all times. The frills descending down her magnificent gut, as if it were a waterfall."
    "Her stomach had pushed both the latex and her breasts so far up that the straps meant to support her monumental bosoms were rendered pointless. The lithe straps did little more than rest on her shoulders, occasionally being enveloped by the fat of her upper chest."
    "Even with the custom made suit, it still couldn't cover the entire soft beachball of an abdomen. At the very bottom of the bikini's frills, the smallest sliver of flawless skin came peeking out."
    "The crescent shape was all that I could see of Alice's uncovered belly. But with each breath that she took, the frills would rise more and more. Slowly, ever so carefully, the loose cover continued to climb up. Teasing me to no end, but also drawing my attention ever closer."
    "Due to the sheer size of Alice's gut, I was having a hard time figuring out where her belly ended and her waist started. It blocked out the entire view of her thighs from the front."
    "However, her love handles provided me with perfect markers. Directing my eyes further downward to see the layers of upper thigh fat layering over each other. This amazing spectacle of adipose made it so the sides of her legs extended from behind her belly."
    "Following along the trail of excess fat billowing from her legs, I finally landed on her backside."
    "Although her posture was directed to face me, I could still see the edges of her plump posterior. The magnitude of its size was taunting me, it was begging me, to see it in all its glory."
    "Only when she turned could I get a hint of its splendor, a perfectly porcine heart shape, with the ends of the heart melting into significantly chubby thighs. The sight alone was enough to drive me crazy."
    "The thought of simply touching it though, was beyond my comprehension. The idea of what it would feel like to cascade my hands down her form was heavenly. The supple layers of flab pushing through my fingers..."
    "The gentle embrace of her voluptuous form was all I could think about."
    show BBW swimsuit-haughty
    BBW "Is this what you call 'trying your hardest?'"
    "My attention was viciously snapped back to reality. Alice gave me a dismissive look, but I could see just a smidge of pride in her eyes."
    MC "{i}Cough{/i} hm, yep... sorry."
    show BBW swimsuit-neutral-2
    BBW "Calm yourself will you, Keisuke? It is not as if you have never seen me in a swimsuit before."
    MC "Yeah, but... last time I saw you in a swimsuit, you weren't this-"
    menu:
        "Big":
            jump BBW047_c3_1
        "Beautiful":
            jump BBW047_c3_2
        "Exposed":
            jump BBW047_c3_3

label BBW047_c3_1:
    show BBW swimsuit-worried
    "Alice's saunter slowed down, her prideful posture had weakened a bit."
    BBW "...Yes, you are correct Keisuke."
    MC "N-No! I didn't mean anything bad by it."
    BBW "I know you had no ill intent, but yet those kinds of expressions still stress me."
    MC "I'm sorry Alice, it's just... seeing you in this bikini must have fried my brain or something."
    show BBW swimsuit-neutral
    "Her smile started to faintly return to her face."
    BBW "At least I know that you still find me irresistible."
    MC "Was there ever any doubt?"
    show BBW swimsuit-neutral-2
    BBW "Your eyes nearly left your head when you saw me come out! Any doubts I had were crushed on the spot."
    jump BBW047_c3_after

label BBW047_c3_2:
    show BBW swimsuit-happy
    BBW "Are you implying that I was not beautiful before?"
    "Alice gazed at me with a cocky smirk."
    MC "No, just more so now that so much of you is on display."
    BBW "An expected answer, but true nevertheless."
    jump BBW047_c3_after

label BBW047_c3_3:
    show BBW swimsuit-doubt
    BBW "There is next to nobody else out here, my choice in attire is perfectly fine."
    MC "What about Aida?"
    BBW "Who do you think helped me pick this design? Besides, it's nothing she hasn't seen before."
    jump BBW047_c3_after

label BBW047_c3_after:
    show BBW swimsuit-neutral
    MC "Are you planning to swim first, or do you want to go sunbathing?"
    BBW "I had considered taking a leisurely swim, but the water will be less cold at midday. So I shall rest on the beach for now, and listen to the calming sound of the waves."
    MC "That's a good point actually, I probably should have thought about that."
    BBW "Did you really plan on submerging yourself in the frigid early morning waters?"
    MC "It's definitely a good way to start off a vacation, yeah?"
    show BBW swimsuit-happy
    "Alice gave me a lighthearted giggle."
    BBW "You never cease to humor me, Keisuke."
    MC "What am I? Your date, or your personal clown?"
    BBW "Hmmm..."
    MC "T-That was a rhetorical question."
    show BBW swimsuit-neutral
    BBW "Oh I know. But now my mind is trying to picture you in a full clown suit."
    MC "I could make it work, they'd call me Folli the clown."
    BBW "Folli?"
    MC "It's short for 'follicles,' on account of my hair."
    show BBW swimsuit-aroused
    "Her head turned away from me for a second, her hand going to cover her mouth."
    MC "Really? That joke got you?"
    show BBW swimsuit-neutral
    BBW "No, not at all! *ahem*...I am actually concerned that you came up with that answer so quickly."
    MC "I always figured that if going into architecture didn't pan out, the circus freak show would be guaranteed employment."
    show BBW swimsuit-happy
    "This time Alice didn't have time to cover her face as she let out a clear laugh."
    BBW "You really would fit right in with the rest of the clowns, Keisuke."
    MC "Naturally... Hey, is that your beach set up down by the shore?"
    scene Summer Beach with fade
    "I pointed to a cozy little set-up close to the waves. There was a rather large beach towel on the sand, and an extra large beach chair resting on it."
    show BBW swimsuit-neutral-2 with dissolve
    BBW "Aida helped me set it up, I swear, she is far too generous."
    MC "Yeah, this seems like the perfect spot to just unwind."
    BBW "And when I am this close to the ocean, I can keep an eye on you to make sure you stay safe."
    MC "Oh? Are you going to be the stunning lifeguard that saves me from a riptide?"
    BBW "I might be, but if you get yourself into trouble on purpose, one of the servants will be the person to give you CPR."
    MC "Here's hoping for a wild current then!"
    "Taking off in a mad dash, I sprinted towards the crashing water."
    "The rising tide continued to slow me down more and more until everything below my chest was submerged."
    "Alice wasn't kidding, the sea was downright frigid. It felt like the very bones in my legs were being frozen. Part of me wondered if I would catch some form of hypothermia."
    MC "Come on! The w-water is f-fine once you g-get used to it."
    show BBW swimsuit-haughty
    "Way back on the beach, I could see Alice reclining in her beach chair. Her voluptuous form shining like a lighthouse on the sand."
    BBW "I can see your teeth chattering from all the way over here, Keisuke. Are you sure that this was a wise move?"
    MC "Of course it is-"
    "A massive wave of chilled sea water hit me right in the back, shoving me face first into the cold abyss."
    "Emerging from the water with a gasp, I pushed my hair out of my eyes and looked back towards Alice."
    MC "S-See? Perfectly fine."
    show BBW swimsuit-doubt
    BBW "You are going to get yourself hurt out there, come back already!"
    MC "Ok ok, fine. But only because I forgot to pack a swim cap, and my hair is weighing me down."
    "Trudging along, I made my way back towards the shore."
    MC "Now I know what Homer felt like in the Odyssey."
    show BBW swimsuit-neutral
    BBW "Apologies... but what do you mean by that?"
    MC "Being beckoned shoreside by the call of a beautiful siren."
    show BBW swimsuit-happy
    "Alice tried her best not to look pleased by the compliment."
    BBW "Sit down and dry yourself off already. Your hair probably weighs more than you now with all that water weight."
    "The next half hour passed rather pleasantly. After draining my hair, Alice and I basked in the warm summer air while we made small talk."
    show BBW swimsuit-worried
    BBW "Hmmm..."
    "After a while, I heard Alice sigh out. Something was very clearly bothering her."
    BBW "Maybe if I... no, that wouldn't work."
    MC "Is something wrong?"
    if getAffection("BBW") < 17:
        show BBW swimsuit-neutral
        BBW "Of course not, I was just pondering what Aida is reading over there."
        MC "Oh, ok."
        "Alice still looked uncomfortable, but decided to stay outside for a little while longer."
        "Although after very little time had passed, she announced that she would rather head back inside."
        "It seemed like a rather odd thing for her to do, especially considering how excited she got for this. I wonder if I could have helped with whatever was bothering her..."
        jump daymenu
    else:
        show BBW swimsuit-surprised
        BBW "What? Oh no, it's nothing to worry about."
        MC "Really?"
        show BBW swimsuit-neutral-2
        BBW "Yes, it's nothing that important."
        menu:
            "Question further":
                jump BBW047_c4_1
            "Stop asking":
                jump BBW047_c4_2

label BBW047_c4_2:
    MC "If you say so."
    show BBW swimsuit-worried
    "Alice still looked uncomfortable, but decided to stay outside for a little while longer."
    "Although after very little time had passed, she announced that she would rather head back inside."
    "It seemed like a rather odd thing for her to do, especially considering how excited she got for this. I wonder if I could have helped with whatever was bothering her..."
    jump daymenu

label BBW047_c4_1:
    MC "Alice, I've known you for long enough to see when you're putting on a brave face. What's really bothering you?"
    show BBW swimsuit-worried
    "Shifting back and forth in her chair uncomfortably, Alice turned her head away from me and spoke into the wind."
    BBW "It really is nothing you need to concern yourself with-"
    MC "Tell. Me. What's. Wrong."
    "I knew that taking such a commanding tone with Alice was a risk. But she was clearly bothered by something, and I was determined to help."
    show BBW swimsuit-stern
    BBW "Damn it all... if you must know..."
    show BBW swimsuit-worried
    BBW "I- I don't know if I'll be able to properly cover myself."
    MC "I can get an umbrella if you want."
    show BBW swimsuit-neutral
    BBW "No no, I wish to tan myself properly. But if I'm unable to coat my body, the risks of sunburn will be far too high."
    MC "Oh, I see... Do you really think you're too big to do it yourself?"
    BBW "Keisuke, I know my own body better than anyone else. And I'm also aware of what areas I can and can't reach."
    MC "What about one of the butlers? I can go ask one of them to help-"
    show BBW swimsuit-surprised
    BBW "No!"
    show BBW swimsuit-sad
    BBW "I mean... please don't let them see me like this."
    MC "Huh?"
    BBW "I've known these people for so long, and they've known me since before I could even walk."
    BBW "Having to rely on one of them for such a basic task, would not only be humiliating for me, but for them as well."
    show BBW swimsuit-worried
    BBW "So please, Kei, I'm asking you to not tell them about this."
    MC "Well what are you gonna do now?"
    show BBW swimsuit-stern
    BBW "What I need-"
    "Her cheeks flushed bright red, as her arms folded over each other."
    BBW "Keisuke, I need to ask something personal from you."
    "Her voice was hushed, her crystal blue eyes were having trouble remaining focused on anything."
    BBW "Will you... Would you be so kind, as to help me apply my sun lotion?"
    "Even with the most grueling of efforts, Alice desperately tried to maintain her aura of composure. But her voice, her body language, her facial expressions. All of it was shouting that she was in a very unfamiliar situation."
    "Alice looked as if she wanted nothing more than to close her eyes, and hope that this was all a bad dream. But there was a hint of something else in her expression."
    "In a rather odd way, while her body language was very closed off, it didn't look like she was entirely uncomfortable. In fact, judging by her face, she was viciously curious about the situation and how I would respond."
    MC "Y-Yeah, no problem."
    show BBW swimsuit-neutral
    BBW "You sound hesitant, are you certain that this task isn't too much for you?"
    MC "Of course not! It's just- I wasn't expecting this."
    show BBW swimsuit-haughty
    BBW "Neither was I... but this is what must be done."
    BBW "Here, take it."
    "Alice handed over her bottle of sun lotion."
    show BBW swimsuit-stern
    BBW "And if I catch you lingering over any of my areas, I will call this whole thing off."
    if getFlag("BBW040_c2_3"):
        MC "You really expect me to take advantage of the situation like that?"
        BBW "As a matter of fact, that is a concern of mine."
        MC "But if I recall correctly, last time this happened, it wasn't so bad."
        show BBW swimsuit-happy
        "Reclining back in her seat, Alice gave me a slight smirk."
        BBW "Consider this a rare privilege, Keisuke. It would be a shame to waste an opportunity such as this."
        BBW "Much like savoring a well made steak- you don't wolf it down, no. You savor every bite, making the most out of the experience."
        MC "Well now you've made me hungry."
        show BBW swimsuit-neutral
        BBW "...I'm afraid I may be a bit peckish at the moment now that you mention that."
        show BBW swimsuit-haughty
        BBW "Regardless, what I am trying to convey, is that the choice is up to you. Do you want to savor this gift, or do you want to rush through it?"
        MC "If it's all the same to you, I'd want to enjoy this as if it was my last meal."
    BBW "Now, are you going to stand around and gawk? Or are you going to help me?"
    MC "Don't have to ask me twice."
    show cg BBW047 with dissolve
    "Alice gave me a reaffirming nod as I positioned myself beside her. Lowering down onto my knees, I could feel the smooth grain of the sand envelop my shins."
    "It took only a second to position myself comfortably, but the sheer size of my task had just dawned on me."
    "It was enormous even when standing eye level with Alice, but being this close to it gave her belly gave it a daunting aura."
    "With each breath, I could see it rising and falling like the tides on the beach. A veritable tsunami of soft fat, crashing over itself again and again."
    "My hands acted almost on their own, as my eyes were too busy gawking. Before I even knew what I was doing, the bottle of lotion had been opened."
    "Tilting it over Alice's behemoth belly, I let the lotion pour out on the upper most part of her stomach. The liquid spread and pooled all across her, dripping into whatever folds it could find."
    BBW "Ah... it's been sitting out in the sun, how is it still cold?"
    "I chuckled as the lotion was put away. Even with the rather excessive amount I applied, some part of me wondered if it would be enough."
    "Not wasting any more time, my eager hands got to work covering her body. Immediately the warm sensation began to coat my hands, as they sunk into her pillowy middle."
    BBW "Mmmmph!"
    MC "Sorry! I'm being too rough aren't I?"
    BBW "No, no. It's just cold is all, that's it."
    MC "Oh, ok. Do you want me to continue?"
    BBW "Y-Yes please."
    "Despite all of Alice's bravado from before, the moment I took her in my hand, she started to unwind. Right before my very eyes, the elegant beauty was starting to relax."
    "Continuing my task, my arms kept up the attack on her belly. Flowing too and fro, back and forth, all across her rotund middle."
    "At some point I started to feel like a baker, preparing dough. I would gently knead the dough, not too much that it was disturbed. But also applying enough force that it spread was spread out evenly."
    menu:
        "Push your luck.":
            jump BBW047_c5_1
        "Show some restraint.":
            jump BBW047_c5_after

label BBW047_c5_1:
    "Against my better judgement, the idea of holding Alice's belly proved too much for me to handle."
    "With all the subtlety one could muster, I stretched forward. Some part of me was curious if my hand could reach the other side of her belly from the other."
    "The answer to that was no, unsurprisingly. Despite my best efforts, I was only able to get most of my arm across her middle."
    "Alice's plush middle was forcing itself very harshly against my arms length. I could feel myself almost sinking into her ever so slowly. Her substantial rolls imbibing me deeper and deeper."
    "I watched in amazement as my arm slowly disappeared under an avalanche of belly. But my curiosity wasn't yet sated..."
    "Using what strength I had, my hand on her other side pulled back with all its force. However, it was met with a strong resistance."
    "In my head, the plan was to slyly pull back, and pretend that I was just adding another layer of lotion. But what happened instead, was me getting caught and almost losing balance."
    "Her belly had an absurd weight, or rather, density. It felt as if I was attempting to move a rather large water balloon..."
    BBW "Is everything alright?"
    MC "Yeah, yep... things are just peachy keen."
    "My tone of voice betrayed my attempt to remain discreet."
    jump BBW047_c5_after

label BBW047_c5_after:
    "As the final layer was applied, I took a step back to admire my work. My hands emerged from her lower most belly roll, still slick with lotion."
    MC "Don't suppose you happen to have a hand towel I can borrow?"
    BBW "Mmmmmmm..."
    "It was then I realized just how much Alice had melted under my hands. Her entire belly was glistening in the sunlight, the bright glare could probably work as a beacon."
    "There was a rather cute smile on her face. As her head tilted, resting on her neck roll slightly, her expression was vaguely reminiscent of a content feline after getting its back scratched."
    MC "Alice?"
    "I got off my knees to see past her belly and breasts, only to notice that Alice had completely fallen asleep at some point."
    "She looked so peaceful there, completely at ease. It made me wonder just how often she got to relax like this."
    "After drying off my hands, I returned to my chair. Reclining back, I just watched the endless sea flow up and down in front of me..."
    "And the ocean was pretty cool as well."
    jump daymenu

label BBW048:
    $setProgress("BBW", "BBW049A")
    scene Summer Guest Bedroom with fade
    play music Rain
    "Coming inside after spending a full day on the beach, the three of us went to our respective chambers to unwind for a bit and get cleaned up before dinner."
    "Having returned once again, the luxuriant accommodations had not yet ceased to inspire awe in me."
    "The striking view from the late afternoon sun beaming through the window caused me to pause as I took in the oceanside vista."

    scene black with fade
    $setTime(TimeEnum.NIGHTLIGHTS)
    scene Summer Beach with fade
    "The weather here really is amazing, the location is perfect. I can't think of a more pleasant day I have had than today."
    "Gazing upon the azure waters, having tinted to more of a violet from the evening sky, the gently rolling waves made me wonder if this gorgeous day spent with such a beautiful woman had been real, or if I merely found myself in some idyllic surreal fantasy of my own imagination..."
    "I ultimately decided that my imagination was not this good, so it had to have been real."
    "My thoughts drifted all the more, taking in the view from my mind's eye of how Alice had looked in her swimsuit."
    show BBW swimsuit-happy with dissolve
    "Every curve, every dimple, every bit as warm and invitingly luxuriant as this seaside mansion. It's crazy how soft her body has become."
    "First getting the chance to help her fit her uniform, now this? I like where things are headed between us."
    "But it's more than that... her confidence, her self-determination, her dignified bearing, not for the sake of superficial appearances, as most who are of wealthy means do- Alice cultivated these attributes out of her own sense of respect for herself."
    "It was something I admired about her, all the more so given the additional challenges her growth had brought so far."
    hide BBW with dissolve

    scene black with fade
    $setTime(TimeEnum.DAY)
    scene Summer Guest Bedroom with fade
    play music MC
    "Lost in my thoughts I was suddenly jerked back to the present reality as the unpleasant brackish smell of my damp, matted hair wafted into my nostrils."
    "Having just come from the beach, the natural first task should have been to hop in the shower and wash all the sand off of my body, rather than reminisce over a day that had not yet passed."

    scene black with fade
    $setTime(TimeEnum.NIGHT)
    scene Summer Guest Bathroom with fade
    "After finally getting into the shower, the seemingly simple task of cleaning the sand off myself quickly proved to be more tedious than anticipated."
    "I hadn't given it much thought until now, but I haven't been to the beach since my factor started to kick in."
    "My hair, having been ravaged by the salty ocean water, combined with my careless regard when lying on the beach, created a sand encrusted tangled mop on top of my head. It felt crunchy and gross."
    "What I thought was going to be a brief, but relaxing shower in this luxury bathroom turned into a tediously difficult task that was taking the better part of an hour to accomplish."
    MC "Man, that is a lot of sand. Probably could have made a sandcastle out of all of that.
    I hope the pipes can handle all of it."
    MC "It wasn't too far fetched to imagine all of my sheddings mixed with sand was going to form some kind of makeshift concrete that would end up flooding the whole house."
    MC "Probably not... but might want to wrap this up quickly just in case."
    play sound Knock
    "{i}knock knock{/i}"
    "I heard a knock on the bathroom door."
    Takada "Mr. Hotsure- is everything alright in there? I didn't want to interrupt, but you've been in the shower for quite some time."
    Takada "It was requested by Miss Nikumaru that I check up on you. Dinner will be ready in 10 minutes. She wanted me to let you know so that you would not be late."
    MC "Oh! Uh, thanks, I'll be out soon."
    MCT "Crap! I'm only just now finishing up with the shampoo. If I don't at least take the time to put some conditioner in, my hair is going to be a wild frizzy mess."
    MCT "With this much hair, it would be pretty noticeable. Alice wouldn't like that. Not to mention I still don't think I have all the sand out of this thick mess growing out of my skull."
    MCT "Then again, she's a stickler for punctuality. It would certainly reflect poorly on me in her eyes if I showed up late, especially after sending in one of her servants to remind me."
    MCT "What should I do?"
    menu:
        "Take the extra time to be clean and presentable.":
            jump BBW048_c1_1
        "Cut the shower short to make it to dinner on time.":
            jump BBW048_c1_2

label BBW048_c1_1:
    MCT "I'll only be late for a handful of minutes, but I'll be a disheveled mess for the rest of the evening if I cut corners and don't get my hair under control. Better take the extra time to do the job right."
    "Taking extra time didn't mean I wasn't still in a mad rush. I squeezed out the bottle of conditioner and furiously raked it through my hair. Even this little bit helped my salt fried hair soften up quite a bit."
    "Once I got it all rinsed out, my crusty wadded mat had yielded into something much lighter and more manageable."
    "Having finished with the pressing issue, I flung open the shower stall door in a whoosh, grabbed a towel and began a frenzied effort to at least get serviceably dry before starting the painstaking task of taming these gorgon locks with a blow-dryer and brush."
    MCT "This is a very tedious and inconvenient aspect of my growth factor, but in light of what Alice and Aida have to go through on a daily basis, I'll gladly choose to deal with this instead."

    scene black with fade
    $setTime(TimeEnum.NIGHT)
    scene Summer Guest Bedroom with fade
    "Having sufficiently reigned in the beast I put on the nice polo shirt and dress slacks I picked out ahead of time for dinner before getting into the shower."
    "After putting on the clothes I gave myself a once over to see how well I managed to put myself together."
    MC "Hmm, not too shabby."
    "A few brush strokes to redo what pulling my shirt over my head messed up and I was good to go."

    scene Summer Hallway with fade
    "Checking my phone for the time to see the damage done revealed that I was 7 minutes late."
    MC "Seven minutes? Not great, not terrible."
    Lee "Aw, mista Hotsure, glad to greet ya comin'! I was sent to check up on ya. Ya know Miss Nikumaru won't start without ya, but she's not exactly patient either."
    MC "Sorry to cause concern. Please, lead the way."

    scene Summer Dining Room with fade
    play music BBW
    show BBW summer-int-stern at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Keisuke! Why are you late? I specifically had Takada check up on you earlier so you would know when you were expected to arrive."
    BBW "Dinner does not start until all guests are present- it would be rude of me as the hostess to do otherwise. In turn, as a courtesy to the other guests it is imperative that you be punctual."
    show BBW summer-int-neutral-2
    BBW "Speaking for myself, a few minutes delay is rather inconsequential but I'm sure Aida is absolutely famished by now."
    show PRG unique
    PRG "...I'm okay... I don't mind waiting for Hotsure-san..."
    show BBW summer-int-haughty
    BBW "Nonsense, I'm sure you're hungry as I am."
    show BBW summer-int-surprised
    BBW "... uh, imagining you would be Aida"
    show BBW summer-int-neutral
    BBW "- yes that's what I meant."
    MC "Pardon my tardiness. I had underestimated the effects of the ocean water and the sandy beach on my hair."
    MC "I guess I'm just not used to how much maintenance it needs these days yet. I needed some additional time in order to look presentable for the occasion."
    BBW "Hmph, some things can't be helped it would seem. You appear to have invested your time wisely."
    $setAffection("BBW", 1)
    show BBW summer-int-neutral-2
    BBW "Perhaps you can begin to appreciate how long it takes me to get ready now. I hope you realize these curls don't magically spring into place each morning when I wake up."
    Lee "Allow me to serve you Mr. Hotsure"
    MC "Thanks."
    show BBW summer-int-neutral
    BBW "Thank you Lee, that will be all for the moment."
    jump BBW048_afterchoice_1

label BBW048_c1_2:
    MCT "Better get out and get dressed. If I'm even a second late, I'm gonna hear about it from Alice."
    "Once I was finally sure I got all the shampoo rinsed out of my hair I immediately turned off the water and flung open the shower stall door in a whoosh!"
    play sound Thud
    "{i}SLAM!{/i}"
    MCT "Guess that was too hard, but whatever- there's no time! I grabbed a towel and began a frenzied clawing at the thick mess on top of my head, which in all likelihood only served to make it more knotted and wilder than it already was."
    "My hair was still kind of damp, but I got it dried off enough that I at least wasn't going to drip water everywhere. Done with that business, I rushed out from the bathroom to the bed to put on the nice polo shirt and dress slacks I picked out ahead of time for dinner before I got into the shower."

    scene Summer Guest Bedroom with fade
    "After putting on the clothes I gave myself a once over in the mirror and a few rakes of a comb to at least get the big knots smoothed out."
    "Smooth was not the right word, because it felt like I was tugging on my skull just to move it through my hair. I at least got the damp frizzled mess to hang down somewhat straight."
    "I managed to avoid the completely unkempt caveman look, but any honest evaluation would only rank it just a few points higher than that... which is basically your average school age guy with long hair."
    MC "Heh, not too bad!"

    scene Summer Hallway with fade
    "I sauntered down the hallway to the dining room with the knowledge that I made comfortable time, if only a minute or two to spare."

    scene Summer Dining Room with fade
    play music BBW
    show BBW summer-int-neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Keisuke, glad you could join us. I was worried you were not going to make it to dinner in a timely manner when you hadn't reemerged from your quarters in quite some time."
    show BBW summer-int-doubt
    BBW "Oh... Keisuke, what's wrong with your hair?"
    MCT "Damn, she noticed. Then again, who wouldn't?"
    MC "Heh, yeah, I kind of had to rush to make sure I wasn't late. I hadn't realized what a number the ocean and the sand did on my hair."
    MC "I guess I didn't quite finish the job- it's more to manage than I realized."
    show BBW summer-int-stern
    BBW "Your appreciation for punctuality is noted but it won't do for the occasion to remain in such a state."
    $setAffection("BBW", -1)
    show BBW summer-int-neutral
    BBW "Aida, do you by chance have a spare hair tie Keisuke can use to help reign in his unruly hair?"
    PRG "Yes. I hope this will do."
    MC "Thanks."
    "Aida passed me one of her spare hair scrunchies. Not being a stranger to having to resort to them before, I quickly corralled my hair and bunched it up in order to allow it to ride up to my neck height."
    "The result was a much more proper, but constrained ponytail that wasn't really my style. I began to regret the decision of my priorities but at least this temporary embarrassment would prevent my hair from frizzing out all over the place as I tried to eat."
    "On cue, the servants came in and with swift, coordinated efficiency, proceeded to set the table with the prepared dishes. A portion of each dish was served to our plates."
    "I didn't even have a chance to process what we were going to be eating before everything was in place and the dinning table was set."
    Takada "Miss Nikumaru and guests, dinner is served."
    show BBW summer-int-haughty
    BBW "Thank you Takada, that will be all for now."
    jump BBW048_afterchoice_1

label BBW048_afterchoice_1:
    MC "Well, let's eat."
    show BBW summer-int-haughty
    BBW "Indeed."
    "Like everything about this luxury vacation, I was quite impressed with the spread before us. My plate reminded me of a food magazine cover."
    "It was some kind of fish steak served as meticulously carved pieces with a variety of steamed vegetables- fancy heirloom varieties like red carrots and purple potatoes."
    "As for the steak, I knew it was fish, but I hadn't seen anything quite like it before. It had a seared crust on the outside where the heat had left a pale beige ring around the interior that framed the rich, pink flesh in the center."
    "It was the capstone of the best food presentation I had ever seen in real life. I took my first bite, going straight for the meat."
    MC "Mmmm..."
    MCT "Wow! This is really good. I could get used to this."
    "Eager to express my enthusiasm, I nearly forgot to not talk with my mouth full."
    "My hastily abrupt change in course nearly shoved it down the wrong tube."
    MC "{i}Cough{/i} -excuse me. {i}errahk{/i} Alice, what is this? It tastes amazing."
    BBW "Easy there Keisuke."
    "My fumbling of basic eating skills hadn't gone unnoticed."
    show BBW summer-int-happy
    BBW "It's seared bluefin tuna, my favorite meat."
    "That was certainly evident. I hadn't gotten the chance to notice until now, my attention previously drawn to the stunning display on my own plate, but Alice's portion of the prepared tuna was quite hardy."
    "So much so that it caught even me off guard, as I considered myself at least somewhat aware of her eating habits by this point."
    "Luckily, I had the presence of mind to restrain my reflexive facial expression of shock, so as to not draw undue attention and make her feel self-conscious."
    "Few things made me as happy as seeing Alice light up with delight when she was enjoying her food."
    BBW "This particular preparation however..."
    show BBW summer-int-aroused
    BBW "is simply exquisite."
    show BBW summer-int-neutral
    BBW "Though I'm unsure of the exact preparation used in this particular dish."
    show BBW summer-int-haughty
    BBW "Aida, with your culinary expertise, can you tell what was used for the seasoning?"
    show PRG excited
    PRG "I can definitely taste soy sauce and cayenne pepper, but there are several other seasonings I'm not sure of."
    show PRG unique
    PRG "I wonder if the chef will let me have the recipe, this tastes great!"
    show BBW summer-int-happy
    BBW "I'll have Francois write it down for you later. The servants here all cook to his recipes and specifications."
    show PRG excited
    PRG "Thanks, Alice."
    show BBW summer-int-neutral-2
    BBW "Think nothing of it."
    show PRG happy
    "Watching Alice dig into her meal, I realized what I had initially thought was an overly generous portion was all too paltry for her appetite, if her current haste was any indication."
    "True to her form, Alice was making sure each forkful was a refined action, though the pace of each was telling of her present hunger."
    "Even Aida, sitting next to her who was eating for ... well quite a few at least, was not up to the task of matching her bite for bite."
    "Admittedly, I found the spectacle rather befuddling- a strange mixture of feeling impressed, aroused, and concerned all at the same time to fluctuating degrees."
    MCT "Maybe I should say something?"
    menu:
        "Play it cool. Be subtle and don't raise her suspicion, but drop a hint.":
            jump BBW048_c2_1
        "Encourage her to eat more.":
            jump BBW048_c2_2

label BBW048_c2_1:
    MC "Mmmm, I agree Alice, this dish is truly exquisite. I have to thank you for being such a generous hostess, I would never have had such a wonderful culinary experience if not for your refined pallet."
    "Each bite just makes me want to slow down and savor the flavor for as long as possible."
    show BBW summer-int-happy
    BBW "I'm glad you are enjoying it as well Keisuke. Indeed, a truly great meal is worth savoring to its fullest."
    $setAffection("BBW", 1)
    "Alice modestly slowed her eating pace to a rate much more in line with her characteristic composure."
    "As much as I like seeing her enjoy her food, I know she would be hard on herself if she thought she had let her growth factor get the better of her sense of control."
    show BBW summer-int-neutral-2
    BBW "After being at Sochi Academy for so long, I had nearly forgotten how much I truly have missed such fine cuisine prepared by competent professionals."
    show BBW summer-int-haughty
    BBW "It would be a shame to not fully seize on the opportunity to avail myself to the present offerings."
    show BBW summer-int-happy
    BBW "I dare say I think I will elect to have another serving of seared tuna."
    show BBW summer-int-neutral-2
    BBW "Takada."
    Takada "Yes, Miss Nikumaru?"
    BBW "I request another serving of the seared tuna, if you please."
    Takada "Of course, Miss Nikumaru. We made sure to prepare plenty, knowing it was one of your favorite dishes."
    "Takada proceeded to serve Alice a portion that was nearly equal to her first offering, filling her plate all over again."
    show BBW summer-int-happy
    "Alice was clearly looking forward to getting to indulge in her favorite dish all over again."
    Takada "Would either of Miss Nikumaru's guests be interested in another serving as well?"
    PRG "I will have some more as well, Takada-san... {size=-6}although not quite so much...{/size}"
    MC "I'm good for now, thanks though."
    jump BBW048_afterchoice_2

label BBW048_c2_2:
    MC "I can see why you were looking forward to this trip."
    show BBW summer-int-neutral
    BBW "Oh, what do you mean?"
    MC  "Well, I've never seen you have such enthusiasm for any of the food at school like this meal. With good reason- it's exquisite, as you said."
    MCT "Why not fully avail yourself to as much of these culinary delights as possible before we have to head back?"
    $setAffection("BBW", -1)
    show BBW summer-int-sad
    BBW "Yes, I suppose I have been indulging my appetite since we've been on vacation. I should probably restrain myself a bit more in light of the present temptations in this environment."
    "My vocal enthusiasm backfired as Alice slowed the pace of her eating considerably. My comment must have inadvertently made her self-conscious over just how visibly she had been enjoying her food."
    "She became much more reserved in her movements. What was previously a burst of enjoyment across her face with each bite now appeared to be an expression of confliction."
    "No doubt her self-consciousness was weighing down her enthusiasm for something she had been looking forward to for quite some time."
    "Alice eventually worked her way through nearly everything on her plate, but for a few paltry bites."
    "Perhaps she was falling back on the old troupe of it being lady-like to leave something on your plate? It was one of the few assumed rules of etiquette I had never seen Alice make any effort to follow before."
    Takada "Miss Nikumaru, would you like some more seared tuna?"
    show BBW summer-int-neutral
    BBW "No thanks Takada, I believe that will be enough for me this evening."
    Takada "Are you sure Miss Nikumaru? I am aware that it was one of your favorite dishes, so we prepared extra. Was it not to your liking?"
    BBW "Not at all. It was exquisite, but I fear I have had too much already."
    Takada "Very well then Miss Nikumaru. Would either of Miss Nikumaru's guests be interested in another serving as well?"
    show PRG neutral
    PRG "I will have some more as well, Takada-san... Although not quite so much..."
    MC "I'm good. Thanks though."
    jump BBW048_afterchoice_2

label BBW048_afterchoice_2:
    "We continued eating in near silence for a minute or two, nothing much but the ambient clangs of silver and glassware that otherwise go unnoticed in the midst of conversation."
    "I've heard it said, 'better to be silent and thought a fool, than to open one's mouth and remove all doubt', but silence feels heavy and foolish decisions are my forte."
    MCT "Maybe a bit of small talk would lighten up the mood?"
    MC "So, what are the plans for tomorrow?"
    "Alice finished chewing and swallowed her food."
    show BBW summer-int-neutral
    BBW "Every summer vacation I'd play volleyball, believe it or not. It's not overly competitive and it is far more fun than other 'sports'."
    show BBW summer-int-sad
    BBW "However, I'm certainly less agile than I was before."
    show BBW summer-int-haughty
    BBW "I'd like to go swimming on the beach since we didn't swim earlier today."
    MC "Yeah, wading into the water is a bit different than actually swimming in the open ocean."
    BBW "Precisely, it would also be good exercise. I can't slip on my routine just because I'm on vacation."
    show BBW summer-int-neutral
    BBW "I trust you'll join me tomorrow?"
    MC "Of course, I'm also a bit curious what swimming with all this hair is going to be like."
    MC "I'm sure there's no way though I'll be able to keep up with you with all the extra drag on me in the water."
    show BBW summer-int-happy
    BBW "Aida, I understand you may prefer to stay on the beach but swimming is actually one of the best forms of exercise during pregnancy, if you'd care to join us."
    show PRG worried
    PRG "I- I don't know."
    show PRG unique
    PRG "This isn't a normal pregnancy. I'm not sure."
    show BBW summer-int-surprised
    BBW "-!"
    show BBW summer-int-neutral-2
    BBW "Aida, it's okay."
    show BBW summer-int-neutral
    BBW "If you'd like, I can help teach you to start swimming properly again."
    show BBW summer-int-neutral-2
    BBW "Trust me. I know how to swim with a belly."
    show PRG happy
    PRG "Okay, Alice. If you're willing to help me then I'll try swimming."
    show BBW summer-int-haughty
    BBW "Fantastic. It's settled then."
    show BBW summer-int-neutral-2
    BBW "Ahhh, what a lovely dinner, both food and present company included."
    MC "We would say the same as well."
    show PRG happy
    PRG "Thanks Alice."
    BBW "But I am quite full myself from the evening's delectable offerings. I could use post meal digestif."
    MC "Isn't that some kind of after-dinner wine?"
    show BBW summer-int-neutral
    BBW "Usually, but the point is to provide something after a meal that will stimulate digestion. Wine was one of the few things my father did not deign to provide for this trip."
    "Which is fine, it would not do for the occasion and would be unfitting for me as a hostess to provide, given that Aida is unable to partake."
    "I'd rather enjoy some ginger ale right now. Ginger is very effective at soothing the stomach. Would either of you care for some as well?"
    MC "Sure."
    show PRG neutral
    PRG "Me too."
    show BBW summer-int-haughty
    BBW "Lee! Could you please bring some ginger ale?"
    "A startled reply came from the kitchen."
    Lee "S-sure can, Miss Nikumaru."
    "A moment later, Lee came rushing out into the dining room."
    Lee "Here you go Miss Ni-"
    show BBW summer-int-surprised
    show PRG surprised
    "Lee had slipped and spilled the drinks everywhere, luckily managing to catch the glasses before they broke. It seemed he was used to such a feat."
    Lee "{size=-6}{i}jojdwaess-eo{/i}{/size}"
    Lee "Miss Nikumaru! I'm so sorry I'll clean this immediately!"
    "Shi rushed out of the kitchen to assess the situation."
    Shi "LEE! YOU IMBACI-"
    show BBW summer-int-stern
    BBW "Shino, that won't be necessary."
    Shi "-!"
    BBW "Spilling some drinks is not going to flood the house, nor set us back financially, I'm quite sure cleaning this up will rectify the situation."
    "Aida remained shocked, seeing Alice take this so calmly seemed to surprise her even more than Lee spilling the drinks did. I wasn't quite sure what to make of her reaction myself."
    "In all the time that I have known her, her exacting nature brought with it demanding expectations for the people that work for her- something Aida and I were intimately familiar with."
    MCT "Then again, perhaps my initial assessments have proven too simplistic. She certainly has high expectations for others and herself, but she has always proven quite understanding when unforeseeable or unavoidable circumstances interfere, such as schoolwork..."
    MCT "...or in Aida's case, the increasing difficulties as her condition progressed."
    BBW "Lee is perfectly capable of cleaning up this accident himself. Please retrieve an additional bottle of ginger ale for me and my guests so that we can continue the evening's pleasantries."
    show PRG worried
    "Lee's fumbling of the drinks was certainly a disastrous performance of his duties, but it was purely accidental, not something born out of laziness, insincerity, or without concern to improve in the future."
    "Perhaps that is the key difference for Alice, not that she expects perfect execution 100%% of the time, but rather a contempt for the acceptance of what is substandard and indifference towards improving one's self."
    "Or maybe she just has a soft spot for lovable klutzes like me."
    MC "Well, after all, no use crying over spilled ginger ale."
    show BBW summer-int-haughty
    BBW "Quite."
    show PRG admire
    show BBW summer-int-neutral
    BBW "Now, where were we?"
    MC "You were talking about ginger ale as a digestif."
    "Shino came out with a new bottle per Alice's direction. Quickly and quietly, so as to not distract from our conversation, she set our glassware and poured a glass for each of us before leaving the bottle with what remained next to Alice, likely knowing she will want more later."
    "Lee, in contrast to his earlier clumsiness, cleaned up the spill with quick efficiency."
    BBW "Ah yes, as I said before, a digestif is intended to be consumed after a meal to help with digestion, this could be wine or brandy, but herbal infusions are the most classic example."
    BBW "This is in contrast to an aperitif, which is a drink consumed before a meal or during appetizers to help stimulate the appetite, as the name would imply."
    "Seemingly unphased by the previous interruption, Alice continued to expound on the topic of fine dining etiquette and terminology."
    "It was something she was well versed in, while also keen on disseminating her knowledge to her listeners whenever the occasion would arise."
    "The conversation continued for quite some time. I tried my best to keep up and absorb the information as much as possible."
    MCT "I suspect I will be held accountable for knowing it later as it would likely come up as I spend more time with Alice."
    "Reflecting back on what just happened, I was proud of her. It would not have been unreasonable for her to have gotten angry, raised her voice, or even harshly chastised Lee for his mistake."
    "Instead, she displayed an unflappable grace throughout the situation that caught both me and Aida off guard."
    "Something tells me I still have a lot to learn about softer side of the hard nosed, industrious young woman I had come to fall for during my time at Seichou Academy."
    show BBW summer-int-surprised
    BBW "Oh my!"
    show BBW summer-int-neutral
    BBW "It appears we have run out of time if we are to retire early enough to be ready for tomorrow morning's activities."
    show BBW summer-int-neutral-2
    BBW "I trust you enjoyed this evening's dinner as much as I did?"
    MC "Absolutely, thank you again Alice."
    show PRG happy
    PRG "Yes, thank you Alice. It was lovely!"
    show BBW summer-int-haughty
    BBW "Excellent. Take your time going back to your rooms, but please make sure you allow enough time to sleep so that you will be refreshed in the morning. Tomorrow's activities start bright and early tomorrow."
    "Alice walked back to her room. Aida followed not long after back to her room as well."
    "I thought about a short evening stroll on the beach just to take in more of the evening, but after the ordeal I went through earlier to remove the sand from my hair- combined with my penchant for oversleeping, I decided better of it and retired to my guest room as well."
    jump daymenu

label BBW049A:
    $setProgress("BBW", "BBW049B")
    scene Summer Guest Bedroom with fade
    play sound Knock
    "{i}knock knock{/i}"
    play music Peaceful
    "A sharp banging on my door the next morning startled me awake."
    BBW "Keisuke, we are heading down to the beach. You better not be sleeping in."
    "Sleeping in was the first thing I had in mind during a vacation, but Alice did admonish me to get enough sleep last night, so I shouldn't have thought I'd get away with it this morning."
    "Rubbing the sleep from my eyes, I quickly got myself dressed for the water."
    "I put on my bathing suit and a light tee-shirt I didn't plan to wear for very long."
    scene Summer Living Room with fade
    "Following the stairs down from the house I could see Alice and Aida already down by the water."
    "I was hurrying a bit to not fall too far behind, but it didn't take too much time and I knew I wasn't going to miss anything."
    scene Summer House Back with fade
    "I stepped out of the beach house, only to be nearly blinded by the radiance of the early morning summer sun."
    "Clearly, I had not managed to fully shake the sleep from my eyes. Shading my sight with my hand on my forehead, I could finally take in the grand view of the beach from the Nikumaru estate."
    "It was a calming setting with the gentle rustling from the waves of translucent light blue waters. I could feel the hot air rising up from the ground as the summer sun beamed down on the pale sand."
    "Looking over at the beachside tent, it looked like Alice and Aida hadn't wasted any time setting up for the day at the beach."
    scene Summer Beach Ocean with fade
    show BBW swimsuit-neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG swimsuit-neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    "As I walked over, it looked like Alice and Aida had made themselves comfortable, having already arranged their towels and beach supplies out in an orderly fashion."
    "Noticing that both of them appeared to have been putting the finishing touches on each other's sunscreen coverage, I winced with the realization that I had indeed missed out on something due to sleeping in a few extra minutes."
    BBW "There you are Keisuke. I was worried for a bit that you had decided to sleep in and not make the best use of our time off."
    "I honestly couldn't tell if she saw right through me and this was intended as a subtle dig at my sleeping habits, or if I had genuinely managed to make good enough time to allay suspicion."
    show BBW swimsuit-haughty
    BBW "I'm eager to get started swimming. It's simply been too long, and I can't let my routine slip just because I'm on vacation. I trust you will be joining me?"
    MC "Absolutely. It's been a while since I got to swim. I'm looking forward to it."
    BBW "Excellent. Do make sure you've properly covered yourself in sunscreen. I don't want either of you suffering the ill effect of too much sun by neglecting something so easily preventable."
    BBW "Make sure you've given it enough time to dry before joining me in the water Keisuke."
    hide BBW with dissolve
    "With that, Alice turned and made her way towards the water."
    "I could tell she was eager for me to join her, but having sufficiently warned me the night before she had a full day of activity planned, I couldn't help but think her unwillingness to wait for me was an intentional consequence of my tardiness."
    "Still though, looking out towards the ocean I got a good view of more than just the water. Alice carried more of her weight out front, but that didn't mean there wasn't plenty to take in from behind."
    "Always mindful of her bearing, she was dainty and deliberate in her movements, especially for someone her size. I couldn't help but think it was more than my imagination her gait had taken on a subtle waddle as she navigated the loose terrane of the beach sand on her way to the water."
    MC "{size=-6}...she certainly fills out that swimsuit well...{/size}"
    "Snapping out of my swimsuit induced trance, I proceeded to get down to the business of slathering myself up with sunscreen, doing my best to make sure I covered everything."
    "Despite my best efforts, I couldn't quite reach everywhere."
    MC "Hey Aida, could you help me make sure I got my back covered?"
    PRG "Sure, Hotsure-san."
    "Aida was reclining back on one of the cushions with a beach towel under her while she was reading a book. I stooped down in front of her so as to not have to have her get up, trying to be mindful of her condition."
    PRG "There you go!"
    MC "Thanks for the help."
    MC "Say Aida, aren't you going to join us for some swimming? I'm sure Alice would want you to join us."
    PRG "That's okay Hosure-san. Maybe a little later. You two deserve some alone time together, so don't worry about me."
    MC "Oh, don't worry about that Aida. You make it sound like you're a third wheel- that's simply not the case if that's what you're trying to imply."
    show PRG swimsuit-happy
    PRG "Thanks Keisuke, but really, it's all right. I'm still a little tired from getting up this morning and I'd rather just relax for now."
    PRG "I brought a book I've been looking forward to reading that I haven't had time for back at school. It's Diant's Inferno, one of those classics I want to check off my lifetime reading list. Please, enjoy your time with Alice."
    PRG "I don't know if or how much she shows it, but I can tell she enjoys spending time with you.  And, seeing her all happy like that makes me feel good, too."
    "Aida had always been kind of a wallflower as long as I had known her, and normally I would have persisted a bit more to get her to join in, but I thought the better of insisting otherwise given how certain she came across with her decision to sit out for now."
    hide PRG with dissolve
    "I couldn't help but crack a smile given what Aida said. It felt reassuring to know I had a cheerleader in my corner who had Alice's ear."
    "Giving myself a pat down, I felt reasonably sure that my brief conversation with Aida had elapsed enough time for my sunscreen to dry up enough for Alice's satisfaction."
    scene Summer House Back with fade
    "With that task checked off, I proceeded to make my way down to the water's edge to see Alice steadily move through the water with a freestyle stroke."
    "Eager to meet her in the water, I waded right in, only to be caught off guard with the sudden difference in temperature from the water relative to the air when I became submerged past my groin."
    MC "WHOAH!"
    "I stood there frozen in my tracks, taking a couple of seconds to overcome the paralysis of a sudden ten degree drop in temperature, focused entirely on my nuts."
    "Having managed to overcome that initial shock, I continued to wade out into the water to greet Alice."
    "The depth was shallow enough that we could still keep our heads above water if we were standing but was still deep enough that we wouldn't have to worry about hitting the sea floor when trying to swim."
    show BBW swimsuit-neutral
    MC "Already putting the laps in?"
    BBW "I guess you could say that, but this was just a warm-up. I've been taking it too easy lately, I want to get a real swim session in. Think you can keep up?"
    if isEventCleared("BBW009"):
        MC "Definitely not after watching you crush Mizutani-san in a swimming race. And I know I'm not as fast as her."
        BBW "Tsk tsk, you have much to learn it would seem. If anything, Mizutani-san's loss to me should encourage you."
        MC "What do you mean?"
        BBW "Swimming is more about efficiency and grace while gliding through the water, rather than forcing yourself through it."
        BBW "Raw power is not enough to make up for poor technique. Keep that in mind and you'll do fine."
        MC "I guess I can see that. Go easy on me though, all this hair is going to be like dragging a net behind me."
    else:
        MC "Probably not, but I'll try. Go easy on me though, all this hair is going to be like dragging a net behind me."
    BBW "Suggestion noted, Keisuke- but ignored. How do you expect to get better if you don't push yourself to do more?"
    "I wasn't sure if this was Alice's way of trying to inspire me or if she just didn't want to pass on the chance to thoroughly demonstrate her skills in something she prided herself on."
    MC "Fair enough. What did you have in mind?"
    BBW "Let's start with the basics. We'll do a freestyle swim. See that driftwood log down the beach? Let's make that our distance marker."
    "I placed my hand above my head to block the sun's glare while I squinted into the distance to see where she was talking about."
    "It took a second to find it, but I was quite shocked at how far away it was when I did. The distance Alice had settled on was no joke for an amateur swimmer such as myself."
    "But it wasn't impossible either, especially since I wasn't trying to race."
    MC "I'll try my best to keep up. Got any tips?"
    show BBW swimsuit-haughty
    BBW "Yes, it's tempting to be lax in your movements but try not to just kick with your knees but use all three of your leg joints in a fluid motion to propel you forward."
    BBW "During the stroke, make sure your hand gently enters the water with your fingertips first while keeping your wrist and elbows above your hand."
    BBW " Keep your fingers extended underwater so you maximize how much of a paddle you can form with your hands. And try not to get too caught up in checking how far you have to go by raising your head out of water to see."
    BBW "That's a rookie mistake. You'll know when you've reached the end once you get there- because I'll be waiting there for you."
    MC "Heh, duly noted."
    BBW "Let's get started shall we?"
    stop music
    "Apparently that was as good as a 'ready-set-go' for Alice because she took off without any further delay."
    hide BBW with dissolve
    "I took off after her but as I moved through the water the full body exertion of swimming set in after the first 40 meters."
    "I'll have to focus on the technique that Alice instructed and temper my pace if I was going to go the distance. Trying to follow her advice, I resolved not to break in order to bob my head up far enough to see my progress."
    "I just had to accept I was in for the long haul. Through the clear azure waters I could tell she was increasing the distance between us, but this wasn't a race for me, it was survival at this point as I estimated I was only a third of the way through."
    "This was even more difficult than I was expecting. I couldn't say if it was because I hadn't swum in a while or if it had more to do with my hair acting as a dragnet behind me."
    "Swimming in the open-ocean was a different animal than a pool as well. The buffeting of the waves was creating more resistance and forcing me to correct course to try to stay straight."
    "At this point I was fatigued. If the water level beneath me wasn't something I could stand in, I would have resigned myself to drowning, but I wanted to push myself."
    MCT "Alice would be disappointed if I gave up. Plus, I at least had to save face for myself given that my growth came with the least amount of physical impediment compared to the rest of my classmates."
    "My muscles burned, and my patience was growing thin as I found myself getting a bit bored from this long distance (for me at least) with no relief in sight, but still I pushed through."
    "Just when I thought I was at my limit I felt a firm tug on my shoulder. It was Alice's hand."
    "Hopeful that I must have finished. I immediately surfaced."
    show BBW swimsuit-neutral with dissolve
    play music Peaceful
    BBW "It appears you took my advice not to keep looking up to heart. You looked like you were about to do another 100 meters if I didn't stop you."
    show BBW swimsuit-haughty
    BBW "I'm surprised you kept up as well as you did Keisuke."
    MCT "Another 100 meters? Taking two zeroes off that number would have been more accurate, but at least I managed to save face to Alice and pushed myself like I knew I could."
    "I seriously needed to catch my breath after that though."
    MC "Thanks...I...I tried to stay... focused.... {i}cough{/i} because I knew it wouldn't be easy for me."
    BBW "I hope you didn't use all your energy just on that. We still have the breaststroke, butterfly, and backstroke to do."
    "I put all my effort into getting this far down the beach, not thinking about having to swim back, let alone down and back again. I had a long morning ahead of me."
    MC "{i}Hoo, haaa, hoo...{/i} Sure, no problem. Just shaking off the rust. I could use a minute or two."
    show BBW swimsuit-neutral-2
    BBW "Well, let me know when you are ready. I'll be waiting on you. I didn't exactly overextend myself at the pace I chose you know."
    MCT "There's plenty of salt in the ocean water, I don't need more rubbed into my wounded pride."
    MC "I'll do my best to keep up- wouldn't want to let you down now."
    BBW "You're doing better than I expected to be honest. Keep in mind I've been doing this for nearly all of my life."
    BBW "It's one of the few physical activities I enjoy... and have a high degree of skill in."
    show BBW swimsuit-neutral
    BBW "We'll do the breaststroke back. That's an easy one to do a casual pace with. It's less movement intensive compared to freestyle."
    BBW "You'll want to save up some energy for when we do the butterfly stroke."
    "Much like before, that apparently was a sufficient indication for Alice for me to know that we were starting."
    hide BBW with dissolve
    "She pushed off back towards are initial starting point, this time doing the breaststroke."
    stop music
    "Not quite sure how that name caught on. I always thought of it as the frog stroke, since it's kind of how frogs swim. The word breaststroke brought other things to mind..."
    "Luckily, like Alice had said, this stroke was much more manageable and lent itself to maintaining a leisurely pace."
    "Unlike the side-to-side head movements of the freestyle stroke, I could look straight ahead as I came up for air and see how long I had to go."
    "I could see Alice wasn't in a frenzied mad speed rush, but her graceful and efficient movements in the water had her continuously extending her lead over me, even more so than before."
    "That was fine though. Alice was looking to get outside and be active to maintain a sense of her regimented schedule- I was just trying to get from point A to point B and not drown in the process."
    "I found this round much more enjoyable, as the near-imminent prospect of drowning from fatigue was far more remote of a concern."
    "It gave me a bit more time to take in just how clear the water was and how good it felt relative to the hot summer air above the surface."
    "After what seemed like ages, I finally made it back to the spot near the awning in front of Alice's family beach house."
    "I undoubtedly left Alice waiting longer this time, not having the same sense of urgency that spurned my initial performance."
    show BBW swimsuit-neutral with dissolve
    play music Peaceful
    BBW "There, that wasn't so bad now was it? You certainly took your time, but at least you're managing to finish."
    MC "Thanks, uh, I guess."
    MC "It's pretty tough for me to go this long, but you don't seem to be having too much trouble."
    BBW "It's not always a matter of effort Keisuke. Efficiency is just as important, so your efforts aren't wasted."
    BBW "It takes practice to master the mechanics of swimming in order to move through the water as smoothly as possible. In fact, it's far more important to keep in mind than in any other sport."
    BBW "Water is much denser than air, so anything you can do to cut down on drag is going to pay greater dividends than what you're able to do for running."
    MC "Makes sense. I guess I hadn't thought about it that way before."
    show BBW swimsuit-haughty
    BBW "Now that I've sufficiently warmed up, I'm fully prepared to go all out this time."
    BBW "I hope you're not already slowing down on me. Are you ready for something actually challenging this time around?"
    MCT "Actually challenging!? Was swimming the better part of a kilometer by this point in the open ocean a fake challenge?"
    MCT "Am I missing something here? If I wasn't still riding the pump of the previous swimming session while simultaneously being buoyed up from standing in the water, I felt like I would have fallen over by this point."
    "The sane part in my brain screamed to tell her no, but looking into Alice's eyes I could see how much she was enjoying herself with this."
    MC "Oh, so you're saying I should stop holding back this time?"
    show BBW swimsuit-happy
    "A wide, delighted smile spread across Alice's face."
    BBW "Heh! Liar. That's very funny Keisuke. I'll make you eat those words."
    BBW "Tsk, tsk, and to think all this time I held back just so you wouldn't get left too far behind."
    BBW "{i}Hehehe!{/i}"
    "Clearly Alice found great enjoyment from the fact that I jokingly insinuated my poor performance compared to hers was born out of some misplaced pity."
    "Whether or not torturing me by goading me to keep up was part of the thrill of it all, I knew there was more to why she was having such a good time dragging me along with her."
    "Like she said, this was one of the few physical activities Alice truly excelled at and actually enjoyed."
    "It was also something that wasn't hampered by her growth. Sure, her growth didn't bring about any physical decrements, but there's definite limits to how her sheer size can get in the way of doing certain activities."
    "Trying to run with a belly like hers couldn't be comfortable, sending rippling shockwaves all throughout her body with each foot fall..."
    MCT "On second thought- better refocus. If I spend too much time on that imagery my blood was going to start pumping somewhere else besides my muscles."
    MC "Alright, you got me. I'm going to need all the help I can get."
    MC "You said we're doing the butterfly stroke this time? I get tired just watching that. Got any tips for me like before?"
    show BBW swimsuit-haughty
    BBW "Of course, I do. Quite frankly I wouldn't expect you to finish without my help."
    "They say pride cometh before the fall, but I knew I was in no position to offer up a lesson in humility. On the bright side though, Alice is always interested in the tutelage of an eager pupil."
    BBW "If you're going to try to swim fast for this distance at your skill level, you'll easily waste all your energy. Focus on being relaxed and moving fluidly with your whole body."
    BBW "Keep your neck in a neutral position, not craning up or down all the time. You don't need to take a breath with each stroke on this one."
    BBW "Don't waste energy flailing your arms all over the place either, they just need to break the surface, not raised straight up out of the water."
    BBW "Think of pushing yourself backwards with the stroke of your arms, don't just flare them out to the sides, you're trying to keep a minimal profile in the water."
    MC "Gotcha- stay fluid, no flailing."
    BBW "Exactly, but it remains to be seen how well you'll put it into practice. Try not to keep me waiting too long this time, Keisuke."
    hide BBW with dissolve
    "Much less surprising this time, apparently that's what Alice meant to indicate 'GO!', but what was far more surprising was the speed and ease she was cruising through the water with."
    "She wasn't kidding about holding back before. I bobbed in the water dumbstruck for a couple of seconds at the unexpected athletic spectacle from Alice, but quickly snapped out of it with the realization I was expected to catch up to her sometime sooner rather than later."
    stop music
    "I dashed into the water eager to try to catch up, but after about twenty meters of that I realized even my best efforts weren't going to reduce the growing spread between us. I needed to focus on efficiency like she had said."
    "By fifty meters I knew I was in trouble, already worn out and not even that far into this one-sided race. I tried to distract myself from my fatigue by focusing on my cadence and the fluidity of my motions."
    "Effort wasn't going to get me through this, efficiency was. After what I could only guess was past the halfway point, the possibility of collapsing to the depths with Davy Jones crossed my mind, even though I could easily avoid a watery grave if I maintained the strength to stand up..."
    "NO! I had to keep going. If I just gave up, I was going to let Alice down. This was something she was really looking forward to doing on her vacation and she wanted to share it with me."
    "After the water polo fiasco, I told her to ask me whenever she wanted a swimming partner. I can't just bail on her on the first instance!"
    "This was one of the few things she could still enjoy and not feel self-conscious about her size. I know she puts on a show, but I can tell deep down she wishes this wasn't happening to her."
    "If I can help her forget about that for just a little while, then I'll swim across the whole damn Sea of Japan!"
    "My delirium induced post-fatigue pep talk wasn't quite enough to make it the full distance. I got slower... and slower... until I started to sink."
    "Before my hazy mind caused me to resort to a dog paddle flail in a vain attempt to save myself from downing, I felt a firm tug on the back of my head from my hair."
    MCT "Oh no!"
    MCT "This is it."
    MCT "I'm being dragged towards the light. My body yielded as a golden haired cherubic figure began to pull me towards the heavens..."
    show BBW swimsuit-neutral with dissolve
    play music Peaceful
    MC "BUHAAA! {i}Hoo, haaa, hooo!{/i} Alice!"
    "Alice, holding my hair, had pulled my head above water so I could breath."
    BBW "What am I going to do with you Keisuke? You looked like you were starting to get in trouble there."
    "I tried to catch my breath, but couldn't."
    MC "{i}Hoo, haaa,{/i} maybe, {i}haa,{/i} a-little-bit, {i}hoo, hoo,{/i} yeah..."
    BBW "Come on. Let's get you out of the water."
    MC "Wait a sec- OW!"
    BBW "Oh, you'll be fine."
    "Alice apparently wasn't going to risk me sinking, still firmly holding on to my hair until she dragged me a sufficient distance to where I could easily stand on the seabed."
    "As we walked out of the water, I began to crawl across the wet sand where the waves swept over the shore of the beach and collapsed in a heap on my back once I determined I was far enough in that the waves weren't going to crash over my head."
    "Alice sat down beside me about an arm's reach away, with her hands bracing herself upright, facing backwards while her belly filled up her lap with her legs forward."
    show BBW swimsuit-neutral-2
    "Craning my neck to peer behind me I could see the piece of driftwood Alice set as our distance marker."
    MC "Hey!... I {i}huff{/i} made it {i}huff{/i}"
    BBW "You certainly did. I didn't expect you to finish, you know. Honestly though, I don't know what possessed you to push yourself to the point you almost drowned."
    MC "You did."
    show BBW swimsuit-surprised
    BBW "What?!"
    MC "I didn't {i}huff{/i} want to let you down {i}huff{/i}"
    show BBW swimsuit-angry
    BBW "I was just teasing you back! We both know you aren't that great of a swimmer! Are you insane?"
    BBW "..."
    show BBW swimsuit-worried
    "Alice seemed to have stopped herself in the midst of her usual critical defensive reaction."
    BBW "...I didn't mean to put that kind of pressure on you. I'm sorry."
    MC "You didn't {i}huff{/i} there's no need to apologize."
    show BBW swimsuit-doubt
    BBW "Well then why are you blaming me!"
    MC "Alice, you didn't pressure me to push myself to my limit, you inspired me to."
    MC "I could tell you were looking forward to getting to do this on your vacation, and I wanted to be a part of doing something that you love, with you."
    MC "I knew I couldn't keep up with you, but I could tell you were enjoying having someone with you to share the experience."
    MC "If I just gave up, I thought it would just put a damper on the whole day."
    show BBW swimsuit-neutral
    BBW "It's just swimming, Keisuke. I do it all the time for exercise at school you know."
    MC "No, it's not just that- this place, the water, you're in your element. It's an escape and a refuge for you, isn't it?"
    MC "I didn't want to do anything that would diminish it for you at a time in your life when you need it more than ever."
    show BBW swimsuit-sad
    BBW "That's very sweet of you Keisuke."
    $setAffection("BBW", 1)
    BBW "{i}Sigh{/i}... You're not wrong. I had hoped my yearly summer retreat from my childhood would help bring me solace by taking me back to a time and place from before I started growing."
    show BBW swimsuit-worried
    BBW "Such a silly notion really. Even if it could all go away for a week I'd still have to return to school where it would all be waiting for me."
    show BBW swimsuit-neutral-2
    BBW "I guess even here I'll have to learn to live with how my body is changing. Swimming helps me do that. Thank you for joining me today Keisuke."
    MC "You're welcome- I wouldn't have missed it for anything!"
    show BBW swimsuit-happy
    BBW "Hehe! Well you've certainly proved that."
    MC "So, tell me more about this place then. It sounds like you have a lot of good memories from spending summers here growing up."
    BBW "I do. It's why I came to love swimming so much, and even volleyball like I mentioned last night."
    show BBW swimsuit-neutral
    BBW "My parents, especially my father, were always busy when I was young. Still are."
    BBW "I don't begrudge them for it, they taught me how much work it takes to be successful in business because of that. But when we stayed here, they got to spend time with me."
    BBW "As a little girl, I loved finally getting all the attention. Each year we came, I never wanted to leave."
    show BBW swimsuit-sad
    BBW "I guess part of me hasn't quite grown out of that yet."
    MC "I don't know if anyone ever grows out of that. Isn't that what nostalgia is? Who doesn't get sentimental from time to time about childhood memories?"
    MC "Maybe it's just something silly about us we have to learn to accept and not worry about so much."
    show BBW swimsuit-haughty
    BBW "Perhaps you're right."
    show BBW swimsuit-surprised
    "Alice began to take a look around, her expression looked like she had just remembered something she had forgotten."
    BBW "Oh! We should get going. This far down isn't part of our beachfront. These are all private beaches, so it would be frowned upon if we were caught loitering on someone else's beach."
    show BBW swimsuit-neutral-2
    BBW "I'm going to swim back. You're welcome to walk instead, you know."
    MC "Nah, I can do it. It's the backstroke this time, right? I can always just stop and float on my back if I get tired."
    MC "Just don't expect me to catch up to you any time soon. I'm going to take it nice and slow this time."
    BBW "I'll be checking up on you anyway just in case."
    "Wading into the water, Alice turned around, smiling at me as she waved goodbye for now before falling backwards into the ocean to swim back the rest of the way."
    hide BBW with dissolve
    "This time I wasn't surprised at her sudden departure and I didn't feel the need to immediately start chasing after her like before."
    MC "Well, I certainly got my workout in for today."
    $setSkill("Athletics", 2)
    "Exhausted but content, I waded back into the water, floating on my back. It was one of the rare occasions I was grateful to have my long bangs draped over my eyes."
    "The piercing summer sun beamed down on my face as I looked up into the sky while I drifted in the water."
    "I occasionally threw in a few strokes but for the most part was content to lay back and float. This was more my pace, but I suppose I would swim an extra 10km if it meant I got to spend more time with Alice."
    "I slowly drifted along making my way back to Alice's beach house, taking about four to five times as long to get back as I did going away."
    jump daymenu

label BBW049B:
    $setProgress("BBW", "BBW049C")
    scene Summer Beach with fade
    play music BBW
    "When I finally realized I arrived at my destination I began to walk back towards the house."
    "Looking up, I could see the servants were just finishing up setting out a fully catered beachside lunch under the tent. Looks like they had set up a volleyball net at Alice's request as well."
    show BBW swimsuit-neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG swimsuit-neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Looks like you managed to find your way back, slowpoke."
    show BBW swimsuit-happy
    "Alice grinned at her subtle chiding of my chosen pace. I could tell she was still appreciative of my earlier efforts though."
    BBW "You're just in time for lunch. Come join us."
    MC "Whoa!"
    "As I walked up closer, I got a much better look at the full splendor of the spread before us."
    "As to be expected with Alice, the usual expectation I had of some smashed sandwiches at the bottom of a cooler for a beachside lunch wouldn't do."
    "If this were any other occasion, I would have thought I'd needed a black tie just to walk around in a place serving this."
    "Everything was set out on ornate metal platters in bite sized servings as horderves. It was a cornucopia of fine dining selections."
    "There was a charcuterie board with cured meats and cheeses, most of which I didn't even recognize."
    "Most of the things I did recognize though, like the brined, whole olives, both the green and black variety. Bruschetta and tapenade were set out next to toasted banquette."
    "For the healthy selections there was beet salad and gazpacho. The centerpiece however was a tiered tower of fresh and cooked seafood kept chilled on a bed of ice."
    "There was the standard jumbo shrimp and oysters on the half shell, along with lobster claws and three different types of crab claws, pre-cracked of course."
    "For dessert there were these perfectly sectioned squares of what appeared to be real deal lemon meringue pie. I'd only ever had the crummy cheap yellow snack cakes that tried to imitate the real thing."
    "The only thing missing was a swan carved out of ice."
    Takada "Miss Nikumaru and guests, lunch is served. Please, enjoy."
    show BBW swimsuit-neutral
    BBW "Thank you Takada."
    BBW "Aida, please go ahead, guests first."
    PRG "Um... thank you, Alice. But, are you sure?"
    BBW "As the hostess, I insist."
    "Unbeknownst to Alice, she would eat those words rather than get to eat any food for what seemed like an unnecessarily long delay."
    "Whether it was Aida's naturally timid and hesitant disposition, or deep contemplation concerning her changing tastes due to her pregnancy, Aida hovered indecisively in front of the food display to the point that it began to feel awkward."
    "She was standing too close to just cut in front of her, but far enough from the table she was standing in the way of everything."
    BBW "..."
    "Alice shot me a side glance, trying to say without saying out loud 'what is going on?'"
    MC "... {i}shrug{/i}"
    "I could tell Alice was getting frustrated. She was obviously very hungry by this point."
    "I myself was feeling almost ravenous after this morning's swim session, and I knew my appetite at its biggest couldn't match Alice's at its smallest."
    "I could tell Alice wanted to say something, if not outright shove Aida out of the way by this point, but even at her most impatient, she'd never lose her composure or go back on her obligation as a hostess."
    "I thought I should say something before Alice felt like she had to."
    MC "Is everything alright Aida? It's okay if you aren't feeling hungry."
    PRG "It all looks so good, but my nose has been really sensitive lately.  With the ocean right there, all I can smell is salt and fish.  So... maybe something sweet would be nice?"
    MCT "Bingo! Okay, we can move this along."
    MC "Well, why not have dessert first? This lemon meringue looks great- maybe you'll get your appetite back later. Just have one of these for now."
    show PRG swimsuit-happy
    PRG "That's a great idea Hotsure-san."
    "I grabbed a plate and served up a piece for Aida, hoping to move things along faster to make up for the delay."
    show PRG swimsuit-neutral
    PRG "Thank-you Hotsure-san."
    "As Aida walked back to her seat on the cushions under the tent, Alice looked at me while shaking her head, expressing 'thank you' with an exasperated smile for what I just did."
    $setAffection("BBW", 1)
    "I decided to forgo my turn so Alice could, in the more figurative sense, get down to business."
    MC "Ladies first- I insist."
    show BBW swimsuit-haughty
    BBW "Such a gentleman."
    "Whether she meant that in the sincerest sense of the word or not, her appreciation was still evident in her tone. There was plenty of food to go around, or at least I had thought."
    "Seeing Alice's ruthless efficiency as she picked out every dish she wanted without hesitation and managed to fill every square centimeter of her plate in just a few seconds."
    "It made me question whether or not her initial offer to go last served a more practical purpose."
    "As Alice took her plate back to the spot she had picked out to recline under the tent I decided it would be prudent to get what I wanted in one go on my plate."
    "I honestly did not know what else would be left if Alice decided to come back for seconds or thirds. I ended up taking a little bit of everything, since it all looked good."
    MC "This is really good!"
    "I exclaimed, taking my first bite as I sat down between the girls."
    show BBW swimsuit-neutral
    BBW "I'm glad you're enjoying it."
    "No sooner had I sat down than Alice had gotten back up for a second pass, leaving an empty plate in her stead. One of the servants quickly removed it from her seat after barely a few seconds."
    "On her way back, Alice's plate was stacked full again, this time with different dishes she had not taken the first time around. I was surprised, maybe even a little impressed, but I decided not to say anything."
    "Anyone would be hungry after a morning of swimming. If I don't stop staring, I might accidently call attention to it. I figured I better try to steer the conversation elsewhere."
    MC "Feeling better Aida?"
    PRG "Yes, thank you. Having something small helped stir my appetite a bit.  I think I might have something more, just preferably not seafood."
    "I probably didn't need to worry about it, given how much food was set out, but part of me did think if she wanted to eat lunch, she'd better do it now before it was all gone."
    "By the time Aida came back to her seat with her food, this time with much less indecision involved, Alice was on her way back to the table to get dessert."
    "Curiosity got the better of me, but I didn't want to make her feel self-conscious. I adjusted my shoulders and neck so as to be looking at the ocean waters, belying my true gaze out of the corner of my eye."
    show BBW swimsuit-neutral-2
    "I was right to be cautious. Alice appeared to be checking to see if anyone was noticing her."
    "I wish she wouldn't continue to cling to this kind of pretense, especially around Aida and me of all people, but in all fairness, it would be difficult for anyone to not feel self-conscious with her growth."
    "Having determined to her knowledge that no one was looking, she proceeded to serve herself the remaining lemon meringue squares from the sheet pan."
    "I suspected since Aida and I had each gotten a piece for ourselves, she didn't feel the necessity to let any more remain."
    "I continued to pretend to pay no mind as she walked back to her seat with a plate full of treats, focusing my gaze down at my own plate instead."
    show PRG swimsuit-happy
    PRG "Oh, thank you, Alice! You didn't need to get up to bring us dessert."
    show BBW swimsuit-surprised
    BBW "Oh... well it was no trouble at all..."
    BBW "I thought... we could all enjoy dessert together after this lovely meal- yes."
    "Unbeknownst to her, Aida's reflexive appreciation of what she interpreted as a nice gesture had left Alice absolutely mortified, judging by how the color had drained from her face and her hesitant reply."
    show PRG swimsuit-neutral
    show BBW swimsuit-worried
    "Aida had been more preoccupied with her meal at the time, so she didn't notice like I did."
    "However, her remark clearly indicated that a normal individual would not have even considered the portion Alice had selected for herself was intended for only one person."
    PRG "Whew. I think I'm going to be pretty full by the time I finish what I have, though."
    MC "I'm good for now. Maybe I'll have one later, but don't save any on account of me."
    "I tried to play it off that her portion was not unreasonable for one person to finish."
    show BBW swimsuit-haughty
    "Having essentially gotten 'permission', in a sense, from both of us to finish the remaining dessert, Alice's expression visibly relaxed."
    "She proceeded to work through her dessert course, though perhaps not as fervently as she initially may have before Aida had said something."
    MC "I can see why you wanted to swim in the morning. Aren't you supposed to wait three hours after eating before swimming? That wouldn't have left much time before night."
    show BBW swimsuit-neutral
    BBW "That's just a common rumor. Swimming is no different than any other exercise where it may not be wise to exert yourself so intensely on a full stomach."
    BBW "It comes from people worrying about getting cramps while swimming that could interfere with their ability to come up for air, but that problem is more related to hydration than if you just ate food."
    MC "Makes sense. Three hours always sounded way too long to me anyway. Professional swimmers are in the pool almost all day- they can't just not eat."
    BBW "Exactly. It's never been a problem for myself."
    MC "What did you have in mind for the rest of the day?"
    BBW "Well as I mentioned last night, I would like to play some volleyball, especially since I have the both of you to play with. I haven't gotten to in quite some time."
    BBW "I much prefer doing it on the beach. Less people on the court in sand volleyball increases the importance of strategic thinking and shot placement."
    BBW "Plus, the sand is far more forgiving when diving for the ball."
    MC "Sounds good. I'm up for it."
    "I began to get up and stretch to shake off the stiffness from the morning's previous activities."
    BBW "Easy there Keisuke. I didn't mean right now. I appreciate the willingness and enthusiasm, but part of a well-planned vacation includes some scheduled rest."
    BBW "Just because exercising after eating too soon isn't life threatening doesn't mean it's not prudent to wait a bit."
    "Having finished her dessert, Alice proceeded to reposition herself between the beach furniture cushions under the tent. She laid down along the beach blanket over the sand while propping her head up against one of the cushions."
    "Once she had found what she deemed to be a sufficiently comfortable position, she interlocked her fingers and rested them on the cresting portion of her belly, partially covered up by her boobs."
    "Having just finished lunch, her belly was looking particularly full and round- more so than I had ever recalled."
    "Watching it rise and swell with each breath she took in was turning up the heat for me far more than the radiance of the midday sun."
    "Feeling a bit of a tug on the fabric of my swim trunks, I suddenly realized the thin material of my bathing suit was not going to conceal my raised sails."
    "Thinking quickly before it became too noticeable, I decided to lie down on the beach blanket next to Alice, chest down though."
    "Turning my head to the side, I still got a good view to drink it all in. Her belly towered high over the rest of her, even more so from this angle."
    scene black with fade
    MC "Yeah, a little rest feels good..."
    jump daymenu

label BBW049C:
    $setProgress("BBW", "BBW050")
    scene Summer Beach Ocean with fade
    play music Peaceful
    "Whether it was from a food coma, the warm summer sun, or the pent-up exhaustion from the morning's swim, I must have dozed off."
    show BBW swimsuit-neutral with dissolve
    BBW "Are you awake? Honestly Keisuke, sometimes I wonder if you would just sleep forever if left to your own devices."
    "Still in a sleepy haze, it took a second or two for things to come into focus. Alice was standing over me with her arms crossed, if she hadn't been bent over enough to look down at me, I certainly would not have been able to see her face over her belly."
    MC "Wha? Oh, yeah, guess I dozed off there."
    BBW "I think we all did for a little bit, but it would be a waste of a day just to lay about."
    BBW "You said you were up for playing some volleyball with me, so we're going to get that in before it gets too late in the day."
    MC "Fine with me. I'm up for more after some food and rest."
    show BBW swimsuit-haughty
    BBW "Good. Come on, Aida is already waiting."
    "The volleyball net was set up a short distance from the tent."
    show BBW swimsuit-haughty at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG swimsuit-neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "I'm assuming both of you are at least somewhat familiar with the rules of volleyball?"
    PRG "A little..."
    MC "Yeah, but it's been a while."
    BBW "That's fine, we'll just stick with the basics. The obvious rules are you can't catch the ball, and the goal is to not let the ball touch the ground on your side."
    BBW "You can't have any successive contacts with the ball, so you need to either send it over the net or pass it to a teammate. In sand volleyball only three total contacts are allowed per volley, but we'll ignore that for now."
    BBW "The main skills you need to know are the forearm pass, and the set. These will help you keep the ball in the air and off the ground- even if you don't know anything else."
    MC "Gotcha."
    BBW "First I'll show you the set."
    "Alice tossed the ball straight up, bringing her hands close together over her head, nearly touching her fingertips together she pushed it straight back up in the air once it came back down and made contact with her hands."
    "She did this a few times in a row, each time perfectly straight up, never taking her eyes off the ball as she continued to explain."
    BBW "The trick is to use more of your fingers and not so much of your palms. This is mostly a set up move for your partner to line up a good shot over the net, which is why you want it to just float up and have a simple trajectory."
    "Alice caught the ball and cradled it against her side after finishing her demonstration."
    BBW "Make sense?"
    MC "Yeah, easy enough, I guess."
    PRG "I think so."
    BBW "Good. The next main skill is called the forearm pass. As the name implies this lets you control the direction better when you return a volley in order to pass it to your teammate."
    "Alice tossed the ball straight up again. She brought her hands together with one hand cradling a fist made with the other while she kept her arms straight."
    "The ball landed on the lower part of her forearms as she bumped it back up into the air. This time she had to adjust her placement a little bit as the ball moved more from side to side."
    "It still wasn't much repositioning though. Her control was excellent."
    BBW "You want to make contact with your forearms. If it hits your wrist or hands, you have no control over how it will bounce off, and if it hits your upper arms, it won't go very far at all."
    "Alice caught the ball to stop it again to see if we were following along."
    BBW "Got that?"
    MC "Makes sense to me."
    PRG "Mhmm."
    BBW "Alright, time to put your attentiveness to the test. I'm going to pass the ball to one of you and you return it to me with either a pass or a set."
    BBW "Once you return it to me, I'll pass it to the other. For now let's just try to keep it off the ground."
    "{i}Bump{/i}"
    "Alice gently passed the ball to me with a nice, easy arc that was no problem to return back to her with a pass. She deflected my volley directly at Aida who was standing to my left as we formed a triangle."
    "Aida had no problem lofting up a nice and high set. We went back and forth like this for quite a while."
    "Any time the ball landed dead on the ground was due to some wild shot from either me or Aida setting it behind us or passing it right into the sand."
    "Alice's shot placement was always spot on, and she was always able to save the ball from the ground even after some of our questionable returns."
    "We started keeping track how many successive passes we could get. Our previous best was 10, but right now we were on a roll."
    "{i}Bump{/i}"
    MC "Fifteen"
    "{i}Bump{/i}"
    BBW "Sixteen"
    "{i}Bump{/i}"
    PRG  "Seventeen"
    "{i}Bump{/i}"
    BBW "Eighteen"
    "{i}SPLAT{/i}"
    "In my eagerness to receive the ball I took a couple of extra unnecessary steps, only to receive it directly with my face, rather than my forearms."
    "Having missed the ball completely with my arms, and unable to correct its trajectory, it bounced right into the sand."
    show PRG swimsuit-surprised
    show BBW swimsuit-neutral
    PRG "A-Are you alright, Hotsure-san?"
    BBW "I'm sure he's fine. He's endured much worse- that's for sure."
    "Alice was right, a light bump on the head from a failed return was nothing compared to a cannon shot to face from Akira."
    MC "Yeah, no big deal. I'm fine. Sorry to ruin our streak."
    show PRG swimsuit-neutral
    BBW "It is not a big loss. You both maintained it for a sufficiently long period of time for me to think we're ready to play a real game."
    MC "A real game? But there's only three of us. Don't we at least need four people?"
    BBW "I'll make do. You and Aida will be on one team, and I will be the other. Considering your fledgling skills, this will be an appropriate handicap, but I get two volleys to keep it fair."
    MC "Seems like it will be pretty hard to cover the whole court by yourself."
    show BBW swimsuit-haughty
    BBW "I'm up for the challenge."
    "I hadn't known Alice to take on a challenge she genuinely thought she could not win, so she must have been feeling pretty confident in her volleyball skills."
    BBW "Accurately serving is an advanced skill, and you can't hit the net on serve. In the
    interest of keeping the game moving, I'll play all time server, but you two can still score points like normal if you manage to have the ball land on my side."
    BBW "Does that sound fair?"
    MC "Fine for me. It's probably for the best."
    PRG "I'm okay with that."
    "We lined up as each of our respective teams on either side of the net. Alice eyed us both with a sly, possibly smug smile, as she lobbed up the ball and smacked it over our side of the net in what would be the first of many."
    "{i}Swoosh!{/i}"
    "In complete incoordination between Aida and I, the ball sailed right between the two of us untouched and landed in the sand on our court behind us."
    MC "Oops."
    PRG "Sorry..."
    MC "Don't worry about it. We just weren't thinking. We'll have to work together. I'll stand closer to the net since I'm taller and you stand further back to get anything that goes over."
    PRG "Right!"
    "I tossed the ball back to Alice under the net. I could see her competitive nature was now fully awakened. She had a devilish grin of satisfaction from having completely outmaneuvered her opponents."
    "Alice set the ball again, placing it in the same spot, likely testing us to see if we had learned from our previous mistake. I jumped in front of it, landing a decent set which let Aida pass it over the net."
    MCT "A success!"
    "But it wasn't good enough as Alice just walked right up and lobbed it over both of us. She had placed her shot to take advantage of how we moved out of our positions and didn't reset."
    BBW "A slight improvement."
    MC "Better than last time at least."
    BBW "You'll have to do better than that I'm afraid if you are going to score a point. I don't see how I can go easier on you than doing this all by myself."
    "As the match continued, Aida and I continued to improve in our coordination. We were able to return more serves and more of Alice's return volleys, but at 0-7 we were still pitifully behind."
    "Alice definitely was good at this, but this was still kind of sad. We had to change something."
    MC "Aida, I have a plan."
    PRG "Okay! What is it?"
    MC "She keeps beating us with her shot placement. She keeps putting the ball where we aren't, while we're just trying to get it over the net."
    MC "We need to use her same strategy against her, only we should be more effective because there's only one of her."
    MC "I may not be that accurate, but I know how to spike the ball and I have a height advantage on her. If I get the ball, I'll pass it to you, then you pass it to me."
    MC "If you can give me a nice gentle pass, I'll have the time to figure out where I want to put the ball and I'll fire it to the opposite of where she's standing on the court."
    MC "If the ball comes to you first, just do your best to set it up for me and we'll do the same."
    PRG "That should work..."
    PRG "I hope I don't let you down."
    MC "Don't worry, it's just for fun, but let's try our best anyway."
    BBW "Are you ready yet?"
    MC "This time- I think so."
    "Alice lobbed a serve to the back towards Aida. To her credit Aida stayed calm and passed me a nice gentle arc towards where I was standing near the net."
    "With a very light tap of my wrist I gave the ball just enough energy to make it over the net."
    "Alice realized what happened all too late, as she ran up to the front of the net. She dove into the sand with the hope of keeping the ball alive but she did not make it."
    show BBW swimsuit-doubt
    BBW "Hmph."
    "Alice dusted herself off."
    BBW "And to think I was starting to go easy on you two."
    "Our new strategy wasn't perfect, we still gave up a few points here and there, but we slowly started inching ahead. Alice's accuracy with the ball was excellent, but it became apparent she had overestimated her ability to cover the court."
    "Knowing that she had felt confident she could beat us, as the game continued it was increasingly clear to me that Alice was not nearly as adapted to her body's recent changes as I had initially thought from seeing her swim."
    "Instead of landing on her forearms, more than a few of her passes landed with a muted {i}BLUMP{/i} as they sank into the ample flesh of her boobs, rebounding with a much weaker trajectory than intended."
    show BBW swimsuit-worried
    BBW "Oh my... that hasn't happened before."
    "Her speed was impressive given her size, but the bulk of her thighs and her belly sticking so far out in front of her did not lend itself to an efficient running stride."
    "She jiggled all throughout her body, while her thighs rubbed together. Much more so than her speed, it was evident that her agility, the ability to change her direction to be in the right place, had been greatly affected by her added weight."
    "By the time we were able to return the ball over the net, Alice was not able to fully accelerate back towards the new spot she needed to be on the court."
    show BBW swimsuit-angry
    BBW "{i}Whew{/i}, 18-20. Match point!"
    "Alice called the score like she had for each set. Alice looked flustered and tired. Aida and I were on match point. I don't know if she thought it was supposed to be easy, but she was clearly disappointed with her performance."
    "As she wound up for this serve, she looked determined. Something told me she was going to try blasting this one as hard as she could before we even got the chance to react."
    "She hadn't really done anything like that before though, probably not wanting to accidently beam Aida in the belly with the full force of her serve, but maybe now she was desperate enough to not care."
    "After she tossed up the ball, Alice laid into this serve like I hadn't seen before. She fired it straight between us- I barely had any time to react..."
    "{i}Twack{/i}"
    "The ball hit the net. The slack let out on the upper part of the net before the ball tumbled harmlessly over the side, an illegal play on a serve."
    "It was certainly anti-climactic, but Aida and I won."
    MC "I guess that's game."
    show BBW swimsuit-worried
    BBW "That would be correct."
    show PRG swimsuit-happy
    PRG "I-I didn't think we would win! Great job Hotsure-san!"
    MC "Well it wasn't just me Aida, I needed your help."
    "Alice had a rather blank expression on her face in contrast to the fiery intensity seen just a few seconds ago."
    "No doubt she was trying to not visibly express her disappointment in herself. I didn't know how much good it would do, but I figured I'd try to cheer her up."
    MC "Alice, you were amazing. We barely won, and there were two of us!"
    BBW "Not nearly amazing enough it would seem. You won according to the rules we agreed upon."
    show BBW swimsuit-neutral
    show PRG swimsuit-neutral
    BBW "I wouldn't have set them out as such if I thought it was not possible for me to win. I must admit, you both did better than I expected. Even my miss at the end could be attributed to your efforts to wear me down."
    MC "Well, that was technically the strategy. We weren't going to win just with skill."
    BBW "Strategy is also a skill. A skill of yours I underestimated."
    MC "I guess next time we'll have to do a full two on two."
    BBW "Perhaps, but that may be a while. Honestly, I didn't find it as enjoyable as I remembered, especially compared to swimming... It didn't really feel the same."
    "It was unfortunate that something she had looked forward to on this vacation turned into another reminder about the changes going on in her body that she couldn't control."
    "I wanted to say something comforting, but my initial consolatory remarks had bounced right off. Besides, for the moment, she seemed keen on moving past it."
    show BBW swimsuit-haughty
    BBW "Speaking of which, Aida, if you're still feeling up for it, I believe I promised to give
    you a swimming lesson."
    PRG "I'd like that. I almost forgot about it. Thanks for remembering."
    BBW "Come with me."
    scene Summer House Back with fade
    show BBW swimsuit-haughty at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG swimsuit-neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    "Alice led Aida down to the water. Alice alternated between demonstrating different techniques herself and helping to position Aida in the water so that she could mimic what she had just been shown."
    "I hung back down the beach at a slight distance, alternating between treading water and wading in the shallows."
    "I didn't want to be aloof and just stay back on the shore, but I felt it best to give them both some space so Aida's lesson could feel more private, since Alice would likely have to make some references to her pregnancy."
    "I could overhear a bit of what she was saying."
    BBW "I know you can swim quite well Aida, but there is always more to learn. I'll show you something a bit more advanced."
    BBW "Possibly the most important thing to teach you for now is the side stroke. It's not as well known, but it is an energy efficient way to move through the water."
    BBW "It lets you keep your head above water at all times, and most importantly, your belly won't get in the way of your leg and arm movements. Like so."
    "Alice proceeded to demonstrate the sidestroke she spoke of. It involved kicking the legs in a scissors like motion while lying on the side with the arms spread out in opposite directions."
    "I'd seen it before, but not that often. In all honesty, I probably could have used it this morning to go the distance rather than exhaust myself."
    PRG "...is this good?"
    BBW "You're doing just fine. Spread your legs and arms out further for a stronger stroke."
    "Alice for her part seemed to be enjoying herself. Her dour and frustrated expression from earlier when we were playing volleyball had turned into a content smile, as she carefully watched over her swimming pupil."
    "Much like how Alice wanted to bring me along to share how she enjoyed swimming, she was doing the same with Aida, but this time in a way that was suitable for her."
    "Earlier I couldn't find the words to help her feel better about what was undoubtedly a disappointing realization regarding her newfound dimensions and the ability to play volleyball like she used to."
    "But then I remembered what she said earlier 'I guess even here I'll have to learn to live with how my body is changing.' I suppose this was her way of doing that. After all, she seemed to have moved on from that incident rather quickly."
    BBW "It looks like you've got the basics down Aida. You've taken to my advice quite well. I think that's enough for today, however. I don't see the need to push you any further."
    PRG "Thank you Alice. I am starting to feel tired. This was fun. I'd love to swim with you again sometime... if you'd want to."
    BBW "Of course, Aida."
    "Alice turned to me."
    show BBW swimsuit-neutral
    BBW "Keisuke, we're going to head back inside. I believe I am satisfied with how well we managed to fill today with the scheduled activities. Please come join us."
    scene Summer Beach with fade
    "We walked back towards the tent to get our towels to dry off after coming out of the water. Aida went up ahead as I stopped to talk to Alice."
    MC "You looked like you were enjoying yourself out there with Aida. You're quite the swim instructor it would seem. It appears you already have two students."
    show BBW swimsuit-haughty at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    show PRG swimsuit-neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "Well, if you enjoy something, isn't it natural to want to share that with others?"
    MC "That is true. Passion can be infectious. Even though I'm feeling worn out, today was a lot more fun than a lazy day on the beach."
    BBW "That's the advantage of structure, Keisuke. There's great satisfaction to be found in an accomplished day that eludes those who sleep halfway through it."
    "At this point, I wasn't sure if she was just making a general observation or was trying to drive home a point with a not-so-subtle jab at my tendency to hit the snooze button."
    BBW "But it was indeed a full day and I'm feeling ready for some rest myself. I'm actually surprised you managed to keep up today, Keisuke."
    BBW "It just goes to show me you have a lot of untapped potential. Perhaps all that's missing is the proper motivation..."
    show BBW swimsuit-aroused
    "Alice's expression turned to a smug, yet sultry smile. My 'proper motivation' was apparently no secret to her."
    show BBW swimsuit-neutral
    BBW "Well, come on now. Let's get dried off, Aida is already ahead of us."
    "We both walked back to the tent as Aida was finishing drying off. I started rubbing my towel through my hair, knowing nothing would get dry if that wet mess was still dripping all over me."
    PRG "I think I'm going to head in. I'd like to lie down for a while, if that's okay."
    BBW "Think nothing of it. Please go ahead Aida, we'll catch up to you."
    "Not thinking much of it at first, I was standing behind Alice when I noticed her bending over to get her beach towel."
    "{i}RIIIIP{/i}"
    show BBW swimsuit-surprised
    BBW "..."
    MC "...!"
    "My head would have snapped to attention from the sound, if my gaze hadn't already been transfixed on the sight unfolding before me."
    "Alice had ripped her swimsuit."
    "It was certainly loud enough for me to hear, but Aida was far enough away she likely didn't have any idea what just happened."
    "She was standing in front of both of us, so she didn't see. I on the other hand got quite a good look at a lot more skin on Alice's backside than the bottom part of her swimsuit intended to reveal."
    "This was not a little tear- only the edge of the fabric on the other side of the rip was hanging on for dear life where the bottom had split slightly off center, revealing nearly the entire middle of her backside."
    "Part of me wanted to stop to drink in the sight of Alice's fully exposed cheeks of her giant, plump ass. At this point however, between Alice's shocked, embarrassed expression, and the stupefied look on my face, Aida was going to realize something was up if I didn't think of something fast."
    menu:
        "Pretend nothing happened.":
            jump BBW049C_c1
        "Come up with a distraction.":
            jump BBW049C_c2

label BBW049C_c1:
    show PRG swimsuit-worried
    PRG "Something wrong?? You both look a little flushed.. Did you lose something in the water?"
    MC "What?! No, I don't think so."
    "I padded my swim trunk pockets in a feigned show of assurance."
    MC "Nope, everything is fine!"
    PRG "Oh my! Alice, your face must have gotten sunburned."
    "Alice's cheeks were cherry red, but not for the reason Aida was thinking."
    PRG "Here, I have some aloe vera gel in my bag. I hope it helps..."
    "Aida walked back over to Alice, rummaging through her beach bag. Finally finding what she was looking for she looked up."
    show PRG swimsuit-surprised
    PRG "Oh! Um... {size=-6}I see{/size}"
    show BBW swimsuit-angry
    "No longer having to be subtle Alice quickly tried to wrap her towel around herself."
    "Obviously flustered and not thinking clearly, she tried to wrap her beach towel up high over her waist, but that didn't leave enough length left for her to keep it wrapped around herself after going over her belly."
    "Embarrassed even further, she had to redo her attempt to cover herself, this time only around her hips, which easily stayed in place with the weight of her belly pressing down on the towel as she wore it."
    BBW "Hmph, so difficult to find quality materials. I expected this swimsuit to hold up for much longer than just one summer vacation. How disappointing."
    MCT "Well at least Alice was able to save face by blaming the swimsuit for being substandard quality."
    show BBW swimsuit-worried
    BBW "*{i}Sigh{/i}... Thank you Aida."
    BBW "Perhaps I didn't reapply sunscreen enough today. All the more reason for us to head inside after a long day."
    show PRG swimsuit-neutral
    "Alice's frustration quickly turned into dejection once she realized she couldn't even hide her own embarrassment anymore. I felt sad and frustrated for her."
    "She came to her family's vacation home to get away for awhile and take her mind off of the effects of her growth."
    "Getting to swim with me and Aida today seemed to have taken her mind off of it, only for this wardrobe fiasco to negate all of that by reminding her how fat she was getting."
    "I didn't think I had anything to say that could take the sting of that realization away, so I tried to change the subject."
    MC "Alice, thanks for everything today. It was really fun."
    show PRG swimsuit-happy
    PRG "Yes, I agree. Thank you Alice! The food was great as well."
    MC "That too. I was blown away by the food."
    BBW "I'm glad you two enjoyed it. I had fun too... {size=-6}for the most part.{/size}. Right now, I'm looking forward to cleaning off with a warm shower. Let's head inside."
    "It was an unfortunately dour note to end on what had been an otherwise great day. I wondered if I could have better preserved Alice's feelings if I would have distracted Aida from noticing she had torn her swimsuit."
    jump daymenu

label BBW049C_c2:
    show PRG swimsuit-worried
    PRG "Is everything alright? You both look like something is wrong. Did you lose something in the water?"
    "I continued to run my beach towel through my hair as I took a couple of steps towards Aida, blocking her line of sight to Alice."
    MC "Oh, uh. It's nothing. I thought I lost my... uh, sandal. But I found it."
    PRG "I didn't think you wore any sandals today, Hotsure-san."
    "Damn! She noticed. Apparently, I needed a more elaborate deception than a simple distraction."
    MC "Exactly! I forgot to bring it entirely! So therefore, it must still be in my guestroom. Nothing to worry about!"
    show BBW swimsuit-neutral
    "Looking back out of the corner of my eye, I could see Alice took the time afforded by my ruse to cover her bottom half with her beach towel, leaving Aida none the wiser."
    show PRG swimsuit-neutral
    PRG "Oh good!"
    BBW "Yes, quite the relief, though it is rather careless to forget something like that in the first place, Keisuke."
    MC "Heh, yeah that's true."
    BBW "Aida I'm sure you must be tired. Don't let us detain you if you would like to lie down for a while before dinner this evening."
    PRG "Yeah, I think I will. I am a little tired. Thanks Alice."
    "After watching Aida walk back towards the beach house Alice turned to me."
    hide PRG with dissolve
    BBW "That was very chivalrous of you to act in order to preserve a lady's honor."
    "At this point I started to blush. Aida may have been oblivious to my act, but Alice was keen to what I had been up to."
    MC "I... I don't know what you mean. I guess I looked panicked for a second when I thought I lost a pair of sandals in the ocean. You know how concerned Aida is about that kind of stuff."
    show BBW swimsuit-happy at Position(xalign=0.5, yalign=1.0) with dissolve
    "Me playing dumb about the whole ordeal brought a coy smile to Alice's face."
    $setAffection("BBW", 1)
    BBW "Sure, Keisuke."
    BBW "Thanks for a lovely day today. I had fun."
    MC "I should be saying that to you, since you're the host. This whole vacation has been amazing."
    BBW "I'm glad you're enjoying yourself. I did have one question for you though."
    MC "What was that?"
    show BBW swimsuit-aroused
    "Alice's voice changed to a sultry tone as she sashayed her hips when she asked the question."
    BBW "Did you get a good look?"
    "I didn't really know what to say, but the heat I felt on my cheeks at that moment was more than just the summer air."
    BBW "Hmm, that's what I thought."
    BBW "Keisuke dear, next time do remember to reapply sunscreen. Your face appears to have gotten sunburnt. {i}*Wink!*{/i}"
    jump daymenu

label BBW050:
    $setProgress("BBW", "BBW051")
    scene Summer Guest Bedroom with fade
    play music Peaceful
    "The early morning sunlight crept through my window, illuminating my room as I checked and rechecked my bags."
    "It was the day of our departure from this summer home. And even though the time here felt short, it felt like Alice and I had grown closer."
    MCT "Now if only I could remember where I left my brush..."
    "Despite my vicious upturning of the room, the brush was nowhere to be found. My mind traced back, trying to remember where I might have left it."
    play sound Knock
    "{i}Knock Knock{/i}"
    Lee "Mornin' Mr. Kei!"
    "Lee opened the door before I even had a chance to answer his knock."
    Lee "So, today's the day you're leavin' huh?"
    MC "Unfortunately, yeah. If I had the option, I'd rather stay here than go back to school."
    Lee "Can't say I blame ya..."
    Lee "Wait, why did I come here again?"
    "Lee turned his head down, deep in thought about why he had barged in my room."
    MC "Um..."
    Lee "Hang on, hang on- it'll come to me."
    Lee "AH-HA, right!"
    "Lee clapped his hands together enthusiastically, like he had just solved a difficult math problem."
    Lee "Miss Alice says you should be out and packed within the hour!"
    MC "Yeah, I should've been down there already, but I can't find something important."
    Lee "Ah, sorry to hear that, Mr. Kei. I'll make sure to double check the entire house for you!"
    "Before even finishing that thought, Lee was out the door and speed-walking down the hall."
    MCT "...I didn't even get to tell him what to look for."
    "With a resigned sigh, I grabbed my bags and headed out. Maybe I would get lucky and he would find my brush."
    "Under all the covers, and between each cushion I checked, yet it was nowhere to be found."
    scene Summer Balcony Exterior with fade
    "With a defeated sigh, I trudged over to the balcony. Alice was right though, the sunrise on this balcony is something to behold."
    "It was at that moment I felt something soft press into my back. No, not just soft, but warm as well. In fact I'm pretty sure I know what's behind me."
    show BBW summer-int-sg-neutral with dissolve
    BBW "If you are hoping, perchance, to find your brush fallen off the balcony... I am sorry to say that you will not find it there."
    "Turning around, I greeted Alice with a beaming smile. Just seeing her so relaxed put my stressed mind at ease."
    BBW "Here, you left it on the beach."
    MC "My brush! How did you find it?"
    BBW "The better question is how did you manage to lose it? It very clearly stands out in the sand."
    MC "I guess my mind was focused on... other things at the time."
    show BBW summer-int-sg-happy
    "Her calm smile quickly turned into a pleased smirk."
    BBW "If you continue to misplace this brush, I am going to have to make you wear it like a necklace."
    show BBW summer-int-sg-neutral
    BBW "That way I won't have to worry about retrieving it for you anymore."
    MC "H-Hey, let's not be too hasty."
    show BBW summer-int-sg-neutral-2
    BBW "I am just simply teasing you, Keisuke."
    MC "Oh, right. You had me going for a second there."
    show BBW summer-int-sg-neutral
    BBW "I'm going to miss seeing the sunrise..."
    "Alice shifted her head to look over the balcony. Her eyes sparkled as they caught the morning lights."
    MC "Me too, but hey there's always next year, yeah?"
    show BBW summer-int-sg-worried
    "Alice looked a bit worried at what I said. Her jovial demeanor sank away slowly."
    BBW "Right..."
    MC "...You're worried that your growth will prevent you from coming here again, aren't you?"
    show BBW summer-int-sg-surprised
    BBW "No! Not at all, not in the slightest."
    show BBW summer-int-sg-worried
    BBW "..."
    MC "Alice-"
    menu:
        "You know that we'll find a way to make it, no matter what.":
            jump BBW050_c1_1
        "Even if it's impossible to bring you to the beach- I'll bring the beach to you!":
            jump BBW050_c1_2

label BBW050_c1_1:
    $setAffection("BBW", 1)
    show BBW summer-int-sg-haughty
    BBW "You're right, where there is a will there's a way."
    jump BBW050_c1_after

label BBW050_c1_2:
    $setAffection("BBW", 3)
    show BBW summer-int-sg-happy
    "Alice couldn't help but giggle at my comment."
    BBW "Oh yeah? And how would you do that?"
    MC "I'm sure that excavators aren't that expensive, we can get loads of sand from here and bring it back!"
    "My tone of voice was clearly joking, but I couldn't help but get into it as Alice started to laugh."
    MC "And if we need to, we can just put some seawater in a water bottle. And boom, we have a beach at home."
    "Alice's worry was completely gone. Her spirits had been lifted by my rather absurd suggestion."
    BBW "To be honest, I'm already taking the best thing back with me."
    MC "Oh yeah, and what's that?"
    BBW "You, Keisuke..."
    "I couldn't help but furiously blush at her comment. Thankfully, without my brush, my bangs obscured my red face."
    jump BBW050_c1_after

label BBW050_c1_after:
    show BBW summer-int-sg-neutral
    BBW "We should probably check out with the butlers as well."
    MC "Good point."
    stop music
    scene Summer Living Room with fade
    play music BBW
    Lee "Mr. Kei, I couldn't find your brush anywhere!"
    show BBW summer-int-sg-neutral with dissolve
    BBW "Oh, speak of the devil."
    MC "Heh, don't worry, Alice found it for me."
    Lee "Oh really? Huh, and here I was thinkin' about just secretly buying you a new one!"
    Shino "You should know that Mr. Hotsure requires a specific brush. Standard commercial brushes will only get stuck."
    Lee "Ahhhh, right... but what if he used two normal brushes at once?"
    MC "Lee!"
    Lee "It's just a joke! Y'know?!"
    "Shino was staring daggers into Lee. Neither of them noticed Takada calmly approaching from behind."
    Takada "It is good to see everyone is in high spirits on the day of departure."
    Shino "I wouldn't say that exactly..."
    Shino "That reminds me, did you pack Mr. Hotsure's luggage like I told you?"
    Lee "I was gonna, but he already packed up himself."
    "Shino shot her gaze over to me, eyes stern with doubt."
    Shino "Is this true?"
    MC "Y-Yeah, I always pack my own bags."
    show BBW summer-int-sg-haughty
    BBW "Hmmph, you try to pack your own bags, but who helps you with space management?"
    MC "...I mostly pack my own bags."
    Takada "There is no need to be so strict today, Shino. The young miss and her companions are leaving soon."
    show BBW summer-int-sg-neutral-2
    BBW "That is correct, Takada. We simply wanted to thank you all for being here for us."
    Takada "I wouldn't miss it for the world."
    Shino "I'll always be by your side to help, miss Alice."
    Lee "Yeah! This was great fun!"
    "Takada chuckled as Shino continued to scowl."
    Takada "The transport is waiting for you, we will load your luggage onto it."
    scene Summer House Entrance with fade
    "After saying goodbyes, and making sure every bit of luggage was on board, we set off."
    stop music
    scene RV Interior with fade
    play music Peaceful
    "Looking out the window, I saw the servants slowly shrink into the distance. The home disappearing from sight not long after them."
    show BBW summer-int-sg-happy with dissolve
    BBW "Keisuke, thank you."
    MC "Huh, for what?"
    BBW "For accepting my invitation to accompany me. This quite possibly... no, this vacation was the most enjoyable one I've had at the beach home."
    MC "Ah, c'mon. I really couldn't have added that much."
    show BBW summer-int-sg-neutral-2
    BBW "You needn't be so modest, my mind wasn't set on going for the longest time."
    BBW "If you hadn't accepted my offer, my plans for the summer should have been drastically different."
    MC "You didn't really expect me to turn down an offer like this, right?!"
    show BBW summer-int-sg-neutral
    BBW "No no, the idea of you denying my offer was an impossibility."
    show BBW summer-int-sg-sad
    BBW "But due to my mother and father being unable to attend this year, my heart refused to even go."
    show BBW summer-int-sg-happy
    BBW "But once I came to the conclusion that you could join me, it felt like a weight had been lifted."
    BBW "So... Thank you, is all I want to say."
    "Alice blushed slightly, her smile sincere."
    show BBW summer-int-sg-haughty
    BBW "It's a long way back to the campus, and my time was spent preparing to leave this morning."
    BBW "I am going to rest for the rest of the return trip, and I recommend that you do the same."
    show BBW summer-int-sg-neutral
    "The rest of the trip back was calm, Alice quietly resting as my own eyelids grew heavy."
    "Even though I know that the only thing waiting for me is more school work, the fact that I'll still have Alice by my side, makes everything seem like it'll turn out fine."
    jump daymenu

label BBW051:
    scene Dorm Interior with fade
    $setSize(4)
    $setTimeFlag("size4")
    $setProgress("BBW", "BBW052")
    "I have the tickets in hand when my phone buzzes from a text. It's from Alice."
    BBWCell "Head over when you are presentable, I'm ready."
    "I check myself over again since I'm dressing far more formally than I have on any of our previous dates. Straightening my tie, I head towards her dorm."
    $setTime(TimeEnum.EVE)

    scene Dorm PRG with fade
    "Aida greets me at the door, as I walk in I observe she's busy cooking. The aroma of meat wafts out filling my nose. If I didn't already have plans I might've stayed to have a taste."
    show PRG neutral with dissolve
    PRG "Oh, good evening, Hotsure-san!  I'm assuming you're here for Alice?  She mentioned that you and her had plans for tonight."
    MC "Has she told you anything about what the plans are?"
    PRG "She said there wasn't much to tell.  She mentioned that you were really vague in your description."
    MC "All I told her was I wanted to treat her to something she enjoys."
    show PRG happy
    PRG "In that case, I'm sure she'll love it."
    "As Aida returns to her cooking I approach Alice's room where I can hear the sound of music leaking through"

    scene black with fade
    #-Sound of knocking-
    BBW "Come in."

    scene Dorm BBW with fade
    "Closing the door behind me I notice Alice standing in front of her makeup mirror putting on lipstick. Standing in front of me is Alice, wrapped in a floor-length dress. Out of all her outfits so far, this one was by far the one I think I liked the most."
    show BBW dress-neutral with dissolve
    BBW "Do you recognize the piece playing Kei?"
    if getSkill("Art") > 4:
         MC "It's Beethoven's Moonlight Sonata. At least one section of it, correct?"
         show BBW dress-happy
         BBW "It is indeed, it's good to see the classics are still appreciated."
         MC "It's a piece that I'm sure many recognize but few know the name of, most classical pieces are that way."

    else:
        MC "Sounds like a normal classical piece of music."
        show BBW dress-angry
        BBW "I do hope it would be a bit more than a normal classical piece, seeing as it's rather famous."
        MC "Sorry, suppose it just didn't ring any bells for me. It's not exactly within my avenue of musical interest."
    show BBW dress-neutral
    BBW "It's a wonderful song regardless, that deserves its own recognition. Though you aren't here to discuss my music choices are you. You've been rather vague with me on exactly what you are planning with me tonight. Care to layout your grand scheme?"
    menu:
        "Tell her the true plans":
            jump BBW051_c1_1
        "Tell her to wait":
            jump BBW051_c1_2
        "Tell her false plans":
            jump BBW051_c1_3

label BBW051_c1_1:
    MC "Well I guessed that since we've done restaurants for the last few dates, a change of pace would be nice."
    show BBW dress-happy
    BBW "Oh? Is that your plan mister?"
    MC "It's much more impressive once we get to the theater."
    $setAffection("BBW", 1)
    show BBW dress-surprised
    BBW "The theater, oh that's a very nice idea."
    show BBW dress-happy
    BBW "I look forward to seeing what show you've decided would pique my interest."
    "To be honest I hadn't considered whether she'd ever seen this show before."
    MC "Well we'd better get going to make sure we can find our seats without much trouble."
    "Alice gives me a smile that seemed to convey a sense of approval that I'd seen before, but this felt to be from a more genuine and heartfelt spot."

    scene Theater Exterior with fade
    "The theater was rather packed tonight, which wasn't unexpected since the show was a rather popular pick."
    show BBW dress-happy with dissolve
    "Seeing Alice in her dress was something I didn't know I needed, but seeing her now I'm not sure how I never imagined it before. Compared to her previous dress, this one stirred me in a new way I didn't know was possible."
    "Where her previous dress had been quite..."
    show BBW dress-neutral
    BBW "Kei, the man at the ticket booth is calling you."
    MC "Oh, I guess I zoned out there."
    "I give the man our tickets and mention that I'd called ahead for accommodations. He nods and assures me that our accommodations have been met before waving us in."
    jump BBW051_c1_after

label BBW051_c1_2:
    MC "I hate to spoil surprises, it ruins all the fun and anticipation."
    show BBW dress-haughty
    BBW "Then I guess I'll have to wait, which I normally hate to do. Though I think I'll make an exception this time."
    "She gives me a smirk as we exit from the room."

    scene Theater Exterior with fade
    show BBW dress-surprised with dissolve
    BBW "Oh my! I was certainly not expecting this to be in consideration!"
    MC "Oh and why so?"
    show BBW dress-sad
    BBW "It's been a rather long time since I've been to an opera or play. I was beginning to think I'd never be able to go back due to, well, everything so far."
    MC "Don't worry I've been careful this time to account for everything."
    show BBW dress-haughty
    BBW "Is that so?"
    MC "I've got this date handled so relax tonight."
    show BBW dress-neutral
    BBW "If you say so Mr. In Charge."
    "I step over and hand our tickets to the usher and inform him of my earlier call for accommodations. He assures me that my request has been properly handled and gestures for us to enter."
    jump BBW051_c1_after

label BBW051_c1_3:
    $setFlag("BBW051_c1_3")
    MC "There is a new seafood restaurant that recently opened in town, they have a dress code that's why I asked that you get dressed up for this occasion."
    $setAffection("BBW", -1)
    show BBW dress-sad
    BBW "Oh, that's very nice."
    MC "Is there a problem with that plan?"
    BBW "Well I was hoping we could maybe do something besides food, but I suppose if the reservations are made we shouldn't disappoint."
    "I feel bad for lying about something so simple but my certainty on what she wants is still rather blurry. So playing it safe this time might've been a bad call."

    scene Theater Interior with fade
    show BBW dress-surprised with dissolve
    BBW "Wait, is this where we were actually going?"
    MC "Yeah, I wanted to surprise you."
    show BBW dress-angry
    BBW "Why would you lie about something so important to our plans?"
    MC "Well this was supposed to be a surprise after all so I wanted to keep up the illusion till we got here."
    BBW "That's still a stupid reason. Did you assume I wouldn't enjoy anything that didn't involve food?"
    MC "No, not at all. I just used the restaurant excuse since our last couple of dates have been to restaurants."
    BBW "You should've just surprised me back at the dorm. I was expecting us to be doing something else till you said we were doing a dinner date again."
    MC "I'm sorry, I didn't know that was your expectation going into this."
    BBW "It wasn't just that Kei, I had fears you might be seeing me as this gluttonous person that was losing control. That's why I was a little disappointed when you said we were doing another restaurant."
    MC "I'd never think that about you! You are far more than something so shallow."
    show BBW dress-sad
    BBW "That's not how it came off, so much has been happening recently that just having that idea seemingly confirmed, struck a little too deep to be comfortable."
    MC "Well as I've said time and time before, that is not how I see you at all. I probably can't understand everything you've been feeling recently but I'm still here regardless of your size."
    if getAffection("BBW") >= 25:
        show BBW dress-haughty
        BBW "If you truly mean that, then that's what I will expect from now on."
        MC "You have my word, Alice."
        "I step over and hand our tickets to the usher and inform him of my earlier call for accommodations. He assures me that my request has been properly handled and gestures for us to enter."

        scene Theater Interior with fade
        show BBW dress-neutral with dissolve
        BBW "So what was the talk with the usher about?"
        MC "I had a feeling that certain features might not properly cooperate with your current size. So I went ahead and called ahead to see what accommodations could be made."
        show BBW dress-haughty
        BBW "What kind of accommodations do you mean?"
        MC "Making sure we have seats that fit each of our figures."
        show BBW dress-surprised
        BBW "Oh, you went ahead and looked into something like that for us?"
        MC "Of course, I care for your comfort, so naturally I wanted to make sure you could enjoy this night without concerning yourself with those sorts of things."
        $setAffection("BBW", 1)
        show BBW dress-happy
        BBW "You always find a way to impress me, Kei."
        MC "And I'll never stop trying."
        "As we enter the theater hall I spot a large couch near the front. Pointing it out to Alice I could tell she was happy to see my efforts had worked. She looks over the couch for a moment with a certain level of prudence before gently seating herself. Her cheeks flush red as the couch gives a small groan as she eases herself down."
        MC "Everything okay for you?"
        show BBW dress-neutral
        BBW "Yeah that was just surprising, that's all."
        MC "Just making sure everything was to your satisfaction."
        "Alice gives me a smile as the lights soon dim, the red curtains of the stage ascend and an organ roars to life with a deep bellowing sound."
        jump BBW051_c2_after
    else:
        MC "Also everyone needs to eat so it shouldn't be taken as an insult. It's just a fact of life."
        pause 2
        BBW "Fine, I suppose I may have been a bit harsh, I guess this stuff has been getting to me a bit."
        MC "You still want to continue tonight?"
        show BBW dress-neutral
        BBW "Well I'd hate for all our efforts to go to waste tonight. So we may as well enjoy the show."
        MCT "Well this certainly was not how I imagined this night going at all."
        "I gave our tickets to the man at the ticket booth and mentioned that I had called ahead for accommodations. He nods and says they've fulfilled the request."

        scene Theater Interior with fade
        show BBW dress-neutral with dissolve
        "As we enter we can both see the large couch like chair in the front row. As we approach I notice Alice giving me a glance with a slight smirk on her lips. She looks over the couch for a moment with a certain level of prudence before gently seating herself. Her cheeks flush red as the couch gives a small groan as she eases herself down."
        MCT "That was kinda hot, but I better not approach that subject tonight."
        "We both remain silent as the lights dim, the red curtains of the stage ascend and an organ roars to life with a deep bellowing sound."
        jump BBW051_c2_after

label BBW051_c1_after:
    scene Theater Interior with fade
    show BBW dress-neutral with dissolve
    BBW "So what was the talk with the usher about?"
    MC "I had a feeling that you might not be able to use their normal seating, so I called ahead to see what they could accommodate."
    show BBW dress-sad
    BBW "Oh. It sounds like a lot of effort to go through just for me."
    MC "Well you shouldn't have to miss out on the things you enjoy. Adapt maybe, but not abandon them."
    BBW "I suppose, but that still doesn't change the fact I'm far larger than most."
    MC "That doesn't change who you are underneath. You are still the confident girl I met all those months ago."
    show BBW dress-haughty
    BBW "I wonder when you picked up such a silver tongue? Though I doubt that the effort of guessing as to such would prove pointless."
    "We shared a laugh, causing her body to bounce and roll in a rather satisfying way as we made our way to our seats. As we enter the hall I spot a large looking couch near the front. Pointing it out to Alice, I could tell she was happy to see what my effort was towards."
    MC "So is this good enough my dear?"
    show BBW dress-neutral
    BBW "You've certainly gone beyond what I could ask of you."
    MC "It was nothing, you deserve to be treated well."
    show BBW dress-haughty
    BBW "Certainly are proving to be quite the gentlemen aren't we?"
    "Alice looks over the couch with a certain level of prudence before gently seating herself. Her cheeks flushing red as the couch gives a small groan as she eases herself down."
    menu:
        "Ask her about the reaction.":
            jump BBW051_c2_1
        "Leave it alone.":
            jump BBW051_c2_2

label BBW051_c2_1:
    $setFlag("BBW051_c2_1")
    MC "You ok?"
    show BBW dress-sad
    BBW "Lately my experiences with furniture have been... inconsistent, to put it lightly. Waking up with a few broken bed slats doesn't make for a pleasant morning."
    "She broke her bed, now that I would've loved to see happen. It was one thing to imagine it, but knowing it came true is another."
    MC "Is that why you were very surprised by me deciding on this?"
    BBW "Honestly, yes. Even as much as I accept my size, there's always uncertainty when using furniture that isn't my own. I have no prior warning if it can hold me or I'll be sent falling to the floor in a minute."
    MC "I'm sure I can probably help in that matter. An extra pair of eyes never hurts to have around. Not to mention an extra pair of hands to catch you if you fall."
    show BBW dress-haughty
    BBW "Well I hope you intend to keep that promise because I'm certain my future at school will involve more than a few splintered chairs."
    "Now that's something I will certainly have to see."
    "The lights soon dim, the red curtains of the stage ascend and an organ roars to life with a deep bellowing sound. Taking my seat next to Alice, I soon feel her hand grip mine as the first scene begins."
    jump BBW051_c2_after

label BBW051_c2_2:
    "She's probably embarrassed I had to hear that so I'd better not push it."
    "The lights soon dim, the red curtains of the stage ascend and an organ roars to life with a deep bellowing sound."
    jump BBW051_c2_after

label BBW051_c2_after:
    scene black with fade
    pause 1
    scene Theater Interior with fade
    "The play stops to allow everyone a brief intermission to use the restroom. Alice and I stand up from our seats to stretch out our stiff legs. We eventually wander over to a balcony overlooking the entrance."
    MC "Have to say that mask-wearing guy, he is one strange dude."
    show BBW dress-happy with dissolve
    BBW "That is the point Kei, he's meant to be off-putting and slightly standoffish. He's a character we have to warm up to and gain empathy for."
    MC "Have you seen this play before?"
    BBW "I did a while back with my parents. We visited some of my mother's family and my father got us tickets for the performance happening on Broadway. It was one of the first shows I saw, so seeing it again is very nice."
    MC "Glad you enjoy it, I had a feeling you might enjoy since I remembered you mentioning a fondness for Opera and singing."
    show BBW dress-neutral
    BBW "Do you remember back when we first started here, I wanted to lead the music club?"
    menu:
        "Of course, I remember you mentioned wanting to be a seated soprano.":
            jump BBW051_c3_1
        "How could I forget, you did make quite a scene.":
            jump BBW051_c3_2
        "Vaguely. It was quite some time ago.":
            jump BBW051_c3_3

label BBW051_c3_1:
    show BBW dress-happy
    BBW "I did, and well I still do, that's why I've been very critical about the matter. Though I suppose now in hindsight I may have been a tad overbearing."
    MC "I think you just matured and dropped some of the brashness you had when you first arrived."
    show BBW dress-neutral
    BBW "Perhaps, though despite my squabbles with the club president I still plan to see myself in a leading position in the club."
    BBW "That is a dream I plan to fulfill, regardless of whatever obstacles may lie ahead of me."
    MC "That does mean you need to have good relationships with your other club members, including Mizawa-san."
    BBW "I'm aware and I'm already working on plans to improve my standings among them. Like you said, patience is valuable in this matter and that is what my plan hinges on."
    "Well she has certainly matured on this front, I hope that she's able to continue without falling back to her old habits."
    "I notice the flow of people heading back into the theater and extend my hand out"
    MC "It would appear it's time to retake our seats. Shall we?"
    show BBW dress-haughty
    BBW "Indeed we shall."

    scene black with fade
    jump BBW051_c3_after

label BBW051_c3_2:
    show BBW dress-angry
    BBW "I had hoped you might have overlooked that low point in my career."
    MC "Sorry for bringing that detail back up."
    show BBW dress-neutral
    BBW "Regardless of how you remember that event, you can't deny I wasn't passionate."
    MC "I doubt a case disproving that idea could exist."
    BBW "It's that exact passion for singing that helps me stay in the music club. Seeing these beautiful plays helps remind me why I remain loyal to that idea."
    MC "Don't you need the help of the other club members as well?"
    show BBW dress-haughty
    BBW "I have a plan for helping me return to their good graces."
    "I consider asking further but decide against it knowing she won't explain her grand plan."
    "Besides people are beginning to return to their seats so we should as well."
    "I offer her my hand but she instead walks ahead. This date is not going as well as I hoped."
    scene black with fade
    jump BBW051_c3_after

label BBW051_c3_3:
    show BBW dress-neutral
    BBW "The details aren't important to the matter I'm addressing, what is important is that I wanted to be a part of that club a lot."
    BBW "The passion I have for music helps me stay in the club. Seeing these beautiful plays helps remind me why I need to continue to commit to that idea. I want to prove that I'm as good as I say I am."
    MC "That's an impressive amount of dedication but won't you need the help of the other club members?"
    show BBW dress-haughty
    BBW "I have a plan for helping me return to their good grace."
    "I consider asking further but decide against it knowing she won't explain her grand plan."
    "Besides people are beginning to return to their seats so we should as well."
    "I offer her my hand but she instead walks ahead. This date is not going as well as I hoped."
    scene black with fade
    jump BBW051_c3_after

label BBW051_c3_after:
    if getFlag("BBW051_c1_3"):
        "The play stops to allow everyone a brief intermission to get snacks and use the restroom. Alice and I stand up from our seats to stretch out our stiff legs."
        MCT "I should probably keep quiet for now, I've already done enough damage tonight. Hopefully, I can still salvage this night and my relationship with Alice by doing so."
        "A couple times Alice opens her mouth seemingly to try and say something, but closes it quickly."
        show BBW dress-neutral with dissolve
        BBW "I'm gonna grab myself a snack from downstairs, I'll back before we reseat."
        "I watch her disappear down the stairwell before returning to my thoughts."
        "After a couple minutes we begin retaking our seats. Alice soon returns with a small bag of popcorn as the curtains open again to continue the show."
        scene black with fade
    if getFlag("BBW051_c2_1"):
        $setTime(TimeEnum.NIGHTLIGHTS)
        scene Town with fade
        "By the time the play finished, the sun had already set behind the horizon. The final bus back to the academy had already departed, thus leaving Alice and I to walk back."
        scene BBW dress-sad with dissolve
        BBW "Hey Kei, I want to thank you for tonight."
        MC "Oh it's no problem, I'm glad you've enjoyed yourself."
        BBW "Well it's more than just that. This was the first time I saw how my new size is to others."
        BBW "As I said back in the theater, my experience with furniture lately has been quite varied. So trusting you to have made the right seating arrangements, made me feel, well helpless. This growth I feel has finally gotten beyond a manageable point."
        MC "Oh I didn't realize you felt that way. I was just doing what I believed would make you feel appreciated and cared for. Are you mad at me?"
        show BBW dress-neutral
        BBW "No, this is a confrontation I've been avoiding for a while now."
        MC "Is there some way I can help?"
        BBW "Well that there is something I've wanted to ask you about. As you know Aida is in no shape to be assisting me full time. I highly doubt I'm done growing but things are already becoming more difficult."
        BBW "Even small tasks have an added challenge to them nowadays. I can't imagine trying to accomplish them at a larger size without some help."
        show BBW dress-haughty
        BBW "I have taken for granted my family's servants and Aida, but it is becoming clear that assistance will become not just a convenience for me but a necessity."
        BBW "The thought of being dependent like that troubles me, more so the fear that I would become a burden. Directly, I'm saying if we were to become serious about this relationship I would need you there for me."
        MC "Of course, I'll help you if you need it. I am your boyfriend after all."
        "She smiles and we hold hands all the way back to the school. Letting the music of the night close out our date."
    jump daymenu

label BBW052:
    $setProgress("BBW", "BBW053")
    scene Cafeteria with fade
    play music HigherEdu
    MCT "After sitting through half a day's worth of lectures my stomach was killing me for some food. With a full tray I quickly scanned out Alice among the crowd."
    MCT "The scene gave me a brief sense of déjà vu as it clicked that everyone now looked quite different from when the semester began."
    MCT "Though even with everyone changing in different ways, one fact remained consistent: Alice's ability to make herself pronounced."
    MCT "Whether it be her voice, her hair or the more obvious, her factor, she made sure to stick out. "
    show BBW neutral with dissolve
    BBW "Good afternoon Keisuke, I take it your morning classes went well."
    MC "They went as slow as possible but they were bearable."
    BBW "That's good to hear, I just wanted to make sure you are feeling well and actually paying attention in class. Last thing you need is to miss anything."
    MC "I've been getting to bed earlier than normal, so sleeping during class hasn't been as much of a problem as it was earlier."
    BBW "That's good to hear, good sleep is a rare commodity."
    MCT "As I began eating my food, I noticed that Alice seemed to be dancing her fork around her plate."
    menu:
            "Say something":
                jump BBW052_c1_1
            "Continue eating":
                jump BBW052_c1_2

label BBW052_c1_1:
    $setFlag("BBW052_c1_1")
    MC "Everything alright there Alice? Is something on your mind?"
    show BBW worried
    BBW "No, the food today tastes underwhelming, as per usual. I also had a large breakfast and am still quite full from that meal."
    MC "Did you get the fried rice? It's amazing, especially with some soy sauce."
    BBW "I didn't but it's a little late to grab some anyway."
    show BBW neutral-2
    BBW "Though that does remind me, would you want to do something this evening?"
    MC "I thought I was supposed to be the one asking you on dates?"
    show BBW neutral
    BBW "It would be more gentlemanly of you, but considering the lengths you went through last night for me, I feel it necessary to return the courtesy."
    MC "You don't need to repay me for treating you like my girlfriend. I wanted to spoil you and that doesn't require you to do anything back."
    show BBW doubt
    BBW "I hate that term, spoil, makes me sound like princess."
    show BBW neutral-2
    BBW "Anyway, I get your concern Keisuke, but let me do this for you. It will make me happy."
    MCT "Weird how she worded it like that."
    MC "Alright what time tonight?"
    BBW "5 pm should do fine. Do dress nicely as we will be heading into town."
    MC "Then it's a date."
    hide BBW with dissolve
    MCT "As the words left my mouth the bell rang again. Gathering my garbage I noticed Alice hastily toss her leftovers out. Her tray still had a fair amount of food on it. Something had happened since the lake house- her appetite wasn't adding up."
    stop music
    scene black with fade
    jump BBW052_c1_after

label BBW052_c1_2:
    MCT "I decided not to push, feeling that if it was something truly important she'd tell me when she was comfortable."
    BBW "Oh Kei, I wanted to ask, would you want to do something this evening?"
    MC "I thought I was supposed to be the one asking you on dates?"
    show BBW neutral
    BBW "It would be more gentlemanly of you, but considering the lengths you went through last night for me, I feel it necessary to return the courtesy."
    MC "You don't need to repay me for treating you like my girlfriend. I wanted to spoil you and that doesn't require you to do anything back."
    show BBW doubt
    BBW "I hate that term, spoil, makes me sound like princess."
    show BBW neutral-2
    BBW "Anyway, I get your concern Keisuke but let me do this for you. It will make me happy."
    MCT "Weird how she worded it like that."
    MC "Alright what time tonight?"
    BBW "5 pm should do fine. Do dress nicely as we will be heading into town"
    MC "Then it's a date."
    hide BBW with dissolve
    MCT "As the words left my mouth the bell rang again. Gathering my garbage I noticed Alice hastily toss her leftovers out."
    MCT "Her tray still had a fair amount of food on it. Something had happened since the lake house- her appetite wasn't adding up."
    stop music
    scene black with fade
    jump BBW052_c1_after

label BBW052_c1_after:
    $setTime(TimeEnum.EVE)
    scene School Front with fade
    play music Peaceful
    MCT "Double checking my watch to confirm my timeliness,  I was happy to spot Alice sitting at the bus stop bench."
    show BBW neutral with dissolve
    BBW "Glad to see your punctuality continues to be great."
    MC "I wouldn't say that in all cases but I hate leaving a lady by herself."
    BBW "You need not worry about me, I can handle myself just fine. Though the thought is appreciated, Keisuke."
    MCT "With a rumble the bus pulled up, displaying the town as its next destination."
    MCT "It was hard to miss Alice giving the bus doors a size up before stepping on board."
    MCT "With a bit of trepidation she stepped on. Her broad hips brushing against the larger than average bus doors."
    MCT "Alice found us a pair of seats near the back and gestured for me to take the seat next to her. Sliding in beside her was a bit awkward cause I don't think she noticed how much of her thigh was pressing against my leg."
    MCT "Despite the minor discomfort in positioning I was not gonna complain about being beside her."
    scene black with fade
    MCT "It didn't take too long to arrive at our destination."
    scene Town with fade
    show BBW neutral with dissolve
    MCT "Once off the bus she directed me towards a shop I hadn't noticed before. The sign read 'Cold as Ice' leaving me a bit confused as to what this place could be serving."
    BBW "Have you ever tried rolled ice cream?"
    MC "Can't say I have. I thought ice cream was already rolled when they serve the scoops."
    show BBW happy
    BBW "Not like that! No, this is something very different, but I appreciate the humor."
    show BBW neutral
    BBW "Though I think seeing the process will do it more justice than I could trying to explain it."
    MC "This must be interesting then if you will let it speak for itself."
    MCT "I didn't need to be facing Alice to hear her rolling her eyes at my comment."
    scene Restaurant with fade
    MCT "Stepping in, the first thing I noticed was the lack of giant ice cream tubs. There also appeared to be some grills where they would have normally been."
    MC "You sure this is an ice cream place? It looks more like a barbeque place."
    show BBW haughty with dissolve
    BBW "Have faith Kei, this will be well worth the confusion."
    MCT "She gave her order to the cashier, a simple strawberry cheesecake. With a nod the cashier pours what I assume was cream onto the flat griddle."
    MCT "Disappearing under the counter, he produces a slice of cheesecake which he drops on the cream spot. With a pair of cutters he very rapidly diced the cake."
    MCT "He then smoothed it out till it was flat. Delicately, he then scraped it into small rolls."
    show BBW happy
    BBW "I hope that satisfied your curiosity."
    MC "That is certainly the most aggressive and unique way I've seen someone make ice cream."
    BBW "Go ahead and order one for yourself. I already paid for a second."
    hide BBW with dissolve
    MCT "I gave the man an order for a cookies and cream which he produced in a similar fashion to Alice's."
    MCT "With ice cream in hand, I joined Alice at the table she'd grabbed us."
    MC "Thank you for this, it looks really good."
    show BBW happy with dissolve
    BBW "Your welcome, it was the least I could do to repay you."
    MCT "As we ate I noticed her picking at the ice cream, only taking small chunks at a time."
    menu:
        "Ask":
            jump BBW052_c2_1
        "Leave her be":
            jump BBW052_c2_2

label BBW052_c2_1:
    $setFlag("BBW052_c2_1")
    MC "Your meal is melting away."
    show BBW worried
    BBW "Oh, apologies. I wasn't expecting it to be so rich. When I previously visited, I ordered a simple strawberry flavor which was not so sweet. Them using a whole slice of cake was a bit surprising to be honest."
    MC "Yeah that was a bit surprising for me as well. Made me scared how many oreos they were gonna use for my order."
    show BBW neutral
    BBW "Lucky for you they didn't go quite so overboard."
    MC "It's appreciated."
    MCT "It was clear that she wasn't gonna open up on the actual issue. I knew I was treading on something as thin as my ice cream but maybe if I played my cards right she might open up."
    jump BBW052_c2_after

label BBW052_c2_2:
    MCT "I decided to not push her on the matter while we were sharing a nice moment together"
    MC "Boy this stuff is good, how did you find out about this place?"
    show BBW neutral
    BBW "Oh Aida and I needed to head to town to get her some things. She suggested we try this place since it had recently opened."
    MC "That's good to hear."
    jump BBW052_c2_after

label BBW052_c2_after:
    scene black with fade
    $setTime(TimeEnum.NIGHTLIGHTS)
    scene School Front with fade
    MCT "Once we had finished we made our way back onto the bus to return to the school."
    MCT "While on the bus I swore I could've heard Alice's stomach growling, but dismissed it as just digestion. Though, part of me couldn't help but wonder if it was the hunch I'd been feeling all day."
    if getFlag("BBW052_c1_1") and getFlag("BBW052_c2_1"):
        jump BBW052_c3_pass
    else:
        jump BBW052_c3_fail

label BBW052_c3_pass:
    stop music
    play music Bittersweet
    MCT "Once off the bus I decided to try one last time at finding out the truth of the matter."
    MC "Alice I know I've bugged you all day, but what is going on with you? At lunch and tonight you seemed almost disgusted by your food. Are you feeling sick?"
    show BBW worried with dissolve
    BBW "Kei, if I told you something that was completely insane, you wouldn't walk away would you?"
    MC "Of course not, I'm here for you in all circumstances."
    BBW "I only ask cause the real reason is quite odd and rather embarrassing for me."
    MC "It would be unfair for me to pass judgement on you, especially since it seems to be bothering you this much."
    BBW "If that's true, then here's the reason. I've been having weird dreams, primarily ones focused on food. They vary wildly in terms of what happens, but food seems to be the one constant."
    MCT "I took a seat on a bench and gestured for her to join me."
    MC "I take it you've been paranoid about them being true."
    BBW "To an extent, yes. Now more than ever have I wanted my eating habits to not define me as a person."
    MC "I see. For the record, regardless of your habit it would not sway my feelings for you. How long have these dreams been happening?"
    BBW "Since we returned from the lakehouse, so approximately two weeks, almost three."
    MC "If it occurs tonight I'd suggest going to the school nurse. She's probably one of the few here that has any sort of idea about our factors, let alone this sort of specific thing."
    BBW "I suppose you are right in that regard, I'd considered going to her, but felt this was just a fluke. If it happens again I'll go there tomorrow before class."
    MC "Sounds like a good plan, if I do say so myself."
    show BBW neutral
    BBW "Don't go getting a big head over this, you already have enough hair on top of it to make it look inflated."
    MC "I meant to trim it earlier, but got busy with preparing for tonight."
    BBW "If it gets too unruly, I could probably try my hand at it. I've never done haircuts on men but your hair is closer to that of a woman that it should be comparable."
    MC "If my trimmers give out I'll take you up on that offer."
    BBW "It's getting late, so I think now we should begin parting ways. Have a goodnight Keisuke."
    MC "You as well Alice, sweet dreams, er... I mean, pleasant dreams."
    BBW "Charmer as always Keisuke."
    stop music
    scene black with fade
    $setTime(TimeEnum.DAY)
    scene Hallway with fade
    play music Hallway
    MCT "The morning classes had passed without event, but I had noticed Alice's absence. The interruption of her normal punctuality was enough to tell me she had had another dream, but checking first might be good."
    MCT "Heading towards the nurse office I noticed another familiar face."
    MC "Kodama-san!"
    show PRG neutral
    PRG "Hi, Hotsure-san. What brings you here?"
    MC "I came to check up on Alice."
    PRG "Oh, she left shortly after I got here. I'm guessing she went back to our dorm. I'm not sure what the nurse said to her, but she seemed really out of sorts."
    show PRG worried
    PRG "Truth be told, I'm a little nervous. T-That isn't like her."
    MC "I think I know, but I'd prefer to check before making assumptions."
    show PRG neutral
    PRG "That's probably for the best. Alice would most likely prefer to keep something like that quiet, anway."
    MC "Exactly my thinking. Thank you for the information, have a good day."
    PRG "You too."
    scene Dorm Exterior with fade
    MCT "Knocking on the door, I was relieved to feel the vibrations of someone approaching the door."
    show BBW happy with dissolve
    BBW "I take it you either encountered Aida or got curious that I wasn't in class."
    MC "A bit of both actually, how'd you guess I'd encounter Aida?"
    BBW "She'd be the only other one who might know where I am, so I guessed you'd seek her out."
    MC "Fair enough."
    BBW "Come in, you are probably curious about what the nurse said."
    scene Dorm BBW with fade
    show BBW neutral-2 with dissolve
    BBW "Now that we have a bit of privacy, let me explain."
    BBW "According to the nurse, my dreams are being caused because I'm not eating enough. Apparently this is a semi-common thing among those with weight gain factors if they limit their intake."
    MC "Well that's a relief that this isn't an isolated incident, but I have to ask why were you trying to limit your appetite?"
    show BBW worried
    BBW "That's a bit embarrassing I must confess. Since arriving here I could normally go two, almost three weeks, without a new uniform,"
    BBW "but since the lake house its shortened dramatically to nearly a week at max. I've been eating the same size meals as before but the urge to snack has certainly spiked."
    menu:
        "Be Understanding":
            jump BBW052_c4_1
        "Be Curious":
            jump BBW052_c4_2
        "Be Encouraging":
            jump BBW052_c4_3

label BBW052_c3_fail:
    MCT "I gave Alice a hand as she stepped off the bus as I had a feeling she may be unsure of her footing coming out."
    MC "Thanks again for tonight, I'd never guess you could make ice cream through brute force."
    show BBW neutral-2
    BBW "I wouldn't describe it that way, but I'm glad you enjoyed it as much as I did."
    BBW "It's late and I promised Aida I'd assist her in some matters, so I shall be saying goodnight here then."
    MC "Have a good night Alice."
    scene Hallway with fade
    MCT "The morning classes had passed without event, but I had noticed Alice's absence. The interruption of her normal punctuality was enough to tell me something was off."
    MCT "Not being sure I decided to head to lunch and see if she had popped up there."
    scene Cafeteria with fade
    MC "I ended up searching for a few minutes before my phone buzzed."
    BBWCell "<I wasn't feeling too great today so I visited the nurse and went back to my room.>"
    Cell "<Need me to bring you anything?>"
    BBWCell "<Not right now, I ate earlier and I have some orders to fill out. Though I may need some help tomorrow if you are available.>"
    Cell "<I certainly can be.>"
    BBWCell "<Thank you Kei, have a good day.>"
    MCT "Guess she must've just been feeling under the weather."
    jump daymenu

label BBW052_c4_1:
    MC "I can see how that sort of thing would kill an appetite. It would not be my first guess since you always appear so sure in your appearance."
    show BBW doubt
    BBW "Normally I am but some memories from earlier in the year got at me again recently."
    show BBW neutral-2
    BBW "Though our talks yesterday reminded me that such comments are only made by those looking to make themselves feel better."
    MC "They also might just be jealous of what they can't have."
    show BBW haughty
    BBW "Doubtful that's the case."
    MC "Just a fun thought to consider, be funnier if it was true."
    show BBW neutral-2
    BBW "I do appreciate it Keisuke, but the constant flattery isn't necessary. I prefer a man to show rather than tell me his affection for me."
    MC "Noted, guess I'll need to get more creative in my approach then."
    jump daymenu

label BBW052_c4_2:
    MC "Really? your previous size meals aren't cutting it anymore?"
    show BBW doubt
    BBW "It would appear not, which is quite ridiculous. I already look quite..."
    show BBW angry
    BBW "No, I won't bow to use that word."
    show BBW stern
    BBW "This whole matter is beyond ridiculous."
    MC "Well there's no use getting mad at what you can't control. It'll only make you more mad at it."
    BBW "I suppose you are correct in that matter. Being mad about it isn't gonna solve anything."
    BBW "*sigh*"
    show BBW neutral-2
    BBW "Thank you for tolerating my rant there. The clothes and dream stuff had really begun getting to me."
    BBW "This will sound rather funny, but can you grab me a granola bar from the kitchen? I'm feeling a bit peckish."
    $setAffection("BBW", 1)
    MC "I'd be foolish to disagree with the doctor's orders."
    jump daymenu

label BBW052_c4_3:
    $setFlag("BBW052_c4_3")
    MC "Are you afraid people will notice your clothes are slightly ill-fitting?"
    show BBW neutral
    BBW "Not really, I was just a bit self conscious of what they would say if I were to start acting more into their cliched image for me."
    MC "It's highly doubtful that they would pass such judgement on you now. At the beginning of the year things were far different than they are now. If anything, people now seem far kinder than before."
    BBW "I have noticed that as well. I suppose when everyone is in the same boat, they are less inclined to make such comments, as the same could be said about them."
    BBW "...."
    show BBW worried
    BBW "I know you mentioned earlier that your feelings wouldn't be swayed by my habits, would that still be true if I began eating more- possibly much more."
    MC "Not at all, if it would help I could be with you at all lunch times."
    show BBW haughty
    BBW "I wouldn't ask for something that extreme, but the eagerness is appreciated."
    "There was a brief silence before a low guttural growl echoed through the room."
    show BBW surprised
    BBW "Oh my."
    show BBW happy
    BBW "I suppose I should take the doctor's advice soon."
    MC "I would agree that would be a good thing to act on. Say, if you aren't busy, I believe the archery club was hosting a barbeque around lunch today. Interested in attending?"
    $setAffection("BBW", 1)
    BBW "It has been a while since I've had some good barbeque, sure."
    jump daymenu

label BBW053:
    "This marks the current end of Alice's route."
    "Her story will be continued in a later release. Until then, feel free to explore other routes."
    jump daymenu_noadvance

label BBWFMG001:
    scene Dorm Exterior with fade
    play music Busy
    MCT "Alice and I had planned to meet up later after class at her dorm. I started walking over a bit early so I wouldn't be late, knowing she'd expect punctuality given how tight she keeps her schedule."
    MCT "Alice said she had to hand off an order to a client after class, or else we would have just walked back to her place together. It was a nice day, so I took a leisurely stroll since I had some extra time."
    MCT "To my surprise I ran into a familiar face- just the person I was looking for."
    show BBW neutral with dissolve
    MCT "But I was unsure why she was meeting me here when she told me to meet her at her place."
    BBW "Keisuke, I'm glad I caught you on your way."
    BBW "I would have felt bad if I stood you up after telling you to come over, but I'm afraid this delivery drop off has taken much longer than initially anticipated. I could use your help."
    MC "Sure, what seems to be the problem?"
    show BBW neutral-2
    BBW "This order is a custom dress for Natsuko. The poor thing can't find anything decent that fits her proportions, I was happy to assist her."
    BBW "I told her it would be ready for her today and that I would give it to her. I thought I would simply run into her after class, but I haven't been able to find her anywhere."
    BBW "{i}Sigh{/i}... unfortunately this is what I get for being lax with scheduling a client."
    MC "So you can't find her anywhere you said?"
    BBW "Yes, I've looked all over and I can't think where she would be."
    MCT "I can't help but think she's overlooked some places."
    MC "Did you try the gym?"
    BBW "No. Why would anyone want to hang out at the gym after class?"
    MCT "Thought so- the gym is definitely not on Alice's radar. If it's not in the water, Alice isn't exactly keen on any physical exertion."
    MC "Yeah... beats me, but I'm sure I've seen her there pretty much every time I've gone. So, it's probably worth a shot, right?"
    show BBW neutral
    BBW "Hmm, well if that's the case it's probably worth checking out. I trust you won't mind making this delivery with me?"
    MC "Not at all. Here, I'll carry it."
    MCT "I took the box from Alice. It was pretty light, just some piece of clothing after all. Though, holding it in my hands, I did kind of wonder what was inside that was so special that Alice didn't mind delivering it herself."
    show BBW happy
    BBW "Such a gentleman."
    hide BBW with dissolve
    scene Auditorium with fade
    show Natsuko neutral at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    MCT "Walking into the gym we both spotted Natsuko almost immediately. With her tall stature and fiery red hair, she certainly stood out. She looked pre-occupied setting some things up for her workout."
    show BBW neutral-2 at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    BBW "There she is. This should be quick. I'll take it from here Keisuke."
    MCT "I handed off the box with Natsuko's clothes to Alice, assuring that it would be delivered by her personally, as per her promise to her client."
    BBW "There you are Natsuko. I had been looking all over for you to give you your order."
    Natsuko "Oh, sorry about that. If you have trouble finding me after class, I'm probably at the gym or at the track."
    show BBW neutral
    BBW "Well I suppose it's nice that at least someone is making use of these facilities. Anyway, here is your custom dress, per your measurements."
    Natsuko "Thank you Alice! It's pretty much impossible to find anything nice that flatters my figure these days."
    FMG "Now if only you could find something that flatters your personality."
    show FMG happy with dissolve
    Natsuko "Your attempts at humor are as miserably inept as your athletic prowess, Akira."
    show FMG neutral
    FMG "That must make me a comedian compared to you then. What do you even need a fancy dress for?"
    Natsuko "Unlike you, some of us do try to take care of our appearance. If that requires purchasing fitted clothing, then I'm willing to take the extra step. You wouldn't understand that kind of effort."
    show FMG angry-2
    FMG "I think what you really mean is you can't find anything that fits your goofy looking padded shoulders and that itty-bitty waist."
    Natsuko "At least I actually look like a woman. You on the other hand have the silhouette of a doorframe."
    show BBW surprised
    show FMG surprised-2
    MCT "Whoa... That was pretty harsh. You could hear a pin drop in the gymnasium after that insult landed."
    FMG "YOU..."
    show FMG angry
    FMG "TAKE THAT BACK!"
    MCT "Just like before, things were quickly getting out of hand with these two. One of us should probably say something to help diffuse the situation."
    menu:
        "Speak up":
            jump BBWFMG001_c1_1
        "Tell Alice to say something.":
            jump BBWFMG001_c1_2

label BBWFMG001_c1_1:
    $setFlag("BBWFMG_c1_1")
    MC "Girls please, none of this is necessary. Natsuko bought a dress from Alice- that's all there is to this story. Look, everyone in the gym is staring, this whole thing is uncomfortable for everyone."
    MCT "Natsuko and Akira moved their gazes in my direction. For a brief moment, I thought I saw their stern, angry expressions both begin to yield into sheepish embarrassment-"
    MCT "right before snapping right back to locking eyes with each other, renewing their fiery hatred in the process."
    MC "Well, I tried."
    jump BBWFMG001_c1_2

label BBWFMG001_c1_2:
    show BBW stern
    BBW "That is quite enough ladies."
    MCT "Both Natsuko and Akira were eager to renew their argument in spite of Alice's stern reprimand, pointing their fingers at the other."
    FMG "But she-"
    Natsuko "But she-"
    show BBW angry
    BBW "I said that's enough!"
    show BBW stern
    BBW "Now you listen- both of you."
    BBW "I don't know what it is that makes two of the most good-natured and easy-going people I've met at this school turn into vulgar beast in the presence of each other, but"
    BBW "I am disappointed that neither of you can manage to keep your composure and act like proper adults towards each other in the presence of company."
    BBW "Quite frankly it's embarrassing to be seen around you two when a fight breaks out."
    MCT "Natsuko and Akira began to look down and to the side, away from each other, slowly absorbing Alice's chastising."
    BBW "Whatever possesses you two to do so is none of my business,"
    BBW "but what I will not stand for is listening to the two of you denigrate each other's bodies for the sake of petty one-upmanship at a time in all our lives where everyone here is the most insecure they've ever been about the changes going on with themselves."
    show FMG sad
    BBW "One of the reasons I started my custom clothing business was that I knew it could be just one thing that could help students here feel normal again."
    BBW "They could forget about the world not built for them for a bit, just by having something fashionable that actually fit them again."
    BBW "It doesn't feel too nice when people make fun of your body shape does it? Look at me. You two don't even know the half of it, and still neither of you can take it."
    BBW "Do you see me fly off the handle every time I hear some snide, inconsiderate remark within an earshot? I suggest you both grow beyond such childish ways."
    FMG "I guess I didn't think of it that way."
    Natsuko "That's because you don't think about anything."
    show FMG angry-2
    show BBW angry
    BBW "Zip it!"
    show BBW stern
    BBW "Keisuke and I are done here."
    BBW "What you two do together in your own time with each other is your own business, but if you insist on ruining the company of our friends with your petty squabbles again, you can forget about using my help to find clothes that actually fit."
    show FMG sad
    MCT "And with that final verdict, Alice turned around and began to walk away. I stood there, momentarily dumbstruck, trying to take in what had just transpired."
    show BBW haughty
    MCT "Alice briefly paused after passing me, shooting me a look to say 'Aren't you coming?' as my eyes just followed her without my feet following suit up till this point."
    MCT "I proceeded to do an about face, hurrying my pace briefly to catch up to her, only to look back at Natsuko and Akira sulking as they walked away from each other."
    MCT "Alice had walked right into the crossfire of a verbal sparring match between two titans, took control of the situation, and left them both looking like sad puppies just moping around."
    if getFlag("BBWFMG_c1_1"):
        MCT "When I tried on the other hand, I was just brushed aside as a minor interruption to the war they were determined to wage against each other."
    MCT "Alice certainly had a commanding presence about her when she wanted it."
    scene Dorm Exterior with fade
    MC "Alice, how did you do that?"
    show BBW haughty with dissolve
    BBW "Do what?"
    MC "How did you get through to them like that? They looked like they were about to strangle each other, blocking out everyone else entirely-"
    MC "but you got through to them and took them to task. I mean Natsuko and Akira are pretty intimidating, but you didn't even blink."
    BBW "If you need to get through to someone like that, you have to be assertive. It's not about being nice, but it's not about being mean either, you just have to stand firm."
    if getFlag("BBWFMG_C1"):
        $setAffection("BBW", 1)
        show BBW happy
        BBW "I know you tried, and it was an admirable effort, but your tone was too nice. That's why they ignored you. Be more assertive next time you have to confront someone."
        show BBW aroused
        BBW "I like it when a man is assertive."
        MC "Duly noted."
    show BBW happy at Position(xpos=0.25, xanchor=0.5, yalign=1.0) with dissolve
    MCT "We proceeded to walk back to Alice's dorm, both eager to resume our original plans to hang out and put the previous incident behind us."
    show FMG neutral at Position(xpos=0.75, xanchor=0.5, yalign=1.0) with dissolve
    FMG "Yo! Alice."
    MCT "Akira called out to Alice and rushed over with surprising speed as she hurried to catch up with us."
    FMG "Hey, uh, it's not easy for me to admit it, but I, um- I just wanted to say back there, you were right."
    FMG "I'm sorry about what I did to make a scene, even if it's cause of Nasty-Natsy. What she said really hurt, and I know I wasn't much better, but thanks for making her stop."
    BBW "Well you're most certainly welcome."
    show FMG happy
    FMG "Awesome! Speaking of what happened back there though, I have to say, you're one tough broad you know that?"
    show BBW surprised
    BBW "Excuse me?!"
    FMG "I mean I think I'm pretty tough, but that steely glare of yours is kinda of scary. You certainly have a commanding presence when you pull it out."
    show BBW doubt
    BBW "Did you just call me-"
    MC "I think what Mitzutani-chan is trying to say is that she has a newfound respect for you, and how you handle yourself."
    BBW "Oh?"
    show FMG flex
    FMG "Bingo- nailed it my man!"
    show BBW neutral-2
    BBW "I see. Well thank you, Mitzutani...-chan. I'm glad to hear that. Keisuke and I have to get going, but I hope you have a great rest of the day. I'm sure we'll be seeing more of each other soon."
    show FMG neutral
    FMG "Oh for sure! I have to get back to my workout anyway- see you around!"
    hide FMG with dissolve
    show BBW neutral-2 at Position(xalign=0.5, yalign=1.0) with dissolve
    MCT "And with that Akira ran off, likely the start of a very long and fast run, knowing her."
    MC "Huh, I thought she'd still be kind of mad, but it seems like you really got through to her."
    BBW "I guess so. I must admit I underestimated her myself even."
    MC "Maybe we'll have to hang out with her more often then."
    jump daymenu
