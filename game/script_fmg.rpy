define FMG = Character('Akira', color="#FF9900")

image FMG neutral = DynamicImage("Graphics/FMG-[globalsize]-neutral.png")
image FMG happy = DynamicImage("Graphics/FMG-[globalsize]-happy.png")
image FMG sad = DynamicImage("Graphics/FMG-[globalsize]-sad.png")
image FMG surprised = DynamicImage("Graphics/FMG-[globalsize]-surprised.png")
image FMG angry = DynamicImage("Graphics/FMG-[globalsize]-angry.png")
image FMG aroused = DynamicImage("Graphics/FMG-[globalsize]-aroused.png")

init python:
    eventlibrary['FMG001'] = {"name": "FMG001", "girls": ["FMG"], "conditions": [], "priority": 0}
    
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

    show FMG neutral with dissolve
    
    FMG "Well hey there...um your name was Keisuke right?"

    MC "Indeed it is."

    FMG "Alright, Keisuke, got it...So as I was saying...what brings you to these parts?”"

    MC "Curiosity mostly, I wanted to checked out the Athletics Area to get a better layout of the school and when I got here I heard an echo that lead me to you."

    show FMG happy with dissolve
    
    FMG "And here I was thinking you were here to check me out."

    "The way she said that sounded she was joking, but I just found it kinda awkward, still it would be a bit rude not to give some sort of reply."

    "My only response was a light chuckle and then silence. We stood there for about 30 seconds till I spoke up."

    MC "So Akira...how are you holding up?"
    
    show FMG neutral with dissolve
    
    FMG "huh, what do you mean?"
 
    MC "Well, I mean that we're going have these 'growths' affect the rest of our lives, so what I’m asking is how you’re taking this?"

    show FMG happy with dissolve
    
    FMG "Oh, in that case I’m fine with it."

    MC "Huh, really?"

    show FMG neutral with dissolve

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

    show FMG sad with dissolve
    FMG "Ah crap! It’s 5:35 I’m five minutes late for my routine!"

    hide FMG
    "She said while running past me to the door."

    MC "Wait huh?"

    "Was all I could say in flustered state. Akira then turned around jogging in one spot for a brief moment."

    show FMG sad with dissolve
    FMG "Sorry! I have to go now, if you want to talk you can find me here whenever theres no classes or at the local Gym, later!"

    "And in a flash, Akira proceeded to sprint out the door, leaving me in the same spot, still a bit confused."

    MC "Well that happened."

    "With that I left the building."
    
    jump daymenu