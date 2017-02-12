define AE = Character('Shiori', color="#FF3300")

image AE neutral = DynamicImage("Graphics/AE-[globalsize]-neutral.png")
image AE happy = DynamicImage("Graphics/AE-[globalsize]-happy.png")
image AE sad = DynamicImage("Graphics/AE-[globalsize]-sad.png")
image AE surprised = DynamicImage("Graphics/AE-[globalsize]-surprised.png")
image AE angry = DynamicImage("Graphics/AE-[globalsize]-angry.png")
image AE aroused = DynamicImage("Graphics/AE-[globalsize]-aroused.png")

init python:
    eventlibrary['AE001'] = {"name": "AE001", "girls": ["AE"], "conditions": [], "priority": 0}
    
label AE001:
    "After a long day, I figured that some time in the library would do well for me. I could use somewhere quiet to wind down."
    
    MCT "Geez, I expected quiet, but this room is practically abandoned!"
    
    "Even though a few hours had passed, what Tashi-sensei said was still ringing in my head. I wasn’t completely sure how to process what had been going on, but I was worried to say the least."
    
    MCT "I need to sit down...the table over there looks good."
    
    "I grabbed a chair, sat down at the table and, resting my head on my hands, I let out a long sigh."
    
    MC "Well, I never got anywhere by just moping... right?"
    
    AE "*Ahem*"
    
    MC "Eh?"
    
    "I looked over to the table adjacent, where I saw Shiori-san flipping through the pages of a large book."
    
    show AE angry
    with dissolve
    
    MC "A-ah! Shiori-san, how are y-"
    
    AE "Hotsure-san, adjust your volume in the library, please."
    
    MCT "Oh...right."
    
    MC "Sorry, Shiori-san."
    
    show AE neutral
    with dissolve
    
    AE "Hm."
    
    hide AE with dissolve
    
    "Shiori looked back down to her book, eyes fixated on the page in front of her. She adjusted her slowly slipping glasses and turned to the next page."
    
    MCT "Ok, I guess I’ll just...sit here."
    
    "The silence in the room was palpable."
    "It’s weird, when you think you’re alone, but then learn another person is there your body just tenses up a bit."
    extend " Though that may very well be Shiori’s presence. She was someone who just emanated a strict and commanding aura..."
    extend " but still I felt as though I should at least try to socialize."
    
    MCT "Should I just move over to her table? Would that be intrusive?"
    
    "I moved over and sat a seat away from where she was, better to be near and speak softly than far and shout I supposed."
    
    MC "So... hey."
    
    "Shiori looked up from her book, glancing at me with an apathetic gaze."
    
    show AE neutral with dissolve
    
    AE "...Hello, Hotsure-san."
    
    MC "How, uh, w-what are you doing?"
    
    MCT "Uaaah, she’s absolutely chilling me to the bone!"
    
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
            MCT "I...don’t really think I do, actually. She’s busy. I shouldn’t bother her."
            jump AE001_after
        "You're worried, aren't you?":
            jump AE001_c3
            
label AE001_c1:
    MC "So...Shiori-san. How are you handling this?"
    
    AE "..."
    extend "I suppose...I just need to further my understanding of the situation. That’s all. It’s unlikely that my situation is anything to worry about, anyway."
    
    MCT "That...didn’t really answer my question."
    jump AE001_after
    
label AE001_c3:
    $ setAffection("AE", -1)
    MC "The reason you’re in here...you’re worried about this whole thing, right?"
    
    show AE angry with dissolve
    
    "Shiori-san stopped writing for a moment and looked up towards me again, with an annoyed look on her face."
    
    AE "How astute of you to presume my emotions after only a day of meeting me. No. I’m not worried about this, and I think it would be best if you didn't say asinine things so bluntly."
    
    MC "A-ah! I meant no...I’m sorry."
    
    "Shiori looked back down at her book, and I felt a chill run down my spine after the talking she gave me."
    
    MCT "What the hell was I thinking?!"
    
    show AE neutral with dissolve
    
    jump AE001_after
    
label AE001_after:
    "We sat in silence a bit more, until I noticed something...I couldn’t hear Shiori writing anymore."
    
    MCT "Eh? Is she done taking notes already?"
    
    "I looked over at Shiori, who had stopped writing mid-sentence. Her eyes seemed focused on a particular line, and her mouth opened slightly as she read."
    
    show AE sad with dissolve
    
    AE "What? But...no...that can’t be true..."
    
    MC "S-Shiori-san...are you ok?"
    
    AE "Yes, I...I just...I have to go. Pardon me, Hotsure-san."
    
    "I could do little but stammer as Shiori quickly stood up, her rear tilting the chair back on its hind legs before she turned and walked away."
    "The clack of the front legs against the floor as the chair dropped level made Shiori flinch, but she had regained her composure in an instant and kept on walking."
    
    hide AE
    
    MC "Shiori-san...hm?"
    
    "I looked over to where Shiori was sitting, and found that she had forgotten to take her book with her."
    
    MC "Ah! Her book!"
    
    MCT "What... do I do? Should I just take it and bring it back to her?"
    MCT "..."
    MCT "I guess it wouldn’t hurt...if I checked it out and brought it back to her tomorrow."
    
    "I picked up the book and read the title, ‘An examination of Cellular Reproduction’."
    
    MCT "But why would she… I guess it’s not too important. I’ll just make sure she gets it next time I see her."
    
    MCT "Well, so much for a relaxing time in the library, eh?"
    
    jump daymenu
    