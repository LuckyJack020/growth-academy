define PRG = Character('Kodama', color="#FF3399", what_prefix='{size=-6}', what_suffix='{/size}')

image PRG neutral = DynamicImage("Graphics/PRG-[globalsize]-neutral.png")
image PRG happy = DynamicImage("Graphics/PRG-[globalsize]-happy.png")
image PRG sad = DynamicImage("Graphics/PRG-[globalsize]-sad.png")
image PRG surprised = DynamicImage("Graphics/PRG-[globalsize]-surprised.png")
image PRG angry = DynamicImage("Graphics/PRG-[globalsize]-angry.png")
image PRG aroused = DynamicImage("Graphics/PRG-[globalsize]-aroused.png")

init python:
    eventlibrary['PRG001'] = {"name": "PRG001", "girls": ["PRG"], "conditions": [], "priority": 0}
    eventlibrary['PRG005'] = {"name": "PRG005", "girls": ["PRG"], "conditions": [[ConditionEnum.PRESET]], "priority": 0}
    
label PRG001:
    MC "Geez, so many first day things to let sink in. First the growing, then my roommate's chatter, and school work to put a nice little cherry on top of things."
    "As I continued to walk down the hall, I saw a student further down the hallway with a mop in her hands and a bucket by her feet as she was...mopping the floor?"
    extend " I stopped as I looked over my shoulder to see the janitor’s closet slightly ajar. Something just didn’t seem to add up right."
    MC "Hey!"
    show PRG sad with dissolve
    "Huh, the poor girl nearly jumped a foot off the ground as she was startled out of her trance. Instantly, she swiveled on her heels to face me with an extremely apologetic expression."
    PRG "K-keisuke-san? "
    "Her eyes glistened as if she was on the verge of tears, whether from happiness or sadness, I couldn’t really tell."
    extend " She gazed down at the floor and her knees clacked together with a nervous expression on her face. It was obvious that I would have to say something, otherwise this would get awkward fast."
    menu:
        "Hey there, uhh, you, what are you doing?":
            jump PRG001_c1
        "That is my name, yes. Who are you again?":
            jump PRG001_c2
        "Please don't look at me with those eyes...":
            jump PRG001_c3

label PRG001_c1:
    $ setAffection("PRG", 2)
    "As if those were some kind of magic words, Aida looked up from the clean floor with her expression a bit happier. But overall, still nervous. "
    PRG "I’m...Aida,"
    "Goodness, just the sound of her voice makes me want to comfort this poor thing."
    PRG "I’m cleaning up…the school, so that...I can be some help."
    jump PRG001_after
    
label PRG001_c2:
    $ setAffection("PRG", 1)
    "She blushed as her grip on the mop handle tightened up."
    if getAffection("PRG") > 1:
        PRG "I’m Aida...remember?"
        "My memory tried to associate that name with her face and all I can remember is her sitting way back in the auditorium during the opening speech."
        MC "Oh yeah! I saw you at the auditorium. What are you doing now though?"
    else:
        PRG "I’m Aida..."
        MC "Well that’s a nice name, but what are you doing?"
        show PRG neutral
        PRG "I just thought....that I would be of some help if....I cleaned up the school...."
    jump PRG001_after

label PRG001_c3:
    "I could’ve sworn I heard a tiny mutter come out of her mouth before I saw water roll down he-Oh god I made her cry...."
    MC "Wait, wait! Don’t cry!"
    PRG "I’m sorry...I didn’t mean to freak you out…"
    "I could see her knuckles whiten as she clenched onto that mop handle. Annnnd, she’s looking back down at the floor."
    MC "Well you didn’t mean to, right? But anyways. What are you doing now?"
    PRG "Cleaning up...the school."
    MC "Well that’s kind of obvious. And no need to sound like all of your puppies died!"
    jump PRG001_after

label PRG001_after:
    MC "But why? The student job list hasn’t even been distributed yet. How did you even get into the supply closet?"
    show PRG sad
    PRG "Well you see...the supply closet wasn’t...locked. And I....I want to be as helpful as I can to everyone here!"
    "Goodness, something doesn’t seem to be right with this girl. At least she was determined to do what she said to do...I should probably get her to put those items back before she gets in trouble."
    MC "Well, is there any way you can be helpful without taking someone’s work away?"
    "She kind of seemed hurt by that comment, even more so than before despite the improbability. She put a finger to her chin in thought to think it over."
    show PRG neutral
    PRG "Well...I am good with cooking..."
    MC "Great, maybe you can make people snacks for when they’re feeling down?"
    "It was as if my words meant the world to her, as the mop fell out of her hands as her smile grew wider. All I did was suggest something!"
    PRG "I think...I’ll do that. I’ll make the best treats...on school grounds, and then maybe people will..."
    "She finally seemed happy with that final statement, like it was her one and only hope. With that, she picked up the cleaning supplies and walked off..."
    jump daymenu
    
label PRG005:
    MC "This scene hasn't been finished, but needs to exist, so here's a placeholder."
    jump daymenu