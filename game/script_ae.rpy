define AE = Character('Shiori', color="#FF3300")
define Student1 = Character('Student 1', color="#FF3300")
define Student2 = Character('Student 2', color="#FF3300")
define Student3 = Character('Student 3', color="#FF3300")

image AE neutral = ConditionSwitch(
    "gametime > datelibrary['AE_size_2']", "Graphics/AE-2-neutral.png",
    "True", "Graphics/AE-1-neutral.png")
image AE happy = ConditionSwitch(
    "gametime > datelibrary['AE_size_2']", "Graphics/AE-2-happy.png",
    "True", "Graphics/AE-1-happy.png")
image AE sad = ConditionSwitch(
    "gametime > datelibrary['AE_size_2']", "Graphics/AE-2-sad.png",
    "True", "Graphics/AE-1-sad.png")
image AE surprised = ConditionSwitch(
    "gametime > datelibrary['AE_size_2']", "Graphics/AE-2-surprised.png",
    "True", "Graphics/AE-1-surprised.png")
image AE angry = ConditionSwitch(
    "gametime > datelibrary['AE_size_2']", "Graphics/AE-2-angry.png",
    "True", "Graphics/AE-1-angry.png")
image AE aroused = ConditionSwitch(
    "gametime > datelibrary['AE_size_2']", "Graphics/AE-2-aroused.png",
    "True", "Graphics/AE-1-aroused.png")

