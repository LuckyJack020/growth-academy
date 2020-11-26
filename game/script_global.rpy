#Characters
define MC = Character('Keisuke', color="#0066CC", image="MC") # Main Character, speaking.
define MCT = Character('Keisuke', color="#0066CC", what_prefix='(', what_suffix=')', image="MC")
define MCCell = Character('Keisuke', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="MC")

define AE = Character('Shiori', color="#FF3300")
define BBW = Character('Alice', color="#CC33FF")
define BBWCell = Character('Alice', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="BBWCell")
define BE = Character('Honoka', color="#FCCF20")
define BECell = Character('Honoka', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="BECell")
define FMG = Character('Akira', color="#FF9900")
define GTS = Character('Naomi', color="#66FF33")
define GTS_S = Character('Naomi', color="#66FF33", image="GTS_S")
define GTSCell = Character('Naomi', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="GTS_S")
define PRG = Character('Aida', color="#FF3399", what_prefix='{size=-6}', what_suffix='{/size}')
define PRGCell = Character('Aida', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="PRGCell")

define Akihiro = Character('Akihiro', color="#C0C0C0")
define Ama = Character('Amatsu-san', color="#ffc3b5")
define Chibuki = Character('Chibuki', color="#CC33FF")
define Chie = Character('Chie', color="#FF9900")
define Francois = Character('François', color="#CC33FF")
define Fujimoto = Character('Fujimoto', color="#FF9900")
define Fumika = Character('Fumika', color="#FF91DC")
define Hamikawa = Character('Hamikawa', color="#C0C0C0")
define Haruhiro = Character('Haruhiro', color="#C0C0C0")
define HR = Character('Tashi-sensei', color="#C0C0C0")
define Kanami = Character('Kanami', color="#C0C0C0")
define Kazumi = Character('Kazumi', color="#C0C0C0")
define Koneko = Character('Koneko', color="#C0C0C0")
define Miko = Character('Miko', color="#C0C0C0")
define Minei = Character('Minei', color="#C0C0C0")
define Misaki = Character('Misaki', color="#C0C0C0")
define Miura = Character('Miura', color="#C0C0C0")
define Minori = Character('Minori', color="#FF91DC")
define Mom = Character('Mom', color="#FF3300")
define Naoki = Character('Naoki', color="#C0C0C0")
define Natsuko = Character('Natsuko', color="#C0C0C0")
define Nurse = Character('Nurse', color="#FF91DC")
define RM = Character('Daichi', color="#BDB8A5")
define Ryoko = Character('Ryoko', color="#FF91DC")
define Sakie = Character('Sakie', color="#C0C0C0")
define Sakura = Character('Sakura', color="#FF3399")
define Takamura = Character('Takamura-Sensei', color="#FF9900")
define TakaraUnknown = Character('Aida\'s Mother', color="#C0C0C0")
define Takara = Character('Takara', color="#C0C0C0")
define Tako = Character('Tako', color="#ce9b50")
define Tomoko = Character('Tomoko', color="#FF3300")
define TomokoCell = Character('Tomoko', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="TomoCell")
define TS = Character('Tsubasa-sensei', color="#C0C0C0")
define Yuki = Character('Yuki', color="#FF91DC")

