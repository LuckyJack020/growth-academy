define FMG = Character('Akira', color="#FF9900")

image FMG neutral = DynamicImage("Graphics/FMG-[globalsize]-neutral.png")
image FMG happy = DynamicImage("Graphics/FMG-[globalsize]-happy.png")
image FMG sad = DynamicImage("Graphics/FMG-[globalsize]-sad.png")
image FMG surprised = DynamicImage("Graphics/FMG-[globalsize]-surprised.png")
image FMG angry = DynamicImage("Graphics/FMG-[globalsize]-angry.png")
image FMG aroused = DynamicImage("Graphics/FMG-[globalsize]-aroused.png")

init python:
    eventlibrary['FMG001'] = {"name": "FMG001", "girls": ["FMG"], "conditions": [], "priority": 0}
    eventlibrary['FMG002'] = {"name": "FMG002", "girls": ["FMG"], "conditions": [], "priority": 0}
    eventlibrary['FMG003'] = {"name": "FMG003", "girls": ["FMG"], "conditions": [[ConditionEnum.EVENT, "FMG002"]], "priority": 0}
    eventlibrary['FMG004'] = {"name": "FMG004", "girls": ["FMG"], "conditions": [[ConditionEnum.EVENT, "FMG003"]], "priority": 0}
    eventlibrary['FMG005'] = {"name": "FMG005", "girls": ["FMG"], "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.EQUALS, "7"], [ConditionEnum.AFFECTION, "FMG", ConditionEqualityEnum.GREATERTHAN, "2"]], "priority": 15}
    
label FMG001:
    "After Thinking it over, I decided to check out the Athletics Area so when I have P.E. I would know where it is."
    "Compared to the rest of the academy, the building itself was not only taller, But almost as wide as the rest of the school."
    "From how tall the windows were made the the building looked least two or three stories tall."
    "As I wondered if the inside really was big as it looked on the outside, I found myself walking in too satisfy my curiosity."
    "The inside was was not what I thought it would look like, what I imagined to be a normal three story building turned out to be just one room that was three stories high."
    "The exercise equipment was unique, to say the least; while some did look normal, most of them came in extreme shapes and sizes."
    "One thing I also noticed was that the building was so empty that there was an lone echo coming from the far end of the building and once again curiosity drove me to follow where the source of the echo was coming from."
    "As I got closer to the source, I began to hear someone counting."
    UNKNOWN "...87...88…"
    "From where I was I could tell it was female, but I couldn’t make out who it was just yet."
    UNKNOWN "...92...93..."
    "After a minute of looking I found that the source of noise was coming from a bench pressing Akira."
    "From what I could guess, she was too focused on her workout to notice me walking towards her, or that she assumed it was just someone who was working out as well."
    show FMG angry with dissolve
    FMG "98...99...100!"
    "Akira Then proceeded to put the weights back on the bar and moving off the bench press; it was only when she looked up she saw me watching her."
    show FMG neutral
    FMG "Well hey there...um your name was Keisuke right?"
    MC "Indeed it is."
    FMG "Alright, Keisuke, got it...So as I was saying...what brings you to these parts?”"
    MC "Curiosity mostly, I wanted to checked out the Athletics Area to get a better layout of the school and when I got here I heard an echo that lead me to you."
    show FMG happy with dissolve
    FMG "And here I was thinking you were here to check me out."
    "The way she said that sounded she was joking, but I just found it kinda awkward, still it would be a bit rude not to give some sort of reply."
    "My only response was a light chuckle and then silence. We stood there for about 30 seconds till I spoke up."
    MC "So Akira...how are you holding up?"
    show FMG neutral
    FMG "huh, what do you mean?"
    MC "Well, I mean that we're going have these 'growths' affect the rest of our lives, so what I’m asking is how you’re taking this?"
    show FMG happy
    FMG "Oh, in that case I’m fine with it."
    MC "Huh, really?"
    show FMG neutral
    FMG "Yeah, I don’t know if I will grow or not but if I do, I accept it with open arms."
    MC "You don’t know you’re going to grow?"
    FMG "Well I mean compared to people like your boob friend or Shiori Buttsumoto, I’d think I look normal enough."
    MC "Well you are a bit muscular."
    FMG "Yeah But not overly."
    "She proceed to put her hand under her chin and push her head to left side, causing a series of loud cracking from her neck. She repeated this process with the right before continuing."
    show FMG happy with dissolve
    FMG "I may work out almost every day, but it’s not my entire life, Just 80%%."
    show FMG neutral with dissolve
    FMG "So yeah, just call it a hunch. What about you?"
    MC "Well I don’t feel any different but I am kinda worried about my sis-"
    "I didn’t get to finish my sentence when Akira looked at a nearby clock and interrupted me."
    show FMG sad
    FMG "Ah crap! It’s 5:35 I’m five minutes late for my routine!"
    hide FMG with dissolve
    "She said while running past me to the door."
    MC "Wait huh?"
    "Was all I could say in flustered state. Akira then turned around jogging in one spot for a brief moment."
    show FMG sad with dissolve
    FMG "Sorry! I have to go now, if you want to talk you can find me here whenever theres no classes or at the local Gym, later!"
    hide FMG with dissolve
    "And in a flash, Akira proceeded to sprint out the door, leaving me in the same spot, still a bit confused."
    MC "Well that happened."
    "With that I left the building."
    jump daymenu
    
label FMG002:
    "With class over I decided to take a shortcut through the Athletics Area."
    "I’d expected to see Akira coming out of the building, what I didn’t expect to see was her looking very tired."
    "I figured she must need some cheering up so went to go talk to her."
    MC "Hey Akira, what’s up?"
    "Her facial response was of that of slight confusion and following that annoyance."
    show FMG angry with dissolve
    FMG "Ugh, what do you want Keisuke?!"
    "I was honestly taken back of Akira’s response, but in hindsight with how tired she looks I probably should have expected this."
    "Her face slowly softened from a face of annoyance to one of regret."
    show FMG sad
    FMG "*Sigh*...Look, I’m sorry, I just get frustrated sometimes."
    "She apologized, for the most part she did look apologetic but she still looked physically tired, if not mentaily."
    MC "Um, is everything alright?"
    "I asked,  took a deep breath before answering."
    FMG "Not really, I went too hard on the treadmill and now I’m too tired to do the rest of my routine."
    MC "Really, how?"
    FMG "I thought if I did twice the speed I normally go I’d get it done in half the time."
    "She paused before continuing."
    FMG "For the most part it worked, but I forgot about the side effect of going past your limit."
    MC "I mean, isn’t that the goal to push yourself?"
    FMG "Yeah, but the point of it is to PUSH your limit, not fricking PASS it to the point of exhaustion."
    FMG "Trust me it’s not healthy to do that, the body can only take so much exercise before needing to repair muscle. If you keep doing it with no breaks you’re doing more harm than good."
    MC "Well that sucks, what are you going to do now?"
    FMG "I’m going to bed, I need to let my muscles heal. So if it’s all the same, I’ll be leaving."
    MC "Ok then, bye."
    FMG "...yeah, later."
    hide FMG with dissolve
    "I was about to make my leave, when I heard Akira call out my name."
    show FMG neutral with dissolve
    FMG "Um...thanks for caring enough to ask."
    MC "You’re welcome Akira."
    "With that we went our separate ways."
    jump daymenu
    
label FMG003:
    "After finally finished with my morning class, I went to get a quick snack from the vending machines before had to repeat the process with my next class."
    "At least for the most part it was business as usual..."
    FMG "HEY KEISUKE!!!"
    "...That is until I saw Akira sprinting down the hall."
    "I braced for impact,but Akira came to a screeching halt just before colliding into me."
    show FMG neutral with dissolve
    FMG "Yo, how’re you?"
    "She asked, almost to casually for someone who just went sprinting down a hallway at 32 kph." 
    MC "Um...fine?"
    show FMG sad
    FMG "Great, hey look about the other day..."
    MC "Oh you don’t have to apologize, you were just having a bad day is all."
    show FMG neutral
    FMG "Yeah I know, but I feel like I should make it up to you. I thought about it and, well, do you want to join me in my work out sessions?"
    MC "Wait what?"
    FMG "Well I figured I could make it up to you by becoming like your personal trainer."
    MC "My personal trainer? Why?"
    FMG "Well I know that you’re not chubby like 'Princess' Alice Whatever-her-last-name-is, but that doesn’t mean you're not out of shape either."
    FMG "Plus it could help having some muscle when in the middle of a fight, or just want to look good to the ladies."
    FMG "But if you don’t want to do that’s fine, I’m not gonna force you to do something you don’t want to do."
    FMG "So, you game?"
    menu:
        "Eagerly agree":
            jump FMG003_c1
        "Agree but at your own pace":
            jump FMG003_c2
        "Refuse":
            jump FMG003_c3

label FMG003_c1:
    $setAffection("FMG", 2)
    MC "Sure, why not? Let's do it!"
    "I honestly have no idea why I came off so excited, maybe some of akira’s energy had rubbed off on me."
    show FMG happy
    FMG "Heck yeah! That’s the spirit, Keisuke. I expect you at your top fitness..."
    show FMG sad
    FMG "...Wait is it top fitness?"
    show FMG happy
    FMG "Ah screw it, just be ready okey?"
    MC "Alright, when do get started?"
    show FMG neutral
    FMG "When the time comes, you’ll know..."
    MC "Um... no I don’t, t-that's why I-"
    FMG "Oh Crap the bell’s gonna to ring in 30 seconds! LATER!"
    hide FMG with dissolve
    "She yelled out before sprinting down the hall... leaving me bewildered."
    MC "...Asked...Wait, 30 seconds!?"
    jump daymenu

label FMG003_c2:
    $setAffection("FMG", 1)
    MC "...Alright, I guess..."
    FMG "Yes! We ca-"
    MC "BUT!"
    "I spoke up, catching her off guard."
    MC "I will only do it at my own pace, I don’t want to feel like i’m dying after the first session."
    show FMG sad
    FMG "...Oh well...yeah that makes sense."
    show FMG neutral
    FMG "I’ll admit I’m a little disappointed, but I’m more glad you’re willing to give it a shot."
    MC "Well I am willing as long as-"
    FMG "Oh Crap the bell’s gonna to ring in 10 seconds! LATER!"
    hide FMG with dissolve
    "She yelled out before sprinting down the hall... leaving me bewildered."
    MC "...You don’t go overboard...Wait, 10 seconds!?"
    jump daymenu

label FMG003_c3:
    $setAffection("FMG", -1)
    MC "Um look it’s nice of you to offer but I got too much to worry about with school and everything else."
    "Upon me saying this her facial expressions turned from hopeful to disappointed."
    show FMG sad
    FMG "Oh...ok."
    MC "I’m sorry about this, but thanks for the offer."
    FMG ":No it's fine, I’m not made of glass. If you change your mind you know where to find me..."
    MC "...So see you later?"
    FMG "Yeah Later."
    hide FMG with dissolve
    "I honestly felt kinda bad for her but i got too much on my plate to worry about exercise."
    "..Like the fact I’m going to be late for class if I don’t move!"
    jump daymenu
    
label FMG004:
    "Another day, another class over...and for once I have nothing to do..."
    "...That is until a paper ball (that Akira throw before running out of class) hit me on the head."
    MC "Ow."
    "I said more out of reflex than pain. I decided to uncrumple the piece of paper out of boredom."
    "\n{i}The time has come! Meet me at the school’s track in 5\n~Akira{/i}"
    "I guessing she must be excited, as she didn't even put a period at the end of her note."
    "Well I promised her i’d join her so might as well see what she’s up to."
    "By the time I got there, I'd expected too see Akira be the here already, all the while doing stretches."
    "As I got closer she stopped doing her stretches and walked up to me."
    show FMG happy with dissolve
    FMG "Welcome partner, to the beginning of your training!"
    MC "Well I'm ready for whatever, what will we be doing today?"
    show FMG neutral
    FMG "Today we shall do something simple and easy."
    "She’s going to make me run is she..."
    FMG "Running this whole track."
    "I hate being right sometimes."
    show FMG sad
    FMG "*sigh*... But first, we have to do something first..."
    "She reached for her bag, pulling out two cups with lids on it."
    FMG "...We have to drink...*gag*... these protein shakes."
    MC "Oh that's it, you made it sound like something bad."
    FMG "Well the thing is, I HATE protein shakes. Like a lot."
    MC "Really? I thought protein shakes were important for exercise."
    FMG "Well it is, doesn't mean I have to like them though. Now as much as I want to delay drinking this sludge, it has to be done."
    "She took it in one go, eyes shut tight the entire time. When she finished it she looked like she was about to vomit."
    "I knew I had to drink it as well, but I figured Akira might just be over exaggerating , I mean can't be that-"
    MC "*GAG*"
    "Oh god, why didn't she add fruit or something..."
    "Well I've already agreed to this, might as well finish it."
    FMG "Ugh...God I feel like I'm gonna die every time I'd drink those things."
    MC "Yeah I don't blame you...just what was is in that?"
    show FMG neutral
    FMG ":It's just water and protein powder, why?"
    MC "Ever thought of using a liquid that has flavor, like milk or Berry tea?"
    "She just looked at me with no expression, but I swear I could hear her screaming internally."
    FMG "..."
    extend "Oh well there's always next time."
    show FMG happy
    FMG "Now that the hard part is over, now we get to the actual exercise! Don't worry, I'm not asking for you to run a mile, just a quarter of one!"
    FMG "Today we're going to just make one lap around this track."
    "I followed her to the starting point."
    show FMG neutral
    FMG "Alright ready..."
    FMG "GO!"
    hide FMG with dissolve
    #if Athletics < 5
    $setAffection("FMG", -1)
    "Ok, akira’s got the lead, but if I can keep a good pace I can do this!"
    "I can do this!"
    "...I can do this..."
    "...I...can...do...this..."
    "Just realized Akira had already finished and she was walking to me...and I'm not even near halfway done."
    show FMG sad with dissolve
    FMG "Um...are you okay?"
    "Her concern was clearly shown."
    MC "I... can't *wheeze* do this..."
    FMG "But... dude you're not even half way."
    "Her concern turned to slight annoyance."
    MC "Don't...care *heavy breathing* must... rest..."
    show FMG angry
    FMG "Dude, you're really not making a good first impression, you're worse off than I thought."
    "Now she looked REALLY annoyed."
    MC "...Tell... Daichi...I took his last chocolate...b-bar..."
    FMG "You're not even dying you big baby!"
    hide FMG
    "The last thing I saw before my world was swallowed in darkness was a angry Akira."
    "When I woke up it was an hour later, Akira was nowhere to be found,but there was a piece of paper on my chest."
    "\n{i}Dear Kei, WORK ON YOUR GET IN FRICKING SHAPE!\n~Akira{/i}"
    "...Yeah I get the feeling Akira is not going to let me live this down..."
    jump daymenu
    #if Athletics >= 5
    $setAffection("FMG", 1)
    "Despite Akira already in the lead, I managed to keep a good pace."
    "I started to feel a bit winded half way but I pushed myself to go farther."
    "It was about to the end when I was starting to get too tired, luckily I've managed to run the whole lap before stopping completely."
    show FMG happy with dissolve
    FMG "WOO!"
    "Akira fist pumped before walking towards me."
    FMG "Great job there dude, you sure got potential!"
    MC "But I lost, you won by a landslide."
    FMG "It’s not about competing, it's about giving all you got and you stuck with it all the way to the end!"
    FMG "Stay right there, need to go get something from the vending machines."
    hide FMG
    "She run to where the vending machines were. When she came back, in each of her hands was ice cream, one cherry blossom and one vanilla."
    show FMG happy
    FMG "Here, A congratulation prize, didn't know what flavor you liked so I got you vanilla."
    MC "Ice cream? But isn't that like the worst thing you could have during a workout?"
    show FMG neutral
    FMG "True, but i’d probably burned half the calories of this ice cream pop in this run, and that's not including the rest of my workout today."
    "I don't think that's how it works…"
    FMG "Besides, I’ll take eating a ice cream pop and workout the entire day then drink a fricking protein shake and workout just for only an hour any day of the week."
    MC "At least you got your priorities straight."
    show FMG happy
    FMG "Hell yeah I do!"
    "We stayed there for a while till both ice cream’s were finished. Akira tossed her popsicle in the trash before turning to me."
    show FMG neutral
    FMG "Well this has been fun, lets call it a day shall we."
    MC "Sure, but I got a question."
    FMG "Shoot."
    MC "Why vanilla?"
    FMG "I don't know, you seem like a vanilla kinda guy."
    "I don't know why but I got a chuckle out of that."
    "I waved good bye before heading back to my room."
    jump daymenu

label FMG005:
    show FMG sad
    FMG "...Hey..."
    "She looked slightly annoyed and she had her left hand on her right upper arm...but I could tell there was some moisture still under her eyes."
    menu:
        "Are you okay?":
            jump FMG005_c1
        "Man shots suck.":
            jump FMG005_c2

label FMG005_c1:
    $setAffection("FMG", -1)
    MC "Are you okay?"
    FMG "No, I just had a stupid needle jammed into my arm to find out my growth factor, which by the way was a waste of time."
    MC "Okay...Well what was it?"
    "I did my best to try and act dumb for her sake but instead she took it the wrong way."
    show FMG angry
    FMG "MY MUSCLES!"
    "I was taken back from her outburst,  to which she grudgingly looked away."
    show FMG sad
    FMG "Look, i’m not in the best of moods so just leave me alone for now, ok?"
    "She preceded to walk away from me, I figured it was best to leave her alone."
    jump daymenu

label FMG005_c2:
    $setAffection("FMG", 1)
    MC "Man, Shots suck am I right."
    "I felt that it was best to try to lighten her up, and it seems I was rewarded."
    show FMG neutral
    FMG "Heh, yeah they do, i’m guessing you heard all of that?"
    MC "Um..."
    FMG "It’s fine, just don’t go spreading what's going to happen to me, I want to tell it on my own terms."
    MC "Fair enough then."
    MC "...so will you be alright?"
    FMG "Well it's not the growth that’s affected me the most...it's the needles."
    MC "Um, if I may, why do you hate needles so much?"
    FMG "When I was 3 I was playing in the backyard when a rabid raccoon bit me on my leg...hard."
    "She emphasized this by pulling down her right sock, revealing a scar in the shape of a bite on her calf."
    FMG "If you were wondering why I wear my socks so high, that's why."
    "She pulled up her sock before continuing."
    FMG "My parents rushed me to the hospital where they injected me with all kinds of needles."
    show FMG sad
    FMG "I think it’s a combination of the bite and the needles that kinda f’d me up."
    FMG "Just the sight alone makes me hyperventilate...but when it goes under is when I start getting pissed."
    MC "Wow...I don’t know what to say."
    show FMG neutral
    FMG "Don’t worry about it, I mean it’s not something I care for, but I usually feel better when talking about it...well when I calm down at least..."
    FMG "Otherwise I’d just get mad for no good reason."
    FMG "Alright, if it’s all the same to you I’d rather be alone right now."
    FMG "But for what it's worth, thanks for the talk...I REALLY needed it."
    hide FMG
    "With that she left, leaving me alone next to the door to the nurse's office."
    jump daymenu