init 2 python:
    datelibrary['AE010_deadline'] = datetime.date(2005, 4, 13)
    datelibrary['AE_size_6'] = datetime.date(2005, 12, 10)
    datelibrary['AE_size_5'] = datetime.date(2005, 12, 10)
    datelibrary['AE_size_4'] = datetime.date(2005, 12, 10)
    datelibrary['AE_size_3'] = datetime.date(2005, 12, 10)
    datelibrary['AE_size_2'] = datetime.date(2005, 4, 10)
    
    eventlibrary['AE001'] = {"name": "AE001", "girls": ["AE"], "location": "library", "conditions": [], "priority": False}
    eventlibrary['AE002'] = {"name": "AE002", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE001"]], "priority": False}
    eventlibrary['AE003'] = {"name": "AE003", "girls": ["AE"], "location": "campuscenter", "conditions": [[ConditionEnum.EVENT, "AE002"]], "priority": False}
    eventlibrary['AE004'] = {"name": "AE004", "girls": ["AE"], "location": "dormexterior", "conditions": [[ConditionEnum.EVENT, "AE003"]], "priority": False}
    eventlibrary['AE005'] = {"name": "AE005", "girls": ["AE"], "location": "hallway", "conditions": [[ConditionEnum.PRESET]], "priority": False}
    eventlibrary['AE006'] = {"name": "AE006", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE004"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": False}
    eventlibrary['AE007'] = {"name": "AE007", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.FLAG, "AE006_helpinginoffice"], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    eventlibrary['AE008'] = {"name": "AE008", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE007"], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    eventlibrary['AE009'] = {"name": "AE009", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE008"], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    #eventlibrary['AE010'] = {"name": "AE010", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.FLAG, "AE006_helpinginoffice"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["AE_size_2"]], [ConditionEnum.GAMETIME, ConditionEqualityEnum.LESSTHAN, datelibrary["AE010_deadline"]], [ConditionEnum.ISNIGHTTIME]], "priority": True}
    eventlibrary['AE010'] = {"name": "AE010", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.FLAG, "AE006_helpinginoffice"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["AE_size_2"]], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    #eventlibrary['AE011'] = {"name": "AE011", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE009"], [ConditionEnum.OR, [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHANEQUALS, datelibrary["AE010_deadline"]], [ConditionEnum.EVENT, "AE010"]], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    #eventlibrary['AE012'] = {"name": "AE012", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE011"], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    #eventlibrary['AE013'] = {"name": "AE013", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE012"], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    #eventlibrary['AE014'] = {"name": "AE014", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE013"], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    #eventlibrary['AE015'] = {"name": "AE015", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE014"], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    #eventlibrary['AE016'] = {"name": "AE016", "girls": ["AE"], "location": "library", "conditions": [[ConditionEnum.EVENT, "AE015"], [ConditionEnum.ISNIGHTTIME]], "priority": False}
    #eventlibrary['AE017'] = {"name": "AE017", "girls": ["AE"], "location": "cafeteria", "conditions": [[ConditionEnum.EVENT, "AE016"]], "priority": False}
    #eventlibrary['AE018'] = {"name": "AE018", "girls": ["AE"], "location": "cafeteria", "conditions": [[ConditionEnum.EVENT, "AE017"], [ConditionEnum.ISDAYTIME]], "priority": False}
    #eventlibrary['AE101'] = {"name": "AE101", "girls": ["FMG", "AE"], "location": "gym", "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": False}
    #eventlibrary['AE102'] = {"name": "AE102", "girls": ["AE", "FMG"], "location": "hallway", "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": False}
    
label AE001:
    scene Library with fade
    "After a long day, I figured that some time in the library would do well for me. I could use somewhere quiet to wind down."
    MCT "Geez, I expected quiet, but this room is practically abandoned!"
    "Even though a few hours had passed, what Tashi-sensei said was still ringing in my head. I wasn't completely sure how to process what had been going on, but I was worried to say the least."
    MCT "I need to sit down...the table over there looks good."
    "I grabbed a chair, sat down at the table and, resting my head on my hands, I let out a long sigh."
    MC "Well, I never got anywhere by just moping... right?"
    AE "*Ahem*"
    MC "Eh?"
    "I looked over to the table adjacent, where I saw Shiori-san flipping through the pages of a large book."
    show AE angry with dissolve
    MC "A-ah! Shiori-san, how are y-"
    AE "Hotsure-san, adjust your volume in the library, please."
    MCT "Oh...right."
    MC "Sorry, Shiori-san."
    show AE neutral
    AE "Hm."
    hide AE with dissolve
    "Shiori looked back down to her book, eyes fixated on the page in front of her. She adjusted her slowly slipping glasses and turned to the next page."
    MCT "Ok, I guess I'll just...sit here."
    "The silence in the room was palpable."
    "It's weird when you think you're alone, but then learn another person is there, and your body just tenses up a bit. Though it may very well have just been Shiori's presence."
    "She was someone who just emanated a strict and commanding aura... but still I felt as though I should at least try to socialize."
    MCT "Should I just move over to her table? Would that be intrusive?"
    "I moved over and sat a seat away from where she was, better to be near and speak softly than far and shout I supposed."
    MC "So... hey."
    "Shiori looked up from her book, glancing at me with an apathetic gaze."
    show AE neutral with dissolve
    AE "...Hello, Hotsure-san."
    MC "How, uh, w-what are you doing?"
    MCT "Uaaah, she's absolutely chilling me to the bone!"
    AE "Researching questions I had that Tashi-Sensei was unable to answer."
    MC "Ah, what about?"
    AE "The nature of the Academy."
    extend " What is going on,"
    extend " how long has this been happening,"
    extend " what preventative measures are there,"
    extend " what school records exist."
    AE "There are so many questions I have, and I plan to make sure they are all answered."
    "Shiori looked back down at her book, steadily writing down notes with her other hand."
    "We sat in silence for a few moments, Shiori-san dutifully writing down line after line of notes while I stared up towards the ceiling."
    MCT "I think...there is still a question I have on my mind..."
    menu:
        "How are you taking all this?":
            jump AE001_c1
        "I don't think I have anything left to say.":
            MCT "I...don't really think I do, actually. She's busy. I shouldn't bother her."
            jump AE001_after
        "You're worried, aren't you?":
            jump AE001_c3
            
label AE001_c1:
    MC "So...Shiori-san. How are you handling this?"
    AE "..."
    extend " I suppose...I just need to further my understanding of the situation. That's all. It's unlikely that my situation is anything to worry about, anyway."
    MCT "That...didn't really answer my question."
    jump AE001_after
    
label AE001_c3:
    $ setAffection("AE", -1)
    MC "The reason you're in here...you're worried about this whole thing, right?"
    show AE angry
    "Shiori-san stopped writing for a moment and looked up towards me again, with an annoyed look on her face."
    AE "How astute of you to presume my emotions after only a day of meeting me. No. I'm not worried about this, and I think it would be best if you didn't say asinine things so bluntly."
    MC "A-ah! I meant no...I'm sorry."
    "Shiori looked back down at her book, and I felt a chill run down my spine after the talking she gave me."
    MCT "What the hell was I thinking?!"
    show AE neutral
    jump AE001_after
    
label AE001_after:
    "We sat in silence a bit more, until I noticed something...I couldn't hear Shiori writing anymore."
    MCT "Eh? Is she done taking notes already?"
    "I looked over at Shiori, who had stopped writing mid-sentence. Her eyes seemed focused on a particular line, and her mouth opened slightly as she read."
    show AE sad
    AE "What? But...no...that can't be true..."
    MC "S-Shiori-san...are you ok?"
    AE "Yes, I...I just...I have to go. Pardon me, Hotsure-san."
    "I could do little but stammer as Shiori quickly stood up, her rear tilting the chair back on its hind legs before she turned and walked away."
    "The clack of the front legs against the floor as the chair dropped level made Shiori flinch, but she had regained her composure in an instant and kept on walking."
    hide AE with dissolve
    MC "Shiori-san...hm?"
    "I looked over to where Shiori was sitting, and found that she had forgotten to take her book with her."
    MC "Ah! Her book!"
    MCT "What... do I do? Should I just take it and bring it back to her?"
    MCT "..."
    MCT "I guess it wouldn't hurt...if I checked it out and brought it back to her tomorrow."
    "I picked up the book and read the title, 'An examination of Cellular Reproduction'."
    MCT "But why would she... I guess it's not too important. I'll just make sure she gets it next time I see her."
    MCT "Well, so much for a relaxing time in the library, eh?"
    jump daymenu

label AE002:
    scene Library with fade
    MCT "Maybe Shiori-san is here today."
    "As my mind recalled yesterday's events, I began to wander about the library. The sheer size of the place was a stark reminder of just how large the school was...and how unlikely it would be to find Shiori-san in it so quickly."
    MC "Let's see...ah!"
    MCT "Ohp, well, nevermind."
    "It was only now that I noticed the door with the sign 'Student Organizations' directly on top of the door frame on the opposite side of the room."
    scene Office with fade
    "As I moved across the library to the door, I began to notice that, like yesterday, not many people were here. Reading just isn't as popular a pastime as it used to be."
    "I saw her through the large window in the wall separating the Library from the room, where she was working on a stack of papers."
    MC "Um, hello, Shiori-san?"
    "Shiori looked up from the paperwork and did something that kind of took me off guard."
    show AE neutral with dissolve
    AE "Ah, Hotsure-san. Welcome to the Student Organization's room, is there something you need?"
    MCT "Huh? She seems like she's gotten a bit better since yesterday...a lot better, actually."
    MC "Oh, yeah, am I interrupting anything?"
    AE "Not at the moment, no. Come in if you wish, it would be best for you to not have to raise your voice."
    MCT "In the...empty library?"
    MC "Sure."
    "The inside of the room was larger than it first looked. There were filing cabinets that lined the walls, and a long table in the middle with different chairs for the representatives and student body to discuss the agenda of the day."
    MC "Yesterday in the library, you forgot this."
    "I took the book from my bag and put it on the table next to Shiori-san. She looked at it for a moment, and inhaled before looking to me."
    MC "I was wondering if you were wanting it back?"
    AE "Ah! Yes...I had no more need or it."
    MC "Huh?"
    AE "Well, I had read all the parts that pertained to what I was looking for, so I figured that there was no point in bringing it back to my dorm."
    MC "Oh, ok...I just kind of figured that you would put it back..."
    AE "A generous assumption...and what would that achieve? Had I put it back or not, it would have inevitably ended up in it's original spot when the library closed, yes? It is a common courtesy, however it's not officially required."
    MC "True...and I checked it out anyway, so no harm no foul!"
    AE "Indeed. In any case, thank you for being considerate. It's that mindset that helps a school run. Well, that and capable leadership."
    "Shiori's attitude had definitely gotten better, from what I could tell, but the way she was acting the other day kept nagging at me."
    AE "Is there anything else you need?"
    MC "Uh..."
    menu:
        "Are you ok?":
            jump AE002_c1
        "I'm fine.":
            jump AE002_c2

label AE002_c1:
    MC "Yeah...yesterday you seemed really out of it. Are you ok?"
    AE "Of course I am."
    MC "Yeah, I-"
    MCT "Wait, what?"
    MC "Really?"
    AE "I wouldn't answer that I am if I wasn't. I already had at least somewhat of an inkling of what the school was for, even before the announcement."
    MCT "She did!?"
    MC "I kind of thought that-"
    AE "Well, let's look at your claim. You said I was 'out of it', what do you mean by that?"
    MC "Well...you were more silent than usual. It seemed like you were really distraught."
    AE "Than usual? We've only known each other for a small amount of time."
    MC "Ah..well...true. But I still felt kind of unsure as to why you seemed to act differently than the first time we met."
    AE "Simple. First, I had questions that went unanswered, and as such immersed myself in my studies. I found the answers, and as such I feel alleviated."
    MCT "Well, she did kind of keep to her book..."
    AE "Second, I was indeed shocked by the initial reveal, however I don't have reason to believe that it should be too much to bear. After all, if this school is indeed for people with unique...growing situations, then I should be able to adapt in well, yes?"
    MC "True...but it doesn't bother you at all?"
    AE "Hotsure-san, fate is inescapable. If I will grow, as per what Tashi-sensei says, then it will happen inevitably. Why worry about that which will happen no matter what?"
    MCT "Wait, what? Something...irks me about that statement."
    MC "I guess...you have a point."
    AE "As class representative, my responsibility is to the school. I don't have the luxury of worrying about these sorts of things when there are more pressing matters at hand."
    MC "...You're right. I was being silly."
    AE "Certainly not. You had a legitimate concern for a fellow student, and you acted accordingly."
    MC "Well...as long as you're doing ok."
    AE "I assure you, Hotsure-san, I am more than capable of handling myself."
    MC "I believe you, Shiori-san."
    AE "Good. Well then, is that all you need?"
    MC "Yeah, I think that I should be alright."
    AE "Then I will see you in class. Remember, our homework is Chapter 1 section 3. I expect good results."
    MC "Yeah...see you then."
    scene Library with fade
    "As Shiori got back to her work, I walked out of the door and back through the library. While her talk was meant to calm me down, it only ended up raising more questions."
    MCT "How can she be so gung-ho about this?! After the news we all got the other day...I just don't know. I need to go find something else to do to keep my thoughts off of it."
    jump daymenu

label AE002_c2:
    MC "No, I should be alright."
    MCT "It really doesn't matter I guess, she seems alright now."
    AE "Alright then, have a good day."
    MC "Alright, see you later, I guess."
    AE "Oh yes, and Hotsure-san?"
    MC "Yeah?"
    AE "Tuck in your shirt, it doesn't comply with the current dress code."
    MC "Uh...yeah...I will."
    "Shiori turned back to her paperwork, and I turned out of the door to leave the library, content that I had been able to get the book situation sorted. But that still left the question of what else I could do today."
    jump daymenu
    
label AE003:
    scene Campus Center with fade
    MCT "C'mon, just a bit farther!"
    "I had spent a good amount of time after class making paper airplanes and throwing them around in the central courtyard, attempting to beat my earlier record by a few precious inches."
    MCT "Almost...there!"
    "The plane soared through the air and made a smooth crisp landing at about four or so feet in front of me."
    MC "Yes! My farthest yet!"
    MCT "I seriously need to work on my plane making...or at least do something productive instead."
    MC "Hmm?"
    "I heard a bit of squabbling as I got up from the bench I was sitting on and decided to take a tiny peak...just for studying purposes of course."
    Student1 "Come on! It's just a wrapper!"
    show AE angry with dissolve
    AE "I don't care if it's a scrap of paper, it says clearly in your student handbook that there is to be no littering on campus. Period. Do I need to talk to administration about this?"
    Student1 "D-don't be unreasonable!"
    AE "There is a garbage can right over there. Pick it up and throw it away."
    hide AE with dissolve
    MCT "Wow...I don't want to be on the end of THAT scolding...wait."
    "I looked behind me to see the legions of failed craft lying on the ground, and I could swear I broke out in a cold sweat."
    MC "Hoooo boy...I need to pick these up quick, lest Shiori-san comes this way."
    "After a short while, I picked up my tiny, oblong aircraft and put them in my bag, ready to head back to my room. The sense of confusion and surprise left in favor for a general feeling of what I can only describe as uneasy acceptance."
    "Shiori's words resonated with me for a small while the more I thought about it, what will happen will happen, all I can really do is accept it. Although it did seem...strange. I never expected Shiori of all people to prescribe things to fate, but as she said, who am I to say what her 'usual' is. Hell, I'm not sure if this school even has anything 'usual'."
    show AE neutral with dissolve
    AE "Everything alright, Hotsure-san?"
    MC "GAH!"
    "In my shock, I nearly dropped my bag with the planes in tow."
    MC "Oh! Hey, Shiori-san. You scared me. Uh, yeah, I'm all good."
    AE "Yes, well, I apologize for frightening you. You seemed distressed about something."
    MC "Oh, no, i'm fine. Thanks though."
    "There was an air of apprehension as Shiori-san looked on at me in an inquisitive manner; almost judging my every move."
    show AE angry
    AE "Yes, well, if there IS anything you need, don't hesitate to ask."
    MC "Yeah, then...what was our homework again?"
    show AE neutral
    AE "Chapter one, section three, page 16. Read it and answer the questions on the following page."
    MC "Ok, thanks, Shiori-san!"
    AE "Hm."
    hide AE with dissolve
    "I strode off in the opposite direction; breathing a sigh of relief knowing that my paper airplanes didn't win me a thrashing."
    scene Hallway with fade
    MCT "Ok, so if Tashi-sensei wants us to do section three by tomorrow, then I can probably finish in about two or so at home, meaning that I can...eh?"
    Student1 "I'm telling you, it's absolute crap!!"
    "As I walked down the dorm hallways, I came across a group of guys getting in a heated discussion. I would normally just ignore it, but my curiosity got the better of me. I pretended to play around with the nearby vending machine as I listened to what they were talking about."
    Student1 "I'm telling you guys, I have no idea why she thinks she can just walk around and start nagging people."
    MCT "It's...that guy from earlier."
    Student2 "She's the student rep, nothing we can do about it."
    Student1 "And that's what sucks!"
    Student3 "What did you even do?"
    Student1 "Nothing! I just threw my wrapper on the ground and she started prattling off about school code BS and made me pick it up. She can't just talk down to me like that!"
    Student2 "She has nothing better to do with her life, you should just as well let it go."
    Student3 "Right, but it's about the principle of the thing."
    Student1 "Exactly! I can't just let her get away with it."
    MCT "Wow, you're a reeeal stable guy aren't you, getting all pissy over something dumb like that."
    "At this point, I stopped pressing buttons and just stood there listening."
    Student2 "Well what do you want to do then?"
    Student1 "Next time I see her I'll just tell her straight up to piss off!"
    MCT "This guy...he really needs to calm the hell down."
    Student1 "I swear, she needs a real man in her life to make her chill out, though I can't imagine who would want THAT."
    MC "H-hey."
    Student1 "Eh?"
    "Without thought, I spoke up. I know, I've only know Shiori for a little bit, but she's at least seems a bit more respectable than this jackoff...when I realized what just happened."
    MCT "WHAT AM I DOING?! BAIL! BAIL!"
    MC "A-any of you guys got a yen?"
    Student1 "Uh...no."
    MC "Oh, that's ok. Sorry."
    MCT "I absolutely CANNOT just start running my mouth off to some random guy, i've only been here a few days!"
    "Feeling slightly disgusted with myself, I walked to my dorm. I couldn't wait for tomorrow to come. I opened my door and plopped down on the bed."
    MCT "Shiori-san...is she really as harsh as that guy was making her out to be?...No, no she was justified in what she did, he just can't handle getting called out."
    MCT "Well, no point in just dwelling on it, might as well get started on my homework."
    "I pulled out all my materials, pencil, book, empty notebook, eraser..."
    MCT "...Wait...what the?"
    "I looked in my notebook and found nothing. Only a few measly papers sticking out...airplanes are expensive."
    MCT "Damnit! Now I have to go and get a new one. Guess I'm headed out then."
    jump daymenu
    
label AE004:
    scene Dorm Interior with fade
    "I slipped my shoes on as my mind began to mull over the incident in the hall the other day, it was strange, but honestly I just felt a bit ticked off about the whole thing. Was it because they were bad mouthing someone I knew, was it because it was just blatant disrespect towards someone who seems like they work hard, or was it because I didn't say anything? Either way, I was off put enough by the whole thing that I now had a big problem on my hands."
    MCT "I can't believe I forgot to get a new notebook!"
    "The notebook that I had been mulling around with yesterday lay in the bin next to my bed. It was old and used up in the first place, but it didn't help that I used it as a factory for miniature planes."
    MC "Ok, so if I rush, I can get to the store in time to get a new one, get back, and start writing my homework down."
    scene Dorm Exterior with fade
    "I opened the door quickly, and began to head out. If it weren't for my reflexes, I would have ran head first into Shiori-san, hand prepped to knock on the door. I jumped a bit, and took a step back."
    show AE neutral with dissolve
    MC "Uwa! S-sorry, Shiori-san! I was just heading out, I didn't mean to startle you."
    "She appeared a bit surprised for a moment, but quickly regained her original posture as she cleared her throat. She slowly put her hand on a large file she was carrying in her other arm."
    AE "Yes, well, just be a bit more careful."
    MC "Can do. So, uh, is there anything that you need? Is something wrong?"
    show AE angry
    AE "Very much so. I need to see Daichi-san. Is he here?"
    MCT "Oh god, what did he do this time?!"
    MC "Oh, I'm sorry. He left earlier and hasn't come back yet, I have no idea where he went."
    AE "I see. Well, when you do see him, tell him I would like a word with him. Thank you, that is all."
    "Shiori-san had begun to walk away, but my interest had been piqued. At this point I just had to know."
    MC "Hey, Shiori-san?"
    show AE neutral
    AE "Hm?"
    MC "What exactly...did Daichi-san do?"
    if getAffection("AE") <= 1:
        AE "It's a matter between myself and him. There's no need to pry any further."
        menu:
            "C'mon please!":
                $setAffection("AE", -1)
                MC "Really? I mean, I promise I won't tell anyone else, please?"
                show AE angry
                AE "Begging, Hotsure-san? Over something so minor? Pitiful."
                MCT "Yikes! She did NOT find that cute."
                jump AE004_aftertest
            "Ah, ok.":
                MC "Ah! Sorry, I shouldn't pry."
                AE "Indeed. If you wish to know, ask him later."
                MCT "I can already hear him screaming 'Classified information!'"
                jump AE004_aftertest
            "I feel like it's my right to know.":
                $setAffection("AE", 1)
                MC "Well, with all due respect, I feel as if it's my right to know."
                AE "Is that so?"
                MC "Well, I want to make sure that Daichi-san isn't up to no good. I mean, if he's doing delinquent activity, I feel like it would benefit the both of us if I knew, right? That way, I could feel safe about this, and I could be able to keep him in check if I feel he oversteps his bounds. He is my roommate after all."
                AE "Hmm."
                "Shiori-san pondered what I said and, after a short moment, spoke with her answer."
                AE "...Very well. Here."
                jump AE004_testpass
    else:
        "Shiori-san paused for a moment, before turning to me and holding the file out in her hands."
        AE "I suppose if anyone should know, it should be you. Take a look."
        jump AE004_testpass
        
label AE004_testpass:
    "Shiori handed me the file with both hands and then crossed them across her chest, fingers tapping at her forearms as she awaited my response. What I saw was..."
    MC "Daichi's...student file?"
    AE "A printed copy, yes, I had planned to transcribe it onto paper for filing; however do you perhaps notice anything strange about it?"
    "I didn't need to look long to see the problems. His height, weight, and appearance seemed to all be described wrong, his record looked like a cheesy spy movie script, and he even put down that he was from a country that seemed nonexistent!"
    MC "Where the hell is Cobrastan?!"
    show AE angry
    AE "Nowhere, clearly."
    MC "Who wrote this?"
    AE "The student registrar is in charge of obtaining all the information on the students, and everyone I asked seemed to say there were no problems with his profile. I came to...question him."
    MC "Couldn't it be a problem with the registrar then?"
    show AE neutral
    AE "Unlikely. They have a 96%% accuracy rating. A bit lenient, yes, but still effective."
    MCT "So then why...wait...did he change what was in his profile last minute?!"
    AE "Something wrong?"
    MC "N-no. Just some stupid thoughts."
    show AE angry
    AE "I wouldn't be so sure they were."
    MCT "She thinks so too?...Wait, how did she-?!"
    AE "Well then, next time you see him, tell him my concerns and that I wish to see him immediately."
    MC "Can do."
    "Shiori-san took the file back and nestled it between her arm and her hip."
    jump AE004_aftertest

label AE004_aftertest:
    AE "In any case, unless you have any issues to bring up, I have other things to do today."
    MCT "Is there anything I want to bring up to Shiori-san?"
    menu:
        "Nothing I can think of.":
            MC "I should be alright, thank you."
            AE "Very well. Have a good day."
            jump daymenu
        "Bring up yesterday's events.":
            jump AE004_prechoice

label AE004_prechoice:
    MC "Actually...yeah. I do have something that's been on my mind."
    AE "Do tell?"
    MCT "That wasn't right for those guys to just start badmouthing Shiori-san like that after she left. I gotta tell her."
    MC "Yesterday, after you left, I caught a conversation between the group of guys that you had talked to."
    AE "The littering incident? It's been taken care of."
    MC "W-well, yeah, but that's not what I mean. Those guys...they said some pretty hurtful things about you."
    AE "..."
    MC "A-and I was kind of thinking that it wasn't right."
    AE "...And what did you do about it?"
    MC "Eh? Oh."
    menu:
        "I told them off!":
            jump AE004_c1
        "I didn't say anything.":
            jump AE004_c2
        "I was gonna say something, but didn't.":
            jump AE004_c3

label AE004_c1:
    $setAffection("AE", -2)
    MC "I wasn't just gonna let them get away with it! I stood up for you, and told them off."
    show AE angry
    AE "Nngh."
    "Shiori-san put her hand under her glasses and lightly shook her head."
    AE "Why would you do that?"
    MC "Eh?"
    AE "You really have no reason to get involved in my personal affairs. I can handle myself. Did you even think about what could have happened?"
    MC "I'm sorry...I was just trying to look out for you."
    AE "Look out for yourself. The less you meddle, the less work I have to do."
    MCT "Ow...that actually hurt a bit."
    jump AE004_afterchoice

label AE004_c2:
    $setAffection("AE", 2)
    MC "Well, I didn't really say anything. I figured it wouldn't help to complicate things, so I just held my tongue and waited to tell you directly instead of starting unneeded drama. It wouldn't have been professional."
    show AE happy
    AE "...I'm impressed, Hotsure-san. You keep your emotions under check and think things through. That will serve you well. Let's hope you continue this behavior in the future."
    jump AE004_afterchoice

label AE004_c3:
    $setAffection("AE", 1)
    MC "Well...I'm sorry, Shiori-san. I was going to say something, but I...kinda got cold feet and backed off."
    AE "I see. That's ok Hotsure-san. Moments of weakness can be common. Next time, don't even say anything, and things will turn out better."
    MC "I know, I-"
    MCT "Wait...what?"
    AE "I can tell your heart was in the right place, but perhaps leave things to your better judgement, hm?"
    MC "U-uh."
    AE "The only thing I am worried about is that lack of resolve. If you do something, commit to it. That is all."
    MCT "That turned out...ok?!"
    jump AE004_afterchoice

label AE004_afterchoice:
    MC "So...what do you plan to do?"
    show AE neutral
    AE "Nothing."
    MC "?!"
    MCT "So quick!"
    MC "B-uh."
    AE "I'm not going to actively feud with delinquents. Their opinion of me is there's, nothing more. Unless it turns to harassment among students, I have no plans to take up things such as this with administration."
    MC "I..."
    MCT "It can't be helped. If Shiori-san thinks that's best..."
    MC "Yes, Shiori-san. I understand."
    AE "Have a good day, Keisuke-san."
    MC "You too, Shiori-san."
    AE "Oh, and Keisuke-san?"
    MC "Y-yeah?"
    show AE angry
    AE "If the wind blew your planes would have been everywhere...keep that in mind next time, and stay near a bin."
    MC "!!!"
    MCT "Gah! But how?!"
    MC "Y-yes, Shiori-san. I will."
    hide AE
    "I watched Shiori-san as she walked away. She was an interesting one. The way she carried herself was astounding...if not slightly baffling."
    MCT "What is your deal...Matsumoto Shiori?"
    jump daymenu

label AE005:
    scene Hallway with fade
    "I let out a sigh, I wasn't quite sure what I was doing. I don't know why, but I still felt a bit of anxiety after the fact. The raw emotion in the area was overwhelming, there was so much tension from everywhere at once."
    MCT "My hair...? My hair. I mean, it's so..."
    "I looked down at my knuckles. Since puberty, I've had a bit of hair on them. I remember how all the other kids would jeer me for, being hairy here isn't exactly that common, especially as a teen."
    "*Click*"
    MCT "Huh?"
    "I stopped for a moment, caught off guard by the sound of the door in front of me slowly creaking open. I stood there, silently watching as a girl walked out. It was Shiori-san, finaly done with her results."
    show AE sad with dissolve
    MC "S-Shiori-san?"
    AE "N-ng! Hah...*ahem* hello, Hotsure-san."
    MCT "H-her face!"
    "Shiori-san held her head high, but her face and body betrayed her. Her eyes seemed more apprehensive than before. Her face showed a certain embarrassment I'd never seen on her before; her cheeks were puffy, and her face was a slight tinge of crimson. Though her posture was fairly uniform, all the posture the human body can muster couldn't hide her trembling."
    MC "Shiori-san, is everything alright? How did it go?"
    AE "Yes. I...should be alright. I was taken slightly aback by my results..."
    "She gave a deep breath, and though her face still showed a tinge of pink, she appeared to instantly regain her composure."
    show AE neutral
    AE "It's nothing that I hadn't expected, of course. I had a theory on what my situation was, it was just that...having it said to me was a bit more jarring than I would have liked."
    MC "A theory on your type of growth?"
    AE "Essentially, yes."
    MC "How did you know?"
    AE "...I'd already been experiencing some of the effects before I came here. I realized that they weren't attributed to my lifestyle beforehand, though I had been assuming so for a while, so I began to research what it could possibly be. Once I got the transfer notice from the school, it was all but confirmed."
    MC "I see...I can expect that from someone like you, Shiori-san. But if you had an idea of what was going on, then why was being told jarring?"
    AE "Well, having a theory is different from getting a confirmation, and when you're told something like that outright..."
    MC "It's like going to the doctor thinking you have a disease, only to be told that you do."
    AE "Yes, precisely. It's strange, it's as though I had some futile hope in the back of my head that my particular case was less that I was making it out to be, even though it was obvious what it was from the start."
    MCT "I think I know what it was."
    menu:
        "Try and play it off.":
            jump AE005_c1
        "Tell her what you think it is.":
            jump AE005_c2

label AE005_c1:
    MC "Well, uh, ya know, it could be anything. I mean, it's not like-"
    AE "You're a horrible liar."
    MC "...Eh?"
    show AE angry
    AE "It's obvious to anyone what my growth is..."
    MC "Shiori-san...I'm sorry."
    show AE sad
    AE "It's fine. At least you were kind enough to make an attempt...and it's always useful to know your tells when being dishonest. It makes it easier."
    jump AE005_after

label AE005_c2:
    $setAffection("AE", -1)
    MC "It's your butt, isn't it?"
    "Shiori-san looked at me with shock. I could tell she didn't expect me to just come out and say it."
    MCT "Why did I say that out loud?! She just told you hearing it was jarring for her."
    MC "Shiori-san! I didn't mean to just blurt that out, I'm sorry."
    show AE angry
    AE "Y-you!"
    show AE neutral
    AE "..."
    if getAffection("AE") >= 3:
        show AE sad
        AE "It's alright Hotsure-san, I realize that this is a stressful time for us all...yes, you're correct. The growth I came to this school for is my...rear."
        "I looked down at Shiori-sans hips. They were already flared out as it was. I've seen butts like hers from American media and stuff like that, but seeing it on a Japanese girl was still so surreal to me."
        MC "I'm sorry. I didn't mean to be so thoughtless."
        show AE neutral
        AE "I've already accepted your apology, Hotsure-san."
    else:
        "Shiori-san peeked behind her back at her derriere. Almost sheepishly, she grabbed the bottom of her skirt and pulled it down."
        show AE angry
        AE "T-that is on a need to know basis, and I see absolutely no reason why you would need to know."
        MC "Ah! Sorry, Shiori-san."
        AE "Hopefully you have more tact in the future...I'll be keeping an eye on you."
    jump AE005_after

label AE005_after:
    show AE neutral
    AE "However, as you know my growth, I think it only fair for information to be exchanged for research purposes. What is your diagnosis."
    MC "O-oh, um. My hair."
    "Shiori-san's eyes lit up for a moment. She looked down at the ground for a second and then back at me, bewilderment strewn across her face."
    show AE angry
    AE "Hair? But why did..."
    MC "S-shiori-san?"
    "Shiori-san bit her knuckle for a moment in contemplation before returning to her regular demeanor."
    show AE neutral
    AE "It's nothing Hotsure-san. Merely thoughts to myself. As we'll both be growing, I assume there will be a level of...mutual learning at some level between us."
    MC "Mutual...huh?"
    AE "In any case, I can tell that tonight will be a fairly arduous night. I'll be filling out forms for the health committee."
    MC "Ok...yeah, you do that."
    AE "Have a good evening."
    hide AE with dissolve
    "Shiori-san walked away toward the library, holding her skirt with one hand from behind her. As I watched her walk away, I started to contemplate what she said."
    MCT "Mutual learning..."
    if getAffection("AE") >= 3:
        MCT "I...look forward to it."
    else:
        MCT "Yeesh, could she get any creepier?"
    jump daymenu

label AE006:
    scene Hallway with fade
    "The soles of my shoes made a loud, squeaky, and wet patter as I walked down the hall, drenched with the torrential downpour from outside."
    MC "Ugh, why does it always have to rain on days that look sunny in the morning? I'm soaked!"
    "In an attempt to shield myself from the heavy rain, I used the notebook in my right hand. Not exactly my brightest idea."
    MC "Man, the whole thing looks trashed, I just bought this!"
    MCT "I can't believe that it's sogged already. Only a few days with this thing and I've only used it once for...oh god no."
    "As I opened up the notebook, a mix of shock and utter despair began to sink in, as I realized my Calculus homework was reduced to what could only be described as a Jackson Pollock wet dream."
    MC "Are you kidding me?! I spent hours trying to figure this out!"
    MCT "Dammit! This is bad. This needs to be done by tomorrow! This is the only notebook I have...uh, had, and the store is on the other side of campus. If I run over I-"
    show AE neutral with dissolve
    AE "Hotsure-san?"
    MC "AGuaH!"
    MCT "Sh-Shiori-san?"
    "Shiori-san stood with a dark brown umbrella carefully tucked away in a sheath under her arm, her glasses fogged by the moisture."
    MC "A-ah, yeah, hey, hi, Shiori-san. How are you holding up?"
    AE "Fine. You, on the other hand, are drenched, and dripping water all over the halls."
    MC "Huh?"
    "I looked down to see the fair-sized puddle forming around my feet. Before looking back up at Shiori-san's piercing gaze."
    MC "Oh! Uh-"
    AE "Quite the unfortunate predicament for you, Hotsure-san. But, you're in company with many of your peers, it seems."
    MC "What do you mean?"
    AE "Well, you aren't the only one to forget your umbrella, I've seen six students with the same problem; Though I will say you're the first to sacrifice your notebook in the process."
    MCT "She...noticed?"
    AE "Hopefully you don't treat that hair of yours with more respect than your homework all the time, lest you fall behind in your studies."
    "Shiori-san took her glasses off and began to rub them with a handkerchief to dry them. She slowly walked past me as she did and came to a stop in front of the library, she turned her head and looked at me."
    AE "Though this advice comes late, perhaps you should look at the weather reports a day in advance and plan accordingly."
    MCT "I haven't really got a good look at her eyes before. I'd never really noticed but...they are kinda beautiful."
    MC "Yeah...well, there are some things that are hard for anyone to plan for."
    AE "How so? I'd easily looked at the local forecast and prepared accordingly for all variables."
    MC "Wind direction and umbrella coverage don't count, then?"
    AE "What?"
    MC "Your skirt."
    "Shiori-san looked down at her skirt and saw what I noticed. The back of her skirt was wet. Though she held her umbrella in a way to guard herself from the rain, her rear stuck out far enough for it to get rained on."
    "The damp fabric of her skirt clung to her cheeks, showing the faint outline of her panties. Shiori-san bristled up for a moment before putting on her glasses and adjusting her skirt."
    show AE angry
    AE "I...hadn't taken into account my...changing dimensions. Besides, I would prefer if you kept your wandering eyes to yourself."
    MC "O-oh, sorry, Shiori-san!"
    MCT "Now I remember. Shiori-san the other day, when we got our reports back, was shown that her butt was getting bigger, right? Man, talk about the short end of the stick...I mean, it was big before, but to think that already freakishly huge butt of hers is only gonna swell..."
    show AE neutral
    AE "It's fine, Hotsure-san. Now, if you will, I have paperwork to do."
    MC "Ok. I'm gonna run down to the store."
    AE "Wait, run?"
    MC "Yeah, I mean, I don't wanna get more wet than i'm about to, right?"
    show AE angry
    AE "Absolutely not."
    MC "Right, so I'll put this over my head and go get another one, put it under my shirt and-"
    show AE neutral
    AE "No, I mean you aren't running outside in this rain. You could slip outside and hurt yourself, plus you got lucky by not getting mud all over your shoes, don't test that."
    MC "I don't know what else to do, my notebook is ruined and I need paper to do my homework."
    AE "Hmm...very well. Come with me."
    MC "Huh? Why?"
    AE "There is paper in the office room, you can use some of it."
    MC "Really? Awesome, thanks."
    AE "Just don't make too much of a ruckus."
    "Shiori-san and I walked into the library and over to the door of the office. She pulled out a key from her pack and unlocked the door, flicking on the lights as she entered the room."
    scene Office with fade
    show AE neutral
    AE "One moment. I'll get the papers with some of the work I need done out first."
    "I leaned up against the wall as Shiori-san began to look through the filing cabinets for papers, I looked at her desk and noticed the obscene stacks of paper piled up."
    MCT "Is she really going though all of that?! It could take months!"
    "My eyes wandered over to where Shiori-san was, and I thought admirably on her hard working nature...and then my eyes began to wander a bit lower."
    "As she hopped on her toes to grab some files on the top of the cabinet, I watched as her big bum began to jiggle ever so slightly. She lifted one leg up, unknowingly accentuating her slightly chubby thighs. My thinking went blank for a moment, before immediately snapping back."
    MCT "Sh-shit! If she saw me staring at her like some kind of perv, she would hate me forever. I gotta keep my cool."
    "Shiori-san turned around as I exhaled a deep breath, holding papers in her hands."
    AE "I apologize. One of my subordinates has been rearranging my files. Here."
    MC "Thanks, Shiori-san."
    AE "Now, if you need me, I will be here."
    MC "Okay."
    "I began to leave, but I had an idea in my head that I couldn't really get out. So I turned back to Shiori-san to say what I needed."
    MC "Hey, uh..."
    AE "Yes?"
    MC "You've really got a lot of papers to work on, yeah?"
    AE "Yes. While usually delegated to multiple members of student organization, I have taken it upon myself to do it all. The other members all seem too scatterbrained in meetings anyways. I swear, it's like they got in through popularity alone."
    MC "Well, I've been thinking. Maybe I could help."
    AE "What?"
    "Shiori-san seemed to be taken aback from my statement for a moment."
    if getAffection("AE") < -3:
        show AE angry
        AE "I apologize, however I think you misunderstood my gesture by giving you paper. I didn't want you to run around outside because the school would be liable. I have no intention of spending any more time with you than I need to."
        MC "Oh...I mean, I just wanted to help."
        AE "I'll take my chances with one of the other members should the need come. Good day."
        MCT "Ouch...well. I guess that's that."
        jump daymenu
        #(The future routes are based on this scene...so I guess route locked? IDK I guess I'll just have to figure something out.)
    elif getAffection("AE") > 2:
        AE "Perhaps...it would be better if I had someone with me. From what I gather, you seem competent and responsible."
        MC "Thank you. And if anything, it will make your work be done more efficiently."
        AE "I see. I must admit, Keisuke-san, in the short time I've known you, you've proven to be quite a driven person. Very well. I will see to it that you will begin to work under me after class ends. Do your best to not miss a day, will you?"
        MC "You have my word, Shiori-san. See you tomorrow."
    else:
        AE "I...no. I can manage this by myself."
        MC "Oh. Um, I didn't mean to say that you needed my help. Just that I think, y'know, it would get done more efficiently."
        AE "..."
        "Shiori-san sat in contemplation for a moment. She brought her thumb up and lightly bit on the end of her fingernail."
        AE "...Very well. If anything, I'll be doing a service to the school by helping you prepare for the outside world."
        MC "Thank you, Shiori-san! I promise, you won't regret this."
        AE "I certainly hope not."
    scene Hallway with fade
    $setFlag("AE006_helpinginoffice")
    "As I left the library, I gazed out the window. The rain had passed into to a soft drizzle on the horizon as the sun's golden rays began to peek through the clouds. As I walked outside into to fresh air, the smell of petrichor hit my nose as I began to ponder how I would spend the rest of the day."
    jump daymenu

label AE007:
    scene Hallway with fade
    "I briskly strode towards the Library, backpack slung across my shoulder as I prepped for a day to do some extra work. Today was the day I promised Shiori-san I would help her with her paperwork, at least, the day she would introduce me to it. As I turned the corner to the Library entrance hallway, the punctual girl came into view, waiting outside the door."
    show AE neutral with dissolve
    MC "Hey, Shiori-san!"
    AE "Hotsure-san, good afternoon."
    MC "So, ready to get to work?"
    AE "Are you?"
    MCT "That...felt more like a challenge than a little small talk from her."
    MC "Yeah. Definitely."
    AE "Good. I've made ample preparations for today's work, and I estimate that I would be able to finish before sunset."
    MCT "Sunset?! That stack the other day looked like it would last waaaay past sunset."
    MC "Ample preparations? Aren't we just filling out forms?"
    AE "There is more to my job than filling out forms, Hotsure-san. You, however, will be working on filing the forms."
    MC "Sounds easy enough!"
    AE "Well then, let's head in."
    scene Office with fade
    show AE neutral
    "We walked into the library and headed to the student council office. Shiori-san unlocked it with a key and flipped the switch on; filling the room with the soft whir of the fluorescent lights. Shiori-san sat down at the table and began to pull assorted items from her bag, stamp, pens, pencils, and a menagerie of different folders."
    MCT "I have to make a good impression. I don't want her to think I'm just some lazy bum who can't hold my own!"
    MC "So, I'm ready to get started! Got anything for me to start off with?"
    AE "Yes. If you would please, sign this."
    "Shiori-san handed over a thick packet of papers to me. Just by looking at the front page, I saw a pool of legal jargon and terminology."
    MC "Um...Shiori-san...what is this?"
    AE "A form that states that you are here assisting me on your free will and accord, as well as a contract stating that you intend to follow the standard rules and procedures set up by the school constitution while working under me."
    MC "Wow...the school administration has a contract like this just to help with the forms?"
    AE "No. I wrote it myself last night with the approval of the administration. It also contains the terms of our cooperation, so that there is no confusion on the nature of this agreement."
    MC "...Shiori-san."
    menu:
        "Ok, I'll sign it.":
            jump AE007_c1
        "No way!":
            jump AE007_c2

label AE007_c1:
    $setAffection("AE", 2)
    MC "Well...sure."
    AE "You don't plan on reading through it first?"
    MCT "THIS beast?!"
    MC "I trust your judgement. If you made it, I'm sure everything in the contract is agreeable. If I ever get confused I can just refer back to it."
    AE "...Well then, thank you for placing your faith in me."
    "I signed my name on the line provided and handed it back to Shiori-san, who put it in one of her folders for safe keeping."
    jump AE007_after

label AE007_c2:
    $setAffection("AE", -3)
    AE "...Well?"
    MC "I'm not signing this."
    show AE angry
    AE "...Mind explaining?"
    MC "I mean, I promised to help, shouldn't that be enough?"
    AE "The contract is a simple agreement stating that-"
    MC "Right, but it's not truly official. I shouldn't be signing things that the school hasn't explicitly made necessary."
    AE "...Very well. I suppose it is unnecessary, then. However, know that I have the clout to terminate your help at any time."
    MCT "I feel like...I might regret not signing that."
    jump AE007_after

label AE007_after:
    show AE neutral
    AE "Well, in any case, as you can see there is a lot of work to be done. If you work efficiently, we may be able to return to our dorms before sundown."
    MC "Right. I'll get to work on filling these out."
    AE "Absolutely not."
    MCT "Ehhhh?"
    MC "But you said-"
    AE "I told you that you could file the forms, not fill them out. These deal with sensitive student information. Your job is to put the forms I finish into their respective filing cabinets."
    MC "Then...will I really be helping at all? If all i'm doing is filing the files, then it would still take months to finish all of that, let alone by sundown! All i'd really be doing is shaving a minute or two off of your workload."
    AE "Keisuke-san, there are two things you're underestimating; my ability to sort documents, and the value of a minute or two."
    MC "...Ok, I guess."
    scene black with fade
    "We got to work, and Shiori-san began filling out forms at neck cracking speeds. Every other minute was the sound of scribbling, stamping, and then sliding a paper to me. I nearly choked for a second, before taking the files in hand and bringing them to the cabinet."
    "The names went on and off the desk like lightning, and it honestly felt like for every paper I would take off the desk and file, two more would take it's place. A document hydra. By the time the stream stopped, I was nearly panting from the quick, bustling motion of it all."
    "The scribbling and stamping had stopped now, and as I grabbed the last few files, I looked back on the pile of files and I realized..."
    scene Office with fade
    MC "They're...gone?"
    AE "Yes, Hotsure-san. I filled them all out."
    MC "B-wha-I-"
    AE "As I said, removing the time to sort the files increased my productivity drastically. I thank you for that."
    MC "Huh...oh...OH! Yeah! It really did!"
    AE "Enough so that we aren't even close to sunset..."
    "Shiori-san let out a sigh, and with a sullen look walked over to the filing cabinets."
    MC "Shiori-san? Is everything ok?"
    show AE angry
    AE "My estimate was wrong for the time needed, which can only mean one thing; you worked faster than my estimate."
    MC "Oh! Thanks, Shio-"
    show AE neutral
    AE "It's my fault, I asked you to sort the files without teaching you a proper method."
    MC "Eh?"
    "I looked down at my “handiwork” and a feeling of absolute despair washed over me."
    MC "EEEEEHHHH?!"
    "Files were strewn about and placed incorrectly in their folders, there were crumpled messes of paper smashed into the areas between folders, and what's more, I had placed poor Haruno-chan into the wrong cabinet, oh god the humanity!"
    MC "Oh man...Shiori-san, it was my responsibility, and my fault. I should have been paying attention."
    AE "It's fine, Hotsure-san, I can fix this easily. It will take a bit after sundown to do so, but I can."
    MC "I...I should go."
    "I began to walk out in solemn silence; after messing up this bad, I shouldn't be trusted with even simple stuff like this. Then, from behind me, I heard Shiori-san say something."
    AE "Pacing." 
    MC "Huh?"
    AE "Your problem is pacing. I plan on rectifying that. I will have plenty of files tomorrow to work on as well, I hope you will be there."
    MC "Shiori-san...thank you. I will."
    AE "Hm."
    scene Hallway with fade
    "I walked out of the library, my hope restored with plans for the next time. Until then, I gotta figure out the rest of the day."
    jump daymenu

label AE008:
    scene Office with fade
    show AE neutral
    "Today was the second day I went to the office with Shiori-san. I kind of felt like I was missing out on a bright, sunny day, but at least I could redeem myself for the other days failure."
    AE "Remember, steady breathing. No matter how quickly you receive files, double check to make sure that everything is in order."
    MC "Got it."
    "Today started off much the same as yesterday, but as promised, she was intent on teaching me “proper filing methods”. It started off with me looking on uninterested, but over time, surprisingly, I actually got invested."
    AE "And here, unless it's the only available cabinet, avoid the ones at the very top and bottom. If you take the middle rows to be the most often used, you won't need to spend extra time and effort bending over or standing on your toes."
    MC "Yeah, I can see how that would help. It looks like you've already moved the paper from the other day."
    AE "Indeed."
    MC "So, how long did all of that take? Putting the files back in the right places?"
    AE "Twenty minutes or so. However, that also involved re copying papers that you crinkled."
    MCT "Oh...right. Man, first day and I actually ADDED work instead of helping. Shiori-san must either feel sorry for me, or really care about me to keep me around..."
    MC "Sorry again. I know it must be a pain having me here."
    AE "Not at all, it's somewhat reaffirming to have someone here of their own volition. It shows you care about the inner workings of the school."
    MCT "That's a VERY generous depiction of me."
    AE "So, all in all, I believe I've given you what you need to be able to sort the files correctly. Use the new method I showed you to sort these files on the desk."
    MC "Got it..."
    MCT "Wait."
    MC "Shiori-san, did you have these pre-prepared for me to work on?"
    show AE happy
    AE "Ah, observant of you, Hotsure-san. Yes. I came in early this morning and filled out some forms in anticipation for your training."
    MCT "Early this morning? How did she get all of these done before class?"
    MC "Oh, uh, thanks Shiori-san, but...how early did you wake up?"
    show AE neutral
    AE "Around five thirty."
    MCT "Five thirty?! Is she insane?!"
    MC "Wow...um, that's...dedication?"
    AE "Thank you. Now, if you will."
    "Shiori-san made a hand motion over to the papers. I could tell that the lack of productivity was making her antsy."
    MC "Ok, what will you do?"
    AE "I have to stamp these documents with the school seal. Feel free to ask for help if you need it."
    MC "Will do."
    hide AE with dissolve
    "I got to work on the filing, this time taking things in stride. Every few seconds, I could hear the click of a stamp pushing down on paper."
    "*K-chk*"
    "It started off as just background noise, but as time went on it felt more like a rhythm, reminding me to keep pace. It worked pretty well...for a bit. Shortly after the student's bane began to set in, the dreaded foe of all academics...boredom."
    MCT "Seriously, how does she just do this day in and day out?! It's killing me."
    show AE neutral with dissolve
    AE "You're stalling. What's wrong?"
    MCT "Ah, I guess she noticed. Well, maybe a bit of conversation will help."
    MC "Hey, Shiori-san, not to seem like I don't like being here, don't get me wrong, it's just...is this it?"
    AE "It? Yes. But “It” is an important task that must be dealt with care."
    MC "I know, but like...do you do anything while you work or is that, I dunno, distracting?"
    AE "Well, I usually just sit in silence. The office is often empty, so I suppose it gives me some time to myself."
    MC "Doesn't that get lonely?"
    "Shiori-san took a bit to answer, thinking to herself as she stamped away."
    AE "I must admit, it can get somewhat...desolate, for lack of a better term."
    MC "Well, would you like to talk a bit then, or?"
    "Shiori-san stopped for a moment, and began gently nibbling on the end of her thumb nail."
    AE "That depends...it seems as though the monotony is affecting your output, but do you think that you can keep working if we do?"
    MCT "Anything that can stop myself from falling asleep would be a godsend."
    MC "Definitely."
    AE "Very well then. Talk to me if you wish."
    MC "Cool."
    "I continued back on my regular filing patterns, feeling slightly renewed with the new prospect of interactivity."
    MC "So, how are classes going?"
    AE "..."
    MCT "..."
    MC "U-um, are they going well or?"
    AE "..."
    MC "Uh, Shiori-san?"
    AE "Yes?"
    MC "Didn't you want to talk?"
    AE "Oh? You wanted me to talk with you?"
    MC "I mean, having a conversation together is what I was hoping for, yeah."
    AE "Hmm...alright. I suppose it wouldn't affect my work one way or another. You asked me about classes, yes?"
    MC "Yeah, how are they?"
    AE "Perfectly fine. The subject matters are interesting, but there are some things that are a bit...unnerving about the room."
    MC "Like what?"
    AE "The size of the room, as well as distance between chairs, for example. That much free room is somewhat strange."
    MC "Well, I mean, it makes sense. After all it's our homeroom, and they will need to be tailored for, y'know, different conditions and stuff."
    AE "And stuff? Such as?"
    MCT "Eh? Why the intensity all of a sudden?"
    MC "Well, I dunno. I mean, we'll all be growing, so the class seating has to be shifted around a bit just in case, right?"
    show AE sad
    AE "...Yes...I'm well aware."
    MC "I don't think I'll be needing to shift around that much, but I mean, you sit right in front of me."
    show AE neutral
    AE "Ye-"
    MCT "...huh?"
    "Shiori-san stopped for a moment, moving her hand a bit closer to her mouth before hesitating. It was faint, but she was lightly blushing."
    show AE sad
    AE "Behind me..."
    MC "Shiori-san? Did you forget?"
    AE "N-no. I merely thought of some things that I...hadn't previously taken into account."
    MC "Uh...ok?"
    AE "I can trust you to..."
    MC "Huh?"
    MCT "Tooo...?"
    show AE neutral
    AE "Never mind. It's of no importance at the moment."
    MCT "Shiori-san doesn't seem like one to leave a thought unfinished...is everything ok?"
    MC "Hey, Shio-"
    AE "You've stopped filing, Hotsure-san."
    MC "Hm? Oh! Sorry, I forgot."
    AE "It's fine, it seems as though you're nearly done anyway."
    MC "Eh?"
    "The stack of papers I had been filing had been thinned down without me noticing. It seems as though her 'training' paid off."
    MC "Ah! H-hey! Yeah, I did it! And I think...Yep, all placed correctly!"
    AE "I've finished as well, so I suppose we can call it a day."
    MC "Alright. Ready to head out?"
    AE "Mm, you go on ahead. I'm going to double check your work and make note of a few things in the office."
    MC "Oh, ok. See you later, Shiori-san!"
    AE "Indeed."
    scene Hallway with fade
    "I walked out of the office door and into the library, ready to finally get some fresh air and sunlight...well, until something hit me. I was at the door of the library when I was hit with a wave of curiosity."
    "Call it a compulsion, a random stroke of unease, whatever, but for some reason I had a suspicion about Shiori-san after I left. I realize that most would consider it crazy, even a bit creepy, but I felt the need to take a quick look back at Shiori-san before I left. Walking up to the office window, I peeked in."
    MCT "Shiori-san? What is she...?"
    "Shiori-san wasn't working. She was standing up. Her hands reached down to the sides of her hips as she looked back at her rear. She was staring at the far wall when I heard her speak."
    AE "Stand...Bow."
    "Shiori san bent over, bowing to the invisible teacher...when she looked back. Her back was arched, and it was impossible not to see her twin mounds, covered by her blue skirt, sticking straight out to see. She looked back, put her hands on her butt and squeezed as the color drained from her face."
    "I dared not look any more, for fear of being seen, and quickly left the library prepared to face a the rest of the day, admittedly, with a new level of concern for my classmate."
    jump daymenu
    
label AE009:
    scene Hallway with fade
    "The sound of rubber squeaking against the laminated floors echoed as I ran down the hall. I briskly rounded the hallway corner, just barely missing another student."
    MCT "Damnit, Diachi! You just had to play that homemade documentary, didn't you?! Shiori-san is going to tear me to shreds!"
    "I hadn't been keeping an eye on the time. I went back to my dorm to grab a bite to eat before I went to the office, but as soon as I got in Daichi decided it was a good idea to sit me down to show me a video he made about the how the School profits are being diverted to some shady Biotech company that I'd never heard of."

    scene Office with fade
    "I slowed down as I neared the library door, composing myself before entering. I made my way through and entered the office, where Shiori-san was writing a report of some kind."
    show AE neutral with dissolve
    AE "There you are, Hotsure-san. I wanted to-"
    MC "I'm really sorry I'm late."
    "Shiori-san winced for a moment, and then replied after a few seconds."
    AE "...It's fine Hotsure-san, just try to be more punctual in the future."
    MC "I hurried to head over here as soon as I-"
    MCT "GAK! DON'T SAY HURRY!"
    show AE angry
    AE "...You didn't run to get here, did you?"
    MCT "Eeeeeehhhhh."
    MC "Kind of?"
    AE "You-w-nghh. Nevermind. I had something I wanted to ask you about first."
    MC "Already? You don't want me to start working to catch up?"
    show AE neutral
    AE "It can wait. I need you to answer this."
    MCT "Woah...Shiori-san is being really serious with this. It must be important."
    MC "Oh. Okay, sure."
    AE "When we do the morning introductions, is my...growth a problem?"
    MC "Um...what do you mean by problem?"
    AE "Is it distracting to you? Unsightly? If you find the situation unsettling I will take precautions to stop it."
    menu:
        "Absolutely not.":
            jump AE009_c1
        "Yes, but it's fine":
            jump AE009_c2
            
label AE009_c1:
    MC "Not at all. I mean, I usually close my eyes whenever I bow, so it's no big deal."
    AE "Hm... I suppose that if we all bowed at the same time it wouldn't be too much of a problem."
    MC "Exactly. You can rest assured that I'm not..."
    extend " You know, gawking."
    AE "Good. I didn't want to have to file a request for seat transfer. However, since it seems as though it won't be affecting you no action will need to be taken."
    jump AE009_after

label AE009_c2:
    MC "Well, I guess in a way it is kind of distracting, yeah. But, I wouldn't say it's that big of a deal."
    if getAffection("AE") >= 4:
        $setAffection("AE", 1)
        show AE sad
        AE "Getting distracted isn't a big deal? Hotsure-san your academic standing is one of my top priorities, if for any reason you feel distracted I would not hesitate-"
        MC "Shiori-san, it's fine! Really. I should be apologizing for not paying attention."
        AE "Hotsure-san, you don't need to say things like that. It's my duty as class president to make sure that you are given an efficient learning environment."
        MC "But it's mine as an individual to adapt to situations. You don't need to take any precautions for my stumblings, besides, I can learn responsibility by reminding myself to keep focused."
        "Shiori-san seemed conflicted for a moment, in not slightly agitated. She let out a sigh and nodded."
        show AE neutral
        AE "Right. Well, that's that then."
    else:
        $setAffection("AE", -1)
        AE "How so?"
        MC "Huh? Oh, well, I notice it a lot, but it's not like, that big of a deal. I mean, it's normal to stare a bit."
        "Shiori-san looked at me with concerned eyes, her brow furrowed in a mix of confusion and what felt like a hint of contempt."
        show AE angry
        AE "Well, if you would please, cease that behavior. If you get distracted it makes the class look bad. Furthermore, I would appreciate that you didn't...gaze at me in the manner that you're implying."
        MC "O-oh! No, no, no, I didn't mean it in that way. I meant more like, it's abnormal to see someone with a body like yours and...I..."
        MCT "Rest in peace Hotsure, you blithering idiot."
        AE "..."
        AE "Just...just make sure that you correct yourself, good?"
        MC "Yeah."
        show AE neutral
        AE "Well, I suppose I won't be needing this then."
    jump AE009_after

label AE009_after:
    "Shiori-san took the piece of paper she had until recently been filling out and folded it twice before carefully placing it in the waste bin."
    AE "So, shall we get to work?"
    MC "Yeah."
    "Like before, Shiori-san wrote away while I took the files she filled and put them in the correct cabinets."
    "I was just about to get done with my first stack when I head Shiori-san speak up from behind me."
    AE "So...Is there anything on your mind?"
    MCT "Any...huh?"
    "I was taken aback for a moment, before realizing what had happened. Shiori-san wanted to start a conversation."
    MC "Sh-Shiori-san?"
    AE "Well, you said that having a conversation helped you work efficiently, yes? Then let's begin."
    "I couldn't help but smile a bit, I hadn't expected this, so I scrambled for a conversation topic really quick."
    MC "So, the academy itself, what do you think?"
    AE "Can you be specific?"
    MC "Well, how does it compare to your old school?"
    AE "Seichou is far better. So far I've only had to deal with minor infractions every now and then."
    MC "Barring the whole, you know, thing with those guys a while ago?"
    AE "Including. It was supposedly nothing but childish comments, I'm used to dealing with that."
    MCT "I guess she's right, getting flak for being the class president should be kind of expected...but wait."
    MC "Used to it? So, you've been in a position like this before?"
    AE "Of course. If I hadn't, and hadn't been good at it, I wouldn't have been chosen to be the class president by the school board."
    MC "Oh yeah. I heard that it was an abnormal election, for the most part. No one wanted to step up aside from you."
    AE "Indeed. Actually, if we can go back to the topic of infractions, I would like to know why you were late."
    MCT "Oh boy, here we go."
    MC "Daichi. Enough said?"
    AE "No."
    MC "Oh. Well, uh, Daichi-san kinda forced me down and had me watch a video he made about a conspiracy he thought up."
    show AE sad
    AE "...I truly do not envy you."
    MC "Right?"
    show AE neutral
    AE "What he needs is strict discipline, and I swear I will bring it right to him once I have justification."
    MCT "Yikes. This is getting kind of intense. I think I should dial it back a bit."
    MC "S-so yeah, uh, you like this school better than your last? That's good. And, you know, I think the reason why the students here have less rules broken and stuff is because everyone is here under...you know, the same circumstances."
    AE "I don't believe that for a second."
    MC "..."
    "The silence hung there in the room, coming out of left field, along with the drastic change in tone from Shiori-san. The way she said that...just didn't feel right."
    "I opened my mouth to say something, when Shiori-san spoke up."
    AE "Well now, Hotsure-san, it seems like you're nearly finished with the stack."
    MC "O-oh, yeah! Just a few more left after this."
    "Shiori-san layed down a few more pages which I picked up readily, preparing to place them in the final slots."
    MC "Two aaaand, done."
    show AE happy
    AE "I must say, Hotsure-san, you're getting very good at this."
    MC "Actually, yeah, I'm really feeling like i'm getting my stride here."
    show AE neutral
    AE "Glad to hear, because I have these."
    "Shiori-san plopped down a second pile on the desk in front of me, around twice the size as the last."
    MC "Shiori-san...what are these?"
    AE "These are the second batch that I also had done before you came."
    MC "U-um, Shiori-san? How am I supposed to file all of these?"
    AE "Consider it your punishment for your tardiness."
    MCT "EEEEHHHHHH?!"
    MC "A-are you sure? I mean, it could take all day! You wanna go home too, right?"
    AE "I can wait."
    
    show black with fade
    "After facing a hellscape of papers, I finally got to leave...once Shiori-san had enough pity for me to let me go."
    jump daymenu
    
label AE010:
    scene Hallway with fade
    "I walked down the hallway, getting ready to meet Shiori-san at the office. I heard that shipping and processing had been getting a lot of orders recently, so I figured that today would be a busy one."
    "I assumed, however, that was the reason for Shiori-san’s absence from class, something I would have never expected."
    MCT "Hmm? Wait...Shiroi-san?"
    "Shiori-san stood by the entrance to the library, holding a stack of yellow sheets in both arms. The spectacled girl had her back against the hallway wall, looking at me from the side."
    MC "Hey, Shiori-san! Have you been waiting out here for me?"
    show AE neutral with dissolve
    AE "Good day, Hotsure-san, I had to get these papers from inventory, so I figured we would meet here around the same time."
    MC "Need me to get those?"
    "Shiori-san stepped back a bit when I put my hands out."
    AE "N-no, it's fine."
    MC "Okay, then. Here, let me get the door."
    "I held the door for a bit before Shiori-san looked at me with determined eyes."
    AE "You go first."
    MC "Um...Alright then."
    
    scene Library with fade
    "We walked through the library, Shiori-san following closely behind me, until we reached the office door."
    MC "Want me to take those, so you can unlock it?"
    show AE neutral with dissolve
    AE "Here. The key is on the stack. Take it."
    MC "Okay...? Thanks."
    MCT "That's a bit convenient, isn't it?"
    "Taking the key in hand, I inserted it and turned the knob. The lights were flicked on and I went to my station."
    
    scene Office with fade
    MC "So, Shiori-san, what's with the stack of papers?"
    show AE neutral with dissolve
    AE "These forms are going to processing after they're filled out, don't worry about them."
    MC "Ok."
    MCT "Doesn't really tell me anything, but whatever."
    AE "Right, well, turn around and get to work."
    MC "..."
    AE "..."
    MC " Um...are you gonna start filling some out so I can...you know?"
    AE "There's still some stacks you've yet to file from last time. I can start approving these forms here while you work."
    MC "Oh, ok. I'll just get those then."
    "I moved to go pick up a stack next to Shiori-san, when she sidestepped away. I took it as just a courtesy, but it got strange once she turned to ensure that she was facing me."
    MCT "Okaaaay. That's weird. It's almost like..."
    "I would move and Shiori-san would reciprocate by maneuvering opposite to me. She tried to make her moves subtle, I could tell, but once I started to catch on, it was impossible not to notice."
    MCT "Is she...avoiding me?"
    "Just as a way to test my suspicion, I made an extra effort to walk over to the far cabinet towards Shiori-san rather than just reaching over. Much to my suspicion, Shiori-san backed away slightly."
    MCT "Ok, something is definitely wrong."
    MC "Shiori-san, is everything alright?"
    AE "Yes, Hotsure-san. Keep working."
    MC "It's just that you seem a bit different this morning."
    MCT "Shiori-san stiffened up a bit, turning further a bit. She brought her thumbnail up to her mouth."
    show AE sad
    AE "Oh...really? How so?"
    MCT "Why is she so apprehensive? Well, more than usual at least."
    MC "I dunno, it's just that you aren't the same as the last time we talked, is all."
    AE "Yes, well...I suppose that we're the same in that regard."
    "Shiori-san pointed at my head in the same way one would when trying to tell someone there was something on their face."
    MCT "Huh? What is she...?"
    "I looked off the the side to catch a glimpse when I saw it."
    "Completely going unnoticed by me until now, my hair was definitely longer. Feeling around the back of my neck, I noticed that it went past my nape at this point, and flowed to bottom of my neck."
    MC "Wait...how did this? When did it get this long?"
    show AE neutral
    AE "You never noticed?"
    MC "No, I..."
    "I sat in confusion for a moment, trying to get a full grasp of just how my hair had grown this long without my knowledge, when I noticed Shiori-san quietly sit down and face her back to the wall. That's when it hit me."
    MC "Shiori-san...are you also?"
    AE "...Also what?"
    MC "Well, if my hair has grown like this for the relatively short time I've been here, then...have you also?"
    "Shiori-san shrunk back a bit, eyes intently glaring at me."
    MCT "I'll take that as a yes."
    show AE sad
    AE "Well..."
    MC "And that's why you've been hiding your back."
    MCT "Now that i'm saying it out loud, I'm starting to realize how dumb I was for not noticing it earlier."
    if getAffection("AE") >= 4:
        "Shiori-san winced a bit when she realized that her gambit had been called, then, finally resigned to the inevitable"
        show AE sad
        AE "...Yes. Yes it is."
        "Shiori-san let out as sigh. Of relief or frustration, I couldn't really tell."
        AE "Well, if I keep trying to hide myself then it seems neither of us will be able to get our work done."
        AE "So I want you to...get it out of your system now." 
    else:
        "Shiori-san looked at me fiercely, an angry scowl spread across her face in return for what she took as grave disrespect."
        show AE angry
        AE "N-now hold on! I would recommend you keep your comments to yourself."
        MC "Shiori-san?"
        AE "My personal affairs are my own, and if I choose to...evade your gaze, I have every right to."
        MC "Sorry, I didn't mean anything by it."
        AE "Look. Just get it out of your system now so we can continue our day."
    "Shiori-san took her back away from the wall and finally did it."
    MC "Out of my system? Shiori-san, I'm not going to insult y-"
    "Shiori-san finally turned around."
    #TODO: Zoom-in or CG or something?
    MC "W-HOA MY GOD!"
    "I took the full force of the sight at once. Shiori-san's skirt did little to hide her gigantic behind, tears appearing along the seams showed small glimpses of pale and taut skin as the fabric squeezed her rear, only leaving a scarce inch between the bottom of her butt and the fabrics end."
    "Both cheeks were blown up to the size of full balloons and stuck out a foot from her back, creating noticeable creases along the top of their curvature. Shiori's shelf-like hips stuck out from her sides to match her astounding ass, taking her poor skirt to it's limits in order to cover her shame."
    "Her legs, though, didn't receive any such mercy. Her thunder thighs were in full view, as the girl could do nothing but show off her fat, chubby legs in embarrassment, her knee being the only respite until reaching her calves, which had curiously seemed to had swelled a bit too."
    MC "Shiori-san! Y-you, you're huge!"
    "Shiori-san turned around, blushing furiously as she brought a hand to the side of her face to avoid eye contact."
    show AE sad
    AE "..."
    MC "I mean...oh my god!"
    if getAffection("AE") >= 4:
        AE "I get it, Hotsure-san."
    else:
        show AE angry
        AE "I get it."
    "Her response served as a reminder of the situation was in, as well as the inappropriate nature of my words."
    MC "Oh! No, I mean, well...sorry."
    show AE sad
    AE "..."
    AE "It's fine, Hotsure-san. I realize that it's...off putting, but now that that's over, we can continue work uninterrupted."
    MC "Y-yeah."
    "I got to work on the stack of last time's papers. An awkward silence permeated the room as we both tried to get over what had just happened. I kept trying to focus on my job, but my mind kept racing back to the image of Shiori-sans rear."
    MCT "Damn it, how was that supposed put my mind at ease again?!"
    MCT "I gotta at least try to start off a conversation, if I don't I'll be standing here all day."
    MC "Did..."
    show AE neutral
    AE "Hmm?"
    MC "Did that happen over night?"
    show AE sad
    AE "...I don't believe so. It's just that I need a larger uniform and I've yet to get one, is all."
    MC "I would have figured that you would ordered early."
    AE "I did. As it so happens there was a backlog."
    "Shiori-san took another stack of yellow papers and placed them on her desk."
    show AE neutral
    AE "This is the backlog."
    MC "So, that's what those were."
    show AE angry
    AE "Yes, and the sooner it's done the sooner I can get out of this embarrassing situation."
    MC "So, what, then students just have to wait until their clothes get too big?"
    show AE neutral
    AE "Well, yes, however the School has a partnership with a local tailor. If you pay a premium then you can get your clothes fixed at any time."
    MC "Oh, really? I didn't know that."
    AE "Most students don't, to be honest. That's why the student council is thinking of ways to get the message out."
    MC "Why don't you do that? Get your clothes fitted?"
    show AE sad
    AE "..."
    "Shiori-san sat in silence for a moment, but spoke up again after a brief period."
    show AE neutral
    AE "I would have to fill out more forms then. My clothes aren't as high a priority as my work."
    MC "They seemed pretty high priority..."
    MCT "I shouldn't get into it."
    AE "What?"
    MC "Nothing."
    AE "Hm."
    "We kept working for a bit, until Shiori-san put her pencil down and stacked the papers."
    AE "There. Forms filled."
    MC "Oh, cool. Should I keep working?"
    AE "No, actually, I think that should be it for today. I need to get these back to processing."
    MC "Ok. I'll head out too then."
    "I closed the file cabinet, and prepared to head out, backpack in tow, when Shiori-san stopped me in the middle of the room."
    AE "Wait, Hotsure-san, before you go..."
    MC "Hm? What's up?"
    show AE sad
    AE "I think it goes without saying, but...could you not bring up earlier to anyone? I showed you...why I was worried in order to ease your mind, nothing else."
    MC "Oh, don't worry about it. It's okay, I mean, as long as you don't go around talking about my rat's-nest hair."
    show AE neutral
    AE "I won't."
    MC "Cool."
    scene Library with fade
    "As we walked out, I couldn't help but catch a glimpse of Shiori-san's butt. It wobbled as she shuffled along, swishing side to side as the bottom of her skirt fabric swayed with her movements."
    MCT "H-hey, c'mon man, don't."
    "My eyes snapped back up to attention, thankfully keeping me from running into the library door frame. I walked out, and headed into the hall to continue my day."
    jump daymenu

label AE011:
    scene Hallway with fade
    MC "Oy! Shiori-san. How's it going?"
    show AE neutral with dissolve
    AE "Perfectly fine, Hotsure-san. Just getting some papers for the printer."
    MC "O-oh, yeah! Cool."
    MCT "Cool? Really?"
    if isEventCleared("AE010"):
        jump AE011_010followup
    else:
        jump AE011_no010

label AE011_010followup:
    "I was trying my best to conceal my awkwardness, but by looking at Shiori-san, the mental image of her big behind kept lingering in my mind."
    MCT "C'mon man, get a grip. You saw a girls clothed ass. Big deal. If you make it awkward then-"
    "My thought was cut short by the sound of Shiori-san clearing her throat."
    MC "Huh?"
    AE "I hope I wasn't interrupting any important thoughts, however we should be heading in if we're to get our work done on time."
    MC "O-oh, yeah. Sounds good."
    "Shiori-san opened the doors of the Library, holding it for me to enter."
    scene Library with fade
    "As we walked, Shiori-san muttered something under her breath. It was low enough for me to not hear, but I know something was said."
    MC "U-um...Shiori-san?"
    show AE neutral with dissolve
    AE "Hm?"
    MC "What was that, just now?"
    AE "..."
    AE "I assume...you kept your end of the bargain?"
    MC "The...?"
    AE "From the other day."
    MC "I don't...know what you're talking about."
    if getAffection("AE") >= 4:
        "Shiori-san turned around with a slight smirk on her face."
        show AE happy
        AE "Ah, I see. Very astute of you, Hotsure-san. You're diligent."
        "I responded with a smile and nod of my own."
        MC "Always."
        "As soon as Shiori-san turned around my smile immediately dropped into a look of confusion."
        MCT "What was that abo-"
        MCT "Oooohhh. The promise, not to talk about...yeah."
    else:
        "Shiori-san let out a sigh, and stopped in place."
        show AE angry
        AE "You forgot, right?"
        MC "The...uh..."
        AE "You said you weren't going to dwell on the events of yesterday or tell anyone."
        if getSkill("Academics") > 3:
            $ setAffection("AE", 2)
            MC "I realize, Shiori-san. That's why I've been pretending like I didn't know."
            show AE neutral
            AE "W-"
            "Shiori-san looked on confused for a moment, before slowly giving a small smirk."
            MCT "I did it."
            show AE happy
            AE "A-ah, I see. Very astute of you, Hotsure-san. I'm sorry for doubting you."
            "I responded with a smile and nod of my own."
            MC "Always."
            MCT "I'm unstoppable."
        else:
            MC "I...uh..."
            AE "Ngh...I suppose it's my fault."
            MCT "Ugh...that hurts."
    jump AE011_aftertest

label AE011_no010:
    "My mind was blanking. For some reason, my eyes kept getting drawn to Shiori-san, but I couldn't tell why."
    AE "Well...let's continue. You go first."
    MC "It's alright. You can."
    show AE angry
    AE "..."
    "Shiori-san let out a sigh."
    AE "Hmph. I have a new skirt anyway, so...fine."
    MC "Um...Shiori-san? What does that have to do with anything?"
    show AE neutral
    AE "...Nothing."
    MC "Okaaaay~."
    scene Library with fade
    "We headed into the library, and it was only a short matter of time before I noticed what had changed."
    MCT "I...is her...butt bigger?!"
    show AE angry
    AE "AHEM."
    "Shiori-san cleared her voice loud enough to startle the librarian at the front."
    show AE neutral
    AE "Khm...I apologize. Throat soreness."
    MC "A-ah..."
    MCT "And with that my eyes are front and centre..."
    jump AE011_aftertest

label AE011_aftertest:
    scene Office with fade
    "We entered the room together. The all too familiar whirr of electric lights sounded as fluorescence filled the room."
    MC "Welp. Let's get to work."
    show AE neutral with dissolve
    AE "Let's."
    "The workday carried out today like previous days. Shiori-san and I gave sparing comments here and there as we worked with little actually happening. That's when it hit me."
    "I was bored."
    "It took me a bit of meandering about my work before I realized what today was lacking; human interaction. Sure, Shiori-san and I were talking here and there, but what the words felt empty. I wanted something with substance."
    MC "Hey, Shiori-san, what've you been up to?"
    "Shiori-san slowed from her lightning speed writing in order to acknowledge my question."
    AE "Up to? Do you think I've been planning something?"
    MCT "It wouldn't be a first."
    MC "Well, no, not like that. I mean what all have you been doing?"
    AE "Hm, well, I've been performing the duties of my office."
    MC "...Filling out papers?"
    AE "...Is that all you think I do?"
    MCT "Yes."
    MC "Not to say that you're job isn't rough or anything, it's just that when I see you work it's usually here filling out forms."
    AE "That's for good reason. Much of my work deals with things not open to the public. Student government tends to be a fairly involved undertaking, both inside of meetings and out."
    MC "Really?"
    AE "Of course. Between meetings, monitoring, management, setting up for events, amending and enforcing laws and the ubiquitous peacekeeping duties in the school, filing forms is one of the few moments of quiet I have in the day."
    MCT "It's really sad when your only down time is filling out paperwork. At that rate I'd just become a NEET."
    MC "And you still have some of the top grades in class? I'm surprised you haven't asked me to stay around more often."
    AE "Trust me. If you were a full time assistant, you wouldn't have been so keen to offer your help."
    MC "I dunno about that. It's been fun spending time with you."
    show AE happy
    AE "Well... I appreciate the sentiment, in that case."
    MC "So... what else do you do?"
    show AE neutral
    AE "Hm?"
    MC "You know, outside of class and work."
    AE "There isn't really that much else for me to do. I study different topics that might help me further my knowledge, I suppose."
    MC "Is... is that it?"
    AE "Does there need to be anything more?"
    menu:
        "There is more to life than classes.":
            jump AE011_c1
        "I guess not.":
            jump AE011_c2
            
label AE011_c1:
    $setAffection("AE", -1)
    MC "There is more to life than just going to class, you know."
    AE "Such as?"
    MC "Well... you know, having hobbies, doing something fun, doing something... anything at all?"
    AE "I live by what I must do to ensure my future, Hotsure-san. My duties are to the school, as is my loyalty. To me that's enough to sustain my lifestyle."
    MC "Well, right, but can't you say something that you have done or do that seems interesting at all?"
    AE "..."
    show AE angry
    AE "What are you insinuating, Hotsure-san?"
    MC "Wait, wait, I didn't mean anything by that. I meant, like, what all is there to look forward to at the end of the day?"
    show AE neutral
    AE "I believe I've already answered that."
    MC "A-ah, right, sorry."
    AE "Hm."
    jump AE011_afterchoice

label AE011_c2:
    $setAffection("AE", 1)
    MC "Well, I guess not, really. You live the way you think is best."
    AE "Exactly. I'm glad you understand."
    MCT "Still, I can't imagine that would be any type of life I'd want to live."
    MC "Well...what keeps you going?"
    AE "My obligation."
    MC "Your...obligation?"
    AE "Well, I suppose we all have one. I simply do everything I can to ensure that I'm doing right by the position of my office."
    MC "Hmm...yeah."
    jump AE011_afterchoice

label AE011_afterchoice:
    MC "Still though, I want to know what your interests are."
    AE "My interests?"
    MC "Yes."
    AE "And why are you concerned about those?"
    "I shrugged, not knowing the best way to respond."
    MC "Dch-I guess I just wanted to know more about you."
    "Shiori-san went from my gaze to looking back down at her papers."
    AE "I don't see why. As you can tell I'm not a person with very exciting life stories."
    MC "Well, You don't need to be. I just wanna know what you like and dislike."
    "Shiori-san began to look around a bit, before facing me again."
    AE "I see...and you would like to know?"
    MC "Of course."
    AE "Hmm...okay."
    MC "Great! So first, wha-"
    AE "Next time we work."
    MC "...Eh?"
    AE "I need to prepare some answers to possible questions. Next time, when we are working, you may ask as many questions about me as you like."
    MCT "Eeeehhhh?"
    MC "Why do you...need to prepare for questions about yourself?"
    AE "Well first of all, I want to ensure completely accurate answers."
    MC "...About yourself."
    AE "Yes."
    MCT "Whatever. I can deal."
    MC "Okay."
    AE "Second, you wish to ask multiple questions, yes?"
    MC "Yes."
    AE "Well I suppose if you did so now you would need to do so quickly."
    MC "Why's that?"
    AE "I have a Student Government meeting soon, and from the looks of it...Yes, I'm done with this stack for today."
    MC "Eh...? Already?"
    AE "Indeed."
    "Shiori-san stood up, and pushed her chair in."
    AE "If you don't mind, close up after you've finished filing."
    MC "Oh, okay, sure."
    AE "That should be all, then. Have a good day."
    "Shiori-san walked away from the desk, nearly knocking over a pile of printer paper with her huge rump before firmly walking out the door. I felt bad for it, but I couldn't help but oggle at her new size the whole time."
    MCT "Ugh...c'mon man. If this is how it's gonna be the rest of the year with her, I'm gonna be in for a mind-numbing time."
    "I finished up filing, and left through the library in order to prep for the rest of the day."
    jump daymenu
    
label AE012:
    scene Hallway with fade
    "I strode through the halls, excited and ready to begin my day with Shiori-san, questions running through my head as I wondered what all I would get to learn."
    MC "Good day, Shiori-san!"
    show AE neutral with dissolve
    AE "Hotsure-san? What's with that look? Your goofy smile is somewhat troubling."
    MC "Hah, it's nice to see you waiting for me; as usual."
    AE "...Of course."
    MC "Wanna head in?"
    AE "Mhm, you first."
    scene Office with fade
    MC "Alright. Ready for another day."
    MCT "Yup, another day, another stack of papers."
    show AE neutral with dissolve
    AE "..."
    "However, today had a different air about it than the day before. Today we were finally going to finish up our conversations and I could finally learn more about Shiori-san. There was a bit of anticipation, to be honest, because I could just feel as though I was going to learn something exciting."
    MC "So, today's the day. You promised you would answer any questions I have!"
    AE "I certainly will. Later. Until then, let's get to work."
    hide AE with dissolve
    MC "Eh?"
    MCT "I completely forgot...dang it."
    "I was so excited to start actually getting to know Shiori-san as a person that I forgot about work. It was faint, but I had a small inkling that this may be intentional."
    MCT "Okay. I'm ready. I just need to remember what I'm gonna ask so I don't look dumb. The big ones were sports, music, food. Ok."
    MCT "So, sports, music-ah, food club form, that goes in the left cabinet."
    MCT "Ok, got it. Just need to remember what all I want to ask, and then I'll know her better."
    "We worked, as usual, for minutes on end, throwing the occasional topic to one another. By the time we finished, we were already deep into a conversation once more."
    MC "-and the sight of it is just...ngh..."
    show AE neutral with dissolve
    AE "Really?"
    MC "H-hooo yeah. That's exactly why I hate peanut butter."
    AE "I must say, I have some eccentric tastes but...hm..."
    "We had gotten done far earlier than expected. Surprisingly enough, it felt like Shiori-san had finished hers even earlier."
    MC "So, Shiori-san, you actually seemed to finish up quicker than usual."
    AE "Observant of you, Hotsure-san. It certainly seems that way."
    MC "You need to work on your pacing, young lady!"
    AE "Indeed. Which means that we can begin. You had questions, yes?"
    MCT "Ah, so that's the sound of a joke getting eviscerated."
    MC "Oh, yeah definitely...so, do you have everything...prepared, I guess?"
    AE "Yes. I have everything prepared."
    MC "Ok..."
    jump AE012_menu

label AE012_menu:
    menu:
        "Favorite activity?" if not getFlag("AE012_activity"):
            $setFlag ("AE012_activity")
            jump AE012_activity
        "Favorite activity? (disabled)" if getFlag("AE012_activity"):
            pass
        "Life goals?" if not getFlag("AE012_goals"):
            $setFlag ("AE012_goals")
            jump AE012_goals
        "Life goals? (disabled)" if getFlag("AE012_goals"):
            pass
        "Food?" if not getFlag("AE012_food"):
            $setFlag ("AE012_food")
            jump AE012_food
        "Food? (disabled)" if getFlag("AE012_food"):
            pass
        "Favorite music?" if not getFlag("AE012_music"):
            $setFlag ("AE012_music")
            jump AE012_music
        "Favorite music? (disabled)" if getFlag("AE012_music"):
            pass
        "Favorite sport?" if not getFlag("AE012_sports"):
            $setFlag ("AE012_sports")
            jump AE012_sports
        "Favorite sport? (disabled)" if getFlag("AE012_sports"):
            pass
        "That's everything...":
            jump AE012_after
            
label AE012_activity:
    MC "What is your favorite activity?"
    AE "Outside of class?"
    MCT "No, during."
    MC "T-that's a given, yes."
    AE "...Puzzles, riddles, things that let me test my knowledge."
    MC "Ok...that's it?"
    AE "I suppose so."
    MC "Well, how about games?"
    AE "No. I don't own a television." #FIXME is this true?
    "I did a bit of a double take. I knew she was dedicated to her studies, but not even having a tv?"
    MC "Woah, really?"
    AE "Yes. It's unnecessary."
    jump AE012_menu
    
label AE012_goals:
    MC "Let's talk about goals. What do you want to do after school?"
    AE "..."
    "Shiori-san looked down for a moment to ponder my question."
    AE "I want to be a lawyer."
    MCT "Knew it."
    MC "Aha! I knew it had something to do with rules!"
    AE "Hmph."
    MC "And I was figuring politics, ha ha. So, uh, Prosecution or-"
    "Before I could finish, Shiori-sans eyes turned to me like ice cold daggers."
    AE "I'm sorry to interrupt, but can we change the subject please?"
    MC "O-oh. Okay."
    MCT "Yeesh. Did I hit a sore spot?"
    jump AE012_menu
    
label AE012_food:
    MC "T-the food club form goes in the left cabinet."
    AE "..."
    MC "..."
    MCT "!!!"
    AE "W-"
    MC "What is your favorite food?"
    show AE sad
    "We sat there in silence for a moment. Shiori-san looked at me with confusion and concern, before finally resolving to just answer the question."
    show AE neutral
    AE "A well made bento."
    MCT "...The whole box?"
    MC "...Um...okay? What type of bento?"
    AE "One with a symmetrical and equal distribution of foods."
    MC "..."
    MCT "I think she's missing my question entirely."
    AE "Doughnuts as well."
    MC "Oh, good! Cool, that's a-"
    AE "The circular ones in particular."
    MCT "Of course."
    jump AE012_menu
    
label AE012_music:
    MC "What is your favorite song?"
    AE "Hmm....Ecce Sacerdos Magnus. However, I like liturgical music in general."
    MCT "I don't understand a single word she just said."
    MC "Is that the only genre you'll listen to, or...?"
    AE "No, I also like piano music, as well as organ works. Really it's more the classical music genre."
    MC "Really? Never would've figured you had a taste in western music."
    AE "Mhn, I acquired it while learning to play piano."
    MC "Oh, you play piano?"
    AE "Occasionally, yes, but not recently."
    MCT "Yes! That's something."
    jump AE012_menu
    
label AE012_sports:
    MC "How about sports?"
    AE "None."
    MCT "And here my hopes of wooing her with my few actual skills has been dashed."
    MC "O-oh, really?"
    AE "Hmm...Kendo I suppose."
    MC "Oh, Kendo? Nice."
    AE "Mhm, it's one of the few sports I enjoy watching for long periods of time."
    jump AE012_menu

label AE012_after:
    MCT "Well, I think I got everything I wanted to ask about her."
    "While I'd been somewhat excited for the day where I could learn more about Shiori-san, that excitement had been dashed when I learned something somewhat disheartening."
    MCT "She's not really that boring or anything it's just...nothing abnormal. She has her eccentricities, but all in all she's just kind of what I would have expected. A typical linchou in every sense of the word."
    AE "I'm sensing some disappointment."
    AE "Looking for something you couldn't find?"
    MC "Huh? N-no, I'm not...disappointed."
    AE "Good. So, now that you know about me, I have some questions for you."
    MC "Eh?"
    "Shiori-san pulled out notecards from her breast pocket, and tapped them on the desk."
    AE "Shall we begin?"
    MC "H-hold on, begin?"
    AE "I have some questions for you as well."
    MCT "So that's why she took so long to prepare!"
    AE "Now, shall we?"
    MC "Uh..."
    "I was caught off guard. I wasn't sure hows to respond outside of some small stammers of protest."
    AE "First. Why do you want to spend time with me? Hasn't this been getting boring to you?"
    "Sitting in the chair, there was little I could do aside from just shrug and purse my lips."
    MC "Because I like hanging out with you, I guess. You're cool."
    AE "How so? As far as I know there's never been that much considered 'cool' about me."
    MCT "Your presence maybe."
    MC "I don't know what to tell you. I just consider you an interesting person to spend time with."
    AE "Hmm...And the work? Does it seem repetitive?"
    MC "Well, I guess, yeah. But I figure it's nice spending time here. It's helping me grow as a person."
    AE "Yes...I know you said that, it's just...I suppose your responsibility is something I didn't expect."
    "Shiori-san took her notecard and flipped it to the back, bringing forth the next one in the row."
    AE "Alright then. When you refer to me, you use -san, yet instead of calling me Matsumoto-san, you use first name basis. Why is that?"
    MC "Eh?"
    MCT "Actually, to be honest I hadn't thought of that."
    MC "Well, um, I guess it's because I consider you to be close enough to me to use first names, but since you're...y'know, the president and all that, it's polite to use -san."
    AE "I see..."
    MC "Do you not like it? I can start calling you Matsumoto-san if-"
    AE "N-no, no, it's fine."
    "Shiori-san was about to move to the next card when she hesitated. She then, out of the blue, decided to put them down. Taking a deep breath."
    AE "Let's just get to the point. My main question for you is 'why are you so curious about my interests?'"
    MC "It's good to know about your friends right?"
    MCT "Ah."
    MCT "I think I let that one slip."
    AE "...Friends?"
    MC "Well...yeah."
    AE "I'm...your friend?"
    MC "I mean...we spend a lot of time together and stuff so...yeah."
    if getAffection("AE") >= 5:
        AE "Friend...Hm."
        "Shiori-san adjusted her glasses, clearly not wholly sure how to take what I just said."
        AE "Well..."
        show AE happy
        AE "Thank you, Hotsure-san. I..."
        AE "Hm. Friends..."
        "Something seemed to brighten up in the room. Shiori-sans usually imposing presence felt less severe; it felt like a weight lifting off my shoulders."
    else:
        AE "Hotsure-san..."
        "Shiori-san seemed somewhat confused by the statement, taking it upon herself to avoid eye contact for a moment while adjusting her glasses."
        AE "I appreciate the sentiment, Hotsure-san. Hopefully I can further assist you as a co-worker."
        "Though nothing that she said seemed malicious on the surface, it was the way she said it that formed a deep pit in my stomach."
        MCT "Did I just get coworker-zoned?!"
    MC "So...is that it?"
    AE "I suppose so, yes. Thank you."
    MC "Alright, well, in any case, I'll see you tomorrow!"
    "I began to grab my bags and walk out the door when I heard Shiori-san speak up."
    AE "If...if you are becoming bored with our meetings-"
    MC "O-oh, no, it's okay! I'm perfectly fine just working files."
    AE "Well...in any case, I...Hmm...meet me outside the office tomorrow. Okay?"
    MC "Huh? What for?"
    AE "Well...I suppose you deserve a bit of variety. Plus, it will be helpful for you to see some of the other functions of the student government."
    MC "Other functions?"
    AE "Yes. Please, tomorrow, simply wait for me by the door."
    MC "Oh, ok. Cool. Well, I'll see you then."
    AE "Yes, 'see you then'."
    "I waked out of the office without a clue of what Shiori-san was talking about, but in my mind, any change of pace was a good one. Admittedly though, I came in with plenty of questions and left with plenty more."
    jump daymenu
    
label AE013:
    #FIXME character positioning probably needs work?
    scene Hallway with fade
    "I walked down the halls to my destination, still anticipating what exactly it was Shiori-san had in mind from the other day."
    "As I walked, I saw posters of a smiling anthropomorphic seed, holding out it's fingers in a peace sign. The picture was accompanied with a message in bright, bubbly hiragana."
    "*Don't wait! Apply for refitting today!*"
    MC "Huh, well it looks like they finally got around to putting up the posters."
    AE "N-not quite."
    MC "Eh?"
    "As I looked up to the source of the voice, I saw Shiori-san, standing on her toes while reaching up to apply a poster to an empty wall."
    show AE neutral with dissolve
    MC "S-shiori-san? What's going on up there?"
    AE "Well as you can see, I, nghf...am setting up posters for the refitting, as was discussed earlier."
    MC "Oh! So you all finally...yeah, you got a design."
    AE "Mhm, though it was more of the design accepted by the entire council."
    MC "So you're just setting up for today?"
    AE "Yes. Although, it's moreso that we're setting up for today."
    MC "Ahhh, ok, I see. So this is what was planned for today."
    AE "Mhm, now, if you please, could you grab those stacks over there and move the ladder when I get down."
    MC "Alight, sure."
    "Taking the stacks in my hands, I lifted them up as Shiori-san plastered the posters across the walls. This continued for a few minutes, with small talk breaking up the monotony every once in awhile."
    MC "Well, hey, you were right. Being the president of the student government, really does have a lot to do, eh? Files and posters."
    AE "Hmpf, well, I'm sure you'll get to appreciate it full hand when you get into a management job at some point."
    MC "Nahh, management isn't really what I'm shooting for."
    AE "Really? Well then what are you planning? After school, that is."
    MC "Uhhhm, I'm not completely sure. I'm thinking something like architecture."
    AE "Hmm...I see. Never figured you as an architect. "
    MC "Ehhh, well, it's not exactly a given...you though, phew, I can see you going places."
    AE "..."
    "Shiori-san quieted up a bit more. At that moment, I started to get a bit of a feeling that Shiori-san is uncomfortable with discussing occupations."
    AE "If I can admit something to you, Hotsure-san, this is my least favorite part of my position."
    MC "Um...putting up signs? I mean, you're a bit short so..."
    AE "That's not what I meant."
    MCT "Eep. Point taken."
    AE "I mean...I mean putting a faux happy spin on things such as this."
    MCT "A faux..."
    MC "Oh, you mean with the posters?"
    AE "Well, yes, however the...gaudy design is merely a symptom of a greater problem with the general mentality about these sort of things."
    MC "Greater mentality? I'm sorry, you kinda lost me there. I mean, I kinda like the posters."
    AE "Hmm...it's hard to put in the most accurate terms..."
    AE "In essence, I think it's unfortunate that people need to digest information with a spectacle. The idea that something needs to be 'cute' or have some sort of friendly overtone in order to get people to do things."
    MC "Oh."
    AE "Yes, and...and I feel like in this setting it's more concerning than anywhere else."
    MC "Here? How so?"
    AE "Well, I suppose that this sort of place is a bit more serious than the school wants to let on. By all accords this place is for people with clinical conditions, and as such the school body needs to treat this all in a, well, clinical manner."
    MC "Well...I get what you're saying but...I don't think I agree."
    AE "Oh? What do you think?"
    MC "I agree, yeah, it is a clinical situation that needs to be taken seriously; but it's because it's such a serious matter that we need to put a bright spin on things to keep people's spirits up. I mean, even you'd agree that people who are happier are more efficient, right?"
    AE "In this particular situation, it's not about efficiency, it's about common decency."
    MC "Either way, we all just gotta do what we can to keep people's hopes up."
    show AE angry
    AE "I apologize, Hotsure-san, however I don't find value in stamping happy face stickers on caskets."
    MC "O-oy, isn't that analogy a bit much?"
    show AE neutral
    AE "Mmm, perhaps, but I got my point across. I prefer a harsh reality to a comforting fantasy. It makes things easier to assess and easier to fix."
    "We continued to work after that somewhat strange discussion, until we ran into a particularly high area."
    MC "Woah...look's like we'll need more than a stepladder for this. Or, y'know, I could get on and we could swap positions."
    AE "Hmm...no. Putting you on top of this ladder would put you at risk."
    MC "Eh? Well, putting you on top would put you at risk, AND make it so you can't reach."
    "Shiori-san bit her thumbnail once more, and began to contemplate a possible solution while closing her eyes."
    AE "If we get Yamasaki-san...no...no she's in the garden. I wouldn't want to use her condition for my gain."
    MCT "Wouldn't want to...? Really? I would have never..."
    AE "Hmm...equilibrium. If the ladder has mass on the bottom to counteract the weight on top, then the ladder will keep stable. "
    "Shiori-san took her thumb away and opened her eyes."
    AE "Hotsure-san. I have a proposition for you."
    MC "Huh? Yeah?"
    MCT "I'm guessing she wants me to-"
    AE "Stand on the ladder while I get on the top."
    MCT "How did I know."
    MC "U-um...Shiori-san? It's not that I want to rebel against your plans or anything but...wouldn't that mean I was..."
    AE "...Yes?"
    MC "Right beneath your skirt?"
    AE "..."
    "Shiori-san bristled a bit, bashfully moving one leg to keep her mind off of it."
    AE "I...I can trust you won't look at my...posterior as I'm working."
    MC "No, I definitely won't."
    AE "Ok...good. Well...get on."
    "As Shiori-san climbed the ladder, my eyes went directly to her posterior. Because of course they did."
    "Could I really help myself though? No. Shiori-san's butt was tantalizingly close to my face. And her beautiful legs..."
    AE "Eep! Hotsure-san?!"
    MC "Don't worry, I'm just grabbing your waist for support."
    AE "O-oh. Smart idea."
    MCT "W-what?! That was an actual concern!"
    "All was going well. I was holding Shiori-san up as she reached for the wall space. But that's when it happened."
    MC "Shiori-san, w-wait, I-"
    show AE surprised
    AE "W-woah!"
    MC "A-I got you!"
    "From my point of view, all I saw was Shiori-san's pillowy mounds push out towards my face, seemingly swelling out as the back of her head faded from my view as she bent over; the fabric of her skirt being the last thing I see as her butt collided with my face. I fell flat on my back on the tile floor below, head missing the floor by about...not at all."
    AE "Oh dear god."
    MC "Ahk-ahw, dammit, ugh..."
    show AE sad
    AE "Hotsure-san, I am so sorry! A-are you alright?!"
    "Shiori-san walked her way down the stepladder to get to me, it wasn't that big of a fall, but it was more of landing directly on my back that knocked the wind out of me."
    AE "Nggh, why did I do that-why did I think that was a good idea."
    MC "It's okay, Shiori-san, I'm alright! I was the one who offered to hold your-"
    AE "But I shouldn't have accepted."
    MC "N-no. It's okay."
    MCT "The view was fine till I hit the floor."
    AE " Here, let me help you up."
    "Shiori-san worriedly reached her hand out to me, grasping my own as I hopped to my feet.#"
    AE "Are you sure you aren't hurt? I can refer you to the nurse."
    MC "I'm telling you, I'm fine! It's alright."
    AE "A-alright. If you say so. Ach, here, you have...dirt all over..."
    "Shiori-san swiftly began to brush the back of my back before, unknowingly I'm sure, began to pat the rear of my pants."
    MC "U-um, hey!"
    show AE neutral
    AE "O-oh! Right, sorry, just let me..."
    MCT "Pat, pat, pat."
    AE "There."
    MC "Alright...well, that was embarrassing."
    "I scratched the back of my head, chuckling to myself as Shiori-san continued her concerned gaze."
    MC "Welp, now that that's over, let's get back to work."
    AE "Oh no, you are staying on the ground and carrying the papers."
    MC "I'm telling you Shiori-san, it's okay."
    "I turned around and grabbed the stepladder, getting ready to move on to the next empty space. Not noticing as Shiori-sans face went from a look of worry to a look of shock and anger. That's when she did something I didn't expect."
    show AE angry
    MC "W-woah, hey!"
    "Shiori-san buried a hand in my hair and felt the back of my head."
    MC "Woah, woah, what was that about...?"
    MCT "What is she looking at?"
    "Shiori-san looked at her hand, a quick look of alarm shooting across her face."
    AE "Like hell you're okay!"
    MC "Huh, what?"
    "She held her finger out to me when I noticed..."
    MCT "...blood?"
    AE "P-put the papers down and go to the nurse, now!"
    MC "Ehh?! But, I didn't even hit my head that ha-"
    AE "No excuses!"
    "Shiori-san grabbed my hand, and I felt each tiny tremble ripple throughout her shaky arms."
    #we need a nurse's office
    scene Nurse Office with fade
    show AE sad with dissolve
    "I sat on the small, cushioned bench, paper crinkling beneath my pants as I shifted position. Shiori-san had spent a good five minutes washing and sanitizing her hands as we waited; eventually sitting down next to me and holding my hand, despite my protests that I was fine."
    "After a brief intermission, the nurse walked back in, a woman with long painted fingernails which clacked with every errant movement on her clipboard."
    Nurse "Okay, Hotsure-san, I did a double check on your medical history and the likelihood you have a concussion is minor."
    AE "Nurse, I would like to inform you that I was the one who-"
    MC "Decided to bring me straight here."
    AE "...W-Hotsure-san you-"
    Nurse "Well, it was a kind gesture, Matsumoto-san, however it seems as though it wasn't necessary."
    AE "N-not necessary? He was bleeding from the impact point."
    Nurse "Hotsure-san, I actually have the perfect solution for you."
    "The nurse reached into her bag and grabbed a bottle of shampoo. The bottle had the school logo on it with a man in a shower."
    MC "Um...ma'am?"
    Nurse "I'm guessing you scratch your head a lot, son?"
    MC "Well...yeah."
    "The nurse gave a soft wink."
    Nurse "It's scalp treatment shampoo. It doesn't flake up, so you don't have to worry about scabs."
    AE "S-scabs?"
    Nurse "Mhm, it seems as though he scratched the back of his head, opening up a scab from showering."
    MC "E-eh?"
    Nurse "Look, see my nails? Whenever I wash, I make sure the edges are rounded so I don't cut my head up. From the looks of it, you've got some sharp nails yourself."
    MC "O-oh."
    "I darted a look over to Shiori-san, who was looking on incredulously."
    MC "Ok ma'am, thank you, I will."
    Nurse "Alright, have a good day. Oh, and tell your girlfriend that she's very loving."
    show AE surprised
    AE "Wha-"
    MC "Gnk-"
    Nurse "Mhnhnhn, have a good day."
    "The door creaked closed, the fogged glass blocking view to the inside."
    AE "H-hold on, I-I believe you've made an error in assessment!"
    MC "..."
    AE "U-um..."
    "Shiori-san straightened up a bit more before adjusting her glasses."
    show AE neutral
    AE "In the diagnosis, that is. You-you're still not in the clear yet. I want you to go to your dorm and take a rest. Then...then I'll see you again tomorrow. When you're healed."
    MC "Shio-"
    "Before I could say anything more, Shiori-san walked away bashfully, rear swinging as she walked. I blew air out of my mouth and rested my back against the wall."
    hide AE with dissolve
    MC "Mhn...girlfriend..."
    MCT "Huh..."
    MCT "Welp, I oughta get heading back, Daichi is probably going to interrogate me about why I was at the nurse's office."
    "I cracked my neck and walked to my dorm, rubbing my neck the way back."
    jump daymenu

label AE014:
    scene Hallway with fade
    "I walked over to the library doors to begin another day of work with Shiori. Newly printed posters adorned the halls, as well as the doors themselves."
    MCT "Yeesh, she really got to work after yesterday, didn't she?"
    "I opened the library door, but this time I noticed something strange. It only opened part of the way before jamming."
    MCT "Eh? What's..."
    "A slight push. Nothing. A greater push. Once more, nothing."
    MC "Okay. You know what, I think I'm good for today."
    "I turned around and began to walk back to my dorm. Mind swimming with what all I was going to do today."
    scene black with fade
    pause 1
    scene Hallway
    MC "RAGH!!"
    "With all the swiftness of the wind gods at my back, I ran forward and punted the door with my knee. The door swung open with a loud creak."
    MC "*Pant* *Pant* Hah! I win..."
    "I looked down in time to notice the dolly with a cabinet on it sitting in front of the door."
    MC "Oh! ...Oh."
    MCT "And the door..."
    "The door had a two inch scratch in the wood finish near the base."
    MC "Mch...M'kay. Yep. I'll just..."
    MCT "I'll just wipe this off aaaan- okay, I made it bigger. I'll just...just...yeah."
    "I left it alone for the moment, wanting to flee the scene. I fled said scene by entering the office; a move similar to entering the police station to escape a bank heist."
    scene Office with fade
    MC "H-hey, Shiori-san, did you see that someone-ohp, woah."
    "I nearly ran face first into a wall of drawers."
    MC "Eh?"
    MCT "Is...is this punishment for what I did to your kin?"
    "I gave a deep bow."
    MCT "I'm sorry, drawer-san."
    AE "Hotsure-san? I assume that's you, yes?"
    MC "Um...yeah, Shiori-san."
    AE "Good, good, I'm over here, behind the cabinets."
    MCT "You're gonna need to be a lil bit more specific there."
    MC "Oh, I don't really see you, um..."
    AE "No? Okay, over by the window, near the far end of the wall."
    MC "Ah! There you are! Finally."
    show AE neutral with dissolve
    "I was greeted with the usually upright and taut Shiori-san now appearing cramped and mousy between a cavalry of black metal drawers."
    MC "Hey, Shiori-san."
    AE "Hotsure-san, good evening. I'd get up to bow, but as you can see, i'm not exactly in a suitable position."
    "I looked around to admire the sheer magnitude of the junk in the room. It's surprisingly fun to have a room you're so used to change like that."
    MC "I guess. What's with all of the tables and cabinets and stuff?"
    AE "Despite my protests, administration is temporarily utilizing the office for storage."
    play sound "Audio/Thud.ogg"
    "*THUNK*" #TODO: replace with SFX?
    MC "ACH-Couldn't they find anywhere else?! I can barely move in here."
    AE "Be thankful you're not in my position at least. I can't move without getting, ngh, stuck every few steps."
    "Shiori-san went to walk forward, but found that doing so sandwiched her vast hips between two cabinets. She let out a sigh of exasperation before beginning to scoot her way out."
    MC "Oh! Here, if you want, I can-"
    AE "No, no, I can do it."
    "With hands on both cabinets, she pressed on, trying to free herself from the tight squeeze."
    show AE angry
    AE "Hggggn-UH!"
    "With a ungraceful tug, she freed herself, sending her bulbous derriere into a wobbling fit before a quick movement of her hips subsided it."
    AE "Confounded-! Nggh..."
    MC "Do you want to move up front?"
    show AE neutral
    AE "That would be a pleasure, if it weren't for the fact that my table hadn't been moved to accommodate the space. The one time I do want Mizutani-san to lift tables about..."
    MC "Well...let's get to work, I guess."
    AE "Simply unacceptable...yes. That will get my mind off of this."
    "We worked together like usual, with the caveat being the metallic labyrinth that I needed to navigate just to get to the correct folders. Shiori-san went to move her arm, and winced in pain as her funny bone was jolted by the edge of a cabinet."
    AE "Hotsure-san, can you get that stray file? It should be on top of the third shelf."
    MCT "Oh, the one at the very top?! Where I've hit my head 4 times?!"
    MC "Sure."
    "I stretched up to reach it, yet it eluded my grasp slightly."
    AE "Ugh, no. The drama club budget sheet needs to be on the lower shelf."
    "Shiori-san got up and walked over to my general location. Seems as though she needed the lower cabinet."
    MC "H-hey, Shiori-san, yo-"
    "I moved my hips back."
    AE "Wait, I just have to just..."
    "She, however, misjudged. And while trying to squeeze out..."
    show AE surprised
    AE "A-ah!"
    MC "Woah!"
    "Squeezed her backside right up against my crotch."
    MC "Wooooah, okay. Um."
    AE "..."
    MCT "Oh god, oh man, oh god, oh man oh god oh man."
    MC "I-it's okay, um, s-should I scooch out of the way or?"
    AE "No, no, let me, I-"
    "Shiori-san tried to perk up and squish her way out, but it only drove her cheeks deeper into my groin."
    MC "Ok, that's not really-"
    AE "Helping-"
    MC "Yeah, no, um..."
    MCT "Damn, this is bad. I gotta get out of this or else...Ahnnn, I can feel her through my...c'mon, c'mon c'mon!"
    "I could feel my heart begin to race. My palms began to sweat as I started blushing deeply."
    MCT "Oh man, if I keep this up I-"
    AE "H-hold on, let me try..."
    MC "A-ah!"
    MCT "OK, OK, NOW IT HURTS. I WANNA GET OFF THIS WILD RIDE."
    MC "NNNNNGGHGH."
    "With what little room I had, I slid my hips out from the side, finally escaping the awkward and intense butt-squish heaven and hell."
    MC "Ok! Alright... I, uh, g-got it."
    "Shiori-san's face was in a deep shock, before slowly turning to a solemn sadness."
    show AE sad
    AE "I'm sorry."
    MC "Oh, no! I'm sorry, I shouldn't have been... i-it's really inappropriate of me."
    AE "I take full responsibility for this."
    MC "W-well... it's fine. I'll make sure it won't happen again."
    AE "Yes. I'm sorry."
    MCT "Wow...she's really beat up about this."
    MC "Don't worry too much about it..."
    "I turned around and continued to work, attempting to alleviate the tension in the room without success."
    MC "Um... I hope I didn't make that super awkward or anything."
    AE "No, no, it's quite alright. I apologize for..."
    AE "Pressing my bottom against your handbook."
    MC "It's oka-"
    MCT "Huh?"
    MC "Handbook? My student handbook?"
    AE "Yes. I'm sorry."
    MCT "Eh? I left my handbook at the do-"
    MCT "..."
    MC "Yeah, it's okay. Don't worry about my handbook."
    MCT "If I tell her it wasn't my handbook she'll flip."
    AE "How could I not? The student handbook is a symbol of rights and school diction, and I besmirched it by...rubbing it against my unmentionables!"
    MCT "On second thought. It'd probably be best if I told her it wasn't."
    AE "Sincerely. Accept my apology to both you and to your symbol of the school!"
    MCT "She gave me an equivalent to a standing lapdance without desire or warning and the first thing she thinks about is apologizing to the school?!"
    MC "Hey, hey! I said it was okay."
    show AE neutral
    AE "V-very well then."
    "We continued to work a bit longer, but not a word was said between us. We worked in silence for another 30 or so minutes before Shiori-san spoke up."
    AE "Well, um, I suppose that should be enough for today. Hopefully by tomorrow this... mess will all be cleared up."
    MCT "I can only hope."
    MC "Okay, well, see you next time."
    AE "Next time, then...I'm sorry."
    MCT "Oh brother."
    hide AE
    "Shiori-san quickly strode out of the office, muttering to herself along the way. I let out a sigh of relief. The scene replaying in my mind as-"
    AE "Who scratched the library door?!"
    MCT "..."
    jump daymenu

label AE015:
    scene Hallway with fade
    "As I walked down the halls, my mind kept flashing back to yesterday's incident. Specifically, my mind travelled more towards the worry that Shiori-san may have realized by now that it wasn't my pocketbook she was rubbing up against."
    MCT "I am NOT looking forward to having to work in such a cramped environment again."
    "I tried to convince myself pathetically, with a smile on my face and less than innocent thoughts running through my head. I headed towards the old wood door, wary of any possible obstructions."
    MC "I hope they got the door scratch fixed."
    "I looked at a blue post-it note on the side of the handle."
    "{i}Please open door GENTLY.{/i}"
    MC "Oh good."
    "I pulled the door open without problem this time, and made my way through the empty library."
    scene Office with fade
    "As I walked into the office, I was greeted with an unbroken wall of black-iron filing cabinets, sitting there menacingly. And in the middle of two cabinets..."
    MC "..."
    MCT "S-shiori-san?!"
    "More specifically, the poor girl's rear and two legs stuck between the cabinets. She was lifted slightly off of the ground by the table, her thick thighs pitifully kicking in resistance."
    MCT "O-oh no! Shiori-san's been captured!"
    AE "Oh god...Mnf..."
    MCT "W-what's gonna happen to her? Is she gonna be eaten and turned into paper? Is she going to become one of the cabinets?!"
    "It took every ounce of my mental fortitude not to start cackling like a hyena."
    AE "*Nngh* *Nnnnff*"
    $setVar("AE015_watch", 0)
    jump AE015_menu

label AE015_menu:
    menu:
        "Watch her a little longer." if getVar("AE015_watch") <= 10:
            $setVar("AE015_watch", getVar("AE015_watch") + 1)
            jump AE015_watch
        "Watch her a little longer. (disabled)" if getVar("AE015_watch") > 10:
            pass
        "Help her out.":
            jump AE015_aftermenu

label AE015_watch:
    if getVar("AE015_watch") <= 3:
        MCT "I...I'm gonna see how this plays out. I'm sure she'll get out eventually."
        "I watched a little longer as Shiori-san kicked her massive legs up and down, her thighs wobbling like mad and her skirt swishing from side to side as she struggled in vain."
        AE "*Pant* *Pant* Hggnnn."
        jump AE015_menu
    if getVar("AE015_watch") <= 6:
        "I couldn't help but stare on at Shiori-san as she began to try and wiggle out, eyes fixed on her round rear as her hips shaked more frequently."
        AE "Hoooah...W-wait...Nggggnn~!"
        "I pulled up a chair and sat down, with pursed lips and hands resting lightly on my abdomen as I watched on."
        AE "Ach-H-hold on...nhg."
        jump AE015_menu
    if getVar("AE015_watch") <= 9:
        "I rested my feet up on the table, watching with intent as Shiori-san continued her struggle."
        MCT "It's like watching an adorable trainwreck."
        AE "Are you-ach- k-kidding me?!"
        jump AE015_menu
    if getVar("AE015_watch") <= 10:
        "I continuously watched as sweat began to form along the seat of Shiori-san's skirt."
        AE "*Pant*...*Pant*...Hng...hnnnnn~."
        "I opened up my backpack and pulled out a bag of shrimp flavoured popcorn. I slowly began to much on the treat as sadistically and smugly as I possibly could."
        AE "H-huh? Hello? Is that shrimp? What's happening?!"
        MC "...*Munch*"
        MCT "Y'know, I should probably help her...or just wait for some students to walk by for end of the day cleaning."
        jump AE015_menu
    if getVar("AE015_watch") <= 11:
        MCT "She's stopped kicking now. It's w-oh, no, there she goes again."
        "I watched on, bag of popcorn now empty, as a twinge of sympathy began to set in."
        MCT "Alright, now I'm getting bored, plus I'm starting to feel bad."
        jump AE015_menu

label AE015_aftermenu:
    if getVar("AE015_watch") >= 5 and getSkill("Academics") > 3:
        $setAffection("AE", 2)
        MCT "Oh, wait, hang on."
        "For subtleties sake, I snuck out of the room, then out of the library before making a show of entering again and making loud footsteps as I entered the office."
        MC "Huuh? What's going on here!?"
        AE "Oh...*pant*...oh thank heavens."
        MCT "Nice."
    MC "U-um, Shiori-san?"
    AE "H-Hotsure-san? Is that you?"
    MC "Y-yeah, Shiori-san, I just got here. Are you stuck?"
    AE "Um...y-yes."
    MC "Here, let me help."
    "I walked behind Shiori-san and put both hands on her hips as I began to tug."
    AE "W-wait, Hotsure-san, isn't there a better way?"
    MC "One, two..."
    "I positioned my own legs in a way that would allow for greater force."
    MC "Three!"
    "With a quick tug, I pulled Shiori-san free from the cabinets. Once free, the two of us both collapsed to the floor, the force from dislodging her pushing us back."
    show AE sad with dissolve
    AE "Nhg..."
    MC " Ayah...y-you alright?"
    "I looked at Shiori-san, her raven hair spread out on the ground, and gave a slight chuckle. Shiori-san opened her eyes, and looked at my face before sitting up and rubbing the side of her head."
    AE "Y-yes. Thank you."
    MC "No problem."
    "Shiori-san's face was cherry red, and there was a light moisture around her eyes."
    MC "You look like you were a couple of seconds away from screaming your head off!"
    show AE neutral
    AE "Come now, Hotsure-san, I have more composure than that."
    "I sprung up and stood straight, stretching my back until I heard a pop from my spine. Shiori-san sat cross legged, before grabbing onto the side of a table and slowly lifting herself up."
    AE "M-mnph."
    MC "Oh, do you ne-"
    AE "No, no, I can get up."
    "Her arms wobbled as she pulled the weight of her large behind from the ground; before finally standing up straight in the doorway."
    AE "Hooo, okay. Wow."
    MC "So...what happened?"
    AE "I, uh, whoo...*ahem*"
    "Shiori-san straightened up, regaining her posture as she repositioned her glasses."
    MCT "Her and those loose glasses."
    AE "I was making an attempt to retrieve some supplies from the room...as it turns out my reach is nowhere near what I would hope for."
    MC "I'd say..."
    "I looked around the inside of the room. It was full of black metal filing cabinets from the door to the back wall."
    MC "So..."
    "I looked to Shiori-san with a slight grin."
    MC "Wanna get to work now?"
    AE "I'm not looking to have a repeat of the...incident from the other day."
    MC "P-please don't bring it up."
    AE "I already have. I gave administration a full account when trying to convince them to remove the extra cabinets."
    MCT "Th-this unbelievable girl is going to get me suspended! Can we please change topics!?"
    MC "Wait, you talked to administration?"
    AE "Yes."
    "Shiori-san rested one hand on her hip, letting the other hand stay at the side of her body as she shifted her weight."
    AE "I'm not usually one to go against the decisions of the administration, however I made an effort recently to have these removed from the office."
    "I took one last exaggerated look around the office room from the doorway."
    MC "Oh...I can see it turned out well."
    AE "No, actually. In fact the administration said that they were planning on keeping the supplies here..."
    extend " For the next few days..."
    extend " In which time I won't be able to access the cabinets."
    "Shiori-san took her thumb nail between her teeth as she stared at the mess of iron filling the room."
    MC "So then, what are you planning on doing?"
    AE "I would usually spend any spare time monitoring the halls, so I suppose that's a good place to start."
    "Shiori-san, grabbed her books, which had been lying on a drawer adjacent."
    AE "We'll pick up work within a few days. Until then, I'll be seeing you in class. Have a good day."
    "She walked past me and began to head towards the library door."
    MC "Hey, Shiori-san, wait."
    AE "Hm? Is everything alright?"
    MC "W-well, yeah, but..."
    "I scratched the back of my head, causing Shiori-san to let out a sigh in exasperation."
    AE "Have you been shampooing correctly?"
    "She pointed an accusatory finger at me while placing a balled hand on her hip."
    AE "I don't want you getting any more cuts on the head. Proper scalp health is vital to-"
    MCT "My mind began to wander a bit as she talked, looking directly into her eyes and nodding every few seconds. My memory was pulled back to a specific statement that the nurse said...and I gave a light smile."
    MC "Do you wanna spend some time together?"
    AE "Further mo-...hm?"
    "Shiori-san let her hand slip from her hip, her finger no longer straightened as she absorbed what I had said."
    MC "We may not be working, but I think we should spend some time together outside of class."
    "We stood there in silence for a moment."
    AE "W-well, um, I don't see any reason why, it's not beneficial to your development..."
    MC "Well, no, but I think it would be nice to hang out together outside of work. We could relax a bit together."
    AE "Relax?"
    "Shiori-san thought to herself a moment, glancing between her feet and myself."
    AE "That...it won't be necessary. We don't really..."
    MC "It'll be fun."
    menu:
        "We can make it your choice what we do.":
            jump AE015_c1
        "It'd be nice to let you loosen up a bit.":
            jump AE015_c2

label AE015_c1:
    $setAffection("AE", 2)
    MC "If you want, we can do whatever you want to do."
    AE "Whatever I want?"
    "Shiori-san stood there, eyes twitching as she contemplated what we could possibly do together."
    AE "Hmm...I see. I'll...keep the possibility in mind. Do you truly trust me to pick something enjoyable?"
    MC "W-well, yeah."
    AE "Hm. Well, thank you."
    jump AE015_afterchoice

label AE015_c2:
    $setAffection("AE", -2)
    MC "I think it would be nice to help you get out of this stuffy office for a bit. It would help you loosen up."
    "Shiori-san seemed a bit taken aback by the words 'loosen up'. She thought to herself a moment before looking to me through severe eyes."
    show AE angry
    AE "Well, I so happen to like my 'stuffy' office. It's an environment that lets me achieve peak performance."
    MC "Really? I mean, can anybody really like-?"
    AE "I certainly do. Or is that not 'loose' enough for you?"
    MCT "Yikes. Wrong call."
    jump AE015_afterchoice

label AE015_afterchoice:
    show AE neutral
    AE "...Still, though. It would be nice to do something outside of office work with you...it could allow me to see how you behave in a...non-formal setting."
    MCT "Uh...yeah, whatever floats your boat."
    AE "Very well then, Hotsure-san, we will spend time together. Free time."
    MC "Alright! It's a date."
    show AE surprised
    AE "...W-what?"
    MC "Oh! Uh, a hang out date. I-it's an expression."
    show AE neutral
    AE "Ah, yes. Expressions! And...hm. S-see you then."
    MC "Yes, see you."
    "Shiori-san was halfway out of the door before stopping and poking her head in to speak to me again."
    AE "Oh, um, about where we'll go."
    MC "Y-yeah?"
    AE "Follow me after class. I will lead us."
    MC "Okay."
    hide AE
    "With that, Shiori-san left. I stood around in the library for a moment before speaking up to myself."
    MC "It's a date...tch, c'mon, man."
    "I let out a sigh of audible exasperation before opening up the door myself and heading out to the dorms, ready to continue the rest of my day."
    jump daymenu

label AE016:
    scene Hallway with fade
    "Today was the day I said I would meet Shiori-san outside of the office. I was somewhat excited for a bit, this was the first day we would actually be able to spend time one on one without working."
    "I got up and followed Shiori-san once class ended. Where, as promised, she lead me to where we would spend time today."
    show AE neutral with dissolve
    AE "Well, here we are."
    "We came to a stop in front of an old wooden door."
    "A familiar old wooden door."
    MC "...Eh?"
    MCT "This is..."
    scene Library with fade
    MCT "The library? Really?"
    MC "U-um...the library?"
    show AE neutral with dissolve
    AE "Yes. It's a good place to spend time, no?"
    "Shiori-san looked at me expectantly, confusion cleary plastered on my face."
    MC "W-well, I mean...weren't we gonna go out and talk or...?"
    AE "Oh. Well, I assumed that you would've wanted to go somewhere like the library. It's quiet, no-one is around, and we can talk uninterrupted. Is there somewhere else?"
    MCT "..."
    MCT "Oooohh, I think I see. She's shy about just going out with me in public. She doesn't want people to get the wrong idea. Okay, I understand now."
    MC "Oh, uh, no this is fine."
    AE "Good."
    AE "Then, please, take a seat."
    "I grabbed one of the large chairs and pulled it across the floor to the table."
    AE "Please don't drag the chairs."
    MC "Eh? Oh."
    "I picked up a chair and put it beside the table."
    AE "There. Best not to scratch the floors. I'll be right back."
    MC "Huh? Okay, but what are-"
    hide AE
    "Shiori san walked away and headed over to a small box near the door of the office; one which had until now escaped my notice. With papers in her hand, she walked over to the table and sat across from me."
    show AE neutral with dissolve
    AE "Alright. That should do it."
    MC "W-Huh? Shiori-san what-"
    MCT "Oh. Oh I get it."
    MCT "She wasn't shy about going outside with me, she just wanted to get some work done in the library."
    MC "Um...Shiori-san?"
    AE "Hm?"
    MC "What's with the papers?"
    AE "Oh, just some things to pass the time. I hoped we could look over these to knock some things off of my to do list, seeing as how today is a day we aren't in the office."
    MCT "As expected. She can't help herself."
    MCT "I gotta try and tear her away from work for even a second."
    menu:
        "Give her a random topic":
            jump AE016_c1
        "Ask her to stop":
            jump AE016_c2
        "Offer to help":
            jump AE016_after

label AE016_c1:
    MCT "I should try and give her an interesting topic. That way she will get immersed in the discussion."
    MC "Well, uhh, did you know that a student slipped on the saliva from Tashi-sensei's tongue?"
    AE "Yes. I had to do the paperwork involved in the incident."
    MC "Heh, I figured."
    AE "..."
    MC "..."
    "The silence was like agony as I desperately wanted at least some form of acknowledgement, moreso for the hope of some small victory in the situation."
    MCT "Of course. Think of something else"
    MC "D-um...I went over to...uh..."
    AE "Please. Don't mind me, continue."
    MCT "I'd be more than happy to. AS SOON AS YOU PUT DOWN THE PAPERS!"
    MCT "Okay, this isn't working. Well, I guess she is, but that's the problem. She's a workaholic.Maybe if I...hmm."
    jump AE016_after

label AE016_c2:
    MC "Um, hey, Shiori-san?"
    "Shiori-san looked up to me, clearly sensing something in my tone I didn't mean to convey."
    MC "Do you wanna talk or am I just...you know, bothering you?"
    "Shiori-san looked at her papers a second before quickly looking back at me."
    show AE sad
    AE "Oh. Is this...is this rude, Hotsure-san? I'm sorry, I didn't mean to..."
    MCT "Aw man, the look in those eyes seem really disheartening. I can't just make her stop like that."
    MC "N-no, no, it's fine! I mean...you can keep working."
    show AE neutral
    AE "Well, good then."
    "Shiori-san looked back to the papers, leaving me to just sit there, running my hand across the back of my neck."
    MCT "Okay, this isn't working. Well, I guess she is, but that's the problem. She's a workaholic.Maybe if I...hmm."
    jump AE016_after

label AE016_after:
    MC "Sooo..."
    AE "Hm? Yes?"
    MC "What are those?"
    AE "These are all request forms submitted by students who have concerns for the Student Government."
    MC "Oh."
    MCT "Student Government here has request forms? Huh..."
    MC "I'm gonna be honest with you, I didn't know we had a request form."
    AE "Of course. The school values feedback from the students, thankfully. These forms are a way to get things done that the students believe need to be handled."
    MC "So, how often do you get those?"
    AE "Hm?"
    MC "You know, the forms, how many do you get?"
    AE "It depends, but so far around twenty or so a week, they're submitted to a box outside of the office and Student Government reads them at the end of every school week. "
    MCT "Twenty or so a week?! Jeez, I didn't realize people here were so needy."
    MC "Well, let's take a look!"
    AE "...You want to help?"
    MC "Well, sure. Unless it's against the rules..."
    MCT "Nice wording."
    AE "Hmm...It's not. Alright, have a look."
    MCT "Alright! That's a step in the right direction."
    "Shiori-san got up and walked over to my side of the table, papers under her arms. She sat down beside me, splaying the papers out in a row. She picked one up and read it aloud."
    AE "'Install sound devices in the girls restroom.'"
    AE "Hm. I like this one. Water expenditures here are abysmal as is, so installing sound devices should help."
    MC "Eh? How would a sound device cut on water?"
    AE "Clearly you know nothing of female toilet etiquette."
    MCT "...What?!"
    AE "What's this one?"
    AE "'Matsuro-san's breath is bad, please expel him.'"
    "We sat in silence for a moment, a blank expression being the only accompaniment to my seething confusion."
    MC "O-oy! That one isn't a real request is it?!"
    AE "For the sake of my sanity, I assume not."
    "Lightly, she took the paper and creased the paper in the middle, placing it gently to the side. She picked up another."
    AE "'Stop making me button up my shirt.'"
    "Another crease."
    show AE angry
    AE "No."
    MCT "I'm 70%% sure that's Mizutani-san's handwriting."
    show AE neutral
    AE "'Satoru-sensei is-' nggh."
    "And another."
    MC "Jeez what's with these dumb requests?!"
    AE "It's par for the course. It was the same as in my previous school."
    MC "Well, is there any way to...I guess cull the requests so there are only serious ones?"
    AE "That's what we're doing right now."
    "For a moment, I forgot I wasn't a member of the student government; what with all the work i'd been doing. It hadn't dawned on me that I wasn't approving anything, just looking over it."
    MC "Well, no, I mean like to even be able to submit one."
    AE "Ah, I see. No, there shouldn't be."
    "I recoiled a bit. That was one of the more unexpected things I've heard from Shiori-san in a while."
    MC "Huh, bu-"
    AE "Everyone deserves the right to have their voice heard, no matter how puerile it may be."
    MCT "Huh...who would've thought."
    MC "I didn't take you as such an advocate for free speech."
    AE "I'm an advocate for whatever rights the school allows its students."
    MCT "Thaaats more what I expected."
    AE " The simple answer is just to take the serious requests into mind and discard the ones that aren't."
    MC "Huh...alright."
    AE "Mhm. Come on. Let's look through these."
    "Within a few minutes, we went through all twenty two requests. In the end, we only came up with seven legitimate concerns. But my mind wasn't on that for the moment, because the air in the room had changed."
    MC "And my sister, my sister, she would always flush the toilet all the time too, and you're saying it's because...pffft-ehehehe."
    show AE happy
    "My chuckle was seemingly contagious, as even Shiori-san gave a little smile of amusement."
    AE "Precisely. And that must have drone your father up a wall for water bills."
    MC "Mm- No, actually, my mom."
    show AE neutral
    AE "Really?"
    MC "Yep, mom was the breadwinner of the house. Dad was just a manager at a department store."
    AE "Ah, really? "
    MC "Yep...so, uh...what about you? Do you ever flush the toilet constantly?"
    show AE angry
    AE "H-hey now! That's not a question to ask the class president!"
    MC "Ahhh alright, alright...but do you?"
    show AE neutral
    "Shiori-san sat for a moment with a light blush on her face."
    AE "Well, yes, but that doesn't give you the right to ask that!"
    MC "HAH! Ahaha!"
    show AE sad
    AE "D-w-mhn..."
    MC "Ah, man. Hey, you know I'm just playing. Hooo, you must have drove YOUR dad up the wall with the water bill."
    show AE neutral
    AE "...No, actually."
    MC "Eh? Ah, so your mom payed the bills too, ri-?"
    AE "Yes."
    MC "..."
    AE "W-well that and I didn't waste water at my house. I was a very conscientious girl."
    MC "Oh! Yeah, true, I can see that."
    "We sat in silence for a short moment before I spoke up."
    MC "Uh, heh heh, uh...man I've been really loud the past few minutes haven't I."
    AE "Yes, yes, I know. You've managed to cause enough ruckus in the library."
    MC "Well, you're the one who chose it! There's no one around."
    AE "Well yes...however if you've noticed I've been keeping my voice at a respectable level."
    MC "Eh, true, true."
    "I leaned back in my chair and put my hands over my abdomen. Letting out a sigh of relief."
    MC "Haaahn...boy, I'm tired."
    AE "Indeed."
    "Shiori-san stood up and put the papers, both full and creased under her arm."
    AE "Well, I suppose we've spent a good amount of time together today. We certainly should...do this again. The outside of work aspect."
    MC "Oh! Yeah, yeah, any time."
    show AE happy
    AE "Good. Well, I'll see you tomorrow then."
    "Shiori-san bowed, and turned around. As she began to walk away, almost as a compulsion, I asked her straight."
    MC "Do you wanna eat lunch with me?"
    show AE neutral
    AE "...Hm?"
    MC "Mw-Well, like...maybe we could get lunch together."
    "Shiori-san stood there for a moment. Looking off to the side with pursed lips. There was an audible inhale as she bean to speak."
    AE "Um...yes. Yes, I'd like that."
    "My only response was a goofy grin and a small scoff."
    MC "Okay, cool. Later?"
    AE "Later, yes. See you later."
    MC "Yeah, later."
    "Shiori-san walked out of the room, her rear bouncing with a light wobble with every step. Strangely enough, I hadn't noticed her ass the entire time we were together, when before I at least took sort glances. I adjusted myself in the chair, before closing my eyes and exhaling a deep breath; an indication of my planning for the rest of the day."
    jump daymenu

label AE017:
    scene Cafeteria with fade
    "After lessons had ended, I walked out of the room. I was going to walk out with Shiori-san, like with yesterday, but a student came up addressing her as \"ma'am\" so I assumed she had further business. I got up and walked over to the cafeteria to get in line and grab some food."
    MCT "I hope everything is alright. I should grab us a table just in case, that way she'll know I was waiting for her."
    "Looking at the selections, it seemed as though the school had a wide variety of different foods and drinks available, definitely more than I'd seen before."
    MC "Uaaah, look at all this stuff."
    MCT "Hmm...I think I'll just go with the Rice and Chicken."
    "I grabbed a bowl and began to fill it up in the self serve area; taking a few small strawberries as a little desert. After grabbing some chopsticks, I went to look for a place to sit."
    MCT "Hmm...let's see...where can I sit where Shiori-san and I-"
    "Almost to answer my own question, I caught a glimpse of the spectacled girl looking at me over a small partition."
    MCT "Oh! Oh, she's here already."
    "I went to walk over to where Shiori-san sat, and when I turned the corner I saw her talking to a short girl with large pouty lips."
    show AE neutral with dissolve
    AE "-and after that, I want you to tell her to get her forms in on time if she cares so much. Good? Alright, good."
    "The girl walked in the other direction as I continued to walk over to where Shiori-san sat, her hands massaging the sides of her temples."
    MC "Hey, you came!"
    "Shiori-san looked up from her hands, quietly putting them back down to her sides."
    AE "Well, I said I would, didn't I?"
    MC "Yeah, I just didn't see you in line."
    AE "I got here fairly early."
    MCT "How did she get here so fast though?!"
    MC "Ah, should have figured."
    "I sat down at the bench and immediately began to sink in the plush cushions."
    MC "Huh, the cushions on these benches are really soft."
    MC "In fact, these benches are pretty wide too."
    AE "Well, I'd suppose they'd have to be."
    MC "Oh, yeah, because...yeah."
    "Shiori-san looked at me softly while I mulled around. Patting the sides of the bench, I decided to ask about what happened."
    MC "So what was that about? With the girl?"
    AE "The art club head has been late with her forms again, I simply told Yuki-san to deliver a message."
    MC "A-ah, ok."
    "I twiddled my fingers a bit before reaching over and grabbing my chopsticks."
    MC "Welp, let's eat!"
    AE "Hm."
    "Shiori-san took hers as well and we began to dig in. Her tray seemed fairly tame; rice, noodles, carrots, and a single piece of strange desert, already half eaten."
    MC "What's that?"
    AE "It's a dough pastry with Hakuto jelly. It's strange, I tried it a while back and I can't get enough of it."
    MC "Well, can I try a bite?"
    "Shiori-san looked at me for a moment, before taking the plate the pastry was on and passing it over to me."
    AE "Go ahead."
    MC "Thanks."
    "I bit into it, and was greeted with a tangy and sweet gush of peach flavored jelly."
    MC "Mmmn~  That's great!"
    show AE happy
    AE "It seems like we have common tastes then. Good."
    MC "Yeah, I love peach suff."
    "As I took a few more bites of the pastry, I figured it would be a good idea to share some of my food with her."
    MC "Oh!"
    "I picked up a strawberry, nearly dropping it for a moment."
    MC "I got some strawberries. Want some?"
    show AE neutral
    AE "Oh, well I-"
    MC "Here."
    "I reached over the table and put it in front of her expectantly waiting. She stared at the small red thing as she slowly began to turn the same shade."
    show AE sad
    AE "U-um... I'm not sure it's appropriate to..."
    MC "Eh?"
    "I looked over at a pair of girls snickering adjacent, when I finally realized what I was doing."
    MC "Oh! Oh, yeah, sorry. Don't wanna give people the wrong...yeah."
    "I placed it on her tray gently, sitting back down as I stared at her. It was interesting watching her. The soft and subtle movements of her boy when she changes emotions is cute."
    MC "Sooo..."
    show AE neutral
    AE "Hm?"
    MC "Isn't it kind of strange for there to be a full cafeteria here?"
    AE "What do you mean?"
    MC "I mean, it's a bit of an abnormality at this level of schooling."
    AE "Well, I suppose the board figured that it would be better to provide lunches for the students, rather than leaving it to them to bring their own."
    MC "Yeah, it kinda feels like middle school again."
    AE "Do you feel like that's a bad thing?"
    MC "Hmmm..."
    MC "Well, no, to be honest. I'm glad we have a cafeteria."
    extend " Why? Do you?"
    AE "To be honest, there are some things I feel the school needs to change for the sake of maturity."
    MC "Ehhh, I dunno. Seeking maturity for the sake of just 'being mature' can often get in the way of stuff getting done."
    AE "True. And I suppose it is necessary for students with more...voracious tendencies."
    MC "Hm? Oh, do you mean the, uh, students who're gaining weight or...?"
    AE "Strictly speaking, yes. They tend to consume far more than it's believed they can bring, so it's for the best that the school provides for them."
    "My mind flashed to Nikumaru-san, as I began to doubt the part about 'far more than they can bring'."
    AE "Besides, if we're going to bring up 'non-conventional' methods, have you noticed something about the shoe lockers?"
    MC "Shoe lockers...?"
    MCT "Shoe lockers...I haven't really used them...wait."
    MC "Oh! We don't have any."
    AE "Precisely. I'm not the only one who noticed either, I found Yamazaki-san walking around in her socks first day looking for a place to put her shoes."
    MC "I mean...I didn't think it was as big of a deal."
    AE "Because you haven't had to clean the floors when they're covered in mud yet; a problem which you almost contributed to a while back."
    MC "Oh yeah...man, that must be a whole lot of extra work."
    AE "Undoubtedly."
    AE "I tell you, it may work fine for now, but when the rainy days really start, that's when administration will regret not installing them."
    MC "Hmn..."
    extend " Y-know i-"
    "As I began to speak, I moved my hand over my tray, accidentally putting my hand on some of the peach-filling from the pastry."
    MC "Ohp..."
    AE "Oh, I-"
    MC "It's alright, I can get a napkin..."
    "I reached over to the dispenser on the end of the table, but I ended up putting my hand in an empty slot."
    MC "Napkin...eh...there are no napkins."
    MCT "Shiori-san would kill me if I just wiped it off on my school uniform, let alone the bench."
    MC "A-Ah well. I can get it later."
    AE "..."
    MC "So, like I was saying, I actually used to forget my shoes at the door of my house all the time."
    "Shiori-san seemed only tangentially focused on me, her eyes changing focus from my own to the mess on my hand."
    AE "..."
    MC "My mom got so mad at me, she made me deep wash the carpet whenever I...Um..."
    AE "..."
    MC "Hey S-"
    "Without warning, Shiori-san grabbed a handkerchief from her shirt and grabbed my hand. She began to rub the spot with the jelly clean, looking intently at my hands as she did. I couldn't really do anything aside from look on in confusion; same with the group of friends next to us who watched on."
    "She finished wiping my hand, gently moving it about with her own soft and delicate hands before she was satisfied."
    AE "There. Clean."
    MC "..."
    AE "I apologize for the intrusion. Please, go on."
    MC "U-uh...yeah."
    MCT "What the hell was that?!"
    MC "Uhh...W-well I, aha...um...is everything alright?"
    AE "It's fine."
    MC "...Okay."
    MCT "I shouldn't question it. If I do I'll probably get an aneurysm."
    MC "But, uh...mom! Yeah, yeah, she would often have me deep wash the carpet until I learned to put my shoes in the cubby. Needless to say, I washed the carpet until I left."
    AE "As a soccer player?"
    MC "E-he-yup."
    AE "Your poor mother."
    MC "Oy, oy! It sucked, I spent a solid forty minutes a day just cleaning the floors!"
    AE "And that, Hotsure-san..."
    "Shiori-san grabbed the strawberry from her tray and put it to her mouth."
    show AE happy
    AE "Is good parenting."
    "She popped it in, satisfied smirk on her face as she began to chuckle in amusement. I rolled my eyes and scoffed at the ridiculous girl in front of me."
    AE "Mmhn. I suppose we need to get heading back, the cafeteria is emptying."
    "We stood up as Shiori-san dabbed her mouth with her handkerchief; the jelly from my hand on the other side."
    "I looked back at the bench where Shiori-san sat. She told me she was there a while, but from the looks of it she'd been waiting for me the entire time. There was a massive indent where she sat, creating a crater that could fit about two people."
    AE "Hotsure-san, are you coming?"
    MC "Y-yeah! I'll be right there."
    jump daymenu
    
label AE018:
    scene Hallway with fade
    "I sat at the windowsill waiting. My feet dangling just lightly off of the floor as I kicked them back and forth. Looking down at them, I was given a slight tunnel vision from my own black locks dangling down a few inches from my face. I looked up to the ceiling, inhaling and letting out a low gust of air from my lips. As I looked back forward, I saw a familiar face slowly heading up the stairs."
    MC "Oy, Shiori-san."
    show AE neutral with dissolve
    AE "Oh, good, Hotsure-san y-"
    "Shiori-san's face swiftly changed to one of concern."
    show AE sad
    AE "H-hey, off the window sill. Off it now."
    MC "Hm?"
    MCT "Oh! Oh...really?"
    MC "Um...okay?"
    "I hopped down in time to catch Shiori-san walking over swiftly to look out the window."
    AE "Be careful. That's a long drop from here."
    MC "Long drop? Shiori-san the window's-"
    show AE neutral
    "Before I could continue, Shiori-san looked at me with an expressionless face as she lightly pushed the window, causing it to swing open at the side. She raised a single eyebrow."
    MC "...latched."
    AE "And you just so happened to find the one window that isn't."
    "Shiori-san let out a light sigh, and put her hands on her hips."
    AE "Such a helpless young man. I'm glad I've been supervising you."
    MC "O-oy, oy!"
    AE "Hm?"
    MCT "..."
    MC "Th-thank you, Shiori-san."
    "Shiori-san stood up a little taller, a light blush crossing her face as she looked away and brushed her hair to the side."
    AE "Y-you don't need to thank me, Hotsure-san...looking out for your well being is what's expected of me."
    MCT "Eheh, she get's so cute when she's bashful."
    MC "So, Shiori-san, why did you want me to wait for you up here?"
    AE "Mm, well, I was making my rounds for monitoring the halls when I decided that we could maybe spend a little time somewhere else."
    MC "Ok, cool. Where at?"
    AE "Follow me."
    "I did as Shiori-san said and followed behind as we climbed the stairs. Though it was subconsciously, I followed a bit closer than was necessary. I looked up the whole time at Shiori-san's tush as we climbed, eyes fixated on the side to side movements of her skirt with every wobble and bounce of her derriere."
    "We climbed for a bit more until we reached our destination."
    MC "Oh, you wanted to go to the roof?"
    AE "Mhm. It's nice up here. Not a lot of people, nice, cool air, and a great view."
    MC "Alright, cool."
    scene Roof with fade
    "Shiori-san opened the doors, and a nice gust of air swept into the doorway. It was fairly strong, and almost instantly as the wind picked up, Shiori-san's skirt was lifted a few inches as well; giving me a brief view of her behind, squeezed tightly by dark-blue panties, before she pulled her skirt back down. Shiori-san cleared her throat."
    show AE sad with dissolve
    AE "Ah, I apologize."
    MC "Oh, no, it's okay."
    MCT "Nose, I swear, if you bleed on me now..."
    "As we walked out onto the gravelly roofing, the sun brightly gleamed in my eyes as I heard the birds around us chirp while they fluttered away to a nearby ledge."
    MC "Oh, wow, it's really nice out today."
    show AE neutral
    AE "I agree. It's a bit warm, but the wind is soothing."
    "We looked around for a place to sit, before coming across a lone metal bench."
    MC "Ah, there we go."
    AE "..."
    MCT "Hm?"
    MC "What's up?"
    show AE aroused
    AE "I-it's nothing."
    "Shiori-san sat down on the double wide bench, with me sitting beside her. We sat in contemplation for a moment, taking in the surroundings."
    MC "Haaaahn~"
    AE "..."
    show AE surprised
    extend "Hotsure-san, do you hear that?"
    play sound "Audio/Bird.ogg"
    MC "Hm?"
    AE "That bird."
    play sound "Audio/Bird.ogg"
    MC "Oh, yeah, it sounds nice."
    show AE happy
    AE "Mhm...it's a Siberian Rubythroat. They're native to the area."
    MC "Hm? Really?"
    show AE neutral
    AE "Yes. Many birds in northern Japan find their way over here."
    MC "Huh, that's nice...how did you know that?"
    AE "Ah, well, I heard it a while ago and looked up the native bird species. I referenced the bird with the image and found an article about them."
    MC "Ahh."
    AE "Mhm..."
    "We sat there in silence for a bit longer. We looked out towards the distant horizon, a few grassy mountains rising over the landscape, slowly fading to blue as it gave way to the far ocean, and the ocean to the sky."
    MC "I wonder...I wonder how far the horizon really is."
    AE "..."
    show AE sad
    AE "I've never thought to ask that..."
    MCT "How far the horizon is..."
    MC "Hey, Shiori-san, I have a question for you?"
    show AE neutral
    AE "Hm?"
    MC "How often do you dream?"
    AE "...That's a strange question to ask."
    MC "Ehe, I figured, but I wanted to know...do you ever have any recurring dreams?"
    AE "..."
    show AE sad
    "Shiori-san's face crinkled up a bit as she thought, hands tapping her thighs as she put the tongue on the inside of her cheek and looked away."
    AE "I...suppose. Why?"
    MC "I've been having this weird dream lately...and i've been wondering what it means."
    AE "What it means...?"
    MC "W-what?"
    show AE neutral
    AE "Well...why does it need to ‘mean' anything?"
    MC "I mean...I dunno. I guess it's just that our dreams are like a look into our minds is all."
    show AE sad
    AE "W-...a look into...?"
    "Shiori-san looked at me with a look of confusion."
    show AE neutral
    AE "I don't mean to be...off putting...but how can you prove that?"
    MC "Well...I don't know. There are some things that you just can't prove, right?"
    show AE sad
    AE "A-um...with enough proper research I-I assume we can know everything there is to know...however, yes, some things can't really be proven."
    MC "Exactly. It's a matter of faith in the idea."
    show AE neutral
    AE "Tch-it has nothing to do with faith, it's about an unproven field of psychoanalysis."
    MC "..."
    MCT "I struggled to bring back the entire memory of my dream, but only one piece of it sprang forth."
    MC "I...I remember standing on a concrete island. There was a blue sky...and blue waves."
    AE "..."
    MC "I was standing in front of a concrete pillar with a red number on it...four, I think...I dunno."
    AE "Oh...well...is that all?"
    MC "Yeah, I think so."
    AE "How very...insightful."
    "I looked over at Shiori-san expectantly."
    MC "Well?"
    AE "Hm?"
    MC "What do you think it means."
    AE "Oh, come on now."
    MC "I think it's about my desire for strength and support in an unknown situation."
    show AE angry
    AE "I think it's about someone who needs more sleep and less caffeine."
    MCT "Hmm, she's not really getting it."
    MC "Alright...tell me yours."
    show AE neutral
    AE "Come now, Hotsure-san, don't be foolish."
    MC "Hey, I told you mine."
    AE "Without my consent or desire."
    "I put on a cute face and spoke in a slow tone."
    MC "Come on, Shiori-san, pleeease~?"
    show AE sad
    AE "Begging...really?"
    "Shiori-san let out a sigh of defeat. She put her hand on her chin and rested it against her knee."
    show AE neutral
    AE "Well...in my dreams, I often see myself climbing a set of white stairs in an old...industrial stairway. I get to the top, and I find myself atop of what I assume to be a tall building. There isn't any light...only fog. The only thing I can see is a blinking red light in the distance."
    MC "..."
    AE "Is that what you wanted to hear?"
    MC "You want to know what I think?"
    AE "You're going to tell me anyway, go ahead."

    if getSkill("Academics") < 2:
        MC "I think...it represents your fear of heights."
        AE "Hmm...do you know what I see?"
        MC "What?"
        show AE angry
        AE "I see a young man, struggling in vain to find answers from a futile source."
        MCT "Oookay, welp, I walked right into that one."
        MC "I mean...am I a little close?"
        show AE neutral
        AE "...Hotsure-san, where are we right now?"
        MC "Um...Seichou?"
        AE "No, no, currently."
        MC "The roof?"
        AE "Why?"
        MC "You wanted us to me--"
        MCT "Oh."
        AE "And the roof is...?"
        MC "Okay, okay, I get it, yeesh."
        AE "You're the Sigmund Freud of dream analysis, Hotsure-san."
        
    elif getSkill("Academics") > 2 and getskill("Academics") < 4:
        MC "I think...you subconsciously believe that you're lonely."
        show AE sad
        AE "..."
        MC "You stand alone. At the top, but alone. It's signifying a deeper fear of alienation."
        show AE angry
        AE "Oh, w-, enough of this nonsense, Hotsure-san."
        MC "Huh?"
        AE "I'll have you know that I don't feel lonely. I've plenty of company, includi--"
        MC "Student council doesn't count."
        AE "..."
        show AE aroused
        AE "Including you."
        MC "..."
        play sound "Audio/Bird.ogg"
        "We stood there, the sounds of the wind carrying with it the chirping of the birds."
        MC "W-...thank you, Shiori-san."
        
    elif getSkill("Academics") >= 4:
        MC "I think...that you're worried about your future."
        AE "...What?"
        MC "Your vision of the horizon, of the top, is completely clouded by fog."
        show AE sad
        MC "You let your fears of isolation completely stop you from being able to visualize a good future for yourself."
        AE "...I...I feel we should stop."
        MC "No, no, I...that was just a little off putting, is all."
        MCT "I must have hit too hard with that."
        
    show AE neutral
    AE "Well...now we at least know each other's dreams, whatever good that does."
    MCT "Eh, I can see I'm not gonna get through to her with the idea."
    MC "Mmm, well, it's nice to know what you think about."
    AE "Presumptively."
    show AE angry
    "Shiori-san let out a grunt as she began to pick her body up. I sprung to my feet and offered a hand to help, but she waved her hand down signifying that she wished to do it on her own."
    AE "M-hrgn...ahn...got it."
    MC "All good?"
    show AE neutral
    AE "Yes, I..."
    "Shiori-san felt the back of her skirt, before shakily feeling under it."
    show AE aroused
    AE "Oh lord."
    "While I couldn't see it all, I'm guessing by the red lines across her thighs that her butt had a bench-shaped pattern etched into the skin."
    show AE sad
    AE "Ugh, this is going to tingle for minutes on end."
    MC "A-ah."
    show AE neutral
    AE "Hmm...well, it's been fun, Hotsure-san, however I must get going."
    MC "O-oh, yeah, okay."
    "Shiori-san turned around and walked towards the door, before turning around to talk to me."
    show AE aroused
    AE "If...if you ever want to come up here with me again...just flag me down."
    MC "Ok...can do."
    hide AE with dissolve
    "Shiori-san opened the door to the stairs and walked down, slowly disappearing from view."
    "I looked up at the blue sky above, and thought about all I learned from Shiori-san's dream. I closed my eyes, and thought about how to spend the rest of the day."
    jump daymenu

#label AE020:
#    scene Office with fade

label AE101:
    scene Gym with fade
    show FMG neutral
    MC "Twelve..."
    FMG "COME ON HOTSURE, GO AT IT LIKE YOU HAVE A PAIR!"
    "Akira-san jeered me on as I lay on the mat...I never even asked her to come over, she just saw what I was doing and started shouting."
    MCT "NNggggh, if I do any more I might end up vomitting. Just. ONE. MORE!!!"
    MC "AGH!"
    "As I reached thirteen, I felt my body give way as I collapsed onto the mat with a loud thud. Akira-san stood over me smiling."
    FMG "So...how do ya feel?"
    MC "Like i'm gonna die."
    FMG "I'm impressed, dude. I've never seen a near fatality from thirteen situps before."
    "Despite my protests, Akira-san picked me up by the shirt with one hand and plopped me down on a bench."
    FMG "Y'know Hotsure-chi, if you wanna build up muscle right, you gotta start off a bit slow, hell, someday you may be able to do more than a seven year old!"
    "Akira-sans boisterous laugh echoed through the gym, as I turned a shade of crimson. I covered my face with a hand and looked to the side to hide my shame when I came across someone who I would have never expected to see here. Akira-san, however, appeared to notice first."
    show FMG neutral at Position (xpos=0.25, xanchor=0.5) with dissolve
    FMG "OOOOOI, Matsumoto-chi, what's up!"
    show AE neutral at Position (xpos=0.75, xanchor=0.5) with dissolve
    "Shiori-san looked over towards our direction and, in acknowledgement to Akira-san's waving, nodded before going back to her clipboard."
    FMG "Awwww, what's with that crap?! Come on over dude!"
    AE "I'm fine, thank you."
    FMG "Aww, come on now, i'm chillin with Hotsure-chi; don't you wanna come over? I can save you a seat on the bench...though you'll probably need two! BAHA!"
    MCT "Ow. I mean, I get it was with good intentions, but that was harsh."
    "Shiori-san closed her eyes and gave a deep inhale, before going back to her examination of...whatever that machine is."
    AE "And have you sweating all over me? No. That won't be happening."
    FMG "Hmmm...aight."
    "Akira-san stood up and out of nowhere..."
    MC "Eh? A-AH!"
    "Lifted up the bench with one arm.  My body lying prone on the bench as Akira-san walked the bench and I over to where Shiori-san stood. Obviously disdainful of the display she was seeing, Shiori-san looked Akira-san directly in her eyes with a scowl on her face."
    AE "Mizutani-san, that is school property! Put that down this instant!"
    MC "W-what about me?!"
    AE "I was talking about you."
    MCT "It hurts just a little."
    FMG "Haha, alright alright."
    "Akira-san placed the bench down with me in tow, still shaking from the experience."
    AE "Back where it belongs."
    FMG "You just said put it down though."
    AE "Nggh...just make sure you put it back before you leave."
    FMG "Can do!"
    "Shiori-san went back to her paperwork unamused as Akira-san started humming to herself."
    FMG "Sooooo, whatcha doin?"
    AE "Taking inventory of the exercise equipment."
    FMG "Bitchin."
    AE "Language!"
    FMG "Ehehe, sorry."
    "Shiori-san was about to go back to her work before she turned around and faced Akira-san, something on her mind as it appeared."
    AE "Actually...why are you here?"
    FMG "Uh, duh! Working out! And I thought you were the braniac."
    AE "You know that's not what I meant. Why would you work out?"
    FMG "Uhh...to gain muscle?"
    AE "But...what? I thought your file stated that you have muscular growth...why would you accelerate it?!"
    FMG "Because it's fun, dude!"
    "Shiori-san seemed somewhat unnerved by this answer."
    AE "Fun? Is that a joke?"
    FMG "Nah...it's who I am. I'm strong, it's kinda my thing."
    AE "I would understand why you would see it as inevitable, but to accentuate it...insulting. Unforgivable."
    FMG "Hey man, I do me and you do you, but I think you might wanna work out too!"
    MCT "Ehhh?!"
    AE "Now you're just saying ridiculous things to cover for yourself. Why would I want to get sweaty and further exhausted then my work is already making me?!"
    FMG "Well, I like gettin big and from the way you talk, it sounds like you don't wanna be big. Maybe a bit of exercise would do something for those ham-hocks of yours."
    MCT "GAH! AKIRA-SAN WHY?!"
    AE "W-why you!"
    "Angered at first, Shiori-san looked like she was about to go off on Akira-san...but her anger gave way to something else. She looked down for a minute and then behind her to her...assets."
    "There was no denying it. Shiori-san had more than just junk in the trunk, she had a full on garbage barge. She slowly moved her hands down to her rear and ran them across the sides of her blooming cheeks. It looked like she had shoved two fleshy globes into her skirt."
    "Despite her best efforts, her undergarments had a noticeable outline on her clothes, leaving little to the imagination as her big bubbly booty jiggled and swayed from side to side with every step. She hated it."
    AE "Is...is that so?"
    FMG "Well, have you tried it?"
    AE "No...I never considered it as an option...all my research indicated that..."
    FMG "Dude, ya can't knock it until you try it!"
    AE "...Very well. Consider this an experiment, I will exercise with you-"
    FMG "Woohoo!"
    "Akira-san snatched the clipboard from Shiori-sans hands, making her jump in shock."
    FMG "You won't be needing this!"
    "Akira snapped the board with a slight movement of her hands."
    AE "...After I am done working....I was using that."
    FMG "O-oh...woops...sorry."
    "Akira-san tried to jam the pieces back together as Shiori-san rubbed her eyes with her fingers."
    MCT "Why do I feel like...this isn't the last time I'll see these two go at it?"
    jump daymenu
    
label AE102:
    scene Hallway with fade
    "And so, we have reached the end of school for the day. I was going to just head back to my dorm room, however I saw Shiori whispered something to Akira before both of them left the room. I was just going to leave it alone, but unfortunately there still outside the classroom for all to hear."
    FMG "For that last time, I an't buttoning my shirt no matter what the stupid dress code says!"
    AE "It is indeed the last time, Mizutani-san, because you WILL be wearing your uniform properly. If you would have listened to me the first time, this wouldn't have been an issue."
    FMG "If you listened the first time, you know I'm not going to button it, not for you or anyone! What is the big deal, it's not like I'm wearing something that shows anything I'm not supposed too!"
    MCT "Ohhh boy, this looks like trouble. If I don't intervene soon these two are going to be going at it for hours."
    show FMG angry at Position (xpos=0.25, xanchor=0.5) with dissolve
    show AE angry at Position (xpos=0.75, xanchor=0.5) with dissolve
    AE "It's not about what you're wearing, it's about what you're NOT wearing. The student handbook page 45-"
    MC "H-hey girls, what's going on?"
    FMG "Little miss honor role here is bugging me about how my shirt isn't buttoned. Oh and by the way, I've been using that handbook to keep the table in my dorm room balanced!"
    AE "Oh so you do know it exists. Good."
    MC "Oookay, yep, that-uh-"
    MCT "Think of something, Hotsure, quick!"
    menu:
        "Defend Shiori":
            jump AE102_c1
        "Defend Akira":
            jump AE102_c2

label AE102_c1:
    MC "Hey, Akira-san, it doesn't seem like that big of a deal. I mean, rules are rules, right?"
    show FMG sad
    FMG "Rules!? Rules!? I thought the whole point of this school was to be comfortable with our bodies, but instead you guys are ganging up on me! *shiff* I would have thought you'd understand Kei!  And Shiori, you're a heartless bitch!"
    "Without so much as a wold, Akira ran off down the hallway with fresh tears falling behind."
    hide FMG
    show AE sad
    AE "N-now Mizutani-san, hold on!"
    "Shiori-san let out a sigh once she realized that Akira-san was long gone."
    show AE angry at Position (xpos=0.5, xanchor=0.5)
    AE "Hotsure-san, why did you have to intervene? I had the situation under control."
    MC "Because if I hadn't that argument could have gotten out of hand, not to mention how it would have gone on forever."
    AE "And a student running off crying isn't out of hand?"
    "Shiori-san took a seat nearby and rested her hand on her head."
    show AE neutral
    AE "I...I'm sorry Hotsure-san. You're right. Mizutani-san made her own decisions, you merely tried to keep the peace."
    MC "And I'm sorry for just running in thoughtlessly."
    AE "Hmm."
    "Shiori-san got up and began to pace, twiddling her fingers behind her back."
    AE "Still, however, Mizutani-san's reactions were a bit more severe than I anticipated. I didn't expect her to start crying and run off. Definitely not a normal reaction to a simple reprimand."
    MCT "She screamed that you were a bitch and you think that's 'a bit' more severe?"
    MC "Well. I mean, she felt cornered and angered."
    AE "That's more than just feeling cornered. I saw it in her eyes. There's more to this, and it has something to do with her shirt. It's only a matter of time until I find out what."
    MCT "..."
    MC "You know, Shiori-san, she did have a point. Why were you so adamant about her shirt?"
    AE "Because it's a rule."
    MCT "Uhhh, ok? That's not what I-"
    AE "Because I must be. I have to."
    show AE sad
    "Shiori-san began nibbling at the end of her thumbnail."
    AE "If I don't, then..."
    MC "...What?"
    AE "..."
    show AE neutral
    AE "Nevermind. It's not a topic for now. If you see Akira-san after this, apologize to her."
    MC "For you?"
    AE "For yourself. My apology will mean nothing to her."
    MC "So...then you're okay with her considering you a 'heartless bitch'."
    AE "Language."
    MCT "Hey, her words!"
    AE "And...yes. That's probably for the best. For now."
    MC "W-what? How c-"
    AE "Good day, Hotsure-san."
    jump daymenu

label AE102_c2:
    MC "Look Shiori, I don't know the whole story but did you ever ask why Akira never has her shirt buttoned?"
    show AE neutral
    AE "What possible explanation could she have for repeatedly breaking the school's mandate? All I know for now is that Mizutani-san is outright defying school legislation, and I refuse to let that happen."
    FMG "Well guess what! I can't wear it buttoned because I don't feel comfortable!"
    AE "It doesn't matter if it is comfortable or not, it's the rules and-"
    show AE angry
    AE "You know what? I've harped on this point enough. This is already enough of a time-vampire as is. Next time, I want to see you conform to the dress code; and Hotsure-san? I would have never expected this level of disregard from you."
    FMG "Leave him out of this, and I hope the door hits your fat ass on the way out!"
    MCT "Oh..."
    show AE surprised
    "Shiori-san gasped in shock. It was obvious that she didn't know how to handle what Mizutani-san just said. She looked at her, then to me, and then, swiftly exiting without a word muttered, began biting her thumbnail."
    hide AE
    show FMG sad at Position (xpos=0.5, xanchor=0.5)
    FMG "*sigh* I swear, that girl better lighten up or she's never going to find a guy, assuming he could get past her extra junk in her trunk."
    MC "Well, it coulda gone better I guess, she could have at least hear you out."
    show FMG neutral
    FMG "Maybe... I also could have handled that better. I only wish she'd see it from my point of view."
    MC "what do you mean by that?"
    "Akira for her part, just exhaled before turning back to me."
    show FMG sad
    FMG "Sorry Kei, but I don't feel comfortable talking about it, maybe another day, maybe not, who knows... who cares..."
    show FMG neutral
    FMG "Anyways, it's probably best if you say sorry to her..."
    MC "In your absence?"
    FMG "Not for me, for you. I get the feeling she's not going to forget the whole 'let the door hit your ass on the way out' comment I made."
    MC "Yeah, probably for the best."
    show FMG sad
    FMG "*sigh* We're only human after all... see you."
    MC "Goodbye Akira."
    jump daymenu