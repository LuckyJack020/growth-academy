define BBW = Character('Alice', color="#CC33FF")
define Lunch = Character('Lunchlady', color="#CC33FF")
define Francois = Character('Francois', color="#CC33FF")

image BBW neutral = DynamicImage("Graphics/BBW-[globalsize]-neutral.png")
image BBW happy = DynamicImage("Graphics/BBW-[globalsize]-happy.png")
image BBW sad = DynamicImage("Graphics/BBW-[globalsize]-sad.png")
image BBW surprised = DynamicImage("Graphics/BBW-[globalsize]-surprised.png")
image BBW angry = DynamicImage("Graphics/BBW-[globalsize]-angry.png")
image BBW aroused = DynamicImage("Graphics/BBW-[globalsize]-aroused.png")
image BBW haughty = DynamicImage("Graphics/BBW-[globalsize]-haughty.png")

init python:
    eventlibrary['BBW001'] = {"name": "BBW001", "girls": ["BBW"], "conditions": [], "priority": 0}
    
label BBW001:
    MC "Well! That was... a first day. I didn’t expect the school to be exactly like my old one, but on a list of unexpected surprises I didn’t think..."
    MC "OK, I guess I couldn’t have expected it for it to be a surprise."
    extend " But still, if the teacher had ripped off his face to reveal an alien underneath I wouldn’t have been more surprised. At least food is familiar enough. A nice snack after class is normal, right?"

    UNKNOWN "I’m sorry, you must not know who you’re talking to."

    MC "I wonder who that is."

    "Alice, accompanied by a man in a chef’s outfit, is arguing with an older (but not ancient) woman in an apron and hairnet."

    show BBW angry with dissolve
    
    BBW "The name is Alice Nikumaru."
    extend " I am sure there was some kind of memorandum circulated among the staff announcing my arrival at this school."
    extend " A missive to let you all know that I am here and that special accommodations to satisfy me would be instituted."

    Lunch "If you have an allergy or other dietary need, I would have been told."

    BBW "You there. Tell... Madame Hairnet here who I am."

    MC "She’s a student. She’s in my class."

    show BBW haughty with dissolve
    
    BBW "I am THE student, as far as you are concerned. You may see hundreds of others passing down your line as you ladle warmed over spaghetti sauce onto rubber pasta, but I am not just another stomach to fill."

    MCT "You didn’t hear the part about me being in your class, did you?"

    BBW "The meals you mass-produce for the student body may be satisfactory given the level of culinary talent you possess, but I have greater needs."
    extend " Francois here studied at the finest institutes in France, Italy and Japan, all for the sake of honing his skills to a level suitable for me."

    Lunch "We make enough food for even the fat kids. Don’t worry, you’ll get your share."

    show BBW angry with dissolve
    
    BBW "I am NOT some “fat kid”. I am not even obese."

    show BBW neutral with dissolve
    
    BBW "And it is not a matter of quantity, but quality. My palate is a delicate instrument that needs to be handled with care."
    extend " I have certain expectations that you – as qualified for this job as you may be – can not meet."
    extend " Now, I’ve already gone to the trouble of ordering the equipment you probably don’t have – wood-fire pizza oven, rotisserie, espresso machine, meat smoker; just a few odds and ends – but he will need, say, 20%% of your workspace emptied out and handed over to him."

    Francois "And deliveries."

    show BBW happy with dissolve
    
    BBW "Of course. And he needs to have deliveries made every day, so if you could give him the address and directions to this building, that would be wonderful."

    MCT "Oh, is that all? Your own private chef and special deliveries every day? Just how loaded is this girl?"

    Lunch "Students don’t get to bring private chefs with them, princess. Outsiders don’t get access to our kitchen or any other facilities on campus. Either you can take what we offer you, or you can make your own meals in the Home Ec classes."

    show BBW angry with dissolve
    
    BBW "What? Francois can not perform at his best in a classroom kitchen. He needs a full assemblage of utensils and appliances-"

    Lunch "I said you can make your meals."
    extend " Yourself."

    show BBW haughty with dissolve
    
    BBW "Do you really expect me to subject my dainty hands and creamy skin to the raw ingredients that come with making a three-star meal?"
    extend " Do you have any idea how much this manicure costs? What would handling an ox tongue or a raw Cornish game hen do to it?"

    Lunch "If you don’t get out of my kitchen in the next five seconds, you’ll be dunking that expensive manicure in cold, greasy dishwater as I have you scrubbing every pot and pan we have."

    show BBW angry with dissolve
    
    BBW "You... You wouldn’t."

    Lunch "You wouldn’t be the first student punished with kitchen duty."

    BBW "Very well, but this is not the end. A Nikumaru does not give up."

    show BBW neutral with dissolve
    
    BBW "Did you see that?"

    MCT "Did you forget that you talked to me not two minutes ago?"

    menu:
        "Yeah. Typical hard-ass school employee, being cruel for the sake of it.":
            jump BBW001_c1_1
        "That was kind of harsh. She could at least have tried to work something out with you.":
            jump BBW001_c1_2
        "I’ve heard of spoiled little girls, but your own private chef? That’s a whole new level.":
            BBW "Is it ‘spoiled’ to have the best that money can buy? I am Alice Nikumaru."
            jump BBW001_c1_after

label BBW001_c1_1:
    show BBW haughty with dissolve
    
    BBW "Maybe this is how they do it at lesser institutions, by in my experience schools exist for the betterment of the students."
    extend " If this is a taste of how this place operates, perhaps transferring is the sensible thing. There must be other schools that can handle my needs."

    MC "I guess if you can have a private chef, you can also have a private tutor."

    jump daymenu

label BBW001_c1_2:
    BBW "Absolutely. Life is filled with give and take, and she wouldn’t even come to the negotiating table. How is it that so many people can not understand the basics of business deals?"

    MC "Fancy yourself something of a business woman, eh?"
    
    show BBW happy with dissolve
    
    BBW "I know a lot about how the world works. It’s an inherited trait."
    jump BBW001_c1_after

label BBW001_c1_after:
    show BBW neutral with dissolve
    
    BBW "Perhaps you’ve heard of my father, Daitaro Nikumaru?"
    menu:
        "Daitaro... Isn’t he some sort of businessman?":
            jump BBW_c2_1
        "Oh, yeah! He’s the guy who plays in that traveling jug band, isn’t he?":
            jump BBW_c2_2

label BBW_c2_1:
    show BBW happy with dissolve
    
    BBW "Not just ‘some sort’ of businessman. He is the leader of the heavy manufacturing and seafood industries in Japan. He is ranked on the list of the richest people in the world."
    
    MC "Consider me impressed. But if he’s so rich, couldn’t he just buy this school and install Francois as head chef?"
    
    show BBW neutral with dissolve
    
    BBW "Francois is not a garden-variety chef you can put in charge of just any mess of underlings. His talent is best utilized when he can focus on a single diner’s menu."
    extend " But you do raise a good point. Perhaps I should have a chat with Father."
    
    hide BBW

    MC "I- Is she really going to ask her father to buy this school? Just because she doesn’t want to eat the cafeteria food?"
    jump daymenu
    
label BBW_c2_2:
    show BBW angry with dissolve
    
    BBW "* scoff * Is there not a single ounce of class or breeding in this place?"
    
    hide BBW
    
    MC "I’d settle for an ounce of humor."
    jump daymenu