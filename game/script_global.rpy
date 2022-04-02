#Characters

#Main Protagonist
define MC = Character('Keisuke', color="#0066CC", image="MC") # Main Character, speaking.
define MCT = Character('Keisuke', color="#0066CC", what_prefix='(', what_suffix=')', image="MC")
define MCCell = Character('Keisuke', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="MC")
define AltMC = Character('Keisuke', color="#0066CC") #For flashback Keisuke, will not show graphic alongside his text.

#Main Cast
define AE = Character('Shiori', color="#FF3300")
define BE = Character('Honoka', color="#FCCF20")
define BECell = Character('Honoka', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="BECell")
define FMG = Character('Akira', color="#FF9900")
define FMGCell = Character('Akira', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="FMGCell")
define GTS = Character('Naomi', color="#66FF33")
define GTS_S = Character('Naomi', color="#66FF33", image="GTS_S")
define GTSCell = Character('Naomi', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="GTSCell")
define PRG = Character('Aida', color="#FF3399", what_prefix='{size=-6}', what_suffix='{/size}')
define PRGCell = Character('Aida', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="PRGCell")
define WG = Character('Alice', color="#CC33FF")
define WGCell = Character('Alice', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="WGCell")

define MC_FMG = Character('Keisuke & Akira', color="#C0C0C0")
define MC_BE = Character('Keisuke & Honoka', color="#C0C0C0")

#Supporting Cast
define Chibuki = Character('Chibuki', color="#CC33FF")
define ChibukiCell = Character('Chibuki', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="ChibukiCell")
define Jineko = Character('Jineko', color="#228B22")
define Kokutan = Character('Kokutan', color="#C0C0C0")
define Minori = Character('Minori', color="#FF91DC")
define Natsuko = Character('Natsuko', color="#C0C0C0")
define RM = Character('Daichi', color="#BDB8A5")
define Ryoko = Character('Ryoko', color="#FF91DC")
define Sakura = Character('Sakura', color="#FF3399")
define Tako = Character('Tako', color="#ce9b50")
define Yuki = Character('Yuki', color="#FF91DC")

#School Staff
define HR = Character('Tashi-sensei', color="#C0C0C0")
define Naoki = Character('Naoki-sensei', color="#C0C0C0")
define Nurse = Character('Nurse Kiyomi', color="#C0C0C0") #Lips
define Nurse2 = Character('Nurse Kiyomi', color="#0099CC") # Nails
define Lunch = Character('Lunchlady', color="#CC33FF")
define Hageshi = Character('Hageshi-sensei', color="#C0C0C0")
define Principal = Character('Principal Noguchi', color="#C0C0C0")
define Takamura = Character('Takamura-sensei', color="#C0C0C0")
define Tsubasa = Character('Tsubasa-sensei', color="#C0C0C0")

#Parents and Other Relatives
define Akihiro = Character('Akihiro', color="#C0C0C0") #Naomi’s Father
define Dad = Character('Dad', color="#C0C0C0") #Keisuke’s Father
define Daitaro = Character('Daitaro', color="#C0C0C0") #Alice’s Father
define Kazumi = Character('Kazumi', color="#C0C0C0") #Naomi’s Sister
define Midori = Character('Midori', color="#C0C0C0") #Akira’s Father
define Miko = Character('Miko', color="#C0C0C0") #Naomi’s Mother
define Minami = Character('Minami', color="#C0C0C0") #Shiori’s Mother
define Mom = Character('Mom', color="#FF3300") #Keisuke’s Mother
define MomCell = Character('Mom', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}') #Keisuke’s Mother Cell
define TakaraUnknown = Character('Aida\'s Mother', color="#C0C0C0") #Aida’s Mother
define Takara = Character('Takara', color="#C0C0C0") #Aida’s Mother
define Tomoko = Character('Tomo', color="#FF3300") #Keisuke’s Sister
define TomokoCell = Character('Tomo', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}', image="TomoCell") #Keisuke’s Sister Cell
define Yuko = Character('Yuko', color="#C0C0C0") #Akira’s Mother

#Other Students
define Fumika = Character('Fumika', color="#FF91DC") #GTS Route
define Hamikawa = Character('Hamikawa', color="#C0C0C0") #AE Route
define Haruhiro = Character('Haruhiro', color="#C0C0C0") #BE Route
define Kanami = Character('Kanami', color="#C0C0C0") #BE Route
define Koneko = Character('Koneko', color="#C0C0C0") #BE Route
define Michiko = Character('Michiko', color="#C0C0C0") #PRG Route
define Sakie = Character('Sakie', color="#C0C0C0") #BE Route

#Background Characters
define Akio = Character('Akio', color="#C0C0C0") #GTS Route
define Chie = Character('Chie', color="#FF9900") #FMG Route, MC Route
define Francois = Character('François', color="#CC33FF") #WG Route
define Fujimoto = Character('Fujimoto', color="#FF9900") #FMG Route
define Haruko = Character('Haruko', color="#FF9900") #FMG Route, MC Route
define Katsumi = Character('Katsumi', color="#C0C0C0") #AE Route
define Lee = Character('Lee', color="#C0C0C0") #WG Route - Summer Arc
define Minei = Character('Minei', color="#C0C0C0") #FMG Route
define Misaki = Character('Misaki', color="#C0C0C0") #WG Route
define Miura = Character('Miura', color="#C0C0C0") #FMG Route
define Shino = Character('Shino', color="#C0C0C0") #WG Route - Summer Arc
define Takada = Character('Takada', color="#C0C0C0") #WG Route - Summer Arc
define Wobbles = Character('Wobbles', color="#E54C84") #AE Route - Shiori's Hypnotized State

