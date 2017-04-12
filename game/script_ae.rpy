define AE = Character('Shiori', color="#FF3300")
define Student1 = Character('Student 1', color="#FF3300")
define Student2 = Character('Student 2', color="#FF3300")
define Student3 = Character('Student 3', color="#FF3300")

image AE neutral = DynamicImage("Graphics/AE-[globalsize]-neutral.png")
image AE happy = DynamicImage("Graphics/AE-[globalsize]-happy.png")
image AE sad = DynamicImage("Graphics/AE-[globalsize]-sad.png")
image AE surprised = DynamicImage("Graphics/AE-[globalsize]-surprised.png")
image AE angry = DynamicImage("Graphics/AE-[globalsize]-angry.png")
image AE aroused = DynamicImage("Graphics/AE-[globalsize]-aroused.png")

init python:
    eventlibrary['AE001'] = {"name": "AE001", "girls": ["AE"], "location": "library", "conditions": [], "priority": 0}
    eventlibrary['AE002'] = {"name": "AE002", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE001"]], "priority": 0}
    eventlibrary['AE003'] = {"name": "AE003", "girls": ["AE"], "location": "campuscenter", "conditions": [[ConditionEnum.EVENT, "AE002"]], "priority": 0}
    eventlibrary['AE004'] = {"name": "AE004", "girls": ["AE"], "location": "dormexterior", "conditions": [[ConditionEnum.EVENT, "AE003"]], "priority": 0}
    eventlibrary['AE005'] = {"name": "AE005", "girls": ["AE"], "location": "hallway", "conditions": [[ConditionEnum.PRESET]], "priority": 0}
    eventlibrary['AE006'] = {"name": "AE006", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE004"], [ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": 0}
    eventlibrary['AE007'] = {"name": "AE007", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.FLAG, "AE006_helpinginoffice"], [ConditionEnum.ISNIGHTTIME]], "priority": 0}
    eventlibrary['AE008'] = {"name": "AE008", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE007"], [ConditionEnum.ISNIGHTTIME]], "priority": 0}
    eventlibrary['AE009'] = {"name": "AE009", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE008"], [ConditionEnum.ISNIGHTTIME]], "priority": 0}
    eventlibrary['AE009'] = {"name": "AE010", "girls": ["AE"], "location": "office", "conditions": [[ConditionEnum.EVENT, "AE009"], [ConditionEnum.ISNIGHTTIME]], "priority": 0}
    eventlibrary['AE100'] = {"name": "AE100", "girls": ["AE", "FMG"], "location": "gym", "conditions": [[ConditionEnum.GAMETIME, ConditionEqualityEnum.GREATERTHAN, datelibrary["testday"]]], "priority": 0}
    
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
    "It's weird, when you think you're alone, but then learn another person is there your body just tenses up a bit."
    extend " Though that may very well be Shiori's presence. She was someone who just emanated a strict and commanding aura..."
    extend " but still I felt as though I should at least try to socialize."
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
    extend " There are so many questions I have, and I plan to make sure they are all answered."
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
    "I picked up the book and read the title, ‘An examination of Cellular Reproduction'."
    MCT "But why would she... I guess it's not too important. I'll just make sure she gets it next time I see her."
    MCT "Well, so much for a relaxing time in the library, eh?"
    jump daymenu

label AE002:
    scene Library with fade
    MCT "Maybe Shiori-san is here again today."
    "As my mind recalled yesterday's events, I began to wander about the Library. The sheer size of the place was a stark reminder of just how large the school was...and how unlikely it would be to find Shiori in it so quickly."
    MC "Let's see...ah!"
    "It was only now I noticed the door with the sign 'Student Organizations' directly on top of the door frame on the opposite side of the room."
    scene Office with fade
    "As I moved across the library to the door, I began to notice that, like yesterday, not many people were here. Reading just isn't as popular a pastime as it used to be. I saw her through the large window in the wall separating the Library from the room, where she was working on a stack of papers."
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
    "I take the book from my bag and put it on the table next to Shiori-san."
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
    MC "She gave a deep breath, and though her face still showed a tinge of pink, she appeared to instantly regain her composure."
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
    MCT "Damint! This is bad. This needs to be done by tomorrow! This is the only notebook I have...uh, had, and the store is on the other side of campus. If I run over I-"
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
    "We got to work, and Shiori-san began filling out forms at neck cracking speeds. Every other minute was the sound of scribbling, stamping, and then sliding a paper to me. I nearly choked for a second, before taking the files in hand and bringing them to the cabinet."
    "The names went on and off the desk like lightning, and it honestly felt like for every paper I would take off the desk and file, two more would take it's place. A document-hydra. By the time the stream stopped, I was nearly panting from the quick, bustling motion of it all."
    "The scribbling and stamping had stopped now, and as I grabbed the last few files, I looked back on the pile of files and I realized..."
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
    AE "Ah, observant of you, Hotsure-san. Yes. I came in early this morning and filled out some forms in anticipation for your training."
    MCT "Early this morning? How did she get all of these done before class?"
    MC "Oh, uh, thanks Shiori-san, but...how early did you wake up?"
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
    MC "Definately."
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
    AE "...Yes...I'm well aware."
    MC "I don't think I'll be needing to shift around that much, but I mean, you sit right in front of me."
    AE "Ye-"
    MCT "...huh?"
    "Shiori-san stopped for a moment, moving her hand a bit closer to her mouth before hesitating. It was faint, but she was lightly blushing."
    AE "Behind me..."
    MC "Shiori-san? Did you forget?"
    AE "N-no. I merely thought of some things that I...hadn't previously taken into account."
    MC "Uh...ok?"
    AE "I can trust you to..."
    MC "Huh?"
    MCT "Tooo...?"
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
    "I walked out of the office door and into the library, ready to finally get some fresh air and sunlight...well, until something hit me. I was at the door of the library when I was hit with a wave of curiosity. Call it a compulsion, a random stroke of unease, whatever, but for some reason I had a suspicion about Shiori-san after I left. I realize that most would consider it crazy, even a bit creepy, but I felt the need to take a quick look back at Shiori-san before I left. Walking up to the office window, I peeked in."
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
    MCT "Hmm? Wait...Shiroi-san?"
    "Shiori-san stood by the entrance to the library, holding a stack of yellow sheets in both arms. The spectacled girl had her back against the hallway wall, looking at me from the side."
    MC "Hey, Shiori-san! Have you been waiting out here for me?"
    show AE neutral with dissolve
    AE "Good day, Hotsure-san, I had to get these papers from inventory, so I figured we would meet here around the same time."
    MC "Need me to get those?"
    "Shiori-san stepped back a bit when I put my hands out."
    show AE sad
    AE "N-no, it's fine."
    MC "Okay, then. Here, let me get the door."
    "I held the door for a bit before Shiori-san looked at me with determined eyes."
    show AE neutral
    AE "You go first."
    MC "Um...Alright then."
    
    scene Library with fade
    "We walked through the library, Shiori-san following closely behind me, until we reached the office door."
    MC "Want me to take those, so you can unlock it?"
    show AE with dissolve
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
    show AE neutral
    AE "Yes, well...I suppose that we're the same in that regard."
    "Shiori-san pointed at my head in the same way one would when trying to tell someone there was something on my face."
    MCT "Huh? What is she...?"
    "I looked off the the side to catch a glimpse when I saw it."
    "Completely going unnoticed by me until now, my hair was definitely longer. Feeling around the back of my neck, I noticed that it went past my nape at this point, and flowed to bottom of my neck."
    MC "Wait...how did this? When did it get this long?"
    AE "You never noticed?"
    MC "No, I..."
    "I sat in confusion for a moment, trying to get a full grasp of just how my hair had grown this long without my knowledge, when I noticed Shiori-san quietly sit down and face her back to the wall. That's when it hit me."
    MC "Shiori-san...are you also?"
    AE "...Also what?"
    MC "Well, if my hair has grown like this for the relatively short time I've been here, then...have you also?"
    "Shiori-san shrunk back a bit, eyes intently glaring at me."
    show AE angry
    MCT "I'll take that as a yes."
    AE "Well..."
    MC "And that's why you've been hiding your back."
    MCT "Now that i'm saying it out loud, I'm starting to realize how dumb I was for not noticing it earlier."
    if getAffection("AE") >= 4:
        "Shiori-san winced a bit when she realized that her gambit had been called, then sighed when she finally resigned to the inevitable."
        show AE sad
        AE "...Yes. Yes it is."
        "Shiori-san let out as sigh. Of relief or frustration, I couldn't really tell."
        show AE neutral
        AE "Well, if I keep trying to hide myself then it seems neither of us will be able to get our work done."
        AE "So I want you to...get it out of your system now." 
    else:
        "Shiori-san looked at me fiercely, an angry scowl spread across her face in return for what she took as grave disrespect."
        show AE angry
        AE "N-now hold on! I would recommend you keep your comments to yourself."
        MC "Shiori-san?"
        AE "My personal affairs are my own, and if I choose to...evade your gaze, I have every right to."
        MC "Sorry, I didn't mean anything by it."
        show AE neutral
        AE "Look. Just get it out of your system now so we can continue our day."
    "Shiori-san took her back away from the wall and finally did it."
    MC "Out of my system? Shiori-san, I'm not going to insult y-"
    "Shiori-san finally turned around."
    #Zoom-in or CG or something?
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
    show AE neutral
    AE "It's fine, Hotsure-san. I realize that it's...off putting, but now that that's over, we can continue work uninterrupted."
    MC "Y-yeah."
    "I got to work on the stack of last time's papers. An awkward silence permeated the room as we both tried to get over what had just happened. I kept trying to focus on my job, but my mind kept racing back to the image of Shiori-sans rear."
    MCT "Damn it, how was that supposed put my mind at ease again?!"
    MCT "I gotta at least try to start off a conversation, if I don't I'll be standing here all day."
    MC "Did..."
    AE "Hmm?"
    MC "Did that happen over night?"
    AE "...I don't believe so. It's just that I need a larger uniform and I've yet to get one, is all."
    MC "I would have figured that you would ordered early."
    AE "I did. As it so happens there was a backlog."
    "Shiori-san took another stack of yellow papers and placed them on her desk."
    AE "This is the backlog."
    MC "So, that's what those were."
    AE "Yes, and the sooner it's done the sooner I can get out of this embarrassing situation."
    MC "So, what, then students just have to wait until their clothes get too big?"
    AE "Well, yes, however the School has a partnership with a local tailor. If you pay a premium then you can get your clothes fixed at any time."
    MC "Oh, really? I didn't know that."
    AE "Most students don't, to be honest. That's why the student council is thinking of ways to get the message out."
    MC "Why don't you do that? Get your clothes fitted?"
    AE "..."
    "Shiori-san sat in silence for a moment, but spoke up again after a brief period."
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
    AE "I think it goes without saying, but...could you not bring up earlier to anyone? I showed you...why I was worried in order to ease your mind, nothing else."
    MC "Oh, don't worry about it. It's okay, I mean, as long as you don't go around talking about my rat's-nest hair."
    AE "I won't."
    MC "Cool."
    scene Library with fade
    "As we walked out, I couldn't help but catch a glimpse of Shiori-san's butt. It wobbled as she shuffled along, swishing side to side as the bottom of her skirt fabric swayed with her movements."
    MCT "H-hey, c'mon man, don't."
    "My eyes snapped back up to attention, thankfully keeping me from running into the library door frame. I walked out, and headed into the hall to continue my day."
    jump daymenu

label AE100:
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