define All = Character('Everyone', color="#ffffff")
define Announcer = Character('Announcer', color="#C0C0C0")
define Barker = Character('Barker', color="#C0C0C0")
define Card = Character('Card', color="#C0C0C0")
define Cashier = Character('Cashier', color="#C0C0C0")
define Cell = Character('Cell', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define CMM = Character('Male Council Member', color="#ffa18a") #Lighter Orange
define CMF = Character('Female Council Member', color="#ffa18a") #Lighter Orange
define Coach = Character('Coach', color="#C0C0C0")
define Computer = Character('Computer', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define DJ = Character('DJ', color="#C0C0C0")
define FemStudent1 = Character('Female Student 1', color="#ce6950") #New color maybe?
define FemStudent2 = Character('Female Student 2', color="#ce9b50") #New color maybe?
define Girls = Character('Girls', color="#ffffff")
define Guard = Character('Guard', color="#C0C0C0")
define Hostess = Character('Hostess', color="#C0C0C0")
define LittleGirl = Character('Little Girl', color="#FF91DC")
define Judge = Character('Judge', color="#C0C0C0")
define Letter = Character('Letter', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Lunch = Character('Lunchlady', color="#CC33FF")
define Note = Character('Note', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Owner = Character('Store Owner', color="#C0C0C0")
define Principal = Character('Principal', color="#C0C0C0")
define Receptionist = Character('Receptionist', color="#C0C0C0")
define Student = Character('Student', color="#FF3300")
define Student1 = Character('Student 1', color="#FF3300")
define Student2 = Character('Student 2', color="#FF3300")
define Student3 = Character('Student 3', color="#FF3300")
define Teacher = Character('Teacher', color="#C0C0C0")
define UNKNOWN = Character('???', color="#FFFFFF")
define UNKNOWNCell = Character('???', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Umpire = Character('Umpire', color="#C0C0C0")
define Vendor = Character('Vendor', color="#FFFFFF")
define Waiter = Character('Waiter', color="#C0C0C0")
define Waitress = Character('Waitress', color="#C0C0C0")

#Scenes
image white = Solid((255, 255, 255, 255))
image black = Solid((0, 0, 0, 255))

image Lake Road = DynamicImage("Graphics/ui/bg/lakeroad.png")
image School Front = "Graphics/ui/bg/schoolfront.png"
image School Inner = "Graphics/ui/bg/schoolinner.png"
image Gate Front = "Graphics/ui/bg/gatefront.png"
image School Planter = "Graphics/ui/bg/schoolplanter.png"
image Hallway = "Graphics/ui/bg/hallway.png"
image Classroom = DynamicImage("Graphics/ui/bg/classroom_[gametime].png")
image Dorm Exterior = "Graphics/ui/bg/dormexterior.png"
image Dorm Interior = "Graphics/ui/bg/dorminterior.png"
image Campus Center = DynamicImage("Graphics/ui/bg/campuscenter_[gametime].png")
image Auditorium = "Graphics/ui/bg/auditorium.png"
image School Exterior = "Graphics/ui/bg/schoolexterior.png"
image F1 Hallway = "Graphics/ui/bg/schoolhallway1.png"
image Library = "Graphics/ui/bg/library.png"
image Office = DynamicImage("Graphics/ui/bg/office_[gametime].png")
image Cafeteria = "Graphics/ui/bg/cafeteria.png"
image Cooking Classroom = "Graphics/ui/bg/cooking.png"
image Music Classroom = DynamicImage("Graphics/ui/bg/music_[gametime].png")
image Art Classroom = "Graphics/ui/bg/NYI.png"
image Gym = "Graphics/ui/bg/auditorium.png"
image Track = DynamicImage("Graphics/ui/bg/track_[gametime].png")
image Roof = "Graphics/ui/bg/roof_day.png"
image Nurse Office = DynamicImage("Graphics/ui/bg/nurseoffice_[gametime].png")
image Pool = "Graphics/ui/bg/schoolpool_day.png"
image Festival = DynamicImage("Graphics/ui/bg/festival_[gametime].png")
image Bathroom = "Graphics/ui/bg/bathroom.png"
image Recreation = "Graphics/ui/bg/NYI.png"
image Town = "Graphics/ui/bg/town.png"
image Arcade = "Graphics/ui/bg/arcade.png"
image Cafe = "Graphics/ui/bg/cafe.png"
image Woods = DynamicImage("Graphics/ui/bg/woods_[gametime].png")
image Restaurant = "Graphics/ui/bg/restaurant.png"
image Hill Road = "Graphics/ui/bg/NYI.png"
image Theater = "Graphics/ui/bg/NYI.png"
image Field = DynamicImage("Graphics/ui/bg/field_[gametime].png")
image Baseball Field = "Graphics/ui/bg/NYI.png"
image Store = "Graphics/ui/bg/NYI.png"
image Game Store = "Graphics/ui/bg/gamestore.png"
image Park = DynamicImage("Graphics/ui/bg/park_[gametime].png")
image Clock Tower = "Graphics/ui/bg/NYI.png"
image Diner = "Graphics/ui/bg/burgerrestaurant.png"
image Clothes Store = "Graphics/ui/bg/clothesstore.png"
image Pharmacy = DynamicImage("Graphics/ui/bg/pharmacy_[gametime].png")
image Supermarket = DynamicImage("Graphics/ui/bg/supermarket_[gametime].png")
image Art Gallery = "Graphics/ui/bg/NYI.png"
image Mountains = DynamicImage("Graphics/ui/bg/mountains_[gametime].png")
image Japanese Room = DynamicImage("Graphics/ui/bg/japaneseroom_[gametime].png")
image Club = "Graphics/ui/bg/NYI.png"
image Beach = DynamicImage("Graphics/ui/bg/beach_[gametime].png")

image Dorm Tomoko = "Graphics/ui/bg/NYI.png"

image Dorm AE = DynamicImage("Graphics/ui/bg/AEdorm_[gametime].png")
image Student Government = DynamicImage("Graphics/ui/bg/studentgovernment_[gametime].png")

image Dorm BBW = "Graphics/ui/bg/BBWDorm.png"
image Dorm BBW Flip = im.Flip("Graphics/ui/bg/BBWDorm.png", horizontal=True)

image Dorm BE = DynamicImage("Graphics/ui/bg/BEdorm_[gametime].png")
image Sushi Restaurant = "Graphics/ui/bg/sushirestaurant.png"

image Dorm FMG = DynamicImage("Graphics/ui/bg/FMGdorm_[gametime].png")

image Dorm GTS = DynamicImage("Graphics/ui/bg/GTSdorm_[gametime].png")
image Giant Dorm Exterior = "Graphics/ui/bg/NYI.png"
image Giant Dorm Interior = "Graphics/ui/bg/GTSdorm_quarry.png"
image GTS Courtyard = "Graphics/ui/bg/NYI.png"

image Dorm PRG = DynamicImage("Graphics/ui/bg/PRGdorm_[gametime].png")

#CG + Images
image splash = "Graphics/ui/bg/splashscreen.png"
image daymenubg = "Graphics/ui/bg/menubg-day.png"

image cg AE024 = "Graphics/ui/gallery/AE024.png"
image cg AE024b = "Graphics/ui/gallery/AE024b.png"
image cg AE024c = "Graphics/ui/gallery/AE024c.png"
image cg AE024d = "Graphics/ui/gallery/AE024d.png"
image cg AE024e = "Graphics/ui/gallery/AE024e.png"

image cg AE050_bj1 = "Graphics/ui/gallery/AE050_bj1.png"
image cg AE050_bj2 = "Graphics/ui/gallery/AE050_bj2.png"
image cg AE050_bj3 = "Graphics/ui/gallery/AE050_bj3.png"
image cg AE050_bj4 = "Graphics/ui/gallery/AE050_bj4.png"
image cg AE050_sit1 = "Graphics/ui/gallery/AE050_sit1.png"
image cg AE050_sit2 = "Graphics/ui/gallery/AE050_sit2.png"
image cg AE050_spank1 = "Graphics/ui/gallery/AE050_spank1.png"
image cg AE050_spank2 = "Graphics/ui/gallery/AE050_spank2.png"
image cg AE050_spank3 = "Graphics/ui/gallery/AE050_spank3.png"
image cg AE050_spank4 = "Graphics/ui/gallery/AE050_spank4.png"
image cg AE050_behind1 = "Graphics/ui/gallery/AE050_behind1.png"
image cg AE050_behind2 = "Graphics/ui/gallery/AE050_behind2.png"
image cg AE050_behind3 = "Graphics/ui/gallery/AE050_behind3.png"
image cg AE050_behind4 = "Graphics/ui/gallery/AE050_behind4.png"
image cg AE050_behind5 = "Graphics/ui/gallery/AE050_behind5.png"
image cg AE050_behind6 = "Graphics/ui/gallery/AE050_behind6.png"

image cg BBW000 = "Graphics/ui/gallery/BBW000.png"
image cg BBW009 = "Graphics/ui/gallery/BBW009.png"

image cg BE000 = "Graphics/ui/gallery/BE000.png"
image cg BE000b = "Graphics/ui/gallery/BE000b.png"
image cg BE001 = "Graphics/ui/gallery/BE001.png"
image cg BE010 = "Graphics/ui/gallery/BE010.png"
image cg BE031 = "Graphics/ui/gallery/BE031.png"
image cg BE031b = "Graphics/ui/gallery/BE031b.png"
image cg BE032 = "Graphics/ui/gallery/BE032.png"

image cg GTS025 = "Graphics/ui/gallery/GTS025.png"
image cg GTS035 = "Graphics/ui/gallery/GTS035.png"

image cg PRG025 = "Graphics/ui/gallery/PRG025.png"
image cg PRG038 = "Graphics/ui/gallery/PRG038.png"

#Character sprites
image RM neutral = "Graphics/minor/RM-neutral.png"
image RM angry = "Graphics/minor/RM-angry.png"
image RM concerned = "Graphics/minor/RM-concerned.png"
image RM concerned-2 = "Graphics/minor/RM-concerned-2.png"
image RM distrustful = "Graphics/minor/RM-distrustful.png"
image RM doubt = "Graphics/minor/RM-doubt.png"
image RM happy = "Graphics/minor/RM-happy.png"
image RM sad = "Graphics/minor/RM-sad.png"
image RM smug = "Graphics/minor/RM-smug.png"

image Yuki neutral = DynamicImage("Graphics/minor/yuki-[minorsize]-neutral.png")
image Yuki happy = DynamicImage("Graphics/minor/yuki-[minorsize]-happy.png")
image Yuki sad = DynamicImage("Graphics/minor/yuki-[minorsize]-sad.png")
image Yuki surprised = DynamicImage("Graphics/minor/yuki-[minorsize]-surprised.png")
image Yuki gossip = DynamicImage("Graphics/minor/yuki-[minorsize]-gossip.png")

image HR neutral = "Graphics/minor/HR-neutral.png"
image HR annoyed = "Graphics/minor/HR-neutral.png"

image Tomoko neutral = "Graphics/minor/tomoko-neutral.png"
image Tomoko happy = "Graphics/minor/tomoko-neutral.png"
image Tomoko surprised = "Graphics/minor/tomoko-neutral.png"
image Tomoko sad = "Graphics/minor/tomoko-neutral.png"

image AE neutral = DynamicImage("Graphics/AE/[globalsize]/neutral.png")
image AE neutral-annoyed = DynamicImage("Graphics/AE/[globalsize]/neutral-annoyed.png")
image AE neutral-eyebrow = DynamicImage("Graphics/AE/[globalsize]/neutral-eyebrow.png")
image AE neutral-noglasses = DynamicImage("Graphics/AE/[globalsize]/neutral-noglasses.png")
image AE neutral-smug = DynamicImage("Graphics/AE/[globalsize]/neutral-smug.png")
image AE happy = DynamicImage("Graphics/AE/[globalsize]/happy.png")
image AE smile = DynamicImage("Graphics/AE/[globalsize]/happy-2.png")
image AE pondering = DynamicImage("Graphics/AE/[globalsize]/pondering.png")
image AE sad = DynamicImage("Graphics/AE/[globalsize]/sad.png")
image AE sad-2 = DynamicImage("Graphics/AE/[globalsize]/sad-2.png")
image AE frown = DynamicImage("Graphics/AE/[globalsize]/sad.png")
image AE surprised = DynamicImage("Graphics/AE/[globalsize]/surprised.png")
image AE admire = DynamicImage("Graphics/AE/[globalsize]/admire.png")
image AE angry = DynamicImage("Graphics/AE/[globalsize]/angry.png")
image AE angry-2 = DynamicImage("Graphics/AE/[globalsize]/angry-2.png")
image AE angry-3 = DynamicImage("Graphics/AE/[globalsize]/angry-3.png")
image AE angry-4 = DynamicImage("Graphics/AE/[globalsize]/angry-4.png")
image AE aroused = DynamicImage("Graphics/AE/[globalsize]/aroused.png")
image AE embarrassed = DynamicImage("Graphics/AE/[globalsize]/embarrassed.png")
image AE aroused-2 = DynamicImage("Graphics/AE/[globalsize]/aroused-2.png")
image AE aroused-3 = DynamicImage("Graphics/AE/[globalsize]/aroused-3.png")
image AE aroused-4 = DynamicImage("Graphics/AE/[globalsize]/aroused-4.png")
image AE glasses = DynamicImage("Graphics/AE/[globalsize]/unique.png")
image AE glasses-2 = DynamicImage("Graphics/AE/[globalsize]/unique-2.png")
image AE glasses-3 = DynamicImage("Graphics/AE/[globalsize]/unique-3.png")
image AE ass = DynamicImage("Graphics/AE/[globalsize]/ass.png")
image AE ass-2 = DynamicImage("Graphics/AE/[globalsize]/ass.png")

image AE nude-neutral = DynamicImage("Graphics/AE/[globalsize]/nude-neutral.png")
image AE nude-neutral-annoyed = DynamicImage("Graphics/AE/[globalsize]/neutral-annoyed.png")
image AE nude-neutral-eyebrow = DynamicImage("Graphics/AE/[globalsize]/neutral-eyebrow.png")
image AE nude-neutral-noglasses = DynamicImage("Graphics/AE/[globalsize]/neutral-noglasses.png")
image AE nude-neutral-smug = DynamicImage("Graphics/AE/[globalsize]/neutral-smug.png")
image AE nude-happy = DynamicImage("Graphics/AE/[globalsize]/nude-happy.png")
image AE nude-smile = DynamicImage("Graphics/AE/[globalsize]/happy.png")
image AE nude-sad = DynamicImage("Graphics/AE/[globalsize]/sad.png")
image AE nude-sad-2 = DynamicImage("Graphics/AE/[globalsize]/sad-2.png")
image AE nude-surprised = DynamicImage("Graphics/AE/[globalsize]/surprised.png")
image AE nude-angry = DynamicImage("Graphics/AE/[globalsize]/angry.png")
image AE nude-angry-2 = DynamicImage("Graphics/AE/[globalsize]/angry-2.png")
image AE nude-angry-3 = DynamicImage("Graphics/AE/[globalsize]/angry-3.png")
image AE nude-aroused = DynamicImage("Graphics/AE/[globalsize]/aroused.png")
image AE nude-embarrassed = DynamicImage("Graphics/AE/[globalsize]/nude-embarrassed.png")
image AE nude-aroused-3 = DynamicImage("Graphics/AE/[globalsize]/aroused-3.png")
image AE nude-aroused-4 = DynamicImage("Graphics/AE/[globalsize]/aroused-4.png")
image AE nude-glasses = DynamicImage("Graphics/AE/[globalsize]/unique.png")
image AE nude-glasses-2 = DynamicImage("Graphics/AE/[globalsize]/unique-2.png")

image AE dress-neutral = DynamicImage("Graphics/AE/[globalsize]/dress-neutral.png")
image AE dress-neutral-2 = DynamicImage("Graphics/AE/[globalsize]/dress-neutral-2.png")
image AE dress-neutral-annoyed = DynamicImage("Graphics/AE/[globalsize]/dress-neutral-annoyed.png")
image AE dress-neutral-eyebrow = DynamicImage("Graphics/AE/[globalsize]/dress-neutral-eyebrow.png")
image AE dress-neutral-smug = DynamicImage("Graphics/AE/[globalsize]/dress-neutral-smug.png")
image AE dress-happy = DynamicImage("Graphics/AE/[globalsize]/dress-happy.png")
image AE dress-smile = DynamicImage("Graphics/AE/[globalsize]/dress-happy-2.png")
image AE dress-sad = DynamicImage("Graphics/AE/[globalsize]/dress-sad.png")
image AE dress-sad-2 = DynamicImage("Graphics/AE/[globalsize]/dress-sad-2.png")
image AE dress-surprised = DynamicImage("Graphics/AE/[globalsize]/dress-surprised.png")
image AE dress-angry = DynamicImage("Graphics/AE/[globalsize]/dress-angry.png")
image AE dress-angry-2 = DynamicImage("Graphics/AE/[globalsize]/dress-angry-2.png")
image AE dress-angry-3 = DynamicImage("Graphics/AE/[globalsize]/dress-angry-3.png")
image AE dress-aroused = DynamicImage("Graphics/AE/[globalsize]/dress-aroused.png")
image AE dress-aroused-2 = DynamicImage("Graphics/AE/[globalsize]/dress-aroused-2.png")
image AE dress-aroused-3 = DynamicImage("Graphics/AE/[globalsize]/dress-aroused-3.png")
image AE dress-aroused-4 = DynamicImage("Graphics/AE/[globalsize]/dress-aroused-4.png")
image AE dress-embarrassed = DynamicImage("Graphics/AE/[globalsize]/dress-embarrassed.png")
image AE dress-glasses = DynamicImage("Graphics/AE/[globalsize]/dress-unique.png")
image AE dress-glasses-2 = DynamicImage("Graphics/AE/[globalsize]/dress-unique-2.png")
image AE dress-glasses-3 = DynamicImage("Graphics/AE/[globalsize]/dress-unique-3.png")

image AE casual-neutral = DynamicImage("Graphics/AE/[globalsize]/dress-neutral.png")
image AE casual-neutral-2 = DynamicImage("Graphics/AE/[globalsize]/dress-neutral-2.png")
image AE casual-neutral-annoyed = DynamicImage("Graphics/AE/[globalsize]/dress-neutral-annoyed.png")
image AE casual-neutral-eyebrow = DynamicImage("Graphics/AE/[globalsize]/dress-neutral-eyebrow.png")
image AE casual-neutral-smug = DynamicImage("Graphics/AE/[globalsize]/dress-neutral-smug.png")
image AE casual-happy = DynamicImage("Graphics/AE/[globalsize]/dress-happy.png")
image AE casual-smile = DynamicImage("Graphics/AE/[globalsize]/dress-happy-2.png")
image AE casual-sad = DynamicImage("Graphics/AE/[globalsize]/dress-sad.png")
image AE casual-sad-2 = DynamicImage("Graphics/AE/[globalsize]/dress-sad-2.png")
image AE casual-surprised = DynamicImage("Graphics/AE/[globalsize]/dress-surprised.png")
image AE casual-angry = DynamicImage("Graphics/AE/[globalsize]/dress-angry.png")
image AE casual-angry-2 = DynamicImage("Graphics/AE/[globalsize]/dress-angry-2.png")
image AE casual-angry-3 = DynamicImage("Graphics/AE/[globalsize]/dress-angry-3.png")
image AE casual-aroused = DynamicImage("Graphics/AE/[globalsize]/dress-aroused.png")
image AE casual-aroused-2 = DynamicImage("Graphics/AE/[globalsize]/dress-aroused-2.png")
image AE casual-aroused-3 = DynamicImage("Graphics/AE/[globalsize]/dress-aroused-3.png")
image AE casual-aroused-4 = DynamicImage("Graphics/AE/[globalsize]/dress-aroused-4.png")
image AE casual-embarrassed = DynamicImage("Graphics/AE/[globalsize]/dress-embarrassed.png")
image AE casual-glasses = DynamicImage("Graphics/AE/[globalsize]/dress-unique.png")
image AE casual-glasses-2 = DynamicImage("Graphics/AE/[globalsize]/dress-unique-2.png")
image AE casual-glasses-3 = DynamicImage("Graphics/AE/[globalsize]/dress-unique-3.png")

image BBW neutral = DynamicImage("Graphics/BBW/[globalsize]/neutral.png")
image BBW neutral-2 = DynamicImage("Graphics/BBW/[globalsize]/neutral-2.png")
image BBW happy = DynamicImage("Graphics/BBW/[globalsize]/happy.png")
image BBW sad = DynamicImage("Graphics/BBW/[globalsize]/sad.png")
image BBW surprised = DynamicImage("Graphics/BBW/[globalsize]/surprised.png")
image BBW angry = DynamicImage("Graphics/BBW/[globalsize]/angry.png")
image BBW aroused = DynamicImage("Graphics/BBW/[globalsize]/aroused.png")
image BBW haughty = DynamicImage("Graphics/BBW/[globalsize]/unique.png")
image BBW stern = DynamicImage("Graphics/BBW/[globalsize]/stern.png")
image BBW doubt = DynamicImage("Graphics/BBW/[globalsize]/doubt.png")

image BBW sick = DynamicImage("Graphics/BBW/[globalsize]/sad.png")
image BBW sick-happy = DynamicImage("Graphics/BBW/[globalsize]/happy.png")
image BBW sick-angry = DynamicImage("Graphics/BBW/[globalsize]/angry.png")

image BBW swim-neutral = DynamicImage("Graphics/BBW/[globalsize]/neutral.png")
image BBW swim-neutral-2 = DynamicImage("Graphics/BBW/[globalsize]/neutral-2.png")
image BBW swim-happy = DynamicImage("Graphics/BBW/[globalsize]/happy.png")
image BBW swim-sad = DynamicImage("Graphics/BBW/[globalsize]/sad.png")
image BBW swim-surprised = DynamicImage("Graphics/BBW/[globalsize]/surprised.png")
image BBW swim-angry = DynamicImage("Graphics/BBW/[globalsize]/angry.png")
image BBW swim-aroused = DynamicImage("Graphics/BBW/[globalsize]/aroused.png")
image BBW swim-haughty = DynamicImage("Graphics/BBW/[globalsize]/unique.png")
image BBW swim-stern = DynamicImage("Graphics/BBW/[globalsize]/stern.png")
image BBW swim-doubt = DynamicImage("Graphics/BBW/[globalsize]/doubt.png")

image BBW casual-neutral = DynamicImage("Graphics/BBW/[globalsize]/neutral.png")
image BBW casual-neutral-2 = DynamicImage("Graphics/BBW/[globalsize]/neutral-2.png")
image BBW casual-happy = DynamicImage("Graphics/BBW/[globalsize]/happy.png")
image BBW casual-sad = DynamicImage("Graphics/BBW/[globalsize]/sad.png")
image BBW casual-surprised = DynamicImage("Graphics/BBW/[globalsize]/surprised.png")
image BBW casual-angry = DynamicImage("Graphics/BBW/[globalsize]/angry.png")
image BBW casual-aroused = DynamicImage("Graphics/BBW/[globalsize]/aroused.png")
image BBW casual-haughty = DynamicImage("Graphics/BBW/[globalsize]/unique.png")
image BBW casual-stern = DynamicImage("Graphics/BBW/[globalsize]/stern.png")
image BBW casual-doubt = DynamicImage("Graphics/BBW/[globalsize]/doubt.png")

image BE neutral = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/neutral.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/neutral.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE happy = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/happy.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/happy.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE sad = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/sad.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/sad.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE surprised = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/surprised.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/surprised.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE surprised-2 = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/surprised-2.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/surprised-2.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE angry = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/angry.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/angry.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE aroused = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/aroused.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/aroused.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE unique = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/unique.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/unique.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE confused = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/confused.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/confused.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE doubt = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/doubt.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/doubt.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE embarrassed = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/embarrassed.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/embarrassed.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE seductive = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/seductive.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/seductive.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )
image BE shrug = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/shrug.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/shrug.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3", "Graphics/BE/[globalsize]/fem_outfit.png",
        None, Null())
    )

image FMG neutral = DynamicImage("Graphics/FMG/[globalsize]/neutral.png")
image FMG happy = DynamicImage("Graphics/FMG/[globalsize]/happy.png")
image FMG sad = DynamicImage("Graphics/FMG/[globalsize]/sad.png")
image FMG surprised = DynamicImage("Graphics/FMG/[globalsize]/surprised.png")
image FMG surprised-2 = DynamicImage("Graphics/FMG/[globalsize]/surprised-2.png")
image FMG confused = DynamicImage("Graphics/FMG/[globalsize]/surprised.png")
image FMG angry = DynamicImage("Graphics/FMG/[globalsize]/angry.png")
image FMG angry-2 = DynamicImage("Graphics/FMG/[globalsize]/angry-2.png")
image FMG aroused = DynamicImage("Graphics/FMG/[globalsize]/aroused.png")
image FMG aroused-2 = DynamicImage("Graphics/FMG/[globalsize]/aroused-2.png")
image FMG flex = DynamicImage("Graphics/FMG/[globalsize]/flex.png")

image GTS neutral = DynamicImage("Graphics/GTS/[globalsize]/neutral.png")
image GTS neutral-2 = DynamicImage("Graphics/GTS/[globalsize]/neutral.png") #nyi
image GTS happy = DynamicImage("Graphics/GTS/[globalsize]/happy.png")
image GTS happy-2 = DynamicImage("Graphics/GTS/[globalsize]/happy-2.png")
image GTS sad = DynamicImage("Graphics/GTS/[globalsize]/sad.png")
image GTS sad-2 = DynamicImage("Graphics/GTS/[globalsize]/sad-2.png")
image GTS surprised = DynamicImage("Graphics/GTS/[globalsize]/surprised.png")
image GTS angry = DynamicImage("Graphics/GTS/[globalsize]/angry.png")
image GTS aroused = DynamicImage("Graphics/GTS/[globalsize]/aroused.png")
image GTS embarrassed = DynamicImage("Graphics/GTS/[globalsize]/embarrassed.png")
image GTS shy = DynamicImage("Graphics/GTS/[globalsize]/embarrassed.png")
image GTS blush = DynamicImage("Graphics/GTS/[globalsize]/embarrassed.png")
image GTS wink = DynamicImage("Graphics/GTS/[globalsize]/wink.png")
image GTS unique = DynamicImage("Graphics/GTS/[globalsize]/unique.png")
image GTS unique-2 = DynamicImage("Graphics/GTS/[globalsize]/unique-2.png")

image GTS_S neutral = DynamicImage("Graphics/GTS/[globalsize]_s/neutral.png")
image GTS_S neutral-2 = DynamicImage("Graphics/GTS/[globalsize]_s/neutral.png") #nyi
image GTS_S happy = DynamicImage("Graphics/GTS/[globalsize]_s/happy.png")
image GTS_S happy-2 = DynamicImage("Graphics/GTS/[globalsize]_s/happy.png") #nyi
image GTS_S sad = DynamicImage("Graphics/GTS/[globalsize]_s/sad.png")
image GTS_S sad-2 = DynamicImage("Graphics/GTS/[globalsize]_s/sad-2.png")
image GTS_S surprised = DynamicImage("Graphics/GTS/[globalsize]_s/surprised.png")
image GTS_S angry = DynamicImage("Graphics/GTS/[globalsize]_s/angry.png")
image GTS_S aroused = DynamicImage("Graphics/GTS/[globalsize]_s/aroused.png")
image GTS_S embarrassed = DynamicImage("Graphics/GTS/[globalsize]_s/embarrassed.png")
image GTS_S shy = DynamicImage("Graphics/GTS/[globalsize]_s/embarrassed.png")
image GTS_S blush = DynamicImage("Graphics/GTS/[globalsize]/embarrassed.png")
image GTS_S wink = DynamicImage("Graphics/GTS/[globalsize]_s/wink.png")
image GTS_S unique = DynamicImage("Graphics/GTS/[globalsize]_s/unique.png")
image GTS_S unique-2 = DynamicImage("Graphics/GTS/[globalsize]_s/unique-2.png")

image GTS casual-neutral = DynamicImage("Graphics/GTS/[globalsize]/casual-neutral.png")
image GTS casual-happy = DynamicImage("Graphics/GTS/[globalsize]/casual-happy.png")
image GTS casual-surprised = DynamicImage("Graphics/GTS/[globalsize]/casual-surprised.png")
image GTS casual-wink = DynamicImage("Graphics/GTS/[globalsize]/casual-wink.png")

image side GTS_S neutral = DynamicImage("Graphics/GTS/[globalsize]_s/side-neutral.png")
image side GTS_S neutral-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side-neutral.png") #nyi
image side GTS_S happy = DynamicImage("Graphics/GTS/[globalsize]_s/side-happy.png")
image side GTS_S happy-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side-happy.png") #nyi
image side GTS_S sad = DynamicImage("Graphics/GTS/[globalsize]_s/side-sad.png")
image side GTS_S sad-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side-sad-2.png")
image side GTS_S surprised = DynamicImage("Graphics/GTS/[globalsize]_s/side-surprised.png")
image side GTS_S angry = DynamicImage("Graphics/GTS/[globalsize]_s/side-angry.png")
image side GTS_S aroused = DynamicImage("Graphics/GTS/[globalsize]_s/side-aroused.png")
image side GTS_S embarrassed = DynamicImage("Graphics/GTS/[globalsize]_s/side-embarrassed.png")
image side GTS_S shy = DynamicImage("Graphics/GTS/[globalsize]_s/side-embarrassed.png")
image side GTS_S blush = DynamicImage("Graphics/GTS/[globalsize]_s/side-embarrassed.png")
image side GTS_S wink = DynamicImage("Graphics/GTS/[globalsize]_s/side-wink.png")
image side GTS_S unique = DynamicImage("Graphics/GTS/[globalsize]_s/side-unique.png")
image side GTS_S unique-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side-unique-2.png")

image PRG neutral = DynamicImage("Graphics/PRG/[prgsize]/neutral.png")
image PRG happy = DynamicImage("Graphics/PRG/[prgsize]/happy.png")
image PRG excited = DynamicImage("Graphics/PRG/[prgsize]/excited.png")
image PRG sad = DynamicImage("Graphics/PRG/[prgsize]/sad.png")
image PRG surprised = DynamicImage("Graphics/PRG/[prgsize]/surprised.png")
image PRG stressball = DynamicImage("Graphics/PRG/[prgsize]/stressball.png")
image PRG angry = DynamicImage("Graphics/PRG/[prgsize]/angry.png")
image PRG aroused = DynamicImage("Graphics/PRG/[prgsize]/aroused.png")
image PRG flattered = DynamicImage("Graphics/PRG/[prgsize]/flattered.png")
image PRG unique = DynamicImage("Graphics/PRG/[prgsize]/unique.png")
image PRG unique-happy = DynamicImage("Graphics/PRG/[prgsize]/unique-happy.png")
image PRG worried = DynamicImage("Graphics/PRG/[prgsize]/worried.png")
image PRG worried-handsbehind = DynamicImage("Graphics/PRG/[prgsize]/worried.png")
image PRG sad-2 = DynamicImage("Graphics/PRG/[prgsize]/sad-2.png")
image PRG lactate = DynamicImage("Graphics/PRG/[prgsize]/lactate.png")
image PRG admire = DynamicImage("Graphics/PRG/[prgsize]/admire.png")
image PRG admire-2 = DynamicImage("Graphics/PRG/[prgsize]/admire-2.png")
image PRG doubt = DynamicImage("Graphics/PRG/[prgsize]/doubt.png")
image PRG nervous = DynamicImage("Graphics/PRG/[prgsize]/nervous.png")
image PRG satisfied = DynamicImage("Graphics/PRG/[prgsize]/satisfied.png")

image PRG dress-neutral = DynamicImage("Graphics/PRG/[prgsize]/dress-neutral.png")
image PRG dress-happy = DynamicImage("Graphics/PRG/[prgsize]/dress-happy.png")
image PRG dress-excited = DynamicImage("Graphics/PRG/[prgsize]/dress-excited.png")
image PRG dress-sad = DynamicImage("Graphics/PRG/[prgsize]/dress-sad.png")
image PRG dress-surprised = DynamicImage("Graphics/PRG/[prgsize]/dress-surprised.png")
image PRG dress-aroused = DynamicImage("Graphics/PRG/[prgsize]/dress-aroused.png")
image PRG dress-flattered = DynamicImage("Graphics/PRG/[prgsize]/dress-flattered.png")
image PRG dress-unique = DynamicImage("Graphics/PRG/[prgsize]/dress-unique.png")
image PRG dress-unique-happy = DynamicImage("Graphics/PRG/[prgsize]/dress-unique-happy.png")
image PRG dress-worried = DynamicImage("Graphics/PRG/[prgsize]/dress-worried.png")
image PRG dress-worried-handsbehind = DynamicImage("Graphics/PRG/[prgsize]/dress-worried.png")
image PRG dress-sad = DynamicImage("Graphics/PRG/[prgsize]/dress-sad-2.png")
image PRG dress-sad-2 = DynamicImage("Graphics/PRG/[prgsize]/dress-sad-2.png")
image PRG dress-admire = DynamicImage("Graphics/PRG/[prgsize]/dress-happy.png")

image PRG nude-neutral = DynamicImage("Graphics/PRG/[prgsize]/nude-neutral.png")
image PRG nude-happy = DynamicImage("Graphics/PRG/[prgsize]/nude-happy.png")
image PRG nude-excited = DynamicImage("Graphics/PRG/[prgsize]/nude-excited.png")
image PRG nude-sad = DynamicImage("Graphics/PRG/[prgsize]/nude-sad.png")
image PRG nude-surprised = DynamicImage("Graphics/PRG/[prgsize]/nude-surprised.png")
image PRG nude-angry = DynamicImage("Graphics/PRG/[prgsize]/nude-angry.png")
image PRG nude-aroused = DynamicImage("Graphics/PRG/[prgsize]/nude-aroused.png")
image PRG nude-flattered = DynamicImage("Graphics/PRG/[prgsize]/nude-flattered.png")
image PRG nude-unique = DynamicImage("Graphics/PRG/[prgsize]/nude-unique.png")
image PRG nude-unique-happy = DynamicImage("Graphics/PRG/[prgsize]/nude-unique-happy.png")
image PRG nude-worried = DynamicImage("Graphics/PRG/[prgsize]/nude-worried.png")
image PRG nude-sad-2 = DynamicImage("Graphics/PRG/[prgsize]/nude-sad-2.png")
image PRG nude-lactate = DynamicImage("Graphics/PRG/[prgsize]/nude-lactate.png")
image PRG nude-lactate2 = DynamicImage("Graphics/PRG/[prgsize]/nude-lactate2.png")
image PRG nude-admire = DynamicImage("Graphics/PRG/[prgsize]/nude-admire.png")
image PRG nude-doubt = DynamicImage("Graphics/PRG/[prgsize]/nude-doubt.png")
image PRG nude-satisfied = DynamicImage("Graphics/PRG/[prgsize]/nude-satisfied.png")

image PRG cow-neutral = DynamicImage("Graphics/PRG/[prgsize]/cow-neutral.png")
image PRG cow-happy = DynamicImage("Graphics/PRG/[prgsize]/cow-happy.png")
image PRG cow-excited = DynamicImage("Graphics/PRG/[prgsize]/cow-excited.png")
image PRG cow-sad = DynamicImage("Graphics/PRG/[prgsize]/cow-sad.png")
image PRG cow-surprised = DynamicImage("Graphics/PRG/[prgsize]/cow-surprised.png")
image PRG cow-aroused = DynamicImage("Graphics/PRG/[prgsize]/cow-aroused.png")
image PRG cow-flattered = DynamicImage("Graphics/PRG/[prgsize]/cow-aroused.png")
image PRG cow-unique = DynamicImage("Graphics/PRG/[prgsize]/cow-unique.png")
image PRG cow-unique-happy = DynamicImage("Graphics/PRG/[prgsize]/cow-unique-happy.png")
image PRG cow-worried = DynamicImage("Graphics/PRG/[prgsize]/cow-worried.png")
image PRG cow-worried-handsbehind = DynamicImage("Graphics/PRG/[prgsize]/cow-worried.png")
image PRG cow-sad-2 = DynamicImage("Graphics/PRG/[prgsize]/cow-sad-2.png")
image PRG cow-lactate = DynamicImage("Graphics/PRG/[prgsize]/cow-lactate.png")
image PRG cow-admire = DynamicImage("Graphics/PRG/[prgsize]/cow-admire.png")

image PRG pj-neutral = DynamicImage("Graphics/PRG/[prgsize]/pajamas.png")
image PRG pj-happy = DynamicImage("Graphics/PRG/[prgsize]/pajamas.png")
image PRG pj-unique = DynamicImage("Graphics/PRG/[prgsize]/pajamas.png")

image side MC = "Graphics/side/mc.png"
image side BECell = ConditionSwitch("getVar('BEMode') == 'Feminine'", DynamicImage("Graphics/side/BE-fem-[globalsize].png"),
                                    "True", DynamicImage("Graphics/side/BE-[globalsize].png"))
image side BBWCell = DynamicImage("Graphics/side/BBW-[globalsize].png")
image side GTSCell = DynamicImage("Graphics/GTS/[globalsize]_s/side-neutral.png")
image side PRGCell = DynamicImage("Graphics/side/PRG-[prgsize].png")
image side TomoCell = "Graphics/side/tomoko.png"

image Ryoko neutral = "Graphics/minor/ryoko-neutral.png"
image Ryoko happy = "Graphics/minor/ryoko-happy.png"
image Ryoko annoyed = "Graphics/minor/ryoko-annoyed.png"
image Ryoko camera = "Graphics/minor/ryoko-camera.png"
image Ryoko surprised = "Graphics/minor/ryoko-surprised.png"
image Ryoko tongue = "Graphics/minor/ryoko-tongue.png"

image Minori neutral = "Graphics/minor/minori-neutral.png"
image Minori happy = "Graphics/minor/minori-happy.png"
image Minori embarrassed = "Graphics/minor/minori-neutral.png"
image Minori sad = "Graphics/minor/minori-neutral.png"

image Chibuki neutral = "Graphics/minor/chibuki-neutral.png"

image Sakura neutral = "Graphics/minor/sakura-neutral.png"

image Natsuko neutral = "Graphics/minor/natsuko-neutral.png"
image Natsuko annoyed = "Graphics/minor/natsuko-neutral.png"
image Natsuko angry = "Graphics/minor/natsuko-neutral.png"
image Natsuko disappointed = "Graphics/minor/natsuko-neutral.png"
image Natsuko smug = "Graphics/minor/natsuko-neutral.png"
image Natsuko flex = "Graphics/minor/natsuko-neutral.png"
image Natsuko happy = "Graphics/minor/natsuko-neutral.png"

image Tako neutral = "Graphics/minor/tako-neutral.png"
image Tako angry = "Graphics/minor/tako-angry.png"
image Tako excited = "Graphics/minor/tako-excited.png"
image Tako happy = "Graphics/minor/tako-happy.png"
image Tako unique = "Graphics/minor/tako-unique.png"
image Tako sad = "Graphics/minor/tako-sad.png"
image Tako surprised = "Graphics/minor/tako-surprised.png"

image Tako nohat-neutral = "Graphics/minor/tako-nohat-neutral.png"
image Tako nohat-angry = "Graphics/minor/tako-nohat-angry.png"
image Tako nohat-excited = "Graphics/minor/tako-nohat-excited.png"
image Tako nohat-happy = "Graphics/minor/tako-nohat-happy.png"
image Tako nohat-unique = "Graphics/minor/tako-nohat-unique.png"
image Tako nohat-sad = "Graphics/minor/tako-nohat-sad.png"
image Tako nohat-surprised = "Graphics/minor/tako-nohat-surprised.png"

image dummy = "Graphics/ui/dummy.png"

#Audio
define audio.Daymenu = "Audio/BGM/menu_daymenu.ogg" #PH
define audio.AE = "Audio/BGM/scene_AE.ogg"
define audio.AEAlt = "Audio/BGM/scene_AEalt.ogg"
define audio.BE = "Audio/BGM/scene_BE.mp3"
define audio.BBW = "Audio/BGM/scene_BBW.ogg" #Aristocratic Opulence
define audio.FMG = "Audio/BGM/scene_FMG.ogg" #Pump It
define audio.GTS = "Audio/BGM/scene_GTS.ogg" #Hidden Meadow
define audio.RM = "Audio/BGM/scene_RM.ogg"
define audio.MC = "Audio/BGM/scene_MC.ogg" #Our Protagonist
define audio.PRG = "Audio/BGM/scene_PRG.ogg" #Quiet Wandering
define audio.PRGDramatic = "Audio/BGM/scene_PRGdrama.ogg"
define audio.PRGChallenge = "Audio/BGM/scene_PRGchallenge.ogg" #The Challenge
define audio.Bittersweet = "Audio/BGM/scene_bittersweet.mp3" #PH
define audio.Busy = "Audio/BGM/scene_busy.mp3" #PH
define audio.Festival = "Audio/BGM/scene_festival.mp3" #PH
define audio.HigherEdu = "Audio/BGM/scene_higheredu.ogg" #Higher Education
define audio.Rain = "Audio/BGM/scene_rain.mp3" #PH
define audio.Romance = "Audio/BGM/scene_tbi.ogg" #NEED
define audio.Peaceful = "Audio/BGM/scene_peaceful.mp3" #PH
define audio.Schoolday = "Audio/BGM/scene_schoolday.mp3" #PH
define audio.Secret = "Audio/BGM/scene_secret.ogg" #A Secret Place
define audio.Steamy = "Audio/BGM/scene_tbi.ogg" #NEED
define audio.Hallway = "Audio/BGM/scene_Hallway.ogg"
define audio.Tension = "Audio/BGM/scene_tbi.ogg" #NEED

define audio.EventStart = "Audio/SFX/sfx_eventstart.ogg"
define audio.AlarmClock = "Audio/SFX/sfx_alarmclock.ogg"
define audio.Bird = "Audio/SFX/sfx_tbi.ogg" #NEED (current one too long)
define audio.Cheer = "Audio/SFX/sfx_cheer.mp3"
define audio.ClockTower = "Audio/SFX/sfx_clocktower.mp3"
define audio.Crash = "Audio/SFX/sfx_thud.wav" #NEED UPDATE
define audio.DoorOpen = "Audio/SFX/sfx_tbi.ogg"
define audio.Boing = "Audio/SFX/sfx_boing.ogg"
define audio.Knock = "Audio/SFX/sfx_knock.mp3"
define audio.Stomach = "Audio/SFX/sfx_tbi.ogg"
define audio.Thud = "Audio/SFX/sfx_thud.wav"
define audio.Thunder = "Audio/SFX/sfx_thunder.wav"
define audio.Victory = "Audio/SFX/sfx_victory.ogg"
define audio.Whistle = "Audio/SFX/sfx_whistle.mp3"
define audio.Bell = "Audio/SFX/sfx_bell.mp3"
define audio.ReleaseArrow = "Audio/SFX/sfw_releasearrow.wav"

init 1 python:
    eventlibrary['global005'] = {"name": "And the Results Are In", "girls": [], "type": EventTypeEnum.OPTIONALCORE,        "location": "auditorium",    "priority": PrioEnum.ALL, "next": "", "obsflags": [],           "conditions": [[ConditionEnum.TIMEFLAG, "testday"]]}
    eventlibrary['RM001'] = {"name": "Getting to Know Your Roommate", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,  "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": []}
    eventlibrary['RM002'] = {"name": "You and Yuki", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                   "location": "hallway",       "priority": PrioEnum.NONE, "next": "", "obsflags": ["size5"],          "conditions": [[ConditionEnum.EVENT, "RM001"]]}

    #Causes minor character scenes to be disabled if thime is between the first and second time in a tuple
    #(In other words, if XOR any two scenes in a tuple, then disable optional events with minor characters)
    minorDisableTimes = [("testday2", "aftertest"), ("size2", "aftersize2")]

init 2 python:
    #Core
    eventlibrary['AE001'] = {"name": "Hush", "girls": ["AE"], "type": EventTypeEnum.CORE,                                       "location": "library",          "priority": PrioEnum.NONE, "sp": 0,     "next": "AE002", "obsflags": ["size2"],         "conditions": []}
    eventlibrary['AE002'] = {"name": "A Hard Read", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "office",           "priority": PrioEnum.NONE, "sp": 0,     "next": "AE003", "obsflags": ["size2"],         "conditions": []}
    eventlibrary['AE003'] = {"name": "The Lord High Executioner", "girls": ["AE"], "type": EventTypeEnum.CORE,                  "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 0,     "next": "AE004", "obsflags": [],                "conditions": []}
    eventlibrary['AE004'] = {"name": "A Statistically Probable Meeting", "girls": ["AE"], "type": EventTypeEnum.CORE,           "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 0,     "next": "AE006", "obsflags": [],                "conditions": []}
    eventlibrary['AE006'] = {"name": "Opportunity and Networking", "girls": ["AE"], "type": EventTypeEnum.CORE,                 "location": "office",           "priority": PrioEnum.NONE, "sp": 1,     "next": "AE007", "obsflags": [],                "conditions": []}
    eventlibrary['AE007'] = {"name": "The Value of a Minute or Two", "girls": ["AE"], "type": EventTypeEnum.CORE,               "location": "office",           "priority": PrioEnum.NONE, "sp": 1,     "next": "AE008", "obsflags": [],                "conditions": []}
    eventlibrary['AE008'] = {"name": "Striking Up a One Sided Conversation", "girls": ["AE"], "type": EventTypeEnum.CORE,       "location": "office",           "priority": PrioEnum.NONE, "sp": 1,     "next": "AE009", "obsflags": [],                "conditions": []}
    eventlibrary['AE009'] = {"name": "On Your Mind", "girls": ["AE"], "type": EventTypeEnum.CORE,                               "location": "office",           "priority": PrioEnum.NONE, "sp": 1,     "next": "AE011",    "obsflags": [],                "conditions": []}
    eventlibrary['AE011'] = {"name": "Raising the Question", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE012",    "obsflags": [],                "conditions": []}
    eventlibrary['AE012'] = {"name": "Inquiry and Response", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE013", "obsflags": [],                "conditions": []}
    eventlibrary['AE013'] = {"name": "Stickers on Caskets", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE014", "obsflags": [],                "conditions": []}
    eventlibrary['AE014'] = {"name": "The Daily Grind", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "next": "AE015", "obsflags": [],                "conditions": []}
    eventlibrary['AE015'] = {"name": "Hostage Situation", "girls": ["AE"], "type": EventTypeEnum.CORE,                          "location": "office",           "priority": PrioEnum.NONE, "sp": 3,     "next": "AE016", "obsflags": [],                "conditions": []}
    eventlibrary['AE016'] = {"name": "A Little List", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "library",          "priority": PrioEnum.NONE, "sp": 3,     "next": "AE017", "obsflags": [],                "conditions": []}
    eventlibrary['AE017'] = {"name": "Chopsticks", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "AE018", "obsflags": [],                "conditions": []}
    eventlibrary['AE018'] = {"name": "Miseri Mei", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "AE019", "obsflags": [],                "conditions": []}
    eventlibrary['AE019'] = {"name": "Rondo Alla Turca", "girls": ["AE"], "type": EventTypeEnum.CORE,                           "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 3,     "next": "AE020", "obsflags": [],                "conditions": []}
    eventlibrary['AE020'] = {"name": "Pascha Nostrum", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "classroom",        "priority": PrioEnum.NONE, "sp": 4,     "next": "AE021", "obsflags": [],                "conditions": []}
    eventlibrary['AE021'] = {"name": "Prelude for Choir", "girls": ["AE", "BBW", "PRG"], "type": EventTypeEnum.CORE,            "location": "classroom",        "priority": PrioEnum.NONE, "sp": 4,     "next": "AE022", "obsflags": [],                "conditions": []}
    eventlibrary['AE022'] = {"name": "Casta Diva", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "hallway",          "priority": PrioEnum.NONE, "sp": 4,     "next": "AE023", "obsflags": [],                "conditions": []}
    eventlibrary['AE023'] = {"name": "Sarabande", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "hallway",          "priority": PrioEnum.NONE, "sp": 4,     "next": "AE024", "obsflags": [],                "conditions": []}
    eventlibrary['AE024'] = {"name": "Carmen", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "roof",             "priority": PrioEnum.NONE, "sp": 4,     "next": "AE025", "obsflags": [],                "conditions": []}
    eventlibrary['AE025'] = {"name": "Seasons", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 5,     "next": "AE026", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE026'] = {"name": "The Most Wondrous Dream", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 5,     "next": "AE027", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE027'] = {"name": "Through Thicc or Thin", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "AE028", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE028'] = {"name": "Bolero", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "roof",             "priority": PrioEnum.NONE, "sp": 5,     "next": "AE029", "obsflags": [],                "conditions": []} #TODO: Not sure if schoolplanter
    eventlibrary['AE029'] = {"name": "Moon in June", "girls": ["AE"], "type": EventTypeEnum.CORE,                               "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 5,     "next": "AE030", "obsflags": [],                "conditions": []}
    eventlibrary['AE030'] = {"name": "Exposure", "girls": ["AE", "BE"], "type": EventTypeEnum.CORE,                             "location": "classroom",        "priority": PrioEnum.NONE, "sp": 6,     "next": "AE031", "obsflags": [],                "conditions": []}
    eventlibrary['AE031'] = {"name": "The Keys to her Heart", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 6,     "next": "AE032", "obsflags": [],                "conditions": []}
    eventlibrary['AE032'] = {"name": "Standardized High Standards", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 6,     "next": "AE033", "obsflags": [],                "conditions": []}
    eventlibrary['AE033'] = {"name": "Your Secret Told on You", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "hallway",          "priority": PrioEnum.NONE, "sp": 6,     "next": "AE034", "obsflags": [],                "conditions": []}
    eventlibrary['AE034'] = {"name": "O Mio Babbino Caro", "girls": ["AE"], "type": EventTypeEnum.CORE,                         "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 6,     "next": "AE035", "obsflags": [],                "conditions": []}
    eventlibrary['AE035'] = {"name": "The Black Box", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 7,     "next": "AE036", "obsflags": [],                "conditions": []}
    eventlibrary['AE036'] = {"name": "Out There", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "schoolfront",      "priority": PrioEnum.NONE, "sp": 7,     "next": "AE037", "obsflags": [],                "conditions": []}
    eventlibrary['AE037'] = {"name": "A Walk Through Town", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "town",             "priority": PrioEnum.NONE, "sp": 7,     "next": "AE038", "obsflags": [],                "conditions": []}
    eventlibrary['AE038'] = {"name": "A Simple Meal", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "town",             "priority": PrioEnum.NONE, "sp": 7,     "next": "AE039", "obsflags": [],                "conditions": []}
    eventlibrary['AE039'] = {"name": "Dawn of Warblade", "girls": ["AE"], "type": EventTypeEnum.CORE,                           "location": "town",             "priority": PrioEnum.NONE, "sp": 7,     "next": "AE040", "obsflags": [],                "conditions": []}
    eventlibrary['AE040'] = {"name": "A Game of Oversized Thrones", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE041", "obsflags": [],                "conditions": []}
    eventlibrary['AE041'] = {"name": "Ambush", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE042", "obsflags": [],                "conditions": []}
    eventlibrary['AE042'] = {"name": "Chaos Reigns", "girls": ["AE"], "type": EventTypeEnum.CORE,                               "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE043", "obsflags": [],                "conditions": []}
    eventlibrary['AE043'] = {"name": "Rainy Skies, Hot Coffee", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE044", "obsflags": [],                "conditions": []}
    eventlibrary['AE044'] = {"name": "From Which The Angel Falls", "girls": ["AE"], "type": EventTypeEnum.CORE,                 "location": "town",             "priority": PrioEnum.NONE, "sp": 8,     "next": "AE045", "obsflags": [],                "conditions": []}
    eventlibrary['AE045'] = {"name": "Let My Prayers Arise", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "clocktower",       "priority": PrioEnum.GIRL, "sp": 9,     "next": "AE046", "obsflags": [],                "conditions": []}
    eventlibrary['AE046'] = {"name": "Perfection in Normality", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "dormAE",           "priority": PrioEnum.NONE, "sp": 9,     "next": "AE047", "obsflags": [],                "conditions": []}
    eventlibrary['AE047'] = {"name": "So Many", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "dormAE",           "priority": PrioEnum.NONE, "sp": 9,     "next": "AE048", "obsflags": [],                "conditions": []}
    eventlibrary['AE048'] = {"name": "Taking it Seriously", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 9,     "next": "AE049", "obsflags": [],                "conditions": []}
    eventlibrary['AE049'] = {"name": "The Wise Thief", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 9,     "next": "AE050", "obsflags": [],                "conditions": []}
    eventlibrary['AE050'] = {"name": "Nights in White Satin", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "dormexterior",     "priority": PrioEnum.ALL, "sp": 10,     "next": "AE051", "obsflags": [],                "conditions": []}
    eventlibrary['AE051'] = {"name": "Never Reaching the End", "girls": ["AE"], "type": EventTypeEnum.CORE,                     "location": "dormexterior",     "priority": PrioEnum.ALL, "sp": 10,     "next": "AE052", "obsflags": [],                "conditions": []}
    eventlibrary['AE052'] = {"name": "Tristesse", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "library",          "priority": PrioEnum.NONE, "sp": 10,    "next": "AE053", "obsflags": [],                "conditions": []}
    eventlibrary['AE053'] = {"name": "Dressed to Impress", "girls": ["AE", "BBW"], "type": EventTypeEnum.CORE,                  "location": "town",             "priority": PrioEnum.NONE, "sp": 10,    "next": "AE054", "obsflags": [],                "conditions": []}
    eventlibrary['AE054'] = {"name": "Molto Allegro", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 10,    "next": "AE055", "obsflags": [],                "conditions": []}
    eventlibrary['AE055'] = {"name": "Ruhe Sanft", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "hillroad",         "priority": PrioEnum.NONE, "sp": 11,    "next": "AE056", "obsflags": [],                "conditions": []}
    eventlibrary['AE056'] = {"name": "Hymn of the Cherubim", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "classroom",        "priority": PrioEnum.NONE, "sp": 11,    "next": "AE057", "obsflags": [],                "conditions": []}
    eventlibrary['AE057'] = {"name": "Norwegian Dance", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 11,    "next": "AE058", "obsflags": [],                "conditions": []}
    eventlibrary['AE058'] = {"name": "Waltz of the Flowers", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "library",          "priority": PrioEnum.NONE, "sp": 11,    "next": "AE059", "obsflags": [],                "conditions": []}
    eventlibrary['AE059'] = {"name": "Eye to Eye, Face to Face, Heart to Heart", "girls": ["AE"], "type": EventTypeEnum.CORE,   "location": "hallway",          "priority": PrioEnum.NONE, "sp": 11,    "next": "AE060", "obsflags": [],                "conditions": []}
    eventlibrary['AE060'] = {"name": "Csárdás", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "library",          "priority": PrioEnum.NONE, "sp": 12,    "next": "AE061", "obsflags": [],                "conditions": []}
    eventlibrary['AE061'] = {"name": "Starless", "girls": ["AE"], "type": EventTypeEnum.CORE,                                   "location": "library",          "priority": PrioEnum.NONE, "sp": 12,    "next": "AE062", "obsflags": [],                "conditions": []}
    eventlibrary['AE062'] = {"name": "Gymnopedies", "girls": ["AE", "BE"], "type": EventTypeEnum.CORE,                          "location": "town",             "priority": PrioEnum.NONE, "sp": 12,    "next": "AE063", "obsflags": [],                "conditions": []}
    eventlibrary['AE063'] = {"name": "Ballade No. 1 in G Minor", "girls": ["AE"], "type": EventTypeEnum.CORE,                   "location": "classroom",        "priority": PrioEnum.NONE, "sp": 12,    "next": "AE064", "obsflags": [],                "conditions": []}
    eventlibrary['AE064'] = {"name": "Nocturne no. 2", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "hallway",          "priority": PrioEnum.NONE, "sp": 12,    "next": "AE065", "obsflags": [],                "conditions": []}
    eventlibrary['AE065'] = {"name": "Prelude in C Minor", "girls": ["AE"], "type": EventTypeEnum.CORE,                         "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 13,    "next": "AE066", "obsflags": [],                "conditions": []}
    eventlibrary['AE066'] = {"name": "Dies Irae", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "hallway",          "priority": PrioEnum.NONE, "sp": 13,    "next": "AE067", "obsflags": [],                "conditions": []}
    eventlibrary['AE067'] = {"name": "Troparion", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "roof",             "priority": PrioEnum.NONE, "sp": 13,    "next": "AE068", "obsflags": [],                "conditions": []}
    eventlibrary['AE068'] = {"name": "Sonata", "girls": ["AE"], "type": EventTypeEnum.CORE,                                     "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 13,    "next": "AE069", "obsflags": [],                "conditions": []}
    eventlibrary['AE069'] = {"name": "The Creed", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "classroom",        "priority": PrioEnum.NONE, "sp": 13,    "next": "AE070", "obsflags": [],                "conditions": []}
    eventlibrary['AE070'] = {"name": "Lento Placido", "girls": ["AE"], "type": EventTypeEnum.CORE,                              "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 14,    "next": "AE071", "obsflags": [],                "conditions": []}
    eventlibrary['AE071'] = {"name": "Shiori End", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "dormexterior",     "priority": PrioEnum.NONE,              "next": "", "obsflags": [],                     "conditions": []}

    eventlibrary['AE007b'] = {"name": "Peer Gynt", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "hallway",          "priority": PrioEnum.NONE, "sp": 1,    "next": "AE008b", "obsflags": [],                "conditions": []}
    eventlibrary['AE008b'] = {"name": "Made of Stone", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 1,    "next": "AE009b", "obsflags": [],                "conditions": []}
    eventlibrary['AE009b'] = {"name": "Jardins sous la Pluie", "girls": ["AE"], "type": EventTypeEnum.CORE,                     "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 1,    "next": "AE011b", "obsflags": [],                "conditions": []}
    eventlibrary['AE011b'] = {"name": "Shiori End", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,    "next": "", "obsflags": [],                     "conditions": []}

    #Optional
    eventlibrary['AE005'] = {"name": "Confirmation", "girls": ["AE"], "type": EventTypeEnum.OPTIONALCORE,                       "location": "hallway",          "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],                      "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
     #fixme: it's an office scene, make sure that's handled in split
    eventlibrary['AE010'] = {"name": "Blue Danube", "girls": ["AE"], "type": EventTypeEnum.OPTIONALCORE,                        "location": "office",           "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": ["aftersize2"],                     "conditions": [[ConditionEnum.TIMEFLAG, "size2"], [ConditionEnum.FLAG, "AE006_helpinginoffice"]]}

    #Core
    eventlibrary['BBW001'] = {"name": "Human Resources", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                                  "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 0,     "next": "BBW002", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW002'] = {"name": "Concerning a Missing Right Arm", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                   "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 0,     "next": "BBW003", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW003'] = {"name": "Necessity is the Mother of Employment", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                     "location": "cookingclassroom", "priority": PrioEnum.NONE, "sp": 0,     "next": "BBW006", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW006'] = {"name": "A Proud Patron of the Arts", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                       "location": "hallway",          "priority": PrioEnum.NONE, "sp": 1,     "next": "BBW007", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW007'] = {"name": "Her Other Fluent Language", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 1,     "next": "BBW008", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW008'] = {"name": "How to Train Your Diva", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                                    "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 1,     "next": "BBW012", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW008A'] = {"name": "The Fat Lady Won't Sing", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                         "location": "cafeteria",        "priority": PrioEnum.GIRL, "sp": 1,     "next": "BBW012", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW012'] = {"name": "Business Business Business Numbers", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                               "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 1,     "next": "BBW015", "obsflags": ["BBWnowork"],                    "conditions": []}
    eventlibrary['BBW015'] = {"name": "This is the Stealth Section", "girls": ["BBW", "AE"], "type": EventTypeEnum.CORE,                                                "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,     "next": "BBW016", "obsflags": ["BBWnowork"],                    "conditions": []}
    eventlibrary['BBW016'] = {"name": "Game Time Interrupted", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                            "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,     "next": "BBW017", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW017'] = {"name": "What's She Got That I Haven't Got More Of?", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                       "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 2,     "next": "BBW020", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW020'] = {"name": "I Like Big...?", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                                            "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "BBW021", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW021'] = {"name": "The Lady in the Pool", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                             "location": "pool",             "priority": PrioEnum.NONE, "sp": 3,     "next": "BBW022", "obsflags": ["BBWnowork"],                    "conditions": []}
    eventlibrary['BBW022'] = {"name": "Helpful Muscle", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                                            "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 3,     "next": "BBW023", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW023'] = {"name": "It Can Be Found Anywhere", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                         "location": "classroom",        "priority": PrioEnum.NONE, "sp": 3,     "next": "BBW025", "obsflags": ["BBWnowork"],                    "conditions": []} #\/ disabled due to affection not being very grindable right now
    eventlibrary['BBW025'] = {"name": "Interoffice Romance", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                              "location": "hallway",          "priority": PrioEnum.NONE, "sp": 4,     "next": "BBW026", "obsflags": [],                               "conditions": []} #"conditions": [[ConditionEnum.AFFECTION, "BBW", ConditionEqualityEnum.GREATERTHANEQUALS, 6]]}
    eventlibrary['BBW026'] = {"name": "The Trial of Smarts", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                              "location": "classroom",        "priority": PrioEnum.NONE, "sp": 4,     "next": "BBW028", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW028'] = {"name": "Who Are the Ad Wizards...", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                        "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 4,     "next": "BBW030", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW030'] = {"name": "Sick Day", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                                                  "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 5,     "next": "BBW031", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW031'] = {"name": "No 'Big Day' Puns, Please", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                        "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "BBW032", "obsflags": [],                               "conditions": [[ConditionEnum.FLAG, "BBW_dating"]]}
    eventlibrary['BBW032'] = {"name": "Art Appreciation", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                                 "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "BBW034", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW034'] = {"name": "Smells Like Team Spirit", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                          "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "BBW035", "obsflags": ["BBWnowork", "BBWclubfail"],     "conditions": []}
    eventlibrary['BBW035'] = {"name": "Styling and Profiling", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                            "location": "town",             "priority": PrioEnum.NONE, "sp": 5,     "next": "BBW036", "obsflags": ["BBWnowork", "BBWclubfail"],     "conditions": []}
    eventlibrary['BBW036'] = {"name": "It's Showtime", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                                    "location": "auditorium",       "priority": PrioEnum.NONE, "sp": 6,     "next": "BBW037", "obsflags": ["BBWnowork", "BBWclubfail"],     "conditions": []}
    eventlibrary['BBW037'] = {"name": "A Meeting with the Boss", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                                                 "location": "auditorium",       "priority": PrioEnum.NONE, "sp": 6,     "next": "BBW039", "obsflags": ["BBWnowork", "BBWclubfail"],     "conditions": []}
    eventlibrary['BBW039'] = {"name": "A Pleasant Day in Pleasant Town", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                                                 "location": "classroom",        "priority": PrioEnum.NONE, "sp": 6,     "next": "BBW040", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW040'] = {"name": "Helping Hands", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                                             "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "BBW041", "obsflags": [],                               "conditions": []} # >=20 affection
    eventlibrary['BBW041'] = {"name": "Beck and Call", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                                    "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "BBW042", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW042'] = {"name": "The Bigger Picture", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                               "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,     "next": "BBW045", "obsflags": ["BBWnowork"],                    "conditions": []}
    eventlibrary['BBW045'] = {"name": "No Need to Wine", "girls": ["BBW", "PRG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 8,     "next": "BBW046", "obsflags": [],                               "conditions": []}
    eventlibrary['BBW046'] = {"name": "Alice end", "girls": ["BBW"], "type": EventTypeEnum.CORE,                                                                        "location": "library",          "priority": PrioEnum.NONE, "sp": 8,     "next": "", "obsflags": [],                                     "conditions": []}

    #Optional
    eventlibrary['BBW004'] = {"name": "As Long as the Job Gets Done, Right?", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONAL,                                  "location": "classroom",        "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": []}
    eventlibrary['BBW009'] = {"name": "Between a Soft and a Hard Place", "girls": ["BBW", "PRG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                "location": "pool",             "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": []}
    eventlibrary['BBW011'] = {"name": "True Romance", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": []}
    eventlibrary['BBW013'] = {"name": "The Elephant In The Room", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                     "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": []}
    eventlibrary['BBW014'] = {"name": "Silence Can Be Heavy", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                         "location": "gym",              "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": []}
    eventlibrary['BBW018'] = {"name": "All the Tycoons", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONAL,                                                       "location": "cafeteria",        "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": [[ConditionEnum.FLAG, "BBW016_testpass"]]}
    eventlibrary['BBW019'] = {"name": "Time Management", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                              "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": []}
    eventlibrary['BBW024'] = {"name": "Mental Defragmentation", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                       "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": []}
    eventlibrary['BBW025A'] = {"name": "Second Chance", "girls": ["BBW"], "type": EventTypeEnum.OPTIONALCORE,                                                           "location": "cafeteria",        "priority": PrioEnum.GIRL,              "obsflags": [],                              "conditions": [[ConditionEnum.AFFECTION, "BBW", ConditionEqualityEnum.GREATERTHANEQUALS, 10], [ConditionEnum.FLAG, "BBW025A_unlock"]]}
    eventlibrary['BBW027'] = {"name": "Have it All?", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                                 "location": "cafeteria",        "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": [[ConditionEnum.FLAG, "BBW_working"]]}
    eventlibrary['BBW029A'] = {"name": "Do the Right Thing", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "cafeteria",        "priority": PrioEnum.GIRL,              "obsflags": [],                              "conditions": [[ConditionEnum.ROUTELOCK, "PRG"]]}
    eventlibrary['BBW029B'] = {"name": "Things Happen", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                               "location": "cafeteria",        "priority": PrioEnum.GIRL,              "obsflags": [],                              "conditions": [[ConditionEnum.EVENT, "PRG026b"]]}
    eventlibrary['BBW029C'] = {"name": "You Did a Bad, Bad Thing", "girls": ["BBW"], "type": EventTypeEnum.OPTIONAL,                                                    "location": "cafeteria",        "priority": PrioEnum.ALL,               "obsflags": [],                              "conditions": [[ConditionEnum.FLAG, "PRG026_c1_2"]]}
    eventlibrary['BBW033'] = {"name": "Wardrobe Dysfunction", "girls": ["BBW", "FMG"], "type": EventTypeEnum.OPTIONAL,                                                  "location": "classroom",        "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": [[ConditionEnum.OR, [ConditionEnum.AFFECTION, "BBW", ConditionEqualityEnum.GREATERTHAN, 10], [ConditionEnum.AFFECTION, "FMG", ConditionEqualityEnum.GREATERTHAN, 10]]]}
    eventlibrary['BBW038'] = {"name": "Deal With It", "girls": ["BBW", "BE"], "type": EventTypeEnum.OPTIONAL,                                                           "location": "classroom",        "priority": PrioEnum.NONE,              "obsflags": [],                              "conditions": [[ConditionEnum.TIMEFLAG, "size3"]]}

    eventlibrary['BBW005'] = {"name": "What to Expect When You're Growing", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONALCORE,                                "location": "cafeteria",        "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],                   "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['BBW005A'] = {"name": "You Ate, You Drank, and You Were Merry, For Today You Diet", "girls": ["BBW", "PRG"], "type": EventTypeEnum.OPTIONALCORE,       "location": "cafeteria",        "priority": PrioEnum.GIRL,              "obsflags": [],                              "conditions": [[ConditionEnum.FLAG, "BBW005_ondiet"]]}
    eventlibrary['BBW005B'] = {"name": "Pump You Up, Not Plump You Up", "girls": ["BBW", "PRG", "FMG"], "type": EventTypeEnum.OPTIONALCORE,                             "location": "gym",              "priority": PrioEnum.GIRL,              "obsflags": [],                              "conditions": [[ConditionEnum.FLAG, "BBW005_workout"]]}
    eventlibrary['BBW010'] = {"name": "ABC: Always Be Clothing", "girls": ["BBW"], "type": EventTypeEnum.OPTIONALCORE,                                                  "location": "cafeteria",        "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": [],                              "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}

    #Core
    eventlibrary['BE001'] = {"name": "Rooftop Reunion", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "roof",             "priority": PrioEnum.NONE, "sp": 0,     "next": "BE003", "obsflags": ["testday"],         "conditions": []}
    eventlibrary['BE002'] = {"name": "Campus Collision", "girls": ["BE"], "type": EventTypeEnum.CORE,                                   "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 0,     "next": "BE003", "obsflags": ["testday"],         "conditions": []}
    eventlibrary['BE003'] = {"name": "Cool Drinks with Honoka", "girls": ["BE"], "type": EventTypeEnum.CORE,                            "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 0,     "next": "BE004", "obsflags": [],                  "conditions": []}
    eventlibrary['BE004'] = {"name": "Chatting at Soccer Practice", "girls": ["BE"], "type": EventTypeEnum.CORE,                        "location": "track",            "priority": PrioEnum.NONE, "sp": 0,     "next": "BE007", "obsflags": [],                  "conditions": []}
    #eventlibrary['BE006'] = {"name": "BE006", "girls": ["BE"], "location": "classroom", "conditions": [], "priority": 0}
    eventlibrary['BE007'] = {"name": "Lunchtime with Honoka", "girls": ["BE"], "type": EventTypeEnum.CORE,                              "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 1,     "next": "BE008", "obsflags": [],                  "conditions": []}
    eventlibrary['BE008'] = {"name": "Manga Breaktime", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 1,     "next": "BE009", "obsflags": [],                  "conditions": []}
    eventlibrary['BE009'] = {"name": "Goal(s)!", "girls": ["BE"], "type": EventTypeEnum.CORE,                                           "location": "track",            "priority": PrioEnum.NONE, "sp": 1,     "next": "BE011", "obsflags": [],                  "conditions": []}
    eventlibrary['BE011'] = {"name": "Quitting the Soccer Club", "girls": ["BE"], "type": EventTypeEnum.CORE,                           "location": "track",            "priority": PrioEnum.NONE, "sp": 2,     "next": "BE012", "obsflags": [],                  "conditions": []}
    eventlibrary['BE012'] = {"name": "Action at the Arcade", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "arcade",           "priority": PrioEnum.NONE, "sp": 2,     "next": "BE014", "obsflags": [],                  "conditions": []}
    eventlibrary['BE014'] = {"name": "Bouncing All Over", "girls": ["BE"], "type": EventTypeEnum.CORE,                                  "location": "hallway",          "priority": PrioEnum.NONE, "sp": 2,     "next": "BE015", "obsflags": [],                  "conditions": []}
    eventlibrary['BE015'] = {"name": "Chocolate Study", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 3,     "next": "BE016", "obsflags": [],                  "conditions": []}
    eventlibrary['BE016'] = {"name": "Basketball Practice", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "gym",              "priority": PrioEnum.NONE, "sp": 3,     "next": "BE017", "obsflags": [],                  "conditions": []}
    eventlibrary['BE017'] = {"name": "Shooting Hoops", "girls": ["BE"], "type": EventTypeEnum.CORE,                                     "location": "arcade",           "priority": PrioEnum.NONE, "sp": 3,     "next": "BE018", "obsflags": [],                  "conditions": []}
    eventlibrary['BE018'] = {"name": "Bra Fitting", "girls": ["BE", "PRG"], "type": EventTypeEnum.CORE,                                 "location": "dormBE",           "priority": PrioEnum.NONE, "sp": 3,     "next": "BE019", "obsflags": [],                  "conditions": []}
    eventlibrary['BE019'] = {"name": "The Fabled Skip Day", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "BE020", "obsflags": [],                  "conditions": []}
    eventlibrary['BE020'] = {"name": "First Date?", "girls": ["BE"], "type": EventTypeEnum.CORE,                                        "location": "hallway",          "priority": PrioEnum.NONE, "sp": 4,     "next": "BE021", "obsflags": [],                  "conditions": []} #affection check maybe?
    eventlibrary['BE021'] = {"name": "Joining the Archery Club", "girls": ["BE"], "type": EventTypeEnum.CORE,                           "location": "woods",            "priority": PrioEnum.NONE, "sp": 4,     "next": "BE022", "obsflags": [],                  "conditions": []}
    eventlibrary['BE022'] = {"name": "A Sneaky Lunch", "girls": ["BE", "BBW"], "type": EventTypeEnum.CORE,                              "location": "library",          "priority": PrioEnum.NONE, "sp": 4,     "next": "BE023", "obsflags": [],                  "conditions": []}
    eventlibrary['BE023'] = {"name": "Showdown in Archery", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "track",            "priority": PrioEnum.NONE, "sp": 4,     "next": "BE024", "obsflags": [],                  "conditions": []}
    eventlibrary['BE024'] = {"name": "I scream, You Cream", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "town",             "priority": PrioEnum.NONE, "sp": 4,     "next": "BE025", "obsflags": [],                  "conditions": []}
    eventlibrary['BE025'] = {"name": "Archery Competition", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "field",            "priority": PrioEnum.NONE, "sp": 5,     "next": "BE026", "obsflags": [],                  "conditions": []}
    eventlibrary['BE026'] = {"name": "Cicada Catching", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "field",            "priority": PrioEnum.NONE, "sp": 5,     "next": "BE027", "obsflags": [],                  "conditions": []}
    eventlibrary['BE027'] = {"name": "Clothes Shopping", "girls": ["BE"], "type": EventTypeEnum.CORE,                                   "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 5,     "next": "BE028", "obsflags": [],                  "conditions": []}
    eventlibrary['BE028'] = {"name": "Arcade Date", "girls": ["BE"], "type": EventTypeEnum.CORE,                                        "location": "arcade",           "priority": PrioEnum.NONE, "sp": 5,     "next": "BE029", "obsflags": [],                  "conditions": []}
    eventlibrary['BE029'] = {"name": "Geology Assignment", "girls": ["BE"], "type": EventTypeEnum.CORE,                                 "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "BE030", "obsflags": [],                  "conditions": []}
    eventlibrary['BE030'] = {"name": "Love Confession", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 6,     "next": "BE031", "obsflags": [],                  "conditions": []}
    eventlibrary['BE031'] = {"name": "Very Special Day", "girls": ["BE"], "type": EventTypeEnum.CORE,                                   "location": "dormBE",           "priority": PrioEnum.NONE, "sp": 6,     "next": "BE032", "obsflags": [],                  "conditions": []}
    eventlibrary['BE032'] = {"name": "The Day After", "girls": ["BE", "AE"], "type": EventTypeEnum.CORE,                                "location": "classroom",        "priority": PrioEnum.NONE, "sp": 6,     "next": "BE033", "obsflags": [],                  "conditions": []}
    eventlibrary['BE033'] = {"name": "The Great Debate", "girls": ["BE", "AE"], "type": EventTypeEnum.CORE,                             "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 6,     "next": "BE034", "obsflags": [],                  "conditions": []}
    eventlibrary['BE034'] = {"name": "No More Archery", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "field",            "priority": PrioEnum.NONE, "sp": 6,     "next": "BE035A", "obsflags": [],                  "conditions": []}
    eventlibrary['BE035'] = {"name": "New Club Intro", "girls": ["BE"], "type": EventTypeEnum.CORE,                                     "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,     "next": "BE036", "obsflags": [],                  "conditions": []}
    eventlibrary['BE035A'] = {"name": "Cooking Club Intro", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,     "next": "BE036", "obsflags": [],                  "conditions": []}
    eventlibrary['BE035B'] = {"name": "Softball Club Intro", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "baseballfield",    "priority": PrioEnum.NONE, "sp": 7,     "next": "BE036", "obsflags": [],                  "conditions": []}
    eventlibrary['BE036'] = {"name": "Flower Gazing", "girls": ["BE", "GTS"], "type": EventTypeEnum.CORE,                               "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 7,     "next": "BE037", "obsflags": [],                  "conditions": []}
    eventlibrary['BE037'] = {"name": "Dock Musing", "girls": ["BE"], "type": EventTypeEnum.CORE,                                        "location": "hillroad",         "priority": PrioEnum.NONE, "sp": 7,     "next": "BE038A", "obsflags": [],                  "conditions": []}
    eventlibrary['BE038'] = {"name": "Club Part 2", "girls": ["BE"], "type": EventTypeEnum.CORE,                                        "location": "classroom",        "priority": PrioEnum.NONE,              "next": "BE039", "obsflags": [],                       "conditions": []}
    eventlibrary['BE038A'] = {"name": "Cooking Club Part 2", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,     "next": "BE039", "obsflags": [],                  "conditions": []}
    eventlibrary['BE038B'] = {"name": "Softball Club Part 2", "girls": ["BE"], "type": EventTypeEnum.CORE,                              "location": "baseballfield",    "priority": PrioEnum.NONE, "sp": 7,     "next": "BE039", "obsflags": [],                  "conditions": []}
    eventlibrary['BE039'] = {"name": "Honoka end", "girls": ["BE"], "type": EventTypeEnum.CORE,                                         "location": "classroom",        "priority": PrioEnum.NONE,              "next": "", "obsflags": [],                       "conditions": []}

    #Optional
    eventlibrary['BE005'] = {"name": "Possible Clubs", "girls": ["BE"], "type": EventTypeEnum.OPTIONALCORE,                             "location": "classroom",        "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],                        "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['BE010'] = {"name": "Surprise, Honoka's Boobs are Bigger", "girls": ["BE"], "type": EventTypeEnum.OPTIONALCORE,        "location": "dorminterior",     "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": ["aftersize2"],                       "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['BE013'] = {"name": "Recovering from a Defeat", "girls": ["BE"], "type": EventTypeEnum.OPTIONALCORE,                   "location": "arcade",           "priority": PrioEnum.ALL,               "obsflags": [],                                   "conditions": [[ConditionEnum.FLAG, "BE013_unlock"]]}

    eventlibrary['BEGTS001'] = {"name": "You Make Me Feel Like a Woman", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,        "location": "dormexterior",     "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.VAR, "BEMode", "Feminine"], [ConditionEnum.EVENT, "BE020"]]}
    eventlibrary['BEGTS002'] = {"name": "Shining Down", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,                         "location": "dormexterior",     "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.EVENT, "BEGTS001"]]}

    #Core
    eventlibrary['FMG001'] = {"name": "Tower of Athletics", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                      "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG002", "obsflags": ["testday"],      "conditions": []}
    eventlibrary['FMG002'] = {"name": "An Off Day", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                               "location": "gym",                      "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG003", "obsflags": [],               "conditions": []}
    eventlibrary['FMG003'] = {"name": "Hallway Opportunity", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG007", "obsflags": [],               "conditions": []}
    eventlibrary['FMG007'] = {"name": "Lunch and Hobbies", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "cafeteria",                "priority": PrioEnum.NONE, "sp": 1,     "next": "FMG008", "obsflags": [],               "conditions": []}
    eventlibrary['FMG008'] = {"name": "The Pencil OF DOOM!", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "dormexterior",             "priority": PrioEnum.NONE, "sp": 1,     "next": "FMG009", "obsflags": [],               "conditions": []}
    eventlibrary['FMG009'] = {"name": "Junk Food Junkie", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                         "location": "cafeteria",                "priority": PrioEnum.NONE, "sp": 1,     "next": "FMG014", "obsflags": [],               "conditions": []}
    eventlibrary['FMG014'] = {"name": "A Problem Solver", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                         "location": "schoolplanter",            "priority": PrioEnum.NONE, "sp": 2,     "next": "FMG015", "obsflags": [],               "conditions": []}
    eventlibrary['FMG015'] = {"name": "Gifted Gaming", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "town",                     "priority": PrioEnum.NONE, "sp": 2,     "next": "FMG017", "obsflags": [],               "conditions": []}
    eventlibrary['FMG016'] = {"name": "The New Girl", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                             "location": "dorminterior",             "priority": PrioEnum.NONE, "sp": 2,     "next": "FMG017", "obsflags": [],               "conditions": []}
    eventlibrary['FMG017'] = {"name": "Beware... The Curse", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 2,     "next": "FMG018", "obsflags": [],               "conditions": []}
    eventlibrary['FMG018'] = {"name": "IT'S RAW!!!", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "cookingclassroom",         "priority": PrioEnum.NONE, "sp": 3,     "next": "FMG019", "obsflags": [],               "conditions": []}
    eventlibrary['FMG019'] = {"name": "You Shine Like the Sun", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                   "location": "roof",                     "priority": PrioEnum.NONE, "sp": 3,     "next": "FMG020", "obsflags": [],               "conditions": []}
    eventlibrary['FMG020'] = {"name": "Fly Me to the Moon", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 3,     "next": "FMG021", "obsflags": [],               "conditions": []}
    eventlibrary['FMG021'] = {"name": "EMUS!", "girls": ["FMG", "AE"], "type": EventTypeEnum.CORE,                                              "location": "library",                  "priority": PrioEnum.NONE, "sp": 4,     "next": "FMG022", "obsflags": [],               "conditions": []}
    eventlibrary['FMG022'] = {"name": "Rock Opera", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                               "location": "track",                    "priority": PrioEnum.NONE, "sp": 4,     "next": "FMG023", "obsflags": [],               "conditions": []}
    eventlibrary['FMG023'] = {"name": "The Wizard on the Sidewalk", "girls": ["FMG", "GTS"], "type": EventTypeEnum.CORE,                        "location": "town",                     "priority": PrioEnum.NONE, "sp": 4,     "next": "FMG024", "obsflags": [],               "conditions": []}
    eventlibrary['FMG024'] = {"name": "Arcade Run-in", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "arcade",                   "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG026", "obsflags": [],               "conditions": []}
    eventlibrary['FMG026'] = {"name": "Arcade Run-in", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "arcade",                   "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG027", "obsflags": [],               "conditions": []}
    eventlibrary['FMG027'] = {"name": "Study Date", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                               "location": "classroom",                "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG028", "obsflags": [],               "conditions": []}
    eventlibrary['FMG028'] = {"name": "Anything but Golf", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG029", "obsflags": [],               "conditions": []}
    eventlibrary['FMG029'] = {"name": "Akira End", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                "location": "mountain",                 "priority": PrioEnum.NONE, "sp": 5,     "next": "", "obsflags": [],                     "conditions": []}

    #Optional
    eventlibrary['FMG004'] = {"name": "Journey of 1000 Miles", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                "location": "track",                    "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG006'] = {"name": "Crying Over Spilled Milk", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                             "location": "gym",                      "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG011'] = {"name": "Press A to Start", "girls": ["FMG", "BBW"], "type": EventTypeEnum.OPTIONAL,                              "location": "dormexterior",             "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": []}
    eventlibrary['FMG012'] = {"name": "Rubbing One Out", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                      "location": "gym",                      "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG013'] = {"name": "Head Strong", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                          "location": "gym",                      "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": []}
    eventlibrary['FMGOPT016'] = {"name": "Fate at the Café", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "schoolplanter",            "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": []}
    eventlibrary['FMG025'] = {"name": "Disco Queen", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                          "location": "track",                    "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": []}
    eventlibrary['FMGBBW001'] = {"name": "Conspiracies with a Side of Cupcakes", "girls": ["FMG", "BBW"], "type": EventTypeEnum.OPTIONAL,       "location": "town",                     "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": []}

    eventlibrary['FMG005'] = {"name": "Despair in the Hallway", "girls": ["FMG"], "type": EventTypeEnum.OPTIONALCORE,                           "location": "hallway",                  "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],                      "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['FMG010'] = {"name": "The Bigger They Are...", "girls": ["FMG"], "type": EventTypeEnum.OPTIONALCORE,                           "location": "dormexterior",             "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": ["aftersize2"],                     "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}

    #Core
    eventlibrary['GTS001'] = {"name": "Girl in the Garden", "girls": ["GTS"], "type": EventTypeEnum.CORE,                  "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 0,          "next": "GTS002", "obsflags": [],       "conditions": []}
    eventlibrary['GTS002'] = {"name": "Planting Seeds", "girls": ["GTS"], "type": EventTypeEnum.CORE,                      "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 0,          "next": "GTS006", "obsflags": [],       "conditions": []}
    eventlibrary['GTS006'] = {"name": "Puppy Love", "girls": ["GTS"], "type": EventTypeEnum.CORE,                          "location": "schoolfront",      "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS007", "obsflags": [],       "conditions": []}
    eventlibrary['GTS007'] = {"name": "Homesick", "girls": ["GTS"], "type": EventTypeEnum.CORE,                            "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS008", "obsflags": [],       "conditions": []}
    eventlibrary['GTS008'] = {"name": "Secret Garden", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "roof",             "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS009", "obsflags": [],       "conditions": []}
    eventlibrary['GTS009'] = {"name": "A Tree Between Mountains", "girls": ["GTS", "BE"], "type": EventTypeEnum.CORE,      "location": "town",             "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS011b", "obsflags": [],      "conditions": []}
    eventlibrary['GTS011'] = {"name": "The Director", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS014", "obsflags": [],       "conditions": [[ConditionEnum.FLAG, "GTS011_unlock"]]}
    eventlibrary['GTS011b'] = {"name": "The Director", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS014", "obsflags": [],       "conditions": [[ConditionEnum.NOFLAG, "GTS011_unlock"]]}
    eventlibrary['GTS014'] = {"name": "A Con or Pro Fession?", "girls": ["GTS"], "type": EventTypeEnum.CORE,               "location": "classroom",        "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS015", "obsflags": [],       "conditions": []}
    eventlibrary['GTS015'] = {"name": "Decisions, Decisions", "girls": ["GTS"], "type": EventTypeEnum.CORE,                "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 3,          "next": "GTS018", "obsflags": [],       "conditions": []}
    eventlibrary['GTS018'] = {"name": "Slam Dunk", "girls": ["GTS"], "type": EventTypeEnum.CORE,                           "location": "schoolexterior",   "priority": PrioEnum.NONE, "sp": 3,          "next": "GTS019", "obsflags": [],       "conditions": []}
    eventlibrary['GTS019'] = {"name": "All in the Wrist", "girls": ["GTS"], "type": EventTypeEnum.CORE,                    "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 3,          "next": "GTS020", "obsflags": [],       "conditions": []}
    eventlibrary['GTS020'] = {"name": "Confessions of a Lonely Heart", "girls": ["GTS"], "type": EventTypeEnum.CORE,       "location": "roof",             "priority": PrioEnum.NONE, "sp": 4,          "next": "GTS021", "obsflags": [],       "conditions": []}
    eventlibrary['GTS021'] = {"name": "Taking a Breather", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 4,          "next": "GTS022", "obsflags": [],       "conditions": []}
    eventlibrary['GTS022'] = {"name": "Ya", "girls": ["GTS"], "type": EventTypeEnum.CORE,                                  "location": "library",          "priority": PrioEnum.NONE, "sp": 4,          "next": "GTS023", "obsflags": [],       "conditions": []}
    eventlibrary['GTS023'] = {"name": "Smash Cut", "girls": ["GTS"], "type": EventTypeEnum.CORE,                           "location": "schoolexterior",   "priority": PrioEnum.NONE, "sp": 4,          "next": "GTS024", "obsflags": [],       "conditions": []}
    eventlibrary['GTS024'] = {"name": "Splotchy Brown and Curling", "girls": ["GTS"], "type": EventTypeEnum.CORE,          "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 4,          "next": "GTS025", "obsflags": [],       "conditions": []}
    eventlibrary['GTS025'] = {"name": "Would it be Okay...?", "girls": ["GTS"], "type": EventTypeEnum.CORE,                "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS027", "obsflags": [],       "conditions": []}
    eventlibrary['GTS027'] = {"name": "Knock on Wood", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "roof",             "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS029", "obsflags": [],       "conditions": []}
    eventlibrary['GTS028T'] = {"name": "Art of Film", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS029", "obsflags": [],       "conditions": [[ConditionEnum.FLAG, "GTS015_movie"]]}
    eventlibrary['GTS029'] = {"name": "Growing Pains", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS030", "obsflags": [],       "conditions": []}
    eventlibrary['GTS030'] = {"name": "A Change in Scenery", "girls": ["GTS"], "type": EventTypeEnum.CORE,                 "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 6,          "next": "GTS031", "obsflags": [],       "conditions": []}
    eventlibrary['GTS031'] = {"name": "Settling In", "girls": ["GTS"], "type": EventTypeEnum.CORE,                         "location": "giantdorminterior","priority": PrioEnum.NONE, "sp": 6,          "next": "GTS032", "obsflags": [],       "conditions": []}
    eventlibrary['GTS032'] = {"name": "Journey of a Thousand Miles", "girls": ["GTS"], "type": EventTypeEnum.CORE,         "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 6,          "next": "GTS034", "obsflags": [],       "conditions": []}
    eventlibrary['GTS034'] = {"name": "A Tall Order", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 6,          "next": "GTS035", "obsflags": [],       "conditions": []}
    eventlibrary['GTS035'] = {"name": "First Impressions", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS037", "obsflags": [],       "conditions": []}
    eventlibrary['GTS037'] = {"name": "Peak Interest", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS038", "obsflags": [],       "conditions": []}
    eventlibrary['GTS038'] = {"name": "Balance", "girls": ["GTS"], "type": EventTypeEnum.CORE,                             "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS039", "obsflags": [],       "conditions": []} #intended duplicate, temporary until actual gts038 exists
    eventlibrary['GTS039'] = {"name": "Balance", "girls": ["GTS"], "type": EventTypeEnum.CORE,                             "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS040", "obsflags": [],       "conditions": []}
    eventlibrary['GTS040'] = {"name": "Naomi end", "girls": ["GTS"], "type": EventTypeEnum.CORE,                           "location": "library",          "priority": PrioEnum.NONE,                   "next": "", "obsflags": [],             "conditions": []}

    #Optional
    eventlibrary['GTS003'] = {"name": "Itadakimasu", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                     "location": "cafeteria",        "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": []}
    eventlibrary['GTS004'] = {"name": "Study Buddy", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                     "location": "library",          "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": []}
    eventlibrary['GTS012'] = {"name": "Tea?", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                            "location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": [[ConditionEnum.EVENT, "GTS011"]]}
    eventlibrary['GTS016'] = {"name": "To Bee or not to Bee", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,            "location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": []}
    eventlibrary['GTS017'] = {"name": "Getting Dirty", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                   "location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": []}

    eventlibrary['GTS005'] = {"name": "A Growing Issue", "girls": ["GTS"], "type": EventTypeEnum.OPTIONALCORE,             "location": "schoolplanter",    "priority": PrioEnum.GIRL, "sp": 1,          "obsflags": ["aftertest"],              "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['GTS010'] = {"name": "A Head Above the Class", "girls": ["GTS"], "type": EventTypeEnum.OPTIONALCORE,      "location": "classroom",        "priority": PrioEnum.GIRL, "sp": 2,          "obsflags": ["aftersize2"],             "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}

    eventlibrary['GTSPRG001'] = {"name": "A Blooming Opportunity", "girls": ["GTS", "PRG"], "type": EventTypeEnum.OPTIONAL,"location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": []}
    eventlibrary['GTSDemo'] = {"name": "Demo", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                           "location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": [[ConditionEnum.FLAG, "debug"]]}


    #Core
    eventlibrary['PRG001'] = {"name": "A Bun Tasting", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,                     "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG003", "obsflags": [],       "conditions": []}
    eventlibrary['PRG003'] = {"name": "An Inviting Aroma", "girls": ["PRG"], "type": EventTypeEnum.CORE,                        "location": "classroom",         "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG008", "obsflags": [],       "conditions": []}
    eventlibrary['PRG008'] = {"name": "Cups and Measurements", "girls": ["PRG"], "type": EventTypeEnum.CORE,                    "location": "classroom",         "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG009", "obsflags": [],       "conditions": []}
    eventlibrary['PRG009'] = {"name": "Handling with Change", "girls": ["PRG"], "type": EventTypeEnum.CORE,                     "location": "campuscenter",      "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG012", "obsflags": [],       "conditions": []}
    eventlibrary['PRG012'] = {"name": "Archetypes", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                         "location": "classroom",         "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG013", "obsflags": [],       "conditions": []}
    eventlibrary['PRG013'] = {"name": "Competitive Spirit", "girls": ["PRG"],"type": EventTypeEnum.CORE,                        "location": "classroom",         "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG014", "obsflags": [],       "conditions": []}
    eventlibrary['PRG014'] = {"name": "Cozy Lunch Time", "girls": ["PRG"], "type": EventTypeEnum.CORE,                          "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG015", "obsflags": [],       "conditions": []}
    eventlibrary['PRG015'] = {"name": "Nurturing", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "dormBBW",           "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG016", "obsflags": [],       "conditions": []}
    eventlibrary['PRG016'] = {"name": "The First Step", "girls": ["PRG"], "type": EventTypeEnum.CORE,                           "location": "classroom",         "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG017", "obsflags": [],       "conditions": []}
    eventlibrary['PRG017'] = {"name": "Slowly Blooming", "girls": ["PRG"], "type": EventTypeEnum.CORE,                          "location": "schoolplanter",     "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG019", "obsflags": [],       "conditions": []}
    eventlibrary['PRG019'] = {"name": "Seconds Please", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,                    "location": "classroom",         "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG020", "obsflags": [],       "conditions": []}
    eventlibrary['PRG020'] = {"name": "Scheduling Conflict", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,               "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG021", "obsflags": [],       "conditions": []}
    eventlibrary['PRG021'] = {"name": "Practice Makes Perfect", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,            "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG022", "obsflags": [],       "conditions": []}
    eventlibrary['PRG022'] = {"name": "Grocery Run", "girls": ["PRG"], "type": EventTypeEnum.CORE,                              "location": "supermarket",       "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG023", "obsflags": [],       "conditions": []}
    eventlibrary['PRG023'] = {"name": "Invaluable Research", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "library",           "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG024", "obsflags": [],       "conditions": []}
    eventlibrary['PRG024'] = {"name": "Flicker", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                  "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG025", "obsflags": [],       "conditions": []}
    eventlibrary['PRG025'] = {"name": "House Call", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG026", "obsflags": [],       "conditions": []}
    eventlibrary['PRG026'] = {"name": "Here Nor There", "girls": ["PRG"], "type": EventTypeEnum.CORE,                           "location": "dormPRG",           "priority": PrioEnum.ALL, "sp": 5,      "next": "PRG027", "obsflags": [],       "conditions": []}
    eventlibrary['PRG027'] = {"name": "The Morning Routine", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "dormPRG",           "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG028", "obsflags": [],       "conditions": []}
    eventlibrary['PRG028'] = {"name": "Flipping Lids", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "cookingclassroom",  "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG029", "obsflags": [],       "conditions": []}
    eventlibrary['PRG029'] = {"name": "Double Team", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                        "location": "town",              "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG030", "obsflags": [],       "conditions": []}
    eventlibrary['PRG030'] = {"name": "The Miracle of Tangents", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dormPRG",           "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG031", "obsflags": [],       "conditions": []}
    eventlibrary['PRG031'] = {"name": "Keep True", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG032", "obsflags": [],       "conditions": []}
    eventlibrary['PRG032'] = {"name": "Littering", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "schoolplanter",     "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG033", "obsflags": [],       "conditions": []}
    eventlibrary['PRG033'] = {"name": "Pensée Alimentaire", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG034", "obsflags": [],       "conditions": []}
    eventlibrary['PRG034'] = {"name": "Back in the Saddle", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "cookingclassroom",  "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG035", "obsflags": [],       "conditions": []}
    eventlibrary['PRG035'] = {"name": "Dinner for Three", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,                  "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG036", "obsflags": [],       "conditions": []}
    eventlibrary['PRG036'] = {"name": "Fallibility", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,                       "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG037", "obsflags": [],       "conditions": []}
    eventlibrary['PRG037'] = {"name": "Powering Through", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,                  "location": "classroom",         "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG038", "obsflags": [],       "conditions": []}
    eventlibrary['PRG038'] = {"name": "Lessons from the Master", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG039", "obsflags": [],       "conditions": []}
    eventlibrary['PRG039'] = {"name": "Conflicted Interests", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,               "location": "classroom",         "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG040", "obsflags": [],       "conditions": []}
    eventlibrary['PRG040'] = {"name": "Tied Up", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                  "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG041", "obsflags": [],       "conditions": []}
    eventlibrary['PRG041'] = {"name": "Expectation for the Unexpected", "girls": ["PRG", "GTS"], "type": EventTypeEnum.CORE,    "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG042", "obsflags": [],       "conditions": []}
    eventlibrary['PRG042'] = {"name": "Clean Sweep", "girls": ["PRG", "AE"], "type": EventTypeEnum.CORE,                        "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG043", "obsflags": [],       "conditions": []}
    eventlibrary['PRG043'] = {"name": "A Mother's Love", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,                   "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG044", "obsflags": [],       "conditions": []}
    eventlibrary['PRG044'] = {"name": "Spoiling", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                 "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG045", "obsflags": [],       "conditions": []}
    eventlibrary['PRG045'] = {"name": "Vider les Réservoirs", "girls": ["PRG", "BBW"], "type": EventTypeEnum.CORE,              "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG046", "obsflags": [],       "conditions": []}
    eventlibrary['PRG046'] = {"name": "The Grind", "girls": ["PRG", "BE", "AE"], "type": EventTypeEnum.CORE,                    "location": "classroom",         "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG047", "obsflags": [],       "conditions": []}
    eventlibrary['PRG047'] = {"name": "Lost in the Feels", "girls": ["PRG"], "type": EventTypeEnum.CORE,                        "location": "classroom",         "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG048", "obsflags": [],       "conditions": []}
    eventlibrary['PRG048'] = {"name": "Checking In", "girls": ["PRG"], "type": EventTypeEnum.CORE,                              "location": "classroom",         "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG049", "obsflags": [],       "conditions": []}
    eventlibrary['PRG049'] = {"name": "Purity and Peace", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG050", "obsflags": [],       "conditions": []}
    eventlibrary['PRG050'] = {"name": "Curse of the Test Taker", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dorminterior",      "priority": PrioEnum.ALL, "sp": 10,     "next": "PRG051", "obsflags": [],       "conditions": []}
    eventlibrary['PRG051'] = {"name": "Dinner and Chill", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "dorminterior",      "priority": PrioEnum.ALL, "sp": 10,     "next": "PRG052", "obsflags": [],       "conditions": []}
    eventlibrary['PRG052'] = {"name": "Icebreaker", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "dorminterior",      "priority": PrioEnum.ALL, "sp": 10,     "next": "PRG053", "obsflags": [],       "conditions": []}
    eventlibrary['PRG053'] = {"name": "Sugar and Rainbows", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "dormPRG",           "priority": PrioEnum.ALL, "sp": 11,     "next": "PRG054", "obsflags": [],       "conditions": []}
    eventlibrary['PRG054'] = {"name": "Down to the Wire", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "campuscenter",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG055A", "obsflags": [],      "conditions": []}
    eventlibrary['PRG055A'] = {"name": "Back to the Basics", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG056A", "obsflags": [],      "conditions": []}
    eventlibrary['PRG055B'] = {"name": "Snowballing", "girls": ["PRG", "AE"], "type": EventTypeEnum.CORE,                       "location": "town",              "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG056B", "obsflags": [],      "conditions": []}
    eventlibrary['PRG055C'] = {"name": "Successful Failure", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG056C", "obsflags": [],      "conditions": []}
    eventlibrary['PRG056A'] = {"name": "Fake it 'till You Make it", "girls": ["PRG"], "type": EventTypeEnum.CORE,               "location": "hallway",           "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG057A", "obsflags": [],      "conditions": []}
    eventlibrary['PRG056B'] = {"name": "Falling For Her", "girls": ["PRG", "AE"], "type": EventTypeEnum.CORE,                   "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG057B", "obsflags": [],      "conditions": []}
    eventlibrary['PRG056C'] = {"name": "Go Team!", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "hallway",           "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG057C", "obsflags": [],      "conditions": []}
    eventlibrary['PRG056'] = {"name": "Down to the Wire", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "campuscenter",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG055A", "obsflags": [],      "conditions": []} #temporary hack fix
    eventlibrary['PRG057A'] = {"name": "Practicing Perfection", "girls": ["PRG"], "type": EventTypeEnum.CORE,                   "location": "hallway",           "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG058", "obsflags": [],       "conditions": []}
    eventlibrary['PRG057B'] = {"name": "The Gift of Thought", "girls": ["PRG"], "type": EventTypeEnum.CORE,                     "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG058", "obsflags": [],       "conditions": []}
    eventlibrary['PRG057C'] = {"name": "Power of a Protoge", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG058", "obsflags": [],       "conditions": []}
    eventlibrary['PRG058'] = {"name": "Aida end", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                 "location": "library",           "priority": PrioEnum.NONE, "sp": 11,    "obsflags": [],                         "conditions": []}

    eventlibrary['PRGend_nofather'] = {"name": "Guiding Hand", "girls": ["PRG"], "type": EventTypeEnum.CORE,                    "location": "dorminterior",       "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG027Z'] = {"name": "Guiding Hand", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                      "location": "dorminterior",       "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG028Z'] = {"name": "Head Case", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                         "location": "hallway",           "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG029Z'] = {"name": "Patchwork", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "hallway",           "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG030Z'] = {"name": "Memoric Gazes", "girls": ["PRG"], "type": EventTypeEnum.CORE,                           "location": "hallway",           "priority": PrioEnum.NONE, "sp": 6,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG031Z'] = {"name": "Aida end", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "library",           "priority": PrioEnum.NONE,              "obsflags": [],                         "conditions": []}

    #Optional
    eventlibrary['PRG001b'] = {"name": "Tongue Twister", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                      "location": "schoolexterior",   "priority": PrioEnum.NONE,              "obsflags": ["testday"],                "conditions": []}
    eventlibrary['PRG004'] = {"name": "Mother Nature", "girls": ["PRG", "FMG"], "type": EventTypeEnum.OPTIONAL,                 "location": "track",            "priority": PrioEnum.NONE,              "obsflags": [],                         "conditions": []}
    eventlibrary['PRG006'] = {"name": "Double Stacked", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                       "location": "campuscenter",     "priority": PrioEnum.NONE,              "obsflags": [],                         "conditions": []}
    eventlibrary['PRG007'] = {"name": "A (Soft) Wall to Hide Behind", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,         "location": "cafeteria",        "priority": PrioEnum.NONE,              "obsflags": [],                         "conditions": []}
    eventlibrary['PRG011'] = {"name": "Homerun!", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                             "location": "classroom",        "priority": PrioEnum.NONE,              "obsflags": [],                         "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['PRG018'] = {"name": "A Small Touchup", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                      "location": "campuscenter",     "priority": PrioEnum.NONE,              "obsflags": [],                         "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}

    eventlibrary['PRG005'] = {"name": "Hold on Tight", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,                    "location": "auditorium",       "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],              "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['PRG010'] = {"name": "Rapidly Curvy", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,                    "location": "cookingclassroom", "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": ["aftersize2"],             "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['PRG026b'] = {"name": "", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                                    "location": "classroom",        "priority": PrioEnum.ALL,               "obsflags": [],                         "conditions": [[ConditionEnum.TIMEFLAG, "size3"], [ConditionEnum.NOROUTELOCK, "PRG"], [ConditionEnum.NOROUTELOCK, ""]]}