#General Use
define All = Character('Everyone', color="#ffffff")
define Announcer = Character('Announcer', color="#C0C0C0")
define Barker = Character('Barker', color="#C0C0C0")
define Barista = Character('Barista', color="#C0C0C0")
define Card = Character('Card', color="#C0C0C0")
define Carnie = Character('Carnie', color="#C0C0C0")
define Cashier = Character('Cashier', color="#C0C0C0")
define Cat = Character('Cat', color="#C0C0C0")
define Cell = Character('Cell', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Chauffeur = Character('Chauffeur', color="#C0C0C0")
define Chef = Character('Chef', color="#C0C0C0")
define Clown = Character('Clown', color="#C0C0C0")
define CMM = Character('Male Council Member', color="#ffa18a") #Lighter Orange
define CMF = Character('Female Council Member', color="#ffa18a") #Lighter Orange
define Coach = Character('Coach', color="#C0C0C0")
define Cook = Character('Cook', color="#C0C0C0")
define Computer = Character('Computer', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define DJ = Character('DJ', color="#C0C0C0")
define FemStudent1 = Character('Female Student 1', color="#ce6950") #New color maybe?
define FemStudent2 = Character('Female Student 2', color="#ce9b50") #New color maybe?
define Girls = Character('Girls', color="#ffffff")
define Guard = Character('Guard', color="#C0C0C0")
define Hostess = Character('Hostess', color="#C0C0C0")
define Interviewer = Character('Interviewer', color="#C0C0C0")
define Judge = Character('Judge', color="#C0C0C0")
define LittleGirl = Character('Little Girl', color="#FF91DC")
define Letter = Character('Letter', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Magician = Character('Magician', color="#C0C0C0")
define Note = Character('Note', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Owner = Character('Store Owner', color="#C0C0C0")
define Receptionist = Character('Receptionist', color="#C0C0C0")
define Referee = Character('Referee', color="#C0C0C0")
define Student = Character('Student', color="#FF3300")
define Student1 = Character('Student 1', color="#FF3300")
define Student2 = Character('Student 2', color="#FF3300")
define Student3 = Character('Student 3', color="#FF3300")
define Teacher = Character('Teacher', color="#C0C0C0")
define Umpire = Character('Umpire', color="#C0C0C0")
define UNKNOWN = Character('???', color="#FFFFFF")
define UNKNOWNCell = Character('???', color="#C0C0C0", what_prefix='{i}', what_suffix='{/i}')
define Vendor = Character('Vendor', color="#FFFFFF")
define Waiter = Character('Waiter', color="#C0C0C0")
define Waitress = Character('Waitress', color="#C0C0C0")
define Woman = Character('Woman', color="#C0C0C0")

#Scenes
image white = Solid((255, 255, 255, 255))
image black = Solid((0, 0, 0, 255))

#Campus
image Art Classroom = DynamicImage("Graphics/ui/bg/artroom_[gametime].png")
image Auditorium = DynamicImage("Graphics/ui/bg/archiveBG/auditorium_[gametime].png")
image Baseball Field = "Graphics/ui/bg/NYI.png"
image Bathroom = "Graphics/ui/bg/archiveBG/bathroom.png"
image Cafeteria = "Graphics/ui/bg/archiveBG/cafeteria.png"
image Campus Center = DynamicImage("Graphics/ui/bg/archiveBG/campuscenter_[gametime].png")
image Classroom = DynamicImage("Graphics/ui/bg/classroom_[gametime].png")
image Classroom2 = DynamicImage("Graphics/ui/bg/classroom_2_[gametime].png")
image Classroom3 = DynamicImage("Graphics/ui/bg/archiveBG/classroom_3_[gametime].png")
image Clock Tower = DynamicImage("Graphics/ui/bg/clocktower_[gametime].png")
image Computer Room = DynamicImage("Graphics/ui/bg/computerroom_[gametime].png")
image Cooking Classroom = "Graphics/ui/bg/cooking.png"
image Faculty Room = DynamicImage("Graphics/ui/bg/archiveBG/facultyroom_[gametime].png")
image Gate Front = "Graphics/ui/bg/gatefront.png"
image Gym = DynamicImage("Graphics/ui/bg/gym_[gametime].png")
image Hallway = DynamicImage("Graphics/ui/bg/archiveBG/schoolhallway1_[gametime].png")
image Hallway2 = DynamicImage("Graphics/ui/bg/archiveBG/schoolhallway2_[gametime].png")
image HallwayStairs = DynamicImage("Graphics/ui/bg/schoolhallway_[gametime].png")
image Hill Road = "Graphics/ui/bg/NYI.png"
image Hospital Room = "Graphics/ui/bg/NYI.png"
image Info Desk = DynamicImage("Graphics/ui/bg/archiveBG/infodesk_[gametime].png")
image Library = DynamicImage("Graphics/ui/bg/archiveBG/library_[gametime].png")
image Lockers = DynamicImage("Graphics/ui/bg/lockers_[gametime].png")
image Music Classroom = DynamicImage("Graphics/ui/bg/archiveBG/music_[gametime].png")
image Nurse Office = DynamicImage("Graphics/ui/bg/archiveBG/nurseoffice_[gametime].png")
image Office = DynamicImage("Graphics/ui/bg/archiveBG/office_[gametime].png")
image Pool = DynamicImage("Graphics/ui/bg/archiveBG/schoolpool_[gametime].png")
image Recreation = "Graphics/ui/bg/NYI.png"
image Roof = DynamicImage("Graphics/ui/bg/roof_[gametime].png")
image Roof Entrance = DynamicImage("Graphics/ui/bg/roofentrance_[gametime].png")
image School Exterior = DynamicImage("Graphics/ui/bg/archiveBG/schoolexterior_[gametime].png")
image School Front = DynamicImage("Graphics/ui/bg/schoolfront_[gametime].png")
image School Inner = "Graphics/ui/bg/schoolinner.png"
image School Planter = "Graphics/ui/bg/schoolplanter.png"
image School Shed = DynamicImage("Graphics/ui/bg/schoolshed_[gametime].png")
image Student Government = DynamicImage("Graphics/ui/bg/archiveBG/studentgovernment_[gametime].png")
image Track = DynamicImage("Graphics/ui/bg/archiveBG/track_[gametime].png")
image Workshop = "Graphics/ui/bg/NYI.png"

#Dorms
image Dorm Exterior = DynamicImage("Graphics/ui/bg/dormexterior_[gametime].png")
image Dorm Hallway = "Graphics/ui/bg/archiveBG/dormhallway.png"
image Dorm Interior = DynamicImage("Graphics/ui/bg/archiveBG/dorminterior_[gametime].png")
image Dorm AE = DynamicImage("Graphics/ui/bg/archiveBG/AEdorm_[gametime].png")
image Dorm BE = DynamicImage("Graphics/ui/bg/archiveBG/BEdorm_[gametime].png")
image Dorm FMG = DynamicImage("Graphics/ui/bg/archiveBG/FMGdorm_[gametime].png")
image Dorm GTS = DynamicImage("Graphics/ui/bg/archiveBG/GTSdorm_[gametime].png")
image Dorm PRG = DynamicImage("Graphics/ui/bg/PRGdorm_[gametime].png")
image Dorm WG = DynamicImage("Graphics/ui/bg/archiveBG/WGDorm_[gametime].png")
image Dorm WG Flip = im.Flip("Graphics/ui/bg/archiveBG/WGDorm_day.png", horizontal=True)
image Dorm Tomoko = "Graphics/ui/bg/NYI.png"

#Giants Facilities
image Chukan Point = DynamicImage("Graphics/ui/bg/chukanpoint_[gametime].png")
image Courtyard GTS = "Graphics/ui/bg/NYI.png"
image Giant Dorm Exterior = DynamicImage("Graphics/ui/bg/GTSdorm_quarry_exterior_[gametime].png")
image Giant Dorm Interior = DynamicImage("Graphics/ui/bg/GTSdorm_quarry_interior_[gametime].png")

#Seichou Town
image Arcade = DynamicImage("Graphics/ui/bg/archiveBG/arcade_[gametime].png")
image Art Gallery = "Graphics/ui/bg/NYI.png"
image Ballroom = DynamicImage("Graphics/ui/bg/archiveBG/ballroom_[gametime].png")
image Cafe = DynamicImage("Graphics/ui/bg/archiveBG/cafe_[gametime].png")
image Clothes Store = "Graphics/ui/bg/archiveBG/clothesstore.png"
image Disco Club = "Graphics/ui/bg/NYI.png"
image Diner = "Graphics/ui/bg/archiveBG/burgerrestaurant.png"
image Festival = DynamicImage("Graphics/ui/bg/archiveBG/festival_[gametime].png")
image Festive Tent = "Graphics/ui/bg/NYI.png"
image Game Store = "Graphics/ui/bg/archiveBG/gamestore.png"
image Hotel Room = DynamicImage("Graphics/ui/bg/archiveBG/hotelroom_[gametime].png")
image Movie Theater = "Graphics/ui/bg/archiveBG/movietheater.png"
image Movie Theater Lights = "Graphics/ui/bg/archiveBG/movietheater_lights.png"
image Movie Theater Exterior = DynamicImage("Graphics/ui/bg/archiveBG/movietheaterext_[gametime].png")
image Park = DynamicImage("Graphics/ui/bg/archiveBG/park_[gametime].png")
image Pharmacy = DynamicImage("Graphics/ui/bg/archiveBG/pharmacy_[gametime].png")
image Restaurant = "Graphics/ui/bg/restaurant.png"
image Store = DynamicImage("Graphics/ui/bg/store_[gametime].png")
image Supermarket = DynamicImage("Graphics/ui/bg/archiveBG/supermarket_[gametime].png")
image Sushi Restaurant = "Graphics/ui/bg/sushirestaurant.png"
image Theater Exterior = DynamicImage("Graphics/ui/bg/theater-exterior_[gametime].png")
image Theater Interior = "Graphics/ui/bg/theater-interior.png"
image Theater Interior Spotlight = "Graphics/ui/bg/theater-interior-spotlight.png"
image Town = DynamicImage("Graphics/ui/bg/archiveBG/town_[gametime].png")
image Town Docks = DynamicImage("Graphics/ui/bg/archiveBG/towndocks_[gametime].png")

#Satoyama Village
image Hot Springs = DynamicImage("Graphics/ui/bg/archiveBG/hotsprings_[gametime].png")
image Hot Springs Steamed = DynamicImage("Graphics/ui/bg/archiveBG/hotsprings_steamed_[gametime].png")
image Ryokan Exterior = DynamicImage("Graphics/ui/bg/archiveBG/ryokanexterior_[gametime].png")
image Ryokan Room = DynamicImage("Graphics/ui/bg/archiveBG/ryokanroom_[gametime].png")

#Giants Town
image Giants Town = "Graphics/ui/bg/NYI.png"
image Giants Town Store = "Graphics/ui/bg/NYI.png"

#Mountains
image Mountains = DynamicImage("Graphics/ui/bg/archiveBG/mountains_[gametime].png")
image Mountains Shrine = "Graphics/ui/bg/mountains_shrine.png"
image Mountains Torii Gate = "Graphics/ui/bg/mountains_gate.png"

#Island
image Beach = DynamicImage("Graphics/ui/bg/beach_[gametime].png")
image Dock = "Graphics/ui/bg/dock_[gametime].png"
image Field = DynamicImage("Graphics/ui/bg/archiveBG/field_[gametime].png")
image Field Winter = DynamicImage("Graphics/ui/bg/archiveBG/field_[gametime].png") #TBI
image Lake Road = DynamicImage("Graphics/ui/bg/lakeroad_[gametime].png")
image Woods = DynamicImage("Graphics/ui/bg/archiveBG/woods_[gametime].png")
image Frozen Beach = "Graphics/ui/bg/NYI.png"

#Alice’s Summer Estate
image RV Interior = "Graphics/ui/bg/WG_summer_rv.png"
image Summer Balcony Exterior = DynamicImage("Graphics/ui/bg/WG_summer_balcony_ext_[gametime].png")
image Summer Balcony Interior = DynamicImage("Graphics/ui/bg/WG_summer_balcony_ext_[gametime].png")
image Summer Beach = DynamicImage("Graphics/ui/bg/WG_summer_beach_[gametime].png")
image Summer Beach Closed = "Graphics/ui/bg/WG_summer_beach_closed.png"
image Summer Beach Ocean = "Graphics/ui/bg/WG_summer_beach_ocean.png"
image Summer Bedroom = DynamicImage("Graphics/ui/bg/WG_summer_bedroom_[gametime].png")
image Summer Dining Room = "Graphics/ui/bg/WG_summer_diningroom.png"
image Summer Guest Bathroom = DynamicImage("Graphics/ui/bg/WG_summer_guest_bathroom_[gametime].png")
image Summer Guest Bathroom Steamed = DynamicImage("Graphics/ui/bg/WG_summer_guest_bathroom_steamed_[gametime].png")
image Summer Guest Bedroom = DynamicImage("Graphics/ui/bg/WG_summer_guest_bedroom_[gametime].png")
image Summer Hallway = "Graphics/ui/bg/WG_summer_hallway.png"
image Summer House Back = "Graphics/ui/bg/WG_summer_houseback.png"
image Summer House Entrance = "Graphics/ui/bg/WG_summer_entrance.png"
image Summer House Front = "Graphics/ui/bg/WG_summer_housefront.png"
image Summer Living Room = "Graphics/ui/bg/WG_summer_livingroom.png"

#Okinawa - FMG Arc
image Okinawa Airport = "Graphics/ui/bg/archiveBG/okinawa_airport.png"
image Okinawa Beach = DynamicImage("Graphics/ui/bg/archiveBG/okinawa_beach_[gametime].png")
image Okinawa Bedroom = DynamicImage("Graphics/ui/bg/archiveBG/okinawa_bedroom_[gametime].png")
image Okinawa Cottage = "Graphics/ui/bg/archiveBG/okinawa_cottage.png"
image Okinawa Island = "Graphics/ui/bg/archiveBG/okinawa_island.png"
image Okinawa Market = "Graphics/ui/bg/archiveBG/okinawa_market.png"
image Okinawa Ocean = DynamicImage("Graphics/ui/bg/archiveBG/okinawa_ocean_[gametime].png")

#General
image Airport = "Graphics/ui/bg/NYI.png"
image Bus Interior = DynamicImage("Graphics/ui/bg/archiveBG/businterior_[gametime].png")
image Ferry = DynamicImage("Graphics/ui/bg/ferry_[gametime].png")
image Plane Interior = "Graphics/ui/bg/NYI.png"

#CG + Images
image daymenubg = "Graphics/ui/bg/archiveBG/menubg-day.png"

image cg AE000 = "Graphics/ui/gallery/AE000.png"
image cg AE015 = "Graphics/ui/gallery/AE015.png"
image cg AE024 = "Graphics/ui/gallery/AE024.png"
image cg AE024b = "Graphics/ui/gallery/AE024b.png"
image cg AE024c = "Graphics/ui/gallery/AE024c.png"
image cg AE024d = "Graphics/ui/gallery/AE024d.png"
image cg AE024e = "Graphics/ui/gallery/AE024e.png"
image cg AE025 = "Graphics/ui/gallery/AE025.png"
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
image cg AE053_mirror1 = "Graphics/ui/gallery/AE053_mirror1.png"
image cg AE053_mirror2 = "Graphics/ui/gallery/AE053_mirror2.png"
image cg AE074_snow1 = "Graphics/ui/gallery/AE074_snow1.png"
image cg AE074_snow2 = "Graphics/ui/gallery/AE074_snow2.png"
image cg AE074_snow3 = "Graphics/ui/gallery/AE074_snow3.png"

image cg BE000 = "Graphics/ui/gallery/BE000.png"
image cg BE000b = "Graphics/ui/gallery/BE000b.png"
image cg BE001 = "Graphics/ui/gallery/BE001.png"
image cg BE010 = "Graphics/ui/gallery/BE010.png"
image cg BE028 = "Graphics/ui/gallery/BE028.png"
image cg BE028_fem = "Graphics/ui/gallery/BE028_fem.png"
image cg BE031 = "Graphics/ui/gallery/BE031.png"
image cg BE031b = "Graphics/ui/gallery/BE031b.png"
image cg BE031c = "Graphics/ui/gallery/BE031c.png"
image cg BE032 = "Graphics/ui/gallery/BE032.png"

image cg FMG016 = "Graphics/ui/gallery/FMG016.png"
image cg FMG041 = "Graphics/ui/gallery/FMG041.png"
image cg FMG050 = "Graphics/ui/gallery/FMG050.png"
image cg FMG055 = "Graphics/ui/gallery/FMG055.png"
image cg FMG056 = "Graphics/ui/gallery/FMG056.png"
image cg FMG061 = "Graphics/ui/gallery/FMG061.png"

image cg GTS000 = "Graphics/ui/gallery/GTS000.png"
image cg GTS024 = "Graphics/ui/gallery/GTS024.png"
image cg GTS025 = "Graphics/ui/gallery/GTS025.png"
image cg GTS035 = "Graphics/ui/gallery/GTS035.png"
image cg GTS044_stars1 = "Graphics/ui/gallery/GTS044_stars1.png"
image cg GTS044_stars2 = "Graphics/ui/gallery/GTS044_stars2.png"
image cg GTS046 = "Graphics/ui/gallery/GTS046.png"

image cg PRG020 = "Graphics/ui/gallery/PRG020.png"
image cg PRG025 = "Graphics/ui/gallery/PRG025.png"
image cg PRG038 = "Graphics/ui/gallery/PRG038.png"

image cg WG000 = "Graphics/ui/gallery/WG000.png"
image cg WG009 = "Graphics/ui/gallery/WG009.png"
image cg WG010 = "Graphics/ui/gallery/WG010.png"
image cg WG039 = "Graphics/ui/gallery/WG039.png"
image cg WG042 = "Graphics/ui/gallery/WG042.png"
image cg WG046 = "Graphics/ui/gallery/WG046.png"
image cg WG047 = "Graphics/ui/gallery/WG047.png"
image cg WG060S = "Graphics/ui/gallery/WG060S.png"

image cg MC000 = "Graphics/ui/gallery/MC000.png"

image cg RM000 = "Graphics/ui/gallery/RM000.png"
image cg RM000_escape1 = "Graphics/ui/gallery/RM000_escape1.png"
image cg RM000_escape2 = "Graphics/ui/gallery/RM000_escape2.png"
image cg RM000_escape3 = "Graphics/ui/gallery/RM000_escape3.png"

#Character sprites
image AE neutral = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral.png")
image AE neutral-annoyed = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral-annoyed.png")
image AE neutral-eyebrow = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral-eyebrow.png")
image AE neutral-noglasses = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral-noglasses.png")
image AE neutral-smug = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/neutral-smug.png")
image AE happy = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/happy.png")
image AE smile = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/happy-2.png")
image AE pondering = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/pondering.png")
image AE sad = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/sad.png")
image AE sad-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/sad-2.png")
image AE frown = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/sad.png")
image AE surprised = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/surprised.png")
image AE surprised-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/surprised-2.png")
image AE admire = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/admire.png")
image AE angry = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/angry.png")
image AE angry-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/angry-2.png")
image AE angry-3 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/angry-3.png")
image AE angry-4 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/angry-4.png")
image AE aroused = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/aroused.png")
image AE back = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/behind.png")
image AE embarrassed = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/embarrassed.png")
image AE aroused-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/aroused-2.png")
image AE aroused-3 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/aroused-3.png")
image AE aroused-4 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/aroused-4.png")
image AE glasses = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/unique.png")
image AE glasses-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/unique-2.png")
image AE glasses-3 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/unique-3.png")
image AE ass = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/ass.png")
image AE ass-2 = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/ass.png")
image AE afraid = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/afraid.png")
image AE ahegao = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/ahegao.png")
image AE hatred = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/hatred.png")
image AE love = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/love.png")
image AE rage = DynamicImage("Graphics/AE/[globalsize]/[AEOutfit]/rage.png")

image BE neutral = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/neutral.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/neutral.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE happy = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/happy.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/happy.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE sad = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/sad.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/sad.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE surprised = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/surprised.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/surprised.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE surprised-2 = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/surprised-2.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/surprised-2.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE angry = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/angry.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/angry.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE aroused = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/aroused.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/aroused.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE unique = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/unique.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/unique.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE confused = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/confused.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/confused.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE disoriented = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/disoriented.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/disoriented.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE doubt = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/doubt.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/doubt.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE embarrassed = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/embarrassed.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/embarrassed.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE seductive = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/seductive.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/seductive.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE shrug = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/shrug.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/shrug.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE wink = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/wink.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/wink.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )
image BE worried = Composite(
    (513, 686),
    (0, 0), ConditionSwitch(
        "globalsize >= 4", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/worried.png"),
        None, Null()),
    (24, 0), ConditionSwitch(
        "globalsize <= 3", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/worried.png"),
        None, Null()),
    (0, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize >= 4 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null()),
    (24, 0), ConditionSwitch(
        "getVar('BEMode') == 'Feminine' and globalsize <= 3 and BEOutfit == OutfitEnum.DEFAULT", "Graphics/BE/[globalsize]/[BEOutfit]/fem_outfit.png",
        None, Null())
    )

image FMG neutral = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/neutral.png")
image FMG happy = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/happy.png")
image FMG sad = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/sad.png")
image FMG sad-2 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/sad-2.png")
image FMG sad-3 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/sad-3.png")
image FMG surprised = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/surprised.png")
image FMG surprised-2 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/surprised-2.png")
image FMG confused = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/surprised.png")
image FMG angry = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/angry.png")
image FMG angry-2 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/angry-2.png")
image FMG angry-3 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/angry-3.png")
image FMG aroused = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/aroused.png")
image FMG aroused-2 = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/aroused-2.png")
image FMG flex = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/flex.png")
image FMG upbeat = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/upbeat.png")

image GTS neutral = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/neutral.png")
image GTS neutral-2 = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/neutral-2.png")
image GTS happy = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/happy.png")
image GTS happy-2 = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/happy-2.png")
image GTS sad = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/sad.png")
image GTS sad-2 = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/sad-2.png")
image GTS surprised = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/surprised.png")
image GTS angry = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/angry.png")
image GTS aroused = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/aroused.png")
image GTS embarrassed = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/embarrassed.png")
image GTS shy = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/embarrassed.png")
image GTS blush = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/embarrassed.png")
image GTS wink = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/wink.png")
image GTS unique = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/unique.png")
image GTS unique-2 = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/unique-2.png")
image GTS despaired-thought = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/despaired-thought.png")
image GTS pondering = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/pondering.png")

image GTS_S neutral = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/neutral.png")
image GTS_S neutral-2 = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/neutral-2.png")
image GTS_S happy = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/happy.png")
image GTS_S happy-2 = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/happy-2.png")
image GTS_S sad = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/sad.png")
image GTS_S sad-2 = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/sad-2.png")
image GTS_S surprised = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/surprised.png")
image GTS_S angry = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/angry.png")
image GTS_S aroused = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/aroused.png")
image GTS_S embarrassed = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/embarrassed.png")
image GTS_S shy = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/embarrassed.png")
image GTS_S blush = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/embarrassed.png")
image GTS_S wink = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/wink.png")
image GTS_S unique = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/unique.png")
image GTS_S unique-2 = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/unique-2.png")
image GTS_S despaired-thought = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/despaired-thought.png")
image GTS_S pondering = DynamicImage("Graphics/GTS/[globalsize]_s/[GTSOutfit]/pondering.png")

image side GTS_S neutral = DynamicImage("Graphics/GTS/[globalsize]_s/side/neutral.png")
image side GTS_S neutral-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side/neutral.png") #nyi
image side GTS_S happy = DynamicImage("Graphics/GTS/[globalsize]_s/side/happy.png")
image side GTS_S happy-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side/happy.png") #nyi
image side GTS_S sad = DynamicImage("Graphics/GTS/[globalsize]_s/side/sad.png")
image side GTS_S sad-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side/sad-2.png")
image side GTS_S surprised = DynamicImage("Graphics/GTS/[globalsize]_s/side/surprised.png")
image side GTS_S angry = DynamicImage("Graphics/GTS/[globalsize]_s/side/angry.png")
image side GTS_S aroused = DynamicImage("Graphics/GTS/[globalsize]_s/side/aroused.png")
image side GTS_S embarrassed = DynamicImage("Graphics/GTS/[globalsize]_s/side/embarrassed.png")
image side GTS_S shy = DynamicImage("Graphics/GTS/[globalsize]_s/side/embarrassed.png")
image side GTS_S blush = DynamicImage("Graphics/GTS/[globalsize]_s/side/embarrassed.png")
image side GTS_S wink = DynamicImage("Graphics/GTS/[globalsize]_s/side/wink.png")
image side GTS_S unique = DynamicImage("Graphics/GTS/[globalsize]_s/side/unique.png")
image side GTS_S unique-2 = DynamicImage("Graphics/GTS/[globalsize]_s/side/unique-2.png")
image side GTS_S despaired-thought = DynamicImage("Graphics/GTS/[globalsize]_s/side/despaired-thought.png")
image side GTS_S pondering = DynamicImage("Graphics/GTS/[globalsize]_s/side/pondering.png")

image PRG neutral = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/neutral.png")
image PRG happy = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/happy.png")
image PRG excited = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/excited.png")
image PRG sad = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/sad.png")
image PRG surprised = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/surprised.png")
image PRG angry = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/angry.png")
image PRG aroused = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/aroused.png")
image PRG blush = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/blush.png")
image PRG flattered = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/flattered.png")
image PRG unique = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/unique.png")
image PRG unique-happy = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/unique-happy.png")
image PRG worried = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/worried.png")
image PRG worried-handsbehind = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/worried.png") #NYI
image PRG sad-2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/sad-2.png")
image PRG lactate = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/lactate.png")
image PRG lactate2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/lactate2.png")
image PRG admire = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/admire.png")
image PRG admire-2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/admire-2.png")
image PRG doubt = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/doubt.png")
image PRG insecure = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/insecure.png")
image PRG nervous = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/nervous.png")
image PRG satisfied = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/satisfied.png")
image PRG angry-2 = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/angry-2.png")
image PRG scared = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/scared.png")
image PRG grope = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/grope.png")
image PRG embarrassed = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/embarrassed.png")

image WG neutral = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/neutral.png")
image WG neutral-2 = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/neutral-2.png")
image WG happy = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/happy.png")
image WG sad = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/sad.png")
image WG surprised = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/surprised.png")
image WG surprised-2 = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/surprised-2.png")
image WG angry = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/angry.png")
image WG aroused = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/aroused.png")
image WG haughty = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/unique.png")
image WG stern = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/stern.png")
image WG doubt = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/doubt.png")
image WG worried = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/worried.png")

image side MC = "Graphics/MC/side.png"
image side BECell = ConditionSwitch("getVar('BEMode') == 'Feminine'", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/side.png"),
                                    "True", DynamicImage("Graphics/BE/[globalsize]/[BEOutfit]/side.png"))
image side WGCell = DynamicImage("Graphics/WG/[globalsize]/[WGOutfit]/side.png")
image side FMGCell = DynamicImage("Graphics/FMG/[globalsize]/[FMGOutfit]/side.png")
image side GTSCell = DynamicImage("Graphics/GTS/[globalsize]/[GTSOutfit]/side.png")
image side PRGCell = DynamicImage("Graphics/PRG/[prgsize]/[PRGOutfit]/side.png")
image side TomoCell = DynamicImage("Graphics/minor/tomoko/[minorsizes[Tomoko]]/[TomoOutfit]/side.png")
image side ChibukiCell = DynamicImage("Graphics/minor/chibuki/side.png")

#Minor characters
#If you add new sizes here, remember to update "legalsizes" in updateMinorSizes() in script.rpy

image RM neutral = "Graphics/minor/RM/neutral.png"
image RM angry = "Graphics/minor/RM/angry.png"
image RM concerned = "Graphics/minor/RM/concerned.png"
image RM concerned-2 = "Graphics/minor/RM/concerned-2.png"
image RM distrustful = "Graphics/minor/RM/distrustful.png"
image RM doubt = "Graphics/minor/RM/doubt.png"
image RM happy = "Graphics/minor/RM/happy.png"
image RM sad = "Graphics/minor/RM/sad.png"
image RM smug = "Graphics/minor/RM/smug.png"

image Yuki neutral = DynamicImage("Graphics/minor/yuki/[minorsizes[Yuki]]/neutral.png")
image Yuki happy = DynamicImage("Graphics/minor/yuki/[minorsizes[Yuki]]/happy.png")
image Yuki sad = DynamicImage("Graphics/minor/yuki/[minorsizes[Yuki]]/sad.png")
image Yuki surprised = DynamicImage("Graphics/minor/yuki/[minorsizes[Yuki]]/surprised.png")
image Yuki gossip = DynamicImage("Graphics/minor/yuki/[minorsizes[Yuki]]/gossip.png")

image HR neutral = "Graphics/minor/faculty/HR/neutral.png"
image HR annoyed = "Graphics/minor/faculty/HR/annoyed.png" #NYI
image HR unique = "Graphics/minor/faculty/HR/unique.png"

#image Hageshi neutral = "Graphics/minor/faculty/hageshi/neutral.png"
#image Hageshi angry = "Graphics/minor/faculty/hageshi/angry.png"
#image Hageshi satisfied = "Graphics/minor/faculty/hageshi/satisfied.png"

#image Takamura neutral = "Graphics/minor/faculty/takamura/neutral.png"
#image Takamura flattered = "Graphics/minor/faculty/takamura/flattered.png"
#image Takamura happy = "Graphics/minor/faculty/takamura/happy.png"
#image Takamura reassuring = "Graphics/minor/faculty/takamura/reassuring.png"
#image Takamura sad = "Graphics/minor/faculty/takamura/sad.png"
#image Takamura strict = "Graphics/minor/faculty/takamura/strict.png"

#image Tsubasa neutral = "Graphics/minor/faculty/tsubasa/neutral.png"
#image Tsubasa annoyed = "Graphics/minor/faculty/tsubasa/annoyed.png"
#image Tsubasa intrigued = "Graphics/minor/faculty/tsubasa/intrigued.png"
#image Tsubasa satisfied = "Graphics/minor/faculty/tsubasa/satisfied.png"


#legalsizes already updated, change images when bigger sprites exist
image Tomoko annoyed = DynamicImage("Graphics/minor/tomoko/[minorsizes[Tomoko]]/[TomoOutfit]/annoyed.png")
image Tomoko distracted = DynamicImage("Graphics/minor/tomoko/[minorsizes[Tomoko]]/[TomoOutfit]/distracted.png")
image Tomoko neutral = DynamicImage("Graphics/minor/tomoko/[minorsizes[Tomoko]]/[TomoOutfit]/neutral.png")
image Tomoko happy = DynamicImage("Graphics/minor/tomoko/[minorsizes[Tomoko]]/[TomoOutfit]/happy.png")
image Tomoko surprised = DynamicImage("Graphics/minor/tomoko/[minorsizes[Tomoko]]/[TomoOutfit]/surprised.png")
image Tomoko sad = DynamicImage("Graphics/minor/tomoko/[minorsizes[Tomoko]]/[TomoOutfit]/sad.png")
image Tomoko unique = DynamicImage("Graphics/minor/tomoko/[minorsizes[Tomoko]]/[TomoOutfit]/unique.png")

image Ryoko neutral = "Graphics/minor/ryoko/[RyokoOutfit]/neutral.png"
image Ryoko happy = "Graphics/minor/ryoko/[RyokoOutfit]/happy.png"
image Ryoko annoyed = "Graphics/minor/ryoko/[RyokoOutfit]/annoyed.png"
image Ryoko camera = "Graphics/minor/ryoko/[RyokoOutfit]/camera.png"
image Ryoko surprised = "Graphics/minor/ryoko/[RyokoOutfit]/surprised.png"
image Ryoko tongue = "Graphics/minor/ryoko/[RyokoOutfit]/unique.png"
image Ryoko confused = "Graphics/minor/ryoko/[RyokoOutfit]/confused.png"
image Ryoko embarrassed = "Graphics/minor/ryoko/[RyokoOutfit]/embarrassed.png"

image Minori neutral = "Graphics/minor/minori/neutral.png"
image Minori happy = "Graphics/minor/minori/happy.png"
image Minori embarrassed = "Graphics/minor/minori/embarrassed.png"
image Minori sad = "Graphics/minor/minori/sad.png"

image Sakura angry = DynamicImage("Graphics/minor/sakura/[minorsizes[Sakura]]/angry.png")
image Sakura deadpan = DynamicImage("Graphics/minor/sakura/[minorsizes[Sakura]]/deadpan.png")
image Sakura frustrated = DynamicImage("Graphics/minor/sakura/[minorsizes[Sakura]]/frustrated.png")
image Sakura neutral = DynamicImage("Graphics/minor/sakura/[minorsizes[Sakura]]/neutral.png")
image Sakura happy = DynamicImage("Graphics/minor/sakura/[minorsizes[Sakura]]/happy.png")
image Sakura nervous = DynamicImage("Graphics/minor/sakura/[minorsizes[Sakura]]/nervous.png")
image Sakura sad = DynamicImage("Graphics/minor/sakura/[minorsizes[Sakura]]/sad.png")
image Sakura sad-2 = DynamicImage("Graphics/minor/sakura/[minorsizes[Sakura]]/sad-2.png")
image Sakura surprised = DynamicImage("Graphics/minor/sakura/[minorsizes[Sakura]]/surprised.png")

image Natsuko neutral = DynamicImage("Graphics/minor/natsuko/[minorsizes[Natsuko]]/[NatsOutfit]/neutral.png")
image Natsuko annoyed = DynamicImage("Graphics/minor/natsuko/[minorsizes[Natsuko]]/[NatsOutfit]/annoyed.png")
image Natsuko angry = DynamicImage("Graphics/minor/natsuko/[minorsizes[Natsuko]]/[NatsOutfit]/angry.png")
image Natsuko disappointed = DynamicImage("Graphics/minor/natsuko/[minorsizes[Natsuko]]/[NatsOutfit]/disappointed.png")
image Natsuko smug = DynamicImage("Graphics/minor/natsuko/[minorsizes[Natsuko]]/[NatsOutfit]/smug.png")
image Natsuko flex = DynamicImage("Graphics/minor/natsuko/[minorsizes[Natsuko]]/[NatsOutfit]/flex.png")
image Natsuko happy = DynamicImage("Graphics/minor/natsuko/[minorsizes[Natsuko]]/[NatsOutfit]/happy.png")
image Natsuko flirty = DynamicImage("Graphics/minor/natsuko/[minorsizes[Natsuko]]/[NatsOutfit]/flirty.png")
image Natsuko aroused = DynamicImage("Graphics/minor/natsuko/[minorsizes[Natsuko]]/[NatsOutfit]/aroused.png")

image Tako neutral = "Graphics/minor/tako/[minorsizes[Tako]]/[TakoOutfit]/neutral.png"
image Tako angry = "Graphics/minor/tako/[minorsizes[Tako]]/[TakoOutfit]/angry.png"
image Tako excited = "Graphics/minor/tako/[minorsizes[Tako]]/[TakoOutfit]/excited.png"
image Tako happy = "Graphics/minor/tako/[minorsizes[Tako]]/[TakoOutfit]/happy.png"
image Tako unique = "Graphics/minor/tako/[minorsizes[Tako]]/[TakoOutfit]/unique.png"
image Tako sad = "Graphics/minor/tako/[minorsizes[Tako]]/[TakoOutfit]/sad.png"
image Tako confused = "Graphics/minor/tako/[minorsizes[Tako]]/[TakoOutfit]/confused.png"

image Midori neutral = "Graphics/minor/parents/midori/neutral.png"
image Midori happy = "Graphics/minor/parents/midori/happy.png"
image Midori nervous = "Graphics/minor/parents/midori/nervous.png"
image Midori pout = "Graphics/minor/parents/midori/pout.png"
image Midori sad = "Graphics/minor/parents/midori/sad.png"
image Midori surprised = "Graphics/minor/parents/midori/surprised.png"
image Midori unique = "Graphics/minor/parents/midori/unique.png"

image Yuko neutral = "Graphics/minor/parents/yuko/neutral.png"
image Yuko angry = "Graphics/minor/parents/yuko/angry.png"
image Yuko happy = "Graphics/minor/parents/yuko/happy.png"
image Yuko shrug = "Graphics/minor/parents/yuko/shrug.png"
image Yuko smug = "Graphics/minor/parents/yuko/smug.png"
image Yuko surprised = "Graphics/minor/parents/yuko/surprised.png"
image Yuko unique = "Graphics/minor/parents/yuko/unique.png"

image Kokutan neutral = "Graphics/minor/kokutan/neutral.png"
image Akihiro neutral = "Graphics/minor/parents/akihiro/neutral.png"
image Miko neutral = "Graphics/minor/parents/miko/neutral.png"

image Minami neutral = "Graphics/minor/parents/minami/neutral.png"
image Minami annoyed = "Graphics/minor/parents/minami/annoyed.png"
image Minami dark = "Graphics/minor/parents/minami/dark.png"
image Minami happy = "Graphics/minor/parents/minami/happy.png"
image Minami unique = "Graphics/minor/parents/minami/unique.png"

image Chibuki neutral = "Graphics/minor/chibuki/neutral.png"
#image Daitaro neutral = "Graphics/minor/parents/daitaro/neutral.png"

image dummy = "Graphics/ui/dummy.png"

#Overlays
image FerryTomo1 = "Graphics/minor/tomoko/1/overlays/table-overlay.png"

#Audio
define audio.AE = "Audio/BGM/scene_AE.ogg"
define audio.AEAlt = "Audio/BGM/scene_AEalt.ogg"
define audio.BE = "Audio/BGM/scene_BE.mp3"
define audio.FMG = "Audio/BGM/scene_FMG.ogg" #Pump It
define audio.GTS = "Audio/BGM/scene_GTS.ogg" #Hidden Meadow
define audio.RM = "Audio/BGM/scene_RM.ogg"
define audio.MC = "Audio/BGM/scene_MC.ogg" #Our Protagonist
define audio.MCGuitar = "Audio/BGM/scene_MCguitar.ogg"
define audio.PRG = "Audio/BGM/scene_PRG.ogg" #Quiet Wandering
define audio.PRGMusicBox = "Audio/BGM/scene_PRGMusicBox.ogg" #Quiet Wandering (Music Box)
define audio.PRGDramatic = "Audio/BGM/scene_PRGdrama.ogg" #Small Moments
define audio.PRGChallenge = "Audio/BGM/scene_PRGchallenge.ogg" #The Challenge
define audio.PRGAlt = "Audio/BGM/scene_PRG2.ogg" #Press On
define audio.WG = "Audio/BGM/scene_WG.ogg" #Aristocratic Opulence
define audio.WGAlt = "Audio/BGM/scene_WG2.ogg" #Elegant Antics
define audio.Bittersweet = "Audio/BGM/scene_bittersweet.mp3" #PH
define audio.BigChanges = "Audio/BGM/scene_uncategorized2.mp3"
define audio.BrightLights = "Audio/BGM/BrightLights.ogg" #Town Theme
define audio.Busy = "Audio/BGM/scene_busy.mp3" #PH
define audio.Chase = "Audio/BGM/Chase.ogg"
define audio.Country = "Audio/BGM/scene_country.ogg" #Country Theme
define audio.CreepingPresence = "Audio/BGM/CreepingPresence.ogg"
define audio.DayByDay = "Audio/BGM/scene_daybyday.ogg" #General Music 3
define audio.Daymenu = "Audio/BGM/menu_daymenu.ogg" #PH
define audio.Festival = "Audio/BGM/scene_festival.mp3" #PH
define audio.HallowedHalls = "Audio/BGM/hallowedhalls.ogg" #Hallowed Halls
define audio.HigherEdu = "Audio/BGM/scene_higheredu.ogg" #Higher Education (This is what Hallway is, in any scripts)
define audio.KnowMyself = "Audio/BGM/knowmyself.mp3" #Know Myself (short loop)
define audio.FullKnowMyself = "Audio/BGM/knowmyself_full.mp3" #Know Myself (full song)
define audio.Love = "Audio/BGM/love.ogg"
define audio.LoveA = "Audio/BGM/love_A.ogg"
define audio.LoveB = "Audio/BGM/love_B.ogg"
define audio.LoveC = "Audio/BGM/love_C.ogg"
define audio.LoveMB = "Audio/BGM/love_mb.ogg" #Music Box variant of Love
define audio.Memories = "Audio/BGM/memories.mp3"
define audio.Nostalgia = "Audio/BGM/nostalgia.ogg"
define audio.NostalgiaSax = "Audio/BGM/nostalgia_sax.ogg"
define audio.Peaceful = "Audio/BGM/scene_peaceful.mp3" #PH
define audio.Rain = "Audio/BGM/scene_rain.mp3" #PH
define audio.Rivalry = "Audio/BGM/rivalry.ogg"
define audio.Requiem = "Audio/BGM/requiem.mp3"
define audio.Romance = "Audio/BGM/scene_tbi.ogg" #NEED
define audio.Schoolday = "Audio/BGM/scene_schoolday.mp3" #PH
define audio.Secret = "Audio/BGM/scene_secret.ogg" #A Secret Place
define audio.Steamy = "Audio/BGM/scene_tbi.ogg" #NEED
define audio.Sunset = "Audio/BGM/scene_sunset.mp3"
define audio.Tension = "Audio/BGM/tension.ogg" #A Tense Moment
define audio.TremblingWhispers = "Audio/BGM/tremblingWhispers.ogg"
define audio.TwilightBright = "Audio/BGM/twilightBright.ogg"
define audio.TwilightAmbient = "Audio/BGM/twilightAmbient.ogg"

define audio.BrandenburgNo4 = "Audio/BGM/brandenburgno4.mp3"
define audio.Gymnopedie = "Audio/BGM/gymnopedie.mp3"
define audio.Pastorale = "Audio/BGM/Pastorale.ogg"
define audio.SimpleSonata = "Audio/BGM/SimpleSonata.ogg"
define audio.MinuetG = "Audio/BGM/MinuetG.ogg"
define audio.MoonlightSonata = "Audio/BGM/moonlightsonata.mp3"
define audio.AgnusDeiX = "Audio/BGM/agnusdeix.mp3"
define audio.AngelsWeep = "Audio/BGM/angelsweep.mp3"
define audio.BachGavottes = "Audio/BGM/Bach_Gavottes.mp3"
define audio.ConcertinoTeleman = "Audio/BGM/Concertino_Teleman.mp3"
define audio.InvitationCastleBall = "Audio/BGM/InvitationCastle_Doug.mp3"
define audio.BaroqueCoffeeHouse = "Audio/BGM/BaroqueCoffee_Doug.mp3"

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
    eventlibrary['MC001'] = {"name": "Sharpening the Senses", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                      "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": [[ConditionEnum.NOEVENT, "global005"]]}
    eventlibrary['MC002'] = {"name": "Warmth of a Heart", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                      "location": "classroom",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": [[ConditionEnum.EVENT, "MC001"]]}
    eventlibrary['MC003'] = {"name": "Will She Ever Grow up?", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                      "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["size2"],          "conditions": [[ConditionEnum.EVENT, "global005"]]}
    eventlibrary['MC006'] = {"name": "A Bad Handoff", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                               "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": ["XX20"],      "conditions": [[ConditionEnum.TIMEFLAG, "aftersize2"]]}
    eventlibrary['MC007'] = {"name": "Conspiracies with a Side of Cupcakes", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,   "location": "unknown",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],                "conditions": [[ConditionEnum.AND, [ConditionEnum.NOEVENT, "FMG010"], [ConditionEnum.FLAG, "XX15"]]]}
    eventlibrary['MC008'] = {"name": "Keisuke End", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                                "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": [[ConditionEnum.EVENT, "MC006"]]}

    eventlibrary['global005'] = {"name": "And the Results Are In", "girls": [], "type": EventTypeEnum.OPTIONALCORE,        "location": "auditorium",    "priority": PrioEnum.ALL, "next": "", "obsflags": [],           "conditions": [[ConditionEnum.TIMEFLAG, "testday"]]}
    eventlibrary['RM001'] = {"name": "Getting to Know Your Roommate", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,  "location": "dorminterior",  "priority": PrioEnum.NONE, "next": "", "obsflags": [],          "conditions": [[ConditionEnum.EVENT, "MC001"]]}
    eventlibrary['RM002'] = {"name": "You and Yuki", "girls": ["minor"], "type": EventTypeEnum.OPTIONAL,                   "location": "hallway",       "priority": PrioEnum.NONE, "next": "", "obsflags": ["size5"],          "conditions": [[ConditionEnum.EVENT, "RM001"]]}

    #Causes minor character scenes to be disabled if time is between the first and second time in a tuple
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
    eventlibrary['AE021'] = {"name": "Prelude for Choir", "girls": ["AE", "WG", "PRG"], "type": EventTypeEnum.CORE,            "location": "classroom",        "priority": PrioEnum.NONE, "sp": 4,     "next": "AE022", "obsflags": [],                "conditions": []}
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
    eventlibrary['AE053'] = {"name": "Dressed to Impress", "girls": ["AE", "WG"], "type": EventTypeEnum.CORE,                  "location": "town",             "priority": PrioEnum.NONE, "sp": 10,    "next": "AE054", "obsflags": [],                "conditions": []}
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
    eventlibrary['AE071'] = {"name": "Poco Adagio", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "hallway",          "priority": PrioEnum.NONE, "sp": 14,    "next": "AE072", "obsflags": [],                "conditions": []}
    eventlibrary['AE072'] = {"name": "Waltz of the Snowflakes", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "frozenbeach",      "priority": PrioEnum.NONE, "sp": 14,    "next": "AE073", "obsflags": [],                "conditions": []}
    eventlibrary['AE073'] = {"name": "Stichera No. 1", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "hallway",          "priority": PrioEnum.NONE, "sp": 14,    "next": "AE074", "obsflags": [],                "conditions": []}
    eventlibrary['AE074'] = {"name": "The Snow is Dancing", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "field",            "priority": PrioEnum.NONE, "sp": 14,    "next": "AE075", "obsflags": [],                "conditions": []}
    eventlibrary['AE075'] = {"name": "Des Pas Sur la Neige", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 15,    "next": "AE076", "obsflags": [],                "conditions": []}
    eventlibrary['AE076'] = {"name": "Stand by Me", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "hallway",          "priority": PrioEnum.NONE, "sp": 15,    "next": "AE077", "obsflags": [],                "conditions": []}
    eventlibrary['AE077'] = {"name": "Pas de Deux", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "hallway",          "priority": PrioEnum.NONE, "sp": 15,    "next": "AE078", "obsflags": [],                "conditions": []}
    eventlibrary['AE078'] = {"name": "Méditation", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "hallway",          "priority": PrioEnum.ALL, "sp": 15,       "next": "AE079", "obsflags": [],                "conditions": []}
    eventlibrary['AE079'] = {"name": "Metamorphosis", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "dorminterior",      "priority": PrioEnum.ALL, "sp": 15,       "next": "AE080", "obsflags": [],                "conditions": []}
    eventlibrary['AE080'] = {"name": "Pavane for Dead Princess", "girls": ["AE"], "type": EventTypeEnum.CORE,                  "location": "dormtomoko",      "priority": PrioEnum.ALL, "sp": 15,       "next": "AE081", "obsflags": [],                "conditions": []}
    eventlibrary['AE081'] = {"name": "Arabesque No. 1", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "classroom",      "priority": PrioEnum.ALL, "sp": 15,       "next": "AE082", "obsflags": [],                "conditions": []}
    eventlibrary['AE082'] = {"name": "Emperor", "girls": ["AE"], "type": EventTypeEnum.CORE,                                    "location": "hallway",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE083", "obsflags": [],                "conditions": []}
    eventlibrary['AE083'] = {"name": "Gnossienne No.1", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "hallway",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE084", "obsflags": [],                "conditions": []}
    eventlibrary['AE084'] = {"name": "Ave Verum Corpus", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "classroom",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE085", "obsflags": [],                "conditions": []}
    eventlibrary['AE085'] = {"name": "Verklärte Nacht", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "clocktower",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE086", "obsflags": [],                "conditions": []}
    eventlibrary['AE086'] = {"name": "Washington Post March", "girls": ["AE"], "type": EventTypeEnum.CORE,                      "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE087", "obsflags": [],                "conditions": []}
    eventlibrary['AE087'] = {"name": "Romantic Pieces", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE088", "obsflags": [],                "conditions": []}
    eventlibrary['AE088'] = {"name": "Raymonda", "girls": ["AE"], "type": EventTypeEnum.CORE,                                   "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE089", "obsflags": [],                "conditions": []}
    eventlibrary['AE089'] = {"name": "Corilan Overture", "girls": ["AE"], "type": EventTypeEnum.CORE,                            "location": "dormAE",          "priority": PrioEnum.NONE, "sp": 15,       "next": "AE090", "obsflags": [],                "conditions": []}
    eventlibrary['AE090'] = {"name": "Adagio for Strings", "girls": ["AE"], "type": EventTypeEnum.CORE,                         "location": "classroom",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE091", "obsflags": [],                "conditions": []}
    eventlibrary['AE091'] = {"name": "4'33\"", "girls": ["AE"], "type": EventTypeEnum.CORE,                                   "location": "classroom",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE092", "obsflags": [],                "conditions": []}
    eventlibrary['AE092'] = {"name": "Det er det skønneste jeg ved", "girls": ["AE"], "type": EventTypeEnum.CORE,             "location": "dormhallway",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE093", "obsflags": [],                "conditions": []}
    eventlibrary['AE093'] = {"name": "Symphony No. 9", "girls": ["AE"], "type": EventTypeEnum.CORE,                         "location": "hallway",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE094", "obsflags": [],                "conditions": []}
    eventlibrary['AE094'] = {"name": "Pensée des Morts", "girls": ["AE"], "type": EventTypeEnum.CORE,                       "location": "dormhallway",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE095", "obsflags": [],                "conditions": []}
    eventlibrary['AE095'] = {"name": "Mars, Bringer of War", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "cafeteria",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE096", "obsflags": [],                "conditions": []}
    eventlibrary['AE096'] = {"name": "Sigfried's Funeral March", "girls": ["AE"], "type": EventTypeEnum.CORE,             "location": "roof",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE097", "obsflags": [],                "conditions": []}
    eventlibrary['AE097'] = {"name": "Silence", "girls": ["AE"], "type": EventTypeEnum.CORE,                                  "location": "dorminterior",      "priority": PrioEnum.ALL, "sp": 15,       "next": "AE098", "obsflags": [],                "conditions": []}
    eventlibrary['AE098'] = {"name": "Give Me Novacaine", "girls": ["AE"], "type": EventTypeEnum.CORE,                        "location": "dormAE",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE099", "obsflags": [],                "conditions": []}
    eventlibrary['AE099'] = {"name": "Tannhäuser Overture", "girls": ["AE"], "type": EventTypeEnum.CORE,                    "location": "dormAE",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE100", "obsflags": [],                "conditions": []}
    eventlibrary['AE100'] = {"name": "Jupiter, The Bringer Of Jollity", "girls": ["AE"], "type": EventTypeEnum.CORE,        "location": "schoolfront",      "priority": PrioEnum.NONE, "sp": 15,       "next": "AE101", "obsflags": [],                "conditions": []}
    eventlibrary['AE101'] = {"name": "Shiori End", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "dormexterior",     "priority": PrioEnum.NONE,              "next": "", "obsflags": [],                     "conditions": []}

    eventlibrary['AE007b'] = {"name": "Peer Gynt", "girls": ["AE"], "type": EventTypeEnum.CORE,                                 "location": "hallway",          "priority": PrioEnum.NONE, "sp": 1,    "next": "AE008b", "obsflags": [],                "conditions": []}
    eventlibrary['AE008b'] = {"name": "Made of Stone", "girls": ["AE"], "type": EventTypeEnum.CORE,                             "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 1,    "next": "AE009b", "obsflags": [],                "conditions": []}
    eventlibrary['AE009b'] = {"name": "Jardins sous la Pluie", "girls": ["AE"], "type": EventTypeEnum.CORE,                     "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 1,    "next": "AE011b", "obsflags": [],                "conditions": []}
    eventlibrary['AE011b'] = {"name": "Symphony No. 92 in G Major", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 3,    "next": "", "obsflags": [],                     "conditions": []}
    eventlibrary['AE015b'] = {"name": "Symphony No. 92 in G Major", "girls": ["AE"], "type": EventTypeEnum.CORE,                "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 3,    "next": "", "obsflags": [],                     "conditions": []}
    eventlibrary['AE016b'] = {"name": "Shiori End", "girls": ["AE"], "type": EventTypeEnum.CORE,                                "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,    "next": "", "obsflags": [],                     "conditions": []}

    #Optional
    eventlibrary['AE005'] = {"name": "Confirmation", "girls": ["AE"], "type": EventTypeEnum.OPTIONALCORE,                       "location": "office",          "priority": PrioEnum.NONE, "sp": 1,     "obsflags": ["aftertest"],                      "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['AE010'] = {"name": "Blue Danube", "girls": ["AE"], "type": EventTypeEnum.OPTIONALCORE,                        "location": "office",           "priority": PrioEnum.NONE, "sp": 2,     "obsflags": ["aftersize2"],                     "conditions": [[ConditionEnum.TIMEFLAG, "size2"], [ConditionEnum.FLAG, "AE006_helpinginoffice"]]}

    eventlibrary['AEBE004'] = {"name": "Kâtibim", "girls": ["AE", "BE"], "type": EventTypeEnum.OPTIONALCORE,                        "location": "festival",           "priority": PrioEnum.NONE, "sp": 4,     "obsflags": ["size5"],                     "conditions": [[ConditionEnum.TIMEFLAG, "size4"]]}


    #Core
    eventlibrary['BE001'] = {"name": "Rooftop Reunion", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "roof",             "priority": PrioEnum.NONE, "sp": 0,     "next": "BE003", "obsflags": ["testday"],         "conditions": []}
    eventlibrary['BE002'] = {"name": "Campus Collision", "girls": ["BE"], "type": EventTypeEnum.CORE,                                   "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 0,     "next": "BE003", "obsflags": ["testday"],         "conditions": []}
    eventlibrary['BE003'] = {"name": "Cool Drinks with Honoka", "girls": ["BE"], "type": EventTypeEnum.CORE,                            "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 0,     "next": "BE004", "obsflags": [],                  "conditions": []}
    eventlibrary['BE004'] = {"name": "Chatting at Soccer Practice", "girls": ["BE"], "type": EventTypeEnum.CORE,                        "location": "track",            "priority": PrioEnum.NONE, "sp": 0,     "next": "BE006", "obsflags": [],                  "conditions": []}
    eventlibrary['BE006'] = {"name": "Meetings and Partings", "girls": ["BE"], "type": EventTypeEnum.CORE,                             "location": "hallway",        "priority": PrioEnum.NONE, "sp": 0,     "next": "BE007", "obsflags": [],                  "conditions": []}
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
    eventlibrary['BE022'] = {"name": "A Sneaky Lunch", "girls": ["BE", "WG"], "type": EventTypeEnum.CORE,                              "location": "library",          "priority": PrioEnum.NONE, "sp": 4,     "next": "BE023", "obsflags": [],                  "conditions": []}
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
    eventlibrary['BE034'] = {"name": "No More Archery", "girls": ["BE"], "type": EventTypeEnum.CORE,                                    "location": "field",            "priority": PrioEnum.NONE, "sp": 6,     "next": "BE035A", "obsflags": [],                 "conditions": []}
    eventlibrary['BE035A'] = {"name": "Just Add Butter", "girls": ["BE"], "type": EventTypeEnum.CORE,                                "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,     "next": "BE036", "obsflags": [],                  "conditions": []}
    eventlibrary['BE035B'] = {"name": "Pop Flies", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "track",            "priority": PrioEnum.NONE, "sp": 7,     "next": "BE036", "obsflags": [],                  "conditions": []}
    eventlibrary['BE036'] = {"name": "Flower Gazing", "girls": ["BE", "GTS"], "type": EventTypeEnum.CORE,                               "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 7,     "next": "BE037", "obsflags": [],                  "conditions": []}
    eventlibrary['BE037'] = {"name": "Dock Musing", "girls": ["BE"], "type": EventTypeEnum.CORE,                                        "location": "hillroad",         "priority": PrioEnum.NONE, "sp": 7,     "next": "BE038A", "obsflags": [],                 "conditions": []}
    eventlibrary['BE038A'] = {"name": "Cooking Club Scene 2", "girls": ["BE"], "type": EventTypeEnum.CORE,                               "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,     "next": "BE039", "obsflags": [],                  "conditions": []}
    eventlibrary['BE038B'] = {"name": "Based", "girls": ["BE"], "type": EventTypeEnum.CORE,                              "location": "baseballfield",    "priority": PrioEnum.NONE, "sp": 7,     "next": "BE039", "obsflags": [],                  "conditions": []}
    eventlibrary['BE039'] = {"name": "Honoka's Roommate", "girls": ["BE"], "type": EventTypeEnum.CORE,                                  "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "BE041A", "obsflags": [],                  "conditions": []}
    eventlibrary['BE041A'] = {"name": "Cooking Club Scene 3", "girls": ["BE"], "type": EventTypeEnum.CORE,                          "location": "cookingclassroom",     "priority": PrioEnum.NONE, "sp": 7,     "next": "BE042", "obsflags": [],                  "conditions": []}
    eventlibrary['BE041B'] = {"name": "Leaving the Softball Club", "girls": ["BE"], "type": EventTypeEnum.CORE,                         "location": "track",     "priority": PrioEnum.NONE, "sp": 7,     "next": "BE042", "obsflags": [],                  "conditions": []}
    eventlibrary['BE042'] = {"name": "Anything but Yellow Polka Dot", "girls": ["BE"], "type": EventTypeEnum.CORE,                     "location": "hallway",            "priority": PrioEnum.NONE, "sp": 7,     "next": "BE043", "obsflags": [],                  "conditions": []}
    eventlibrary['BE043'] = {"name": "(Insert Movie Here)", "girls": ["BE"], "type": EventTypeEnum.CORE,                             "location": "dorminterior",            "priority": PrioEnum.NONE, "sp": 7,     "next": "BE044", "obsflags": [],                  "conditions": []}
    eventlibrary['BE044'] = {"name": "Beach Day", "girls": ["BE"], "type": EventTypeEnum.CORE,                                       "location": "schoolfront",            "priority": PrioEnum.NONE, "sp": 7,     "next": "BE045", "obsflags": [],                  "conditions": []}
    eventlibrary['BE045'] = {"name": "Honoka end", "girls": ["BE"], "type": EventTypeEnum.CORE,                                         "location": "classroom",        "priority": PrioEnum.NONE,              "next": "", "obsflags": [],                       "conditions": []}

    #Optional
    eventlibrary['BE005'] = {"name": "Possible Clubs", "girls": ["BE"], "type": EventTypeEnum.OPTIONALCORE,                             "location": "classroom",        "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],                        "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['BE010'] = {"name": "Surprise, Honoka's Boobs are Bigger", "girls": ["BE"], "type": EventTypeEnum.OPTIONALCORE,        "location": "dorminterior",     "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": ["aftersize2"],                       "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['BE013'] = {"name": "Recovering from a Defeat", "girls": ["BE"], "type": EventTypeEnum.OPTIONALCORE,                   "location": "arcade",           "priority": PrioEnum.ALL,               "obsflags": [],                                   "conditions": [[ConditionEnum.FLAG, "BE013_unlock"]]}

    eventlibrary['BEGTS001'] = {"name": "You Make Me Feel Like a Woman", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,        "location": "dormexterior",     "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.VAR, "BEMode", "Feminine"], [ConditionEnum.EVENT, "BE020"]]}
    eventlibrary['BEGTS002'] = {"name": "Shining Down", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,                         "location": "dormexterior",     "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.EVENT, "BEGTS001"]]}
    eventlibrary['BEGTS003'] = {"name": "A Haze of Judgement", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,                  "location": "dormexterior",     "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.EVENT, "BEGTS002"]]}
    eventlibrary['BEGTS004'] = {"name": "Boiling Point", "girls": ["BE", "GTS"], "type": EventTypeEnum.OPTIONAL,                        "location": "hallway",          "priority": PrioEnum.NONE,               "obsflags": [],                                   "conditions": [[ConditionEnum.EVENT, "BEGTS003"]]}

    #Core
    eventlibrary['FMG001'] = {"name": "Tower of Athletics", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                      "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG002", "obsflags": ["testday"],      "conditions": []}
    eventlibrary['FMG002'] = {"name": "Nerd Alert", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                               "location": "hallway",                      "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG003", "obsflags": [],               "conditions": []}
    eventlibrary['FMG003'] = {"name": "The Agreement", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "library",                  "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG004", "obsflags": [],               "conditions": []}
    eventlibrary['FMG004'] = {"name": "First Time?", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "gym",                    "priority": PrioEnum.NONE, "sp": 0,     "next": "FMG007", "obsflags": [],            "conditions": []}
    eventlibrary['FMG007'] = {"name": "Lunch and Hobbies", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "cafeteria",                "priority": PrioEnum.NONE, "sp": 1,     "next": "FMG008", "obsflags": [],               "conditions": []}
    eventlibrary['FMG008'] = {"name": "Everything Hurts", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "dormexterior",             "priority": PrioEnum.NONE, "sp": 1,     "next": "FMG009", "obsflags": [],               "conditions": []}
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
    eventlibrary['FMG023'] = {"name": "The Wizard on the Sidewalk", "girls": ["FMG", "GTS"], "type": EventTypeEnum.CORE,                        "location": "town",                     "priority": PrioEnum.NONE, "sp": 4,     "next": "FMG026", "obsflags": [],               "conditions": []}
    #eventlibrary['FMG024'] = {"name": "Arcade Run-in", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "arcade",                   "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG026", "obsflags": [],               "conditions": []} Commenting this out until actual FMG024 is written
    eventlibrary['FMG026'] = {"name": "Arcade Run-in", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "woods",                   "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG027", "obsflags": [],               "conditions": []}
    eventlibrary['FMG027'] = {"name": "Study Date", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                               "location": "classroom",                "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG028", "obsflags": [],               "conditions": []}
    eventlibrary['FMG028'] = {"name": "Anything but Golf", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG029", "obsflags": [],               "conditions": []}
    eventlibrary['FMG029'] = {"name": "Man, These Waffles Suck", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 5,     "next": "FMG030", "obsflags": [],               "conditions": []}
    eventlibrary['FMG030'] = {"name": "Oki", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                      "location": "dormexterior",             "priority": PrioEnum.NONE, "sp": 6,     "next": "FMG031", "obsflags": [],               "conditions": []}
    eventlibrary['FMG031'] = {"name": "What's Your Drive?", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "lockers",                  "priority": PrioEnum.NONE, "sp": 6,     "next": "FMG032", "obsflags": [],               "conditions": []}
    eventlibrary['FMG032'] = {"name": "Chumby the Cat", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                           "location": "pool",                     "priority": PrioEnum.NONE, "sp": 6,     "next": "FMG033", "obsflags": [],               "conditions": []}
    eventlibrary['FMG033'] = {"name": "Dress Malfunction", "girls": ["FMG", "WG"], "type": EventTypeEnum.CORE,                                 "location": "classroom",                "priority": PrioEnum.NONE, "sp": 6,     "next": "FMG034", "obsflags": [],               "conditions": []}
    eventlibrary['FMG034'] = {"name": "That's a Huge Bitch!", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                    "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 6,     "next": "FMG037", "obsflags": [],               "conditions": []}
    eventlibrary['FMG035'] = {"name": "Getting Out Of Hand", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                     "location": "gym",                  "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG038", "obsflags": [],               "conditions": []} #tmp
    eventlibrary['FMG037'] = {"name": "Getting Out Of Hand", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "gym",                   "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG038", "obsflags": [],               "conditions": []} #tmp
    eventlibrary['FMG038'] = {"name": "Yokai", "girls": ["FMG", "AE"], "type": EventTypeEnum.CORE,                                              "location": "dorminterior",             "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG039", "obsflags": [],               "conditions": []}
    eventlibrary['FMG039'] = {"name": "Down with the Sickness", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                   "location": "nurseoffice",              "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG040", "obsflags": [],               "conditions": []}
    eventlibrary['FMG040'] = {"name": "Summer Love", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG041", "obsflags": [],               "conditions": []}
    eventlibrary['FMG041'] = {"name": "Lose Yourself", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                            "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG042", "obsflags": [],               "conditions": []}
    eventlibrary['FMG042'] = {"name": "Gamer Moment", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                             "location": "dormFMG",                  "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG043", "obsflags": [],               "conditions": []}
    eventlibrary['FMG043'] = {"name": "She Will Be Loved", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "dormFMG",                  "priority": PrioEnum.NONE, "sp": 7,     "next": "FMG044", "obsflags": [],               "conditions": []}
    eventlibrary['FMG044'] = {"name": "Shower Time", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "lockers",                  "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG045", "obsflags": [],               "conditions": []}
    eventlibrary['FMG045'] = {"name": "The Birds and the Bees", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                   "location": "dorminterior",             "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG046", "obsflags": [],               "conditions": []}
    eventlibrary['FMG046'] = {"name": "The Wonders of Cooking", "girls": ["FMG", "PRG"], "type": EventTypeEnum.CORE,                            "location": "cookingclassroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG047", "obsflags": [],               "conditions": []}
    eventlibrary['FMG047'] = {"name": "Kitchen Nightmare", "girls": ["FMG", "PRG"], "type": EventTypeEnum.CORE,                                 "location": "campuscenter",             "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG048", "obsflags": [],               "conditions": []}
    eventlibrary['FMG048'] = {"name": "What a Twist", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "cafeteria",                "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG049", "obsflags": [],               "conditions": []}
    eventlibrary['FMG049'] = {"name": "Love Hurts", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                              "location": "dorminterior",                "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG050", "obsflags": [],               "conditions": []}
    eventlibrary['FMG050'] = {"name": "What's Good, Shorty?", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                      "location": "dormFMG",                "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG051", "obsflags": [],               "conditions": []}
    eventlibrary['FMG051'] = {"name": "Das a Big Rock", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                           "location": "lockers",                "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG052", "obsflags": [],               "conditions": []}
    eventlibrary['FMG052'] = {"name": "Got That Fresh Fit", "girls": ["FMG", "WG"], "type": EventTypeEnum.CORE,                                  "location": "track",                "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG053", "obsflags": [],               "conditions": []}
    eventlibrary['FMG053'] = {"name": "League of Ancients", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                          "location": "classroom",            "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG054", "obsflags": [],               "conditions": []}
    eventlibrary['FMG054'] = {"name": "The Yang", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                  "location": "gym",                     "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG055", "obsflags": [],               "conditions": []}
    eventlibrary['FMG055'] = {"name": "She Wears Nice Clothes?", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                  "location": "supermarket",                "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG056", "obsflags": [],               "conditions": []}
    eventlibrary['FMG056'] = {"name": "Clash of the Titans", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                     "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG057", "obsflags": [],               "conditions": []}
    eventlibrary['FMG057'] = {"name": "It's Fine, Don't Move", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                     "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG058", "obsflags": [],               "conditions": []}
    eventlibrary['FMG058'] = {"name": "Pose For The Fans", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                     "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG059", "obsflags": [],               "conditions": []}
    eventlibrary['FMG059'] = {"name": "Muscles Too Huge", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "gym",                     "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG060", "obsflags": [],               "conditions": []}
    eventlibrary['FMG060'] = {"name": "The Truth Revealed", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "roof",                     "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG061", "obsflags": [],               "conditions": []}
    eventlibrary['FMG061'] = {"name": "A Day To Relax", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                       "location": "dormFMG",                     "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG062", "obsflags": [],               "conditions": []}
    eventlibrary['FMG062'] = {"name": "Big Booty Bitches?", "girls": ["FMG", "AE"], "type": EventTypeEnum.CORE,                            "location": "gym",                     "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG063", "obsflags": [],               "conditions": []}
    eventlibrary['FMG063'] = {"name": "A Tough Choice", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                        "location": "gym",                     "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG064", "obsflags": [],               "conditions": []}
    eventlibrary['FMG064'] = {"name": "I Hate Sand", "girls": ["FMG", "PRG"], "type": EventTypeEnum.CORE,                                        "location": "cookingclassroom",    "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG065", "obsflags": [],               "conditions": []}
    eventlibrary['FMG065'] = {"name": "Belly and Abs", "girls": ["FMG", "PRG"], "type": EventTypeEnum.CORE,                                        "location": "beach",          "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG066", "obsflags": [],               "conditions": []}
    eventlibrary['FMG066'] = {"name": "Altitude Apprehension", "girls": ["FMG", "WG"], "type": EventTypeEnum.CORE,                          "location": "airport",               "priority": PrioEnum.NONE, "sp": 8,     "next": "FMG067", "obsflags": [],               "conditions": []}
    eventlibrary['FMG067'] = {"name": "Akira End", "girls": ["FMG"], "type": EventTypeEnum.CORE,                                                "location": "hallway",               "priority": PrioEnum.NONE, "sp": 8,     "next": "", "obsflags": [],               "conditions": []}

    #Optional
    eventlibrary['FMG005'] = {"name": "Despair in the Hallway", "girls": ["FMG"], "type": EventTypeEnum.OPTIONALCORE,                           "location": "hallway",                  "priority": PrioEnum.NONE, "sp": 1,     "obsflags": ["aftertest"],                      "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['FMG006'] = {"name": "Crying Over Spilled Milk", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                             "location": "gym",                      "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG010'] = {"name": "The Bigger They Are...", "girls": ["FMG"], "type": EventTypeEnum.OPTIONALCORE,                           "location": "dormexterior",             "priority": PrioEnum.NONE, "sp": 2,     "obsflags": ["aftersize2"],                     "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['FMG011'] = {"name": "Press A to Start", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                              "location": "dormexterior",             "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.EVENT, "FMG001"]]}
    eventlibrary['FMG012'] = {"name": "Rubbing One Out", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                      "location": "gym",                      "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.FLAG, "FMG_workout"]]}
    eventlibrary['FMG013'] = {"name": "Head Strong", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                          "location": "gym",                      "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.EVENT, "FMG012"]]}
    eventlibrary['FMGOPT016'] = {"name": "Fate at the Café", "girls": ["FMG"], "type": EventTypeEnum.OPTIONALCORE,                           "location": "schoolplanter",            "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.EVENT, "FMG001"]]}
    eventlibrary['FMG025'] = {"name": "Disco Queen", "girls": ["FMG"], "type": EventTypeEnum.OPTIONAL,                                          "location": "track",                    "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.EVENT, "FMG028"]]}
    eventlibrary['FMGWG001'] = {"name": "Conspiracies with a Side of Cupcakes", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,       "location": "town",                     "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "FMG010"], [ConditionEnum.FLAG, "XX15"]]]}
    eventlibrary['FMGWG002'] = {"name": "Built like a Gorilla", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                       "location": "hallway",                  "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.EVENT, "FMG033"]]}
    eventlibrary['FMGWG003'] = {"name": "Horā Eiga", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                                   "location": "hallway",                  "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "FMGWG002"], [ConditionEnum.EVENT, "FMG038"]]]}
    eventlibrary['FMGWG004'] = {"name": "An Unstoppable Force", "girls": ["FMG", "WG"], "type": EventTypeEnum.OPTIONAL,                        "location": "schoolexterior",           "priority": PrioEnum.NONE,              "obsflags": [],                                 "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "FMGWG003"], [ConditionEnum.EVENT, "FMG064"]]]}

    #Core
    eventlibrary['GTS001'] = {"name": "Girl in the Garden", "girls": ["GTS"], "type": EventTypeEnum.CORE,                  "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 0,          "next": "GTS002", "obsflags": [],       "conditions": []}
    eventlibrary['GTS002'] = {"name": "Planting Seeds", "girls": ["GTS"], "type": EventTypeEnum.CORE,                      "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 0,          "next": "GTS004", "obsflags": [],       "conditions": []}
    eventlibrary['GTS004'] = {"name": "Study Buddy", "girls": ["GTS"], "type": EventTypeEnum.CORE,                         "location": "library",          "priority": PrioEnum.NONE, "sp":0,                 "next": "GTS006","obsflags": [],        "conditions": []}
    eventlibrary['GTS006'] = {"name": "Puppy Love", "girls": ["GTS"], "type": EventTypeEnum.CORE,                          "location": "schoolfront",      "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS007", "obsflags": [],       "conditions": []}
    eventlibrary['GTS007'] = {"name": "Far From Home", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS008", "obsflags": [],       "conditions": []}
    eventlibrary['GTS008'] = {"name": "Secret Garden", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "roof",             "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS009", "obsflags": [],       "conditions": []}
    eventlibrary['GTS009'] = {"name": "A Tree Between Mountains", "girls": ["GTS", "BE"], "type": EventTypeEnum.CORE,      "location": "town",             "priority": PrioEnum.NONE, "sp": 1,          "next": "GTS011b", "obsflags": [],      "conditions": []}
    eventlibrary['GTS011'] = {"name": "The Director", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS014", "obsflags": [],       "conditions": [[ConditionEnum.FLAG, "GTS011_unlock"]]}
    eventlibrary['GTS011b'] = {"name": "The Director", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS014", "obsflags": [],       "conditions": [[ConditionEnum.NOFLAG, "GTS011_unlock"]]}
    eventlibrary['GTS013'] = {"name": "The Craft of Confection", "girls": ["GTS"], "type": EventTypeEnum.CORE,             "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 2,          "next": "GTS015", "obsflags": [],       "conditions": []}
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
    eventlibrary['GTS026'] = {"name": "Rain Upon the Iris", "girls": ["GTS"], "type": EventTypeEnum.CORE,                  "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS027", "obsflags": [],       "conditions": []}
    eventlibrary['GTS027'] = {"name": "Knock on Wood", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "roof",             "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS029", "obsflags": [],       "conditions": []}
    eventlibrary['GTS028S'] = {"name": "Don't Fear the Rebate", "girls": ["GTS"], "type": EventTypeEnum.CORE,              "location": "town",              "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS029", "obsflags": [],       "conditions": [[ConditionEnum.FLAG, "GTS015_shopping"]]}
    eventlibrary['GTS028T'] = {"name": "Art of Film", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS029", "obsflags": [],       "conditions": [[ConditionEnum.FLAG, "GTS015_movie"]]}
    eventlibrary['GTS029'] = {"name": "Growing Pains", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 5,          "next": "GTS030", "obsflags": [],       "conditions": []}
    eventlibrary['GTS030'] = {"name": "A Change in Scenery", "girls": ["GTS"], "type": EventTypeEnum.CORE,                 "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 6,          "next": "GTS031", "obsflags": [],       "conditions": []}
    eventlibrary['GTS031'] = {"name": "Settling In", "girls": ["GTS"], "type": EventTypeEnum.CORE,                         "location": "giantdorminterior","priority": PrioEnum.NONE, "sp": 6,          "next": "GTS032", "obsflags": [],       "conditions": []}
    eventlibrary['GTS032'] = {"name": "Journey of a Thousand Miles", "girls": ["GTS"], "type": EventTypeEnum.CORE,         "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 6,          "next": "GTS034", "obsflags": [],       "conditions": []}
    eventlibrary['GTS034'] = {"name": "A Tall Order", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 6,          "next": "GTS035", "obsflags": [],       "conditions": []}
    eventlibrary['GTS035'] = {"name": "First Impressions", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS036", "obsflags": [],       "conditions": []}
    eventlibrary['GTS036'] = {"name": "Worth 1000 Words", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS037", "obsflags": [],       "conditions": []}
    eventlibrary['GTS037'] = {"name": "Peak Interest", "girls": ["GTS"], "type": EventTypeEnum.CORE,                       "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS039", "obsflags": [],       "conditions": []}
    #eventlibrary['GTS038'] = {"name": "Balance", "girls": ["GTS"], "type": EventTypeEnum.CORE,                             "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS039", "obsflags": [],       "conditions": []} #intended duplicate, temporary until actual gts038 exists
    eventlibrary['GTS039'] = {"name": "Balance", "girls": ["GTS"], "type": EventTypeEnum.CORE,                             "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS040", "obsflags": [],       "conditions": []}
    eventlibrary['GTS040'] = {"name": "Mukashi, Mukashi", "girls": ["GTS"], "type": EventTypeEnum.CORE,                   "location": "dorminterior",          "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS041", "obsflags": [],       "conditions": []}
    eventlibrary['GTS041'] = {"name": "The City in the Hills", "girls": ["GTS"], "type": EventTypeEnum.CORE,               "location": "giantdorminterior", "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS042", "obsflags": [],       "conditions": []}
    eventlibrary['GTS042'] = {"name": "It Will Whisper Your Name", "girls": ["GTS"], "type": EventTypeEnum.CORE,           "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS043", "obsflags": [],       "conditions": []}
    eventlibrary['GTS043'] = {"name": "Powerhouse", "girls": ["GTS", "FMG"], "type": EventTypeEnum.CORE,                   "location": "hallway",          "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS044", "obsflags": [],       "conditions": []}
    eventlibrary['GTS044'] = {"name": "Spéirghealach", "girls": ["GTS"], "type": EventTypeEnum.CORE,                        "location": "classroom",        "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS045", "obsflags": [],       "conditions": []}
    eventlibrary['GTS045'] = {"name": "A Legacy to Protect", "girls": ["GTS"], "type": EventTypeEnum.CORE,                 "location": "dormexterior",        "priority": PrioEnum.NONE, "sp": 7,          "next": "GTS046", "obsflags": [],       "conditions": []}
    eventlibrary['GTS046'] = {"name": "The Harder She Falls", "girls": ["GTS"], "type": EventTypeEnum.CORE,                 "location": "giantdorminterior",  "priority": PrioEnum.ALL, "sp": 7,          "next": "GTS047", "obsflags": [],       "conditions": []}
    eventlibrary['GTS047'] = {"name": "Naomi end", "girls": ["GTS"], "type": EventTypeEnum.CORE,                           "location": "library",          "priority": PrioEnum.NONE,                   "next": "", "obsflags": [],             "conditions": []}

    #Optional
    eventlibrary['GTS003'] = {"name": "Itadakimasu", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                     "location": "cafeteria",        "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": [[ConditionEnum.EVENT, "GTS001"]]}
    eventlibrary['GTS012'] = {"name": "Tea?", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                            "location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": [[ConditionEnum.EVENT, "GTS011"]]}
    eventlibrary['GTS016'] = {"name": "To Bee or not to Bee", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,            "location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": [[ConditionEnum.EVENT, "GTS001"]]}
    eventlibrary['GTS017'] = {"name": "Getting Dirty", "girls": ["GTS"], "type": EventTypeEnum.OPTIONAL,                   "location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": [[ConditionEnum.EVENT, "GTS001"]]}

    eventlibrary['GTS005'] = {"name": "A Growing Issue", "girls": ["GTS"], "type": EventTypeEnum.OPTIONALCORE,             "location": "schoolplanter",    "priority": PrioEnum.GIRL, "sp": 1,          "obsflags": ["aftertest"],              "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['GTS010'] = {"name": "A Head Above the Class", "girls": ["GTS"], "type": EventTypeEnum.OPTIONALCORE,      "location": "classroom",        "priority": PrioEnum.GIRL, "sp": 2,          "obsflags": ["aftersize2"],             "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}

    eventlibrary['GTSPRG001'] = {"name": "A Blooming Opportunity", "girls": ["GTS", "PRG"], "type": EventTypeEnum.OPTIONAL,"location": "schoolplanter",    "priority": PrioEnum.NONE,                   "obsflags": [],                         "conditions": []}

    #Core
    eventlibrary['PRG001'] = {"name": "Overtime", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,                          "location": "classroom",         "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG002", "obsflags": [],       "conditions": []}
    eventlibrary['PRG002'] = {"name": "A Girl in Gray", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                     "location": "hallway",           "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG003", "obsflags": [],       "conditions": []}
    eventlibrary['PRG003'] = {"name": "Mad Skills", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "hallway",           "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG004", "obsflags": [],       "conditions": []}
    eventlibrary['PRG004'] = {"name": "Nature vs Nurture", "girls": ["PRG"], "type": EventTypeEnum.CORE,                        "location": "hallway",           "priority": PrioEnum.NONE, "sp": 0,     "next": "PRG006", "obsflags": [],       "conditions": []}
    eventlibrary['PRG006'] = {"name": "Legwork", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                  "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG007", "obsflags": [],       "conditions": []}
    eventlibrary['PRG007'] = {"name": "The Koi", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                  "location": "classroom",         "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG008", "obsflags": [],       "conditions": []}
    eventlibrary['PRG008'] = {"name": "Insane in the Headspace", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG009", "obsflags": [],       "conditions": []}
    eventlibrary['PRG009'] = {"name": "Booked Solid", "girls": ["PRG"], "type": EventTypeEnum.CORE,                             "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG011", "obsflags": [],       "conditions": []}
    eventlibrary['PRG011'] = {"name": "Cups and Measurements", "girls": ["PRG"], "type": EventTypeEnum.CORE,                    "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 1,     "next": "PRG012", "obsflags": [],       "conditions": []}
    eventlibrary['PRG012'] = {"name": "Picking the Flower", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                 "location": "campuscenter",      "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG013", "obsflags": [],       "conditions": []}
    eventlibrary['PRG013'] = {"name": "Go for Gold", "girls": ["PRG"],"type": EventTypeEnum.CORE,                                "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG014", "obsflags": [],       "conditions": []}
    eventlibrary['PRG014'] = {"name": "Major Leagues", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "classroom",         "priority": PrioEnum.NONE, "sp": 2,     "next": "PRG015", "obsflags": [],       "conditions": []}
    eventlibrary['PRG015'] = {"name": "Seal of Approval", "girls": ["PRG"], "type": EventTypeEnum.CORE,                          "location": "classroom",        "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG016", "obsflags": [],       "conditions": []}
    eventlibrary['PRG016'] = {"name": "The First Step", "girls": ["PRG"], "type": EventTypeEnum.CORE,                           "location": "classroom",         "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG017", "obsflags": [],       "conditions": []}
    eventlibrary['PRG017'] = {"name": "Full Bloom", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "schoolplanter",     "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG018", "obsflags": [],       "conditions": []}
    eventlibrary['PRG018'] = {"name": "A Cut Above", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "campuscenter",     "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG019", "obsflags": [],       "conditions": []}
    eventlibrary['PRG019'] = {"name": "Cream and Sugar", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,                    "location": "classroom",         "priority": PrioEnum.NONE, "sp": 3,     "next": "PRG020", "obsflags": [],       "conditions": []}
    eventlibrary['PRG020'] = {"name": "R&R", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,                            "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG021", "obsflags": [],       "conditions": []}
    eventlibrary['PRG021'] = {"name": "Back to the Usual", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,            "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG022", "obsflags": [],       "conditions": []}
    eventlibrary['PRG022'] = {"name": "Reality", "girls": ["PRG"], "type": EventTypeEnum.CORE,                              "location": "supermarket",       "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG023", "obsflags": [],       "conditions": []}
    eventlibrary['PRG023'] = {"name": "Healing a Heart", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "library",           "priority": PrioEnum.NONE, "sp": 4,     "next": "PRG024", "obsflags": [],       "conditions": []}
    eventlibrary['PRG024'] = {"name": "Butterflies", "girls": ["PRG"], "type": EventTypeEnum.CORE,                             "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG025", "obsflags": [],       "conditions": []}
    eventlibrary['PRG025'] = {"name": "Heartfire", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "hallway",      "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG026", "obsflags": [],       "conditions": []}
    eventlibrary['PRG026'] = {"name": "That Which Binds Us", "girls": ["PRG"], "type": EventTypeEnum.CORE,                     "location": "hallway",           "priority": PrioEnum.ALL, "sp": 5,      "next": "PRG027", "obsflags": [],       "conditions": []}
    eventlibrary['PRG027'] = {"name": "Rise", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                 "location": "dormPRG",           "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG028", "obsflags": [],       "conditions": []}
    eventlibrary['PRG028'] = {"name": "Two Become One", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "dorminterior",  "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG029", "obsflags": [],       "conditions": []}
    eventlibrary['PRG029'] = {"name": "Procrastination Sensation", "girls": ["PRG"], "type": EventTypeEnum.CORE,         "location": "dormexterior",              "priority": PrioEnum.NONE, "sp": 5,     "next": "PRG0295", "obsflags": [],       "conditions": []}
    eventlibrary['PRG0295'] = {"name": "Double Team", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                      "location": "dormexterior",              "priority": PrioEnum.ALL, "sp": 5,     "next": "PRG030", "obsflags": [],       "conditions": []}
    eventlibrary['PRG030'] = {"name": "Comfort in Chaos", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "dormexterior",           "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG031", "obsflags": [],       "conditions": []}
    eventlibrary['PRG031'] = {"name": "Seared", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "hallway",              "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG032", "obsflags": [],       "conditions": []}
    eventlibrary['PRG032'] = {"name": "The Charm", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG033", "obsflags": [],       "conditions": []}
    eventlibrary['PRG033'] = {"name": "Hanging Clouds", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG034", "obsflags": [],       "conditions": []}
    eventlibrary['PRG034'] = {"name": "Back in the Saddle", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "cookingclassroom",  "priority": PrioEnum.NONE, "sp": 6,     "next": "PRG035", "obsflags": [],       "conditions": []}
    eventlibrary['PRG035'] = {"name": "Dinner for Three", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,                  "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG036", "obsflags": [],       "conditions": []}
    eventlibrary['PRG036'] = {"name": "Fallibility", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,                       "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG037", "obsflags": [],       "conditions": []}
    eventlibrary['PRG037'] = {"name": "Powering Through", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,                  "location": "classroom",         "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG038", "obsflags": [],       "conditions": []}
    eventlibrary['PRG038'] = {"name": "Lessons from the Master", "girls": ["PRG"], "type": EventTypeEnum.CORE,                  "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG039", "obsflags": [],       "conditions": []}
    eventlibrary['PRG039'] = {"name": "Conflicted Interests", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,               "location": "classroom",         "priority": PrioEnum.NONE, "sp": 7,     "next": "PRG040", "obsflags": [],       "conditions": []}
    eventlibrary['PRG040'] = {"name": "Tied Up", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                  "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG041", "obsflags": [],       "conditions": []}
    eventlibrary['PRG041'] = {"name": "Expectation for the Unexpected", "girls": ["PRG", "GTS"], "type": EventTypeEnum.CORE,    "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG042", "obsflags": [],       "conditions": []}
    eventlibrary['PRG042'] = {"name": "Clean Sweep", "girls": ["PRG", "AE"], "type": EventTypeEnum.CORE,                        "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG043", "obsflags": [],       "conditions": []}
    eventlibrary['PRG043'] = {"name": "A Mother's Love", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,                   "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG044", "obsflags": [],       "conditions": []}
    eventlibrary['PRG044'] = {"name": "Spoiling", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                 "location": "classroom",         "priority": PrioEnum.NONE, "sp": 8,     "next": "PRG045", "obsflags": [],       "conditions": []}
    eventlibrary['PRG045'] = {"name": "Vider les Réservoirs", "girls": ["PRG", "WG"], "type": EventTypeEnum.CORE,              "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 9,     "next": "PRG046", "obsflags": [],       "conditions": []}
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
    eventlibrary['PRG057C'] = {"name": "Power of a Protege", "girls": ["PRG"], "type": EventTypeEnum.CORE,                      "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG058", "obsflags": [],       "conditions": []}
    eventlibrary['PRG058'] = {"name": "Girls Gone Fertile", "girls": ["PRG"], "type": EventTypeEnum.CORE,                       "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG059", "obsflags": [],       "conditions": []}
    eventlibrary['PRG059'] = {"name": "Riding the Hormonal Rollercoaster", "girls": ["PRG"], "type": EventTypeEnum.CORE,        "location": "campuscenter",      "priority": PrioEnum.NONE, "sp": 11,    "next": "PRG060", "obsflags": [],       "conditions": []}
    eventlibrary['PRG060'] = {"name": "True or False", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 12,    "next": "PRG061", "obsflags": [],       "conditions": []}
    eventlibrary['PRG061'] = {"name": "Freshly Baked", "girls": ["PRG"], "type": EventTypeEnum.CORE,                            "location": "nurseoffice",       "priority": PrioEnum.NONE, "sp": 12,    "next": "PRG062", "obsflags": [],       "conditions": []}
    eventlibrary['PRG062'] = {"name": "Echoes of Lunacy", "girls": ["PRG"], "type": EventTypeEnum.CORE,                         "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 12,    "next": "PRG063", "obsflags": [],       "conditions": []}
    eventlibrary['PRG063'] = {"name": "Autumn Rains", "girls": ["PRG"], "type": EventTypeEnum.CORE,                             "location": "hallway",           "priority": PrioEnum.NONE, "sp": 12,    "next": "PRG064", "obsflags": [],       "conditions": []}
    eventlibrary['PRG064'] = {"name": "Where the Fairies Play", "girls": ["PRG"], "type": EventTypeEnum.CORE,                   "location": "dormexterior",      "priority": PrioEnum.NONE, "sp": 12,    "next": "PRG065", "obsflags": [],       "conditions": []}
    eventlibrary['PRG065'] = {"name": "All Out", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                  "location": "hallway",           "priority": PrioEnum.NONE, "sp": 12,    "next": "PRG066", "obsflags": [],       "conditions": []}
    eventlibrary['PRG066'] = {"name": "Aida end", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                 "location": "library",           "priority": PrioEnum.NONE, "sp": 12,    "obsflags": [],                         "conditions": []}

    eventlibrary['PRGend_nofather'] = {"name": "Guiding Hand", "girls": ["PRG"], "type": EventTypeEnum.CORE,                    "location": "dorminterior",       "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG027Z'] = {"name": "Guiding Hand", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                      "location": "dorminterior",       "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG028Z'] = {"name": "Head Case", "girls": ["PRG", "BE"], "type": EventTypeEnum.CORE,                         "location": "hallway",           "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG029Z'] = {"name": "Patchwork", "girls": ["PRG"], "type": EventTypeEnum.CORE,                               "location": "hallway",           "priority": PrioEnum.NONE, "sp": 5,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG030Z'] = {"name": "Memoric Gazes", "girls": ["PRG"], "type": EventTypeEnum.CORE,                           "location": "hallway",           "priority": PrioEnum.NONE, "sp": 6,     "obsflags": [],                         "conditions": []}
    eventlibrary['PRG031Z'] = {"name": "Aida end", "girls": ["PRG"], "type": EventTypeEnum.CORE,                                "location": "library",           "priority": PrioEnum.NONE,              "obsflags": [],                         "conditions": []}

    #Optional
    eventlibrary['PRG001b'] = {"name": "Tongue Twister", "girls": ["PRG"], "type": EventTypeEnum.OPTIONAL,                      "location": "schoolexterior",   "priority": PrioEnum.NONE,              "obsflags": ["testday"],                "conditions": [[ConditionEnum.EVENT, "PRG001"]]}
    eventlibrary['PRG005'] = {"name": "Camouflage", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,                       "location": "auditorium",       "priority": PrioEnum.GIRL, "sp": 1,     "obsflags": ["aftertest"],              "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['PRG010'] = {"name": "Buckle Up", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,                        "location": "hallway", "priority": PrioEnum.GIRL, "sp": 2,     "obsflags": ["aftersize2"],             "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['PRG026b'] = {"name": "New Arrival", "girls": ["PRG"], "type": EventTypeEnum.OPTIONALCORE,                        "location": "classroom",        "priority": PrioEnum.ALL,               "obsflags": [],                         "conditions": [[ConditionEnum.TIMEFLAG, "size3"], [ConditionEnum.NOROUTELOCK, "PRG"], [ConditionEnum.NOROUTELOCK, ""]]}
    #Using filler title "New Arrival" for now.

    #Core
    eventlibrary['WG001'] = {"name": "Human Resources", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                  "location": "cafeteria",         "priority": PrioEnum.NONE, "sp": 0,     "next": "WG002", "obsflags": [],                               "conditions": []}
    eventlibrary['WG002'] = {"name": "Good Help is Impossible to Find", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                   "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 0,     "next": "WG003", "obsflags": [],                               "conditions": []}
    eventlibrary['WG003'] = {"name": "Necessity is the Mother of Employment", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                     "location": "cookingclassroom",  "priority": PrioEnum.NONE, "sp": 0,     "next": "WG004", "obsflags": [],                               "conditions": []}
    eventlibrary['WG004'] = {"name": "In the Books", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                      "location": "classroom",        "priority": PrioEnum.NONE, "sp": 0,     "next": "WG005", "obsflags": [],                               "conditions": []}
    eventlibrary['WG005'] = {"name": "What to Expect When You're Expanding", "girls": ["WG"], "type": EventTypeEnum.CORE,                                               "location": "cafeteria",        "priority": PrioEnum.GIRL, "sp": 1,     "next": "WG006", "obsflags": ["aftertest"],                   "conditions": [[ConditionEnum.TIMEFLAG, "testday2"]]}
    eventlibrary['WG006'] = {"name": "A Proud Patron of the Arts", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                 "location": "hallway",          "priority": PrioEnum.NONE, "sp": 1,     "next": "WG007", "obsflags": [],                               "conditions": []}
    eventlibrary['WG007'] = {"name": "Her Other Fluent Language", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 1,     "next": "WG008", "obsflags": [],                               "conditions": []}
    eventlibrary['WG008'] = {"name": "How to Train Your Diva", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                    "location": "musicclassroom",   "priority": PrioEnum.NONE, "sp": 1,     "next": "WG010", "obsflags": [],                               "conditions": []}
    eventlibrary['WG008A'] = {"name": "The Fat Lady Won't Sing", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                         "location": "cafeteria",        "priority": PrioEnum.GIRL, "sp": 1,     "next": "WG010", "obsflags": [],                               "conditions": []}
    eventlibrary['WG010'] = {"name": "ABC: Always Be Clothing", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "cafeteria",        "priority": PrioEnum.GIRL, "sp": 1,     "next": "WG012",  "obsflags": [],                                "conditions": [[ConditionEnum.TIMEFLAG, "size2"]]}
    eventlibrary['WG012'] = {"name": "Risky Business", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 1,     "next": "WG015", "obsflags": [],                                "conditions": []}
    eventlibrary['WG015'] = {"name": "This is the Stealth Section", "girls": ["WG", "AE"], "type": EventTypeEnum.CORE,                                                "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,     "next": "WG016", "obsflags": [],                               "conditions": []}
    eventlibrary['WG016'] = {"name": "Game Time Interrupted", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                            "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 2,     "next": "WG019", "obsflags": [],                               "conditions": []}
    eventlibrary['WG019'] = {"name": "Helpful Muscle", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                            "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 3,     "next": "WG020", "obsflags": [],                               "conditions": []}
    eventlibrary['WG020'] = {"name": "It Can Be Found Anywhere", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                         "location": "classroom",        "priority": PrioEnum.NONE, "sp": 3,     "next": "WG022", "obsflags": [],                              "conditions": []} #\/ disabled due to affection not being very grindable right now
    eventlibrary['WG022'] = {"name": "The Trial of Smarts", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                              "location": "classroom",        "priority": PrioEnum.NONE, "sp": 4,     "next": "WG024", "obsflags": [],                               "conditions": []}
    eventlibrary['WG024'] = {"name": "What's She Got That I Haven't Got More Of?", "girls": ["WG"], "type": EventTypeEnum.CORE,                                       "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 2,     "next": "WG025", "obsflags": [],                               "conditions": []}
    eventlibrary['WG025'] = {"name": "I Like Big...?", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                            "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 3,     "next": "WG026", "obsflags": [],                               "conditions": []}
    eventlibrary['WG026'] = {"name": "The Lady in the Pool", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                             "location": "pool",             "priority": PrioEnum.NONE, "sp": 3,     "next": "WG027", "obsflags": [],                               "conditions": []}
    eventlibrary['WG027'] = {"name": "Interoffice Romance", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                              "location": "hallway",          "priority": PrioEnum.NONE, "sp": 4,     "next": "WG028", "obsflags": [],                               "conditions": []} #"conditions": [[ConditionEnum.AFFECTION, "WG", ConditionEqualityEnum.GREATERTHANEQUALS, 6]]}
    eventlibrary['WG027A'] = {"name": "Second Chance", "girls": ["WG"], "type": EventTypeEnum.OPTIONALCORE,                                                           "location": "cafeteria",        "priority": PrioEnum.GIRL, "sp": 4,     "next": "WG028", "obsflags": [],                               "conditions": [[ConditionEnum.AND, [ConditionEnum.AFFECTION, "WG", ConditionEqualityEnum.GREATERTHANEQUALS, 10], [ConditionEnum.FLAG, "WG027A_unlock"]]]}
    eventlibrary['WG028'] = {"name": "Sick Day", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                                  "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 5,     "next": "WG029", "obsflags": [],                               "conditions": [[ConditionEnum.FLAG, "WG_dating"]]}
    eventlibrary['WG029'] = {"name": "No 'Big Day' Puns, Please", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "WG030", "obsflags": [],                               "conditions": []}
    eventlibrary['WG030'] = {"name": "Who Are the Ad Wizards...", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 4,     "next": "WG031", "obsflags": [],                               "conditions": []}
    eventlibrary['WG031'] = {"name": "Future Prospects", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                 "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "WG033", "obsflags": [],                               "conditions": []}
    eventlibrary['WG033'] = {"name": "Smells Like Team Spirit", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                          "location": "classroom",        "priority": PrioEnum.NONE, "sp": 5,     "next": "WG034", "obsflags": [],                               "conditions": []}
    eventlibrary['WG034'] = {"name": "Styling and Profiling", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                            "location": "town",             "priority": PrioEnum.NONE, "sp": 5,     "next": "WG035", "obsflags": [],                               "conditions": []}
    eventlibrary['WG035'] = {"name": "It's Showtime", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                    "location": "auditorium",       "priority": PrioEnum.NONE, "sp": 6,     "next": "WG036", "obsflags": [],                                "conditions": []}
    eventlibrary['WG036'] = {"name": "A Meeting with the Boss", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                          "location": "auditorium",       "priority": PrioEnum.NONE, "sp": 6,     "next": "WG037", "obsflags": [],                                "conditions": []}
    eventlibrary['WG037'] = {"name": "A Pleasant Day in Pleasant Town", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                  "location": "dorminterior",        "priority": PrioEnum.NONE, "sp": 6,     "next": "WG038", "obsflags": [],                               "conditions": []}
    eventlibrary['WG038'] = {"name": "Beck and Call", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                    "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "WG039", "obsflags": [],                               "conditions": []}
    eventlibrary['WG039'] = {"name": "Helping Hands", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                   "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "WG041", "obsflags": [],                               "conditions": []} # >=20 affection
    eventlibrary['WG041'] = {"name": "Carnival of Delights", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                              "location": "festival",        "priority": PrioEnum.NONE, "sp": 7,     "next": "WG042", "obsflags": [],                               "conditions": []}
    eventlibrary['WG042'] = {"name": "Carnival of Sins", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                 "location": "festival",        "priority": PrioEnum.ALL, "sp": 7,      "next": "WG043", "obsflags": [],                                "conditions": []}
    eventlibrary['WG043'] = {"name": "Pool Sharks", "girls": ["WG", "PRG", "BE", "FMG"], "type": EventTypeEnum.CORE,                                                  "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "WG044", "obsflags": [],                               "conditions": []}
    eventlibrary['WG044'] = {"name": "A Totally Fitting Meeting", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 7,     "next": "WG045", "obsflags": [],                               "conditions": []}
    eventlibrary['WG045'] = {"name": "No Need to Wine", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 8,     "next": "WG046", "obsflags": [],                               "conditions": []}
    eventlibrary['WG046'] = {"name": "Arrival and Unpacking", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                            "location": "schoolfront",      "priority": PrioEnum.NONE, "sp": 8,     "next": "WG047", "obsflags": [],                               "conditions": []}
    eventlibrary['WG047'] = {"name": "Full Coverage", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                             "location": "summer-guestbedroom","priority": PrioEnum.ALL, "sp": 8,    "next": "WG048", "obsflags": [],                               "conditions": []}
    eventlibrary['WG048'] = {"name": "Dinner is Served", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                          "location": "summer-guestbedroom","priority": PrioEnum.ALL, "sp": 8,    "next": "WG049", "obsflags": [],                               "conditions": []}
    eventlibrary['WG049'] = {"name": "Going the Distance", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                       "location": "summer-guestbedroom","priority": PrioEnum.ALL, "sp": 8,    "next": "WG050", "obsflags": [],                               "conditions": []}
    eventlibrary['WG050'] = {"name": "A Feast for the Eyes", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                     "location": "summer-guestbedroom","priority": PrioEnum.ALL, "sp": 8,    "next": "WG051", "obsflags": [],                               "conditions": []}
    eventlibrary['WG051'] = {"name": "Serve's Up!", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                              "location": "summer-beach",     "priority": PrioEnum.ALL, "sp": 8,      "next": "WG052", "obsflags": [],                               "conditions": []}
    eventlibrary['WG052'] = {"name": "Departure", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                        "location": "summer-beach",     "priority": PrioEnum.ALL, "sp": 8,      "next": "WG053", "obsflags": [],                               "conditions": []}
    eventlibrary['WG053'] = {"name": "The Music of the Night", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 9,     "next": "WG054", "obsflags": [],                               "conditions": []}
    eventlibrary['WG054'] = {"name": "Sweet Dreams (Are made of what?)", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                 "location": "cafeteria",        "priority": PrioEnum.NONE, "sp": 9,     "next": "WG055", "obsflags": [],                               "conditions": []}
    eventlibrary['WG055'] = {"name": "Music in the Garden", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                              "location": "schoolplanter",    "priority": PrioEnum.NONE, "sp": 9,     "next": "WG056", "obsflags": [],                               "conditions": []}
    eventlibrary['WG056'] = {"name": "A Sisterly Bond", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                  "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 9,     "next": "WG057", "obsflags": [],                               "conditions": []}
    eventlibrary['WG057'] = {"name": "Chef Boyhairdee", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 10,     "next": "WG059", "obsflags": [],                               "conditions": []}
    eventlibrary['WG059'] = {"name": "Puff Pastry and Pears", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",     "priority": PrioEnum.NONE, "sp": 10,     "next": "WG060", "obsflags": [],                               "conditions": []}
    eventlibrary['WG059S'] = {"name": "A Fattening Proposition", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                         "location": "dormWG",            "priority": PrioEnum.NONE, "sp": 10,     "next": "WG060S", "obsflags": [],                               "conditions": []}
    eventlibrary['WG060'] = {"name": "Bedside Manner", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                  "location": "classroom",        "priority": PrioEnum.NONE, "sp": 10,     "next": "WG061", "obsflags": [],                               "conditions": []}
    eventlibrary['WG060S'] = {"name": "Pushing Bounds and Buttons", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                     "location": "dorminterior",     "priority": PrioEnum.ALL, "sp": 10,     "next": "WG061S", "obsflags": [],                               "conditions": []}
    eventlibrary['WG061'] = {"name": "Bon Appetite", "girls": ["WG", "PRG"], "type": EventTypeEnum.CORE,                                                           "location": "cookingclassroom",     "priority": PrioEnum.NONE, "sp": 10,     "next": "WG062", "obsflags": [],                               "conditions": []}
    eventlibrary['WG061S'] = {"name": "Through Thick and Thicker", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                      "location": "dormWG",            "priority": PrioEnum.ALL, "sp": 10,     "next": "WG062", "obsflags": [],                               "conditions": []}
    eventlibrary['WG061D'] = {"name": "A False Impression", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                           "location": "dorminterior",        "priority": PrioEnum.ALL, "sp": 10,     "next": "WG062", "obsflags": [],                               "conditions": []}
    eventlibrary['WG062'] = {"name": "Breast Friend, Biggest Ally", "girls": ["WG", "BE"], "type": EventTypeEnum.CORE,                                              "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 10,     "next": "WG063", "obsflags": [],                               "conditions": []}
    eventlibrary['WG063'] = {"name": "A Very Unfitting Meeting", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                        "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 10,     "next": "WG064", "obsflags": [],                               "conditions": []}
    eventlibrary['WG064'] = {"name": "The Sorceress and the Seamstress", "girls": ["WG"], "type": EventTypeEnum.CORE,                                              "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 10,     "next": "WG066", "obsflags": [],                               "conditions": []}
    eventlibrary['WG066'] = {"name": "Sister Golden Hair Surmised", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                      "location": "dormexterior",     "priority": PrioEnum.NONE, "sp": 10,     "next": "WG067", "obsflags": [],                               "conditions": []}
    eventlibrary['WG067'] = {"name": "Down to the Letter", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                             "location": "dormWG",             "priority": PrioEnum.NONE, "sp": 10,     "next": "WG068", "obsflags": [],                               "conditions": []}
    eventlibrary['WG068'] = {"name": "The Lady in Waiting", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                             "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 10,     "next": "WG069", "obsflags": [],                               "conditions": []}
    eventlibrary['WG069'] = {"name": "Having a Ball", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                             "location": "dorminterior",      "priority": PrioEnum.NONE, "sp": 10,     "next": "WG070", "obsflags": [],                               "conditions": []}
    eventlibrary['WG070'] = {"name": "The Businessman and the Ballroom", "girls": ["WG"], "type": EventTypeEnum.CORE,                                           "location": "ballroom",      "priority": PrioEnum.ALL, "sp": 10,     "next": "WG071", "obsflags": [],                               "conditions": []}
    eventlibrary['WG071'] = {"name": "Alice end", "girls": ["WG"], "type": EventTypeEnum.CORE,                                                                        "location": "library",          "priority": PrioEnum.NONE, "sp": 10,     "next": "", "obsflags": [],                                     "conditions": []}

    #Optional
    eventlibrary['WG009'] = {"name": "Between a Soft and a Hard Place", "girls": ["WG", "PRG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                "location": "pool",             "priority": PrioEnum.NONE,              "obsflags": [],                "conditions": [[ConditionEnum.EVENT, "WG008"]]}
    eventlibrary['WG011'] = {"name": "True Romance", "girls": ["WG", "PRG"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],               "conditions": [[ConditionEnum.EVENT, "WG008"]]}
    eventlibrary['WG001M'] = {"name": "Practice Makes Passable", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                   "location": "musicclassroom",          "priority": PrioEnum.NONE,              "obsflags": [],           "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG010"], [ConditionEnum.SKILL, "Art", ConditionEqualityEnum.GREATERTHANEQUALS, 3]]]}
    eventlibrary['WG013'] = {"name": "The Elephant In The Room", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                     "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],               "conditions": [[ConditionEnum.EVENT, "WG012"]]}
    eventlibrary['WG014'] = {"name": "Silence Can Be Heavy", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                         "location": "gym",              "priority": PrioEnum.NONE,              "obsflags": [],                "conditions": [[ConditionEnum.EVENT, "WG012"]]}
    eventlibrary['WG017'] = {"name": "All the Tycoons", "girls": ["WG", "PRG"], "type": EventTypeEnum.OPTIONAL,                                                       "location": "cafeteria",        "priority": PrioEnum.NONE,              "obsflags": [],                "conditions": [[ConditionEnum.AND, [ConditionEnum.FLAG, "WG016_testpass"], [ConditionEnum.EVENT, "WG019"]]]}
    eventlibrary['WG018'] = {"name": "Time Management", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                              "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],                "conditions": [[ConditionEnum.EVENT, "WG016"]]}
    eventlibrary['WG002M'] = {"name": "Practice Makes Presentable", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                  "location": "musicclassroom",    "priority": PrioEnum.NONE,              "obsflags": [],              "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG001M"], [ConditionEnum.AND, [ConditionEnum.EVENT, "WG020"], [ConditionEnum.SKILL, "Art", ConditionEqualityEnum.GREATERTHANEQUALS, 6]]]]}
    eventlibrary['WG021'] = {"name": "Mental Defragmentation", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                       "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": [],              "conditions": [[ConditionEnum.EVENT, "WG020"]]}
    eventlibrary['WG023'] = {"name": "Have it All?", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                                 "location": "cafeteria",        "priority": PrioEnum.NONE,              "obsflags": [],              "conditions": [[ConditionEnum.EVENT, "WG022"]]}
    eventlibrary['WG032'] = {"name": "Wardrobe Dysfunction", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                                  "location": "classroom",        "priority": PrioEnum.NONE,              "obsflags": [],              "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG030"], [ConditionEnum.OR, [ConditionEnum.AFFECTION, "WG", ConditionEqualityEnum.GREATERTHAN, 10], [ConditionEnum.AFFECTION, "FMG", ConditionEqualityEnum.GREATERTHAN, 10]]]]}
    eventlibrary['WG040'] = {"name": "The Bigger Picture", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                            "location": "classroom",        "priority": PrioEnum.NONE,             "obsflags": [],              "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG038"], [ConditionEnum.NOEVENT, "WG046"]]]}
    eventlibrary['WG003M'] = {"name": "A So-So Superstar", "girls": ["WG"], "type": EventTypeEnum.OPTIONAL,                                                             "location": "musicclassroom",    "priority": PrioEnum.NONE,              "obsflags": [],              "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG002M"], [ConditionEnum.AND, [ConditionEnum.EVENT, "WG053"], [ConditionEnum.SKILL, "Art", ConditionEqualityEnum.GREATERTHANEQUALS, 10]]]]}
    eventlibrary['WG058'] = {"name": "Silver Screen Starlet", "girls": ["WG", "PRG"], "type": EventTypeEnum.OPTIONAL,                                                  "location": "woods",            "priority": PrioEnum.NONE,              "obsflags": ["size5"],      "conditions": [[ConditionEnum.EVENT, "WG057"]]}
    eventlibrary['WG065'] = {"name": "A Hefty Heist", "girls": ["WG", "PRG", "BE", "FMG"], "type": EventTypeEnum.OPTIONAL,                                            "location": "dorminterior",            "priority": PrioEnum.NONE,              "obsflags": [],      "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG063"], [ConditionEnum.NOEVENT, "WG069"]]]}

    eventlibrary['WGBE001'] = {"name": "So Bad It's Good", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "classroom",        "priority": PrioEnum.NONE,              "obsflags": [],            "conditions": [[ConditionEnum.AND, [ConditionEnum.FLAG, "DormWG_Seen"], [ConditionEnum.NOEVENT, "WG044"]]]}
    eventlibrary['WGBE002'] = {"name": "Fashion Faux Pas", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "schoolexterior",        "priority": PrioEnum.NONE,              "obsflags": [],            "conditions": [[ConditionEnum.AND, [ConditionEnum.EVENT, "WG035"], [ConditionEnum.NOEVENT, "WG044"]]]}
    eventlibrary['WGBE003'] = {"name": "It's a Miracle!", "girls": ["WG", "BE"], "type": EventTypeEnum.OPTIONAL,                                                          "location": "dormWG",        "priority": PrioEnum.NONE,              "obsflags": [],            "conditions": [[ConditionEnum.EVENT, "WG062"]]}
    eventlibrary['WGFMG001'] = {"name": "Afraid of a Little Fun?", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                             "location": "gym",               "priority": PrioEnum.NONE,              "obsflags": [],              "conditions": [[ConditionEnum.AND, [ConditionEnum.NOEVENT, "WG043"], [ConditionEnum.OR, [ConditionEnum.EVENT, "WG032"], [ConditionEnum.EVENT, "WG037"]]]]}
    eventlibrary['WGFMG002'] = {"name": "Tamer of Dragons", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                                   "location": "dorminterior",     "priority": PrioEnum.NONE,              "obsflags": [],                  "conditions": [[ConditionEnum.EVENT, "WG043"]]}
    eventlibrary['WGFMG003'] = {"name": "An Immovable Object", "girls": ["WG", "FMG"], "type": EventTypeEnum.OPTIONAL,                                                 "location": "schoolexterior",     "priority": PrioEnum.NONE,              "obsflags": ["size5"],        "conditions": [[ConditionEnum.EVENT, "WG063"]]}
    eventlibrary['WGGTS001'] = {"name": "Off to a Bad Start", "girls": ["WG", "GTS"], "type": EventTypeEnum.OPTIONAL,                                                 "location": "classroom",        "priority": PrioEnum.NONE,              "obsflags": ["size3"],            "conditions": [[ConditionEnum.EVENT, "WG005"]]}
    eventlibrary['WGGTS002'] = {"name": "Aggressive Expansion", "girls": ["WG", "GTS"], "type": EventTypeEnum.OPTIONAL,                                               "location": "hallway",          "priority": PrioEnum.NONE,              "obsflags": ["size3"],           "conditions": [[ConditionEnum.EVENT, "WG012"]]}
    eventlibrary['WGGTS003'] = {"name": "Delivery Boy Debacle", "girls": ["WG", "GTS"], "type": EventTypeEnum.OPTIONAL,                                               "location": "dormexterior",     "priority": PrioEnum.NONE,              "obsflags": ["size4"],           "conditions": [[ConditionEnum.EVENT, "WG022"]]}
