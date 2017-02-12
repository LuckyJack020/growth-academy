define GTS = Character('Naomi', color="#66FF33")

image GTS neutral = DynamicImage("Graphics/GTS-[globalsize]-neutral.png")
image GTS happy = DynamicImage("Graphics/GTS-[globalsize]-happy.png")
image GTS sad = DynamicImage("Graphics/GTS-[globalsize]-sad.png")
image GTS surprised = DynamicImage("Graphics/GTS-[globalsize]-surprised.png")
image GTS angry = DynamicImage("Graphics/GTS-[globalsize]-angry.png")
image GTS aroused = DynamicImage("Graphics/GTS-[globalsize]-aroused.png")

init python:
    eventlibrary['GTS001'] = {"name": "GTS001", "girls": ["GTS"], "conditions": [], "priority": 0}
    
label GTS001:
    "The words from Tashi-Sensei stayed with me long after class had concluded. I just wasn’t sure how to properly process what we were told."
    "What Daichi had told me earlier was starting to resonate more and I began to wonder if perhaps others knew about the purpose of this school before they were enrolled into it."
    "I hadn’t realized how long I was lost in my own thoughts until I finally noticed my surroundings; I was at the school’s garden."
    
    "It was nice here, the breeze along with the sounds of leaves and grass moved by the flow of wind had a sort of calming factor to them."
    "I stood there for a few moments longer until a figure walked beside me, catching me by surprise."
    
    show GTS neutral
    
    MC "Huh? Oh Naomi. sorry, I wasn’t aware you were here."
    
    GTS "It’s alright Keisuke. I shouldn’t have intruded unannounced."
    
    "She stood there, smiling ever so slightly, the flow of wind causing her long hair to dance ever so tenderly until I decided to break the silence."
    
    MC "So what are you doing here in the garden?"
    
    GTS "Oh, I merely wanted to spend a little more time here. Reflect on my thoughts and think about how the day went so far."
    
    MC "I see, were you also possibly thinking about what Tashi Sensei told us earlier?"
    
    GTS "A little yes, I think many of the students are. Were you as well?"
    
    MC "Yeah I was. It really came out of left field so I guess I needed some time to think about it."
    
    menu:
        "What do you think about it?":
            jump GTS001_c1
        "I'm curous about what changes I might go through...":
            jump GTS001_c2
        "I’m concerned about what that might mean for my little sister honestly.":
            jump GTS001_c3
            
label GTS001_c1:
    GTS "It’s a little concerning I will admit; however, I think some of those feelings come from the sudden nature in which we were told."
    GTS "I’m sure if we take more time to process it and reflect on it, the situation won’t feel as frightening as it possibly does for some."
    extend " Thank you for asking though."
    
    MC "No problem, we’re all in this together, after all right?"
    
    GTS "An interesting way to put it, but indeed I would say so."
    
    jump GTS001_after

label GTS001_c2:
    GTS "It’s good to see you’re looking at the news with more curiosity rather than concern. It’d be rather pointless to worry about it now, especially without knowing all the facts first."
    extend " I’m sure they have methods to tell what will be changing in us, though I’m sure with some students it’d be more obvious than others."
    extend " Oh sorry! That sounded rather rude didn’t it? I don’t mean to judge any of the other students."
    
    MC "Heh, it’s okay Naomi I can tell you’re not the type to do that."
    
    GTS "Thank goodness, I wouldn’t want to start making the wrong impression on the first day of school after all."
    
    jump GTS001_after

label GTS001_c3:
    GTS "Oh? You have a younger sister Keisuke?"
    
    MC "Yeah, she’s going to school here too."
    extend " I’m just thinking about what Sensei said, about how sometimes siblings are transferred to this school simply because of the results of the other."
    extend " I’m sure I can cope with whatever might happen to me, but I’m worried about her. I just don’t want her to go through something that might hurt her."

    GTS "It’s only natural to worry as the older sibling Keisuke, but you mustn’t let it concern you too much. There’s no way to know for certain at the moment, so it’s best to just be hopeful and keep your chin up."
    
    MC "Yeah I guess that’s true. Sorry for sounding like a mother hen here."

    GTS "It’s not worry Keisuke, like I mentioned it’s just natural to feel that way. I know I’m very much the same with my own sister."

    MC "You have a sister too?"

    GTS "Yes, she’s much younger though so there’s no worry about her predicament in this situation. But just know that you’re not the only one who can sometimes come off as a mother hen."

    jump GTS001_after

label GTS001_after:
    "She gave a soft chuckle and kept her warm smile."
    "I guess she must have noticed me staring, because she soon chimed in."

    GTS "It’s quite rude to stare."

    "There was a hint of red on her cheeks as she said that."

    MC "O-Oh! Sorry… I was just thinking again haha… so are you going to be doing anything else later today?"
    
    "She placed a finger on her lip as she thought about her plans for the evening before finally replying."

    GTS "Well I had planned to return to my dorm room so I can tell my family about how my first day went. I just wanted to see the garden a little bit before I did so."
    GTS "However, I do plan to explore the garden later this evening. There’s a surprisingly large variety of flowers here."
    extend " At least more than I would expect so I want to make a mental list of what’s here and maybe ask the groundskeeper about where they obtained the seeds for them."

    MC "Oh I see; I won’t hold you up then. I should probably do the same myself really. I’m sure my family would love to hear about how my day went as well. I’ll see you around Naomi."

    GTS "Farewell Keisuke, I hope the rest of your day goes well. Do try to visit the garden every so often, you’ll be surprised how much good can come from resting in a garden for a few moments."

    MC "Heh, I might take you up on that advice. Later Naomi."

    "She gave me a small bow before I departed."
    
    jump daymenu